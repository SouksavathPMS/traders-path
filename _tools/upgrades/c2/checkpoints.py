"""C2 · add 0.12, 3.8 and 3.9 to their phase checkpoints (takeaway rows + quiz questions). Additive, idempotent."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

# reuse the insertion helpers from C1 without re-running its edits
src = (ROOT / "_tools/upgrades/c1/checkpoints.py").read_text(encoding="utf-8")
helpers = src[src.index("def insert_rows"):src.index("for rel, langs in ADD.items():")]
exec(helpers)

ADD = {
    "00 Markets, Brokers & News/0.10 Checkpoint- Phase 0 Review.md": {
        "en": {"heading": "## Key takeaways",
               "rows": ["| 0.12 Short Selling | Borrow, sell, buy back, return. You pay borrow fees and dividends; losses have no ceiling; crowded shorts squeeze. Check local rules first. |"],
               "quiz": """Q: You short 100 shares at 50 and the price rises to 150. What is the loss before costs?
- 5,000, the most a short can lose
- 50, one share's worth
* 10,000, and it could keep growing
E: (50 − 150) × 100 = −10,000. A short's loss has no ceiling (see 0.12).
Q: A stock has a 50% yearly borrow fee and short interest near 100% of the float. What does this tell you?
- It's a safe, popular short
* The short side is crowded: costly to hold and at high risk of a squeeze
- The stock will fall soon
E: A high fee and high short interest mean many forced buyers if the price rises (see 0.12)."""},
        "th": {"heading": "## ประเด็นสำคัญ",
               "rows": ["| 0.12 การขายชอร์ต | ยืม ขาย ซื้อคืน คืนหุ้น คุณจ่ายค่ายืมและปันผล การขาดทุนไม่มีเพดาน หุ้นที่ถูกชอร์ตแออัดเกิด Squeeze ได้ ตรวจกฎในประเทศก่อน |"],
               "quiz": """Q: คุณชอร์ต 100 หุ้นที่ 50 และราคาขึ้นไป 150 ขาดทุนก่อนต้นทุนเท่าไร?
- 5,000 ซึ่งเป็นการขาดทุนสูงสุดของการชอร์ต
- 50 เท่ากับราคาหุ้นหนึ่งหุ้น
* 10,000 และอาจโตขึ้นอีก
E: (50 − 150) × 100 = −10,000 การขาดทุนของการชอร์ตไม่มีเพดาน (ดู 0.12)
Q: หุ้นตัวหนึ่งมีค่ายืม 50% ต่อปี และ Short interest ใกล้ 100% ของ Float บอกอะไรคุณ?
- เป็นหุ้นที่ชอร์ตได้ปลอดภัยและเป็นที่นิยม
* ฝั่งชอร์ตแออัด: ถือแพงและเสี่ยง Squeeze สูง
- หุ้นจะลงเร็ว ๆ นี้
E: ค่ายืมสูงและ Short interest สูงหมายถึงผู้ซื้อที่ถูกบังคับจำนวนมากถ้าราคาขึ้น (ดู 0.12)"""},
    },
    "03 Risk & Money Management/3.7 Checkpoint- Phase 3 Review.md": {
        "en": {"heading": "## Key takeaways",
               "rows": ["| 3.8 Trade Management | Management reshapes wins and losses but can't create an edge. One written method per setup; only move stops towards less risk; never average down. |",
                        "| 3.9 Portfolio Risk | Correlated trades are one bet. Kelly assumes perfect knowledge; use a small fraction or 0.5–1%. Simulate drawdowns before they happen. |"],
               "quiz": """Q: A simulation with no edge tests five exit methods. What should their average results be?
- The trailing stop should win clearly
* All close to 0R; management can't create an edge
- The 3R target should be best because it wins more
E: In 3.8's simulation every method averaged within ±0.02R of zero when there was no edge.
Q: Win rate 45%, average win 2R. What is the Kelly fraction?
- 45%
- 2%
* 17.5%
E: 0.45 − 0.55 ÷ 2 = 0.175. Real traders use a small fraction of it, because their estimates are uncertain (see 3.9).
Q: You hold long EUR/USD, long GBP/USD and long gold at 1% each. How should you count them against an open-risk limit?
* Mostly as one dollar bet: they tend to win and lose together
- As three unrelated 1% risks
- As zero risk, because they hedge each other
E: Correlated positions behave like one bigger position (see 3.9)."""},
        "th": {"heading": "## ประเด็นสำคัญ",
               "rows": ["| 3.8 การบริหารเทรด | การบริหารเปลี่ยนรูปกำไรขาดทุน แต่สร้างความได้เปรียบไม่ได้ ใช้หนึ่งวิธีที่เขียนไว้ต่อ Setup เลื่อน Stop ได้เฉพาะทางที่ลดความเสี่ยง ห้ามถัวขาลง |",
                        "| 3.9 ความเสี่ยงระดับพอร์ต | เทรดที่สัมพันธ์กันคือเดิมพันเดียว Kelly สมมติว่ารู้ทุกอย่าง ใช้เศษส่วนเล็ก ๆ หรือ 0.5–1% จำลอง Drawdown ก่อนที่มันจะเกิด |"],
               "quiz": """Q: การจำลองที่ไม่มีความได้เปรียบทดสอบวิธีออกห้าแบบ ผลเฉลี่ยควรเป็นอย่างไร?
- Trailing stop ควรชนะชัดเจน
* ทั้งหมดใกล้ 0R การบริหารสร้างความได้เปรียบไม่ได้
- เป้า 3R ควรดีที่สุดเพราะชนะบ่อยกว่า
E: ในการจำลองของบท 3.8 ทุกวิธีเฉลี่ยอยู่ในช่วง ±0.02R รอบศูนย์เมื่อไม่มีความได้เปรียบ
Q: อัตราชนะ 45% กำไรเฉลี่ย 2R สัดส่วน Kelly คือเท่าไร?
- 45%
- 2%
* 17.5%
E: 0.45 − 0.55 ÷ 2 = 0.175 นักเทรดจริงใช้แค่เศษส่วนเล็ก ๆ เพราะค่าประมาณของพวกเขาไม่แน่นอน (ดู 3.9)
Q: คุณถือซื้อ EUR/USD ซื้อ GBP/USD และซื้อทอง ไม้ละ 1% ควรนับอย่างไรเทียบกับขีดจำกัดความเสี่ยงที่เปิดอยู่?
* ส่วนใหญ่เป็นเดิมพันดอลลาร์ครั้งเดียว: มักชนะและแพ้พร้อมกัน
- เป็นความเสี่ยง 1% สามก้อนที่ไม่เกี่ยวกัน
- เป็นศูนย์ เพราะมันป้องกันความเสี่ยงให้กันและกัน
E: โพซิชันที่สัมพันธ์กันทำตัวเหมือนโพซิชันใหญ่ไม้เดียว (ดู 3.9)"""},
    },
}

for rel, langs in ADD.items():
    p = ROOT / rel
    en, th = p.read_text(encoding="utf-8").split("%% TH %%")
    out, added = [], 0
    for part, lang in ((en, "en"), (th, "th")):
        spec = langs[lang]
        lines = part.split("\n")
        if spec["rows"][0] not in part:
            lines = insert_rows(lines, spec["heading"], spec["rows"])
            added += len(spec["rows"])
        if spec["quiz"].split("\n")[0] not in part:
            lines = insert_quiz(lines, lines.index(spec["heading"]), spec["quiz"])
            added += spec["quiz"].count("\nQ: ") + 1
        out.append("\n".join(lines))
    p.write_text("%% TH %%".join(out), encoding="utf-8")
    print(f"{p.name}: +{added} rows/questions")
