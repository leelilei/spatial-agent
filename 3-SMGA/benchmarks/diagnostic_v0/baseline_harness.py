#!/usr/bin/env python3
"""Prepare M0 baseline prompt bundles for SMGA diagnostic probes.

This harness does not call a model. It creates condition-specific prompts and
scorer-readable response templates so the later model-calling runner can focus
only on API execution and normalization.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from benchmark_loader import ScenarioPackage, load_seed


BASELINE_CONDITIONS = ("M0_GA", "M0_prompted")


@dataclass(frozen=True)
class BaselineCondition:
    condition_id: str
    description: str
    reflection_instruction: str


CONDITIONS: dict[str, BaselineCondition] = {
    "M0_GA": BaselineCondition(
        condition_id="M0_GA",
        description="GA-style memory stream with ordinary reflection.",
        reflection_instruction=(
            "Use the event history as an ordinary generative-agent memory stream. "
            "Reflect briefly on the memories that seem relevant, then answer the probe."
        ),
    ),
    "M0_prompted": BaselineCondition(
        condition_id="M0_prompted",
        description="Prompted reflection over social-memory categories.",
        reflection_instruction=(
            "Use the event history as an ordinary generative-agent memory stream. "
            "Before answering, explicitly consider relevant people, places, relationships, "
            "activities, routines, norms, and information states. Then answer the probe."
        ),
    ),
}


def build_prompt_bundle(package: ScenarioPackage, condition: BaselineCondition) -> list[dict[str, Any]]:
    entity_catalog = format_entity_catalog(package)
    event_history = format_event_history(package)

    return [
        {
            "scenario_id": package.scenario_id,
            "seed_id": package.seed_id,
            "condition_id": condition.condition_id,
            "probe_id": probe["probe_id"],
            "probe_type": probe.get("probe_type"),
            "acting_agent": probe.get("acting_agent"),
            "system_prompt": build_system_prompt(condition),
            "user_prompt": build_user_prompt(
                condition=condition,
                entity_catalog=entity_catalog,
                event_history=event_history,
                probe=probe,
            ),
            "expected_raw_output_schema": {
                "probe_id": probe["probe_id"],
                "response_text": "natural-language answer to the probe",
            },
        }
        for probe in package.probes
    ]


def build_response_template(package: ScenarioPackage, condition_id: str) -> dict[str, Any]:
    return {
        "scenario_id": package.scenario_id,
        "seed_id": package.seed_id,
        "condition_id": condition_id,
        "model_config": {
            "provider": "TODO",
            "model": "TODO_PIN_BEFORE_STAGE_1",
            "temperature": 0,
        },
        "responses": [
            {
                "probe_id": probe["probe_id"],
                "response_text": "",
                "chosen_affordance_type": "",
                "target_entities": [],
                "current_status_used": [],
                "raw_model_output": None,
                "normalization_notes": "Fill after model execution and condition-blind normalization.",
            }
            for probe in package.probes
        ],
    }


def build_system_prompt(condition: BaselineCondition) -> str:
    return (
        "You are running an SMGA diagnostic baseline condition. "
        "Your task is to answer the user's probe using only the provided scripted event history. "
        "Do not mention hidden benchmark labels, success conditions, or scoring rules. "
        "Return valid JSON with exactly two keys: probe_id and response_text."
    )


def build_user_prompt(
    *,
    condition: BaselineCondition,
    entity_catalog: str,
    event_history: str,
    probe: dict[str, Any],
) -> str:
    return "\n\n".join(
        [
            f"Condition: {condition.condition_id}",
            f"Condition description: {condition.description}",
            f"Reflection instruction: {condition.reflection_instruction}",
            "Entity catalog:",
            entity_catalog,
            "Scripted event history:",
            event_history,
            "Probe:",
            str(probe["prompt"]),
            "Output JSON:",
            json.dumps(
                {
                    "probe_id": probe["probe_id"],
                    "response_text": "your answer here",
                },
                ensure_ascii=False,
            ),
        ]
    )


def format_entity_catalog(package: ScenarioPackage) -> str:
    lines = []
    for entity in package.entities:
        aliases = entity.get("aliases") or []
        alias_text = f" aliases={aliases}" if aliases else ""
        lines.append(
            "- {entity_id} ({entity_type}): {display_name}{alias_text}. {description}".format(
                entity_id=entity.get("entity_id"),
                entity_type=entity.get("entity_type"),
                display_name=entity.get("display_name"),
                alias_text=alias_text,
                description=entity.get("description", ""),
            )
        )
    return "\n".join(lines)


def format_event_history(package: ScenarioPackage) -> str:
    lines = []
    for event in package.events:
        actor_names = ", ".join(entity_name(package, entity_id) for entity_id in event.get("actors", []))
        location = entity_name(package, str(event.get("location", "")))
        topic = entity_name(package, str(event.get("topic", "")))
        lines.append(
            "- {event_id} | {time} | {event_type} | actors: {actors} | location: {location} | "
            "topic: {topic} | {content}".format(
                event_id=event.get("event_id"),
                time=event.get("time"),
                event_type=event.get("event_type"),
                actors=actor_names,
                location=location,
                topic=topic,
                content=event.get("content"),
            )
        )
    return "\n".join(lines)


def entity_name(package: ScenarioPackage, entity_id: str) -> str:
    entity = package.entity_by_id.get(entity_id)
    if not entity:
        return entity_id
    return f"{entity.get('display_name')} [{entity_id}]"


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
            file.write("\n")


def write_json(path: Path, data: dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as file:
        json.dump(data, file, indent=2, ensure_ascii=False, sort_keys=True)
        file.write("\n")


def selected_conditions(condition_arg: str) -> list[str]:
    if condition_arg == "all":
        return list(BASELINE_CONDITIONS)
    return [condition_arg]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare SMGA M0 baseline prompt bundles.")
    parser.add_argument("seed_dir", type=Path, help="Path to a scenario seed directory.")
    parser.add_argument(
        "--condition",
        choices=(*BASELINE_CONDITIONS, "all"),
        default="all",
        help="Baseline condition to prepare. Defaults to all.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("tmp") / "smga_baseline_harness",
        help="Directory for generated prompt bundles and response templates.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        package = load_seed(args.seed_dir)
    except (OSError, json.JSONDecodeError, TypeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if not package.validation.ok:
        print("error: seed validation failed; refusing to prepare baseline prompts", file=sys.stderr)
        for error in package.validation.errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    for condition_id in selected_conditions(args.condition):
        condition = CONDITIONS[condition_id]
        prompt_path = output_dir / f"{package.seed_id}_{condition_id}_prompts.jsonl"
        template_path = output_dir / f"{package.seed_id}_{condition_id}_responses.template.json"

        prompt_bundle = build_prompt_bundle(package, condition)
        response_template = build_response_template(package, condition_id)
        write_jsonl(prompt_path, prompt_bundle)
        write_json(template_path, response_template)

        print(f"{condition_id}: wrote {len(prompt_bundle)} prompts")
        print(f"  prompts: {prompt_path}")
        print(f"  response template: {template_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
