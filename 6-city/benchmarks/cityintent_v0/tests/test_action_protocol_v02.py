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
    UtilityPlannerPolicy,
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

    def test_utility_candidate_choice_excludes_event_closed_place(self) -> None:
        scenario = {
            **self.scenario,
            "primary_agent": "aria",
            "agents": [
                {
                    "agent_id": "aria",
                    "start_location": "home",
                    "budget": 10,
                }
            ],
            "events": [
                {
                    "time": "10:00",
                    "type": "closure",
                    "location": "shop",
                    "effect": {"closed_until": "12:00"},
                }
            ],
            "success_conditions": [],
        }
        policy = UtilityPlannerPolicy(self.world, scenario, scenario["agents"][0])

        self.assertEqual(
            policy.choose_from_candidates(["shop", "cafe"], self.state()),
            "cafe",
        )

    def test_evidence_labels_ignore_separator_formatting_only(self) -> None:
        state = self.state()
        state.services.append(
            {"location": "shop", "service": "check-in", "time": state.time}
        )
        condition = {
            "type": "use_service_at",
            "location": "shop",
            "service": "check_in",
        }

        self.assertEqual(condition_success(condition, state, self.scenario), 1.0)
        self.assertEqual(len(condition_evidence(condition, state)), 1)
        self.assertEqual(
            condition_success(
                {**condition, "service": "prescription_pickup"},
                state,
                self.scenario,
            ),
            0.0,
        )

    def test_purchase_at_accepts_any_item_but_requires_purchase_evidence(self) -> None:
        state = self.state()
        condition = {"type": "purchase_at", "location": "cafe"}
        self.assertEqual(condition_success(condition, state, self.scenario), 0.0)

        state.purchases.append(
            {"location": "cafe", "item": "coffee", "time": state.time}
        )
        self.assertEqual(condition_success(condition, state, self.scenario), 1.0)
        self.assertEqual(len(condition_evidence(condition, state)), 1)

    def test_obtain_at_accepts_purchase_or_service_before_deadline(self) -> None:
        condition = {
            "type": "obtain_at",
            "location": "shop",
            "item": "prescription",
            "service": "prescription_pickup",
            "deadline": "10:10",
        }
        purchased = self.state()
        purchased.purchases.append(
            {"location": "shop", "item": "prescription", "time": parse_time("10:05")}
        )
        serviced = self.state()
        serviced.services.append(
            {
                "location": "shop",
                "service": "prescription pickup",
                "time": parse_time("10:05"),
            }
        )
        late = self.state()
        late.services.append(
            {
                "location": "shop",
                "service": "prescription_pickup",
                "time": parse_time("10:11"),
            }
        )

        self.assertEqual(condition_success(condition, purchased, self.scenario), 1.0)
        self.assertEqual(condition_success(condition, serviced, self.scenario), 1.0)
        self.assertEqual(condition_success(condition, late, self.scenario), 0.0)
        self.assertEqual(condition_evidence(condition, purchased)[0]["evidence_kind"], "purchase")

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

    def test_presence_without_counterpart_interaction_is_not_copresence(self) -> None:
        scenario = {
            **self.scenario,
            "agents": [
                {"agent_id": "aria", "start_location": "home"},
                {"agent_id": "ben", "start_location": "home"},
            ],
            "success_conditions": [
                {
                    "id": "meet_ben",
                    "type": "co_presence",
                    "role": "outcome",
                    "agents": ["aria", "ben"],
                    "location_any_of": ["cafe"],
                    "time_window": ["10:00", "11:00"],
                    "weight": 1.0,
                }
            ],
        }
        state = self.state()
        execute_action(self.world, scenario, state, Action("move", target="cafe"))
        execute_action(self.world, scenario, state, Action("enter", target="cafe"))

        condition = scenario["success_conditions"][0]
        self.assertEqual(condition_success(condition, state, scenario), 0)
        self.assertEqual(condition_evidence(condition, state), [])

    def test_copresence_requires_message_when_scenario_declares_coordination(self) -> None:
        scenario = {
            **self.scenario,
            "agents": [
                {"agent_id": "aria", "start_location": "home"},
                {"agent_id": "ben", "start_location": "home"},
            ],
            "success_conditions": [
                {
                    "id": "confirm",
                    "type": "send_message",
                    "role": "outcome",
                    "to": "ben",
                    "weight": 0.2,
                },
                {
                    "id": "meet_ben",
                    "type": "co_presence",
                    "role": "outcome",
                    "agents": ["aria", "ben"],
                    "location_any_of": ["cafe"],
                    "time_window": ["10:00", "11:00"],
                    "weight": 0.8,
                },
            ],
        }
        rejected = self.state()
        execute_action(self.world, scenario, rejected, Action("move", target="cafe"))
        execute_action(self.world, scenario, rejected, Action("enter", target="cafe"))
        execute_action(
            self.world, scenario, rejected, Action("interact", to="ben", minutes=5)
        )
        self.assertFalse(rejected.interactions)
        self.assertIn(
            "interaction_target_unavailable",
            [item["kind"] for item in rejected.violations],
        )

        accepted = self.state()
        execute_action(self.world, scenario, accepted, Action("message", to="ben"))
        execute_action(self.world, scenario, accepted, Action("move", target="cafe"))
        execute_action(self.world, scenario, accepted, Action("enter", target="cafe"))
        execute_action(
            self.world, scenario, accepted, Action("interact", to="ben", minutes=5)
        )
        condition = scenario["success_conditions"][1]
        self.assertEqual(condition_success(condition, accepted, scenario), 1)
        self.assertEqual(condition_evidence(condition, accepted)[0]["location"], "cafe")
        self.assertFalse(accepted.violations)

    def test_service_completion_honors_deadline(self) -> None:
        condition = {
            "type": "use_service_at",
            "location": "shop",
            "service": "child_pickup",
            "deadline": "10:15",
        }
        before = self.state()
        execute_action(self.world, self.scenario, before, Action("move", target="shop"))
        execute_action(self.world, self.scenario, before, Action("enter", target="shop"))
        execute_action(
            self.world,
            self.scenario,
            before,
            Action("use_service", target="shop", service="child_pickup", minutes=2),
        )
        self.assertEqual(condition_success(condition, before, self.scenario), 1)

        after = self.state()
        after.time = parse_time("10:16")
        after.location = "shop"
        after.inside_location = "shop"
        execute_action(
            self.world,
            self.scenario,
            after,
            Action("use_service", target="shop", service="child_pickup", minutes=2),
        )
        self.assertEqual(condition_success(condition, after, self.scenario), 0)
        self.assertEqual(condition_evidence(condition, after), [])

    def test_task_completion_cannot_be_replaced_by_constraint_points(self) -> None:
        scenario = {
            **self.scenario,
            "agents": [{"agent_id": "aria", "start_location": "home"}],
            "success_conditions": [
                {
                    "id": "pickup",
                    "type": "use_service_at",
                    "role": "outcome",
                    "location": "shop",
                    "service": "child_pickup",
                    "weight": 0.5,
                },
                {
                    "id": "budget",
                    "type": "budget_at_least",
                    "role": "constraint",
                    "min_remaining": 0,
                    "weight": 0.5,
                },
            ],
        }
        scored = score_trace(self.world, scenario, self.state())
        self.assertEqual(scored["metrics"]["goal_completion"], 0.5)
        self.assertEqual(scored["metrics"]["task_completion"], 0)
        self.assertEqual(scored["metrics"]["constraint_satisfaction"], 1)


if __name__ == "__main__":
    unittest.main()
