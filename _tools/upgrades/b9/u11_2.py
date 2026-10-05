"""B9e · v2 upgrade of 11.2 Write Your Investment Policy (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("11 Capstone/11.2 Write Your Investment Policy.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> An Investment Policy Statement is a short letter from your calm self to your future scared or excited self. It says what your long-term money is for, how it's split, how much you add each month, and exactly what you'll do if markets crash or boom. When the headlines get loud, you follow the letter instead of your feelings.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **IPS (Investment Policy Statement)** — your written rules for long-term investing.
> - **Horizon** — when you'll need the money.
> - **Risk tolerance** — the largest fall you can hold through without selling.
> - **Target allocation / band** — the % you aim for in each asset, and the allowed range (e.g. 50% ± 5).
> - **Rebalancing** — trading back to targets on a calendar date or when a band breaks *(see 10.7)*.
> - **Emergency fund** — 3–6 months of expenses in cash, never invested.
> - **Expense ratio** — a fund's yearly fee as a % of your money.
> - **Contribution** — the amount you add regularly, ideally automatically.
> - **Crisis plan** — pre-written actions for falls of 20%, 30% or 50%.
> - **Tax-advantaged fund** — a fund with tax benefits under local rules; the rules and limits change, so check the current ones.
""")
L.before_heading("en", "2.", """
> [!analogy]
> An IPS is like a **fire drill**. You practise the exits on a calm day so that, when the alarm rings, your body follows the plan without thinking. Nobody designs the escape route while the building is full of smoke.
>
> **Where it breaks:** a fire is obvious and over quickly. A market crash can last months and arrive with convincing stories about why "this time is different", so the plan also needs a rule like "wait 72 hours before any unscheduled change".

> [!walkthrough] Step by step: the money before the IPS
> Monthly expenses **25,000 THB**, salary **40,000 THB**.
> 1. **Emergency fund** = 6 × 25,000 = **150,000 THB** in savings, set aside first and never invested.
> 2. **Contribution** of 15% of income = 0.15 × 40,000 = **6,000 THB a month** = **72,000 THB a year**, automated on payday.
> 3. A fund with a **0.2%** fee costs **2 THB a year** per 1,000 THB invested; one with **2.0%** costs **20 THB**. Over decades that gap compounds *(see the fee table in 10.7)*.
> 4. **So what?** The emergency fund protects the IPS: without it, a job loss in a crash forces you to sell at the bottom.

> [!check]- Check your understanding: the eight sections
> **Q1.** Which section answers "what do I do if my portfolio falls 30%?", and why must it be written before a crash?
> > [!answer]-
> > The **crisis plan**. During a crash, fear makes selling feel urgent and right (4.1); a pre-written plan turns the moment into a checklist.
""")
L.before_callout("en", "example", """
> [!check]- Check your understanding: two worlds
> **Q1.** Your trading account lost 25% this year. Can you move money from the IPS portfolio to refill it?
> > [!answer]-
> > No. Never refill the trading account from the IPS after losses, and never raid the IPS to "make back" trading losses. Write this rule into both documents.
""")
L.before_callout("en", "action", """
![[p11-crash-rebalance.en.svg]]

> [!walkthrough] Step by step: the sample IPS in a crash
> **1,000,000 THB** at targets: global equity 50%, Thai equity 15%, bonds 25%, gold 5%, cash 5%. Then equities fall **30%**, bonds rise 3%, gold rises 10% (illustrative).
> 1. New values: equities 350,000 + 105,000; bonds 257,500; gold 55,000; cash 50,000 → total **817,500 THB** (**−18.25%**).
> 2. Weights now: global equity **42.8%** (below its 45–55% band), bonds **31.5%** (above its 20–30% band).
> 3. Rebalance to targets: **buy** 58,750 global + 17,625 Thai equity; **sell** 53,125 bonds, 14,125 gold, 9,125 cash.
> 4. **So what?** The rule makes you buy equities after the fall, exactly when feelings say sell. That's the IPS doing its job.

> [!market]
> - **Forex:** a Thai investor's foreign funds carry USD/THB risk; decide in the IPS whether to hedge or accept it *(see 10.4)*.
> - **Gold:** a small fixed weight (e.g. 5%) acts as a diversifier; rebalancing trims it after rallies *(see 0.4)*.
> - **Stocks:** broad, low-cost index funds form the core; cap any single stock (e.g. 5%) *(see 0.5, 10.7)*.
> - **Crypto:** if included at all, a small capped weight (e.g. ≤ 3%) that you can lose entirely *(see 0.7)*.

> [!caution]
> Selling the core portfolio in a crash, or piling into a hot asset in a boom, can permanently lose years of compounding. Investing money you'll need within a few years, or without an emergency fund, forces sales at the worst moment. Write the crisis plan and the 72-hour rule now.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Name the eight sections of an IPS.
> > [!answer]-
> > Goals & horizon, risk tolerance, target allocation, instruments & costs, contributions, rebalancing rule, crisis plan, review.
> **Q2.** Target: stocks 70% ± 5, bonds 30%. After a rally, the portfolio is 600,000 THB stocks and 200,000 THB bonds. Is a band broken, and what's the rebalance trade?
> > [!answer]-
> > Stocks = 600 ÷ 800 = **75%**, at the top of the band (≤ 75%), so not yet broken. At a calendar rebalance: target stocks 560,000 → **sell 40,000** stocks, buy 40,000 bonds.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> IPS คือจดหมายสั้น ๆ จากตัวคุณที่ใจสงบ ถึงตัวคุณในอนาคตที่กำลังกลัวหรือตื่นเต้น บอกว่าเงินระยะยาวมีไว้ทำอะไร แบ่งอย่างไร เติมเดือนละเท่าไร และจะทำอะไรเมื่อตลาดถล่มหรือร้อนแรง เมื่อพาดหัวข่าวดังขึ้น คุณทำตามจดหมาย ไม่ใช่ตามความรู้สึก
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **IPS (Investment Policy Statement)** — กฎการลงทุนระยะยาวที่เขียนไว้
> - **ระยะเวลา (Horizon)** — คุณจะต้องใช้เงินเมื่อไร
> - **ความทนทานต่อความเสี่ยง (Risk tolerance)** — การร่วงมากที่สุดที่คุณถือผ่านได้โดยไม่ขาย
> - **สัดส่วนเป้าหมาย / กรอบ (Target allocation / Band)** — % ที่ตั้งเป้าในแต่ละสินทรัพย์ และช่วงที่อนุญาต (เช่น 50% ± 5)
> - **การปรับสมดุล (Rebalancing)** — ซื้อขายกลับไปที่เป้าตามวันที่กำหนด หรือเมื่อหลุดกรอบ *(ดู 10.7)*
> - **เงินสำรองฉุกเฉิน (Emergency fund)** — ค่าใช้จ่าย 3–6 เดือนในรูปเงินสด ไม่นำไปลงทุน
> - **อัตราค่าใช้จ่ายกองทุน (Expense ratio)** — ค่าธรรมเนียมรายปีของกองทุนเป็น % ของเงินคุณ
> - **เงินลงทุนสม่ำเสมอ (Contribution)** — จำนวนที่เติมเป็นประจำ ควรเป็นแบบอัตโนมัติ
> - **แผนรับวิกฤต (Crisis plan)** — การกระทำที่เขียนไว้ล่วงหน้าเมื่อตลาดร่วง 20%, 30% หรือ 50%
> - **กองทุนลดหย่อนภาษี (Tax-advantaged fund)** — กองทุนที่มีสิทธิประโยชน์ทางภาษีตามกฎในประเทศ กฎและวงเงินเปลี่ยนได้ จึงต้องตรวจกฎปัจจุบัน
""")
L.before_heading("th", "2.", """
> [!analogy]
> IPS เหมือน **การซ้อมหนีไฟ** คุณซ้อมเส้นทางออกในวันที่สงบ เพื่อให้เมื่อสัญญาณเตือนดัง ร่างกายทำตามแผนโดยไม่ต้องคิด ไม่มีใครออกแบบเส้นทางหนีไฟตอนที่อาคารเต็มไปด้วยควัน
>
> **จุดที่เปรียบเทียบไม่ได้:** ไฟไหม้เห็นชัดและจบเร็ว แต่ตลาดถล่มอาจยาวหลายเดือน และมาพร้อมเรื่องเล่าที่ฟังขึ้นว่า "ครั้งนี้ไม่เหมือนเดิม" แผนจึงต้องมีกฎอย่าง "รอ 72 ชั่วโมงก่อนเปลี่ยนแปลงใด ๆ ที่ไม่ได้อยู่ในกำหนด"

> [!walkthrough] ไล่ทีละขั้น: เงินที่ต้องจัดการก่อน IPS
> ค่าใช้จ่ายต่อเดือน **25,000 บาท** เงินเดือน **40,000 บาท**
> 1. **เงินสำรองฉุกเฉิน** = 6 × 25,000 = **150,000 บาท** ในบัญชีเงินฝาก กันไว้ก่อนและไม่นำไปลงทุน
> 2. **เงินลงทุนสม่ำเสมอ** 15% ของรายได้ = 0.15 × 40,000 = **6,000 บาทต่อเดือน** = **72,000 บาทต่อปี** ตัดอัตโนมัติวันเงินเดือนออก
> 3. กองทุนค่าธรรมเนียม **0.2%** มีค่าใช้จ่าย **2 บาทต่อปี** ต่อเงินลงทุน 1,000 บาท กองทุน **2.0%** มีค่าใช้จ่าย **20 บาท** ในหลายสิบปีส่วนต่างนี้ทบต้น *(ดูตารางค่าธรรมเนียมในบทที่ 10.7)*
> 4. **แล้วไง?** เงินสำรองฉุกเฉินปกป้อง IPS: ถ้าไม่มี การตกงานในช่วงตลาดถล่มจะบังคับให้คุณขายที่ก้น

> [!check]- เช็กความเข้าใจ: แปดส่วน
> **Q1.** ส่วนไหนตอบคำถาม "ถ้าพอร์ตร่วง 30% ฉันจะทำอะไร?" และทำไมต้องเขียนก่อนตลาดถล่ม?
> > [!answer]-
> > **แผนรับวิกฤต** ระหว่างตลาดถล่ม ความกลัวทำให้การขายรู้สึกเร่งด่วนและถูกต้อง (4.1) แผนที่เขียนไว้ล่วงหน้าเปลี่ยนช่วงเวลานั้นให้เป็นเช็กลิสต์
""")
L.before_callout("th", "example", """
> [!check]- เช็กความเข้าใจ: สองโลก
> **Q1.** บัญชีเทรดของคุณขาดทุน 25% ปีนี้ คุณย้ายเงินจากพอร์ต IPS มาเติมได้ไหม?
> > [!answer]-
> > ไม่ได้ ห้ามเติมบัญชีเทรดจาก IPS หลังขาดทุน และห้ามดึงเงิน IPS ไป "เอาคืน" การขาดทุนจากการเทรด เขียนกฎนี้ไว้ในเอกสารทั้งสองฉบับ
""")
L.before_callout("th", "action", """
![[p11-crash-rebalance.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: IPS ตัวอย่างในตลาดถล่ม
> **1,000,000 บาท** ตามเป้า: หุ้นโลก 50% หุ้นไทย 15% พันธบัตร 25% ทองคำ 5% เงินสด 5% แล้วหุ้นร่วง **30%** พันธบัตรขึ้น 3% ทองขึ้น 10% (ตัวอย่าง)
> 1. มูลค่าใหม่: หุ้น 350,000 + 105,000 พันธบัตร 257,500 ทอง 55,000 เงินสด 50,000 → รวม **817,500 บาท** (**−18.25%**)
> 2. น้ำหนักตอนนี้: หุ้นโลก **42.8%** (ต่ำกว่ากรอบ 45–55%) พันธบัตร **31.5%** (สูงกว่ากรอบ 20–30%)
> 3. ปรับสมดุลกลับเป้า: **ซื้อ** หุ้นโลก 58,750 + หุ้นไทย 17,625 **ขาย** พันธบัตร 53,125 ทอง 14,125 เงินสด 9,125
> 4. **แล้วไง?** กฎบังคับให้คุณซื้อหุ้นหลังราคาร่วง ตอนที่ความรู้สึกบอกให้ขาย นั่นคือ IPS กำลังทำหน้าที่

> [!market]
> - **ฟอเร็กซ์:** กองทุนต่างประเทศของนักลงทุนไทยมีความเสี่ยง USD/THB ตัดสินใจใน IPS ว่าจะป้องกันหรือยอมรับมัน *(ดู 10.4)*
> - **ทองคำ:** น้ำหนักคงที่เล็ก ๆ (เช่น 5%) ทำหน้าที่กระจายความเสี่ยง การปรับสมดุลจะตัดลงหลังราคาขึ้น *(ดู 0.4)*
> - **หุ้น:** กองทุนดัชนีกว้าง ต้นทุนต่ำ เป็นแกนหลัก จำกัดหุ้นรายตัวใด ๆ (เช่น 5%) *(ดู 0.5, 10.7)*
> - **คริปโต:** ถ้าจะมี ให้เป็นน้ำหนักเล็กที่มีเพดาน (เช่น ≤ 3%) ที่คุณยอมเสียทั้งหมดได้ *(ดู 0.7)*

> [!caution]
> การขายพอร์ตหลักตอนตลาดถล่ม หรือทุ่มเงินเข้าสินทรัพย์ที่กำลังร้อนแรงตอนตลาดบูม อาจทำให้เสียการทบต้นหลายปีไปอย่างถาวร การลงทุนด้วยเงินที่ต้องใช้ในไม่กี่ปี หรือโดยไม่มีเงินสำรองฉุกเฉิน บังคับให้ขายในจังหวะที่แย่ที่สุด เขียนแผนรับวิกฤตและกฎ 72 ชั่วโมงตอนนี้
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกแปดส่วนของ IPS
> > [!answer]-
> > เป้าหมายและระยะเวลา ความทนทานต่อความเสี่ยง สัดส่วนเป้าหมาย เครื่องมือและต้นทุน เงินลงทุนสม่ำเสมอ กฎการปรับสมดุล แผนรับวิกฤต การทบทวน
> **Q2.** เป้า: หุ้น 70% ± 5 พันธบัตร 30% หลังตลาดขึ้น พอร์ตมีหุ้น 600,000 บาท พันธบัตร 200,000 บาท หลุดกรอบไหม และการปรับสมดุลคืออะไร?
> > [!answer]-
> > หุ้น = 600 ÷ 800 = **75%** อยู่ที่ขอบบนของกรอบ (≤ 75%) จึงยังไม่หลุด เมื่อถึงวันปรับสมดุลตามปฏิทิน: เป้าหุ้น 560,000 → **ขายหุ้น 40,000** ซื้อพันธบัตร 40,000
""")

L.set_meta("level", "v2")
L.save()
