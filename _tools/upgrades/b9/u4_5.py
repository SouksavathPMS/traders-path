"""B9d · v2 upgrade of 4.5 Journaling & The Review Loop (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("04 Psychology & Execution/4.5 Journaling & The Review Loop.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> A trading journal is a notebook where you write down every trade: the plan, the result, whether you followed your rules and how you felt. Once a week you read it back and look for patterns. Memory lies and forgets; the journal doesn't. It's the only reliable way to find out what's really helping and what's really costing you money.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Trading journal** — a record of every trade's plan, result, execution and emotions.
> - **R-multiple** — the trade result in units of risk *(see 3.3)*.
> - **Execution grade (A/B/C)** — A = followed the plan, B = small deviation, C = broke a rule.
> - **Tag** — a short label for a pattern, such as `chased` or `moved-stop`.
> - **Review loop** — plan → trade → journal → review → adjust → plan.
> - **Expectancy per setup** — the average R of one setup type *(see 3.4)*.
> - **Deliberate practice** — working on one weakness at a time with feedback.
> - **Leak** — a repeated behaviour that quietly loses R.
""")
L.before_heading("en", "2.", """
> [!analogy]
> Journaling is like a **football team watching the match video**. In the moment, every player remembers a different game. On video, everyone can see who lost the ball and why. The team then trains on one problem for the next week.
>
> **Where it breaks:** a match video shows everything. Your journal only shows what you record, so leaving out the embarrassing trades makes the video useless.

> [!check]- Check your understanding: grading
> **Q1.** A random trade with no setup made +3R. A planned trade hit its stop. Grade both.
> > [!answer]-
> > Random +3R = **C** (broke the plan). Planned stop-out = **A** (followed the plan). Grade execution, not outcome.
""")
L.before_callout("en", "example", """
> [!walkthrough] Step by step: expectancy per setup in a monthly review
> Two setups in a month (illustrative):
> 1. **Setup 1:** 24 trades, 10 wins averaging **+2.2R**, 14 losses at **−1R** → (22 − 14) ÷ 24 = **+0.33R** per trade.
> 2. **Setup 2:** 16 trades, 7 wins averaging **+1.4R**, 9 losses at **−1R** → (9.8 − 9) ÷ 16 = **+0.05R** per trade.
> 3. Setup 2 barely covers costs; with spreads it's probably negative.
> 4. **So what?** Total R hides which setup is doing the work. Split by setup and keep collecting data; with only 16 trades, decide to reduce or adjust Setup 2 rather than declare a final verdict.

> [!check]- Check your understanding: the review loop
> **Q1.** Your weekly review suggests three changes. How many do you make next week, and why?
> > [!answer]-
> > **One.** If you change several things at once, you can't tell which one helped or hurt.
""")
L.before_callout("en", "action", """
![[p4-grade-split.en.svg]]

> [!walkthrough] Step by step: the A/C split from the example
> 1. **A-grade:** 6 trades = **+3.1R**. **C-grade:** 3 trades = **−3.5R**. Total **−0.4R**.
> 2. Without the C trades the week would be **+3.1R**: the rule-breaking cost **3.5R** in one week.
> 3. At 1R = 50 USD, that's **175 USD** lost to behaviour, not to the market.
> 4. **So what?** This split is the most useful number in your journal: it prices your mistakes and shows whether the system or the trader is the problem.

> [!market]
> - **Forex:** tag the session (Asia / London / New York); many traders find one session loses for them *(see 0.3)*.
> - **Gold:** tag trades near US data; compare their R with quiet-hour trades *(see 0.4)*.
> - **Stocks:** tag earnings-related trades separately; their gap risk changes the stats *(see 0.5)*.
> - **Crypto:** tag weekend trades; thin liquidity often changes results *(see 0.7)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Name the six groups of journal fields.
> > [!answer]-
> > Plan, result, execution, mind, tags, evidence (screenshots).
> **Q2.** A week: A-grade trades +2.4R, C-grade trades −3.0R. What's the total, and what's the conclusion?
> > [!answer]-
> > Total **−0.6R**. The planned trades made money; rule-breaking cost 3.0R. Fix behaviour before changing the system.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> บันทึกการเทรดคือสมุดที่คุณจดทุกเทรด: แผน ผลลัพธ์ ทำตามกฎหรือไม่ และรู้สึกอย่างไร สัปดาห์ละครั้งคุณอ่านย้อนและมองหารูปแบบ ความจำโกหกและลืม แต่บันทึกไม่ลืม มันคือวิธีเดียวที่เชื่อถือได้ในการรู้ว่าอะไรช่วยจริง และอะไรทำให้เสียเงินจริง
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **บันทึกการเทรด (Trading journal)** — บันทึกแผน ผลลัพธ์ การปฏิบัติ และอารมณ์ของทุกเทรด
> - **R-multiple** — ผลของเทรดในหน่วยความเสี่ยง *(ดู 3.3)*
> - **เกรดการปฏิบัติ (A/B/C)** — A = ทำตามแผน B = เบี่ยงเล็กน้อย C = ผิดกฎ
> - **แท็ก (Tag)** — ป้ายสั้น ๆ สำหรับรูปแบบ เช่น `chased` หรือ `moved-stop`
> - **วงจรทบทวน (Review loop)** — แผน → เทรด → บันทึก → ทบทวน → ปรับ → แผน
> - **ค่าคาดหวังต่อ Setup (Expectancy per setup)** — R เฉลี่ยของ Setup แต่ละแบบ *(ดู 3.4)*
> - **การฝึกอย่างตั้งใจ (Deliberate practice)** — แก้จุดอ่อนทีละจุด พร้อมรับผลสะท้อนกลับ
> - **รูรั่ว (Leak)** — พฤติกรรมซ้ำ ๆ ที่ทำให้เสีย R อย่างเงียบ ๆ
""")
L.before_heading("th", "2.", """
> [!analogy]
> การบันทึกเหมือน **ทีมฟุตบอลดูวิดีโอการแข่งขัน** ระหว่างแข่ง ผู้เล่นแต่ละคนจำเกมได้คนละแบบ ในวิดีโอทุกคนเห็นว่าใครเสียบอลและเพราะอะไร แล้วทีมก็ฝึกแก้ปัญหาหนึ่งเรื่องในสัปดาห์ถัดไป
>
> **จุดที่เปรียบเทียบไม่ได้:** วิดีโอการแข่งขันแสดงทุกอย่าง แต่บันทึกของคุณแสดงเฉพาะสิ่งที่คุณจด การไม่จดเทรดที่น่าอายจึงทำให้วิดีโอไร้ประโยชน์

> [!check]- เช็กความเข้าใจ: การให้เกรด
> **Q1.** เทรดสุ่ม ๆ ที่ไม่มี Setup ได้ +3R เทรดที่วางแผนไว้โดน Stop ให้เกรดทั้งสองไม้
> > [!answer]-
> > สุ่มได้ +3R = **C** (ผิดแผน) ตามแผนแล้วโดน Stop = **A** (ทำตามแผน) ให้เกรดการปฏิบัติ ไม่ใช่ผลลัพธ์
""")
L.before_callout("th", "example", """
> [!walkthrough] ไล่ทีละขั้น: ค่าคาดหวังต่อ Setup ในการทบทวนรายเดือน
> Setup สองแบบในหนึ่งเดือน (ตัวอย่าง):
> 1. **Setup 1:** 24 ไม้ ชนะ 10 ไม้เฉลี่ย **+2.2R** แพ้ 14 ไม้ที่ **−1R** → (22 − 14) ÷ 24 = **+0.33R** ต่อไม้
> 2. **Setup 2:** 16 ไม้ ชนะ 7 ไม้เฉลี่ย **+1.4R** แพ้ 9 ไม้ที่ **−1R** → (9.8 − 9) ÷ 16 = **+0.05R** ต่อไม้
> 3. Setup 2 แทบไม่พอค่าต้นทุน หลังหัก Spread น่าจะติดลบ
> 4. **แล้วไง?** R รวมซ่อนว่า Setup ไหนทำงานจริง แยกตาม Setup และเก็บข้อมูลต่อ ด้วยแค่ 16 ไม้ ให้ตัดสินใจลดหรือปรับ Setup 2 แทนการตัดสินขั้นสุดท้าย

> [!check]- เช็กความเข้าใจ: วงจรทบทวน
> **Q1.** การทบทวนรายสัปดาห์เสนอการเปลี่ยนแปลงสามอย่าง สัปดาห์หน้าคุณเปลี่ยนกี่อย่าง และเพราะอะไร?
> > [!answer]-
> > **หนึ่งอย่าง** ถ้าเปลี่ยนหลายอย่างพร้อมกัน คุณจะไม่รู้ว่าอันไหนช่วยหรือทำร้าย
""")
L.before_callout("th", "action", """
![[p4-grade-split.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: แยก A/C จากตัวอย่าง
> 1. **เกรด A:** 6 ไม้ = **+3.1R** **เกรด C:** 3 ไม้ = **−3.5R** รวม **−0.4R**
> 2. ถ้าไม่มีไม้เกรด C สัปดาห์นี้จะได้ **+3.1R**: การผิดกฎมีราคา **3.5R** ในสัปดาห์เดียว
> 3. ที่ 1R = 50 ดอลลาร์ นั่นคือ **175 ดอลลาร์** ที่เสียไปกับพฤติกรรม ไม่ใช่กับตลาด
> 4. **แล้วไง?** การแยกนี้คือตัวเลขที่มีประโยชน์ที่สุดในบันทึก: มันตีราคาความผิดพลาดของคุณ และบอกว่าปัญหาอยู่ที่ระบบหรือที่ตัวนักเทรด

> [!market]
> - **ฟอเร็กซ์:** แท็กเซสชัน (เอเชีย / ลอนดอน / นิวยอร์ก) นักเทรดจำนวนมากพบว่ามีเซสชันหนึ่งที่ตัวเองขาดทุน *(ดู 0.3)*
> - **ทองคำ:** แท็กเทรดที่ใกล้ข้อมูลสหรัฐ เทียบ R กับเทรดในชั่วโมงเงียบ *(ดู 0.4)*
> - **หุ้น:** แท็กเทรดที่เกี่ยวกับงบการเงินแยกไว้ ความเสี่ยง Gap เปลี่ยนสถิติ *(ดู 0.5)*
> - **คริปโต:** แท็กเทรดช่วงสุดสัปดาห์ สภาพคล่องที่บางมักเปลี่ยนผลลัพธ์ *(ดู 0.7)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกกลุ่มข้อมูลในบันทึกทั้งหกกลุ่ม
> > [!answer]-
> > แผน ผลลัพธ์ การปฏิบัติ จิตใจ แท็ก หลักฐาน (ภาพหน้าจอ)
> **Q2.** หนึ่งสัปดาห์: ไม้เกรด A +2.4R ไม้เกรด C −3.0R รวมเท่าไร และสรุปอะไร?
> > [!answer]-
> > รวม **−0.6R** ไม้ตามแผนทำเงิน การผิดกฎเสีย 3.0R แก้พฤติกรรมก่อนเปลี่ยนระบบ
""")

L.set_meta("level", "v2")
L.save()
