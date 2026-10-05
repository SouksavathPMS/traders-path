"""B4 · v2 upgrade of 5.3 Dealing Range: Premium & Discount (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("05 Liquidity & ICT/5.3 Dealing Range- Premium & Discount.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Every time price makes a move, it creates a "price range" from its lowest point to its highest point. The top half of that range is the expensive part; the bottom half is the cheap part. If you think price will go up, you want to buy in the cheap half, not the expensive half, for the same reason you'd rather buy a shirt on sale. Buying cheap also lets you put your stop close and your target far away, which is where good trades come from.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Swing high / swing low** — a turning point in price *(see 2.1)*.
> - **Leg** — one move from a swing low to a swing high (or the reverse).
> - **Dealing range** — the price range of the current leg on your timeframe.
> - **Equilibrium (EQ)** — the 50% level of the dealing range: the "fair" middle.
> - **Premium** — the upper half of the range (expensive; better for selling).
> - **Discount** — the lower half of the range (cheap; better for buying).
> - **OTE (optimal trade entry)** — ICT's name for the 62–79% retracement zone of a leg.
> - **Retracement** — how far price pulls back into the previous leg, as a percentage *(Fibonacci, see 6.1)*.
> - **PD array (premium/discount array)** — any reason for price to react inside premium or discount: FVG, order block, swept level, supply/demand zone.
> - **BOS** — break of structure *(see 2.3)*.
> - **HTF / MTF / LTF** — higher / middle / lower timeframe *(see 1.5, 2.6)*.
> - **BSL** — buy-side liquidity above highs *(see 5.1)*.
""")
L.before_heading("en", "2.", """
![[p5-range-pips.en.svg]]

> [!analogy]
> A dealing range is like a **shop's price list**. The same shirt is sold in the **sale section** (discount) and in the **premium aisle** (premium). A smart shopper who wants the shirt buys it on sale; a smart seller sells in the premium aisle. You don't need to know what the shirt is "really" worth; you just avoid paying the top price.
>
> **Where it breaks:** a shop's price list stays fixed. A dealing range is redrawn every time the market makes a new high or low, so "cheap" today can become "expensive" tomorrow.

> [!walkthrough] Step by step: premium and discount in pips
> EUR/USD makes an up-leg from **1.0800** to **1.0900** (100 pips) and breaks structure.
> 1. **Equilibrium** = (1.0800 + 1.0900) ÷ 2 = **1.0850**.
> 2. **Premium** = 1.0850 to 1.0900 (top **50 pips**). **Discount** = 1.0800 to 1.0850 (bottom **50 pips**).
> 3. **OTE for longs** = 62–79% retracement from the high: 1.0900 − 0.62 × 100 pips = **1.0838**; 1.0900 − 0.79 × 100 pips = **1.0821** → **1.0821–1.0838**.
> 4. **Entry A, in premium:** buy at **1.0880**, stop **1.0795** (below the low), target **1.0920** (BSL above the high) → risk 85 pips, reward 40 pips → **0.47R**.
> 5. **Entry B, in discount (inside the OTE):** buy at **1.0830**, same stop and target → risk 35 pips, reward 90 pips → **2.57R**.
> 6. **So what?** Same chart, same direction, same stop and target, yet the discount entry has more than five times the reward per unit of risk. Location is half of your edge.

> [!check]- Check your understanding
> **Q1.** A leg runs from 50.00 to 60.00. Where is equilibrium, and is 57.00 premium or discount?
> > [!answer]-
> > Equilibrium = 55.00. 57.00 is above it, so it's premium (expensive for buying).
""")
L.before_heading("en", "3.", """
> [!check]- Check your understanding: the OTE
> **Q1.** A down-leg runs from **1.2700** to **1.2500**. For a short, where is the OTE (62–79% retracement)?
> > [!answer]-
> > Range 200 pips. 1.2500 + 0.62 × 200 pips = 1.2624; 1.2500 + 0.79 × 200 pips = 1.2658 → OTE 1.2624–1.2658 (above equilibrium 1.2600, i.e. in premium).
> **Q2.** Price is inside the OTE but there's no FVG, order block or swept level there. Do you buy?
> > [!answer]-
> > No. The OTE is a location, not a reason. You still need a PD array and an LTF trigger.
""")
L.before_callout("en", "action", """
> [!check]- Check your understanding: ranges inside ranges
> **Q1.** On the 15-minute chart price is in discount, but on the daily chart it's in the top 10% of the range. Is this an A-grade long?
> > [!answer]-
> > No. It's cheap inside an expensive area. The best longs are in discount on both the HTF and the LTF range.

> [!market]
> - **Forex:** clean ranges; the 50% level often acts as a magnet during quiet sessions *(see 5.6)*.
> - **Gold:** legs are large (often 50–150 USD), so the gap between premium and discount entries is many dollars per ounce; position size matters even more *(see 0.4)*.
> - **Stocks:** use regular-session data; an overnight gap can move the whole range at once *(see 0.5)*.
> - **Crypto:** 24/7 legs with deep wicks; draw the range on candle **closes** or bodies if wicks make it unreadable *(see 0.7)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Why does buying in discount improve R:R even when the stop and target don't change?
> > [!answer]-
> > Because the entry is closer to the stop (less risk) and further from the target (more reward). The same idea becomes a much better bet.
> **Q2.** Up-leg 2,000 → 2,100. Give equilibrium and the OTE band for longs.
> > [!answer]-
> > Equilibrium 2,050. OTE = 2,100 − 0.62 × 100 = 2,038 to 2,100 − 0.79 × 100 = 2,021 → 2,021–2,038.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ทุกครั้งที่ราคาวิ่ง จะเกิด "กรอบราคา" จากจุดต่ำสุดถึงจุดสูงสุดของการวิ่งนั้น ครึ่งบนของกรอบคือส่วนที่แพง ครึ่งล่างคือส่วนที่ถูก ถ้าคุณคิดว่าราคาจะขึ้น คุณอยากซื้อในครึ่งที่ถูก ไม่ใช่ครึ่งที่แพง ด้วยเหตุผลเดียวกับที่อยากซื้อเสื้อตอนลดราคา การซื้อถูกยังทำให้วาง Stop ได้ใกล้และเป้าหมายอยู่ไกล ซึ่งเป็นที่มาของไม้เทรดที่ดี
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **Swing high / Swing low** — จุดกลับตัวของราคา *(ดู 2.1)*
> - **ขา (Leg)** — การวิ่งหนึ่งครั้งจาก Swing low ถึง Swing high (หรือกลับกัน)
> - **Dealing range** — กรอบราคาของขาปัจจุบันบนไทม์เฟรมของคุณ
> - **จุดสมดุล (Equilibrium, EQ)** — ระดับ 50% ของ Dealing range: จุดกลางที่ "ยุติธรรม"
> - **Premium** — ครึ่งบนของกรอบ (แพง เหมาะกับการขาย)
> - **Discount** — ครึ่งล่างของกรอบ (ถูก เหมาะกับการซื้อ)
> - **OTE (Optimal trade entry)** — ชื่อที่ ICT ใช้เรียกโซนการย่อกลับ 62–79% ของขา
> - **การย่อกลับ (Retracement)** — ราคาย่อกลับเข้าไปในขาก่อนหน้ามากแค่ไหน คิดเป็นเปอร์เซ็นต์ *(Fibonacci ดู 6.1)*
> - **PD array (Premium/Discount array)** — เหตุผลใดก็ตามที่ราคาจะตอบสนองใน Premium หรือ Discount: FVG Order block ระดับที่ถูกกวาด โซน Supply/Demand
> - **BOS** — การทะลุโครงสร้าง *(ดู 2.3)*
> - **HTF / MTF / LTF** — ไทม์เฟรมสูง / กลาง / ต่ำ *(ดู 1.5, 2.6)*
> - **BSL** — สภาพคล่องฝั่งซื้อเหนือจุดสูง *(ดู 5.1)*
""")
L.before_heading("th", "2.", """
![[p5-range-pips.th.svg]]

> [!analogy]
> Dealing range เหมือน **ป้ายราคาในร้าน** เสื้อตัวเดียวกันขายทั้งใน **มุมลดราคา** (Discount) และใน **มุมพรีเมียม** (Premium) นักช้อปที่ฉลาดและอยากได้เสื้อจะซื้อตอนลดราคา ผู้ขายที่ฉลาดจะขายในมุมพรีเมียม คุณไม่ต้องรู้ว่าเสื้อ "จริง ๆ" มีค่าเท่าไหร่ แค่อย่าจ่ายราคาสูงสุดก็พอ
>
> **จุดที่เปรียบเทียบไม่ได้:** ป้ายราคาในร้านคงที่ แต่ Dealing range ถูกวาดใหม่ทุกครั้งที่ตลาดทำจุดสูงหรือต่ำใหม่ "ถูก" วันนี้อาจกลายเป็น "แพง" พรุ่งนี้

> [!walkthrough] ไล่ทีละขั้น: Premium และ Discount เป็น pip
> EUR/USD ทำขาขึ้นจาก **1.0800** ถึง **1.0900** (100 pip) และทะลุโครงสร้าง
> 1. **จุดสมดุล** = (1.0800 + 1.0900) ÷ 2 = **1.0850**
> 2. **Premium** = 1.0850 ถึง 1.0900 (**50 pip** บน) **Discount** = 1.0800 ถึง 1.0850 (**50 pip** ล่าง)
> 3. **OTE สำหรับ Long** = ย่อกลับ 62–79% จากจุดสูง: 1.0900 − 0.62 × 100 pip = **1.0838**; 1.0900 − 0.79 × 100 pip = **1.0821** → **1.0821–1.0838**
> 4. **จุดเข้า A ใน Premium:** ซื้อที่ **1.0880** Stop **1.0795** (ใต้จุดต่ำ) เป้าหมาย **1.0920** (BSL เหนือจุดสูง) → ความเสี่ยง 85 pip ผลตอบแทน 40 pip → **0.47R**
> 5. **จุดเข้า B ใน Discount (ใน OTE):** ซื้อที่ **1.0830** Stop และเป้าหมายเดิม → ความเสี่ยง 35 pip ผลตอบแทน 90 pip → **2.57R**
> 6. **แล้วไง?** กราฟเดียวกัน ทิศทางเดียวกัน Stop และเป้าหมายเดียวกัน แต่จุดเข้าใน Discount ให้ผลตอบแทนต่อหน่วยความเสี่ยงมากกว่าห้าเท่า ตำแหน่งคือครึ่งหนึ่งของความได้เปรียบของคุณ

> [!check]- เช็กความเข้าใจ
> **Q1.** ขาหนึ่งวิ่งจาก 50.00 ถึง 60.00 จุดสมดุลอยู่ที่ไหน และ 57.00 เป็น Premium หรือ Discount?
> > [!answer]-
> > จุดสมดุล = 55.00 ส่วน 57.00 อยู่เหนือจุดนั้น จึงเป็น Premium (แพงสำหรับการซื้อ)
""")
L.before_heading("th", "3.", """
> [!check]- เช็กความเข้าใจ: OTE
> **Q1.** ขาลงวิ่งจาก **1.2700** ถึง **1.2500** สำหรับการ Short OTE (ย่อกลับ 62–79%) อยู่ที่ไหน?
> > [!answer]-
> > กรอบ 200 pip  1.2500 + 0.62 × 200 pip = 1.2624; 1.2500 + 0.79 × 200 pip = 1.2658 → OTE 1.2624–1.2658 (เหนือจุดสมดุล 1.2600 คืออยู่ใน Premium)
> **Q2.** ราคาอยู่ใน OTE แต่ไม่มี FVG Order block หรือระดับที่ถูกกวาดตรงนั้น คุณซื้อไหม?
> > [!answer]-
> > ไม่ซื้อ OTE เป็นแค่ตำแหน่ง ไม่ใช่เหตุผล ยังต้องมี PD array และสัญญาณจาก LTF
""")
L.before_callout("th", "action", """
> [!check]- เช็กความเข้าใจ: กรอบซ้อนกรอบ
> **Q1.** บนกราฟ 15 นาที ราคาอยู่ใน Discount แต่บนกราฟรายวันอยู่ใน 10% บนสุดของกรอบ นี่คือ Long เกรด A ไหม?
> > [!answer]-
> > ไม่ใช่ เป็นของถูกในพื้นที่ที่แพง Long ที่ดีที่สุดอยู่ใน Discount ทั้งในกรอบของ HTF และ LTF

> [!market]
> - **ฟอเร็กซ์:** กรอบชัดเจน ระดับ 50% มักทำตัวเหมือนแม่เหล็กในช่วงเซสชันที่เงียบ *(ดู 5.6)*
> - **ทองคำ:** ขาใหญ่ (มัก 50–150 ดอลลาร์) ส่วนต่างระหว่างจุดเข้าใน Premium กับ Discount จึงหลายดอลลาร์ต่อออนซ์ ขนาดไม้ยิ่งสำคัญ *(ดู 0.4)*
> - **หุ้น:** ใช้ข้อมูลช่วงซื้อขายปกติ Gap ข้ามคืนอาจย้ายทั้งกรอบในครั้งเดียว *(ดู 0.5)*
> - **คริปโต:** ขาวิ่ง 24/7 และไส้เทียนลึก วาดกรอบจาก **ราคาปิด** หรือตัวแท่งถ้าไส้ทำให้อ่านยาก *(ดู 0.7)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** ทำไมการซื้อใน Discount จึงทำให้ R:R ดีขึ้น แม้ Stop และเป้าหมายไม่เปลี่ยน?
> > [!answer]-
> > เพราะจุดเข้าใกล้ Stop มากขึ้น (เสี่ยงน้อยลง) และไกลจากเป้าหมายมากขึ้น (ผลตอบแทนมากขึ้น) ไอเดียเดียวกันกลายเป็นการเดิมพันที่ดีกว่ามาก
> **Q2.** ขาขึ้น 2,000 → 2,100 บอกจุดสมดุลและโซน OTE สำหรับ Long
> > [!answer]-
> > จุดสมดุล 2,050  OTE = 2,100 − 0.62 × 100 = 2,038 ถึง 2,100 − 0.79 × 100 = 2,021 → 2,021–2,038
""")

L.set_meta("level", "v2")
L.save()
