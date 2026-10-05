"""B9c · v2 upgrade of 3.1 Why Risk Comes First (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("03 Risk & Money Management/3.1 Why Risk Comes First.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Even a good method loses many times in a row sometimes. If you bet a big part of your money on each trade, one of those bad runs can wipe you out before the good runs arrive. If you bet only a small slice each time, you survive the bad runs and the method has time to work. Small bets are not timid; they are how you stay in the game.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Risk per trade** — the % of the account you lose if the stop is hit.
> - **1R** — that amount in money *(see 3.3)*.
> - **Fixed-fractional risk** — risking the same % of the current account on every trade.
> - **Drawdown** — how far the account is below its highest point *(see 3.6)*.
> - **Losing streak** — several losses in a row *(see 1.1)*.
> - **Compounding** — each loss (or gain) is a % of a smaller (or bigger) account than the last.
> - **Ruin** — losing so much that you can't or won't continue.
> - **Open risk** — the total you would lose if every open trade hit its stop.
> - **Correlated trades** — trades that tend to win or lose together.
> - **Daily loss limit** — the loss after which you stop trading for the day.
""")
L.before_heading("en", "2.", """
> [!analogy]
> Risk per trade is like the **speed you ride a motorbike on a long mountain road with few fuel stations**. Ride flat-out and you might get far quickly, but you run dry before the next station. Ride steadily and you always reach the next one.
>
> **Where it breaks:** fuel stations are on the map. Losing streaks aren't: you don't know when the next win comes, so you must ride as if the next station is far away.

![[p3-dd-odds.en.svg]]

> [!walkthrough] Step by step: what size does to the same edge
> Same system as section 1 (45% wins at +2R), 200 trades, 20,000 computer simulations per column.
> 1. **Risk 1%:** chance of a −20% drawdown from the peak ≈ **0.7%**; a −50% drawdown ≈ **0%**.
> 2. **Risk 2%:** −20% drawdown ≈ **36%**.
> 3. **Risk 3%:** −20% ≈ **82%**. **Risk 5%:** −20% is almost certain, and −50% ≈ **18%**.
> 4. **Risk 10%:** −50% ≈ **94%**: the edge is still there, but the account usually isn't.
> 5. **So what?** You don't choose whether bad streaks happen. You choose how much they cost.

> [!check]- Check your understanding: same system, different size
> **Q1.** Two traders use the same profitable system. One risks 1%, the other 10%. Why can the second one lose everything?
> > [!answer]-
> > Losing streaks are certain. At 10% per trade, an ordinary 8-loss streak takes the account down about 57%; the deeper the hole, the harder the recovery, and many traders break their rules on the way.
""")
L.before_heading("en", "3.", """
> [!walkthrough] Step by step: pricing a 10-loss streak
> 1. At **1%**, each loss is 1% of what's left: 0.99¹⁰ ≈ 0.904 → **−9.6%**. To get back: 1 ÷ 0.904 − 1 ≈ **+10.6%**.
> 2. At **5%**: 0.95¹⁰ ≈ 0.599 → **−40.1%**. To get back: **+67%**.
> 3. Same streak, same system: one is a bad month, the other may take years to repair *(see 3.6)*.
> 4. **So what?** Before you choose a risk %, calculate what a 10-loss streak would cost and ask whether you could keep following your rules at that level.

> [!check]- Check your understanding: streaks
> **Q1.** With a 40% win rate, roughly how likely is a streak of 8+ losses within 100 trades?
> > [!answer]-
> > About **49%**, roughly a coin flip (see the table above). Plan for it.
""")
L.before_callout("en", "example", """
> [!check]- Check your understanding: the four rules
> **Q1.** You have 1% open on each of three longs: two US tech stocks and the Nasdaq index. Your max open risk is 3%. Are you within the rule?
> > [!answer]-
> > On paper yes (3%), but all three tend to move together, so it behaves like one 3% bet on tech. If your rule treats correlated trades as one, you're at the limit for a single idea.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** high leverage makes it easy to risk far more than 1% by accident; always size from the stop *(see 0.3, 3.2)*.
> - **Gold:** large daily ranges; a "small" 0.10-lot position can be a big % of a small account *(see 0.4)*.
> - **Stocks:** overnight gaps can jump past your stop, so a 1% plan can become a 2–3% loss *(see 0.5)*.
> - **Crypto:** 24/7 moves and weekend crashes; many traders cut risk per trade here *(see 0.7)*.

> [!caution]
> Risking 5–10% per trade, adding to losers, or holding many correlated positions can empty an account within weeks, even with a good method. Leverage magnifies all of this. Start at 0.5% per trade.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Account 8,000 USD, risk 0.5%. What's your 1R, and what would 10 losses in a row cost (compounded)?
> > [!answer]-
> > 1R = **40 USD**. 0.995¹⁰ ≈ 0.951 → about **−4.9%** (≈ 390 USD).
> **Q2.** Why does large risk per trade make a good system worse in practice, not better?
> > [!answer]-
> > It doesn't change the edge, only the damage from streaks: deeper drawdowns, much larger gains needed to recover, and more emotional mistakes.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> แม้วิธีที่ดีก็แพ้ติดกันหลายครั้งได้เป็นบางครั้ง ถ้าคุณเดิมพันเงินส่วนใหญ่ในแต่ละไม้ ช่วงแย่ ๆ ครั้งหนึ่งอาจล้างพอร์ตก่อนช่วงดีจะมาถึง ถ้าคุณเดิมพันแค่ส่วนเล็ก ๆ ทุกครั้ง คุณจะรอดช่วงแย่ และวิธีการก็มีเวลาทำงาน การเดิมพันเล็กไม่ใช่ความขี้ขลาด แต่เป็นวิธีที่คุณจะอยู่ในเกมได้
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **ความเสี่ยงต่อไม้ (Risk per trade)** — % ของบัญชีที่เสียถ้าโดน Stop
> - **1R** — จำนวนเงินนั้น *(ดู 3.3)*
> - **ความเสี่ยงแบบสัดส่วนคงที่ (Fixed-fractional risk)** — เสี่ยง % เดิมของบัญชีปัจจุบันทุกไม้
> - **Drawdown** — บัญชีอยู่ต่ำกว่าจุดสูงสุดเท่าไร *(ดู 3.6)*
> - **แพ้ติดกัน (Losing streak)** — แพ้หลายไม้ติดต่อกัน *(ดู 1.1)*
> - **การทบต้น (Compounding)** — การขาดทุน (หรือกำไร) แต่ละครั้งเป็น % ของบัญชีที่เล็กลง (หรือใหญ่ขึ้น) กว่าครั้งก่อน
> - **พอร์ตพัง (Ruin)** — เสียมากจนไปต่อไม่ได้หรือไม่อยากไปต่อ
> - **ความเสี่ยงที่เปิดอยู่ (Open risk)** — ยอดรวมที่จะเสียถ้าทุกไม้ที่เปิดอยู่โดน Stop
> - **ไม้ที่สัมพันธ์กัน (Correlated trades)** — ไม้ที่มักชนะหรือแพ้พร้อมกัน
> - **ขีดจำกัดขาดทุนรายวัน (Daily loss limit)** — ขาดทุนถึงระดับนี้แล้วหยุดเทรดในวันนั้น
""")
L.before_heading("th", "2.", """
> [!analogy]
> ความเสี่ยงต่อไม้เหมือน **ความเร็วที่คุณขี่มอเตอร์ไซค์บนถนนภูเขายาว ๆ ที่มีปั๊มน้ำมันน้อย** บิดเต็มที่อาจไปได้ไกลเร็ว แต่น้ำมันหมดก่อนถึงปั๊มถัดไป ขี่สม่ำเสมอแล้วคุณจะถึงปั๊มถัดไปเสมอ
>
> **จุดที่เปรียบเทียบไม่ได้:** ปั๊มน้ำมันมีอยู่บนแผนที่ แต่การแพ้ติดกันไม่มี คุณไม่รู้ว่าไม้ชนะถัดไปจะมาเมื่อไร จึงต้องขี่เหมือนปั๊มถัดไปอยู่ไกล

![[p3-dd-odds.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ขนาดไม้ทำอะไรกับความได้เปรียบเดียวกัน
> ระบบเดียวกับหัวข้อ 1 (ชนะ 45% ได้ +2R) 200 ไม้ จำลองด้วยคอมพิวเตอร์คอลัมน์ละ 20,000 ครั้ง
> 1. **เสี่ยง 1%:** โอกาส Drawdown −20% จากจุดสูงสุด ≈ **0.7%** Drawdown −50% ≈ **0%**
> 2. **เสี่ยง 2%:** Drawdown −20% ≈ **36%**
> 3. **เสี่ยง 3%:** −20% ≈ **82%** **เสี่ยง 5%:** −20% แทบแน่นอน และ −50% ≈ **18%**
> 4. **เสี่ยง 10%:** −50% ≈ **94%**: ความได้เปรียบยังอยู่ แต่บัญชีมักไม่อยู่แล้ว
> 5. **แล้วไง?** คุณเลือกไม่ได้ว่าช่วงแย่จะเกิดหรือไม่ แต่เลือกได้ว่ามันจะแพงแค่ไหน

> [!check]- เช็กความเข้าใจ: ระบบเดียวกัน ขนาดต่างกัน
> **Q1.** เทรดเดอร์สองคนใช้ระบบที่ทำกำไรระบบเดียวกัน คนหนึ่งเสี่ยง 1% อีกคน 10% ทำไมคนที่สองจึงเสียทั้งหมดได้?
> > [!answer]-
> > การแพ้ติดกันเกิดขึ้นแน่นอน ที่ 10% ต่อไม้ การแพ้ 8 ไม้ติดตามปกติทำให้บัญชีลดลงราว 57% หลุมยิ่งลึก ยิ่งฟื้นยาก และนักเทรดจำนวนมากทำผิดกฎระหว่างทาง
""")
L.before_heading("th", "3.", """
> [!walkthrough] ไล่ทีละขั้น: คิดราคาการแพ้ 10 ไม้ติด
> 1. ที่ **1%** แต่ละครั้งเสีย 1% ของที่เหลือ: 0.99¹⁰ ≈ 0.904 → **−9.6%** ต้องได้คืน: 1 ÷ 0.904 − 1 ≈ **+10.6%**
> 2. ที่ **5%**: 0.95¹⁰ ≈ 0.599 → **−40.1%** ต้องได้คืน: **+67%**
> 3. การแพ้ติดกันเดียวกัน ระบบเดียวกัน: แบบหนึ่งคือเดือนที่แย่ อีกแบบอาจใช้เวลาหลายปีซ่อม *(ดู 3.6)*
> 4. **แล้วไง?** ก่อนเลือก % ความเสี่ยง ให้คำนวณว่าการแพ้ 10 ไม้ติดจะเสียเท่าไร และถามตัวเองว่าจะยังทำตามกฎได้ไหมที่ระดับนั้น

> [!check]- เช็กความเข้าใจ: การแพ้ติดกัน
> **Q1.** ที่อัตราชนะ 40% โอกาสแพ้ติดกัน 8 ไม้ขึ้นไปใน 100 ไม้ประมาณเท่าไร?
> > [!answer]-
> > ราว **49%** พอ ๆ กับการโยนเหรียญ (ดูตารางด้านบน) วางแผนรับไว้
""")
L.before_callout("th", "example", """
> [!check]- เช็กความเข้าใจ: กฎ 4 ข้อ
> **Q1.** คุณเปิดไม้ซื้อสามไม้ ไม้ละ 1%: หุ้นเทคสหรัฐสองตัวและดัชนี Nasdaq ขีดจำกัดความเสี่ยงที่เปิดอยู่คือ 3% อยู่ในกฎไหม?
> > [!answer]-
> > ตามตัวเลขอยู่ (3%) แต่ทั้งสามมักขยับไปด้วยกัน จึงเหมือนเดิมพันหุ้นเทค 3% ก้อนเดียว ถ้ากฎของคุณนับไม้ที่สัมพันธ์กันเป็นหนึ่ง คุณถึงขีดจำกัดสำหรับไอเดียเดียวแล้ว
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** เลเวอเรจสูงทำให้เผลอเสี่ยงเกิน 1% ได้ง่าย คำนวณขนาดจาก Stop เสมอ *(ดู 0.3, 3.2)*
> - **ทองคำ:** กรอบรายวันกว้าง โพซิชัน "เล็ก ๆ" 0.10 ล็อตอาจเป็น % ใหญ่ของบัญชีเล็ก *(ดู 0.4)*
> - **หุ้น:** Gap ข้ามคืนอาจกระโดดข้าม Stop แผน 1% จึงกลายเป็นขาดทุน 2–3% ได้ *(ดู 0.5)*
> - **คริปโต:** ขยับ 24/7 และร่วงหนักช่วงสุดสัปดาห์ นักเทรดจำนวนมากลดความเสี่ยงต่อไม้ในตลาดนี้ *(ดู 0.7)*

> [!caution]
> การเสี่ยง 5–10% ต่อไม้ การถัวไม้ที่ขาดทุน หรือการถือหลายโพซิชันที่สัมพันธ์กัน ล้างบัญชีได้ภายในไม่กี่สัปดาห์ แม้วิธีจะดี เลเวอเรจขยายทั้งหมดนี้ เริ่มที่ 0.5% ต่อไม้
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บัญชี 8,000 ดอลลาร์ เสี่ยง 0.5% 1R เท่าไร และแพ้ 10 ไม้ติด (แบบทบต้น) เสียเท่าไร?
> > [!answer]-
> > 1R = **40 ดอลลาร์** 0.995¹⁰ ≈ 0.951 → ราว **−4.9%** (≈ 390 ดอลลาร์)
> **Q2.** ทำไมความเสี่ยงต่อไม้ที่สูงทำให้ระบบที่ดีแย่ลงในทางปฏิบัติ ไม่ใช่ดีขึ้น?
> > [!answer]-
> > มันไม่เปลี่ยนความได้เปรียบ แต่เพิ่มความเสียหายจากการแพ้ติดกัน: Drawdown ลึกขึ้น ต้องได้กำไรมากขึ้นมากเพื่อฟื้น และทำผิดพลาดทางอารมณ์มากขึ้น
""")

L.set_meta("level", "v2")
L.save()
