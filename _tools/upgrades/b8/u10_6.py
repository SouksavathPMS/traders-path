"""B8 · v2 upgrade of 10.6 Fundamental Analysis & Valuation (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("10 Macro, Wall Street & Investing/10.6 Fundamental Analysis & Valuation.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Buying a share means owning a tiny slice of a real business. A business is worth the cash it will hand back to its owners over its life. Money you get later is worth less than money today, so future cash is "discounted". If you pay much less than that value, you have room for mistakes; if you pay much more, you need everything to go right.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Fundamental analysis** — judging a business by its sales, profits, cash, debt and competitive position.
> - **FCF (free cash flow)** — cash from operations minus investment spending (capex): cash the owners could take out.
> - **PV (present value)** — what a future amount is worth today, after discounting.
> - **Discount rate** — the yearly return you require; higher rates mean lower present values.
> - **DCF (discounted cash flow)** — valuing a business as the sum of the present values of its future cash flows.
> - **Terminal value** — the value of all cash flows after the forecast years.
> - **EBITDA** — earnings before interest, taxes, depreciation and amortisation: a rough measure of operating profit.
> - **Net debt** — debt minus cash.
> - **EV (enterprise value)** — market cap + debt − cash: the price of the whole business.
> - **P/E, P/B** — price ÷ earnings per share; price ÷ book value per share.
> - **ROE / ROIC** — return on equity / on invested capital: how much profit each unit of capital earns.
> - **Moat** — a lasting competitive advantage that protects profits.
> - **Margin of safety** — the gap between your value estimate and the price you pay.
""")
L.before_heading("en", "2.", """
> [!analogy]
> Valuing a company is like valuing a **rental flat**. You look at the rent it brings in (cash flow), the repairs it needs (capex), any mortgage on it (debt), and how the area will develop (growth and moat). Then you ask how many years of rent you are paying.
>
> **Where it breaks:** a flat's rent is fairly predictable and the flat stays the same. A company's cash flows can grow, shrink or disappear as competitors, technology and managers change.

> [!check]- Check your understanding: reading a business
> **Q1.** A company reports rising net income every year, but free cash flow has been negative for five years. What's the concern?
> > [!answer]-
> > Profits aren't turning into cash; it may need heavy investment, or its accounting profits may be of low quality. Owners can only be paid from cash.
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: present value
> 1. You'll receive **100** in one year. At an **8%** discount rate it's worth 100 ÷ 1.08 = **92.59** today.
> 2. The same 100 in **10 years**: 100 ÷ 1.08¹⁰ = **46.32** today.
> 3. At **10%**: 100 ÷ 1.10¹⁰ = **38.55**, about 17% less, just from a 2-point rate change.
> 4. **So what?** Distant cash flows are very sensitive to interest rates. That is why growth stocks (most value far in the future) react most to rate changes.

![[p10-ev-bridge.en.svg]]

> [!walkthrough] Step by step: why EV beats market cap
> Both companies have a market cap of **10 bn** and EBITDA of **1.2 bn**.
> 1. **Company A:** no debt, 1 bn cash → EV = 10 + 0 − 1 = **9 bn** → EV/EBITDA = 9 ÷ 1.2 = **7.5×**.
> 2. **Company B:** 6 bn debt, no cash → EV = 10 + 6 − 0 = **16 bn** → EV/EBITDA = 16 ÷ 1.2 ≈ **13.3×**.
> 3. **FCF yield** for a stock at **40** with FCF per share **2.0**: 2.0 ÷ 40 = **5%**.
> 4. **So what?** Two companies with the same market cap can be very differently priced. Buying B means also taking on its debt.

> [!check]- Check your understanding: valuation
> **Q1.** Why did raising the discount rate from 8% to 10% cut the DCF value in the table by 26%?
> > [!answer]-
> > Every future cash flow is divided by a bigger number, and most of the value lies far in the future (terminal value), where the effect is largest.
""")
L.before_callout("en", "action", """
> [!check]- Check your understanding: margin of safety
> **Q1.** Your value estimate is 41 and the price is 30. What's the margin of safety?
> > [!answer]-
> > (41 − 30) ÷ 41 ≈ **27%**.

> [!market]
> - **Forex:** currencies have no cash flows; their "fundamentals" are rates, inflation and trade balances *(see 10.2, 0.3)*.
> - **Gold:** pays no cash flow, so a DCF doesn't apply; it competes with real yields *(see 10.4, 0.4)*.
> - **Stocks:** where this lesson applies fully *(see 0.5)*.
> - **Crypto:** most tokens have no cash flows to discount; treat valuation claims with extra scepticism *(see 0.7)*.

> [!caution]
> A low P/E or a high dividend yield can be a **value trap**: the business is shrinking and the "cheap" price keeps falling. A DCF built on optimistic inputs can justify any price. Don't concentrate your savings in one "undervalued" stock.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Why do higher interest rates lower the value of a business, even if nothing changes in the business?
> > [!answer]-
> > Future cash flows are discounted at a higher rate, so their present value falls.
> **Q2.** Company X: market cap 20 bn, debt 5 bn, cash 1 bn, EBITDA 2 bn. What are its EV and EV/EBITDA?
> > [!answer]-
> > EV = 20 + 5 − 1 = **24 bn**; EV/EBITDA = 24 ÷ 2 = **12×**.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> การซื้อหุ้นคือการเป็นเจ้าของชิ้นเล็ก ๆ ของธุรกิจจริง ธุรกิจมีค่าเท่ากับเงินสดที่มันจะคืนให้เจ้าของตลอดอายุ เงินที่ได้ทีหลังมีค่าน้อยกว่าเงินวันนี้ เงินสดในอนาคตจึงถูก "คิดลด" ถ้าคุณจ่ายน้อยกว่ามูลค่านั้นมาก คุณมีที่ว่างให้ผิดพลาด ถ้าจ่ายมากกว่ามาก ทุกอย่างต้องเป็นไปตามคาด
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **การวิเคราะห์ปัจจัยพื้นฐาน (Fundamental analysis)** — ตัดสินธุรกิจจากยอดขาย กำไร เงินสด หนี้ และสถานะการแข่งขัน
> - **กระแสเงินสดอิสระ (FCF / Free cash flow)** — เงินสดจากการดำเนินงานลบรายจ่ายลงทุน (Capex): เงินที่เจ้าของเอาออกไปได้
> - **มูลค่าปัจจุบัน (PV / Present value)** — มูลค่าวันนี้ของเงินในอนาคตหลังคิดลด
> - **อัตราคิดลด (Discount rate)** — ผลตอบแทนต่อปีที่คุณต้องการ อัตราสูงขึ้น มูลค่าปัจจุบันต่ำลง
> - **DCF (Discounted cash flow)** — ประเมินธุรกิจเป็นผลรวมมูลค่าปัจจุบันของกระแสเงินสดในอนาคต
> - **มูลค่าสุดท้าย (Terminal value)** — มูลค่าของกระแสเงินสดทั้งหมดหลังปีที่พยากรณ์
> - **EBITDA** — กำไรก่อนดอกเบี้ย ภาษี ค่าเสื่อมราคาและค่าตัดจำหน่าย: มาตรวัดคร่าว ๆ ของกำไรจากการดำเนินงาน
> - **หนี้สุทธิ (Net debt)** — หนี้ลบเงินสด
> - **EV (Enterprise value)** — มูลค่าตลาด + หนี้ − เงินสด: ราคาของทั้งธุรกิจ
> - **P/E, P/B** — ราคา ÷ กำไรต่อหุ้น; ราคา ÷ มูลค่าทางบัญชีต่อหุ้น
> - **ROE / ROIC** — ผลตอบแทนต่อส่วนของผู้ถือหุ้น / ต่อเงินลงทุน: เงินทุนแต่ละหน่วยสร้างกำไรได้เท่าไร
> - **คูเมือง (Moat)** — ความได้เปรียบทางการแข่งขันที่ยั่งยืนและปกป้องกำไร
> - **ส่วนเผื่อความปลอดภัย (Margin of safety)** — ช่องว่างระหว่างมูลค่าที่คุณประเมินกับราคาที่จ่าย
""")
L.before_heading("th", "2.", """
> [!analogy]
> การประเมินมูลค่าบริษัทเหมือนการประเมิน **ห้องชุดให้เช่า** คุณดูค่าเช่าที่ได้ (กระแสเงินสด) ค่าซ่อมที่ต้องจ่าย (Capex) ภาระจำนอง (หนี้) และทำเลจะพัฒนาอย่างไร (การเติบโตและคูเมือง) แล้วถามว่าคุณกำลังจ่ายค่าเช่ากี่ปี
>
> **จุดที่เปรียบเทียบไม่ได้:** ค่าเช่าห้องค่อนข้างคาดเดาได้และห้องก็เหมือนเดิม แต่กระแสเงินสดของบริษัทเติบโต หดตัว หรือหายไปได้ เมื่อคู่แข่ง เทคโนโลยี และผู้บริหารเปลี่ยน

> [!check]- เช็กความเข้าใจ: อ่านธุรกิจ
> **Q1.** บริษัทรายงานกำไรสุทธิเพิ่มขึ้นทุกปี แต่กระแสเงินสดอิสระติดลบมาห้าปี น่ากังวลเรื่องอะไร?
> > [!answer]-
> > กำไรไม่ได้กลายเป็นเงินสด อาจต้องลงทุนหนัก หรือกำไรทางบัญชีอาจมีคุณภาพต่ำ เจ้าของได้รับเงินจากเงินสดเท่านั้น
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: มูลค่าปัจจุบัน
> 1. คุณจะได้ **100** ในหนึ่งปี ที่อัตราคิดลด **8%** มีค่าวันนี้ 100 ÷ 1.08 = **92.59**
> 2. 100 เดิมใน **10 ปี**: 100 ÷ 1.08¹⁰ = **46.32** วันนี้
> 3. ที่ **10%**: 100 ÷ 1.10¹⁰ = **38.55** น้อยลงราว 17% เพียงเพราะอัตราเปลี่ยน 2 จุด
> 4. **แล้วไง?** กระแสเงินสดที่ไกลออกไปไวต่ออัตราดอกเบี้ยมาก หุ้นเติบโต (มูลค่าส่วนใหญ่อยู่ไกลในอนาคต) จึงตอบสนองต่อการเปลี่ยนดอกเบี้ยมากที่สุด

![[p10-ev-bridge.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ทำไม EV ดีกว่ามูลค่าตลาด
> ทั้งสองบริษัทมีมูลค่าตลาด **10 พันล้าน** และ EBITDA **1.2 พันล้าน**
> 1. **บริษัท A:** ไม่มีหนี้ เงินสด 1 พันล้าน → EV = 10 + 0 − 1 = **9 พันล้าน** → EV/EBITDA = 9 ÷ 1.2 = **7.5 เท่า**
> 2. **บริษัท B:** หนี้ 6 พันล้าน ไม่มีเงินสด → EV = 10 + 6 − 0 = **16 พันล้าน** → EV/EBITDA = 16 ÷ 1.2 ≈ **13.3 เท่า**
> 3. **FCF yield** ของหุ้นราคา **40** ที่มี FCF ต่อหุ้น **2.0**: 2.0 ÷ 40 = **5%**
> 4. **แล้วไง?** สองบริษัทที่มูลค่าตลาดเท่ากันอาจถูกตั้งราคาต่างกันมาก การซื้อ B หมายถึงรับหนี้ของมันมาด้วย

> [!check]- เช็กความเข้าใจ: การประเมินมูลค่า
> **Q1.** ทำไมการเพิ่มอัตราคิดลดจาก 8% เป็น 10% ทำให้มูลค่า DCF ในตารางลดลง 26%?
> > [!answer]-
> > กระแสเงินสดในอนาคตทุกงวดถูกหารด้วยตัวเลขที่ใหญ่ขึ้น และมูลค่าส่วนใหญ่อยู่ไกลในอนาคต (Terminal value) ซึ่งได้รับผลมากที่สุด
""")
L.before_callout("th", "action", """
> [!check]- เช็กความเข้าใจ: ส่วนเผื่อความปลอดภัย
> **Q1.** มูลค่าที่คุณประเมินคือ 41 และราคาคือ 30 ส่วนเผื่อความปลอดภัยเท่าไร?
> > [!answer]-
> > (41 − 30) ÷ 41 ≈ **27%**

> [!market]
> - **ฟอเร็กซ์:** สกุลเงินไม่มีกระแสเงินสด "ปัจจัยพื้นฐาน" ของมันคือดอกเบี้ย เงินเฟ้อ และดุลการค้า *(ดู 10.2, 0.3)*
> - **ทองคำ:** ไม่จ่ายกระแสเงินสด จึงใช้ DCF ไม่ได้ มันแข่งกับ Real yield *(ดู 10.4, 0.4)*
> - **หุ้น:** บทเรียนนี้ใช้ได้เต็มที่ *(ดู 0.5)*
> - **คริปโต:** โทเคนส่วนใหญ่ไม่มีกระแสเงินสดให้คิดลด ให้สงสัยคำอ้างเรื่องมูลค่าเป็นพิเศษ *(ดู 0.7)*

> [!caution]
> P/E ต่ำหรือเงินปันผลสูงอาจเป็น **กับดักมูลค่า (Value trap)**: ธุรกิจกำลังหดตัวและราคา "ถูก" ก็ลงต่อ DCF ที่สร้างจากสมมติฐานมองโลกในแง่ดีสามารถอ้างราคาใดก็ได้ อย่ากระจุกเงินออมไว้ในหุ้น "ต่ำกว่ามูลค่า" ตัวเดียว
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** ทำไมดอกเบี้ยที่สูงขึ้นจึงลดมูลค่าธุรกิจ แม้ธุรกิจไม่ได้เปลี่ยนอะไร?
> > [!answer]-
> > กระแสเงินสดในอนาคตถูกคิดลดด้วยอัตราที่สูงขึ้น มูลค่าปัจจุบันจึงลดลง
> **Q2.** บริษัท X: มูลค่าตลาด 20 พันล้าน หนี้ 5 พันล้าน เงินสด 1 พันล้าน EBITDA 2 พันล้าน EV และ EV/EBITDA เท่าไร?
> > [!answer]-
> > EV = 20 + 5 − 1 = **24 พันล้าน**; EV/EBITDA = 24 ÷ 2 = **12 เท่า**
""")

L.set_meta("level", "v2")
L.save()
