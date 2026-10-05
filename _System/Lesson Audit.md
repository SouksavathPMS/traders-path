---
tags: [system, audit]
---
# Lesson Audit · beginner-readiness (Oct 2026)

**What was scanned:** all 75 lessons, by script (acronyms used before they are explained, word count, figures, worked examples) and by reading lessons 7.4, 8.2, 8.3, 8.4 and 8.5 in full.

## Findings

1. **Written for intermediate traders.** The content is correct, but it assumes words a beginner has never met. Example from 8.4: *"gamma × open interest × contract multiplier × spot²"* appears before *open interest*, *contract multiplier* or *spot* are explained anywhere.
2. **One worked example per lesson.** Hard mechanisms (dealer hedging, delta, footprint imbalances, Elliott counts) need 2–3 small numeric walkthroughs. One realistic example is not enough.
3. **No analogies.** Deep concepts are only explained formally.
4. **Undefined acronyms by lesson** (script output): 5.1 PDH/PDL/PWH/PWL · 5.4 BISI/SIBI · 5.6 KZ, Q1–Q4 · 6.6 SD, VIX · 7.2 POC/VAH/VAL/HVN/LVN · 7.3 ES/NQ/CL · 8.1 ATM/ITM/OTM/ETF · 8.5 OI/OPEX · 8.7 OI/OTM · 9.4 TICK/TRIN/ADD/VOLD/SPY · 9.5–9.6 CAGR · 10.1 ISM/PMI/QE · 10.3 CPI/FOMC/GDP/PCE · 10.4 EM/SET/SET50/THB · 10.5 CTA/IPO · 10.6 EBITDA/EV/FCF/PV.
5. **Missing jargon the script can't catch** (plain words used as technical terms): spot, underlying, strike, premium, expiry, open interest, implied volatility, notional, contract multiplier, dealer/market maker, delta-neutral, mean reversion, regime, initiative vs responsive, absorption, liquidity pool, displacement, dealing range, equilibrium, impulse, correction, z-score, sample size, overfitting, yield, real yield, basis points.
6. **No asset-class context.** The lessons rarely say how a concept behaves in Forex vs Gold vs Stocks vs Crypto (sessions, leverage, volume data, 24/7). → solved by the new **Phase 0** plus `[!market]` blocks.
7. **Doesn't explain why exchanges and brokers exist, what news to watch, or what moves markets** — added in Phase 0.

## Upgrade status

| Status | Lessons |
|---|---|
| ✅ Upgraded to v2 (gold standard; copy this pattern) | 8.1, 8.2, 8.3, 8.4, 8.5 · new Phase 0 lessons 0.1, 0.3, 0.8 |
| ✅ New, written to v2 (B1–B3, Oct 2026) — Phase 0 complete | 0.2, 0.4, 0.5, 0.6, 0.7, 0.9, 0.10 |
| ✅ Upgraded to v2 (B4, Oct 2026; scripts in `_tools/upgrades/b4/`) | 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7 |
| ✅ Upgraded to v2 (B5, Oct 2026; scripts in `_tools/upgrades/b5/`) | 6.1, 6.2, 6.3, 6.4, 6.5, 6.6 |
| ✅ Upgraded to v2 (B6, Oct 2026; scripts in `_tools/upgrades/b6/`) | 7.1, 7.2, 7.3, 7.4, 7.5, 7.6 |
| ✅ Upgraded to v2 (B7, Oct 2026; scripts in `_tools/upgrades/b7/`, runnable code in `_tools/quant/`) | 8.6, 8.7, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6 |
| ✅ Upgraded to v2 (B8, Oct 2026; scripts in `_tools/upgrades/b8/`) | 2.3, 2.5, 3.2, 3.4, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7 |
| ✅ Upgraded to v2 (B9a, Oct 2026; scripts in `_tools/upgrades/b9/`) | 1.1, 1.2, 1.3, 1.4, 1.5, checkpoint 1.6 |
| ✅ Upgraded to v2 (B9b, Oct 2026; scripts in `_tools/upgrades/b9/`) | 2.1, 2.2, 2.4, 2.6, checkpoint 2.7 |
| ✅ Upgraded to v2 (B9c, Oct 2026; scripts in `_tools/upgrades/b9/`) | 3.1, 3.3, 3.5, 3.6, checkpoint 3.7 |
| ✅ Upgraded to v2 (B9d, Oct 2026; scripts in `_tools/upgrades/b9/`) | 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, checkpoint 4.7 |
| ✅ Upgraded to v2 (B9e, Oct 2026; scripts in `_tools/upgrades/b9/`) | 11.1, 11.2, 11.3 |
| ✅ Upgraded to v2 (B9f, Oct 2026; scripts in `_tools/upgrades/b9/`) | checkpoints 5.8, 6.7, 7.7, 8.8, 9.7, 10.8 (worked problems + final check) |
| ✅ Glossary (B10, Oct 2026) | `_System/Glossary.md`: +382 rows from every `[!terms]` block (575 rows total); duplicates merged, phase column lists every phase that uses the term |
| ✅ New, written to v2 (C1, Oct 2026) | 0.11 Personal Finance First · 2.8 Indicators · 2.9 Classic Chart Patterns (placed before checkpoints 0.10 / 2.7; quiz + takeaways added there via `_tools/upgrades/c1/checkpoints.py`) |
| ✅ New, written to v2 (C2, Oct 2026) | 0.12 Short Selling · 3.8 Trade Management · 3.9 Portfolio Risk (runnable `_tools/quant/monte_carlo.py` and `_tools/quant/exit_methods.py`; checkpoints 0.10 / 3.7 updated via `_tools/upgrades/c2/checkpoints.py`) |
| ✅ New phase, written to v2 (C3, Oct 2026) | Phase 12 History Lessons: 12.1 Black Monday 1987 · 12.2 2008 Crisis · 12.3 Swiss Franc 2015 · 12.4 COVID 2020 · 12.5 2022 Rate Shock · 12.6 FTX 2022 · 12.7 SVB 2023 · 12.8 Checkpoint (market data via `_tools/history/fetch_history.py` → `_tools/history/data/`; figures in `_tools/figures/p12.py`) |
| ✅ New, written to v2 (C4, Oct 2026) | 10.9 Index Funds & ETFs · 10.10 DCA vs Lump Sum · 10.11 Bonds · 10.12 Dividends · 10.13 REITs · 10.14 Investing from Thailand & Laos (data: `_tools/investing/fetch_investing.py`; every number from `_tools/investing/analysis.py`; figures `_tools/figures/p10inv.py`; checkpoint 10.8 via `_tools/upgrades/c4/checkpoints.py`; dated facts as of Oct 2026, re-check yearly) |
| ✅ New, written to v2 (C5, Oct 2026) | 0.13 TradingView Basics · 0.14 Economic Calendars & Stock Screeners · 0.15 Prop Firms & Funded Challenges (every number from `_tools/toolkit/analysis.py`, incl. time-zone conversions and a 20,000-run challenge simulation; figures `_tools/figures/p0tools.py`; checkpoint 0.10 via `_tools/upgrades/c5/checkpoints.py`; plan limits, release dates and prop-firm rules/statistics dated Oct 2026, re-check before each review) |
| ✅ Website features (C6, Oct 2026) | Takeaway box on 93 lessons (the lesson's own row from its phase checkpoint, both languages; Phase 11 has no checkpoint, so no box) · offline search (`/` or Ctrl/⌘+K; lessons + glossary, EN/TH) · glossary page + tooltips on bold terms (meanings in English only so far) · position-size calculator (`_tools/site_src/calc.js`, maths unit-tested in Node against 0.12/0.13 examples) · disclaimer page from `_System/Disclaimer.md` (draft for owner review) · footer + sidebar tool links. All generated by `_tools/build.py`. |
| ✅ Chart drills (C7, Oct 2026) | 11 interactive drills on the website, 10 rounds each: Phase 1 (who won, pin bar, bullish engulfing, build the 4H candle), Phase 2 (label the swing, trend or range, BOS/CHoCH/no break), Phase 5 (equal highs/lows, sweep or run, premium/discount, click the FVG). Generated by `_tools/drills/make_drills.py`: each round's answer is re-derived from the candles with the lesson's rule (1.3–1.5, 2.1–2.3, 5.1–5.4), answers balanced so no button always wins. Pages `drills*.html`; linked from phases 1/2/5, 10 lessons and the sidebar. Charts are generated examples, labelled as such. |
| ✅ Obsidian toolkit (C8, Oct 2026) | 7 learner templates × EN/TH in `_System/Templates` (trade journal, daily routine, weekly & monthly review, trading plan, investment policy, lesson notes; fields taken from 4.4, 4.5, 11.1, 11.2; Templates plugin folder set) · 3 Bases dashboards in `_System/Dashboards` (Course Progress, Trade Journal with expectancy/win-rate summaries, Reviews & Plans) · 1,084 EN + 1,084 TH flashcards in `_System/Flashcards`, generated from each lesson's [!terms] box by `_tools/flashcards.py` (Spaced Repetition plugin format) · guide note [[Learning Toolkit]] linked from Home. |
| ✅ Quality pass (C9, Oct 2026) | `last_reviewed` added to all 108 lessons (file's last-edit date; shown on the site) · all 570 figures re-rendered and checked by `_tools/qa/figure_check.py` (text overflow/overlap measured in Chrome): 5 figures fixed (p0-fx-quote, p0-money-ladder, p8-delta-curve, p9-ten-equity, p9-walk-forward), now 0 issues · [[Fact Register]] (260 time-sensitive facts in 52 lessons, 7 overdue ⚠) by `_tools/qa/fact_register.py` · [[Thai Review List]] by `_tools/qa/thai_check.py`: EN↔TH mirror check finds 0 differences (callouts, sections, figures, questions, numbers); 45 Thai lines in 38 lessons flagged for a native read · handoff gaps closed: calculator linked from 0.3/0.4/3.2, Backtest Log template + dashboard, 626 EN + 626 TH self-check question flashcards. |
| ✅ Publishing (C10, Oct 2026) | [[Publishing Guide]] (EN/TH: public-repo caution, one-time setup, daily use, QA checklist, troubleshooting) · `.github/workflows/publish-site.yml` (PDFs → build.py → check for raw `![[`/BLOCKTOKEN → GitHub Pages; action versions configure-pages@v5, upload-pages-artifact@v4, deploy-pages@v4) · `requirements.txt` (markdown 3.11) · `.gitignore` (site/ is built in CI) · `_tools/make_pdfs.py`: 26 A4 PDFs (13 phases × EN/TH, 1,465 pages, 55 MB) with cover, takeaways, opened self-checks and quiz answer keys, linked from each phase page · CI steps verified on a clean copy with only requirements.txt installed. |

## Upgrade briefs for the deep part
What each lesson needs on top of the standard v2 blocks in [[Style Guide]].

### Phase 5 — Liquidity & ICT
- **5.1 Liquidity** — analogy: *stops are like a crowd's exit doors; big players need crowds to trade with.* Walkthrough: 300 traders each with a stop 10 pips under an obvious low = how many lots of sell orders waiting there. Terms: PDH/PDL/PWH/PWL, buy-side and sell-side liquidity, liquidity pool, resting order.
- **5.2 Sweeps** — candle-by-candle story of a sweep (5 numbered candles). A figure showing "sweep + close back inside" vs "real breakout + acceptance". Check: how do you tell them apart **after** the candle closes?
- **5.3 Dealing range** — analogy: *a shop's price list — buy in the sale section (discount), sell in the premium aisle.* Walkthrough: range 1.0800–1.0900 → equilibrium 1.0850 → premium/discount zones in pips.
- **5.4 FVG** — 3-candle walkthrough with real numbers (candle 1 high 100.20, candle 3 low 100.60 → gap 0.40); define BISI/SIBI in plain words; when an FVG is **invalid**; a `[!market]` block (FVGs in 24/7 crypto vs gapping stocks).
- **5.5 Order blocks** — why the *last opposite candle* matters, as a story of unfilled orders; a breaker as an "order block that failed"; mitigation explained with numbers.
- **5.6 Time / QT** — convert every session and killzone to **Thailand/Laos time (UTC+7)** with a table that includes DST changes; define Q1–Q4 of a day/week; analogy: *market's daily shift schedule.*
- **5.7 Model setup** — a checklist walkthrough where every step references its lesson, with a "what if it fails" branch.

### Phase 6 — Fibonacci, Elliott Wave, Std Dev
- **6.1 Fibonacci** — where 0.618 comes from (in 2 lines, no mysticism); walkthrough of a retracement (swing 100→150: 38.2% = 130.9 …) and an extension. Explain honestly that levels work partly because many traders watch them.
- **6.2 Elliott 5-3** — crowd-psychology story for each wave (W1 smart money, W2 doubt, W3 recognition, W4 profit-taking, W5 euphoria/FOMO); define FOMO; one fully labelled candlestick chart **plus** the same chart with the wrong count.
- **6.3 Rules** — the 3 hard rules as a "count validator" flow; walkthrough that breaks one rule and shows how the count must change.
- **6.4 Corrections** — side-by-side figure of zigzag/flat/triangle with A-B-C sub-waves; analogy for a flat ("market catches its breath").
- **6.5 Confluence** — numeric worked case: W1 = 100→120 → W2 at 61.8% = 107.6 → W3 target 1.618 × 20 + 107.6 = 140.0.
- **6.6 Std dev** — explain standard deviation with a non-market example first (heights of students); 68-95-99.7 figure; walkthrough of daily expected move from VIX (VIX 16 → 16/√252 ≈ 1.0% per day). Define SD, VIX.

### Phase 7 — Orderflow & AMT
- **7.1 AMT** — analogy: *a night market — the seller drops prices until people buy, raises them when there's a queue.* Initiative vs responsive in plain words.
- **7.2 Volume profile** — build a profile **by hand** from 10 candles (table → histogram figure); define POC/VAH/VAL/HVN/LVN; walkthrough of the 70% value-area calculation.
- **7.3 DOM** — define ES/NQ/CL; a "watch 5 seconds of the DOM" animation-style sequence (3 frames); spoofing explained simply; `[!market]` no central DOM in spot Forex/Gold CFDs — use futures (6E, GC) or crypto exchange books.
- **7.4 Footprint** — explain "bid × ask" with one single trade first; walkthrough computing a diagonal imbalance with 2 numbers; a CVD figure with divergence labelled.
- **7.5 Heatmaps** — what colours mean; pulling vs absorbing liquidity, as frames.
- **7.6 Absorption/exhaustion** — two short numeric tapes (prints) the reader must classify; self-check.

### Phase 8 — Options (remaining)
- **8.6 Vanna/Charm** — analogy: *the hedge "melts" as time passes (charm) or as fear fades (vanna)*; walkthrough of a put delta shrinking from −0.30 to −0.20 → dealers buy back hedges → supportive flow into OPEX. Define CPI, OPEX, OTM, VIX.
- **8.7 Options flow** — define sweep, block, premium, aggressor side, OI vs volume; walkthrough "is this flow opening or closing?" using volume > OI; warning about paid "flow alert" services.

### Phase 9 — Quant
- **9.1 Statistics** — mean/median/std with 10 trade results by hand; histogram figure; fat tails shown against a normal curve.
- **9.2 Probability & EV** — coin-flip and dice before trades; EV walkthrough with costs (spread + commission).
- **9.3 Backtesting** — the five biases each with a 3-line story (look-ahead, survivorship, overfitting, data snooping, ignoring costs); in-sample vs out-of-sample figure.
- **9.4 Internals** — define TICK/TRIN/ADD/VOLD/SPY; numbered example of reading $TICK extremes (the "top ticks" from the iceberg).
- **9.5 Python** — line-by-line commented code, how to install Python on macOS, expected output printed; link to `_tools/quant/sma_crossover.py`.
- **9.6 Metrics** — compute Sharpe, Sortino, profit factor and max DD from the same 10-trade list used in 9.1; define CAGR.
