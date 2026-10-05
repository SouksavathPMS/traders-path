"""Phase 0 figures: the playing field (exchanges, brokers, forex, leverage, news)."""
from charts import SVG, CandleChart, C, tr, candles_from_path

FIGURES = {}


def fig(fn):
    FIGURES["p0-" + fn.__name__.replace("_", "-")] = fn
    return fn


def box(s, x, y, w, h, head, body, col, hs=15, bs=12):
    s.rect(x, y, w, h, fill=C["panel"], stroke=col, rx=12)
    s.text(x + w / 2, y + 28, head, hs, col, "middle", 700)
    if body:
        s.text(x + w / 2, y + 50, body, bs, C["muted"], "middle")


# ---------------------------------------------------------------- 0.1
@fig
def plumbing(lang):
    t = tr(lang)
    s = SVG(960, 540, t("Who stands between you and the market", "ใครอยู่ระหว่างคุณกับตลาด"),
            t("Two ways your order can travel: through an exchange, or to a broker that IS the market.",
              "คำสั่งของคุณเดินทางได้สองแบบ: ผ่านตลาดกลาง หรือไปหาโบรกเกอร์ที่เป็นตลาดเสียเอง"))
    # row 1: exchange model
    s.text(28, 112, t("A · EXCHANGE MODEL  (stocks, futures, listed options, ETFs)", "A · แบบตลาดกลาง  (หุ้น ฟิวเจอร์ส ออปชันจดทะเบียน ETF)"), 13, C["blue"], weight=700)
    y = 128
    box(s, 28, y, 150, 74, t("You", "คุณ"), t("app / platform", "แอป / แพลตฟอร์ม"), C["text"])
    box(s, 228, y, 170, 74, t("Your broker", "โบรกเกอร์ของคุณ"), t("checks money,\nsends the order", "เช็กเงิน\nส่งคำสั่งต่อ"), C["blue"])
    box(s, 448, y, 200, 74, t("Exchange", "ตลาดหลักทรัพย์"), t("matching engine:\nbuyer meets seller", "ระบบจับคู่:\nผู้ซื้อพบผู้ขาย"), C["amber"])
    box(s, 698, y, 234, 74, t("Other brokers & traders", "โบรกเกอร์และเทรดเดอร์อื่น"), t("millions of orders", "คำสั่งนับล้าน"), C["text"])
    for x1, x2 in ((178, 228), (398, 448)):
        s.arrow(x1 + 2, y + 37, x2 - 4, y + 37, C["muted"], 2)
    s.arrow(696, y + 37, 652, y + 37, C["muted"], 2)
    box(s, 448, 238, 200, 70, t("Clearing house", "สำนักหักบัญชี"), t("guarantees both sides pay", "รับประกันว่าทั้งสองฝ่ายจ่ายจริง"), C["teal"])
    box(s, 228, 238, 170, 70, t("Custodian", "ผู้รับฝากทรัพย์สิน"), t("holds your shares\nin your name", "เก็บหุ้นไว้\nในชื่อคุณ"), C["teal"])
    s.arrow(548, y + 76, 548, 236, C["muted"], 1.5, "4 4")
    s.arrow(446, 273, 400, 273, C["muted"], 1.5, "4 4")
    s.text(698, 262, t("✓ One public price for everyone\n✓ Your assets kept separately\n✓ Strong regulation", "✓ ราคาเดียวสำหรับทุกคน\n✓ ทรัพย์สินแยกเก็บจากโบรกเกอร์\n✓ กำกับดูแลเข้มงวด"), 13, C["bull"])
    # row 2: OTC / CFD
    s.line(28, 336, 932, 336, C["border"], 1)
    s.text(28, 370, t("B · OTC / CFD MODEL  (most retail forex, gold, crypto CFDs)", "B · แบบ OTC / CFD  (ฟอเร็กซ์ ทองคำ CFD คริปโตของรายย่อยส่วนใหญ่)"), 13, C["pink"], weight=700)
    y = 388
    box(s, 28, y, 150, 74, t("You", "คุณ"), t("app / platform", "แอป / แพลตฟอร์ม"), C["text"])
    box(s, 228, y, 220, 74, t("Broker = your counterparty", "โบรกเกอร์ = คู่สัญญาของคุณ"), t("quotes its own price;\nmay keep or pass on your trade", "ตั้งราคาเอง\nอาจรับไว้เองหรือส่งต่อ"), C["pink"])
    box(s, 498, y, 200, 74, t("Liquidity providers", "ผู้ให้สภาพคล่อง"), t("banks, big market makers", "ธนาคาร มาร์เก็ตเมกเกอร์ใหญ่"), C["amber"])
    s.arrow(180, y + 37, 224, y + 37, C["muted"], 2)
    s.arrow(450, y + 37, 494, y + 37, C["muted"], 2, "5 4")
    s.text(450 + 22, y + 96, t("only if the broker hedges", "เฉพาะเมื่อโบรกเกอร์เฮดจ์"), 11, C["muted"], "middle")
    s.text(712, 410, t("✗ Price set by the broker\n✗ Your loss can be its profit\n✗ Protection depends on the\n   regulator — check it!", "✗ ราคาตั้งโดยโบรกเกอร์\n✗ การขาดทุนของคุณอาจเป็นกำไรของเขา\n✗ ความคุ้มครองขึ้นกับผู้กำกับดูแล\n   — ตรวจสอบเสมอ!"), 13, C["bear"])
    s.text(28, 520, t("Neither model is 'bad'. B is how almost all retail forex & gold trading works — the broker's licence is what protects you.",
                      "ไม่มีแบบไหน 'ไม่ดี' แบบ B คือวิธีที่ฟอเร็กซ์และทองคำของรายย่อยเกือบทั้งหมดทำงาน — ใบอนุญาตของโบรกเกอร์คือสิ่งที่ปกป้องคุณ"), 13, C["amber"], weight=600)
    return s.render()


# ---------------------------------------------------------------- 0.2 / 0.3 leverage
@fig
def leverage(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Leverage: a small deposit controls a big position", "เลเวอเรจ: เงินวางประกันน้อย ควบคุมโพซิชันใหญ่"),
            t("Account 1,000 USD. Same 1% market move, different leverage used.", "บัญชี 1,000 ดอลลาร์ ตลาดขยับ 1% เท่ากัน แต่ใช้เลเวอเรจต่างกัน"))
    rows = [("1 : 1", 1000, C["bull"]), ("1 : 10", 10000, C["teal"]), ("1 : 50", 50000, C["amber"]), ("1 : 100", 100000, C["bear"])]
    s.text(150, 118, t("Position size", "ขนาดโพซิชัน"), 13, C["muted"], weight=700)
    s.text(700, 118, t("1% move =", "ขยับ 1% ="), 13, C["muted"], weight=700)
    s.text(830, 118, t("% of account", "% ของบัญชี"), 13, C["muted"], weight=700)
    for i, (lab, pos, col) in enumerate(rows):
        y = 134 + i * 64
        s.text(40, y + 30, lab, 18, col, weight=700)
        w = 400 * pos / 100000
        s.rect(150, y + 8, max(w, 6), 32, fill=col, rx=6, opacity=0.85)
        s.text(150 + max(w, 6) + 10, y + 30, f"{pos:,} USD", 14, C["text"], weight=600)
        s.text(700, y + 30, f"± {pos // 100:,} USD", 15, col, weight=700)
        s.text(830, y + 30, f"± {pos // 1000}%", 18, col, weight=700)
    s.rect(28, 400, 904, 52, fill=C["bear"], opacity=0.12, stroke=C["bear"], rx=10)
    s.text(48, 432, t("At 1:100, a normal 1% day can wipe out the whole account. Leverage doesn't change the market — it changes how much a move costs YOU.",
                      "ที่ 1:100 วันที่ตลาดขยับปกติ 1% ก็ล้างบัญชีได้ทั้งหมด เลเวอเรจไม่ได้เปลี่ยนตลาด แต่เปลี่ยนว่าการขยับนั้นทำให้ คุณ เสียเท่าไหร่"), 13, C["text"], weight=600)
    return s.render()


@fig
def fx_quote(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Reading a forex quote", "อ่านราคาฟอเร็กซ์"),
            t("EUR/USD 1.0850 means: 1 euro costs 1.0850 US dollars.", "EUR/USD 1.0850 หมายถึง: 1 ยูโรมีราคา 1.0850 ดอลลาร์สหรัฐ"))
    s.text(200, 200, "EUR", 64, C["blue"], "middle", 800)
    s.text(285, 200, "/", 64, C["muted"], "middle", 300)
    s.text(370, 200, "USD", 64, C["amber"], "middle", 800)
    s.text(200, 240, t("BASE currency\n(what you buy or sell)", "สกุลเงินหลัก (Base)\n(สิ่งที่คุณซื้อหรือขาย)"), 13, C["blue"], "middle", 600)
    s.text(370, 240, t("QUOTE currency\n(what you pay with)", "สกุลเงินอ้างอิง (Quote)\n(สิ่งที่ใช้จ่าย)"), 13, C["amber"], "middle", 600)
    # price with pip
    s.text(641, 200, "1.08", 64, C["text"], "end", 800)
    s.text(646, 200, "5", 64, C["bull"], "start", 800)
    s.text(684, 200, "0", 64, C["dim"], "start", 800)
    s.line(664, 214, 664, 262, C["bull"], 2)
    s.text(656, 284, t("4th decimal = 1 PIP", "ทศนิยมตำแหน่งที่ 4 = 1 PIP"), 13, C["bull"], "end", 700)
    s.line(702, 214, 702, 310, C["dim"], 1.5)
    s.text(712, 330, t("5th = pipette (1/10 pip)", "ตำแหน่งที่ 5 = Pipette (1/10 pip)"), 12, C["muted"], "start")
    s.rect(28, 360, 904, 62, fill=C["panel"], stroke=C["border"], rx=10)
    s.text(48, 386, t("BUY EUR/USD = buy euros, pay dollars → profit if the euro gets stronger.", "BUY EUR/USD = ซื้อยูโร จ่ายดอลลาร์ → กำไรถ้ายูโรแข็งค่าขึ้น"), 14, C["bull"], weight=600)
    s.text(48, 408, t("SELL EUR/USD = sell euros, get dollars → profit if the euro gets weaker.  (JPY pairs: 1 pip = 0.01)",
                      "SELL EUR/USD = ขายยูโร รับดอลลาร์ → กำไรถ้ายูโรอ่อนค่าลง  (คู่เงิน JPY: 1 pip = 0.01)"), 14, C["bear"], weight=600)
    return s.render()


@fig
def lots(lang):
    t = tr(lang)
    s = SVG(960, 400, t("Lots and pip value (pairs ending in USD)", "ขนาดล็อตและมูลค่าต่อ Pip (คู่เงินที่ลงท้ายด้วย USD)"),
            t("Pip value = units × 0.0001. Your risk = pips to stop × pip value.", "มูลค่าต่อ pip = จำนวนหน่วย × 0.0001  ความเสี่ยง = ระยะ pip ถึง Stop × มูลค่าต่อ pip"))
    rows = [(t("Standard lot", "ล็อตมาตรฐาน"), "1.00", "100,000", "10.00", "200.00"),
            (t("Mini lot", "มินิล็อต"), "0.10", "10,000", "1.00", "20.00"),
            (t("Micro lot", "ไมโครล็อต"), "0.01", "1,000", "0.10", "2.00")]
    heads = [t("Name", "ชื่อ"), t("Lots", "ล็อต"), t("Units of EUR", "จำนวนยูโร"), t("1 pip =", "1 pip ="), t("20-pip stop =", "Stop 20 pip =")]
    xs = [48, 280, 420, 610, 780]
    for x, h in zip(xs, heads):
        s.text(x, 120, h, 13, C["muted"], weight=700)
    for i, row in enumerate(rows):
        y = 136 + i * 70
        s.rect(28, y, 904, 58, fill=C["panel"], stroke=C["border"], rx=10)
        cols = [C["text"], C["blue"], C["text"], C["bull"], C["bear"]]
        for k, (x, v) in enumerate(zip(xs, row)):
            txt = v if k < 3 else f"{v} USD"
            s.text(x, y + 36, txt, 16, cols[k], weight=700 if k else 600)
    s.text(48, 370, t("Gold (XAU/USD) and crypto use different contract sizes — always check your broker's 'contract specification'.",
                      "ทองคำ (XAU/USD) และคริปโตใช้ขนาดสัญญาต่างกัน — ตรวจ 'Contract specification' ของโบรกเกอร์เสมอ"), 13, C["amber"], weight=600)
    return s.render()


@fig
def market_clock(lang):
    t = tr(lang)
    s = SVG(960, 400, t("The market clock in Thailand / Laos time (UTC+7)", "นาฬิกาตลาดตามเวลาไทย / ลาว (UTC+7)"),
            t("Northern-summer times (about mid-March to early November). In winter, London and New York start 1 hour LATER.",
              "เวลาช่วงฤดูร้อนซีกโลกเหนือ (ราวกลาง มี.ค. – ต้น พ.ย.) ช่วงฤดูหนาว ลอนดอนและนิวยอร์กเริ่ม ช้าลง 1 ชั่วโมง"))
    x0, w = 120, 800
    X = lambda h: x0 + w * ((h - 4) % 24) / 24  # axis starts 04:00
    for h in range(4, 29, 2):
        x = X(h % 24) if h % 24 != 4 or h == 4 else x0 + w
        s.line(x, 110, x, 300, C["grid"], 1)
        s.text(x, 320, f"{h % 24:02d}", 12, C["muted"], "middle")
    sess = [(t("Sydney", "ซิดนีย์"), 4, 13, C["purple"]), (t("Tokyo", "โตเกียว"), 7, 16, C["blue"]),
            (t("London", "ลอนดอน"), 14, 23, C["teal"]), (t("New York", "นิวยอร์ก"), 19, 28, C["amber"])]
    for i, (name, a, b, col) in enumerate(sess):
        y = 120 + i * 42
        s.rect(X(a), y, X(a) + w * (b - a) / 24 - X(a), 30, fill=col, rx=6, opacity=0.8)
        s.text(X(a) + 10, y + 20, f"{name}  {a:02d}:00–{b % 24:02d}:00", 13, C["white"], weight=700)
    s.rect(X(19), 112, w * 4 / 24, 186, fill=C["white"], opacity=0.06, stroke=C["amber"], rx=6, dash="5 4")
    s.text(X(21), 296, t("London–NY overlap: busiest", "ช่วงลอนดอน–นิวยอร์กซ้อนกัน: คึกคักสุด"), 11, C["amber"], "middle", 700)
    s.text(48, 356, t("US data (CPI, jobs): 19:30 · US stock open: 20:30 · Fed decision: 01:00 (next day) · Crypto: 24/7",
                      "ข้อมูลสหรัฐ (CPI, การจ้างงาน): 19:30 · ตลาดหุ้นสหรัฐเปิด: 20:30 · ประกาศ Fed: 01:00 (วันถัดไป) · คริปโต: 24/7"), 13, C["text"], weight=600)
    s.text(48, 380, t("Winter: add 1 hour to each (20:30 · 21:30 · 02:00).", "ฤดูหนาว: บวก 1 ชั่วโมงทุกรายการ (20:30 · 21:30 · 02:00)"), 12, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 0.8 news
@fig
def calendar_row(lang):
    t = tr(lang)
    s = SVG(960, 420, t("How to read an economic calendar", "วิธีอ่านปฏิทินเศรษฐกิจ"),
            t("The market moves on the SURPRISE: actual vs forecast — not on whether the number is 'good'.",
              "ตลาดขยับตาม ความเซอร์ไพรส์: ตัวเลขจริง vs คาดการณ์ — ไม่ใช่ว่าตัวเลข 'ดี' หรือไม่"))
    heads = [t("Time (UTC+7)", "เวลา (UTC+7)"), t("Cur.", "สกุล"), t("Impact", "ผลกระทบ"), t("Event", "เหตุการณ์"),
             t("Actual", "ตัวเลขจริง"), t("Forecast", "คาดการณ์"), t("Previous", "ครั้งก่อน")]
    xs = [40, 170, 240, 330, 620, 730, 840]
    s.rect(28, 100, 904, 40, fill=C["panel"], stroke=C["border"], rx=8)
    for x, h in zip(xs, heads):
        s.text(x, 126, h, 13, C["muted"], weight=700)
    rows = [("19:30", "USD", 3, t("Non-Farm Payrolls", "การจ้างงานนอกภาคเกษตร (NFP)"), "+275K", "+200K", "+229K", C["bull"]),
            ("19:30", "USD", 3, t("CPI y/y (inflation)", "CPI y/y (เงินเฟ้อ)"), "3.1%", "3.3%", "3.4%", C["bear"]),
            ("14:00", "GBP", 2, t("GDP m/m", "GDP m/m"), "0.2%", "0.2%", "-0.1%", C["muted"])]
    for i, (tm, cur, imp, ev, a, f, p, col) in enumerate(rows):
        y = 148 + i * 52
        s.rect(28, y, 904, 44, fill=C["bg"], stroke=C["border"], rx=8)
        vals = [tm, cur, None, ev, a, f, p]
        for k, (x, v) in enumerate(zip(xs, vals)):
            if k == 2:
                for d in range(3):
                    s.rect(x + d * 16, y + 15, 12, 14, fill=C["bear"] if d < imp else C["border"], rx=2)
            else:
                s.text(x, y + 28, v, 14, col if k == 4 else C["text"], weight=700 if k in (3, 4) else 500)
    s.text(40, 330, t("Row 1: jobs beat forecast by 75K → strong economy → rates may stay high → USD up, gold & stocks often down.",
                      "แถว 1: การจ้างงานดีกว่าคาด 75K → เศรษฐกิจแข็ง → ดอกเบี้ยอาจสูงนาน → USD ขึ้น ทองและหุ้นมักลง"), 13, C["bull"], weight=600)
    s.text(40, 356, t("Row 2: inflation BELOW forecast → rate cuts more likely → USD down, gold & stocks often up.",
                      "แถว 2: เงินเฟ้อ ต่ำกว่า คาด → โอกาสลดดอกเบี้ยมากขึ้น → USD ลง ทองและหุ้นมักขึ้น"), 13, C["bear"], weight=600)
    s.text(40, 382, t("Row 3: in line with forecast → little reaction. Three red bars = can move markets hard; plan around them.",
                      "แถว 3: ตรงตามคาด → ตลาดตอบสนองน้อย  สามแถบแดง = ขยับตลาดแรงได้ ต้องวางแผนรับมือ"), 13, C["muted"], weight=600)
    return s.render()


@fig
def news_spike(lang):
    t = tr(lang)
    s = SVG(960, 470, t("What a big release looks like on a 1-minute chart", "ข่าวใหญ่หน้าตาเป็นอย่างไรบนกราฟ 1 นาที"),
            t("Quiet → spike → whipsaw → real direction. Spreads widen and stops slip in the first seconds.",
              "เงียบ → พุ่ง → สะบัดไปมา → ทิศทางจริง  Spread กว้างขึ้นและ Stop ลื่นไถลในวินาทีแรก"))
    cs = candles_from_path([100, 100.4, 99.8, 100.2], [6, 4, 5], seed=31, vol=0.6)
    o = cs[-1][3]
    cs.append([o, o + 2.6, o - 0.3, o + 2.1])
    cs.append([o + 2.1, o + 2.3, o - 1.4, o - 0.9])
    cs.append([o - 0.9, o + 1.0, o - 1.2, o + 0.7])
    cs += candles_from_path([o + 0.7, o + 1.8, o + 1.3, o + 2.9], [4, 3, 5], seed=32)
    s.rect(28, 90, 904, 360, fill=C["panel"], stroke=C["border"], rx=12)
    ch = CandleChart(s, 40, 120, 880, 300, cs)
    k = 15
    x0 = ch.X(k) - ch.step / 2
    s.rect(x0, 112, ch.step * 3, 316, fill=C["amber"], opacity=0.10, rx=4)
    ch.draw()
    s.text(ch.X(k), 108, t("19:30 release", "19:30 ข่าวออก"), 12, C["amber"], "start", 700)
    ch.label(k, cs[k][1], t("1 · spike", "1 · พุ่ง"), C["bull"], dy=-10, anchor="end", dx=-10)
    ch.label(k + 1, cs[k + 1][2], t("2 · reversal: early buyers stopped out", "2 · กลับตัว: คนซื้อตามโดน Stop"), C["bear"], dy=22, anchor="start", dx=10)
    ch.label(len(cs) - 3, cs[-3][1], t("3 · real direction after 5–15 min", "3 · ทิศทางจริงหลัง 5–15 นาที"), C["teal"], dy=-14, anchor="end")
    s.text(56, 140, t("before: tiny candles,\neveryone waiting", "ก่อนข่าว: แท่งเล็ก\nทุกคนรอ"), 12, C["muted"])
    return s.render()


@fig
def what_moves(lang):
    t = tr(lang)
    s = SVG(960, 460, t("What moves each market", "อะไรขยับแต่ละตลาด"),
            t("Same news, different reactions. Learn the main driver of the market you trade.", "ข่าวเดียวกัน ปฏิกิริยาต่างกัน รู้ตัวขับเคลื่อนหลักของตลาดที่คุณเทรด"))
    cards = [
        (C["blue"], t("Forex", "ฟอเร็กซ์"), t("Interest-rate differences\nbetween countries, central\nbank speeches, CPI, jobs,\nGDP, trade, risk mood", "ส่วนต่างดอกเบี้ยระหว่างประเทศ\nสุนทรพจน์ธนาคารกลาง CPI\nการจ้างงาน GDP การค้า\nอารมณ์ความเสี่ยง")),
        (C["amber"], t("Gold", "ทองคำ"), t("Real interest rates (↓ = gold ↑),\nUS dollar (↓ = gold ↑), fear &\nwars, central-bank buying,\ninflation worries", "ดอกเบี้ยที่แท้จริง (↓ = ทอง ↑)\nดอลลาร์ (↓ = ทอง ↑) ความกลัว\nสงคราม ธนาคารกลางซื้อทอง\nความกังวลเงินเฟ้อ")),
        (C["bull"], t("Stocks & indices", "หุ้นและดัชนี"), t("Earnings & guidance, interest\nrates, economic growth, sector\nnews (AI, chips), big-tech\nresults, buybacks", "ผลประกอบการและประมาณการ\nดอกเบี้ย การเติบโตเศรษฐกิจ\nข่าวอุตสาหกรรม (AI ชิป)\nงบบริษัทเทคใหญ่ การซื้อหุ้นคืน")),
        (C["purple"], t("Crypto", "คริปโต"), t("Global liquidity & risk mood,\nETF flows, regulation news,\nleverage liquidations,\nexchange hacks / failures", "สภาพคล่องโลกและอารมณ์เสี่ยง\nเงินไหลเข้า ETF ข่าวกฎหมาย\nการล้างพอร์ตเลเวอเรจ\nแฮ็ก / ล้มของแพลตฟอร์ม")),
    ]
    for k, (col, head, body) in enumerate(cards):
        x = 28 + k * 230
        s.card(x, 96, 216, 170, head, body, col, 18, 13)
    s.rect(28, 286, 904, 156, fill=C["panel"], stroke=C["border"], rx=12)
    s.text(48, 316, t("Example: US inflation comes in HOTTER than forecast", "ตัวอย่าง: เงินเฟ้อสหรัฐออกมา สูงกว่า คาด"), 16, C["text"], weight=700)
    chain = [(t("Rates stay\nhigher for longer", "ดอกเบี้ยสูง\nนานขึ้น"), C["muted"]), (t("USD ↑", "USD ↑"), C["bull"]),
             (t("EUR/USD ↓", "EUR/USD ↓"), C["bear"]), (t("Gold ↓", "ทอง ↓"), C["bear"]), (t("Nasdaq ↓", "Nasdaq ↓"), C["bear"]), (t("Bitcoin ↓", "Bitcoin ↓"), C["bear"])]
    for i, (txt, col) in enumerate(chain):
        x = 48 + i * 148
        s.rect(x, 338, 128, 64, fill=col, opacity=0.12, stroke=col, rx=8)
        s.text(x + 64, 364, txt, 13, C["text"], "middle", 700)
        if i < len(chain) - 1:
            s.arrow(x + 130, 370, x + 146, 370, C["muted"], 1.5)
    s.text(48, 426, t("Typical first reaction, not a rule — positioning and other news can change it.", "ปฏิกิริยาแรกที่พบบ่อย ไม่ใช่กฎตายตัว — สถานะของตลาดและข่าวอื่นเปลี่ยนผลได้"), 12, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 0.2 instruments
@fig
def wrappers(lang):
    t = tr(lang)
    s = SVG(960, 560, t("One asset, five wrappers", "สินทรัพย์เดียว ห่อได้ห้าแบบ"),
            t("Gold, the S&P 500 or Bitcoin can each be traded in several ways. The price is the same; the contract is not.",
              "ทองคำ S&P 500 หรือ Bitcoin เทรดได้หลายแบบ ราคาเดียวกัน แต่สัญญาต่างกัน"))
    s.circle(480, 150, 52, C["amber"])
    s.text(480, 146, t("GOLD", "ทองคำ"), 20, C["bg"], "middle", 800)
    s.text(480, 168, t("the asset", "ตัวสินทรัพย์"), 12, C["bg"], "middle", 600)
    cards = [
        (C["bull"], t("Spot", "Spot"), t("You OWN it\n(bar, coin, share)\nNo expiry\nNo leverage", "คุณ เป็นเจ้าของ\n(แท่ง เหรียญ หุ้น)\nไม่มีวันหมดอายุ\nไม่มีเลเวอเรจ")),
        (C["pink"], t("CFD", "CFD"), t("Contract with\nyour BROKER\nNo expiry, swap\nHigh leverage", "สัญญากับ\nโบรกเกอร์\nไม่หมดอายุ มี Swap\nเลเวอเรจสูง")),
        (C["blue"], t("Futures", "ฟิวเจอร์ส"), t("Contract on an\nEXCHANGE (CME)\nHas an expiry\nMargin, leverage", "สัญญาบน\nตลาด (CME)\nมีวันหมดอายุ\nมาร์จิ้น เลเวอเรจ")),
        (C["teal"], t("ETF", "ETF"), t("A SHARE of a fund\nthat holds gold\nNo expiry\nYearly fee", "หน่วยของกองทุน\nที่ถือทองคำ\nไม่หมดอายุ\nค่าธรรมเนียมรายปี")),
        (C["purple"], t("Option", "ออปชัน"), t("The RIGHT to buy\nor sell later\nHas an expiry\nsee 8.1", "สิทธิ ซื้อหรือขาย\nในอนาคต\nมีวันหมดอายุ\nดู 8.1")),
    ]
    for k, (col, head, body) in enumerate(cards):
        x = 28 + k * 182
        s.arrow(480, 204, x + 84, 258, col, 1.6)
        s.card(x, 262, 170, 168, head, body, col, 18, 13)
    s.rect(28, 452, 904, 86, fill=C["panel"], stroke=C["border"], rx=12)
    s.text(48, 482, t("Ask three questions about any product:", "ถามสามข้อกับทุกผลิตภัณฑ์:"), 15, C["text"], weight=700)
    s.text(48, 510, t("① Who is on the other side?   ② Does it expire?   ③ Can I lose more than I deposited?",
                      "① ใครอยู่อีกฝั่ง?   ② มีวันหมดอายุไหม?   ③ ขาดทุนเกินเงินที่ฝากได้ไหม?"), 15, C["amber"], weight=600)
    return s.render()


@fig
def margin_call(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Margin call and stop out: 0.20 lot gold, 2,000 USD account", "Margin call และ Stop out: ทองคำ 0.20 ล็อต บัญชี 2,000 ดอลลาร์"),
            t("Bought at 4,000 with 1:100 leverage → 800 USD margin locked. No stop loss.",
              "ซื้อที่ 4,000 เลเวอเรจ 1:100 → ล็อกมาร์จิ้น 800 ดอลลาร์ ไม่มี Stop loss"))
    x0, x1, y0, y1 = 120, 900, 110, 410
    pmin, pmax, emin, emax = 3910, 4000, 0, 2200
    X = lambda p: x0 + (pmax - p) / (pmax - pmin) * (x1 - x0)
    Y = lambda e: y1 - (e - emin) / (emax - emin) * (y1 - y0)
    for e in range(0, 2201, 400):
        s.line(x0, Y(e), x1, Y(e), C["grid"], 1)
        s.text(x0 - 10, Y(e) + 4, f"{e:,}", 12, C["muted"], "end")
    for p in range(4000, 3909, -10):
        s.text(X(p), y1 + 22, f"{p:,}", 12, C["muted"], "middle")
    s.text((x0 + x1) / 2, y1 + 46, t("Gold price (USD) — falling →", "ราคาทอง (ดอลลาร์) — ร่วงลง →"), 13, C["muted"], "middle", 600)
    s.text(40, 100, t("Equity (USD)", "มูลค่าบัญชี (ดอลลาร์)"), 12, C["muted"], weight=600)
    s.rect(X(3920), y0, x1 - X(3920), y1 - y0, fill=C["bear"], opacity=0.10)
    s.line(x0, Y(800), x1, Y(800), C["amber"], 1.6, "6 5")
    s.text(x0 + 8, Y(800) - 8, t("Margin call: equity = margin (800) → margin level 100%", "Margin call: มูลค่าบัญชี = มาร์จิ้น (800) → Margin level 100%"), 13, C["amber"], weight=700)
    s.line(x0, Y(400), x1, Y(400), C["bear"], 1.6, "6 5")
    s.text(x0 + 8, Y(400) - 8, t("Stop out: margin level 50% → broker closes the trade", "Stop out: Margin level 50% → โบรกเกอร์ปิดไม้ให้"), 13, C["bear"], weight=700)
    s.polyline([(X(4000), Y(2000)), (X(3920), Y(400))], C["blue"], 3)
    s.polyline([(X(3920), Y(400)), (x1, Y(400))], C["blue"], 3, "3 5")
    for p, e, lab, col, dy in ((4000, 2000, t("start: 2,000", "เริ่ม: 2,000"), C["text"], -14),
                               (3940, 800, t("3,940 (−60)", "3,940 (−60)"), C["amber"], 26),
                               (3920, 400, t("3,920 (−80, only −2%)", "3,920 (−80 แค่ −2%)"), C["bear"], 26)):
        s.circle(X(p), Y(e), 6, col)
        s.text(X(p), Y(e) + dy, lab, 13, col, "middle", 700)
    s.text(x1 - 4, y0 + 22, t("trade closed here:\nloss 1,600 USD (−80%)", "ไม้ถูกปิดที่นี่:\nขาดทุน 1,600 ดอลลาร์ (−80%)"), 13, C["bear"], "end", 700)
    return s.render()


@fig
def futures_curve(lang):
    t = tr(lang)
    s = SVG(960, 430, t("Futures curve: contango vs backwardation", "เส้นโค้งฟิวเจอร์ส: Contango กับ Backwardation"),
            t("Each dot is the price of a contract that expires in a different month.", "แต่ละจุดคือราคาของสัญญาที่หมดอายุคนละเดือน"))
    months = ["Spot", "Dec", "Feb", "Apr", "Jun", "Aug"]
    if lang == "th":
        months = ["Spot", "ธ.ค.", "ก.พ.", "เม.ย.", "มิ.ย.", "ส.ค."]
    for k, (title, col, vals, note) in enumerate((
            (t("Contango (normal for gold)", "Contango (ปกติของทองคำ)"), C["blue"], [round(4000 * (1 + 0.04 * m / 12)) for m in (0, 2, 4, 6, 8, 10)],
             t("Later = more expensive.\nThe gap ≈ interest for holding\ngold until that month.", "ยิ่งไกล = ยิ่งแพง\nส่วนต่าง ≈ ดอกเบี้ยของการถือ\nทองไปจนถึงเดือนนั้น")),
            (t("Backwardation", "Backwardation"), C["amber"], [80, 78.5, 77, 75.8, 74.9, 74.2],
             t("Later = cheaper. People want\nit NOW (e.g. oil in a supply\nshortage).", "ยิ่งไกล = ยิ่งถูก คนต้องการ\nของ ตอนนี้ (เช่น น้ำมัน\nช่วงขาดแคลน)")))):
        bx = 28 + k * 462
        s.rect(bx, 92, 442, 318, fill=C["panel"], stroke=C["border"], rx=12)
        s.text(bx + 20, 122, title, 16, col, weight=700)
        lo, hi = min(vals), max(vals)
        pts = []
        for i, v in enumerate(vals):
            x = bx + 50 + i * 70
            y = 300 - (v - lo) / (hi - lo) * 140
            pts.append((x, y))
            s.text(x, 330, months[i], 12, C["muted"], "middle")
        s.polyline(pts, col, 3)
        for i, (x, y) in enumerate(pts):
            s.circle(x, y, 5, col)
            if i in (0, len(pts) - 1):
                s.text(x, y - 14, f"{vals[i]:,}", 12, C["text"], "middle", 700)
        s.text(bx + 20, 360, note, 13, C["text"])
    return s.render()


@fig
def leveraged_etf_decay(lang):
    t = tr(lang)
    s = SVG(960, 460, t("Why leveraged ETFs decay in a choppy market", "ทำไม ETF แบบเลเวอเรจจึงเสื่อมค่าในตลาดที่แกว่ง"),
            t("20 days: the index goes +5%, −5%, +5%, −5% … and ends almost flat. The 3× ETF does not.",
              "20 วัน: ดัชนีขึ้น +5% ลง −5% สลับกัน … จบเกือบที่เดิม แต่ ETF 3 เท่าไม่ใช่"))
    x0, x1, y0, y1 = 90, 720, 110, 380
    vmin, vmax = 60, 130
    X = lambda d: x0 + d / 20 * (x1 - x0)
    Y = lambda v: y1 - (v - vmin) / (vmax - vmin) * (y1 - y0)
    for v in range(60, 131, 10):
        s.line(x0, Y(v), x1, Y(v), C["grid"], 1)
        s.text(x0 - 10, Y(v) + 4, str(v), 12, C["muted"], "end")
    for d in range(0, 21, 5):
        s.text(X(d), y1 + 22, t(f"day {d}", f"วันที่ {d}"), 12, C["muted"], "middle")
    a, b = [100.0], [100.0]
    for d in range(20):
        r = 0.05 if d % 2 == 0 else -0.05
        a.append(a[-1] * (1 + r))
        b.append(b[-1] * (1 + 3 * r))
    s.line(x0, Y(100), x1, Y(100), C["dim"], 1.2, "4 4")
    s.polyline([(X(d), Y(v)) for d, v in enumerate(a)], C["blue"], 2.5)
    s.polyline([(X(d), Y(v)) for d, v in enumerate(b)], C["bear"], 2.5)
    s.text(X(20) + 12, Y(a[-1]) + 5, t(f"Index: {a[-1]:.1f}  (−{100 - a[-1]:.1f}%)", f"ดัชนี: {a[-1]:.1f}  (−{100 - a[-1]:.1f}%)"), 14, C["blue"], weight=700)
    s.text(X(20) + 12, Y(b[-1]) + 5, t(f"3× ETF: {b[-1]:.1f}  (−{100 - b[-1]:.1f}%)", f"ETF 3 เท่า: {b[-1]:.1f}  (−{100 - b[-1]:.1f}%)"), 14, C["bear"], weight=700)
    s.text(28, 442, t("Each day the 3× fund resets. Losses are taken from a bigger base than gains → it bleeds when price chops.",
                      "กองทุน 3 เท่ารีเซ็ตทุกวัน ขาดทุนคิดจากฐานที่ใหญ่กว่ากำไร → ตลาดแกว่งเมื่อไหร่ก็เสื่อมค่า"), 13, C["amber"], weight=600)
    return s.render()


# ---------------------------------------------------------------- 0.4 gold
@fig
def gold_drivers(lang):
    t = tr(lang)
    s = SVG(960, 400, t("Gold's dashboard: four main drivers", "แผงหน้าปัดของทองคำ: ตัวขับเคลื่อนหลัก 4 ตัว"),
            t("Typical relationships, not laws. They can break for months (see section 3).",
              "ความสัมพันธ์ที่พบบ่อย ไม่ใช่กฎตายตัว บางช่วงก็ไม่เป็นไปตามนี้นานหลายเดือน (ดูหัวข้อ 3)"))
    items = [
        (C["blue"], t("Real interest rates", "ดอกเบี้ยที่แท้จริง"), "↑", "↓",
         t("Gold pays no interest. When safe\nbonds pay more after inflation,\nholding gold costs more.", "ทองไม่จ่ายดอกเบี้ย เมื่อพันธบัตร\nให้ผลตอบแทนหลังเงินเฟ้อสูงขึ้น\nการถือทองก็มีต้นทุนสูงขึ้น")),
        (C["teal"], t("US dollar", "ดอลลาร์สหรัฐ"), "↑", "↓",
         t("Gold is priced in USD. A stronger\ndollar makes gold dearer for\neveryone else.", "ทองตั้งราคาเป็นดอลลาร์ ดอลลาร์\nแข็งทำให้ทองแพงขึ้นสำหรับ\nคนที่ใช้สกุลอื่น")),
        (C["bear"], t("Fear & crisis", "ความกลัวและวิกฤต"), "↑", "↑",
         t("Wars, bank failures, market\ncrashes → people want an asset\nwith no issuer that can fail.", "สงคราม ธนาคารล้ม ตลาดถล่ม\n→ คนต้องการสินทรัพย์ที่ไม่มี\nผู้ออกที่จะล้มได้")),
        (C["amber"], t("Central-bank buying", "ธนาคารกลางซื้อทอง"), "↑", "↑",
         t("Steady, price-insensitive buyers\nthat diversify reserves away\nfrom the dollar.", "ผู้ซื้อที่ซื้อสม่ำเสมอไม่สนราคา\nเพื่อกระจายทุนสำรอง\nออกจากดอลลาร์")),
    ]
    for k, (col, head, a, b, body) in enumerate(items):
        x = 28 + k * 230
        s.rect(x, 96, 216, 250, fill=C["panel"], stroke=C["border"], rx=12)
        s.rect(x, 96, 216, 5, fill=col, rx=2)
        s.text(x + 108, 130, head, 16, col, "middle", 700)
        s.text(x + 60, 196, a, 44, col, "middle", 800)
        s.text(x + 156, 196, b, 44, C["bull"] if b == "↑" else C["bear"], "middle", 800)
        s.text(x + 60, 222, t("driver", "ตัวขับ"), 12, C["muted"], "middle")
        s.text(x + 156, 222, t("gold", "ทอง"), 12, C["muted"], "middle")
        s.arrow(x + 86, 182, x + 128, 182, C["muted"], 1.5)
        s.text(x + 16, 262, body, 12, C["text"])
    s.text(28, 378, t("Also watch: inflation expectations, Indian & Chinese jewellery demand, ETF flows (e.g. GLD holdings).",
                      "ควรดูด้วย: การคาดการณ์เงินเฟ้อ ความต้องการทองรูปพรรณในอินเดียและจีน เงินไหลเข้าออก ETF (เช่น GLD)"), 13, C["muted"], weight=600)
    return s.render()


@fig
def thai_gold(lang):
    t = tr(lang)
    s = SVG(960, 470, t("From XAU/USD to the Thai gold price", "จาก XAU/USD สู่ราคาทองไทย"),
            t("Example numbers: gold 4,000 USD/oz, USD/THB 33.00. One baht-weight bar = 15.244 g of 96.5% gold.",
              "ตัวเลขตัวอย่าง: ทอง 4,000 ดอลลาร์/ออนซ์ USD/THB 33.00 ทองแท่ง 1 บาท = 15.244 กรัม ความบริสุทธิ์ 96.5%"))
    steps = [
        (C["amber"], t("World price", "ราคาโลก"), "4,000", t("USD per troy oz\n(31.1035 g pure)", "ดอลลาร์ต่อทรอยออนซ์\n(ทองบริสุทธิ์ 31.1035 กรัม)")),
        (C["teal"], t("Pure gold in 1 baht", "ทองบริสุทธิ์ใน 1 บาท"), "0.47295", t("oz = 15.244 × 0.965\n÷ 31.1035", "ออนซ์ = 15.244 × 0.965\n÷ 31.1035")),
        (C["blue"], t("Exchange rate", "อัตราแลกเปลี่ยน"), "33.00", t("THB per USD", "บาทต่อดอลลาร์")),
        (C["bull"], t("Thai bar price", "ราคาทองแท่งไทย"), "≈ 62,430", t("THB per baht-weight\n(before shop margin)", "บาทต่อทอง 1 บาท\n(ก่อนส่วนต่างร้านทอง)")),
    ]
    for k, (col, head, big, small) in enumerate(steps):
        x = 28 + k * 232
        s.rect(x, 100, 208, 190, fill=C["panel"], stroke=col, rx=12)
        s.text(x + 104, 130, head, 14, col, "middle", 700)
        s.text(x + 104, 186, big, 30, C["text"], "middle", 800)
        s.text(x + 104, 226, small, 12, C["muted"], "middle")
        if k < 3:
            s.text(x + 220, 196, "×" if k < 2 else "=", 26, C["muted"], "middle", 700)
    s.rect(28, 312, 904, 140, fill=C["panel"], stroke=C["border"], rx=12)
    s.text(48, 342, t("Thai price ≈ XAU/USD × USD/THB × 0.47295", "ราคาทองไทย ≈ XAU/USD × USD/THB × 0.47295"), 18, C["amber"], weight=700)
    s.text(48, 374, t("Gold +10 USD (rate fixed)  →  +156 THB per baht-weight", "ทอง +10 ดอลลาร์ (ค่าเงินคงที่)  →  +156 บาท ต่อทอง 1 บาท"), 14, C["text"], weight=600)
    s.text(48, 400, t("Baht weakens 33.00 → 33.10 (gold fixed)  →  +189 THB per baht-weight", "บาทอ่อน 33.00 → 33.10 (ทองคงที่)  →  +189 บาท ต่อทอง 1 บาท"), 14, C["text"], weight=600)
    s.text(48, 428, t("So Thai gold can rise on a day when world gold is flat — because the baht fell.", "ทองไทยจึงขึ้นได้ในวันที่ทองโลกไม่ขยับ — เพราะเงินบาทอ่อนลง"), 13, C["muted"])
    return s.render()


@fig
def gold_sizing(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Sizing a gold trade (CFD, 1 lot = 100 oz)", "คำนวณขนาดไม้ทองคำ (CFD 1 ล็อต = 100 ออนซ์)"),
            t("Account 2,000 USD, risk 1% = 20 USD. Check your broker's contract size first!",
              "บัญชี 2,000 ดอลลาร์ เสี่ยง 1% = 20 ดอลลาร์ ตรวจขนาดสัญญาของโบรกเกอร์ก่อนเสมอ!"))
    heads = [t("Lots", "ล็อต"), t("Ounces", "ออนซ์"), t("1 USD move =", "ขยับ 1 ดอลลาร์ ="), t("5 USD stop =", "Stop 5 ดอลลาร์ ="), t("15 USD stop =", "Stop 15 ดอลลาร์ =")]
    xs = [48, 200, 360, 560, 750]
    for x, h in zip(xs, heads):
        s.text(x, 116, h, 13, C["muted"], weight=700)
    rows = [("1.00", "100", 100), ("0.10", "10", 10), ("0.04", "4", 4), ("0.01", "1", 1)]
    for i, (lot, oz, v) in enumerate(rows):
        y = 130 + i * 58
        hl = lot == "0.04"
        s.rect(28, y, 904, 48, fill=C["bull"] if hl else C["panel"], opacity=0.15 if hl else 1, stroke=C["bull"] if hl else C["border"], rx=10)
        vals = [lot, oz, f"{v:,} USD", f"{5 * v:,} USD", f"{15 * v:,} USD"]
        for k, (x, val) in enumerate(zip(xs, vals)):
            col = C["blue"] if k == 0 else (C["bear"] if k >= 3 else C["text"])
            s.text(x, y + 31, val, 16, col, weight=700)
    s.text(48, 384, t("Lots = risk ÷ (stop in USD × 100) = 20 ÷ (5 × 100) = 0.04  ✓", "ล็อต = ความเสี่ยง ÷ (Stop เป็นดอลลาร์ × 100) = 20 ÷ (5 × 100) = 0.04  ✓"), 15, C["bull"], weight=700)
    s.text(48, 412, t("Smallest size 0.01 lot = 1 USD per 1 USD move → with 20 USD risk, your stop can be at most 20 USD wide.",
                      "ขนาดเล็กสุด 0.01 ล็อต = 1 ดอลลาร์ต่อการขยับ 1 ดอลลาร์ → เสี่ยง 20 ดอลลาร์ Stop กว้างได้ไม่เกิน 20 ดอลลาร์"), 13, C["amber"], weight=600)
    return s.render()


@fig
def gold_day(lang):
    t = tr(lang)
    s = SVG(960, 420, t("A gold trading day in Thailand / Laos time (UTC+7)", "หนึ่งวันของทองคำตามเวลาไทย / ลาว (UTC+7)"),
            t("Northern-summer times. In northern winter, the London and New York events come 1 hour LATER.",
              "เวลาช่วงฤดูร้อนซีกโลกเหนือ ช่วงฤดูหนาว เหตุการณ์ของลอนดอนและนิวยอร์กจะ ช้าลง 1 ชั่วโมง"))
    x0, w = 60, 840
    X = lambda h: x0 + w * ((h - 5) % 24) / 24
    for h in range(5, 30, 2):
        x = X(h % 24) if h < 29 else x0 + w
        s.line(x, 100, x, 250, C["grid"], 1)
        s.text(x, 270, f"{h % 24:02d}", 12, C["muted"], "middle")
    bands = [(t("Asia: Shanghai, Tokyo — calmer", "เอเชีย: เซี่ยงไฮ้ โตเกียว — ค่อนข้างเงียบ"), 7, 14, C["blue"]),
             (t("London", "ลอนดอน"), 14, 23, C["teal"]), (t("New York (COMEX)", "นิวยอร์ก (COMEX)"), 19, 28, C["amber"])]
    for i, (name, a, b, col) in enumerate(bands):
        y = 110 + i * 44
        s.rect(X(a), y, w * (b - a) / 24, 32, fill=col, rx=6, opacity=0.8)
        s.text(X(a) + 10, y + 21, name, 13, C["white"], weight=700)
    ev = [(16.5, t("16:30 LBMA AM", "16:30 LBMA AM"), C["pink"]), (19.5, t("19:30 US data", "19:30 ข้อมูลสหรัฐ"), C["bear"]),
          (21.0, t("21:00 LBMA PM", "21:00 LBMA PM"), C["pink"]), (1.0, t("01:00 Fed", "01:00 Fed"), C["bear"])]
    for k, (h, lab, col) in enumerate(ev):
        x = X(h)
        s.line(x, 96, x, 250, col, 2, "4 3")
        s.text(x, 300 + (k % 2) * 20, lab, 12, col, "middle", 700)
    s.text(48, 362, t("Most of gold's daily range usually happens from London open to the first hours of New York.",
                      "ช่วงที่ทองวิ่งมากที่สุดของวันมักอยู่ระหว่างลอนดอนเปิดถึงชั่วโมงแรก ๆ ของนิวยอร์ก"), 14, C["text"], weight=600)
    s.text(48, 388, t("Winter: LBMA 17:30 & 22:00 · US data 20:30 · Fed 02:00.", "ฤดูหนาว: LBMA 17:30 และ 22:00 · ข้อมูลสหรัฐ 20:30 · Fed 02:00"), 13, C["muted"])
    return s.render()


@fig
def gold_round(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Gold and round numbers: a sweep of 4,000", "ทองกับเลขกลม: การกวาด (Sweep) ที่ 4,000"),
            t("Illustration, not real data. Stops pile up just under obvious levels (see 5.1–5.2).",
              "ภาพประกอบ ไม่ใช่ข้อมูลจริง Stop มักกองอยู่ใต้ระดับที่เห็นชัด (ดู 5.1–5.2)"))
    cs = candles_from_path([4030, 4004, 4022, 4003, 4026], [5, 4, 4, 4], seed=7, vol=0.4)
    o = cs[-1][3]
    cs += candles_from_path([o, 4008], [4], seed=8, vol=0.3)
    o = cs[-1][3]
    cs.append([o, o + 2, 3991.5, 4006.0])
    cs += candles_from_path([4006.0, 4018, 4012, 4038], [3, 2, 4], seed=9, vol=0.4)
    s.rect(28, 90, 904, 360, fill=C["panel"], stroke=C["border"], rx=12)
    ch = CandleChart(s, 40, 110, 880, 320, cs, pmin=3985, pmax=4045)
    k = 21
    ch.zone(3992, 4000, C["bear"], t("stops of buyers sit here", "Stop ของฝั่งซื้อกองอยู่ตรงนี้"), 0, k - 1, 0.12, label_pos="below")
    ch.hline(4000, t("4,000 round number", "เลขกลม 4,000"), C["amber"])
    ch.draw(highlight={k: C["amber"]})
    ch.label(k, cs[k][2], t("wick under 4,000, close back above", "ไส้เทียนหลุด 4,000 แล้วปิดกลับขึ้นมา"), C["amber"], dy=22, anchor="start", dx=16)
    return s.render()


# ---------------------------------------------------------------- 0.5 stocks & indices
@fig
def share_slices(lang):
    t = tr(lang)
    s = SVG(960, 440, t("A share = a slice of a business", "หุ้น = ส่วนแบ่งชิ้นหนึ่งของธุรกิจ"),
            t("A noodle shop is split into 1,000 equal shares. You buy 10.", "ร้านก๋วยเตี๋ยวถูกแบ่งเป็น 1,000 หุ้นเท่า ๆ กัน คุณซื้อ 10 หุ้น"))
    cx, cy, r = 200, 250, 130
    import math
    for k in range(40):
        a0, a1 = k / 40 * 2 * math.pi - math.pi / 2, (k + 1) / 40 * 2 * math.pi - math.pi / 2
        col = C["amber"] if k == 0 else C["panel"]
        pts = [(cx, cy)] + [(cx + r * math.cos(a0 + (a1 - a0) * j / 6), cy + r * math.sin(a0 + (a1 - a0) * j / 6)) for j in range(7)]
        s.polygon(pts, col, 1, C["border"])
    s.text(cx + 40, cy - r - 10, t("your 1%", "ของคุณ 1%"), 14, C["amber"], "start", 700)
    rows = [(C["text"], t("Shop profit this year", "กำไรร้านปีนี้"), "100,000 USD", t("→ your 1% share", "→ ส่วนของคุณ 1%"), "1,000 USD"),
            (C["bull"], t("Paid out as dividend (40%)", "จ่ายเป็นเงินปันผล (40%)"), "40,000 USD", t("→ cash to you", "→ เงินสดถึงคุณ"), "400 USD"),
            (C["blue"], t("Kept to open a 2nd shop", "เก็บไว้เปิดสาขา 2"), "60,000 USD", t("→ shop worth more", "→ ร้านมีมูลค่ามากขึ้น"), t("price ↑ ?", "ราคา ↑ ?")),
            (C["purple"], t("Buyback: shop buys 100 shares", "ซื้อหุ้นคืน 100 หุ้น"), t("900 left", "เหลือ 900"), t("→ you now own", "→ คุณถือ"), "1.11%")]
    for i, (col, a, b, c, d) in enumerate(rows):
        y = 118 + i * 72
        s.rect(380, y, 552, 58, fill=C["panel"], stroke=C["border"], rx=10)
        s.rect(380, y, 5, 58, fill=col, rx=2)
        s.text(398, y + 24, a, 14, col, weight=700)
        s.text(398, y + 46, b, 13, C["muted"])
        s.text(700, y + 24, c, 13, C["muted"])
        s.text(700, y + 46, d, 16, C["text"], weight=700)
    return s.render()


@fig
def index_weights(lang):
    t = tr(lang)
    s = SVG(960, 500, t("S&P 500: the 10 biggest weights", "S&P 500: 10 อันดับน้ำหนักมากที่สุด"),
            t("Weights in SPY (tracks the S&P 500), 29 Sep 2026. Source: stockanalysis.com. These change every day.",
              "น้ำหนักใน SPY (ตามดัชนี S&P 500) 29 ก.ย. 2026 ที่มา: stockanalysis.com ตัวเลขเปลี่ยนทุกวัน"))
    data = [("Nvidia", 8.32), ("Apple", 7.27), ("Microsoft", 5.72), ("Amazon", 3.66), ("Alphabet A", 3.03),
            ("Broadcom", 2.56), ("Meta", 2.46), ("Alphabet C", 2.43), ("Micron", 1.82), ("Tesla", 1.50)]
    for i, (name, w) in enumerate(data):
        y = 100 + i * 32
        s.text(170, y + 19, name, 14, C["text"], "end", 600)
        s.rect(184, y + 4, w * 60, 22, fill=C["blue"] if i else C["bull"], rx=4, opacity=0.9)
        s.text(184 + w * 60 + 8, y + 20, f"{w:.2f}%", 13, C["text"], weight=700)
    s.rect(28, 432, 904, 52, fill=C["panel"], stroke=C["border"], rx=10)
    s.text(48, 464, t("Top 10 ≈ 38.8% of the index. The other ~490 companies share the remaining ~61%.",
                      "10 อันดับแรก ≈ 38.8% ของดัชนี บริษัทอีกราว 490 แห่งแบ่งกันอีก ~61%"), 15, C["amber"], weight=700)
    s.text(760, 160, t("Same company,\ntwo share classes\n(A and C)", "บริษัทเดียวกัน\nหุ้นสองประเภท\n(A และ C)"), 12, C["muted"])
    return s.render()


@fig
def stock_gap(lang):
    t = tr(lang)
    s = SVG(960, 470, t("An earnings gap: the stop doesn't protect you overnight", "Gap จากงบ: Stop ไม่ได้ปกป้องคุณข้ามคืน"),
            t("Illustration, not real data. Close 100 → bad results after the close → opens at 88.",
              "ภาพประกอบ ไม่ใช่ข้อมูลจริง ปิด 100 → งบแย่ออกหลังตลาดปิด → เปิดที่ 88"))
    cs = candles_from_path([97, 101.5, 99, 102, 100.3], [5, 3, 4, 3], seed=21, vol=0.4)
    cs[-1][3] = 100.0
    cs[-1][1] = max(cs[-1][1], 100.4)
    cs.append([88.0, 89.6, 86.4, 87.2])
    cs += candles_from_path([87.2, 85.5, 88.5, 86.5], [3, 3, 3], seed=22, vol=0.4)
    s.rect(28, 90, 904, 360, fill=C["panel"], stroke=C["border"], rx=12)
    ch = CandleChart(s, 40, 110, 880, 320, cs, pmin=83, pmax=104)
    k = 15
    ch.hline(95, t("your stop 95", "Stop ของคุณ 95"), C["bear"], 0, k, side="left")
    ch.draw(highlight={k: C["amber"]})
    ch.arrow(k - 1, 100.0, k, 88.6, C["amber"], 2, "5 4")
    ch.label(k - 1, 100.6, t("close 100", "ปิด 100"), C["text"], dy=-10)
    ch.label(k, cs[k][2], t("opens 88: stop fills ~88, not 95", "เปิด 88: Stop ได้ราคา ~88 ไม่ใช่ 95"), C["amber"], dy=24, anchor="start", dx=14)
    s.text(ch.X(k) + 20, ch.Y(95.5), t("no trades\nin between", "ไม่มีการซื้อขาย\nระหว่างทาง"), 12, C["muted"])
    return s.render()


@fig
def stock_clock(lang):
    t = tr(lang)
    s = SVG(960, 400, t("Stock market hours in Thailand / Laos time (UTC+7)", "เวลาตลาดหุ้นตามเวลาไทย / ลาว (UTC+7)"),
            t("US times for northern summer. In northern winter, US sessions start and end 1 hour LATER.",
              "เวลาสหรัฐช่วงฤดูร้อนซีกโลกเหนือ ช่วงฤดูหนาว ตลาดสหรัฐเปิดและปิด ช้าลง 1 ชั่วโมง"))
    x0, w = 60, 840
    X = lambda h: x0 + w * ((h - 7) % 24) / 24
    for h in range(7, 32, 2):
        x = X(h % 24) if h < 31 else x0 + w
        s.line(x, 100, x, 290, C["grid"], 1)
        s.text(x, 310, f"{h % 24:02d}", 12, C["muted"], "middle")
    s.text(X(11.5) + 10, 112 + 20, t("LSX (Laos) 08:30–11:30", "LSX (ลาว) 08:30–11:30"), 12, C["purple"], weight=700)
    s.text(X(16.5) + 10, 154 + 20, t("SET (Thailand) 10:00–12:30 · 14:00–16:30", "SET (ไทย) 10:00–12:30 · 14:00–16:30"), 12, C["teal"], weight=700)
    bars = [("", 8.5, 11.5, C["purple"], 0),
            ("", 10, 12.5, C["teal"], 1),
            ("", 14, 16.5, C["teal"], 1),
            (t("US pre-market 15:00–20:30", "US ก่อนเปิด 15:00–20:30"), 15, 20.5, C["dim"], 2),
            (t("US regular 20:30–03:00", "US ปกติ 20:30–03:00"), 20.5, 27, C["amber"], 3),
            (t("after-hours → 07:00", "หลังปิด → 07:00"), 27, 31, C["dim"], 3)]
    for name, a, b, col, row in bars:
        y = 112 + row * 42
        s.rect(X(a), y, w * (b - a) / 24, 30, fill=col, rx=6, opacity=0.85)
        s.text(X(a) + 8, y + 20, name, 12, C["white"], weight=700)
    s.text(48, 344, t("Big US company results usually come out after 03:00 (before the open, or after the close): price GAPS at the next open.",
                      "งบบริษัทใหญ่ของสหรัฐมักออกนอกเวลาตลาด (ก่อนเปิดหรือหลังปิด): ราคาจะ กระโดด (Gap) ตอนเปิดครั้งถัดไป"), 13, C["text"], weight=600)
    s.text(48, 370, t("Winter: US regular 21:30–04:00. SET and LSX don't change (no daylight saving).",
                      "ฤดูหนาว: ตลาดสหรัฐปกติ 21:30–04:00  SET และ LSX ไม่เปลี่ยน (ไม่มีการปรับเวลาออมแสง)"), 12, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 0.6 nvidia
@fig
def nvda_drivers(lang):
    t = tr(lang)
    s = SVG(960, 500, t("What moves Nvidia (NVDA)", "อะไรขยับ Nvidia (NVDA)"),
            t("One company, many forces. Earnings night is when they all get tested at once.",
              "บริษัทเดียว หลายแรง คืนประกาศงบคือคืนที่ทุกแรงถูกทดสอบพร้อมกัน"))
    cx, cy = 480, 290
    nodes = [(170, 140, C["amber"], t("Earnings & guidance", "งบและประมาณการ"), t("4×/year, after US close", "ปีละ 4 ครั้ง หลังตลาดสหรัฐปิด")),
             (480, 120, C["blue"], t("Big Tech AI spending", "งบลงทุน AI ของบริษัทเทคใหญ่"), t("capex plans of cloud giants", "แผนลงทุนของยักษ์คลาวด์")),
             (790, 140, C["bear"], t("Export rules (China)", "กฎส่งออก (จีน)"), t("licences, bans, tariffs", "ใบอนุญาต การห้าม ภาษี")),
             (170, 440, C["purple"], t("Competition", "คู่แข่ง"), t("AMD, custom chips, cheaper AI", "AMD ชิปสั่งทำ AI ราคาถูก")),
             (480, 460, C["teal"], t("Supply (TSMC)", "การผลิต (TSMC)"), t("can enough chips be made?", "ผลิตชิปได้พอไหม?")),
             (790, 440, C["pink"], t("Interest rates & mood", "ดอกเบี้ยและอารมณ์ตลาด"), t("growth stocks are rate-sensitive", "หุ้นเติบโตไวต่อดอกเบี้ย"))]
    for x, y, col, head, body in nodes:
        s.line(cx, cy, x, y, col, 1.5, "5 4")
        s.rect(x - 140, y - 34, 280, 62, fill=C["panel"], stroke=col, rx=10)
        s.text(x, y - 10, head, 15, col, "middle", 700)
        s.text(x, y + 14, body, 12, C["muted"], "middle")
    s.circle(cx, cy, 62, C["bull"])
    s.text(cx, cy - 4, "NVDA", 24, C["bg"], "middle", 800)
    s.text(cx, cy + 18, t("AI chips", "ชิป AI"), 13, C["bg"], "middle", 700)
    return s.render()


@fig
def earnings_move(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Nvidia, 26–27 Aug 2026: priced move vs actual move", "Nvidia 26–27 ส.ค. 2026: การขยับที่ตลาดคาด vs ที่เกิดจริง"),
            t("Options priced about ±5.4% for the day after results. The stock rose about 8.7%.",
              "ออปชันตั้งราคาการขยับราว ±5.4% ในวันหลังประกาศงบ หุ้นขึ้นจริงราว 8.7%"))
    x0, zero, sc = 120, 480, 30
    s.line(zero, 220, zero, 360, C["dim"], 1.5)
    for v in range(-10, 11, 2):
        x = zero + v * sc
        s.line(x, 360, x, 366, C["dim"], 1)
        s.text(x, 384, f"{v:+d}%" if v else "0", 12, C["muted"], "middle")
    s.rect(zero - 5.4 * sc, 130, 10.8 * sc, 70, fill=C["blue"], opacity=0.25, stroke=C["blue"], rx=6)
    s.text(zero, 160, t("options' expected range ±5.4%", "กรอบที่ออปชันคาด ±5.4%"), 14, C["blue"], "middle", 700)
    s.text(zero, 182, t("(about 68% of outcomes expected inside)", "(คาดว่าราว 68% ของผลลัพธ์อยู่ในกรอบ)"), 12, C["muted"], "middle")
    s.rect(zero, 240, 8.7 * sc, 60, fill=C["bull"], opacity=0.85, rx=6)
    s.text(zero + 8.7 * sc + 10, 276, t("actual ≈ +8.7%", "จริง ≈ +8.7%"), 16, C["bull"], "start", 700)
    s.text(zero - 10, 276, t("next-day move", "การขยับวันถัดไป"), 13, C["text"], "end", 600)
    s.text(48, 412, t("Sources: CryptoDaily (options data, 26 Aug 2026); CNBC (27 Aug 2026). Other services quoted 5.9–7.0% at other times.",
                      "ที่มา: CryptoDaily (ข้อมูลออปชัน 26 ส.ค. 2026); CNBC (27 ส.ค. 2026) บริการอื่นรายงาน 5.9–7.0% ในเวลาต่างกัน"), 12, C["muted"])
    return s.render()


@fig
def nvda_chart(lang):
    t = tr(lang)
    s = SVG(960, 470, t("A high-growth stock around earnings (daily candles)", "หุ้นเติบโตสูงช่วงประกาศงบ (แท่งเทียนรายวัน)"),
            t("Illustration in the style of NVDA, not real prices. Note the gaps at each report.",
              "ภาพประกอบสไตล์ NVDA ไม่ใช่ราคาจริง สังเกต Gap ทุกครั้งที่ประกาศงบ"))
    cs = candles_from_path([180, 196, 188, 205], [8, 5, 7], seed=41, vol=0.5)
    o = cs[-1][3]
    cs.append([o * 0.93, o * 0.945, o * 0.905, o * 0.915])
    cs += candles_from_path([cs[-1][3], 182, 194, 201], [6, 7, 6], seed=42, vol=0.5)
    o = cs[-1][3]
    cs.append([o * 1.07, o * 1.095, o * 1.06, o * 1.085])
    cs += candles_from_path([cs[-1][3], 212, 222], [4, 5], seed=43, vol=0.5)
    s.rect(28, 90, 904, 360, fill=C["panel"], stroke=C["border"], rx=12)
    ch = CandleChart(s, 40, 110, 880, 320, cs)
    e1, e2 = 20, 40
    ch.draw(highlight={e1: C["bear"], e2: C["bull"]})
    ch.label(e1, cs[e1][2], t("report 1: gap down ~7%\n(\"good, but not good enough\")", "งบ 1: Gap ลง ~7%\n(\"ดี แต่ไม่ดีพอ\")"), C["bear"], dy=24)
    ch.label(e2, cs[e2][1], t("report 2: gap up ~7%", "งบ 2: Gap ขึ้น ~7%"), C["bull"], dy=-14)
    s.text(60, 140, t("between reports: drift with\nAI news and the market", "ระหว่างงบ: ไหลตามข่าว AI\nและตลาดโดยรวม"), 12, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 0.7 crypto
@fig
def ledger(lang):
    t = tr(lang)
    s = SVG(960, 470, t("A blockchain = a village notebook everyone copies", "บล็อกเชน = สมุดบัญชีของหมู่บ้านที่ทุกคนถือสำเนา"),
            t("No bank in the middle: thousands of computers keep the same list of who sent what to whom.",
              "ไม่มีธนาคารตรงกลาง: คอมพิวเตอร์นับพันเครื่องเก็บรายการเดียวกันว่าใครส่งอะไรให้ใคร"))
    pages = [(t("Page 1", "หน้า 1"), ["A → B  2", "C → A  1"]), (t("Page 2", "หน้า 2"), ["B → D  1", "A → C  0.5"]),
             (t("Page 3", "หน้า 3"), ["D → E  0.3", "C → B  1"]), (t("Page 4 (new)", "หน้า 4 (ใหม่)"), ["E → A  0.1", "…"])]
    for i, (head, rows) in enumerate(pages):
        x = 40 + i * 225
        col = C["amber"] if i == 3 else C["blue"]
        s.rect(x, 100, 180, 150, fill=C["panel"], stroke=col, rx=10)
        s.text(x + 90, 128, head, 15, col, "middle", 700)
        for k, r in enumerate(rows):
            s.text(x + 22, 162 + k * 26, r, 14, C["text"], weight=600)
        s.text(x + 90, 236, t("seal: links to page before", "ตราผนึก: โยงกับหน้าก่อน"), 11, C["muted"], "middle")
        if i < 3:
            s.arrow(x + 182, 175, x + 222, 175, C["muted"], 2)
    for k in range(7):
        x = 90 + k * 120
        s.circle(x, 320, 22, C["panel"], C["teal"], 2)
        s.text(x, 326, "📒", 16, C["text"], "middle")
    s.text(480, 370, t("Every computer holds a full copy. To cheat, you'd have to change most copies at once.",
                       "ทุกเครื่องมีสำเนาครบ จะโกงได้ต้องแก้สำเนาส่วนใหญ่พร้อมกัน"), 14, C["teal"], "middle", 700)
    s.rect(28, 396, 904, 56, fill=C["panel"], stroke=C["border"], rx=10)
    s.text(48, 420, t("Bitcoin: the notebook only records bitcoin; max 21 million coins.  Ether: the notebook can also run programs (smart contracts).",
                      "Bitcoin: สมุดบันทึกเฉพาะบิตคอยน์ สูงสุด 21 ล้านเหรียญ  Ether: สมุดนี้รันโปรแกรมได้ด้วย (Smart contract)"), 13, C["text"], weight=600)
    s.text(48, 442, t("Stablecoin: a token that promises 1 coin = 1 USD, backed by reserves held by a company.",
                      "Stablecoin: โทเคนที่สัญญาว่า 1 เหรียญ = 1 ดอลลาร์ โดยมีทุนสำรองที่บริษัทถือไว้หนุนหลัง"), 13, C["muted"])
    return s.render()


@fig
def volatility_compare(lang):
    t = tr(lang)
    s = SVG(960, 460, t("How much does each market move in a day?", "แต่ละตลาดขยับวันละเท่าไหร่?"),
            t("Average absolute daily % change, 4 Jul – 30 Sep 2026, and the biggest single day.",
              "ค่าเฉลี่ยการเปลี่ยนแปลงรายวัน (ไม่คิดเครื่องหมาย) 4 ก.ค. – 30 ก.ย. 2026 และวันที่ขยับมากที่สุด"))
    data = [("EUR/USD", 0.20, 0.84, C["blue"]), (t("Gold", "ทองคำ"), 1.14, 4.96, C["amber"]),
            ("Bitcoin", 1.33, 7.25, C["purple"]), ("Ether", 1.74, 17.5, C["pink"])]
    s.text(250, 116, t("average day", "วันเฉลี่ย"), 13, C["muted"], weight=700)
    s.text(610, 116, t("biggest day", "วันที่แรงที่สุด"), 13, C["muted"], weight=700)
    for i, (name, avg, mx, col) in enumerate(data):
        y = 132 + i * 66
        s.text(220, y + 28, name, 16, col, "end", 700)
        s.rect(250, y + 8, avg * 150, 30, fill=col, rx=5, opacity=0.9)
        s.text(250 + avg * 150 + 8, y + 29, f"{avg:.2f}%", 14, C["text"], weight=700)
        s.rect(610, y + 8, mx * 16, 30, fill=col, rx=5, opacity=0.45)
        s.text(610 + mx * 16 + 8, y + 29, f"{mx:.1f}%", 14, C["text"], weight=700)
    s.text(28, 412, t("Sources: CoinGecko daily prices (Bitcoin, Ether, PAX Gold token for gold); ECB reference rates via frankfurter.app (EUR/USD, weekdays).",
                      "ที่มา: ราคารายวัน CoinGecko (Bitcoin, Ether, โทเคน PAX Gold แทนทอง); อัตราอ้างอิง ECB ผ่าน frankfurter.app (EUR/USD วันทำการ)"), 11, C["muted"])
    s.text(28, 434, t("Crypto counted over all 7 days a week. Volatility changes over time: measure it yourself with ATR (0.4).",
                      "คริปโตนับครบ 7 วันต่อสัปดาห์ ความผันผวนเปลี่ยนตามเวลา วัดเองด้วย ATR (0.4)"), 11, C["muted"])
    return s.render()


@fig
def liquidation_cascade(lang):
    t = tr(lang)
    s = SVG(960, 480, t("A liquidation cascade (long squeeze)", "การล้างพอร์ตต่อเนื่อง (Long squeeze)"),
            t("Illustration, not real data. Forced selling at each cluster of liquidation prices pushes price into the next one.",
              "ภาพประกอบ ไม่ใช่ข้อมูลจริง การบังคับขายที่กลุ่มราคาล้างพอร์ตแต่ละกลุ่ม ดันราคาลงไปหากลุ่มถัดไป"))
    cs = candles_from_path([83000, 84200, 83300, 84000, 82900], [5, 4, 4, 4], seed=51, vol=0.4)
    o = cs[-1][3]
    for c, h, l in ((81600, o + 150, 81300), (79700, 81700, 79300), (77600, 79800, 77100)):
        cs.append([o, h, l, c])
        o = c
    cs += candles_from_path([o, 79500, 78800, 80300], [3, 3, 4], seed=52, vol=0.4)
    s.rect(28, 90, 904, 370, fill=C["panel"], stroke=C["border"], rx=12)
    ch = CandleChart(s, 40, 110, 880, 330, cs, pmin=76500, pmax=85000)
    for p, lab in ((82000, t("50× longs liquidated", "Long 50× ถูกล้าง")), (80000, t("20× longs", "Long 20×")), (78000, t("10× longs", "Long 10×"))):
        ch.hline(p, lab, C["bear"], dash="4 4", side="left")
    ch.draw(highlight={18: C["amber"], 19: C["amber"]})
    ch.label(19, cs[19][2], t("forced selling feeds itself", "การบังคับขายป้อนตัวเอง"), C["amber"], dy=24, anchor="start", dx=10)
    ch.label(len(cs) - 1, 81400, t("bounce once the forced sellers are gone", "เด้งกลับเมื่อคนที่ถูกบังคับขายหมดไป"), C["teal"], dy=0, anchor="end")
    return s.render()


@fig
def funding(lang):
    t = tr(lang)
    s = SVG(960, 420, t("Perpetual futures: the funding rate", "Perpetual futures: Funding rate"),
            t("No expiry, so a small payment between longs and shorts (often every 8 hours) keeps the price near spot.",
              "ไม่มีวันหมดอายุ จึงมีการจ่ายเงินเล็กน้อยระหว่างฝั่ง Long และ Short (มักทุก 8 ชั่วโมง) เพื่อให้ราคาใกล้ Spot"))
    for k, (head, cond, col, a, b) in enumerate((
            (t("Funding POSITIVE", "Funding เป็นบวก"), t("perp price above spot\n(too many longs)", "ราคา Perp สูงกว่า Spot\n(Long เยอะเกินไป)"), C["bull"], t("Longs", "Long"), t("Shorts", "Short")),
            (t("Funding NEGATIVE", "Funding เป็นลบ"), t("perp price below spot\n(too many shorts)", "ราคา Perp ต่ำกว่า Spot\n(Short เยอะเกินไป)"), C["bear"], t("Shorts", "Short"), t("Longs", "Long")))):
        x = 28 + k * 462
        s.rect(x, 96, 442, 230, fill=C["panel"], stroke=col, rx=12)
        s.text(x + 221, 126, head, 18, col, "middle", 700)
        s.text(x + 221, 152, cond, 13, C["muted"], "middle")
        s.rect(x + 30, 200, 130, 60, fill=col, opacity=0.2, stroke=col, rx=10)
        s.text(x + 95, 236, a, 16, C["text"], "middle", 700)
        s.rect(x + 282, 200, 130, 60, fill=C["blue"], opacity=0.2, stroke=C["blue"], rx=10)
        s.text(x + 347, 236, b, 16, C["text"], "middle", 700)
        s.arrow(x + 164, 230, x + 278, 230, C["amber"], 2.5)
        s.text(x + 221, 220, t("pay", "จ่าย"), 13, C["amber"], "middle", 700)
        s.text(x + 221, 300, t("→ discourages new " + ("longs" if k == 0 else "shorts"), "→ ทำให้คนไม่อยากเปิด " + ("Long" if k == 0 else "Short") + " เพิ่ม"), 13, C["text"], "middle", 600)
    s.text(48, 362, t("Example: +0.01% per 8 h on a 10,000 USD long = 1 USD each time, 3 USD a day, about 11% a year.",
                      "ตัวอย่าง: +0.01% ต่อ 8 ชม. บน Long 10,000 ดอลลาร์ = ครั้งละ 1 ดอลลาร์ วันละ 3 ดอลลาร์ ราว 11% ต่อปี"), 14, C["amber"], weight=600)
    s.text(48, 390, t("Very high positive funding = crowded longs: a warning sign, not a buy signal.",
                      "Funding บวกสูงมาก = Long แออัด: สัญญาณเตือน ไม่ใช่สัญญาณซื้อ"), 13, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 0.9 scams
@fig
def scam_funnel(lang):
    t = tr(lang)
    s = SVG(960, 500, t("How a 'pig-butchering' scam works", "กลโกง 'เชือดหมู' (Pig-butchering) ทำงานอย่างไร"),
            t("It takes weeks. Every step is designed to build trust before the money disappears.",
              "ใช้เวลาหลายสัปดาห์ ทุกขั้นถูกออกแบบให้สร้างความไว้ใจก่อนที่เงินจะหายไป"))
    steps = [(C["blue"], t("1 · Contact", "1 · ทัก"), t("'Wrong number' message, dating app,\nLINE / Facebook friend request", "ข้อความ 'ทักผิดคน' แอปหาคู่\nขอเป็นเพื่อนใน LINE / Facebook")),
             (C["teal"], t("2 · Friendship", "2 · สร้างสัมพันธ์"), t("Daily chats for weeks. Photos of a\nsuccessful life. No money talk yet.", "คุยทุกวันหลายสัปดาห์ รูปชีวิตที่ประสบ\nความสำเร็จ ยังไม่พูดเรื่องเงิน")),
             (C["purple"], t("3 · The 'opportunity'", "3 · 'โอกาส'"), t("'My uncle has inside info…' Points you\nto a trading app or website", "'ลุงฉันมีข้อมูลวงใน…' ชี้ไปที่\nแอปหรือเว็บเทรด")),
             (C["amber"], t("4 · Small win", "4 · ชนะเล็กน้อย"), t("Deposit a little, withdraw a little.\nIt works! Trust grows.", "ฝากนิดหน่อย ถอนได้นิดหน่อย\nได้จริง! ความไว้ใจเพิ่ม")),
             (C["pink"], t("5 · Go big", "5 · ลงหนัก"), t("Screen shows huge 'profits'. Pressure\nto deposit savings, borrow money", "หน้าจอโชว์ 'กำไร' มหาศาล กดดัน\nให้ฝากเงินเก็บ กู้เงินมาเพิ่ม")),
             (C["bear"], t("6 · The trap", "6 · กับดัก"), t("Withdrawal 'needs a tax / fee first'.\nPay it → another fee → contact vanishes", "ถอนเงิน 'ต้องจ่ายภาษี / ค่าธรรมเนียมก่อน'\nจ่าย → มีค่าอื่นอีก → ติดต่อไม่ได้"))]
    for i, (col, head, body) in enumerate(steps):
        y = 96 + i * 64
        w = 904 - i * 60
        x = 28 + i * 30
        s.rect(x, y, w, 54, fill=col, opacity=0.14, stroke=col, rx=10)
        s.text(x + 18, y + 33, head, 16, col, weight=700)
        s.text(x + 250, y + 22, body, 13, C["text"])
    s.text(480, 488, t("The 'profit' was only a number on a screen the scammers control. There was never any trading.",
                       "'กำไร' เป็นแค่ตัวเลขบนหน้าจอที่มิจฉาชีพควบคุม ไม่เคยมีการเทรดจริงเลย"), 13, C["amber"], "middle", 700)
    return s.render()


@fig
def red_flags(lang):
    t = tr(lang)
    s = SVG(960, 520, t("Red-flag checklist: stop if you see even ONE", "เช็กลิสต์สัญญาณอันตราย: หยุดทันทีถ้าเจอแม้แต่ ข้อเดียว"),
            t("Print it, screenshot it, send it to your family.", "พิมพ์ แคปหน้าจอ ส่งให้ครอบครัว"))
    flags = [(t("Guaranteed or fixed returns", "รับประกันผลตอบแทน หรือผลตอบแทนคงที่"), t("'10% a month, no risk'", "'เดือนละ 10% ไม่มีความเสี่ยง'")),
             (t("Urgency", "เร่งรีบ"), t("'Only today', 'last 3 seats'", "'วันนี้วันเดียว' 'เหลือ 3 ที่สุดท้าย'")),
             (t("Secrecy", "ให้เก็บเป็นความลับ"), t("'Don't tell your family / bank'", "'อย่าบอกครอบครัว / ธนาคาร'")),
             (t("Rewards for recruiting", "ได้รางวัลเมื่อชวนคนอื่น"), t("bonus for every friend who joins", "โบนัสทุกครั้งที่ชวนเพื่อนเข้า")),
             (t("Not licensed", "ไม่มีใบอนุญาต"), t("not on the regulator's own register", "ไม่อยู่ในทะเบียนของผู้กำกับดูแล")),
             (t("Withdrawal problems", "ถอนเงินมีปัญหา"), t("fees, 'taxes', delays before you can withdraw", "ค่าธรรมเนียม 'ภาษี' ถ่วงเวลาก่อนถอน")),
             (t("Celebrity or 'mentor' ads", "โฆษณาคนดัง หรือ 'เมนเทอร์'"), t("famous faces, Lamborghinis, screenshots of profits", "หน้าคนดัง รถหรู ภาพกำไร")),
             (t("Contact starts with them", "เขาเป็นฝ่ายทักมาก่อน"), t("unknown message, 'account manager' call", "ข้อความจากคนไม่รู้จัก โทรจาก 'ผู้จัดการบัญชี'"))]
    for i, (head, ex) in enumerate(flags):
        col, row = i % 2, i // 2
        x, y = 28 + col * 458, 96 + row * 100
        s.rect(x, y, 446, 88, fill=C["panel"], stroke=C["bear"], rx=12)
        s.rect(x + 18, y + 24, 26, 26, fill="none", stroke=C["bear"], sw=2, rx=5)
        s.text(x + 31, y + 44, "✗", 18, C["bear"], "middle", 700)
        s.text(x + 60, y + 38, head, 16, C["text"], weight=700)
        s.text(x + 60, y + 64, ex, 13, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 0.10 checkpoint
@fig
def summary(lang):
    t = tr(lang)
    s = SVG(960, 630, t("Phase 0 on one page", "สรุปเฟส 0 ในหน้าเดียว"))
    cx, cy = 480, 340
    nodes = [
        (165, 130, C["blue"], t("0.1 Exchanges & brokers", "0.1 ตลาดและโบรกเกอร์"), t("Exchange model vs CFD model.\nCheck the licence yourself.", "แบบตลาดกลาง vs แบบ CFD\nตรวจใบอนุญาตเอง")),
        (480, 110, C["pink"], t("0.2 Wrappers & leverage", "0.2 ห่อและเลเวอเรจ"), t("Who's on the other side?\nSize from the stop.", "ใครอยู่อีกฝั่ง?\nขนาดไม้มาจาก Stop")),
        (795, 130, C["teal"], t("0.3 Forex", "0.3 ฟอเร็กซ์"), t("1 pip = 0.0001. Lots from\nrisk ÷ (stop × pip value).", "1 pip = 0.0001 ล็อตจาก\nความเสี่ยง ÷ (Stop × มูลค่า pip)")),
        (165, 340, C["amber"], t("0.4 Gold", "0.4 ทองคำ"), t("Real yields, USD, fear,\ncentral banks. 1 lot = 100 oz.", "Real yield ดอลลาร์ ความกลัว\nธนาคารกลาง 1 ล็อต = 100 ออนซ์")),
        (795, 340, C["bull"], t("0.5–0.6 Stocks & Nvidia", "0.5–0.6 หุ้นและ Nvidia"), t("Price = expected profits.\nEarnings gaps; index weights.", "ราคา = กำไรที่คาด\nGap จากงบ น้ำหนักในดัชนี")),
        (165, 550, C["purple"], t("0.7 Crypto", "0.7 คริปโต"), t("24/7, very volatile.\nNot your keys, not your coins.", "24/7 ผันผวนสูง\nไม่ใช่คีย์คุณ ก็ไม่ใช่เหรียญคุณ")),
        (480, 570, C["bear"], t("0.8 News", "0.8 ข่าว"), t("Markets move on the surprise.\nTimes in UTC+7 (+1 h winter).", "ตลาดขยับตามความเซอร์ไพรส์\nเวลา UTC+7 (ฤดูหนาว +1 ชม.)")),
        (795, 550, C["text"], t("0.9 Scams", "0.9 กลโกง"), t("Guaranteed returns = scam.\nVerify on the regulator's site.", "รับประกันผลตอบแทน = กลโกง\nตรวจบนเว็บผู้กำกับดูแล")),
    ]
    for x, y, col, head, body in nodes:
        s.line(cx, cy, x, y, col, 2, opacity=0.5)
    s.circle(cx, cy, 78, C["panel"], C["text"], 2)
    s.text(cx, cy - 4, t("PHASE 0", "เฟส 0"), 20, C["text"], "middle", 700)
    s.text(cx, cy + 20, t("The Playing Field", "สนามเล่น"), 14, C["muted"], "middle")
    for x, y, col, head, body in nodes:
        s.rect(x - 135, y - 42, 270, 86, fill=C["panel"], stroke=col, rx=12)
        s.text(x, y - 16, head, 15, col, "middle", 700)
        s.text(x, y + 8, body, 12, C["text"], "middle")
    return s.render()


# ---------------------------------------------------------------- 0.11 (C1)
@fig
def money_ladder(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Money comes in this order: trading is the last step", "เงินต้องเรียงตามลำดับนี้: การเทรดคือขั้นสุดท้าย"),
            t("Climb one step at a time. Each step protects the one above it.", "ขึ้นทีละขั้น แต่ละขั้นปกป้องขั้นที่อยู่ข้างบน"))
    steps = [
        (t("1 · Budget & bills paid", "1 · ทำงบและจ่ายบิลครบ"), t("Know your essential monthly costs", "รู้ค่าใช้จ่ายจำเป็นต่อเดือน"), C["blue"]),
        (t("2 · Starter emergency fund", "2 · เงินสำรองฉุกเฉินเริ่มต้น"), t("About 1 month of essentials in cash", "ค่าใช้จ่ายจำเป็นราว 1 เดือนเป็นเงินสด"), C["teal"]),
        (t("3 · Pay off high-interest debt", "3 · ปลดหนี้ดอกเบี้ยสูง"), t("Credit cards, personal loans: a sure 16–25% 'return'", "บัตรเครดิต สินเชื่อบุคคล: 'ผลตอบแทน' 16–25% แน่นอน"), C["bear"]),
        (t("4 · Full emergency fund", "4 · เงินสำรองฉุกเฉินเต็มจำนวน"), t("3–6 months of essentials", "ค่าใช้จ่ายจำเป็น 3–6 เดือน"), C["teal"]),
        (t("5 · Long-term investing", "5 · ลงทุนระยะยาว"), t("Diversified, low-cost, by your IPS (11.2)", "กระจายความเสี่ยง ต้นทุนต่ำ ตาม IPS (11.2)"), C["bull"]),
        (t("6 · Trading (risk capital)", "6 · การเทรด (เงินที่เสี่ยงได้)"), t("Small; losing all of it wouldn't change your life", "จำนวนน้อย เสียทั้งหมดแล้วชีวิตไม่เปลี่ยน"), C["amber"]),
    ]
    for k, (head, body, col) in enumerate(steps):
        x, y = 40 + k * 112, 400 - k * 52
        s.rect(x, y, 290, 46, fill=C["panel"], stroke=col, sw=2, rx=10)
        s.text(x + 14, y + 20, head, 14, col, weight=700)
        s.text(x + 14, y + 38, body, 11, C["muted"])
    return s.render()


def _payoff(bal, rate, pay):
    r, path, tot = rate / 12, [bal], 0.0
    while bal > 0 and len(path) < 600:
        i = bal * r
        tot += i
        bal = max(bal + i - pay, 0)
        path.append(bal)
    return path, tot


@fig
def debt_payoff(lang):
    t = tr(lang)
    s = SVG(960, 460, t("A 50,000 THB credit-card balance at 16% a year", "ยอดบัตรเครดิต 50,000 บาท ดอกเบี้ย 16% ต่อปี"),
            t("Same debt, three monthly payments (computed, interest charged monthly).", "หนี้เท่ากัน จ่ายต่อเดือนสามแบบ (คำนวณจริง คิดดอกเบี้ยรายเดือน)"))
    x0, y0, w, h = 80, 100, 560, 300
    s.rect(x0 - 50, y0 - 10, w + 70, h + 50, fill=C["panel"], stroke=C["border"], rx=12)
    X = lambda mth: x0 + w * mth / 84
    Y = lambda v: y0 + h * (1 - v / 50000)
    for v in (0, 25000, 50000):
        s.line(x0, Y(v), x0 + w, Y(v), C["grid"], 1)
        s.text(x0 - 6, Y(v) + 4, f"{v:,}", 11, C["muted"], "end")
    for mth in (0, 12, 24, 36, 48, 60, 72, 84):
        s.text(X(mth), y0 + h + 20, t(f"{mth} mo", f"{mth} ด."), 11, C["muted"], "middle")
    rows = []
    for pay, col in ((1000, C["bear"]), (2000, C["amber"]), (5000, C["bull"])):
        path, tot = _payoff(50000, 0.16, pay)
        s.polyline([(X(i), Y(v)) for i, v in enumerate(path)], col, 2.5)
        rows.append((pay, len(path) - 1, tot, col))
    for k, (pay, mo, tot, col) in enumerate(rows):
        y = 110 + k * 100
        s.card(670, y, 260, 88, t(f"Pay {pay:,} THB / month", f"จ่าย {pay:,} บาท / เดือน"), None, col, 15)
        s.text(690, y + 58, t(f"{mo} months · interest {tot:,.0f} THB", f"{mo} เดือน · ดอกเบี้ย {tot:,.0f} บาท"), 13, C["text"])
    return s.render()


@fig
def risk_capital(lang):
    t = tr(lang)
    s = SVG(960, 460, t("How much of your savings is 'money you can afford to risk'?", "เงินออมส่วนไหนคือ 'เงินที่เสี่ยงได้'?"),
            t("Example: 400,000 THB savings, essential costs 19,000 THB a month (illustrative).", "ตัวอย่าง: เงินออม 400,000 บาท ค่าใช้จ่ายจำเป็น 19,000 บาทต่อเดือน (ตัวอย่าง)"))
    parts = [(t("Savings", "เงินออม"), 400000, 0, C["blue"]),
             (t("− Emergency fund\n(6 × 19,000)", "− เงินสำรองฉุกเฉิน\n(6 × 19,000)"), -114000, 400000, C["teal"]),
             (t("− Needed within\n3 years", "− ต้องใช้ภายใน\n3 ปี"), -150000, 286000, C["purple"]),
             (t("= Investable", "= ลงทุนได้"), 136000, 0, C["bull"]),
             (t("Trading money\n(≤ 10% of it)", "เงินเทรด\n(≤ 10% ของส่วนนี้)"), 13600, 0, C["amber"])]
    base, sc = 380, 260 / 400000
    for k, (name, v, start, col) in enumerate(parts):
        x = 60 + k * 175
        top = start if v < 0 else v
        bot = start + v if v < 0 else 0
        s.rect(x, base - top * sc, 110, max((top - bot) * sc, 3), fill=col, opacity=0.85, rx=4)
        s.text(x + 55, base - top * sc - 8, f"{abs(v):,}", 13, col, "middle", 700)
        s.text(x + 55, base + 22, name, 12, C["text"], "middle", 600)
    s.text(60, 445, t("At 1% risk per trade, 1R on a 13,600 THB account is 136 THB.", "ที่ความเสี่ยง 1% ต่อไม้ 1R ของบัญชี 13,600 บาท คือ 136 บาท"), 13, C["amber"], weight=600)
    return s.render()


# ---------------------------------------------------------------- 0.12 short selling (C2)
@fig
def short_steps(lang):
    t = tr(lang)
    s = SVG(960, 420, t("How a short sale works (shares)", "การขายชอร์ตทำงานอย่างไร (หุ้น)"),
            t("Example: 100 shares, sold at 50, bought back at 40 (illustrative).", "ตัวอย่าง: 100 หุ้น ขายที่ 50 ซื้อคืนที่ 40 (ตัวอย่าง)"))
    steps = [(t("1 · Borrow", "1 · ยืม"), t("Your broker borrows\n100 shares for you", "โบรกเกอร์ยืม\n100 หุ้นให้คุณ"), C["blue"]),
             (t("2 · Sell", "2 · ขาย"), t("Sell them at 50:\n+5,000 in cash", "ขายที่ 50:\n+5,000 เป็นเงินสด"), C["amber"]),
             (t("3 · Buy back", "3 · ซื้อคืน"), t("Later buy 100\nat 40: −4,000", "ภายหลังซื้อคืน 100\nที่ 40: −4,000"), C["teal"]),
             (t("4 · Return", "4 · คืน"), t("Give the shares back.\nKeep 1,000 − fees", "คืนหุ้น\nเก็บ 1,000 − ค่าธรรมเนียม"), C["bull"])]
    for k, (head, body, col) in enumerate(steps):
        x = 40 + k * 228
        s.rect(x, 130, 200, 130, fill=C["panel"], stroke=col, sw=2, rx=12)
        s.text(x + 100, 165, head, 17, col, "middle", 700)
        s.text(x + 100, 200, body, 13, C["text"], "middle")
        if k < 3:
            s.arrow(x + 204, 195, x + 224, 195, C["dim"], 2)
    s.text(40, 310, t("While the short is open you pay: a borrow fee (e.g. 0.30% a year → 5,000 × 0.003 × 30/360 = 1.25 for 30 days),",
                      "ระหว่างที่ชอร์ตอยู่คุณจ่าย: ค่ายืม (เช่น 0.30% ต่อปี → 5,000 × 0.003 × 30/360 = 1.25 สำหรับ 30 วัน)"), 13, C["text"])
    s.text(40, 334, t("and any dividend (0.50 per share × 100 = 50). A hard-to-borrow stock at 50% a year would cost 208.33 for the same 30 days.",
                      "และเงินปันผลที่จ่ายระหว่างนั้น (0.50 ต่อหุ้น × 100 = 50) หุ้นที่ยืมยากที่ 50% ต่อปีจะมีค่ายืม 208.33 ใน 30 วันเดียวกัน"), 13, C["text"])
    s.text(40, 378, t("If the price rises instead, you must buy back higher: the loss has no ceiling.", "ถ้าราคาขึ้นแทน คุณต้องซื้อคืนแพงกว่า: การขาดทุนไม่มีเพดาน"), 14, C["bear"], weight=700)
    return s.render()


@fig
def short_payoff(lang):
    t = tr(lang)
    s = SVG(960, 460, t("Long vs short: the loss limits are not symmetric", "ซื้อ vs ชอร์ต: ขีดจำกัดการขาดทุนไม่สมมาตรกัน"),
            t("100 shares opened at 50, no stop. Profit or loss at the price shown on the axis.",
              "100 หุ้น เปิดที่ 50 ไม่มี Stop กำไรหรือขาดทุนที่ราคาบนแกน"))
    x0, y0, w, h = 110, 100, 760, 300
    s.rect(x0 - 80, y0 - 14, w + 110, h + 64, fill=C["panel"], stroke=C["border"], rx=12)
    X = lambda p: x0 + w * p / 150
    Y = lambda v: y0 + h * (10000 - v) / 20000
    for v in (-10000, -5000, 0, 5000, 10000):
        s.line(x0, Y(v), x0 + w, Y(v), C["dim"] if v == 0 else C["grid"], 1.5 if v == 0 else 1)
        s.text(x0 - 8, Y(v) + 4, f"{v:+,}", 11, C["muted"], "end")
    for p in (0, 25, 50, 75, 100, 125, 150):
        s.text(X(p), y0 + h + 20, str(p), 11, C["muted"], "middle")
    s.polyline([(X(0), Y(-5000)), (X(150), Y(10000))], C["bull"], 3)
    s.polyline([(X(0), Y(5000)), (X(150), Y(-10000))], C["bear"], 3)
    s.text(X(140), Y(9000) + 22, t("long: +10,000 at 150 · worst case −5,000 at 0", "ซื้อ: +10,000 ที่ 150 · แย่สุด −5,000 ที่ 0"), 12, C["bull"], "end", 700)
    s.text(X(140), Y(-9000) + 22, t("short: −5,000 at 100, −10,000 at 150, no limit", "ชอร์ต: −5,000 ที่ 100 −10,000 ที่ 150 ไม่มีขีดจำกัด"), 12, C["bear"], "end", 700)
    s.text(X(2), Y(5000) - 10, t("short's best case +5,000 (price 0)", "ชอร์ตดีที่สุด +5,000 (ราคา 0)"), 12, C["bear"], "start", 600)
    return s.render()


@fig
def squeeze_loop(lang):
    t = tr(lang)
    s = SVG(960, 480, t("The short squeeze loop", "วงจร Short squeeze"),
            t("Rising price forces shorts to buy, and their buying pushes the price higher still.", "ราคาที่ขึ้นบังคับให้คนชอร์ตซื้อ และแรงซื้อของพวกเขาดันราคาให้สูงขึ้นอีก"))
    nodes = [(480, 140, t("Price rises\n(news, buyers)", "ราคาขึ้น\n(ข่าว ผู้ซื้อ)"), C["bull"]),
             (720, 260, t("Shorts' losses grow;\nstops and margin calls", "ขาดทุนของคนชอร์ตโตขึ้น\nStop และ Margin call"), C["amber"]),
             (480, 380, t("Shorts must BUY\nto close", "คนชอร์ตต้อง 'ซื้อ'\nเพื่อปิดสถานะ"), C["bear"]),
             (240, 260, t("Few shares to buy\n(high short interest)", "หุ้นให้ซื้อมีน้อย\n(Short interest สูง)"), C["purple"])]
    for x, y, txt, col in nodes:
        s.rect(x - 120, y - 40, 240, 80, fill=C["panel"], stroke=col, sw=2, rx=14)
        s.text(x, y - 6, txt, 14, col, "middle", 700)
    for (a, b) in ((0, 1), (1, 2), (2, 3), (3, 0)):
        x1, y1 = nodes[a][0], nodes[a][1]
        x2, y2 = nodes[b][0], nodes[b][1]
        s.arrow(x1 + (x2 - x1) * 0.35, y1 + (y2 - y1) * 0.35, x1 + (x2 - x1) * 0.62, y1 + (y2 - y1) * 0.62, C["dim"], 2.2)
    s.card(30, 90, 190, 120, t("GameStop, Jan 2021", "GameStop ม.ค. 2021"),
           t("about $17 → $483\nintraday on 28 Jan\n(pre-2022-split prices)\n~140% of float short", "ราว $17 → $483\nระหว่างวัน 28 ม.ค.\n(ราคาก่อนแตกพาร์ปี 2022)\nชอร์ต ~140% ของ Float"), C["bear"], 14, 12)
    return s.render()
