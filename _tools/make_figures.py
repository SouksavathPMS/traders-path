#!/usr/bin/env python3
"""Generate every figure (EN + TH) into _assets/charts/.
Figures live in _tools/figures/pN.py as FIGURES = {"name": fn(lang) -> svg}.
Run: python3 _tools/make_figures.py [p1 p2 ...]
"""
import importlib, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "_tools"))
OUT = ROOT / "_assets/charts"
OUT.mkdir(parents=True, exist_ok=True)

mods = sys.argv[1:] or sorted(p.stem for p in (ROOT / "_tools/figures").glob("p*.py"))
count = 0
for m in mods:
    mod = importlib.import_module(f"figures.{m}")
    for name, fn in mod.FIGURES.items():
        for lang in ("en", "th"):
            (OUT / f"{name}.{lang}.svg").write_text(fn(lang), encoding="utf-8")
            count += 1
print(f"wrote {count} svg files to {OUT}")
