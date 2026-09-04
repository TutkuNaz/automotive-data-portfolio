#!/usr/bin/env python3
"""Search and filter the automotive open-data catalog."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "datasets" / "catalog.csv"


def load_rows(path: Path = CATALOG) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def search_rows(
    query: str = "",
    category: str | None = None,
    geography: str | None = None,
) -> list[dict[str, str]]:
    terms = [term.casefold() for term in query.split() if term.strip()]
    results = []

    for row in load_rows():
        if category and row["category"].casefold() != category.casefold():
            continue
        if geography and geography.casefold() not in row["geography"].casefold():
            continue
        haystack = " ".join(row.values()).casefold()
        if all(term in haystack for term in terms):
            results.append(row)

    return results


def print_table(rows: list[dict[str, str]]) -> None:
    name_width = min(48, max(len("Dataset"), *(len(row["name"]) for row in rows)))
    category_width = max(
        len("Category"),
        *(len(row["category"]) for row in rows),
    )
    geography_width = min(
        32,
        max(len("Geography"), *(len(row["geography"]) for row in rows)),
    )
    header = (
        f"{'Dataset':<{name_width}}  "
        f"{'Category':<{category_width}}  "
        f"{'Geography':<{geography_width}}"
    )
    print(header)
    print("-" * len(header))

    for row in rows:
        print(
            f"{row['name'][:name_width]:<{name_width}}  "
            f"{row['category']:<{category_width}}  "
            f"{row['geography'][:geography_width]:<{geography_width}}"
        )


def print_details(rows: list[dict[str, str]]) -> None:
    for row in rows:
        print(f"\n{row['name']} — {row['provider']}")
        print(f"  Category: {row['category']} | Geography: {row['geography']}")
        print(f"  Access: {row['access']} | Terms: {row['license_or_terms']}")
        print(f"  Idea: {row['project_idea']}")
        print(f"  Source: {row['source_url']}")


def print_categories(rows: list[dict[str, str]]) -> None:
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["category"]] = counts.get(row["category"], 0) + 1
    for category, count in sorted(counts.items()):
        print(f"{category}: {count}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find public automotive and mobility datasets"
    )
    parser.add_argument(
        "query",
        nargs="?",
        default="",
        help="keywords, for example 'ev charging'",
    )
    parser.add_argument("--category", help="exact category filter")
    parser.add_argument(
        "--geography",
        help="case-insensitive country, region or city filter",
    )
    parser.add_argument(
        "--format",
        choices=("detail", "table", "json"),
        default="detail",
    )
    parser.add_argument(
        "--list-categories",
        action="store_true",
        help="show categories and dataset counts",
    )
    args = parser.parse_args()

    if args.list_categories:
        print_categories(load_rows())
        return

    results = search_rows(args.query, args.category, args.geography)
    if not results:
        raise SystemExit("No matching datasets found.")

    if args.format == "json":
        print(json.dumps(results, indent=2, ensure_ascii=False))
    elif args.format == "table":
        print_table(results)
    else:
        print_details(results)


if __name__ == "__main__":
    main()
