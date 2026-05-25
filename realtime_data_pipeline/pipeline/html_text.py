from __future__ import annotations

import re
from html import unescape
from html.parser import HTMLParser


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._skip_depth = 0
        self._title_depth = 0
        self.title_parts: list[str] = []
        self.text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript", "svg"}:
            self._skip_depth += 1
        if tag == "title":
            self._title_depth += 1
        if tag in {"p", "br", "li", "tr", "h1", "h2", "h3"}:
            self.text_parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "svg"} and self._skip_depth:
            self._skip_depth -= 1
        if tag == "title" and self._title_depth:
            self._title_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._skip_depth:
            return
        cleaned = data.strip()
        if not cleaned:
            return
        if self._title_depth:
            self.title_parts.append(cleaned)
        self.text_parts.append(cleaned)


def html_to_text(html: str) -> tuple[str, str]:
    parser = TextExtractor()
    parser.feed(html)
    title = normalize_text(" ".join(parser.title_parts))
    text = normalize_text(" ".join(parser.text_parts))
    return title, text


def normalize_text(value: str) -> str:
    value = unescape(value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def snippet_around(text: str, term: str, radius: int = 180) -> str:
    lower_text = text.lower()
    idx = lower_text.find(term.lower())
    if idx < 0:
        return text[: radius * 2].strip()
    start = max(0, idx - radius)
    end = min(len(text), idx + len(term) + radius)
    return text[start:end].strip()

