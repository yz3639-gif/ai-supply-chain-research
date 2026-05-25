from __future__ import annotations

import json
from typing import Any

from .http_client import fetch_url


SEC_TICKER_URL = "https://www.sec.gov/files/company_tickers.json"
SEC_SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik10}.json"


def fetch_sec_filings(tickers: list[str], limit_per_ticker: int = 8) -> list[dict[str, Any]]:
    mapping_result = fetch_url(SEC_TICKER_URL)
    if not mapping_result.text or mapping_result.status != 200:
        return [
            {
                "ticker": ticker,
                "error": f"Unable to fetch SEC ticker map: {mapping_result.error or mapping_result.status}",
            }
            for ticker in tickers
        ]
    raw_map = json.loads(mapping_result.text)
    ticker_to_cik = {
        item["ticker"].upper(): int(item["cik_str"])
        for item in raw_map.values()
        if "ticker" in item and "cik_str" in item
    }
    records: list[dict[str, Any]] = []
    for ticker in tickers:
        cik = ticker_to_cik.get(ticker.upper())
        if not cik:
            records.append({"ticker": ticker, "error": "CIK not found in SEC ticker map"})
            continue
        cik10 = f"{cik:010d}"
        submission_result = fetch_url(SEC_SUBMISSIONS_URL.format(cik10=cik10))
        if not submission_result.text or submission_result.status != 200:
            records.append(
                {
                    "ticker": ticker,
                    "cik": cik10,
                    "error": f"Unable to fetch SEC submissions: {submission_result.error or submission_result.status}",
                }
            )
            continue
        data = json.loads(submission_result.text)
        recent = data.get("filings", {}).get("recent", {})
        forms = recent.get("form", [])
        filing_dates = recent.get("filingDate", [])
        accession_numbers = recent.get("accessionNumber", [])
        primary_documents = recent.get("primaryDocument", [])
        for idx, form in enumerate(forms[:limit_per_ticker]):
            accession = accession_numbers[idx] if idx < len(accession_numbers) else ""
            accession_no_dash = accession.replace("-", "")
            primary_doc = primary_documents[idx] if idx < len(primary_documents) else ""
            filing_url = ""
            if accession and primary_doc:
                filing_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_no_dash}/{primary_doc}"
            records.append(
                {
                    "ticker": ticker,
                    "cik": cik10,
                    "company_name": data.get("name", ""),
                    "form": form,
                    "filing_date": filing_dates[idx] if idx < len(filing_dates) else "",
                    "accession_number": accession,
                    "filing_url": filing_url,
                    "fetched_at_utc": submission_result.fetched_at_utc,
                    "error": "",
                }
            )
    return records

