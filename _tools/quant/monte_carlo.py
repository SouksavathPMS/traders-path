#!/usr/bin/env python3
"""Monte Carlo drawdowns for a trading system (Lesson 3.9). Pure Python, no dependencies.

The system: each trade wins with probability W and makes +B R, or loses -1 R (plus optional costs).
Each run plays N trades, risking a fixed % of the *current* account per trade, and records
the final account and the worst drop from a peak (max drawdown).

Run:  python3 _tools/quant/monte_carlo.py                        (defaults used in lesson 3.9)
      python3 _tools/quant/monte_carlo.py --win 0.40 --payoff 2.5 --risk 0.5 --trades 300
      python3 _tools/quant/monte_carlo.py --compare                (Kelly vs fractions table)
"""
import argparse
import math
import random


def kelly(win, payoff):
    """Kelly fraction for a bet that wins `payoff` per 1 risked with probability `win`."""
    return win - (1 - win) / payoff


def run(win, payoff, risk, trades, runs, seed, cost=0.0):
    """Return a list of (final_equity, max_drawdown, longest_losing_streak) per run. Equity starts at 1.0."""
    rnd = random.Random(seed)
    out = []
    for _ in range(runs):
        eq = peak = 1.0
        max_dd = 0.0
        streak = longest = 0
        for _ in range(trades):
            if rnd.random() < win:
                eq *= 1 + risk * (payoff - cost)
                streak = 0
            else:
                eq *= 1 - risk * (1 + cost)
                streak += 1
                longest = max(longest, streak)
            peak = max(peak, eq)
            max_dd = max(max_dd, 1 - eq / peak)
        out.append((eq, max_dd, longest))
    return out


def pct(xs, p):
    """p-th percentile (0-100) of a list, nearest-rank method."""
    s = sorted(xs)
    k = max(0, min(len(s) - 1, int(math.ceil(p / 100 * len(s))) - 1))
    return s[k]


def report(win, payoff, risk_pct, trades, runs, seed, cost):
    res = run(win, payoff, risk_pct / 100, trades, runs, seed, cost)
    fin = [r[0] for r in res]
    dd = [r[1] for r in res]
    st = [r[2] for r in res]
    ev = win * payoff - (1 - win) * 1 - cost
    print(f"System: win {win:.0%}, win = +{payoff}R, loss = -1R, cost {cost}R  ->  expectancy {ev:+.2f}R per trade")
    print(f"Risk {risk_pct}% per trade, {trades} trades, {runs:,} runs, seed {seed}")
    print("                 5th pct   median   95th pct")
    print(f"final account   {pct(fin, 5) * 100 - 100:+8.1f}% {pct(fin, 50) * 100 - 100:+8.1f}% {pct(fin, 95) * 100 - 100:+8.1f}%")
    print(f"max drawdown    {pct(dd, 5) * 100:8.1f}% {pct(dd, 50) * 100:8.1f}% {pct(dd, 95) * 100:8.1f}%")
    print(f"longest losing  {pct(st, 5):8d}  {pct(st, 50):8d}  {pct(st, 95):8d}")
    for lvl in (0.10, 0.20, 0.30, 0.50):
        p = sum(1 for x in dd if x >= lvl) / runs
        print(f"P(drawdown >= {lvl:.0%}) = {p:.1%}")
    print(f"P(account ends below start) = {sum(1 for x in fin if x < 1) / runs:.1%}")


def compare(win, payoff, trades, runs, seed, cost):
    f = kelly(win, payoff)
    print(f"Kelly fraction for win {win:.0%}, payoff {payoff}R: {win} - {1 - win:.2f}/{payoff} = {f:.3f} ({f:.1%} per trade)")
    print("risk/trade   median final   median maxDD   95th pct maxDD   P(DD>=50%)")
    for label, r in (("full Kelly", f), ("half Kelly", f / 2), ("quarter K.", f / 4), ("2%", 0.02), ("1%", 0.01)):
        res = run(win, payoff, r, trades, runs, seed, cost)
        fin = [x[0] for x in res]
        dd = [x[1] for x in res]
        p50 = sum(1 for x in dd if x >= 0.5) / runs
        print(f"{label:<10} {r * 100:5.2f}%  {pct(fin, 50) * 100 - 100:+12.0f}%  {pct(dd, 50) * 100:11.1f}%  {pct(dd, 95) * 100:13.1f}%  {p50:10.1%}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--win", type=float, default=0.45, help="win rate, e.g. 0.45")
    ap.add_argument("--payoff", type=float, default=2.0, help="average win in R, e.g. 2.0")
    ap.add_argument("--risk", type=float, default=1.0, help="risk per trade in %% of the account")
    ap.add_argument("--trades", type=int, default=200)
    ap.add_argument("--runs", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--cost", type=float, default=0.0, help="cost per trade in R, e.g. 0.05")
    ap.add_argument("--compare", action="store_true", help="compare Kelly, half/quarter Kelly, 2%% and 1%%")
    a = ap.parse_args()
    if a.compare:
        compare(a.win, a.payoff, a.trades, a.runs, a.seed, a.cost)
    else:
        report(a.win, a.payoff, a.risk, a.trades, a.runs, a.seed, a.cost)
