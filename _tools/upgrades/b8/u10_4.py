"""B8 · v2 upgrade of 10.4 Intermarket Analysis (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("10 Macro, Wall Street & Investing/10.4 Intermarket Analysis.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Markets are like rooms in one house that share the same water pipes. When the "price of money" (interest rates) or the value of the US dollar changes, water flows from some rooms into others. Watching a few neighbouring rooms tells you whether the move in your room is part of a house-wide flow or just a local splash.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Intermarket analysis** — reading one market in the context of related markets.
> - **DXY (US dollar index)** — the dollar's value against a basket of six major currencies.
> - **Real yield** — a bond yield minus expected inflation.
> - **Credit spread** — the extra yield companies pay over government bonds; it widens when lenders get nervous.
> - **High-yield (junk) bonds** — bonds of riskier companies; their spreads are an early stress gauge.
> - **Risk-on / risk-off** — periods when investors buy risky assets / flee to safety.
> - **Correlation** — how closely two markets move together, from −1 (opposite) to +1 (together) *(see 9.1)*.
> - **EM (emerging markets)** — developing economies such as Thailand, Indonesia or Brazil.
> - **SET / SET50** — the Stock Exchange of Thailand / its index of the 50 largest stocks *(see 0.5)*.
> - **THB** — the Thai baht.
> - **Brent** — the main international oil price benchmark.
""")
L.before_heading("en", "2.", """
> [!analogy]
> Think of the **connected pipes** in a building: open a big tap on one floor (the Fed raises rates) and the pressure drops on other floors (stocks, gold, emerging markets). A plumber who checks only one tap misses the cause.
>
> **Where it breaks:** pipes follow fixed physics. Market links are habits of investors, and they change with the regime: stocks and bonds fell together in 2022, the opposite of their usual pattern.

> [!walkthrough] Step by step: real yield
> 1. The US 10-year yield is **4.5%**, and expected inflation is **2.3%** (illustrative numbers).
> 2. Real yield = 4.5 − 2.3 = **2.2%**: what a bond holder earns after inflation.
> 3. If the yield stays at 4.5% but expected inflation rises to 2.8%, the real yield falls to **1.7%**: usually supportive for gold, which pays nothing.
> 4. **So what?** Watch real yields, not only the headline yield, when you analyse gold and growth stocks.

> [!check]- Check your understanding: the main relationships
> **Q1.** The dollar index rallies strongly. What tends to happen to gold and to Thai stocks, and why?
> > [!answer]-
> > Both tend to come under pressure: gold is priced in dollars, and a strong dollar tightens funding for emerging markets, so foreign investors often sell. These are tendencies, not laws.
""")
L.before_heading("en", "3.", """
> [!check]- Check your understanding: confirmation and divergence
> **Q1.** The S&P 500 makes a new high, but high-yield credit spreads are widening. What is this called, and what does it suggest?
> > [!answer]-
> > A divergence: the bond market is getting nervous while stocks are still rising. It doesn't time a top, but it's a reason for caution and smaller size.
""")
L.before_callout("en", "example", """
![[p10-fx-effect.en.svg]]

> [!walkthrough] Step by step: a US stock return in baht
> You convert **360,000 THB** at USD/THB **36.0** → **10,000 USD**, and the US stock rises **10%** → **11,000 USD**.
> 1. **Baht stable (36.0):** 11,000 × 36.0 = **396,000 THB** → **+10%**.
> 2. **Baht strengthens to 32.4:** 11,000 × 32.4 = **356,400 THB** → **−1%**. The gain is gone.
> 3. **Baht weakens to 39.6:** 11,000 × 39.6 = **435,600 THB** → **+21%**.
> 4. **So what?** A foreign investment is two bets: the asset and the currency. Always measure your result in the currency you spend.

> [!check]- Check your understanding: the Thai dashboard
> **Q1.** Why does the oil price matter so much for Thailand?
> > [!answer]-
> > Thailand is a net energy importer, so higher oil raises inflation, worsens the trade balance and affects energy stocks such as the PTT group.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** the dollar index and yield differentials are the main drivers of USD pairs, including USD/THB *(see 0.3)*.
> - **Gold:** usually moves against real yields and the dollar, and rises in fear *(see 0.4)*.
> - **Stocks:** watch yields and credit spreads for confirmation of index moves *(see 0.5, 0.6)*.
> - **Crypto:** in recent years has behaved like a high-risk asset: it often falls in risk-off moves with growth stocks *(see 0.7)*.

> [!caution]
> Currency moves can wipe out or double a foreign return, and correlations can break suddenly in a crisis. Don't lever up a position because "the intermarket picture confirms it": the context can flip in one data release.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Name four markets you would put on an intermarket watchlist and what each tells you.
> > [!answer]-
> > For example: US 10-year yield (price of money), DXY (dollar strength), oil (inflation pressure), gold (fear and real yields); add VIX and USD/THB if you invest in Thailand.
> **Q2.** A US ETF rose 8% in dollars, while USD/THB went from 36.0 to 34.0. What's your return in baht?
> > [!answer]-
> > 1.08 × (34.0 ÷ 36.0) − 1 ≈ **+2.0%**.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ตลาดต่าง ๆ เหมือนห้องในบ้านหลังเดียวที่ใช้ท่อน้ำร่วมกัน เมื่อ "ราคาของเงิน" (อัตราดอกเบี้ย) หรือค่าเงินดอลลาร์เปลี่ยน น้ำจะไหลจากบางห้องไปห้องอื่น การดูห้องข้างเคียงไม่กี่ห้องบอกคุณว่าการขยับในห้องของคุณเป็นส่วนหนึ่งของการไหลทั้งบ้าน หรือเป็นแค่น้ำกระเซ็นเฉพาะที่
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **การวิเคราะห์ระหว่างตลาด (Intermarket analysis)** — อ่านตลาดหนึ่งในบริบทของตลาดที่เกี่ยวข้อง
> - **DXY (US dollar index)** — ค่าดอลลาร์เทียบกับตะกร้าสกุลเงินหลักหกสกุล
> - **ผลตอบแทนที่แท้จริง (Real yield)** — ผลตอบแทนพันธบัตรลบเงินเฟ้อที่คาดไว้
> - **ส่วนต่างเครดิต (Credit spread)** — ผลตอบแทนส่วนเพิ่มที่บริษัทจ่ายเหนือพันธบัตรรัฐบาล ถ่างออกเมื่อผู้ให้กู้กังวล
> - **พันธบัตรผลตอบแทนสูง (High-yield / Junk bonds)** — พันธบัตรของบริษัทที่เสี่ยงกว่า ส่วนต่างของมันเป็นมาตรวัดความตึงเครียดล่วงหน้า
> - **Risk-on / Risk-off** — ช่วงที่นักลงทุนซื้อสินทรัพย์เสี่ยง / หนีไปหาความปลอดภัย
> - **สหสัมพันธ์ (Correlation)** — ตลาดสองแห่งเคลื่อนไหวไปด้วยกันแค่ไหน จาก −1 (ตรงข้าม) ถึง +1 (ไปด้วยกัน) *(ดู 9.1)*
> - **ตลาดเกิดใหม่ (EM / Emerging markets)** — เศรษฐกิจกำลังพัฒนา เช่น ไทย อินโดนีเซีย บราซิล
> - **SET / SET50** — ตลาดหลักทรัพย์แห่งประเทศไทย / ดัชนีหุ้นใหญ่ที่สุด 50 ตัว *(ดู 0.5)*
> - **THB** — เงินบาท
> - **Brent** — ราคาอ้างอิงน้ำมันหลักของโลก
""")
L.before_heading("th", "2.", """
> [!analogy]
> นึกถึง **ท่อน้ำที่เชื่อมกัน** ในอาคาร: เปิดก๊อกใหญ่ที่ชั้นหนึ่ง (Fed ขึ้นดอกเบี้ย) แรงดันที่ชั้นอื่นก็ลดลง (หุ้น ทอง ตลาดเกิดใหม่) ช่างประปาที่ดูแค่ก๊อกเดียวจะมองไม่เห็นสาเหตุ
>
> **จุดที่เปรียบเทียบไม่ได้:** ท่อน้ำทำตามหลักฟิสิกส์ที่ตายตัว แต่ความเชื่อมโยงของตลาดคือพฤติกรรมของนักลงทุน และเปลี่ยนไปตามสภาวะ: ในปี 2022 หุ้นและพันธบัตรลงพร้อมกัน ตรงข้ามกับรูปแบบปกติ

> [!walkthrough] ไล่ทีละขั้น: ผลตอบแทนที่แท้จริง
> 1. ผลตอบแทนพันธบัตรสหรัฐ 10 ปีอยู่ที่ **4.5%** และเงินเฟ้อที่คาดไว้ **2.3%** (ตัวเลขตัวอย่าง)
> 2. Real yield = 4.5 − 2.3 = **2.2%**: สิ่งที่ผู้ถือพันธบัตรได้หลังหักเงินเฟ้อ
> 3. ถ้าผลตอบแทนยังอยู่ที่ 4.5% แต่เงินเฟ้อที่คาดเพิ่มเป็น 2.8% Real yield ลดลงเหลือ **1.7%**: มักเป็นผลดีต่อทองซึ่งไม่จ่ายผลตอบแทน
> 4. **แล้วไง?** เมื่อวิเคราะห์ทองและหุ้นเติบโต ให้ดู Real yield ไม่ใช่แค่ผลตอบแทนที่ประกาศ

> [!check]- เช็กความเข้าใจ: ความสัมพันธ์หลัก
> **Q1.** ดัชนีดอลลาร์พุ่งแรง ทองและหุ้นไทยมักเป็นอย่างไร และเพราะอะไร?
> > [!answer]-
> > ทั้งสองมักถูกกดดัน: ทองตั้งราคาเป็นดอลลาร์ และดอลลาร์แข็งทำให้เงินทุนของตลาดเกิดใหม่ตึงตัว นักลงทุนต่างชาติจึงมักขาย นี่คือแนวโน้ม ไม่ใช่กฎ
""")
L.before_heading("th", "3.", """
> [!check]- เช็กความเข้าใจ: การยืนยันและการแตกต่าง
> **Q1.** S&P 500 ทำจุดสูงใหม่ แต่ส่วนต่างเครดิตของพันธบัตรผลตอบแทนสูงกำลังถ่างออก เรียกว่าอะไร และบอกอะไร?
> > [!answer]-
> > การแตกต่าง (Divergence): ตลาดพันธบัตรเริ่มกังวลขณะที่หุ้นยังขึ้น มันไม่ได้บอกจังหวะยอด แต่เป็นเหตุผลให้ระวังและลดขนาด
""")
L.before_callout("th", "example", """
![[p10-fx-effect.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ผลตอบแทนหุ้นสหรัฐเป็นเงินบาท
> คุณแลก **360,000 บาท** ที่ USD/THB **36.0** → **10,000 ดอลลาร์** และหุ้นสหรัฐขึ้น **10%** → **11,000 ดอลลาร์**
> 1. **บาทคงที่ (36.0):** 11,000 × 36.0 = **396,000 บาท** → **+10%**
> 2. **บาทแข็งเป็น 32.4:** 11,000 × 32.4 = **356,400 บาท** → **−1%** กำไรหายหมด
> 3. **บาทอ่อนเป็น 39.6:** 11,000 × 39.6 = **435,600 บาท** → **+21%**
> 4. **แล้วไง?** การลงทุนต่างประเทศคือการเดิมพันสองอย่าง: ตัวสินทรัพย์และค่าเงิน วัดผลเป็นสกุลเงินที่คุณใช้จ่ายเสมอ

> [!check]- เช็กความเข้าใจ: แดชบอร์ดไทย
> **Q1.** ทำไมราคาน้ำมันจึงสำคัญมากสำหรับประเทศไทย?
> > [!answer]-
> > ไทยเป็นผู้นำเข้าพลังงานสุทธิ น้ำมันที่แพงขึ้นจึงดันเงินเฟ้อ ทำให้ดุลการค้าแย่ลง และกระทบหุ้นพลังงาน เช่น กลุ่ม ปตท.
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** ดัชนีดอลลาร์และส่วนต่างผลตอบแทนเป็นตัวขับหลักของคู่ USD รวมถึง USD/THB *(ดู 0.3)*
> - **ทองคำ:** มักเคลื่อนสวนทางกับ Real yield และดอลลาร์ และขึ้นเมื่อตลาดกลัว *(ดู 0.4)*
> - **หุ้น:** ดูผลตอบแทนพันธบัตรและส่วนต่างเครดิตเพื่อยืนยันการขยับของดัชนี *(ดู 0.5, 0.6)*
> - **คริปโต:** ช่วงหลายปีหลังทำตัวเหมือนสินทรัพย์เสี่ยงสูง มักลงพร้อมหุ้นเติบโตในช่วง Risk-off *(ดู 0.7)*

> [!caution]
> การขยับของค่าเงินลบหรือเพิ่มผลตอบแทนต่างประเทศได้เป็นเท่าตัว และสหสัมพันธ์อาจแตกกะทันหันในวิกฤต อย่าเพิ่มเลเวอเรจเพราะ "ภาพระหว่างตลาดยืนยันแล้ว": บริบทพลิกได้ในการประกาศข้อมูลครั้งเดียว
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกตลาดสี่แห่งที่คุณจะใส่ใน Watchlist ระหว่างตลาด และแต่ละแห่งบอกอะไร
> > [!answer]-
> > ตัวอย่าง: ผลตอบแทนพันธบัตรสหรัฐ 10 ปี (ราคาของเงิน), DXY (ความแข็งของดอลลาร์), น้ำมัน (แรงกดดันเงินเฟ้อ), ทอง (ความกลัวและ Real yield) เพิ่ม VIX และ USD/THB ถ้าลงทุนในไทย
> **Q2.** ETF สหรัฐขึ้น 8% เป็นดอลลาร์ ขณะที่ USD/THB จาก 36.0 เป็น 34.0 ผลตอบแทนเป็นบาทเท่าไร?
> > [!answer]-
> > 1.08 × (34.0 ÷ 36.0) − 1 ≈ **+2.0%**
""")

L.set_meta("level", "v2")
L.save()
