#!/usr/bin/env python3
"""Collect a broad Phase 1 candidate pool from OpenAlex and emit family JSONL files."""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import date
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from spatial_agent_survey.export import export_json
from spatial_agent_survey.ingest import openalex_result_to_raw_record


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=PROJECT_ROOT / "configs" / "queries.yaml",
        help="YAML config path containing query families and OpenAlex variants.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PROJECT_ROOT / "data" / "raw",
        help="Directory for output JSONL files.",
    )
    parser.add_argument(
        "--summary-output",
        type=Path,
        default=PROJECT_ROOT / "results" / "logs" / "phase1_openalex_pool_summary.json",
        help="JSON summary output path.",
    )
    parser.add_argument(
        "--batch-date",
        default=str(date.today()),
        help="Date stamp used in output filenames, e.g. 2026-04-13.",
    )
    parser.add_argument(
        "--sleep-seconds",
        type=float,
        default=0.2,
        help="Delay between API calls to avoid bursty traffic.",
    )
    return parser.parse_args()


def load_query_families(config_path: Path) -> dict:
    with config_path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle).get("query_families", {})


def build_openalex_url(*, search_term: str, year_from: int | None, per_page: int, page: int) -> str:
    params = {
        "search": search_term,
        "per-page": per_page,
        "page": page,
        "sort": "relevance_score:desc",
    }
    filters = ["language:en"]
    if year_from:
        filters.append(f"from_publication_date:{year_from}-01-01")
    params["filter"] = ",".join(filters)
    return "https://api.openalex.org/works?" + urllib.parse.urlencode(params)


def fetch_json(url: str) -> dict:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "spatial-agent-survey/0.1 (phase1 candidate collection)",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def family_output_path(output_dir: Path, family_key: str, batch_date: str) -> Path:
    return output_dir / f"phase1_{family_key.lower()}_openalex_{batch_date}.jsonl"


def dedupe_key(record: dict) -> str:
    doi = str(record.get("doi") or "").strip().lower()
    if doi:
        return f"doi:{doi}"
    url = str(record.get("url") or "").strip().lower()
    if url:
        return f"url:{url}"
    openalex_id = str(record.get("openalex_id") or "").strip().lower()
    if openalex_id:
        return f"openalex:{openalex_id}"
    title = str(record.get("title") or "").strip().lower()
    year = str(record.get("year") or "").strip()
    return f"title:{title}::{year}"


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> int:
    args = parse_args()
    query_families = load_query_families(args.config)

    overall_seen: set[str] = set()
    overall_unique = 0
    summary: dict[str, object] = {
        "batch_date": args.batch_date,
        "source": "openalex",
        "families": {},
        "overall": {},
    }

    for family_key, family_cfg in query_families.items():
        phase1_cfg = family_cfg.get("phase1_openalex")
        if not phase1_cfg:
            continue

        family_rows: list[dict] = []
        family_seen: set[str] = set()
        family_stats = {
            "name": family_cfg.get("name", family_key),
            "query": family_cfg.get("query", ""),
            "variants": [],
            "raw_results": 0,
            "unique_results": 0,
        }

        for variant in phase1_cfg.get("variants", []):
            variant_stat = {
                "query": variant,
                "pages": [],
            }
            for page in range(1, int(phase1_cfg.get("pages", 1)) + 1):
                url = build_openalex_url(
                    search_term=variant,
                    year_from=phase1_cfg.get("year_from"),
                    per_page=int(phase1_cfg.get("per_page", 25)),
                    page=page,
                )
                payload = fetch_json(url)
                results = payload.get("results", [])
                family_stats["raw_results"] += len(results)
                variant_stat["pages"].append(
                    {
                        "page": page,
                        "returned": len(results),
                        "meta_count": payload.get("meta", {}).get("count"),
                    }
                )
                for result in results:
                    row = openalex_result_to_raw_record(
                        result,
                        query_family=family_key,
                        search_variant=variant,
                        search_batch=f"phase1_openalex_{args.batch_date}",
                    )
                    if not row.get("title"):
                        continue
                    key = dedupe_key(row)
                    if key in family_seen:
                        continue
                    family_seen.add(key)
                    family_rows.append(row)
                    if key not in overall_seen:
                        overall_seen.add(key)
                        overall_unique += 1
                time.sleep(args.sleep_seconds)
            family_stats["variants"].append(variant_stat)

        family_stats["unique_results"] = len(family_rows)
        summary["families"][family_key] = family_stats
        write_jsonl(family_output_path(args.output_dir, family_key, args.batch_date), family_rows)
        print(f"{family_key}: wrote {len(family_rows)} unique rows")

    summary["overall"] = {
        "family_count": len(summary["families"]),
        "unique_candidate_count": overall_unique,
        "output_dir": str(args.output_dir),
    }
    export_json(args.summary_output, summary)
    print(f"Overall unique candidate count: {overall_unique}")
    print(f"Summary written to {args.summary_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
