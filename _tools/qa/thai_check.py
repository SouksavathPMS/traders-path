#!/usr/bin/env python3
"""Thai review list (C9): help the owner find Thai text that needs a human read.

Part A (objective) — does the Thai half mirror the English half?
  same number of callouts of each kind, ## sections, figures (.en ↔ .th), **Qn.** questions, and the same numbers.
Part B (heuristic) — lines that *read like* machine translation. Signals (each scores points):
  long untranslated English run (5+ English words outside brackets) · "มัน" used for "it" · passive "ถูก…" for
  neutral verbs · stiff calques ("ในแง่ของ", "ทำให้แน่ใจว่า", "เป็นสิ่งที่", "ซึ่งเป็น", "ได้รับการ", "ของมัน", …) ·
  semicolons · very long run-on lines.
It cannot judge meaning; it only points at lines worth reading. Output: _System/Thai Review List.md

Run: python3 _tools/qa/thai_check.py
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "_tools"))
import sync  # noqa: E402

CUR = json.loads((ROOT / "_tools/curriculum.json").read_text(encoding="utf-8"))
OUT = ROOT / "_System/Thai Review List.md"

CALQUES = {
    "ในแง่ของ": "calque of “in terms of”",
    "ทำให้แน่ใจว่า": "calque of “make sure that”",
    "เป็นสิ่งที่": "“is something that” — usually removable",
    "ซึ่งเป็นสิ่งที่": "“which is something that”",
    "ได้รับการ": "formal passive “has been …”",
    "ของมัน": "“its” as ของมัน — often unnatural",
    "ณ จุดนี้": "calque of “at this point”",
    "สิ่งนี้": "“this thing” — often unnatural",
    "คุณจะต้อง": "“you will have to” — heavy",
    "ในขณะเดียวกัน": "“at the same time” — check if needed",
    "มีแนวโน้มที่จะ": "“tends to” — wordy",
    "เพื่อที่จะ": "“in order to” — wordy",
    "อย่างไรก็ตาม": "“however” — check overuse",
}
PASSIVE = re.compile(r"ถูก(ใช้|เรียก|สร้าง|นับ|ยอมรับ|มอง|ออกแบบ|กำหนด|วาง|แสดง|คำนวณ|พิจารณา|ทำ|เขียน|ตั้ง|ซื้อขาย|บันทึก)")
EN_RUN = re.compile(r"(?:\b[A-Za-z][A-Za-z'’\-]*\b[ ,]+){5,}[A-Za-z]")
NUM = re.compile(r"(?<![0-9A-Za-z])(?<![0-9]\.)[-−+]?\d[\d,]*(?:\.\d+)?%?")  # "ป.161" counts as 161
CALLOUT = re.compile(r"^>\s*\[!(\w+)\]", re.M)


def halves(p):
    t = p.read_text(encoding="utf-8")
    t = re.sub(r"^---\n.*?\n---\n", "", t, count=1, flags=re.S)
    en, _, th = t.partition("%% TH %%")
    return en, th


def strip_brackets(s):
    s = re.sub(r"\([^()]*\)", " ", s)
    s = re.sub(r"`[^`]*`", " ", s)
    s = re.sub(r"!\[\[[^\]]*\]\]|\[\[[^\]]*\]\]", " ", s)
    s = re.sub(r"\*\*[A-Za-z][^*]{0,40}\*\*", " ", s)  # bold English terms are allowed
    return s


def numbers(s):
    s = re.sub(r"!\[\[[^\]]*\]\]|\[\[[^\]]*\]\]", " ", s)
    s = re.sub(r"\(ดู [^)]*\)|\(see [^)]*\)|\*\(see [^)]*\)\*|\*\(ดู [^)]*\)\*", " ", s)
    s = re.sub(r"\bQ\d+\b", " ", s)
    return Counter(n.replace("−", "-").rstrip(",") for n in NUM.findall(s))


# Differences already read by a person and found correct: {lesson id: {number: why}}
KNOWN_OK = {
    "0.1": {"30": "TH says เสียเพิ่ม 30 (lose 30 more) where EN writes −30"},
    "0.7": {"03": "TH writes 03:00 as ตอนตีสาม (3 a.m.)"},
}


def structure(en, th, lid=""):
    issues = []
    ce, ct = Counter(CALLOUT.findall(en)), Counter(CALLOUT.findall(th))
    for k in sorted(set(ce) | set(ct)):
        if ce[k] != ct[k]:
            issues.append(f"callout [!{k}]: EN {ce[k]} vs TH {ct[k]}")
    he, ht = len(re.findall(r"^## ", en, re.M)), len(re.findall(r"^## ", th, re.M))
    if he != ht:
        issues.append(f"## sections: EN {he} vs TH {ht}")
    fe = [f.replace(".en.svg", "") for f in re.findall(r"!\[\[([^\]|]+?\.en\.svg)", en)]
    ft = [f.replace(".th.svg", "") for f in re.findall(r"!\[\[([^\]|]+?\.th\.svg)", th)]
    if fe != ft:
        issues.append(f"figures differ: EN {len(fe)} vs TH {len(ft)}" + (f" (only EN: {', '.join(sorted(set(fe) - set(ft)))})" if set(fe) - set(ft) else ""))
    qe, qt = len(re.findall(r"\*\*Q\d+\.\*\*", en)), len(re.findall(r"\*\*Q\d+\.\*\*", th))
    if qe != qt:
        issues.append(f"questions **Qn.**: EN {qe} vs TH {qt}")
    ne, nt = numbers(en), numbers(th)
    small = {str(i) for i in range(11)}  # "four" in English is often "4" in Thai, so ignore whole numbers 0-10
    # compare which numbers appear, not how often (Thai dates and phrasing repeat numbers differently)
    miss = [n for n in set(ne) - set(nt) if len(n.strip("%-,.")) and n not in small]
    extra = [n for n in set(nt) - set(ne) if len(n.strip("%-,.")) and n not in small]
    ok = KNOWN_OK.get(lid, {})
    miss = [n for n in miss if n not in ok]
    extra = [n for n in extra if n not in ok]
    if miss:
        issues.append("numbers in EN but not TH: " + ", ".join(sorted(miss, key=lambda x: (len(x), x))[:12]) + (" …" if len(miss) > 12 else ""))
    if extra:
        issues.append("numbers in TH but not EN: " + ", ".join(sorted(extra, key=lambda x: (len(x), x))[:12]) + (" …" if len(extra) > 12 else ""))
    return issues


def score_line(line):
    body = re.sub(r"^\s*(>\s*)+", "", line).strip()
    if not body or body.startswith(("|---", "![[", "%%")) or not re.search(r"[฀-๿]", body):
        return 0, []
    pts, why = 0, []
    run = EN_RUN.search(strip_brackets(body))
    if run:
        pts += 2
        why.append(f"English left in: “{run.group(0)[:50]}”")
    n_man = len(re.findall(r"มัน", body))
    if n_man >= 2:
        pts += n_man - 1
        why.append(f"“มัน” ×{n_man}")
    for m in PASSIVE.finditer(body):
        pts += 1
        why.append(f"passive “{m.group(0)}”")
    for k, v in CALQUES.items():
        if k in body:
            pts += 1
            why.append(v)
    if ";" in body:
        pts += 1
        why.append("semicolon")
    if len(body) > 320:
        pts += 1
        why.append(f"very long line ({len(body)} chars)")
    return pts, why


def main():
    out_struct, out_lines, totals = [], [], Counter()
    for ph in CUR["phases"]:
        for l in ph["lessons"]:
            p = sync.lesson_path(ph, l)
            if not p.exists():
                continue
            en, th = halves(p)
            iss = structure(en, th, l["id"])
            if iss:
                out_struct.append((l["id"], p.stem, iss))
            flagged = []
            for ln, line in enumerate(th.splitlines()):
                pts, why = score_line(line)
                if pts >= 2:
                    flagged.append((pts, line.strip(), why))
            flagged.sort(key=lambda x: -x[0])
            totals[l["id"]] = len(flagged)
            if flagged:
                out_lines.append((l["id"], p.stem, flagged))
    doc = ["---", "tags: [system, thai-review]", "---", "# Thai Review List",
           "",
           "> [!note] Generated by `_tools/qa/thai_check.py` (C9, Oct 2026). Re-run after editing; don't edit this list by hand.",
           "> **Part A** is objective: places where the Thai half doesn't mirror the English half. **Part B** is a heuristic: lines that "
           "*may* read like machine translation. Only a Thai reader can judge Part B; many flagged lines will be fine. "
           "Fix in the lesson (minimal edits), then re-run.",
           "",
           f"**Summary:** {len(out_struct)} lessons with mirror differences · {sum(totals.values())} Thai lines flagged in "
           f"{sum(1 for v in totals.values() if v)} lessons.",
           "",
           "## Part A · Mirror check (EN ↔ TH)",
           ""]
    if not out_struct:
        doc.append("No differences found.")
    for lid, stem, iss in out_struct:
        doc.append(f"- **{lid}** [[{stem}]]")
        doc += [f"    - {i}" for i in iss]
    doc += ["", "## Part B · Lines worth a native read", "",
            "Score = number of signals. Highest first; at most 8 lines per lesson.", ""]
    for lid, stem, fl in out_lines:
        doc += [f"### {lid} [[{stem}]] · {len(fl)} line{'s' if len(fl) > 1 else ''}", ""]
        for pts, line, why in fl[:8]:
            short = line if len(line) <= 300 else line[:297] + "…"
            doc.append(f"- [ ] **{pts}** · {'; '.join(why)}")
            doc.append(f"    > {short.lstrip('> ').strip()}")
        doc.append("")
    OUT.write_text("\n".join(doc) + "\n", encoding="utf-8")
    print(f"mirror differences in {len(out_struct)} lessons; {sum(totals.values())} Thai lines flagged in "
          f"{sum(1 for v in totals.values() if v)} lessons → {OUT}")
    return out_struct, out_lines


if __name__ == "__main__":
    main()
