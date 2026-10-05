/* Position-size calculator (Trader's Path). Pure maths in sizeTrade(); UI wiring below.
   Money values are in the account currency. Forex presets assume a USD account. */
(function (root) {
  var MARKETS = {
    fx_usd_quote: { contract: 100000, step: 0.01, pip: 0.0001, unit: "lots" },  // EUR/USD, GBP/USD, AUD/USD…
    fx_usd_base:  { contract: 100000, step: 0.01, pip: 0.0001, unit: "lots", base: true }, // USD/CHF, USD/CAD
    fx_usd_jpy:   { contract: 100000, step: 0.01, pip: 0.01, unit: "lots", base: true },   // USD/JPY
    gold:         { contract: 100, step: 0.01, unit: "lots" },                 // XAU/USD, 1 lot = 100 oz
    stock:        { contract: 1, step: 1, unit: "shares" },                    // board lot set by the user
    crypto:       { contract: 1, step: 0.0001, unit: "units" },
    custom:       { contract: 1, step: 0.01, unit: "lots" }
  };

  function floorTo(x, step) {
    var n = Math.floor(x / step + 1e-9);
    return +(n * step).toFixed(8);
  }

  /* inp: {market, balance, riskPct, entry, stop, target?, boardLot?, valuePerPoint?, step?} */
  function sizeTrade(inp) {
    var m = MARKETS[inp.market];
    if (!m) return { error: "market" };
    var bal = +inp.balance, rp = +inp.riskPct, e = +inp.entry, s = +inp.stop, t = inp.target === "" || inp.target == null ? null : +inp.target;
    if (!(bal > 0) || !(rp > 0) || !(e > 0) || !(s > 0)) return { error: "input" };
    if (e === s) return { error: "stop" };
    var long = s < e;
    if (t !== null && (long ? t <= e : t >= e)) return { error: "target" };
    var dist = Math.abs(e - s);
    // money lost per 1 lot/share/unit if the stop is hit
    var perUnit;
    if (inp.market === "custom") perUnit = dist * (+inp.valuePerPoint || 0);
    else if (m.base) perUnit = dist * m.contract / e;       // P&L in the quote currency converted at the entry price
    else perUnit = dist * m.contract;
    if (!(perUnit > 0)) return { error: "input" };
    var step = inp.market === "stock" ? Math.max(1, Math.round(+inp.boardLot || 1)) : (inp.market === "custom" ? (+inp.step || m.step) : m.step);
    var riskMoney = bal * rp / 100;
    var raw = riskMoney / perUnit;
    var size = floorTo(raw, step);
    var out = {
      long: long, riskMoney: riskMoney, distance: dist, pips: m.pip ? dist / m.pip : null,
      perUnit: perUnit, rawSize: raw, size: size, unit: m.unit, step: step,
      actualRisk: size * perUnit, actualRiskPct: 100 * size * perUnit / bal
    };
    if (t !== null) {
      var rd = Math.abs(t - e);
      out.rr = rd / dist;
      out.reward = size * perUnit * rd / dist;
    }
    return out;
  }

  root.TPCalc = { sizeTrade: sizeTrade, MARKETS: MARKETS, floorTo: floorTo };
  if (typeof module !== "undefined") module.exports = root.TPCalc;

  // ---------------------------------------------------------------- UI
  if (typeof document === "undefined") return;
  var form = document.getElementById("calc");
  if (!form) return;
  var th = function () { return document.documentElement.getAttribute("data-lang") === "th"; };
  var U = { lots: ["lots", "ล็อต"], shares: ["shares", "หุ้น"], units: ["units", "หน่วย"] };
  var ERR = {
    input: ["Fill in balance, risk %, entry and stop with positive numbers.", "กรอกยอดเงิน % ความเสี่ยง จุดเข้า และ Stop เป็นตัวเลขบวก"],
    stop: ["The stop can't equal the entry.", "Stop ต้องไม่เท่ากับจุดเข้า"],
    target: ["The target must be on the profit side of the entry.", "เป้าต้องอยู่ฝั่งกำไรของจุดเข้า"]
  };
  function fmt(x, d) { return Number(x).toLocaleString("en-US", { minimumFractionDigits: d, maximumFractionDigits: d }); }
  function dec(step) { var s = String(step); return s.indexOf(".") < 0 ? 0 : s.split(".")[1].length; }
  function v(id) { return document.getElementById(id).value; }
  document.querySelectorAll("#c-market option").forEach(function (o) { o.setAttribute("data-en", o.textContent); });
  function show() {
    document.querySelectorAll("#c-market option").forEach(function (o) { o.textContent = o.getAttribute(th() ? "data-th" : "data-en"); });
    var mk = v("c-market");
    document.querySelectorAll("[data-only]").forEach(function (el) {
      el.hidden = el.getAttribute("data-only").split(" ").indexOf(mk) < 0;
    });
    var r = sizeTrade({ market: mk, balance: v("c-balance"), riskPct: v("c-risk"), entry: v("c-entry"), stop: v("c-stop"),
      target: v("c-target"), boardLot: v("c-board"), valuePerPoint: v("c-vpp"), step: v("c-step") });
    var out = document.getElementById("c-out"), L = th() ? 1 : 0;
    if (r.error) { out.innerHTML = '<p class="calc-err">' + ERR[r.error][L] + "</p>"; return; }
    var u = U[r.unit][L], rows = [];
    function row(a, b, cls) { rows.push('<div class="calc-row ' + (cls || "") + '"><span>' + a + "</span><b>" + b + "</b></div>"); }
    row(L ? "ทิศทาง" : "Direction", r.long ? (L ? "Long (ซื้อ)" : "Long (buy)") : (L ? "Short (ขาย)" : "Short (sell)"));
    row(L ? "เงินที่ยอมเสี่ยง" : "Money at risk", fmt(r.riskMoney, 2));
    row(L ? "ระยะ Stop" : "Stop distance", fmt(r.distance, 5).replace(/0+$/, "").replace(/\.$/, "") + (r.pips !== null ? " (" + fmt(r.pips, 1) + " pips)" : ""));
    row(L ? "ขาดทุนต่อ 1 " + u : "Loss per 1 " + u.replace(/s$/, ""), fmt(r.perUnit, 2));
    row(L ? "ขนาดสถานะ" : "Position size", fmt(r.size, dec(r.step)) + " " + u, "big");
    row(L ? "ความเสี่ยงจริงหลังปัดเศษ" : "Actual risk after rounding", fmt(r.actualRisk, 2) + " (" + fmt(r.actualRiskPct, 2) + "%)");
    if (r.rr !== undefined) {
      row("Risk : Reward", "1 : " + fmt(r.rr, 2));
      row(L ? "กำไรถ้าถึงเป้า" : "Profit at target", fmt(r.reward, 2));
    }
    var warn = [];
    if (r.size === 0) warn.push(L ? "ขนาดที่ปัดแล้วเป็น 0: Stop กว้างเกินไปหรือบัญชีเล็กเกินไปสำหรับตลาดนี้ อย่าเพิ่มความเสี่ยงเพื่อให้เทรดได้" :
      "Rounded size is 0: the stop is too wide or the account too small for this market. Don't raise the risk to make it fit.");
    if (+v("c-risk") > 2) warn.push(L ? "ความเสี่ยงเกิน 2% ต่อเทรด บทเรียน 3.1–3.2 แนะนำ 0.5–1%" : "Risk above 2% per trade. Lessons 3.1–3.2 suggest 0.5–1%.");
    out.innerHTML = rows.join("") + warn.map(function (w) { return '<p class="calc-warn">⚠ ' + w + "</p>"; }).join("");
  }
  form.addEventListener("input", show);
  document.querySelectorAll("[data-set-lang]").forEach(function (b) { b.addEventListener("click", function () { setTimeout(show, 0); }); });
  show();
})(typeof window !== "undefined" ? window : this);
