"""Phase 1 figures: Foundations."""
import random
from charts import SVG, CandleChart, C, tr, candles_from_path

FIGURES = {}


def fig(fn):
    FIGURES["p1-" + fn.__name__.replace("_", "-")] = fn
    return fn


# ---------------------------------------------------------------- 1.1
@fig
def series(lang):
    t = tr(lang)
    s = SVG(960, 440, t("One trade is random. 100 trades reveal your edge.",
                        "เทรดไม้เดียวคือความสุ่ม 100 ไม้ถึงจะเห็นความได้เปรียบ"),
            t("Example system: 45% win rate, win = +2R, loss = -1R",
              "ตัวอย่างระบบ: ชนะ 45%, ชนะได้ +2R, แพ้เสีย -1R"))
    rnd = random.Random(7)
    res = [2 if rnd.random() < 0.45 else -1 for _ in range(100)]
    # left: next 10 trades
    s.card(28, 100, 290, 310, t("The next 10 trades", "10 ไม้ถัดไป"), None, C["purple"])
    for k in range(10):
        r = res[k]
        x, y = 50 + (k % 5) * 52, 160 + (k // 5) * 62
        col = C["bull"] if r > 0 else C["bear"]
        s.rect(x, y, 42, 46, fill=col, rx=8, opacity=0.9)
        s.text(x + 21, y + 29, "W" if r > 0 else "L", 18, C["white"], "middle", 700)
    s.text(48, 318, t("Wins and losses arrive in a\nrandom order. You cannot know\nthe next one — and you don't need to.",
                      "ชนะและแพ้มาแบบสุ่ม\nคุณไม่มีทางรู้ไม้ถัดไป\nและไม่จำเป็นต้องรู้"), 14, C["muted"])
    # right: equity curve
    x0, y0, w, h = 360, 110, 570, 290
    s.rect(x0, y0 - 10, w, h + 30, fill=C["panel"], stroke=C["border"], rx=12)
    eq, cur = [0], 0
    for r in res:
        cur += r; eq.append(cur)
    lo, hi = min(eq) - 3, max(eq) + 3
    X = lambda i: x0 + 30 + (w - 60) * i / 100
    Y = lambda v: y0 + 20 + (h - 50) * (hi - v) / (hi - lo)
    s.line(X(0), Y(0), X(100), Y(0), C["dim"], 1, "4 4")
    s.text(X(0), Y(0) + 18, "0R", 12, C["muted"])
    # find worst losing streak
    best, run, end = 0, 0, 0
    for i, r in enumerate(res):
        run = run + 1 if r < 0 else 0
        if run > best:
            best, end = run, i
    st = end - best + 1
    s.rect(X(st), y0 + 5, X(end + 1) - X(st), h - 25, fill=C["bear"], opacity=0.12, rx=4)
    s.text(X(st) + (X(end + 1) - X(st)) / 2, y0 + 24, t(f"{best} losses in a row", f"แพ้ติดกัน {best} ไม้"), 12,
           C["bear"], "middle", 700)
    s.polyline([(X(i), Y(v)) for i, v in enumerate(eq)], C["bull"], 2.5)
    s.circle(X(100), Y(eq[-1]), 5, C["bull"])
    s.text(X(100) - 8, Y(eq[-1]) - 14, f"+{eq[-1]}R", 16, C["bull"], "end", 700)
    s.text(x0 + 24, y0 + h + 8, t("Trade #1 → #100", "ไม้ที่ 1 → 100"), 13, C["muted"])
    s.text(x0 + w - 24, y0 + h + 8, t("Expectancy = 0.45×2 − 0.55×1 = +0.35R per trade",
                                      "ค่าคาดหวัง = 0.45×2 − 0.55×1 = +0.35R ต่อไม้"), 13, C["amber"], "end", 600)
    return s.render()


@fig
def process_outcome(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Judge the process, not the outcome", "ตัดสินที่กระบวนการ ไม่ใช่ผลลัพธ์"),
            t("A win can be a mistake. A loss can be perfect trading.", "ชนะอาจเป็นความผิดพลาด แพ้อาจเป็นการเทรดที่สมบูรณ์แบบ"))
    gx, gy, cw, ch = 210, 130, 360, 150
    s.text(gx + cw / 2, gy - 14, t("GOOD OUTCOME (win)", "ผลลัพธ์ดี (ชนะ)"), 14, C["bull"], "middle", 700)
    s.text(gx + cw * 1.5 + 12, gy - 14, t("BAD OUTCOME (loss)", "ผลลัพธ์แย่ (แพ้)"), 14, C["bear"], "middle", 700)
    s.text(gx - 16, gy + ch / 2, t("GOOD\nPROCESS", "กระบวนการ\nดี"), 15, C["blue"], "end", 700)
    s.text(gx - 16, gy + ch * 1.5 + 12, t("BAD\nPROCESS", "กระบวนการ\nแย่"), 15, C["amber"], "end", 700)
    cells = [
        (0, 0, C["bull"], t("Deserved win", "ชนะอย่างสมควร"),
         t("Followed the plan, it worked.\n→ Repeat it.", "ทำตามแผน และได้ผล\n→ ทำซ้ำ")),
        (1, 0, C["blue"], t("Bad luck — still good", "โชคไม่ดี — แต่ยังดีอยู่"),
         t("Followed the plan, lost anyway.\n→ Accept it. Losses are a cost\n   of doing business.",
           "ทำตามแผน แต่ก็แพ้\n→ ยอมรับ การแพ้คือต้นทุน\n   ของธุรกิจนี้")),
        (0, 1, C["amber"], t("Dumb luck — DANGEROUS", "ฟลุ๊ค — อันตรายที่สุด"),
         t("Broke rules and still won.\n→ Teaches bad habits.\n   Log it as a mistake.",
           "ผิดกฎแต่ดันชนะ\n→ สร้างนิสัยเสีย\n   ให้บันทึกว่าเป็นความผิดพลาด")),
        (1, 1, C["bear"], t("Deserved loss", "แพ้อย่างสมควร"),
         t("Broke rules and lost.\n→ Fix the process.", "ผิดกฎและแพ้\n→ แก้ที่กระบวนการ")),
    ]
    for cx, cy, col, title, body in cells:
        x, y = gx + cx * (cw + 12), gy + cy * (ch + 12)
        s.rect(x, y, cw, ch, fill=col, opacity=0.1, stroke=col, sw=1.5, rx=12)
        s.text(x + 20, y + 36, title, 19, col, weight=700)
        s.text(x + 20, y + 70, body, 15, C["text"])
    return s.render()


# ---------------------------------------------------------------- 1.2
@fig
def order_book(lang):
    t = tr(lang)
    s = SVG(960, 520, t("The order book: where every price comes from", "สมุดคำสั่ง: ที่มาของราคาทุกราคา"),
            t("Price only moves when aggressive orders use up the resting orders on one side.",
              "ราคาจะขยับก็ต่อเมื่อคำสั่งแบบรุก (Market) กินคำสั่งที่รออยู่ (Limit) ฝั่งใดฝั่งหนึ่งจนหมด"))
    x0, y0, rh = 250, 110, 34
    s.text(x0 + 60, y0, t("BID size\n(buyers waiting)", "ฝั่ง BID\n(ผู้ซื้อที่รออยู่)"), 13, C["bull"], "middle", 700)
    s.text(x0 + 180, y0 + 8, t("Price", "ราคา"), 13, C["muted"], "middle", 700)
    s.text(x0 + 300, y0, t("ASK size\n(sellers waiting)", "ฝั่ง ASK\n(ผู้ขายที่รออยู่)"), 13, C["bear"], "middle", 700)
    asks = [(100.05, 900), (100.04, 650), (100.03, 1200), (100.02, 300), (100.01, 250)]
    bids = [(100.00, 400), (99.99, 700), (99.98, 1100), (99.97, 500), (99.96, 800)]
    y = y0 + 34
    for p, q in asks:
        eaten = p <= 100.02
        s.rect(x0 + 125, y, 110, rh - 4, fill=C["panel"], stroke=C["border"], rx=4)
        s.text(x0 + 180, y + 21, f"{p:.2f}", 14, C["text"], "middle", 600)
        s.rect(x0 + 245, y, q / 1200 * 110, rh - 4, fill=C["bear"], opacity=0.25 if eaten else 0.7, rx=4)
        s.text(x0 + 250, y + 21, str(q), 13, C["white"], weight=600)
        if eaten:
            s.line(x0 + 245, y + 15, x0 + 245 + q / 1200 * 110, y + 15, C["white"], 1.5)
        y += rh
    s.rect(x0 + 125, y - 2, 110, 26, fill=C["amber"], opacity=0.15, rx=4)
    s.text(x0 + 180, y + 16, t("spread 0.01", "สเปรด 0.01"), 12, C["amber"], "middle", 700)
    y += 28
    for p, q in bids:
        s.rect(x0 + 125, y, 110, rh - 4, fill=C["panel"], stroke=C["border"], rx=4)
        s.text(x0 + 180, y + 21, f"{p:.2f}", 14, C["text"], "middle", 600)
        s.rect(x0 + 115 - q / 1200 * 110, y, q / 1200 * 110, rh - 4, fill=C["bull"], opacity=0.7, rx=4)
        s.text(x0 + 110, y + 21, str(q), 13, C["white"], "end", 600)
        y += rh
    # market buy callout
    s.card(650, 130, 285, 190, t("Market BUY 550", "ส่ง Market BUY 550"),
           t("1) fills 250 @ 100.01\n2) fills 300 @ 100.02\n→ ask level gone, next best\n   ask is 100.03\n→ last price ticks UP",
             "1) ได้ 250 ที่ 100.01\n2) ได้ 300 ที่ 100.02\n→ ฝั่ง ASK ระดับนั้นหมด\n   ราคาขายถัดไปคือ 100.03\n→ ราคาล่าสุดขยับ ขึ้น"),
           C["bull"], 17, 14)
    s.arrow(645, 230, x0 + 290, y0 + 34 + rh * 3 + 15, C["bull"], 2)
    s.card(28, 130, 200, 150, t("Key idea", "แนวคิดสำคัญ"),
           t("Limit orders = wall.\nMarket orders = hammer.\nPrice moves when the\nhammer breaks the wall.",
             "Limit = กำแพง\nMarket = ค้อน\nราคาขยับเมื่อค้อน\nทุบกำแพงจนทะลุ"), C["purple"], 16, 14)
    return s.render()


@fig
def auction(lang):
    t = tr(lang)
    s = SVG(960, 400, t("Every candle is a tug-of-war", "ทุกแท่งเทียนคือการชักเย่อ"),
            t("Aggression decides direction — not the number of people.", "ความก้าวร้าวของคำสั่งเป็นตัวกำหนดทิศทาง ไม่ใช่จำนวนคน"))
    states = [
        (C["bull"], t("Buyers more aggressive", "ผู้ซื้อรุกมากกว่า"), t("Price rises to find sellers", "ราคาขึ้นไปหาผู้ขาย"),
         [0, 1, 0.6, 2, 1.7, 3, 2.6, 4]),
        (C["amber"], t("Balanced", "สมดุล"), t("Price rotates in a range", "ราคาแกว่งในกรอบ"),
         [2, 3, 1.4, 2.8, 1.3, 2.9, 1.6, 2.2]),
        (C["bear"], t("Sellers more aggressive", "ผู้ขายรุกมากกว่า"), t("Price falls to find buyers", "ราคาลงไปหาผู้ซื้อ"),
         [4, 3, 3.4, 2, 2.4, 1, 1.5, 0]),
    ]
    for k, (col, head, sub, path) in enumerate(states):
        x = 28 + k * 308
        s.rect(x, 100, 290, 270, fill=C["panel"], stroke=C["border"], rx=12)
        s.text(x + 145, 134, head, 17, col, "middle", 700)
        # tug bar
        share = [0.7, 0.5, 0.3][k]
        s.rect(x + 25, 152, 240 * share, 14, fill=C["bull"], rx=7)
        s.rect(x + 25 + 240 * share, 152, 240 * (1 - share), 14, fill=C["bear"], rx=7)
        s.text(x + 25, 186, t("buy", "ซื้อ"), 12, C["bull"])
        s.text(x + 265, 186, t("sell", "ขาย"), 12, C["bear"], "end")
        pts = [(x + 35 + i * 31, 330 - v * 30) for i, v in enumerate(path)]
        s.polyline(pts, col, 3)
        s.text(x + 145, 360, sub, 14, C["muted"], "middle")
    return s.render()


@fig
def order_types(lang):
    t = tr(lang)
    s = SVG(960, 380, t("Three order types you must know", "คำสั่ง 3 แบบที่ต้องรู้"))
    specs = [
        (C["blue"], t("Market order", "Market Order"), t("Buy/sell NOW at the best\navailable price. Certain fill,\nuncertain price.",
                                                         "ซื้อ/ขาย ทันที ที่ราคาดีที่สุด\nได้ของแน่นอน\nแต่ราคาไม่แน่นอน"), "market"),
        (C["bull"], t("Limit order", "Limit Order"), t("Wait at YOUR price (buy below /\nsell above market). Certain\nprice, uncertain fill.",
                                                       "รอที่ราคาของคุณ (ซื้อต่ำกว่า /\nขายสูงกว่าราคาตลาด)\nราคาแน่นอน แต่อาจไม่ได้ของ"), "limit"),
        (C["bear"], t("Stop order", "Stop Order"), t("Becomes a market order when\nprice touches it. Used for stop\nlosses and breakout entries.",
                                                     "กลายเป็น Market Order เมื่อราคา\nแตะถึง ใช้ตั้ง Stop Loss\nและเข้าเทรดตอนเบรกเอาท์"), "stop"),
    ]
    for k, (col, head, body, kind) in enumerate(specs):
        x = 28 + k * 308
        s.card(x, 60, 290, 300, head, body, col, 19, 14)
        # mini price line
        px, py = x + 30, 290
        path = [0, 0.8, 0.3, 1.2, 0.5, -0.4, 0.2, 1.5, 2.2]
        pts = [(px + i * 28, py - v * 30) for i, v in enumerate(path)]
        s.polyline(pts, C["text"], 2)
        if kind == "market":
            s.circle(pts[0][0], pts[0][1], 7, col)
            s.text(pts[0][0] + 12, pts[0][1] + 22, t("filled now", "ได้ทันที"), 12, col, weight=700)
        elif kind == "limit":
            ly = py + 0.4 * 30 - 0.0
            s.line(px, ly, px + 230, ly, col, 1.5, "5 4")
            s.text(px, ly + 20, t("buy limit (waits below)", "buy limit (รอด้านล่าง)"), 12, col, weight=700)
            s.circle(pts[5][0], pts[5][1], 7, col)
        else:
            sy = py - 1.35 * 30
            s.line(px, sy, px + 230, sy, col, 1.5, "5 4")
            s.text(px, sy - 8, t("buy stop (above price)", "buy stop (เหนือราคา)"), 12, col, weight=700)
            s.circle(px + 7 * 28 - 8, sy, 7, col)
    return s.render()


# ---------------------------------------------------------------- 1.3
def _big_candle(s, x, yo, yc, yh, yl, bw, col):
    s.line(x, yh, x, yl, col, 3)
    s.rect(x - bw / 2, min(yo, yc), bw, abs(yc - yo), fill=col, rx=4)


@fig
def candle_anatomy(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Anatomy of a candlestick", "กายวิภาคของแท่งเทียน"),
            t("Four prices, one period: Open · High · Low · Close (OHLC)", "4 ราคาในหนึ่งช่วงเวลา: เปิด · สูงสุด · ต่ำสุด · ปิด (OHLC)"))
    for k, bull in enumerate((True, False)):
        cx = 250 + k * 440
        col = C["bull"] if bull else C["bear"]
        yh, yl = 120, 430
        yo, yc = (330, 190) if bull else (190, 330)
        s.text(cx, 108 - 0, "", 1)
        _big_candle(s, cx, yo, yc, yh, yl, 90, col)
        s.pill(cx, 452, t("BULLISH  close > open", "แท่งเขียว  ปิด > เปิด") if bull else t("BEARISH  close < open", "แท่งแดง  ปิด < เปิด"), col, 13)
        # labels left: prices
        def lab(y, txt, side, c=C["text"]):
            if side == "L":
                s.line(cx - 55, y, cx - 110, y, C["dim"], 1.2, "3 3")
                s.text(cx - 118, y + 5, txt, 14, c, "end", 700)
            else:
                s.line(cx + 55, y, cx + 110, y, C["dim"], 1.2, "3 3")
                s.text(cx + 118, y + 5, txt, 14, c, "start", 700)
        lab(yh, t("High", "สูงสุด (High)"), "L")
        lab(yl, t("Low", "ต่ำสุด (Low)"), "L")
        lab(yc, t("Close", "ปิด (Close)"), "L", col)
        lab(yo, t("Open", "เปิด (Open)"), "L", col)
        lab((yh + min(yo, yc)) / 2, t("Upper wick\n= price rejected\n   up here", "ไส้บน\n= ราคาถูกปฏิเสธ\n   ที่ด้านบน"), "R", C["muted"])
        lab((yo + yc) / 2, t("Body\n= who won\n   the period", "ตัวแท่ง\n= ใครชนะ\n   ในช่วงนั้น"), "R", col)
        lab((yl + max(yo, yc)) / 2, t("Lower wick\n= price rejected\n   down here", "ไส้ล่าง\n= ราคาถูกปฏิเสธ\n   ที่ด้านล่าง"), "R", C["muted"])
    return s.render()


@fig
def candle_story(lang):
    t = tr(lang)
    s = SVG(960, 490, t("The story inside one candle", "เรื่องราวที่ซ่อนอยู่ในแท่งเทียนแท่งเดียว"),
            t("A 1-hour candle compresses 60 minutes of fighting into 4 numbers.",
              "แท่งเทียน 1 ชั่วโมง บีบอัดการต่อสู้ 60 นาทีให้เหลือเพียง 4 ตัวเลข"))
    path = [100, 99.2, 98, 97, 98.4, 100.2, 101.6, 104, 103.4, 103]
    lo, hi = 96, 105
    Y = lambda p: 110 + 300 * (hi - p) / (hi - lo)
    X = lambda i: 70 + i * 50
    s.rect(40, 95, 530, 340, fill=C["panel"], stroke=C["border"], rx=12)
    s.polyline([(X(i), Y(p)) for i, p in enumerate(path)], C["text"], 2.5)
    marks = [(0, 100, "O", t("Opens at 100", "เปิดที่ 100"), C["blue"], -14),
             (3, 97, "L", t("Sellers push to 97", "ผู้ขายกดลงถึง 97"), C["bear"], 28),
             (7, 104, "H", t("Buyers drive to 104", "ผู้ซื้อดันขึ้นถึง 104"), C["bull"], -14),
             (9, 103, "C", t("Closes at 103", "ปิดที่ 103"), C["amber"], 28)]
    for i, p, k, txt, col, dy in marks:
        s.circle(X(i), Y(p), 7, col)
        s.text(X(i), Y(p) + dy, f"{k} · {txt}", 13, col, "middle" if 0 < i < 9 else ("start" if i == 0 else "end"), 700)
    s.text(70, 425, "09:00", 12, C["muted"])
    s.text(520, 425, "10:00", 12, C["muted"], "end")
    # arrow and candle
    s.arrow(590, 260, 660, 260, C["muted"], 2.5)
    cx = 760
    for p, col in ((104, C["bull"]), (97, C["bear"]), (100, C["blue"]), (103, C["amber"])):
        s.line(X(9) + 10, Y(p), cx - 40, Y(p), col, 1, "3 4", opacity=0.6)
    _big_candle(s, cx, Y(100), Y(103), Y(104), Y(97), 64, C["bull"])
    s.text(cx + 50, Y(104) + 5, "H 104", 14, C["bull"], weight=700)
    s.text(cx + 50, Y(103) + 5, "C 103", 14, C["amber"], weight=700)
    s.text(cx + 50, Y(100) + 5, "O 100", 14, C["blue"], weight=700)
    s.text(cx + 50, Y(97) + 5, "L 97", 14, C["bear"], weight=700)
    s.text(cx, 448, t("Long lower wick: sellers tried\nand FAILED. Buyers won.", "ไส้ล่างยาว: ผู้ขายพยายามแล้ว\nแต่ล้มเหลว ผู้ซื้อชนะ"),
           13, C["muted"], "middle")
    return s.render()


@fig
def candle_strength(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Read the fight: body vs wick", "อ่านการต่อสู้: ตัวแท่ง vs ไส้เทียน"),
            t("Big body = conviction. Long wick = rejection. Tiny body = indecision.",
              "ตัวแท่งใหญ่ = มั่นใจ  ไส้ยาว = ถูกปฏิเสธ  ตัวแท่งเล็ก = ลังเล"))
    items = [
        ((0, 10.1, -0.1, 10), t("Marubozu", "มารูโบซุ"), t("Total control\nby buyers", "ผู้ซื้อคุมเกม\nเต็มที่"), C["bull"]),
        ((1, 9.2, 0, 8), t("Strong body", "ตัวแท่งใหญ่"), t("Buyers in\ncontrol", "ผู้ซื้อ\nได้เปรียบ"), C["bull"]),
        ((4.2, 9, 1, 5.4), t("Spinning top", "สปินนิ่งท็อป"), t("Both sides\nfought, no winner", "สู้กันทั้งสองฝ่าย\nไม่มีผู้ชนะ"), C["amber"]),
        ((5, 9, 1, 5.05), t("Doji", "โดจิ"), t("Perfect\nindecision", "ลังเล\nสมบูรณ์แบบ"), C["amber"]),
        ((8, 8.9, 0.3, 8.6), t("Hammer / Pin bar", "แฮมเมอร์ / พินบาร์"), t("Sellers REJECTED\n(bullish at lows)", "ผู้ขายถูกปฏิเสธ\n(บวกเมื่ออยู่ที่จุดต่ำ)"), C["teal"]),
        ((2, 9.8, 1.2, 1.1), t("Shooting star", "ชูตติ้งสตาร์"), t("Buyers REJECTED\n(bearish at highs)", "ผู้ซื้อถูกปฏิเสธ\n(ลบเมื่ออยู่ที่จุดสูง)"), C["pink"]),
        ((10, 10.1, -0.1, 0), t("Bear marubozu", "มารูโบซุแดง"), t("Total control\nby sellers", "ผู้ขายคุมเกม\nเต็มที่"), C["bear"]),
    ]
    Y = lambda p: 330 - p * 20
    for k, ((o, h, l, c), name, meaning, col) in enumerate(items):
        x = 90 + k * 130
        cc = C["bull"] if c >= o else C["bear"]
        s.line(x, Y(h), x, Y(l), cc, 2.5)
        s.rect(x - 20, Y(max(o, c)), 40, max(abs(Y(o) - Y(c)), 3), fill=cc, rx=3)
        s.text(x, 368, name, 14, col, "middle", 700)
        s.text(x, 390, meaning, 12, C["muted"], "middle")
    return s.render()


# ---------------------------------------------------------------- 1.4
PATTERNS = [
    ("bull_engulf", [(10, 10.3, 8.7, 9), (9, 9.3, 7.9, 8.1), (8.2, 8.4, 7.4, 7.6), (7.4, 9.9, 7.2, 9.7)],
     ("Bullish engulfing", "Bullish Engulfing (กลืนกินขาขึ้น)"),
     ("Buyers overwhelm the last\nsellers in one candle.", "ผู้ซื้อกลืนแรงขายล่าสุด\nได้หมดในแท่งเดียว"), C["bull"], 3),
    ("bear_engulf", [(7, 8.3, 6.7, 8), (8, 9.1, 7.8, 8.9), (8.8, 9.6, 8.6, 9.4), (9.6, 9.8, 7.1, 7.3)],
     ("Bearish engulfing", "Bearish Engulfing (กลืนกินขาลง)"),
     ("Sellers overwhelm the last\nbuyers in one candle.", "ผู้ขายกลืนแรงซื้อล่าสุด\nได้หมดในแท่งเดียว"), C["bear"], 3),
    ("hammer", [(10, 10.2, 8.8, 9), (9, 9.2, 7.8, 8), (8, 8.3, 5.6, 8.1), (8.1, 9.3, 7.9, 9.1)],
     ("Hammer (bullish pin bar)", "Hammer (พินบาร์ขาขึ้น)"),
     ("Price dropped, got rejected,\nclosed near the high.", "ราคาลงไปแล้วถูกปฏิเสธ\nปิดใกล้จุดสูงสุด"), C["teal"], 2),
    ("star", [(6, 7.2, 5.8, 7), (7, 8.2, 6.8, 8), (8, 10.6, 7.9, 7.9), (7.9, 8.1, 6.8, 7)],
     ("Shooting star (bearish pin)", "Shooting Star (พินบาร์ขาลง)"),
     ("Price spiked up, got rejected,\nclosed near the low.", "ราคาพุ่งขึ้นแล้วถูกปฏิเสธ\nปิดใกล้จุดต่ำสุด"), C["pink"], 2),
    ("doji", [(6, 7.3, 5.8, 7.1), (7.1, 8.4, 6.9, 8.2), (8.2, 9.3, 7.3, 8.25), (8.2, 8.4, 7.2, 7.4)],
     ("Doji", "Doji (โดจิ)"),
     ("Open = close. Momentum paused;\nwait for the next candle.", "เปิด = ปิด โมเมนตัมหยุดพัก\nรอดูแท่งถัดไป"), C["amber"], 2),
    ("inside", [(6, 6.4, 5.5, 6.2), (6.2, 9.4, 6, 9.1), (8.6, 8.9, 7.6, 7.9), (7.9, 9.9, 7.7, 9.7)],
     ("Inside bar", "Inside Bar (อินไซด์บาร์)"),
     ("Range inside the prior candle:\ncompression before a move.", "กรอบราคาอยู่ในแท่งก่อนหน้า:\nบีบตัวก่อนเลือกทาง"), C["blue"], 2),
]


@fig
def patterns(lang):
    t = tr(lang)
    s = SVG(960, 660, t("Six candlestick patterns worth knowing", "รูปแบบแท่งเทียน 6 แบบที่ควรรู้"),
            t("The highlighted candle is the signal. It only matters at a meaningful level (next figure).",
              "แท่งที่ถูกไฮไลต์คือสัญญาณ ซึ่งจะมีความหมายก็ต่อเมื่ออยู่ในตำแหน่งสำคัญเท่านั้น (ดูภาพถัดไป)"))
    for k, (_, cs, name, mean, col, hi) in enumerate(PATTERNS):
        x = 28 + (k % 3) * 308
        y = 100 + (k // 3) * 280
        s.rect(x, y, 290, 262, fill=C["panel"], stroke=C["border"], rx=12)
        s.text(x + 18, y + 30, t(*name) if lang == "en" else name[1], 15, col, weight=700)
        ch = CandleChart(s, x + 50, y + 44, 190, 140, cs, grid=False)
        ch.draw(highlight={hi: col})
        s.text(x + 18, y + 214, mean[0] if lang == "en" else mean[1], 13, C["text"])
    return s.render()


@fig
def location(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Location beats pattern", "ตำแหน่งสำคัญกว่ารูปแบบ"),
            t("The same hammer means different things in different places.", "แฮมเมอร์แบบเดียวกัน ความหมายต่างกันเมื่ออยู่คนละที่"))
    # left: hammer at support
    cs = candles_from_path([112, 100.5, 110, 100.8, 113], [5, 5, 5, 6], seed=3)
    i = 14
    cs[i] = [cs[i - 1][3], 102.6, 100.4, 102.3]
    cs[i + 1][0] = 102.3
    s.rect(28, 90, 440, 360, fill=C["panel"], stroke=C["border"], rx=12)
    ch = CandleChart(s, 40, 130, 416, 270, cs)
    ch.zone(100.2, 101.8, C["blue"], t("Support (tested before)", "แนวรับ (เคยทดสอบมาแล้ว)"), label_pos="below")
    ch.draw(highlight={i: C["teal"]})
    ch.label(i, 100.2, t("↑ Hammer at support", "↑ แฮมเมอร์ที่แนวรับ"), C["teal"], dy=18, anchor="start", dx=-6)
    s.text(48, 120, t("✓ Works: sellers rejected at a level buyers defend",
                      "✓ ได้ผล: ผู้ขายถูกปฏิเสธที่ระดับที่ผู้ซื้อปกป้อง"), 14, C["bull"], weight=700)
    # right: hammer mid-trend
    cs2 = candles_from_path([120, 110, 114, 103, 106, 95], [5, 3, 6, 3, 5], seed=5)
    j = 11
    o = cs2[j - 1][3]
    cs2[j] = [o, o + 0.6, o - 3.2, o + 0.4]
    cs2[j + 1][0] = o + 0.4
    s.rect(492, 90, 440, 360, fill=C["panel"], stroke=C["border"], rx=12)
    ch2 = CandleChart(s, 504, 130, 416, 270, cs2)
    ch2.draw(highlight={j: C["bear"]})
    ch2.label(j, cs2[j][2], t("Hammer in mid-air", "แฮมเมอร์กลางอากาศ"), C["bear"], dy=5, anchor="end", dx=-16)
    s.text(512, 120, t("✗ Fails: no level, strong downtrend", "✗ ล้มเหลว: ไม่มีแนวรองรับ เทรนด์ขาลงแรง"), 14, C["bear"], weight=700)
    return s.render()


@fig
def engulfing_trade(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Example: a bullish engulfing trade, planned before entry",
                        "ตัวอย่าง: เทรด Bullish Engulfing ที่วางแผนไว้ก่อนเข้า"),
            t("Level first → signal second → risk defined → target at the next obstacle",
              "ระดับราคามาก่อน → สัญญาณตามมา → กำหนดความเสี่ยง → เป้าหมายที่อุปสรรคถัดไป"))
    cs = candles_from_path([125, 110, 118, 105], [6, 4, 7], seed=11)
    last = cs[-1]
    o = last[3] - 0.2
    c = last[0] + 1.4
    eng = [o, c + 0.3, min(last[2], o) - 0.4, c]
    cs.append(eng)
    cs += candles_from_path([c, 112.5, 110.5, 118], [4, 2, 4], seed=12)
    k = 17
    entry, stop = eng[3], eng[2] - 0.5
    target = 118
    r = (target - entry) / (entry - stop)
    s.rect(28, 90, 904, 390, fill=C["panel"], stroke=C["border"], rx=12)
    ch = CandleChart(s, 40, 110, 880, 350, cs, right_space=170)
    ch.zone(103.4, 106, C["blue"], t("Daily support zone", "โซนแนวรับรายวัน"), i0=0, label_pos="below")
    ch.hline(118, t("Prior swing high = target", "จุดสูงเดิม = เป้าหมาย"), C["dim"], i0=8, i1=len(cs) - 1, side="left")
    x0, x1 = ch.X(k) - ch.step / 2, ch.X(len(cs) - 1) + ch.step / 2
    s.rect(x0, ch.Y(target), x1 - x0, ch.Y(entry) - ch.Y(target), fill=C["bull"], opacity=0.14, rx=2)
    s.rect(x0, ch.Y(entry), x1 - x0, ch.Y(stop) - ch.Y(entry), fill=C["bear"], opacity=0.2, rx=2)
    ch.draw(highlight={k: C["bull"]})
    lx = x1 + 12
    s.text(lx, ch.Y(target) + 5, t(f"Target +{r:.1f}R", f"เป้าหมาย +{r:.1f}R"), 14, C["bull"], weight=700)
    s.text(lx, ch.Y(entry) + 5, t("Entry (close)", "จุดเข้า (ราคาปิด)"), 14, C["text"], weight=700)
    s.text(lx, ch.Y(stop) + 5, t("Stop −1R", "Stop −1R"), 14, C["bear"], weight=700)
    s.text(lx, ch.Y(stop) + 26, t("(below signal low)", "(ใต้จุดต่ำของสัญญาณ)"), 12, C["muted"])
    ch.label(k, eng[2], t("Engulfing", "Engulfing"), C["bull"], dy=34)
    return s.render()


# ---------------------------------------------------------------- 1.5
@fig
def timeframes(lang):
    t = tr(lang)
    s = SVG(960, 560, t("Timeframes are zoom levels of the same price", "ไทม์เฟรมคือการซูมเข้า-ออกของราคาชุดเดียวกัน"),
            t("One 1-hour candle = four 15-minute candles.", "แท่ง 1 ชั่วโมง 1 แท่ง = แท่ง 15 นาที 4 แท่ง"))
    big = [100, 104, 97, 103]
    small = [(100, 100.8, 97, 97.8), (97.8, 100.5, 97.5, 100.2), (100.2, 104, 100, 103.5), (103.5, 103.8, 102.6, 103)]
    Y = lambda p: 110 + 250 * (105 - p) / 9
    s.rect(28, 90, 904, 300, fill=C["panel"], stroke=C["border"], rx=12)
    for p, col in ((104, C["bull"]), (97, C["bear"])):
        s.line(150, Y(p), 800, Y(p), col, 1, "4 4", opacity=0.6)
    _big_candle(s, 220, Y(big[0]), Y(big[3]), Y(big[1]), Y(big[2]), 70, C["bull"])
    s.text(220, 380, t("1 × 1H", "1 × 1 ชั่วโมง"), 15, C["text"], "middle", 700)
    s.text(400, Y(100.5), "=", 50, C["muted"], "middle", 700)
    for k, (o, h, l, c) in enumerate(small):
        x = 520 + k * 80
        col = C["bull"] if c >= o else C["bear"]
        _big_candle(s, x, Y(o), Y(c), Y(h), Y(l), 44, col)
        s.text(x, 352, f"{k * 15:02d}'", 12, C["muted"], "middle")
    s.text(640, 380 + 0, t("4 × 15m", "4 × 15 นาที"), 15, C["text"], "middle", 700)
    s.text(830, Y(104) + 5, "H", 14, C["bull"], weight=700)
    s.text(830, Y(97) + 5, "L", 14, C["bear"], weight=700)
    # ladder
    tfs = ["1M", "1W", "1D", "4H", "1H", "15m", "5m", "1m"]
    styles = [(0, 2, C["purple"], t("Investor", "นักลงทุน")), (2, 4, C["blue"], t("Swing trader", "สวิงเทรดเดอร์")),
              (4, 6, C["teal"], t("Day trader", "เดย์เทรดเดอร์")), (6, 8, C["amber"], t("Scalper", "สแกลเปอร์"))]
    x0, w = 60, 105
    for i, tf in enumerate(tfs):
        s.rect(x0 + i * w, 420, w - 8, 40, fill=C["panel"], stroke=C["border"], rx=8)
        s.text(x0 + i * w + (w - 8) / 2, 446, tf, 15, C["text"], "middle", 700)
    for a, b, col, name in styles:
        s.rect(x0 + a * w, 470, (b - a) * w - 8, 8, fill=col, rx=4)
        s.text(x0 + a * w + ((b - a) * w - 8) / 2, 500, name, 13, col, "middle", 700)
    s.text(x0, 540, t("← bigger picture, slower, more reliable", "← ภาพใหญ่ ช้า น่าเชื่อถือกว่า"), 13, C["muted"])
    s.text(x0 + 8 * w - 8, 540, t("smaller detail, faster, more noise →", "รายละเอียด เร็ว สัญญาณรบกวนมาก →"), 13, C["muted"], "end")
    return s.render()


@fig
def top_down(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Top-down analysis: direction → location → trigger", "วิเคราะห์จากบนลงล่าง: ทิศทาง → ตำแหน่ง → จังหวะเข้า"),
            t("Never take a small-timeframe signal against the big-timeframe story.", "อย่าเทรดสัญญาณไทม์เฟรมเล็กที่สวนเรื่องราวของไทม์เฟรมใหญ่"))
    panels = [
        ("1 · Daily", t("Direction: uptrend,\npulling back → look for LONGS", "ทิศทาง: ขาขึ้น กำลังย่อ\n→ มองหาจังหวะ ซื้อ"), C["purple"],
         candles_from_path([100, 120, 111, 131, 122], [7, 4, 7, 4], seed=21), None),
        ("2 · 1H", t("Location: pullback reaches\nthe demand zone", "ตำแหน่ง: ราคาย่อลงมาถึง\nโซนอุปสงค์"), C["blue"],
         candles_from_path([131, 125, 128, 121.3, 122.8], [5, 3, 6, 3], seed=22), (121, 122.6)),
        ("3 · 5m", t("Trigger: bullish engulfing\nat the zone → enter", "จังหวะ: เกิด Bullish Engulfing\nในโซน → เข้าเทรด"), C["bull"],
         None, None),
    ]
    c3 = candles_from_path([123, 121.4, 122.4, 121.6], [5, 3, 3], seed=23)
    lo3 = c3[-1]
    e = [lo3[3] - 0.05, lo3[0] + 0.6, lo3[3] - 0.2, lo3[0] + 0.5]
    c3.append(e)
    c3 += candles_from_path([e[3], 123.2, 122.8, 124], [3, 1, 2], seed=24)
    for k, (head, body, col, cs, zone) in enumerate(panels):
        x = 28 + k * 308
        s.rect(x, 95, 290, 355, fill=C["panel"], stroke=C["border"], rx=12)
        s.text(x + 18, 124, head, 17, col, weight=700)
        cs = cs or c3
        ch = CandleChart(s, x + 14, 140, 262, 210, cs, grid=False)
        if zone:
            ch.zone(zone[0], zone[1], C["blue"], opacity=0.2)
        if k == 0:
            ch.zone(120, 124, C["blue"], opacity=0.15, i0=18)
        if k == 2:
            ch.zone(121.25, 121.7, C["blue"], opacity=0.18)
        ch.draw(highlight={len(c3) - 7: C["bull"]} if k == 2 else None)
        s.text(x + 18, 385, body, 14, C["text"])
        if k < 2:
            s.arrow(x + 292, 250, x + 306, 250, C["muted"], 2.5)
    return s.render()


# ---------------------------------------------------------------- 1.6
@fig
def summary(lang):
    t = tr(lang)
    s = SVG(960, 520, t("Phase 1 on one page", "สรุปเฟส 1 ในหน้าเดียว"))
    cx, cy = 480, 290
    nodes = [
        (180, 150, C["purple"], t("Mindset", "ความคิด"), t("Think in 100 trades.\nJudge process, not outcome.", "คิดเป็นชุด 100 ไม้\nตัดสินที่กระบวนการ")),
        (780, 150, C["blue"], t("Auction", "การประมูล"), t("Aggressive orders eat\nresting orders → price moves.", "คำสั่งรุกกินคำสั่งรอ\n→ ราคาขยับ")),
        (140, 330, C["bull"], t("Candles", "แท่งเทียน"), t("Body = who won.\nWick = rejection.", "ตัวแท่ง = ใครชนะ\nไส้ = การปฏิเสธ")),
        (820, 330, C["teal"], t("Patterns", "รูปแบบ"), t("Location first,\npattern second.", "ตำแหน่งมาก่อน\nรูปแบบตามมา")),
        (480, 450, C["amber"], t("Timeframes", "ไทม์เฟรม"), t("HTF direction → MTF zone\n→ LTF trigger.", "HTF ทิศทาง → MTF โซน\n→ LTF จังหวะเข้า")),
    ]
    for x, y, col, head, body in nodes:
        s.line(cx, cy, x, y, col, 2, opacity=0.5)
    s.circle(cx, cy, 70, C["panel"], C["text"], 2)
    s.text(cx, cy - 4, t("PHASE 1", "เฟส 1"), 20, C["text"], "middle", 700)
    s.text(cx, cy + 20, t("Foundations", "พื้นฐาน"), 14, C["muted"], "middle")
    for x, y, col, head, body in nodes:
        s.rect(x - 125, y - 42, 250, 92, fill=C["panel"], stroke=col, rx=12)
        s.text(x, y - 14, head, 17, col, "middle", 700)
        s.text(x, y + 10, body, 13, C["text"], "middle")
    return s.render()


@fig
def momentum(lang):
    t = tr(lang)
    s = SVG(960, 420, t("Read candles as a sequence, not one by one", "อ่านแท่งเทียนเป็นลำดับ ไม่ใช่ทีละแท่ง"),
            t("Growing bodies = momentum. Shrinking bodies + wicks = the push is running out.",
              "ตัวแท่งใหญ่ขึ้น = โมเมนตัม  ตัวแท่งเล็กลง + ไส้ยาว = แรงส่งกำลังหมด"))
    mom = [(100, 100.8, 99.7, 100.6), (100.6, 101.6, 100.4, 101.5), (101.5, 103, 101.3, 102.9),
           (102.9, 105.1, 102.8, 105), (105, 107.8, 104.9, 107.6), (107.6, 110.6, 107.4, 110.4)]
    exh = [(100, 103, 99.8, 102.8), (102.8, 105.2, 102.6, 105), (105, 107, 104.8, 106.5),
           (106.5, 108.2, 106.2, 107.2), (107.2, 108.6, 106.9, 107.5), (107.5, 108.7, 106.6, 106.9)]
    for k, (cs, head, body, col) in enumerate([
        (mom, t("Momentum", "โมเมนตัม"), t("Each body bigger than the\nlast, closes near the highs\n→ buyers accelerating.\nDon't fight it.",
                                          "ตัวแท่งใหญ่ขึ้นทุกแท่ง ปิดใกล้จุดสูง\n→ ผู้ซื้อเร่งแรง อย่าสวน"), C["bull"]),
        (exh, t("Exhaustion", "หมดแรง"), t("Bodies shrink, upper wicks\ngrow → buyers still push\nbut get rejected. Watch for\na reversal signal.",
                                            "ตัวแท่งเล็กลง ไส้บนยาวขึ้น →\nผู้ซื้อยังดันแต่ถูกปฏิเสธ\nระวังสัญญาณกลับตัว"), C["amber"])]):
        x = 28 + k * 460
        s.rect(x, 90, 444, 310, fill=C["panel"], stroke=C["border"], rx=12)
        s.text(x + 20, 120, head, 18, col, weight=700)
        ch = CandleChart(s, x + 20, 135, 200, 240, cs, pmin=99, pmax=111.5, grid=False)
        ch.draw()
        if k == 1:
            ch.path([(2, 107.6), (5, 109.3)], C["amber"], 1.5, "4 4")
        s.text(x + 240, 175, body, 14, C["text"])
    return s.render()


# ---------------------------------------------------------------- v2 additions (B9a)
def _run_odds(n, k, q):
    """Probability of at least one run of >= k losses in n trades (loss prob q)."""
    dp, hit = [1.0] + [0.0] * (k - 1), 0.0
    for _ in range(n):
        nd = [0.0] * k
        for r, pr in enumerate(dp):
            nd[0] += pr * (1 - q)
            if r + 1 >= k:
                hit += pr * q
            else:
                nd[r + 1] += pr * q
        dp = nd
    return hit


@fig
def streak_odds(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Losing streaks are normal, even in a winning system", "การแพ้ติดกันเป็นเรื่องปกติ แม้ในระบบที่ทำกำไร"),
            t("Chance of at least one losing streak of N trades in 100 trades (45% win rate, computed)",
              "โอกาสที่จะแพ้ติดกันอย่างน้อย N ไม้ ภายใน 100 ไม้ (อัตราชนะ 45% คำนวณจริง)"))
    x0, base, bw, gap, hmax = 110, 360, 70, 30, 230
    s.line(x0 - 20, base, x0 + 8 * (bw + gap), base, C["dim"], 1.5)
    for k, n in enumerate(range(5, 13)):
        p = _run_odds(100, n, 0.55)
        x = x0 + k * (bw + gap)
        col = C["bear"] if p >= 0.5 else (C["amber"] if p >= 0.1 else C["blue"])
        s.rect(x, base - p * hmax, bw, p * hmax, fill=col, opacity=0.85, rx=4)
        s.text(x + bw / 2, base - p * hmax - 10, f"{p * 100:.0f}%", 15, col, "middle", 700)
        s.text(x + bw / 2, base + 24, t(f"{n} in a row", f"ติดกัน {n}"), 13, C["muted"], "middle")
    s.text(x0 - 20, 410, t("Plan for streaks before they happen: a system that loses 8 in a row about 1 time in 3 is still profitable (+0.35R per trade).",
                           "วางแผนรับการแพ้ติดกันไว้ก่อน: ระบบที่แพ้ 8 ไม้ติดราว 1 ใน 3 ครั้ง ยังทำกำไรได้ (+0.35R ต่อไม้)"), 13, C["amber"], weight=600)
    return s.render()


@fig
def book_walk(lang):
    t = tr(lang)
    s = SVG(960, 460, t("Slippage: a big market order walks up the book", "Slippage: คำสั่ง Market ขนาดใหญ่ไต่ขึ้นไปในสมุดคำสั่ง"),
            t("Resting sell orders (asks). Best ask 100.01. Each market buy takes the cheapest offers first (illustrative).",
              "คำสั่งขายที่รออยู่ (Ask) ราคา Ask ดีที่สุด 100.01 คำสั่งซื้อ Market กินราคาถูกสุดก่อนเสมอ (ตัวอย่าง)"))
    asks = [(100.04, 500), (100.03, 400), (100.02, 300), (100.01, 250)]
    x0, y0, rh = 60, 120, 52
    for k, (p, q) in enumerate(asks):
        y = y0 + k * rh
        s.text(x0, y + 30, f"{p:.2f}", 15, C["bear"], weight=700)
        s.rect(x0 + 80, y + 10, q * 0.4, 30, fill=C["bear"], opacity=0.35, rx=4)
        s.text(x0 + 90 + q * 0.4, y + 31, f"{q}", 13, C["muted"])
    s.text(x0, y0 + 4 * rh + 30, t("price", "ราคา"), 12, C["muted"])
    s.text(x0 + 80, y0 + 4 * rh + 30, t("size for sale", "จำนวนที่ตั้งขาย"), 12, C["muted"])

    def fill(q):
        cost, left, last = 0.0, q, None
        for p, sz in reversed(asks):
            take = min(sz, left)
            cost += take * p
            left -= take
            last = p
            if left == 0:
                break
        return cost / q, last
    rows = [(100, C["bull"]), (550, C["amber"]), (1200, C["bear"])]
    for k, (q, col) in enumerate(rows):
        avg, last = fill(q)
        y = 110 + k * 108
        s.rect(400, y, 520, 92, fill=C["panel"], stroke=col, rx=12)
        s.text(420, y + 30, t(f"Market buy {q:,}", f"ซื้อ Market {q:,}"), 17, col, weight=700)
        s.text(420, y + 56, t(f"average fill {avg:.4f} · last fill {last:.2f}", f"ราคาเฉลี่ย {avg:.4f} · ราคาสุดท้าย {last:.2f}"), 14, C["text"])
        s.text(420, y + 78, t(f"extra cost vs 100.01: {(avg - 100.01) * q:.2f} USD", f"ต้นทุนเพิ่มเทียบ 100.01: {(avg - 100.01) * q:.2f} ดอลลาร์"), 13, C["muted"])
    return s.render()


@fig
def close_location(lang):
    t = tr(lang)
    s = SVG(960, 460, t("Where did it close? Measure the close inside the range", "ปิดที่ไหน? วัดตำแหน่งราคาปิดภายในกรอบของแท่ง"),
            t("Close location = (close − low) ÷ (high − low). Top 25% = strong, bottom 25% = weak.",
              "ตำแหน่งปิด = (ปิด − ต่ำสุด) ÷ (สูงสุด − ต่ำสุด)  บน 25% = แข็ง  ล่าง 25% = อ่อน"))
    hi, lo = 104, 97
    Y = lambda p: 110 + 300 * (hi - p) / (hi - lo)
    cx = 260
    for a, b, col, lab in ((0.75, 1, C["bull"], t("strong (top 25%)", "แข็ง (บน 25%)")), (0.25, 0.75, C["dim"], t("middle", "กลาง")),
                           (0, 0.25, C["bear"], t("weak (bottom 25%)", "อ่อน (ล่าง 25%)"))):
        ya, yb = Y(lo + b * (hi - lo)), Y(lo + a * (hi - lo))
        s.rect(cx - 150, ya, 300, yb - ya, fill=col, opacity=0.12, rx=4)
        s.text(cx + 170, (ya + yb) / 2 + 5, lab, 13, col, weight=700)
    _big_candle(s, cx, Y(100), Y(103), Y(104), Y(97), 60, C["bull"])
    for p, txt in ((104, "H 104"), (103, "C 103"), (100, "O 100"), (97, "L 97")):
        s.text(cx - 160, Y(p) + 5, txt, 13, C["text"], "end", 700)
    s.card(560, 110, 370, 300, t("The example candle", "แท่งตัวอย่าง"), None, C["amber"])
    lines = [(t("Range", "กรอบ"), "104 − 97 = 7"), (t("Body", "ตัวแท่ง"), "103 − 100 = 3"),
             (t("Lower wick", "ไส้ล่าง"), "100 − 97 = 3"), (t("Upper wick", "ไส้บน"), "104 − 103 = 1"),
             (t("Close location", "ตำแหน่งปิด"), "(103 − 97) ÷ 7 = 86%")]
    for k, (a, b) in enumerate(lines):
        s.text(580, 170 + k * 38, a, 14, C["muted"])
        s.text(910, 170 + k * 38, b, 15, C["amber"] if k == 4 else C["text"], "end", 700)
    s.text(580, 380, t("86% → top 25%: buyers won the close.", "86% → อยู่บน 25%: ผู้ซื้อชนะตอนปิด"), 14, C["bull"], weight=700)
    return s.render()


@fig
def pin_quality(lang):
    t = tr(lang)
    s = SVG(960, 480, t("Is it a real pin bar? Two quality checks", "พินบาร์จริงไหม? ตรวจคุณภาพสองข้อ"),
            t("Check 1: lower wick ≥ 2× body. Check 2: close in the top third of the range (≥ 67%).",
              "ข้อ 1: ไส้ล่าง ≥ 2 เท่าของตัวแท่ง  ข้อ 2: ปิดในหนึ่งในสามบนของกรอบ (≥ 67%)"))
    hi, lo = 51.2, 47.8
    Y = lambda p: 130 + 200 * (hi - p) / (hi - lo)
    cands = [("A", (50.0, 50.8, 48.0, 50.6)), ("B", (50.0, 50.9, 49.0, 50.8)), ("C", (49.6, 51.0, 48.0, 49.4))]
    for k, (name, (o, h, l, c)) in enumerate(cands):
        x = 170 + k * 310
        body, lw = abs(c - o), min(o, c) - l
        ratio, cl = lw / body, (c - l) / (h - l)
        ok1, ok2 = ratio >= 2, cl >= 0.67
        col = C["bull"] if c >= o else C["bear"]
        _big_candle(s, x, Y(o), Y(c), Y(h), Y(l), 44, col)
        s.text(x, 100, t(f"Candle {name}", f"แท่ง {name}"), 16, C["text"], "middle", 700)
        s.text(x, 360, f"O {o:g} · H {h:g} · L {l:g} · C {c:g}", 12, C["muted"], "middle")
        s.text(x, 386, t(f"wick ÷ body = {lw:.1f} ÷ {body:.1f} = {ratio:.1f}×", f"ไส้ ÷ ตัว = {lw:.1f} ÷ {body:.1f} = {ratio:.1f} เท่า"), 13,
               C["bull"] if ok1 else C["bear"], "middle", 700)
        s.text(x, 408, t(f"close location {cl:.0%}", f"ตำแหน่งปิด {cl:.0%}"), 13, C["bull"] if ok2 else C["bear"], "middle", 700)
        verdict = (t("PASS", "ผ่าน"), C["bull"]) if ok1 and ok2 else (t("FAIL", "ไม่ผ่าน"), C["bear"])
        s.pill(x, 448, verdict[0], verdict[1], 14)
    return s.render()


@fig
def stop_by_tf(lang):
    t = tr(lang)
    s = SVG(960, 460, t("Same trade idea, three entry timeframes", "ไอเดียเทรดเดียวกัน สามไทม์เฟรมสำหรับเข้า"),
            t("Entry 100, target 104 (from the daily trend), risk 100 USD per trade (illustrative).",
              "เข้าที่ 100 เป้า 104 (จากเทรนด์รายวัน) เสี่ยง 100 ดอลลาร์ต่อไม้ (ตัวอย่าง)"))
    rows = [(t("Trigger on 5m", "สัญญาณบน 5m"), 99.5, C["bull"]), (t("Trigger on 1H", "สัญญาณบน 1H"), 98.5, C["amber"]),
            (t("Trigger on Daily", "สัญญาณบนรายวัน"), 96.0, C["bear"])]
    X = lambda p: 300 + (p - 95) * 60
    for p in (96, 98, 100, 102, 104):
        s.line(X(p), 110, X(p), 360, C["grid"], 1)
        s.text(X(p), 380, f"{p}", 12, C["muted"], "middle")
    for k, (name, stop, col) in enumerate(rows):
        y = 130 + k * 78
        risk = 100 - stop
        s.text(40, y + 26, name, 15, col, weight=700)
        s.rect(X(stop), y + 8, X(100) - X(stop), 30, fill=C["bear"], opacity=0.5, rx=3)
        s.rect(X(100), y + 8, X(104) - X(100), 30, fill=C["bull"], opacity=0.35, rx=3)
        s.text(X(stop) - 8, y + 29, t(f"stop {stop:g}", f"Stop {stop:g}"), 12, C["text"], "end")
        s.text(X(104) + 10, y + 22, f"R:R {4 / risk:.2g}", 14, col, weight=700)
        s.text(X(104) + 10, y + 42, t(f"size {100 / risk:.0f} units", f"ขนาด {100 / risk:.0f} หน่วย"), 12, C["muted"])
    s.text(40, 420, t("Smaller trigger timeframe → tighter stop → bigger size and better R:R for the same 100 USD risk, but more noise.",
                      "ไทม์เฟรมสัญญาณเล็กลง → Stop แคบลง → ขนาดใหญ่ขึ้นและ R:R ดีขึ้นที่ความเสี่ยง 100 ดอลลาร์เท่าเดิม แต่มีสัญญาณรบกวนมากขึ้น"), 13, C["amber"], weight=600)
    return s.render()
