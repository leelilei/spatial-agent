"""Shared provenance and execution helpers for external framework adapters."""

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
STANDARD_LLM_DIR = RESEARCH_ROOT / "0-Tools" / "research-standard"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
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


def verify_official_checkout(root: Path, manifest_path: Path) -> dict[str, Any]:
    manifest = load_json(manifest_path)
    if not (root / ".git").exists():
        raise RuntimeError(
            f"{manifest['framework_name']} checkout not found at {root}. Run "
            f"tools/setup_external_framework.py --framework {manifest['setup_name']} first."
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
        raise RuntimeError(
            f"invalid {manifest['framework_name']} checkout: " + "; ".join(errors)
        )
    return {
        "source_repo": manifest["source_repo"],
        "source_commit": commit,
        "integration_level": manifest["integration_level"],
        "native_backend": bool(manifest["native_backend"]),
        "verified_files": verified_files,
    }


def compile_named_function(source_path: Path, function_name: str) -> Callable[..., Any]:
    """Compile one dependency-free function directly from verified official source."""

    tree = ast.parse(source_path.read_text(encoding="utf-8"), filename=str(source_path))
    nodes = [
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == function_name
    ]
    if len(nodes) != 1:
        raise RuntimeError(f"{function_name} not found exactly once in {source_path}")
    module = ast.Module(body=nodes, type_ignores=[])
    ast.fix_missing_locations(module)
    namespace: dict[str, Any] = {}
    exec(compile(module, str(source_path), "exec"), namespace)
    return namespace[function_name]


def extract_assigned_string(source_path: Path, variable_name: str) -> str:
    tree = ast.parse(source_path.read_text(encoding="utf-8"), filename=str(source_path))
    values: list[str] = []
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if not any(isinstance(target, ast.Name) and target.id == variable_name for target in targets):
            continue
        value = ast.literal_eval(node.value)
        if isinstance(value, str):
            values.append(value)
    if len(values) != 1:
        raise RuntimeError(f"{variable_name} not found exactly once in {source_path}")
    return values[0]


def extract_function_string(source_path: Path, function_name: str, contains: str) -> str:
    tree = ast.parse(source_path.read_text(encoding="utf-8"), filename=str(source_path))
    functions = [
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == function_name
    ]
    if len(functions) != 1:
        raise RuntimeError(f"{function_name} not found exactly once in {source_path}")
    matches = [
        node.value
        for node in ast.walk(functions[0])
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
        and contains in node.value
    ]
    if len(matches) != 1:
        raise RuntimeError(
            f"string containing {contains!r} not found exactly once in {function_name}"
        )
    return matches[0]


def render_official_file_prompt(
    renderer: Callable[[Any, str], str], curr_input: Any, template: Path
) -> str:
    """Run an official renderer while forcing its UTF-8 template on Windows."""

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
    value = max(0, value)
    return f"{value // 60:02d}:{value % 60:02d}"


class OfficialAdapterBase:
    """Common CityIntent-facing state for adapted official decision modules."""

    agent_id = "official_adapter"
    framework_name = "ExternalFramework"

    def configure(
        self,
        world: Any,
        scenario: dict[str, Any],
        primary: dict[str, Any],
        llm_config: Path | None,
        provenance: dict[str, Any],
    ) -> None:
        if llm_config is None:
            raise ValueError(f"{self.agent_id} requires --llm-config")
        if str(STANDARD_LLM_DIR) not in sys.path:
            sys.path.insert(0, str(STANDARD_LLM_DIR))
        from llm_client import LLM  # type: ignore

        self.llm = LLM(llm_config)
        self.world = world
        self.scenario = scenario
        self.primary = primary
        self.queue: list[dict[str, Any]] = []
        self.last_raw_response = ""
        self.last_violation_count = 0
        self.observed_event_keys: set[str] = set()
        self.model_info = {
            "provider": self.llm.config.provider,
            "model": self.llm.config.model,
            "wire_api": self.llm.config.wire_api,
            "base_url": self.llm.config.base_url,
            "framework": self.framework_name,
            "framework_agent": self.agent_id,
            "source_verified": True,
            **provenance,
        }

    def complete_json(self, system: str, prompt: str) -> dict[str, Any]:
        self.last_raw_response = self.llm.complete(system, prompt)
        from llm_client import parse_response_json  # type: ignore

        parsed = parse_response_json(self.last_raw_response)
        return parsed if isinstance(parsed, dict) else {}

    def network_description(self) -> str:
        lines = [f"City network: {self.world.world.get('name', 'micro city')}", "Facilities:"]
        for location in self.world.world["locations"]:
            lines.append(
                f"- {location['id']}: type={location.get('type')}; "
                f"tags={','.join(location.get('tags', []))}; "
                f"open={'-'.join(location.get('open', []))}; "
                f"cost={location.get('typical_cost', 0)}"
            )
        lines.append("Edges (minutes):")
        for edge in self.world.world["edges"]:
            lines.append(f"- {edge['from']} <-> {edge['to']}: {edge['minutes']}")
        return "\n".join(lines)

    def person_description(self) -> str:
        return "\n".join(
            [
                f"Name: {self.primary['agent_id']}",
                f"Persona: {self.primary['persona']}",
                f"Private goal: {self.primary['private_intention']}",
                f"Start: {self.primary['start_location']}",
                f"Budget: {self.primary['budget']}",
                "Known facilities: " + ", ".join(self.primary.get("known_locations", [])),
                "Memories: " + " | ".join(self.primary.get("memory_seeds", [])),
            ]
        )

    def state_description(self, state: Any) -> str:
        return json.dumps(
            {
                "time": format_time(state.time),
                "location": state.location,
                "budget": state.budget,
                "visited": [visit["location"] for visit in state.visits],
                "dwell": dict(state.dwell),
                "messages": state.messages,
                "interactions": state.interactions,
                "violations": state.violations,
                "visible_events": self.visible_events(state),
            },
            ensure_ascii=False,
        )

    def visible_events(self, state: Any) -> list[dict[str, Any]]:
        return [
            event
            for event in self.scenario.get("events", [])
            if event.get("visibility", "public") == "public"
            and parse_time(event["time"]) <= state.time
        ]

    @staticmethod
    def event_key(event: dict[str, Any]) -> str:
        return f"{event.get('time')}:{event.get('type')}:{event.get('location', '')}"

    def needs_replan(self, state: Any) -> bool:
        return len(state.violations) > self.last_violation_count or any(
            self.event_key(event) not in self.observed_event_keys
            for event in self.visible_events(state)
        )

    def record_observations(self, state: Any, changed: bool) -> None:
        events = self.visible_events(state)
        if events and changed:
            state.replanned_after_event = True
        self.last_violation_count = len(state.violations)
        self.observed_event_keys.update(self.event_key(event) for event in events)

    def validate_actions(self, value: Any) -> list[dict[str, Any]]:
        if not isinstance(value, list):
            return []
        allowed = {"kind", "target", "path", "minutes", "to", "content", "reason"}
        actions: list[dict[str, Any]] = []
        for item in value[:12]:
            if not isinstance(item, dict):
                continue
            action = {key: item[key] for key in allowed if key in item}
            kind = str(action.get("kind", "")).strip().lower()
            if kind not in {"move", "dwell", "message", "interact", "finish"}:
                continue
            action["kind"] = kind
            if kind == "move":
                target = str(action.get("target", ""))
                if target not in self.world.locations:
                    continue
                action["target"] = target
                if isinstance(action.get("path"), str):
                    action["path"] = [
                        node.strip()
                        for node in re.split(r"\s*(?:,|->|\u2192)\s*", action["path"])
                        if node.strip()
                    ]
            if kind in {"dwell", "interact"}:
                try:
                    action["minutes"] = max(1, int(action.get("minutes", 1)))
                except (TypeError, ValueError):
                    action["minutes"] = 1
            action.setdefault("reason", f"{self.framework_name} official adapter action")
            actions.append(action)
        return actions

    def next_queued_action(self, state: Any) -> dict[str, Any]:
        while self.queue:
            action = dict(self.queue[0])
            if action["kind"] == "move" and state.location == action.get("target"):
                self.queue.pop(0)
                continue
            if action["kind"] != "move":
                self.queue.pop(0)
            action["raw_response"] = self.last_raw_response
            return action
        return {
            "kind": "finish",
            "reason": f"{self.framework_name} adapted official plan exhausted",
            "raw_response": self.last_raw_response,
        }
