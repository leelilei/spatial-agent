"""CityIntent adapter for SOTOPIA's verified official LLMAgent action policy."""

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
    compile_named_function,
    extract_function_string,
    verify_official_checkout,
)


MANIFEST_PATH = ADAPTER_DIR / "sotopia_manifest.json"
DEFAULT_ROOT = PROJECT_ROOT / "tmp" / "external" / "sotopia"


class SOTOPIAOfficialLLMAgentAdapter(OfficialAdapterBase):
    """Use SOTOPIA's official per-turn private-goal action prompt."""

    agent_id = "sotopia_official_llm_agent"
    framework_name = "SOTOPIA"

    def __init__(
        self,
        world: Any,
        scenario: dict[str, Any],
        primary: dict[str, Any],
        llm_config: Path | None = None,
    ) -> None:
        root = Path(os.environ.get("CITYAGENCY_SOTOPIA_ROOT", DEFAULT_ROOT)).resolve()
        provenance = verify_official_checkout(root, MANIFEST_PATH)
        generate_source = root / "sotopia" / "generation_utils" / "generate.py"
        self.fill_template = compile_named_function(generate_source, "fill_template")
        self.action_template = extract_function_string(
            generate_source,
            "agenerate_action",
            "Imagine you are {agent}",
        )
        self.turn_number = 0
        self.configure(world, scenario, primary, llm_config, provenance)

    def _history(self, state: Any) -> str:
        lines = [
            "Here is the context of the interaction:",
            self.person_description(),
            self.network_description(),
            "Success conditions: "
            + json.dumps(self.scenario.get("success_conditions", []), ensure_ascii=False),
            f"Episode: {self.scenario['episode']['start_time']}-{self.scenario['episode']['end_time']}",
            "Current authoritative observation: " + self.state_description(state),
        ]
        for entry in state.actions[-6:]:
            action = entry["action"]
            lines.append(
                f"Turn {entry['step']}: at {entry['start_location']} chose "
                f"{action.get('kind')} target={action.get('target')} minutes={action.get('minutes')}; "
                f"ended at {entry['end_location']} with violations={entry['violations']}"
            )
        return "\n".join(lines)

    @staticmethod
    def _format_instructions() -> str:
        return (
            '{"action_type":"action|speak|non-verbal communication|none|leave",'
            '"argument":"one command string","to":[]}'
        )

    def _adapter_override(self) -> str:
        return """
CITYAGENCY ACTION ADAPTER:
The environment is authoritative. Choose exactly one outer SOTOPIA AgentAction.
For physical city behavior use action_type "action" and one argument command:
- move FACILITY_ID
- enter FACILITY_ID
- use_service FACILITY_ID SERVICE_NAME MINUTES
- buy FACILITY_ID ITEM_NAME MINUTES
- dwell MINUTES
- message AGENT_ID: TEXT
- interact AGENT_ID MINUTES
- finish
- abandon REASON
Use only exact facility ids from the observation. Moving only arrives outside;
enter before buy/use_service/dwell. Only buy/use_service spends money and proves
consumption. Never claim an action succeeded; the environment will execute it.
Return only the outer JSON object.
""".strip()

    def _parse_command(self, action_type: str, argument: Any, recipients: Any) -> dict[str, Any]:
        text = str(argument or "").strip()
        if action_type in {"none", "leave"} or text.lower() == "finish":
            return {"kind": "finish", "reason": "SOTOPIA chose to stop or leave"}
        if text.lower().startswith("abandon "):
            return {"kind": "abandon", "reason": text.split(" ", 1)[1].strip()}
        if action_type == "speak":
            target = recipients[0] if isinstance(recipients, list) and recipients else None
            return {
                "kind": "message",
                "to": target,
                "content": text,
                "reason": "SOTOPIA speak action",
            }
        if action_type == "non-verbal communication":
            target = recipients[0] if isinstance(recipients, list) and recipients else None
            return {
                "kind": "interact",
                "to": target,
                "minutes": 2,
                "reason": f"SOTOPIA non-verbal action: {text}",
            }
        move = re.fullmatch(r"move\s+([A-Za-z0-9_-]+)", text, flags=re.IGNORECASE)
        if move:
            return {
                "kind": "move",
                "target": move.group(1),
                "reason": "SOTOPIA physical action",
            }
        enter = re.fullmatch(r"enter\s+([A-Za-z0-9_-]+)", text, flags=re.IGNORECASE)
        if enter:
            return {
                "kind": "enter",
                "target": enter.group(1),
                "reason": "SOTOPIA physical action",
            }
        service = re.fullmatch(
            r"use_service\s+([A-Za-z0-9_-]+)\s+([A-Za-z0-9_-]+)\s+(\d+)",
            text,
            flags=re.IGNORECASE,
        )
        if service:
            return {
                "kind": "use_service",
                "target": service.group(1),
                "service": service.group(2),
                "minutes": int(service.group(3)),
                "reason": "SOTOPIA physical action",
            }
        buy = re.fullmatch(
            r"buy\s+([A-Za-z0-9_-]+)\s+([A-Za-z0-9_-]+)\s+(\d+)",
            text,
            flags=re.IGNORECASE,
        )
        if buy:
            return {
                "kind": "buy",
                "target": buy.group(1),
                "item": buy.group(2),
                "minutes": int(buy.group(3)),
                "reason": "SOTOPIA physical action",
            }
        dwell = re.fullmatch(r"dwell\s+(\d+)", text, flags=re.IGNORECASE)
        if dwell:
            return {
                "kind": "dwell",
                "minutes": int(dwell.group(1)),
                "reason": "SOTOPIA physical action",
            }
        message = re.fullmatch(
            r"message\s+([A-Za-z0-9_-]+)\s*:\s*(.+)", text, flags=re.IGNORECASE
        )
        if message:
            return {
                "kind": "message",
                "to": message.group(1),
                "content": message.group(2),
                "reason": "SOTOPIA physical action",
            }
        interact = re.fullmatch(
            r"interact\s+([A-Za-z0-9_-]+)\s+(\d+)", text, flags=re.IGNORECASE
        )
        if interact:
            return {
                "kind": "interact",
                "to": interact.group(1),
                "minutes": int(interact.group(2)),
                "reason": "SOTOPIA physical action",
            }
        return {
            "kind": "finish",
            "reason": f"unparseable SOTOPIA AgentAction argument: {text}",
        }

    def next_action(self, state: Any) -> dict[str, Any]:
        self.turn_number += 1
        prompt = self.fill_template(
            self.action_template,
            agent=self.primary["agent_id"],
            history=self._history(state),
            turn_number=str(self.turn_number),
            action_list="action speak non-verbal communication none leave",
            goal=self.primary["private_intention"],
            format_instructions=self._format_instructions(),
        )
        prompt += "\n\n" + self._adapter_override()
        parsed = self.complete_json(
            "You are the official SOTOPIA-style LLMAgent acting one turn toward a private goal.",
            prompt,
        )
        action = self._parse_command(
            str(parsed.get("action_type", "none")),
            parsed.get("argument", ""),
            parsed.get("to", []),
        )
        validated = self.validate_actions([action])
        self.record_observations(state, changed=bool(validated))
        if not validated:
            action = {"kind": "finish", "reason": "invalid SOTOPIA AgentAction"}
        else:
            action = validated[0]
        action["raw_response"] = self.last_raw_response
        return action
