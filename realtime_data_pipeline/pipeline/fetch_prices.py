from __future__ import annotations

import csv
from io import StringIO
from typing import Any

from .http_client import fetch_url


def fetch_stooq_prices(tickers: list[str], url_template: str) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for ticker in tickers:
        symbol = ticker.lower()
        result = fetch_url(url_template.format(symbol=symbol))
        if result.status != 200 or not result.text:
            records.append(
                {
                    "ticker": ticker,
                    "date": "",
                    "time": "",
                    "close": "",
                    "volume": "",
                    "provider": "stooq_quote_csv",
                    "fetched_at_utc": result.fetched_at_utc,
                    "error": result.error or f"status={result.status}",
                }
            )
            continue
        rows = list(csv.DictReader(StringIO(result.text)))
        valid = [row for row in rows if row.get("Close") not in {"", "null", None}]
        if not valid:
            records.append(
                {
                    "ticker": ticker,
                    "date": "",
                    "time": "",
                    "close": "",
                    "volume": "",
                    "provider": "stooq_quote_csv",
                    "fetched_at_utc": result.fetched_at_utc,
                    "error": "no price rows returned",
                }
            )
            continue
        latest = valid[-1]
        records.append(
            {
                "ticker": ticker,
                "date": latest.get("Date", ""),
                "time": latest.get("Time", ""),
                "open": latest.get("Open", ""),
                "high": latest.get("High", ""),
                "low": latest.get("Low", ""),
                "close": latest.get("Close", ""),
                "volume": latest.get("Volume", ""),
                "provider": "stooq_quote_csv",
                "fetched_at_utc": result.fetched_at_utc,
                "error": "",
            }
        )
    return records
