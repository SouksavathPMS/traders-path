"""Phase 8 figures: Options & Dealer Positioning (GEX). Uses Black-Scholes (r = 0)."""
import math
import random
from charts import SVG, C, tr
from figures.p2 import panel
from figures.p6 import Plot

FIGURES = {}


def fig(fn):
    FIGURES["p8-" + fn.__name__.replace("_", "-")] = fn
    return fn


# ---------------------------------------------------------------- Black-Scholes
def N(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def n(x):
    return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)


def bs(S, K, T, iv, kind="c"):
    """Returns dict(price, delta, gamma, theta_day, vega_pt). T in years."""
    T = max(T, 1e-6)
    d1 = (math.log(S / K) + 0.5 * iv * iv * T) / (iv * math.sqrt(T))
    d2 = d1 - iv * math.sqrt(T)
    if kind == "c":
        price, delta = S * N(d1) - K * N(d2), N(d1)
    else:
        price, delta = K * N(-d2) - S * N(-d1), N(d1) - 1
    gamma = n(d1) / (S * iv * math.sqrt(T))
    theta = -S * n(d1) * iv / (2 * math.sqrt(T)) / 365
    vega = S * n(d1) * math.sqrt(T) / 100
    return dict(price=price, delta=delta, gamma=gamma, theta=theta, vega=vega)


# Synthetic index option chain (contracts of open interest), spot 5,000, 20 days, IV 16%
SPOT, T_CHAIN, IV_CHAIN = 5000.0, 20 / 365, 0.16
STRIKES = list(range(4700, 5301, 50))
CALL_OI = {4900: 8000, 4950: 12000, 5000: 30000, 5050: 38000, 5100: 70000, 5150: 30000, 5200: 45000, 5250: 15000, 5300: 12000}
PUT_OI = {4700: 25000, 4750: 18000, 4800: 45000, 4850: 30000, 4900: 75000, 4950: 40000, 5000: 30000, 5050: 10000}


def gex_by_strike(S):
    """Dealer GEX per strike in $bn per 1% move. Convention: dealers long calls, short puts."""
    out = {}
    for K in STRIKES:
        g = bs(S, K, T_CHAIN, IV_CHAIN)["gamma"]
        dollar = g * 100 * S * S * 0.01 / 1e9
        out[K] = dollar * CALL_OI.get(K, 0) - dollar * PUT_OI.get(K, 0)
    return out


def total_gex(S):
    return sum(gex_by_strike(S).values())


def gamma_flip():
    lo, hi = 4800.0, 5200.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if total_gex(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


# ---------------------------------------------------------------- 8.1
@fig
def payoff(lang):
    t = tr(lang)
    s = SVG(960, 520, t("Option payoffs at expiry", "ผลตอบแทนของออปชันตอนหมดอายุ"),
            t("Strike 100, premium 3. Buyers risk only the premium; sellers collect it and take the open-ended risk.",
              "Strike 100 ค่าพรีเมียม 3 ผู้ซื้อเสี่ยงแค่ค่าพรีเมียม ผู้ขายเก็บค่าพรีเมียมแต่รับความเสี่ยงที่ไม่จำกัด"))
    specs = [
        (t("Long call", "ซื้อ Call"), C["bull"], lambda S: max(S - 100, 0) - 3, t("Bullish. Max loss 3.\nBreak-even 103.", "มองขึ้น ขาดทุนสูงสุด 3\nจุดคุ้มทุน 103")),
        (t("Long put", "ซื้อ Put"), C["bear"], lambda S: max(100 - S, 0) - 3, t("Bearish / hedge. Max loss 3.\nBreak-even 97.", "มองลง / ป้องกัน ขาดทุนสูงสุด 3\nจุดคุ้มทุน 97")),
        (t("Short call", "ขาย Call"), C["amber"], lambda S: 3 - max(S - 100, 0), t("Max gain 3. Loss grows\nwithout limit as price rises.", "กำไรสูงสุด 3 ขาดทุนไม่จำกัด\nเมื่อราคาขึ้น")),
        (t("Short put", "ขาย Put"), C["purple"], lambda S: 3 - max(100 - S, 0), t("Max gain 3. Large loss\nif price collapses.", "กำไรสูงสุด 3 ขาดทุนมาก\nถ้าราคาร่วง")),
    ]
    for k, (head, col, f, body) in enumerate(specs):
        x = 28 + k * 231
        panel(s, x, 90, 219, 410, head, col)
        P = Plot(s, x + 18, 140, 183, 220, 1, -12, 12)
        X = lambda S: x + 18 + 183 * (S - 85) / 30
        s.line(x + 14, P.Y(0), x + 205, P.Y(0), C["dim"], 1)
        s.line(X(100), 140, X(100), 360, C["dim"], 1, "3 3")
        pts = [(X(S), P.Y(max(min(f(S), 12), -12))) for S in [85 + i * 0.5 for i in range(61)]]
        s.polyline(pts, col, 3)
        s.text(X(100), 378, "K=100", 11, C["muted"], "middle")
        s.text(x + 14, 410, body, 13, C["text"])
    return s.render()


@fig
def moneyness(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Moneyness and what you pay for", "Moneyness และสิ่งที่คุณจ่ายเงินซื้อ"),
            t("Premium = intrinsic value + time value. Stock at 100, 30 days, implied volatility 30%.",
              "ค่าพรีเมียม = มูลค่าที่แท้จริง + มูลค่าเวลา หุ้นที่ 100 อายุ 30 วัน ความผันผวนแฝง 30%"))
    panel(s, 28, 90, 904, 360)
    strikes = [90, 95, 100, 105, 110]
    x0 = 140
    heads = [t("Strike", "Strike"), t("Call premium", "พรีเมียม Call"), t("intrinsic", "มูลค่าแท้"), t("time", "มูลค่าเวลา"),
             t("Call is…", "Call เป็น…"), t("Put is…", "Put เป็น…")]
    xs = [70, 200, 330, 450, 570, 740]
    for hx, h in zip(xs, heads):
        s.text(hx, 130, h, 13, C["muted"], weight=700)
    for r, K in enumerate(strikes):
        y = 170 + r * 52
        c = bs(100, K, 30 / 365, 0.30, "c")
        intr = max(100 - K, 0)
        tv = c["price"] - intr
        s.rect(50, y - 26, 860, 44, fill=C["amber"] if K == 100 else C["panel"], opacity=0.12 if K == 100 else 1, rx=8)
        s.text(70, y, f"{K}", 15, C["text"], weight=700)
        s.text(200, y, f"{c['price']:.2f}", 15, C["text"], weight=700)
        s.rect(330, y - 14, intr * 6, 18, fill=C["bull"], opacity=0.8, rx=3)
        s.text(330 + intr * 6 + 6, y, f"{intr:.2f}", 13, C["bull"])
        s.rect(450, y - 14, tv * 20, 18, fill=C["blue"], opacity=0.8, rx=3)
        s.text(450 + tv * 20 + 6, y, f"{tv:.2f}", 13, C["blue"])
        mc = "ITM" if K < 100 else ("ATM" if K == 100 else "OTM")
        mp = "OTM" if K < 100 else ("ATM" if K == 100 else "ITM")
        col = {"ITM": C["bull"], "ATM": C["amber"], "OTM": C["muted"]}
        s.text(570, y, mc, 15, col[mc], weight=700)
        s.text(740, y, mp, 15, col[mp], weight=700)
    s.text(50, 438, t("Time value is largest at the money and decays to zero by expiry (theta, 8.2).",
                      "มูลค่าเวลาสูงสุดที่ ATM และลดลงเหลือศูนย์ตอนหมดอายุ (Theta, 8.2)"), 13, C["amber"], weight=600)
    return s.render()


# ---------------------------------------------------------------- 8.2
@fig
def greeks(lang):
    t = tr(lang)
    s = SVG(960, 585, t("The four Greeks you need", "Greeks 4 ตัวที่ต้องรู้"),
            t("How an option's price reacts to price, time and volatility (call, strike 100, IV 30%).",
              "ราคาออปชันตอบสนองต่อราคา เวลา และความผันผวนอย่างไร (Call, Strike 100, IV 30%)"))
    specs = [
        ("Δ Delta", C["blue"], t("Change in option price per $1 move.\nAlso ≈ chance of finishing ITM.", "ราคาออปชันเปลี่ยนเท่าไหร่ต่อ $1\nและ ≈ โอกาสจบแบบ ITM"),
         lambda S: bs(S, 100, 30 / 365, 0.3)["delta"], (80, 120), (0, 1), t("stock price", "ราคาหุ้น")),
        ("Γ Gamma", C["purple"], t("Change in delta per $1 move.\nHighest at the money, near expiry.", "Delta เปลี่ยนเท่าไหร่ต่อ $1\nสูงสุดที่ ATM ใกล้หมดอายุ"),
         lambda S: bs(S, 100, 30 / 365, 0.3)["gamma"], (80, 120), (0, 0.15), t("stock price", "ราคาหุ้น")),
        ("Θ Theta", C["bear"], t("Value lost per day from time decay.\nAccelerates in the last weeks.", "มูลค่าที่หายไปต่อวันจากเวลา\nเร่งขึ้นในสัปดาห์สุดท้าย"),
         lambda d: bs(100, 100, max(d, 0.5) / 365, 0.3)["price"], (60, 0), (0, 7.5), t("days to expiry →", "วันถึงหมดอายุ →")),
        ("ν Vega", C["teal"], t("Change in price per 1-point\nchange in implied volatility.", "ราคาเปลี่ยนเท่าไหร่ต่อ IV\nที่เปลี่ยน 1 จุด"),
         lambda v: bs(100, 100, 30 / 365, v / 100)["price"], (10, 60), (0, 7.5), t("implied volatility %", "ความผันผวนแฝง %")),
    ]
    for k, (name, col, body, f, (a, b), (lo, hi), xl) in enumerate(specs):
        x = 28 + (k % 2) * 460
        y = 92 + (k // 2) * 232
        panel(s, x, y, 444, 220)
        s.text(x + 18, y + 32, name, 20, col, weight=700)
        s.text(x + 18, y + 62, body, 13, C["text"])
        P = Plot(s, x + 240, y + 30, 185, 150, 1, lo, hi)
        X = lambda v: x + 240 + 185 * (v - a) / (b - a)
        pts = [(X(a + (b - a) * i / 80), P.Y(f(a + (b - a) * i / 80))) for i in range(81)]
        s.line(x + 240, y + 180, x + 425, y + 180, C["dim"], 1)
        s.polyline(pts, col, 2.6)
        s.text(x + 332, y + 200, xl, 11, C["muted"], "middle")
    c = bs(100, 100, 30 / 365, 0.3)
    s.text(28, 570, t(f"ATM call, 30 days: price {c['price']:.2f} · delta {c['delta']:.2f} · gamma {c['gamma']:.3f} · theta {c['theta']:.3f}/day · vega {c['vega']:.3f}/pt",
                      f"Call ATM อายุ 30 วัน: ราคา {c['price']:.2f} · Delta {c['delta']:.2f} · Gamma {c['gamma']:.3f} · Theta {c['theta']:.3f}/วัน · Vega {c['vega']:.3f}/จุด"),
           13, C["amber"], weight=600)
    return s.render()


@fig
def delta_curve(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Gamma grows as expiry approaches", "Gamma เพิ่มขึ้นเมื่อใกล้หมดอายุ"),
            t("Call delta vs price for different days to expiry (strike 100, IV 30%). Steeper curve = more gamma.",
              "Delta ของ Call เทียบกับราคา ในวันถึงหมดอายุต่าง ๆ (Strike 100, IV 30%) เส้นชันกว่า = Gamma มากกว่า"))
    panel(s, 28, 90, 904, 360)
    P = Plot(s, 90, 120, 620, 280, 1, 0, 1)
    X = lambda S: 90 + 620 * (S - 80) / 40
    for v in (0, 0.5, 1):
        s.line(90, P.Y(v), 710, P.Y(v), C["grid"], 1)
        s.text(80, P.Y(v) + 4, f"{v:.1f}", 12, C["muted"], "end")
    s.line(X(100), 120, X(100), 400, C["dim"], 1, "3 3")
    labels = []
    for days, col in ((90, C["blue"]), (30, C["teal"]), (7, C["amber"]), (1, C["bear"])):
        pts = [(X(S), P.Y(bs(S, 100, days / 365, 0.3)["delta"])) for S in [80 + 40 * i / 120 for i in range(121)]]
        s.polyline(pts, col, 2.6)
        labels.append([P.Y(bs(120, 100, days / 365, 0.3)["delta"]) + 4, t(f"{days} day" + ("s" if days > 1 else ""), f"{days} วัน"), col])
    labels.sort(key=lambda r: r[0])
    for k in range(1, len(labels)):  # keep end labels at least 17 px apart (C9 figure check)
        labels[k][0] = max(labels[k][0], labels[k - 1][0] + 17)
    for y, txt, col in labels:
        s.text(730, y, txt, 13, col, weight=700)
    for S in (80, 90, 100, 110, 120):
        s.text(X(S), 420, str(S), 12, C["muted"], "middle")
    s.text(730, 300, t("Near expiry, delta\njumps from 0 to 1\naround the strike:\ngamma explodes.", "ใกล้หมดอายุ Delta\nกระโดดจาก 0 ไป 1\nรอบ Strike:\nGamma พุ่ง"), 13, C["text"])
    return s.render()


# ---------------------------------------------------------------- 8.3
@fig
def hedging(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Why dealers trade the underlying", "ทำไมดีลเลอร์ต้องซื้อขายสินทรัพย์อ้างอิง"),
            t("A market maker sells you a call, then hedges to stay delta-neutral. Their hedging moves the market.",
              "มาร์เก็ตเมกเกอร์ขาย Call ให้คุณ แล้วป้องกันความเสี่ยงให้ Delta เป็นกลาง การป้องกันนั้นขยับตลาด"))
    c1 = bs(5000, 5100, 20 / 365, 0.16)
    c2 = bs(5050, 5100, 20 / 365, 0.16)
    steps = [
        (C["blue"], t("1 · You buy 100 calls", "1 · คุณซื้อ 100 Call"), t("Strike 5,100, index 5,000.\nThe dealer is now SHORT\nthe calls.", "Strike 5,100 ดัชนี 5,000\nดีลเลอร์ตอนนี้ Short\nCall อยู่")),
        (C["amber"], t("2 · Dealer hedges", "2 · ดีลเลอร์ป้องกัน"), t(f"Call delta ≈ {c1['delta']:.2f}.\nShort calls = short {c1['delta'] * 100:.0f} deltas\n→ dealer BUYS ≈ {c1['delta'] * 100:.0f} units.",
                                                                   f"Delta ของ Call ≈ {c1['delta']:.2f}\nShort Call = Short {c1['delta'] * 100:.0f} Delta\n→ ดีลเลอร์ ซื้อ ≈ {c1['delta'] * 100:.0f} หน่วย")),
        (C["bull"], t("3 · Price rises to 5,050", "3 · ราคาขึ้นไป 5,050"), t(f"Delta grows to ≈ {c2['delta']:.2f} (gamma).\nDealer must BUY ≈ {(c2['delta'] - c1['delta']) * 100:.0f}\nmore units, into the rally.",
                                                                           f"Delta เพิ่มเป็น ≈ {c2['delta']:.2f} (Gamma)\nดีลเลอร์ต้อง ซื้อ เพิ่ม ≈ {(c2['delta'] - c1['delta']) * 100:.0f}\nหน่วย ตามการขึ้น")),
        (C["bear"], t("4 · Price falls back", "4 · ราคาร่วงกลับ"), t("Delta shrinks.\nDealer SELLS the extra\nhedge, into the decline.", "Delta หดลง\nดีลเลอร์ ขาย Hedge\nส่วนเกิน ตามการลง")),
    ]
    for k, (col, head, body) in enumerate(steps):
        x = 28 + k * 231
        s.card(x, 96, 219, 190, head, body, col, 15, 13)
        if k < 3:
            s.arrow(x + 221, 190, x + 229, 190, C["muted"], 2)
    s.rect(28, 304, 904, 146, fill=C["panel"], stroke=C["border"], rx=12)
    s.text(48, 336, t("Key idea", "แนวคิดสำคัญ"), 17, C["amber"], weight=700)
    s.text(48, 366, t("Dealers SHORT gamma (sold options) must buy rallies and sell dips → they AMPLIFY moves.\n"
                      "Dealers LONG gamma (bought options) sell rallies and buy dips → they DAMPEN moves.\n"
                      "So the sign of dealers' gamma tells you whether the market tends to trend or to stay pinned (8.4).",
                      "ดีลเลอร์ที่ SHORT Gamma (ขายออปชัน) ต้องซื้อตอนขึ้นและขายตอนลง → พวกเขา ขยาย การเคลื่อนไหว\n"
                      "ดีลเลอร์ที่ LONG Gamma (ซื้อออปชัน) ขายตอนขึ้นและซื้อตอนลง → พวกเขา ลดทอน การเคลื่อนไหว\n"
                      "เครื่องหมายของ Gamma ดีลเลอร์จึงบอกว่าตลาดมักวิ่งเป็นเทรนด์หรือถูกตรึง (8.4)"), 14, C["text"])
    return s.render()


@fig
def gamma_regimes(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Positive vs negative gamma: two kinds of market", "Gamma บวก vs ลบ: ตลาดสองแบบ"),
            t("Same news, different dealer positioning, very different price behaviour.",
              "ข่าวเดียวกัน สถานะดีลเลอร์ต่างกัน พฤติกรรมราคาต่างกันมาก"))
    rnd = random.Random(4)
    shocks = [rnd.gauss(0, 1) for _ in range(60)]
    for k, (head, col, damp, body) in enumerate((
            (t("Positive gamma (above the flip)", "Gamma บวก (เหนือ Flip)"), C["bull"], True,
             t("Dealers sell rips, buy dips → mean\nreversion, small ranges, low realised vol.\nFade extremes; expect pins.", "ดีลเลอร์ขายตอนพุ่ง ซื้อตอนย่อ → กลับสู่ค่าเฉลี่ย\nกรอบแคบ ความผันผวนจริงต่ำ\nสวนจุดสุด คาดการตรึงราคา")),
            (t("Negative gamma (below the flip)", "Gamma ลบ (ใต้ Flip)"), C["bear"], False,
             t("Dealers sell into drops, buy into rips →\nmomentum, gaps, high realised vol.\nRespect breaks; size down.", "ดีลเลอร์ขายตามการร่วง ซื้อตามการพุ่ง →\nโมเมนตัม Gap ความผันผวนจริงสูง\nเคารพการเบรก ลดขนาดไม้")))):
        x = 28 + k * 460
        panel(s, x, 90, 444, 360, head, col)
        p, v, pts = 0.0, 0.0, [0.0]
        for z in shocks:
            if damp:
                p = 0.6 * p + 0.8 * z
            else:
                v = 0.55 * v + z
                p = p + 0.9 * v
            pts.append(p)
        lo, hi = -25, 25
        P = Plot(s, x + 20, 140, 404, 180, 60, lo, hi)
        s.line(x + 20, P.Y(0), x + 424, P.Y(0), C["dim"], 1, "3 3")
        P.path([(i, max(min(q, hi), lo)) for i, q in enumerate(pts)], col, 2.2)
        s.text(x + 18, 365, body, 13, C["text"])
    return s.render()


# ---------------------------------------------------------------- 8.4
@fig
def gex_profile(lang):
    t = tr(lang)
    s = SVG(960, 560, t("GEX by strike and the gamma flip", "GEX แยกตาม Strike และ Gamma Flip"),
            t("Synthetic index chain, spot 5,000. Bars: dealer gamma per strike ($bn per 1% move). Line: total GEX if spot moved there.",
              "เชนดัชนีจำลอง ราคา 5,000 แท่ง: Gamma ของดีลเลอร์ต่อ Strike ($bn ต่อการขยับ 1%) เส้น: GEX รวมถ้าราคาย้ายไปที่นั่น"))
    panel(s, 28, 90, 904, 450)
    g = gex_by_strike(SPOT)
    flip = gamma_flip()
    curve = [(S, total_gex(S)) for S in range(4700, 5301, 10)]
    mx = max(max(abs(v) for v in g.values()), max(abs(v) for _, v in curve)) * 1.1
    x0, w, y0, h = 90, 760, 120, 360
    X = lambda S: x0 + w * (S - 4675) / 650
    Y = lambda v: y0 + h / 2 - (h / 2) * v / mx
    s.line(x0, Y(0), x0 + w, Y(0), C["dim"], 1)
    s.rect(x0, y0, X(flip) - x0, h, fill=C["bear"], opacity=0.06)
    s.rect(X(flip), y0, x0 + w - X(flip), h, fill=C["bull"], opacity=0.06)
    for K, v in g.items():
        col = C["bull"] if v > 0 else C["bear"]
        s.rect(X(K) - 14, min(Y(v), Y(0)), 28, abs(Y(v) - Y(0)), fill=col, opacity=0.8, rx=3)
        s.text(X(K), y0 + h + 22, f"{K}", 11, C["muted"], "middle")
    s.polyline([(X(S), Y(v)) for S, v in curve], C["amber"], 2.5)
    s.line(X(flip), y0, X(flip), y0 + h, C["amber"], 1.8, "6 4")
    s.text(X(flip) + 6, y0 + 18, t(f"gamma flip ≈ {flip:,.0f}", f"Gamma Flip ≈ {flip:,.0f}"), 13, C["amber"], weight=700)
    s.line(X(SPOT), y0, X(SPOT), y0 + h, C["white"], 1.2, "2 3")
    s.text(X(SPOT) + 6, y0 + 40, t(f"spot 5,000 · total {total_gex(SPOT):+.1f}bn", f"ราคา 5,000 · รวม {total_gex(SPOT):+.1f}bn"), 12, C["white"], weight=700)
    s.text(x0 + 10, y0 + h - 12, t("NEGATIVE gamma: moves amplified", "Gamma ลบ: การเคลื่อนไหวถูกขยาย"), 13, C["bear"], weight=700)
    s.text(x0 + w - 10, y0 + h - 12, t("POSITIVE gamma: moves dampened", "Gamma บวก: การเคลื่อนไหวถูกลดทอน"), 13, C["bull"], "end", 700)
    return s.render()


# ---------------------------------------------------------------- 8.5
@fig
def walls(lang):
    t = tr(lang)
    s = SVG(960, 545, t("Call wall and put wall", "Call Wall และ Put Wall"),
            t("Open interest by strike (same synthetic chain). The biggest call and put strikes often act as a ceiling and a floor.",
              "Open Interest แยกตาม Strike (เชนจำลองเดียวกัน) Strike ของ Call และ Put ที่ใหญ่ที่สุดมักเป็นเพดานและพื้น"))
    panel(s, 28, 90, 904, 435)
    y0, rh = 112, 28
    mid = 480
    mx = max(max(CALL_OI.values()), max(PUT_OI.values()))
    cw = max(CALL_OI, key=CALL_OI.get)
    pw = max(PUT_OI, key=PUT_OI.get)
    s.text(mid - 20, y0 + 4, t("← put OI", "← OI ของ Put"), 13, C["bear"], "end", 700)
    s.text(mid + 20, y0 + 4, t("call OI →", "OI ของ Call →"), 13, C["bull"], weight=700)
    for r, K in enumerate(sorted(STRIKES, reverse=True)):
        y = y0 + 14 + r * rh
        po, co = PUT_OI.get(K, 0), CALL_OI.get(K, 0)
        s.rect(mid - 30 - 300 * po / mx, y, 300 * po / mx, rh - 6, fill=C["bear"], opacity=0.9 if K == pw else 0.5, rx=3)
        s.rect(mid + 30, y, 300 * co / mx, rh - 6, fill=C["bull"], opacity=0.9 if K == cw else 0.5, rx=3)
        s.text(mid, y + 16, f"{K}", 12, C["white"] if K == 5000 else C["muted"], "middle", 700 if K in (cw, pw, 5000) else 400)
        if K == cw:
            s.text(mid + 40 + 300 * co / mx, y + 16, t("CALL WALL", "CALL WALL"), 13, C["bull"], weight=700)
        if K == pw:
            s.text(mid - 40 - 300 * po / mx, y + 16, t("PUT WALL", "PUT WALL"), 13, C["bear"], "end", 700)
        if K == 5000:
            s.rect(mid - 26, y - 1, 52, rh - 4, stroke=C["white"], sw=1.2, rx=4)
    s.text(48, 512, t("Spot 5,000 sits between the put wall (4,900) and the call wall (5,100): a likely range while positioning stays the same.",
                      "ราคา 5,000 อยู่ระหว่าง Put Wall (4,900) และ Call Wall (5,100): น่าจะเป็นกรอบตราบใดที่สถานะยังเหมือนเดิม"),
           13, C["amber"], weight=600)
    return s.render()


@fig
def opex_pin(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Pinning into expiry, release after", "การตรึงราคาก่อนหมดอายุ และการปลดปล่อยหลังจากนั้น"),
            t("Large gamma at a strike can hold price near it into options expiration (OPEX). After expiry, that gamma is gone.",
              "Gamma ก้อนใหญ่ที่ Strike หนึ่งตรึงราคาให้อยู่ใกล้ ๆ จนถึงวันหมดอายุออปชัน (OPEX) หลังหมดอายุ Gamma นั้นหายไป"))
    panel(s, 28, 90, 904, 360)
    rnd = random.Random(9)
    path, p = [], 5040.0
    for i in range(40):
        if i < 28:
            p += (5050 - p) * (0.08 + i * 0.012) + rnd.gauss(0, 9 * (1 - i / 34))
        else:
            p += rnd.gauss(-6, 22)
        path.append(p)
    P = Plot(s, 70, 130, 820, 270, 39, 4930, 5110)
    s.line(70, P.Y(5050), 890, P.Y(5050), C["amber"], 1.6, "6 4")
    s.text(76, P.Y(5050) - 8, t("big gamma strike 5,050", "Strike ที่มี Gamma ใหญ่ 5,050"), 12, C["amber"], weight=700)
    s.line(P.X(28), 130, P.X(28), 400, C["purple"], 1.5, "4 4")
    s.text(P.X(28) + 6, 148, "OPEX", 13, C["purple"], weight=700)
    s.rect(P.X(20), 130, P.X(28) - P.X(20), 270, fill=C["amber"], opacity=0.07)
    P.path(list(enumerate(path)), C["text"], 2.4)
    s.text(P.X(24), 420, t("pin: range shrinks", "ตรึง: กรอบแคบลง"), 13, C["amber"], "middle", 700)
    s.text(P.X(34), 420, t("release: volatility returns", "ปลดปล่อย: ความผันผวนกลับมา"), 13, C["purple"], "middle", 700)
    return s.render()


# ---------------------------------------------------------------- 8.6
@fig
def vanna_charm(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Vanna and charm: hedges that change without price moving", "Vanna และ Charm: Hedge ที่เปลี่ยนโดยราคาไม่ต้องขยับ"),
            t("Example: customers hold many index puts; dealers are short those puts and hedged by being short futures.",
              "ตัวอย่าง: ลูกค้าถือ Put ดัชนีจำนวนมาก ดีลเลอร์ Short Put เหล่านั้นและป้องกันด้วยการ Short ฟิวเจอร์ส"))
    put_d = lambda iv, days: bs(5000, 4800, days / 365, iv, "p")["delta"]
    for k, (name, col, xl, xs, f, body) in enumerate((
            ("Vanna", C["teal"], t("implied volatility (%)", "ความผันผวนแฝง (%)"), (30, 12),
             lambda v: put_d(v / 100, 20),
             t("Delta changes when IV changes.\nIV falls (e.g. after an event) →\nOTM put delta shrinks → dealers\nBUY BACK futures hedges →\nsupportive 'vanna rally'.",
               "Delta เปลี่ยนเมื่อ IV เปลี่ยน\nIV ลด (เช่น หลังเหตุการณ์) →\nDelta ของ Put OTM หดลง → ดีลเลอร์\nซื้อคืน Hedge ฟิวเจอร์ส →\n'Vanna Rally' ที่หนุนราคา")),
            ("Charm", C["purple"], t("days to expiry", "วันถึงหมดอายุ"), (30, 1),
             lambda d: put_d(0.18, d),
             t("Delta changes as time passes.\nOTM put delta decays toward 0\ninto expiry → dealers buy back\nhedges day by day → steady\nbid into OPEX.",
               "Delta เปลี่ยนเมื่อเวลาผ่านไป\nDelta ของ Put OTM ลดลงเข้าหา 0\nเมื่อใกล้หมดอายุ → ดีลเลอร์ซื้อคืน\nHedge ทีละวัน → แรงซื้อสม่ำเสมอ\nก่อน OPEX")))):
        x = 28 + k * 460
        panel(s, x, 90, 444, 390, name, col, 20)
        a, b = xs
        vals = [f(a + (b - a) * i / 60) for i in range(61)]
        P = Plot(s, x + 40, 168, 370, 122, 60, min(vals) * 1.1, 0)
        s.line(x + 40, 290, x + 410, 290, C["dim"], 1)
        P.path(list(enumerate(vals)), col, 2.6)
        s.text(x + 40, 310, f"{a}", 11, C["muted"])
        s.text(x + 410, 310, f"{b}", 11, C["muted"], "end")
        s.text(x + 225, 310, xl + " →", 11, C["muted"], "middle")
        v0, v1 = vals[0] + 0.0, abs(vals[-1]) if abs(vals[-1]) < 0.005 else vals[-1]
        s.text(x + 18, 152, t(f"4,800 put delta: {v0:.2f} → {v1:.2f}", f"Delta ของ Put 4,800: {v0:.2f} → {v1:.2f}"), 12, col, weight=700)
        s.text(x + 18, 340, body, 13, C["text"])
    return s.render()


# ---------------------------------------------------------------- 8.7
@fig
def flow_tape(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Reading the options tape", "อ่านเทปออปชัน"),
            t("Who was aggressive, how much money, and is it new? Example prints (illustrative).",
              "ใครรุก เงินเท่าไหร่ และเป็นสถานะใหม่หรือไม่? ตัวอย่างรายการ (สมมติ)"))
    heads = [t("Time", "เวลา"), t("Ticker", "หุ้น"), t("Strike / exp", "Strike / หมดอายุ"), t("Type", "ประเภท"), t("Side", "ฝั่ง"),
             t("Size", "ขนาด"), t("Premium", "พรีเมียม"), "Vol / OI", t("Read", "การอ่าน")]
    xs = [44, 98, 152, 272, 340, 396, 462, 548, 690]
    rows = [
        ("10:02", "XYZ", "150C · 3w", t("SWEEP", "SWEEP"), t("ask", "Ask"), "4,000", "$1.6M", "4,000 / 900", t("aggressive, likely new", "รุก น่าจะเป็นสถานะใหม่"), C["bull"]),
        ("10:15", "XYZ", "140P · 3w", t("block", "Block"), t("bid", "Bid"), "2,500", "$0.9M", "2,500 / 12,000", t("likely closing / selling", "น่าจะปิด / ขาย"), C["muted"]),
        ("11:40", "IDX", "4800P · 2d", t("block", "Block"), t("mid", "Mid"), "10,000", "$3.2M", "10,000 / 40,000", t("hedge? unclear", "Hedge? ไม่ชัด"), C["amber"]),
        ("13:05", "ABC", "80C · 1d", t("sweep", "Sweep"), t("ask", "Ask"), "1,200", "$36K", "1,200 / 300", t("lottery ticket", "ตั๋วลอตเตอรี่"), C["dim"]),
    ]
    panel(s, 28, 90, 904, 250)
    for hx, h in zip(xs, heads):
        s.text(hx, 122, h, 12, C["muted"], weight=700)
    for r, row in enumerate(rows):
        y = 162 + r * 44
        col = row[-1]
        s.rect(36, y - 24, 888, 38, fill=col, opacity=0.08, rx=6)
        for j, (hx, cell) in enumerate(zip(xs, row[:-1])):
            s.text(hx, y, cell, 12, col if j in (3, 8) else C["text"], weight=700 if j in (3, 6) else 400)
    checks = [
        (C["bull"], t("Side", "ฝั่ง"), t("At/above ask = buyer aggressive.\nAt bid = seller aggressive.", "ที่/เหนือ Ask = ผู้ซื้อรุก\nที่ Bid = ผู้ขายรุก")),
        (C["blue"], t("Vol vs OI", "Vol เทียบ OI"), t("Volume > open interest\n→ likely NEW positions.", "วอลุ่ม > Open Interest\n→ น่าจะเป็นสถานะ ใหม่")),
        (C["amber"], t("Size & premium", "ขนาด & พรีเมียม"), t("$1M+ matters. Tiny\npremium = noise.", "$1M+ มีความหมาย พรีเมียม\nเล็ก = สัญญาณรบกวน")),
        (C["purple"], t("Context", "บริบท"), t("Could be a hedge or one leg\nof a spread. Never certain.", "อาจเป็น Hedge หรือขาหนึ่ง\nของ Spread ไม่มีอะไรแน่นอน")),
    ]
    for k, (col, head, body) in enumerate(checks):
        s.card(28 + k * 231, 356, 219, 124, head, body, col, 15, 12)
    return s.render()


# ---------------------------------------------------------------- 8.8
@fig
def summary(lang):
    t = tr(lang)
    s = SVG(960, 560, t("Phase 8 on one page", "สรุปเฟส 8 ในหน้าเดียว"))
    cx, cy = 480, 310
    nodes = [
        (170, 140, C["blue"], t("8.1–8.2 Options & Greeks", "8.1–8.2 ออปชัน & Greeks"), t("Premium = intrinsic + time.\nΔ Γ Θ ν.", "พรีเมียม = มูลค่าแท้ + เวลา\nΔ Γ Θ ν")),
        (790, 140, C["amber"], t("8.3 Dealer hedging", "8.3 การ Hedge ของดีลเลอร์"), t("Short gamma amplifies.\nLong gamma dampens.", "Short Gamma ขยาย\nLong Gamma ลดทอน")),
        (150, 320, C["bull"], t("8.4 GEX & flip", "8.4 GEX & Flip"), t("Above flip: pinned.\nBelow flip: volatile.", "เหนือ Flip: ถูกตรึง\nใต้ Flip: ผันผวน")),
        (810, 320, C["bear"], t("8.5 Walls", "8.5 Walls"), t("Call wall ceiling,\nput wall floor, OPEX pin.", "Call Wall เพดาน\nPut Wall พื้น ตรึงช่วง OPEX")),
        (250, 480, C["teal"], t("8.6 Vanna & charm", "8.6 Vanna & Charm"), t("IV drop & time decay\n→ dealers buy back hedges.", "IV ลด & เวลาผ่านไป\n→ ดีลเลอร์ซื้อคืน Hedge")),
        (710, 480, C["purple"], t("8.7 Options flow", "8.7 Options Flow"), t("Side · size · vol vs OI.\nContext, not signals.", "ฝั่ง · ขนาด · Vol เทียบ OI\nบริบท ไม่ใช่สัญญาณ")),
    ]
    for x, y, col, head, body in nodes:
        s.line(cx, cy, x, y, col, 2, opacity=0.5)
    s.circle(cx, cy, 74, C["panel"], C["text"], 2)
    s.text(cx, cy - 4, t("PHASE 8", "เฟส 8"), 20, C["text"], "middle", 700)
    s.text(cx, cy + 20, t("Options & GEX", "ออปชัน & GEX"), 14, C["muted"], "middle")
    for x, y, col, head, body in nodes:
        s.rect(x - 130, y - 42, 260, 92, fill=C["panel"], stroke=col, rx=12)
        s.text(x, y - 14, head, 16, col, "middle", 700)
        s.text(x, y + 10, body, 13, C["text"], "middle")
    return s.render()


# ---------------------------------------------------------------- v2 beginner figures
@fig
def insurance(lang):
    t = tr(lang)
    s = SVG(960, 560, t("Options are things you already know", "ออปชันคือสิ่งที่คุณรู้จักอยู่แล้ว"),
            t("A put works like insurance. A call works like a deposit that locks today's price.",
              "Put ทำงานเหมือนประกันภัย ส่วน Call ทำงานเหมือนเงินมัดจำที่ล็อกราคาวันนี้ไว้"))
    halves = [
        (C["bear"], t("PUT  =  insurance on your car", "PUT  =  ประกันรถยนต์"), [
            (t("You pay the insurer", "คุณจ่ายเงินให้บริษัทประกัน"), t("Premium", "ค่าพรีเมียม (Premium)")),
            (t("Car insured at 100", "รถถูกประกันไว้ที่ 100"), t("Strike = 100", "Strike = 100")),
            (t("Policy ends in 1 year", "กรมธรรม์หมดอายุใน 1 ปี"), t("Expiry", "วันหมดอายุ (Expiry)")),
            (t("Crash → insurer pays you", "รถชน → บริษัทจ่ายให้คุณ"), t("Price falls → put pays", "ราคาร่วง → Put ได้เงิน")),
            (t("No crash → premium is gone", "ไม่ชน → เสียค่าพรีเมียมไป"), t("Price stays up → lose premium", "ราคาไม่ลง → เสียพรีเมียม")),
        ]),
        (C["bull"], t("CALL  =  deposit to lock a condo price", "CALL  =  มัดจำล็อกราคาคอนโด"), [
            (t("You pay a deposit", "คุณจ่ายเงินมัดจำ"), t("Premium", "ค่าพรีเมียม (Premium)")),
            (t("Locked price 100", "ล็อกราคาไว้ที่ 100"), t("Strike = 100", "Strike = 100")),
            (t("Offer valid 3 months", "ข้อเสนอมีผล 3 เดือน"), t("Expiry", "วันหมดอายุ (Expiry)")),
            (t("Prices jump to 130 → buy at 100", "ราคาพุ่งเป็น 130 → ซื้อที่ 100"), t("Price rises → call pays", "ราคาขึ้น → Call ได้เงิน")),
            (t("Prices fall → walk away", "ราคาลง → ไม่ซื้อก็ได้"), t("Lose only the deposit", "เสียแค่เงินมัดจำ")),
        ]),
    ]
    for k, (col, head, rows) in enumerate(halves):
        x = 28 + k * 460
        s.rect(x, 96, 444, 440, fill=C["panel"], stroke=C["border"], rx=12)
        s.text(x + 20, 128, head, 17, col, weight=700)
        s.text(x + 20, 158, t("Everyday life", "ชีวิตประจำวัน"), 12, C["muted"], weight=700)
        s.text(x + 250, 158, t("Option word", "ศัพท์ออปชัน"), 12, C["muted"], weight=700)
        for i, (a, b) in enumerate(rows):
            y = 174 + i * 70
            s.rect(x + 16, y, 200, 54, fill=C["bg"], stroke=C["border"], rx=8)
            s.text(x + 28, y + 32, a, 13, C["text"])
            s.arrow(x + 220, y + 27, x + 240, y + 27, col, 2)
            s.rect(x + 244, y, 184, 54, fill=col, opacity=0.14, stroke=col, rx=8)
            s.text(x + 256, y + 32, b, 13, C["text"], weight=600)
    return s.render()


@fig
def open_interest(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Open interest = contracts still open", "Open Interest = จำนวนสัญญาที่ยังเปิดอยู่"),
            t("Volume counts every trade. Open interest only rises when a NEW contract is created.",
              "Volume นับทุกการซื้อขาย แต่ Open Interest จะเพิ่มก็ต่อเมื่อมีการสร้างสัญญา ใหม่"))
    rows = [
        (t("Day 1", "วันที่ 1"), t("Ann BUYS 1 call from Ben\n(both are new)", "แอนซื้อ Call 1 สัญญาจากเบน\n(ทั้งคู่เปิดใหม่)"), 1, 1, C["bull"], t("+1 opened", "+1 เปิดใหม่")),
        (t("Day 2", "วันที่ 2"), t("Cat BUYS 1 call from Dan\n(both are new)", "แคทซื้อ Call 1 สัญญาจากแดน\n(ทั้งคู่เปิดใหม่)"), 1, 2, C["bull"], t("+1 opened", "+1 เปิดใหม่")),
        (t("Day 3", "วันที่ 3"), t("Ann SELLS her call to Eve\n(Ann closes, Eve opens)", "แอนขาย Call ให้อีฟ\n(แอนปิด อีฟเปิดแทน)"), 1, 2, C["amber"], t("ownership moved", "แค่เปลี่ยนมือ")),
        (t("Day 4", "วันที่ 4"), t("Cat SELLS to Dan\n(both close)", "แคทขายคืนให้แดน\n(ทั้งคู่ปิด)"), 1, 1, C["bear"], t("−1 closed", "−1 ปิดสัญญา")),
    ]
    s.text(360, 120, t("Volume", "Volume"), 13, C["muted"], "middle", 700)
    s.text(470, 120, t("Open interest", "Open Interest"), 13, C["muted"], "middle", 700)
    for i, (day, what, vol, oi, col, note) in enumerate(rows):
        y = 136 + i * 76
        s.rect(28, y, 904, 64, fill=C["panel"], stroke=C["border"], rx=10)
        s.text(48, y + 38, day, 15, C["text"], weight=700)
        s.text(120, y + 27, what, 13, C["text"])
        s.text(360, y + 40, str(vol), 22, C["blue"], "middle", 700)
        s.text(470, y + 40, str(oi), 22, col, "middle", 700)
        for k in range(oi):
            s.rect(530 + k * 34, y + 18, 26, 28, fill=col, rx=5, opacity=0.85)
        s.text(910, y + 40, note, 13, col, "end", 700)
    s.text(48, 450, t("Big open interest at one strike = many live contracts there = many dealer hedges tied to that price (8.5).",
                      "Open Interest สูงที่ Strike ใด = มีสัญญาค้างอยู่มาก = ดีลเลอร์มี Hedge ผูกกับราคานั้นมาก (8.5)"), 13, C["amber"], weight=600)
    return s.render()


# ================================================================ v2 additions (Oct 2026)
@fig
def hedge_melt(lang):
    t = tr(lang)
    s = SVG(960, 480, t("The hedge 'melts': a put's delta from −0.30 to −0.20", "เฮดจ์ที่ 'ละลาย': Delta ของ Put จาก −0.30 เป็น −0.20"),
            t("Index 5,000, put strike 4,885. Dealers are short 10,000 puts and short futures to hedge.",
              "ดัชนี 5,000 Put Strike 4,885 ดีลเลอร์ Short Put 10,000 สัญญา และ Short ฟิวเจอร์สเพื่อเฮดจ์"))
    rows = [(t("Start: 20 days, IV 20%", "เริ่ม: 20 วัน IV 20%"), 20, 0.20, C["muted"]),
            (t("Charm only: 8 days left, IV 20%", "Charm อย่างเดียว: เหลือ 8 วัน IV 20%"), 8, 0.20, C["amber"]),
            (t("Vanna only: 20 days, IV falls to 12%", "Vanna อย่างเดียว: 20 วัน IV ลดเป็น 12%"), 20, 0.12, C["teal"]),
            (t("Both: 15 days left, IV 14%", "ทั้งสองอย่าง: เหลือ 15 วัน IV 14%"), 15, 0.14, C["bull"])]
    base = None
    for k, (lab, days, iv, col) in enumerate(rows):
        d = bs(5000, 4885, days / 365, iv, "p")["delta"]
        hedge = round(-d * 10000)
        if base is None:
            base = hedge
        y = 110 + k * 78
        s.text(48, y + 26, lab, 14, col, weight=700)
        s.text(48, y + 48, t(f"put delta {d:+.2f}", f"Delta ของ Put {d:+.2f}"), 13, C["muted"])
        s.rect(400, y + 10, hedge * 0.12, 34, fill=C["bear"], opacity=0.75, rx=5)
        s.text(400 + hedge * 0.12 + 10, y + 33, t(f"short {hedge:,} futures", f"Short ฟิวเจอร์ส {hedge:,}"), 14, C["text"], weight=700)
        if k:
            s.text(880, y + 33, t(f"buy back {base - hedge:,}", f"ซื้อคืน {base - hedge:,}"), 14, C["bull"], "end", 700)
    s.rect(28, 420, 904, 44, fill=C["panel"], stroke=C["border"], rx=10)
    s.text(48, 448, t("No one decided to buy: the hedge shrank because time passed (charm) or fear faded (vanna).",
                      "ไม่มีใครตัดสินใจซื้อ: เฮดจ์หดเพราะเวลาผ่านไป (Charm) หรือความกลัวจางลง (Vanna)"), 14, C["amber"], weight=600)
    return s.render()


@fig
def open_close(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Is this options flow opening or closing?", "Options flow นี้เป็นการเปิดหรือปิดโพซิชัน?"),
            t("Compare today's volume at the strike with the open interest that existed before today.",
              "เทียบวอลุ่มวันนี้ที่ Strike นั้นกับ Open interest ที่มีอยู่ก่อนวันนี้"))
    cases = [(C["bull"], t("A · Volume 4,000 > OI 900", "A · วอลุ่ม 4,000 > OI 900"), 900, 4000,
              t("At least 3,100 contracts MUST be new\npositions → likely opening", "อย่างน้อย 3,100 สัญญา ต้อง เป็น\nโพซิชันใหม่ → น่าจะเป็นการเปิด")),
             (C["amber"], t("B · Volume 2,500 < OI 12,000", "B · วอลุ่ม 2,500 < OI 12,000"), 12000, 2500,
              t("Could all be closing existing positions.\nCheck tomorrow's OI to know.", "อาจเป็นการปิดโพซิชันเดิมทั้งหมด\nดู OI พรุ่งนี้จึงจะรู้"))]
    for k, (col, head, oi, vol, note) in enumerate(cases):
        bx = 28 + k * 462
        s.rect(bx, 96, 442, 320, fill=C["panel"], stroke=col, rx=12)
        s.text(bx + 20, 128, head, 16, col, weight=700)
        sc = 160 / 12000
        s.rect(bx + 60, 370 - oi * sc, 100, oi * sc, fill=C["dim"], opacity=0.8, rx=4)
        s.text(bx + 110, 390, t("open interest\n(yesterday)", "Open interest\n(เมื่อวาน)"), 12, C["muted"], "middle")
        s.rect(bx + 220, 370 - vol * sc, 100, vol * sc, fill=col, opacity=0.8, rx=4)
        s.text(bx + 270, 390, t("today's volume", "วอลุ่มวันนี้"), 12, C["muted"], "middle")
        s.text(bx + 110, 362 - oi * sc, f"{oi:,}", 13, C["text"], "middle", 700)
        s.text(bx + 270, 362 - vol * sc, f"{vol:,}", 13, C["text"], "middle", 700)
        s.text(bx + 20, 158, note, 13, C["text"])
    return s.render()
