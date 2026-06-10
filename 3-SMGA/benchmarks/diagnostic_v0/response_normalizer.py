#!/usr/bin/env python3
"""Normalize raw SMGA probe responses into scorer-readable fields.

This first normalizer is deliberately condition-blind and rule-based. It uses
the scenario entity catalog plus response text, but it does not inspect
`condition_id` or the probe success conditions when assigning labels.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from benchmark_loader import ScenarioPackage, load_seed


AFFORDANCE_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    (
        "maintain_privacy",
        (
            "private",
            "privacy",
            "confidential",
            "do not disclose",
            "not disclose",
            "do not share",
            "not share",
            "keep it to",
            "permission",
        ),
    ),
    (
        "repair_relationship",
        (
            "apologize",
            "apologise",
            "sorry",
            "repair",
            "make amends",
            "restore trust",
            "take responsibility",
        ),
    ),
    (
        "choose_collaboration_context",
        (
            "verify",
            "less rely",
            "rely less",
            "next revision",
            "revision pass",
            "assign",
            "delegate",
        ),
    ),
    (
        "follow_commitment",
        (
            "send the notes",
            "send notes",
            "follow through",
            "honor the commitment",
            "keep the promise",
        ),
    ),
    (
        "avoid_contact",
        (
            "avoid",
            "wait until",
            "stop interrupting",
            "do not interrupt",
            "not interrupt",
        ),
    ),
    (
        "share_information",
        (
            "share",
            "tell",
            "disclose",
            "explain the private issue",
        ),
    ),
    (
        "seek_information",
        (
            "ask about",
            "find out",
            "learn whether",
            "check whether",
        ),
    ),
    (
        "seek_contact",
        (
            "look for",
            "find",
            "contact",
            "reach out",
            "talk to",
            "speak with",
            "ask ",
            "meet",
        ),
    ),
)

STATUS_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    (
        "contradicted",
        (
            "missed",
            "missing",
            "has not sent",
            "not sent",
            "failed",
            "broken promise",
            "missed commitment",
        ),
    ),
    (
        "revised",
        (
            "repair",
            "partially restored",
            "less rely",
            "rely less",
            "verify",
            "delay",
            "apologize",
            "apologise",
        ),
    ),
    (
        "active",
        (
            "private",
            "permission",
            "dry run",
            "stop interrupting",
            "studio",
            "late afternoon",
            "usually works",
            "current",
        ),
    ),
    (
        "expired",
        (
            "expired",
            "no longer",
        ),
    ),
    (
        "unknown",
        (
            "unknown",
            "not sure",
            "unclear",
        ),
    ),
)


@dataclass(frozen=True)
class EntityMention:
    entity_id: str
    position: int
    matched_text: str


def load_json_object(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise TypeError(f"{path} must contain a JSON object")
    return data


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as file:
        json.dump(data, file, indent=2, ensure_ascii=False, sort_keys=True)
        file.write("\n")


def normalize_response_file(seed_dir: Path, input_path: Path) -> dict[str, Any]:
    package = load_seed(seed_dir)
    response_doc = load_json_object(input_path)
    normalized_doc = dict(response_doc)
    normalized_responses = []

    for response in response_doc.get("responses", []):
        if not isinstance(response, dict):
            continue
        normalized_responses.append(normalize_response(package, response))

    normalized_doc["responses"] = normalized_responses
    normalized_doc["normalization"] = {
        "normalizer": "response_normalizer.py",
        "normalizer_version": "0.1-rule-based",
        "condition_blind": True,
        "uses_success_conditions": False,
        "notes": (
            "Rule-based pilot normalizer. It uses response_text and the entity catalog, "
            "not condition_id or probe success conditions."
        ),
    }
    return normalized_doc


def normalize_response(package: ScenarioPackage, response: dict[str, Any]) -> dict[str, Any]:
    text = str(response.get("response_text", ""))
    normalized = dict(response)
    affordance, affordance_matches = infer_affordance(text)
    entities, entity_matches = infer_target_entities(package, text)
    statuses, status_matches = infer_statuses(text)

    normalized["chosen_affordance_type"] = affordance
    normalized["target_entities"] = entities
    normalized["current_status_used"] = statuses
    normalized["normalization_notes"] = (
        "condition-blind rule normalization; "
        f"affordance_matches={affordance_matches}; "
        f"entity_matches={entity_matches}; "
        f"status_matches={status_matches}"
    )
    return normalized


def infer_affordance(text: str) -> tuple[str, list[str]]:
    normalized_text = text.lower()
    best_affordance = ""
    best_matches: list[str] = []
    for affordance, markers in AFFORDANCE_RULES:
        matches = [marker for marker in markers if marker in normalized_text]
        if len(matches) > len(best_matches):
            best_affordance = affordance
            best_matches = matches
    return best_affordance, best_matches


def infer_statuses(text: str) -> tuple[list[str], dict[str, list[str]]]:
    normalized_text = text.lower()
    statuses: list[str] = []
    matched_by_status: dict[str, list[str]] = {}
    for status, markers in STATUS_RULES:
        matches = [marker for marker in markers if marker in normalized_text]
        if matches:
            statuses.append(status)
            matched_by_status[status] = matches
    return statuses, matched_by_status


def infer_target_entities(package: ScenarioPackage, text: str) -> tuple[list[str], list[dict[str, Any]]]:
    mentions: list[EntityMention] = []
    for entity in package.entities:
        entity_id = str(entity.get("entity_id", ""))
        terms = entity_terms(entity)
        for term in terms:
            match = find_term(text, term)
            if match is not None:
                mentions.append(
                    EntityMention(
                        entity_id=entity_id,
                        position=match.start(),
                        matched_text=match.group(0),
                    )
                )
                break

    mentions.sort(key=lambda item: (item.position, item.entity_id))
    entity_ids: list[str] = []
    for mention in mentions:
        if mention.entity_id not in entity_ids:
            entity_ids.append(mention.entity_id)

    match_details = [
        {
            "entity_id": mention.entity_id,
            "matched_text": mention.matched_text,
            "position": mention.position,
        }
        for mention in mentions
    ]
    return entity_ids, match_details


def entity_terms(entity: dict[str, Any]) -> list[str]:
    terms = [
        str(entity.get("display_name", "")),
        str(entity.get("entity_id", "")),
    ]
    aliases = entity.get("aliases")
    if isinstance(aliases, list):
        terms.extend(str(alias) for alias in aliases)
    return [term for term in terms if term]


def find_term(text: str, term: str) -> re.Match[str] | None:
    pattern = r"(?<![A-Za-z0-9_])" + re.escape(term) + r"(?![A-Za-z0-9_])"
    return re.search(pattern, text, flags=re.IGNORECASE)


def default_output_path(input_path: Path) -> Path:
    if input_path.name.endswith(".raw_draft.json"):
        return input_path.with_name(input_path.name.replace(".raw_draft.json", ".normalized.json"))
    if input_path.name.endswith(".template.json"):
        return input_path.with_name(input_path.name.replace(".template.json", ".normalized.json"))
    return input_path.with_name(f"{input_path.stem}.normalized.json")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Normalize SMGA raw response drafts.")
    parser.add_argument("seed_dir", type=Path, help="Path to a scenario seed directory.")
    parser.add_argument("responses_json", type=Path, help="Raw response draft or response JSON.")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output normalized response JSON. Defaults next to input.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_path = args.output or default_output_path(args.responses_json)
    try:
        normalized = normalize_response_file(args.seed_dir, args.responses_json)
        write_json(output_path, normalized)
    except (OSError, json.JSONDecodeError, TypeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"normalized responses: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
