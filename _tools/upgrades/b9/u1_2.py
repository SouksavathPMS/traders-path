"""B9a · v2 upgrade of 1.2 How Markets Move (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("01 Foundations/1.2 How Markets Move.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Price is set by people agreeing to trade. Some people wait patiently with orders at fixed prices; others want to trade right now and accept whatever price is available. When the impatient buyers use up all the waiting sellers at one price, the next trade happens at a higher price, and the chart goes up. That's all a price move is.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Order book** — the list of waiting buy and sell orders at each price.
> - **Bid / ask (offer)** — the best price buyers are paying / sellers are asking right now.
> - **Spread** — ask minus bid: the cost of trading immediately.
> - **Liquidity** — how much can be traded near the current price without moving it.
> - **Market order** — buy or sell now at the best available price.
> - **Limit order** — buy or sell only at your price or better.
> - **Stop order** — becomes a market order when price reaches a level *(stop loss = a stop order that closes your trade)*.
> - **Slippage** — the difference between the price you expected and the price you got.
> - **Aggressive vs passive** — taking liquidity with market orders vs providing it with limit orders.
> - **Market maker** — a firm that always quotes a bid and an ask and earns the spread.
> - **HFT (high-frequency trading)** — computer programs that trade in fractions of a second.
""")
L.before_heading("en", "2.", """
> [!analogy]
> Think of a **morning market stall** selling mangoes. Sellers write prices on their boxes and wait (limit orders). A restaurant buyer who needs 200 kg now (a market order) buys the cheapest boxes first, then the next cheapest, until the order is filled. By the end, the "price of mangoes" is higher, simply because the cheap boxes are gone.
>
> **Where it breaks:** at the market stall you can see every box. In financial markets, many orders are hidden, cancelled in milliseconds, or sit on other venues, so the visible book is only part of the picture *(see 7.3)*.

> [!check]- Check your understanding: the auction
> **Q1.** "Price went up because there were more buyers than sellers." What's wrong with this sentence, and how would you fix it?
> > [!answer]-
> > Every trade has one buyer and one seller, so the numbers are always equal. Better: "Price went up because buyers were more aggressive: they kept paying the ask until sellers were found at higher prices."
""")
L.before_heading("en", "3.", """
![[p1-book-walk.en.svg]]

> [!walkthrough] Step by step: what a market order really costs
> Asks: **250 at 100.01**, **300 at 100.02**, **400 at 100.03**, **500 at 100.04** (illustrative).
> 1. **Buy 550 at market:** 250 × 100.01 + 300 × 100.02 = 55,008.50 → average **100.0155**.
> 2. If all 550 had filled at 100.01 it would cost 55,005.50 → **slippage = 3.00 USD**.
> 3. **Buy 1,200:** fills 250 + 300 + 400 + the first 250 at 100.04 → average **100.0254**, slippage **18.50 USD**.
> 4. **Spread cost:** a 0.8-pip EUR/USD spread on 1 standard lot (1 pip = 10 USD) costs **8 USD** each time you trade; 20 trades a month = **160 USD**.
> 5. **So what?** Bigger orders in thinner books cost more. Check the spread and depth before using market orders.

> [!check]- Check your understanding: bid, ask and spread
> **Q1.** Bid 1.0850, ask 1.0852 on EUR/USD. What's the spread in pips, and what does a 1-lot trade pay for it?
> > [!answer]-
> > 1.0852 − 1.0850 = 0.0002 = **2 pips**; at 10 USD per pip per lot = **20 USD**.
""")
L.before_heading("en", "4.", """
> [!check]- Check your understanding: order types
> **Q1.** You want to buy only if price falls back to 1,950 support. Which order type do you use, and what's the risk?
> > [!answer]-
> > A **limit buy** at 1,950. You get your price, but if price never comes back, you're not filled.
> **Q2.** Why do big players care where stop losses sit?
> > [!answer]-
> > Stops become market orders when hit. A cluster of sell stops is a pool of market sell orders that a big buyer can buy from (liquidity).
""")
L.before_callout("en", "action", """
> [!check]- Check your understanding: why price moves
> **Q1.** Name the three causes of a change in urgency from section 5, with one example each.
> > [!answer]-
> > New information (an inflation release), forced flows (stop losses or margin calls being triggered), liquidity gaps (a thin book at night lets a small order move price a lot).

> [!market]
> - **Forex:** no single central order book; your broker or liquidity provider shows you a quote. Spreads widen around 04:00 UTC+7 rollover and news *(see 0.3)*.
> - **Gold:** spreads widen in the Asian session and at US data releases *(see 0.4)*.
> - **Stocks:** each exchange has a real order book; small-cap stocks can have very thin books *(see 0.5)*.
> - **Crypto:** order books are public on each exchange; liquidity drops at weekends *(see 0.7)*.

> [!caution]
> A market order or stop in a thin market can fill far from the price you saw: at news releases, at the weekly open, or in small stocks and coins. A stop loss limits the loss in normal conditions, but it does not guarantee the price.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** The book shows 100 for sale at 50.10 and 400 at 50.12. You buy 300 at market. What's your average price?
> > [!answer]-
> > (100 × 50.10 + 200 × 50.12) ÷ 300 = (5,010 + 10,024) ÷ 300 = **50.1133**.
> **Q2.** Explain in one sentence why a stop loss is "a market order waiting to happen".
> > [!answer]-
> > When price touches the stop level, the stop becomes a market order and fills at the best available price, not necessarily at the stop price.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ราคาเกิดจากคนตกลงซื้อขายกัน บางคนรออย่างอดทนด้วยคำสั่งที่ราคาคงที่ อีกกลุ่มอยากซื้อขายเดี๋ยวนี้และยอมรับราคาที่มี เมื่อผู้ซื้อใจร้อนกินผู้ขายที่รออยู่ที่ราคาหนึ่งจนหมด การซื้อขายถัดไปก็เกิดที่ราคาสูงขึ้น และกราฟก็ขึ้น นั่นคือทั้งหมดของการขยับราคา
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **สมุดคำสั่ง (Order book)** — รายการคำสั่งซื้อและขายที่รออยู่ในแต่ละราคา
> - **Bid / Ask (Offer)** — ราคาดีที่สุดที่ผู้ซื้อให้ / ผู้ขายขอ ณ ตอนนี้
> - **Spread** — Ask ลบ Bid: ต้นทุนของการซื้อขายทันที
> - **สภาพคล่อง (Liquidity)** — ปริมาณที่ซื้อขายได้ใกล้ราคาปัจจุบันโดยไม่ทำให้ราคาขยับ
> - **คำสั่ง Market (Market order)** — ซื้อหรือขายเดี๋ยวนี้ที่ราคาดีที่สุดที่มี
> - **คำสั่ง Limit (Limit order)** — ซื้อหรือขายเฉพาะที่ราคาของคุณหรือดีกว่า
> - **คำสั่ง Stop (Stop order)** — กลายเป็นคำสั่ง Market เมื่อราคาแตะระดับที่ตั้ง *(Stop loss = คำสั่ง Stop ที่ปิดไม้ของคุณ)*
> - **Slippage** — ส่วนต่างระหว่างราคาที่คาดกับราคาที่ได้จริง
> - **แบบรุก vs แบบรอ (Aggressive vs passive)** — กินสภาพคล่องด้วยคำสั่ง Market vs ให้สภาพคล่องด้วยคำสั่ง Limit
> - **ผู้ดูแลสภาพคล่อง (Market maker)** — บริษัทที่เสนอ Bid และ Ask ตลอดเวลาและได้กำไรจาก Spread
> - **HFT (High-frequency trading)** — โปรแกรมคอมพิวเตอร์ที่ซื้อขายในเสี้ยววินาที
""")
L.before_heading("th", "2.", """
> [!analogy]
> นึกถึง **แผงมะม่วงในตลาดเช้า** ผู้ขายเขียนราคาไว้บนลังแล้วรอ (คำสั่ง Limit) ร้านอาหารที่ต้องการ 200 กิโลเดี๋ยวนี้ (คำสั่ง Market) ซื้อลังที่ถูกที่สุดก่อน แล้วลังถัดไป จนครบ พอจบ "ราคามะม่วง" ก็สูงขึ้น เพียงเพราะลังราคาถูกหมดไปแล้ว
>
> **จุดที่เปรียบเทียบไม่ได้:** ที่แผงมะม่วงคุณเห็นทุกลัง แต่ในตลาดการเงิน คำสั่งจำนวนมากถูกซ่อน ถูกยกเลิกในเสี้ยววินาที หรืออยู่ในสถานที่ซื้อขายอื่น สมุดคำสั่งที่เห็นจึงเป็นแค่ส่วนหนึ่งของภาพ *(ดู 7.3)*

> [!check]- เช็กความเข้าใจ: การประมูล
> **Q1.** "ราคาขึ้นเพราะมีผู้ซื้อมากกว่าผู้ขาย" ประโยคนี้ผิดตรงไหน และจะแก้อย่างไร?
> > [!answer]-
> > ทุกการซื้อขายมีผู้ซื้อหนึ่งและผู้ขายหนึ่ง จำนวนจึงเท่ากันเสมอ ที่ถูกกว่า: "ราคาขึ้นเพราะผู้ซื้อรุกมากกว่า: พวกเขาจ่ายที่ราคา Ask ต่อไปเรื่อย ๆ จนเจอผู้ขายที่ราคาสูงขึ้น"
""")
L.before_heading("th", "3.", """
![[p1-book-walk.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: คำสั่ง Market มีต้นทุนจริงเท่าไร
> Ask: **250 ที่ 100.01**, **300 ที่ 100.02**, **400 ที่ 100.03**, **500 ที่ 100.04** (ตัวอย่าง)
> 1. **ซื้อ Market 550:** 250 × 100.01 + 300 × 100.02 = 55,008.50 → เฉลี่ย **100.0155**
> 2. ถ้าทั้ง 550 ได้ที่ 100.01 จะเสีย 55,005.50 → **Slippage = 3.00 ดอลลาร์**
> 3. **ซื้อ 1,200:** ได้ 250 + 300 + 400 + อีก 250 แรกที่ 100.04 → เฉลี่ย **100.0254** Slippage **18.50 ดอลลาร์**
> 4. **ต้นทุน Spread:** Spread EUR/USD 0.8 pip กับ 1 ล็อตมาตรฐาน (1 pip = 10 ดอลลาร์) เสีย **8 ดอลลาร์** ทุกครั้งที่เทรด 20 ไม้ต่อเดือน = **160 ดอลลาร์**
> 5. **แล้วไง?** คำสั่งใหญ่ในสมุดคำสั่งที่บางมีต้นทุนสูงกว่า ตรวจ Spread และความลึกก่อนใช้คำสั่ง Market

> [!check]- เช็กความเข้าใจ: Bid, Ask และ Spread
> **Q1.** EUR/USD Bid 1.0850 Ask 1.0852 Spread กี่ pip และเทรด 1 ล็อตต้องจ่ายเท่าไร?
> > [!answer]-
> > 1.0852 − 1.0850 = 0.0002 = **2 pip** ที่ 10 ดอลลาร์ต่อ pip ต่อล็อต = **20 ดอลลาร์**
""")
L.before_heading("th", "4.", """
> [!check]- เช็กความเข้าใจ: ประเภทคำสั่ง
> **Q1.** คุณอยากซื้อเฉพาะเมื่อราคาย่อกลับมาที่แนวรับ 1,950 ใช้คำสั่งแบบไหน และมีความเสี่ยงอะไร?
> > [!answer]-
> > **Limit buy** ที่ 1,950 ได้ราคาที่ต้องการ แต่ถ้าราคาไม่กลับมา คุณก็ไม่ได้เข้า
> **Q2.** ทำไมผู้เล่นรายใหญ่จึงสนใจว่า Stop loss อยู่ตรงไหน?
> > [!answer]-
> > Stop กลายเป็นคำสั่ง Market เมื่อถูกแตะ กลุ่ม Stop ฝั่งขายคือแหล่งคำสั่งขาย Market ที่ผู้ซื้อรายใหญ่ใช้ซื้อได้ (สภาพคล่อง)
""")
L.before_callout("th", "action", """
> [!check]- เช็กความเข้าใจ: ทำไมราคาขยับ
> **Q1.** บอกสาเหตุสามข้อของการเปลี่ยนแปลงความเร่งรีบจากหัวข้อ 5 พร้อมตัวอย่างข้อละหนึ่ง
> > [!answer]-
> > ข้อมูลใหม่ (การประกาศเงินเฟ้อ) กระแสเงินที่ถูกบังคับ (Stop loss หรือ Margin call ถูกเรียก) ช่องว่างสภาพคล่อง (สมุดคำสั่งบางตอนกลางคืน ทำให้คำสั่งเล็กขยับราคาได้มาก)

> [!market]
> - **ฟอเร็กซ์:** ไม่มีสมุดคำสั่งกลางที่เดียว โบรกเกอร์หรือผู้ให้สภาพคล่องแสดงราคาให้คุณ Spread ถ่างช่วงตัดรอบวันราว 04:00 UTC+7 และช่วงข่าว *(ดู 0.3)*
> - **ทองคำ:** Spread ถ่างในช่วงเอเชียและตอนประกาศข้อมูลสหรัฐ *(ดู 0.4)*
> - **หุ้น:** แต่ละตลาดหลักทรัพย์มีสมุดคำสั่งจริง หุ้นขนาดเล็กอาจมีสมุดคำสั่งที่บางมาก *(ดู 0.5)*
> - **คริปโต:** สมุดคำสั่งเปิดเผยในแต่ละกระดานเทรด สภาพคล่องลดลงช่วงสุดสัปดาห์ *(ดู 0.7)*

> [!caution]
> คำสั่ง Market หรือ Stop ในตลาดที่บางอาจได้ราคาห่างจากที่เห็นมาก: ตอนประกาศข่าว ตอนเปิดตลาดต้นสัปดาห์ หรือในหุ้นและเหรียญขนาดเล็ก Stop loss จำกัดการขาดทุนในสภาวะปกติ แต่ไม่รับประกันราคา
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** สมุดคำสั่งแสดง 100 ตั้งขายที่ 50.10 และ 400 ที่ 50.12 คุณซื้อ Market 300 ราคาเฉลี่ยเท่าไร?
> > [!answer]-
> > (100 × 50.10 + 200 × 50.12) ÷ 300 = (5,010 + 10,024) ÷ 300 = **50.1133**
> **Q2.** อธิบายในหนึ่งประโยคว่าทำไม Stop loss คือ "คำสั่ง Market ที่รอเกิดขึ้น"
> > [!answer]-
> > เมื่อราคาแตะระดับ Stop คำสั่ง Stop จะกลายเป็นคำสั่ง Market และได้ราคาดีที่สุดที่มี ไม่จำเป็นต้องเป็นราคา Stop
""")

L.set_meta("level", "v2")
L.save()
