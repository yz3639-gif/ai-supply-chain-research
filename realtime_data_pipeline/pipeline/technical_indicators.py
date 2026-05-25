from __future__ import annotations

import json
from datetime import datetime, timezone
from math import sqrt
from typing import Any
from urllib.parse import quote

from .http_client import fetch_url


YAHOO_CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range=1y&interval=1d"


def fetch_technical_indicators(tickers: list[str]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for ticker in tickers:
        result = fetch_url(YAHOO_CHART_URL.format(symbol=quote(ticker)))
        if result.status != 200 or not result.text:
            records.append(error_record(ticker, result.fetched_at_utc, result.error or f"status={result.status}"))
            continue
        try:
            timestamps, closes = parse_yahoo_chart(result.text)
        except (KeyError, IndexError, TypeError, ValueError, json.JSONDecodeError) as exc:
            records.append(error_record(ticker, result.fetched_at_utc, f"parse_error={type(exc).__name__}: {exc}"))
            continue
        valid = [(ts, close) for ts, close in zip(timestamps, closes, strict=False) if close is not None]
        if len(valid) < 20:
            records.append(error_record(ticker, result.fetched_at_utc, "insufficient history for BOLL20"))
            continue
        latest_ts, latest_close = valid[-1]
        close_values = [float(close) for _, close in valid]
        boll = bollinger(close_values, window=20, stdevs=2.0)
        ema20 = ema(close_values, 20)
        ema50 = ema(close_values, 50)
        ema200 = ema(close_values, 200)
        upper = boll["upper"]
        lower = boll["lower"]
        middle = boll["middle"]
        percent_b = ""
        if upper is not None and lower is not None and upper != lower:
            percent_b = (latest_close - lower) / (upper - lower)
        trend_state = classify_trend(latest_close, ema20, ema50, ema200)
        records.append(
            {
                "ticker": ticker,
                "date": datetime.fromtimestamp(latest_ts, tz=timezone.utc).strftime("%Y-%m-%d"),
                "close": round(latest_close, 4),
                "ema20": round_or_blank(ema20),
                "ema50": round_or_blank(ema50),
                "ema200": round_or_blank(ema200),
                "boll20_mid": round_or_blank(middle),
                "boll20_upper": round_or_blank(upper),
                "boll20_lower": round_or_blank(lower),
                "boll20_percent_b": round_or_blank(percent_b),
                "boll20_bandwidth": round_or_blank(boll["bandwidth"]),
                "close_vs_ema20_pct": pct_diff(latest_close, ema20),
                "close_vs_ema50_pct": pct_diff(latest_close, ema50),
                "close_vs_ema200_pct": pct_diff(latest_close, ema200),
                "trend_state": trend_state,
                "history_points": len(valid),
                "provider": "yahoo_chart_1y_1d",
                "fetched_at_utc": result.fetched_at_utc,
                "error": "",
            }
        )
    return records


def parse_yahoo_chart(text: str) -> tuple[list[int], list[float | None]]:
    payload = json.loads(text)
    result = payload["chart"]["result"][0]
    timestamps = result.get("timestamp") or []
    closes = result["indicators"]["quote"][0]["close"]
    return timestamps, closes


def ema(values: list[float], span: int) -> float | None:
    if not values:
        return None
    alpha = 2 / (span + 1)
    current = values[0]
    for value in values[1:]:
        current = alpha * value + (1 - alpha) * current
    return current


def bollinger(values: list[float], window: int = 20, stdevs: float = 2.0) -> dict[str, float | None]:
    if len(values) < window:
        return {"middle": None, "upper": None, "lower": None, "bandwidth": None}
    sample = values[-window:]
    middle = sum(sample) / window
    variance = sum((value - middle) ** 2 for value in sample) / window
    std = sqrt(variance)
    upper = middle + stdevs * std
    lower = middle - stdevs * std
    bandwidth = (upper - lower) / middle if middle else None
    return {"middle": middle, "upper": upper, "lower": lower, "bandwidth": bandwidth}


def pct_diff(value: float, reference: float | None) -> str:
    if reference in {None, 0}:
        return ""
    return str(round((value / reference - 1) * 100, 4))


def round_or_blank(value: Any) -> str:
    if value is None or value == "":
        return ""
    return str(round(float(value), 4))


def classify_trend(close: float, ema20_value: float | None, ema50_value: float | None, ema200_value: float | None) -> str:
    if ema20_value is None or ema50_value is None or ema200_value is None:
        return "insufficient_history"
    if close > ema20_value > ema50_value > ema200_value:
        return "strong_uptrend"
    if close > ema20_value and ema20_value > ema50_value:
        return "uptrend"
    if close < ema20_value < ema50_value < ema200_value:
        return "strong_downtrend"
    if close < ema20_value and ema20_value < ema50_value:
        return "downtrend"
    return "mixed"


def error_record(ticker: str, fetched_at_utc: str, error: str) -> dict[str, Any]:
    return {
        "ticker": ticker,
        "date": "",
        "close": "",
        "ema20": "",
        "ema50": "",
        "ema200": "",
        "boll20_mid": "",
        "boll20_upper": "",
        "boll20_lower": "",
        "boll20_percent_b": "",
        "boll20_bandwidth": "",
        "close_vs_ema20_pct": "",
        "close_vs_ema50_pct": "",
        "close_vs_ema200_pct": "",
        "trend_state": "",
        "history_points": "",
        "provider": "yahoo_chart_1y_1d",
        "fetched_at_utc": fetched_at_utc,
        "error": error,
    }
