"""B9c · v2 upgrade of 3.6 Drawdown Math & Recovery (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("03 Risk & Money Management/3.6 Drawdown Math & Recovery.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> If you lose half your money, you have to double what's left just to get back to where you started. Small losses are easy to recover from; big ones take years. So the most important skill is keeping losses small, and having rules that make you bet even smaller when things are going badly.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Drawdown** — the % the account is below its highest peak.
> - **Equity peak** — the highest account value so far.
> - **Recovery gain** — the gain needed to return to the peak: loss ÷ (1 − loss).
> - **Streak drawdown** — the loss from n losses in a row: 1 − (1 − risk)ⁿ.
> - **Variance** — normal ups and downs of results, even with a real edge.
> - **Drawdown rules** — pre-set actions at set drawdown levels (halve risk, stop and review).
> - **Martingale** — doubling size after each loss to "win it back"; a path to ruin.
> - **Revenge trading** — bigger, worse trades right after a loss *(see 4.6)*.
""")
L.before_heading("en", "2.", """
> [!analogy]
> A drawdown is like **falling into a well**. A short fall, you climb out in a minute. A deep fall, and every extra metre makes the climb back much harder, while your arms get tired (your confidence). The best plan is to stop digging as soon as you notice you're sinking.
>
> **Where it breaks:** a well has a fixed depth. In markets you choose how deep you go, through your size and your rules.

> [!walkthrough] Step by step: measuring and repairing a drawdown
> 1. Account goes 10,000 → **11,000** (new peak) → **10,200**. Drawdown = 10,200 ÷ 11,000 − 1 = **−7.3%**, even though you're still up 2% overall.
> 2. To return to the peak: 11,000 ÷ 10,200 − 1 = **+7.8%**.
> 3. A **−35%** drawdown needs 0.35 ÷ 0.65 = **+53.8%** to recover.
> 4. **So what?** Always measure from the peak, and treat −20% as a hard line: below it, recovery takes far longer than the fall did.

> [!check]- Check your understanding: recovery maths
> **Q1.** Your account falls from 5,000 to 3,500. What's the drawdown, and what gain do you need?
> > [!answer]-
> > Drawdown = 1,500 ÷ 5,000 = **−30%**. Gain needed = 0.30 ÷ 0.70 ≈ **+42.9%**.
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: what streaks cost at 1% and 2%
> Streak drawdown = 1 − (1 − risk)ⁿ.
> 1. **1% risk:** 8 losses ≈ **−7.7%**, 10 ≈ **−9.6%**, 12 ≈ **−11.4%**.
> 2. **2% risk:** 8 losses ≈ **−14.9%**, 10 ≈ **−18.3%**, 12 ≈ **−21.5%**.
> 3. With the rule of thumb (worst drawdown ≈ 1.5–2× the worst streak), 2% risk and a 12-loss streak points to a real drawdown of roughly −30% to −40%.
> 4. **So what?** Pick the risk % whose realistic worst case you could live through without changing your rules.

> [!check]- Check your understanding: expected drawdown
> **Q1.** Your worst losing streak in a backtest is 9 trades. You risk 1%. Roughly what worst drawdown should you prepare for?
> > [!answer]-
> > Streak ≈ 1 − 0.99⁹ ≈ **−8.6%**; times 1.5–2 → plan for about **−13% to −17%**.
""")
L.before_callout("en", "action", """
![[p3-sizing-policies.en.svg]]

> [!walkthrough] Step by step: three ways to react to the same streak
> 8 losses in a row, then 6 wins at +2R, starting at **10,000 USD** with 1% risk.
> 1. **Fixed 1%:** worst **9,227** (−7.7%), end **10,392**.
> 2. **Halve to 0.5% at −5%:** worst **9,321** (−6.8%), end **10,292**. A shallower hole, slightly slower recovery.
> 3. **Double after each loss** (1%, 2%, 4% … 128%): after 7 losses the account is down to **1,762** and the next trade risks 128% of it, so the 8th loss takes it to **0**. The 6 wins never arrive for this trader.
> 4. **So what?** Cutting size costs a little upside; doubling risks everything. The streak itself was ordinary.

> [!check]- Check your understanding: drawdown rules
> **Q1.** You're 6% below your peak; your plan halves risk at −5%. A setup looks perfect. What size do you use?
> > [!answer]-
> > The reduced size (e.g. 0.5%). The rule exists for exactly this moment; "this one looks perfect" is not an exception.

> [!market]
> - **Forex:** leverage makes it easy to break the drawdown rules with one oversized trade *(see 0.3)*.
> - **Gold:** volatile weeks can push you into the "halve risk" level faster than expected *(see 0.4)*.
> - **Stocks:** a long bear market can mean months of drawdown for long-only strategies *(see 0.5, 10.7)*.
> - **Crypto:** drawdowns of 50%+ in the coins themselves are common; size so the account doesn't follow *(see 0.7)*.

> [!caution]
> Doubling size to "win it back" (martingale) or revenge trading after losses can take an account to zero in a single ordinary streak. Write your drawdown rules now and follow them mechanically.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** What gain is needed to recover from −20%, −50% and −75%?
> > [!answer]-
> > **+25%**, **+100%**, **+300%**.
> **Q2.** Why is cutting risk the right response both to bad luck and to a broken system?
> > [!answer]-
> > If it's bad luck, it costs little because you scale back up at a new high. If the system or your execution is broken, it protects capital while you find the problem.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ถ้าคุณเสียเงินไปครึ่งหนึ่ง คุณต้องทำให้ที่เหลือเพิ่มเป็นสองเท่าเพื่อกลับไปที่จุดเริ่ม การขาดทุนเล็ก ๆ ฟื้นง่าย การขาดทุนใหญ่ใช้เวลาหลายปี ทักษะสำคัญที่สุดจึงเป็นการทำให้การขาดทุนเล็ก และมีกฎที่บังคับให้คุณเดิมพันเล็กลงอีกเมื่อทุกอย่างกำลังแย่
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **Drawdown** — % ที่บัญชีอยู่ต่ำกว่าจุดสูงสุด
> - **จุดสูงสุดของพอร์ต (Equity peak)** — มูลค่าบัญชีสูงสุดจนถึงตอนนี้
> - **กำไรที่ต้องใช้ฟื้นตัว (Recovery gain)** — กำไรที่ต้องได้เพื่อกลับไปจุดสูงสุด: ขาดทุน ÷ (1 − ขาดทุน)
> - **Drawdown จากการแพ้ติดกัน (Streak drawdown)** — การขาดทุนจากการแพ้ n ไม้ติด: 1 − (1 − ความเสี่ยง)ⁿ
> - **ความแปรปรวน (Variance)** — การขึ้นลงตามปกติของผลลัพธ์ แม้มีความได้เปรียบจริง
> - **กฎ Drawdown (Drawdown rules)** — การกระทำที่กำหนดไว้ล่วงหน้าที่ระดับ Drawdown ต่าง ๆ (ลดความเสี่ยงครึ่งหนึ่ง หยุดและทบทวน)
> - **Martingale** — เพิ่มขนาดเป็นสองเท่าหลังแพ้แต่ละครั้งเพื่อ "เอาคืน" เป็นเส้นทางสู่พอร์ตพัง
> - **เทรดแก้แค้น (Revenge trading)** — เทรดใหญ่ขึ้นและแย่ลงทันทีหลังแพ้ *(ดู 4.6)*
""")
L.before_heading("th", "2.", """
> [!analogy]
> Drawdown เหมือน **การตกลงไปในบ่อ** ตกตื้น ๆ ปีนขึ้นได้ในนาทีเดียว ตกลึก ทุกเมตรที่เพิ่มทำให้ปีนกลับยากขึ้นมาก ขณะที่แขนเริ่มล้า (ความมั่นใจ) แผนที่ดีที่สุดคือหยุดขุดทันทีที่รู้ตัวว่ากำลังจม
>
> **จุดที่เปรียบเทียบไม่ได้:** บ่อมีความลึกตายตัว แต่ในตลาด คุณเลือกเองว่าจะลงลึกแค่ไหน ผ่านขนาดไม้และกฎของคุณ

> [!walkthrough] ไล่ทีละขั้น: วัดและซ่อม Drawdown
> 1. บัญชีจาก 10,000 → **11,000** (จุดสูงสุดใหม่) → **10,200** Drawdown = 10,200 ÷ 11,000 − 1 = **−7.3%** แม้โดยรวมยังกำไร 2%
> 2. กลับไปจุดสูงสุด: 11,000 ÷ 10,200 − 1 = **+7.8%**
> 3. Drawdown **−35%** ต้องได้ 0.35 ÷ 0.65 = **+53.8%** เพื่อฟื้น
> 4. **แล้วไง?** วัดจากจุดสูงสุดเสมอ และถือ −20% เป็นเส้นตาย ต่ำกว่านั้น การฟื้นใช้เวลานานกว่าการร่วงมาก

> [!check]- เช็กความเข้าใจ: คณิตศาสตร์การฟื้นตัว
> **Q1.** บัญชีลดจาก 5,000 เหลือ 3,500 Drawdown เท่าไร และต้องได้กำไรเท่าไร?
> > [!answer]-
> > Drawdown = 1,500 ÷ 5,000 = **−30%** กำไรที่ต้องได้ = 0.30 ÷ 0.70 ≈ **+42.9%**
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: การแพ้ติดกันมีราคาเท่าไรที่ 1% และ 2%
> Streak drawdown = 1 − (1 − ความเสี่ยง)ⁿ
> 1. **เสี่ยง 1%:** แพ้ 8 ไม้ ≈ **−7.7%** 10 ไม้ ≈ **−9.6%** 12 ไม้ ≈ **−11.4%**
> 2. **เสี่ยง 2%:** แพ้ 8 ไม้ ≈ **−14.9%** 10 ไม้ ≈ **−18.3%** 12 ไม้ ≈ **−21.5%**
> 3. ตามหลักคร่าว ๆ (Drawdown แย่สุด ≈ 1.5–2 เท่าของการแพ้ติดกันแย่สุด) เสี่ยง 2% กับการแพ้ 12 ไม้ติด ชี้ไปที่ Drawdown จริงราว −30% ถึง −40%
> 4. **แล้วไง?** เลือก % ความเสี่ยงที่กรณีแย่สุดที่สมจริง คุณผ่านไปได้โดยไม่เปลี่ยนกฎ

> [!check]- เช็กความเข้าใจ: Drawdown ที่ควรคาด
> **Q1.** การแพ้ติดกันแย่สุดในแบ็กเทสต์คือ 9 ไม้ คุณเสี่ยง 1% ควรเตรียมรับ Drawdown แย่สุดราวเท่าไร?
> > [!answer]-
> > Streak ≈ 1 − 0.99⁹ ≈ **−8.6%** คูณ 1.5–2 → เตรียมรับราว **−13% ถึง −17%**
""")
L.before_callout("th", "action", """
![[p3-sizing-policies.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: สามวิธีตอบสนองต่อการแพ้ติดกันชุดเดียวกัน
> แพ้ติดกัน 8 ไม้ แล้วชนะ 6 ไม้ที่ +2R เริ่มที่ **10,000 ดอลลาร์** เสี่ยง 1%
> 1. **คงที่ 1%:** ต่ำสุด **9,227** (−7.7%) จบที่ **10,392**
> 2. **ลดเหลือ 0.5% ที่ −5%:** ต่ำสุด **9,321** (−6.8%) จบที่ **10,292** หลุมตื้นกว่า ฟื้นช้าลงเล็กน้อย
> 3. **เพิ่มเท่าตัวหลังแพ้แต่ละครั้ง** (1%, 2%, 4% … 128%): หลังแพ้ 7 ไม้ บัญชีเหลือ **1,762** และไม้ถัดไปเสี่ยง 128% ของบัญชี การแพ้ไม้ที่ 8 จึงทำให้เหลือ **0** ไม้ชนะ 6 ไม้ไม่มีวันมาถึงสำหรับเทรดเดอร์คนนี้
> 4. **แล้วไง?** การลดขนาดเสียโอกาสขาขึ้นนิดหน่อย การเพิ่มเท่าตัวเสี่ยงทุกอย่าง ทั้งที่การแพ้ติดกันครั้งนี้เป็นเรื่องธรรมดา

> [!check]- เช็กความเข้าใจ: กฎ Drawdown
> **Q1.** คุณอยู่ต่ำกว่าจุดสูงสุด 6% แผนของคุณลดความเสี่ยงครึ่งหนึ่งที่ −5% มี Setup ที่ดูสมบูรณ์แบบ ใช้ขนาดเท่าไร?
> > [!answer]-
> > ขนาดที่ลดแล้ว (เช่น 0.5%) กฎมีไว้สำหรับช่วงเวลานี้พอดี "ไม้นี้ดูสมบูรณ์แบบ" ไม่ใช่ข้อยกเว้น

> [!market]
> - **ฟอเร็กซ์:** เลเวอเรจทำให้ฝ่ากฎ Drawdown ได้ง่ายด้วยไม้ใหญ่เกินไม้เดียว *(ดู 0.3)*
> - **ทองคำ:** สัปดาห์ที่ผันผวนอาจดันคุณถึงระดับ "ลดความเสี่ยงครึ่งหนึ่ง" เร็วกว่าที่คิด *(ดู 0.4)*
> - **หุ้น:** ตลาดหมีที่ยาวอาจหมายถึง Drawdown หลายเดือนสำหรับกลยุทธ์ที่ซื้ออย่างเดียว *(ดู 0.5, 10.7)*
> - **คริปโต:** ตัวเหรียญร่วง 50% ขึ้นไปเป็นเรื่องปกติ กำหนดขนาดให้บัญชีไม่ร่วงตาม *(ดู 0.7)*

> [!caution]
> การเพิ่มขนาดเป็นสองเท่าเพื่อ "เอาคืน" (Martingale) หรือการเทรดแก้แค้นหลังแพ้ ทำให้บัญชีเหลือศูนย์ได้ในการแพ้ติดกันธรรมดาเพียงครั้งเดียว เขียนกฎ Drawdown ตอนนี้ และทำตามอย่างเป็นกลไก
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** ต้องได้กำไรเท่าไรเพื่อฟื้นจาก −20%, −50% และ −75%?
> > [!answer]-
> > **+25%**, **+100%**, **+300%**
> **Q2.** ทำไมการลดความเสี่ยงจึงเป็นการตอบสนองที่ถูกต้อง ทั้งต่อโชคร้ายและต่อระบบที่พัง?
> > [!answer]-
> > ถ้าเป็นโชคร้าย มันเสียน้อยเพราะคุณกลับไปขนาดเต็มเมื่อทำจุดสูงสุดใหม่ ถ้าระบบหรือการปฏิบัติของคุณพัง มันปกป้องเงินทุนขณะที่คุณหาปัญหา
""")

L.set_meta("level", "v2")
L.save()
