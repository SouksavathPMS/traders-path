"""B8 · v2 upgrade of 10.1 The Business Cycle (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("10 Macro, Wall Street & Investing/10.1 The Business Cycle.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Economies breathe in and out. For a few years businesses sell more, hire more and borrow more; then things overheat, interest rates rise, spending slows, and the economy shrinks for a while before recovering. Different kinds of companies do best at different moments: banks and car makers when things speed up, food and healthcare companies when things slow down. Knowing roughly where we are in this cycle tells you which way the tide is flowing.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Business cycle** — the repeating pattern of expansion and contraction in an economy.
> - **GDP (gross domestic product)** — the total value of everything a country produces in a period.
> - **Recession** — a broad fall in economic activity lasting months (often described as two quarters of falling GDP, though official definitions vary).
> - **PMI (Purchasing Managers' Index)** — a monthly survey of company purchasing managers; above 50 = expansion, below 50 = contraction.
> - **ISM** — the Institute for Supply Management, which publishes the main US PMIs.
> - **Leading / coincident / lagging indicators** — data that tend to turn before / with / after the economy.
> - **Yield curve** — interest rates on government bonds from short to long maturities *(see 10.2)*.
> - **Credit spread** — the extra yield companies pay over government bonds; it widens when lenders get nervous.
> - **QE (quantitative easing)** — a central bank creating money to buy bonds *(see 10.2)*.
> - **Cyclical / defensive sectors** — industries that rise and fall with the economy / that stay steadier *(see 0.5)*.
> - **Small caps** — shares of smaller companies, usually more sensitive to the economy.
""")
L.before_heading("en", "2.", """
![[p10-pmi-gauge.en.svg]]

> [!walkthrough] Step by step: how a PMI number is built
> Purchasing managers answer one question: is business better, the same or worse than last month?
> 1. **Month A:** 30% better, 40% same, 30% worse → PMI = 30 + ½ × 40 = **50**: no change.
> 2. **Month B:** 25% better, 40% same, 35% worse → 25 + 20 = **45**: contraction.
> 3. **Month C:** 35% better, 45% same, 20% worse → 35 + 22.5 = **57.5**: strong expansion.
> 4. **So what?** PMI is a quick "mood count" of real businesses, published early in each month, which is why it's a **leading** indicator. Watch both the level (above/below 50) and the direction over several months.

> [!analogy]
> The business cycle is like **the seasons for a farmer**. In spring you plant (early cycle), in summer crops grow fast (mid), in autumn you harvest and things start to cool (late), and winter is quiet (recession). A good farmer doesn't predict the exact date of the first frost; they notice the days getting shorter and prepare.
>
> **Where it breaks:** seasons always come in the same order and length. Economic cycles vary a lot in length, and a shock (a pandemic, an energy crisis) can jump from summer straight to winter.

> [!check]- Check your understanding: phases
> **Q1.** PMI has risen from 46 to 52 over four months, the central bank has stopped cutting, and small caps are outperforming. Which phase?
> > [!answer]-
> > Most likely early cycle (recovery): growth rebounding, policy still supportive, cyclicals and small caps leading.
""")
L.before_callout("en", "example", """
> [!walkthrough] Step by step: scoring the phase with six signals
> Give each signal a vote: early, mid, late or recession.
> 1. **PMI 48 and falling for 4 months** → late / recession.
> 2. **Yield curve inverted a year ago** → late.
> 3. **Central bank still hiking** → late.
> 4. **Unemployment low, but jobless claims rising** → late.
> 5. **Energy beating technology** → late.
> 6. **Credit spreads starting to widen** → late / recession.
> 7. **Count:** 6 of 6 point to late cycle (2 also hint at recession).
> 8. **So what?** You don't need certainty: when most signals agree, adjust your tilt (more defensive, smaller sizes) rather than making an all-or-nothing bet.

> [!check]- Check your understanding: leading vs lagging
> **Q1.** Is the unemployment rate a leading or lagging indicator, and why does it matter?
> > [!answer]-
> > Lagging: companies lay people off after the slowdown has started. Waiting for unemployment to rise usually means the market has already moved.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** currencies of countries early in their cycle (with rising rates) tend to strengthen *(see 0.3)*.
> - **Gold:** often does well late in the cycle and in recessions, when real yields fall *(see 0.4)*.
> - **Stocks:** sector leadership rotates with the cycle; the market itself usually bottoms before the data improve *(see 0.5)*.
> - **Crypto:** behaves like a high-risk asset: strongest when liquidity is plentiful (early/mid), weakest when it's withdrawn *(see 0.7)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Name the four phases and one asset or sector that tends to lead in each.
> > [!answer]-
> > Early: small caps/financials. Mid: technology/broad equities. Late: energy/commodities/staples. Recession: bonds/utilities/healthcare.
> **Q2.** A PMI survey has 20% better, 50% same, 30% worse. What's the PMI?
> > [!answer]-
> > 20 + ½ × 50 = 45: contraction.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> เศรษฐกิจหายใจเข้าออก ไม่กี่ปีธุรกิจขายได้มากขึ้น จ้างงานมากขึ้น กู้มากขึ้น แล้วก็ร้อนแรงเกินไป ดอกเบี้ยขึ้น การใช้จ่ายชะลอ เศรษฐกิจหดตัวช่วงหนึ่งก่อนฟื้น บริษัทต่างประเภททำได้ดีในจังหวะต่างกัน: ธนาคารและผู้ผลิตรถยนต์เมื่อเศรษฐกิจเร่ง บริษัทอาหารและสุขภาพเมื่อเศรษฐกิจชะลอ การรู้คร่าว ๆ ว่าเราอยู่ตรงไหนของวัฏจักร บอกคุณว่ากระแสน้ำไหลไปทางไหน
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **วัฏจักรธุรกิจ (Business cycle)** — รูปแบบซ้ำ ๆ ของการขยายตัวและหดตัวของเศรษฐกิจ
> - **GDP (Gross domestic product)** — มูลค่ารวมของทุกอย่างที่ประเทศผลิตในช่วงเวลาหนึ่ง
> - **เศรษฐกิจถดถอย (Recession)** — กิจกรรมเศรษฐกิจลดลงอย่างกว้างขวางนานหลายเดือน (มักอธิบายว่า GDP ลดลงสองไตรมาส แม้นิยามทางการจะต่างกัน)
> - **PMI (Purchasing Managers' Index)** — แบบสำรวจรายเดือนของผู้จัดการฝ่ายจัดซื้อ เหนือ 50 = ขยายตัว ต่ำกว่า 50 = หดตัว
> - **ISM** — Institute for Supply Management ผู้เผยแพร่ PMI หลักของสหรัฐ
> - **ตัวชี้นำ / ตัวชี้พร้อม / ตัวชี้ตาม (Leading / Coincident / Lagging)** — ข้อมูลที่มักเปลี่ยนทิศก่อน / พร้อม / หลังเศรษฐกิจ
> - **เส้นอัตราผลตอบแทน (Yield curve)** — ดอกเบี้ยพันธบัตรรัฐบาลจากอายุสั้นถึงยาว *(ดู 10.2)*
> - **ส่วนต่างเครดิต (Credit spread)** — ผลตอบแทนส่วนเพิ่มที่บริษัทจ่ายเหนือพันธบัตรรัฐบาล ถ่างออกเมื่อผู้ให้กู้กังวล
> - **QE (Quantitative easing)** — ธนาคารกลางสร้างเงินเพื่อซื้อพันธบัตร *(ดู 10.2)*
> - **กลุ่มวัฏจักร / กลุ่มปลอดภัย** — อุตสาหกรรมที่ขึ้นลงตามเศรษฐกิจ / ที่นิ่งกว่า *(ดู 0.5)*
> - **หุ้นขนาดเล็ก (Small caps)** — หุ้นของบริษัทเล็ก มักไวต่อเศรษฐกิจมากกว่า
""")
L.before_heading("th", "2.", """
![[p10-pmi-gauge.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ตัวเลข PMI สร้างขึ้นอย่างไร
> ผู้จัดการฝ่ายจัดซื้อตอบคำถามเดียว: ธุรกิจดีขึ้น เท่าเดิม หรือแย่ลงกว่าเดือนก่อน?
> 1. **เดือน A:** ดีขึ้น 30% เท่าเดิม 40% แย่ลง 30% → PMI = 30 + ½ × 40 = **50**: ไม่เปลี่ยนแปลง
> 2. **เดือน B:** ดีขึ้น 25% เท่าเดิม 40% แย่ลง 35% → 25 + 20 = **45**: หดตัว
> 3. **เดือน C:** ดีขึ้น 35% เท่าเดิม 45% แย่ลง 20% → 35 + 22.5 = **57.5**: ขยายตัวแรง
> 4. **แล้วไง?** PMI คือการนับ "อารมณ์" ของธุรกิจจริงแบบรวดเร็ว เผยแพร่ต้นเดือน จึงเป็นตัว **ชี้นำ** ดูทั้งระดับ (เหนือ/ใต้ 50) และทิศทางหลายเดือน

> [!analogy]
> วัฏจักรธุรกิจเหมือน **ฤดูกาลของชาวนา** ฤดูใบไม้ผลิคุณปลูก (ต้นวัฏจักร) ฤดูร้อนพืชโตเร็ว (กลาง) ฤดูใบไม้ร่วงเก็บเกี่ยวและเริ่มเย็นลง (ปลาย) ฤดูหนาวเงียบ (ถดถอย) ชาวนาที่ดีไม่ได้ทำนายวันที่น้ำค้างแข็งครั้งแรกเป๊ะ ๆ แต่สังเกตว่ากลางวันสั้นลงแล้วเตรียมตัว
>
> **จุดที่เปรียบเทียบไม่ได้:** ฤดูกาลมาเรียงลำดับเดิมและยาวเท่าเดิมเสมอ แต่วัฏจักรเศรษฐกิจยาวไม่เท่ากันมาก และเหตุช็อก (โรคระบาด วิกฤตพลังงาน) อาจกระโดดจากฤดูร้อนไปฤดูหนาวเลย

> [!check]- เช็กความเข้าใจ: ช่วงของวัฏจักร
> **Q1.** PMI ขึ้นจาก 46 เป็น 52 ในสี่เดือน ธนาคารกลางหยุดลดดอกเบี้ย และหุ้นเล็กชนะตลาด อยู่ช่วงไหน?
> > [!answer]-
> > น่าจะเป็นต้นวัฏจักร (ฟื้นตัว): การเติบโตฟื้น นโยบายยังเอื้อ กลุ่มวัฏจักรและหุ้นเล็กนำ
""")
L.before_callout("th", "example", """
> [!walkthrough] ไล่ทีละขั้น: ให้คะแนนช่วงวัฏจักรด้วยสัญญาณหกข้อ
> ให้แต่ละสัญญาณโหวต: ต้น กลาง ปลาย หรือถดถอย
> 1. **PMI 48 และลดลง 4 เดือน** → ปลาย / ถดถอย
> 2. **Yield curve กลับหัวเมื่อปีก่อน** → ปลาย
> 3. **ธนาคารกลางยังขึ้นดอกเบี้ย** → ปลาย
> 4. **การว่างงานต่ำ แต่ผู้ขอรับสวัสดิการว่างงานเพิ่ม** → ปลาย
> 5. **กลุ่มพลังงานชนะกลุ่มเทคโนโลยี** → ปลาย
> 6. **Credit spread เริ่มถ่าง** → ปลาย / ถดถอย
> 7. **นับ:** 6 จาก 6 ชี้ไปที่ปลายวัฏจักร (2 ข้อบอกใบ้ถึงถดถอยด้วย)
> 8. **แล้วไง?** คุณไม่ต้องแน่ใจ: เมื่อสัญญาณส่วนใหญ่ตรงกัน ให้ปรับน้ำหนัก (เน้นปลอดภัยขึ้น ขนาดเล็กลง) แทนการเดิมพันแบบหมดหน้าตัก

> [!check]- เช็กความเข้าใจ: ตัวชี้นำ vs ตัวชี้ตาม
> **Q1.** อัตราการว่างงานเป็นตัวชี้นำหรือตัวชี้ตาม และทำไมจึงสำคัญ?
> > [!answer]-
> > ตัวชี้ตาม: บริษัทเลิกจ้างหลังจากเศรษฐกิจเริ่มชะลอแล้ว การรอให้การว่างงานเพิ่มมักแปลว่าตลาดขยับไปแล้ว
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** สกุลเงินของประเทศที่อยู่ต้นวัฏจักร (ดอกเบี้ยกำลังขึ้น) มักแข็งค่า *(ดู 0.3)*
> - **ทองคำ:** มักไปได้ดีช่วงปลายวัฏจักรและช่วงถดถอย เมื่อ Real yield ลง *(ดู 0.4)*
> - **หุ้น:** กลุ่มที่นำหมุนตามวัฏจักร ตลาดเองมักทำจุดต่ำก่อนข้อมูลจะดีขึ้น *(ดู 0.5)*
> - **คริปโต:** ทำตัวเหมือนสินทรัพย์เสี่ยงสูง: แรงที่สุดเมื่อสภาพคล่องล้น (ต้น/กลาง) อ่อนที่สุดเมื่อถูกดึงกลับ *(ดู 0.7)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกสี่ช่วง และสินทรัพย์หรือกลุ่มหนึ่งที่มักนำในแต่ละช่วง
> > [!answer]-
> > ต้น: หุ้นเล็ก/การเงิน กลาง: เทคโนโลยี/หุ้นโดยรวม ปลาย: พลังงาน/สินค้าโภคภัณฑ์/สินค้าจำเป็น ถดถอย: พันธบัตร/สาธารณูปโภค/สุขภาพ
> **Q2.** แบบสำรวจ PMI มีดีขึ้น 20% เท่าเดิม 50% แย่ลง 30% PMI เท่าไหร่?
> > [!answer]-
> > 20 + ½ × 50 = 45: หดตัว
""")

L.set_meta("level", "v2")
L.save()
