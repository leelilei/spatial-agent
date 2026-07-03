"""Validate and ingest completed CityIntent human-annotation CSV submissions."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


TOOLS_DIR = Path(__file__).resolve().parent
BENCHMARK_ROOT = TOOLS_DIR.parent
REPO_ROOT = BENCHMARK_ROOT.parents[2]
DEFAULT_AUDIT_DIR = (
    REPO_ROOT
    / "6-city"
    / "annotation"
    / "cityintent_v1_rc1_blind_validation_2026-07-02"
)

if str(TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_DIR))

from build_human_audit import ANNOTATION_FIELDS, write_csv  # noqa: E402
from score_human_audit import (  # noqa: E402
    index_rows,
    read_csv,
    score_annotations,
    validate_row,
    write_findings_csv,
    write_json,
    write_summary,
)


REQUIRED_FIELDS = [
    "completion_label",
    "feasibility_label",
    "replan_label",
    "evidence_sufficient",
    "confidence",
]
ALLOWED_ANNOTATORS = {"annotator_a", "annotator_b"}


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_submission(
    submission: Path, key_path: Path
) -> tuple[str, list[dict[str, str]]]:
    rows = read_csv(submission)
    indexed = index_rows(rows, str(submission))
    key = index_rows(read_csv(key_path), str(key_path))
    errors: list[str] = []
    if set(indexed) != set(key):
        errors.append("submission audit_id set must exactly match the sealed key")
    annotator_ids = {row.get("annotator_id", "").strip() for row in indexed.values()}
    if len(annotator_ids) != 1:
        errors.append("submission must contain exactly one annotator_id")
        annotator = ""
    else:
        annotator = next(iter(annotator_ids))
        if annotator not in ALLOWED_ANNOTATORS:
            errors.append(f"unsupported annotator_id: {annotator!r}")
    for row in indexed.values():
        errors.extend(validate_row(row, str(submission)))
        missing = [field for field in REQUIRED_FIELDS if not row.get(field, "").strip()]
        if missing:
            errors.append(f"{row['audit_id']} missing required labels: {missing}")
    if errors:
        raise ValueError("; ".join(errors))
    ordered = [indexed[audit_id] for audit_id in sorted(indexed)]
    return annotator, ordered


def canonical_is_filled(path: Path) -> bool:
    return any(
        any((row.get(field, "") or "").strip() for field in REQUIRED_FIELDS)
        for row in read_csv(path)
    )


def canonical_is_complete(path: Path) -> bool:
    rows = read_csv(path)
    return bool(rows) and all(
        all((row.get(field, "") or "").strip() for field in REQUIRED_FIELDS)
        for row in rows
    )


def score_if_complete(audit_dir: Path) -> dict[str, Any] | None:
    annotations_a = audit_dir / "annotations" / "annotator_a.csv"
    annotations_b = audit_dir / "annotations" / "annotator_b.csv"
    if not canonical_is_complete(annotations_a) or not canonical_is_complete(annotations_b):
        return None
    result = score_annotations(
        annotations_a,
        annotations_b,
        audit_dir / "sealed" / "audit_key.csv",
    )
    output_dir = audit_dir / "agreement"
    output_dir.mkdir(parents=True, exist_ok=True)
    write_json(output_dir / "agreement.json", result)
    write_summary(output_dir / "agreement.md", result)
    write_findings_csv(output_dir / "material_findings.csv", result)
    return result


def ingest_submission(
    submission: Path, audit_dir: Path, replace: bool = False
) -> dict[str, Any]:
    key_path = audit_dir / "sealed" / "audit_key.csv"
    annotator, rows = validate_submission(submission, key_path)
    destination = audit_dir / "annotations" / f"{annotator}.csv"
    if canonical_is_filled(destination) and not replace:
        raise FileExistsError(
            f"canonical {annotator} submission already contains labels; use --replace intentionally"
        )
    submissions_dir = audit_dir / "submissions"
    submissions_dir.mkdir(parents=True, exist_ok=True)
    raw_copy = submissions_dir / f"{annotator}.submitted.csv"
    shutil.copyfile(submission, raw_copy)
    write_csv(destination, rows, ANNOTATION_FIELDS)
    manifest = {
        "schema_version": "cityintent_human_submission_v1",
        "annotator_id": annotator,
        "row_count": len(rows),
        "source_name": submission.name,
        "source_sha256": file_sha256(submission),
        "archived_submission": raw_copy.name,
        "archived_sha256": file_sha256(raw_copy),
        "canonical_sha256": file_sha256(destination),
        "submitted_at": datetime.now(timezone.utc).isoformat(),
        "replaced_existing": bool(replace),
    }
    manifest_path = submissions_dir / f"{annotator}.manifest.json"
    with manifest_path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--submission", type=Path, action="append", required=True)
    parser.add_argument("--audit-dir", type=Path, default=DEFAULT_AUDIT_DIR)
    parser.add_argument("--replace", action="store_true")
    args = parser.parse_args()
    seen: set[str] = set()
    for submission in args.submission:
        manifest = ingest_submission(submission, args.audit_dir, replace=args.replace)
        annotator = manifest["annotator_id"]
        if annotator in seen:
            raise ValueError(f"duplicate submission for {annotator}")
        seen.add(annotator)
        print(f"Ingested {annotator}: {manifest['row_count']} rows")
    score = score_if_complete(args.audit_dir)
    if score is None:
        print("Waiting for the other independent annotator.")
    else:
        print(
            "Both submissions complete; wrote agreement and "
            f"{len(score['material_findings'])} material findings."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
