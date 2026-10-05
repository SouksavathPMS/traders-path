"""B8 · v2 upgrade of 2.3 Break of Structure & Change of Character (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("02 Market Structure/2.3 Break of Structure & Change of Character.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> In an uptrend, price climbs like stairs: each step up is higher, and each dip stops above the last dip. When price closes above the last step, the climb continues: that's a **break of structure (BOS)**. When price instead closes below the dip that the buyers had to defend, the stairs are broken for the first time: that's a **change of character (CHoCH)**. It doesn't mean the price will fall; it means the "easy" uptrend is over and you should stop buying it blindly.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Swing high / swing low** — a turning point in price *(see 2.1)*.
> - **HH / HL / LH / LL** — higher high / higher low / lower high / lower low *(see 2.1)*.
> - **BOS (break of structure)** — a candle close beyond the last swing **in** the trend's direction.
> - **CHoCH (change of character)** — the first candle close beyond the protected swing **against** the trend.
> - **MSS (market structure shift)** — ICT's name for a CHoCH that follows a liquidity sweep *(see 5.2)*.
> - **Protected low / high** — the HL (or LH) from which the latest HH (or LL) was made; the trend's key defence.
> - **Acceptance / rejection** — price closing and staying beyond a level / only wicking through it and closing back inside.
> - **Trailing stop** — moving the stop up behind each new protected low as the trend continues.
> - **HTF / LTF** — higher / lower timeframe *(see 1.5, 2.6)*.
""")
L.before_heading("en", "2.", """
> [!analogy]
> A trend is like **a team defending a goal line that keeps moving forward**. Every time the team scores (a BOS), it moves its defensive line up to the last position it held (the protected low). As long as that line holds, the team is in control. The first time the opponents break through that line (a CHoCH), the match isn't lost, but the team is no longer clearly dominant.
>
> **Where it breaks:** a sports match has a fixed field. Market structure depends on which timeframe you watch: a CHoCH on the 5-minute chart may be just a normal dip on the daily.

> [!check]- Check your understanding: BOS vs CHoCH
> **Q1.** In a downtrend, price closes above the last lower high that created the latest lower low. BOS or CHoCH?
> > [!answer]-
> > CHoCH: a close beyond the protected swing **against** the downtrend.
""")
L.before_heading("en", "3.", """
![[p2-protected-low.en.svg]]

> [!walkthrough] Step by step: trailing the protected low (figure)
> Swings: 100 → **108** → 104 → **114** → 109 → **120** → 111.5 → 116 → down.
> 1. **BOS 114** (close above 108): it was made from the HL at **104** → protected low = **104**. A trend trader's stop goes just below it.
> 2. **BOS 120** (close above 114): made from the HL at **109** → protected low moves up to **109**; the stop trails to below 109.
> 3. **Pullback to 111.5:** above 109 → still a pullback, nothing changes.
> 4. **Rally to 116:** fails below 120 → a possible **lower high**.
> 5. **A candle closes below 109** → **CHoCH**. The buyers lost the level they needed to hold. No new longs; the trailing stop has already taken you out.
> 6. **So what?** You never have to guess where the trend ends. You just keep asking "which low must hold?", and you move your stop there.

> [!check]- Check your understanding: the protected low
> **Q1.** After BOS 120, price dips to 111.5 and a candle closes at 111.0, below a minor low at 111.3 inside the pullback. CHoCH?
> > [!answer]-
> > No. Only a close below the protected low (109) counts. Minor lows inside a pullback don't change the trend.
""")
L.before_heading("en", "4.", """
> [!walkthrough] Step by step: close vs wick at the protected low (109)
> 1. **Candle A:** low **108.6**, close **109.8** → a wick through 109, body back above → **rejection**, not a CHoCH. Often a liquidity grab *(see 5.2)*.
> 2. **Candle B:** low **108.2**, close **108.4** → body closes below 109 → **acceptance** → **CHoCH**.
> 3. **So what?** On your analysis timeframe, wait for the candle to **close** before calling the break. Deciding while the candle is still open is how traders get trapped by wicks.

> [!check]- Check your understanding: close, not wick
> **Q1.** On the 1-hour chart a candle wicks 5 points below the protected low and closes 2 points above it. What do you record?
> > [!answer]-
> > No break: a rejection (possible sweep). The trend's structure is intact on the 1-hour chart.
""")
L.before_callout("en", "action", """
> [!check]- Check your understanding: from CHoCH to a new trend
> **Q1.** After a CHoCH down, price rallies and makes a **new high** above the old one. What happened?
> > [!answer]-
> > A false alarm: the uptrend resumed. A new downtrend needs a lower high followed by a BOS down.

> [!market]
> - **Forex:** clean structure on 1H–daily; use the session closes you trade *(see 0.3, 5.6)*.
> - **Gold:** fast wicks around news often poke through protected lows and close back: insist on the close *(see 0.4)*.
> - **Stocks:** overnight gaps can jump past a protected low; the gap itself is the close beyond it *(see 0.5)*.
> - **Crypto:** 24/7 with deep liquidation wicks; use daily closes at 07:00 UTC+7 for HTF structure *(see 0.7)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Define BOS and CHoCH in one line each, for an uptrend.
> > [!answer]-
> > BOS: a candle close above the last swing high (trend continues). CHoCH: the first candle close below the protected HL (the HL that made the latest HH).
> **Q2.** Why is the CHoCH candle usually a poor place to sell?
> > [!answer]-
> > It often closes right into support and is followed by a retest. A lower high and a BOS down give a better-defined entry and stop.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ในเทรนด์ขาขึ้น ราคาไต่เหมือนบันได: แต่ละขั้นสูงขึ้น และแต่ละครั้งที่ย่อก็หยุดเหนือจุดย่อครั้งก่อน เมื่อราคาปิดเหนือขั้นล่าสุด การไต่ก็ดำเนินต่อ: นั่นคือ **การทะลุโครงสร้าง (BOS)** เมื่อราคากลับปิดใต้จุดย่อที่ผู้ซื้อต้องปกป้อง บันไดก็หักเป็นครั้งแรก: นั่นคือ **การเปลี่ยนนิสัย (CHoCH)** ไม่ได้แปลว่าราคาจะลง แต่แปลว่าเทรนด์ขาขึ้นแบบ "ง่าย ๆ" จบแล้ว และคุณควรเลิกซื้อแบบไม่คิด
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **Swing high / Swing low** — จุดกลับตัวของราคา *(ดู 2.1)*
> - **HH / HL / LH / LL** — Higher high / Higher low / Lower high / Lower low *(ดู 2.1)*
> - **BOS (Break of structure)** — แท่งเทียนปิดเลย Swing ล่าสุด **ใน** ทิศทางของเทรนด์
> - **CHoCH (Change of character)** — แท่งเทียนปิดเลย Swing ที่ถูกปกป้องเป็นครั้งแรก **สวน** เทรนด์
> - **MSS (Market structure shift)** — ชื่อที่ ICT ใช้เรียก CHoCH ที่ตามหลังการกวาดสภาพคล่อง *(ดู 5.2)*
> - **Protected low / high** — HL (หรือ LH) ที่เป็นจุดเริ่มของ HH (หรือ LL) ล่าสุด แนวป้องกันสำคัญของเทรนด์
> - **การยอมรับ / การปฏิเสธ (Acceptance / Rejection)** — ราคาปิดและอยู่เลยระดับได้ / แค่ไส้ทะลุแล้วปิดกลับเข้ามา
> - **Trailing stop** — เลื่อน Stop ขึ้นตามหลัง Protected low ใหม่แต่ละจุดเมื่อเทรนด์ไปต่อ
> - **HTF / LTF** — ไทม์เฟรมสูง / ต่ำ *(ดู 1.5, 2.6)*
""")
L.before_heading("th", "2.", """
> [!analogy]
> เทรนด์เหมือน **ทีมที่ป้องกันเส้นประตูซึ่งขยับไปข้างหน้าเรื่อย ๆ** ทุกครั้งที่ทีมทำประตูได้ (BOS) ทีมจะย้ายแนวรับขึ้นไปที่ตำแหน่งล่าสุดที่ยึดไว้ (Protected low) ตราบใดที่แนวนั้นยังอยู่ ทีมก็ยังคุมเกม ครั้งแรกที่คู่แข่งทะลุแนวนั้นได้ (CHoCH) เกมยังไม่แพ้ แต่ทีมไม่ได้เหนือกว่าอย่างชัดเจนอีกแล้ว
>
> **จุดที่เปรียบเทียบไม่ได้:** สนามกีฬามีขนาดคงที่ แต่โครงสร้างตลาดขึ้นกับไทม์เฟรมที่คุณดู CHoCH บนกราฟ 5 นาทีอาจเป็นแค่การย่อตัวปกติบนกราฟรายวัน

> [!check]- เช็กความเข้าใจ: BOS vs CHoCH
> **Q1.** ในเทรนด์ขาลง ราคาปิดเหนือ Lower high ล่าสุดที่เป็นจุดเริ่มของ Lower low ล่าสุด เป็น BOS หรือ CHoCH?
> > [!answer]-
> > CHoCH: การปิดเลย Swing ที่ถูกปกป้อง **สวน** เทรนด์ขาลง
""")
L.before_heading("th", "3.", """
![[p2-protected-low.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: เลื่อนตาม Protected low (ภาพ)
> Swing: 100 → **108** → 104 → **114** → 109 → **120** → 111.5 → 116 → ลง
> 1. **BOS 114** (ปิดเหนือ 108): เกิดจาก HL ที่ **104** → Protected low = **104** Stop ของเทรดเดอร์ตามเทรนด์อยู่ใต้จุดนี้นิดเดียว
> 2. **BOS 120** (ปิดเหนือ 114): เกิดจาก HL ที่ **109** → Protected low ขยับขึ้นเป็น **109** Stop เลื่อนไปใต้ 109
> 3. **ย่อลง 111.5:** เหนือ 109 → ยังเป็นการย่อตัว ไม่มีอะไรเปลี่ยน
> 4. **เด้งขึ้น 116:** ไม่ผ่าน 120 → อาจเป็น **Lower high**
> 5. **แท่งเทียนปิดใต้ 109** → **CHoCH** ผู้ซื้อเสียระดับที่ต้องรักษาไว้ ไม่เปิด Long ใหม่ Trailing stop พาคุณออกไปแล้ว
> 6. **แล้วไง?** คุณไม่ต้องเดาว่าเทรนด์จะจบตรงไหน แค่ถามเสมอว่า "จุดต่ำไหนที่ต้องยืนได้?" แล้วเลื่อน Stop ไปตรงนั้น

> [!check]- เช็กความเข้าใจ: Protected low
> **Q1.** หลัง BOS 120 ราคาย่อลงไป 111.5 และมีแท่งปิดที่ 111.0 ใต้จุดต่ำย่อย 111.3 ในระหว่างการย่อ เป็น CHoCH ไหม?
> > [!answer]-
> > ไม่ใช่ นับเฉพาะการปิดใต้ Protected low (109) จุดต่ำย่อยในการย่อตัวไม่เปลี่ยนเทรนด์
""")
L.before_heading("th", "4.", """
> [!walkthrough] ไล่ทีละขั้น: ราคาปิด vs ไส้ ที่ Protected low (109)
> 1. **แท่ง A:** ต่ำสุด **108.6** ปิด **109.8** → ไส้ทะลุ 109 ตัวแท่งกลับขึ้นมา → **การปฏิเสธ** ไม่ใช่ CHoCH มักเป็นการกวาดสภาพคล่อง *(ดู 5.2)*
> 2. **แท่ง B:** ต่ำสุด **108.2** ปิด **108.4** → ตัวแท่งปิดใต้ 109 → **การยอมรับ** → **CHoCH**
> 3. **แล้วไง?** บนไทม์เฟรมที่วิเคราะห์ รอให้แท่ง **ปิด** ก่อนจะเรียกว่าทะลุ การตัดสินใจขณะที่แท่งยังไม่ปิดคือวิธีที่เทรดเดอร์ติดกับดักไส้เทียน

> [!check]- เช็กความเข้าใจ: ราคาปิด ไม่ใช่ไส้
> **Q1.** บนกราฟ 1 ชั่วโมง แท่งหนึ่งมีไส้ลงไปใต้ Protected low 5 จุด แต่ปิดเหนือมัน 2 จุด คุณบันทึกว่าอะไร?
> > [!answer]-
> > ไม่ทะลุ: เป็นการปฏิเสธ (อาจเป็นการกวาด) โครงสร้างของเทรนด์บนกราฟ 1 ชั่วโมงยังสมบูรณ์
""")
L.before_callout("th", "action", """
> [!check]- เช็กความเข้าใจ: จาก CHoCH สู่เทรนด์ใหม่
> **Q1.** หลัง CHoCH ขาลง ราคาเด้งขึ้นและทำ **จุดสูงใหม่** เหนือจุดสูงเดิม เกิดอะไรขึ้น?
> > [!answer]-
> > สัญญาณหลอก: เทรนด์ขาขึ้นกลับมา เทรนด์ขาลงใหม่ต้องมี Lower high ตามด้วย BOS ขาลง

> [!market]
> - **ฟอเร็กซ์:** โครงสร้างชัดบน 1 ชั่วโมงถึงรายวัน ใช้ราคาปิดของเซสชันที่คุณเทรด *(ดู 0.3, 5.6)*
> - **ทองคำ:** ไส้ที่วิ่งเร็วช่วงข่าวมักทะลุ Protected low แล้วปิดกลับ ต้องยึดราคาปิด *(ดู 0.4)*
> - **หุ้น:** Gap ข้ามคืนอาจกระโดดข้าม Protected low Gap นั้นถือเป็นการปิดเลยระดับ *(ดู 0.5)*
> - **คริปโต:** 24/7 และไส้จากการล้างพอร์ตลึก ใช้ราคาปิดรายวันตอน 07:00 UTC+7 สำหรับโครงสร้าง HTF *(ดู 0.7)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** นิยาม BOS และ CHoCH ข้อละบรรทัด สำหรับเทรนด์ขาขึ้น
> > [!answer]-
> > BOS: แท่งเทียนปิดเหนือ Swing high ล่าสุด (เทรนด์ไปต่อ) CHoCH: แท่งเทียนปิดใต้ Protected HL (HL ที่เป็นจุดเริ่มของ HH ล่าสุด) เป็นครั้งแรก
> **Q2.** ทำไมแท่ง CHoCH มักเป็นจุดขายที่ไม่ดี?
> > [!answer]-
> > มักปิดลงไปชนแนวรับพอดี และตามด้วยการทดสอบซ้ำ Lower high และ BOS ขาลงให้จุดเข้าและ Stop ที่ชัดเจนกว่า
""")

L.set_meta("level", "v2")
L.save()
