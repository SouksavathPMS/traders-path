"""B9a · v2 upgrade of 1.4 Candlestick Patterns in Context (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("01 Foundations/1.4 Candlestick Patterns in Context.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Some candle shapes show that one side tried hard and failed, or that one side suddenly took over. Those shapes only mean something at a price where people have a reason to act, such as a level where price turned before. The same shape in the middle of nowhere is just noise. So: find the place first, then look for the shape.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Candlestick pattern** — a shape of one to three candles that shows a shift in control.
> - **Engulfing** — a candle whose body covers the whole body of the previous candle.
> - **Pin bar (hammer / shooting star)** — a candle with one long wick and a small body at the other end.
> - **Doji** — a candle whose open and close are almost equal.
> - **Inside bar** — a candle whose whole range sits inside the previous candle's range.
> - **Level** — a price where orders cluster: support, resistance, a previous high or low *(see 2.4)*.
> - **Context** — the trend and situation around the pattern, especially on a higher timeframe *(see 1.5)*.
> - **Confirmation / anticipation** — waiting for the pattern to close / entering before it forms.
> - **Reward-to-risk (R:R)** — distance to target ÷ distance to stop *(see 3.3)*.
> - **Backtest** — testing a rule on past charts *(see 9.3)*.
""")
L.before_heading("en", "2.", """
![[p1-pin-quality.en.svg]]

> [!walkthrough] Step by step: grading three pin bars
> Rule: lower wick ≥ **2×** the body, and close in the top third (close location ≥ **67%**).
> 1. **A:** O 50.0, H 50.8, L 48.0, C 50.6 → body 0.6, wick 2.0 = **3.3×** ✓; close location (50.6 − 48.0) ÷ 2.8 = **93%** ✓ → **pass**.
> 2. **B:** O 50.0, H 50.9, L 49.0, C 50.8 → body 0.8, wick 1.0 = **1.3×** ✗ → **fail** (just a green candle).
> 3. **C:** O 49.6, H 51.0, L 48.0, C 49.4 → wick 1.4 = 7× body ✓, but close location (49.4 − 48.0) ÷ 3.0 = **47%** ✗ → **fail** (indecision, not rejection).
> 4. **So what?** Grade with numbers, not by eye. Only candle A shows a clear rejection of lower prices.

> [!check]- Check your understanding: patterns
> **Q1.** A candle's whole range sits inside the previous candle's range. What is it called, and how is it traded?
> > [!answer]-
> > An inside bar: compression. You trade the break of its high or low, ideally in the direction of the higher-timeframe trend.
""")
L.before_heading("en", "3.", """
> [!analogy]
> A pattern is like a **raised hand**. In a classroom, right after the teacher asks a question, a raised hand means "I have the answer". The same raised hand on a bus means nothing. The location gives the signal its meaning.
>
> **Where it breaks:** a classroom stays a classroom. A price level can stop mattering once it breaks, so the "classroom" itself can disappear *(see 2.4 on role reversal)*.

> [!check]- Check your understanding: location
> **Q1.** Why does the same hammer work at support and fail in the middle of a downtrend?
> > [!answer]-
> > At support there are resting buy orders and sellers taking profit, so someone has a reason to defend that price. In the middle of nowhere there are no special orders to react.
""")
L.before_heading("en", "5.", """
> [!walkthrough] Step by step: the engulfing trade in numbers
> EUR/USD on the daily chart, account **5,000 USD**, risk **1% = 50 USD** (illustrative prices).
> 1. **Entry** at the engulfing close: **1.0850**. Engulfing low 1.0815 → **stop** a few pips below at **1.0810** → risk **40 pips**.
> 2. **Target** at the prior swing high **1.0950** → **100 pips**. R:R = 100 ÷ 40 = **2.5**.
> 3. **Size** = 50 ÷ (40 pips × 10 USD per pip per lot) = 0.125 → round **down** to **0.12 lot**: risk = 0.12 × 10 × 40 = **48 USD**.
> 4. If the target is hit: 0.12 × 10 × 100 = **+120 USD (+2.4% of the account)**.
> 5. **So what?** The pattern gives the stop location, the next level gives the target, and the account size gives the position size. All three are decided before you click.

> [!check]- Check your understanding: the three filters
> **Q1.** A clean bullish engulfing forms at a weekly support zone, but the daily trend is strongly down. How many filters does it pass, and what do you do?
> > [!answer]-
> > Location ✓ and quality ✓, but context ✗: two filters = **watch**, don't trade yet.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** patterns on the daily close (04:00 UTC+7) are cleaner than on small timeframes full of noise *(see 0.3)*.
> - **Gold:** news spikes create long wicks that look like pin bars; check whether a release caused the wick *(see 0.4)*.
> - **Stocks:** an earnings gap can turn a perfect pattern irrelevant overnight *(see 0.5)*.
> - **Crypto:** thin weekend trading creates fake-looking wicks; give more weight to patterns with real volume *(see 0.7)*.

> [!caution]
> Trading every pattern you see, without a level, context and a stop, turns small losses into many losses. And never place the stop inside the signal candle, where normal noise will hit it.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** List the three filters in order and how many must pass before you trade.
> > [!answer]-
> > Location, context, quality. All **three** must pass; two = watch; one = ignore.
> **Q2.** Entry 2,010, stop 2,000, target 2,035. What's the R:R, and does it pass the checklist rule?
> > [!answer]-
> > Risk 10, reward 25 → R:R = **2.5**. Yes: it's at least 2× the risk.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> รูปร่างแท่งเทียนบางแบบแสดงว่าฝ่ายหนึ่งพยายามหนักแล้วล้มเหลว หรือฝ่ายหนึ่งเข้ามาคุมเกมอย่างฉับพลัน รูปร่างเหล่านี้มีความหมายเฉพาะที่ราคาที่คนมีเหตุผลจะลงมือ เช่น ระดับที่ราคาเคยกลับตัวมาก่อน รูปร่างเดียวกันกลางทางที่ไม่มีอะไรเป็นแค่สัญญาณรบกวน ดังนั้น: หาตำแหน่งก่อน แล้วค่อยมองหารูปร่าง
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **รูปแบบแท่งเทียน (Candlestick pattern)** — รูปร่างของแท่งเทียน 1–3 แท่งที่แสดงการเปลี่ยนผู้คุมเกม
> - **Engulfing** — แท่งที่ตัวแท่งครอบตัวแท่งก่อนหน้าทั้งหมด
> - **พินบาร์ (Pin bar / Hammer / Shooting star)** — แท่งที่มีไส้ยาวด้านเดียว และตัวแท่งเล็กอยู่อีกด้าน
> - **โดจิ (Doji)** — แท่งที่ราคาเปิดและปิดเกือบเท่ากัน
> - **Inside bar** — แท่งที่กรอบทั้งหมดอยู่ในกรอบของแท่งก่อนหน้า
> - **ระดับราคา (Level)** — ราคาที่คำสั่งกระจุกตัว: แนวรับ แนวต้าน จุดสูงหรือต่ำเดิม *(ดู 2.4)*
> - **บริบท (Context)** — เทรนด์และสถานการณ์รอบรูปแบบ โดยเฉพาะในไทม์เฟรมใหญ่ *(ดู 1.5)*
> - **รอยืนยัน / ดักล่วงหน้า (Confirmation / Anticipation)** — รอให้รูปแบบปิด / เข้าก่อนรูปแบบเกิด
> - **ผลตอบแทนต่อความเสี่ยง (R:R)** — ระยะถึงเป้า ÷ ระยะถึง Stop *(ดู 3.3)*
> - **แบ็กเทสต์ (Backtest)** — ทดสอบกฎกับกราฟในอดีต *(ดู 9.3)*
""")
L.before_heading("th", "2.", """
![[p1-pin-quality.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ให้คะแนนพินบาร์สามแท่ง
> กฎ: ไส้ล่าง ≥ **2 เท่า** ของตัวแท่ง และปิดในหนึ่งในสามบน (ตำแหน่งปิด ≥ **67%**)
> 1. **A:** เปิด 50.0 สูง 50.8 ต่ำ 48.0 ปิด 50.6 → ตัวแท่ง 0.6 ไส้ 2.0 = **3.3 เท่า** ✓ ตำแหน่งปิด (50.6 − 48.0) ÷ 2.8 = **93%** ✓ → **ผ่าน**
> 2. **B:** เปิด 50.0 สูง 50.9 ต่ำ 49.0 ปิด 50.8 → ตัวแท่ง 0.8 ไส้ 1.0 = **1.3 เท่า** ✗ → **ไม่ผ่าน** (เป็นแค่แท่งเขียว)
> 3. **C:** เปิด 49.6 สูง 51.0 ต่ำ 48.0 ปิด 49.4 → ไส้ 1.4 = 7 เท่าของตัวแท่ง ✓ แต่ตำแหน่งปิด (49.4 − 48.0) ÷ 3.0 = **47%** ✗ → **ไม่ผ่าน** (ลังเล ไม่ใช่การปฏิเสธ)
> 4. **แล้วไง?** ให้คะแนนด้วยตัวเลข ไม่ใช่ด้วยสายตา มีแค่แท่ง A ที่แสดงการปฏิเสธราคาต่ำอย่างชัดเจน

> [!check]- เช็กความเข้าใจ: รูปแบบ
> **Q1.** แท่งเทียนที่กรอบทั้งหมดอยู่ในกรอบของแท่งก่อนหน้าเรียกว่าอะไร และเทรดอย่างไร?
> > [!answer]-
> > Inside bar: การบีบตัว เทรดเมื่อราคาทะลุจุดสูงหรือต่ำของมัน โดยควรไปในทิศทางเทรนด์ไทม์เฟรมใหญ่
""")
L.before_heading("th", "3.", """
> [!analogy]
> รูปแบบแท่งเทียนเหมือน **การยกมือ** ในห้องเรียน ทันทีหลังครูถามคำถาม การยกมือหมายถึง "หนูรู้คำตอบ" แต่การยกมือแบบเดียวกันบนรถเมล์ไม่ได้หมายความอะไร ตำแหน่งทำให้สัญญาณมีความหมาย
>
> **จุดที่เปรียบเทียบไม่ได้:** ห้องเรียนยังเป็นห้องเรียนเสมอ แต่ระดับราคาอาจหมดความสำคัญเมื่อถูกทะลุ "ห้องเรียน" เองจึงหายไปได้ *(ดู 2.4 เรื่องการสลับบทบาท)*

> [!check]- เช็กความเข้าใจ: ตำแหน่ง
> **Q1.** ทำไมแฮมเมอร์แบบเดียวกันจึงได้ผลที่แนวรับ แต่ล้มเหลวกลางเทรนด์ขาลง?
> > [!answer]-
> > ที่แนวรับมีคำสั่งซื้อรออยู่และผู้ขายที่ทำกำไร จึงมีคนมีเหตุผลที่จะป้องกันราคานั้น กลางทางไม่มีคำสั่งพิเศษใดให้ตอบสนอง
""")
L.before_heading("th", "5.", """
> [!walkthrough] ไล่ทีละขั้น: เทรด Engulfing เป็นตัวเลข
> EUR/USD กราฟรายวัน บัญชี **5,000 ดอลลาร์** เสี่ยง **1% = 50 ดอลลาร์** (ราคาตัวอย่าง)
> 1. **เข้า** ที่ราคาปิดของแท่ง Engulfing: **1.0850** จุดต่ำของ Engulfing 1.0815 → **Stop** ต่ำกว่าเล็กน้อยที่ **1.0810** → เสี่ยง **40 pip**
> 2. **เป้า** ที่จุดสูงของสวิงก่อนหน้า **1.0950** → **100 pip** R:R = 100 ÷ 40 = **2.5**
> 3. **ขนาด** = 50 ÷ (40 pip × 10 ดอลลาร์ต่อ pip ต่อล็อต) = 0.125 → ปัด **ลง** เป็น **0.12 ล็อต**: ความเสี่ยง = 0.12 × 10 × 40 = **48 ดอลลาร์**
> 4. ถ้าถึงเป้า: 0.12 × 10 × 100 = **+120 ดอลลาร์ (+2.4% ของบัญชี)**
> 5. **แล้วไง?** รูปแบบให้ตำแหน่ง Stop ระดับถัดไปให้เป้า และขนาดบัญชีให้ขนาดโพซิชัน ทั้งสามอย่างตัดสินก่อนกดปุ่ม

> [!check]- เช็กความเข้าใจ: การกรอง 3 ชั้น
> **Q1.** แท่ง Bullish engulfing สวย ๆ เกิดที่โซนแนวรับรายสัปดาห์ แต่เทรนด์รายวันเป็นขาลงแรง ผ่านกี่ชั้น และคุณทำอะไร?
> > [!answer]-
> > ตำแหน่ง ✓ และคุณภาพ ✓ แต่บริบท ✗: สองชั้น = **เฝ้าดู** ยังไม่เทรด
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** รูปแบบบนราคาปิดรายวัน (04:00 UTC+7) สะอาดกว่าไทม์เฟรมเล็กที่เต็มไปด้วยสัญญาณรบกวน *(ดู 0.3)*
> - **ทองคำ:** การพุ่งช่วงข่าวสร้างไส้ยาวที่ดูเหมือนพินบาร์ ตรวจว่าไส้นั้นเกิดจากการประกาศข้อมูลหรือไม่ *(ดู 0.4)*
> - **หุ้น:** Gap จากงบการเงินทำให้รูปแบบที่สมบูรณ์แบบไร้ความหมายได้ในคืนเดียว *(ดู 0.5)*
> - **คริปโต:** การซื้อขายบาง ๆ ช่วงสุดสัปดาห์สร้างไส้ที่ดูหลอกตา ให้น้ำหนักกับรูปแบบที่มีวอลุ่มจริงมากกว่า *(ดู 0.7)*

> [!caution]
> การเทรดทุกรูปแบบที่เห็นโดยไม่มีระดับราคา บริบท และ Stop ทำให้การขาดทุนเล็ก ๆ กลายเป็นการขาดทุนหลายครั้ง และอย่าวาง Stop ไว้ในแท่งสัญญาณ ซึ่งสัญญาณรบกวนปกติจะชนได้
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกการกรองสามชั้นตามลำดับ และต้องผ่านกี่ชั้นก่อนเทรด
> > [!answer]-
> > ตำแหน่ง บริบท คุณภาพ ต้องผ่านทั้ง **สาม** ชั้น สองชั้น = เฝ้าดู หนึ่งชั้น = ไม่สนใจ
> **Q2.** เข้า 2,010 Stop 2,000 เป้า 2,035 R:R เท่าไร และผ่านกฎในเช็กลิสต์ไหม?
> > [!answer]-
> > เสี่ยง 10 ผลตอบแทน 25 → R:R = **2.5** ผ่าน เพราะอย่างน้อย 2 เท่าของความเสี่ยง
""")

L.set_meta("level", "v2")
L.save()
