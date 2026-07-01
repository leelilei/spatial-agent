"""Adapter for the official GATSim planning prompt and activity-plan schema.

This is intentionally labelled ``adapted_official_planner``. It verifies and
executes GATSim's pinned ``generate_prompt`` implementation and official plan
templates, while CityIntent retains ownership of the world and action executor.
It is not a claim that the complete native GATSim backend runs in micro_city_v0.
"""

from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable
from unittest.mock import patch


ADAPTER_DIR = Path(__file__).resolve().parent
BENCHMARK_ROOT = ADAPTER_DIR.parent
PROJECT_ROOT = ADAPTER_DIR.parents[2]
RESEARCH_ROOT = ADAPTER_DIR.parents[3]
DEFAULT_GATSIM_ROOT = PROJECT_ROOT / "tmp" / "external" / "gatsim"
MANIFEST_PATH = ADAPTER_DIR / "gatsim_manifest.json"
STANDARD_LLM_DIR = RESEARCH_ROOT / "0-Tools" / "research-standard"


def load_manifest() -> dict[str, Any]:
    with MANIFEST_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_output(root: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(root), *args],
        text=True,
        encoding="utf-8",
        errors="replace",
    ).strip()


def normalize_repo(value: str) -> str:
    return value.strip().lower().removesuffix("/").removesuffix(".git")


def verify_official_checkout(root: Path) -> dict[str, Any]:
    manifest = load_manifest()
    if not (root / ".git").exists():
        raise RuntimeError(
            f"GATSim checkout not found at {root}. Run "
            "tools/setup_external_framework.py --framework gatsim first."
        )
    commit = git_output(root, "rev-parse", "HEAD")
    remote = git_output(root, "remote", "get-url", "origin")
    errors: list[str] = []
    if commit != manifest["source_commit"]:
        errors.append(f"commit {commit} != {manifest['source_commit']}")
    if normalize_repo(remote) != normalize_repo(manifest["source_repo"]):
        errors.append(f"remote {remote} != {manifest['source_repo']}")
    verified_files: list[str] = []
    for relative, expected_hash in manifest["required_files"].items():
        path = root / relative
        if not path.exists():
            errors.append(f"missing {relative}")
            continue
        actual_hash = file_sha256(path)
        if actual_hash != expected_hash:
            errors.append(f"sha256 mismatch for {relative}")
            continue
        verified_files.append(relative)
    if errors:
        raise RuntimeError("invalid GATSim checkout: " + "; ".join(errors))
    return {
        "source_repo": manifest["source_repo"],
        "source_commit": commit,
        "integration_level": manifest["integration_level"],
        "native_backend": bool(manifest["native_backend"]),
        "verified_files": verified_files,
    }


def load_official_generate_prompt(root: Path) -> Callable[[Any, str], str]:
    """Compile only GATSim's official generate_prompt function from llm.py."""

    source_path = root / "gatsim" / "agent" / "llm_modules" / "llm.py"
    tree = ast.parse(source_path.read_text(encoding="utf-8"), filename=str(source_path))
    nodes = [
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "generate_prompt"
    ]
    if len(nodes) != 1:
        raise RuntimeError("official GATSim generate_prompt function not found exactly once")
    module = ast.Module(body=nodes, type_ignores=[])
    ast.fix_missing_locations(module)
    namespace: dict[str, Any] = {}
    exec(compile(module, str(source_path), "exec"), namespace)
    return namespace["generate_prompt"]


def render_official_prompt(
    renderer: Callable[[Any, str], str], curr_input: Any, template: Path
) -> str:
    """Run GATSim's renderer while making its UTF-8 template portable on Windows."""

    original_open = open
    target = template.resolve()

    def open_utf8(file: Any, *args: Any, **kwargs: Any) -> Any:
        mode = kwargs.get("mode", args[0] if args else "r")
        if (
            isinstance(file, (str, os.PathLike))
            and Path(file).resolve() == target
            and "b" not in mode
        ):
            kwargs.setdefault("encoding", "utf-8")
        return original_open(file, *args, **kwargs)

    with patch("builtins.open", open_utf8):
        return renderer(curr_input, str(template))


def parse_time(value: str) -> int:
    hour, minute = value.split(":", 1)
    return int(hour) * 60 + int(minute)


def format_time(value: int) -> str:
    return f"{max(0, value) // 60:02d}:{max(0, value) % 60:02d}"


class GATSimOfficialPlannerAdapter:
    """Use GATSim's official activity-plan representation in CityIntent."""

    agent_id = "gatsim_official_planner"

    def __init__(
        self,
        world: Any,
        scenario: dict[str, Any],
        primary: dict[str, Any],
        llm_config: Path | None = None,
    ) -> None:
        if llm_config is None:
            raise ValueError("gatsim_official_planner requires --llm-config")
        external_root = Path(os.environ.get("CITYAGENCY_GATSIM_ROOT", DEFAULT_GATSIM_ROOT)).resolve()
        provenance = verify_official_checkout(external_root)
        self.official_generate_prompt = load_official_generate_prompt(external_root)
        self.daily_template = (
            external_root
            / "gatsim"
            / "agent"
            / "llm_modules"
            / "prompt_templates"
            / "generate_daily_activity_plan_v1.txt"
        )
        self.update_template = (
            external_root
            / "gatsim"
            / "agent"
            / "llm_modules"
            / "prompt_templates"
            / "update_daily_activity_plan_v1.txt"
        )
        if str(STANDARD_LLM_DIR) not in sys.path:
            sys.path.insert(0, str(STANDARD_LLM_DIR))
        from llm_client import LLM  # type: ignore

        self.llm = LLM(llm_config)
        self.world = world
        self.scenario = scenario
        self.primary = primary
        self.original_plan: list[list[Any]] = []
        self.revised_plans: list[dict[str, Any]] = []
        self.queue: list[list[Any]] = []
        self.wait_until: int | None = None
        self.observed_event_keys: set[str] = set()
        self.last_violation_count = 0
        self.last_raw_response = ""
        self.model_info = {
            "provider": self.llm.config.provider,
            "model": self.llm.config.model,
            "wire_api": self.llm.config.wire_api,
            "base_url": self.llm.config.base_url,
            "framework": "GATSim",
            "framework_agent": self.agent_id,
            "source_verified": True,
            **provenance,
        }
        self._generate_initial_plan()

    def _network_description(self) -> str:
        lines = [f"City network: {self.world.world.get('name', 'micro city')}", "Valid facilities:"]
        for location in self.world.world["locations"]:
            lines.append(
                f"- {location['id']}: type={location.get('type')}; tags={','.join(location.get('tags', []))}; "
                f"open={'-'.join(location.get('open', []))}; cost={location.get('typical_cost', 0)}"
            )
        lines.append("Travel edges in minutes:")
        for edge in self.world.world["edges"]:
            lines.append(f"- {edge['from']} <-> {edge['to']}: {edge['minutes']}")
        return "\n".join(lines)

    def _person_description(self) -> str:
        return "\n".join(
            [
                f"Name: {self.primary['agent_id']}",
                f"Persona: {self.primary['persona']}",
                f"Private intention: {self.primary['private_intention']}",
                f"Start facility: {self.primary['start_location']}",
                f"Budget: {self.primary['budget']} credits",
                "Known facilities: " + ", ".join(self.primary.get("known_locations", [])),
            ]
        )

    def _adapter_override(self) -> str:
        episode = self.scenario["episode"]
        return "\n".join(
            [
                "CITYAGENCY ADAPTER OVERRIDE (higher priority than generic day rules):",
                f"- Plan only the benchmark episode {episode['start_time']}-{episode['end_time']}.",
                "- Do not add waking, sleeping, commuting-to-work, or return-home activities unless required by the private intention.",
                "- Use only exact facility ids listed under Valid facilities.",
                "- Satisfy the private intention and explicit success conditions within time and budget.",
                "- The first plan item may begin at the current facility; later items should be destinations.",
                "- Preserve GATSim's official six-field activity schema and JSON output keys.",
                "Success conditions: " + json.dumps(self.scenario.get("success_conditions", []), ensure_ascii=False),
            ]
        )

    def _complete_json(self, system: str, prompt: str) -> dict[str, Any]:
        self.last_raw_response = self.llm.complete(system, prompt)
        if str(STANDARD_LLM_DIR) not in sys.path:
            sys.path.insert(0, str(STANDARD_LLM_DIR))
        from llm_client import parse_response_json  # type: ignore

        parsed = parse_response_json(self.last_raw_response)
        return parsed if isinstance(parsed, dict) else {}

    def _generate_initial_plan(self) -> None:
        args = [
            self.world.world.get("description", "Urban mobility simulation."),
            self._network_description(),
            self._person_description(),
            "Mon 2026-06-29 " + self.scenario["episode"]["start_time"],
            "No previous-day plan is available.",
            "No previous-day reflection is available.",
            self.scenario.get("public_context", ""),
            "\n".join(self.primary.get("memory_seeds", [])),
            "No chat summary is available.",
        ]
        prompt = render_official_prompt(self.official_generate_prompt, args, self.daily_template)
        prompt += "\n\n" + self._adapter_override()
        parsed = self._complete_json(
            "You are executing the official GATSim activity-planning format inside a controlled CityAgency episode.",
            prompt,
        )
        plan = parsed.get("plan", [])
        self.original_plan = self._validated_plan(plan)
        self.queue = list(self.original_plan)

    def _validated_plan(self, value: Any) -> list[list[Any]]:
        if not isinstance(value, list):
            return []
        valid: list[list[Any]] = []
        for activity in value:
            if not isinstance(activity, list) or len(activity) != 6:
                continue
            target = str(activity[0])
            if target not in self.world.locations:
                continue
            valid.append(activity)
        return valid

    def _visible_events(self, state: Any) -> list[dict[str, Any]]:
        return [
            event
            for event in self.scenario.get("events", [])
            if event.get("visibility", "public") == "public" and parse_time(event["time"]) <= state.time
        ]

    def _event_key(self, event: dict[str, Any]) -> str:
        return f"{event.get('time')}:{event.get('type')}:{event.get('location', '')}"

    def _needs_replan(self, state: Any) -> bool:
        new_violation = len(state.violations) > self.last_violation_count
        new_event = any(self._event_key(event) not in self.observed_event_keys for event in self._visible_events(state))
        return new_violation or new_event

    def _replan(self, state: Any) -> None:
        visible_events = self._visible_events(state)
        args = [
            self.world.world.get("description", "Urban mobility simulation."),
            self._network_description(),
            self._person_description(),
            "Mon 2026-06-29 " + format_time(state.time),
            json.dumps(self.original_plan, ensure_ascii=False),
            json.dumps(self.revised_plans, ensure_ascii=False),
            json.dumps(
                {
                    "location": state.location,
                    "budget": state.budget,
                    "visited": [visit["location"] for visit in state.visits],
                    "dwell": dict(state.dwell),
                    "violations": state.violations,
                },
                ensure_ascii=False,
            ),
            json.dumps(visible_events, ensure_ascii=False),
            "Blocked edges and closed facilities are authoritative environment constraints.",
            "\n".join(self.primary.get("memory_seeds", [])),
            "No new chat summary is available.",
        ]
        prompt = render_official_prompt(self.official_generate_prompt, args, self.update_template)
        prompt += "\n\n" + self._adapter_override()
        parsed = self._complete_json(
            "You are executing GATSim's official activity-plan revision format after observing a city event.",
            prompt,
        )
        plan = parsed.get("plan", "none")
        changed = False
        if isinstance(plan, list):
            revised = self._validated_plan(plan)
            if revised:
                self.queue = revised
                changed = True
        elif isinstance(plan, str):
            lower = plan.strip().lower()
            departure = re.search(r"update departure time:\s*(\d{2}:\d{2})", lower)
            if departure:
                self.wait_until = parse_time(departure.group(1))
                changed = True
            elif lower.startswith("update path:"):
                if self.queue:
                    self.queue[0][4] = plan.split(":", 1)[1].strip()
                changed = True
        self.revised_plans.append(
            {
                "time": format_time(state.time),
                "reflection": parsed.get("reflection", ""),
                "plan": plan,
            }
        )
        self.last_violation_count = len(state.violations)
        self.observed_event_keys.update(self._event_key(event) for event in visible_events)

    def _required_dwell(self, target: str, state: Any) -> int:
        required = 0
        for condition in self.scenario.get("success_conditions", []):
            if condition.get("type") != "dwell_minutes":
                continue
            candidates = condition.get("location_any_of", [condition.get("location")])
            if target in candidates:
                required = max(required, int(condition.get("min_minutes", 0)))
        return max(0, required - int(state.dwell.get(target, 0)))

    def _required_evidence_action(
        self, target: str, state: Any
    ) -> dict[str, Any] | None:
        for condition in self.scenario.get("success_conditions", []):
            if condition.get("location") != target:
                continue
            if condition.get("type") == "buy_item":
                item = str(condition.get("item", "item"))
                if not any(
                    record.get("location") == target and record.get("item") == item
                    for record in state.purchases
                ):
                    return {
                        "kind": "buy",
                        "target": target,
                        "item": item,
                        "minutes": int(condition.get("minutes", 5)),
                        "reason": "execute GATSim activity as explicit purchase evidence",
                        "raw_response": self.last_raw_response,
                    }
            if condition.get("type") == "use_service_at":
                service = str(condition.get("service", "general_service"))
                if not any(
                    record.get("location") == target
                    and record.get("service") == service
                    for record in state.services
                ):
                    return {
                        "kind": "use_service",
                        "target": target,
                        "service": service,
                        "minutes": int(condition.get("minutes", 5)),
                        "reason": "execute GATSim activity as explicit service evidence",
                        "raw_response": self.last_raw_response,
                    }
        if (
            self._required_dwell(target, state) > 0
            and self.world.location_cost(target) > 0
            and not any(record.get("location") == target for record in state.services)
            and not any(record.get("location") == target for record in state.purchases)
        ):
            return {
                "kind": "use_service",
                "target": target,
                "service": "workspace_access",
                "minutes": 5,
                "reason": "pay for access before the GATSim-planned activity",
                "raw_response": self.last_raw_response,
            }
        return None

    def _explicit_path(self, activity: list[Any], current: str) -> list[str] | None:
        value = str(activity[4]).strip()
        if not value or value.lower() in {"none", "shortest", "direct", "null"}:
            return None
        nodes = [node.strip() for node in re.split(r"\s*(?:,|->|\u2192)\s*", value) if node.strip()]
        if current in nodes:
            nodes = nodes[nodes.index(current) :]
        elif not nodes or nodes[0] != current:
            nodes.insert(0, current)
        target = str(activity[0])
        if not nodes or nodes[-1] != target:
            nodes.append(target)
        return nodes

    def next_action(self, state: Any) -> dict[str, Any]:
        if self._needs_replan(state):
            self._replan(state)
        if self.wait_until is not None and state.time < self.wait_until:
            minutes = self.wait_until - state.time
            self.wait_until = None
            return {
                "kind": "dwell",
                "minutes": minutes,
                "reason": "GATSim official plan revision adjusted the next departure time",
                "raw_response": self.last_raw_response,
            }
        while self.queue:
            activity = self.queue[0]
            target = str(activity[0])
            if state.location != target:
                return {
                    "kind": "move",
                    "target": target,
                    "path": self._explicit_path(activity, state.location),
                    "reason": "follow GATSim official activity-plan destination",
                    "raw_response": self.last_raw_response,
                }
            if state.inside_location != target:
                return {
                    "kind": "enter",
                    "target": target,
                    "reason": "enter the GATSim activity destination",
                    "raw_response": self.last_raw_response,
                }
            evidence_action = self._required_evidence_action(target, state)
            if evidence_action:
                return evidence_action
            remaining_dwell = self._required_dwell(target, state)
            self.queue.pop(0)
            if remaining_dwell > 0:
                return {
                    "kind": "dwell",
                    "minutes": remaining_dwell,
                    "reason": "complete the GATSim-planned activity duration required by the private goal",
                    "raw_response": self.last_raw_response,
                }
        return {
            "kind": "finish",
            "reason": "GATSim official activity plan exhausted",
            "raw_response": self.last_raw_response,
        }
