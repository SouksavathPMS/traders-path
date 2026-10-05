"""B8 · v2 upgrade of 10.7 Portfolio Construction & Asset Allocation (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("10 Macro, Wall Street & Investing/10.7 Portfolio Construction & Asset Allocation.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Don't put all your eggs in one basket. Split long-term savings between a few types of assets that don't all fall at the same time, keep costs low, add money every month, and leave it alone for years. How you split the money matters more than which single stock you pick, and the best mix is one you can keep holding when markets crash.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Asset allocation** — how you divide money between stocks, bonds, cash, gold and other assets.
> - **Diversification** — combining assets that don't move together, so the whole portfolio swings less.
> - **Correlation** — how closely two assets move together, from −1 to +1 *(see 10.4)*.
> - **Volatility** — how much returns swing up and down; a common measure of risk.
> - **Drawdown** — the fall from a peak to a low *(see 3.6)*.
> - **Rebalancing** — selling what has grown above its target weight and buying what has fallen below.
> - **DCA (dollar-cost averaging)** — investing a fixed amount on a fixed schedule.
> - **Core–satellite** — a large, diversified core plus a small active part.
> - **Emergency fund** — 3–6 months of expenses in cash, kept outside your investments.
> - **Expense ratio** — a fund's yearly fee as a % of your money.
> - **Compounding** — earning returns on earlier returns.
> - **IPS (Investment Policy Statement)** — your written investing rules *(see 11.2)*.
""")
L.before_heading("en", "2.", """
> [!walkthrough] Step by step: the crash test
> Imagine stocks fall **50%** and bonds rise **5%** (a severe, illustrative crash) on a **1,000,000 THB** portfolio.
> 1. **100/0:** −50% → **500,000 THB**. You need **+100%** to get back.
> 2. **80/20:** 0.8 × (−50%) + 0.2 × 5% = **−39%** → **610,000 THB**. Needs **+64%** to recover.
> 3. **60/40:** 0.6 × (−50%) + 0.4 × 5% = **−28%** → **720,000 THB**. Needs **+39%** to recover.
> 4. **So what?** Pick the mix whose crash number you could watch without selling. Bonds don't always rise in a crash (2022), so treat this as a stress test, not a promise.

> [!analogy]
> Asset allocation is like a **balanced diet**. No single food gives you everything, and eating only one thing, however good, eventually hurts. A mix of foods keeps you healthy across seasons, and the diet only works if you stick to it.
>
> **Where it breaks:** foods don't suddenly start behaving alike. In a market panic, assets that usually move separately can fall together, so diversification helps less exactly when you need it most.

> [!check]- Check your understanding: allocation
> **Q1.** Why can a "less optimal" 60/40 portfolio beat 100% stocks in real life?
> > [!answer]-
> > Because an investor who panics and sells in a crash locks in the loss. A mix you can hold through a fall keeps compounding; one you abandon doesn't.
""")
L.before_heading("en", "3.", """
> [!check]- Check your understanding: building blocks
> **Q1.** Why should the emergency fund come before the first investment?
> > [!answer]-
> > Without it, an unexpected expense or job loss during a crash forces you to sell investments at the worst time.
""")
L.before_callout("en", "example", """
![[p10-rebalance.en.svg]]

> [!walkthrough] Step by step: rebalancing after a rally
> 1. Start with **100**: stocks **60**, bonds **40** (target 60/40).
> 2. Stocks rise **25%**, bonds flat → stocks **75**, bonds **40**, total **115** → now **65% / 35%**.
> 3. Target stocks = 60% × 115 = **69** → **sell 6** of stocks, **buy 6** of bonds → **69 / 46**.
> 4. **So what?** Rebalancing makes you sell high and buy low by rule, without predicting anything, and keeps your risk at the level you chose.

> [!check]- Check your understanding: costs and rebalancing
> **Q1.** In the fee table, how much more does the 0.2% fund leave you after 30 years than the 2.0% fund?
> > [!answer]-
> > About 9.40M − 6.85M ≈ **2.55M THB**, from the same contributions.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** not a long-term asset class for most investors, but currency exposure comes with every foreign fund *(see 10.4)*.
> - **Gold:** a common 5–10% diversifier in the core *(see 0.4)*.
> - **Stocks:** broad, low-cost index funds form the core for most people *(see 0.5)*.
> - **Crypto:** if held at all, belongs in the satellite, sized so that losing all of it wouldn't change your life *(see 0.7)*.

> [!caution]
> Leverage in a long-term portfolio, no emergency fund, or a large crypto or single-stock satellite can turn a normal market crash into a permanent loss. Size the satellite so you could lose all of it, and never borrow to fund the core.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Stocks fall 40% and bonds rise 5%. What happens to an 80/20 portfolio?
> > [!answer]-
> > 0.8 × (−40%) + 0.2 × 5% = **−31%**.
> **Q2.** Give three rules that keep a long-term investor on track.
> > [!answer]-
> > For example: rebalance on a schedule, invest a fixed amount monthly (DCA), keep costs low, keep an emergency fund, and write down what you'll do in a crash.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> อย่าใส่ไข่ทั้งหมดไว้ในตะกร้าใบเดียว แบ่งเงินออมระยะยาวไว้ในสินทรัพย์ไม่กี่ประเภทที่ไม่ได้ลงพร้อมกันทั้งหมด รักษาต้นทุนให้ต่ำ เติมเงินทุกเดือน และปล่อยไว้หลายปี วิธีแบ่งเงินสำคัญกว่าการเลือกหุ้นตัวใดตัวหนึ่ง และสัดส่วนที่ดีที่สุดคือสัดส่วนที่คุณถือต่อได้เมื่อตลาดถล่ม
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **การจัดสรรสินทรัพย์ (Asset allocation)** — การแบ่งเงินระหว่างหุ้น พันธบัตร เงินสด ทอง และสินทรัพย์อื่น
> - **การกระจายความเสี่ยง (Diversification)** — รวมสินทรัพย์ที่ไม่เคลื่อนไหวไปด้วยกัน ทั้งพอร์ตจึงแกว่งน้อยลง
> - **สหสัมพันธ์ (Correlation)** — สินทรัพย์สองอย่างเคลื่อนไหวไปด้วยกันแค่ไหน จาก −1 ถึง +1 *(ดู 10.4)*
> - **ความผันผวน (Volatility)** — ผลตอบแทนแกว่งขึ้นลงมากแค่ไหน เป็นมาตรวัดความเสี่ยงที่ใช้กันทั่วไป
> - **Drawdown** — การลดลงจากจุดสูงสุดถึงจุดต่ำ *(ดู 3.6)*
> - **การปรับสมดุล (Rebalancing)** — ขายสิ่งที่โตเกินน้ำหนักเป้าหมาย และซื้อสิ่งที่ต่ำกว่าเป้า
> - **DCA (Dollar-cost averaging)** — ลงทุนจำนวนเงินคงที่ตามกำหนดเวลาคงที่
> - **Core–satellite** — แกนหลักขนาดใหญ่ที่กระจายความเสี่ยง บวกส่วนเชิงรุกขนาดเล็ก
> - **เงินสำรองฉุกเฉิน (Emergency fund)** — ค่าใช้จ่าย 3–6 เดือนในรูปเงินสด เก็บแยกจากเงินลงทุน
> - **อัตราค่าใช้จ่ายกองทุน (Expense ratio)** — ค่าธรรมเนียมรายปีของกองทุนเป็น % ของเงินคุณ
> - **ดอกเบี้ยทบต้น (Compounding)** — ได้ผลตอบแทนจากผลตอบแทนก่อนหน้า
> - **IPS (Investment Policy Statement)** — กฎการลงทุนที่คุณเขียนไว้ *(ดู 11.2)*
""")
L.before_heading("th", "2.", """
> [!walkthrough] ไล่ทีละขั้น: ทดสอบตลาดถล่ม
> สมมติหุ้นลง **50%** และพันธบัตรขึ้น **5%** (การถล่มรุนแรง ตัวอย่าง) กับพอร์ต **1,000,000 บาท**
> 1. **100/0:** −50% → **500,000 บาท** ต้องขึ้น **+100%** จึงกลับมาเท่าเดิม
> 2. **80/20:** 0.8 × (−50%) + 0.2 × 5% = **−39%** → **610,000 บาท** ต้องขึ้น **+64%** จึงฟื้น
> 3. **60/40:** 0.6 × (−50%) + 0.4 × 5% = **−28%** → **720,000 บาท** ต้องขึ้น **+39%** จึงฟื้น
> 4. **แล้วไง?** เลือกสัดส่วนที่คุณดูตัวเลขตอนถล่มได้โดยไม่ขาย พันธบัตรไม่ได้ขึ้นทุกครั้งที่ตลาดถล่ม (ปี 2022) ให้ถือเป็นการทดสอบภาวะวิกฤต ไม่ใช่คำสัญญา

> [!analogy]
> การจัดสรรสินทรัพย์เหมือน **อาหารที่สมดุล** ไม่มีอาหารอย่างเดียวที่ให้ทุกอย่าง และการกินอย่างเดียว ไม่ว่าจะดีแค่ไหน สุดท้ายก็ส่งผลเสีย อาหารที่หลากหลายทำให้คุณแข็งแรงตลอดทุกฤดู และจะได้ผลก็ต่อเมื่อคุณทำต่อเนื่อง
>
> **จุดที่เปรียบเทียบไม่ได้:** อาหารไม่ได้จู่ ๆ เริ่มทำตัวเหมือนกัน แต่ในช่วงตลาดตื่นตระหนก สินทรัพย์ที่ปกติเคลื่อนแยกกันอาจลงพร้อมกัน การกระจายความเสี่ยงจึงช่วยได้น้อยลงในตอนที่คุณต้องการมันมากที่สุด

> [!check]- เช็กความเข้าใจ: การจัดสรรสินทรัพย์
> **Q1.** ทำไมพอร์ต 60/40 ที่ "ไม่เหมาะสมที่สุด" จึงอาจชนะหุ้น 100% ในชีวิตจริง?
> > [!answer]-
> > เพราะนักลงทุนที่ตื่นตระหนกและขายตอนตลาดถล่มคือการล็อกขาดทุน สัดส่วนที่คุณถือผ่านการลงได้ยังทบต้นต่อ ส่วนที่คุณทิ้งไปไม่ได้ทบต้น
""")
L.before_heading("th", "3.", """
> [!check]- เช็กความเข้าใจ: ส่วนประกอบพื้นฐาน
> **Q1.** ทำไมเงินสำรองฉุกเฉินต้องมาก่อนการลงทุนครั้งแรก?
> > [!answer]-
> > ถ้าไม่มี ค่าใช้จ่ายที่ไม่คาดคิดหรือการตกงานในช่วงตลาดถล่ม จะบังคับให้คุณขายเงินลงทุนในเวลาที่แย่ที่สุด
""")
L.before_callout("th", "example", """
![[p10-rebalance.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ปรับสมดุลหลังหุ้นขึ้นแรง
> 1. เริ่มที่ **100**: หุ้น **60** พันธบัตร **40** (เป้า 60/40)
> 2. หุ้นขึ้น **25%** พันธบัตรทรงตัว → หุ้น **75** พันธบัตร **40** รวม **115** → ตอนนี้ **65% / 35%**
> 3. เป้าหุ้น = 60% × 115 = **69** → **ขายหุ้น 6** **ซื้อพันธบัตร 6** → **69 / 46**
> 4. **แล้วไง?** การปรับสมดุลทำให้คุณขายแพงซื้อถูกตามกฎ โดยไม่ต้องทำนายอะไร และรักษาความเสี่ยงไว้ที่ระดับที่คุณเลือก

> [!check]- เช็กความเข้าใจ: ต้นทุนและการปรับสมดุล
> **Q1.** ในตารางค่าธรรมเนียม กองทุน 0.2% เหลือเงินให้คุณมากกว่ากองทุน 2.0% เท่าไรหลัง 30 ปี?
> > [!answer]-
> > ราว 9.40 ล้าน − 6.85 ล้าน ≈ **2.55 ล้านบาท** จากเงินลงทุนเท่ากัน
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** ไม่ใช่สินทรัพย์ระยะยาวสำหรับนักลงทุนส่วนใหญ่ แต่ความเสี่ยงค่าเงินมาพร้อมกองทุนต่างประเทศทุกกอง *(ดู 10.4)*
> - **ทองคำ:** ตัวกระจายความเสี่ยงที่นิยม 5–10% ในแกนหลัก *(ดู 0.4)*
> - **หุ้น:** กองทุนดัชนีกว้าง ต้นทุนต่ำ เป็นแกนหลักสำหรับคนส่วนใหญ่ *(ดู 0.5)*
> - **คริปโต:** ถ้าจะถือ ให้อยู่ในส่วน Satellite ในขนาดที่หายหมดแล้วชีวิตไม่เปลี่ยน *(ดู 0.7)*

> [!caution]
> เลเวอเรจในพอร์ตระยะยาว ไม่มีเงินสำรองฉุกเฉิน หรือ Satellite ที่เป็นคริปโตหรือหุ้นตัวเดียวขนาดใหญ่ สามารถเปลี่ยนการถล่มของตลาดตามปกติให้กลายเป็นการขาดทุนถาวร กำหนดขนาด Satellite ให้เสียได้ทั้งหมด และอย่ากู้เงินมาลงทุนในแกนหลัก
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** หุ้นลง 40% และพันธบัตรขึ้น 5% พอร์ต 80/20 เป็นอย่างไร?
> > [!answer]-
> > 0.8 × (−40%) + 0.2 × 5% = **−31%**
> **Q2.** บอกกฎสามข้อที่ช่วยให้นักลงทุนระยะยาวอยู่ในเส้นทาง
> > [!answer]-
> > ตัวอย่าง: ปรับสมดุลตามกำหนด ลงทุนจำนวนคงที่ทุกเดือน (DCA) รักษาต้นทุนให้ต่ำ มีเงินสำรองฉุกเฉิน และเขียนไว้ว่าจะทำอะไรเมื่อตลาดถล่ม
""")

L.set_meta("level", "v2")
L.save()
