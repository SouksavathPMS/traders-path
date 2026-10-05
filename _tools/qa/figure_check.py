#!/usr/bin/env python3
"""Figure QA (C9): render every SVG in _assets/charts in headless Chrome, measure each <text> with getBBox(),
and report text that (a) runs outside the figure or (b) overlaps another text label.

Run: python3 _tools/qa/figure_check.py [name-prefix ...]   → prints a report and writes _tools/qa/figure_report.json
Needs Google Chrome (macOS path below).
"""
import html
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHARTS = ROOT / "_assets/charts"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT = Path(__file__).resolve().parent / "figure_report.json"

JS = r"""
(function(){
  var res = [];
  document.querySelectorAll('div.f').forEach(function(d){
    var svg = d.querySelector('svg'); if (!svg) return;
    var vb = svg.viewBox.baseVal, W = vb.width, H = vb.height, boxes = [];
    svg.querySelectorAll('text').forEach(function(t){
      var b; try { b = t.getBBox(); } catch(e) { return; }
      if (!b.width || !t.textContent.trim()) return;
      boxes.push({x:b.x, y:b.y, w:b.width, h:b.height, s:t.textContent.trim().slice(0,60)});
    });
    boxes.forEach(function(b){
      if (b.x < -1 || b.y < -1 || b.x + b.w > W + 1 || b.y + b.h > H + 1)
        res.push({f:d.id, k:'overflow', s:b.s, d:Math.round(Math.max(-b.x, -b.y, b.x+b.w-W, b.y+b.h-H))});
    });
    for (var i=0;i<boxes.length;i++) for (var j=i+1;j<boxes.length;j++){
      var a=boxes[i], c=boxes[j];
      var ix = Math.min(a.x+a.w, c.x+c.w) - Math.max(a.x, c.x), iy = Math.min(a.y+a.h, c.y+c.h) - Math.max(a.y, c.y);
      if (ix <= 0 || iy <= 0) continue;
      var small = Math.min(a.w*a.h, c.w*c.h), frac = ix*iy/small;
      if (frac > 0.25 && iy > 4) res.push({f:d.id, k:'overlap', s:a.s + '  ⟷  ' + c.s, d:Math.round(frac*100)});
    }
  });
  var pre = document.createElement('pre'); pre.id = 'out'; pre.textContent = JSON.stringify(res); document.body.appendChild(pre);
})();
"""


def main():
    pref = sys.argv[1:]
    files = sorted(p for p in CHARTS.glob("*.svg") if not pref or any(p.name.startswith(x) for x in pref))
    parts = ['<!doctype html><meta charset="utf-8"><body>']
    for p in files:
        svg = p.read_text(encoding="utf-8")
        parts.append(f'<div class="f" id="{html.escape(p.stem)}">{svg}</div>')
    parts.append(f"<script>{JS}</script></body>")
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as tmp:
        tmp.write("".join(parts))
    dom = subprocess.run([CHROME, "--headless", "--disable-gpu", "--virtual-time-budget=20000", "--dump-dom", f"file://{tmp.name}"],
                         capture_output=True, text=True, timeout=600).stdout
    m = re.search(r'<pre id="out">(.*?)</pre>', dom, re.S)
    res = json.loads(html.unescape(m.group(1))) if m else []
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    figs = sorted({r["f"] for r in res})
    print(f"checked {len(files)} svg · {len(res)} issues in {len(figs)} figures")
    for r in res:
        print(f"  {r['f']:40s} {r['k']:8s} {r['d']:>4}  {r['s']}")


if __name__ == "__main__":
    main()
