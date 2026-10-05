"""B6 · v2 upgrade of 7.5 Liquidity Heatmaps (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("07 Orderflow & Auction Market Theory/7.5 Liquidity Heatmaps.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> A heatmap is a picture of the order book over time. Each price is a row, time runs left to right, and the colour shows how many orders were waiting at that price: dark means few, bright means many. A long bright line is a big order that sat there for a while. When price arrives, three things can happen: the big order trades and holds price (real), it gets eaten and price breaks through (overpowered), or it simply disappears (it was never meant to trade).
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Liquidity heatmap** — a chart of resting limit orders at every price over time.
> - **Brightness / colour** — how much size was resting at that price at that moment (dark = little, bright = a lot; most tools use blue → yellow → white).
> - **Resting liquidity** — limit orders waiting in the book *(see 7.3)*.
> - **Wall / band** — a bright horizontal line: a large order sitting at one price.
> - **Absorbing (holding)** — the wall trades a lot and stays: real liquidity defending the level.
> - **Eaten** — the wall shrinks because aggressive trades fill it, then price breaks through.
> - **Pulled** — the wall disappears without trading.
> - **Liquidity migration** — bands being moved up or down with price.
> - **Bubbles** — markers for large **executed** trades on many heatmap tools.
> - **Magnet** — a large resting band that price tends to travel toward *(see 5.1)*.
""")
L.before_heading("en", "2.", """
![[p7-heatmap-frames.en.svg]]

> [!walkthrough] Step by step: the same wall, two endings (ES, illustrative)
> A bright band of **1,800** contracts bid at **4,998.00** has been on the heatmap for 40 minutes. Price is falling toward it.
> 1. **Scenario A (absorbing):** price reaches 4,998.00. Bubbles appear: **1,600** contracts trade there. The band stays bright (it refills). Price stops and turns up → real buyer, **absorption** (7.6).
> 2. **Scenario B (pulling):** as price gets two ticks away, the band fades to nothing. **No** bubbles print at 4,998.00. Price falls straight to **4,995.00** (12 ticks).
> 3. **The trap:** a trader bought at **4,998.25** "in front of the wall" with a stop at **4,997.75** (2 ticks = 0.5 points = **25 USD** per ES contract). In scenario B the fast drop fills the stop at about **4,997.00**: a loss of 1.25 points = **62.50 USD**, 2.5 times the plan.
> 4. **So what?** The heatmap looked identical until price arrived. Decide only after you see whether the band **trades and holds**, gets **eaten**, or is **pulled**.

> [!analogy]
> A heatmap is like a **crowd map at a concert**. Bright spots show where lots of people are standing right now. A huge bright spot near the stage suggests a strong crowd that won't move easily. But people can walk away in seconds, and a spot that looked solid can be empty when you get there.
>
> **Where it breaks:** concert-goers don't usually pretend to stand somewhere. In markets, some large orders are placed only to be seen and are cancelled before anyone reaches them (spoofing, 7.3).

> [!check]- Check your understanding: reading the map
> **Q1.** A bright band ends abruptly just before price reaches it, and no large trades print. What happened?
> > [!answer]-
> > The order was pulled (cancelled). There was no real support there.
> **Q2.** What do the bubbles show that the bright bands don't?
> > [!answer]-
> > Real executed trades (aggression). Bands only show intentions that can be cancelled.
""")
L.before_callout("en", "example", """
> [!check]- Check your understanding: eaten vs pulled
> **Q1.** A band at 62,500 shrinks steadily while big buy bubbles hit it, then price breaks through. Eaten or pulled, and what does it suggest?
> > [!answer]-
> > Eaten: aggressive buyers filled the resting sellers. It suggests strong initiative buying and a likely continuation.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex & gold CFDs:** no central book, so no meaningful heatmap; use CME futures (6E, GC) *(see 7.3)*.
> - **Stocks & indices:** index futures (ES, NQ) give the most reliable heatmaps.
> - **Crypto:** heatmaps are popular and widely available, but each exchange shows only its own book; the same participant can show orders on several exchanges at once *(see 0.7)*.

> [!caution]
> Heatmaps are hypnotic and full of orders that will never trade. Watching them all day leads to overtrading and to trusting walls that vanish. Use them only at levels you already marked from structure or the volume profile, and always confirm with executed volume (bubbles, footprint) before risking money.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Name the three possible fates of a bright band when price reaches it, and what each means.
> > [!answer]-
> > Holds (trades a lot, stays): real absorbing liquidity. Eaten (shrinks under aggressive trades, then breaks): initiative wins. Pulled (vanishes without trades): fake or nervous liquidity, no support.
> **Q2.** Why are large resting bands often useful as **targets** rather than entries?
> > [!answer]-
> > Price tends to be drawn to large liquidity (big participants need it to fill), but you can't know in advance whether the band will hold, so it's safer as a place to take profit than as a place to rely on for support.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> Heatmap คือภาพของสมุดคำสั่งตามเวลา แต่ละราคาคือหนึ่งแถว เวลาวิ่งจากซ้ายไปขวา และสีบอกว่ามีคำสั่งรออยู่ที่ราคานั้นมากแค่ไหน: มืด = น้อย สว่าง = มาก เส้นสว่างยาว ๆ คือคำสั่งใหญ่ที่รออยู่ตรงนั้นนาน เมื่อราคามาถึง เกิดได้สามแบบ: คำสั่งใหญ่ถูกซื้อขายและยันราคาไว้ (ของจริง) ถูกกินจนราคาทะลุผ่าน (สู้ไม่ไหว) หรือหายไปเฉย ๆ (ไม่เคยตั้งใจให้ซื้อขายเลย)
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **Liquidity heatmap** — กราฟของคำสั่ง Limit ที่รออยู่ในทุกราคาตามเวลา
> - **ความสว่าง / สี** — มีขนาดคำสั่งรออยู่ที่ราคานั้นในขณะนั้นเท่าไหร่ (มืด = น้อย สว่าง = มาก เครื่องมือส่วนใหญ่ใช้ น้ำเงิน → เหลือง → ขาว)
> - **สภาพคล่องที่รออยู่ (Resting liquidity)** — คำสั่ง Limit ที่รออยู่ในสมุด *(ดู 7.3)*
> - **กำแพง / แถบ (Wall / Band)** — เส้นแนวนอนที่สว่าง: คำสั่งใหญ่ที่อยู่ที่ราคาเดียว
> - **ดูดซับ / ยืนได้ (Absorbing / Holding)** — กำแพงถูกซื้อขายมากและยังอยู่: สภาพคล่องจริงที่ป้องกันระดับ
> - **ถูกกิน (Eaten)** — กำแพงหดลงเพราะการซื้อขายเชิงรุกเติมมัน แล้วราคาทะลุผ่าน
> - **ถูกถอน (Pulled)** — กำแพงหายไปโดยไม่มีการซื้อขาย
> - **การย้ายสภาพคล่อง (Liquidity migration)** — แถบถูกย้ายขึ้นหรือลงตามราคา
> - **ฟอง (Bubbles)** — เครื่องหมายแสดงการซื้อขายขนาดใหญ่ที่ **เกิดขึ้นจริง** บนเครื่องมือ Heatmap หลายตัว
> - **แม่เหล็ก (Magnet)** — แถบที่รออยู่ขนาดใหญ่ที่ราคามักเดินทางไปหา *(ดู 5.1)*
""")
L.before_heading("th", "2.", """
![[p7-heatmap-frames.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: กำแพงเดียวกัน สองตอนจบ (ES ภาพประกอบ)
> แถบสว่าง **1,800** สัญญาฝั่ง Bid ที่ **4,998.00** อยู่บน Heatmap มา 40 นาที ราคากำลังลงไปหา
> 1. **สถานการณ์ A (ดูดซับ):** ราคาถึง 4,998.00 มีฟองปรากฏ: ซื้อขาย **1,600** สัญญาตรงนั้น แถบยังสว่าง (เติมใหม่) ราคาหยุดและกลับขึ้น → ผู้ซื้อจริง **Absorption** (7.6)
> 2. **สถานการณ์ B (ถอน):** ตอนราคาห่างสอง tick แถบจางหายไป **ไม่มี** ฟองที่ 4,998.00 ราคาร่วงตรงไปที่ **4,995.00** (12 tick)
> 3. **กับดัก:** เทรดเดอร์ซื้อที่ **4,998.25** "หน้ากำแพง" Stop ที่ **4,997.75** (2 tick = 0.5 จุด = **25 ดอลลาร์** ต่อสัญญา ES) ในสถานการณ์ B การร่วงเร็วทำให้ Stop ได้ราคาราว **4,997.00**: ขาดทุน 1.25 จุด = **62.50 ดอลลาร์** มากกว่าแผน 2.5 เท่า
> 4. **แล้วไง?** Heatmap ดูเหมือนกันทุกอย่างจนราคามาถึง ตัดสินใจหลังจากเห็นว่าแถบ **ซื้อขายและยืนได้** ถูก **กิน** หรือถูก **ถอน** เท่านั้น

> [!analogy]
> Heatmap เหมือน **แผนที่ฝูงชนในคอนเสิร์ต** จุดสว่างแสดงว่าตอนนี้มีคนยืนตรงไหนเยอะ จุดสว่างใหญ่ใกล้เวทีบอกว่าฝูงชนแน่นและขยับยาก แต่คนเดินออกได้ในไม่กี่วินาที และจุดที่ดูแน่นอาจว่างเปล่าตอนคุณไปถึง
>
> **จุดที่เปรียบเทียบไม่ได้:** คนดูคอนเสิร์ตมักไม่แกล้งทำเป็นยืนอยู่ตรงไหน แต่ในตลาด คำสั่งใหญ่บางตัววางไว้แค่ให้เห็น และถูกยกเลิกก่อนใครจะไปถึง (Spoofing, 7.3)

> [!check]- เช็กความเข้าใจ: อ่านแผนที่
> **Q1.** แถบสว่างหายไปทันทีก่อนราคาจะถึง และไม่มีการซื้อขายใหญ่เกิดขึ้น เกิดอะไรขึ้น?
> > [!answer]-
> > คำสั่งถูกถอน (ยกเลิก) ไม่มีแนวรับจริงตรงนั้น
> **Q2.** ฟองแสดงอะไรที่แถบสว่างไม่ได้แสดง?
> > [!answer]-
> > การซื้อขายที่เกิดขึ้นจริง (แรงรุก) แถบแสดงแค่ความตั้งใจที่ยกเลิกได้
""")
L.before_callout("th", "example", """
> [!check]- เช็กความเข้าใจ: ถูกกิน vs ถูกถอน
> **Q1.** แถบที่ 62,500 หดลงเรื่อย ๆ ขณะที่ฟองซื้อขนาดใหญ่กดใส่ แล้วราคาทะลุผ่าน ถูกกินหรือถูกถอน และบอกอะไร?
> > [!answer]-
> > ถูกกิน: ผู้ซื้อเชิงรุกเติมคำสั่งขายที่รออยู่จนหมด บอกถึงแรงซื้อเชิงริเริ่มที่แรง และน่าจะวิ่งต่อ
""")
L.before_callout("th", "action", """
> [!market]
> - **CFD ฟอเร็กซ์และทองคำ:** ไม่มีสมุดคำสั่งกลาง จึงไม่มี Heatmap ที่มีความหมาย ใช้ฟิวเจอร์ส CME (6E, GC) *(ดู 7.3)*
> - **หุ้นและดัชนี:** ฟิวเจอร์สดัชนี (ES, NQ) ให้ Heatmap ที่เชื่อถือได้ที่สุด
> - **คริปโต:** Heatmap เป็นที่นิยมและหาได้ทั่วไป แต่แต่ละกระดานแสดงแค่สมุดของตัวเอง และผู้เล่นคนเดียวอาจวางคำสั่งหลายกระดานพร้อมกัน *(ดู 0.7)*

> [!caution]
> Heatmap สะกดสายตาและเต็มไปด้วยคำสั่งที่จะไม่มีวันถูกซื้อขาย การจ้องทั้งวันนำไปสู่การเทรดมากเกินไปและการเชื่อกำแพงที่หายไป ใช้เฉพาะที่ระดับที่คุณทำเครื่องหมายไว้แล้วจากโครงสร้างหรือ Volume profile และยืนยันด้วยวอลุ่มที่ซื้อขายจริง (ฟอง Footprint) ก่อนเสี่ยงเงินเสมอ
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกชะตากรรมสามแบบของแถบสว่างเมื่อราคามาถึง และแต่ละแบบหมายถึงอะไร
> > [!answer]-
> > ยืนได้ (ซื้อขายมาก ยังอยู่): สภาพคล่องจริงที่ดูดซับ ถูกกิน (หดลงจากการซื้อขายเชิงรุก แล้วแตก): ฝั่งริเริ่มชนะ ถูกถอน (หายไปโดยไม่มีการซื้อขาย): สภาพคล่องปลอมหรือขี้ตกใจ ไม่มีแนวรับ
> **Q2.** ทำไมแถบใหญ่ที่รออยู่จึงมักมีประโยชน์ในฐานะ **เป้าหมาย** มากกว่าจุดเข้า?
> > [!answer]-
> > ราคามักถูกดึงไปหาสภาพคล่องก้อนใหญ่ (ผู้เล่นรายใหญ่ต้องใช้มันเติมคำสั่ง) แต่คุณรู้ล่วงหน้าไม่ได้ว่าแถบจะยืนได้ไหม จึงปลอดภัยกว่าที่จะใช้เป็นที่ปิดกำไร มากกว่าเป็นที่พึ่งพาเป็นแนวรับ
""")

L.set_meta("level", "v2")
L.save()
