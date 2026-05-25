#!/usr/bin/env python3
"""Small event-study helper for AI supply-chain catalyst tracking."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import pandas as pd
import yfinance as yf


def _pct(a: float, b: float) -> float:
    return (b / a - 1.0) * 100.0


def load_prices(symbols: list[str], start: str, end: str) -> pd.DataFrame:
    data = yf.download(
        symbols,
        start=start,
        end=end,
        auto_adjust=True,
        progress=False,
        group_by="ticker",
        threads=True,
    )
    closes = {}
    for symbol in symbols:
        if isinstance(data.columns, pd.MultiIndex):
            closes[symbol] = data[symbol]["Close"].dropna()
        else:
            closes[symbol] = data["Close"].dropna()
    return pd.DataFrame(closes).sort_index()


def first_trading_index(index: pd.DatetimeIndex, date: pd.Timestamp) -> int | None:
    loc = index.searchsorted(date)
    if loc >= len(index):
        return None
    return int(loc)


def run(events_path: Path, output_path: Path) -> None:
    events = pd.read_csv(events_path, parse_dates=["event_date"])
    symbols = sorted(set(events["ticker"]).union({"QQQ", "SMH"}))
    start = (events["event_date"].min() - pd.Timedelta(days=30)).strftime("%Y-%m-%d")
    end = (pd.Timestamp.today() + pd.Timedelta(days=2)).strftime("%Y-%m-%d")
    prices = load_prices(symbols, start, end)

    rows: list[dict[str, object]] = []
    horizons = [1, 5, 20, 60]
    for _, event in events.iterrows():
        ticker = event["ticker"]
        idx = first_trading_index(prices.index, event["event_date"])
        if idx is None or idx == 0 or ticker not in prices:
            continue
        event_idx = idx
        prev_idx = idx - 1
        row: dict[str, object] = {
            "event_date": event["event_date"].date().isoformat(),
            "trade_date": prices.index[event_idx].date().isoformat(),
            "ticker": ticker,
            "event_type": event["event_type"],
            "event_name": event["event_name"],
        }
        for h in horizons:
            end_idx = min(event_idx + h, len(prices.index) - 1)
            if pd.isna(prices[ticker].iloc[prev_idx]) or pd.isna(prices[ticker].iloc[end_idx]):
                row[f"ret_{h}d_%"] = ""
                row[f"xqqq_{h}d_%"] = ""
                row[f"xsmh_{h}d_%"] = ""
                continue
            ticker_ret = _pct(prices[ticker].iloc[prev_idx], prices[ticker].iloc[end_idx])
            qqq_ret = _pct(prices["QQQ"].iloc[prev_idx], prices["QQQ"].iloc[end_idx])
            smh_ret = _pct(prices["SMH"].iloc[prev_idx], prices["SMH"].iloc[end_idx])
            row[f"ret_{h}d_%"] = round(ticker_ret, 2)
            row[f"xqqq_{h}d_%"] = round(ticker_ret - qqq_ret, 2)
            row[f"xsmh_{h}d_%"] = round(ticker_ret - smh_ret, 2)
        rows.append(row)

    with output_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [])
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--events", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    run(args.events, args.output)


if __name__ == "__main__":
    main()

