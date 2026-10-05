"""B9e · v2 upgrade of 11.3 The Lifelong Learning Loop (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("11 Capstone/11.3 The Lifelong Learning Loop.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Markets keep changing, so a plan that works today needs regular check-ups. Set fixed times to look back: a few minutes each day, half an hour each week, an hour each month. Each time, change at most one thing and measure whether it helped. Don't jump to a new method after every bad week; collect enough data first.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Cadence** — a fixed rhythm of reviews: daily, weekly, monthly, quarterly, yearly.
> - **Changelog** — a dated list of every plan change, its reason and the data behind it.
> - **Plan version** — v1.0, v1.1 …: each tested change gets a new number.
> - **System hopping** — switching methods after losing streaks without enough data on any of them.
> - **Regime** — the market's current state (trend/range, quiet/volatile) *(see 2.2, 7.1)*.
> - **Edge decay** — an edge weakening as more people use it or markets change.
> - **Provisional result** — a result from a small sample that still needs more trades.
> - **Buy & hold benchmark** — what simply holding the market would have returned *(see 9.6)*.
""")
L.before_heading("en", "2.", """
> [!analogy]
> The learning loop is like an **athlete's training log**. A runner doesn't change shoes, diet and training plan in the same week after one slow race. They log every session, review weekly, change one thing, and see whether race times improve over months.
>
> **Where it breaks:** a runner's stopwatch is precise. Market results are noisy: luck can hide a good change or flatter a bad one for a long time, so your "stopwatch" needs many trades.

> [!walkthrough] Step by step: what the loop costs in time
> Using the rhythm table (quarterly and yearly durations are assumptions):
> 1. **Daily** 15 min × about 250 trading days = **62.5 hours**.
> 2. **Weekly** 30 min × 52 = **26 hours**. **Monthly** 1 hour × 12 = **12 hours**.
> 3. **Quarterly** study and testing, about 10 hours × 4 = **40 hours**. **Yearly** audit about **4 hours**.
> 4. Total ≈ **145 hours a year**, under **3 hours a week**.
> 5. **So what?** The loop is a small, fixed time cost. Skipping it to "save time" is how years of trading turn into one year repeated.

> [!check]- Check your understanding: the rhythm
> **Q1.** What is the output of a weekly review, and of a monthly review?
> > [!answer]-
> > Weekly: **one** improvement to test. Monthly: a plan version update (v1.1, v1.2 …) based on expectancy per setup, drawdown and comparison with buy & hold.
""")
L.before_heading("en", "3.", """
![[p11-change-test.en.svg]]

> [!walkthrough] Step by step: is 40 trades enough to keep a filter?
> From the example: with the volume-profile filter **+0.42R**, without **+0.22R**, 40 trades each. Assume results vary by about **1.5R** per trade.
> 1. 95% range at **40 trades** = ±1.96 × 1.5 ÷ √40 ≈ **±0.46R** → with filter roughly −0.04R to +0.88R; without −0.24R to +0.68R. Heavily overlapping.
> 2. At **160 trades** each: ±**0.23R** → +0.19R to +0.65R vs −0.01R to +0.45R. Still overlapping.
> 3. The filter looks **promising**, not proven. Keeping it is reasonable if it doesn't add risk, but keep tagging and comparing.
> 4. **So what?** Label small-sample results "provisional" in your changelog and re-check them after more trades.

> [!check]- Check your understanding: adding something new
> **Q1.** A YouTube strategy claims 80% wins. What are the five steps before it enters your plan?
> > [!answer]-
> > Write the rule precisely, backtest it on 50+ occurrences, paper trade it alongside your plan (tagged separately), compare expectancy, drawdown and trade count with your current setup, and keep it only if it improves results with enough trades.
""")
L.before_heading("en", "4.", """
> [!check]- Check your understanding: using the vault
> **Q1.** Your setup has lost for six weeks. Which lessons do you go back to first, and what question do they answer?
> > [!answer]-
> > 9.1–9.3: is this variance or has something changed? Then 2.2 and 7.1: what's the current regime? Also check your journal grades (4.5) to rule out execution problems.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** regimes shift with central-bank cycles; check whether your pairs moved from trend to range *(see 10.2)*.
> - **Gold:** its drivers (real yields, the dollar, central-bank buying) change over years; review them yearly *(see 10.4)*.
> - **Stocks:** compare your results with simply holding the index every month *(see 9.6, 10.7)*.
> - **Crypto:** market structure and regulation change fast; treat old backtests with extra caution *(see 0.7)*.

> [!caution]
> System hopping with real money, or adding an untested tool at full size, can quietly drain an account while it feels like progress. Test new ideas on paper or at micro size first, one at a time.
""")
L.before_callout("en", "key", """
> [!check]- Final check
> **Q1.** Name the five review cadences and what each produces.
> > [!answer]-
> > Daily: clean data. Weekly: one improvement to test. Monthly: a plan version update. Quarterly: a keep/drop decision on a new module. Yearly: an updated plan and IPS.
> **Q2.** What does a changelog entry need, and why?
> > [!answer]-
> > A date, the change, the reason and the data behind it. It turns your plan's history into evidence, and lets you undo changes that didn't help.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ตลาดเปลี่ยนตลอด แผนที่ใช้ได้วันนี้จึงต้องตรวจเป็นประจำ กำหนดเวลาย้อนดูให้แน่นอน: วันละไม่กี่นาที สัปดาห์ละครึ่งชั่วโมง เดือนละหนึ่งชั่วโมง แต่ละครั้งเปลี่ยนไม่เกินหนึ่งอย่าง แล้ววัดว่าช่วยไหม อย่ากระโดดไปวิธีใหม่หลังสัปดาห์ที่แย่ทุกครั้ง เก็บข้อมูลให้พอก่อน
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **จังหวะการทบทวน (Cadence)** — รอบการทบทวนที่แน่นอน: รายวัน รายสัปดาห์ รายเดือน รายไตรมาส รายปี
> - **บันทึกการเปลี่ยนแปลง (Changelog)** — รายการการเปลี่ยนแผนทุกครั้งพร้อมวันที่ เหตุผล และข้อมูลประกอบ
> - **เวอร์ชันแผน (Plan version)** — v1.0, v1.1 …: การเปลี่ยนที่ทดสอบแล้วได้เลขใหม่
> - **กระโดดระบบ (System hopping)** — เปลี่ยนวิธีหลังแพ้ติดกัน โดยไม่มีข้อมูลพอสำหรับวิธีไหนเลย
> - **สภาวะตลาด (Regime)** — สภาพปัจจุบันของตลาด (เทรนด์/กรอบ เงียบ/ผันผวน) *(ดู 2.2, 7.1)*
> - **ความได้เปรียบเสื่อม (Edge decay)** — ความได้เปรียบอ่อนลงเมื่อคนใช้มากขึ้นหรือตลาดเปลี่ยน
> - **ผลชั่วคราว (Provisional result)** — ผลจากตัวอย่างเล็กที่ยังต้องการไม้เพิ่ม
> - **เกณฑ์ซื้อแล้วถือ (Buy & hold benchmark)** — ผลตอบแทนถ้าแค่ถือตลาดไว้ *(ดู 9.6)*
""")
L.before_heading("th", "2.", """
> [!analogy]
> วงจรการเรียนรู้เหมือน **สมุดบันทึกการฝึกของนักกีฬา** นักวิ่งไม่เปลี่ยนรองเท้า อาหาร และแผนซ้อมพร้อมกันในสัปดาห์เดียวหลังวิ่งช้าครั้งเดียว พวกเขาบันทึกทุกการซ้อม ทบทวนรายสัปดาห์ เปลี่ยนทีละอย่าง แล้วดูว่าเวลาวิ่งดีขึ้นไหมในหลายเดือน
>
> **จุดที่เปรียบเทียบไม่ได้:** นาฬิกาจับเวลาของนักวิ่งแม่นยำ แต่ผลในตลาดมีสัญญาณรบกวนมาก โชคอาจซ่อนการเปลี่ยนที่ดีหรือทำให้การเปลี่ยนที่แย่ดูดีได้นาน "นาฬิกาจับเวลา" ของคุณจึงต้องใช้หลายไม้

> [!walkthrough] ไล่ทีละขั้น: วงจรนี้ใช้เวลาเท่าไร
> ใช้ตารางจังหวะ (ระยะเวลารายไตรมาสและรายปีเป็นการสมมติ):
> 1. **รายวัน** 15 นาที × ราว 250 วันทำการ = **62.5 ชั่วโมง**
> 2. **รายสัปดาห์** 30 นาที × 52 = **26 ชั่วโมง** **รายเดือน** 1 ชั่วโมง × 12 = **12 ชั่วโมง**
> 3. **รายไตรมาส** ศึกษาและทดสอบราว 10 ชั่วโมง × 4 = **40 ชั่วโมง** **รายปี** ตรวจสอบราว **4 ชั่วโมง**
> 4. รวม ≈ **145 ชั่วโมงต่อปี** ไม่ถึง **3 ชั่วโมงต่อสัปดาห์**
> 5. **แล้วไง?** วงจรนี้เป็นต้นทุนเวลาที่เล็กและคงที่ การข้ามมันเพื่อ "ประหยัดเวลา" คือวิธีที่การเทรดหลายปีกลายเป็นปีเดียวที่ซ้ำไปซ้ำมา

> [!check]- เช็กความเข้าใจ: จังหวะ
> **Q1.** ผลลัพธ์ของการทบทวนรายสัปดาห์และรายเดือนคืออะไร?
> > [!answer]-
> > รายสัปดาห์: การปรับปรุง **หนึ่ง** อย่างเพื่อทดสอบ รายเดือน: อัปเดตเวอร์ชันแผน (v1.1, v1.2 …) จากค่าคาดหวังต่อ Setup Drawdown และการเทียบกับการซื้อแล้วถือ
""")
L.before_heading("th", "3.", """
![[p11-change-test.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: 40 ไม้พอที่จะเก็บตัวกรองไว้ไหม?
> จากตัวอย่าง: ใช้ตัวกรอง Volume profile **+0.42R** ไม่ใช้ **+0.22R** อย่างละ 40 ไม้ สมมติผลแปรผันราว **1.5R** ต่อไม้
> 1. ช่วง 95% ที่ **40 ไม้** = ±1.96 × 1.5 ÷ √40 ≈ **±0.46R** → ใช้ตัวกรองราว −0.04R ถึง +0.88R ไม่ใช้ −0.24R ถึง +0.68R ซ้อนกันมาก
> 2. ที่ **160 ไม้** อย่างละ: ±**0.23R** → +0.19R ถึง +0.65R vs −0.01R ถึง +0.45R ยังซ้อนกัน
> 3. ตัวกรองดู **มีแวว** แต่ยังไม่พิสูจน์ การเก็บไว้สมเหตุสมผลถ้ามันไม่เพิ่มความเสี่ยง แต่ต้องแท็กและเปรียบเทียบต่อไป
> 4. **แล้วไง?** ติดป้ายผลจากตัวอย่างเล็กว่า "ชั่วคราว" ในบันทึกการเปลี่ยนแปลง และตรวจซ้ำหลังมีไม้มากขึ้น

> [!check]- เช็กความเข้าใจ: การเพิ่มสิ่งใหม่
> **Q1.** กลยุทธ์จาก YouTube อ้างว่าชนะ 80% ห้าขั้นตอนก่อนจะเข้าแผนของคุณคืออะไร?
> > [!answer]-
> > เขียนกฎให้แม่นยำ แบ็กเทสต์ 50 ครั้งขึ้นไป เทรดบนกระดาษคู่กับแผนเดิม (แท็กแยก) เทียบค่าคาดหวัง Drawdown และจำนวนไม้กับ Setup ปัจจุบัน และเก็บไว้เฉพาะเมื่อมันดีขึ้นด้วยจำนวนไม้ที่มากพอ
""")
L.before_heading("th", "4.", """
> [!check]- เช็กความเข้าใจ: ใช้คลังความรู้
> **Q1.** Setup ของคุณขาดทุนมาหกสัปดาห์ ควรกลับไปบทไหนก่อน และบทเหล่านั้นตอบคำถามอะไร?
> > [!answer]-
> > 9.1–9.3: นี่คือความแปรปรวนหรือมีอะไรเปลี่ยนไป? แล้ว 2.2 และ 7.1: สภาวะตลาดตอนนี้คืออะไร? และตรวจเกรดในบันทึก (4.5) เพื่อตัดปัญหาการปฏิบัติออก
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** สภาวะตลาดเปลี่ยนตามวัฏจักรธนาคารกลาง ตรวจว่าคู่เงินของคุณเปลี่ยนจากเทรนด์เป็นกรอบราคาหรือไม่ *(ดู 10.2)*
> - **ทองคำ:** ตัวขับเคลื่อน (Real yield ดอลลาร์ การซื้อของธนาคารกลาง) เปลี่ยนไปในหลายปี ทบทวนทุกปี *(ดู 10.4)*
> - **หุ้น:** เทียบผลของคุณกับการถือดัชนีเฉย ๆ ทุกเดือน *(ดู 9.6, 10.7)*
> - **คริปโต:** โครงสร้างตลาดและกฎระเบียบเปลี่ยนเร็ว ระวังแบ็กเทสต์เก่าเป็นพิเศษ *(ดู 0.7)*

> [!caution]
> การกระโดดระบบด้วยเงินจริง หรือการเพิ่มเครื่องมือที่ยังไม่ทดสอบด้วยขนาดเต็ม อาจดูดเงินในบัญชีอย่างเงียบ ๆ ทั้งที่รู้สึกเหมือนก้าวหน้า ทดสอบไอเดียใหม่บนกระดาษหรือขนาดจิ๋วก่อน ทีละอย่าง
""")
L.before_callout("th", "key", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกจังหวะการทบทวนห้าแบบ และผลลัพธ์ของแต่ละแบบ
> > [!answer]-
> > รายวัน: ข้อมูลที่สะอาด รายสัปดาห์: การปรับปรุงหนึ่งอย่างเพื่อทดสอบ รายเดือน: อัปเดตเวอร์ชันแผน รายไตรมาส: ตัดสินเก็บ/ทิ้งโมดูลใหม่ รายปี: แผนและ IPS ฉบับปรับปรุง
> **Q2.** บันทึกการเปลี่ยนแปลงแต่ละรายการต้องมีอะไร และทำไม?
> > [!answer]-
> > วันที่ การเปลี่ยน เหตุผล และข้อมูลประกอบ มันเปลี่ยนประวัติของแผนให้เป็นหลักฐาน และทำให้ย้อนการเปลี่ยนที่ไม่ได้ช่วยได้
""")

L.set_meta("level", "v2")
L.save()
