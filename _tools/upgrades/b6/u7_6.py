"""B6 · v2 upgrade of 7.6 Absorption & Exhaustion Setups (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("07 Orderflow & Auction Market Theory/7.6 Absorption & Exhaustion Setups.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Imagine pushing a door as hard as you can and it doesn't move: someone strong is leaning on the other side. That's **absorption**: lots of aggressive selling (or buying), but price doesn't move, because a big hidden player is taking it all. Now imagine a runner who gets slower with every lap: that's **exhaustion**. Price keeps making new highs, but each one needs less buying, until the buyers simply run out. Both tell you the side that looks strong is about to lose.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Absorption** — heavy aggressive orders meet a large passive order and price doesn't move.
> - **Exhaustion** — the aggressive push fades (less volume and delta) as price makes new extremes.
> - **Effort vs result** — effort = aggressive volume/delta; result = how far price moves.
> - **Aggressive / passive** — market orders that cross the spread / limit orders that wait *(see 7.4)*.
> - **Tape / prints / time and sales** — the list of every executed trade with time, price and size.
> - **Iceberg** — a hidden large order that keeps refilling *(see 7.3)*.
> - **Delta flip** — candle delta changing sign (e.g. from strongly positive to negative) at an extreme.
> - **Climax** — a final, high-volume push that marks the end of a move.
> - **Trapped traders** — traders who entered on the wrong side and must exit, adding fuel to the reversal.
> - **CHoCH** — change of character, the price trigger that confirms the turn *(see 2.3)*.
""")
L.before_heading("en", "2.", """
> [!analogy]
> Absorption is like **pushing a door that someone is holding shut**: huge effort, no result, and when you get tired the door swings the other way. Exhaustion is like a **runner slowing down each lap**: still moving forward, but every lap costs more and gains less, until they stop.
>
> **Where it breaks:** you can feel a door push back. In markets you only infer the hidden absorber from numbers (heavy delta, no movement), and sometimes the "door" breaks open suddenly when the absorber has finished.

> [!check]- Check your understanding: absorption
> **Q1.** At a support level, three candles show delta of −1,500, −1,800 and −1,650, but the low stays within 0.05. Effort or result missing?
> > [!answer]-
> > Big effort (heavy selling), no result (price doesn't fall): absorption by a passive buyer.
""")
L.before_heading("en", "3.", """
![[p7-tapes.en.svg]]

> [!walkthrough] Step by step: classify the two tapes
> **Tape A (at support 100.10):**
> 1. Five sells hit the bid at **100.10**: 300 + 250 + 400 + 350 + 280 = **1,580** contracts.
> 2. Price never trades below 100.10, and the visible bid only ever showed about **100**.
> 3. Then a buyer lifts the ask at **100.15**.
> 4. **Classification: absorption.** 1,580 sold into a bid that looked like 100: a hidden buyer (an iceberg) took it all. Effort without result.
> **Tape B (at new highs):**
> 5. Buyers lift the ask at **101.20, 101.30, 101.40, 101.45** with sizes **400, 250, 120, 60**: each new high needs less buying.
> 6. Then sellers hit the bid for **300** and **280**, pushing price back to 101.30. Delta flips negative.
> 7. **Classification: exhaustion.** Buyers ran out of fuel at the top, and sellers took control.
> 8. **So what?** Neither tape is a trade by itself. Tape A says "look for a long trigger above the absorption"; tape B says "look for a short trigger, the trend may be ending". The price trigger (CHoCH) still decides.

> [!check]- Check your understanding: exhaustion
> **Q1.** Price makes three new highs with candle deltas of +900, +500 and +150, then a candle with delta −600. What pattern is this?
> > [!answer]-
> > Exhaustion: shrinking positive delta on new highs, then a delta flip. Look for a sweep and a CHoCH down.
""")
L.before_callout("en", "action", """
> [!walkthrough] Step by step: sizing the absorption long
> From the example: entry **101.0**, stop **99.8** (below the absorption lows + buffer), target **103.4**.
> 1. **Risk per unit** = 101.0 − 99.8 = **1.2**.
> 2. **Account 10,000 USD, risk 1%** = 100 USD → 100 ÷ 1.2 = 83.3 → **83 units** (real risk 99.60 USD).
> 3. **Reward per unit** = 103.4 − 101.0 = **2.4** → **2.0R** (= 199.20 USD on 83 units).
> 4. **If the absorber gives up** and price breaks below 100.0, the trapped buyers are now you: the stop at 99.8 caps the loss at 1R.
> 5. **So what?** Orderflow improved the **location** and confidence, not the rules: the stop still goes beyond the extreme and the size still comes from it.

> [!market]
> - **Forex & gold CFDs:** no real trade data, so absorption and exhaustion can't be read directly; use futures (6E, GC) *(see 7.3)*.
> - **Stocks & indices:** index futures (ES, NQ) show absorption most clearly; single stocks also show it on Level 2 + time and sales.
> - **Crypto:** absorption is visible on the main exchanges' tapes; exhaustion often ends in a liquidation cascade *(see 0.7)*.

> [!caution]
> Calling absorption too early is expensive: if the hidden buyer stops, price can fall through the level fast, often with slippage. Never enter on the orderflow signal alone. Wait for the price trigger, keep the stop beyond the extreme, and size for 1R.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Describe absorption and exhaustion in terms of effort vs result.
> > [!answer]-
> > Absorption: big effort (aggressive volume/delta), little or no result (price doesn't move). Exhaustion: the effort itself fades while price still extends, until it stops.
> **Q2.** Why does location matter so much for these signals?
> > [!answer]-
> > Absorption or exhaustion at a level that already matters (HTF zone, VAL/VAH, swept liquidity) shows a real participant defending it. In the middle of nowhere it's usually noise.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ลองนึกถึงการผลักประตูสุดแรงแต่ประตูไม่ขยับ: มีคนแข็งแรงยันอยู่อีกฝั่ง นั่นคือ **Absorption (การดูดซับ)**: มีแรงขาย (หรือซื้อ) เชิงรุกมาก แต่ราคาไม่ขยับ เพราะผู้เล่นรายใหญ่ที่ซ่อนอยู่รับไปหมด ทีนี้ลองนึกถึงนักวิ่งที่ช้าลงทุกรอบ: นั่นคือ **Exhaustion (ความเหนื่อยล้า)** ราคายังทำจุดสูงใหม่ แต่แต่ละครั้งใช้แรงซื้อน้อยลง จนผู้ซื้อหมดแรง ทั้งสองบอกว่าฝั่งที่ดูแข็งแรงกำลังจะแพ้
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **การดูดซับ (Absorption)** — คำสั่งเชิงรุกจำนวนมากเจอคำสั่งแบบรับขนาดใหญ่ และราคาไม่ขยับ
> - **ความเหนื่อยล้า (Exhaustion)** — แรงดันเชิงรุกจางลง (วอลุ่มและ Delta น้อยลง) ขณะที่ราคาทำจุดสุดใหม่
> - **ความพยายาม vs ผลลัพธ์ (Effort vs result)** — ความพยายาม = วอลุ่ม/Delta เชิงรุก ผลลัพธ์ = ราคาขยับไปไกลแค่ไหน
> - **เชิงรุก / แบบรับ (Aggressive / Passive)** — คำสั่ง Market ที่ข้าม Spread / คำสั่ง Limit ที่รอ *(ดู 7.4)*
> - **Tape / Prints / Time and sales** — รายการการซื้อขายที่เกิดจริงทุกรายการ พร้อมเวลา ราคา และขนาด
> - **Iceberg** — คำสั่งใหญ่ที่ซ่อนอยู่และเติมใหม่เรื่อย ๆ *(ดู 7.3)*
> - **Delta flip** — Delta ของแท่งเปลี่ยนเครื่องหมาย (เช่น จากบวกแรงเป็นลบ) ที่จุดสุด
> - **Climax** — การดันครั้งสุดท้ายด้วยวอลุ่มสูงที่บ่งบอกจุดจบของการวิ่ง
> - **เทรดเดอร์ที่ติดกับ (Trapped traders)** — คนที่เข้าผิดฝั่งและต้องออก ซึ่งเพิ่มเชื้อเพลิงให้การกลับตัว
> - **CHoCH** — การเปลี่ยนนิสัย สัญญาณจากราคาที่ยืนยันการกลับตัว *(ดู 2.3)*
""")
L.before_heading("th", "2.", """
> [!analogy]
> Absorption เหมือน **การผลักประตูที่มีคนยันไว้**: ออกแรงมาก ไม่มีผล และเมื่อคุณเหนื่อย ประตูก็เหวี่ยงกลับมาอีกทาง Exhaustion เหมือน **นักวิ่งที่ช้าลงทุกรอบ**: ยังวิ่งไปข้างหน้า แต่ทุกรอบใช้แรงมากขึ้นและได้ระยะน้อยลง จนหยุด
>
> **จุดที่เปรียบเทียบไม่ได้:** คุณรู้สึกได้ว่าประตูดันกลับ แต่ในตลาดคุณอนุมานผู้ดูดซับที่ซ่อนอยู่ได้จากตัวเลขเท่านั้น (Delta หนัก ราคาไม่ขยับ) และบางครั้ง "ประตู" เปิดผัวะทันทีเมื่อผู้ดูดซับรับครบแล้ว

> [!check]- เช็กความเข้าใจ: Absorption
> **Q1.** ที่แนวรับ สามแท่งมี Delta −1,500, −1,800 และ −1,650 แต่จุดต่ำแทบไม่ขยับ (ภายใน 0.05) ขาดความพยายามหรือขาดผลลัพธ์?
> > [!answer]-
> > ความพยายามมาก (ขายหนัก) ไม่มีผลลัพธ์ (ราคาไม่ลง): ผู้ซื้อแบบรับกำลังดูดซับ
""")
L.before_heading("th", "3.", """
![[p7-tapes.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: จำแนก Tape สองชุด
> **Tape A (ที่แนวรับ 100.10):**
> 1. มีการขายกด Bid ที่ **100.10** ห้าครั้ง: 300 + 250 + 400 + 350 + 280 = **1,580** สัญญา
> 2. ราคาไม่เคยซื้อขายต่ำกว่า 100.10 และ Bid ที่มองเห็นแสดงแค่ราว **100** ตลอด
> 3. จากนั้นมีผู้ซื้อยก Ask ที่ **100.15**
> 4. **จำแนก: Absorption** ขาย 1,580 ใส่ Bid ที่ดูเหมือนมีแค่ 100: ผู้ซื้อที่ซ่อนอยู่ (Iceberg) รับไปหมด มีความพยายามแต่ไม่มีผลลัพธ์
> **Tape B (ที่จุดสูงใหม่):**
> 5. ผู้ซื้อยก Ask ที่ **101.20, 101.30, 101.40, 101.45** ด้วยขนาด **400, 250, 120, 60**: จุดสูงใหม่แต่ละครั้งใช้แรงซื้อน้อยลง
> 6. จากนั้นผู้ขายกด Bid **300** และ **280** ดันราคากลับไป 101.30  Delta พลิกเป็นลบ
> 7. **จำแนก: Exhaustion** ผู้ซื้อหมดเชื้อเพลิงที่ยอด และผู้ขายเข้าควบคุม
> 8. **แล้วไง?** Tape ทั้งสองยังไม่ใช่ไม้เทรดในตัวเอง Tape A บอกว่า "หาสัญญาณ Long เหนือบริเวณดูดซับ" Tape B บอกว่า "หาสัญญาณ Short เทรนด์อาจกำลังจบ" สัญญาณจากราคา (CHoCH) ยังเป็นตัวตัดสิน

> [!check]- เช็กความเข้าใจ: Exhaustion
> **Q1.** ราคาทำจุดสูงใหม่สามครั้งด้วย Delta ของแท่ง +900, +500 และ +150 แล้วตามด้วยแท่งที่ Delta −600 นี่คือรูปแบบอะไร?
> > [!answer]-
> > Exhaustion: Delta บวกที่หดลงบนจุดสูงใหม่ แล้วพลิกเป็นลบ รอดูการกวาดและ CHoCH ขาลง
""")
L.before_callout("th", "action", """
> [!walkthrough] ไล่ทีละขั้น: คำนวณขนาดไม้ Long จาก Absorption
> จากตัวอย่าง: เข้า **101.0** Stop **99.8** (ใต้จุดต่ำของการดูดซับ + ระยะเผื่อ) เป้า **103.4**
> 1. **ความเสี่ยงต่อหน่วย** = 101.0 − 99.8 = **1.2**
> 2. **บัญชี 10,000 ดอลลาร์ เสี่ยง 1%** = 100 ดอลลาร์ → 100 ÷ 1.2 = 83.3 → **83 หน่วย** (ความเสี่ยงจริง 99.60 ดอลลาร์)
> 3. **ผลตอบแทนต่อหน่วย** = 103.4 − 101.0 = **2.4** → **2.0R** (= 199.20 ดอลลาร์ที่ 83 หน่วย)
> 4. **ถ้าผู้ดูดซับยอมแพ้** และราคาหลุดใต้ 100.0 ผู้ซื้อที่ติดกับคราวนี้คือคุณ: Stop ที่ 99.8 จำกัดการขาดทุนไว้ที่ 1R
> 5. **แล้วไง?** ออเดอร์โฟลว์ช่วยเรื่อง **ตำแหน่ง** และความมั่นใจ ไม่ได้เปลี่ยนกฎ: Stop ยังอยู่เลยจุดสุด และขนาดไม้ยังมาจาก Stop

> [!market]
> - **CFD ฟอเร็กซ์และทองคำ:** ไม่มีข้อมูลการซื้อขายจริง จึงอ่าน Absorption และ Exhaustion โดยตรงไม่ได้ ใช้ฟิวเจอร์ส (6E, GC) *(ดู 7.3)*
> - **หุ้นและดัชนี:** ฟิวเจอร์สดัชนี (ES, NQ) แสดง Absorption ชัดที่สุด หุ้นรายตัวก็เห็นได้จาก Level 2 + Time and sales
> - **คริปโต:** เห็น Absorption ได้บน Tape ของกระดานหลัก Exhaustion มักจบด้วยการล้างพอร์ตต่อเนื่อง *(ดู 0.7)*

> [!caution]
> การเรียก Absorption เร็วเกินไปแพง: ถ้าผู้ซื้อที่ซ่อนอยู่หยุด ราคาอาจหลุดระดับอย่างรวดเร็ว และมัก Slippage อย่าเข้าจากสัญญาณออเดอร์โฟลว์อย่างเดียว รอสัญญาณจากราคา วาง Stop เลยจุดสุด และคำนวณขนาดสำหรับ 1R
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** อธิบาย Absorption และ Exhaustion ในแง่ความพยายาม vs ผลลัพธ์
> > [!answer]-
> > Absorption: ความพยายามมาก (วอลุ่ม/Delta เชิงรุก) ผลลัพธ์น้อยหรือไม่มี (ราคาไม่ขยับ) Exhaustion: ความพยายามเองจางลงขณะที่ราคายังวิ่งต่อ จนหยุด
> **Q2.** ทำไมตำแหน่งจึงสำคัญมากสำหรับสัญญาณเหล่านี้?
> > [!answer]-
> > Absorption หรือ Exhaustion ที่ระดับที่สำคัญอยู่แล้ว (โซน HTF VAL/VAH สภาพคล่องที่ถูกกวาด) แสดงว่ามีผู้เล่นจริงป้องกันอยู่ ถ้าอยู่กลางที่โล่ง มักเป็นแค่สัญญาณรบกวน
""")

L.set_meta("level", "v2")
L.save()
