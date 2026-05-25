from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


def build_markdown_report(
    *,
    run_id: str,
    pages: list[dict[str, Any]],
    events: list[dict[str, Any]],
    filings: list[dict[str, Any]],
    prices: list[dict[str, Any]],
    technicals: list[dict[str, Any]] | None = None,
    global_markets: list[dict[str, Any]] | None = None,
    global_summary: list[dict[str, Any]] | None = None,
) -> str:
    technicals = technicals or []
    global_markets = global_markets or []
    global_summary = global_summary or []
    event_counts = Counter(event.get("category", "") for event in events)
    failed_pages = [page for page in pages if page.get("error") or page.get("status") not in {200, 201, 202}]
    report = [
        "# Realtime Pipeline Snapshot",
        "",
        f"run_id: `{run_id}`",
        f"generated_at: `{datetime.now().isoformat(timespec='seconds')}`",
        "",
        "## Summary",
        "",
        f"- Source pages fetched: {len(pages)}",
        f"- Detected signal rows: {len(events)}",
        f"- SEC filing rows: {len(filings)}",
        f"- Price rows: {len(prices)}",
        f"- Technical indicator rows: {len(technicals)}",
        f"- Global market rows: {len(global_markets)}",
        f"- Failed source pages: {len(failed_pages)}",
        "",
        "## Event Categories",
        "",
    ]
    if event_counts:
        for category, count in event_counts.most_common():
            report.append(f"- `{category}`: {count}")
    else:
        report.append("- No events detected")
    report.extend(["", "## Latest Prices", ""])
    report.append("| ticker | date | close | volume | error |")
    report.append("|---|---:|---:|---:|---|")
    for row in prices:
        report.append(
            f"| {row.get('ticker','')} | {row.get('date','')} | {row.get('close','')} | "
            f"{row.get('volume','')} | {row.get('error','')} |"
        )
    report.extend(["", "## EMA / BOLL", ""])
    report.append("| ticker | date | close | EMA20 | EMA50 | EMA200 | BOLL% b | BOLL bandwidth | trend | error |")
    report.append("|---|---:|---:|---:|---:|---:|---:|---:|---|---|")
    for row in technicals:
        report.append(
            f"| {row.get('ticker','')} | {row.get('date','')} | {row.get('close','')} | "
            f"{row.get('ema20','')} | {row.get('ema50','')} | {row.get('ema200','')} | "
            f"{row.get('boll20_percent_b','')} | {row.get('boll20_bandwidth','')} | "
            f"{row.get('trend_state','')} | {row.get('error','')} |"
        )
    report.extend(["", "## Global Market Context", ""])
    if global_summary:
        report.append("| group | region | theme | fresh | avg prev % | avg open % | interpretation |")
        report.append("|---|---|---|---:|---:|---:|---|")
        for row in global_summary:
            report.append(
                f"| {row.get('group','')} | {row.get('region','')} | {row.get('theme_signal','')} | "
                f"{row.get('fresh_count','')}/{row.get('count','')} | {row.get('avg_pct_from_prev_close','')} | "
                f"{row.get('avg_pct_from_open','')} | {row.get('interpretation','')} |"
            )
    else:
        report.append("- No global market context rows.")
    report.extend(["", "### Global Market Detail", ""])
    report.append("| name | symbol | region | date | price | prev % | open % | freshness |")
    report.append("|---|---|---|---:|---:|---:|---:|---|")
    for row in global_markets[:40]:
        report.append(
            f"| {row.get('name','')} | {row.get('symbol','')} | {row.get('region','')} | "
            f"{row.get('date','')} | {row.get('price','')} | {row.get('pct_from_prev_close','')} | "
            f"{row.get('pct_from_open','')} | {row.get('freshness','') or row.get('error','')} |"
        )
    report.extend(["", "## High-Quality Signals", ""])
    high_quality = [event for event in events if event.get("source_quality") == "A"]
    if not high_quality:
        report.append("- No A-quality signal rows detected in this run.")
    for event in high_quality[:25]:
        snippet = str(event.get("snippet", "")).replace("|", "/")
        if len(snippet) > 240:
            snippet = snippet[:237] + "..."
        report.append(
            f"- `{event.get('ticker')}` `{event.get('category')}` "
            f"`{event.get('model_action')}`: {snippet} "
            f"([source]({event.get('source_url')}))"
        )
    report.extend(["", "## Recent SEC Filings", ""])
    material_forms = [row for row in filings if row.get("form") in {"8-K", "10-Q", "10-K", "6-K", "20-F"}]
    if not material_forms:
        report.append("- No material filing rows available.")
    for row in material_forms[:30]:
        url = row.get("filing_url", "")
        link = f" [filing]({url})" if url else ""
        report.append(
            f"- `{row.get('ticker')}` {row.get('form')} filed {row.get('filing_date')}{link}"
        )
    if failed_pages:
        report.extend(["", "## Fetch Errors", ""])
        for page in failed_pages:
            report.append(f"- `{page.get('ticker')}` {page.get('status')} {page.get('error')} {page.get('source_url')}")
    return "\n".join(report) + "\n"


def write_report(path: Path, report: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(report, encoding="utf-8")
