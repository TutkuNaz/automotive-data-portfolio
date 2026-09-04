#!/usr/bin/env python3
"""Check catalog source URLs with retries and CI-friendly reporting."""
import argparse, csv, time, urllib.error, urllib.request
from pathlib import Path
CATALOG = Path(__file__).resolve().parents[1] / "datasets/catalog.csv"
USER_AGENT = "automotive-open-data-link-check/1.0"
def load_urls():
    with CATALOG.open(encoding="utf-8", newline="") as handle: return [(r["name"], r["source_url"]) for r in csv.DictReader(handle)]
def check_url(url: str, timeout: float = 15, attempts: int = 2):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response: code = response.getcode()
            return code < 400, str(code)
        except urllib.error.HTTPError as exc:
            if exc.code in {401, 403, 405, 429}: return True, f"{exc.code} (restricted)"
            detail = f"HTTP {exc.code}"
        except (urllib.error.URLError, TimeoutError) as exc: detail = str(getattr(exc, "reason", exc))
        if attempt + 1 < attempts: time.sleep(1)
    return False, detail
def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--timeout", type=float, default=15); parser.add_argument("--attempts", type=int, default=2); parser.add_argument("--limit", type=int); args = parser.parse_args()
    failures, urls = [], load_urls()[:args.limit]
    for name, url in urls:
        ok, status = check_url(url, args.timeout, args.attempts); print(f"{'OK' if ok else 'FAIL':4} {status:18} {name}")
        if not ok: failures.append((name, url, status))
    if failures: raise SystemExit(f"{len(failures)} of {len(urls)} links failed")
    print(f"All {len(urls)} links are reachable.")
if __name__ == "__main__": main()
