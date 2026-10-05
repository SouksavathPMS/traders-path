"""B7 · v2 upgrade of 9.1 Statistics for Traders (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("09 Quant & Data Analysis/9.1 Statistics for Traders.md")

OUTPUT = """```
trades (R): [2.0, -1.0, 0.5, -1.0, 3.0, -1.0, 1.5, -0.5, -1.0, 2.5]
trades 10  win rate 50%  total +5.0R
mean +0.50R  median +0.00R  sd 1.62R
uncertainty of mean (sd/sqrt n) 0.51R  -> 95% range -0.50R to +1.50R
avg win +1.90R  avg loss -0.90R  profit factor 2.11
Sharpe-like (per trade) 0.31  Sortino-like (per trade) 0.77
equity curve (R): [2.0, 1.0, 1.5, 0.5, 3.5, 2.5, 4.0, 3.5, 2.5, 5.0]
max drawdown 1.5R
```"""

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> After ten trades you want to know: am I any good? Statistics gives you a few simple numbers to answer honestly. The **average** says what a typical trade earned. The **middle value** says what a "normal" trade looked like. The **spread** says how much results jump around. And the **sample size** says how much you can trust any of it. With only a handful of trades, luck can make anyone look brilliant or hopeless.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **R-multiple (R)** — a trade's result divided by the amount risked at the stop *(see 3.3)*.
> - **Mean (average)** — the sum of the results divided by how many there are.
> - **Median** — the middle result when they're sorted; not pulled by extreme values.
> - **SD / σ (standard deviation)** — how far results typically are from the mean *(see 6.6)*.
> - **Distribution / histogram** — how often each result occurs / a bar chart of that.
> - **Skew** — lopsidedness: negative skew = rare big losses; positive = rare big wins.
> - **Kurtosis / fat tails** — how often extreme results happen compared with a bell curve.
> - **Sample size (n)** — the number of trades or days measured.
> - **Standard error** — the uncertainty of an average: SD ÷ √n.
> - **95% range (confidence interval)** — the range that would contain the true value about 95% of the time.
> - **Correlation** — how much two series move together (from −1 to +1).
> - **Causation** — one thing actually causing another.
""")
L.before_heading("en", "2.", """
![[p9-ten-trades.en.svg]]

> [!walkthrough] Step by step: ten trades by hand
> Results in R: **+2, −1, +0.5, −1, +3, −1, +1.5, −0.5, −1, +2.5**.
> 1. **Mean:** sum = +5.0R → 5.0 ÷ 10 = **+0.50R** per trade.
> 2. **Median:** sorted: −1, −1, −1, −1, −0.5, +0.5, +1.5, +2, +2.5, +3. The middle two are −0.5 and +0.5 → (−0.5 + 0.5) ÷ 2 = **0R**.
> 3. **Distances from the mean:** +1.5, −1.5, 0, −1.5, +2.5, −1.5, +1.0, −1.0, −1.5, +2.0.
> 4. **Squares:** 2.25, 2.25, 0, 2.25, 6.25, 2.25, 1, 1, 2.25, 4 → sum **23.5**. Divide by n − 1 = 9 → 2.61. Square root → **SD ≈ 1.62R**.
> 5. **Win rate:** 5 winners of 10 = **50%**.
> 6. **So what?** The mean is positive, but the median is zero: the "typical" trade earns nothing, and three or four big winners carry the whole result. That's normal for trend-style trading, and it means skipping a few trades can destroy the edge.

> [!analogy]
> Mean vs median is like **average income in a village** where one person is a millionaire: the average looks rich, but the middle household is ordinary. Your trading average can be pulled up the same way by one or two huge winners.
>
> **Where it breaks:** a village's millionaire stays rich. In trading, you never know in advance which trade will be the big one, so you have to take them all.

> [!check]- Check your understanding: describing results
> **Q1.** Five trades: +1, +1, +1, +1, −6. What are the mean and the median, and what does the difference tell you?
> > [!answer]-
> > Mean = −2 ÷ 5 = −0.4R; median = +1R. Most trades win small, but one big loss wipes them out: negative skew, typical of strategies without tight stops.
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: how sure can you be after 10 trades?
> 1. **Uncertainty of the mean (standard error)** = SD ÷ √n = 1.62 ÷ √10 = 1.62 ÷ 3.16 ≈ **0.51R**.
> 2. **95% range** ≈ mean ± 1.96 × 0.51 = 0.50 ± 1.0 → **−0.50R to +1.50R**.
> 3. **Win rate range** at 50% with 20 trades: 1.96 × √(0.5 × 0.5 ÷ 20) ≈ 0.22 → **28% to 72%**. With 100 trades: ± 0.098 → **40% to 60%**.
> 4. **So what?** After ten trades the true average could be negative. You can't yet tell skill from luck, so keep the size small and keep collecting trades.

The same numbers come out of a short script in the vault, so you can check your own trades:

```bash
python3 _tools/quant/ten_trades.py                    # the ten trades above
python3 _tools/quant/ten_trades.py 1.5 -1 2 -1 0.5    # your own R-multiples
```

Real output for the ten trades:

""" + OUTPUT + """

> [!check]- Check your understanding: sample size
> **Q1.** A strategy has mean +0.4R and SD 2R over 25 trades. Is the average clearly above zero?
> > [!answer]-
> > Standard error = 2 ÷ √25 = 0.4R; 95% range ≈ 0.4 ± 0.78 → −0.38R to +1.18R. Not yet clearly above zero.
""")
L.before_callout("en", "example", """
> [!check]- Check your understanding: correlation
> **Q1.** Over the last year, Bitcoin and a tech stock rose and fell together almost every day. Can you hedge one with the other next year?
> > [!answer]-
> > Not safely. Correlation describes the past and can change, often in a crisis exactly when you need it. It also doesn't mean one causes the other.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** majors have relatively thin tails day to day, but central-bank surprises create rare huge moves *(see 0.3)*.
> - **Gold:** fat tails around US data and crises; in mid-2026 its average daily move was about 1.1% *(see 0.4, 0.7)*.
> - **Stocks:** single stocks have very fat tails on earnings days (gaps of 10–20%) *(see 0.5)*.
> - **Crypto:** the fattest tails of all; 10%+ days happen several times a year *(see 0.7)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Why is the median sometimes more useful than the mean for describing trades?
> > [!answer]-
> > Because a few extreme results pull the mean but not the median; the median shows what a normal trade looks like.
> **Q2.** How many trades do you need before the 95% range of a 50% win rate is narrower than ±10 percentage points?
> > [!answer]-
> > About 100 (1.96 × √(0.25 ÷ 100) ≈ 0.098).
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> หลังเทรดสิบไม้ คุณอยากรู้ว่า: ฉันเก่งไหม? สถิติให้ตัวเลขง่าย ๆ ไม่กี่ตัวเพื่อตอบอย่างซื่อสัตย์ **ค่าเฉลี่ย** บอกว่าไม้ทั่วไปได้เท่าไหร่ **ค่ากลาง** บอกว่าไม้ "ปกติ" หน้าตาเป็นอย่างไร **การกระจาย** บอกว่าผลแกว่งมากแค่ไหน และ **ขนาดตัวอย่าง** บอกว่าคุณเชื่อตัวเลขเหล่านี้ได้แค่ไหน ถ้ามีแค่ไม่กี่ไม้ โชคทำให้ใครก็ดูเก่งมากหรือแย่มากได้
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **R-multiple (R)** — ผลของไม้หารด้วยเงินที่เสี่ยงไว้ที่ Stop *(ดู 3.3)*
> - **ค่าเฉลี่ย (Mean / Average)** — ผลรวมหารด้วยจำนวนผล
> - **มัธยฐาน (Median)** — ผลที่อยู่ตรงกลางเมื่อเรียงลำดับ ไม่ถูกค่าสุดขั้วดึง
> - **SD / σ (ส่วนเบี่ยงเบนมาตรฐาน)** — ผลมักห่างจากค่าเฉลี่ยเท่าไหร่ *(ดู 6.6)*
> - **การแจกแจง / ฮิสโตแกรม (Distribution / Histogram)** — แต่ละผลเกิดบ่อยแค่ไหน / กราฟแท่งของสิ่งนั้น
> - **ความเบ้ (Skew)** — ความไม่สมมาตร: เบ้ลบ = ขาดทุนใหญ่ที่เกิดนาน ๆ ครั้ง เบ้บวก = กำไรใหญ่ที่เกิดนาน ๆ ครั้ง
> - **ความโด่ง / หางอ้วน (Kurtosis / Fat tails)** — ผลสุดขั้วเกิดบ่อยแค่ไหนเมื่อเทียบกับ Bell curve
> - **ขนาดตัวอย่าง (Sample size, n)** — จำนวนไม้หรือวันที่วัด
> - **Standard error** — ความไม่แน่นอนของค่าเฉลี่ย: SD ÷ √n
> - **ช่วง 95% (Confidence interval)** — ช่วงที่น่าจะมีค่าจริงอยู่ข้างในราว 95% ของกรณี
> - **สหสัมพันธ์ (Correlation)** — สองชุดข้อมูลขยับไปด้วยกันมากแค่ไหน (จาก −1 ถึง +1)
> - **เหตุและผล (Causation)** — สิ่งหนึ่งทำให้อีกสิ่งเกิดขึ้นจริง
""")
L.before_heading("th", "2.", """
![[p9-ten-trades.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: สิบไม้ด้วยมือ
> ผลเป็น R: **+2, −1, +0.5, −1, +3, −1, +1.5, −0.5, −1, +2.5**
> 1. **ค่าเฉลี่ย:** ผลรวม = +5.0R → 5.0 ÷ 10 = **+0.50R** ต่อไม้
> 2. **มัธยฐาน:** เรียงลำดับ: −1, −1, −1, −1, −0.5, +0.5, +1.5, +2, +2.5, +3 สองค่ากลางคือ −0.5 และ +0.5 → (−0.5 + 0.5) ÷ 2 = **0R**
> 3. **ระยะห่างจากค่าเฉลี่ย:** +1.5, −1.5, 0, −1.5, +2.5, −1.5, +1.0, −1.0, −1.5, +2.0
> 4. **ยกกำลังสอง:** 2.25, 2.25, 0, 2.25, 6.25, 2.25, 1, 1, 2.25, 4 → รวม **23.5** หารด้วย n − 1 = 9 → 2.61 ถอดรากที่สอง → **SD ≈ 1.62R**
> 5. **อัตราชนะ:** ชนะ 5 จาก 10 = **50%**
> 6. **แล้วไง?** ค่าเฉลี่ยเป็นบวก แต่มัธยฐานเป็นศูนย์: ไม้ "ทั่วไป" ไม่ได้อะไรเลย ไม้ชนะใหญ่สามสี่ไม้แบกผลทั้งหมด เป็นเรื่องปกติของการเทรดแบบตามเทรนด์ และหมายความว่าการข้ามไม่กี่ไม้อาจทำลายความได้เปรียบทั้งหมด

> [!analogy]
> ค่าเฉลี่ย vs มัธยฐานเหมือน **รายได้เฉลี่ยของหมู่บ้าน** ที่มีเศรษฐีหนึ่งคน: ค่าเฉลี่ยดูรวย แต่ครัวเรือนตรงกลางธรรมดา ค่าเฉลี่ยการเทรดของคุณก็ถูกดึงขึ้นแบบเดียวกันได้ด้วยไม้ชนะใหญ่หนึ่งสองไม้
>
> **จุดที่เปรียบเทียบไม่ได้:** เศรษฐีในหมู่บ้านยังรวยอยู่ แต่ในการเทรด คุณไม่มีทางรู้ล่วงหน้าว่าไม้ไหนจะเป็นไม้ใหญ่ จึงต้องเทรดทุกไม้

> [!check]- เช็กความเข้าใจ: อธิบายผลลัพธ์
> **Q1.** ห้าไม้: +1, +1, +1, +1, −6 ค่าเฉลี่ยและมัธยฐานเท่าไหร่ และความต่างบอกอะไร?
> > [!answer]-
> > ค่าเฉลี่ย = −2 ÷ 5 = −0.4R มัธยฐาน = +1R ไม้ส่วนใหญ่ชนะเล็ก ๆ แต่ขาดทุนใหญ่ไม้เดียวลบทิ้งหมด: เบ้ลบ พบบ่อยในกลยุทธ์ที่ไม่มี Stop แน่น
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: หลัง 10 ไม้ มั่นใจได้แค่ไหน?
> 1. **ความไม่แน่นอนของค่าเฉลี่ย (Standard error)** = SD ÷ √n = 1.62 ÷ √10 = 1.62 ÷ 3.16 ≈ **0.51R**
> 2. **ช่วง 95%** ≈ ค่าเฉลี่ย ± 1.96 × 0.51 = 0.50 ± 1.0 → **−0.50R ถึง +1.50R**
> 3. **ช่วงของอัตราชนะ** ที่ 50% กับ 20 ไม้: 1.96 × √(0.5 × 0.5 ÷ 20) ≈ 0.22 → **28% ถึง 72%** กับ 100 ไม้: ± 0.098 → **40% ถึง 60%**
> 4. **แล้วไง?** หลังสิบไม้ ค่าเฉลี่ยจริงอาจติดลบก็ได้ คุณยังแยกฝีมือออกจากโชคไม่ได้ จึงต้องใช้ขนาดเล็กและเก็บไม้ต่อไป

ตัวเลขชุดเดียวกันได้จากสคริปต์สั้น ๆ ใน Vault คุณจึงตรวจไม้ของตัวเองได้:

```bash
python3 _tools/quant/ten_trades.py                    # สิบไม้ข้างบน
python3 _tools/quant/ten_trades.py 1.5 -1 2 -1 0.5    # R-multiple ของคุณเอง
```

ผลลัพธ์จริงของสิบไม้:

""" + OUTPUT + """

> [!check]- เช็กความเข้าใจ: ขนาดตัวอย่าง
> **Q1.** กลยุทธ์หนึ่งมีค่าเฉลี่ย +0.4R และ SD 2R จาก 25 ไม้ ค่าเฉลี่ยสูงกว่าศูนย์ชัดเจนไหม?
> > [!answer]-
> > Standard error = 2 ÷ √25 = 0.4R ช่วง 95% ≈ 0.4 ± 0.78 → −0.38R ถึง +1.18R ยังไม่ชัดเจนว่าสูงกว่าศูนย์
""")
L.before_callout("th", "example", """
> [!check]- เช็กความเข้าใจ: สหสัมพันธ์
> **Q1.** ปีที่ผ่านมา Bitcoin กับหุ้นเทคตัวหนึ่งขึ้นลงพร้อมกันเกือบทุกวัน ปีหน้าใช้ตัวหนึ่งเฮดจ์อีกตัวได้ไหม?
> > [!answer]-
> > ไม่ปลอดภัย สหสัมพันธ์อธิบายอดีตและเปลี่ยนได้ มักเปลี่ยนตอนวิกฤตซึ่งเป็นตอนที่คุณต้องการมันพอดี และไม่ได้แปลว่าตัวหนึ่งเป็นเหตุของอีกตัว
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** คู่เงินหลักมีหางค่อนข้างบางในแต่ละวัน แต่การเซอร์ไพรส์ของธนาคารกลางสร้างการขยับมหาศาลนาน ๆ ครั้ง *(ดู 0.3)*
> - **ทองคำ:** หางอ้วนรอบข้อมูลสหรัฐและวิกฤต ช่วงกลางปี 2026 ขยับเฉลี่ยราว 1.1% ต่อวัน *(ดู 0.4, 0.7)*
> - **หุ้น:** หุ้นรายตัวมีหางอ้วนมากในวันประกาศงบ (Gap 10–20%) *(ดู 0.5)*
> - **คริปโต:** หางอ้วนที่สุด วันที่ขยับเกิน 10% เกิดหลายครั้งต่อปี *(ดู 0.7)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** ทำไมบางครั้งมัธยฐานจึงมีประโยชน์กว่าค่าเฉลี่ยในการอธิบายไม้เทรด?
> > [!answer]-
> > เพราะผลสุดขั้วไม่กี่ค่าดึงค่าเฉลี่ยได้ แต่ไม่ดึงมัธยฐาน มัธยฐานแสดงว่าไม้ปกติหน้าตาเป็นอย่างไร
> **Q2.** ต้องเทรดกี่ไม้ ช่วง 95% ของอัตราชนะ 50% จึงจะแคบกว่า ±10 จุดเปอร์เซ็นต์?
> > [!answer]-
> > ราว 100 ไม้ (1.96 × √(0.25 ÷ 100) ≈ 0.098)
""")

L.set_meta("level", "v2")
L.save()
