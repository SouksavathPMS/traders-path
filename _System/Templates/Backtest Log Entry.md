---
trade_date: 
market: 
timeframe: 
setup: 
rules_version: "1.0"
sample: in-sample
direction: 
entry: 
stop: 
target: 
r: 
costs_included: true
ugly: false
tags: [backtest]
---
# Backtest · {{title}}

> [!note] How to use
> One note per setup found while replaying the past (lesson [[9.3 Backtesting Without Fooling Yourself|9.3]]). Write the rules **before** you start and keep `rules_version` fixed for the whole test. Log **every** setup that meets the rules, including the ugly ones (`ugly: true`). `sample` = `in-sample` (data used to choose the rules), `out-of-sample` (kept aside, used **once**) or `forward` (real time, paper or small size). `r` = result in R after costs. The [[Backtest Log.base|Backtest Log]] dashboard compares the three samples.

## Did the setup meet every rule?
- [ ] Location: 
- [ ] Trigger: 
- [ ] Filters: 

## What happened (only information available at that time)
- Entry / stop / target: 
- Exit and R (after costs): 

## Screenshot
- 
