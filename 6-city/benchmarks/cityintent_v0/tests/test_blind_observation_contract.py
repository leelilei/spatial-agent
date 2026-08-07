from __future__ import annotations

import sys
import unittest
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

from run_baseline_traces import (  # noqa: E402
    Action,
    APILLMDirectActor,
    APILLMPlanThenAct,
    APILLMReActToolPolicy,
    CityWorld,
    TraceState,
    execute_action,
    parse_time,
)


class BlindObservationContractTest(unittest.TestCase):
    def setUp(self) -> None:
        self.world = CityWorld(
            {
                "locations": [
                    {
                        "id": "home",
                        "name": "Home",
                        "type": "home",
                        "tags": [],
                        "open": ["00:00", "23:59"],
                        "typical_cost": 0,
                    },
                    {
                        "id": "cafe",
                        "name": "Cafe",
                        "type": "cafe",
                        "tags": ["meeting"],
                        "open": ["09:00", "18:00"],
                        "typical_cost": 3,
                    },
                ],
                "edges": [{"from": "home", "to": "cafe", "minutes": 5}],
            }
        )
        self.primary = {
            "agent_id": "aria",
            "persona": "Resident",
            "private_intention": "Meet Ben inside the cafe before noon.",
            "start_location": "home",
            "budget": 20,
            "known_locations": ["home", "cafe"],
            "memory_seeds": [],
        }
        self.scenario = {
            "scenario_id": "blind_contract_test",
            "title": "Blind contract test",
            "family": "social_coordination_copresence",
            "public_context": "Only observable action evidence counts.",
            "episode": {"start_time": "10:00", "end_time": "12:00", "max_steps": 8},
            "primary_agent": "aria",
            "events": [],
            "agents": [
                self.primary,
                {
                    "agent_id": "ben",
                    "persona": "Friend",
                    "start_location": "cafe",
                },
            ],
            "success_conditions": [
                {
                    "id": "hidden_meeting_key",
                    "type": "co_presence",
                    "agents": ["aria", "ben"],
                    "location_any_of": ["cafe"],
                    "time_window": ["10:30", "12:00"],
                }
            ],
            "benchmark_metadata": {
                "observation_contract": "intent_only_v1",
                "expose_verifier_conditions": False,
            },
        }
        self.state = TraceState(
            scenario_id=self.scenario["scenario_id"],
            agent_id="aria",
            agent_type="api_llm_react_tool_policy",
            time=parse_time("10:00"),
            end_time=parse_time("12:00"),
            location="home",
            budget=20,
            inside_location="home",
        )

    def policy(self, cls):
        policy = cls.__new__(cls)
        policy.world = self.world
        policy.scenario = self.scenario
        policy.primary = self.primary
        return policy

    def test_direct_actor_hides_evaluator_conditions(self) -> None:
        observation = self.policy(APILLMDirectActor).build_observation(self.state)

        self.assertNotIn("success_conditions", observation["scenario"])
        self.assertIn("evaluation_contract", observation["scenario"])
        self.assertNotIn("hidden_meeting_key", str(observation))

    def test_plan_then_act_hides_conditions_and_social_recipe(self) -> None:
        observation = self.policy(APILLMPlanThenAct).build_plan_observation()

        self.assertNotIn("success_conditions", observation["scenario"])
        self.assertEqual(observation["social_success_recipes"], [])
        self.assertNotIn("hidden_meeting_key", str(observation))

    def test_plan_does_not_see_future_public_event(self) -> None:
        self.scenario["events"] = [
            {
                "time": "10:30",
                "type": "future_closure",
                "location": "cafe",
                "visibility": "public",
                "effect": {"closed_until": "12:00"},
            }
        ]

        plan_observation = self.policy(APILLMPlanThenAct).build_plan_observation()
        self.assertEqual(plan_observation["scenario"]["events"], [])

        self.state.time = parse_time("10:31")
        direct_observation = self.policy(APILLMDirectActor).build_observation(self.state)
        self.assertEqual(
            direct_observation["visible_events"][0]["type"], "future_closure"
        )

    def test_react_hides_condition_status_and_derived_next_action(self) -> None:
        policy = self.policy(APILLMReActToolPolicy)
        self.state.location = "cafe"
        self.state.inside_location = "cafe"
        observation = policy.build_observation(self.state)

        self.assertEqual(observation["react_state"]["condition_status"], [])
        self.assertEqual(observation["react_state"]["unfinished_conditions"], [])
        self.assertIsNone(observation["react_state"]["required_next_action"])
        self.assertNotIn("hidden_meeting_key", str(observation))

    def test_historical_scenario_defaults_to_visible_conditions(self) -> None:
        self.scenario.pop("benchmark_metadata")
        observation = self.policy(APILLMDirectActor).build_observation(self.state)

        self.assertEqual(
            observation["scenario"]["success_conditions"],
            self.scenario["success_conditions"],
        )

    def test_recall_contract_hides_then_reveals_private_memories(self) -> None:
        self.primary["memory_seeds"] = ["The office focus room is my reliable fallback."]
        self.scenario["benchmark_metadata"]["memory_access_contract"] = "recall_required_v1"
        policy = self.policy(APILLMDirectActor)

        before = policy.build_observation(self.state)
        self.assertEqual(before["primary_agent"]["memory_seeds"], [])
        self.assertEqual(before["current_state"]["recalled_memories"], [])

        execute_action(
            self.world,
            self.scenario,
            self.state,
            Action("recall", query="reliable fallback"),
        )
        after = policy.build_observation(self.state)
        self.assertEqual(
            after["current_state"]["recalled_memories"],
            self.primary["memory_seeds"],
        )

        plan = self.policy(APILLMPlanThenAct).build_plan_observation()
        self.assertEqual(plan["primary_agent"]["memory_seeds"], [])
        self.assertIn("will not be replanned", plan["primary_agent"]["memory_access"])


if __name__ == "__main__":
    unittest.main()
