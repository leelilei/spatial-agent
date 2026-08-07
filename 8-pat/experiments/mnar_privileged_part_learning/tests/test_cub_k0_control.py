import sys
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from run_cub_k0_control import evaluate_gates  # noqa: E402


def test_k0_control_gate_passes_only_when_both_branches_pass():
    assert evaluate_gates([1.2, 0.8, 1.1], [2.5, 2.0, 1.8]) == (
        True,
        True,
        True,
    )
    assert evaluate_gates([0.4, 0.6, 0.7], [2.5, 2.0, 1.8]) == (
        False,
        True,
        False,
    )
    assert evaluate_gates([1.2, 0.8, 1.1], [0.9, 1.0, 1.1]) == (
        True,
        False,
        False,
    )
