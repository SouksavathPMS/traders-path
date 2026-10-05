"""B9a · v2 upgrade of 1.1 Think Like a Trader (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("01 Foundations/1.1 Think Like a Trader.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Nobody knows whether the next trade will win. Good traders don't try to know. They repeat one kind of trade that, over many tries, wins a little more than it loses, and they risk only a small amount each time. Like a shop that earns a little on many customers, the result only shows after many trades, not after one.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Edge** — a repeatable situation where the odds are tilted in your favour.
> - **R** — the amount you risk on one trade; +2R = you made twice what you risked *(see 3.3)*.
> - **Win rate** — the % of trades that win.
> - **Expectancy** — the average result per trade: win rate × average win − loss rate × average loss *(see 3.4)*.
> - **Losing streak** — several losing trades in a row.
> - **Sample size** — how many trades you judge a method on; small samples mislead.
> - **Setup / trigger / management** — when you trade, what makes you enter, how you exit.
> - **Process vs outcome** — whether you followed your rules vs whether the trade made money.
> - **P&L (profit and loss)** — the money result of a trade or a period.
""")
L.before_heading("en", "2.", """
> [!analogy]
> A trader is like a **noodle shop owner**. Some days it rains and few customers come; some days the shop is full. The owner doesn't close the shop after one bad day, because the business is judged over a year, and a fair price on every bowl adds up.
>
> **Where it breaks:** a shop rarely loses money on a sale. A trader with a good edge still loses on 40–60% of trades, so the bad days are more frequent and feel worse.

> [!check]- Check your understanding: probability
> **Q1.** Your system has a real edge, but you lose the next 5 trades. What does that tell you about the system?
> > [!answer]-
> > Almost nothing: 5 trades is far too small a sample. Losing streaks are normal inside winning systems (see the figure in section 3).
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: what an edge earns over 100 trades
> The system from the chart: win rate **45%**, win **+2R**, loss **−1R**.
> 1. Expectancy = 0.45 × 2 − 0.55 × 1 = 0.90 − 0.55 = **+0.35R per trade**.
> 2. Over **100 trades**: 45 wins × 2R = **+90R**, 55 losses × −1R = **−55R** → **+35R** in total.
> 3. With **1R = 100 USD** (1% of a 10,000 USD account): +35R ≈ **+3,500 USD**, even though you lost more trades than you won.
> 4. **So what?** Judge a method by its expectancy over many trades, never by whether the last trade won.

> [!check]- Check your understanding: edges
> **Q1.** Write a complete edge in three lines for a trade you've seen or read about.
> > [!answer]-
> > For example. **Setup:** uptrend on the daily, price pulls back to a support zone. **Trigger:** a bullish engulfing candle closes in the zone. **Management:** stop below the candle's low, target at the previous high.
""")
L.before_heading("en", "4.", """
![[p1-streak-odds.en.svg]]

> [!walkthrough] Step by step: how likely is a long losing streak?
> Same system, 45% win rate, so each trade has a **55%** chance to lose. Over 100 trades (computed exactly, then checked with 100,000 simulations):
> 1. At least **5 losses in a row**: about **92%**: almost certain.
> 2. At least **8 in a row**: about **31%**: roughly 1 time in 3.
> 3. At least **10 in a row**: about **10%**.
> 4. Risking 1% a trade, 8 losses cost about **8%** of the account; risking 5% a trade, about **34%** (0.95⁸ ≈ 0.66).
> 5. **So what?** Expect long streaks and size small enough to survive them. Phase 3 shows how.

> [!check]- Check your understanding: process vs outcome
> **Q1.** You entered without a stop, the trade went against you, then came back and closed at +2R. Which box is it, and what do you log?
> > [!answer]-
> > Bad process + good outcome ("dumb luck", the dangerous box). Log it as a mistake so the habit isn't rewarded.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** many small, frequent moves; spreads are low, so the same edge can be traded often *(see 0.3)*.
> - **Gold:** larger swings per trade; streaks feel bigger in money unless you size down *(see 0.4)*.
> - **Stocks:** single stocks can gap on earnings, so one trade can cost more than 1R *(see 0.5)*.
> - **Crypto:** trades 24/7 with big moves; the same probability thinking applies, with smaller size *(see 0.7)*.

> [!caution]
> The fastest way to lose an account is to increase size after losses to "win it back", or after a lucky win because you feel sure. A normal losing streak at large size can wipe out months of gains. Keep risk per trade fixed and small.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** A system wins 35% of trades with wins of +3R and losses of −1R. What's its expectancy, and is it worth trading?
> > [!answer]-
> > 0.35 × 3 − 0.65 × 1 = 1.05 − 0.65 = **+0.40R** per trade. Yes, if it holds over a large sample, even though it loses most trades.
> **Q2.** Why is "bad process, good outcome" the most dangerous result?
> > [!answer]-
> > It rewards breaking the rules, so you're likely to repeat it, and over many trades that habit loses money.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ไม่มีใครรู้ว่าเทรดไม้ถัดไปจะชนะไหม นักเทรดที่ดีไม่พยายามรู้ พวกเขาทำการเทรดแบบเดียวซ้ำ ๆ ซึ่งเมื่อทำหลายครั้ง ชนะมากกว่าแพ้เล็กน้อย และเสี่ยงแค่จำนวนน้อยในแต่ละครั้ง เหมือนร้านค้าที่ได้กำไรเล็กน้อยจากลูกค้าจำนวนมาก ผลลัพธ์จะเห็นหลังเทรดหลายไม้ ไม่ใช่ไม้เดียว
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **ความได้เปรียบ (Edge)** — สถานการณ์ที่เกิดซ้ำได้ ซึ่งโอกาสเอียงมาทางคุณ
> - **R** — จำนวนเงินที่คุณเสี่ยงต่อหนึ่งไม้ +2R = ได้กำไรสองเท่าของที่เสี่ยง *(ดู 3.3)*
> - **อัตราชนะ (Win rate)** — % ของไม้ที่ชนะ
> - **ค่าคาดหวัง (Expectancy)** — ผลเฉลี่ยต่อไม้: อัตราชนะ × กำไรเฉลี่ย − อัตราแพ้ × ขาดทุนเฉลี่ย *(ดู 3.4)*
> - **แพ้ติดกัน (Losing streak)** — แพ้หลายไม้ติดต่อกัน
> - **ขนาดตัวอย่าง (Sample size)** — จำนวนไม้ที่ใช้ตัดสินวิธีการ ตัวอย่างน้อยทำให้เข้าใจผิด
> - **Setup / Trigger / Management** — เมื่อไหร่จะเทรด อะไรทำให้เข้า และจะออกอย่างไร
> - **กระบวนการ vs ผลลัพธ์ (Process vs outcome)** — คุณทำตามกฎหรือไม่ vs ไม้นั้นได้เงินหรือไม่
> - **P&L (Profit and loss)** — ผลกำไรขาดทุนเป็นเงินของไม้หนึ่งหรือช่วงเวลาหนึ่ง
""")
L.before_heading("th", "2.", """
> [!analogy]
> นักเทรดเหมือน **เจ้าของร้านก๋วยเตี๋ยว** บางวันฝนตก ลูกค้าน้อย บางวันร้านเต็ม เจ้าของไม่ปิดร้านหลังวันแย่ ๆ วันเดียว เพราะธุรกิจถูกตัดสินกันทั้งปี และราคาที่ยุติธรรมในทุกชามก็ค่อย ๆ รวมกันเป็นกำไร
>
> **จุดที่เปรียบเทียบไม่ได้:** ร้านค้าแทบไม่ขาดทุนต่อการขายหนึ่งครั้ง แต่นักเทรดที่มีความได้เปรียบดีก็ยังแพ้ 40–60% ของไม้ วันแย่ ๆ จึงมาบ่อยกว่าและรู้สึกแย่กว่า

> [!check]- เช็กความเข้าใจ: ความน่าจะเป็น
> **Q1.** ระบบของคุณมีความได้เปรียบจริง แต่คุณแพ้ 5 ไม้ถัดไป สิ่งนี้บอกอะไรเกี่ยวกับระบบ?
> > [!answer]-
> > แทบไม่บอกอะไรเลย 5 ไม้เป็นตัวอย่างที่น้อยเกินไป การแพ้ติดกันเป็นเรื่องปกติในระบบที่ทำกำไร (ดูภาพในหัวข้อ 3)
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: ความได้เปรียบทำเงินได้เท่าไรใน 100 ไม้
> ระบบจากกราฟ: อัตราชนะ **45%** ชนะ **+2R** แพ้ **−1R**
> 1. ค่าคาดหวัง = 0.45 × 2 − 0.55 × 1 = 0.90 − 0.55 = **+0.35R ต่อไม้**
> 2. ใน **100 ไม้**: ชนะ 45 ไม้ × 2R = **+90R** แพ้ 55 ไม้ × −1R = **−55R** → รวม **+35R**
> 3. ถ้า **1R = 100 ดอลลาร์** (1% ของบัญชี 10,000 ดอลลาร์): +35R ≈ **+3,500 ดอลลาร์** แม้จะแพ้มากกว่าชนะ
> 4. **แล้วไง?** ตัดสินวิธีการจากค่าคาดหวังในหลายไม้ ไม่ใช่จากว่าไม้ล่าสุดชนะหรือไม่

> [!check]- เช็กความเข้าใจ: ความได้เปรียบ
> **Q1.** เขียนความได้เปรียบให้ครบสามบรรทัด สำหรับการเทรดที่คุณเคยเห็นหรือเคยอ่าน
> > [!answer]-
> > ตัวอย่าง **Setup:** เทรนด์ขาขึ้นบนกราฟรายวัน ราคาย่อลงมาที่โซนแนวรับ **Trigger:** แท่ง Bullish engulfing ปิดในโซน **Management:** Stop ใต้จุดต่ำของแท่ง เป้าที่จุดสูงเดิม
""")
L.before_heading("th", "4.", """
![[p1-streak-odds.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: แพ้ติดกันยาว ๆ มีโอกาสแค่ไหน?
> ระบบเดิม อัตราชนะ 45% แต่ละไม้จึงมีโอกาสแพ้ **55%** ใน 100 ไม้ (คำนวณแบบแม่นยำ แล้วตรวจด้วยการจำลอง 100,000 ครั้ง):
> 1. แพ้ติดกันอย่างน้อย **5 ไม้**: ราว **92%** แทบแน่นอน
> 2. อย่างน้อย **8 ไม้**: ราว **31%** ประมาณ 1 ใน 3 ครั้ง
> 3. อย่างน้อย **10 ไม้**: ราว **10%**
> 4. เสี่ยง 1% ต่อไม้ แพ้ 8 ไม้เสียราว **8%** ของบัญชี เสี่ยง 5% ต่อไม้ เสียราว **34%** (0.95⁸ ≈ 0.66)
> 5. **แล้วไง?** คาดไว้เลยว่าจะแพ้ติดกันยาว และกำหนดขนาดให้เล็กพอที่จะรอด เฟส 3 จะสอนวิธี

> [!check]- เช็กความเข้าใจ: กระบวนการ vs ผลลัพธ์
> **Q1.** คุณเข้าโดยไม่ตั้ง Stop ราคาวิ่งสวน แล้วกลับมาปิดที่ +2R เป็นช่องไหน และคุณบันทึกอะไร?
> > [!answer]-
> > กระบวนการแย่ + ผลลัพธ์ดี ("ฟลุ๊ค" ช่องอันตราย) บันทึกเป็นความผิดพลาด เพื่อไม่ให้นิสัยนั้นได้รางวัล
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** การขยับเล็ก ๆ บ่อยครั้ง Spread ต่ำ ความได้เปรียบเดียวกันจึงเทรดได้บ่อย *(ดู 0.3)*
> - **ทองคำ:** แกว่งต่อไม้มากกว่า การแพ้ติดกันจะรู้สึกหนักเป็นเงิน ถ้าไม่ลดขนาด *(ดู 0.4)*
> - **หุ้น:** หุ้นรายตัวอาจเกิด Gap ตอนประกาศงบ ไม้เดียวอาจเสียมากกว่า 1R *(ดู 0.5)*
> - **คริปโต:** ซื้อขาย 24/7 ขยับแรง ใช้วิธีคิดเชิงความน่าจะเป็นแบบเดียวกัน แต่ใช้ขนาดเล็กลง *(ดู 0.7)*

> [!caution]
> วิธีเสียบัญชีที่เร็วที่สุดคือเพิ่มขนาดหลังแพ้เพื่อ "เอาคืน" หรือหลังชนะแบบฟลุ๊คเพราะรู้สึกมั่นใจ การแพ้ติดกันตามปกติที่ขนาดใหญ่สามารถลบกำไรหลายเดือนได้ ให้ความเสี่ยงต่อไม้คงที่และเล็ก
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** ระบบชนะ 35% ของไม้ ชนะได้ +3R แพ้เสีย −1R ค่าคาดหวังเท่าไร และคุ้มที่จะเทรดไหม?
> > [!answer]-
> > 0.35 × 3 − 0.65 × 1 = 1.05 − 0.65 = **+0.40R** ต่อไม้ คุ้ม ถ้าผลนี้ยืนได้ในตัวอย่างขนาดใหญ่ แม้จะแพ้เป็นส่วนใหญ่
> **Q2.** ทำไม "กระบวนการแย่ ผลลัพธ์ดี" จึงเป็นผลที่อันตรายที่สุด?
> > [!answer]-
> > มันให้รางวัลกับการผิดกฎ คุณจึงมีแนวโน้มทำซ้ำ และเมื่อทำหลายไม้ นิสัยนั้นทำให้เสียเงิน
""")

L.set_meta("level", "v2")
L.save()
