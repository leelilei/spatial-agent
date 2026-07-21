"""Guard the hard tier: every scenario stays winnable (oracle) AND keeps
defeating the plausible greedy play (difficulty is proven, not asserted)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for extra in (ROOT, ROOT / "tools"):
    if str(extra) not in sys.path:
        sys.path.insert(0, str(extra))

import run_baseline_traces as rbt  # noqa: E402
from run_compliance_probe import load_json  # noqa: E402
from verify_social_outcome_hard_family import (  # noqa: E402
    PLANS,
    WORLD_PATH,
    verify_scenario,
)


def test_hard_family_two_sided() -> None:
    world = rbt.CityWorld(load_json(WORLD_PATH))
    for scenario_id in PLANS:
        result = verify_scenario(world, scenario_id)
        assert result["oracle"]["task_completion"] == 1.0, (
            f"{scenario_id}: oracle cannot win — unfair scenario: {result['oracle']}"
        )
        assert result["oracle"]["trace_feasibility"] == 1.0
        assert result["oracle"]["violations"] == 0
        assert result["oracle"]["outcomes_evidenced"]
        assert result["greedy"]["task_completion"] < 1.0, (
            f"{scenario_id}: greedy play scores full marks — no difficulty headroom"
        )
