"""B5 · v2 upgrade of 6.1 Fibonacci Retracements & Extensions (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("06 Fibonacci, Elliott Wave & Std Dev/6.1 Fibonacci Retracements & Extensions.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> After price rises, it usually falls back a bit before rising again. Fibonacci levels are a standard set of "how far back" marks (about a quarter, a third, a half, two thirds of the rise) that almost every trader draws the same way. Because so many people watch the same marks, orders gather there, and price often pauses near one of them. Fibonacci can also project how far the next rise might go. It's a ruler everyone shares, not a prediction machine.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Fibonacci sequence** — 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89…: each number is the sum of the two before it.
> - **Golden ratio** — about 1.618 (and its inverse 0.618), the value that neighbouring Fibonacci numbers approach.
> - **Swing high / swing low** — turning points of price *(see 2.1)*.
> - **Leg** — one move from a swing low to a swing high, or the reverse.
> - **Retracement** — how far price pulls back into the previous leg, as a percentage of that leg.
> - **Extension / projection** — a target beyond the leg, measured as a multiple of a previous leg.
> - **A, B, C (anchors)** — the start of the leg (A), its end (B) and the end of the pullback (C).
> - **AB = CD** — the idea that the next leg (C→D) often equals the previous one (A→B).
> - **BOS / CHoCH** — break of structure / change of character *(see 2.3)*.
> - **OTE** — ICT's 62–79% retracement zone *(see 5.3)*.
> - **Confluence** — several independent reasons pointing at the same price.
> - **Self-fulfilling** — something that works partly because many people believe in it and act on it.
""")
L.before_heading("en", "2.", """
> [!walkthrough] Step by step: where 0.618 comes from (no mysticism)
> 1. Take neighbouring Fibonacci numbers and divide: 21 ÷ 34 = **0.6176**, 34 ÷ 55 = **0.6182**, 55 ÷ 89 = **0.6180**. The further you go, the closer it gets to **0.618**.
> 2. Divide by the number two places ahead: 34 ÷ 89 = **0.382**. And 0.618 × 0.618 ≈ 0.382.
> 3. **0.786** is just √0.618 ≈ **0.786**; **0.5** isn't a Fibonacci ratio at all, it's added because it's the midpoint.
> 4. **So what?** The ratios are simple arithmetic. They matter in markets mainly because **everyone draws them**, so orders and decisions cluster there. Treat them as a shared ruler, and only trust a level when something else (structure, a zone, liquidity) agrees.

> [!check]- Check your understanding: the ratios
> **Q1.** Is there evidence that markets "obey" the golden ratio?
> > [!answer]-
> > No good evidence. Fib levels work partly because many traders watch them (self-fulfilling) and partly because pullbacks of a third to two thirds are simply common.
""")
L.before_heading("en", "3.", """
![[p6-fib-candles.en.svg]]

> [!analogy]
> A Fibonacci tool is like the **marks on a measuring tape**. The tape doesn't make the plank stop at 60 cm; it just lets everyone describe "about two thirds of the way" in the same words. When thousands of builders all agree to cut at the same mark, though, you'll find a lot of sawdust there.
>
> **Where it breaks:** a tape measure is exact and fixed. Fibonacci depends on which swing you choose as the start and end; pick different anchors and every level moves.

> [!walkthrough] Step by step: retracement levels for a swing from 100 to 150
> Leg A = **100** → B = **150**, so the leg is **50** points. Each level = B − ratio × 50.
> 1. **23.6%:** 150 − 0.236 × 50 = 150 − 11.8 = **138.2**.
> 2. **38.2%:** 150 − 19.1 = **130.9**.
> 3. **50%:** 150 − 25 = **125.0**.
> 4. **61.8%:** 150 − 30.9 = **119.1**.
> 5. **78.6%:** 150 − 39.3 = **110.7**.
> 6. **So what?** In the figure the pullback stopped at 130.9 (38.2%): shallow, a sign of a strong trend. A stop for a long would go below the next meaningful level and the structure (below 125 or 119), and size comes from that distance *(see 3.2)*.

> [!check]- Check your understanding: retracements
> **Q1.** A down-leg runs from 80 to 60. Where is the 61.8% retracement?
> > [!answer]-
> > Leg = 20. The retracement goes back **up**: 60 + 0.618 × 20 = 72.36.
> **Q2.** Price falls through 100% of the up-leg (below its start). What does that mean?
> > [!answer]-
> > The swing low broke: a CHoCH against the trend. The leg is no longer valid as a pullback in an uptrend.
""")
L.before_callout("en", "example", """
> [!walkthrough] Step by step: projecting the next leg from C = 130.9
> A→B = 50 points. C (the pullback low) = **130.9**. Target = C + ratio × 50.
> 1. **1.0 (AB = CD):** 130.9 + 50 = **180.9**.
> 2. **1.272:** 130.9 + 63.6 = **194.5**.
> 3. **1.618:** 130.9 + 80.9 = **211.8**.
> 4. **So what?** These are **possible** targets. Choose the one nearest to a liquidity pool or HTF level (5.1) and take partial profit there; don't hold everything for 1.618 because it "should" get there.

> [!check]- Check your understanding: extensions
> **Q1.** A = 50, B = 60, C = 56. What is the 1.618 projection?
> > [!answer]-
> > A→B = 10. 56 + 1.618 × 10 = 72.18.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** Fib levels on daily and 4H swings are widely watched; pip-precise touches are rare, so think in zones.
> - **Gold:** large swings (50–150 USD) make the gap between levels big; combine with round numbers *(see 0.4)*.
> - **Stocks & indices:** draw on regular-session prices; overnight gaps can jump straight past a level *(see 0.5)*.
> - **Crypto:** deep wicks from liquidations often overshoot to 78.6% or beyond; wait for a close-based trigger *(see 0.7)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Swing 200 → 260. Give the 38.2%, 50% and 61.8% retracements.
> > [!answer]-
> > Leg 60. 38.2% = 260 − 22.92 = 237.08; 50% = 230; 61.8% = 260 − 37.08 = 222.92.
> **Q2.** Why does a lone Fib level make a weak entry reason?
> > [!answer]-
> > With five levels, price is almost always near one. A level only matters when it lines up with structure, a zone, an FVG or liquidity, and an LTF trigger confirms it.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> หลังราคาขึ้น มักย่อลงนิดหนึ่งก่อนขึ้นต่อ ระดับฟีโบนัชชีคือชุดเครื่องหมาย "ย่อกลับไปแค่ไหน" มาตรฐาน (ราวหนึ่งในสี่ หนึ่งในสาม ครึ่งหนึ่ง สองในสามของการขึ้น) ที่เทรดเดอร์แทบทุกคนวาดแบบเดียวกัน เพราะคนจำนวนมากดูเครื่องหมายเดียวกัน คำสั่งจึงไปกองอยู่ตรงนั้น และราคามักหยุดพักใกล้ระดับใดระดับหนึ่ง ฟีโบนัชชียังใช้คาดว่าการขึ้นรอบถัดไปจะไปไกลแค่ไหนได้ด้วย มันคือไม้บรรทัดที่ทุกคนใช้ร่วมกัน ไม่ใช่เครื่องทำนาย
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **ลำดับฟีโบนัชชี (Fibonacci sequence)** — 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89…: แต่ละตัวคือผลรวมของสองตัวก่อนหน้า
> - **อัตราส่วนทองคำ (Golden ratio)** — ประมาณ 1.618 (และส่วนกลับ 0.618) ค่าที่อัตราส่วนของเลขฟีโบนัชชีที่อยู่ติดกันเข้าใกล้
> - **Swing high / Swing low** — จุดกลับตัวของราคา *(ดู 2.1)*
> - **ขา (Leg)** — การวิ่งหนึ่งครั้งจาก Swing low ถึง Swing high หรือกลับกัน
> - **รีเทรซเมนต์ (Retracement)** — ราคาย่อกลับเข้าไปในขาก่อนหน้ามากแค่ไหน คิดเป็นเปอร์เซ็นต์ของขานั้น
> - **เอกซ์เทนชัน / การฉายเป้า (Extension / Projection)** — เป้าหมายที่อยู่เลยขาออกไป วัดเป็นจำนวนเท่าของขาก่อนหน้า
> - **A, B, C (จุดยึด)** — จุดเริ่มของขา (A) จุดจบ (B) และจุดจบของการย่อ (C)
> - **AB = CD** — แนวคิดว่าขาถัดไป (C→D) มักยาวเท่าขาก่อนหน้า (A→B)
> - **BOS / CHoCH** — การทะลุโครงสร้าง / การเปลี่ยนนิสัย *(ดู 2.3)*
> - **OTE** — โซนย่อกลับ 62–79% ของ ICT *(ดู 5.3)*
> - **Confluence (จุดบรรจบ)** — เหตุผลอิสระหลายข้อที่ชี้ไปที่ราคาเดียวกัน
> - **คำทำนายที่เป็นจริงเพราะคนเชื่อ (Self-fulfilling)** — สิ่งที่ได้ผลส่วนหนึ่งเพราะคนจำนวนมากเชื่อและทำตาม
""")
L.before_heading("th", "2.", """
> [!walkthrough] ไล่ทีละขั้น: 0.618 มาจากไหน (ไม่มีเรื่องลึกลับ)
> 1. เอาเลขฟีโบนัชชีที่อยู่ติดกันมาหาร: 21 ÷ 34 = **0.6176**, 34 ÷ 55 = **0.6182**, 55 ÷ 89 = **0.6180** ยิ่งไปไกลยิ่งเข้าใกล้ **0.618**
> 2. หารด้วยตัวที่อยู่ถัดไปสองตำแหน่ง: 34 ÷ 89 = **0.382** และ 0.618 × 0.618 ≈ 0.382
> 3. **0.786** คือ √0.618 ≈ **0.786** ส่วน **0.5** ไม่ใช่อัตราส่วนฟีโบนัชชีเลย ใส่ไว้เพราะเป็นจุดกึ่งกลาง
> 4. **แล้วไง?** อัตราส่วนเหล่านี้เป็นเลขคณิตง่าย ๆ มันสำคัญในตลาดเพราะ **ทุกคนวาดมัน** คำสั่งและการตัดสินใจจึงไปรวมอยู่ตรงนั้น ให้ถือเป็นไม้บรรทัดร่วม และเชื่อระดับก็ต่อเมื่อมีอย่างอื่น (โครงสร้าง โซน สภาพคล่อง) ยืนยัน

> [!check]- เช็กความเข้าใจ: อัตราส่วน
> **Q1.** มีหลักฐานไหมว่าตลาด "เชื่อฟัง" อัตราส่วนทองคำ?
> > [!answer]-
> > ไม่มีหลักฐานที่ดี ระดับฟีโบได้ผลส่วนหนึ่งเพราะเทรดเดอร์จำนวนมากดูมัน (Self-fulfilling) และส่วนหนึ่งเพราะการย่อหนึ่งในสามถึงสองในสามเป็นเรื่องปกติอยู่แล้ว
""")
L.before_heading("th", "3.", """
![[p6-fib-candles.th.svg]]

> [!analogy]
> เครื่องมือฟีโบนัชชีเหมือน **ขีดบนสายวัด** สายวัดไม่ได้ทำให้แผ่นไม้หยุดที่ 60 ซม. แค่ทำให้ทุกคนพูดถึง "ราวสองในสามของทาง" ด้วยคำเดียวกัน แต่เมื่อช่างไม้นับพันคนตกลงตัดที่ขีดเดียวกัน คุณก็จะเห็นขี้เลื่อยกองอยู่ตรงนั้นเยอะ
>
> **จุดที่เปรียบเทียบไม่ได้:** สายวัดแม่นยำและคงที่ แต่ฟีโบนัชชีขึ้นกับว่าคุณเลือก Swing ไหนเป็นจุดเริ่มและจุดจบ เลือกจุดยึดต่างกัน ทุกระดับก็ย้าย

> [!walkthrough] ไล่ทีละขั้น: ระดับรีเทรซเมนต์ของสวิงจาก 100 ถึง 150
> ขา A = **100** → B = **150** ขายาว **50** จุด แต่ละระดับ = B − อัตราส่วน × 50
> 1. **23.6%:** 150 − 0.236 × 50 = 150 − 11.8 = **138.2**
> 2. **38.2%:** 150 − 19.1 = **130.9**
> 3. **50%:** 150 − 25 = **125.0**
> 4. **61.8%:** 150 − 30.9 = **119.1**
> 5. **78.6%:** 150 − 39.3 = **110.7**
> 6. **แล้วไง?** ในภาพ การย่อหยุดที่ 130.9 (38.2%): ตื้น เป็นสัญญาณของเทรนด์แรง Stop ของ Long จะอยู่ใต้ระดับที่มีความหมายถัดไปและโครงสร้าง (ใต้ 125 หรือ 119) และขนาดไม้มาจากระยะนั้น *(ดู 3.2)*

> [!check]- เช็กความเข้าใจ: รีเทรซเมนต์
> **Q1.** ขาลงวิ่งจาก 80 ถึง 60 รีเทรซเมนต์ 61.8% อยู่ที่ไหน?
> > [!answer]-
> > ขา = 20 รีเทรซเมนต์ย้อน **ขึ้น**: 60 + 0.618 × 20 = 72.36
> **Q2.** ราคาลงทะลุ 100% ของขาขึ้น (ต่ำกว่าจุดเริ่ม) หมายความว่าอะไร?
> > [!answer]-
> > Swing low แตก: เป็น CHoCH สวนเทรนด์ ขานั้นใช้เป็นการย่อในเทรนด์ขาขึ้นไม่ได้แล้ว
""")
L.before_callout("th", "example", """
> [!walkthrough] ไล่ทีละขั้น: ฉายขาถัดไปจาก C = 130.9
> A→B = 50 จุด C (จุดต่ำของการย่อ) = **130.9** เป้า = C + อัตราส่วน × 50
> 1. **1.0 (AB = CD):** 130.9 + 50 = **180.9**
> 2. **1.272:** 130.9 + 63.6 = **194.5**
> 3. **1.618:** 130.9 + 80.9 = **211.8**
> 4. **แล้วไง?** นี่คือเป้าที่ **เป็นไปได้** เลือกตัวที่ใกล้กองสภาพคล่องหรือระดับ HTF ที่สุด (5.1) แล้วปิดกำไรบางส่วนตรงนั้น อย่าถือทั้งหมดไปถึง 1.618 เพียงเพราะ "ควรจะไปถึง"

> [!check]- เช็กความเข้าใจ: เอกซ์เทนชัน
> **Q1.** A = 50, B = 60, C = 56 เป้า 1.618 อยู่ที่เท่าไหร่?
> > [!answer]-
> > A→B = 10  56 + 1.618 × 10 = 72.18
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** ระดับฟีโบบนสวิงรายวันและ 4 ชั่วโมงมีคนดูเยอะ การแตะแม่นระดับ pip หายาก ให้คิดเป็นโซน
> - **ทองคำ:** สวิงใหญ่ (50–150 ดอลลาร์) ทำให้ระยะระหว่างระดับกว้าง ใช้ร่วมกับเลขกลม *(ดู 0.4)*
> - **หุ้นและดัชนี:** วาดจากราคาช่วงซื้อขายปกติ Gap ข้ามคืนอาจกระโดดข้ามระดับไปเลย *(ดู 0.5)*
> - **คริปโต:** ไส้ลึกจากการล้างพอร์ตมักเลยไปถึง 78.6% หรือมากกว่า รอสัญญาณที่ยืนยันด้วยราคาปิด *(ดู 0.7)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** สวิง 200 → 260 บอกรีเทรซเมนต์ 38.2%, 50% และ 61.8%
> > [!answer]-
> > ขา 60  38.2% = 260 − 22.92 = 237.08; 50% = 230; 61.8% = 260 − 37.08 = 222.92
> **Q2.** ทำไมระดับฟีโบเดี่ยว ๆ จึงเป็นเหตุผลเข้าที่อ่อน?
> > [!answer]-
> > มีห้าระดับ ราคาจึงอยู่ใกล้ระดับใดระดับหนึ่งเกือบตลอด ระดับจะมีความหมายก็ต่อเมื่อตรงกับโครงสร้าง โซน FVG หรือสภาพคล่อง และมีสัญญาณ LTF ยืนยัน
""")

L.set_meta("level", "v2")
L.save()
