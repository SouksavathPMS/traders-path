"""B4 · v2 upgrade of 5.5 Order Blocks & Breakers (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("05 Liquidity & ICT/5.5 Order Blocks & Breakers.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> When a big buyer wants a huge amount, they can't buy it all at once without pushing the price up. So they buy quietly while others are still selling (the last red candle before a big rise). Often price runs away before they've bought everything. When price comes back to that spot later, their remaining buy orders are still waiting there, so price tends to bounce. That spot is an **order block**. If price instead smashes straight through it, everyone who bought there is now losing, and the spot turns into a ceiling: a **breaker**.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **OB (order block)** — the last opposite-colour candle before a displacement that breaks structure: the last down candle before a strong up-move (bullish OB), or the last up candle before a strong down-move (bearish OB).
> - **Displacement / BOS / MSS** — fast one-sided move / break of structure / market structure shift *(see 2.3, 5.2)*.
> - **Mean threshold** — the 50% line of the order block candle.
> - **Mitigation** — price returning to an order block so the waiting orders get filled; once mitigated, the block is "used up".
> - **Breaker (breaker block)** — an order block that price **closed through**; it often flips role (support → resistance).
> - **Trapped traders** — traders holding positions that are now losing; they often exit at break-even when price returns.
> - **Break-even** — the price where a trade has neither profit nor loss.
> - **Role reversal** — old support becoming resistance, or the reverse *(see 2.4)*.
> - **Refine** — redraw a wide zone more precisely on a lower timeframe.
> - **Demand / supply zone** — the base before a strong move *(see 2.5)*.
""")
L.before_heading("en", "2.", """
![[p5-ob-orders.en.svg]]

> [!analogy]
> An order block is like a **sold-out bakery with a waiting list**. Customers who couldn't buy write their names down. When the next batch of bread comes out (price returns), the waiting list buys it all immediately, so the bread doesn't sit on the shelf. Once the list is used up, the next batch has no guaranteed buyers.
>
> **Where it breaks:** a bakery's waiting list is written down. A market's "waiting list" is invisible; you only infer it from the displacement, and some of those buyers may have changed their minds.

> [!walkthrough] Step by step: an order block as unfilled orders (illustrative)
> 4H chart. A fund wants to buy **1,000 contracts** around **101.8–102.4**.
> 1. **The last red candle** (open 102.4, low 101.8): the fund absorbs sellers and fills **600**.
> 2. **Displacement + BOS:** price runs to 106+ before the fund is done. **400** contracts are still wanted, and the fund would like them near its average price.
> 3. **Mean threshold** = (101.8 + 102.4) ÷ 2 = **102.1**.
> 4. **First return:** price drops back to 102.3. The 400 waiting buys meet it: price holds and bounces. The block is now **mitigated** (all 1,000 filled).
> 5. **Second return:** no unfilled orders are left, so there's no reason for a strong bounce. That's why the **first** touch matters most.
> 6. **So what?** An OB works only if a large participant really was there (displacement + BOS prove it) and only while orders remain (fresh). A third or fourth touch is trading an empty waiting list.

> [!check]- Check your understanding: order blocks
> **Q1.** An up-move starts from the last red candle, but it's slow, overlapping and doesn't break any swing high. Is that last red candle an order block?
> > [!answer]-
> > No. Without displacement and a BOS, nothing proves a large participant was there. Every move has a "last opposite candle".
> **Q2.** Why is the first return to an OB stronger than the second?
> > [!answer]-
> > The first return fills the remaining orders (mitigation). After that there are no unfilled orders left waiting there.
""")
L.before_callout("en", "tip", """
> [!walkthrough] Step by step: how a failed OB becomes a breaker
> Bullish OB **101.8–102.4**, mean threshold **102.1**.
> 1. **Buyers defend it:** many traders go long around **102.1**, stops below 101.8.
> 2. **It fails:** a 4H candle **closes at 101.2**, below the OB. Longs from 102.1 are now **0.9** per unit under water; their stops below 101.8 fire as sells.
> 3. **Price bounces back to 102.1:** trapped longs who held on can now get out at **break-even**, so they **sell** there. New sellers who saw the breakdown join them.
> 4. **Result:** the old support at 101.8–102.4 now acts as **resistance**: a bearish breaker.
> 5. **So what?** A failed OB isn't just "wrong"; it's new information. Re-label it and watch it from the other side.

> [!check]- Check your understanding: breakers
> **Q1.** A bearish OB at 55.0–55.6 is closed through to the upside at 56.4. When price returns to 55.6, what is it likely to act as, and why?
> > [!answer]-
> > Support (a bullish breaker). Shorts who sold at the OB are trapped; when price returns they buy back at break-even, and new buyers join.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** OBs on 1H–4H during London/New York are the most used; refine them on 15m.
> - **Gold:** 4H OBs can be 10–20 USD wide; refine on a lower timeframe or reduce size *(see 0.4)*.
> - **Stocks:** daily OBs often line up with earnings-gap bases; an overnight gap can jump straight through an OB *(see 0.5)*.
> - **Crypto:** liquidation wicks create many false "last candles"; insist on displacement **and** a close-based BOS *(see 0.7)*.

> [!caution]
> Order blocks look obvious after the move and much less obvious before it. Hindsight makes every chart full of "perfect" OBs. Mark your OB and plan the trade **before** price returns, and expect some A-grade OBs to fail. Your stop below the OB is what limits the damage.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Give the four conditions that make a "last opposite candle" a real order block.
> > [!answer]-
> > Displacement away from it, a break of structure (BOS/MSS), ideally an FVG left behind, and a location in discount (bullish) or premium (bearish). Fresh and in the HTF direction are bonuses.
> **Q2.** What turns a bullish OB into a bearish breaker?
> > [!answer]-
> > A candle **closing** below the OB. Traders who bought there are trapped and sell at break-even when price returns, so the old support becomes resistance.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> เมื่อผู้ซื้อรายใหญ่ต้องการซื้อจำนวนมหาศาล เขาซื้อทีเดียวไม่ได้โดยไม่ดันราคาขึ้น จึงค่อย ๆ ซื้อเงียบ ๆ ขณะที่คนอื่นยังขายอยู่ (แท่งแดงแท่งสุดท้ายก่อนการขึ้นแรง) บ่อยครั้งราคาวิ่งหนีไปก่อนที่เขาจะซื้อครบ เมื่อราคากลับมาที่จุดนั้นทีหลัง คำสั่งซื้อที่เหลือยังรออยู่ ราคาจึงมักเด้ง จุดนั้นคือ **Order block** ถ้าราคากลับทุบทะลุลงไป ทุกคนที่ซื้อตรงนั้นจะขาดทุน และจุดนั้นกลายเป็นเพดาน: **Breaker**
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **OB (Order block)** — แท่งเทียนสีตรงข้ามแท่งสุดท้ายก่อนแรงส่งที่ทะลุโครงสร้าง: แท่งลงแท่งสุดท้ายก่อนการขึ้นแรง (OB ขาขึ้น) หรือแท่งขึ้นแท่งสุดท้ายก่อนการลงแรง (OB ขาลง)
> - **แรงส่ง / BOS / MSS** — การวิ่งเร็วไปทางเดียว / การทะลุโครงสร้าง / การเปลี่ยนโครงสร้างตลาด *(ดู 2.3, 5.2)*
> - **Mean threshold** — เส้น 50% ของแท่ง Order block
> - **Mitigation (การถูกใช้)** — ราคากลับมาที่ Order block จนคำสั่งที่รออยู่ได้เติม เมื่อถูกใช้แล้ว บล็อกนั้นถือว่า "หมดแรง"
> - **Breaker (Breaker block)** — Order block ที่ราคา **ปิดทะลุ** ไปแล้ว มักสลับบทบาท (แนวรับ → แนวต้าน)
> - **เทรดเดอร์ที่ติดกับ (Trapped traders)** — คนที่ถือโพซิชันที่ตอนนี้ขาดทุน มักออกที่จุดคุ้มทุนเมื่อราคากลับมา
> - **จุดคุ้มทุน (Break-even)** — ราคาที่ไม้นั้นไม่กำไรไม่ขาดทุน
> - **การสลับบทบาท (Role reversal)** — แนวรับเก่ากลายเป็นแนวต้าน หรือกลับกัน *(ดู 2.4)*
> - **Refine** — วาดโซนที่กว้างใหม่ให้แม่นขึ้นบนไทม์เฟรมต่ำ
> - **โซน Demand / Supply** — ฐานก่อนการวิ่งแรง *(ดู 2.5)*
""")
L.before_heading("th", "2.", """
![[p5-ob-orders.th.svg]]

> [!analogy]
> Order block เหมือน **ร้านขนมปังที่ขายหมดและมีรายชื่อรอคิว** ลูกค้าที่ซื้อไม่ทันเขียนชื่อไว้ เมื่อขนมปังชุดใหม่ออกจากเตา (ราคากลับมา) คนในรายชื่อก็ซื้อหมดทันที ขนมปังจึงไม่ค้างบนชั้น เมื่อรายชื่อหมดแล้ว ชุดถัดไปก็ไม่มีผู้ซื้อรับประกัน
>
> **จุดที่เปรียบเทียบไม่ได้:** รายชื่อรอคิวของร้านเขียนไว้ชัด แต่ "รายชื่อรอคิว" ของตลาดมองไม่เห็น คุณอนุมานได้จากแรงส่งเท่านั้น และผู้ซื้อบางรายอาจเปลี่ยนใจไปแล้ว

> [!walkthrough] ไล่ทีละขั้น: Order block คือคำสั่งที่ยังไม่ได้เติม (ภาพประกอบ)
> กราฟ 4 ชั่วโมง กองทุนต้องการซื้อ **1,000 สัญญา** แถว **101.8–102.4**
> 1. **แท่งแดงแท่งสุดท้าย** (เปิด 102.4 ต่ำสุด 101.8): กองทุนรับแรงขายและเติมได้ **600**
> 2. **แรงส่ง + BOS:** ราคาวิ่งไป 106+ ก่อนกองทุนซื้อเสร็จ ยังต้องการอีก **400** สัญญา และอยากได้ใกล้ราคาเฉลี่ยของตัวเอง
> 3. **Mean threshold** = (101.8 + 102.4) ÷ 2 = **102.1**
> 4. **กลับมาครั้งแรก:** ราคาลงมาที่ 102.3 คำสั่งซื้อ 400 ที่รออยู่เจอราคา: ราคายืนได้และเด้ง บล็อกนี้ถูก **ใช้แล้ว (Mitigated)** (เติมครบ 1,000)
> 5. **กลับมาครั้งที่สอง:** ไม่มีคำสั่งค้างเหลือ จึงไม่มีเหตุผลให้เด้งแรง นี่คือเหตุผลที่การแตะ **ครั้งแรก** สำคัญที่สุด
> 6. **แล้วไง?** OB ได้ผลก็ต่อเมื่อมีผู้เล่นรายใหญ่อยู่ตรงนั้นจริง (แรงส่ง + BOS เป็นหลักฐาน) และเฉพาะตอนที่คำสั่งยังเหลืออยู่ (ยังสด) การแตะครั้งที่สามหรือสี่คือการเทรดกับรายชื่อรอคิวที่ว่างเปล่า

> [!check]- เช็กความเข้าใจ: Order block
> **Q1.** การขึ้นเริ่มจากแท่งแดงแท่งสุดท้าย แต่ช้า แท่งซ้อนกัน และไม่ทะลุ Swing high ใดเลย แท่งแดงแท่งสุดท้ายนั้นเป็น Order block ไหม?
> > [!answer]-
> > ไม่ใช่ ถ้าไม่มีแรงส่งและ BOS ก็ไม่มีอะไรพิสูจน์ว่ามีผู้เล่นรายใหญ่อยู่ ทุกการวิ่งมี "แท่งสีตรงข้ามแท่งสุดท้าย" เสมอ
> **Q2.** ทำไมการกลับมาที่ OB ครั้งแรกจึงแรงกว่าครั้งที่สอง?
> > [!answer]-
> > การกลับมาครั้งแรกเติมคำสั่งที่เหลือ (Mitigation) หลังจากนั้นไม่มีคำสั่งค้างรออยู่ตรงนั้นอีก
""")
L.before_callout("th", "tip", """
> [!walkthrough] ไล่ทีละขั้น: OB ที่ล้มเหลวกลายเป็น Breaker ได้อย่างไร
> OB ขาขึ้น **101.8–102.4** Mean threshold **102.1**
> 1. **ผู้ซื้อป้องกันไว้:** เทรดเดอร์จำนวนมากเปิด Long แถว **102.1** Stop ใต้ 101.8
> 2. **ล้มเหลว:** แท่ง 4 ชั่วโมง **ปิดที่ 101.2** ใต้ OB  Long จาก 102.1 ขาดทุน **0.9** ต่อหน่วย Stop ใต้ 101.8 ทำงานเป็นคำสั่งขาย
> 3. **ราคาเด้งกลับมา 102.1:** Long ที่ติดกับและยังถืออยู่ออกได้ที่ **จุดคุ้มทุน** จึง **ขาย** ตรงนั้น ผู้ขายใหม่ที่เห็นการหลุดก็ร่วมขายด้วย
> 4. **ผลลัพธ์:** แนวรับเก่าที่ 101.8–102.4 ทำหน้าที่เป็น **แนวต้าน**: Breaker ขาลง
> 5. **แล้วไง?** OB ที่ล้มเหลวไม่ได้แค่ "ผิด" แต่เป็นข้อมูลใหม่ ติดป้ายใหม่และดูมันจากอีกฝั่ง

> [!check]- เช็กความเข้าใจ: Breaker
> **Q1.** OB ขาลงที่ 55.0–55.6 ถูกปิดทะลุขึ้นไปที่ 56.4 เมื่อราคากลับมาที่ 55.6 มันน่าจะทำหน้าที่อะไร และเพราะอะไร?
> > [!answer]-
> > แนวรับ (Breaker ขาขึ้น) คนที่ Short ที่ OB ติดกับ เมื่อราคากลับมาเขาซื้อคืนที่จุดคุ้มทุน และผู้ซื้อใหม่ร่วมด้วย
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** OB บน 1H–4H ช่วงลอนดอน/นิวยอร์กใช้กันมากที่สุด Refine บน 15 นาที
> - **ทองคำ:** OB 4 ชั่วโมงอาจกว้าง 10–20 ดอลลาร์ Refine บนไทม์เฟรมต่ำ หรือลดขนาด *(ดู 0.4)*
> - **หุ้น:** OB รายวันมักตรงกับฐานของ Gap จากงบ Gap ข้ามคืนอาจกระโดดทะลุ OB ไปเลย *(ดู 0.5)*
> - **คริปโต:** ไส้จากการล้างพอร์ตสร้าง "แท่งสุดท้าย" ปลอมจำนวนมาก ต้องมีทั้งแรงส่ง **และ** BOS ที่ยืนยันด้วยราคาปิด *(ดู 0.7)*

> [!caution]
> Order block ดูชัดเจนหลังการวิ่ง แต่ไม่ชัดเท่าไหร่ก่อนการวิ่ง การมองย้อนหลังทำให้ทุกกราฟเต็มไปด้วย OB ที่ "สมบูรณ์แบบ" ทำเครื่องหมาย OB และวางแผนเทรด **ก่อน** ราคากลับมา และเตรียมใจว่า OB เกรด A บางอันจะล้มเหลว Stop ใต้ OB คือสิ่งที่จำกัดความเสียหาย
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกสี่เงื่อนไขที่ทำให้ "แท่งสีตรงข้ามแท่งสุดท้าย" เป็น Order block จริง
> > [!answer]-
> > มีแรงส่งออกจากแท่งนั้น ทะลุโครงสร้าง (BOS/MSS) ควรทิ้ง FVG ไว้ และอยู่ใน Discount (ขาขึ้น) หรือ Premium (ขาลง) ยังสดและตามทิศทาง HTF เป็นโบนัส
> **Q2.** อะไรเปลี่ยน OB ขาขึ้นให้กลายเป็น Breaker ขาลง?
> > [!answer]-
> > แท่งเทียนที่ **ปิด** ใต้ OB คนที่ซื้อตรงนั้นติดกับ และขายที่จุดคุ้มทุนเมื่อราคากลับมา แนวรับเก่าจึงกลายเป็นแนวต้าน
""")

L.set_meta("level", "v2")
L.save()
