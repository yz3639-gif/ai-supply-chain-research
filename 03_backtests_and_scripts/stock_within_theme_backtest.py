#!/usr/bin/env python3
"""Ticker-level backtest inside predefined AI bottleneck theme baskets."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import pandas as pd
import yfinance as yf


HORIZONS = [20, 60, 120, 252]


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
        try:
            if isinstance(data.columns, pd.MultiIndex):
                closes[symbol] = data[symbol]["Close"].dropna()
            else:
                closes[symbol] = data["Close"].dropna()
        except Exception:
            continue
    return pd.DataFrame(closes).sort_index()


def pct(start: float, end: float) -> float:
    return (end / start - 1.0) * 100.0


def first_trading_index(index: pd.DatetimeIndex, date: pd.Timestamp) -> int | None:
    loc = index.searchsorted(date)
    if loc >= len(index):
        return None
    return int(loc)


def run(events_path: Path, event_output: Path, summary_output: Path) -> None:
    events = pd.read_csv(events_path, parse_dates=["node_date"])
    symbols = {"QQQ", "SMH"}
    for tickers in events["basket_tickers"]:
        symbols.update([x.strip() for x in str(tickers).split("|") if x.strip()])
    start = (events["node_date"].min() - pd.Timedelta(days=40)).strftime("%Y-%m-%d")
    end = (pd.Timestamp.today() + pd.Timedelta(days=3)).strftime("%Y-%m-%d")
    prices = load_prices(sorted(symbols), start, end)

    rows: list[dict[str, object]] = []
    for _, event in events.iterrows():
        event_idx = first_trading_index(prices.index, event["node_date"])
        if event_idx is None or event_idx == 0:
            continue
        prev_idx = event_idx - 1
        tickers = [x.strip() for x in str(event["basket_tickers"]).split("|") if x.strip()]
        for ticker in tickers:
            if ticker not in prices:
                continue
            row: dict[str, object] = {
                "node_date": event["node_date"].date().isoformat(),
                "trade_date": prices.index[event_idx].date().isoformat(),
                "node_id": event["node_id"],
                "theme": event["theme"],
                "ticker": ticker,
                "node_type": event["node_type"],
                "trigger": event["trigger"],
            }
            for horizon in HORIZONS:
                end_idx = min(event_idx + horizon, len(prices.index) - 1)
                actual_days = end_idx - event_idx
                row[f"actual_days_{horizon}d"] = actual_days
                start_px = prices[ticker].iloc[prev_idx]
                end_px = prices[ticker].iloc[end_idx]
                q_start = prices["QQQ"].iloc[prev_idx]
                q_end = prices["QQQ"].iloc[end_idx]
                s_start = prices["SMH"].iloc[prev_idx]
                s_end = prices["SMH"].iloc[end_idx]
                if any(pd.isna(x) or x <= 0 for x in [start_px, end_px, q_start, q_end, s_start, s_end]):
                    row[f"ret_{horizon}d_%"] = ""
                    row[f"xQQQ_{horizon}d_%"] = ""
                    row[f"xSMH_{horizon}d_%"] = ""
                    continue
                stock_ret = pct(float(start_px), float(end_px))
                row[f"ret_{horizon}d_%"] = round(stock_ret, 2)
                row[f"xQQQ_{horizon}d_%"] = round(stock_ret - pct(float(q_start), float(q_end)), 2)
                row[f"xSMH_{horizon}d_%"] = round(stock_ret - pct(float(s_start), float(s_end)), 2)
            rows.append(row)

    detail = pd.DataFrame(rows)
    detail.to_csv(event_output, index=False, quoting=csv.QUOTE_MINIMAL)

    summary_rows: list[dict[str, object]] = []
    for (theme, ticker), group in detail.groupby(["theme", "ticker"]):
        row: dict[str, object] = {"theme": theme, "ticker": ticker, "appearances": len(group)}
        for horizon in HORIZONS:
            sub = group[group[f"actual_days_{horizon}d"] >= horizon]
            for col, label in [
                (f"ret_{horizon}d_%", "abs"),
                (f"xQQQ_{horizon}d_%", "xqqq"),
                (f"xSMH_{horizon}d_%", "xsmh"),
            ]:
                vals = pd.to_numeric(sub[col], errors="coerce").dropna()
                row[f"{label}_median_{horizon}d_%"] = round(float(vals.median()), 2) if len(vals) else ""
                row[f"{label}_hit_rate_{horizon}d"] = round(float((vals > 0).mean()), 3) if len(vals) else ""
                row[f"{label}_n_{horizon}d"] = int(len(vals))
        summary_rows.append(row)
    pd.DataFrame(summary_rows).sort_values(["theme", "ticker"]).to_csv(summary_output, index=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--events", required=True, type=Path)
    parser.add_argument("--event-output", required=True, type=Path)
    parser.add_argument("--summary-output", required=True, type=Path)
    args = parser.parse_args()
    run(args.events, args.event_output, args.summary_output)


if __name__ == "__main__":
    main()
