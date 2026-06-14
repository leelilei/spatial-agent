#!/usr/bin/env python3
"""Score normalized probe responses against SMGA diagnostic probes.

The scorer is deliberately mechanical: it checks structured response fields and
case-insensitive text markers against the locked success/failure conditions in
`probes.json`.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def normalize_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str)]
    return []


def contains_marker(text: str, marker: str) -> bool:
    return marker.lower() in text.lower()


def score_probe(probe: dict[str, Any], response: dict[str, Any] | None) -> dict[str, Any]:
    probe_id = probe["probe_id"]
    if response is None:
        return {
            "probe_id": probe_id,
            "success": False,
            "excluded_from_headline": bool(probe.get("no_history_solvability_flag")),
            "failure_reasons": ["missing response"],
            "success_details": {},
            "failure_details": {},
        }

    success_condition = probe.get("success_condition", {})
    failure_condition = probe.get("failure_condition", {})
    response_text = str(response.get("response_text", ""))
    chosen_affordance = response.get("chosen_affordance_type")
    # v0.2: judge acceptability against the set of all expressed affordances, not a
    # single winner-take-all label. Fall back to the single label for older drafts.
    affordance_candidates = set(normalize_list(response.get("affordance_candidates")))
    if not affordance_candidates and chosen_affordance:
        affordance_candidates = {chosen_affordance}
    target_entities = set(normalize_list(response.get("target_entities")))
    current_status_used = set(normalize_list(response.get("current_status_used")))

    failure_details: dict[str, Any] = {}
    failure_reasons: list[str] = []

    # Forbidden affordance is judged on the single dominant label only: an
    # incidental keyword mention in a verbose answer should not count as the
    # agent *choosing* a forbidden action. Acceptable affordance (below) is the
    # lenient candidate-set check.
    forbidden_affordances = set(normalize_list(failure_condition.get("forbidden_affordance_types")))
    if chosen_affordance in forbidden_affordances:
        failure_details["forbidden_affordance"] = chosen_affordance
        failure_reasons.append(f"forbidden affordance: {chosen_affordance}")

    forbidden_markers = normalize_list(failure_condition.get("forbidden_response_markers"))
    matched_forbidden_markers = [
        marker for marker in forbidden_markers if contains_marker(response_text, marker)
    ]
    if matched_forbidden_markers:
        failure_details["forbidden_markers"] = matched_forbidden_markers
        failure_reasons.append("forbidden response marker present")

    success_details: dict[str, Any] = {}
    acceptable_affordances = set(normalize_list(success_condition.get("acceptable_affordance_types")))
    if acceptable_affordances:
        matched_acceptable = sorted(acceptable_affordances & affordance_candidates)
        affordance_ok = bool(matched_acceptable)
        success_details["affordance_ok"] = affordance_ok
        success_details["matched_acceptable_affordances"] = matched_acceptable
        success_details["affordance_candidates"] = sorted(affordance_candidates)
        if not affordance_ok:
            failure_reasons.append("no acceptable affordance expressed")

    required_targets = set(normalize_list(success_condition.get("required_target_entities")))
    if required_targets:
        missing_targets = sorted(required_targets - target_entities)
        success_details["missing_target_entities"] = missing_targets
        if missing_targets:
            failure_reasons.append("required target entity missing")

    required_statuses = set(normalize_list(success_condition.get("required_current_status")))
    if required_statuses:
        status_ok = bool(required_statuses & current_status_used)
        success_details["status_ok"] = status_ok
        if not status_ok:
            failure_reasons.append("required current status not represented")

    required_markers = normalize_list(success_condition.get("required_response_markers"))
    matched_markers = [marker for marker in required_markers if contains_marker(response_text, marker)]
    minimum_marker_count = int(success_condition.get("minimum_marker_count", len(required_markers)))
    marker_ok = len(matched_markers) >= minimum_marker_count
    success_details["matched_markers"] = matched_markers
    success_details["minimum_marker_count"] = minimum_marker_count
    success_details["marker_ok"] = marker_ok
    if not marker_ok:
        failure_reasons.append("not enough required response markers")

    return {
        "probe_id": probe_id,
        "success": not failure_reasons,
        "excluded_from_headline": bool(probe.get("no_history_solvability_flag")),
        "failure_reasons": failure_reasons,
        "success_details": success_details,
        "failure_details": failure_details,
    }


def score(seed_dir: Path, responses_path: Path) -> dict[str, Any]:
    probes_doc = load_json(seed_dir / "probes.json")
    responses_doc = load_json(responses_path)

    probes = probes_doc.get("probes", [])
    responses = {
        response.get("probe_id"): response
        for response in responses_doc.get("responses", [])
        if isinstance(response, dict)
    }

    results = [score_probe(probe, responses.get(probe.get("probe_id"))) for probe in probes]
    headline_results = [result for result in results if not result["excluded_from_headline"]]
    successes = sum(1 for result in headline_results if result["success"])
    total = len(headline_results)
    success_rate = successes / total if total else 0.0

    return {
        "scenario_id": probes_doc.get("scenario_id"),
        "condition_id": responses_doc.get("condition_id", "unknown"),
        "responses_path": str(responses_path),
        "seed_dir": str(seed_dir),
        "headline_successes": successes,
        "headline_total": total,
        "headline_success_rate": success_rate,
        "results": results,
    }


def print_human_summary(result: dict[str, Any]) -> None:
    rate = result["headline_success_rate"]
    print(
        f"{result['condition_id']}: "
        f"{result['headline_successes']}/{result['headline_total']} "
        f"headline probes passed ({rate:.1%})"
    )
    for item in result["results"]:
        status = "PASS" if item["success"] else "FAIL"
        excluded = " excluded" if item["excluded_from_headline"] else ""
        print(f"  {item['probe_id']}: {status}{excluded}")
        for reason in item["failure_reasons"]:
            print(f"    - {reason}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Score SMGA diagnostic probe responses.")
    parser.add_argument("seed_dir", type=Path, help="Path to a scenario seed directory.")
    parser.add_argument("responses_json", type=Path, help="Path to normalized probe responses JSON.")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit full scoring result as JSON instead of a human summary.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        result = score(args.seed_dir, args.responses_json)
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    else:
        print_human_summary(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

