"""B8 · v2 upgrade of 2.5 Supply & Demand Zones (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("02 Market Structure/2.5 Supply & Demand Zones.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> When a big buyer wants to buy a huge amount, price first goes quiet for a moment while they buy (a small pause on the chart), then shoots up once the sellers run out. Often the big buyer didn't get everything they wanted. If price later comes back to that quiet spot, their remaining orders may still be waiting there and push price up again. That spot is a **demand zone**. A **supply zone** is the same thing for a big seller.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Demand / supply zone** — a price area where big buyers / sellers likely left unfilled orders.
> - **Base** — the 1–3 small candles where price paused before the strong move.
> - **Leg-in / leg-out** — the move into the base / the strong move out of it.
> - **RBR, DBR, RBD, DBD** — rally-base-rally, drop-base-rally, rally-base-drop, drop-base-drop (the four zone patterns).
> - **Proximal / distal line** — the zone edge nearest to current price (entry) / the far edge (stop goes beyond it).
> - **Fresh** — not yet revisited since it formed.
> - **Departure** — how fast and strongly price left the base.
> - **BOS** — break of structure *(see 2.3)*.
> - **Confluence** — several reasons agreeing at one price.
> - **Confirmation entry** — waiting for an LTF CHoCH inside the zone before entering *(see 2.6)*.
> - **R / R:R** — risk unit and reward-to-risk *(see 3.3)*.
""")
L.before_heading("en", "3.", """
> [!analogy]
> A demand zone is like a **shop that sold out in minutes**. The crowd that arrived late left their names on a waiting list. When new stock arrives (price returns to the zone), the waiting list buys it immediately. The faster the shop sold out, the longer the list.
>
> **Where it breaks:** a waiting list is written down and certain. Unfilled orders are invisible and may have been cancelled, and the second time new stock arrives, the list is already used up (a zone gets weaker with each return).

> [!walkthrough] Step by step: why some orders are left over (illustrative)
> 1. A fund wants to buy **2,000,000** shares near 105.
> 2. While price sits in the base, it fills **1,200,000** shares by absorbing sellers.
> 3. The sellers run out; price jumps 10% in two days. **800,000** shares are still wanted.
> 4. The fund won't chase 10% higher. It leaves orders back near **105**, its average price.
> 5. **So what?** When price returns to the base for the first time, those 800,000 shares of buying meet it. That's the logic behind "fresh" zones and "fast departure".

> [!check]- Check your understanding: why zones exist
> **Q1.** Why is the first return to a zone usually stronger than the third?
> > [!answer]-
> > The first return fills the leftover orders. After that, fewer unfilled orders remain at that price.
""")
L.before_heading("en", "5.", """
![[p2-zone-grade.en.svg]]

> [!walkthrough] Step by step: the trade numbers from the example
> Zone: proximal **105.8**, distal **104.4**. Stop just beyond distal: **103.6**.
> 1. **Risk** = 105.8 − 103.6 = **2.2** per share.
> 2. **First target** (leg-out high 117.6): reward 117.6 − 105.8 = **11.8** → 11.8 ÷ 2.2 ≈ **5.4R**.
> 3. **Full target** (prior high 121): reward 15.2 → 15.2 ÷ 2.2 ≈ **6.9R**.
> 4. **Size** with 1R = 100 USD: 100 ÷ 2.2 = 45.5 → **45 shares** *(see 3.2)*.
> 5. **So what?** The zone gives you a tight, logical stop and a far target: that's where large R comes from. Grade it first (figure): this one scores 5/6 because it's against the HTF trend, so wait for an LTF confirmation.

> [!check]- Check your understanding: drawing and grading
> **Q1.** A demand zone's base spans bodies up to 50.4 and wicks down to 49.6. Where are the proximal and distal lines?
> > [!answer]-
> > Proximal 50.4 (top of the base bodies); distal 49.6 (lowest wick). The stop goes a little below 49.6.
""")
L.before_callout("en", "action", """
> [!check]- Check your understanding: entries
> **Q1.** You're a beginner and the zone is against the HTF trend. Limit order or confirmation entry?
> > [!answer]-
> > Confirmation: wait for an LTF CHoCH inside the zone. You'll miss some trades but avoid many zones that fail.

> [!market]
> - **Forex:** zones on 4H–daily work best around the London and New York sessions *(see 5.6)*.
> - **Gold:** zones are wide in dollars; refine on a lower timeframe or reduce size *(see 0.4)*.
> - **Stocks:** daily zones often form at earnings-gap bases; an overnight gap can jump straight through a zone *(see 0.5)*.
> - **Crypto:** liquidation wicks pierce zones often; use bodies for the proximal line and expect deeper tests *(see 0.7)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** What three parts does every zone have, and which part do you draw?
> > [!answer]-
> > Leg-in, base, leg-out. You draw the base: proximal at the body edge nearest price, distal at the far wick.
> **Q2.** Which three grading factors make you skip a zone if they fail?
> > [!answer]-
> > Departure (no explosive move away), freshness (3rd+ return), and trend (against the HTF without strong compensation).
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> เมื่อผู้ซื้อรายใหญ่ต้องการซื้อจำนวนมหาศาล ราคาจะเงียบไปพักหนึ่งขณะที่เขาซื้อ (จุดพักเล็ก ๆ บนกราฟ) แล้วพุ่งขึ้นเมื่อผู้ขายหมด บ่อยครั้งผู้ซื้อรายใหญ่ยังซื้อไม่ครบ ถ้าราคากลับมาที่จุดเงียบนั้นทีหลัง คำสั่งที่เหลืออาจยังรออยู่และดันราคาขึ้นอีก จุดนั้นคือ **โซน Demand** ส่วน **โซน Supply** คือสิ่งเดียวกันสำหรับผู้ขายรายใหญ่
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **โซน Demand / Supply** — บริเวณราคาที่ผู้ซื้อ / ผู้ขายรายใหญ่น่าจะทิ้งคำสั่งที่ยังไม่ได้เติมไว้
> - **ฐาน (Base)** — แท่งเทียนเล็ก 1–3 แท่งที่ราคาหยุดพักก่อนวิ่งแรง
> - **ขาเข้า / ขาออก (Leg-in / Leg-out)** — การวิ่งเข้าสู่ฐาน / การวิ่งแรงออกจากฐาน
> - **RBR, DBR, RBD, DBD** — Rally-base-rally, Drop-base-rally, Rally-base-drop, Drop-base-drop (รูปแบบโซนสี่แบบ)
> - **เส้น Proximal / Distal** — ขอบโซนที่ใกล้ราคาปัจจุบัน (จุดเข้า) / ขอบไกล (Stop อยู่เลยออกไป)
> - **ยังสด (Fresh)** — ยังไม่เคยถูกกลับมาทดสอบตั้งแต่เกิด
> - **การออกจากฐาน (Departure)** — ราคาออกจากฐานเร็วและแรงแค่ไหน
> - **BOS** — การทะลุโครงสร้าง *(ดู 2.3)*
> - **Confluence (จุดบรรจบ)** — หลายเหตุผลที่ตรงกันที่ราคาเดียว
> - **การเข้าแบบรอยืนยัน (Confirmation entry)** — รอ CHoCH บน LTF ภายในโซนก่อนเข้า *(ดู 2.6)*
> - **R / R:R** — หน่วยความเสี่ยงและผลตอบแทนต่อความเสี่ยง *(ดู 3.3)*
""")
L.before_heading("th", "3.", """
> [!analogy]
> โซน Demand เหมือน **ร้านที่ของหมดในไม่กี่นาที** คนที่มาช้าทิ้งชื่อไว้ในรายชื่อรอคิว เมื่อของล็อตใหม่มาถึง (ราคากลับมาที่โซน) คนในรายชื่อก็ซื้อทันที ยิ่งร้านขายหมดเร็ว รายชื่อรอคิวก็ยิ่งยาว
>
> **จุดที่เปรียบเทียบไม่ได้:** รายชื่อรอคิวเขียนไว้ชัดและแน่นอน แต่คำสั่งที่ยังไม่ได้เติมมองไม่เห็น และอาจถูกยกเลิกไปแล้ว และครั้งที่สองที่ของมาถึง รายชื่อก็ถูกใช้ไปแล้ว (โซนอ่อนลงทุกครั้งที่ถูกกลับมา)

> [!walkthrough] ไล่ทีละขั้น: ทำไมคำสั่งบางส่วนจึงเหลือค้าง (ภาพประกอบ)
> 1. กองทุนต้องการซื้อ **2,000,000** หุ้นแถว 105
> 2. ขณะที่ราคาอยู่ในฐาน กองทุนเติมได้ **1,200,000** หุ้นโดยรับแรงขาย
> 3. ผู้ขายหมด ราคากระโดด 10% ในสองวัน ยังต้องการอีก **800,000** หุ้น
> 4. กองทุนไม่ไล่ซื้อที่สูงขึ้น 10% แต่ทิ้งคำสั่งไว้แถว **105** ซึ่งเป็นราคาเฉลี่ยของตัวเอง
> 5. **แล้วไง?** เมื่อราคากลับมาที่ฐานครั้งแรก แรงซื้อ 800,000 หุ้นนั้นจะเจอราคา นี่คือตรรกะเบื้องหลังโซนที่ "ยังสด" และ "ออกจากฐานเร็ว"

> [!check]- เช็กความเข้าใจ: ทำไมโซนจึงมีอยู่
> **Q1.** ทำไมการกลับมาที่โซนครั้งแรกมักแรงกว่าครั้งที่สาม?
> > [!answer]-
> > การกลับมาครั้งแรกเติมคำสั่งที่เหลือค้าง หลังจากนั้นคำสั่งที่ยังไม่ได้เติมที่ราคานั้นก็เหลือน้อยลง
""")
L.before_heading("th", "5.", """
![[p2-zone-grade.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ตัวเลขเทรดจากตัวอย่าง
> โซน: Proximal **105.8** Distal **104.4** Stop เลย Distal นิดเดียว: **103.6**
> 1. **ความเสี่ยง** = 105.8 − 103.6 = **2.2** ต่อหุ้น
> 2. **เป้าแรก** (จุดสูงของขาออก 117.6): ผลตอบแทน 117.6 − 105.8 = **11.8** → 11.8 ÷ 2.2 ≈ **5.4R**
> 3. **เป้าเต็ม** (จุดสูงก่อนหน้า 121): ผลตอบแทน 15.2 → 15.2 ÷ 2.2 ≈ **6.9R**
> 4. **ขนาด** เมื่อ 1R = 100 ดอลลาร์: 100 ÷ 2.2 = 45.5 → **45 หุ้น** *(ดู 3.2)*
> 5. **แล้วไง?** โซนให้ Stop ที่แคบและมีเหตุผล กับเป้าที่ไกล: นั่นคือที่มาของ R ก้อนใหญ่ ให้คะแนนก่อน (ภาพ): โซนนี้ได้ 5/6 เพราะสวนเทรนด์ HTF จึงต้องรอการยืนยันบน LTF

> [!check]- เช็กความเข้าใจ: การขีดและให้คะแนน
> **Q1.** ฐานของโซน Demand มีตัวแท่งสูงสุดที่ 50.4 และไส้ต่ำสุดที่ 49.6 เส้น Proximal และ Distal อยู่ที่ไหน?
> > [!answer]-
> > Proximal 50.4 (ยอดของตัวแท่งในฐาน) Distal 49.6 (ไส้ต่ำสุด) Stop อยู่ใต้ 49.6 นิดหน่อย
""")
L.before_callout("th", "action", """
> [!check]- เช็กความเข้าใจ: วิธีเข้า
> **Q1.** คุณเป็นมือใหม่และโซนสวนเทรนด์ HTF ใช้ Limit order หรือการเข้าแบบรอยืนยัน?
> > [!answer]-
> > รอยืนยัน: รอ CHoCH บน LTF ภายในโซน คุณจะพลาดบางไม้ แต่หลบโซนที่ล้มเหลวได้มาก

> [!market]
> - **ฟอเร็กซ์:** โซนบน 4 ชั่วโมงถึงรายวันได้ผลดีที่สุดรอบเซสชันลอนดอนและนิวยอร์ก *(ดู 5.6)*
> - **ทองคำ:** โซนกว้างเป็นดอลลาร์ Refine บนไทม์เฟรมต่ำ หรือลดขนาด *(ดู 0.4)*
> - **หุ้น:** โซนรายวันมักเกิดที่ฐานของ Gap จากงบ Gap ข้ามคืนอาจกระโดดทะลุโซนไปเลย *(ดู 0.5)*
> - **คริปโต:** ไส้จากการล้างพอร์ตทะลุโซนบ่อย ใช้ตัวแท่งสำหรับเส้น Proximal และเตรียมรับการทดสอบที่ลึกกว่า *(ดู 0.7)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** ทุกโซนมีสามส่วนอะไรบ้าง และคุณขีดส่วนไหน?
> > [!answer]-
> > ขาเข้า ฐาน ขาออก คุณขีดที่ฐาน: Proximal ที่ขอบตัวแท่งที่ใกล้ราคา Distal ที่ไส้ด้านไกล
> **Q2.** ปัจจัยให้คะแนนสามข้อไหนที่ถ้าไม่ผ่านจะทำให้คุณข้ามโซน?
> > [!answer]-
> > การออกจากฐาน (ไม่มีการวิ่งออกแบบระเบิด) ความสด (กลับมาครั้งที่ 3 ขึ้นไป) และเทรนด์ (สวน HTF โดยไม่มีอะไรชดเชยที่แข็งแรง)
""")

L.set_meta("level", "v2")
L.save()
