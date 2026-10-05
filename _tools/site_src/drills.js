/* Interactive chart drills (Trader's Path, C7). Data: window.DRILLS from assets/drills-data.js,
   generated and answer-checked by _tools/drills/make_drills.py. */
(function () {
  if (!window.DRILLS) return;
  var root = document.documentElement;
  function L() { return root.getAttribute("data-lang") === "th" ? 1 : 0; }
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  var NS = "http://www.w3.org/2000/svg";
  var COL = { bull: "#22c55e", bear: "#ef4444", grid: "rgba(142,160,189,.18)", text: "#8ea0bd", amber: "#f59e0b", blue: "#38bdf8", pink: "#ec4899", teal: "#14b8a6" };
  var OPT = {
    bull: ["Buyers won", "ผู้ซื้อชนะ"], bear: ["Sellers won", "ผู้ขายชนะ"], indecision: ["Nobody: indecision", "ไม่มีใครชนะ: ลังเล"],
    HH: ["HH · higher high", "HH · จุดสูงที่สูงขึ้น"], HL: ["HL · higher low", "HL · จุดต่ำที่สูงขึ้น"],
    LH: ["LH · lower high", "LH · จุดสูงที่ต่ำลง"], LL: ["LL · lower low", "LL · จุดต่ำที่ต่ำลง"],
    up: ["Uptrend", "ขาขึ้น"], down: ["Downtrend", "ขาลง"], range: ["Range", "กรอบ (Range)"],
    bos: ["BOS", "BOS"], choch: ["CHoCH", "CHoCH"], none: ["No break", "ยังไม่เบรก"],
    A: ["Level A", "ระดับ A"], B: ["Level B", "ระดับ B"], C: ["Level C", "ระดับ C"],
    sweep: ["Sweep", "Sweep"], run: ["Run (accepted beyond)", "Run (ยอมรับเลยระดับ)"],
    premium: ["Premium", "Premium"], eq: ["Equilibrium (≈50%)", "Equilibrium (≈50%)"], discount: ["Discount", "Discount"]
  };
  var LINE = { sh: ["last swing high", "จุดสูงล่าสุด"], pl: ["protected low", "จุดต่ำที่ต้องปกป้อง"], old: ["old level", "ระดับเดิม"],
    price: ["last price", "ราคาล่าสุด"], A: ["A", "A"], B: ["B", "B"], C: ["C", "C"] };
  var T = {
    start: ["Start 5 rounds", "เริ่ม 5 รอบ"], next: ["Next →", "ถัดไป →"], again: ["Practise again", "ฝึกอีกครั้ง"],
    right: ["Correct.", "ถูกต้อง"], wrong: ["Not quite.", "ยังไม่ถูก"], round: ["Round", "รอบที่"], score: ["Score", "คะแนน"],
    best: ["Best", "ดีที่สุด"], click: ["Click a candle on the chart.", "คลิกแท่งเทียนบนกราฟ"], lesson: ["Lesson", "บทเรียน"]
  };
  function el(tag, attrs, parent) {
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }
  function txt(parent, x, y, s, size, fill, anchor, weight) {
    var t = el("text", { x: x, y: y, "font-size": size || 12, fill: fill || COL.text, "text-anchor": anchor || "start", "font-weight": weight || 400 }, parent);
    t.textContent = s; return t;
  }

  function chart(r, onPick) {
    var W = 720, H = 340, pl = 14, pr = 64, pt = 16, pb = 26;
    var svg = el("svg", { viewBox: "0 0 " + W + " " + H, class: "drill-svg", role: "img" });
    var lo = Infinity, hi = -Infinity;
    r.c.forEach(function (k) { lo = Math.min(lo, k[2]); hi = Math.max(hi, k[1]); });
    (r.lines || []).forEach(function (l) { lo = Math.min(lo, l.p); hi = Math.max(hi, l.p); });
    if (r.zone) { lo = Math.min(lo, r.zone.lo); hi = Math.max(hi, r.zone.hi); }
    var pad = (hi - lo) * 0.08; lo -= pad; hi += pad;
    var n = r.c.length, step = (W - pl - pr) / n;
    function X(i) { return pl + step * (i + 0.5); }
    function Y(p) { return pt + (H - pt - pb) * (hi - p) / (hi - lo); }
    for (var g = 0; g <= 4; g++) {
      var p = lo + (hi - lo) * g / 4;
      el("line", { x1: pl, x2: W - pr, y1: Y(p), y2: Y(p), stroke: COL.grid }, svg);
      txt(svg, W - pr + 6, Y(p) + 4, p.toFixed(2), 11);
    }
    if (r.zone) {
      el("rect", { x: pl, width: W - pl - pr, y: Y(r.zone.hi), height: Y(r.zone.lo) - Y(r.zone.hi), fill: COL.blue, "fill-opacity": .07 }, svg);
      var eq = (r.zone.lo + r.zone.hi) / 2;
      el("line", { x1: pl, x2: W - pr, y1: Y(eq), y2: Y(eq), stroke: COL.blue, "stroke-dasharray": "6 5" }, svg);
      txt(svg, pl + 4, Y(eq) - 5, "EQ 50% " + eq.toFixed(2), 11, COL.blue);
      txt(svg, pl + 4, Y(r.zone.hi) + 14, L() ? "Premium (ครึ่งบน)" : "Premium (upper half)", 11, COL.text);
      txt(svg, pl + 4, Y(r.zone.lo) - 6, L() ? "Discount (ครึ่งล่าง)" : "Discount (lower half)", 11, COL.text);
    }
    if (r.hl !== undefined) el("rect", { x: X(r.hl) - step / 2, width: step, y: pt, height: H - pt - pb, fill: COL.amber, "fill-opacity": .12, rx: 4 }, svg);
    var bodies = [];
    r.c.forEach(function (k, i) {
      var up = k[3] >= k[0], col = up ? COL.bull : COL.bear;
      el("line", { x1: X(i), x2: X(i), y1: Y(k[1]), y2: Y(k[2]), stroke: col, "stroke-width": 1.6 }, svg);
      var top = Y(Math.max(k[0], k[3])), h = Math.max(Math.abs(Y(k[0]) - Y(k[3])), 1.5);
      bodies.push(el("rect", { x: X(i) - step * 0.3, width: step * 0.6, y: top, height: h, fill: col, rx: 1.5 }, svg));
      txt(svg, X(i), H - 8, String(i + 1), 10, COL.text, "middle");
    });
    (r.lines || []).forEach(function (l) {
      var c = /^[ABC]$/.test(l.k) ? COL.pink : l.k === "price" ? COL.teal : COL.amber;
      el("line", { x1: pl, x2: W - pr, y1: Y(l.p), y2: Y(l.p), stroke: c, "stroke-width": 1.5, "stroke-dasharray": "7 5" }, svg);
      var lab = (LINE[l.k] ? LINE[l.k][L()] : l.k) + " " + l.p.toFixed(2);
      var tw = lab.length * 6.6 + 10;
      // tag on the left: the newest candles (on the right) are usually the ones the question is about
      el("rect", { x: pl + 2, y: Y(l.p) - 19, width: tw, height: 16, rx: 4, fill: "#0b1220", "fill-opacity": .92, stroke: c, "stroke-opacity": .5 }, svg);
      txt(svg, pl + 7, Y(l.p) - 7, lab, 11, c, "start", 700);
    });
    (r.marks || []).forEach(function (m) {
      var y = Y(m.p) + (m.up ? -9 : 9);
      el("circle", { cx: X(m.i), cy: y, r: m.txt ? 9 : 4, fill: m.txt ? COL.amber : COL.blue }, svg);
      if (m.txt) txt(svg, X(m.i), y + 4, m.txt, 12, "#0b1220", "middle", 800);
    });
    var api = { svg: svg, X: X, Y: Y, step: step, bodies: bodies, top: pt, h: H - pt - pb };
    if (onPick) {
      r.c.forEach(function (k, i) {
        var hit = el("rect", { x: X(i) - step / 2, width: step, y: pt, height: H - pt - pb, fill: "transparent", class: "drill-hit" }, svg);
        hit.addEventListener("click", function () { onPick(i); });
      });
    }
    return api;
  }

  function mini(o, lo, hi) {  // all options share one price scale so their shapes compare fairly
    var svg = el("svg", { viewBox: "0 0 120 150", class: "drill-mini" });
    var Y = function (p) { return 12 + 96 * (hi - p) / (hi - lo || 1); };
    var col = o[3] >= o[0] ? COL.bull : COL.bear;
    el("line", { x1: 60, x2: 60, y1: Y(o[1]), y2: Y(o[2]), stroke: col, "stroke-width": 2 }, svg);
    el("rect", { x: 44, width: 32, y: Y(Math.max(o[0], o[3])), height: Math.max(Math.abs(Y(o[0]) - Y(o[3])), 2), fill: col, rx: 2 }, svg);
    txt(svg, 60, 126, "O " + o[0].toFixed(2) + "  H " + o[1].toFixed(2), 9.5, COL.text, "middle");
    txt(svg, 60, 140, "L " + o[2].toFixed(2) + "  C " + o[3].toFixed(2), 9.5, COL.text, "middle");
    return svg;
  }

  function Drill(box, d) {
    var stage = box.querySelector(".drill-stage"), set = [], pos = 0, right = 0, done = false, answered = null;
    var bestKey = "tp-drill-" + d.key;
    function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
    function start() {
      set = shuffle(d.rounds.map(function (_, i) { return i; })).slice(0, 5); pos = 0; right = 0; answered = null; render();
    }
    function bestLine() { var b = store(bestKey); return b ? " · " + T.best[L()] + " " + b + " / 5" : ""; }
    function render() {
      stage.innerHTML = "";
      var l = L();
      if (!set.length) {
        var b = document.createElement("button"); b.className = "btn primary drill-start"; b.textContent = T.start[l];
        b.addEventListener("click", start); stage.appendChild(b);
        var s = document.createElement("span"); s.className = "drill-best"; s.textContent = bestLine().replace(/^ · /, ""); stage.appendChild(s);
        return;
      }
      if (pos >= set.length) {
        var best = Math.max(+(store(bestKey) || 0), right); store(bestKey, String(best));
        stage.innerHTML = '<p class="drill-score">' + T.score[l] + ": " + right + " / " + set.length + " · " + T.best[l] + " " + best + " / 5</p>";
        var again = document.createElement("button"); again.className = "btn primary"; again.textContent = T.again[l];
        again.addEventListener("click", start); stage.appendChild(again);
        return;
      }
      var r = d.rounds[set[pos]];
      var head = document.createElement("p"); head.className = "drill-head";
      head.textContent = T.round[l] + " " + (pos + 1) + " / " + set.length + " · " + T.score[l] + " " + right;
      stage.appendChild(head);
      var c = chart(r, r.ask === "click" && answered === null ? function (i) { answer(i); } : null);
      if (answered !== null && r.ask === "click") {
        var ok = answered === r.a;
        c.bodies[answered].setAttribute("stroke", ok ? COL.bull : COL.bear); c.bodies[answered].setAttribute("stroke-width", 3);
        el("rect", { x: c.X(r.a) - c.step / 2, width: c.step, y: c.top, height: c.h, fill: "none", stroke: COL.bull, "stroke-width": 2, rx: 4 }, c.svg);
        if (r.zone_fvg) el("rect", { x: c.X(r.zone_fvg.i - 1) - c.step / 2, width: c.step * 4, y: c.Y(r.zone_fvg.hi), height: c.Y(r.zone_fvg.lo) - c.Y(r.zone_fvg.hi), fill: COL.amber, "fill-opacity": .25 }, c.svg);
      }
      stage.appendChild(c.svg);
      var ctl = document.createElement("div"); ctl.className = "drill-ctl"; stage.appendChild(ctl);
      if (r.ask === "click") {
        if (answered === null) { var hint = document.createElement("p"); hint.className = "drill-hint"; hint.textContent = T.click[l]; ctl.appendChild(hint); }
      } else if (r.ask === "candle") {
        var mlo = Math.min.apply(null, r.cand.map(function (o) { return o[2]; })), mhi = Math.max.apply(null, r.cand.map(function (o) { return o[1]; }));
        r.cand.forEach(function (o, i) {
          var b = document.createElement("button"); b.className = "drill-opt drill-cand"; b.appendChild(mini(o, mlo, mhi));
          if (answered !== null) { b.disabled = true; if (i === r.a) b.classList.add("right"); else if (i === answered) b.classList.add("wrong"); }
          else b.addEventListener("click", function () { answer(i); });
          ctl.appendChild(b);
        });
      } else {
        r.opts.forEach(function (o) {
          var b = document.createElement("button"); b.className = "drill-opt"; b.textContent = OPT[o] ? OPT[o][l] : o;
          if (answered !== null) { b.disabled = true; if (o === r.a) b.classList.add("right"); else if (o === answered) b.classList.add("wrong"); }
          else b.addEventListener("click", function () { answer(o); });
          ctl.appendChild(b);
        });
      }
      if (answered !== null) {
        var ex = document.createElement("div"); ex.className = "drill-exp " + (answered === r.a ? "ok" : "no");
        ex.innerHTML = "<b>" + (answered === r.a ? T.right[l] : T.wrong[l]) + "</b> ";
        ex.appendChild(document.createTextNode(r.e[l])); stage.appendChild(ex);
        var nx = document.createElement("button"); nx.className = "btn primary drill-next"; nx.textContent = T.next[l];
        nx.addEventListener("click", function () { pos++; answered = null; render(); }); stage.appendChild(nx);
      }
    }
    function answer(a) {
      if (answered !== null) return;
      answered = a; if (a === d.rounds[set[pos]].a) right++; render();
    }
    render();
    document.querySelectorAll("[data-set-lang]").forEach(function (b) { b.addEventListener("click", function () { setTimeout(render, 0); }); });
  }

  document.querySelectorAll(".drill[data-phase]").forEach(function (box) {
    var list = window.DRILLS[box.getAttribute("data-phase")] || [];
    var d = list.filter(function (x) { return x.key === box.getAttribute("data-key"); })[0];
    if (d) Drill(box, d);
  });
})();
