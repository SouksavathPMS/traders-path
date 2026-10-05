---
tags: [system, handoff]
---
# Claude Code Handoff

How to continue this project with Claude Code:

1. Open a terminal in this vault folder (`Investing/`) and run `claude`.
2. Claude Code reads `CLAUDE.md` automatically (project rules, commands and file layout).
3. Paste the **master prompt** below once.
4. After each batch, review the notes in Obsidian and the pages in `site/`, then type **"next batch"** (or give corrections).

---

## Master prompt (copy everything inside the box)

```text
You are continuing "Trader's Path", a bilingual (English master + Thai mirror) trading & investing course that lives in this Obsidian vault and builds into a static site with python3 _tools/build.py.

READ FIRST, in this order, before changing anything:
1. CLAUDE.md (project rules, layout, commands)
2. _System/Style Guide.md (especially "v2 · The deep-explanation layer")
3. _System/Lesson Audit.md (what is missing, upgrade briefs per lesson, status table)
4. The gold-standard lessons: "00 Markets, Brokers & News/0.1 …", "0.3 …", "0.8 …" (new lessons) and "08 Options & Dealer Positioning/8.1 … to 8.5 …" (upgraded lessons). Match their depth, tone and structure exactly.
5. _tools/upgrade_lesson.py, _tools/charts.py and _tools/figures/p0.py + p8.py (how blocks and figures are added).

GOAL: make every lesson understandable for someone who knows nothing about trading, without deleting or rewriting existing content, and finish the new Phase 0 (markets, brokers, forex, gold, stocks, Nvidia, crypto, news, scams).

WORK IN SMALL BATCHES. Do ONE batch, then stop and give me: what changed (files), new figures, anything you were unsure about, and facts you researched (with sources and dates). Wait for me to say "next batch".

BATCHES:
B1  Write Phase 0 lessons 0.2 (Instruments & Leverage) and 0.4 (Gold) from the writer briefs inside each note. New figures in _tools/figures/p0.py.
B2  Write 0.5 (Stocks & Indices) and 0.6 (Case Study: Nvidia). Use web research for current facts; every changing number gets "as of <month year>" and a source in a footnote-style line. No buy/sell advice.
B3  Write 0.7 (Crypto) and 0.9 (Staying Safe: scams), then 0.10 (Checkpoint with a 10-question quiz in EN and TH). Set status: done on each finished lesson.
B4  v2 upgrade of Phase 5 (5.1–5.7) following the briefs in Lesson Audit.
B5  v2 upgrade of Phase 6 (6.1–6.6) — Elliott Wave lessons need fully labelled candlestick charts, including one "wrong count" example.
B6  v2 upgrade of Phase 7 (7.1–7.6).
B7  v2 upgrade of 8.6, 8.7 and Phase 9 (9.1–9.6). Python code in 9.5 must run; put runnable files in _tools/quant/ and show real output.
B8  v2 upgrade of Phase 10 (10.1–10.7) plus 2.3, 2.5, 3.2, 3.4.
B9  v2 upgrade of the remaining lessons in Phases 1–4 and 11, then add [!check] blocks to every checkpoint lesson (x.7/x.8 etc.).
B10 Glossary: add every term introduced in a [!terms] block that is not yet in _System/Glossary.md (EN, TH, meaning, phase).

FOR EVERY LESSON YOU UPGRADE:
- Add, using _tools/upgrade_lesson.py (write a small script per batch, like the ones used for 8.1–8.5):
  [!eli5] + [!terms] after the mindset; at least one [!analogy]; a [!walkthrough] after every formula or mechanism (small round numbers, every step shown, ending with "So what?"); a folded [!check]- per major section with **Q1.** questions and nested [!answer]-; a [!market] block saying how the idea works in Forex / Gold / Stocks / Crypto when it differs; a [!caution] where money can be lost fast; a final [!check]-.
- Add at least one NEW figure per lesson where the audit asks for it (candlestick chart for price ideas, diagram for mechanisms), in both languages via t("en","th").
- Every acronym must be spelled out in [!terms] before use.
- Verify every number by computing it in Python before writing it.
- Thai mirrors the English completely (same blocks, same order, same figures). Natural Thai, English term in brackets on first use.
- Set level: v2 in the frontmatter (L.set_meta("level","v2")).

AFTER EACH BATCH:
1. python3 _tools/make_figures.py <phases touched>
2. python3 _tools/build.py
3. Check: grep for "BLOCKTOKEN" and "![[" in site/*.html must return nothing; every new figure file exists in both .en.svg and .th.svg.
4. If you can, render a couple of the new SVGs / pages to PNG and look at them for overlapping or overflowing text; fix any you find.
5. Update the status table in _System/Lesson Audit.md.
6. Report back and wait.

NEVER: delete existing lesson text, change lesson ids or file names, edit files in site/ by hand, give investment advice, or invent statistics.
```

---

## Short prompts for later

**Upgrade one lesson:**
```text
Read CLAUDE.md and the Style Guide v2. Upgrade lesson <id> to v2 using _tools/upgrade_lesson.py, following its brief in _System/Lesson Audit.md and the 8.1–8.5 examples. Add one new figure, verify all numbers in Python, mirror everything in Thai, rebuild, and show me the changes.
```

**Explain a lesson more simply for me:**
```text
I don't understand <topic> in lesson <id>. Read the lesson, then add one extra [!analogy] and one extra [!walkthrough] with very small numbers that targets exactly this confusion: "<what confuses you>". EN + TH. Rebuild.
```

**Add a new lesson:**
```text
Add a new lesson "<title>" to phase <N> after lesson <id>: update _tools/curriculum.json (EN + TH title), run python3 _tools/sync.py to create the stub, then write it to the v2 standard with figures, set status: done and rebuild.
```

**Build an add-on** (see [[Add-on Ideas]]):
```text
Read CLAUDE.md and _System/Add-on Ideas.md. Build add-on #<n>. Propose the design in 5 bullet points first and wait for my OK before writing code.
```

---

## Round 2 prompt (October 2026 review: all 85 lessons are done at v2)

```text
Read CLAUDE.md, _System/Style Guide.md, _System/Lesson Audit.md and _System/Add-on Ideas.md first. All 85 lessons are already at v2. This round fills content gaps and improves the learning experience. Same rules as before: never delete lesson text, verify every number in Python, EN + TH mirror, figures for every new section, one batch at a time, then stop and report.

BATCHES:
C1  New lessons (add to _tools/curriculum.json, run sync.py, write to v2 with figures):
    - 0.11 "Personal Finance First: emergency fund, debt, money you can afford to risk"
    - 2.8  "Indicators: moving averages, RSI, MACD, ATR, volume — what they measure and their limits"
    - 2.9  "Classic chart patterns: double top/bottom, head & shoulders, triangles, flags — with failure rates and context"
    Place each before the phase checkpoint in the reading order and add questions about them to that checkpoint's quiz.
C2  New lessons:
    - 3.8 "Trade management: partial profits, trailing stops, scaling in and out"
    - 3.9 "Portfolio risk: correlation, total open risk, Kelly (and why to use a fraction of it), Monte Carlo drawdowns" (runnable Monte Carlo in _tools/quant/, show real output)
    - 0.12 "Short selling: how it works, borrow fees, short squeezes"
C3  New Phase 12 "History Lessons" (case studies, each with a candlestick or line chart, timeline, what traders who followed this course's rules would have done): 1987 crash, 2008 crisis, 2015 Swiss franc shock, 2020 COVID crash, 2022 rate hikes, FTX 2022, SVB 2023. Research facts and cite dates.
C4  Investing gaps in Phase 10/11: dollar-cost averaging vs lump sum (computed example), index funds & ETFs for long-term investors, dividends, REITs/real estate, bonds as an investment. Then a Thailand/Laos lesson: accessing SET, LSX and US stocks, taxes and tax-saving funds — research current rules, date-stamp them, add a caution that rules change.
C5  Tools lesson: TradingView basics (drawing levels, alerts, multi-timeframe layout), economic calendar setup, screeners; plus "Prop firms & funded accounts: how they work, the maths of the challenge, red flags".
C6  Learning experience on the website:
    - a 1-minute "In this lesson you'll learn / Key takeaway" box at the top of every lesson (generated from existing mindset + key blocks where possible; write it where missing)
    - site search and glossary hover tooltips (from _System/Glossary.md)
    - a position-size calculator page (forex, gold, stocks, crypto) linked from 0.3, 0.4 and 3.2
    - a disclaimer / how-to-use page
C7  Practice drills: an interactive "chart drill" page per phase (generated candles; the reader clicks to mark HH/HL, BOS, FVG, Elliott waves, entry/stop/target; the page checks the answer and explains). Start with Phases 1, 2 and 5.
C8  Obsidian study tools: Trading Journal template, Backtest Log template, a Bases dashboard (win rate, R, expectancy by setup), and flashcards for the Spaced Repetition plugin generated from the Glossary and every [!check] question.
C9  Quality pass: add "last reviewed: <date>" to every lesson's frontmatter; list every time-sensitive fact (prices, rates, rules, release times) in _System/Fact Register.md with source and date; re-render all figures and fix any overlapping or overflowing text; flag Thai passages that read like machine translation for my own review.
C10 Publish: GitHub Pages setup guide and a workflow that runs build.py; then a printable PDF per phase.
```
