"""C5 numbers: lessons 0.13 (TradingView basics), 0.14 (calendars & screeners), 0.15 (prop firms).
Every number written in those lessons comes from this file. Run it to print them.
"""
import random
from datetime import datetime
from zoneinfo import ZoneInfo

BKK = ZoneInfo("Asia/Bangkok")
NY = ZoneInfo("America/New_York")
LDN = ZoneInfo("Europe/London")
FRA = ZoneInfo("Europe/Berlin")

# ------------------------------------------------------------------ 0.13 TradingView
PLANS = {  # tradingview.com/pricing, checked Oct 2026 (monthly price, USD)
    "Basic": dict(price=0, ind=2, charts=1, price_alerts=3, tech_alerts=20, bars=5_000),
    "Essential": dict(price=12.95, ind=5, charts=2, price_alerts=20, tech_alerts=20, bars=10_000),
    "Plus": dict(price=29.95, ind=10, charts=4, price_alerts=100, tech_alerts=100, bars=10_000),
    "Premium": dict(price=59.95, ind=25, charts=8, price_alerts=400, tech_alerts=400, bars=20_000),
}


def bars_cover(bars):
    """How much history N bars shows on common timeframes."""
    return {
        "1m_fx_days": bars / (24 * 60),          # forex trades ~24h on weekdays
        "1m_us_days": bars / 390,                # US cash session 6.5h
        "1h_fx_weeks": bars / (24 * 5),
        "daily_years": bars / 252,
    }


def position_tool(entry, stop, target, risk_money, pip=0.0001, pip_value_per_lot=10):
    risk_pips = abs(entry - stop) / pip
    reward_pips = abs(target - entry) / pip
    lots = risk_money / (risk_pips * pip_value_per_lot)
    return dict(risk_pips=round(risk_pips, 1), reward_pips=round(reward_pips, 1),
                rr=reward_pips / risk_pips, lots=lots, reward_money=lots * reward_pips * pip_value_per_lot)


def log_vs_linear(a0=10, a1=20, b0=100, b1=200):
    return dict(pct_a=(a1 / a0 - 1) * 100, pct_b=(b1 / b0 - 1) * 100,
                linear_height_ratio=(b1 - b0) / (a1 - a0))


# ------------------------------------------------------------------ 0.14 calendars
def to_bkk(y, m, d, hh, mm, tz):
    return datetime(y, m, d, hh, mm, tzinfo=tz).astimezone(BKK)


RELEASES = [  # official schedules (BLS, Federal Reserve), checked Oct 2026; local release times
    ("US CPI", (2026, 10, 14, 8, 30), NY),
    ("FOMC decision", (2026, 10, 28, 14, 0), NY),
    ("US jobs report (NFP)", (2026, 11, 6, 8, 30), NY),
    ("US CPI", (2026, 11, 10, 8, 30), NY),
    ("US jobs report (NFP)", (2026, 12, 4, 8, 30), NY),
    ("FOMC decision", (2026, 12, 9, 14, 0), NY),
    ("US CPI", (2026, 12, 10, 8, 30), NY),
]


def dst_gap_2026():
    """NY open (09:30 NY) and London open (08:00 London) in Bangkok time around the clock changes."""
    out = []
    for d in [(2026, 10, 23), (2026, 10, 27), (2026, 11, 3)]:
        out.append((d, to_bkk(*d, 8, 0, LDN).strftime("%H:%M"), to_bkk(*d, 9, 30, NY).strftime("%H:%M")))
    return out


def surprise(actual, forecast):
    return actual - forecast


# Hypothetical screener universe (made-up example data, labelled as such in the lesson)
UNIVERSE = [
    # name, market cap (bn THB), avg daily value traded (m THB), P/E, price vs 200-day avg (%), div yield %
    ("A", 420, 1450, 14.2, 6.1, 3.4),
    ("B", 95, 310, 9.8, -4.5, 5.2),
    ("C", 12, 18, 7.1, 12.4, 6.8),
    ("D", 260, 820, 31.5, 9.7, 0.9),
    ("E", 38, 140, 11.3, 3.2, 4.1),
    ("F", 6, 4, 4.9, -18.0, 9.5),
    ("G", 150, 560, 16.8, -1.2, 2.7),
    ("H", 71, 95, 12.6, 4.8, 3.9),
    ("I", 510, 2100, 19.4, 2.5, 3.1),
    ("J", 22, 60, 8.4, 7.9, 4.6),
]
FILTERS = [
    ("Market cap ≥ 20bn", lambda r: r[1] >= 20),
    ("Value traded ≥ 50m/day", lambda r: r[2] >= 50),
    ("P/E ≤ 20", lambda r: r[3] <= 20),
    ("Above 200-day average", lambda r: r[4] > 0),
]


def screen():
    rows, steps = UNIVERSE, [("All stocks", len(UNIVERSE), [r[0] for r in UNIVERSE])]
    for name, f in FILTERS:
        rows = [r for r in rows if f(r)]
        steps.append((name, len(rows), [r[0] for r in rows]))
    return steps


# ------------------------------------------------------------------ 0.15 prop firms
def daily_floor(start_of_day_balance, initial=100_000, daily_pct=0.05):
    """FTMO-style: lowest equity allowed today = balance at start of day − 5% of initial."""
    return start_of_day_balance - initial * daily_pct


def trailing_mll(eod_balances, start=50_000, mll=2_000):
    """Topstep-style end-of-day trailing limit that locks at the starting balance."""
    floor, out = start - mll, []
    for b in eod_balances:
        floor = min(max(floor, b - mll), start)
        out.append(floor)
    return out


def simulate(p_win, win_r, risk_pct, target=0.10, max_loss=0.10, daily=0.05, trades_per_day=3,
             max_days=None, n=20_000, seed=7):
    """Chance of reaching the target before breaking a loss rule. Each trade risks risk_pct of the
    INITIAL balance (fixed size), wins win_r × that or loses 1 ×. Static max loss, daily loss limit."""
    rng = random.Random(seed)
    passed, days_used = 0, []
    for _ in range(n):
        bal, day = 0.0, 0
        while True:
            day += 1
            start = bal
            done = None
            for _ in range(trades_per_day):
                bal += risk_pct * win_r if rng.random() < p_win else -risk_pct
                if bal <= -max_loss + 1e-12 or bal <= start - daily + 1e-12:
                    done = "fail"
                    break
                if bal >= target - 1e-12:
                    done = "pass"
                    break
            if done == "pass":
                passed += 1
                days_used.append(day)
                break
            if done == "fail" or (max_days and day >= max_days):
                break
    return passed / n, (sum(days_used) / len(days_used) if days_used else None)


EDGES = {  # (win probability, reward in R)
    "no edge after costs": (0.50, 0.90),   # expectancy −0.05R
    "zero edge": (0.50, 1.00),             # 0R
    "real edge": (0.45, 2.00),             # +0.35R
}


def expectancy(p, r):
    return p * r - (1 - p)


def fee_maths(fee=540, p_pass=0.14, p_payout_given_funded=0.45):
    attempts = 1 / p_pass
    return dict(attempts=attempts, fees=attempts * fee, p_paid=p_pass * p_payout_given_funded)


if __name__ == "__main__":
    print("== 0.13")
    for k, v in PLANS.items():
        print(k, v, {a: round(b, 1) for a, b in bars_cover(v["bars"]).items()})
    print("position tool", position_tool(1.0850, 1.0830, 1.0890, 100))
    print("log vs linear", log_vs_linear())
    print("== 0.14")
    for name, dt, tz in RELEASES:
        print(f"{name:22s} {datetime(*dt, tzinfo=tz):%a %d %b %H:%M %Z} -> {to_bkk(*dt, tz):%a %d %b %H:%M} BKK")
    for d, l, n in dst_gap_2026():
        print("London open / NY open in BKK", d, l, n)
    print("surprise", surprise(3.1, 2.9))
    for d in [(2026, 10, 22), (2026, 11, 5)]:
        print("ECB 14:15 Frankfurt ->", d, to_bkk(*d, 14, 15, FRA).strftime("%H:%M"), "BKK")
    from datetime import date
    print("US winter time 1 Nov 2026 -> 14 Mar 2027:", (date(2027, 3, 14) - date(2026, 11, 1)).days, "days")
    print("5,000 five-minute bars of forex =", round(5000 * 5 / 1440, 1), "days")
    for s in screen():
        print(s)
    print("== 0.15")
    print("daily floor at 104,000:", daily_floor(104_000), " static floor:", 100_000 * 0.9)
    print("trailing", trailing_mll([50_500, 50_000, 51_200, 52_300, 51_000]))
    for name, (p, r) in EDGES.items():
        print(name, "expectancy", round(expectancy(p, r), 3))
        for risk in (0.005, 0.01, 0.02, 0.03):
            pr, d = simulate(p, r, risk)
            print(f"   risk {risk*100:.1f}%  P(pass phase1) {pr*100:.1f}%  avg days {d and round(d,1)}")
    # two-step: phase 1 (10%) then phase 2 (5%), both 1% risk
    for name, (p, r) in EDGES.items():
        p1, _ = simulate(p, r, 0.01)
        p2, _ = simulate(p, r, 0.01, target=0.05, seed=11)
        print("two-step @1%", name, round(p1 * 100, 1), round(p2 * 100, 1), "both", round(p1 * p2 * 100, 1))
    print("fees", fee_maths())
