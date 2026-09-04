import csv
import unittest
from pathlib import Path

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
        self.assertGreaterEqual(len(self.rows), 12)
        self.assertGreaterEqual(len({row["category"] for row in self.rows}), 6)

    def test_rows_are_complete_and_sources_are_https(self):
        for row in self.rows:
            for column in REQUIRED:
                self.assertTrue(row[column].strip(), f"Missing {column} for {row.get('name', 'unknown row')}")
            self.assertTrue(row["source_url"].startswith("https://"))

    def test_dataset_names_are_unique(self):
        names = [row["name"] for row in self.rows]
        self.assertEqual(len(names), len(set(names)))


if __name__ == "__main__":
    unittest.main()
