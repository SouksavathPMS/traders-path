#!/usr/bin/env python3
"""Compare exit methods on simulated price paths (Lesson 3.8). Pure Python, no dependencies.

Each trade: entry at 0, stop at -1R. Price moves in small random steps (0.1R per step, 1,500 steps max)
with an optional drift (the "edge"). A stop fills at the price actually reached (so gaps past the stop
cost a little more than 1R); targets fill exactly (limit orders). Trades still open at the end close
at the last price (a time stop).

Run:  python3 _tools/quant/exit_methods.py               (both cases used in lesson 3.8)
      python3 _tools/quant/exit_methods.py --drift 0.002 --trades 5000
"""
import argparse
import random

METHODS = [("Target 1R", ("fixed", 1.0)), ("Target 2R", ("fixed", 2.0)), ("Target 3R", ("fixed", 3.0)),
           ("Half at 2R, BE, rest 4R", ("partial", 2.0, 4.0)), ("Trail 1R after +1R", ("trail",))]


def path(rnd, drift, sd=0.1, n=1500):
    p = 0.0
    for _ in range(n):
        p += drift + rnd.gauss(0, sd)
        yield p


def trade(prices, method):
    """Return the trade result in R."""
    stop, peak, banked, size, half_done = -1.0, 0.0, 0.0, 1.0, False
    p = 0.0
    for p in prices:
        peak = max(peak, p)
        if method[0] == "fixed":
            if p <= stop:
                return p
            if p >= method[1]:
                return method[1]
        elif method[0] == "partial":
            a, b = method[1], method[2]
            if p <= stop:
                return banked + size * p
            if not half_done and p >= a:
                banked, size, stop, half_done = 0.5 * a, 0.5, 0.0, True   # bank half, stop to break-even
            if half_done and p >= b:
                return banked + size * b
        else:  # trail: once +1R is reached, keep the stop 1R below the best price so far
            if peak >= 1.0:
                stop = max(stop, peak - 1.0)
            if p <= stop:
                return p
    return banked + size * p if method[0] == "partial" else p


def compare(drift, trades, seed):
    print(f"drift {drift} R per step, {trades:,} trades per method, seed {seed}")
    print("method                        expectancy   win rate   avg win   avg loss   best")
    for name, m in METHODS:
        rnd = random.Random(seed)                     # same price paths for every method
        res = [trade(path(rnd, drift), m) for _ in range(trades)]
        wins = [r for r in res if r > 0.001]
        losses = [r for r in res if r <= 0.001]
        print(f"{name:<28} {sum(res) / len(res):+9.3f}R {len(wins) / len(res):9.1%} {sum(wins) / max(len(wins), 1):8.2f} "
              f"{sum(losses) / max(len(losses), 1):9.2f} {max(res):7.1f}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--drift", type=float, default=None, help="edge per step in R; omit to run 0 and 0.0012")
    ap.add_argument("--trades", type=int, default=20000)
    ap.add_argument("--seed", type=int, default=11)
    a = ap.parse_args()
    for d in ([a.drift] if a.drift is not None else [0.0, 0.0012]):
        compare(d, a.trades, a.seed)
        print()
