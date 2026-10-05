"""B5 · v2 upgrade of 6.6 Standard Deviation Projections (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("06 Fibonacci, Elliott Wave & Std Dev/6.6 Standard Deviation Projections.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> If you measure the height of everyone in a class, most students are close to the average and only a few are very tall or very short. **Standard deviation** is one number that says how spread out the heights are. Markets work similarly: most days price moves a "normal" amount, and a few days it moves a lot. Knowing what "normal" is helps you set realistic targets and stops. But markets surprise more often than heights do: very big days happen more than the textbook says.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Mean (average)** — the sum of the values divided by how many there are.
> - **SD / σ (standard deviation, "sigma")** — a measure of how far values typically are from the mean.
> - **Normal distribution (bell curve)** — a symmetric shape where about 68% of values lie within ±1 SD, 95% within ±2 SD, 99.7% within ±3 SD.
> - **Fat tails** — extreme values happening more often than a bell curve predicts; typical of markets.
> - **Volatility** — how much prices move; usually quoted as an **annualised** SD of returns, in %.
> - **Realised vs implied volatility** — measured from past prices / implied by today's option prices *(see 8.2)*.
> - **VIX** — the CBOE Volatility Index: the market's expected 30-day volatility of the S&P 500, taken from option prices, in annual %.
> - **√time rule** — volatility grows with the square root of time: daily SD ≈ annual SD ÷ √252 (252 ≈ trading days in a year).
> - **ATR (average true range)** — average candle range; a practical cousin of SD *(see 0.4, 3.5)*.
> - **Bollinger Bands** — a 20-period moving average ± 2 SD of closing prices.
> - **Squeeze** — Bollinger Bands narrowing: low volatility, often before a big move.
> - **ICT "SD" projection** — multiples of a reference leg projected beyond it; a measured move, not statistics.
""")
L.before_heading("en", "2.", """
![[p6-heights.en.svg]]

> [!walkthrough] Step by step: standard deviation by hand, with five students
> Heights: **158, 162, 165, 168, 172** cm.
> 1. **Mean** = (158 + 162 + 165 + 168 + 172) ÷ 5 = 825 ÷ 5 = **165**.
> 2. **Distance from the mean:** −7, −3, 0, +3, +7.
> 3. **Square them:** 49, 9, 0, 9, 49 → sum **116**.
> 4. **Average of the squares:** 116 ÷ 5 = **23.2**. Square root: √23.2 ≈ **4.8 cm**. That's the SD. (Statistics software often divides by 4 instead of 5 for samples: √29 ≈ 5.4.)
> 5. **For a bigger class with SD 7 cm** (figure): about 68% of students are within 165 ± 7 = **158–172**, about 95% within **151–179**.
> 6. **So what?** Replace "height" with "daily % change" and you have market volatility. The same arithmetic tells you what a normal day looks like.

> [!analogy]
> SD for markets is like the **typical height spread in a class**. If the average student is 165 cm and the SD is 7 cm, a 172 cm student is ordinary, a 186 cm student is rare. A +1 SD market day is ordinary; a +3 SD day is rare.
>
> **Where it breaks:** heights really are close to a bell curve, and nobody is 3 metres tall. Markets have fat tails: "impossible" 5 SD or 10 SD days do happen (crashes, gaps), so never size a position as if they can't.

> [!check]- Check your understanding: the bell curve
> **Q1.** Mean 165 cm, SD 7 cm. Roughly what share of students are between 151 and 179 cm?
> > [!answer]-
> > That's ±2 SD → about 95%.
> **Q2.** Why can't you use the 99.7% (±3 SD) rule to say a market crash is "practically impossible"?
> > [!answer]-
> > Market returns have fat tails: extreme days happen far more often than a normal distribution predicts.
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: from the VIX to an expected daily move
> 1. **VIX = 16** means the options market expects about **16% annualised** volatility for the S&P 500.
> 2. **Daily:** 16% ÷ √252 = 16% ÷ 15.87 ≈ **1.0% per day**.
> 3. **In points:** with the index at **5,000**, 1% ≈ **50 points** → about 68% of days within ±50.
> 4. **Weekly:** 16% × √(5/252) ≈ **2.25%** ≈ 113 points.
> 5. **If the VIX jumps to 30:** 30% ÷ 15.87 ≈ **1.89% per day** ≈ **94 points**. The same 50-point stop that was "1σ" is now only about half a normal day.
> 6. **So what?** When volatility rises, widen stops **and** cut size so 1R stays the same *(see 3.2)*. When it falls, targets must shrink.

> [!check]- Check your understanding: expected move
> **Q1.** VIX is 25 and the index is at 6,000. Roughly what is a 1 SD daily move in points?
> > [!answer]-
> > 25% ÷ 15.87 ≈ 1.58% → 6,000 × 1.58% ≈ 95 points.
""")
L.before_heading("en", "4.", """
> [!check]- Check your understanding: Bollinger Bands
> **Q1.** Price closes above the upper Bollinger Band three days in a row during a strong uptrend. Is that a sell signal?
> > [!answer]-
> > Not on its own. In strong trends price can "walk the band". A close back inside after a close outside is more meaningful, especially at a liquidity level.
""")
L.before_callout("en", "example", """
> [!check]- Check your understanding: ICT projections
> **Q1.** The reference leg runs from 98.6 to 104.2. Where is the −1 projection, and is it a statistical level?
> > [!answer]-
> > Leg = 5.6 → 104.2 + 5.6 = 109.8. It's a measured move, not statistics; use it only with liquidity or an HTF level.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** low volatility: EUR/USD's average daily move was about 0.2% in Jul–Sep 2026 *(figure in 0.7)*; σ-based targets are small in pips *(see 0.3)*.
> - **Gold:** much more volatile than currencies (≈1.1% a day on average in mid-2026, see 0.7); widen stops, cut size *(see 0.4)*.
> - **Stocks & indices:** the VIX gives you implied volatility for the S&P 500 directly; single stocks jump around earnings *(see 0.5, 0.6)*.
> - **Crypto:** 24/7, so use √365 instead of √252 for daily conversions; tails are especially fat *(see 0.7)*.

> [!caution]
> Standard deviation describes normal days and says little about the rare day that can wipe out an account. A position sized on "a 4 SD move is almost impossible" will eventually meet one. Always size from your stop and your maximum loss (Phase 3), not from probabilities.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Annual volatility 20%. What's the approximate daily 1 SD move in %?
> > [!answer]-
> > 20% ÷ √252 ≈ 20 ÷ 15.87 ≈ 1.26%.
> **Q2.** What's the difference between a statistical standard deviation and an ICT "SD" projection?
> > [!answer]-
> > Statistical SD measures how spread out returns are; ICT projections are multiples of a chosen price leg (a measured move). Only the first is statistics.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ถ้าคุณวัดส่วนสูงของทุกคนในห้องเรียน นักเรียนส่วนใหญ่สูงใกล้ค่าเฉลี่ย มีไม่กี่คนที่สูงมากหรือเตี้ยมาก **ส่วนเบี่ยงเบนมาตรฐาน** คือตัวเลขตัวเดียวที่บอกว่าส่วนสูงกระจายแค่ไหน ตลาดก็คล้ายกัน: วันส่วนใหญ่ราคาขยับ "ปกติ" และมีไม่กี่วันที่ขยับมาก การรู้ว่า "ปกติ" คือเท่าไหร่ช่วยให้ตั้งเป้าและ Stop ได้สมจริง แต่ตลาดทำให้ประหลาดใจบ่อยกว่าส่วนสูง: วันที่ขยับแรงมากเกิดบ่อยกว่าที่ตำราบอก
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **ค่าเฉลี่ย (Mean / Average)** — ผลรวมของค่าทั้งหมดหารด้วยจำนวนค่า
> - **SD / σ (Standard deviation ส่วนเบี่ยงเบนมาตรฐาน "ซิกมา")** — ตัววัดว่าค่าต่าง ๆ มักห่างจากค่าเฉลี่ยเท่าไหร่
> - **การแจกแจงปกติ (Normal distribution / Bell curve)** — รูปทรงสมมาตรที่ราว 68% ของค่าอยู่ใน ±1 SD 95% ใน ±2 SD 99.7% ใน ±3 SD
> - **หางอ้วน (Fat tails)** — ค่าสุดขั้วเกิดบ่อยกว่าที่ Bell curve ทำนาย เป็นลักษณะของตลาด
> - **ความผันผวน (Volatility)** — ราคาขยับมากแค่ไหน มักบอกเป็น SD ของผลตอบแทน **ต่อปี** เป็น %
> - **ความผันผวนที่เกิดจริง vs ที่แฝงอยู่ (Realised vs Implied volatility)** — วัดจากราคาในอดีต / แฝงอยู่ในราคาออปชันวันนี้ *(ดู 8.2)*
> - **VIX** — ดัชนีความผันผวน CBOE: ความผันผวน 30 วันข้างหน้าที่ตลาดคาดของ S&P 500 คำนวณจากราคาออปชัน เป็น % ต่อปี
> - **กฎรากที่สองของเวลา (√time rule)** — ความผันผวนเพิ่มตามรากที่สองของเวลา: SD รายวัน ≈ SD รายปี ÷ √252 (252 ≈ จำนวนวันซื้อขายต่อปี)
> - **ATR (Average true range)** — ช่วงแท่งเทียนเฉลี่ย ญาติที่ใช้งานง่ายของ SD *(ดู 0.4, 3.5)*
> - **Bollinger Bands** — เส้นค่าเฉลี่ย 20 แท่ง ± 2 SD ของราคาปิด
> - **Squeeze** — Bollinger Bands แคบลง: ความผันผวนต่ำ มักเกิดก่อนการวิ่งใหญ่
> - **"SD" แบบ ICT** — จำนวนเท่าของขาอ้างอิงที่ฉายเลยออกไป เป็นการวัดระยะ ไม่ใช่สถิติ
""")
L.before_heading("th", "2.", """
![[p6-heights.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: คำนวณส่วนเบี่ยงเบนมาตรฐานด้วยมือ กับนักเรียนห้าคน
> ส่วนสูง: **158, 162, 165, 168, 172** ซม.
> 1. **ค่าเฉลี่ย** = (158 + 162 + 165 + 168 + 172) ÷ 5 = 825 ÷ 5 = **165**
> 2. **ระยะห่างจากค่าเฉลี่ย:** −7, −3, 0, +3, +7
> 3. **ยกกำลังสอง:** 49, 9, 0, 9, 49 → รวม **116**
> 4. **ค่าเฉลี่ยของค่ายกกำลังสอง:** 116 ÷ 5 = **23.2** ถอดรากที่สอง: √23.2 ≈ **4.8 ซม.** นั่นคือ SD (โปรแกรมสถิติมักหารด้วย 4 แทน 5 สำหรับกลุ่มตัวอย่าง: √29 ≈ 5.4)
> 5. **สำหรับห้องที่ใหญ่กว่าที่ SD 7 ซม.** (ภาพ): นักเรียนราว 68% อยู่ใน 165 ± 7 = **158–172** ราว 95% อยู่ใน **151–179**
> 6. **แล้วไง?** เปลี่ยน "ส่วนสูง" เป็น "% การเปลี่ยนแปลงรายวัน" แล้วคุณจะได้ความผันผวนของตลาด เลขคณิตเดียวกันบอกว่าวันปกติหน้าตาเป็นอย่างไร

> [!analogy]
> SD ของตลาดเหมือน **การกระจายของส่วนสูงในห้องเรียน** ถ้านักเรียนเฉลี่ยสูง 165 ซม. และ SD 7 ซม. คนสูง 172 ซม. เป็นเรื่องธรรมดา คนสูง 186 ซม. หายาก วันที่ตลาดขยับ +1 SD เป็นเรื่องธรรมดา วัน +3 SD หายาก
>
> **จุดที่เปรียบเทียบไม่ได้:** ส่วนสูงใกล้เคียง Bell curve จริง และไม่มีใครสูง 3 เมตร แต่ตลาดมีหางอ้วน: วัน 5 SD หรือ 10 SD ที่ "เป็นไปไม่ได้" เกิดขึ้นจริง (ตลาดถล่ม Gap) อย่าคำนวณขนาดไม้ราวกับว่ามันเกิดไม่ได้

> [!check]- เช็กความเข้าใจ: Bell curve
> **Q1.** ค่าเฉลี่ย 165 ซม. SD 7 ซม. นักเรียนประมาณกี่ส่วนที่สูงระหว่าง 151 ถึง 179 ซม.?
> > [!answer]-
> > นั่นคือ ±2 SD → ราว 95%
> **Q2.** ทำไมใช้กฎ 99.7% (±3 SD) บอกว่าตลาดถล่ม "แทบเป็นไปไม่ได้" ไม่ได้?
> > [!answer]-
> > ผลตอบแทนของตลาดมีหางอ้วน: วันสุดขั้วเกิดบ่อยกว่าที่การแจกแจงปกติทำนายมาก
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: จาก VIX สู่การขยับรายวันที่คาด
> 1. **VIX = 16** หมายความว่าตลาดออปชันคาดความผันผวนของ S&P 500 ราว **16% ต่อปี**
> 2. **รายวัน:** 16% ÷ √252 = 16% ÷ 15.87 ≈ **1.0% ต่อวัน**
> 3. **เป็นจุด:** ดัชนีที่ **5,000** 1% ≈ **50 จุด** → ราว 68% ของวันอยู่ใน ±50
> 4. **รายสัปดาห์:** 16% × √(5/252) ≈ **2.25%** ≈ 113 จุด
> 5. **ถ้า VIX พุ่งเป็น 30:** 30% ÷ 15.87 ≈ **1.89% ต่อวัน** ≈ **94 จุด** Stop 50 จุดเดิมที่เคยเป็น "1σ" ตอนนี้เหลือแค่ราวครึ่งหนึ่งของวันปกติ
> 6. **แล้วไง?** เมื่อความผันผวนเพิ่ม ให้ขยาย Stop **และ** ลดขนาด เพื่อให้ 1R เท่าเดิม *(ดู 3.2)* เมื่อความผันผวนลด เป้าก็ต้องหดลง

> [!check]- เช็กความเข้าใจ: การขยับที่คาด
> **Q1.** VIX อยู่ที่ 25 ดัชนีที่ 6,000 การขยับรายวัน 1 SD ประมาณกี่จุด?
> > [!answer]-
> > 25% ÷ 15.87 ≈ 1.58% → 6,000 × 1.58% ≈ 95 จุด
""")
L.before_heading("th", "4.", """
> [!check]- เช็กความเข้าใจ: Bollinger Bands
> **Q1.** ราคาปิดเหนือเส้นบนของ Bollinger Band สามวันติดในเทรนด์ขาขึ้นแรง นั่นคือสัญญาณขายไหม?
> > [!answer]-
> > ไม่ใช่ถ้าดูอย่างเดียว ในเทรนด์แรงราคาอาจ "เดินเกาะขอบ" ได้ การปิดกลับเข้ามาหลังปิดออกไปมีความหมายมากกว่า โดยเฉพาะที่ระดับสภาพคล่อง
""")
L.before_callout("th", "example", """
> [!check]- เช็กความเข้าใจ: การฉายแบบ ICT
> **Q1.** ขาอ้างอิงวิ่งจาก 98.6 ถึง 104.2 ระดับ −1 อยู่ที่ไหน และเป็นระดับทางสถิติไหม?
> > [!answer]-
> > ขา = 5.6 → 104.2 + 5.6 = 109.8 เป็นการวัดระยะ ไม่ใช่สถิติ ใช้เมื่อมีสภาพคล่องหรือระดับ HTF ร่วมด้วยเท่านั้น
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** ความผันผวนต่ำ: EUR/USD ขยับเฉลี่ยราว 0.2% ต่อวันช่วง ก.ค.–ก.ย. 2026 *(ภาพใน 0.7)* เป้าตาม σ เป็น pip จึงเล็ก *(ดู 0.3)*
> - **ทองคำ:** ผันผวนกว่าสกุลเงินมาก (เฉลี่ยราว 1.1% ต่อวันช่วงกลางปี 2026 ดู 0.7) ขยาย Stop ลดขนาด *(ดู 0.4)*
> - **หุ้นและดัชนี:** VIX ให้ความผันผวนแฝงของ S&P 500 โดยตรง หุ้นรายตัวกระโดดรอบวันประกาศงบ *(ดู 0.5, 0.6)*
> - **คริปโต:** 24/7 จึงใช้ √365 แทน √252 เมื่อแปลงเป็นรายวัน หางอ้วนเป็นพิเศษ *(ดู 0.7)*

> [!caution]
> ส่วนเบี่ยงเบนมาตรฐานอธิบายวันปกติ และแทบไม่บอกอะไรเกี่ยวกับวันหายากที่ล้างบัญชีได้ โพซิชันที่คำนวณขนาดจาก "การขยับ 4 SD แทบเป็นไปไม่ได้" สักวันจะเจอมัน คำนวณขนาดจาก Stop และขาดทุนสูงสุดเสมอ (เฟส 3) ไม่ใช่จากความน่าจะเป็น
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** ความผันผวนรายปี 20% การขยับรายวัน 1 SD ประมาณกี่ %?
> > [!answer]-
> > 20% ÷ √252 ≈ 20 ÷ 15.87 ≈ 1.26%
> **Q2.** ส่วนเบี่ยงเบนมาตรฐานทางสถิติต่างจาก "SD" แบบ ICT อย่างไร?
> > [!answer]-
> > SD ทางสถิติวัดว่าผลตอบแทนกระจายแค่ไหน การฉายแบบ ICT คือจำนวนเท่าของขาราคาที่เลือก (การวัดระยะ) มีแค่อย่างแรกที่เป็นสถิติ
""")

L.set_meta("level", "v2")
L.save()
