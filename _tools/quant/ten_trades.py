#!/usr/bin/env python3
"""Statistics and performance metrics for a list of trade results in R (Lessons 9.1 and 9.6).
Pure Python, no dependencies.

Run:  python3 _tools/quant/ten_trades.py                 (the 10-trade example from the lessons)
      python3 _tools/quant/ten_trades.py 1.5 -1 2 -1 ...  (your own R-multiples)
"""
import math
import sys

# The example list used in 9.1 and 9.6: ten trades, each result in R (1R = the money lost at the stop).
EXAMPLE = [2.0, -1.0, 0.5, -1.0, 3.0, -1.0, 1.5, -0.5, -1.0, 2.5]


def describe(r):
    n = len(r)
    mean = sum(r) / n                                   # average result per trade
    s = sorted(r)
    median = (s[n // 2 - 1] + s[n // 2]) / 2 if n % 2 == 0 else s[n // 2]   # middle value
    sd = math.sqrt(sum((x - mean) ** 2 for x in r) / (n - 1))              # sample standard deviation
    return n, mean, median, sd


def metrics(r):
    n, mean, median, sd = describe(r)
    wins = [x for x in r if x > 0]
    losses = [x for x in r if x <= 0]
    profit_factor = sum(wins) / -sum(losses)            # gross wins ÷ gross losses
    downside = math.sqrt(sum(min(x, 0) ** 2 for x in r) / n)   # only the losing side counts
    # running total (equity curve in R) and the worst peak-to-trough fall
    total, peak, max_dd, curve = 0.0, 0.0, 0.0, []
    for x in r:
        total += x
        curve.append(total)
        peak = max(peak, total)
        max_dd = max(max_dd, peak - total)
    return dict(
        trades=n, win_rate=len(wins) / n, mean=mean, median=median, sd=sd,
        se=sd / math.sqrt(n),                           # uncertainty of the mean (9.1)
        avg_win=sum(wins) / len(wins), avg_loss=sum(losses) / len(losses),
        profit_factor=profit_factor,
        sharpe_per_trade=mean / sd,                     # "Sharpe-like": mean ÷ spread, per trade
        sortino_per_trade=mean / downside,              # same, but only losses count as risk
        max_dd=max_dd, curve=curve, total=total,
    )


if __name__ == "__main__":
    r = [float(x) for x in sys.argv[1:]] or EXAMPLE
    m = metrics(r)
    lo, hi = m["mean"] - 1.96 * m["se"], m["mean"] + 1.96 * m["se"]
    print("trades (R):", r)
    print(f"trades {m['trades']}  win rate {m['win_rate']:.0%}  total {m['total']:+.1f}R")
    print(f"mean {m['mean']:+.2f}R  median {m['median']:+.2f}R  sd {m['sd']:.2f}R")
    print(f"uncertainty of mean (sd/sqrt n) {m['se']:.2f}R  -> 95% range {lo:+.2f}R to {hi:+.2f}R")
    print(f"avg win {m['avg_win']:+.2f}R  avg loss {m['avg_loss']:+.2f}R  profit factor {m['profit_factor']:.2f}")
    print(f"Sharpe-like (per trade) {m['sharpe_per_trade']:.2f}  Sortino-like (per trade) {m['sortino_per_trade']:.2f}")
    print("equity curve (R):", [round(x, 1) for x in m["curve"]])
    print(f"max drawdown {m['max_dd']:.1f}R")
