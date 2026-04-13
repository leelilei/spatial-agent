#!/usr/bin/env python3
"""Generate an assistant first-pass pre-screen for the Phase 1 broad candidate pool."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from spatial_agent_survey.export import export_json
from spatial_agent_survey.ingest import read_jsonl, write_csv
from spatial_agent_survey.screening import assistant_phase1_prescreen_decision, normalize_title_key


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--papers",
        type=Path,
        default=PROJECT_ROOT / "data" / "processed" / "papers_master_phase1_2026-04-13.csv",
        help="Phase 1 deduplicated candidate pool CSV.",
    )
    parser.add_argument(
        "--seed-jsonl",
        type=Path,
        default=PROJECT_ROOT / "data" / "raw" / "phase1_search_seed_2026-04-13.jsonl",
        help="Curated Phase 1 seed JSONL used as anchors.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=PROJECT_ROOT / "data" / "processed" / "screening_sheet_phase1_assistant_prescreen_2026-04-13.csv",
        help="Assistant pre-screen output CSV path.",
    )
    parser.add_argument(
        "--keep-output",
        type=Path,
        default=PROJECT_ROOT / "data" / "processed" / "screening_keep_pool_phase1_assistant_prescreen_2026-04-13.csv",
        help="Deduplicated keep-pool CSV path.",
    )
    parser.add_argument(
        "--summary-output",
        type=Path,
        default=PROJECT_ROOT / "results" / "logs" / "prisma_summary_phase1_assistant_prescreen_2026-04-13.json",
        help="Summary JSON path.",
    )
    return parser.parse_args()


def read_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def load_seed_tier_map(seed_jsonl_path: Path) -> dict[str, str]:
    seed_map: dict[str, str] = {}
    if not seed_jsonl_path.exists():
        return seed_map
    for row in read_jsonl(seed_jsonl_path):
        title = normalize_title_key(str(row.get("title") or ""))
        tier = str(row.get("corpus_tier_guess") or "").strip().lower()
        if title and tier:
            seed_map[title] = tier
    return seed_map


def build_prescreen_rows(paper_rows: list[dict], seed_tier_map: dict[str, str]) -> list[dict]:
    rows: list[dict] = []
    for row in paper_rows:
        decision = assistant_phase1_prescreen_decision(row, seed_tier_map=seed_tier_map)
        status = decision["assistant_status"]
        exclusion_reason = decision["assistant_exclusion_reason"]
        rows.append(
            {
                "paper_id": row.get("paper_id", ""),
                "title": row.get("title", ""),
                "year": row.get("year", ""),
                "venue": row.get("venue", ""),
                "source_families": row.get("source_families", ""),
                "assistant_status": status,
                "assistant_corpus_tier": decision["assistant_corpus_tier"],
                "assistant_exclusion_reason": exclusion_reason,
                "assistant_confidence": decision["assistant_confidence"],
                "assistant_priority": decision["assistant_priority"],
                "assistant_rule": decision["assistant_rule"],
                "assistant_rationale": decision["assistant_rationale"],
                "final_status": status,
                "corpus_tier": decision["assistant_corpus_tier"],
                "exclusion_reason": exclusion_reason,
                "notes": f"[assistant_prescreen] {decision['assistant_rationale']}",
            }
        )
    return rows


def dedupe_keep_pool(rows: list[dict]) -> list[dict]:
    priority_rank = {"high": 0, "medium": 1, "low": 2}
    kept: dict[str, dict] = {}
    for row in rows:
        if row["assistant_status"] == "excluded":
            continue
        title_key = normalize_title_key(row["title"])
        if title_key not in kept:
            kept[title_key] = dict(row)
            continue
        current = kept[title_key]
        current_rank = priority_rank.get(current.get("assistant_priority", "low"), 2)
        challenger_rank = priority_rank.get(row.get("assistant_priority", "low"), 2)
        if challenger_rank < current_rank:
            base = dict(row)
        else:
            base = dict(current)
        merged_families = sorted(
            {
                family.strip()
                for family in (current.get("source_families", "") + ";" + row.get("source_families", "")).split(";")
                if family.strip()
            }
        )
        base["source_families"] = "; ".join(merged_families)
        kept[title_key] = base
    return sorted(
        kept.values(),
        key=lambda row: (
            {"core": 0, "adjacent": 1, "foundational": 2}.get(row["assistant_status"], 9),
            {"high": 0, "medium": 1, "low": 2}.get(row["assistant_priority"], 2),
            row["title"].lower(),
        ),
    )


def build_summary(rows: list[dict], keep_rows: list[dict]) -> dict:
    counter = Counter(row["assistant_status"] for row in rows)
    keep_counter = Counter(row["assistant_status"] for row in keep_rows)
    return {
        "total_candidates": len(rows),
        "assistant_prescreen_counts": dict(sorted(counter.items())),
        "keep_pool_after_title_dedupe": len(keep_rows),
        "keep_pool_counts": dict(sorted(keep_counter.items())),
    }


def main() -> int:
    args = parse_args()
    paper_rows = read_rows(args.papers)
    seed_tier_map = load_seed_tier_map(args.seed_jsonl)
    prescreen_rows = build_prescreen_rows(paper_rows, seed_tier_map)
    keep_rows = dedupe_keep_pool(prescreen_rows)

    fieldnames = [
        "paper_id",
        "title",
        "year",
        "venue",
        "source_families",
        "assistant_status",
        "assistant_corpus_tier",
        "assistant_exclusion_reason",
        "assistant_confidence",
        "assistant_priority",
        "assistant_rule",
        "assistant_rationale",
        "final_status",
        "corpus_tier",
        "exclusion_reason",
        "notes",
    ]
    write_csv(args.output, prescreen_rows, fieldnames)
    write_csv(args.keep_output, keep_rows, fieldnames)
    summary = build_summary(prescreen_rows, keep_rows)
    export_json(args.summary_output, summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
