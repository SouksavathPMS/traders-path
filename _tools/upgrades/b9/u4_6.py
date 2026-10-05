"""B9d · v2 upgrade of 4.6 Losing Streaks & Tilt (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("04 Psychology & Execution/4.6 Losing Streaks & Tilt.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> After a few losses, it's normal to feel angry or desperate to win the money back. When those feelings start making your trading decisions, that's called tilt, and it turns small losses into big ones. The fix is simple rules you set in advance, like "after 3 losses I stop for the day", so you don't have to rely on willpower when you're upset.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Tilt** — emotions such as anger, frustration or panic taking over trading decisions.
> - **Green / Amber / Red** — in control / warming up / tilted.
> - **Revenge trade** — a trade taken to win back a loss, usually outside the plan.
> - **Circuit breaker** — a pre-set rule that stops or reduces trading automatically.
> - **Pre-commitment** — deciding your actions in advance, while calm.
> - **Variance** — normal random swings in results, even with a real edge *(see 3.6)*.
> - **Market state** — trend, range, quiet or volatile *(see 2.2)*.
> - **Reset activity** — what you do in a break: walking, exercise, anything away from screens.
""")
L.before_heading("en", "2.", """
> [!analogy]
> Tilt is like a **car engine overheating**. The temperature gauge creeps up long before steam comes out. Pull over when the needle enters the amber zone and the engine is fine. Keep driving because "it's only a little further" and you'll be stuck at the roadside.
>
> **Where it breaks:** a car has a gauge on the dashboard. Your gauge is your list of personal signs, which only works if you've written it down and actually look at it.

> [!check]- Check your understanding: stages of tilt
> **Q1.** You notice you're checking P&L every minute and skipping a checklist item. Which stage, and what's the rule?
> > [!answer]-
> > **Amber.** Pause 15 minutes; the next trade at half size and A-grade only.
""")
L.before_heading("en", "3.", """
![[p4-breaker-savings.en.svg]]

> [!walkthrough] Step by step: what a circuit breaker saves on a bad day
> An illustrative bad day: three normal losses (−1R each), then a sized-up loss (−1.5R), a moved stop (−2R) and two revenge trades (−1R each).
> 1. **Without breakers:** −1 −1 −1 −1.5 −2 −1 −1 = **−8.5R**.
> 2. **With "3 losses → done for the day":** trading stops at **−3R**.
> 3. Saved: **5.5R**, which at 1R = 100 USD is **550 USD** in one day.
> 4. **So what?** The first three losses were normal; everything after them was tilt. The breaker removes exactly the trades that tilt would have taken.

> [!check]- Check your understanding: circuit breakers
> **Q1.** Why are circuit breakers decided "in Green"?
> > [!answer]-
> > Because in Red your judgment is the problem. Rules made while calm, with simple triggers (number of losses, R lost), apply without needing judgment.
""")
L.before_callout("en", "example", """
> [!walkthrough] Step by step: is this streak normal?
> Win rate **40%**, so each trade has a **60%** chance to lose.
> 1. Chance of at least one **6-loss** streak within **50 trades** ≈ **63%**; within **100 trades** ≈ **87%**.
> 2. Chance of at least one **8-loss** streak within 100 trades ≈ **49%** *(see the table in 3.1)*.
> 3. So a 6-loss streak at a 40% win rate is the **expected** case, not a sign the system broke.
> 4. **So what?** Check the numbers first. If the streak is within range and the trades were A-grade, it's variance: reduce size, keep executing.

> [!check]- Check your understanding: getting through a streak
> **Q1.** Your last 7 trades lost, but 5 of them were C-grade. Is the problem the system or you? What do you do?
> > [!answer]-
> > Mostly you: the losses come from breaking rules. Reduce size, trade A-grade only, and work on the specific mistake tags before judging the system.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** 24-hour sessions make it easy to keep trading after a bad day; close the platform when a breaker fires *(see 0.3)*.
> - **Gold:** large intraday swings can trigger several stops quickly; daily limits matter most here *(see 0.4)*.
> - **Stocks:** after a loss, avoid jumping into "hot" names you don't normally trade *(see 0.5)*.
> - **Crypto:** 24/7 trading and high leverage make revenge trading especially costly *(see 0.7)*.

> [!caution]
> Tilt can turn a normal −3R day into −10R or worse within an hour, especially with leverage. Increasing size to win it back is the fastest path to a blown account. When a circuit breaker fires, close the platform.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** List three of your circuit-breaker triggers and their actions.
> > [!answer]-
> > For example: any loss → 15-minute break; −2R or 3 losses today → done for the day; −5R this week → done for the week; −10% from peak → stop live trading and review.
> **Q2.** Both traders in the example lost 5R in week 1. Trader B made +1.5R in week 2 at half size. What's B's two-week total, compared with A's −13R?
> > [!answer]-
> > −5 + 1.5 = **−3.5R**, about 9.5R better than A, with the habits intact.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> หลังแพ้ไม่กี่ไม้ เป็นเรื่องปกติที่จะรู้สึกโกรธหรืออยากเอาเงินคืนอย่างร้อนรน เมื่อความรู้สึกเหล่านั้นเริ่มตัดสินใจเทรดแทนคุณ นั่นเรียกว่า Tilt และมันเปลี่ยนการขาดทุนเล็กให้เป็นการขาดทุนใหญ่ ทางแก้คือกฎง่าย ๆ ที่ตั้งไว้ล่วงหน้า เช่น "แพ้ 3 ไม้แล้วหยุดวันนี้" คุณจะได้ไม่ต้องพึ่งกำลังใจตอนที่กำลังหัวเสีย
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **Tilt** — อารมณ์อย่างความโกรธ ความหงุดหงิด หรือความตื่นตระหนก เข้ามาคุมการตัดสินใจเทรด
> - **เขียว / เหลืองอำพัน / แดง (Green / Amber / Red)** — ควบคุมได้ / เริ่มร้อน / Tilt แล้ว
> - **เทรดแก้แค้น (Revenge trade)** — เทรดเพื่อเอาคืนการขาดทุน มักนอกแผน
> - **เบรกเกอร์ตัดไฟ (Circuit breaker)** — กฎที่ตั้งไว้ล่วงหน้าให้หยุดหรือลดการเทรดโดยอัตโนมัติ
> - **การผูกมัดล่วงหน้า (Pre-commitment)** — ตัดสินใจการกระทำไว้ก่อน ตอนที่ใจสงบ
> - **ความแปรปรวน (Variance)** — การแกว่งแบบสุ่มตามปกติของผลลัพธ์ แม้มีความได้เปรียบจริง *(ดู 3.6)*
> - **สภาวะตลาด (Market state)** — เทรนด์ กรอบราคา เงียบ หรือผันผวน *(ดู 2.2)*
> - **กิจกรรมรีเซ็ต (Reset activity)** — สิ่งที่ทำระหว่างพัก: เดิน ออกกำลังกาย อะไรก็ได้ที่ห่างจากหน้าจอ
""")
L.before_heading("th", "2.", """
> [!analogy]
> Tilt เหมือน **เครื่องยนต์รถที่ร้อนเกินไป** เข็มวัดอุณหภูมิค่อย ๆ ขึ้นนานก่อนจะมีไอน้ำพุ่ง จอดข้างทางตอนเข็มเข้าโซนเหลือง เครื่องก็ยังดี ขับต่อเพราะ "อีกนิดเดียว" แล้วคุณจะติดอยู่ข้างถนน
>
> **จุดที่เปรียบเทียบไม่ได้:** รถมีเข็มวัดบนแผงหน้าปัด แต่เข็มวัดของคุณคือรายการสัญญาณเฉพาะตัว ซึ่งได้ผลก็ต่อเมื่อคุณเขียนไว้และเปิดดูจริง

> [!check]- เช็กความเข้าใจ: ระดับของ Tilt
> **Q1.** คุณสังเกตว่าตัวเองเช็ก P&L ทุกนาที และข้ามรายการในเช็กลิสต์ไปหนึ่งข้อ อยู่ระดับไหน และกฎคืออะไร?
> > [!answer]-
> > **เหลืองอำพัน** พัก 15 นาที ไม้ถัดไปครึ่งขนาด และเกรด A เท่านั้น
""")
L.before_heading("th", "3.", """
![[p4-breaker-savings.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: เบรกเกอร์ตัดไฟช่วยได้เท่าไรในวันแย่ ๆ
> วันแย่ ๆ ตัวอย่าง: แพ้ปกติสามไม้ (ไม้ละ −1R) แล้วแพ้ไม้ที่เพิ่มขนาด (−1.5R) ไม้ที่เลื่อน Stop (−2R) และไม้แก้แค้นสองไม้ (ไม้ละ −1R)
> 1. **ไม่มีเบรกเกอร์:** −1 −1 −1 −1.5 −2 −1 −1 = **−8.5R**
> 2. **มีกฎ "แพ้ 3 ไม้ → จบวัน":** หยุดเทรดที่ **−3R**
> 3. ประหยัด **5.5R** ที่ 1R = 100 ดอลลาร์คือ **550 ดอลลาร์** ในวันเดียว
> 4. **แล้วไง?** สามไม้แรกเป็นการแพ้ปกติ ทุกอย่างหลังจากนั้นคือ Tilt เบรกเกอร์ตัดเฉพาะเทรดที่ Tilt จะเป็นคนเปิด

> [!check]- เช็กความเข้าใจ: เบรกเกอร์ตัดไฟ
> **Q1.** ทำไมเบรกเกอร์ตัดไฟจึงต้องตัดสินใจ "ตอนเขียว"?
> > [!answer]-
> > เพราะตอนแดง วิจารณญาณของคุณคือปัญหา กฎที่ตั้งตอนใจสงบด้วยตัวกระตุ้นง่าย ๆ (จำนวนไม้ที่แพ้ R ที่เสีย) ใช้ได้โดยไม่ต้องใช้วิจารณญาณ
""")
L.before_callout("th", "example", """
> [!walkthrough] ไล่ทีละขั้น: การแพ้ติดกันนี้ปกติไหม?
> อัตราชนะ **40%** แต่ละไม้จึงมีโอกาสแพ้ **60%**
> 1. โอกาสแพ้ติดกัน **6 ไม้** อย่างน้อยหนึ่งครั้งภายใน **50 ไม้** ≈ **63%** ภายใน **100 ไม้** ≈ **87%**
> 2. โอกาสแพ้ติดกัน **8 ไม้** อย่างน้อยหนึ่งครั้งภายใน 100 ไม้ ≈ **49%** *(ดูตารางในบทที่ 3.1)*
> 3. การแพ้ 6 ไม้ติดที่อัตราชนะ 40% จึงเป็นกรณีที่ **คาดได้** ไม่ใช่สัญญาณว่าระบบพัง
> 4. **แล้วไง?** ตรวจตัวเลขก่อน ถ้าการแพ้ติดกันอยู่ในช่วงปกติและไม้เป็นเกรด A นั่นคือความแปรปรวน: ลดขนาด และทำตามแผนต่อ

> [!check]- เช็กความเข้าใจ: ผ่านช่วงแพ้ติดกัน
> **Q1.** 7 ไม้ล่าสุดแพ้หมด แต่ 5 ไม้เป็นเกรด C ปัญหาอยู่ที่ระบบหรือที่คุณ? คุณทำอะไร?
> > [!answer]-
> > ส่วนใหญ่ที่คุณ: การขาดทุนมาจากการผิดกฎ ลดขนาด เทรดเฉพาะเกรด A และแก้แท็กความผิดพลาดที่เจาะจงก่อนตัดสินระบบ
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** ตลาด 24 ชั่วโมงทำให้เทรดต่อหลังวันแย่ได้ง่าย ปิดแพลตฟอร์มเมื่อเบรกเกอร์ทำงาน *(ดู 0.3)*
> - **ทองคำ:** การแกว่งระหว่างวันที่ใหญ่อาจชน Stop หลายไม้อย่างรวดเร็ว ขีดจำกัดรายวันสำคัญที่สุดตรงนี้ *(ดู 0.4)*
> - **หุ้น:** หลังแพ้ อย่ากระโดดเข้าหุ้น "ร้อน ๆ" ที่ปกติไม่ได้เทรด *(ดู 0.5)*
> - **คริปโต:** การซื้อขาย 24/7 และเลเวอเรจสูงทำให้การเทรดแก้แค้นแพงเป็นพิเศษ *(ดู 0.7)*

> [!caution]
> Tilt เปลี่ยนวัน −3R ตามปกติให้เป็น −10R หรือแย่กว่าได้ภายในชั่วโมงเดียว โดยเฉพาะเมื่อใช้เลเวอเรจ การเพิ่มขนาดเพื่อเอาคืนคือทางที่เร็วที่สุดสู่บัญชีพัง เมื่อเบรกเกอร์ทำงาน ปิดแพลตฟอร์ม
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกตัวกระตุ้นเบรกเกอร์สามข้อของคุณ และการกระทำของแต่ละข้อ
> > [!answer]-
> > ตัวอย่าง: แพ้ไม้ใดก็ตาม → พัก 15 นาที −2R หรือแพ้ 3 ไม้วันนี้ → จบวัน −5R สัปดาห์นี้ → จบสัปดาห์ −10% จากจุดสูงสุด → หยุดเทรดจริงและทบทวน
> **Q2.** เทรดเดอร์ทั้งสองในตัวอย่างเสีย 5R ในสัปดาห์แรก เทรดเดอร์ B ได้ +1.5R ในสัปดาห์ที่สองด้วยครึ่งขนาด สองสัปดาห์รวมของ B เท่าไร เทียบกับ −13R ของ A?
> > [!answer]-
> > −5 + 1.5 = **−3.5R** ดีกว่า A ราว 9.5R และนิสัยยังอยู่ครบ
""")

L.set_meta("level", "v2")
L.save()
