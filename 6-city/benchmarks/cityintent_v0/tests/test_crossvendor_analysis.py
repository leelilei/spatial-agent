from __future__ import annotations

import sys
import unittest
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

from analyze_crossvendor_backbones import permutation_bootstrap  # noqa: E402
from analyze_e3e_multivendor_backbones import holm_adjust  # noqa: E402


class CrossVendorAnalysisTest(unittest.TestCase):
    def test_permutation_bootstrap_is_deterministic(self) -> None:
        first = [0.8, 0.85, 0.9, 0.95, 1.0]
        second = [0.2, 0.25, 0.3, 0.35, 0.4]

        result_a = permutation_bootstrap(
            first, second, samples=1_000, seed=17
        )
        result_b = permutation_bootstrap(
            first, second, samples=1_000, seed=17
        )

        self.assertEqual(result_a, result_b)
        self.assertAlmostEqual(result_a["delta"], 0.6)
        self.assertLess(result_a["p_value"], 0.05)

    def test_permutation_bootstrap_reports_null_difference(self) -> None:
        values = [0.2, 0.5, 0.8]

        result = permutation_bootstrap(
            values, values, samples=1_000, seed=23
        )

        self.assertEqual(result["delta"], 0.0)
        self.assertEqual(result["p_value"], 1.0)

    def test_holm_adjustment_is_monotone_in_sorted_p_values(self) -> None:
        rows = [
            {"p_value": 0.06},
            {"p_value": 0.001},
            {"p_value": 0.02},
        ]

        holm_adjust(rows)

        ordered = sorted(rows, key=lambda row: row["p_value"])
        adjusted = [row["p_holm"] for row in ordered]
        self.assertEqual(adjusted, sorted(adjusted))
        self.assertEqual(ordered[0]["p_holm"], 0.003)
        self.assertFalse(rows[0]["significant_holm_0_05"])


if __name__ == "__main__":
    unittest.main()
