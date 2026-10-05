"""B9e · v2 upgrade of 11.1 Write Your Trading Plan (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("11 Capstone/11.1 Write Your Trading Plan.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> This lesson turns the whole course into one page of rules: what you trade, when, how you enter, how much you risk and when you stop. Then you test those rules step by step, first on old charts, then without money, then with tiny money, before you trade normal size. You only move up a step when the rules have earned it.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Trading plan** — your written rules, version-numbered (v1.0, v1.1 …).
> - **Required core / optional module** — the phases every plan needs / extra tools added one at a time.
> - **Setup** — a specific location + trigger + filters, written as an IF … AND … THEN rule *(see 4.3)*.
> - **Backtest** — testing the setup on past charts *(see 9.3)*.
> - **Paper trading** — following the plan in real time without money.
> - **Micro live** — real money at very small risk (e.g. 0.25%).
> - **Gate** — the condition you must meet before moving to the next stage.
> - **Expectancy** — the average R per trade *(see 3.4)*.
> - **95% range** — where a measured result usually lands, given the sample size.
""")
L.before_heading("en", "2.", """
> [!analogy]
> A trading plan is like a **recipe card** in a restaurant kitchen. Any trained cook should be able to make the same dish from it: exact amounts, exact steps, exact times. "Add some salt until it tastes right" is not a recipe.
>
> **Where it breaks:** ingredients behave the same every day; markets don't. That's why the plan also needs the testing stages and a review schedule.

> [!check]- Check your understanding: choosing the system
> **Q1.** Which phases are required in every plan, and how should you add an optional module?
> > [!answer]-
> > Required: structure (2), risk (3), psychology & execution (4), measurement (9). Add one optional module at a time and keep it only if your journal shows it improves expectancy.
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: turning section 6 into exact numbers
> Account **8,000 USD**, risk **0.5%**, EUR/USD stop **18 pips**, costs about **1 pip** per trade, 10 USD per pip per lot.
> 1. **1R** = 8,000 × 0.005 = **40 USD**.
> 2. **Size** = 1R ÷ (stop + costs) = 40 ÷ (19 × 10) = 0.21 → **0.21 lot** (risk ≈ 39.90 USD).
> 3. **Max open risk 1.5%** = **120 USD** = 3R: at most three such trades open at once.
> 4. **So what?** "Small size" isn't a rule; "0.5% risk, size = 1R ÷ (stop + costs), max 3R open" is. Every blank in the template should end up as a number like this.

> [!check]- Check your understanding: the template
> **Q1.** Is "trade with the trend and use good risk management" an acceptable section 3/6? Rewrite it.
> > [!answer]-
> > No, it's too vague. For example: "Bias: daily HH + HL = longs only; range = no trades. Risk: 0.5% per trade, max 1.5% open, size = 1R ÷ (stop + costs)."
""")
L.before_callout("en", "example", """
![[p11-expectancy-ci.en.svg]]

> [!walkthrough] Step by step: why the gates use 50+ trades, and why that's still not proof
> A system with true expectancy **+0.35R** (45% wins at +2R). Each trade's result varies by about **1.49R**, so the measured average after n trades usually lands within ±1.96 × 1.49 ÷ √n:
> 1. **30 trades:** ±**0.53R** → anywhere from about −0.18R to +0.88R.
> 2. **50 trades:** ±**0.41R**. **100 trades:** ±**0.29R**.
> 3. **200 trades:** ±**0.21R**. **400 trades:** ±**0.15R**.
> 4. **So what?** 50 trades is the minimum to decide whether to continue, not proof of an edge. That's why the stages add up: backtest + paper + micro live together give 130+ trades before normal size.

> [!check]- Check your understanding: the stages
> **Q1.** You're in micro live at 0.25%. After 50 trades, expectancy is −0.15R and you broke circuit breakers twice. What does the plan say?
> > [!answer]-
> > Step back a stage (to paper trading): negative expectancy over 50 trades and repeated circuit-breaker violations are both step-back triggers.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** pick at most 1–2 pairs and fixed hours (e.g. the London–New York overlap) in section 2 *(see 0.3)*.
> - **Gold:** write a specific rule for US data releases in section 8 *(see 0.4, 10.3)*.
> - **Stocks / index futures:** add earnings and opening-auction rules if you trade single stocks or the open *(see 0.5)*.
> - **Crypto:** set trading hours; a 24/7 market without hours leads to overtrading *(see 0.7)*.

> [!caution]
> Going straight to normal size with an untested plan is how many new traders lose a large part of their account in the first months. Follow the stages: backtest, paper, micro live at 0.25%, then 0.5–1% only after passing each gate.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Name the four stages from plan to live money and one gate for each.
> > [!answer]-
> > Backtest (50+ occurrences), paper trade (30+ real-time trades with the full routine), micro live at 0.25% (50+ trades), normal size 0.5–1% (only after the plan has held up and you follow it reliably).
> **Q2.** Account 20,000 USD, risk 0.5%, gold stop 6 USD per oz plus 0.4 USD costs, 1 lot = 100 oz. Size?
> > [!answer]-
> > 1R = **100 USD**. 100 ÷ (6.4 × 100) = 0.156 → **0.15 lot** (risk 96 USD).
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> บทนี้เปลี่ยนทั้งหลักสูตรให้เป็นกฎหนึ่งหน้า: เทรดอะไร เมื่อไร เข้าอย่างไร เสี่ยงเท่าไร และหยุดเมื่อไร แล้วทดสอบกฎทีละขั้น ครั้งแรกบนกราฟในอดีต แล้วไม่ใช้เงิน แล้วใช้เงินน้อยมาก ก่อนจะเทรดขนาดปกติ คุณขึ้นขั้นถัดไปได้ก็ต่อเมื่อกฎพิสูจน์ตัวเองแล้ว
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **แผนการเทรด (Trading plan)** — กฎที่เขียนไว้ มีเลขเวอร์ชัน (v1.0, v1.1 …)
> - **แกนบังคับ / โมดูลเสริม (Required core / Optional module)** — เฟสที่ทุกแผนต้องมี / เครื่องมือเพิ่มเติมที่เพิ่มทีละอย่าง
> - **Setup** — ตำแหน่ง + สัญญาณเข้า + ตัวกรองที่เจาะจง เขียนเป็นกฎ ถ้า … และ … แล้ว *(ดู 4.3)*
> - **แบ็กเทสต์ (Backtest)** — ทดสอบ Setup บนกราฟในอดีต *(ดู 9.3)*
> - **เทรดบนกระดาษ (Paper trading)** — ทำตามแผนแบบเรียลไทม์โดยไม่ใช้เงิน
> - **เงินจริงขนาดจิ๋ว (Micro live)** — เงินจริงที่ความเสี่ยงน้อยมาก (เช่น 0.25%)
> - **ด่าน (Gate)** — เงื่อนไขที่ต้องผ่านก่อนไปขั้นถัดไป
> - **ค่าคาดหวัง (Expectancy)** — R เฉลี่ยต่อไม้ *(ดู 3.4)*
> - **ช่วง 95% (95% range)** — ช่วงที่ผลที่วัดได้มักตกอยู่ ตามขนาดตัวอย่าง
""")
L.before_heading("th", "2.", """
> [!analogy]
> แผนการเทรดเหมือน **การ์ดสูตรอาหาร** ในครัวร้านอาหาร พ่อครัวที่ผ่านการฝึกคนไหนก็ทำจานเดียวกันได้จากการ์ดนี้: ปริมาณที่แน่นอน ขั้นตอนที่แน่นอน เวลาที่แน่นอน "ใส่เกลือนิดหน่อยจนรสชาติพอดี" ไม่ใช่สูตร
>
> **จุดที่เปรียบเทียบไม่ได้:** วัตถุดิบมีพฤติกรรมเหมือนเดิมทุกวัน แต่ตลาดไม่ใช่ แผนจึงต้องมีขั้นตอนการทดสอบและกำหนดการทบทวนด้วย

> [!check]- เช็กความเข้าใจ: เลือกระบบ
> **Q1.** เฟสไหนบังคับในทุกแผน และควรเพิ่มโมดูลเสริมอย่างไร?
> > [!answer]-
> > บังคับ: โครงสร้าง (2) ความเสี่ยง (3) จิตวิทยาและการปฏิบัติ (4) การวัดผล (9) เพิ่มโมดูลเสริมทีละหนึ่ง และเก็บไว้เฉพาะเมื่อบันทึกแสดงว่ามันเพิ่มค่าคาดหวัง
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: เปลี่ยนส่วนที่ 6 ให้เป็นตัวเลขที่แน่นอน
> บัญชี **8,000 ดอลลาร์** เสี่ยง **0.5%** Stop EUR/USD **18 pip** ต้นทุนราว **1 pip** ต่อไม้ 10 ดอลลาร์ต่อ pip ต่อล็อต
> 1. **1R** = 8,000 × 0.005 = **40 ดอลลาร์**
> 2. **ขนาด** = 1R ÷ (Stop + ต้นทุน) = 40 ÷ (19 × 10) = 0.21 → **0.21 ล็อต** (เสี่ยง ≈ 39.90 ดอลลาร์)
> 3. **ความเสี่ยงที่เปิดอยู่สูงสุด 1.5%** = **120 ดอลลาร์** = 3R: เปิดไม้แบบนี้พร้อมกันได้มากที่สุดสามไม้
> 4. **แล้วไง?** "ขนาดเล็ก" ไม่ใช่กฎ "เสี่ยง 0.5% ขนาด = 1R ÷ (Stop + ต้นทุน) เปิดได้สูงสุด 3R" คือกฎ ทุกช่องว่างในแม่แบบควรจบด้วยตัวเลขแบบนี้

> [!check]- เช็กความเข้าใจ: แม่แบบ
> **Q1.** "เทรดตามเทรนด์และบริหารความเสี่ยงให้ดี" ใช้เป็นส่วนที่ 3/6 ได้ไหม? เขียนใหม่
> > [!answer]-
> > ไม่ได้ คลุมเครือเกินไป ตัวอย่าง: "ทิศทาง: รายวัน HH + HL = ซื้อเท่านั้น กรอบราคา = ไม่เทรด ความเสี่ยง: 0.5% ต่อไม้ เปิดได้สูงสุด 1.5% ขนาด = 1R ÷ (Stop + ต้นทุน)"
""")
L.before_callout("th", "example", """
![[p11-expectancy-ci.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ทำไมด่านใช้ 50 ไม้ขึ้นไป และทำไมนั่นยังไม่ใช่การพิสูจน์
> ระบบที่ค่าคาดหวังจริง **+0.35R** (ชนะ 45% ที่ +2R) ผลแต่ละไม้แปรผันราว **1.49R** ค่าเฉลี่ยที่วัดได้หลัง n ไม้จึงมักอยู่ในช่วง ±1.96 × 1.49 ÷ √n:
> 1. **30 ไม้:** ±**0.53R** → ตั้งแต่ราว −0.18R ถึง +0.88R
> 2. **50 ไม้:** ±**0.41R** **100 ไม้:** ±**0.29R**
> 3. **200 ไม้:** ±**0.21R** **400 ไม้:** ±**0.15R**
> 4. **แล้วไง?** 50 ไม้คือขั้นต่ำเพื่อตัดสินว่าจะไปต่อไหม ไม่ใช่การพิสูจน์ความได้เปรียบ นี่คือเหตุผลที่ขั้นตอนต่าง ๆ รวมกัน: แบ็กเทสต์ + กระดาษ + เงินจริงขนาดจิ๋ว ให้ 130 ไม้ขึ้นไปก่อนถึงขนาดปกติ

> [!check]- เช็กความเข้าใจ: ขั้นตอน
> **Q1.** คุณอยู่ในขั้นเงินจริงขนาดจิ๋วที่ 0.25% หลัง 50 ไม้ ค่าคาดหวังคือ −0.15R และคุณฝ่าเบรกเกอร์สองครั้ง แผนบอกว่าอะไร?
> > [!answer]-
> > ถอยกลับหนึ่งขั้น (ไปเทรดบนกระดาษ): ค่าคาดหวังติดลบใน 50 ไม้ และการฝ่าเบรกเกอร์ซ้ำ ๆ เป็นตัวกระตุ้นให้ถอยทั้งคู่
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** เลือกไม่เกิน 1–2 คู่ และชั่วโมงที่แน่นอน (เช่น ช่วงลอนดอน–นิวยอร์กซ้อนกัน) ในส่วนที่ 2 *(ดู 0.3)*
> - **ทองคำ:** เขียนกฎเฉพาะสำหรับการประกาศข้อมูลสหรัฐในส่วนที่ 8 *(ดู 0.4, 10.3)*
> - **หุ้น / ฟิวเจอร์สดัชนี:** เพิ่มกฎเรื่องงบการเงินและการประมูลเปิดตลาด ถ้าเทรดหุ้นรายตัวหรือช่วงเปิดตลาด *(ดู 0.5)*
> - **คริปโต:** กำหนดชั่วโมงเทรด ตลาด 24/7 ที่ไม่มีชั่วโมงกำหนดนำไปสู่การเทรดมากเกินไป *(ดู 0.7)*

> [!caution]
> การกระโดดไปขนาดปกติทันทีด้วยแผนที่ยังไม่ทดสอบ คือวิธีที่นักเทรดใหม่จำนวนมากเสียเงินก้อนใหญ่ในเดือนแรก ๆ ทำตามขั้นตอน: แบ็กเทสต์ กระดาษ เงินจริงขนาดจิ๋วที่ 0.25% แล้วค่อย 0.5–1% หลังผ่านแต่ละด่าน
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกสี่ขั้นจากแผนสู่เงินจริง และด่านของแต่ละขั้น
> > [!answer]-
> > แบ็กเทสต์ (50 ครั้งขึ้นไป) เทรดบนกระดาษ (30 ไม้ขึ้นไปแบบเรียลไทม์พร้อมกิจวัตรครบ) เงินจริงขนาดจิ๋วที่ 0.25% (50 ไม้ขึ้นไป) ขนาดปกติ 0.5–1% (หลังแผนยืนได้และคุณทำตามอย่างสม่ำเสมอเท่านั้น)
> **Q2.** บัญชี 20,000 ดอลลาร์ เสี่ยง 0.5% Stop ทองคำ 6 ดอลลาร์ต่อออนซ์ บวกต้นทุน 0.4 ดอลลาร์ 1 ล็อต = 100 ออนซ์ ขนาดเท่าไร?
> > [!answer]-
> > 1R = **100 ดอลลาร์** 100 ÷ (6.4 × 100) = 0.156 → **0.15 ล็อต** (เสี่ยง 96 ดอลลาร์)
""")

L.set_meta("level", "v2")
L.save()
