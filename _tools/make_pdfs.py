#!/usr/bin/env python3
"""Printable PDF per phase (C10): one A4 PDF per phase and language → site/pdf/phase-N-en.pdf / phase-N-th.pdf.

Reuses build.py's renderer, so the PDF has exactly the published lesson text: a cover with the lesson list,
then every published lesson starting on a new page. Folded self-checks are printed open; checkpoint quiz
answers are moved to an answer key at the end of that lesson. Light theme, vector figures.

Run: python3 _tools/make_pdfs.py [phase numbers…]     (needs Google Chrome or Chromium; set CHROME=/path to override)
Run it before build.py so the phase pages can link to the PDFs.
"""
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402  (renderer, curriculum, takeaways)
import sync  # noqa: E402

ROOT = build.ROOT
OUT = build.SITE / "pdf"
LABEL = {
    "en": dict(phase="Phase", lessons="Lessons in this phase", key="Answer key", reviewed="Last reviewed",
               note="Education only, not investment advice. Facts marked “as of” a date may have changed; the website has the latest version.",
               made="Printed from the Trader's Path course"),
    "th": dict(phase="เฟส", lessons="บทเรียนในเฟสนี้", key="เฉลย", reviewed="ทบทวนล่าสุด",
               note="เพื่อการศึกษาเท่านั้น ไม่ใช่คำแนะนำการลงทุน ข้อมูลที่ระบุ “ณ” วันที่อาจเปลี่ยนไปแล้ว เว็บไซต์มีฉบับล่าสุด",
               made="พิมพ์จากคอร์ส Trader's Path"),
}

CSS = """
@page { size: A4; margin: 16mm 15mm 16mm 15mm; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
html, body { background: #ffffff; }
body { font-family: Inter, "Noto Sans Thai", "Noto Sans", Sarabun, Thonburi, sans-serif; font-size: 10.4pt; line-height: 1.55; color: #111827; margin: 0; }
html[lang="th"] body { line-height: 1.7; }
a { color: inherit; text-decoration: none; }
.cover { height: 250mm; display: flex; flex-direction: column; justify-content: center; page-break-after: always; }
.cover .brand { font-size: 12pt; font-weight: 700; color: #2563eb; letter-spacing: .08em; text-transform: uppercase; }
.cover h1 { font-size: 30pt; line-height: 1.15; margin: 8mm 0 4mm; }
.cover .goal { font-size: 12.5pt; color: #374151; max-width: 150mm; }
.cover ol { margin-top: 10mm; padding-left: 0; list-style: none; font-size: 11pt; }
.cover li { padding: 1.2mm 0; border-bottom: 0.3pt solid #e5e7eb; }
.cover .lid { display: inline-block; min-width: 12mm; color: #2563eb; font-weight: 700; }
.cover .foot { margin-top: auto; font-size: 8.5pt; color: #6b7280; }
article { page-break-before: always; }
article:first-of-type { page-break-before: auto; }
h1 { font-size: 20pt; line-height: 1.2; margin: 0 0 4mm; }
h1 .num { color: #2563eb; margin-right: 3mm; }
h2 { font-size: 14pt; margin: 7mm 0 2mm; padding-top: 2mm; border-top: 0.6pt solid #d1d5db; page-break-after: avoid; }
h3 { font-size: 12pt; margin: 5mm 0 2mm; page-break-after: avoid; }
p, li { orphans: 3; widows: 3; }
table { width: 100%; border-collapse: collapse; margin: 3mm 0; font-size: 9.2pt; page-break-inside: auto; }
th, td { border: 0.5pt solid #d1d5db; padding: 1.4mm 2mm; text-align: left; vertical-align: top; }
th { background: #f3f4f6; }
tr { page-break-inside: avoid; }
code { font-size: 9pt; background: #f3f4f6; padding: 0 1mm; border-radius: 1mm; }
pre { background: #f3f4f6; padding: 3mm; border-radius: 2mm; white-space: pre-wrap; font-size: 8.6pt; }
.fig { margin: 4mm 0; page-break-inside: avoid; }
.fig img { width: 100%; height: auto; display: block; border-radius: 2mm; }
.fig figcaption { font-size: 8.5pt; color: #6b7280; text-align: center; }
.callout { --cc: #6b7280; border: 0.5pt solid #e5e7eb; border-left: 1.4mm solid var(--cc); background: #fafafa; border-radius: 1.5mm; padding: 2.5mm 3.5mm; margin: 3.5mm 0; page-break-inside: avoid; }
.callout .callout { page-break-inside: auto; }
.callout-title { font-weight: 700; color: var(--cc); margin-bottom: 1mm; display: block; list-style: none; }
.callout-title::-webkit-details-marker { display: none; }
.callout-body > :first-child { margin-top: 0; } .callout-body > :last-child { margin-bottom: 0; }
.c-mindset { --cc: #7c3aed; } .c-concept { --cc: #2563eb; } .c-example { --cc: #0284c7; } .c-action { --cc: #16a34a; }
.c-why { --cc: #d97706; } .c-warning { --cc: #dc2626; } .c-practice { --cc: #0d9488; } .c-key { --cc: #db2777; }
.c-eli5 { --cc: #0284c7; } .c-analogy { --cc: #9333ea; } .c-terms { --cc: #475569; } .c-walkthrough { --cc: #0891b2; }
.c-check, .c-answer { --cc: #65a30d; } .c-market { --cc: #ea580c; } .c-caution { --cc: #e11d48; } .c-tip { --cc: #d97706; }
.c-terms ul { list-style: none; padding-left: 0; }
.takeaway { border: 0.6pt solid #db2777; background: #fdf2f8; border-radius: 1.5mm; padding: 2.5mm 3.5mm; margin: 0 0 4mm; }
.takeaway-title { font-size: 8pt; font-weight: 800; letter-spacing: .08em; text-transform: uppercase; color: #db2777; }
.takeaway p { margin: 1mm 0 0; font-weight: 600; }
.quiz .q { margin: 3mm 0; page-break-inside: avoid; }
.quiz .q-text { font-weight: 600; margin: 0 0 1mm; }
.quiz ol.opts { margin: 0; padding-left: 7mm; list-style: upper-alpha; }
.answer-key { margin-top: 6mm; padding-top: 2mm; border-top: 0.6pt dashed #9ca3af; font-size: 9.2pt; }
.answer-key h3 { margin-top: 0; }
.answer-key li { margin-bottom: 1mm; }
.reviewed { margin-top: 5mm; font-size: 8.5pt; color: #6b7280; }
input[type=checkbox] { width: 3mm; height: 3mm; margin-right: 1.5mm; vertical-align: -0.3mm; }
"""


def chrome():
    for c in (os.environ.get("CHROME"), "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              shutil.which("google-chrome"), shutil.which("google-chrome-stable"), shutil.which("chromium"), shutil.which("chromium-browser")):
        if c and Path(c).exists():
            return c
    raise SystemExit("Chrome/Chromium not found: set CHROME=/path/to/chrome")


def print_quiz(h, lang, key):
    """Turn interactive quiz HTML into a printed list; answers go into `key` (shown at the end of the lesson)."""
    def one_quiz(m):
        out = ['<div class="quiz">']
        for q in re.finditer(r'<div class="q"><p class="q-text">(.*?)</p><div class="opts">(.*?)</div><div class="q-exp">(.*?)</div></div>', m.group(0), re.S):
            opts = re.findall(r'<button class="opt" data-ok="(\d)">(.*?)</button>', q.group(2), re.S)
            letter = next((chr(65 + i) for i, (ok, _) in enumerate(opts) if ok == "1"), "?")
            num = re.search(r"<b>(\d+)\.</b>", q.group(1))
            key.append((num.group(1) if num else str(len(key) + 1), letter, q.group(3)))
            out.append(f'<div class="q"><p class="q-text">{q.group(1)}</p><ol class="opts">'
                       + "".join(f"<li>{o}</li>" for _, o in opts) + "</ol></div>")
        out.append("</div>")
        return "".join(out)
    return re.sub(r'<div class="quiz">.*?<div class="quiz-score"></div></div>', one_quiz, h, flags=re.S)


def phase_html(ph, lessons, tk, lang):
    L = LABEL[lang]
    title = ph["title"][lang]
    items = [(l, meta, parts) for p_, l, meta, parts in lessons if p_ is ph and meta.get("status") == "done"]
    cover = (f'<section class="cover"><div class="brand">Trader\'s Path · {L["phase"]} {ph["n"]}</div>'
             f'<h1>{html.escape(title)}</h1><p class="goal">{html.escape(ph["goal"][lang])}</p>'
             f'<p><b>{L["lessons"]}</b></p><ol>'
             + "".join(f'<li><span class="lid">{"✓" if l["en"].startswith("Checkpoint") else l["id"]}</span>{html.escape(l[lang])}</li>' for l, _, _ in items)
             + f'</ol><p class="foot">{L["made"]} · {date.today():%Y-%m-%d}<br>{L["note"]}</p></section>')
    arts = []
    for l, meta, parts in items:
        h = build.Renderer(lang, {}).render(parts.get(lang, ""))
        h = h.replace('src="assets/charts/', 'src="charts/').replace('href="assets/charts/', 'href="charts/')
        h = h.replace('<details class="callout', '<details open class="callout')
        num = "✓" if l["en"].startswith("Checkpoint") else l["id"]
        h = re.sub(r"<h1>", f'<h1><span class="num">{num}</span>', h, count=1)
        if tk.get(l["id"], {}).get(lang):
            h = h.replace("</h1>", "</h1>" + build.takeaway_box(tk[l["id"]][lang], lang), 1)
        key = []
        h = print_quiz(h, lang, key)
        if key:
            h += (f'<div class="answer-key"><h3>{L["key"]}</h3><ol>'
                  + "".join(f'<li value="{n}"><b>{a}</b> · {e}</li>' for n, a, e in key) + "</ol></div>")
        if meta.get("last_reviewed"):
            h += f'<p class="reviewed">{L["reviewed"]} {html.escape(meta["last_reviewed"])}</p>'
        arts.append(f"<article>{h}</article>")
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8">'
            f'<base href="{(ROOT / "_assets").as_uri()}/">'
            '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Noto+Sans+Thai:wght@400;600;700&display=swap" rel="stylesheet">'
            f"<title>Trader's Path · {L['phase']} {ph['n']}</title><style>{CSS}</style></head><body>{cover}{''.join(arts)}</body></html>")


def main():
    want = {int(x) for x in sys.argv[1:]} or None
    exe = chrome()
    OUT.mkdir(parents=True, exist_ok=True)
    lessons = []
    for ph in build.CUR["phases"]:
        for l in ph["lessons"]:
            p = sync.lesson_path(ph, l)
            meta, parts = build.parse_note(p) if p.exists() else ({}, {})
            lessons.append((ph, l, meta, parts))
    tk = build.takeaways(lessons)
    tmpdir = Path(tempfile.mkdtemp())
    for ph in build.CUR["phases"]:
        if want and ph["n"] not in want:
            continue
        for lang in build.LANGS:
            src = tmpdir / f"phase-{ph['n']}-{lang}.html"
            src.write_text(phase_html(ph, lessons, tk, lang), encoding="utf-8")
            pdf = OUT / f"phase-{ph['n']}-{lang}.pdf"
            subprocess.run([exe, "--headless", "--disable-gpu", "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
                            "--virtual-time-budget=15000", f"--print-to-pdf={pdf}", src.as_uri()],
                           check=True, capture_output=True, timeout=300)
            print(f"{pdf.relative_to(ROOT)}  {pdf.stat().st_size / 1e6:.1f} MB")
    shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == "__main__":
    main()
