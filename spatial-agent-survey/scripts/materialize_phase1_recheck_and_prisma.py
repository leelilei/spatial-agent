#!/usr/bin/env python3
"""Generate exclusion recheck sample and PRISMA summary from a finalized Phase 1 screening sheet."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
import sys

if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from spatial_agent_survey.ingest import write_csv
from spatial_agent_survey.screening import sample_exclusion_recheck, summarize_prisma


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--screening",
        type=Path,
        default=PROJECT_ROOT / "data" / "processed" / "screening_sheet_phase1_2026-04-13.csv",
        help="Formalized Phase 1 screening sheet.",
    )
    parser.add_argument(
        "--recheck-output",
        type=Path,
        default=PROJECT_ROOT / "data" / "processed" / "exclusion_recheck_sample_phase1_2026-04-13.csv",
        help="Exclusion recheck sample CSV output.",
    )
    parser.add_argument(
        "--prisma-output",
        type=Path,
        default=PROJECT_ROOT / "results" / "logs" / "prisma_summary_phase1_2026-04-13.json",
        help="PRISMA summary JSON output.",
    )
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    screening_rows = read_rows(args.screening)
    recheck_rows = sample_exclusion_recheck(screening_rows)
    prisma = summarize_prisma(screening_rows)
    write_csv(
        args.recheck_output,
        recheck_rows,
        [
            "paper_id",
            "title",
            "year",
            "venue",
            "source_families",
            "final_status",
            "corpus_tier",
            "exclusion_reason",
            "notes",
            "recheck_required",
            "rechecked_status",
            "rechecked_exclusion_reason",
            "recheck_notes",
        ],
        encoding="utf-8-sig",
    )
    write_json(args.prisma_output, prisma)
    print(f"Wrote {len(recheck_rows)} recheck rows to {args.recheck_output}")
    print(f"Wrote PRISMA summary to {args.prisma_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
