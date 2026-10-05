"""B9b · v2 upgrade of 2.6 Multi-Timeframe Structure (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("02 Market Structure/2.6 Multi-Timeframe Structure.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Every big move on a slow chart is made of many small moves on a fast chart. A dip on the daily chart looks like a full downtrend on the 1-hour chart. Use the slow chart to decide which way to trade and where; then watch the fast chart for the moment that small downtrend turns back up. That moment is your entry.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **HTF / MTF / LTF** — higher / middle / lower timeframe *(see 1.5)*.
> - **Nested structure** — a complete LTF trend inside each HTF leg.
> - **Bias** — the direction you're allowed to trade, set by the HTF.
> - **HTF zone** — an HTF level: protected HL, S/R or demand/supply *(see 2.3–2.5)*.
> - **CHoCH (change of character)** — the first close beyond the swing that protected the trend *(see 2.3)*.
> - **BOS (break of structure)** — a close beyond a swing in the trend direction *(see 2.3)*.
> - **Alignment** — HTF and LTF pointing the same way.
> - **Trailing a stop** — moving the stop behind new swing lows (in a long) as the trade progresses.
""")
L.before_heading("en", "2.", """
> [!analogy]
> Structure is like **Russian nesting dolls**: open the big doll (a daily pullback) and there's a complete smaller doll inside (a 1H downtrend), and another inside that. Each doll has the same shape at a smaller size.
>
> **Where it breaks:** the dolls never change. A market's small doll can grow into a big one: a 1H move against the daily trend can sometimes become a daily trend change, which is why the HTF protected low still matters.

> [!check]- Check your understanding: nesting
> **Q1.** The daily chart is pulling back in an uptrend. What does the 1H chart usually show at that time?
> > [!answer]-
> > A small downtrend: LH + LL. The 1H downtrend **is** the daily pullback.
""")
L.before_heading("en", "3.", """
> [!check]- Check your understanding: the three jobs
> **Q1.** Match each job to a timeframe: trigger, direction, location.
> > [!answer]-
> > Direction → HTF (e.g. daily). Location → MTF (e.g. 4H zone). Trigger → LTF (e.g. 1H CHoCH in the HTF direction).
""")
L.before_heading("en", "4.", """
> [!check]- Check your understanding: alignment
> **Q1.** Daily uptrend. On 1H, price breaks below the last HL (a 1H CHoCH **down**) while still far above any daily zone. Short it?
> > [!answer]-
> > No. That's the start of the daily pullback, against the HTF direction. Wait for price to reach a daily zone and look for a 1H CHoCH **up**.
""")
L.before_callout("en", "action", """
![[p2-mtf-vs-daily.en.svg]]

> [!walkthrough] Step by step: what the 1H trigger adds
> The trade from the example: daily demand **121.5–124**, target the daily high **131**, risk **100 USD**.
> 1. **Daily candle only:** wait for a bullish daily close off the zone, e.g. **126.5**; stop **121.3** → risk 5.2, reward 4.5 → **0.9R**; size ≈ **19 units**, +87 USD at target.
> 2. **1H CHoCH, buy the HL:** entry **124.0**, same stop **121.3** → risk 2.7, reward 7.0 → **2.6R**; size ≈ **37 units**, +259 USD at target.
> 3. Same daily idea, about **3×** the R:R and the same 100 USD at risk.
> 4. **So what?** The HTF gives a reason to trade; the LTF gives a cheaper entry. Don't then widen the stop back to the HTF, because that breaks your sizing.

> [!market]
> - **Forex:** Daily → 4H → 1H works well; avoid LTF triggers in the quiet hours after 04:00 UTC+7 *(see 0.3)*.
> - **Gold:** fast LTF moves around US data can fake a CHoCH; wait for the candle to close *(see 0.4)*.
> - **Stocks:** use the opening hour carefully: LTF structure is noisy right after the open *(see 0.5)*.
> - **Crypto:** 24/7 charts mean the LTF keeps moving while you sleep; set alerts at HTF zones instead of watching *(see 0.7)*.

> [!caution]
> Tight LTF stops make larger positions possible. One slippage or news spike can then cost more than 1R. Size from the LTF stop distance, but keep the account risk at your normal 1% or less.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** List the 7 steps of the MTF entry model in order (short names are fine).
> > [!answer]-
> > HTF bias → HTF location → LTF pullback structure → LTF CHoCH → entry (new HL or retest) → stop below the CHoCH low → target the HTF swing high, then trail.
> **Q2.** Daily demand 88–90, target 98. A 1H CHoCH gives an entry at 90.2 with a stop at 87.6. What's the R:R?
> > [!answer]-
> > Risk 2.6, reward 7.8 → **3R**.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> การขยับใหญ่ทุกครั้งบนกราฟช้าประกอบด้วยการขยับเล็ก ๆ หลายครั้งบนกราฟเร็ว การย่อบนกราฟรายวันจะดูเหมือนขาลงเต็มรูปแบบบนกราฟ 1 ชั่วโมง ใช้กราฟช้าตัดสินว่าจะเทรดทางไหนและที่ไหน แล้วดูกราฟเร็วรอจังหวะที่ขาลงเล็ก ๆ นั้นกลับขึ้น จังหวะนั้นคือจุดเข้าของคุณ
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **HTF / MTF / LTF** — ไทม์เฟรมใหญ่ / กลาง / เล็ก *(ดู 1.5)*
> - **โครงสร้างซ้อนกัน (Nested structure)** — เทรนด์ LTF ที่ครบสมบูรณ์อยู่ภายในแต่ละขาของ HTF
> - **ทิศทางที่เลือก (Bias)** — ทิศทางที่อนุญาตให้เทรด กำหนดโดย HTF
> - **โซน HTF (HTF zone)** — ระดับราคาบน HTF: Protected HL, แนวรับแนวต้าน หรือ Demand/Supply *(ดู 2.3–2.5)*
> - **CHoCH (Change of character)** — การปิดครั้งแรกเลยสวิงที่ปกป้องเทรนด์ *(ดู 2.3)*
> - **BOS (Break of structure)** — การปิดเลยสวิงในทิศทางเทรนด์ *(ดู 2.3)*
> - **ความสอดคล้อง (Alignment)** — HTF และ LTF ชี้ไปทางเดียวกัน
> - **เลื่อน Stop ตาม (Trailing a stop)** — เลื่อน Stop ตามจุดสวิงต่ำใหม่ (ในไม้ซื้อ) ขณะที่เทรดไปได้ดี
""")
L.before_heading("th", "2.", """
> [!analogy]
> โครงสร้างเหมือน **ตุ๊กตาแม่ลูกดก (Matryoshka)**: เปิดตุ๊กตาตัวใหญ่ (การย่อรายวัน) จะเจอตุ๊กตาตัวเล็กที่ครบสมบูรณ์อยู่ข้างใน (ขาลงบน 1H) และมีอีกตัวข้างในนั้น ทุกตัวรูปร่างเหมือนกันแต่ขนาดเล็กลง
>
> **จุดที่เปรียบเทียบไม่ได้:** ตุ๊กตาไม่เคยเปลี่ยน แต่ตุ๊กตาตัวเล็กของตลาดโตเป็นตัวใหญ่ได้: การขยับบน 1H ที่สวนเทรนด์รายวันบางครั้งกลายเป็นการเปลี่ยนเทรนด์รายวัน นี่คือเหตุผลที่ Protected low ของ HTF ยังสำคัญ

> [!check]- เช็กความเข้าใจ: โครงสร้างซ้อนกัน
> **Q1.** กราฟรายวันกำลังย่อตัวในขาขึ้น กราฟ 1H มักแสดงอะไรในตอนนั้น?
> > [!answer]-
> > ขาลงเล็ก ๆ: LH + LL ขาลงบน 1H **คือ** การย่อของกราฟรายวัน
""")
L.before_heading("th", "3.", """
> [!check]- เช็กความเข้าใจ: หน้าที่ 3 อย่าง
> **Q1.** จับคู่หน้าที่กับไทม์เฟรม: จังหวะเข้า ทิศทาง ตำแหน่ง
> > [!answer]-
> > ทิศทาง → HTF (เช่น รายวัน) ตำแหน่ง → MTF (เช่น โซนบน 4H) จังหวะเข้า → LTF (เช่น CHoCH บน 1H ในทิศทาง HTF)
""")
L.before_heading("th", "4.", """
> [!check]- เช็กความเข้าใจ: ความสอดคล้อง
> **Q1.** รายวันเป็นขาขึ้น บน 1H ราคาหลุด HL ล่าสุด (CHoCH **ลง** บน 1H) ขณะที่ยังอยู่ห่างจากโซนรายวันมาก ควร Short ไหม?
> > [!answer]-
> > ไม่ควร นั่นคือจุดเริ่มของการย่อรายวัน ซึ่งสวนทิศทาง HTF รอให้ราคาถึงโซนรายวัน แล้วมองหา CHoCH **ขึ้น** บน 1H
""")
L.before_callout("th", "action", """
![[p2-mtf-vs-daily.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: สัญญาณบน 1H เพิ่มอะไรให้
> เทรดจากตัวอย่าง: Demand รายวัน **121.5–124** เป้าจุดสูงรายวัน **131** เสี่ยง **100 ดอลลาร์**
> 1. **แท่งรายวันอย่างเดียว:** รอแท่งรายวันปิดเขียวเด้งจากโซน เช่น **126.5** Stop **121.3** → เสี่ยง 5.2 ผลตอบแทน 4.5 → **0.9R** ขนาด ≈ **19 หน่วย** ถึงเป้าได้ +87 ดอลลาร์
> 2. **CHoCH บน 1H ซื้อที่ HL:** เข้า **124.0** Stop เดิม **121.3** → เสี่ยง 2.7 ผลตอบแทน 7.0 → **2.6R** ขนาด ≈ **37 หน่วย** ถึงเป้าได้ +259 ดอลลาร์
> 3. ไอเดียรายวันเดียวกัน R:R ราว **3 เท่า** ด้วยเงินเสี่ยง 100 ดอลลาร์เท่าเดิม
> 4. **แล้วไง?** HTF ให้เหตุผลในการเทรด LTF ให้จุดเข้าที่ถูกกว่า อย่าขยาย Stop กลับไปที่ HTF ภายหลัง เพราะจะทำให้การคำนวณขนาดพัง

> [!market]
> - **ฟอเร็กซ์:** Daily → 4H → 1H ใช้ได้ดี หลีกเลี่ยงสัญญาณ LTF ในชั่วโมงเงียบหลัง 04:00 UTC+7 *(ดู 0.3)*
> - **ทองคำ:** การขยับเร็วบน LTF ช่วงข้อมูลสหรัฐอาจสร้าง CHoCH หลอก รอให้แท่งปิด *(ดู 0.4)*
> - **หุ้น:** ระวังชั่วโมงแรกหลังเปิดตลาด: โครงสร้าง LTF มีสัญญาณรบกวนมากทันทีหลังเปิด *(ดู 0.5)*
> - **คริปโต:** กราฟ 24/7 หมายความว่า LTF ขยับต่อขณะที่คุณหลับ ตั้งการแจ้งเตือนที่โซน HTF แทนการนั่งเฝ้า *(ดู 0.7)*

> [!caution]
> Stop ที่แคบบน LTF ทำให้เปิดโพซิชันใหญ่ขึ้นได้ Slippage หรือการพุ่งของข่าวครั้งเดียวอาจเสียมากกว่า 1R คำนวณขนาดจากระยะ Stop บน LTF แต่รักษาความเสี่ยงของบัญชีไว้ที่ 1% ตามปกติหรือน้อยกว่า
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอก 7 ขั้นของโมเดลการเข้าแบบหลายไทม์เฟรมตามลำดับ (ชื่อสั้น ๆ ก็ได้)
> > [!answer]-
> > ทิศทาง HTF → ตำแหน่ง HTF → โครงสร้างการย่อบน LTF → CHoCH บน LTF → เข้า (HL ใหม่หรือการทดสอบซ้ำ) → Stop ใต้จุดต่ำที่สร้าง CHoCH → เป้าจุดสวิงสูงของ HTF แล้วเลื่อน Stop ตาม
> **Q2.** Demand รายวัน 88–90 เป้า 98 CHoCH บน 1H ให้จุดเข้าที่ 90.2 Stop ที่ 87.6 R:R เท่าไร?
> > [!answer]-
> > เสี่ยง 2.6 ผลตอบแทน 7.8 → **3R**
""")

L.set_meta("level", "v2")
L.save()
