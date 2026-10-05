"""Plain-Python indicator maths used by the 2.8 figures (no numpy)."""
import random


def series(seed=5, legs=((60, 0.35), (45, -0.45), (55, 0.05), (40, 0.4)), start=100.0, vol=0.9):
    """Deterministic OHLCV path: legs = (bars, drift per bar)."""
    rnd = random.Random(seed)
    o = c = start
    out = []
    for n, drift in legs:
        for _ in range(n):
            o = c
            c = o + drift + rnd.gauss(0, vol)
            h = max(o, c) + abs(rnd.gauss(0, vol * 0.6))
            l = min(o, c) - abs(rnd.gauss(0, vol * 0.6))
            v = 1000 * (1 + abs(c - o) / vol) * rnd.uniform(0.7, 1.3)
            out.append([o, h, l, c, v])
    return out


def sma(xs, n):
    return [None if i < n - 1 else sum(xs[i - n + 1:i + 1]) / n for i in range(len(xs))]


def ema(xs, n):
    k, out, e = 2 / (n + 1), [], None
    for i, x in enumerate(xs):
        if i < n - 1:
            out.append(None)
            continue
        e = sum(xs[:n]) / n if i == n - 1 else x * k + e * (1 - k)
        out.append(e)
    return out


def rsi(closes, n=14):
    """Wilder's RSI."""
    out = [None] * len(closes)
    gains = [max(closes[i] - closes[i - 1], 0) for i in range(1, len(closes))]
    losses = [max(closes[i - 1] - closes[i], 0) for i in range(1, len(closes))]
    if len(gains) < n:
        return out
    ag, al = sum(gains[:n]) / n, sum(losses[:n]) / n
    for i in range(n, len(closes)):
        if i > n:
            ag = (ag * (n - 1) + gains[i - 1]) / n
            al = (al * (n - 1) + losses[i - 1]) / n
        out[i] = 100.0 if al == 0 else 100 - 100 / (1 + ag / al)
    return out


def macd(closes, fast=12, slow=26, sig=9):
    ef, es = ema(closes, fast), ema(closes, slow)
    line = [None if a is None or b is None else a - b for a, b in zip(ef, es)]
    valid = [x for x in line if x is not None]
    s = ema(valid, sig)
    pad = len(line) - len(valid)
    signal = [None] * pad + s
    hist = [None if a is None or b is None else a - b for a, b in zip(line, signal)]
    return line, signal, hist


def atr(cs, n=14):
    """Wilder's ATR from [o, h, l, c, ...] rows."""
    tr = [cs[0][1] - cs[0][2]] + [max(h - l, abs(h - cs[i - 1][3]), abs(l - cs[i - 1][3]))
                                  for i, (o, h, l, c, *_) in enumerate(cs) if i > 0]
    out = [None] * len(cs)
    a = sum(tr[:n]) / n
    out[n - 1] = a
    for i in range(n, len(cs)):
        a = (a * (n - 1) + tr[i]) / n
        out[i] = a
    return out
