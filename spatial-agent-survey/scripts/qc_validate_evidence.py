#!/usr/bin/env python3
"""Validate evidence tables and QC gates for the survey workflow."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from spatial_agent_survey.schemas import system_from_row
from spatial_agent_survey.screening import compute_flip_rate, compute_raw_agreement, qc_gate_status


def read_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    core_path = PROJECT_ROOT / "data" / "processed" / "core_evidence_template.csv"
    screening_path = PROJECT_ROOT / "data" / "processed" / "screening_sheet.csv"
    recheck_path = PROJECT_ROOT / "data" / "processed" / "exclusion_recheck_sample.csv"
    audit_path = PROJECT_ROOT / "data" / "processed" / "audit_log.csv"
    output_path = PROJECT_ROOT / "results" / "logs" / "qc_summary.json"

    errors = []
    for index, row in enumerate(read_rows(core_path), start=1):
        populated = any(str(value).strip() for value in row.values())
        if not populated:
            continue
        try:
            system_from_row(row)
        except Exception as exc:  # noqa: BLE001
            errors.append({"row": index, "error": str(exc)})

    screening_rows = read_rows(screening_path)
    rechecked_rows = read_rows(recheck_path)
    audit_rows = read_rows(audit_path)
    flip_rate = compute_flip_rate(screening_rows, rechecked_rows)
    raw_agreement = compute_raw_agreement(audit_rows, "original_label", "auditor_label")
    gate = qc_gate_status(flip_rate=flip_rate, raw_agreement=raw_agreement)
    reviewed_recheck_rows = sum(1 for row in rechecked_rows if str(row.get("rechecked_status") or "").strip())
    reviewed_audit_rows = sum(
        1
        for row in audit_rows
        if str(row.get("original_label") or "").strip() and str(row.get("auditor_label") or "").strip()
    )
    summary = {
        "validation_errors": errors,
        "flip_rate": flip_rate,
        "reviewed_recheck_rows": reviewed_recheck_rows,
        "raw_agreement": raw_agreement,
        "reviewed_audit_rows": reviewed_audit_rows,
        **gate,
    }
    write_json(output_path, summary)
    if errors or gate["phase_gate_blocked"]:
        print(f"QC checks failed; see {output_path}")
        return 1
    print(f"QC checks passed; summary written to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
