from __future__ import annotations

import json
from collections import defaultdict
from datetime import date, datetime, timezone
from statistics import mean
from typing import Any
from urllib.parse import quote

from .http_client import fetch_url


YAHOO_CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?range=5d&interval=1d"


def fetch_global_market_context(items: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    today_utc = datetime.now(timezone.utc).date()
    for item in items:
        symbol = item["symbol"]
        result = fetch_url(YAHOO_CHART_URL.format(symbol=quote(symbol, safe="")))
        if result.status != 200 or not result.text:
            rows.append(error_row(item, result.fetched_at_utc, result.error or f"status={result.status}"))
            continue
        try:
            rows.append(parse_market_row(item, result.text, result.fetched_at_utc, today_utc))
        except (KeyError, IndexError, TypeError, ValueError, json.JSONDecodeError) as exc:
            rows.append(error_row(item, result.fetched_at_utc, f"parse_error={type(exc).__name__}: {exc}"))
    return rows, summarize_market_context(rows)


def parse_market_row(item: dict[str, Any], text: str, fetched_at_utc: str, today_utc: date) -> dict[str, Any]:
    payload = json.loads(text)
    result = payload["chart"]["result"][0]
    meta = result.get("meta", {})
    timestamps = result.get("timestamp") or []
    quote_data = result["indicators"]["quote"][0]
    closes = quote_data.get("close") or []
    opens = quote_data.get("open") or []
    highs = quote_data.get("high") or []
    lows = quote_data.get("low") or []
    volumes = quote_data.get("volume") or []
    valid_indices = [idx for idx, close in enumerate(closes) if close is not None]
    if not valid_indices:
        return error_row(item, fetched_at_utc, "no valid close rows")
    latest_idx = valid_indices[-1]
    previous_idx = valid_indices[-2] if len(valid_indices) >= 2 else None
    latest_ts = timestamps[latest_idx]
    market_date = datetime.fromtimestamp(latest_ts, tz=timezone.utc).date()
    close = float(closes[latest_idx])
    open_price = float(opens[latest_idx]) if opens[latest_idx] is not None else None
    previous_close = float(closes[previous_idx]) if previous_idx is not None else None
    pct_prev = pct_change(close, previous_close)
    pct_open = pct_change(close, open_price)
    freshness = "fresh_today" if market_date == today_utc else "stale"
    return {
        "name": item.get("name", ""),
        "symbol": item.get("symbol", ""),
        "region": item.get("region", ""),
        "group": item.get("group", ""),
        "theme_signal": item.get("theme_signal", ""),
        "currency": meta.get("currency", ""),
        "date": market_date.isoformat(),
        "price": round(close, 4),
        "open": round_or_blank(open_price),
        "high": round_or_blank(highs[latest_idx] if latest_idx < len(highs) else None),
        "low": round_or_blank(lows[latest_idx] if latest_idx < len(lows) else None),
        "previous_close": round_or_blank(previous_close),
        "pct_from_prev_close": round_or_blank(pct_prev),
        "pct_from_open": round_or_blank(pct_open),
        "volume": volumes[latest_idx] if latest_idx < len(volumes) and volumes[latest_idx] is not None else "",
        "freshness": freshness,
        "provider": "yahoo_chart_5d_1d",
        "fetched_at_utc": fetched_at_utc,
        "error": "",
    }


def summarize_market_context(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[row.get("group", "")].append(row)
    summaries: list[dict[str, Any]] = []
    for group, group_rows in sorted(grouped.items()):
        usable = [row for row in group_rows if not row.get("error") and row.get("pct_from_prev_close") != ""]
        fresh = [row for row in usable if row.get("freshness") == "fresh_today"]
        pct_prev_values = [float(row["pct_from_prev_close"]) for row in usable]
        pct_open_values = [float(row["pct_from_open"]) for row in usable if row.get("pct_from_open") != ""]
        avg_prev = mean(pct_prev_values) if pct_prev_values else None
        avg_open = mean(pct_open_values) if pct_open_values else None
        positives = sum(1 for row in usable if float(row["pct_from_prev_close"]) > 0)
        negatives = sum(1 for row in usable if float(row["pct_from_prev_close"]) < 0)
        region = "|".join(sorted({row.get("region", "") for row in group_rows if row.get("region")}))
        theme_signal = "|".join(sorted({row.get("theme_signal", "") for row in group_rows if row.get("theme_signal")}))
        summaries.append(
            {
                "group": group,
                "region": region,
                "theme_signal": theme_signal,
                "count": len(group_rows),
                "fresh_count": len(fresh),
                "avg_pct_from_prev_close": round_or_blank(avg_prev),
                "avg_pct_from_open": round_or_blank(avg_open),
                "positive_count": positives,
                "negative_count": negatives,
                "freshness": "fresh_today" if fresh else "stale_or_closed",
                "interpretation": interpret_group(len(fresh), avg_prev, positives, negatives),
            }
        )
    return summaries


def interpret_group(fresh_count: int, avg_pct_from_prev: float | None, positives: int, negatives: int) -> str:
    if fresh_count == 0:
        return "no_fresh_today_signal"
    if avg_pct_from_prev is None:
        return "insufficient_data"
    if avg_pct_from_prev >= 1.5 and positives >= max(1, negatives):
        return "positive_external_confirmation"
    if avg_pct_from_prev <= -1.5 and negatives >= max(1, positives):
        return "negative_external_warning"
    return "mixed_or_neutral"


def pct_change(value: float | None, reference: float | None) -> float | None:
    if value is None or reference in {None, 0}:
        return None
    return (value / reference - 1) * 100


def round_or_blank(value: Any) -> str:
    if value is None or value == "":
        return ""
    return str(round(float(value), 4))


def error_row(item: dict[str, Any], fetched_at_utc: str, error: str) -> dict[str, Any]:
    return {
        "name": item.get("name", ""),
        "symbol": item.get("symbol", ""),
        "region": item.get("region", ""),
        "group": item.get("group", ""),
        "theme_signal": item.get("theme_signal", ""),
        "currency": "",
        "date": "",
        "price": "",
        "open": "",
        "high": "",
        "low": "",
        "previous_close": "",
        "pct_from_prev_close": "",
        "pct_from_open": "",
        "volume": "",
        "freshness": "",
        "provider": "yahoo_chart_5d_1d",
        "fetched_at_utc": fetched_at_utc,
        "error": error,
    }
