"""Phase 7 figures: Orderflow & Auction Market Theory."""
import math
import random
from charts import SVG, CandleChart, C, tr
from figures.p2 import walk, extend, panel
from figures.p6 import Plot

FIGURES = {}


def fig(fn):
    FIGURES["p7-" + fn.__name__.replace("_", "-")] = fn
    return fn


def profile(cs, lo, hi, n=40, vols=None):
    """Distribute each candle's volume evenly over its range -> (bins, edges)."""
    step = (hi - lo) / n
    bins = [0.0] * n
    for k, (o, h, l, c) in enumerate(cs):
        v = vols[k] if vols else 1.0
        a, b = int((l - lo) / step), int((h - lo) / step)
        a, b = max(a, 0), min(b, n - 1)
        for j in range(a, b + 1):
            bins[j] += v / (b - a + 1)
    return bins, step


def value_area(bins, share=0.7):
    poc = max(range(len(bins)), key=lambda j: bins[j])
    lo = hi = poc
    tot, acc = sum(bins), bins[poc]
    while acc < share * tot:
        up = bins[hi + 1] if hi + 1 < len(bins) else -1
        dn = bins[lo - 1] if lo - 1 >= 0 else -1
        if up >= dn:
            hi += 1
            acc += up
        else:
            lo -= 1
            acc += dn
    return poc, lo, hi


# ---------------------------------------------------------------- 7.1
@fig
def balance(lang):
    t = tr(lang)
    s = SVG(960, 500, t("The auction: balance → imbalance → new balance", "การประมูล: สมดุล → ไม่สมดุล → สมดุลใหม่"),
            t("Markets rotate around fair value until new information pushes them to find a new one.",
              "ตลาดหมุนรอบมูลค่ายุติธรรม จนกว่าข้อมูลใหม่จะผลักให้มันออกไปหามูลค่าใหม่"))
    piv = [102, 104.8, 99.6, 104.6, 100.0, 104.4, 100.3, 103.8,
           112.5, 110.6, 115.4, 113.0, 116.6, 112.8, 116.4, 113.4, 115.0]
    bars = [3, 4, 4, 4, 4, 4, 3, 6, 2, 4, 2, 3, 3, 3, 3, 2]
    cs, idx = walk(piv, bars, seed=7)
    panel(s, 28, 90, 904, 390)
    ch = CandleChart(s, 40, 130, 880, 300, cs, pmin=97, pmax=119)
    ch.zone(99.5, 104.9, C["blue"], t("BALANCE 1 · two-sided rotation", "สมดุล 1 · หมุนสองทาง"), i0=0, i1=idx[7], opacity=0.12, label_pos="below")
    ch.zone(112.6, 116.7, C["blue"], t("BALANCE 2 · new value", "สมดุล 2 · มูลค่าใหม่"), i0=idx[9] - 1, opacity=0.12, label_side="right", label_pos="above")
    x0, x1 = ch.X(idx[7]) - ch.step / 2, ch.X(idx[8]) + ch.step / 2
    s.rect(x0, 130, x1 - x0, 300, fill=C["amber"], opacity=0.10)
    s.text((x0 + x1) / 2, 124, t("IMBALANCE", "ไม่สมดุล"), 13, C["amber"], "middle", 700)
    ch.draw()
    s.text(48, 462, t("Balance: buyers and sellers agree on value → range, responsive trading at the edges.   Imbalance: one side is more aggressive → trend toward new value.",
                      "สมดุล: ผู้ซื้อผู้ขายเห็นตรงกันเรื่องมูลค่า → กรอบ เทรดสวนที่ขอบ   ไม่สมดุล: ฝ่ายหนึ่งรุกกว่า → เทรนด์ไปหามูลค่าใหม่"),
           12, C["muted"])
    return s.render()


@fig
def auction_rules(lang):
    t = tr(lang)
    s = SVG(960, 470, t("How the auction works", "การประมูลทำงานอย่างไร"),
            t("Price advertises, time regulates, volume validates.", "ราคาเป็นตัวโฆษณา เวลาเป็นตัวควบคุม วอลุ่มเป็นตัวยืนยัน"))
    cards = [
        (C["blue"], t("Price advertises", "ราคาโฆษณา"),
         t("Price moves to attract the\nother side. Up = searching\nfor sellers; down = searching\nfor buyers.", "ราคาขยับเพื่อดึงอีกฝั่งเข้ามา\nขึ้น = หาผู้ขาย\nลง = หาผู้ซื้อ")),
        (C["amber"], t("Time regulates", "เวลาควบคุม"),
         t("The longer price stays at a\nlevel, the more it is accepted\nas fair. Quick rejection =\nunfair price.", "ราคาอยู่ที่ระดับไหนนาน\nยิ่งถูกยอมรับว่ายุติธรรม\nถูกปฏิเสธเร็ว =\nราคาไม่ยุติธรรม")),
        (C["bull"], t("Volume validates", "วอลุ่มยืนยัน"),
         t("High volume at a price =\nacceptance (value).\nLow volume = rejection\n(price moves through fast).", "วอลุ่มสูงที่ราคาไหน =\nยอมรับ (มูลค่า)\nวอลุ่มต่ำ = ปฏิเสธ\n(ราคาวิ่งผ่านเร็ว)")),
    ]
    for k, (col, head, body) in enumerate(cards):
        s.card(28 + k * 308, 92, 290, 190, head, body, col, 19, 14)
    rows = [
        (C["teal"], t("Responsive activity", "การตอบสนอง (Responsive)"),
         t("Buying below value / selling above value. Expect rotation back to value. → balance", "ซื้อใต้มูลค่า / ขายเหนือมูลค่า คาดว่าจะหมุนกลับหามูลค่า → สมดุล")),
        (C["pink"], t("Initiative activity", "การริเริ่ม (Initiative)"),
         t("Buying above value / selling below value. Expect continuation away from value. → imbalance", "ซื้อเหนือมูลค่า / ขายใต้มูลค่า คาดว่าจะวิ่งต่อออกจากมูลค่า → ไม่สมดุล")),
    ]
    for k, (col, head, body) in enumerate(rows):
        y = 300 + k * 80
        s.rect(28, y, 904, 68, fill=C["panel"], stroke=C["border"], rx=10)
        s.rect(28, y, 5, 68, fill=col, rx=2)
        s.text(48, y + 28, head, 16, col, weight=700)
        s.text(48, y + 52, body, 13, C["text"])
    return s.render()


# ---------------------------------------------------------------- 7.2
def _vp_data():
    piv = [101, 104.6, 100.2, 106.5, 103.2, 105.6, 102.4, 108.8, 106.0, 107.6]
    cs, _ = walk(piv, [4, 5, 6, 4, 5, 4, 7, 4, 3], seed=17)
    rnd = random.Random(3)
    vols = [rnd.uniform(0.6, 1.4) * (1.8 if 103.5 < (c[1] + c[2]) / 2 < 105.5 else 1.0) for c in cs]
    return cs, vols


@fig
def volume_profile(lang):
    t = tr(lang)
    s = SVG(960, 520, t("Volume profile: where the market did business", "Volume Profile: ตลาดซื้อขายกันที่ราคาไหน"),
            t("Volume by PRICE, not by time. POC = most traded price; value area = ~70% of volume.",
              "วอลุ่มตาม ราคา ไม่ใช่ตามเวลา POC = ราคาที่ซื้อขายมากที่สุด Value Area = ~70% ของวอลุ่ม"))
    cs, vols = _vp_data()
    lo, hi = 99, 110
    bins, step = profile(cs, lo, hi, 44, vols)
    poc, vl, vh = value_area(bins)
    panel(s, 28, 90, 904, 410)
    ch = CandleChart(s, 40, 115, 560, 360, cs, pmin=lo, pmax=hi, grid=False)
    vah, val, pocp = lo + (vh + 1) * step, lo + vl * step, lo + (poc + 0.5) * step
    ch.zone(val, vah, C["blue"], None, opacity=0.08)
    ch.draw()
    x0, w = 620, 200
    mx = max(bins)
    for j, v in enumerate(bins):
        y0, y1 = ch.Y(lo + (j + 1) * step), ch.Y(lo + j * step)
        col = C["amber"] if j == poc else (C["blue"] if vl <= j <= vh else C["dim"])
        s.rect(x0, y0 + 0.5, w * v / mx, y1 - y0 - 1, fill=col, opacity=0.85)
    for p, name, col in ((vah, "VAH", C["blue"]), (pocp, "POC", C["amber"]), (val, "VAL", C["blue"])):
        s.line(40, ch.Y(p), x0 + w + 10, ch.Y(p), col, 1.3, "5 4")
        s.text(x0 + w + 16, ch.Y(p) + 5, f"{name} {p:.1f}", 13, col, weight=700)
    lvn = min(range(vh + 1, len(bins) - 3), key=lambda j: bins[j])
    s.text(x0 + w * bins[lvn] / mx + 8, ch.Y(lo + (lvn + 0.5) * step) + 4, t("LVN", "LVN"), 12, C["muted"], weight=700)
    s.text(x0 + 6, 492, t("blue = value area (70%)", "สีน้ำเงิน = Value Area (70%)"), 12, C["blue"])
    return s.render()


@fig
def profile_shapes(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Profile shapes tell the story of the session", "รูปทรงของ Profile เล่าเรื่องของเซสชัน"),
            t("Read the shape before the details.", "อ่านรูปทรงก่อนรายละเอียด"))
    def norm(y, m, sd):
        return math.exp(-((y - m) / sd) ** 2 / 2)
    shapes = [
        (C["blue"], t("D · normal / balanced", "D · ปกติ / สมดุล"), lambda y: norm(y, 0.5, 0.17),
         t("Two-sided trade. Fade the\nedges, target the POC.", "ซื้อขายสองทาง สวนที่ขอบ\nเป้าหมายที่ POC")),
        (C["bull"], t("P · short covering / buying", "P · Short Cover / แรงซื้อ"), lambda y: 0.15 + norm(y, 0.75, 0.12),
         t("Fast rally, then acceptance\nhigh. Often shorts covering.", "ขึ้นเร็ว แล้วถูกยอมรับด้านบน\nมักเป็นการปิด Short")),
        (C["bear"], t("b · long liquidation / selling", "b · ขาย Long / แรงขาย"), lambda y: 0.15 + norm(y, 0.25, 0.12),
         t("Fast drop, then acceptance\nlow. Longs getting out.", "ลงเร็ว แล้วถูกยอมรับด้านล่าง\nคน Long กำลังออก")),
        (C["purple"], t("Double distribution", "Double Distribution"), lambda y: norm(y, 0.25, 0.09) + norm(y, 0.75, 0.09) + 0.03,
         t("Trend day: value moved.\nThe thin middle = LVN.", "วันเทรนด์: มูลค่าย้าย\nตรงกลางที่บาง = LVN")),
    ]
    for k, (col, head, f, body) in enumerate(shapes):
        x = 28 + k * 231
        panel(s, x, 92, 219, 358)
        s.text(x + 110, 120, head, 13, col, "middle", 700)
        n = 32
        vals = [f(1 - (j + 0.5) / n) for j in range(n)]
        mx = max(vals)
        for j, v in enumerate(vals):
            y = 140 + j * 6.5
            s.rect(x + 30, y, 150 * v / mx, 5.5, fill=col, opacity=0.8, rx=1)
        s.text(x + 16, 390, body, 12, C["text"])
    return s.render()


# ---------------------------------------------------------------- 7.3
@fig
def dom(lang):
    t = tr(lang)
    s = SVG(960, 560, t("Level 2 / DOM: the resting orders around price", "Level 2 / DOM: คำสั่งที่รออยู่รอบราคา"),
            t("Shows limit orders waiting (liquidity), not what will trade. Orders can be pulled at any time.",
              "แสดงคำสั่ง Limit ที่รออยู่ (สภาพคล่อง) ไม่ใช่สิ่งที่จะเกิดการซื้อขาย คำสั่งถูกถอนได้ทุกเมื่อ"))
    rows = [(100.06, None, 380), (100.05, None, 2600), (100.04, None, 410), (100.03, None, 520), (100.02, None, 300),
            (100.01, None, 240), (100.00, 260, None), (99.99, 450, None), (99.98, 380, None), (99.97, 520, None),
            (99.96, 3100, None), (99.95, 470, None)]
    x0, y0, rh = 200, 100, 36
    s.text(x0 + 70, y0 + 16, t("BID size", "ฝั่ง BID"), 13, C["bull"], "middle", 700)
    s.text(x0 + 200, y0 + 16, t("Price", "ราคา"), 13, C["muted"], "middle", 700)
    s.text(x0 + 330, y0 + 16, t("ASK size", "ฝั่ง ASK"), 13, C["bear"], "middle", 700)
    y = y0 + 30
    for p, b, a in rows:
        big = (a or 0) > 2000 or (b or 0) > 2000
        s.rect(x0 + 145, y, 110, rh - 4, fill=C["panel"], stroke=C["amber"] if big else C["border"], rx=4)
        s.text(x0 + 200, y + 22, f"{p:.2f}", 14, C["text"], "middle", 600)
        if b:
            w = min(b / 3100, 1) * 130
            s.rect(x0 + 135 - w, y, w, rh - 4, fill=C["bull"], opacity=0.75, rx=4)
            s.text(x0 + 128, y + 22, f"{b:,}", 13, C["white"], "end", 700)
        if a:
            w = min(a / 3100, 1) * 130
            s.rect(x0 + 265, y, w, rh - 4, fill=C["bear"], opacity=0.75, rx=4)
            s.text(x0 + 272, y + 22, f"{a:,}", 13, C["white"], weight=700)
        y += rh
    s.card(650, 100, 282, 130, t("Big ask wall · 100.05", "กำแพง Ask ใหญ่ · 100.05"),
           t("2,600 to sell. Real seller?\nOr bait, pulled when price\ngets close (spoofing)?", "รอขาย 2,600 เป็นผู้ขายจริง?\nหรือเหยื่อล่อที่ถูกถอนเมื่อ\nราคาเข้าใกล้ (Spoofing)?"), C["bear"], 15, 13)
    s.card(650, 244, 282, 130, t("Big bid wall · 99.96", "กำแพง Bid ใหญ่ · 99.96"),
           t("3,100 to buy. Watch what\nhappens when price arrives:\nfilled & holds, or pulled?", "รอซื้อ 3,100 ดูว่าเกิดอะไร\nเมื่อราคามาถึง:\nถูกกินแล้วยืน หรือถูกถอน?"), C["bull"], 15, 13)
    s.card(650, 388, 282, 150, t("Iceberg", "Iceberg"),
           t("Shows 300 at 100.02, but\n2,000 trade there and the 300\nkeeps refilling → a hidden\nlarge order.", "แสดง 300 ที่ 100.02 แต่ซื้อขาย\nไปแล้ว 2,000 และ 300 ยังเติม\nกลับมาเรื่อย ๆ → คำสั่งใหญ่\nที่ซ่อนอยู่"), C["purple"], 15, 13)
    s.text(40, 545, t("Spread = 100.01 − 100.00 = 0.01", "Spread = 100.01 − 100.00 = 0.01"), 13, C["amber"], weight=700)
    return s.render()


# ---------------------------------------------------------------- 7.4
FP = [  # (price, sells_at_bid, buys_at_ask) per level, per candle, top to bottom
    [(100.50, 0, 12), (100.25, 40, 160), (100.00, 120, 410), (99.75, 210, 260), (99.50, 180, 60)],
    [(101.00, 10, 85), (100.75, 60, 390), (100.50, 140, 520), (100.25, 260, 300), (100.00, 90, 40)],
    [(101.25, 30, 20), (101.00, 410, 120), (100.75, 520, 95), (100.50, 300, 140), (100.25, 60, 10)],
]


@fig
def footprint(lang):
    t = tr(lang)
    s = SVG(960, 590, t("Footprint: inside each candle, bid × ask at every price", "Footprint: ภายในแท่ง Bid × Ask ทุกระดับราคา"),
            t("Left number = market SELLS (hit the bid). Right = market BUYS (lifted the ask). Delta = buys − sells.",
              "ตัวเลขซ้าย = Market SELL (ชน Bid) ขวา = Market BUY (กิน Ask) Delta = ซื้อ − ขาย"))
    panel(s, 28, 90, 600, 480)
    hi, lo = 101.25, 99.5
    ytop, rh = 120, 48
    Y = lambda p: ytop + (hi - p) / 0.25 * rh
    for p in [hi - 0.25 * k for k in range(8)]:
        s.text(70, Y(p) + 30, f"{p:.2f}", 12, C["muted"], "end")
    for k, levels in enumerate(FP):
        x = 110 + k * 170
        buys = sum(b for _, _, b in levels)
        sells = sum(a for _, a, _ in levels)
        d = buys - sells
        col = C["bull"] if d > 0 else C["bear"]
        top, bot = levels[0][0], levels[-1][0]
        s.rect(x, Y(top) + 4, 150, Y(bot) - Y(top) + rh - 4, fill=col, opacity=0.07, stroke=col, rx=6)
        for j, (p, sl, by) in enumerate(levels):
            yy = Y(p) + 30
            imb_buy = j + 1 < len(levels) and by >= 100 and by >= 3 * max(levels[j + 1][1], 1)
            imb_sell = j > 0 and sl >= 100 and sl >= 3 * max(levels[j - 1][2], 1)
            s.text(x + 60, yy, f"{sl}", 14, C["bear"] if imb_sell else C["text"], "end", 700 if imb_sell else 400)
            s.text(x + 75, yy, "×", 12, C["dim"], "middle")
            s.text(x + 90, yy, f"{by}", 14, C["bull"] if imb_buy else C["text"], weight=700 if imb_buy else 400)
            if imb_buy:
                s.rect(x + 86, yy - 16, 50, 22, stroke=C["bull"], sw=1.3, rx=4)
            if imb_sell:
                s.rect(x + 14, yy - 16, 50, 22, stroke=C["bear"], sw=1.3, rx=4)
        s.text(x + 75, 530, t(f"Δ {d:+d}", f"Δ {d:+d}"), 15, col, "middle", 700)
        s.text(x + 75, 550, t(f"vol {buys + sells:,}", f"วอลุ่ม {buys + sells:,}"), 11, C["muted"], "middle")
    s.card(650, 92, 282, 150, t("Delta", "Delta"),
           t("Δ = market buys − market sells.\nPositive: buyers more aggressive.\nCandle 3: big negative Δ at the\ntop → sellers stepped in.", "Δ = Market Buy − Market Sell\nบวก: ผู้ซื้อรุกกว่า\nแท่ง 3: Δ ติดลบมากที่ยอด\n→ ผู้ขายเข้ามา"), C["amber"], 16, 13)
    s.card(650, 256, 282, 150, t("Diagonal imbalance", "Imbalance แนวทแยง"),
           t("Compare ask at a price with\nbid one tick lower. ≥ 3× =\nimbalance (boxed). Stacked\nimbalances = strong initiative.", "เทียบ Ask ที่ราคาหนึ่งกับ Bid\nที่ต่ำกว่าหนึ่ง Tick ≥ 3 เท่า =\nImbalance (มีกรอบ) ซ้อนกัน\nหลายชั้น = แรงริเริ่มที่แข็ง"), C["bull"], 16, 13)
    s.card(650, 420, 282, 150, t("Read the story", "อ่านเรื่องราว"),
           t("1–2: buyers lift offers.\n3: buyers stop, sellers hit\nbids at the high → turn?", "1–2: ผู้ซื้อกินฝั่งขาย\n3: ผู้ซื้อหยุด ผู้ขายชน Bid\nที่ยอด → กลับตัว?"), C["purple"], 16, 13)
    return s.render()


@fig
def cvd(lang):
    t = tr(lang)
    s = SVG(960, 520, t("Cumulative delta (CVD): is aggression confirming price?", "Cumulative Delta (CVD): ความรุกยืนยันราคาไหม?"),
            t("Price makes a higher high, CVD makes a lower high → buyers are less aggressive at the new high.",
              "ราคาทำ Higher High แต่ CVD ทำ Lower High → ผู้ซื้อรุกน้อยลงที่จุดสูงใหม่"))
    panel(s, 28, 90, 904, 410)
    price = [100, 101.2, 100.6, 102.4, 103.6, 102.8, 104.2, 105.6, 104.4, 103.6, 104.8, 105.4, 106.1, 105.2, 104.0, 102.6, 101.8]
    cvdv = [0, 400, 250, 900, 1500, 1200, 1800, 2600, 2000, 1700, 2000, 2150, 2250, 1700, 1100, 500, 100]
    n = len(price) - 1
    P = Plot(s, 70, 120, 820, 200, n, 99.5, 107)
    Q = Plot(s, 70, 345, 820, 130, n, -200, 2900)
    s.text(48, 132, t("Price", "ราคา"), 12, C["muted"], weight=700)
    s.text(48, 357, "CVD", 12, C["muted"], weight=700)
    P.path(list(enumerate(price)), C["text"], 2.5)
    Q.path(list(enumerate(cvdv)), C["amber"], 2.5)
    s.line(P.X(7), P.Y(105.6), P.X(12), P.Y(106.1), C["bull"], 2, "5 4")
    s.line(Q.X(7), Q.Y(2600), Q.X(12), Q.Y(2250), C["bear"], 2, "5 4")
    s.text(P.X(12) + 8, P.Y(106.1) - 6, t("higher high", "Higher High"), 13, C["bull"], weight=700)
    s.text(Q.X(12) + 8, Q.Y(2250) - 6, t("lower high", "Lower High"), 13, C["bear"], weight=700)
    s.text(P.X(15), P.Y(102.6) + 26, t("reversal", "กลับตัว"), 13, C["bear"], "middle", 700)
    return s.render()


# ---------------------------------------------------------------- 7.5
@fig
def heatmap(lang):
    t = tr(lang)
    s = SVG(960, 520, t("Liquidity heatmap: resting orders over time", "Liquidity Heatmap: คำสั่งที่รออยู่ตามเวลา"),
            t("Brighter = more resting limit orders at that price and time. The line is the traded price.",
              "สว่างกว่า = คำสั่ง Limit รออยู่ที่ราคาและเวลานั้นมากกว่า เส้นคือราคาที่ซื้อขายจริง"))
    panel(s, 28, 90, 904, 410)
    rnd = random.Random(11)
    nx, ny = 60, 36
    x0, y0, w, h = 60, 115, 640, 360
    cw, chh = w / nx, h / ny
    lo, hi = 98.0, 107.0
    py = lambda j: hi - (j + 0.5) * (hi - lo) / ny
    price = []
    p = 102.4
    for i in range(nx):
        if i < 22:
            p += rnd.uniform(-0.25, 0.25)
            p = min(max(p, 101.2), 103.6)
        elif i < 30:
            p += 0.33
        else:
            p += rnd.uniform(-0.3, 0.32)
            p = min(max(p, 104.3), 106.2)
        price.append(p)
    pulled_at = 26
    for i in range(nx):
        for j in range(ny):
            pp = py(j)
            v = 0.08 + 0.18 * rnd.random()
            if abs(pp - 100.6) < 0.2:
                v += 0.75
            if abs(pp - 104.1) < 0.2 and i < pulled_at:
                v += 0.8
            if abs(pp - 106.6) < 0.2 and i > 28:
                v += 0.6
            v += 0.35 * math.exp(-abs(pp - price[i]) * 1.5)
            v = min(v, 1)
            col = C["amber"] if v > 0.75 else (C["purple"] if v > 0.45 else C["blue"])
            s.rect(x0 + i * cw, y0 + j * chh, cw + 0.3, chh + 0.3, fill=col, opacity=0.12 + 0.75 * v)
    Y = lambda q: y0 + h * (hi - q) / (hi - lo)
    s.polyline([(x0 + (i + 0.5) * cw, Y(q)) for i, q in enumerate(price)], C["white"], 2.5)
    s.card(720, 105, 200, 115, t("Wall that holds", "กำแพงที่ยืนได้"),
           t("Bid wall at 100.6 stays\nall session. Price never\nreaches it: a magnet\nor a floor.", "Bid ใหญ่ที่ 100.6 อยู่\nทั้งเซสชัน ราคาไม่เคย\nไปถึง: แม่เหล็ก\nหรือพื้น"), C["amber"], 15, 12)
    s.card(720, 232, 200, 120, t("Wall that's pulled", "กำแพงที่ถูกถอน"),
           t("Ask wall at 104.1 vanishes\njust before price arrives →\nno real seller → price runs\nthrough.", "Ask ใหญ่ที่ 104.1 หายไป\nก่อนราคามาถึง → ไม่มี\nผู้ขายจริง → ราคาวิ่ง\nทะลุ"), C["pink"], 15, 12)
    s.card(720, 364, 200, 120, t("Caution", "ข้อควรระวัง"),
           t("Resting orders are\nintentions, not trades.\nConfirm with executed\nvolume (footprint, 7.4).", "คำสั่งที่รออยู่คือความตั้งใจ\nไม่ใช่การซื้อขาย ยืนยัน\nด้วยวอลุ่มที่เกิดขึ้นจริง\n(Footprint, 7.4)"), C["muted"], 15, 12)
    s.line(x0 + pulled_at * cw, y0, x0 + pulled_at * cw, y0 + h, C["pink"], 1.2, "3 3")
    return s.render()


# ---------------------------------------------------------------- 7.6
def _with_delta(s, x, y, w, h, cs, deltas, vols, hl=None, notes=()):
    ch = CandleChart(s, x, y, w, h * 0.62, cs, grid=False)
    by, bh = y + h * 0.70, h * 0.28
    mx = max(abs(d) for d in deltas)
    mid = by + bh / 2
    s.line(x, mid, x + w, mid, C["dim"], 1)
    for i, d in enumerate(deltas):
        col = C["bull"] if d > 0 else C["bear"]
        hh = (bh / 2 - 2) * abs(d) / mx
        s.rect(ch.X(i) - ch.step * 0.3, mid - hh if d > 0 else mid, ch.step * 0.6, hh, fill=col, opacity=0.8, rx=1)
    s.text(x, by - 4, t_delta[0], 11, C["muted"], weight=700)
    return ch


t_delta = ["delta"]


@fig
def absorption(lang):
    t = tr(lang)
    t_delta[0] = t("delta per candle", "Delta ต่อแท่ง")
    s = SVG(960, 520, t("Absorption: aggression without progress", "Absorption: รุกหนักแต่ราคาไม่ไปไหน"),
            t("Heavy market selling into support, but price stops falling → a large passive buyer is absorbing it.",
              "แรงขาย Market หนักใส่แนวรับ แต่ราคาหยุดลง → ผู้ซื้อ Passive รายใหญ่กำลังดูดซับ"))
    pre, _ = walk([106, 101.6, 103.2, 100.8], [5, 3, 4], seed=33)
    o = pre[-1][3]
    absorb = [[o, o + 0.3, 100.1, 100.6], [100.6, 100.9, 100.05, 100.4], [100.4, 100.8, 100.1, 100.5], [100.5, 101.6, 100.2, 101.4]]
    cs = extend(pre, absorb)
    post, _ = walk([101.4, 103.4, 102.6, 105.6], [3, 2, 4], seed=34)
    cs = extend(cs, post[1:])
    deltas = [-300, -420, -380, -500, -200, 250, 180, -350, -280, -400, -310, -450][:len(pre)]
    deltas += [-1500, -1800, -1650, 900] + [1200, 700, 400, -200, 800, 900, 600, 500, 400][:len(cs) - len(pre) - 4]
    panel(s, 28, 90, 640, 410)
    ch = _with_delta(s, 44, 110, 608, 380, cs, deltas, None)
    a0 = len(pre)
    ch.zone(99.9, 100.7, C["bull"], t("support", "แนวรับ"), i0=a0 - 2, i1=a0 + 3, opacity=0.18, label_side="left", label_pos="below")
    ch.draw(highlight={a0: C["amber"], a0 + 1: C["amber"], a0 + 2: C["amber"]})
    s.card(684, 92, 248, 200, t("What you see", "สิ่งที่เห็น"),
           t("· 3 candles of big NEGATIVE Δ\n· lows barely move (~100.1)\n· long lower wicks\n· then a close above the\n  absorption range", "· Δ ติดลบมาก 3 แท่ง\n· จุดต่ำแทบไม่ขยับ (~100.1)\n· ไส้ล่างยาว\n· แล้วปิดเหนือกรอบ\n  ที่ดูดซับ"), C["amber"], 16, 13)
    s.card(684, 306, 248, 194, t("What it means", "ความหมาย"),
           t("Sellers hit the bid hard, but a\npassive buyer filled all of it.\nWhen sellers run out, price\nlifts: sellers are trapped\n→ fuel for the move up.", "ผู้ขายชน Bid หนัก แต่ผู้ซื้อ\nPassive รับไว้ทั้งหมด เมื่อ\nผู้ขายหมดแรง ราคาก็ขึ้น:\nผู้ขายติดกับ → เชื้อเพลิง\nของการขึ้น"), C["bull"], 16, 13)
    return s.render()


@fig
def exhaustion(lang):
    t = tr(lang)
    t_delta[0] = t("delta per candle", "Delta ต่อแท่ง")
    s = SVG(960, 520, t("Exhaustion: the push runs out of buyers", "Exhaustion: แรงดันหมดผู้ซื้อ"),
            t("Each new high attracts less aggressive buying. The last push into liquidity has the weakest delta.",
              "จุดสูงใหม่แต่ละครั้งดึงแรงซื้อเชิงรุกได้น้อยลง การดันครั้งสุดท้ายเข้ากองสภาพคล่องมี Delta อ่อนที่สุด"))
    up = [[100, 101.6, 99.8, 101.4], [101.4, 103.2, 101.2, 103.0], [103.0, 104.3, 102.6, 104.0], [104.0, 104.6, 103.2, 103.5],
          [103.5, 105.1, 103.3, 104.8], [104.8, 105.6, 104.4, 105.2], [105.2, 106.2, 104.9, 105.4], [105.4, 106.6, 105.1, 105.5],
          [105.5, 106.9, 104.6, 104.8], [104.8, 105.0, 103.2, 103.4], [103.4, 103.9, 102.1, 102.4], [102.4, 103.1, 101.6, 101.9],
          [101.9, 102.5, 100.8, 101.0]]
    deltas = [900, 1300, 800, -200, 600, 420, 260, 150, -900, -1200, -800, -500, -600]
    panel(s, 28, 90, 640, 410)
    ch = _with_delta(s, 44, 110, 608, 380, up, deltas, None)
    ch.hline(106.5, t("BSL (equal highs)", "BSL (จุดสูงเท่ากัน)"), C["amber"], 0, None, "4 4", side="left", size=12)
    ch.draw(highlight={8: C["bear"]})
    s.card(684, 92, 248, 200, t("What you see", "สิ่งที่เห็น"),
           t("· higher highs: 104.3 → 105.6\n  → 106.2 → 106.6 → 106.9\n· delta shrinks: +800 → +420\n  → +260 → +150\n· sweep of BSL, close back\n  below, big negative Δ", "· จุดสูงสูงขึ้น: 104.3 → 105.6\n  → 106.2 → 106.6 → 106.9\n· Delta หดลง: +800 → +420\n  → +260 → +150\n· กวาด BSL ปิดกลับลงมา\n  Δ ติดลบมาก"), C["amber"], 16, 13)
    s.card(684, 306, 248, 194, t("What it means", "ความหมาย"),
           t("Buyers are running out. The\nlast high was made by stops\n(BSL) more than by initiative\nbuying. Confirm with a CHoCH\nbefore acting (5.2).", "ผู้ซื้อกำลังหมด จุดสูงสุดท้าย\nเกิดจาก Stop (BSL) มากกว่า\nการซื้อเชิงริเริ่ม ยืนยันด้วย\nCHoCH ก่อนลงมือ (5.2)"), C["bear"], 16, 13)
    return s.render()


# ---------------------------------------------------------------- 7.7
@fig
def summary(lang):
    t = tr(lang)
    s = SVG(960, 560, t("Phase 7 on one page", "สรุปเฟส 7 ในหน้าเดียว"))
    cx, cy = 480, 310
    nodes = [
        (170, 140, C["blue"], t("7.1 Auction", "7.1 การประมูล"), t("Balance ↔ imbalance.\nResponsive vs initiative.", "สมดุล ↔ ไม่สมดุล\nตอบสนอง vs ริเริ่ม")),
        (790, 140, C["amber"], t("7.2 Volume profile", "7.2 Volume Profile"), t("POC · VAH · VAL · LVN.\nValue = 70% of volume.", "POC · VAH · VAL · LVN\nมูลค่า = 70% ของวอลุ่ม")),
        (150, 320, C["bull"], t("7.3 DOM", "7.3 DOM"), t("Resting orders = intentions.\nWalls can be pulled.", "คำสั่งที่รอ = ความตั้งใจ\nกำแพงถูกถอนได้")),
        (810, 320, C["purple"], t("7.4 Footprint & delta", "7.4 Footprint & Delta"), t("Buys − sells per price.\nCVD divergence.", "ซื้อ − ขาย ต่อระดับราคา\nCVD Divergence")),
        (250, 480, C["pink"], t("7.5 Heatmaps", "7.5 Heatmap"), t("Liquidity over time.\nHeld vs pulled walls.", "สภาพคล่องตามเวลา\nกำแพงที่ยืน vs ถูกถอน")),
        (710, 480, C["teal"], t("7.6 Absorption", "7.6 Absorption"), t("Aggression without progress.\nExhaustion at liquidity.", "รุกแต่ราคาไม่ไป\nหมดแรงที่กองสภาพคล่อง")),
    ]
    for x, y, col, head, body in nodes:
        s.line(cx, cy, x, y, col, 2, opacity=0.5)
    s.circle(cx, cy, 74, C["panel"], C["text"], 2)
    s.text(cx, cy - 4, t("PHASE 7", "เฟส 7"), 20, C["text"], "middle", 700)
    s.text(cx, cy + 20, t("Orderflow", "ออเดอร์โฟลว์"), 14, C["muted"], "middle")
    for x, y, col, head, body in nodes:
        s.rect(x - 130, y - 42, 260, 92, fill=C["panel"], stroke=col, rx=12)
        s.text(x, y - 14, head, 17, col, "middle", 700)
        s.text(x, y + 10, body, 13, C["text"], "middle")
    return s.render()


# ================================================================ v2 additions (Oct 2026)
@fig
def night_market(lang):
    t = tr(lang)
    s = SVG(960, 470, t("A night-market stall runs an auction every evening", "แผงตลาดนัดกลางคืนก็คือการประมูลทุกเย็น"),
            t("Mango sticky rice, price per box (THB). Price moves to find buyers; volume shows where they agree.",
              "ข้าวเหนียวมะม่วง ราคาต่อกล่อง (บาท) ราคาขยับเพื่อหาผู้ซื้อ ปริมาณขายบอกว่าตกลงกันที่ไหน"))
    steps = [(C["muted"], "18:00", "60", t("long queue", "คิวยาว"), 40, t("too cheap → raise", "ถูกไป → ขึ้นราคา")),
             (C["bull"], "18:30", "70", t("steady sales", "ขายได้เรื่อย ๆ"), 120, t("fair: most boxes sold", "ยุติธรรม: ขายได้มากที่สุด")),
             (C["bear"], "19:00", "80", t("nobody stops", "ไม่มีใครแวะ"), 5, t("too dear → lower", "แพงไป → ลดราคา")),
             (C["bull"], "19:30", "70", t("sales return", "ขายได้อีกครั้ง"), 110, t("back to value = BALANCE", "กลับสู่มูลค่า = สมดุล")),
             (C["amber"], "20:00", "90", t("tour buses arrive", "รถทัวร์มาถึง"), 150, t("new info → new value\n= IMBALANCE", "ข้อมูลใหม่ → มูลค่าใหม่\n= ไม่สมดุล"))]
    for k, (col, tm, price, note, sold, read) in enumerate(steps):
        x = 28 + k * 184
        s.rect(x, 96, 172, 330, fill=C["panel"], stroke=col, rx=12)
        s.text(x + 86, 124, tm, 14, C["muted"], "middle", 700)
        s.text(x + 86, 166, price + t(" THB", " บาท"), 26, col, "middle", 800)
        s.text(x + 86, 194, note, 13, C["text"], "middle", 600)
        h = sold * 0.95
        s.rect(x + 56, 360 - h, 60, h, fill=col, opacity=0.6, rx=4)
        s.text(x + 86, 376, t(f"{sold} boxes", f"{sold} กล่อง"), 12, C["text"], "middle")
        s.text(x + 86, 400, read, 11, col, "middle", 700)
    s.text(48, 452, t("Price advertises (raise/lower), time regulates (how long a price lasts), volume validates (boxes sold).",
                      "ราคาประกาศ (ขึ้น/ลด) เวลากำกับ (ราคาอยู่ได้นานแค่ไหน) ปริมาณยืนยัน (จำนวนกล่องที่ขายได้)"), 13, C["amber"], weight=600)
    return s.render()


PBH = [(100, 103, 400), (102, 105, 600), (103, 106, 800), (104, 106, 900), (104, 107, 800),
       (105, 107, 600), (103, 105, 600), (104, 105, 400), (105, 108, 400), (107, 109, 300)]


@fig
def profile_by_hand(lang):
    t = tr(lang)
    s = SVG(960, 540, t("Building a volume profile by hand from 10 candles", "สร้าง Volume profile ด้วยมือจาก 10 แท่งเทียน"),
            t("Each candle's volume is spread evenly over the prices it traded. Add up each row.",
              "กระจายวอลุ่มของแต่ละแท่งเท่า ๆ กันตามราคาที่แท่งนั้นซื้อขาย แล้วรวมแต่ละแถว"))
    rows = {p: 0.0 for p in range(100, 110)}
    for lo, hi, v in PBH:
        for p in range(lo, hi + 1):
            rows[p] += v / (hi - lo + 1)
    s.text(48, 112, t("Candle  low–high  volume", "แท่ง  ต่ำ–สูง  วอลุ่ม"), 13, C["muted"], weight=700)
    for k, (lo, hi, v) in enumerate(PBH):
        s.text(48, 140 + k * 26, f"{k + 1:>2}    {lo}–{hi}    {v}", 13, C["text"])
        s.text(240, 140 + k * 26, t(f"→ {v // (hi - lo + 1)} per row", f"→ แถวละ {v // (hi - lo + 1)}"), 12, C["muted"])
    s.text(48, 420, t("Total volume = 5,800\n70% of it = 4,060", "วอลุ่มรวม = 5,800\n70% = 4,060"), 14, C["amber"], weight=700)
    x0, y0, rh = 470, 100, 36
    for i, p in enumerate(range(109, 99, -1)):
        y = y0 + i * rh
        v = rows[p]
        col = C["amber"] if p == 105 else (C["blue"] if 103 <= p <= 106 else C["dim"])
        s.text(x0 - 12, y + 23, str(p), 14, C["text"], "end", 600)
        s.rect(x0, y + 6, v * 0.22, rh - 10, fill=col, rx=4, opacity=0.9)
        s.text(x0 + v * 0.22 + 8, y + 24, f"{v:,.0f}", 13, C["text"], weight=600)
    s.text(x0 + 12, y0 + 4 * rh + 23, t("POC 105", "POC 105"), 14, C["bg"], weight=800)
    s.text(x0 + 300, y0 + 3 * rh + 24, t("VAH 106", "VAH 106"), 13, C["blue"], weight=700)
    s.text(x0 + 200, y0 + 6 * rh + 24, t("VAL 103", "VAL 103"), 13, C["blue"], weight=700)
    s.text(x0 + 120, y0 + 0 * rh + 24, t("LVN: thin, price moved fast", "LVN: บาง ราคาวิ่งผ่านเร็ว"), 12, C["muted"])
    s.text(x0 - 20, 488, t("Value area 103–106 = 4,450 of 5,800 = 76.7% (first total ≥ 70%)", "Value area 103–106 = 4,450 จาก 5,800 = 76.7% (ยอดแรกที่ ≥ 70%)"), 14, C["blue"], weight=700)
    return s.render()


@fig
def dom_frames(lang):
    t = tr(lang)
    s = SVG(960, 520, t("Five seconds on the ES DOM, in three frames (illustrative)", "ห้าวินาทีบน DOM ของ ES ในสามภาพ (ภาพประกอบ)"),
            t("E-mini S&P 500 futures. 1 tick = 0.25 points. Watch what TRADES, not what is shown.",
              "ฟิวเจอร์ส E-mini S&P 500  1 tick = 0.25 จุด ดูว่าอะไร ซื้อขายจริง ไม่ใช่อะไรถูกแสดง"))
    prices = [5000.75, 5000.50, 5000.25, 5000.00, 4999.75, 4999.50, 4999.25, 4999.00, 4998.75, 4998.50, 4998.25, 4998.00]
    frames = [
        (t("0 s · start", "0 วิ · เริ่ม"), {5000.75: (420, 0), 5000.50: (300, 0), 5000.25: (0, 250), 5000.00: (0, 310), 4999.75: (0, 280), 4999.50: (0, 300), 4999.25: (0, 260), 4999.00: (0, 330), 4998.75: (0, 290), 4998.50: (0, 270), 4998.25: (0, 310), 4998.00: (0, 1800)}, 5000.25, None),
        (t("2 s · sellers hit the bid", "2 วิ · ผู้ขายกดใส่ Bid"), {5000.75: (420, 0), 5000.50: (300, 0), 5000.25: (240, 0), 5000.00: (0, 60), 4999.75: (0, 280), 4999.50: (0, 300), 4999.25: (0, 260), 4999.00: (0, 330), 4998.75: (0, 290), 4998.50: (0, 270), 4998.25: (0, 310), 4998.00: (0, 1800)}, 5000.00, t("traded: 250 @ 5000.25\n+ 250 @ 5000.00", "ซื้อขายจริง: 250 @ 5000.25\n+ 250 @ 5000.00")),
        (t("5 s · the wall vanishes", "5 วิ · กำแพงหายไป"), {5000.75: (420, 0), 5000.50: (300, 0), 5000.25: (240, 0), 5000.00: (0, 60), 4999.75: (0, 280), 4999.50: (0, 300), 4999.25: (0, 260), 4999.00: (0, 330), 4998.75: (0, 290), 4998.50: (0, 270), 4998.25: (0, 310), 4998.00: (0, 200)}, 5000.00, t("1,800 → 200 with NO trade:\npulled, not filled", "1,800 → 200 โดย ไม่มี การซื้อขาย:\nถูกถอน ไม่ได้ถูกเติม"))]
    for k, (title, book, last, note) in enumerate(frames):
        x = 28 + k * 308
        panel(s, x, 90, 296, 410, title, C["blue"] if k < 2 else C["bear"], 14)
        s.text(x + 60, 140, t("Bid", "Bid"), 12, C["bull"], "middle", 700)
        s.text(x + 148, 140, t("Price", "ราคา"), 12, C["muted"], "middle", 700)
        s.text(x + 236, 140, t("Ask", "Ask"), 12, C["bear"], "middle", 700)
        for i, p in enumerate(prices):
            y = 150 + i * 22
            ask, bid = book[p]
            if p == last:
                s.rect(x + 104, y + 2, 88, 20, fill=C["amber"], opacity=0.25, rx=3)
            s.text(x + 148, y + 17, f"{p:.2f}", 12, C["text"], "middle")
            if bid:
                big = bid >= 1000 or (k == 2 and p == 4998.00)
                s.rect(x + 14, y + 4, min(bid, 600) * 0.06, 16, fill=C["bear"] if (k == 2 and p == 4998.00) else C["bull"], opacity=0.75, rx=2)
                s.text(x + 96, y + 17, f"{bid:,}", 12, C["amber"] if big else C["text"], "end", 700 if big else 400)
            if ask:
                s.rect(x + 200, y + 4, min(ask, 600) * 0.08, 16, fill=C["bear"], opacity=0.75, rx=2)
                s.text(x + 280, y + 17, f"{ask:,}", 12, C["text"], "end")
        if note:
            s.text(x + 18, 438, note, 12, C["amber"] if k == 1 else C["bear"], weight=700)
    return s.render()


@fig
def single_trade(lang):
    t = tr(lang)
    s = SVG(960, 470, t("How trades land on a footprint: bid × ask", "การซื้อขายลงบน Footprint อย่างไร: Bid × Ask"),
            t("Best bid 100.00 / best ask 100.25. Two market orders, then the diagonal imbalance check.",
              "Bid ดีที่สุด 100.00 / Ask ดีที่สุด 100.25 คำสั่ง Market สองคำสั่ง แล้วตรวจ Diagonal imbalance"))
    panel(s, 28, 90, 440, 350, t("1 · Two single trades", "1 · การซื้อขายสองครั้ง"), C["text"], 15)
    rows = [("100.25", "0", "5"), ("100.00", "3", "0")]
    s.text(80, 160, t("Price    sells × buys", "ราคา    ขาย × ซื้อ"), 13, C["muted"], weight=700)
    for i, (p, sl, by) in enumerate(rows):
        y = 186 + i * 40
        s.rect(60, y - 22, 300, 34, fill=C["bg"], stroke=C["border"], rx=6)
        s.text(80, y, p, 15, C["text"], weight=600)
        s.text(210, y, sl, 15, C["bear"], "end", 700)
        s.text(232, y, "×", 15, C["muted"], "middle")
        s.text(254, y, by, 15, C["bull"], "start", 700)
    s.text(48, 290, t("A buys 5 with a MARKET order → fills at the\nask 100.25 → right column: 0 × 5\nB sells 3 with a MARKET order → fills at the\nbid 100.00 → left column: 3 × 0\nDelta = buys − sells = 5 − 3 = +2",
                      "A ซื้อ 5 ด้วยคำสั่ง MARKET → ได้ที่\nAsk 100.25 → คอลัมน์ขวา: 0 × 5\nB ขาย 3 ด้วยคำสั่ง MARKET → ได้ที่\nBid 100.00 → คอลัมน์ซ้าย: 3 × 0\nDelta = ซื้อ − ขาย = 5 − 3 = +2"), 13, C["text"])
    panel(s, 492, 90, 440, 350, t("2 · Diagonal imbalance (≥ 3×)", "2 · Diagonal imbalance (≥ 3 เท่า)"), C["text"], 15)
    rows2 = [("100.50", "90", "210"), ("100.25", "140", "450"), ("100.00", "120", "160")]
    s.text(544, 160, t("Price    sells × buys", "ราคา    ขาย × ซื้อ"), 13, C["muted"], weight=700)
    for i, (p, sl, by) in enumerate(rows2):
        y = 186 + i * 40
        s.rect(524, y - 22, 300, 34, fill=C["bg"], stroke=C["border"], rx=6)
        s.text(544, y, p, 15, C["text"], weight=600)
        s.text(674, y, sl, 15, C["bear"], "end", 700)
        s.text(696, y, "×", 15, C["muted"], "middle")
        s.text(718, y, by, 15, C["bull"], "start", 700)
    s.arrow(735, 222, 670, 260, C["amber"], 2)
    s.text(840, 230, t("450 ÷ 120\n= 3.75 ✓", "450 ÷ 120\n= 3.75 ✓"), 14, C["amber"], "middle", 700)
    s.text(512, 330, t("Buyers at 100.25 vs sellers one tick LOWER\n(100.00): 450 vs 120 → buy imbalance.\nStraight across (450 vs 140) would be wrong:\nthose trades happened at different prices.",
                       "ผู้ซื้อที่ 100.25 เทียบผู้ขายที่ต่ำกว่าหนึ่ง tick\n(100.00): 450 กับ 120 → Buy imbalance\nเทียบแนวนอน (450 กับ 140) ผิด:\nเพราะเกิดคนละราคา"), 13, C["text"])
    return s.render()


@fig
def heatmap_frames(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Heatmap: the same wall, two endings (illustrative)", "Heatmap: กำแพงเดียวกัน สองตอนจบ (ภาพประกอบ)"),
            t("Brighter = more resting limit orders. Bubbles = real executed trades.", "ยิ่งสว่าง = คำสั่ง Limit รออยู่มาก  ฟอง = การซื้อขายที่เกิดจริง"))
    for k, (title, col, held) in enumerate(((t("A · Absorbing: the wall holds", "A · ดูดซับ: กำแพงยืนได้"), C["bull"], True),
                                            (t("B · Pulling: the wall vanishes", "B · ถอน: กำแพงหายไป"), C["bear"], False))):
        bx = 28 + k * 462
        panel(s, bx, 90, 442, 390, title, col, 15)
        X0, Y0, W, H = bx + 20, 130, 400, 300
        for j in range(16):
            x = X0 + j * W / 16
            for r in range(12):
                y = Y0 + r * H / 12
                b = 0.05 + 0.08 * ((j * 7 + r * 3) % 5) / 5
                s.rect(x, y, W / 16 - 1, H / 12 - 1, fill=C["blue"], opacity=b)
            wall_on = held or j < 11
            if wall_on:
                s.rect(x, Y0 + 9 * H / 12, W / 16 - 1, H / 12 - 1, fill=C["amber"], opacity=0.85)
        path = [(0, 2), (3, 4), (6, 5), (9, 7), (11, 8.4)] + ([(12, 8.8), (13, 8.7), (14, 7), (16, 4)] if held else [(12, 9.5), (13, 10.6), (14, 11.5), (16, 11.8)])
        pts = [(X0 + a * W / 16, Y0 + b * H / 12) for a, b in path]
        s.polyline(pts, C["white"], 2.5)
        if held:
            for a, rad in ((12, 10), (12.7, 14), (13.3, 8)):
                s.circle(X0 + a * W / 16, Y0 + 9.2 * H / 12, rad, C["bull"])
            s.text(X0 + 4, Y0 + 9 * H / 12 - 8, t("wall 4,998.00: trades print, wall stays", "กำแพง 4,998.00: มีการซื้อขาย กำแพงยังอยู่"), 12, C["bull"], weight=700)
        else:
            s.text(X0 + 4, Y0 + 9 * H / 12 - 8, t("wall 4,998.00 disappears, NO bubbles", "กำแพง 4,998.00 หายไป ไม่มีฟอง"), 12, C["bear"], weight=700)
        s.text(X0, 462, t("→ real support: absorption (7.6)" if held else "→ no support: price falls through",
                          "→ แนวรับจริง: การดูดซับ (7.6)" if held else "→ ไม่มีแนวรับ: ราคาร่วงผ่าน"), 13, col, weight=700)
    return s.render()


@fig
def tapes(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Classify the tape: two sequences of trades (prints)", "จำแนก Tape: ลำดับการซื้อขายสองชุด (Prints)"),
            t("Each line is one executed trade: time, price, size, and which side was aggressive.",
              "แต่ละบรรทัดคือการซื้อขายที่เกิดจริงหนึ่งครั้ง: เวลา ราคา ขนาด และฝั่งไหนรุก"))
    tapes_ = [(t("Tape A · at support 100.10", "Tape A · ที่แนวรับ 100.10"),
               [("10:01:05", "100.10", "300", t("sell (hit bid)", "ขาย (กด Bid)")), ("10:01:09", "100.10", "250", t("sell (hit bid)", "ขาย (กด Bid)")),
                ("10:01:14", "100.10", "400", t("sell (hit bid)", "ขาย (กด Bid)")), ("10:01:20", "100.10", "350", t("sell (hit bid)", "ขาย (กด Bid)")),
                ("10:01:27", "100.10", "280", t("sell (hit bid)", "ขาย (กด Bid)")), ("10:01:33", "100.15", "120", t("buy (lift ask)", "ซื้อ (ยก Ask)"))],
               t("1,580 sold at 100.10, price never lower;\nvisible bid only ever showed ~100", "ขาย 1,580 ที่ 100.10 ราคาไม่ลงต่ำกว่านั้น\nBid ที่มองเห็นแสดงแค่ราว 100")),
              (t("Tape B · at new highs", "Tape B · ที่จุดสูงใหม่"),
               [("14:20:02", "101.20", "400", t("buy (lift ask)", "ซื้อ (ยก Ask)")), ("14:20:31", "101.30", "250", t("buy (lift ask)", "ซื้อ (ยก Ask)")),
                ("14:21:05", "101.40", "120", t("buy (lift ask)", "ซื้อ (ยก Ask)")), ("14:21:48", "101.45", "60", t("buy (lift ask)", "ซื้อ (ยก Ask)")),
                ("14:22:10", "101.35", "300", t("sell (hit bid)", "ขาย (กด Bid)")), ("14:22:15", "101.30", "280", t("sell (hit bid)", "ขาย (กด Bid)"))],
               t("each new high needs less buying\n(400 → 250 → 120 → 60), then sellers hit", "จุดสูงใหม่แต่ละครั้งใช้แรงซื้อน้อยลง\n(400 → 250 → 120 → 60) แล้วผู้ขายกดลงมา"))]
    for k, (title, rows, note) in enumerate(tapes_):
        bx = 28 + k * 462
        panel(s, bx, 90, 442, 390, title, C["amber"], 15)
        for j, h in enumerate((t("time", "เวลา"), t("price", "ราคา"), t("size", "ขนาด"), t("aggressor", "ฝั่งที่รุก"))):
            s.text(bx + 24 + [0, 100, 180, 250][j], 150, h, 12, C["muted"], weight=700)
        for i, (tm, p, sz, side) in enumerate(rows):
            y = 180 + i * 30
            col = C["bear"] if "sell" in side or "ขาย" in side else C["bull"]
            for j, v in enumerate((tm, p, sz, side)):
                s.text(bx + 24 + [0, 100, 180, 250][j], y, v, 13, col if j == 3 else C["text"], weight=600 if j == 2 else 400)
        s.text(bx + 24, 382, note, 12, C["text"])
        s.text(bx + 24, 452, t("Absorption or exhaustion? (answer in the lesson)", "Absorption หรือ Exhaustion? (เฉลยในบทเรียน)"), 12, C["amber"], weight=700)
    return s.render()
