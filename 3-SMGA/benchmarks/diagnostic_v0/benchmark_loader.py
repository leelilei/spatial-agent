#!/usr/bin/env python3
"""Load SMGA diagnostic benchmark scenario packages.

The loader is the shared entrypoint for baseline runners, SMGA treatment
modules, and scorers. It keeps file parsing in one place and optionally runs
the existing seed validator before returning a typed package object.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from validate_seed import SeedValidator


@dataclass(frozen=True)
class ValidationReport:
    ok: bool
    warnings: tuple[str, ...]
    errors: tuple[str, ...]


@dataclass(frozen=True)
class ScenarioPackage:
    seed_dir: Path
    metadata: dict[str, Any]
    entities: tuple[dict[str, Any], ...]
    events: tuple[dict[str, Any], ...]
    gold_facts: tuple[dict[str, Any], ...]
    contradictions: tuple[dict[str, Any], ...]
    probes: tuple[dict[str, Any], ...]
    validation: ValidationReport

    @property
    def scenario_id(self) -> str:
        return str(self.metadata.get("scenario_id", "unknown_scenario"))

    @property
    def seed_id(self) -> str:
        return str(self.metadata.get("seed_id", self.seed_dir.name))

    @property
    def entity_by_id(self) -> dict[str, dict[str, Any]]:
        return index_by_id(self.entities, "entity_id")

    @property
    def event_by_id(self) -> dict[str, dict[str, Any]]:
        return index_by_id(self.events, "event_id")

    @property
    def fact_by_id(self) -> dict[str, dict[str, Any]]:
        return index_by_id(self.gold_facts, "fact_id")

    @property
    def contradiction_by_id(self) -> dict[str, dict[str, Any]]:
        return index_by_id(self.contradictions, "contradiction_id")

    @property
    def probe_by_id(self) -> dict[str, dict[str, Any]]:
        return index_by_id(self.probes, "probe_id")

    def summary_dict(self) -> dict[str, Any]:
        return {
            "scenario_id": self.scenario_id,
            "seed_id": self.seed_id,
            "seed_dir": str(self.seed_dir),
            "entities": len(self.entities),
            "events": len(self.events),
            "gold_facts": len(self.gold_facts),
            "contradictions": len(self.contradictions),
            "probes": len(self.probes),
            "validation_ok": self.validation.ok,
            "validation_warnings": list(self.validation.warnings),
            "validation_errors": list(self.validation.errors),
        }


def load_seed(seed_dir: Path, *, validate: bool = True) -> ScenarioPackage:
    seed_dir = seed_dir.resolve()
    validation = validate_seed(seed_dir) if validate else ValidationReport(True, (), ())

    metadata = load_json_object(seed_dir / "metadata.json")
    entities_doc = load_json_object(seed_dir / "entities.json")
    facts_doc = load_json_object(seed_dir / "gold_facts.json")
    contradictions_doc = load_json_object(seed_dir / "contradictions.json")
    probes_doc = load_json_object(seed_dir / "probes.json")

    return ScenarioPackage(
        seed_dir=seed_dir,
        metadata=metadata,
        entities=tuple(expect_object_list(entities_doc, "entities.json", "entities")),
        events=tuple(load_jsonl(seed_dir / "event_log.jsonl")),
        gold_facts=tuple(expect_object_list(facts_doc, "gold_facts.json", "gold_facts")),
        contradictions=tuple(
            expect_object_list(contradictions_doc, "contradictions.json", "contradictions")
        ),
        probes=tuple(expect_object_list(probes_doc, "probes.json", "probes")),
        validation=validation,
    )


def validate_seed(seed_dir: Path) -> ValidationReport:
    validator = SeedValidator(seed_dir)
    ok = validator.validate()
    return ValidationReport(
        ok=ok,
        warnings=tuple(validator.warnings),
        errors=tuple(validator.errors),
    )


def load_json_object(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise TypeError(f"{path} must contain a JSON object")
    return data


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as file:
        for line_no, line in enumerate(file, start=1):
            if not line.strip():
                continue
            record = json.loads(line)
            if not isinstance(record, dict):
                raise TypeError(f"{path}:{line_no} must contain a JSON object")
            records.append(record)
    return records


def expect_object_list(doc: dict[str, Any], filename: str, key: str) -> list[dict[str, Any]]:
    value = doc.get(key)
    if not isinstance(value, list):
        raise TypeError(f"{filename}.{key} must be a list")
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            raise TypeError(f"{filename}.{key}[{index}] must be an object")
    return value


def index_by_id(items: tuple[dict[str, Any], ...], id_field: str) -> dict[str, dict[str, Any]]:
    return {
        item[id_field]: item
        for item in items
        if isinstance(item.get(id_field), str) and item.get(id_field)
    }


def print_human_summary(package: ScenarioPackage) -> None:
    validation = "OK" if package.validation.ok else "FAILED"
    print(f"{package.scenario_id} / {package.seed_id}")
    print(f"entities: {len(package.entities)}")
    print(f"events: {len(package.events)}")
    print(f"gold facts: {len(package.gold_facts)}")
    print(f"contradictions: {len(package.contradictions)}")
    print(f"probes: {len(package.probes)}")
    print(f"validation: {validation}")
    for warning in package.validation.warnings:
        print(f"  warning: {warning}")
    for error in package.validation.errors:
        print(f"  error: {error}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Load an SMGA diagnostic benchmark seed.")
    parser.add_argument("seed_dir", type=Path, help="Path to a scenario seed directory.")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit the package summary as JSON instead of human-readable text.",
    )
    parser.add_argument(
        "--no-validate",
        action="store_true",
        help="Load the package without running validate_seed.py checks.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        package = load_seed(args.seed_dir, validate=not args.no_validate)
    except (OSError, json.JSONDecodeError, TypeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(package.summary_dict(), indent=2, ensure_ascii=False, sort_keys=True))
    else:
        print_human_summary(package)
    return 0 if package.validation.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
