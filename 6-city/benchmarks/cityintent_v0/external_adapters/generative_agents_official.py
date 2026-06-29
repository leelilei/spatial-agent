"""Adapter for the verified Generative Agents memory/planning prompts."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from .adapter_common import (
    ADAPTER_DIR,
    PROJECT_ROOT,
    OfficialAdapterBase,
    compile_named_function,
    format_time,
    render_official_file_prompt,
    verify_official_checkout,
)


MANIFEST_PATH = ADAPTER_DIR / "generative_agents_manifest.json"
DEFAULT_ROOT = PROJECT_ROOT / "tmp" / "external" / "generative_agents"


class GenerativeAgentsOfficialPlannerAdapter(OfficialAdapterBase):
    """Use Smallville's official daily-plan, reflection, and revision prompts."""

    agent_id = "generative_agents_official_planner"
    framework_name = "Generative Agents"

    def __init__(
        self,
        world: Any,
        scenario: dict[str, Any],
        primary: dict[str, Any],
        llm_config: Path | None = None,
    ) -> None:
        root = Path(
            os.environ.get("CITYAGENCY_GENERATIVE_AGENTS_ROOT", DEFAULT_ROOT)
        ).resolve()
        provenance = verify_official_checkout(root, MANIFEST_PATH)
        prompt_root = root / "reverie" / "backend_server" / "persona" / "prompt_template"
        self.generate_prompt = compile_named_function(
            prompt_root / "gpt_structure.py", "generate_prompt"
        )
        self.daily_template = prompt_root / "v2" / "daily_planning_v6.txt"
        self.revision_template = prompt_root / "v2" / "new_decomp_schedule_v1.txt"
        self.insight_template = prompt_root / "v2" / "insight_and_evidence_v1.txt"
        self.original_plan: list[dict[str, Any]] = []
        self.reflections: list[str] = []
        self.configure(world, scenario, primary, llm_config, provenance)
        self._generate_initial_plan()

    def _commonset(self) -> str:
        return "\n\n".join(
            [
                self.person_description(),
                self.network_description(),
                "Public context: " + self.scenario.get("public_context", ""),
            ]
        )

    def _adapter_override(self, state: Any | None = None) -> str:
        episode = self.scenario["episode"]
        observation = ""
        if state is not None:
            observation = "\nCurrent authoritative observation: " + self.state_description(state)
        return f"""
CITYAGENCY PLAN ADAPTER:
Plan only {episode['start_time']}-{episode['end_time']}; ignore generic waking and sleeping.
The private goal and success conditions have priority. Use only exact facility ids.
Return only JSON with this schema:
{{"reflection":"brief memory-based reasoning","plan":[
  {{"time":"HH:MM","activity":"description","kind":"move","target":"facility_id","path":null}},
  {{"time":"HH:MM","activity":"description","kind":"dwell","minutes":15}},
  {{"time":"HH:MM","activity":"description","kind":"message","to":"agent_id","content":"text"}},
  {{"time":"HH:MM","activity":"description","kind":"interact","to":"agent_id","minutes":5}}
]}}
Do not report success in advance. The environment executes and validates actions.
Success conditions: {json.dumps(self.scenario.get('success_conditions', []), ensure_ascii=False)}
{observation}
""".strip()

    def _generate_initial_plan(self) -> None:
        start = self.scenario["episode"]["start_time"]
        args = [
            self._commonset(),
            self.primary["persona"],
            "Monday June 29, 2026 " + start,
            self.primary["agent_id"],
            start,
        ]
        prompt = render_official_file_prompt(
            self.generate_prompt, args, self.daily_template
        )
        prompt += "\n\n" + self._adapter_override()
        parsed = self.complete_json(
            "You are the planning module from Generative Agents (Smallville).",
            prompt,
        )
        self.original_plan = self.validate_actions(parsed.get("plan", []))
        self.queue = list(self.original_plan)
        reflection = str(parsed.get("reflection", "")).strip()
        if reflection:
            self.reflections.append(reflection)

    def _reflect(self, state: Any) -> str:
        statements: list[str] = []
        statements.extend(self.primary.get("memory_seeds", []))
        statements.extend(
            json.dumps(event, ensure_ascii=False) for event in self.visible_events(state)
        )
        statements.extend(
            json.dumps(violation, ensure_ascii=False) for violation in state.violations
        )
        numbered = "\n".join(
            f"{index}. {statement}" for index, statement in enumerate(statements, 1)
        ) or "1. No new event."
        prompt = render_official_file_prompt(
            self.generate_prompt,
            [numbered, self.primary["agent_id"]],
            self.insight_template,
        )
        prompt += '\n\nReturn only JSON: {"insights":["high-level insight"]}'
        parsed = self.complete_json(
            "You are the reflection module from Generative Agents (Smallville).",
            prompt,
        )
        insights = parsed.get("insights", [])
        if isinstance(insights, list):
            reflection = " | ".join(str(value) for value in insights)
        else:
            reflection = str(insights)
        if reflection:
            self.reflections.append(reflection)
        return reflection

    def _replan(self, state: Any) -> None:
        reflection = self._reflect(state)
        start = format_time(state.time)
        end = self.scenario["episode"]["end_time"]
        event_text = json.dumps(
            {
                "events": self.visible_events(state),
                "violations": state.violations,
                "reflection": reflection,
                "state": json.loads(self.state_description(state)),
            },
            ensure_ascii=False,
        )
        args = [
            self.primary["agent_id"],
            start,
            end,
            json.dumps(self.original_plan, ensure_ascii=False),
            self.primary["agent_id"],
            event_text,
            "0",
            self.primary["agent_id"],
            start,
            end,
            end,
            "1)",
        ]
        prompt = render_official_file_prompt(
            self.generate_prompt, args, self.revision_template
        )
        prompt += "\n\n" + self._adapter_override(state)
        parsed = self.complete_json(
            "You are revising a Generative Agents schedule after a new event.",
            prompt,
        )
        revised = self.validate_actions(parsed.get("plan", []))
        if revised:
            self.queue = revised
        self.record_observations(state, changed=bool(revised))

    def next_action(self, state: Any) -> dict[str, Any]:
        if self.needs_replan(state):
            self._replan(state)
        return self.next_queued_action(state)
