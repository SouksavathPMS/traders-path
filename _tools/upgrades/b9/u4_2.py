"""B9d · v2 upgrade of 4.2 Cognitive Biases That Cost Money (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("04 Psychology & Execution/4.2 Cognitive Biases That Cost Money.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Your brain takes shortcuts to decide quickly. In daily life they help; in trading they quietly cost money. For example, a loss hurts more than an equal win feels good, so people hold losers and sell winners too soon. Knowing this isn't enough to stop it. What works is writing rules and checklists that catch the shortcut before you click.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Cognitive bias** — a systematic error in thinking caused by mental shortcuts.
> - **Loss aversion** — losses feel roughly twice as strong as equal gains.
> - **Confirmation bias** — looking for evidence that agrees with what you already believe.
> - **Recency bias** — giving too much weight to the last few results.
> - **Overconfidence** — overrating your skill, especially after wins.
> - **Anchoring** — fixing on a reference number, such as an old price or your entry.
> - **Sunk cost** — letting money already lost drive the next decision.
> - **Disposition effect** — selling winners too early and holding losers too long.
> - **Pre-mortem** — imagining a trade has already failed and asking why.
""")
L.before_heading("en", "2.", """
> [!analogy]
> Biases are like **optical illusions**. Even after someone measures the two lines and shows you they're the same length, your eyes still see one as longer. Knowledge doesn't change the perception; only a ruler (a rule, a checklist, your statistics) gives the right answer.
>
> **Where it breaks:** an illusion looks the same every time. Biases get stronger with money at stake, time pressure and tiredness, so the "ruler" matters most exactly when you least want to use it.

![[p4-sample-luck.en.svg]]

> [!walkthrough] Step by step: why recency bias fools you
> A real edge: 45% wins at +2R, losses −1R → **+0.35R** per trade. How often does a stretch of trades still end below 0R? (exact maths)
> 1. **10 trades:** **26.6%**: about 1 in 4 stretches lose money.
> 2. **20 trades:** **13.0%**. **50 trades:** **4.3%**.
> 3. **100 trades:** **1.0%**. **200 trades:** under 0.1%.
> 4. **So what?** Dropping a system after a bad 10 trades means throwing away good systems about a quarter of the time. Judge on 100+ trades.

> [!check]- Check your understanding: the six biases
> **Q1.** "It was 120 last month, so 95 is cheap." Which bias, and what rule catches it?
> > [!answer]-
> > **Anchoring.** Decide on structure and current levels, not on old prices or your entry.
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: checking the disposition table
> 1. **As planned:** 0.45 × 2.0 − 0.55 × 1.0 = 0.90 − 0.55 = **+0.35R**.
> 2. **As traded:** 0.55 × 0.8 − 0.45 × 1.6 = 0.44 − 0.72 = **−0.28R**.
> 3. Over 100 trades at 1R = 100 USD: **+3,500 USD** as planned vs **−2,800 USD** as traded, with the higher win rate in the losing version.
> 4. **So what?** A rising win rate can hide a falling account. Watch average win and average loss in R, not just how often you win.

> [!check]- Check your understanding: disposition effect
> **Q1.** Your journal shows a 62% win rate, average win +0.7R and average loss −1.4R. What's happening?
> > [!answer]-
> > Expectancy = 0.62 × 0.7 − 0.38 × 1.4 = 0.434 − 0.532 ≈ **−0.10R**. Classic disposition effect: winners cut, losers held.
""")
L.before_callout("en", "example", """
> [!check]- Check your understanding: debiasing
> **Q1.** What is a pre-mortem, and what do you do if the answer is obvious?
> > [!answer]-
> > Before entry, imagine the trade has already lost and ask why. If the most likely reason is obvious (e.g. "against the HTF trend"), don't take the trade.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** anchoring to round numbers and to "where it was last week" is common; trade structure *(see 0.3)*.
> - **Gold:** strong stories ("gold always goes up in a crisis") feed confirmation bias *(see 0.4)*.
> - **Stocks:** anchoring to your purchase price makes many investors hold falling stocks for years *(see 0.5)*.
> - **Crypto:** social feeds deliver endless confirming opinions; recency bias is extreme after big runs *(see 0.7)*.

> [!caution]
> Holding a loser because "I can't sell at a loss" (sunk cost, anchoring) can turn −1R into −5R or worse. Averaging down into a losing trade multiplies the damage. Take the planned stop.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Why doesn't knowing about a bias protect you from it?
> > [!answer]-
> > Biases work fast and automatically; careful reasoning is slow. Under pressure the fast system wins, so you need external rules, checklists and statistics.
> **Q2.** After 3 wins in a row you want to double your size. Which bias, and what's the rule?
> > [!answer]-
> > **Overconfidence** (helped by recency). The rule: fixed risk % per trade; a win streak earns nothing.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> สมองใช้ทางลัดเพื่อตัดสินใจให้เร็ว ในชีวิตประจำวันมันช่วยได้ แต่ในการเทรดมันทำให้เสียเงินอย่างเงียบ ๆ เช่น การขาดทุนเจ็บกว่าความดีใจจากกำไรเท่ากัน คนจึงถือไม้ขาดทุนและขายไม้กำไรเร็วเกินไป การรู้เรื่องนี้ไม่พอจะหยุดมัน สิ่งที่ได้ผลคือการเขียนกฎและเช็กลิสต์ที่ดักทางลัดไว้ก่อนคุณกดปุ่ม
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **อคติทางความคิด (Cognitive bias)** — ความผิดพลาดในการคิดอย่างเป็นระบบที่เกิดจากทางลัดของสมอง
> - **การเกลียดการขาดทุน (Loss aversion)** — การขาดทุนรู้สึกแรงราวสองเท่าของกำไรที่เท่ากัน
> - **อคติยืนยันความเชื่อ (Confirmation bias)** — มองหาหลักฐานที่เห็นด้วยกับสิ่งที่เชื่ออยู่แล้ว
> - **อคติเหตุการณ์ล่าสุด (Recency bias)** — ให้น้ำหนักผลลัพธ์ไม่กี่ครั้งล่าสุดมากเกินไป
> - **ความมั่นใจเกินเหตุ (Overconfidence)** — ประเมินฝีมือตัวเองสูงเกิน โดยเฉพาะหลังชนะ
> - **การยึดติดตัวเลข (Anchoring)** — ยึดกับตัวเลขอ้างอิง เช่น ราคาเก่าหรือราคาที่เข้า
> - **ต้นทุนจม (Sunk cost)** — ปล่อยให้เงินที่เสียไปแล้วกำหนดการตัดสินใจครั้งถัดไป
> - **Disposition effect** — ขายไม้กำไรเร็วเกินไปและถือไม้ขาดทุนนานเกินไป
> - **Pre-mortem** — จินตนาการว่าเทรดล้มเหลวไปแล้ว แล้วถามว่าเพราะอะไร
""")
L.before_heading("th", "2.", """
> [!analogy]
> อคติเหมือน **ภาพลวงตา** แม้มีคนวัดเส้นสองเส้นให้ดูว่ายาวเท่ากัน ตาคุณก็ยังเห็นเส้นหนึ่งยาวกว่า ความรู้ไม่เปลี่ยนการรับรู้ มีแค่ไม้บรรทัด (กฎ เช็กลิสต์ สถิติของคุณ) ที่ให้คำตอบที่ถูก
>
> **จุดที่เปรียบเทียบไม่ได้:** ภาพลวงตาดูเหมือนเดิมทุกครั้ง แต่อคติแรงขึ้นเมื่อมีเงินเดิมพัน มีแรงกดดันด้านเวลา และเมื่อเหนื่อย "ไม้บรรทัด" จึงสำคัญที่สุดในตอนที่คุณไม่อยากใช้มันที่สุด

![[p4-sample-luck.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ทำไมอคติเหตุการณ์ล่าสุดหลอกคุณ
> ความได้เปรียบจริง: ชนะ 45% ที่ +2R แพ้ −1R → **+0.35R** ต่อไม้ ช่วงของเทรดยังจบต่ำกว่า 0R บ่อยแค่ไหน? (คำนวณแบบแม่นยำ)
> 1. **10 ไม้:** **26.6%**: ราว 1 ใน 4 ช่วงขาดทุน
> 2. **20 ไม้:** **13.0%** **50 ไม้:** **4.3%**
> 3. **100 ไม้:** **1.0%** **200 ไม้:** ต่ำกว่า 0.1%
> 4. **แล้วไง?** การทิ้งระบบหลัง 10 ไม้ที่แย่ เท่ากับทิ้งระบบที่ดีราวหนึ่งในสี่ของเวลา ตัดสินจาก 100 ไม้ขึ้นไป

> [!check]- เช็กความเข้าใจ: อคติ 6 อย่าง
> **Q1.** "เดือนก่อนมันอยู่ที่ 120 ดังนั้น 95 ถือว่าถูก" นี่คืออคติอะไร และกฎไหนดักได้?
> > [!answer]-
> > **การยึดติดตัวเลข (Anchoring)** ตัดสินจากโครงสร้างและระดับราคาปัจจุบัน ไม่ใช่ราคาเก่าหรือราคาที่เข้า
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: ตรวจตาราง Disposition
> 1. **ตามแผน:** 0.45 × 2.0 − 0.55 × 1.0 = 0.90 − 0.55 = **+0.35R**
> 2. **ตามที่เทรดจริง:** 0.55 × 0.8 − 0.45 × 1.6 = 0.44 − 0.72 = **−0.28R**
> 3. ใน 100 ไม้ที่ 1R = 100 ดอลลาร์: ตามแผน **+3,500 ดอลลาร์** vs ตามที่เทรดจริง **−2,800 ดอลลาร์** โดยแบบที่ขาดทุนมีอัตราชนะสูงกว่า
> 4. **แล้วไง?** อัตราชนะที่เพิ่มขึ้นอาจซ่อนบัญชีที่ลดลง ดูกำไรเฉลี่ยและขาดทุนเฉลี่ยในหน่วย R ไม่ใช่แค่ว่าชนะบ่อยแค่ไหน

> [!check]- เช็กความเข้าใจ: Disposition effect
> **Q1.** บันทึกของคุณแสดงอัตราชนะ 62% กำไรเฉลี่ย +0.7R ขาดทุนเฉลี่ย −1.4R เกิดอะไรขึ้น?
> > [!answer]-
> > ค่าคาดหวัง = 0.62 × 0.7 − 0.38 × 1.4 = 0.434 − 0.532 ≈ **−0.10R** Disposition effect แบบคลาสสิก: ตัดไม้กำไร ถือไม้ขาดทุน
""")
L.before_callout("th", "example", """
> [!check]- เช็กความเข้าใจ: การลดอคติ
> **Q1.** Pre-mortem คืออะไร และถ้าคำตอบชัดเจนคุณทำอะไร?
> > [!answer]-
> > ก่อนเข้า ให้จินตนาการว่าเทรดแพ้ไปแล้วและถามว่าเพราะอะไร ถ้าเหตุผลที่น่าจะเป็นที่สุดชัดเจน (เช่น "สวนเทรนด์ HTF") อย่าเข้าเทรดนั้น
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** การยึดติดเลขกลมและ "สัปดาห์ที่แล้วมันอยู่ตรงไหน" พบบ่อย ให้เทรดตามโครงสร้าง *(ดู 0.3)*
> - **ทองคำ:** เรื่องเล่าที่ทรงพลัง ("ทองขึ้นเสมอเมื่อเกิดวิกฤต") หล่อเลี้ยงอคติยืนยันความเชื่อ *(ดู 0.4)*
> - **หุ้น:** การยึดติดราคาที่ซื้อทำให้นักลงทุนจำนวนมากถือหุ้นที่ร่วงอยู่หลายปี *(ดู 0.5)*
> - **คริปโต:** ฟีดโซเชียลป้อนความเห็นที่ยืนยันไม่รู้จบ อคติเหตุการณ์ล่าสุดรุนแรงมากหลังราคาวิ่งแรง *(ดู 0.7)*

> [!caution]
> การถือไม้ขาดทุนเพราะ "ขายขาดทุนไม่ได้" (ต้นทุนจม การยึดติดตัวเลข) เปลี่ยน −1R เป็น −5R หรือแย่กว่า การถัวเฉลี่ยขาลงในไม้ที่ขาดทุนทวีความเสียหาย ออกตาม Stop ที่วางแผนไว้
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** ทำไมการรู้จักอคติไม่ได้ปกป้องคุณจากมัน?
> > [!answer]-
> > อคติทำงานเร็วและอัตโนมัติ การคิดอย่างรอบคอบช้า ภายใต้แรงกดดันระบบที่เร็วชนะ คุณจึงต้องมีกฎ เช็กลิสต์ และสถิติจากภายนอก
> **Q2.** หลังชนะ 3 ไม้ติด คุณอยากเพิ่มขนาดเป็นสองเท่า นี่คืออคติอะไร และกฎคืออะไร?
> > [!answer]-
> > **ความมั่นใจเกินเหตุ** (มีอคติเหตุการณ์ล่าสุดช่วย) กฎ: % ความเสี่ยงต่อไม้คงที่ การชนะติดกันไม่ได้ให้สิทธิ์อะไรเพิ่ม
""")

L.set_meta("level", "v2")
L.save()
