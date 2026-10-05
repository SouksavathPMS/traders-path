---
tags: [moc]
---
# Trader's Path · เส้นทางนักเทรด

> [!concept] What this vault is
> A step-by-step learning path from the first candle to Wall Street macro. Every note here is the **source** for the bilingual (EN / TH) website in `site/`.
> Vault นี้คือเส้นทางการเรียนรู้ทีละขั้น ตั้งแต่แท่งเทียนแรกจนถึงเศรษฐกิจมหภาค ทุกโน้ตคือ **ต้นฉบับ** ของเว็บไซต์สองภาษาในโฟลเดอร์ `site/`

## Start here
- [[Roadmap]] — the 11 phases and how they map to the iceberg
- [[Style Guide]] — how every lesson is written (the mindset flow)
- [[Task Board]] — what is done, what is next
- [[Glossary]] — every term, EN ↔ TH
- [[Publishing Guide]] — put the website and phase PDFs online with GitHub Pages (automatic builds)
- [[Learning Toolkit]] — templates, dashboards (Bases) and flashcards for journaling, reviewing and self-testing
- [[Lesson Audit]] — which lessons have the beginner-friendly v2 layer
- [[Add-on Ideas]] — extra modules and tools worth adding
- [[Claude Code Handoff]] — the prompt for continuing this project with Claude Code

## Phases
0. [[00 Markets, Brokers & News - Index|The Playing Field: Markets, Brokers & News]] — start here if you've never traded
1. [[01 Foundations - Index|Foundations: The Trader's Mind & The Language of Price]]
2. [[02 Market Structure - Index|Market Structure]]
3. [[03 Risk & Money Management - Index|Risk & Money Management]]
4. [[04 Psychology & Execution - Index|Psychology & Execution]]
5. [[05 Liquidity & ICT - Index|Liquidity & ICT Concepts]]
6. [[06 Fibonacci, Elliott Wave & Std Dev - Index|Fibonacci, Elliott Wave & Std Dev]]
7. [[07 Orderflow & Auction Market Theory - Index|Orderflow & Auction Market Theory]]
8. [[08 Options & Dealer Positioning - Index|Options & Dealer Positioning (GEX)]]
9. [[09 Quant & Data Analysis - Index|Quant & Data Analysis]]
10. [[10 Macro, Wall Street & Investing - Index|Macro, Wall Street & Investing]]
11. [[11 Capstone - Index|Capstone: Your Own System]]
12. [[12 History Lessons - Index|History Lessons: Crashes, Shocks & Collapses]] — case studies that test the course's rules

## Build the website
```bash
python3 _tools/make_figures.py   # regenerate charts & infographics (EN + TH SVG)
python3 _tools/build.py          # turn these notes into site/
open site/index.html
```
