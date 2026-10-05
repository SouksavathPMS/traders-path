"""B9a · v2 upgrade of 1.6 Checkpoint: Phase 1 Review (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("01 Foundations/1.6 Checkpoint- Phase 1 Review.md")

# ---------------------------------------------------------------- EN
L.before_callout("en", "practice", """
> [!check]- Worked problems: Phase 1
> **Q1.** A system wins 40% of trades: average win +2.5R, average loss −1R. What's the expectancy, and what would you expect over 50 trades?
> > [!answer]-
> > 0.4 × 2.5 − 0.6 × 1 = 1.0 − 0.6 = **+0.4R** per trade → about **+20R** over 50 trades (with long losing streaks along the way, see 1.1).
> **Q2.** The book has 200 for sale at 10.00 and 300 at 10.05. You buy 400 at market. What's your average price, and how much slippage did you pay versus 10.00?
> > [!answer]-
> > 200 × 10.00 + 200 × 10.05 = 4,010 → average **10.025**; slippage = 4,010 − 4,000 = **10** (see 1.2).
> **Q3.** O 120, H 121, L 112, C 120.5. Colour, body, lower wick and close location?
> > [!answer]-
> > Green; body **0.5**; lower wick 120 − 112 = **8**; close location (120.5 − 112) ÷ 9 ≈ **94%**: a strong hammer shape. It still needs a level and context to be a setup (see 1.3, 1.4).
> **Q4.** Daily uptrend. Entry 200, target 212. A 1H trigger allows a stop at 197; a daily trigger needs 190. With 60 USD risk, what's the R:R and size of each?
> > [!answer]-
> > 1H: risk 3 → R:R **4**, size 60 ÷ 3 = **20 units**. Daily: risk 10 → R:R **1.2**, size **6 units** (see 1.5).
""")
L.before_callout("en", "key", """
> [!check]- Final check: Phase 1
> **Q1.** You bought a hammer in the middle of a downtrend without a stop, and it made +3R. Grade the trade and say what you log.
> > [!answer]-
> > Bad process (no level, against context, no stop) + good outcome. Log it as a **mistake**: it's the "dumb luck" box from 1.1.
> **Q2.** In one line each: what does the HTF decide, what does the MTF decide, what does the LTF decide?
> > [!answer]-
> > HTF: direction. MTF: location (the level to trade from). LTF: the trigger and a tight, logical stop.
""")

# ---------------------------------------------------------------- TH
L.before_callout("th", "practice", """
> [!check]- โจทย์ฝึกคำนวณ: เฟส 1
> **Q1.** ระบบชนะ 40% ของไม้: กำไรเฉลี่ย +2.5R ขาดทุนเฉลี่ย −1R ค่าคาดหวังเท่าไร และคาดว่าจะได้เท่าไรใน 50 ไม้?
> > [!answer]-
> > 0.4 × 2.5 − 0.6 × 1 = 1.0 − 0.6 = **+0.4R** ต่อไม้ → ราว **+20R** ใน 50 ไม้ (ระหว่างทางมีแพ้ติดกันยาวได้ ดู 1.1)
> **Q2.** สมุดคำสั่งมี 200 ตั้งขายที่ 10.00 และ 300 ที่ 10.05 คุณซื้อ Market 400 ราคาเฉลี่ยเท่าไร และเสีย Slippage เท่าไรเทียบกับ 10.00?
> > [!answer]-
> > 200 × 10.00 + 200 × 10.05 = 4,010 → เฉลี่ย **10.025** Slippage = 4,010 − 4,000 = **10** (ดู 1.2)
> **Q3.** เปิด 120 สูงสุด 121 ต่ำสุด 112 ปิด 120.5 สี ตัวแท่ง ไส้ล่าง และตำแหน่งปิด?
> > [!answer]-
> > เขียว ตัวแท่ง **0.5** ไส้ล่าง 120 − 112 = **8** ตำแหน่งปิด (120.5 − 112) ÷ 9 ≈ **94%**: รูปทรงแฮมเมอร์ที่แข็งแรง แต่ยังต้องมีระดับราคาและบริบทจึงจะเป็น Setup (ดู 1.3, 1.4)
> **Q4.** เทรนด์รายวันขาขึ้น เข้า 200 เป้า 212 สัญญาณ 1H ให้ตั้ง Stop ที่ 197 สัญญาณรายวันต้องตั้งที่ 190 เสี่ยง 60 ดอลลาร์ R:R และขนาดของแต่ละแบบเท่าไร?
> > [!answer]-
> > 1H: เสี่ยง 3 → R:R **4** ขนาด 60 ÷ 3 = **20 หน่วย** รายวัน: เสี่ยง 10 → R:R **1.2** ขนาด **6 หน่วย** (ดู 1.5)
""")
L.before_callout("th", "key", """
> [!check]- ทดสอบสุดท้าย: เฟส 1
> **Q1.** คุณซื้อแฮมเมอร์กลางเทรนด์ขาลงโดยไม่ตั้ง Stop และได้ +3R ให้เกรดไม้นี้ และบอกว่าบันทึกอะไร
> > [!answer]-
> > กระบวนการแย่ (ไม่มีระดับราคา สวนบริบท ไม่มี Stop) + ผลลัพธ์ดี บันทึกเป็น **ความผิดพลาด**: เป็นช่อง "ฟลุ๊ค" จาก 1.1
> **Q2.** ตอบข้อละบรรทัด: HTF ตัดสินอะไร MTF ตัดสินอะไร LTF ตัดสินอะไร?
> > [!answer]-
> > HTF: ทิศทาง MTF: ตำแหน่ง (ระดับราคาที่จะเทรด) LTF: จังหวะเข้าและ Stop ที่แคบและมีเหตุผล
""")

L.set_meta("level", "v2")
L.save()
