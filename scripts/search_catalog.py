#!/usr/bin/env python3
"""Search the automotive open-data catalog from the command line."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / "datasets" / "catalog.csv"


def load_rows() -> list[dict[str, str]]:
    with CATALOG.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def search_rows(query: str, category: str | None = None) -> list[dict[str, str]]:
    terms = [term.lower() for term in query.split() if term.strip()]
    rows = load_rows()
    results: list[dict[str, str]] = []

    for row in rows:
        if category and row["category"].lower() != category.lower():
            continue
        haystack = " ".join(row.values()).lower()
        if all(term in haystack for term in terms):
            results.append(row)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description="Search automotive public datasets")
    parser.add_argument("query", nargs="?", default="", help="keywords such as 'ev charging' or 'safety recalls'")
    parser.add_argument("--category", help="optional exact category filter")
    args = parser.parse_args()

    results = search_rows(args.query, args.category)
    if not results:
        print("No matching datasets found.")
        return

    for row in results:
        print(f"\n{row['name']} — {row['provider']}")
        print(f"  Category: {row['category']} | Geography: {row['geography']}")
        print(f"  Access: {row['access']} | Terms: {row['license_or_terms']}")
        print(f"  Idea: {row['project_idea']}")
        print(f"  Source: {row['source_url']}")


if __name__ == "__main__":
    main()
