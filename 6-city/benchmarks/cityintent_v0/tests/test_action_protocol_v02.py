from __future__ import annotations

import sys
import unittest
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

from run_baseline_traces import (  # noqa: E402
    Action,
    CityWorld,
    TraceState,
    condition_evidence,
    condition_success,
    execute_action,
    has_arrived,
    has_entered,
    parse_time,
    record_entry,
    score_trace,
)


class ActionProtocolV02Test(unittest.TestCase):
    def setUp(self) -> None:
        self.world = CityWorld(
            {
                "locations": [
                    {"id": "home", "open": ["00:00", "23:59"], "typical_cost": 0},
                    {"id": "hallway", "open": ["00:00", "23:59"], "typical_cost": 0},
                    {"id": "shop", "open": ["09:00", "18:00"], "typical_cost": 4},
                    {"id": "cafe", "open": ["09:00", "18:00"], "typical_cost": 3},
                ],
                "edges": [
                    {"from": "home", "to": "hallway", "minutes": 5},
                    {"from": "hallway", "to": "shop", "minutes": 5},
                    {"from": "hallway", "to": "cafe", "minutes": 4},
                    {"from": "shop", "to": "cafe", "minutes": 3},
                ],
            }
        )
        self.scenario = {
            "scenario_id": "protocol_test",
            "events": [],
            "episode": {"start_time": "10:00", "end_time": "12:00", "max_steps": 8},
        }

    def state(self) -> TraceState:
        state = TraceState(
            scenario_id="protocol_test",
            agent_id="aria",
            agent_type="utility_planner",
            time=parse_time("10:00"),
            end_time=parse_time("12:00"),
            location="home",
            budget=10,
        )
        state.inside_location = "home"
        record_entry(state, "home", state.time, kind="start")
        return state

    def test_move_arrival_does_not_enter_spend_or_complete_purchase(self) -> None:
        state = self.state()
        condition = {
            "type": "buy_item",
            "location": "shop",
            "item": "groceries",
        }

        execute_action(
            self.world,
            self.scenario,
            state,
            Action("move", target="shop", path=["home", "hallway", "shop"]),
        )

        self.assertTrue(has_arrived(state, "shop"))
        self.assertFalse(has_entered(state, "shop"))
        self.assertFalse(has_entered(state, "hallway"))
        self.assertIsNone(state.inside_location)
        self.assertEqual(state.budget, 10)
        self.assertEqual(condition_success(condition, state, self.scenario), 0)

    def test_enter_then_buy_creates_evidence_and_charges_once(self) -> None:
        state = self.state()
        execute_action(self.world, self.scenario, state, Action("move", target="shop"))
        execute_action(self.world, self.scenario, state, Action("enter", target="shop"))
        execute_action(
            self.world,
            self.scenario,
            state,
            Action("buy", target="shop", item="groceries", minutes=2),
        )

        condition = {
            "type": "buy_item",
            "location": "shop",
            "item": "groceries",
        }
        self.assertTrue(has_entered(state, "shop"))
        self.assertEqual(condition_success(condition, state, self.scenario), 1)
        self.assertEqual(state.budget, 6)
        self.assertEqual(state.purchases[0]["item"], "groceries")
        self.assertFalse(state.violations)

    def test_ignored_start_is_not_return_evidence(self) -> None:
        state = self.state()
        condition = {
            "type": "visit_before",
            "location": "home",
            "deadline": "12:00",
            "ignore_start": True,
        }

        self.assertEqual(condition_success(condition, state, self.scenario), 0)
        self.assertEqual(condition_evidence(condition, state), [])

    def test_closed_entry_and_unpaid_dwell_are_rejected(self) -> None:
        closed_scenario = {
            **self.scenario,
            "events": [
                {
                    "time": "09:30",
                    "location": "cafe",
                    "effect": {"closed_until": "11:00"},
                }
            ],
        }
        state = self.state()
        execute_action(self.world, closed_scenario, state, Action("move", target="cafe"))
        execute_action(self.world, closed_scenario, state, Action("enter", target="cafe"))
        self.assertIn("closed_location", [item["kind"] for item in state.violations])
        self.assertFalse(has_entered(state, "cafe"))

        paid_state = self.state()
        execute_action(self.world, self.scenario, paid_state, Action("move", target="shop"))
        execute_action(self.world, self.scenario, paid_state, Action("enter", target="shop"))
        execute_action(self.world, self.scenario, paid_state, Action("dwell", minutes=10))
        self.assertIn(
            "unpaid_service_required",
            [item["kind"] for item in paid_state.violations],
        )
        self.assertEqual(paid_state.dwell.get("shop", 0), 0)

    def test_new_midroute_block_interrupts_without_agent_violation(self) -> None:
        scenario = {
            **self.scenario,
            "events": [
                {
                    "time": "10:07",
                    "type": "road_closure",
                    "visibility": "public",
                    "effect": {
                        "blocked_edge": ["hallway", "shop"],
                        "until": "11:00",
                    },
                }
            ],
        }
        state = self.state()

        execute_action(
            self.world,
            scenario,
            state,
            Action("move", target="shop", path=["home", "hallway", "shop"]),
        )

        self.assertEqual(state.location, "hallway")
        self.assertEqual(state.time, parse_time("10:07"))
        self.assertEqual(len(state.route_interruptions), 1)
        self.assertEqual(state.route_interruptions[0]["event_id"], "road_closure")
        self.assertFalse(has_arrived(state, "shop"))
        self.assertFalse(state.violations)

    def test_detour_after_interruption_creates_verified_replan(self) -> None:
        scenario = {
            **self.scenario,
            "events": [
                {
                    "time": "10:07",
                    "type": "road_closure",
                    "visibility": "public",
                    "effect": {
                        "blocked_edge": ["hallway", "shop"],
                        "until": "11:00",
                    },
                }
            ],
        }
        state = self.state()
        execute_action(
            self.world,
            scenario,
            state,
            Action("move", target="shop", path=["home", "hallway", "shop"]),
        )
        execute_action(self.world, scenario, state, Action("move", target="shop"))

        condition = {"type": "replan_after_event", "event_id": "road_closure"}
        self.assertEqual(state.location, "shop")
        self.assertEqual(len(state.replans), 1)
        self.assertEqual(
            state.replans[0]["chosen_path"], ["hallway", "cafe", "shop"]
        )
        self.assertEqual(condition_success(condition, state, scenario), 1)
        self.assertEqual(condition_evidence(condition, state), state.replans)
        self.assertFalse(state.violations)

    def test_known_blocked_edge_attempt_is_a_violation(self) -> None:
        scenario = {
            **self.scenario,
            "events": [
                {
                    "time": "10:04",
                    "type": "road_closure",
                    "visibility": "public",
                    "effect": {
                        "blocked_edge": ["hallway", "shop"],
                        "until": "11:00",
                    },
                }
            ],
        }
        state = self.state()
        state.agent_type = "llm_direct_actor"
        execute_action(
            self.world,
            scenario,
            state,
            Action("move", target="hallway", path=["home", "hallway"]),
        )
        execute_action(
            self.world,
            scenario,
            state,
            Action("move", target="shop", path=["hallway", "shop"]),
        )

        self.assertEqual(state.location, "hallway")
        self.assertIn("blocked_edge", [item["kind"] for item in state.violations])
        self.assertFalse(state.route_interruptions)

    def test_goal_drift_does_not_reduce_trace_feasibility(self) -> None:
        scenario = {
            **self.scenario,
            "agents": [{"start_location": "home"}],
            "success_conditions": [
                {
                    "id": "reach_shop",
                    "type": "visit_location",
                    "location": "shop",
                    "weight": 1.0,
                }
            ],
        }
        state = self.state()
        execute_action(self.world, scenario, state, Action("finish"))

        scored = score_trace(self.world, scenario, state)

        self.assertEqual(scored["metrics"]["goal_completion"], 0)
        self.assertEqual(scored["failure_taxonomy"].get("goal_drift"), 1)
        self.assertEqual(scored["metrics"]["trace_feasibility"], 1)
        self.assertEqual(scored["metrics"]["impossible_trace_rate"], 0)


if __name__ == "__main__":
    unittest.main()
