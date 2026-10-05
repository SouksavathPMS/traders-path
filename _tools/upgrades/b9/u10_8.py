"""B9f · v2 upgrade of 10.8 Checkpoint: Phase 10 Review (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("10 Macro, Wall Street & Investing/10.8 Checkpoint- Phase 10 Review.md")

# ---------------------------------------------------------------- EN
L.before_callout("en", "practice", """
> [!check]- Worked problems: Phase 10
> **Q1.** A bond fund has a duration of about 6. Yields fall by 0.75 percentage points. Approximate price change?
> > [!answer]-
> > −6 × (−0.75%) ≈ **+4.5%** (see 10.2).
> **Q2.** A US index ETF rises 12% in dollars. USD/THB moves from 35.0 to 33.6. What's the return in baht?
> > [!answer]-
> > 1.12 × (33.6 ÷ 35.0) − 1 ≈ **+7.5%**: the stronger baht took away about 4.5 points (see 10.4).
> **Q3.** Market cap 50 bn, debt 12 bn, cash 4 bn, EBITDA 7.5 bn. EV and EV/EBITDA?
> > [!answer]-
> > EV = 50 + 12 − 4 = **58 bn**; EV/EBITDA = 58 ÷ 7.5 ≈ **7.7×** (see 10.6).
> **Q4.** Northern winter. US CPI comes out at 08:30 New York time. When is that in Bangkok, and what's a 30-minute no-trade window around it?
> > [!answer]-
> > **20:30** UTC+7; no new entries **20:00–21:00** (see 10.3).
""")
L.before_callout("en", "key", """
> [!check]- Final check: Phase 10
> **Q1.** Your estimate of a stock's value is 50 and you want a 25% margin of safety. Below what price would you consider buying?
> > [!answer]-
> > 50 × (1 − 0.25) = **37.5** (see 10.6).
> **Q2.** Why keep the trading account and the long-term portfolio separate?
> > [!answer]-
> > They have different goals, rules and time horizons. Mixing them lets trading losses (or excitement) damage the money meant for decades: never refill one from the other (see 10.7, 11.2).
""")

# ---------------------------------------------------------------- TH
L.before_callout("th", "practice", """
> [!check]- โจทย์ฝึกคำนวณ: เฟส 10
> **Q1.** กองทุนพันธบัตรมี Duration ราว 6 ผลตอบแทนลดลง 0.75 จุดเปอร์เซ็นต์ ราคาเปลี่ยนประมาณเท่าไร?
> > [!answer]-
> > −6 × (−0.75%) ≈ **+4.5%** (ดู 10.2)
> **Q2.** ETF ดัชนีสหรัฐขึ้น 12% เป็นดอลลาร์ USD/THB ขยับจาก 35.0 เป็น 33.6 ผลตอบแทนเป็นบาทเท่าไร?
> > [!answer]-
> > 1.12 × (33.6 ÷ 35.0) − 1 ≈ **+7.5%**: บาทที่แข็งขึ้นกินไปราว 4.5 จุด (ดู 10.4)
> **Q3.** มูลค่าตลาด 50 พันล้าน หนี้ 12 พันล้าน เงินสด 4 พันล้าน EBITDA 7.5 พันล้าน EV และ EV/EBITDA เท่าไร?
> > [!answer]-
> > EV = 50 + 12 − 4 = **58 พันล้าน** EV/EBITDA = 58 ÷ 7.5 ≈ **7.7 เท่า** (ดู 10.6)
> **Q4.** ช่วงฤดูหนาวซีกโลกเหนือ CPI สหรัฐออกตอน 08:30 นิวยอร์ก ตรงกับกี่โมงในกรุงเทพฯ และช่วงห้ามเทรด 30 นาทีรอบนั้นคือช่วงไหน?
> > [!answer]-
> > **20:30** UTC+7 ไม่เข้าไม้ใหม่ช่วง **20:00–21:00** (ดู 10.3)
""")
L.before_callout("th", "key", """
> [!check]- ทดสอบสุดท้าย: เฟส 10
> **Q1.** คุณประเมินมูลค่าหุ้นได้ 50 และต้องการส่วนเผื่อความปลอดภัย 25% จะพิจารณาซื้อที่ราคาต่ำกว่าเท่าไร?
> > [!answer]-
> > 50 × (1 − 0.25) = **37.5** (ดู 10.6)
> **Q2.** ทำไมต้องแยกบัญชีเทรดกับพอร์ตระยะยาว?
> > [!answer]-
> > มีเป้าหมาย กฎ และระยะเวลาต่างกัน การปนกันทำให้การขาดทุน (หรือความตื่นเต้น) จากการเทรดทำร้ายเงินที่ตั้งใจไว้หลายสิบปี ห้ามเติมฝั่งหนึ่งจากอีกฝั่ง (ดู 10.7, 11.2)
""")

L.set_meta("level", "v2")
L.save()
