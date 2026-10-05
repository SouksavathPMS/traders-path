"""B9c · v2 upgrade of 3.3 R-Multiples & Risk:Reward (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("03 Risk & Money Management/3.3 R-Multiples & Risk-Reward.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Instead of counting your results in dollars or baht, count them in "units of risk". If you risked 100 and made 300, that's +3R. If you lost the 100, that's −1R. This way a small account and a big account speak the same language, and you can see whether your decisions are good regardless of how much money is on the line.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **R (1R)** — your initial risk on a trade: (entry − stop) × size.
> - **R-multiple** — a trade's profit or loss ÷ 1R.
> - **Planned R:R** — (target − entry) ÷ (entry − stop).
> - **Break-even win rate** — the win rate at which a given R:R neither makes nor loses money: 1 ÷ (1 + R:R).
> - **Total R** — the sum of R-multiples over a period.
> - **Average win / average loss** — in R; an average loss worse than −1R signals a leak.
> - **Costs** — spread, commission and slippage *(see 0.1, 1.2)*.
> - **Leak** — a habit that quietly lowers results, such as moving stops.
""")
L.before_heading("en", "2.", """
> [!analogy]
> R is like **converting every price into one currency** before comparing. A meal costs 120 baht in Bangkok and 60,000 kip in Vientiane: you can't tell which is cheaper until you convert. R converts every trade, in any market and any size, into the same unit.
>
> **Where it breaks:** currencies have one exchange rate for everyone. Your 1R depends on where you put the stop, so a sloppy stop makes your R numbers sloppy too.

> [!check]- Check your understanding: R-multiples
> **Q1.** Long 32.00, stop 31.20, exit 34.10. Short 1.0850, stop 1.0880, exit 1.0790. R-multiples?
> > [!answer]-
> > Long: 1R = 0.80; (34.10 − 32.00) ÷ 0.80 = **+2.63R**. Short: 1R = 30 pips; profit 60 pips → **+2R**.
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: what costs do to a small target
> A forex trade: stop **10 pips**, target **15 pips** → planned R:R **1.5**, break-even win rate 1 ÷ 2.5 = **40%**.
> 1. Add **1.5 pips** of spread and commission per trade.
> 2. A win now nets 15 − 1.5 = **13.5 pips**; a loss costs 10 + 1.5 = **11.5 pips**.
> 3. Real R:R = 13.5 ÷ 11.5 ≈ **1.17** → break-even win rate 1 ÷ 2.17 ≈ **46%**.
> 4. **So what?** On small targets, costs can move the bar from 40% to 46%. Check R:R after costs, or use bigger targets.

> [!check]- Check your understanding: break-even
> **Q1.** You win 70% of trades, but your average win is 0.4R and your average loss is 1R. Profitable?
> > [!answer]-
> > Break-even for 1:0.4 is 1 ÷ 1.4 ≈ **71%**. At 70%: 0.7 × 0.4 − 0.3 × 1 = **−0.02R** per trade, slightly losing.
""")
L.before_callout("en", "example", """
> [!check]- Check your understanding: honest R:R
> **Q1.** Your structural stop is 2.0 away and the next resistance is 2.2 away. You want 1:3, so you set the target 6.0 away. What's wrong?
> > [!answer]-
> > The target is invented. The honest R:R is about **1.1** (to the real obstacle). Skip the trade or find a better entry; don't stretch the target.
""")
L.before_callout("en", "action", """
![[p3-r-week.en.svg]]

> [!walkthrough] Step by step: reading the week in R
> Trades: +2.0R, −1.0R, −1.0R, +3.1R, −0.4R.
> 1. **Total** = 2.0 − 1.0 − 1.0 + 3.1 − 0.4 = **+2.7R**.
> 2. **Win rate** = 2 ÷ 5 = **40%**. **Average win** = (2.0 + 3.1) ÷ 2 = **+2.55R**. **Average loss** = (1.0 + 1.0 + 0.4) ÷ 3 = **−0.8R**.
> 3. An average loss **smaller** than −1R is healthy (one trade was closed early on purpose). If it were −1.3R, you'd be moving stops or suffering slippage: a leak to fix.
> 4. **So what?** Four numbers (total R, win rate, average win, average loss) describe your trading better than any dollar figure.

> [!market]
> - **Forex:** costs are measured in pips; with tight stops they're a big share of 1R *(see 0.3)*.
> - **Gold:** spreads of tens of cents per ounce add up quickly on short-term trades *(see 0.4)*.
> - **Stocks:** commission per trade matters more on small positions *(see 0.5)*.
> - **Crypto:** taker fees on both entry and exit; check them before planning small targets *(see 0.7)*.

> [!caution]
> Moving or removing a stop during a trade turns a planned −1R into −2R or worse, and a few of those wipe out many winning trades. Never widen a stop after entry.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** What's the break-even win rate for a planned 1:2.5 trade (before costs)?
> > [!answer]-
> > 1 ÷ 3.5 ≈ **29%**.
> **Q2.** Why measure progress in R instead of in dollars?
> > [!answer]-
> > R separates skill (the R your decisions produce) from size (how much each R is worth), so you can compare trades across markets and see whether you're improving even while your size changes.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> แทนที่จะนับผลเป็นดอลลาร์หรือบาท ให้นับเป็น "หน่วยความเสี่ยง" ถ้าคุณเสี่ยง 100 และได้ 300 คือ +3R ถ้าเสีย 100 นั้นไปคือ −1R ด้วยวิธีนี้ บัญชีเล็กและบัญชีใหญ่พูดภาษาเดียวกัน และคุณเห็นได้ว่าการตัดสินใจของคุณดีหรือไม่ โดยไม่ขึ้นกับว่าเงินเดิมพันมากแค่ไหน
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **R (1R)** — ความเสี่ยงเริ่มต้นของไม้: (ราคาเข้า − Stop) × ขนาด
> - **R-multiple** — กำไรหรือขาดทุนของไม้ ÷ 1R
> - **R:R ที่วางแผน (Planned R:R)** — (เป้า − ราคาเข้า) ÷ (ราคาเข้า − Stop)
> - **อัตราชนะคุ้มทุน (Break-even win rate)** — อัตราชนะที่ R:R นั้นไม่กำไรไม่ขาดทุน: 1 ÷ (1 + R:R)
> - **R รวม (Total R)** — ผลรวมของ R-multiple ในช่วงเวลาหนึ่ง
> - **กำไรเฉลี่ย / ขาดทุนเฉลี่ย (Average win / loss)** — ในหน่วย R ขาดทุนเฉลี่ยที่แย่กว่า −1R คือสัญญาณรั่วไหล
> - **ต้นทุน (Costs)** — Spread ค่าคอมมิชชัน และ Slippage *(ดู 0.1, 1.2)*
> - **รูรั่ว (Leak)** — นิสัยที่ลดผลลัพธ์อย่างเงียบ ๆ เช่น การเลื่อน Stop
""")
L.before_heading("th", "2.", """
> [!analogy]
> R เหมือน **การแปลงทุกราคาเป็นสกุลเงินเดียว** ก่อนเปรียบเทียบ อาหารมื้อหนึ่งราคา 120 บาทในกรุงเทพฯ และ 60,000 กีบในเวียงจันทน์ คุณบอกไม่ได้ว่าที่ไหนถูกกว่าจนกว่าจะแปลง R แปลงทุกไม้ ทุกตลาด ทุกขนาด ให้เป็นหน่วยเดียวกัน
>
> **จุดที่เปรียบเทียบไม่ได้:** สกุลเงินมีอัตราแลกเปลี่ยนเดียวสำหรับทุกคน แต่ 1R ของคุณขึ้นกับว่าคุณวาง Stop ตรงไหน Stop ที่ไม่ประณีตจึงทำให้ตัวเลข R ไม่ประณีตไปด้วย

> [!check]- เช็กความเข้าใจ: R-multiple
> **Q1.** ซื้อ 32.00 Stop 31.20 ออก 34.10 / ขาย 1.0850 Stop 1.0880 ออก 1.0790 R-multiple ของแต่ละไม้?
> > [!answer]-
> > ไม้ซื้อ: 1R = 0.80; (34.10 − 32.00) ÷ 0.80 = **+2.63R** ไม้ขาย: 1R = 30 pip กำไร 60 pip → **+2R**
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: ต้นทุนทำอะไรกับเป้าเล็ก ๆ
> เทรดฟอเร็กซ์: Stop **10 pip** เป้า **15 pip** → R:R ที่วางแผน **1.5** อัตราชนะคุ้มทุน 1 ÷ 2.5 = **40%**
> 1. เพิ่ม Spread และค่าคอมมิชชัน **1.5 pip** ต่อไม้
> 2. ไม้ชนะได้สุทธิ 15 − 1.5 = **13.5 pip** ไม้แพ้เสีย 10 + 1.5 = **11.5 pip**
> 3. R:R จริง = 13.5 ÷ 11.5 ≈ **1.17** → อัตราชนะคุ้มทุน 1 ÷ 2.17 ≈ **46%**
> 4. **แล้วไง?** กับเป้าเล็ก ต้นทุนอาจขยับเกณฑ์จาก 40% เป็น 46% ตรวจ R:R หลังหักต้นทุน หรือใช้เป้าที่ใหญ่ขึ้น

> [!check]- เช็กความเข้าใจ: จุดคุ้มทุน
> **Q1.** คุณชนะ 70% ของไม้ แต่กำไรเฉลี่ย 0.4R และขาดทุนเฉลี่ย 1R ทำกำไรไหม?
> > [!answer]-
> > จุดคุ้มทุนของ 1:0.4 คือ 1 ÷ 1.4 ≈ **71%** ที่ 70%: 0.7 × 0.4 − 0.3 × 1 = **−0.02R** ต่อไม้ ขาดทุนเล็กน้อย
""")
L.before_callout("th", "example", """
> [!check]- เช็กความเข้าใจ: R:R ที่ซื่อตรง
> **Q1.** Stop ตามโครงสร้างห่าง 2.0 แนวต้านถัดไปห่าง 2.2 คุณอยากได้ 1:3 จึงตั้งเป้าห่าง 6.0 ผิดตรงไหน?
> > [!answer]-
> > เป้าถูกแต่งขึ้น R:R ที่ซื่อตรงคือราว **1.1** (ถึงอุปสรรคจริง) ข้ามไม้นี้หรือหาจุดเข้าที่ดีกว่า อย่ายืดเป้า
""")
L.before_callout("th", "action", """
![[p3-r-week.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: อ่านหนึ่งสัปดาห์ในหน่วย R
> ผล: +2.0R, −1.0R, −1.0R, +3.1R, −0.4R
> 1. **รวม** = 2.0 − 1.0 − 1.0 + 3.1 − 0.4 = **+2.7R**
> 2. **อัตราชนะ** = 2 ÷ 5 = **40%** **กำไรเฉลี่ย** = (2.0 + 3.1) ÷ 2 = **+2.55R** **ขาดทุนเฉลี่ย** = (1.0 + 1.0 + 0.4) ÷ 3 = **−0.8R**
> 3. ขาดทุนเฉลี่ย **น้อยกว่า** −1R เป็นสัญญาณดี (มีไม้หนึ่งปิดก่อนอย่างตั้งใจ) ถ้าเป็น −1.3R แปลว่าคุณเลื่อน Stop หรือเจอ Slippage: เป็นรูรั่วที่ต้องแก้
> 4. **แล้วไง?** ตัวเลขสี่ตัว (R รวม อัตราชนะ กำไรเฉลี่ย ขาดทุนเฉลี่ย) อธิบายการเทรดของคุณได้ดีกว่าตัวเลขเงินใด ๆ

> [!market]
> - **ฟอเร็กซ์:** ต้นทุนวัดเป็น pip กับ Stop แคบ มันเป็นส่วนใหญ่ของ 1R *(ดู 0.3)*
> - **ทองคำ:** Spread หลายสิบเซนต์ต่อออนซ์รวมกันเร็วในเทรดระยะสั้น *(ดู 0.4)*
> - **หุ้น:** ค่าคอมมิชชันต่อไม้สำคัญมากขึ้นกับโพซิชันเล็ก *(ดู 0.5)*
> - **คริปโต:** ค่าธรรมเนียม Taker ทั้งตอนเข้าและออก ตรวจก่อนวางแผนเป้าเล็ก *(ดู 0.7)*

> [!caution]
> การเลื่อนหรือยกเลิก Stop ระหว่างเทรด เปลี่ยน −1R ที่วางแผนไว้เป็น −2R หรือแย่กว่า ไม่กี่ครั้งก็ลบไม้ชนะหลายไม้ อย่าขยาย Stop หลังเข้าเทรดเด็ดขาด
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** อัตราชนะคุ้มทุนของไม้ที่วางแผน 1:2.5 (ก่อนต้นทุน) เท่าไร?
> > [!answer]-
> > 1 ÷ 3.5 ≈ **29%**
> **Q2.** ทำไมวัดความก้าวหน้าเป็น R แทนดอลลาร์?
> > [!answer]-
> > R แยกฝีมือ (R ที่การตัดสินใจของคุณสร้าง) ออกจากขนาด (R หนึ่งหน่วยมีค่าเท่าไร) คุณจึงเปรียบเทียบเทรดข้ามตลาดได้ และเห็นว่ากำลังพัฒนาหรือไม่ แม้ขนาดจะเปลี่ยน
""")

L.set_meta("level", "v2")
L.save()
