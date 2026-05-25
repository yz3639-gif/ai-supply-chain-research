from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_USER_AGENT = (
    "ai-supply-chain-research/1.0 "
    "contact: research-local@example.com"
)


@dataclass
class FetchResult:
    url: str
    status: int
    fetched_at_utc: str
    content_type: str
    text: str
    error: str = ""


def fetch_url(url: str, timeout: int = 20, user_agent: str = DEFAULT_USER_AGENT) -> FetchResult:
    fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    request = Request(url, headers={"User-Agent": user_agent, "Accept": "*/*"})
    try:
        with urlopen(request, timeout=timeout) as response:
            raw = response.read()
            content_type = response.headers.get("Content-Type", "")
            charset = response.headers.get_content_charset() or "utf-8"
            text = raw.decode(charset, errors="replace")
            return FetchResult(
                url=url,
                status=getattr(response, "status", 200),
                fetched_at_utc=fetched_at,
                content_type=content_type,
                text=text,
            )
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if exc.fp else ""
        return FetchResult(
            url=url,
            status=exc.code,
            fetched_at_utc=fetched_at,
            content_type="",
            text=body,
            error=f"HTTPError: {exc}",
        )
    except (URLError, TimeoutError, OSError) as exc:
        return FetchResult(
            url=url,
            status=0,
            fetched_at_utc=fetched_at,
            content_type="",
            text="",
            error=f"{type(exc).__name__}: {exc}",
        )

