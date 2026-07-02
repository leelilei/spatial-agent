"""Run a model-only dry-run of the blinded human-audit rubric.

These labels are for rubric debugging and must never be reported as human
validation.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[2]
STANDARD_LLM_DIR = REPO_ROOT / "0-Tools" / "research-standard"

FIELDS = [
    "audit_id",
    "annotator_id",
    "completion_label",
    "feasibility_label",
    "replan_label",
    "evidence_sufficient",
    "first_invalid_step",
    "confidence",
    "notes",
]
ALLOWED = {
    "completion_label": {"complete", "partial", "not_complete", "uncertain"},
    "feasibility_label": {"feasible", "infeasible", "uncertain"},
    "replan_label": {"successful", "failed", "not_applicable", "uncertain"},
    "evidence_sufficient": {"yes", "no", "uncertain"},
}
PROFILES = {
    "literal": (
        "Apply a strict evidence standard. Never infer an unrecorded entry, "
        "purchase, service, interaction, meeting, or arrival."
    ),
    "behavioral": (
        "Judge ordinary urban behavior fairly, but still require observable "
        "evidence for task completion and identify invalid transitions."
    ),
}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write("\n")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def load_existing(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def normalize_label(
    audit_id: str,
    annotator_id: str,
    value: Any,
) -> dict[str, Any]:
    raw = value if isinstance(value, dict) else {}
    output: dict[str, Any] = {
        "audit_id": audit_id,
        "annotator_id": annotator_id,
    }
    for field, allowed in ALLOWED.items():
        label = str(raw.get(field, "uncertain")).strip().lower()
        output[field] = label if label in allowed else "uncertain"
    invalid_step = raw.get("first_invalid_step", "")
    try:
        invalid_step = int(invalid_step) if str(invalid_step).strip() else ""
    except (TypeError, ValueError):
        invalid_step = ""
    output["first_invalid_step"] = invalid_step if invalid_step == "" or invalid_step > 0 else ""
    try:
        confidence = int(raw.get("confidence", 3))
    except (TypeError, ValueError):
        confidence = 3
    output["confidence"] = min(5, max(1, confidence))
    output["notes"] = str(raw.get("notes", ""))[:500]
    return output


def build_prompt(item: dict[str, Any], rubric: str, profile: str) -> tuple[str, str]:
    system = (
        "You are debugging a blinded CityIntent human-annotation rubric. "
        "You are a model dry-run, not a human annotator. Return one JSON object "
        "with no markdown. "
        + PROFILES[profile]
    )
    payload = {
        "rubric": rubric,
        "response_schema": {
            "completion_label": sorted(ALLOWED["completion_label"]),
            "feasibility_label": sorted(ALLOWED["feasibility_label"]),
            "replan_label": sorted(ALLOWED["replan_label"]),
            "evidence_sufficient": sorted(ALLOWED["evidence_sufficient"]),
            "first_invalid_step": "positive integer or empty string",
            "confidence": "integer 1-5",
            "notes": "one concise reason grounded only in the blinded packet",
        },
        "audit_item": item,
    }
    return system, json.dumps(payload, ensure_ascii=False, indent=2)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--packet", type=Path, required=True)
    parser.add_argument("--rubric", type=Path, required=True)
    parser.add_argument("--llm-config", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--annotator-id", required=True)
    parser.add_argument("--profile", choices=sorted(PROFILES), required=True)
    parser.add_argument("--no-resume", action="store_true")
    args = parser.parse_args()

    if str(STANDARD_LLM_DIR) not in sys.path:
        sys.path.insert(0, str(STANDARD_LLM_DIR))
    from llm_client import LLM, parse_response_json  # type: ignore

    items = load_jsonl(args.packet)
    rubric = args.rubric.read_text(encoding="utf-8")
    output_csv = args.output_dir / f"{args.annotator_id}.csv"
    rows = [] if args.no_resume else load_existing(output_csv)
    completed = {row["audit_id"] for row in rows}
    details_path = args.output_dir / f"{args.annotator_id}_details.json"
    details = (
        json.loads(details_path.read_text(encoding="utf-8"))
        if details_path.exists() and not args.no_resume
        else []
    )
    llm = LLM(args.llm_config)
    for index, item in enumerate(items, start=1):
        audit_id = item["audit_id"]
        if audit_id in completed:
            continue
        system, user = build_prompt(item, rubric, args.profile)
        raw_response = llm.complete(system, user)
        parsed = parse_response_json(raw_response)
        row = normalize_label(audit_id, args.annotator_id, parsed)
        rows.append(row)
        completed.add(audit_id)
        details.append(
            {
                "audit_id": audit_id,
                "profile": args.profile,
                "label": row,
                "raw_response": raw_response,
            }
        )
        write_csv(output_csv, rows)
        write_json(details_path, details)
        print(f"[{index}/{len(items)}] {args.annotator_id} labeled {audit_id}")

    write_json(
        args.output_dir / f"{args.annotator_id}_manifest.json",
        {
            "status": "model_dry_run_not_human_validation",
            "annotator_id": args.annotator_id,
            "profile": args.profile,
            "item_count": len(rows),
            "llm_config": str(args.llm_config),
            "telemetry": llm.telemetry_summary(),
            "calls": llm.telemetry,
        },
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
