"""B9c · v2 upgrade of 3.7 Checkpoint: Phase 3 Review (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("03 Risk & Money Management/3.7 Checkpoint- Phase 3 Review.md")

# ---------------------------------------------------------------- EN
L.before_callout("en", "practice", """
> [!check]- Worked problems: Phase 3
> **Q1.** Account 15,000 USD, risk 0.75%. Long a stock at 84.20 with a stop at 82.60. How many shares?
> > [!answer]-
> > 1R = 15,000 × 0.0075 = **112.50 USD**. Risk per share 1.60 → 112.50 ÷ 1.60 = 70.3 → **70 shares** (actual risk 112 USD) (see 3.2).
> **Q2.** 38% win rate, average win +2.4R, average loss −1.05R. Expectancy, and the result of 100 trades at 1R = 100 USD?
> > [!answer]-
> > 0.38 × 2.4 − 0.62 × 1.05 = 0.912 − 0.651 = **+0.26R** per trade → about **+26R ≈ +2,610 USD** over 100 trades (see 3.4).
> **Q3.** Equity peak 12,400 USD, account now 11,000 USD. Your rules: halve at −5%, stop and review at −10%. What's the drawdown, and what do you do?
> > [!answer]-
> > 11,000 ÷ 12,400 − 1 ≈ **−11.3%** → **stop live trading and review**. You need +12.7% to get back to the peak (see 3.6).
> **Q4.** Short EUR/USD at 1.0880. Swing high 1.0912, ATR 0.0020, buffer 0.25 × ATR. Risk 50 USD, 10 USD per pip per lot. Stop and size?
> > [!answer]-
> > Stop = 1.0912 + 0.0005 = **1.0917** → 37 pips. Size = 50 ÷ (37 × 10) = 0.135 → **0.13 lot** (risk ≈ 48 USD) (see 3.5).
""")
L.before_callout("en", "key", """
> [!check]- Final check: Phase 3
> **Q1.** Why must you take at least 30 trades with one exit method before judging it?
> > [!answer]-
> > A handful of trades is mostly luck; streaks of 6–8 losses are normal. Only a larger sample gives an expectancy you can trust (and 100+ is better).
> **Q2.** In one line each: what decides the stop, the target and the size?
> > [!answer]-
> > Stop: the structure that proves the idea wrong, plus a buffer. Target: the next real opposing level. Size: 1R ÷ stop distance.
""")

# ---------------------------------------------------------------- TH
L.before_callout("th", "practice", """
> [!check]- โจทย์ฝึกคำนวณ: เฟส 3
> **Q1.** บัญชี 15,000 ดอลลาร์ เสี่ยง 0.75% ซื้อหุ้นที่ 84.20 Stop ที่ 82.60 ได้กี่หุ้น?
> > [!answer]-
> > 1R = 15,000 × 0.0075 = **112.50 ดอลลาร์** เสี่ยงต่อหุ้น 1.60 → 112.50 ÷ 1.60 = 70.3 → **70 หุ้น** (เสี่ยงจริง 112 ดอลลาร์) (ดู 3.2)
> **Q2.** อัตราชนะ 38% กำไรเฉลี่ย +2.4R ขาดทุนเฉลี่ย −1.05R ค่าคาดหวังเท่าไร และผลของ 100 ไม้ที่ 1R = 100 ดอลลาร์?
> > [!answer]-
> > 0.38 × 2.4 − 0.62 × 1.05 = 0.912 − 0.651 = **+0.26R** ต่อไม้ → ราว **+26R ≈ +2,610 ดอลลาร์** ใน 100 ไม้ (ดู 3.4)
> **Q3.** จุดสูงสุดของพอร์ต 12,400 ดอลลาร์ ตอนนี้ 11,000 ดอลลาร์ กฎของคุณ: ลดครึ่งที่ −5% หยุดและทบทวนที่ −10% Drawdown เท่าไร และทำอะไร?
> > [!answer]-
> > 11,000 ÷ 12,400 − 1 ≈ **−11.3%** → **หยุดเทรดจริงและทบทวน** ต้องได้ +12.7% เพื่อกลับไปจุดสูงสุด (ดู 3.6)
> **Q4.** ขาย EUR/USD ที่ 1.0880 จุดสวิงสูง 1.0912 ATR 0.0020 ระยะเผื่อ 0.25 × ATR เสี่ยง 50 ดอลลาร์ 10 ดอลลาร์ต่อ pip ต่อล็อต Stop และขนาด?
> > [!answer]-
> > Stop = 1.0912 + 0.0005 = **1.0917** → 37 pip ขนาด = 50 ÷ (37 × 10) = 0.135 → **0.13 ล็อต** (เสี่ยง ≈ 48 ดอลลาร์) (ดู 3.5)
""")
L.before_callout("th", "key", """
> [!check]- ทดสอบสุดท้าย: เฟส 3
> **Q1.** ทำไมต้องเทรดอย่างน้อย 30 ไม้ด้วยวิธีออกแบบเดียวก่อนตัดสิน?
> > [!answer]-
> > ไม่กี่ไม้ส่วนใหญ่คือโชค การแพ้ติดกัน 6–8 ไม้เป็นเรื่องปกติ ตัวอย่างที่ใหญ่ขึ้นเท่านั้นจึงให้ค่าคาดหวังที่เชื่อได้ (100 ไม้ขึ้นไปดีกว่า)
> **Q2.** ตอบข้อละบรรทัด: อะไรกำหนด Stop เป้า และขนาด?
> > [!answer]-
> > Stop: โครงสร้างที่พิสูจน์ว่าไอเดียผิด บวกระยะเผื่อ เป้า: ระดับฝั่งตรงข้ามจริงถัดไป ขนาด: 1R ÷ ระยะ Stop
""")

L.set_meta("level", "v2")
L.save()
