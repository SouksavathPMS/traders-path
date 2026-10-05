"""B7 · v2 upgrade of 8.6 Vanna (VEX) & Charm (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("08 Options & Dealer Positioning/8.6 Vanna (VEX) & Charm.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Big option dealers protect themselves against the options they've sold by holding futures. How much protection they need depends on three things: price, time and fear. As days pass, or as fear calms down after an event, the puts customers hold become less "dangerous", so dealers need less protection and **buy back** the futures they had sold. Nobody decided the market should go up; the protection simply melted. That's why markets often drift higher after scary events and in the days before options expire.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Delta** — how much an option's price moves when the underlying moves 1 point; for puts it's negative *(see 8.2)*.
> - **Dealer / market maker** — the firm on the other side of customers' option trades, which hedges its risk *(see 8.3)*.
> - **Hedge** — an offsetting position; here, dealers short futures to balance the positive delta of the puts they're short.
> - **Vanna** — how much delta changes when implied volatility changes.
> - **Charm** — how much delta changes as time passes ("delta decay").
> - **VEX (vanna exposure)** — dealers' total vanna; like GEX *(see 8.4)*, but for volatility changes.
> - **IV (implied volatility)** — the volatility priced into options *(see 8.2)*.
> - **IV crush** — a sharp fall in IV right after an event *(see 0.6)*.
> - **OTM / ATM (out of / at the money)** — a put with strike below the current price / at it *(see 8.1)*.
> - **OPEX (options expiration)** — the day options expire; monthly OPEX is the third Friday *(see 8.5)*.
> - **CPI (Consumer Price Index)** — the main US inflation report, a big scheduled event *(see 0.8)*.
> - **VIX** — the index of expected 30-day S&P 500 volatility from option prices *(see 6.6)*.
""")
L.before_heading("en", "2.", """
![[p8-hedge-melt.en.svg]]

> [!analogy]
> A dealer's hedge against customers' puts is like **ice protecting a drink from getting warm**. The more danger (fear, time left), the more ice you need. As time passes and the danger shrinks, the ice **melts**, and the dealer takes its futures shorts off: that is buying. Charm is the melting from time; vanna is the melting when fear (IV) cools.
>
> **Where it breaks:** ice only melts one way. The hedge can also **grow** again: if fear spikes, IV rises, put deltas grow and dealers must sell more futures (reverse vanna).

> [!check]- Check your understanding: the two Greeks
> **Q1.** Which Greek describes delta changing as **time** passes, and which one as **volatility** changes?
> > [!answer]-
> > Time: charm. Volatility: vanna.
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: a put delta from −0.30 to −0.20, and the futures dealers buy back
> Index **5,000**, put strike **4,885**, 20 days left, IV **20%** (Black-Scholes, as in the figure). Customers are long **10,000** of these puts; dealers are short them.
> 1. **Start:** put delta **−0.30** → a short put has delta +0.30 → dealers hedge by shorting 10,000 × 0.30 ≈ **3,014** futures.
> 2. **Charm only** (12 days pass, IV unchanged): delta shrinks to **−0.21** → hedge **2,117** → dealers **buy back 897** futures.
> 3. **Vanna only** (same day, IV falls from 20% to 12%): delta **−0.20** → hedge **1,998** → **buy back 1,016**.
> 4. **Both** (5 days pass and IV falls to 14%): delta **−0.20** → hedge **2,021** → **buy back 993**.
> 5. **So what?** In every case, roughly **1,000 futures** get bought without any customer deciding to buy. That mechanical buying is the "supportive flow" into OPEX and after events.

> [!check]- Check your understanding: the flow
> **Q1.** If customers mostly hold **calls** instead of puts and dealers are short them, what does falling IV do to dealers' hedges?
> > [!answer]-
> > OTM call deltas shrink too, so dealers who were long futures to hedge short calls would **sell** some of them back. The direction of the flow depends on who holds what.
""")
L.before_callout("en", "example", """
> [!walkthrough] Step by step: reverse vanna when fear spikes
> Same put (strike 4,885, 20 days), but IV **rises** from 20% to **28%** after a shock.
> 1. Put delta goes from **−0.30** to **−0.35**.
> 2. Dealers' hedge grows from **3,014** to **3,491** short futures.
> 3. They must **sell 477 more futures**, into a falling market.
> 4. **So what?** The same mechanics that support calm markets **accelerate** declines when fear jumps. Vanna is a tailwind in calm and a headwind in panic.

> [!check]- Check your understanding: timing
> **Q1.** Why is the week **after** monthly OPEX often called a "window of weakness"?
> > [!answer]-
> > The expiring options and their charm/vanna support disappear, so the steady dealer buying stops, and the market is more exposed to new selling.
""")
L.before_callout("en", "action", """
> [!market]
> - **Stocks & indices:** these flows matter most for the S&P 500 (SPX, ES, SPY) and big single stocks with huge options markets (e.g. NVDA, *see 0.6*).
> - **Gold:** gold options exist (on GC futures and GLD) but are much smaller relative to the market, so these flows are weaker *(see 0.4)*.
> - **Forex:** FX options are traded over the counter; dealer positioning is not public, so these effects can't be estimated retail-side *(see 0.3)*.
> - **Crypto:** Bitcoin and Ether options (e.g. on Deribit) have big quarterly expiries; charm/vanna effects are discussed there too, with the same uncertainty *(see 0.7)*.

> [!caution]
> Vanna and charm describe tendencies, not guarantees. Shorting into a calm pre-OPEX drift is often painful; but buying because "vanna will push it up" can fail badly if fear suddenly returns, when the same mechanics reverse. Use them as context and keep normal stops and size.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Customers are long puts and dealers hedge with short futures. What happens to dealer flow as (a) time passes and (b) IV falls?
> > [!answer]-
> > In both cases put deltas shrink, dealers need fewer short futures, and they buy futures back: supportive flow.
> **Q2.** Using the walkthrough, how many futures do dealers buy back when a 10,000-put position's delta goes from −0.30 to −0.20?
> > [!answer]-
> > About 1,000 (10,000 × 0.10).
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ดีลเลอร์ออปชันรายใหญ่ปกป้องตัวเองจากออปชันที่ขายไปด้วยการถือฟิวเจอร์ส ต้องการการปกป้องมากแค่ไหนขึ้นกับสามอย่าง: ราคา เวลา และความกลัว เมื่อวันผ่านไป หรือความกลัวสงบลงหลังเหตุการณ์ Put ที่ลูกค้าถือก็ "อันตราย" น้อยลง ดีลเลอร์จึงต้องการการปกป้องน้อยลงและ **ซื้อคืน** ฟิวเจอร์สที่ขายไว้ ไม่มีใครตัดสินใจให้ตลาดขึ้น การปกป้องแค่ละลายไปเอง นี่คือเหตุผลที่ตลาดมักไหลขึ้นหลังเหตุการณ์น่ากลัว และในวันก่อนออปชันหมดอายุ
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **Delta** — ราคาออปชันขยับเท่าไหร่เมื่อสินทรัพย์อ้างอิงขยับ 1 จุด ของ Put เป็นค่าลบ *(ดู 8.2)*
> - **ดีลเลอร์ / มาร์เก็ตเมกเกอร์ (Dealer / Market maker)** — บริษัทที่อยู่อีกฝั่งของการซื้อขายออปชันของลูกค้า และเฮดจ์ความเสี่ยงของตัวเอง *(ดู 8.3)*
> - **เฮดจ์ (Hedge)** — โพซิชันหักล้าง ที่นี่คือดีลเลอร์ Short ฟิวเจอร์สเพื่อหักล้าง Delta บวกของ Put ที่ตัวเอง Short
> - **Vanna** — Delta เปลี่ยนเท่าไหร่เมื่อความผันผวนแฝงเปลี่ยน
> - **Charm** — Delta เปลี่ยนเท่าไหร่เมื่อเวลาผ่านไป ("Delta decay")
> - **VEX (Vanna exposure)** — Vanna รวมของดีลเลอร์ เหมือน GEX *(ดู 8.4)* แต่สำหรับความผันผวนที่เปลี่ยน
> - **IV (Implied volatility)** — ความผันผวนที่ตั้งราคาอยู่ในออปชัน *(ดู 8.2)*
> - **IV crush** — IV ร่วงแรงทันทีหลังเหตุการณ์ *(ดู 0.6)*
> - **OTM / ATM (Out of / At the money)** — Put ที่ Strike ต่ำกว่าราคาปัจจุบัน / เท่ากับราคาปัจจุบัน *(ดู 8.1)*
> - **OPEX (Options expiration)** — วันที่ออปชันหมดอายุ OPEX รายเดือนคือวันศุกร์ที่สาม *(ดู 8.5)*
> - **CPI (Consumer Price Index)** — รายงานเงินเฟ้อหลักของสหรัฐ เหตุการณ์ใหญ่ที่มีกำหนดการ *(ดู 0.8)*
> - **VIX** — ดัชนีความผันผวน 30 วันที่คาดของ S&P 500 จากราคาออปชัน *(ดู 6.6)*
""")
L.before_heading("th", "2.", """
![[p8-hedge-melt.th.svg]]

> [!analogy]
> เฮดจ์ของดีลเลอร์ต่อ Put ของลูกค้าเหมือน **น้ำแข็งที่กันเครื่องดื่มไม่ให้อุ่น** ยิ่งอันตรายมาก (ความกลัว เวลาที่เหลือ) ยิ่งต้องใช้น้ำแข็งมาก เมื่อเวลาผ่านไปและอันตรายลดลง น้ำแข็งก็ **ละลาย** และดีลเลอร์ปิด Short ฟิวเจอร์ส: นั่นคือการซื้อ Charm คือการละลายจากเวลา Vanna คือการละลายเมื่อความกลัว (IV) เย็นลง
>
> **จุดที่เปรียบเทียบไม่ได้:** น้ำแข็งละลายได้ทางเดียว แต่เฮดจ์ **โตขึ้น** ใหม่ได้ ถ้าความกลัวพุ่ง IV เพิ่ม Delta ของ Put โตขึ้น และดีลเลอร์ต้องขายฟิวเจอร์สเพิ่ม (Reverse vanna)

> [!check]- เช็กความเข้าใจ: Greeks สองตัว
> **Q1.** Greek ตัวไหนอธิบาย Delta ที่เปลี่ยนเมื่อ **เวลา** ผ่านไป และตัวไหนเมื่อ **ความผันผวน** เปลี่ยน?
> > [!answer]-
> > เวลา: Charm ความผันผวน: Vanna
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: Delta ของ Put จาก −0.30 เป็น −0.20 และฟิวเจอร์สที่ดีลเลอร์ซื้อคืน
> ดัชนี **5,000** Put Strike **4,885** เหลือ 20 วัน IV **20%** (Black-Scholes เหมือนในภาพ) ลูกค้า Long Put นี้ **10,000** สัญญา ดีลเลอร์ Short
> 1. **เริ่ม:** Delta ของ Put **−0.30** → Put ที่ Short มี Delta +0.30 → ดีลเลอร์เฮดจ์ด้วยการ Short ฟิวเจอร์ส 10,000 × 0.30 ≈ **3,014** สัญญา
> 2. **Charm อย่างเดียว** (ผ่านไป 12 วัน IV เท่าเดิม): Delta หดเหลือ **−0.21** → เฮดจ์ **2,117** → ดีลเลอร์ **ซื้อคืน 897** สัญญา
> 3. **Vanna อย่างเดียว** (วันเดียวกัน IV ลดจาก 20% เป็น 12%): Delta **−0.20** → เฮดจ์ **1,998** → **ซื้อคืน 1,016**
> 4. **ทั้งสองอย่าง** (ผ่านไป 5 วันและ IV ลดเป็น 14%): Delta **−0.20** → เฮดจ์ **2,021** → **ซื้อคืน 993**
> 5. **แล้วไง?** ทุกกรณีมีการซื้อฟิวเจอร์สราว **1,000 สัญญา** โดยไม่มีลูกค้าคนไหนตัดสินใจซื้อ แรงซื้อเชิงกลไกนี้คือ "กระแสหนุน" ช่วงก่อน OPEX และหลังเหตุการณ์

> [!check]- เช็กความเข้าใจ: กระแสเงิน
> **Q1.** ถ้าลูกค้าส่วนใหญ่ถือ **Call** แทน Put และดีลเลอร์ Short Call เหล่านั้น IV ที่ลดลงทำอะไรกับเฮดจ์ของดีลเลอร์?
> > [!answer]-
> > Delta ของ Call ที่ OTM ก็หดเช่นกัน ดีลเลอร์ที่ Long ฟิวเจอร์สเพื่อเฮดจ์ Short call จะ **ขาย** คืนบางส่วน ทิศทางของกระแสขึ้นกับว่าใครถืออะไร
""")
L.before_callout("th", "example", """
> [!walkthrough] ไล่ทีละขั้น: Reverse vanna เมื่อความกลัวพุ่ง
> Put เดิม (Strike 4,885 เหลือ 20 วัน) แต่ IV **เพิ่ม** จาก 20% เป็น **28%** หลังเกิดเหตุช็อก
> 1. Delta ของ Put เปลี่ยนจาก **−0.30** เป็น **−0.35**
> 2. เฮดจ์ของดีลเลอร์โตจาก **3,014** เป็น **3,491** สัญญา Short ฟิวเจอร์ส
> 3. ดีลเลอร์ต้อง **ขายฟิวเจอร์สเพิ่ม 477 สัญญา** ใส่ตลาดที่กำลังลง
> 4. **แล้วไง?** กลไกเดียวกับที่หนุนตลาดที่สงบ **เร่ง** การร่วงเมื่อความกลัวพุ่ง Vanna เป็นลมส่งท้ายตอนสงบ และเป็นลมต้านตอนตื่นตระหนก

> [!check]- เช็กความเข้าใจ: จังหวะเวลา
> **Q1.** ทำไมสัปดาห์ **หลัง** OPEX รายเดือนจึงมักถูกเรียกว่า "ช่วงอ่อนแอ"?
> > [!answer]-
> > ออปชันที่หมดอายุและแรงหนุนจาก Charm/Vanna หายไป แรงซื้อสม่ำเสมอของดีลเลอร์จึงหยุด และตลาดเปิดรับแรงขายใหม่มากขึ้น
""")
L.before_callout("th", "action", """
> [!market]
> - **หุ้นและดัชนี:** กระแสเหล่านี้สำคัญที่สุดกับ S&P 500 (SPX, ES, SPY) และหุ้นใหญ่ที่มีตลาดออปชันมหาศาล (เช่น NVDA *ดู 0.6*)
> - **ทองคำ:** มีออปชันทอง (บนฟิวเจอร์ส GC และ GLD) แต่เล็กกว่ามากเมื่อเทียบกับตลาด กระแสเหล่านี้จึงอ่อนกว่า *(ดู 0.4)*
> - **ฟอเร็กซ์:** ออปชัน FX ซื้อขายนอกตลาด สถานะของดีลเลอร์ไม่เปิดเผย รายย่อยจึงประเมินผลเหล่านี้ไม่ได้ *(ดู 0.3)*
> - **คริปโต:** ออปชัน Bitcoin และ Ether (เช่น บน Deribit) มีวันหมดอายุรายไตรมาสก้อนใหญ่ มีการพูดถึงผลของ Charm/Vanna เช่นกัน ด้วยความไม่แน่นอนแบบเดียวกัน *(ดู 0.7)*

> [!caution]
> Vanna และ Charm อธิบายแนวโน้ม ไม่ใช่การรับประกัน การ Short สวนการไหลขึ้นที่สงบก่อน OPEX มักเจ็บ แต่การซื้อเพราะ "Vanna จะดันขึ้น" ก็พังหนักได้ถ้าความกลัวกลับมาทันที เมื่อกลไกเดียวกันกลับทิศ ใช้เป็นบริบท และใช้ Stop กับขนาดไม้ตามปกติ
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** ลูกค้า Long Put และดีลเลอร์เฮดจ์ด้วย Short ฟิวเจอร์ส จะเกิดอะไรกับกระแสของดีลเลอร์เมื่อ (ก) เวลาผ่านไป และ (ข) IV ลดลง?
> > [!answer]-
> > ทั้งสองกรณี Delta ของ Put หดลง ดีลเลอร์ต้องการ Short ฟิวเจอร์สน้อยลง และซื้อฟิวเจอร์สคืน: กระแสหนุน
> **Q2.** จากตัวอย่าง ดีลเลอร์ซื้อฟิวเจอร์สคืนกี่สัญญาเมื่อ Delta ของ Put 10,000 สัญญาเปลี่ยนจาก −0.30 เป็น −0.20?
> > [!answer]-
> > ราว 1,000 (10,000 × 0.10)
""")

L.set_meta("level", "v2")
L.save()
