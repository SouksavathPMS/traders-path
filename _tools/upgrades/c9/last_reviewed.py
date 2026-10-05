"""C9 · add `last_reviewed: YYYY-MM-DD` to every lesson's frontmatter (additive; existing values are kept).
The date is the file's last-modified date at the time this ran (= when the lesson was last written or upgraded).
When you re-read and check a lesson later, change the date by hand."""
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "_tools"))
import sync  # noqa: E402

CUR = json.loads((ROOT / "_tools/curriculum.json").read_text(encoding="utf-8"))
added = kept = 0
for ph in CUR["phases"]:
    for l in ph["lessons"]:
        p = sync.lesson_path(ph, l)
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m or re.search(r"^last_reviewed:", m.group(1), re.M):
            kept += 1
            continue
        d = datetime.date.fromtimestamp(p.stat().st_mtime).isoformat()
        head = re.sub(r"^(status:.*)$", rf"\1\nlast_reviewed: {d}", m.group(1), count=1, flags=re.M)
        p.write_text(text[:m.start(1)] + head + text[m.end(1):], encoding="utf-8")
        added += 1
print(f"last_reviewed added to {added} lessons, {kept} already had one")
