"""B9d · v2 upgrade of 4.1 Fear, Greed, Hope & Regret (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("04 Psychology & Execution/4.1 Fear, Greed, Hope & Regret.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> Every trade stirs up feelings: fear of losing, greed for more, hope that a loser comes back, regret about a missed move. Those feelings push you to break your plan at exactly the wrong moments. You can't stop feeling them, but you can notice them, give them a name, and then do what your written plan says.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Fear** — worry about losing; makes you skip setups or exit winners early.
> - **Greed** — wanting more; makes you oversize, chase and overtrade.
> - **Hope** — believing a loser will come back; makes you hold losers and move stops.
> - **Regret** — pain about a missed or lost trade; leads to revenge trades and chasing.
> - **FOMO (fear of missing out)** — the urge to jump in because a move is running without you.
> - **Euphoria / capitulation** — the crowd's extreme optimism near tops / giving up near bottoms.
> - **Emotional state score** — a 1–5 self-rating before trading (1 = calm, 5 = agitated).
> - **Average win** — the average R of winning trades *(see 3.3)*.
""")
L.before_heading("en", "2.", """
> [!analogy]
> Emotions while trading are like a **loud passenger in the back seat**. They shout "Faster!", "Turn here!", "Stop!" You can't throw them out of the car, but you don't have to hand them the steering wheel. You hear them, then you follow the map you planned before the trip.
>
> **Where it breaks:** a passenger is a separate person. Emotions come from inside you and can feel exactly like good judgment, which is why written rules matter more than "just ignoring them".

> [!check]- Check your understanding: the crowd's cycle
> **Q1.** Where in the emotional cycle is buying most dangerous, and where is it most rewarding?
> > [!answer]-
> > Most dangerous near **euphoria** (the top, when it feels obvious). Most rewarding near **capitulation and despondency** (the bottom, when selling feels like relief).
""")
L.before_heading("en", "3.", """
> [!check]- Check your understanding: the four emotions
> **Q1.** You widen your stop because "it will come back". Which emotion is this, and what rule blocks it?
> > [!answer]-
> > **Hope.** The block: a hard stop placed in the market with the entry, and only ever moved to reduce risk.
""")
L.before_callout("en", "example", """
> [!check]- Check your understanding: naming it
> **Q1.** Write the three steps of "name it to tame it".
> > [!answer]-
> > Rate your state 1–5 before entry; when you want to break a rule, say the emotion out loud; then ask "What does the plan say?" and do that.
""")
L.before_callout("en", "action", """
![[p4-early-exits.en.svg]]

> [!walkthrough] Step by step: what Trader A's fear costs over many trades
> The plan: **40%** wins at **+2.5R**, losses **−1R** → expectancy 0.4 × 2.5 − 0.6 × 1 = **+0.40R** per trade.
> 1. Fear closes **1 in 4** winners early at +0.3R → average win = 0.75 × 2.5 + 0.25 × 0.3 = **1.95R** → expectancy **+0.18R**.
> 2. Closing **half** of winners early → average win **1.4R** → expectancy 0.4 × 1.4 − 0.6 = **−0.04R**: a losing system.
> 3. The break-even point is cutting about **45%** of winners: the edge is gone without a single bad entry.
> 4. **So what?** Exits driven by fear can turn a good system into a losing one. Holding to the plan's exit is part of the edge.

> [!market]
> - **Forex:** fast news spikes trigger fear and FOMO; plan news rules in advance *(see 0.8, 10.3)*.
> - **Gold:** big daily swings make it easy to panic out of good trades; size so a swing is boring *(see 0.4)*.
> - **Stocks:** social media hype around single names feeds greed and FOMO *(see 0.6)*.
> - **Crypto:** 24/7 prices and extreme moves make euphoria and capitulation especially strong *(see 0.7)*.

> [!caution]
> Strong emotions during a trade usually mean the position is too big. Greed-driven oversizing and hope-driven stop moves are the fastest ways to turn one bad trade into a large loss. If you feel at 4–5 out of 5, cut size or stop for the day.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Which pairs of emotions mess up entries, exits, and the trades after a loss?
> > [!answer]-
> > Entries: fear and greed. Exits: fear and hope. After a loss: regret.
> **Q2.** A system plans +3R wins at a 35% win rate. If fear makes the average win 1.8R, what's the new expectancy?
> > [!answer]-
> > Planned: 0.35 × 3 − 0.65 = **+0.40R**. With 1.8R: 0.35 × 1.8 − 0.65 = **−0.02R**: slightly losing.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> ทุกเทรดกระตุ้นความรู้สึก: กลัวเสีย โลภอยากได้มากขึ้น หวังว่าไม้ที่ขาดทุนจะกลับมา เสียดายการขยับที่พลาดไป ความรู้สึกเหล่านี้ผลักให้คุณผิดแผนในจังหวะที่แย่ที่สุด คุณหยุดรู้สึกไม่ได้ แต่สังเกตมันได้ เรียกชื่อมันได้ แล้วทำตามที่แผนเขียนไว้
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **ความกลัว (Fear)** — กังวลว่าจะเสีย ทำให้ข้าม Setup หรือออกจากไม้กำไรเร็วเกินไป
> - **ความโลภ (Greed)** — อยากได้มากขึ้น ทำให้เปิดไม้ใหญ่เกิน ไล่ราคา และเทรดมากเกินไป
> - **ความหวัง (Hope)** — เชื่อว่าไม้ขาดทุนจะกลับมา ทำให้ถือไม้ขาดทุนและเลื่อน Stop
> - **ความเสียดาย (Regret)** — เจ็บปวดกับเทรดที่พลาดหรือแพ้ นำไปสู่การเทรดแก้แค้นและไล่ราคา
> - **FOMO (Fear of missing out)** — แรงกระตุ้นให้กระโดดเข้าเพราะราคาวิ่งไปโดยไม่มีคุณ
> - **ความคลั่งไคล้ / การยอมแพ้ (Euphoria / Capitulation)** — การมองโลกแง่ดีสุดโต่งของฝูงชนใกล้ยอด / การยอมแพ้ใกล้ก้น
> - **คะแนนสภาพอารมณ์ (Emotional state score)** — ให้คะแนนตัวเอง 1–5 ก่อนเทรด (1 = สงบ 5 = ปั่นป่วน)
> - **กำไรเฉลี่ย (Average win)** — R เฉลี่ยของไม้ที่ชนะ *(ดู 3.3)*
""")
L.before_heading("th", "2.", """
> [!analogy]
> อารมณ์ระหว่างเทรดเหมือน **ผู้โดยสารเสียงดังที่เบาะหลัง** ตะโกนว่า "เร็วอีก!", "เลี้ยวตรงนี้!", "หยุด!" คุณไล่เขาลงจากรถไม่ได้ แต่ไม่จำเป็นต้องยื่นพวงมาลัยให้ คุณได้ยินเขา แล้วขับตามแผนที่ที่วางไว้ก่อนออกเดินทาง
>
> **จุดที่เปรียบเทียบไม่ได้:** ผู้โดยสารเป็นอีกคนหนึ่ง แต่อารมณ์มาจากข้างในตัวคุณ และอาจรู้สึกเหมือนวิจารณญาณที่ดีทุกประการ นี่คือเหตุผลที่กฎที่เขียนไว้สำคัญกว่า "แค่ไม่สนใจ"

> [!check]- เช็กความเข้าใจ: วงจรอารมณ์ของฝูงชน
> **Q1.** ในวงจรอารมณ์ การซื้อตรงไหนอันตรายที่สุด และตรงไหนให้ผลตอบแทนดีที่สุด?
> > [!answer]-
> > อันตรายที่สุดใกล้ **ความคลั่งไคล้** (ยอด ตอนที่รู้สึกว่าชัดเจน) ให้ผลดีที่สุดใกล้ **การยอมแพ้และความสิ้นหวัง** (ก้น ตอนที่การขายรู้สึกโล่งใจ)
""")
L.before_heading("th", "3.", """
> [!check]- เช็กความเข้าใจ: อารมณ์ 4 อย่าง
> **Q1.** คุณขยาย Stop เพราะ "เดี๋ยวมันก็กลับมา" นี่คืออารมณ์อะไร และกฎไหนป้องกันได้?
> > [!answer]-
> > **ความหวัง** ป้องกันด้วย: Stop จริงที่วางในตลาดพร้อมการเข้า และเลื่อนได้เฉพาะเพื่อลดความเสี่ยงเท่านั้น
""")
L.before_callout("th", "example", """
> [!check]- เช็กความเข้าใจ: การเรียกชื่อ
> **Q1.** เขียนสามขั้นของ "เรียกชื่อมันเพื่อสยบมัน"
> > [!answer]-
> > ให้คะแนนสภาพ 1–5 ก่อนเข้า เมื่ออยากผิดกฎ ให้พูดชื่ออารมณ์ออกมา แล้วถามว่า "แผนบอกว่าอะไร?" และทำตามนั้น
""")
L.before_callout("th", "action", """
![[p4-early-exits.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ความกลัวของเทรดเดอร์ A มีราคาเท่าไรในหลายไม้
> แผน: ชนะ **40%** ที่ **+2.5R** แพ้ **−1R** → ค่าคาดหวัง 0.4 × 2.5 − 0.6 × 1 = **+0.40R** ต่อไม้
> 1. ความกลัวทำให้ปิดไม้ชนะ **1 ใน 4** เร็วที่ +0.3R → กำไรเฉลี่ย = 0.75 × 2.5 + 0.25 × 0.3 = **1.95R** → ค่าคาดหวัง **+0.18R**
> 2. ปิดไม้ชนะเร็ว **ครึ่งหนึ่ง** → กำไรเฉลี่ย **1.4R** → ค่าคาดหวัง 0.4 × 1.4 − 0.6 = **−0.04R**: ระบบที่ขาดทุน
> 3. จุดคุ้มทุนคือการตัดไม้ชนะราว **45%**: ความได้เปรียบหายไปโดยไม่มีจุดเข้าแย่แม้แต่ไม้เดียว
> 4. **แล้วไง?** การออกที่ขับเคลื่อนด้วยความกลัวเปลี่ยนระบบที่ดีให้ขาดทุนได้ การยึดจุดออกตามแผนคือส่วนหนึ่งของความได้เปรียบ

> [!market]
> - **ฟอเร็กซ์:** การพุ่งเร็วช่วงข่าวกระตุ้นความกลัวและ FOMO วางกฎเรื่องข่าวไว้ล่วงหน้า *(ดู 0.8, 10.3)*
> - **ทองคำ:** การแกว่งรายวันที่ใหญ่ทำให้ตกใจออกจากไม้ดี ๆ ได้ง่าย กำหนดขนาดให้การแกว่งน่าเบื่อ *(ดู 0.4)*
> - **หุ้น:** กระแสในโซเชียลมีเดียเกี่ยวกับหุ้นรายตัวกระตุ้นความโลภและ FOMO *(ดู 0.6)*
> - **คริปโต:** ราคา 24/7 และการขยับสุดโต่งทำให้ความคลั่งไคล้และการยอมแพ้รุนแรงเป็นพิเศษ *(ดู 0.7)*

> [!caution]
> อารมณ์ที่รุนแรงระหว่างเทรดมักแปลว่าโพซิชันใหญ่เกินไป การเปิดไม้ใหญ่เพราะโลภ และการเลื่อน Stop เพราะหวัง คือทางที่เร็วที่สุดที่เปลี่ยนเทรดแย่ไม้เดียวให้เป็นการขาดทุนก้อนใหญ่ ถ้ารู้สึกที่ระดับ 4–5 จาก 5 ให้ลดขนาดหรือหยุดวันนั้น
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** อารมณ์คู่ไหนทำลายจุดเข้า จุดออก และเทรดหลังแพ้?
> > [!answer]-
> > จุดเข้า: กลัวและโลภ จุดออก: กลัวและหวัง หลังแพ้: เสียดาย
> **Q2.** ระบบวางแผนชนะ +3R ที่อัตราชนะ 35% ถ้าความกลัวทำให้กำไรเฉลี่ยเหลือ 1.8R ค่าคาดหวังใหม่เท่าไร?
> > [!answer]-
> > ตามแผน: 0.35 × 3 − 0.65 = **+0.40R** ที่ 1.8R: 0.35 × 1.8 − 0.65 = **−0.02R**: ขาดทุนเล็กน้อย
""")

L.set_meta("level", "v2")
L.save()
