"""B9f · v2 upgrade of 7.7 Checkpoint: Phase 7 Review (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("07 Orderflow & Auction Market Theory/7.7 Checkpoint- Phase 7 Review.md")

# ---------------------------------------------------------------- EN
L.before_callout("en", "practice", """
> [!check]- Worked problems: Phase 7
> **Q1.** A session's volume by price: 100: 5 · 101: 10 · 102: 20 · 103: 30 · 104: 18 · 105: 12 · 106: 5 (total 100). Find the POC and the 70% value area, adding one row at a time (the bigger neighbour first).
> > [!answer]-
> > POC **103** (30). Add 102 (20) → 50; then 104 (18) → 68; then 105 (12) → 80 ≥ 70. Value area **102–105**: VAL 102, VAH 105 (see 7.2).
> **Q2.** At a daily demand zone, three candles show market buys/sells of 900/1,300, 1,100/1,600 and 800/1,500, but the lows hold within two ticks. Deltas, cumulative delta, and the reading?
> > [!answer]-
> > Deltas **−400, −500, −700** → cumulative **−1,600**. Heavy selling with no new lows = **absorption** by a passive buyer. Wait for a price trigger before buying (see 7.4, 7.6).
> **Q3.** Delta on a 5-minute candle is +1,200, yet the candle closes with a long upper wick at the session's VAH. What's the likely story?
> > [!answer]-
> > Big effort (aggressive buying), poor result (rejection at value's edge): a passive seller absorbed it. Reversal risk back into value (see 7.1, 7.6).
""")
L.before_callout("en", "key", """
> [!check]- Final check: Phase 7
> **Q1.** Explain "effort vs result" in one line.
> > [!answer]-
> > Compare the aggression (volume, delta) with the price move it produced: big effort with little result means someone large is on the other side.
> **Q2.** Why do orderflow tools work best on futures and stocks, and poorly on spot forex?
> > [!answer]-
> > Futures and stocks trade on central exchanges with a complete order book and trade data; spot forex has no central exchange, so DOM and footprint data are partial (see 7.3).
""")

# ---------------------------------------------------------------- TH
L.before_callout("th", "practice", """
> [!check]- โจทย์ฝึกคำนวณ: เฟส 7
> **Q1.** วอลุ่มตามราคาของเซสชันหนึ่ง: 100: 5 · 101: 10 · 102: 20 · 103: 30 · 104: 18 · 105: 12 · 106: 5 (รวม 100) หา POC และ Value area 70% โดยเพิ่มทีละแถว (แถวข้างเคียงที่ใหญ่กว่าก่อน)
> > [!answer]-
> > POC **103** (30) เพิ่ม 102 (20) → 50 แล้ว 104 (18) → 68 แล้ว 105 (12) → 80 ≥ 70 Value area **102–105**: VAL 102, VAH 105 (ดู 7.2)
> **Q2.** ที่โซน Demand รายวัน แท่งเทียนสามแท่งมีคำสั่งซื้อ/ขาย Market 900/1,300, 1,100/1,600 และ 800/1,500 แต่จุดต่ำยืนได้ภายในสอง Tick Delta, Cumulative delta และการตีความ?
> > [!answer]-
> > Delta **−400, −500, −700** → สะสม **−1,600** แรงขายหนักแต่ไม่มีจุดต่ำใหม่ = **การดูดซับ (Absorption)** โดยผู้ซื้อแบบรอ รอสัญญาณราคาก่อนซื้อ (ดู 7.4, 7.6)
> **Q3.** Delta ของแท่ง 5 นาทีคือ +1,200 แต่แท่งปิดด้วยไส้บนยาวที่ VAH ของเซสชัน เรื่องที่น่าจะเกิดคืออะไร?
> > [!answer]-
> > แรงมาก (ซื้อแบบรุก) ผลน้อย (ถูกปฏิเสธที่ขอบของ Value): ผู้ขายแบบรอดูดซับไว้ มีความเสี่ยงกลับตัวลงเข้า Value (ดู 7.1, 7.6)
""")
L.before_callout("th", "key", """
> [!check]- ทดสอบสุดท้าย: เฟส 7
> **Q1.** อธิบาย "แรงที่ใช้ vs ผลลัพธ์ (Effort vs result)" ในหนึ่งบรรทัด
> > [!answer]-
> > เทียบความรุก (วอลุ่ม Delta) กับการขยับราคาที่มันสร้าง: แรงมากแต่ผลน้อย แปลว่ามีรายใหญ่อยู่อีกฝั่ง
> **Q2.** ทำไมเครื่องมือ Orderflow ใช้ได้ดีที่สุดกับฟิวเจอร์สและหุ้น แต่ใช้ได้ไม่ดีกับฟอเร็กซ์ Spot?
> > [!answer]-
> > ฟิวเจอร์สและหุ้นซื้อขายในตลาดกลางที่มีสมุดคำสั่งและข้อมูลการซื้อขายครบ ฟอเร็กซ์ Spot ไม่มีตลาดกลาง ข้อมูล DOM และ Footprint จึงไม่ครบ (ดู 7.3)
""")

L.set_meta("level", "v2")
L.save()
