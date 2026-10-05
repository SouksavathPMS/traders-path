"""B9a · v2 upgrade of 1.3 Candlestick Anatomy (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("01 Foundations/1.3 Candlestick Anatomy.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> A candle is a short summary of a period of trading, drawn with four prices: where it started, the highest and lowest points, and where it ended. The thick part (the body) shows who won the period. The thin lines (the wicks) show prices that were tried but pushed back. The ending price, the close, matters most.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **OHLC** — open, high, low, close: the four prices of a candle.
> - **Body** — the part between open and close; green/bullish if close > open, red/bearish if close < open.
> - **Wick (shadow)** — the thin lines above and below the body: prices visited but not accepted.
> - **Range** — high minus low.
> - **Close location** — where the close sits inside the range, from 0% (at the low) to 100% (at the high).
> - **Rejection** — a long wick showing one side pushed and failed.
> - **Conviction / indecision** — a big body with small wicks / a small body with wicks on both sides.
> - **Momentum** — candles getting bigger in one direction.
> - **Line chart / bar chart** — a chart of closes only / the same OHLC as candles drawn as bars.
""")
L.before_heading("en", "2.", """
> [!analogy]
> A candle is like the **final score of a football match**. "Home 3 – Away 1" tells you who won (the body), and the match report says the away team led early before collapsing (the wicks). You don't see every pass, but you know the result and where one side was pushed back.
>
> **Where it breaks:** a match ends at 90 minutes for everyone. A candle's "match" is just the timeframe you chose; on another timeframe the same trading gives a different score *(see 1.5)*.

> [!check]- Check your understanding: OHLC
> **Q1.** A candle has open 50, high 53, low 49, close 52. Draw it in words: colour, body size, each wick.
> > [!answer]-
> > Green (close 52 > open 50). Body 52 − 50 = **2**. Upper wick 53 − 52 = **1**. Lower wick 50 − 49 = **1**.
""")
L.before_heading("en", "4.", """
![[p1-close-location.en.svg]]

> [!walkthrough] Step by step: measuring a candle
> The candle from section 2: **O 100, H 104, L 97, C 103**.
> 1. **Range** = 104 − 97 = **7**.
> 2. **Body** = 103 − 100 = **3** (green). **Lower wick** = 100 − 97 = **3**. **Upper wick** = 104 − 103 = **1**.
> 3. **Close location** = (103 − 97) ÷ 7 = 6 ÷ 7 ≈ **86%** → in the top 25%: strong.
> 4. The lower wick (3) is 3× the upper wick (1): sellers were the side that got rejected.
> 5. **So what?** Two numbers, body size and close location, turn "it looks bullish" into something you can measure and log.

> [!check]- Check your understanding: body vs wick
> **Q1.** O 80, H 81, L 74, C 75. What's the close location, and who won?
> > [!answer]-
> > (75 − 74) ÷ (81 − 74) = 1 ÷ 7 ≈ **14%**: bottom 25%. Red candle, sellers won and closed near the low.
""")
L.before_callout("en", "action", """
> [!check]- Check your understanding: sequences
> **Q1.** Five green candles in a row, each body smaller than the last and with growing upper wicks. What is the market telling you?
> > [!answer]-
> > The push up is losing energy: buyers are still trying, but each attempt is rejected higher up. It's a warning, not yet a reversal.

> [!market]
> - **Forex:** daily candles usually close at 17:00 New York = **04:00 UTC+7** (05:00 in northern winter); brokers in other time zones show different daily candles *(see 0.3)*.
> - **Gold:** same daily close as forex at most brokers; wicks are often long around US data *(see 0.4)*.
> - **Stocks:** candles follow exchange hours, so overnight news shows up as a gap between one close and the next open *(see 0.5)*.
> - **Crypto:** daily candles usually close at 00:00 UTC = **07:00 UTC+7** and there are no weekend gaps *(see 0.7)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Why is the close the most important of the four prices?
> > [!answer]-
> > It's where the fight ended: the price both sides accepted at the end of the period. Highs and lows were only visited.
> **Q2.** A candle has a big red body and a close location of 5%. Is the minute before the close a good moment to judge it? Why or why not?
> > [!answer]-
> > No: until the candle closes, its shape can still change completely. Judge candles only after they close.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> แท่งเทียนคือสรุปสั้น ๆ ของการซื้อขายในช่วงเวลาหนึ่ง วาดด้วยสี่ราคา: ราคาเริ่ม จุดสูงสุดและต่ำสุด และราคาจบ ส่วนหนา (ตัวแท่ง) บอกว่าใครชนะในช่วงนั้น เส้นบาง (ไส้) บอกราคาที่ถูกลองแต่ถูกดันกลับ ราคาจบหรือราคาปิดสำคัญที่สุด
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **OHLC** — เปิด สูงสุด ต่ำสุด ปิด: สี่ราคาของแท่งเทียน
> - **ตัวแท่ง (Body)** — ส่วนระหว่างราคาเปิดกับปิด เขียว/ขาขึ้นถ้าปิด > เปิด แดง/ขาลงถ้าปิด < เปิด
> - **ไส้ (Wick / Shadow)** — เส้นบางเหนือและใต้ตัวแท่ง: ราคาที่ไปถึงแต่ไม่ถูกยอมรับ
> - **กรอบ (Range)** — สูงสุดลบต่ำสุด
> - **ตำแหน่งปิด (Close location)** — ราคาปิดอยู่ตรงไหนในกรอบ จาก 0% (ที่จุดต่ำสุด) ถึง 100% (ที่จุดสูงสุด)
> - **การปฏิเสธ (Rejection)** — ไส้ยาวที่แสดงว่าฝ่ายหนึ่งดันแล้วล้มเหลว
> - **ความมั่นใจ / ความลังเล (Conviction / Indecision)** — ตัวแท่งใหญ่ไส้สั้น / ตัวแท่งเล็กมีไส้ทั้งสองด้าน
> - **โมเมนตัม (Momentum)** — แท่งเทียนใหญ่ขึ้นเรื่อย ๆ ในทิศทางเดียว
> - **กราฟเส้น / กราฟแท่ง (Line chart / Bar chart)** — กราฟของราคาปิดเท่านั้น / OHLC เหมือนแท่งเทียนแต่วาดเป็นแท่งเส้น
""")
L.before_heading("th", "2.", """
> [!analogy]
> แท่งเทียนเหมือน **ผลสกอร์สุดท้ายของการแข่งฟุตบอล** "เจ้าบ้าน 3 – ทีมเยือน 1" บอกว่าใครชนะ (ตัวแท่ง) และรายงานการแข่งขันบอกว่าทีมเยือนนำก่อนแล้วพังทีหลัง (ไส้) คุณไม่เห็นทุกจังหวะส่งบอล แต่รู้ผลและรู้ว่าฝ่ายไหนถูกดันกลับตรงไหน
>
> **จุดที่เปรียบเทียบไม่ได้:** ฟุตบอลจบที่ 90 นาทีสำหรับทุกคน แต่ "การแข่ง" ของแท่งเทียนคือไทม์เฟรมที่คุณเลือก ในไทม์เฟรมอื่น การซื้อขายชุดเดียวกันให้สกอร์ต่างกัน *(ดู 1.5)*

> [!check]- เช็กความเข้าใจ: OHLC
> **Q1.** แท่งเทียนเปิด 50 สูงสุด 53 ต่ำสุด 49 ปิด 52 อธิบายเป็นคำ: สี ขนาดตัวแท่ง และไส้แต่ละด้าน
> > [!answer]-
> > เขียว (ปิด 52 > เปิด 50) ตัวแท่ง 52 − 50 = **2** ไส้บน 53 − 52 = **1** ไส้ล่าง 50 − 49 = **1**
""")
L.before_heading("th", "4.", """
![[p1-close-location.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: วัดแท่งเทียน
> แท่งจากหัวข้อ 2: **เปิด 100 สูงสุด 104 ต่ำสุด 97 ปิด 103**
> 1. **กรอบ** = 104 − 97 = **7**
> 2. **ตัวแท่ง** = 103 − 100 = **3** (เขียว) **ไส้ล่าง** = 100 − 97 = **3** **ไส้บน** = 104 − 103 = **1**
> 3. **ตำแหน่งปิด** = (103 − 97) ÷ 7 = 6 ÷ 7 ≈ **86%** → อยู่ใน 25% บน: แข็งแรง
> 4. ไส้ล่าง (3) ยาวเป็น 3 เท่าของไส้บน (1): ผู้ขายคือฝ่ายที่ถูกปฏิเสธ
> 5. **แล้วไง?** ตัวเลขสองตัว ขนาดตัวแท่งและตำแหน่งปิด เปลี่ยน "ดูเหมือนขาขึ้น" ให้เป็นสิ่งที่วัดและบันทึกได้

> [!check]- เช็กความเข้าใจ: ตัวแท่ง vs ไส้
> **Q1.** เปิด 80 สูงสุด 81 ต่ำสุด 74 ปิด 75 ตำแหน่งปิดเท่าไร และใครชนะ?
> > [!answer]-
> > (75 − 74) ÷ (81 − 74) = 1 ÷ 7 ≈ **14%**: อยู่ใน 25% ล่าง แท่งแดง ผู้ขายชนะและปิดใกล้จุดต่ำสุด
""")
L.before_callout("th", "action", """
> [!check]- เช็กความเข้าใจ: อ่านเป็นลำดับ
> **Q1.** แท่งเขียวห้าแท่งติดกัน แต่ละแท่งตัวเล็กลงและไส้บนยาวขึ้น ตลาดกำลังบอกอะไร?
> > [!answer]-
> > แรงดันขึ้นกำลังหมด: ผู้ซื้อยังพยายาม แต่ทุกครั้งถูกปฏิเสธที่ราคาสูงขึ้น เป็นสัญญาณเตือน ยังไม่ใช่การกลับตัว

> [!market]
> - **ฟอเร็กซ์:** แท่งรายวันมักปิด 17:00 นิวยอร์ก = **04:00 UTC+7** (05:00 ช่วงฤดูหนาวซีกโลกเหนือ) โบรกเกอร์ในเขตเวลาอื่นจะแสดงแท่งรายวันต่างกัน *(ดู 0.3)*
> - **ทองคำ:** ปิดรายวันเหมือนฟอเร็กซ์ในโบรกเกอร์ส่วนใหญ่ ไส้มักยาวช่วงข้อมูลสหรัฐ *(ดู 0.4)*
> - **หุ้น:** แท่งเทียนตามเวลาทำการของตลาด ข่าวข้ามคืนจึงปรากฏเป็น Gap ระหว่างราคาปิดกับราคาเปิดถัดไป *(ดู 0.5)*
> - **คริปโต:** แท่งรายวันมักปิด 00:00 UTC = **07:00 UTC+7** และไม่มี Gap ช่วงสุดสัปดาห์ *(ดู 0.7)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** ทำไมราคาปิดจึงสำคัญที่สุดในสี่ราคา?
> > [!answer]-
> > เป็นจุดที่การต่อสู้จบ: ราคาที่ทั้งสองฝ่ายยอมรับตอนสิ้นช่วง ส่วนจุดสูงและต่ำเป็นแค่ที่ราคาไปถึง
> **Q2.** แท่งเทียนตัวแดงใหญ่และตำแหน่งปิด 5% หนึ่งนาทีก่อนปิดแท่งเป็นจังหวะที่ดีในการตัดสินไหม? ทำไม?
> > [!answer]-
> > ไม่ใช่ จนกว่าแท่งจะปิด รูปร่างยังเปลี่ยนได้ทั้งหมด ตัดสินแท่งเทียนหลังปิดแล้วเท่านั้น
""")

L.set_meta("level", "v2")
L.save()
