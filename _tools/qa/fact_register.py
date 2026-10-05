#!/usr/bin/env python3
"""Fact Register (C9): find every time-sensitive fact in the lessons (English master text) and list it in
_System/Fact Register.md with its lesson, kind, date, source and a re-check date.

A sentence counts as time-sensitive when it has
  - "as of …"                                   → kind "dated"
  - a clock time with a place/zone (19:30 UTC+7) → kind "schedule"   (changes with daylight-saving rules)
  - a rule / tax / fee / price word + a number   → kind "rule-cost"
  - a month-year or year from 2024 on + a number → kind "recent"
Historical facts (events before 2024 with no "as of") are skipped: they don't go stale.

Run: python3 _tools/qa/fact_register.py      (re-run after editing lessons; the file is generated)
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "_tools"))
import sync  # noqa: E402

CUR = json.loads((ROOT / "_tools/curriculum.json").read_text(encoding="utf-8"))
OUT = ROOT / "_System/Fact Register.md"
TODAY = date(2026, 10, 4)
MONTHS = {m: i + 1 for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}

RE_ASOF = re.compile(r"\bas of\b", re.I)
RE_CLOCK = re.compile(r"\b\d{1,2}:\d{2}\b")
RE_ZONE = re.compile(r"UTC|Bangkok|New York|London|Frankfurt|Tokyo|\bET\b|\bEDT\b|\bEST\b|Thai time|local time", re.I)
RE_RULE = re.compile(r"\b(tax|taxes|withh?olding|deduct\w*|exempt\w*|treaty|regulat\w*|licen[cs]\w*|SEC|ban|banned|uptick|"
                     r"ThaiESG\w*|RMF|SSF|commission|margin requirement|leverage (cap|limit)|pricing|profit split|"
                     r"trading hours|price alerts|indicators per chart|bars of history|refunded)\b", re.I)
RE_STORY = re.compile(r"\b(price|candle|closes|sweep|drops|rallies|pulls back|entry|stop at|target)\b", re.I)
RE_EXAMPLE = re.compile(r"\b(e\.g\.|for example|suppose|imagine|example|you pay|paying)\b", re.I)
RE_NUM = re.compile(r"\d")
RE_MY = re.compile(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+(20\d\d)\b")
RE_YEAR = re.compile(r"\b(20\d\d)\b")
RE_SRC2 = re.compile(r"\(([A-Z][^()]{1,70}?,\s*(?:\d{1,2}\s)?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+20\d\d)\)")
RE_SRC = re.compile(r"\(([^()]{0,90}?(?:SEC|BLS|BEA|Federal Reserve|\bFed\b|SPIVA|S&P|Vanguard|Revenue Department|IRS|Finance Magnates|S3 Partners|"
                    r"Topstep|FTMO|FPFX|tradingview|set\.or\.th|SET\b|Laotian Times|Asia Frontier|Yahoo|Reuters|Bloomberg|CFTC|FX News Group|"
                    r"report|scorecard|\.com|\.org|\.gov|\.th|disclosure|announcement|notice|Por\.|s\.\d)[^()]{0,90})\)", re.I)
RE_ACC = re.compile(r"\b(?:According to|per|data from|reported by)\s+([A-Z][\w&.\- ]{2,40})")


def clean(s):
    s = re.sub(r"!\[\[[^\]]*\]\]", "", s)
    s = re.sub(r"\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", s)
    s = re.sub(r"[*_`]", "", s)
    s = re.sub(r"^\s*(>\s*)+", "", s)
    s = re.sub(r"^\s*([-*]|\d+\.)\s+", "", s)
    s = re.sub(r"\[!\w+\][-+]?\s*", "", s)
    return re.sub(r"\s+", " ", s).strip()


def sentences(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    out = []
    for raw in text.splitlines():
        line = clean(raw)
        if not line or line.startswith("|---") or line.startswith("#"):
            continue
        if line.startswith("|"):
            out.append(" · ".join(c.strip() for c in line.strip("|").split("|") if c.strip()))
            continue
        out += [p.strip() for p in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(])", line) if len(p.strip()) > 20]
    return out


def fact_date(s):
    my = RE_MY.findall(s)
    if my:
        return max(date(int(y), MONTHS[m.lower()[:3]], 1) for m, y in my)
    ys = [int(y) for y in RE_YEAR.findall(s) if 2000 <= int(y) <= 2030]
    return date(max(ys), 1, 1) if ys else None


def classify(s):
    years = [int(y) for y in RE_YEAR.findall(s)]
    if RE_ASOF.search(s):
        return "dated"
    if RE_CLOCK.search(s) and RE_ZONE.search(s):
        return None if RE_STORY.search(s) else "schedule"   # chart narration with times is not a schedule
    if years and max(years) < 2024:
        return None  # historical: fixed, doesn't go stale
    if RE_RULE.search(s) and RE_NUM.search(s) and not RE_EXAMPLE.search(s):
        return "rule-cost"
    if years and max(years) >= 2024 and RE_NUM.search(re.sub(RE_YEAR, "", s)):
        return "recent"
    return None


def main():
    rows, per = [], {}
    for ph in CUR["phases"]:
        for l in ph["lessons"]:
            p = sync.lesson_path(ph, l)
            if not p.exists():
                continue
            txt = p.read_text(encoding="utf-8")
            txt = re.sub(r"^---\n.*?\n---\n", "", txt, count=1, flags=re.S)
            en = txt.partition("%% TH %%")[0]
            seen = set()
            for s in sentences(en):
                kind = classify(s)
                if not kind or s in seen:
                    continue
                seen.add(s)
                d = fact_date(s)
                src = RE_SRC2.search(s) or RE_SRC.search(s) or RE_ACC.search(s)
                src = src.group(1).strip() if src else ""
                if kind == "schedule":
                    recheck = "each March & Oct/Nov (clock changes) + yearly"
                else:
                    base = d or date(2026, 10, 1)
                    recheck = date(base.year + 1, base.month, 1).strftime("%b %Y")
                # due: a current-state fact (dated / rule-cost) whose re-check date has already passed
                stale = bool(kind in ("dated", "rule-cost") and d and d.year >= 2024 and date(d.year + 1, d.month, 1) <= TODAY)
                rows.append(dict(id=l["id"], stem=p.stem, kind=kind, text=s if len(s) <= 260 else s[:257] + "…",
                                 date=d.strftime("%b %Y") if d else "", src=src, recheck=recheck, stale=stale))
                per[l["id"]] = per.get(l["id"], 0) + 1
    kinds = {k: sum(1 for r in rows if r["kind"] == k) for k in ("dated", "schedule", "rule-cost", "recent")}
    out = ["---", "tags: [system, facts]", "---",
           "# Fact Register · time-sensitive facts",
           "",
           f"> [!note] Generated {TODAY:%d %b %Y} by `_tools/qa/fact_register.py` from the English master text. "
           "Edit the lessons, then re-run; don't edit this table by hand. The **Status** column in your own copy is yours: "
           "tick a row when you have re-checked it against the source.",
           "",
           f"**{len(rows)} facts in {len(per)} lessons** · dated (\"as of\"): {kinds['dated']} · schedules/release times: {kinds['schedule']} · "
           f"rules, taxes, fees & prices: {kinds['rule-cost']} · other recent figures: {kinds['recent']}.",
           "",
           "How to use it:",
           "1. Once a year (and after any big rule change), work down the **Re-check by** column.",
           "2. Schedules (UTC+7 times) shift by one hour when the US or Europe change clocks; check them each March and October/November.",
           "3. Rows marked ⚠ are current-state facts (rules, taxes, fees, \"as of\" figures) whose re-check date has already passed: check them first.",
           "4. *recent* rows are figures and events from 2024 on (reports, prices, company numbers): fixed history once published, but check that newer data hasn't replaced them.",
           "5. The **Source** column is filled when the sentence names one; empty means the source is elsewhere in the lesson or should be added.",
           ""]
    cur = None
    titles = {l["id"]: l["en"] for ph in CUR["phases"] for l in ph["lessons"]}
    for r in rows:
        if r["id"] != cur:
            cur = r["id"]
            stem = r["stem"]
            out += ["", f"## {cur} [[{stem}|{titles[cur]}]]", "", "| Kind | Fact (as written) | Date | Source | Re-check by |", "|---|---|---|---|---|"]
        t = r["text"].replace("|", "/")
        out.append(f"| {r['kind']}{' ⚠' if r['stale'] else ''} | {t} | {r['date']} | {r['src'].replace('|', '/')} | {r['recheck']} |")
    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(rows)} facts in {len(per)} lessons · {kinds} · stale ⚠ {sum(r['stale'] for r in rows)}")
    return rows


if __name__ == "__main__":
    main()
