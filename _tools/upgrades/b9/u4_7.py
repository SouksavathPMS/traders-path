"""B9d · v2 upgrade of 4.7 Checkpoint: Phase 4 Review (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("04 Psychology & Execution/4.7 Checkpoint- Phase 4 Review.md")

# ---------------------------------------------------------------- EN
L.before_callout("en", "practice", """
> [!check]- Worked problems: Phase 4
> **Q1.** The plan: 45% wins at +2R, losses −1R. Fear makes you close 40% of winners at +0.5R. New average win and expectancy?
> > [!answer]-
> > Average win = 0.6 × 2 + 0.4 × 0.5 = **1.4R**. Expectancy = 0.45 × 1.4 − 0.55 = **+0.08R**, down from +0.35R (see 4.1).
> **Q2.** Planned EUR/USD long: entry 1.0850, stop 1.0820, target 1.0940. You miss it and chase at 1.0870. R:R before and after, and the new break-even win rate?
> > [!answer]-
> > Planned: 90 ÷ 30 = **3.0**. Chased: 70 ÷ 50 = **1.4** → break-even 1 ÷ 2.4 ≈ **42%** (was 25%) (see 4.3).
> **Q3.** A week: 5 A-grade trades = +2.0R, 2 C-grade trades = −2.5R. Total, and what to work on?
> > [!answer]-
> > Total **−0.5R**. The plan made +2.0R; the two rule-breaks cost 2.5R. Work on the C-trade tags, not the system (see 4.5).
> **Q4.** Northern winter. When is an FOMC decision (14:00 New York) in UTC+7, and what's a 30-minute no-trade window around it?
> > [!answer]-
> > **02:00** UTC+7; no new entries **01:30–02:30** (see 4.4, 10.3).
""")
L.before_callout("en", "key", """
> [!check]- Final check: Phase 4
> **Q1.** Name two personal Amber signs and the rule that applies at Amber.
> > [!answer]-
> > For example: checking P&L every minute, skipping a checklist item, clicking faster, annoyance at the market. Rule: pause 15 minutes; next trade half size, A-grade only.
> **Q2.** When are you allowed to change your plan's rules?
> > [!answer]-
> > Only at scheduled reviews (weekly/monthly), one rule at a time, measured over enough trades. Never mid-week or after a single loss.
""")

# ---------------------------------------------------------------- TH
L.before_callout("th", "practice", """
> [!check]- โจทย์ฝึกคำนวณ: เฟส 4
> **Q1.** แผน: ชนะ 45% ที่ +2R แพ้ −1R ความกลัวทำให้คุณปิดไม้ชนะ 40% ที่ +0.5R กำไรเฉลี่ยและค่าคาดหวังใหม่เท่าไร?
> > [!answer]-
> > กำไรเฉลี่ย = 0.6 × 2 + 0.4 × 0.5 = **1.4R** ค่าคาดหวัง = 0.45 × 1.4 − 0.55 = **+0.08R** ลดลงจาก +0.35R (ดู 4.1)
> **Q2.** แผนซื้อ EUR/USD: เข้า 1.0850 Stop 1.0820 เป้า 1.0940 คุณพลาดและไล่เข้าที่ 1.0870 R:R ก่อนและหลัง และอัตราชนะคุ้มทุนใหม่?
> > [!answer]-
> > ตามแผน: 90 ÷ 30 = **3.0** ไล่ราคา: 70 ÷ 50 = **1.4** → คุ้มทุน 1 ÷ 2.4 ≈ **42%** (เดิม 25%) (ดู 4.3)
> **Q3.** หนึ่งสัปดาห์: ไม้เกรด A 5 ไม้ = +2.0R ไม้เกรด C 2 ไม้ = −2.5R รวมเท่าไร และควรแก้อะไร?
> > [!answer]-
> > รวม **−0.5R** แผนทำได้ +2.0R การผิดกฎสองครั้งเสีย 2.5R แก้ที่แท็กของไม้เกรด C ไม่ใช่ที่ระบบ (ดู 4.5)
> **Q4.** ช่วงฤดูหนาวซีกโลกเหนือ ผลประชุม FOMC (14:00 นิวยอร์ก) คือกี่โมงใน UTC+7 และช่วงห้ามเทรด 30 นาทีรอบนั้นคือช่วงไหน?
> > [!answer]-
> > **02:00** UTC+7 ไม่เข้าไม้ใหม่ช่วง **01:30–02:30** (ดู 4.4, 10.3)
""")
L.before_callout("th", "key", """
> [!check]- ทดสอบสุดท้าย: เฟส 4
> **Q1.** บอกสัญญาณเหลืองอำพันเฉพาะตัวสองข้อ และกฎที่ใช้ในระดับนั้น
> > [!answer]-
> > ตัวอย่าง: เช็ก P&L ทุกนาที ข้ามรายการในเช็กลิสต์ คลิกเร็วขึ้น หงุดหงิดกับตลาด กฎ: พัก 15 นาที ไม้ถัดไปครึ่งขนาด เกรด A เท่านั้น
> **Q2.** คุณเปลี่ยนกฎในแผนได้เมื่อไร?
> > [!answer]-
> > เฉพาะในการทบทวนตามกำหนด (รายสัปดาห์/รายเดือน) ทีละหนึ่งกฎ และวัดผลในจำนวนไม้ที่มากพอ ห้ามเปลี่ยนกลางสัปดาห์หรือหลังแพ้ไม้เดียว
""")

L.set_meta("level", "v2")
L.save()
