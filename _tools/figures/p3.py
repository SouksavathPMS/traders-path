"""Phase 3 figures: Risk & Money Management."""
import random
from charts import SVG, CandleChart, C, tr, candles_from_path

FIGURES = {}


def fig(fn):
    FIGURES["p3-" + fn.__name__.replace("_", "-")] = fn
    return fn


def panel(s, x, y, w, h, title=None, color=C["text"], size=16):
    s.rect(x, y, w, h, fill=C["panel"], stroke=C["border"], rx=12)
    if title:
        s.text(x + 18, y + 30, title, size, color, weight=700)


def trades(seed, n=100, wr=0.45, win=2.0):
    rnd = random.Random(seed)
    return [win if rnd.random() < wr else -1 for _ in range(n)]


def streak_prob(n, q, k):
    """P(at least one run of >= k losses in n trades), loss prob q."""
    dp = [1.0] + [0.0] * (k - 1)  # dp[j] = P(current run = j, no run >= k yet)
    for _ in range(n):
        new = [0.0] * k
        new[0] = sum(dp) * (1 - q)
        for j in range(k - 1):
            new[j + 1] = dp[j] * q
        dp = new
    return 1 - sum(dp)


# ---------------------------------------------------------------- 3.1
@fig
def same_trades(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Same 100 trades. Same edge. Four different fates.", "เทรด 100 ไม้ชุดเดียวกัน ความได้เปรียบเท่ากัน แต่ชะตาต่างกัน 4 แบบ"),
            t("System: 45% win rate, +2R / −1R. Only the % of the account risked per trade changes.",
              "ระบบ: ชนะ 45%, +2R / −1R สิ่งเดียวที่ต่างคือ % ของพอร์ตที่เสี่ยงต่อไม้"))
    res = trades(2)
    panel(s, 28, 90, 904, 390)
    x0, y0, w, h = 90, 115, 680, 320
    series = []
    for risk, col in ((0.01, C["blue"]), (0.02, C["bull"]), (0.10, C["amber"]), (0.25, C["bear"])):
        e, pts = 1.0, [1.0]
        for r in res:
            e *= 1 + risk * r
            pts.append(e)
        series.append((risk, col, pts))
    hi = max(max(p) for _, _, p in series) * 1.05
    X = lambda i: x0 + w * i / 100
    Y = lambda v: y0 + h * (hi - v) / hi
    for v in (0, 1, 2):
        if v <= hi:
            s.line(x0, Y(v), x0 + w, Y(v), C["grid"] if v != 1 else C["dim"], 1, None if v != 1 else "4 4")
            s.text(x0 - 10, Y(v) + 4, f"{v * 100:.0f}%", 12, C["muted"], "end")
    # longest losing streak
    best = run = end = 0
    for i, r in enumerate(res):
        run = run + 1 if r < 0 else 0
        if run > best:
            best, end = run, i
    st = end - best + 1
    s.rect(X(st), y0, X(end + 1) - X(st), h, fill=C["bear"], opacity=0.1, rx=3)
    s.text((X(st) + X(end + 1)) / 2, y0 + 16, t(f"{best} losses in a row", f"แพ้ติดกัน {best} ไม้"), 12, C["bear"], "middle", 700)
    labels = []
    for risk, col, pts in series:
        s.polyline([(X(i), Y(v)) for i, v in enumerate(pts)], col, 2.4)
        end_v = pts[-1]
        chg = (end_v - 1) * 100
        dd, pk = 0, 1
        for v in pts:
            pk = max(pk, v)
            dd = max(dd, 1 - v / pk)
        labels.append((Y(end_v), col, f"{risk * 100:.0f}% " + t("risk", "เสี่ยง"),
                       t(f"end {chg:+.0f}% · max DD −{dd * 100:.0f}%", f"จบ {chg:+.0f}% · DD สูงสุด −{dd * 100:.0f}%")))
    labels.sort()
    ys = []
    for y, *_ in labels:
        ys.append(max(y, ys[-1] + 42) if ys else y)
    over = max(0, ys[-1] - 448)
    ys = [y - over for y in ys]
    for k in range(len(ys) - 2, -1, -1):
        ys[k] = min(ys[k], ys[k + 1] - 42)
    for (_, col, a, b), y in zip(labels, ys):
        s.text(790, y, a, 15, col, weight=700)
        s.text(790, y + 18, b, 12, C["muted"])
    s.text(x0, 462, t("Trade #1 → #100. The system finished +8R, a winning system.", "ไม้ที่ 1 → 100 ระบบจบที่ +8R ซึ่งเป็นระบบที่ชนะ"), 13, C["muted"])
    return s.render()


@fig
def streaks(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Losing streaks are not bad luck. They are math.", "การแพ้ติดกันไม่ใช่โชคร้าย มันคือคณิตศาสตร์"),
            t("Chance of at least one losing streak of this length somewhere in 100 trades",
              "โอกาสที่จะเจอการแพ้ติดกันอย่างน้อยหนึ่งครั้งตามความยาวนี้ ใน 100 ไม้"))
    panel(s, 28, 90, 904, 360)
    ks = list(range(3, 11))
    sets = [(0.5, C["blue"], t("50% win rate", "ชนะ 50%")), (0.6, C["bear"], t("40% win rate", "ชนะ 40%"))]
    x0, y0, h = 90, 130, 250
    gw = 100
    for v in (0, 0.5, 1):
        y = y0 + h * (1 - v)
        s.line(x0 - 10, y, x0 + gw * len(ks), y, C["grid"], 1)
        s.text(x0 - 16, y + 4, f"{v * 100:.0f}%", 12, C["muted"], "end")
    for gi, k in enumerate(ks):
        gx = x0 + gi * gw
        for si, (q, col, _) in enumerate(sets):
            p = streak_prob(100, q, k)
            bx = gx + 14 + si * 36
            s.rect(bx, y0 + h * (1 - p), 32, h * p, fill=col, rx=4, opacity=0.85)
            s.text(bx + 16, y0 + h * (1 - p) - 6, f"{p * 100:.0f}", 11, col, "middle", 700)
        s.text(gx + 48, y0 + h + 22, t(f"{k} in a row", f"{k} ไม้ติด"), 13, C["text"], "middle", 600)
    for si, (_, col, name) in enumerate(sets):
        s.rect(700 + si * 120, 104, 14, 14, fill=col, rx=3)
        s.text(720 + si * 120, 116, name, 13, C["text"])
    s.text(x0, 428, t("With a 40% win rate, 6+ losses in a row in 100 trades is closer to certain than to unlucky. Size for it.",
                      "เมื่อชนะ 40% การแพ้ติดกัน 6 ไม้ขึ้นไปใน 100 ไม้แทบเป็นเรื่องแน่นอน ไม่ใช่โชคร้าย ให้กำหนดขนาดไม้เผื่อไว้"),
           13, C["amber"], weight=600)
    return s.render()


# ---------------------------------------------------------------- 3.2
@fig
def size_formula(lang):
    t = tr(lang)
    s = SVG(960, 470, t("The position-size formula", "สูตรคำนวณขนาดไม้"),
            t("Decide the money you can lose first. The stop decides how much you can buy.",
              "ตัดสินเงินที่ยอมเสียได้ก่อน แล้วให้ Stop เป็นตัวบอกว่าซื้อได้เท่าไหร่"))
    boxes = [
        (C["blue"], t("Account", "เงินในพอร์ต"), "$10,000"),
        (None, "×", None),
        (C["purple"], t("Risk %", "% ความเสี่ยง"), "1%"),
        (None, "=", None),
        (C["bear"], t("$ at risk (1R)", "เงินที่เสี่ยง (1R)"), "$100"),
        (None, "÷", None),
        (C["amber"], t("Stop distance", "ระยะ Stop"), "$2.00"),
        (None, "=", None),
        (C["bull"], t("Position size", "ขนาดไม้"), t("50 shares", "50 หุ้น")),
    ]
    x = 28
    for col, a, b in boxes:
        if col is None:
            s.text(x + 14, 178, a, 30, C["muted"], "middle", 700)
            x += 28
            continue
        s.rect(x, 110, 152, 110, fill=C["panel"], stroke=col, rx=12)
        s.text(x + 76, 145, a, 13, col, "middle", 700)
        s.text(x + 76, 190, b, 22, C["text"], "middle", 700)
        x += 162
    s.text(28 + 162 * 3 + 28 * 3 + 76, 240, t("entry 50.00 − stop 48.00", "เข้า 50.00 − Stop 48.00"), 12, C["muted"], "middle")
    s.card(28, 270, 440, 180, t("Crypto / any market", "คริปโต / ตลาดไหนก็ได้"),
           t("Risk $100. BTC entry 60,000, stop 58,500.\nStop distance = $1,500 per 1 BTC\nSize = 100 ÷ 1,500 = 0.0667 BTC\n(position value ≈ $4,000)",
             "เสี่ยง $100 เข้า BTC ที่ 60,000 Stop 58,500\nระยะ Stop = $1,500 ต่อ 1 BTC\nขนาด = 100 ÷ 1,500 = 0.0667 BTC\n(มูลค่าสถานะ ≈ $4,000)"),
           C["teal"], 17, 14)
    s.card(492, 270, 440, 180, t("Position value ≠ risk", "มูลค่าสถานะ ≠ ความเสี่ยง"),
           t("50 shares × $50 = $2,500 (25% of the account)\nbut if the stop is hit you lose only $100 (1%).\nRisk is what you lose at the stop,\nnot what you spend.",
             "50 หุ้น × $50 = $2,500 (25% ของพอร์ต)\nแต่ถ้าโดน Stop คุณเสียแค่ $100 (1%)\nความเสี่ยงคือเงินที่เสียเมื่อโดน Stop\nไม่ใช่เงินที่จ่ายไป"),
           C["amber"], 17, 14)
    return s.render()


@fig
def same_risk(lang):
    t = tr(lang)
    s = SVG(960, 450, t("Same $100 risk, different stops → different sizes", "เสี่ยง $100 เท่ากัน Stop ต่างกัน → ขนาดไม้ต่างกัน"),
            t("The stop goes where the idea is wrong. The size adjusts to it, never the other way round.",
              "Stop อยู่ตรงที่ไอเดียผิด แล้วปรับขนาดไม้ตาม ไม่ใช่กลับกัน"))
    specs = [
        (t("Tight stop: $1.00", "Stop แคบ: $1.00"), 49, t("$100 ÷ $1 = 100 shares", "$100 ÷ $1 = 100 หุ้น"), C["blue"]),
        (t("Wide stop: $4.00", "Stop กว้าง: $4.00"), 46, t("$100 ÷ $4 = 25 shares", "$100 ÷ $4 = 25 หุ้น"), C["purple"]),
    ]
    cs = candles_from_path([56, 50.2, 53, 46.6, 50.5], [5, 4, 5, 4], seed=5)
    for k, (head, stop, calc, col) in enumerate(specs):
        x = 28 + k * 460
        panel(s, x, 90, 444, 340, head, col)
        ch = CandleChart(s, x + 16, 135, 300, 220, cs, pmin=44.5, pmax=57, grid=False)
        ch.hline(50, t("entry 50", "เข้า 50"), C["text"], side="left")
        ch.hline(stop, t(f"stop {stop}", f"Stop {stop}"), C["bear"], side="left")
        ch.draw()
        x1 = x + 320
        s.rect(x1, ch.Y(50), 20, ch.Y(stop) - ch.Y(50), fill=C["bear"], opacity=0.35, rx=3)
        s.text(x1 + 30, (ch.Y(50) + ch.Y(stop)) / 2 + 5, "= $100", 15, C["bear"], weight=700)
        s.text(x + 18, 390, calc, 16, col, weight=700)
        s.text(x + 18, 412, t("Hit by normal noise?" if k == 0 else "Survives the wick at 46.6? Barely.",
                              "โดนสัญญาณรบกวนปกติเก็บไหม?" if k == 0 else "รอดจากไส้ที่ 46.6? แบบเฉียดฉิว"), 13, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 3.3
@fig
def r_ruler(lang):
    t = tr(lang)
    s = SVG(960, 480, t("Measure every trade in R", "วัดทุกเทรดเป็นหน่วย R"),
            t("1R = the amount you lose if the stop is hit. Results become comparable across markets and sizes.",
              "1R = เงินที่เสียถ้าโดน Stop ผลลัพธ์จึงเทียบกันได้ทุกตลาดและทุกขนาดไม้"))
    panel(s, 28, 90, 600, 370)
    cs = candles_from_path([104, 100.4, 102.5, 100.6, 104.5, 103, 107.3], [4, 3, 3, 4, 2, 5], seed=8)
    ch = CandleChart(s, 44, 110, 560, 330, cs, pmin=97.5, pmax=108.5, grid=False)
    entry, risk = 101.5, 1.5
    i0 = 10
    for m, col in ((3, C["bull"]), (2, C["bull"]), (1, C["bull"]), (0, C["text"]), (-1, C["bear"])):
        p = entry + m * risk
        ch.hline(p, ("+" if m > 0 else "") + (f"{m}R" if m else t("entry  0R", "จุดเข้า  0R")), col, i0, side="right",
                 dash="5 4" if m else None)
    x0 = ch.X(i0) - ch.step / 2
    x1 = ch.X(len(cs) - 1) + ch.step / 2
    s.rect(x0, ch.Y(entry + 3 * risk), x1 - x0, ch.Y(entry) - ch.Y(entry + 3 * risk), fill=C["bull"], opacity=0.08)
    s.rect(x0, ch.Y(entry), x1 - x0, ch.Y(entry - risk) - ch.Y(entry), fill=C["bear"], opacity=0.15)
    ch.draw()
    s.card(650, 90, 282, 175, t("The ruler", "ไม้บรรทัด"),
           t("Entry 101.5, stop 100.0\n→ 1R = 1.5 points\n= $100 if you sized for $100\n+2R target = 104.5\n+3R target = 106.0",
             "เข้า 101.5 Stop 100.0\n→ 1R = 1.5 จุด\n= $100 ถ้าคำนวณไม้ให้เสี่ยง $100\nเป้า +2R = 104.5\nเป้า +3R = 106.0"), C["blue"], 17, 14)
    s.card(650, 280, 282, 180, t("A week in R", "หนึ่งสัปดาห์ในหน่วย R"),
           t("+2.0  −1.0  −1.0  +3.1  −0.4\n= +2.7R\nWhether 1R was $10 or $1,000,\nthe skill is the same.",
             "+2.0  −1.0  −1.0  +3.1  −0.4\n= +2.7R\nไม่ว่า 1R จะเป็น $10 หรือ $1,000\nฝีมือก็เท่าเดิม"), C["bull"], 17, 14)
    return s.render()


@fig
def breakeven(lang):
    t = tr(lang)
    s = SVG(960, 480, t("The win rate you need depends on your reward:risk", "อัตราชนะที่ต้องการ ขึ้นกับ Reward:Risk ของคุณ"),
            t("Break-even win rate = 1 ÷ (1 + R:R)   (before costs)", "อัตราชนะที่เท่าทุน = 1 ÷ (1 + R:R)   (ยังไม่รวมต้นทุน)"))
    panel(s, 28, 90, 904, 370)
    x0, y0, w, h = 110, 120, 640, 280
    X = lambda rr: x0 + w * (rr - 0.5) / 4.5
    Y = lambda p: y0 + h * (0.8 - p) / 0.8
    for p in (0, 0.2, 0.4, 0.6, 0.8):
        s.line(x0, Y(p), x0 + w, Y(p), C["grid"], 1)
        s.text(x0 - 10, Y(p) + 4, f"{p * 100:.0f}%", 12, C["muted"], "end")
    for rr in (0.5, 1, 2, 3, 4, 5):
        s.text(X(rr), y0 + h + 22, f"1:{rr:g}", 12, C["muted"], "middle")
    pts = [(X(0.5 + i * 0.05), Y(1 / (1.5 + i * 0.05))) for i in range(91)]
    s.polygon([(x0, y0)] + [(x0, pts[0][1])] + pts + [(x0 + w, y0)], C["bull"], 0.08)
    s.polygon([(x0, y0 + h)] + [(x0, pts[0][1])] + pts + [(x0 + w, y0 + h)], C["bear"], 0.08)
    s.polyline(pts, C["text"], 2.5)
    for rr in (0.5, 1, 2, 3, 4):
        p = 1 / (1 + rr)
        s.circle(X(rr), Y(p), 5, C["amber"])
        s.text(X(rr) + 10, Y(p) - 8, f"{p * 100:.0f}%", 13, C["amber"], weight=700)
    s.text(x0 + w - 10, y0 + 24, t("PROFITABLE ZONE", "โซนทำกำไร"), 14, C["bull"], "end", 700)
    s.text(x0 + 20, y0 + h - 14, t("LOSING ZONE", "โซนขาดทุน"), 14, C["bear"], weight=700)
    s.text(x0 + w / 2, y0 + h + 44, t("Reward : Risk", "Reward : Risk"), 13, C["text"], "middle", 600)
    s.text(780, 160, t("1:0.5 → need 67%\n1:1   → need 50%\n1:2   → need 33%\n1:3   → need 25%",
                       "1:0.5 → ต้องชนะ 67%\n1:1   → ต้องชนะ 50%\n1:2   → ต้องชนะ 33%\n1:3   → ต้องชนะ 25%"), 14, C["text"])
    s.text(780, 290, t("Neither number alone\ntells you anything.", "ตัวเลขเดียว\nไม่บอกอะไรเลย"), 14, C["amber"], weight=700)
    return s.render()


# ---------------------------------------------------------------- 3.4
@fig
def expectancy_grid(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Expectancy = (Win% × avg win) − (Loss% × avg loss)", "ค่าคาดหวัง = (%ชนะ × กำไรเฉลี่ย) − (%แพ้ × ขาดทุนเฉลี่ย)"),
            t("R earned per trade on average, with the average loss fixed at 1R", "R ที่ได้ต่อไม้โดยเฉลี่ย เมื่อขาดทุนเฉลี่ยคงที่ 1R"))
    panel(s, 28, 90, 904, 390)
    wrs = [0.3, 0.4, 0.5, 0.6, 0.7]
    wins = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    gx, gy, cw, chh = 200, 140, 112, 56
    s.text(gx + cw * 3, 126, t("Average win (R) →", "กำไรเฉลี่ย (R) →"), 13, C["muted"], "middle", 600)
    s.text(gx - 20, gy - 8, t("Win rate ↓", "อัตราชนะ ↓"), 13, C["muted"], "end", 600)
    for j, wv in enumerate(wins):
        s.text(gx + cw * j + cw / 2, gy + 2, f"{wv:g}R", 13, C["text"], "middle", 700)
    for i, wr in enumerate(wrs):
        y = gy + 14 + i * chh
        s.text(gx - 20, y + chh / 2 + 5, f"{wr * 100:.0f}%", 14, C["text"], "end", 700)
        for j, wv in enumerate(wins):
            e = wr * wv - (1 - wr)
            col = C["bull"] if e > 0.001 else (C["bear"] if e < -0.001 else C["dim"])
            op = min(0.12 + abs(e) * 0.45, 0.85)
            x = gx + cw * j
            s.rect(x + 3, y + 3, cw - 6, chh - 6, fill=col, opacity=op, rx=6)
            s.text(x + cw / 2, y + chh / 2 + 6, f"{e:+.2f}", 16, C["white"], "middle", 700)
    s.text(60, 452, t("Examples:  40% × 2.5R → +0.40R   ·   70% × 0.5R → −0.05R   ·   30% × 3R → +0.20R",
                      "ตัวอย่าง:  40% × 2.5R → +0.40R   ·   70% × 0.5R → −0.05R   ·   30% × 3R → +0.20R"), 13, C["amber"], weight=600)
    return s.render()


@fig
def paths(lang):
    t = tr(lang)
    s = SVG(960, 480, t("A positive edge, played 200 times by six different traders", "ความได้เปรียบที่เป็นบวก เล่น 200 ไม้ โดยเทรดเดอร์ 6 คน"),
            t("System: 45% win rate, +1.8R / −1R → expectancy +0.26R. Same rules, different luck.",
              "ระบบ: ชนะ 45%, +1.8R / −1R → ค่าคาดหวัง +0.26R กฎเดียวกัน โชคต่างกัน"))
    panel(s, 28, 90, 904, 370)
    n = 200
    runs = []
    for seed in (3, 11, 19, 27, 35, 43):
        eq, cur = [0], 0
        for r in trades(seed, n, 0.45, 1.8):
            cur += r
            eq.append(cur)
        runs.append(eq)
    lo = min(min(e) for e in runs) - 4
    hi = max(max(e) for e in runs) + 4
    x0, y0, w, h = 90, 115, 700, 310
    X = lambda i: x0 + w * i / n
    Y = lambda v: y0 + h * (hi - v) / (hi - lo)
    for v in range(-20, 121, 20):
        if lo <= v <= hi:
            s.line(x0, Y(v), x0 + w, Y(v), C["grid"] if v else C["dim"], 1, None if v else "4 4")
            s.text(x0 - 10, Y(v) + 4, f"{v:+d}R" if v else "0R", 12, C["muted"], "end")
    cols = [C["blue"], C["teal"], C["purple"], C["pink"], C["amber"], C["muted"]]
    for eq, col in zip(runs, cols):
        s.polyline([(X(i), Y(v)) for i, v in enumerate(eq)], col, 1.8, opacity=0.9)
    s.polyline([(X(0), Y(0)), (X(n), Y(0.26 * n))], C["white"], 2, "6 5")
    s.text(X(n) + 8, Y(0.26 * n) + 4, t("expected\n+52R", "คาดหวัง\n+52R"), 13, C["white"], weight=700)
    worst = min(runs, key=lambda e: e[-1])
    best = max(runs, key=lambda e: e[-1])
    s.text(X(n) + 8, Y(best[-1]) - 10, f"{best[-1]:+.0f}R", 13, C["bull"], weight=700)
    s.text(X(n) + 8, Y(worst[-1]) + 18, f"{worst[-1]:+.0f}R", 13, C["bear"], weight=700)
    s.text(x0, 448, t("Over 20 trades, anything can happen. Over 200, the edge shows. Judge a system on its sample, not its week.",
                      "ใน 20 ไม้ อะไรก็เกิดได้ ใน 200 ไม้ ความได้เปรียบจึงปรากฏ ตัดสินระบบจากกลุ่มตัวอย่าง ไม่ใช่จากสัปดาห์เดียว"),
           13, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 3.5
@fig
def stop_placement(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Where the stop goes: where the idea is wrong", "Stop อยู่ตรงไหน: ตรงที่ไอเดียผิด"),
            t("Not where the loss feels small. Beyond the structure, plus a buffer for noise.",
              "ไม่ใช่ตรงที่รู้สึกว่าเสียน้อย แต่เลยโครงสร้างออกไป บวกระยะเผื่อสัญญาณรบกวน"))
    cs = candles_from_path([110, 103.4, 105.5, 102.6, 104.2], [5, 3, 3, 2], seed=14)
    o = cs[-1][3]
    cs.append([o, o + 0.5, 101.9, o + 0.3])
    cs += candles_from_path([o + 0.3, 107, 105.6, 112], [3, 2, 5], seed=15)[0:]
    cs[len(cs) - 10][0] = cs[len(cs) - 11][3]
    wick_i = 13
    specs = [
        (t("✗ Arbitrary tight stop", "✗ Stop แคบแบบไม่มีเหตุผล"), C["bear"], 103.0,
         t("Stop at 103.0 sits inside the zone.\nA normal wick to 101.9 takes you out,\nthen price runs to target without you.",
           "Stop ที่ 103.0 อยู่ในโซน ไส้ปกติลงไป\n101.9 ก็เก็บคุณออก แล้วราคาวิ่งไป\nถึงเป้าหมายโดยไม่มีคุณ")),
        (t("✓ Structural stop", "✓ Stop ตามโครงสร้าง"), C["bull"], 101.2,
         t("Below the zone and the swing low, plus a\nbuffer (e.g. 0.5 × ATR). If price gets\nhere, buyers really failed.",
           "ใต้โซนและใต้ Swing Low บวกระยะเผื่อ\n(เช่น 0.5 × ATR) ถ้าราคามาถึงตรงนี้\nแปลว่าผู้ซื้อล้มเหลวจริง")),
    ]
    for k, (head, col, stop, body) in enumerate(specs):
        x = 28 + k * 460
        panel(s, x, 90, 444, 360, head, col)
        ch = CandleChart(s, x + 16, 130, 412, 210, cs, pmin=100, pmax=113, grid=False)
        ch.zone(102.2, 103.6, C["blue"], t("Demand", "Demand"), i0=4, opacity=0.18, label_side="left", label_pos="below")
        ch.hline(stop, t("stop", "Stop"), col, i0=9, side="right")
        ch.draw()
        if k == 0:
            s.text(ch.X(wick_i), ch.Y(101.9) + 22, "✗", 18, C["bear"], "middle", 700)
        s.text(x + 18, 375, body, 13, C["text"])
    return s.render()


@fig
def exits(lang):
    t = tr(lang)
    s = SVG(960, 480, t("Three ways to take profit", "การทำกำไร 3 แบบ"),
            t("Pick one before you enter. Write it down.", "เลือกหนึ่งแบบก่อนเข้า แล้วเขียนไว้"))
    piv = [100, 104.5, 102.8, 108, 106, 111.5, 109.4, 115, 112.2]
    cs = candles_from_path(piv, [3, 2, 4, 2, 4, 2, 4, 3], seed=17)
    panel(s, 28, 90, 600, 370)
    ch = CandleChart(s, 44, 110, 568, 330, cs, pmin=97, pmax=117, grid=False)
    ch.hline(98.5, t("stop (1R = 1.5)", "Stop (1R = 1.5)"), C["bear"], side="left")
    ch.hline(106, t("A · fixed +4R at prior high", "A · เป้าตายตัว +4R ที่จุดสูงเดิม"), C["amber"], side="right")
    ch.hline(103, t("B · half off at +2R", "B · ปิดครึ่งที่ +2R"), C["teal"], side="right", i0=3)
    idx = [0] + [sum([3, 2, 4, 2, 4, 2, 4, 3][:k]) - 1 for k in range(1, len(piv))]
    steps = [(0, 98.5)]
    for k in (2, 4, 6):
        i = idx[k]
        lvl = cs[i][2] - 0.4
        steps += [(i + 2, steps[-1][1]), (i + 2, lvl)]
    steps.append((len(cs) - 1, steps[-1][1]))
    ch.path(steps, C["purple"], 2.2)
    ch.draw()
    ch.label(len(cs) - 1, steps[-1][1], t("C · trail", "C · เลื่อนตาม"), C["purple"], dy=20, anchor="end")
    s.card(650, 90, 282, 115, t("A · Fixed target", "A · เป้าตายตัว"),
           t("At the next opposing level.\nSimple. Caps big winners.", "ที่ระดับฝั่งตรงข้ามถัดไป\nง่าย แต่จำกัดไม้ที่ชนะใหญ่"), C["amber"], 16, 13)
    s.card(650, 218, 282, 115, t("B · Partial + runner", "B · ปิดบางส่วน + ปล่อยวิ่ง"),
           t("Bank half at +2R, move stop\nto break-even, let the rest run.", "เก็บครึ่งที่ +2R ย้าย Stop\nไปจุดเท่าทุน ปล่อยที่เหลือวิ่ง"), C["teal"], 16, 13)
    s.card(650, 346, 282, 115, t("C · Structure trail", "C · เลื่อนตามโครงสร้าง"),
           t("Move the stop under each new HL\n(BOS confirmed). Catches trends.", "ย้าย Stop ไปใต้ HL ใหม่ทุกครั้ง\n(หลัง BOS) จับเทรนด์ได้ยาว"), C["purple"], 16, 13)
    return s.render()


# ---------------------------------------------------------------- 3.6
@fig
def recovery(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Losses and recoveries are not symmetric", "การขาดทุนกับการฟื้นตัวไม่สมมาตรกัน"),
            t("Gain needed to get back to break-even = loss ÷ (1 − loss)", "กำไรที่ต้องทำเพื่อกลับมาเท่าทุน = ขาดทุน ÷ (1 − ขาดทุน)"))
    panel(s, 28, 90, 904, 360)
    losses = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.75, 0.90]
    x0, base, scale = 90, 330, 1.15
    cap = 200
    s.line(x0 - 20, base, 900, base, C["dim"], 1)
    for k, L in enumerate(losses):
        gx = x0 + k * 102
        g = L / (1 - L)
        lh = L * 100 * scale * 0.8
        s.rect(gx, base, 34, lh * 0.55, fill=C["bear"], rx=3, opacity=0.85)
        s.text(gx + 17, base + lh * 0.55 + 16, f"−{L * 100:.0f}%", 12, C["bear"], "middle", 700)
        gh = min(g * 100, 150) * scale
        s.rect(gx + 40, base - gh, 34, gh, fill=C["bull"], rx=3, opacity=0.85)
        if g * 100 > 150:
            s.line(gx + 36, base - gh + 14, gx + 78, base - gh + 6, C["panel"], 4)
        s.text(gx + 57, base - gh - 8, f"+{g * 100:.0f}%", 13, C["bull"], "middle", 700)
    s.rect(640, 108, 14, 14, fill=C["bear"], rx=3)
    s.text(660, 120, t("loss", "ขาดทุน"), 13, C["text"])
    s.rect(730, 108, 14, 14, fill=C["bull"], rx=3)
    s.text(750, 120, t("gain needed to recover", "กำไรที่ต้องทำเพื่อฟื้น"), 13, C["text"])
    s.text(60, 432, t("Small losses are cheap to repair. Big ones may be impossible. Keep drawdowns small and you never need a miracle.",
                      "ขาดทุนเล็กซ่อมได้ถูก ขาดทุนใหญ่อาจซ่อมไม่ได้เลย รักษา Drawdown ให้เล็ก แล้วคุณจะไม่ต้องพึ่งปาฏิหาริย์"),
           13, C["amber"], weight=600)
    return s.render()


@fig
def drawdown_rules(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Drawdown rules: cut size when you are wrong, restore it when you are right",
                        "กฎ Drawdown: ลดขนาดไม้เมื่อผิด คืนขนาดเมื่อกลับมาถูก"),
            t("Decided in advance, applied automatically. Never decided in the middle of a losing streak.",
              "ตัดสินใจไว้ล่วงหน้า ทำตามอัตโนมัติ ห้ามตัดสินใจกลางช่วงแพ้ติดกัน"))
    panel(s, 28, 90, 600, 390)
    eq = [100, 101.5, 103, 102, 104.5, 106, 105, 103.5, 102, 100.6, 101.2, 99.8, 98.4, 97.3, 96.4, 97, 96.6, 97.6,
          98.3, 99.3, 100.4, 101.6, 103, 104.8, 106.4, 107.2, 109]
    n = len(eq) - 1
    x0, y0, w, h = 80, 115, 520, 230
    lo, hi = 93, 110
    X = lambda i: x0 + w * i / n
    Y = lambda v: y0 + h * (hi - v) / (hi - lo)
    pk = 106
    for d, col, lab in ((0.05, C["amber"], "−5%"), (0.10, C["bear"], "−10%")):
        v = pk * (1 - d)
        s.line(x0, Y(v), x0 + w, Y(v), col, 1.4, "5 4")
        s.text(x0 + w - 4, Y(v) - 6, t(f"{lab} from peak", f"{lab} จากจุดสูงสุด"), 12, col, "end", 700)
    s.line(x0, Y(pk), x0 + w, Y(pk), C["dim"], 1, "2 4")
    s.text(x0 + 4, Y(pk) - 6, t("equity peak", "จุดสูงสุดของพอร์ต"), 12, C["muted"])
    s.polyline([(X(i), Y(v)) for i, v in enumerate(eq)], C["text"], 2.4)
    # risk strip
    risk = []
    peak = 0
    cur = 1.0
    for v in eq:
        if v >= peak:
            peak, cur = v, 1.0
        elif v <= peak * 0.95:
            cur = 0.5
        risk.append(cur)
    ry, rh = 380, 60
    s.text(x0 - 8, ry + 10, "1%", 11, C["muted"], "end")
    s.text(x0 - 8, ry + rh / 2 + 10, "0.5%", 11, C["muted"], "end")
    for i, r in enumerate(risk[:-1]):
        col = C["bull"] if r == 1 else C["amber"]
        s.rect(X(i) + 1, ry + rh * (1 - r), X(i + 1) - X(i) - 2, rh * r, fill=col, opacity=0.7, rx=2)
    s.text(x0, ry - 10, t("Risk per trade", "ความเสี่ยงต่อไม้"), 12, C["muted"], weight=600)
    rules = [
        (C["bull"], t("At a new equity high", "เมื่อพอร์ตทำจุดสูงใหม่"), t("Full risk (e.g. 1%)", "เสี่ยงเต็ม (เช่น 1%)")),
        (C["amber"], t("Down 5% from peak", "ลง 5% จากจุดสูงสุด"), t("Halve risk to 0.5%", "ลดความเสี่ยงครึ่งหนึ่ง เหลือ 0.5%")),
        (C["bear"], t("Down 10% from peak", "ลง 10% จากจุดสูงสุด"), t("Stop. Review the journal.\nTrade on demo until fixed.", "หยุด ทบทวนบันทึกการเทรด\nเทรดบัญชีทดลองจนกว่าจะแก้ได้")),
        (C["purple"], t("Daily loss limit", "ลิมิตขาดทุนรายวัน"), t("−2R or 3 losses → done\nfor the day.", "−2R หรือแพ้ 3 ไม้ → พอ\nสำหรับวันนี้")),
    ]
    for k, (col, head, body) in enumerate(rules):
        s.card(650, 90 + k * 98, 282, 88, head, body, col, 15, 13)
    return s.render()


# ---------------------------------------------------------------- 3.7
@fig
def summary(lang):
    t = tr(lang)
    s = SVG(960, 560, t("Phase 3 on one page", "สรุปเฟส 3 ในหน้าเดียว"))
    cx, cy = 480, 310
    nodes = [
        (170, 140, C["purple"], t("3.1 Survive first", "3.1 อยู่รอดก่อน"), t("Risk 0.5–1% per trade.\nStreaks are certain.", "เสี่ยง 0.5–1% ต่อไม้\nแพ้ติดกันเกิดแน่นอน")),
        (790, 140, C["blue"], t("3.2 Position sizing", "3.2 ขนาดไม้"), t("$ risk ÷ stop distance\n= size.", "เงินที่เสี่ยง ÷ ระยะ Stop\n= ขนาดไม้")),
        (150, 320, C["bull"], t("3.3 R-multiples", "3.3 หน่วย R"), t("1R = loss at the stop.\nMeasure everything in R.", "1R = เงินที่เสียเมื่อโดน Stop\nวัดทุกอย่างเป็น R")),
        (810, 320, C["amber"], t("3.4 Expectancy", "3.4 ค่าคาดหวัง"), t("Win% × avg win − Loss% × 1R.\nJudge on 100+ trades.", "%ชนะ × กำไรเฉลี่ย − %แพ้ × 1R\nตัดสินจาก 100+ ไม้")),
        (250, 480, C["teal"], t("3.5 Stops & targets", "3.5 Stop และเป้าหมาย"), t("Stop where the idea is wrong.\nExit plan before entry.", "Stop ตรงที่ไอเดียผิด\nแผนออกก่อนเข้า")),
        (710, 480, C["bear"], t("3.6 Drawdown", "3.6 Drawdown"), t("−50% needs +100%.\nCut size when down.", "−50% ต้องทำ +100%\nลดไม้เมื่อขาดทุน")),
    ]
    for x, y, col, head, body in nodes:
        s.line(cx, cy, x, y, col, 2, opacity=0.5)
    s.circle(cx, cy, 74, C["panel"], C["text"], 2)
    s.text(cx, cy - 4, t("PHASE 3", "เฟส 3"), 20, C["text"], "middle", 700)
    s.text(cx, cy + 20, t("Risk & Money", "ความเสี่ยงและเงินทุน"), 14, C["muted"], "middle")
    for x, y, col, head, body in nodes:
        s.rect(x - 130, y - 42, 260, 92, fill=C["panel"], stroke=col, rx=12)
        s.text(x, y - 14, head, 17, col, "middle", 700)
        s.text(x, y + 10, body, 13, C["text"], "middle")
    return s.render()


# ================================================================ v2 additions (Oct 2026)
@fig
def size_markets(lang):
    t = tr(lang)
    s = SVG(960, 480, t("One formula, four markets (1R = 100 USD)", "สูตรเดียว สี่ตลาด (1R = 100 ดอลลาร์)"),
            t("Size = 1R ÷ loss per unit at the stop. Only the 'unit' changes.", "ขนาด = 1R ÷ ขาดทุนต่อหน่วยเมื่อโดน Stop เปลี่ยนแค่ 'หน่วย'"))
    cards = [(C["blue"], t("Stock", "หุ้น"), t("entry 50.00\nstop 48.00", "เข้า 50.00\nStop 48.00"), t("2.00 per share", "2.00 ต่อหุ้น"), "100 ÷ 2.00", t("50 shares", "50 หุ้น")),
             (C["purple"], t("Crypto", "คริปโต"), t("BTC 60,000\nstop 58,500", "BTC 60,000\nStop 58,500"), t("1,500 per coin", "1,500 ต่อเหรียญ"), "100 ÷ 1,500", "0.0667 BTC"),
             (C["teal"], t("Forex", "ฟอเร็กซ์"), t("EUR/USD\n25-pip stop", "EUR/USD\nStop 25 pip"), t("25 × 10 = 250 per lot", "25 × 10 = 250 ต่อล็อต"), "100 ÷ 250", t("0.4 lots", "0.4 ล็อต")),
             (C["amber"], t("Futures (MES)", "ฟิวเจอร์ส (MES)"), t("4-point stop\n5 USD per point", "Stop 4 จุด\n5 ดอลลาร์ต่อจุด"), t("4 × 5 = 20 per contract", "4 × 5 = 20 ต่อสัญญา"), "100 ÷ 20", t("5 contracts", "5 สัญญา"))]
    for k, (col, head, setup, unit, calc, ans) in enumerate(cards):
        x = 28 + k * 230
        s.rect(x, 96, 216, 340, fill=C["panel"], stroke=col, rx=12)
        s.text(x + 108, 128, head, 17, col, "middle", 700)
        s.text(x + 108, 168, setup, 14, C["text"], "middle")
        s.text(x + 108, 248, t("loss per unit", "ขาดทุนต่อหน่วย"), 12, C["muted"], "middle")
        s.text(x + 108, 272, unit, 13, C["text"], "middle", 700)
        s.text(x + 108, 330, calc, 14, C["muted"], "middle")
        s.text(x + 108, 380, "= " + ans, 20, col, "middle", 800)
    s.text(28, 462, t("Always round DOWN. If the smallest tradable size is still too big, the trade is not for your account.",
                      "ปัดลงเสมอ ถ้าขนาดเล็กที่สุดที่ซื้อขายได้ยังใหญ่เกิน ไม้นั้นไม่ใช่สำหรับบัญชีของคุณ"), 13, C["amber"], weight=600)
    return s.render()


@fig
def breakeven_curve(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Break-even win rate = 1 ÷ (1 + reward:risk)", "อัตราชนะที่เท่าทุน = 1 ÷ (1 + ผลตอบแทน:ความเสี่ยง)"),
            t("Above the curve you make money (before costs); below it you lose.", "เหนือเส้นโค้งคุณได้เงิน (ก่อนหักต้นทุน) ใต้เส้นคุณเสียเงิน"))
    x0, x1, y0, y1 = 100, 880, 110, 400
    X = lambda r: x0 + (r - 0.25) / (4 - 0.25) * (x1 - x0)
    Y = lambda w: y1 - w * (y1 - y0)
    for w in (0, 0.25, 0.5, 0.75, 1.0):
        s.line(x0, Y(w), x1, Y(w), C["grid"], 1)
        s.text(x0 - 10, Y(w) + 4, f"{w:.0%}", 12, C["muted"], "end")
    for r in (0.5, 1, 1.5, 2, 3, 4):
        s.text(X(r), y1 + 20, f"{r:g}R", 12, C["muted"], "middle")
    s.text((x0 + x1) / 2, y1 + 42, t("average win ÷ average loss (reward:risk)", "กำไรเฉลี่ย ÷ ขาดทุนเฉลี่ย (ผลตอบแทน:ความเสี่ยง)"), 12, C["muted"], "middle")
    pts = [(X(r), Y(1 / (1 + r))) for r in [0.25 + 0.05 * i for i in range(76)]]
    s.polygon(pts + [(X(4), Y(1)), (X(0.25), Y(1))], C["bull"], 0.08)
    s.polyline(pts, C["amber"], 3)
    for r, w, lab, col in ((0.3, 0.75, t("scalper 75% @ 0.3R", "Scalper 75% @ 0.3R"), C["bear"]), (1.8, 0.45, t("swing 45% @ 1.8R", "Swing 45% @ 1.8R"), C["bull"]),
                           (3.0, 0.35, t("trend 35% @ 3R", "Trend 35% @ 3R"), C["bull"])):
        s.circle(X(r), Y(w), 7, col)
        s.text(X(r) + 12, Y(w) - 10, lab, 13, col, weight=700)
    for r in (1, 2, 3):
        s.text(X(r), Y(1 / (1 + r)) + 22, f"{1 / (1 + r):.0%}", 12, C["amber"], "middle", 700)
    return s.render()


# ---------------------------------------------------------------- v2 additions (B9c)
def dd_odds_sim(risk, dd, n=200, runs=20000, seed=11):
    """Monte Carlo: P(drawdown from peak >= dd within n trades), 45% wins at +2R, losses -1R."""
    rnd = random.Random(seed)
    hit = 0
    for _ in range(runs):
        eq = peak = 1.0
        for _ in range(n):
            eq *= (1 + 2 * risk) if rnd.random() < 0.45 else (1 - risk)
            peak = max(peak, eq)
            if eq <= peak * (1 - dd):
                hit += 1
                break
    return hit / runs


@fig
def dd_odds(lang):
    t = tr(lang)
    s = SVG(960, 460, t("Same winning system, different risk: odds of a deep drawdown", "ระบบที่ชนะเดียวกัน ความเสี่ยงต่างกัน: โอกาสเกิด Drawdown ลึก"),
            t("Chance of falling 20% (and 50%) below the peak within 200 trades. 45% wins at +2R. 20,000 simulations each.",
              "โอกาสร่วงต่ำกว่าจุดสูงสุด 20% (และ 50%) ภายใน 200 ไม้ ชนะ 45% ได้ +2R จำลองอย่างละ 20,000 ครั้ง"))
    risks = [0.005, 0.01, 0.02, 0.03, 0.05, 0.10]
    x0, base, hmax, gw = 90, 370, 200, 136
    s.line(x0 - 20, base, x0 + len(risks) * gw, base, C["dim"], 1.5)
    for k, r in enumerate(risks):
        x = x0 + k * gw
        for j, (dd, col) in enumerate(((0.20, C["amber"]), (0.50, C["bear"]))):
            p = dd_odds_sim(r, dd)
            bx = x + j * 48
            s.rect(bx, base - p * hmax, 42, max(p * hmax, 1.5), fill=col, opacity=0.85, rx=4)
            s.text(bx + 21, base - p * hmax - 8, f"{p * 100:.0f}%" if p >= 0.01 or p == 0 else "<1%", 13, col, "middle", 700)
        s.text(x + 45, base + 24, t(f"risk {r * 100:g}%", f"เสี่ยง {r * 100:g}%"), 14, C["text"], "middle", 700)
    s.rect(70, 104, 14, 14, fill=C["amber"], rx=3)
    s.text(92, 116, t("−20% from peak", "−20% จากจุดสูงสุด"), 13, C["text"])
    s.rect(240, 104, 14, 14, fill=C["bear"], rx=3)
    s.text(262, 116, t("−50% from peak", "−50% จากจุดสูงสุด"), 13, C["text"])
    s.text(70, 430, t("The edge is identical in every column. Only the size changes, and above ~2% a deep drawdown becomes likely.",
                      "ความได้เปรียบเท่ากันทุกคอลัมน์ เปลี่ยนแค่ขนาด และเมื่อเกิน ~2% Drawdown ลึกก็มีโอกาสสูง"), 13, C["amber"], weight=600)
    return s.render()


@fig
def r_week(lang):
    t = tr(lang)
    s = SVG(960, 440, t("A week in R: five trades, one number", "หนึ่งสัปดาห์ในหน่วย R: ห้าไม้ ตัวเลขเดียว"),
            t("Results from lesson 3.3's example. The line is the running total.", "ผลจากตัวอย่างในบทที่ 3.3 เส้นคือยอดรวมสะสม"))
    res = [2.0, -1.0, -1.0, 3.1, -0.4]
    x0, zero, sc, bw = 120, 250, 36, 70
    s.line(x0 - 30, zero, x0 + 5 * 120, zero, C["dim"], 1.5)
    s.text(x0 - 40, zero + 4, "0R", 12, C["muted"], "end")
    cum, pts = 0, [(x0 - 30, zero)]
    for k, r in enumerate(res):
        x = x0 + k * 120
        col = C["bull"] if r > 0 else C["bear"]
        s.rect(x, min(zero, zero - r * sc), bw, abs(r) * sc, fill=col, opacity=0.8, rx=4)
        s.text(x + bw / 2, zero - r * sc + (-8 if r > 0 else 18), f"{r:+.1f}R", 14, col, "middle", 700)
        s.text(x + bw / 2, 400, t(f"trade {k + 1}", f"ไม้ที่ {k + 1}"), 12, C["muted"], "middle")
        cum += r
        pts.append((x + bw / 2, zero - cum * sc))
    s.polyline(pts, C["amber"], 2.5, "6 4")
    for x, y in pts[1:]:
        s.circle(x, y, 4, C["amber"])
    s.card(730, 100, 200, 300, t("The week", "สัปดาห์นี้"),
           t("Total: +2.7R\nWin rate: 2/5 = 40%\nAvg win: +2.55R\nAvg loss: −0.8R\n \nAt 1R = 50 USD:\n+135 USD\nAt 1R = 500 USD:\n+1,350 USD",
             "รวม: +2.7R\nอัตราชนะ: 2/5 = 40%\nชนะเฉลี่ย: +2.55R\nแพ้เฉลี่ย: −0.8R\n \nที่ 1R = 50 ดอลลาร์:\n+135 ดอลลาร์\nที่ 1R = 500 ดอลลาร์:\n+1,350 ดอลลาร์"), C["amber"], 16, 14)
    return s.render()


@fig
def buffer_math(lang):
    t = tr(lang)
    s = SVG(960, 440, t("The buffer: a little more risk, a lot fewer false stops", "ระยะเผื่อ: เสี่ยงเพิ่มนิดเดียว แต่โดน Stop หลอกน้อยลงมาก"),
            t("Lesson 3.5's long: entry 103.6, swing low 101.9, ATR 1.4, target 110, risk 100 USD per trade.",
              "ไม้ซื้อในบทที่ 3.5: เข้า 103.6 Swing low 101.9 ATR 1.4 เป้า 110 เสี่ยงไม้ละ 100 ดอลลาร์"))
    rows = [(t("No buffer", "ไม่มีระยะเผื่อ"), 101.9, C["bear"], t("✗ the wick to 101.9 touches it", "✗ ไส้ที่ 101.9 แตะพอดี")),
            (t("0.25 × ATR", "0.25 × ATR"), 101.55, C["amber"], t("✓ survives the wick", "✓ รอดจากไส้")),
            (t("0.5 × ATR", "0.5 × ATR"), 101.2, C["bull"], t("✓ survives, more room", "✓ รอด และมีที่ว่างมากกว่า"))]
    X = lambda p: 210 + (p - 100.5) * 56
    for p in (102, 104, 106, 108, 110):
        s.line(X(p), 105, X(p), 360, C["grid"], 1)
        s.text(X(p), 378, f"{p}", 12, C["muted"], "middle")
    s.line(X(101.9), 105, X(101.9), 360, C["blue"], 1.5, "4 4")
    s.text(X(101.9), 398, t("swing low 101.9", "Swing low 101.9"), 12, C["blue"], "middle", 600)
    for k, (name, stop, col, note) in enumerate(rows):
        y = 120 + k * 80
        risk, rew = 103.6 - stop, 110 - 103.6
        s.text(40, y + 22, name, 15, col, weight=700)
        s.text(40, y + 44, t(f"stop {stop:g}", f"Stop {stop:g}"), 12, C["muted"])
        s.rect(X(stop), y + 6, X(103.6) - X(stop), 28, fill=C["bear"], opacity=0.5, rx=3)
        s.rect(X(103.6), y + 6, X(110) - X(103.6), 28, fill=C["bull"], opacity=0.3, rx=3)
        s.text(X(110) + 10, y + 20, f"{rew / risk:.1f}R · " + t(f"size {100 / risk:.0f}", f"ขนาด {100 / risk:.0f}"), 13, col, weight=700)
        s.text(X(110) + 10, y + 38, note, 12, C["text"])
    return s.render()


def policy_path(policy, seq="LLLLLLLLWWWWWW", start=10000.0):
    eq = peak = start
    risk, out = 0.01, [start]
    for ch in seq:
        if policy == "halve":
            risk = 0.005 if eq <= peak * 0.95 else 0.01
        r = min(eq * risk, eq)
        eq = max(eq + (2 * r if ch == "W" else -r), 0)
        peak = max(peak, eq)
        if policy == "double":
            risk = 0.01 if ch == "W" else risk * 2
        out.append(eq)
    return out


@fig
def sizing_policies(lang):
    t = tr(lang)
    s = SVG(960, 480, t("Same trades, three sizing rules", "เทรดชุดเดียวกัน กฎขนาดไม้สามแบบ"),
            t("8 losses in a row, then 6 wins at +2R. Start 10,000 USD, 1% risk (computed).",
              "แพ้ติดกัน 8 ไม้ แล้วชนะ 6 ไม้ที่ +2R เริ่ม 10,000 ดอลลาร์ เสี่ยง 1% (คำนวณจริง)"))
    pols = [("fixed", t("Fixed 1%", "คงที่ 1%"), C["blue"]), ("halve", t("Halve at −5%", "ลดครึ่งที่ −5%"), C["bull"]),
            ("double", t("Double after each loss", "เพิ่มเท่าตัวหลังแพ้"), C["bear"])]
    x0, y0, w, h = 70, 110, 560, 300
    s.rect(x0 - 20, y0 - 10, w + 40, h + 40, fill=C["panel"], stroke=C["border"], rx=12)
    X = lambda i: x0 + i * w / 14
    Y = lambda v: y0 + h * (10600 - v) / 10600
    for v in (0, 2500, 5000, 7500, 10000):
        s.line(x0, Y(v), x0 + w, Y(v), C["grid"], 1)
        s.text(x0 - 6, Y(v) + 4, f"{v:,}", 11, C["muted"], "end")
    s.rect(X(0), y0, X(8) - X(0), h, fill=C["bear"], opacity=0.06)
    s.text((X(0) + X(8)) / 2, y0 + 16, t("8 losses", "แพ้ 8 ไม้"), 12, C["bear"], "middle", 600)
    s.text((X(8) + X(14)) / 2, y0 + 16, t("6 wins", "ชนะ 6 ไม้"), 12, C["bull"], "middle", 600)
    for k, (key, name, col) in enumerate(pols):
        path = policy_path(key)
        s.polyline([(X(i), Y(v)) for i, v in enumerate(path)], col, 2.5)
        low = min(path)
        y = 130 + k * 95
        s.card(660, y - 20, 270, 82, name, None, col, 15)
        s.text(680, y + 34, t(f"worst: {low:,.0f} ({(low / 10000 - 1) * 100:+.1f}%)", f"ต่ำสุด: {low:,.0f} ({(low / 10000 - 1) * 100:+.1f}%)"), 13, C["text"])
        s.text(680, y + 54, t(f"end: {path[-1]:,.0f}", f"สุดท้าย: {path[-1]:,.0f}"), 13, col, weight=700)
    return s.render()


# ---------------------------------------------------------------- 3.8 trade management (C2)
# Results printed by _tools/quant/exit_methods.py (20,000 trades per method, seed 11).
EXIT_RESULTS = {
    "none": [(-0.022, 50.4), (-0.004, 34.5), (0.011, 26.7), (0.015, 34.8), (0.011, 47.9)],
    "edge": [(0.107, 56.6), (0.259, 43.1), (0.418, 36.8), (0.376, 43.1), (0.243, 54.5)],
}


@fig
def exit_methods(lang):
    t = tr(lang)
    s = SVG(960, 520, t("Exit methods reshape results; they don't create an edge", "วิธีออกเปลี่ยนรูปผลลัพธ์ แต่ไม่ได้สร้างความได้เปรียบ"),
            t("Simulated price paths, stop −1R, 20,000 trades per method (_tools/quant/exit_methods.py).",
              "เส้นทางราคาจำลอง Stop −1R วิธีละ 20,000 ไม้ (_tools/quant/exit_methods.py)"))
    names = [t("Target 1R", "เป้า 1R"), t("Target 2R", "เป้า 2R"), t("Target 3R", "เป้า 3R"),
             t("Half at 2R, BE,\nrest at 4R", "ครึ่งที่ 2R, เท่าทุน,\nที่เหลือ 4R"), t("Trail 1R\nafter +1R", "เลื่อน Stop 1R\nหลัง +1R")]
    for k, (key, title, col) in enumerate((("none", t("No edge (random walk)", "ไม่มีความได้เปรียบ (สุ่ม)"), C["muted"]),
                                          ("edge", t("With an edge (small upward drift)", "มีความได้เปรียบ (แนวโน้มขึ้นเล็กน้อย)"), C["bull"]))):
        x0 = 40 + k * 460
        panel(s, x0 - 12, 92, 444, 400, title, col)
        base, sc = 330, 380
        s.line(x0, base, x0 + 420, base, C["dim"], 1.5)
        for j, ((e, w), nm) in enumerate(zip(EXIT_RESULTS[key], names)):
            x = x0 + 14 + j * 82
            h = e * sc
            c = C["bull"] if e > 0.03 else (C["bear"] if e < -0.03 else C["amber"])
            s.rect(x, min(base, base - h), 50, max(abs(h), 2), fill=c, opacity=0.85, rx=3)
            s.text(x + 25, base - max(h, 0) - 8, f"{round(e, 2) + 0:+.2f}R", 12, c, "middle", 700)
            s.text(x + 25, base + 22, f"{w:.0f}% " + t("wins", "ชนะ"), 11, C["muted"], "middle")
            s.text(x + 25, base + 44, nm, 11, C["text"], "middle", 600)
    s.text(40, 510, t("No edge: every method averages ≈ 0R (within ±0.02R noise). With an edge, how you exit changes how much of it you keep.",
                      "ไม่มีความได้เปรียบ: ทุกวิธีเฉลี่ย ≈ 0R (ภายในสัญญาณรบกวน ±0.02R) เมื่อมีความได้เปรียบ วิธีออกกำหนดว่าคุณเก็บได้มากแค่ไหน"), 12, C["amber"], weight=600)
    return s.render()


@fig
def partial_tree(lang):
    t = tr(lang)
    s = SVG(960, 440, t("'Half at +2R, stop to break-even, rest to +4R': the three outcomes", "'ครึ่งที่ +2R เลื่อน Stop ไปจุดเท่าทุน ที่เหลือ +4R': ผลลัพธ์สามแบบ"),
            t("Entry 100, stop 98 (1R = 2 points), 2 units. Targets 104 (+2R) and 108 (+4R).",
              "เข้า 100 Stop 98 (1R = 2 จุด) 2 หน่วย เป้า 104 (+2R) และ 108 (+4R)"))
    s.card(40, 170, 200, 90, t("Entry", "เข้า"), t("2 units at 100\nstop 98", "2 หน่วยที่ 100\nStop 98"), C["blue"], 16, 13)
    outs = [(t("Stopped before 104", "โดน Stop ก่อนถึง 104"), t("2 units × −2 = −4 points", "2 หน่วย × −2 = −4 จุด"), "−1R", C["bear"], 100),
            (t("104 hit, then back to 100", "ถึง 104 แล้วกลับมา 100"), t("1 unit +4, 1 unit 0 = +4 points", "1 หน่วย +4, 1 หน่วย 0 = +4 จุด"), "+1R", C["amber"], 210),
            (t("104 hit, then 108 hit", "ถึง 104 แล้วถึง 108"), t("1 unit +4, 1 unit +8 = +12 points", "1 หน่วย +4, 1 หน่วย +8 = +12 จุด"), "+3R", C["bull"], 320)]
    for name, body, r, col, y in outs:
        s.arrow(244, 215, 380, y + 30, C["dim"], 1.8)
        s.card(390, y, 420, 76, name, body, col, 15, 13)
        s.text(860, y + 46, r, 24, col, "middle", 800)
    s.text(40, 428, t("4 points of profit = 4 ÷ (2 units × 2 points of risk) = +1R. The worst case after the first target is +1R, not −1R.",
                      "กำไร 4 จุด = 4 ÷ (2 หน่วย × ความเสี่ยง 2 จุด) = +1R กรณีแย่สุดหลังถึงเป้าแรกคือ +1R ไม่ใช่ −1R"), 12, C["muted"])
    return s.render()


@fig
def trail_chart(lang):
    t = tr(lang)
    s = SVG(960, 460, t("Trailing a stop under structure", "เลื่อน Stop ตามโครงสร้าง"),
            t("Long from 100, initial stop 98. After each new higher low is confirmed, the stop moves below it (illustrative).",
              "ซื้อที่ 100 Stop แรก 98 ทุกครั้งที่จุดต่ำที่สูงขึ้นใหม่ยืนยัน Stop เลื่อนไปใต้มัน (ตัวอย่าง)"))
    piv = [100, 104, 101.6, 107, 104.5, 110, 107.2, 112.5, 106.4]
    cs = candles_from_path(piv, [4, 3, 4, 3, 4, 3, 4, 5], seed=33)
    panel(s, 28, 86, 904, 350)
    ch = CandleChart(s, 50, 110, 860, 280, cs, pmin=96.8, grid=False)
    ch.draw()
    stops = [(0, 98.0), (7, 98.0), (7, 101.2), (14, 101.2), (14, 104.1), (21, 104.1), (21, 106.8), (len(cs) - 1, 106.8)]
    ch.path(stops, C["bear"], 2.2, "6 4")
    for i, p, lab in ((0, 98.0, "98"), (7, 101.2, "101.2"), (14, 104.1, "104.1"), (21, 106.8, "106.8")):
        ch.label(i + 1.2, p, lab, C["bear"], dy=16, size=12)
    end = len(cs) - 1
    ch.label(end, cs[end][2], t("exit at 106.8 = +3.4R", "ออกที่ 106.8 = +3.4R"), C["bull"], dy=30, size=13, anchor="end")
    s.text(50, 425, t("Each stop sits just below a confirmed higher low. The trend's first lower low ends the trade with most of the move kept.",
                      "Stop แต่ละครั้งอยู่ใต้จุดต่ำที่สูงขึ้นที่ยืนยันแล้ว จุดต่ำที่ต่ำลงครั้งแรกของเทรนด์จบเทรด โดยเก็บการขยับส่วนใหญ่ไว้ได้"), 12, C["muted"])
    return s.render()


@fig
def scale_in(lang):
    t = tr(lang)
    s = SVG(960, 460, t("Scaling in without raising your risk", "เพิ่มโพซิชันโดยไม่เพิ่มความเสี่ยง"),
            t("Risk budget 100 USD (1R). Add only after the first part is in profit, and move the stop so the total worst case stays 1R.",
              "งบความเสี่ยง 100 ดอลลาร์ (1R) เพิ่มเฉพาะหลังส่วนแรกกำไร และเลื่อน Stop ให้กรณีแย่สุดรวมยังเป็น 1R"))
    rows = [(t("Step 1 · buy 50 at 100, stop 98", "ขั้น 1 · ซื้อ 50 ที่ 100 Stop 98"), t("worst case: 50 × (98 − 100) = −100 USD = −1R", "กรณีแย่สุด: 50 × (98 − 100) = −100 ดอลลาร์ = −1R"), C["blue"]),
            (t("Step 2 · price 104: add 50 at 104, move ALL stops to 101", "ขั้น 2 · ราคา 104: เพิ่ม 50 ที่ 104 เลื่อน Stop ทั้งหมดไป 101"),
             t("worst case: 50 × (+1) + 50 × (−3) = +50 − 150 = −100 USD = −1R · average entry 102", "กรณีแย่สุด: 50 × (+1) + 50 × (−3) = +50 − 150 = −100 ดอลลาร์ = −1R · ต้นทุนเฉลี่ย 102"), C["amber"]),
            (t("Step 3 · price reaches 110", "ขั้น 3 · ราคาถึง 110"),
             t("50 × 10 + 50 × 6 = +800 USD = +8R  (one unit only: 50 × 10 = +500 USD = +5R)", "50 × 10 + 50 × 6 = +800 ดอลลาร์ = +8R  (หน่วยเดียว: 50 × 10 = +500 ดอลลาร์ = +5R)"), C["bull"])]
    for k, (head, body, col) in enumerate(rows):
        y = 100 + k * 110
        s.card(40, y, 880, 92, head, body, col, 16, 14)
    s.text(40, 445, t("The add is paid for by the first unit's open profit. If the trade had never moved in your favour, you would never have added.",
                      "การเพิ่มจ่ายด้วยกำไรที่ยังไม่ปิดของหน่วยแรก ถ้าเทรดไม่เคยวิ่งไปในทางของคุณ คุณก็จะไม่เพิ่มเลย"), 12, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 3.9 portfolio risk (C2)
import math as _m


@fig
def correlation_risk(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Correlation: two 1% trades are not always '2% spread out'", "สหสัมพันธ์: เทรด 1% สองไม้ไม่ได้ 'กระจาย 2%' เสมอไป"),
            t("Typical swing of the combined position, in % of the account, for two positions that each swing 1% (σ = √(1² + 1² + 2ρ)).",
              "การแกว่งโดยทั่วไปของโพซิชันรวม เป็น % ของบัญชี สำหรับสองโพซิชันที่แกว่งตัวละ 1% (σ = √(1² + 1² + 2ρ))"))
    rows = [(0.0, t("unrelated (ρ = 0)", "ไม่สัมพันธ์ (ρ = 0)")), (0.5, t("ρ = 0.5", "ρ = 0.5")), (0.9, t("very similar (ρ = 0.9)", "คล้ายกันมาก (ρ = 0.9)")),
            (1.0, t("identical (ρ = 1)", "เหมือนกันทุกอย่าง (ρ = 1)"))]
    base, sc = 340, 110
    for k, (rho, name) in enumerate(rows):
        v = _m.sqrt(2 + 2 * rho)
        x = 110 + k * 200
        col = C["bull"] if rho == 0 else (C["amber"] if rho < 0.9 else C["bear"])
        s.rect(x, base - v * sc, 100, v * sc, fill=col, opacity=0.85, rx=4)
        s.text(x + 50, base - v * sc - 10, f"{v:.2f}%", 15, col, "middle", 700)
        s.text(x + 50, base + 24, name, 12, C["text"], "middle", 600)
    s.line(90, base, 900, base, C["dim"], 1.5)
    s.text(60, 410, t("Five 1% positions with ρ = 0.8 swing like √(5 + 20 × 0.8) = 4.58%, almost five times one trade; unrelated, √5 = 2.24%.",
                      "ห้าโพซิชัน 1% ที่ ρ = 0.8 แกว่งเท่ากับ √(5 + 20 × 0.8) = 4.58% เกือบห้าเท่าของเทรดเดียว ถ้าไม่สัมพันธ์กัน √5 = 2.24%"), 12, C["amber"], weight=600)
    return s.render()


@fig
def kelly_curve(lang):
    t = tr(lang)
    W, b = 0.45, 2.0
    g = lambda f: W * _m.log(1 + b * f) + (1 - W) * _m.log(1 - f)
    s = SVG(960, 470, t("Kelly: growth per trade vs risk per trade", "Kelly: การเติบโตต่อไม้ vs ความเสี่ยงต่อไม้"),
            t("System: 45% wins at +2R, losses −1R. Growth = average log return per trade (computed).",
              "ระบบ: ชนะ 45% ที่ +2R แพ้ −1R การเติบโต = ผลตอบแทนลอการิทึมเฉลี่ยต่อไม้ (คำนวณจริง)"))
    x0, y0, w, h = 90, 100, 800, 300
    panel(s, x0 - 60, y0 - 14, w + 90, h + 70)
    X = lambda f: x0 + w * f / 0.40
    Y = lambda v: y0 + h * (0.035 - v) / 0.055
    for v in (-0.02, -0.01, 0, 0.01, 0.02, 0.03):
        s.line(x0, Y(v), x0 + w, Y(v), C["dim"] if v == 0 else C["grid"], 1.5 if v == 0 else 1)
        s.text(x0 - 8, Y(v) + 4, f"{v * 100:+.0f}%", 11, C["muted"], "end")
    for f in (0, 0.1, 0.2, 0.3, 0.4):
        s.text(X(f), y0 + h + 22, f"{f:.0%}", 11, C["muted"], "middle")
    s.polyline([(X(f / 1000), Y(g(f / 1000))) for f in range(0, 400, 2)], C["blue"], 3)
    for f, lab, col in ((0.01, "1%", C["bull"]), (0.02, "2%", C["bull"]), (0.04375, t("¼ Kelly", "¼ Kelly"), C["teal"]),
                        (0.0875, t("½ Kelly", "½ Kelly"), C["amber"]), (0.175, t("Kelly 17.5%", "Kelly 17.5%"), C["bear"])):
        s.circle(X(f), Y(g(f)), 6, col)
        dy, anc, dx = ((22, "start", 8) if f == 0.01 else (-12, "middle", 0))
        s.text(X(f) + dx, Y(g(f)) + dy, f"{lab} · {g(f) * 100:.2f}%", 11, col, anc, 700)
    s.text(X(0.3557), Y(0) + 18, t("growth = 0 at 35.6%", "การเติบโต = 0 ที่ 35.6%"), 11, C["bear"], "middle", 700)
    s.text(x0 + w / 2, y0 + h + 44, t("risk per trade (% of account)", "ความเสี่ยงต่อไม้ (% ของบัญชี)"), 12, C["muted"], "middle")
    return s.render()


def _mc_paths(risk, n=2000, trades=200, seed=7, win=0.45, payoff=2.0):
    import random as _r
    rnd = _r.Random(seed)
    paths = []
    for _ in range(n):
        eq, p = 1.0, [1.0]
        for _ in range(trades):
            eq *= (1 + risk * payoff) if rnd.random() < win else (1 - risk)
            p.append(eq)
        paths.append(p)
    return paths


@fig
def mc_fan(lang):
    t = tr(lang)
    s = SVG(960, 480, t("Monte Carlo: the same system, 2,000 possible futures", "Monte Carlo: ระบบเดียวกัน 2,000 อนาคตที่เป็นไปได้"),
            t("45% wins at +2R, 200 trades. Shaded: 5th–95th percentile of the account; line: median. Left 1% risk, right 2% risk.",
              "ชนะ 45% ที่ +2R 200 ไม้ แถบ: เปอร์เซ็นไทล์ที่ 5–95 ของบัญชี เส้น: มัธยฐาน ซ้ายเสี่ยง 1% ขวาเสี่ยง 2%"))
    for k, risk in enumerate((0.01, 0.02)):
        x0 = 60 + k * 450
        panel(s, x0 - 30, 92, 430, 360, t(f"risk {risk:.0%} per trade", f"เสี่ยง {risk:.0%} ต่อไม้"), C["bull"] if k == 0 else C["amber"])
        paths = _mc_paths(risk)
        cols = list(zip(*paths))
        q = lambda c, p: sorted(c)[int(p * (len(c) - 1))]
        lo = [q(c, 0.05) for c in cols]
        md = [q(c, 0.5) for c in cols]
        hi = [q(c, 0.95) for c in cols]
        top = 8.0
        X = lambda i: x0 + 380 * i / 200
        Y = lambda v: 140 + 280 * (_m.log(top) - _m.log(v)) / (_m.log(top) - _m.log(0.5))
        for v in (0.5, 1, 2, 4, 8):
            s.line(x0, Y(v), x0 + 380, Y(v), C["grid"], 1)
            s.text(x0 - 6, Y(v) + 4, f"{v:g}×", 11, C["muted"], "end")
        s.polygon([(X(i), Y(v)) for i, v in enumerate(hi)] + [(X(i), Y(v)) for i, v in reversed(list(enumerate(lo)))],
                  C["blue"], opacity=0.25)
        s.polyline([(X(i), Y(v)) for i, v in enumerate(md)], C["blue"], 2.5)
        s.text(X(200) - 4, Y(md[-1]) - 10, t(f"median {md[-1]:.2f}×", f"มัธยฐาน {md[-1]:.2f}×"), 12, C["text"], "end", 700)
        s.text(X(200) - 4, Y(lo[-1]) + 18, t(f"5th pct {lo[-1]:.2f}×", f"เปอร์เซ็นไทล์ 5: {lo[-1]:.2f}×"), 11, C["muted"], "end")
    return s.render()
