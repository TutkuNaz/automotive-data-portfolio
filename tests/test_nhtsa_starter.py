import json
import unittest
from pathlib import Path

from examples.nhtsa_reliability_starter import (
    parse_payload,
    summarize,
    vehicle_label,
)


SAMPLE_ROWS = [
    {
        "components": "STEERING,POWER TRAIN",
        "crash": "Y",
        "fire": "N",
        "products": [
            {
                "productYear": "2012",
                "productMake": "ACURA",
                "productModel": "RDX",
            }
        ],
    },
    {
        "components": "POWER TRAIN,POWER TRAIN",
        "crash": False,
        "fire": True,
        "products": [],
    },
]
ROOT = Path(__file__).resolve().parents[1]


class NhtsaStarterTests(unittest.TestCase):
    def test_payload_shape_is_validated(self):
        self.assertEqual(parse_payload({"count": 2, "results": SAMPLE_ROWS}), SAMPLE_ROWS)
        with self.assertRaisesRegex(ValueError, "results"):
            parse_payload({"message": "rate limit"})
        with self.assertRaisesRegex(ValueError, "does not match"):
            parse_payload({"count": 3, "results": SAMPLE_ROWS})

    def test_components_are_counted_individually(self):
        summary = summarize(SAMPLE_ROWS)
        self.assertEqual(summary["complaints"], 2)
        self.assertEqual(summary["crash_reports"], 1)
        self.assertEqual(summary["fire_reports"], 1)
        self.assertEqual(summary["top_components"][0], ("POWER TRAIN", 2))

    def test_taxonomy_commas_are_preserved(self):
        rows = [
            {
                "components": (
                    "SERVICE BRAKES, HYDRAULIC:FOUNDATION COMPONENTS:"
                    "MASTER CYLINDER"
                )
            }
        ]
        self.assertEqual(
            summarize(rows)["top_components"],
            [
                (
                    "SERVICE BRAKES, HYDRAULIC:FOUNDATION COMPONENTS:"
                    "MASTER CYLINDER",
                    1,
                )
            ],
        )

    def test_tied_components_keep_first_seen_order(self):
        rows = [{"components": "STEERING,POWER TRAIN"}]
        self.assertEqual(
            summarize(rows)["top_components"],
            [("STEERING", 1), ("POWER TRAIN", 1)],
        )

    def test_offline_vehicle_label_comes_from_response(self):
        self.assertEqual(vehicle_label(SAMPLE_ROWS), "2012 ACURA RDX")
        self.assertEqual(
            vehicle_label([], None),
            "Mixed or unspecified NHTSA response",
        )

    def test_mixed_offline_response_is_not_mislabeled(self):
        mixed = SAMPLE_ROWS + [
            {
                "products": [
                    {
                        "productYear": "2020",
                        "productMake": "HONDA",
                        "productModel": "CIVIC",
                    }
                ]
            }
        ]
        self.assertEqual(
            vehicle_label(mixed),
            "Mixed or unspecified NHTSA response",
        )

    def test_notebook_code_cells_compile(self):
        notebook = json.loads(
            (ROOT / "examples/nhtsa_reliability_starter.ipynb").read_text(
                encoding="utf-8"
            )
        )
        code_cells = [
            "".join(cell["source"])
            for cell in notebook["cells"]
            if cell["cell_type"] == "code"
        ]
        self.assertTrue(code_cells)
        for index, source in enumerate(code_cells, start=1):
            compile(source, f"notebook-cell-{index}", "exec")


if __name__ == "__main__":
    unittest.main()
