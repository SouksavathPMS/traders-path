"""B9f · v2 upgrade of 5.8 Checkpoint: Phase 5 Review (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("05 Liquidity & ICT/5.8 Checkpoint- Phase 5 Review.md")

# ---------------------------------------------------------------- EN
L.before_callout("en", "practice", """
> [!check]- Worked problems: Phase 5
> **Q1.** A bullish dealing range on EUR/USD runs from 1.0800 to 1.0920. Where is equilibrium, and where is the OTE zone for longs (62–79%)?
> > [!answer]-
> > Range = 0.0120. Equilibrium = **1.0860**. OTE = 1.0920 − 0.62 × 0.0120 = **1.0846** down to 1.0920 − 0.79 × 0.0120 = **1.0825** (see 5.3).
> **Q2.** Gold: candle 1 high 2,341.0, candle 2 a big up candle, candle 3 low 2,346.4. What's the FVG and its CE? Entry at the CE, stop 2,336.0 below the sweep low, target the buy-side liquidity at 2,371.0. R:R?
> > [!answer]-
> > FVG **2,341.0–2,346.4**, CE **2,343.7**. Risk 7.7, reward 27.3 → about **3.5R** (see 5.4, 5.7).
> **Q3.** It's northern summer. When are the London and New York AM killzones in Bangkok time?
> > [!answer]-
> > London **13:00–16:00**; New York AM **18:00–21:00** (one hour later in northern winter) (see 5.6).
""")
L.before_callout("en", "key", """
> [!check]- Final check: Phase 5
> **Q1.** Put the model's steps in order: MSS, liquidity target, sweep, bias, PD array, discount, time, risk.
> > [!answer]-
> > Bias → liquidity target → discount → sweep → time → MSS → PD array → risk (see 5.7).
> **Q2.** Price wicks below equal lows and closes back above, but there's no displacement and no MSS. Do you buy?
> > [!answer]-
> > No. A sweep without confirmation is not a trade; it may simply be a run that continues lower (see 5.2).
""")

# ---------------------------------------------------------------- TH
L.before_callout("th", "practice", """
> [!check]- โจทย์ฝึกคำนวณ: เฟส 5
> **Q1.** Dealing range ขาขึ้นของ EUR/USD จาก 1.0800 ถึง 1.0920 Equilibrium อยู่ที่ไหน และโซน OTE สำหรับฝั่งซื้อ (62–79%) อยู่ที่ไหน?
> > [!answer]-
> > ช่วง = 0.0120 Equilibrium = **1.0860** OTE = 1.0920 − 0.62 × 0.0120 = **1.0846** ลงไปถึง 1.0920 − 0.79 × 0.0120 = **1.0825** (ดู 5.3)
> **Q2.** ทองคำ: แท่ง 1 จุดสูง 2,341.0 แท่ง 2 เป็นแท่งขึ้นใหญ่ แท่ง 3 จุดต่ำ 2,346.4 FVG และ CE อยู่ที่ไหน? เข้าที่ CE Stop 2,336.0 ใต้จุดต่ำที่ถูก Sweep เป้า Buy-side liquidity ที่ 2,371.0 R:R เท่าไร?
> > [!answer]-
> > FVG **2,341.0–2,346.4** CE **2,343.7** เสี่ยง 7.7 ผลตอบแทน 27.3 → ราว **3.5R** (ดู 5.4, 5.7)
> **Q3.** ช่วงฤดูร้อนซีกโลกเหนือ Killzone ลอนดอนและนิวยอร์กช่วงเช้าอยู่กี่โมงตามเวลากรุงเทพฯ?
> > [!answer]-
> > ลอนดอน **13:00–16:00** นิวยอร์กช่วงเช้า **18:00–21:00** (ช่วงฤดูหนาวซีกโลกเหนือช้าลงหนึ่งชั่วโมง) (ดู 5.6)
""")
L.before_callout("th", "key", """
> [!check]- ทดสอบสุดท้าย: เฟส 5
> **Q1.** เรียงขั้นตอนของโมเดล: MSS, เป้าสภาพคล่อง, Sweep, Bias, PD array, Discount, เวลา, ความเสี่ยง
> > [!answer]-
> > Bias → เป้าสภาพคล่อง → Discount → Sweep → เวลา → MSS → PD array → ความเสี่ยง (ดู 5.7)
> **Q2.** ราคาแทงไส้ใต้ Equal lows แล้วปิดกลับขึ้นมา แต่ไม่มี Displacement และไม่มี MSS คุณซื้อไหม?
> > [!answer]-
> > ไม่ซื้อ Sweep ที่ไม่มีการยืนยันไม่ใช่เทรด อาจเป็นแค่การวิ่งที่ลงต่อ (ดู 5.2)
""")

L.set_meta("level", "v2")
L.save()
