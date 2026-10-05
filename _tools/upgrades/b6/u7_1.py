"""B6 · v2 upgrade of 7.1 Auction Market Theory: Balance & Imbalance (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("07 Orderflow & Auction Market Theory/7.1 Auction Market Theory- Balance & Imbalance.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Every market is an auction that never stops. Price goes up to see if sellers appear, and down to see if buyers appear. When both sides are happy at a price, the market stays around it for a long time: that's **balance**. When something new happens (news, results), the old price stops making sense and the market moves quickly until it finds a new price where both sides are happy again: that's **imbalance**. Knowing which of the two is happening right now tells you whether to bet on a return to the middle or on the move continuing.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Auction** — a process where price moves until buyers and sellers agree to trade.
> - **AMT (Auction Market Theory)** — a way of reading markets as a continuous two-way auction (J. Peter Steidlmayer, Chicago Board of Trade, 1980s).
> - **Value** — the price area where most trading happens; what the market currently considers "fair".
> - **Balance** — price rotating inside a range around value; neither side in control.
> - **Imbalance** — price moving directionally away from old value to find new value.
> - **Acceptance** — price staying at a new level with time and volume: the market agrees with it.
> - **Rejection** — price moving through a level quickly with little volume: the market disagrees with it.
> - **Failed auction** — a quick break out of balance that returns inside; the AMT name for a sweep *(see 5.2)*.
> - **Responsive activity** — buying below value or selling above value ("this is cheap / expensive").
> - **Initiative activity** — buying above value or selling below value ("value is moving").
> - **Edges** — the top and bottom of a balance range.
> - **Volume** — how much was traded; here, the market's "vote" on a price.
""")
L.before_heading("en", "2.", """
![[p7-night-market.en.svg]]

> [!analogy]
> A **night-market stall** runs an auction every evening. If there's a long queue for mango sticky rice at 60 baht, the seller raises the price. At 80 baht nobody stops, so the price drops back. At 70 baht boxes sell steadily: that's value, and the stall is in **balance**. When tour buses arrive, the old price is suddenly too cheap: the seller raises to 90 and still sells more boxes than ever. That's **imbalance** and **new value**.
>
> **Where it breaks:** the stall owner sets the price alone. In a real market thousands of buyers and sellers move price together, and nobody announces the "tour buses"; you see them only through price, time and volume.

> [!walkthrough] Step by step: the night market in auction terms
> 1. **18:00, 60 THB, 40 boxes, long queue:** buyers are more eager than the seller → price must rise to find the other side.
> 2. **18:30, 70 THB, 120 boxes:** the most business is done here → **value**.
> 3. **19:00, 80 THB, 5 boxes:** almost no volume → **rejection**. Price returns to 70.
> 4. **19:30, 70 THB, 110 boxes:** back at value, plenty of trade → **balance**.
> 5. **20:00, 90 THB, 150 boxes:** new information (tour buses); a higher price **and** more volume → **acceptance** of new value = **imbalance**.
> 6. **So what?** Price alone can't tell you if 80 or 90 is "too high". Volume and time at that price can: 80 was rejected (5 boxes), 90 was accepted (150 boxes).

> [!check]- Check your understanding: balance vs imbalance
> **Q1.** A pair has traded between 1.0850 and 1.0920 for five days. Balance or imbalance? What's the basic approach?
> > [!answer]-
> > Balance. Fade the edges back toward the middle; don't chase breakouts without acceptance.
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: is a breakout accepted? (illustrative)
> A stock has been in balance between **99.6** and **104.9**. Average hourly volume: **10,000** shares.
> 1. **Case A:** price spikes to **105.6** on 9,000 shares, then the next hourly candle closes at **104.5**, back inside. Little volume, no time outside → **rejection / failed auction**. Plan: fade it back toward the middle (102.25) and the other edge (99.6).
> 2. **Case B:** price breaks to **105.6** and the next three hours close at 105.4, 106.0, 106.3 on **22,000**, **25,000** and **21,000** shares (2.2–2.5× normal). Time **and** volume outside → **acceptance**. Plan: buy pullbacks toward 104.9 (old edge, now support, *see 2.4*).
> 3. **So what?** The same breakout candle leads to opposite trades. You decide only **after** you see time and volume, not on the first poke.

> [!check]- Check your understanding: acceptance
> **Q1.** Price breaks above a range on low volume and comes back inside within 20 minutes. What is it called, and where is price likely to go?
> > [!answer]-
> > A failed auction (rejection). Price often travels back through the range toward the opposite edge.
""")
L.before_callout("en", "example", """
> [!check]- Check your understanding: responsive vs initiative
> **Q1.** Value is 100–104. Price is at 106 and buyers keep lifting offers. Responsive or initiative buying?
> > [!answer]-
> > Initiative buying: they are buying **above** value, betting that value is moving up.
> **Q2.** Price drops to 99.5 and buyers step in strongly, pushing it back to 101. Responsive or initiative?
> > [!answer]-
> > Responsive buying: buying **below** value because it's cheap, expecting a return to value.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** spot FX has no central volume; AMT traders use futures volume (e.g. 6E = euro futures on CME) or tick volume as a rough guide *(see 0.3)*.
> - **Gold:** gold futures (GC) give real volume; balance often forms in Asia and breaks in London/New York *(see 0.4, 5.6)*.
> - **Stocks & indices:** real exchange volume; the opening auction and the previous day's value are key *(see 0.5)*.
> - **Crypto:** volume differs by exchange; 24/7 trading means balance often forms at weekends and breaks on Monday *(see 0.7)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Name the three AMT variables and what each one does.
> > [!answer]-
> > Price advertises (moves to find the other side), time regulates (how long price stays = how accepted it is), volume validates (high volume = acceptance, low volume = rejection).
> **Q2.** In balance, which kind of trader usually wins, and in imbalance?
> > [!answer]-
> > Balance: responsive traders (fading the edges). Imbalance: initiative traders (going with the move).
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ทุกตลาดคือการประมูลที่ไม่เคยหยุด ราคาขึ้นเพื่อดูว่าผู้ขายจะโผล่มาไหม และลงเพื่อดูว่าผู้ซื้อจะโผล่มาไหม เมื่อทั้งสองฝั่งพอใจที่ราคาหนึ่ง ตลาดจะอยู่แถวนั้นนาน: นั่นคือ **สมดุล (Balance)** เมื่อมีเรื่องใหม่เกิดขึ้น (ข่าว งบ) ราคาเดิมไม่สมเหตุสมผลแล้ว ตลาดจะวิ่งเร็วจนกว่าจะเจอราคาใหม่ที่ทั้งสองฝั่งพอใจอีกครั้ง: นั่นคือ **ไม่สมดุล (Imbalance)** การรู้ว่าตอนนี้เป็นแบบไหน บอกคุณว่าควรเดิมพันว่าราคาจะกลับเข้ากลาง หรือจะวิ่งต่อ
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **การประมูล (Auction)** — กระบวนการที่ราคาขยับจนผู้ซื้อและผู้ขายตกลงซื้อขายกัน
> - **AMT (Auction Market Theory)** — การอ่านตลาดเป็นการประมูลสองทางต่อเนื่อง (J. Peter Steidlmayer, Chicago Board of Trade ทศวรรษ 1980)
> - **มูลค่า (Value)** — บริเวณราคาที่มีการซื้อขายมากที่สุด คือสิ่งที่ตลาดมองว่า "ยุติธรรม" ตอนนี้
> - **สมดุล (Balance)** — ราคาแกว่งในกรอบรอบมูลค่า ไม่มีฝั่งไหนคุม
> - **ไม่สมดุล (Imbalance)** — ราคาวิ่งเป็นทิศทางออกจากมูลค่าเดิมเพื่อหามูลค่าใหม่
> - **การยอมรับ (Acceptance)** — ราคาอยู่ที่ระดับใหม่ได้ด้วยเวลาและวอลุ่ม: ตลาดเห็นด้วย
> - **การปฏิเสธ (Rejection)** — ราคาวิ่งผ่านระดับเร็วด้วยวอลุ่มน้อย: ตลาดไม่เห็นด้วย
> - **การประมูลที่ล้มเหลว (Failed auction)** — การทะลุออกจากสมดุลแบบเร็วแล้วกลับเข้ามา ชื่อแบบ AMT ของการกวาด *(ดู 5.2)*
> - **กิจกรรมตอบสนอง (Responsive)** — ซื้อใต้มูลค่าหรือขายเหนือมูลค่า ("ถูกแล้ว / แพงแล้ว")
> - **กิจกรรมริเริ่ม (Initiative)** — ซื้อเหนือมูลค่าหรือขายใต้มูลค่า ("มูลค่ากำลังย้าย")
> - **ขอบ (Edges)** — ยอดและก้นของกรอบสมดุล
> - **วอลุ่ม (Volume)** — ปริมาณที่ซื้อขาย ในที่นี้คือ "คะแนนโหวต" ของตลาดต่อราคา
""")
L.before_heading("th", "2.", """
![[p7-night-market.th.svg]]

> [!analogy]
> **แผงตลาดนัดกลางคืน** เปิดประมูลทุกเย็น ถ้าข้าวเหนียวมะม่วงราคา 60 บาทมีคิวยาว แม่ค้าก็ขึ้นราคา ที่ 80 บาทไม่มีใครแวะ ราคาจึงลดกลับ ที่ 70 บาทขายได้เรื่อย ๆ: นั่นคือมูลค่า และแผงอยู่ใน **สมดุล** เมื่อรถทัวร์มาถึง ราคาเดิมกลายเป็นถูกเกินไปทันที แม่ค้าขึ้นเป็น 90 และยังขายได้มากกว่าที่เคย นั่นคือ **ไม่สมดุล** และ **มูลค่าใหม่**
>
> **จุดที่เปรียบเทียบไม่ได้:** แม่ค้าตั้งราคาคนเดียว แต่ในตลาดจริงผู้ซื้อผู้ขายนับพันขยับราคาไปด้วยกัน และไม่มีใครประกาศว่า "รถทัวร์มาแล้ว" คุณเห็นได้ผ่านราคา เวลา และวอลุ่มเท่านั้น

> [!walkthrough] ไล่ทีละขั้น: ตลาดนัดในภาษาการประมูล
> 1. **18:00 ราคา 60 บาท ขาย 40 กล่อง คิวยาว:** ผู้ซื้ออยากได้มากกว่าที่แม่ค้าอยากขาย → ราคาต้องขึ้นเพื่อหาอีกฝั่ง
> 2. **18:30 ราคา 70 บาท ขาย 120 กล่อง:** ธุรกิจเกิดมากที่สุดตรงนี้ → **มูลค่า**
> 3. **19:00 ราคา 80 บาท ขาย 5 กล่อง:** แทบไม่มีวอลุ่ม → **การปฏิเสธ** ราคากลับไป 70
> 4. **19:30 ราคา 70 บาท ขาย 110 กล่อง:** กลับมาที่มูลค่า ซื้อขายเยอะ → **สมดุล**
> 5. **20:00 ราคา 90 บาท ขาย 150 กล่อง:** ข้อมูลใหม่ (รถทัวร์) ราคาสูงขึ้น **และ** วอลุ่มมากขึ้น → **การยอมรับ** มูลค่าใหม่ = **ไม่สมดุล**
> 6. **แล้วไง?** ราคาอย่างเดียวบอกไม่ได้ว่า 80 หรือ 90 "สูงเกินไป" แต่วอลุ่มและเวลาที่ราคานั้นบอกได้: 80 ถูกปฏิเสธ (5 กล่อง) 90 ถูกยอมรับ (150 กล่อง)

> [!check]- เช็กความเข้าใจ: สมดุล vs ไม่สมดุล
> **Q1.** คู่เงินหนึ่งซื้อขายระหว่าง 1.0850 ถึง 1.0920 มาห้าวัน สมดุลหรือไม่สมดุล? แนวทางพื้นฐานคืออะไร?
> > [!answer]-
> > สมดุล เทรดสวนที่ขอบกลับเข้าหากลาง อย่าไล่การทะลุที่ไม่มีการยอมรับ
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: การทะลุถูกยอมรับไหม? (ภาพประกอบ)
> หุ้นตัวหนึ่งอยู่ในสมดุลระหว่าง **99.6** ถึง **104.9** วอลุ่มเฉลี่ยรายชั่วโมง **10,000** หุ้น
> 1. **กรณี A:** ราคาพุ่งไป **105.6** ด้วย 9,000 หุ้น แล้วแท่งชั่วโมงถัดไปปิดที่ **104.5** กลับเข้ากรอบ วอลุ่มน้อย ไม่มีเวลาอยู่ข้างนอก → **ปฏิเสธ / การประมูลล้มเหลว** แผน: เทรดสวนกลับเข้าหากลาง (102.25) และขอบอีกด้าน (99.6)
> 2. **กรณี B:** ราคาทะลุไป **105.6** และอีกสามชั่วโมงปิดที่ 105.4, 106.0, 106.3 ด้วย **22,000**, **25,000** และ **21,000** หุ้น (2.2–2.5 เท่าของปกติ) มีทั้งเวลา **และ** วอลุ่มข้างนอก → **การยอมรับ** แผน: ซื้อตอนย่อกลับหา 104.9 (ขอบเดิม ตอนนี้เป็นแนวรับ *ดู 2.4*)
> 3. **แล้วไง?** แท่งทะลุแท่งเดียวกันนำไปสู่เทรดที่ตรงข้ามกัน คุณตัดสินใจ **หลัง** เห็นเวลาและวอลุ่ม ไม่ใช่ตอนที่ราคาทะลุครั้งแรก

> [!check]- เช็กความเข้าใจ: การยอมรับ
> **Q1.** ราคาทะลุขึ้นเหนือกรอบด้วยวอลุ่มน้อย แล้วกลับเข้ากรอบภายใน 20 นาที เรียกว่าอะไร และราคามีแนวโน้มไปทางไหน?
> > [!answer]-
> > การประมูลที่ล้มเหลว (การปฏิเสธ) ราคามักวิ่งกลับผ่านกรอบไปหาขอบอีกด้าน
""")
L.before_callout("th", "example", """
> [!check]- เช็กความเข้าใจ: ตอบสนอง vs ริเริ่ม
> **Q1.** มูลค่าอยู่ที่ 100–104 ราคาอยู่ที่ 106 และผู้ซื้อยังยก Ask ขึ้นเรื่อย ๆ เป็นการซื้อแบบตอบสนองหรือริเริ่ม?
> > [!answer]-
> > ริเริ่ม: ซื้อ **เหนือ** มูลค่า เดิมพันว่ามูลค่ากำลังย้ายขึ้น
> **Q2.** ราคาลงไป 99.5 แล้วผู้ซื้อเข้ามาแรง ดันกลับขึ้นไป 101 ตอบสนองหรือริเริ่ม?
> > [!answer]-
> > ตอบสนอง: ซื้อ **ใต้** มูลค่าเพราะถูก คาดว่าจะกลับสู่มูลค่า
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** ฟอเร็กซ์ Spot ไม่มีวอลุ่มกลาง เทรดเดอร์ AMT ใช้วอลุ่มฟิวเจอร์ส (เช่น 6E = ฟิวเจอร์สยูโรบน CME) หรือ Tick volume เป็นแนวทางคร่าว ๆ *(ดู 0.3)*
> - **ทองคำ:** ฟิวเจอร์สทอง (GC) ให้วอลุ่มจริง สมดุลมักเกิดช่วงเอเชียและแตกช่วงลอนดอน/นิวยอร์ก *(ดู 0.4, 5.6)*
> - **หุ้นและดัชนี:** วอลุ่มจริงจากตลาด การประมูลช่วงเปิดและมูลค่าของวันก่อนสำคัญ *(ดู 0.5)*
> - **คริปโต:** วอลุ่มต่างกันตามกระดาน ซื้อขาย 24/7 สมดุลจึงมักเกิดช่วงสุดสัปดาห์และแตกวันจันทร์ *(ดู 0.7)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกตัวแปรสามตัวของ AMT และหน้าที่ของแต่ละตัว
> > [!answer]-
> > ราคาประกาศ (ขยับเพื่อหาอีกฝั่ง) เวลากำกับ (ราคาอยู่นานแค่ไหน = ถูกยอมรับแค่ไหน) วอลุ่มยืนยัน (วอลุ่มสูง = ยอมรับ วอลุ่มต่ำ = ปฏิเสธ)
> **Q2.** ในสมดุล เทรดเดอร์แบบไหนมักชนะ และในไม่สมดุลล่ะ?
> > [!answer]-
> > สมดุล: เทรดเดอร์แบบตอบสนอง (สวนที่ขอบ) ไม่สมดุล: เทรดเดอร์แบบริเริ่ม (ไปกับการวิ่ง)
""")

L.set_meta("level", "v2")
L.save()
