"""B7 · v2 upgrade of 8.7 Reading Options Flow (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("08 Options & Dealer Positioning/8.7 Reading Options Flow.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Options flow is a live list of big option trades as they happen. It's tempting to think "a whale just bought calls, so the stock will go up". But you only see one piece of a trader's plan: the call buyer might also be short the stock, closing an old position, or hedging something else. Flow is like hearing one sentence of someone else's phone call. It can add a little confidence to an idea you already have, but it's never enough on its own.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Options flow** — the stream of executed option trades, often filtered to large or unusual ones.
> - **Print** — one executed trade on the tape.
> - **Premium** — the price paid for an option; total premium = option price × 100 shares per contract × number of contracts.
> - **Aggressor side** — who crossed the spread: filled **at or above the ask** = buyer aggressive; **at or below the bid** = seller aggressive; **mid** = unclear.
> - **Sweep** — one large order split across many exchanges at once to fill fast (urgency).
> - **Block** — one large trade negotiated and printed in one piece (often institutional).
> - **Volume** — contracts traded today at that strike and expiry.
> - **Open interest (OI)** — contracts still open from previous days at that strike and expiry (updated once a day).
> - **Opening / closing trade** — creates a new position / ends an existing one.
> - **OTM (out of the money)** — a call with strike above the price, or a put below it *(see 8.1)*.
> - **Spread (strategy)** — two or more option legs traded together; one leg alone can look misleading.
> - **Hedge** — a trade that offsets another position's risk.
> - **Unusual options activity (UOA)** — paid services that alert you to large or odd prints.
""")
L.before_heading("en", "2.", """
![[p8-open-close.en.svg]]

> [!walkthrough] Step by step: is this flow opening or closing?
> XYZ 150 calls, 3-week expiry. Yesterday's **open interest: 900**. Today's **volume: 4,000**.
> 1. At most **900** of today's contracts could have closed existing positions (that's all there were).
> 2. So at least 4,000 − 900 = **3,100** contracts must be **new positions** → likely opening.
> 3. **Next morning:** OI is published as **4,600** → OI rose by 3,700 → at least 3,700 contracts were opened overall.
> 4. **Compare:** XYZ 140 puts, volume **2,500**, OI **12,000**: every one of those could be closing old puts. Volume < OI tells you nothing about direction until tomorrow's OI.
> 5. **So what?** Volume greater than open interest is the quickest way to know a print is probably a **new bet**. Closing trades say little about anyone's future view.

> [!check]- Check your understanding: volume vs OI
> **Q1.** A strike has OI 5,000 and today's volume is 1,200. Can you tell whether the trades were opening or closing?
> > [!answer]-
> > Not today. All 1,200 could be closing. Check tomorrow's OI: if it rises, some were opening; if it falls, most were closing.
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: how big is that print really?
> The XYZ 150-call sweep: **4,000 contracts** filled at **4.00**.
> 1. One contract covers **100 shares**, so one contract costs 4.00 × 100 = **400 USD**.
> 2. Total premium = 4,000 × 400 = **1,600,000 USD** ($1.6M).
> 3. **Compare:** a 1-day OTM call bought 300 times at 1.20 = 300 × 120 = **36,000 USD**: a lottery ticket, not a signal.
> 4. **So what?** Always convert prints into premium. Size, side (ask vs bid) and volume vs OI together decide whether a print deserves your attention.

> [!check]- Check your understanding: reading a print
> **Q1.** A $2M put block prints **at the bid**, volume 3,000 vs OI 20,000. Bearish bet?
> > [!answer]-
> > Probably not. At the bid means the seller was aggressive, and volume < OI means it may be closing. Most likely someone sold or closed puts.
""")
L.before_callout("en", "action", """
> [!analogy]
> Options flow is like **footprints in the snow**. You can see that someone big walked here, and roughly which way. You can't see who they were, why they walked, or whether they turned around a few metres later. A trail that matches the map you already have is helpful; following random footprints into the forest is not.
>
> **Where it breaks:** footprints can't be faked cheaply; option prints can be part of a larger trade designed to look different from what it is (hedges, spreads).

> [!market]
> - **Stocks & indices:** US equity and index options have public tape data; this is where flow services operate *(see 0.5, 0.6)*.
> - **Gold:** GC and GLD options have public prints but much less activity *(see 0.4)*.
> - **Forex:** FX options are mostly over the counter; there's no public tape of the real flow *(see 0.3)*.
> - **Crypto:** exchange option trades (e.g. Deribit) are public; big block trades are often hedges by funds *(see 0.7)*.

> [!caution]
> Paid "flow alert" services can cost hundreds of USD a month and make random prints look meaningful. Copying alerts with short-dated OTM options can lose your whole premium in days. Before paying for any service, log free flow observations for a month in your journal and check whether they would have improved your own trades.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Which four things do you check on a print before giving it any weight?
> > [!answer]-
> > Side (at ask vs at bid), size in premium, volume vs open interest (opening?), and context (expiry, part of a spread or hedge, upcoming events).
> **Q2.** Can a single large aggressive call sweep be a reason to buy the stock?
> > [!answer]-
> > No. At most it raises conviction in a setup you already have (structure, levels, trigger). Never trade because of one print.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> Options flow คือรายการสดของการซื้อขายออปชันขนาดใหญ่ที่เกิดขึ้น น่าคิดว่า "วาฬเพิ่งซื้อ Call หุ้นจะขึ้น" แต่คุณเห็นแค่ชิ้นเดียวของแผนเทรดเดอร์: คนซื้อ Call อาจ Short หุ้นอยู่ด้วย กำลังปิดโพซิชันเก่า หรือเฮดจ์อย่างอื่น Flow เหมือนได้ยินประโยคเดียวจากโทรศัพท์ของคนอื่น อาจเพิ่มความมั่นใจนิดหน่อยให้ไอเดียที่คุณมีอยู่แล้ว แต่ไม่เคยพอในตัวเอง
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **Options flow** — กระแสการซื้อขายออปชันที่เกิดขึ้นจริง มักกรองเฉพาะรายการใหญ่หรือผิดปกติ
> - **Print** — การซื้อขายหนึ่งรายการบน Tape
> - **Premium (ค่าพรีเมียม)** — ราคาที่จ่ายเพื่อซื้อออปชัน พรีเมียมรวม = ราคาออปชัน × 100 หุ้นต่อสัญญา × จำนวนสัญญา
> - **ฝั่งที่รุก (Aggressor side)** — ใครข้าม Spread: ได้ราคา **ที่ Ask หรือสูงกว่า** = ผู้ซื้อรุก **ที่ Bid หรือต่ำกว่า** = ผู้ขายรุก **กลาง (Mid)** = ไม่ชัด
> - **Sweep** — คำสั่งใหญ่หนึ่งคำสั่งที่แบ่งไปหลายตลาดพร้อมกันเพื่อให้ได้เร็ว (เร่งด่วน)
> - **Block** — การซื้อขายใหญ่ที่ต่อรองและแสดงเป็นก้อนเดียว (มักเป็นสถาบัน)
> - **วอลุ่ม (Volume)** — จำนวนสัญญาที่ซื้อขายวันนี้ที่ Strike และวันหมดอายุนั้น
> - **Open interest (OI)** — สัญญาที่ยังเปิดอยู่จากวันก่อน ๆ ที่ Strike และวันหมดอายุนั้น (อัปเดตวันละครั้ง)
> - **การเปิด / การปิดโพซิชัน (Opening / Closing trade)** — สร้างโพซิชันใหม่ / จบโพซิชันเดิม
> - **OTM (Out of the money)** — Call ที่ Strike สูงกว่าราคา หรือ Put ที่ต่ำกว่าราคา *(ดู 8.1)*
> - **Spread (กลยุทธ์)** — ออปชันสองขาขึ้นไปที่ซื้อขายพร้อมกัน ขาเดียวอาจดูหลอกตา
> - **เฮดจ์ (Hedge)** — การซื้อขายที่หักล้างความเสี่ยงของโพซิชันอื่น
> - **Unusual options activity (UOA)** — บริการเสียเงินที่แจ้งเตือน Print ใหญ่หรือแปลก
""")
L.before_heading("th", "2.", """
![[p8-open-close.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: Flow นี้เปิดหรือปิดโพซิชัน?
> XYZ Call 150 หมดอายุในสามสัปดาห์ **Open interest เมื่อวาน: 900** **วอลุ่มวันนี้: 4,000**
> 1. สัญญาวันนี้ปิดโพซิชันเดิมได้มากที่สุด **900** สัญญา (มีอยู่แค่นั้น)
> 2. ดังนั้นอย่างน้อย 4,000 − 900 = **3,100** สัญญาต้องเป็น **โพซิชันใหม่** → น่าจะเป็นการเปิด
> 3. **เช้าวันถัดไป:** OI ประกาศเป็น **4,600** → OI เพิ่ม 3,700 → อย่างน้อย 3,700 สัญญาถูกเปิดโดยรวม
> 4. **เปรียบเทียบ:** XYZ Put 140 วอลุ่ม **2,500** OI **12,000**: ทุกสัญญาอาจเป็นการปิด Put เดิม วอลุ่ม < OI ไม่บอกทิศทางอะไรจนกว่าจะเห็น OI พรุ่งนี้
> 5. **แล้วไง?** วอลุ่มมากกว่า Open interest คือวิธีที่เร็วที่สุดที่จะรู้ว่า Print นั้นน่าจะเป็น **การเดิมพันใหม่** การปิดโพซิชันแทบไม่บอกอะไรเกี่ยวกับมุมมองในอนาคตของใคร

> [!check]- เช็กความเข้าใจ: วอลุ่ม vs OI
> **Q1.** Strike หนึ่งมี OI 5,000 วอลุ่มวันนี้ 1,200 บอกได้ไหมว่าเป็นการเปิดหรือปิด?
> > [!answer]-
> > วันนี้ยังบอกไม่ได้ ทั้ง 1,200 อาจเป็นการปิด ดู OI พรุ่งนี้: ถ้าเพิ่ม มีการเปิดบางส่วน ถ้าลด ส่วนใหญ่เป็นการปิด
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: Print นั้นใหญ่จริงแค่ไหน?
> Sweep ของ XYZ Call 150: **4,000 สัญญา** ได้ราคา **4.00**
> 1. หนึ่งสัญญาครอบคลุม **100 หุ้น** หนึ่งสัญญาจึงราคา 4.00 × 100 = **400 ดอลลาร์**
> 2. พรีเมียมรวม = 4,000 × 400 = **1,600,000 ดอลลาร์** (1.6 ล้าน)
> 3. **เปรียบเทียบ:** Call OTM หมดอายุ 1 วัน ซื้อ 300 สัญญาที่ 1.20 = 300 × 120 = **36,000 ดอลลาร์**: ล็อตเตอรี่ ไม่ใช่สัญญาณ
> 4. **แล้วไง?** แปลง Print เป็นพรีเมียมเสมอ ขนาด ฝั่ง (Ask vs Bid) และวอลุ่ม vs OI รวมกันตัดสินว่า Print นั้นควรได้รับความสนใจไหม

> [!check]- เช็กความเข้าใจ: อ่าน Print
> **Q1.** Put block มูลค่า 2 ล้านดอลลาร์แสดง **ที่ Bid** วอลุ่ม 3,000 เทียบ OI 20,000 เป็นการเดิมพันขาลงไหม?
> > [!answer]-
> > น่าจะไม่ใช่ ที่ Bid แปลว่าผู้ขายรุก และวอลุ่ม < OI แปลว่าอาจเป็นการปิด น่าจะเป็นคนขายหรือปิด Put มากกว่า
""")
L.before_callout("th", "action", """
> [!analogy]
> Options flow เหมือน **รอยเท้าบนหิมะ** คุณเห็นว่ามีคนตัวใหญ่เดินผ่านตรงนี้ และไปทางไหนคร่าว ๆ แต่ไม่เห็นว่าเป็นใคร เดินทำไม หรือหันกลับในอีกไม่กี่เมตรหรือเปล่า รอยที่ตรงกับแผนที่ที่คุณมีอยู่แล้วช่วยได้ แต่การเดินตามรอยเท้าสุ่ม ๆ เข้าป่าไม่ช่วย
>
> **จุดที่เปรียบเทียบไม่ได้:** รอยเท้าปลอมยาก แต่ Print ของออปชันอาจเป็นส่วนหนึ่งของการซื้อขายที่ใหญ่กว่า ซึ่งออกแบบมาให้ดูต่างจากความจริง (เฮดจ์ Spread)

> [!market]
> - **หุ้นและดัชนี:** ออปชันหุ้นและดัชนีสหรัฐมีข้อมูล Tape สาธารณะ เป็นที่ที่บริการ Flow ทำงาน *(ดู 0.5, 0.6)*
> - **ทองคำ:** ออปชัน GC และ GLD มี Print สาธารณะ แต่ซื้อขายน้อยกว่ามาก *(ดู 0.4)*
> - **ฟอเร็กซ์:** ออปชัน FX ส่วนใหญ่ซื้อขายนอกตลาด ไม่มี Tape สาธารณะของ Flow จริง *(ดู 0.3)*
> - **คริปโต:** การซื้อขายออปชันบนกระดาน (เช่น Deribit) เปิดเผย Block ใหญ่มักเป็นการเฮดจ์ของกองทุน *(ดู 0.7)*

> [!caution]
> บริการ "แจ้งเตือน Flow" แบบเสียเงินอาจแพงหลายร้อยดอลลาร์ต่อเดือน และทำให้ Print สุ่ม ๆ ดูมีความหมาย การลอกการแจ้งเตือนด้วยออปชัน OTM อายุสั้นอาจเสียพรีเมียมทั้งหมดในไม่กี่วัน ก่อนจ่ายเงินให้บริการใด ๆ ให้บันทึกการสังเกต Flow ฟรีในบันทึกการเทรดหนึ่งเดือน แล้วเช็กว่ามันจะช่วยไม้ของคุณเองหรือไม่
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** คุณตรวจสี่อย่างไหนใน Print ก่อนให้น้ำหนักกับมัน?
> > [!answer]-
> > ฝั่ง (ที่ Ask vs ที่ Bid) ขนาดเป็นพรีเมียม วอลุ่ม vs Open interest (เปิดใหม่ไหม?) และบริบท (วันหมดอายุ เป็นส่วนของ Spread หรือเฮดจ์ไหม เหตุการณ์ที่จะมาถึง)
> **Q2.** Call sweep เชิงรุกขนาดใหญ่หนึ่งรายการเป็นเหตุผลให้ซื้อหุ้นได้ไหม?
> > [!answer]-
> > ไม่ได้ อย่างมากแค่เพิ่มความมั่นใจใน Setup ที่คุณมีอยู่แล้ว (โครงสร้าง ระดับ สัญญาณ) อย่าเทรดเพราะ Print เดียว
""")

L.set_meta("level", "v2")
L.save()
