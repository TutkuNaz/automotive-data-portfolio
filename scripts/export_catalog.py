#!/usr/bin/env python3
"""Create the committed JSON catalog from the canonical CSV file."""
import csv, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
CSV_PATH, JSON_PATH = ROOT / "datasets/catalog.csv", ROOT / "datasets/catalog.json"
def build_export() -> dict:
    with CSV_PATH.open(encoding="utf-8", newline="") as handle: datasets = list(csv.DictReader(handle))
    return {"schema_version": 1, "dataset_count": len(datasets), "categories": sorted({r["category"] for r in datasets}), "datasets": datasets}
def main() -> None:
    JSON_PATH.write_text(json.dumps(build_export(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {JSON_PATH.relative_to(ROOT)}")
if __name__ == "__main__": main()
