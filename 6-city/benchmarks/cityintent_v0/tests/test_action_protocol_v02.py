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


if __name__ == "__main__":
    unittest.main()
