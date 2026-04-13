#!/usr/bin/env python3
"""Generate Chinese abstract summaries for the Phase 1 manual review sheet."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT.parent

PLACEHOLDER_FOR_MISSING_ABSTRACT = "当前未获取到英文摘要；现阶段仅能依据题名与分层做初步判断，需补全文或外部元数据后再进一步复核。"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_manual_tier_review_sheet_translation_input_2026-04-13.json",
        help="JSON input exported by export_phase1_manual_review_sheet.py.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_manual_tier_review_sheet_zh_summary_2026-04-13.json",
        help="Merged JSON output path.",
    )
    parser.add_argument(
        "--batch-dir",
        type=Path,
        default=PROJECT_ROOT / "data" / "processed" / "tmp_translation" / "phase1_zh_batches",
        help="Directory for temporary batch files.",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=12,
        help="Number of items per Codex batch.",
    )
    return parser.parse_args()


def read_input(path: Path) -> list[dict[str, str]]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def load_existing_output(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list):
        return {}
    return {
        str(item.get("paper_id") or "").strip(): str(item.get("abstract_zh_summary") or "").strip()
        for item in payload
        if str(item.get("paper_id") or "").strip()
    }


def build_placeholder_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    placeholder_rows: list[dict[str, str]] = []
    for row in rows:
        placeholder_rows.append(
            {
                "paper_id": str(row.get("paper_id") or "").strip(),
                "abstract_zh_summary": PLACEHOLDER_FOR_MISSING_ABSTRACT,
            }
        )
    return placeholder_rows


def chunk_rows(rows: list[dict[str, str]], batch_size: int) -> list[list[dict[str, str]]]:
    return [rows[i : i + batch_size] for i in range(0, len(rows), batch_size)]


def run_codex_batch(batch_input_path: Path, batch_output_path: Path) -> list[dict[str, str]]:
    rel_input = batch_input_path.resolve().relative_to(REPO_ROOT.resolve())
    prompt = (
        f"Read {rel_input.as_posix()} and return ONLY a JSON array. "
        "For each item, keep paper_id and add abstract_zh_summary in Simplified Chinese. "
        "Write a faithful screening-oriented Chinese summary of the abstract, typically 70-140 Chinese characters. "
        "Do not use markdown. Do not add extra keys. Do not omit any item."
    )
    command = [
        "codex",
        "exec",
        "--skip-git-repo-check",
        "--sandbox",
        "read-only",
        "-C",
        str(REPO_ROOT),
        "-o",
        str(batch_output_path),
        prompt,
    ]
    subprocess.run(command, check=True, cwd=REPO_ROOT)
    return json.loads(batch_output_path.read_text(encoding="utf-8"))


def persist_merged_map(output_path: Path, merged_map: dict[str, str]) -> None:
    payload = [
        {"paper_id": paper_id, "abstract_zh_summary": merged_map[paper_id]}
        for paper_id in sorted(merged_map)
    ]
    write_json(output_path, payload)


def main() -> int:
    args = parse_args()
    rows = read_input(args.input)
    batch_dir = args.batch_dir
    batch_dir.mkdir(parents=True, exist_ok=True)

    merged_map = load_existing_output(args.output)

    rows_with_abstract = [row for row in rows if str(row.get("abstract") or "").strip()]
    rows_without_abstract = [row for row in rows if not str(row.get("abstract") or "").strip()]
    for row in build_placeholder_rows(rows_without_abstract):
        merged_map.setdefault(row["paper_id"], row["abstract_zh_summary"])
    persist_merged_map(args.output, merged_map)

    batches = chunk_rows(rows_with_abstract, args.batch_size)
    total_batches = len(batches)

    for index, batch_rows in enumerate(batches, start=1):
        batch_input_path = batch_dir / f"batch_{index:02d}_input.json"
        batch_output_path = batch_dir / f"batch_{index:02d}_output.json"
        write_json(batch_input_path, batch_rows)
        batch_ids = [str(row.get("paper_id") or "").strip() for row in batch_rows]
        if all(paper_id and paper_id in merged_map for paper_id in batch_ids):
            print(f"[{index}/{total_batches}] already merged, skipping")
            continue
        if batch_output_path.exists():
            print(f"[{index}/{total_batches}] reusing existing batch output")
            batch_output = json.loads(batch_output_path.read_text(encoding="utf-8"))
        else:
            print(f"[{index}/{total_batches}] translating {len(batch_rows)} papers")
            batch_output = run_codex_batch(batch_input_path, batch_output_path)
        for item in batch_output:
            paper_id = str(item.get("paper_id") or "").strip()
            summary = str(item.get("abstract_zh_summary") or "").strip()
            if paper_id and summary:
                merged_map[paper_id] = summary
        persist_merged_map(args.output, merged_map)

    persist_merged_map(args.output, merged_map)
    print(f"Wrote {len(merged_map)} Chinese summaries to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
