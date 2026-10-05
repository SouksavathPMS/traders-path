"""B9f · v2 upgrade of 8.8 Checkpoint: Phase 8 Review (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("08 Options & Dealer Positioning/8.8 Checkpoint- Phase 8 Review.md")

# ---------------------------------------------------------------- EN
L.before_callout("en", "practice", """
> [!check]- Worked problems: Phase 8
> **Q1.** You buy a 4,900 put on an index for 35 points. At expiry the index is at 4,820, or at 4,880. Result per point in each case, and the break-even?
> > [!answer]-
> > At 4,820: intrinsic 80 − 35 = **+45**. At 4,880: intrinsic 20 − 35 = **−15**. Break-even = 4,900 − 35 = **4,865** (see 8.1).
> **Q2.** A call has delta 0.40 and gamma 0.03. The stock rises 3. New delta? For 10 contracts (100 shares each), how many shares of exposure before and after?
> > [!answer]-
> > Delta ≈ 0.40 + 0.03 × 3 = **0.49**. Exposure 10 × 100 × 0.40 = **400** shares → 10 × 100 × 0.49 = **490** shares (see 8.2).
> **Q3.** Dealers are short 2,000 calls (100 shares each) with delta 0.50, hedged with stock. Price rises and the delta becomes 0.60. What must they do?
> > [!answer]-
> > Hedge = 2,000 × 100 × 0.50 = **100,000** shares long; needed now 120,000 → **buy 20,000 more** into the rally. Short gamma means buying strength and selling weakness, which amplifies moves (see 8.3).
""")
L.before_callout("en", "key", """
> [!check]- Final check: Phase 8
> **Q1.** Above vs below the gamma flip: which tactics fit each?
> > [!answer]-
> > Above (positive gamma): calmer, mean-reverting: fade the edges, take profits quickly. Below (negative gamma): faster, trending: smaller size, wider stops, follow breaks (see 8.4).
> **Q2.** Why are GEX levels and options flow only context, never a trigger?
> > [!answer]-
> > They are estimates built on assumptions (who is long or short, daily open interest) and don't give direction on their own; the trade still needs your structure setup and risk plan (see 8.4, 8.7).
""")

# ---------------------------------------------------------------- TH
L.before_callout("th", "practice", """
> [!check]- โจทย์ฝึกคำนวณ: เฟส 8
> **Q1.** คุณซื้อ Put ราคาใช้สิทธิ 4,900 ของดัชนีที่ 35 จุด ตอนหมดอายุดัชนีอยู่ที่ 4,820 หรือ 4,880 ผลต่อจุดในแต่ละกรณี และจุดคุ้มทุน?
> > [!answer]-
> > ที่ 4,820: มูลค่าที่แท้จริง 80 − 35 = **+45** ที่ 4,880: 20 − 35 = **−15** จุดคุ้มทุน = 4,900 − 35 = **4,865** (ดู 8.1)
> **Q2.** Call มี Delta 0.40 และ Gamma 0.03 หุ้นขึ้น 3 Delta ใหม่เท่าไร? สำหรับ 10 สัญญา (สัญญาละ 100 หุ้น) ความเสี่ยงเทียบเป็นหุ้นก่อนและหลังเท่าไร?
> > [!answer]-
> > Delta ≈ 0.40 + 0.03 × 3 = **0.49** ความเสี่ยง 10 × 100 × 0.40 = **400** หุ้น → 10 × 100 × 0.49 = **490** หุ้น (ดู 8.2)
> **Q3.** ดีลเลอร์ Short Call 2,000 สัญญา (สัญญาละ 100 หุ้น) Delta 0.50 และป้องกันความเสี่ยงด้วยหุ้น ราคาขึ้นและ Delta กลายเป็น 0.60 พวกเขาต้องทำอะไร?
> > [!answer]-
> > การป้องกัน = 2,000 × 100 × 0.50 = **100,000** หุ้นฝั่งซื้อ ตอนนี้ต้องมี 120,000 → **ซื้อเพิ่ม 20,000** ในขาขึ้น Short gamma หมายถึงซื้อตอนแข็งและขายตอนอ่อน ซึ่งขยายการขยับ (ดู 8.3)
""")
L.before_callout("th", "key", """
> [!check]- ทดสอบสุดท้าย: เฟส 8
> **Q1.** เหนือ vs ใต้ Gamma flip: กลยุทธ์ไหนเหมาะกับแต่ละฝั่ง?
> > [!answer]-
> > เหนือ (Gamma บวก): สงบกว่า กลับสู่ค่าเฉลี่ย: เทรดสวนที่ขอบ ทำกำไรเร็ว ใต้ (Gamma ลบ): เร็วกว่า เป็นเทรนด์: ขนาดเล็กลง Stop กว้างขึ้น ตามการทะลุ (ดู 8.4)
> **Q2.** ทำไมระดับ GEX และ Options flow จึงเป็นแค่บริบท ไม่ใช่สัญญาณเข้า?
> > [!answer]-
> > เป็นการประมาณบนสมมติฐาน (ใครซื้อใครขาย Open interest รายวัน) และไม่ได้บอกทิศทางด้วยตัวเอง เทรดยังต้องมี Setup ตามโครงสร้างและแผนความเสี่ยงของคุณ (ดู 8.4, 8.7)
""")

L.set_meta("level", "v2")
L.save()
