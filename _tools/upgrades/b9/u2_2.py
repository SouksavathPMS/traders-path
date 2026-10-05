"""B9b · v2 upgrade of 2.2 Trends, Ranges & Market Cycles (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("02 Market Structure/2.2 Trends, Ranges & Market Cycles.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> A market is either going somewhere (a trend) or going sideways between a floor and a ceiling (a range). Each needs a different plan: in a trend you join the direction after small dips; in a range you buy near the floor and sell near the ceiling. Most mistakes come from using the trend plan in a range, or the range plan in a trend.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Trend** — a market making HH + HL (up) or LH + LL (down) *(see 2.1)*.
> - **Range** — price moving between a roughly flat ceiling and floor.
> - **Balance / imbalance** — buyers and sellers agree on value / one side is more urgent *(see 7.1)*.
> - **Breakout** — price closing outside a range or beyond a key level.
> - **Healthy vs tired trend** — strong impulses with shallow pullbacks vs shrinking impulses and deeper pullbacks.
> - **Wyckoff cycle** — accumulation → markup → distribution → markdown.
> - **Accumulation / distribution** — large players buying / selling inside a range.
> - **Markup / markdown** — the trending phase up / down after a range.
> - **Re-accumulation** — a range inside an uptrend that leads to continuation.
""")
L.before_heading("en", "2.", """
> [!analogy]
> Trends and ranges are like **driving and parking**. On the highway (a trend) you keep going with the traffic and only change lanes carefully. In a car park (a range) you move slowly between clear lines. Driving at highway speed in a car park, or parking on the highway, is how accidents happen.
>
> **Where it breaks:** you know when you're on a highway. In markets you often only know the state for sure after it has changed, so you act on the best current reading and accept being wrong sometimes.

> [!walkthrough] Step by step: why you never trade the middle of a range
> Range from the example below (section 3): floor **100**, ceiling **106**, stop under the floor at **99**, target near the ceiling at **105**.
> 1. **Buy near the floor at 100.5:** risk 100.5 − 99 = **1.5**, reward 105 − 100.5 = **4.5** → **3R**.
> 2. **Buy in the middle at 103:** risk 103 − 99 = **4**, reward 105 − 103 = **2** → **0.5R**.
> 3. Same idea, same stop, same target, but the middle entry risks almost 3× more to make less than half as much.
> 4. **So what?** In a range, the location is the edge. Without a price near a boundary, there's no trade.

> [!check]- Check your understanding: the three states
> **Q1.** Highs: 75.2, 75.0, 75.3. Lows: 71.1, 70.9, 71.0. What's the state, and what is allowed?
> > [!answer]-
> > Highs and lows roughly equal → **range** with a ceiling near 75 and a floor near 71. Buy near the floor, sell near the ceiling, or wait. Never the middle.
""")
L.before_heading("en", "3.", """
![[p2-trend-health.en.svg]]

> [!walkthrough] Step by step: measuring trend health
> Divide each pullback by the impulse before it (illustrative legs).
> 1. **Healthy:** impulses +8, +9, +8; pullbacks −3, −3, −2.5 → ratios **0.38, 0.33, 0.31**: pullbacks stay small.
> 2. **Tired:** impulses +8, +5, +3; pullbacks −3, −4, −3 → ratios **0.38, 0.80, 1.00**: the last pullback erased the whole impulse.
> 3. Highs in the tired trend: 108 → 110 → **109**, the last high failed.
> 4. **So what?** Rising ratios tell you to stop adding and tighten management. They don't tell you to reverse: wait for structure to break *(see 2.3)*.

> [!check]- Check your understanding: trend health
> **Q1.** Impulse +6, pullback −5. Healthy or tired, and what do you do?
> > [!answer]-
> > Ratio 5 ÷ 6 ≈ 0.83: **tired**. Stop adding, manage open trades tightly, and wait for a break of structure before any reversal idea.
""")
L.before_callout("en", "example", """
> [!check]- Check your understanding: the cycle
> **Q1.** After a long uptrend, price goes sideways for weeks. What are the two possible outcomes, and how will you know which one?
> > [!answer]-
> > Continuation (re-accumulation) or reversal (distribution). The breakout tells you: a close above the range = continuation; a close below = likely markdown.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** major pairs spend much of their time in ranges; trends often start around London open and big data releases *(see 0.3)*.
> - **Gold:** strong multi-month trends with long ranges between them *(see 0.4)*.
> - **Stocks:** indices trend up over long periods; single stocks range for months before breaking on news or earnings *(see 0.5)*.
> - **Crypto:** long ranges followed by very fast trends; breakouts often fail at first *(see 0.7)*.

> [!caution]
> Many breakouts from a range fail and return inside, trapping traders who bought the first move with large size. And shorting a strong trend "because it went up a lot" can lose many R in a row. Size small at breakouts and wait for structure, not opinions.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Name the three states and the main rule for each.
> > [!answer]-
> > Uptrend: buy pullbacks, no shorts. Downtrend: sell rallies, no longs. Range: trade the edges or wait, never the middle.
> **Q2.** Range 50–56. You buy at 50.4 with a stop at 49.4. Target 55.4. What's the R:R?
> > [!answer]-
> > Risk 1.0, reward 5.0 → **5R**.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ตลาดอาจกำลังไปที่ไหนสักแห่ง (เทรนด์) หรือวิ่งออกข้างระหว่างพื้นกับเพดาน (กรอบราคา) แต่ละแบบต้องใช้แผนต่างกัน: ในเทรนด์ คุณเข้าร่วมทิศทางหลังการย่อเล็ก ๆ ในกรอบราคา คุณซื้อใกล้พื้นและขายใกล้เพดาน ความผิดพลาดส่วนใหญ่เกิดจากใช้แผนเทรนด์ในกรอบราคา หรือใช้แผนกรอบราคาในเทรนด์
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **เทรนด์ (Trend)** — ตลาดที่ทำ HH + HL (ขึ้น) หรือ LH + LL (ลง) *(ดู 2.1)*
> - **กรอบราคา (Range)** — ราคาวิ่งระหว่างเพดานและพื้นที่ค่อนข้างแบน
> - **สมดุล / ไม่สมดุล (Balance / Imbalance)** — ผู้ซื้อและผู้ขายเห็นตรงกันเรื่องมูลค่า / ฝ่ายหนึ่งเร่งรีบกว่า *(ดู 7.1)*
> - **การทะลุ (Breakout)** — ราคาปิดนอกกรอบราคาหรือเลยระดับสำคัญ
> - **เทรนด์แข็งแรง vs เหนื่อย (Healthy vs tired)** — แรงส่งแรงและการย่อตื้น vs แรงส่งหดลงและการย่อลึกขึ้น
> - **วัฏจักรไวคอฟฟ์ (Wyckoff cycle)** — สะสม → ขาขึ้น → แจกจ่าย → ขาลง
> - **การสะสม / การแจกจ่าย (Accumulation / Distribution)** — ผู้เล่นรายใหญ่ซื้อ / ขายภายในกรอบราคา
> - **Markup / Markdown** — ช่วงเทรนด์ขึ้น / ลงหลังกรอบราคา
> - **การสะสมซ้ำ (Re-accumulation)** — กรอบราคาภายในขาขึ้นที่นำไปสู่การไปต่อ
""")
L.before_heading("th", "2.", """
> [!analogy]
> เทรนด์และกรอบราคาเหมือน **การขับรถและการจอดรถ** บนทางด่วน (เทรนด์) คุณไปตามกระแสรถและเปลี่ยนเลนอย่างระวัง ในลานจอดรถ (กรอบราคา) คุณขยับช้า ๆ ระหว่างเส้นที่ชัดเจน ขับเร็วแบบทางด่วนในลานจอด หรือจอดรถบนทางด่วน คือที่มาของอุบัติเหตุ
>
> **จุดที่เปรียบเทียบไม่ได้:** คุณรู้ว่ากำลังอยู่บนทางด่วน แต่ในตลาด คุณมักรู้สภาวะแน่ชัดหลังจากมันเปลี่ยนไปแล้ว จึงต้องลงมือตามการอ่านที่ดีที่สุดในตอนนี้ และยอมรับว่าบางครั้งจะผิด

> [!walkthrough] ไล่ทีละขั้น: ทำไมไม่เทรดกลางกรอบราคา
> กรอบราคาจากตัวอย่างด้านล่าง (หัวข้อ 3): พื้น **100** เพดาน **106** Stop ใต้พื้นที่ **99** เป้าใกล้เพดานที่ **105**
> 1. **ซื้อใกล้พื้นที่ 100.5:** เสี่ยง 100.5 − 99 = **1.5** ผลตอบแทน 105 − 100.5 = **4.5** → **3R**
> 2. **ซื้อกลางกรอบที่ 103:** เสี่ยง 103 − 99 = **4** ผลตอบแทน 105 − 103 = **2** → **0.5R**
> 3. ไอเดียเดียวกัน Stop เดียวกัน เป้าเดียวกัน แต่การเข้ากลางกรอบเสี่ยงเกือบ 3 เท่า เพื่อได้น้อยกว่าครึ่ง
> 4. **แล้วไง?** ในกรอบราคา ตำแหน่งคือความได้เปรียบ ถ้าราคาไม่ได้อยู่ใกล้ขอบ ก็ไม่มีเทรด

> [!check]- เช็กความเข้าใจ: สภาวะ 3 แบบ
> **Q1.** จุดสูง: 75.2, 75.0, 75.3 จุดต่ำ: 71.1, 70.9, 71.0 สภาวะคืออะไร และอนุญาตให้ทำอะไร?
> > [!answer]-
> > จุดสูงและจุดต่ำใกล้เคียงกัน → **กรอบราคา** เพดานราว 75 พื้นราว 71 ซื้อใกล้พื้น ขายใกล้เพดาน หรือรอ ห้ามเทรดกลางกรอบ
""")
L.before_heading("th", "3.", """
![[p2-trend-health.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: วัดความแข็งแรงของเทรนด์
> หารการย่อแต่ละครั้งด้วยแรงส่งก่อนหน้า (ขาราคาตัวอย่าง)
> 1. **แข็งแรง:** แรงส่ง +8, +9, +8 การย่อ −3, −3, −2.5 → อัตราส่วน **0.38, 0.33, 0.31**: การย่อยังเล็ก
> 2. **เหนื่อย:** แรงส่ง +8, +5, +3 การย่อ −3, −4, −3 → อัตราส่วน **0.38, 0.80, 1.00**: การย่อครั้งล่าสุดลบแรงส่งหมด
> 3. จุดสูงในเทรนด์ที่เหนื่อย: 108 → 110 → **109** จุดสูงล่าสุดล้มเหลว
> 4. **แล้วไง?** อัตราส่วนที่เพิ่มขึ้นบอกให้หยุดเพิ่มโพซิชันและบริหารให้เข้มขึ้น ไม่ได้บอกให้กลับข้าง: รอให้โครงสร้างแตก *(ดู 2.3)*

> [!check]- เช็กความเข้าใจ: ความแข็งแรงของเทรนด์
> **Q1.** แรงส่ง +6 การย่อ −5 แข็งแรงหรือเหนื่อย และคุณทำอะไร?
> > [!answer]-
> > อัตราส่วน 5 ÷ 6 ≈ 0.83: **เหนื่อย** หยุดเพิ่มโพซิชัน บริหารไม้ที่เปิดอยู่ให้เข้ม และรอโครงสร้างแตกก่อนคิดเรื่องกลับตัว
""")
L.before_callout("th", "example", """
> [!check]- เช็กความเข้าใจ: วัฏจักร
> **Q1.** หลังขาขึ้นยาว ราคาวิ่งออกข้างหลายสัปดาห์ ผลที่เป็นไปได้สองแบบคืออะไร และคุณจะรู้ได้อย่างไรว่าเป็นแบบไหน?
> > [!answer]-
> > ไปต่อ (สะสมซ้ำ) หรือกลับตัว (แจกจ่าย) การทะลุจะบอก: ปิดเหนือกรอบ = ไปต่อ ปิดใต้กรอบ = น่าจะเป็นขาลง
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** คู่เงินหลักใช้เวลาส่วนใหญ่ในกรอบราคา เทรนด์มักเริ่มช่วงลอนดอนเปิดและการประกาศข้อมูลใหญ่ *(ดู 0.3)*
> - **ทองคำ:** เทรนด์แรงหลายเดือน คั่นด้วยกรอบราคายาว *(ดู 0.4)*
> - **หุ้น:** ดัชนีขึ้นเป็นเทรนด์ในระยะยาว หุ้นรายตัววิ่งในกรอบหลายเดือนก่อนทะลุจากข่าวหรืองบ *(ดู 0.5)*
> - **คริปโต:** กรอบราคายาวตามด้วยเทรนด์ที่เร็วมาก การทะลุมักล้มเหลวในครั้งแรก *(ดู 0.7)*

> [!caution]
> การทะลุกรอบราคาจำนวนมากล้มเหลวและกลับเข้ากรอบ ทำให้คนที่ซื้อการขยับแรกด้วยขนาดใหญ่ติดกับ และการ Short เทรนด์ที่แรง "เพราะขึ้นมาเยอะแล้ว" อาจเสียหลาย R ติดกัน ใช้ขนาดเล็กตอนทะลุ และรอโครงสร้าง ไม่ใช่ความเห็น
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกสภาวะสามแบบและกฎหลักของแต่ละแบบ
> > [!answer]-
> > ขาขึ้น: ซื้อตอนย่อ ห้าม Short ขาลง: ขายตอนเด้ง ห้ามซื้อ กรอบราคา: เทรดที่ขอบหรือรอ ห้ามเทรดกลางกรอบ
> **Q2.** กรอบราคา 50–56 คุณซื้อที่ 50.4 Stop ที่ 49.4 เป้า 55.4 R:R เท่าไร?
> > [!answer]-
> > เสี่ยง 1.0 ผลตอบแทน 5.0 → **5R**
""")

L.set_meta("level", "v2")
L.save()
