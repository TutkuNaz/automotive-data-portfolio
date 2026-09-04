import csv
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

from scripts.export_catalog import build_export
from scripts.search_catalog import search_rows

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "datasets" / "catalog.csv"
REQUIRED = {
    "category",
    "name",
    "provider",
    "geography",
    "access",
    "license_or_terms",
    "update_cadence",
    "project_idea",
    "source_url",
}


class CatalogTests(unittest.TestCase):
    def setUp(self):
        with CATALOG.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            self.fieldnames = set(reader.fieldnames or [])
            self.rows = list(reader)

    def test_required_columns_exist(self):
        self.assertTrue(REQUIRED.issubset(self.fieldnames))

    def test_catalog_has_useful_breadth(self):
        self.assertGreaterEqual(len(self.rows), 35)
        self.assertGreaterEqual(len({row["category"] for row in self.rows}), 10)

    def test_rows_are_complete_and_sources_are_https(self):
        for row in self.rows:
            for column in REQUIRED:
                self.assertTrue(row[column].strip(), f"Missing {column} for {row.get('name', 'unknown row')}")
            self.assertTrue(row["source_url"].startswith("https://"))

    def test_dataset_names_are_unique(self):
        names = [row["name"] for row in self.rows]
        self.assertEqual(len(names), len(set(names)))

    def test_json_export_matches_csv(self):
        exported = json.loads(
            (ROOT / "datasets/catalog.json").read_text(encoding="utf-8")
        )
        self.assertEqual(exported["schema_version"], 1)
        self.assertEqual(exported["dataset_count"], len(self.rows))
        self.assertEqual(exported["datasets"], self.rows)
        self.assertEqual(exported, build_export())

    def test_readme_catalog_counts_are_current(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        summary = re.search(
            r"\*\*(\d+) curated datasets · (\d+) categories",
            readme,
        )
        self.assertIsNotNone(summary)
        self.assertEqual(int(summary.group(1)), len(self.rows))
        self.assertEqual(
            int(summary.group(2)),
            len({row["category"] for row in self.rows}),
        )

    def test_country_geography_filter_includes_subnational_rows(self):
        results = search_rows(geography="United States")
        names = {row["name"] for row in results}
        self.assertIn("NYC TLC Trip Record Data", names)
        self.assertIn("Electric Vehicle Population Data", names)

    def test_search_cli_json_output(self):
        result = subprocess.run(
            [
                sys.executable,
                ROOT / "scripts/search_catalog.py",
                "recall",
                "--format",
                "json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        rows = json.loads(result.stdout)
        self.assertTrue(rows)
        self.assertTrue(all("recall" in " ".join(row.values()).casefold() for row in rows))


if __name__ == "__main__":
    unittest.main()
