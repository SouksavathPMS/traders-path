#!/usr/bin/env python3
"""Build the bilingual static site from the Obsidian vault.
Run: python3 _tools/build.py      → writes ../site/
Only lessons with `status: done` are published; others appear as "coming soon".
"""
import html, json, re, shutil
from pathlib import Path

import markdown

import sync  # shares naming rules + regenerates Task Board

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
SRC = ROOT / "_tools/site_src"
CUR = json.loads((ROOT / "_tools/curriculum.json").read_text(encoding="utf-8"))
LANGS = ("en", "th")
CALLOUT_TITLES = {
    "mindset": ("Mindset", "ตั้งหลักความคิด"), "concept": ("Concept", "แนวคิด"),
    "example": ("Example", "ตัวอย่าง"), "action": ("How to act", "ลงมือทำอย่างไร"),
    "why": ("Why it works", "ทำไมจึงได้ผล"), "warning": ("Common mistakes", "ข้อผิดพลาดที่พบบ่อย"),
    "practice": ("Practice", "ฝึกปฏิบัติ"), "key": ("Key takeaway", "ประเด็นสำคัญ"),
    "note": ("Note", "หมายเหตุ"), "todo": ("To do", "สิ่งที่ต้องทำ"), "tip": ("Tip", "เคล็ดลับ"),
    # deep-explanation layer (Style Guide v2)
    "eli5": ("In plain words", "อธิบายแบบง่ายที่สุด"), "analogy": ("Think of it like…", "เปรียบเทียบให้เห็นภาพ"),
    "terms": ("Words you need for this lesson", "คำศัพท์ที่ต้องรู้ในบทนี้"),
    "walkthrough": ("Step-by-step walkthrough", "ไล่ทีละขั้นตอน"),
    "check": ("Check your understanding", "เช็กความเข้าใจ"), "answer": ("Answer", "คำตอบ"),
    "market": ("Across markets", "ในแต่ละตลาด"), "caution": ("Risk warning", "คำเตือนความเสี่ยง"),
}


def esc(s):
    return html.escape(str(s))


def bi(en, th, tag="span"):
    return f'<{tag} class="l-en">{esc(en)}</{tag}><{tag} class="l-th">{esc(th)}</{tag}>'


def lesson_file(ph, l):
    return f"lesson-{l['id'].replace('.', '-')}.html"


# ---------------------------------------------------------------- markdown
def parse_note(path):
    text = path.read_text(encoding="utf-8")
    meta = {}
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
        text = text[m.end():]
    parts = {"en": "", "th": ""}
    chunks = re.split(r"%%\s*(EN|TH)\s*%%", text)
    for i in range(1, len(chunks), 2):
        body = chunks[i + 1].strip()
        body = re.sub(r"^---\s*\n", "", body)
        parts[chunks[i].lower()] = body
    return meta, parts


class Renderer:
    def __init__(self, lang, links):
        self.lang, self.links, self.blocks = lang, links, []

    def token(self, html_block):
        self.blocks.append(html_block)
        return f"\n\nBLOCKTOKEN{len(self.blocks) - 1}X\n\n"

    def inline(self, s):
        # embeds ![[file.svg|caption]]
        def emb(m):
            name, _, cap = m.group(1).partition("|")
            fig = (f'<figure class="fig"><a href="assets/charts/{esc(name)}" target="_blank" title="Open full size">'
                   f'<img src="assets/charts/{esc(name)}" alt="{esc(cap or name)}" loading="lazy"></a>')
            if cap:
                fig += f"<figcaption>{esc(cap)}</figcaption>"
            return self.token(fig + "</figure>")

        s = re.sub(r"!\[\[([^\]]+)\]\]", emb, s)

        def wl(m):
            target, _, label = m.group(1).partition("|")
            label = label or target
            href = self.links.get(target.strip())
            return f"[{label}]({href})" if href else f"*{label}*"

        s = re.sub(r"\[\[([^\]]+)\]\]", wl, s)
        return s

    def quiz(self, body):
        qs, cur = [], None
        for line in body.splitlines():
            line = line.rstrip()
            if line.startswith("Q:"):
                cur = {"q": line[2:].strip(), "opts": [], "e": ""}
                qs.append(cur)
            elif cur and re.match(r"^[-*] ", line):
                cur["opts"].append((line[0] == "*", line[2:].strip()))
            elif cur and line.startswith("E:"):
                cur["e"] = line[2:].strip()
        md = lambda s: markdown.markdown(s).removeprefix("<p>").removesuffix("</p>")
        out = ['<div class="quiz">']
        for n, q in enumerate(qs, 1):
            out.append(f'<div class="q"><p class="q-text"><b>{n}.</b> {md(q["q"])}</p><div class="opts">')
            for ok, o in q["opts"]:
                out.append(f'<button class="opt" data-ok="{int(ok)}">{md(o)}</button>')
            out.append(f'</div><div class="q-exp">{md(q["e"])}</div></div>')
        out.append('<div class="quiz-score"></div></div>')
        return self.token("".join(out))

    def render(self, text):
        text = re.sub(r"%%.*?%%", "", text, flags=re.S)
        # quiz blocks
        text = re.sub(r"```quiz\n(.*?)```", lambda m: self.quiz(m.group(1)), text, flags=re.S)
        # callouts
        lines, out, i = text.split("\n"), [], 0
        while i < len(lines):
            m = re.match(r"^>\s*\[!(\w+)\]([-+]?)\s*(.*)$", lines[i])
            if m:
                kind, fold, title = m.group(1).lower(), m.group(2), m.group(3).strip()
                body = []
                i += 1
                while i < len(lines) and lines[i].startswith(">"):
                    body.append(re.sub(r"^>\s?", "", lines[i]))
                    i += 1
                if not title:
                    t = CALLOUT_TITLES.get(kind, (kind.title(), kind.title()))
                    title = t[1] if self.lang == "th" else t[0]
                inner = Renderer(self.lang, self.links).render("\n".join(body))
                if fold:  # foldable callout ("> [!check]-") -> <details>, closed unless "+"
                    out.append(self.token(
                        f'<details class="callout c-{kind}"{" open" if fold == "+" else ""}><summary class="callout-title">'
                        f'{esc(title)}</summary><div class="callout-body">{inner}</div></details>'))
                else:
                    out.append(self.token(
                        f'<div class="callout c-{kind}"><div class="callout-title">{esc(title)}</div>'
                        f'<div class="callout-body">{inner}</div></div>'))
                continue
            out.append(lines[i])
            i += 1
        # python-markdown needs a blank line before a list (Obsidian doesn't) — add one
        fixed, prev = [], ""
        for l in out:
            is_item = re.match(r"^\s*([-*+]|\d+\.)\s", l)
            prev_item = re.match(r"^\s*([-*+]|\d+\.)\s", prev)
            if is_item and prev.strip() and not prev_item and not prev.lstrip().startswith(("|", "BLOCKTOKEN")):
                fixed.append("")
            fixed.append(l)
            prev = l
        text = self.inline("\n".join(fixed))
        h = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
        h = h.replace("[ ] ", '<input type="checkbox"> ').replace("[x] ", '<input type="checkbox" checked> ')
        for n in range(len(self.blocks) - 1, -1, -1):
            h = h.replace(f"<p>BLOCKTOKEN{n}X</p>", self.blocks[n]).replace(f"BLOCKTOKEN{n}X", self.blocks[n])
        return h


def lid(l):
    """Lesson number shown on the site; checkpoints get a ✓ instead, since they always close their phase."""
    if l["en"].startswith("Checkpoint"):
        return '<span class="lid lid-cp" title="' + l["id"] + '">✓</span>'
    return f'<span class="lid">{l["id"]}</span>'


# ---------------------------------------------------------------- site extras (C6)
TAKEAWAY_HEADS = ("## Key takeaways", "## ประเด็นสำคัญ")


def takeaways(lessons):
    """lesson id -> {lang: one-line takeaway}, read from the 'Key takeaways' table of each phase checkpoint.
    The box on a lesson page repeats that row word for word; no new text is written."""
    out = {}
    for ph, l, meta, parts in lessons:
        if not l["en"].startswith("Checkpoint"):
            continue
        for lang in LANGS:
            body = parts.get(lang, "")
            start = min((body.find(h) for h in TAKEAWAY_HEADS if h in body), default=-1)
            if start < 0:
                continue
            nxt = body.find("\n## ", start + 4)
            block = body[start:nxt if nxt > 0 else None]
            for m in re.finditer(r"^\|\s*(\d+\.\d+)\b[^|\n]*\|([^|\n]+)\|\s*$", block, re.M):
                out.setdefault(m.group(1), {})[lang] = m.group(2).strip()
    return out


def takeaway_box(text, lang):
    title = "สิ่งเดียวที่ต้องจำ" if lang == "th" else "The one thing to remember"
    body = markdown.markdown(text).removeprefix("<p>").removesuffix("</p>")
    return f'<div class="takeaway"><div class="takeaway-title">{title}</div><p>{body}</p></div>'


def slug(s, seen):
    base = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "term"
    k, n = base, 2
    while k in seen:
        k, n = f"{base}-{n}", n + 1
    seen.add(k)
    return k


def load_glossary():
    rows, seen = [], set()
    for line in (ROOT / "_System/Glossary.md").read_text(encoding="utf-8").splitlines():
        if not line.startswith("| ") or line.startswith("| Term"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 4:
            continue
        rows.append(dict(term=cells[0], th=cells[1], meaning=cells[2], phase=cells[3], slug=slug(cells[0], seen)))
    return rows


def glossary_page(rows):
    by_phase = {}
    for r in rows:
        first = re.match(r"\d+", r["phase"])
        by_phase.setdefault(int(first.group()) if first else -1, []).append(r)
    out = [f'<div class="doc gloss-page"><div class="crumbs"><a href="index.html">{bi("Overview", "ภาพรวม")}</a></div>'
           f'<p class="eyebrow">{bi("Reference", "อ้างอิง")}</p><h1>{bi("Glossary", "อภิธานศัพท์")}</h1>'
           f'<p class="lead">{bi(f"{len(rows)} terms used in the course, grouped by the phase where they first appear.", f"คำศัพท์ {len(rows)} คำที่ใช้ในคอร์ส จัดกลุ่มตามเฟสที่ปรากฏครั้งแรก")}'
           f' {bi("Meanings are in English for now.", "คำอธิบายยังเป็นภาษาอังกฤษในตอนนี้")}</p>'
           f'<input class="gloss-filter" type="search" placeholder="Filter… / กรอง…" aria-label="Filter glossary">']
    titles = {ph["n"]: ph["title"] for ph in CUR["phases"]}
    for n in sorted(by_phase):
        t = titles.get(n, {"en": "Other", "th": "อื่น ๆ"})
        out.append(f'<h2 class="gloss-h">{bi("Phase", "เฟส")} {n} · {bi(t["en"], t["th"])}</h2><table class="gloss"><tbody>')
        for r in by_phase[n]:
            out.append(f'<tr id="{r["slug"]}"><td><b>{esc(r["term"])}</b><br><span class="g-th">{esc(r["th"])}</span></td>'
                       f'<td>{esc(r["meaning"])}</td><td class="g-ph">{esc(r["phase"])}</td></tr>')
        out.append("</tbody></table>")
    out.append("</div>")
    return "".join(out)


def pdf_links(ph):
    """Download links to the printable PDFs made by _tools/make_pdfs.py (only if they exist)."""
    files = [(lang, f"pdf/phase-{ph['n']}-{lang}.pdf") for lang in LANGS]
    files = [(lang, f) for lang, f in files if (SITE / f).exists()]
    if not files:
        return ""
    names = {"en": "English", "th": "ไทย"}
    links = " · ".join(f'<a href="{f}" download>{names[lang]} ({(SITE / f).stat().st_size / 1e6:.1f} MB)</a>' for lang, f in files)
    return (f'<div class="practice-box pdf-box"><b>{bi("Printable PDF of this phase", "PDF สำหรับพิมพ์ของเฟสนี้")}</b>'
            f'<span>{links}</span></div>')


CALC_LESSONS = {"0.3", "0.4", "3.2"}  # lessons that link to the position-size calculator (handoff C6)
DRILLS_JSON = ROOT / "_tools/drills/drills.json"


def load_drills():
    return json.loads(DRILLS_JSON.read_text(encoding="utf-8")) if DRILLS_JSON.exists() else {}


def drill_lessons(drills):
    """lesson id -> [(phase, key, title)] so lesson pages can link to their drills."""
    out = {}
    for ph, items in drills.items():
        for d in items:
            out.setdefault(d["lesson"], []).append((ph, d["key"], d["title"]))
    return out


def drill_page(ph, items):
    title = {p["n"]: p["title"] for p in CUR["phases"]}[int(ph)]
    out = [f'<div class="doc drill-page"><div class="crumbs"><a href="drills.html">{bi("Chart drills", "แบบฝึกกราฟ")}</a></div>'
           f'<p class="eyebrow">{bi("Phase", "เฟส")} {ph} · {bi("Practice", "ฝึกฝน")}</p>'
           f'<h1>{bi(title["en"], title["th"])}</h1>'
           f'<p class="lead">{bi("Short chart drills. Each set is 5 random rounds; every answer is checked with the rule from the lesson, and the explanation shows the numbers.", "แบบฝึกกราฟสั้น ๆ ชุดละ 5 รอบแบบสุ่ม ทุกคำตอบตรวจด้วยกฎจากบทเรียน และคำอธิบายแสดงตัวเลข")}'
           f' {bi("Charts are generated examples, not real market data.", "กราฟเป็นตัวอย่างที่สร้างขึ้น ไม่ใช่ข้อมูลตลาดจริง")}</p>']
    for d in items:
        out.append(f'<section class="drill" id="{d["key"]}" data-phase="{ph}" data-key="{d["key"]}">'
                   f'<h2>{bi(d["title"][0], d["title"][1])}</h2>'
                   f'<p class="drill-prompt">{bi(d["prompt"][0], d["prompt"][1])} '
                   f'<a class="drill-lesson" href="lesson-{d["lesson"].replace(".", "-")}.html">{bi("Lesson", "บทเรียน")} {d["lesson"]}</a></p>'
                   f'<div class="drill-stage"></div></section>')
    out.append('</div><script src="assets/drills-data.js"></script><script src="assets/drills.js"></script>')
    return "".join(out)


def drills_hub(drills):
    titles = {p["n"]: p["title"] for p in CUR["phases"]}
    cards = "".join(
        f'<a class="hub-card" href="drills-{ph}.html"><span class="pn">{int(ph):02d}</span>{bi(titles[int(ph)]["en"], titles[int(ph)]["th"], "b")}'
        f'<small>{" · ".join(esc(d["title"][0]) for d in items)}</small></a>' for ph, items in drills.items())
    return (f'<div class="doc"><div class="crumbs"><a href="index.html">{bi("Overview", "ภาพรวม")}</a></div>'
            f'<p class="eyebrow">{bi("Practice", "ฝึกฝน")}</p><h1>{bi("Chart drills", "แบบฝึกกราฟ")}</h1>'
            f'<p class="lead">{bi("Train your eye on the patterns from Phases 1, 2 and 5. Click on the chart or pick an answer; you get the reason and the numbers straight away.", "ฝึกสายตากับรูปแบบจากเฟส 1, 2 และ 5 คลิกบนกราฟหรือเลือกคำตอบ แล้วรับเหตุผลและตัวเลขทันที")}</p>'
            f'<div class="hub-cards">{cards}</div></div>')


def plain(h):
    h = re.sub(r"<(script|style)\b.*?</\1>", " ", h, flags=re.S)
    h = re.sub(r"<[^>]+>", " ", h)
    return re.sub(r"\s+", " ", html.unescape(h)).strip()


# ---------------------------------------------------------------- layout
def sidebar(active_id, published):
    out = ['<nav class="side"><a class="side-home" href="index.html">' + bi("Overview", "ภาพรวม") + "</a>"
           '<div class="side-tools"><a href="glossary.html">' + bi("Glossary", "อภิธานศัพท์") + '</a>'
           '<a href="drills.html">' + bi("Chart drills", "แบบฝึกกราฟ") + '</a>'
           '<a href="calculator.html">' + bi("Position-size calculator", "เครื่องคำนวณขนาดสถานะ") + '</a>'
           '<a href="disclaimer.html">' + bi("Disclaimer", "ข้อจำกัดความรับผิดชอบ") + "</a></div>"]
    for ph in CUR["phases"]:
        open_ = any(l["id"] == active_id for l in ph["lessons"])
        out.append(f'<details class="side-phase"{" open" if open_ else ""}><summary>'
                   f'<span class="pn">{ph["n"]:02d}</span>{bi(ph["title"]["en"], ph["title"]["th"])}</summary><ul>')
        for l in ph["lessons"]:
            cls = "active" if l["id"] == active_id else ""
            label = f'{lid(l)}{bi(l["en"], l["th"])}'
            if l["id"] in published:
                out.append(f'<li class="{cls}" data-id="{l["id"]}"><a href="{lesson_file(ph, l)}">{label}</a></li>')
            else:
                out.append(f'<li class="soon" title="coming soon">{label}</li>')
        out.append("</ul></details>")
    out.append("</nav>")
    return "".join(out)


def page(title, body, active_id=None, published=(), cls=""):
    tpl = (SRC / "page.html").read_text(encoding="utf-8")
    return (tpl.replace("{{TITLE}}", esc(title))
            .replace("{{SITE_EN}}", esc(CUR["site"]["title"]["en"]))
            .replace("{{SITE_TH}}", esc(CUR["site"]["title"]["th"]))
            .replace("{{SIDEBAR}}", sidebar(active_id, published))
            .replace("{{BODY_CLASS}}", cls)
            .replace("{{BODY}}", body))


ICEBERG_LAYERS = [
    ("surface", "#7dd3fc", "Tip · what everyone sees", "ยอดภูเขา · สิ่งที่ทุกคนเห็น"),
    ("shallow", "#38bdf8", "Just under the water", "ใต้ผิวน้ำ"),
    ("mid", "#0ea5e9", "Orderflow", "ออเดอร์โฟลว์"),
    ("deep", "#0369a1", "Options & dealers", "ออปชันและดีลเลอร์"),
    ("abyss", "#1e3a8a", "Quant", "ควอนต์"),
    ("floor", "#172554", "Macro & Wall Street", "มหภาคและวอลล์สตรีท"),
]


PHASE_TOPICS = {
    0: ["Exchanges", "Brokers", "Forex", "Gold", "Stocks", "Nvidia", "Crypto", "News"],
    1: ["Mindset", "Order book", "Candlesticks", "Timeframes"],
    2: ["HH/HL", "BOS", "CHoCH", "S/R", "Supply & Demand"],
    3: ["Position size", "R-multiple", "Expectancy", "Drawdown"],
    4: ["Biases", "Trading plan", "Routine", "Journal", "Tilt"],
    5: ["Liquidity", "ICT", "FVGs", "Order blocks", "QT"],
    6: ["Fibonacci", "Elliott Wave", "Stdv"],
    7: ["AMT", "Volume profile", "Lv2 data", "Footprints", "Heat maps"],
    8: ["Options flow", "Gex", "Gamma exposure", "Flips", "Put walls", "Call walls", "Vex"],
    9: ["Statistics", "Backtesting", "Top ticks", "Python", "Mathematically proven"],
    10: ["Macro economics", "Central banks", "Wall Street", "Valuation", "Portfolio"],
    11: ["Trading plan", "Investment policy"],
}


def ice_card(p):
    tags = "".join(f"<i>{esc(t)}</i>" for t in PHASE_TOPICS.get(p["n"], []))
    return (f'<a class="ice-card" href="phase-{p["n"]}.html" data-phase="{p["n"]}"><span class="pn">{p["n"]:02d}</span>'
            f'{bi(p["title"]["en"], p["title"]["th"], "b")}<span class="tags">{tags}</span><i class="bar"><i></i></i></a>')


def iceberg():
    """Clickable iceberg roadmap. Base phases (1-4) are the 'boat' you need before you dive."""
    ph = {p["layer"]: [] for p in CUR["phases"]}
    for p in CUR["phases"]:
        ph[p["layer"]].append(p)
    rows = []
    base = ph.get("base", [])
    rows.append('<div class="ice-base"><div class="ice-label">' +
                bi("Start here · the foundation every layer stands on", "เริ่มที่นี่ · รากฐานที่ทุกชั้นยืนอยู่") + '</div><div class="ice-cards">')
    for p in base:
        rows.append(ice_card(p))
    rows.append("</div></div><div class=\"ice-sea\">")
    for i, (layer, col, en, th) in enumerate(ICEBERG_LAYERS):
        width = 34 + i * 11
        rows.append(f'<div class="ice-layer" style="--c:{col};--w:{width}%"><div class="ice-shape"></div>'
                    f'<div class="ice-label">{bi(en, th)}</div><div class="ice-cards">')
        for p in ph.get(layer, []):
            rows.append(ice_card(p))
        rows.append("</div></div>")
    rows.append("</div>")
    return '<div class="iceberg">' + "".join(rows) + "</div>"


def main():
    sync.main()
    (SITE / "assets/charts").mkdir(parents=True, exist_ok=True)  # files are overwritten in place
    (SITE / ".nojekyll").touch()  # GitHub Pages: serve files as they are, no Jekyll processing
    for f in (ROOT / "_assets/charts").glob("*.svg"):
        shutil.copy(f, SITE / "assets/charts" / f.name)
    for f in ("style.css", "app.js", "calc.js", "drills.js"):
        shutil.copy(SRC / f, SITE / "assets" / f)

    # collect lessons
    lessons, published, links = [], set(), {}
    for ph in CUR["phases"]:
        links[f"{ph['folder']} - Index"] = f"phase-{ph['n']}.html"
        for l in ph["lessons"]:
            p = sync.lesson_path(ph, l)
            meta, parts = parse_note(p) if p.exists() else ({}, {})
            lessons.append((ph, l, meta, parts))
            if meta.get("status") == "done":
                published.add(l["id"])
                links[p.stem] = lesson_file(ph, l)
    order = [x for x in lessons if x[1]["id"] in published]
    ids = {l["id"]: l for _, l, _, _ in lessons}

    tk = takeaways(lessons)
    search = []
    drills = load_drills()
    dl = drill_lessons(drills)

    # lesson pages
    for k, (ph, l, meta, parts) in enumerate(order):
        prev_ = order[k - 1] if k else None
        next_ = order[k + 1] if k + 1 < len(order) else None
        content, entry = "", {"u": lesson_file(ph, l), "i": l["id"], "t": [l["en"], l["th"]], "h": [], "x": []}
        for lang in LANGS:
            art = Renderer(lang, links).render(parts.get(lang, ""))
            entry["h"].append([plain(x) for x in re.findall(r"<h2[^>]*>(.*?)</h2>", art, re.S)])
            entry["x"].append(plain(art))
            if tk.get(l["id"], {}).get(lang):
                art = art.replace("</h1>", "</h1>" + takeaway_box(tk[l["id"]][lang], lang), 1)
            content += f'<article class="lesson l-{lang}" lang="{lang}">{art}</article>'
        search.append(entry)
        nav = '<div class="pager">'
        nav += (f'<a class="prev" href="{lesson_file(prev_[0], prev_[1])}"><small>{bi("Previous", "ก่อนหน้า")}</small>'
                f'{bi(prev_[1]["en"], prev_[1]["th"], "b")}</a>') if prev_ else "<span></span>"
        nav += (f'<a class="next" href="{lesson_file(next_[0], next_[1])}"><small>{bi("Next", "ถัดไป")}</small>'
                f'{bi(next_[1]["en"], next_[1]["th"], "b")}</a>') if next_ else "<span></span>"
        nav += "</div>"
        head = (f'<div class="crumbs"><a href="phase-{ph["n"]}.html">{bi("Phase", "เฟส")} {ph["n"]} · '
                f'{bi(ph["title"]["en"], ph["title"]["th"])}</a></div>')
        done_btn = (f'<button class="done-btn" data-id="{l["id"]}"><span class="t-todo">{bi("Mark lesson complete", "ทำเครื่องหมายว่าเรียนจบแล้ว")}</span>'
                    f'<span class="t-done">{bi("Completed ✓", "เรียนจบแล้ว ✓")}</span></button>')
        practice = ""
        if l["id"] in CALC_LESSONS:
            practice += (f'<a class="practice-box tool-box" href="calculator.html"><b>{bi("Check the size with the calculator", "ตรวจขนาดไม้ด้วยเครื่องคำนวณ")}</b>'
                         f'<span>{bi("Position-size calculator: forex, gold, stocks, crypto", "เครื่องคำนวณขนาดสถานะ: ฟอเร็กซ์ ทองคำ หุ้น คริปโต")} →</span></a>')
        if l["id"] in dl:
            links_ = "".join(f'<a href="drills-{dp}.html#{dk}">{bi(dt[0], dt[1])} →</a>' for dp, dk, dt in dl[l["id"]])
            practice += (f'<div class="practice-box"><b>{bi("Practise this on a chart", "ฝึกเรื่องนี้บนกราฟ")}</b>{links_}</div>')
        reviewed = ""
        if meta.get("last_reviewed"):
            reviewed = (f'<p class="reviewed">{bi("Last reviewed", "ทบทวนล่าสุด")} {esc(meta["last_reviewed"])} · '
                        f'{bi("Facts that change are marked “as of” a date.", "ข้อมูลที่เปลี่ยนได้ระบุว่า “ณ” วันที่")} '
                        f'<a href="disclaimer.html">{bi("Disclaimer", "ข้อจำกัดความรับผิดชอบ")}</a></p>')
        body = f'<div class="doc" data-lesson="{l["id"]}">{head}{content}{practice}{done_btn}{reviewed}{nav}</div><aside class="toc"></aside>'
        (SITE / lesson_file(ph, l)).write_text(page(f'{l["id"]} {l["en"]}', body, l["id"], published), encoding="utf-8")

    # phase pages
    for ph in CUR["phases"]:
        items = []
        for l in ph["lessons"]:
            if l["id"] in published:
                items.append(f'<li data-id="{l["id"]}"><a href="{lesson_file(ph, l)}">{lid(l)}'
                             f'{bi(l["en"], l["th"])}<span class="chk">✓</span></a></li>')
            else:
                items.append(f'<li class="soon">{lid(l)}{bi(l["en"], l["th"])}'
                             f'<em>{bi("coming soon", "เร็ว ๆ นี้")}</em></li>')
        body = (f'<div class="doc phase-page"><div class="crumbs"><a href="index.html">{bi("Overview", "ภาพรวม")}</a></div>'
                f'<p class="eyebrow">{bi("Phase", "เฟส")} {ph["n"]}</p>'
                f'<h1>{bi(ph["title"]["en"], ph["title"]["th"])}</h1>'
                f'<p class="lead">{bi(ph["goal"]["en"], ph["goal"]["th"])}</p>'
                f'<ol class="lesson-list">{"".join(items)}</ol>'
                + pdf_links(ph)
                + (f'<a class="practice-box" href="drills-{ph["n"]}.html"><b>{bi("Chart drills for this phase", "แบบฝึกกราฟของเฟสนี้")}</b>'
                   f'<span>{" · ".join(esc(d["title"][0]) for d in drills.get(str(ph["n"]), []))}</span></a>' if str(ph["n"]) in drills else "")
                + '</div>')
        (SITE / f"phase-{ph['n']}.html").write_text(
            page(f'Phase {ph["n"]}', body, ph["lessons"][0]["id"] if False else None, published), encoding="utf-8")

    # glossary page + data for tooltips and search
    gl = load_glossary()
    (SITE / "glossary.html").write_text(page("Glossary", glossary_page(gl), None, published, "gloss"), encoding="utf-8")
    (SITE / "assets/glossary.js").write_text(
        "window.GLOSSARY=" + json.dumps([[r["term"], r["th"], r["meaning"], r["phase"], r["slug"]] for r in gl],
                                        ensure_ascii=False, separators=(",", ":")) + ";", encoding="utf-8")
    (SITE / "assets/search-index.js").write_text(
        "window.SEARCH_INDEX=" + json.dumps(search, ensure_ascii=False, separators=(",", ":")) + ";", encoding="utf-8")

    # disclaimer (vault note _System/Disclaimer.md) and calculator
    meta_d, parts_d = parse_note(ROOT / "_System/Disclaimer.md")
    disc = "".join(f'<article class="lesson l-{lang}" lang="{lang}">{Renderer(lang, links).render(parts_d.get(lang, ""))}</article>'
                   for lang in LANGS)
    (SITE / "disclaimer.html").write_text(
        page("Disclaimer", f'<div class="doc"><div class="crumbs"><a href="index.html">{bi("Overview", "ภาพรวม")}</a></div>{disc}</div>',
             None, published), encoding="utf-8")
    (SITE / "calculator.html").write_text(
        page("Position-size calculator", (SRC / "calculator.html").read_text(encoding="utf-8"), None, published), encoding="utf-8")

    # chart drills (data from _tools/drills/make_drills.py)
    if drills:
        (SITE / "assets/drills-data.js").write_text("window.DRILLS=" + json.dumps(drills, ensure_ascii=False, separators=(",", ":")) + ";",
                                                 encoding="utf-8")
        (SITE / "drills.html").write_text(page("Chart drills", drills_hub(drills), None, published), encoding="utf-8")
        for ph, items in drills.items():
            (SITE / f"drills-{ph}.html").write_text(page(f"Chart drills · Phase {ph}", drill_page(ph, items), None, published), encoding="utf-8")

    # home
    total = len(lessons)
    all_ids = json.dumps({str(p["n"]): [l["id"] for l in p["lessons"]] for p in CUR["phases"]})
    home = (SRC / "home.html").read_text(encoding="utf-8")
    home = (home.replace("{{TAGLINE}}", bi(CUR["site"]["tagline"]["en"], CUR["site"]["tagline"]["th"]))
            .replace("{{SITE}}", bi(CUR["site"]["title"]["en"], CUR["site"]["title"]["th"]))
            .replace("{{ICEBERG}}", iceberg())
            .replace("{{STATS}}", f'{len(CUR["phases"])} {bi("phases", "เฟส")} · {total} {bi("lessons", "บทเรียน")} · '
                                  f'{len(published)} {bi("published", "เผยแพร่แล้ว")}')
            .replace("{{PHASE_MAP}}", all_ids))
    (SITE / "index.html").write_text(page("Trader's Path", home, None, published, "home"), encoding="utf-8")
    print(f"site built: {len(published)} lessons published → {SITE}")


if __name__ == "__main__":
    main()
