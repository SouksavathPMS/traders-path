"""B9d · v2 upgrade of 4.3 The Trading Plan & If-Then Rules (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("04 Psychology & Execution/4.3 The Trading Plan & If-Then Rules.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> A trading plan is a one-page list of what you trade, when you enter, how much you risk and when you get out, written while you're calm. Then, when the market is moving and your heart is racing, you don't have to think; you just check the list. If the list says no, the answer is no, and that costs you nothing.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Trading plan** — your written rules for markets, setups, entries, risk, exits and routine.
> - **If-then rule (implementation intention)** — "If X happens, then I do Y."
> - **Entry chain** — all conditions that must be true before you enter, joined by AND.
> - **Situation rule** — an if-then rule for a difficult moment (after a loss, a missed entry, news).
> - **Circuit breaker** — a rule that stops or reduces trading automatically *(see 3.6, 4.6)*.
> - **Process goal** — a goal about your actions ("follow the plan"), not about money.
> - **Paper trading** — following the plan without real money.
> - **Chasing** — entering late, after price has already left your planned entry.
""")
L.before_heading("en", "2.", """
> [!analogy]
> A trading plan is like a **pilot's checklist**. Pilots with thousands of hours still read it aloud before take-off, not because they forget how to fly, but because under pressure even experts skip steps. The checklist makes the boring, correct action automatic.
>
> **Where it breaks:** a pilot's checklist rarely changes and the plane's physics never do. Markets change, so your plan needs scheduled reviews, but never changes mid-flight.

> [!check]- Check your understanding: the one-page plan
> **Q1.** Why is "make 1,000 USD this month" a poor goal for your plan? Give a better one.
> > [!answer]-
> > It pushes you to force trades when the market offers none. Better: a process goal you control, e.g. "follow the plan on 95% of trades and journal 100%".
""")
L.before_heading("en", "3.", """
![[p4-chase-cost.en.svg]]

> [!walkthrough] Step by step: why "no chasing beyond 0.5R" is a rule
> The BTC plan from the example: entry **62,000**, stop **61,050** (1R = 950), target **64,400**.
> 1. **Planned entry:** R:R = 2,400 ÷ 950 = **2.53** → break-even win rate 1 ÷ 3.53 ≈ **28%**.
> 2. **Chase by 0.5R** (entry 62,475): risk 1,425, reward 1,925 → R:R **1.35** → break-even win rate **43%**.
> 3. **Chase by 1R** (entry 62,950): risk 1,900, reward 1,450 → R:R **0.76** → break-even **57%**.
> 4. **So what?** The same idea gets much worse with every bit of chasing. Letting a missed trade go costs 0R.

> [!check]- Check your understanding: if-then rules
> **Q1.** Rewrite "I'll be more disciplined after losses" as an if-then rule.
> > [!answer]-
> > For example: "**If** I take a loss, **then** I step away from the screen for 15 minutes and re-read the plan before the next trade."
""")
L.before_callout("en", "example", """
> [!check]- Check your understanding: changing the plan
> **Q1.** After two losing days you want to change your stop rule, your trigger and your timeframe. What does the plan say?
> > [!answer]-
> > Don't change rules mid-week. Write the ideas down; at the weekly review, change **one** rule at a time and measure it over enough trades.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** write which sessions you trade (e.g. 14:00–23:00 UTC+7) and which pairs, or you'll trade whatever moves *(see 0.3)*.
> - **Gold:** add a news rule; US data at 19:30 UTC+7 (20:30 in northern winter) moves gold hard *(see 0.4)*.
> - **Stocks:** add an earnings rule: close or reduce before the report, or accept the gap risk *(see 0.5)*.
> - **Crypto:** 24/7 markets need hours in the plan, or you'll trade at 3 a.m. *(see 0.7)*.

> [!caution]
> Without written stops, size rules and daily limits, a single emotional session can undo months of work. Don't trade real money until the plan exists on paper and you've followed it for at least 30 paper trades.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Write your entry chain in one IF … AND … THEN sentence (use the lesson's as a template).
> > [!answer]-
> > For example: **IF** the HTF is trending **AND** price is in an HTF zone in that direction **AND** the LTF prints a CHoCH in the HTF direction **AND** R:R ≥ 2 **AND** no circuit breaker is active **THEN** size it, place entry + stop + target, and journal it.
> **Q2.** Account 12,000 USD, risk 0.5%, stop 950 below entry on BTC. Size?
> > [!answer]-
> > 60 ÷ 950 ≈ **0.063 BTC**.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> แผนการเทรดคือรายการหนึ่งหน้าว่าคุณเทรดอะไร เข้าเมื่อไร เสี่ยงเท่าไร และออกเมื่อไร เขียนตอนที่ใจสงบ แล้วเมื่อตลาดกำลังขยับและใจเต้นแรง คุณไม่ต้องคิด แค่ตรวจตามรายการ ถ้ารายการบอกว่าไม่ คำตอบคือไม่ และนั่นไม่ทำให้คุณเสียอะไรเลย
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **แผนการเทรด (Trading plan)** — กฎที่เขียนไว้เรื่องตลาด Setup จุดเข้า ความเสี่ยง จุดออก และกิจวัตร
> - **กฎถ้า-แล้ว (If-then rule / Implementation intention)** — "ถ้า X เกิดขึ้น แล้วฉันทำ Y"
> - **ห่วงโซ่การเข้า (Entry chain)** — เงื่อนไขทั้งหมดที่ต้องเป็นจริงก่อนเข้า เชื่อมด้วย "และ"
> - **กฎสถานการณ์ (Situation rule)** — กฎถ้า-แล้วสำหรับช่วงเวลายาก (หลังแพ้ พลาดจุดเข้า ข่าว)
> - **เบรกเกอร์ตัดไฟ (Circuit breaker)** — กฎที่หยุดหรือลดการเทรดโดยอัตโนมัติ *(ดู 3.6, 4.6)*
> - **เป้าหมายด้านกระบวนการ (Process goal)** — เป้าหมายเรื่องการกระทำ ("ทำตามแผน") ไม่ใช่เรื่องเงิน
> - **เทรดบนกระดาษ (Paper trading)** — ทำตามแผนโดยไม่ใช้เงินจริง
> - **การไล่ราคา (Chasing)** — เข้าช้า หลังราคาออกจากจุดเข้าที่วางแผนไปแล้ว
""")
L.before_heading("th", "2.", """
> [!analogy]
> แผนการเทรดเหมือน **เช็กลิสต์ของนักบิน** นักบินที่บินมาหลายพันชั่วโมงยังอ่านออกเสียงก่อนขึ้นบิน ไม่ใช่เพราะลืมวิธีบิน แต่เพราะภายใต้แรงกดดัน แม้ผู้เชี่ยวชาญก็ข้ามขั้นตอน เช็กลิสต์ทำให้การกระทำที่น่าเบื่อแต่ถูกต้องกลายเป็นอัตโนมัติ
>
> **จุดที่เปรียบเทียบไม่ได้:** เช็กลิสต์ของนักบินแทบไม่เปลี่ยน และฟิสิกส์ของเครื่องบินไม่เคยเปลี่ยน แต่ตลาดเปลี่ยน แผนของคุณจึงต้องทบทวนตามกำหนด แต่ห้ามเปลี่ยนกลางเที่ยวบิน

> [!check]- เช็กความเข้าใจ: แผนหนึ่งหน้า
> **Q1.** ทำไม "ทำเงิน 1,000 ดอลลาร์เดือนนี้" จึงเป็นเป้าหมายที่ไม่ดีสำหรับแผน? ยกตัวอย่างที่ดีกว่า
> > [!answer]-
> > มันผลักให้คุณฝืนเทรดตอนที่ตลาดไม่มีโอกาส ที่ดีกว่า: เป้าหมายด้านกระบวนการที่คุณควบคุมได้ เช่น "ทำตามแผน 95% ของไม้ และบันทึก 100%"
""")
L.before_heading("th", "3.", """
![[p4-chase-cost.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ทำไม "ห้ามไล่เกิน 0.5R" จึงเป็นกฎ
> แผน BTC จากตัวอย่าง: เข้า **62,000** Stop **61,050** (1R = 950) เป้า **64,400**
> 1. **จุดเข้าตามแผน:** R:R = 2,400 ÷ 950 = **2.53** → อัตราชนะคุ้มทุน 1 ÷ 3.53 ≈ **28%**
> 2. **ไล่ไป 0.5R** (เข้า 62,475): เสี่ยง 1,425 ผลตอบแทน 1,925 → R:R **1.35** → อัตราชนะคุ้มทุน **43%**
> 3. **ไล่ไป 1R** (เข้า 62,950): เสี่ยง 1,900 ผลตอบแทน 1,450 → R:R **0.76** → คุ้มทุน **57%**
> 4. **แล้วไง?** ไอเดียเดียวกันแย่ลงมากทุกครั้งที่ไล่ราคา การปล่อยเทรดที่พลาดไปเสีย 0R

> [!check]- เช็กความเข้าใจ: กฎถ้า-แล้ว
> **Q1.** เขียน "ฉันจะมีวินัยมากขึ้นหลังแพ้" ใหม่เป็นกฎถ้า-แล้ว
> > [!answer]-
> > ตัวอย่าง: "**ถ้า** ฉันแพ้ **แล้ว** ฉันจะลุกจากหน้าจอ 15 นาที และอ่านแผนซ้ำก่อนเทรดไม้ถัดไป"
""")
L.before_callout("th", "example", """
> [!check]- เช็กความเข้าใจ: การเปลี่ยนแผน
> **Q1.** หลังแพ้สองวัน คุณอยากเปลี่ยนกฎ Stop สัญญาณเข้า และไทม์เฟรม แผนบอกว่าอะไร?
> > [!answer]-
> > ห้ามเปลี่ยนกฎกลางสัปดาห์ จดไอเดียไว้ ในการทบทวนรายสัปดาห์ให้เปลี่ยน **ทีละหนึ่ง** กฎ แล้ววัดผลในจำนวนไม้ที่มากพอ
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** เขียนว่าเทรดช่วงไหน (เช่น 14:00–23:00 UTC+7) และคู่เงินไหน ไม่อย่างนั้นคุณจะเทรดทุกอย่างที่ขยับ *(ดู 0.3)*
> - **ทองคำ:** เพิ่มกฎเรื่องข่าว ข้อมูลสหรัฐ 19:30 UTC+7 (20:30 ช่วงฤดูหนาวซีกโลกเหนือ) ขยับทองแรง *(ดู 0.4)*
> - **หุ้น:** เพิ่มกฎเรื่องงบการเงิน: ปิดหรือลดก่อนประกาศ หรือยอมรับความเสี่ยง Gap *(ดู 0.5)*
> - **คริปโต:** ตลาด 24/7 ต้องกำหนดชั่วโมงในแผน ไม่อย่างนั้นคุณจะเทรดตอนตีสาม *(ดู 0.7)*

> [!caution]
> ถ้าไม่มี Stop กฎขนาด และขีดจำกัดรายวันที่เขียนไว้ เซสชันที่ใช้อารมณ์เพียงครั้งเดียวก็ลบงานหลายเดือนได้ อย่าเทรดเงินจริงจนกว่าแผนจะอยู่บนกระดาษ และคุณทำตามมันอย่างน้อย 30 ไม้บนกระดาษ
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** เขียนห่วงโซ่การเข้าของคุณเป็นประโยค ถ้า … และ … แล้ว ประโยคเดียว (ใช้ของบทเรียนเป็นแม่แบบ)
> > [!answer]-
> > ตัวอย่าง: **ถ้า** HTF เป็นเทรนด์ **และ** ราคาอยู่ในโซน HTF ในทิศทางนั้น **และ** LTF เกิด CHoCH ในทิศทาง HTF **และ** R:R ≥ 2 **และ** ไม่มีเบรกเกอร์ทำงาน **แล้ว** คำนวณขนาด วางจุดเข้า + Stop + เป้า และบันทึก
> **Q2.** บัญชี 12,000 ดอลลาร์ เสี่ยง 0.5% Stop ห่างจากจุดเข้า 950 ใน BTC ขนาดเท่าไร?
> > [!answer]-
> > 60 ÷ 950 ≈ **0.063 BTC**
""")

L.set_meta("level", "v2")
L.save()
