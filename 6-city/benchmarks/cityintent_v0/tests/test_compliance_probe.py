"""Guard the oracle compliance probe: the evidence contract must stay satisfiable
and each adapter action surface must keep expressing the winning move."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for extra in (ROOT, ROOT / "tools"):
    if str(extra) not in sys.path:
        sys.path.insert(0, str(extra))

import run_baseline_traces as rbt  # noqa: E402
from run_compliance_probe import (  # noqa: E402
    ORACLE_PLANS,
    SCENARIO_DIR,
    WORLD_PATH,
    load_json,
    run_oracle_trace,
    tier_a_check,
    tier_b_plan_format,
    tier_b_sotopia,
)


def _world() -> rbt.CityWorld:
    return rbt.CityWorld(load_json(WORLD_PATH))


def test_tier_a_contract_is_satisfiable_for_every_scenario() -> None:
    world = _world()
    for scenario_id, plan in ORACLE_PLANS.items():
        scenario = load_json(SCENARIO_DIR / f"{scenario_id}.json")
        trace = run_oracle_trace(world, scenario, plan["actions"])
        tier_a = tier_a_check(trace)
        assert tier_a["passed"], f"{scenario_id}: contract not satisfiable: {tier_a}"
        assert tier_a["task_completion"] == 1.0
        assert tier_a["trace_feasibility"] == 1.0
        assert tier_a["violation_count"] == 0


def test_tier_b_adapter_surfaces_express_the_winning_move() -> None:
    world = _world()
    for scenario_id, plan in ORACLE_PLANS.items():
        assert tier_b_sotopia(world, plan)["passed"], f"{scenario_id}: SOTOPIA surface"
        assert tier_b_plan_format(
            world, plan, "generative_agents_official",
            "GenerativeAgentsOfficialPlannerAdapter", "GenerativeAgents",
        )["passed"], f"{scenario_id}: GenerativeAgents surface"
        assert tier_b_plan_format(
            world, plan, "agentsociety_official",
            "AgentSocietyOfficialPlanBlocksAdapter", "AgentSociety",
        )["passed"], f"{scenario_id}: AgentSociety surface"
