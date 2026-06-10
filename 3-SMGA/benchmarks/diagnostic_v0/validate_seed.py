#!/usr/bin/env python3
"""Validate SMGA diagnostic scenario-package seeds.

This script intentionally has no third-party dependencies. It checks the v0.1
scenario package shape used by the first hand-authored diagnostic seeds.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_FILES = [
    "metadata.json",
    "entities.json",
    "event_log.jsonl",
    "gold_facts.json",
    "contradictions.json",
    "probes.json",
]

REQUIRED_METADATA_FIELDS = {
    "scenario_id",
    "seed_id",
    "benchmark_id",
    "schema_version",
    "phase_1_design",
    "simulated_horizon",
    "agent_count",
    "location_count",
    "held_out_patterns",
}

REQUIRED_ENTITY_FIELDS = {
    "entity_id",
    "entity_type",
    "display_name",
    "aliases",
    "description",
}

REQUIRED_EVENT_FIELDS = {
    "event_id",
    "scenario_id",
    "time",
    "event_type",
    "actors",
    "location",
    "topic",
    "content",
    "mentioned_entities",
    "gold_fact_ids",
}

REQUIRED_FACT_FIELDS = {
    "fact_id",
    "fact_type",
    "subject_entities",
    "claim",
    "supporting_evidence_ids",
    "contradicting_evidence_ids",
    "current_status",
    "validity_scope",
}

REQUIRED_CONTRADICTION_FIELDS = {
    "contradiction_id",
    "original_fact_id",
    "original_evidence_id",
    "contradicting_evidence_id",
    "contradiction_type",
    "expected_current_status",
}

REQUIRED_PROBE_FIELDS = {
    "probe_id",
    "probe_type",
    "acting_agent",
    "prompt",
    "required_prior_evidence_ids",
    "required_fact_ids",
    "success_condition",
    "failure_condition",
    "no_history_solvability_flag",
}

REQUIRED_SUCCESS_FIELDS = {
    "acceptable_affordance_types",
    "required_target_entities",
    "required_current_status",
    "required_response_markers",
}

REQUIRED_FAILURE_FIELDS = {
    "forbidden_affordance_types",
    "forbidden_response_markers",
}

PERSON_ENTITY_TYPE = "person"
PLACE_ENTITY_TYPE = "place"


class SeedValidator:
    def __init__(self, seed_dir: Path):
        self.seed_dir = seed_dir
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.metadata: dict[str, Any] = {}
        self.entities: list[dict[str, Any]] = []
        self.events: list[dict[str, Any]] = []
        self.facts: list[dict[str, Any]] = []
        self.contradictions: list[dict[str, Any]] = []
        self.probes: list[dict[str, Any]] = []

    def validate(self) -> bool:
        self._check_files()
        if self.errors:
            return False

        self._load_files()
        if self.errors:
            return False

        self._validate_metadata()
        self._validate_entities()
        self._validate_events()
        self._validate_facts()
        self._validate_contradictions()
        self._validate_probes()
        self._validate_package_requirements()
        return not self.errors

    def summary(self) -> str:
        return (
            f"entities={len(self.entities)} "
            f"events={len(self.events)} "
            f"facts={len(self.facts)} "
            f"contradictions={len(self.contradictions)} "
            f"probes={len(self.probes)}"
        )

    def _check_files(self) -> None:
        if not self.seed_dir.exists():
            self._error(f"seed directory does not exist: {self.seed_dir}")
            return
        if not self.seed_dir.is_dir():
            self._error(f"seed path is not a directory: {self.seed_dir}")
            return
        for filename in REQUIRED_FILES:
            if not (self.seed_dir / filename).is_file():
                self._error(f"missing required file: {filename}")

    def _load_files(self) -> None:
        self.metadata = self._load_json("metadata.json", expected_type=dict)
        entities_doc = self._load_json("entities.json", expected_type=dict)
        facts_doc = self._load_json("gold_facts.json", expected_type=dict)
        contradictions_doc = self._load_json("contradictions.json", expected_type=dict)
        probes_doc = self._load_json("probes.json", expected_type=dict)

        self.entities = self._expect_list(entities_doc, "entities.json", "entities")
        self.facts = self._expect_list(facts_doc, "gold_facts.json", "gold_facts")
        self.contradictions = self._expect_list(
            contradictions_doc, "contradictions.json", "contradictions"
        )
        self.probes = self._expect_list(probes_doc, "probes.json", "probes")
        self.events = self._load_jsonl("event_log.jsonl")

    def _validate_metadata(self) -> None:
        self._require_fields(self.metadata, REQUIRED_METADATA_FIELDS, "metadata")
        if self.metadata.get("phase_1_design") != "scripted_replay":
            self._error("metadata.phase_1_design must be scripted_replay")
        if not isinstance(self.metadata.get("held_out_patterns"), list):
            self._error("metadata.held_out_patterns must be a list")

    def _validate_entities(self) -> None:
        entity_ids = self._unique_ids(self.entities, "entity_id", "entity")
        for entity in self.entities:
            self._require_fields(entity, REQUIRED_ENTITY_FIELDS, f"entity {entity.get('entity_id')}")
            if not isinstance(entity.get("aliases"), list):
                self._error(f"entity {entity.get('entity_id')} aliases must be a list")
        if not any(entity.get("entity_type") == PERSON_ENTITY_TYPE for entity in self.entities):
            self._error("entities must include at least one person")
        if not any(entity.get("entity_type") == PLACE_ENTITY_TYPE for entity in self.entities):
            self._error("entities must include at least one place")
        if not entity_ids:
            self._error("entities must not be empty")

    def _validate_events(self) -> None:
        entity_ids = self.entity_ids
        fact_ids = self.fact_ids
        self._unique_ids(self.events, "event_id", "event")

        previous_time: tuple[int, int, int] | None = None
        for event in self.events:
            event_id = event.get("event_id")
            self._require_fields(event, REQUIRED_EVENT_FIELDS, f"event {event_id}")
            current_time = self._parse_time(event.get("time"), f"event {event_id}")
            if current_time is not None and previous_time is not None and current_time < previous_time:
                self._error(f"event {event_id} is out of chronological order")
            if current_time is not None:
                previous_time = current_time

            self._require_entity_refs(event.get("actors"), entity_ids, f"event {event_id}.actors")
            self._require_entity_ref(event.get("location"), entity_ids, f"event {event_id}.location")
            self._require_entity_ref(event.get("topic"), entity_ids, f"event {event_id}.topic")
            self._require_entity_refs(
                event.get("mentioned_entities"), entity_ids, f"event {event_id}.mentioned_entities"
            )
            self._require_fact_refs(event.get("gold_fact_ids"), fact_ids, f"event {event_id}.gold_fact_ids")

    def _validate_facts(self) -> None:
        entity_ids = self.entity_ids
        event_ids = self.event_ids
        self._unique_ids(self.facts, "fact_id", "fact")

        for fact in self.facts:
            fact_id = fact.get("fact_id")
            self._require_fields(fact, REQUIRED_FACT_FIELDS, f"fact {fact_id}")
            self._require_entity_refs(
                fact.get("subject_entities"), entity_ids, f"fact {fact_id}.subject_entities"
            )
            self._require_event_refs(
                fact.get("supporting_evidence_ids"), event_ids, f"fact {fact_id}.supporting_evidence_ids"
            )
            self._require_event_refs(
                fact.get("contradicting_evidence_ids"),
                event_ids,
                f"fact {fact_id}.contradicting_evidence_ids",
            )
            if not fact.get("supporting_evidence_ids"):
                self._error(f"fact {fact_id} must have at least one supporting evidence id")
            if not isinstance(fact.get("validity_scope"), dict):
                self._error(f"fact {fact_id}.validity_scope must be an object")

    def _validate_contradictions(self) -> None:
        fact_ids = self.fact_ids
        event_ids = self.event_ids
        event_order = {event["event_id"]: index for index, event in enumerate(self.events)}
        self._unique_ids(self.contradictions, "contradiction_id", "contradiction")

        for contradiction in self.contradictions:
            contradiction_id = contradiction.get("contradiction_id")
            self._require_fields(
                contradiction, REQUIRED_CONTRADICTION_FIELDS, f"contradiction {contradiction_id}"
            )
            self._require_fact_ref(
                contradiction.get("original_fact_id"),
                fact_ids,
                f"contradiction {contradiction_id}.original_fact_id",
            )
            original_event = contradiction.get("original_evidence_id")
            contradicting_event = contradiction.get("contradicting_evidence_id")
            self._require_event_ref(
                original_event, event_ids, f"contradiction {contradiction_id}.original_evidence_id"
            )
            self._require_event_ref(
                contradicting_event,
                event_ids,
                f"contradiction {contradiction_id}.contradicting_evidence_id",
            )
            if original_event in event_order and contradicting_event in event_order:
                if event_order[contradicting_event] <= event_order[original_event]:
                    self._error(
                        f"contradiction {contradiction_id} contradicting evidence must occur after original evidence"
                    )

    def _validate_probes(self) -> None:
        entity_ids = self.entity_ids
        event_ids = self.event_ids
        fact_ids = self.fact_ids
        self._unique_ids(self.probes, "probe_id", "probe")

        for probe in self.probes:
            probe_id = probe.get("probe_id")
            self._require_fields(probe, REQUIRED_PROBE_FIELDS, f"probe {probe_id}")
            self._require_entity_ref(probe.get("acting_agent"), entity_ids, f"probe {probe_id}.acting_agent")
            self._require_event_refs(
                probe.get("required_prior_evidence_ids"),
                event_ids,
                f"probe {probe_id}.required_prior_evidence_ids",
            )
            self._require_fact_refs(probe.get("required_fact_ids"), fact_ids, f"probe {probe_id}.required_fact_ids")

            success_condition = probe.get("success_condition")
            failure_condition = probe.get("failure_condition")
            if not isinstance(success_condition, dict):
                self._error(f"probe {probe_id}.success_condition must be an object")
                success_condition = {}
            if not isinstance(failure_condition, dict):
                self._error(f"probe {probe_id}.failure_condition must be an object")
                failure_condition = {}
            self._require_fields(
                success_condition, REQUIRED_SUCCESS_FIELDS, f"probe {probe_id}.success_condition"
            )
            self._require_fields(
                failure_condition, REQUIRED_FAILURE_FIELDS, f"probe {probe_id}.failure_condition"
            )
            self._require_entity_refs(
                success_condition.get("required_target_entities"),
                entity_ids,
                f"probe {probe_id}.success_condition.required_target_entities",
            )
            if probe.get("no_history_solvability_flag") is True:
                self._warning(f"probe {probe_id} is no-history solvable and must be excluded from headline metrics")

    def _validate_package_requirements(self) -> None:
        if len(self.contradictions) < 2:
            self._error("minimal diagnostic seed must include at least two planted contradictions")

        contradicted_fact_ids = {
            fact["fact_id"] for fact in self.facts if fact.get("contradicting_evidence_ids")
        }
        if self.facts:
            contradiction_fraction = len(contradicted_fact_ids) / len(self.facts)
            if contradiction_fraction < 0.25:
                self._error(
                    f"contradiction coverage is {contradiction_fraction:.2%}; expected at least 25%"
                )

    @property
    def entity_ids(self) -> set[str]:
        return {entity["entity_id"] for entity in self.entities if "entity_id" in entity}

    @property
    def event_ids(self) -> set[str]:
        return {event["event_id"] for event in self.events if "event_id" in event}

    @property
    def fact_ids(self) -> set[str]:
        return {fact["fact_id"] for fact in self.facts if "fact_id" in fact}

    def _load_json(self, filename: str, expected_type: type) -> Any:
        path = self.seed_dir / filename
        try:
            with path.open(encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError as exc:
            self._error(f"{filename} is invalid JSON: {exc}")
            return {} if expected_type is dict else []
        except OSError as exc:
            self._error(f"could not read {filename}: {exc}")
            return {} if expected_type is dict else []
        if not isinstance(data, expected_type):
            self._error(f"{filename} must be a {expected_type.__name__}")
            return {} if expected_type is dict else []
        return data

    def _load_jsonl(self, filename: str) -> list[dict[str, Any]]:
        path = self.seed_dir / filename
        records: list[dict[str, Any]] = []
        try:
            with path.open(encoding="utf-8") as file:
                for line_no, line in enumerate(file, start=1):
                    if not line.strip():
                        continue
                    try:
                        record = json.loads(line)
                    except json.JSONDecodeError as exc:
                        self._error(f"{filename}:{line_no} is invalid JSON: {exc}")
                        continue
                    if not isinstance(record, dict):
                        self._error(f"{filename}:{line_no} must be an object")
                        continue
                    records.append(record)
        except OSError as exc:
            self._error(f"could not read {filename}: {exc}")
        return records

    def _expect_list(self, doc: dict[str, Any], filename: str, key: str) -> list[dict[str, Any]]:
        value = doc.get(key)
        if not isinstance(value, list):
            self._error(f"{filename}.{key} must be a list")
            return []
        bad_indexes = [index for index, item in enumerate(value) if not isinstance(item, dict)]
        for index in bad_indexes:
            self._error(f"{filename}.{key}[{index}] must be an object")
        return [item for item in value if isinstance(item, dict)]

    def _unique_ids(self, items: list[dict[str, Any]], id_field: str, label: str) -> set[str]:
        seen: set[str] = set()
        for index, item in enumerate(items):
            value = item.get(id_field)
            if not isinstance(value, str) or not value:
                self._error(f"{label} at index {index} missing string {id_field}")
                continue
            if value in seen:
                self._error(f"duplicate {label} {id_field}: {value}")
            seen.add(value)
        return seen

    def _require_fields(self, item: dict[str, Any], fields: set[str], label: str) -> None:
        missing = sorted(field for field in fields if field not in item)
        if missing:
            self._error(f"{label} missing fields: {', '.join(missing)}")

    def _require_entity_ref(self, value: Any, entity_ids: set[str], label: str) -> None:
        if not isinstance(value, str):
            self._error(f"{label} must be a string entity id")
            return
        if value not in entity_ids:
            self._error(f"{label} references missing entity: {value}")

    def _require_entity_refs(self, values: Any, entity_ids: set[str], label: str) -> None:
        self._require_refs(values, entity_ids, label, "entity")

    def _require_event_ref(self, value: Any, event_ids: set[str], label: str) -> None:
        if not isinstance(value, str):
            self._error(f"{label} must be a string event id")
            return
        if value not in event_ids:
            self._error(f"{label} references missing event: {value}")

    def _require_event_refs(self, values: Any, event_ids: set[str], label: str) -> None:
        self._require_refs(values, event_ids, label, "event")

    def _require_fact_ref(self, value: Any, fact_ids: set[str], label: str) -> None:
        if not isinstance(value, str):
            self._error(f"{label} must be a string fact id")
            return
        if value not in fact_ids:
            self._error(f"{label} references missing fact: {value}")

    def _require_fact_refs(self, values: Any, fact_ids: set[str], label: str) -> None:
        self._require_refs(values, fact_ids, label, "fact")

    def _require_refs(self, values: Any, allowed_ids: set[str], label: str, ref_kind: str) -> None:
        if not isinstance(values, list):
            self._error(f"{label} must be a list")
            return
        for value in values:
            if not isinstance(value, str):
                self._error(f"{label} contains non-string {ref_kind} id")
            elif value not in allowed_ids:
                self._error(f"{label} references missing {ref_kind}: {value}")

    def _parse_time(self, value: Any, label: str) -> tuple[int, int, int] | None:
        if not isinstance(value, str):
            self._error(f"{label}.time must be a string")
            return None
        match = re.fullmatch(r"day_(\d+)_(\d{2}):(\d{2})", value)
        if not match:
            self._error(f"{label}.time must match day_N_HH:MM, got {value!r}")
            return None
        day, hour, minute = map(int, match.groups())
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            self._error(f"{label}.time has invalid clock value: {value}")
            return None
        return (day, hour, minute)

    def _error(self, message: str) -> None:
        self.errors.append(message)

    def _warning(self, message: str) -> None:
        self.warnings.append(message)


def discover_seed_dirs(root: Path) -> list[Path]:
    seeds_dir = root / "seeds"
    if not seeds_dir.is_dir():
        return []
    return sorted(path for path in seeds_dir.iterdir() if path.is_dir())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate SMGA diagnostic benchmark seeds.")
    parser.add_argument(
        "seed_dirs",
        nargs="*",
        type=Path,
        help="Seed directories to validate. Defaults to all directories under ./seeds.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(__file__).resolve().parent
    seed_dirs = args.seed_dirs or discover_seed_dirs(root)
    if not seed_dirs:
        print("No seed directories found.", file=sys.stderr)
        return 1

    all_ok = True
    for seed_dir in seed_dirs:
        validator = SeedValidator(seed_dir)
        ok = validator.validate()
        status = "OK" if ok else "FAILED"
        print(f"{seed_dir}: {status} ({validator.summary()})")
        for warning in validator.warnings:
            print(f"  warning: {warning}")
        for error in validator.errors:
            print(f"  error: {error}")
        all_ok = all_ok and ok

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

