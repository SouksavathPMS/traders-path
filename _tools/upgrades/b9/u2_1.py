"""B9b · v2 upgrade of 2.1 Swings: HH, HL, LH, LL (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("02 Market Structure/2.1 Swings- HH, HL, LH, LL.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Price moves like a person climbing stairs: two steps up, one step back, two steps up. Each turning point is a swing. If every peak is higher than the last peak and every dip is higher than the last dip, buyers are winning. If they're all lower, sellers are winning. Comparing turning points is the simplest way to read who is in control.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Swing high / swing low** — a peak / trough where price turned.
> - **Impulse leg** — a move in the direction of control; usually longer and faster.
> - **Pullback (correction)** — a move against it; usually shorter and slower.
> - **HH / HL** — higher high / higher low: buyers in control.
> - **LH / LL** — lower high / lower low: sellers in control.
> - **Contraction / expansion** — LH + HL (a squeeze) / HH + LL (wild swings, no control).
> - **Fractal (5-candle rule)** — a swing high is above the 2 candles on each side; a swing low is below them.
> - **Confirmed swing** — one whose 2 candles on the right have closed.
> - **Major / minor swing** — a meaningful turning point / a small pause inside a leg.
> - **Bar replay** — a platform tool that hides the future and plays candles one by one.
""")
L.before_heading("en", "2.", """
> [!analogy]
> Reading swings is like watching a **tug of war** from above. You don't need to see every pull. You only check where the rope's centre ends up after each big heave and each rest. If it ends further towards one team every time, that team is winning.
>
> **Where it breaks:** a tug of war has two fixed teams. In markets, people switch sides all the time, and a new large player can change the result in one move.

> [!check]- Check your understanding: impulse and pullback
> **Q1.** In an uptrend, which legs are the impulses, and which are the pullbacks? How do they usually differ?
> > [!answer]-
> > Up legs are impulses, down legs are pullbacks. Impulses are usually longer and faster; pullbacks shorter and slower.
""")
L.before_heading("en", "3.", """
> [!check]- Check your understanding: the four labels
> **Q1.** Highs: 80 → 83 → 81. Lows: 75 → 78 → 79. Label the last high and the last low, then name the state.
> > [!answer]-
> > 81 is an **LH** (below 83); 79 is an **HL** (above 78). LH + HL = **contraction**: a squeeze or a range is forming.
""")
L.before_callout("en", "example", """
![[p2-fractal-rule.en.svg]]

> [!walkthrough] Step by step: applying the 5-candle rule
> Candle highs (left to right): 101, 102.5, **104**, 103.6, 102, 103.5, **105.5**, 105.2, 104, **106.2**, 106.
> 1. **104** is above 101, 102.5 (left) and 103.6, 102 (right) → swing high, confirmed.
> 2. **105.5** is above 102, 103.5 and 105.2, 104 → swing high, confirmed. 105.5 > 104 → **HH**.
> 3. Swing lows by the same rule: **100.2** and then **102.6** → 102.6 > 100.2 → **HL**.
> 4. **106.2** is above everything near it, but only **one** candle has closed on its right → **possible**, not confirmed yet.
> 5. **So what?** Read the state from confirmed swings only: HH + HL = uptrend. Labelling 106.2 too early is how traders "see" swings that later disappear.

> [!check]- Check your understanding: confirmation
> **Q1.** A candle makes a new high, and the next candle has a lower high. Can you mark a confirmed swing high yet?
> > [!answer]-
> > No. One candle on the right isn't enough; you need **two** closed candles with lower highs.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** clean swings on 4H and daily; the Asian session often adds minor swings to ignore *(see 0.3)*.
> - **Gold:** news spikes create sharp swing points; check whether a swing came from one release candle *(see 0.4)*.
> - **Stocks:** overnight gaps can skip swings; use daily charts for structure *(see 0.5)*.
> - **Crypto:** 24/7 trading gives continuous swings with no gaps, but weekend swings are often minor *(see 0.7)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** What does a higher low tell you about buyers' behaviour?
> > [!answer]-
> > Buyers stepped in earlier, at a higher price than last time: demand is getting more eager.
> **Q2.** Highs: 120 → 124 → 127. Lows: 115 → 113 → 110. What's the state, and what should you do?
> > [!answer]-
> > HH + LL = **expansion**: volatile, no side in control. Trade smaller or stand aside.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ราคาขยับเหมือนคนขึ้นบันได: ขึ้นสองขั้น ถอยหนึ่งขั้น ขึ้นอีกสองขั้น แต่ละจุดกลับตัวคือสวิง ถ้ายอดทุกครั้งสูงกว่ายอดก่อน และจุดย่อทุกครั้งสูงกว่าจุดย่อก่อน ผู้ซื้อกำลังชนะ ถ้าต่ำลงทั้งหมด ผู้ขายกำลังชนะ การเทียบจุดกลับตัวคือวิธีที่ง่ายที่สุดในการอ่านว่าใครคุมเกม
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **จุดสวิงสูง / จุดสวิงต่ำ (Swing high / Swing low)** — ยอด / จุดต่ำที่ราคากลับตัว
> - **ขาแรงส่ง (Impulse leg)** — การขยับในทิศทางของฝ่ายที่คุมเกม มักยาวและเร็วกว่า
> - **การย่อ (Pullback / Correction)** — การขยับสวนทาง มักสั้นและช้ากว่า
> - **HH / HL** — จุดสูงที่สูงขึ้น / จุดต่ำที่สูงขึ้น: ผู้ซื้อคุมเกม
> - **LH / LL** — จุดสูงที่ต่ำลง / จุดต่ำที่ต่ำลง: ผู้ขายคุมเกม
> - **บีบตัว / ขยายตัว (Contraction / Expansion)** — LH + HL (การบีบ) / HH + LL (แกว่งแรง ไม่มีใครคุม)
> - **Fractal (กฎ 5 แท่ง)** — จุดสวิงสูงอยู่เหนือ 2 แท่งทั้งสองข้าง จุดสวิงต่ำอยู่ใต้ 2 แท่งทั้งสองข้าง
> - **สวิงที่ยืนยันแล้ว (Confirmed swing)** — สวิงที่ 2 แท่งด้านขวาปิดแล้ว
> - **สวิงหลัก / สวิงย่อย (Major / Minor swing)** — จุดกลับตัวที่มีความหมาย / การหยุดพักเล็ก ๆ ภายในขาราคา
> - **Bar replay** — เครื่องมือในแพลตฟอร์มที่ซ่อนอนาคตและเล่นแท่งเทียนทีละแท่ง
""")
L.before_heading("th", "2.", """
> [!analogy]
> การอ่านสวิงเหมือนดู **การชักเย่อ** จากด้านบน คุณไม่ต้องเห็นทุกการดึง แค่ดูว่ากึ่งกลางเชือกไปอยู่ตรงไหนหลังการดึงแรงแต่ละครั้งและการพักแต่ละครั้ง ถ้าทุกครั้งมันไปทางทีมหนึ่งมากขึ้น ทีมนั้นกำลังชนะ
>
> **จุดที่เปรียบเทียบไม่ได้:** การชักเย่อมีสองทีมที่ตายตัว แต่ในตลาด คนเปลี่ยนข้างตลอดเวลา และผู้เล่นรายใหญ่รายใหม่สามารถเปลี่ยนผลได้ในการขยับครั้งเดียว

> [!check]- เช็กความเข้าใจ: แรงส่งและการย่อ
> **Q1.** ในขาขึ้น ขาไหนคือแรงส่ง ขาไหนคือการย่อ และมักต่างกันอย่างไร?
> > [!answer]-
> > ขาขึ้นคือแรงส่ง ขาลงคือการย่อ แรงส่งมักยาวและเร็วกว่า การย่อสั้นและช้ากว่า
""")
L.before_heading("th", "3.", """
> [!check]- เช็กความเข้าใจ: ป้าย 4 แบบ
> **Q1.** จุดสูง: 80 → 83 → 81 จุดต่ำ: 75 → 78 → 79 ติดป้ายจุดสูงและจุดต่ำล่าสุด แล้วบอกสภาวะ
> > [!answer]-
> > 81 คือ **LH** (ต่ำกว่า 83) 79 คือ **HL** (สูงกว่า 78) LH + HL = **บีบตัว**: กำลังเกิดการบีบหรือกรอบราคา
""")
L.before_callout("th", "example", """
![[p2-fractal-rule.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ใช้กฎ 5 แท่ง
> ราคาสูงสุดของแท่ง (ซ้ายไปขวา): 101, 102.5, **104**, 103.6, 102, 103.5, **105.5**, 105.2, 104, **106.2**, 106
> 1. **104** สูงกว่า 101, 102.5 (ซ้าย) และ 103.6, 102 (ขวา) → จุดสวิงสูง ยืนยันแล้ว
> 2. **105.5** สูงกว่า 102, 103.5 และ 105.2, 104 → จุดสวิงสูง ยืนยันแล้ว 105.5 > 104 → **HH**
> 3. จุดสวิงต่ำด้วยกฎเดียวกัน: **100.2** แล้ว **102.6** → 102.6 > 100.2 → **HL**
> 4. **106.2** สูงกว่าทุกแท่งรอบข้าง แต่ด้านขวาปิดแล้วแค่ **หนึ่ง** แท่ง → **อาจเป็น** ยังไม่ยืนยัน
> 5. **แล้วไง?** อ่านสภาวะจากสวิงที่ยืนยันแล้วเท่านั้น: HH + HL = ขาขึ้น การติดป้าย 106.2 เร็วเกินไปคือวิธีที่นักเทรด "เห็น" สวิงที่หายไปทีหลัง

> [!check]- เช็กความเข้าใจ: การยืนยัน
> **Q1.** แท่งหนึ่งทำจุดสูงใหม่ และแท่งถัดไปมีจุดสูงที่ต่ำกว่า ติดป้ายจุดสวิงสูงที่ยืนยันแล้วได้หรือยัง?
> > [!answer]-
> > ยังไม่ได้ แท่งเดียวด้านขวาไม่พอ ต้องมี **สอง** แท่งที่ปิดแล้วและมีจุดสูงต่ำกว่า
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** สวิงชัดบน 4H และรายวัน ช่วงเอเชียมักเพิ่มสวิงย่อยที่ควรมองข้าม *(ดู 0.3)*
> - **ทองคำ:** การพุ่งช่วงข่าวสร้างจุดสวิงที่แหลมคม ตรวจว่าสวิงมาจากแท่งประกาศข้อมูลแท่งเดียวหรือไม่ *(ดู 0.4)*
> - **หุ้น:** Gap ข้ามคืนอาจข้ามสวิงไป ใช้กราฟรายวันในการอ่านโครงสร้าง *(ดู 0.5)*
> - **คริปโต:** ซื้อขาย 24/7 ให้สวิงต่อเนื่องไม่มี Gap แต่สวิงช่วงสุดสัปดาห์มักเป็นสวิงย่อย *(ดู 0.7)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** จุดต่ำที่สูงขึ้นบอกอะไรเกี่ยวกับพฤติกรรมของผู้ซื้อ?
> > [!answer]-
> > ผู้ซื้อเข้ามาเร็วขึ้น ที่ราคาสูงกว่าครั้งก่อน: ความต้องการซื้อกระตือรือร้นขึ้น
> **Q2.** จุดสูง: 120 → 124 → 127 จุดต่ำ: 115 → 113 → 110 สภาวะคืออะไร และควรทำอะไร?
> > [!answer]-
> > HH + LL = **ขยายตัว**: ผันผวน ไม่มีฝ่ายไหนคุม เทรดเล็กลงหรือหยุดดู
""")

L.set_meta("level", "v2")
L.save()
