"""C4 · add 10.9-10.14 to the Phase 10 checkpoint (takeaway rows + quiz questions). Additive, idempotent."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

# reuse the insertion helpers from C1 without re-running its edits
src = (ROOT / "_tools/upgrades/c1/checkpoints.py").read_text(encoding="utf-8")
helpers = src[src.index("def insert_rows"):src.index("for rel, langs in ADD.items():")]
exec(helpers)

ADD = {
    "10 Macro, Wall Street & Investing/10.8 Checkpoint- Phase 10 Review.md": {
        "en": {"heading": "## Key takeaways",
               "rows": ["| 10.9 Index funds & ETFs | Own the whole market at low cost; over 15–20 years about 9 in 10 active US large-cap funds trailed the index. Compare TER and tracking difference. |",
                        "| 10.10 DCA vs lump sum | A lump sum invested at once won about 81% of 12-month windows (S&P 500, 1988–2025); DCA is for behaviour, and salary investing is DCA by default. |",
                        "| 10.11 Bonds | Ask who you lend to and for how long. Long bonds fall most when yields rise; debentures aren't deposits. |",
                        "| 10.12 Dividends | Judge total return after tax; the price drops on XD; a very high yield is often a warning. |",
                        "| 10.13 REITs | Property income with stock-like risk and rate sensitivity; check occupancy, leases, gearing and NAV. |",
                        "| 10.14 Thailand & Laos | Know your routes, costs and tax rules (dated); tax deductions are worth your top rate; re-check every year. |"],
               "quiz": """Q: Two funds track the same index. One charges 0.05% a year, the other 1.5%. Over 30 years at 7% before fees, roughly how much more does 1,000,000 become in the cheap fund?
- About 15,000
- About 450,000
* About 2,660,000
E: 7,498,895 vs 4,837,269, a gap of 2,661,626 (see 10.9).
Q: In our S&P 500 test (1988–2025), how often was a lump sum ahead of 12-month DCA after 12 months?
* About 81% of start months
- About 50%, a coin flip
- About 19% of start months
E: 367 of 453 start months. Vanguard's 2023 study, with interest on waiting cash, found about two-thirds (see 10.10).
Q: Yields rise from 4% to 5%. Which 4%-coupon bond falls most?
- The 2-year bond
- The 10-year bond
* The 30-year bond
E: 98.14, 92.28 and 84.63: the longer the bond, the bigger the fall (see 10.11).
Q: A share at 50 pays a 2 baht dividend. On the XD day, what usually happens?
- The price stays at 50 and you gain 2 baht
* The price opens near 48; you receive 2 baht less 10% tax
- The price rises because of the dividend
E: The dividend leaves the company, so the price falls by about the dividend (see 10.12).
Q: A REIT trades at 8, its NAV is 10 and it pays 0.56 a year. Yield and discount?
- 5.6% yield, 25% discount
* 7% yield, 20% discount
- 7% yield, 25% premium
E: 0.56 ÷ 8 = 7%; 1 − 8 ÷ 10 = 20% (see 10.13).
Q: Your net income is 900,000 baht. Roughly what does a 100,000 baht ThaiESG purchase save in tax (rules as of Oct 2026)?
- 5,000
- 35,000
* 20,000
E: It comes off your 20% bracket: tax falls from 95,000 to 75,000 (see 10.14)."""},
        "th": {"heading": "## ประเด็นสำคัญ",
               "rows": ["| 10.9 กองทุนดัชนี & ETF | ถือทั้งตลาดด้วยต้นทุนต่ำ ใน 15–20 ปี กองทุนหุ้นใหญ่สหรัฐฯ เชิงรุกราว 9 ใน 10 แพ้ดัชนี เทียบ TER และส่วนต่างการติดตาม |",
                        "| 10.10 DCA vs ก้อนเดียว | การลงทุนก้อนเดียวทันทีชนะราว 81% ของช่วง 12 เดือน (S&P 500, 1988–2025) DCA มีไว้เพื่อพฤติกรรม และการลงทุนจากเงินเดือนคือ DCA โดยธรรมชาติ |",
                        "| 10.11 พันธบัตร | ถามว่าให้ใครกู้และนานเท่าไร พันธบัตรยาวร่วงมากที่สุดเมื่อผลตอบแทนขึ้น หุ้นกู้ไม่ใช่เงินฝาก |",
                        "| 10.12 ปันผล | ตัดสินจากผลตอบแทนรวมหลังภาษี ราคาลดลงในวัน XD อัตราปันผลที่สูงมากมักเป็นสัญญาณเตือน |",
                        "| 10.13 REIT | รายได้จากอสังหาฯ ที่มีความเสี่ยงแบบหุ้นและอ่อนไหวต่อดอกเบี้ย ตรวจอัตราการเช่า สัญญาเช่า Gearing และ NAV |",
                        "| 10.14 ไทย & ลาว | รู้ช่องทาง ต้นทุน และกฎภาษี (ระบุวันที่) ค่าลดหย่อนมีค่าเท่าอัตราภาษีขั้นสูงสุด ตรวจซ้ำทุกปี |"],
               "quiz": """Q: กองทุนสองกองติดตามดัชนีเดียวกัน กองหนึ่งเก็บ 0.05% ต่อปี อีกกอง 1.5% ใน 30 ปีที่ 7% ก่อนค่าธรรมเนียม เงิน 1,000,000 ในกองถูกจะมากกว่าราวเท่าไร?
- ราว 15,000
- ราว 450,000
* ราว 2,660,000
E: 7,498,895 vs 4,837,269 ส่วนต่าง 2,661,626 (ดู 10.9)
Q: ในการทดสอบ S&P 500 ของเรา (1988–2025) ก้อนเดียวนำ DCA 12 เดือนหลัง 12 เดือนบ่อยแค่ไหน?
* ราว 81% ของเดือนเริ่มต้น
- ราว 50% เหมือนโยนเหรียญ
- ราว 19% ของเดือนเริ่มต้น
E: 367 จาก 453 เดือนเริ่มต้น งานวิจัย Vanguard ปี 2023 ซึ่งให้ดอกเบี้ยกับเงินสดที่รอ พบราวสองในสาม (ดู 10.10)
Q: ผลตอบแทนขึ้นจาก 4% เป็น 5% พันธบัตรคูปอง 4% ตัวไหนร่วงมากที่สุด?
- พันธบัตร 2 ปี
- พันธบัตร 10 ปี
* พันธบัตร 30 ปี
E: 98.14, 92.28 และ 84.63: พันธบัตรยิ่งยาว ยิ่งร่วงมาก (ดู 10.11)
Q: หุ้นราคา 50 จ่ายปันผล 2 บาท ในวัน XD มักเกิดอะไรขึ้น?
- ราคาคงที่ที่ 50 และคุณได้กำไร 2 บาท
* ราคาเปิดใกล้ 48 คุณได้ 2 บาทหักภาษี 10%
- ราคาขึ้นเพราะปันผล
E: ปันผลออกจากบริษัท ราคาจึงลดลงราวเท่าปันผล (ดู 10.12)
Q: REIT ซื้อขายที่ 8 NAV คือ 10 และจ่าย 0.56 ต่อปี อัตราผลตอบแทนและส่วนลดเท่าไร?
- ผลตอบแทน 5.6% ส่วนลด 25%
* ผลตอบแทน 7% ส่วนลด 20%
- ผลตอบแทน 7% ส่วนเกิน 25%
E: 0.56 ÷ 8 = 7% และ 1 − 8 ÷ 10 = 20% (ดู 10.13)
Q: เงินได้สุทธิของคุณคือ 900,000 บาท การซื้อ ThaiESG 100,000 บาทประหยัดภาษีราวเท่าไร (กฎ ณ ต.ค. 2026)?
- 5,000
- 35,000
* 20,000
E: หักออกจากขั้นภาษี 20%: ภาษีลดจาก 95,000 เป็น 75,000 (ดู 10.14)"""},
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
