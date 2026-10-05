"""B9c · v2 upgrade of 3.5 Stop Loss & Take Profit Placement (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("03 Risk & Money Management/3.5 Stop Loss & Take Profit Placement.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Put your stop at the price where your reason for the trade is clearly wrong, plus a little extra room for normal wiggles. Then choose the position size so that being stopped costs your usual 1R. Decide where you'll take profit before you enter, because once money is moving, it's much harder to think clearly.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Invalidation** — the price that proves the trade idea wrong.
> - **Structural stop** — beyond the swing or zone the trade depends on, plus a buffer.
> - **Buffer** — extra distance for spread and noise, often 0.25–0.5 × ATR.
> - **ATR (Average True Range)** — the average size of recent candles on a timeframe.
> - **Volatility stop** — a stop set at a multiple of ATR from entry.
> - **Time stop** — exiting if the trade hasn't worked within a set number of candles.
> - **Partial profit / runner** — closing part of the position at a target and letting the rest run.
> - **Break-even** — moving the stop to the entry price.
> - **Trailing stop** — moving the stop behind new swings as the trade progresses *(see 2.3)*.
""")
L.before_heading("en", "2.", """
> [!analogy]
> A stop is like the **fire exit you choose before the show starts**. You pick it calmly, where it actually leads outside. Looking for it once the theatre is full of smoke is too late, and running to the nearest door that turns out to be a cupboard (a stop inside the noise) doesn't save you.
>
> **Where it breaks:** a fire exit is always open. In a fast market, price can jump past your stop and fill worse, so the stop limits the loss but doesn't guarantee the exact price.

![[p3-buffer-math.en.svg]]

> [!walkthrough] Step by step: choosing the buffer
> The long from the example: entry **103.6**, swing low **101.9**, ATR(14) **1.4**, target **110**, risk **100 USD**.
> 1. **No buffer:** stop **101.9** → risk 1.7 → **3.8R**, size ≈ **59 units**. But the wick that comes back to 101.9 touches it, and you're out.
> 2. **0.25 × ATR** = 0.35 → stop **101.55** → risk 2.05 → **3.1R**, size ≈ **49 units**.
> 3. **0.5 × ATR** = 0.7 → stop **101.2** → risk 2.4 → **2.7R**, size ≈ **42 units**.
> 4. **So what?** The buffer lowers the R:R a little and the size a little, but stops you from being taken out by the exact move the setup expects.

> [!check]- Check your understanding: stop location
> **Q1.** Long on a 1H CHoCH. The swing low that created it is 48.20; ATR(14) on 1H is 0.60. Where's the stop with a 0.5 × ATR buffer?
> > [!answer]-
> > 48.20 − 0.30 = **47.90**.
""")
L.before_heading("en", "3.", """
> [!check]- Check your understanding: when the stop is far
> **Q1.** The structural stop is 4.0 away instead of the usual 2.0. Your risk is 100 USD. What changes?
> > [!answer]-
> > Only the size: 100 ÷ 4.0 = **25 units** instead of 50. Don't tighten the stop into the noise; if the R:R to the real target is now too low, skip the trade.
""")
L.before_callout("en", "action", """
> [!walkthrough] Step by step: method A vs method B in R
> Same trade: entry **103.6**, stop **101.2** (1R = 2.4), first target **108.4**, final target **110**.
> 1. **Method A, full exit at 110:** +6.4 ÷ 2.4 = **+2.67R**. If price reaches 108.4 and then falls back to the stop: **−1R**.
> 2. **Method B, half at 108.4 (+2R), rest at 110 (+2.67R):** average = **+2.33R**.
> 3. Method B if the runner is stopped at break-even after the first target: 0.5 × 2 + 0.5 × 0 = **+1R**, instead of −1R.
> 4. **So what?** B gives up a little on the best outcome to turn some reversals into wins. Neither is "right"; choose one and keep it for 30+ trades.

> [!check]- Check your understanding: exits
> **Q1.** You move to break-even the moment a trade reaches +0.5R. What tends to happen, and what's a better rule?
> > [!answer]-
> > Normal pullbacks stop you out at zero right before the move. Better: move to break-even only after a new swing in your favour (BOS) or at +1.5–2R.

> [!market]
> - **Forex:** on a short, the stop is triggered by the ask price, so add the spread to the buffer; rollover around 04:00 UTC+7 can widen spreads *(see 0.3)*.
> - **Gold:** ATR on 1H is often several dollars; check it before choosing a stop *(see 0.4)*.
> - **Stocks:** stops don't protect against overnight gaps; size smaller over earnings *(see 0.5, 10.3)*.
> - **Crypto:** wicks can be extreme on thin exchanges; use the exchange with the deepest book *(see 0.7)*.

> [!caution]
> A stop order is not a guaranteed price. Gaps, news spikes and thin markets can fill it far beyond your level, so a 1R plan can lose more. Reduce size before high-impact events, and never trade without a stop in the platform.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Name the four prices to write before every entry.
> > [!answer]-
> > Invalidation, stop (invalidation ± buffer), target(s), and the management rule (A, B or C, plus when to move to break-even).
> **Q2.** Short at 75.40. The swing high is 76.10, ATR 0.80, buffer 0.25 × ATR. Where's the stop, and what's 1R per unit?
> > [!answer]-
> > Stop = 76.10 + 0.20 = **76.30**. 1R = 76.30 − 75.40 = **0.90** per unit.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> วาง Stop ที่ราคาซึ่งเหตุผลในการเทรดผิดอย่างชัดเจน บวกระยะเผื่อเล็กน้อยสำหรับการแกว่งปกติ แล้วเลือกขนาดโพซิชันให้การโดน Stop เสียเท่ากับ 1R ตามปกติ ตัดสินใจว่าจะทำกำไรตรงไหนก่อนเข้า เพราะเมื่อเงินเริ่มขยับ การคิดให้ชัดจะยากขึ้นมาก
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **จุดที่ไอเดียผิด (Invalidation)** — ราคาที่พิสูจน์ว่าไอเดียเทรดผิด
> - **Stop ตามโครงสร้าง (Structural stop)** — เลยสวิงหรือโซนที่เทรดพึ่งพา บวกระยะเผื่อ
> - **ระยะเผื่อ (Buffer)** — ระยะเพิ่มสำหรับ Spread และสัญญาณรบกวน มักเป็น 0.25–0.5 × ATR
> - **ATR (Average True Range)** — ขนาดเฉลี่ยของแท่งเทียนล่าสุดในไทม์เฟรมหนึ่ง
> - **Stop ตามความผันผวน (Volatility stop)** — Stop ที่ห่างจากจุดเข้าเป็นจำนวนเท่าของ ATR
> - **Stop ตามเวลา (Time stop)** — ออกถ้าเทรดยังไม่ทำงานภายในจำนวนแท่งที่กำหนด
> - **ทำกำไรบางส่วน / ส่วนที่ปล่อยวิ่ง (Partial profit / Runner)** — ปิดบางส่วนที่เป้า และปล่อยส่วนที่เหลือวิ่งต่อ
> - **จุดเท่าทุน (Break-even)** — เลื่อน Stop ไปที่ราคาเข้า
> - **เลื่อน Stop ตาม (Trailing stop)** — เลื่อน Stop ตามสวิงใหม่ขณะที่เทรดไปได้ดี *(ดู 2.3)*
""")
L.before_heading("th", "2.", """
> [!analogy]
> Stop เหมือน **ทางหนีไฟที่คุณเลือกก่อนการแสดงเริ่ม** คุณเลือกอย่างใจเย็น และเลือกประตูที่ออกไปข้างนอกได้จริง การหาทางออกตอนโรงละครเต็มไปด้วยควันสายเกินไป และการวิ่งไปประตูที่ใกล้ที่สุดซึ่งกลายเป็นตู้เก็บของ (Stop ที่อยู่ในสัญญาณรบกวน) ก็ไม่ช่วยอะไร
>
> **จุดที่เปรียบเทียบไม่ได้:** ทางหนีไฟเปิดอยู่เสมอ แต่ในตลาดที่เร็ว ราคาอาจกระโดดข้าม Stop และได้ราคาแย่กว่า Stop จำกัดการขาดทุน แต่ไม่รับประกันราคาที่แน่นอน

![[p3-buffer-math.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: เลือกระยะเผื่อ
> ไม้ซื้อจากตัวอย่าง: เข้า **103.6** Swing low **101.9** ATR(14) **1.4** เป้า **110** เสี่ยง **100 ดอลลาร์**
> 1. **ไม่มีระยะเผื่อ:** Stop **101.9** → เสี่ยง 1.7 → **3.8R** ขนาด ≈ **59 หน่วย** แต่ไส้ที่ลงมาที่ 101.9 จะแตะพอดี และคุณโดนเก็บออก
> 2. **0.25 × ATR** = 0.35 → Stop **101.55** → เสี่ยง 2.05 → **3.1R** ขนาด ≈ **49 หน่วย**
> 3. **0.5 × ATR** = 0.7 → Stop **101.2** → เสี่ยง 2.4 → **2.7R** ขนาด ≈ **42 หน่วย**
> 4. **แล้วไง?** ระยะเผื่อลด R:R และขนาดลงเล็กน้อย แต่ป้องกันไม่ให้คุณโดนเก็บออกจากการขยับที่ Setup คาดไว้อยู่แล้ว

> [!check]- เช็กความเข้าใจ: ตำแหน่ง Stop
> **Q1.** ซื้อตาม CHoCH บน 1H จุดสวิงต่ำที่สร้าง CHoCH คือ 48.20 ATR(14) บน 1H คือ 0.60 Stop อยู่ที่ไหนถ้าใช้ระยะเผื่อ 0.5 × ATR?
> > [!answer]-
> > 48.20 − 0.30 = **47.90**
""")
L.before_heading("th", "3.", """
> [!check]- เช็กความเข้าใจ: เมื่อ Stop อยู่ไกล
> **Q1.** Stop ตามโครงสร้างห่าง 4.0 แทนที่จะเป็น 2.0 ตามปกติ คุณเสี่ยง 100 ดอลลาร์ อะไรเปลี่ยน?
> > [!answer]-
> > เปลี่ยนแค่ขนาด: 100 ÷ 4.0 = **25 หน่วย** แทน 50 อย่าบีบ Stop เข้าไปในสัญญาณรบกวน ถ้า R:R ถึงเป้าจริงต่ำเกินไป ให้ข้ามไม้นี้
""")
L.before_callout("th", "action", """
> [!walkthrough] ไล่ทีละขั้น: วิธี A vs วิธี B ในหน่วย R
> เทรดเดิม: เข้า **103.6** Stop **101.2** (1R = 2.4) เป้าแรก **108.4** เป้าสุดท้าย **110**
> 1. **วิธี A ออกทั้งหมดที่ 110:** +6.4 ÷ 2.4 = **+2.67R** ถ้าราคาถึง 108.4 แล้วกลับลงไปโดน Stop: **−1R**
> 2. **วิธี B ปิดครึ่งที่ 108.4 (+2R) ที่เหลือที่ 110 (+2.67R):** เฉลี่ย = **+2.33R**
> 3. วิธี B ถ้าส่วนที่ปล่อยวิ่งโดน Stop ที่จุดเท่าทุนหลังเป้าแรก: 0.5 × 2 + 0.5 × 0 = **+1R** แทน −1R
> 4. **แล้วไง?** B ยอมเสียนิดหน่อยในกรณีที่ดีที่สุด เพื่อเปลี่ยนการกลับตัวบางครั้งให้เป็นไม้ชนะ ไม่มีวิธีไหน "ถูก" เลือกหนึ่งวิธีและใช้ต่อเนื่อง 30 ไม้ขึ้นไป

> [!check]- เช็กความเข้าใจ: การออก
> **Q1.** คุณเลื่อนไปจุดเท่าทุนทันทีที่เทรดถึง +0.5R มักเกิดอะไรขึ้น และกฎที่ดีกว่าคืออะไร?
> > [!answer]-
> > การย่อปกติเก็บคุณออกที่ศูนย์ก่อนราคาวิ่ง ดีกว่า: เลื่อนไปจุดเท่าทุนหลังเกิดสวิงใหม่ในทางของคุณ (BOS) หรือที่ +1.5–2R

> [!market]
> - **ฟอเร็กซ์:** ในไม้ขาย Stop ถูกเรียกด้วยราคา Ask จึงบวก Spread เข้าไปในระยะเผื่อ ช่วงตัดรอบวันราว 04:00 UTC+7 Spread อาจถ่าง *(ดู 0.3)*
> - **ทองคำ:** ATR บน 1H มักหลายดอลลาร์ ตรวจก่อนเลือก Stop *(ดู 0.4)*
> - **หุ้น:** Stop ไม่ป้องกัน Gap ข้ามคืน ลดขนาดช่วงประกาศงบ *(ดู 0.5, 10.3)*
> - **คริปโต:** ไส้อาจสุดโต่งในกระดานเทรดที่บาง ใช้กระดานที่สมุดคำสั่งลึกที่สุด *(ดู 0.7)*

> [!caution]
> คำสั่ง Stop ไม่ใช่ราคาที่รับประกัน Gap การพุ่งของข่าว และตลาดที่บาง อาจทำให้ได้ราคาเลยระดับไปมาก แผน 1R จึงเสียมากกว่านั้นได้ ลดขนาดก่อนเหตุการณ์ผลกระทบสูง และอย่าเทรดโดยไม่มี Stop ในแพลตฟอร์ม
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกราคาสี่ตัวที่ต้องเขียนก่อนเข้าทุกเทรด
> > [!answer]-
> > จุดที่ไอเดียผิด, Stop (จุดที่ไอเดียผิด ± ระยะเผื่อ), เป้า และกฎการบริหาร (A, B หรือ C พร้อมเวลาที่จะเลื่อนไปจุดเท่าทุน)
> **Q2.** ขายที่ 75.40 จุดสวิงสูง 76.10 ATR 0.80 ระยะเผื่อ 0.25 × ATR Stop อยู่ที่ไหน และ 1R ต่อหน่วยเท่าไร?
> > [!answer]-
> > Stop = 76.10 + 0.20 = **76.30** 1R = 76.30 − 75.40 = **0.90** ต่อหน่วย
""")

L.set_meta("level", "v2")
L.save()
