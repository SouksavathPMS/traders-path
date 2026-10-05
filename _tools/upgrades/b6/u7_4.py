"""B6 · v2 upgrade of 7.4 Footprint Charts & Delta (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("07 Orderflow & Auction Market Theory/7.4 Footprint Charts & Delta.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> A normal candle only tells you four prices: open, high, low, close. A footprint opens the candle up and shows, for every price inside it, how many people **bought in a hurry** (paying the seller's price) and how many **sold in a hurry** (accepting the buyer's price). Subtract the two and you get **delta**: which side was pushing harder. It's like seeing not just the final score of a match, but who had the ball and where.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Footprint chart** — a candle split into price rows, showing executed volume at the bid and at the ask for each row.
> - **Aggressor** — the side that used a market order: a buyer who **lifts the ask** or a seller who **hits the bid**.
> - **Passive side** — the resting limit order that got filled.
> - **Bid × ask (sells × buys)** — left number: market sells that traded at the bid; right number: market buys that traded at the ask.
> - **Delta (Δ)** — market buys − market sells (for a row or a whole candle).
> - **Diagonal imbalance** — buys at one price compared with sells **one tick lower** (or sells vs buys one tick higher), usually flagged at ≥ 3×.
> - **Stacked imbalances** — three or more imbalances in a row in the same direction.
> - **CVD (cumulative volume delta)** — delta added up over time.
> - **Divergence** — price makes a new high (low) but CVD doesn't.
> - **Tick data** — every individual trade; footprints need it.
""")
L.before_heading("en", "2.", """
![[p7-single-trade.en.svg]]

> [!walkthrough] Step by step: one trade at a time
> Best bid **100.00**, best ask **100.25**.
> 1. **Trader A** buys **5** with a market order. A buyer in a hurry pays the ask → 5 trade at **100.25** → the footprint row 100.25 shows **0 × 5** (right column).
> 2. **Trader B** sells **3** with a market order. A seller in a hurry accepts the bid → 3 trade at **100.00** → row 100.00 shows **3 × 0** (left column).
> 3. **Delta** for this tiny candle = buys − sells = 5 − 3 = **+2**.
> 4. **So what?** Every number on a footprint is a pile of these single decisions. Left = people who were in a hurry to sell, right = people in a hurry to buy. Nothing on the footprint shows the patient limit orders; those are on the DOM (7.3).

> [!analogy]
> If the DOM is the **price tags in a shop window**, the footprint is the **till receipts**: what was actually paid, at which price, and whether the customer paid the full ticket price (aggressive buyer) or the shop accepted a lower offer (aggressive seller).
>
> **Where it breaks:** receipts tell you what happened, not why. A big buyer splitting one decision into hundreds of small trades looks like many small customers.

> [!check]- Check your understanding: bid × ask
> **Q1.** A row shows **120 × 450**. Which side was more aggressive at that price, and what is the row delta?
> > [!answer]-
> > Buyers: 450 bought at the ask vs 120 sold at the bid. Delta = 450 − 120 = +330.
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: checking a diagonal imbalance
> Rows (sells × buys): 100.50 → **90 × 210**, 100.25 → **140 × 450**, 100.00 → **120 × 160**.
> 1. **Buy imbalance at 100.25?** Compare buys at 100.25 (**450**) with sells one tick **lower**, at 100.00 (**120**): 450 ÷ 120 = **3.75** ≥ 3 → **yes**.
> 2. **Why diagonal?** The buyer at 100.25 traded against sellers resting at the ask, while the sellers at 100.00 traded against buyers at the bid. Comparing 450 with 140 (same row) would compare trades that happened at different prices.
> 3. **Sell imbalance at 100.00?** Compare sells at 100.00 (**120**) with buys one tick **higher**, at 100.25 (**450**): 120 ÷ 450 ≈ 0.27 → **no**.
> 4. **So what?** One imbalance is just a moment. Three stacked buy imbalances in a row show sustained initiative buying, and that area is often defended on a retest.

> [!check]- Check your understanding: imbalances
> **Q1.** At 101.00 sells are **600**; at 101.25 buys are **150**. Is there a sell imbalance at 101.00 (3× rule)?
> > [!answer]-
> > Yes: 600 ÷ 150 = 4 ≥ 3.
""")
L.before_callout("en", "example", """
> [!walkthrough] Step by step: building CVD from three candles
> Candle deltas from the figure: **+352**, **+775**, **−935**.
> 1. After candle 1: CVD = **+352**.
> 2. After candle 2: 352 + 775 = **+1,127**.
> 3. After candle 3: 1,127 − 935 = **+192**.
> 4. **Read:** price made its high in candle 3, but CVD dropped from +1,127 to +192: aggressive selling took over exactly at the high.
> 5. **So what?** A new price high with falling CVD is a **divergence**: the push is no longer confirmed by aggression. It's a warning to look for a structure shift (CHoCH), not a sell signal on its own.

> [!check]- Check your understanding: CVD
> **Q1.** Price makes a lower low but CVD makes a higher low. What could that mean?
> > [!answer]-
> > A bullish divergence: sellers are less aggressive at the new low, or a passive buyer is absorbing them. Watch for a CHoCH up.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** spot FX has no real trade data, so no true footprint; use currency futures (6E, 6J) *(see 7.3)*.
> - **Gold:** use COMEX futures (GC/MGC) for footprints; XAU/USD CFD "volume" is only tick counts *(see 0.4)*.
> - **Stocks & indices:** index futures (ES, NQ) give the cleanest footprints; single stocks work but are fragmented across venues.
> - **Crypto:** footprints are available per exchange; delta can differ between exchanges, so use the main venue or an aggregate *(see 0.7)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** A trader buys 10 with a market order when the bid is 50.00 and the ask is 50.05. Where does it appear on the footprint?
> > [!answer]-
> > In the ask (right) column of the 50.05 row: 0 × 10. Delta +10.
> **Q2.** Strong positive delta but price doesn't rise. What might be happening?
> > [!answer]-
> > A large passive seller is absorbing the aggressive buying (absorption, 7.6). Delta shows aggression, not direction.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> แท่งเทียนปกติบอกแค่สี่ราคา: เปิด สูง ต่ำ ปิด Footprint เปิดแท่งเทียนออกแล้วแสดงว่า ในทุกราคาภายในแท่ง มีกี่คนที่ **รีบซื้อ** (จ่ายราคาที่ผู้ขายตั้ง) และกี่คนที่ **รีบขาย** (ยอมรับราคาที่ผู้ซื้อเสนอ) ลบสองค่านี้ คุณจะได้ **Delta**: ฝั่งไหนดันแรงกว่า เหมือนไม่ได้เห็นแค่สกอร์สุดท้ายของการแข่งขัน แต่เห็นว่าใครครองบอลและอยู่ตรงไหน
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **Footprint chart** — แท่งเทียนที่แบ่งเป็นแถวราคา แสดงวอลุ่มที่ซื้อขายจริงที่ Bid และที่ Ask ของแต่ละแถว
> - **ฝั่งที่รุก (Aggressor)** — ฝั่งที่ใช้คำสั่ง Market: ผู้ซื้อที่ **ยก Ask** หรือผู้ขายที่ **กด Bid**
> - **ฝั่งรับ (Passive side)** — คำสั่ง Limit ที่รออยู่แล้วถูกจับคู่
> - **Bid × Ask (ขาย × ซื้อ)** — เลขซ้าย: คำสั่งขาย Market ที่ซื้อขายที่ Bid เลขขวา: คำสั่งซื้อ Market ที่ซื้อขายที่ Ask
> - **Delta (Δ)** — ซื้อแบบ Market − ขายแบบ Market (ของแถวหรือของทั้งแท่ง)
> - **Diagonal imbalance** — การซื้อที่ราคาหนึ่งเทียบกับการขายที่ **ต่ำกว่าหนึ่ง tick** (หรือการขายเทียบกับการซื้อที่สูงกว่าหนึ่ง tick) มักนับเมื่อ ≥ 3 เท่า
> - **Stacked imbalances** — Imbalance สามอันขึ้นไปติดกันในทิศทางเดียวกัน
> - **CVD (Cumulative volume delta)** — Delta ที่บวกสะสมตามเวลา
> - **Divergence** — ราคาทำจุดสูง (ต่ำ) ใหม่ แต่ CVD ไม่ทำ
> - **Tick data** — การซื้อขายทุกรายการ Footprint ต้องใช้ข้อมูลนี้
""")
L.before_heading("th", "2.", """
![[p7-single-trade.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ทีละการซื้อขาย
> Bid ดีที่สุด **100.00** Ask ดีที่สุด **100.25**
> 1. **เทรดเดอร์ A** ซื้อ **5** ด้วยคำสั่ง Market ผู้ซื้อที่รีบจ่ายราคา Ask → ซื้อขาย 5 ที่ **100.25** → แถว 100.25 บน Footprint แสดง **0 × 5** (คอลัมน์ขวา)
> 2. **เทรดเดอร์ B** ขาย **3** ด้วยคำสั่ง Market ผู้ขายที่รีบยอมรับราคา Bid → ซื้อขาย 3 ที่ **100.00** → แถว 100.00 แสดง **3 × 0** (คอลัมน์ซ้าย)
> 3. **Delta** ของแท่งจิ๋วนี้ = ซื้อ − ขาย = 5 − 3 = **+2**
> 4. **แล้วไง?** ทุกตัวเลขบน Footprint คือกองของการตัดสินใจเดี่ยว ๆ แบบนี้ ซ้าย = คนที่รีบขาย ขวา = คนที่รีบซื้อ Footprint ไม่แสดงคำสั่ง Limit ที่อดทนรอ สิ่งนั้นอยู่บน DOM (7.3)

> [!analogy]
> ถ้า DOM คือ **ป้ายราคาในตู้โชว์** Footprint คือ **ใบเสร็จที่เครื่องคิดเงิน**: จ่ายจริงเท่าไหร่ ที่ราคาไหน และลูกค้าจ่ายราคาเต็มป้าย (ผู้ซื้อที่รุก) หรือร้านยอมรับราคาที่ต่ำกว่า (ผู้ขายที่รุก)
>
> **จุดที่เปรียบเทียบไม่ได้:** ใบเสร็จบอกว่าเกิดอะไร ไม่ได้บอกว่าทำไม ผู้ซื้อรายใหญ่ที่แบ่งการตัดสินใจเดียวเป็นการซื้อขายเล็ก ๆ หลายร้อยครั้ง ดูเหมือนลูกค้ารายเล็กจำนวนมาก

> [!check]- เช็กความเข้าใจ: Bid × Ask
> **Q1.** แถวหนึ่งแสดง **120 × 450** ฝั่งไหนรุกกว่าที่ราคานั้น และ Delta ของแถวเท่าไหร่?
> > [!answer]-
> > ผู้ซื้อ: ซื้อที่ Ask 450 เทียบกับขายที่ Bid 120  Delta = 450 − 120 = +330
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: ตรวจ Diagonal imbalance
> แถว (ขาย × ซื้อ): 100.50 → **90 × 210**, 100.25 → **140 × 450**, 100.00 → **120 × 160**
> 1. **Buy imbalance ที่ 100.25?** เทียบการซื้อที่ 100.25 (**450**) กับการขายที่ **ต่ำกว่าหนึ่ง tick** ที่ 100.00 (**120**): 450 ÷ 120 = **3.75** ≥ 3 → **ใช่**
> 2. **ทำไมต้องทแยง?** ผู้ซื้อที่ 100.25 ซื้อขายกับผู้ขายที่รออยู่ที่ Ask ส่วนผู้ขายที่ 100.00 ซื้อขายกับผู้ซื้อที่ Bid การเทียบ 450 กับ 140 (แถวเดียวกัน) คือการเทียบการซื้อขายที่เกิดคนละราคา
> 3. **Sell imbalance ที่ 100.00?** เทียบการขายที่ 100.00 (**120**) กับการซื้อที่ **สูงกว่าหนึ่ง tick** ที่ 100.25 (**450**): 120 ÷ 450 ≈ 0.27 → **ไม่ใช่**
> 4. **แล้วไง?** Imbalance เดียวเป็นแค่ชั่วขณะ แต่ Buy imbalance สามอันซ้อนกันแสดงแรงซื้อเชิงริเริ่มที่ต่อเนื่อง และบริเวณนั้นมักถูกป้องกันเมื่อราคากลับมาทดสอบ

> [!check]- เช็กความเข้าใจ: Imbalance
> **Q1.** ที่ 101.00 มีการขาย **600** ที่ 101.25 มีการซื้อ **150** มี Sell imbalance ที่ 101.00 ไหม (กฎ 3 เท่า)?
> > [!answer]-
> > มี: 600 ÷ 150 = 4 ≥ 3
""")
L.before_callout("th", "example", """
> [!walkthrough] ไล่ทีละขั้น: สร้าง CVD จากสามแท่ง
> Delta ของแท่งในภาพ: **+352**, **+775**, **−935**
> 1. หลังแท่ง 1: CVD = **+352**
> 2. หลังแท่ง 2: 352 + 775 = **+1,127**
> 3. หลังแท่ง 3: 1,127 − 935 = **+192**
> 4. **อ่าน:** ราคาทำจุดสูงในแท่ง 3 แต่ CVD ลดจาก +1,127 เหลือ +192: แรงขายเชิงรุกเข้าควบคุมตรงจุดสูงพอดี
> 5. **แล้วไง?** จุดสูงใหม่ของราคาพร้อม CVD ที่ลดลงคือ **Divergence**: การดันไม่ได้รับการยืนยันจากแรงรุกแล้ว เป็นคำเตือนให้มองหาการเปลี่ยนโครงสร้าง (CHoCH) ไม่ใช่สัญญาณขายในตัวเอง

> [!check]- เช็กความเข้าใจ: CVD
> **Q1.** ราคาทำจุดต่ำใหม่ แต่ CVD ทำจุดต่ำที่สูงขึ้น หมายความว่าอะไรได้บ้าง?
> > [!answer]-
> > Bullish divergence: ผู้ขายรุกน้อยลงที่จุดต่ำใหม่ หรือมีผู้ซื้อแบบรับกำลังดูดซับอยู่ รอดู CHoCH ขาขึ้น
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** ฟอเร็กซ์ Spot ไม่มีข้อมูลการซื้อขายจริง จึงไม่มี Footprint ที่แท้ ใช้ฟิวเจอร์สค่าเงิน (6E, 6J) *(ดู 7.3)*
> - **ทองคำ:** ใช้ฟิวเจอร์ส COMEX (GC/MGC) ทำ Footprint "วอลุ่ม" ของ CFD XAU/USD เป็นแค่จำนวน Tick *(ดู 0.4)*
> - **หุ้นและดัชนี:** ฟิวเจอร์สดัชนี (ES, NQ) ให้ Footprint สะอาดที่สุด หุ้นรายตัวใช้ได้แต่กระจายหลายตลาด
> - **คริปโต:** มี Footprint แยกตามกระดาน Delta อาจต่างกันระหว่างกระดาน ใช้กระดานหลักหรือข้อมูลรวม *(ดู 0.7)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** เทรดเดอร์ซื้อ 10 ด้วยคำสั่ง Market ตอน Bid 50.00 และ Ask 50.05 จะแสดงตรงไหนบน Footprint?
> > [!answer]-
> > ในคอลัมน์ Ask (ขวา) ของแถว 50.05: 0 × 10  Delta +10
> **Q2.** Delta เป็นบวกแรง แต่ราคาไม่ขึ้น อาจเกิดอะไรขึ้น?
> > [!answer]-
> > มีผู้ขายแบบรับรายใหญ่ดูดซับแรงซื้อเชิงรุก (Absorption, 7.6) Delta บอกแรงรุก ไม่ได้บอกทิศทาง
""")

L.set_meta("level", "v2")
L.save()
