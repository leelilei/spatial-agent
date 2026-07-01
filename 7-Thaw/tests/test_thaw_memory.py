from __future__ import annotations

import sys
import unittest
from pathlib import Path


SIM_DIR = Path(__file__).resolve().parents[2] / "5-Telephone" / "sim"
sys.path.insert(0, str(SIM_DIR))

from memories import GAReflectionMemory, ThawGAReflectionMemory  # noqa: E402
from society import demo_world  # noqa: E402


class FakeLLM:
    def complete_json(self, system: str, user: str) -> dict:
        return {"insights": ["The old plan is still widely repeated."]}


class ThawMemoryTests(unittest.TestCase):
    def test_zero_forgetting_matches_ga_retrievable_content(self) -> None:
        llm = FakeLLM()
        ga = GAReflectionMemory(llm=llm)
        thaw = ThawGAReflectionMemory(llm=llm, forget_rate=0.0)
        for round_idx in range(3):
            event = {"round": round_idx, "text": f"repair drive message {round_idx}"}
            thaw.begin_round(round_idx)
            ga.observe(event.copy())
            thaw.observe(event.copy())
            ga.consolidate()
            thaw.consolidate()
        self.assertEqual(ga.events, thaw.events)
        self.assertEqual(ga.reflections, thaw.reflections)
        self.assertEqual(ga.retrieve("repair drive"), thaw.retrieve("repair drive"))

    def test_old_items_decay_but_fresh_correction_survives(self) -> None:
        memory = ThawGAReflectionMemory(
            llm=None, forget_rate=0.5, forget_floor=0.2
        )
        memory.begin_round(0)
        memory.observe({"round": 0, "text": "The drive is Saturday."})
        memory.begin_round(1)  # 1.0 -> 0.5
        memory.begin_round(2)  # 0.5 -> 0.25
        memory.begin_round(3)  # 0.25 -> 0.125 -> forgotten
        self.assertEqual(memory.events, [])

        memory.observe({"round": 3, "text": "Update: the drive is Sunday."})
        self.assertIn("Sunday", memory.retrieve("drive"))
        self.assertEqual(memory._event_strengths, [1.0])

    def test_rehearsal_creates_a_fresh_copy(self) -> None:
        memory = ThawGAReflectionMemory(
            llm=None, forget_rate=0.8, forget_floor=0.1
        )
        memory.begin_round(0)
        memory.observe({"round": 0, "text": "The drive is Saturday."})
        memory.begin_round(1)
        memory.observe({"round": 1, "text": "A neighbor repeats Saturday."})
        memory.begin_round(2)
        texts = [event["text"] for event in memory.events]
        self.assertNotIn("The drive is Saturday.", texts)
        self.assertIn("A neighbor repeats Saturday.", texts)

    def test_broadcast_initial_fact_is_actually_observed(self) -> None:
        world = demo_world(
            lambda: ThawGAReflectionMemory(llm=None),
            agent_count=4,
            initial_fact_scope="broadcast",
        )
        for agent in world.agents:
            snapshot = agent.memory.snapshot()
            self.assertEqual(snapshot["n_events"], 1)
            self.assertTrue(snapshot["events"][0]["injected_initial"])
            self.assertIn("Saturday", snapshot["events"][0]["text"])


if __name__ == "__main__":
    unittest.main()
