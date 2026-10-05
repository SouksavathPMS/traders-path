"""B4 · v2 upgrade of 5.6 Time: Sessions, Killzones & Quarterly Theory (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("05 Liquidity & ICT/5.6 Time- Sessions, Killzones & Quarterly Theory.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Markets have busy hours and quiet hours, like a restaurant. When the big banks in London and New York start work, lots of orders arrive at once and prices move a lot. When they go home, prices often drift sideways. ICT gives names to the busiest windows ("killzones") and describes a typical day as: quiet build-up, a fake move, then the real move. In Thailand and Laos these windows fall in the afternoon and evening, and they shift by one hour twice a year because Europe and the US change their clocks.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Session** — the hours when a financial centre is open: Asia (Tokyo, Sydney, Shanghai), London, New York.
> - **KZ (killzone)** — ICT's name for the high-activity windows around the London and New York opens.
> - **NY time** — New York local time; ICT quotes everything in it.
> - **UTC / UTC+7** — Coordinated Universal Time / Thailand and Laos time (no daylight saving).
> - **DST (daylight saving time)** — moving clocks forward one hour in summer. The US and UK change on **different dates**.
> - **Asian range** — the high and low made during the Asian session; liquidity for later sessions *(see 5.1)*.
> - **London close** — the end of the European trading day, when the day's move often retraces.
> - **Daily open (true day open)** — ICT uses **midnight NY time** as the start of the trading day.
> - **AMD (accumulation, manipulation, distribution)** — ICT's "power of three": build-up, false move, real move.
> - **Judas swing** — the false move (manipulation) against the day's real direction.
> - **Quarterly theory** — ICT's idea of splitting every time cycle (year, month, week, day) into four quarters.
> - **Q1–Q4 (of a day)** — four 6-hour blocks starting at 18:00 NY: Asia, London, NY AM, NY PM.
> - **Q1–Q4 (of a week)** — Monday, Tuesday, Wednesday, Thursday; Friday is the "X" (reversal or continuation).
> - **US data at 08:30 NY** — the release time of CPI, jobs and similar reports *(see 0.8)*.
""")
L.before_heading("en", "2.", """
![[p5-killzones-utc7.en.svg]]

**The ICT windows in UTC+7.** ICT times are New York times, so for us they move with **US** daylight saving:

| Window | NY time | UTC+7, US summer (8 Mar – 1 Nov 2026) | UTC+7, US winter |
|---|---|---|---|
| Asian session | 19:00–04:00 | 06:00–15:00 | 07:00–16:00 |
| London killzone | 02:00–05:00 | 13:00–16:00 | 14:00–17:00 |
| NY AM killzone | 07:00–10:00 | 18:00–21:00 | 19:00–22:00 |
| London close | 10:00–12:00 | 21:00–23:00 | 22:00–00:00 |
| US data releases | 08:30 | 19:30 | 20:30 |
| US stock open | 09:30 | 20:30 | 21:30 |
| Daily open (midnight NY) | 00:00 | 11:00 | 12:00 |

**DST dates:** US summer time runs 8 Mar – 1 Nov 2026 and 14 Mar – 7 Nov 2027. UK summer time runs 29 Mar – 25 Oct 2026 and 28 Mar – 31 Oct 2027. In the **gap weeks** between those dates, New York has changed its clocks but London hasn't (or the reverse), so the real London open (08:00 London) moves to **15:00 UTC+7** while the NY-based killzones stay on the US-summer column.

> [!analogy]
> Think of the market's day as a **restaurant's shift schedule**. Morning prep (Asia) is quiet: staff set up and a few customers come in. The lunch rush (London) brings a crowd and some chaos. The dinner rush (New York) is the busiest, with the biggest orders. After closing (late New York), only a few customers drift in. You make most of your money when the restaurant is full.
>
> **Where it breaks:** a restaurant's rushes are guaranteed by meal times. Market rushes are likely, not certain: a holiday or a quiet news day can leave the "rush" empty.

> [!walkthrough] Step by step: converting ICT times to your clock
> 1. **US CPI in July** (US summer): 08:30 NY + 11 h = **19:30 UTC+7**.
> 2. **US CPI in January** (US winter): 08:30 NY + 12 h = **20:30 UTC+7**.
> 3. **London killzone in January:** 02:00–05:00 NY + 12 h = **14:00–17:00 UTC+7**.
> 4. **A gap week, 16 March 2026:** the US is already on summer time, the UK isn't. NY AM killzone = 07:00 + 11 = **18:00–21:00 UTC+7**, but the London open (08:00 GMT) = **15:00 UTC+7**, two hours into the London killzone.
> 5. **So what?** Write your trading windows in **both** NY time and UTC+7, and set calendar reminders for the four DST change dates each year. Being an hour early or late means trading the quiet part of the session.

> [!check]- Check your understanding: converting times
> **Q1.** It's December. At what time UTC+7 does the NY AM killzone start?
> > [!answer]-
> > 07:00 NY + 12 h = 19:00 UTC+7 (US winter).
> **Q2.** Why do Thai and Lao traders see the killzones move, even though Thailand and Laos never change their clocks?
> > [!answer]-
> > Because New York and London change theirs (daylight saving). The windows are fixed in NY time, so they move in UTC+7.
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: why buys below the daily open are better on a bullish day (illustrative GBP/USD)
> US summer. The daily open (midnight NY) is at **11:00 UTC+7**: **1.2650**. Daily bias: bullish.
> 1. **Accumulation (Asia):** a tight range 1.2640–1.2665.
> 2. **Manipulation (London KZ, ≈13:30 UTC+7):** a drop to **1.2628**, 22 pips **below** the daily open, sweeping the Asia low: the Judas swing.
> 3. **Entry A (below the open):** buy at **1.2648** after the MSS, stop **1.2622**, target the previous day's high **1.2720** → risk 26 pips, reward 72 pips → **2.77R**.
> 4. **Entry B (chasing after the NY open):** buy at **1.2690** with the same stop and target → risk 68 pips, reward 30 pips → **0.44R**.
> 5. **So what?** On a bullish day the best prices usually come **before** the real move, below the open. Chasing in New York means a far stop and a near target.

> [!check]- Check your understanding: AMD
> **Q1.** Your daily bias is bearish. Where do you prefer to look for shorts: above or below the daily open?
> > [!answer]-
> > Above it. On a bearish day the Judas swing often goes up first (manipulation), so the best short prices tend to be above the open.
""")
L.before_callout("en", "example", """
**Quarters of the day in UTC+7** (6-hour blocks starting 18:00 NY):

| Quarter | NY time | UTC+7, US summer | UTC+7, US winter |
|---|---|---|---|
| Q1 · Asia | 18:00–00:00 | 05:00–11:00 | 06:00–12:00 |
| Q2 · London | 00:00–06:00 | 11:00–17:00 | 12:00–18:00 |
| Q3 · NY AM | 06:00–12:00 | 17:00–23:00 | 18:00–00:00 |
| Q4 · NY PM | 12:00–18:00 | 23:00–05:00 | 00:00–06:00 |

> [!check]- Check your understanding: quarters
> **Q1.** It's August and 20:00 in Bangkok. Which quarter of the ICT day is it?
> > [!answer]-
> > Q3 (NY AM): 17:00–23:00 UTC+7 in US summer.
> **Q2.** What should you do with quarterly theory before trading it?
> > [!answer]-
> > Test it on your own data (Phase 9). It's the least proven part of ICT; treat it as a hypothesis, not a rule.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** the killzones were designed for FX; London and NY AM are where most of the day's range happens *(see 0.3)*.
> - **Gold:** same windows plus the LBMA auctions at 16:30 and 21:00 UTC+7 in northern summer *(see 0.4)*.
> - **Stocks & index futures:** the regular session is 20:30–03:00 UTC+7 (summer); the NY AM killzone covers the US data and the open *(see 0.5)*.
> - **Crypto:** 24/7, but volume still clusters in London and New York hours; the daily candle closes at 07:00 UTC+7 (00:00 UTC), not at midnight NY *(see 0.7)*.

> [!caution]
> The NY AM killzone contains the 19:30/20:30 UTC+7 US data releases. A level that looks perfect can be blown through in seconds, with slippage beyond your stop. Check the calendar every morning and don't hold a fresh setup into a red-flag release *(see 0.8)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Fill in UTC+7 for the London killzone and the NY AM killzone, in US summer and in US winter.
> > [!answer]-
> > Summer: London 13:00–16:00, NY AM 18:00–21:00. Winter: London 14:00–17:00, NY AM 19:00–22:00.
> **Q2.** Which part of this lesson is well supported by data, and which part is not?
> > [!answer]-
> > Well supported: volume and volatility cluster around session opens and data releases (you can measure it). Weakly supported: quarterly theory and exact AMD timing on every day.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ตลาดมีชั่วโมงที่ยุ่งและชั่วโมงที่เงียบ เหมือนร้านอาหาร เมื่อธนาคารใหญ่ในลอนดอนและนิวยอร์กเริ่มงาน คำสั่งจำนวนมากเข้ามาพร้อมกัน ราคาขยับมาก เมื่อเขาเลิกงาน ราคามักไหลออกข้าง ICT ตั้งชื่อช่วงที่ยุ่งที่สุดว่า "Killzone" และอธิบายวันปกติว่า: สะสมเงียบ ๆ วิ่งหลอก แล้วจึงวิ่งจริง ในไทยและลาวช่วงเวลาเหล่านี้อยู่ตอนบ่ายและค่ำ และเลื่อนหนึ่งชั่วโมงปีละสองครั้ง เพราะยุโรปและสหรัฐเปลี่ยนเวลานาฬิกา
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **เซสชัน (Session)** — ชั่วโมงที่ศูนย์กลางการเงินเปิดทำการ: เอเชีย (โตเกียว ซิดนีย์ เซี่ยงไฮ้) ลอนดอน นิวยอร์ก
> - **KZ (Killzone)** — ชื่อที่ ICT ใช้เรียกช่วงเวลาที่คึกคักรอบการเปิดของลอนดอนและนิวยอร์ก
> - **เวลานิวยอร์ก (NY time)** — เวลาท้องถิ่นของนิวยอร์ก ICT ใช้เวลานี้ทั้งหมด
> - **UTC / UTC+7** — เวลาสากลเชิงพิกัด / เวลาไทยและลาว (ไม่มีเวลาออมแสง)
> - **DST (Daylight saving time)** — การเลื่อนนาฬิกาเร็วขึ้นหนึ่งชั่วโมงช่วงฤดูร้อน สหรัฐและอังกฤษเปลี่ยน **คนละวัน**
> - **กรอบเอเชีย (Asian range)** — จุดสูงและต่ำที่เกิดช่วงเซสชันเอเชีย เป็นสภาพคล่องให้เซสชันถัดไป *(ดู 5.1)*
> - **London close** — ช่วงสิ้นวันเทรดของยุโรป ซึ่งการวิ่งของวันมักย่อกลับ
> - **ราคาเปิดรายวัน (Daily open / True day open)** — ICT ใช้ **เที่ยงคืนเวลานิวยอร์ก** เป็นจุดเริ่มวันเทรด
> - **AMD (Accumulation, manipulation, distribution)** — "Power of three" ของ ICT: สะสม วิ่งหลอก วิ่งจริง
> - **Judas swing** — การวิ่งหลอก (Manipulation) ที่สวนทิศทางจริงของวัน
> - **Quarterly theory** — แนวคิดของ ICT ที่แบ่งทุกวัฏจักรเวลา (ปี เดือน สัปดาห์ วัน) ออกเป็นสี่ส่วน
> - **Q1–Q4 (ของวัน)** — สี่ช่วงช่วงละ 6 ชั่วโมง เริ่ม 18:00 เวลานิวยอร์ก: เอเชีย ลอนดอน NY AM NY PM
> - **Q1–Q4 (ของสัปดาห์)** — วันจันทร์ อังคาร พุธ พฤหัส วันศุกร์คือ "X" (กลับตัวหรือไปต่อ)
> - **ข้อมูลสหรัฐเวลา 08:30 NY** — เวลาประกาศ CPI การจ้างงาน และรายงานลักษณะเดียวกัน *(ดู 0.8)*
""")
L.before_heading("th", "2.", """
![[p5-killzones-utc7.th.svg]]

**ช่วงเวลาของ ICT ตามเวลา UTC+7** เวลาของ ICT คือเวลานิวยอร์ก สำหรับเราจึงเลื่อนตามเวลาออมแสงของ **สหรัฐ**:

| ช่วงเวลา | เวลา NY | UTC+7 ฤดูร้อนสหรัฐ (8 มี.ค. – 1 พ.ย. 2026) | UTC+7 ฤดูหนาวสหรัฐ |
|---|---|---|---|
| เซสชันเอเชีย | 19:00–04:00 | 06:00–15:00 | 07:00–16:00 |
| London killzone | 02:00–05:00 | 13:00–16:00 | 14:00–17:00 |
| NY AM killzone | 07:00–10:00 | 18:00–21:00 | 19:00–22:00 |
| London close | 10:00–12:00 | 21:00–23:00 | 22:00–00:00 |
| ประกาศข้อมูลสหรัฐ | 08:30 | 19:30 | 20:30 |
| ตลาดหุ้นสหรัฐเปิด | 09:30 | 20:30 | 21:30 |
| ราคาเปิดรายวัน (เที่ยงคืน NY) | 00:00 | 11:00 | 12:00 |

**วันเปลี่ยนเวลาออมแสง:** เวลาฤดูร้อนของสหรัฐคือ 8 มี.ค. – 1 พ.ย. 2026 และ 14 มี.ค. – 7 พ.ย. 2027 เวลาฤดูร้อนของอังกฤษคือ 29 มี.ค. – 25 ต.ค. 2026 และ 28 มี.ค. – 31 ต.ค. 2027 ใน **สัปดาห์ที่ไม่ตรงกัน** ระหว่างวันเหล่านั้น นิวยอร์กเปลี่ยนเวลาแล้วแต่ลอนดอนยัง (หรือกลับกัน) ลอนดอนเปิดจริง (08:00 เวลาลอนดอน) จึงเลื่อนไปเป็น **15:00 UTC+7** ขณะที่ Killzone ที่อิงเวลานิวยอร์กยังอยู่ในคอลัมน์ฤดูร้อนสหรัฐ

> [!analogy]
> นึกถึงวันของตลาดเป็น **ตารางกะของร้านอาหาร** ช่วงเตรียมของตอนเช้า (เอเชีย) เงียบ: พนักงานจัดร้าน ลูกค้าไม่กี่คน ช่วงเที่ยง (ลอนดอน) คนเยอะและวุ่นวายบ้าง ช่วงเย็น (นิวยอร์ก) ยุ่งที่สุด ออร์เดอร์ใหญ่ที่สุด หลังปิดร้าน (นิวยอร์กช่วงดึก) มีลูกค้าเดินเข้ามาแค่ไม่กี่คน คุณทำเงินได้มากที่สุดตอนร้านเต็ม
>
> **จุดที่เปรียบเทียบไม่ได้:** ช่วงคนเยอะของร้านอาหารรับประกันได้ด้วยเวลาอาหาร แต่ช่วงคึกคักของตลาดเป็นแค่ความน่าจะเป็น ไม่แน่นอน วันหยุดหรือวันที่ไม่มีข่าวอาจทำให้ "ช่วงยุ่ง" ว่างเปล่า

> [!walkthrough] ไล่ทีละขั้น: แปลงเวลาของ ICT เป็นนาฬิกาของคุณ
> 1. **CPI สหรัฐเดือนกรกฎาคม** (ฤดูร้อนสหรัฐ): 08:30 NY + 11 ชม. = **19:30 UTC+7**
> 2. **CPI สหรัฐเดือนมกราคม** (ฤดูหนาวสหรัฐ): 08:30 NY + 12 ชม. = **20:30 UTC+7**
> 3. **London killzone เดือนมกราคม:** 02:00–05:00 NY + 12 ชม. = **14:00–17:00 UTC+7**
> 4. **สัปดาห์ที่ไม่ตรงกัน 16 มีนาคม 2026:** สหรัฐเข้าเวลาฤดูร้อนแล้ว อังกฤษยัง NY AM killzone = 07:00 + 11 = **18:00–21:00 UTC+7** แต่ลอนดอนเปิด (08:00 GMT) = **15:00 UTC+7** คือสองชั่วโมงหลังเริ่ม London killzone
> 5. **แล้วไง?** เขียนช่วงเวลาเทรดของคุณทั้งเวลา NY และ UTC+7 และตั้งการแจ้งเตือนในปฏิทินสำหรับวันเปลี่ยนเวลาออมแสงทั้งสี่วันของแต่ละปี มาเร็วหรือช้าไปหนึ่งชั่วโมงหมายถึงเทรดช่วงที่เงียบของเซสชัน

> [!check]- เช็กความเข้าใจ: การแปลงเวลา
> **Q1.** ตอนนี้เดือนธันวาคม NY AM killzone เริ่มกี่โมง UTC+7?
> > [!answer]-
> > 07:00 NY + 12 ชม. = 19:00 UTC+7 (ฤดูหนาวสหรัฐ)
> **Q2.** ทำไมเทรดเดอร์ไทยและลาวจึงเห็น Killzone เลื่อน ทั้งที่ไทยและลาวไม่เคยเปลี่ยนนาฬิกา?
> > [!answer]-
> > เพราะนิวยอร์กและลอนดอนเปลี่ยน (เวลาออมแสง) ช่วงเวลาถูกกำหนดเป็นเวลา NY จึงเลื่อนเมื่อดูเป็น UTC+7
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: ทำไมการซื้อใต้ราคาเปิดรายวันจึงดีกว่าในวันขาขึ้น (GBP/USD ภาพประกอบ)
> ฤดูร้อนสหรัฐ ราคาเปิดรายวัน (เที่ยงคืน NY) อยู่ที่ **11:00 UTC+7**: **1.2650** Bias รายวัน: ขาขึ้น
> 1. **สะสม (เอเชีย):** กรอบแคบ 1.2640–1.2665
> 2. **วิ่งหลอก (London KZ ≈13:30 UTC+7):** ลงไปที่ **1.2628** ต่ำกว่าราคาเปิดรายวัน 22 pip กวาดจุดต่ำของเอเชีย: Judas swing
> 3. **จุดเข้า A (ใต้ราคาเปิด):** ซื้อที่ **1.2648** หลัง MSS Stop **1.2622** เป้าหมายจุดสูงของวันก่อน **1.2720** → เสี่ยง 26 pip ผลตอบแทน 72 pip → **2.77R**
> 4. **จุดเข้า B (ไล่ซื้อหลังนิวยอร์กเปิด):** ซื้อที่ **1.2690** Stop และเป้าหมายเดิม → เสี่ยง 68 pip ผลตอบแทน 30 pip → **0.44R**
> 5. **แล้วไง?** ในวันขาขึ้น ราคาที่ดีที่สุดมักมา **ก่อน** การวิ่งจริง ใต้ราคาเปิด การไล่ซื้อในช่วงนิวยอร์กหมายถึง Stop ไกลและเป้าหมายใกล้

> [!check]- เช็กความเข้าใจ: AMD
> **Q1.** Bias รายวันของคุณเป็นขาลง คุณควรหาจุด Short เหนือหรือใต้ราคาเปิดรายวัน?
> > [!answer]-
> > เหนือราคาเปิด ในวันขาลง Judas swing มักขึ้นก่อน (วิ่งหลอก) ราคา Short ที่ดีที่สุดจึงมักอยู่เหนือราคาเปิด
""")
L.before_callout("th", "example", """
**ช่วงของวันตามเวลา UTC+7** (ช่วงละ 6 ชั่วโมง เริ่ม 18:00 NY):

| ช่วง | เวลา NY | UTC+7 ฤดูร้อนสหรัฐ | UTC+7 ฤดูหนาวสหรัฐ |
|---|---|---|---|
| Q1 · เอเชีย | 18:00–00:00 | 05:00–11:00 | 06:00–12:00 |
| Q2 · ลอนดอน | 00:00–06:00 | 11:00–17:00 | 12:00–18:00 |
| Q3 · NY AM | 06:00–12:00 | 17:00–23:00 | 18:00–00:00 |
| Q4 · NY PM | 12:00–18:00 | 23:00–05:00 | 00:00–06:00 |

> [!check]- เช็กความเข้าใจ: ช่วงของวัน
> **Q1.** ตอนนี้เดือนสิงหาคม เวลา 20:00 ที่กรุงเทพฯ เป็นช่วงไหนของวันแบบ ICT?
> > [!answer]-
> > Q3 (NY AM): 17:00–23:00 UTC+7 ช่วงฤดูร้อนสหรัฐ
> **Q2.** ควรทำอะไรกับ Quarterly theory ก่อนนำไปเทรด?
> > [!answer]-
> > ทดสอบกับข้อมูลของคุณเอง (เฟส 9) เป็นส่วนที่พิสูจน์ได้น้อยที่สุดของ ICT ให้ถือเป็นสมมติฐาน ไม่ใช่กฎ
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** Killzone ออกแบบมาสำหรับ FX ช่วงลอนดอนและ NY AM คือช่วงที่ราคาวิ่งส่วนใหญ่ของวัน *(ดู 0.3)*
> - **ทองคำ:** ช่วงเวลาเดียวกัน บวกการประมูล LBMA เวลา 16:30 และ 21:00 UTC+7 ช่วงฤดูร้อนซีกโลกเหนือ *(ดู 0.4)*
> - **หุ้นและฟิวเจอร์สดัชนี:** ช่วงซื้อขายปกติ 20:30–03:00 UTC+7 (ฤดูร้อน) NY AM killzone ครอบคลุมข้อมูลสหรัฐและการเปิดตลาด *(ดู 0.5)*
> - **คริปโต:** 24/7 แต่ปริมาณยังกระจุกในชั่วโมงลอนดอนและนิวยอร์ก แท่งรายวันปิด 07:00 UTC+7 (00:00 UTC) ไม่ใช่เที่ยงคืน NY *(ดู 0.7)*

> [!caution]
> NY AM killzone มีการประกาศข้อมูลสหรัฐเวลา 19:30/20:30 UTC+7 อยู่ข้างใน ระดับที่ดูสมบูรณ์แบบอาจถูกทะลุในไม่กี่วินาที และ Slippage เลย Stop ของคุณ เช็กปฏิทินทุกเช้า และอย่าถือ Setup ใหม่เข้าไปในข่าวธงแดง *(ดู 0.8)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** เติมเวลา UTC+7 ของ London killzone และ NY AM killzone ทั้งฤดูร้อนและฤดูหนาวของสหรัฐ
> > [!answer]-
> > ฤดูร้อน: London 13:00–16:00, NY AM 18:00–21:00 ฤดูหนาว: London 14:00–17:00, NY AM 19:00–22:00
> **Q2.** ส่วนไหนของบทเรียนนี้มีข้อมูลรองรับดี และส่วนไหนไม่มี?
> > [!answer]-
> > รองรับดี: ปริมาณและความผันผวนกระจุกรอบการเปิดเซสชันและการประกาศข้อมูล (วัดเองได้) รองรับน้อย: Quarterly theory และจังหวะ AMD ที่ตรงเป๊ะทุกวัน
""")

L.set_meta("level", "v2")
L.save()
