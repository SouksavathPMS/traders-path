"""Phase 10 investing add-on figures (C4: lessons 10.9-10.14).
Market data comes from _tools/investing/data/ (see fetch_investing.py); every number is computed in
_tools/investing/analysis.py, which these figures import.
"""
import math
import sys
from pathlib import Path
from charts import SVG, C, tr

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "investing"))
import analysis as A  # noqa: E402

FIGURES = {}


def fig(fn):
    FIGURES["p10-" + fn.__name__.replace("_", "-")] = fn
    return fn


def panel(s, x, y, w, h):
    s.rect(x, y, w, h, fill=C["panel"], stroke=C["border"], rx=12)


def fmt(v):
    return f"{v:,.0f}"


class Box:
    """Linear (or log) value->pixel mapper."""

    def __init__(self, x, y, w, h, x0, x1, y0, y1, log=False):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.x0, self.x1, self.log = x0, x1, log
        self.y0, self.y1 = (math.log10(y0), math.log10(y1)) if log else (y0, y1)

    def X(self, v):
        return self.x + self.w * (v - self.x0) / (self.x1 - self.x0)

    def Y(self, v):
        v = math.log10(v) if self.log else v
        return self.y + self.h * (self.y1 - v) / (self.y1 - self.y0)


def month_index(d, base):
    return A.months_between(base, d)


# ---------------------------------------------------------------- 10.9 Index funds & ETFs
@fig
def index_basket(lang):
    t = tr(lang)
    s = SVG(960, 470, t("One fund, the whole market", "กองทุนเดียว ได้ทั้งตลาด"),
            t("An index fund copies a list of companies (the index) instead of trying to pick winners.",
              "กองทุนดัชนีลอกรายชื่อบริษัทตามดัชนี แทนที่จะพยายามเลือกหุ้นผู้ชนะ"))
    # left: picking stocks
    panel(s, 28, 96, 430, 350)
    s.text(48, 128, t("Picking stocks yourself", "เลือกหุ้นเอง"), 17, C["amber"], weight=700)
    for k, (nm, col) in enumerate([("A", C["bull"]), ("B", C["bear"]), ("C", C["bull"]), ("D", C["bear"]), ("E", C["bear"])]):
        s.rect(60 + k * 76, 150, 60, 60, fill=col, opacity=0.25, stroke=col, rx=8)
        s.text(90 + k * 76, 188, nm, 20, col, "middle", 700)
    s.text(48, 248, t("• 5–20 companies\n• one bad pick hurts a lot\n• needs research and time\n• you pay trading costs each switch",
                      "• 5–20 บริษัท\n• เลือกผิดตัวเดียวเจ็บมาก\n• ต้องใช้การวิเคราะห์และเวลา\n• เสียค่าซื้อขายทุกครั้งที่เปลี่ยน"), 15, C["text"])
    # right: index fund grid
    panel(s, 502, 96, 430, 350)
    s.text(522, 128, t("Index fund / ETF", "กองทุนดัชนี / ETF"), 17, C["bull"], weight=700)
    for r in range(5):
        for c in range(20):
            col = C["bull"] if (r * 20 + c) % 3 else C["bear"]
            s.rect(524 + c * 19.5, 146 + r * 14, 15, 10, fill=col, opacity=0.55, rx=2)
    s.text(522, 238, t("• hundreds or thousands of companies\n• winners and losers average out\n• rules decide what's held: no stock picking\n• costs as low as a few hundredths of 1% a year",
                       "• หลายร้อยหรือหลายพันบริษัท\n• ตัวชนะและตัวแพ้เฉลี่ยกัน\n• กฎกำหนดว่าถืออะไร: ไม่ต้องเลือกหุ้น\n• ค่าใช้จ่ายต่ำได้ถึงไม่กี่ส่วนร้อยของ 1% ต่อปี"), 15, C["text"])
    s.text(522, 400, t("You get the market's return, minus a small fee.", "คุณได้ผลตอบแทนของตลาด หักค่าธรรมเนียมเล็กน้อย"), 14, C["teal"], weight=700)
    return s.render()


@fig
def fee_drag(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Small fees, big difference: 1,000,000 over 30 years", "ค่าธรรมเนียมเล็ก ผลต่างใหญ่: 1,000,000 ใน 30 ปี"),
            t("Same 7% a year before fees; only the yearly fee changes. Illustrative return, not a forecast.",
              "ผลตอบแทนก่อนค่าธรรมเนียม 7% ต่อปีเท่ากัน ต่างกันแค่ค่าธรรมเนียมรายปี ตัวเลขสมมติ ไม่ใช่การพยากรณ์"))
    panel(s, 28, 92, 904, 390)
    B = Box(110, 120, 600, 320, 0, 30, 0, 8_000_000)
    for v in range(0, 8_000_001, 2_000_000):
        s.line(B.X(0), B.Y(v), B.X(30), B.Y(v), C["grid"], 1)
        s.text(B.X(0) - 8, B.Y(v) + 4, f"{v/1e6:.0f}M", 12, C["muted"], "end")
    for yr in range(0, 31, 5):
        s.text(B.X(yr), 462, t(f"yr {yr}", f"ปี {yr}"), 12, C["muted"], "middle")
    cols = {0.0005: C["bull"], 0.005: C["amber"], 0.015: C["bear"]}
    end = A.fee_drag()
    for f, col in cols.items():
        pts = [(B.X(y), B.Y(1_000_000 * ((1.07) * (1 - f)) ** y)) for y in range(31)]
        s.polyline(pts, col, 3)
    ys = [150, 230, 330]
    for (f, col), y in zip(cols.items(), ys):
        s.text(730, y, t(f"fee {f*100:.2f}%", f"ค่าธรรมเนียม {f*100:.2f}%"), 15, col, weight=700)
        s.text(730, y + 22, fmt(end[f]), 20, col, weight=700)
    lost = end[0.0005] - end[0.015]
    s.text(730, 410, t(f"Gap: {fmt(lost)}", f"ส่วนต่าง: {fmt(lost)}"), 14, C["text"], weight=700)
    s.text(730, 430, t("paid away in fees", "จ่ายออกไปเป็นค่าธรรมเนียม"), 13, C["muted"])
    return s.render()


@fig
def spiva(lang):
    t = tr(lang)
    s = SVG(960, 470, t("How many professional funds lose to the index?", "กองทุนมืออาชีพแพ้ดัชนีกี่เปอร์เซ็นต์?"),
            t("Share of active US large-cap funds that returned less than the S&P 500 (SPIVA U.S. Scorecard).",
              "สัดส่วนกองทุนหุ้นใหญ่สหรัฐฯ แบบบริหารเชิงรุกที่ได้ผลตอบแทนน้อยกว่า S&P 500 (SPIVA U.S. Scorecard)"))
    panel(s, 28, 92, 904, 350)
    data = [(t("1 yr\n(2025)", "1 ปี\n(2025)"), 79.0), (t("5 yr", "5 ปี"), 86.91), (t("10 yr", "10 ปี"), 85.98),
            (t("15 yr", "15 ปี"), 88.29), (t("20 yr", "20 ปี"), 91.03)]
    base, sc = 380, 2.6
    s.line(80, base, 900, base, C["border"], 1.5)
    s.line(80, base - 50 * sc, 900, base - 50 * sc, C["dim"], 1, "5 5")
    s.text(84, base - 50 * sc - 6, t("50%: a coin flip", "50%: เหมือนโยนเหรียญ"), 12, C["muted"])
    for k, (nm, v) in enumerate(data):
        x = 230 + k * 135
        s.rect(x, base - v * sc, 100, v * sc, fill=C["bear"], opacity=0.8, rx=4)
        s.text(x + 50, base - v * sc - 10, f"{v:.0f}%", 18, C["bear"], "middle", 700)
        s.text(x + 50, base + 22, nm, 13, C["text"], "middle", 600)
    s.text(40, 462, t("1-year figure: calendar 2025 (Year-End 2025 report). 5–20 years: periods ending 30 Jun 2025 (Mid-Year 2025 report). Fund returns are after fees.",
                      "ตัวเลข 1 ปี: ปีปฏิทิน 2025 (รายงาน Year-End 2025) 5–20 ปี: ช่วงที่สิ้นสุด 30 มิ.ย. 2025 (รายงาน Mid-Year 2025) ผลตอบแทนกองทุนหลังหักค่าธรรมเนียม"), 11, C["dim"])
    return s.render()


@fig
def etf_checklist(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Choosing an index fund: five checks", "การเลือกกองทุนดัชนี: ตรวจห้าข้อ"),
            t("Compare funds that track the same kind of index; the cheapest well-run one usually wins.",
              "เทียบกองทุนที่ติดตามดัชนีแบบเดียวกัน กองที่ถูกที่สุดและบริหารดีมักชนะ"))
    items = [
        (C["blue"], t("1 · What index?", "1 · ดัชนีอะไร?"), t("World, US, Thai, bonds?\nBroad beats narrow for a core.", "โลก สหรัฐฯ ไทย พันธบัตร?\nแกนหลักควรกว้าง ไม่แคบ")),
        (C["bull"], t("2 · Yearly cost (TER)", "2 · ค่าใช้จ่ายต่อปี (TER)"), t("Lower is better. Compare\nwithin the same index.", "ยิ่งต่ำยิ่งดี เทียบในดัชนี\nเดียวกัน")),
        (C["teal"], t("3 · Tracking difference", "3 · ส่วนต่างการติดตาม"), t("Fund return minus index\nreturn, over several years.", "ผลตอบแทนกองทุนลบผลตอบแทน\nดัชนี ดูหลายปี")),
        (C["amber"], t("4 · Size & trading", "4 · ขนาด & การซื้อขาย"), t("Big funds with tight\nbid–ask spreads cost less.", "กองใหญ่ที่ส่วนต่างราคา\nซื้อ–ขายแคบ เสียต้นทุนน้อยกว่า")),
        (C["purple"], t("5 · Where it's based", "5 · จดทะเบียนที่ไหน"), t("Fund country changes\ndividend tax & estate rules.", "ประเทศของกองทุนเปลี่ยน\nภาษีปันผลและกฎมรดก")),
    ]
    for k, (col, title, body) in enumerate(items):
        x = 28 + (k % 3) * 304
        y = 96 + (k // 3) * 160
        s.card(x, y, 296, 148, title, body, col, 16, 14)
    s.card(636, 256, 296, 148, t("Accumulating vs distributing", "สะสม vs จ่ายปันผล"),
           t("Acc: reinvests dividends.\nDist: pays them to you.\nSame index, different tax.", "สะสม: นำปันผลไปลงทุนต่อ\nจ่าย: จ่ายปันผลให้คุณ\nดัชนีเดียวกัน ภาษีต่างกัน"), C["pink"], 16, 14)
    return s.render()


# ---------------------------------------------------------------- 10.10 DCA vs lump sum
def dca_path(prices, monthly=10_000):
    units = [monthly / p for p in prices]
    return units, sum(units)


@fig
def dca_units(lang):
    t = tr(lang)
    s = SVG(960, 520, t("DCA: the same money buys more units when prices are low", "DCA: เงินเท่าเดิมซื้อได้หลายหน่วยขึ้นเมื่อราคาต่ำ"),
            t("10,000 a month for 6 months (60,000 in total) vs 60,000 invested at once in month 1. Made-up prices.",
              "เดือนละ 10,000 นาน 6 เดือน (รวม 60,000) เทียบกับลง 60,000 ครั้งเดียวในเดือนที่ 1 ราคาสมมติ"))
    paths = [(t("A · price dips, then recovers", "A · ราคาย่อแล้วฟื้น"), [100, 80, 60, 80, 100, 120]),
             (t("B · price rises steadily", "B · ราคาขึ้นต่อเนื่อง"), [100, 110, 120, 130, 140, 150])]
    for k, (name, pr) in enumerate(paths):
        x0 = 28 + k * 466
        panel(s, x0, 92, 438, 408)
        s.text(x0 + 20, 122, name, 16, C["text"], weight=700)
        B = Box(x0 + 50, 150, 360, 140, 0, 5, 40, 160)
        for p in (50, 100, 150):
            s.line(B.X(0), B.Y(p), B.X(5), B.Y(p), C["grid"], 1)
            s.text(B.X(0) - 8, B.Y(p) + 4, str(p), 11, C["muted"], "end")
        s.polyline([(B.X(i), B.Y(p)) for i, p in enumerate(pr)], C["blue"], 3)
        units, tot = dca_path(pr)
        for i, (p, u) in enumerate(zip(pr, units)):
            s.circle(B.X(i), B.Y(p), 4, C["blue"])
            s.text(B.X(i), 316, f"{u:.0f}", 13, C["teal"], "middle", 700)
            s.text(B.X(i), 334, t(f"m{i+1}", f"ด{i+1}"), 11, C["muted"], "middle")
        s.text(x0 + 20, 354, t("green numbers = units bought that month", "ตัวเลขสีเขียว = จำนวนหน่วยที่ซื้อในเดือนนั้น"), 12, C["teal"])
        end = pr[-1]
        dca_v, lump_v = tot * end, 600 * end
        avg_cost, avg_price = 60_000 / tot, sum(pr) / len(pr)
        lines = [
            (t(f"DCA: {tot:.0f} units, average cost {avg_cost:.2f}", f"DCA: {tot:.0f} หน่วย ต้นทุนเฉลี่ย {avg_cost:.2f}"), C["teal"]),
            (t(f"(average price was {avg_price:.0f})", f"(ราคาเฉลี่ยคือ {avg_price:.0f})"), C["muted"]),
            (t(f"Lump sum: 600 units at 100", "ก้อนเดียว: 600 หน่วยที่ 100"), C["amber"]),
            (t(f"Value at {end}: DCA {fmt(dca_v)} · lump {fmt(lump_v)}", f"มูลค่าที่ {end}: DCA {fmt(dca_v)} · ก้อนเดียว {fmt(lump_v)}"), C["text"]),
        ]
        for j, (txt, col) in enumerate(lines):
            s.text(x0 + 20, 384 + j * 24, txt, 14, col, weight=700 if j != 1 else 400)
        win = t("DCA wins" if dca_v > lump_v else "Lump sum wins", "DCA ชนะ" if dca_v > lump_v else "ก้อนเดียวชนะ")
        s.pill(x0 + 360, 122, win, C["teal"] if dca_v > lump_v else C["amber"], 13)
    return s.render()


@fig
def dca_history(lang):
    t = tr(lang)
    res = A.dca_vs_lump()
    wins = sum(1 for _, l, d in res if l > d)
    s = SVG(960, 500, t("Lump sum vs 12-month DCA, S&P 500, every start month 1988–2025", "ก้อนเดียว vs DCA 12 เดือน S&P 500 ทุกเดือนเริ่มต้น 1988–2025"),
            t(f"Bar = lump sum minus DCA after 12 months, % of the money. Lump sum won {wins} of {len(res)} starts ({wins/len(res):.0%}).",
              f"แท่ง = ก้อนเดียวลบ DCA หลัง 12 เดือน เป็น % ของเงิน ก้อนเดียวชนะ {wins} จาก {len(res)} ครั้ง ({wins/len(res):.0%})"))
    panel(s, 28, 92, 904, 370)
    diffs = [((l - d) / 120_000 * 100) for _, l, d in res]
    lo, hi = -35, 40
    B = Box(80, 112, 830, 320, 0, len(res), lo, hi)
    for v in (-30, -20, -10, 0, 10, 20, 30, 40):
        s.line(B.X(0), B.Y(v), B.X(len(res)), B.Y(v), C["border"] if v == 0 else C["grid"], 1.5 if v == 0 else 1)
        s.text(B.X(0) - 8, B.Y(v) + 4, f"{v:+d}%" if v else "0", 11, C["muted"], "end")
    bw = 830 / len(res)
    for i, dv in enumerate(diffs):
        col = C["amber"] if dv > 0 else C["teal"]
        y0, y1 = B.Y(max(dv, 0)), B.Y(min(dv, 0))
        s.rect(B.X(i), y0, max(bw - 0.3, 0.8), max(y1 - y0, 0.5), fill=col, opacity=0.9)
    for i, (d, _, _) in enumerate(res):
        if d.endswith("-01") and int(d[:4]) % 5 == 0:
            s.text(B.X(i), 452, d[:4], 11, C["muted"], "middle")
    s.text(100, 132, t("▲ lump sum ahead", "▲ ก้อนเดียวนำ"), 13, C["amber"], weight=700)
    s.text(100, 420, t("▼ DCA ahead (mostly when a big fall came soon after the start: 2000–02, 2007–08, 2021–22)",
                       "▼ DCA นำ (ส่วนใหญ่เมื่อตลาดร่วงหนักไม่นานหลังเริ่ม: 2000–02, 2007–08, 2021–22)"), 13, C["teal"], weight=700)
    s.text(40, 484, t("Data: ^SP500TR monthly (dividends reinvested), Yahoo Finance, Jan 1988 – Sep 2026. Cash waiting to be invested earns 0%; no taxes or fees.",
                      "ข้อมูล: ^SP500TR รายเดือน (รวมปันผลลงทุนต่อ) Yahoo Finance ม.ค. 1988 – ก.ย. 2026 เงินสดที่รอลงทุนได้ 0% ไม่รวมภาษีและค่าธรรมเนียม"), 11, C["dim"])
    return s.render()


@fig
def dca_choice(lang):
    t = tr(lang)
    s = SVG(960, 340, t("Which one fits your situation?", "แบบไหนเหมาะกับสถานการณ์ของคุณ?"),
            t("The maths favours investing sooner; your behaviour decides what you can stick with.",
              "คณิตศาสตร์เอียงไปทางลงทุนเร็ว แต่พฤติกรรมของคุณตัดสินว่าทำได้จริงแบบไหน"))
    s.card(28, 96, 290, 220, t("Monthly salary", "เงินเดือนรายเดือน"),
           t("You invest as money\narrives. That is DCA\nby default, and it's\nthe right habit.\n\nAutomate it on\npayday.", "คุณลงทุนเมื่อเงินเข้า\nนั่นคือ DCA โดยธรรมชาติ\nและเป็นนิสัยที่ถูกต้อง\n\nตั้งให้ตัดอัตโนมัติ\nในวันเงินเดือนออก"), C["bull"], 17, 15)
    s.card(335, 96, 290, 220, t("A lump sum, calm", "เงินก้อน ใจนิ่ง"),
           t("Investing it all now\nhas won most of the\ntime historically,\nbecause markets\nrise more often\nthan they fall.", "ลงทุนทั้งหมดตอนนี้\nชนะเป็นส่วนใหญ่ในอดีต\nเพราะตลาดขึ้นบ่อยกว่า\nลง"), C["amber"], 17, 15)
    s.card(642, 96, 290, 220, t("A lump sum, nervous", "เงินก้อน ใจไม่นิ่ง"),
           t("If a fall right after\ninvesting would make\nyou sell, DCA over\n6–12 months with a\nwritten schedule.\nIt costs a little on\naverage; panic\ncosts more.", "ถ้าการร่วงหลังลงทุนทันที\nจะทำให้คุณขาย ให้ DCA\nใน 6–12 เดือนตาม\nตารางที่เขียนไว้\nโดยเฉลี่ยเสียเล็กน้อย\nแต่การตื่นตระหนก\nเสียมากกว่า"), C["teal"], 17, 15)
    return s.render()


# ---------------------------------------------------------------- 10.11 Bonds
@fig
def bond_cashflows(lang):
    t = tr(lang)
    s = SVG(960, 390, t("A bond is a loan with a timetable", "พันธบัตรคือเงินกู้ที่มีตารางเวลา"),
            t("Buy a 5-year bond for 1,000 with a 4% coupon: 40 a year, then your 1,000 back.",
              "ซื้อพันธบัตร 5 ปี ราคา 1,000 คูปอง 4%: ได้ปีละ 40 แล้วได้ 1,000 คืน"))
    panel(s, 28, 92, 904, 278)
    base, sc = 250, 0.1
    s.line(60, base, 900, base, C["border"], 2)
    s.rect(90, base, 80, 1000 * sc, fill=C["bear"], opacity=0.8, rx=4)
    s.text(130, base + 60, "−1,000", 15, C["white"], "middle", 700)
    s.text(130, base - 10, t("today: you lend", "วันนี้: คุณให้กู้"), 13, C["bear"], "middle", 700)
    for yr in range(1, 6):
        x = 90 + yr * 140
        h = 40 * 0.6
        s.rect(x, base - h, 80, h, fill=C["bull"], opacity=0.85, rx=4)
        if yr < 5:
            s.text(x + 40, base - h - 8, "+40", 14, C["bull"], "middle", 700)
        s.text(x + 40, base + 22, t(f"year {yr}", f"ปีที่ {yr}"), 12, C["muted"], "middle")
    x = 90 + 5 * 140
    s.rect(x, base - 24 - 1000 * sc, 80, 1000 * sc, fill=C["blue"], opacity=0.8, rx=4)
    s.text(x + 40, base - 24 - 1000 * sc - 8, "+40 +1,000", 14, C["blue"], "middle", 700)
    s.text(250, 130, t("Coupon = interest you receive.\nFace value = the amount repaid at maturity.\nTotal received: 5 × 40 + 1,000 = 1,200.",
                       "คูปอง = ดอกเบี้ยที่คุณได้รับ\nมูลค่าที่ตราไว้ = เงินที่ได้คืนเมื่อครบกำหนด\nได้รับรวม: 5 × 40 + 1,000 = 1,200"), 15, C["text"])
    return s.render()


@fig
def price_yield(lang):
    t = tr(lang)
    s = SVG(960, 500, t("When yields rise, bond prices fall, and long bonds fall most", "เมื่อผลตอบแทนขึ้น ราคาพันธบัตรลง และพันธบัตรยาวลงมากที่สุด"),
            t("Price of a bond paying a 4% coupon (face 100) at different market yields.",
              "ราคาของพันธบัตรคูปอง 4% (มูลค่าที่ตราไว้ 100) ที่ผลตอบแทนตลาดต่าง ๆ"))
    panel(s, 28, 92, 904, 380)
    B = Box(100, 112, 600, 320, 1, 8, 50, 190)
    for v in (60, 80, 100, 120, 140, 160, 180):
        s.line(B.X(1), B.Y(v), B.X(8), B.Y(v), C["border"] if v == 100 else C["grid"], 1)
        s.text(B.X(1) - 8, B.Y(v) + 4, str(v), 11, C["muted"], "end")
    for y in range(1, 9):
        s.text(B.X(y), 452, f"{y}%", 12, C["muted"], "middle")
    s.text(B.X(4.5), 470, t("market yield", "ผลตอบแทนตลาด"), 12, C["muted"], "middle")
    for n, col in ((2, C["teal"]), (10, C["amber"]), (30, C["bear"])):
        pts = [(B.X(y / 10), B.Y(A.bond_price(0.04, y / 1000, n))) for y in range(10, 81)]
        s.polyline(pts, col, 3)
    s.circle(B.X(4), B.Y(100), 6, C["text"])
    s.text(B.X(4) + 10, B.Y(100) - 10, t("at 4%: all = 100", "ที่ 4%: ทุกตัว = 100"), 12, C["text"], weight=700)
    rows = [(C["teal"], t("2-year", "2 ปี"), 2), (C["amber"], t("10-year", "10 ปี"), 10), (C["bear"], t("30-year", "30 ปี"), 30)]
    s.text(730, 140, t("Yield 4% → 5%:", "ผลตอบแทน 4% → 5%:"), 15, C["text"], weight=700)
    for k, (col, nm, n) in enumerate(rows):
        p = A.bond_price(0.04, 0.05, n)
        s.text(730, 176 + k * 32, f"{nm}: {p:.2f} ({p-100:+.1f}%)", 15, col, weight=700)
    s.text(730, 290, t("Yield 4% → 3%:", "ผลตอบแทน 4% → 3%:"), 15, C["text"], weight=700)
    for k, (col, nm, n) in enumerate(rows):
        p = A.bond_price(0.04, 0.03, n)
        s.text(730, 326 + k * 32, f"{nm}: {p:.2f} ({p-100:+.1f}%)", 15, col, weight=700)
    return s.render()


@fig
def credit_ladder(lang):
    t = tr(lang)
    s = SVG(960, 460, t("Who are you lending to? Credit quality", "คุณให้ใครกู้? คุณภาพเครดิต"),
            t("Higher yield is payment for higher risk of not being paid back. Ratings help but can be wrong.",
              "ผลตอบแทนที่สูงกว่าคือค่าตอบแทนสำหรับความเสี่ยงที่จะไม่ได้เงินคืน อันดับเครดิตช่วยได้แต่ผิดได้"))
    rungs = [
        (C["bull"], t("Government (own currency)", "รัฐบาล (สกุลเงินของตัวเอง)"), t("Lowest default risk; main risk is rates and inflation.", "ความเสี่ยงผิดนัดต่ำสุด ความเสี่ยงหลักคือดอกเบี้ยและเงินเฟ้อ"), "AAA–A"),
        (C["teal"], t("Investment-grade companies", "บริษัทระดับน่าลงทุน"), t("Rated BBB− or better; small extra yield.", "อันดับ BBB− ขึ้นไป ผลตอบแทนเพิ่มเล็กน้อย"), "≥ BBB−"),
        (C["amber"], t("High-yield (\"junk\")", "ผลตอบแทนสูง (\"Junk\")"), t("Rated below BBB−; defaults rise in recessions.", "อันดับต่ำกว่า BBB− ผิดนัดเพิ่มขึ้นในภาวะถดถอย"), "≤ BB+"),
        (C["bear"], t("Unrated / unlisted", "ไม่มีอันดับ / ไม่จดทะเบียน"), t("Little information; hard to sell; high loss risk.", "ข้อมูลน้อย ขายยาก เสี่ยงขาดทุนสูง"), "?"),
    ]
    for k, (col, title, body, tag) in enumerate(rungs):
        y = 96 + k * 86
        w = 700 - k * 60
        s.rect(28, y, w, 74, fill=C["panel"], stroke=col, rx=10)
        s.text(48, y + 30, title, 17, col, weight=700)
        s.text(48, y + 56, body, 14, C["text"])
        s.pill(28 + w - 50, y + 37, tag, col, 13)
    s.arrow(860, 420, 860, 110, C["bear"], 3)
    s.text(880, 270, t("more yield\nmore risk", "ผลตอบแทน\nมากขึ้น\nเสี่ยง\nมากขึ้น"), 13, C["bear"], "start", 700)
    return s.render()


@fig
def bond_etfs(lang):
    t = tr(lang)
    s = SVG(960, 440, t("2022: the same government, very different losses", "2022: รัฐบาลเดียวกัน ขาดทุนต่างกันมาก"),
            t("US Treasury bond funds by maturity, total return including interest (Yahoo Finance adjusted closes).",
              "กองทุนพันธบัตรรัฐบาลสหรัฐฯ ตามอายุ ผลตอบแทนรวมดอกเบี้ย (ราคาปรับแล้วจาก Yahoo Finance)"))
    panel(s, 28, 92, 904, 320)
    items = [("SHY", t("1–3 yr", "1–3 ปี"), "shy_m", C["teal"]), ("IEF", t("7–10 yr", "7–10 ปี"), "ief_m", C["amber"]), ("TLT", t("20+ yr", "20+ ปี"), "tlt_m", C["bear"])]
    base, sc = 140, 7
    s.line(80, base, 900, base, C["border"], 1.5)
    s.text(84, base - 10, t("calendar 2022 return", "ผลตอบแทนปี 2022"), 13, C["muted"])
    s.text(520, base - 10, t("worst fall from a high, 2020–Sep 2026", "ร่วงหนักสุดจากจุดสูง 2020–ก.ย. 2026"), 13, C["muted"])
    for k, (sym, nm, key, col) in enumerate(items):
        r = A.year_return(key, 2022) * 100
        dd = A.dd_window(key, "2020-01", "2026-09") * 100
        x = 110 + k * 120
        s.rect(x, base, 80, -r * sc, fill=col, opacity=0.85, rx=4)
        s.text(x + 40, base - r * sc + 20, f"{r:.1f}%", 15, col, "middle", 700)
        s.text(x + 40, 395, f"{sym}\n{nm}", 12, C["text"], "middle", 600)
        x2 = 540 + k * 120
        s.rect(x2, base, 80, -dd * 4.5, fill=col, opacity=0.5, rx=4)
        s.text(x2 + 40, base - dd * 4.5 + 20, f"{dd:.1f}%", 15, col, "middle", 700)
        s.text(x2 + 40, 395, f"{sym}\n{nm}", 12, C["text"], "middle", 600)
    s.line(490, 110, 490, 400, C["border"], 1)
    return s.render()


# ---------------------------------------------------------------- 10.12 Dividends
@fig
def dividend_dates(lang):
    t = tr(lang)
    s = SVG(960, 340, t("Four dates of a dividend", "สี่วันสำคัญของเงินปันผล"),
            t("To get the dividend you must own the shares before the ex-dividend date (XD in Thailand).",
              "เพื่อได้รับปันผล คุณต้องถือหุ้นก่อนวันที่ไม่มีสิทธิรับปันผล (XD ในไทย)"))
    panel(s, 28, 92, 904, 228)
    y = 170
    s.line(70, y, 890, y, C["border"], 3)
    pts = [
        (130, C["blue"], t("Declaration", "วันประกาศ"), t("Board announces\namount and dates", "คณะกรรมการประกาศ\nจำนวนและวันที่")),
        (360, C["bear"], t("Ex-dividend (XD)", "วัน XD"), t("Buy on/after this day:\nno dividend. Price\nusually opens lower\nby about the dividend.", "ซื้อในหรือหลังวันนี้:\nไม่ได้ปันผล ราคามักเปิด\nต่ำลงราวเท่าปันผล")),
        (590, C["amber"], t("Record date", "วันกำหนดรายชื่อ"), t("Company checks\nwho the owners are", "บริษัทตรวจสอบ\nรายชื่อผู้ถือหุ้น")),
        (810, C["bull"], t("Payment", "วันจ่าย"), t("Cash arrives,\nafter any tax\nwithheld", "เงินเข้า\nหลังหักภาษี\nณ ที่จ่าย")),
    ]
    for x, col, title, body in pts:
        s.circle(x, y, 9, col)
        s.text(x, y - 30, title, 15, col, "middle", 700)
        s.text(x, y + 36, body, 13, C["text"], "middle")
    return s.render()


@fig
def total_return(lang):
    t = tr(lang)
    g, tr_ = A.series("gspc_m", 1), A.series("sp500tr_m")
    keys = sorted(k for k in g if k >= "1988-01")
    s = SVG(960, 500, t("Dividends matter: 100,000 in the S&P 500 since January 1988", "ปันผลสำคัญ: 100,000 ใน S&P 500 ตั้งแต่มกราคม 1988"),
            t("Price only vs price + dividends reinvested (total return). Log scale; before tax and fees.",
              "ราคาอย่างเดียว vs ราคา + ปันผลลงทุนต่อ (ผลตอบแทนรวม) สเกลลอการิทึม ก่อนภาษีและค่าธรรมเนียม"))
    panel(s, 28, 92, 904, 380)
    B = Box(110, 112, 600, 320, 0, len(keys) - 1, 50_000, 10_000_000, log=True)
    for v in (100_000, 300_000, 1_000_000, 3_000_000, 10_000_000):
        s.line(B.X(0), B.Y(v), B.X(len(keys) - 1), B.Y(v), C["grid"], 1)
        s.text(B.X(0) - 8, B.Y(v) + 4, f"{v/1e6:g}M" if v >= 1e6 else f"{v/1e3:g}k", 11, C["muted"], "end")
    for i, k in enumerate(keys):
        if k.endswith("-01") and int(k[:4]) % 5 == 0:
            s.text(B.X(i), 452, k[:4], 11, C["muted"], "middle")
    p0, t0 = g[keys[0]], tr_[keys[0]]
    s.polyline([(B.X(i), B.Y(100_000 * g[k] / p0)) for i, k in enumerate(keys)], C["amber"], 2.5)
    s.polyline([(B.X(i), B.Y(100_000 * tr_[k] / t0)) for i, k in enumerate(keys)], C["bull"], 2.5)
    end_p, end_t = 100_000 * g[keys[-1]] / p0, 100_000 * tr_[keys[-1]] / t0
    yrs = (len(keys) - 1) / 12
    s.text(730, 160, t("Total return", "ผลตอบแทนรวม"), 15, C["bull"], weight=700)
    s.text(730, 184, f"{fmt(end_t)}", 20, C["bull"], weight=700)
    s.text(730, 206, t(f"{A.cagr(t0, tr_[keys[-1]], yrs):.1%} a year", f"{A.cagr(t0, tr_[keys[-1]], yrs):.1%} ต่อปี"), 13, C["bull"])
    s.text(730, 260, t("Price only", "ราคาอย่างเดียว"), 15, C["amber"], weight=700)
    s.text(730, 284, f"{fmt(end_p)}", 20, C["amber"], weight=700)
    s.text(730, 306, t(f"{A.cagr(p0, g[keys[-1]], yrs):.1%} a year", f"{A.cagr(p0, g[keys[-1]], yrs):.1%} ต่อปี"), 13, C["amber"])
    s.text(730, 360, t(f"to {keys[-1]} (Sep 2026)", f"ถึง {keys[-1]} (ก.ย. 2026)"), 12, C["muted"])
    s.text(730, 380, t("Data: Yahoo Finance\n^GSPC and ^SP500TR", "ข้อมูล: Yahoo Finance\n^GSPC และ ^SP500TR"), 12, C["dim"])
    return s.render()


@fig
def yield_trap(lang):
    t = tr(lang)
    s = SVG(960, 470, t("High yield can be a warning, and tax takes a cut", "ปันผลสูงอาจเป็นสัญญาณเตือน และภาษีหักส่วนหนึ่ง"),
            t("Dividend yield = yearly dividend ÷ price. It rises when the price falls, before any cut is announced.",
              "อัตราปันผล = ปันผลต่อปี ÷ ราคา มันสูงขึ้นเมื่อราคาลง ก่อนที่จะประกาศลดปันผล"))
    panel(s, 28, 92, 440, 350)
    s.text(48, 124, t("Same 4.00 dividend, falling price", "ปันผล 4.00 เท่าเดิม ราคาลดลง"), 15, C["text"], weight=700)
    for k, p in enumerate((100, 80, 50)):
        y = 150 + k * 80
        s.rect(48, y, p * 2.6, 52, fill=C["blue"], opacity=0.35 + k * 0.1, rx=6)
        s.text(60, y + 32, t(f"price {p}", f"ราคา {p}"), 15, C["text"], weight=700)
        s.text(330, y + 32, f"{4 / p:.0%}", 22, [C["bull"], C["amber"], C["bear"]][k], "start", 700)
    s.text(48, 412, t("An 8% yield often means the market expects a cut.", "อัตราปันผล 8% มักแปลว่าตลาดคาดว่าจะลดปันผล"), 13, C["bear"], weight=700)
    panel(s, 492, 92, 440, 350)
    s.text(512, 124, t("1,000 of dividends: what you keep", "ปันผล 1,000: คุณเหลือเท่าไร"), 15, C["text"], weight=700)
    rows = [(t("Thai stock, Thai resident", "หุ้นไทย ผู้มีถิ่นที่อยู่ในไทย"), 0.10, C["bull"]),
            (t("US stock, Thai resident (treaty)", "หุ้นสหรัฐฯ ผู้มีถิ่นที่อยู่ในไทย (อนุสัญญา)"), 0.15, C["amber"]),
            (t("US stock, Lao resident (no treaty)", "หุ้นสหรัฐฯ ผู้มีถิ่นที่อยู่ในลาว (ไม่มีอนุสัญญา)"), 0.30, C["bear"])]
    for k, (nm, rate, col) in enumerate(rows):
        y = 150 + k * 80
        s.text(512, y + 4, nm, 13, C["text"])
        s.rect(512, y + 14, 380 * (1 - rate), 30, fill=col, opacity=0.8, rx=4)
        s.rect(512 + 380 * (1 - rate), y + 14, 380 * rate, 30, fill=C["dim"], opacity=0.6, rx=4)
        s.text(522, y + 35, f"{fmt(1000 * (1 - rate))}", 15, C["bg"], weight=700)
        s.text(897, y + 35, f"−{rate:.0%}", 13, C["muted"], "end", 700)
    s.text(512, 400, t("First tax withheld at source, as of Oct 2026.\nMore tax may be due at home (see 10.14).", "ภาษีที่ถูกหัก ณ ต้นทางขั้นแรก ณ ต.ค. 2026\nอาจมีภาษีเพิ่มในประเทศของคุณ (ดู 10.14)"), 12, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 10.13 REITs
@fig
def reit_structure(lang):
    t = tr(lang)
    s = SVG(960, 380, t("How a REIT works", "REIT ทำงานอย่างไร"),
            t("Many investors pool money to own rent-paying property; most of the profit must be paid out.",
              "นักลงทุนจำนวนมากรวมเงินกันเป็นเจ้าของอสังหาฯ ที่มีค่าเช่า กำไรส่วนใหญ่ต้องจ่ายออก"))
    boxes = [(40, C["blue"], t("You + other\ninvestors", "คุณ + นักลงทุน\nคนอื่น")),
             (370, C["purple"], t("REIT\n(listed trust)", "REIT\n(ทรัสต์จดทะเบียน)")),
             (700, C["amber"], t("Malls, offices,\nwarehouses,\nhotels, towers", "ห้าง สำนักงาน\nคลังสินค้า โรงแรม\nเสาโทรคมนาคม"))]
    for x, col, txt in boxes:
        s.rect(x, 130, 220, 120, fill=C["panel"], stroke=col, rx=12)
        s.text(x + 110, 175, txt, 16, col, "middle", 700)
    s.arrow(265, 165, 365, 165, C["blue"], 2.5)
    s.text(315, 155, t("money", "เงิน"), 12, C["blue"], "middle")
    s.arrow(595, 165, 695, 165, C["purple"], 2.5)
    s.text(645, 155, t("buys", "ซื้อ"), 12, C["purple"], "middle")
    s.arrow(695, 220, 595, 220, C["bull"], 2.5)
    s.text(645, 240, t("rent", "ค่าเช่า"), 12, C["bull"], "middle")
    s.arrow(365, 220, 265, 220, C["bull"], 2.5)
    s.text(315, 240, t("≥ 90% paid out", "จ่ายออก ≥ 90%"), 12, C["bull"], "middle", 700)
    s.text(40, 300, t("• You can buy and sell units on the exchange like a share.\n• Income comes from rent; value moves with rents, occupancy and interest rates.\n• US REITs and Thai REITs must pay out at least 90% of their (taxable or adjusted net) profit.",
                      "• ซื้อขายหน่วยได้ในตลาดหลักทรัพย์เหมือนหุ้น\n• รายได้มาจากค่าเช่า มูลค่าขยับตามค่าเช่า อัตราการเช่า และดอกเบี้ย\n• REIT สหรัฐฯ และ REIT ไทยต้องจ่ายอย่างน้อย 90% ของกำไร (ทางภาษีหรือกำไรสุทธิที่ปรับปรุงแล้ว)"), 15, C["text"])
    return s.render()


@fig
def reit_vs_stocks(lang):
    t = tr(lang)
    v, sp = A.series("vnq_m"), A.series("sp500tr_m")
    keys = sorted(k for k in v if k >= "2005-01")
    s = SVG(960, 500, t("US REITs vs US stocks, 2005–2026 (100 invested, dividends reinvested)", "REIT สหรัฐฯ vs หุ้นสหรัฐฯ 2005–2026 (ลงทุน 100 ปันผลลงทุนต่อ)"),
            t("VNQ (Vanguard US REIT ETF) vs S&P 500 total return, monthly. REITs fell further in 2008–09 and in the 2022 rate rise.",
              "VNQ (ETF REIT สหรัฐฯ ของ Vanguard) vs S&P 500 ผลตอบแทนรวม รายเดือน REIT ร่วงหนักกว่าในปี 2008–09 และช่วงขึ้นดอกเบี้ยปี 2022"))
    panel(s, 28, 92, 904, 380)
    hi = max(100 * sp[k] / sp[keys[0]] for k in keys) * 1.08
    B = Box(90, 112, 640, 320, 0, len(keys) - 1, 0, hi)
    for val in range(0, int(hi) + 1, 200):
        s.line(B.X(0), B.Y(val), B.X(len(keys) - 1), B.Y(val), C["grid"], 1)
        s.text(B.X(0) - 8, B.Y(val) + 4, str(val), 11, C["muted"], "end")
    for i, k in enumerate(keys):
        if k.endswith("-01") and int(k[:4]) % 3 == 2:
            s.text(B.X(i), 452, k[:4], 11, C["muted"], "middle")
    s.polyline([(B.X(i), B.Y(100 * sp[k] / sp[keys[0]])) for i, k in enumerate(keys)], C["blue"], 2.5)
    s.polyline([(B.X(i), B.Y(100 * v[k] / v[keys[0]])) for i, k in enumerate(keys)], C["amber"], 2.5)
    yrs = (len(keys) - 1) / 12
    e_sp, e_v = 100 * sp[keys[-1]] / sp[keys[0]], 100 * v[keys[-1]] / v[keys[0]]
    s.text(750, 150, t("S&P 500", "S&P 500"), 15, C["blue"], weight=700)
    s.text(750, 172, f"{e_sp:.0f} · {A.cagr(sp[keys[0]], sp[keys[-1]], yrs):.1%}/yr", 15, C["blue"])
    s.text(750, 215, t("US REITs (VNQ)", "REIT สหรัฐฯ (VNQ)"), 15, C["amber"], weight=700)
    s.text(750, 237, f"{e_v:.0f} · {A.cagr(v[keys[0]], v[keys[-1]], yrs):.1%}/yr", 15, C["amber"])
    s.text(750, 290, t("Worst fall 2007–09\n(monthly closes):", "ร่วงหนักสุด 2007–09\n(ราคาปิดรายเดือน):"), 13, C["text"], weight=700)
    s.text(750, 330, t(f"REITs {A.dd_window('vnq_m', '2006-01', '2010-12'):.0%}\nS&P 500 {A.dd_window('sp500tr_m', '2006-01', '2010-12'):.0%}",
                       f"REIT {A.dd_window('vnq_m', '2006-01', '2010-12'):.0%}\nS&P 500 {A.dd_window('sp500tr_m', '2006-01', '2010-12'):.0%}"), 13, C["text"])
    s.text(750, 380, t(f"2022: REITs {A.year_return('vnq_m', 2022):.0%},\nS&P 500 {A.year_return('sp500tr_m', 2022):.0%}",
                       f"2022: REIT {A.year_return('vnq_m', 2022):.0%}\nS&P 500 {A.year_return('sp500tr_m', 2022):.0%}"), 13, C["text"])
    return s.render()


@fig
def reit_checklist(lang):
    t = tr(lang)
    s = SVG(960, 370, t("Before you buy a REIT: six questions", "ก่อนซื้อ REIT: หกคำถาม"),
            t("A high distribution yield means nothing if the rent behind it is shrinking.",
              "อัตราจ่ายผลตอบแทนสูงไม่มีความหมาย ถ้าค่าเช่าเบื้องหลังกำลังหดตัว"))
    items = [
        (C["blue"], t("Occupancy", "อัตราการเช่า"), t("What % of space is rented?\nFalling = warning.", "เช่าไปกี่ % ของพื้นที่?\nลดลง = สัญญาณเตือน")),
        (C["teal"], t("Lease length", "อายุสัญญาเช่า"), t("When do big leases end?\nLand lease expiry?", "สัญญาใหญ่หมดเมื่อไร?\nสิทธิการเช่าที่ดินหมดเมื่อไร?")),
        (C["amber"], t("Debt (gearing)", "หนี้ (Gearing)"), t("Debt ÷ assets. High debt\nhurts when rates rise.", "หนี้ ÷ สินทรัพย์ หนี้สูง\nเจ็บเมื่อดอกเบี้ยขึ้น")),
        (C["bull"], t("Yield vs bonds", "ผลตอบแทน vs พันธบัตร"), t("Extra yield over government\nbonds pays for the risk.", "ผลตอบแทนส่วนเกินเหนือ\nพันธบัตรรัฐบาลคือค่าความเสี่ยง")),
        (C["purple"], t("Price vs NAV", "ราคา vs NAV"), t("Price below net asset value\n= discount; above = premium.", "ราคาต่ำกว่ามูลค่าทรัพย์สินสุทธิ\n= ส่วนลด สูงกว่า = ส่วนเกิน")),
        (C["pink"], t("Sponsor & fees", "ผู้สนับสนุน & ค่าธรรมเนียม"), t("Who manages it and\nwho do the fees go to?", "ใครบริหาร และค่าธรรมเนียม\nไปที่ใคร?")),
    ]
    for k, (col, title, body) in enumerate(items):
        x = 28 + (k % 3) * 304
        y = 96 + (k // 3) * 134
        s.card(x, y, 296, 124, title, body, col, 17, 14)
    return s.render()


# ---------------------------------------------------------------- 10.14 Thailand & Laos
@fig
def home_markets(lang):
    t = tr(lang)
    s = SVG(960, 450, t("Your home exchanges: SET and LSX (as of Oct 2026)", "ตลาดหลักทรัพย์ในบ้าน: SET และ LSX (ณ ต.ค. 2026)"),
            t("Both exchanges run on UTC+7, Monday–Friday except holidays. Check the official sites for changes.",
              "ทั้งสองตลาดใช้เวลา UTC+7 วันจันทร์–ศุกร์ ยกเว้นวันหยุด ตรวจสอบการเปลี่ยนแปลงที่เว็บไซต์ทางการ"))
    s.card(28, 92, 440, 196, t("SET · Stock Exchange of Thailand", "SET · ตลาดหลักทรัพย์แห่งประเทศไทย"),
           t("• Main board SET + mai for smaller firms\n• Prices in baht; most orders in lots of 100\n• Also lists ETFs, REITs, DRs (foreign\n  shares in baht, e.g. Apple, Tencent)\n• Gains on SET shares: no personal income\n  tax; dividends: 10% withheld",
             "• กระดานหลัก SET + mai สำหรับบริษัทเล็ก\n• ราคาเป็นบาท ส่วนใหญ่ซื้อขายเป็นล็อต 100 หุ้น\n• มี ETF REIT และ DR (หุ้นต่างประเทศ\n  เป็นบาท เช่น Apple Tencent)\n• กำไรจากขายหุ้นใน SET: ไม่เสียภาษี\n  เงินได้บุคคล ปันผล: หัก 10%"), C["blue"], 16, 14)
    s.card(492, 92, 440, 196, t("LSX · Lao Securities Exchange", "LSX · ตลาดหลักทรัพย์ลาว"),
           t("• Opened 11 Jan 2011 in Vientiane\n  (Korea Exchange owns 49%)\n• About a dozen listed companies\n  (12 as of Apr 2026), prices in kip\n• Small and thinly traded: buying and\n  selling can move the price a lot\n• Dividends taxed 10%; share sales 2%",
             "• เปิด 11 ม.ค. 2011 ที่เวียงจันทน์\n  (Korea Exchange ถือหุ้น 49%)\n• บริษัทจดทะเบียนราวสิบกว่าแห่ง\n  (12 ณ เม.ย. 2026) ราคาเป็นกีบ\n• ตลาดเล็ก สภาพคล่องต่ำ: การซื้อขาย\n  อาจทำให้ราคาขยับมาก\n• ปันผลเสียภาษี 10% ขายหุ้น 2%"), C["purple"], 16, 14)
    # session bars
    panel(s, 28, 300, 904, 140)
    x0, x1, h0, h1 = 150, 900, 8.5, 17.0
    X = lambda hh: x0 + (x1 - x0) * (hh - h0) / (h1 - h0)
    for hh in range(9, 18):
        s.line(X(hh), 336, X(hh), 420, C["grid"], 1)
        s.text(X(hh), 434, f"{hh:02d}:00", 11, C["muted"], "middle")
    s.text(44, 357, "SET", 15, C["blue"], weight=700)
    s.rect(X(9.5), 343, X(10) - X(9.5), 22, fill=C["blue"], opacity=0.3)
    s.rect(X(10), 343, X(12.5) - X(10), 22, fill=C["blue"], opacity=0.85)
    s.rect(X(13.5), 343, X(14) - X(13.5), 22, fill=C["blue"], opacity=0.3)
    s.rect(X(14), 343, X(16.5) - X(14), 22, fill=C["blue"], opacity=0.85)
    s.rect(X(16.5), 343, X(16 + 40 / 60) - X(16.5), 22, fill=C["blue"], opacity=0.3)
    s.text(44, 401, "LSX", 15, C["purple"], weight=700)
    s.rect(X(8.5), 387, X(9) - X(8.5), 22, fill=C["purple"], opacity=0.3)
    s.rect(X(9), 387, X(14 + 50 / 60) - X(9), 22, fill=C["purple"], opacity=0.85)
    s.rect(X(14 + 50 / 60), 387, X(15) - X(14 + 50 / 60), 22, fill=C["purple"], opacity=0.3)
    s.text(X(12.9), 322, t("pale = auction (pre-open / pre-close)", "สีจาง = ช่วงประมูล (ก่อนเปิด / ก่อนปิด)"), 11, C["muted"], "middle")
    return s.render()


@fig
def us_routes(lang):
    t = tr(lang)
    s = SVG(960, 400, t("Four ways to own US stocks from Thailand", "สี่ทางในการถือหุ้นสหรัฐฯ จากประเทศไทย"),
            t("Each route has different costs, tax paperwork and protection. Compare total cost, not just commission.",
              "แต่ละทางมีต้นทุน เอกสารภาษี และความคุ้มครองต่างกัน เทียบต้นทุนรวม ไม่ใช่แค่ค่าคอมมิชชัน"))
    items = [
        (C["blue"], t("1 · Thai broker, foreign-stock account", "1 · โบรกเกอร์ไทย บัญชีหุ้นต่างประเทศ"),
         t("+ Thai regulator (SEC), Thai support\n− FX spread and higher commissions\n− you handle foreign-income tax", "+ อยู่ใต้ ก.ล.ต. ไทย มีบริการภาษาไทย\n− ส่วนต่างค่าเงินและค่าคอมสูงกว่า\n− คุณจัดการภาษีเงินได้ต่างประเทศเอง")),
        (C["teal"], t("2 · Overseas broker", "2 · โบรกเกอร์ต่างประเทศ"),
         t("+ low commissions, many markets\n− foreign regulator; disputes are hard\n− you handle forms (W-8BEN) and tax", "+ ค่าคอมต่ำ หลายตลาด\n− อยู่ใต้หน่วยงานต่างประเทศ ข้อพิพาทยาก\n− คุณจัดการแบบฟอร์ม (W-8BEN) และภาษีเอง")),
        (C["amber"], t("3 · DRs on the SET", "3 · DR ใน SET"),
         t("+ buy in baht through a normal account\n− only some stocks; small premium or\n  discount to the real share possible", "+ ซื้อเป็นบาทผ่านบัญชีปกติ\n− มีแค่บางตัว ราคาอาจสูงหรือต่ำกว่า\n  หุ้นจริงเล็กน้อย")),
        (C["purple"], t("4 · Thai fund (feeder / index fund)", "4 · กองทุนไทย (Feeder / กองทุนดัชนี)"),
         t("+ easy, small amounts, some tax-saving\n− two layers of fees (Thai + foreign fund)\n− check the fund's currency hedge", "+ ง่าย ลงทุนน้อยได้ บางกองลดหย่อนภาษี\n− ค่าธรรมเนียมสองชั้น (ไทย + กองต่างประเทศ)\n− ตรวจการป้องกันความเสี่ยงค่าเงิน")),
    ]
    for k, (col, title, body) in enumerate(items):
        x = 28 + (k % 2) * 460
        y = 92 + (k // 2) * 142
        s.card(x, y, 444, 132, title, body, col, 16, 14)
    s.text(40, 388, t("Lao residents: routes 2 and 4 depend on your bank and broker; check foreign-exchange rules with your bank first.",
                      "ผู้มีถิ่นที่อยู่ในลาว: ทาง 2 และ 4 ขึ้นกับธนาคารและโบรกเกอร์ของคุณ ตรวจกฎการแลกเปลี่ยนเงินตรากับธนาคารก่อน"), 12, C["muted"])
    return s.render()


THAI_PIT = [(150_000, 0.0), (300_000, 0.05), (500_000, 0.10), (750_000, 0.15), (1_000_000, 0.20),
            (2_000_000, 0.25), (5_000_000, 0.30), (float("inf"), 0.35)]


def thai_tax(net):
    tax, lo = 0.0, 0
    for hi, r in THAI_PIT:
        if net > lo:
            tax += (min(net, hi) - lo) * r
        lo = hi
    return tax


@fig
def tax_funds(lang):
    t = tr(lang)
    s = SVG(960, 534, t("Thai tax-saving funds (rules as of Oct 2026)", "กองทุนลดหย่อนภาษีไทย (กฎ ณ ต.ค. 2026)"),
            t("The deduction lowers taxable income. What it saves depends on your top tax rate; the lock-up is the price.",
              "การลดหย่อนลดเงินได้สุทธิ สิ่งที่ประหยัดได้ขึ้นกับอัตราภาษีขั้นสูงสุดของคุณ ระยะถือขั้นต่ำคือราคาที่ต้องจ่าย"))
    s.card(28, 92, 440, 196, "ThaiESG",
           t("• Deduct up to 30% of income,\n  max 300,000 baht a year\n• Hold at least 5 years from purchase\n• Thai stocks/bonds meeting ESG rules\n• Scheme covers purchases 2024–2026",
             "• ลดหย่อนได้ถึง 30% ของเงินได้\n  สูงสุด 300,000 บาทต่อปี\n• ถือขั้นต่ำ 5 ปีนับจากวันซื้อ\n• หุ้น/ตราสารหนี้ไทยตามเกณฑ์ ESG\n• มาตรการครอบคลุมการซื้อปี 2024–2026"), C["bull"], 17, 14)
    s.card(492, 92, 440, 196, "RMF",
           t("• Deduct up to 30% of income,\n  max 500,000 baht (shared with\n  provident fund, pension insurance etc.)\n• Hold 5+ years AND until age 55\n• For retirement saving",
             "• ลดหย่อนได้ถึง 30% ของเงินได้\n  สูงสุด 500,000 บาท (รวมกับกองทุน\n  สำรองเลี้ยงชีพ ประกันบำนาญ ฯลฯ)\n• ถือ 5 ปีขึ้นไป และ จนอายุ 55\n• สำหรับการออมเพื่อเกษียณ"), C["amber"], 17, 14)
    panel(s, 28, 304, 904, 196)
    s.text(48, 334, t("Tax saved by putting 100,000 into a deductible fund (Thai personal income tax rates)", "ภาษีที่ประหยัดเมื่อซื้อกองทุนลดหย่อน 100,000 บาท (อัตราภาษีเงินได้บุคคลธรรมดาไทย)"), 14, C["text"], weight=700)
    nets = [400_000, 900_000, 1_500_000, 3_000_000]
    for k, n in enumerate(nets):
        saved = thai_tax(n) - thai_tax(n - 100_000)
        x = 60 + k * 220
        h = saved / 30_000 * 110
        s.rect(x, 470 - h, 120, h, fill=C["teal"], opacity=0.85, rx=4)
        s.text(x + 60, 462 - h, fmt(saved), 15, C["teal"], "middle", 700)
        s.text(x + 130, 420, t(f"net income\n{fmt(n)}", f"เงินได้สุทธิ\n{fmt(n)}"), 12, C["muted"])
    s.text(48, 515, t("SSF: no new tax deduction for purchases after 2024. ThaiESGX: special window May–June 2025 only.",
                      "SSF: ไม่มีสิทธิลดหย่อนใหม่สำหรับการซื้อหลังปี 2024 ThaiESGX: ช่วงพิเศษ พ.ค.–มิ.ย. 2025 เท่านั้น"), 11, C["dim"])
    return s.render()
