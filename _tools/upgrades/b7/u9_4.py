"""B7 · v2 upgrade of 9.4 Tick Data & Market Internals ($TICK) (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("09 Quant & Data Analysis/9.4 Tick Data & Market Internals ($TICK).md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> An index like the S&P 500 is one number made from hundreds of stocks. It can rise because almost every stock is rising, or because two giant companies are rising while most others fall. **Market internals** look underneath the index and count: how many stocks are going up right now, how much money is flowing into rising stocks, how urgent the buying or selling is. A move with broad support is healthier than one carried by a few names.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Market internals / breadth** — measures of how many stocks, and how much volume, take part in a move.
> - **NYSE** — the New York Stock Exchange; most internals are calculated from its stocks.
> - **Uptick / downtick** — a trade at a higher / lower price than the previous trade in that stock.
> - **$TICK** — the number of NYSE stocks whose last trade was an uptick minus those on a downtick, updated every second.
> - **$ADD (advance–decline)** — advancing stocks minus declining stocks today.
> - **$VOLD** — volume in rising stocks minus volume in falling stocks.
> - **$TRIN (Arms index)** — (advancers ÷ decliners) ÷ (up volume ÷ down volume); below 1 = bullish volume, above 1 = bearish.
> - **VIX** — expected 30-day S&P 500 volatility from option prices *(see 6.6)*.
> - **SPY / ES / NQ** — the S&P 500 ETF / E-mini S&P 500 futures / E-mini Nasdaq-100 futures *(see 0.2, 7.3)*.
> - **Program trading** — large computer-driven orders that buy or sell many stocks at once.
> - **Capitulation** — a final burst of panic selling that often marks a low.
""")
L.before_heading("en", "2.", """
> [!walkthrough] Step by step: calculating $TRIN by hand
> At 11:00 New York time: **2,000** stocks advancing, **1,000** declining; up volume **1.5 bn** shares, down volume **0.5 bn**.
> 1. **Advance/decline ratio** = 2,000 ÷ 1,000 = **2.0**.
> 2. **Up/down volume ratio** = 1.5 ÷ 0.5 = **3.0**.
> 3. **$TRIN** = 2.0 ÷ 3.0 ≈ **0.67**.
> 4. **Read:** below 1 → volume is flowing into rising stocks even more strongly than the count of rising stocks suggests: bullish.
> 5. **$ADD** at the same time = 2,000 − 1,000 = **+1,000**: broad participation.
> 6. **So what?** You can check in seconds whether an index rally is broad (most stocks and most volume rising) or narrow.

> [!check]- Check your understanding: the measures
> **Q1.** The S&P 500 is up 0.6%, but $ADD is −400. What does that suggest?
> > [!answer]-
> > A narrow rally: a few heavyweight stocks are lifting the index while most stocks fall. Less trustworthy, especially for breakouts.
""")
L.before_heading("en", "3.", """
![[p9-tick-extremes.en.svg]]

> [!walkthrough] Step by step: reading $TICK extremes at a level (illustrative)
> ES (S&P 500 futures) is falling into a marked HTF support at **5,000**.
> 1. **$TICK −1,150** as price touches **4,999.50**: almost every NYSE stock is ticking down at once, a program-selling burst. But price holds the level.
> 2. **Next readings:** −600, then **−350**: the selling urgency fades while price stays at 5,000. Effort without result, like absorption *(see 7.6)*.
> 3. **CHoCH up:** price breaks the last lower high and $TICK swings to **+900**: buyers now in control. This is the long trigger, with the stop below 4,999.50.
> 4. **Later, $TICK +1,050** at a new high **in the trend direction**: not a reason to short. In strong trends, extremes come with continuation.
> 5. **So what?** A ±1,000 $TICK reading only matters **at a level you already marked**, and its meaning depends on whether price keeps moving (continuation) or stalls (exhaustion or absorption).

> [!check]- Check your understanding: $TICK
> **Q1.** On a strong up day, $TICK hits +1,000 three times and price keeps rising. Should you short each +1,000 reading?
> > [!answer]-
> > No. In a trend, extremes in the trend direction show strength. Only fade an extreme at a level where price stalls and structure shifts.
""")
L.before_callout("en", "example", """
> [!analogy]
> The index is the **scoreboard**; internals are **how many fans are cheering**. A team can be ahead on the scoreboard while half the stadium has gone quiet. If the lead comes from one lucky goal and the crowd is silent, it's more fragile than a lead built on pressure from the whole team.
>
> **Where it breaks:** fans don't change the score. In markets, the "fans" (stocks and their buyers) are the score: if most stocks fall, the index eventually feels it.

> [!check]- Check your understanding: internals as a filter
> **Q1.** The index breaks above yesterday's high, $ADD is +1,700 and $VOLD strongly positive. How should that change your view of the breakout?
> > [!answer]-
> > It supports the breakout: broad participation (initiative buying). You can trust it more and use trend tactics.
""")
L.before_callout("en", "action", """
> [!market]
> - **Stocks & indices:** internals are built for US stocks (NYSE/Nasdaq) and US index trading (ES, NQ, SPY). Thai traders can use SET advance/decline counts in a similar way for the Thai market *(see 0.5)*.
> - **Forex:** no equivalent; use the DXY or several pairs together as a rough "breadth" of the dollar *(see 0.3)*.
> - **Gold:** no breadth measure; gold miners or GLD flows are only loose proxies *(see 0.4)*.
> - **Crypto:** some data providers count how many large coins are rising; much noisier, and dominated by Bitcoin *(see 0.7)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Define $TICK, $ADD and $TRIN in one line each.
> > [!answer]-
> > $TICK: NYSE stocks on an uptick minus those on a downtick, right now. $ADD: advancing minus declining stocks today. $TRIN: (advancers ÷ decliners) ÷ (up volume ÷ down volume); below 1 bullish.
> **Q2.** Where does a −1,000 $TICK reading matter most?
> > [!answer]-
> > At a pre-marked support level where price stops falling: a possible capitulation or absorption, to be confirmed by a price trigger.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ดัชนีอย่าง S&P 500 คือตัวเลขเดียวที่ทำจากหุ้นหลายร้อยตัว มันขึ้นได้เพราะหุ้นเกือบทุกตัวขึ้น หรือเพราะบริษัทยักษ์สองบริษัทขึ้นขณะที่ตัวอื่นส่วนใหญ่ลง **Market internals** มองลึกลงไปใต้ดัชนีแล้วนับ: ตอนนี้มีหุ้นกี่ตัวที่ขึ้น เงินไหลเข้าหุ้นที่กำลังขึ้นมากแค่ไหน การซื้อหรือขายเร่งด่วนแค่ไหน การวิ่งที่มีแรงหนุนกว้างแข็งแรงกว่าการวิ่งที่ถูกแบกด้วยหุ้นไม่กี่ตัว
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **Market internals / Breadth (ความกว้างของตลาด)** — ตัววัดว่ามีหุ้นกี่ตัว และวอลุ่มเท่าไหร่ที่มีส่วนร่วมในการวิ่ง
> - **NYSE** — ตลาดหลักทรัพย์นิวยอร์ก Internals ส่วนใหญ่คำนวณจากหุ้นในตลาดนี้
> - **Uptick / Downtick** — การซื้อขายที่ราคาสูงกว่า / ต่ำกว่าการซื้อขายครั้งก่อนของหุ้นตัวนั้น
> - **$TICK** — จำนวนหุ้น NYSE ที่การซื้อขายล่าสุดเป็น Uptick ลบด้วยตัวที่เป็น Downtick อัปเดตทุกวินาที
> - **$ADD (Advance–decline)** — จำนวนหุ้นที่ขึ้นลบจำนวนหุ้นที่ลงในวันนี้
> - **$VOLD** — วอลุ่มของหุ้นที่ขึ้นลบวอลุ่มของหุ้นที่ลง
> - **$TRIN (Arms index)** — (หุ้นขึ้น ÷ หุ้นลง) ÷ (วอลุ่มขึ้น ÷ วอลุ่มลง) ต่ำกว่า 1 = วอลุ่มเป็นบวก สูงกว่า 1 = เป็นลบ
> - **VIX** — ความผันผวน 30 วันที่คาดของ S&P 500 จากราคาออปชัน *(ดู 6.6)*
> - **SPY / ES / NQ** — ETF ของ S&P 500 / ฟิวเจอร์ส E-mini S&P 500 / ฟิวเจอร์ส E-mini Nasdaq-100 *(ดู 0.2, 7.3)*
> - **Program trading** — คำสั่งขนาดใหญ่ที่ขับด้วยคอมพิวเตอร์ ซื้อหรือขายหุ้นหลายตัวพร้อมกัน
> - **Capitulation (การยอมแพ้)** — แรงขายตื่นตระหนกครั้งสุดท้าย มักเป็นจุดต่ำ
""")
L.before_heading("th", "2.", """
> [!walkthrough] ไล่ทีละขั้น: คำนวณ $TRIN ด้วยมือ
> เวลา 11:00 นิวยอร์ก: หุ้นขึ้น **2,000** ตัว ลง **1,000** ตัว วอลุ่มขึ้น **1.5 พันล้าน** หุ้น วอลุ่มลง **0.5 พันล้าน**
> 1. **อัตราส่วนขึ้น/ลง** = 2,000 ÷ 1,000 = **2.0**
> 2. **อัตราส่วนวอลุ่มขึ้น/ลง** = 1.5 ÷ 0.5 = **3.0**
> 3. **$TRIN** = 2.0 ÷ 3.0 ≈ **0.67**
> 4. **อ่าน:** ต่ำกว่า 1 → วอลุ่มไหลเข้าหุ้นที่ขึ้นแรงกว่าที่จำนวนหุ้นที่ขึ้นบอกด้วยซ้ำ: เป็นบวก
> 5. **$ADD** ณ เวลาเดียวกัน = 2,000 − 1,000 = **+1,000**: การมีส่วนร่วมกว้าง
> 6. **แล้วไง?** คุณเช็กได้ในไม่กี่วินาทีว่าดัชนีที่ขึ้นนั้นกว้าง (หุ้นส่วนใหญ่และวอลุ่มส่วนใหญ่ขึ้น) หรือแคบ

> [!check]- เช็กความเข้าใจ: ตัวชี้วัด
> **Q1.** S&P 500 ขึ้น 0.6% แต่ $ADD เป็น −400 บอกอะไร?
> > [!answer]-
> > การขึ้นแบบแคบ: หุ้นน้ำหนักมากไม่กี่ตัวยกดัชนีขึ้น ขณะที่หุ้นส่วนใหญ่ลง เชื่อถือได้น้อยกว่า โดยเฉพาะกับการทะลุ
""")
L.before_heading("th", "3.", """
![[p9-tick-extremes.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: อ่านค่าสุดขั้วของ $TICK ที่ระดับราคา (ภาพประกอบ)
> ES (ฟิวเจอร์ส S&P 500) กำลังลงไปหาแนวรับ HTF ที่ทำเครื่องหมายไว้ที่ **5,000**
> 1. **$TICK −1,150** ขณะที่ราคาแตะ **4,999.50**: หุ้น NYSE เกือบทุกตัว Downtick พร้อมกัน เป็นแรงขายแบบ Program แต่ราคายืนระดับได้
> 2. **ค่าถัดไป:** −600 แล้ว **−350**: ความเร่งด่วนของแรงขายจางลง ขณะที่ราคายังอยู่ที่ 5,000 มีความพยายามแต่ไม่มีผล เหมือน Absorption *(ดู 7.6)*
> 3. **CHoCH ขึ้น:** ราคาทะลุ Lower high ล่าสุด และ $TICK แกว่งไป **+900**: ผู้ซื้อคุมแล้ว นี่คือสัญญาณ Long Stop ใต้ 4,999.50
> 4. **ทีหลัง $TICK +1,050** ที่จุดสูงใหม่ **ในทิศทางของเทรนด์**: ไม่ใช่เหตุผลให้ Short ในเทรนด์แรง ค่าสุดขั้วมาพร้อมการไปต่อ
> 5. **แล้วไง?** ค่า $TICK ±1,000 สำคัญเฉพาะ **ที่ระดับที่คุณทำเครื่องหมายไว้แล้ว** และความหมายขึ้นกับว่าราคาวิ่งต่อ (ไปต่อ) หรือหยุด (เหนื่อยล้าหรือถูกดูดซับ)

> [!check]- เช็กความเข้าใจ: $TICK
> **Q1.** ในวันขาขึ้นแรง $TICK แตะ +1,000 สามครั้งและราคายังขึ้นต่อ ควร Short ทุกครั้งที่แตะ +1,000 ไหม?
> > [!answer]-
> > ไม่ ในเทรนด์ ค่าสุดขั้วในทิศทางเทรนด์แสดงความแข็งแรง จะสวนค่าสุดขั้วเฉพาะที่ระดับที่ราคาหยุดและโครงสร้างเปลี่ยน
""")
L.before_callout("th", "example", """
> [!analogy]
> ดัชนีคือ **ป้ายสกอร์** Internals คือ **จำนวนแฟนบอลที่กำลังเชียร์** ทีมอาจนำบนป้ายสกอร์ ขณะที่ครึ่งสนามเงียบไปแล้ว ถ้าความนำมาจากลูกฟลุกลูกเดียวและกองเชียร์เงียบ ก็เปราะบางกว่าความนำที่มาจากการกดดันของทั้งทีม
>
> **จุดที่เปรียบเทียบไม่ได้:** แฟนบอลไม่ได้เปลี่ยนสกอร์ แต่ในตลาด "แฟนบอล" (หุ้นและผู้ซื้อของมัน) คือสกอร์เอง ถ้าหุ้นส่วนใหญ่ลง ดัชนีก็จะรู้สึกในที่สุด

> [!check]- เช็กความเข้าใจ: Internals เป็นตัวกรอง
> **Q1.** ดัชนีทะลุเหนือจุดสูงเมื่อวาน $ADD อยู่ที่ +1,700 และ $VOLD เป็นบวกแรง ควรเปลี่ยนมุมมองต่อการทะลุอย่างไร?
> > [!answer]-
> > สนับสนุนการทะลุ: มีส่วนร่วมกว้าง (แรงซื้อเชิงริเริ่ม) เชื่อถือได้มากขึ้น และใช้แท็กติกแบบตามเทรนด์ได้
""")
L.before_callout("th", "action", """
> [!market]
> - **หุ้นและดัชนี:** Internals สร้างมาสำหรับหุ้นสหรัฐ (NYSE/Nasdaq) และการเทรดดัชนีสหรัฐ (ES, NQ, SPY) เทรดเดอร์ไทยใช้จำนวนหุ้นขึ้น/ลงของ SET แบบคล้ายกันกับตลาดไทยได้ *(ดู 0.5)*
> - **ฟอเร็กซ์:** ไม่มีตัวเทียบเท่า ใช้ DXY หรือดูหลายคู่เงินพร้อมกันเป็น "ความกว้าง" ของดอลลาร์คร่าว ๆ *(ดู 0.3)*
> - **ทองคำ:** ไม่มีตัววัดความกว้าง หุ้นเหมืองทองหรือกระแสเงินของ GLD เป็นแค่ตัวแทนหลวม ๆ *(ดู 0.4)*
> - **คริปโต:** ผู้ให้ข้อมูลบางรายนับว่ามีเหรียญใหญ่กี่ตัวที่ขึ้น มีสัญญาณรบกวนมากกว่ามาก และ Bitcoin ครอบงำ *(ดู 0.7)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** นิยาม $TICK, $ADD และ $TRIN ข้อละบรรทัด
> > [!answer]-
> > $TICK: หุ้น NYSE ที่ Uptick ลบตัวที่ Downtick ณ ตอนนี้ $ADD: หุ้นที่ขึ้นลบหุ้นที่ลงในวันนี้ $TRIN: (หุ้นขึ้น ÷ หุ้นลง) ÷ (วอลุ่มขึ้น ÷ วอลุ่มลง) ต่ำกว่า 1 เป็นบวก
> **Q2.** ค่า $TICK −1,000 สำคัญที่สุดตรงไหน?
> > [!answer]-
> > ที่แนวรับที่ทำเครื่องหมายไว้ก่อน ซึ่งราคาหยุดลง: อาจเป็น Capitulation หรือ Absorption ที่ต้องยืนยันด้วยสัญญาณจากราคา
""")

L.set_meta("level", "v2")
L.save()
