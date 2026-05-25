#!/usr/bin/env python3
"""Update price and momentum snapshot for the AI supply-chain master database."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import yfinance as yf


def load_tickers(path: Path) -> list[str]:
    with path.open() as f:
        return [r["ticker"] for r in csv.DictReader(f) if r.get("ticker")]


def price_snapshot(tickers: list[str]) -> list[dict[str, object]]:
    data = yf.download(
        tickers,
        period="6mo",
        auto_adjust=True,
        group_by="ticker",
        progress=False,
        threads=True,
    )
    rows: list[dict[str, object]] = []
    for ticker in tickers:
        try:
            is_multi = getattr(data.columns, "nlevels", 1) > 1
            close = data[ticker]["Close"].dropna() if is_multi else data["Close"].dropna()
            volume = data[ticker]["Volume"].dropna() if is_multi else data["Volume"].dropna()
            if close.empty:
                continue
            last = float(close.iloc[-1])
            row = {
                "ticker": ticker,
                "date": close.index[-1].date().isoformat(),
                "close": round(last, 4),
                "volume": int(volume.iloc[-1]) if not volume.empty else "",
                "ret_5d_%": round((last / float(close.iloc[-6]) - 1) * 100, 2) if len(close) > 5 else "",
                "ret_20d_%": round((last / float(close.iloc[-21]) - 1) * 100, 2) if len(close) > 20 else "",
                "ret_60d_%": round((last / float(close.iloc[-61]) - 1) * 100, 2) if len(close) > 60 else "",
                "dist_from_6m_high_%": round((last / float(close.max()) - 1) * 100, 2),
            }
            rows.append(row)
        except Exception:
            continue
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--master", default="company_master_database_v1_2026-05-24.csv", type=Path)
    parser.add_argument("--output", default="watchlist_price_snapshot.csv", type=Path)
    args = parser.parse_args()
    tickers = load_tickers(args.master)
    rows = price_snapshot(tickers)
    with args.output.open("w", newline="") as f:
        fieldnames = [
            "ticker",
            "date",
            "close",
            "volume",
            "ret_5d_%",
            "ret_20d_%",
            "ret_60d_%",
            "dist_from_6m_high_%",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {args.output} with {len(rows)} rows")


if __name__ == "__main__":
    main()
