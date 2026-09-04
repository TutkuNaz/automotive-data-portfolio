#!/usr/bin/env python3
"""Summarize NHTSA vehicle complaints with no third-party dependencies."""

from __future__ import annotations

import argparse
import collections
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

API = "https://api.nhtsa.gov/complaints/complaintsByVehicle"
TRUE_VALUES = {"Y", "YES", "TRUE"}


def parse_payload(payload: Any) -> list[dict]:
    """Validate the NHTSA response shape instead of treating errors as no data."""
    if not isinstance(payload, dict):
        raise ValueError("Expected a JSON object from the NHTSA API.")
    rows = payload.get("results")
    if not isinstance(rows, list):
        raise ValueError("NHTSA response is missing a list-valued 'results' field.")
    if not all(isinstance(row, dict) for row in rows):
        raise ValueError("NHTSA 'results' contains an unexpected non-object item.")
    count = payload.get("count")
    if isinstance(count, int) and count != len(rows):
        raise ValueError(
            f"NHTSA response count ({count}) does not match results ({len(rows)})."
        )
    return rows


def fetch(
    make: str,
    model: str,
    year: int,
    attempts: int = 3,
) -> list[dict]:
    if attempts < 1:
        raise ValueError("attempts must be at least 1")
    query = urllib.parse.urlencode(
        {"make": make, "model": model, "modelYear": year}
    )
    request = urllib.request.Request(
        f"{API}?{query}",
        headers={"User-Agent": "automotive-open-data-example/1.0"},
    )
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return parse_payload(json.load(response))
        except urllib.error.HTTPError as exc:
            if exc.code != 429 and not 500 <= exc.code < 600:
                raise
            last_error: Exception = exc
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
        if attempt + 1 < attempts:
            time.sleep(attempt + 1)
    raise last_error


def component_names(row: dict) -> list[str]:
    value = row.get("components")
    if not isinstance(value, str) or not value.strip():
        return ["UNKNOWN"]
    # NHTSA separates multiple components with a comma and no following space.
    # Commas followed by spaces may be part of one official component name.
    return [
        component.strip()
        for component in re.split(r",(?=\S)", value)
        if component.strip()
    ]


def summarize(rows: list[dict]) -> dict:
    components: collections.Counter[str] = collections.Counter()
    for row in rows:
        components.update(list(dict.fromkeys(component_names(row))))

    def flagged(field: str) -> int:
        return sum(str(row.get(field, "")).upper() in TRUE_VALUES for row in rows)

    return {
        "complaints": len(rows),
        "crash_reports": flagged("crash"),
        "fire_reports": flagged("fire"),
        "top_components": components.most_common(10),
    }


def vehicle_label(rows: list[dict], fallback: str | None = None) -> str:
    """Read vehicle identity from an offline response when available."""
    identities: set[tuple[str, str, str]] = set()
    for row in rows:
        products = row.get("products")
        if not isinstance(products, list):
            continue
        for product in products:
            if not isinstance(product, dict):
                continue
            parts = [
                product.get("productYear"),
                product.get("productMake"),
                product.get("productModel"),
            ]
            if all(value not in (None, "") for value in parts):
                identities.add(tuple(str(value) for value in parts))
    if len(identities) == 1:
        return " ".join(next(iter(identities)))
    if len(identities) > 1:
        return "Mixed or unspecified NHTSA response"
    return fallback or "Mixed or unspecified NHTSA response"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Summarize NHTSA complaints for one vehicle"
    )
    parser.add_argument("--make")
    parser.add_argument("--model")
    parser.add_argument("--year", type=int)
    parser.add_argument(
        "--input",
        type=Path,
        help="read a saved NHTSA JSON response instead of calling the API",
    )
    args = parser.parse_args()

    if args.input:
        if any(value is not None for value in (args.make, args.model, args.year)):
            parser.error("--input cannot be combined with --make, --model or --year")
        try:
            payload = json.loads(args.input.read_text(encoding="utf-8"))
            rows = parse_payload(payload)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            parser.exit(1, f"Unable to read a valid NHTSA response: {exc}\n")
        label = vehicle_label(rows)
    else:
        make = args.make or "HONDA"
        model = args.model or "CIVIC"
        year = args.year or 2020
        try:
            rows = fetch(make, model, year)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ValueError) as exc:
            parser.exit(1, f"Unable to retrieve a valid NHTSA response: {exc}\n")
        label = vehicle_label(rows, f"{year} {make} {model}")

    print(json.dumps({"vehicle": label, **summarize(rows)}, indent=2))


if __name__ == "__main__":
    main()
