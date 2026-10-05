"""Phase 9 figures: Quant & Data Analysis. Backtest numbers come from _tools/quant/sma_crossover.py."""
import math
import random
from charts import SVG, C, tr
from figures.p2 import panel
from figures.p6 import Plot
from quant import sma_crossover as q

FIGURES = {}
_RES = {}


def fig(fn):
    FIGURES["p9-" + fn.__name__.replace("_", "-")] = fn
    return fn


def res():
    if not _RES:
        prices = q.synthetic_prices()
        _RES.update(q.run(prices), prices=prices)
    return _RES


def fat_returns(n=2000, seed=3):
    rnd = random.Random(seed)
    return [(rnd.gauss(0.0004, 0.009) if rnd.random() > 0.06 else rnd.gauss(-0.002, 0.03)) for _ in range(n)]


# ---------------------------------------------------------------- 9.1
@fig
def distribution(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Daily returns: centre, spread and tails", "ผลตอบแทนรายวัน: ศูนย์กลาง การกระจาย และหาง"),
            t("2,000 simulated days. Most are small; a few are large, mostly on the downside (fat left tail).",
              "2,000 วันจำลอง ส่วนใหญ่เล็ก มีไม่กี่วันที่ใหญ่ ส่วนมากเป็นขาลง (หางซ้ายอ้วน)"))
    r = fat_returns()
    n = len(r)
    mean = sum(r) / n
    sd = math.sqrt(sum((x - mean) ** 2 for x in r) / (n - 1))
    med = sorted(r)[n // 2]
    skew = sum((x - mean) ** 3 for x in r) / n / sd ** 3
    kurt = sum((x - mean) ** 4 for x in r) / n / sd ** 4 - 3
    beyond3 = sum(abs(x - mean) > 3 * sd for x in r)
    panel(s, 28, 90, 904, 390)
    lo, hi, nb = -0.06, 0.04, 50
    w = (hi - lo) / nb
    bins = [0] * nb
    for x in r:
        j = int((x - lo) / w)
        if 0 <= j < nb:
            bins[j] += 1
    mx = max(bins)
    x0, W, base, H = 60, 600, 430, 300
    X = lambda v: x0 + W * (v - lo) / (hi - lo)
    for j, c in enumerate(bins):
        h = H * c / mx
        s.rect(X(lo + j * w) + 1, base - h, W / nb - 2, h, fill=C["blue"], opacity=0.75, rx=1)
    pdf = lambda v: n * w * math.exp(-((v - mean) / sd) ** 2 / 2) / (sd * math.sqrt(2 * math.pi))
    s.polyline([(X(lo + (hi - lo) * k / 200), base - H * pdf(lo + (hi - lo) * k / 200) / mx) for k in range(201)], C["amber"], 2, "6 4")
    s.line(x0, base, x0 + W, base, C["dim"], 1)
    for v in (-0.06, -0.04, -0.02, 0, 0.02, 0.04):
        s.text(X(v), base + 20, f"{v * 100:+.0f}%" if v else "0", 11, C["muted"], "middle")
    s.line(X(mean), 120, X(mean), base, C["bull"], 1.5, "3 3")
    stats = [
        (t("Mean", "ค่าเฉลี่ย"), f"{mean * 100:+.3f}%"), (t("Median", "มัธยฐาน"), f"{med * 100:+.3f}%"),
        (t("Std dev (σ)", "ส่วนเบี่ยงเบนมาตรฐาน"), f"{sd * 100:.2f}%"), (t("Skew", "ความเบ้"), f"{skew:+.2f}"),
        (t("Excess kurtosis", "ความโด่งส่วนเกิน"), f"{kurt:.1f}"), (t("Days beyond 3σ", "วันที่เกิน 3σ"), f"{beyond3} ({beyond3 / n:.1%})"),
    ]
    for k, (a, b) in enumerate(stats):
        y = 130 + k * 46
        s.text(690, y, a, 13, C["muted"])
        s.text(690, y + 20, b, 17, C["text"], weight=700)
    s.text(690, 420, t("Normal curve predicts\n~0.3% beyond 3σ.", "เส้นโค้งปกติทำนาย\n~0.3% เกิน 3σ"), 12, C["amber"])
    return s.render()


@fig
def sample_size(lang):
    t = tr(lang)
    s = SVG(960, 470, t("How much can a sample tell you?", "กลุ่มตัวอย่างบอกอะไรได้แค่ไหน?"),
            t("You measured a 50% win rate. The true win rate is probably inside this range (95% confidence).",
              "คุณวัดอัตราชนะได้ 50% อัตราชนะจริงน่าจะอยู่ในช่วงนี้ (ความเชื่อมั่น 95%)"))
    panel(s, 28, 90, 904, 360)
    ns = [10, 20, 30, 50, 100, 200, 500]
    x0, W = 160, 700
    X = lambda p: x0 + W * p
    for p in (0, 0.25, 0.5, 0.75, 1):
        s.line(X(p), 120, X(p), 410, C["grid"], 1)
        s.text(X(p), 430, f"{p:.0%}", 12, C["muted"], "middle")
    for k, n in enumerate(ns):
        y = 140 + k * 40
        h = 1.96 * math.sqrt(0.25 / n)
        a, b = max(0, 0.5 - h), min(1, 0.5 + h)
        col = C["bear"] if n < 50 else (C["amber"] if n < 200 else C["bull"])
        s.rect(X(a), y - 10, X(b) - X(a), 20, fill=col, opacity=0.7, rx=10)
        s.circle(X(0.5), y, 5, C["white"])
        s.text(150, y + 5, t(f"{n} trades", f"{n} เทรด"), 13, C["text"], "end", 700)
        s.text(X(b) + 10, y + 5, f"{a:.0%} – {b:.0%}", 12, col, weight=700)
    s.text(48, 450, t("Range ≈ win rate ± 1.96 × √(p(1−p)/n). With 20 trades, a 50% result is consistent with anything from ~28% to ~72%.",
                      "ช่วง ≈ อัตราชนะ ± 1.96 × √(p(1−p)/n) ด้วย 20 เทรด ผล 50% สอดคล้องกับค่าจริงตั้งแต่ ~28% ถึง ~72%"), 12, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 9.2
@fig
def ev_tree(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Expected value: weigh every outcome by its probability", "ค่าคาดหวัง: ถ่วงน้ำหนักทุกผลลัพธ์ด้วยความน่าจะเป็น"),
            t("EV = Σ (probability × outcome). Include every branch, including costs and partial outcomes.",
              "EV = Σ (ความน่าจะเป็น × ผลลัพธ์) รวมทุกกิ่ง รวมถึงต้นทุนและผลลัพธ์บางส่วน"))
    panel(s, 28, 90, 904, 330)
    root = (110, 255)
    s.circle(*root, 30, C["panel"], C["text"], 2)
    s.text(root[0], root[1] + 5, t("trade", "เทรด"), 13, C["text"], "middle", 700)
    branches = [
        (150, C["bull"], "40%", t("full target", "ถึงเป้าเต็ม"), "+2.5R", 0.40 * 2.5),
        (230, C["teal"], "15%", t("partial / trailed", "บางส่วน / เลื่อน Stop"), "+0.8R", 0.15 * 0.8),
        (310, C["muted"], "10%", t("scratch (break-even)", "เสมอตัว"), "0R", 0.0),
        (390, C["bear"], "35%", t("stop hit", "โดน Stop"), "−1.05R", -0.35 * 1.05),
    ]
    for y, col, p, name, out, ev in branches:
        s.line(root[0] + 30, root[1], 330, y, col, 2.5)
        s.text(250, (root[1] + y) / 2 - 6, p, 14, col, "middle", 700)
        s.rect(330, y - 22, 300, 44, fill=C["panel"], stroke=col, rx=10)
        s.text(345, y + 6, name, 14, C["text"])
        s.text(615, y + 6, out, 15, col, "end", 700)
        s.text(660, y + 6, f"{p} × {out} = {ev:+.3f}R", 13, C["muted"])
    total = sum(b[-1] for b in branches)
    s.text(50, 390, t(f"EV = {total:+.2f}R per trade", f"EV = {total:+.2f}R ต่อเทรด"), 18, C["amber"], weight=700)
    s.text(50, 410, t("(−1.05R loss includes slippage)", "(ขาดทุน −1.05R รวม Slippage)"), 11, C["muted"])
    return s.render()


@fig
def convergence(lang):
    t = tr(lang)
    s = SVG(960, 470, t("The law of large numbers: luck averages out, slowly", "กฎจำนวนมาก: โชคเฉลี่ยออกไป แต่ช้า"),
            t("Running average R per trade for five traders with the same +0.35R edge (45% win, +2R / −1R).",
              "ค่าเฉลี่ย R ต่อเทรดสะสมของเทรดเดอร์ 5 คนที่มีความได้เปรียบเท่ากัน +0.35R (ชนะ 45%, +2R / −1R)"))
    panel(s, 28, 90, 904, 360)
    n = 300
    P = Plot(s, 90, 115, 780, 290, n, -1, 1.6)
    for v in (-1, -0.5, 0, 0.5, 1, 1.5):
        s.line(90, P.Y(v), 870, P.Y(v), C["grid"] if v else C["dim"], 1)
        s.text(80, P.Y(v) + 4, f"{v:+.1f}R" if v else "0", 11, C["muted"], "end")
    s.line(90, P.Y(0.35), 870, P.Y(0.35), C["amber"], 2, "6 4")
    s.text(872, P.Y(0.35) + 4, "+0.35R", 12, C["amber"], weight=700)
    for seed, col in zip((1, 2, 3, 4, 5), (C["blue"], C["teal"], C["purple"], C["pink"], C["bull"])):
        rnd = random.Random(seed)
        tot, pts = 0.0, []
        for i in range(1, n + 1):
            tot += 2 if rnd.random() < 0.45 else -1
            pts.append((i, max(min(tot / i, 1.6), -1)))
        P.path(pts, col, 1.8)
    for k in (20, 100, 300):
        s.line(P.X(k), 115, P.X(k), 405, C["dim"], 1, "2 4")
        s.text(P.X(k), 425, t(f"{k} trades", f"{k} เทรด"), 11, C["muted"], "middle")
    return s.render()


# ---------------------------------------------------------------- 9.3
@fig
def overfit(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Overfitting: the best in-sample result is rarely the best out-of-sample",
                        "Overfitting: ผลดีที่สุดในกลุ่มตัวอย่าง ไม่ค่อยดีที่สุดนอกกลุ่มตัวอย่าง"),
            t("Each dot = one SMA (fast, slow) pair tested on the same synthetic data. In-sample = first 70%, out-of-sample = last 30%.",
              "แต่ละจุด = คู่ SMA (เร็ว, ช้า) หนึ่งคู่ที่ทดสอบบนข้อมูลจำลองเดียวกัน In-sample = 70% แรก Out-of-sample = 30% หลัง"))
    prices = res()["prices"]
    cut = int(len(prices) * 0.7)
    pts = []
    for fa in range(5, 65, 5):
        for sl in range(40, 260, 20):
            if fa < sl:
                r, _, _ = q.backtest(prices, fa, sl)
                pts.append((q.metrics(r[:cut])["sharpe"], q.metrics(r[cut:])["sharpe"], fa, sl))
    panel(s, 28, 90, 620, 390)
    P = Plot(s, 90, 115, 530, 320, 1, -0.6, 1.2)
    xlo, xhi = -0.4, 0.8
    X = lambda v: 90 + 530 * (v - xlo) / (xhi - xlo)
    for v in (-0.4, 0, 0.4, 0.8):
        s.line(X(v), 115, X(v), 435, C["grid"], 1)
        s.text(X(v), 455, f"{v:.1f}", 11, C["muted"], "middle")
    for v in (-0.5, 0, 0.5, 1.0):
        s.line(90, P.Y(v), 620, P.Y(v), C["grid"], 1)
        s.text(82, P.Y(v) + 4, f"{v:.1f}", 11, C["muted"], "end")
    best = max(pts)
    for a, b, fa, sl in pts:
        s.circle(X(max(min(a, xhi), xlo)), P.Y(max(min(b, 1.2), -0.6)), 4, C["blue"])
    s.circle(X(best[0]), P.Y(best[1]), 8, C["amber"])
    s.text(X(best[0]) - 10, P.Y(best[1]) - 12, t(f"best in-sample ({best[2]}/{best[3]})", f"ดีที่สุด In-sample ({best[2]}/{best[3]})"), 12, C["amber"], "end", 700)
    s.text(355, 475, t("in-sample Sharpe →", "Sharpe In-sample →"), 12, C["muted"], "middle")
    s.text(40, 110, t("out-of-sample Sharpe ↑", "Sharpe Out-of-sample ↑"), 12, C["muted"])
    ranks = sorted(pts, key=lambda p: -p[1])
    best_rank = [p[2:] for p in ranks].index(best[2:]) + 1
    s.card(668, 92, 264, 190, t("What it shows", "สิ่งที่แสดง"),
           t(f"{len(pts)} combinations tested.\nThe in-sample winner ranks\n#{best_rank} of {len(pts)} out-of-sample.\nPast fit ≠ future edge.",
             f"ทดสอบ {len(pts)} คู่\nผู้ชนะใน In-sample อยู่อันดับ\n#{best_rank} จาก {len(pts)} ใน Out-of-sample\nเข้ากับอดีต ≠ ความได้เปรียบในอนาคต"), C["amber"], 16, 13)
    s.card(668, 296, 264, 184, t("Defences", "การป้องกัน"),
           t("· few parameters\n· out-of-sample & walk-forward\n· prefer broad 'plateaus'\n  over single peaks\n· costs always included", "· พารามิเตอร์น้อย\n· Out-of-sample & Walk-forward\n· เลือก 'ที่ราบสูง' กว้าง ๆ\n  แทนยอดแหลมเดี่ยว\n· รวมต้นทุนเสมอ"), C["bull"], 16, 13)
    return s.render()


@fig
def walk_forward(lang):
    t = tr(lang)
    s = SVG(960, 400, t("Walk-forward testing", "การทดสอบแบบ Walk-forward"),
            t("Optimise on a window, test on the next unseen window, roll forward, repeat. Only the test results count.",
              "ปรับพารามิเตอร์บนหน้าต่างหนึ่ง ทดสอบบนหน้าต่างถัดไปที่ยังไม่เคยเห็น เลื่อนไปข้างหน้า ทำซ้ำ นับเฉพาะผลทดสอบ"))
    panel(s, 28, 90, 904, 290)
    x0, W = 120, 760
    for k in range(5):
        y = 120 + k * 46
        a = x0 + k * 90
        s.rect(a, y, 330, 30, fill=C["blue"], opacity=0.6, rx=6)
        s.text(a + 165, y + 20, t("optimise (train)", "ปรับ (Train)"), 12, C["white"], "middle", 700)
        s.rect(a + 334, y, 106, 30, fill=C["bull"], opacity=0.85, rx=6)
        s.text(a + 387, y + 20, t("test", "ทดสอบ"), 12, C["white"], "middle", 700)
        s.text(100, y + 20, t(f"run {k + 1}", f"รอบ {k + 1}"), 12, C["muted"], "end")
    s.arrow(x0, 360, x0 + W, 360, C["muted"], 2)
    s.text(x0 + W, 350, t("time →", "เวลา →"), 12, C["muted"], "end")
    s.text(x0, 350, t("Stitch the green test periods together = your honest equity curve.",
                      "ต่อช่วงทดสอบสีเขียวเข้าด้วยกัน = Equity Curve ที่ซื่อตรงของคุณ"), 12, C["bull"], weight=700)
    return s.render()


# ---------------------------------------------------------------- 9.4
@fig
def tick(lang):
    t = tr(lang)
    s = SVG(960, 520, t("$TICK: the market's breath, every few seconds", "$TICK: ลมหายใจของตลาด ทุกไม่กี่วินาที"),
            t("$TICK = NYSE stocks on an uptick − stocks on a downtick. Extremes show broad, urgent buying or selling.",
              "$TICK = จำนวนหุ้น NYSE ที่ขึ้นใน Tick ล่าสุด − ที่ลงใน Tick ล่าสุด ค่าสุดขั้วแสดงการซื้อหรือขายที่กว้างและเร่งรีบ"))
    rnd = random.Random(12)
    n = 78
    price, ticks, p = [], [], 5000.0
    for i in range(n):
        if i < 30:
            drift, base = -1.2, -350
        elif i < 34:
            drift, base = -0.5, -900
        else:
            drift, base = 2.0, 380
        tk = base + rnd.gauss(0, 330)
        if i in (31, 32):
            tk = -1180 + rnd.gauss(0, 60)
        p += drift + rnd.gauss(0, 2.2)
        price.append(p)
        ticks.append(tk)
    panel(s, 28, 90, 620, 410)
    P = Plot(s, 60, 110, 570, 160, n - 1, min(price) - 3, max(price) + 3)
    P.path(list(enumerate(price)), C["text"], 2.2)
    s.text(60, 106, t("index (5-minute)", "ดัชนี (5 นาที)"), 11, C["muted"], weight=700)
    Q = Plot(s, 60, 300, 570, 170, n - 1, -1500, 1500)
    for v, col in ((1000, C["bull"]), (-1000, C["bear"]), (0, C["dim"])):
        s.line(60, Q.Y(v), 630, Q.Y(v), col, 1.2, "5 4" if v else None)
        s.text(56, Q.Y(v) + 4, f"{v:+d}" if v else "0", 11, col, "end")
    for i, v in enumerate(ticks):
        col = C["bull"] if v > 0 else C["bear"]
        s.line(Q.X(i), Q.Y(0), Q.X(i), Q.Y(max(min(v, 1500), -1500)), col, 4, opacity=0.8)
    s.text(Q.X(31), Q.Y(-1300) + 4, t("−1,000 extreme at the low", "−1,000 สุดขั้วที่จุดต่ำ"), 11, C["bear"], "middle", 700)
    s.text(60, 296, "$TICK", 11, C["muted"], weight=700)
    cards = [
        (C["blue"], "$TICK", t("Upticks − downticks now.\n±1,000 = extreme urgency.", "Uptick − Downtick ตอนนี้\n±1,000 = เร่งรีบสุดขั้ว")),
        (C["bull"], "$ADD", t("Advancing − declining issues.\nTrend day = one-sided all day.", "หุ้นขึ้น − หุ้นลง\nวันเทรนด์ = ด้านเดียวทั้งวัน")),
        (C["amber"], "$VOLD", t("Up volume − down volume.\nWhere the money is going.", "วอลุ่มขึ้น − วอลุ่มลง\nเงินกำลังไหลไปทางไหน")),
        (C["purple"], "VIX", t("30-day implied volatility.\nRising = fear, wider ranges.", "ความผันผวนแฝง 30 วัน\nเพิ่ม = กลัว กรอบกว้างขึ้น")),
    ]
    for k, (col, name, body) in enumerate(cards):
        s.card(668, 92 + k * 103, 264, 94, name, body, col, 15, 12)
    return s.render()


# ---------------------------------------------------------------- 9.5
@fig
def backtest(lang):
    t = tr(lang)
    r = res()
    s = SVG(960, 540, t(f"Backtest: SMA {r['fast']}/{r['slow']} trend filter vs buy & hold",
                        f"Backtest: ตัวกรองเทรนด์ SMA {r['fast']}/{r['slow']} เทียบกับซื้อแล้วถือ"),
            t("Synthetic daily data, next-bar execution, 0.10% cost per change. Parameters chosen on the shaded in-sample period only.",
              "ข้อมูลรายวันจำลอง ส่งคำสั่งแท่งถัดไป ต้นทุน 0.10% ต่อการเปลี่ยนสถานะ เลือกพารามิเตอร์จากช่วง In-sample ที่แรเงาเท่านั้น"))
    eq_s, eq_b = q.equity(r["rets"]), q.equity(r["bh"])
    n, cut = len(eq_s), r["cut"]
    panel(s, 28, 90, 904, 430)
    hi = max(max(eq_s), max(eq_b)) * 1.05
    P = Plot(s, 80, 115, 820, 260, n - 1, 0.5, hi)
    s.rect(P.X(0), 115, P.X(cut) - P.X(0), 380, fill=C["blue"], opacity=0.06)
    s.text(P.X(cut / 2), 130, t("IN-SAMPLE (optimised here)", "IN-SAMPLE (ปรับพารามิเตอร์ที่นี่)"), 12, C["blue"], "middle", 700)
    s.text(P.X((cut + n) / 2), 130, t("OUT-OF-SAMPLE", "OUT-OF-SAMPLE"), 12, C["bull"], "middle", 700)
    s.line(P.X(cut), 115, P.X(cut), 495, C["dim"], 1.2, "4 4")
    for v in (1, 2):
        if v < hi:
            s.line(80, P.Y(v), 900, P.Y(v), C["grid"], 1)
            s.text(74, P.Y(v) + 4, f"{v:.0f}×", 11, C["muted"], "end")
    step = 3
    P.path([(i, eq_b[i]) for i in range(0, n, step)], C["dim"], 1.8)
    P.path([(i, eq_s[i]) for i in range(0, n, step)], C["amber"], 2.4)
    s.text(P.X(n - 1) - 4, P.Y(eq_b[-1]) - 8, t(f"buy & hold {eq_b[-1]:.2f}×", f"ซื้อแล้วถือ {eq_b[-1]:.2f}×"), 12, C["muted"], "end", 700)
    s.text(P.X(n - 1) - 4, P.Y(eq_s[-1]) + 18, t(f"strategy {eq_s[-1]:.2f}×", f"กลยุทธ์ {eq_s[-1]:.2f}×"), 12, C["amber"], "end", 700)
    D = Plot(s, 80, 400, 820, 90, n - 1, -0.35, 0)
    for eq, col in ((eq_b, C["dim"]), (eq_s, C["bear"])):
        peak, dd = 0, []
        for i, v in enumerate(eq):
            peak = max(peak, v)
            dd.append((i, v / peak - 1))
        D.path(dd[::step], col, 1.5)
    s.text(74, 404, "0%", 11, C["muted"], "end")
    s.text(74, 490, "−35%", 11, C["muted"], "end")
    s.text(84, 396, t("drawdown", "Drawdown"), 11, C["muted"], weight=700)
    return s.render()


# ---------------------------------------------------------------- 9.6
@fig
def metrics_card(lang):
    t = tr(lang)
    r = res()
    s = SVG(960, 520, t("Performance metrics from the backtest", "ตัวชี้วัดผลงานจาก Backtest"),
            t("Same run as Lesson 9.5. Compare strategy vs buy & hold, in-sample vs out-of-sample.",
              "ผลรันเดียวกับบท 9.5 เทียบกลยุทธ์กับซื้อแล้วถือ ทั้ง In-sample และ Out-of-sample"))
    cols = [(t("Strategy IS", "กลยุทธ์ IS"), r["ins"], C["blue"]), (t("Buy&hold IS", "ซื้อถือ IS"), r["bh_ins"], C["dim"]),
            (t("Strategy OOS", "กลยุทธ์ OOS"), r["oos"], C["amber"]), (t("Buy&hold OOS", "ซื้อถือ OOS"), r["bh_oos"], C["dim"])]
    rows = [
        ("CAGR", "cagr", "{:+.1%}", t("compound annual growth", "การเติบโตทบต้นต่อปี")),
        (t("Volatility", "ความผันผวน"), "vol", "{:.1%}", t("annualised σ of daily returns", "σ รายวันแปลงเป็นรายปี")),
        ("Sharpe", "sharpe", "{:.2f}", t("mean ÷ σ × √252", "ค่าเฉลี่ย ÷ σ × √252")),
        ("Sortino", "sortino", "{:.2f}", t("mean ÷ downside σ × √252", "ค่าเฉลี่ย ÷ σ ขาลง × √252")),
        (t("Max drawdown", "Drawdown สูงสุด"), "max_dd", "−{:.1%}", t("worst peak-to-trough", "จากยอดถึงก้นที่แย่ที่สุด")),
        (t("Trades", "จำนวนเทรด"), "trades", "{}", t("round trips", "เข้า-ออกครบรอบ")),
        (t("Win rate", "อัตราชนะ"), "win_rate", "{:.0%}", ""),
        (t("Profit factor", "Profit Factor"), "profit_factor", "{:.2f}", t("gross wins ÷ gross losses", "กำไรรวม ÷ ขาดทุนรวม")),
    ]
    panel(s, 28, 90, 904, 410)
    xs = [270, 430, 590, 750]
    for (name, _, col), x in zip(cols, xs):
        s.text(x, 122, name, 13, col if col != C["dim"] else C["muted"], "middle", 700)
    for k, (name, key, f, note) in enumerate(rows):
        y = 158 + k * 40
        s.rect(40, y - 22, 880, 34, fill=C["panel"] if k % 2 else C["grid"], opacity=0.6, rx=6)
        s.text(56, y, name, 14, C["text"], weight=700)
        s.text(56, y + 12, note, 9, C["muted"])
        for (_, m, col), x in zip(cols, xs):
            v = m.get(key)
            txt = f.format(v) if v is not None else "—"
            s.text(x, y + 2, txt, 14, col if col != C["dim"] else C["text"], "middle", 600)
    s.text(48, 490, t("Profit factor > 11 from 8 and 3 trades is not an edge. It's a tiny sample. Out-of-sample, buy & hold had the higher Sharpe.",
                      "Profit Factor > 11 จาก 8 และ 3 เทรดไม่ใช่ความได้เปรียบ แต่เป็นกลุ่มตัวอย่างที่เล็กมาก ใน Out-of-sample การซื้อแล้วถือมี Sharpe สูงกว่า"),
           12, C["amber"], weight=600)
    return s.render()


# ---------------------------------------------------------------- 9.7
@fig
def summary(lang):
    t = tr(lang)
    s = SVG(960, 560, t("Phase 9 on one page", "สรุปเฟส 9 ในหน้าเดียว"))
    cx, cy = 480, 310
    nodes = [
        (170, 140, C["blue"], t("9.1 Statistics", "9.1 สถิติ"), t("Mean, σ, fat tails.\nSmall samples lie.", "ค่าเฉลี่ย σ หางอ้วน\nกลุ่มตัวอย่างเล็กโกหก")),
        (790, 140, C["amber"], t("9.2 Probability & EV", "9.2 ความน่าจะเป็น & EV"), t("Σ p × outcome.\nLuck averages out slowly.", "Σ p × ผลลัพธ์\nโชคเฉลี่ยออกอย่างช้า ๆ")),
        (150, 320, C["bear"], t("9.3 Backtesting", "9.3 Backtest"), t("No look-ahead, costs,\nout-of-sample, walk-forward.", "ไม่ดูอนาคต รวมต้นทุน\nOut-of-sample Walk-forward")),
        (810, 320, C["purple"], t("9.4 Internals", "9.4 Internals"), t("$TICK · $ADD · $VOLD · VIX.\nBreadth confirms price.", "$TICK · $ADD · $VOLD · VIX\nความกว้างยืนยันราคา")),
        (250, 480, C["teal"], t("9.5 Python strategy", "9.5 กลยุทธ์ Python"), t("Simple rules, honest test.\nIS winner can lose OOS.", "กฎง่าย ทดสอบอย่างซื่อตรง\nผู้ชนะ IS แพ้ OOS ได้")),
        (710, 480, C["bull"], t("9.6 Metrics", "9.6 ตัวชี้วัด"), t("Sharpe, Sortino, max DD,\nprofit factor, sample size.", "Sharpe, Sortino, Max DD\nProfit Factor, ขนาดตัวอย่าง")),
    ]
    for x, y, col, head, body in nodes:
        s.line(cx, cy, x, y, col, 2, opacity=0.5)
    s.circle(cx, cy, 74, C["panel"], C["text"], 2)
    s.text(cx, cy - 4, t("PHASE 9", "เฟส 9"), 20, C["text"], "middle", 700)
    s.text(cx, cy + 20, t("Quant", "ควอนต์"), 14, C["muted"], "middle")
    for x, y, col, head, body in nodes:
        s.rect(x - 130, y - 42, 260, 92, fill=C["panel"], stroke=col, rx=12)
        s.text(x, y - 14, head, 16, col, "middle", 700)
        s.text(x, y + 10, body, 13, C["text"], "middle")
    return s.render()


# ================================================================ v2 additions (Oct 2026)
from quant import ten_trades as tt


@fig
def ten_trades(lang):
    t = tr(lang)
    r = tt.EXAMPLE
    m = tt.metrics(r)
    s = SVG(960, 470, t("Ten trades, described by hand", "สิบไม้ อธิบายด้วยมือ"),
            t("Results in R: +2, −1, +0.5, −1, +3, −1, +1.5, −0.5, −1, +2.5", "ผลเป็น R: +2, −1, +0.5, −1, +3, −1, +1.5, −0.5, −1, +2.5"))
    panel(s, 28, 90, 540, 360, t("Histogram (how many trades per result)", "ฮิสโตแกรม (จำนวนไม้ต่อผลลัพธ์)"), C["text"], 14)
    bins = [-1.0, -0.5, 0.5, 1.5, 2.0, 2.5, 3.0]
    x0, base = 60, 400
    for i, b in enumerate(bins):
        c = sum(1 for x in r if x == b)
        x = x0 + i * 70
        s.rect(x, base - c * 60, 50, c * 60, fill=C["bear"] if b < 0 else C["bull"], opacity=0.85, rx=4)
        s.text(x + 25, base + 20, f"{b:+g}R", 12, C["muted"], "middle")
        s.text(x + 25, base - c * 60 - 8, str(c), 13, C["text"], "middle", 700)
    stats = [(t("Mean (average)", "ค่าเฉลี่ย"), f"{m['mean']:+.2f}R", C["amber"]), (t("Median (middle)", "มัธยฐาน (ตรงกลาง)"), f"{m['median']:+.2f}R", C["teal"]),
             (t("Standard deviation", "ส่วนเบี่ยงเบนมาตรฐาน"), f"{m['sd']:.2f}R", C["blue"]), (t("Win rate", "อัตราชนะ"), f"{m['win_rate']:.0%}", C["text"]),
             (t("95% range of the mean", "ช่วง 95% ของค่าเฉลี่ย"), "−0.50R … +1.50R", C["bear"])]
    for k, (a, b, col) in enumerate(stats):
        y = 130 + k * 62
        s.text(600, y, a, 13, C["muted"], weight=600)
        s.text(600, y + 26, b, 20, col, weight=800)
    s.text(600, 440, t("Mean +0.5R but median 0: a few big winners\ncarry the result. 10 trades prove nothing yet.", "ค่าเฉลี่ย +0.5R แต่มัธยฐาน 0: ไม้ชนะใหญ่ไม่กี่ไม้\nแบกผลลัพธ์ไว้ 10 ไม้ยังพิสูจน์อะไรไม่ได้"), 12, C["muted"])
    return s.render()


@fig
def coin_dice(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Expected value before trading: a coin, a die, then a trade", "ค่าคาดหวังก่อนเทรด: เหรียญ ลูกเต๋า แล้วจึงเป็นไม้เทรด"),
            t("EV = Σ probability × result. Only the average over many repetitions matters.", "EV = Σ ความน่าจะเป็น × ผลลัพธ์ มีแค่ค่าเฉลี่ยจากการทำซ้ำหลายครั้งที่สำคัญ"))
    games = [(C["bull"], t("Coin game", "เกมโยนเหรียญ"), t("Heads: +2\nTails: −1", "หัว: +2\nก้อย: −1"), "0.5 × 2 − 0.5 × 1", "+0.50", t("good bet", "เดิมพันที่ดี")),
             (C["muted"], t("Dice game", "เกมลูกเต๋า"), t("Six: +5\nAnything else: −1", "ออกหก: +5\nอย่างอื่น: −1"), "1/6 × 5 − 5/6 × 1", "0.00", t("pointless", "ไม่มีประโยชน์")),
             (C["blue"], t("Trade, no costs", "ไม้เทรด ไม่มีต้นทุน"), t("Win 45%: +2R\nLose 55%: −1R", "ชนะ 45%: +2R\nแพ้ 55%: −1R"), "0.45 × 2 − 0.55 × 1", "+0.35R", t("good bet", "เดิมพันที่ดี")),
             (C["amber"], t("Same trade, 10-pip stop", "ไม้เดิม Stop 10 pip"), t("Costs 1.9 pips\n= 0.19R per trade", "ต้นทุน 1.9 pip\n= 0.19R ต่อไม้"), "0.35 − 0.19", "+0.16R", t("costs ate half", "ต้นทุนกินไปครึ่ง"))]
    for k, (col, head, rule, calc, ev, verdict) in enumerate(games):
        x = 28 + k * 230
        s.rect(x, 96, 216, 320, fill=C["panel"], stroke=col, rx=12)
        s.text(x + 108, 128, head, 15, col, "middle", 700)
        s.text(x + 108, 168, rule, 14, C["text"], "middle")
        s.text(x + 108, 250, calc, 12, C["muted"], "middle")
        s.text(x + 108, 310, "EV = " + ev, 22, col, "middle", 800)
        s.text(x + 108, 350, verdict, 13, C["text"], "middle", 600)
    return s.render()


@fig
def five_biases(lang):
    t = tr(lang)
    s = SVG(960, 520, t("Five ways a backtest lies, as tiny stories", "ห้าวิธีที่ Backtest โกหก เล่าเป็นเรื่องสั้น"),
            t("Each one makes the past look better than the future will be.", "แต่ละแบบทำให้อดีตดูดีกว่าอนาคตที่จะเป็น"))
    items = [(C["bear"], t("Look-ahead", "Look-ahead"), t("Buys at the open using that day's close.\nKnew the future → impossible in real life.", "ซื้อตอนเปิดโดยใช้ราคาปิดของวันนั้น\nรู้อนาคต → ทำจริงไม่ได้")),
             (C["amber"], t("Survivorship", "Survivorship"), t("Tests today's index members only.\nThe companies that went bust are missing.", "ทดสอบเฉพาะหุ้นที่อยู่ในดัชนีวันนี้\nบริษัทที่เจ๊งไปแล้วหายไปจากข้อมูล")),
             (C["purple"], t("Overfitting", "Overfitting"), t("Tunes 6 settings until the past is perfect.\nFits the noise; fails on new data.", "ปรับ 6 ค่าจนอดีตสมบูรณ์แบบ\nจับคู่กับสัญญาณรบกวน พังกับข้อมูลใหม่")),
             (C["blue"], t("Data snooping", "Data snooping"), t("Tries 200 ideas, shows the best one.\nBy luck alone, some will look great.", "ลอง 200 ไอเดีย โชว์ตัวที่ดีที่สุด\nแค่โชคก็ทำให้บางตัวดูดีมากแล้ว")),
             (C["teal"], t("Ignoring costs", "ไม่คิดต้นทุน"), t("200 trades a year, no spread or commission.\n+20% on paper becomes −5% for real.", "เทรด 200 ไม้ต่อปี ไม่คิด Spread หรือค่าคอม\n+20% บนกระดาษกลายเป็น −5% ในของจริง"))]
    for k, (col, head, story) in enumerate(items):
        y = 96 + k * 82
        s.rect(28, y, 904, 72, fill=C["panel"], stroke=C["border"], rx=10)
        s.rect(28, y, 6, 72, fill=col, rx=2)
        s.text(52, y + 42, head, 17, col, weight=700)
        s.text(300, y + 30, story, 13, C["text"])
    return s.render()


@fig
def tick_extremes(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Reading $TICK extremes at a level (illustrative)", "อ่านค่าสุดขั้วของ $TICK ที่ระดับราคา (ภาพประกอบ)"),
            t("ES at a marked support of 5,000. $TICK shown below price; ±1,000 = extreme.", "ES ที่แนวรับ 5,000 ที่ทำเครื่องหมายไว้ $TICK แสดงใต้ราคา ±1,000 = สุดขั้ว"))
    px = [5012, 5008, 5004, 5001, 4999.5, 5000.5, 5000, 5003, 5006, 5011, 5015, 5013, 5018]
    tk = [200, -300, -650, -900, -1150, -600, -350, 300, 650, 900, 1050, 400, 700]
    n = len(px)
    P = Plot(s, 80, 110, 820, 180, n - 1, 4996, 5020)
    T = Plot(s, 80, 320, 820, 140, n - 1, -1300, 1300)
    s.line(80, P.Y(5000), 900, P.Y(5000), C["amber"], 1.5, "5 4")
    s.text(905, P.Y(5000) + 4, "5,000", 12, C["amber"])
    P.path(list(enumerate(px)), C["text"], 2.5)
    for v, col in ((1000, C["bull"]), (-1000, C["bear"]), (0, C["dim"])):
        s.line(80, T.Y(v), 900, T.Y(v), col, 1.2, "4 4" if v else None)
        s.text(70, T.Y(v) + 4, f"{v:+,}" if v else "0", 11, col, "end")
    for i, v in enumerate(tk):
        s.rect(T.X(i) - 10, min(T.Y(v), T.Y(0)), 20, abs(T.Y(v) - T.Y(0)), fill=C["bull"] if v > 0 else C["bear"], opacity=0.8, rx=2)
    for num, i, txt in ((1, 4, t("−1,150 at 5,000, low holds", "−1,150 ที่ 5,000 จุดต่ำยืนได้")), (2, 6, t("weaker selling: −350", "แรงขายอ่อนลง: −350")),
                        (3, 9, t("CHoCH up, +900", "CHoCH ขึ้น +900")), (4, 10, t("+1,050 with the trend: not a short", "+1,050 ตามเทรนด์: ไม่ใช่จุด Short"))):
        s.circle(P.X(i), P.Y(px[i]), 11, C["panel"], C["amber"], 2)
        s.text(P.X(i), P.Y(px[i]) + 5, str(num), 12, C["amber"], "middle", 700)
        s.text(P.X(i), P.Y(px[i]) + (30 if num in (1, 2) else -18), txt, 11, C["amber"], "middle", 600)
    return s.render()


@fig
def ten_equity(lang):
    t = tr(lang)
    m = tt.metrics(tt.EXAMPLE)
    s = SVG(960, 460, t("The same ten trades as an equity curve (in R)", "สิบไม้เดิมในรูปกราฟเงินทุน (เป็น R)"),
            t("Running total after each trade. Max drawdown = the biggest fall from a peak.", "ยอดสะสมหลังแต่ละไม้ Max drawdown = การลดลงจากจุดสูงสุดมากที่สุด"))
    curve = [0.0] + m["curve"]
    P = Plot(s, 90, 110, 560, 280, 10, -0.5, 5.5)
    for v in range(0, 6):
        s.line(90, P.Y(v), 650, P.Y(v), C["grid"], 1)
        s.text(80, P.Y(v) + 4, f"{v}R", 12, C["muted"], "end")
    for i in range(11):
        s.text(P.X(i), 410, str(i), 12, C["muted"], "middle")
    s.text(370, 432, t("trade number", "ไม้ที่"), 12, C["muted"], "middle")
    P.path(list(enumerate(curve)), C["blue"], 3)
    for i, v in enumerate(curve):
        s.circle(P.X(i), P.Y(v), 4, C["blue"])
    s.rect(P.X(1) - 6, P.Y(2.0), P.X(4) - P.X(1) + 12, P.Y(0.5) - P.Y(2.0), fill=C["bear"], opacity=0.14, stroke=C["bear"], rx=4)
    s.text(P.X(2.5), P.Y(0.5) + 22, t("−1.5R (peak 2 → 0.5)", "−1.5R (จุดสูง 2 → 0.5)"), 12, C["bear"], "middle", 700)
    rows = [(t("Profit factor", "Profit factor"), f"{m['profit_factor']:.2f}", t("9.5R won ÷ 4.5R lost", "ชนะ 9.5R ÷ แพ้ 4.5R")),
            (t("Max drawdown", "Max drawdown"), f"{m['max_dd']:.1f}R", t("= 1.5% of the account at 1% risk", "= 1.5% ของบัญชีที่เสี่ยง 1%")),
            (t("Sharpe-like (per trade)", "คล้าย Sharpe (ต่อไม้)"), f"{m['sharpe_per_trade']:.2f}", t("mean 0.5 ÷ SD 1.62", "ค่าเฉลี่ย 0.5 ÷ SD 1.62")),
            (t("Sortino-like (per trade)", "คล้าย Sortino (ต่อไม้)"), f"{m['sortino_per_trade']:.2f}", t("mean 0.5 ÷ downside 0.65", "ค่าเฉลี่ย 0.5 ÷ ด้านลบ 0.65"))]
    for k, (a, b, c) in enumerate(rows):
        y = 124 + k * 80
        s.text(690, y, a, 13, C["muted"], weight=600)
        s.text(690, y + 28, b, 22, C["text"], weight=800)
        s.text(690, y + 47, c, 11, C["muted"])
    return s.render()
