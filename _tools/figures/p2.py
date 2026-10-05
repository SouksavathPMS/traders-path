"""Phase 2 figures: Market Structure."""
from charts import SVG, CandleChart, C, tr, candles_from_path

FIGURES = {}


def fig(fn):
    FIGURES["p2-" + fn.__name__.replace("_", "-")] = fn
    return fn


# ---------------------------------------------------------------- helpers
def walk(pivots, bars, seed=1, vol=0.25, wick=0.4):
    """candles_from_path + make every pivot the true extreme of its neighbourhood.
    Returns (candles, idx) where idx[k] is the candle index of pivot k (idx[0] = 0)."""
    cs = candles_from_path(pivots, bars, seed=seed, vol=vol, wick=wick)
    idx = [0] + [sum(bars[:k]) - 1 for k in range(1, len(pivots))]
    eps = abs(pivots[1] - pivots[0]) * 0.03
    for k in range(1, len(pivots)):
        i, p = idx[k], pivots[k]
        peak = p > pivots[k - 1]
        if k + 1 < len(pivots) and (pivots[k + 1] > p) == peak:
            continue  # trend continues through this pivot: not a turning point
        for j in range(max(0, i - 3), min(len(cs), i + 4)):
            if j == i:
                continue
            o, h, l, c = cs[j]
            if peak:
                o, c = min(o, p - eps), min(c, p - eps)
                h = max(min(h, p - eps), o, c)
            else:
                o, c = max(o, p + eps), max(c, p + eps)
                l = min(max(l, p + eps), o, c)
            cs[j] = [o, h, l, c]
    for j in range(1, len(cs)):  # keep open = previous close after clamping
        cs[j][0] = cs[j - 1][3]
        cs[j][1] = max(cs[j][1], cs[j][0], cs[j][3])
        cs[j][2] = min(cs[j][2], cs[j][0], cs[j][3])
    return cs, idx


def extend(cs, more):
    """Append candles that continue from the last close."""
    more[0][0] = cs[-1][3]
    more[0][1] = max(more[0][1], more[0][0])
    more[0][2] = min(more[0][2], more[0][0])
    return cs + more


def first_close(cs, start, level, up):
    for j in range(start, len(cs)):
        if (up and cs[j][3] > level) or (not up and cs[j][3] < level):
            return j
    return len(cs) - 1


def swing_labels(ch, cs, idx, names, colors, size=13, skip=()):
    for k, name in enumerate(names):
        if not name or k in skip:
            continue
        i = idx[k]
        top = name.endswith("H") or name in ("H",)
        col = colors.get(name, C["text"])
        if top:
            ch.label(i, cs[i][1], name, col, dy=-12, size=size)
        else:
            ch.label(i, cs[i][2], name, col, dy=24, size=size)


def zigzag(ch, cs, idx, pivots, color, k0=0, dash="5 4"):
    pts = []
    for k in range(k0, len(pivots)):
        i = idx[k]
        up = k > 0 and pivots[k] > pivots[k - 1]
        pts.append((i, cs[i][1] if up else cs[i][2]) if k > 0 else (i, pivots[0]))
    ch.path(pts, color, 1.6, dash)


def panel(s, x, y, w, h, title=None, color=C["text"], size=17):
    s.rect(x, y, w, h, fill=C["panel"], stroke=C["border"], rx=12)
    if title:
        s.text(x + 18, y + 30, title, size, color, weight=700)


LBL = {"HH": C["bull"], "HL": C["bull"], "LH": C["bear"], "LL": C["bear"], "H": C["muted"], "L": C["muted"]}


# ---------------------------------------------------------------- 2.1
@fig
def swings(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Structure in four labels: HH · HL · LH · LL", "โครงสร้างใน 4 ป้าย: HH · HL · LH · LL"),
            t("Each new swing is compared with the previous swing of the same kind.",
              "สวิงใหม่แต่ละจุดเทียบกับสวิงก่อนหน้าที่เป็นชนิดเดียวกัน"))
    specs = [
        (t("Uptrend: Higher Highs + Higher Lows", "ขาขึ้น: Higher High + Higher Low"), C["bull"],
         [100, 108, 104, 113, 108.5, 118, 113, 122], ["L", "H", "HL", "HH", "HL", "HH", "HL", "HH"], 3,
         t("Buyers push each high higher and\ndefend each pullback earlier.", "ผู้ซื้อดันจุดสูงขึ้นไปเรื่อย ๆ\nและรับของเร็วขึ้นทุกครั้งที่ย่อ")),
        (t("Downtrend: Lower Highs + Lower Lows", "ขาลง: Lower High + Lower Low"), C["bear"],
         [122, 114, 118, 109, 113.5, 104, 108, 100], ["H", "L", "LH", "LL", "LH", "LL", "LH", "LL"], 4,
         t("Sellers push each low lower and\nsell each bounce earlier.", "ผู้ขายกดจุดต่ำลงไปเรื่อย ๆ\nและขายเร็วขึ้นทุกครั้งที่เด้ง")),
    ]
    for k, (head, col, piv, names, seed, foot) in enumerate(specs):
        x = 28 + k * 460
        panel(s, x, 90, 444, 360, head, col, 16)
        cs, idx = walk(piv, [4, 3, 4, 3, 4, 3, 4], seed=seed)
        ch = CandleChart(s, x + 16, 140, 412, 230, cs, grid=False)
        zigzag(ch, cs, idx, piv, col, k0=1)
        ch.draw()
        names[0] = None  # start candle is not a confirmed swing
        swing_labels(ch, cs, idx, names, LBL, 13)
        s.text(x + 18, 410, foot, 13, C["muted"])
    return s.render()


@fig
def swing_points(lang):
    t = tr(lang)
    s = SVG(960, 470, t("What counts as a swing?", "อะไรนับเป็นสวิง?"),
            t("A swing is a turning point that held. Mark the major ones; ignore the noise inside a leg.",
              "สวิงคือจุดกลับตัวที่ยืนได้ มาร์กเฉพาะสวิงหลัก และเมินสัญญาณรบกวนภายในขา"))
    # left: the fractal rule
    panel(s, 28, 90, 330, 360, t("The 5-candle rule", "กฎ 5 แท่ง"), C["blue"])
    hi = [(100, 102, 99.4, 101.6), (101.6, 103.4, 101.2, 103), (103, 105.5, 102.6, 104), (104, 104.4, 102.2, 102.6),
          (102.6, 103, 100.8, 101.2)]
    ch = CandleChart(s, 50, 140, 130, 120, hi, grid=False)
    ch.draw(highlight={2: C["bear"]})
    ch.hline(105.5, None, C["bear"], 0, 4, "3 3")
    ch.label(2, 105.5, t("Swing high", "Swing High"), C["bear"], dy=-10, size=12)
    lo = [(104, 104.5, 102.4, 102.8), (102.8, 103.2, 101.2, 101.6), (101.6, 102.2, 99, 101.8), (101.8, 103.4, 101.4, 103),
          (103, 104.8, 102.7, 104.4)]
    ch2 = CandleChart(s, 200, 150, 130, 120, lo, grid=False)
    ch2.draw(highlight={2: C["bull"]})
    ch2.hline(99, None, C["bull"], 0, 4, "3 3")
    ch2.label(2, 99, t("Swing low", "Swing Low"), C["bull"], dy=26, size=12)
    s.text(46, 330, t("A swing high is a candle whose high\nis above the 2 highs on each side.\n"
                      "A swing low: low below the 2 lows\non each side. It is only confirmed\nafter the 2 candles on the right close.",
                      "Swing High คือแท่งที่จุดสูงสุด\nสูงกว่าจุดสูงของ 2 แท่งทั้งซ้ายและขวา\n"
                      "Swing Low คือแท่งที่จุดต่ำสุด\nต่ำกว่า 2 แท่งทั้งซ้ายและขวา จะยืนยันได้\nเมื่อ 2 แท่งด้านขวาปิดแล้วเท่านั้น"),
           13, C["text"])
    # right: major vs minor
    panel(s, 374, 90, 558, 360, t("Major swings vs. minor noise", "สวิงหลัก vs. สัญญาณรบกวนย่อย"), C["amber"])
    piv = [100, 106, 104.6, 112, 103.5, 115, 113.4, 121]
    cs, idx = walk(piv, [4, 2, 4, 5, 4, 2, 3], seed=9)
    ch3 = CandleChart(s, 392, 136, 522, 240, cs, grid=False)
    major = [0, 3, 4, 7]
    ch3.path([(idx[0], piv[0])] + [(idx[k], cs[idx[k]][1] if k in (3, 7) else cs[idx[k]][2]) for k in major[1:]],
             C["amber"], 2.2)
    ch3.draw()
    for k in (1, 2, 5, 6):
        i = idx[k]
        up = piv[k] > piv[k - 1]
        ch3.label(i, cs[i][1] if up else cs[i][2], t("minor", "ย่อย"), C["dim"], dy=-10 if up else 22, size=11)
    ch3.label(idx[3], cs[idx[3]][1], t("Major high", "สวิงสูงหลัก"), C["amber"], dy=-12, pill=False, size=13)
    ch3.label(idx[4], cs[idx[4]][2], t("Major low", "สวิงต่ำหลัก"), C["amber"], dy=24, size=13)
    s.text(392, 412, t("Major = the pullback was big enough to matter (it took out a\nprior swing or retraced about a third of the leg). Minor = pause.",
                       "สวิงหลัก = การย่อใหญ่พอจะมีความหมาย (กินสวิงก่อนหน้า\nหรือย่อประมาณ 1 ใน 3 ของขา) สวิงย่อย = แค่หยุดพัก"),
           13, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 2.2
@fig
def market_phases(lang):
    t = tr(lang)
    s = SVG(960, 450, t("Three states of every market", "ตลาดมีได้ 3 สภาวะ"),
            t("Name the state first. It decides which trades are even allowed.",
              "ระบุสภาวะก่อน มันตัดสินว่าเทรดแบบไหนที่ทำได้"))
    specs = [
        (t("Uptrend", "ขาขึ้น"), C["bull"], [100, 107, 103.5, 111, 107.5, 115], [4, 3, 4, 3, 4], 31,
         t("HH + HL\n→ buy pullbacks to the HL", "HH + HL\n→ ซื้อตอนย่อลงมาที่ HL")),
        (t("Range", "ไซด์เวย์ (กรอบ)"), C["amber"], [104, 110.5, 103.6, 110.8, 103.4, 110.2, 106], [3, 4, 4, 4, 4, 2], 32,
         t("Equal highs + equal lows\n→ trade the edges, or wait", "จุดสูงเท่ากัน + จุดต่ำเท่ากัน\n→ เทรดที่ขอบกรอบ หรือรอ")),
        (t("Downtrend", "ขาลง"), C["bear"], [115, 108, 111.5, 104, 107.5, 100], [4, 3, 4, 3, 4], 33,
         t("LH + LL\n→ sell rallies to the LH", "LH + LL\n→ ขายตอนเด้งขึ้นไปที่ LH")),
    ]
    for k, (head, col, piv, bars, seed, foot) in enumerate(specs):
        x = 28 + k * 308
        panel(s, x, 90, 290, 340, head, col, 18)
        cs, idx = walk(piv, bars, seed=seed)
        ch = CandleChart(s, x + 14, 134, 262, 210, cs, grid=False)
        if k == 1:
            ch.zone(110, 111.2, C["bear"], opacity=0.15)
            ch.zone(102.9, 104.1, C["bull"], opacity=0.15)
        ch.draw()
        s.text(x + 18, 384, foot, 14, C["text"])
    return s.render()


@fig
def cycle(lang):
    t = tr(lang)
    s = SVG(960, 520, t("The market cycle: ranges build the trends", "วัฏจักรตลาด: กรอบราคาสร้างเทรนด์"),
            t("Accumulation → Markup → Distribution → Markdown (Wyckoff)", "สะสม → ขาขึ้น → กระจาย → ขาลง (Wyckoff)"))
    piv = [104, 100.5, 106, 101, 105.8, 100.8, 106.5,
           117, 112, 126, 121, 131,
           125.5, 131.5, 125, 130.8, 124.5,
           113, 117, 105, 108, 99]
    bars = [3] * 6 + [5, 3, 5, 3, 5] + [3] * 5 + [5, 3, 5, 3, 4]
    cs, idx = walk(piv, bars, seed=41)
    panel(s, 28, 90, 904, 410)
    ch = CandleChart(s, 40, 150, 880, 260, cs)
    phases = [
        (0, 6, C["blue"], t("ACCUMULATION", "สะสม (Accumulation)"), t("Big buyers quietly\nabsorb supply", "รายใหญ่ทยอยเก็บของ\nอย่างเงียบ ๆ")),
        (6, 11, C["bull"], t("MARKUP", "ขาขึ้น (Markup)"), t("Supply gone → trend up\nHH + HL", "ของหมด → เทรนด์ขึ้น\nHH + HL")),
        (11, 16, C["amber"], t("DISTRIBUTION", "กระจาย (Distribution)"), t("Big sellers unload\ninto late buyers", "รายใหญ่ทยอยขาย\nให้คนที่มาซื้อทีหลัง")),
        (16, 21, C["bear"], t("MARKDOWN", "ขาลง (Markdown)"), t("Demand gone → trend down\nLH + LL", "แรงซื้อหมด → เทรนด์ลง\nLH + LL")),
    ]
    for a, b, col, name, desc in phases:
        i0, i1 = idx[a] if a else 0, idx[b]
        x0, x1 = ch.X(i0) - ch.step / 2, ch.X(i1) + ch.step / 2
        s.rect(x0, 110, x1 - x0, 310, fill=col, opacity=0.07, rx=4)
        s.text((x0 + x1) / 2, 132, name, 14, col, "middle", 700)
        s.text((x0 + x1) / 2, 446, desc, 13, C["muted"], "middle")
    ch.draw()
    return s.render()


# ---------------------------------------------------------------- 2.3
@fig
def bos_choch(lang):
    t = tr(lang)
    s = SVG(960, 520, t("BOS continues the trend. CHoCH warns it may be over.",
                        "BOS = เทรนด์ไปต่อ  CHoCH = สัญญาณเตือนว่าเทรนด์อาจจบ"),
            t("A break is a candle CLOSE beyond the swing that matters.",
              "การเบรกคือ ราคาปิด ของแท่งเทียนที่ทะลุสวิงที่สำคัญ"))
    piv = [100, 108, 104, 113, 109, 118, 112.5, 116, 107, 111, 102]
    bars = [4, 3, 4, 3, 4, 3, 3, 5, 3, 5]
    cs, idx = walk(piv, bars, seed=51)
    panel(s, 28, 90, 904, 410)
    ch = CandleChart(s, 40, 120, 880, 330, cs)
    breaks = [
        (1, True, "BOS", C["bull"]),
        (3, True, "BOS", C["bull"]),
        (6, False, "CHoCH", C["purple"]),
        (8, False, "BOS", C["bear"]),
    ]
    for k, up, name, col in breaks:
        i = idx[k]
        lvl = cs[i][1] if up else cs[i][2]
        j = first_close(cs, idx[k + 1] + 1, lvl, up)
        ch.hline(lvl, None, col, i, j, "6 4")
        ch.label((i + j) / 2, lvl, name, col, dy=-8 if up else 20, size=14)
        ch.s.circle(ch.X(j), ch.Y(cs[j][3]), 5, col)
    ch.draw()
    names = ["", "H", "HL", "HH", "HL", "HH", "HL", "LH", "LL", "LH", "LL"]
    swing_labels(ch, cs, idx, names, LBL, 12, skip=(0,))
    s.text(60, 478, t("● = the candle close that confirms the break", "● = ราคาปิดที่ยืนยันการเบรก"), 13, C["muted"])
    s.text(900, 478, t("First break AGAINST the trend = CHoCH. Breaks WITH the trend = BOS.",
                       "เบรกครั้งแรกที่ สวน เทรนด์ = CHoCH  เบรกที่ ตาม เทรนด์ = BOS"), 13, C["purple"], "end", 600)
    return s.render()


@fig
def break_quality(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Real break or fake break? Watch the close.", "เบรกจริงหรือหลอก? ดูที่ราคาปิด"),
            t("Wicks probe. Closes commit.", "ไส้เทียนแค่หยั่งเชิง ราคาปิดคือการยืนยัน"))
    base, _ = walk([104, 109.4, 105.8, 109.6, 106.4], [4, 3, 3, 3], seed=61)
    for k in range(2):
        x = 28 + k * 460
        good = k == 0
        col = C["bull"] if good else C["bear"]
        panel(s, x, 90, 444, 360, t("✓ Acceptance: body closes above", "✓ ยอมรับ: ตัวแท่งปิดเหนือแนว") if good
              else t("✗ Rejection: wick above, close back inside", "✗ ปฏิเสธ: ไส้ทะลุ แต่ปิดกลับเข้ากรอบ"), col, 16)
        cs = [c[:] for c in base]
        o = cs[-1][3]
        if good:
            cs = extend(cs, [[o, 112.6, o - 0.3, 112.2]])
            more, _ = walk([112.2, 113.6, 110.6, 116.5], [2, 3, 4], seed=62)
        else:
            cs = extend(cs, [[o, 111.8, o - 0.3, 108.4]])
            more, _ = walk([108.4, 109.2, 104.5, 105.5, 101.5], [1, 3, 2, 3], seed=63)
        cs = extend(cs, more[1:] if len(more) > 1 else more)
        ch = CandleChart(s, x + 16, 140, 412, 220, cs, pmin=99.5, pmax=118, grid=False)
        ch.hline(110, t("Resistance", "แนวต้าน"), C["amber"], side="left")
        ch.draw(highlight={len(base): col})
        s.text(x + 18, 400, t("Buyers accepted higher prices.\nThe level is broken → look for a retest.",
                              "ผู้ซื้อยอมรับราคาที่สูงขึ้น\nแนวถูกเบรกแล้ว → รอดูการทดสอบซ้ำ") if good else
               t("Buyers who chased the breakout are trapped.\nOften a liquidity grab (Phase 5).",
                 "คนที่ไล่ซื้อตอนเบรกติดดอย\nมักเป็นการกวาดสภาพคล่อง (เฟส 5)"), 13, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 2.4
@fig
def role_reversal(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Role reversal: broken resistance becomes support", "การสลับบทบาท: แนวต้านที่ถูกเบรกกลายเป็นแนวรับ"),
            t("The same price, a different job — because the people trapped there now act differently.",
              "ราคาเดิม หน้าที่ใหม่ เพราะคนที่ติดอยู่ตรงนั้นเปลี่ยนพฤติกรรม"))
    piv = [101, 109.8, 103, 110.1, 104, 117, 110.4, 121]
    bars = [4, 4, 4, 4, 6, 4, 4]
    cs, idx = walk(piv, bars, seed=71)
    panel(s, 28, 90, 904, 390)
    ch = CandleChart(s, 40, 120, 700, 330, cs, right_space=0)
    brk = first_close(cs, idx[4], 110.6, True)
    ch.zone(109.2, 110.6, C["bear"], t("Resistance", "แนวต้าน"), i0=0, i1=brk - 1, opacity=0.18)
    ch.zone(109.2, 110.6, C["bull"], t("Support", "แนวรับ"), i0=brk, opacity=0.18, label_side="right", label_pos="below")
    ch.draw(highlight={brk: C["bull"], idx[6]: C["blue"]})
    ch.label(idx[1], cs[idx[1]][1], "1", C["bear"], dy=-12)
    ch.label(idx[3], cs[idx[3]][1], "2", C["bear"], dy=-12)
    ch.label(brk, cs[brk][1], t("Break", "เบรก"), C["bull"], dy=-12)
    ch.label(idx[6], cs[idx[6]][2], t("Retest holds", "ทดสอบซ้ำแล้วยืนได้"), C["blue"], dy=28)
    cx = 760
    s.card(cx, 110, 160, 110, t("Before", "ก่อนเบรก"), t("Sellers defend.\nBuyers who\nbought here: stuck.", "ผู้ขายป้องกัน\nคนที่ซื้อตรงนี้\nติดอยู่"),
           C["bear"], 15, 12)
    s.card(cx, 232, 160, 110, t("After", "หลังเบรก"), t("Shorts must buy\nback; missed buyers\nwant in at the level.", "คน Short ต้อง\nซื้อคืน คนที่ตกรถ\nอยากเข้าที่ระดับนี้"),
           C["bull"], 15, 12)
    s.card(cx, 354, 160, 110, t("Trade", "เทรด"), t("Buy the retest,\nstop below\nthe zone.", "ซื้อตอนทดสอบซ้ำ\nStop ใต้โซน"),
           C["blue"], 15, 12)
    return s.render()


@fig
def level_strength(lang):
    t = tr(lang)
    s = SVG(960, 480, t("Draw zones, not lines — and grade them", "ขีดเป็นโซน ไม่ใช่เส้น — แล้วให้คะแนน"),
            t("A level is an area where orders sat. Price rarely turns at the exact same tick.",
              "ระดับราคาคือพื้นที่ที่มีคำสั่งรออยู่ ราคาแทบไม่เคยกลับตัวที่จุดเดิมเป๊ะ"))
    panel(s, 28, 90, 420, 370, t("Zone = wicks to bodies", "โซน = จากปลายไส้ถึงตัวแท่ง"), C["blue"])
    piv = [104, 98.6, 105, 98.9, 104.6, 98.3, 103.5]
    cs, idx = walk(piv, [4, 4, 4, 4, 4, 3], seed=81)
    ch = CandleChart(s, 44, 140, 388, 230, cs, grid=False)
    top = max(min(cs[idx[k]][0], cs[idx[k]][3]) for k in (1, 3, 5))
    ch.zone(min(piv[1], piv[3], piv[5]) - 0.1, top, C["blue"], opacity=0.2)
    ch.hline(piv[3], None, C["dim"], dash="2 4")
    ch.draw()
    for n, k in enumerate((1, 3, 5), 1):
        ch.label(idx[k], cs[idx[k]][2], str(n), C["blue"], dy=24)
    s.text(46, 400, t("A single line (dotted) gets pierced every time.\nThe zone holds all three touches.",
                      "เส้นเดียว (เส้นประ) ถูกแทงทะลุทุกครั้ง\nแต่โซนรองรับได้ครบทั้ง 3 ครั้ง"), 13, C["muted"])
    items = [
        (C["purple"], t("Higher timeframe", "ไทม์เฟรมใหญ่"), t("Weekly/daily levels beat 5-minute levels.", "ระดับรายสัปดาห์/รายวัน ชนะระดับ 5 นาที")),
        (C["bull"], t("Clean, strong reaction", "ปฏิกิริยาแรงและชัด"), t("Price left fast and far = many orders there.", "ราคาออกไปเร็วและไกล = คำสั่งรออยู่เยอะ")),
        (C["teal"], t("Recency", "ความใหม่"), t("Recent levels still hold live orders.", "ระดับล่าสุดยังมีคำสั่งรออยู่จริง")),
        (C["amber"], t("Confluence", "จุดบรรจบ"), t("Round number, prior day high/low, role reversal.", "ตัวเลขกลม จุดสูง/ต่ำเมื่อวาน การสลับบทบาท")),
        (C["bear"], t("Number of tests", "จำนวนครั้งที่ทดสอบ"), t("Each test uses up orders. 3rd–4th test → weaker.", "ทดสอบแต่ละครั้งใช้คำสั่งไป ครั้งที่ 3–4 → อ่อนลง")),
    ]
    for k, (col, head, body) in enumerate(items):
        y = 90 + k * 76
        s.rect(468, y, 464, 66, fill=C["panel"], stroke=C["border"], rx=10)
        s.rect(468, y, 5, 66, fill=col, rx=2)
        s.text(488, y + 26, head, 15, col, weight=700)
        s.text(488, y + 50, body, 13, C["text"])
    return s.render()


# ---------------------------------------------------------------- 2.5
def _leg(start, n, step, seed=0):
    out, p = [], start
    for k in range(n):
        o = p
        c = p + step * (1 + 0.15 * ((k + seed) % 3 - 1))
        w = abs(step) * 0.18
        out.append([o, max(o, c) + w, min(o, c) - w, c])
        p = c
    return out


def _base(price, n, amp=0.35):
    out, p = [], price
    shape = [(-0.25, 0.1), (0.15, -0.1), (-0.05, 0.12), (0.1, -0.05)]
    for k in range(n):
        o = p
        c = price + shape[k % 4][0] * amp * 2
        out.append([o, max(o, c) + amp * 0.9, min(o, c) - amp * 0.9, c])
        p = c
    return out


def _sd_pattern(leg_in, leg_out):
    start = 104 - leg_in * 5.5
    cs = _leg(start, 4, leg_in * 1.4, 1)
    nb = len(cs)
    cs += _base(cs[-1][3], 3)
    ne = len(cs)
    cs += _leg(cs[-1][3], 4, leg_out * 1.7, 2)
    return cs, nb, ne


@fig
def sd_patterns(lang):
    t = tr(lang)
    s = SVG(960, 620, t("Supply & demand: a base, then an explosive departure", "Supply & Demand: ฐานราคา ตามด้วยการพุ่งออกอย่างแรง"),
            t("The zone is the base. The strong move away proves orders were left there.",
              "โซนคือฐานราคา การพุ่งออกอย่างแรงพิสูจน์ว่ายังมีคำสั่งค้างอยู่ตรงนั้น"))
    specs = [
        (1, 1, "Rally-Base-Rally (RBR)", t("Demand · continuation", "Demand · ไปต่อ"), C["bull"]),
        (-1, 1, "Drop-Base-Rally (DBR)", t("Demand · reversal", "Demand · กลับตัว"), C["bull"]),
        (1, -1, "Rally-Base-Drop (RBD)", t("Supply · reversal", "Supply · กลับตัว"), C["bear"]),
        (-1, -1, "Drop-Base-Drop (DBD)", t("Supply · continuation", "Supply · ไปต่อ"), C["bear"]),
    ]
    for k, (a, b, name, kind, col) in enumerate(specs):
        x = 28 + (k % 2) * 460
        y = 90 + (k // 2) * 262
        panel(s, x, y, 444, 248)
        s.text(x + 18, y + 30, name, 16, col, weight=700)
        s.text(x + 426, y + 30, kind, 14, C["muted"], "end", 600)
        cs, nb, ne = _sd_pattern(a, b)
        ch = CandleChart(s, x + 40, y + 44, 260, 190, cs, grid=False)
        base = cs[nb:ne]
        if b > 0:  # demand: proximal = top of base bodies, distal = lowest wick
            prox, dist = max(max(c[0], c[3]) for c in base), min(c[2] for c in base)
        else:
            prox, dist = min(min(c[0], c[3]) for c in base), max(c[1] for c in base)
        ch.zone(prox, dist, col, i0=nb, opacity=0.2)
        ch.draw()
        lx = x + 316
        s.text(lx, y + 92, t("leg-in", "ขาเข้า"), 13, C["muted"], weight=600)
        s.text(lx, y + 92 + 22, "→ " + t("base", "ฐาน"), 13, col, weight=700)
        s.text(lx, y + 92 + 44, "→ " + t("leg-out", "ขาออก"), 13, C["muted"], weight=600)
        s.text(lx, y + 180, t("Zone = the base\n(1–3 small candles)", "โซน = ฐานราคา\n(แท่งเล็ก 1–3 แท่ง)"), 12, C["dim"])
    return s.render()


@fig
def sd_zone(lang):
    t = tr(lang)
    s = SVG(960, 520, t("Anatomy of a demand-zone trade", "กายวิภาคของการเทรดที่โซน Demand"),
            t("Fresh zone + strong departure + BOS = a zone worth trading.",
              "โซนใหม่ + พุ่งออกแรง + มี BOS = โซนที่น่าเทรด"))
    leg_in, _ = walk([121, 112, 115.2, 105], [5, 3, 5], seed=91)
    cs = leg_in + []
    nb = len(cs)
    cs = extend(cs, _base(cs[-1][3], 3, 0.8))
    ne = len(cs)
    cs = extend(cs, _leg(cs[-1][3], 5, 2.3, 1))
    pull, _ = walk([cs[-1][3], 117.6, 113.4, 115, 106.4], [1, 3, 2, 3], seed=92)
    cs = extend(cs, pull[1:])
    ent_i = len(cs) - 1
    rally, _ = walk([cs[-1][3], 112, 110.2, 121.5], [3, 2, 5], seed=93)
    cs = extend(cs, rally[1:])
    base = cs[nb:ne]
    prox = max(max(c[0], c[3]) for c in base)
    dist = min(c[2] for c in base)
    cs[ent_i][2] = min(cs[ent_i][2], prox - 0.2)
    panel(s, 28, 90, 904, 410)
    ch = CandleChart(s, 40, 115, 700, 360, cs)
    ch.zone(prox, dist, C["bull"], t("Demand zone (base)", "โซน Demand (ฐาน)"), i0=nb, opacity=0.18, label_pos="below")
    ch.hline(prox, None, C["bull"], nb, None, "3 3")
    ch.hline(dist, None, C["bull"], nb, None, "3 3")
    lh = 115.2
    j = first_close(cs, ne, lh, True)
    ch.hline(lh, "BOS", C["purple"], 5, j, "6 4", side="left", size=13)
    stop = dist - 0.8
    ch.hline(stop, None, C["bear"], ent_i, None, "4 3")
    ch.hline(121, None, C["dim"], 0, None, "2 4")
    ch.draw(highlight={ent_i: C["blue"]})
    ch.label(ent_i, cs[ent_i][1], t("1st return", "กลับมาครั้งแรก"), C["blue"], dy=-14)
    notes = [
        (C["text"], t("Target", "เป้าหมาย"), t("opposing supply / prior high", "Supply ฝั่งตรงข้าม / จุดสูงเดิม"), 121),
        (C["bull"], t("Proximal line = entry", "เส้น Proximal = จุดเข้า"), t("top of the base bodies", "ขอบบนของตัวแท่งในฐาน"), prox),
        (C["bull"], t("Distal line", "เส้น Distal"), t("lowest wick of the base", "ปลายไส้ต่ำสุดของฐาน"), dist),
        (C["bear"], t("Stop", "Stop"), t("a little beyond distal", "เลยเส้น Distal เล็กน้อย"), stop),
    ]
    ys = []
    for _, _, _, p in notes:
        y = ch.Y(p) + 5
        ys.append(max(y, ys[-1] + 44) if ys else y)
    shift = max(0, ys[-1] - 470)
    ys = [y - shift if k else y for k, y in enumerate(ys)]
    for k in range(2, 0, -1):
        ys[k] = min(ys[k], ys[k + 1] - 44)
    for (col, head, body, p), y in zip(notes, ys):
        s.line(748, ch.Y(p), 756, y - 5, col, 1.2)
        s.text(762, y, head, 14, col, weight=700)
        s.text(760, y + 20, body, 12, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 2.6
@fig
def mtf(lang):
    t = tr(lang)
    s = SVG(960, 520, t("Multi-timeframe structure: the LTF downtrend is the HTF pullback",
                        "โครงสร้างหลายไทม์เฟรม: ขาลงบน LTF คือการย่อของ HTF"),
            t("Bias from the higher timeframe. Timing from a lower-timeframe CHoCH inside the HTF zone.",
              "ทิศทางจากไทม์เฟรมใหญ่ จังหวะจาก CHoCH บนไทม์เฟรมเล็กภายในโซนของ HTF"))
    # left: HTF
    panel(s, 28, 90, 400, 410, t("Daily — bias: LONG", "รายวัน — ทิศทาง: ซื้อ"), C["purple"])
    piv = [100, 120, 111, 131, 122.5]
    cs, idx = walk(piv, [7, 4, 7, 4], seed=21)
    ch = CandleChart(s, 44, 140, 368, 280, cs, grid=False)
    ch.zone(121.5, 124, C["blue"], t("Demand", "Demand"), i0=10, opacity=0.2, label_pos="below")
    ch.draw()
    swing_labels(ch, cs, idx, ["", "HH", "HL", "HH", ""], LBL, 12)
    x0 = ch.X(idx[3]) - 8
    s.rect(x0, ch.Y(131) - 26, ch.X(len(cs) - 1) + 10 - x0, ch.Y(121) - ch.Y(131) + 26, stroke=C["amber"], sw=1.8, rx=6, dash="5 4")
    s.text(44, 460, t("HH + HL, now pulling back into demand.\nOnly longs are allowed.", "HH + HL กำลังย่อลงมาที่ Demand\nอนุญาตเฉพาะฝั่งซื้อ"), 13, C["muted"])
    s.arrow(432, 200, 456, 200, C["amber"], 2.5)
    s.text(444, 186, t("zoom", "ซูม"), 12, C["amber"], "middle", 700)
    # right: LTF
    panel(s, 462, 90, 470, 410, t("1H — the pullback, in detail", "1H — การย่อ แบบละเอียด"), C["blue"])
    piv2 = [131, 127, 129.2, 124.6, 126.6, 122.2, 125.9, 123.6, 130]
    cs2, idx2 = walk(piv2, [3, 3, 4, 3, 4, 4, 3, 5], seed=101)
    ch2 = CandleChart(s, 478, 140, 438, 280, cs2, grid=False)
    ch2.zone(121.5, 124, C["blue"], t("Daily demand", "Demand รายวัน"), opacity=0.16, label_side="left", label_pos="below")
    lvl = cs2[idx2[4]][1]
    j = first_close(cs2, idx2[5] + 1, lvl, True)
    ch2.hline(lvl, None, C["purple"], idx2[4], j, "6 4")
    ch2.label((idx2[4] + j) / 2 + 0.5, lvl, "CHoCH", C["purple"], dy=-8, size=13)
    ch2.draw(highlight={idx2[7]: C["bull"]})
    swing_labels(ch2, cs2, idx2, ["", "", "LH", "LL", "LH", "LL", "", "HL", ""], LBL, 12)
    ch2.label(idx2[7], cs2[idx2[7]][2], t("entry on HL", "เข้าที่ HL"), C["bull"], dy=42, size=12)
    s.text(478, 460, t("LH + LL = a small downtrend (the daily pullback).\nIt reaches daily demand, then CHoCH up → buy the HL.",
                       "LH + LL = ขาลงเล็ก ๆ (คือการย่อของกราฟรายวัน)\nถึง Demand รายวัน แล้วเกิด CHoCH ขึ้น → ซื้อที่ HL"), 13, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 2.7
@fig
def summary(lang):
    t = tr(lang)
    s = SVG(960, 560, t("Phase 2 on one page", "สรุปเฟส 2 ในหน้าเดียว"))
    cx, cy = 480, 310
    nodes = [
        (170, 140, C["purple"], t("2.1 Swings", "2.1 สวิง"), t("Label HH · HL · LH · LL.\nMajor swings only.", "ติดป้าย HH · HL · LH · LL\nเฉพาะสวิงหลัก")),
        (790, 140, C["blue"], t("2.2 Trend / Range", "2.2 เทรนด์ / กรอบ"), t("Name the state first.\nRanges build trends.", "ระบุสภาวะก่อน\nกรอบราคาสร้างเทรนด์")),
        (150, 320, C["bull"], t("2.3 BOS / CHoCH", "2.3 BOS / CHoCH"), t("BOS = continue.\nCHoCH = warning. Close only.", "BOS = ไปต่อ\nCHoCH = เตือน  นับที่ราคาปิด")),
        (810, 320, C["amber"], t("2.4 S/R", "2.4 แนวรับ/แนวต้าน"), t("Zones, not lines.\nBroken levels flip roles.", "โซน ไม่ใช่เส้น\nแนวที่ถูกเบรกสลับบทบาท")),
        (250, 480, C["teal"], t("2.5 Supply & Demand", "2.5 Supply & Demand"), t("Base + explosive departure.\nFresh zones are best.", "ฐาน + พุ่งออกแรง\nโซนใหม่ดีที่สุด")),
        (710, 480, C["pink"], t("2.6 Multi-timeframe", "2.6 หลายไทม์เฟรม"), t("HTF bias + zone →\nLTF CHoCH = entry.", "HTF ทิศทาง + โซน →\nLTF CHoCH = จุดเข้า")),
    ]
    for x, y, col, head, body in nodes:
        s.line(cx, cy, x, y, col, 2, opacity=0.5)
    s.circle(cx, cy, 74, C["panel"], C["text"], 2)
    s.text(cx, cy - 4, t("PHASE 2", "เฟส 2"), 20, C["text"], "middle", 700)
    s.text(cx, cy + 20, t("Market Structure", "โครงสร้างตลาด"), 14, C["muted"], "middle")
    for x, y, col, head, body in nodes:
        s.rect(x - 130, y - 42, 260, 92, fill=C["panel"], stroke=col, rx=12)
        s.text(x, y - 14, head, 17, col, "middle", 700)
        s.text(x, y + 10, body, 13, C["text"], "middle")
    return s.render()


# ================================================================ v2 additions (Oct 2026)
@fig
def protected_low(lang):
    t = tr(lang)
    s = SVG(960, 500, t("The protected low moves up with every BOS", "Protected low ขยับขึ้นทุกครั้งที่เกิด BOS"),
            t("Illustrative uptrend. The stop trails to each new protected HL; a CLOSE below it is the CHoCH.",
              "เทรนด์ขาขึ้นตัวอย่าง Stop เลื่อนตาม Protected HL ใหม่แต่ละจุด การ ปิด ใต้จุดนั้นคือ CHoCH"))
    piv = [100, 108, 104, 114, 109, 120, 111.5, 116, 105.5]
    cs, idx = walk(piv, [5, 3, 5, 3, 5, 3, 3, 5], seed=23)
    panel(s, 28, 90, 904, 390)
    ch = CandleChart(s, 40, 110, 880, 350, cs, pmin=97, pmax=123)
    ch.hline(104, t("protected HL 104", "Protected HL 104"), C["muted"], idx[2], idx[5], "5 4", side="right", size=11)
    ch.hline(109, None, C["amber"], idx[4], None, "5 4")
    s.text(ch.X(idx[4]) - 6, ch.Y(109) + 18, t("protected HL 109", "Protected HL 109"), 11, C["amber"], "end", 600)
    ch.draw()
    for k in (1, 3, 5):
        ch.label(idx[k], cs[idx[k]][1], f"BOS {piv[k]:g}", C["bull"], dy=-10, size=12)
    ch.label(idx[6], cs[idx[6]][2], t("111.5 holds", "111.5 ยืนได้"), C["muted"], dy=22, size=11)
    ch.label(idx[7], cs[idx[7]][1], t("116 = lower high", "116 = Lower high"), C["amber"], dy=-10, size=12)
    j = first_close(cs, idx[7], 109, False)
    ch.label(j, cs[j][2], t("close < 109 → CHoCH", "ปิด < 109 → CHoCH"), C["bear"], dy=24, anchor="end", size=12)
    return s.render()


@fig
def zone_grade(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Grading a demand zone: a 6-point scorecard", "ให้คะแนนโซน Demand: ตาราง 6 ข้อ"),
            t("Example from the lesson: base 104.4–105.8, leg-out through 115.2 (BOS), first return.", "ตัวอย่างจากบทเรียน: ฐาน 104.4–105.8 ขาออกทะลุ 115.2 (BOS) กลับมาครั้งแรก"))
    rows = [(t("Departure", "การออกจากฐาน"), t("big bodies, left fast", "แท่งใหญ่ ออกเร็ว"), True),
            (t("Time in base", "เวลาในฐาน"), t("3 candles", "3 แท่ง"), True),
            (t("Freshness", "ความสด"), t("1st return", "กลับมาครั้งแรก"), True),
            (t("Structure", "โครงสร้าง"), t("leg-out broke 115.2 (BOS)", "ขาออกทะลุ 115.2 (BOS)"), True),
            (t("HTF trend", "เทรนด์ HTF"), t("daily trend still down", "เทรนด์รายวันยังเป็นขาลง"), False),
            (t("Room", "ระยะ"), t("5.4R to 117.6", "5.4R ถึง 117.6"), True)]
    for k, (a, b, ok) in enumerate(rows):
        y = 100 + k * 50
        col = C["bull"] if ok else C["bear"]
        s.rect(28, y, 600, 42, fill=C["panel"], stroke=C["border"], rx=8)
        s.text(48, y + 27, a, 15, C["text"], weight=700)
        s.text(260, y + 27, b, 13, C["muted"])
        s.text(600, y + 28, "✓" if ok else "✗", 20, col, "end", 800)
    s.rect(660, 100, 272, 292, fill=C["panel"], stroke=C["amber"], rx=12)
    s.text(796, 150, t("Score", "คะแนน"), 16, C["muted"], "middle", 700)
    s.text(796, 220, "5 / 6", 48, C["amber"], "middle", 800)
    s.text(796, 270, t("Tradable, but against\nthe HTF trend:", "เทรดได้ แต่สวนเทรนด์ HTF:"), 13, C["text"], "middle")
    s.text(796, 320, t("wait for an LTF CHoCH,\nsize normally", "รอ CHoCH บน LTF\nใช้ขนาดปกติ"), 13, C["amber"], "middle", 700)
    s.text(28, 430, t("Rule: skip any zone that fails departure, freshness or trend unless another strong factor compensates.",
                      "กฎ: ข้ามโซนที่ไม่ผ่านการออกจากฐาน ความสด หรือเทรนด์ เว้นแต่มีปัจจัยแข็งแรงอื่นชดเชย"), 13, C["muted"])
    return s.render()


# ---------------------------------------------------------------- v2 additions (B9b)
FRACTAL_CS = [[100.0, 101.0, 99.4, 100.6], [100.6, 102.5, 100.3, 102.2], [102.2, 104.0, 101.8, 103.4],
              [103.4, 103.6, 101.6, 101.9], [101.9, 102.0, 100.2, 100.8], [100.8, 103.5, 100.6, 103.2],
              [103.2, 105.5, 103.0, 105.1], [105.1, 105.2, 103.4, 103.7], [103.7, 104.0, 102.6, 103.0],
              [103.0, 106.2, 102.9, 105.9], [105.9, 106.0, 104.9, 105.2]]


def fractals(cs, n=2):
    """Return (confirmed_highs, confirmed_lows, possible_highs, possible_lows) as candle indices."""
    hi, lo, phi, plo = [], [], [], []
    for i in range(n, len(cs)):
        left = cs[i - n:i]
        right = cs[i + 1:i + 1 + n]
        if all(cs[i][1] > c[1] for c in left + right):
            (hi if len(right) == n else phi).append(i)
        if all(cs[i][2] < c[2] for c in left + right):
            (lo if len(right) == n else plo).append(i)
    return hi, lo, phi, plo


@fig
def fractal_rule(lang):
    t = tr(lang)
    s = SVG(960, 470, t("The 5-candle rule: when is a swing confirmed?", "กฎ 5 แท่ง: สวิงยืนยันเมื่อไหร่?"),
            t("A swing high is above the 2 candles on each side. It is confirmed only when the 2 candles on its right have closed.",
              "จุดสวิงสูงต้องสูงกว่า 2 แท่งทั้งสองข้าง และยืนยันเมื่อ 2 แท่งด้านขวาปิดแล้วเท่านั้น"))
    cs = FRACTAL_CS
    panel(s, 28, 90, 600, 360)
    ch = CandleChart(s, 50, 120, 560, 300, cs, pmin=98.8, pmax=107.4)
    hi, lo, phi, _ = fractals(cs)
    ch.draw(highlight={phi[0]: C["amber"]})
    prev_h = prev_l = None
    for i in hi:
        name = "H" if prev_h is None else ("HH" if cs[i][1] > prev_h else "LH")
        ch.label(i, cs[i][1], f"{name} {cs[i][1]:g}", LBL[name], dy=-12, size=12)
        prev_h = cs[i][1]
    for i in lo:
        name = "L" if prev_l is None else ("HL" if cs[i][2] > prev_l else "LL")
        ch.label(i, cs[i][2], f"{name} {cs[i][2]:g}", LBL[name], dy=24, size=12)
        prev_l = cs[i][2]
    i = phi[0]
    ch.label(i, cs[i][1], t("possible", "อาจเป็น"), C["amber"], dy=-12, size=12)
    for j in (i - 2, i - 1, i + 1):
        ch.label(j, cs[j][1], "✓", C["muted"], dy=-12, size=11)
    ch.label(i + 1.6, cs[i][1], "?", C["amber"], dy=-12, size=14)
    s.card(650, 90, 282, 360, t("Reading the chart", "อ่านกราฟนี้"),
           t("Confirmed swing highs:\n   104 → 105.5 = HH\nConfirmed swing lows:\n   100.2 → 102.6 = HL\n→ HH + HL = uptrend\n \n106.2 is only POSSIBLE:\n1 candle has closed on its\nright; it needs 2.",
             "จุดสวิงสูงที่ยืนยันแล้ว:\n   104 → 105.5 = HH\nจุดสวิงต่ำที่ยืนยันแล้ว:\n   100.2 → 102.6 = HL\n→ HH + HL = ขาขึ้น\n \n106.2 เป็นแค่ 'อาจเป็น':\nด้านขวาปิดแล้ว 1 แท่ง\nต้องมี 2 แท่ง"),
           C["amber"], 16, 15)
    return s.render()


@fig
def trend_health(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Healthy or tired? Compare pullbacks with impulses", "แข็งแรงหรือเหนื่อย? เทียบการย่อกับแรงส่ง"),
            t("Pullback ÷ impulse before it. Rising ratios = the trend is tiring (illustrative legs).",
              "การย่อ ÷ แรงส่งก่อนหน้า อัตราส่วนที่เพิ่มขึ้น = เทรนด์กำลังเหนื่อย (ขาราคาตัวอย่าง)"))
    sets = [(t("Healthy trend", "เทรนด์แข็งแรง"), [8, -3, 9, -3, 8, -2.5], C["bull"]),
            (t("Tired trend", "เทรนด์เหนื่อย"), [8, -3, 5, -4, 3, -3], C["amber"])]
    for k, (name, legs, col) in enumerate(sets):
        x0 = 28 + k * 462
        panel(s, x0, 90, 442, 360, name, col)
        pts, p = [100], 100
        for d in legs:
            p += d
            pts.append(p)
        X = lambda i: x0 + 40 + i * 58
        Y = lambda v: 330 - (v - 100) * 10
        s.polyline([(X(i), Y(v)) for i, v in enumerate(pts)], col, 2.5)
        for i, v in enumerate(pts[1:], 1):
            s.circle(X(i), Y(v), 4, col)
            d = legs[i - 1]
            mx, my = (X(i) + X(i - 1)) / 2, (Y(v) + Y(pts[i - 1])) / 2
            s.text(mx - 12 if d > 0 else mx + 4, my + (0 if d > 0 else -10), f"{d:+g}", 12,
                   C["text"] if d > 0 else C["bear"], "end" if d > 0 else "start", 700)
        ratios = [abs(legs[j + 1]) / legs[j] for j in range(0, len(legs), 2)]
        s.text(x0 + 20, 380, t("pullback ÷ impulse:", "การย่อ ÷ แรงส่ง:"), 13, C["muted"])
        s.text(x0 + 20, 404, "   ".join(f"{r:.2f}" for r in ratios), 17, col, weight=700)
        s.text(x0 + 20, 430, t("Each new high: ", "จุดสูงใหม่แต่ละครั้ง: ") + " → ".join(f"{v:g}" for v in pts[1::2]), 13, C["muted"])
    return s.render()


def _lanes(s, t, rows, lo, hi, target, x0=330, scale=None):
    """Horizontal risk (red) / reward (green) lanes. rows: (name, entry, stop, colour)."""
    scale = scale or 560 / (hi - lo)
    X = lambda p: x0 + (p - lo) * scale
    for p in range(int(lo) + 1, int(hi) + 1):
        if p % 2 == 0:
            s.line(X(p), 110, X(p), 330, C["grid"], 1)
            s.text(X(p), 350, f"{p}", 12, C["muted"], "middle")
    for k, (name, entry, stop, col) in enumerate(rows):
        y = 130 + k * 100
        risk, rew = entry - stop, target - entry
        s.text(40, y + 24, name, 15, col, weight=700)
        s.text(40, y + 46, t(f"entry {entry:g} · stop {stop:g}", f"เข้า {entry:g} · Stop {stop:g}"), 12, C["muted"])
        s.rect(X(stop), y + 8, X(entry) - X(stop), 30, fill=C["bear"], opacity=0.5, rx=3)
        s.rect(X(entry), y + 8, X(target) - X(entry), 30, fill=C["bull"], opacity=0.35, rx=3)
        s.text(X(stop) + 6, y + 64, t(f"risk {risk:.1f}", f"เสี่ยง {risk:.1f}"), 12, C["bear"], weight=600)
        s.text(X(target) - 6, y + 64, t(f"reward {rew:.1f}  →  {rew / risk:.1f}R", f"ผลตอบแทน {rew:.1f}  →  {rew / risk:.1f}R"), 13, col, "end", 700)
        s.text(X(target) + 10, y + 22, t(f"size {100 / risk:.0f}", f"ขนาด {100 / risk:.0f}"), 12, C["muted"])
        s.text(X(target) + 10, y + 40, t(f"+{100 * rew / risk:.0f} USD", f"+{100 * rew / risk:.0f} ดอลลาร์"), 12, col, weight=700)


@fig
def retest_vs_chase(lang):
    t = tr(lang)
    s = SVG(960, 420, t("Chase the breakout or wait for the retest?", "ไล่ซื้อตอนเบรก หรือรอทดสอบซ้ำ?"),
            t("Same breakout, same stop below the old zone (108.9), same target 117, risk 100 USD each (illustrative).",
              "เบรกเดียวกัน Stop เดียวกันใต้โซนเดิม (108.9) เป้าเดียวกัน 117 เสี่ยงไม้ละ 100 ดอลลาร์ (ตัวอย่าง)"))
    _lanes(s, t, [(t("Chase at 114", "ไล่ซื้อที่ 114"), 114.0, 108.9, C["bear"]),
                  (t("Buy the retest", "ซื้อตอนทดสอบซ้ำ"), 110.6, 108.9, C["bull"])], 107, 118, 117, x0=300, scale=48)
    s.text(40, 395, t("The retest gives a smaller risk for the same idea: about 6× the R:R (0.6R vs 3.8R). The cost: sometimes price never comes back.",
                      "การทดสอบซ้ำให้ความเสี่ยงเล็กกว่าสำหรับไอเดียเดียวกัน: R:R ดีขึ้นราว 6 เท่า (0.6R vs 3.8R) ต้นทุนคือบางครั้งราคาไม่กลับมา"), 13, C["amber"], weight=600)
    return s.render()


@fig
def mtf_vs_daily(lang):
    t = tr(lang)
    s = SVG(960, 420, t("Why use a lower-timeframe trigger?", "ทำไมต้องใช้สัญญาณจากไทม์เฟรมเล็ก?"),
            t("Same daily demand zone and target 131, risk 100 USD each (illustrative).",
              "โซน Demand รายวันเดียวกัน เป้า 131 เสี่ยงไม้ละ 100 ดอลลาร์ (ตัวอย่าง)"))
    _lanes(s, t, [(t("Daily candle only", "แท่งรายวันอย่างเดียว"), 126.5, 121.3, C["bear"]),
                  (t("1H CHoCH, buy the HL", "CHoCH บน 1H ซื้อที่ HL"), 124.0, 121.3, C["bull"])], 120, 132, 131, x0=300, scale=44)
    s.text(40, 395, t("The 1H CHoCH gives earlier timing and a defined stop: about 3× the R:R for the same daily idea.",
                      "CHoCH บน 1H ให้จังหวะที่เร็วกว่าและ Stop ที่ชัดเจน: R:R ดีขึ้นราว 3 เท่า สำหรับไอเดียรายวันเดียวกัน"), 13, C["amber"], weight=600)
    return s.render()


# ---------------------------------------------------------------- 2.8 indicators (C1)
from figures.indicators import series as _ind_series, sma as _sma, rsi as _rsi, macd as _macd, atr as _atr


def _sub(s, x, y, w, h, vals, lo, hi, n0, n1, color, sw=1.8):
    X = lambda i: x + w * (i - n0) / (n1 - n0)
    Y = lambda v: y + h * (hi - v) / (hi - lo)
    pts = [(X(i), Y(v)) for i, v in enumerate(vals) if n0 <= i <= n1 and v is not None]
    if pts:
        s.polyline(pts, color, sw)
    return X, Y


@fig
def indicator_stack(lang):
    t = tr(lang)
    cs = _ind_series()
    cl = [c[3] for c in cs]
    s20, s50 = _sma(cl, 20), _sma(cl, 50)
    r = _rsi(cl)
    m, sg, hist = _macd(cl)
    a = _atr(cs)
    s = SVG(960, 720, t("Five indicators on the same 200 candles", "อินดิเคเตอร์ห้าตัวบนแท่งเทียน 200 แท่งเดียวกัน"),
            t("Generated price series (up-trend, down-trend, range, up-trend). Every line is computed from the candles.",
              "ราคาที่สร้างขึ้น (ขาขึ้น ขาลง กรอบ ขาขึ้น) ทุกเส้นคำนวณจากแท่งเทียน"))
    x0, w, n0, n1 = 70, 860, 0, 199
    panel(s, 28, 86, 904, 620)
    # price + MAs
    ch = CandleChart(s, x0, 100, w, 230, [c[:4] for c in cs], grid=False)
    ch.draw(width=0.7)
    for vals, col, lab in ((s20, C["amber"], "SMA 20"), (s50, C["purple"], "SMA 50")):
        ch.path([(i, v) for i, v in enumerate(vals) if v is not None], col, 2)
    s.text(x0 + 6, 116, "SMA 20", 12, C["amber"], weight=700)
    s.text(x0 + 70, 116, "SMA 50", 12, C["purple"], weight=700)
    # volume
    vmax = max(c[4] for c in cs)
    for i, c in enumerate(cs):
        hgt = 40 * c[4] / vmax
        s.rect(ch.X(i) - 1.5, 372 - hgt, 3, hgt, fill=C["bull"] if c[3] >= c[0] else C["bear"], opacity=0.55)
    s.text(x0 - 8, 360, t("Vol", "วอลุ่ม"), 11, C["muted"], "end")
    # RSI
    y = 390
    for lvl, col in ((70, C["bear"]), (30, C["bull"])):
        yy = y + 90 * (100 - lvl) / 100
        s.line(x0, yy, x0 + w, yy, col, 1, "4 4")
        s.text(x0 - 8, yy + 4, str(lvl), 11, col, "end")
    _sub(s, x0, y, w, 90, r, 0, 100, n0, n1, C["blue"])
    s.text(x0 + 6, y + 12, "RSI 14", 12, C["blue"], weight=700)
    # MACD
    y = 500
    hv = [v for v in hist if v is not None]
    mx = max(abs(v) for v in m if v is not None)
    Xm = lambda i: x0 + w * i / 199
    Ym = lambda v: y + 45 - 45 * v / mx
    for i, v in enumerate(hist):
        if v is not None:
            s.rect(Xm(i) - 1.5, min(Ym(0), Ym(v)), 3, abs(Ym(v) - Ym(0)), fill=C["bull"] if v >= 0 else C["bear"], opacity=0.6)
    _sub(s, x0, y, w, 90, m, -mx, mx, n0, n1, C["teal"])
    _sub(s, x0, y, w, 90, sg, -mx, mx, n0, n1, C["pink"], 1.4)
    s.text(x0 + w - 4, y + 12, t("MACD 12-26-9 (line, signal, histogram)", "MACD 12-26-9 (เส้น สัญญาณ ฮิสโตแกรม)"), 12, C["teal"], "end", 700)
    # ATR
    y = 610
    av = [v for v in a if v is not None]
    _sub(s, x0, y, w, 80, a, 0, max(av) * 1.1, n0, n1, C["amber"])
    s.text(x0 + 6, y + 12, t(f"ATR 14 (now {a[-1]:.2f})", f"ATR 14 (ล่าสุด {a[-1]:.2f})"), 12, C["amber"], weight=700)
    return s.render()


@fig
def rsi_trend(lang):
    t = tr(lang)
    cs = _ind_series()[:72]
    cl = [c[3] for c in cs]
    r = _rsi(cl)
    s = SVG(960, 540, t("'Overbought' is not a sell signal in a strong trend", "'ซื้อมากเกินไป' ไม่ใช่สัญญาณขายในเทรนด์ที่แรง"),
            t("Same generated series, first 72 candles. RSI is above 70 again and again while price keeps rising.",
              "ราคาชุดเดิม 72 แท่งแรก RSI อยู่เหนือ 70 ซ้ำแล้วซ้ำเล่า ขณะที่ราคายังขึ้นต่อ"))
    panel(s, 28, 86, 904, 410)
    ch = CandleChart(s, 70, 110, 860, 240, [c[:4] for c in cs], grid=False)
    ch.draw()
    first = next(i for i, x in enumerate(r) if x and x > 70)
    top = max(range(len(cl)), key=lambda i: cl[i])
    s.circle(ch.X(first), ch.Y(cl[first]), 6, C["bear"])
    ch.label(first, cs[first][2], t(f"RSI first > 70 · close {cl[first]:.2f}", f"RSI เกิน 70 ครั้งแรก · ปิด {cl[first]:.2f}"), C["bear"], dy=34, size=12, anchor="start", dx=8)
    ch.label(top, cs[top][1], t(f"top · {cl[top]:.2f} (+{(cl[top] / cl[first] - 1) * 100:.1f}%)", f"ยอด · {cl[top]:.2f} (+{(cl[top] / cl[first] - 1) * 100:.1f}%)"), C["bull"], dy=-14, size=12)
    y = 370
    for lvl, col in ((70, C["bear"]), (30, C["bull"])):
        yy = y + 110 * (100 - lvl) / 100
        s.line(70, yy, 930, yy, col, 1, "4 4")
        s.text(62, yy + 4, str(lvl), 11, col, "end")
    X, Y = _sub(s, 70, y, 860, 110, r, 0, 100, 0, len(cs) - 1, C["blue"], 2)
    for i, x in enumerate(r):
        if x and x > 70:
            s.circle(ch.X(i), Y(x), 3, C["bear"])
    n70 = sum(1 for i in range(first, top + 1) if r[i] and r[i] > 70)
    s.text(70, 522, t(f"{n70} candles closed with RSI above 70 between the first 'overbought' reading and the top. Selling the first one would have lost money.",
                      f"มี {n70} แท่งที่ปิดโดย RSI เหนือ 70 ระหว่างครั้งแรกที่ 'ซื้อมากเกินไป' จนถึงยอด การขายครั้งแรกจะขาดทุน"), 12, C["amber"], weight=600)
    return s.render()


@fig
def ma_lag(lang):
    t = tr(lang)
    allc = _ind_series()
    cl_all = [c[3] for c in allc]
    s20a, s50a = _sma(cl_all, 20), _sma(cl_all, 50)
    n0, n1 = 40, 90
    cs = allc[n0:n1 + 1]
    s = SVG(960, 480, t("Moving averages lag: they confirm, they don't predict", "ค่าเฉลี่ยเคลื่อนที่ช้ากว่าราคา: ยืนยันได้ แต่ทำนายไม่ได้"),
            t("Same series, candles 40–90 around the top of the first up-trend.", "ราคาชุดเดิม แท่งที่ 40–90 รอบยอดของขาขึ้นแรก"))
    panel(s, 28, 86, 904, 370)
    ch = CandleChart(s, 70, 110, 860, 300, [c[:4] for c in cs], grid=False)
    ch.draw()
    ch.path([(i - n0, s20a[i]) for i in range(n0, n1 + 1) if s20a[i] is not None], C["amber"], 2)
    ch.path([(i - n0, s50a[i]) for i in range(n0, n1 + 1) if s50a[i] is not None], C["purple"], 2)
    top = max(range(0, 80), key=lambda i: cl_all[i])
    below = next(i for i in range(top, 200) if cl_all[i] < s20a[i])
    cross = next(i for i in range(top, 200) if s50a[i] is not None and s20a[i] < s50a[i])
    marks = ((top, C["bull"], t(f"1 · top: bar {top}, close {cl_all[top]:.2f}", f"1 · ยอด: แท่ง {top} ปิด {cl_all[top]:.2f}")),
             (below, C["amber"], t(f"2 · first close below SMA 20: bar {below}, {cl_all[below]:.2f}", f"2 · ปิดใต้ SMA 20 ครั้งแรก: แท่ง {below} {cl_all[below]:.2f}")),
             (cross, C["bear"], t(f"3 · SMA 20 crosses below SMA 50: bar {cross}, {cl_all[cross]:.2f}", f"3 · SMA 20 ตัดลงใต้ SMA 50: แท่ง {cross} {cl_all[cross]:.2f}")))
    for k, (i, col, lab) in enumerate(marks):
        s.circle(ch.X(i - n0), ch.Y(cl_all[i]), 9, col)
        s.text(ch.X(i - n0), ch.Y(cl_all[i]) + 5, str(k + 1), 12, C["bg"], "middle", 800)
        s.text(80, 340 + k * 22, lab, 12, col, weight=700)
    s.text(70, 440, t(f"The crossover came {cross - top} candles after the top and {cl_all[top] - cl_all[cross]:.1f} points lower: useful as a trend filter, late as an exit.",
                      f"เส้นตัดกันเกิดหลังยอด {cross - top} แท่ง และต่ำกว่า {cl_all[top] - cl_all[cross]:.1f} จุด: ใช้เป็นตัวกรองเทรนด์ได้ แต่ช้าเกินไปสำหรับการออก"), 12, C["amber"], weight=600)
    return s.render()


# ---------------------------------------------------------------- 2.9 classic patterns (C1)
@fig
def classic_patterns(lang):
    t = tr(lang)
    s = SVG(960, 640, t("Four classic patterns and their measured targets", "รูปแบบคลาสสิกสี่แบบและเป้าวัดระยะ"),
            t("Illustrative candles. A pattern only counts after the close beyond the neckline / trend line.",
              "แท่งเทียนตัวอย่าง รูปแบบนับได้ก็ต่อเมื่อราคาปิดเลยเส้นคอ / เส้นแนวโน้มแล้วเท่านั้น"))
    specs = [
        (t("Double top", "ยอดคู่ (Double top)"), [40, 50, 46, 49.8, 45.4, 42], [6, 5, 5, 5, 4], 46.0, 42.0, C["bear"],
         t("neckline 46 · height 4 → target 42", "เส้นคอ 46 · ความสูง 4 → เป้า 42")),
        (t("Head & shoulders top", "หัวไหล่ (Head & shoulders)"), [100, 115, 110, 120, 110, 115.5, 109.4, 100], [5, 3, 4, 4, 4, 3, 5], 110.0, 100.0, C["bear"],
         t("neckline 110 · height 10 → target 100", "เส้นคอ 110 · ความสูง 10 → เป้า 100")),
        (t("Ascending triangle", "สามเหลี่ยมขาขึ้น (Ascending)"), [42, 50, 46, 50, 47.5, 50, 48.6, 54], [6, 3, 3, 3, 3, 2, 5], 50.0, 54.0, C["bull"],
         t("flat top 50 · height 4 → target 54", "ยอดแบน 50 · ความสูง 4 → เป้า 54")),
        (t("Bull flag", "ธงขาขึ้น (Bull flag)"), [100, 112, 110, 111.2, 109.2, 110.6, 109.0, 123], [6, 2, 2, 2, 2, 2, 8], 111.0, 123.0, C["bull"],
         t("pole 12 · break 111 → target 123", "เสาธง 12 · ทะลุ 111 → เป้า 123")),
    ]
    for k, (name, piv, bars, line, tgt, col, note) in enumerate(specs):
        x, y = 28 + (k % 2) * 462, 90 + (k // 2) * 270
        panel(s, x, y, 442, 256, name, col)
        cs, idx = walk(piv, bars, seed=40 + k)
        lo, hi = min(min(c[2] for c in cs), tgt), max(max(c[1] for c in cs), tgt)
        ch = CandleChart(s, x + 16, y + 44, 410, 170, cs, pmin=lo - (hi - lo) * 0.05, pmax=hi + (hi - lo) * 0.08, grid=False)
        ch.draw()
        ch.hline(line, None, C["amber"], 0, len(cs) - 1, "6 4")
        ch.hline(tgt, None, col, int(len(cs) * 0.6), len(cs) - 1, "2 3")
        s.text(x + 18, y + 240, note, 12, C["text"], weight=600)
    return s.render()


@fig
def pattern_stats(lang):
    t = tr(lang)
    s = SVG(960, 540, t("How often do patterns fail? Published statistics", "รูปแบบล้มเหลวบ่อยแค่ไหน? สถิติที่เผยแพร่"),
            t("Bulkowski, thepatternsite.com: US stocks, bull markets, daily charts, 1,100–3,000+ trades per pattern (checked Oct 2026).",
              "Bulkowski, thepatternsite.com: หุ้นสหรัฐ ตลาดขาขึ้น กราฟรายวัน 1,100–3,000+ ครั้งต่อรูปแบบ (ตรวจสอบ ต.ค. 2026)"))
    rows = [(t("Double bottom (up)", "ก้นคู่ (ขึ้น)"), 16, 73), (t("Ascending triangle (up)", "สามเหลี่ยมขาขึ้น (ขึ้น)"), 17, 70),
            (t("Head & shoulders top (down)", "หัวไหล่ (ลง)"), 19, 51), (t("Double top (down)", "ยอดคู่ (ลง)"), 25, 64),
            (t("Symmetrical triangle (up)", "สามเหลี่ยมสมมาตร (ขึ้น)"), 25, 58), (t("Symmetrical triangle (down)", "สามเหลี่ยมสมมาตร (ลง)"), 37, 36),
            (t("Ascending triangle (down)", "สามเหลี่ยมขาขึ้น (ลง)"), 38, 44), (t("Flag (up)", "ธง (ขึ้น)"), 44, 46)]
    x0, sc = 330, 4.4
    s.text(x0, 106, t("break-even failure rate", "อัตราล้มเหลวที่จุดคุ้มทุน"), 13, C["bear"], weight=700)
    s.text(x0 + 300, 106, t("% reaching the measured target", "% ที่ถึงเป้าวัดระยะ"), 13, C["bull"], weight=700)
    for k, (name, fail, hit) in enumerate(rows):
        y = 124 + k * 44
        s.text(x0 - 14, y + 20, name, 13, C["text"], "end", 600)
        s.rect(x0, y + 4, fail * sc, 24, fill=C["bear"], opacity=0.8, rx=3)
        s.text(x0 + fail * sc + 8, y + 22, f"{fail}%", 13, C["bear"], weight=700)
        s.rect(x0 + 300, y + 4, hit * sc * 0.75, 24, fill=C["bull"], opacity=0.7, rx=3)
        s.text(x0 + 300 + hit * sc * 0.75 + 8, y + 22, f"{hit}%", 13, C["bull"], weight=700)
    s.text(40, 500, t("Break-even failure = price fails to move at least 5% in the breakout direction. Measured without stops: not your expectancy.",
                      "ล้มเหลวที่จุดคุ้มทุน = ราคาไม่ขยับอย่างน้อย 5% ในทิศทางที่ทะลุ วัดโดยไม่มี Stop: ไม่ใช่ค่าคาดหวังของคุณ"), 12, C["amber"], weight=600)
    s.text(40, 522, t("Double top = Adam & Adam type; Eve & Eve double tops fail 20%.", "ยอดคู่ = แบบ Adam & Adam ส่วนแบบ Eve & Eve ล้มเหลว 20%"), 12, C["muted"])
    return s.render()


@fig
def pattern_entries(lang):
    t = tr(lang)
    s = SVG(960, 440, t("Where you enter decides the R:R, not the pattern", "จุดเข้าเป็นตัวกำหนด R:R ไม่ใช่ตัวรูปแบบ"),
            t("The double top from the first figure: same pattern, same target 42.0 (illustrative prices).",
              "ยอดคู่จากภาพแรก: รูปแบบเดียวกัน เป้าเดียวกัน 42.0 (ราคาตัวอย่าง)"))
    rows = [(t("Short the breakout close", "Short ตอนปิดทะลุ"), 45.8, 50.4, C["bear"], t("stop above the right top", "Stop เหนือยอดขวา")),
            (t("Short the pullback to the neckline", "Short ตอนย่อกลับมาที่เส้นคอ"), 46.0, 47.2, C["bull"], t("stop above the pullback high (46.8) + buffer", "Stop เหนือจุดสูงของการย่อกลับ (46.8) + ระยะเผื่อ"))]
    X = lambda p: 820 - (p - 41) * 62
    for p in (42, 44, 46, 48, 50):
        s.line(X(p), 110, X(p), 320, C["grid"], 1)
        s.text(X(p), 340, f"{p}", 12, C["muted"], "middle")
    for k, (name, entry, stop, col, note) in enumerate(rows):
        y = 130 + k * 100
        risk, rew = stop - entry, entry - 42.0
        s.text(40, y + 20, name, 15, col, weight=700)
        s.text(40, y + 42, t(f"entry {entry} · stop {stop}", f"เข้า {entry} · Stop {stop}"), 12, C["muted"])
        s.text(40, y + 60, note, 11, C["muted"])
        s.rect(X(stop), y + 8, X(entry) - X(stop), 28, fill=C["bear"], opacity=0.5, rx=3)
        s.rect(X(entry), y + 8, X(42.0) - X(entry), 28, fill=C["bull"], opacity=0.3, rx=3)
        s.text(X(42.0) + 10, y + 28, f"{rew / risk:.2f}R", 15, col, weight=700)
    s.text(40, 400, t("Bulkowski reports a pullback to the neckline in about 64% of double tops, so the better entry is often available, but not always.",
                      "Bulkowski รายงานว่าราคาย่อกลับมาที่เส้นคอราว 64% ของยอดคู่ จุดเข้าที่ดีกว่าจึงมักมีให้ แต่ไม่ใช่ทุกครั้ง"), 12, C["amber"], weight=600)
    return s.render()
