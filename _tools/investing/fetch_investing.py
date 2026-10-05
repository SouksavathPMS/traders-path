#!/usr/bin/env python3
"""Download the monthly price data used by the C4 investing lessons (10.9-10.14) into _tools/investing/data/.
Run once (needs internet):  python3 _tools/investing/fetch_investing.py
The figures and _tools/investing/analysis.py read the saved JSON, so everything rebuilds offline.

Source: Yahoo Finance chart API (free, public). Rows are [date, close, adjusted close];
the adjusted close includes reinvested dividends, so it is a total-return series.
  ^GSPC     S&P 500 price index            ^SP500TR  S&P 500 total-return index
  VNQ       Vanguard US REIT ETF (Yahoo has no usable history for the Thai SET index)
  SHY / IEF / TLT  US Treasury ETFs: 1-3 year, 7-10 year, 20+ year
"""
import datetime as dt
import json
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent / "data"
UA = {"User-Agent": "Mozilla/5.0"}
END = (2026, 10, 1)


def yahoo_monthly(symbol, start):
    p1 = int(dt.datetime(*start, tzinfo=dt.timezone.utc).timestamp())
    p2 = int(dt.datetime(*END, tzinfo=dt.timezone.utc).timestamp())
    sym = symbol.replace("^", "%5E")
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?period1={p1}&period2={p2}&interval=1mo&events=div"
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        res = json.load(r)["chart"]["result"][0]
    close = res["indicators"]["quote"][0]["close"]
    adj = res["indicators"].get("adjclose", [{}])[0].get("adjclose") or close
    rows = []
    for i, ts in enumerate(res["timestamp"]):
        if close[i] is None or adj[i] is None:
            continue
        rows.append([dt.datetime.fromtimestamp(ts, dt.timezone.utc).date().isoformat()[:7], round(close[i], 4), round(adj[i], 4)])
    return {"source": f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol} (monthly)", "rows": rows}


DATASETS = {
    "gspc_m": ("^GSPC", (1988, 1, 1)),
    "sp500tr_m": ("^SP500TR", (1988, 1, 1)),
    "vnq_m": ("VNQ", (2005, 1, 1)),
    "shy_m": ("SHY", (2003, 1, 1)),
    "ief_m": ("IEF", (2003, 1, 1)),
    "tlt_m": ("TLT", (2003, 1, 1)),
}

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for name, (sym, start) in DATASETS.items():
        d = yahoo_monthly(sym, start)
        d["fetched"] = dt.date.today().isoformat()
        (OUT / f"{name}.json").write_text(json.dumps(d), encoding="utf-8")
        print(f"{name}: {len(d['rows'])} rows, {d['rows'][0][0]} → {d['rows'][-1][0]}")
