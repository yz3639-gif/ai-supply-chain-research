from __future__ import annotations

import re
from dataclasses import dataclass

from .html_text import snippet_around


EVENT_PATTERNS: dict[str, list[str]] = {
    "order_backlog": [
        r"\border(?:s|ed|ing)?\b",
        r"\bbacklog\b",
        r"\bbook-to-bill\b",
        r"\bpurchase order\b",
        r"\bbookings?\b",
        r"\bawarded\b",
    ],
    "guidance_outlook": [
        r"\boutlook\b",
        r"\bguid(?:e|ance|ed)\b",
        r"\brais(?:e|ed|ing)\b",
        r"\bforecast\b",
        r"\bexpects?\b",
    ],
    "margin_cash": [
        r"\bgross margin\b",
        r"\badjusted gross margin\b",
        r"\bfree cash flow\b",
        r"\boperating cash flow\b",
        r"\bFCF\b",
        r"\bcash\b",
    ],
    "capacity_supply": [
        r"\bcapacity\b",
        r"\bexpand(?:s|ed|ing)?\b",
        r"\bproduction ramp\b",
        r"\bmanufacturing\b",
        r"\bqualification\b",
        r"\bsamples?\b",
        r"\bshipments?\b",
    ],
    "financing_balance_sheet": [
        r"\boffering\b",
        r"\binvestment\b",
        r"\bfinancing\b",
        r"\bwarrant\b",
        r"\bbalance sheet\b",
        r"\bdebt\b",
    ],
    "ai_datacenter": [
        r"\bAI\b",
        r"\bdata center\b",
        r"\bdatacenter\b",
        r"\bhyperscale\b",
        r"\bhyperscaler\b",
        r"\b800G\b",
        r"\b1\.6T\b",
        r"\b3\.2T\b",
        r"\bHBM\b",
        r"\bInP\b",
        r"\bindium phosphide\b",
    ],
}


@dataclass
class DetectedEvent:
    ticker: str
    theme: str
    source_url: str
    source_type: str
    source_quality: str
    category: str
    matched_terms: str
    snippet: str
    model_action: str


def detect_events(
    *,
    ticker: str,
    theme: str,
    source_url: str,
    source_type: str,
    source_quality: str,
    text: str,
) -> list[DetectedEvent]:
    events: list[DetectedEvent] = []
    for category, patterns in EVENT_PATTERNS.items():
        matches: list[str] = []
        for pattern in patterns:
            if re.search(pattern, text, flags=re.IGNORECASE):
                matches.append(pattern.replace(r"\b", "").replace("\\", ""))
        if not matches:
            continue
        first_term = matches[0].strip("^$")
        events.append(
            DetectedEvent(
                ticker=ticker,
                theme=theme,
                source_url=source_url,
                source_type=source_type,
                source_quality=source_quality,
                category=category,
                matched_terms="|".join(matches[:8]),
                snippet=snippet_around(text, first_term.split("|")[0] if first_term else text[:20]),
                model_action=recommended_action(source_quality, category),
            )
        )
    return events


def recommended_action(source_quality: str, category: str) -> str:
    if source_quality == "A" and category in {"order_backlog", "guidance_outlook", "margin_cash"}:
        return "eligible_for_event_ledger_review"
    if source_quality in {"A", "B"}:
        return "update_pre_confirmation_or_watch"
    return "research_only"

