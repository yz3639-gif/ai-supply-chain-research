#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

if __package__ in {None, ""}:
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from realtime_data_pipeline.pipeline.fetch_prices import fetch_stooq_prices
from realtime_data_pipeline.pipeline.fetch_sec import fetch_sec_filings
from realtime_data_pipeline.pipeline.fetch_sources import fetch_configured_pages
from realtime_data_pipeline.pipeline.global_markets import fetch_global_market_context
from realtime_data_pipeline.pipeline.io_utils import read_json, write_csv, write_jsonl
from realtime_data_pipeline.pipeline.report import build_markdown_report, write_report
from realtime_data_pipeline.pipeline.technical_indicators import fetch_technical_indicators


BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "config" / "data_sources.json"
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
REPORT_DIR = BASE_DIR / "reports"


EVENT_FIELDS = [
    "event_id",
    "ticker",
    "theme",
    "category",
    "source_quality",
    "source_type",
    "model_action",
    "decision_route",
    "matched_terms",
    "snippet",
    "source_title",
    "source_url",
    "fetched_at_utc",
]

PAGE_FIELDS = [
    "ticker",
    "theme",
    "source_type",
    "source_quality",
    "source_url",
    "source_note",
    "status",
    "fetched_at_utc",
    "content_type",
    "title",
    "error",
    "text_length",
]

FILING_FIELDS = [
    "ticker",
    "cik",
    "company_name",
    "form",
    "filing_date",
    "accession_number",
    "filing_url",
    "fetched_at_utc",
    "error",
]

PRICE_FIELDS = [
    "ticker",
    "date",
    "time",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "provider",
    "fetched_at_utc",
    "error",
]

TECHNICAL_FIELDS = [
    "ticker",
    "date",
    "close",
    "ema20",
    "ema50",
    "ema200",
    "boll20_mid",
    "boll20_upper",
    "boll20_lower",
    "boll20_percent_b",
    "boll20_bandwidth",
    "close_vs_ema20_pct",
    "close_vs_ema50_pct",
    "close_vs_ema200_pct",
    "trend_state",
    "history_points",
    "provider",
    "fetched_at_utc",
    "error",
]

GLOBAL_MARKET_FIELDS = [
    "name",
    "symbol",
    "region",
    "group",
    "theme_signal",
    "currency",
    "date",
    "price",
    "open",
    "high",
    "low",
    "previous_close",
    "pct_from_prev_close",
    "pct_from_open",
    "volume",
    "freshness",
    "provider",
    "fetched_at_utc",
    "error",
]

GLOBAL_SUMMARY_FIELDS = [
    "group",
    "region",
    "theme_signal",
    "count",
    "fresh_count",
    "avg_pct_from_prev_close",
    "avg_pct_from_open",
    "positive_count",
    "negative_count",
    "freshness",
    "interpretation",
]


def main() -> int:
    args = parse_args()
    if args.loop_seconds and args.loop_seconds < 30:
        print("Refusing loop intervals below 30 seconds. Use 60 seconds for the requested minute cadence.")
        return 2
    run_count = 0
    while True:
        run_count += 1
        try:
            run_once(args)
        except Exception as exc:  # noqa: BLE001 - keep long-running watcher alive.
            print(f"[pipeline-error] {datetime.now().isoformat(timespec='seconds')} {type(exc).__name__}: {exc}", file=sys.stderr)
        if not args.loop_seconds:
            break
        if args.max_runs and run_count >= args.max_runs:
            break
        time.sleep(args.loop_seconds)
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch public AI supply-chain data into the model ingest layer.")
    parser.add_argument("--config", type=Path, default=CONFIG_PATH, help="Path to data_sources.json")
    parser.add_argument("--loop-seconds", type=int, default=0, help="Run continuously at this cadence; use 60 for every minute.")
    parser.add_argument("--max-runs", type=int, default=0, help="Optional cap for test loops.")
    parser.add_argument("--skip-sec", action="store_true", help="Skip SEC submissions fetch.")
    parser.add_argument(
        "--sec-min-interval-seconds",
        type=int,
        default=3600,
        help="Do not refetch SEC submissions if latest SEC file is newer than this many seconds.",
    )
    parser.add_argument("--skip-prices", action="store_true", help="Skip Stooq price fetch.")
    parser.add_argument("--skip-technicals", action="store_true", help="Skip EMA/BOLL indicator fetch.")
    parser.add_argument("--skip-global-markets", action="store_true", help="Skip non-US/global market context fetch.")
    parser.add_argument("--source-limit", type=int, default=0, help="Fetch only the first N configured source pages.")
    return parser.parse_args()


def run_once(args: argparse.Namespace) -> None:
    config = read_json(args.config)
    if args.source_limit:
        config = {**config, "source_pages": config.get("source_pages", [])[: args.source_limit]}
    run_id = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    print(f"[pipeline] run_id={run_id} start")

    pages, events = fetch_configured_pages(config)
    enrich_events(events)

    tickers = config.get("tickers", [])
    if args.skip_sec:
        filings = read_existing_csv(PROCESSED_DIR / "sec_filings_latest.csv")
    else:
        if should_fetch_sec(args.sec_min_interval_seconds):
            filings = fetch_sec_filings(tickers)
        else:
            filings = read_existing_csv(PROCESSED_DIR / "sec_filings_latest.csv")
    if args.skip_prices:
        prices = read_existing_csv(PROCESSED_DIR / "prices_latest.csv")
    else:
        provider = config.get("price_provider", {})
        prices = fetch_stooq_prices(tickers, provider.get("url_template", ""))
    if args.skip_technicals:
        technicals = read_existing_csv(PROCESSED_DIR / "technical_indicators_latest.csv")
    else:
        technicals = fetch_technical_indicators(tickers)
    if args.skip_global_markets:
        global_markets = read_existing_csv(PROCESSED_DIR / "global_market_context_latest.csv")
        global_summary = read_existing_csv(PROCESSED_DIR / "global_market_theme_summary_latest.csv")
    else:
        global_markets, global_summary = fetch_global_market_context(config.get("global_markets", []))

    write_outputs(run_id, pages, events, filings, prices, technicals, global_markets, global_summary)
    print(
        f"[pipeline] run_id={run_id} pages={len(pages)} events={len(events)} "
        f"filings={len(filings)} prices={len(prices)} technicals={len(technicals)} "
        f"global_markets={len(global_markets)} done"
    )


def enrich_events(events: list[dict[str, Any]]) -> None:
    for event in events:
        event["event_id"] = event_id(event)
        event["decision_route"] = decision_route(event)


def event_id(event: dict[str, Any]) -> str:
    key = "|".join(
        [
            str(event.get("ticker", "")),
            str(event.get("category", "")),
            str(event.get("source_url", "")),
            str(event.get("matched_terms", "")),
            str(event.get("snippet", ""))[:240],
        ]
    )
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def decision_route(event: dict[str, Any]) -> str:
    action = event.get("model_action", "")
    quality = event.get("source_quality", "")
    if action == "eligible_for_event_ledger_review" and quality == "A":
        return "event_ledger_review_after_no_trade_check"
    if quality in {"A", "B"}:
        return "pre_confirmation_signal_log"
    return "research_only"


def write_outputs(
    run_id: str,
    pages: list[dict[str, Any]],
    events: list[dict[str, Any]],
    filings: list[dict[str, Any]],
    prices: list[dict[str, Any]],
    technicals: list[dict[str, Any]],
    global_markets: list[dict[str, Any]],
    global_summary: list[dict[str, Any]],
) -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    write_jsonl(RAW_DIR / f"source_pages_{run_id}.jsonl", pages)
    write_jsonl(RAW_DIR / f"events_{run_id}.jsonl", events)
    write_jsonl(RAW_DIR / f"filings_{run_id}.jsonl", filings)
    write_jsonl(RAW_DIR / f"prices_{run_id}.jsonl", prices)
    write_jsonl(RAW_DIR / f"technicals_{run_id}.jsonl", technicals)
    write_jsonl(RAW_DIR / f"global_markets_{run_id}.jsonl", global_markets)
    write_jsonl(RAW_DIR / f"global_market_summary_{run_id}.jsonl", global_summary)

    write_csv(PROCESSED_DIR / "source_pages_latest.csv", pages, PAGE_FIELDS)
    write_csv(PROCESSED_DIR / "events_latest.csv", events, EVENT_FIELDS)
    write_csv(PROCESSED_DIR / "model_ingest_latest.csv", events, EVENT_FIELDS)
    write_csv(PROCESSED_DIR / "sec_filings_latest.csv", filings, FILING_FIELDS)
    write_csv(PROCESSED_DIR / "prices_latest.csv", prices, PRICE_FIELDS)
    write_csv(PROCESSED_DIR / "technical_indicators_latest.csv", technicals, TECHNICAL_FIELDS)
    write_csv(PROCESSED_DIR / "global_market_context_latest.csv", global_markets, GLOBAL_MARKET_FIELDS)
    write_csv(PROCESSED_DIR / "global_market_theme_summary_latest.csv", global_summary, GLOBAL_SUMMARY_FIELDS)
    update_event_history(PROCESSED_DIR / "events_history.csv", events)

    report = build_markdown_report(
        run_id=run_id,
        pages=pages,
        events=events,
        filings=filings,
        prices=prices,
        technicals=technicals,
        global_markets=global_markets,
        global_summary=global_summary,
    )
    write_report(REPORT_DIR / "realtime_snapshot_latest.md", report)
    write_report(REPORT_DIR / f"realtime_snapshot_{run_id}.md", report)


def should_fetch_sec(min_interval_seconds: int) -> bool:
    latest = PROCESSED_DIR / "sec_filings_latest.csv"
    if min_interval_seconds <= 0 or not latest.exists():
        return True
    if len(read_existing_csv(latest)) == 0:
        return True
    age = time.time() - latest.stat().st_mtime
    return age >= min_interval_seconds


def read_existing_csv(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def update_event_history(path: Path, events: list[dict[str, Any]]) -> None:
    existing_rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    if path.exists():
        with path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                existing_rows.append(row)
                if row.get("event_id"):
                    seen.add(row["event_id"])
    new_rows = [row for row in events if row.get("event_id") not in seen]
    if not new_rows and path.exists():
        return
    combined = existing_rows + [{field: row.get(field, "") for field in EVENT_FIELDS} for row in new_rows]
    write_csv(path, combined, EVENT_FIELDS)


if __name__ == "__main__":
    raise SystemExit(main())
