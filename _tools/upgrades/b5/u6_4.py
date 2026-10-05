"""B5 · v2 upgrade of 6.4 Corrective Patterns: Zigzag, Flat, Triangle (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("06 Fibonacci, Elliott Wave & Std Dev/6.4 Corrective Patterns- Zigzag, Flat, Triangle.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> After a strong move, the market needs to rest before it can move again. That rest is a **correction**, and it can take three main shapes: a sharp drop (zigzag), a sideways back-and-forth (flat), or a narrowing range (triangle). Corrections are messy and fool traders on both sides. The skill here is mostly **patience**: recognise "we're resting", don't trade every wiggle, and get ready for the moment the rest ends.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Correction** — a move against the larger trend, made of overlapping, choppy swings.
> - **Zigzag (5-3-5)** — a sharp, deep correction: wave A in 5 sub-waves, B in 3, C in 5.
> - **Flat (3-3-5)** — a sideways correction: A in 3, B in 3 (returning near A's start), C in 5.
> - **Expanded flat** — a flat where B goes beyond A's start and C goes beyond A's end.
> - **Triangle (3-3-3-3-3)** — a contracting range of five legs, A-B-C-D-E, each in 3.
> - **Thrust** — the fast move out of a triangle in the trend direction.
> - **Combination (W-X-Y)** — two corrections joined by a connecting wave X.
> - **Sub-waves** — the smaller waves inside each leg (i-v for 5-wave legs, a-b-c for 3-wave legs).
> - **C = A** — the common guideline that wave C is about as long as wave A (also 1.618 × A).
> - **CHoCH** — change of character, here used as the signal that the correction has ended *(see 2.3)*.
""")
L.before_heading("en", "2.", """
![[p6-corrections-subwaves.en.svg]]

> [!analogy]
> A flat is the market **catching its breath** after a sprint: it stops, walks back a little, walks forward again to almost where it stopped, then steps back once more before running on. A zigzag is a runner who trips and falls hard, then gets up. A triangle is a runner jogging on the spot in smaller and smaller steps before sprinting off.
>
> **Where it breaks:** a runner always rests the same way. Corrections change shape while they form: a flat can turn into a triangle or a combination, so you often only know the shape at the end.

> [!walkthrough] Step by step: where a zigzag's C may end (as wave 2)
> Wave 1: **100 → 110**. Wave A drops to **105** (A = 5). Wave B bounces to **107.5** (50% of A).
> 1. **C = A:** 107.5 − 5 = **102.5**.
> 2. **C = 1.618 × A:** 107.5 − 1.618 × 5 = 107.5 − 8.09 = **99.41**.
> 3. **Rule check:** as wave 2, the correction may not go below wave 1's start (**100**). So 99.41 is **impossible** for a valid wave 2; if price gets there, the count is wrong.
> 4. **Fib check:** 61.8–78.6% of wave 1 = **103.8–102.1**. Together with C = A (102.5), the target zone is about **102.1–103.8**.
> 5. **So what?** Two independent measurements plus a rule shrink "somewhere below 107.5" into a 1.7-point zone with a hard invalidation at 100.

> [!check]- Check your understanding: zigzag
> **Q1.** A = 8 points, B ends at 92. Where does C end if C = A? If C = 1.618 × A (falling correction)?
> > [!answer]-
> > C = A: 92 − 8 = 84. C = 1.618 × A: 92 − 12.94 = 79.06.
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: measuring a flat
> After an up-trend, wave A falls **110 → 105** (A = 5).
> 1. **B returns about 90% of A:** 105 + 0.9 × 5 = **109.5** (sideways, not a new high).
> 2. **C = A from B:** 109.5 − 5 = **104.5**, just below A's end (105).
> 3. **C = 1.272 × A:** 109.5 − 6.36 = **103.14** (a common "expanded" target).
> 4. **So what?** In a flat, wave C typically **sweeps** A's low (105): the stops of traders who bought there get taken (5.2), then the trend resumes. That sweep is often the entry, not the warning.

> [!check]- Check your understanding: flat and triangle
> **Q1.** Price has made five contracting swings (A-B-C-D-E) in an uptrend. What do you wait for?
> > [!answer]-
> > A close outside the triangle in the trend direction (the thrust), or a sweep of one side followed by a reversal back into the trend. Not an entry inside the triangle.
> **Q2.** Why is wave B of a flat dangerous to short in an uptrend?
> > [!answer]-
> > B often returns 90–100% of A or even beyond A's start (expanded flat), stopping out shorts; and the larger trend is still up.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** most of the time pairs are correcting; triangles before big data releases are common.
> - **Gold:** corrections often include sharp spikes (news) that look like zigzags inside flats *(see 0.4)*.
> - **Stocks & indices:** wave C often ends near an earnings date or a big index level; overnight gaps distort shapes *(see 0.5)*.
> - **Crypto:** expanded flats with deep liquidation sweeps of A's low are very common *(see 0.7)*.

> [!caution]
> Most losses with Elliott happen inside corrections: overlapping swings stop out both longs and shorts. If you can't tell which correction it is, that's the answer: stay out or reduce size until a clear CHoCH in the trend direction appears.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Match the shape to its internal structure: zigzag, flat, triangle.
> > [!answer]-
> > Zigzag 5-3-5; flat 3-3-5; triangle 3-3-3-3-3.
> **Q2.** You're unsure which correction is forming. What's the practical approach?
> > [!answer]-
> > Label it simply "correction", mark C = A / 1.618 × A and the Fib zone of the prior impulse, and wait for an LTF CHoCH in the trend direction in that zone.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> หลังการวิ่งแรง ตลาดต้องพักก่อนจะวิ่งต่อ การพักนั้นคือ **การปรับฐาน** มีหน้าตาหลักสามแบบ: ร่วงแหลม (Zigzag) แกว่งออกข้างไปมา (Flat) หรือกรอบที่แคบลงเรื่อย ๆ (Triangle) การปรับฐานยุ่งเหยิงและหลอกเทรดเดอร์ทั้งสองฝั่ง ทักษะที่นี่ส่วนใหญ่คือ **ความอดทน**: รู้ว่า "ตอนนี้กำลังพัก" ไม่เทรดทุกการแกว่ง และเตรียมพร้อมสำหรับจังหวะที่การพักจบ
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **การปรับฐาน (Correction)** — การวิ่งสวนเทรนด์ใหญ่ ประกอบด้วย Swing ที่ซ้อนกันและไม่เป็นระเบียบ
> - **Zigzag (5-3-5)** — การปรับฐานแหลมและลึก: คลื่น A มี 5 คลื่นย่อย B มี 3 C มี 5
> - **Flat (3-3-5)** — การปรับฐานออกข้าง: A มี 3 B มี 3 (กลับไปใกล้จุดเริ่มของ A) C มี 5
> - **Expanded flat** — Flat ที่ B เลยจุดเริ่มของ A และ C เลยจุดจบของ A
> - **Triangle (3-3-3-3-3)** — กรอบที่แคบลง มีห้าขา A-B-C-D-E แต่ละขามี 3
> - **Thrust** — การวิ่งเร็วออกจาก Triangle ในทิศทางของเทรนด์
> - **Combination (W-X-Y)** — การปรับฐานสองชุดเชื่อมกันด้วยคลื่น X
> - **คลื่นย่อย (Sub-waves)** — คลื่นเล็กภายในแต่ละขา (i-v สำหรับขาแบบ 5 คลื่น a-b-c สำหรับขาแบบ 3 คลื่น)
> - **C = A** — แนวทางทั่วไปว่าคลื่น C ยาวพอ ๆ กับคลื่น A (หรือ 1.618 × A)
> - **CHoCH** — การเปลี่ยนนิสัย ที่นี่ใช้เป็นสัญญาณว่าการปรับฐานจบแล้ว *(ดู 2.3)*
""")
L.before_heading("th", "2.", """
![[p6-corrections-subwaves.th.svg]]

> [!analogy]
> Flat คือตลาด **พักหายใจ** หลังวิ่งสปรินต์: หยุด เดินถอยนิดหนึ่ง เดินไปข้างหน้าเกือบถึงจุดที่หยุด แล้วถอยอีกก้าวก่อนวิ่งต่อ Zigzag คือนักวิ่งที่สะดุดล้มแรงแล้วลุกขึ้น Triangle คือนักวิ่งที่วิ่งเหยาะอยู่กับที่ด้วยก้าวที่เล็กลงเรื่อย ๆ ก่อนพุ่งออกไป
>
> **จุดที่เปรียบเทียบไม่ได้:** นักวิ่งพักแบบเดิมเสมอ แต่การปรับฐานเปลี่ยนรูประหว่างก่อตัว Flat อาจกลายเป็น Triangle หรือ Combination คุณจึงมักรู้รูปทรงตอนจบเท่านั้น

> [!walkthrough] ไล่ทีละขั้น: C ของ Zigzag อาจจบตรงไหน (ในฐานะคลื่น 2)
> คลื่น 1: **100 → 110** คลื่น A ลงถึง **105** (A = 5) คลื่น B เด้งถึง **107.5** (50% ของ A)
> 1. **C = A:** 107.5 − 5 = **102.5**
> 2. **C = 1.618 × A:** 107.5 − 1.618 × 5 = 107.5 − 8.09 = **99.41**
> 3. **ตรวจกฎ:** ในฐานะคลื่น 2 การปรับฐานลงต่ำกว่าจุดเริ่มคลื่น 1 (**100**) ไม่ได้ 99.41 จึง **เป็นไปไม่ได้** สำหรับคลื่น 2 ที่ถูกต้อง ถ้าราคาไปถึง การนับผิด
> 4. **ตรวจฟีโบ:** 61.8–78.6% ของคลื่น 1 = **103.8–102.1** รวมกับ C = A (102.5) โซนเป้าคือราว **102.1–103.8**
> 5. **แล้วไง?** การวัดอิสระสองแบบบวกกฎหนึ่งข้อ ย่อ "ที่ไหนสักแห่งใต้ 107.5" ให้เหลือโซนกว้าง 1.7 จุด พร้อมจุด Invalidation ที่ชัดเจนที่ 100

> [!check]- เช็กความเข้าใจ: Zigzag
> **Q1.** A = 8 จุด B จบที่ 92 C จบที่ไหนถ้า C = A? ถ้า C = 1.618 × A (การปรับฐานขาลง)?
> > [!answer]-
> > C = A: 92 − 8 = 84  C = 1.618 × A: 92 − 12.94 = 79.06
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: วัด Flat
> หลังเทรนด์ขาขึ้น คลื่น A ลง **110 → 105** (A = 5)
> 1. **B กลับไปราว 90% ของ A:** 105 + 0.9 × 5 = **109.5** (ออกข้าง ไม่ใช่จุดสูงใหม่)
> 2. **C = A จาก B:** 109.5 − 5 = **104.5** ต่ำกว่าจุดจบของ A (105) นิดเดียว
> 3. **C = 1.272 × A:** 109.5 − 6.36 = **103.14** (เป้า "Expanded" ที่พบบ่อย)
> 4. **แล้วไง?** ใน Flat คลื่น C มัก **กวาด** จุดต่ำของ A (105): Stop ของคนที่ซื้อตรงนั้นถูกเก็บ (5.2) แล้วเทรนด์ไปต่อ การกวาดนั้นมักเป็นจุดเข้า ไม่ใช่คำเตือน

> [!check]- เช็กความเข้าใจ: Flat และ Triangle
> **Q1.** ราคาทำ Swing ที่แคบลงห้าครั้ง (A-B-C-D-E) ในเทรนด์ขาขึ้น คุณรออะไร?
> > [!answer]-
> > รอการปิดนอก Triangle ในทิศทางของเทรนด์ (Thrust) หรือการกวาดฝั่งหนึ่งแล้วกลับตัวเข้าสู่เทรนด์ ไม่ใช่เข้าภายใน Triangle
> **Q2.** ทำไมการ Short คลื่น B ของ Flat ในเทรนด์ขาขึ้นจึงอันตราย?
> > [!answer]-
> > B มักกลับไป 90–100% ของ A หรือเลยจุดเริ่มของ A ด้วยซ้ำ (Expanded flat) ทำให้ Short โดน Stop และเทรนด์ใหญ่ยังเป็นขาขึ้น
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** ส่วนใหญ่คู่เงินอยู่ในช่วงปรับฐาน Triangle ก่อนข้อมูลสำคัญพบบ่อย
> - **ทองคำ:** การปรับฐานมักมีการพุ่งแหลม (ข่าว) ที่ดูเหมือน Zigzag ซ้อนอยู่ใน Flat *(ดู 0.4)*
> - **หุ้นและดัชนี:** คลื่น C มักจบใกล้วันประกาศงบหรือระดับดัชนีสำคัญ Gap ข้ามคืนบิดเบือนรูปทรง *(ดู 0.5)*
> - **คริปโต:** Expanded flat ที่กวาดจุดต่ำของ A ลึกจากการล้างพอร์ตพบบ่อยมาก *(ดู 0.7)*

> [!caution]
> การขาดทุนส่วนใหญ่กับ Elliott เกิดภายในการปรับฐาน: Swing ที่ซ้อนกันทำให้ทั้ง Long และ Short โดน Stop ถ้าคุณบอกไม่ได้ว่าเป็นการปรับฐานแบบไหน นั่นคือคำตอบ: อยู่นอกตลาดหรือลดขนาด จนกว่าจะเห็น CHoCH ที่ชัดเจนในทิศทางของเทรนด์
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** จับคู่รูปทรงกับโครงสร้างภายใน: Zigzag, Flat, Triangle
> > [!answer]-
> > Zigzag 5-3-5; Flat 3-3-5; Triangle 3-3-3-3-3
> **Q2.** คุณไม่แน่ใจว่ากำลังเกิดการปรับฐานแบบไหน วิธีปฏิบัติคืออะไร?
> > [!answer]-
> > ติดป้ายง่าย ๆ ว่า "การปรับฐาน" ทำเครื่องหมาย C = A / 1.618 × A และโซนฟีโบของแรงส่งก่อนหน้า แล้วรอ CHoCH บน LTF ในทิศทางของเทรนด์ในโซนนั้น
""")

L.set_meta("level", "v2")
L.save()
