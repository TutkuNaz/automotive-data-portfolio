#!/usr/bin/env python3
"""Check catalog source URLs with retries and CI-friendly reporting."""

from __future__ import annotations

import argparse
import csv
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / "datasets" / "catalog.csv"
USER_AGENT = (
    "automotive-open-data-link-check/1.0 "
    "(+https://github.com/atasardacagan/automotive-data-portfolio)"
)
RESTRICTED_STATUSES = {401, 403, 405, 429}


def load_urls() -> list[tuple[str, str]]:
    with CATALOG.open(encoding="utf-8", newline="") as handle:
        return [
            (row["name"], row["source_url"])
            for row in csv.DictReader(handle)
        ]


def check_url(
    url: str,
    timeout: float = 15,
    attempts: int = 2,
) -> tuple[bool, str]:
    """Return whether a URL is reachable and a human-readable status."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    detail = "unknown error"

    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                status = response.getcode()
            return status < 400, str(status)
        except urllib.error.HTTPError as exc:
            # These responses demonstrate that the host/page exists but blocks
            # or rate-limits automated requests. They are not broken links.
            if exc.code in RESTRICTED_STATUSES:
                return True, f"{exc.code} (restricted)"
            detail = f"HTTP {exc.code}"
        except (urllib.error.URLError, TimeoutError) as exc:
            detail = str(getattr(exc, "reason", exc))

        if attempt + 1 < attempts:
            time.sleep(1)

    return False, detail


def check_item(
    item: tuple[str, str],
    timeout: float,
    attempts: int,
) -> tuple[str, str, bool, str]:
    name, url = item
    ok, status = check_url(url, timeout=timeout, attempts=attempts)
    return name, url, ok, status


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check source links in datasets/catalog.csv"
    )
    parser.add_argument("--timeout", type=float, default=15)
    parser.add_argument("--attempts", type=int, default=2)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--limit", type=int, help="check only the first N links")
    args = parser.parse_args()

    urls = load_urls()[: args.limit]
    failures: list[tuple[str, str, str]] = []
    workers = max(1, args.workers)

    with ThreadPoolExecutor(max_workers=workers) as pool:
        results = pool.map(
            lambda item: check_item(item, args.timeout, args.attempts),
            urls,
        )
        for name, url, ok, status in results:
            print(f"{'OK' if ok else 'FAIL':4} {status:18} {name}")
            if not ok:
                failures.append((name, url, status))

    if failures:
        print(f"\n{len(failures)} of {len(urls)} links failed:")
        for name, url, status in failures:
            print(f"- {name}: {status} ({url})")
        raise SystemExit(1)

    print(f"\nAll {len(urls)} links are reachable.")


if __name__ == "__main__":
    main()
