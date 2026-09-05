#!/usr/bin/env python3
"""Check catalog source URLs with retries and CI-friendly reporting."""

from __future__ import annotations

import argparse
import csv
import http.client
import socket
import ssl
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Literal

CATALOG = Path(__file__).resolve().parents[1] / "datasets" / "catalog.csv"
USER_AGENT = (
    "automotive-open-data-link-check/1.0 "
    "(+https://github.com/TutkuNaz/automotive-data-portfolio)"
)
RESTRICTED_STATUSES = {401, 403, 405}
BROKEN_STATUSES = {404, 410}
TRANSIENT_STATUSES = {408, 425, 429}
LinkState = Literal["ok", "warning", "failed"]


def load_sources() -> list[tuple[str, str]]:
    with CATALOG.open(encoding="utf-8", newline="") as handle:
        return [
            (row["name"], row["source_url"])
            for row in csv.DictReader(handle)
        ]


def unique_urls(sources: list[tuple[str, str]]) -> list[str]:
    """Keep URL order while avoiding duplicate requests to shared landing pages."""
    return list(dict.fromkeys(url for _, url in sources))


def retry_delay(exc: urllib.error.HTTPError, fallback: int) -> int:
    value = exc.headers.get("Retry-After") if exc.headers else None
    try:
        return min(5, max(1, int(value)))
    except (TypeError, ValueError):
        return fallback


def check_url(
    url: str,
    timeout: float = 15,
    attempts: int = 2,
) -> tuple[LinkState, str]:
    """Return a link state and human-readable status after bounded retries."""
    if attempts < 1:
        raise ValueError("attempts must be at least 1")

    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    state: LinkState = "warning"
    detail = "unknown error"

    for attempt in range(attempts):
        delay = attempt + 1
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                status = response.getcode()
            return "ok", str(status)
        except urllib.error.HTTPError as exc:
            if exc.code in RESTRICTED_STATUSES:
                return "warning", f"HTTP {exc.code} (automated access restricted)"
            if exc.code in TRANSIENT_STATUSES:
                state, detail = "warning", f"HTTP {exc.code} (transient response)"
            elif exc.code in BROKEN_STATUSES or 400 <= exc.code < 500:
                state, detail = "failed", f"HTTP {exc.code}"
            else:
                state, detail = "warning", f"HTTP {exc.code} (server error)"
            delay = retry_delay(exc, delay)
        except (
            urllib.error.URLError,
            TimeoutError,
            ConnectionError,
            http.client.RemoteDisconnected,
            OSError,
        ) as exc:
            reason = getattr(exc, "reason", exc)
            permanent = isinstance(
                reason,
                (socket.gaierror, ssl.SSLCertVerificationError, ConnectionRefusedError),
            )
            state = "failed" if permanent else "warning"
            detail = str(reason)

        if attempt + 1 < attempts:
            time.sleep(delay)

    if state == "warning" and not detail.startswith("HTTP "):
        detail = f"unverified after retries: {detail}"
    return state, detail


def check_item(
    url: str,
    timeout: float,
    attempts: int,
) -> tuple[str, LinkState, str]:
    state, status = check_url(url, timeout=timeout, attempts=attempts)
    return url, state, status


def positive_int(value: str) -> int:
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return parsed


def positive_float(value: str) -> float:
    parsed = float(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be greater than 0")
    return parsed


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check source links in datasets/catalog.csv"
    )
    parser.add_argument("--timeout", type=positive_float, default=15)
    parser.add_argument("--attempts", type=positive_int, default=2)
    parser.add_argument("--workers", type=positive_int, default=8)
    parser.add_argument(
        "--limit",
        type=positive_int,
        help="check only the first N catalog entries",
    )
    args = parser.parse_args()

    sources = load_sources()[: args.limit]
    urls = unique_urls(sources)
    status_by_url: dict[str, tuple[LinkState, str]] = {}

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = pool.map(
            lambda url: check_item(url, args.timeout, args.attempts),
            urls,
        )
        for url, state, status in results:
            status_by_url[url] = (state, status)

    failures: list[tuple[str, str, str]] = []
    warning_count = 0
    for name, url in sources:
        state, status = status_by_url[url]
        print(f"{state.upper():7} {status:45} {name}")
        if state == "failed":
            failures.append((name, url, status))
        elif state == "warning":
            warning_count += 1

    if failures:
        print(f"\n{len(failures)} of {len(sources)} catalog entries failed:")
        for name, url, status in failures:
            print(f"- {name}: {status} ({url})")
        raise SystemExit(1)

    print(
        f"\nNo definitively broken links found across {len(sources)} entries; "
        f"{warning_count} could not be fully verified automatically."
    )


if __name__ == "__main__":
    main()
