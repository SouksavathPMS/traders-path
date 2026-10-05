"""B8 · v2 upgrade of 10.2 Central Banks, Rates & Liquidity (QE/QT) (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("10 Macro, Wall Street & Investing/10.2 Central Banks, Rates & Liquidity (QE-QT).md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> A central bank decides how expensive it is to borrow money. When borrowing is cheap, people and companies borrow and spend more, and investors pay higher prices for shares and property. When borrowing is expensive, everyone slows down and prices of risky assets tend to fall. Central banks can also create money to buy bonds (QE) or remove it (QT). Because almost every asset is priced against interest rates, a change in rates moves almost everything at once.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Central bank** — the institution that sets a country's interest rate and manages its money (Fed, ECB, BoJ, BoT).
> - **Fed (Federal Reserve)** — the US central bank. **BoT** — the Bank of Thailand.
> - **Policy rate / Fed funds rate** — the short-term interest rate the central bank targets.
> - **Basis point (bp)** — 0.01 percentage point; 25 bp = 0.25%.
> - **Hawkish / dovish** — leaning towards higher rates / lower rates.
> - **Forward guidance** — the central bank's hints about future decisions.
> - **QE (quantitative easing)** — the central bank buys bonds with newly created reserves.
> - **QT (quantitative tightening)** — the central bank lets bonds mature or sells them, shrinking its balance sheet.
> - **Balance sheet / reserves** — what the central bank owns / the money banks hold at the central bank.
> - **Yield** — the annual return a bond pays relative to its price.
> - **Duration** — how sensitive a bond's price is to a change in yields (roughly % price change per 1 percentage point).
> - **Yield curve / inversion** — yields from short to long maturities / short yields above long yields.
> - **CME FedWatch** — a tool that shows market-implied probabilities of Fed decisions.
""")
L.before_heading("en", "2.", """
> [!analogy]
> A central bank is like a **thermostat in a big house with very slow pipes**. Turning the heating up (cutting rates, QE) warms the economy, but only after many months. Turning it down (hikes, QT) cools it, again with a long delay. Markets, though, react the moment someone touches the dial, because they price what the temperature will be later.
>
> **Where it breaks:** a thermostat responds to one temperature. A central bank must balance inflation and jobs at the same time, and its "dial" also moves currencies and asset prices worldwide.

> [!walkthrough] Step by step: what QE does, in round numbers
> 1. The central bank creates **100 bn** of new reserves and uses them to buy **100 bn** of government bonds from banks and investors.
> 2. Extra demand for bonds pushes bond **prices up** and **yields down**.
> 3. The sellers now hold cash instead of bonds and look for other assets (corporate bonds, shares) → those prices rise too.
> 4. Lower long-term yields make mortgages and company borrowing cheaper.
> 5. **So what?** QE lifts asset prices through liquidity even before the economy improves; QT does the reverse, slowly.

> [!check]- Check your understanding: the tools
> **Q1.** The Fed raises rates by 50 bp. How many percentage points is that?
> > [!answer]-
> > 0.50 percentage points (1 bp = 0.01%).
""")
L.before_heading("en", "3.", """
![[p10-duration.en.svg]]

> [!walkthrough] Step by step: why bond prices fall when yields rise
> A simple 1-year bond: you pay **1,000**, and in a year you get **1,040** back (a 4% coupon plus your money).
> 1. If new bonds suddenly pay **5%**, nobody will pay 1,000 for yours. Its fair price = 1,040 ÷ 1.05 ≈ **990.48**.
> 2. Price change ≈ **−0.95%** for a 1-point rise in yields: a 1-year bond has a duration of about 1.
> 3. A 10-year bond with duration about **8** loses about **8%** for a 1-point rise, or about **4%** for a 0.5-point rise (figure).
> 4. **So what?** "Safe" long bonds can lose a lot when rates rise, and the same logic hits long-duration stocks (growth and tech).

> [!check]- Check your understanding: duration
> **Q1.** A bond fund has a duration of 6. Yields fall by 0.75 percentage points. Roughly what happens to its price?
> > [!answer]-
> > About +4.5% (−6 × −0.75).
""")
L.before_callout("en", "example", """
> [!check]- Check your understanding: the yield curve
> **Q1.** The 2-year yield is 4.8% and the 10-year yield is 4.2%. What shape is the curve and what does it often signal?
> > [!answer]-
> > Inverted (short above long): policy is tight now and markets expect cuts later, often because they expect a slowdown.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** rate differences between countries are the main long-term driver of currencies *(see 0.3)*.
> - **Gold:** falls when real yields rise and rises when they fall *(see 0.4)*.
> - **Stocks:** higher rates lower valuations, especially for growth stocks; rate cuts during a recession often come with falling stocks *(see 0.5)*.
> - **Crypto:** very sensitive to liquidity: QE and rate cuts have tended to help, tightening to hurt *(see 0.7)*.

> [!caution]
> Bond funds are not risk-free. When yields rose sharply in 2022, long-duration government bond funds lost more than many stock investors expected. Know the duration of any bond fund you hold, and don't trade on the headline rate decision: markets move on the surprise versus expectations *(see 10.3)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** What's the difference between QE and QT?
> > [!answer]-
> > QE: the central bank buys bonds with new reserves (adds liquidity, lowers yields). QT: it lets bonds roll off or sells them (removes liquidity, a slow headwind).
> **Q2.** Why can a rate cut make stocks fall on the day?
> > [!answer]-
> > If the cut is smaller than expected or comes with signals of fewer future cuts, it's hawkish relative to what was priced in; yields and the dollar can rise.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ธนาคารกลางตัดสินว่าการกู้เงินแพงแค่ไหน เมื่อกู้ถูก ผู้คนและบริษัทกู้และใช้จ่ายมากขึ้น นักลงทุนยอมจ่ายแพงขึ้นสำหรับหุ้นและอสังหาฯ เมื่อกู้แพง ทุกคนชะลอ และราคาสินทรัพย์เสี่ยงมักลง ธนาคารกลางยังสร้างเงินเพื่อซื้อพันธบัตรได้ (QE) หรือดึงเงินออก (QT) เพราะสินทรัพย์เกือบทุกอย่างตั้งราคาเทียบกับดอกเบี้ย การเปลี่ยนดอกเบี้ยจึงขยับเกือบทุกอย่างพร้อมกัน
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **ธนาคารกลาง (Central bank)** — สถาบันที่กำหนดดอกเบี้ยและดูแลเงินของประเทศ (Fed, ECB, BoJ, ธปท.)
> - **Fed (Federal Reserve)** — ธนาคารกลางสหรัฐ **ธปท. (BoT)** — ธนาคารแห่งประเทศไทย
> - **อัตราดอกเบี้ยนโยบาย / Fed funds rate** — ดอกเบี้ยระยะสั้นที่ธนาคารกลางตั้งเป้า
> - **Basis point (bp)** — 0.01 จุดเปอร์เซ็นต์ 25 bp = 0.25%
> - **Hawkish / Dovish** — เอนไปทางดอกเบี้ยสูง / ดอกเบี้ยต่ำ
> - **Forward guidance** — การส่งสัญญาณของธนาคารกลางเกี่ยวกับการตัดสินใจในอนาคต
> - **QE (Quantitative easing)** — ธนาคารกลางซื้อพันธบัตรด้วยเงินสำรองที่สร้างขึ้นใหม่
> - **QT (Quantitative tightening)** — ธนาคารกลางปล่อยให้พันธบัตรครบอายุหรือขายออก งบดุลหดลง
> - **งบดุล / เงินสำรอง (Balance sheet / Reserves)** — สิ่งที่ธนาคารกลางถือ / เงินที่ธนาคารพาณิชย์ฝากไว้ที่ธนาคารกลาง
> - **อัตราผลตอบแทน (Yield)** — ผลตอบแทนรายปีที่พันธบัตรจ่ายเทียบกับราคา
> - **Duration** — ราคาพันธบัตรไวต่อการเปลี่ยนของผลตอบแทนแค่ไหน (ประมาณ % ราคาที่เปลี่ยนต่อ 1 จุดเปอร์เซ็นต์)
> - **เส้นอัตราผลตอบแทน / การกลับหัว (Yield curve / Inversion)** — ผลตอบแทนจากอายุสั้นถึงยาว / ผลตอบแทนระยะสั้นสูงกว่าระยะยาว
> - **CME FedWatch** — เครื่องมือแสดงความน่าจะเป็นของการตัดสินใจของ Fed ตามที่ตลาดคาด
""")
L.before_heading("th", "2.", """
> [!analogy]
> ธนาคารกลางเหมือน **เทอร์โมสตัทในบ้านหลังใหญ่ที่ท่อส่งความร้อนช้ามาก** การเพิ่มความร้อน (ลดดอกเบี้ย QE) ทำให้เศรษฐกิจอุ่นขึ้น แต่หลังจากหลายเดือน การลดความร้อน (ขึ้นดอกเบี้ย QT) ทำให้เย็นลง ก็ช้าเช่นกัน แต่ตลาดตอบสนองทันทีที่มีคนแตะปุ่ม เพราะตลาดตั้งราคาตามอุณหภูมิในอนาคต
>
> **จุดที่เปรียบเทียบไม่ได้:** เทอร์โมสตัทดูอุณหภูมิอย่างเดียว แต่ธนาคารกลางต้องสมดุลทั้งเงินเฟ้อและการจ้างงานพร้อมกัน และ "ปุ่ม" ของมันยังขยับค่าเงินและราคาสินทรัพย์ทั่วโลกด้วย

> [!walkthrough] ไล่ทีละขั้น: QE ทำอะไร ด้วยตัวเลขกลม ๆ
> 1. ธนาคารกลางสร้างเงินสำรองใหม่ **100 พันล้าน** แล้วใช้ซื้อพันธบัตรรัฐบาล **100 พันล้าน** จากธนาคารและนักลงทุน
> 2. ความต้องการพันธบัตรที่เพิ่มขึ้นดัน **ราคาขึ้น** และ **ผลตอบแทนลง**
> 3. ผู้ขายตอนนี้ถือเงินสดแทนพันธบัตร และมองหาสินทรัพย์อื่น (หุ้นกู้ หุ้น) → ราคาเหล่านั้นขึ้นด้วย
> 4. ผลตอบแทนระยะยาวที่ต่ำลงทำให้สินเชื่อบ้านและการกู้ของบริษัทถูกลง
> 5. **แล้วไง?** QE ยกราคาสินทรัพย์ผ่านสภาพคล่องได้ก่อนที่เศรษฐกิจจะดีขึ้นด้วยซ้ำ QT ทำกลับกันอย่างช้า ๆ

> [!check]- เช็กความเข้าใจ: เครื่องมือ
> **Q1.** Fed ขึ้นดอกเบี้ย 50 bp เท่ากับกี่จุดเปอร์เซ็นต์?
> > [!answer]-
> > 0.50 จุดเปอร์เซ็นต์ (1 bp = 0.01%)
""")
L.before_heading("th", "3.", """
![[p10-duration.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ทำไมราคาพันธบัตรลงเมื่อผลตอบแทนขึ้น
> พันธบัตรอายุ 1 ปีแบบง่าย: คุณจ่าย **1,000** และอีกหนึ่งปีได้คืน **1,040** (ดอกเบี้ย 4% บวกเงินต้น)
> 1. ถ้าพันธบัตรใหม่จ่าย **5%** ขึ้นมาทันที ไม่มีใครยอมจ่าย 1,000 ซื้อของคุณ ราคายุติธรรม = 1,040 ÷ 1.05 ≈ **990.48**
> 2. ราคาเปลี่ยน ≈ **−0.95%** เมื่อผลตอบแทนขึ้น 1 จุด: พันธบัตร 1 ปีมี Duration ราว 1
> 3. พันธบัตร 10 ปีที่ Duration ราว **8** เสียราว **8%** เมื่อขึ้น 1 จุด หรือราว **4%** เมื่อขึ้น 0.5 จุด (ภาพ)
> 4. **แล้วไง?** พันธบัตรระยะยาวที่ "ปลอดภัย" เสียได้มากเมื่อดอกเบี้ยขึ้น และตรรกะเดียวกันกระทบหุ้นที่มี Duration ยาว (หุ้นเติบโตและเทค)

> [!check]- เช็กความเข้าใจ: Duration
> **Q1.** กองทุนพันธบัตรมี Duration 6 ผลตอบแทนลด 0.75 จุดเปอร์เซ็นต์ ราคาจะเป็นอย่างไรโดยประมาณ?
> > [!answer]-
> > ราว +4.5% (−6 × −0.75)
""")
L.before_callout("th", "example", """
> [!check]- เช็กความเข้าใจ: Yield curve
> **Q1.** ผลตอบแทน 2 ปีอยู่ที่ 4.8% และ 10 ปีที่ 4.2% เส้นเป็นรูปทรงอะไร และมักส่งสัญญาณอะไร?
> > [!answer]-
> > กลับหัว (ระยะสั้นสูงกว่าระยะยาว): นโยบายตึงตัวตอนนี้ และตลาดคาดว่าจะลดดอกเบี้ยภายหลัง มักเพราะคาดว่าเศรษฐกิจจะชะลอ
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** ส่วนต่างดอกเบี้ยระหว่างประเทศคือตัวขับเคลื่อนระยะยาวหลักของค่าเงิน *(ดู 0.3)*
> - **ทองคำ:** ลงเมื่อ Real yield ขึ้น และขึ้นเมื่อ Real yield ลง *(ดู 0.4)*
> - **หุ้น:** ดอกเบี้ยสูงลดมูลค่า โดยเฉพาะหุ้นเติบโต การลดดอกเบี้ยช่วงเศรษฐกิจถดถอยมักมาพร้อมหุ้นที่ลง *(ดู 0.5)*
> - **คริปโต:** ไวต่อสภาพคล่องมาก: QE และการลดดอกเบี้ยมักช่วย การตึงตัวมักกดดัน *(ดู 0.7)*

> [!caution]
> กองทุนพันธบัตรไม่ใช่สิ่งที่ไร้ความเสี่ยง เมื่อผลตอบแทนพุ่งแรงในปี 2022 กองทุนพันธบัตรรัฐบาลที่มี Duration ยาวเสียมากกว่าที่นักลงทุนหุ้นหลายคนคาด รู้ Duration ของกองทุนพันธบัตรที่ถือ และอย่าเทรดตามพาดหัวการตัดสินดอกเบี้ย: ตลาดขยับตามความเซอร์ไพรส์เทียบกับความคาดหวัง *(ดู 10.3)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** QE กับ QT ต่างกันอย่างไร?
> > [!answer]-
> > QE: ธนาคารกลางซื้อพันธบัตรด้วยเงินสำรองใหม่ (เพิ่มสภาพคล่อง ลดผลตอบแทน) QT: ปล่อยให้พันธบัตรครบอายุหรือขายออก (ดึงสภาพคล่อง เป็นลมต้านช้า ๆ)
> **Q2.** ทำไมการลดดอกเบี้ยอาจทำให้หุ้นลงในวันนั้น?
> > [!answer]-
> > ถ้าลดน้อยกว่าที่คาด หรือมาพร้อมสัญญาณว่าจะลดน้อยลงในอนาคต ก็ถือว่า Hawkish เมื่อเทียบกับสิ่งที่ตลาดตั้งราคาไว้ ผลตอบแทนและดอลลาร์อาจขึ้น
""")

L.set_meta("level", "v2")
L.save()
