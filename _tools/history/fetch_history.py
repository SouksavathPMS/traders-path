#!/usr/bin/env python3
"""Download the price data used by the Phase 12 case-study charts and save it in _tools/history/data/.
Run once (needs internet):  python3 _tools/history/fetch_history.py
The saved JSON files are what the figures read, so the charts rebuild offline and stay reproducible.

Sources (free, public):
  Yahoo Finance chart API  - S&P 500 (^GSPC), US 10-year yield (^TNX), regional-bank ETF (KRE)
  Frankfurter (ECB rates)  - EUR/CHF daily reference rate
  Binance public API       - BTC/USDT and FTT/USDT daily candles
"""
import datetime as dt
import json
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent / "data"
UA = {"User-Agent": "Mozilla/5.0"}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return json.load(r)


def yahoo(symbol, start, end, interval="1d"):
    p1 = int(dt.datetime(*start, tzinfo=dt.timezone.utc).timestamp())
    p2 = int(dt.datetime(*end, tzinfo=dt.timezone.utc).timestamp())
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?period1={p1}&period2={p2}&interval={interval}"
    r = get(url)["chart"]["result"][0]
    q = r["indicators"]["quote"][0]
    tz = dt.timezone(dt.timedelta(seconds=r["meta"].get("gmtoffset", 0)))
    rows = []
    for i, ts in enumerate(r["timestamp"]):
        o, h, l, c = q["open"][i], q["high"][i], q["low"][i], q["close"][i]
        if None in (o, h, l, c):
            continue
        rows.append([dt.datetime.fromtimestamp(ts, tz).date().isoformat(), round(o, 4), round(h, 4), round(l, 4), round(c, 4)])
    return {"source": url.split("?")[0].replace("%5E", "^"), "rows": rows}


def frankfurter(start, end, base="EUR", sym="CHF"):
    url = f"https://api.frankfurter.dev/v1/{start}..{end}?base={base}&symbols={sym}"
    d = get(url)
    rows = [[k, v[sym]] for k, v in sorted(d["rates"].items())]
    return {"source": "https://api.frankfurter.dev (ECB reference rates)", "rows": rows}


def binance(symbol, start, end):
    s = int(dt.datetime(*start, tzinfo=dt.timezone.utc).timestamp() * 1000)
    e = int(dt.datetime(*end, tzinfo=dt.timezone.utc).timestamp() * 1000)
    k = get(f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1d&startTime={s}&endTime={e}&limit=1000")
    rows = [[dt.datetime.fromtimestamp(x[0] / 1000, dt.timezone.utc).date().isoformat(),
             float(x[1]), float(x[2]), float(x[3]), float(x[4])] for x in k]
    return {"source": f"https://api.binance.com/api/v3/klines ({symbol}, 1d)", "rows": rows}


DATASETS = {
    "sp500_1987": lambda: yahoo("%5EGSPC", (1987, 1, 1), (1988, 1, 31)),
    "sp500_2008": lambda: yahoo("%5EGSPC", (2006, 6, 1), (2009, 12, 31), "1wk"),
    "eurchf_2015": lambda: frankfurter("2014-11-01", "2015-03-31"),
    "sp500_2020": lambda: yahoo("%5EGSPC", (2020, 1, 1), (2020, 9, 30)),
    "sp500_2022": lambda: yahoo("%5EGSPC", (2021, 1, 1), (2023, 1, 31), "1wk"),
    "us10y_2022": lambda: yahoo("%5ETNX", (2021, 1, 1), (2023, 1, 31), "1wk"),
    "btc_2022": lambda: binance("BTCUSDT", (2022, 10, 15), (2022, 12, 15)),
    "ftt_2022": lambda: binance("FTTUSDT", (2022, 10, 15), (2022, 12, 15)),
    "kre_2023": lambda: yahoo("KRE", (2023, 2, 1), (2023, 5, 31)),
}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    today = dt.date.today().isoformat()
    for name, fn in DATASETS.items():
        d = fn()
        d["fetched"] = today
        (OUT / f"{name}.json").write_text(json.dumps(d, indent=0), encoding="utf-8")
        print(f"{name:12s} {len(d['rows']):4d} rows  {d['rows'][0][0]} .. {d['rows'][-1][0]}")
