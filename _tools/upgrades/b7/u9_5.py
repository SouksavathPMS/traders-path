"""B7 · v2 upgrade of 9.5 A Simple Quant Strategy in Python (additive, idempotent)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from upgrade_lesson import Lesson

L = Lesson("09 Quant & Data Analysis/9.5 A Simple Quant Strategy in Python.md")

# Real output of `python3 _tools/quant/sma_crossover.py` (checked Oct 2026, Python 3.13 on macOS).
OUTPUT = """```
bars: 2016  in-sample: 1411  out-of-sample: 605
best parameters in-sample: SMA 30 / 200
top 3 in-sample Sharpe: [(0.55, 30, 200), (0.49, 50, 200), (0.35, 10, 200)]
IN-SAMPLE   strategy : CAGR +7.1%  vol 14.3%  Sharpe 0.55  Sortino 0.79  maxDD 20.1%  trades 8  win 62%  PF 11.42  avg win +12.1%  avg loss -1.8%
IN-SAMPLE   buy&hold : CAGR +6.6%  vol 18.3%  Sharpe 0.44  Sortino 0.64  maxDD 25.6%
OUT-SAMPLE  strategy : CAGR +4.6%  vol 14.4%  Sharpe 0.39  Sortino 0.57  maxDD 17.5%  trades 3  win 67%  PF 12.21  avg win +6.1%  avg loss -1.0%
OUT-SAMPLE  buy&hold : CAGR +10.4%  vol 17.8%  Sharpe 0.64  Sortino 0.95  maxDD 22.9%
```"""

CODE_EN = """```python
def backtest(prices, fast, slow, cost=0.001):
    f = sma(prices, fast)            # fast moving average for every day (None until enough data)
    s = sma(prices, slow)            # slow moving average
    # position for each day: 1 = long if fast > slow, 0 = flat (also 0 while averages aren't ready)
    pos = [1 if (f[i] and s[i] and f[i] > s[i]) else 0 for i in range(len(prices))]
    rets = [0.0]                     # day 0 has no return
    for i in range(1, len(prices)):  # walk through the days in order, like real time
        held = pos[i - 1]            # we can only hold what YESTERDAY's close told us (no look-ahead)
        r = held * (prices[i] / prices[i - 1] - 1)   # today's % change, earned only if we were long
        if i >= 2 and pos[i - 1] != pos[i - 2]:      # the position changed at today's open...
            r -= cost                                # ...so pay 0.10% for spread, commission, slippage
        rets.append(r)               # store today's strategy return
    return rets                      # list of daily returns → equity curve, Sharpe, drawdown (9.6)
```"""

CODE_TH = """```python
def backtest(prices, fast, slow, cost=0.001):
    f = sma(prices, fast)            # ค่าเฉลี่ยเร็วของทุกวัน (None จนกว่าข้อมูลจะพอ)
    s = sma(prices, slow)            # ค่าเฉลี่ยช้า
    # โพซิชันของแต่ละวัน: 1 = Long ถ้าเส้นเร็ว > เส้นช้า, 0 = ไม่ถือ (และ 0 ระหว่างที่ค่าเฉลี่ยยังไม่พร้อม)
    pos = [1 if (f[i] and s[i] and f[i] > s[i]) else 0 for i in range(len(prices))]
    rets = [0.0]                     # วันที่ 0 ไม่มีผลตอบแทน
    for i in range(1, len(prices)):  # เดินไปทีละวันตามลำดับ เหมือนเวลาจริง
        held = pos[i - 1]            # ถือได้แค่สิ่งที่ราคาปิด "เมื่อวาน" บอก (ไม่มี Look-ahead)
        r = held * (prices[i] / prices[i - 1] - 1)   # % เปลี่ยนแปลงวันนี้ ได้เฉพาะถ้าเรา Long อยู่
        if i >= 2 and pos[i - 1] != pos[i - 2]:      # โพซิชันเปลี่ยนตอนเปิดวันนี้...
            r -= cost                                # ...จึงจ่าย 0.10% เป็นค่า Spread ค่าคอม Slippage
        rets.append(r)               # เก็บผลตอบแทนของกลยุทธ์วันนี้
    return rets                      # รายการผลตอบแทนรายวัน → กราฟเงินทุน Sharpe Drawdown (9.6)
```"""

# ---------------------------------------------------------------- EN
L.after_callout("en", "mindset", """
> [!eli5]
> A computer follows rules exactly, without hope or fear, and it can't peek at tomorrow unless you accidentally let it. That makes it a great tool to test a trading idea honestly. In this lesson a short Python program checks one simple rule ("hold the market only when the short-term average is above the long-term average") on 8 years of data, then reports how it did on data it never saw while being tuned. You don't need to be a programmer: you need to run it, read it, and understand what it proves and what it doesn't.
""")
L.after_callout("en", "eli5", """
> [!terms]
> - **Python** — a free, beginner-friendly programming language.
> - **Script** — a text file of Python instructions you run from the Terminal.
> - **Terminal** — the macOS app (Applications → Utilities) where you type commands.
> - **Function** — a named block of code that takes inputs and returns a result (here `backtest` and `sma`).
> - **List** — an ordered collection of values, e.g. daily prices.
> - **Loop** — code that repeats for each item, e.g. each day.
> - **SMA (simple moving average)** — the average of the last *n* closing prices.
> - **CSV (comma-separated values)** — a plain text data file you can export from a spreadsheet or broker.
> - **Synthetic data** — computer-generated prices with realistic behaviour, used so everyone gets the same result.
> - **In-sample / out-of-sample** — data used to choose the settings / data kept back to judge them *(see 9.3)*.
> - **CAGR, Sharpe, Sortino, maxDD, PF** — performance metrics explained in 9.6.
""")
L.before_heading("en", "2.", """
> [!walkthrough] Step by step: install and run Python on a Mac
> 1. Open **Terminal** (press Cmd + Space, type "Terminal", Enter).
> 2. Type `python3 --version` and press Enter. If you see something like `Python 3.12.x` or newer, skip to step 4.
> 3. If macOS offers to install the **Command Line Developer Tools**, click Install (it includes Python 3). Alternatively, download the official macOS installer from python.org and run it.
> 4. Go to your vault folder: type `cd ` (with a space), drag the vault folder from Finder into the Terminal window, press Enter.
> 5. Run `python3 _tools/quant/sma_crossover.py`. It needs no extra packages and finishes in a few seconds.
> 6. **So what?** If your output matches the block below exactly, your setup works and the numbers in this lesson are reproducible. If it doesn't match, something is different (Python version, edited file), and you've learned that before trusting any result.

Real output of the script (synthetic data, seed 42):

""" + OUTPUT + """

> [!check]- Check your understanding: running the script
> **Q1.** The script prints "bars: 2016 in-sample: 1411 out-of-sample: 605". What do those three numbers mean?
> > [!answer]-
> > 2,016 daily prices in total; the first 1,411 (70%) were used to choose the moving-average settings; the last 605 (30%) were kept back to judge them.
""")
L.before_heading("en", "3.", """
**The same function with every line explained:**

""" + CODE_EN + """

> [!walkthrough] Step by step: the loop on four tiny days
> Prices **100, 101, 103, 102**; positions from the signal **0, 1, 1, 0** (flat, long, long, flat). Cost 0.10%.
> 1. **Day 1:** we held yesterday's position (0) → return **0%**.
> 2. **Day 2:** held position 1 (decided at day 1's close). Price 101 → 103 = **+1.98%**. The position changed (0 → 1) at today's open → minus 0.10% = **+1.88%**.
> 3. **Day 3:** held 1. Price 103 → 102 = **−0.97%**. No change in position → no cost.
> 4. Day 3's signal is 0, so the exit (and its 0.10% cost) happens at day 4's open.
> 5. **So what?** Each day's return uses only information from the day before. Change `pos[i - 1]` to `pos[i]` and the strategy would "know" today's close before trading at today's open: a tiny look-ahead bug that makes any backtest look brilliant.

> [!check]- Check your understanding: the code
> **Q1.** Why does the code use `held = pos[i - 1]` and not `pos[i]`?
> > [!answer]-
> > The signal is computed from day i−1's close, so it can only be traded from day i onward. Using pos[i] would trade on information not yet available (look-ahead bias).
""")
L.before_callout("en", "example", """
> [!analogy]
> A backtest script is like a **recipe followed by a robot cook**. The robot never "adds a bit more salt because it feels right", so if the dish is bad, you know it's the recipe. But the robot also follows a wrong instruction perfectly: if the recipe says to taste tomorrow's soup, the robot will happily do it, and the result is fiction.
>
> **Where it breaks:** a robot cook would notice there's no tomorrow's soup; code doesn't notice look-ahead or survivorship. You have to check the recipe yourself.

> [!check]- Check your understanding: the result
> **Q1.** In-sample the strategy beat buy and hold; out-of-sample it didn't. Which result should guide your expectations, and why?
> > [!answer]-
> > Out-of-sample: the settings were chosen to look good in-sample, so that part is flattered. Unseen data is the honest estimate (and even it is based on only 3 trades).
""")
L.before_callout("en", "action", """
> [!market]
> - **Stocks & indices:** download daily closes of an index ETF (e.g. SPY) as CSV; 252 trading days per year is correct here.
> - **Forex & gold:** daily data trade about 5 days a week (~260 bars a year); costs differ, so change `COST` *(see 0.1)*.
> - **Crypto:** prices trade 365 days a year, so annualising with √252 overstates or understates; use 365 in the metric code *(see 0.7)*.

> [!caution]
> A script that runs without errors can still be wrong. Before trusting any backtest, read the code line by line, reproduce the numbers, test on real data and other markets, and never move from a backtest straight to real money: forward test first *(see 9.3)*.
""")
L.at_end("en", """
> [!check]- Final check
> **Q1.** Name the three honesty rules built into the script.
> > [!answer]-
> > No look-ahead (signal on day t traded on day t+1), costs on every position change, and settings chosen on the first 70% only, judged on the last 30%.
> **Q2.** What is the single biggest weakness of this test's conclusion?
> > [!answer]-
> > Far too few trades (8 in-sample, 3 out-of-sample) on one synthetic series. Nothing can be concluded about edge from that sample.
""")

# ---------------------------------------------------------------- TH
L.after_callout("th", "mindset", """
> [!eli5]
> คอมพิวเตอร์ทำตามกฎเป๊ะ ๆ ไม่มีความหวังหรือความกลัว และแอบดูพรุ่งนี้ไม่ได้ เว้นแต่คุณเผลอปล่อยให้ทำ จึงเป็นเครื่องมือที่ดีมากในการทดสอบไอเดียเทรดอย่างซื่อสัตย์ ในบทนี้ โปรแกรม Python สั้น ๆ ทดสอบกฎง่าย ๆ ข้อเดียว ("ถือตลาดเฉพาะตอนที่ค่าเฉลี่ยระยะสั้นอยู่เหนือค่าเฉลี่ยระยะยาว") กับข้อมูล 8 ปี แล้วรายงานผลบนข้อมูลที่มันไม่เคยเห็นตอนปรับค่า คุณไม่ต้องเป็นโปรแกรมเมอร์: แค่รัน อ่าน และเข้าใจว่ามันพิสูจน์อะไรและไม่ได้พิสูจน์อะไร
""")
L.after_callout("th", "eli5", """
> [!terms]
> - **Python** — ภาษาโปรแกรมฟรีที่เหมาะกับผู้เริ่มต้น
> - **สคริปต์ (Script)** — ไฟล์ข้อความที่มีคำสั่ง Python ซึ่งรันจาก Terminal
> - **Terminal** — แอปของ macOS (Applications → Utilities) ที่ใช้พิมพ์คำสั่ง
> - **ฟังก์ชัน (Function)** — ก้อนโค้ดที่มีชื่อ รับข้อมูลเข้าและคืนผลลัพธ์ (ในที่นี้คือ `backtest` และ `sma`)
> - **ลิสต์ (List)** — ชุดค่าที่เรียงลำดับ เช่น ราคารายวัน
> - **ลูป (Loop)** — โค้ดที่ทำซ้ำกับทุกรายการ เช่น ทุกวัน
> - **SMA (Simple moving average)** — ค่าเฉลี่ยของราคาปิด *n* ตัวล่าสุด
> - **CSV (Comma-separated values)** — ไฟล์ข้อมูลแบบข้อความธรรมดา ส่งออกได้จากสเปรดชีตหรือโบรกเกอร์
> - **ข้อมูลสังเคราะห์ (Synthetic data)** — ราคาที่คอมพิวเตอร์สร้างให้มีพฤติกรรมสมจริง ใช้เพื่อให้ทุกคนได้ผลเหมือนกัน
> - **In-sample / Out-of-sample** — ข้อมูลที่ใช้เลือกค่า / ข้อมูลที่เก็บไว้ตัดสิน *(ดู 9.3)*
> - **CAGR, Sharpe, Sortino, maxDD, PF** — ตัวชี้วัดผลงานที่อธิบายใน 9.6
""")
L.before_heading("th", "2.", """
> [!walkthrough] ไล่ทีละขั้น: ติดตั้งและรัน Python บน Mac
> 1. เปิด **Terminal** (กด Cmd + Space พิมพ์ "Terminal" แล้ว Enter)
> 2. พิมพ์ `python3 --version` แล้ว Enter ถ้าเห็นประมาณ `Python 3.12.x` หรือใหม่กว่า ข้ามไปขั้นที่ 4
> 3. ถ้า macOS เสนอให้ติดตั้ง **Command Line Developer Tools** กด Install (มี Python 3 รวมอยู่) หรือดาวน์โหลดตัวติดตั้งทางการสำหรับ macOS จาก python.org แล้วรัน
> 4. ไปที่โฟลเดอร์ Vault: พิมพ์ `cd ` (มีเว้นวรรค) ลากโฟลเดอร์ Vault จาก Finder มาใส่หน้าต่าง Terminal แล้ว Enter
> 5. รัน `python3 _tools/quant/sma_crossover.py` ไม่ต้องติดตั้งแพ็กเกจเพิ่ม และเสร็จในไม่กี่วินาที
> 6. **แล้วไง?** ถ้าผลของคุณตรงกับกล่องด้านล่างเป๊ะ แปลว่าเครื่องพร้อมและตัวเลขในบทนี้ทำซ้ำได้ ถ้าไม่ตรง มีบางอย่างต่างไป (เวอร์ชัน Python ไฟล์ถูกแก้) และคุณได้เรียนรู้เรื่องนี้ก่อนจะเชื่อผลใด ๆ

ผลลัพธ์จริงของสคริปต์ (ข้อมูลสังเคราะห์ seed 42):

""" + OUTPUT + """

> [!check]- เช็กความเข้าใจ: การรันสคริปต์
> **Q1.** สคริปต์พิมพ์ "bars: 2016 in-sample: 1411 out-of-sample: 605" ตัวเลขสามตัวหมายถึงอะไร?
> > [!answer]-
> > ราคารายวันทั้งหมด 2,016 วัน 1,411 วันแรก (70%) ใช้เลือกค่าเส้นค่าเฉลี่ย 605 วันสุดท้าย (30%) เก็บไว้ตัดสิน
""")
L.before_heading("th", "3.", """
**ฟังก์ชันเดียวกัน อธิบายทุกบรรทัด:**

""" + CODE_TH + """

> [!walkthrough] ไล่ทีละขั้น: ลูปบนสี่วันจิ๋ว
> ราคา **100, 101, 103, 102** โพซิชันจากสัญญาณ **0, 1, 1, 0** (ไม่ถือ Long Long ไม่ถือ) ต้นทุน 0.10%
> 1. **วันที่ 1:** ถือโพซิชันของเมื่อวาน (0) → ผลตอบแทน **0%**
> 2. **วันที่ 2:** ถือโพซิชัน 1 (ตัดสินตอนปิดวันที่ 1) ราคา 101 → 103 = **+1.98%** โพซิชันเปลี่ยน (0 → 1) ตอนเปิดวันนี้ → หัก 0.10% = **+1.88%**
> 3. **วันที่ 3:** ถือ 1 ราคา 103 → 102 = **−0.97%** โพซิชันไม่เปลี่ยน → ไม่มีต้นทุน
> 4. สัญญาณของวันที่ 3 คือ 0 การออก (และต้นทุน 0.10%) จึงเกิดตอนเปิดวันที่ 4
> 5. **แล้วไง?** ผลตอบแทนของแต่ละวันใช้แค่ข้อมูลจากวันก่อน ถ้าเปลี่ยน `pos[i - 1]` เป็น `pos[i]` กลยุทธ์จะ "รู้" ราคาปิดวันนี้ก่อนเทรดตอนเปิดวันนี้: บั๊ก Look-ahead เล็ก ๆ ที่ทำให้ Backtest ไหนก็ดูยอดเยี่ยม

> [!check]- เช็กความเข้าใจ: โค้ด
> **Q1.** ทำไมโค้ดใช้ `held = pos[i - 1]` ไม่ใช่ `pos[i]`?
> > [!answer]-
> > สัญญาณคำนวณจากราคาปิดวัน i−1 จึงเทรดได้ตั้งแต่วัน i เป็นต้นไป การใช้ pos[i] คือการเทรดด้วยข้อมูลที่ยังไม่มี (Look-ahead bias)
""")
L.before_callout("th", "example", """
> [!analogy]
> สคริปต์ Backtest เหมือน **สูตรอาหารที่หุ่นยนต์ทำตาม** หุ่นยนต์ไม่เคย "เติมเกลืออีกนิดเพราะรู้สึกว่าใช่" ถ้าอาหารไม่อร่อย คุณรู้ว่าเป็นที่สูตร แต่หุ่นยนต์ก็ทำตามคำสั่งที่ผิดได้อย่างสมบูรณ์แบบเช่นกัน: ถ้าสูตรบอกให้ชิมซุปของพรุ่งนี้ หุ่นยนต์ก็ทำอย่างเต็มใจ และผลลัพธ์ก็เป็นเรื่องแต่ง
>
> **จุดที่เปรียบเทียบไม่ได้:** หุ่นยนต์ทำอาหารจะสังเกตว่าซุปของพรุ่งนี้ยังไม่มี แต่โค้ดไม่สังเกต Look-ahead หรือ Survivorship คุณต้องตรวจสูตรเอง

> [!check]- เช็กความเข้าใจ: ผลลัพธ์
> **Q1.** ใน In-sample กลยุทธ์ชนะการซื้อแล้วถือ แต่ใน Out-of-sample ไม่ชนะ ผลไหนควรเป็นตัวกำหนดความคาดหวังของคุณ และเพราะอะไร?
> > [!answer]-
> > Out-of-sample: ค่าถูกเลือกให้ดูดีใน In-sample ส่วนนั้นจึงดูดีเกินจริง ข้อมูลที่ไม่เคยเห็นคือการประเมินที่ซื่อสัตย์ (และก็ยังมาจากแค่ 3 ไม้)
""")
L.before_callout("th", "action", """
> [!market]
> - **หุ้นและดัชนี:** ดาวน์โหลดราคาปิดรายวันของ ETF ดัชนี (เช่น SPY) เป็น CSV ใช้ 252 วันซื้อขายต่อปีได้ถูกต้อง
> - **ฟอเร็กซ์และทองคำ:** ข้อมูลรายวันซื้อขายราว 5 วันต่อสัปดาห์ (~260 แท่งต่อปี) ต้นทุนต่างกัน จึงต้องเปลี่ยน `COST` *(ดู 0.1)*
> - **คริปโต:** ซื้อขาย 365 วันต่อปี การปรับเป็นรายปีด้วย √252 จึงคลาดเคลื่อน ให้ใช้ 365 ในโค้ดตัวชี้วัด *(ดู 0.7)*

> [!caution]
> สคริปต์ที่รันได้โดยไม่มี Error ก็ยังผิดได้ ก่อนเชื่อ Backtest ใด ๆ ให้อ่านโค้ดทีละบรรทัด ทำตัวเลขซ้ำให้ได้ ทดสอบกับข้อมูลจริงและตลาดอื่น และอย่าข้ามจาก Backtest ไปใช้เงินจริงทันที: Forward test ก่อน *(ดู 9.3)*
""")
L.at_end("th", """
> [!check]- ทดสอบสุดท้าย
> **Q1.** บอกกฎความซื่อสัตย์สามข้อที่ฝังอยู่ในสคริปต์
> > [!answer]-
> > ไม่มี Look-ahead (สัญญาณวัน t เทรดวัน t+1) คิดต้นทุนทุกครั้งที่โพซิชันเปลี่ยน และเลือกค่าจาก 70% แรกเท่านั้น ตัดสินด้วย 30% สุดท้าย
> **Q2.** จุดอ่อนที่ใหญ่ที่สุดของข้อสรุปจากการทดสอบนี้คืออะไร?
> > [!answer]-
> > จำนวนไม้น้อยเกินไปมาก (In-sample 8 ไม้ Out-of-sample 3 ไม้) บนข้อมูลสังเคราะห์ชุดเดียว สรุปอะไรเรื่องความได้เปรียบจากตัวอย่างนี้ไม่ได้
""")

L.set_meta("level", "v2")
L.save()
