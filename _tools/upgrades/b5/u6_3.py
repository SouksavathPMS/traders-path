"""B5 · v2 upgrade of 6.3 Elliott Wave Rules & Guidelines (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("06 Fibonacci, Elliott Wave & Std Dev/6.3 Elliott Wave Rules & Guidelines.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Anyone can draw numbers on a chart. What makes an Elliott count useful is that it can be **proven wrong**. There are three hard rules; if price breaks one, your count is wrong, full stop. Those break points are exactly where your stop loss belongs. There are also softer "guidelines" that describe what usually happens; they help you choose between counts that pass the rules, but they're allowed to fail.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Rule** — something that must never happen in a valid count; one break = the count is wrong.
> - **Guideline** — something that usually happens; useful for ranking counts, not for rejecting them.
> - **Invalidation** — the price at which a rule breaks; your natural stop level.
> - **Overlap** — wave 4 trading into wave 1's price territory (below wave 1's high in an uptrend).
> - **Diagonal** — a wedge-shaped 5-wave pattern where wave 4 is allowed to overlap wave 1; rare, mostly at the very start (wave 1) or end (wave 5) of a trend.
> - **Extension** — one motive wave much longer than the others, usually wave 3.
> - **Alternation** — waves 2 and 4 tend to look different (one sharp, one sideways).
> - **Channel** — parallel lines through wave ends, used to project where waves 4 and 5 may end.
> - **Divergence** — a new price high with weaker momentum *(see 6.2)*.
> - **Score** — how many guidelines a count matches (used to rank valid counts).
""")
L.before_heading("en", "2.", """
![[p6-count-validator.en.svg]]

> [!walkthrough] Step by step: a count that breaks rule 3, and what it costs
> Swings: 0 = **100**, 1 = **110**, 2 = **103.8**, 3 = **120**, then the pullback reaches **108.5** instead of 113.8.
> 1. **Rule 1:** wave 2 low 103.8 > wave 1 start 100 → ✓.
> 2. **Rule 2:** wave 1 = 10, wave 3 = 120 − 103.8 = 16.2 → wave 3 isn't the shortest so far → ✓.
> 3. **Rule 3:** wave 4 low 108.5 < wave 1 high 110 → ✗. The count 1-2-3-4 is **invalid**.
> 4. **Your trade:** you bought "wave 4" at **113.8** with the rule-3 stop at **109.6**. Price hit 109.6 on the way to 108.5: a loss of 113.8 − 109.6 = 4.2 per unit = **−1R**. The rule did its job: the loss was planned and limited.
> 5. **Relabel:** maybe 103.8 → 120 was only sub-wave (i) of a bigger wave 3 (then 108.5 must hold above 103.8), or the whole rise was a correction. Write both, with their own invalidation levels.
> 6. **So what?** A broken rule is a signal to **exit and re-think**, never to "adjust" the count so you can hold the trade.

> [!check]- Check your understanding: the rules
> **Q1.** Wave 1: 50 → 58. Wave 2 ends at 49.5. Which rule breaks?
> > [!answer]-
> > Rule 1: wave 2 went below wave 1's start (50). It wasn't wave 2.
> **Q2.** Waves: 1 = 12, 3 = 9, 5 = 15. Which rule breaks?
> > [!answer]-
> > Rule 2: wave 3 (9) is the shortest of the three.
""")
L.before_heading("en", "3.", """
> [!analogy]
> The rules are like the **offside rule in football**: break it and the goal doesn't count, however beautiful it was. The guidelines are like **typical tactics**: most teams attack down the wings, but a team that doesn't is still playing football.
>
> **Where it breaks:** a referee decides offside on the spot. In Elliott you're the referee, and the temptation to "not see" a rule break when you're in a trade is strong. Write the numbers down.

> [!check]- Check your understanding: guidelines
> **Q1.** Wave 2 was sharp and deep. What does alternation suggest about wave 4?
> > [!answer]-
> > It's likely to be shallow and sideways (a flat or triangle), not another sharp drop.
> **Q2.** Wave 3 is only 1.2 × wave 1 instead of 1.618. Is the count invalid?
> > [!answer]-
> > No. 1.618 is a guideline. As long as wave 3 isn't the shortest and the other rules hold, the count is valid; it just scores lower.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex & indices:** smooth, liquid trends; rule-based invalidations usually sit at clear swing points.
> - **Gold:** news spikes can briefly poke through a rule level and come back; decide in advance whether you use closes or wicks *(see 0.4)*.
> - **Stocks:** earnings gaps can jump over the invalidation level, so your loss can exceed 1R *(see 0.5)*.
> - **Crypto:** liquidation wicks often break rules intraday; many counters use daily closes *(see 0.7)*.

> [!check]- Check your understanding: invalidation as a stop
> **Q1.** You buy wave 2 at 105 with wave 1 running 100 → 112. Where is the rule-based stop, and what's the risk per unit?
> > [!answer]-
> > Below wave 1's start, 100 (plus a buffer, e.g. 99.5). Risk ≈ 105 − 99.5 = 5.5 per unit.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** State the three rules in one line each.
> > [!answer]-
> > 1) Wave 2 never goes below wave 1's start. 2) Wave 3 is never the shortest of 1, 3 and 5. 3) Wave 4 never overlaps wave 1's price territory (except in diagonals).
> **Q2.** What do you do the moment a rule breaks while you're in the trade?
> > [!answer]-
> > Your stop (placed at the rule level) should already have closed the trade. Then relabel with an alternative count; never move the stop to keep the original story alive.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ใครก็เขียนตัวเลขบนกราฟได้ สิ่งที่ทำให้การนับ Elliott มีประโยชน์คือมัน **พิสูจน์ได้ว่าผิด** มีกฎเหล็กสามข้อ ถ้าราคาผิดกฎข้อใดข้อหนึ่ง การนับของคุณผิด จบ จุดที่ผิดกฎเหล่านั้นคือที่ที่ Stop loss ของคุณควรอยู่พอดี ยังมี "แนวทาง" ที่อ่อนกว่า ซึ่งอธิบายสิ่งที่มักเกิดขึ้น ช่วยเลือกระหว่างการนับที่ผ่านกฎ แต่แนวทางผิดได้
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **กฎ (Rule)** — สิ่งที่ห้ามเกิดในการนับที่ถูกต้อง ผิดข้อเดียว = การนับผิด
> - **แนวทาง (Guideline)** — สิ่งที่มักเกิดขึ้น ใช้จัดอันดับการนับ ไม่ใช้ตัดการนับทิ้ง
> - **Invalidation** — ราคาที่กฎถูกละเมิด คือระดับ Stop ตามธรรมชาติของคุณ
> - **การทับซ้อน (Overlap)** — คลื่น 4 ลงไปในพื้นที่ราคาของคลื่น 1 (ต่ำกว่าจุดสูงคลื่น 1 ในขาขึ้น)
> - **Diagonal** — รูปแบบ 5 คลื่นรูปลิ่มที่อนุญาตให้คลื่น 4 ทับซ้อนคลื่น 1 ได้ พบน้อย ส่วนใหญ่อยู่ตอนต้น (คลื่น 1) หรือตอนท้าย (คลื่น 5) ของเทรนด์
> - **การยืด (Extension)** — คลื่นขับเคลื่อนหนึ่งคลื่นยาวกว่าคลื่นอื่นมาก มักเป็นคลื่น 3
> - **การสลับ (Alternation)** — คลื่น 2 และ 4 มักหน้าตาต่างกัน (อันหนึ่งแหลม อีกอันออกข้าง)
> - **ช่องขนาน (Channel)** — เส้นขนานที่ลากผ่านปลายคลื่น ใช้ฉายว่าคลื่น 4 และ 5 อาจจบตรงไหน
> - **Divergence** — จุดสูงใหม่ที่โมเมนตัมอ่อนลง *(ดู 6.2)*
> - **คะแนน (Score)** — การนับตรงกับแนวทางกี่ข้อ (ใช้จัดอันดับการนับที่ถูกต้อง)
""")
L.before_heading("th", "2.", """
![[p6-count-validator.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: การนับที่ผิดกฎ 3 และราคาที่ต้องจ่าย
> Swing: 0 = **100**, 1 = **110**, 2 = **103.8**, 3 = **120** แล้วการย่อลงไปถึง **108.5** แทนที่จะเป็น 113.8
> 1. **กฎ 1:** จุดต่ำคลื่น 2 103.8 > จุดเริ่มคลื่น 1 100 → ✓
> 2. **กฎ 2:** คลื่น 1 = 10 คลื่น 3 = 120 − 103.8 = 16.2 → คลื่น 3 ยังไม่สั้นที่สุด → ✓
> 3. **กฎ 3:** จุดต่ำคลื่น 4 108.5 < จุดสูงคลื่น 1 110 → ✗ การนับ 1-2-3-4 **ใช้ไม่ได้**
> 4. **ไม้ของคุณ:** คุณซื้อ "คลื่น 4" ที่ **113.8** Stop ตามกฎ 3 ที่ **109.6** ราคาโดน 109.6 ระหว่างทางลงไป 108.5: ขาดทุน 113.8 − 109.6 = 4.2 ต่อหน่วย = **−1R** กฎทำหน้าที่ของมัน: การขาดทุนถูกวางแผนและจำกัดไว้
> 5. **ติดป้ายใหม่:** บางที 103.8 → 120 เป็นแค่คลื่นย่อย (i) ของคลื่น 3 ที่ใหญ่กว่า (ถ้าอย่างนั้น 108.5 ต้องยืนเหนือ 103.8) หรือการขึ้นทั้งหมดเป็นการปรับฐาน เขียนทั้งสองแบบพร้อมระดับ Invalidation ของแต่ละแบบ
> 6. **แล้วไง?** กฎที่ถูกละเมิดคือสัญญาณให้ **ออกและคิดใหม่** ไม่ใช่ "ปรับ" การนับเพื่อจะได้ถือไม้ต่อ

> [!check]- เช็กความเข้าใจ: กฎ
> **Q1.** คลื่น 1: 50 → 58 คลื่น 2 จบที่ 49.5 ผิดกฎข้อไหน?
> > [!answer]-
> > กฎ 1: คลื่น 2 ลงต่ำกว่าจุดเริ่มคลื่น 1 (50) นั่นไม่ใช่คลื่น 2
> **Q2.** คลื่น: 1 = 12, 3 = 9, 5 = 15 ผิดกฎข้อไหน?
> > [!answer]-
> > กฎ 2: คลื่น 3 (9) สั้นที่สุดในสามคลื่น
""")
L.before_heading("th", "3.", """
> [!analogy]
> กฎเหมือน **กฎล้ำหน้าในฟุตบอล**: ละเมิดแล้วประตูไม่นับ ไม่ว่าจะสวยแค่ไหน แนวทางเหมือน **แท็กติกทั่วไป**: ทีมส่วนใหญ่บุกทางปีก แต่ทีมที่ไม่ทำแบบนั้นก็ยังเล่นฟุตบอลอยู่
>
> **จุดที่เปรียบเทียบไม่ได้:** ผู้ตัดสินตัดสินล้ำหน้าทันที แต่ใน Elliott คุณเป็นผู้ตัดสินเอง และเมื่ออยู่ในไม้เทรด คุณจะอยากทำเป็น "ไม่เห็น" การผิดกฎมาก จดตัวเลขไว้

> [!check]- เช็กความเข้าใจ: แนวทาง
> **Q1.** คลื่น 2 แหลมและลึก การสลับบอกอะไรเกี่ยวกับคลื่น 4?
> > [!answer]-
> > คลื่น 4 น่าจะตื้นและออกข้าง (Flat หรือ Triangle) ไม่ใช่การร่วงแหลมอีกครั้ง
> **Q2.** คลื่น 3 ยาวแค่ 1.2 × คลื่น 1 แทนที่จะเป็น 1.618 การนับใช้ไม่ได้ไหม?
> > [!answer]-
> > ใช้ได้ 1.618 เป็นแนวทาง ตราบใดที่คลื่น 3 ไม่สั้นที่สุดและกฎอื่นยังผ่าน การนับก็ถูกต้อง แค่ได้คะแนนต่ำลง
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์และดัชนี:** เทรนด์ราบเรียบและมีสภาพคล่อง ระดับ Invalidation ตามกฎมักอยู่ที่จุด Swing ที่ชัดเจน
> - **ทองคำ:** ข่าวพุ่งอาจทะลุระดับกฎชั่วครู่แล้วกลับมา ตัดสินใจล่วงหน้าว่าจะใช้ราคาปิดหรือไส้ *(ดู 0.4)*
> - **หุ้น:** Gap จากงบอาจกระโดดข้ามระดับ Invalidation ขาดทุนจึงเกิน 1R ได้ *(ดู 0.5)*
> - **คริปโต:** ไส้จากการล้างพอร์ตมักผิดกฎระหว่างวัน นักนับหลายคนใช้ราคาปิดรายวัน *(ดู 0.7)*

> [!check]- เช็กความเข้าใจ: Invalidation คือ Stop
> **Q1.** คุณซื้อคลื่น 2 ที่ 105 โดยคลื่น 1 วิ่ง 100 → 112 Stop ตามกฎอยู่ที่ไหน และความเสี่ยงต่อหน่วยเท่าไหร่?
> > [!answer]-
> > ใต้จุดเริ่มคลื่น 1 คือ 100 (บวกระยะเผื่อ เช่น 99.5) ความเสี่ยง ≈ 105 − 99.5 = 5.5 ต่อหน่วย
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกกฎสามข้อ ข้อละบรรทัด
> > [!answer]-
> > 1) คลื่น 2 ไม่เคยลงต่ำกว่าจุดเริ่มคลื่น 1 2) คลื่น 3 ไม่เคยสั้นที่สุดในคลื่น 1, 3, 5 3) คลื่น 4 ไม่เคยทับซ้อนพื้นที่ราคาของคลื่น 1 (ยกเว้นใน Diagonal)
> **Q2.** ทันทีที่กฎถูกละเมิดระหว่างที่คุณอยู่ในไม้ คุณทำอย่างไร?
> > [!answer]-
> > Stop ของคุณ (วางไว้ที่ระดับของกฎ) ควรปิดไม้ไปแล้ว จากนั้นติดป้ายใหม่ด้วยการนับสำรอง ห้ามเลื่อน Stop เพื่อให้เรื่องเดิมยังอยู่
""")

L.set_meta("level", "v2")
L.save()
