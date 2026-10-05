"""B9a · v2 upgrade of 1.5 Timeframes & Top-Down Analysis (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("01 Foundations/1.5 Timeframes & Top-Down Analysis.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> A timeframe is how much time one candle covers: one minute, one hour, one day. It's the same market seen from closer or further away. Look at the big picture first to see which way the market is going, then zoom in to find a good moment to join it. Going with the big picture is easier than fighting it.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Timeframe** — the time each candle represents (1m, 5m, 1H, 4H, D, W, M).
> - **HTF / MTF / LTF** — higher, middle and lower timeframe in your set of three.
> - **Top-down analysis** — reading the HTF first, then the MTF, then the LTF.
> - **Direction / location / trigger** — which way to trade / where to join / what makes you enter.
> - **Noise** — small, random moves that mean nothing on the bigger picture.
> - **Pullback** — a move against the trend before it continues.
> - **Swing trading / day trading / scalping** — holding days–weeks / minutes–hours / seconds–minutes.
> - **Timeframe hopping** — switching charts to find a reason to enter or to keep a losing trade.
> - **Alert** — a price notification from your platform.
""")
L.before_heading("en", "2.", """
> [!analogy]
> Timeframes are like the **zoom on a map app**. Zoomed out, you see that the road runs from Bangkok to Chiang Mai (the trend). Zoomed in, you see every bend and traffic light (the noise). You pick the route zoomed out and drive the next turn zoomed in.
>
> **Where it breaks:** a map doesn't change while you look at it. Markets do: the HTF picture can change, so check it again regularly instead of setting it once.

> [!check]- Check your understanding: zoom levels
> **Q1.** A 1-hour candle is green with a long lower wick. What do its four 15-minute candles probably look like?
> > [!answer]-
> > Price fell early in the hour (red 15m candle(s) making the low), then recovered (green 15m candles), closing near the top. Same data, more detail.
""")
L.before_heading("en", "3.", """
> [!check]- Check your understanding: choosing timeframes
> **Q1.** Is 1H → 4H → Daily a sensible set of three? Check the ratios.
> > [!answer]-
> > 4H ÷ 1H = **4×**; Daily ÷ 4H = **6×** (24 hours ÷ 4). Both are within the 4–6× rule, so yes.
""")
L.before_heading("en", "4.", """
![[p1-stop-by-tf.en.svg]]

> [!walkthrough] Step by step: why the trigger timeframe matters
> Direction from the daily chart: up. Entry **100**, target **104** (next daily level), fixed risk **100 USD** (illustrative).
> 1. **5m trigger:** stop under the 5m low at **99.5** → risk 0.5 → R:R = 4 ÷ 0.5 = **8**; size = 100 ÷ 0.5 = **200 units**.
> 2. **1H trigger:** stop **98.5** → risk 1.5 → R:R ≈ **2.7**; size ≈ **67 units**.
> 3. **Daily trigger:** stop **96** → risk 4 → R:R = **1**; size = **25 units**.
> 4. **So what?** The HTF gives the direction and the target; a lower-timeframe trigger gives a tighter stop and a better R:R. The cost: tighter stops get hit by noise more often, so the win rate is lower.

> [!check]- Check your understanding: top-down
> **Q1.** Put these in order and name each step: "bullish engulfing on 1H", "daily uptrend", "4H pullback into demand".
> > [!answer]-
> > Daily uptrend (**direction**) → 4H pullback into demand (**location**) → bullish engulfing on 1H (**trigger**).
""")
L.before_callout("en", "action", """
> [!check]- Check your understanding: disagreement
> **Q1.** The daily trend is down, and the 15m chart shows a strong bounce. What does the table say to do?
> > [!answer]-
> > Don't buy the bounce. Wait for it to fail at resistance, then look for sells in the daily direction.

> [!market]
> - **Forex:** the daily candle closes at 04:00 UTC+7 (05:00 in northern winter); your daily chart depends on your broker's server time *(see 0.3)*.
> - **Gold:** fast intraday moves around US data make 1m–5m charts very noisy; start with 1H and above *(see 0.4)*.
> - **Stocks:** daily and weekly charts include overnight gaps that intraday charts show as jumps *(see 0.5)*.
> - **Crypto:** 24/7 markets, so a "daily" candle has no natural close; most exchanges use 00:00 UTC = 07:00 UTC+7 *(see 0.7)*.

> [!caution]
> Small timeframes allow tight stops, which tempts traders into large positions. A tight stop with a big position can be hit by one spike or slippage and lose much more than planned. Size every trade from the stop distance (Phase 3), not from the excitement of a setup.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Name the three steps of top-down analysis and which timeframe each uses.
> > [!answer]-
> > Direction on the HTF, location on the MTF, trigger on the LTF.
> **Q2.** Entry 50, target 56 from the HTF. A 15m trigger allows a stop at 49; a 4H trigger needs a stop at 47. What's the R:R of each?
> > [!answer]-
> > 15m: 6 ÷ 1 = **6**. 4H: 6 ÷ 3 = **2**.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ไทม์เฟรมคือระยะเวลาที่แท่งเทียนหนึ่งแท่งครอบคลุม: หนึ่งนาที หนึ่งชั่วโมง หนึ่งวัน เป็นตลาดเดียวกันที่มองจากใกล้หรือไกล ดูภาพใหญ่ก่อนเพื่อเห็นว่าตลาดไปทางไหน แล้วซูมเข้าไปหาจังหวะดี ๆ เพื่อเข้าร่วม การไปตามภาพใหญ่ง่ายกว่าการสู้กับมัน
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **ไทม์เฟรม (Timeframe)** — เวลาที่แท่งเทียนแต่ละแท่งแทน (1m, 5m, 1H, 4H, D, W, M)
> - **HTF / MTF / LTF** — ไทม์เฟรมใหญ่ กลาง และเล็ก ในชุดสามไทม์เฟรมของคุณ
> - **วิเคราะห์จากบนลงล่าง (Top-down analysis)** — อ่าน HTF ก่อน แล้ว MTF แล้ว LTF
> - **ทิศทาง / ตำแหน่ง / จังหวะเข้า (Direction / Location / Trigger)** — เทรดทางไหน / เข้าร่วมตรงไหน / อะไรทำให้เข้า
> - **สัญญาณรบกวน (Noise)** — การขยับเล็ก ๆ แบบสุ่มที่ไม่มีความหมายในภาพใหญ่
> - **การย่อตัว (Pullback)** — การขยับสวนเทรนด์ก่อนที่เทรนด์จะไปต่อ
> - **Swing trading / Day trading / Scalping** — ถือหลายวันถึงหลายสัปดาห์ / หลายนาทีถึงหลายชั่วโมง / หลายวินาทีถึงหลายนาที
> - **กระโดดไทม์เฟรม (Timeframe hopping)** — สลับกราฟเพื่อหาเหตุผลเข้า หรือเพื่อถือไม้ที่ขาดทุนต่อ
> - **การแจ้งเตือน (Alert)** — การแจ้งเตือนราคาจากแพลตฟอร์ม
""")
L.before_heading("th", "2.", """
> [!analogy]
> ไทม์เฟรมเหมือน **การซูมในแอปแผนที่** ซูมออก คุณเห็นว่าถนนวิ่งจากกรุงเทพฯ ไปเชียงใหม่ (เทรนด์) ซูมเข้า คุณเห็นทุกโค้งและไฟแดง (สัญญาณรบกวน) คุณเลือกเส้นทางตอนซูมออก และขับโค้งถัดไปตอนซูมเข้า
>
> **จุดที่เปรียบเทียบไม่ได้:** แผนที่ไม่เปลี่ยนขณะที่คุณดู แต่ตลาดเปลี่ยน ภาพ HTF อาจเปลี่ยนได้ จึงต้องตรวจซ้ำเป็นประจำ ไม่ใช่ตั้งครั้งเดียวจบ

> [!check]- เช็กความเข้าใจ: ระดับการซูม
> **Q1.** แท่งเทียน 1 ชั่วโมงเป็นสีเขียวมีไส้ล่างยาว แท่ง 15 นาทีทั้งสี่แท่งข้างในน่าจะเป็นอย่างไร?
> > [!answer]-
> > ราคาลงช่วงต้นชั่วโมง (แท่ง 15m สีแดงที่ทำจุดต่ำ) แล้วฟื้นตัว (แท่ง 15m สีเขียว) ปิดใกล้จุดสูง ข้อมูลเดียวกัน รายละเอียดมากขึ้น
""")
L.before_heading("th", "3.", """
> [!check]- เช็กความเข้าใจ: เลือกไทม์เฟรม
> **Q1.** 1H → 4H → Daily เป็นชุดสามไทม์เฟรมที่เหมาะสมไหม? ตรวจอัตราส่วน
> > [!answer]-
> > 4H ÷ 1H = **4 เท่า** Daily ÷ 4H = **6 เท่า** (24 ชั่วโมง ÷ 4) ทั้งสองอยู่ในกฎ 4–6 เท่า จึงเหมาะสม
""")
L.before_heading("th", "4.", """
![[p1-stop-by-tf.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ทำไมไทม์เฟรมของสัญญาณเข้าจึงสำคัญ
> ทิศทางจากกราฟรายวัน: ขึ้น เข้าที่ **100** เป้า **104** (ระดับรายวันถัดไป) ความเสี่ยงคงที่ **100 ดอลลาร์** (ตัวอย่าง)
> 1. **สัญญาณบน 5m:** Stop ใต้จุดต่ำ 5m ที่ **99.5** → เสี่ยง 0.5 → R:R = 4 ÷ 0.5 = **8** ขนาด = 100 ÷ 0.5 = **200 หน่วย**
> 2. **สัญญาณบน 1H:** Stop **98.5** → เสี่ยง 1.5 → R:R ≈ **2.7** ขนาด ≈ **67 หน่วย**
> 3. **สัญญาณบนรายวัน:** Stop **96** → เสี่ยง 4 → R:R = **1** ขนาด = **25 หน่วย**
> 4. **แล้วไง?** HTF ให้ทิศทางและเป้า สัญญาณบนไทม์เฟรมเล็กให้ Stop ที่แคบกว่าและ R:R ที่ดีกว่า ต้นทุนคือ Stop แคบถูกสัญญาณรบกวนชนบ่อยกว่า อัตราชนะจึงต่ำลง

> [!check]- เช็กความเข้าใจ: จากบนลงล่าง
> **Q1.** เรียงลำดับและบอกชื่อแต่ละขั้น: "Bullish engulfing บน 1H", "เทรนด์ขาขึ้นรายวัน", "4H ย่อลงเข้าโซน Demand"
> > [!answer]-
> > เทรนด์ขาขึ้นรายวัน (**ทิศทาง**) → 4H ย่อลงเข้าโซน Demand (**ตำแหน่ง**) → Bullish engulfing บน 1H (**จังหวะเข้า**)
""")
L.before_callout("th", "action", """
> [!check]- เช็กความเข้าใจ: เมื่อขัดแย้งกัน
> **Q1.** เทรนด์รายวันเป็นขาลง และกราฟ 15m แสดงการเด้งแรง ตารางบอกให้ทำอะไร?
> > [!answer]-
> > อย่าซื้อตอนเด้ง รอให้การเด้งล้มเหลวที่แนวต้าน แล้วมองหาจังหวะขายตามทิศทางรายวัน

> [!market]
> - **ฟอเร็กซ์:** แท่งรายวันปิด 04:00 UTC+7 (05:00 ช่วงฤดูหนาวซีกโลกเหนือ) กราฟรายวันของคุณขึ้นกับเวลาเซิร์ฟเวอร์ของโบรกเกอร์ *(ดู 0.3)*
> - **ทองคำ:** การขยับเร็วระหว่างวันช่วงข้อมูลสหรัฐทำให้กราฟ 1m–5m มีสัญญาณรบกวนมาก เริ่มที่ 1H ขึ้นไป *(ดู 0.4)*
> - **หุ้น:** กราฟรายวันและรายสัปดาห์รวม Gap ข้ามคืน ซึ่งกราฟระหว่างวันแสดงเป็นการกระโดด *(ดู 0.5)*
> - **คริปโต:** ตลาด 24/7 แท่ง "รายวัน" จึงไม่มีเวลาปิดตามธรรมชาติ กระดานเทรดส่วนใหญ่ใช้ 00:00 UTC = 07:00 UTC+7 *(ดู 0.7)*

> [!caution]
> ไทม์เฟรมเล็กทำให้ตั้ง Stop แคบได้ ซึ่งล่อให้นักเทรดเปิดโพซิชันใหญ่ Stop แคบกับโพซิชันใหญ่อาจโดนการพุ่งครั้งเดียวหรือ Slippage และเสียมากกว่าที่วางแผนมาก กำหนดขนาดทุกไม้จากระยะ Stop (เฟส 3) ไม่ใช่จากความตื่นเต้นกับ Setup
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกสามขั้นของการวิเคราะห์จากบนลงล่าง และแต่ละขั้นใช้ไทม์เฟรมไหน
> > [!answer]-
> > ทิศทางบน HTF ตำแหน่งบน MTF จังหวะเข้าบน LTF
> **Q2.** เข้าที่ 50 เป้า 56 จาก HTF สัญญาณ 15m ให้ตั้ง Stop ที่ 49 สัญญาณ 4H ต้องตั้ง Stop ที่ 47 R:R ของแต่ละแบบเท่าไร?
> > [!answer]-
> > 15m: 6 ÷ 1 = **6** 4H: 6 ÷ 3 = **2**
""")

L.set_meta("level", "v2")
L.save()
