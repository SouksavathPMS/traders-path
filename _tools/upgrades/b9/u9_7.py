"""B9f · v2 upgrade of 9.7 Checkpoint: Phase 9 Review (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("09 Quant & Data Analysis/9.7 Checkpoint- Phase 9 Review.md")

# ---------------------------------------------------------------- EN
L.before_callout("en", "practice", """
> [!check]- Worked problems: Phase 9
> **Q1.** A setup wins 22 of 40 trades (55%). Roughly what range could the true win rate be in (95%)?
> > [!answer]-
> > ± 1.96 × √(0.55 × 0.45 ÷ 40) ≈ ±0.15 → about **40% to 70%**. Not yet enough to call it better than 50% (see 9.1).
> **Q2.** A trade has a 35% chance of +2.5R, 25% chance of +0.3R and 40% chance of −1R, with costs of 0.05R per trade. EV?
> > [!answer]-
> > 0.35 × 2.5 + 0.25 × 0.3 − 0.40 × 1 − 0.05 = 0.875 + 0.075 − 0.40 − 0.05 = **+0.50R** (see 9.2).
> **Q3.** 80 trades: 30 winners averaging +1.8R, 50 losers at −1R. Profit factor and expectancy?
> > [!answer]-
> > Gross wins 54R, gross losses 50R → profit factor **1.08**; expectancy (54 − 50) ÷ 80 = **+0.05R**: barely positive, and costs could erase it (see 9.6).
""")
L.before_callout("en", "key", """
> [!check]- Final check: Phase 9
> **Q1.** Name three ways a backtest can lie, and the fix for each.
> > [!answer]-
> > For example: look-ahead bias (only use data available at the decision time); ignoring costs (include spread, commission, slippage); overfitting (keep an out-of-sample period, use walk-forward) (see 9.3).
> **Q2.** Why must every performance metric come with a trade count?
> > [!answer]-
> > Small samples give extreme, unreliable numbers (e.g. profit factor 12 from 3 trades). The trade count tells you how much luck could be in the result.
""")

# ---------------------------------------------------------------- TH
L.before_callout("th", "practice", """
> [!check]- โจทย์ฝึกคำนวณ: เฟส 9
> **Q1.** Setup ชนะ 22 จาก 40 ไม้ (55%) อัตราชนะจริงอาจอยู่ในช่วงประมาณเท่าไร (95%)?
> > [!answer]-
> > ± 1.96 × √(0.55 × 0.45 ÷ 40) ≈ ±0.15 → ราว **40% ถึง 70%** ยังไม่พอจะบอกว่าดีกว่า 50% (ดู 9.1)
> **Q2.** เทรดหนึ่งมีโอกาส 35% ที่ +2.5R โอกาส 25% ที่ +0.3R และโอกาส 40% ที่ −1R ต้นทุน 0.05R ต่อไม้ EV เท่าไร?
> > [!answer]-
> > 0.35 × 2.5 + 0.25 × 0.3 − 0.40 × 1 − 0.05 = 0.875 + 0.075 − 0.40 − 0.05 = **+0.50R** (ดู 9.2)
> **Q3.** 80 ไม้: ชนะ 30 ไม้เฉลี่ย +1.8R แพ้ 50 ไม้ที่ −1R Profit factor และค่าคาดหวังเท่าไร?
> > [!answer]-
> > กำไรรวม 54R ขาดทุนรวม 50R → Profit factor **1.08** ค่าคาดหวัง (54 − 50) ÷ 80 = **+0.05R**: บวกเพียงเล็กน้อย และต้นทุนอาจลบมันหมด (ดู 9.6)
""")
L.before_callout("th", "key", """
> [!check]- ทดสอบสุดท้าย: เฟส 9
> **Q1.** บอกสามวิธีที่แบ็กเทสต์โกหกได้ และวิธีแก้แต่ละข้อ
> > [!answer]-
> > ตัวอย่าง: Look-ahead bias (ใช้เฉพาะข้อมูลที่มีในเวลาตัดสินใจ) ไม่คิดต้นทุน (รวม Spread ค่าคอมมิชชัน Slippage) Overfitting (เก็บช่วง Out-of-sample ไว้ ใช้ Walk-forward) (ดู 9.3)
> **Q2.** ทำไมตัวชี้วัดผลงานทุกตัวต้องมาพร้อมจำนวนไม้?
> > [!answer]-
> > ตัวอย่างเล็กให้ตัวเลขสุดโต่งที่เชื่อไม่ได้ (เช่น Profit factor 12 จาก 3 ไม้) จำนวนไม้บอกว่าผลลัพธ์อาจมีโชคปนอยู่มากแค่ไหน
""")

L.set_meta("level", "v2")
L.save()
