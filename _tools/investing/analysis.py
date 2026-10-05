#!/usr/bin/env python3
"""Every number used in lessons 10.9-10.14 (C4) is computed here from the saved data.
Run:  python3 _tools/investing/analysis.py
Simplifications are stated next to each calculation (no taxes, cash earns 0% while waiting in DCA, etc.).
"""
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"


def load(name):
    return json.loads((DATA / f"{name}.json").read_text(encoding="utf-8"))["rows"]


def series(name, col=2):
    """{YYYY-MM: value}; col 1 = close (price only), col 2 = adjusted close (dividends reinvested)."""
    return {r[0]: r[col] for r in load(name)}


def cagr(v0, v1, years):
    return (v1 / v0) ** (1 / years) - 1


def max_dd(vals):
    peak, dd = vals[0], 0.0
    for v in vals:
        peak = max(peak, v)
        dd = min(dd, v / peak - 1)
    return dd


def months_between(a, b):
    return (int(b[:4]) - int(a[:4])) * 12 + int(b[5:]) - int(a[5:])


# ---------------------------------------------------------------- DCA vs lump sum (10.10)
def dca_vs_lump(total=120_000, n=12, hold=12):
    """Lump sum invested in month s vs 1/n of it invested at the start of each of n months (cash earns 0%).
    Both valued `hold` months after s. Uses S&P 500 total return (^SP500TR), monthly closes."""
    tr = load("sp500tr_m")
    px = [r[2] for r in tr]
    out = []
    for s in range(len(px) - hold):
        lump = total * px[s + hold] / px[s]
        dca = sum(total / n * px[s + hold] / px[s + k] for k in range(n))
        out.append((tr[s][0], lump, dca))
    return out


def dca_case(start, total=120_000, n=12, hold=12):
    for d, lump, dca in dca_vs_lump(total, n, hold):
        if d == start:
            return lump, dca


# ---------------------------------------------------------------- fees (10.9)
def fee_drag(amount=1_000_000, gross=0.07, years=30, fees=(0.0005, 0.005, 0.015)):
    return {f: amount * ((1 + gross) * (1 - f)) ** years for f in fees}


# ---------------------------------------------------------------- bonds (10.11)
def bond_price(coupon, ytm, years, face=100, freq=1):
    c, r, n = coupon * face / freq, ytm / freq, int(years * freq)
    return sum(c / (1 + r) ** k for k in range(1, n + 1)) + face / (1 + r) ** n


def year_return(name, y):
    s = series(name)
    return s[f"{y}-12"] / s[f"{y - 1}-12"] - 1


def dd_window(name, a, b):
    s = series(name)
    return max_dd([v for k, v in sorted(s.items()) if a <= k <= b])


if __name__ == "__main__":
    # 10.9 index funds: fees
    print("== fees: 1,000,000 at 7%/yr gross for 30 years")
    for f, v in fee_drag().items():
        print(f"  fee {f:.2%}: {v:,.0f}")
    g, t = series("gspc_m", 1), series("sp500tr_m")
    yrs = months_between("1988-01", "2026-09") / 12
    print(f"== S&P 500 1988-01 → 2026-09 ({yrs:.2f} y): price x{g['2026-09']/g['1988-01']:.2f} CAGR {cagr(g['1988-01'], g['2026-09'], yrs):.2%};"
          f" total return x{t['2026-09']/t['1988-01']:.2f} CAGR {cagr(t['1988-01'], t['2026-09'], yrs):.2%}")
    print(f"   100,000 → price {100000*g['2026-09']/g['1988-01']:,.0f}, total {100000*t['2026-09']/t['1988-01']:,.0f}")

    # 10.10 DCA
    res = dca_vs_lump()
    wins = sum(1 for _, l, d in res if l > d)
    diff = [(l - d) / 120_000 for _, l, d in res]
    print(f"== DCA vs lump sum, 12-month DCA, {len(res)} windows {res[0][0]} → {res[-1][0]}")
    print(f"  lump wins {wins}/{len(res)} = {wins/len(res):.1%}; avg edge {sum(diff)/len(diff):+.2%} of 120,000")
    best = max(res, key=lambda r: r[2] - r[1]); worst = max(res, key=lambda r: r[1] - r[2])
    print(f"  DCA best: {best[0]} lump {best[1]:,.0f} dca {best[2]:,.0f}; lump best: {worst[0]} lump {worst[1]:,.0f} dca {worst[2]:,.0f}")
    for st in ("2007-10", "2009-03", "2020-01", "2021-12"):
        l, d = dca_case(st)
        print(f"  start {st}: lump {l:,.0f}  dca {d:,.0f}")
    r10 = dca_vs_lump(hold=120)
    w10 = sum(1 for _, l, d in r10 if l > d)
    print(f"  valued after 10 years instead: lump wins {w10}/{len(r10)} = {w10/len(r10):.1%}")
    # regret: months where the lump sum was underwater after 12 months
    neg = sum(1 for _, l, d in res if l < 120_000)
    print(f"  lump sum below 120,000 after 12 months: {neg}/{len(res)} = {neg/len(res):.1%}")

    # 10.11 bonds
    print("== bond prices (annual coupon)")
    for c, y, n in [(0.04, 0.04, 10), (0.04, 0.05, 10), (0.04, 0.03, 10), (0.04, 0.05, 2), (0.04, 0.05, 30), (0.03, 0.05, 5)]:
        print(f"  coupon {c:.0%} ytm {y:.0%} {n}y: {bond_price(c, y, n):.2f}")
    for nm in ("shy_m", "ief_m", "tlt_m"):
        print(f"  {nm} 2022 total return {year_return(nm, 2022):+.1%}; drawdown 2020-01..2026-09 {dd_window(nm, '2020-01', '2026-09'):.1%}")
    # ladder: 1,000,000 split over 1-5 year rungs
    print("  ladder: 200,000 per rung, 1..5 years")

    # 10.13 REITs
    v, vp = series("vnq_m"), series("vnq_m", 1)
    a, b = "2005-01", "2026-09"
    yv = months_between(a, b) / 12
    print(f"== VNQ {a} → {b}: total CAGR {cagr(v[a], v[b], yv):.2%}, price CAGR {cagr(vp[a], vp[b], yv):.2%};"
          f" S&P TR CAGR {cagr(t[a], t[b], yv):.2%}")
    print(f"  VNQ max drawdown 2007-2009 {dd_window('vnq_m', '2006-01', '2010-12'):.1%}; S&P TR {dd_window('sp500tr_m', '2006-01', '2010-12'):.1%}")
    print(f"  VNQ 2022 {year_return('vnq_m', 2022):+.1%}; S&P TR 2022 {year_return('sp500tr_m', 2022):+.1%}")
    print(f"  VNQ 2020 {year_return('vnq_m', 2020):+.1%}; S&P TR 2020 {year_return('sp500tr_m', 2020):+.1%}")

    # 10.12 dividends: withholding examples on 10,000 USD of US dividends
    print("== US dividend 1,000 USD: Thai resident (treaty 15%) keeps 850; no treaty (e.g. Laos, 30%) keeps 700")
