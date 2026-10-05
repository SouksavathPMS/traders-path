"""B4 · v2 upgrade of 5.7 An ICT Model Setup, Step by Step (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("05 Liquidity & ICT/5.7 An ICT Model Setup, Step by Step.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Each idea from this phase (liquidity, sweeps, cheap vs expensive prices, gaps, order blocks, timing) is weak on its own. This lesson puts them in a fixed order, like a checklist, so you only trade when **all** of them agree. Most days they won't, and that's the point: the checklist says "no" far more often than "yes". When it does say yes, you also know in advance what you'll do if the trade works, half-works, or fails.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Model** — a fixed, written set of rules for finding, entering and managing a trade.
> - **Confluence** — several independent reasons pointing to the same trade.
> - **HTF bias** — the direction allowed by the higher-timeframe trend *(see 2.2, 2.6)*.
> - **Draw on liquidity** — the pool price is likely heading to: your target *(see 5.1)*.
> - **PD array** — an FVG, order block or other level where price may react *(see 5.3–5.5)*.
> - **MSS / CHoCH** — the structure shift that proves the reversal *(see 2.3, 5.2)*.
> - **CE** — the 50% line of an FVG *(see 5.4)*.
> - **Killzone** — the London or NY AM high-activity window *(see 5.6)*.
> - **R / R:R** — 1R = what you lose at the stop; R:R = reward ÷ risk *(see 3.3)*.
> - **Partial profit** — closing part of the position early (e.g. half at +2R).
> - **Break-even stop** — moving the stop to the entry price so the rest can't lose.
> - **Expectancy** — average result per trade in R: win% × average win − loss% × average loss *(see 3.4)*.
> - **Paper trading / forward test** — following the model in real time without real money, or with very small size, to collect honest statistics.
""")
L.before_heading("en", "3.", """
![[p5-model-flow.en.svg]]

> [!analogy]
> The model is like a **pilot's pre-flight checklist**. The pilot doesn't skip "fuel checked" because the weather looks nice. Every item is read out, and one "no" means the plane stays on the ground. Most of the safety comes from the boring discipline of the list, not from the pilot's talent.
>
> **Where it breaks:** a pre-flight checklist covers things that really decide safety. A trading checklist only raises the odds; a trade that passes all eight steps can still lose, and you need many trades to know whether the list works at all.

> [!walkthrough] Step by step: the worked example in money, including every outcome
> Account **10,000 USD**, risk **1% = 100 USD**. Entry **105.25**, stop **101.9** → risk per unit **3.35**.
> 1. **Size:** 100 ÷ 3.35 = 29.85 → round down to **29 units**. Real risk = 29 × 3.35 = **97.15 USD** (≈1R).
> 2. **Outcome A, it works:** half (14 units) closed at +2R (**111.95**): 14 × 6.70 = **93.80**. Stop to break-even. The other 15 units reach **113.95**: 15 × 8.70 = **130.50**. Total **224.30 USD** = **+2.31R**.
> 3. **Outcome B, it half-works:** half closed at +2R (+93.80), then price returns and the rest is stopped at break-even (0). Total **+93.80 USD** = **+0.97R**.
> 4. **Outcome C, it fails:** price closes below the sweep low and hits **101.9** before +2R: **−97.15 USD** = **−1R**. The sweep was really a run. No revenge trade; wait for a completely new setup.
> 5. **Outcome D, no fill:** price never retraces to 105.25. Cancel the order; don't chase. Result **0**.
> 6. **So what?** Before entering, you already know the result of every branch. The only decision left during the trade is to follow the plan.

> [!check]- Check your understanding: the worked example
> **Q1.** Your account is 5,000 USD. Same entry and stop. How many units for 1% risk?
> > [!answer]-
> > Risk = 50 USD. 50 ÷ 3.35 = 14.9 → 14 units (real risk 46.90 USD).
> **Q2.** After the half at +2R, price comes back to the entry. Why is this a +0.97R trade and not a loss?
> > [!answer]-
> > Half the position was already closed at +2R, and the stop on the rest was moved to break-even, so the second half closed at zero.
""")
L.before_callout("en", "action", """
> [!walkthrough] Step by step: judging the model by its statistics, not by one trade
> You paper trade the model for **30 setups** (illustrative numbers).
> 1. **Results:** 12 winners at an average of **+2.6R** = +31.2R; 18 losers at **−1R** = −18R.
> 2. **Net:** 31.2 − 18 = **+13.2R** over 30 trades.
> 3. **Expectancy** = 13.2 ÷ 30 = **+0.44R per trade** (the same as 0.4 × 2.6 − 0.6 × 1).
> 4. **After costs** (spread, commission, slippage), say 0.1R per trade: 0.44 − 0.10 = **+0.34R**.
> 5. **So what?** A 40% win rate is fine if the winners are big enough. But 30 trades is a small sample *(see 9.3)*: treat +0.34R as "promising", keep logging, and only increase size after 100+ trades confirm it.

> [!check]- Check your understanding: statistics
> **Q1.** Over 20 trades the model wins 6 at +2.5R and loses 14 at −1R. What is the expectancy?
> > [!answer]-
> > 6 × 2.5 = 15R; 14 × 1 = 14R; net +1R ÷ 20 = +0.05R per trade, and probably negative after costs. Not good enough yet.

> [!market]
> - **Forex:** the model was built for FX; use the London or NY AM killzone and session highs/lows as pools *(see 5.6)*.
> - **Gold:** works the same way, but stops are wide (often 10–30 USD), so the position is small; check the US data calendar *(see 0.4)*.
> - **Stocks & index futures:** use the US regular session (20:30 UTC+7 in summer); overnight gaps can skip step 4 entirely *(see 0.5)*.
> - **Crypto:** 24/7 and highly leveraged; sweeps are deeper, so use wider stops and smaller size, and remember the daily close is 07:00 UTC+7 *(see 0.7)*.

> [!caution]
> A good-looking model on past charts can still lose money live: hindsight makes every sweep and FVG look obvious, and costs and slippage are easy to forget. Don't trade it with real money until you have **at least 30 forward-tested setups**, and even then start at a fraction of normal size. Expect losing streaks: with a 40% win rate, the chance of at least 6 losses in a row somewhere in 100 trades is about 87%, and of 8 in a row about 49% *(see 3.6)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Name the eight steps of the model in order.
> > [!answer]-
> > HTF bias → draw on liquidity (target) → discount/premium → liquidity taken (sweep) → time (killzone) → displacement + MSS → entry at the PD array (FVG CE / OB) → risk (stop beyond the sweep, size for 1R, R:R ≥ 2).
> **Q2.** A setup passes seven steps, but the R:R to the target is 1.4. What do you do?
> > [!answer]-
> > Skip it. A missing step is the filter working, not bad luck.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> แต่ละแนวคิดในเฟสนี้ (สภาพคล่อง การกวาด ราคาถูกหรือแพง ช่องว่าง Order block จังหวะเวลา) ใช้เดี่ยว ๆ แล้วอ่อน บทนี้เรียงทั้งหมดตามลำดับตายตัวเหมือนเช็กลิสต์ คุณจะเทรดก็ต่อเมื่อ **ทุกข้อ** เห็นตรงกัน ส่วนใหญ่จะไม่ครบ และนั่นคือประเด็น: เช็กลิสต์ตอบ "ไม่" บ่อยกว่า "ใช่" มาก เมื่อมันตอบใช่ คุณก็รู้ล่วงหน้าแล้วว่าจะทำอะไรถ้าไม้นั้นได้ผล ได้ผลครึ่งเดียว หรือล้มเหลว
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **โมเดล (Model)** — ชุดกฎที่เขียนไว้ตายตัว สำหรับหา เข้า และจัดการไม้เทรด
> - **Confluence** — เหตุผลอิสระหลายข้อที่ชี้ไปที่ไม้เดียวกัน
> - **Bias ของ HTF** — ทิศทางที่อนุญาตตามเทรนด์ของไทม์เฟรมสูง *(ดู 2.2, 2.6)*
> - **Draw on liquidity** — กองที่ราคาน่าจะไปหา: เป้าหมายของคุณ *(ดู 5.1)*
> - **PD array** — FVG Order block หรือระดับอื่นที่ราคาอาจตอบสนอง *(ดู 5.3–5.5)*
> - **MSS / CHoCH** — การเปลี่ยนโครงสร้างที่พิสูจน์การกลับตัว *(ดู 2.3, 5.2)*
> - **CE** — เส้น 50% ของ FVG *(ดู 5.4)*
> - **Killzone** — ช่วงคึกคักของลอนดอนหรือ NY AM *(ดู 5.6)*
> - **R / R:R** — 1R = เงินที่เสียเมื่อโดน Stop  R:R = ผลตอบแทน ÷ ความเสี่ยง *(ดู 3.3)*
> - **ปิดกำไรบางส่วน (Partial profit)** — ปิดโพซิชันบางส่วนก่อน (เช่น ครึ่งหนึ่งที่ +2R)
> - **Stop ที่จุดคุ้มทุน (Break-even stop)** — เลื่อน Stop ไปที่ราคาเข้า ส่วนที่เหลือจึงไม่ขาดทุน
> - **ค่าคาดหวัง (Expectancy)** — ผลเฉลี่ยต่อไม้เป็น R: %ชนะ × กำไรเฉลี่ย − %แพ้ × ขาดทุนเฉลี่ย *(ดู 3.4)*
> - **เทรดบนกระดาษ / ทดสอบไปข้างหน้า (Paper trading / Forward test)** — ทำตามโมเดลแบบเรียลไทม์โดยไม่ใช้เงินจริง หรือใช้ขนาดเล็กมาก เพื่อเก็บสถิติที่ซื่อสัตย์
""")
L.before_heading("th", "3.", """
![[p5-model-flow.th.svg]]

> [!analogy]
> โมเดลนี้เหมือน **เช็กลิสต์ก่อนบินของนักบิน** นักบินไม่ข้าม "ตรวจน้ำมันแล้ว" เพราะอากาศดูดี ทุกข้อถูกอ่านออกเสียง และคำตอบ "ไม่" ข้อเดียวหมายถึงเครื่องบินอยู่บนพื้น ความปลอดภัยส่วนใหญ่มาจากวินัยที่น่าเบื่อของรายการ ไม่ใช่จากพรสวรรค์ของนักบิน
>
> **จุดที่เปรียบเทียบไม่ได้:** เช็กลิสต์ก่อนบินครอบคลุมสิ่งที่ตัดสินความปลอดภัยจริง ๆ แต่เช็กลิสต์การเทรดแค่เพิ่มโอกาส ไม้ที่ผ่านครบแปดข้อก็ยังขาดทุนได้ และคุณต้องเทรดหลายไม้กว่าจะรู้ว่ารายการนี้ได้ผลหรือไม่

> [!walkthrough] ไล่ทีละขั้น: ตัวอย่างจริงเป็นเงิน รวมทุกผลลัพธ์
> บัญชี **10,000 ดอลลาร์** เสี่ยง **1% = 100 ดอลลาร์** เข้า **105.25** Stop **101.9** → ความเสี่ยงต่อหน่วย **3.35**
> 1. **ขนาด:** 100 ÷ 3.35 = 29.85 → ปัดลงเป็น **29 หน่วย** ความเสี่ยงจริง = 29 × 3.35 = **97.15 ดอลลาร์** (≈1R)
> 2. **ผลลัพธ์ A ได้ผล:** ปิดครึ่ง (14 หน่วย) ที่ +2R (**111.95**): 14 × 6.70 = **93.80** เลื่อน Stop ไปจุดคุ้มทุน อีก 15 หน่วยไปถึง **113.95**: 15 × 8.70 = **130.50** รวม **224.30 ดอลลาร์** = **+2.31R**
> 3. **ผลลัพธ์ B ได้ผลครึ่งเดียว:** ปิดครึ่งที่ +2R (+93.80) แล้วราคากลับมา ส่วนที่เหลือโดน Stop ที่จุดคุ้มทุน (0) รวม **+93.80 ดอลลาร์** = **+0.97R**
> 4. **ผลลัพธ์ C ล้มเหลว:** ราคาปิดใต้จุดกวาดและโดน **101.9** ก่อนถึง +2R: **−97.15 ดอลลาร์** = **−1R** การกวาดนั้นจริง ๆ คือการวิ่งทะลุ ห้ามเทรดแก้แค้น รอ Setup ใหม่ทั้งหมด
> 5. **ผลลัพธ์ D ไม่ได้เข้า:** ราคาไม่ย่อกลับมาที่ 105.25 ยกเลิกคำสั่ง อย่าไล่ราคา ผล **0**
> 6. **แล้วไง?** ก่อนเข้า คุณรู้ผลของทุกทางแยกแล้ว การตัดสินใจเดียวที่เหลือระหว่างเทรดคือทำตามแผน

> [!check]- เช็กความเข้าใจ: ตัวอย่างจริง
> **Q1.** บัญชีของคุณ 5,000 ดอลลาร์ จุดเข้าและ Stop เดิม เสี่ยง 1% ได้กี่หน่วย?
> > [!answer]-
> > ความเสี่ยง = 50 ดอลลาร์ 50 ÷ 3.35 = 14.9 → 14 หน่วย (ความเสี่ยงจริง 46.90 ดอลลาร์)
> **Q2.** หลังปิดครึ่งที่ +2R ราคากลับมาที่จุดเข้า ทำไมไม้นี้จึงเป็น +0.97R ไม่ใช่ขาดทุน?
> > [!answer]-
> > ครึ่งหนึ่งของโพซิชันปิดไปแล้วที่ +2R และ Stop ของส่วนที่เหลือถูกเลื่อนไปจุดคุ้มทุน ครึ่งหลังจึงปิดที่ศูนย์
""")
L.before_callout("th", "action", """
> [!walkthrough] ไล่ทีละขั้น: ตัดสินโมเดลจากสถิติ ไม่ใช่จากไม้เดียว
> คุณเทรดโมเดลบนกระดาษ **30 Setup** (ตัวเลขประกอบการอธิบาย)
> 1. **ผล:** ชนะ 12 ไม้ เฉลี่ย **+2.6R** = +31.2R แพ้ 18 ไม้ที่ **−1R** = −18R
> 2. **สุทธิ:** 31.2 − 18 = **+13.2R** ใน 30 ไม้
> 3. **ค่าคาดหวัง** = 13.2 ÷ 30 = **+0.44R ต่อไม้** (เท่ากับ 0.4 × 2.6 − 0.6 × 1)
> 4. **หลังหักต้นทุน** (Spread ค่าคอมมิชชัน Slippage) สมมติ 0.1R ต่อไม้: 0.44 − 0.10 = **+0.34R**
> 5. **แล้วไง?** อัตราชนะ 40% ใช้ได้ถ้าไม้ชนะใหญ่พอ แต่ 30 ไม้เป็นตัวอย่างที่เล็ก *(ดู 9.3)* ให้ถือว่า +0.34R "น่าสนใจ" บันทึกต่อไป และเพิ่มขนาดเมื่อ 100+ ไม้ยืนยันแล้วเท่านั้น

> [!check]- เช็กความเข้าใจ: สถิติ
> **Q1.** ใน 20 ไม้ โมเดลชนะ 6 ไม้ที่ +2.5R และแพ้ 14 ไม้ที่ −1R ค่าคาดหวังเท่าไหร่?
> > [!answer]-
> > 6 × 2.5 = 15R; 14 × 1 = 14R; สุทธิ +1R ÷ 20 = +0.05R ต่อไม้ และน่าจะติดลบหลังหักต้นทุน ยังไม่ดีพอ

> [!market]
> - **ฟอเร็กซ์:** โมเดลนี้สร้างมาสำหรับ FX ใช้ London หรือ NY AM killzone และจุดสูง/ต่ำของเซสชันเป็นกองสภาพคล่อง *(ดู 5.6)*
> - **ทองคำ:** ทำงานแบบเดียวกัน แต่ Stop กว้าง (มัก 10–30 ดอลลาร์) โพซิชันจึงเล็ก เช็กปฏิทินข้อมูลสหรัฐ *(ดู 0.4)*
> - **หุ้นและฟิวเจอร์สดัชนี:** ใช้ช่วงซื้อขายปกติของสหรัฐ (20:30 UTC+7 ฤดูร้อน) Gap ข้ามคืนอาจข้ามขั้นที่ 4 ไปเลย *(ดู 0.5)*
> - **คริปโต:** 24/7 และใช้เลเวอเรจสูง การกวาดลึกกว่า จึงใช้ Stop กว้างขึ้นและขนาดเล็กลง และจำไว้ว่าราคาปิดรายวันคือ 07:00 UTC+7 *(ดู 0.7)*

> [!caution]
> โมเดลที่ดูดีบนกราฟในอดีตก็ยังขาดทุนในตลาดจริงได้: การมองย้อนหลังทำให้ทุกการกวาดและ FVG ดูชัดเจน และต้นทุนกับ Slippage ลืมได้ง่าย อย่าเทรดด้วยเงินจริงจนกว่าจะมี **Setup ที่ทดสอบไปข้างหน้าอย่างน้อย 30 ครั้ง** และแม้แต่ตอนนั้นก็เริ่มด้วยขนาดเพียงเศษเสี้ยวของปกติ เตรียมรับการแพ้ติดกัน: ที่อัตราชนะ 40% โอกาสที่จะแพ้ติดกันอย่างน้อย 6 ไม้สักช่วงหนึ่งใน 100 ไม้คือราว 87% และ 8 ไม้ติดราว 49% *(ดู 3.6)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกแปดขั้นตอนของโมเดลตามลำดับ
> > [!answer]-
> > Bias ของ HTF → Draw on liquidity (เป้าหมาย) → Discount/Premium → สภาพคล่องถูกเก็บ (การกวาด) → เวลา (Killzone) → แรงส่ง + MSS → เข้าที่ PD array (CE ของ FVG / OB) → ความเสี่ยง (Stop เลยจุดกวาด ขนาดสำหรับ 1R R:R ≥ 2)
> **Q2.** Setup ผ่านเจ็ดขั้น แต่ R:R ถึงเป้าหมายคือ 1.4 คุณทำอย่างไร?
> > [!answer]-
> > ข้าม ขั้นที่ขาดไปคือการกรองที่ทำงาน ไม่ใช่โชคร้าย
""")

L.set_meta("level", "v2")
L.save()
