#!/usr/bin/env python3
"""Small NHTSA complaints analysis using only the Python standard library."""
from __future__ import annotations
import argparse, collections, json, urllib.parse, urllib.request
from pathlib import Path
API = "https://api.nhtsa.gov/complaints/complaintsByVehicle"
def fetch(make: str, model: str, year: int) -> list[dict]:
    query = urllib.parse.urlencode({"make": make, "model": model, "modelYear": year})
    request = urllib.request.Request(f"{API}?{query}", headers={"User-Agent": "automotive-open-data-example/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response: return json.load(response).get("results", [])
def summarize(rows: list[dict]) -> dict:
    components = collections.Counter(row.get("components") or "UNKNOWN" for row in rows)
    flagged = lambda field: sum(str(row.get(field, "")).upper() in {"Y", "YES", "TRUE"} for row in rows)
    return {"complaints": len(rows), "crash_reports": flagged("crash"), "fire_reports": flagged("fire"), "top_components": components.most_common(10)}
def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize NHTSA complaints for one vehicle")
    parser.add_argument("--make", default="HONDA"); parser.add_argument("--model", default="CIVIC"); parser.add_argument("--year", type=int, default=2020); parser.add_argument("--input", type=Path)
    args = parser.parse_args()
    rows = json.loads(args.input.read_text(encoding="utf-8")).get("results", []) if args.input else fetch(args.make, args.model, args.year)
    print(json.dumps({"vehicle": f"{args.year} {args.make} {args.model}", **summarize(rows)}, indent=2))
if __name__ == "__main__": main()
