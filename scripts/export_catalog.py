#!/usr/bin/env python3
"""Create or verify the JSON export of the canonical CSV catalog."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "datasets" / "catalog.csv"
JSON_PATH = ROOT / "datasets" / "catalog.json"


def build_export() -> dict:
    with CSV_PATH.open(encoding="utf-8", newline="") as handle:
        datasets = list(csv.DictReader(handle))
    return {
        "schema_version": 1,
        "dataset_count": len(datasets),
        "categories": sorted({row["category"] for row in datasets}),
        "datasets": datasets,
    }


def serialize_export() -> str:
    return json.dumps(build_export(), indent=2, ensure_ascii=False) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create or verify datasets/catalog.json"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if the committed JSON does not match the CSV",
    )
    args = parser.parse_args()
    expected = serialize_export()

    if args.check:
        if not JSON_PATH.exists() or JSON_PATH.read_text(encoding="utf-8") != expected:
            raise SystemExit(
                "datasets/catalog.json is stale; run scripts/export_catalog.py"
            )
        print("datasets/catalog.json is current.")
        return

    JSON_PATH.write_text(expected, encoding="utf-8")
    print(f"Wrote {JSON_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
