"""Phase 12 figures: History Lessons. All price data comes from _tools/history/data/ (see fetch_history.py)."""
import json
from pathlib import Path
from charts import SVG, CandleChart, C, tr

FIGURES = {}
DATA = Path(__file__).resolve().parents[1] / "history" / "data"


def fig(fn):
    FIGURES["p12-" + fn.__name__.replace("_", "-")] = fn
    return fn


def load(name):
    return json.loads((DATA / f"{name}.json").read_text(encoding="utf-8"))["rows"]


def sma(xs, n):
    return [None if i < n - 1 else sum(xs[i - n + 1:i + 1]) / n for i in range(len(xs))]


def panel(s, x, y, w, h):
    s.rect(x, y, w, h, fill=C["panel"], stroke=C["border"], rx=12)


def window(rows, a, b):
    return [r for r in rows if a <= r[0] <= b]


def month_labels(s, ch, rows, every=1, y=None, size=11):
    seen, k = set(), 0
    for i, r in enumerate(rows):
        m = r[0][:7]
        if m not in seen:
            seen.add(m)
            if k % every == 0:
                s.text(ch.X(i), y, m, size, C["muted"], "middle")
            k += 1


def mark(s, ch, i, price, text, col, dy=-14, anchor="middle", size=12, dx=0):
    s.circle(ch.X(i), ch.Y(price), 5, col)
    s.text(ch.X(i) + dx, ch.Y(price) + dy, text, size, col, anchor, 700)


def source_note(s, t, text_en, text_th, y):
    s.text(40, y, t(text_en, text_th), 11, C["dim"])


def bars(s, items, x0, base, sc, bw=110, gap=60, fmt="{:+.1f}%"):
    for k, (name, v, col) in enumerate(items):
        x = x0 + k * (bw + gap)
        h = v * sc
        s.rect(x, min(base, base - h), bw, max(abs(h), 2), fill=col, opacity=0.85, rx=4)
        s.text(x + bw / 2, base - h - 8 if v >= 0 else base - h + 20, fmt.format(v), 14, col, "middle", 700)
        s.text(x + bw / 2, base + 24 if v >= 0 else base + 24, name, 12, C["text"], "middle", 600)


# ---------------------------------------------------------------- 12.1 Black Monday 1987
@fig
def crash_1987(lang):
    t = tr(lang)
    allr = load("sp500_1987")
    s50a = sma([r[4] for r in allr], 50)
    rows = window(allr, "1987-08-01", "1987-12-31")
    off = allr.index(rows[0])
    s = SVG(960, 520, t("S&P 500, August–December 1987 (daily candles)", "S&P 500 สิงหาคม–ธันวาคม 1987 (แท่งเทียนรายวัน)"),
            t("Orange line: 50-day average. The trend had already turned weeks before Black Monday.",
              "เส้นส้ม: ค่าเฉลี่ย 50 วัน เทรนด์กลับตัวไปแล้วหลายสัปดาห์ก่อนแบล็กมันเดย์"))
    panel(s, 28, 86, 904, 400)
    ch = CandleChart(s, 60, 110, 850, 330, [r[1:5] for r in rows], pmin=200, pmax=350, grid=True)
    ch.draw(width=0.7)
    ch.path([(i, s50a[off + i]) for i in range(len(rows)) if s50a[off + i]], C["amber"], 2)
    d = [r[0] for r in rows]
    i = d.index("1987-08-25"); mark(s, ch, i, rows[i][4], t("peak 336.77 · 25 Aug", "ยอด 336.77 · 25 ส.ค."), C["bull"])
    i = d.index("1987-09-04"); mark(s, ch, i, rows[i][4], t("first close below 50-day avg · 4 Sep", "ปิดใต้ค่าเฉลี่ย 50 วันครั้งแรก · 4 ก.ย."), C["amber"], dy=30, anchor="start", dx=6)
    i = d.index("1987-10-16"); mark(s, ch, i, rows[i][4], t("Fri 16 Oct · 282.70", "ศุกร์ 16 ต.ค. · 282.70"), C["text"], dy=-16, anchor="end", dx=-8)
    i = d.index("1987-10-19"); mark(s, ch, i, rows[i][4], t("Mon 19 Oct · 224.84 (−20.5%)", "จันทร์ 19 ต.ค. · 224.84 (−20.5%)"), C["bear"], dy=24, anchor="start", dx=8)
    month_labels(s, ch, rows, y=462)
    source_note(s, t, "Data: Yahoo Finance ^GSPC daily (fetched Oct 2026).", "ข้อมูล: Yahoo Finance ^GSPC รายวัน (ดึงข้อมูล ต.ค. 2026)", 506)
    return s.render()


@fig
def traders_1987(lang):
    t = tr(lang)
    s = SVG(960, 470, t("19 October 1987: the same day, four traders (10,000 USD accounts)", "19 ตุลาคม 1987: วันเดียวกัน นักเทรดสี่คน (บัญชี 10,000 ดอลลาร์)"),
            t("Long S&P 500 exposure from Friday's close (282.70). Loss as % of the account (computed).",
              "ถือฝั่งซื้อ S&P 500 จากราคาปิดวันศุกร์ (282.70) ขาดทุนเป็น % ของบัญชี (คำนวณจริง)"))
    items = [(t("Trend filter:\nflat since 4 Sep", "ตัวกรองเทรนด์:\nไม่ถือตั้งแต่ 4 ก.ย."), 0.0, C["bull"]),
             (t("1% risk, stop 275,\nfilled at 260", "เสี่ยง 1% Stop 275\nได้ราคา 260"), -2.95, C["amber"]),
             (t("Same size,\nno stop", "ขนาดเดียวกัน\nไม่มี Stop"), -7.51, C["bear"]),
             (t("10× leverage,\nno stop", "เลเวอเรจ 10 เท่า\nไม่มี Stop"), -204.7, C["bear"])]
    base, sc = 150, 1.0
    s.line(60, base, 900, base, C["dim"], 1.5)
    for k, (name, v, col) in enumerate(items):
        x = 90 + k * 210
        h = min(abs(v), 250) * sc
        s.rect(x, base, 130, max(h, 2), fill=col, opacity=0.85, rx=4)
        s.text(x + 65, base + h + 22, f"{v:+.1f}%" if v else "0%", 15, col, "middle", 700)
        s.text(x + 65, base - 30, name, 12, C["text"], "middle", 600)
    s.text(90 + 3 * 210 + 65, base + 250 - 12, t("bar cut off", "แท่งถูกตัด"), 11, C["muted"], "middle")
    s.text(60, 440, t("Position for 1% risk: 100 ÷ (7.70 ÷ 282.70) ≈ 3,671 USD of index exposure. A gap or fast market fills stops late; leverage turns a bad day into ruin.",
                      "ขนาดสำหรับเสี่ยง 1%: 100 ÷ (7.70 ÷ 282.70) ≈ 3,671 ดอลลาร์ของดัชนี ตลาดที่เร็วหรือ Gap ทำให้ Stop ได้ราคาช้า เลเวอเรจเปลี่ยนวันแย่ให้เป็นพอร์ตพัง"), 12, C["amber"], weight=600)
    return s.render()


# ---------------------------------------------------------------- 12.2 2008
@fig
def crisis_2008(lang):
    t = tr(lang)
    allr = load("sp500_2008")
    s40a = sma([r[4] for r in allr], 40)
    rows = window(allr, "2007-06-01", "2009-12-31")
    off = allr.index(rows[0])
    s = SVG(960, 540, t("S&P 500, 2007–2009 (weekly candles)", "S&P 500 ปี 2007–2009 (แท่งเทียนรายสัปดาห์)"),
            t("Orange: 40-week average (≈ 200 days). Peak close 1,565.15 (9 Oct 2007) → low close 676.53 (9 Mar 2009): −56.8%.",
              "ส้ม: ค่าเฉลี่ย 40 สัปดาห์ (≈ 200 วัน) ปิดสูงสุด 1,565.15 (9 ต.ค. 2007) → ปิดต่ำสุด 676.53 (9 มี.ค. 2009): −56.8%"))
    panel(s, 28, 86, 904, 420)
    ch = CandleChart(s, 60, 110, 850, 350, [r[1:5] for r in rows], pmin=600, pmax=1650, grid=True)
    ch.draw(width=0.7)
    ch.path([(i, s40a[off + i]) for i in range(len(rows)) if s40a[off + i]], C["amber"], 2)
    d = [r[0] for r in rows]
    def at(date):
        return next(i for i, x in enumerate(d) if x >= date)
    evs = (("2007-10-08", t("peak close 1,565.15 · 9 Oct 2007", "ปิดสูงสุด 1,565.15 · 9 ต.ค. 2007"), C["bull"]),
           ("2007-11-05", t("first weekly close below the 40-week average", "ปิดรายสัปดาห์ใต้ค่าเฉลี่ย 40 สัปดาห์ครั้งแรก"), C["amber"]),
           ("2008-03-10", t("Bear Stearns rescued · Mar 2008", "ช่วยเหลือ Bear Stearns · มี.ค. 2008"), C["purple"]),
           ("2008-09-15", t("Lehman Brothers bankrupt · 15 Sep 2008", "Lehman Brothers ล้มละลาย · 15 ก.ย. 2008"), C["bear"]),
           ("2009-03-09", t("low close 676.53 · 9 Mar 2009", "ปิดต่ำสุด 676.53 · 9 มี.ค. 2009"), C["bear"]),
           ("2009-05-25", t("weekly close back above the average", "ปิดรายสัปดาห์กลับเหนือค่าเฉลี่ย"), C["amber"]))
    for k, (date, txt, col) in enumerate(evs):
        i = at(date)
        s.circle(ch.X(i), ch.Y(rows[i][4]), 9, col)
        s.text(ch.X(i), ch.Y(rows[i][4]) + 5, str(k + 1), 11, C["bg"], "middle", 800)
        s.text(560, 130 + k * 20, f"{k + 1} · {txt}", 12, col, weight=700)
    month_labels(s, ch, rows, every=6, y=482)
    source_note(s, t, "Data: Yahoo Finance ^GSPC weekly (fetched Oct 2026). Event dates: Wikipedia, Global financial crisis in September 2008.",
                "ข้อมูล: Yahoo Finance ^GSPC รายสัปดาห์ (ดึงข้อมูล ต.ค. 2026) วันที่ของเหตุการณ์: Wikipedia", 526)
    return s.render()


@fig
def filter_2008(lang):
    t = tr(lang)
    allr = load("sp500_2008")
    wc = [r[4] for r in allr]
    w40 = sma(wc, 40)
    start = next(i for i, r in enumerate(allr) if r[0] >= "2007-06-01")
    bh, fl, inm = [100.0], [100.0], wc[start - 1] > w40[start - 1]
    for i in range(start, len(allr)):
        ret = wc[i] / wc[i - 1] - 1
        bh.append(bh[-1] * (1 + ret))
        fl.append(fl[-1] * (1 + ret) if inm else fl[-1])
        inm = wc[i] > w40[i]
    s = SVG(960, 480, t("Buy & hold vs a simple trend filter, June 2007 – December 2009", "ซื้อแล้วถือ vs ตัวกรองเทรนด์ง่าย ๆ มิ.ย. 2007 – ธ.ค. 2009"),
            t("Start = 100. Filter: hold the index only while the weekly close is above its 40-week average (no costs, no dividends).",
              "เริ่ม = 100 ตัวกรอง: ถือดัชนีเฉพาะตอนราคาปิดรายสัปดาห์อยู่เหนือค่าเฉลี่ย 40 สัปดาห์ (ไม่รวมต้นทุนและปันผล)"))
    panel(s, 28, 86, 904, 360)
    X = lambda i: 70 + 840 * i / (len(bh) - 1)
    Y = lambda v: 110 + 300 * (115 - v) / 75
    for v in (40, 60, 80, 100):
        s.line(70, Y(v), 910, Y(v), C["grid"], 1)
        s.text(62, Y(v) + 4, str(v), 11, C["muted"], "end")
    s.polyline([(X(i), Y(v)) for i, v in enumerate(bh)], C["bear"], 2.5)
    s.polyline([(X(i), Y(v)) for i, v in enumerate(fl)], C["bull"], 2.5)

    def mdd(e):
        pk, m = e[0], 0
        for v in e:
            pk = max(pk, v)
            m = max(m, 1 - v / pk)
        return m * 100
    s.text(900, Y(55), t(f"buy & hold: end {bh[-1]:.1f}, worst drop −{mdd(bh):.1f}%", f"ซื้อแล้วถือ: จบ {bh[-1]:.1f} ร่วงหนักสุด −{mdd(bh):.1f}%"), 13, C["bear"], "end", 700)
    s.text(900, Y(fl[-1]) - 12, t(f"trend filter: end {fl[-1]:.1f}, worst drop −{mdd(fl):.1f}%", f"ตัวกรองเทรนด์: จบ {fl[-1]:.1f} ร่วงหนักสุด −{mdd(fl):.1f}%"), 13, C["bull"], "end", 700)
    s.text(40, 470, t("The filter switched 10 times in this window. It cut the crash, but in sideways markets the same rule loses on every false signal (see 12.5).",
                      "ตัวกรองสลับ 10 ครั้งในช่วงนี้ ช่วยลดการร่วงได้ แต่ในตลาดออกข้าง กฎเดียวกันขาดทุนทุกครั้งที่สัญญาณหลอก (ดู 12.5)"), 12, C["amber"], weight=600)
    return s.render()


# ---------------------------------------------------------------- 12.3 Swiss franc 2015
@fig
def chf_2015(lang):
    t = tr(lang)
    rows = load("eurchf_2015")
    s = SVG(960, 500, t("EUR/CHF, November 2014 – March 2015 (ECB daily reference rate)", "EUR/CHF พ.ย. 2014 – มี.ค. 2015 (อัตราอ้างอิงรายวันของ ECB)"),
            t("The SNB held a 1.20 floor from 6 Sep 2011. On 15 Jan 2015 it dropped it without warning.",
              "SNB รักษาระดับต่ำสุด 1.20 ตั้งแต่ 6 ก.ย. 2011 วันที่ 15 ม.ค. 2015 ยกเลิกโดยไม่แจ้งล่วงหน้า"))
    panel(s, 28, 86, 904, 380)
    x0, w, lo, hi = 70, 840, 0.80, 1.25
    X = lambda i: x0 + w * i / (len(rows) - 1)
    Y = lambda v: 110 + 320 * (hi - v) / (hi - lo)
    for v in (0.85, 0.95, 1.05, 1.15, 1.25):
        s.line(x0, Y(v), x0 + w, Y(v), C["grid"], 1)
        s.text(x0 - 8, Y(v) + 4, f"{v:.2f}", 11, C["muted"], "end")
    s.line(x0, Y(1.20), x0 + w, Y(1.20), C["amber"], 1.5, "6 4")
    s.text(x0 + 6, Y(1.20) - 8, t("SNB floor 1.20", "ระดับต่ำสุดของ SNB 1.20"), 12, C["amber"], weight=700)
    s.polyline([(X(i), Y(r[1])) for i, r in enumerate(rows)], C["blue"], 2.5)
    d = [r[0] for r in rows]
    i = d.index("2015-01-15")
    s.circle(X(i), Y(rows[i][1]), 6, C["bear"])
    s.text(X(i) + 10, Y(rows[i][1]) + 4, t(f"15 Jan fixing {rows[i][1]:.3f}", f"อัตราอ้างอิง 15 ม.ค. {rows[i][1]:.3f}"), 12, C["bear"], weight=700)
    s.line(X(i), Y(1.20), X(i), Y(0.85), C["bear"], 2, "3 3")
    s.circle(X(i), Y(0.85), 5, C["bear"])
    s.text(X(i) + 10, Y(0.85) + 4, t("intraday low ≈ 0.85 within minutes (≈ −30%)", "จุดต่ำระหว่างวัน ≈ 0.85 ภายในไม่กี่นาที (≈ −30%)"), 12, C["bear"], weight=700)
    for k, r in enumerate(rows):
        if r[0][8:10] in ("01", "02", "03") and (k == 0 or rows[k - 1][0][:7] != r[0][:7]):
            s.text(X(k), 452, r[0][:7], 11, C["muted"], "middle")
    source_note(s, t, "Daily data: Frankfurter / ECB reference rates (fetched Oct 2026). Intraday low: reports of 15 Jan 2015 (e.g. Forbes, CNBC).",
                "ข้อมูลรายวัน: Frankfurter / อัตราอ้างอิง ECB (ดึงข้อมูล ต.ค. 2026) จุดต่ำระหว่างวัน: รายงานข่าว 15 ม.ค. 2015", 488)
    return s.render()


@fig
def gap_2015(lang):
    t = tr(lang)
    s = SVG(960, 440, t("A 30-pip stop on EUR/CHF on 15 January 2015", "Stop 30 pip บน EUR/CHF วันที่ 15 มกราคม 2015"),
            t("Account 10,000 CHF, risk 1% = 100 CHF. Long 0.333 lots at 1.2010, stop 1.1980 (10 CHF per pip per lot).",
              "บัญชี 10,000 ฟรังก์ เสี่ยง 1% = 100 ฟรังก์ ซื้อ 0.333 ล็อตที่ 1.2010 Stop 1.1980 (10 ฟรังก์ต่อ pip ต่อล็อต)"))
    items = [(t("Planned loss\n(stop at 1.1980)", "ขาดทุนตามแผน\n(Stop ที่ 1.1980)"), 100, C["amber"]),
             (t("Filled near the\nday's fixing 1.028", "ได้ราคาใกล้อัตรา\nอ้างอิงของวัน 1.028"), 5767, C["bear"]),
             (t("Filled near the\nintraday low 0.85", "ได้ราคาใกล้จุดต่ำ\nระหว่างวัน 0.85"), 11700, C["bear"])]
    base, sc = 120, 0.022
    for k, (name, v, col) in enumerate(items):
        x = 120 + k * 260
        s.rect(x, base, 150, max(v * sc, 3), fill=col, opacity=0.85, rx=4)
        s.text(x + 75, base + v * sc + 22, f"−{v:,} CHF", 15, col, "middle", 700)
        s.text(x + 75, base - 24, name, 12, C["text"], "middle", 600)
    s.line(100, base + 10000 * sc, 900, base + 10000 * sc, C["text"], 1.5, "6 4")
    s.text(905, base + 10000 * sc + 4, t("whole account", "ทั้งบัญชี"), 11, C["text"], "end")
    s.text(40, 428, t("Brokers' own losses that day: Alpari UK declared insolvency, FXCM needed a rescue, Global Brokers NZ closed.",
                      "ความเสียหายของโบรกเกอร์เองวันนั้น: Alpari UK ประกาศล้มละลาย FXCM ต้องได้รับความช่วยเหลือ Global Brokers NZ ปิดกิจการ"), 12, C["amber"], weight=600)
    return s.render()


# ---------------------------------------------------------------- 12.4 COVID 2020
@fig
def covid_2020(lang):
    t = tr(lang)
    rows = load("sp500_2020")
    s = SVG(960, 520, t("S&P 500, January–September 2020 (daily candles)", "S&P 500 มกราคม–กันยายน 2020 (แท่งเทียนรายวัน)"),
            t("3,386.15 (19 Feb) → 2,237.40 (23 Mar): −33.9% in 23 trading days. Back to a record close on 18 Aug (3,389.78).",
              "3,386.15 (19 ก.พ.) → 2,237.40 (23 มี.ค.): −33.9% ใน 23 วันทำการ กลับไปปิดสูงสุดใหม่ 18 ส.ค. (3,389.78)"))
    panel(s, 28, 86, 904, 400)
    ch = CandleChart(s, 60, 110, 850, 330, [r[1:5] for r in rows], pmin=2100, pmax=3650, grid=True)
    ch.draw(width=0.7)
    d = [r[0] for r in rows]
    i = d.index("2020-02-19"); mark(s, ch, i, rows[i][4], t("peak · 19 Feb", "ยอด · 19 ก.พ."), C["bull"])
    for k, date in enumerate(("2020-03-09", "2020-03-12", "2020-03-16", "2020-03-18")):
        i = d.index(date)
        s.text(ch.X(i), ch.Y(rows[i][2]) - 10, "⚡", 14, C["amber"], "middle")
    s.text(ch.X(d.index("2020-03-12")) + 12, 140, t("⚡ circuit breakers: 9, 12, 16, 18 Mar", "⚡ เบรกเกอร์หยุดซื้อขาย: 9, 12, 16, 18 มี.ค."), 12, C["amber"], "start", 700)
    i = d.index("2020-03-23"); mark(s, ch, i, rows[i][4], t("low · 23 Mar", "ต่ำสุด · 23 มี.ค."), C["bear"], dy=26)
    i = d.index("2020-08-18"); mark(s, ch, i, rows[i][4], t("new record · 18 Aug", "สูงสุดใหม่ · 18 ส.ค."), C["bull"], dy=-16, anchor="end", dx=-6)
    month_labels(s, ch, rows, y=462)
    source_note(s, t, "Data: Yahoo Finance ^GSPC daily (fetched Oct 2026). Circuit-breaker dates: Wikipedia, 2020 stock market crash.",
                "ข้อมูล: Yahoo Finance ^GSPC รายวัน (ดึงข้อมูล ต.ค. 2026) วันที่เบรกเกอร์: Wikipedia", 506)
    return s.render()


@fig
def rebalance_2020(lang):
    t = tr(lang)
    g = 3389.78 / 2237.40
    st0, bd = 600000.0, 400000.0
    st1 = st0 * 2237.40 / 3386.15
    tot = st1 + bd
    buy = 0.6 * tot - st1
    withr = (st1 + buy) * g + (bd - buy)
    without = st1 * g + bd
    s = SVG(960, 460, t("An IPS rebalance in March 2020 (60/40, illustrative)", "การปรับสมดุลตาม IPS ในมีนาคม 2020 (60/40 ตัวอย่าง)"),
            t("1,000,000 THB at 60/40. Stocks follow the S&P 500 path; bonds held flat for simplicity.",
              "1,000,000 บาทที่ 60/40 หุ้นเดินตามเส้นทาง S&P 500 พันธบัตรสมมติให้คงที่เพื่อความง่าย"))
    items = [(t("19 Feb\nstart", "19 ก.พ.\nเริ่ม"), 1000000, C["blue"]), (t("23 Mar\nafter the fall", "23 มี.ค.\nหลังร่วง"), tot, C["bear"]),
             (t("18 Aug\nno rebalance", "18 ส.ค.\nไม่ปรับสมดุล"), without, C["muted"]), (t("18 Aug\nrebalanced on 23 Mar", "18 ส.ค.\nปรับสมดุลวันที่ 23 มี.ค."), withr, C["bull"])]
    base, sc = 380, 0.00026
    for k, (name, v, col) in enumerate(items):
        x = 90 + k * 210
        s.rect(x, base - v * sc, 130, v * sc, fill=col, opacity=0.85, rx=4)
        s.text(x + 65, base - v * sc - 10, f"{v:,.0f}", 14, col, "middle", 700)
        s.text(x + 65, base + 22, name, 12, C["text"], "middle", 600)
    s.text(40, 446, t(f"After the fall stocks were {st1 / tot:.1%} of the portfolio; the rule bought {buy:,.0f} THB of stocks. By 18 Aug that added {withr - without:,.0f} THB ({(withr / without - 1) * 100:.1f}%).",
                      f"หลังร่วง หุ้นเหลือ {st1 / tot:.1%} ของพอร์ต กฎสั่งให้ซื้อหุ้น {buy:,.0f} บาท ถึง 18 ส.ค. ได้เพิ่ม {withr - without:,.0f} บาท ({(withr / without - 1) * 100:.1f}%)"), 12, C["amber"], weight=600)
    return s.render()


# ---------------------------------------------------------------- 12.5 2022 rate shock
@fig
def rates_2022(lang):
    t = tr(lang)
    allr = load("sp500_2022")
    s40a = sma([r[4] for r in allr], 40)
    rows = window(allr, "2021-10-01", "2023-01-31")
    off = allr.index(rows[0])
    ty = {r[0]: r[4] for r in load("us10y_2022")}
    s = SVG(960, 600, t("2022: stocks and bonds fell together as the Fed hiked", "2022: หุ้นและพันธบัตรร่วงพร้อมกันขณะที่ Fed ขึ้นดอกเบี้ย"),
            t("Top: S&P 500 weekly, 40-week average. Bottom: US 10-year yield. Dashes: the seven 2022 Fed hikes.",
              "บน: S&P 500 รายสัปดาห์ ค่าเฉลี่ย 40 สัปดาห์ ล่าง: ผลตอบแทนพันธบัตรสหรัฐ 10 ปี เส้นประ: Fed ขึ้นดอกเบี้ยเจ็ดครั้งในปี 2022"))
    panel(s, 28, 86, 904, 480)
    ch = CandleChart(s, 60, 110, 850, 270, [r[1:5] for r in rows], pmin=3400, pmax=4900, grid=True)
    ch.draw(width=0.7)
    ch.path([(i, s40a[off + i]) for i in range(len(rows)) if s40a[off + i]], C["amber"], 2)
    d = [r[0] for r in rows]
    hikes = [("2022-03-16", "+0.25"), ("2022-05-04", "+0.50"), ("2022-06-15", "+0.75"), ("2022-07-27", "+0.75"),
             ("2022-09-21", "+0.75"), ("2022-11-02", "+0.75"), ("2022-12-14", "+0.50")]
    for date, sz in hikes:
        i = next(k for k, x in enumerate(d) if x >= date) - 1
        s.line(ch.X(i), 110, ch.X(i), 530, C["purple"], 1, "3 4")
        s.text(ch.X(i), 396, sz, 10, C["purple"], "middle", 700)
    i = next(k for k, x in enumerate(d) if x >= "2021-12-27"); mark(s, ch, i, rows[i][4], t("record 4,796.56 · 3 Jan", "สูงสุด 4,796.56 · 3 ม.ค."), C["bull"])
    i = next(k for k, x in enumerate(d) if x >= "2022-10-10"); mark(s, ch, i, rows[i][3], t("low close 3,577.03 · 12 Oct (−25.4%)", "ปิดต่ำสุด 3,577.03 · 12 ต.ค. (−25.4%)"), C["bear"], dy=24, anchor="end", dx=-8)
    yv = [ty.get(r[0]) for r in rows]
    Y2 = lambda v: 530 - 110 * (v - 1.0) / 3.5
    for v in (1.5, 2.5, 3.5, 4.5):
        s.line(60, Y2(v), 910, Y2(v), C["grid"], 1)
        s.text(52, Y2(v) + 4, f"{v}%", 10, C["muted"], "end")
    s.polyline([(ch.X(i), Y2(v)) for i, v in enumerate(yv) if v], C["blue"], 2.5)
    s.text(70, 420, t("US 10-year yield: about 1.5% → 4.2%", "ผลตอบแทน 10 ปีสหรัฐ: ราว 1.5% → 4.2%"), 12, C["blue"], weight=700)
    month_labels(s, ch, rows, every=3, y=548)
    source_note(s, t, "Data: Yahoo Finance ^GSPC, ^TNX weekly (fetched Oct 2026). Hike dates/sizes: FOMC decisions 2022.",
                "ข้อมูล: Yahoo Finance ^GSPC, ^TNX รายสัปดาห์ (ดึงข้อมูล ต.ค. 2026) วันที่และขนาดการขึ้นดอกเบี้ย: มติ FOMC ปี 2022", 590)
    return s.render()


@fig
def portfolio_2022(lang):
    t = tr(lang)
    s = SVG(960, 440, t("2022 calendar-year returns: no place to hide", "ผลตอบแทนตลอดปี 2022: ไม่มีที่หลบ"),
            t("Index returns as reported; the 60/40 line is a simple weighted mix (illustrative, no rebalancing).",
              "ผลตอบแทนดัชนีตามที่รายงาน เส้น 60/40 คือค่าเฉลี่ยถ่วงน้ำหนักอย่างง่าย (ตัวอย่าง ไม่ปรับสมดุล)"))
    items = [(t("S&P 500\n(price)", "S&P 500\n(ราคา)"), -19.4, C["bear"]), (t("US bonds\n(Bloomberg Agg)", "พันธบัตรสหรัฐ\n(Bloomberg Agg)"), -13.0, C["bear"]),
             (t("60/40 mix", "พอร์ต 60/40"), -16.8, C["amber"])]
    base, sc = 140, 11
    for k, (name, v, col) in enumerate(items):
        x = 150 + k * 250
        s.rect(x, base, 140, -v * sc, fill=col, opacity=0.85, rx=4)
        s.text(x + 70, base - v * sc + 22, f"{v:+.1f}%", 15, col, "middle", 700)
        s.text(x + 70, base - 24, name, 12, C["text"], "middle", 600)
    s.text(40, 412, t("0.6 × (−19.4%) + 0.4 × (−13.0%) = −16.8%. The bond index had its worst year since its start in 1976.",
                      "0.6 × (−19.4%) + 0.4 × (−13.0%) = −16.8% ดัชนีพันธบัตรมีปีที่แย่ที่สุดนับตั้งแต่เริ่มในปี 1976"), 12, C["amber"], weight=600)
    s.text(40, 432, t("Sources: Yahoo Finance year-end report (S&P 500 −19.4%); A Wealth of Common Sense, Jan 2023 (Agg −13%).",
                      "ที่มา: รายงานสิ้นปีของ Yahoo Finance (S&P 500 −19.4%) A Wealth of Common Sense ม.ค. 2023 (Agg −13%)"), 11, C["dim"])
    return s.render()


# ---------------------------------------------------------------- 12.6 FTX
@fig
def ftx_2022(lang):
    t = tr(lang)
    btc = load("btc_2022")
    ftt = {r[0]: r[4] for r in load("ftt_2022")}
    s = SVG(960, 560, t("FTX, November 2022: Bitcoin (daily candles) and FTX's own token FTT", "FTX พฤศจิกายน 2022: Bitcoin (แท่งรายวัน) และโทเคน FTT ของ FTX เอง"),
            t("Top: BTC/USDT. Bottom: FTT/USDT closing price. Events from the bankruptcy timeline.",
              "บน: BTC/USDT ล่าง: ราคาปิด FTT/USDT เหตุการณ์จากลำดับเวลาการล้มละลาย"))
    panel(s, 28, 86, 904, 440)
    ch = CandleChart(s, 60, 110, 850, 230, [r[1:5] for r in btc], pmin=15000, pmax=21800, grid=True)
    ch.draw(width=0.7)
    d = [r[0] for r in btc]
    events = [("2022-11-02", t("2 Nov · CoinDesk report", "2 พ.ย. · รายงานของ CoinDesk")), ("2022-11-06", t("6 Nov · Binance to sell FTT", "6 พ.ย. · Binance จะขาย FTT")),
              ("2022-11-08", t("8 Nov · withdrawals, rescue deal", "8 พ.ย. · แห่ถอน ข้อตกลงช่วยเหลือ")), ("2022-11-11", t("11 Nov · bankruptcy", "11 พ.ย. · ล้มละลาย"))]
    for k, (date, txt) in enumerate(events):
        i = d.index(date)
        s.line(ch.X(i), 118, ch.X(i), 500, C["purple"], 1, "3 4")
        s.circle(ch.X(i), 116, 8, C["purple"])
        s.text(ch.X(i), 120, str(k + 1), 10, C["bg"], "middle", 800)
        s.text(600, 130 + k * 18, f"{k + 1} · {txt}", 12, C["purple"], "start", 700)
    i = d.index("2022-11-05"); mark(s, ch, i, btc[i][4], t("BTC 21,299 · 5 Nov", "BTC 21,299 · 5 พ.ย."), C["text"], dy=26, anchor="end", dx=-14)
    i = d.index("2022-11-21"); mark(s, ch, i, btc[i][3], t("low 15,476 · 21 Nov", "ต่ำสุด 15,476 · 21 พ.ย."), C["bear"], dy=22)
    Y2 = lambda v: 500 - 130 * v / 26
    for v in (0, 10, 20):
        s.line(60, Y2(v), 910, Y2(v), C["grid"], 1)
        s.text(52, Y2(v) + 4, f"${v}", 10, C["muted"], "end")
    pts = [(ch.X(k), Y2(ftt[r[0]])) for k, r in enumerate(btc) if r[0] in ftt]
    s.polyline(pts, C["amber"], 2.5)
    s.text(520, 430, t("FTT: 24.08 (5 Nov) → 2.27 (9 Nov, −90.6%) → 1.43 (15 Nov)", "FTT: 24.08 (5 พ.ย.) → 2.27 (9 พ.ย., −90.6%) → 1.43 (15 พ.ย.)"), 12, C["amber"], weight=700)
    month_labels(s, ch, btc, y=516)
    source_note(s, t, "Data: Binance public API, BTCUSDT and FTTUSDT daily (fetched Oct 2026). Events: Wikipedia, Bankruptcy of FTX.",
                "ข้อมูล: Binance public API, BTCUSDT และ FTTUSDT รายวัน (ดึงข้อมูล ต.ค. 2026) เหตุการณ์: Wikipedia", 548)
    return s.render()


@fig
def custody_ftx(lang):
    t = tr(lang)
    s = SVG(960, 420, t("1 BTC on FTX vs 1 BTC in your own wallet", "1 BTC บน FTX vs 1 BTC ในกระเป๋าของคุณเอง"),
            t("FTX claims were valued in US dollars at the bankruptcy date (11 Nov 2022 close: 17,070 USD per BTC).",
              "สิทธิเรียกร้องของ FTX คิดเป็นดอลลาร์ ณ วันล้มละลาย (ราคาปิด 11 พ.ย. 2022: 17,070 ดอลลาร์ต่อ BTC)"))
    s.card(40, 110, 420, 250, t("On the exchange (FTX)", "บนกระดานเทรด (FTX)"),
           t("Withdrawals frozen 9 Nov 2022.\nYou become an unsecured creditor.\nEstimated recovery 118–142% of the\npetition-date dollar value:\n17,070 × 1.18 = 20,143 USD\n17,070 × 1.42 = 24,240 USD\nPaid in dollars, years later; no BTC.",
             "ถอนไม่ได้ตั้งแต่ 9 พ.ย. 2022\nคุณกลายเป็นเจ้าหนี้ไม่มีหลักประกัน\nคาดว่าได้คืน 118–142% ของมูลค่า\nดอลลาร์ ณ วันยื่นล้มละลาย:\n17,070 × 1.18 = 20,143 ดอลลาร์\n17,070 × 1.42 = 24,240 ดอลลาร์\nได้เป็นดอลลาร์ หลายปีต่อมา ไม่ได้ BTC"), C["bear"], 17, 14)
    s.card(500, 110, 420, 250, t("In your own wallet", "ในกระเป๋าของคุณเอง"),
           t("Nobody can freeze it.\nPrice still fell with the market\n(−25% in the week), but you kept\nthe coin and full control.\nRisk moves to you: lose the seed\nphrase and the coin is gone.",
             "ไม่มีใครระงับได้\nราคายังร่วงตามตลาด\n(−25% ในสัปดาห์นั้น) แต่คุณยังมี\nเหรียญและควบคุมได้เต็มที่\nความเสี่ยงย้ายมาที่คุณ: ทำ Seed\nphrase หายก็เสียเหรียญไป"), C["bull"], 17, 14)
    s.text(40, 400, t("Source for recovery estimate: FTX CEO John J. Ray III, as reported (Wikipedia, Bankruptcy of FTX).",
                      "ที่มาของการประมาณการคืนเงิน: CEO ของ FTX John J. Ray III ตามที่รายงาน (Wikipedia)"), 11, C["dim"])
    return s.render()


# ---------------------------------------------------------------- 12.7 SVB
@fig
def svb_2023(lang):
    t = tr(lang)
    rows = load("kre_2023")
    s = SVG(960, 520, t("US regional banks after SVB (KRE ETF, daily candles)", "ธนาคารระดับภูมิภาคสหรัฐหลัง SVB (ETF KRE แท่งรายวัน)"),
            t("SVB's own shares fell 60% on 9 March 2023 and stopped trading; KRE shows how the fear spread.",
              "หุ้นของ SVB ร่วง 60% วันที่ 9 มีนาคม 2023 และหยุดซื้อขาย KRE แสดงว่าความกลัวลามไปอย่างไร"))
    panel(s, 28, 86, 904, 400)
    ch = CandleChart(s, 60, 110, 850, 330, [r[1:5] for r in rows], pmin=33, pmax=66, grid=True)
    ch.draw(width=0.7)
    d = [r[0] for r in rows]
    evs = (("2023-03-08", t("8 Mar · SVB reports a 1.8 bn loss, plans a capital raise", "8 มี.ค. · SVB รายงานขาดทุน 1.8 พันล้าน วางแผนเพิ่มทุน"), C["amber"]),
           ("2023-03-09", t("9 Mar · SVB shares −60%; 42 bn USD withdrawals attempted", "9 มี.ค. · หุ้น SVB −60% ลูกค้าพยายามถอน 42 พันล้านดอลลาร์"), C["bear"]),
           ("2023-03-10", t("10 Mar · regulators close SVB (FDIC receivership)", "10 มี.ค. · ทางการปิด SVB (FDIC เข้าควบคุม)"), C["bear"]),
           ("2023-03-13", t("12–13 Mar · all deposits guaranteed; BTFP launched", "12–13 มี.ค. · ค้ำประกันเงินฝากทั้งหมด เปิด BTFP"), C["purple"]),
           ("2023-05-01", t("1 May · First Republic seized", "1 พ.ค. · ยึด First Republic"), C["bear"]))
    for k, (date, txt, col) in enumerate(evs):
        i = d.index(date)
        s.circle(ch.X(i), ch.Y(rows[i][4]), 9, col)
        s.text(ch.X(i), ch.Y(rows[i][4]) + 4, str(k + 1), 10, C["bg"], "middle", 800)
        s.text(400, 130 + k * 19, f"{k + 1} · {txt}", 12, col, weight=700)
    month_labels(s, ch, rows, y=462)
    source_note(s, t, "Data: Yahoo Finance KRE daily (fetched Oct 2026). Events: Wikipedia, Collapse of Silicon Valley Bank; CNBC 9 Mar 2023.",
                "ข้อมูล: Yahoo Finance KRE รายวัน (ดึงข้อมูล ต.ค. 2026) เหตุการณ์: Wikipedia, CNBC 9 มี.ค. 2023", 506)
    return s.render()


@fig
def bank_run(lang):
    t = tr(lang)
    s = SVG(960, 460, t("How rising rates and uninsured deposits broke SVB", "ดอกเบี้ยขาขึ้นและเงินฝากที่ไม่ได้รับการคุ้มครองทำให้ SVB พังได้อย่างไร"),
            t("Bond maths (computed) and SVB's reported balance sheet (Wikipedia, Collapse of Silicon Valley Bank).",
              "คณิตศาสตร์พันธบัตร (คำนวณจริง) และงบดุลที่รายงานของ SVB (Wikipedia)"))
    steps = [(t("1 · Deposits flood in (2020–21)", "1 · เงินฝากไหลเข้า (2020–21)"), t("Tech start-ups park cash at SVB.\n~89% of deposits above the\n250,000 USD insurance limit.", "สตาร์ตอัปเทคฝากเงินที่ SVB\n~89% ของเงินฝากเกินวงเงิน\nคุ้มครอง 250,000 ดอลลาร์"), C["blue"]),
             (t("2 · Bought long bonds at low yields", "2 · ซื้อพันธบัตรยาวตอนดอกเบี้ยต่ำ"), t("A 10-year 1.5% bond is worth\n79.72 when yields reach 4%\n(−20%). Unrealised losses on\nheld-to-maturity bonds > 15 bn USD.", "พันธบัตร 10 ปี คูปอง 1.5% มีค่า\n79.72 เมื่อผลตอบแทนเป็น 4%\n(−20%) ขาดทุนที่ยังไม่รับรู้ใน\nพันธบัตรถือจนครบกำหนด > 15 พันล้านดอลลาร์"), C["amber"]),
             (t("3 · Forced to sell, run starts", "3 · ถูกบังคับขาย เกิดการแห่ถอน"), t("8 Mar: sells bonds at a 1.8 bn loss.\n9 Mar: customers try to pull\n42 bn USD in one day.\n10 Mar: closed by regulators.", "8 มี.ค.: ขายพันธบัตรขาดทุน 1.8 พันล้าน\n9 มี.ค.: ลูกค้าพยายามถอน\n42 พันล้านดอลลาร์ในวันเดียว\n10 มี.ค.: ถูกทางการปิด"), C["bear"])]
    for k, (head, body, col) in enumerate(steps):
        x = 30 + k * 310
        s.card(x, 100, 290, 250, head, body, col, 15, 13)
    s.text(40, 392, t("Deposit insurance limits: US FDIC 250,000 USD per depositor per bank; Thailand DPA 1,000,000 THB per depositor per bank (since 11 Aug 2021).",
                      "วงเงินคุ้มครองเงินฝาก: FDIC สหรัฐ 250,000 ดอลลาร์ต่อผู้ฝากต่อธนาคาร ไทย สคฝ. 1,000,000 บาทต่อผู้ฝากต่อสถาบัน (ตั้งแต่ 11 ส.ค. 2021)"), 12, C["amber"], weight=600)
    s.text(40, 414, t("On 12 March 2023 regulators guaranteed all SVB deposits anyway, using a systemic-risk exception: a rescue you can't count on.",
                      "วันที่ 12 มีนาคม 2023 ทางการค้ำประกันเงินฝากทั้งหมดของ SVB โดยใช้ข้อยกเว้นความเสี่ยงเชิงระบบ: การช่วยเหลือที่คุณนับเป็นหลักประกันไม่ได้"), 12, C["muted"])
    return s.render()


# ---------------------------------------------------------------- 12.8 summary
@fig
def history_summary(lang):
    t = tr(lang)
    s = SVG(960, 520, t("Seven events, one lesson: survive first", "เจ็ดเหตุการณ์ บทเรียนเดียว: ต้องรอดก่อน"),
            t("Peak-to-trough falls in the case studies (each from its lesson; different assets and time spans).",
              "การร่วงจากจุดสูงสุดถึงต่ำสุดในกรณีศึกษา (จากแต่ละบท สินทรัพย์และช่วงเวลาต่างกัน)"))
    items = [(t("1987 · S&P 500", "1987 · S&P 500"), 33.5, t("record again Jul 1989", "สูงสุดใหม่ ก.ค. 1989")),
             (t("2008 · S&P 500", "2008 · S&P 500"), 56.8, t("record again Mar 2013", "สูงสุดใหม่ มี.ค. 2013")),
             (t("2015 · EUR/CHF intraday", "2015 · EUR/CHF ระหว่างวัน"), 30.0, t("in minutes", "ในไม่กี่นาที")),
             (t("2020 · S&P 500", "2020 · S&P 500"), 33.9, t("record again Aug 2020", "สูงสุดใหม่ ส.ค. 2020")),
             (t("2022 · S&P 500", "2022 · S&P 500"), 25.4, t("record again Jan 2024", "สูงสุดใหม่ ม.ค. 2024")),
             (t("2022 · FTT token", "2022 · โทเคน FTT"), 94.1, t("did not recover", "ไม่ฟื้นกลับมา")),
             (t("2023 · KRE banks ETF", "2023 · ETF ธนาคาร KRE"), 37.5, t("to 4 May 2023", "ถึง 4 พ.ค. 2023"))]
    for k, (name, v, note) in enumerate(items):
        y = 104 + k * 54
        s.text(250, y + 24, name, 13, C["text"], "end", 600)
        s.rect(262, y + 6, v * 5, 30, fill=C["bear"], opacity=0.8, rx=4)
        s.text(270 + v * 5, y + 27, f"−{v:.1f}%  · " + note, 13, C["bear"], weight=700)
    s.text(40, 500, t("Common thread: small risk per trade, real stops, no borrowed money, money you control, and a written plan kept people in the game.",
                      "สิ่งที่เหมือนกัน: ความเสี่ยงต่อไม้เล็ก Stop จริง ไม่ใช้เงินกู้ เงินที่คุณควบคุมได้ และแผนที่เขียนไว้ ทำให้คนยังอยู่ในเกม"), 12, C["amber"], weight=600)
    return s.render()
