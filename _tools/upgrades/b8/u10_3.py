"""B8 · v2 upgrade of 10.3 Economic Data & Event Risk (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("10 Macro, Wall Street & Investing/10.3 Economic Data & Event Risk.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Some of the biggest price jumps happen at times you can know weeks in advance: when governments publish inflation or jobs numbers, or when central banks announce interest rates. Before each release, economists publish a forecast. Prices already reflect that forecast, so what moves the market is how different the real number is. Your job isn't to guess the number; it's to know when it's coming and make sure a surprise can't hurt you badly.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Economic calendar** — a schedule of upcoming data releases and central-bank meetings *(see 0.8)*.
> - **CPI (Consumer Price Index)** — the main monthly measure of inflation; **core CPI** excludes food and energy.
> - **PCE (Personal Consumption Expenditures) price index** — the inflation measure the Fed prefers.
> - **NFP (Nonfarm payrolls)** — the number of US jobs added last month, released on the first Friday.
> - **GDP (gross domestic product)** — the total output of the economy *(see 10.1)*.
> - **ISM / PMI** — business surveys of manufacturing and services *(see 10.1)*.
> - **FOMC (Federal Open Market Committee)** — the Fed committee that sets US interest rates, 8 scheduled meetings a year.
> - **BoT** — the Bank of Thailand.
> - **Consensus / forecast** — the average economists' prediction for a release.
> - **Surprise** — actual minus consensus.
> - **High-impact event** — a release that regularly moves markets sharply.
> - **Gap / slippage** — price jumping past your stop / being filled worse than planned *(see 0.1)*.
> - **IV crush** — option prices falling after the uncertainty of an event passes *(see 8.6)*.
""")
L.before_heading("en", "2.", """
> [!analogy]
> Data releases are like a **weather forecast before a big outdoor event**. Everyone has already planned around the forecast ("light rain"). If it rains lightly, nothing changes. If a storm arrives instead, everyone scrambles. Markets move on the gap between forecast and reality, not on whether it rains.
>
> **Where it breaks:** the weather doesn't react to the forecast. In markets, a surprise changes expectations about central-bank decisions, which then feed back into prices for weeks.

> [!check]- Check your understanding: the calendar
> **Q1.** It's US winter. At what time in Bangkok is the US CPI released?
> > [!answer]-
> > 08:30 New York + 12 hours = 20:30 UTC+7 (19:30 in US summer).
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: reading two surprises
> 1. **Payrolls:** consensus **+180,000** jobs, actual **+250,000** → surprise **+70,000**. A strong economy → rate cuts less likely → yields and the dollar usually rise; gold and growth stocks often fall.
> 2. **CPI:** consensus **3.0%**, actual **3.3%** → surprise **+0.3** points: hotter inflation → same direction as above.
> 3. **Both at once:** if payrolls surprise **up** but CPI surprises **down**, the effects partly cancel; the market reacts to what matters more for the central bank right now.
> 4. **So what?** Before every release, write down the consensus and what a big upside or downside surprise would mean for your position.

> [!check]- Check your understanding: surprise
> **Q1.** CPI comes in at 2.8% vs a 2.6% consensus, but last month was 3.2%. Is this a hot or cool surprise?
> > [!answer]-
> > Hot: it's above the consensus (+0.2), even though it's lower than last month. Markets compare with the forecast.
""")
L.before_callout("en", "example", """
![[p10-gap-risk.en.svg]]

> [!walkthrough] Step by step: sizing a position you'll hold through news
> EUR/USD long, account **10,000 USD**, 1R = **100 USD**, stop **20 pips**, 10 USD per pip per lot.
> 1. **Normal size** = 100 ÷ (20 × 10) = **0.5 lot**.
> 2. **Gap test:** a release could fill you **50 pips** away → 0.5 × 10 × 50 = **250 USD = 2.5R**. Too much.
> 3. **Cap the gap at 2R** (200 USD): size = 200 ÷ (50 × 10) = **0.4 lot**.
> 4. With 0.4 lot, a normal stop costs 0.4 × 10 × 20 = **80 USD (0.8R)**, and the bad gap **200 USD (2R)**.
> 5. **So what?** Size for the worst realistic fill, not just the stop price, whenever you hold through a high-impact event.

> [!check]- Check your understanding: event rules
> **Q1.** A high-impact release is in 10 minutes and you see a perfect setup. What does the plan say?
> > [!answer]-
> > No new entry until 15–30 minutes after the release. The setup can be re-evaluated once the first spike settles.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** the biggest reactions come in the currency of the releasing country and USD pairs *(see 0.3)*.
> - **Gold:** very sensitive to US CPI, payrolls and FOMC; 20–40 USD spikes in minutes are common *(see 0.4)*.
> - **Stocks:** company earnings are the stock-specific events; index futures react to macro data *(see 0.5, 0.6)*.
> - **Crypto:** reacts to US CPI and FOMC as a risk asset; trades 24/7, so it often moves first, at 19:30–20:30 Bangkok time *(see 0.7)*.

> [!caution]
> In the first seconds after a big release, spreads can widen several times, liquidity disappears and stops fill far from their price. Highly leveraged positions can lose much more than 1R. If you hold through an event, reduce size beforehand; if you're flat, wait for the first spike to settle.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** What moves price at a data release: the number itself or the surprise? Explain in one line.
> > [!answer]-
> > The surprise: actual minus consensus, because the consensus is already priced in.
> **Q2.** Name three high-impact US releases and their Bangkok time in US summer.
> > [!answer]-
> > CPI 19:30, nonfarm payrolls 19:30 (first Friday), FOMC decision 01:00 the next morning (press conference 01:30).
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> การกระโดดของราคาครั้งใหญ่ที่สุดบางครั้งเกิดในเวลาที่คุณรู้ล่วงหน้าเป็นสัปดาห์: ตอนที่รัฐบาลประกาศตัวเลขเงินเฟ้อหรือการจ้างงาน หรือตอนธนาคารกลางประกาศดอกเบี้ย ก่อนประกาศแต่ละครั้ง นักเศรษฐศาสตร์เผยแพร่ตัวเลขคาดการณ์ ราคาสะท้อนตัวเลขคาดการณ์นั้นไปแล้ว สิ่งที่ขยับตลาดคือตัวเลขจริงต่างจากที่คาดแค่ไหน หน้าที่ของคุณไม่ใช่ทายตัวเลข แต่คือรู้ว่าเมื่อไหร่จะประกาศ และทำให้แน่ใจว่าความเซอร์ไพรส์ทำร้ายคุณหนักไม่ได้
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **ปฏิทินเศรษฐกิจ (Economic calendar)** — ตารางการประกาศข้อมูลและการประชุมธนาคารกลางที่จะมาถึง *(ดู 0.8)*
> - **CPI (Consumer Price Index)** — ตัวชี้วัดเงินเฟ้อรายเดือนหลัก **Core CPI** ไม่รวมอาหารและพลังงาน
> - **ดัชนีราคา PCE (Personal Consumption Expenditures)** — ตัวชี้วัดเงินเฟ้อที่ Fed ชอบใช้
> - **NFP (Nonfarm payrolls)** — จำนวนตำแหน่งงานที่เพิ่มขึ้นในสหรัฐเดือนก่อน ประกาศวันศุกร์แรกของเดือน
> - **GDP (Gross domestic product)** — ผลผลิตรวมของเศรษฐกิจ *(ดู 10.1)*
> - **ISM / PMI** — แบบสำรวจธุรกิจภาคการผลิตและบริการ *(ดู 10.1)*
> - **FOMC (Federal Open Market Committee)** — คณะกรรมการของ Fed ที่กำหนดดอกเบี้ยสหรัฐ ประชุมตามกำหนดปีละ 8 ครั้ง
> - **ธปท. (BoT)** — ธนาคารแห่งประเทศไทย
> - **ค่าคาดการณ์ (Consensus / Forecast)** — ค่าเฉลี่ยการทำนายของนักเศรษฐศาสตร์สำหรับการประกาศนั้น
> - **ความเซอร์ไพรส์ (Surprise)** — ตัวเลขจริงลบค่าคาดการณ์
> - **เหตุการณ์ผลกระทบสูง (High-impact event)** — การประกาศที่ขยับตลาดแรงเป็นประจำ
> - **Gap / Slippage** — ราคากระโดดข้าม Stop / ได้ราคาแย่กว่าที่วางแผน *(ดู 0.1)*
> - **IV crush** — ราคาออปชันลดลงหลังความไม่แน่นอนของเหตุการณ์ผ่านไป *(ดู 8.6)*
""")
L.before_heading("th", "2.", """
> [!analogy]
> การประกาศข้อมูลเหมือน **พยากรณ์อากาศก่อนงานกลางแจ้งใหญ่** ทุกคนวางแผนตามพยากรณ์ไปแล้ว ("ฝนตกเล็กน้อย") ถ้าฝนตกเล็กน้อยจริง ก็ไม่มีอะไรเปลี่ยน ถ้าพายุมาแทน ทุกคนวุ่นวาย ตลาดขยับตามช่องว่างระหว่างพยากรณ์กับความจริง ไม่ใช่ตามว่าฝนตกหรือไม่
>
> **จุดที่เปรียบเทียบไม่ได้:** อากาศไม่ตอบสนองต่อพยากรณ์ แต่ในตลาด ความเซอร์ไพรส์เปลี่ยนความคาดหวังเรื่องการตัดสินใจของธนาคารกลาง ซึ่งย้อนกลับมาที่ราคาอีกหลายสัปดาห์

> [!check]- เช็กความเข้าใจ: ปฏิทิน
> **Q1.** ตอนนี้เป็นฤดูหนาวของสหรัฐ CPI สหรัฐประกาศกี่โมงตามเวลากรุงเทพฯ?
> > [!answer]-
> > 08:30 นิวยอร์ก + 12 ชั่วโมง = 20:30 UTC+7 (ฤดูร้อนสหรัฐ 19:30)
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: อ่านความเซอร์ไพรส์สองแบบ
> 1. **Payrolls:** คาด **+180,000** ตำแหน่ง จริง **+250,000** → เซอร์ไพรส์ **+70,000** เศรษฐกิจแข็งแรง → โอกาสลดดอกเบี้ยน้อยลง → ผลตอบแทนพันธบัตรและดอลลาร์มักขึ้น ทองและหุ้นเติบโตมักลง
> 2. **CPI:** คาด **3.0%** จริง **3.3%** → เซอร์ไพรส์ **+0.3** จุด: เงินเฟ้อร้อนกว่าคาด → ทิศทางเดียวกับข้างบน
> 3. **ทั้งสองพร้อมกัน:** ถ้า Payrolls เซอร์ไพรส์ **ขึ้น** แต่ CPI เซอร์ไพรส์ **ลง** ผลจะหักล้างกันบางส่วน ตลาดตอบสนองต่อสิ่งที่สำคัญกว่าสำหรับธนาคารกลางในตอนนั้น
> 4. **แล้วไง?** ก่อนทุกการประกาศ จดค่าคาดการณ์ และเขียนว่าความเซอร์ไพรส์ใหญ่ขึ้นหรือลงหมายถึงอะไรต่อโพซิชันของคุณ

> [!check]- เช็กความเข้าใจ: ความเซอร์ไพรส์
> **Q1.** CPI ออกมา 2.8% เทียบค่าคาด 2.6% แต่เดือนก่อนอยู่ที่ 3.2% เป็นความเซอร์ไพรส์แบบร้อนหรือเย็น?
> > [!answer]-
> > ร้อน: สูงกว่าค่าคาด (+0.2) แม้จะต่ำกว่าเดือนก่อน ตลาดเทียบกับค่าคาดการณ์
""")
L.before_callout("th", "example", """
![[p10-gap-risk.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: คำนวณขนาดโพซิชันที่จะถือผ่านข่าว
> Long EUR/USD บัญชี **10,000 ดอลลาร์** 1R = **100 ดอลลาร์** Stop **20 pip** 10 ดอลลาร์ต่อ pip ต่อล็อต
> 1. **ขนาดปกติ** = 100 ÷ (20 × 10) = **0.5 ล็อต**
> 2. **ทดสอบ Gap:** ข่าวอาจทำให้ได้ราคาห่างไป **50 pip** → 0.5 × 10 × 50 = **250 ดอลลาร์ = 2.5R** มากเกินไป
> 3. **จำกัด Gap ที่ 2R** (200 ดอลลาร์): ขนาด = 200 ÷ (50 × 10) = **0.4 ล็อต**
> 4. ที่ 0.4 ล็อต Stop ปกติเสีย 0.4 × 10 × 20 = **80 ดอลลาร์ (0.8R)** และ Gap แย่ ๆ เสีย **200 ดอลลาร์ (2R)**
> 5. **แล้วไง?** เมื่อถือผ่านเหตุการณ์ผลกระทบสูง ให้คำนวณขนาดจากราคาแย่ที่สุดที่สมจริง ไม่ใช่แค่ราคา Stop

> [!check]- เช็กความเข้าใจ: กฎเหตุการณ์
> **Q1.** อีก 10 นาทีจะมีการประกาศผลกระทบสูง และคุณเห็น Setup ที่สมบูรณ์แบบ แผนบอกว่าอะไร?
> > [!answer]-
> > ไม่เข้าใหม่จนกว่าจะผ่านไป 15–30 นาทีหลังประกาศ ประเมิน Setup ใหม่เมื่อการพุ่งครั้งแรกสงบแล้ว
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** ปฏิกิริยาใหญ่ที่สุดอยู่ในสกุลเงินของประเทศที่ประกาศและคู่ USD *(ดู 0.3)*
> - **ทองคำ:** ไวมากต่อ CPI Payrolls และ FOMC ของสหรัฐ พุ่ง 20–40 ดอลลาร์ในไม่กี่นาทีเป็นเรื่องปกติ *(ดู 0.4)*
> - **หุ้น:** งบบริษัทคือเหตุการณ์เฉพาะตัวหุ้น ฟิวเจอร์สดัชนีตอบสนองต่อข้อมูลมหภาค *(ดู 0.5, 0.6)*
> - **คริปโต:** ตอบสนองต่อ CPI และ FOMC ของสหรัฐในฐานะสินทรัพย์เสี่ยง ซื้อขาย 24/7 จึงมักขยับก่อน ตอน 19:30–20:30 เวลากรุงเทพฯ *(ดู 0.7)*

> [!caution]
> ในไม่กี่วินาทีแรกหลังประกาศใหญ่ Spread อาจถ่างหลายเท่า สภาพคล่องหายไป และ Stop ได้ราคาห่างจากที่ตั้งไว้มาก โพซิชันที่ใช้เลเวอเรจสูงอาจเสียมากกว่า 1R มาก ถ้าจะถือผ่านเหตุการณ์ ให้ลดขนาดล่วงหน้า ถ้าไม่มีโพซิชัน ให้รอให้การพุ่งครั้งแรกสงบ
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** อะไรขยับราคาตอนประกาศข้อมูล: ตัวเลขเอง หรือความเซอร์ไพรส์? อธิบายในหนึ่งบรรทัด
> > [!answer]-
> > ความเซอร์ไพรส์: ตัวเลขจริงลบค่าคาดการณ์ เพราะค่าคาดการณ์ถูกตั้งราคาไว้แล้ว
> **Q2.** บอกการประกาศผลกระทบสูงของสหรัฐสามรายการ และเวลากรุงเทพฯ ช่วงฤดูร้อนสหรัฐ
> > [!answer]-
> > CPI 19:30, Nonfarm payrolls 19:30 (วันศุกร์แรก), การตัดสินของ FOMC 01:00 เช้าวันถัดไป (แถลงข่าว 01:30)
""")

L.set_meta("level", "v2")
L.save()
