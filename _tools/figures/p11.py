"""Phase 11 figures: Capstone."""
from charts import SVG, C, tr
from figures.p2 import panel

FIGURES = {}


def fig(fn):
    FIGURES["p11-" + fn.__name__.replace("_", "-")] = fn
    return fn


@fig
def system_map(lang):
    t = tr(lang)
    s = SVG(960, 540, t("Your system: every phase has a job", "ระบบของคุณ: ทุกเฟสมีหน้าที่"),
            t("Foundation phases are required. Advanced tools are optional modules, kept only if your data says they help.",
              "เฟสพื้นฐานเป็นข้อบังคับ เครื่องมือขั้นสูงเป็นโมดูลเสริม เก็บไว้เฉพาะเมื่อข้อมูลของคุณบอกว่ามันช่วย"))
    rows = [
        (C["bull"], t("REQUIRED CORE", "แกนหลักที่ต้องมี"), [
            ("1–2", t("Read price\n& structure", "อ่านราคา\n& โครงสร้าง")),
            ("3", t("Risk &\nsizing", "ความเสี่ยง\n& ขนาดไม้")),
            ("4", t("Plan, routine,\njournal", "แผน กิจวัตร\nบันทึก")),
            ("9", t("Measure\nwhat works", "วัดว่า\nอะไรได้ผล")),
        ]),
        (C["blue"], t("OPTIONAL MODULES", "โมดูลเสริม"), [
            ("5", t("Liquidity\n& ICT", "สภาพคล่อง\n& ICT")),
            ("6", t("Fib, Elliott,\nσ", "ฟีโบ Elliott\nσ")),
            ("7", t("Orderflow\n& profile", "ออเดอร์โฟลว์\n& Profile")),
            ("8", t("Options\n& GEX", "ออปชัน\n& GEX")),
        ]),
        (C["amber"], t("CONTEXT & WEALTH", "บริบท & ความมั่งคั่ง"), [
            ("10", t("Macro\ncontext", "บริบท\nมหภาค")),
            ("10.7", t("Long-term\nportfolio", "พอร์ต\nระยะยาว")),
            ("11", t("Your written\nplan & policy", "แผน & นโยบาย\nที่เขียนไว้")),
        ]),
    ]
    for r, (col, head, items) in enumerate(rows):
        y = 100 + r * 140
        s.rect(28, y, 904, 124, fill=C["panel"], stroke=C["border"], rx=12)
        s.rect(28, y, 6, 124, fill=col, rx=3)
        s.text(50, y + 30, head, 15, col, weight=700)
        for k, (ph, name) in enumerate(items):
            x = 240 + k * 172
            s.rect(x, y + 16, 156, 92, fill=col, opacity=0.12, stroke=col, rx=10)
            s.text(x + 78, y + 42, t(f"Phase {ph}", f"เฟส {ph}"), 12, col, "middle", 700)
            s.text(x + 78, y + 66, name, 13, C["text"], "middle")
    s.text(48, 528, t("Rule: add one optional module at a time, and keep it only if it improves expectancy over 30+ trades (9.1–9.2).",
                      "กฎ: เพิ่มโมดูลเสริมทีละตัว และเก็บไว้เฉพาะถ้ามันเพิ่มค่าคาดหวังใน 30+ เทรด (9.1–9.2)"), 13, C["amber"], weight=600)
    return s.render()


@fig
def plan_sheet(lang):
    t = tr(lang)
    s = SVG(960, 560, t("Trading plan v1.0: one page, ten sections", "แผนการเทรด v1.0: หนึ่งหน้า สิบส่วน"),
            t("Fill it in, print it, read it before every session. Change it only at monthly reviews.",
              "กรอก พิมพ์ อ่านก่อนทุกเซสชัน เปลี่ยนเฉพาะตอนทบทวนรายเดือน"))
    secs = [
        (C["purple"], "1", t("Purpose & process goals", "จุดประสงค์ & เป้าหมายด้านกระบวนการ")),
        (C["blue"], "2", t("Markets, timeframes, hours", "ตลาด ไทม์เฟรม เวลา")),
        (C["teal"], "3", t("Bias rules (HTF, macro)", "กฎทิศทาง (HTF มหภาค)")),
        (C["bull"], "4", t("Setup A: entry checklist", "เซ็ตอัพ A: เช็กลิสต์เข้า")),
        (C["bull"], "5", t("Setup B (optional)", "เซ็ตอัพ B (ถ้ามี)")),
        (C["bear"], "6", t("Risk & sizing", "ความเสี่ยง & ขนาดไม้")),
        (C["amber"], "7", t("Exits & management", "การออก & การบริหาร")),
        (C["pink"], "8", t("Routine & no-trade rules", "กิจวัตร & กฎห้ามเทรด")),
        (C["muted"], "9", t("Circuit breakers", "เบรกเกอร์ตัดไฟ")),
        (C["purple"], "10", t("Journal & review", "บันทึก & ทบทวน")),
    ]
    for k, (col, n, name) in enumerate(secs):
        x = 28 + (k % 2) * 460
        y = 92 + (k // 2) * 90
        s.rect(x, y, 444, 78, fill=C["panel"], stroke=C["border"], rx=10)
        s.circle(x + 34, y + 39, 18, col)
        s.text(x + 34, y + 45, n, 15, C["white"], "middle", 700)
        s.text(x + 66, y + 34, name, 15, C["text"], weight=700)
        s.line(x + 66, y + 54, x + 420, y + 54, C["dim"], 1, "3 4")
    return s.render()


@fig
def ips_sheet(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Investment Policy Statement: your rules for the long game", "นโยบายการลงทุน: กฎของคุณสำหรับเกมระยะยาว"),
            t("Written when calm, followed when markets are not.", "เขียนตอนใจเย็น ทำตามตอนที่ตลาดไม่เย็น"))
    secs = [
        (C["purple"], t("Goals & horizon", "เป้าหมาย & ระยะเวลา"), t("What the money is for, and when", "เงินนี้มีไว้ทำอะไร และเมื่อไหร่")),
        (C["blue"], t("Risk tolerance", "ความทนต่อความเสี่ยง"), t("Max drawdown you'll hold through", "Drawdown สูงสุดที่คุณจะถือผ่านได้")),
        (C["bull"], t("Target allocation", "การจัดสรรเป้าหมาย"), t("Asset classes, % weights, ranges", "ประเภทสินทรัพย์ % น้ำหนัก ช่วงที่ยอมรับ")),
        (C["teal"], t("Instruments & costs", "เครื่องมือ & ต้นทุน"), t("Which funds, max yearly fee", "กองทุนไหน ค่าธรรมเนียมสูงสุดต่อปี")),
        (C["amber"], t("Contributions", "การเติมเงิน"), t("Amount, frequency, automation", "จำนวน ความถี่ ระบบอัตโนมัติ")),
        (C["pink"], t("Rebalancing rule", "กฎการปรับสมดุล"), t("Calendar and/or ±5% bands", "ตามปฏิทิน และ/หรือ เบี่ยง ±5%")),
        (C["bear"], t("Crisis plan", "แผนรับวิกฤต"), t("What you do in a −30% market", "สิ่งที่ทำเมื่อตลาด −30%")),
        (C["muted"], t("Review", "การทบทวน"), t("Yearly, or on life changes", "รายปี หรือเมื่อชีวิตเปลี่ยน")),
    ]
    for k, (col, head, body) in enumerate(secs):
        x = 28 + (k % 4) * 231
        y = 96 + (k // 4) * 196
        s.card(x, y, 219, 182, head, body, col, 15, 12)
    return s.render()


@fig
def progression(lang):
    t = tr(lang)
    s = SVG(960, 470, t("From learning to live trading: earn each step", "จากการเรียนสู่การเทรดจริง: ผ่านทีละขั้น"),
            t("Each stage has an exit gate. Fail the gate → stay or step back. Money follows proof.",
              "แต่ละขั้นมีประตูผ่าน ไม่ผ่าน → อยู่ต่อหรือถอยกลับ เงินตามหลักฐาน"))
    stages = [
        (C["blue"], t("1 · Study & backtest", "1 · เรียน & Backtest"), t("50+ manual backtest\ntrades, written rules", "Backtest แมนนวล 50+ เทรด\nกฎที่เขียนไว้"), t("Gate: positive EV\non 50+ trades", "ประตู: EV บวก\nใน 50+ เทรด")),
        (C["teal"], t("2 · Paper / demo", "2 · กระดาษ / บัญชีทดลอง"), t("30+ live-market trades,\nfull routine & journal", "เทรดในตลาดจริง 30+ เทรด\nครบกิจวัตรและบันทึก"), t("Gate: ≥ 90% A/B grade,\nEV still positive", "ประตู: เกรด A/B ≥ 90%\nEV ยังบวก")),
        (C["amber"], t("3 · Micro live", "3 · เงินจริงไม้เล็ก"), t("0.25% risk, real money,\n50+ trades", "เสี่ยง 0.25% เงินจริง\n50+ เทรด"), t("Gate: rules followed\nunder real emotion", "ประตู: ทำตามกฎได้\nภายใต้อารมณ์จริง")),
        (C["bull"], t("4 · Normal size", "4 · ขนาดปกติ"), t("0.5–1% risk,\nmonthly reviews", "เสี่ยง 0.5–1%\nทบทวนรายเดือน"), t("Gate: 100+ trades,\nwithin drawdown rules", "ประตู: 100+ เทรด\nอยู่ในกฎ Drawdown")),
    ]
    for k, (col, head, body, gate) in enumerate(stages):
        x = 28 + k * 231
        s.rect(x, 100, 219, 330, fill=C["panel"], stroke=col, rx=12)
        s.rect(x, 100, 219, 46, fill=col, opacity=0.18, rx=12)
        s.text(x + 110, 129, head, 14, col, "middle", 700)
        s.text(x + 18, 180, body, 13, C["text"])
        s.rect(x + 12, 330, 195, 84, fill=col, opacity=0.12, rx=10)
        s.text(x + 24, 360, gate, 13, col, weight=700)
        if k < 3:
            s.arrow(x + 221, 265, x + 229, 265, C["muted"], 2)
    s.text(48, 458, t("Back to the previous stage if: −10% drawdown, broken circuit breakers, or EV turns negative over 50 trades.",
                      "ถอยกลับขั้นก่อนหน้าถ้า: Drawdown −10% ผิดกฎเบรกเกอร์ หรือ EV ติดลบใน 50 เทรด"), 13, C["bear"], weight=600)
    return s.render()


@fig
def cadence(lang):
    t = tr(lang)
    s = SVG(960, 470, t("The learning loop: a rhythm for years", "วงจรการเรียนรู้: จังหวะที่ใช้ได้หลายปี"),
            t("Small, regular reviews beat occasional big overhauls.", "การทบทวนเล็ก ๆ อย่างสม่ำเสมอชนะการรื้อใหญ่นาน ๆ ครั้ง"))
    rows = [
        (C["blue"], t("Daily", "รายวัน"), t("Routine, journal every trade, grade A/B/C (4.4–4.5)", "กิจวัตร บันทึกทุกเทรด ให้เกรด A/B/C (4.4–4.5)"), t("15–45 min", "15–45 นาที")),
        (C["teal"], t("Weekly", "รายสัปดาห์"), t("R, % A-grade, top mistake tag, one change (4.5)", "R, % เกรด A, แท็กความผิดพลาดอันดับหนึ่ง, หนึ่งการเปลี่ยน (4.5)"), t("30 min", "30 นาที")),
        (C["amber"], t("Monthly", "รายเดือน"), t("Expectancy per setup, drawdown vs rules, plan v-update (9.6)", "ค่าคาดหวังต่อเซ็ตอัพ Drawdown เทียบกฎ อัปเดตเวอร์ชันแผน (9.6)"), t("1–2 h", "1–2 ชม.")),
        (C["purple"], t("Quarterly", "รายไตรมาส"), t("Study one new topic; test it as an optional module", "ศึกษาหัวข้อใหม่หนึ่งเรื่อง ทดสอบเป็นโมดูลเสริม"), t("half day", "ครึ่งวัน")),
        (C["bull"], t("Yearly", "รายปี"), t("Full audit: trading results, IPS review, rebalance, goals", "ตรวจสอบทั้งหมด: ผลการเทรด ทบทวนนโยบายการลงทุน ปรับสมดุล เป้าหมาย"), t("1 day", "1 วัน")),
    ]
    for k, (col, when, what, time) in enumerate(rows):
        y = 96 + k * 72
        s.rect(28, y, 904, 60, fill=C["panel"], stroke=C["border"], rx=10)
        s.rect(28, y, 6, 60, fill=col, rx=3)
        s.text(52, y + 37, when, 16, col, weight=700)
        s.text(200, y + 37, what, 14, C["text"])
        s.text(912, y + 37, time, 13, C["muted"], "end", 700)
    return s.render()


# ---------------------------------------------------------------- v2 additions (B9e)
import math


def _panel(s, x, y, w, h):
    s.rect(x, y, w, h, fill=C["panel"], stroke=C["border"], rx=12)


@fig
def expectancy_ci(lang):
    t = tr(lang)
    s = SVG(960, 460, t("How sure can you be after N trades?", "หลัง N ไม้ คุณมั่นใจได้แค่ไหน?"),
            t("A system with true expectancy +0.35R (45% wins at +2R). Bars: the range where a measured result usually lands (95%).",
              "ระบบที่ค่าคาดหวังจริง +0.35R (ชนะ 45% ที่ +2R) แท่ง: ช่วงที่ผลที่วัดได้มักตกอยู่ (95%)"))
    sd = math.sqrt(0.45 * 4 + 0.55 * 1 - 0.35 ** 2)
    ns = [30, 50, 100, 200, 400]
    x0, y0, w, h = 120, 110, 560, 280
    _panel(s, x0 - 70, y0 - 20, w + 100, h + 70)
    lo, hi = -0.4, 1.0
    Y = lambda v: y0 + h * (hi - v) / (hi - lo)
    for v in (-0.2, 0, 0.2, 0.4, 0.6, 0.8):
        s.line(x0, Y(v), x0 + w, Y(v), C["dim"] if v == 0 else C["grid"], 1.5 if v == 0 else 1)
        s.text(x0 - 10, Y(v) + 4, f"{v:+.1f}R", 12, C["muted"], "end")
    s.line(x0, Y(0.35), x0 + w, Y(0.35), C["amber"], 1.5, "6 4")
    s.text(x0 + 4, Y(0.35) - 8, t("true +0.35R", "ค่าจริง +0.35R"), 12, C["amber"], "start", 700)
    for k, n in enumerate(ns):
        x = x0 + 140 + k * 100
        m = 1.96 * sd / math.sqrt(n)
        col = C["bear"] if 0.35 - m < 0 else C["bull"]
        s.rect(x - 16, Y(0.35 + m), 32, Y(0.35 - m) - Y(0.35 + m), fill=col, opacity=0.35, rx=4)
        s.text(x, Y(0.35 + m) - 8, f"±{m:.2f}", 13, col, "middle", 700)
        s.text(x, y0 + h + 24, t(f"{n} trades", f"{n} ไม้"), 13, C["text"], "middle", 700)
    s.card(720, 90, 210, 350, t("What it means", "หมายความว่า"),
           t("After 30–50 trades\na real +0.35R edge can\nstill measure near 0\n(or look like +0.8R).\n \nAfter 200+ trades the\nrange is much tighter.\n \nTreat early numbers\nas provisional and\nkeep the stages.",
             "หลัง 30–50 ไม้\nความได้เปรียบจริง +0.35R\nอาจวัดได้ใกล้ 0\n(หรือดูเหมือน +0.8R)\n \nหลัง 200 ไม้ขึ้นไป\nช่วงจะแคบลงมาก\n \nถือตัวเลขช่วงแรก\nเป็นผลชั่วคราว และ\nทำตามขั้นตอนต่อ"),
           C["amber"], 16, 13)
    return s.render()


@fig
def crash_rebalance(lang):
    t = tr(lang)
    s = SVG(960, 480, t("The sample IPS in a crash: what the rule makes you do", "IPS ตัวอย่างในตลาดถล่ม: กฎทำให้คุณทำอะไร"),
            t("1,000,000 THB at targets. Equities −30%, bonds +3%, gold +10%, cash 0% (illustrative). Then rebalance to targets.",
              "1,000,000 บาทตามเป้า หุ้น −30% พันธบัตร +3% ทอง +10% เงินสด 0% (ตัวอย่าง) แล้วปรับสมดุลกลับเป้า"))
    assets = [(t("Global equity", "หุ้นโลก"), 50, -0.30, C["blue"]), (t("Thai equity", "หุ้นไทย"), 15, -0.30, C["teal"]),
              (t("Bonds", "พันธบัตร"), 25, 0.03, C["amber"]), (t("Gold", "ทองคำ"), 5, 0.10, C["pink"]), (t("Cash", "เงินสด"), 5, 0.0, C["muted"])]
    tot = 1_000_000
    vals = [tot * w / 100 * (1 + r) for _, w, r, _ in assets]
    T = sum(vals)
    s.text(60, 112, t("asset", "สินทรัพย์"), 13, C["muted"], weight=600)
    for x, h in ((300, t("target", "เป้า")), (420, t("after crash", "หลังถล่ม")), (560, t("weight now", "น้ำหนักตอนนี้")), (730, t("rebalance trade", "การปรับสมดุล"))):
        s.text(x, 112, h, 13, C["muted"], "middle", 600)
    for k, ((name, w, r, col), v) in enumerate(zip(assets, vals)):
        y = 150 + k * 52
        s.rect(40, y - 26, 880, 44, fill=C["panel"], stroke=C["border"], rx=8)
        s.text(60, y + 2, name, 15, col, weight=700)
        s.text(300, y + 2, f"{w}%", 14, C["text"], "middle")
        s.text(420, y + 2, f"{v:,.0f}", 14, C["text"], "middle")
        now = v / T * 100
        out = abs(now - w) > 5
        s.text(560, y + 2, f"{now:.1f}%" + (t("  out of band", "  หลุดกรอบ") if out else ""), 14, C["bear"] if out else C["text"], "middle", 700 if out else 400)
        trade = T * w / 100 - v
        s.text(730, y + 2, (t("buy ", "ซื้อ ") if trade > 0 else t("sell ", "ขาย ")) + f"{abs(trade):,.0f}", 14, C["bull"] if trade > 0 else C["amber"], "middle", 700)
    s.text(60, 430, t(f"Portfolio: 1,000,000 → {T:,.0f} THB ({(T / tot - 1) * 100:.2f}%). The rule buys equities after the fall, when feelings say sell.",
                      f"พอร์ต: 1,000,000 → {T:,.0f} บาท ({(T / tot - 1) * 100:.2f}%) กฎให้ซื้อหุ้นหลังร่วง ตอนที่ความรู้สึกบอกให้ขาย"), 13, C["amber"], weight=600)
    return s.render()


@fig
def change_test(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Is the new filter really better? Check the ranges", "ตัวกรองใหม่ดีกว่าจริงไหม? ดูช่วงของค่า"),
            t("Lesson 11.3's test: +0.42R with the filter vs +0.22R without. Assumed spread of results: 1.5R per trade. 95% ranges.",
              "การทดสอบในบทที่ 11.3: +0.42R เมื่อใช้ตัวกรอง vs +0.22R เมื่อไม่ใช้ สมมติการกระจายของผล 1.5R ต่อไม้ ช่วง 95%"))
    x0, w = 200, 560
    lo, hi = -0.3, 1.0
    X = lambda v: x0 + w * (v - lo) / (hi - lo)
    for v in (-0.2, 0, 0.2, 0.4, 0.6, 0.8, 1.0):
        s.line(X(v), 110, X(v), 360, C["dim"] if v == 0 else C["grid"], 1.5 if v == 0 else 1)
        s.text(X(v), 380, f"{v:+.1f}R", 12, C["muted"], "middle")
    rows = [(40, t("40 trades each", "อย่างละ 40 ไม้")), (160, t("160 trades each", "อย่างละ 160 ไม้"))]
    for k, (n, lab) in enumerate(rows):
        m = 1.96 * 1.5 / math.sqrt(n)
        yb = 130 + k * 120
        s.text(40, yb + 30, lab, 15, C["text"], weight=700)
        s.text(40, yb + 50, f"±{m:.2f}R", 13, C["muted"])
        for j, (mean, col, nm) in enumerate(((0.42, C["bull"], t("with filter", "ใช้ตัวกรอง")), (0.22, C["blue"], t("without", "ไม่ใช้")))):
            y = yb + 14 + j * 40
            s.line(X(mean - m), y, X(mean + m), y, col, 6)
            s.circle(X(mean), y, 7, col)
            s.text(X(mean + m) + 10, y + 5, f"{nm} {mean:+.2f}R", 13, col, weight=700)
    s.text(40, 415, t("The ranges overlap at 40 trades and still at 160: keep the filter as 'promising', keep logging, and don't call it proven yet.",
                      "ช่วงซ้อนกันที่ 40 ไม้ และยังซ้อนที่ 160 ไม้: ถือตัวกรองว่า 'มีแวว' บันทึกต่อไป และอย่าเพิ่งเรียกว่าพิสูจน์แล้ว"), 13, C["amber"], weight=600)
    return s.render()
