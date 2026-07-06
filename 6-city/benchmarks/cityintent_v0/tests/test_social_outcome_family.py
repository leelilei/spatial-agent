"""Guard the social-outcome scenario family: every scenario must stay a fair
(oracle-winnable) test with an accepted co-presence outcome."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for extra in (ROOT, ROOT / "tools"):
    if str(extra) not in sys.path:
        sys.path.insert(0, str(extra))

import run_baseline_traces as rbt  # noqa: E402
from run_compliance_probe import load_json  # noqa: E402
from verify_social_outcome_family import (  # noqa: E402
    ORACLE_PLANS,
    WORLD_PATH,
    verify_scenario,
)


def test_every_social_outcome_scenario_is_oracle_winnable() -> None:
    world = rbt.CityWorld(load_json(WORLD_PATH))
    for scenario_id in ORACLE_PLANS:
        result = verify_scenario(world, scenario_id)
        assert result["passed"], f"{scenario_id} not winnable: {result}"
        assert result["task_completion"] == 1.0
        assert result["trace_feasibility"] == 1.0
        assert result["co_presence_outcomes"] >= 1
        assert result["accepted_interactions"], f"{scenario_id}: no accepted interaction"
