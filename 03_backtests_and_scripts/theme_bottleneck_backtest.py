#!/usr/bin/env python3
"""Theme-level event backtest for AI supply-chain bottleneck migration.

The script intentionally uses simple equal-weight baskets and benchmark-relative
returns. It is not an optimizer; it is a sanity check against narrative overfit.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import yfinance as yf


HORIZONS = [20, 60, 120, 252]


@dataclass(frozen=True)
class Event:
    node_date: pd.Timestamp
    node_id: str
    theme: str
    node_type: str
    trigger: str
    tickers: list[str]
    primary_benchmark: str
    secondary_benchmark: str
    source_url: str
    thesis: str


def load_events(path: Path) -> list[Event]:
    df = pd.read_csv(path, parse_dates=["node_date"])
    events: list[Event] = []
    for _, row in df.iterrows():
        tickers = [x.strip() for x in str(row["basket_tickers"]).split("|") if x.strip()]
        events.append(
            Event(
                node_date=row["node_date"],
                node_id=row["node_id"],
                theme=row["theme"],
                node_type=row["node_type"],
                trigger=row["trigger"],
                tickers=tickers,
                primary_benchmark=row["primary_benchmark"],
                secondary_benchmark=row["secondary_benchmark"],
                source_url=row["source_url"],
                thesis=row["predefined_thesis"],
            )
        )
    return events


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
    closes: dict[str, pd.Series] = {}
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


def basket_return(
    prices: pd.DataFrame,
    tickers: list[str],
    prev_idx: int,
    end_idx: int,
) -> tuple[float | None, int, str]:
    returns: list[float] = []
    used: list[str] = []
    for ticker in tickers:
        if ticker not in prices:
            continue
        start = prices[ticker].iloc[prev_idx]
        end = prices[ticker].iloc[end_idx]
        if pd.isna(start) or pd.isna(end) or start <= 0:
            continue
        returns.append(pct(float(start), float(end)))
        used.append(ticker)
    if not returns:
        return None, 0, ""
    return float(sum(returns) / len(returns)), len(returns), "|".join(used)


def run(events_path: Path, event_output: Path, summary_output: Path) -> None:
    events = load_events(events_path)
    symbols = sorted(
        {
            ticker
            for event in events
            for ticker in event.tickers + [event.primary_benchmark, event.secondary_benchmark]
        }
    )
    start = (min(event.node_date for event in events) - pd.Timedelta(days=40)).strftime("%Y-%m-%d")
    end = (pd.Timestamp.today() + pd.Timedelta(days=3)).strftime("%Y-%m-%d")
    prices = load_prices(symbols, start, end)

    rows: list[dict[str, object]] = []
    for event in events:
        event_idx = first_trading_index(prices.index, event.node_date)
        if event_idx is None or event_idx == 0:
            continue
        prev_idx = event_idx - 1
        base: dict[str, object] = {
            "node_date": event.node_date.date().isoformat(),
            "trade_date": prices.index[event_idx].date().isoformat(),
            "node_id": event.node_id,
            "theme": event.theme,
            "node_type": event.node_type,
            "trigger": event.trigger,
            "source_url": event.source_url,
            "thesis": event.thesis,
        }
        for horizon in HORIZONS:
            end_idx = min(event_idx + horizon, len(prices.index) - 1)
            actual_days = end_idx - event_idx
            basket_ret, used_count, used_tickers = basket_return(prices, event.tickers, prev_idx, end_idx)
            primary_ret, _, _ = basket_return(prices, [event.primary_benchmark], prev_idx, end_idx)
            secondary_ret, _, _ = basket_return(prices, [event.secondary_benchmark], prev_idx, end_idx)
            if basket_ret is None or primary_ret is None or secondary_ret is None:
                base[f"basket_ret_{horizon}d_%"] = ""
                base[f"x{event.primary_benchmark}_{horizon}d_%"] = ""
                base[f"x{event.secondary_benchmark}_{horizon}d_%"] = ""
            else:
                base[f"basket_ret_{horizon}d_%"] = round(basket_ret, 2)
                base[f"x{event.primary_benchmark}_{horizon}d_%"] = round(basket_ret - primary_ret, 2)
                base[f"x{event.secondary_benchmark}_{horizon}d_%"] = round(basket_ret - secondary_ret, 2)
            base[f"actual_days_{horizon}d"] = actual_days
            base[f"used_count_{horizon}d"] = used_count
            base[f"used_tickers_{horizon}d"] = used_tickers
        rows.append(base)

    event_df = pd.DataFrame(rows)
    event_df.to_csv(event_output, index=False, quoting=csv.QUOTE_MINIMAL)

    summary_rows: list[dict[str, object]] = []
    for theme, group in event_df.groupby("theme"):
        row: dict[str, object] = {"theme": theme, "events": len(group)}
        for horizon in HORIZONS:
            q_col = f"xQQQ_{horizon}d_%"
            s_col = f"xSMH_{horizon}d_%"
            b_col = f"basket_ret_{horizon}d_%"
            enough_col = f"actual_days_{horizon}d"
            sub = group[group[enough_col] >= horizon]
            for col, label in [(b_col, "abs"), (q_col, "xqqq"), (s_col, "xsmh")]:
                vals = pd.to_numeric(sub[col], errors="coerce").dropna()
                row[f"{label}_median_{horizon}d_%"] = round(float(vals.median()), 2) if len(vals) else ""
                row[f"{label}_mean_{horizon}d_%"] = round(float(vals.mean()), 2) if len(vals) else ""
                row[f"{label}_hit_rate_{horizon}d"] = round(float((vals > 0).mean()), 3) if len(vals) else ""
                row[f"{label}_n_{horizon}d"] = int(len(vals))
        summary_rows.append(row)
    pd.DataFrame(summary_rows).sort_values("theme").to_csv(summary_output, index=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--events", required=True, type=Path)
    parser.add_argument("--event-output", required=True, type=Path)
    parser.add_argument("--summary-output", required=True, type=Path)
    args = parser.parse_args()
    run(args.events, args.event_output, args.summary_output)


if __name__ == "__main__":
    main()
