"""Adapter for AgentSociety's verified official planning and mobility blocks."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

from .adapter_common import (
    ADAPTER_DIR,
    PROJECT_ROOT,
    OfficialAdapterBase,
    extract_assigned_string,
    format_time,
    verify_official_checkout,
)


MANIFEST_PATH = ADAPTER_DIR / "agentsociety_manifest.json"
DEFAULT_ROOT = PROJECT_ROOT / "tmp" / "external" / "agentsociety"


class AgentSocietyOfficialPlanBlocksAdapter(OfficialAdapterBase):
    """Run AgentSociety's TPB guidance and typed detailed-plan prompts."""

    agent_id = "agentsociety_official_plan_blocks"
    framework_name = "AgentSociety"

    def __init__(
        self,
        world: Any,
        scenario: dict[str, Any],
        primary: dict[str, Any],
        llm_config: Path | None = None,
    ) -> None:
        root = Path(os.environ.get("CITYAGENCY_AGENTSOCIETY_ROOT", DEFAULT_ROOT)).resolve()
        provenance = verify_official_checkout(root, MANIFEST_PATH)
        block_root = (
            root
            / "packages"
            / "agentsociety"
            / "agentsociety"
            / "cityagent"
            / "blocks"
        )
        self.guidance_template = extract_assigned_string(
            block_root / "plan_block.py", "GUIDANCE_SELECTION_PROMPT"
        )
        self.detail_template = extract_assigned_string(
            block_root / "plan_block.py", "DETAILED_PLAN_PROMPT"
        )
        self.place_template = extract_assigned_string(
            block_root / "mobility_block.py", "PLACE_ANALYSIS_PROMPT"
        )
        self.guidance_history: list[dict[str, Any]] = []
        self.configure(world, scenario, primary, llm_config, provenance)
        self._generate_plan(None)

    def _location_options(self) -> str:
        return "\n".join(
            f"- {location['id']}: type={location.get('type')}; "
            f"tags={','.join(location.get('tags', []))}; "
            f"cost={location.get('typical_cost', 0)}"
            for location in self.world.world["locations"]
        )

    def _other_info(self, state: Any | None) -> str:
        parts = [
            self.scenario.get("public_context", ""),
            "Private goal: " + self.primary["private_intention"],
            "Success conditions: "
            + json.dumps(self.scenario.get("success_conditions", []), ensure_ascii=False),
            self.network_description(),
        ]
        if state is not None:
            parts.append("Authoritative state: " + self.state_description(state))
        return "\n".join(parts)

    @staticmethod
    def _render_agent_society_complex(
        template: str, context: dict[str, Any], profile: dict[str, Any]
    ) -> str:
        expressions: dict[str, str] = {}

        def protect(match: re.Match[str]) -> str:
            marker = f"__EXPR_{len(expressions)}__"
            expressions[marker] = match.group(1)
            return marker

        rendered = re.sub(
            r"\$\{((?:context|profile)\.[^}]+)\}", protect, template
        ).format()
        for marker, expression in expressions.items():
            scope, key = expression.split(".", 1)
            source = context if scope == "context" else profile
            rendered = rendered.replace(marker, str(source.get(key, "Don't know")))
        return rendered

    def _guidance_prompt(self, state: Any | None) -> str:
        current_location = state.location if state is not None else self.primary["start_location"]
        current_time = (
            format_time(state.time)
            if state is not None
            else self.scenario["episode"]["start_time"]
        )
        return self.guidance_template.format(
            weather="not modeled",
            temperature="not modeled",
            other_info=self._other_info(state),
            current_need=self.primary["private_intention"],
            current_location=current_location,
            current_time=current_time,
            consumption_level=f"budget {state.budget if state is not None else self.primary['budget']}",
            occupation=self.primary["persona"],
            age="not specified",
            emotion_types="goal-focused",
            thought=" | ".join(self.primary.get("memory_seeds", [])),
            options=self._location_options(),
        )

    def _detail_prompt(
        self, guidance: dict[str, Any], state: Any | None
    ) -> str:
        context = {
            "weather": "not modeled",
            "temperature": "not modeled",
            "other_information": self._other_info(state),
            "plan_target": guidance.get("selected_option", self.primary["private_intention"]),
            "current_position": state.location if state is not None else self.primary["start_location"],
            "current_time": format_time(state.time)
            if state is not None
            else self.scenario["episode"]["start_time"],
            "current_thought": guidance.get("evaluation", {}).get("reasoning", ""),
            "max_plan_steps": 8,
        }
        profile = {
            "consumption": f"budget {state.budget if state is not None else self.primary['budget']}",
            "occupation": self.primary["persona"],
            "age": "not specified",
            "emotion_types": "goal-focused",
        }
        prompt = self._render_agent_society_complex(
            self.detail_template, context, profile
        )
        prompt += """

CITYAGENCY STEP EXTENSION:
Keep AgentSociety's official plan.target and step intention/type fields. Add an
"action" object to every executable step using exactly one of:
{"kind":"move","target":"exact_facility_id","path":null}
{"kind":"enter","target":"exact_facility_id"}
{"kind":"use_service","target":"exact_facility_id","service":"meal or access","minutes":5}
{"kind":"buy","target":"exact_facility_id","item":"item name","minutes":5}
{"kind":"dwell","minutes":15}
{"kind":"message","to":"agent_id","content":"text"}
{"kind":"interact","to":"agent_id","minutes":5}
Moving only arrives outside. Enter before buy/use_service/dwell. Only
buy/use_service spends money and proves consumption. Do not claim success; the
environment executes and validates every action.
Return only JSON.
"""
        return prompt

    def _place_action(self, plan: dict[str, Any], step: dict[str, Any]) -> dict[str, Any] | None:
        prompt = self.place_template.format(
            plan=json.dumps(plan, ensure_ascii=False),
            intention=step.get("intention", ""),
            other_info=self.scenario.get("public_context", ""),
            place_list=list(self.world.locations),
        )
        parsed = self.complete_json(
            "You are AgentSociety's official mobility place-analysis block.", prompt
        )
        target = str(parsed.get("place_type", ""))
        if target not in self.world.locations:
            return None
        return {
            "kind": "move",
            "target": target,
            "reason": "AgentSociety official PlaceAnalysisPrompt",
        }

    def _actions_from_plan(self, plan: Any) -> list[dict[str, Any]]:
        if not isinstance(plan, dict) or not isinstance(plan.get("steps"), list):
            return []
        actions: list[dict[str, Any]] = []
        for step in plan["steps"]:
            if not isinstance(step, dict):
                continue
            candidate = self.validate_actions([step.get("action")])
            if candidate:
                candidate[0]["reason"] = (
                    "AgentSociety official plan step: " + str(step.get("intention", ""))
                )
                actions.extend(candidate)
            elif step.get("type") == "mobility":
                fallback = self._place_action(plan, step)
                if fallback:
                    actions.extend(
                        [
                            fallback,
                            {
                                "kind": "enter",
                                "target": fallback["target"],
                                "reason": "enter AgentSociety-selected destination",
                            },
                        ]
                    )
        return actions

    def _generate_plan(self, state: Any | None) -> bool:
        guidance = self.complete_json(
            "You are AgentSociety's official Theory-of-Planned-Behavior guidance block.",
            self._guidance_prompt(state),
        )
        self.guidance_history.append(guidance)
        parsed = self.complete_json(
            "You are AgentSociety's official detailed planning block.",
            self._detail_prompt(guidance, state),
        )
        actions = self._actions_from_plan(parsed.get("plan", {}))
        if actions:
            self.queue = actions
        if state is not None:
            self.record_observations(state, changed=bool(actions))
        return bool(actions)

    def next_action(self, state: Any) -> dict[str, Any]:
        if self.needs_replan(state):
            self._generate_plan(state)
        return self.next_queued_action(state)
