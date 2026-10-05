#!/usr/bin/env python3
"""A simple, honest trend-following backtest (Lesson 9.5). Pure Python, no dependencies.

Strategy: long when the fast moving average is above the slow one, flat otherwise.
Honesty rules built in:
  - signal computed on today's close, trade executed on the NEXT bar (no look-ahead)
  - trading cost charged on every position change
  - parameters chosen on the first 70% of the data (in-sample), judged on the last 30% (out-of-sample)

Run:  python3 _tools/quant/sma_crossover.py            (synthetic data, reproducible)
      python3 _tools/quant/sma_crossover.py prices.csv (one close per line, oldest first)
"""
import math
import random
import sys

COST = 0.001  # 0.10% per position change (commission + spread + slippage)


# ---------------------------------------------------------------- data
def synthetic_prices(n=2016, seed=42):
    """Random walk with persistent bull/bear regimes (8 years of daily bars)."""
    rnd = random.Random(seed)
    p, out, bull = 100.0, [], True
    for _ in range(n):
        if rnd.random() < 1 / 180:            # regimes last ~180 days on average
            bull = not bull
        mu = 0.14 if bull else -0.12          # annual drift
        r = mu / 252 + 0.18 / math.sqrt(252) * rnd.gauss(0, 1)
        p *= math.exp(r)
        out.append(p)
    return out


def load_csv(path):
    with open(path) as f:
        return [float(line.strip().split(",")[-1]) for line in f if line.strip() and line[0].isdigit()]


# ---------------------------------------------------------------- strategy
def sma(xs, n):
    out, s = [None] * len(xs), 0.0
    for i, x in enumerate(xs):
        s += x
        if i >= n:
            s -= xs[i - n]
        if i >= n - 1:
            out[i] = s / n
    return out


def backtest(prices, fast, slow, cost=COST):
    """Returns (daily strategy returns, positions, list of round-trip trade returns)."""
    f, s = sma(prices, fast), sma(prices, slow)
    pos = [0] * len(prices)
    for i in range(len(prices)):
        if f[i] is not None and s[i] is not None:
            pos[i] = 1 if f[i] > s[i] else 0
    rets, trades, entry = [0.0], [], None
    for i in range(1, len(prices)):
        held = pos[i - 1]                       # yesterday's signal = today's position
        r = held * (prices[i] / prices[i - 1] - 1)
        if i >= 2 and pos[i - 1] != pos[i - 2]:  # position changed at today's open
            r -= cost
            if pos[i - 1] == 1:
                entry = prices[i - 1]
            elif entry is not None:
                trades.append(prices[i - 1] / entry - 1 - 2 * cost)
                entry = None
        rets.append(r)
    if entry is not None:
        trades.append(prices[-1] / entry - 1 - 2 * cost)
    return rets, pos, trades


# ---------------------------------------------------------------- metrics
def equity(rets):
    e, out = 1.0, []
    for r in rets:
        e *= 1 + r
        out.append(e)
    return out


def metrics(rets, trades=None):
    n = len(rets)
    eq = equity(rets)
    mean = sum(rets) / n
    sd = math.sqrt(sum((r - mean) ** 2 for r in rets) / (n - 1))
    down = math.sqrt(sum(min(r, 0) ** 2 for r in rets) / n)
    peak, mdd = 1.0, 0.0
    for v in eq:
        peak = max(peak, v)
        mdd = max(mdd, 1 - v / peak)
    m = dict(
        cagr=eq[-1] ** (252 / n) - 1,
        vol=sd * math.sqrt(252),
        sharpe=mean / sd * math.sqrt(252) if sd else 0.0,
        sortino=mean / down * math.sqrt(252) if down else 0.0,
        max_dd=mdd,
        total=eq[-1] - 1,
    )
    if trades:
        wins = [t for t in trades if t > 0]
        losses = [t for t in trades if t <= 0]
        m.update(
            trades=len(trades),
            win_rate=len(wins) / len(trades),
            avg_win=sum(wins) / len(wins) if wins else 0.0,
            avg_loss=sum(losses) / len(losses) if losses else 0.0,
            profit_factor=sum(wins) / -sum(losses) if losses and sum(losses) else float("inf"),
        )
    return m


def optimise(prices, fasts=(10, 20, 30, 50), slows=(100, 150, 200)):
    """Pick the best (fast, slow) by in-sample Sharpe. Returns the full grid too."""
    grid = []
    for fa in fasts:
        for sl in slows:
            if fa < sl:
                rets, _, _ = backtest(prices, fa, sl)
                grid.append((metrics(rets)["sharpe"], fa, sl))
    grid.sort(reverse=True)
    return grid


def run(prices, split=0.7):
    cut = int(len(prices) * split)
    grid = optimise(prices[:cut])
    _, fa, sl = grid[0]
    rets, pos, trades = backtest(prices, fa, sl)
    bh = [0.0] + [prices[i] / prices[i - 1] - 1 for i in range(1, len(prices))]
    oos_trades = backtest(prices[cut - sl:], fa, sl)[2]
    return dict(
        fast=fa, slow=sl, cut=cut, grid=grid, rets=rets, pos=pos, bh=bh,
        ins=metrics(rets[:cut], trades), oos=metrics(rets[cut:], oos_trades),
        bh_ins=metrics(bh[:cut]), bh_oos=metrics(bh[cut:]),
    )


def fmt(m):
    s = (f"CAGR {m['cagr']:+.1%}  vol {m['vol']:.1%}  Sharpe {m['sharpe']:.2f}  "
         f"Sortino {m['sortino']:.2f}  maxDD {m['max_dd']:.1%}")
    if "trades" in m:
        s += (f"  trades {m['trades']}  win {m['win_rate']:.0%}  PF {m['profit_factor']:.2f}"
              f"  avg win {m['avg_win']:+.1%}  avg loss {m['avg_loss']:+.1%}")
    return s


if __name__ == "__main__":
    prices = load_csv(sys.argv[1]) if len(sys.argv) > 1 else synthetic_prices()
    res = run(prices)
    print(f"bars: {len(prices)}  in-sample: {res['cut']}  out-of-sample: {len(prices) - res['cut']}")
    print(f"best parameters in-sample: SMA {res['fast']} / {res['slow']}")
    print("top 3 in-sample Sharpe:", [(round(sh, 2), fa, sl) for sh, fa, sl in res["grid"][:3]])
    print("IN-SAMPLE   strategy :", fmt(res["ins"]))
    print("IN-SAMPLE   buy&hold :", fmt(res["bh_ins"]))
    print("OUT-SAMPLE  strategy :", fmt(res["oos"]))
    print("OUT-SAMPLE  buy&hold :", fmt(res["bh_oos"]))
