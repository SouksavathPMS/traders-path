"""B4 · v2 upgrade of 5.4 Fair Value Gaps (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("05 Liquidity & ICT/5.4 Fair Value Gaps (FVG).md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Sometimes buyers are in such a hurry that price jumps up in one big candle, skipping over prices where almost nobody traded. That skipped area is a **fair value gap**. Later, price often comes back to that area, because traders who missed the jump left orders there and want to get in at the price they missed. If the gap holds when price returns, the move often continues; if price closes right through it, the idea is finished.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **FVG (fair value gap)** — a 3-candle price area where the middle candle moved so fast that candle 1 and candle 3 don't overlap.
> - **Imbalance / inefficiency** — a price area where one side (buyers or sellers) dominated and the other barely traded.
> - **Displacement** — a fast, one-sided move with big bodies *(see 5.2)*.
> - **Candle 1 / 2 / 3** — the three candles of the pattern; candle 2 is the big one in the middle.
> - **CE (consequent encroachment)** — the 50% line of the gap.
> - **BISI (buy-side imbalance, sell-side inefficiency)** — ICT's name for a **bullish** FVG: buyers rushed, sellers were barely filled.
> - **SIBI (sell-side imbalance, buy-side inefficiency)** — ICT's name for a **bearish** FVG: sellers rushed, buyers were barely filled.
> - **Inverse FVG** — an FVG that price closed through; it often flips role (support becomes resistance).
> - **Internal liquidity** — liquidity inside the current range, such as FVGs *(see 5.1)*.
> - **First return / fresh** — the first time price comes back to the gap since it formed.
> - **BOS / MSS** — break of structure / market structure shift *(see 2.3, 5.2)*.
""")
L.before_heading("en", "2.", """
![[p5-fvg-numbers.en.svg]]

> [!walkthrough] Step by step: finding a bullish FVG with real numbers
> Three consecutive candles:
> 1. **Candle 1:** high **100.20** (low 99.95).
> 2. **Candle 2:** a big green displacement candle from 100.10 to 100.85.
> 3. **Candle 3:** low **100.60**.
> 4. **Test:** is candle 3's low above candle 1's high? 100.60 > 100.20 → **yes, a bullish FVG (a BISI)**.
> 5. **Size** = 100.60 − 100.20 = **0.40**. **CE** = (100.20 + 100.60) ÷ 2 = **100.40**.
> 6. **Invalid if** a later candle **closes** below **100.20** (the far side of the gap). A wick below that closes back inside is still alive.
> 7. **So what?** Two numbers (candle 1's high and candle 3's low) define the whole zone, its midpoint and its invalidation. If you can't find them, there is no FVG.

> [!check]- Check your understanding: finding an FVG
> **Q1.** Candle 1 low **50.00**, candle 3 high **49.70**, with a big red candle in between. What is it, how big, and where is the CE?
> > [!answer]-
> > A bearish FVG (a SIBI): 50.00 − 49.70 = 0.30; CE = 49.85. It's invalid if a candle closes above 50.00.
> **Q2.** Candle 1 high 100.20, candle 3 low 100.15. Is there an FVG?
> > [!answer]-
> > No. Candle 3's low is below candle 1's high, so the candles overlap: no gap.
""")
L.before_heading("en", "3.", """
> [!analogy]
> An FVG is like a **bus that skipped several stops** because it was running late. The passengers waiting at those stops didn't get on. When the bus comes back along the route, those passengers are still waiting and finally board. That's the "fill" on the return.
>
> **Where it breaks:** a real bus always comes back along its route. A market doesn't have to: in a strong trend some gaps are never revisited, and some passengers give up and leave (orders get cancelled).

> [!check]- Check your understanding: why gaps get revisited
> **Q1.** Why are FVGs counted as internal liquidity?
> > [!answer]-
> > They sit inside the current range, and they hold unfilled orders from traders who missed the fast move. Price is often drawn back into them before going on to the next external pool.
""")
L.before_callout("en", "action", """
> [!walkthrough] Step by step: trading the return with a fixed risk
> Bullish FVG **100.20–100.60** (CE **100.40**), created by displacement that broke structure, in discount. Account **10,000 USD**, risk **1% = 100 USD**.
> 1. **Entry:** limit buy at the CE **100.40**.
> 2. **Stop:** below candle 1's low and the gap: **99.90** → risk per unit = 100.40 − 99.90 = **0.50**.
> 3. **Size:** 100 ÷ 0.50 = **200 units**.
> 4. **Target:** the next BSL at **101.90** → reward per unit **1.50** → **3R** (= 300 USD if it works, −100 USD if not).
> 5. **So what?** The FVG gives you all three numbers (entry, stop, invalidation) before price arrives. Decide them in advance; on the return you only execute.

> [!check]- Check your understanding: trading the return
> **Q1.** Same trade, but you choose the more aggressive entry at the top of the gap (100.60). What's the new risk per unit and size?
> > [!answer]-
> > Risk = 100.60 − 99.90 = 0.70 → size = 100 ÷ 0.70 = 142.9 → 142 units. Better fill chance, smaller size.

> [!market]
> - **Forex:** FVGs form constantly on low timeframes; use only those from displacement during London/New York *(see 5.6)*.
> - **Gold:** large FVGs after US data at 19:30 UTC+7 (summer); they're often revisited, but wide, so size down *(see 0.4)*.
> - **Stocks:** an overnight **gap** between sessions is not the same as an intraday FVG, though traders treat big opening gaps in a similar way; FVGs inside the regular session behave as in this lesson *(see 0.5)*.
> - **Crypto:** trades 24/7, so there are no session gaps, only intraday FVGs; very fast liquidation moves leave big FVGs that are often revisited *(see 0.7)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Define a bullish FVG in one sentence, using the three candles.
> > [!answer]-
> > Three candles where the middle one is a big up candle and candle 3's low is above candle 1's high; the gap between them is the FVG.
> **Q2.** What exactly makes an FVG invalid?
> > [!answer]-
> > A candle **closing** through the far side of the gap (below candle 1's high for a bullish FVG). A wick through that closes back inside does not invalidate it.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> บางครั้งผู้ซื้อรีบมากจนราคากระโดดขึ้นในแท่งเทียนใหญ่แท่งเดียว ข้ามราคาที่แทบไม่มีใครซื้อขายไปเลย บริเวณที่ถูกข้ามนั้นคือ **Fair value gap** ต่อมาราคามักกลับมาที่บริเวณนั้น เพราะเทรดเดอร์ที่ตกรถทิ้งคำสั่งไว้และอยากเข้าที่ราคาที่พลาดไป ถ้าช่องว่างยืนได้ตอนราคากลับมา การวิ่งมักไปต่อ ถ้าราคาปิดทะลุผ่านไป ไอเดียก็จบ
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **FVG (Fair value gap)** — บริเวณราคาจากแท่งเทียน 3 แท่ง ที่แท่งกลางวิ่งเร็วมากจนแท่ง 1 และแท่ง 3 ไม่ซ้อนกัน
> - **ความไม่สมดุล (Imbalance / Inefficiency)** — บริเวณราคาที่ฝั่งหนึ่ง (ผู้ซื้อหรือผู้ขาย) ครอบงำ และอีกฝั่งแทบไม่ได้ซื้อขาย
> - **แรงส่ง (Displacement)** — การวิ่งเร็วไปทางเดียว แท่งตัวใหญ่ *(ดู 5.2)*
> - **แท่ง 1 / 2 / 3** — แท่งเทียนสามแท่งของรูปแบบ แท่ง 2 คือแท่งใหญ่ตรงกลาง
> - **CE (Consequent encroachment)** — เส้น 50% ของช่องว่าง
> - **BISI (Buy-side imbalance, sell-side inefficiency)** — ชื่อที่ ICT ใช้เรียก FVG **ขาขึ้น**: ผู้ซื้อรีบ ผู้ขายแทบไม่ได้ขาย
> - **SIBI (Sell-side imbalance, buy-side inefficiency)** — ชื่อที่ ICT ใช้เรียก FVG **ขาลง**: ผู้ขายรีบ ผู้ซื้อแทบไม่ได้ซื้อ
> - **Inverse FVG** — FVG ที่ราคาปิดทะลุผ่านไปแล้ว มักสลับบทบาท (แนวรับกลายเป็นแนวต้าน)
> - **สภาพคล่องภายใน (Internal liquidity)** — สภาพคล่องภายในกรอบปัจจุบัน เช่น FVG *(ดู 5.1)*
> - **กลับมาครั้งแรก / ยังสด (First return / Fresh)** — ครั้งแรกที่ราคากลับมาที่ช่องว่างนับตั้งแต่เกิดขึ้น
> - **BOS / MSS** — การทะลุโครงสร้าง / การเปลี่ยนโครงสร้างตลาด *(ดู 2.3, 5.2)*
""")
L.before_heading("th", "2.", """
![[p5-fvg-numbers.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: หา FVG ขาขึ้นด้วยตัวเลขจริง
> แท่งเทียนสามแท่งติดกัน:
> 1. **แท่ง 1:** High **100.20** (Low 99.95)
> 2. **แท่ง 2:** แท่งเขียวใหญ่ที่เป็นแรงส่ง จาก 100.10 ถึง 100.85
> 3. **แท่ง 3:** Low **100.60**
> 4. **ทดสอบ:** Low ของแท่ง 3 อยู่เหนือ High ของแท่ง 1 ไหม? 100.60 > 100.20 → **ใช่ เป็น FVG ขาขึ้น (BISI)**
> 5. **ขนาด** = 100.60 − 100.20 = **0.40**  **CE** = (100.20 + 100.60) ÷ 2 = **100.40**
> 6. **ใช้ไม่ได้ถ้า** มีแท่งเทียนต่อมา **ปิด** ใต้ **100.20** (ขอบไกลของช่องว่าง) ไส้ที่ทะลุลงไปแต่ปิดกลับเข้ามายังถือว่ายังใช้ได้
> 7. **แล้วไง?** ตัวเลขสองตัว (High แท่ง 1 และ Low แท่ง 3) กำหนดทั้งโซน จุดกึ่งกลาง และจุดที่ไอเดียผิด ถ้าหาสองตัวนี้ไม่เจอ ก็ไม่มี FVG

> [!check]- เช็กความเข้าใจ: การหา FVG
> **Q1.** แท่ง 1 Low **50.00** แท่ง 3 High **49.70** มีแท่งแดงใหญ่อยู่ตรงกลาง นี่คืออะไร ใหญ่เท่าไหร่ และ CE อยู่ที่ไหน?
> > [!answer]-
> > FVG ขาลง (SIBI): 50.00 − 49.70 = 0.30  CE = 49.85 ใช้ไม่ได้ถ้ามีแท่งปิดเหนือ 50.00
> **Q2.** แท่ง 1 High 100.20 แท่ง 3 Low 100.15 มี FVG ไหม?
> > [!answer]-
> > ไม่มี Low ของแท่ง 3 อยู่ใต้ High ของแท่ง 1 แท่งเทียนจึงซ้อนกัน: ไม่มีช่องว่าง
""")
L.before_heading("th", "3.", """
> [!analogy]
> FVG เหมือน **รถเมล์ที่ข้ามหลายป้าย** เพราะวิ่งช้ากว่ากำหนด ผู้โดยสารที่รออยู่ที่ป้ายเหล่านั้นไม่ได้ขึ้น เมื่อรถเมล์วิ่งกลับมาตามเส้นทาง ผู้โดยสารยังรออยู่และได้ขึ้นในที่สุด นั่นคือการ "เติม" ตอนราคากลับมา
>
> **จุดที่เปรียบเทียบไม่ได้:** รถเมล์จริงวิ่งกลับมาตามเส้นทางเสมอ แต่ตลาดไม่จำเป็นต้องกลับ ในเทรนด์แรงบางช่องว่างไม่เคยถูกกลับมาเยือน และผู้โดยสารบางคนก็ถอดใจกลับบ้าน (คำสั่งถูกยกเลิก)

> [!check]- เช็กความเข้าใจ: ทำไมช่องว่างถูกกลับมาเยือน
> **Q1.** ทำไม FVG จึงนับเป็นสภาพคล่องภายใน?
> > [!answer]-
> > เพราะอยู่ภายในกรอบปัจจุบัน และมีคำสั่งที่ยังไม่ได้เติมจากเทรดเดอร์ที่พลาดการวิ่งเร็ว ราคามักถูกดึงกลับเข้าไปก่อนจะไปหากองสภาพคล่องภายนอกถัดไป
""")
L.before_callout("th", "action", """
> [!walkthrough] ไล่ทีละขั้น: เทรดตอนราคากลับมาด้วยความเสี่ยงที่กำหนด
> FVG ขาขึ้น **100.20–100.60** (CE **100.40**) เกิดจากแรงส่งที่ทะลุโครงสร้าง อยู่ใน Discount บัญชี **10,000 ดอลลาร์** เสี่ยง **1% = 100 ดอลลาร์**
> 1. **จุดเข้า:** Limit buy ที่ CE **100.40**
> 2. **Stop:** ใต้ Low ของแท่ง 1 และช่องว่าง: **99.90** → ความเสี่ยงต่อหน่วย = 100.40 − 99.90 = **0.50**
> 3. **ขนาด:** 100 ÷ 0.50 = **200 หน่วย**
> 4. **เป้าหมาย:** BSL ถัดไปที่ **101.90** → ผลตอบแทนต่อหน่วย **1.50** → **3R** (= 300 ดอลลาร์ถ้าได้ผล −100 ดอลลาร์ถ้าไม่ได้)
> 5. **แล้วไง?** FVG ให้ตัวเลขครบทั้งสาม (จุดเข้า Stop จุดที่ไอเดียผิด) ก่อนราคาจะมาถึง ตัดสินใจไว้ล่วงหน้า ตอนราคากลับมาคุณแค่ทำตาม

> [!check]- เช็กความเข้าใจ: เทรดตอนราคากลับมา
> **Q1.** ไม้เดิม แต่คุณเลือกเข้าแบบรุกที่ขอบบนของช่องว่าง (100.60) ความเสี่ยงต่อหน่วยและขนาดใหม่เป็นเท่าไหร่?
> > [!answer]-
> > ความเสี่ยง = 100.60 − 99.90 = 0.70 → ขนาด = 100 ÷ 0.70 = 142.9 → 142 หน่วย โอกาสได้เข้าสูงกว่า แต่ขนาดเล็กลง

> [!market]
> - **ฟอเร็กซ์:** FVG เกิดตลอดเวลาบนไทม์เฟรมต่ำ ใช้เฉพาะที่เกิดจากแรงส่งช่วงลอนดอน/นิวยอร์ก *(ดู 5.6)*
> - **ทองคำ:** FVG ใหญ่หลังข้อมูลสหรัฐตอน 19:30 UTC+7 (ฤดูร้อน) มักถูกกลับมาเยือน แต่กว้าง จึงต้องลดขนาด *(ดู 0.4)*
> - **หุ้น:** **Gap** ข้ามคืนระหว่างเซสชันไม่เหมือน FVG ระหว่างวัน แม้เทรดเดอร์จะปฏิบัติกับ Gap ช่วงเปิดขนาดใหญ่คล้ายกัน FVG ภายในช่วงซื้อขายปกติทำงานตามบทเรียนนี้ *(ดู 0.5)*
> - **คริปโต:** ซื้อขาย 24/7 จึงไม่มี Gap ระหว่างเซสชัน มีแต่ FVG ระหว่างวัน การล้างพอร์ตที่เร็วมากทิ้ง FVG ใหญ่ซึ่งมักถูกกลับมาเยือน *(ดู 0.7)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** นิยาม FVG ขาขึ้นในประโยคเดียว โดยใช้แท่งเทียนสามแท่ง
> > [!answer]-
> > แท่งเทียนสามแท่งที่แท่งกลางเป็นแท่งขึ้นตัวใหญ่ และ Low ของแท่ง 3 อยู่เหนือ High ของแท่ง 1 ช่องว่างระหว่างสองค่านี้คือ FVG
> **Q2.** อะไรที่ทำให้ FVG ใช้ไม่ได้?
> > [!answer]-
> > แท่งเทียนที่ **ปิด** ทะลุขอบไกลของช่องว่าง (ใต้ High ของแท่ง 1 สำหรับ FVG ขาขึ้น) ไส้ที่ทะลุแต่ปิดกลับเข้ามาไม่ได้ทำให้ใช้ไม่ได้
""")

L.set_meta("level", "v2")
L.save()
