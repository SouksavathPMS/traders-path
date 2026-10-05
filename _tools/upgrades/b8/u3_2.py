"""B8 · v2 upgrade of 3.2 Position Sizing (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("03 Risk & Money Management/3.2 Position Sizing.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Decide first how much money you're willing to lose if your idea is wrong, say 100 USD. Then look at the chart and decide where the idea is wrong: that's your stop. If the stop is close, you can buy more; if it's far, you buy less. Either way, if the stop is hit you lose the same 100 USD. The size of the trade is simply the answer to a division, never a feeling.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Position size** — how many shares, coins, lots or contracts you buy or sell.
> - **Risk % / 1R** — the share of your account you accept to lose on one trade / that amount in money *(see 3.1)*.
> - **Stop distance per unit** — how much one unit loses if the stop is hit (entry − stop, plus costs).
> - **Pip value** — how much one pip is worth per lot in forex *(see 0.3)*.
> - **Contract multiplier** — how many USD one point is worth on a futures contract (e.g. MES = 5 USD per point).
> - **MES** — Micro E-mini S&P 500 futures *(see 0.2)*.
> - **Lot** — trade size unit in forex (standard lot = 100,000 units) *(see 0.3)*.
> - **Margin / leverage** — the deposit locked for a position / controlling more than you deposit *(see 0.2)*.
> - **Round down** — always cut a fractional size down to the nearest tradable amount.
> - **Gap** — price jumping past your stop with no trades in between *(see 0.5)*.
""")
L.before_heading("en", "2.", """
> [!analogy]
> Position sizing is like **shopping with a fixed budget**. With 100 USD to spend, you can buy 50 cheap items at 2 USD or 20 expensive ones at 5 USD. You never decide "I want 50 items" and then find money somewhere. In trading the "price per item" is your stop distance, and the budget is your 1R.
>
> **Where it breaks:** in a shop, the price is the price. In markets, gaps and slippage can make the "price per item" bigger than planned after you've bought, so you keep a margin for that (section 4).

> [!walkthrough] Step by step: same 1R, two stops
> 1R = **100 USD**.
> 1. **Tight stop** 2 USD per share → 100 ÷ 2 = **50 shares**. If hit: 50 × 2 = **−100 USD**.
> 2. **Wide stop** 5 USD per share → 100 ÷ 5 = **20 shares**. If hit: 20 × 5 = **−100 USD**.
> 3. **So what?** The stop decides the size, not the other way round. You can always put the stop where the chart says.

> [!check]- Check your understanding: the formula
> **Q1.** Account 5,000 USD, risk 1%, stop distance 0.80 per share. How many shares?
> > [!answer]-
> > 1R = 50 USD. 50 ÷ 0.80 = 62.5 → round down to 62 shares.
""")
L.before_heading("en", "4.", """
![[p3-size-markets.en.svg]]

> [!check]- Check your understanding: other markets
> **Q1.** 1R = 60 USD. EUR/USD stop 30 pips, 10 USD per pip per standard lot. What size?
> > [!answer]-
> > Loss per lot = 30 × 10 = 300 USD. 60 ÷ 300 = 0.2 lots.
> **Q2.** 1R = 30 USD. You want to trade one full E-mini S&P (50 USD per point) with a 4-point stop. Can you?
> > [!answer]-
> > No: one contract risks 4 × 50 = 200 USD, more than 1R. Use micro contracts (MES: 4 × 5 = 20 USD each → 1 contract) or skip.
""")
L.before_callout("en", "example", """
> [!walkthrough] Step by step: what a gap does to the example trade
> From the example below: **76 shares**, entry **24.30**, stop **23.55**, 1R = **60 USD**.
> 1. Bad news overnight; the stock **opens at 22.80**, below the stop.
> 2. The stop fills near 22.80: loss per share = 24.30 − 22.80 + 0.03 costs = **1.53**.
> 3. Total loss = 76 × 1.53 ≈ **116 USD** ≈ **1.94R**, almost double the plan.
> 4. **So what?** Over earnings or big news, cut the size so a realistic gap still costs no more than about 2R *(see 10.3)*.

> [!check]- Check your understanding: gaps
> **Q1.** Why can't a stop loss guarantee your maximum loss?
> > [!answer]-
> > A stop is an order that becomes a market order when touched. If price gaps past it, it fills at the next available price, which can be much worse.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** size in lots from pips × pip value; JPY pairs and cross pairs have different pip values *(see 0.3)*.
> - **Gold:** 1 lot is usually 100 oz, so 1 USD of movement = 100 USD per lot; check your broker's contract size *(see 0.4)*.
> - **Stocks:** fractional shares help small accounts; plan for earnings gaps *(see 0.5)*.
> - **Crypto:** size in coins (fractions allowed); very wide stops on volatile coins mean small positions *(see 0.7)*.

> [!caution]
> High leverage lets you open a position far bigger than your formula allows, and nothing on the platform stops you. If you skip the sizing step, one normal move can cost 10–30% of the account *(see 0.2, 0.3)*. Never enter until step 4 of the action checklist is done.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Write the position-size formula and say what each part means.
> > [!answer]-
> > Size = (Account × Risk %) ÷ Stop distance per unit. Account × Risk % is 1R in money; the stop distance is how much one unit loses at the stop (plus costs).
> **Q2.** Why do you always round down?
> > [!answer]-
> > Rounding up quietly increases the risk above 1R; rounding down keeps the loss at or below your limit.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ตัดสินใจก่อนว่ายอมเสียเงินเท่าไหร่ถ้าไอเดียผิด เช่น 100 ดอลลาร์ แล้วดูกราฟเพื่อหาจุดที่ไอเดียผิด: นั่นคือ Stop ถ้า Stop อยู่ใกล้ คุณซื้อได้มากขึ้น ถ้าอยู่ไกล ซื้อน้อยลง ไม่ว่าแบบไหน ถ้าโดน Stop คุณเสีย 100 ดอลลาร์เท่ากัน ขนาดของไม้เป็นแค่คำตอบของการหาร ไม่ใช่ความรู้สึก
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **ขนาดโพซิชัน (Position size)** — จำนวนหุ้น เหรียญ ล็อต หรือสัญญาที่ซื้อหรือขาย
> - **% ความเสี่ยง / 1R** — สัดส่วนของบัญชีที่ยอมเสียในหนึ่งไม้ / จำนวนเงินนั้น *(ดู 3.1)*
> - **ระยะ Stop ต่อหน่วย** — หนึ่งหน่วยขาดทุนเท่าไหร่ถ้าโดน Stop (จุดเข้า − Stop บวกต้นทุน)
> - **มูลค่าต่อ pip (Pip value)** — หนึ่ง pip มีค่าเท่าไหร่ต่อล็อตในฟอเร็กซ์ *(ดู 0.3)*
> - **ตัวคูณสัญญา (Contract multiplier)** — หนึ่งจุดมีค่ากี่ดอลลาร์ในสัญญาฟิวเจอร์ส (เช่น MES = 5 ดอลลาร์ต่อจุด)
> - **MES** — ฟิวเจอร์ส Micro E-mini S&P 500 *(ดู 0.2)*
> - **ล็อต (Lot)** — หน่วยขนาดไม้ในฟอเร็กซ์ (ล็อตมาตรฐาน = 100,000 หน่วย) *(ดู 0.3)*
> - **มาร์จิ้น / เลเวอเรจ** — เงินประกันที่ถูกล็อกสำหรับโพซิชัน / การคุมโพซิชันใหญ่กว่าเงินที่ฝาก *(ดู 0.2)*
> - **ปัดลง (Round down)** — ตัดขนาดที่เป็นเศษลงให้เป็นจำนวนที่ซื้อขายได้ใกล้ที่สุดเสมอ
> - **Gap** — ราคากระโดดข้าม Stop โดยไม่มีการซื้อขายระหว่างทาง *(ดู 0.5)*
""")
L.before_heading("th", "2.", """
> [!analogy]
> การคำนวณขนาดไม้เหมือน **การช็อปปิงด้วยงบที่กำหนด** ถ้ามีงบ 100 ดอลลาร์ คุณซื้อของถูกราคา 2 ดอลลาร์ได้ 50 ชิ้น หรือของแพงราคา 5 ดอลลาร์ได้ 20 ชิ้น คุณไม่เคยตัดสินใจว่า "ฉันอยากได้ 50 ชิ้น" แล้วค่อยไปหาเงิน ในการเทรด "ราคาต่อชิ้น" คือระยะ Stop และงบคือ 1R ของคุณ
>
> **จุดที่เปรียบเทียบไม่ได้:** ในร้าน ราคาก็คือราคา แต่ในตลาด Gap และ Slippage อาจทำให้ "ราคาต่อชิ้น" สูงกว่าที่วางแผนไว้หลังจากซื้อแล้ว คุณจึงต้องเผื่อไว้ (หัวข้อ 4)

> [!walkthrough] ไล่ทีละขั้น: 1R เท่ากัน Stop สองแบบ
> 1R = **100 ดอลลาร์**
> 1. **Stop แคบ** 2 ดอลลาร์ต่อหุ้น → 100 ÷ 2 = **50 หุ้น** ถ้าโดน: 50 × 2 = **−100 ดอลลาร์**
> 2. **Stop กว้าง** 5 ดอลลาร์ต่อหุ้น → 100 ÷ 5 = **20 หุ้น** ถ้าโดน: 20 × 5 = **−100 ดอลลาร์**
> 3. **แล้วไง?** Stop เป็นตัวกำหนดขนาด ไม่ใช่กลับกัน คุณวาง Stop ตรงที่กราฟบอกได้เสมอ

> [!check]- เช็กความเข้าใจ: สูตร
> **Q1.** บัญชี 5,000 ดอลลาร์ เสี่ยง 1% ระยะ Stop 0.80 ต่อหุ้น ได้กี่หุ้น?
> > [!answer]-
> > 1R = 50 ดอลลาร์ 50 ÷ 0.80 = 62.5 → ปัดลงเป็น 62 หุ้น
""")
L.before_heading("th", "4.", """
![[p3-size-markets.th.svg]]

> [!check]- เช็กความเข้าใจ: ตลาดอื่น
> **Q1.** 1R = 60 ดอลลาร์ Stop EUR/USD 30 pip 10 ดอลลาร์ต่อ pip ต่อล็อตมาตรฐาน ขนาดเท่าไหร่?
> > [!answer]-
> > ขาดทุนต่อล็อต = 30 × 10 = 300 ดอลลาร์ 60 ÷ 300 = 0.2 ล็อต
> **Q2.** 1R = 30 ดอลลาร์ คุณอยากเทรด E-mini S&P ขนาดเต็มหนึ่งสัญญา (50 ดอลลาร์ต่อจุด) Stop 4 จุด ทำได้ไหม?
> > [!answer]-
> > ไม่ได้: หนึ่งสัญญาเสี่ยง 4 × 50 = 200 ดอลลาร์ มากกว่า 1R ใช้สัญญาไมโคร (MES: 4 × 5 = 20 ดอลลาร์ต่อสัญญา → 1 สัญญา) หรือข้ามไป
""")
L.before_callout("th", "example", """
> [!walkthrough] ไล่ทีละขั้น: Gap ทำอะไรกับไม้ตัวอย่าง
> จากตัวอย่างด้านล่าง: **76 หุ้น** เข้า **24.30** Stop **23.55** 1R = **60 ดอลลาร์**
> 1. มีข่าวร้ายข้ามคืน หุ้น **เปิดที่ 22.80** ต่ำกว่า Stop
> 2. Stop ได้ราคาราว 22.80: ขาดทุนต่อหุ้น = 24.30 − 22.80 + ต้นทุน 0.03 = **1.53**
> 3. ขาดทุนรวม = 76 × 1.53 ≈ **116 ดอลลาร์** ≈ **1.94R** เกือบสองเท่าของแผน
> 4. **แล้วไง?** ช่วงประกาศงบหรือข่าวใหญ่ ให้ลดขนาดจน Gap ที่สมจริงยังเสียไม่เกินราว 2R *(ดู 10.3)*

> [!check]- เช็กความเข้าใจ: Gap
> **Q1.** ทำไม Stop loss รับประกันขาดทุนสูงสุดไม่ได้?
> > [!answer]-
> > Stop คือคำสั่งที่กลายเป็นคำสั่ง Market เมื่อราคาแตะ ถ้าราคากระโดดข้ามไป จะได้ราคาถัดไปที่มี ซึ่งอาจแย่กว่ามาก
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** คำนวณเป็นล็อตจาก pip × มูลค่า pip คู่เงิน JPY และคู่เงินไขว้มีมูลค่า pip ต่างกัน *(ดู 0.3)*
> - **ทองคำ:** 1 ล็อตมักเป็น 100 ออนซ์ ราคาขยับ 1 ดอลลาร์ = 100 ดอลลาร์ต่อล็อต ตรวจขนาดสัญญาของโบรกเกอร์ *(ดู 0.4)*
> - **หุ้น:** หุ้นแบบเศษส่วนช่วยบัญชีเล็ก วางแผนรับ Gap ช่วงประกาศงบ *(ดู 0.5)*
> - **คริปโต:** คำนวณเป็นจำนวนเหรียญ (เป็นเศษได้) Stop ที่กว้างมากของเหรียญผันผวนหมายถึงโพซิชันเล็ก *(ดู 0.7)*

> [!caution]
> เลเวอเรจสูงทำให้คุณเปิดโพซิชันใหญ่กว่าที่สูตรอนุญาตมาก และไม่มีอะไรบนแพลตฟอร์มห้ามคุณ ถ้าข้ามขั้นตอนคำนวณขนาด การขยับปกติครั้งเดียวอาจทำให้เสีย 10–30% ของบัญชี *(ดู 0.2, 0.3)* ห้ามเข้าจนกว่าจะทำขั้นที่ 4 ของเช็กลิสต์เสร็จ
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** เขียนสูตรขนาดโพซิชันและบอกความหมายของแต่ละส่วน
> > [!answer]-
> > ขนาด = (บัญชี × % ความเสี่ยง) ÷ ระยะ Stop ต่อหน่วย บัญชี × % ความเสี่ยง คือ 1R เป็นเงิน ระยะ Stop คือหนึ่งหน่วยเสียเท่าไหร่เมื่อโดน Stop (บวกต้นทุน)
> **Q2.** ทำไมต้องปัดลงเสมอ?
> > [!answer]-
> > การปัดขึ้นเพิ่มความเสี่ยงเกิน 1R แบบเงียบ ๆ การปัดลงรักษาขาดทุนให้อยู่ที่หรือต่ำกว่าขีดจำกัด
""")

L.set_meta("level", "v2")
L.save()
