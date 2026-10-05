"""Phase 4 figures: Psychology & Execution."""
import math
from charts import SVG, C, tr

FIGURES = {}


def fig(fn):
    FIGURES["p4-" + fn.__name__.replace("_", "-")] = fn
    return fn


def panel(s, x, y, w, h, title=None, color=C["text"], size=16):
    s.rect(x, y, w, h, fill=C["panel"], stroke=C["border"], rx=12)
    if title:
        s.text(x + 18, y + 30, title, size, color, weight=700)


def smooth(keys, steps=12):
    """Cosine-interpolate between (x, y) key points."""
    pts = []
    for (x0, y0), (x1, y1) in zip(keys, keys[1:]):
        for k in range(steps):
            u = k / steps
            v = (1 - math.cos(math.pi * u)) / 2
            pts.append((x0 + (x1 - x0) * u, y0 + (y1 - y0) * v))
    pts.append(keys[-1])
    return pts


# ---------------------------------------------------------------- 4.1
@fig
def emotion_cycle(lang):
    t = tr(lang)
    s = SVG(960, 560, t("The cycle of market emotions", "วัฏจักรอารมณ์ของตลาด"),
            t("Feelings peak exactly when they are most expensive to act on.",
              "อารมณ์พุ่งสูงสุดตรงจุดที่การทำตามมันแพงที่สุด"))
    panel(s, 28, 90, 904, 450)
    keys = [(60, 400), (150, 340), (240, 270), (320, 200), (400, 150), (470, 210), (520, 250), (570, 300),
            (630, 360), (690, 420), (740, 455), (790, 440), (840, 400), (880, 360), (915, 330)]
    pts = smooth(keys)
    s.polyline(pts, C["text"], 3)
    lab = [
        (0, t("Optimism", "มองโลกแง่ดี"), C["bull"], -16, "middle"),
        (1, t("Excitement", "ตื่นเต้น"), C["bull"], -16, "end"),
        (2, t("Thrill", "ฮึกเหิม"), C["bull"], -16, "end"),
        (3, t("Greed", "โลภ"), C["amber"], -16, "end"),
        (4, t("EUPHORIA", "ยินดีสุดขีด"), C["amber"], -4, "start"),
        (5, t("Anxiety", "กังวล"), C["amber"], -12, "start"),
        (6, t("Denial", "ปฏิเสธความจริง"), C["amber"], -12, "start"),
        (7, t("Fear", "กลัว"), C["bear"], -12, "start"),
        (8, t("Desperation", "สิ้นหวัง"), C["bear"], -12, "start"),
        (9, t("Panic", "ตื่นตระหนก"), C["bear"], -12, "start"),
        (10, t("CAPITULATION", "ยอมแพ้"), C["bear"], 30, "middle"),
        (11, t("Despondency", "หดหู่"), C["purple"], 26, "start"),
        (12, t("Hope", "ความหวัง"), C["blue"], 26, "start"),
        (13, t("Relief", "โล่งใจ"), C["blue"], 26, "start"),
    ]
    for k, name, col, dy, anc in lab:
        x, y = keys[k]
        s.circle(x, y, 5, col)
        dx = -8 if anc == "end" else (8 if anc == "start" else 0)
        s.text(x + dx, y + dy, name, 13, col, anc, 700)
    x, y = keys[4]
    s.pill(x, y - 36, t("Max financial risk: everyone wants to buy", "ความเสี่ยงสูงสุด: ทุกคนอยากซื้อ"), C["bear"], 12)
    x, y = keys[10]
    s.pill(x - 180, y + 45, t("Max opportunity: everyone wants out", "โอกาสสูงสุด: ทุกคนอยากออก"), C["bull"], 12)
    s.text(60, 528, t("Your own P&L goes through the same cycle on every trade. The feeling is data about you, not about the market.",
                      "กำไรขาดทุนของคุณเองก็วิ่งผ่านวัฏจักรนี้ทุกเทรด ความรู้สึกคือข้อมูลเกี่ยวกับตัวคุณ ไม่ใช่เกี่ยวกับตลาด"), 13, C["muted"])
    return s.render()


@fig
def four_emotions(lang):
    t = tr(lang)
    s = SVG(960, 520, t("The four emotions that move your mouse", "อารมณ์ 4 อย่างที่ขยับเมาส์ของคุณ"),
            t("Name it, notice what it wants you to do, then do what the plan says instead.",
              "เรียกชื่อมัน สังเกตว่ามันอยากให้คุณทำอะไร แล้วทำตามแผนแทน"))
    cells = [
        (C["bear"], t("FEAR", "กลัว"), t("\"What if it goes against me?\"", "\"ถ้ามันสวนทางล่ะ?\""),
         t("Skip valid setups · exit winners early\n· move stop to break-even too soon", "ข้ามเซ็ตอัพที่ถูกต้อง · ปิดไม้กำไรเร็ว\n· ย้าย Stop ไปเท่าทุนเร็วเกินไป"),
         t("Risk small enough that a loss is boring.", "เสี่ยงน้อยพอที่การแพ้จะน่าเบื่อ")),
        (C["amber"], t("GREED", "โลภ"), t("\"This could be huge. Add more.\"", "\"ไม้นี้อาจใหญ่มาก เพิ่มอีก\""),
         t("Oversize · chase entries · remove\nthe target · overtrade", "ไม้ใหญ่เกิน · ไล่ราคา · ลบเป้าหมาย\n· เทรดถี่เกินไป"),
         t("Fixed risk per trade. Targets set before entry.", "ความเสี่ยงต่อไม้คงที่ ตั้งเป้าก่อนเข้า")),
        (C["blue"], t("HOPE", "หวัง"), t("\"It will come back.\"", "\"เดี๋ยวมันก็กลับมา\""),
         t("Hold losers · widen stops · average\ndown into a losing trade", "ถือไม้ขาดทุน · ขยาย Stop · ถัวเฉลี่ย\nขาลงในไม้ที่แพ้"),
         t("Hard stop in the market the moment you enter.", "ตั้ง Stop จริงทันทีที่เข้าเทรด")),
        (C["purple"], t("REGRET", "เสียดาย"), t("\"I should have…\"", "\"รู้งี้…\""),
         t("Revenge trades · chase the move\nyou missed · break rules to make it back", "เทรดแก้แค้น · ไล่ราคาที่พลาดไป\n· ผิดกฎเพื่อเอาคืน"),
         t("Missed trades cost 0R. Wait for the next one.", "เทรดที่พลาดเสีย 0R รอไม้ถัดไป")),
    ]
    for k, (col, name, voice, does, fix) in enumerate(cells):
        x = 28 + (k % 2) * 460
        y = 92 + (k // 2) * 210
        s.rect(x, y, 444, 196, fill=C["panel"], stroke=col, rx=12)
        s.text(x + 20, y + 34, name, 20, col, weight=700)
        s.text(x + 120, y + 34, voice, 14, C["muted"], italic=True)
        s.text(x + 20, y + 66, t("Makes you:", "ทำให้คุณ:"), 12, C["dim"], weight=700)
        s.text(x + 20, y + 88, does, 14, C["text"])
        s.rect(x + 14, y + 140, 416, 42, fill=col, opacity=0.12, rx=8)
        s.text(x + 26, y + 167, "→ " + fix, 14, col, weight=700)
    return s.render()


# ---------------------------------------------------------------- 4.2
@fig
def biases(lang):
    t = tr(lang)
    s = SVG(960, 560, t("Six biases that cost traders money", "อคติ 6 อย่างที่ทำให้นักเทรดเสียเงิน"),
            t("Everyone has them. The goal is not to remove them, but to build rules that catch them.",
              "ทุกคนมีอคติ เป้าหมายไม่ใช่ลบมันออก แต่สร้างกฎที่ดักจับมันไว้"))
    items = [
        (C["bear"], t("Loss aversion", "เกลียดการขาดทุน"), t("A loss hurts ~2× more than an\nequal gain feels good.", "ขาดทุนเจ็บประมาณ 2 เท่า\nของความสุขจากกำไรเท่ากัน"),
         t("Fix: think in R, accept −1R in advance", "แก้: คิดเป็น R ยอมรับ −1R ล่วงหน้า")),
        (C["amber"], t("Confirmation bias", "อคติยืนยันความเชื่อ"), t("You see only the evidence that\nagrees with your position.", "เห็นแต่หลักฐานที่\nเข้าข้างสถานะของตัวเอง"),
         t("Fix: write what would prove you wrong", "แก้: เขียนว่าอะไรจะพิสูจน์ว่าคุณผิด")),
        (C["blue"], t("Recency bias", "อคติเหตุการณ์ล่าสุด"), t("The last 3 trades feel like\nthe whole truth.", "3 เทรดล่าสุดรู้สึกเหมือน\nความจริงทั้งหมด"),
         t("Fix: judge on 100+ trades (3.4)", "แก้: ตัดสินจาก 100+ ไม้ (3.4)")),
        (C["purple"], t("Overconfidence", "มั่นใจเกินไป"), t("After a win streak, you size up\nand loosen the rules.", "หลังชนะติดกัน\nเพิ่มไม้และหย่อนกฎ"),
         t("Fix: risk is fixed, never 'earned'", "แก้: ความเสี่ยงคงที่ ไม่ได้ 'ได้มา' จากการชนะ")),
        (C["teal"], t("Anchoring", "การยึดติดตัวเลข"), t("\"It was 120 last month, so 95\nis cheap.\"", "\"เดือนก่อน 120\nตอนนี้ 95 ถือว่าถูก\""),
         t("Fix: structure, not old prices", "แก้: ดูโครงสร้าง ไม่ใช่ราคาเก่า")),
        (C["pink"], t("Sunk cost / disposition", "ต้นทุนจม / Disposition"), t("Sell winners fast, hold losers\nbecause 'I've lost too much to sell'.",
                                                                                   "ขายไม้กำไรเร็ว ถือไม้ขาดทุน\nเพราะ 'ขาดทุนมากเกินจะขายแล้ว'"),
         t("Fix: stop and target set before entry", "แก้: ตั้ง Stop และเป้าก่อนเข้า")),
    ]
    for k, (col, name, body, fix) in enumerate(items):
        x = 28 + (k % 3) * 308
        y = 92 + (k // 3) * 228
        s.rect(x, y, 290, 214, fill=C["panel"], stroke=C["border"], rx=12)
        s.rect(x, y, 290, 6, fill=col, rx=3)
        s.text(x + 18, y + 40, name, 17, col, weight=700)
        s.text(x + 18, y + 74, body, 14, C["text"])
        s.text(x + 18, y + 170, fix, 13, col, weight=600)
    return s.render()


@fig
def disposition(lang):
    t = tr(lang)
    s = SVG(960, 480, t("How emotions turn a winning plan into a losing one", "อารมณ์เปลี่ยนแผนที่ชนะให้กลายเป็นแผนที่แพ้ได้อย่างไร"),
            t("Same setups, same entries. Only the exits changed: winners cut early, losers held \"until they come back\".",
              "เซ็ตอัพเดียวกัน จุดเข้าเดียวกัน ต่างแค่การออก: ตัดไม้กำไรเร็ว ถือไม้ขาดทุน \"จนกว่าจะกลับมา\""))
    specs = [
        (t("As planned", "ตามแผน"), C["bull"], 0.45, 2.0, 1.0),
        (t("As traded (fear + hope)", "ที่เทรดจริง (กลัว + หวัง)"), C["bear"], 0.55, 0.8, 1.6),
    ]
    for k, (head, col, wr, aw, al) in enumerate(specs):
        x = 28 + k * 460
        panel(s, x, 90, 444, 370, head, col, 18)
        base = 270
        sc = 50
        bx = x + 60
        s.line(x + 30, base, x + 420, base, C["dim"], 1)
        # avg win / avg loss bars
        s.rect(bx, base - aw * sc, 70, aw * sc, fill=C["bull"], rx=4, opacity=0.85)
        s.text(bx + 35, base - aw * sc - 8, f"+{aw}R", 15, C["bull"], "middle", 700)
        s.text(bx + 35, base + al * sc + 40 if False else 420 - 70, "", 1)
        s.rect(bx + 90, base, 70, al * sc, fill=C["bear"], rx=4, opacity=0.85)
        s.text(bx + 125, base + al * sc + 20, f"−{al}R", 15, C["bear"], "middle", 700)
        s.text(bx + 35, base + 20, t("avg win", "กำไรเฉลี่ย"), 12, C["muted"], "middle")
        s.text(bx + 125, base - 10, t("avg loss", "ขาดทุนเฉลี่ย"), 12, C["muted"], "middle")
        e = wr * aw - (1 - wr) * al
        s.text(x + 250, 170, t(f"Win rate {wr * 100:.0f}%", f"อัตราชนะ {wr * 100:.0f}%"), 16, C["text"], weight=700)
        s.text(x + 250, 200, f"{wr:.2f}×{aw} − {1 - wr:.2f}×{al}", 14, C["muted"])
        s.text(x + 250, 240, t("Expectancy", "ค่าคาดหวัง"), 14, C["muted"])
        s.text(x + 250, 276, f"{e:+.2f}R", 32, C["bull"] if e > 0 else C["bear"], weight=700)
        s.text(x + 30, 438, t("Higher win rate… and a losing system." if k else "Lower win rate, positive edge.",
                              "อัตราชนะสูงขึ้น… แต่ระบบขาดทุน" if k else "อัตราชนะต่ำกว่า แต่มีความได้เปรียบ"), 14,
               col, weight=700)
    return s.render()


# ---------------------------------------------------------------- 4.3
@fig
def plan_onepage(lang):
    t = tr(lang)
    s = SVG(960, 560, t("The one-page trading plan", "แผนการเทรดหนึ่งหน้า"),
            t("If it doesn't fit on one page, you won't follow it when it matters.",
              "ถ้าใส่ในหน้าเดียวไม่ได้ คุณจะไม่ทำตามมันในตอนที่สำคัญ"))
    items = [
        (C["purple"], t("1 · Why & goals", "1 · ทำไม & เป้าหมาย"), t("Process goals, not $ goals.\n\"Follow the plan on 95% of trades.\"", "เป้าหมายด้านกระบวนการ ไม่ใช่เงิน\n\"ทำตามแผน 95% ของเทรด\"")),
        (C["blue"], t("2 · Markets & timeframes", "2 · ตลาด & ไทม์เฟรม"), t("e.g. 3 markets · Daily / 4H / 1H\nTrading hours I am available", "เช่น 3 ตลาด · รายวัน / 4H / 1H\nช่วงเวลาที่ว่างเทรด")),
        (C["teal"], t("3 · Setups (A+ only)", "3 · เซ็ตอัพ (เฉพาะ A+)"), t("1–2 setups with screenshots:\nwhat they look like, what they need", "1–2 เซ็ตอัพพร้อมภาพตัวอย่าง:\nหน้าตาเป็นอย่างไร ต้องมีอะไร")),
        (C["bull"], t("4 · Entry rules", "4 · กฎการเข้า"), t("Checklist from Phase 2:\nHTF bias · zone · LTF CHoCH · R:R ≥ 2", "เช็กลิสต์จากเฟส 2:\nทิศทาง HTF · โซน · CHoCH บน LTF · R:R ≥ 2")),
        (C["bear"], t("5 · Risk rules", "5 · กฎความเสี่ยง"), t("Risk 0.5–1% · max open 3R\nDaily −2R · weekly −5R", "เสี่ยง 0.5–1% · เปิดรวมไม่เกิน 3R\nรายวัน −2R · รายสัปดาห์ −5R")),
        (C["amber"], t("6 · Exit rules", "6 · กฎการออก")
         , t("Stop beyond structure + buffer\nTarget method A / B / C (3.5)", "Stop เลยโครงสร้าง + ระยะเผื่อ\nวิธีทำกำไร A / B / C (3.5)")),
        (C["pink"], t("7 · Routine", "7 · กิจวัตร"), t("Before · during · after (4.4)\nJournal every trade (4.5)", "ก่อน · ระหว่าง · หลัง (4.4)\nบันทึกทุกเทรด (4.5)")),
        (C["muted"], t("8 · Circuit breakers", "8 · เบรกเกอร์ตัดไฟ"), t("−5% → half risk · −10% → stop & review\nTilt signs → walk away (4.6)", "−5% → ลดครึ่ง · −10% → หยุดและทบทวน\nสัญญาณ Tilt → ลุกออกไป (4.6)")),
    ]
    for k, (col, head, body) in enumerate(items):
        x = 28 + (k % 2) * 460
        y = 92 + (k // 2) * 114
        s.rect(x, y, 444, 102, fill=C["panel"], stroke=C["border"], rx=12)
        s.rect(x, y, 5, 102, fill=col, rx=2)
        s.text(x + 22, y + 30, head, 16, col, weight=700)
        s.text(x + 22, y + 58, body, 14, C["text"])
    return s.render()


@fig
def if_then(lang):
    t = tr(lang)
    s = SVG(960, 600, t("If-then rules: the decision is made before the moment", "กฎถ้า-แล้ว: ตัดสินใจไว้ก่อนถึงเวลาจริง"),
            t("Every \"no\" is a complete, correct decision. It costs 0R.", "ทุก \"ไม่\" คือการตัดสินใจที่ครบและถูกต้อง มันเสีย 0R"))
    steps = [
        t("IF the HTF state is a trend (not range / unclear)", "ถ้า สภาวะ HTF เป็นเทรนด์ (ไม่ใช่กรอบ / ไม่ชัด)"),
        t("AND price is in an HTF zone in the trend direction", "และ ราคาอยู่ในโซน HTF ตามทิศทางเทรนด์"),
        t("AND the LTF prints a CHoCH in the HTF direction", "และ LTF เกิด CHoCH ในทิศทางของ HTF"),
        t("AND the honest R:R to a real level is ≥ 2", "และ R:R ตามจริงถึงระดับราคาจริง ≥ 2"),
        t("AND no circuit breaker is active (daily/weekly limits, tilt)", "และ ไม่มีเบรกเกอร์ทำงาน (ลิมิตรายวัน/สัปดาห์ Tilt)"),
    ]
    x, w, h = 60, 560, 58
    for k, txt in enumerate(steps):
        y = 100 + k * 84
        s.rect(x, y, w, h, fill=C["panel"], stroke=C["blue"], rx=10)
        s.text(x + 20, y + 35, txt, 15, C["text"], weight=600)
        s.arrow(x + w + 4, y + h / 2, x + w + 96, y + h / 2, C["bear"], 2)
        s.text(x + w + 50, y + h / 2 - 8, t("no", "ไม่"), 12, C["bear"], "middle", 700)
        if k < len(steps) - 1:
            s.arrow(x + w / 2, y + h + 2, x + w / 2, y + 82, C["bull"], 2)
            s.text(x + w / 2 + 10, y + h + 18, t("yes", "ใช่"), 12, C["bull"], weight=700)
    s.rect(x + w + 100, 100, 240, 4 * 84 + h, fill=C["bear"], opacity=0.1, stroke=C["bear"], rx=12)
    s.text(x + w + 220, 300, t("NO TRADE\n\nwrite why in\nthe journal", "ไม่เทรด\n\nเขียนเหตุผล\nลงในบันทึก"), 18, C["bear"], "middle", 700)
    y = 100 + 5 * 84
    s.arrow(x + w / 2, y - 26 + 2, x + w / 2, y + 4, C["bull"], 2)
    s.rect(x, y + 6, w, 58, fill=C["bull"], opacity=0.15, stroke=C["bull"], rx=10)
    s.text(x + 20, y + 41, t("THEN size it (3.2) → place entry, stop and target → journal it", "แล้ว คำนวณขนาด (3.2) → วางจุดเข้า Stop เป้าหมาย → บันทึก"), 15, C["bull"], weight=700)
    return s.render()


# ---------------------------------------------------------------- 4.4
@fig
def routine(lang):
    t = tr(lang)
    s = SVG(960, 520, t("A daily routine: before, during, after", "กิจวัตรประจำวัน: ก่อน ระหว่าง หลัง"),
            t("Routines remove decisions. Fewer decisions = less room for emotion.",
              "กิจวัตรลดการตัดสินใจ ตัดสินใจน้อยลง = อารมณ์มีที่เล่นน้อยลง"))
    cols = [
        (C["blue"], t("BEFORE · 20–30 min", "ก่อน · 20–30 นาที"), [
            t("State check: sleep, mood, stress 1–5", "เช็กตัวเอง: นอน อารมณ์ เครียด 1–5"),
            t("News & event calendar (Phase 10)", "ข่าวและปฏิทินเศรษฐกิจ (เฟส 10)"),
            t("HTF state for each market", "สภาวะ HTF ของแต่ละตลาด"),
            t("Mark zones, set price alerts", "มาร์กโซน ตั้งแจ้งเตือนราคา"),
            t("Write today's if-then plan", "เขียนแผนถ้า-แล้วของวันนี้"),
        ]),
        (C["bull"], t("DURING · on alert", "ระหว่าง · เมื่อมีแจ้งเตือน"), [
            t("Alert fires → open LTF", "แจ้งเตือนดัง → เปิด LTF"),
            t("Run the if-then checklist", "ไล่เช็กลิสต์ถ้า-แล้ว"),
            t("Size → enter → stop in market", "คำนวณขนาด → เข้า → ตั้ง Stop จริง"),
            t("Manage by the plan only", "บริหารตามแผนเท่านั้น"),
            t("No alert = no screen", "ไม่มีแจ้งเตือน = ไม่ต้องดูจอ"),
        ]),
        (C["purple"], t("AFTER · 15 min", "หลัง · 15 นาที"), [
            t("Journal every trade + screenshot", "บันทึกทุกเทรด + ภาพหน้าจอ"),
            t("Grade execution A / B / C", "ให้เกรดการลงมือ A / B / C"),
            t("Note emotions at entry & exit", "จดอารมณ์ตอนเข้าและตอนออก"),
            t("Update equity peak & drawdown", "อัปเดตจุดสูงสุดของพอร์ต & Drawdown"),
            t("Close the platform. Done.", "ปิดแพลตฟอร์ม จบวัน"),
        ]),
    ]
    for k, (col, head, items) in enumerate(cols):
        x = 28 + k * 308
        s.rect(x, 92, 290, 408, fill=C["panel"], stroke=C["border"], rx=12)
        s.rect(x, 92, 290, 50, fill=col, opacity=0.18, rx=12)
        s.text(x + 145, 124, head, 16, col, "middle", 700)
        for j, it in enumerate(items):
            y = 172 + j * 64
            s.circle(x + 28, y - 5, 12, col)
            s.text(x + 28, y, str(j + 1), 12, C["white"], "middle", 700)
            s.text(x + 50, y, it, 13, C["text"])
        if k < 2:
            s.arrow(x + 292, 300, x + 306, 300, C["muted"], 2.5)
    return s.render()


# ---------------------------------------------------------------- 4.5
@fig
def journal(lang):
    t = tr(lang)
    s = SVG(960, 500, t("A journal entry that teaches you something", "บันทึกการเทรดที่สอนอะไรคุณได้"),
            t("Numbers tell you WHAT happened. Tags and notes tell you WHY.", "ตัวเลขบอกว่า เกิดอะไรขึ้น แท็กและโน้ตบอกว่า ทำไม"))
    heads = [t("Date", "วันที่"), t("Setup", "เซ็ตอัพ"), t("Plan R:R", "R:R แผน"), t("Result", "ผลลัพธ์"),
             t("Grade", "เกรด"), t("Emotion", "อารมณ์"), t("Tags", "แท็ก")]
    widths = [80, 160, 80, 80, 60, 140, 270]
    rows = [
        ("03-02", t("Demand + 1H CHoCH", "Demand + CHoCH 1H"), "1:2.7", "+2.0R", "A", t("calm", "สงบ"), t("followed-plan", "ทำตามแผน")),
        ("03-03", t("Break & retest", "Break & Retest"), "1:2.1", "−1.0R", "A", t("calm", "สงบ"), t("followed-plan · valid-loss", "ทำตามแผน · แพ้ถูกต้อง")),
        ("03-03", t("No setup (chased)", "ไม่มีเซ็ตอัพ (ไล่ราคา)"), "—", "−1.6R", "C", t("FOMO after loss", "FOMO หลังแพ้"), t("broke-plan · revenge · moved-stop", "ผิดแผน · แก้แค้น · ย้าย Stop")),
    ]
    x0, y0 = 28, 100
    total = sum(widths)
    s.rect(x0, y0, total, 44, fill=C["panel"], stroke=C["border"], rx=8)
    x = x0
    for hd, w in zip(heads, widths):
        s.text(x + 12, y0 + 28, hd, 13, C["muted"], weight=700)
        x += w
    for r, row in enumerate(rows):
        y = y0 + 52 + r * 52
        bad = row[4] == "C"
        s.rect(x0, y, total, 46, fill=C["bear"] if bad else C["panel"], opacity=0.12 if bad else 1, stroke=C["border"], rx=8)
        x = x0
        for j, (cell, w) in enumerate(zip(row, widths)):
            col = C["text"]
            if j == 3:
                col = C["bull"] if cell.startswith("+") else C["bear"]
            if j == 4:
                col = {"A": C["bull"], "B": C["amber"], "C": C["bear"]}[cell]
            s.text(x + 12, y + 29, cell, 13, col, weight=700 if j in (3, 4) else 400)
            x += w
    s.card(28, 320, 440, 160, t("What the numbers say", "ตัวเลขบอกอะไร"),
           t("Day total: −0.6R. Looks like a bad day.\nBut the plan trades made +1.0R.\nThe loss came from one C-grade trade.",
             "รวมทั้งวัน: −0.6R ดูเหมือนวันที่แย่\nแต่เทรดตามแผนทำได้ +1.0R\nการขาดทุนมาจากเทรดเกรด C ไม้เดียว"), C["amber"], 17, 14)
    s.card(492, 320, 440, 160, t("The lesson", "บทเรียน"),
           t("Not \"my system is broken\" but\n\"after a loss I chase\". The fix is a rule:\n\"After any loss: 15-minute break.\"",
             "ไม่ใช่ \"ระบบพัง\" แต่คือ\n\"หลังแพ้ ฉันไล่ราคา\" ทางแก้คือกฎ:\n\"หลังแพ้ทุกครั้ง: พัก 15 นาที\""), C["bull"], 17, 14)
    return s.render()


@fig
def review_loop(lang):
    t = tr(lang)
    s = SVG(960, 520, t("The review loop: how traders actually improve", "วงจรทบทวน: วิธีที่นักเทรดพัฒนาได้จริง"),
            t("Change ONE thing at a time, then measure it over enough trades.", "เปลี่ยนทีละ หนึ่ง อย่าง แล้ววัดผลจากจำนวนเทรดที่มากพอ"))
    cx, cy, r = 330, 300, 160
    nodes = [
        (C["blue"], t("PLAN", "วางแผน"), t("rules written", "เขียนกฎไว้")),
        (C["bull"], t("TRADE", "เทรด"), t("follow the rules", "ทำตามกฎ")),
        (C["amber"], t("JOURNAL", "บันทึก"), t("every trade, tagged", "ทุกเทรด ติดแท็ก")),
        (C["purple"], t("REVIEW", "ทบทวน"), t("weekly & monthly", "รายสัปดาห์ & เดือน")),
        (C["pink"], t("ADJUST", "ปรับ"), t("ONE change", "เปลี่ยน หนึ่ง อย่าง")),
    ]
    pos = []
    for k in range(5):
        a = -math.pi / 2 + k * 2 * math.pi / 5
        pos.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    for k in range(5):
        (x0, y0), (x1, y1) = pos[k], pos[(k + 1) % 5]
        dx, dy = x1 - x0, y1 - y0
        L = math.hypot(dx, dy)
        ux, uy = dx / L, dy / L
        s.arrow(x0 + ux * 62, y0 + uy * 62, x1 - ux * 66, y1 - uy * 66, C["muted"], 2.5)
    for (x, y), (col, name, sub) in zip(pos, nodes):
        s.circle(x, y, 56, C["panel"], col, 2.5)
        s.text(x, y - 2, name, 15, col, "middle", 700)
        s.text(x, y + 18, sub, 11, C["muted"], "middle")
    s.card(600, 100, 332, 190, t("Weekly review (30 min)", "ทบทวนรายสัปดาห์ (30 นาที)"),
           t("· Total R, win %, avg win / loss\n· % of trades that followed the plan\n· R from A-grade vs C-grade trades\n· Most common mistake tag\n· One thing to change next week",
             "· R รวม %ชนะ กำไร/ขาดทุนเฉลี่ย\n· % เทรดที่ทำตามแผน\n· R จากเทรดเกรด A vs เกรด C\n· แท็กความผิดพลาดที่เจอบ่อยสุด\n· สิ่งเดียวที่จะเปลี่ยนสัปดาห์หน้า"),
           C["purple"], 17, 14)
    s.card(600, 306, 332, 190, t("Monthly review (1 hour)", "ทบทวนรายเดือน (1 ชั่วโมง)"),
           t("· Expectancy per setup (3.4)\n· Drawdown vs your rules (3.6)\n· Best & worst 3 trades: re-watch\n· Is the change from last month\n  working? Keep, adjust or drop.",
             "· ค่าคาดหวังแยกตามเซ็ตอัพ (3.4)\n· Drawdown เทียบกับกฎ (3.6)\n· 3 เทรดดีสุดและแย่สุด: ดูซ้ำ\n· สิ่งที่เปลี่ยนเดือนก่อนได้ผลไหม?\n  เก็บไว้ ปรับ หรือทิ้ง"),
           C["pink"], 17, 14)
    return s.render()


# ---------------------------------------------------------------- 4.6
@fig
def tilt(lang):
    t = tr(lang)
    s = SVG(960, 500, t("The tilt meter: know where you are before you click", "มาตรวัด Tilt: รู้ว่าตัวเองอยู่ตรงไหนก่อนกดคลิก"),
            t("Tilt = emotion has taken over decisions. It builds in stages, and each stage has a rule.",
              "Tilt = อารมณ์เข้ามาคุมการตัดสินใจ มันก่อตัวเป็นขั้น และแต่ละขั้นมีกฎของมัน"))
    zones = [
        (C["bull"], t("GREEN · in control", "เขียว · ควบคุมได้"),
         t("Calm, patient, bored by\nwaiting. Losses feel like\nbusiness costs.", "สงบ อดทน เบื่อกับการรอ\nการแพ้รู้สึกเหมือน\nต้นทุนธุรกิจ"),
         t("Trade the plan.", "เทรดตามแผน")),
        (C["amber"], t("AMBER · warming up", "เหลือง · เริ่มร้อน"),
         t("Checking P&L often, urge to\n'make it back', faster clicks,\nskipping checklist steps.", "ดูกำไรขาดทุนบ่อย อยาก\n'เอาคืน' คลิกเร็วขึ้น\nข้ามขั้นในเช็กลิสต์"),
         t("Pause 15 min. Half size.", "พัก 15 นาที ลดไม้ครึ่งหนึ่ง")),
        (C["bear"], t("RED · tilted", "แดง · Tilt แล้ว"),
         t("Anger or panic, revenge\ntrades, moving stops,\nsizing up after losses.", "โกรธหรือตื่นตระหนก เทรดแก้แค้น\nย้าย Stop เพิ่มไม้\nหลังแพ้"),
         t("Close the platform. Done today.", "ปิดแพลตฟอร์ม จบวันนี้")),
    ]
    x0, y0, w = 40, 110, 880
    seg = w / 3
    for k, (col, name, signs, rule) in enumerate(zones):
        x = x0 + k * seg
        s.rect(x + 2, y0, seg - 4, 22, fill=col, rx=11, opacity=0.9)
        s.rect(x + 2, y0 + 36, seg - 4, 330, fill=C["panel"], stroke=col, rx=12)
        s.text(x + 22, y0 + 72, name, 17, col, weight=700)
        s.text(x + 22, y0 + 104, t("Signs:", "สัญญาณ:"), 12, C["dim"], weight=700)
        s.text(x + 22, y0 + 128, signs, 14, C["text"])
        s.rect(x + 14, y0 + 270, seg - 32, 80, fill=col, opacity=0.14, rx=10)
        s.text(x + 26, y0 + 296, t("Rule:", "กฎ:"), 12, C["dim"], weight=700)
        s.text(x + 26, y0 + 324, rule, 15, col, weight=700)
    return s.render()


@fig
def circuit_breakers(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Circuit breakers for losing streaks", "เบรกเกอร์ตัดไฟสำหรับช่วงแพ้ติดกัน"),
            t("Automatic, pre-agreed, not negotiable in the moment.", "อัตโนมัติ ตกลงไว้ล่วงหน้า ห้ามต่อรองในตอนนั้น"))
    steps = [
        (C["amber"], t("Any loss", "แพ้ทุกครั้ง"), t("15-minute break away from the screen", "พัก 15 นาทีห่างจากจอ")),
        (C["amber"], t("2 losses in a row", "แพ้ติดกัน 2 ไม้"), t("Re-read the plan. Next trade must be A-grade only", "อ่านแผนอีกครั้ง ไม้ถัดไปต้องเป็นเกรด A เท่านั้น")),
        (C["bear"], t("−2R or 3 losses today", "−2R หรือแพ้ 3 ไม้ในวันนี้"), t("Done for the day. Journal, then close the platform", "จบวันนี้ บันทึก แล้วปิดแพลตฟอร์ม")),
        (C["bear"], t("−5R this week", "−5R ในสัปดาห์นี้"), t("Done for the week. Weekly review early", "จบสัปดาห์นี้ ทำการทบทวนรายสัปดาห์ก่อนกำหนด")),
        (C["purple"], t("−10% from equity peak", "−10% จากจุดสูงสุดของพอร์ต"), t("Stop live trading. Full review. Demo until fixed", "หยุดเงินจริง ทบทวนทั้งหมด ใช้บัญชีทดลอง")),
    ]
    for k, (col, trig, act) in enumerate(steps):
        y = 96 + k * 72
        x = 40 + k * 40
        s.rect(x, y, 300, 60, fill=col, opacity=0.18, stroke=col, rx=10)
        s.text(x + 18, y + 37, trig, 16, col, weight=700)
        s.arrow(x + 306, y + 30, x + 346, y + 30, C["muted"], 2)
        s.rect(x + 352, y, 520 - k * 40, 60, fill=C["panel"], stroke=C["border"], rx=10)
        s.text(x + 370, y + 37, act, 14, C["text"])
    return s.render()


# ---------------------------------------------------------------- 4.7
@fig
def summary(lang):
    t = tr(lang)
    s = SVG(960, 560, t("Phase 4 on one page", "สรุปเฟส 4 ในหน้าเดียว"))
    cx, cy = 480, 310
    nodes = [
        (170, 140, C["bear"], t("4.1 Emotions", "4.1 อารมณ์"), t("Fear · greed · hope · regret.\nName it, then follow the plan.", "กลัว · โลภ · หวัง · เสียดาย\nเรียกชื่อมัน แล้วทำตามแผน")),
        (790, 140, C["amber"], t("4.2 Biases", "4.2 อคติ"), t("Everyone has them.\nRules catch them.", "ทุกคนมี\nกฎดักจับมันได้")),
        (150, 320, C["blue"], t("4.3 Trading plan", "4.3 แผนการเทรด"), t("One page. If-then rules.\n\"No\" costs 0R.", "หนึ่งหน้า กฎถ้า-แล้ว\n\"ไม่\" เสีย 0R")),
        (810, 320, C["bull"], t("4.4 Routine", "4.4 กิจวัตร"), t("Before · during · after.\nNo alert = no screen.", "ก่อน · ระหว่าง · หลัง\nไม่มีแจ้งเตือน = ไม่ต้องดูจอ")),
        (250, 480, C["purple"], t("4.5 Journal & review", "4.5 บันทึก & ทบทวน"), t("Tag every trade.\nChange one thing at a time.", "ติดแท็กทุกเทรด\nเปลี่ยนทีละอย่าง")),
        (710, 480, C["pink"], t("4.6 Streaks & tilt", "4.6 แพ้ติดกัน & Tilt"), t("Know your tilt signs.\nCircuit breakers decide.", "รู้สัญญาณ Tilt ของตัวเอง\nให้เบรกเกอร์ตัดสิน")),
    ]
    for x, y, col, head, body in nodes:
        s.line(cx, cy, x, y, col, 2, opacity=0.5)
    s.circle(cx, cy, 74, C["panel"], C["text"], 2)
    s.text(cx, cy - 4, t("PHASE 4", "เฟส 4"), 20, C["text"], "middle", 700)
    s.text(cx, cy + 20, t("Psychology", "จิตวิทยา"), 14, C["muted"], "middle")
    for x, y, col, head, body in nodes:
        s.rect(x - 130, y - 42, 260, 92, fill=C["panel"], stroke=col, rx=12)
        s.text(x, y - 14, head, 17, col, "middle", 700)
        s.text(x, y + 10, body, 13, C["text"], "middle")
    return s.render()


# ---------------------------------------------------------------- v2 additions (B9d)
from math import comb


@fig
def early_exits(lang):
    t = tr(lang)
    s = SVG(960, 460, t("What cutting winners early does to a good system", "การตัดกำไรเร็วทำอะไรกับระบบที่ดี"),
            t("Plan: 40% wins at +2.5R, losses −1R. Fear closes some winners at +0.3R instead (computed).",
              "แผน: ชนะ 40% ที่ +2.5R แพ้ −1R ความกลัวทำให้ปิดไม้ชนะบางไม้ที่ +0.3R แทน (คำนวณจริง)"))
    x0, y0, w, h = 110, 110, 560, 280
    panel(s, x0 - 60, y0 - 20, w + 100, h + 70)
    lo, hi = -0.5, 0.5
    X = lambda f: x0 + f * w
    Y = lambda e: y0 + h * (hi - e) / (hi - lo)
    for e in (-0.4, -0.2, 0, 0.2, 0.4):
        s.line(x0, Y(e), x0 + w, Y(e), C["dim"] if e == 0 else C["grid"], 1.5 if e == 0 else 1)
        s.text(x0 - 10, Y(e) + 4, f"{e:+.1f}R", 12, C["muted"], "end")
    ex = lambda f: 0.4 * ((1 - f) * 2.5 + f * 0.3) - 0.6
    s.polyline([(X(f / 100), Y(ex(f / 100))) for f in range(0, 101, 5)], C["amber"], 3)
    be = (2.5 - 1.5) / (2.5 - 0.3)
    for f in (0, 0.25, be, 0.5, 0.75):
        e = ex(f)
        col = C["bull"] if e > 0.001 else (C["text"] if abs(e) < 0.001 else C["bear"])
        s.circle(X(f), Y(e), 6, col)
        if abs(e) > 0.001:
            s.text(X(f) + 10, Y(e) - 10, f"{e:+.2f}R", 13, col, weight=700)
        else:
            s.text(X(f) - 10, Y(e) - 12, t("break-even (45%)", "คุ้มทุน (45%)"), 13, col, "end", 700)
    for f in (0, 0.25, 0.5, 0.75, 1):
        s.text(X(f), y0 + h + 22, f"{f:.0%}", 12, C["muted"], "middle")
    s.text(x0 + w / 2, y0 + h + 42, t("share of winners closed early at +0.3R", "สัดส่วนไม้ชนะที่ปิดเร็วที่ +0.3R"), 13, C["muted"], "middle")
    s.card(740, 90, 190, 350, t("Read it", "อ่านอย่างไร"),
           t("No early exits:\n+0.40R / trade\n \nCut 1 in 4:\n+0.18R\n \nCut 45%:\nzero edge\n \nCut half:\n−0.04R\n(a losing system)",
             "ไม่ตัดเร็วเลย:\n+0.40R / ไม้\n \nตัด 1 ใน 4:\n+0.18R\n \nตัด 45%:\nความได้เปรียบเป็นศูนย์\n \nตัดครึ่งหนึ่ง:\n−0.04R\n(ระบบที่ขาดทุน)"),
           C["amber"], 16, 14)
    return s.render()


@fig
def sample_luck(lang):
    t = tr(lang)
    s = SVG(960, 440, t("A real edge still has losing stretches", "ความได้เปรียบจริงก็ยังมีช่วงที่ขาดทุน"),
            t("Chance that a run of N trades ends below 0R, for a system with +0.35R per trade (45% wins at +2R). Exact binomial maths.",
              "โอกาสที่ N ไม้ติดกันจบต่ำกว่า 0R สำหรับระบบ +0.35R ต่อไม้ (ชนะ 45% ที่ +2R) คำนวณทวินามแบบแม่นยำ"))
    ns = [10, 20, 50, 100, 200]
    x0, base, hmax, gw = 120, 350, 220, 160
    s.line(x0 - 30, base, x0 + len(ns) * gw - 40, base, C["dim"], 1.5)
    for k, n in enumerate(ns):
        p = sum(comb(n, j) * 0.45 ** j * 0.55 ** (n - j) for j in range(n + 1) if 3 * j - n < 0)
        x = x0 + k * gw
        col = C["bear"] if p > 0.2 else (C["amber"] if p > 0.02 else C["bull"])
        s.rect(x, base - p * hmax / 0.3, 90, max(p * hmax / 0.3, 2), fill=col, opacity=0.85, rx=4)
        s.text(x + 45, base - p * hmax / 0.3 - 10, f"{p * 100:.1f}%" if p >= 0.001 else "<0.1%", 15, col, "middle", 700)
        s.text(x + 45, base + 24, t(f"{n} trades", f"{n} ไม้"), 14, C["text"], "middle", 700)
    s.text(90, 410, t("Judging a system on its last 10 trades is close to judging it on a coin flip. 100+ trades tell you much more.",
                      "การตัดสินระบบจาก 10 ไม้ล่าสุดแทบไม่ต่างจากการโยนเหรียญ 100 ไม้ขึ้นไปบอกอะไรได้มากกว่ามาก"), 13, C["amber"], weight=600)
    return s.render()


@fig
def chase_cost(lang):
    t = tr(lang)
    s = SVG(960, 460, t("The cost of chasing a missed entry", "ต้นทุนของการไล่ตามจุดเข้าที่พลาด"),
            t("Lesson 4.3's BTC plan: entry 62,000, stop 61,050 (1R = 950), target 64,400. Same stop and target, later entries.",
              "แผน BTC ในบทที่ 4.3: เข้า 62,000 Stop 61,050 (1R = 950) เป้า 64,400 Stop และเป้าเดิม แต่เข้าช้าลง"))
    e0, stop, tgt = 62000, 61050, 64400
    X = lambda p: 250 + (p - 60800) * 0.14
    for p in (61000, 62000, 63000, 64000):
        s.line(X(p), 105, X(p), 400, C["grid"], 1)
        s.text(X(p), 420, f"{p:,}", 12, C["muted"], "middle")
    for k, c in enumerate((0, 0.25, 0.5, 1.0)):
        e = e0 + c * 950
        rr = (tgt - e) / (e - stop)
        be = 1 / (1 + rr)
        col = [C["bull"], C["amber"], C["orange"] if "orange" in C else C["amber"], C["bear"]][k]
        y = 120 + k * 72
        s.text(40, y + 22, t("planned entry", "จุดเข้าตามแผน") if c == 0 else t(f"chase +{c:g}R", f"ไล่ +{c:g}R"), 15, col, weight=700)
        s.text(40, y + 42, t(f"entry {e:,.0f}", f"เข้า {e:,.0f}"), 12, C["muted"])
        s.rect(X(stop), y + 8, X(e) - X(stop), 26, fill=C["bear"], opacity=0.5, rx=3)
        s.rect(X(e), y + 8, X(tgt) - X(e), 26, fill=C["bull"], opacity=0.3, rx=3)
        s.text(X(tgt) + 10, y + 20, f"R:R {rr:.2f}", 14, col, weight=700)
        s.text(X(tgt) + 10, y + 38, t(f"break-even win rate {be:.0%}", f"อัตราชนะคุ้มทุน {be:.0%}"), 12, C["text"])
    return s.render()


@fig
def day_clock(lang):
    t = tr(lang)
    s = SVG(960, 470, t("A trading day in UTC+7: when the market moves", "หนึ่งวันเทรดในเวลา UTC+7: ตลาดขยับเมื่อไร"),
            t("Times for northern summer. In northern winter, add one hour (crypto's 07:00 close does not change).",
              "เวลาช่วงฤดูร้อนซีกโลกเหนือ ช่วงฤดูหนาวบวกหนึ่งชั่วโมง (เวลาปิดแท่งคริปโต 07:00 ไม่เปลี่ยน)"))
    h0, h1 = 12, 32  # 12:00 to 08:00 next day
    X = lambda hr: 60 + (hr - h0) * 42
    y = 250
    s.rect(X(h0), y - 14, X(h1) - X(h0), 28, fill=C["panel"], stroke=C["border"], rx=6)
    s.rect(X(14), y - 14, X(23) - X(14), 28, fill=C["blue"], opacity=0.25, rx=6)
    s.text(X(14) + 14, y + 5, t("London session", "ช่วงลอนดอน"), 12, C["text"], "start", 600)
    s.text(X(23) - 8, y + 5, t("NY overlap", "ซ้อนนิวยอร์ก"), 12, C["text"], "end", 600)
    for hr in range(h0, h1 + 1, 2):
        s.text(X(hr), y + 38, f"{hr % 24:02d}:00", 11, C["muted"], "middle")
        s.line(X(hr), y + 14, X(hr), y + 22, C["dim"], 1)
    evs = [(14, t("London open", "ลอนดอนเปิด"), C["blue"], -1, "middle"), (19.5, t("US CPI / jobs data", "ข้อมูล CPI / จ้างงานสหรัฐ"), C["bear"], -2, "end"),
           (20.5, t("US stock open", "ตลาดหุ้นสหรัฐเปิด"), C["amber"], -2, "start"), (25, t("FOMC decision", "ผลประชุม FOMC"), C["purple"], -1, "middle"),
           (28, t("FX/gold daily close", "ปิดแท่งรายวัน FX/ทอง"), C["teal"], -2, "middle"), (31, t("crypto daily close", "ปิดแท่งรายวันคริปโต"), C["pink"], -1, "end")]
    for hr, name, col, lvl, anc in evs:
        yy = y - 30 + lvl * 40
        s.line(X(hr), yy + 6, X(hr), y - 14, col, 1.5, "3 3")
        s.circle(X(hr), y, 5, col)
        hh, mm = int(hr % 24), int(round((hr % 1) * 60))
        dx = {"middle": 0, "end": -6, "start": 6}[anc]
        s.text(X(hr) + dx, yy - 12, name, 12, col, anc, 700)
        s.text(X(hr) + dx, yy + 2, f"{hh:02d}:{mm:02d}", 12, C["text"], anc)
    # example trader (lesson 4.4)
    yb = 340
    s.text(60, yb, t("The swing trader in lesson 4.4:", "สวิงเทรดเดอร์ในบทที่ 4.4:"), 13, C["muted"], weight=600)
    for a, b, lab, col in ((19.5, 19.92, t("before", "ก่อน"), C["bull"]), (21.67, 21.75, t("entry", "เข้า"), C["amber"]),
                           (22, 22.25, t("after", "หลัง"), C["bull"])):
        s.rect(X(a), yb + 14, max(X(b) - X(a), 6), 22, fill=col, opacity=0.8, rx=4)
        s.text(X(a) + max(X(b) - X(a), 6) / 2, yb + 6 if a == 21.67 else yb + 54, lab, 12, col, "middle", 700)
    s.text(60, 430, t("Plan your session around these times: no new entries just before high-impact releases (see 10.3).",
                      "วางแผนเซสชันรอบเวลาเหล่านี้: ไม่เข้าไม้ใหม่ก่อนการประกาศข้อมูลสำคัญ (ดู 10.3)"), 13, C["amber"], weight=600)
    return s.render()


@fig
def grade_split(lang):
    t = tr(lang)
    s = SVG(960, 430, t("Split the week by grade: where did the R go?", "แยกสัปดาห์ตามเกรด: R ไปไหน?"),
            t("Lesson 4.5's week: 9 trades, −0.4R in total.", "สัปดาห์ในบทที่ 4.5: 9 ไม้ รวม −0.4R"))
    rows = [(t("A-grade (6 trades)", "เกรด A (6 ไม้)"), 3.1, C["bull"]), (t("C-grade (3 trades)", "เกรด C (3 ไม้)"), -3.5, C["bear"]),
            (t("Week total", "รวมทั้งสัปดาห์"), -0.4, C["amber"]), (t("Week without C trades", "สัปดาห์ที่ไม่มีไม้เกรด C"), 3.1, C["blue"])]
    zero, sc = 520, 55
    s.line(zero, 100, zero, 380, C["dim"], 1.5)
    for k, (name, r, col) in enumerate(rows):
        y = 115 + k * 68
        s.text(60, y + 26, name, 15, col, weight=700)
        s.rect(min(zero, zero + r * sc), y + 6, abs(r) * sc, 34, fill=col, opacity=0.8, rx=4)
        s.text(zero + r * sc + (10 if r > 0 else -10), y + 29, f"{r:+.1f}R", 15, col, "start" if r > 0 else "end", 700)
    s.text(60, 405, t("Tags on the C trades: revenge ×2, moved-stop ×1. The system worked; the leak was behaviour after losses.",
                      "แท็กของไม้เกรด C: แก้แค้น ×2, เลื่อน Stop ×1 ระบบใช้ได้ รอยรั่วคือพฤติกรรมหลังแพ้"), 13, C["muted"])
    return s.render()


@fig
def breaker_savings(lang):
    t = tr(lang)
    s = SVG(960, 450, t("A bad day with and without the circuit breaker", "วันแย่ ๆ ที่มีและไม่มีเบรกเกอร์ตัดไฟ"),
            t("Illustrative sequence: 3 normal losses, then a sized-up loss, a moved stop and two revenge trades.",
              "ลำดับตัวอย่าง: แพ้ปกติ 3 ไม้ แล้วแพ้ไม้ที่เพิ่มขนาด ไม้ที่เลื่อน Stop และไม้แก้แค้นอีกสองไม้"))
    seq = [-1, -1, -1, -1.5, -2, -1, -1]
    tags = ["", "", "", t("size up", "เพิ่มขนาด"), t("moved stop", "เลื่อน Stop"), t("revenge", "แก้แค้น"), t("revenge", "แก้แค้น")]
    x0, y0, w, h = 90, 110, 600, 270
    panel(s, x0 - 50, y0 - 20, w + 80, h + 60)
    X = lambda i: x0 + i * w / 7
    Y = lambda v: y0 + h * (0.5 - v) / 9.5
    for v in (0, -2, -4, -6, -8):
        s.line(x0, Y(v), x0 + w, Y(v), C["grid"], 1)
        s.text(x0 - 8, Y(v) + 4, f"{v}R", 12, C["muted"], "end")
    cum, pts = 0, [(X(0), Y(0))]
    for i, r in enumerate(seq, 1):
        cum += r
        pts.append((X(i), Y(cum)))
        if tags[i - 1]:
            s.text(X(i), Y(cum) + 22, tags[i - 1], 11, C["bear"], "middle", 600)
    s.polyline(pts, C["bear"], 2.5)
    s.polyline(pts[:4], C["bull"], 4)
    s.line(X(3), Y(-3) - 30, X(3), y0 + h, C["bull"], 1.5, "5 4")
    s.text(X(3), Y(-3) - 38, t("breaker: 3 losses → stop", "เบรกเกอร์: แพ้ 3 ไม้ → หยุด"), 12, C["bull"], "middle", 700)
    s.text(X(7), Y(cum) - 12, f"{cum:+g}R", 15, C["bear"], "middle", 700)
    s.card(740, 90, 190, 330, t("The difference", "ความต่าง"),
           t("With the breaker:\n−3R\n(−300 USD at 1R = 100)\n \nWithout it:\n−8.5R\n(−850 USD)\n \nSaved: 5.5R, plus\nthe habit of\nstopping.",
             "มีเบรกเกอร์:\n−3R\n(−300 ดอลลาร์ ที่ 1R = 100)\n \nไม่มี:\n−8.5R\n(−850 ดอลลาร์)\n \nประหยัด 5.5R และ\nนิสัยการหยุด"),
           C["bull"], 16, 13)
    return s.render()
