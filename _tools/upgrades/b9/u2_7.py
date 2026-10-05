"""B9b · v2 upgrade of 2.7 Checkpoint: Phase 2 Review (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("02 Market Structure/2.7 Checkpoint- Phase 2 Review.md")

# ---------------------------------------------------------------- EN
L.before_callout("en", "practice", """
> [!check]- Worked problems: Phase 2
> **Q1.** Swings in order: H 40, L 37, H 44, L 41, H 47, L 43. What's the state, which low is protected, and what does a close at 42.5 mean?
> > [!answer]-
> > Uptrend (HH + HL). The protected low is **41**, the low the latest HH (47) was built from. A close at 42.5 breaks the newest low (43) but not 41: a deeper pullback, **not** a CHoCH (see 2.3).
> **Q2.** Gold support 1,950–1,960 breaks with a daily close at 1,938. Price rallies to 1,952. You sell at 1,950, stop 1,962, target 1,914. Account 3,000 USD, risk 1%. R:R and size? (1 lot = 100 oz)
> > [!answer]-
> > Risk 12, reward 36 → **3R**. Risk budget 30 USD ÷ 12 USD per oz = 2.5 oz → round down to **0.02 lot (2 oz)** → actual risk **24 USD** (see 2.4, 0.4).
> **Q3.** Daily uptrend, daily demand 45–47, target 55. A 1H CHoCH up gives an entry at 47.0 with a stop at 44.5. R:R, and size for a 100 USD risk?
> > [!answer]-
> > Risk 2.5, reward 8.0 → **3.2R**; size 100 ÷ 2.5 = **40 units** (see 2.6).
""")
L.before_callout("en", "key", """
> [!check]- Final check: Phase 2
> **Q1.** What's the difference between a BOS and a CHoCH?
> > [!answer]-
> > A BOS is a close beyond a swing **in** the trend direction (continuation). A CHoCH is the first close beyond the **protected** swing against the trend (control may be changing).
> **Q2.** Why buy the retest of a broken level instead of chasing the breakout?
> > [!answer]-
> > Same idea and stop, but a much smaller risk and a much better R:R (about 6× in lesson 2.4's example). Missing a trade costs less than chasing it.
""")

# ---------------------------------------------------------------- TH
L.before_callout("th", "practice", """
> [!check]- โจทย์ฝึกคำนวณ: เฟส 2
> **Q1.** สวิงตามลำดับ: H 40, L 37, H 44, L 41, H 47, L 43 สภาวะคืออะไร จุดต่ำไหนถูกปกป้อง และการปิดที่ 42.5 หมายถึงอะไร?
> > [!answer]-
> > ขาขึ้น (HH + HL) Protected low คือ **41** จุดต่ำที่ HH ล่าสุด (47) สร้างขึ้นมา การปิดที่ 42.5 หลุดจุดต่ำล่าสุด (43) แต่ไม่หลุด 41: เป็นการย่อที่ลึกขึ้น **ไม่ใช่** CHoCH (ดู 2.3)
> **Q2.** แนวรับทองคำ 1,950–1,960 แตกด้วยราคาปิดรายวันที่ 1,938 ราคาเด้งขึ้นมาที่ 1,952 คุณขายที่ 1,950 Stop 1,962 เป้า 1,914 บัญชี 3,000 ดอลลาร์ เสี่ยง 1% R:R และขนาดเท่าไร? (1 ล็อต = 100 ออนซ์)
> > [!answer]-
> > เสี่ยง 12 ผลตอบแทน 36 → **3R** งบความเสี่ยง 30 ดอลลาร์ ÷ 12 ดอลลาร์ต่อออนซ์ = 2.5 ออนซ์ → ปัดลงเป็น **0.02 ล็อต (2 ออนซ์)** → ความเสี่ยงจริง **24 ดอลลาร์** (ดู 2.4, 0.4)
> **Q3.** รายวันขาขึ้น Demand รายวัน 45–47 เป้า 55 CHoCH ขึ้นบน 1H ให้จุดเข้า 47.0 Stop 44.5 R:R และขนาดสำหรับความเสี่ยง 100 ดอลลาร์?
> > [!answer]-
> > เสี่ยง 2.5 ผลตอบแทน 8.0 → **3.2R** ขนาด 100 ÷ 2.5 = **40 หน่วย** (ดู 2.6)
""")
L.before_callout("th", "key", """
> [!check]- ทดสอบสุดท้าย: เฟส 2
> **Q1.** BOS กับ CHoCH ต่างกันอย่างไร?
> > [!answer]-
> > BOS คือการปิดเลยสวิง **ใน** ทิศทางเทรนด์ (ไปต่อ) CHoCH คือการปิดครั้งแรกเลยสวิงที่ **ปกป้อง** เทรนด์ในทิศทางสวน (ผู้คุมเกมอาจกำลังเปลี่ยน)
> **Q2.** ทำไมควรซื้อตอนทดสอบซ้ำระดับที่แตก แทนการไล่ซื้อตอนทะลุ?
> > [!answer]-
> > ไอเดียและ Stop เดียวกัน แต่ความเสี่ยงเล็กกว่ามากและ R:R ดีกว่ามาก (ราว 6 เท่าในตัวอย่างของบทที่ 2.4) การพลาดเทรดเสียน้อยกว่าการไล่ซื้อ
""")

L.set_meta("level", "v2")
L.save()
