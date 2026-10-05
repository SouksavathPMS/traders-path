"""B9d · v2 upgrade of 4.4 Daily Routine: Before, During, After (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("04 Psychology & Execution/4.4 Daily Routine- Before, During, After.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Good traders treat each day the same way. Before trading, they check how they feel, what news is coming and where they want to act, then set alerts and walk away. During trading, they only act when an alert rings and the checklist agrees. After trading, they write down what happened and switch off. Fewer decisions means fewer emotional mistakes.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Routine** — the same before / during / after steps every trading day.
> - **State check** — rating sleep, mood, stress and health 1–5 before trading.
> - **Economic calendar** — the schedule of data releases and central-bank events *(see 0.8)*.
> - **No-trade window** — a period around big news when you don't open new trades.
> - **Price alert** — a platform notification when price reaches a level.
> - **Execution grade (A/B/C)** — how well you followed the plan, regardless of the result.
> - **Screen time** — time spent watching charts; more is not better.
> - **Daylight saving time (DST)** — clocks moving one hour in summer in the US and Europe, which shifts their times in UTC+7.
""")
L.before_heading("en", "2.", """
> [!analogy]
> A good routine is like **fishing with several lines and bells**. You bait each line at the right spot (zones and alerts), then sit back. When a bell rings, you check that line. Staring at the water for hours doesn't catch more fish; it just makes you pull the line too early.
>
> **Where it breaks:** fish don't move the water around your line. Markets can move fast around news, so your "bells" need to include the calendar, not just price levels.

> [!check]- Check your understanding: the three blocks
> **Q1.** What is the goal of each block: before, during, after?
> > [!answer]-
> > Before: know your state, the day's risks and exactly what you're waiting for. During: execute the checklist only when an alert fires. After: record what happened while it's fresh and close the day.
""")
L.before_heading("en", "3.", """
![[p4-day-clock.en.svg]]

> [!walkthrough] Step by step: putting the day's events into UTC+7
> New York is UTC−4 in its summer and UTC−5 in its winter, so add **11 hours** (summer) or **12 hours** (winter).
> 1. **US CPI / jobs data** 08:30 New York → **19:30** UTC+7 (20:30 in winter).
> 2. **US stock open** 09:30 New York → **20:30** (21:30). **FOMC decision** 14:00 New York → **01:00** next day (02:00).
> 3. **London open** 08:00 London (UTC+1 in summer) → **14:00** (15:00 in winter).
> 4. For a few weeks in March and late October/early November, the US and Europe change clocks on different dates. Check the calendar's times in those weeks.
> 5. **So what?** Mark these times in your "before" block. A no-trade window of 30 minutes either side of a high-impact release is a simple, useful rule *(see 10.3)*.

> [!check]- Check your understanding: before
> **Q1.** You slept badly and rate your state 4/5. What does the routine say?
> > [!answer]-
> > Trade half size or not at all. A bad day for you is a bad day to trade.
""")
L.before_heading("en", "4.", """
> [!check]- Check your understanding: during
> **Q1.** No alert has fired for two hours, and you feel you "should be doing something". What does the routine say?
> > [!answer]-
> > No alert = no screen time. Close the charts; impulsive trades are born while watching "just in case".
""")
L.before_callout("en", "action", """
> [!check]- Check your understanding: after
> **Q1.** A trade followed every rule but hit its stop. How do you grade it, and why?
> > [!answer]-
> > **A**: the grade is about execution, not the result.

> [!market]
> - **Forex:** the most active hours in UTC+7 are London and the London–New York overlap, about 14:00–23:00 (one hour later in northern winter) *(see 0.3)*.
> - **Gold:** moves most around the London open and US data at 19:30 *(see 0.4)*.
> - **Stocks:** the US open (20:30) is volatile for the first 30 minutes; the SET has its own hours in Bangkok *(see 0.5)*.
> - **Crypto:** 24/7, so the routine must set your hours; the daily candle closes at 07:00 UTC+7 *(see 0.7)*.

> [!caution]
> Trading late into the night in UTC+7 (US session, FOMC at 01:00–02:00) when tired lowers your control. Many costly mistakes happen after midnight. Set an end time in your routine and keep it.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** List three items of your before-routine.
> > [!answer]-
> > Any three of: state check (1–5), economic calendar and no-trade windows, HTF state per market, zones and alerts, today's if-then plan.
> **Q2.** It's northern winter. At what time in Bangkok does the US stock market open, and when is a 08:30 New York release?
> > [!answer]-
> > Open 09:30 New York = **21:30** UTC+7; the release at 08:30 = **20:30** UTC+7.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> นักเทรดที่ดีทำทุกวันเหมือนกัน ก่อนเทรด ตรวจว่ารู้สึกอย่างไร มีข่าวอะไรจะมา และอยากลงมือตรงไหน แล้วตั้งการแจ้งเตือนและเดินออกไป ระหว่างเทรด ลงมือเฉพาะเมื่อการแจ้งเตือนดังและเช็กลิสต์เห็นด้วย หลังเทรด จดสิ่งที่เกิดขึ้นแล้วปิดเครื่อง การตัดสินใจน้อยลงหมายถึงความผิดพลาดทางอารมณ์น้อยลง
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **กิจวัตร (Routine)** — ขั้นตอนก่อน / ระหว่าง / หลังที่เหมือนกันทุกวันเทรด
> - **ตรวจสภาพ (State check)** — ให้คะแนนการนอน อารมณ์ ความเครียด และสุขภาพ 1–5 ก่อนเทรด
> - **ปฏิทินเศรษฐกิจ (Economic calendar)** — ตารางการประกาศข้อมูลและเหตุการณ์ธนาคารกลาง *(ดู 0.8)*
> - **ช่วงห้ามเทรด (No-trade window)** — ช่วงรอบข่าวใหญ่ที่ไม่เปิดไม้ใหม่
> - **การแจ้งเตือนราคา (Price alert)** — การแจ้งเตือนจากแพลตฟอร์มเมื่อราคาถึงระดับที่ตั้ง
> - **เกรดการปฏิบัติ (A/B/C)** — ทำตามแผนได้ดีแค่ไหน ไม่ขึ้นกับผลลัพธ์
> - **เวลาหน้าจอ (Screen time)** — เวลาที่นั่งดูกราฟ ยิ่งมากไม่ได้แปลว่ายิ่งดี
> - **เวลาออมแสง (Daylight saving time, DST)** — การเลื่อนนาฬิกาหนึ่งชั่วโมงช่วงฤดูร้อนในสหรัฐและยุโรป ทำให้เวลาของพวกเขาใน UTC+7 เปลี่ยน
""")
L.before_heading("th", "2.", """
> [!analogy]
> กิจวัตรที่ดีเหมือน **การตกปลาด้วยเบ็ดหลายคันที่ติดกระดิ่ง** คุณเกี่ยวเหยื่อแต่ละคันไว้ตรงจุดที่ใช่ (โซนและการแจ้งเตือน) แล้วนั่งพัก เมื่อกระดิ่งดัง คุณค่อยไปดูคันนั้น การจ้องน้ำหลายชั่วโมงไม่ได้ทำให้ได้ปลามากขึ้น แค่ทำให้กระตุกเบ็ดเร็วเกินไป
>
> **จุดที่เปรียบเทียบไม่ได้:** ปลาไม่ได้ทำให้น้ำรอบเบ็ดปั่นป่วน แต่ตลาดขยับเร็วรอบข่าว "กระดิ่ง" ของคุณจึงต้องรวมปฏิทินด้วย ไม่ใช่แค่ระดับราคา

> [!check]- เช็กความเข้าใจ: สามช่วง
> **Q1.** เป้าหมายของแต่ละช่วงคืออะไร: ก่อน ระหว่าง หลัง?
> > [!answer]-
> > ก่อน: รู้สภาพตัวเอง ความเสี่ยงของวัน และสิ่งที่รออยู่อย่างชัดเจน ระหว่าง: ทำตามเช็กลิสต์เฉพาะเมื่อการแจ้งเตือนดัง หลัง: บันทึกสิ่งที่เกิดขึ้นขณะที่ยังจำได้ดี และปิดวัน
""")
L.before_heading("th", "3.", """
![[p4-day-clock.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: แปลงเหตุการณ์ของวันเป็น UTC+7
> นิวยอร์กเป็น UTC−4 ในฤดูร้อนของเขา และ UTC−5 ในฤดูหนาว จึงบวก **11 ชั่วโมง** (ฤดูร้อน) หรือ **12 ชั่วโมง** (ฤดูหนาว)
> 1. **ข้อมูล CPI / การจ้างงานสหรัฐ** 08:30 นิวยอร์ก → **19:30** UTC+7 (20:30 ช่วงฤดูหนาว)
> 2. **ตลาดหุ้นสหรัฐเปิด** 09:30 นิวยอร์ก → **20:30** (21:30) **ผลประชุม FOMC** 14:00 นิวยอร์ก → **01:00** วันถัดไป (02:00)
> 3. **ลอนดอนเปิด** 08:00 ลอนดอน (UTC+1 ช่วงฤดูร้อน) → **14:00** (15:00 ช่วงฤดูหนาว)
> 4. ช่วงไม่กี่สัปดาห์ในเดือนมีนาคม และปลายตุลาคมถึงต้นพฤศจิกายน สหรัฐและยุโรปเปลี่ยนเวลาไม่ตรงวันกัน ตรวจเวลาในปฏิทินช่วงสัปดาห์เหล่านั้น
> 5. **แล้วไง?** ทำเครื่องหมายเวลาเหล่านี้ในช่วง "ก่อน" ช่วงห้ามเทรด 30 นาทีก่อนและหลังการประกาศข้อมูลสำคัญเป็นกฎที่ง่ายและมีประโยชน์ *(ดู 10.3)*

> [!check]- เช็กความเข้าใจ: ก่อน
> **Q1.** คุณนอนไม่ดีและให้คะแนนสภาพตัวเอง 4/5 กิจวัตรบอกว่าอะไร?
> > [!answer]-
> > เทรดครึ่งขนาดหรือไม่เทรดเลย วันที่แย่สำหรับคุณคือวันที่แย่สำหรับการเทรด
""")
L.before_heading("th", "4.", """
> [!check]- เช็กความเข้าใจ: ระหว่าง
> **Q1.** ไม่มีการแจ้งเตือนมาสองชั่วโมงแล้ว และคุณรู้สึกว่า "ควรทำอะไรสักอย่าง" กิจวัตรบอกว่าอะไร?
> > [!answer]-
> > ไม่มีการแจ้งเตือน = ไม่มีเวลาหน้าจอ ปิดกราฟ เทรดตามอารมณ์เกิดขึ้นขณะนั่งดู "เผื่อไว้"
""")
L.before_callout("th", "action", """
> [!check]- เช็กความเข้าใจ: หลัง
> **Q1.** เทรดที่ทำตามกฎทุกข้อแต่โดน Stop ให้เกรดอะไร และทำไม?
> > [!answer]-
> > **A**: เกรดวัดการปฏิบัติ ไม่ใช่ผลลัพธ์

> [!market]
> - **ฟอเร็กซ์:** ชั่วโมงที่คึกคักที่สุดใน UTC+7 คือช่วงลอนดอนและช่วงลอนดอน–นิวยอร์กซ้อนกัน ราว 14:00–23:00 (ช้าลงหนึ่งชั่วโมงช่วงฤดูหนาวซีกโลกเหนือ) *(ดู 0.3)*
> - **ทองคำ:** ขยับมากที่สุดช่วงลอนดอนเปิดและข้อมูลสหรัฐตอน 19:30 *(ดู 0.4)*
> - **หุ้น:** ตลาดสหรัฐเปิด (20:30) ผันผวนใน 30 นาทีแรก SET มีเวลาทำการของตัวเองตามเวลากรุงเทพฯ *(ดู 0.5)*
> - **คริปโต:** 24/7 กิจวัตรจึงต้องกำหนดชั่วโมงของคุณเอง แท่งรายวันปิด 07:00 UTC+7 *(ดู 0.7)*

> [!caution]
> การเทรดดึกใน UTC+7 (ช่วงตลาดสหรัฐ FOMC ตอน 01:00–02:00) ขณะเหนื่อย ทำให้การควบคุมตัวเองลดลง ความผิดพลาดราคาแพงจำนวนมากเกิดหลังเที่ยงคืน กำหนดเวลาเลิกในกิจวัตรและรักษามันไว้
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกสามรายการในกิจวัตรช่วงก่อนของคุณ
> > [!answer]-
> > สามข้อใดก็ได้: ตรวจสภาพ (1–5) ปฏิทินเศรษฐกิจและช่วงห้ามเทรด สภาวะ HTF ของแต่ละตลาด โซนและการแจ้งเตือน แผนถ้า-แล้วของวันนี้
> **Q2.** ช่วงฤดูหนาวซีกโลกเหนือ ตลาดหุ้นสหรัฐเปิดกี่โมงตามเวลากรุงเทพฯ และการประกาศตอน 08:30 นิวยอร์กคือกี่โมง?
> > [!answer]-
> > เปิด 09:30 นิวยอร์ก = **21:30** UTC+7 การประกาศตอน 08:30 = **20:30** UTC+7
""")

L.set_meta("level", "v2")
L.save()
