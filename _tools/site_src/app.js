(function () {
  var root = document.documentElement;
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function doneSet() { try { return new Set(JSON.parse(store("tp-done") || "[]")); } catch (e) { return new Set(); } }
  function saveDone(s) { store("tp-done", JSON.stringify(Array.from(s))); }

  // language
  function setLang(l) { root.setAttribute("data-lang", l); root.setAttribute("lang", l); store("tp-lang", l); buildToc(); }
  document.querySelectorAll("[data-set-lang]").forEach(function (b) {
    b.addEventListener("click", function () { setLang(b.getAttribute("data-set-lang")); });
  });
  // theme
  var tb = document.querySelector(".theme-btn");
  if (tb) tb.addEventListener("click", function () {
    var t = root.getAttribute("data-theme") === "light" ? "dark" : "light";
    root.setAttribute("data-theme", t); store("tp-theme", t);
  });
  // mobile nav
  var mb = document.querySelector(".menu-btn");
  if (mb) mb.addEventListener("click", function () { document.body.classList.toggle("nav-open"); });

  // progress
  function paint() {
    var d = doneSet();
    document.querySelectorAll("[data-id]").forEach(function (el) { el.classList.toggle("done", d.has(el.getAttribute("data-id"))); });
    var btn = document.querySelector(".done-btn");
    if (btn) btn.classList.toggle("is-done", d.has(btn.getAttribute("data-id")));
    if (window.PHASE_MAP) {
      document.querySelectorAll(".ice-card[data-phase]").forEach(function (c) {
        var ids = window.PHASE_MAP[c.getAttribute("data-phase")] || [];
        var n = ids.filter(function (i) { return d.has(i); }).length;
        var bar = c.querySelector(".bar i"); if (bar) bar.style.width = (ids.length ? 100 * n / ids.length : 0) + "%";
      });
    }
  }
  var db = document.querySelector(".done-btn");
  if (db) db.addEventListener("click", function () {
    var d = doneSet(), id = db.getAttribute("data-id");
    d.has(id) ? d.delete(id) : d.add(id); saveDone(d); paint();
  });
  var doc = document.querySelector("[data-lesson]");
  if (doc) store("tp-last", location.pathname.split("/").pop());
  var cont = document.querySelector(".continue-btn"), last = store("tp-last");
  if (cont && last) { cont.href = last; cont.hidden = false; }
  paint();

  // table of contents for the visible language
  function buildToc() {
    var toc = document.querySelector(".toc"); if (!toc) return;
    var art = document.querySelector("article.l-" + root.getAttribute("data-lang")); if (!art) return;
    var hs = art.querySelectorAll("h2");
    toc.innerHTML = hs.length ? "<b>" + (root.getAttribute("data-lang") === "th" ? "ในหน้านี้" : "On this page") + "</b>" : "";
    hs.forEach(function (h, i) {
      if (!h.id) h.id = art.getAttribute("lang") + "-s" + i;
      var a = document.createElement("a"); a.href = "#" + h.id; a.textContent = h.textContent; toc.appendChild(a);
    });
  }
  buildToc();
  window.addEventListener("scroll", function () {
    var links = document.querySelectorAll(".toc a"), cur = null;
    links.forEach(function (a) { var h = document.getElementById(a.getAttribute("href").slice(1)); if (h && h.getBoundingClientRect().top < 120) cur = a; });
    links.forEach(function (a) { a.classList.toggle("on", a === cur); });
  }, { passive: true });

  // quizzes
  document.querySelectorAll(".quiz").forEach(function (qz) {
    var qs = qz.querySelectorAll(".q"), score = qz.querySelector(".quiz-score"), right = 0, answered = 0;
    qs.forEach(function (q) {
      q.querySelectorAll(".opt").forEach(function (o) {
        o.addEventListener("click", function () {
          if (q.classList.contains("answered")) return;
          q.classList.add("answered"); answered++;
          var ok = o.getAttribute("data-ok") === "1"; if (ok) right++;
          o.classList.add(ok ? "right" : "wrong");
          q.querySelectorAll(".opt").forEach(function (x) { x.disabled = true; if (x.getAttribute("data-ok") === "1") x.classList.add("right"); });
          if (answered === qs.length && score) {
            var th = root.getAttribute("data-lang") === "th";
            score.textContent = (th ? "คะแนน: " : "Score: ") + right + " / " + qs.length +
              (right === qs.length ? (th ? " — ยอดเยี่ยม! พร้อมไปเฟสถัดไป" : " — excellent, ready for the next phase!") : (th ? " — ทบทวนข้อที่ผิดอีกครั้ง" : " — review the ones you missed."));
          }
        });
      });
    });
  });
})();

/* ---------------------------------------------------------------- C6: search, glossary tooltips, glossary filter */
(function () {
  var root = document.documentElement;
  function th() { return root.getAttribute("data-lang") === "th"; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function load(src, cb) {
    var s = document.createElement("script"); s.src = src; s.onload = cb; document.head.appendChild(s);
  }

  // ---------- search
  var ov = null, input, list, sel = 0, hits = [];
  function openSearch() {
    if (!ov) {
      ov = document.createElement("div"); ov.className = "search-ov";
      ov.innerHTML = '<div class="search-box" role="dialog" aria-label="Search"><input type="search" autocomplete="off">' +
        '<div class="search-res"></div><div class="search-hint"></div></div>';
      document.body.appendChild(ov);
      input = ov.querySelector("input"); list = ov.querySelector(".search-res");
      ov.addEventListener("click", function (e) { if (e.target === ov) closeSearch(); });
      input.addEventListener("input", run);
      input.addEventListener("keydown", function (e) {
        if (e.key === "ArrowDown") { sel = Math.min(sel + 1, hits.length - 1); paintSel(); e.preventDefault(); }
        else if (e.key === "ArrowUp") { sel = Math.max(sel - 1, 0); paintSel(); e.preventDefault(); }
        else if (e.key === "Enter" && hits[sel]) { location.href = hits[sel].u; }
        else if (e.key === "Escape") closeSearch();
      });
    }
    input.placeholder = th() ? "ค้นหาบทเรียนและคำศัพท์…" : "Search lessons and terms…";
    ov.querySelector(".search-hint").textContent = th() ? "↑↓ เลือก · Enter เปิด · Esc ปิด" : "↑↓ to move · Enter to open · Esc to close";
    ov.classList.add("open"); input.focus(); input.select();
    if (!window.SEARCH_INDEX) load("assets/search-index.js", run);
    if (!window.GLOSSARY) load("assets/glossary.js", run);
  }
  function closeSearch() { if (ov) ov.classList.remove("open"); }
  function snippet(text, terms) {
    var low = text.toLowerCase(), i = -1;
    for (var k = 0; k < terms.length && i < 0; k++) i = low.indexOf(terms[k]);
    var a = Math.max(0, i - 60);
    while (a > 0 && /[\u0E31\u0E34-\u0E3A\u0E47-\u0E4E]/.test(text.charAt(a))) a--;  // don't start on a Thai vowel/tone mark
    var s = (a ? "…" : "") + text.slice(a, a + 170) + (a + 170 < text.length ? "…" : "");
    var h = esc(s);
    terms.forEach(function (t) {
      if (!t) return;
      h = h.replace(new RegExp(t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "gi"), function (m) { return "<mark>" + m + "</mark>"; });
    });
    return h;
  }
  function run() {
    if (!ov) return;
    var q = input.value.trim().toLowerCase(), L = th() ? 1 : 0;
    hits = []; sel = 0;
    if (q.length < 2) { list.innerHTML = ""; return; }
    var terms = q.split(/\s+/).filter(Boolean);
    (window.GLOSSARY || []).forEach(function (g) {
      var hay = (g[0] + " " + g[1]).toLowerCase();
      if (terms.every(function (t) { return hay.indexOf(t) >= 0; }))
        hits.push({ u: "glossary.html#" + g[4], score: 100, g: true, t: g[0] === g[1] ? g[0] : (L ? g[1] + " (" + g[0] + ")" : g[0] + " · " + g[1]), s: esc(g[2]) });
    });
    hits = hits.slice(0, 5);
    var docs = [];
    (window.SEARCH_INDEX || []).forEach(function (d) {
      var t = d.t[L].toLowerCase(), h = d.h[L].join(" | ").toLowerCase(), x = d.x[L].toLowerCase(), score = 0, ok = true;
      terms.forEach(function (w) {
        var inT = (d.i + " " + t).indexOf(w) >= 0, inH = h.indexOf(w) >= 0, n = 0, p = x.indexOf(w);
        while (p >= 0 && n < 6) { n++; p = x.indexOf(w, p + w.length); }
        if (!inT && !inH && !n) ok = false;
        score += (inT ? 30 : 0) + (inH ? 10 : 0) + n;
      });
      if (ok) docs.push({ u: d.u, score: score, t: d.i + " " + d.t[L], s: snippet(d.x[L], terms) });
    });
    docs.sort(function (a, b) { return b.score - a.score; });
    hits = hits.concat(docs.slice(0, 25));
    if (!hits.length) {
      list.innerHTML = '<p class="search-none">' + (window.SEARCH_INDEX ? (th() ? "ไม่พบผลลัพธ์" : "No results") : (th() ? "กำลังโหลด…" : "Loading…")) + "</p>";
      return;
    }
    list.innerHTML = hits.map(function (r, i) {
      return '<a class="search-hit' + (r.g ? " is-gloss" : "") + '" href="' + r.u + '" data-i="' + i + '"><b>' +
        (r.g ? (th() ? "คำศัพท์ · " : "Term · ") : "") + esc(r.t) + "</b><small>" + r.s + "</small></a>";
    }).join("");
    paintSel();
  }
  function paintSel() {
    list.querySelectorAll(".search-hit").forEach(function (a, i) { a.classList.toggle("sel", i === sel); if (i === sel) a.scrollIntoView({ block: "nearest" }); });
  }
  var sb = document.querySelector(".search-btn");
  if (sb) sb.addEventListener("click", openSearch);
  document.addEventListener("keydown", function (e) {
    var tag = (e.target.tagName || "").toLowerCase(), typing = tag === "input" || tag === "textarea" || tag === "select";
    if ((e.key === "/" && !typing) || ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k")) { e.preventDefault(); openSearch(); }
  });

  // ---------- glossary tooltips on bold terms in lessons
  var arts = document.querySelectorAll("article.lesson");
  if (arts.length && !document.body.classList.contains("gloss")) {
    load("assets/glossary.js", function () {
      var map = {};
      function keys(s) {
        var out = [], parts = s.split(/\s+\/\s+/);
        parts.concat([s]).forEach(function (p) {
          var base = p.replace(/\s*\([^)]*\)\s*/g, " ").trim(), inner = (p.match(/\(([^)]*)\)/) || [])[1];
          [p, base, inner].forEach(function (k) { if (k && k.trim().length > 1) out.push(k.trim().toLowerCase()); });
        });
        return out;
      }
      window.GLOSSARY.forEach(function (g, i) {
        keys(g[0]).concat(keys(g[1])).forEach(function (k) { if (!(k in map)) map[k] = i; });
      });
      function find(txt) {
        var t = txt.trim().replace(/[:.,;]+$/, "").toLowerCase();
        var cands = [t, t.replace(/\s*\([^)]*\)\s*/g, " ").trim(), ((t.match(/\(([^)]*)\)/) || [])[1] || "").trim()];
        if (/s$/.test(t)) cands.push(t.slice(0, -1));
        for (var k = 0; k < cands.length; k++) if (cands[k] && cands[k].length > 1 && cands[k] in map && !/^[\d\s.,%:+−-]+$/.test(cands[k])) return map[cands[k]];
        return -1;
      }
      arts.forEach(function (art) {
        var used = {};
        art.querySelectorAll("strong").forEach(function (el) {
          if (el.closest(".c-terms, .quiz, h1, h2, h3, .takeaway, a")) return;
          if (/:\s*$/.test(el.textContent)) return;  // "**Forex:**"-style labels, not terms
          var i = find(el.textContent);
          if (i < 0 || used[i]) return;
          used[i] = 1; el.classList.add("gl"); el.setAttribute("data-gi", i); el.setAttribute("tabindex", "0");
        });
      });
      var tip = document.createElement("div"); tip.className = "gl-tip"; tip.setAttribute("role", "tooltip"); document.body.appendChild(tip);
      var pinned = null;
      function showTip(el) {
        var g = window.GLOSSARY[+el.getAttribute("data-gi")];
        tip.innerHTML = (g[0] === g[1] ? "<b>" + esc(g[0]) + "</b>" : th() ? "<b>" + esc(g[1]) + "</b> (" + esc(g[0]) + ")" : "<b>" + esc(g[0]) + "</b> · " + esc(g[1])) +
          "<p>" + esc(g[2]) + "</p><a href=\"glossary.html#" + g[4] + "\">" + (th() ? "อภิธานศัพท์ →" : "Glossary →") + "</a>" +
          (th() ? '<small>คำอธิบายเป็นภาษาอังกฤษ</small>' : "");
        var r = el.getBoundingClientRect();
        tip.classList.add("open");
        var w = tip.offsetWidth, x = Math.min(Math.max(8, r.left + r.width / 2 - w / 2), window.innerWidth - w - 8);
        var y = r.bottom + 8 + tip.offsetHeight > window.innerHeight ? r.top - tip.offsetHeight - 8 : r.bottom + 8;
        tip.style.left = x + "px"; tip.style.top = (y + window.scrollY) + "px";
      }
      function hide() { if (!pinned) tip.classList.remove("open"); }
      document.querySelectorAll(".gl").forEach(function (el) {
        el.addEventListener("mouseenter", function () { showTip(el); });
        el.addEventListener("mouseleave", function () { setTimeout(function () { if (!tip.matches(":hover")) hide(); }, 120); });
        el.addEventListener("focus", function () { showTip(el); });
        el.addEventListener("blur", hide);
        el.addEventListener("click", function (e) { e.stopPropagation(); pinned = pinned === el ? null : el; pinned ? showTip(el) : tip.classList.remove("open"); });
      });
      tip.addEventListener("mouseleave", hide);
      document.addEventListener("click", function (e) { if (!tip.contains(e.target)) { pinned = null; tip.classList.remove("open"); } });
    });
  }

  // ---------- glossary page filter
  var gf = document.querySelector(".gloss-filter");
  if (gf) {
    gf.addEventListener("input", function () {
      var q = gf.value.trim().toLowerCase();
      document.querySelectorAll("table.gloss").forEach(function (tb) {
        var any = false;
        tb.querySelectorAll("tr").forEach(function (tr) { var ok = !q || tr.textContent.toLowerCase().indexOf(q) >= 0; tr.hidden = !ok; any = any || ok; });
        tb.hidden = !any; tb.previousElementSibling.hidden = !any;
      });
    });
    if (location.hash) { var t = document.getElementById(location.hash.slice(1)); if (t) t.classList.add("hl"); }
  }
})();
