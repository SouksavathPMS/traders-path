"""Phase 10 figures: Macro, Wall Street & Investing (illustrative, not current data)."""
import math
from charts import SVG, C, tr
from figures.p2 import panel
from figures.p6 import Plot

FIGURES = {}


def fig(fn):
    FIGURES["p10-" + fn.__name__.replace("_", "-")] = fn
    return fn


def dcf(fcf=100, g=0.05, years=10, tg=0.02, r=0.08):
    flows, cf = [], fcf
    for t in range(1, years + 1):
        cf *= 1 + g
        flows.append(cf / (1 + r) ** t)
    tv = cf * (1 + tg) / (r - tg) / (1 + r) ** years
    return flows, tv, sum(flows) + tv


def mix(w, rs=0.07, vs=0.16, rb=0.03, vb=0.06, corr=0.1):
    ret = w * rs + (1 - w) * rb
    vol = math.sqrt((w * vs) ** 2 + ((1 - w) * vb) ** 2 + 2 * w * (1 - w) * vs * vb * corr)
    return ret, vol


# ---------------------------------------------------------------- 10.1
@fig
def business_cycle(lang):
    t = tr(lang)
    s = SVG(960, 500, t("The business cycle and what tends to lead", "วัฏจักรธุรกิจ และสิ่งที่มักนำหน้า"),
            t("Stylised. Real cycles vary in length and shape; markets usually move before the economic data.",
              "เป็นภาพจำลอง วัฏจักรจริงยาวสั้นและรูปร่างต่างกัน ตลาดมักเคลื่อนก่อนตัวเลขเศรษฐกิจ"))
    panel(s, 28, 90, 904, 390)
    P = Plot(s, 60, 120, 840, 200, 400, -1.3, 1.3)
    s.line(60, P.Y(0), 900, P.Y(0), C["dim"], 1, "4 4")
    s.text(64, P.Y(0) - 6, t("trend growth", "การเติบโตตามแนวโน้ม"), 11, C["muted"])
    P.path([(i, -math.cos(i / 400 * 2 * math.pi)) for i in range(401)], C["text"], 3)
    phases = [
        (0, 100, C["bull"], t("EARLY", "ช่วงต้น"), t("Recovery: rates low,\nprofits rebound.\nLeaders: small caps,\nfinancials, cyclicals", "ฟื้นตัว: ดอกเบี้ยต่ำ\nกำไรฟื้น ผู้นำ: หุ้นเล็ก\nการเงิน กลุ่มวัฏจักร")),
        (100, 200, C["blue"], t("MID", "ช่วงกลาง"), t("Steady growth.\nLeaders: technology,\nindustrials", "เติบโตสม่ำเสมอ\nผู้นำ: เทคโนโลยี\nอุตสาหกรรม")),
        (200, 300, C["amber"], t("LATE", "ช่วงปลาย"), t("Inflation, rate hikes,\ncurve flattens/inverts.\nLeaders: energy,\nmaterials, staples", "เงินเฟ้อ ขึ้นดอกเบี้ย\nเส้นผลตอบแทนแบน/กลับหัว\nผู้นำ: พลังงาน วัตถุดิบ\nสินค้าจำเป็น")),
        (300, 400, C["bear"], t("RECESSION", "ถดถอย"), t("Earnings fall, rate cuts.\nLeaders: bonds, utilities,\nhealth care, cash", "กำไรลด ลดดอกเบี้ย\nผู้นำ: พันธบัตร สาธารณูปโภค\nสุขภาพ เงินสด")),
    ]
    for a, b, col, name, body in phases:
        s.rect(P.X(a), 120, P.X(b) - P.X(a), 200, fill=col, opacity=0.07)
        s.text((P.X(a) + P.X(b)) / 2, 140, name, 14, col, "middle", 700)
        s.text(P.X(a) + 10, 352, body, 12, C["text"])
    return s.render()


# ---------------------------------------------------------------- 10.2
@fig
def transmission(lang):
    t = tr(lang)
    s = SVG(960, 470, t("How central bank policy reaches your chart", "นโยบายธนาคารกลางเดินทางมาถึงกราฟของคุณอย่างไร"),
            t("Higher policy rates or QT tighten financial conditions; cuts or QE loosen them, usually with a lag.",
              "ดอกเบี้ยนโยบายที่สูงขึ้นหรือ QT ทำให้ภาวะการเงินตึงตัว การลดดอกเบี้ยหรือ QE ผ่อนคลาย มักมีความล่าช้า"))
    boxes = [
        (60, C["purple"], t("Policy rate\n+ balance sheet\n(QE / QT)", "ดอกเบี้ยนโยบาย\n+ งบดุล\n(QE / QT)")),
        (270, C["blue"], t("Bond yields,\nmortgage & credit\nspreads", "ผลตอบแทนพันธบัตร\nสินเชื่อบ้าน &\nส่วนต่างเครดิต")),
        (480, C["amber"], t("Currency,\nliquidity, risk\nappetite", "ค่าเงิน\nสภาพคล่อง\nความกล้าเสี่ยง")),
        (690, C["bull"], t("Valuations, spending,\nearnings → asset\nprices", "มูลค่า การใช้จ่าย\nกำไร → ราคา\nสินทรัพย์")),
    ]
    for k, (x, col, body) in enumerate(boxes):
        s.rect(x, 100, 190, 120, fill=C["panel"], stroke=col, rx=12)
        s.text(x + 95, 140, body, 14, col, "middle", 700)
        if k < 3:
            s.arrow(x + 192, 160, x + 208, 160, C["muted"], 2.5)
    s.card(28, 250, 444, 200, t("QE: quantitative easing", "QE: การผ่อนคลายเชิงปริมาณ"),
           t("Central bank BUYS bonds with new reserves.\n→ lower long-term yields, more liquidity,\ninvestors pushed into riskier assets.\nHistorically supportive for stocks and credit.",
             "ธนาคารกลาง ซื้อ พันธบัตรด้วยเงินสำรองใหม่\n→ ผลตอบแทนระยะยาวต่ำลง สภาพคล่องเพิ่ม\nนักลงทุนถูกผลักไปหาสินทรัพย์เสี่ยงกว่า\nในอดีตเป็นแรงหนุนต่อหุ้นและตราสารหนี้เอกชน"), C["bull"], 17, 14)
    s.card(488, 250, 444, 200, t("QT: quantitative tightening", "QT: การตึงตัวเชิงปริมาณ"),
           t("Central bank lets bonds mature or SELLS them.\n→ reserves drain, upward pressure on yields,\nless liquidity in the system.\nUsually a headwind; effects are slow and debated.",
             "ธนาคารกลางปล่อยพันธบัตรครบอายุหรือ ขาย\n→ เงินสำรองลดลง ผลตอบแทนมีแรงกดขึ้น\nสภาพคล่องในระบบลดลง\nมักเป็นลมต้าน ผลช้าและยังถกเถียงกันอยู่"), C["bear"], 17, 14)
    return s.render()


@fig
def yield_curve(lang):
    t = tr(lang)
    s = SVG(960, 440, t("The yield curve: normal vs inverted", "เส้นผลตอบแทน: ปกติ vs กลับหัว"),
            t("Yield by maturity. An inverted curve (short > long) has often preceded recessions, with long and variable lags.",
              "ผลตอบแทนตามอายุ เส้นที่กลับหัว (ระยะสั้น > ระยะยาว) มักนำหน้าภาวะถดถอยในอดีต ด้วยระยะเวลาที่ยาวและไม่แน่นอน"))
    panel(s, 28, 90, 904, 330)
    mats = [0.25, 0.5, 1, 2, 3, 5, 7, 10, 20, 30]
    X = lambda m: 90 + 760 * math.log(m / 0.25) / math.log(30 / 0.25)
    Y = lambda y: 120 + 250 * (6 - y) / 6
    for y in range(0, 7):
        s.line(90, Y(y), 850, Y(y), C["grid"], 1)
        s.text(82, Y(y) + 4, f"{y}%", 11, C["muted"], "end")
    for m, lab in zip(mats, ["3m", "6m", "1y", "2y", "3y", "5y", "7y", "10y", "20y", "30y"]):
        s.text(X(m), 395, lab, 11, C["muted"], "middle")
    normal = [1.5, 1.7, 2.0, 2.4, 2.7, 3.1, 3.4, 3.7, 4.1, 4.2]
    inverted = [5.3, 5.3, 5.1, 4.7, 4.5, 4.3, 4.3, 4.3, 4.5, 4.4]
    s.polyline([(X(m), Y(y)) for m, y in zip(mats, normal)], C["bull"], 3)
    s.polyline([(X(m), Y(y)) for m, y in zip(mats, inverted)], C["bear"], 3)
    s.text(X(30) - 4, Y(4.2) + 22, t("normal: growth expected", "ปกติ: คาดการเติบโต"), 13, C["bull"], "end", 700)
    s.text(X(0.3), Y(5.3) - 10, t("inverted: tight policy now, cuts expected later", "กลับหัว: นโยบายตึงตอนนี้ คาดลดดอกเบี้ยภายหลัง"), 13, C["bear"], weight=700)
    return s.render()


# ---------------------------------------------------------------- 10.3
@fig
def calendar(lang):
    t = tr(lang)
    s = SVG(960, 520, t("The events that move markets", "เหตุการณ์ที่ขยับตลาด"),
            t("US releases, New York time (Bangkok = +11 h in US summer, +12 h in winter). Check an economic calendar weekly.",
              "ตัวเลขสหรัฐฯ เวลานิวยอร์ก (กรุงเทพฯ = +11 ชม. ช่วงฤดูร้อนสหรัฐฯ, +12 ชม. ฤดูหนาว) เช็กปฏิทินเศรษฐกิจทุกสัปดาห์"))
    rows = [
        (t("FOMC rate decision", "ประชุม FOMC"), "14:00", t("8× a year", "ปีละ 8 ครั้ง"), "★★★", t("Rates, dollar, everything", "ดอกเบี้ย ดอลลาร์ ทุกอย่าง")),
        (t("CPI (inflation)", "CPI (เงินเฟ้อ)"), "08:30", t("monthly", "รายเดือน"), "★★★", t("Rate expectations", "การคาดการณ์ดอกเบี้ย")),
        (t("Nonfarm payrolls (jobs)", "Nonfarm Payrolls (การจ้างงาน)"), "08:30", t("1st Friday", "ศุกร์แรกของเดือน"), "★★★", t("Growth & rates", "การเติบโต & ดอกเบี้ย")),
        (t("PCE inflation", "เงินเฟ้อ PCE"), "08:30", t("monthly", "รายเดือน"), "★★", t("Fed's preferred gauge", "มาตรวัดที่ Fed ชอบ")),
        (t("GDP", "GDP"), "08:30", t("quarterly", "รายไตรมาส"), "★★", t("Growth", "การเติบโต")),
        (t("ISM PMIs", "ISM PMI"), "10:00", t("monthly", "รายเดือน"), "★★", t("Business cycle (50 = line)", "วัฏจักรธุรกิจ (เส้น 50)")),
        (t("Retail sales", "ยอดค้าปลีก"), "08:30", t("monthly", "รายเดือน"), "★★", t("Consumer", "ผู้บริโภค")),
        (t("Jobless claims", "ผู้ขอรับสวัสดิการว่างงาน"), "08:30", t("weekly Thu", "พฤหัสทุกสัปดาห์"), "★", t("Early labour signal", "สัญญาณแรงงานล่วงหน้า")),
        (t("Company earnings", "ประกาศงบบริษัท"), t("pre/post market", "ก่อน/หลังตลาด"), t("quarterly", "รายไตรมาส"), "★★★", t("Single stocks, sectors", "หุ้นรายตัว กลุ่มอุตสาหกรรม")),
    ]
    xs = [40, 330, 480, 640, 720]
    for x, h in zip(xs, [t("Release", "รายการ"), t("NY time", "เวลา NY"), t("When", "เมื่อไหร่"), t("Impact", "ผลกระทบ"), t("Moves", "ขยับอะไร")]):
        s.text(x, 112, h, 12, C["muted"], weight=700)
    for k, row in enumerate(rows):
        y = 146 + k * 40
        s.rect(28, y - 24, 904, 36, fill=C["panel"], stroke=C["border"], rx=6)
        for j, (x, cell) in enumerate(zip(xs, row)):
            col = C["amber"] if j == 3 else C["text"]
            s.text(x, y, cell, 13, col, weight=700 if j in (0, 3) else 400)
    return s.render()


@fig
def surprise(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Markets react to the SURPRISE, not the number", "ตลาดตอบสนองต่อ ความประหลาดใจ ไม่ใช่ตัวเลข"),
            t("Same 'good' number, different reactions, depending on what was expected and already priced.",
              "ตัวเลข 'ดี' เดียวกัน ปฏิกิริยาต่างกัน ขึ้นกับสิ่งที่คาดไว้และสิ่งที่ราคาสะท้อนไปแล้ว"))
    cases = [
        (C["bull"], t("Better than expected", "ดีกว่าคาด"), t("Forecast 150k jobs\nActual 250k", "คาดการณ์ 150k\nจริง 250k"), [0, 0.1, 0, 2.2, 2.8, 2.5, 3.0]),
        (C["muted"], t("In line", "ตามคาด"), t("Forecast 250k\nActual 245k", "คาดการณ์ 250k\nจริง 245k"), [0, 0.2, -0.1, 0.9, -0.6, 0.3, 0.1]),
        (C["bear"], t("'Too good': rate fears", "'ดีเกินไป': กลัวดอกเบี้ยขึ้น"), t("Forecast 150k\nActual 400k → hike fears", "คาดการณ์ 150k\nจริง 400k → กลัวขึ้นดอกเบี้ย"), [0, 0.1, 0, 1.5, -1.0, -2.5, -3.0]),
    ]
    for k, (col, head, body, path) in enumerate(cases):
        x = 28 + k * 308
        panel(s, x, 90, 290, 330, head, col)
        P = Plot(s, x + 20, 150, 250, 160, 6, -3.5, 3.5)
        s.line(P.X(2.5), 140, P.X(2.5), 320, C["amber"], 1.2, "3 3")
        s.text(P.X(2.5) + 4, 148, "08:30", 11, C["amber"], weight=700)
        P.path(list(enumerate(path)), col, 2.6)
        s.text(x + 18, 350, body, 13, C["text"])
    return s.render()


# ---------------------------------------------------------------- 10.4
@fig
def intermarket(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Intermarket relationships (typical, not fixed)", "ความสัมพันธ์ระหว่างตลาด (ทั่วไป ไม่ตายตัว)"),
            t("Relationships change with the regime, especially with inflation. Check, don't assume.",
              "ความสัมพันธ์เปลี่ยนตามสภาวะ โดยเฉพาะเงินเฟ้อ ตรวจสอบเสมอ อย่าสมมติเอา"))
    rels = [
        (C["blue"], t("Stronger US dollar", "ดอลลาร์สหรัฐแข็งค่า"), t("→ often weaker commodities (priced in $)\n→ pressure on emerging markets incl. Thailand", "→ สินค้าโภคภัณฑ์มักอ่อน (ราคาเป็น $)\n→ กดดันตลาดเกิดใหม่ รวมถึงไทย")),
        (C["teal"], t("Higher real bond yields", "ผลตอบแทนพันธบัตรแท้จริงสูงขึ้น"), t("→ lower stock valuations, esp. growth stocks\n→ often a stronger dollar", "→ มูลค่าหุ้นลดลง โดยเฉพาะหุ้นเติบโต\n→ ดอลลาร์มักแข็งขึ้น")),
        (C["amber"], t("Oil / commodities up", "น้ำมัน / โภคภัณฑ์ขึ้น"), t("→ inflation expectations up → yields up\n→ helps energy stocks, hurts importers", "→ คาดการณ์เงินเฟ้อขึ้น → ผลตอบแทนขึ้น\n→ หนุนหุ้นพลังงาน กระทบผู้นำเข้า")),
        (C["pink"], t("Gold", "ทองคำ"), t("→ often rises when real yields and the $ fall\n→ a fear / currency-debasement hedge", "→ มักขึ้นเมื่อผลตอบแทนแท้จริงและ $ ลดลง\n→ เครื่องป้องกันความกลัว / ค่าเงินเสื่อม")),
        (C["bull"], t("Stocks vs bonds", "หุ้น vs พันธบัตร"), t("→ low inflation: often move opposite (bonds hedge)\n→ high inflation: can fall together (e.g. 2022)", "→ เงินเฟ้อต่ำ: มักเคลื่อนสวนกัน (พันธบัตรป้องกัน)\n→ เงินเฟ้อสูง: ลงพร้อมกันได้ (เช่น ปี 2022)")),
        (C["purple"], t("Risk-off shock", "ภาวะหนีความเสี่ยง"), t("→ stocks, EM, crypto down; $, yen, US bonds\n   often bid (flight to safety)", "→ หุ้น ตลาดเกิดใหม่ คริปโต ลง $ เยน พันธบัตรสหรัฐฯ\n   มักมีแรงซื้อ (หนีไปหาที่ปลอดภัย)")),
    ]
    for k, (col, head, body) in enumerate(rels):
        x = 28 + (k % 2) * 460
        y = 92 + (k // 2) * 132
        s.card(x, y, 444, 120, head, body, col, 16, 13)
    return s.render()


# ---------------------------------------------------------------- 10.5
@fig
def wall_street(lang):
    t = tr(lang)
    s = SVG(960, 500, t("How Wall Street fits together", "วอลล์สตรีทประกอบกันอย่างไร"),
            t("The sell side makes markets and sells services; the buy side manages money. Everyone needs liquidity.",
              "ฝั่ง Sell Side สร้างตลาดและขายบริการ ฝั่ง Buy Side บริหารเงิน ทุกคนต้องการสภาพคล่อง"))
    cols = [
        (28, C["purple"], t("ISSUERS", "ผู้ออกหลักทรัพย์"), [t("Companies", "บริษัท"), t("Governments", "รัฐบาล")], t("need capital", "ต้องการทุน")),
        (260, C["blue"], t("SELL SIDE", "SELL SIDE"), [t("Investment banks (IPOs, M&A)", "วาณิชธนกิจ (IPO, M&A)"), t("Brokers & research", "โบรกเกอร์ & บทวิเคราะห์"), t("Market makers / dealers", "มาร์เก็ตเมกเกอร์ / ดีลเลอร์")], t("earn fees & spreads", "ได้ค่าธรรมเนียม & ส่วนต่าง")),
        (492, C["amber"], t("MARKETS", "ตลาด"), [t("Exchanges (NYSE, CME…)", "ตลาดหลักทรัพย์ (NYSE, CME…)"), t("Dark pools / OTC", "Dark Pool / OTC"), t("Clearing houses", "สำนักหักบัญชี")], t("match & settle", "จับคู่ & ชำระราคา")),
        (724, C["bull"], t("BUY SIDE", "BUY SIDE"), [t("Pension & sovereign funds", "กองทุนบำนาญ & กองทุนรัฐ"), t("Mutual funds & ETFs", "กองทุนรวม & ETF"), t("Hedge funds, CTAs", "เฮดจ์ฟันด์, CTA"), t("Retail (you)", "รายย่อย (คุณ)")], t("invest & speculate", "ลงทุน & เก็งกำไร")),
    ]
    for k, (x, col, head, items, foot) in enumerate(cols):
        s.rect(x, 100, 208, 300, fill=C["panel"], stroke=col, rx=12)
        s.text(x + 104, 130, head, 15, col, "middle", 700)
        for j, it in enumerate(items):
            s.rect(x + 12, 150 + j * 52, 184, 42, fill=col, opacity=0.12, rx=8)
            s.text(x + 104, 176 + j * 52, it, 12, C["text"], "middle")
        s.text(x + 104, 385, foot, 12, C["muted"], "middle", 700)
        if k < 3:
            s.arrow(x + 210, 250, x + 256, 250, C["muted"], 2)
    s.text(48, 440, t("Conflicts of interest exist everywhere: research sells, banks underwrite, brokers profit from activity.",
                      "ผลประโยชน์ทับซ้อนมีอยู่ทุกที่: บทวิเคราะห์ช่วยขาย ธนาคารรับประกันการจำหน่าย โบรกเกอร์ได้กำไรจากการซื้อขาย"),
           13, C["amber"], weight=600)
    s.text(48, 465, t("Ask of every message: who is paying for this, and what do they want me to do?",
                      "ถามทุกข้อความ: ใครจ่ายเงินให้สิ่งนี้ และเขาอยากให้ฉันทำอะไร?"), 13, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 10.6
@fig
def dcf_chart(lang):
    t = tr(lang)
    s = SVG(960, 480, t("Valuation: a business is worth its future cash, discounted", "การประเมินมูลค่า: ธุรกิจมีค่าเท่ากับเงินสดในอนาคตที่คิดลดแล้ว"),
            t("Free cash flow 100, growing 5% for 10 years, then 2% forever. Same company, two discount rates.",
              "กระแสเงินสดอิสระ 100 เติบโต 5% เป็นเวลา 10 ปี แล้ว 2% ตลอดไป บริษัทเดียวกัน อัตราคิดลดสองแบบ"))
    for k, (r, col) in enumerate(((0.08, C["bull"]), (0.10, C["bear"]))):
        flows, tv, total = dcf(r=r)
        x = 28 + k * 460
        panel(s, x, 90, 444, 370, t(f"Discount rate {r:.0%}", f"อัตราคิดลด {r:.0%}"), col)
        mx = 220
        for i, f in enumerate(flows):
            h = 200 * f / mx
            s.rect(x + 24 + i * 21, 360 - h, 16, h, fill=col, opacity=0.75, rx=2)
        s.text(x + 30, 380, t("PV of years 1–10", "มูลค่าปัจจุบันปี 1–10"), 11, C["muted"])
        s.text(x + 345, 150, t("Terminal value (PV)", "มูลค่าปลายทาง (PV)"), 12, C["muted"], "middle")
        s.text(x + 345, 175, f"{tv:,.0f}", 20, col, "middle", 700)
        s.text(x + 345, 230, t("Total value", "มูลค่ารวม"), 12, C["muted"], "middle")
        s.text(x + 345, 262, f"{total:,.0f}", 28, C["text"], "middle", 700)
        s.text(x + 345, 290, t(f"= {total / 100:.0f}× today's cash flow", f"= {total / 100:.0f} เท่าของกระแสเงินสดวันนี้"), 12, C["muted"], "middle")
        s.text(x + 18, 420, t(f"Sum of years 1–10: {sum(flows):,.0f} ({sum(flows) / total:.0%} of value)",
                              f"รวมปี 1–10: {sum(flows):,.0f} ({sum(flows) / total:.0%} ของมูลค่า)"), 13, C["text"])
    return s.render()


# ---------------------------------------------------------------- 10.7
@fig
def allocation(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Stock/bond mixes: return vs risk", "สัดส่วนหุ้น/พันธบัตร: ผลตอบแทน vs ความเสี่ยง"),
            t("Assumed long-run: stocks 7% return / 16% vol, bonds 3% / 6%, correlation 0.1. Illustrative, not a forecast.",
              "สมมติระยะยาว: หุ้นผลตอบแทน 7% / ผันผวน 16% พันธบัตร 3% / 6% สหสัมพันธ์ 0.1 เป็นตัวอย่าง ไม่ใช่การพยากรณ์"))
    panel(s, 28, 90, 620, 390)
    X = lambda v: 90 + 520 * (v - 0.04) / 0.14
    Y = lambda r: 120 + 300 * (0.08 - r) / 0.06
    for v in (0.04, 0.08, 0.12, 0.16):
        s.line(X(v), 120, X(v), 420, C["grid"], 1)
        s.text(X(v), 440, f"{v:.0%}", 11, C["muted"], "middle")
    for r in (0.02, 0.04, 0.06, 0.08):
        s.line(90, Y(r), 610, Y(r), C["grid"], 1)
        s.text(84, Y(r) + 4, f"{r:.0%}", 11, C["muted"], "end")
    pts = [(w / 20, *mix(w / 20)) for w in range(21)]
    s.polyline([(X(v), Y(r)) for _, r, v in pts], C["blue"], 2.5)
    for w, lab in ((0, "0/100"), (0.4, "40/60"), (0.6, "60/40"), (0.8, "80/20"), (1.0, "100/0")):
        r, v = mix(w)
        s.circle(X(v), Y(r), 6, C["amber"])
        s.text(X(v) + (10 if w < 1 else -10), Y(r) + (4 if w < 1 else -10), f"{lab}  {r:.1%} / {v:.1%}", 12, C["text"], "start" if w < 1 else "end", 700)
    s.text(350, 465, t("volatility (risk) →", "ความผันผวน (ความเสี่ยง) →"), 12, C["muted"], "middle")
    s.text(40, 112, t("expected return ↑", "ผลตอบแทนคาดหวัง ↑"), 12, C["muted"])
    s.card(668, 92, 264, 180, t("Read it", "อ่านอย่างไร"),
           t("Adding a little of a\nlow-correlated asset cuts\nrisk faster than return:\ndiversification.\nLabels = stocks/bonds %.", "เพิ่มสินทรัพย์ที่สหสัมพันธ์ต่ำ\nเล็กน้อยช่วยลดความเสี่ยง\nได้เร็วกว่าลดผลตอบแทน:\nการกระจายความเสี่ยง\nป้าย = % หุ้น/พันธบัตร"), C["blue"], 16, 13)
    s.card(668, 286, 264, 194, t("Real drawdowns (S&P 500)", "Drawdown จริง (S&P 500)"),
           t("2000–02: about −49%\n2007–09: about −57%\n2020: about −34%\n2022: about −25%\nCan you hold through these?", "2000–02: ประมาณ −49%\n2007–09: ประมาณ −57%\n2020: ประมาณ −34%\n2022: ประมาณ −25%\nคุณถือผ่านช่วงเหล่านี้ได้ไหม?"), C["bear"], 16, 13)
    return s.render()


@fig
def compounding(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Time and cost: the quiet giants of investing", "เวลาและค่าใช้จ่าย: ยักษ์เงียบของการลงทุน"),
            t("Investing 10,000 THB a month for 30 years at a 6% annual return, with different yearly fees.",
              "ลงทุนเดือนละ 10,000 บาท เป็นเวลา 30 ปี ผลตอบแทน 6% ต่อปี ด้วยค่าธรรมเนียมรายปีต่างกัน"))
    panel(s, 28, 90, 904, 330)
    P = Plot(s, 100, 120, 600, 260, 30, 0, 10.5e6)
    for v in (0, 2.5e6, 5e6, 7.5e6, 10e6):
        s.line(100, P.Y(v), 700, P.Y(v), C["grid"], 1)
        s.text(94, P.Y(v) + 4, f"{v / 1e6:.1f}M", 11, C["muted"], "end")
    finals = []
    for fee, col in ((0.002, C["bull"]), (0.01, C["amber"]), (0.02, C["bear"])):
        bal, pts = 0.0, [(0, 0)]
        m = (1 + 0.06 - fee) ** (1 / 12) - 1
        for month in range(1, 361):
            bal = bal * (1 + m) + 10000
            if month % 12 == 0:
                pts.append((month // 12, bal))
        P.path(pts, col, 2.6)
        finals.append((fee, bal, col))
    contrib = [(y, 120000 * y) for y in range(31)]
    P.path(contrib, C["dim"], 1.8, "5 4")
    for k, (fee, bal, col) in enumerate(finals):
        s.text(720, 160 + k * 50, t(f"fee {fee:.1%}: {bal / 1e6:.2f}M THB", f"ค่าธรรมเนียม {fee:.1%}: {bal / 1e6:.2f} ล้านบาท"), 14, col, weight=700)
    s.text(720, 320, t("dashed: money you put in\n(3.6M THB)", "เส้นประ: เงินที่คุณใส่เข้าไป\n(3.6 ล้านบาท)"), 13, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 10.8
@fig
def summary(lang):
    t = tr(lang)
    s = SVG(960, 560, t("Phase 10 on one page", "สรุปเฟส 10 ในหน้าเดียว"))
    cx, cy = 480, 310
    nodes = [
        (170, 140, C["bull"], t("10.1–10.2 Cycle & policy", "10.1–10.2 วัฏจักร & นโยบาย"), t("Where are we in the cycle?\nWhat is the central bank doing?", "เราอยู่ช่วงไหนของวัฏจักร?\nธนาคารกลางทำอะไรอยู่?")),
        (790, 140, C["amber"], t("10.3 Data & events", "10.3 ข้อมูล & เหตุการณ์"), t("Surprise vs expectation.\nNo new trades into big news.", "ความประหลาดใจ vs ความคาดหวัง\nไม่เปิดไม้ใหม่ก่อนข่าวใหญ่")),
        (150, 320, C["blue"], t("10.4 Intermarket", "10.4 ระหว่างตลาด"), t("Dollar, yields, oil, gold.\nRelationships shift.", "ดอลลาร์ ผลตอบแทน น้ำมัน ทอง\nความสัมพันธ์เปลี่ยนได้")),
        (810, 320, C["purple"], t("10.5 Wall Street", "10.5 วอลล์สตรีท"), t("Sell side vs buy side.\nFollow the incentives.", "Sell Side vs Buy Side\nดูแรงจูงใจ")),
        (250, 480, C["teal"], t("10.6 Valuation", "10.6 การประเมินมูลค่า"), t("Cash flows, discounted.\nRates drive multiples.", "กระแสเงินสดที่คิดลด\nดอกเบี้ยขับเคลื่อนมูลค่า")),
        (710, 480, C["pink"], t("10.7 Portfolio", "10.7 พอร์ตลงทุน"), t("Diversify, keep costs low,\nhold through drawdowns.", "กระจายความเสี่ยง ค่าใช้จ่ายต่ำ\nถือผ่าน Drawdown")),
    ]
    for x, y, col, head, body in nodes:
        s.line(cx, cy, x, y, col, 2, opacity=0.5)
    s.circle(cx, cy, 74, C["panel"], C["text"], 2)
    s.text(cx, cy - 4, t("PHASE 10", "เฟส 10"), 20, C["text"], "middle", 700)
    s.text(cx, cy + 20, t("Macro & Investing", "มหภาค & ลงทุน"), 14, C["muted"], "middle")
    for x, y, col, head, body in nodes:
        s.rect(x - 140, y - 42, 280, 92, fill=C["panel"], stroke=col, rx=12)
        s.text(x, y - 14, head, 15, col, "middle", 700)
        s.text(x, y + 10, body, 12, C["text"], "middle")
    return s.render()


# ================================================================ v2 additions (Oct 2026)
@fig
def pmi_gauge(lang):
    t = tr(lang)
    s = SVG(960, 440, t("How a PMI number is made", "ตัวเลข PMI สร้างขึ้นอย่างไร"),
            t("Purchasing managers answer: better, same or worse than last month? PMI = % better + ½ × % same.",
              "ผู้จัดการฝ่ายจัดซื้อตอบว่า: ดีขึ้น เท่าเดิม หรือแย่ลงกว่าเดือนก่อน? PMI = % ดีขึ้น + ½ × % เท่าเดิม"))
    surveys = [(t("Month A", "เดือน A"), 30, 40, 30), (t("Month B", "เดือน B"), 25, 40, 35), (t("Month C", "เดือน C"), 35, 45, 20)]
    for k, (name, b, sm, w) in enumerate(surveys):
        y = 110 + k * 90
        s.text(48, y + 32, name, 15, C["text"], weight=700)
        x = 160
        for val, col in ((b, C["bull"]), (sm, C["muted"]), (w, C["bear"])):
            s.rect(x, y + 10, val * 4.4, 36, fill=col, opacity=0.8)
            s.text(x + val * 2.2, y + 34, f"{val}%", 13, C["white"], "middle", 700)
            x += val * 4.4
        pmi = b + 0.5 * sm
        col = C["bull"] if pmi > 50 else (C["bear"] if pmi < 50 else C["amber"])
        s.text(640, y + 34, f"{b} + ½ × {sm} =", 14, C["muted"])
        s.text(800, y + 36, f"{pmi:g}", 26, col, weight=800)
    s.text(160, 104, t("better", "ดีขึ้น"), 12, C["bull"], weight=700)
    s.text(300, 104, t("same", "เท่าเดิม"), 12, C["muted"], weight=700)
    s.text(470, 104, t("worse", "แย่ลง"), 12, C["bear"], weight=700)
    s.rect(28, 380, 904, 44, fill=C["panel"], stroke=C["border"], rx=10)
    s.text(48, 408, t("Above 50 = more firms say business is improving (expansion). Below 50 = contraction. The direction matters too.",
                      "เหนือ 50 = บริษัทส่วนใหญ่บอกว่าธุรกิจดีขึ้น (ขยายตัว) ต่ำกว่า 50 = หดตัว ทิศทางก็สำคัญด้วย"), 13, C["amber"], weight=600)
    return s.render()


@fig
def duration(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Duration: how much a bond falls when yields rise", "Duration: พันธบัตรร่วงเท่าไหร่เมื่อผลตอบแทนขึ้น"),
            t("Rule of thumb: price change ≈ −duration × yield change. Here yields rise by 0.5 percentage points.",
              "กฎง่าย ๆ: ราคาเปลี่ยน ≈ −Duration × ผลตอบแทนที่เปลี่ยน ที่นี่ผลตอบแทนขึ้น 0.5 จุดเปอร์เซ็นต์"))
    rows = [(t("2-year bond", "พันธบัตร 2 ปี"), 2, C["teal"]), (t("10-year bond", "พันธบัตร 10 ปี"), 8, C["amber"]), (t("30-year bond", "พันธบัตร 30 ปี"), 17, C["bear"])]
    for k, (name, d, col) in enumerate(rows):
        y = 120 + k * 80
        s.text(48, y + 30, name, 16, col, weight=700)
        s.text(48, y + 52, t(f"duration ≈ {d}", f"Duration ≈ {d}"), 13, C["muted"])
        loss = d * 0.5
        s.rect(300, y + 10, loss * 50, 40, fill=col, opacity=0.8, rx=5)
        s.text(300 + loss * 50 + 12, y + 36, f"≈ −{loss:g}%", 18, col, weight=800)
    s.rect(28, 370, 904, 50, fill=C["panel"], stroke=C["border"], rx=10)
    s.text(48, 400, t("Long-duration assets (long bonds, growth stocks) are the most sensitive to interest rates.",
                      "สินทรัพย์ที่มี Duration ยาว (พันธบัตรระยะยาว หุ้นเติบโต) ไวต่อดอกเบี้ยมากที่สุด"), 14, C["amber"], weight=600)
    return s.render()


@fig
def gap_risk(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Event gap risk: sizing so a gap costs at most 2R", "ความเสี่ยงจาก Gap ช่วงข่าว: คำนวณขนาดให้ Gap เสียไม่เกิน 2R"),
            t("EUR/USD long, account 10,000 USD, 1R = 100 USD, stop 20 pips. A news gap can fill 50 pips away.",
              "Long EUR/USD บัญชี 10,000 ดอลลาร์ 1R = 100 ดอลลาร์ Stop 20 pip ข่าวอาจทำให้ได้ราคาห่างไป 50 pip"))
    for k, (title, lots, col) in enumerate(((t("Normal size: 0.5 lot", "ขนาดปกติ: 0.5 ล็อต"), 0.5, C["bear"]), (t("Event size: 0.4 lot", "ขนาดช่วงข่าว: 0.4 ล็อต"), 0.4, C["bull"]))):
        bx = 28 + k * 462
        panel(s, bx, 90, 442, 320, title, col, 16)
        planned = lots * 10 * 20
        gap = lots * 10 * 50
        for j, (lab, val) in enumerate(((t("stop hit normally (20 pips)", "โดน Stop ปกติ (20 pip)"), planned), (t("filled after a 50-pip gap", "ได้ราคาหลัง Gap 50 pip"), gap))):
            y = 150 + j * 100
            s.text(bx + 20, y, lab, 13, C["muted"])
            s.rect(bx + 20, y + 12, val * 0.95, 34, fill=col if j else C["dim"], opacity=0.85, rx=5)
            s.text(bx + 30 + val * 0.95, y + 36, f"−{val:g} USD = {val / 100:g}R", 15, C["text"], weight=700)
        s.text(bx + 20, 380, t("too much: a gap costs 2.5R" if k == 0 else "gap capped at 2R; normal stop = 0.8R", "มากไป: Gap ทำให้เสีย 2.5R" if k == 0 else "Gap ถูกจำกัดที่ 2R Stop ปกติ = 0.8R"), 14, col, weight=700)
    return s.render()


@fig
def fx_effect(lang):
    t = tr(lang)
    s = SVG(960, 420, t("Currency effect for a Thai investor in US stocks", "ผลของค่าเงินต่อนักลงทุนไทยในหุ้นสหรัฐ"),
            t("The US stock rises 10% in dollars. What you get in baht depends on USD/THB (illustrative rates).",
              "หุ้นสหรัฐขึ้น 10% เป็นดอลลาร์ สิ่งที่คุณได้เป็นบาทขึ้นกับ USD/THB (อัตราตัวอย่าง)"))
    cases = [(t("Baht stable", "บาทคงที่"), "36.0 → 36.0", 10.0, C["blue"]), (t("Baht strengthens 10%", "บาทแข็ง 10%"), "36.0 → 32.4", -1.0, C["bear"]),
             (t("Baht weakens 10%", "บาทอ่อน 10%"), "36.0 → 39.6", 21.0, C["bull"])]
    zero = 480
    s.line(zero, 100, zero, 340, C["dim"], 1.5)
    for k, (name, rate, ret, col) in enumerate(cases):
        y = 120 + k * 72
        s.text(48, y + 22, name, 15, col, weight=700)
        s.text(48, y + 44, "USD/THB " + rate, 12, C["muted"])
        w = ret * 16
        s.rect(min(zero, zero + w), y + 6, abs(w), 40, fill=col, opacity=0.85, rx=4)
        s.text(zero + w + (10 if w >= 0 else -10), y + 32, f"{ret:+g}% " + t("in THB", "เป็นบาท"), 15, col, "start" if w >= 0 else "end", 700)
    s.text(48, 380, t("Formula: return in THB = (1 + stock return) × (new rate ÷ old rate) − 1", "สูตร: ผลตอบแทนเป็นบาท = (1 + ผลตอบแทนหุ้น) × (อัตราใหม่ ÷ อัตราเดิม) − 1"), 14, C["amber"], weight=600)
    return s.render()


@fig
def inclusion_flow(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Index inclusion: a forced, scheduled flow (illustrative)", "การเข้าดัชนี: กระแสเงินที่ถูกบังคับและมีกำหนดการ (ภาพประกอบ)"),
            t("Index funds hold ~15% of each member. A 10 bn USD company joins at the close on day 10.",
              "กองทุนดัชนีถือราว 15% ของแต่ละสมาชิก บริษัทมูลค่า 10 พันล้านดอลลาร์เข้าดัชนีตอนปิดวันที่ 10"))
    P = Plot(s, 90, 110, 560, 240, 14, 96, 116)
    path = [(0, 100), (1, 100.3), (2, 106), (3, 106.8), (4, 107.2), (5, 108), (6, 108.6), (7, 109.5), (8, 110.4), (9, 111.5), (10, 113), (11, 110.2), (12, 109.3), (13, 108.9), (14, 108.5)]
    for v in range(96, 117, 4):
        s.line(90, P.Y(v), 650, P.Y(v), C["grid"], 1)
    P.path(path, C["blue"], 3)
    for i, txt, col, up in ((2, t("announcement: +6%", "ประกาศ: +6%"), C["bull"], True), (10, t("inclusion close:\nforced buying peaks", "ปิดวันเข้าดัชนี:\nแรงซื้อบังคับสูงสุด"), C["amber"], True),
                            (13, t("gives back after", "คืนกำไรหลังจากนั้น"), C["bear"], False)):
        p = dict(path)[i]
        s.circle(P.X(i), P.Y(p), 6, col)
        s.text(P.X(i), P.Y(p) + (-(16 + 16 * txt.count(chr(10))) if up else 28), txt, 12, col, "middle", 700)
    for d in (0, 5, 10, 14):
        s.text(P.X(d), 372, t(f"day {d}", f"วันที่ {d}"), 12, C["muted"], "middle")
    rows = [(t("Company value", "มูลค่าบริษัท"), "10 bn USD"), (t("Index funds must own", "กองทุนดัชนีต้องถือ"), "15% = 1.5 bn"),
            (t("Normal daily volume", "วอลุ่มปกติต่อวัน"), "200 m USD"), (t("Forced buying =", "แรงซื้อบังคับ ="), t("7.5 days of volume", "วอลุ่ม 7.5 วัน"))]
    for k, (a, b) in enumerate(rows):
        s.text(690, 140 + k * 60, a, 13, C["muted"], weight=600)
        s.text(690, 164 + k * 60, b, 16, C["text"], weight=700)
    return s.render()


@fig
def ev_bridge(lang):
    t = tr(lang)
    s = SVG(960, 460, t("Enterprise value: same market cap, different companies", "Enterprise value: มูลค่าตลาดเท่ากัน แต่บริษัทต่างกัน"),
            t("EV = market cap + debt − cash. Both earn EBITDA of 1.2 bn (illustrative, in bn USD).",
              "EV = มูลค่าตลาด + หนี้ − เงินสด ทั้งคู่มี EBITDA 1.2 พันล้าน (ตัวอย่าง หน่วยพันล้านดอลลาร์)"))
    for k, (name, mc, debt, cash, col) in enumerate(((t("Company A", "บริษัท A"), 10, 0, 1, C["bull"]), (t("Company B", "บริษัท B"), 10, 6, 0, C["bear"]))):
        bx = 28 + k * 462
        panel(s, bx, 90, 442, 350, name, col, 17)
        sc = 13
        x = bx + 40
        base = 400
        s.rect(x, base - mc * sc, 70, mc * sc, fill=C["blue"], opacity=0.8, rx=4)
        s.text(x + 35, base + 20, t("market cap", "มูลค่าตลาด"), 11, C["muted"], "middle")
        s.text(x + 35, base - mc * sc - 8, f"{mc}", 13, C["text"], "middle", 700)
        x += 100
        s.rect(x, base - (mc + debt) * sc, 70, debt * sc, fill=C["bear"], opacity=0.8, rx=4)
        s.text(x + 35, base + 20, t("+ debt", "+ หนี้"), 11, C["muted"], "middle")
        s.text(x + 35, base - (mc + debt) * sc - 8, f"+{debt}" if debt else "0", 13, C["text"], "middle", 700)
        x += 100
        if cash:
            s.rect(x, base - (mc + debt) * sc, 70, cash * sc, fill=C["bull"], opacity=0.8, rx=4)
        s.text(x + 35, base + 20, t("− cash", "− เงินสด"), 11, C["muted"], "middle")
        s.text(x + 35, base - (mc + debt) * sc - 8, f"−{cash}" if cash else "0", 13, C["text"], "middle", 700)
        ev = mc + debt - cash
        s.text(bx + 360, 160, "EV", 14, C["muted"], "middle", 700)
        s.text(bx + 360, 200, f"{ev}", 34, col, "middle", 800)
        s.text(bx + 360, 250, "EV/EBITDA", 13, C["muted"], "middle", 700)
        s.text(bx + 360, 285, f"{ev / 1.2:.1f}×", 26, col, "middle", 800)
    return s.render()


@fig
def rebalance(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Rebalancing a 60/40 portfolio after a stock rally", "ปรับสมดุลพอร์ต 60/40 หลังหุ้นขึ้นแรง"),
            t("Start 100 (60 stocks + 40 bonds). Stocks +25%, bonds flat. Rebalance back to 60/40.",
              "เริ่ม 100 (หุ้น 60 + พันธบัตร 40) หุ้น +25% พันธบัตรเท่าเดิม ปรับกลับเป็น 60/40"))
    cols = [(t("Start", "เริ่ม"), 60, 40), (t("After the rally", "หลังหุ้นขึ้น"), 75, 40), (t("After rebalancing", "หลังปรับสมดุล"), 69, 46)]
    for k, (name, st, bd) in enumerate(cols):
        x = 120 + k * 260
        base = 380
        sc = 2.2
        s.rect(x, base - st * sc, 120, st * sc, fill=C["blue"], opacity=0.85, rx=4)
        s.rect(x, base - (st + bd) * sc, 120, bd * sc, fill=C["amber"], opacity=0.85, rx=4)
        tot = st + bd
        s.text(x + 60, base - st * sc / 2 + 5, t(f"stocks {st:g}", f"หุ้น {st:g}"), 14, C["white"], "middle", 700)
        s.text(x + 60, base - st * sc - bd * sc / 2 + 5, t(f"bonds {bd:g}", f"พันธบัตร {bd:g}"), 14, C["bg"], "middle", 700)
        s.text(x + 60, base + 22, name, 14, C["text"], "middle", 700)
        s.text(x + 60, base - tot * sc - 10, f"{st / tot:.0%} / {bd / tot:.0%}", 13, C["muted"], "middle", 700)
    s.arrow(510, 220, 630, 220, C["bull"], 2)
    s.text(570, 180, t("sell 6 stocks,\nbuy 6 bonds", "ขายหุ้น 6\nซื้อพันธบัตร 6"), 12, C["bull"], "middle", 700)
    return s.render()
