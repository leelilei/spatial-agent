"""Validate and score two blinded CityIntent human-annotation files."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any


COMPLETION = {"complete", "partial", "not_complete", "uncertain"}
FEASIBILITY = {"feasible", "infeasible", "uncertain"}
REPLAN = {"successful", "failed", "not_applicable", "uncertain"}
EVIDENCE = {"yes", "no", "uncertain"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write("\n")


def index_rows(rows: list[dict[str, str]], source: str) -> dict[str, dict[str, str]]:
    indexed: dict[str, dict[str, str]] = {}
    for row in rows:
        audit_id = row.get("audit_id", "").strip()
        if not audit_id:
            raise ValueError(f"missing audit_id in {source}")
        if audit_id in indexed:
            raise ValueError(f"duplicate audit_id {audit_id} in {source}")
        indexed[audit_id] = {key: (value or "").strip() for key, value in row.items()}
    return indexed


def validate_row(row: dict[str, str], source: str) -> list[str]:
    errors = []
    fields = [
        ("completion_label", COMPLETION),
        ("feasibility_label", FEASIBILITY),
        ("replan_label", REPLAN),
        ("evidence_sufficient", EVIDENCE),
    ]
    for field, allowed in fields:
        value = row.get(field, "")
        if value and value not in allowed:
            errors.append(f"{source}:{row['audit_id']} invalid {field}={value!r}")
    confidence = row.get("confidence", "")
    if confidence:
        try:
            number = int(confidence)
        except ValueError:
            errors.append(f"{source}:{row['audit_id']} confidence must be 1-5")
        else:
            if number not in range(1, 6):
                errors.append(f"{source}:{row['audit_id']} confidence must be 1-5")
    invalid_step = row.get("first_invalid_step", "")
    if invalid_step:
        try:
            if int(invalid_step) < 1:
                raise ValueError
        except ValueError:
            errors.append(
                f"{source}:{row['audit_id']} first_invalid_step must be a positive integer"
            )
    return errors


def cohen_kappa(labels_a: list[str], labels_b: list[str]) -> float | None:
    if len(labels_a) != len(labels_b):
        raise ValueError("label lists must have equal length")
    if not labels_a:
        return None
    categories = sorted(set(labels_a) | set(labels_b))
    observed = sum(a == b for a, b in zip(labels_a, labels_b)) / len(labels_a)
    counts_a = Counter(labels_a)
    counts_b = Counter(labels_b)
    expected = sum(
        counts_a[category] / len(labels_a) * counts_b[category] / len(labels_b)
        for category in categories
    )
    if expected == 1.0:
        return 1.0 if observed == 1.0 else 0.0
    return round((observed - expected) / (1.0 - expected), 3)


def agreement(
    rows_a: dict[str, dict[str, str]],
    rows_b: dict[str, dict[str, str]],
    field: str,
) -> dict[str, Any]:
    pairs = [
        (rows_a[audit_id].get(field, ""), rows_b[audit_id].get(field, ""))
        for audit_id in sorted(set(rows_a) & set(rows_b))
        if rows_a[audit_id].get(field, "") and rows_b[audit_id].get(field, "")
    ]
    labels_a = [pair[0] for pair in pairs]
    labels_b = [pair[1] for pair in pairs]
    return {
        "n": len(pairs),
        "exact_agreement": (
            round(sum(a == b for a, b in pairs) / len(pairs), 3) if pairs else None
        ),
        "cohen_kappa": cohen_kappa(labels_a, labels_b),
    }


def deterministic_completion(value: float) -> str:
    if value >= 0.999:
        return "complete"
    if value <= 0.001:
        return "not_complete"
    return "partial"


def calibration(
    rows: dict[str, dict[str, str]], key: dict[str, dict[str, str]]
) -> dict[str, Any]:
    comparisons: dict[str, list[tuple[str, str]]] = {
        "completion_label": [],
        "feasibility_label": [],
        "replan_label": [],
    }
    for audit_id in sorted(set(rows) & set(key)):
        human = rows[audit_id]
        truth = key[audit_id]
        completion = human.get("completion_label", "")
        if completion and completion != "uncertain":
            completion_score = truth.get("task_completion", "")
            if completion_score == "":
                completion_score = truth["goal_completion"]
            comparisons["completion_label"].append(
                (completion, deterministic_completion(float(completion_score)))
            )
        feasibility = human.get("feasibility_label", "")
        if feasibility and feasibility != "uncertain":
            deterministic = (
                "feasible" if float(truth["trace_feasibility"]) >= 0.999 else "infeasible"
            )
            comparisons["feasibility_label"].append((feasibility, deterministic))
        replan = human.get("replan_label", "")
        deterministic_raw = truth.get("replanning_success", "")
        if replan and replan not in {"uncertain", "not_applicable"} and deterministic_raw:
            deterministic = (
                "successful" if float(deterministic_raw) >= 0.999 else "failed"
            )
            comparisons["replan_label"].append((replan, deterministic))
    output = {}
    for field, pairs in comparisons.items():
        output[field] = {
            "n": len(pairs),
            "exact_agreement": (
                round(sum(human == truth for human, truth in pairs) / len(pairs), 3)
                if pairs
                else None
            ),
            "confusion": dict(
                sorted(Counter(f"human={human}|verifier={truth}" for human, truth in pairs).items())
            ),
        }
    return output


def score_annotations(
    annotations_a: Path,
    annotations_b: Path,
    key_path: Path,
    allow_incomplete: bool = False,
) -> dict[str, Any]:
    rows_a = index_rows(read_csv(annotations_a), str(annotations_a))
    rows_b = index_rows(read_csv(annotations_b), str(annotations_b))
    key = index_rows(read_csv(key_path), str(key_path))
    errors = []
    for source, rows in (("annotator_a", rows_a), ("annotator_b", rows_b)):
        for row in rows.values():
            errors.extend(validate_row(row, source))
    if set(rows_a) != set(key) or set(rows_b) != set(key):
        errors.append("annotation audit_id sets must exactly match the sealed key")
    required = [
        "completion_label",
        "feasibility_label",
        "replan_label",
        "evidence_sufficient",
        "confidence",
    ]
    pending = {
        "annotator_a": sum(
            any(not row.get(field, "") for field in required) for row in rows_a.values()
        ),
        "annotator_b": sum(
            any(not row.get(field, "") for field in required) for row in rows_b.values()
        ),
    }
    if not allow_incomplete and any(pending.values()):
        errors.append(f"incomplete annotation rows: {pending}")
    if errors:
        raise ValueError("; ".join(errors))
    fields = [
        "completion_label",
        "feasibility_label",
        "replan_label",
        "evidence_sufficient",
        "first_invalid_step",
    ]
    return {
        "audit_item_count": len(key),
        "pending_rows": pending,
        "inter_annotator_agreement": {
            field: agreement(rows_a, rows_b, field) for field in fields
        },
        "verifier_calibration": {
            "annotator_a": calibration(rows_a, key),
            "annotator_b": calibration(rows_b, key),
        },
    }


def write_summary(path: Path, result: dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("# CityIntent Human Audit Agreement\n\n")
        f.write(f"Audit items: {result['audit_item_count']}\n\n")
        f.write(f"Pending rows: `{json.dumps(result['pending_rows'], sort_keys=True)}`\n\n")
        f.write("## Inter-Annotator Agreement\n\n")
        f.write("| Field | n | Exact agreement | Cohen kappa |\n")
        f.write("|---|---:|---:|---:|\n")
        for field, values in result["inter_annotator_agreement"].items():
            f.write(
                f"| `{field}` | {values['n']} | {values['exact_agreement']} | "
                f"{values['cohen_kappa']} |\n"
            )
        f.write("\n## Verifier Calibration\n\n")
        for annotator, dimensions in result["verifier_calibration"].items():
            f.write(f"### {annotator}\n\n")
            f.write("| Field | n | Exact agreement |\n")
            f.write("|---|---:|---:|\n")
            for field, values in dimensions.items():
                f.write(
                    f"| `{field}` | {values['n']} | {values['exact_agreement']} |\n"
                )
            f.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--annotations-a", type=Path, required=True)
    parser.add_argument("--annotations-b", type=Path, required=True)
    parser.add_argument("--key", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--allow-incomplete", action="store_true")
    args = parser.parse_args()
    result = score_annotations(
        args.annotations_a,
        args.annotations_b,
        args.key,
        allow_incomplete=args.allow_incomplete,
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_json(args.output_dir / "agreement.json", result)
    write_summary(args.output_dir / "agreement.md", result)
    print(f"Wrote human-audit agreement to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
