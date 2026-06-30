"""Run deterministic CityIntent v0 baseline traces.

This runner is intentionally small and dependency-free. It is not yet a full
simulator; it is a reproducible harness for checking whether scenario packages
can produce comparable traces and first-pass metrics.

The `llm_direct_actor` implementation here is an offline proxy for a direct
LLM-action policy. It does not call an external model.
"""

from __future__ import annotations

import argparse
import csv
import heapq
import json
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS_DIR = ROOT.parents[1] / "results" / "cityintent_v0" / "baseline_smoke"
STANDARD_LLM_DIR = ROOT.parents[2] / "0-Tools" / "research-standard"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write("\n")


def parse_time(value: str) -> int:
    hour, minute = value.split(":", 1)
    return int(hour) * 60 + int(minute)


def format_time(value: int) -> str:
    value = max(0, value)
    return f"{value // 60:02d}:{value % 60:02d}"


def normalize_edge(edge: list[str] | tuple[str, str]) -> tuple[str, str]:
    a, b = edge
    return tuple(sorted((a, b)))


@dataclass
class Action:
    kind: str
    target: str | None = None
    path: list[str] | None = None
    minutes: int = 0
    to: str | None = None
    content: str = ""
    item: str = ""
    service: str = ""
    reason: str = ""
    raw_response: str = ""


@dataclass
class TraceState:
    scenario_id: str
    agent_id: str
    agent_type: str
    time: int
    end_time: int
    location: str
    budget: float
    completed_work: bool = False
    replanned_after_event: bool = False
    violations: list[dict[str, Any]] = field(default_factory=list)
    actions: list[dict[str, Any]] = field(default_factory=list)
    visits: list[dict[str, Any]] = field(default_factory=list)
    traversals: list[dict[str, Any]] = field(default_factory=list)
    dwell: dict[str, int] = field(default_factory=lambda: defaultdict(int))
    messages: list[dict[str, Any]] = field(default_factory=list)
    interactions: list[dict[str, Any]] = field(default_factory=list)
    entries: list[dict[str, Any]] = field(default_factory=list)
    services: list[dict[str, Any]] = field(default_factory=list)
    purchases: list[dict[str, Any]] = field(default_factory=list)
    abandonments: list[dict[str, Any]] = field(default_factory=list)
    inside_location: str | None = None
    paid_services: set[str] = field(default_factory=set)


class CityWorld:
    def __init__(self, world: dict[str, Any]):
        self.world = world
        self.locations = {loc["id"]: loc for loc in world["locations"]}
        self.graph: dict[str, list[tuple[str, float]]] = defaultdict(list)
        for edge in world["edges"]:
            a = edge["from"]
            b = edge["to"]
            minutes = float(edge["minutes"])
            self.graph[a].append((b, minutes))
            self.graph[b].append((a, minutes))

    def location_cost(self, location_id: str) -> float:
        return float(self.locations[location_id].get("typical_cost", 0))

    def is_open(self, location_id: str, at_time: int, scenario: dict[str, Any]) -> bool:
        location = self.locations[location_id]
        open_start, open_end = [parse_time(v) for v in location.get("open", ["00:00", "23:59"])]
        if not (open_start <= at_time <= open_end):
            return False
        for event in scenario.get("events", []):
            if event.get("location") != location_id:
                continue
            effect = event.get("effect", {})
            closed_until = effect.get("closed_until")
            if closed_until and parse_time(event["time"]) <= at_time < parse_time(closed_until):
                return False
        return True

    def active_blocked_edges(self, scenario: dict[str, Any], at_time: int) -> set[tuple[str, str]]:
        blocked: set[tuple[str, str]] = set()
        for event in scenario.get("events", []):
            effect = event.get("effect", {})
            edge = effect.get("blocked_edge")
            if not edge:
                continue
            start = parse_time(event["time"])
            end = parse_time(effect.get("until", "23:59"))
            if start <= at_time < end:
                blocked.add(normalize_edge(edge))
        return blocked

    def edge_blocked_during(self, scenario: dict[str, Any], edge: tuple[str, str], depart: int, arrive: int) -> bool:
        normalized = normalize_edge(edge)
        for event in scenario.get("events", []):
            effect = event.get("effect", {})
            blocked_edge = effect.get("blocked_edge")
            if not blocked_edge or normalize_edge(blocked_edge) != normalized:
                continue
            start = parse_time(event["time"])
            end = parse_time(effect.get("until", "23:59"))
            if depart < end and arrive > start:
                return True
        return False

    def shortest_path(
        self,
        start: str,
        goal: str,
        scenario: dict[str, Any] | None = None,
        at_time: int = 0,
        avoid_active_blocks: bool = True,
    ) -> tuple[list[str], float]:
        blocked = self.active_blocked_edges(scenario or {}, at_time) if avoid_active_blocks else set()
        heap: list[tuple[float, str, list[str]]] = [(0.0, start, [start])]
        best: dict[str, float] = {start: 0.0}
        while heap:
            distance, node, path = heapq.heappop(heap)
            if node == goal:
                return path, distance
            if distance != best[node]:
                continue
            for neighbor, minutes in self.graph[node]:
                if normalize_edge((node, neighbor)) in blocked:
                    continue
                if (
                    avoid_active_blocks
                    and scenario
                    and neighbor != goal
                    and not self.is_open(neighbor, at_time, scenario)
                ):
                    continue
                next_distance = distance + minutes
                if next_distance < best.get(neighbor, float("inf")):
                    best[neighbor] = next_distance
                    heapq.heappush(heap, (next_distance, neighbor, path + [neighbor]))
        return [start], float("inf")


class BasePolicy:
    agent_id = "base"

    def __init__(
        self,
        world: CityWorld,
        scenario: dict[str, Any],
        primary: dict[str, Any],
        llm_config: Path | None = None,
    ):
        self.world = world
        self.scenario = scenario
        self.primary = primary
        self.llm_config = llm_config
        self.model_info: dict[str, Any] | None = None
        self.queue = self.build_queue()

    def build_queue(self) -> list[str]:
        raise NotImplementedError

    def next_action(self, state: TraceState) -> Action:
        raise NotImplementedError

    def choose_from_candidates(self, candidates: list[str], state: TraceState, prefer_cost: bool = True) -> str:
        scored: list[tuple[float, str]] = []
        for candidate in candidates:
            _, distance = self.world.shortest_path(state.location, candidate, self.scenario, state.time)
            cost = self.world.location_cost(candidate) if prefer_cost else 0
            score = distance + cost * 0.75
            scored.append((score, candidate))
        return min(scored)[1]


class UtilityPlannerPolicy(BasePolicy):
    agent_id = "utility_planner"

    def build_queue(self) -> list[str]:
        queue: list[str] = []
        pseudo_state = TraceState(
            scenario_id=self.scenario["scenario_id"],
            agent_id=self.primary["agent_id"],
            agent_type=self.agent_id,
            time=parse_time(self.scenario["episode"]["start_time"]),
            end_time=parse_time(self.scenario["episode"]["end_time"]),
            location=self.primary["start_location"],
            budget=float(self.primary["budget"]),
        )
        for condition in self.scenario["success_conditions"]:
            ctype = condition["type"]
            if ctype in {"visit_location", "visit_before"}:
                queue.append(condition["location"])
            elif ctype in {"buy_item", "use_service_at"}:
                queue.append(condition["location"])
            elif ctype == "visit_location_any_of":
                queue.append(self.choose_from_candidates(condition["location_any_of"], pseudo_state))
            elif ctype in {"visit_open_location", "dwell_minutes"}:
                candidates = condition.get("location_any_of") or [condition.get("location")]
                candidates = [item for item in candidates if item]
                queue.append(self.choose_from_candidates(candidates, pseudo_state))
            elif ctype == "co_presence":
                queue.append(self.choose_from_candidates(condition["location_any_of"], pseudo_state))
        if self.scenario["scenario_id"] == "budget_errand_chain":
            queue = ["pharmacy", "budget_diner", "home_aria"]
        return dedupe(queue)

    def next_action(self, state: TraceState) -> Action:
        if self.scenario["scenario_id"] == "conflicting_social_obligation":
            if state.location == "coworking" and state.dwell.get("coworking", 0) < 45:
                if not has_used_service(state, "coworking"):
                    return Action(
                        "use_service",
                        target="coworking",
                        service="workspace_access",
                        minutes=5,
                        reason="pay for coworking before the protected work block",
                    )
                return Action("dwell", minutes=45, reason="protect work block before handling social invitation")
            if not any(msg.get("to") == "ben" for msg in state.messages):
                return Action(
                    "message",
                    to="ben",
                    content="I need to finish a client deadline first, but I can meet after the work block.",
                    reason="maintain relationship without false commitment",
                )
        timed_action = self.next_condition_action(state)
        if timed_action:
            return timed_action
        return Action("finish", reason="all planned utility targets completed")

    def next_condition_action(self, state: TraceState) -> Action | None:
        for condition in self.scenario["success_conditions"]:
            ctype = condition["type"]
            if ctype == "buy_item":
                target = condition["location"]
                item = condition.get("item", "item")
                if has_purchased(state, target, item):
                    continue
                access = self.access_action(state, target, "reach purchase location")
                if access:
                    return access
                return Action(
                    "buy",
                    target=target,
                    item=item,
                    minutes=int(condition.get("minutes", 5)),
                    reason="produce explicit purchase evidence",
                )
            if ctype == "use_service_at":
                target = condition["location"]
                service = condition.get("service", "general_service")
                if has_used_service(state, target, service):
                    continue
                access = self.access_action(state, target, "reach service location")
                if access:
                    return access
                return Action(
                    "use_service",
                    target=target,
                    service=service,
                    minutes=int(condition.get("minutes", 15)),
                    reason="produce explicit service evidence",
                )
            if ctype == "dwell_minutes":
                candidates = condition.get("location_any_of") or [condition.get("location")]
                candidates = [item for item in candidates if item]
                target = self.choose_from_candidates(candidates, state)
                current_dwell = state.dwell.get(state.location, 0) if state.location in candidates else 0
                if current_dwell >= condition["min_minutes"]:
                    continue
                if state.location not in candidates or state.inside_location != state.location:
                    access = self.access_action(
                        state, target, "reach and enter a place for the required dwell"
                    )
                    if access:
                        return access
                if self.world.location_cost(state.location) > 0 and not (
                    has_used_service(state, state.location)
                    or has_purchased(state, state.location)
                ):
                    return Action(
                        "use_service",
                        target=state.location,
                        service="workspace_access",
                        minutes=5,
                        reason="pay for access before using a paid place",
                    )
                return Action(
                    "dwell",
                    minutes=int(condition["min_minutes"] - current_dwell),
                    reason="complete required dwell time for the private intention",
                )
            if ctype == "co_presence":
                target = self.choose_from_candidates(condition["location_any_of"], state)
                start, end = [parse_time(v) for v in condition["time_window"]]
                if condition_success(condition, state, self.scenario) >= 1.0:
                    continue
                access = self.access_action(state, target, "reach and enter meeting location")
                if access:
                    return access
                if state.time < start:
                    if self.world.location_cost(state.location) > 0 and not (
                        has_used_service(state, state.location)
                        or has_purchased(state, state.location)
                    ):
                        return Action(
                            "use_service",
                            target=state.location,
                            service="meeting_refreshment",
                            minutes=5,
                            reason="use paid meeting venue before waiting",
                        )
                    return Action("dwell", minutes=start - state.time, reason="wait until the meeting window")
                if state.time <= end:
                    return Action("dwell", minutes=5, reason="stay present for the meeting")
            if ctype == "visit_open_location":
                candidates = condition.get("location_any_of") or [condition.get("location")]
                candidates = [item for item in candidates if item]
                target = self.choose_from_candidates(candidates, state)
                start, end = [parse_time(v) for v in condition["time_window"]]
                if any(start <= t <= end for t in presence_times(state, candidates)):
                    continue
                access = self.access_action(state, target, "reach and enter an open replacement")
                if access:
                    return access
                if state.time < start:
                    if self.world.location_cost(state.location) > 0 and not (
                        has_used_service(state, state.location)
                        or has_purchased(state, state.location)
                    ):
                        return Action(
                            "use_service",
                            target=state.location,
                            service="workspace_access",
                            minutes=5,
                            reason="pay before waiting in a paid replacement",
                        )
                    return Action("dwell", minutes=start - state.time, reason="wait until the valid replacement window")
                if state.time <= end:
                    if self.world.location_cost(state.location) > 0 and not (
                        has_used_service(state, state.location)
                        or has_purchased(state, state.location)
                    ):
                        return Action(
                            "use_service",
                            target=state.location,
                            service="workspace_access",
                            minutes=5,
                            reason="pay before using a paid replacement",
                        )
                    return Action("dwell", minutes=1, reason="mark presence in the valid replacement window")
            if ctype in {"visit_location", "visit_before"}:
                include_start = not bool(condition.get("ignore_start", False))
                if not visit_times(state, [condition["location"]], include_start=include_start):
                    return self.access_action(
                        state,
                        condition["location"],
                        "satisfy explicit entered-location target",
                    )
            if ctype == "visit_location_any_of" and not visit_times(state, condition["location_any_of"]):
                target = self.choose_from_candidates(condition["location_any_of"], state)
                return self.access_action(
                    state, target, "satisfy one acceptable entered-location target"
                )
            if ctype == "send_message" and not any(
                message.get("to") == condition["to"] for message in state.messages
            ):
                return Action(
                    "message",
                    to=condition["to"],
                    content="Confirming the feasible meeting plan and timing.",
                    reason="satisfy explicit communication requirement",
                )
            if ctype == "bounded_social_interaction":
                minutes = sum(
                    interaction.get("minutes", 0)
                    for interaction in state.interactions
                    if interaction.get("with") == condition["with"]
                )
                if minutes == 0:
                    return Action(
                        "interact",
                        to=condition["with"],
                        minutes=min(5, int(condition["max_minutes"])),
                        reason="take the bounded social opportunity",
                    )
        return None

    def access_action(
        self, state: TraceState, target: str, reason: str
    ) -> Action | None:
        if state.location != target:
            return Action("move", target=target, reason=reason)
        if state.inside_location != target:
            return Action("enter", target=target, reason=reason)
        return None


class DirectActorOfflineProxy(BasePolicy):
    agent_id = "llm_direct_actor"

    def build_queue(self) -> list[str]:
        scenario_id = self.scenario["scenario_id"]
        scripted = {
            "budget_errand_chain": ["pharmacy", "cafe_central", "home_aria"],
            "avoid_crowd_event": ["plaza", "market"],
            "closed_poi_replacement": ["library", "quiet_cafe"],
            "memory_dependent_place_choice": ["cafe_central"],
            "conflicting_social_obligation": ["theatre"],
            "unexpected_friend_encounter": ["market", "pharmacy"],
            "commute_disruption": ["office"],
            "lunch_meeting_time_pressure": ["cafe_central"],
        }
        if scenario_id in scripted:
            return scripted[scenario_id]
        queue: list[str] = []
        for condition in self.scenario["success_conditions"]:
            if "location" in condition:
                queue.append(condition["location"])
            elif "location_any_of" in condition:
                queue.append(condition["location_any_of"][0])
        return dedupe(queue)

    def next_action(self, state: TraceState) -> Action:
        if self.scenario["scenario_id"] == "conflicting_social_obligation":
            if not any(msg.get("to") == "ben" for msg in state.messages):
                return Action(
                    "message",
                    to="ben",
                    content="Great, I will come to the theatre at 18:00.",
                    reason="directly accept salient social invitation",
                )
        if self.scenario["scenario_id"] == "unexpected_friend_encounter":
            if state.location == "market" and not state.interactions:
                return Action("interact", to="casey", minutes=20, reason="over-engage with salient unexpected encounter")
        for target in self.queue:
            if not self.target_complete(state, target):
                if state.location != target:
                    return Action("move", target=target, reason="direct action from salient scenario cue")
                if state.inside_location != target:
                    return Action("enter", target=target, reason="enter the salient destination")
                for condition in self.scenario["success_conditions"]:
                    if condition.get("location") != target:
                        continue
                    if condition["type"] == "buy_item":
                        return Action(
                            "buy",
                            target=target,
                            item=condition.get("item", "item"),
                            minutes=5,
                            reason="complete salient purchase",
                        )
                    if condition["type"] == "use_service_at":
                        return Action(
                            "use_service",
                            target=target,
                            service=condition.get("service", "general_service"),
                            minutes=15,
                            reason="complete salient service",
                        )
                if self.world.location_cost(target) > 0 and not (
                    has_used_service(state, target) or has_purchased(state, target)
                ):
                    return Action(
                        "use_service",
                        target=target,
                        service="salient_activity",
                        minutes=5,
                        reason="pay before using the salient destination",
                    )
                return Action("dwell", minutes=15, reason="act on the currently salient destination")
        return Action("finish", reason="no salient destination remains")

    def target_complete(self, state: TraceState, target: str) -> bool:
        matching = [
            condition
            for condition in self.scenario["success_conditions"]
            if condition["type"]
            in {
                "visit_location",
                "visit_location_any_of",
                "visit_before",
                "visit_open_location",
                "dwell_minutes",
                "buy_item",
                "use_service_at",
                "co_presence",
            }
            and (
                condition.get("location") == target
                or target in condition.get("location_any_of", [])
            )
        ]
        if not matching:
            return has_visited(state, target)
        return all(
            condition_success(condition, state, self.scenario) >= 1.0
            for condition in matching
        )


class APILLMDirectActor(BasePolicy):
    agent_id = "api_llm_direct_actor"

    def __init__(
        self,
        world: CityWorld,
        scenario: dict[str, Any],
        primary: dict[str, Any],
        llm_config: Path | None = None,
    ):
        if llm_config is None:
            raise ValueError("api_llm_direct_actor requires --llm-config")
        if str(STANDARD_LLM_DIR) not in sys.path:
            sys.path.insert(0, str(STANDARD_LLM_DIR))
        from llm_client import LLM, parse_response_json  # type: ignore

        self._parse_response_json = parse_response_json
        self.llm = LLM(llm_config)
        super().__init__(world, scenario, primary, llm_config=llm_config)
        cfg = self.llm.config
        self.model_info = {
            "provider": cfg.provider,
            "model": cfg.model,
            "wire_api": cfg.wire_api,
            "base_url": cfg.base_url,
            "temperature": cfg.temperature,
            "json_mode": cfg.json_mode,
        }

    def build_queue(self) -> list[str]:
        return []

    def next_action(self, state: TraceState) -> Action:
        system = self.system_prompt()
        user = json.dumps(self.build_observation(state), ensure_ascii=False, indent=2)
        raw = self.llm.complete(system, user)
        parsed = self._parse_response_json(raw)
        if isinstance(parsed, dict) and isinstance(parsed.get("action"), dict):
            parsed = parsed["action"]
        if not isinstance(parsed, dict):
            return Action("invalid_model_action", reason="model did not return parseable JSON", raw_response=raw)
        return self.parse_action(parsed, raw)

    def system_prompt(self) -> str:
        return (
            "You are a city-agent policy inside CityIntent. "
            "Choose exactly one next action for the primary agent. "
            "Return exactly one JSON object and no markdown. "
            "Allowed kinds: move, enter, use_service, buy, dwell, message, interact, finish, abandon. "
            "Use only location ids and agent ids given in the observation."
        )

    def build_observation(self, state: TraceState) -> dict[str, Any]:
        known_locations = self.primary.get("known_locations", [])
        location_cards = []
        for location_id in known_locations:
            if location_id in self.world.locations:
                loc = self.world.locations[location_id]
                path, minutes = self.world.shortest_path(state.location, location_id, self.scenario, state.time)
                location_cards.append(
                    {
                        "id": location_id,
                        "name": loc.get("name"),
                        "type": loc.get("type"),
                        "tags": loc.get("tags", []),
                        "open": loc.get("open"),
                        "typical_cost": loc.get("typical_cost", 0),
                        "currently_open": self.world.is_open(location_id, state.time, self.scenario),
                        "shortest_path_minutes": None if minutes == float("inf") else minutes,
                        "path": path,
                    }
                )
        visible_events = [
            event
            for event in self.scenario.get("events", [])
            if event.get("visibility") == "public" or parse_time(event["time"]) <= state.time
        ]
        return {
            "task": "Choose the next typed action for the primary city agent.",
            "response_schema": {
                "kind": "move|enter|use_service|buy|dwell|message|interact|finish|abandon",
                "target": "location id for move/enter/use_service/buy, otherwise null",
                "minutes": "integer minutes for use_service/buy/dwell/interact, otherwise 0",
                "to": "agent id for message/interact, otherwise null",
                "content": "message text if kind=message, otherwise empty string",
                "item": "purchased item if kind=buy, otherwise empty string",
                "service": "service used if kind=use_service, otherwise empty string",
                "reason": "short reason grounded in the observation",
            },
            "scenario": {
                "id": self.scenario["scenario_id"],
                "title": self.scenario["title"],
                "family": self.scenario["family"],
                "public_context": self.scenario.get("public_context", ""),
                "success_conditions": self.scenario.get("success_conditions", []),
            },
            "primary_agent": {
                "id": self.primary["agent_id"],
                "persona": self.primary["persona"],
                "private_intention": self.primary["private_intention"],
                "memory_seeds": self.primary.get("memory_seeds", []),
            },
            "current_state": {
                "time": format_time(state.time),
                "episode_end": format_time(state.end_time),
                "location": state.location,
                "inside_location": state.inside_location,
                "budget": state.budget,
                "arrivals": state.visits,
                "entries": state.entries,
                "services_used": state.services,
                "purchases": state.purchases,
                "dwell_minutes_by_location": dict(state.dwell),
                "messages_sent": state.messages,
                "interactions": state.interactions,
                "violations_so_far": state.violations,
            },
            "known_locations": location_cards,
            "visible_events": visible_events,
            "other_agents": [
                {
                    "id": agent["agent_id"],
                    "persona": agent["persona"],
                    "start_location": agent["start_location"],
                }
                for agent in self.scenario.get("agents", [])
                if agent["agent_id"] != self.primary["agent_id"]
            ],
            "action_guidance": [
                "Prefer feasible actions over merely plausible narration.",
                "Move only changes location; it never enters a POI, pays, buys, or completes an errand.",
                "After moving, use enter before dwell, buy, or use_service.",
                "Use buy for item evidence and use_service for meals, tickets, or paid access.",
                "Only buy/use_service deducts typical_cost; pass-through and arrival are free.",
                "If a place is closed, do not enter it; choose an alternative.",
                "Use dwell only after entering. Paid places require buy/use_service before dwell.",
                "If the current place satisfies the intention, dwell there instead of moving to another similar place.",
                "If all important goals have evidence, use finish. If impossible, use abandon with an honest reason.",
            ],
        }

    def parse_action(self, parsed: dict[str, Any], raw: str) -> Action:
        kind = str(parsed.get("kind", "")).strip().lower()
        if kind == "wait":
            kind = "dwell"
        target = parsed.get("target")
        target = str(target).strip() if target is not None and str(target).strip() else None
        to = parsed.get("to")
        to = str(to).strip() if to is not None and str(to).strip() else None
        content = str(parsed.get("content", "") or "")
        item = str(parsed.get("item", "") or "")
        service = str(parsed.get("service", "") or "")
        reason = str(parsed.get("reason", "") or "")
        try:
            minutes = int(float(parsed.get("minutes", 0) or 0))
        except (TypeError, ValueError):
            minutes = 0
        if kind == "move":
            if target not in self.world.locations:
                return Action("invalid_model_action", reason=f"unknown move target: {target}", raw_response=raw)
            return Action("move", target=target, reason=reason, raw_response=raw)
        if kind == "enter":
            if target is not None and target not in self.world.locations:
                return Action("invalid_model_action", reason=f"unknown enter target: {target}", raw_response=raw)
            return Action("enter", target=target, reason=reason, raw_response=raw)
        if kind == "use_service":
            if target is not None and target not in self.world.locations:
                return Action("invalid_model_action", reason=f"unknown service target: {target}", raw_response=raw)
            return Action(
                "use_service",
                target=target,
                service=service or "general_service",
                minutes=max(1, min(minutes or 5, 90)),
                reason=reason,
                raw_response=raw,
            )
        if kind == "buy":
            if target is not None and target not in self.world.locations:
                return Action("invalid_model_action", reason=f"unknown purchase target: {target}", raw_response=raw)
            return Action(
                "buy",
                target=target,
                item=item or "item",
                minutes=max(1, min(minutes or 5, 90)),
                reason=reason,
                raw_response=raw,
            )
        if kind == "dwell":
            return Action("dwell", minutes=max(1, min(minutes or 10, 90)), reason=reason, raw_response=raw)
        if kind == "message":
            return Action("message", to=to, content=content, reason=reason, raw_response=raw)
        if kind == "interact":
            return Action("interact", to=to, minutes=max(1, min(minutes or 10, 60)), reason=reason, raw_response=raw)
        if kind == "finish":
            return Action("finish", reason=reason, raw_response=raw)
        if kind == "abandon":
            return Action("abandon", reason=reason, raw_response=raw)
        return Action("invalid_model_action", reason=f"unsupported action kind: {kind}", raw_response=raw)


class APILLMPlanThenAct(APILLMDirectActor):
    agent_id = "api_llm_plan_then_act"

    def build_queue(self) -> list[str]:
        self.plan_actions: list[dict[str, Any]] = []
        system = (
            "You are a city-agent planner inside CityIntent. "
            "Create a short executable plan for the primary agent before the episode starts. "
            "Return exactly one JSON object with key plan, whose value is a list of action objects. "
            "Allowed action kinds: move, enter, use_service, buy, dwell, message, interact, finish, abandon. "
            "Use only location ids and agent ids from the scenario. "
            "Do not include markdown."
        )
        user = json.dumps(self.build_plan_observation(), ensure_ascii=False, indent=2)
        raw = self.llm.complete(system, user)
        parsed = self._parse_response_json(raw)
        if isinstance(parsed, dict) and isinstance(parsed.get("plan"), list):
            self.plan_actions = [item for item in parsed["plan"] if isinstance(item, dict)]
        elif isinstance(parsed, list):
            self.plan_actions = [item for item in parsed if isinstance(item, dict)]
        else:
            self.plan_actions = [
                {
                    "kind": "finish",
                    "reason": "planner did not return a parseable plan",
                    "raw_response": raw,
                }
            ]
        self.plan_raw_response = raw
        return []

    def build_plan_observation(self) -> dict[str, Any]:
        start_time = parse_time(self.scenario["episode"]["start_time"])
        known_locations = []
        for location_id in self.primary.get("known_locations", []):
            if location_id not in self.world.locations:
                continue
            loc = self.world.locations[location_id]
            path, minutes = self.world.shortest_path(self.primary["start_location"], location_id, self.scenario, start_time)
            known_locations.append(
                {
                    "id": location_id,
                    "name": loc.get("name"),
                    "type": loc.get("type"),
                    "tags": loc.get("tags", []),
                    "open": loc.get("open"),
                    "typical_cost": loc.get("typical_cost", 0),
                    "shortest_path_from_start_minutes": None if minutes == float("inf") else minutes,
                    "path_from_start": path,
                }
            )
        return {
            "task": "Make an initial plan. The plan will be executed later without replanning.",
            "response_schema": {
                "plan": [
                    {
                        "kind": "move|enter|use_service|buy|dwell|message|interact|finish|abandon",
                        "target": "location id for move/enter/use_service/buy, otherwise null",
                        "minutes": "integer minutes for use_service/buy/dwell/interact, otherwise 0",
                        "to": "agent id for message/interact, otherwise null",
                        "content": "message text if kind=message, otherwise empty string",
                        "item": "item name for buy",
                        "service": "service name for use_service",
                        "reason": "short feasibility-aware reason",
                    }
                ]
            },
            "scenario": {
                "id": self.scenario["scenario_id"],
                "title": self.scenario["title"],
                "family": self.scenario["family"],
                "public_context": self.scenario.get("public_context", ""),
                "episode": self.scenario["episode"],
                "events": self.scenario.get("events", []),
                "success_conditions": self.scenario.get("success_conditions", []),
            },
            "primary_agent": {
                "id": self.primary["agent_id"],
                "persona": self.primary["persona"],
                "private_intention": self.primary["private_intention"],
                "start_location": self.primary["start_location"],
                "budget": self.primary["budget"],
                "memory_seeds": self.primary.get("memory_seeds", []),
            },
            "known_locations": known_locations,
            "other_agents": [
                {
                    "id": agent["agent_id"],
                    "persona": agent["persona"],
                    "start_location": agent["start_location"],
                }
                for agent in self.scenario.get("agents", [])
                if agent["agent_id"] != self.primary["agent_id"]
            ],
        }

    def next_action(self, state: TraceState) -> Action:
        if not self.plan_actions:
            return Action("finish", reason="initial plan exhausted")
        parsed = self.plan_actions.pop(0)
        raw = str(getattr(self, "plan_raw_response", ""))
        action = self.parse_action(parsed, raw)
        if action.kind == "finish" and self.plan_actions:
            return action
        return action


class APILLMReactiveReplanner(APILLMDirectActor):
    agent_id = "api_llm_reactive_replanner"

    def system_prompt(self) -> str:
        return (
            "You are a reactive city-agent replanner inside CityIntent. "
            "At every step, reassess unfinished goals, prior violations, current time, budget, open POIs, and visible events. "
            "Choose exactly one next action that is feasible now. "
            "Do not repeat an action that already caused a violation. "
            "Return exactly one JSON object and no markdown. "
            "Allowed kinds: move, enter, use_service, buy, dwell, message, interact, finish, abandon."
        )

    def build_observation(self, state: TraceState) -> dict[str, Any]:
        observation = super().build_observation(state)
        condition_status = []
        for condition in self.scenario["success_conditions"]:
            condition_status.append(
                {
                    "id": condition["id"],
                    "type": condition["type"],
                    "score_now": condition_success(condition, state, self.scenario),
                    "condition": condition,
                }
            )
        violated_targets = []
        for action in state.actions:
            if action.get("violations"):
                payload = action.get("action", {})
                violated_targets.append(
                    {
                        "step": action["step"],
                        "kind": payload.get("kind"),
                        "target": payload.get("target"),
                        "violations": action.get("violations", []),
                    }
                )
        observation["replanning_state"] = {
            "condition_status": condition_status,
            "unfinished_conditions": [item for item in condition_status if item["score_now"] < 1.0],
            "violated_prior_actions": violated_targets,
            "failure_taxonomy_so_far": failure_taxonomy_counts(state),
        }
        observation["action_guidance"] = [
            "First satisfy unfinished_conditions, not just salient text.",
            "If violated_prior_actions is non-empty, choose a different feasible route or goal strategy.",
            "If a disruption makes the original path impossible, replan around it.",
            "If remaining time or budget makes a goal impossible, stop false continuation and choose finish with an honest reason.",
            *observation.get("action_guidance", []),
        ]
        return observation


class ReactiveReplannerPolicy(UtilityPlannerPolicy):
    agent_id = "reactive_replanner"

    def next_action(self, state: TraceState) -> Action:
        if self.scenario["scenario_id"] == "commute_disruption":
            event_time = parse_time("08:15")
            if not has_arrived(state, "transit_hub"):
                return Action("move", target="transit_hub", reason="start with the normal commute route")
            if state.location == "transit_hub" and state.inside_location != "transit_hub":
                return Action("enter", target="transit_hub", reason="enter the transit hub while monitoring service")
            if state.time < event_time:
                return Action("dwell", minutes=event_time - state.time, reason="observe disruption before committing to office edge")
            if not has_visited(state, "office"):
                return self.access_action(
                    state, "office", "replan around the blocked transit-office edge"
                ) or Action("finish", reason="office reached")
        if self.scenario["scenario_id"] == "closed_poi_replacement":
            if not has_visited(state, "bookstore"):
                return self.access_action(
                    state, "bookstore", "switch to an open quiet replacement after closure"
                ) or Action("finish", reason="bookstore reached")
            if not has_used_service(state, "bookstore"):
                return Action(
                    "use_service",
                    target="bookstore",
                    service="workspace_access",
                    minutes=5,
                    reason="pay before using the bookstore workspace",
                )
            if state.dwell.get("bookstore", 0) < 60:
                return Action("dwell", minutes=60 - state.dwell.get("bookstore", 0), reason="complete focus session after replanning")
        return super().next_action(state)


class MemoryReflectionPolicy(UtilityPlannerPolicy):
    agent_id = "memory_reflection"

    def choose_from_candidates(self, candidates: list[str], state: TraceState, prefer_cost: bool = True) -> str:
        scenario_id = self.scenario["scenario_id"]
        if scenario_id in {"lunch_meeting_time_pressure", "memory_dependent_place_choice", "closed_poi_replacement"}:
            if "quiet_cafe" in candidates:
                return "quiet_cafe"
        if scenario_id == "avoid_crowd_event" and "park" in candidates:
            return "park"
        return super().choose_from_candidates(candidates, state, prefer_cost)

    def build_queue(self) -> list[str]:
        scenario_id = self.scenario["scenario_id"]
        scripted = {
            "lunch_meeting_time_pressure": ["quiet_cafe"],
            "memory_dependent_place_choice": ["quiet_cafe"],
            "closed_poi_replacement": ["quiet_cafe"],
            "avoid_crowd_event": ["park", "market"],
            "unexpected_friend_encounter": ["market", "pharmacy"],
        }
        if scenario_id in scripted:
            return scripted[scenario_id]
        return super().build_queue()

    def next_action(self, state: TraceState) -> Action:
        if self.scenario["scenario_id"] == "closed_poi_replacement" and state.time < parse_time("15:30"):
            return Action("dwell", minutes=parse_time("15:30") - state.time, reason="wait for the closure update before choosing a fallback")
        if self.scenario["scenario_id"] == "unexpected_friend_encounter":
            if state.location == "market" and not state.interactions:
                return Action("interact", to="casey", minutes=8, reason="use memory that Casey gives concise useful updates")
        return super().next_action(state)


def dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if item and item not in seen:
            seen.add(item)
            out.append(item)
    return out


def has_visited(state: TraceState, location: str) -> bool:
    return any(entry["location"] == location for entry in state.entries)


def has_arrived(state: TraceState, location: str) -> bool:
    return any(visit["location"] == location for visit in state.visits)


def has_entered(state: TraceState, location: str) -> bool:
    return state.inside_location == location or has_visited(state, location)


def has_used_service(state: TraceState, location: str, service: str | None = None) -> bool:
    return any(
        record["location"] == location
        and (service is None or record.get("service") == service)
        for record in state.services
    )


def has_purchased(state: TraceState, location: str, item: str | None = None) -> bool:
    return any(
        record["location"] == location
        and (item is None or record.get("item") == item)
        for record in state.purchases
    )


def record_visit(state: TraceState, location: str, at_time: int, kind: str = "visit") -> None:
    state.visits.append({"location": location, "time": at_time, "kind": kind})


def record_entry(state: TraceState, location: str, at_time: int, kind: str = "enter") -> None:
    state.entries.append({"location": location, "time": at_time, "kind": kind})


def append_violation(state: TraceState, kind: str, detail: dict[str, Any]) -> None:
    state.violations.append({"kind": kind, **detail})


def classify_failure(kind: str) -> str:
    mapping = {
        "blocked_edge": "impossible_route",
        "unreachable_move": "impossible_route",
        "closed_location": "closed_place_action",
        "budget_negative": "money_budget_failure",
        "enter_not_at_location": "invalid_state_transition",
        "duplicate_enter": "done_state_loop",
        "service_without_entry": "invalid_state_transition",
        "duplicate_service": "done_state_loop",
        "dwell_without_entry": "invalid_state_transition",
        "unpaid_service_required": "money_budget_failure",
        "invalid_explicit_path": "impossible_route",
        "episode_overtime": "time_budget_failure",
        "unknown_action": "plausible_but_invalid_rationale",
        "invalid_model_action": "plausible_but_invalid_rationale",
    }
    return mapping.get(kind, "other_constraint_failure")


def failure_taxonomy_counts(state: TraceState) -> dict[str, int]:
    counts: dict[str, int] = {}
    for violation in state.violations:
        failure_type = classify_failure(violation["kind"])
        counts[failure_type] = counts.get(failure_type, 0) + 1
    if has_done_state_loop(state):
        counts["done_state_loop"] = counts.get("done_state_loop", 0) + 1
    if has_social_derailment(state):
        counts["social_derailment"] = counts.get("social_derailment", 0) + 1
    if has_goal_drift(state):
        counts["goal_drift"] = counts.get("goal_drift", 0) + 1
    return dict(sorted(counts.items()))


def has_done_state_loop(state: TraceState) -> bool:
    repeated_completion_actions: dict[tuple[str, str, str], int] = {}
    for action in state.actions:
        payload = action["action"]
        kind = payload.get("kind")
        if kind not in {"buy", "use_service"}:
            continue
        target = payload.get("target") or action.get("start_location", "")
        label = payload.get("item") if kind == "buy" else payload.get("service")
        key = (str(kind), str(target), str(label or ""))
        repeated_completion_actions[key] = repeated_completion_actions.get(key, 0) + 1
    return any(count > 1 for count in repeated_completion_actions.values())


def has_social_derailment(state: TraceState) -> bool:
    return bool(state.interactions) and any(
        condition.get("score", 0.0) < 1.0
        for condition in getattr(state, "_condition_scores", [])
        if condition["type"] not in {"bounded_social_interaction"}
    )


def has_goal_drift(state: TraceState) -> bool:
    unfinished_weight = sum(
        float(condition.get("weight", 0.0))
        for condition in getattr(state, "_condition_scores", [])
        if condition.get("score", 0.0) < 1.0
    )
    return unfinished_weight >= 0.5 and not state.violations


def action_plausibility(action: dict[str, Any]) -> float:
    payload = action.get("action", {})
    kind = payload.get("kind")
    if kind in {"unknown_action", "invalid_model_action"}:
        return 0.0
    if kind not in {
        "move",
        "enter",
        "use_service",
        "buy",
        "dwell",
        "message",
        "interact",
        "finish",
        "abandon",
    }:
        return 0.25
    reason = str(payload.get("reason", "") or "")
    if reason.strip():
        return 1.0
    return 0.75 if kind in {"finish", "abandon"} else 0.6


def plan_plausibility_score(state: TraceState) -> float:
    non_finish = [
        action
        for action in state.actions
        if action["action"]["kind"] not in {"finish", "abandon"}
    ]
    if not non_finish:
        return 0.0
    return round(sum(action_plausibility(action) for action in non_finish) / len(non_finish), 3)


def city_false_continue_score(state: TraceState) -> float:
    false_continue_failures = {
        "impossible_route",
        "closed_place_action",
        "money_budget_failure",
        "time_budget_failure",
    }
    counts = failure_taxonomy_counts(state)
    continued_after_violation = False
    first_violation_step: int | None = None
    for action in state.actions:
        if action.get("violations") and first_violation_step is None:
            first_violation_step = int(action["step"])
    if first_violation_step is not None:
        continued_after_violation = any(
            int(action["step"]) > first_violation_step
            and action["action"]["kind"] not in {"finish", "abandon"}
            for action in state.actions
        )
    if any(counts.get(kind, 0) for kind in false_continue_failures) and continued_after_violation:
        return 1.0
    return 0.0


def execute_action(world: CityWorld, scenario: dict[str, Any], state: TraceState, action: Action) -> None:
    before = state.time
    entry: dict[str, Any] = {
        "scenario_id": state.scenario_id,
        "agent_type": state.agent_type,
        "step": len(state.actions) + 1,
        "start_time": format_time(before),
        "start_location": state.location,
        "action": action.__dict__,
    }

    if action.kind == "move" and action.target:
        invalid_explicit_path = False
        if action.path:
            path = list(action.path)
            invalid_explicit_path = (
                path[0] != state.location
                or path[-1] != action.target
                or any(node not in world.locations for node in path)
                or any(not any(neighbor == dst for neighbor, _ in world.graph[src]) for src, dst in zip(path, path[1:]))
            )
            minutes = (
                float("inf")
                if invalid_explicit_path
                else sum(
                    next(weight for neighbor, weight in world.graph[src] if neighbor == dst)
                    for src, dst in zip(path, path[1:])
                )
            )
        else:
            avoid_blocks = state.agent_type != "llm_direct_actor"
            path, minutes = world.shortest_path(
                state.location,
                action.target,
                scenario,
                state.time,
                avoid_active_blocks=avoid_blocks,
            )
        if invalid_explicit_path:
            append_violation(
                state,
                "invalid_explicit_path",
                {"from": state.location, "to": action.target, "path": action.path},
            )
        elif minutes == float("inf") or path == [state.location] and state.location != action.target:
            append_violation(state, "unreachable_move", {"from": state.location, "to": action.target, "time": format_time(state.time)})
        else:
            if path and path[-1] != state.location:
                state.inside_location = None
            for src, dst in zip(path, path[1:]):
                edge = normalize_edge((src, dst))
                edge_minutes = next(weight for neighbor, weight in world.graph[src] if neighbor == dst)
                depart_time = state.time
                arrive_time = state.time + int(edge_minutes)
                if world.edge_blocked_during(scenario, edge, depart_time, arrive_time):
                    append_violation(
                        state,
                        "blocked_edge",
                        {
                            "edge": list(edge),
                            "depart_time": format_time(depart_time),
                            "arrive_time": format_time(arrive_time),
                            "agent_type": state.agent_type,
                        },
                    )
                state.time += int(edge_minutes)
                state.location = dst
                state.traversals.append({"from": src, "to": dst, "arrive_time": state.time, "minutes": int(edge_minutes)})
                record_visit(state, dst, state.time, kind="pass_through" if dst != action.target else "arrival")
    elif action.kind == "enter":
        target = action.target or state.location
        state.time += 1
        if target != state.location:
            append_violation(
                state,
                "enter_not_at_location",
                {"location": state.location, "target": target, "time": format_time(state.time)},
            )
        elif state.inside_location == target:
            append_violation(
                state,
                "duplicate_enter",
                {"location": target, "time": format_time(state.time)},
            )
        elif not world.is_open(target, state.time, scenario):
            append_violation(
                state,
                "closed_location",
                {"location": target, "time": format_time(state.time)},
            )
        else:
            state.inside_location = target
            record_entry(state, target, state.time)
    elif action.kind in {"use_service", "buy"}:
        target = action.target or state.location
        duration = max(1, action.minutes or 5)
        state.time += duration
        label = (action.service if action.kind == "use_service" else action.item).strip()
        label = label or ("general_service" if action.kind == "use_service" else "item")
        if target != state.location or state.inside_location != target:
            append_violation(
                state,
                "service_without_entry",
                {
                    "action": action.kind,
                    "location": state.location,
                    "target": target,
                    "time": format_time(state.time),
                },
            )
        elif not world.is_open(target, state.time, scenario):
            append_violation(
                state,
                "closed_location",
                {"location": target, "time": format_time(state.time)},
            )
        else:
            payment_key = f"{action.kind}:{target}:{label}"
            if payment_key in state.paid_services:
                append_violation(
                    state,
                    "duplicate_service",
                    {"action": action.kind, "location": target, "label": label},
                )
            else:
                cost = world.location_cost(target)
                state.budget -= cost
                state.paid_services.add(payment_key)
                record = {
                    "location": target,
                    "time": state.time,
                    "cost": cost,
                    "budget_after": state.budget,
                }
                if action.kind == "use_service":
                    state.services.append({**record, "service": label})
                else:
                    state.purchases.append({**record, "item": label})
                if state.budget < 0:
                    append_violation(
                        state,
                        "budget_negative",
                        {"location": target, "budget": state.budget},
                    )
    elif action.kind == "dwell":
        minutes = max(1, action.minutes)
        state.time += minutes
        if state.inside_location != state.location:
            append_violation(
                state,
                "dwell_without_entry",
                {"location": state.location, "time": format_time(state.time)},
            )
        elif world.location_cost(state.location) > 0 and not (
            has_used_service(state, state.location) or has_purchased(state, state.location)
        ):
            append_violation(
                state,
                "unpaid_service_required",
                {"location": state.location, "time": format_time(state.time)},
            )
        else:
            state.dwell[state.location] += minutes
            record_visit(state, state.location, state.time, kind="dwell")
            if state.location == "coworking" and state.dwell[state.location] >= 45:
                state.completed_work = True
    elif action.kind == "message":
        state.messages.append({"to": action.to, "content": action.content, "time": state.time})
        state.time += 2
    elif action.kind == "interact":
        minutes = max(1, action.minutes)
        state.interactions.append({"with": action.to, "minutes": minutes, "time": state.time})
        state.time += minutes
    elif action.kind == "finish":
        pass
    elif action.kind == "abandon":
        state.abandonments.append(
            {"time": state.time, "location": state.location, "reason": action.reason}
        )
    else:
        append_violation(state, "unknown_action", {"action": action.kind})

    if before <= state.end_time < state.time:
        append_violation(
            state,
            "episode_overtime",
            {"end_time": format_time(state.end_time), "actual_time": format_time(state.time)},
        )

    if before < state.time:
        for event in scenario.get("events", []):
            event_time = parse_time(event["time"])
            if before <= event_time <= state.time and action.kind in {
                "move",
                "enter",
                "use_service",
                "buy",
                "dwell",
                "message",
                "interact",
            }:
                if state.agent_type != "llm_direct_actor":
                    state.replanned_after_event = True

    entry.update(
        {
            "end_time": format_time(state.time),
            "end_location": state.location,
            "budget": round(state.budget, 2),
            "violations": list(state.violations),
        }
    )
    state.actions.append(entry)


def visit_times(state: TraceState, locations: list[str], include_start: bool = True) -> list[int]:
    location_set = set(locations)
    return [
        entry["time"]
        for entry in state.entries
        if entry["location"] in location_set and (include_start or entry.get("kind") != "start")
    ]


def presence_times(state: TraceState, locations: list[str]) -> list[int]:
    location_set = set(locations)
    times = visit_times(state, locations)
    times.extend(
        visit["time"]
        for visit in state.visits
        if visit["location"] in location_set and visit.get("kind") == "dwell"
    )
    return times


def condition_success(condition: dict[str, Any], state: TraceState, scenario: dict[str, Any]) -> float:
    ctype = condition["type"]
    if ctype == "visit_location":
        return float(bool(visit_times(state, [condition["location"]], include_start=not condition.get("ignore_start", False))))
    if ctype == "visit_location_any_of":
        return float(bool(visit_times(state, condition["location_any_of"])))
    if ctype == "visit_before":
        deadline = parse_time(condition["deadline"])
        times = visit_times(state, [condition["location"]], include_start=not condition.get("ignore_start", False))
        return float(any(t <= deadline for t in times))
    if ctype == "visit_open_location":
        start, end = [parse_time(v) for v in condition["time_window"]]
        return float(
            any(
                start <= time <= end
                for time in presence_times(state, condition["location_any_of"])
            )
        )
    if ctype == "do_not_enter_closed_location":
        start, end = [parse_time(v) for v in condition["time_window"]]
        return float(not any(start <= t <= end for t in visit_times(state, [condition["location"]])))
    if ctype == "dwell_minutes":
        locations = condition.get("location_any_of") or [condition.get("location")]
        dwell = sum(state.dwell.get(loc, 0) for loc in locations)
        return float(dwell >= condition["min_minutes"])
    if ctype == "buy_item":
        return float(
            has_purchased(state, condition["location"], condition.get("item"))
        )
    if ctype == "use_service_at":
        return float(
            has_used_service(state, condition["location"], condition.get("service"))
        )
    if ctype == "co_presence":
        start, end = [parse_time(v) for v in condition["time_window"]]
        return float(
            any(
                start <= time <= end
                for time in presence_times(state, condition["location_any_of"])
            )
        )
    if ctype == "budget_at_least":
        return float(state.budget >= condition["min_remaining"])
    if ctype == "avoid_when_possible":
        return float(not visit_times(state, condition["avoid_locations"]))
    if ctype == "avoid_after_time":
        after = parse_time(condition["after"])
        return float(not any(t >= after for t in visit_times(state, condition["avoid_locations"])))
    if ctype == "no_feasibility_violation":
        return float(not state.violations)
    if ctype == "avoid_blocked_edge":
        edge = normalize_edge(condition["edge"])
        start, end = [parse_time(v) for v in condition["time_window"]]
        for traversal in state.traversals:
            if normalize_edge((traversal["from"], traversal["to"])) == edge and start <= traversal["arrive_time"] <= end:
                return 0.0
        return 1.0
    if ctype == "replan_after_event":
        return float(state.replanned_after_event and not any(v["kind"] == "blocked_edge" for v in state.violations))
    if ctype == "send_message":
        return float(any(msg.get("to") == condition["to"] for msg in state.messages))
    if ctype == "no_infeasible_social_commitment":
        accepted = any("come to the theatre" in msg.get("content", "").lower() for msg in state.messages)
        return float(not accepted and not any(v["kind"] == "budget_negative" for v in state.violations))
    if ctype == "bounded_social_interaction":
        minutes = sum(i.get("minutes", 0) for i in state.interactions if i.get("with") == condition["with"])
        return float(0 < minutes <= condition["max_minutes"])
    if ctype == "episode_complete_before":
        return float(state.time <= parse_time(condition["deadline"]))
    return 0.0


def condition_evidence(condition: dict[str, Any], state: TraceState) -> list[dict[str, Any]]:
    ctype = condition["type"]
    if ctype == "buy_item":
        return [
            record
            for record in state.purchases
            if record["location"] == condition["location"]
            and (not condition.get("item") or record.get("item") == condition["item"])
        ]
    if ctype == "visit_open_location":
        start, end = [parse_time(value) for value in condition["time_window"]]
        return [
            {"location": location, "time": time, "kind": "presence"}
            for location in condition["location_any_of"]
            for time in presence_times(state, [location])
            if start <= time <= end
        ]
    if ctype == "use_service_at":
        return [
            record
            for record in state.services
            if record["location"] == condition["location"]
            and (
                not condition.get("service")
                or record.get("service") == condition["service"]
            )
        ]
    if ctype == "dwell_minutes":
        locations = condition.get("location_any_of") or [condition.get("location")]
        return [
            {"location": location, "minutes": state.dwell.get(location, 0)}
            for location in locations
            if state.dwell.get(location, 0) > 0
        ]
    if ctype == "co_presence":
        start, end = [parse_time(value) for value in condition["time_window"]]
        return [
            {"location": location, "time": time, "kind": "presence"}
            for location in condition["location_any_of"]
            for time in presence_times(state, [location])
            if start <= time <= end
        ]
    locations = condition.get("location_any_of") or [condition.get("location")]
    locations = [location for location in locations if location]
    if locations:
        include_start = not bool(condition.get("ignore_start", False))
        return [
            entry
            for entry in state.entries
            if entry["location"] in locations
            and (include_start or entry.get("kind") != "start")
        ]
    if ctype == "send_message":
        return [message for message in state.messages if message.get("to") == condition["to"]]
    if ctype == "bounded_social_interaction":
        return [
            interaction
            for interaction in state.interactions
            if interaction.get("with") == condition["with"]
        ]
    return []


def score_trace(world: CityWorld, scenario: dict[str, Any], state: TraceState) -> dict[str, Any]:
    condition_scores: list[dict[str, Any]] = []
    weighted = 0.0
    for condition in scenario["success_conditions"]:
        score = condition_success(condition, state, scenario)
        weighted += score * float(condition["weight"])
        condition_scores.append(
            {
                "id": condition["id"],
                "type": condition["type"],
                "score": score,
                "weight": condition["weight"],
                "evidence": condition_evidence(condition, state),
            }
        )
    setattr(state, "_condition_scores", condition_scores)

    action_count = max(
        1,
        len(
            [
                action
                for action in state.actions
                if action["action"]["kind"] not in {"finish", "abandon"}
            ]
        ),
    )
    violation_rate = min(1.0, len(state.violations) / action_count)
    plan_plausibility = plan_plausibility_score(state)
    failure_counts = failure_taxonomy_counts(state)
    impossible_failures = sum(failure_counts.values())
    impossible_trace_rate = round(min(1.0, impossible_failures / action_count), 3)
    trace_feasibility = round(1.0 - impossible_trace_rate, 3)
    plausibility_feasibility_gap = round(max(0.0, plan_plausibility - trace_feasibility), 3)
    actual_travel = sum(t.get("minutes", 0) for t in state.traversals)
    target_locations = []
    for condition in scenario["success_conditions"]:
        if "location" in condition:
            target_locations.append(condition["location"])
        elif "location_any_of" in condition:
            target_locations.append(condition["location_any_of"][0])
    target_locations = [loc for loc in dedupe(target_locations) if loc in world.locations]
    optimal = 0.0
    cursor = scenario["agents"][0]["start_location"]
    for target in target_locations:
        _, distance = world.shortest_path(cursor, target, scenario, parse_time(scenario["episode"]["start_time"]))
        if distance != float("inf"):
            optimal += distance
            cursor = target
    travel_efficiency = 1.0 if actual_travel <= 0 else max(0.0, min(1.0, optimal / actual_travel))

    replan_conditions = [c for c in condition_scores if c["type"] == "replan_after_event"]
    social_conditions = [c for c in condition_scores if c["type"] in {"co_presence", "send_message", "bounded_social_interaction", "no_infeasible_social_commitment"}]

    metrics = {
        "plan_plausibility": plan_plausibility,
        "trace_feasibility": trace_feasibility,
        "plausibility_feasibility_gap": plausibility_feasibility_gap,
        "impossible_trace_rate": impossible_trace_rate,
        "city_false_continue": city_false_continue_score(state),
        "goal_completion": round(weighted, 3),
        "feasibility_violation": round(violation_rate, 3),
        "replanning_success": round(sum(c["score"] for c in replan_conditions) / len(replan_conditions), 3) if replan_conditions else None,
        "travel_efficiency": round(travel_efficiency, 3),
        "budget_consistency": float(state.budget >= 0),
        "intention_consistency": round(weighted * (1.0 - violation_rate), 3),
        "social_appropriateness": round(sum(c["score"] for c in social_conditions) / len(social_conditions), 3) if social_conditions else None,
        "done_state_loop_rate": float(has_done_state_loop(state)),
        "social_derailment_rate": float(has_social_derailment(state)),
    }
    return {
        "metrics": metrics,
        "conditions": condition_scores,
        "failure_taxonomy": failure_counts,
        "final_state": {
            "time": format_time(state.time),
            "location": state.location,
            "inside_location": state.inside_location,
            "budget": round(state.budget, 2),
            "entries": state.entries,
            "services": state.services,
            "purchases": state.purchases,
            "abandonments": state.abandonments,
            "violations": state.violations,
        },
    }


def run_trace(world: CityWorld, scenario: dict[str, Any], agent_type: str, llm_config: Path | None = None) -> dict[str, Any]:
    primary = next(agent for agent in scenario["agents"] if agent["agent_id"] == scenario["primary_agent"])
    policy_registry: dict[str, Any] = {
        "utility_planner": UtilityPlannerPolicy,
        "llm_direct_actor": DirectActorOfflineProxy,
        "reactive_replanner": ReactiveReplannerPolicy,
        "memory_reflection": MemoryReflectionPolicy,
        "api_llm_direct_actor": APILLMDirectActor,
        "api_llm_plan_then_act": APILLMPlanThenAct,
        "api_llm_reactive_replanner": APILLMReactiveReplanner,
    }
    if agent_type == "gatsim_official_planner":
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from external_adapters.gatsim_official import GATSimOfficialPlannerAdapter

        policy_registry[agent_type] = GATSimOfficialPlannerAdapter
    elif agent_type == "sotopia_official_llm_agent":
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from external_adapters.sotopia_official import SOTOPIAOfficialLLMAgentAdapter

        policy_registry[agent_type] = SOTOPIAOfficialLLMAgentAdapter
    elif agent_type == "generative_agents_official_planner":
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from external_adapters.generative_agents_official import (
            GenerativeAgentsOfficialPlannerAdapter,
        )

        policy_registry[agent_type] = GenerativeAgentsOfficialPlannerAdapter
    elif agent_type == "agentsociety_official_plan_blocks":
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from external_adapters.agentsociety_official import (
            AgentSocietyOfficialPlanBlocksAdapter,
        )

        policy_registry[agent_type] = AgentSocietyOfficialPlanBlocksAdapter
    policy_cls = policy_registry[agent_type]
    state = TraceState(
        scenario_id=scenario["scenario_id"],
        agent_id=primary["agent_id"],
        agent_type=agent_type,
        time=parse_time(scenario["episode"]["start_time"]),
        end_time=parse_time(scenario["episode"]["end_time"]),
        location=primary["start_location"],
        budget=float(primary["budget"]),
    )
    state.inside_location = state.location
    record_visit(state, state.location, state.time, kind="start")
    record_entry(state, state.location, state.time, kind="start")
    policy = policy_cls(world, scenario, primary, llm_config=llm_config)
    for _ in range(int(scenario["episode"]["max_steps"])):
        action_value = policy.next_action(state)
        action = Action(**action_value) if isinstance(action_value, dict) else action_value
        execute_action(world, scenario, state, action)
        if action.kind in {"finish", "abandon"} or state.time >= state.end_time:
            break
    scored = score_trace(world, scenario, state)
    llm = getattr(policy, "llm", None)
    llm_telemetry = list(getattr(llm, "telemetry", []))
    llm_summary = (
        llm.telemetry_summary()
        if llm is not None and hasattr(llm, "telemetry_summary")
        else None
    )
    model_info = dict(policy.model_info) if policy.model_info else None
    if model_info is not None and llm_summary is not None:
        model_info["llm_telemetry_summary"] = llm_summary
    return {
        "scenario_id": scenario["scenario_id"],
        "scenario_title": scenario["title"],
        "family": scenario["family"],
        "agent_type": agent_type,
        "trace": state.actions,
        "visits": state.visits,
        "traversals": state.traversals,
        "messages": state.messages,
        "interactions": state.interactions,
        "entries": state.entries,
        "services": state.services,
        "purchases": state.purchases,
        "abandonments": state.abandonments,
        "model_info": model_info,
        "llm_telemetry": llm_telemetry,
        **scored,
    }


def load_worlds(config: dict[str, Any]) -> dict[str, CityWorld]:
    worlds = {}
    for world_ref in config["worlds"]:
        raw = load_json(ROOT / world_ref)
        worlds[raw["world_id"]] = CityWorld(raw)
    return worlds


def write_outputs(results: list[dict[str, Any]], results_dir: Path) -> None:
    results_dir.mkdir(parents=True, exist_ok=True)
    write_json(results_dir / "traces.json", results)
    with (results_dir / "traces.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for result in results:
            f.write(json.dumps(result, ensure_ascii=False) + "\n")

    metric_keys = [
        "plan_plausibility",
        "trace_feasibility",
        "plausibility_feasibility_gap",
        "impossible_trace_rate",
        "city_false_continue",
        "goal_completion",
        "feasibility_violation",
        "replanning_success",
        "travel_efficiency",
        "budget_consistency",
        "intention_consistency",
        "social_appropriateness",
        "done_state_loop_rate",
        "social_derailment_rate",
    ]
    summary_path = results_dir / "summary.csv"
    with summary_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "scenario_id",
                "family",
                "agent_type",
                *metric_keys,
                "final_time",
                "final_location",
                "final_budget",
                "violations",
                "failure_taxonomy",
                "llm_calls",
                "llm_latency_seconds",
                "llm_input_tokens",
                "llm_output_tokens",
                "llm_total_tokens",
                "llm_usage_complete",
            ],
        )
        writer.writeheader()
        for result in results:
            row = {
                "scenario_id": result["scenario_id"],
                "family": result["family"],
                "agent_type": result["agent_type"],
                "final_time": result["final_state"]["time"],
                "final_location": result["final_state"]["location"],
                "final_budget": result["final_state"]["budget"],
                "violations": len(result["final_state"]["violations"]),
                "failure_taxonomy": json.dumps(result.get("failure_taxonomy", {}), ensure_ascii=False, sort_keys=True),
            }
            telemetry = (result.get("model_info") or {}).get(
                "llm_telemetry_summary", {}
            )
            row.update(
                {
                    "llm_calls": telemetry.get("calls", 0),
                    "llm_latency_seconds": telemetry.get("latency_seconds", 0),
                    "llm_input_tokens": telemetry.get("input_tokens", 0),
                    "llm_output_tokens": telemetry.get("output_tokens", 0),
                    "llm_total_tokens": telemetry.get("total_tokens", 0),
                    "llm_usage_complete": telemetry.get("usage_complete", False),
                }
            )
            row.update(result["metrics"])
            writer.writerow(row)

    aggregate: dict[str, dict[str, float]] = {}
    for agent_type in sorted({r["agent_type"] for r in results}):
        agent_results = [r for r in results if r["agent_type"] == agent_type]
        aggregate[agent_type] = {}
        for key in metric_keys:
            values = [r["metrics"][key] for r in agent_results if r["metrics"][key] is not None]
            if values:
                aggregate[agent_type][key] = round(sum(values) / len(values), 3)
    write_json(results_dir / "aggregate.json", aggregate)

    telemetry_aggregate: dict[str, dict[str, Any]] = {}
    for agent_type in sorted({r["agent_type"] for r in results}):
        summaries = [
            (result.get("model_info") or {}).get("llm_telemetry_summary")
            for result in results
            if result["agent_type"] == agent_type
        ]
        summaries = [summary for summary in summaries if isinstance(summary, dict)]
        if not summaries:
            continue
        telemetry_aggregate[agent_type] = {
            "traces": len(summaries),
            "calls": sum(int(summary.get("calls", 0)) for summary in summaries),
            "latency_seconds": round(
                sum(float(summary.get("latency_seconds", 0)) for summary in summaries),
                3,
            ),
            "input_tokens": sum(
                int(summary.get("input_tokens", 0)) for summary in summaries
            ),
            "output_tokens": sum(
                int(summary.get("output_tokens", 0)) for summary in summaries
            ),
            "total_tokens": sum(
                int(summary.get("total_tokens", 0)) for summary in summaries
            ),
            "usage_complete": all(
                bool(summary.get("usage_complete", False)) for summary in summaries
            ),
        }
    write_json(results_dir / "telemetry_aggregate.json", telemetry_aggregate)

    with (results_dir / "summary.md").open("w", encoding="utf-8", newline="\n") as f:
        has_api = any(r["agent_type"].startswith("api_llm_") for r in results)
        external_agents = sorted(
            {
                r["agent_type"]
                for r in results
                if (r.get("model_info") or {}).get("integration_level")
            }
        )
        f.write("# CityIntent v0.2 Trace Results\n\n")
        if has_api:
            f.write("This run includes `api_llm_*` agents, which call a configured real model provider.\n\n")
        if external_agents:
            names = ", ".join(f"`{agent}`" for agent in external_agents)
            f.write(f"This run includes verified external-framework adapters: {names}.\n\n")
        f.write(
            "Controlled agents without `model_info` remain offline architecture proxies, "
            "not real model or external-framework results.\n\n"
        )
        f.write("## Aggregate Metrics\n\n")
        f.write("| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |\n")
        f.write("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n")
        for agent_type, metrics in aggregate.items():
            f.write(
                f"| {agent_type} | {metrics.get('plan_plausibility', '')} | {metrics.get('trace_feasibility', '')} | "
                f"{metrics.get('plausibility_feasibility_gap', '')} | {metrics.get('impossible_trace_rate', '')} | "
                f"{metrics.get('city_false_continue', '')} | {metrics.get('goal_completion', '')} | "
                f"{metrics.get('feasibility_violation', '')} | {metrics.get('replanning_success', '')} | "
                f"{metrics.get('travel_efficiency', '')} | {metrics.get('budget_consistency', '')} | "
                f"{metrics.get('intention_consistency', '')} | {metrics.get('social_appropriateness', '')} | "
                f"{metrics.get('done_state_loop_rate', '')} | {metrics.get('social_derailment_rate', '')} |\n"
            )
        f.write("\n## Scenario-Level Rows\n\n")
        f.write("See `summary.csv` and `traces.jsonl` in this directory.\n")
        if telemetry_aggregate:
            f.write("\n## LLM Telemetry\n\n")
            f.write("| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |\n")
            f.write("|---|---:|---:|---:|---:|---:|---|\n")
            for agent_type, telemetry in telemetry_aggregate.items():
                f.write(
                    f"| {agent_type} | {telemetry['calls']} | {telemetry['latency_seconds']} | "
                    f"{telemetry['input_tokens']} | {telemetry['output_tokens']} | "
                    f"{telemetry['total_tokens']} | {telemetry['usage_complete']} |\n"
                )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--agents",
        default="utility_planner,llm_direct_actor,reactive_replanner,memory_reflection",
        help="Comma-separated agent ids to run. Includes controlled baselines, api_llm_* policies, and verified external adapters.",
    )
    parser.add_argument("--results-dir", default=str(DEFAULT_RESULTS_DIR))
    parser.add_argument("--llm-config", type=Path, default=None, help="LLM config for provider-backed and external adapted agents.")
    parser.add_argument("--scenario-ids", default="", help="Comma-separated scenario ids to run.")
    parser.add_argument("--limit-scenarios", type=int, default=None)
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow replacing an existing traces.json in the result directory.",
    )
    args = parser.parse_args()

    results_dir = Path(args.results_dir)
    if (results_dir / "traces.json").exists() and not args.overwrite:
        raise SystemExit(
            f"Refusing to overwrite archived run: {results_dir}. "
            "Choose a new --results-dir or pass --overwrite explicitly."
        )

    requested_agents = [item.strip() for item in args.agents.split(",") if item.strip()]
    implemented_agents = {
        "utility_planner",
        "llm_direct_actor",
        "reactive_replanner",
        "memory_reflection",
        "api_llm_direct_actor",
        "api_llm_plan_then_act",
        "api_llm_reactive_replanner",
        "gatsim_official_planner",
        "sotopia_official_llm_agent",
        "generative_agents_official_planner",
        "agentsociety_official_plan_blocks",
    }
    unknown = sorted(set(requested_agents) - implemented_agents)
    if unknown:
        raise SystemExit(f"Unsupported agents for this runner: {', '.join(unknown)}")
    llm_agents = {
        "gatsim_official_planner",
        "sotopia_official_llm_agent",
        "generative_agents_official_planner",
        "agentsociety_official_plan_blocks",
    }
    if any(agent.startswith("api_llm_") or agent in llm_agents for agent in requested_agents) and args.llm_config is None:
        raise SystemExit("--llm-config is required when running API-backed or adapted external agents")

    config = load_json(ROOT / "benchmark_config.json")
    worlds = load_worlds(config)
    scenarios = [load_json(path) for path in sorted((ROOT / config["scenario_dir"]).glob("*.json"))]
    scenario_ids = {item.strip() for item in args.scenario_ids.split(",") if item.strip()}
    if scenario_ids:
        scenarios = [scenario for scenario in scenarios if scenario["scenario_id"] in scenario_ids]
    if args.limit_scenarios is not None:
        scenarios = scenarios[: args.limit_scenarios]
    results: list[dict[str, Any]] = []
    for scenario in scenarios:
        world = worlds[scenario["world_id"]]
        for agent_type in requested_agents:
            results.append(run_trace(world, scenario, agent_type, llm_config=args.llm_config))
    write_outputs(results, results_dir)
    llm_config = load_json(args.llm_config) if args.llm_config else None
    if llm_config:
        llm_config = {
            key: value
            for key, value in llm_config.items()
            if key == "api_key_env" or "key" not in key.lower()
        }
    write_json(
        results_dir / "run_manifest.json",
        {
            "timestamp": datetime.now().astimezone().isoformat(timespec="seconds"),
            "benchmark_id": config["benchmark_id"],
            "benchmark_version": config["version"],
            "runner": str(Path(__file__).resolve()),
            "agents": requested_agents,
            "scenario_ids": [scenario["scenario_id"] for scenario in scenarios],
            "llm_config_path": str(args.llm_config) if args.llm_config else None,
            "llm_config": llm_config,
            "results_dir": str(results_dir),
            "overwrite": args.overwrite,
        },
    )
    print(f"Wrote {len(results)} traces to {args.results_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
