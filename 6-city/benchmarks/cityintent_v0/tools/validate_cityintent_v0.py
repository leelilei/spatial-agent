"""Validate the CityAgency CityIntent release-candidate package.

This is a dependency-free smoke validator. It checks structural consistency,
world graph reachability, metric coverage, and whether every scenario probes the
first four agent architectures.
"""

from __future__ import annotations

import argparse
import heapq
import hashlib
import json
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SUPPORTED_CONDITION_TYPES = {
    "visit_location",
    "visit_location_any_of",
    "visit_before",
    "visit_open_location",
    "do_not_enter_closed_location",
    "dwell_minutes",
    "buy_item",
    "purchase_at",
    "obtain_at",
    "use_service_at",
    "co_presence",
    "budget_at_least",
    "avoid_when_possible",
    "avoid_after_time",
    "no_feasibility_violation",
    "avoid_blocked_edge",
    "replan_after_event",
    "send_message",
    "recall_memory",
    "no_infeasible_social_commitment",
    "bounded_social_interaction",
    "episode_complete_before",
}
SUPPORTED_CONDITION_ROLES = {"outcome", "process", "constraint"}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def parse_time(value: str) -> int:
    try:
        hour_text, minute_text = value.split(":", 1)
        hour = int(hour_text)
        minute = int(minute_text)
    except ValueError as exc:
        raise ValueError(f"invalid time {value!r}") from exc
    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        raise ValueError(f"invalid time {value!r}")
    return hour * 60 + minute


def build_graph(world: dict[str, Any]) -> dict[str, list[tuple[str, float]]]:
    graph: dict[str, list[tuple[str, float]]] = defaultdict(list)
    for edge in world.get("edges", []):
        a = edge["from"]
        b = edge["to"]
        minutes = float(edge["minutes"])
        graph[a].append((b, minutes))
        graph[b].append((a, minutes))
    return graph


def dijkstra(graph: dict[str, list[tuple[str, float]]], start: str) -> dict[str, float]:
    distances: dict[str, float] = {start: 0.0}
    heap: list[tuple[float, str]] = [(0.0, start)]
    while heap:
        current_distance, node = heapq.heappop(heap)
        if current_distance != distances[node]:
            continue
        for neighbor, weight in graph.get(node, []):
            next_distance = current_distance + weight
            if next_distance < distances.get(neighbor, float("inf")):
                distances[neighbor] = next_distance
                heapq.heappush(heap, (next_distance, neighbor))
    return distances


def connected_component(graph: dict[str, list[tuple[str, float]]], start: str) -> set[str]:
    seen = {start}
    queue: deque[str] = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor, _ in graph.get(node, []):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return seen


def collect_location_refs(condition: dict[str, Any]) -> list[str]:
    refs: list[str] = []
    for key in ("location",):
        if isinstance(condition.get(key), str):
            refs.append(condition[key])
    for key in ("location_any_of", "avoid_locations"):
        value = condition.get(key)
        if isinstance(value, list):
            refs.extend(item for item in value if isinstance(item, str))
    edge = condition.get("edge")
    if isinstance(edge, list):
        refs.extend(item for item in edge if isinstance(item, str))
    return refs


def paired_common_payload(scenario: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in scenario.items()
        if key not in {"scenario_id", "events", "perturbation_pair"}
    }


def payload_sha256(value: dict[str, Any]) -> str:
    encoded = json.dumps(value, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--benchmark-config",
        type=Path,
        default=ROOT / "benchmark_config.json",
        help="Benchmark configuration to validate. Relative paths are resolved from its directory.",
    )
    args = parser.parse_args(argv)
    errors: list[str] = []
    warnings: list[str] = []

    config_path = args.benchmark_config.resolve()
    config_root = config_path.parent
    config = load_json(config_path)
    metric_ids = {metric["id"] for metric in config.get("metrics", [])}
    required_metric_ids = set(config.get("validation", {}).get("required_metric_ids", []))
    required_agent_ids = set(config.get("validation", {}).get("required_agent_ids", []))
    configured_agent_ids = {agent["id"] for agent in config.get("agents_under_test", [])}

    if not required_metric_ids <= metric_ids:
        errors.append("benchmark_config validation.required_metric_ids contains unknown metrics")
    if not required_agent_ids <= configured_agent_ids:
        errors.append("benchmark_config validation.required_agent_ids contains unknown agents")

    worlds_by_id: dict[str, dict[str, Any]] = {}
    graphs_by_world_id: dict[str, dict[str, list[tuple[str, float]]]] = {}
    location_ids_by_world_id: dict[str, set[str]] = {}

    for world_ref in config.get("worlds", []):
        world_path = config_root / world_ref
        if not world_path.exists():
            errors.append(f"missing world file: {world_ref}")
            continue
        world = load_json(world_path)
        world_id = world.get("world_id")
        if not isinstance(world_id, str):
            errors.append(f"{world_ref}: missing world_id")
            continue
        locations = world.get("locations", [])
        location_ids = [loc.get("id") for loc in locations]
        duplicates = [loc_id for loc_id, count in Counter(location_ids).items() if count > 1]
        if duplicates:
            errors.append(f"{world_ref}: duplicate location ids {duplicates}")
        location_id_set = {loc_id for loc_id in location_ids if isinstance(loc_id, str)}

        for loc in locations:
            open_window = loc.get("open")
            if isinstance(open_window, list) and len(open_window) == 2:
                try:
                    parse_time(open_window[0])
                    parse_time(open_window[1])
                except ValueError as exc:
                    errors.append(f"{world_ref}: {loc.get('id')}: {exc}")

        for edge in world.get("edges", []):
            a = edge.get("from")
            b = edge.get("to")
            minutes = edge.get("minutes")
            if a not in location_id_set or b not in location_id_set:
                errors.append(f"{world_ref}: edge references unknown location {a!r}->{b!r}")
            if not isinstance(minutes, (int, float)) or minutes <= 0:
                errors.append(f"{world_ref}: edge {a!r}->{b!r} has invalid minutes")

        graph = build_graph(world)
        if location_id_set:
            reached = connected_component(graph, next(iter(location_id_set)))
            missing = sorted(location_id_set - reached)
            if missing:
                errors.append(f"{world_ref}: disconnected locations {missing}")

        worlds_by_id[world_id] = world
        graphs_by_world_id[world_id] = graph
        location_ids_by_world_id[world_id] = location_id_set

    scenario_dir = config_root / config.get("scenario_dir", "scenarios")
    scenario_paths = (
        sorted(
            path
            for split in config["scenario_splits"]
            for path in (scenario_dir / split).rglob("*.json")
        )
        if config.get("scenario_splits")
        else sorted(scenario_dir.rglob("*.json"))
    )
    min_scenarios = int(config.get("validation", {}).get("min_scenarios", 0))
    if len(scenario_paths) < min_scenarios:
        errors.append(f"expected at least {min_scenarios} scenarios, found {len(scenario_paths)}")

    seen_scenario_ids: set[str] = set()
    family_counts: Counter[str] = Counter()
    metric_coverage: set[str] = set()
    reachability_checks = 0
    perturbation_pairs: dict[str, list[tuple[Path, dict[str, Any]]]] = defaultdict(list)

    for path in scenario_paths:
        rel = path.relative_to(ROOT)
        scenario = load_json(path)
        scenario_id = scenario.get("scenario_id")
        if not isinstance(scenario_id, str):
            errors.append(f"{rel}: missing scenario_id")
            continue
        if scenario_id in seen_scenario_ids:
            errors.append(f"{rel}: duplicate scenario_id {scenario_id}")
        seen_scenario_ids.add(scenario_id)

        pair = scenario.get("perturbation_pair")
        if pair is not None:
            pair_id = pair.get("pair_id")
            variant = pair.get("variant")
            event_types = pair.get("treatment_event_types")
            if not isinstance(pair_id, str) or not pair_id:
                errors.append(f"{rel}: perturbation_pair requires pair_id")
            elif variant not in {"control", "treatment"}:
                errors.append(f"{rel}: perturbation_pair has invalid variant {variant!r}")
            elif not isinstance(event_types, list) or not event_types:
                errors.append(f"{rel}: perturbation_pair requires treatment_event_types")
            else:
                perturbation_pairs[pair_id].append((path, scenario))

        world_id = scenario.get("world_id")
        if world_id not in worlds_by_id:
            errors.append(f"{rel}: unknown world_id {world_id!r}")
            continue
        graph = graphs_by_world_id[world_id]
        location_ids = location_ids_by_world_id[world_id]

        episode = scenario.get("episode", {})
        try:
            start_time = parse_time(episode.get("start_time", ""))
            end_time = parse_time(episode.get("end_time", ""))
            if end_time <= start_time:
                errors.append(f"{rel}: episode end_time must be after start_time")
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            start_time = 0
            end_time = 0
        duration = max(0, end_time - start_time)

        agents = scenario.get("agents", [])
        agent_ids = [agent.get("agent_id") for agent in agents]
        agent_id_set = {agent_id for agent_id in agent_ids if isinstance(agent_id, str)}
        if len(agent_id_set) != len(agent_ids):
            errors.append(f"{rel}: duplicate or invalid agent ids")
        primary_agent = scenario.get("primary_agent")
        if primary_agent not in agent_id_set:
            errors.append(f"{rel}: primary_agent {primary_agent!r} is not in agents")

        primary_start = None
        for agent in agents:
            start_location = agent.get("start_location")
            if start_location not in location_ids:
                errors.append(f"{rel}: agent {agent.get('agent_id')} starts at unknown location {start_location!r}")
            if agent.get("agent_id") == primary_agent:
                primary_start = start_location
            for known_location in agent.get("known_locations", []):
                if known_location not in location_ids:
                    errors.append(f"{rel}: agent {agent.get('agent_id')} knows unknown location {known_location!r}")

        for event in scenario.get("events", []):
            event_location = event.get("location")
            if event_location is not None and event_location not in location_ids:
                errors.append(f"{rel}: event {event.get('type')} references unknown location {event_location!r}")
            effect = event.get("effect", {})
            for affected_location in effect.get("affected_locations", []):
                if affected_location not in location_ids:
                    errors.append(f"{rel}: event {event.get('type')} affects unknown location {affected_location!r}")
            blocked_edge = effect.get("blocked_edge")
            if isinstance(blocked_edge, list):
                for node in blocked_edge:
                    if node not in location_ids:
                        errors.append(f"{rel}: blocked_edge references unknown location {node!r}")
            for agent in effect.get("agents_present", []):
                if agent not in agent_id_set:
                    errors.append(
                        f"{rel}: event {event.get('type')} references unknown present agent {agent!r}"
                    )

        critical_locations = scenario.get("critical_locations", [])
        for loc in critical_locations:
            if loc not in location_ids:
                errors.append(f"{rel}: unknown critical location {loc!r}")

        weight_sum = 0.0
        role_counts: Counter[str] = Counter()
        for condition in scenario.get("success_conditions", []):
            condition_type = condition.get("type")
            condition_role = condition.get("role")
            if condition_type not in SUPPORTED_CONDITION_TYPES:
                errors.append(
                    f"{rel}: condition {condition.get('id')} has unsupported type {condition_type!r}"
                )
            if condition_role not in SUPPORTED_CONDITION_ROLES:
                errors.append(
                    f"{rel}: condition {condition.get('id')} has unsupported role {condition_role!r}"
                )
            else:
                role_counts[condition_role] += 1
            if condition_type == "buy_item" and not condition.get("item"):
                errors.append(
                    f"{rel}: buy_item condition {condition.get('id')} requires item"
                )
            if condition_type == "obtain_at" and not (
                condition.get("item") or condition.get("service")
            ):
                errors.append(
                    f"{rel}: obtain_at condition {condition.get('id')} requires item or service"
                )
            if condition_type == "co_presence":
                if len(condition.get("agents", [])) < 2:
                    errors.append(
                        f"{rel}: co_presence condition {condition.get('id')} requires at least two agents"
                    )
                if not condition.get("location_any_of") and not condition.get("location"):
                    errors.append(
                        f"{rel}: co_presence condition {condition.get('id')} requires a location"
                    )
                if not condition.get("time_window"):
                    errors.append(
                        f"{rel}: co_presence condition {condition.get('id')} requires time_window"
                    )
            if condition_type == "bounded_social_interaction" and not isinstance(
                condition.get("max_minutes"), int
            ):
                errors.append(
                    f"{rel}: bounded_social_interaction condition {condition.get('id')} requires max_minutes"
                )
            for time_key in ("deadline", "after"):
                if condition.get(time_key) is not None:
                    try:
                        parse_time(condition[time_key])
                    except (AttributeError, TypeError, ValueError) as exc:
                        errors.append(f"{rel}: condition {condition.get('id')}: {exc}")
            if condition.get("time_window") is not None:
                window = condition.get("time_window")
                if not isinstance(window, list) or len(window) != 2:
                    errors.append(
                        f"{rel}: condition {condition.get('id')} requires a two-value time_window"
                    )
                else:
                    try:
                        window_start, window_end = [parse_time(value) for value in window]
                        if window_end < window_start:
                            errors.append(
                                f"{rel}: condition {condition.get('id')} time_window is reversed"
                            )
                    except (AttributeError, TypeError, ValueError) as exc:
                        errors.append(f"{rel}: condition {condition.get('id')}: {exc}")
            weight = condition.get("weight")
            if not isinstance(weight, (int, float)) or weight <= 0:
                errors.append(f"{rel}: condition {condition.get('id')} has invalid weight")
            else:
                weight_sum += float(weight)
            for loc in collect_location_refs(condition):
                if loc not in location_ids:
                    errors.append(f"{rel}: condition {condition.get('id')} references unknown location {loc!r}")
            for agent_key in ("agent", "to", "with"):
                value = condition.get(agent_key)
                if isinstance(value, str) and value not in agent_id_set:
                    errors.append(f"{rel}: condition {condition.get('id')} references unknown agent {value!r}")
            for agent in condition.get("agents", []):
                if agent not in agent_id_set:
                    errors.append(f"{rel}: condition {condition.get('id')} references unknown agent {agent!r}")
        if scenario.get("success_conditions") and not role_counts["outcome"]:
            errors.append(f"{rel}: at least one outcome condition is required")
        if scenario.get("success_conditions") and abs(weight_sum - 1.0) > 0.01:
            warnings.append(f"{rel}: success condition weights sum to {weight_sum:.2f}, not 1.00")

        scenario_metrics = set(scenario.get("scoring_metrics", []))
        unknown_metrics = sorted(scenario_metrics - metric_ids)
        if unknown_metrics:
            errors.append(f"{rel}: unknown scoring metrics {unknown_metrics}")
        if len(scenario_metrics) < 4:
            warnings.append(f"{rel}: fewer than four scoring metrics")
        metric_coverage.update(scenario_metrics)

        architecture_probes = scenario.get("architecture_probes", {})
        probe_ids = set(architecture_probes.keys())
        if probe_ids != required_agent_ids:
            errors.append(
                f"{rel}: architecture_probes must cover {sorted(required_agent_ids)}, found {sorted(probe_ids)}"
            )

        if isinstance(scenario.get("family"), str):
            family_counts[scenario["family"]] += 1

        if primary_start in location_ids:
            distances = dijkstra(graph, primary_start)
            for loc in critical_locations:
                reachability_checks += 1
                if distances.get(loc, float("inf")) == float("inf"):
                    errors.append(f"{rel}: {primary_start!r} cannot reach critical location {loc!r}")
                elif duration and distances[loc] > duration:
                    warnings.append(
                        f"{rel}: shortest path from {primary_start} to {loc} is {distances[loc]:.0f} min, "
                        f"longer than episode duration {duration} min"
                    )

    missing_global_metrics = sorted(required_metric_ids - metric_coverage)
    if missing_global_metrics:
        errors.append(f"scenario set does not cover required metrics {missing_global_metrics}")

    for pair_id, members in sorted(perturbation_pairs.items()):
        variants = {
            scenario["perturbation_pair"]["variant"]: (path, scenario)
            for path, scenario in members
        }
        if len(members) != 2 or set(variants) != {"control", "treatment"}:
            errors.append(
                f"perturbation pair {pair_id!r} must contain exactly one control and one treatment"
            )
            continue
        control_path, control = variants["control"]
        treatment_path, treatment = variants["treatment"]
        if payload_sha256(paired_common_payload(control)) != payload_sha256(
            paired_common_payload(treatment)
        ):
            errors.append(
                f"perturbation pair {pair_id!r} differs outside scenario_id, events, or pair metadata"
            )
        if control.get("events"):
            errors.append(f"{control_path.relative_to(ROOT)}: paired control must have no events")
        declared = set(treatment["perturbation_pair"]["treatment_event_types"])
        actual = {event.get("type") for event in treatment.get("events", [])}
        if not actual or actual != declared:
            errors.append(
                f"{treatment_path.relative_to(ROOT)}: treatment events {sorted(actual)} "
                f"do not match declared types {sorted(declared)}"
            )

    if errors:
        print("CityIntent v0 validation failed:\n")
        for error in errors:
            print(f"ERROR: {error}")
        if warnings:
            print("\nWarnings:")
            for warning in warnings:
                print(f"WARNING: {warning}")
        return 1

    print(f"CityIntent {config.get('version', 'unknown')} validation passed.")
    print(f"- worlds: {len(worlds_by_id)}")
    print(f"- scenarios: {len(scenario_paths)}")
    print(f"- scenario families: {dict(sorted(family_counts.items()))}")
    print(f"- agent architectures: {', '.join(sorted(required_agent_ids))}")
    print(f"- metric coverage: {', '.join(sorted(metric_coverage))}")
    print(f"- reachability checks: {reachability_checks}")
    print(f"- perturbation pairs: {len(perturbation_pairs)}")
    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"WARNING: {warning}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
