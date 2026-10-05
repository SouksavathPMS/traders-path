"""B7 · v2 upgrade of 9.3 Backtesting Without Fooling Yourself (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("09 Quant & Data Analysis/9.3 Backtesting Without Fooling Yourself.md")

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> A backtest is like asking "what if I had used these rules last year?" and checking old charts. It sounds simple, but it's very easy to cheat without noticing: using information you couldn't have had, testing only the winners, forgetting fees, or tweaking the rules until the past looks perfect. The result is a beautiful number that won't happen in the future. This lesson is a list of those traps and how to avoid them.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Backtest** — applying fixed rules to past data to see what would have happened.
> - **Parameter** — an adjustable number in the rules (e.g. a 20-day moving average).
> - **In-sample / out-of-sample** — the data used to choose the rules / data kept aside and used once to test them.
> - **Walk-forward** — repeatedly optimising on one window and testing on the next unseen window.
> - **Forward test** — following the rules in real time on paper or small size.
> - **Look-ahead bias** — using information that wasn't available at the moment of the decision.
> - **Survivorship bias** — testing only the stocks or coins that still exist; the failures are missing.
> - **Overfitting** — tuning rules to the noise of one history so they fail on new data.
> - **Data snooping** — trying many ideas and keeping the best one, which is often just luck.
> - **Delisted** — removed from an exchange (bankrupt, taken over, or failed).
> - **Plateau** — a region of parameters where many nearby settings work; more trustworthy than a single sharp peak.
> - **Regime** — a market condition (trending, ranging, high or low volatility) *(see 2.2)*.
> - **Slippage** — getting filled worse than the planned price *(see 0.1)*.
""")
L.before_heading("en", "2.", """
![[p9-five-biases.en.svg]]

> [!walkthrough] Step by step: putting numbers on two biases
> **Ignoring costs:** a strategy makes **200 trades a year** and shows **+20%** before costs.
> 1. Realistic cost per round trip: 0.125% (spread + commission + slippage).
> 2. Total cost = 200 × 0.125% = **25%** a year.
> 3. Real result ≈ 20% − 25% = **−5%**. The "edge" was smaller than its costs.
> **Data snooping:** you test **200** random ideas, each with a 5% chance of looking "significant" by pure luck.
> 4. Expected lucky "winners" = 200 × 5% = **10 ideas** that look great and mean nothing.
> 5. **So what?** Always charge costs, and count how many ideas you tried. The more you tried, the stronger the evidence you need before believing the best one.

> [!check]- Check your understanding: the biases
> **Q1.** A test buys at today's open when today's close is above the 20-day average. What's wrong?
> > [!answer]-
> > Look-ahead bias: at the open you can't know today's close. Signal on today's close, trade at tomorrow's open.
> **Q2.** You test a strategy on the 30 stocks in today's index over 20 years. Which bias, and why does it flatter the result?
> > [!answer]-
> > Survivorship bias: companies that failed or were removed from the index are missing, so the test only includes the winners.
""")
L.before_heading("en", "3.", """
> [!analogy]
> Overfitting is like a **suit tailored to one pose**. It fits perfectly while you stand exactly like that, but the moment you walk, it rips. A robust strategy is an off-the-rack suit that fits reasonably well in many positions.
>
> **Where it breaks:** with a suit you can see the tear immediately. An overfit strategy fails quietly over months, and it's easy to blame "the market changed" instead of the fitting.

> [!check]- Check your understanding: overfitting
> **Q1.** The best in-sample pair was SMA 45/240, but its neighbours (40/240, 45/220, 50/260) all lost money. Trust it?
> > [!answer]-
> > No. A lone sharp peak surrounded by losers is the signature of overfitting. Prefer parameter regions where many neighbours work (a plateau).
""")
L.before_heading("en", "4.", """
> [!check]- Check your understanding: out-of-sample
> **Q1.** You run the out-of-sample test, don't like the result, change one parameter and run it again. Is it still out-of-sample?
> > [!answer]-
> > No. Once you adjust after seeing it, that data has been used to choose the rules; it's now in-sample.
""")
L.before_callout("en", "action", """
> [!market]
> - **Forex:** costs and swap must be included; broker data quality varies, so check for gaps and bad ticks *(see 0.1, 0.2)*.
> - **Gold:** spreads widen sharply at news; assume worse fills around 19:30 UTC+7 releases *(see 0.4, 0.8)*.
> - **Stocks:** survivorship is the big trap; use data that includes delisted companies, and model overnight gaps at stops *(see 0.5)*.
> - **Crypto:** thousands of coins have died; testing only today's top coins is extreme survivorship bias; fees and funding matter *(see 0.7)*.

> [!caution]
> A backtest that looks too good is usually wrong. Before risking money: check the code for look-ahead, add realistic costs, test out-of-sample once, and forward test for 30+ trades at small size. Money lost by trusting a flawed backtest is real; the backtest's profits never were.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Name the five biases from the figure and one fix for each.
> > [!answer]-
> > Look-ahead: signal on bar t, trade on t+1. Survivorship: include delisted symbols. Overfitting: few parameters, plateaus, out-of-sample. Data snooping: count ideas tried, demand stronger evidence. Ignoring costs: charge realistic costs and slippage on every trade.
> **Q2.** What is the most honest test of a strategy, and why?
> > [!answer]-
> > A forward test in real time (paper or small size): the data didn't exist when the rules were written, so no hindsight can leak in.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> Backtest เหมือนการถามว่า "ถ้าปีที่แล้วฉันใช้กฎนี้ จะเป็นอย่างไร?" แล้วไปดูกราฟเก่า ฟังดูง่าย แต่โกงตัวเองได้ง่ายมากโดยไม่รู้ตัว: ใช้ข้อมูลที่ตอนนั้นไม่มีทางรู้ ทดสอบแต่ตัวที่ชนะ ลืมค่าธรรมเนียม หรือปรับกฎจนอดีตดูสมบูรณ์แบบ ผลคือตัวเลขสวยงามที่จะไม่เกิดในอนาคต บทนี้คือรายการกับดักเหล่านั้นและวิธีหลบ
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **Backtest** — ใช้กฎที่กำหนดไว้ตายตัวกับข้อมูลในอดีตเพื่อดูว่าจะเกิดอะไรขึ้น
> - **พารามิเตอร์ (Parameter)** — ตัวเลขที่ปรับได้ในกฎ (เช่น เส้นค่าเฉลี่ย 20 วัน)
> - **In-sample / Out-of-sample** — ข้อมูลที่ใช้เลือกกฎ / ข้อมูลที่เก็บไว้และใช้ทดสอบครั้งเดียว
> - **Walk-forward** — ปรับค่าบนช่วงหนึ่งแล้วทดสอบกับช่วงถัดไปที่ยังไม่เคยเห็น ซ้ำไปเรื่อย ๆ
> - **Forward test** — ทำตามกฎแบบเรียลไทม์บนกระดาษหรือด้วยขนาดเล็ก
> - **Look-ahead bias** — ใช้ข้อมูลที่ยังไม่มี ณ ตอนตัดสินใจ
> - **Survivorship bias** — ทดสอบเฉพาะหุ้นหรือเหรียญที่ยังอยู่ ตัวที่ล้มเหลวหายไป
> - **Overfitting** — ปรับกฎให้เข้ากับสัญญาณรบกวนของประวัติชุดเดียว จนพังกับข้อมูลใหม่
> - **Data snooping** — ลองหลายไอเดียแล้วเก็บตัวที่ดีที่สุด ซึ่งมักเป็นแค่โชค
> - **ถูกถอนออกจากตลาด (Delisted)** — ถูกเอาออกจากตลาด (ล้มละลาย ถูกซื้อกิจการ หรือล้มเหลว)
> - **Plateau (ที่ราบ)** — ช่วงพารามิเตอร์ที่ค่าใกล้เคียงหลายค่าได้ผล น่าเชื่อกว่ายอดแหลมยอดเดียว
> - **สภาวะตลาด (Regime)** — สภาพของตลาด (มีเทรนด์ ออกข้าง ผันผวนสูงหรือต่ำ) *(ดู 2.2)*
> - **Slippage** — ได้ราคาแย่กว่าที่วางแผน *(ดู 0.1)*
""")
L.before_heading("th", "2.", """
![[p9-five-biases.th.svg]]

> [!walkthrough] ไล่ทีละขั้น: ใส่ตัวเลขให้อคติสองแบบ
> **ไม่คิดต้นทุน:** กลยุทธ์หนึ่งเทรด **200 ไม้ต่อปี** และแสดงผล **+20%** ก่อนหักต้นทุน
> 1. ต้นทุนที่สมจริงต่อการเปิด-ปิดหนึ่งรอบ: 0.125% (Spread + ค่าคอมมิชชัน + Slippage)
> 2. ต้นทุนรวม = 200 × 0.125% = **25%** ต่อปี
> 3. ผลจริง ≈ 20% − 25% = **−5%** "ความได้เปรียบ" เล็กกว่าต้นทุนของมันเอง
> **Data snooping:** คุณทดสอบ **200** ไอเดียสุ่ม แต่ละไอเดียมีโอกาส 5% ที่จะดู "มีนัยสำคัญ" ด้วยโชคล้วน ๆ
> 4. "ผู้ชนะ" ที่ได้จากโชคที่คาดไว้ = 200 × 5% = **10 ไอเดีย** ที่ดูดีมากแต่ไม่มีความหมาย
> 5. **แล้วไง?** คิดต้นทุนเสมอ และนับว่าลองไปกี่ไอเดีย ยิ่งลองมาก ยิ่งต้องการหลักฐานที่แข็งแรงขึ้นก่อนจะเชื่อไอเดียที่ดีที่สุด

> [!check]- เช็กความเข้าใจ: อคติ
> **Q1.** การทดสอบหนึ่งซื้อตอนเปิดวันนี้ เมื่อราคาปิดวันนี้อยู่เหนือค่าเฉลี่ย 20 วัน ผิดตรงไหน?
> > [!answer]-
> > Look-ahead bias: ตอนเปิดคุณยังไม่รู้ราคาปิดวันนี้ ให้สัญญาณจากราคาปิดวันนี้ และเทรดตอนเปิดพรุ่งนี้
> **Q2.** คุณทดสอบกลยุทธ์กับหุ้น 30 ตัวในดัชนีวันนี้ย้อนหลัง 20 ปี อคติแบบไหน และทำไมทำให้ผลดูดีเกินจริง?
> > [!answer]-
> > Survivorship bias: บริษัทที่ล้มเหลวหรือถูกเอาออกจากดัชนีหายไป การทดสอบจึงมีแต่ผู้ชนะ
""")
L.before_heading("th", "3.", """
> [!analogy]
> Overfitting เหมือน **สูทที่ตัดให้พอดีกับท่าเดียว** ใส่พอดีเป๊ะตอนยืนท่านั้น แต่พอเดินก็ขาด กลยุทธ์ที่แข็งแรงคือสูทสำเร็จรูปที่พอดีพอสมควรในหลายท่า
>
> **จุดที่เปรียบเทียบไม่ได้:** สูทขาดเห็นได้ทันที แต่กลยุทธ์ที่ Overfit ล้มเหลวเงียบ ๆ ในหลายเดือน และง่ายที่จะโทษว่า "ตลาดเปลี่ยน" แทนที่จะโทษการปรับจนเกินไป

> [!check]- เช็กความเข้าใจ: Overfitting
> **Q1.** คู่ที่ดีที่สุดใน In-sample คือ SMA 45/240 แต่ค่าข้างเคียง (40/240, 45/220, 50/260) ขาดทุนหมด เชื่อได้ไหม?
> > [!answer]-
> > ไม่ได้ ยอดแหลมยอดเดียวที่รายล้อมด้วยผู้แพ้คือลายเซ็นของ Overfitting ให้เลือกช่วงพารามิเตอร์ที่ค่าข้างเคียงหลายค่าได้ผล (Plateau)
""")
L.before_heading("th", "4.", """
> [!check]- เช็กความเข้าใจ: Out-of-sample
> **Q1.** คุณรันการทดสอบ Out-of-sample ไม่ชอบผล เปลี่ยนพารามิเตอร์หนึ่งตัวแล้วรันใหม่ ยังเป็น Out-of-sample อยู่ไหม?
> > [!answer]-
> > ไม่ใช่แล้ว เมื่อคุณปรับหลังเห็นผล ข้อมูลนั้นถูกใช้เลือกกฎไปแล้ว ตอนนี้มันเป็น In-sample
""")
L.before_callout("th", "action", """
> [!market]
> - **ฟอเร็กซ์:** ต้องรวมต้นทุนและ Swap คุณภาพข้อมูลของโบรกเกอร์ต่างกัน ตรวจหาช่องว่างและ Tick ที่ผิด *(ดู 0.1, 0.2)*
> - **ทองคำ:** Spread ถ่างแรงช่วงข่าว ให้สมมติว่าได้ราคาแย่ลงรอบข่าว 19:30 UTC+7 *(ดู 0.4, 0.8)*
> - **หุ้น:** Survivorship คือกับดักใหญ่ ใช้ข้อมูลที่รวมบริษัทที่ถูกถอนออก และจำลอง Gap ข้ามคืนที่ Stop *(ดู 0.5)*
> - **คริปโต:** เหรียญนับพันตายไปแล้ว การทดสอบแค่เหรียญท็อปวันนี้คือ Survivorship bias ขั้นสุด ค่าธรรมเนียมและ Funding สำคัญ *(ดู 0.7)*

> [!caution]
> Backtest ที่ดูดีเกินไปมักผิด ก่อนเสี่ยงเงิน: ตรวจโค้ดหา Look-ahead ใส่ต้นทุนที่สมจริง ทดสอบ Out-of-sample ครั้งเดียว และ Forward test 30+ ไม้ด้วยขนาดเล็ก เงินที่เสียเพราะเชื่อ Backtest ที่มีข้อบกพร่องเป็นของจริง แต่กำไรของ Backtest ไม่เคยเป็นของจริง
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกอคติห้าแบบในภาพ และวิธีแก้แบบละหนึ่งวิธี
> > [!answer]-
> > Look-ahead: สัญญาณที่แท่ง t เทรดที่ t+1 Survivorship: รวมสัญลักษณ์ที่ถูกถอนออก Overfitting: พารามิเตอร์น้อย เลือก Plateau ทดสอบ Out-of-sample Data snooping: นับจำนวนไอเดียที่ลอง ต้องการหลักฐานที่แข็งแรงขึ้น ไม่คิดต้นทุน: คิดต้นทุนและ Slippage ที่สมจริงทุกไม้
> **Q2.** การทดสอบกลยุทธ์ที่ซื่อสัตย์ที่สุดคืออะไร และเพราะอะไร?
> > [!answer]-
> > Forward test แบบเรียลไทม์ (บนกระดาษหรือขนาดเล็ก): ข้อมูลยังไม่มีอยู่ตอนเขียนกฎ จึงไม่มีการมองย้อนหลังรั่วเข้ามาได้
""")

L.set_meta("level", "v2")
L.save()
