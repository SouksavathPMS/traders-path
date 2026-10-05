"""B4 · v2 upgrade of 5.2 Liquidity Sweeps & Stop Hunts (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("05 Liquidity & ICT/5.2 Liquidity Sweeps & Stop Hunts.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Price sometimes pokes just past an obvious high or low, sets off everyone's stop orders, and then turns straight back. That poke is a **sweep**. It happens because the stop orders gave a big trader exactly what they needed (lots of orders to trade against), and once those orders are used up, there's nobody left to push price further. A sweep only matters if the market then **proves** it has turned: a strong move the other way that breaks the last swing.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Sweep (liquidity grab, stop hunt)** — price trades through a liquidity pool, triggers the resting orders, then closes back on the original side.
> - **Run** — price takes a pool and keeps going (the break is accepted).
> - **Acceptance** — price closing beyond a level and staying there *(see 2.3)*.
> - **Displacement** — a fast, one-sided move with big candle bodies, often leaving an FVG *(see 5.4)*.
> - **BOS (break of structure)** — a close beyond a swing in the trend's direction *(see 2.3)*.
> - **CHoCH (change of character)** — the first close beyond a swing against the previous direction *(see 2.3)*.
> - **MSS (market structure shift)** — ICT's name for a CHoCH that comes right after a sweep, with displacement.
> - **Opposite pool** — the liquidity on the other side of the range (the target after a sweep).
> - **Buffer** — extra distance added beyond a level when placing a stop *(see 3.5)*.
> - **R / R:R** — 1R = the amount you lose if the stop is hit; R:R = reward ÷ risk *(see 3.3)*.
> - **Killzone** — the high-activity time windows around the London and New York opens *(see 5.6)*.
""")
L.before_heading("en", "2.", """
![[p5-sweep-story.en.svg]]

> [!walkthrough] Step by step: a sweep, five candles, one decision each (15-minute EUR/USD, illustrative)
> Equal lows at about **1.0781** = SSL. The swing high that started the last drop is **1.0815**.
> 1. **Candle 1 · approach:** price drifts down to the lows. Decision: **wait**. Nothing has happened yet.
> 2. **Candle 2 · sweep:** low **1.0768** (13 pips under the lows), but it **closes at 1.0784**, back above. Decision: **mark it** as a possible sweep; still no trade.
> 3. **Candle 3 · displacement:** big green body, closes **1.0810**. Decision: the reversal is gaining proof; keep watching.
> 4. **Candle 4 · MSS:** closes **1.0825**, above the swing high 1.0815. It leaves an FVG between candle 2's high **1.0790** and candle 4's low **1.0806**; CE = **1.0798**. Decision: **plan** the trade.
> 5. **Candle 5 · retrace:** low **1.0799**, so a limit order at **1.0798** is about to fill. Stop **1.0765** (below the sweep low 1.0768 + 3-pip buffer) → risk **33 pips**. Target: equal highs (BSL) at **1.0880** → reward **82 pips** → **≈ 2.5R**.
> 6. **So what?** Each decision was made on a **closed** candle. The wick in candle 2 alone was never a reason to buy; the close back inside, the displacement and the MSS were.

> [!check]- Check your understanding
> **Q1.** In the walkthrough, what would have cancelled the trade idea after candle 2?
> > [!answer]-
> > A candle **closing** back below the equal lows (below 1.0781) and staying there: that would be acceptance below, a run rather than a sweep.
> **Q2.** Why is the stop at 1.0765 and not at 1.0781?
> > [!answer]-
> > The sweep low (1.0768) is where the idea is proven wrong. 1.0781 is inside the noise of the sweep itself, and a second poke is common. The stop goes beyond the sweep extreme plus a buffer.
""")
L.before_heading("en", "3.", """
> [!analogy]
> A sweep is like a **false fire alarm in a cinema**. The alarm (price poking through the level) makes the crowd rush for the doors (stops fire). A few calm people buy the seats near the screen cheaply while everyone runs. When it turns out there's no fire, people walk back in and prices go back to normal. A **run** is a real fire: people leave and don't come back.
>
> **Where it breaks:** you can't tell a false alarm from a real fire while it's ringing. In the market you also only know **after** the candle closes: back inside, or accepted beyond.

> [!check]- Check your understanding
> **Q1.** After the candle has closed, how do you tell a sweep from a real breakout?
> > [!answer]-
> > Look at the close. Sweep: a wick beyond the level but the **close is back inside**, followed by displacement the other way. Real breakout: the **close is beyond** the level and the next candles hold there (a retest holds, BOS in the same direction).
> **Q2.** Price closes above the equal highs, pulls back, and the retest holds as support. Sweep or run?
> > [!answer]-
> > A run. The close beyond plus a retest that holds is acceptance (role reversal, 2.4).
""")
L.before_callout("en", "action", """
> [!check]- Check your understanding: HTF context
> **Q1.** The daily trend is up. You see a sweep of equal **highs** during London. Should it carry as much weight as a sweep of equal **lows**?
> > [!answer]-
> > Less. In a daily uptrend, sweeps of SSL (below lows) during pullbacks fit the HTF bias. A sweep of the highs against the trend more often turns into a run.

> [!market]
> - **Forex:** sweeps of the Asian-session high/low during the London open are the classic pattern *(see 5.6)*.
> - **Gold:** fast and deep sweeps of round numbers and the previous day's high/low; wicks of 10–20 USD are normal *(see 0.4)*.
> - **Stocks & index futures:** the previous day's high/low and the opening range are swept around 20:30–21:00 UTC+7 (US open, summer); single stocks can **gap** past a level overnight, which is not a sweep *(see 0.5)*.
> - **Crypto:** sweeps are often **liquidation cascades**, much deeper than in forex, and can happen at any hour, including weekends *(see 0.7)*.

> [!caution]
> Trading every sweep is one of the fastest ways to lose money with ICT concepts. In a strong trend, "sweeps" against the trend are usually just runs, and your stop is hit again and again. A stop placed **inside** the sweep wick will often be taken by a second poke. Trade only with the close back inside, displacement, an MSS and a stop beyond the extreme, and size for 1R.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** List the five things that must happen, in order, before you short a sweep of equal highs.
> > [!answer]-
> > 1) An obvious pool (equal highs, PDH). 2) A wick above it with a close back inside. 3) Displacement down. 4) A close below the swing that launched the sweep (CHoCH/MSS). 5) A retrace entry with the stop above the sweep high + buffer and R:R ≥ 2 to the opposite pool.
> **Q2.** Entry 1.0798, stop 1.0765, target 1.0880. What is the R:R?
> > [!answer]-
> > Risk 33 pips, reward 82 pips → 82 ÷ 33 ≈ 2.5R.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> บางครั้งราคาทะลุเลยจุดสูงหรือจุดต่ำที่ชัดเจนไปนิดเดียว ทำให้คำสั่ง Stop ของทุกคนทำงาน แล้วก็หันกลับทันที การทะลุนั้นคือ **การกวาด (Sweep)** มันเกิดขึ้นเพราะคำสั่ง Stop ให้สิ่งที่เทรดเดอร์รายใหญ่ต้องการพอดี (คำสั่งจำนวนมากให้ซื้อขายด้วย) และเมื่อคำสั่งเหล่านั้นถูกใช้หมด ก็ไม่เหลือใครดันราคาต่อ การกวาดจะมีความหมายก็ต่อเมื่อตลาด **พิสูจน์** ว่ากลับตัวแล้ว: วิ่งแรงไปอีกทางจนทะลุ Swing ล่าสุด
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **การกวาด (Sweep / Liquidity grab / Stop hunt)** — ราคาวิ่งทะลุกองสภาพคล่อง กระตุ้นคำสั่งที่รออยู่ แล้วปิดกลับมาฝั่งเดิม
> - **การวิ่งทะลุ (Run)** — ราคาเก็บกองสภาพคล่องแล้ววิ่งต่อ (การทะลุถูกยอมรับ)
> - **การยอมรับ (Acceptance)** — ราคาปิดเลยระดับและอยู่ตรงนั้นได้ *(ดู 2.3)*
> - **แรงส่ง (Displacement)** — การวิ่งเร็วไปทางเดียว แท่งเทียนตัวใหญ่ มักทิ้ง FVG ไว้ *(ดู 5.4)*
> - **BOS (Break of structure)** — การปิดเลย Swing ในทิศทางของเทรนด์ *(ดู 2.3)*
> - **CHoCH (Change of character)** — การปิดเลย Swing ครั้งแรกที่สวนทิศทางเดิม *(ดู 2.3)*
> - **MSS (Market structure shift)** — ชื่อที่ ICT ใช้เรียก CHoCH ที่เกิดทันทีหลังการกวาด พร้อมแรงส่ง
> - **กองฝั่งตรงข้าม (Opposite pool)** — สภาพคล่องอีกฝั่งของกรอบ (เป้าหมายหลังการกวาด)
> - **ระยะเผื่อ (Buffer)** — ระยะที่เพิ่มเลยระดับเมื่อวาง Stop *(ดู 3.5)*
> - **R / R:R** — 1R = เงินที่เสียถ้าโดน Stop  R:R = ผลตอบแทน ÷ ความเสี่ยง *(ดู 3.3)*
> - **Killzone** — ช่วงเวลาที่คึกคักรอบการเปิดของลอนดอนและนิวยอร์ก *(ดู 5.6)*
""")
L.before_heading("th", "2.", """
![[p5-sweep-story.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: การกวาด ห้าแท่ง แต่ละแท่งหนึ่งการตัดสินใจ (EUR/USD 15 นาที ภาพประกอบ)
> จุดต่ำเท่ากันราว **1.0781** = SSL  Swing high ที่เริ่มการร่วงรอบล่าสุดคือ **1.0815**
> 1. **แท่ง 1 · เข้าใกล้:** ราคาไหลลงหาจุดต่ำ การตัดสินใจ: **รอ** ยังไม่มีอะไรเกิดขึ้น
> 2. **แท่ง 2 · กวาด:** ต่ำสุด **1.0768** (ต่ำกว่าจุดต่ำ 13 pip) แต่ **ปิดที่ 1.0784** กลับขึ้นมาเหนือจุดต่ำ การตัดสินใจ: **ทำเครื่องหมาย** ว่าอาจเป็นการกวาด ยังไม่เทรด
> 3. **แท่ง 3 · แรงส่ง:** แท่งเขียวตัวใหญ่ ปิด **1.0810** การตัดสินใจ: การกลับตัวเริ่มมีหลักฐาน ดูต่อ
> 4. **แท่ง 4 · MSS:** ปิด **1.0825** เหนือ Swing high 1.0815 ทิ้ง FVG ระหว่าง High ของแท่ง 2 **1.0790** กับ Low ของแท่ง 4 **1.0806** CE = **1.0798** การตัดสินใจ: **วางแผน** เทรด
> 5. **แท่ง 5 · ย่อกลับ:** ต่ำสุด **1.0799** คำสั่ง Limit ที่ **1.0798** ใกล้ถูกจับคู่ Stop **1.0765** (ใต้จุดกวาด 1.0768 + เผื่อ 3 pip) → ความเสี่ยง **33 pip** เป้าหมาย: จุดสูงเท่ากัน (BSL) ที่ **1.0880** → ผลตอบแทน **82 pip** → **≈ 2.5R**
> 6. **แล้วไง?** ทุกการตัดสินใจเกิดบนแท่งที่ **ปิดแล้ว** ไส้เทียนของแท่ง 2 อย่างเดียวไม่เคยเป็นเหตุผลให้ซื้อ แต่การปิดกลับเข้ามา แรงส่ง และ MSS ต่างหาก

> [!check]- เช็กความเข้าใจ
> **Q1.** ในตัวอย่าง อะไรจะยกเลิกไอเดียเทรดหลังแท่ง 2?
> > [!answer]-
> > แท่งเทียนที่ **ปิด** กลับลงไปใต้จุดต่ำเท่ากัน (ใต้ 1.0781) และอยู่ตรงนั้นได้: นั่นคือการยอมรับด้านล่าง เป็นการวิ่งทะลุ ไม่ใช่การกวาด
> **Q2.** ทำไม Stop อยู่ที่ 1.0765 ไม่ใช่ 1.0781?
> > [!answer]-
> > จุดกวาด (1.0768) คือจุดที่พิสูจน์ว่าไอเดียผิด 1.0781 อยู่ในการแกว่งของการกวาดเอง และการทะลุซ้ำครั้งที่สองพบบ่อย Stop จึงต้องอยู่เลยจุดสุดของการกวาดบวกระยะเผื่อ
""")
L.before_heading("th", "3.", """
> [!analogy]
> การกวาดเหมือน **สัญญาณไฟไหม้ปลอมในโรงหนัง** สัญญาณ (ราคาทะลุระดับ) ทำให้ฝูงชนวิ่งไปที่ประตู (Stop ทำงาน) คนใจเย็นไม่กี่คนได้ที่นั่งใกล้จอราคาถูกขณะที่ทุกคนวิ่ง เมื่อรู้ว่าไม่มีไฟ คนก็เดินกลับเข้ามา ราคากลับสู่ปกติ ส่วน **การวิ่งทะลุ** คือไฟไหม้จริง: คนออกไปแล้วไม่กลับมา
>
> **จุดที่เปรียบเทียบไม่ได้:** ขณะที่สัญญาณยังดังอยู่ คุณแยกไม่ออกว่าปลอมหรือจริง ในตลาดก็เช่นกัน คุณจะรู้ก็ต่อเมื่อแท่งเทียน **ปิดแล้ว**: ปิดกลับเข้ามา หรือถูกยอมรับเลยระดับไป

> [!check]- เช็กความเข้าใจ
> **Q1.** หลังแท่งเทียนปิดแล้ว คุณแยกการกวาดออกจากการทะลุจริงได้อย่างไร?
> > [!answer]-
> > ดูราคาปิด การกวาด: ไส้ทะลุระดับแต่ **ปิดกลับเข้ามา** ตามด้วยแรงส่งไปอีกทาง การทะลุจริง: **ปิดเลย** ระดับและแท่งต่อมายืนได้ (Retest ยืนได้ มี BOS ทางเดียวกัน)
> **Q2.** ราคาปิดเหนือจุดสูงเท่ากัน ย่อกลับ และ Retest ยืนเป็นแนวรับได้ เป็นการกวาดหรือการวิ่งทะลุ?
> > [!answer]-
> > การวิ่งทะลุ การปิดเลยระดับบวกกับ Retest ที่ยืนได้คือการยอมรับ (การสลับบทบาท 2.4)
""")
L.before_callout("th", "action", """
> [!check]- เช็กความเข้าใจ: บริบทของ HTF
> **Q1.** เทรนด์รายวันเป็นขาขึ้น คุณเห็นการกวาดจุดสูงเท่ากันช่วงลอนดอน ควรให้น้ำหนักเท่ากับการกวาดจุด **ต่ำ** เท่ากันไหม?
> > [!answer]-
> > น้อยกว่า ในเทรนด์ขาขึ้นรายวัน การกวาด SSL (ใต้จุดต่ำ) ระหว่างการย่อตัวสอดคล้องกับ Bias ของ HTF การกวาดจุดสูงที่สวนเทรนด์มักกลายเป็นการวิ่งทะลุมากกว่า

> [!market]
> - **ฟอเร็กซ์:** การกวาดจุดสูง/ต่ำของเซสชันเอเชียตอนลอนดอนเปิดคือรูปแบบคลาสสิก *(ดู 5.6)*
> - **ทองคำ:** กวาดเลขกลมและจุดสูง/ต่ำของวันก่อนได้เร็วและลึก ไส้ 10–20 ดอลลาร์เป็นเรื่องปกติ *(ดู 0.4)*
> - **หุ้นและฟิวเจอร์สดัชนี:** จุดสูง/ต่ำของวันก่อนและกรอบช่วงเปิดตลาดถูกกวาดราว 20:30–21:00 UTC+7 (ตลาดสหรัฐเปิด ฤดูร้อน) หุ้นรายตัวอาจ **Gap** ข้ามระดับข้ามคืน ซึ่งไม่ใช่การกวาด *(ดู 0.5)*
> - **คริปโต:** การกวาดมักเป็น **การล้างพอร์ตต่อเนื่อง** ลึกกว่าในฟอเร็กซ์มาก และเกิดได้ทุกชั่วโมงรวมถึงวันหยุดสุดสัปดาห์ *(ดู 0.7)*

> [!caution]
> การเทรดทุกการกวาดเป็นหนึ่งในวิธีที่เสียเงินเร็วที่สุดกับแนวคิด ICT ในเทรนด์แรง "การกวาด" ที่สวนเทรนด์มักเป็นแค่การวิ่งทะลุ และ Stop ของคุณจะโดนซ้ำแล้วซ้ำเล่า Stop ที่วาง **ภายใน** ไส้ของการกวาดมักโดนการทะลุครั้งที่สอง เทรดเฉพาะเมื่อมีการปิดกลับเข้ามา แรงส่ง MSS และ Stop เลยจุดสุด และคำนวณขนาดสำหรับ 1R
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกห้าสิ่งที่ต้องเกิดขึ้นตามลำดับ ก่อนคุณจะ Short การกวาดจุดสูงเท่ากัน
> > [!answer]-
> > 1) กองสภาพคล่องที่ชัดเจน (จุดสูงเท่ากัน PDH) 2) ไส้ทะลุขึ้นไปแล้วปิดกลับเข้ามา 3) แรงส่งลง 4) ปิดใต้ Swing ที่เป็นจุดเริ่มของการกวาด (CHoCH/MSS) 5) เข้าตอนย่อกลับ Stop เหนือจุดกวาด + ระยะเผื่อ และ R:R ≥ 2 ไปถึงกองฝั่งตรงข้าม
> **Q2.** เข้า 1.0798 Stop 1.0765 เป้า 1.0880 R:R เท่าไหร่?
> > [!answer]-
> > ความเสี่ยง 33 pip ผลตอบแทน 82 pip → 82 ÷ 33 ≈ 2.5R
""")

L.set_meta("level", "v2")
L.save()
