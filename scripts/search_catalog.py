#!/usr/bin/env python3
"""Search and filter the automotive open-data catalog."""
from __future__ import annotations
import argparse, csv, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "datasets" / "catalog.csv"

def load_rows(path: Path = CATALOG) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle: return list(csv.DictReader(handle))

def search_rows(query: str = "", category: str | None = None, geography: str | None = None) -> list[dict[str, str]]:
    terms = [term.casefold() for term in query.split() if term.strip()]
    results = []
    for row in load_rows():
        if category and row["category"].casefold() != category.casefold(): continue
        if geography and geography.casefold() not in row["geography"].casefold(): continue
        if all(term in " ".join(row.values()).casefold() for term in terms): results.append(row)
    return results

def print_table(rows: list[dict[str, str]]) -> None:
    nw = min(42, max(len("Dataset"), *(len(r["name"]) for r in rows)))
    cw = max(len("Category"), *(len(r["category"]) for r in rows))
    gw = min(24, max(len("Geography"), *(len(r["geography"]) for r in rows)))
    header = f"{'Dataset':<{nw}}  {'Category':<{cw}}  {'Geography':<{gw}}"
    print(header); print("-" * len(header))
    for row in rows: print(f"{row['name'][:nw]:<{nw}}  {row['category']:<{cw}}  {row['geography'][:gw]:<{gw}}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Find public automotive and mobility datasets")
    parser.add_argument("query", nargs="?", default="", help="keywords, for example 'ev charging'")
    parser.add_argument("--category"); parser.add_argument("--geography")
    parser.add_argument("--format", choices=("detail", "table", "json"), default="detail")
    parser.add_argument("--list-categories", action="store_true")
    args = parser.parse_args()
    if args.list_categories:
        counts = {}
        for row in load_rows(): counts[row["category"]] = counts.get(row["category"], 0) + 1
        for category, count in sorted(counts.items()): print(f"{category}: {count}")
        return
    results = search_rows(args.query, args.category, args.geography)
    if not results: raise SystemExit("No matching datasets found.")
    if args.format == "json": print(json.dumps(results, indent=2, ensure_ascii=False))
    elif args.format == "table": print_table(results)
    else:
        for row in results:
            print(f"\n{row['name']} — {row['provider']}\n  Category: {row['category']} | Geography: {row['geography']}\n  Access: {row['access']} | Terms: {row['license_or_terms']}\n  Idea: {row['project_idea']}\n  Source: {row['source_url']}")

if __name__ == "__main__": main()
