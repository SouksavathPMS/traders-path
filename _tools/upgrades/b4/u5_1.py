"""B4 · v2 upgrade of 5.1 What Liquidity Really Is (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("05 Liquidity & ICT/5.1 What Liquidity Really Is.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Imagine a busy concert hall. Most people stand near the exit doors so they can leave fast if something goes wrong. In a market, the "exit doors" are **stop-loss orders**, and traders put them in the same obvious places: just past a recent high or low. Big traders who need to buy or sell a lot look for those crowds, because a crowd of orders is the only place they can trade large amounts at once. That's why price so often travels to obvious highs and lows: that's where the orders are waiting.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Liquidity** — orders available to trade against; here, mainly **resting orders** waiting in the order book *(see 1.2)*.
> - **Resting order** — an order placed in advance that waits for price (a limit order, or a stop order that becomes a market order when touched).
> - **Stop-loss (stop order)** — an order that closes a losing trade when price reaches a level. A long's stop is a **sell** order; a short's stop is a **buy** order.
> - **Market order** — an order that trades immediately at the best available price.
> - **Liquidity pool** — a cluster of resting orders at one price area.
> - **BSL (buy-side liquidity)** — buy orders resting **above** highs (shorts' stops + breakout buy entries).
> - **SSL (sell-side liquidity)** — sell orders resting **below** lows (longs' stops + breakdown sell entries).
> - **Equal highs / equal lows** — two or more highs (or lows) at almost the same price; very obvious, so very crowded.
> - **PDH / PDL** — previous day's high / low. **PWH / PWL** — previous week's high / low.
> - **External / internal liquidity** — pools beyond the current range's high and low / imbalances inside the range such as FVGs *(see 5.4)*.
> - **Draw on liquidity** — the pool price is most likely heading to next.
> - **Slippage** — getting filled at a worse price than expected because there weren't enough orders at your price *(see 0.1)*.
> - **ICT (Inner Circle Trader)** — the online educator whose vocabulary this phase uses.
> - **HTF / MTF / LTF** — higher / middle / lower timeframe *(see 1.5)*.
> - **Pip / lot** — the small price step and the trade size in forex *(see 0.3)*.
""")
L.before_heading("en", "2.", """
![[p5-stop-cluster.en.svg]]

> [!analogy]
> Stops are like a **crowd's exit doors**. Everyone in the hall picks the nearest, most obvious door. If someone shouts "fire!", the whole crowd rushes the same door at once: that rush is the stop cluster firing, and it's why price moves so fast through obvious levels. A big player who wants to trade a large size waits by those doors, because that's where the crowd will be.
>
> **Where it breaks:** in a real hall the crowd leaves and doesn't come back. In a market, once the stops have fired, price often snaps back, because the rush was forced, not a real change of opinion *(see 5.2)*.

> [!walkthrough] Step by step: how much is waiting under an obvious low
> EUR/USD has made **equal lows at 1.0780**. Numbers are illustrative.
> 1. **300 traders** are long with a stop about 10 pips under the low (≈1.0770), **0.5 lots** each: 300 × 0.5 = **150 lots** of sell stops.
> 2. **100 breakout traders** have sell-stop entries just under the low, **0.3 lots** each: 100 × 0.3 = **30 lots**.
> 3. **Total** = 150 + 30 = **180 lots** = 180 × 100,000 = **18 million euros** of market sells waiting in a few pips.
> 4. **Normal depth** nearby is about **20 lots per pip**. When the 180 lots fire, they eat through about 180 ÷ 20 ≈ **9 pips** almost instantly: that's the fast wick through the low.
> 5. **So what?** A fund that wants to **buy** 18 million euros can do it in seconds right there, at a price below the obvious low. If your stop is in that cluster, you are the fuel. Put it beyond the next structure or with a buffer *(see 3.5)*.

> [!check]- Check your understanding
> **Q1.** You are short EUR/USD. Your stop is just above the equal highs. Is your stop part of BSL or SSL?
> > [!answer]-
> > BSL. A short's stop is a **buy** order, and it rests above the highs.
> **Q2.** Why are equal highs a bigger pool than a single high?
> > [!answer]-
> > They're more obvious. More traders see them as resistance, short there with stops just above, and breakout traders place buy entries just above, so more orders pile up.
""")
L.before_callout("en", "action", """
> [!walkthrough] Step by step: which pool is the likely draw?
> Yesterday's high (PDH) is **1.0920** and yesterday's low (PDL) is **1.0850**. Price is now **1.0900**.
> 1. **Distance to PDH:** 1.0920 − 1.0900 = **20 pips**.
> 2. **Distance to PDL:** 1.0900 − 1.0850 = **50 pips**.
> 3. **Obviousness:** the PDH was also touched twice this week (equal highs) → bigger pool.
> 4. **HTF bias** (Phase 2): the daily trend is up.
> 5. **So what?** The closer, more obvious pool in the direction of the HTF trend (BSL at 1.0920) is the likely draw on liquidity. It's a working hypothesis, not a prediction: write it down before the session and check it afterwards.

> [!check]- Check your understanding
> **Q1.** Why does a fund that wants to sell a lot like price to rise into buy stops first?
> > [!answer]-
> > Because the buy stops become market buy orders. The fund can sell its large size into that buying at a high price, without pushing price down against itself.
> **Q2.** Which is external liquidity: the equal highs at the top of the range, or an FVG in the middle of the range?
> > [!answer]-
> > The equal highs (beyond the range). The FVG inside the range is internal liquidity.

> [!market]
> - **Forex:** no central order book; each broker sees only its own flow. Pools still form at obvious levels because traders everywhere use the same charts *(see 7.3)*.
> - **Gold:** round numbers (4,000, 4,100) and the Asian-session range are classic pools *(see 0.4)*.
> - **Stocks & index futures:** the previous day's high/low and the opening range attract stops; futures have a real, visible order book (DOM, *see 7.3*).
> - **Crypto:** pools are clearly visible as **liquidation levels** of leveraged positions, and sweeps through them can be violent *(see 0.7)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** In one sentence, what is liquidity and where does it pool?
> > [!answer]-
> > Liquidity is the resting orders available to trade against; it pools just beyond obvious highs and lows (equal highs/lows, PDH/PDL, session extremes, round numbers), where stops and breakout entries cluster.
> **Q2.** 200 longs each have a 0.2-lot stop under the same low. How many lots of market sells is that, and in which pool?
> > [!answer]-
> > 200 × 0.2 = 40 lots of sells, part of the SSL below the low.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ลองนึกถึงห้องคอนเสิร์ตที่คนแน่น คนส่วนใหญ่ยืนใกล้ประตูทางออก เผื่อมีอะไรผิดปกติจะได้ออกเร็ว ในตลาด "ประตูทางออก" คือ **คำสั่ง Stop-loss** และเทรดเดอร์มักวางไว้ที่เดียวกันที่เห็นชัด: เลยจุดสูงหรือจุดต่ำล่าสุดไปนิดเดียว เทรดเดอร์รายใหญ่ที่ต้องซื้อหรือขายจำนวนมากจะมองหาฝูงชนเหล่านั้น เพราะกองคำสั่งเป็นที่เดียวที่เขาซื้อขายจำนวนมากได้ในทีเดียว ราคาจึงเดินทางไปหาจุดสูงจุดต่ำที่ชัดเจนบ่อย ๆ: เพราะคำสั่งรออยู่ที่นั่น
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **สภาพคล่อง (Liquidity)** — คำสั่งที่พร้อมให้ซื้อขายด้วย ในที่นี้หมายถึง **คำสั่งที่รออยู่ (Resting order)** ในสมุดคำสั่งเป็นหลัก *(ดู 1.2)*
> - **คำสั่งที่รออยู่ (Resting order)** — คำสั่งที่วางไว้ล่วงหน้ารอราคา (Limit order หรือ Stop order ที่กลายเป็น Market order เมื่อราคาแตะ)
> - **Stop-loss (Stop order)** — คำสั่งที่ปิดไม้ที่ขาดทุนเมื่อราคาถึงระดับหนึ่ง Stop ของ Long คือคำสั่ง **ขาย** Stop ของ Short คือคำสั่ง **ซื้อ**
> - **Market order** — คำสั่งที่ซื้อขายทันทีที่ราคาดีที่สุดที่มี
> - **กองสภาพคล่อง (Liquidity pool)** — กลุ่มคำสั่งที่รออยู่ ณ บริเวณราคาเดียวกัน
> - **BSL (Buy-side liquidity)** — คำสั่งซื้อที่รออยู่ **เหนือ** จุดสูง (Stop ของ Short + คำสั่งซื้อ Breakout)
> - **SSL (Sell-side liquidity)** — คำสั่งขายที่รออยู่ **ใต้** จุดต่ำ (Stop ของ Long + คำสั่งขาย Breakdown)
> - **จุดสูงเท่ากัน / จุดต่ำเท่ากัน (Equal highs / lows)** — จุดสูง (หรือต่ำ) สองจุดขึ้นไปที่ราคาเกือบเท่ากัน เห็นชัดมาก จึงคนแน่นมาก
> - **PDH / PDL** — จุดสูง / ต่ำของวันก่อน **PWH / PWL** — จุดสูง / ต่ำของสัปดาห์ก่อน
> - **สภาพคล่องภายนอก / ภายใน (External / Internal liquidity)** — กองที่อยู่เลยจุดสูงและต่ำของกรอบปัจจุบัน / ความไม่สมดุลภายในกรอบ เช่น FVG *(ดู 5.4)*
> - **Draw on liquidity** — กองสภาพคล่องที่ราคาน่าจะไปหาต่อไป
> - **Slippage** — ได้ราคาแย่กว่าที่คาด เพราะคำสั่งที่ราคาของคุณมีไม่พอ *(ดู 0.1)*
> - **ICT (Inner Circle Trader)** — ผู้สอนออนไลน์ที่เฟสนี้ใช้คำศัพท์ของเขา
> - **HTF / MTF / LTF** — ไทม์เฟรมสูง / กลาง / ต่ำ *(ดู 1.5)*
> - **Pip / ล็อต** — หน่วยราคาเล็ก ๆ และขนาดไม้ในฟอเร็กซ์ *(ดู 0.3)*
""")
L.before_heading("th", "2.", """
![[p5-stop-cluster.th.svg]]

> [!analogy]
> Stop เปรียบเหมือน **ประตูทางออกของฝูงชน** ทุกคนในห้องเลือกประตูที่ใกล้และเห็นชัดที่สุด ถ้ามีคนตะโกนว่า "ไฟไหม้!" ทั้งฝูงก็พุ่งไปประตูเดียวกันพร้อมกัน การพุ่งนั้นคือกลุ่ม Stop ที่ทำงาน และเป็นเหตุผลที่ราคาวิ่งเร็วมากผ่านระดับที่ชัดเจน ผู้เล่นรายใหญ่ที่ต้องการซื้อขายขนาดใหญ่จะรออยู่ที่ประตูเหล่านั้น เพราะฝูงชนจะไปอยู่ตรงนั้น
>
> **จุดที่เปรียบเทียบไม่ได้:** ในห้องจริง ฝูงชนออกไปแล้วไม่กลับมา แต่ในตลาด เมื่อ Stop ทำงานหมดแล้ว ราคามักดีดกลับ เพราะการพุ่งนั้นเป็นการถูกบังคับ ไม่ใช่การเปลี่ยนความเห็นจริง *(ดู 5.2)*

> [!walkthrough] ไล่ทีละขั้น: มีอะไรรออยู่ใต้จุดต่ำที่ชัดเจนเท่าไหร่
> EUR/USD ทำ **จุดต่ำเท่ากันที่ 1.0780** ตัวเลขเป็นตัวอย่างประกอบ
> 1. **เทรดเดอร์ 300 คน** ถือ Long ตั้ง Stop ใต้จุดต่ำราว 10 pip (≈1.0770) คนละ **0.5 ล็อต**: 300 × 0.5 = Stop ขาย **150 ล็อต**
> 2. **เทรดเดอร์ Breakout 100 คน** ตั้งคำสั่ง Sell-stop ใต้จุดต่ำนิดเดียว คนละ **0.3 ล็อต**: 100 × 0.3 = **30 ล็อต**
> 3. **รวม** = 150 + 30 = **180 ล็อต** = 180 × 100,000 = คำสั่งขาย Market **18 ล้านยูโร** รออยู่ในไม่กี่ pip
> 4. **ความลึกปกติ** แถวนั้นราว **20 ล็อตต่อ pip** เมื่อ 180 ล็อตทำงาน จะกินราคาลงไปราว 180 ÷ 20 ≈ **9 pip** แทบทันที: นั่นคือไส้เทียนที่ทะลุจุดต่ำอย่างรวดเร็ว
> 5. **แล้วไง?** กองทุนที่อยากซื้อ 18 ล้านยูโรทำได้ในไม่กี่วินาทีตรงนั้น ที่ราคาต่ำกว่าจุดต่ำที่ชัดเจน ถ้า Stop ของคุณอยู่ในกลุ่มนั้น คุณคือเชื้อเพลิง วาง Stop เลยโครงสร้างถัดไป หรือเผื่อระยะไว้ *(ดู 3.5)*

> [!check]- เช็กความเข้าใจ
> **Q1.** คุณ Short EUR/USD และตั้ง Stop เหนือจุดสูงเท่ากันนิดเดียว Stop ของคุณเป็นส่วนหนึ่งของ BSL หรือ SSL?
> > [!answer]-
> > BSL Stop ของ Short คือคำสั่ง **ซื้อ** และรออยู่เหนือจุดสูง
> **Q2.** ทำไมจุดสูงเท่ากันจึงเป็นกองที่ใหญ่กว่าจุดสูงจุดเดียว?
> > [!answer]-
> > เพราะเห็นชัดกว่า เทรดเดอร์มองว่าเป็นแนวต้านมากกว่า จึง Short ตรงนั้นพร้อม Stop เหนือขึ้นไปนิดเดียว และเทรดเดอร์ Breakout ก็วางคำสั่งซื้อเหนือขึ้นไป คำสั่งจึงกองมากขึ้น
""")
L.before_callout("th", "action", """
> [!walkthrough] ไล่ทีละขั้น: กองไหนน่าจะเป็นเป้าหมายที่ราคาถูกดึงไป?
> จุดสูงเมื่อวาน (PDH) คือ **1.0920** และจุดต่ำเมื่อวาน (PDL) คือ **1.0850** ราคาตอนนี้ **1.0900**
> 1. **ระยะถึง PDH:** 1.0920 − 1.0900 = **20 pip**
> 2. **ระยะถึง PDL:** 1.0900 − 1.0850 = **50 pip**
> 3. **ความชัดเจน:** PDH ยังถูกแตะสองครั้งในสัปดาห์นี้ (จุดสูงเท่ากัน) → กองใหญ่กว่า
> 4. **Bias ของ HTF** (เฟส 2): เทรนด์รายวันเป็นขาขึ้น
> 5. **แล้วไง?** กองที่ใกล้กว่าและชัดกว่าในทิศทางของเทรนด์ HTF (BSL ที่ 1.0920) น่าจะเป็น Draw on liquidity เป็นสมมติฐานในการทำงาน ไม่ใช่คำทำนาย เขียนไว้ก่อนเซสชันแล้วตรวจทีหลัง

> [!check]- เช็กความเข้าใจ
> **Q1.** ทำไมกองทุนที่อยากขายจำนวนมากจึงชอบให้ราคาขึ้นไปหา Buy stop ก่อน?
> > [!answer]-
> > เพราะ Buy stop กลายเป็นคำสั่งซื้อ Market กองทุนจึงขายขนาดใหญ่ใส่แรงซื้อนั้นได้ที่ราคาสูง โดยไม่ต้องกดราคาลงด้วยตัวเอง
> **Q2.** อะไรคือสภาพคล่องภายนอก: จุดสูงเท่ากันที่ยอดกรอบ หรือ FVG กลางกรอบ?
> > [!answer]-
> > จุดสูงเท่ากัน (อยู่นอกกรอบ) ส่วน FVG ภายในกรอบคือสภาพคล่องภายใน

> [!market]
> - **ฟอเร็กซ์:** ไม่มีสมุดคำสั่งกลาง แต่ละโบรกเกอร์เห็นแค่คำสั่งของตัวเอง แต่กองยังเกิดที่ระดับชัดเจน เพราะเทรดเดอร์ทุกที่ดูกราฟเดียวกัน *(ดู 7.3)*
> - **ทองคำ:** เลขกลม (4,000, 4,100) และกรอบราคาช่วงเอเชียคือกองคลาสสิก *(ดู 0.4)*
> - **หุ้นและฟิวเจอร์สดัชนี:** จุดสูง/ต่ำของวันก่อนและกรอบช่วงเปิดตลาดดึงดูด Stop ฟิวเจอร์สมีสมุดคำสั่งจริงที่มองเห็นได้ (DOM *ดู 7.3*)
> - **คริปโต:** กองมองเห็นได้ชัดเป็น **ราคาล้างพอร์ต** ของโพซิชันที่ใช้เลเวอเรจ และการกวาดผ่านจุดเหล่านั้นอาจรุนแรงมาก *(ดู 0.7)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** ตอบประโยคเดียว: สภาพคล่องคืออะไร และกองอยู่ที่ไหน?
> > [!answer]-
> > สภาพคล่องคือคำสั่งที่รออยู่ให้ซื้อขายด้วย กองอยู่เลยจุดสูงจุดต่ำที่ชัดเจน (จุดสูง/ต่ำเท่ากัน PDH/PDL จุดสุดของเซสชัน เลขกลม) ที่ Stop และคำสั่ง Breakout รวมตัวกัน
> **Q2.** Long 200 คน ตั้ง Stop คนละ 0.2 ล็อตใต้จุดต่ำเดียวกัน รวมเป็นคำสั่งขาย Market กี่ล็อต และอยู่ในกองไหน?
> > [!answer]-
> > 200 × 0.2 = คำสั่งขาย 40 ล็อต เป็นส่วนหนึ่งของ SSL ใต้จุดต่ำ
""")

L.set_meta("level", "v2")
L.save()
