"""B8 · v2 upgrade of 10.5 How Wall Street Works (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("10 Macro, Wall Street & Investing/10.5 How Wall Street Works.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Wall Street is a big marketplace with many kinds of players: companies that need money, banks that help them raise it, brokers who take your orders, and giant funds that invest other people's savings. Each one gets paid in a different way, and that shapes what they do and say. Some of their trades follow fixed rules and calendars, so you can see them coming.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Sell side** — firms that sell services: investment banks, brokers, research, market makers.
> - **Buy side** — firms that invest money: pension funds, mutual funds, ETFs, hedge funds.
> - **IPO (initial public offering)** — a company selling its shares to the public for the first time.
> - **M&A (mergers and acquisitions)** — companies buying or combining with each other.
> - **Market maker** — a firm that always quotes a buy and a sell price and earns the spread *(see 0.1)*.
> - **PFOF (payment for order flow)** — a broker being paid by a market maker to send it your orders.
> - **Dark pool** — a private trading venue where orders aren't shown publicly *(see 7.3)*.
> - **Benchmark** — the index a fund is measured against.
> - **Rebalancing** — trading back to target weights after prices move.
> - **CTA (commodity trading advisor)** — a systematic, usually trend-following fund.
> - **Buyback** — a company buying its own shares in the market.
> - **Triple witching** — the quarterly day when stock options, index options and index futures expire together *(see 8.5)*.
> - **Front-running** — trading ahead of a flow you know is coming.
""")
L.before_heading("en", "2.", """
> [!analogy]
> Wall Street is like a **professional sports league**. The players (funds) are judged against each other and against the league average (the benchmark), the league takes a cut of every ticket (exchanges and brokers), and the agents (banks) earn on every transfer (deal).
>
> **Where it breaks:** in sports you can only watch. In markets you're also on the field, and the "league" earns money from your activity whether you win or lose.

> [!check]- Check your understanding: who earns what
> **Q1.** Your free trading app is paid by a market maker for your orders. What is this called, and what's the conflict?
> > [!answer]-
> > Payment for order flow (PFOF). The broker earns more when you trade more, so the app has a reason to encourage frequent trading, which usually hurts you.
""")
L.before_heading("en", "3.", """
![[p10-inclusion-flow.en.svg]]

> [!walkthrough] Step by step: sizing an index-inclusion flow
> 1. A company worth **10 bn USD** will join an index. Index funds own about **15%** of every member (illustrative).
> 2. Forced buying = 10 bn × 15% = **1.5 bn USD**.
> 3. The stock normally trades **200 m USD** a day → 1.5 bn ÷ 200 m = **7.5 days** of normal volume, concentrated at one closing auction.
> 4. **So what?** A flow this large relative to volume moves price. The move often happens between announcement and inclusion, and may fade after.

> [!walkthrough] Step by step: month-end pension rebalancing
> 1. A pension fund has **100 bn** with a **60/40** stock/bond target.
> 2. During the month stocks rise **5%** → stocks **63**, bonds **40**, total **103** (stocks now 61.2%).
> 3. Target stocks = 60% × 103 = **61.8** → the fund must **sell 1.2 bn** of stocks and buy bonds near month-end.
> 4. **So what?** After a strong month for stocks, month-end flows can be a headwind for stocks, and the reverse after a weak month. It's a tendency, not a guarantee.

> [!check]- Check your understanding: mechanical flows
> **Q1.** Why are these flows partly predictable?
> > [!answer]-
> > They follow rules and calendars (index methodology, target weights, expiry dates), not opinions, so their timing and direction are known in advance.
""")
L.before_heading("en", "4.", """
> [!check]- Check your understanding: reading critically
> **Q1.** An analyst raises a price target right after the stock has risen 20%. What should you conclude?
> > [!answer]-
> > Price targets often follow price. Treat it as information about sentiment, not as an independent forecast; ask who benefits if you act on it.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** month-end "fixing" flows (e.g. the London 4 pm fix, 22:00/23:00 Bangkok time) can move major pairs *(see 0.3)*.
> - **Gold:** central-bank and ETF flows are the big buy-side players *(see 0.4)*.
> - **Stocks:** index inclusions, buybacks, OPEX and pension rebalancing are the main mechanical flows *(see 0.5, 0.6)*.
> - **Crypto:** spot ETF flows and exchange listings act like inclusions; exchanges themselves are often broker, market maker and custodian at once *(see 0.7)*.

> [!caution]
> Trying to front-run known flows is crowded: many professionals do the same, so the move can happen early or reverse sharply. Treat flow dates as context and risk windows, and keep normal position sizes.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Name one sell-side and one buy-side player, and how each is paid.
> > [!answer]-
> > Sell side: an investment bank, paid fees for IPOs and M&A (or a broker, paid commissions/spreads). Buy side: a pension fund or ETF, paid management fees and judged on returns against a benchmark.
> **Q2.** Give two advantages a small, patient investor has over a large fund.
> > [!answer]-
> > Any two of: no benchmark pressure (can hold cash), small size (no price impact), long horizon, no forced selling without excessive leverage.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> วอลล์สตรีทคือตลาดใหญ่ที่มีผู้เล่นหลายแบบ: บริษัทที่ต้องการเงิน ธนาคารที่ช่วยระดมเงิน โบรกเกอร์ที่รับคำสั่งของคุณ และกองทุนยักษ์ที่ลงทุนเงินออมของคนอื่น แต่ละรายได้เงินคนละแบบ ซึ่งกำหนดสิ่งที่พวกเขาทำและพูด การซื้อขายบางส่วนของพวกเขาทำตามกฎและปฏิทินที่ตายตัว คุณจึงมองเห็นล่วงหน้าได้
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **ฝั่งขาย (Sell side)** — บริษัทที่ขายบริการ: วาณิชธนกิจ โบรกเกอร์ ฝ่ายวิจัย Market maker
> - **ฝั่งซื้อ (Buy side)** — บริษัทที่ลงทุนเงิน: กองทุนบำนาญ กองทุนรวม ETF เฮดจ์ฟันด์
> - **IPO (Initial public offering)** — บริษัทขายหุ้นให้ประชาชนเป็นครั้งแรก
> - **M&A (Mergers and acquisitions)** — บริษัทซื้อหรือควบรวมกัน
> - **ผู้ดูแลสภาพคล่อง (Market maker)** — บริษัทที่เสนอราคาซื้อและขายตลอดเวลาและได้กำไรจาก Spread *(ดู 0.1)*
> - **PFOF (Payment for order flow)** — โบรกเกอร์ได้เงินจาก Market maker เพื่อส่งคำสั่งของคุณไปให้
> - **Dark pool** — สถานที่ซื้อขายส่วนตัวที่ไม่แสดงคำสั่งต่อสาธารณะ *(ดู 7.3)*
> - **ดัชนีอ้างอิง (Benchmark)** — ดัชนีที่ใช้วัดผลกองทุน
> - **การปรับสมดุล (Rebalancing)** — ซื้อขายกลับไปที่น้ำหนักเป้าหมายหลังราคาเปลี่ยน
> - **CTA (Commodity trading advisor)** — กองทุนเชิงระบบ ส่วนใหญ่ตามเทรนด์
> - **การซื้อหุ้นคืน (Buyback)** — บริษัทซื้อหุ้นตัวเองในตลาด
> - **Triple witching** — วันรายไตรมาสที่ออปชันหุ้น ออปชันดัชนี และฟิวเจอร์สดัชนีหมดอายุพร้อมกัน *(ดู 8.5)*
> - **Front-running** — ซื้อขายดักหน้ากระแสเงินที่รู้ว่าจะมา
""")
L.before_heading("th", "2.", """
> [!analogy]
> วอลล์สตรีทเหมือน **ลีกกีฬาอาชีพ** ผู้เล่น (กองทุน) ถูกตัดสินเทียบกันเองและเทียบค่าเฉลี่ยลีก (Benchmark) ลีกหักส่วนแบ่งจากตั๋วทุกใบ (ตลาดหลักทรัพย์และโบรกเกอร์) และเอเจนต์ (ธนาคาร) ได้เงินจากการย้ายทีมทุกครั้ง (ดีล)
>
> **จุดที่เปรียบเทียบไม่ได้:** ในกีฬาคุณได้แค่ดู แต่ในตลาดคุณอยู่ในสนามด้วย และ "ลีก" ได้เงินจากกิจกรรมของคุณไม่ว่าคุณจะชนะหรือแพ้

> [!check]- เช็กความเข้าใจ: ใครได้เงินจากอะไร
> **Q1.** แอปเทรดฟรีของคุณได้เงินจาก Market maker สำหรับคำสั่งของคุณ เรียกว่าอะไร และมีผลประโยชน์ทับซ้อนอะไร?
> > [!answer]-
> > Payment for order flow (PFOF) โบรกเกอร์ได้มากขึ้นเมื่อคุณเทรดมากขึ้น แอปจึงมีเหตุผลที่จะกระตุ้นให้เทรดบ่อย ซึ่งมักทำร้ายคุณ
""")
L.before_heading("th", "3.", """
![[p10-inclusion-flow.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ประเมินขนาดกระแสเงินจากการเข้าดัชนี
> 1. บริษัทมูลค่า **10 พันล้านดอลลาร์** จะเข้าดัชนี กองทุนดัชนีถือราว **15%** ของทุกสมาชิก (ตัวอย่าง)
> 2. แรงซื้อบังคับ = 10 พันล้าน × 15% = **1.5 พันล้านดอลลาร์**
> 3. หุ้นปกติซื้อขาย **200 ล้านดอลลาร์** ต่อวัน → 1.5 พันล้าน ÷ 200 ล้าน = **7.5 วัน** ของวอลุ่มปกติ กระจุกในการประมูลปิดตลาดครั้งเดียว
> 4. **แล้วไง?** กระแสเงินที่ใหญ่ขนาดนี้เทียบกับวอลุ่มย่อมขยับราคา การขยับมักเกิดระหว่างวันประกาศถึงวันเข้าดัชนี และอาจจางลงหลังจากนั้น

> [!walkthrough] ไล่ทีละขั้น: การปรับสมดุลสิ้นเดือนของกองทุนบำนาญ
> 1. กองทุนบำนาญมี **100 พันล้าน** เป้าหมายหุ้น/พันธบัตร **60/40**
> 2. ระหว่างเดือนหุ้นขึ้น **5%** → หุ้น **63** พันธบัตร **40** รวม **103** (หุ้นตอนนี้ 61.2%)
> 3. เป้าหุ้น = 60% × 103 = **61.8** → กองทุนต้อง **ขายหุ้น 1.2 พันล้าน** และซื้อพันธบัตรช่วงใกล้สิ้นเดือน
> 4. **แล้วไง?** หลังเดือนที่หุ้นขึ้นแรง กระแสเงินสิ้นเดือนอาจเป็นแรงต้านของหุ้น และกลับกันหลังเดือนที่อ่อนแอ เป็นแนวโน้ม ไม่ใช่การรับประกัน

> [!check]- เช็กความเข้าใจ: กระแสเงินเชิงกลไก
> **Q1.** ทำไมกระแสเงินเหล่านี้จึงคาดการณ์ได้บางส่วน?
> > [!answer]-
> > มันทำตามกฎและปฏิทิน (วิธีคำนวณดัชนี น้ำหนักเป้าหมาย วันหมดอายุ) ไม่ใช่ความเห็น จังหวะและทิศทางจึงรู้ล่วงหน้า
""")
L.before_heading("th", "4.", """
> [!check]- เช็กความเข้าใจ: อ่านอย่างมีวิจารณญาณ
> **Q1.** นักวิเคราะห์ปรับราคาเป้าหมายขึ้นทันทีหลังหุ้นขึ้นไป 20% คุณควรสรุปอะไร?
> > [!answer]-
> > ราคาเป้าหมายมักตามราคา ให้มองเป็นข้อมูลเรื่องอารมณ์ตลาด ไม่ใช่การพยากรณ์อิสระ และถามว่าใครได้ประโยชน์ถ้าคุณทำตาม
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** กระแสเงิน "Fixing" สิ้นเดือน (เช่น London 4 pm fix 22:00/23:00 เวลากรุงเทพฯ) ขยับคู่เงินหลักได้ *(ดู 0.3)*
> - **ทองคำ:** กระแสเงินจากธนาคารกลางและ ETF คือผู้เล่นฝั่งซื้อรายใหญ่ *(ดู 0.4)*
> - **หุ้น:** การเข้าดัชนี Buyback, OPEX และการปรับสมดุลของกองทุนบำนาญคือกระแสเงินเชิงกลไกหลัก *(ดู 0.5, 0.6)*
> - **คริปโต:** กระแสเงิน Spot ETF และการลิสต์บนกระดานเทรดทำหน้าที่คล้ายการเข้าดัชนี กระดานเทรดเองมักเป็นทั้งโบรกเกอร์ Market maker และผู้รับฝากในคราวเดียว *(ดู 0.7)*

> [!caution]
> การดักหน้ากระแสเงินที่รู้ล่วงหน้าเป็นเกมที่แออัด มืออาชีพจำนวนมากทำเหมือนกัน การขยับจึงอาจเกิดก่อนเวลาหรือกลับตัวรุนแรง ให้ใช้วันของกระแสเงินเป็นบริบทและช่วงเวลาเสี่ยง และคงขนาดโพซิชันปกติ
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกผู้เล่นฝั่งขายหนึ่งรายและฝั่งซื้อหนึ่งราย และแต่ละรายได้เงินอย่างไร
> > [!answer]-
> > ฝั่งขาย: วาณิชธนกิจ ได้ค่าธรรมเนียมจาก IPO และ M&A (หรือโบรกเกอร์ ได้ค่าคอมมิชชัน/Spread) ฝั่งซื้อ: กองทุนบำนาญหรือ ETF ได้ค่าธรรมเนียมการจัดการ และถูกวัดผลเทียบ Benchmark
> **Q2.** บอกข้อได้เปรียบสองข้อที่นักลงทุนรายเล็กที่อดทนมีเหนือกองทุนใหญ่
> > [!answer]-
> > สองข้อใดก็ได้: ไม่มีแรงกดดันจาก Benchmark (ถือเงินสดได้), ขนาดเล็ก (ไม่กระทบราคา), ระยะเวลายาว, ไม่ถูกบังคับขายถ้าไม่ใช้เลเวอเรจเกินไป
""")

L.set_meta("level", "v2")
L.save()
