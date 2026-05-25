from __future__ import annotations

from dataclasses import asdict
from typing import Any

from .event_detector import detect_events
from .html_text import html_to_text
from .http_client import fetch_url


def fetch_configured_pages(config: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    pages: list[dict[str, Any]] = []
    events: list[dict[str, Any]] = []
    companies = config.get("companies", {})
    for source in config.get("source_pages", []):
        ticker = source["ticker"]
        theme = companies.get(ticker, {}).get("theme", "")
        result = fetch_url(source["url"])
        title = ""
        text = ""
        if result.text:
            title, text = html_to_text(result.text)
        page_record = {
            "ticker": ticker,
            "theme": theme,
            "source_type": source.get("source_type", ""),
            "source_quality": source.get("source_quality", ""),
            "source_url": source["url"],
            "source_note": source.get("note", ""),
            "status": result.status,
            "fetched_at_utc": result.fetched_at_utc,
            "content_type": result.content_type,
            "title": title,
            "error": result.error,
            "text_length": len(text),
        }
        pages.append(page_record)
        if result.status and text:
            for event in detect_events(
                ticker=ticker,
                theme=theme,
                source_url=source["url"],
                source_type=source.get("source_type", ""),
                source_quality=source.get("source_quality", ""),
                text=text,
            ):
                event_record = asdict(event)
                event_record["fetched_at_utc"] = result.fetched_at_utc
                event_record["source_title"] = title
                events.append(event_record)
    return pages, events

