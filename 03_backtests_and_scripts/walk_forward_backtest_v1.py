#!/usr/bin/env python3
"""
Walk-forward backtest for the AI supply-chain v3 decision system.

Rules:
- Use only prediction rows already defined in walk_forward_information_sets_v1.csv.
- Compute post-prediction basket returns from public market data.
- Do not score unavailable hyperscaler/private order data as a model failure.
"""

from __future__ import annotations

import csv
from datetime import timedelta
from pathlib import Path

import pandas as pd
import yfinance as yf


BASE = Path(__file__).resolve().parent
INPUT = BASE / "walk_forward_information_sets_v1.csv"
OUTPUT = BASE / "walk_forward_backtest_results_v1.csv"


def pct(a: float, b: float) -> float:
    return round((b / a - 1.0) * 100.0, 2)


def first_on_or_after(series: pd.Series, date: pd.Timestamp) -> tuple[pd.Timestamp, float] | tuple[None, None]:
    s = series.dropna()
    s = s[s.index >= date]
    if s.empty:
        return None, None
    return s.index[0], float(s.iloc[0])


def first_on_or_before(series: pd.Series, date: pd.Timestamp) -> tuple[pd.Timestamp, float] | tuple[None, None]:
    s = series.dropna()
    s = s[s.index <= date]
    if s.empty:
        return None, None
    return s.index[-1], float(s.iloc[-1])


def main() -> None:
    rows = list(csv.DictReader(INPUT.open(newline="", encoding="utf-8")))
    tickers = sorted({t for row in rows for t in row["basket_tickers"].split("|") if t})
    data = yf.download(tickers, start="2023-01-01", auto_adjust=True, progress=False)["Close"]
    if isinstance(data, pd.Series):
        data = data.to_frame(tickers[0])

    out = []
    for row in rows:
        prediction_date = pd.Timestamp(row["prediction_date"])
        basket = [t for t in row["basket_tickers"].split("|") if t in data.columns]
        basket_returns = {}
        used = {}
        for months, days in [("3m", 92), ("6m", 183), ("12m", 365)]:
            vals = []
            used_tickers = []
            for t in basket:
                series = data[t]
                start_dt, start_px = first_on_or_after(series, prediction_date)
                end_dt, end_px = first_on_or_before(series, prediction_date + timedelta(days=days))
                if start_px and end_px:
                    vals.append(pct(start_px, end_px))
                    used_tickers.append(t)
            basket_returns[months] = round(sum(vals) / len(vals), 2) if vals else ""
            used[months] = "|".join(used_tickers)

        score = float(row["model_score_at_time"])
        confidence = float(row["confidence_at_time"])
        result_6m = basket_returns["6m"]
        if result_6m == "":
            forecast_error_reason = "insufficient_price_history"
        elif score >= 70 and result_6m < 0:
            forecast_error_reason = "public_signal_failed"
        elif confidence <= 50 and result_6m > 20:
            forecast_error_reason = "blind_spot_or_unobservable_demand_likely"
        else:
            forecast_error_reason = "public_signal_reasonably_matched"

        out.append(
            {
                "ticker": row["ticker"],
                "date": "2026-05-25",
                "source": "yfinance adjusted close plus v3 information set",
                "source_url": "walk_forward_information_sets_v1.csv",
                "source_type": "market_data_and_internal_model",
                "reliability_score": "0.70",
                "prediction_date": row["prediction_date"],
                "theme": row["theme"],
                "available_information": row["available_information"],
                "unavailable_information": row["unavailable_information"],
                "model_score_at_time": row["model_score_at_time"],
                "confidence_at_time": row["confidence_at_time"],
                "actual_result_3m": basket_returns["3m"],
                "actual_result_6m": basket_returns["6m"],
                "actual_result_12m": basket_returns["12m"],
                "used_tickers_3m": used["3m"],
                "used_tickers_6m": used["6m"],
                "used_tickers_12m": used["12m"],
                "forecast_error_reason": forecast_error_reason,
                "unobservable_data_flag": row["unobservable_data_flag"],
            }
        )

    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        writer.writeheader()
        writer.writerows(out)
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
