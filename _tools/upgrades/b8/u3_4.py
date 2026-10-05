"""B8 · v2 upgrade of 3.4 Win Rate × R = Expectancy (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("03 Risk & Money Management/3.4 Win Rate x R = Expectancy.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Being right often doesn't make you money by itself. What matters is how much you win when you're right compared with how much you lose when you're wrong. A trader who is right only 1 time in 3 can do very well if each win is three times bigger than each loss; a trader who is right 3 times in 4 can still lose money if the wins are tiny. **Expectancy** puts both together into one number: the average result per trade.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Win rate (Win%)** — the share of trades that end in profit.
> - **Average win / average loss (in R)** — the typical size of winners and losers, measured in R *(see 3.3)*.
> - **Expectancy** — the average result per trade: Win% × average win − Loss% × average loss.
> - **Reward:risk (R:R)** — average win ÷ average loss.
> - **Break-even win rate** — the win rate at which expectancy is exactly zero: 1 ÷ (1 + R:R).
> - **Sample size** — the number of trades your numbers are based on *(see 9.1)*.
> - **Costs in R** — spread, commission and slippage divided by 1R *(see 9.2)*.
> - **Setup** — one specific, repeatable trade pattern with its own rules.
""")
L.before_heading("en", "2.", """
![[p3-breakeven-curve.en.svg]]

> [!walkthrough] Step by step: the break-even win rate
> Break-even win rate = 1 ÷ (1 + R:R).
> 1. **R:R 1** → 1 ÷ 2 = **50%**.
> 2. **R:R 2** → 1 ÷ 3 = **33%**.
> 3. **R:R 3** → 1 ÷ 4 = **25%**.
> 4. **The scalper** in the table wins 75% at 0.3R: break-even is 1 ÷ 1.3 ≈ **77%**. At 75% it's just **below** the curve, so it loses.
> 5. **So what?** Never judge a win rate on its own. First ask what R:R it comes with; then check which side of the curve you're on.

> [!walkthrough] Step by step: costs change the answer
> Assume costs of **0.05R** per trade (spread + commission), taken off every trade.
> 1. **Swing trader:** +0.26R − 0.05R = **+0.21R** per trade. Still good.
> 2. **Scalper:** wins become 0.30 − 0.05 = 0.25R; losses become 1.05R → 0.75 × 0.25 − 0.25 × 1.05 = 0.1875 − 0.2625 = **−0.075R**. Worse.
> 3. **So what?** Costs hit small-R systems hardest because they're a bigger slice of each small win.

> [!analogy]
> Expectancy is like a **fruit stall's profit per crate**. One stall sells many crates at a tiny profit each, but one spoiled crate wipes out twenty sales. Another sells fewer crates at a big profit and can afford some spoiled ones. What matters is the average profit per crate across all crates, not how many sold at a profit.
>
> **Where it breaks:** a stall knows its numbers after a month. A trader needs 100+ trades before the average is reliable (section 2).

> [!check]- Check your understanding: the formula
> **Q1.** Win rate 40%, average win 2.5R, average loss 1R. What's the expectancy, and is it above break-even?
> > [!answer]-
> > 0.40 × 2.5 − 0.60 × 1 = 1.00 − 0.60 = +0.40R. Break-even at 2.5R is 1 ÷ 3.5 ≈ 29%, so 40% is well above.
""")
L.before_heading("en", "3.", """
> [!check]- Check your understanding: sample size
> **Q1.** Your system shows −0.1R per trade after 15 trades. Should you abandon it?
> > [!answer]-
> > Not on that evidence. 15 trades is far too few; a +0.26R system can easily be negative after 15 trades. Keep following the plan at small risk and re-check at 50 and 100.
""")
L.before_callout("en", "example", """
> [!walkthrough] Step by step: from expectancy to a month
> Swing system after costs: **+0.21R** per trade; **20** trades a month; 1R = **1%** of the account.
> 1. Expected R per month = 0.21 × 20 = **+4.2R**.
> 2. At 1% per R ≈ **+4.2%** a month on average, before compounding.
> 3. Some months will be negative: with 20 trades, luck still matters a lot (9.1).
> 4. **So what?** Doubling trades only helps if the extra trades keep the same expectancy; forcing extra low-quality trades usually lowers it.

> [!check]- Check your understanding: growth
> **Q1.** Expectancy +0.3R, 10 trades a month, 0.5% risk per trade. Expected return per month?
> > [!answer]-
> > 0.3 × 10 = 3R → 3 × 0.5% = about +1.5% a month on average.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** low costs on majors, but tight intraday stops make costs a big share of 1R *(see 9.2)*.
> - **Gold:** wider spreads; strategies with small R targets struggle after costs *(see 0.4)*.
> - **Stocks:** commissions are often tiny, but slippage and gaps add to the average loss *(see 0.5)*.
> - **Crypto:** exchange fees on both sides plus funding can turn a small positive expectancy negative *(see 0.7)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Write the expectancy formula and calculate it for 35% wins at 3R and 65% losses at 1R.
> > [!answer]-
> > Expectancy = Win% × avg win − Loss% × avg loss = 0.35 × 3 − 0.65 × 1 = +0.40R.
> **Q2.** What win rate do you need to break even with an average win of 1.5R and an average loss of 1R?
> > [!answer]-
> > 1 ÷ (1 + 1.5) = 40%.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> การถูกบ่อยไม่ได้ทำให้ได้เงินในตัวมันเอง สิ่งที่สำคัญคือเวลาถูกคุณได้เท่าไหร่ เทียบกับเวลาผิดคุณเสียเท่าไหร่ เทรดเดอร์ที่ถูกแค่ 1 ใน 3 ครั้งอาจทำได้ดีมาก ถ้าแต่ละครั้งที่ชนะได้มากกว่าที่แพ้สามเท่า เทรดเดอร์ที่ถูก 3 ใน 4 ครั้งก็ยังขาดทุนได้ ถ้ากำไรแต่ละครั้งเล็กนิดเดียว **ค่าคาดหวัง (Expectancy)** รวมทั้งสองอย่างเป็นตัวเลขเดียว: ผลเฉลี่ยต่อไม้
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **อัตราชนะ (Win rate, Win%)** — สัดส่วนของไม้ที่จบด้วยกำไร
> - **กำไรเฉลี่ย / ขาดทุนเฉลี่ย (เป็น R)** — ขนาดทั่วไปของไม้ชนะและไม้แพ้ วัดเป็น R *(ดู 3.3)*
> - **ค่าคาดหวัง (Expectancy)** — ผลเฉลี่ยต่อไม้: Win% × กำไรเฉลี่ย − Loss% × ขาดทุนเฉลี่ย
> - **ผลตอบแทน:ความเสี่ยง (R:R)** — กำไรเฉลี่ย ÷ ขาดทุนเฉลี่ย
> - **อัตราชนะที่เท่าทุน (Break-even win rate)** — อัตราชนะที่ทำให้ค่าคาดหวังเป็นศูนย์พอดี: 1 ÷ (1 + R:R)
> - **ขนาดตัวอย่าง (Sample size)** — จำนวนไม้ที่ตัวเลขของคุณอ้างอิง *(ดู 9.1)*
> - **ต้นทุนเป็น R** — Spread ค่าคอมมิชชัน และ Slippage หารด้วย 1R *(ดู 9.2)*
> - **Setup** — รูปแบบไม้เทรดหนึ่งแบบที่ทำซ้ำได้และมีกฎของตัวเอง
""")
L.before_heading("th", "2.", """
![[p3-breakeven-curve.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: อัตราชนะที่เท่าทุน
> อัตราชนะที่เท่าทุน = 1 ÷ (1 + R:R)
> 1. **R:R 1** → 1 ÷ 2 = **50%**
> 2. **R:R 2** → 1 ÷ 3 = **33%**
> 3. **R:R 3** → 1 ÷ 4 = **25%**
> 4. **Scalper** ในตารางชนะ 75% ที่ 0.3R: จุดเท่าทุนคือ 1 ÷ 1.3 ≈ **77%** ที่ 75% อยู่ **ใต้** เส้นโค้งพอดี จึงขาดทุน
> 5. **แล้วไง?** อย่าตัดสินอัตราชนะโดยดูอย่างเดียว ถามก่อนว่ามาพร้อม R:R เท่าไหร่ แล้วเช็กว่าคุณอยู่ฝั่งไหนของเส้นโค้ง

> [!walkthrough] ไล่ทีละขั้น: ต้นทุนเปลี่ยนคำตอบ
> สมมติต้นทุน **0.05R** ต่อไม้ (Spread + ค่าคอมมิชชัน) หักทุกไม้
> 1. **Swing trader:** +0.26R − 0.05R = **+0.21R** ต่อไม้ ยังดีอยู่
> 2. **Scalper:** กำไรกลายเป็น 0.30 − 0.05 = 0.25R ขาดทุนกลายเป็น 1.05R → 0.75 × 0.25 − 0.25 × 1.05 = 0.1875 − 0.2625 = **−0.075R** แย่ลง
> 3. **แล้วไง?** ต้นทุนกระทบระบบที่ R เล็กหนักที่สุด เพราะเป็นสัดส่วนที่ใหญ่ของกำไรเล็ก ๆ แต่ละครั้ง

> [!analogy]
> ค่าคาดหวังเหมือน **กำไรต่อลังของแผงผลไม้** แผงหนึ่งขายหลายลังโดยได้กำไรนิดเดียวต่อลัง แต่ลังเน่าลังเดียวลบยอดขายไปยี่สิบลัง อีกแผงขายน้อยลังแต่ได้กำไรมาก จึงรับลังเน่าได้บ้าง สิ่งที่สำคัญคือกำไรเฉลี่ยต่อลังจากทุกลัง ไม่ใช่จำนวนลังที่ขายได้กำไร
>
> **จุดที่เปรียบเทียบไม่ได้:** แผงผลไม้รู้ตัวเลขของตัวเองหลังผ่านไปหนึ่งเดือน แต่เทรดเดอร์ต้องมี 100+ ไม้ก่อนค่าเฉลี่ยจะเชื่อถือได้ (หัวข้อ 2)

> [!check]- เช็กความเข้าใจ: สูตร
> **Q1.** อัตราชนะ 40% กำไรเฉลี่ย 2.5R ขาดทุนเฉลี่ย 1R ค่าคาดหวังเท่าไหร่ และสูงกว่าจุดเท่าทุนไหม?
> > [!answer]-
> > 0.40 × 2.5 − 0.60 × 1 = 1.00 − 0.60 = +0.40R จุดเท่าทุนที่ 2.5R คือ 1 ÷ 3.5 ≈ 29% 40% จึงสูงกว่ามาก
""")
L.before_heading("th", "3.", """
> [!check]- เช็กความเข้าใจ: ขนาดตัวอย่าง
> **Q1.** ระบบของคุณได้ −0.1R ต่อไม้หลัง 15 ไม้ ควรทิ้งไหม?
> > [!answer]-
> > ยังไม่ควรด้วยหลักฐานแค่นี้ 15 ไม้น้อยเกินไปมาก ระบบ +0.26R ติดลบหลัง 15 ไม้ได้ง่าย ๆ ทำตามแผนต่อด้วยความเสี่ยงต่ำ แล้วเช็กใหม่ที่ 50 และ 100 ไม้
""")
L.before_callout("th", "example", """
> [!walkthrough] ไล่ทีละขั้น: จากค่าคาดหวังสู่หนึ่งเดือน
> ระบบ Swing หลังหักต้นทุน: **+0.21R** ต่อไม้ **20** ไม้ต่อเดือน 1R = **1%** ของบัญชี
> 1. R ที่คาดต่อเดือน = 0.21 × 20 = **+4.2R**
> 2. ที่ 1% ต่อ R ≈ เฉลี่ย **+4.2%** ต่อเดือน ก่อนทบต้น
> 3. บางเดือนจะติดลบ: กับ 20 ไม้ โชคยังมีผลมาก (9.1)
> 4. **แล้วไง?** การเทรดเพิ่มเป็นสองเท่าช่วยได้ก็ต่อเมื่อไม้ที่เพิ่มมีค่าคาดหวังเท่าเดิม การฝืนเทรดไม้คุณภาพต่ำเพิ่มมักลดค่าคาดหวังลง

> [!check]- เช็กความเข้าใจ: การเติบโต
> **Q1.** ค่าคาดหวัง +0.3R 10 ไม้ต่อเดือน เสี่ยง 0.5% ต่อไม้ ผลตอบแทนที่คาดต่อเดือนเท่าไหร่?
> > [!answer]-
> > 0.3 × 10 = 3R → 3 × 0.5% = เฉลี่ยราว +1.5% ต่อเดือน
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** ต้นทุนของคู่เงินหลักต่ำ แต่ Stop ระหว่างวันที่แคบทำให้ต้นทุนเป็นสัดส่วนใหญ่ของ 1R *(ดู 9.2)*
> - **ทองคำ:** Spread กว้างกว่า กลยุทธ์ที่เป้า R เล็กลำบากหลังหักต้นทุน *(ดู 0.4)*
> - **หุ้น:** ค่าคอมมิชชันมักต่ำมาก แต่ Slippage และ Gap เพิ่มขาดทุนเฉลี่ย *(ดู 0.5)*
> - **คริปโต:** ค่าธรรมเนียมกระดานทั้งสองข้างบวก Funding อาจเปลี่ยนค่าคาดหวังบวกเล็ก ๆ ให้ติดลบ *(ดู 0.7)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** เขียนสูตรค่าคาดหวังและคำนวณสำหรับชนะ 35% ที่ 3R และแพ้ 65% ที่ 1R
> > [!answer]-
> > ค่าคาดหวัง = Win% × กำไรเฉลี่ย − Loss% × ขาดทุนเฉลี่ย = 0.35 × 3 − 0.65 × 1 = +0.40R
> **Q2.** ต้องมีอัตราชนะเท่าไหร่จึงจะเท่าทุน ถ้ากำไรเฉลี่ย 1.5R และขาดทุนเฉลี่ย 1R?
> > [!answer]-
> > 1 ÷ (1 + 1.5) = 40%
""")

L.set_meta("level", "v2")
L.save()
