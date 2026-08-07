from __future__ import annotations

import sys
import unittest
from pathlib import Path

try:
    import torch
except ModuleNotFoundError:  # Local audit hosts may not have the GPU runtime.
    torch = None


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

if torch is not None:
    from gradient_safety import protect_classification_gradient  # noqa: E402


@unittest.skipIf(torch is None, "PyTorch runtime is tested on the GPU host")
class GradientSafetyTests(unittest.TestCase):
    def test_conflicting_auxiliary_gradient_is_projected(self):
        classification = [torch.tensor([1.0, 0.0])]
        auxiliary = [torch.tensor([-1.0, 1.0])]
        protected, diagnostics = protect_classification_gradient(
            classification, auxiliary
        )
        self.assertTrue(diagnostics.conflict)
        self.assertLess(diagnostics.dot_before, 0)
        self.assertAlmostEqual(diagnostics.dot_after, 0.0, places=6)
        torch.testing.assert_close(protected[0], torch.tensor([0.0, 1.0]))

    def test_aligned_gradient_is_unchanged(self):
        classification = [torch.tensor([1.0, 0.0])]
        auxiliary = [torch.tensor([1.0, 1.0])]
        protected, diagnostics = protect_classification_gradient(
            classification, auxiliary
        )
        self.assertFalse(diagnostics.conflict)
        torch.testing.assert_close(protected[0], auxiliary[0])

    def test_none_for_classifier_only_parameter_is_preserved(self):
        classification = [
            torch.tensor([1.0, 0.0]),
            torch.tensor([2.0]),
        ]
        auxiliary = [torch.tensor([-1.0, 1.0]), None]
        protected, diagnostics = protect_classification_gradient(
            classification, auxiliary
        )
        self.assertTrue(diagnostics.conflict)
        self.assertIsNone(protected[1])


if __name__ == "__main__":
    unittest.main()
