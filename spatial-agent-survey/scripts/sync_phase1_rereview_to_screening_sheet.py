#!/usr/bin/env python3
"""Sync Phase 1 assistant prescreen results with abstract rereview decisions."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT.parent
SRC_ROOT = PROJECT_ROOT / "src"
import sys

if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from spatial_agent_survey.ingest import write_csv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--assistant-screening",
        type=Path,
        default=PROJECT_ROOT / "data" / "processed" / "screening_sheet_phase1_assistant_prescreen_2026-04-13.csv",
        help="Assistant-prescreen Phase 1 screening sheet.",
    )
    parser.add_argument(
        "--rereview",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_abstract_rereview_round1_2026-04-13.csv",
        help="Phase 1 abstract rereview CSV.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=PROJECT_ROOT / "data" / "processed" / "screening_sheet_phase1_2026-04-13.csv",
        help="Formalized Phase 1 screening sheet.",
    )
    parser.add_argument(
        "--summary-output",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_screening_formalization_summary_2026-04-14.md",
        help="Markdown summary of the synchronization result.",
    )
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def build_rereview_map(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {str(row["paper_id"]).strip(): row for row in rows if str(row.get("paper_id") or "").strip()}


def merge_notes(existing: str, rereview_note: str) -> str:
    base = existing.strip()
    suffix = f"[abstract_rereview_r1] {rereview_note.strip()}"
    if not base:
        return suffix
    return f"{base} | {suffix}"


def sync_rows(assistant_rows: list[dict[str, str]], rereview_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    rereview_map = build_rereview_map(rereview_rows)
    synced: list[dict[str, str]] = []
    for row in assistant_rows:
        paper_id = str(row.get("paper_id") or "").strip()
        synced_row = {
            "paper_id": paper_id,
            "title": row.get("title", ""),
            "year": row.get("year", ""),
            "venue": row.get("venue", ""),
            "source_families": row.get("source_families", ""),
            "final_status": row.get("final_status", ""),
            "corpus_tier": row.get("corpus_tier", ""),
            "exclusion_reason": row.get("exclusion_reason", ""),
            "notes": row.get("notes", ""),
        }
        if paper_id in rereview_map:
            review = rereview_map[paper_id]
            final_status = str(review.get("r1_recommended_tier") or "").strip()
            synced_row["final_status"] = final_status
            synced_row["corpus_tier"] = final_status
            synced_row["exclusion_reason"] = str(review.get("r1_exclusion_reason") or "").strip()
            synced_row["notes"] = merge_notes(synced_row["notes"], str(review.get("r1_note") or ""))
        synced.append(synced_row)
    return synced


def build_summary(rows: list[dict[str, str]], rereview_rows: list[dict[str, str]]) -> str:
    status_counter = Counter(row["final_status"] for row in rows if row["final_status"])
    exclusion_counter = Counter(row["exclusion_reason"] for row in rows if row["final_status"] == "excluded" and row["exclusion_reason"])
    covered_ids = {str(row.get("paper_id") or "").strip() for row in rereview_rows}
    covered_count = sum(1 for row in rows if str(row.get("paper_id") or "").strip() in covered_ids)
    lines = [
        "# Phase 1 Screening Formalization Summary",
        "",
        "日期：2026-04-14",
        "",
        "## 写入范围",
        "",
        f"- assistant prescreen 底表行数：`{len(rows)}`",
        f"- 被 `R1` 覆盖的行数：`{covered_count}`",
        "",
        "## 最终状态统计",
        "",
        f"- `core`: `{status_counter.get('core', 0)}`",
        f"- `adjacent`: `{status_counter.get('adjacent', 0)}`",
        f"- `foundational`: `{status_counter.get('foundational', 0)}`",
        f"- `excluded`: `{status_counter.get('excluded', 0)}`",
        "",
        "## 排除原因统计",
        "",
        f"- `E1`: `{exclusion_counter.get('E1', 0)}`",
        f"- `E2`: `{exclusion_counter.get('E2', 0)}`",
        f"- `E3`: `{exclusion_counter.get('E3', 0)}`",
        f"- `E4`: `{exclusion_counter.get('E4', 0)}`",
        f"- `E5`: `{exclusion_counter.get('E5', 0)}`",
        "",
        "## 说明",
        "",
        "- 417 行 Phase 1 candidate pool 已全部写入正式 `screening_sheet_phase1_2026-04-13.csv`。",
        "- 其中 117 行来自 `abstract rereview round 1` 的人工/规则覆盖；其余行保留 assistant prescreen 结果。",
        "- `notes` 字段保留 assistant 说明，并追加 `[abstract_rereview_r1]` 裁定说明。",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    assistant_rows = read_rows(args.assistant_screening)
    rereview_rows = read_rows(args.rereview)
    synced_rows = sync_rows(assistant_rows, rereview_rows)
    write_csv(
        args.output,
        synced_rows,
        ["paper_id", "title", "year", "venue", "source_families", "final_status", "corpus_tier", "exclusion_reason", "notes"],
        encoding="utf-8-sig",
    )
    args.summary_output.parent.mkdir(parents=True, exist_ok=True)
    args.summary_output.write_text(build_summary(synced_rows, rereview_rows), encoding="utf-8")
    print(f"Wrote {len(synced_rows)} rows to {args.output}")
    print(f"Wrote summary to {args.summary_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
