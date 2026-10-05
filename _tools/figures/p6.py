"""Phase 6 figures: Fibonacci, Elliott Wave & Standard Deviation."""
import math
import random
from charts import SVG, CandleChart, C, tr
from figures.p2 import walk, extend, panel

FIGURES = {}


def fig(fn):
    FIGURES["p6-" + fn.__name__.replace("_", "-")] = fn
    return fn


RET = [(0.236, C["dim"]), (0.382, C["teal"]), (0.5, C["amber"]), (0.618, C["bull"]), (0.786, C["purple"])]


class Plot:
    """Simple price->pixel mapper for line diagrams inside a box."""

    def __init__(self, s, x, y, w, h, n, lo, hi):
        self.s, self.x, self.y, self.w, self.h, self.n, self.lo, self.hi = s, x, y, w, h, n, lo, hi

    def X(self, i):
        return self.x + self.w * i / self.n

    def Y(self, p):
        return self.y + self.h * (self.hi - p) / (self.hi - self.lo)

    def path(self, pts, color=C["text"], sw=2.5, dash=None):
        self.s.polyline([(self.X(i), self.Y(p)) for i, p in pts], color, sw, dash)

    def label(self, i, p, txt, color, up=True, size=14):
        self.s.circle(self.X(i), self.Y(p), 4, color)
        self.s.text(self.X(i), self.Y(p) + (-12 if up else 24), txt, size, color, "middle", 700)


# Ideal impulse + correction: 0 1 2 3 4 5 A B C
EW = [100, 110, 103.82, 120.0, 113.82, 123.82, 118.0, 121.2, 115.4]
EW_X = [0, 2, 3.2, 6, 7.2, 9, 10.3, 11.2, 12.8]
EW_L = ["0", "1", "2", "3", "4", "5", "A", "B", "C"]


# ---------------------------------------------------------------- 6.1
@fig
def fib_retrace(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Fibonacci retracements: how deep is the pullback?", "ฟีโบนัชชีรีเทรซเมนต์: การย่อลึกแค่ไหน?"),
            t("Draw from the swing low to the swing high (uptrend). Levels show % of the leg given back.",
              "ลากจาก Swing Low ไป Swing High (ขาขึ้น) ระดับต่าง ๆ บอก % ของขาที่ถูกคืนไป"))
    piv = [100, 120, 107.64, 126]
    cs, idx = walk(piv, [9, 6, 7], seed=81)
    panel(s, 28, 90, 904, 390)
    ch = CandleChart(s, 40, 115, 640, 340, cs, pmin=97, pmax=128, grid=False)
    lo, hi = cs[idx[0]][2] if False else 100, 120
    i0 = 0
    for r, col in RET:
        p = hi - r * (hi - lo)
        ch.hline(p, f"{r * 100:.1f}%  {p:.2f}", col, i0, None, "4 4", side="right", size=12)
    ch.hline(hi, "0%  120.00", C["muted"], i0, None, "2 4", side="left", size=12)
    ch.hline(lo, "100%  100.00", C["muted"], i0, None, "2 4", side="right", size=12)
    ch.draw(highlight={idx[2]: C["bull"]})
    ch.label(idx[2], cs[idx[2]][2], t("turns at 61.8%", "กลับตัวที่ 61.8%"), C["bull"], dy=26, size=12)
    rows = [
        ("23.6%", t("shallow: very strong trend", "ตื้น: เทรนด์แรงมาก")),
        ("38.2%", t("normal pullback in a strong trend", "การย่อปกติในเทรนด์แรง")),
        ("50%", t("equilibrium (5.3), not a Fib ratio", "จุดสมดุล (5.3) ไม่ใช่อัตราส่วนฟีโบ")),
        ("61.8%", t("the 'golden' level; deep, common", "ระดับ 'ทองคำ' ลึก พบบ่อย")),
        ("78.6%", t("very deep; last line before failure", "ลึกมาก ด่านสุดท้ายก่อนล้มเหลว")),
    ]
    cols = [C["dim"], C["teal"], C["amber"], C["bull"], C["purple"]]
    for k, ((lv, txt), col) in enumerate(zip(rows, cols)):
        y = 130 + k * 64
        s.text(760, y, lv, 16, col, weight=700)
        s.text(760, y + 22, txt, 12, C["muted"])
    s.text(760, 455, t("62–79% = the OTE (5.3)", "62–79% = OTE (5.3)"), 13, C["blue"], weight=700)
    return s.render()


@fig
def fib_extension(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Fibonacci extensions: where might the next leg end?", "ฟีโบนัชชีเอกซ์เทนชัน: ขาถัดไปน่าจะจบตรงไหน?"),
            t("Project the first leg (A→B) from the pullback low (C). Targets, not predictions.",
              "ฉายขาแรก (A→B) จากจุดต่ำของการย่อ (C) เป็นเป้าหมาย ไม่ใช่คำทำนาย"))
    A, B, Cc = 100, 120, 107.64
    piv = [A, B, Cc, 127.9, 124.6, 140.2]
    cs, idx = walk(piv, [9, 6, 7, 3, 6], seed=82)
    panel(s, 28, 90, 904, 390)
    ch = CandleChart(s, 40, 115, 640, 340, cs, pmin=97, pmax=143, grid=False)
    leg = B - A
    for r, col in ((1.0, C["teal"]), (1.272, C["amber"]), (1.618, C["bull"])):
        p = Cc + r * leg
        ch.hline(p, f"{r:g} × AB  {p:.1f}", col, idx[2], None, "4 4", side="left", size=12)
    ch.draw()
    for k, name in ((0, "A"), (1, "B"), (2, "C")):
        up = k == 1
        ch.label(idx[k], cs[idx[k]][1] if up else cs[idx[k]][2], name, C["text"], dy=-12 if up else 24, size=15)
    ch.path([(idx[0], A), (idx[1], B)], C["blue"], 1.5, "3 3")
    s.card(700, 110, 220, 170, t("Projection", "การฉาย"),
           t("C + 1.0 × AB = 127.6\nC + 1.272 × AB = 133.1\nC + 1.618 × AB = 140.0\n(AB = 20, C = 107.6)",
             "C + 1.0 × AB = 127.6\nC + 1.272 × AB = 133.1\nC + 1.618 × AB = 140.0\n(AB = 20, C = 107.6)"), C["teal"], 16, 13)
    s.card(700, 294, 220, 170, t("How to use", "วิธีใช้"),
           t("Take partials at 1.0,\ntrail toward 1.618.\nStrongest when an\nextension lines up with\nBSL or an HTF level.", "ปิดบางส่วนที่ 1.0\nเลื่อน Stop ไปทาง 1.618\nแข็งแรงที่สุดเมื่อตรงกับ\nBSL หรือระดับ HTF"), C["amber"], 16, 13)
    return s.render()


# ---------------------------------------------------------------- 6.2
@fig
def wave_structure(lang):
    t = tr(lang)
    s = SVG(960, 480, t("Elliott Wave: five waves with the trend, three against", "Elliott Wave: ห้าคลื่นตามเทรนด์ สามคลื่นสวนเทรนด์"),
            t("Motive waves (1, 3, 5) push; corrective waves (2, 4) and the A-B-C correction rest.",
              "คลื่นขับเคลื่อน (1, 3, 5) ดันไปข้างหน้า คลื่นปรับฐาน (2, 4) และ A-B-C พักตัว"))
    panel(s, 28, 90, 904, 370)
    P = Plot(s, 70, 140, 600, 280, 13, 97, 126)
    s.rect(P.X(0), 120, P.X(9) - P.X(0), 320, fill=C["bull"], opacity=0.06, rx=6)
    s.rect(P.X(9), 120, P.X(12.8) - P.X(9), 320, fill=C["bear"], opacity=0.06, rx=6)
    s.text((P.X(0) + P.X(9)) / 2, 138, t("IMPULSE (5 waves)", "แรงส่ง (5 คลื่น)"), 14, C["bull"], "middle", 700)
    s.text((P.X(9) + P.X(12.8)) / 2, 138, t("CORRECTION (3)", "ปรับฐาน (3)"), 14, C["bear"], "middle", 700)
    pts = list(zip(EW_X, EW))
    P.path(pts, C["text"], 2.8)
    for k, (i, p) in enumerate(pts):
        up = k == 0 or EW[k] > EW[k - 1]
        col = C["bull"] if EW_L[k] in "135" else (C["bear"] if EW_L[k] in "24ABC" else C["muted"])
        P.label(i, p, EW_L[k], col, up=up if k else False)
    notes = [
        (C["bull"], "1", t("early buyers; few believe it", "ผู้ซื้อกลุ่มแรก ยังไม่ค่อยมีใครเชื่อ")),
        (C["bear"], "2", t("deep doubt; often 50–61.8%", "ความสงสัยลึก มักย่อ 50–61.8%")),
        (C["bull"], "3", t("the crowd joins; usually longest", "ฝูงชนเข้าร่วม มักยาวที่สุด")),
        (C["bear"], "4", t("pause; often ~38.2%", "พักตัว มักย่อ ~38.2%")),
        (C["bull"], "5", t("late buyers; momentum fades", "ผู้ซื้อกลุ่มท้าย โมเมนตัมลดลง")),
        (C["bear"], "A-B-C", t("correction of the whole move", "การปรับฐานของทั้งขา")),
    ]
    for k, (col, w, txt) in enumerate(notes):
        y = 140 + k * 50
        s.text(700, y, w, 16, col, weight=700)
        s.text(760, y, txt, 13, C["text"])
    return s.render()


@fig
def wave_fractal(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Waves are fractal: each wave is made of smaller waves", "คลื่นเป็น Fractal: แต่ละคลื่นประกอบด้วยคลื่นที่เล็กกว่า"),
            t("Motive waves subdivide into 5; corrective waves into 3. Same pattern, every timeframe.",
              "คลื่นขับเคลื่อนแบ่งย่อยเป็น 5 คลื่นปรับฐานแบ่งย่อยเป็น 3 รูปแบบเดิมในทุกไทม์เฟรม"))
    panel(s, 28, 90, 904, 360)
    P = Plot(s, 70, 130, 820, 280, 9, 98, 125)

    def sub5(i0, p0, i1, p1):
        d, w = p1 - p0, i1 - i0
        fr = [(0, 0), (0.2, 0.32), (0.3, 0.2), (0.62, 0.78), (0.74, 0.64), (1, 1)]
        return [(i0 + a * w, p0 + b * d) for a, b in fr]

    def sub3(i0, p0, i1, p1):
        d, w = p1 - p0, i1 - i0
        fr = [(0, 0), (0.4, 0.62), (0.6, 0.38), (1, 1)]
        return [(i0 + a * w, p0 + b * d) for a, b in fr]

    main = list(zip(EW_X[:6], EW[:6]))
    P.path(main, C["dim"], 7)
    detail = []
    for k in range(5):
        (i0, p0), (i1, p1) = main[k], main[k + 1]
        seg = sub5(i0, p0, i1, p1) if k % 2 == 0 else sub3(i0, p0, i1, p1)
        detail += seg if not detail else seg[1:]
    P.path(detail, C["text"], 2)
    for k, (i, p) in enumerate(main):
        if k:
            up = EW[k] > EW[k - 1]
            P.label(i, p, f"({EW_L[k]})", C["bull"] if k % 2 else C["bear"], up=up, size=15)
    i0, p0 = main[2]
    i1, p1 = main[3]
    sub = sub5(i0, p0, i1, p1)
    for k, (i, p) in enumerate(sub[1:], 1):
        s.text(P.X(i) + 10, P.Y(p) + (14 if k % 2 == 0 else -4), ["", "i", "ii", "iii", "iv", "v"][k], 12, C["amber"], weight=700)
    s.text(70, 432, t("Thick grey = one larger-degree impulse (1)-(5). Thin white = its smaller waves. Wave (3) shown with sub-waves i-v.",
                      "เส้นเทาหนา = แรงส่งระดับใหญ่ (1)-(5) เส้นขาวบาง = คลื่นย่อย คลื่น (3) แสดงคลื่นย่อย i-v"), 12, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 6.3
@fig
def ew_rules(lang):
    t = tr(lang)
    s = SVG(960, 500, t("The three unbreakable rules", "กฎ 3 ข้อที่ห้ามละเมิด"),
            t("Break one and the count is wrong. Re-label, don't argue.", "ละเมิดข้อเดียว การนับก็ผิด นับใหม่ อย่าเถียงกับตลาด"))
    specs = [
        (t("1 · Wave 2 never goes below the start of wave 1", "1 · คลื่น 2 ไม่ต่ำกว่าจุดเริ่มคลื่น 1"),
         [100, 110, 103.8, 120], [100, 110, 98.5, 112], 0, 100),
        (t("2 · Wave 3 is never the shortest of 1, 3, 5", "2 · คลื่น 3 ไม่เคยสั้นที่สุดใน 1, 3, 5"),
         [100, 110, 104, 120, 114, 124], [100, 110, 104, 111.5, 107, 121], 1, None),
        (t("3 · Wave 4 never enters wave 1's territory", "3 · คลื่น 4 ไม่เข้าเขตของคลื่น 1"),
         [100, 110, 104, 120, 114, 124], [100, 110, 104, 120, 108.5, 122], 2, 110),
    ]
    for k, (head, good, bad, kind, lvl) in enumerate(specs):
        y = 92 + k * 132
        s.rect(28, y, 904, 120, fill=C["panel"], stroke=C["border"], rx=12)
        s.text(46, y + 30, head, 16, C["text"], weight=700)
        for j, (path, ok) in enumerate(((good, True), (bad, False))):
            x0 = 520 + j * 210
            col = C["bull"] if ok else C["bear"]
            P = Plot(s, x0, y + 18, 170, 92, len(path) - 1, 97, 125)
            if lvl:
                s.line(x0 - 6, P.Y(lvl), x0 + 176, P.Y(lvl), C["amber"], 1.2, "3 3")
            P.path(list(enumerate(path)), col, 2.2)
            s.text(x0 + 192, y + 64, "✓" if ok else "✗", 20, col, "start", 700)
        expl = [t("If it does, it was not wave 2: the 'impulse' failed.", "ถ้าต่ำกว่า มันไม่ใช่คลื่น 2: 'แรงส่ง' ล้มเหลว"),
                t("Measure in price. If 3 is shortest, relabel.", "วัดเป็นราคา ถ้าคลื่น 3 สั้นสุด ให้นับใหม่"),
                t("No overlap with wave 1's high (except diagonals).", "ห้ามซ้อนจุดสูงของคลื่น 1 (ยกเว้น Diagonal)")][kind]
        s.text(46, y + 64, expl, 13, C["muted"])
    return s.render()


@fig
def ew_guidelines(lang):
    t = tr(lang)
    s = SVG(960, 480, t("Guidelines: what usually happens (not always)", "แนวทาง: สิ่งที่มักเกิดขึ้น (ไม่เสมอไป)"),
            t("Rules invalidate a count. Guidelines rank which count is more likely.", "กฎใช้ตัดการนับทิ้ง แนวทางใช้จัดอันดับว่าการนับไหนน่าจะเป็นมากกว่า"))
    panel(s, 28, 90, 520, 370)
    P = Plot(s, 60, 140, 460, 280, 9, 97, 127)
    pts = list(zip(EW_X[:6], EW[:6]))
    i1, p1 = pts[1]
    i3, p3 = pts[3]
    i2, p2 = pts[2]
    slope = (p3 - p1) / (i3 - i1)
    s.line(P.X(0), P.Y(p1 - slope * (i1 - 0)), P.X(9.5), P.Y(p1 + slope * (9.5 - i1)), C["blue"], 1.3, "5 4")
    s.line(P.X(0), P.Y(p2 - slope * (i2 - 0)), P.X(9.5), P.Y(p2 + slope * (9.5 - i2)), C["blue"], 1.3, "5 4")
    P.path(pts, C["text"], 2.6)
    for k, (i, p) in enumerate(pts):
        if k:
            P.label(i, p, EW_L[k], C["bull"] if k % 2 else C["bear"], up=EW[k] > EW[k - 1])
    s.text(70, 440, t("Channel: line through 1-3, parallel through 2 → wave 5 target zone",
                      "ช่องราคา: เส้นผ่าน 1-3 เส้นขนานผ่าน 2 → โซนเป้าหมายคลื่น 5"), 12, C["blue"])
    items = [
        (C["bull"], t("Wave 3 ≈ 1.618 × wave 1", "คลื่น 3 ≈ 1.618 × คลื่น 1"), t("often the longest, strongest leg", "มักเป็นขาที่ยาวและแรงที่สุด")),
        (C["teal"], t("Wave 2 ≈ 50–61.8% of 1", "คลื่น 2 ≈ 50–61.8% ของ 1"), t("deep, sharp correction", "ปรับฐานลึกและแหลม")),
        (C["amber"], t("Wave 4 ≈ 38.2% of 3", "คลื่น 4 ≈ 38.2% ของ 3"), t("shallow, sideways correction", "ปรับฐานตื้นและออกข้าง")),
        (C["purple"], t("Alternation", "การสลับรูปแบบ"), t("if 2 is sharp, 4 is usually flat (and vice versa)", "ถ้าคลื่น 2 แหลม คลื่น 4 มักแบน (และกลับกัน)")),
        (C["pink"], t("Wave 5 ≈ wave 1", "คลื่น 5 ≈ คลื่น 1"), t("when wave 3 extended; momentum diverges", "เมื่อคลื่น 3 ยืดยาว โมเมนตัมเริ่มสวนทาง")),
    ]
    for k, (col, head, body) in enumerate(items):
        y = 90 + k * 76
        s.rect(564, y, 368, 66, fill=C["panel"], stroke=C["border"], rx=10)
        s.rect(564, y, 5, 66, fill=col, rx=2)
        s.text(584, y + 26, head, 15, col, weight=700)
        s.text(584, y + 50, body, 13, C["text"])
    return s.render()


# ---------------------------------------------------------------- 6.4
@fig
def corrections(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Three corrective shapes", "รูปแบบการปรับฐาน 3 แบบ"),
            t("Corrections are messier than impulses. Knowing the shapes helps you wait instead of guessing.",
              "การปรับฐานยุ่งเหยิงกว่าแรงส่ง การรู้รูปแบบช่วยให้คุณรอแทนการเดา"))
    specs = [
        (t("Zigzag  5-3-5", "Zigzag  5-3-5"), C["bear"],
         [(0, 120), (2, 112), (3, 116), (5, 106)], ["", "A", "B", "C"],
         t("Sharp and deep. B retraces\nless than ~61.8% of A.\nC ≈ A in length.", "แหลมและลึก B ย่อน้อยกว่า\n~61.8% ของ A\nC ยาวประมาณ A")),
        (t("Flat  3-3-5", "Flat  3-3-5"), C["amber"],
         [(0, 120), (2, 112), (3.3, 119.8), (5, 111)], ["", "A", "B", "C"],
         t("Sideways. B returns ~90–100%\n(or more) of A. C ends near\nor just beyond A's end.", "ออกข้าง B กลับไป ~90–100%\n(หรือมากกว่า) ของ A C จบใกล้\nหรือเลยจุดจบของ A เล็กน้อย")),
        (t("Triangle  3-3-3-3-3", "Triangle  3-3-3-3-3"), C["purple"],
         [(0, 120), (1, 110), (2, 118), (3, 112), (4, 116.5), (5, 113.5)], ["", "A", "B", "C", "D", "E"],
         t("Contracting range. Usually\nwave 4 or B. A thrust in the\ntrend direction follows.", "กรอบบีบตัว มักเป็นคลื่น 4\nหรือ B ตามด้วยการพุ่ง\nในทิศทางเทรนด์")),
    ]
    for k, (head, col, pts, labs, body) in enumerate(specs):
        x = 28 + k * 308
        panel(s, x, 90, 290, 360, head, col, 18)
        P = Plot(s, x + 30, 140, 230, 170, 5, 104, 122)
        if k == 2:
            s.line(P.X(0), P.Y(120), P.X(5), P.Y(115.5), C["dim"], 1.2, "4 4")
            s.line(P.X(0), P.Y(108), P.X(5), P.Y(113), C["dim"], 1.2, "4 4")
        P.path(pts, C["text"], 2.5)
        for j, (i, p) in enumerate(pts):
            if labs[j]:
                P.label(i, p, labs[j], col, up=p > pts[j - 1][1], size=13)
        s.text(x + 18, 360, body, 13, C["text"])
    return s.render()


# ---------------------------------------------------------------- 6.5
@fig
def confluence(lang):
    t = tr(lang)
    s = SVG(960, 520, t("Elliott + Fibonacci: two entries, two targets", "Elliott + ฟีโบนัชชี: สองจุดเข้า สองเป้าหมาย"),
            t("Wave 2 at 61.8% → ride wave 3 to 1.618. Wave 4 at 38.2% → ride wave 5 to wave 1's length.",
              "คลื่น 2 ที่ 61.8% → ตามคลื่น 3 ไปที่ 1.618 คลื่น 4 ที่ 38.2% → ตามคลื่น 5 เท่าความยาวคลื่น 1"))
    cs, idx = walk(EW[:6], [6, 4, 9, 4, 6], seed=91)
    panel(s, 28, 90, 904, 410)
    ch = CandleChart(s, 40, 115, 680, 360, cs, pmin=97, pmax=127, grid=False)
    w1 = EW[1] - EW[0]
    ch.zone(EW[1] - 0.5 * w1, EW[1] - 0.618 * w1, C["bull"], "50–61.8%", i0=idx[1], i1=idx[3], opacity=0.18, label_side="right")
    ch.hline(EW[2] + 1.618 * w1, "1.618 × W1", C["bull"], idx[2], idx[4], "4 4", side="right", size=11)
    w3 = EW[3] - EW[2]
    ch.zone(EW[3] - 0.382 * w3 + 0.5, EW[3] - 0.382 * w3 - 0.5, C["amber"], "38.2% W3", i0=idx[3], opacity=0.22, label_side="left", label_pos="below")
    ch.hline(EW[4] + w1, "W5 = W1", C["amber"], idx[4], None, "4 4", side="left", size=11)
    ch.hline(EW[1], t("W1 high", "จุดสูง W1"), C["dim"], idx[1], None, "2 4", side="right", size=11)
    ch.draw(highlight={idx[2]: C["bull"], idx[4]: C["amber"]})
    for k in range(1, 6):
        up = EW[k] > EW[k - 1]
        ch.label(idx[k], cs[idx[k]][1] if up else cs[idx[k]][2], EW_L[k], C["bull"] if up else C["bear"], dy=-12 if up else 24, size=15)
    s.card(740, 105, 180, 180, t("Trade 1 · wave 3", "เทรด 1 · คลื่น 3"),
           t("Buy 61.8% of W1\n(103.8) after LTF\nCHoCH. Stop below\nwave 1 start (100).\nTarget 1.618: 120.0", "ซื้อที่ 61.8% ของ W1\n(103.8) หลัง CHoCH\nบน LTF Stop ใต้จุด\nเริ่มคลื่น 1 (100)\nเป้า 1.618: 120.0"), C["bull"], 15, 12)
    s.card(740, 300, 180, 180, t("Trade 2 · wave 5", "เทรด 2 · คลื่น 5"),
           t("Buy 38.2% of W3\n(113.8). Stop below\nW1 high (110): rule 3.\nTarget W5 = W1:\n123.8", "ซื้อที่ 38.2% ของ W3\n(113.8) Stop ใต้จุดสูง\nW1 (110): กฎข้อ 3\nเป้า W5 = W1:\n123.8"), C["amber"], 15, 12)
    return s.render()


# ---------------------------------------------------------------- 6.6
@fig
def bell_curve(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Standard deviation: the ruler of normal movement", "ส่วนเบี่ยงเบนมาตรฐาน: ไม้บรรทัดของการเคลื่อนไหวปกติ"),
            t("If returns were normal: ±1σ ≈ 68% of days, ±2σ ≈ 95%, ±3σ ≈ 99.7%. Real markets have fatter tails.",
              "ถ้าผลตอบแทนเป็นแบบปกติ: ±1σ ≈ 68% ของวัน ±2σ ≈ 95% ±3σ ≈ 99.7% ตลาดจริงมีหางที่อ้วนกว่า"))
    panel(s, 28, 90, 904, 360)
    x0, w, base, h = 80, 800, 390, 250
    X = lambda z: x0 + w * (z + 4) / 8
    pdf = lambda z: math.exp(-z * z / 2) / math.sqrt(2 * math.pi)
    for a, b, col, op in ((-3, 3, C["blue"], 0.10), (-2, 2, C["blue"], 0.16), (-1, 1, C["blue"], 0.28)):
        pts = [(X(a), base)] + [(X(a + (b - a) * k / 60), base - h * pdf(a + (b - a) * k / 60) / 0.4) for k in range(61)] + [(X(b), base)]
        s.polygon(pts, col, op)
    curve = [(X(-4 + 8 * k / 160), base - h * pdf(-4 + 8 * k / 160) / 0.4) for k in range(161)]
    s.polyline(curve, C["text"], 2.5)
    fat = lambda z: 0.88 * pdf(z) + 0.12 * math.exp(-z * z / 8) / (2 * math.sqrt(2 * math.pi))
    s.polyline([(X(-4 + 8 * k / 160), base - h * fat(-4 + 8 * k / 160) / 0.4) for k in range(161)], C["amber"], 2, "6 4")
    s.line(x0, base, x0 + w, base, C["dim"], 1)
    for z in range(-3, 4):
        s.line(X(z), base, X(z), base + 6, C["muted"], 1)
        s.text(X(z), base + 22, f"{z:+d}σ" if z else "0", 12, C["muted"], "middle")
    s.text(X(0), base - 90, "68%", 18, C["white"], "middle", 700)
    s.text(X(-1.5), base - 30, "95%", 14, C["text"], "middle", 700)
    s.text(X(-2.5), base - 12, "99.7%", 12, C["text"], "middle", 700)
    s.text(X(2.6), 170, t("— normal curve", "— เส้นโค้งปกติ"), 13, C["text"], weight=600)
    s.text(X(2.6), 192, t("- - real returns: fatter tails", "- - ผลตอบแทนจริง: หางอ้วนกว่า"), 13, C["amber"], weight=600)
    s.text(X(2.6), 214, t("(big moves happen more\noften than the bell says)", "(การเคลื่อนไหวใหญ่เกิดบ่อย\nกว่าที่ระฆังบอก)"), 12, C["muted"])
    return s.render()


@fig
def expected_move(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Expected move: σ bands from volatility", "Expected Move: แถบ σ จากความผันผวน"),
            t("Daily σ ≈ price × annual volatility ÷ √252. Example: index at 5,000, volatility 16% → σ ≈ 50 points.",
              "σ รายวัน ≈ ราคา × ความผันผวนรายปี ÷ √252 ตัวอย่าง: ดัชนี 5,000 ความผันผวน 16% → σ ≈ 50 จุด"))
    rnd = random.Random(2)
    n = 30
    opens, closes = [5000], []
    sd = 5000 * 0.16 / math.sqrt(252)
    panel(s, 28, 90, 904, 390)
    x0, w, y0, h = 80, 640, 120, 330
    lo, hi = 5000 - 3.2 * sd, 5000 + 3.2 * sd
    X = lambda i: x0 + w * i / n
    Y = lambda p: y0 + h * (hi - p) / (hi - lo)
    for k, col in ((2, C["bear"]), (1, C["amber"])):
        s.rect(x0, Y(5000 + k * sd), w, Y(5000 - k * sd) - Y(5000 + k * sd), fill=col, opacity=0.07)
        for sign in (1, -1):
            p = 5000 + sign * k * sd
            s.line(x0, Y(p), x0 + w, Y(p), col, 1.3, "5 4")
            s.text(x0 + w + 8, Y(p) + 4, f"{'+' if sign > 0 else '−'}{k}σ  {p:,.0f}", 12, col, weight=700)
    s.line(x0, Y(5000), x0 + w, Y(5000), C["dim"], 1)
    s.text(x0 + w + 8, Y(5000) + 4, t("open 5,000", "เปิด 5,000"), 12, C["muted"], weight=700)
    inside1 = inside2 = 0
    for i in range(n):
        z = rnd.gauss(0, 1) if rnd.random() > 0.08 else rnd.choice([-1, 1]) * rnd.uniform(2.2, 3.0)
        c = 5000 + z * sd
        inside1 += abs(z) <= 1
        inside2 += abs(z) <= 2
        col = C["bull"] if c >= 5000 else C["bear"]
        s.line(X(i + 0.5), Y(5000), X(i + 0.5), Y(c), col, 6, opacity=0.85)
    s.text(x0, 470, t(f"30 days, each bar = that day's close vs. its open (all opens aligned at 5,000). Inside ±1σ: {inside1}/30 · inside ±2σ: {inside2}/30",
                      f"30 วัน แต่ละแท่ง = ราคาปิดเทียบราคาเปิดของวันนั้น (จัดราคาเปิดไว้ที่ 5,000) อยู่ใน ±1σ: {inside1}/30 · อยู่ใน ±2σ: {inside2}/30"),
           12, C["muted"])
    return s.render()


@fig
def sd_projection(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Range projections: measuring the next leg with the last one", "การฉายกรอบ: วัดขาถัดไปด้วยขาก่อนหน้า"),
            t("ICT-style 'standard deviation' projections: multiples of a reference leg (−1, −2, −2.5, −4).",
              "การฉาย 'ส่วนเบี่ยงเบนมาตรฐาน' แบบ ICT: ผลคูณของขาอ้างอิง (−1, −2, −2.5, −4)"))
    pre, idx = walk([104, 101.2, 103.0, 98.6, 99.6], [4, 3, 4, 2], seed=97)
    o = pre[-1][3]
    cs = extend(pre, [[o, 99.8, o - 0.3, 99.7], [99.7, 103.4, 99.6, 103.2], [103.2, 104.2, 102.6, 103.9]])
    leg_lo, leg_hi = 98.6, 104.2
    rng = leg_hi - leg_lo
    more, _ = walk([103.9, 104.6, 102.9, 109.9, 108.6, 115.4, 114.6], [1, 3, 5, 2, 4, 2], seed=98)
    cs = extend(cs, more[1:])
    panel(s, 28, 90, 904, 390)
    ch = CandleChart(s, 40, 115, 640, 340, cs, pmin=97, pmax=121, grid=False)
    i0 = idx[3]
    ch.zone(leg_lo, leg_hi, C["blue"], t("reference leg = 1", "ขาอ้างอิง = 1"), i0=i0, i1=i0 + 7, opacity=0.18, label_side="left", label_pos="below")
    for m, col in ((1, C["teal"]), (2, C["amber"]), (2.5, C["bull"]), (4, C["purple"])):
        p = leg_lo + (1 + m) * rng if False else leg_hi + m * rng
        if p < 121:
            ch.hline(p, f"−{m:g}  {p:.1f}", col, i0, None, "4 4", side="right", size=12)
    ch.draw()
    s.card(700, 110, 220, 190, t("How it's drawn", "วาดอย่างไร"),
           t("Take the leg that broke\nstructure (98.6 → 104.2,\nrange 5.6). Project\nmultiples of it beyond\nits end: −1 = 109.8,\n−2 = 115.4, −2.5 = 118.2", "ใช้ขาที่เบรกโครงสร้าง\n(98.6 → 104.2 กรอบ 5.6)\nฉายผลคูณของมัน\nต่อจากปลายขา: −1 = 109.8\n−2 = 115.4, −2.5 = 118.2"), C["blue"], 15, 12)
    s.card(700, 314, 220, 150, t("Honest note", "หมายเหตุตามจริง"),
           t("This is a measured-move\nruler, not statistics.\nUse levels as targets\nonly with confluence.", "นี่คือไม้บรรทัดวัดระยะ\nไม่ใช่สถิติ ใช้ระดับ\nเป็นเป้าหมายเฉพาะเมื่อ\nมีจุดบรรจบ"), C["amber"], 15, 12)
    return s.render()


# ---------------------------------------------------------------- 6.7
@fig
def summary(lang):
    t = tr(lang)
    s = SVG(960, 560, t("Phase 6 on one page", "สรุปเฟส 6 ในหน้าเดียว"))
    cx, cy = 480, 310
    nodes = [
        (170, 140, C["bull"], t("6.1 Fibonacci", "6.1 ฟีโบนัชชี"), t("Retrace 38.2 / 50 / 61.8 / 78.6.\nExtend 1.0 / 1.272 / 1.618.", "ย่อ 38.2 / 50 / 61.8 / 78.6\nขยาย 1.0 / 1.272 / 1.618")),
        (790, 140, C["blue"], t("6.2 Elliott 5-3", "6.2 Elliott 5-3"), t("5 waves with the trend,\n3 against. Fractal.", "5 คลื่นตามเทรนด์\n3 คลื่นสวน เป็น Fractal")),
        (150, 320, C["bear"], t("6.3 Rules", "6.3 กฎ"), t("W2 < 100% · W3 not shortest\n· W4 no overlap with W1.", "W2 < 100% · W3 ไม่สั้นสุด\n· W4 ไม่ซ้อน W1")),
        (810, 320, C["amber"], t("6.4 Corrections", "6.4 การปรับฐาน"), t("Zigzag · flat · triangle.\nMessy: wait, don't guess.", "Zigzag · Flat · Triangle\nยุ่งเหยิง: รอ อย่าเดา")),
        (250, 480, C["purple"], t("6.5 Confluence", "6.5 จุดบรรจบ"), t("W2 @ 61.8% → W3 to 1.618.\nInvalidation = the rules.", "W2 @ 61.8% → W3 ถึง 1.618\nจุดผิด = กฎ")),
        (710, 480, C["teal"], t("6.6 Std dev", "6.6 ส่วนเบี่ยงเบนมาตรฐาน"), t("σ ≈ price × vol ÷ √252.\nTails are fatter than normal.", "σ ≈ ราคา × ความผันผวน ÷ √252\nหางอ้วนกว่าปกติ")),
    ]
    for x, y, col, head, body in nodes:
        s.line(cx, cy, x, y, col, 2, opacity=0.5)
    s.circle(cx, cy, 74, C["panel"], C["text"], 2)
    s.text(cx, cy - 4, t("PHASE 6", "เฟส 6"), 20, C["text"], "middle", 700)
    s.text(cx, cy + 20, t("Measuring", "การวัดตลาด"), 14, C["muted"], "middle")
    for x, y, col, head, body in nodes:
        s.rect(x - 130, y - 42, 260, 92, fill=C["panel"], stroke=col, rx=12)
        s.text(x, y - 14, head, 17, col, "middle", 700)
        s.text(x, y + 10, body, 13, C["text"], "middle")
    return s.render()


# ================================================================ v2 additions (Oct 2026)
def _ew_candles():
    cs, idx = walk(EW, [5, 3, 7, 3, 5, 3, 2, 4], seed=61, vol=0.3)
    return cs, idx


PSY = {"en": ["", "smart money\nbuys quietly", "doubt:\n'just a bounce'", "recognition:\nthe crowd joins", "profit-taking", "euphoria / FOMO,\nweaker momentum", "first drop", "'buy the dip'\nfails", "real decline"],
       "th": ["", "เงินฉลาด\nซื้อเงียบ ๆ", "สงสัย:\n'แค่เด้ง'", "ยอมรับ:\nฝูงชนเข้าร่วม", "ขายทำกำไร", "ตื่นเต้น / FOMO\nโมเมนตัมอ่อนลง", "ลงครั้งแรก", "'ซื้อตอนย่อ'\nล้มเหลว", "ลงจริง"]}


@fig
def fib_candles(lang):
    t = tr(lang)
    s = SVG(960, 520, t("Fibonacci on a real-looking swing: 100 → 150", "ฟีโบนัชชีบนสวิงที่ดูเหมือนจริง: 100 → 150"),
            t("Illustrative candles. Retracement from the swing low to the swing high; extension projected from the pullback low.",
              "แท่งเทียนประกอบการอธิบาย รีเทรซเมนต์จาก Swing low ถึง Swing high เอกซ์เทนชันวัดจากจุดต่ำของการย่อ"))
    cs, idx = walk([100, 150, 130.9, 171], [12, 7, 9], seed=62, vol=0.3)
    panel(s, 28, 90, 904, 410)
    ch = CandleChart(s, 40, 112, 640, 370, cs, pmin=96, pmax=186)
    for r, col in RET:
        p = 150 - r * 50
        ch.hline(p, f"{r * 100:.1f}% = {p:.1f}", col, idx[1], None, "4 4", side="right", size=11)
    ch.hline(180.9, t("1.0 ext = 180.9", "Ext 1.0 = 180.9"), C["amber"], idx[2], None, "2 4", side="right", size=11)
    ch.draw(highlight={idx[2]: C["teal"]})
    ch.label(idx[0], cs[idx[0]][2], "A 100", C["text"], dy=22, size=12)
    ch.label(idx[1], cs[idx[1]][1], "B 150", C["text"], dy=-10, size=12)
    ch.label(idx[2], cs[idx[2]][2], t("C 130.9 (38.2%)", "C 130.9 (38.2%)"), C["teal"], dy=6, size=12, anchor="end", dx=-16)
    rows = [(t("Retracement (100 → 150)", "รีเทรซเมนต์ (100 → 150)"), C["text"], True)] + \
           [(f"{r * 100:.1f}% → {150 - r * 50:.1f}", col, False) for r, col in RET] + \
           [(t("Extension from C = 130.9", "เอกซ์เทนชันจาก C = 130.9"), C["text"], True),
            ("1.0 → 180.9", C["amber"], False), ("1.272 → 194.5", C["amber"], False), ("1.618 → 211.8", C["amber"], False)]
    for k, (txt, col, head) in enumerate(rows):
        s.text(712, 130 + k * 30, txt, 14 if head else 14, col, weight=700 if head else 600)
    s.text(712, 470, t("194.5 and 211.8 are off the chart:\ntargets, not predictions.", "194.5 และ 211.8 อยู่นอกกราฟ:\nเป็นเป้าหมาย ไม่ใช่คำทำนาย"), 12, C["muted"])
    return s.render()


def _ew_panel(s, t, lang, labels, colors, y=120, h=330):
    cs, idx = _ew_candles()
    ch = CandleChart(s, 40, y, 880, h, cs, pmin=94.5, pmax=129)
    ch.draw()
    for k, lab in enumerate(labels):
        if lab is None:
            continue
        i = idx[k]
        up = k == 0 or EW[k] > EW[k - 1]
        p = cs[i][1] if up else cs[i][2]
        if k == 0:
            p, up = cs[i][2], False
        ch.label(i, p, lab, colors[k], dy=-12 if up else 22, size=16)
    return ch, cs, idx


@fig
def ew_labelled(lang):
    t = tr(lang)
    s = SVG(960, 560, t("A fully labelled Elliott count (correct)", "การนับคลื่น Elliott ที่ติดป้ายครบ (ถูกต้อง)"),
            t("Illustrative candles. Each wave is a crowd changing its mind. All three rules pass.",
              "แท่งเทียนประกอบการอธิบาย แต่ละคลื่นคือฝูงชนที่เปลี่ยนความคิด ผ่านกฎครบทั้งสามข้อ"))
    panel(s, 28, 90, 904, 450)
    cols = [C["muted"], C["bull"], C["bear"], C["bull"], C["bear"], C["bull"], C["bear"], C["bull"], C["bear"]]
    ch, cs, idx = _ew_panel(s, t, lang, EW_L, cols)
    ch.path([(idx[k], EW[k]) for k in range(len(EW))], C["blue"], 1.5, "4 4")
    psy = PSY[lang]
    for k in range(1, 9):
        i = idx[k]
        up = EW[k] > EW[k - 1]
        y = ch.Y(cs[i][1]) - 48 if up else ch.Y(cs[i][2]) + 50
        s.text(ch.X(i), y, psy[k], 11, cols[k], "middle")
    ch.hline(110, None, C["amber"], idx[1], idx[5], "3 4")
    s.text(48, 506, t("Dashed amber line = wave-1 high (110): wave 4 must stay above it (rule 3).", "เส้นประสีส้ม = จุดสูงคลื่น 1 (110): คลื่น 4 ต้องอยู่เหนือเส้นนี้ (กฎ 3)"), 12, C["amber"], weight=600)
    s.text(48, 528, t("W1 = 10 · W2 = 61.8% of W1 · W3 = 16.18 (1.618 × W1, the longest) · W4 = 38.2% of W3, stays above 110 · W5 = W1",
                      "W1 = 10 · W2 = 61.8% ของ W1 · W3 = 16.18 (1.618 × W1 ยาวที่สุด) · W4 = 38.2% ของ W3 อยู่เหนือ 110 · W5 = W1"), 12, C["muted"])
    return s.render()


@fig
def ew_wrong_count(lang):
    t = tr(lang)
    s = SVG(960, 560, t("The same candles, counted wrong", "แท่งเทียนชุดเดิม นับผิด"),
            t("Someone calls 120 'wave 1' and the C low at 115.4 'wave 4'. Two rules break.",
              "มีคนเรียก 120 ว่า 'คลื่น 1' และจุดต่ำ C ที่ 115.4 ว่า 'คลื่น 4' ผิดกฎสองข้อ"))
    panel(s, 28, 90, 904, 450)
    wrong = ["0", None, None, "1?", "2?", "3?", None, None, "4?"]
    cols = [C["muted"]] + [C["bear"]] * 8
    ch, cs, idx = _ew_panel(s, t, lang, wrong, cols, y=110, h=320)
    ch.path([(idx[0], EW[0]), (idx[3], EW[3]), (idx[4], EW[4]), (idx[5], EW[5]), (idx[8], EW[8])], C["bear"], 1.5, "4 4")
    ch.hline(120, None, C["amber"], idx[3], idx[8], "3 4")
    ch.zone(115.4, 120, C["bear"], None, idx[7], idx[8], 0.18)
    notes = [(t("✗ Rule 3: 'wave 4' (115.4) overlaps 'wave 1' (above 115.4 up to 120)", "✗ กฎ 3: 'คลื่น 4' (115.4) ทับซ้อนพื้นที่ของ 'คลื่น 1' (ต่ำกว่า 120)"), C["bear"]),
             (t("✗ Rule 2 at risk: 'wave 3' = 10 is already shorter than 'wave 1' = 20", "✗ กฎ 2 เสี่ยง: 'คลื่น 3' = 10 สั้นกว่า 'คลื่น 1' = 20 แล้ว"), C["bear"]),
             (t("A trader 'buying wave 4 for wave 5' at 115.4 is buying a correction (it's really wave C).", "เทรดเดอร์ที่ 'ซื้อคลื่น 4 เพื่อรอคลื่น 5' ที่ 115.4 กำลังซื้อการปรับฐาน (ที่จริงคือคลื่น C)"), C["amber"])]
    for k, (txt, col) in enumerate(notes):
        s.text(48, 466 + k * 24, txt, 13, col, weight=700)
    return s.render()


@fig
def count_validator(lang):
    t = tr(lang)
    s = SVG(960, 500, t("The count validator: check the rules with numbers", "ตัวตรวจการนับ: ตรวจกฎด้วยตัวเลข"),
            t("Example: 0 = 100, 1 = 110, 2 = 103.8, 3 = 120, 4 = 108.5 (instead of 113.8).",
              "ตัวอย่าง: 0 = 100, 1 = 110, 2 = 103.8, 3 = 120, 4 = 108.5 (แทนที่จะเป็น 113.8)"))
    steps = [(t("Rule 1", "กฎ 1"), t("wave 2 low > wave 1 start?", "จุดต่ำคลื่น 2 > จุดเริ่มคลื่น 1?"), t("103.8 > 100 ✓", "103.8 > 100 ✓"), True),
             (t("Rule 2", "กฎ 2"), t("wave 3 not the shortest?", "คลื่น 3 ไม่สั้นที่สุด?"), t("16.2 > 10 ✓", "16.2 > 10 ✓"), True),
             (t("Rule 3", "กฎ 3"), t("wave 4 low > wave 1 high?", "จุดต่ำคลื่น 4 > จุดสูงคลื่น 1?"), t("108.5 < 110 ✗", "108.5 < 110 ✗"), False)]
    for k, (head, q, ans, ok) in enumerate(steps):
        x = 40 + k * 230
        col = C["bull"] if ok else C["bear"]
        s.rect(x, 110, 200, 120, fill=C["panel"], stroke=col, rx=12)
        s.text(x + 100, 140, head, 17, col, "middle", 700)
        s.text(x + 100, 168, q, 12, C["text"], "middle")
        s.text(x + 100, 206, ans, 18, col, "middle", 800)
        if k < 2:
            s.arrow(x + 202, 170, x + 228, 170, C["bull"], 2)
    s.rect(730, 110, 202, 120, fill=C["bear"], opacity=0.15, stroke=C["bear"], rx=12)
    s.text(831, 145, t("Count INVALID", "การนับ ใช้ไม่ได้"), 16, C["bear"], "middle", 700)
    s.text(831, 172, t("Exit / don't enter.\nThen relabel:", "ออก / ไม่เข้า\nแล้วติดป้ายใหม่:"), 12, C["text"], "middle")
    s.arrow(700, 170, 726, 170, C["bear"], 2)
    s.rect(40, 260, 892, 210, fill=C["panel"], stroke=C["border"], rx=12)
    s.text(60, 292, t("Alternatives once rule 3 fails", "ทางเลือกเมื่อกฎ 3 ใช้ไม่ได้"), 16, C["text"], weight=700)
    alts = [t("A · 103.8 → 120 was only sub-wave (i) of a larger wave 3; 108.5 is (ii). Needs: 108.5 holds above 103.8.",
              "A · 103.8 → 120 เป็นแค่คลื่นย่อย (i) ของคลื่น 3 ที่ใหญ่กว่า 108.5 คือ (ii) ต้อง: 108.5 ยืนเหนือ 103.8"),
            t("B · The whole rise 100 → 120 is a correction (A-B-C) in a downtrend. Needs: lower lows to follow.",
              "B · การขึ้นทั้งหมด 100 → 120 คือการปรับฐาน (A-B-C) ในขาลง ต้อง: มีจุดต่ำใหม่ตามมา"),
            t("C · A leading diagonal (wedge) where overlap is allowed. Rare; needs a wedge shape.",
              "C · Leading diagonal (ลิ่ม) ที่อนุญาตให้ทับซ้อนได้ พบน้อย ต้องมีรูปลิ่ม")]
    for k, a in enumerate(alts):
        s.text(60, 330 + k * 40, a, 13, C["amber"] if k == 0 else C["muted"], weight=600)
    s.text(60, 450, t("A long from 'wave 4' at 113.8 with the rule-3 stop at 109.6 was stopped out for −1R before 108.5 printed.",
                      "Long จาก 'คลื่น 4' ที่ 113.8 พร้อม Stop ตามกฎ 3 ที่ 109.6 โดน Stop −1R ก่อนราคาลงถึง 108.5"), 13, C["bear"], weight=700)
    return s.render()


@fig
def corrections_subwaves(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Inside the corrections: the sub-waves", "ภายในการปรับฐาน: คลื่นย่อย"),
            t("Small labels show how each leg subdivides. 5 = impulse-like leg, 3 = corrective leg.",
              "ป้ายเล็กแสดงว่าแต่ละขาแบ่งย่อยอย่างไร 5 = ขาที่เหมือน Impulse, 3 = ขาปรับฐาน"))
    shapes = [
        (C["bear"], t("Zigzag 5-3-5", "Zigzag 5-3-5"),
         [(0, 100), (1, 96), (1.6, 98), (2.6, 93), (3.2, 95), (4, 90), (5, 93), (5.6, 91.5), (6.6, 95), (7.6, 91), (8.2, 92.5), (9.4, 86), (10.2, 88), (11.6, 81)],
         [(4, 90, "A"), (6.6, 95, "B"), (11.6, 81, "C")], ["i", "ii", "iii", "iv", "v", "a", "b", "c", "i", "ii", "iii", "iv", "v"]),
        (C["amber"], t("Flat 3-3-5", "Flat 3-3-5"),
         [(0, 100), (1.5, 94), (2.5, 97), (4, 91), (5.5, 96), (6.5, 93.5), (8, 99.5), (8.8, 96), (9.3, 97.5), (10.2, 92), (10.8, 94), (11.6, 89)],
         [(4, 91, "A"), (8, 99.5, "B"), (11.6, 89, "C")], ["a", "b", "c", "a", "b", "c", "i", "ii", "iii", "iv", "v"]),
        (C["purple"], t("Triangle 3-3-3-3-3", "Triangle 3-3-3-3-3"),
         [(0, 100), (0.8, 92), (1.3, 95), (2, 88), (2.8, 95), (3.2, 93), (4, 98), (4.6, 93), (5, 95), (5.8, 90), (6.4, 94), (6.8, 92.5), (7.6, 96.5), (8.2, 93), (8.6, 94.5), (9.4, 91.5)],
         [(2, 88, "A"), (4, 98, "B"), (5.8, 90, "C"), (7.6, 96.5, "D"), (9.4, 91.5, "E")], ["a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c", "a", "b", "c"]),
    ]
    for k, (col, title, pts, big, small) in enumerate(shapes):
        bx = 28 + k * 308
        panel(s, bx, 90, 296, 360, title, col, 16)
        P = Plot(s, bx + 20, 140, 256, 270, 12, 78, 102)
        P.path(pts, C["text"], 2)
        for j, (i, p) in enumerate(pts[1:]):
            prev = pts[j][1]
            up = p > prev
            if any(abs(i - bi) < 1e-9 for bi, _, _ in big):
                continue
            s.text(P.X(i), P.Y(p) + (-7 if up else 15), small[j] if j < len(small) else "", 10, C["muted"], "middle")
        for i, p, lab in big:
            P.label(i, p, lab, col, up=lab in ("B", "D"), size=15)
    return s.render()


@fig
def confluence_candles(lang):
    t = tr(lang)
    s = SVG(960, 520, t("Elliott + Fibonacci on candles: W1 100 → 120", "Elliott + Fibonacci บนแท่งเทียน: W1 100 → 120"),
            t("Illustrative. Wave 2 at 61.8% = 107.6, wave 3 target = 107.6 + 1.618 × 20 = 140.0.",
              "ภาพประกอบ คลื่น 2 ที่ 61.8% = 107.6 เป้าคลื่น 3 = 107.6 + 1.618 × 20 = 140.0"))
    cs, idx = walk([100, 120, 107.64, 140.0], [8, 6, 12], seed=65, vol=0.3)
    panel(s, 28, 90, 904, 410)
    ch = CandleChart(s, 40, 112, 640, 370, cs, pmin=96, pmax=144)
    ch.zone(120 - 0.5 * 20, 120 - 0.618 * 20, C["bull"], t("wave-2 zone 50–61.8%", "โซนคลื่น 2 50–61.8%"), idx[1], idx[2] + 3, 0.15, size=11, label_pos="below")
    ch.hline(99.5, t("stop 99.5 (rule 1)", "Stop 99.5 (กฎ 1)"), C["bear"], idx[2], None, "4 4", side="right", size=11)
    ch.hline(140.0, t("target 140.0", "เป้า 140.0"), C["amber"], idx[2], None, "4 4", side="left", size=11)
    ch.draw(highlight={idx[2]: C["bull"]})
    for k, lab in enumerate(["0", "1", "2", "3"]):
        i = idx[k]
        up = k in (1, 3)
        ch.label(i, cs[i][1] if up else cs[i][2], lab, C["bull"] if up else (C["bear"] if k else C["muted"]), dy=-12 if up else 22, size=16)
    rows = [(t("Wave 1", "คลื่น 1"), "100 → 120 = 20"), (t("Wave 2 = 61.8%", "คลื่น 2 = 61.8%"), "120 − 12.36 = 107.64"),
            (t("Entry (on LTF CHoCH)", "จุดเข้า (เมื่อ CHoCH บน LTF)"), "≈ 107.6"), (t("Stop below W1 start", "Stop ใต้จุดเริ่ม W1"), "99.5 → risk 8.14"),
            (t("Target 1.618 × W1", "เป้า 1.618 × W1"), "107.64 + 32.36 = 140.0"), (t("Reward ÷ risk", "ผลตอบแทน ÷ ความเสี่ยง"), "32.36 ÷ 8.14 ≈ 3.98R")]
    for k, (a, b) in enumerate(rows):
        s.text(704, 136 + k * 54, a, 13, C["muted"], weight=600)
        s.text(704, 158 + k * 54, b, 15, C["text"], weight=700)
    return s.render()


@fig
def heights(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Standard deviation without markets: students' heights", "ส่วนเบี่ยงเบนมาตรฐานแบบไม่มีตลาด: ส่วนสูงของนักเรียน"),
            t("Illustrative class: average 165 cm, standard deviation 7 cm.", "ห้องเรียนสมมติ: ค่าเฉลี่ย 165 ซม. ส่วนเบี่ยงเบนมาตรฐาน 7 ซม."))
    x0, x1, base, top = 80, 880, 380, 110
    X = lambda h: x0 + (h - 140) / 50 * (x1 - x0)
    for band, col, op in ((3, C["dim"], 0.10), (2, C["blue"], 0.14), (1, C["bull"], 0.22)):
        s.rect(X(165 - 7 * band), top, X(165 + 7 * band) - X(165 - 7 * band), base - top, fill=col, opacity=op)
    pts = []
    for k in range(201):
        h = 140 + 50 * k / 200
        y = base - (base - top - 20) * math.exp(-((h - 165) ** 2) / (2 * 49))
        pts.append((X(h), y))
    s.polyline(pts, C["text"], 2.5)
    for h in range(144, 190, 7):
        s.line(X(h), base, X(h), base + 6, C["muted"], 1)
        s.text(X(h), base + 22, str(h), 12, C["muted"], "middle")
    s.text((x0 + x1) / 2, base + 44, t("height (cm)", "ส่วนสูง (ซม.)"), 12, C["muted"], "middle")
    s.text(X(165), top + 120, t("±1 SD: 158–172 cm\n≈ 68% of students", "±1 SD: 158–172 ซม.\n≈ 68% ของนักเรียน"), 13, C["bull"], "middle", 700)
    s.text(X(152), top + 150, t("±2 SD: 151–179\n≈ 95%", "±2 SD: 151–179\n≈ 95%"), 12, C["blue"], "middle", 700)
    s.text(X(146.5), top + 175, t("±3 SD:\n144–186\n≈ 99.7%", "±3 SD:\n144–186\n≈ 99.7%"), 11, C["muted"], "middle", 700)
    s.text(48, 455, t("Markets differ: returns have fat tails, so '3 SD' days happen far more often than 0.3% of the time.",
                      "ตลาดต่างออกไป: ผลตอบแทนมีหางอ้วน วัน '3 SD' จึงเกิดบ่อยกว่า 0.3% มาก"), 13, C["amber"], weight=600)
    return s.render()
