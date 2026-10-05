"""B6 · v2 upgrade of 7.2 Volume Profile: POC, VAH, VAL (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("07 Orderflow & Auction Market Theory/7.2 Volume Profile- POC, VAH, VAL.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> A normal chart tells you **when** trading happened. A volume profile turns it sideways and tells you **at which prices** trading happened, as a bar for each price. Long bars are prices where buyers and sellers happily traded a lot (the market liked that price). Short bars are prices the market rushed through. When price comes back later, it tends to slow down at the long bars and speed through the short ones.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Volume profile** — a sideways histogram of how much volume traded at each price over a chosen period.
> - **POC (point of control)** — the single price with the most volume.
> - **Value area (VA)** — the price range around the POC that holds about **70%** of the volume.
> - **VAH / VAL (value area high / low)** — the top and bottom of the value area.
> - **HVN / LVN (high- / low-volume node)** — a thick part of the profile (lots of trading) / a thin part (little trading).
> - **Session profile / composite profile** — a profile of one day / of many days combined.
> - **D, P, b shapes** — balanced day / rally then acceptance at the top / drop then acceptance at the bottom.
> - **Double distribution** — two separate value areas in one session (a trend day), with an LVN between them.
> - **Short covering / long liquidation** — shorts buying back to exit / longs selling to exit.
> - **80% rule** — market-profile folklore: if price re-enters yesterday's value and holds, it often crosses to the other side. Untested folklore until you test it.
> - **6E** — euro FX futures on CME, used for real volume on EUR/USD.
""")
L.before_heading("en", "2.", """
![[p7-profile-by-hand.en.svg]]

> [!walkthrough] Step by step: build a profile by hand from 10 candles
> Price rows are whole numbers from 100 to 109. Each candle's volume is shared equally across the rows it touched.
> 1. **Candle 1** traded 100–103 (4 rows) with 400 → **100 per row**. Candle 4 traded 104–106 (3 rows) with 900 → **300 per row**. Do the same for all 10 candles (left side of the figure).
> 2. **Add up each row:** 100 → 100, 101 → 100, 102 → 250, 103 → 650, 104 → 1,250, **105 → 1,550**, 106 → 1,000, 107 → 600, 108 → 200, 109 → 100. Total **5,800**.
> 3. **POC** = the biggest row = **105** (1,550).
> 4. **HVN** = the thick block **104–106**. **LVNs** = thin rows at **100–101** and **108–109**.
> 5. **So what?** You've turned 10 candles into a map of where the market agreed (104–106) and where it barely traded (the edges). That map is what the profile tool draws automatically.

> [!walkthrough] Step by step: the 70% value area, one row at a time
> Target: 70% of 5,800 = **4,060**.
> 1. Start at the **POC 105**: 1,550 (26.7% of the total).
> 2. Compare the next row up (106: 1,000) and down (104: 1,250). Add the bigger → **104**: total **2,800** (48.3%).
> 3. Compare 106 (1,000) and 103 (650). Add **106**: total **3,800** (65.5%). Still below 4,060.
> 4. Compare 107 (600) and 103 (650). Add **103**: total **4,450** (76.7%) ≥ 4,060 → stop.
> 5. **Value area = 103–106**: **VAL 103**, **VAH 106**.
> 6. **So what?** Profile tools do exactly this (some add two rows at a time, so results can differ slightly). Knowing the rule tells you why VAH/VAL sit where they do.

> [!analogy]
> A volume profile is like the **footpath worn into a lawn**. Where people walk every day, the grass is gone (HVN: lots of trading). Where almost nobody walks, the grass is tall (LVN). Newcomers naturally follow the worn path, and cross the tall grass quickly.
>
> **Where it breaks:** a footpath stays where it is for years. Value moves: when new information arrives, the market wears a new path somewhere else (imbalance, *see 7.1*).

> [!check]- Check your understanding: POC and value area
> **Q1.** Rows: 50 → 200, 51 → 600, 52 → 900, 53 → 500, 54 → 100 (total 2,300). Where is the POC and what is the value area?
> > [!answer]-
> > POC = 52 (900). 70% of 2,300 = 1,610. Start 900; add 51 (600) → 1,500; add 53 (500) → 2,000 ≥ 1,610. Value area 51–53.
""")
L.before_heading("en", "3.", """
> [!check]- Check your understanding: profile shapes
> **Q1.** A session rallies hard in the morning, then trades sideways at the top all afternoon. What shape is the profile, and what is a common cause?
> > [!answer]-
> > A P shape: a fast rally, then acceptance at the top. Often short covering.
""")
L.before_callout("en", "action", """
> [!check]- Check your understanding: trading value
> **Q1.** Yesterday's value area was 102.5–106.2. Today opens at 107.0 and stays above 106.2 for two hours on strong volume. What does that suggest?
> > [!answer]-
> > Initiative buying and value moving higher (imbalance). Yesterday's VAH (106.2) becomes likely support; fading back to the POC is the wrong tool.

> [!market]
> - **Forex:** spot FX has no central volume. Use currency futures (6E for EUR/USD, 6J for USD/JPY) or treat broker tick volume as rough *(see 0.3)*.
> - **Gold:** use COMEX gold futures (GC, MGC) for real volume profiles *(see 0.4)*.
> - **Stocks & indices:** real exchange volume; session profiles of the regular session work best *(see 0.5)*.
> - **Crypto:** each exchange has its own volume; use the largest venue or an aggregated feed, and note that profiles never "close" for the night *(see 0.7)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Define POC, VAH, VAL, HVN and LVN in one line each.
> > [!answer]-
> > POC: the price with the most volume. VAH/VAL: the top/bottom of the range holding ~70% of volume. HVN: a thick part of the profile where price slows. LVN: a thin part where price moves fast.
> **Q2.** Why are LVNs good places for stops **beyond**, but bad places to wait for a reaction?
> > [!answer]-
> > Little trading happened there, so few participants defend those prices; price tends to move through them quickly rather than stop.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> กราฟปกติบอกว่าการซื้อขายเกิด **เมื่อไหร่** Volume profile พลิกกราฟตะแคงแล้วบอกว่าการซื้อขายเกิด **ที่ราคาไหน** เป็นแท่งสำหรับแต่ละราคา แท่งยาวคือราคาที่ผู้ซื้อผู้ขายซื้อขายกันมาก (ตลาดชอบราคานั้น) แท่งสั้นคือราคาที่ตลาดวิ่งผ่านไปอย่างรวดเร็ว เมื่อราคากลับมาทีหลัง มักชะลอที่แท่งยาวและวิ่งผ่านแท่งสั้น
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **Volume profile** — ฮิสโตแกรมแนวนอนที่บอกว่าแต่ละราคามีวอลุ่มซื้อขายเท่าไหร่ในช่วงที่เลือก
> - **POC (Point of control)** — ราคาเดียวที่มีวอลุ่มมากที่สุด
> - **Value area (VA)** — ช่วงราคารอบ POC ที่รวมวอลุ่มราว **70%**
> - **VAH / VAL (Value area high / low)** — ขอบบนและขอบล่างของ Value area
> - **HVN / LVN (High- / Low-volume node)** — ส่วนที่หนาของ Profile (ซื้อขายเยอะ) / ส่วนที่บาง (ซื้อขายน้อย)
> - **Session profile / Composite profile** — Profile ของหนึ่งวัน / ของหลายวันรวมกัน
> - **รูปทรง D, P, b** — วันสมดุล / ขึ้นแล้วยอมรับที่ด้านบน / ลงแล้วยอมรับที่ด้านล่าง
> - **Double distribution** — Value area สองชุดแยกกันในเซสชันเดียว (วันที่มีเทรนด์) มี LVN คั่นกลาง
> - **Short covering / Long liquidation** — Short ซื้อคืนเพื่อออก / Long ขายเพื่อออก
> - **กฎ 80% (80% rule)** — ความเชื่อของสาย Market profile: ถ้าราคากลับเข้ามูลค่าของเมื่อวานและยืนได้ มักวิ่งไปถึงอีกฝั่ง ยังเป็นแค่ความเชื่อจนกว่าคุณจะทดสอบ
> - **6E** — ฟิวเจอร์สค่าเงินยูโรบน CME ใช้ดูวอลุ่มจริงของ EUR/USD
""")
L.before_heading("th", "2.", """
![[p7-profile-by-hand.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: สร้าง Profile ด้วยมือจาก 10 แท่งเทียน
> แถวราคาเป็นจำนวนเต็มจาก 100 ถึง 109 วอลุ่มของแต่ละแท่งถูกแบ่งเท่า ๆ กันในแถวที่แท่งนั้นแตะ
> 1. **แท่ง 1** ซื้อขาย 100–103 (4 แถว) วอลุ่ม 400 → **แถวละ 100** แท่ง 4 ซื้อขาย 104–106 (3 แถว) วอลุ่ม 900 → **แถวละ 300** ทำแบบเดียวกันทั้ง 10 แท่ง (ด้านซ้ายของภาพ)
> 2. **รวมแต่ละแถว:** 100 → 100, 101 → 100, 102 → 250, 103 → 650, 104 → 1,250, **105 → 1,550**, 106 → 1,000, 107 → 600, 108 → 200, 109 → 100 รวม **5,800**
> 3. **POC** = แถวที่ใหญ่ที่สุด = **105** (1,550)
> 4. **HVN** = ก้อนหนา **104–106** **LVN** = แถวบางที่ **100–101** และ **108–109**
> 5. **แล้วไง?** คุณเปลี่ยน 10 แท่งเทียนให้เป็นแผนที่ว่าตลาดตกลงกันที่ไหน (104–106) และแทบไม่ซื้อขายที่ไหน (ขอบ) แผนที่นี้คือสิ่งที่เครื่องมือ Profile วาดให้อัตโนมัติ

> [!walkthrough] ไล่ทีละขั้น: Value area 70% ทีละแถว
> เป้า: 70% ของ 5,800 = **4,060**
> 1. เริ่มที่ **POC 105**: 1,550 (26.7% ของทั้งหมด)
> 2. เทียบแถวถัดขึ้น (106: 1,000) กับถัดลง (104: 1,250) เพิ่มอันที่ใหญ่กว่า → **104**: รวม **2,800** (48.3%)
> 3. เทียบ 106 (1,000) กับ 103 (650) เพิ่ม **106**: รวม **3,800** (65.5%) ยังไม่ถึง 4,060
> 4. เทียบ 107 (600) กับ 103 (650) เพิ่ม **103**: รวม **4,450** (76.7%) ≥ 4,060 → หยุด
> 5. **Value area = 103–106**: **VAL 103** **VAH 106**
> 6. **แล้วไง?** เครื่องมือ Profile ทำแบบนี้เป๊ะ (บางตัวเพิ่มทีละสองแถว ผลจึงต่างกันเล็กน้อย) การรู้กฎทำให้คุณรู้ว่าทำไม VAH/VAL จึงอยู่ตรงนั้น

> [!analogy]
> Volume profile เหมือน **ทางเดินที่ถูกเหยียบจนเป็นรอยบนสนามหญ้า** ที่ที่คนเดินทุกวัน หญ้าหายไป (HVN: ซื้อขายเยอะ) ที่ที่แทบไม่มีใครเดิน หญ้าสูง (LVN) คนที่มาใหม่จะเดินตามทางที่เป็นรอยโดยธรรมชาติ และเดินผ่านหญ้าสูงอย่างรวดเร็ว
>
> **จุดที่เปรียบเทียบไม่ได้:** ทางเดินบนสนามหญ้าอยู่ที่เดิมเป็นปี แต่มูลค่าย้ายได้ เมื่อมีข้อมูลใหม่ ตลาดจะเหยียบทางใหม่ที่อื่น (ไม่สมดุล *ดู 7.1*)

> [!check]- เช็กความเข้าใจ: POC และ Value area
> **Q1.** แถว: 50 → 200, 51 → 600, 52 → 900, 53 → 500, 54 → 100 (รวม 2,300) POC อยู่ที่ไหน และ Value area คืออะไร?
> > [!answer]-
> > POC = 52 (900) 70% ของ 2,300 = 1,610 เริ่ม 900 เพิ่ม 51 (600) → 1,500 เพิ่ม 53 (500) → 2,000 ≥ 1,610  Value area 51–53
""")
L.before_heading("th", "3.", """
> [!check]- เช็กความเข้าใจ: รูปทรงของ Profile
> **Q1.** เซสชันหนึ่งขึ้นแรงตอนเช้า แล้วซื้อขายออกข้างที่ด้านบนทั้งบ่าย Profile เป็นรูปทรงอะไร และสาเหตุที่พบบ่อยคืออะไร?
> > [!answer]-
> > รูป P: ขึ้นเร็วแล้วยอมรับที่ด้านบน มักเกิดจาก Short covering
""")
L.before_callout("th", "action", """
> [!check]- เช็กความเข้าใจ: เทรดตามมูลค่า
> **Q1.** Value area ของเมื่อวานคือ 102.5–106.2 วันนี้เปิดที่ 107.0 และอยู่เหนือ 106.2 สองชั่วโมงด้วยวอลุ่มแรง หมายความว่าอะไร?
> > [!answer]-
> > การซื้อแบบริเริ่มและมูลค่ากำลังย้ายขึ้น (ไม่สมดุล) VAH ของเมื่อวาน (106.2) น่าจะกลายเป็นแนวรับ การเทรดสวนกลับไปหา POC เป็นเครื่องมือที่ผิด

> [!market]
> - **ฟอเร็กซ์:** ฟอเร็กซ์ Spot ไม่มีวอลุ่มกลาง ใช้ฟิวเจอร์สค่าเงิน (6E สำหรับ EUR/USD, 6J สำหรับ USD/JPY) หรือถือ Tick volume ของโบรกเกอร์เป็นแค่ค่าคร่าว ๆ *(ดู 0.3)*
> - **ทองคำ:** ใช้ฟิวเจอร์สทอง COMEX (GC, MGC) สำหรับ Volume profile จริง *(ดู 0.4)*
> - **หุ้นและดัชนี:** วอลุ่มจริงจากตลาด Session profile ของช่วงซื้อขายปกติใช้ได้ดีที่สุด *(ดู 0.5)*
> - **คริปโต:** แต่ละกระดานมีวอลุ่มของตัวเอง ใช้กระดานที่ใหญ่ที่สุดหรือข้อมูลรวม และ Profile ไม่เคย "ปิด" ตอนกลางคืน *(ดู 0.7)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** นิยาม POC, VAH, VAL, HVN และ LVN ข้อละบรรทัด
> > [!answer]-
> > POC: ราคาที่มีวอลุ่มมากที่สุด VAH/VAL: ขอบบน/ล่างของช่วงที่รวมวอลุ่มราว 70% HVN: ส่วนหนาของ Profile ที่ราคาชะลอ LVN: ส่วนบางที่ราคาวิ่งเร็ว
> **Q2.** ทำไม LVN จึงเหมาะวาง Stop **เลยออกไป** แต่ไม่เหมาะรอการตอบสนอง?
> > [!answer]-
> > เพราะซื้อขายตรงนั้นน้อย คนที่จะป้องกันราคาเหล่านั้นจึงมีน้อย ราคามักวิ่งผ่านเร็วมากกว่าจะหยุด
""")

L.set_meta("level", "v2")
L.save()
