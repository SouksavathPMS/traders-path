"""B9b · v2 upgrade of 2.4 Support, Resistance & Role Reversal (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("02 Market Structure/2.4 Support, Resistance & Role Reversal.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Support is a price area where falling prices stopped before, because buyers showed up. Resistance is where rising prices stopped, because sellers showed up. People remember these prices and leave orders there again, so price often reacts there. But every visit uses up some of those orders, and when a level finally breaks, it often swaps roles.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Support / resistance (S/R)** — price areas where buyers / sellers stopped price before.
> - **Zone** — a price band, not a single line, from the wick extremes to where the bodies cluster.
> - **Test** — price returning to a level.
> - **Confluence** — several reasons for a level at the same price (round number, previous high, role reversal).
> - **Role reversal** — broken resistance becoming support, or broken support becoming resistance.
> - **Bounce** — trading a rejection at a level in the trend direction.
> - **Break & retest** — trading the first pullback to a level that was broken with a close.
> - **Failed break** — price wicks through a level but closes back inside *(see 5.2)*.
> - **Round number** — a price like 100, 1.1000 or 2,000 that many people watch.
""")
L.before_heading("en", "2.", """
> [!analogy]
> A level is like a **popular street-food stall's "sold out at 8 pm"**: people remember it and arrive early next time. But the stall has only so many bowls. If huge crowds come again and again, it runs out sooner, and one evening there's nothing left to stop the queue.
>
> **Where it breaks:** a stall restocks every day. A price level doesn't refill by itself; new orders only arrive if traders still care about that price.

> [!check]- Check your understanding: why levels exist
> **Q1.** Name two groups of traders who add buy orders at a support level, and why.
> > [!answer]-
> > For example: buyers who missed the last bounce (want a second chance), and short sellers whose stops or profit-taking orders sit there (they must buy to close).
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: drawing a zone instead of a line
> Three bounces from the same area (illustrative): wick lows **98.6, 98.9, 99.1**; candle bodies cluster at **99.4–99.7**.
> 1. Zone = lowest wick to top of the body cluster = **98.6–99.7** (1.1 wide).
> 2. A "line" at **99.0** with a stop at 98.9 would have been hit by the **98.6** wick, even though the level held.
> 3. With the zone, the stop goes beyond it: **98.4**. Buying a rejection that closes at **100.2** risks **1.8**.
> 4. **So what?** A zone accepts that orders sit across a band of prices. Wider stops mean smaller size (Phase 3), but far fewer "right idea, stopped by noise" losses.

> [!check]- Check your understanding: grading zones
> **Q1.** A 15m support from 2 years ago, tested 4 times last week, with no confluence. Strong or weak? Why?
> > [!answer]-
> > Weak on almost every factor: small timeframe, old, heavily tested (orders used up), no confluence. Delete it or treat it as minor.
""")
L.before_heading("en", "4.", """
> [!check]- Check your understanding: role reversal
> **Q1.** Support at 50 breaks with a daily close at 48. Price rallies back to 49.8. What do you expect, and why?
> > [!answer]-
> > Old support may act as **resistance**: buyers who bought at 50 are now in loss and want to sell at break-even, and missed sellers want a second chance. Watch for a rejection to sell.
""")
L.before_callout("en", "action", """
![[p2-retest-vs-chase.en.svg]]

> [!walkthrough] Step by step: chasing vs waiting for the retest
> The breakout from the example: old zone **109.2–110.6**, stop under it at **108.9**, target **117**, risk **100 USD** per trade.
> 1. **Chase at 114** (after the breakout is "obvious"): risk 5.1, reward 3.0 → **0.6R**; size 100 ÷ 5.1 ≈ **20 units**, +59 USD at target.
> 2. **Buy the retest at 110.6:** risk 1.7, reward 6.4 → **3.8R**; size ≈ **59 units**, +376 USD at target.
> 3. Same idea, same stop, same target: the retest has about **6×** the R:R.
> 4. **So what?** The retest costs you nothing but patience. The risk is that price never comes back; then you simply miss the trade, which is cheaper than chasing.

> [!check]- Check your understanding: three plays
> **Q1.** Price wicks 0.5 above resistance and closes back below it. Which play is this, and where does the stop go?
> > [!answer]-
> > A **failed break**: sell after the close back inside, stop beyond the wick extreme.

> [!market]
> - **Forex:** round numbers (1.1000, 150.00) and the previous day's high and low are widely watched levels *(see 0.3)*.
> - **Gold:** round numbers every 50 and 100 USD often act as levels *(see 0.4)*.
> - **Stocks:** previous highs, IPO prices and round numbers; earnings gaps can jump straight through levels *(see 0.5)*.
> - **Crypto:** round numbers (e.g. every 1,000 or 10,000 USD) attract many orders and stops *(see 0.7)*.

> [!caution]
> Levels are not walls. A stop placed exactly at an obvious level is where many others sit, and it's easy to hit. Buying support in a strong downtrend can turn into many losses in a row. Always use a stop beyond the zone and size from that distance.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Why can "more touches = stronger" be misleading?
> > [!answer]-
> > Many touches prove the level matters, but each touch fills orders waiting there. A level hit many times in a short period is more likely to break next time.
> **Q2.** Resistance zone 74.0–75.0 breaks with a close at 76.5. You buy the retest at 75.0, stop 73.8, target 79.2. What's the R:R?
> > [!answer]-
> > Risk 1.2, reward 4.2 → **3.5R**.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> แนวรับคือโซนราคาที่ราคาที่ลงมาเคยหยุด เพราะผู้ซื้อเข้ามา แนวต้านคือที่ราคาที่ขึ้นไปเคยหยุด เพราะผู้ขายเข้ามา คนจำราคาเหล่านี้และวางคำสั่งไว้อีก ราคาจึงมักตอบสนองตรงนั้น แต่ทุกครั้งที่ราคากลับมา คำสั่งบางส่วนถูกใช้ไป และเมื่อระดับราคาแตกในที่สุด มันมักสลับบทบาท
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **แนวรับ / แนวต้าน (Support / Resistance, S/R)** — โซนราคาที่ผู้ซื้อ / ผู้ขายเคยหยุดราคา
> - **โซน (Zone)** — แถบราคา ไม่ใช่เส้นเดียว จากปลายไส้ถึงจุดที่ตัวแท่งกระจุกตัว
> - **การทดสอบ (Test)** — ราคากลับมาที่ระดับนั้น
> - **การซ้อนทับของเหตุผล (Confluence)** — มีหลายเหตุผลที่ราคาเดียวกัน (เลขกลม จุดสูงเดิม การสลับบทบาท)
> - **การสลับบทบาท (Role reversal)** — แนวต้านที่แตกกลายเป็นแนวรับ หรือแนวรับที่แตกกลายเป็นแนวต้าน
> - **Bounce** — เทรดการปฏิเสธที่ระดับราคาในทิศทางเทรนด์
> - **Break & retest** — เทรดการย่อครั้งแรกกลับมาที่ระดับที่แตกด้วยราคาปิด
> - **การทะลุหลอก (Failed break)** — ราคาแทงไส้ทะลุระดับแต่ปิดกลับเข้ามา *(ดู 5.2)*
> - **เลขกลม (Round number)** — ราคาอย่าง 100, 1.1000 หรือ 2,000 ที่คนจำนวนมากจับตา
""")
L.before_heading("th", "2.", """
> [!analogy]
> ระดับราคาเหมือน **ร้านสตรีทฟู้ดดังที่ "หมดตอนสองทุ่ม"** คนจำได้และมาเร็วขึ้นในครั้งถัดไป แต่ร้านมีอยู่จำนวนชามจำกัด ถ้าคนมาเยอะซ้ำ ๆ ของก็หมดเร็วขึ้น และวันหนึ่งก็ไม่มีอะไรเหลือให้หยุดคิว
>
> **จุดที่เปรียบเทียบไม่ได้:** ร้านเติมของทุกวัน แต่ระดับราคาไม่เติมเอง คำสั่งใหม่จะมาก็ต่อเมื่อนักเทรดยังสนใจราคานั้นอยู่

> [!check]- เช็กความเข้าใจ: ทำไมระดับราคาจึงมีอยู่
> **Q1.** บอกนักเทรดสองกลุ่มที่เพิ่มคำสั่งซื้อที่แนวรับ และเพราะอะไร
> > [!answer]-
> > ตัวอย่าง: ผู้ซื้อที่พลาดการเด้งครั้งก่อน (อยากได้โอกาสที่สอง) และคน Short ที่ Stop หรือคำสั่งทำกำไรอยู่ตรงนั้น (ต้องซื้อเพื่อปิดไม้)
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: ขีดโซนแทนเส้น
> การเด้งสามครั้งจากพื้นที่เดียวกัน (ตัวอย่าง): ไส้ต่ำ **98.6, 98.9, 99.1** ตัวแท่งกระจุกที่ **99.4–99.7**
> 1. โซน = ไส้ต่ำสุดถึงขอบบนของกลุ่มตัวแท่ง = **98.6–99.7** (กว้าง 1.1)
> 2. "เส้น" ที่ **99.0** กับ Stop ที่ 98.9 จะโดนไส้ **98.6** ชน แม้ระดับราคาจะยืนได้
> 3. เมื่อใช้โซน Stop อยู่เลยโซน: **98.4** ซื้อการปฏิเสธที่ปิดที่ **100.2** เสี่ยง **1.8**
> 4. **แล้วไง?** โซนยอมรับว่าคำสั่งกระจายอยู่ทั่วแถบราคา Stop ที่กว้างขึ้นหมายถึงขนาดเล็กลง (เฟส 3) แต่ลดการแพ้แบบ "คิดถูก แต่โดนสัญญาณรบกวนชน" ได้มาก

> [!check]- เช็กความเข้าใจ: ให้คะแนนโซน
> **Q1.** แนวรับบน 15m จากเมื่อ 2 ปีก่อน ถูกทดสอบ 4 ครั้งเมื่อสัปดาห์ที่แล้ว ไม่มีเหตุผลซ้อน แข็งหรืออ่อน? ทำไม?
> > [!answer]-
> > อ่อนแทบทุกปัจจัย: ไทม์เฟรมเล็ก เก่า ถูกทดสอบหนัก (คำสั่งถูกใช้ไป) ไม่มีเหตุผลซ้อน ลบทิ้งหรือถือเป็นระดับย่อย
""")
L.before_heading("th", "4.", """
> [!check]- เช็กความเข้าใจ: การสลับบทบาท
> **Q1.** แนวรับที่ 50 แตกด้วยราคาปิดรายวันที่ 48 ราคาเด้งกลับมาที่ 49.8 คุณคาดอะไร และเพราะอะไร?
> > [!answer]-
> > แนวรับเดิมอาจทำหน้าที่เป็น **แนวต้าน**: คนที่ซื้อที่ 50 ตอนนี้ขาดทุนและอยากขายเท่าทุน และคนที่พลาดการขายอยากได้โอกาสที่สอง รอดูการปฏิเสธเพื่อขาย
""")
L.before_callout("th", "action", """
![[p2-retest-vs-chase.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ไล่ซื้อ vs รอทดสอบซ้ำ
> การทะลุจากตัวอย่าง: โซนเดิม **109.2–110.6** Stop ใต้โซนที่ **108.9** เป้า **117** เสี่ยงไม้ละ **100 ดอลลาร์**
> 1. **ไล่ซื้อที่ 114** (หลังการทะลุ "ชัดแล้ว"): เสี่ยง 5.1 ผลตอบแทน 3.0 → **0.6R** ขนาด 100 ÷ 5.1 ≈ **20 หน่วย** ถึงเป้าได้ +59 ดอลลาร์
> 2. **ซื้อตอนทดสอบซ้ำที่ 110.6:** เสี่ยง 1.7 ผลตอบแทน 6.4 → **3.8R** ขนาด ≈ **59 หน่วย** ถึงเป้าได้ +376 ดอลลาร์
> 3. ไอเดียเดียวกัน Stop เดียวกัน เป้าเดียวกัน: การทดสอบซ้ำให้ R:R ราว **6 เท่า**
> 4. **แล้วไง?** การรอทดสอบซ้ำไม่เสียอะไรนอกจากความอดทน ความเสี่ยงคือราคาไม่กลับมา แล้วคุณก็แค่พลาดเทรดนั้น ซึ่งถูกกว่าการไล่ซื้อ

> [!check]- เช็กความเข้าใจ: เทรด 3 แบบ
> **Q1.** ราคาแทงไส้เหนือแนวต้าน 0.5 แล้วปิดกลับมาใต้แนวต้าน นี่คือเทรดแบบไหน และ Stop อยู่ตรงไหน?
> > [!answer]-
> > **การทะลุหลอก (Failed break)**: ขายหลังราคาปิดกลับเข้ามา Stop เลยปลายไส้

> [!market]
> - **ฟอเร็กซ์:** เลขกลม (1.1000, 150.00) และจุดสูงจุดต่ำของวันก่อนเป็นระดับที่คนจับตามาก *(ดู 0.3)*
> - **ทองคำ:** เลขกลมทุก 50 และ 100 ดอลลาร์มักทำหน้าที่เป็นระดับราคา *(ดู 0.4)*
> - **หุ้น:** จุดสูงเดิม ราคา IPO และเลขกลม Gap จากงบการเงินอาจกระโดดข้ามระดับราคาไปเลย *(ดู 0.5)*
> - **คริปโต:** เลขกลม (เช่น ทุก 1,000 หรือ 10,000 ดอลลาร์) ดึงดูดคำสั่งและ Stop จำนวนมาก *(ดู 0.7)*

> [!caution]
> ระดับราคาไม่ใช่กำแพง Stop ที่วางตรงระดับที่เห็นชัดคือที่ที่คนอื่นจำนวนมากวางไว้ด้วย และโดนชนได้ง่าย การซื้อแนวรับในขาลงแรงอาจกลายเป็นการแพ้หลายไม้ติดกัน ใช้ Stop เลยโซนเสมอ และคำนวณขนาดจากระยะนั้น
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** ทำไม "แตะยิ่งเยอะยิ่งแข็งแรง" จึงอาจทำให้เข้าใจผิด?
> > [!answer]-
> > การแตะหลายครั้งพิสูจน์ว่าระดับนั้นสำคัญ แต่ทุกครั้งที่แตะ คำสั่งที่รออยู่ถูกใช้ไป ระดับที่ถูกชนหลายครั้งในเวลาสั้นจึงมีโอกาสแตกมากขึ้นในครั้งถัดไป
> **Q2.** โซนแนวต้าน 74.0–75.0 แตกด้วยราคาปิดที่ 76.5 คุณซื้อตอนทดสอบซ้ำที่ 75.0 Stop 73.8 เป้า 79.2 R:R เท่าไร?
> > [!answer]-
> > เสี่ยง 1.2 ผลตอบแทน 4.2 → **3.5R**
""")

L.set_meta("level", "v2")
L.save()
