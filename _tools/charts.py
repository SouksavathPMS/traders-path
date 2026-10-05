"""Tiny SVG toolkit for Trader's Path: infographics + annotated candlestick charts.
No dependencies. Every figure function takes `lang` ("en"|"th") and returns an SVG string.
"""
import random
from html import escape

FONT = "Inter, 'Noto Sans Thai', Sarabun, Thonburi, 'Sukhumvit Set', 'Segoe UI', Roboto, sans-serif"

C = dict(
    bg="#0b1220", panel="#111a2e", border="#23314f", grid="#1a2540",
    text="#e5ecf6", muted="#8ea0bd", dim="#5b6b88",
    bull="#22c55e", bear="#ef4444", blue="#3b82f6", purple="#a855f7",
    amber="#f59e0b", teal="#14b8a6", pink="#ec4899", white="#ffffff",
)


def tr(lang):
    """t('english', 'ไทย') -> string for the current language."""
    return lambda en, th: th if lang == "th" else en


class SVG:
    def __init__(self, w, h, title=None, subtitle=None, bg=True):
        self.w, self.h = w, h
        self.els = []
        self.defs = set()
        if bg:
            self.els.append(f'<rect width="{w}" height="{h}" rx="16" fill="{C["bg"]}"/>')
        if title:
            self.text(28, 44, title, 24, C["text"], weight=700)
        if subtitle:
            self.text(28, 72, subtitle, 15, C["muted"])

    # ---------- primitives ----------
    def raw(self, s):
        self.els.append(s)

    def rect(self, x, y, w, h, fill="none", stroke=None, sw=1.5, rx=0, opacity=1, dash=None):
        st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.els.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(w,0):.1f}" height="{max(h,0):.1f}" rx="{rx}" '
                        f'fill="{fill}" fill-opacity="{opacity}"{st}{d}/>')

    def line(self, x1, y1, x2, y2, color=C["muted"], sw=1.5, dash=None, opacity=1):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.els.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" '
                        f'stroke-width="{sw}" stroke-opacity="{opacity}"{d} stroke-linecap="round"/>')

    def circle(self, x, y, r, fill=C["blue"], stroke=None, sw=2):
        st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
        self.els.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}"{st}/>')

    def polyline(self, pts, color=C["blue"], sw=2, dash=None, fill="none", opacity=1):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        self.els.append(f'<polyline points="{p}" fill="{fill}" stroke="{color}" stroke-width="{sw}" '
                        f'stroke-opacity="{opacity}" stroke-linejoin="round" stroke-linecap="round"{d}/>')

    def polygon(self, pts, fill, opacity=1, stroke=None):
        st = f' stroke="{stroke}" stroke-width="1.5"' if stroke else ""
        p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        self.els.append(f'<polygon points="{p}" fill="{fill}" fill-opacity="{opacity}"{st}/>')

    def text(self, x, y, s, size=14, color=C["text"], anchor="start", weight=400, italic=False, lh=1.35):
        """Multi-line text: use \\n for line breaks."""
        lines = str(s).split("\n")
        style = ' font-style="italic"' if italic else ""
        tsp = "".join(
            f'<tspan x="{x:.1f}" dy="{0 if i == 0 else size * lh:.1f}">{escape(l)}</tspan>' for i, l in enumerate(lines)
        )
        self.els.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{color}" text-anchor="{anchor}" '
                        f'font-weight="{weight}"{style}>{tsp}</text>')

    def arrow(self, x1, y1, x2, y2, color=C["muted"], sw=2, dash=None):
        mid = "a" + color.strip("#")
        self.defs.add(f'<marker id="{mid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
                      f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{color}"/></marker>')
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.els.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{color}" '
                        f'stroke-width="{sw}"{d} marker-end="url(#{mid})"/>')

    def pill(self, x, y, s, color=C["blue"], size=13, anchor="middle", fg=C["white"]):
        w = max(len(s) * size * 0.58 + 18, 30)
        x0 = x - w / 2 if anchor == "middle" else (x if anchor == "start" else x - w)
        self.rect(x0, y - size - 4, w, size + 12, fill=color, rx=(size + 12) / 2)
        self.text(x0 + w / 2, y + 2, s, size, fg, "middle", 600)

    def card(self, x, y, w, h, title=None, body=None, color=C["blue"], title_size=17, body_size=14, icon=None):
        self.rect(x, y, w, h, fill=C["panel"], stroke=C["border"], rx=12)
        self.rect(x, y, 5, h, fill=color, rx=2)
        ty = y + 30
        if title:
            self.text(x + 20, ty, title, title_size, color, weight=700)
            ty += title_size + 12
        if body:
            self.text(x + 20, ty, body, body_size, C["text"])

    def render(self):
        defs = f"<defs>{''.join(sorted(self.defs))}</defs>" if self.defs else ""
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" '
                f'height="{self.h}" font-family="{FONT}">{defs}{"".join(self.els)}</svg>')


# ---------- candle data ----------
def candles_from_path(pivots, bars, seed=1, vol=0.35, wick=0.5):
    """Build OHLC candles that walk through pivot prices.
    pivots: [p0, p1, p2, ...]  bars: candles per leg (len = len(pivots)-1)
    The candle at each pivot touches the pivot with its wick."""
    rnd = random.Random(seed)
    out = []
    price = pivots[0]
    for leg, n in enumerate(bars):
        a, b = pivots[leg], pivots[leg + 1]
        step = (b - a) / n
        for k in range(n):
            o = price
            c = a + step * (k + 1) + rnd.uniform(-1, 1) * abs(step) * vol
            if k == n - 1:
                c = b - step * 0.25
            body = abs(c - o)
            h = max(o, c) + rnd.uniform(0.05, 1) * wick * (body + abs(step) * 0.3)
            l = min(o, c) - rnd.uniform(0.05, 1) * wick * (body + abs(step) * 0.3)
            if k == n - 1:  # pivot candle tags the pivot
                if b > a:
                    h = b
                else:
                    l = b
            out.append([o, h, l, c])
            price = c
    return out


class CandleChart:
    """Draw candles inside a box of an SVG and annotate by (index, price)."""

    def __init__(self, svg, x, y, w, h, candles, pmin=None, pmax=None, pad=0.08, grid=True, right_space=0):
        self.s, self.x, self.y, self.w, self.h = svg, x, y, w, h
        self.cs = candles
        lo = min(c[2] for c in candles)
        hi = max(c[1] for c in candles)
        r = hi - lo or 1
        self.pmin = pmin if pmin is not None else lo - r * pad
        self.pmax = pmax if pmax is not None else hi + r * pad
        self.n = len(candles)
        self.step = (w - right_space) / self.n
        if grid:
            for i in range(1, 5):
                gy = y + h * i / 5
                svg.line(x, gy, x + w, gy, C["grid"], 1)

    def X(self, i):
        return self.x + self.step * (i + 0.5)

    def Y(self, p):
        return self.y + self.h * (self.pmax - p) / (self.pmax - self.pmin)

    def draw(self, highlight=None, dim=None, width=0.62):
        highlight = highlight or {}
        dim = set(dim or [])
        bw = self.step * width
        for i, (o, h, l, c) in enumerate(self.cs):
            col = C["bull"] if c >= o else C["bear"]
            op = 0.35 if i in dim else 1
            x = self.X(i)
            self.s.line(x, self.Y(h), x, self.Y(l), col, 1.6, opacity=op)
            top, bot = self.Y(max(o, c)), self.Y(min(o, c))
            self.s.rect(x - bw / 2, top, bw, max(bot - top, 1.5), fill=col, rx=1.5, opacity=op)
            if i in highlight:
                self.s.rect(x - bw / 2 - 5, self.Y(h) - 5, bw + 10, self.Y(l) - self.Y(h) + 10,
                            stroke=highlight[i], sw=2, rx=6, dash="5 4")
        return self

    def hline(self, p, label=None, color=C["amber"], i0=0, i1=None, dash="6 5", side="right", size=12):
        x0 = self.X(i0) - self.step / 2
        x1 = self.X(i1 if i1 is not None else self.n - 1) + self.step / 2
        y = self.Y(p)
        self.s.line(x0, y, x1, y, color, 1.6, dash)
        if label:
            if side == "right":
                self.s.text(x1 - 4, y - 7, label, size, color, "end", 600)
            else:
                self.s.text(x0 + 4, y - 7, label, size, color, "start", 600)

    def zone(self, p0, p1, color=C["blue"], label=None, i0=0, i1=None, opacity=0.16, size=12, label_side="left", label_pos="top"):
        x0 = self.X(i0) - self.step / 2
        x1 = self.X(i1 if i1 is not None else self.n - 1) + self.step / 2
        ya, yb = self.Y(max(p0, p1)), self.Y(min(p0, p1))
        self.s.rect(x0, ya, x1 - x0, yb - ya, fill=color, opacity=opacity, stroke=color, sw=1, rx=3)
        if label:
            ly = ya + 16 if label_pos == "top" else (yb + 16 if label_pos == "below" else ya - 6)
            if label_side == "left":
                self.s.text(x0 + 8, ly, label, size, color, weight=600)
            else:
                self.s.text(x1 - 8, ly, label, size, color, "end", 600)

    def label(self, i, p, s, color=C["text"], dy=-12, size=13, anchor="middle", pill=False, dx=0):
        if pill:
            self.s.pill(self.X(i) + dx, self.Y(p) + dy, s, color, size)
        else:
            self.s.text(self.X(i) + dx, self.Y(p) + dy, s, size, color, anchor, 700)

    def path(self, pts, color=C["blue"], sw=2, dash=None, dots=False):
        xy = [(self.X(i), self.Y(p)) for i, p in pts]
        self.s.polyline(xy, color, sw, dash)
        if dots:
            for x, y in xy:
                self.s.circle(x, y, 4, color)

    def arrow(self, i0, p0, i1, p1, color=C["text"], sw=2, dash=None):
        self.s.arrow(self.X(i0), self.Y(p0), self.X(i1), self.Y(p1), color, sw, dash)

    def high(self, i):
        return self.cs[i][1]

    def low(self, i):
        return self.cs[i][2]
