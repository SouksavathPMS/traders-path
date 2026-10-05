"""B7 · v2 upgrade of 9.2 Probability & Expected Value (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("09 Quant & Data Analysis/9.2 Probability & Expected Value.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Before betting on anything, ask: if I made this same bet a thousand times, would I end up ahead? That's **expected value**: the average result per bet over many repeats. A coin game that pays you 2 when you win and costs you 1 when you lose is a good bet, even though you'll lose half the flips. Trading works the same way, except that costs (spread, commission) are taken off every single bet, and they can turn a good bet into a bad one.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Probability** — how likely something is, from 0 (never) to 1 (always), often written in %.
> - **Outcome** — one possible result (full target, partial, scratch, stop).
> - **EV (expected value)** — Σ probability × result: the average result per bet over many repeats.
> - **Expectancy** — EV of a trading setup, usually in R *(see 3.4)*.
> - **Costs in R** — spread + commission + slippage, divided by the money risked at the stop.
> - **Scratch** — a trade closed at about break-even.
> - **Independence** — one result doesn't change the odds of the next.
> - **Gambler's fallacy** — believing a win is "due" after losses.
> - **Conditional probability** — the probability of an outcome *given* some condition (e.g. "win rate when the HTF trend agrees").
> - **Base rate** — how often something happens in general, before any special story.
> - **Law of large numbers** — the average of many independent repeats gets close to the EV.
> - **Martingale** — doubling the bet after each loss; guarantees ruin eventually.
""")
L.before_heading("en", "2.", """
![[p9-coin-dice.en.svg]]

> [!walkthrough] Step by step: a coin, a die, then a trade
> 1. **Coin game:** heads +2, tails −1. EV = 0.5 × 2 − 0.5 × 1 = **+0.50** per flip. You lose half the time and still win over many flips.
> 2. **Dice game:** a six pays +5, anything else costs 1. EV = 1/6 × 5 − 5/6 × 1 = 0.833 − 0.833 = **0**. Exciting when it hits, pointless on average.
> 3. **A trade:** win 45% of the time at +2R, lose 55% at −1R. EV = 0.45 × 2 − 0.55 × 1 = 0.90 − 0.55 = **+0.35R** before costs.
> 4. **So what?** A win rate below 50% can be a great bet, and a jackpot can be a pointless one. Only probability × payoff, added up, tells you which.

> [!check]- Check your understanding: EV
> **Q1.** A setup wins 30% at +3R and loses 70% at −1R. What's the EV?
> > [!answer]-
> > 0.30 × 3 − 0.70 × 1 = 0.90 − 0.70 = +0.20R per trade (before costs).
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: costs measured in R
> EUR/USD: spread **1.2 pips** + commission 7 USD per lot round turn (= **0.7 pips**) → **1.9 pips** per trade *(see 0.1)*.
> 1. **10-pip stop:** costs = 1.9 ÷ 10 = **0.19R** per trade → EV = 0.35 − 0.19 = **+0.16R**. Costs ate more than half the edge.
> 2. **40-pip stop:** costs = 1.9 ÷ 40 = **0.0475R** → EV = 0.35 − 0.05 ≈ **+0.30R**.
> 3. **So what?** The same costs in pips are four times heavier with a stop four times tighter. Short-term strategies need a much bigger raw edge to survive costs.

> [!check]- Check your understanding: independence
> **Q1.** You've lost five trades in a row with a 45% win-rate setup. Is the next trade more likely to win?
> > [!answer]-
> > No. If trades are independent, the probability is still about 45%. "A win is due" is the gambler's fallacy.
""")
L.before_callout("en", "example", """
> [!analogy]
> A casino doesn't know whether the next spin will win or lose, and doesn't care. It knows each bet has a small positive EV for the house, and over millions of spins that edge becomes almost certain profit. Your goal is to be the casino: small positive EV, many repetitions, never a bet big enough to ruin you.
>
> **Where it breaks:** a casino's odds are fixed and known exactly. Your edge is estimated from limited data and can change when the market changes (9.1, 9.3).

> [!check]- Check your understanding: the law of large numbers
> **Q1.** After 20 trades a trader with a real +0.35R edge is at −0.10R per trade. Is the edge gone?
> > [!answer]-
> > Not necessarily. 20 trades is far too few; running averages swing widely early on and converge only over hundreds of trades.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** costs are mainly spread and commission; they matter most for tight intraday stops *(see 0.1, 0.3)*.
> - **Gold:** wider spreads in dollars, swap on overnight holds *(see 0.2, 0.4)*.
> - **Stocks:** commissions are small at many brokers, but spreads and slippage on less liquid stocks add up; overnight gaps add to the loss branch *(see 0.5)*.
> - **Crypto:** exchange fees (often 0.05–0.1% per side) and funding on perps go into the EV calculation *(see 0.7)*.

> [!caution]
> The gambler's fallacy leads straight to **martingale**: doubling size after each loss to "win it back". With a 45% win rate, the chance of at least one run of 8 losses is about 53% in 200 trades and 68% in 300; doubling from 1% risk means the eighth trade alone risks 128% of the account. It ends in ruin, not recovery.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Write the EV formula and calculate it for: 40% at +2.5R, 15% at +0.8R, 10% at 0R, 35% at −1.05R.
> > [!answer]-
> > EV = Σ p × result = 1.00 + 0.12 + 0 − 0.3675 ≈ +0.75R.
> **Q2.** Why does a tighter stop make costs more dangerous?
> > [!answer]-
> > Costs are fixed in price terms (pips, cents), so they are a bigger fraction of a smaller risk: 1.9 pips is 0.19R on a 10-pip stop but under 0.05R on a 40-pip stop.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ก่อนเดิมพันอะไรก็ตาม ให้ถามว่า: ถ้าฉันเดิมพันแบบนี้พันครั้ง ฉันจะได้หรือเสีย? นั่นคือ **ค่าคาดหวัง (Expected value)**: ผลเฉลี่ยต่อการเดิมพันหนึ่งครั้งเมื่อทำซ้ำหลายครั้ง เกมโยนเหรียญที่จ่าย 2 เมื่อชนะและเสีย 1 เมื่อแพ้ คือการเดิมพันที่ดี แม้คุณจะแพ้ครึ่งหนึ่งของการโยน การเทรดก็เหมือนกัน ต่างแค่ต้นทุน (Spread ค่าคอมมิชชัน) ถูกหักทุกครั้ง และอาจเปลี่ยนการเดิมพันที่ดีให้กลายเป็นแย่
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **ความน่าจะเป็น (Probability)** — โอกาสที่จะเกิด จาก 0 (ไม่เคย) ถึง 1 (เสมอ) มักเขียนเป็น %
> - **ผลลัพธ์ (Outcome)** — ผลที่เป็นไปได้หนึ่งแบบ (ถึงเป้าเต็ม บางส่วน เสมอตัว โดน Stop)
> - **EV (Expected value)** — Σ ความน่าจะเป็น × ผล: ผลเฉลี่ยต่อการเดิมพันเมื่อทำซ้ำหลายครั้ง
> - **ค่าคาดหวังของ Setup (Expectancy)** — EV ของ Setup การเทรด มักเป็น R *(ดู 3.4)*
> - **ต้นทุนเป็น R** — Spread + ค่าคอมมิชชัน + Slippage หารด้วยเงินที่เสี่ยงที่ Stop
> - **ไม้เสมอตัว (Scratch)** — ไม้ที่ปิดราวจุดคุ้มทุน
> - **ความเป็นอิสระ (Independence)** — ผลหนึ่งไม่เปลี่ยนโอกาสของผลถัดไป
> - **ความเชื่อผิดของนักพนัน (Gambler's fallacy)** — เชื่อว่า "ถึงคิวชนะแล้ว" หลังแพ้ติดกัน
> - **ความน่าจะเป็นแบบมีเงื่อนไข (Conditional probability)** — โอกาสของผลหนึ่ง *เมื่อ* มีเงื่อนไขบางอย่าง (เช่น "อัตราชนะเมื่อเทรนด์ HTF เห็นด้วย")
> - **อัตราพื้นฐาน (Base rate)** — สิ่งหนึ่งเกิดบ่อยแค่ไหนโดยทั่วไป ก่อนมีเรื่องเล่าพิเศษใด ๆ
> - **กฎจำนวนมาก (Law of large numbers)** — ค่าเฉลี่ยของการทำซ้ำอิสระจำนวนมากเข้าใกล้ EV
> - **Martingale** — เพิ่มเดิมพันเป็นสองเท่าหลังแพ้ทุกครั้ง รับประกันว่าจะล้มละลายในที่สุด
""")
L.before_heading("th", "2.", """
![[p9-coin-dice.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: เหรียญ ลูกเต๋า แล้วจึงเป็นไม้เทรด
> 1. **เกมโยนเหรียญ:** หัว +2 ก้อย −1  EV = 0.5 × 2 − 0.5 × 1 = **+0.50** ต่อครั้ง คุณแพ้ครึ่งหนึ่งแต่ยังชนะเมื่อโยนหลายครั้ง
> 2. **เกมลูกเต๋า:** ออกหกได้ +5 อย่างอื่นเสีย 1  EV = 1/6 × 5 − 5/6 × 1 = 0.833 − 0.833 = **0** ตื่นเต้นตอนถูก แต่เฉลี่ยแล้วไม่มีประโยชน์
> 3. **ไม้เทรด:** ชนะ 45% ที่ +2R แพ้ 55% ที่ −1R  EV = 0.45 × 2 − 0.55 × 1 = 0.90 − 0.55 = **+0.35R** ก่อนหักต้นทุน
> 4. **แล้วไง?** อัตราชนะต่ำกว่า 50% อาจเป็นการเดิมพันที่ดีมาก และแจ็กพอตอาจเป็นการเดิมพันที่ไร้ประโยชน์ มีแค่ ความน่าจะเป็น × ผลตอบแทน รวมกัน ที่บอกได้

> [!check]- เช็กความเข้าใจ: EV
> **Q1.** Setup หนึ่งชนะ 30% ที่ +3R แพ้ 70% ที่ −1R  EV เท่าไหร่?
> > [!answer]-
> > 0.30 × 3 − 0.70 × 1 = 0.90 − 0.70 = +0.20R ต่อไม้ (ก่อนหักต้นทุน)
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: วัดต้นทุนเป็น R
> EUR/USD: Spread **1.2 pip** + ค่าคอมมิชชัน 7 ดอลลาร์ต่อล็อต (เปิด+ปิด) (= **0.7 pip**) → **1.9 pip** ต่อไม้ *(ดู 0.1)*
> 1. **Stop 10 pip:** ต้นทุน = 1.9 ÷ 10 = **0.19R** ต่อไม้ → EV = 0.35 − 0.19 = **+0.16R** ต้นทุนกินความได้เปรียบไปเกินครึ่ง
> 2. **Stop 40 pip:** ต้นทุน = 1.9 ÷ 40 = **0.0475R** → EV = 0.35 − 0.05 ≈ **+0.30R**
> 3. **แล้วไง?** ต้นทุนเป็น pip เท่ากัน แต่หนักขึ้นสี่เท่าเมื่อ Stop แคบลงสี่เท่า กลยุทธ์ระยะสั้นต้องมีความได้เปรียบดิบที่ใหญ่กว่ามากจึงจะรอดจากต้นทุน

> [!check]- เช็กความเข้าใจ: ความเป็นอิสระ
> **Q1.** คุณแพ้ห้าไม้ติดกันกับ Setup ที่อัตราชนะ 45% ไม้ถัดไปมีโอกาสชนะมากขึ้นไหม?
> > [!answer]-
> > ไม่ ถ้าแต่ละไม้เป็นอิสระต่อกัน โอกาสยังราว 45% "ถึงคิวชนะแล้ว" คือความเชื่อผิดของนักพนัน
""")
L.before_callout("th", "example", """
> [!analogy]
> คาสิโนไม่รู้ว่าการหมุนครั้งถัดไปจะชนะหรือแพ้ และไม่สนด้วย มันรู้ว่าการเดิมพันแต่ละครั้งมี EV บวกเล็กน้อยสำหรับเจ้ามือ และเมื่อหมุนหลายล้านครั้ง ความได้เปรียบนั้นกลายเป็นกำไรที่แทบแน่นอน เป้าหมายของคุณคือเป็นคาสิโน: EV บวกเล็กน้อย ทำซ้ำหลายครั้ง และไม่มีการเดิมพันครั้งไหนใหญ่จนทำให้คุณล้ม
>
> **จุดที่เปรียบเทียบไม่ได้:** อัตราต่อรองของคาสิโนคงที่และรู้แน่นอน แต่ความได้เปรียบของคุณประเมินจากข้อมูลที่จำกัด และเปลี่ยนได้เมื่อตลาดเปลี่ยน (9.1, 9.3)

> [!check]- เช็กความเข้าใจ: กฎจำนวนมาก
> **Q1.** หลัง 20 ไม้ เทรดเดอร์ที่มีความได้เปรียบจริง +0.35R อยู่ที่ −0.10R ต่อไม้ ความได้เปรียบหายไปแล้วไหม?
> > [!answer]-
> > ไม่จำเป็น 20 ไม้น้อยเกินไปมาก ค่าเฉลี่ยสะสมแกว่งแรงในช่วงแรก และเข้าใกล้ค่าจริงเมื่อผ่านไปหลายร้อยไม้เท่านั้น
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** ต้นทุนหลักคือ Spread และค่าคอมมิชชัน สำคัญที่สุดกับ Stop ระหว่างวันที่แคบ *(ดู 0.1, 0.3)*
> - **ทองคำ:** Spread กว้างกว่าเป็นดอลลาร์ และมี Swap เมื่อถือข้ามคืน *(ดู 0.2, 0.4)*
> - **หุ้น:** หลายโบรกเกอร์ค่าคอมมิชชันต่ำ แต่ Spread และ Slippage ของหุ้นสภาพคล่องต่ำสะสมได้ Gap ข้ามคืนเพิ่มขนาดของกิ่งขาดทุน *(ดู 0.5)*
> - **คริปโต:** ค่าธรรมเนียมกระดาน (มัก 0.05–0.1% ต่อข้าง) และ Funding ของ Perp ต้องใส่ในการคำนวณ EV *(ดู 0.7)*

> [!caution]
> ความเชื่อผิดของนักพนันนำไปสู่ **Martingale** โดยตรง: เพิ่มขนาดเป็นสองเท่าหลังแพ้ทุกครั้งเพื่อ "เอาคืน" ที่อัตราชนะ 45% โอกาสแพ้ติดกัน 8 ไม้อย่างน้อยหนึ่งครั้งคือราว 53% ใน 200 ไม้ และ 68% ใน 300 ไม้ ถ้าเริ่มจากเสี่ยง 1% แล้วเพิ่มเท่าตัว ไม้ที่แปดไม้เดียวเสี่ยง 128% ของบัญชี จบที่ล้มละลาย ไม่ใช่การฟื้นตัว
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** เขียนสูตร EV และคำนวณสำหรับ: 40% ที่ +2.5R, 15% ที่ +0.8R, 10% ที่ 0R, 35% ที่ −1.05R
> > [!answer]-
> > EV = Σ p × ผล = 1.00 + 0.12 + 0 − 0.3675 ≈ +0.75R
> **Q2.** ทำไม Stop ที่แคบขึ้นทำให้ต้นทุนอันตรายขึ้น?
> > [!answer]-
> > ต้นทุนคงที่เป็นราคา (pip เซนต์) จึงเป็นสัดส่วนที่ใหญ่ขึ้นของความเสี่ยงที่เล็กลง: 1.9 pip คือ 0.19R บน Stop 10 pip แต่น้อยกว่า 0.05R บน Stop 40 pip
""")

L.set_meta("level", "v2")
L.save()
