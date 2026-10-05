#!/usr/bin/env python3
"""Interactive chart drills (C7) for Phases 1, 2 and 5.

Each round is built by a generator, then an independent classifier re-derives the answer from the
candles alone, using the rules taught in the lessons (1.3, 1.4, 1.5, 2.1-2.3, 5.1-5.4). A round is kept
only if the two agree and the answer is unambiguous. Every number in a question or explanation is
computed here. Output: _tools/drills/drills.json (build.py turns it into site/assets/drills-data.js).

Run: python3 _tools/drills/make_drills.py
"""
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from charts import candles_from_path  # noqa: E402

OUT = Path(__file__).resolve().parent / "drills.json"
ROUNDS = 10


def r2(x):
    return round(x + 0.0, 2)


def rc(c):
    return [[r2(v) for v in k] for k in c]


def f(x):
    return f"{x:.2f}"


# ------------------------------------------------------------------ classifiers (the lesson rules)
def body(k):
    return abs(k[3] - k[0])


def rng(k):
    return k[1] - k[2]


def upper(k):
    return k[1] - max(k[0], k[3])


def lower(k):
    return min(k[0], k[3]) - k[2]


def who_won(k):
    """1.3: small body with wicks on both sides = indecision; otherwise the close vs open decides."""
    R = rng(k)
    if body(k) <= 0.2 * R and min(upper(k), lower(k)) >= 0.2 * R:
        return "indecision"
    if body(k) >= 0.4 * R:
        return "bull" if k[3] > k[0] else "bear"
    return None  # in between: not used in a drill


def pin_bar(k):
    """1.4: wick at least 2x the body, close in the outer third of the range."""
    R = rng(k)
    if R <= 0:
        return None
    if lower(k) >= 2 * body(k) and k[3] >= k[2] + 2 * R / 3:
        return "bull"
    if upper(k) >= 2 * body(k) and k[3] <= k[2] + R / 3:
        return "bear"
    return None


def bull_engulfing(c, i, look=5):
    """1.4: bullish body covers the previous (bearish) body and is larger than the recent average body."""
    if i < look:
        return False
    k, p = c[i], c[i - 1]
    if not (k[3] > k[0] and p[3] < p[0]):
        return False
    covers = min(k[0], k[3]) <= min(p[0], p[3]) and max(k[0], k[3]) >= max(p[0], p[3])
    avg = sum(body(x) for x in c[i - look:i]) / look
    return covers and body(k) > avg


def fractals(c):
    """2.1: 5-candle rule. Returns (swing_high_indices, swing_low_indices), confirmed only."""
    hs, ls = [], []
    for i in range(2, len(c) - 2):
        if all(c[i][1] > c[j][1] for j in (i - 2, i - 1, i + 1, i + 2)):
            hs.append(i)
        if all(c[i][2] < c[j][2] for j in (i - 2, i - 1, i + 1, i + 2)):
            ls.append(i)
    return hs, ls


def fvgs(c):
    """5.4: middle-candle indices of 3-candle gaps: bullish if low[i+1] > high[i-1], bearish if high[i+1] < low[i-1]."""
    out = []
    for i in range(1, len(c) - 1):
        if c[i + 1][2] > c[i - 1][1]:
            out.append((i, "bull"))
        elif c[i + 1][1] < c[i - 1][2]:
            out.append((i, "bear"))
    return out


# ------------------------------------------------------------------ helpers
def walk(rnd, n, start=100.0, drift=0.0, bmin=0.3, bmax=1.0, wmax=0.45):
    """Ordinary candles: overlapping, moderate wicks."""
    out, p = [], start
    for _ in range(n):
        o = p
        c = o + rnd.choice([-1, 1]) * rnd.uniform(bmin, bmax) + drift
        h = max(o, c) + rnd.uniform(0.08, wmax)
        l = min(o, c) - rnd.uniform(0.08, wmax)
        out.append([o, h, l, c])
        p = c
    return out


def q(en, th):
    return [en, th]


# ------------------------------------------------------------------ Phase 1
def gen_who_won(rnd):
    target = rnd.choice(["bull", "bear", "indecision"])
    c = walk(rnd, 9)
    o = c[5][0]
    R = rnd.uniform(1.6, 2.4)
    if target == "indecision":
        b = rnd.uniform(0.02, 0.15) * R
        up = rnd.uniform(0.3, 0.55) * (R - b)
        top = o + max(b, 0) + up if rnd.random() < 0.5 else o + up
        cl = o + rnd.choice([-1, 1]) * b
        h = max(o, cl) + up
        l = h - R
    else:
        b = rnd.uniform(0.5, 0.8) * R
        cl = o + b if target == "bull" else o - b
        rest = R - b
        uw = rnd.uniform(0.2, 0.8) * rest
        h = max(o, cl) + uw
        l = min(o, cl) - (rest - uw)
    c[5] = [o, h, l, cl]
    for j in range(6, 9):  # keep following candles connected
        c[j][0] = c[j - 1][3]
        c[j][1] = max(c[j][1], c[j][0] + 0.05)
        c[j][2] = min(c[j][2], c[j][0] - 0.05)
    c = rc(c)
    k = c[5]
    got = who_won(k)
    if got != target:
        return None
    pct = 100 * body(k) / rng(k)
    if got == "indecision":
        e = q(f"Open {f(k[0])}, close {f(k[3])}: the body is only {pct:.0f}% of the range, with wicks on both sides "
              f"(upper {f(upper(k))}, lower {f(lower(k))}). Both sides fought and nobody won: indecision.",
              f"เปิด {f(k[0])} ปิด {f(k[3])}: ตัวแท่งเป็นเพียง {pct:.0f}% ของช่วงราคา มีไส้ทั้งสองด้าน "
              f"(บน {f(upper(k))} ล่าง {f(lower(k))}) ทั้งสองฝ่ายสู้กันแต่ไม่มีใครชนะ: ลังเล")
    else:
        side = ("above", "buyers") if got == "bull" else ("below", "sellers")
        side_th = ("เหนือ", "ผู้ซื้อ") if got == "bull" else ("ใต้", "ผู้ขาย")
        e = q(f"Open {f(k[0])}, close {f(k[3])}: it closed {side[0]} its open with a body of {pct:.0f}% of the range. "
              f"The {side[1]} won this candle.",
              f"เปิด {f(k[0])} ปิด {f(k[3])}: ปิด{side_th[0]}ราคาเปิด ตัวแท่ง {pct:.0f}% ของช่วงราคา "
              f"{side_th[1]}ชนะแท่งนี้")
    return dict(c=c, hl=5, ask="choice", opts=["bull", "bear", "indecision"], a=got, e=e)


def gen_pin_bar(rnd):
    c = walk(rnd, 12, drift=rnd.choice([-0.15, 0.15]))
    i = rnd.randint(4, 10)
    side = rnd.choice(["bull", "bear"])
    o = c[i][0]
    R = rnd.uniform(2.0, 3.0)
    b = rnd.uniform(0.08, 0.2) * R
    if side == "bull":
        hi = o + rnd.uniform(0.02, 0.12) * R
        cl = hi - rnd.uniform(0.0, 0.08) * R
        op = cl - b
        k = [op, hi, hi - R, cl]
    else:
        lo = o - rnd.uniform(0.02, 0.12) * R
        cl = lo + rnd.uniform(0.0, 0.08) * R
        op = cl + b
        k = [op, lo + R, lo, cl]
    shift = c[i][0] - k[0]
    c[i] = [v + shift for v in k]
    for j in range(i + 1, 12):
        d = c[j - 1][3] - c[j][0]
        c[j] = [v + d for v in c[j]]
    c = rc(c)
    found = [j for j in range(len(c)) if pin_bar(c[j])]
    if found != [i]:
        return None
    k = c[i]
    w = lower(k) if side == "bull" else upper(k)
    third = "top" if side == "bull" else "bottom"
    third_th = "บน" if side == "bull" else "ล่าง"
    name = ("hammer", "แฮมเมอร์ (Hammer)") if side == "bull" else ("shooting star", "ชูตติ้งสตาร์ (Shooting star)")
    e = q(f"Candle {i + 1}: {'lower' if side == 'bull' else 'upper'} wick {f(w)} = {w / max(body(k), 0.01):.1f}× the body {f(body(k))}, "
          f"and the close {f(k[3])} is in the {third} third of the range {f(k[2])}–{f(k[1])}. That's a pin bar ({name[0]}). "
          f"Whether it matters depends on where it forms (1.4).",
          f"แท่งที่ {i + 1}: ไส้{'ล่าง' if side == 'bull' else 'บน'} {f(w)} = {w / max(body(k), 0.01):.1f} เท่าของตัวแท่ง {f(body(k))} "
          f"และราคาปิด {f(k[3])} อยู่ในส่วนสาม{third_th}ของช่วง {f(k[2])}–{f(k[1])} นี่คือ Pin bar ({name[1]}) "
          f"จะมีความหมายหรือไม่ขึ้นกับว่าเกิดที่ไหน (1.4)")
    return dict(c=c, ask="click", a=i, e=e)


def gen_engulfing(rnd):
    c = walk(rnd, 12, drift=-0.12, bmin=0.25, bmax=0.7)
    i = rnd.randint(6, 10)
    p = c[i - 1]
    if p[3] >= p[0]:  # make the previous candle bearish
        p[0], p[3] = p[3], p[0]
    pb = body(p)
    o = p[3] - rnd.uniform(0.0, 0.15)
    cl = p[0] + rnd.uniform(0.3, 0.9)
    c[i] = [o, cl + rnd.uniform(0.05, 0.3), o - rnd.uniform(0.05, 0.3), cl]
    for j in range(i + 1, 12):
        d = c[j - 1][3] - c[j][0]
        c[j] = [v + d for v in c[j]]
    c = rc(c)
    found = [j for j in range(len(c)) if bull_engulfing(c, j)]
    if found != [i] or pb < 0.15:
        return None
    k, p = c[i], c[i - 1]
    avg = sum(body(x) for x in c[i - 5:i]) / 5
    e = q(f"Candle {i + 1}: bullish body {f(k[0])}→{f(k[3])} covers the previous bearish body {f(p[0])}→{f(p[3])}, "
          f"and its size {f(body(k))} is larger than the average of the last 5 bodies ({f(avg)}). That's a bullish engulfing.",
          f"แท่งที่ {i + 1}: ตัวแท่งขาขึ้น {f(k[0])}→{f(k[3])} ครอบตัวแท่งขาลงก่อนหน้า {f(p[0])}→{f(p[3])} "
          f"และขนาด {f(body(k))} ใหญ่กว่าค่าเฉลี่ยของ 5 แท่งก่อนหน้า ({f(avg)}) นี่คือ Bullish engulfing")
    return dict(c=c, ask="click", a=i, e=e)


def gen_aggregate(rnd):
    c = rc(walk(rnd, 4, bmin=0.3, bmax=1.1, wmax=0.5))
    O, H, L, C = c[0][0], max(k[1] for k in c), min(k[2] for k in c), c[3][3]
    right = [O, H, L, C]
    wrong1 = [O, H, L, c[2][3]]          # close taken from the 3rd hour
    wrong2 = [c[3][0], c[3][1], L, C]    # open and high taken from the last hour only
    opts = [right, wrong1, wrong2]
    if wrong1 == right or wrong2 == right or wrong1 == wrong2 or abs(c[2][3] - C) < 0.15 or abs(c[3][1] - H) < 0.15 and abs(c[3][0] - O) < 0.15:
        return None
    order = [0, 1, 2]
    rnd.shuffle(order)
    shown = [opts[k] for k in order]
    a = order.index(0)
    hi = max(range(4), key=lambda k: c[k][1]) + 1
    lo = min(range(4), key=lambda k: c[k][2]) + 1
    e = q(f"Open = the first hour's open {f(O)}; high = the highest high {f(H)} (hour {hi}); low = the lowest low {f(L)} (hour {lo}); "
          f"close = the last hour's close {f(C)}.",
          f"เปิด = ราคาเปิดชั่วโมงแรก {f(O)} สูงสุด = จุดสูงสุด {f(H)} (ชั่วโมงที่ {hi}) ต่ำสุด = จุดต่ำสุด {f(L)} (ชั่วโมงที่ {lo}) "
          f"ปิด = ราคาปิดชั่วโมงสุดท้าย {f(C)}")
    return dict(c=c, ask="candle", cand=[[r2(v) for v in o] for o in shown], a=a, e=e)


# ------------------------------------------------------------------ Phase 2
def path_candles(rnd, piv, bars=None, vol=0.12):
    bars = bars or [rnd.randint(4, 5) for _ in range(len(piv) - 1)]
    return rc(candles_from_path(piv, bars, seed=rnd.randint(1, 10 ** 6), vol=vol, wick=0.35)), bars


def pivot_index(bars):
    idx, s = [], 0
    for n in bars:
        s += n
        idx.append(s - 1)
    return idx


def gen_label_swing(rnd):
    kind = rnd.choice(["HH", "HL", "LH", "LL"])
    up = rnd.choice([True, False])
    p = [100.0]
    for k in range(6):
        leg = rnd.uniform(3, 6)
        p.append(p[-1] + (leg if (k % 2 == 0) == up else -leg * rnd.uniform(0.5, 0.95)))
    # force the last swing to the asked label by adjusting the last pivot vs the previous same-type pivot
    last, prev = p[-1], p[-3]
    is_high = p[-1] > p[-2]
    if is_high != (kind in ("HH", "LH")):
        p.append(p[-1] + (-rnd.uniform(3, 5) if is_high else rnd.uniform(3, 5)))
    last_i, prev_i = len(p) - 1, len(p) - 3
    d = rnd.uniform(0.6, 1.8)
    want_higher = kind in ("HH", "HL")
    p[last_i] = p[prev_i] + (d if want_higher else -d)
    if (p[last_i] > p[last_i - 1]) != (kind in ("HH", "LH")):
        return None
    p.append(p[last_i] + (-2.5 if kind in ("HH", "LH") else 2.5))  # confirm with 2+ candles after
    c, bars = path_candles(rnd, p)
    piv = pivot_index(bars)
    hs, ls = fractals(c)
    want = sorted(piv[:-1])
    if sorted(hs + ls) != want:
        return None
    target = piv[last_i - 1]
    same = hs if target in hs else ls
    j = same.index(target)
    if j == 0:
        return None
    prv = same[j - 1]
    if target in hs:
        got = "HH" if c[target][1] > c[prv][1] else "LH"
        a_, b_ = c[target][1], c[prv][1]
        word, word_th = "swing high", "จุดกลับตัวสูง (Swing high)"
    else:
        got = "HL" if c[target][2] > c[prv][2] else "LL"
        a_, b_ = c[target][2], c[prv][2]
        word, word_th = "swing low", "จุดกลับตัวต่ำ (Swing low)"
    if got != kind:
        return None
    marks = [dict(i=i, p=c[i][1] if i in hs else c[i][2], up=i in hs, txt="?" if i == target else "") for i in sorted(hs + ls)]
    rel = "above" if a_ > b_ else "below"
    rel_th = "สูงกว่า" if a_ > b_ else "ต่ำกว่า"
    e = q(f"This {word} at {f(a_)} is {rel} the previous {word} at {f(b_)} → {got}.",
          f"{word_th} นี้ที่ {f(a_)} {rel_th} {word_th} ก่อนหน้าที่ {f(b_)} → {got}")
    return dict(c=c, marks=marks, ask="choice", opts=["HH", "HL", "LH", "LL"], a=got, e=e)


def gen_trend(rnd):
    kind = rnd.choice(["up", "down", "range"])
    p, base = [100.0], 100.0
    if kind == "range":
        top, bot = 100 + rnd.uniform(5, 7), 100.0
        p = [bot + 1.5]
        for k in range(7):
            p.append((top if k % 2 == 0 else bot) + rnd.uniform(-0.4, 0.4))
    else:
        s = 1 if kind == "up" else -1
        p = [base]
        for k in range(7):
            p.append(p[-1] + s * (rnd.uniform(4, 6) if k % 2 == 0 else -rnd.uniform(2, 3.5)))
    p.append(p[-1] + (-2 if p[-1] > p[-2] else 2))
    c, bars = path_candles(rnd, p)
    hs, ls = fractals(c)
    if len(hs) < 3 or len(ls) < 3:
        return None
    H = [c[i][1] for i in hs[-3:]]
    Lw = [c[i][2] for i in ls[-3:]]
    if all(b > a for a, b in zip(H, H[1:])) and all(b > a for a, b in zip(Lw, Lw[1:])):
        got = "up"
    elif all(b < a for a, b in zip(H, H[1:])) and all(b < a for a, b in zip(Lw, Lw[1:])):
        got = "down"
    elif max(H) - min(H) < 1.0 and max(Lw) - min(Lw) < 1.0:
        got = "range"
    else:
        got = None
    if got != kind:
        return None
    hs_t, ls_t = " → ".join(f(x) for x in H), " → ".join(f(x) for x in Lw)
    verdict = {"up": ("higher highs and higher lows: an uptrend", "จุดสูงยกตัวและจุดต่ำยกตัว: ขาขึ้น"),
               "down": ("lower highs and lower lows: a downtrend", "จุดสูงต่ำลงและจุดต่ำต่ำลง: ขาลง"),
               "range": ("highs and lows at about the same levels (each within 1.00): a range",
                         "จุดสูงและจุดต่ำอยู่ระดับเดียวกัน (ห่างไม่เกิน 1.00): กรอบ (Range)")}[got]
    marks = [dict(i=i, p=c[i][1] if i in hs else c[i][2], up=i in hs, txt="") for i in sorted(hs + ls)]
    e = q(f"Last three swing highs {hs_t}; last three swing lows {ls_t}: {verdict[0]}.",
          f"สามจุดสูงล่าสุด {hs_t} สามจุดต่ำล่าสุด {ls_t}: {verdict[1]}")
    return dict(c=c, marks=marks, ask="choice", opts=["up", "down", "range"], a=got, e=e)


def gen_bos_choch(rnd):
    kind = rnd.choice(["bos", "choch", "none"])
    sub = rnd.choice(["up", "down"]) if kind == "none" else None
    piv = [100.0, 106.0, 103.0, 109.5, 106.0]
    piv = [x + rnd.uniform(-0.3, 0.3) for x in piv]
    if kind == "bos" or sub == "up":
        piv.append(piv[3] - rnd.uniform(0.5, 0.9))    # rally back up, closes still below the swing high
    else:
        piv += [piv[3] + rnd.uniform(2, 3)]          # new HH first
        piv.append(piv[4] + rnd.uniform(0.6, 1.0))   # fall back towards the protected low, staying above it
    c, bars = path_candles(rnd, piv, bars=[4, 4, 4, 4, 3] + ([3] if len(piv) == 7 else []), vol=0.08)
    hs, ls = fractals(c)
    if not hs or not ls:
        return None
    sh = hs[-1]
    prot = [i for i in ls if i < sh]
    if not prot:
        return None
    pl = prot[-1]
    SH, PL = c[sh][1], c[pl][2]
    o = c[-1][3]
    if kind == "bos":
        cl = SH + rnd.uniform(0.3, 0.9)
        k = [o, cl + rnd.uniform(0.05, 0.3), o - rnd.uniform(0.05, 0.2), cl]
    elif kind == "choch":
        cl = PL - rnd.uniform(0.3, 0.9)
        k = [o, o + rnd.uniform(0.05, 0.2), cl - rnd.uniform(0.05, 0.3), cl]
    elif sub == "up":
        cl = SH - rnd.uniform(0.2, 0.5)
        k = [o, SH + rnd.uniform(0.3, 0.8), min(o, cl) - 0.15, cl]
    else:
        cl = PL + rnd.uniform(0.2, 0.5)
        k = [o, max(o, cl) + 0.15, PL - rnd.uniform(0.3, 0.8), cl]
    c = rc(c + [k])
    # independent check: no earlier candle after the swing high closed beyond either level
    hs2, ls2 = fractals(c[:-1])
    if not hs2 or hs2[-1] != sh or [i for i in ls2 if i < sh][-1] != pl:
        return None
    if any(x[3] > SH or x[3] < PL for x in c[sh + 1:-1]):
        return None
    last = c[-1]
    got = "bos" if last[3] > SH else "choch" if last[3] < PL else "none"
    if got != kind:
        return None
    lines = [dict(p=SH, k="sh"), dict(p=PL, k="pl")]
    if got == "bos":
        e = q(f"The candle closed at {f(last[3])}, above the last swing high {f(SH)}, in the direction of the uptrend → BOS. "
              f"The protected low moves up to the HL that made this new high.",
              f"แท่งนี้ปิดที่ {f(last[3])} เหนือจุดสูงล่าสุด {f(SH)} ในทิศทางของขาขึ้น → BOS "
              f"จุดต่ำที่ต้องปกป้องเลื่อนขึ้นไปที่ HL ที่สร้างจุดสูงใหม่นี้")
    elif got == "choch":
        e = q(f"The candle closed at {f(last[3])}, below the protected low {f(PL)} (the HL that created the last high {f(SH)}) → CHoCH. "
              f"A warning: stop looking for longs, not an automatic short.",
              f"แท่งนี้ปิดที่ {f(last[3])} ใต้จุดต่ำที่ต้องปกป้อง {f(PL)} (HL ที่สร้างจุดสูงล่าสุด {f(SH)}) → CHoCH "
              f"เป็นคำเตือนให้หยุดหาจังหวะซื้อ ไม่ใช่สัญญาณขายอัตโนมัติ")
    else:
        lvl, wk = (SH, last[1]) if sub == "up" else (PL, last[2])
        e = q(f"The wick reached {f(wk)}, beyond {f(lvl)}, but the candle closed back at {f(last[3])}. "
              f"Only a close beyond the level counts, so there's no break (a possible sweep, 5.2).",
              f"ไส้ไปถึง {f(wk)} เลย {f(lvl)} แต่แท่งปิดกลับมาที่ {f(last[3])} "
              f"นับเฉพาะการปิดเลยระดับเท่านั้น จึงยังไม่มีการเบรก (อาจเป็น Sweep ดู 5.2)")
    return dict(c=c, hl=len(c) - 1, lines=lines, ask="choice", opts=["bos", "choch", "none"], a=got, e=e)


# ------------------------------------------------------------------ Phase 5
def gen_liquidity(rnd):
    up = rnd.choice([True, False])  # equal highs or equal lows
    lvl_a = 100 + rnd.uniform(5.5, 6.5)
    piv = [100.0, lvl_a, 101.5 + rnd.uniform(-0.3, 0.3), 0, 100.8 + rnd.uniform(-0.3, 0.3), 104.0]
    eq = rnd.uniform(0.02, 0.08)
    piv[3] = lvl_a + eq * rnd.choice([-1, 1])
    if not up:  # mirror: equal lows
        piv = [200 - x for x in piv]
    piv.append(piv[-1] + (-2 if piv[-1] > piv[-2] else 2))
    c, bars = path_candles(rnd, piv, vol=0.08)
    hs, ls = fractals(c)
    pts = [(i, c[i][1], "h") for i in hs] + [(i, c[i][2], "l") for i in ls]
    if len(pts) < 4:
        return None
    pair = [(a, b) for a in pts for b in pts if a[0] < b[0] and a[2] == b[2] and abs(a[1] - b[1]) <= 0.10]
    if len(pair) != 1:
        return None
    (i1, p1, t), (i2, p2, _) = pair[0]
    singles = [x for x in pts if x[0] not in (i1, i2) and abs(x[1] - p1) > 0.8]
    if len(singles) < 2:
        return None
    rnd.shuffle(singles)
    levels = [((p1 + p2) / 2, True)] + [(x[1], False) for x in singles[:2]]
    rnd.shuffle(levels)
    letters = "ABC"
    a = letters[[k for k, (_, ok) in enumerate(levels) if ok][0]]
    lines = [dict(p=r2(v), k=letters[k]) for k, (v, _) in enumerate(levels)]
    side = ("highs", "buy stops (BSL) rest above them", "จุดสูง", "คำสั่ง Buy stop (BSL) รออยู่เหนือมัน") if t == "h" else \
           ("lows", "sell stops (SSL) rest below them", "จุดต่ำ", "คำสั่ง Sell stop (SSL) รออยู่ใต้มัน")
    e = q(f"Level {a}: two swing {side[0]} at {f(p1)} and {f(p2)}, only {abs(p1 - p2):.2f} apart → equal {side[0]}. "
          f"They are obvious to everyone, so {side[1]}.",
          f"ระดับ {a}: {side[2]}สองจุดที่ {f(p1)} และ {f(p2)} ห่างกันเพียง {abs(p1 - p2):.2f} → {side[2]}เท่ากัน (Equal {side[0]}) "
          f"ทุกคนเห็นชัด จึงมี{side[3]}")
    return dict(c=c, lines=lines, ask="choice", opts=["A", "B", "C"], a=a, e=e)


def gen_sweep(rnd):
    kind = rnd.choice(["sweep", "run"])
    low_side = rnd.choice([True, False])
    piv = [104.0, 100.0, 103.5, 100.0 + rnd.uniform(0.4, 0.9)]
    if not low_side:
        piv = [200 - x for x in piv]
    c, bars = path_candles(rnd, piv, bars=[4, 4, 4], vol=0.08)
    hs, ls = fractals(c)
    ref = ls if low_side else hs
    if not ref:
        return None
    li = ref[0]
    L = c[li][2] if low_side else c[li][1]
    o = c[-1][3]
    s = 1 if low_side else -1  # +1: level below price
    if kind == "sweep":
        ext = L - s * rnd.uniform(0.3, 0.8)
        cl = L + s * rnd.uniform(0.2, 0.6)
    else:
        ext = L - s * rnd.uniform(0.9, 1.4)
        cl = L - s * rnd.uniform(0.4, 0.8)
    k = [o, max(o, cl) + 0.1, ext, cl] if low_side else [o, ext, min(o, cl) - 0.1, cl]
    c = rc(c + [k])
    if any((x[2] < L if low_side else x[1] > L) for x in c[li + 1:-1]):
        return None
    last = c[-1]
    through = last[2] < L if low_side else last[1] > L
    back = last[3] > L if low_side else last[3] < L
    got = "sweep" if through and back else "run" if through else None
    if got != kind:
        return None
    word = ("low", "below", "SSL") if low_side else ("high", "above", "BSL")
    word_th = ("จุดต่ำ", "ใต้", "SSL") if low_side else ("จุดสูง", "เหนือ", "BSL")
    wk = last[2] if low_side else last[1]
    if got == "sweep":
        e = q(f"The wick went to {f(wk)}, {word[1]} the old {word[0]} {f(L)}, triggering the stops ({word[2]}), "
              f"but the candle closed back at {f(last[3])} → a sweep. It becomes a trade idea only after displacement and a CHoCH/MSS (5.2).",
              f"ไส้ไปถึง {f(wk)} {word_th[1]}{word_th[0]}เดิม {f(L)} ทำให้ Stop ({word_th[2]}) ทำงาน "
              f"แต่แท่งปิดกลับมาที่ {f(last[3])} → Sweep จะเป็นไอเดียเทรดได้หลังมี Displacement และ CHoCH/MSS เท่านั้น (5.2)")
    else:
        e = q(f"The candle closed at {f(last[3])}, {word[1]} the old {word[0]} {f(L)} → accepted beyond the level: a run, not a sweep. "
              f"Don't fade it; the next pool is the target.",
              f"แท่งปิดที่ {f(last[3])} {word_th[1]}{word_th[0]}เดิม {f(L)} → ราคาถูกยอมรับเลยระดับ: เป็นการวิ่งต่อ (Run) ไม่ใช่ Sweep "
              f"อย่าสวน เป้าคือ Pool ถัดไป")
    return dict(c=c, hl=len(c) - 1, lines=[dict(p=L, k="old")], ask="choice", opts=["sweep", "run"], a=got, e=e)


def gen_pd(rnd):
    kind = rnd.choice(["premium", "discount", "eq"])
    lo, hi = 100 + rnd.uniform(-0.5, 0.5), 100 + rnd.uniform(9, 12)
    eq = (lo + hi) / 2
    R = hi - lo
    if kind == "premium":
        tgt = eq + rnd.uniform(0.15, 0.35) * R
    elif kind == "discount":
        tgt = eq - rnd.uniform(0.15, 0.35) * R
    else:
        tgt = eq + rnd.uniform(-0.01, 0.01) * R
    piv = [lo + 2.5, lo, hi, tgt]
    c, bars = path_candles(rnd, piv, bars=[3, 6, 4], vol=0.08)
    hs, ls = fractals(c)
    if not hs or not ls:
        return None
    L, H = c[ls[0]][2], c[hs[-1]][1]
    if not (ls[0] < hs[-1]):
        return None
    # place the last close exactly where the round wants it, measured on the actual leg
    off = {"premium": rnd.uniform(0.15, 0.35), "discount": -rnd.uniform(0.15, 0.35), "eq": rnd.uniform(-0.01, 0.01)}[kind]
    last = c[-1]
    last[3] = r2((L + H) / 2 + off * (H - L))
    last[1] = r2(max(last[1], last[0], last[3]) + 0.0)
    last[2] = r2(min(last[2], last[0], last[3]))
    P = c[-1][3]
    EQ = (L + H) / 2
    pos = (P - L) / (H - L)
    got = "eq" if abs(pos - 0.5) <= 0.02 else ("premium" if pos > 0.5 else "discount")
    if got != kind or c[-1][2] < L:
        return None
    pct = 100 * pos
    word = {"premium": ("above", "premium: expensive for buying", "เหนือ", "Premium: แพงสำหรับการซื้อ"),
            "discount": ("below", "discount: cheap for buying in an up-leg", "ใต้", "Discount: ถูกสำหรับการซื้อในขาขึ้น"),
            "eq": ("at", "equilibrium (within 2% of the 50% line)", "ที่", "Equilibrium (ห่างเส้น 50% ไม่เกิน 2%)")}[got]
    e = q(f"Leg {f(L)} → {f(H)}. EQ = ({f(L)} + {f(H)}) ÷ 2 = {f(EQ)}. Price {f(P)} sits at {pct:.0f}% of the leg, {word[0]} EQ → {word[1]}.",
          f"ขา {f(L)} → {f(H)} EQ = ({f(L)} + {f(H)}) ÷ 2 = {f(EQ)} ราคา {f(P)} อยู่ที่ {pct:.0f}% ของขา {word[2]} EQ → {word[3]}")
    return dict(c=c, zone=dict(lo=L, hi=H), lines=[dict(p=r2(P), k="price")], ask="choice", opts=["premium", "eq", "discount"], a=got, e=e)


def gen_fvg(rnd):
    side = rnd.choice(["bull", "bear"])
    s = 1 if side == "bull" else -1
    c = walk(rnd, 14, bmin=0.2, bmax=0.6, wmax=0.5)
    i = rnd.randint(4, 11)
    c1 = c[i - 1]
    o = c1[3]
    big = rnd.uniform(2.2, 3.2)
    cl = o + s * big
    c[i] = [o, max(o, cl) + 0.1, min(o, cl) - 0.1, cl]
    gap = rnd.uniform(0.35, 0.9)
    edge = c1[1] if side == "bull" else c1[2]
    o3 = cl
    if side == "bull":
        l3 = edge + gap
        c[i + 1] = [o3, o3 + rnd.uniform(0.3, 0.8), l3, o3 + rnd.uniform(0.1, 0.5)]
        c[i + 1][2] = min(l3, c[i + 1][0] - 0.05, c[i + 1][3] - 0.05)
    else:
        h3 = edge - gap
        c[i + 1] = [o3, h3, o3 - rnd.uniform(0.3, 0.8), o3 - rnd.uniform(0.1, 0.5)]
        c[i + 1][1] = max(h3, c[i + 1][0] + 0.05, c[i + 1][3] + 0.05)
    for j in range(i + 2, 14):
        d = c[j - 1][3] - c[j][0]
        c[j] = [v + d for v in c[j]]
    c = rc(c)
    found = fvgs(c)
    if found != [(i, side)]:
        return None
    a1, a3 = c[i - 1], c[i + 1]
    if side == "bull":
        lo_, hi_ = a1[1], a3[2]
        e = q(f"Candles {i}–{i + 2}: candle {i + 2}'s low {f(hi_)} is above candle {i}'s high {f(lo_)} → bullish FVG (BISI) "
              f"of {f(hi_ - lo_)}, CE {f((lo_ + hi_) / 2)}. You click the middle candle ({i + 1}).",
              f"แท่ง {i}–{i + 2}: จุดต่ำของแท่ง {i + 2} ({f(hi_)}) อยู่เหนือจุดสูงของแท่ง {i} ({f(lo_)}) → Bullish FVG (BISI) "
              f"ขนาด {f(hi_ - lo_)} CE {f((lo_ + hi_) / 2)} คลิกแท่งกลาง (แท่งที่ {i + 1})")
    else:
        hi_, lo_ = a1[2], a3[1]
        e = q(f"Candles {i}–{i + 2}: candle {i + 2}'s high {f(lo_)} is below candle {i}'s low {f(hi_)} → bearish FVG (SIBI) "
              f"of {f(hi_ - lo_)}, CE {f((lo_ + hi_) / 2)}. You click the middle candle ({i + 1}).",
              f"แท่ง {i}–{i + 2}: จุดสูงของแท่ง {i + 2} ({f(lo_)}) อยู่ใต้จุดต่ำของแท่ง {i} ({f(hi_)}) → Bearish FVG (SIBI) "
              f"ขนาด {f(hi_ - lo_)} CE {f((lo_ + hi_) / 2)} คลิกแท่งกลาง (แท่งที่ {i + 1})")
    return dict(c=c, ask="click", a=i, zone_fvg=dict(lo=r2(lo_), hi=r2(hi_), i=i), e=e)


# ------------------------------------------------------------------ assemble
DRILLS = {
    "1": [
        ("who-won", gen_who_won, "1.3",
         q("Who won this candle?", "ใครชนะแท่งนี้?"),
         q("Look at the highlighted candle: buyers, sellers, or nobody?", "ดูแท่งที่ไฮไลต์: ผู้ซื้อ ผู้ขาย หรือไม่มีใครชนะ?")),
        ("pin-bar", gen_pin_bar, "1.4",
         q("Find the pin bar", "หา Pin bar"),
         q("Click the one candle with a wick at least 2× its body and a close in the outer third.",
           "คลิกแท่งเดียวที่มีไส้ยาวอย่างน้อย 2 เท่าของตัวแท่ง และปิดในส่วนสามด้านนอก")),
        ("engulfing", gen_engulfing, "1.4",
         q("Find the bullish engulfing", "หา Bullish engulfing"),
         q("Click the bullish candle whose body covers the previous bearish body and is bigger than the recent average.",
           "คลิกแท่งขาขึ้นที่ตัวแท่งครอบตัวแท่งขาลงก่อนหน้า และใหญ่กว่าค่าเฉลี่ยล่าสุด")),
        ("aggregate", gen_aggregate, "1.5",
         q("Build the 4-hour candle", "สร้างแท่ง 4 ชั่วโมง"),
         q("These are four 1-hour candles. Which 4-hour candle do they make?", "นี่คือแท่ง 1 ชั่วโมงสี่แท่ง รวมกันเป็นแท่ง 4 ชั่วโมงแบบไหน?")),
    ],
    "2": [
        ("label-swing", gen_label_swing, "2.1",
         q("Label the swing", "ระบุชนิดของ Swing"),
         q("Dots mark confirmed swings (5-candle rule). What is the swing marked “?”",
           "จุดแสดง Swing ที่ยืนยันแล้ว (กฎ 5 แท่ง) Swing ที่มีเครื่องหมาย “?” คืออะไร?")),
        ("trend", gen_trend, "2.2",
         q("Trend or range?", "เทรนด์หรือกรอบ?"),
         q("Read the last three swing highs and lows. What is the market doing?",
           "อ่านจุดสูงและจุดต่ำสามจุดล่าสุด ตลาดกำลังทำอะไร?")),
        ("bos-choch", gen_bos_choch, "2.3",
         q("BOS, CHoCH or no break?", "BOS, CHoCH หรือยังไม่เบรก?"),
         q("Uptrend. Dashed lines: last swing high and protected low. What did the highlighted candle do?",
           "ขาขึ้น เส้นประ: จุดสูงล่าสุดและจุดต่ำที่ต้องปกป้อง แท่งที่ไฮไลต์ทำอะไร?")),
    ],
    "5": [
        ("liquidity", gen_liquidity, "5.1",
         q("Where are the equal highs or lows?", "Equal highs/lows อยู่ที่ไหน?"),
         q("Which level, A, B or C, has equal highs or equal lows (a crowded pool of stops)?",
           "ระดับไหน A, B หรือ C ที่มีจุดสูงเท่ากันหรือจุดต่ำเท่ากัน (Pool ของ Stop ที่แออัด)?")),
        ("sweep", gen_sweep, "5.2",
         q("Sweep or run?", "Sweep หรือ Run?"),
         q("The highlighted candle traded through the old level. Was it a sweep or a run?",
           "แท่งที่ไฮไลต์ทะลุระดับเดิม เป็น Sweep หรือ Run?")),
        ("pd", gen_pd, "5.3",
         q("Premium or discount?", "Premium หรือ Discount?"),
         q("The shaded box is the current up-leg. Where is the last price?", "กรอบแรเงาคือขาขึ้นปัจจุบัน ราคาล่าสุดอยู่ตรงไหน?")),
        ("fvg", gen_fvg, "5.4",
         q("Click the FVG", "คลิก FVG"),
         q("Click the middle candle of the fair value gap.", "คลิกแท่งกลางของ Fair value gap")),
    ],
}


def main():
    out = {}
    for phase, items in DRILLS.items():
        out[phase] = []
        for key, gen, lesson, title, prompt in items:
            rnd, rounds, tries = random.Random(f"{phase}-{key}"), [], 0
            while len(rounds) < ROUNDS:
                tries += 1
                if tries > 20000:
                    raise SystemExit(f"could not build {key}")
                r = gen(rnd)
                if not r:
                    continue
                if r["ask"] == "choice":  # balance answers so "always click X" never wins
                    cap = -(-ROUNDS // len(r["opts"]))
                    if sum(1 for x in rounds if x["a"] == r["a"]) >= cap:
                        continue
                rounds.append(r)
            out[phase].append(dict(key=key, lesson=lesson, title=title, prompt=prompt, rounds=rounds))
            print(f"phase {phase} {key:12s} {len(rounds)} rounds ({tries} tries)  answers: "
                  + " ".join(str(r['a']) for r in rounds))
    OUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print("wrote", OUT, OUT.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
