"""Phase 0 tool add-on figures (C5: lessons 0.13 TradingView basics, 0.14 calendars & screeners,
0.15 prop firms). Every number comes from _tools/toolkit/analysis.py (or investing/analysis.py for
the S&P 500 series)."""
import math
import sys
from pathlib import Path
from charts import SVG, C, tr

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "toolkit"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "investing"))
import analysis as A  # noqa: E402  (investing/analysis.py: S&P 500 data)
import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "toolkit_analysis", Path(__file__).resolve().parents[1] / "toolkit" / "analysis.py")
T = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(T)

FIGURES = {}


def fig(fn):
    FIGURES["p0-" + fn.__name__.replace("_", "-")] = fn
    return fn


def panel(s, x, y, w, h, fill=None):
    s.rect(x, y, w, h, fill=fill or C["panel"], stroke=C["border"], rx=12)


def fmt(v):
    return f"{v:,.0f}"


# ---------------------------------------------------------------- 0.13 TradingView basics
@fig
def tv_layout(lang):
    t = tr(lang)
    s = SVG(960, 560, t("A charting screen, piece by piece", "หน้าจอกราฟ ทีละส่วน"),
        t("Most charting platforms (TradingView, broker apps, MT5) use the same layout. Learn the parts once.",
          "แพลตฟอร์มกราฟส่วนใหญ่ (TradingView, แอปโบรกเกอร์, MT5) ใช้หน้าตาคล้ายกัน เรียนรู้ส่วนต่างๆ ครั้งเดียว"))
    # window frame
    panel(s, 28, 92, 904, 440, C["bg"])
    # top bar
    s.rect(28, 92, 904, 40, fill=C["panel"], stroke=C["border"], rx=12)
    s.rect(44, 101, 120, 22, fill=C["grid"], rx=6)
    s.text(54, 117, "EURUSD 🔍", 13, C["text"])
    for k, tf in enumerate(["5m", "15m", "1h", "4h", "D", "W"]):
        col = C["blue"] if tf == "1h" else C["muted"]
        s.text(186 + k * 34, 117, tf, 13, col, weight=700 if tf == "1h" else 400)
    s.text(400, 117, "ƒx " + t("Indicators", "อินดิเคเตอร์"), 13, C["text"])
    s.text(540, 117, "⏰ " + t("Alert", "แจ้งเตือน"), 13, C["text"])
    s.text(650, 117, "↺ " + t("Replay", "ย้อนดู"), 13, C["text"])
    # left drawing toolbar
    s.rect(28, 132, 40, 400, fill=C["panel"], stroke=C["border"])
    for k, ic in enumerate(["╱", "─", "▭", "⌇", "✎", "📏", "T", "🧲"]):
        s.text(48, 162 + k * 40, ic, 15, C["text"], "middle")
    # right watchlist
    s.rect(742, 132, 190, 400, fill=C["panel"], stroke=C["border"])
    s.text(756, 156, t("Watchlist", "รายการจับตา"), 13, C["amber"], weight=700)
    wl = [("EURUSD", "+0.12%", C["bull"]), ("XAUUSD", "−0.40%", C["bear"]), ("SPX", "+0.31%", C["bull"]),
          ("NVDA", "+1.05%", C["bull"]), ("BTCUSD", "−2.10%", C["bear"]), ("PTT", "D  +0.50%", C["bull"])]
    for k, (sym, ch, col) in enumerate(wl):
        s.text(756, 184 + k * 24, sym, 12, C["text"])
        s.text(918, 184 + k * 24, ch, 12, col, "end")
    # chart area: simple candle path
    import random
    rnd = random.Random(4)
    p = 100.0
    for i in range(44):
        o = p
        c = o + rnd.uniform(-1.6, 1.8)
        hi, lo = max(o, c) + rnd.uniform(0.2, 1.0), min(o, c) - rnd.uniform(0.2, 1.0)
        X = 92 + i * 13

        def Y(v):
            return 470 - (v - 92) * 11
        col = C["bull"] if c >= o else C["bear"]
        s.line(X, Y(hi), X, Y(lo), col, 1.2)
        s.rect(X - 4, Y(max(o, c)), 8, max(abs(Y(o) - Y(c)), 1.5), fill=col)
        p = c
    # price scale and time scale
    s.line(682, 132, 682, 500, C["border"], 1)
    s.line(68, 500, 742, 500, C["border"], 1)
    for k in range(5):
        s.text(712, 170 + k * 80, f"1.08{9 - 2 * k}0", 11, C["muted"], "middle")
    for k, d in enumerate(["06", "07", "08", "09"]):
        s.text(130 + k * 150, 518, f"Oct {d}" if lang == "en" else f"{d} ต.ค.", 11, C["muted"], "middle")

    def callout(x, y, tx, ty, label, col):
        s.line(x, y, tx, ty, col, 1.5)
        s.circle(x, y, 4, col)
        s.pill(tx, ty, label, col, 12)

    callout(110, 128, 150, 160, t("1 Symbol search", "1 ค้นหาสัญลักษณ์"), C["blue"])
    callout(262, 128, 330, 190, t("2 Timeframes", "2 ไทม์เฟรม"), C["teal"])
    callout(48, 242, 170, 300, t("3 Drawing tools", "3 เครื่องมือวาด"), C["purple"])
    callout(430, 128, 470, 220, t("4 Indicators", "4 อินดิเคเตอร์"), C["amber"])
    callout(560, 128, 600, 260, t("5 Alerts", "5 การแจ้งเตือน"), C["pink"])
    callout(712, 330, 610, 400, t("6 Price scale", "6 สเกลราคา"), C["muted"])
    callout(856, 308, 830, 470, t("7 'D' = delayed", "7 'D' = ข้อมูลล่าช้า"), C["bear"])
    return s.render()


@fig
def tv_plans(lang):
    t = tr(lang)
    s = SVG(960, 470, t("Free vs paid charting plans (TradingView, as of Oct 2026)", "แพ็กเกจฟรีกับแบบเสียเงิน (TradingView ณ ต.ค. 2026)"),
        t("The free plan is enough to learn everything in this course. Prices are monthly, in USD.",
          "แพ็กเกจฟรีเพียงพอสำหรับเรียนทุกอย่างในคอร์สนี้ ราคาเป็นรายเดือน หน่วย USD"))
    panel(s, 28, 92, 904, 350)
    cols = [t("Plan", "แพ็กเกจ"), t("Price / month", "ราคา/เดือน"), t("Indicators\nper chart", "อินดิเคเตอร์\nต่อกราฟ"),
            t("Charts\nper tab", "กราฟ\nต่อแท็บ"), t("Price\nalerts", "แจ้งเตือน\nราคา"), t("Bars of\nhistory", "จำนวนแท่ง\nย้อนหลัง"),
            t("= daily bars\n(years)", "= แท่งรายวัน\n(ปี)")]
    xs = [60, 190, 330, 450, 560, 670, 800]
    for x, h in zip(xs, cols):
        s.text(x, 128, h, 13, C["muted"], weight=700)
    for r, (name, v) in enumerate(T.PLANS.items()):
        y = 200 + r * 52
        col = C["bull"] if name == "Basic" else C["text"]
        s.line(48, y - 26, 912, y - 26, C["grid"], 1)
        price = t("free", "ฟรี") if v["price"] == 0 else f"${v['price']:.2f}"
        cells = [name, price, str(v["ind"]), str(v["charts"]), str(v["price_alerts"]), fmt(v["bars"]),
                 f"{T.bars_cover(v['bars'])['daily_years']:.1f}"]
        for x, c in zip(xs, cells):
            s.text(x, y, c, 16, col, weight=700 if x == 60 else 400)
    s.text(48, 420, t("Source: tradingview.com/pricing (checked Oct 2026). Plans and limits change; check before paying. Years = bars ÷ 252 trading days.",
                      "ที่มา: tradingview.com/pricing (ตรวจ ต.ค. 2026) แพ็กเกจและข้อจำกัดเปลี่ยนได้ ตรวจก่อนจ่ายเงิน ปี = จำนวนแท่ง ÷ 252 วันทำการ"), 12, C["dim"])
    return s.render()


@fig
def log_linear(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Same data, two price scales: S&P 500, 1988–2026", "ข้อมูลเดียวกัน สองสเกลราคา: S&P 500 ปี 1988–2026"),
        t("Linear: equal distances = equal points. Log: equal distances = equal percentages.",
          "Linear: ระยะเท่ากัน = จำนวนจุดเท่ากัน   Log: ระยะเท่ากัน = เปอร์เซ็นต์เท่ากัน"))
    ser = A.series("gspc_m", 1)
    keys = sorted(ser)
    vals = [ser[k] for k in keys]
    dd = ser["2002-09"] / ser["2000-08"] - 1
    for j, (log, title) in enumerate([(False, t("Linear scale", "สเกล Linear")), (True, t("Log scale", "สเกล Log"))]):
        x0 = 28 + j * 462
        panel(s, x0, 92, 442, 380)
        s.text(x0 + 20, 122, title, 16, C["amber"] if not log else C["teal"], weight=700)
        bx, by, bw, bh = x0 + 62, 140, 360, 290
        lo, hi = 200, 9000
        ticks = [250, 500, 1000, 2000, 4000, 8000] if log else [2000, 4000, 6000, 8000]

        def Y(v):
            if log:
                return by + bh * (math.log10(hi) - math.log10(v)) / (math.log10(hi) - math.log10(lo))
            return by + bh * (hi - v) / (hi - lo)
        for tk in ticks:
            s.line(bx, Y(tk), bx + bw, Y(tk), C["grid"], 1)
            s.text(bx - 6, Y(tk) + 4, fmt(tk), 11, C["muted"], "end")
        pts = [(bx + bw * i / (len(vals) - 1), Y(v)) for i, v in enumerate(vals)]
        s.polyline(pts, C["blue"], 2)
        # highlight 2000-2002 fall
        i0, i1 = keys.index("2000-08"), keys.index("2002-09")
        s.polyline(pts[i0:i1 + 1], C["bear"], 3.5)
        mx = pts[i1][0]
        s.text(mx, Y(ser["2002-09"]) + (34 if log else -46), t(f"2000–02: {dd*100:.0f}%", f"2000–02: {dd*100:.0f}%"), 12, C["bear"], "middle", 700)
        for yr in (1990, 2000, 2010, 2020):
            i = keys.index(f"{yr}-01")
            s.text(bx + bw * i / (len(vals) - 1), 448, str(yr), 11, C["muted"], "middle")
    s.text(40, 490, t("Both panels show the same fall of the same size. Use log for long histories and fast-growing assets (stocks, BTC).",
                      "ทั้งสองแผงแสดงการร่วงที่ขนาดเท่ากัน ใช้ Log กับข้อมูลระยะยาวและสินทรัพย์ที่โตเร็ว (หุ้น, BTC)"), 12, C["dim"])
    return s.render()


@fig
def position_tool(lang):
    t = tr(lang)
    r = T.position_tool(1.0850, 1.0830, 1.0890, 100)
    s = SVG(960, 470, t("The long-position tool: risk, reward and size in one drawing", "เครื่องมือ Long Position: ความเสี่ยง ผลตอบแทน และขนาด ในภาพเดียว"),
        t("EUR/USD example. You drag three lines; the tool does the maths you learned in 3.2 and 3.3.",
          "ตัวอย่าง EUR/USD ลากเส้นสามเส้น เครื่องมือคำนวณแบบที่เรียนในบท 3.2 และ 3.3 ให้"))
    panel(s, 28, 92, 904, 350)

    def Y(p):
        return 420 - (p - 1.0815) / (1.0900 - 1.0815) * 300
    x0, x1 = 250, 620
    s.rect(x0, Y(1.0890), x1 - x0, Y(1.0850) - Y(1.0890), fill=C["bull"], opacity=0.22, stroke=C["bull"], sw=1)
    s.rect(x0, Y(1.0850), x1 - x0, Y(1.0830) - Y(1.0850), fill=C["bear"], opacity=0.25, stroke=C["bear"], sw=1)
    for p, lab, col in [(1.0890, t("Target 1.0890", "เป้า 1.0890"), C["bull"]), (1.0850, t("Entry 1.0850", "เข้า 1.0850"), C["text"]),
                        (1.0830, t("Stop 1.0830", "Stop 1.0830"), C["bear"])]:
        s.line(x0, Y(p), x1, Y(p), col, 2)
        s.text(x0 - 12, Y(p) + 5, lab, 14, col, "end", 700)
    s.text((x0 + x1) / 2, (Y(1.0890) + Y(1.0850)) / 2 + 5, t(f"+{r['reward_pips']:.0f} pips", f"+{r['reward_pips']:.0f} pips"), 16, C["bull"], "middle", 700)
    s.text((x0 + x1) / 2, (Y(1.0850) + Y(1.0830)) / 2 + 5, t(f"−{r['risk_pips']:.0f} pips", f"−{r['risk_pips']:.0f} pips"), 15, C["bear"], "middle", 700)
    bx = 660
    s.text(bx, 140, t("Tool read-out", "ค่าที่เครื่องมือแสดง"), 16, C["amber"], weight=700)
    lines = [
        (t("Account", "บัญชี"), "10,000 USD"),
        (t("Risk", "ความเสี่ยง"), "1% = 100 USD"),
        (t("Risk/reward", "Risk/Reward"), f"1 : {r['rr']:.1f}"),
        (t("Size", "ขนาด"), t(f"{r['lots']:.2f} lots", f"{r['lots']:.2f} ล็อต")),
        (t("If target hit", "ถ้าถึงเป้า"), f"+{r['reward_money']:.0f} USD"),
        (t("If stop hit", "ถ้าโดน Stop"), "−100 USD"),
    ]
    for k, (a, b) in enumerate(lines):
        s.text(bx, 176 + k * 36, a, 14, C["muted"])
        s.text(910, 176 + k * 36, b, 15, C["text"], "end", 700)
    s.text(bx, 410, t("1 standard lot: 1 pip = 10 USD", "1 ล็อตมาตรฐาน: 1 pip = 10 USD"), 12, C["dim"])
    return s.render()


# ---------------------------------------------------------------- 0.14 calendars & screeners
@fig
def cal_dates(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Big US releases, Oct–Dec 2026, in Bangkok time", "ข่าวใหญ่สหรัฐฯ ต.ค.–ธ.ค. 2026 ตามเวลากรุงเทพฯ"),
        t("Official dates (BLS, Federal Reserve). Watch the jump of +1 hour after the US clocks change on 1 Nov.",
          "วันที่ทางการ (BLS, ธนาคารกลางสหรัฐฯ) สังเกตว่าเวลาเลื่อน +1 ชั่วโมงหลังสหรัฐฯ เปลี่ยนเวลาวันที่ 1 พ.ย."))
    panel(s, 28, 92, 904, 380)
    hdr = [t("Release", "ข่าว"), t("New York time", "เวลานิวยอร์ก"), t("Bangkok time (UTC+7)", "เวลากรุงเทพฯ (UTC+7)")]
    for x, h in zip([60, 360, 620], hdr):
        s.text(x, 128, h, 14, C["muted"], weight=700)
    th_days = {"Mon": "จ.", "Tue": "อ.", "Wed": "พ.", "Thu": "พฤ.", "Fri": "ศ.", "Sat": "ส.", "Sun": "อา."}
    th_mon = {"Oct": "ต.ค.", "Nov": "พ.ย.", "Dec": "ธ.ค."}
    names = {"US CPI": t("US CPI (inflation)", "CPI สหรัฐฯ (เงินเฟ้อ)"), "FOMC decision": t("FOMC rate decision", "FOMC ตัดสินดอกเบี้ย"),
             "US jobs report (NFP)": t("US jobs report (NFP)", "รายงานการจ้างงาน (NFP)")}

    def d(dt):
        a, dd, m, hm = dt.strftime("%a %d %b %H:%M").split()
        return f"{a} {dd} {m}  {hm}" if lang == "en" else f"{th_days[a]} {int(dd)} {th_mon[m]}  {hm}"
    from datetime import datetime
    for k, (name, dt, tz) in enumerate(T.RELEASES):
        y = 164 + k * 40 + (20 if k >= 2 else 0)
        local = datetime(*dt, tzinfo=tz)
        bkk = T.to_bkk(*dt, tz)
        winter = local.utcoffset().total_seconds() == -5 * 3600
        col = C["amber"] if "FOMC" in name else C["text"]
        s.text(60, y, names[name], 15, col, weight=700)
        s.text(360, y, d(local) + (" EST" if winter else " EDT"), 14, C["muted"])
        s.text(620, y, d(bkk), 16, C["teal"] if not winter else C["blue"], weight=700)
        if k == 2:
            s.line(48, y - 40, 912, y - 40, C["pink"], 1.5, "6 4")
            s.text(910, y - 24, t("US clocks go back 1 Nov", "สหรัฐฯ ปรับเวลาถอยหลัง 1 พ.ย."), 12, C["pink"], "end", 700)
    s.text(48, 460, t("Dates as published Oct 2026; they can change (e.g. a government shutdown delayed US data in 2025). Check the official calendar each week.",
                      "วันที่ตามที่ประกาศ ต.ค. 2026 อาจเปลี่ยนได้ (เช่น การปิดหน่วยงานรัฐทำให้ข้อมูลสหรัฐฯ เลื่อนในปี 2025) ตรวจปฏิทินทางการทุกสัปดาห์"), 12, C["dim"])
    return s.render()


@fig
def cal_dst(lang):
    t = tr(lang)
    s = SVG(960, 420, t("The clock-change trap: Europe and the US switch on different dates", "กับดักการเปลี่ยนเวลา: ยุโรปกับสหรัฐฯ เปลี่ยนคนละวัน"),
        t("Thailand and Laos never change clocks, so session times shift for us twice a year, in two steps.",
          "ไทยและลาวไม่เปลี่ยนเวลา เวลาเปิดตลาดจึงเลื่อนสำหรับเราปีละสองครั้ง และเลื่อนเป็นสองขั้น"))
    rows = T.dst_gap_2026()
    labels = [t("Fri 23 Oct\n(both on summer time)", "ศ. 23 ต.ค.\n(ทั้งคู่ใช้เวลาฤดูร้อน)"),
              t("Tue 27 Oct\n(Europe changed 25 Oct)", "อ. 27 ต.ค.\n(ยุโรปเปลี่ยน 25 ต.ค.)"),
              t("Tue 3 Nov\n(US changed 1 Nov)", "อ. 3 พ.ย.\n(สหรัฐฯ เปลี่ยน 1 พ.ย.)")]
    for k, ((dte, lon, ny), lab) in enumerate(zip(rows, labels)):
        x = 28 + k * 304
        panel(s, x, 96, 288, 290)
        s.text(x + 20, 128, lab, 15, C["text"], weight=700)
        s.text(x + 20, 210, t("London open", "ลอนดอนเปิด"), 14, C["muted"])
        s.text(x + 268, 210, lon, 26, C["blue"], "end", 700)
        s.text(x + 20, 280, t("New York open", "นิวยอร์กเปิด"), 14, C["muted"])
        s.text(x + 268, 280, ny, 26, C["amber"], "end", 700)
        s.text(x + 20, 350, t("Bangkok time", "เวลากรุงเทพฯ"), 12, C["dim"])
        if k:
            prev = rows[k - 1]
            changed = [t("London", "ลอนดอน") if lon != prev[1] else None, t("New York", "นิวยอร์ก") if ny != prev[2] else None]
            changed = [c for c in changed if c]
            s.pill(x + 144, 372, t("+1h: ", "+1 ชม.: ") + ", ".join(changed), C["pink"], 12)
    s.text(40, 408, t("London opens 08:00 London time; New York stock market opens 09:30 New York time. Computed with Python zoneinfo for 2026.",
                      "ลอนดอนเปิด 08:00 เวลาลอนดอน ตลาดหุ้นนิวยอร์กเปิด 09:30 เวลานิวยอร์ก คำนวณด้วย Python zoneinfo สำหรับปี 2026"), 12, C["dim"])
    return s.render()


@fig
def screener_funnel(lang):
    t = tr(lang)
    steps = T.screen()
    s = SVG(960, 480, t("A screener is a funnel: each filter removes stocks", "Screener คือกรวย: ทุกตัวกรองตัดหุ้นออก"),
        t("Made-up example of 10 stocks. A screener finds candidates to study, not trades to take.",
          "ตัวอย่างสมมติ 10 หุ้น Screener หาหุ้นที่ควรศึกษา ไม่ใช่หุ้นที่ต้องซื้อ"))
    names = [t("All stocks in the list", "หุ้นทั้งหมดในรายการ"), t("Market cap ≥ 20bn baht", "มูลค่าตลาด ≥ 2 หมื่นล้านบาท"),
             t("Traded ≥ 50m baht a day", "ซื้อขาย ≥ 50 ล้านบาท/วัน"), t("P/E ≤ 20", "P/E ≤ 20"),
             t("Price above its 200-day average", "ราคาอยู่เหนือค่าเฉลี่ย 200 วัน")]
    cols = [C["blue"], C["teal"], C["purple"], C["amber"], C["bull"]]
    for k, ((_, n, kept), nm, col) in enumerate(zip(steps, names, cols)):
        y = 100 + k * 70
        w = 560 * n / 10
        x = 330 - w / 2 + 120
        s.rect(x, y, w, 52, fill=col, opacity=0.28, stroke=col, rx=10)
        s.text(x + w / 2, y + 33, str(n), 22, col, "middle", 700)
        s.text(40, y + 24, nm, 14, C["text"], weight=700)
        s.text(40, y + 44, " ".join(kept), 12, C["muted"])
    s.text(40, 460, t("Note: the volume filter removed nothing here because the size filter had already removed the two tiny, thinly traded stocks.",
                      "หมายเหตุ: ตัวกรองสภาพคล่องไม่ได้ตัดหุ้นเพิ่ม เพราะตัวกรองขนาดตัดหุ้นเล็กที่ซื้อขายน้อยสองตัวออกไปแล้ว"), 12, C["dim"])
    return s.render()


@fig
def screener_filters(lang):
    t = tr(lang)
    s = SVG(960, 340, t("Four kinds of screener filters", "ตัวกรองใน Screener สี่ประเภท"),
        t("Start with filters that protect you (size, liquidity), then add the ones that describe your style.",
          "เริ่มด้วยตัวกรองที่ปกป้องคุณ (ขนาด สภาพคล่อง) แล้วค่อยเพิ่มตัวกรองที่ตรงกับสไตล์ของคุณ"))
    cards = [
        (C["blue"], t("1 · Safety", "1 · ความปลอดภัย"),
         t("Market cap\nAverage volume / value\nPrice above a minimum\nExchange / country", "มูลค่าตลาด\nปริมาณ/มูลค่าซื้อขายเฉลี่ย\nราคาขั้นต่ำ\nตลาด / ประเทศ")),
        (C["teal"], t("2 · Value & quality", "2 · มูลค่า & คุณภาพ"),
         t("P/E, P/B\nDividend yield\nDebt / equity\nProfit growth  (see 10.6)", "P/E, P/B\nอัตราปันผล\nหนี้สิน/ทุน\nการเติบโตของกำไร  (ดู 10.6)")),
        (C["amber"], t("3 · Trend & momentum", "3 · เทรนด์ & โมเมนตัม"),
         t("Price vs 50/200-day average\n% from 52-week high\nRSI  (see 2.8)\nRelative volume", "ราคาเทียบค่าเฉลี่ย 50/200 วัน\n% ห่างจากจุดสูงสุด 52 สัปดาห์\nRSI  (ดู 2.8)\nปริมาณซื้อขายเทียบปกติ")),
        (C["pink"], t("4 · Events", "4 · เหตุการณ์"),
         t("Earnings date soon\nEx-dividend date soon\nGap up / down today\nNew listings", "ใกล้ประกาศงบ\nใกล้วันขึ้น XD\nเปิดกระโดดขึ้น/ลงวันนี้\nหุ้นเข้าใหม่")),
    ]
    for k, (col, title, body) in enumerate(cards):
        s.card(28 + k * 228, 100, 212, 190, title, body, col, title_size=16, body_size=14)
    s.text(40, 320, t("Tools: TradingView screener, finviz.com (US), your broker's app and set.or.th (Thailand). Fundamental data can be days or weeks old.",
                      "เครื่องมือ: Screener ของ TradingView, finviz.com (สหรัฐฯ), แอปโบรกเกอร์ และ set.or.th (ไทย) ข้อมูลพื้นฐานอาจเก่าหลายวันหรือหลายสัปดาห์"), 12, C["dim"])
    return s.render()


# ---------------------------------------------------------------- 0.15 prop firms
@fig
def prop_flow(lang):
    t = tr(lang)
    s = SVG(960, 420, t("How a typical prop-firm challenge works", "Challenge ของ Prop firm ทั่วไปทำงานอย่างไร"),
        t("Example: FTMO 2-Step rules as published Oct 2026. Other firms differ in the details.",
          "ตัวอย่าง: กฎ FTMO แบบ 2-Step ตามที่เผยแพร่ ต.ค. 2026 บริษัทอื่นต่างกันในรายละเอียด"))
    boxes = [
        (C["amber"], t("You pay a fee", "คุณจ่ายค่าธรรมเนียม"), t("≈ €540 for a\n100,000 demo\naccount", "≈ €540 สำหรับ\nบัญชีเดโม\n100,000")),
        (C["blue"], t("Phase 1", "เฟส 1"), t("Make +10%\nwithout breaking\nthe loss rules", "ทำกำไร +10%\nโดยไม่ผิด\nกฎขาดทุน")),
        (C["teal"], t("Phase 2", "เฟส 2"), t("Make +5%\nsame loss rules", "ทำกำไร +5%\nกฎขาดทุนเดิม")),
        (C["purple"], t("\"Funded\" account", "บัญชี \"Funded\""), t("Still simulated;\nyou keep 80% of\nprofits (up to 90%)", "ยังเป็นบัญชีจำลอง\nได้ 80% ของกำไร\n(สูงสุด 90%)")),
    ]
    for k, (col, title, body) in enumerate(boxes):
        x = 28 + k * 232
        s.card(x, 100, 208, 140, title, body, col, title_size=16, body_size=14)
        if k < 3:
            s.arrow(x + 210, 170, x + 230, 170, C["muted"], 2)
    panel(s, 28, 256, 904, 130)
    s.text(48, 286, t("Loss rules (both phases)", "กฎขาดทุน (ทั้งสองเฟส)"), 15, C["bear"], weight=700)
    s.text(48, 314, t("• Daily: equity may not fall more than 5% of the starting capital below the day's opening balance\n• Total: equity may never go below 90% of the starting capital (−10%)\n• Break either rule once → the account is closed and the fee is gone",
                      "• รายวัน: Equity ห้ามต่ำกว่ายอดต้นวันเกิน 5% ของทุนเริ่มต้น\n• รวม: Equity ห้ามต่ำกว่า 90% ของทุนเริ่มต้น (−10%)\n• ผิดกฎข้อใดครั้งเดียว → บัญชีถูกปิด ค่าธรรมเนียมหายไป"), 14, C["text"])
    s.text(48, 408, t("FTMO states that all its accounts are demo accounts with fictitious funds. The fee is refunded with the first payout.",
                      "FTMO ระบุว่าบัญชีทั้งหมดเป็นบัญชีเดโมที่ใช้เงินสมมติ ค่าธรรมเนียมคืนพร้อมการจ่ายกำไรครั้งแรก"), 12, C["dim"])
    return s.render()


@fig
def prop_rules(lang):
    t = tr(lang)
    s = SVG(960, 500, t("Static vs trailing loss limits", "เพดานขาดทุนแบบคงที่ กับแบบเลื่อนตาม"),
        t("Left: 100,000 account, static + daily floor. Right: 50,000 account, floor trails the best end-of-day balance.",
          "ซ้าย: บัญชี 100,000 พื้นคงที่ + พื้นรายวัน  ขวา: บัญชี 50,000 พื้นเลื่อนตามยอดปิดวันสูงสุด"))
    # left
    panel(s, 28, 96, 442, 370)
    s.text(48, 126, t("Static + daily (FTMO-style)", "คงที่ + รายวัน (แบบ FTMO)"), 15, C["amber"], weight=700)

    def YL(v):
        return 430 - (v - 88_000) / (108_000 - 88_000) * 270
    bals = [100_000, 101_500, 103_000, 104_000, 102_200, 104_800]
    xs = [80 + k * 70 for k in range(len(bals))]
    s.line(70, YL(90_000), 450, YL(90_000), C["bear"], 2, "7 5")
    s.text(448, YL(90_000) - 6, t("static floor 90,000", "พื้นคงที่ 90,000"), 12, C["bear"], "end", 700)
    for k in range(len(bals) - 1):
        fl = T.daily_floor(bals[k])
        s.line(xs[k], YL(fl), xs[k + 1], YL(fl), C["pink"], 2)
    s.text(60, YL(92_400), t(f"pink = daily floor. Day 3 starts at 104,000 → floor {fmt(T.daily_floor(104_000))}", f"สีชมพู = พื้นรายวัน วันที่ 3 เริ่มที่ 104,000 → พื้น {fmt(T.daily_floor(104_000))}"), 12, C["pink"])
    s.polyline(list(zip(xs, [YL(b) for b in bals])), C["blue"], 3)
    for x, b in zip(xs, bals):
        s.circle(x, YL(b), 4, C["blue"])
    for k, x in enumerate(xs):
        s.text(x, 452, t(f"d{k}", f"ว{k}"), 11, C["muted"], "middle")
    # right
    panel(s, 490, 96, 442, 370)
    s.text(510, 126, t("End-of-day trailing (Topstep-style)", "เลื่อนตามยอดปิดวัน (แบบ Topstep)"), 15, C["amber"], weight=700)
    eod = [50_000, 50_500, 50_000, 51_200, 52_300, 51_000]
    fl = [48_000] + T.trailing_mll(eod[1:])

    def YR(v):
        return 430 - (v - 47_500) / (53_000 - 47_500) * 270
    xr = [540 + k * 70 for k in range(len(eod))]
    s.polyline(list(zip(xr, [YR(v) for v in fl])), C["bear"], 2.5, "7 5")
    s.polyline(list(zip(xr, [YR(v) for v in eod])), C["blue"], 3)
    for x, b, f in zip(xr, eod, fl):
        s.circle(x, YR(b), 4, C["blue"])
        s.text(x, YR(f) + 18, fmt(f), 11, C["bear"], "middle")
    s.text(xr[4], YR(52_300) - 12, "52,300", 11, C["blue"], "middle", 700)
    s.text(xr[4] + 30, YR(50_000) - 30, t("floor locks at\n50,000", "พื้นล็อกที่\n50,000"), 12, C["bear"], "middle", 700)
    for k, x in enumerate(xr):
        s.text(x, 452, t(f"d{k}", f"ว{k}"), 11, C["muted"], "middle")
    s.text(40, 490, t("Profits raise a trailing floor but losses never lower it. Your real room to lose can shrink to almost nothing.",
                      "กำไรดันเส้นพื้นแบบเลื่อนตามขึ้น แต่ขาดทุนไม่เคยดันมันลง พื้นที่ให้ขาดทุนจริงจึงหดจนแทบไม่เหลือได้"), 12, C["dim"])
    return s.render()


@fig
def prop_sim(lang):
    t = tr(lang)
    s = SVG(960, 520, t("Chance of passing phase 1 (+10% before −10%), by risk per trade", "โอกาสผ่านเฟส 1 (+10% ก่อน −10%) ตามความเสี่ยงต่อเทรด"),
        t("20,000 simulated challenges per bar. 5% daily limit, up to 3 trades a day, no time limit.",
          "จำลอง 20,000 ครั้งต่อแท่ง เพดานขาดทุนรายวัน 5% เทรดไม่เกิน 3 ครั้งต่อวัน ไม่จำกัดเวลา"))
    panel(s, 28, 92, 904, 380)
    risks = [0.005, 0.01, 0.02, 0.03]
    edges = [("no edge after costs", t("Small negative edge\n(50% wins at 0.9R)", "ได้เปรียบติดลบเล็กน้อย\n(ชนะ 50% ที่ 0.9R)"), C["bear"]),
             ("zero edge", t("Zero edge\n(50% wins at 1R)", "ไม่มีความได้เปรียบ\n(ชนะ 50% ที่ 1R)"), C["muted"]),
             ("real edge", t("Real edge\n(45% wins at 2R)", "มีความได้เปรียบจริง\n(ชนะ 45% ที่ 2R)"), C["bull"])]
    base, sc = 420, 2.8
    for v in (25, 50, 75, 100):
        s.line(90, base - v * sc, 910, base - v * sc, C["grid"], 1)
        s.text(84, base - v * sc + 4, f"{v}%", 11, C["muted"], "end")
    s.line(90, base, 910, base, C["border"], 1.5)
    for g, rk in enumerate(risks):
        gx = 110 + g * 200
        for e, (key, _, col) in enumerate(edges):
            p, r = T.EDGES[key]
            pr, _ = T.simulate(p, r, rk)
            x = gx + e * 56
            s.rect(x, base - pr * 100 * sc, 46, pr * 100 * sc, fill=col, opacity=0.85, rx=3)
            s.text(x + 23, base - pr * 100 * sc - 6, f"{pr*100:.0f}%", 12, col, "middle", 700)
        s.text(gx + 79, base + 22, t(f"{rk*100:.1f}% risk", f"เสี่ยง {rk*100:.1f}%"), 13, C["text"], "middle", 700)
    for e, (_, lab, col) in enumerate(edges):
        s.rect(110 + e * 270, 480, 14, 14, fill=col, rx=3)
        s.text(132 + e * 270, 492, lab, 12, C["text"])
    return s.render()


@fig
def prop_funnel(lang):
    t = tr(lang)
    s = SVG(960, 470, t("What happens to 100 challenge buyers?", "เกิดอะไรขึ้นกับผู้ซื้อ Challenge 100 คน?"),
        t("Industry data: FPFX Technologies, 300,000+ accounts at 10 firms (reported Sep 2024).",
          "ข้อมูลอุตสาหกรรม: FPFX Technologies บัญชีกว่า 300,000 บัญชีจาก 10 บริษัท (รายงาน ก.ย. 2024)"))
    panel(s, 28, 92, 904, 340)
    stages = [(100, t("bought a challenge", "ซื้อ Challenge"), C["blue"]),
              (14, t("passed and got a\n\"funded\" account", "ผ่านและได้บัญชี\n\"Funded\""), C["amber"]),
              (7, t("ever received\na payout", "เคยได้รับ\nเงินจริง"), C["bull"])]
    for k, (n, lab, col) in enumerate(stages):
        x0 = 60 + k * 300
        for i in range(100):
            cx, cy = x0 + (i % 10) * 22, 120 + (i // 10) * 22
            s.circle(cx + 8, cy + 8, 7, col if i < n else C["grid"])
        s.text(x0 + 104, 360, f"{n}", 26, col, "middle", 700)
        if k < 2:
            s.arrow(x0 + 225, 220, x0 + 290, 220, C["muted"], 2)
    for k, (n, lab, col) in enumerate(stages):
        s.text(60 + k * 300 + 104, 408, lab, 13, C["text"], "middle")
    s.text(40, 452, t("Topstep's own disclosure for 2025: 16.8% of Combines passed; 33.3% of traders at the funded level received a payout.",
                      "ข้อมูลเปิดเผยของ Topstep ปี 2025: Combine ผ่าน 16.8% และเทรดเดอร์ระดับ Funded ได้รับเงิน 33.3%"), 12, C["dim"])
    return s.render()
