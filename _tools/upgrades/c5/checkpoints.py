"""C5 · add 0.13-0.15 to the Phase 0 checkpoint (takeaway rows + quiz questions). Additive, idempotent."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

# reuse the insertion helpers from C1 without re-running its edits
src = (ROOT / "_tools/upgrades/c1/checkpoints.py").read_text(encoding="utf-8")
helpers = src[src.index("def insert_rows"):src.index("for rel, langs in ADD.items():")]
exec(helpers)

ADD = {
    "00 Markets, Brokers & News/0.10 Checkpoint- Phase 0 Review.md": {
        "en": {"heading": "## Key takeaways",
               "rows": ["| 0.13 TradingView Basics | Seven parts of the screen; watch for D (delayed). Few drawings, ≤ 2 indicators, the position tool for size, alerts instead of screen-staring. Log scale for long histories. |",
                        "| 0.14 Calendars & Screeners | Calendar on UTC+7, top importance; know time, forecast and your floor before a release. Europe and the US change clocks on different dates. A screener gives a study list, not a buy list. |",
                        "| 0.15 Prop Firms | A paid test on a demo account. About 14% pass and 7% get paid (FPFX). Loss rules, not targets, end challenges; risk ≤ 0.5% and set a fee budget. |"],
               "quiz": """Q: On a 10,000 USD account, the long-position tool shows entry 1.0850 and stop 1.0830 on EUR/USD. You risk 1%. What size should it show?
* 0.50 lots
- 0.05 lots
- 5.00 lots
E: 100 USD ÷ (20 pips × 10 USD per pip per lot) = 0.50 lots (see 0.13).
Q: The FOMC decision is at 14:00 New York time on Wednesday 9 December 2026. When is that in Bangkok?
- Wednesday 9 December, 02:00
- Thursday 10 December, 01:00
* Thursday 10 December, 02:00
E: The US is on winter time (UTC−5) in December, so the gap is 12 hours (see 0.14).
Q: In the simulation, a zero-edge trader risking 1% per trade passes phase 1 (+10% before −10%) about how often?
- About 5%
* About 50%
- About 90%
E: 50.0% of 20,000 runs: with no edge and equal barriers it is a coin flip, so passing proves little (see 0.15)."""},
        "th": {"heading": "## ประเด็นสำคัญ",
               "rows": ["| 0.13 พื้นฐาน TradingView | เจ็ดส่วนของหน้าจอ ระวังตัว D (ล่าช้า) รูปวาดน้อย อินดิเคเตอร์ ≤ 2 ตัว ใช้เครื่องมือ Position หาขนาด ใช้การแจ้งเตือนแทนการจ้องจอ ใช้สเกล Log กับข้อมูลระยะยาว |",
                        "| 0.14 ปฏิทิน & Screener | ตั้งปฏิทินเป็น UTC+7 ความสำคัญสูงสุด รู้เวลา ค่าคาดการณ์ และพื้นของคุณก่อนข่าวออก ยุโรปกับสหรัฐฯ เปลี่ยนเวลาคนละวัน Screener ให้รายการศึกษา ไม่ใช่รายการซื้อ |",
                        "| 0.15 Prop Firm | การสอบแบบเสียเงินบนบัญชีเดโม ผ่านราว 14% ได้เงินจริง 7% (FPFX) กฎขาดทุน ไม่ใช่เป้ากำไร ที่ทำให้ Challenge จบ เสี่ยง ≤ 0.5% และตั้งงบค่าธรรมเนียม |"],
               "quiz": """Q: บนบัญชี 10,000 USD เครื่องมือ Long Position แสดงจุดเข้า 1.0850 และ Stop 1.0830 บน EUR/USD คุณเสี่ยง 1% ควรแสดงขนาดเท่าไร?
* 0.50 ล็อต
- 0.05 ล็อต
- 5.00 ล็อต
E: 100 USD ÷ (20 pips × 10 USD ต่อ pip ต่อล็อต) = 0.50 ล็อต (ดู 0.13)
Q: FOMC ตัดสินเวลา 14:00 นิวยอร์ก วันพุธ 9 ธันวาคม 2026 ตรงกับเวลากรุงเทพฯ เมื่อไร?
- วันพุธ 9 ธันวาคม 02:00
- วันพฤหัสบดี 10 ธันวาคม 01:00
* วันพฤหัสบดี 10 ธันวาคม 02:00
E: เดือนธันวาคมสหรัฐฯ ใช้เวลาฤดูหนาว (UTC−5) จึงห่างกัน 12 ชั่วโมง (ดู 0.14)
Q: ในการจำลอง เทรดเดอร์ที่ไม่มีความได้เปรียบ เสี่ยง 1% ต่อเทรด ผ่านเฟส 1 (+10% ก่อน −10%) บ่อยแค่ไหน?
- ราว 5%
* ราว 50%
- ราว 90%
E: 50.0% จาก 20,000 รอบ: เมื่อไม่มีความได้เปรียบและเส้นทั้งสองห่างเท่ากัน มันคือการโยนเหรียญ การผ่านจึงพิสูจน์ได้น้อย (ดู 0.15)"""},
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
