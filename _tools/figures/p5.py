"""Phase 5 figures: Liquidity & ICT concepts."""
from charts import SVG, CandleChart, C, tr
from figures.p2 import walk, extend, first_close, panel

FIGURES = {}


def fig(fn):
    FIGURES["p5-" + fn.__name__.replace("_", "-")] = fn
    return fn


def fvg_of(cs, i):
    """Bullish FVG formed by candles i, i+1, i+2 -> (low, high) or None."""
    lo, hi = cs[i][1], cs[i + 2][2]
    return (lo, hi) if hi > lo else None


# ---------------------------------------------------------------- 5.1
@fig
def liquidity_pools(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Liquidity = resting orders. It pools above highs and below lows.",
                        "สภาพคล่อง = คำสั่งที่รออยู่ มันกองรวมอยู่เหนือจุดสูงและใต้จุดต่ำ"),
            t("The more obvious the level, the more orders sit just beyond it.",
              "ยิ่งระดับราคาชัดเจนเท่าไหร่ คำสั่งก็ยิ่งกองอยู่ถัดออกไปมากเท่านั้น"))
    piv = [105, 110, 100.3, 109.95, 100.1, 110.05, 100.2, 105.5]
    cs, idx = walk(piv, [4, 5, 5, 5, 5, 5, 3], seed=5)
    panel(s, 28, 90, 600, 390)
    ch = CandleChart(s, 44, 140, 568, 290, cs, pmin=97, pmax=113, grid=False)
    ch.zone(110.2, 111.8, C["bull"], opacity=0.12)
    ch.zone(98.4, 99.9, C["bear"], opacity=0.12)
    ch.hline(110.1, None, C["bull"], dash="2 3")
    ch.hline(100.0, None, C["bear"], dash="2 3")
    ch.draw()
    for k in (1, 3, 5):
        ch.label(idx[k], cs[idx[k]][1], "=", C["bull"], dy=-8, size=14)
    for k in (2, 4, 6):
        ch.label(idx[k], cs[idx[k]][2], "=", C["bear"], dy=20, size=14)
    s.text(60, 128, t("BSL · buy-side liquidity (equal highs)", "BSL · สภาพคล่องฝั่งซื้อ (จุดสูงเท่ากัน)"), 14, C["bull"], weight=700)
    s.text(60, 466, t("SSL · sell-side liquidity (equal lows)", "SSL · สภาพคล่องฝั่งขาย (จุดต่ำเท่ากัน)"), 14, C["bear"], weight=700)
    s.card(650, 90, 282, 190, t("Above the highs", "เหนือจุดสูง"),
           t("· Stop-losses of shorts\n  (= market BUY orders)\n· Buy-stop breakout entries\n→ fuel for a big SELLER",
             "· Stop Loss ของคน Short\n  (= Market Order ฝั่งซื้อ)\n· คำสั่ง Buy Stop เข้าตอนเบรก\n→ เชื้อเพลิงของผู้ขายรายใหญ่"),
           C["bull"], 17, 14)
    s.card(650, 290, 282, 190, t("Below the lows", "ใต้จุดต่ำ"),
           t("· Stop-losses of longs\n  (= market SELL orders)\n· Sell-stop breakdown entries\n→ fuel for a big BUYER",
             "· Stop Loss ของคน Long\n  (= Market Order ฝั่งขาย)\n· คำสั่ง Sell Stop เข้าตอนหลุด\n→ เชื้อเพลิงของผู้ซื้อรายใหญ่"),
           C["bear"], 17, 14)
    return s.render()


@fig
def who_needs(lang):
    t = tr(lang)
    s = SVG(960, 460, t("Why a big seller needs your buy stops", "ทำไมผู้ขายรายใหญ่ต้องการ Buy Stop ของคุณ"),
            t("To sell size without crashing the price, you need lots of buyers at once. Stops provide them.",
              "การขายก้อนใหญ่โดยไม่ทำให้ราคาร่วง ต้องมีผู้ซื้อจำนวนมากพร้อมกัน Stop ให้สิ่งนั้น"))
    steps = [
        (t("1 · Orders pile up", "1 · คำสั่งกองรวมกัน"),
         t("Equal highs at 110. Shorts put\nstops just above; breakout\ntraders put buy-stops there too.",
           "จุดสูงเท่ากันที่ 110 คน Short วาง\nStop เหนือนั้น นักเทรดเบรกเอาท์\nก็วาง Buy Stop ไว้ตรงนั้นเช่นกัน"), 0),
        (t("2 · The run", "2 · การวิ่งไปกวาด"),
         t("Price pushes through 110.\nStops fire as market BUYS.\nThe big seller fills into them.",
           "ราคาดันทะลุ 110 Stop ทำงาน\nกลายเป็น Market Order ฝั่งซื้อ\nผู้ขายรายใหญ่ขายใส่พวกเขา"), 1),
        (t("3 · Fuel gone", "3 · เชื้อเพลิงหมด"),
         t("No buyers left above. Price\ncloses back below 110 and\nfalls: a sweep (5.2).",
           "ผู้ซื้อด้านบนหมดแล้ว ราคาปิด\nกลับใต้ 110 แล้วร่วงลง:\nการกวาด (Sweep, 5.2)"), 2),
    ]
    base, _ = walk([104, 109.9, 106, 110, 106.8], [4, 3, 3, 3], seed=7)
    for k, (head, body, stage) in enumerate(steps):
        x = 28 + k * 308
        panel(s, x, 90, 290, 350, head, [C["amber"], C["bull"], C["bear"]][k])
        cs = [c[:] for c in base]
        if stage >= 1:
            o = cs[-1][3]
            cs = extend(cs, [[o, 111.4, o - 0.2, 110.6]])
        if stage >= 2:
            cs = extend(cs, [[110.6, 110.8, 108.9, 109.1], [109.1, 109.3, 106.4, 106.7], [106.7, 107.2, 104.6, 105.0]])
        ch = CandleChart(s, x + 14, 130, 262, 190, base + [base[-1]] * 4, pmin=102.5, pmax=112.5, grid=False)
        ch.cs = cs  # same scale in all three panels, fewer candles drawn
        ch.hline(110.05, None, C["amber"], dash="4 4")
        if stage == 0:
            s.text(ch.X(len(base) - 1), ch.Y(111.2), "$ $ $ $", 13, C["bull"], "middle", 700)
        ch.draw(highlight={len(base): C["bull"]} if stage >= 1 else None)
        s.text(x + 18, 360, body, 13, C["text"])
    return s.render()


# ---------------------------------------------------------------- 5.2
def _sweep_chart():
    pre, idx = walk([104, 99.5, 109.8, 105.5, 109.9, 106.2, 108.8], [4, 6, 3, 3, 3, 2], seed=12)
    o = pre[-1][3]
    cs = extend(pre, [[o, 111.3, o - 0.2, 109.2]])
    sw = len(cs) - 1
    down, _ = walk([109.2, 109.6, 104.6, 107.6, 99.2], [1, 4, 3, 6], seed=13)
    cs = extend(cs, down[1:])
    return cs, idx, sw


@fig
def sweep(lang):
    t = tr(lang)
    s = SVG(960, 520, t("A liquidity sweep: take the stops, then reverse", "การกวาดสภาพคล่อง: เก็บ Stop แล้วกลับตัว"),
            t("Wick beyond the pool → close back inside → displacement the other way → structure shift.",
              "ไส้ทะลุกองสภาพคล่อง → ปิดกลับเข้ามา → แรงส่งสวนทาง → โครงสร้างเปลี่ยน"))
    cs, idx, sw = _sweep_chart()
    panel(s, 28, 90, 904, 410)
    ch = CandleChart(s, 40, 120, 700, 350, cs, pmin=97.5, pmax=112.5)
    ch.hline(109.9, t("equal highs = BSL", "จุดสูงเท่ากัน = BSL"), C["amber"], idx[2] - 1, sw, "4 4", side="left")
    ch.hline(99.5, t("SSL (target)", "SSL (เป้าหมาย)"), C["bear"], idx[1] - 1, None, "4 4", side="left")
    lvl = cs[idx[5]][2]
    j = first_close(cs, sw + 1, lvl, False)
    ch.hline(lvl, None, C["purple"], idx[5], j, "6 4")
    ch.label((idx[5] + j) / 2, lvl, "CHoCH / MSS", C["purple"], dy=22, size=13)
    ch.draw(highlight={sw: C["bear"]})
    ch.label(sw, cs[sw][1], t("sweep", "กวาด"), C["bear"], dy=-12)
    ent = 107.6
    ch.hline(ent, t("entry on retrace", "เข้าตอนย่อกลับ"), C["blue"], j, None, "3 3", side="right", size=12)
    ch.hline(111.6, t("stop above sweep", "Stop เหนือจุดกวาด"), C["bear"], sw, None, "3 3", side="right", size=12)
    notes = [
        (C["amber"], t("1 · Pool", "1 · กองสภาพคล่อง"), t("obvious equal highs", "จุดสูงเท่ากันที่ชัดเจน")),
        (C["bear"], t("2 · Sweep", "2 · กวาด"), t("wick above, close back below", "ไส้ทะลุขึ้น ปิดกลับลงมา")),
        (C["purple"], t("3 · Shift", "3 · เปลี่ยนโครงสร้าง"), t("displacement + CHoCH down", "แรงส่ง + CHoCH ลง")),
        (C["blue"], t("4 · Entry", "4 · จุดเข้า"), t("retrace, stop above sweep", "ย่อกลับ Stop เหนือจุดกวาด")),
        (C["bull"], t("5 · Target", "5 · เป้าหมาย"), t("the opposite pool (SSL)", "กองสภาพคล่องฝั่งตรงข้าม (SSL)")),
    ]
    for k, (col, head, body) in enumerate(notes):
        y = 128 + k * 72
        s.text(760, y, head, 15, col, weight=700)
        s.text(760, y + 22, body, 12, C["muted"])
    return s.render()


@fig
def sweep_vs_run(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Sweep or run? The close and what follows decide", "กวาดหรือวิ่งทะลุ? ราคาปิดและสิ่งที่ตามมาเป็นตัวตัดสิน"),
            t("Taking liquidity does not always mean reversal. Sometimes price takes it and keeps going.",
              "การกินสภาพคล่องไม่ได้แปลว่าต้องกลับตัวเสมอ บางครั้งราคากินแล้ววิ่งต่อ"))
    base, _ = walk([103, 109.8, 105.6, 109.9, 106.4], [4, 3, 3, 3], seed=21)
    for k in range(2):
        x = 28 + k * 460
        rev = k == 0
        col = C["bear"] if rev else C["bull"]
        panel(s, x, 90, 444, 360, t("Sweep → reversal", "กวาด → กลับตัว") if rev else t("Run → continuation", "วิ่งทะลุ → ไปต่อ"), col)
        cs = [c[:] for c in base]
        o = cs[-1][3]
        if rev:
            cs = extend(cs, [[o, 111.5, o - 0.2, 109.0], [109.0, 109.2, 106.8, 107.0]])
            more, _ = walk([107.0, 107.8, 103.6, 104.8, 101.5], [1, 3, 2, 3], seed=22)
        else:
            cs = extend(cs, [[o, 111.6, o - 0.2, 111.3], [111.3, 112.6, 110.9, 112.3]])
            more, _ = walk([112.3, 113.0, 110.5, 116.5], [1, 3, 4], seed=23)
        cs = extend(cs, more[1:])
        ch = CandleChart(s, x + 16, 135, 412, 220, cs, pmin=100, pmax=118, grid=False)
        ch.hline(109.9, "BSL", C["amber"], side="left")
        ch.draw(highlight={len(base): col})
        s.text(x + 18, 385, t("Close back below + displacement down\n+ CHoCH = the pool was the fuel for sellers.",
                              "ปิดกลับลงมา + แรงส่งลง + CHoCH\n= กองสภาพคล่องคือเชื้อเพลิงของผู้ขาย") if rev else
               t("Closes above and holds; retest becomes support.\nPrice is drawing to the NEXT pool higher up.",
                 "ปิดเหนือและยืนได้ การทดสอบซ้ำกลายเป็นแนวรับ\nราคากำลังวิ่งไปหากองสภาพคล่อง ถัดไป ด้านบน"), 13, C["text"])
    return s.render()


# ---------------------------------------------------------------- 5.3
@fig
def dealing_range(lang):
    t = tr(lang)
    s = SVG(960, 500, t("The dealing range: buy in discount, sell in premium", "Dealing Range: ซื้อในโซนส่วนลด ขายในโซนพรีเมียม"),
            t("Range = swing low to swing high of the current leg. 50% = equilibrium.",
              "กรอบ = จาก Swing Low ถึง Swing High ของขาปัจจุบัน 50% = จุดสมดุล"))
    piv = [100, 106, 103.2, 120, 107.6, 124]
    cs, idx = walk(piv, [5, 3, 8, 6, 6], seed=31)
    panel(s, 28, 90, 904, 390)
    ch = CandleChart(s, 40, 120, 640, 330, cs, pmin=97, pmax=126, grid=False)
    lo, hi = cs[idx[2]][2], cs[idx[3]][1]
    eq = (lo + hi) / 2
    i0 = idx[2]
    ch.zone(eq, hi, C["bear"], t("PREMIUM · sell side", "พรีเมียม · ฝั่งขาย"), i0=i0, opacity=0.10, label_side="left")
    ch.zone(lo, eq, C["bull"], t("DISCOUNT · buy side", "ส่วนลด · ฝั่งซื้อ"), i0=i0, opacity=0.10, label_side="right", label_pos="below")
    ote_hi, ote_lo = hi - 0.62 * (hi - lo), hi - 0.79 * (hi - lo)
    ch.zone(ote_lo, ote_hi, C["blue"], "OTE 62–79%", i0=idx[3], opacity=0.22, label_side="left")
    ch.hline(eq, t("equilibrium 50%", "จุดสมดุล 50%"), C["amber"], i0, side="left")
    ch.draw()
    ch.label(idx[2], lo, t("swing low", "Swing Low"), C["muted"], dy=24, size=12)
    ch.label(idx[3], hi, t("swing high", "Swing High"), C["muted"], dy=-12, size=12)
    s.card(700, 110, 220, 160, t("In an uptrend", "ในขาขึ้น"),
           t("Buy only below 50%.\nBest: the OTE band\n(62–79% retrace)\nwith a PD array (5.4–5.5).", "ซื้อเฉพาะใต้ 50%\nดีที่สุด: แถบ OTE\n(ย่อ 62–79%)\nร่วมกับ PD Array (5.4–5.5)"),
           C["bull"], 16, 13)
    s.card(700, 284, 220, 170, t("Why it matters", "ทำไมจึงสำคัญ"),
           t("Buying in premium = paying\nthe most for the least R:R.\nDiscount gives room for\nthe stop AND the target.", "ซื้อในพรีเมียม = จ่ายแพงสุด\nได้ R:R น้อยสุด\nส่วนลดให้ที่ว่างทั้งกับ\nStop และเป้าหมาย"),
           C["amber"], 16, 13)
    return s.render()


# ---------------------------------------------------------------- 5.4
@fig
def fvg_anatomy(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Fair Value Gap: three candles, one gap", "Fair Value Gap: สามแท่ง หนึ่งช่องว่าง"),
            t("The middle candle moved so fast that candles 1 and 3 don't overlap. Price traded one-sided there.",
              "แท่งกลางวิ่งเร็วมากจนแท่งที่ 1 กับ 3 ไม่ซ้อนกัน ราคาซื้อขายแค่ฝั่งเดียวในช่วงนั้น"))
    bull = [[99.6, 101.0, 99.2, 100.7], [100.7, 104.8, 100.5, 104.5], [104.5, 105.6, 102.6, 105.2], [105.2, 105.9, 104.3, 104.6]]
    bear = [[105.4, 105.8, 104.0, 104.3], [104.3, 104.5, 100.2, 100.5], [100.5, 102.4, 99.4, 99.8], [99.8, 100.9, 99.1, 100.6]]
    for k, (cs, col, name) in enumerate(((bull, C["bull"], t("Bullish FVG", "FVG ขาขึ้น")),
                                         (bear, C["bear"], t("Bearish FVG", "FVG ขาลง")))):
        x = 28 + k * 460
        panel(s, x, 90, 444, 360, name, col, 18)
        ch = CandleChart(s, x + 30, 130, 240, 270, cs, pmin=98.5, pmax=106.5, grid=False)
        if k == 0:
            a, b = cs[0][1], cs[2][2]
        else:
            a, b = cs[2][1], cs[0][2]
        ch.zone(a, b, col, i0=0, opacity=0.25)
        ch.hline((a + b) / 2, None, C["white"], 0, 3, "3 3")
        ch.draw()
        for i in range(3):
            ch.label(i, cs[i][2], str(i + 1), C["muted"], dy=22, size=13)
        lx = x + 290
        s.text(lx, ch.Y(max(a, b)) + 4, t("candle 3 low" if k == 0 else "candle 1 low", "จุดต่ำแท่ง 3" if k == 0 else "จุดต่ำแท่ง 1"), 12, col, weight=700)
        s.text(lx, ch.Y((a + b) / 2) + 4, t("CE = 50%", "CE = 50%"), 12, C["white"], weight=700)
        s.text(lx, ch.Y(min(a, b)) + 4, t("candle 1 high" if k == 0 else "candle 3 high", "จุดสูงแท่ง 1" if k == 0 else "จุดสูงแท่ง 3"), 12, col, weight=700)
        s.text(x + 18, 425, t("Often acts as support on the return." if k == 0 else "Often acts as resistance on the return.",
                              "มักทำหน้าที่เป็นแนวรับเมื่อราคากลับมา" if k == 0 else "มักทำหน้าที่เป็นแนวต้านเมื่อราคากลับมา"), 13, C["muted"])
    return s.render()


@fig
def fvg_trade(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Trading the return to an FVG", "เทรดตอนราคากลับมาที่ FVG"),
            t("Displacement leaves a gap → price often returns to rebalance it → continuation if the gap holds.",
              "แรงส่งทิ้งช่องว่างไว้ → ราคามักกลับมาเติมให้สมดุล → ไปต่อถ้าช่องว่างยืนได้"))
    pre, _ = walk([100, 105.2, 101.8, 103.0], [5, 4, 2], seed=41)
    o = pre[-1][3]
    cs = extend(pre, [[o, 103.4, o - 0.4, 103.1], [103.1, 107.6, 103.0, 107.4], [107.4, 108.7, 105.8, 108.4]])
    gi = len(pre)
    a, b = fvg_of(cs, gi)
    ce = (a + b) / 2
    more, _ = walk([108.4, 109.2, ce - 0.05, 106.6, 113.5], [1, 4, 2, 6], seed=42)
    cs = extend(cs, more[1:])
    ret = gi + 3 + 4
    panel(s, 28, 90, 904, 360)
    ch = CandleChart(s, 40, 115, 700, 310, cs, pmin=99, pmax=115, grid=False)
    ch.zone(a, b, C["bull"], "FVG", i0=gi, opacity=0.22, label_side="left")
    ch.hline(ce, "CE", C["white"], gi, None, "3 3", side="right", size=11)
    ch.draw(highlight={gi + 1: C["bull"], ret: C["blue"]})
    ch.label(gi + 1, cs[gi + 1][1], t("displacement", "แรงส่ง"), C["bull"], dy=-12, size=12)
    ch.label(ret, cs[ret][2], t("return to CE", "กลับมาที่ CE"), C["blue"], dy=24, size=12)
    s.card(760, 105, 160, 150, t("Valid if…", "ใช้ได้เมื่อ…"),
           t("· in trend direction\n· in discount\n· formed by\n  displacement", "· ตามทิศทางเทรนด์\n· อยู่ในส่วนลด\n· เกิดจาก\n  แรงส่ง"), C["bull"], 15, 12)
    s.card(760, 268, 160, 160, t("Invalid if…", "ใช้ไม่ได้เมื่อ…"),
           t("· a candle CLOSES\n  through it\n· it becomes an\n  inverse FVG", "· มีแท่ง ปิด ทะลุ\n  ผ่านมัน\n· กลายเป็น\n  Inverse FVG"), C["bear"], 15, 12)
    return s.render()


# ---------------------------------------------------------------- 5.5
@fig
def order_block(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Order block: the last opposite candle before displacement", "Order Block: แท่งสวนทางแท่งสุดท้ายก่อนแรงส่ง"),
            t("Bullish OB = last down candle before an up-move that breaks structure.",
              "Bullish OB = แท่งแดงแท่งสุดท้ายก่อนการขึ้นที่เบรกโครงสร้าง"))
    pre, idx = walk([108, 103.5, 106.2, 102.4], [5, 3, 4], seed=51)
    o = pre[-1][3]
    cs = extend(pre, [[o, o + 0.3, 101.8, 102.1]])
    obi = len(cs) - 1
    cs = extend(cs, [[102.1, 105.4, 102.0, 105.2], [105.2, 107.6, 105.0, 107.3], [107.3, 108.4, 106.6, 108.1]])
    more, _ = walk([108.1, 108.8, 103.4, 104.6, 112], [1, 5, 1, 5], seed=52)
    cs = extend(cs, more[1:])
    panel(s, 28, 90, 904, 360)
    ch = CandleChart(s, 40, 115, 700, 310, cs, pmin=100, pmax=113, grid=False)
    ob_hi, ob_lo = cs[obi][0], cs[obi][2]
    ch.zone(ob_lo, ob_hi, C["bull"], t("Bullish OB", "Bullish OB"), i0=obi, opacity=0.22, label_side="right", label_pos="below")
    lh = cs[idx[2]][1]
    j = first_close(cs, obi + 1, lh, True)
    ch.hline(lh, "BOS", C["purple"], idx[2], j, "6 4", side="left", size=13)
    ch.draw(highlight={obi: C["bull"]})
    s.card(760, 105, 160, 160, t("Draw it", "ขีดอย่างไร"),
           t("Open → low of the\nlast down candle.\nMean threshold =\n50% of the OB.", "ราคาเปิด → จุดต่ำ\nของแท่งแดงแท่งสุดท้าย\nMean Threshold =\n50% ของ OB"), C["bull"], 15, 12)
    s.card(760, 278, 160, 150, t("Needs", "ต้องมี"),
           t("· displacement\n· BOS / MSS\n· ideally an FVG\n· in discount", "· แรงส่ง\n· BOS / MSS\n· ดีถ้ามี FVG\n· อยู่ในส่วนลด"), C["purple"], 15, 12)
    return s.render()


@fig
def breaker(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Breaker: an order block that failed and flipped", "Breaker: Order Block ที่ล้มเหลวแล้วพลิกบทบาท"),
            t("When price closes through an OB, the trapped orders there turn it into resistance (role reversal, 2.4).",
              "เมื่อราคาปิดทะลุ OB คำสั่งที่ติดอยู่ตรงนั้นทำให้มันกลายเป็นแนวต้าน (การสลับบทบาท 2.4)"))
    pre, _ = walk([106, 102.8, 104.6, 102.3], [4, 3, 3], seed=61)
    o = pre[-1][3]
    cs = extend(pre, [[o, o + 0.2, 101.9, 102.2]])
    obi = len(cs) - 1
    cs = extend(cs, [[102.2, 104.5, 102.1, 104.3], [104.3, 105.6, 103.9, 105.2]])
    more, _ = walk([105.2, 105.6, 101.2, 100.4, 97.2, 102.3, 101.6, 94.5], [1, 3, 1, 3, 4, 1, 5], seed=62)
    cs = extend(cs, more[1:])
    panel(s, 28, 90, 904, 360)
    ch = CandleChart(s, 40, 115, 700, 310, cs, pmin=93, pmax=108, grid=False)
    ob_hi, ob_lo = cs[obi][0], cs[obi][2]
    brk = first_close(cs, obi + 3, ob_lo, False)
    ch.zone(ob_lo, ob_hi, C["bull"], t("bullish OB", "Bullish OB"), i0=obi, i1=brk - 1, opacity=0.2, label_pos="above")
    ch.zone(ob_lo, ob_hi, C["bear"], t("→ bearish breaker", "→ Bearish Breaker"), i0=brk, opacity=0.2, label_side="right", label_pos="above")
    ch.draw(highlight={brk: C["bear"]})
    ch.label(brk, cs[brk][2], t("close through", "ปิดทะลุ"), C["bear"], dy=24, size=12, anchor="end", dx=-14)
    s.card(760, 105, 160, 320, t("Story", "เรื่องราว"),
           t("1 Buyers defend\n  the OB.\n2 Sellers close\n  price through it:\n  buyers trapped.\n3 On the retest,\n  trapped buyers\n  sell to exit.\n→ resistance.",
             "1 ผู้ซื้อป้องกัน\n  OB\n2 ผู้ขายปิดราคา\n  ทะลุลงไป:\n  ผู้ซื้อติดกับ\n3 ตอนทดสอบซ้ำ\n  ผู้ซื้อที่ติด\n  ขายเพื่อออก\n→ แนวต้าน"), C["bear"], 15, 12)
    return s.render()


# ---------------------------------------------------------------- 5.6
@fig
def sessions(lang):
    t = tr(lang)
    s = SVG(960, 460, t("Sessions and killzones (New York time)", "เซสชันและ Killzone (เวลานิวยอร์ก)"),
            t("Liquidity and volatility arrive when big centres open. ICT focuses on these windows.",
              "สภาพคล่องและความผันผวนมาพร้อมการเปิดของศูนย์กลางการเงินใหญ่ ICT โฟกัสที่ช่วงเวลาเหล่านี้"))
    x0, w = 120, 800
    X = lambda h: x0 + w * h / 24
    panel(s, 28, 90, 904, 350)
    for h in range(0, 25, 2):
        s.line(X(h), 120, X(h), 380, C["grid"], 1)
        s.text(X(h), 116, f"{h:02d}", 11, C["muted"], "middle")
    s.text(40, 116, t("NY", "นิวยอร์ก"), 11, C["muted"], weight=700)
    rows = [
        (150, t("Sessions", "เซสชัน"), [(19, 24, C["purple"], t("Asia", "เอเชีย")), (0, 4, C["purple"], ""),
                                       (3, 12, C["blue"], t("London", "ลอนดอน")), (8, 17, C["amber"], t("New York", "นิวยอร์ก"))]),
        (250, t("Killzones", "Killzone"), [(20, 24, C["purple"], t("Asian KZ", "Asian KZ")),
                                            (2, 5, C["blue"], t("London KZ", "London KZ")),
                                            (7, 10, C["amber"], t("NY AM KZ", "NY AM KZ")),
                                            (10, 12, C["teal"], t("LDN close", "LDN close"))]),
    ]
    for y, name, bars in rows:
        s.text(40, y + 22, name, 13, C["text"], weight=700)
        lanes = {}
        for k, (a, b, col, lab) in enumerate(bars):
            lane = 0 if y == 250 else (1 if lab in (t("New York", "นิวยอร์ก"),) else 0)
            yy = y + lane * 38
            s.rect(X(a), yy, X(b) - X(a), 30, fill=col, opacity=0.75, rx=6)
            if lab:
                s.text((X(a) + X(b)) / 2, yy + 20, lab, 12, C["white"], "middle", 700)
    s.text(40, 330, t("Bangkok", "กรุงเทพฯ"), 12, C["text"], weight=700)
    for h in range(0, 25, 2):
        s.text(X(h), 330, f"{(h + 12) % 24:02d}", 11, C["teal"], "middle")
    s.text(40, 350, t("(winter)", "(ฤดูหนาว)"), 10, C["muted"])
    s.text(40, 410, t("Summer (US daylight saving): Bangkok = NY + 11 h. Winter: NY + 12 h. ICT times are always quoted in New York time.",
                      "ฤดูร้อน (สหรัฐฯ ปรับเวลา): กรุงเทพฯ = นิวยอร์ก + 11 ชม. ฤดูหนาว: + 12 ชม. เวลาของ ICT อ้างอิงเวลานิวยอร์กเสมอ"),
           12, C["muted"])
    return s.render()


@fig
def amd(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Power of Three: accumulate → manipulate → distribute", "Power of Three: สะสม → หลอก → กระจาย"),
            t("One way ICT reads a bullish day. A model to test, not a law.", "วิธีที่ ICT อ่านวันขาขึ้นหนึ่งวัน เป็นโมเดลที่ต้องทดสอบ ไม่ใช่กฎตายตัว"))
    panel(s, 28, 90, 620, 390)
    path = [100, 100.4, 99.7, 100.3, 99.8, 100.2, 99.6, 98.9, 98.3, 98.6, 99.4, 100.6, 101.8, 101.3, 102.6, 103.8, 103.2, 104.1, 103.6, 103.5]
    lo, hi = 97.5, 105
    X = lambda i: 60 + i * 30
    Y = lambda p: 130 + 300 * (hi - p) / (hi - lo)
    phases = [(0, 6, C["purple"], t("A · Asia", "A · เอเชีย"), t("accumulation:\ntight range", "สะสม:\nกรอบแคบ")),
              (6, 10, C["bear"], t("M · London", "M · ลอนดอน"), t("manipulation:\nfalse move down\n(Judas swing)", "หลอก:\nวิ่งลงหลอก\n(Judas Swing)")),
              (10, 19, C["bull"], t("D · New York", "D · นิวยอร์ก"), t("distribution:\nreal move up", "กระจาย:\nการวิ่งจริงขึ้น"))]
    for a, b, col, name, desc in phases:
        s.rect(X(a), 110, X(b) - X(a), 340, fill=col, opacity=0.08)
        s.text((X(a) + X(b)) / 2, 128, name, 13, col, "middle", 700)
        s.text((X(a) + X(b)) / 2, 400, desc, 11, C["muted"], "middle")
    s.line(X(0), Y(100), X(19), Y(100), C["dim"], 1, "4 4")
    s.text(X(0) + 4, Y(100) - 6, t("daily open", "ราคาเปิดวัน"), 11, C["muted"])
    s.polyline([(X(i), Y(p)) for i, p in enumerate(path)], C["text"], 2.5)
    cx = 790
    s.rect(670, 90, 262, 390, fill=C["panel"], stroke=C["border"], rx=12)
    s.text(cx, 118, t("The daily candle", "แท่งเทียนรายวัน"), 15, C["text"], "middle", 700)
    s.line(cx, Y(104.1), cx, Y(98.3), C["bull"], 3)
    s.rect(cx - 30, Y(103.5), 60, Y(100) - Y(103.5), fill=C["bull"], rx=4)
    s.text(cx + 42, Y(100) + 4, t("open", "เปิด"), 12, C["muted"])
    s.text(cx + 42, Y(98.3) + 4, t("low = Judas", "ต่ำสุด = Judas"), 12, C["bear"], weight=700)
    s.text(cx + 42, Y(103.5) + 4, t("close", "ปิด"), 12, C["muted"])
    s.text(cx, 455, t("Buy below the open,\nnot above it.", "ซื้อใต้ราคาเปิด\nไม่ใช่เหนือมัน"), 13, C["amber"], "middle", 700)
    return s.render()


# ---------------------------------------------------------------- 5.7
def _model():
    pre, idx = walk([110, 114, 108, 113.9, 103.2, 107.3, 104.6], [3, 4, 4, 7, 4, 3], seed=71)
    o = pre[-1][3]
    cs = extend(pre, [[o, o + 0.3, 102.2, 104.0]])
    sw = len(cs) - 1
    cs = extend(cs, [[104.0, 104.5, 103.7, 104.3], [104.3, 107.6, 104.2, 107.4], [107.4, 108.6, 106.0, 108.3]])
    gi = sw + 1
    more, _ = walk([108.3, 109.0, 105.3, 106.8, 110.5, 109.4, 114.6], [1, 4, 2, 4, 2, 5], seed=72)
    cs = extend(cs, more[1:])
    return cs, idx, sw, gi


@fig
def model_setup(lang):
    t = tr(lang)
    s = SVG(960, 560, t("An ICT-style long, step by step", "Long แบบ ICT ทีละขั้น"),
            t("HTF bullish → discount → SSL sweep in a killzone → displacement + MSS → FVG entry → BSL target",
              "HTF ขาขึ้น → ส่วนลด → กวาด SSL ใน Killzone → แรงส่ง + MSS → เข้าที่ FVG → เป้า BSL"))
    cs, idx, sw, gi = _model()
    panel(s, 28, 90, 904, 450)
    ch = CandleChart(s, 40, 120, 700, 380, cs, pmin=100.5, pmax=116, grid=False)
    hi, lo = 114.0, cs[sw][2]
    eq = (hi + lo) / 2
    ch.zone(lo, eq, C["bull"], t("discount", "ส่วนลด"), i0=idx[3], opacity=0.06, label_side="left", label_pos="below")
    x0, x1 = ch.X(sw - 1) - ch.step / 2, ch.X(gi + 2) + ch.step / 2
    s.rect(x0, 122, x1 - x0, 376, fill=C["amber"], opacity=0.08, rx=4)
    s.text((x0 + x1) / 2, 136, t("killzone", "Killzone"), 11, C["amber"], "middle", 700)
    ch.hline(113.95, t("BSL · equal highs = target", "BSL · จุดสูงเท่ากัน = เป้าหมาย"), C["bull"], idx[1], None, "4 4", side="right", size=12)
    ch.hline(103.2, "SSL", C["bear"], idx[4] - 3, sw + 2, "4 4", side="left", size=12)
    ch.hline(eq, t("50%", "50%"), C["amber"], idx[3], None, "2 4", side="left", size=11)
    a, b = fvg_of(cs, gi)
    ch.zone(a, b, C["blue"], "FVG", i0=gi, opacity=0.25, label_side="right")
    lh = cs[idx[5]][1]
    j = first_close(cs, sw + 1, lh, True)
    ch.hline(lh, "MSS", C["purple"], idx[5], j, "6 4", side="left", size=12)
    ce = (a + b) / 2
    stop = lo - 0.3
    ch.hline(stop, t("stop", "Stop"), C["bear"], gi, None, "3 3", side="right", size=11)
    ch.draw(highlight={sw: C["bear"], gi + 1: C["bull"]})
    ch.label(sw, lo, t("sweep", "กวาด"), C["bear"], dy=24, size=12)
    r = (113.95 - ce) / (ce - stop)
    steps = [
        (C["purple"], t("1 HTF bias: bullish", "1 ทิศทาง HTF: ขึ้น")),
        (C["bull"], t("2 Price in discount", "2 ราคาอยู่ในส่วนลด")),
        (C["bear"], t("3 SSL swept", "3 กวาด SSL")),
        (C["amber"], t("4 …inside a killzone", "4 …ใน Killzone")),
        (C["purple"], t("5 Displacement + MSS", "5 แรงส่ง + MSS")),
        (C["blue"], t("6 Entry: FVG (CE)", "6 เข้า: FVG (CE)")),
        (C["bear"], t("7 Stop below sweep", "7 Stop ใต้จุดกวาด")),
        (C["bull"], t(f"8 Target BSL ≈ {r:.1f}R", f"8 เป้า BSL ≈ {r:.1f}R")),
    ]
    for k, (col, txt) in enumerate(steps):
        s.text(760, 140 + k * 46, txt, 14, col, weight=700)
    return s.render()


# ---------------------------------------------------------------- 5.8
@fig
def summary(lang):
    t = tr(lang)
    s = SVG(960, 560, t("Phase 5 on one page", "สรุปเฟส 5 ในหน้าเดียว"))
    cx, cy = 480, 310
    nodes = [
        (170, 140, C["amber"], t("5.1–5.2 Liquidity", "5.1–5.2 สภาพคล่อง"), t("Stops pool beyond highs/lows.\nSweep = take it, then reverse.", "Stop กองเหนือ/ใต้จุดสูง/ต่ำ\nกวาด = กินแล้วกลับตัว")),
        (790, 140, C["bull"], t("5.3 Dealing range", "5.3 Dealing Range"), t("Buy discount, sell premium.\n50% = equilibrium.", "ซื้อส่วนลด ขายพรีเมียม\n50% = จุดสมดุล")),
        (150, 320, C["blue"], t("5.4 FVG", "5.4 FVG"), t("3-candle imbalance.\nReturn to CE, then continue.", "ความไม่สมดุล 3 แท่ง\nกลับมาที่ CE แล้วไปต่อ")),
        (810, 320, C["purple"], t("5.5 OB & breaker", "5.5 OB & Breaker"), t("Last opposite candle before\ndisplacement. Failed OB flips.", "แท่งสวนทางสุดท้ายก่อนแรงส่ง\nOB ที่ล้มเหลวจะพลิก")),
        (250, 480, C["teal"], t("5.6 Time", "5.6 เวลา"), t("Killzones in NY time.\nAMD: the Judas move.", "Killzone ตามเวลานิวยอร์ก\nAMD: การวิ่งหลอก Judas")),
        (710, 480, C["pink"], t("5.7 The model", "5.7 โมเดล"), t("Bias → discount → sweep →\nMSS → FVG → opposite pool.", "ทิศทาง → ส่วนลด → กวาด →\nMSS → FVG → กองฝั่งตรงข้าม")),
    ]
    for x, y, col, head, body in nodes:
        s.line(cx, cy, x, y, col, 2, opacity=0.5)
    s.circle(cx, cy, 74, C["panel"], C["text"], 2)
    s.text(cx, cy - 4, t("PHASE 5", "เฟส 5"), 20, C["text"], "middle", 700)
    s.text(cx, cy + 20, t("Liquidity & ICT", "สภาพคล่อง & ICT"), 14, C["muted"], "middle")
    for x, y, col, head, body in nodes:
        s.rect(x - 130, y - 42, 260, 92, fill=C["panel"], stroke=col, rx=12)
        s.text(x, y - 14, head, 17, col, "middle", 700)
        s.text(x, y + 10, body, 13, C["text"], "middle")
    return s.render()


# ================================================================ v2 additions (Oct 2026)
@fig
def stop_cluster(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Why a sweep wick happens: orders resting near an obvious low", "ทำไมไส้เทียนกวาดจึงเกิด: คำสั่งที่รออยู่ใกล้จุดต่ำที่ชัดเจน"),
            t("Illustrative order book for EUR/USD. Normal depth ≈ 20 lots per pip; the stop cluster holds 180 lots.",
              "สมุดคำสั่ง EUR/USD สมมติ ความลึกปกติ ≈ 20 ล็อตต่อ pip กลุ่ม Stop มี 180 ล็อต"))
    levels = [1.0790, 1.0788, 1.0786, 1.0784, 1.0782, 1.0780, 1.0778, 1.0776, 1.0774, 1.0772, 1.0770, 1.0768, 1.0766]
    x0, y0, row = 220, 100, 28
    for i, p in enumerate(levels):
        y = y0 + i * row
        stop = 1.0768 <= p <= 1.0772
        lots = 60 if stop else 20
        col = C["bear"] if stop else C["blue"]
        s.text(x0 - 14, y + 18, f"{p:.4f}", 13, C["amber"] if abs(p - 1.0780) < 1e-9 else C["muted"], "end", 700 if abs(p - 1.0780) < 1e-9 else 400)
        s.rect(x0, y + 4, lots * 6, row - 8, fill=col, opacity=0.85, rx=3)
        s.text(x0 + lots * 6 + 8, y + 18, f"{lots}", 12, C["text"])
    s.line(x0 - 4, y0 + 5 * row + 14, 660, y0 + 5 * row + 14, C["amber"], 1.5, "5 4")
    s.text(x0 + 190, y0 + 5 * row + 10, t("equal lows 1.0780 (SSL)", "จุดต่ำเท่ากัน 1.0780 (SSL)"), 13, C["amber"], weight=700)
    s.text(x0 + 400, y0 + 9 * row + 20, t("← 300 long stops × 0.5 lot = 150\n← 100 breakout sells × 0.3 = 30\n= 180 lots of market SELLS", "← Stop ของ Long 300 ราย × 0.5 ล็อต = 150\n← Breakout ขาย 100 ราย × 0.3 = 30\n= คำสั่งขาย Market 180 ล็อต"), 13, C["bear"], weight=700)
    s.rect(660, 100, 272, 230, fill=C["panel"], stroke=C["border"], rx=12)
    s.text(680, 130, t("What happens", "จะเกิดอะไรขึ้น"), 15, C["text"], weight=700)
    s.text(680, 158, t("1. Price ticks to 1.0772.\n2. 180 lots of stops fire\n   as market sells.\n3. Each pip below holds ~20\n   lots → 180 ÷ 20 ≈ 9 pips\n   of fast drop = the wick.\n4. A big buyer fills 180 lots\n   cheaply, price snaps back.",
                         "1. ราคาลงถึง 1.0772\n2. Stop 180 ล็อตทำงาน\n   เป็นคำสั่งขาย Market\n3. แต่ละ pip ข้างล่างมี ~20\n   ล็อต → 180 ÷ 20 ≈ 9 pip\n   ร่วงเร็ว = ไส้เทียน\n4. ผู้ซื้อรายใหญ่ได้ 180 ล็อต\n   ราคาถูก ราคาดีดกลับ"), 13, C["muted"])
    s.text(48, 478, t("Illustration of the mechanism, not real order-book data. Spot forex has no central book (see 7.3).",
                      "ภาพประกอบกลไก ไม่ใช่ข้อมูลสมุดคำสั่งจริง ฟอเร็กซ์ Spot ไม่มีสมุดคำสั่งกลาง (ดู 7.3)"), 12, C["muted"])
    return s.render()


@fig
def sweep_story(lang):
    t = tr(lang)
    s = SVG(960, 520, t("A sweep, candle by candle (15-minute EUR/USD, illustrative)", "การกวาดทีละแท่ง (EUR/USD 15 นาที ภาพประกอบ)"),
            t("The decision is made on the CLOSE of each candle, never on the wick while it's forming.",
              "การตัดสินใจเกิดตอน ปิด แท่ง ไม่ใช่ตอนไส้เทียนกำลังก่อตัว"))
    cs = [[1.0812, 1.0815, 1.0800, 1.0803], [1.0803, 1.0806, 1.0781, 1.0784], [1.0784, 1.0800, 1.0782, 1.0796],
          [1.0796, 1.0798, 1.0781, 1.0786],
          [1.0786, 1.0790, 1.0784, 1.0786], [1.0786, 1.0790, 1.0768, 1.0784], [1.0784, 1.0812, 1.0782, 1.0810],
          [1.0810, 1.0828, 1.0806, 1.0825], [1.0825, 1.0827, 1.0799, 1.0818], [1.0818, 1.0840, 1.0815, 1.0836]]
    panel(s, 28, 90, 904, 410)
    ch = CandleChart(s, 40, 120, 600, 350, cs, pmin=1.0760, pmax=1.0848)
    ch.hline(1.0781, None, C["amber"], 0, 6, "4 4")
    s.text(ch.X(0) - 10, ch.Y(1.0781) + 18, t("equal lows ≈ 1.0781 (SSL)", "จุดต่ำเท่ากัน ≈ 1.0781 (SSL)"), 12, C["amber"], weight=600)
    ch.hline(1.0815, t("swing high 1.0815", "Swing high 1.0815"), C["purple"], 0, 7, "6 4", side="left")
    ch.zone(1.0790, 1.0806, C["blue"], None, 5, 9, 0.18)
    ch.draw(highlight={5: C["bear"], 7: C["purple"]})
    for k in range(5):
        i = 4 + k
        ch.label(i, cs[i][2], str(k + 1), C["text"], dy=22, size=15)
    notes = [(C["muted"], t("1 · Approach", "1 · เข้าใกล้"), t("price drifts to the equal lows", "ราคาไหลลงหาจุดต่ำเท่ากัน")),
             (C["bear"], t("2 · Sweep", "2 · กวาด"), t("low 1.0768 (13 pips under),\nCLOSE 1.0784: back inside", "ต่ำสุด 1.0768 (ต่ำกว่า 13 pip)\nปิด 1.0784: กลับเข้ามา")),
             (C["bull"], t("3 · Displacement", "3 · แรงส่ง"), t("big green body, close 1.0810", "แท่งเขียวใหญ่ ปิด 1.0810")),
             (C["purple"], t("4 · Shift (MSS)", "4 · เปลี่ยนโครงสร้าง (MSS)"), t("close 1.0825 > swing high 1.0815\nFVG 1.0790–1.0806 left behind", "ปิด 1.0825 > Swing high 1.0815\nเหลือ FVG 1.0790–1.0806")),
             (C["blue"], t("5 · Retrace & entry", "5 · ย่อกลับและเข้า"), t("low 1.0799 tags the FVG CE 1.0798", "ต่ำสุด 1.0799 แตะ CE ของ FVG 1.0798"))]
    for k, (col, head, body) in enumerate(notes):
        y = 128 + k * 74
        s.text(662, y, head, 15, col, weight=700)
        s.text(662, y + 22, body, 12, C["muted"])
    return s.render()


@fig
def range_pips(lang):
    t = tr(lang)
    s = SVG(960, 480, t("The dealing range as a price list (EUR/USD up-leg 1.0800 → 1.0900)", "Dealing range เหมือนป้ายราคา (EUR/USD ขาขึ้น 1.0800 → 1.0900)"),
            t("Same trade idea, two entries. Stop below 1.0795, target 1.0920 (BSL above the high).",
              "ไอเดียเดียวกัน สองจุดเข้า Stop ใต้ 1.0795 เป้า 1.0920 (BSL เหนือจุดสูง)"))
    x0, x1, top, bot = 230, 460, 110, 430
    Y = lambda p: top + (1.0920 - p) / (1.0920 - 1.0790) * (bot - top)
    s.rect(x0, Y(1.0900), x1 - x0, Y(1.0850) - Y(1.0900), fill=C["bear"], opacity=0.15, stroke=C["bear"], rx=4)
    s.rect(x0, Y(1.0850), x1 - x0, Y(1.0800) - Y(1.0850), fill=C["bull"], opacity=0.15, stroke=C["bull"], rx=4)
    s.rect(x0, Y(1.0838), x1 - x0, Y(1.0821) - Y(1.0838), fill=C["blue"], opacity=0.25, stroke=C["blue"], rx=4)
    s.text((x0 + x1) / 2, Y(1.0875) + 5, t("PREMIUM (expensive)", "PREMIUM (แพง)"), 15, C["bear"], "middle", 700)
    s.text((x0 + x1) / 2, Y(1.0862) + 5, t("50 pips", "50 pip"), 12, C["muted"], "middle")
    s.text((x0 + x1) / 2, Y(1.0811) + 5, t("DISCOUNT (cheap)", "DISCOUNT (ถูก)"), 15, C["bull"], "middle", 700)
    s.text((x0 + x1) / 2, Y(1.0829) + 5, t("OTE 1.0821–1.0838", "OTE 1.0821–1.0838"), 12, C["blue"], "middle", 700)
    for p, lab, col in ((1.0920, t("target 1.0920", "เป้า 1.0920"), C["amber"]), (1.0900, "1.0900 high", C["text"]), (1.0850, t("1.0850 equilibrium (50%)", "1.0850 จุดสมดุล (50%)"), C["amber"]),
                        (1.0800, "1.0800 low", C["text"]), (1.0795, t("stop 1.0795", "Stop 1.0795"), C["bear"])):
        s.line(x0 - 10, Y(p), x1 + 10, Y(p), col, 1.4, "4 4")
        s.text(x0 - 16, Y(p) + 4, lab, 12, col, "end", 600)
    for k, (entry, risk, rew, rr, col, head) in enumerate((
            (1.0880, 85, 40, "0.47R", C["bear"], t("Buy in premium at 1.0880", "ซื้อใน Premium ที่ 1.0880")),
            (1.0830, 35, 90, "2.57R", C["bull"], t("Buy in discount at 1.0830", "ซื้อใน Discount ที่ 1.0830")))):
        y = 120 + k * 160
        s.circle(x1 + 30, Y(entry), 6, col)
        s.rect(520, y, 412, 140, fill=C["panel"], stroke=col, rx=12)
        s.text(540, y + 30, head, 16, col, weight=700)
        s.text(540, y + 60, t(f"risk  {risk} pips", f"ความเสี่ยง  {risk} pip"), 14, C["text"])
        s.text(540, y + 86, t(f"reward {rew} pips", f"ผลตอบแทน {rew} pip"), 14, C["text"])
        s.text(540, y + 118, t(f"reward ÷ risk = {rr}", f"ผลตอบแทน ÷ ความเสี่ยง = {rr}"), 16, col, weight=700)
    return s.render()


@fig
def fvg_numbers(lang):
    t = tr(lang)
    s = SVG(960, 480, t("A fair value gap with numbers, and when it's invalid", "Fair value gap พร้อมตัวเลข และเมื่อไหร่ที่มันใช้ไม่ได้"),
            t("Gap = candle 3's low − candle 1's high = 100.60 − 100.20 = 0.40. CE (50%) = 100.40.",
              "ช่องว่าง = Low แท่ง 3 − High แท่ง 1 = 100.60 − 100.20 = 0.40  CE (50%) = 100.40"))
    for k, (title, col, extra) in enumerate(((t("Valid: first return holds", "ใช้ได้: กลับมาครั้งแรกแล้วยืนได้"), C["bull"], [[100.95, 101.05, 100.38, 100.70], [100.70, 101.40, 100.65, 101.30]]),
                                             (t("Invalid: a candle CLOSES below 100.20", "ใช้ไม่ได้: แท่งเทียน ปิด ใต้ 100.20"), C["bear"], [[100.95, 101.00, 100.30, 100.45], [100.45, 100.50, 99.90, 100.05]]))):
        bx = 28 + k * 462
        panel(s, bx, 90, 442, 370, title, col, 15)
        cs = [[99.95, 100.20, 99.95, 100.10], [100.10, 100.95, 100.05, 100.85], [100.85, 101.10, 100.60, 100.95]] + extra
        ch = CandleChart(s, bx + 20, 140, 300, 290, cs, pmin=99.7, pmax=101.6)
        ch.zone(100.20, 100.60, C["blue"], None, 0, 4, 0.18)
        ch.hline(100.40, "CE 100.40", C["blue"], 0, 4, "3 3", size=11)
        ch.draw()
        for i in range(3):
            ch.label(i, cs[i][2], str(i + 1), C["text"], dy=20, size=14)
        s.text(bx + 330, ch.Y(100.20) + 4, t("candle 1 high\n100.20", "High แท่ง 1\n100.20"), 12, C["muted"])
        s.text(bx + 330, ch.Y(100.60) - 14, t("candle 3 low\n100.60", "Low แท่ง 3\n100.60"), 12, C["muted"])
        s.text(bx + 330, ch.Y(99.95) + 10, t("→ support\n→ hold longs" if k == 0 else "→ idea dead\n→ may flip to\n   resistance\n   (inverse FVG)",
                                "→ แนวรับ\n→ ถือ Long ต่อ" if k == 0 else "→ ไอเดียจบ\n→ อาจกลายเป็น\n   แนวต้าน\n   (Inverse FVG)"), 12, col, weight=700)
    return s.render()


@fig
def ob_orders(lang):
    t = tr(lang)
    s = SVG(960, 460, t("Order block as unfilled orders (illustrative)", "Order block คือคำสั่งที่ยังไม่ได้เติม (ภาพประกอบ)"),
            t("A fund wants to buy 1,000 contracts around 101.8–102.4. Price runs away before it's finished.",
              "กองทุนอยากซื้อ 1,000 สัญญาแถว 101.8–102.4 ราคาวิ่งหนีไปก่อนซื้อครบ"))
    steps = [(C["bear"], t("1 · The last red candle", "1 · แท่งแดงแท่งสุดท้าย"), t("Fund absorbs sellers:\n600 of 1,000 filled", "กองทุนรับแรงขาย:\nเติมได้ 600 จาก 1,000"), 600, 0),
             (C["bull"], t("2 · Displacement + BOS", "2 · แรงส่ง + BOS"), t("Price runs to 106+.\n400 still wanted", "ราคาวิ่งไป 106+\nยังต้องการอีก 400"), 600, 0),
             (C["blue"], t("3 · First return", "3 · กลับมาครั้งแรก"), t("400 resting buys meet\nprice → support", "คำสั่งซื้อ 400 ที่รอ\nเจอราคา → แนวรับ"), 600, 400),
             (C["muted"], t("4 · Mitigated", "4 · ถูกใช้แล้ว (Mitigated)"), t("All 1,000 filled. A 2nd\nreturn finds no buyers", "เติมครบ 1,000 แล้ว กลับมา\nครั้งที่ 2 ไม่มีผู้ซื้อรอ"), 1000, 0)]
    for k, (col, head, body, filled, new) in enumerate(steps):
        x = 28 + k * 230
        s.rect(x, 100, 216, 320, fill=C["panel"], stroke=col, rx=12)
        s.text(x + 108, 130, head, 14, col, "middle", 700)
        s.rect(x + 78, 160, 60, 160, fill="none", stroke=C["border"], rx=4)
        h1 = 160 * min(filled, 1000) / 1000
        s.rect(x + 78, 320 - h1, 60, h1, fill=C["bull"] if k < 3 else C["muted"], opacity=0.6, rx=4)
        if new:
            s.rect(x + 78, 320 - h1 - 160 * new / 1000, 60, 160 * new / 1000, fill=C["blue"], opacity=0.85, rx=4)
        s.text(x + 108, 340, t(f"filled {filled + new:,} / 1,000", f"เติมแล้ว {filled + new:,} / 1,000"), 12, C["text"], "middle", 600)
        s.text(x + 108, 372, body, 12, C["muted"], "middle")
    return s.render()


@fig
def killzones_utc7(lang):
    t = tr(lang)
    s = SVG(960, 470, t("ICT windows in Thailand / Laos time (UTC+7)", "ช่วงเวลาของ ICT ตามเวลาไทย / ลาว (UTC+7)"),
            t("ICT times are New York times, so they shift with US daylight saving: UTC+7 = NY + 11 h (US summer) or + 12 h (US winter).",
              "เวลาของ ICT คือเวลานิวยอร์ก จึงเลื่อนตามเวลาออมแสงสหรัฐ: UTC+7 = NY + 11 ชม. (ฤดูร้อนสหรัฐ) หรือ + 12 ชม. (ฤดูหนาวสหรัฐ)"))
    x0, w = 150, 760
    X = lambda h: x0 + w * ((h - 5) % 24) / 24
    for h in range(5, 30, 2):
        x = X(h % 24) if h < 29 else x0 + w
        s.line(x, 100, x, 330, C["grid"], 1)
        s.text(x, 350, f"{h % 24:02d}", 12, C["muted"], "middle")
    wins = [(t("Asia", "เอเชีย"), 19, 4, C["purple"]), (t("London KZ", "London KZ"), 2, 5, C["teal"]),
            (t("NY AM KZ", "NY AM KZ"), 7, 10, C["amber"]), (t("London close", "London close"), 10, 12, C["blue"])]
    for r, (label, off) in enumerate(((t("US summer\n(Mar–Nov)", "ฤดูร้อนสหรัฐ\n(มี.ค.–พ.ย.)"), 11), (t("US winter\n(Nov–Mar)", "ฤดูหนาวสหรัฐ\n(พ.ย.–มี.ค.)"), 12))):
        y0 = 112 + r * 112
        s.text(28, y0 + 30, label, 13, C["text"], weight=700)
        for k, (name, a, b, col) in enumerate(wins):
            ua, ub = (a + off) % 24, (b + off) % 24
            dur = (b - a) % 24
            y = y0 + k * 25
            xa = X(ua)
            wd = w * dur / 24
            s.rect(xa, y, wd, 21, fill=col, rx=5, opacity=0.85)
            lab = f"{name} {ua:02d}:00–{ub:02d}:00"
            if wd > 200:
                s.text(xa + 8, y + 15, lab, 12, C["white"], weight=700)
            elif xa + wd + 190 < x0 + w:
                s.text(xa + wd + 8, y + 15, lab, 12, col, weight=700)
            else:
                s.text(xa - 8, y + 15, lab, 12, col, "end", 700)
    s.text(28, 390, t("2026: US summer time 8 Mar – 1 Nov · UK summer time 29 Mar – 25 Oct. In the gap weeks (8–29 Mar, 25 Oct – 1 Nov)",
                      "2026: เวลาฤดูร้อนสหรัฐ 8 มี.ค. – 1 พ.ย. · อังกฤษ 29 มี.ค. – 25 ต.ค. ในสัปดาห์ที่ไม่ตรงกัน (8–29 มี.ค., 25 ต.ค. – 1 พ.ย.)"), 12, C["amber"], weight=600)
    s.text(28, 410, t("the London open (08:00 London) is at 15:00 UTC+7, inside the 13:00–16:00 London killzone instead of at its start.",
                      "ลอนดอนเปิด (08:00 เวลาลอนดอน) ตรงกับ 15:00 UTC+7 อยู่กลาง London killzone 13:00–16:00 แทนที่จะอยู่ตอนต้น"), 12, C["amber"], weight=600)
    s.text(28, 440, t("Laos and Thailand don't use daylight saving, so only the markets move.", "ลาวและไทยไม่ใช้เวลาออมแสง มีแต่ตลาดที่เลื่อน"), 12, C["muted"])
    return s.render()


@fig
def model_flow(lang):
    t = tr(lang)
    s = SVG(960, 560, t("The model as a flowchart, including the failure branch", "โมเดลในรูปผังงาน รวมทางแยกเมื่อล้มเหลว"),
            t("Every 'no' means no trade. After entry, every outcome has a pre-written answer.",
              "ทุกคำตอบ 'ไม่' คือไม่เทรด หลังเข้าแล้ว ทุกผลลัพธ์มีคำตอบเขียนไว้ล่วงหน้า"))
    steps = [t("1 Bias\n(2.2)", "1 Bias\n(2.2)"), t("2 Target pool\n(5.1)", "2 เป้าหมาย\n(5.1)"), t("3 Discount\n(5.3)", "3 Discount\n(5.3)"), t("4 Sweep\n(5.2)", "4 กวาด\n(5.2)"),
             t("5 Killzone\n(5.6)", "5 Killzone\n(5.6)"), t("6 MSS\n(5.2)", "6 MSS\n(5.2)"), t("7 FVG / OB\n(5.4–5.5)", "7 FVG / OB\n(5.4–5.5)"), t("8 R:R ≥ 2\n(3.2)", "8 R:R ≥ 2\n(3.2)")]
    for i, name in enumerate(steps):
        x = 28 + i * 114
        s.rect(x, 100, 104, 54, fill=C["panel"], stroke=C["blue"], rx=8)
        s.text(x + 52, 122, name, 12, C["text"], "middle", 700)
        if i < 7:
            s.arrow(x + 104, 127, x + 112, 127, C["bull"], 1.5)
        s.arrow(x + 52, 156, x + 52, 186, C["bear"], 1.5)
        s.text(x + 52, 204, t("no →", "ไม่ →"), 11, C["bear"], "middle", 700)
        s.text(x + 52, 220, t("skip", "ข้าม"), 11, C["bear"], "middle", 700)
    s.text(480, 252, t("all 8 = yes → enter at the FVG CE / OB, stop beyond the sweep, size for 1R", "ครบ 8 ข้อ = ใช่ → เข้าที่ CE ของ FVG / OB  Stop เลยจุดกวาด  ขนาดสำหรับ 1R"), 14, C["bull"], "middle", 700)
    outs = [(C["bull"], t("A · Hits +2R", "A · ถึง +2R"), t("Take half off, stop to\nbreak-even, rest to target.\nExample: +2.31R", "ปิดครึ่ง เลื่อน Stop ไป\nจุดคุ้มทุน ที่เหลือไปเป้า\nตัวอย่าง: +2.31R")),
            (C["amber"], t("B · +2R, then back to entry", "B · +2R แล้วกลับมาจุดเข้า"), t("Half closed at +2R, rest\nstopped at break-even.\nExample: +0.97R", "ปิดครึ่งที่ +2R ที่เหลือ\nโดน Stop ที่จุดคุ้มทุน\nตัวอย่าง: +0.97R")),
            (C["bear"], t("C · Closes below sweep low", "C · ปิดใต้จุดกวาด"), t("Stop hit: −1R. The sweep\nwas a run. No revenge\nre-entry; new setup only.", "โดน Stop: −1R การกวาดคือ\nการวิ่งทะลุ ห้ามเข้าแก้แค้น\nรอ Setup ใหม่เท่านั้น")),
            (C["muted"], t("D · Never fills", "D · ไม่ได้เข้า"), t("Price runs without a\nretrace. Cancel the order;\ndon't chase.", "ราคาวิ่งไปไม่ย่อกลับ\nยกเลิกคำสั่ง\nอย่าไล่ราคา"))]
    for k, (col, head, body) in enumerate(outs):
        x = 28 + k * 230
        s.arrow(480, 266, x + 108, 296, col, 1.4)
        s.rect(x, 300, 216, 170, fill=C["panel"], stroke=col, rx=12)
        s.text(x + 108, 330, head, 14, col, "middle", 700)
        s.text(x + 108, 362, body, 12, C["text"], "middle")
    s.text(480, 510, t("Example numbers from 5.7: account 10,000 USD, 29 units, risk 97.15 USD (≈1R).", "ตัวเลขตัวอย่างจาก 5.7: บัญชี 10,000 ดอลลาร์ 29 หน่วย ความเสี่ยง 97.15 ดอลลาร์ (≈1R)"), 13, C["muted"], "middle")
    s.text(480, 534, t("Expectancy if 40% of trades are A at +2.6R and 60% are C at −1R: 0.4 × 2.6 − 0.6 = +0.44R (illustrative).",
                       "ค่าคาดหวังถ้า 40% เป็นแบบ A ที่ +2.6R และ 60% เป็นแบบ C ที่ −1R: 0.4 × 2.6 − 0.6 = +0.44R (สมมติ)"), 13, C["muted"], "middle")
    return s.render()
