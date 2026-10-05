"""C1 · add the new lessons (0.11, 2.8, 2.9) to their phase checkpoints: takeaway rows + quiz questions.
Additive and idempotent: inserts table rows after the last takeaway row and questions before the quiz's closing fence."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

ADD = {
    "00 Markets, Brokers & News/0.10 Checkpoint- Phase 0 Review.md": {
        "en": {
            "heading": "## Key takeaways",
            "rows": ["| 0.11 Personal Finance First | Budget → starter emergency fund → pay off high-interest debt → 3–6 month fund → long-term investing → trading with risk capital only. |"],
            "quiz": """Q: You have 30,000 THB on a credit card at 16% a year and 30,000 THB you planned to trade with. What's the better move?
* Pay off the card first: a guaranteed 16% a year saved
- Trade it: a good month could pay the card off faster
- Split it 50/50 between the card and trading
E: Repaying 16% debt is a guaranteed, risk-free return that very few trades can beat (see 0.11).
Q: Savings 300,000 THB, essentials 20,000 THB a month, nothing needed within 3 years. Using a 6-month emergency fund and the 10% rule, what's the largest trading account?
- 30,000 THB
- 6,000 THB
* 18,000 THB
E: Fund 6 × 20,000 = 120,000 → investable 180,000 → trading ≤ 10% = 18,000 THB (see 0.11).""",
        },
        "th": {
            "heading": "## ประเด็นสำคัญ",
            "rows": ["| 0.11 การเงินส่วนตัวมาก่อน | ทำงบ → เงินสำรองฉุกเฉินเริ่มต้น → ปลดหนี้ดอกเบี้ยสูง → เงินสำรอง 3–6 เดือน → ลงทุนระยะยาว → เทรดด้วยเงินที่เสี่ยงได้เท่านั้น |"],
            "quiz": """Q: คุณมีหนี้บัตรเครดิต 30,000 บาทที่ 16% ต่อปี และมีเงิน 30,000 บาทที่ตั้งใจจะเทรด ทางไหนดีกว่า?
* ปลดหนี้บัตรก่อน: ประหยัด 16% ต่อปีแบบแน่นอน
- เทรด: เดือนที่ดีอาจปลดหนี้ได้เร็วกว่า
- แบ่งครึ่งระหว่างหนี้บัตรกับการเทรด
E: การคืนหนี้ 16% คือผลตอบแทนที่แน่นอนและไม่มีความเสี่ยง ซึ่งการเทรดน้อยครั้งจะชนะได้ (ดู 0.11)
Q: เงินออม 300,000 บาท ค่าใช้จ่ายจำเป็น 20,000 บาทต่อเดือน ไม่มีเงินที่ต้องใช้ภายใน 3 ปี ใช้เงินสำรองฉุกเฉิน 6 เดือนและกฎ 10% บัญชีเทรดใหญ่ที่สุดคือเท่าไร?
- 30,000 บาท
- 6,000 บาท
* 18,000 บาท
E: เงินสำรอง 6 × 20,000 = 120,000 → ลงทุนได้ 180,000 → เทรด ≤ 10% = 18,000 บาท (ดู 0.11)""",
        },
    },
    "02 Market Structure/2.7 Checkpoint- Phase 2 Review.md": {
        "en": {
            "heading": "## Key takeaways",
            "rows": ["| 2.8 Indicators | Formulas on past prices: they lag and describe, they don't predict. One per family (trend, momentum, volatility, volume); structure decides. |",
                     "| 2.9 Chart patterns | Structure with a name. Confirm with a close beyond the neckline; prefer the pullback entry; even good patterns fail 16–45% of the time (Bulkowski). |"],
            "quiz": """Q: A daily up-trend is intact and RSI(14) reads 78. What does this tell you?
- Sell now: the market is overbought
* Buying has been strong recently; it is not a reversal signal on its own
- The trend will end within 14 candles
E: RSI describes momentum. In a strong trend it can stay above 70 for many candles (see 2.8).
Q: Why is a 20/50 moving-average crossover late as an exit?
- Because the settings are wrong
- Because moving averages use volume
* Because both averages are built from past closes, so they turn only after price has already turned
E: In 2.8's example the crossover came 14 candles after the top and 12.2 points lower.
Q: A head-and-shoulders top has a head at 120 and a neckline at 110. When is it confirmed, and what's the measured target?
* After a close below 110; target 100
- When the right shoulder forms; target 110
- After a close below 110; target 90
E: Height = 120 − 110 = 10, projected down from the neckline. Bulkowski reports only about half reach it (see 2.9).""",
        },
        "th": {
            "heading": "## ประเด็นสำคัญ",
            "rows": ["| 2.8 อินดิเคเตอร์ | สูตรบนราคาในอดีต: ช้ากว่าราคาและใช้อธิบาย ไม่ใช่ทำนาย ใช้กลุ่มละหนึ่งตัว (เทรนด์ โมเมนตัม ความผันผวน วอลุ่ม) โครงสร้างเป็นตัวตัดสิน |",
                     "| 2.9 รูปแบบกราฟ | โครงสร้างที่มีชื่อเรียก ยืนยันด้วยราคาปิดเลยเส้นคอ เลือกเข้าตอนย่อกลับ แม้รูปแบบที่ดีก็ล้มเหลว 16–45% ของครั้ง (Bulkowski) |"],
            "quiz": """Q: ขาขึ้นรายวันยังสมบูรณ์ และ RSI(14) อยู่ที่ 78 บอกอะไรคุณ?
- ขายเลย: ตลาดซื้อมากเกินไป
* แรงซื้อช่วงหลังแข็งแรง ไม่ใช่สัญญาณกลับตัวด้วยตัวมันเอง
- เทรนด์จะจบภายใน 14 แท่ง
E: RSI อธิบายโมเมนตัม ในเทรนด์ที่แรงมันอยู่เหนือ 70 ได้หลายแท่ง (ดู 2.8)
Q: ทำไมการตัดกันของค่าเฉลี่ย 20/50 จึงช้าเกินไปสำหรับการออก?
- เพราะตั้งค่าผิด
- เพราะค่าเฉลี่ยเคลื่อนที่ใช้วอลุ่ม
* เพราะค่าเฉลี่ยทั้งสองสร้างจากราคาปิดในอดีต จึงกลับทิศหลังจากราคากลับไปแล้ว
E: ในตัวอย่างของบท 2.8 การตัดกันเกิดหลังยอด 14 แท่ง และต่ำกว่า 12.2 จุด
Q: หัวไหล่มีหัวที่ 120 และเส้นคอที่ 110 ยืนยันเมื่อไร และเป้าวัดระยะคือเท่าไร?
* หลังปิดใต้ 110 เป้า 100
- เมื่อไหล่ขวาเกิด เป้า 110
- หลังปิดใต้ 110 เป้า 90
E: ความสูง = 120 − 110 = 10 ฉายลงจากเส้นคอ Bulkowski รายงานว่าถึงเป้าราวครึ่งหนึ่งเท่านั้น (ดู 2.9)""",
        },
    },
}


def insert_rows(lines, heading, rows):
    i = lines.index(heading)
    j = i + 1
    while j < len(lines) and not lines[j].startswith("|"):
        j += 1
    while j < len(lines) and lines[j].startswith("|"):
        j += 1
    return lines[:j] + rows + lines[j:]


def insert_quiz(lines, start, quiz):
    i = next(k for k in range(start, len(lines)) if lines[k] == "```quiz")
    end = next(k for k in range(i + 1, len(lines)) if lines[k] == "```")
    return lines[:end] + quiz.split("\n") + lines[end:]


for rel, langs in ADD.items():
    p = ROOT / rel
    text = p.read_text(encoding="utf-8")
    en, th = text.split("%% TH %%")
    out, added = [], 0
    for part, lang in ((en, "en"), (th, "th")):
        spec = langs[lang]
        lines = part.split("\n")
        if spec["rows"][0] not in part:
            lines = insert_rows(lines, spec["heading"], spec["rows"])
            added += len(spec["rows"])
        first_q = spec["quiz"].split("\n")[0]
        if first_q not in part:
            lines = insert_quiz(lines, lines.index(spec["heading"]), spec["quiz"])
            added += spec["quiz"].count("\nQ: ") + 1
        out.append("\n".join(lines))
    p.write_text("%% TH %%".join(out), encoding="utf-8")
    print(f"{p.name}: +{added} rows/questions")
