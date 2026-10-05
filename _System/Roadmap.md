---
tags: [system, roadmap]
---
# Roadmap · แผนที่การเรียนรู้

## The idea
The iceberg image ranks trading topics from "what everyone sees" (top) to "what professionals use" (bottom). A learner who jumps straight to ICT or GEX without the base layers usually fails, because **concepts sit on top of structure, and structure only pays if risk and psychology are handled**.

So the path goes **base → surface → deep**, and every phase reuses what came before.

## Phases mapped to the iceberg

| Iceberg layer | Phase | Topics from the image | Extra (not in image) |
|---|---|---|---|
| Before the iceberg — the playing field | 0 Markets, Brokers & News | — | Exchanges vs brokers, Forex, Gold, Stocks, Nvidia, Crypto, economic calendar, scams |
| Foundation (below the whole iceberg, but first to learn) | 1 Foundations | — | Mindset, auction basics, candlesticks, timeframes |
| | 2 Market Structure | — | HH/HL, BOS/CHoCH, S/R, supply & demand |
| | 3 Risk & Money Mgmt | — | Sizing, R, expectancy, drawdown |
| | 4 Psychology & Execution | — | Biases, plan, routine, journal, tilt |
| Tip (above water) | 5 Liquidity & ICT | Liquidity, ICT, FVGs, QT | Order blocks, killzones |
| Just under water | 6 Measuring tools | Fibonacci, Stdv | **Elliott Wave** (your addition) |
| Layer 3 | 7 Orderflow & AMT | Lv2 data, Footprints, Heat maps, AMT, Orderflow | Volume profile |
| Layer 4 | 8 Options & Gamma | Put walls, Call walls, Flips, Vex, Gex, Gamma exposure, Options flow | Greeks, dealer hedging |
| Layer 5 | 9 Quant | Quant, top ticks, "mathematically proven" | Stats, backtesting, Python |
| Floor | 10 Macro & Investing | Macro economics, Wall Street | Valuation, portfolio |
| — | 11 Capstone | — | Your written plan |

> [!note] Term notes
> - "Cell walls" in the image = **Call walls**.
> - "QT" next to Fibonacci/Stdv = ICT **Quarterly Theory** (time-based cycles). QT as *Quantitative Tightening* is covered in Phase 10.
> - "Vex" = **Vanna exposure**. "Flips" = the **gamma flip** level.

## How each phase is built (small tasks, one at a time)
1. Write lesson notes (EN master, then TH) following [[Style Guide]].
2. Add figures to `_tools/figures/pN.py`, run `make_figures.py`.
3. Run `build.py`, check the pages in both languages.
4. Tick the phase on [[Task Board]].

## Order of study
`0 → 1 → 2 → 3 → 4` is mandatory (skip 0 only if you already trade with a regulated broker and size positions correctly) and in order. After that `5 → 6 → 7 → 8 → 9 → 10` goes from simple chart concepts to professional data. Revisit Phase 3 and 4 after every new phase: every new tool is only as good as the risk and discipline around it.
