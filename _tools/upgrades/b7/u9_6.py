"""B7 · v2 upgrade of 9.6 Performance Metrics: Sharpe, Sortino, Profit Factor (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("09 Quant & Data Analysis/9.6 Performance Metrics- Sharpe, Sortino, Profit Factor.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Two cars can reach the same city, one calmly and one swerving through traffic at double the speed limit. Both "arrived", but you'd only want to repeat the first trip. Performance metrics do the same for trading: besides "how much did I make?", they ask "how bumpy was the ride?", "how deep did I fall at the worst moment?" and "how many trades is this based on?". Read them together, never one alone.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **CAGR (compound annual growth rate)** — the steady yearly growth that would turn the start value into the end value: (end ÷ start)^(1 ÷ years) − 1.
> - **Volatility** — the standard deviation of returns, usually annualised *(see 6.6)*.
> - **Sharpe ratio** — average return ÷ volatility (minus a risk-free rate), annualised: return per unit of total bumpiness.
> - **Sortino ratio** — like Sharpe, but only the **downside** (losing) bumpiness counts as risk.
> - **Downside deviation** — the "standard deviation" of losses only.
> - **Max drawdown (maxDD)** — the biggest fall from a peak to a later low *(see 3.6)*.
> - **Calmar ratio** — CAGR ÷ max drawdown.
> - **Profit factor (PF)** — gross profits ÷ gross losses.
> - **Expectancy** — average result per trade *(see 3.4)*.
> - **Risk-free rate** — the return on very safe cash, such as short-term government bills.
> - **Benchmark** — what you compare against, e.g. buy-and-hold of the same market.
""")
L.before_heading("en", "2.", """
![[p9-ten-equity.en.svg]]

> [!walkthrough] Step by step: metrics from the same ten trades as 9.1
> Trades in R: **+2, −1, +0.5, −1, +3, −1, +1.5, −0.5, −1, +2.5** (from `_tools/quant/ten_trades.py`).
> 1. **Profit factor:** winners 2 + 0.5 + 3 + 1.5 + 2.5 = **9.5R**; losers 1 + 1 + 1 + 0.5 + 1 = **4.5R** → 9.5 ÷ 4.5 = **2.11**.
> 2. **Equity curve (running total):** 2, 1, 1.5, 0.5, 3.5, 2.5, 4, 3.5, 2.5, **5.0R**.
> 3. **Max drawdown:** biggest fall from a peak: from 2.0 to 0.5 = **1.5R** (also 4.0 → 2.5). At 1% risk per trade that's about **1.5%** of the account.
> 4. **Sharpe-like (per trade):** mean 0.5 ÷ SD 1.62 = **0.31**.
> 5. **Sortino-like (per trade):** downside deviation = √((1² + 1² + 1² + 0.5² + 1²) ÷ 10) = √0.425 ≈ 0.65 → 0.5 ÷ 0.65 = **0.77**. Higher than Sharpe because the big swings were mostly **winners**.
> 6. **So what?** PF 2.11 looks strong, but with ten trades it means little (9.1). Track these numbers as the sample grows; trust them only after 100+ trades.

> [!check]- Check your understanding: profit factor and drawdown
> **Q1.** Trades: +3, −1, −1, −1, +2. What are the profit factor and the max drawdown in R?
> > [!answer]-
> > PF = 5 ÷ 3 ≈ 1.67. Equity: 3, 2, 1, 0, 2 → max drawdown from 3 to 0 = 3R.
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: CAGR and Calmar
> 1. **One year:** 10,000 → 10,500 USD → CAGR = 10,500 ÷ 10,000 − 1 = **5%**.
> 2. **Five years:** 10,000 → 16,105 USD → (16,105 ÷ 10,000)^(1/5) − 1 = 1.6105^0.2 − 1 ≈ **10% a year**. (Not 61% ÷ 5 = 12.2%: growth compounds.)
> 3. **Calmar:** a strategy with CAGR **10%** and max drawdown **20%** → 10 ÷ 20 = **0.5**: decent.
> 4. **So what?** CAGR alone hides risk; dividing by drawdown tells you how much growth you got for each unit of pain.

> [!check]- Check your understanding: CAGR
> **Q1.** An account doubles in 7 years. Roughly what is the CAGR?
> > [!answer]-
> > 2^(1/7) − 1 ≈ 10.4% a year.
""")
L.before_callout("en", "example", """
> [!analogy]
> Risk-adjusted metrics are like a car's **fuel consumption** rather than its top speed. Top speed (total return) is exciting, but how far you get per litre (return per unit of risk) tells you whether you can keep driving for years.
>
> **Where it breaks:** fuel use is stable; risk isn't. A strategy can look smooth for years and then show its real risk in one crash (selling options, for example). Calm history is not proof of low risk.

> [!check]- Check your understanding: reading metrics together
> **Q1.** A backtest shows Sharpe 3.5 and profit factor 6 over 400 trades. What should you check first?
> > [!answer]-
> > Bugs and biases: look-ahead, missing costs, survivorship. Numbers that good with many trades are usually a mistake, not an edge.
""")
L.before_callout("en", "action", """
> [!market]
> - **Stocks & indices:** compare with buy-and-hold of the index; annualise daily data with √252.
> - **Forex & gold:** include swap costs in returns; about 260 trading days a year *(see 0.2)*.
> - **Crypto:** 365 trading days a year; volatility is far higher, so a Sharpe that looks low can still mean big swings *(see 0.7)*.
> - **All markets:** for your discretionary trading, compute metrics in **R** so different markets can be compared.

> [!caution]
> Strategies that sell options or average down often show smooth curves, high win rates and high Sharpe ratios for a long time, then lose years of gains in days. Always look at the worst drawdown, the worst single trade and the number of trades, not just the ratios.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** What does Sortino measure that Sharpe doesn't?
> > [!answer]-
> > It counts only downside volatility (losses) as risk, so strategies with big winning swings aren't penalised for them.
> **Q2.** Why must you always note the number of trades next to a metric?
> > [!answer]-
> > Metrics from few trades are dominated by luck; the same profit factor or Sharpe means far more over 300 trades than over 10.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> รถสองคันไปถึงเมืองเดียวกันได้ คันหนึ่งขับสบาย ๆ อีกคันปาดซ้ายขวาด้วยความเร็วสองเท่าของที่กำหนด ทั้งคู่ "ถึง" แต่คุณจะอยากเดินทางซ้ำแบบคันแรกเท่านั้น ตัวชี้วัดผลงานทำแบบเดียวกันกับการเทรด: นอกจาก "ได้เท่าไหร่?" ยังถามว่า "ทางขรุขระแค่ไหน?" "ตอนแย่ที่สุดลงไปลึกแค่ไหน?" และ "อิงจากกี่ไม้?" อ่านพร้อมกัน ไม่ใช่ดูตัวเดียว
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **CAGR (Compound annual growth rate)** — อัตราเติบโตรายปีคงที่ที่จะเปลี่ยนค่าเริ่มต้นเป็นค่าสุดท้าย: (สุดท้าย ÷ เริ่ม)^(1 ÷ จำนวนปี) − 1
> - **ความผันผวน (Volatility)** — ส่วนเบี่ยงเบนมาตรฐานของผลตอบแทน มักปรับเป็นรายปี *(ดู 6.6)*
> - **Sharpe ratio** — ผลตอบแทนเฉลี่ย ÷ ความผันผวน (หักอัตราไร้ความเสี่ยง) ปรับเป็นรายปี: ผลตอบแทนต่อหน่วยความขรุขระทั้งหมด
> - **Sortino ratio** — เหมือน Sharpe แต่นับเฉพาะความขรุขระ **ด้านลบ** (ขาดทุน) เป็นความเสี่ยง
> - **Downside deviation** — "ส่วนเบี่ยงเบนมาตรฐาน" ของการขาดทุนเท่านั้น
> - **Max drawdown (maxDD)** — การลดลงมากที่สุดจากจุดสูงสุดถึงจุดต่ำที่ตามมา *(ดู 3.6)*
> - **Calmar ratio** — CAGR ÷ Max drawdown
> - **Profit factor (PF)** — กำไรรวม ÷ ขาดทุนรวม
> - **ค่าคาดหวัง (Expectancy)** — ผลเฉลี่ยต่อไม้ *(ดู 3.4)*
> - **อัตราไร้ความเสี่ยง (Risk-free rate)** — ผลตอบแทนของเงินสดที่ปลอดภัยมาก เช่น ตั๋วเงินคลังระยะสั้น
> - **เกณฑ์เปรียบเทียบ (Benchmark)** — สิ่งที่ใช้เทียบ เช่น การซื้อแล้วถือตลาดเดียวกัน
""")
L.before_heading("th", "2.", """
![[p9-ten-equity.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ตัวชี้วัดจากสิบไม้ชุดเดียวกับ 9.1
> ไม้เป็น R: **+2, −1, +0.5, −1, +3, −1, +1.5, −0.5, −1, +2.5** (จาก `_tools/quant/ten_trades.py`)
> 1. **Profit factor:** ไม้ชนะ 2 + 0.5 + 3 + 1.5 + 2.5 = **9.5R** ไม้แพ้ 1 + 1 + 1 + 0.5 + 1 = **4.5R** → 9.5 ÷ 4.5 = **2.11**
> 2. **กราฟเงินทุน (ยอดสะสม):** 2, 1, 1.5, 0.5, 3.5, 2.5, 4, 3.5, 2.5, **5.0R**
> 3. **Max drawdown:** การลดลงมากที่สุดจากจุดสูงสุด: จาก 2.0 เหลือ 0.5 = **1.5R** (และ 4.0 → 2.5 ด้วย) ที่ความเสี่ยง 1% ต่อไม้ คือราว **1.5%** ของบัญชี
> 4. **คล้าย Sharpe (ต่อไม้):** ค่าเฉลี่ย 0.5 ÷ SD 1.62 = **0.31**
> 5. **คล้าย Sortino (ต่อไม้):** Downside deviation = √((1² + 1² + 1² + 0.5² + 1²) ÷ 10) = √0.425 ≈ 0.65 → 0.5 ÷ 0.65 = **0.77** สูงกว่า Sharpe เพราะการแกว่งใหญ่ส่วนใหญ่เป็น **ไม้ชนะ**
> 6. **แล้วไง?** PF 2.11 ดูแข็งแรง แต่กับสิบไม้แทบไม่มีความหมาย (9.1) ติดตามตัวเลขเหล่านี้ไปเรื่อย ๆ เมื่อตัวอย่างโตขึ้น และเชื่อหลังผ่าน 100+ ไม้เท่านั้น

> [!check]- เช็กความเข้าใจ: Profit factor และ Drawdown
> **Q1.** ไม้: +3, −1, −1, −1, +2 Profit factor และ Max drawdown เป็น R เท่าไหร่?
> > [!answer]-
> > PF = 5 ÷ 3 ≈ 1.67 เงินทุน: 3, 2, 1, 0, 2 → Max drawdown จาก 3 ลงไป 0 = 3R
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: CAGR และ Calmar
> 1. **หนึ่งปี:** 10,000 → 10,500 ดอลลาร์ → CAGR = 10,500 ÷ 10,000 − 1 = **5%**
> 2. **ห้าปี:** 10,000 → 16,105 ดอลลาร์ → (16,105 ÷ 10,000)^(1/5) − 1 = 1.6105^0.2 − 1 ≈ **10% ต่อปี** (ไม่ใช่ 61% ÷ 5 = 12.2%: การเติบโตทบต้น)
> 3. **Calmar:** กลยุทธ์ที่ CAGR **10%** และ Max drawdown **20%** → 10 ÷ 20 = **0.5**: พอใช้ได้
> 4. **แล้วไง?** CAGR อย่างเดียวซ่อนความเสี่ยง การหารด้วย Drawdown บอกว่าคุณได้การเติบโตเท่าไหร่ต่อความเจ็บปวดหนึ่งหน่วย

> [!check]- เช็กความเข้าใจ: CAGR
> **Q1.** บัญชีเพิ่มเป็นสองเท่าใน 7 ปี CAGR ประมาณเท่าไหร่?
> > [!answer]-
> > 2^(1/7) − 1 ≈ 10.4% ต่อปี
""")
L.before_callout("th", "example", """
> [!analogy]
> ตัวชี้วัดที่ปรับความเสี่ยงเหมือน **อัตราสิ้นเปลืองน้ำมัน** ของรถ แทนที่จะเป็นความเร็วสูงสุด ความเร็วสูงสุด (ผลตอบแทนรวม) น่าตื่นเต้น แต่วิ่งได้กี่กิโลต่อลิตร (ผลตอบแทนต่อหน่วยความเสี่ยง) บอกว่าคุณขับต่อไปได้อีกหลายปีไหม
>
> **จุดที่เปรียบเทียบไม่ได้:** การใช้น้ำมันคงที่ แต่ความเสี่ยงไม่คงที่ กลยุทธ์อาจดูราบเรียบหลายปี แล้วเผยความเสี่ยงจริงในการถล่มครั้งเดียว (เช่น การขายออปชัน) ประวัติที่สงบไม่ใช่หลักฐานว่าความเสี่ยงต่ำ

> [!check]- เช็กความเข้าใจ: อ่านตัวชี้วัดร่วมกัน
> **Q1.** Backtest แสดง Sharpe 3.5 และ Profit factor 6 จาก 400 ไม้ ควรตรวจอะไรก่อน?
> > [!answer]-
> > บั๊กและอคติ: Look-ahead ต้นทุนที่หายไป Survivorship ตัวเลขดีขนาดนั้นกับไม้จำนวนมากมักเป็นความผิดพลาด ไม่ใช่ความได้เปรียบ
""")
L.before_callout("th", "action", """
> [!market]
> - **หุ้นและดัชนี:** เทียบกับการซื้อแล้วถือดัชนี ปรับข้อมูลรายวันเป็นรายปีด้วย √252
> - **ฟอเร็กซ์และทองคำ:** รวมต้นทุน Swap ในผลตอบแทน ราว 260 วันซื้อขายต่อปี *(ดู 0.2)*
> - **คริปโต:** 365 วันซื้อขายต่อปี ความผันผวนสูงกว่ามาก Sharpe ที่ดูต่ำก็ยังหมายถึงการแกว่งใหญ่ได้ *(ดู 0.7)*
> - **ทุกตลาด:** สำหรับการเทรดแบบใช้ดุลยพินิจ ให้คำนวณตัวชี้วัดเป็น **R** เพื่อเทียบระหว่างตลาดได้

> [!caution]
> กลยุทธ์ที่ขายออปชันหรือถัวเฉลี่ยขาลงมักแสดงกราฟราบเรียบ อัตราชนะสูง และ Sharpe สูงเป็นเวลานาน แล้วเสียกำไรหลายปีในไม่กี่วัน ดู Drawdown ที่แย่ที่สุด ไม้ที่แย่ที่สุด และจำนวนไม้เสมอ ไม่ใช่แค่อัตราส่วน
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** Sortino วัดอะไรที่ Sharpe ไม่วัด?
> > [!answer]-
> > นับเฉพาะความผันผวนด้านลบ (การขาดทุน) เป็นความเสี่ยง กลยุทธ์ที่มีการแกว่งขึ้นใหญ่ ๆ จึงไม่ถูกลงโทษเพราะมัน
> **Q2.** ทำไมต้องจดจำนวนไม้ไว้ข้างตัวชี้วัดเสมอ?
> > [!answer]-
> > ตัวชี้วัดจากไม้จำนวนน้อยถูกโชคครอบงำ Profit factor หรือ Sharpe ค่าเดียวกันมีความหมายมากกว่ามากเมื่อมาจาก 300 ไม้ แทนที่จะเป็น 10 ไม้
""")

L.set_meta("level", "v2")
L.save()
