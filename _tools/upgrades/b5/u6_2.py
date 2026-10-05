"""B5 · v2 upgrade of 6.2 Elliott Wave: The 5-3 Structure (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("06 Fibonacci, Elliott Wave & Std Dev/6.2 Elliott Wave- The 5-3 Structure.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> When a crowd changes its mind, it doesn't happen all at once. First a few people act, others doubt them, then everyone joins, some take profits, and finally the latecomers rush in just before the move ends. Elliott Wave gives those stages numbers: five steps forward (1-2-3-4-5) and three steps back (A-B-C). It's a way to say "we're probably in this stage of the story", and, more importantly, "if price goes past here, my story is wrong".
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Elliott Wave** — a way of reading trends as repeating waves of crowd behaviour, from Ralph Nelson Elliott (1930s).
> - **Motive / impulse wave** — a wave in the direction of the larger trend (1, 3, 5).
> - **Corrective wave** — a wave against the larger trend (2, 4, and A-B-C).
> - **Cycle** — a complete 5-wave advance plus its 3-wave correction (8 waves).
> - **Count** — your labelling of the waves on a chart.
> - **Alternative (alternate) count** — a second, different labelling you keep in mind in case the main count fails.
> - **Invalidation level** — the price that proves a count wrong *(rules in 6.3)*.
> - **Degree** — the size (timeframe) of a wave; waves of one degree contain waves of the next smaller degree.
> - **Fractal** — the same pattern repeating at different scales *(see 2.6)*.
> - **Sub-wave** — a smaller wave inside a bigger one (written i–v or a-b-c).
> - **FOMO (fear of missing out)** — buying because everyone else seems to be making money, not because of a plan.
> - **Momentum / divergence** — the speed of price moves / a new high made with less speed than the previous one (a warning sign).
> - **BOS / CHoCH** — break of structure / change of character *(see 2.3)*.
""")
L.before_heading("en", "2.", """
![[p6-ew-labelled.en.svg]]

> [!check]- Check your understanding: the 5-3 pattern
> **Q1.** In an uptrend, which waves move with the trend and which against it?
> > [!answer]-
> > With the trend: 1, 3, 5 (motive). Against it: 2, 4 and the A-B-C correction.
""")
L.before_heading("en", "3.", """
> [!analogy]
> A trend is like a **rumour spreading through a town**. A few insiders hear it first and act (wave 1). Others say it's nonsense (wave 2). Then the newspapers print it and everyone talks about it (wave 3). Some people cash in and step back (wave 4). Finally the people who heard it last rush in, just as the insiders are leaving (wave 5). Then the story fades (A-B-C).
>
> **Where it breaks:** a rumour runs through each stage once. Markets can skip stages, repeat them, or turn a "wave 3" into a correction, and you often only know which stage it was afterwards.

> [!walkthrough] Step by step: measuring each wave in the figure (and the crowd behind it)
> Swings: 0 = **100**, 1 = **110**, 2 = **103.82**, 3 = **120.00**, 4 = **113.82**, 5 = **123.82**.
> 1. **Wave 1 (smart money):** 110 − 100 = **10**. Few believe it; it looks like a bounce.
> 2. **Wave 2 (doubt):** 110 − 103.82 = 6.18 → 6.18 ÷ 10 = **61.8%** of wave 1. Deep, but it holds above 100.
> 3. **Wave 3 (recognition):** 120 − 103.82 = **16.18** = **1.618 × wave 1**. The longest, strongest wave.
> 4. **Wave 4 (profit-taking):** 120 − 113.82 = 6.18 → 6.18 ÷ 16.18 = **38.2%** of wave 3. Shallow and sideways, above wave 1's high (110).
> 5. **Wave 5 (euphoria / FOMO):** 123.82 − 113.82 = **10** = wave 1, with weaker momentum.
> 6. **So what?** The numbers turn a story into checkable facts. During wave 4 you knew the long idea was wrong below **110**; after wave 5 you knew the trend was mature. That's what the count is for.

> [!check]- Check your understanding: crowd psychology
> **Q1.** Which wave is usually the longest and strongest, and why?
> > [!answer]-
> > Wave 3: the majority recognises the trend, news turns positive and money floods in.
> **Q2.** What does FOMO look like on the chart in wave 5?
> > [!answer]-
> > A new high made with weaker momentum (smaller bodies, divergence), often after a sweep of buy-side liquidity, while late buyers chase.
""")
L.before_callout("en", "example", """
![[p6-ew-wrong-count.en.svg]]

> [!walkthrough] Step by step: why the "wrong count" in the second figure fails
> Someone labels 100 → **120** as wave 1, 113.82 as wave 2, 123.82 as wave 3, and the C low at **115.4** as wave 4.
> 1. **Wave 1** = 120 − 100 = **20**. **Wave 3** = 123.82 − 113.82 = **10**.
> 2. **Rule 2 at risk:** wave 3 is already shorter than wave 1. For it not to be the shortest, wave 5 would have to be shorter than 10: possible, but a warning.
> 3. **Rule 3 broken:** wave 4's low (**115.4**) is below wave 1's high (**120**): the waves overlap.
> 4. **The cost:** a trader "buying wave 4 for wave 5" at 115.4 is really buying wave C of a correction, against the new direction.
> 5. **So what?** Write the numbers and check the rules (6.3) **before** trading a count. The same candles can tell two very different stories; only one passes the rules.

> [!check]- Check your understanding: the wrong count
> **Q1.** In the wrong count, which single price check proves it wrong?
> > [!answer]-
> > Wave 4's low 115.4 is below wave 1's high 120: wave 4 overlaps wave 1 (rule 3).
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex & indices:** liquid, trending markets are where clean 5-wave counts appear most often, usually on 4H–daily.
> - **Gold:** strong trends but violent news spikes; wave 3s are often extended *(see 0.4)*.
> - **Stocks:** single stocks can gap through invalidation levels on earnings; counts on indices are more reliable than on individual names *(see 0.5)*.
> - **Crypto:** popular with wave counters and very emotional, so the psychology fits; but liquidation wicks distort swings, so count on closes *(see 0.7)*.

> [!caution]
> Elliott counts are easy to fit after the fact and hard to trade live. The most expensive mistakes are "picking the top of wave 5" against a strong trend and holding a losing trade because you can always invent a new count. Your stop is the rule-based invalidation, not a new story.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Name the crowd behaviour behind each of waves 1 to 5.
> > [!answer]-
> > 1: early/smart money buys quietly. 2: doubt, retest. 3: recognition, the crowd joins. 4: profit-taking pause. 5: late buyers, FOMO, weaker momentum.
> **Q2.** Why should you always keep an alternative count?
> > [!answer]-
> > Counts are subjective and often only clear afterwards. When the main count is invalidated, the alternative tells you what's likely happening instead of leaving you lost or hoping.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> เมื่อฝูงชนเปลี่ยนความคิด มันไม่ได้เกิดพร้อมกันทีเดียว ตอนแรกมีไม่กี่คนลงมือ คนอื่นสงสัย จากนั้นทุกคนเข้าร่วม บางคนขายทำกำไร และสุดท้ายคนมาทีหลังรีบเข้ามาก่อนการวิ่งจะจบ Elliott Wave ให้ตัวเลขกับขั้นเหล่านั้น: ก้าวหน้าห้าขั้น (1-2-3-4-5) และถอยสามขั้น (A-B-C) เป็นวิธีบอกว่า "เราน่าจะอยู่ขั้นนี้ของเรื่อง" และที่สำคัญกว่าคือ "ถ้าราคาเลยตรงนี้ไป เรื่องของฉันผิด"
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **Elliott Wave** — วิธีอ่านเทรนด์เป็นคลื่นพฤติกรรมฝูงชนที่ซ้ำ ๆ จาก Ralph Nelson Elliott (ทศวรรษ 1930)
> - **คลื่นขับเคลื่อน (Motive / Impulse wave)** — คลื่นในทิศทางของเทรนด์ใหญ่ (1, 3, 5)
> - **คลื่นปรับฐาน (Corrective wave)** — คลื่นที่สวนเทรนด์ใหญ่ (2, 4 และ A-B-C)
> - **วัฏจักร (Cycle)** — การขึ้นครบ 5 คลื่นบวกการปรับฐาน 3 คลื่น (8 คลื่น)
> - **การนับ (Count)** — การติดป้ายคลื่นบนกราฟของคุณ
> - **การนับสำรอง (Alternative / Alternate count)** — การติดป้ายแบบที่สองที่เก็บไว้ในใจ เผื่อการนับหลักผิด
> - **ระดับที่ทำให้การนับผิด (Invalidation level)** — ราคาที่พิสูจน์ว่าการนับผิด *(กฎใน 6.3)*
> - **ระดับคลื่น (Degree)** — ขนาด (ไทม์เฟรม) ของคลื่น คลื่นระดับหนึ่งมีคลื่นระดับเล็กกว่าอยู่ข้างใน
> - **Fractal** — รูปแบบเดียวกันที่ซ้ำในหลายขนาด *(ดู 2.6)*
> - **คลื่นย่อย (Sub-wave)** — คลื่นเล็กในคลื่นใหญ่ (เขียน i–v หรือ a-b-c)
> - **FOMO (Fear of missing out)** — ซื้อเพราะดูเหมือนคนอื่นทำเงินกันหมด ไม่ใช่เพราะมีแผน
> - **โมเมนตัม / Divergence** — ความเร็วของการวิ่ง / จุดสูงใหม่ที่เกิดด้วยความเร็วน้อยกว่าครั้งก่อน (สัญญาณเตือน)
> - **BOS / CHoCH** — การทะลุโครงสร้าง / การเปลี่ยนนิสัย *(ดู 2.3)*
""")
L.before_heading("th", "2.", """
![[p6-ew-labelled.th.svg]]

> [!check]- เช็กความเข้าใจ: รูปแบบ 5-3
> **Q1.** ในเทรนด์ขาขึ้น คลื่นไหนไปตามเทรนด์ และคลื่นไหนสวนเทรนด์?
> > [!answer]-
> > ตามเทรนด์: 1, 3, 5 (คลื่นขับเคลื่อน) สวนเทรนด์: 2, 4 และการปรับฐาน A-B-C
""")
L.before_heading("th", "3.", """
> [!analogy]
> เทรนด์เหมือน **ข่าวลือที่แพร่ไปทั่วเมือง** คนวงในไม่กี่คนได้ยินก่อนและลงมือ (คลื่น 1) คนอื่นบอกว่าไร้สาระ (คลื่น 2) จากนั้นหนังสือพิมพ์ลงข่าว ทุกคนพูดถึง (คลื่น 3) บางคนรับผลประโยชน์แล้วถอยออก (คลื่น 4) สุดท้ายคนที่ได้ยินทีหลังสุดรีบเข้ามา ตอนที่คนวงในกำลังออก (คลื่น 5) แล้วเรื่องก็ซาลง (A-B-C)
>
> **จุดที่เปรียบเทียบไม่ได้:** ข่าวลือผ่านแต่ละขั้นครั้งเดียว แต่ตลาดอาจข้ามขั้น ทำซ้ำ หรือเปลี่ยน "คลื่น 3" ให้กลายเป็นการปรับฐาน และบ่อยครั้งคุณรู้ว่าเป็นขั้นไหนก็ต่อเมื่อผ่านไปแล้ว

> [!walkthrough] ไล่ทีละขั้น: วัดแต่ละคลื่นในภาพ (และฝูงชนเบื้องหลัง)
> Swing: 0 = **100**, 1 = **110**, 2 = **103.82**, 3 = **120.00**, 4 = **113.82**, 5 = **123.82**
> 1. **คลื่น 1 (เงินฉลาด):** 110 − 100 = **10** มีคนเชื่อน้อย ดูเหมือนแค่เด้ง
> 2. **คลื่น 2 (ความสงสัย):** 110 − 103.82 = 6.18 → 6.18 ÷ 10 = **61.8%** ของคลื่น 1 ลึก แต่ยืนเหนือ 100
> 3. **คลื่น 3 (การยอมรับ):** 120 − 103.82 = **16.18** = **1.618 × คลื่น 1** ยาวและแรงที่สุด
> 4. **คลื่น 4 (ขายทำกำไร):** 120 − 113.82 = 6.18 → 6.18 ÷ 16.18 = **38.2%** ของคลื่น 3 ตื้นและออกข้าง อยู่เหนือจุดสูงคลื่น 1 (110)
> 5. **คลื่น 5 (ตื่นเต้น / FOMO):** 123.82 − 113.82 = **10** = คลื่น 1 โมเมนตัมอ่อนลง
> 6. **แล้วไง?** ตัวเลขเปลี่ยนเรื่องเล่าให้เป็นข้อเท็จจริงที่ตรวจได้ ระหว่างคลื่น 4 คุณรู้ว่าไอเดีย Long ผิดถ้าต่ำกว่า **110** หลังคลื่น 5 คุณรู้ว่าเทรนด์เติบโตเต็มที่แล้ว นั่นคือประโยชน์ของการนับ

> [!check]- เช็กความเข้าใจ: จิตวิทยาฝูงชน
> **Q1.** คลื่นไหนมักยาวและแรงที่สุด และเพราะอะไร?
> > [!answer]-
> > คลื่น 3: คนส่วนใหญ่ยอมรับเทรนด์ ข่าวเป็นบวก และเงินไหลเข้ามามาก
> **Q2.** FOMO ในคลื่น 5 หน้าตาเป็นอย่างไรบนกราฟ?
> > [!answer]-
> > จุดสูงใหม่ที่โมเมนตัมอ่อนลง (แท่งเล็กลง Divergence) มักหลังการกวาดสภาพคล่องฝั่งซื้อ ขณะที่คนซื้อทีหลังไล่ราคา
""")
L.before_callout("th", "example", """
![[p6-ew-wrong-count.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ทำไม "การนับผิด" ในภาพที่สองจึงใช้ไม่ได้
> มีคนติดป้าย 100 → **120** เป็นคลื่น 1, 113.82 เป็นคลื่น 2, 123.82 เป็นคลื่น 3 และจุดต่ำ C ที่ **115.4** เป็นคลื่น 4
> 1. **คลื่น 1** = 120 − 100 = **20** **คลื่น 3** = 123.82 − 113.82 = **10**
> 2. **กฎ 2 เสี่ยง:** คลื่น 3 สั้นกว่าคลื่น 1 แล้ว ถ้าจะไม่ให้สั้นที่สุด คลื่น 5 ต้องสั้นกว่า 10: เป็นไปได้ แต่เป็นสัญญาณเตือน
> 3. **ผิดกฎ 3:** จุดต่ำคลื่น 4 (**115.4**) อยู่ใต้จุดสูงคลื่น 1 (**120**): คลื่นทับซ้อนกัน
> 4. **ราคาที่ต้องจ่าย:** เทรดเดอร์ที่ "ซื้อคลื่น 4 เพื่อรอคลื่น 5" ที่ 115.4 จริง ๆ กำลังซื้อคลื่น C ของการปรับฐาน สวนทิศทางใหม่
> 5. **แล้วไง?** เขียนตัวเลขและตรวจกฎ (6.3) **ก่อน** เทรดตามการนับ แท่งเทียนชุดเดียวกันเล่าเรื่องได้ต่างกันมาก มีแค่เรื่องเดียวที่ผ่านกฎ

> [!check]- เช็กความเข้าใจ: การนับผิด
> **Q1.** ในการนับผิด การตรวจราคาข้อเดียวไหนที่พิสูจน์ว่าผิด?
> > [!answer]-
> > จุดต่ำคลื่น 4 ที่ 115.4 อยู่ใต้จุดสูงคลื่น 1 ที่ 120: คลื่น 4 ทับซ้อนคลื่น 1 (กฎ 3)
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์และดัชนี:** ตลาดที่มีสภาพคล่องและมีเทรนด์คือที่ที่การนับ 5 คลื่นชัด ๆ ปรากฏบ่อยที่สุด มักบน 4 ชั่วโมงถึงรายวัน
> - **ทองคำ:** เทรนด์แรงแต่มีข่าวพุ่งรุนแรง คลื่น 3 มักยืดยาว *(ดู 0.4)*
> - **หุ้น:** หุ้นรายตัวอาจ Gap ทะลุระดับ Invalidation ตอนประกาศงบ การนับบนดัชนีเชื่อถือได้มากกว่าหุ้นรายตัว *(ดู 0.5)*
> - **คริปโต:** เป็นที่นิยมของนักนับคลื่นและอารมณ์แรงมาก จิตวิทยาจึงเข้ากัน แต่ไส้จากการล้างพอร์ตบิดเบือน Swing ให้นับจากราคาปิด *(ดู 0.7)*

> [!caution]
> การนับ Elliott ง่ายที่จะจับคู่หลังเหตุการณ์ แต่ยากที่จะเทรดจริง ความผิดพลาดที่แพงที่สุดคือ "ทายยอดคลื่น 5" สวนเทรนด์แรง และถือไม้ขาดทุนต่อเพราะคุณคิดการนับใหม่ได้เสมอ Stop ของคุณคือระดับ Invalidation ตามกฎ ไม่ใช่เรื่องเล่าใหม่
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกพฤติกรรมฝูงชนเบื้องหลังคลื่น 1 ถึง 5
> > [!answer]-
> > 1: เงินฉลาด/คนกลุ่มแรกซื้อเงียบ ๆ 2: สงสัย ทดสอบซ้ำ 3: ยอมรับ ฝูงชนเข้าร่วม 4: พักขายทำกำไร 5: คนซื้อทีหลัง FOMO โมเมนตัมอ่อนลง
> **Q2.** ทำไมต้องมีการนับสำรองเสมอ?
> > [!answer]-
> > การนับเป็นเรื่องอัตวิสัยและมักชัดเจนหลังเหตุการณ์ เมื่อการนับหลักใช้ไม่ได้ การนับสำรองบอกว่าน่าจะเกิดอะไรขึ้นแทน ไม่ให้คุณหลงทางหรือได้แต่หวัง
""")

L.set_meta("level", "v2")
L.save()
