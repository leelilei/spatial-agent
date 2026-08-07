#!/usr/bin/env python3
"""Merge resume/recovery trace shards with deterministic first-source priority."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trace_key(row: dict[str, Any]) -> tuple[str, str, str]:
    model = str((row.get("model_info") or {}).get("model", "unknown"))
    return model, row["agent_type"], row["scenario_id"]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", action="append", type=Path, required=True)
    parser.add_argument("--expected-traces", type=int, required=True)
    parser.add_argument("--expected-scenarios", type=int, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--scenario-ids", help="Optional comma-separated scenario allowlist")
    args = parser.parse_args()
    scenario_allowlist = set(args.scenario_ids.split(",")) if args.scenario_ids else None

    selected: dict[tuple[str, str, str], dict[str, Any]] = {}
    sources = []
    ignored_duplicates = []
    for priority, directory in enumerate(args.run_dir):
        trace_path = directory.resolve() / "traces.json"
        rows = json.loads(trace_path.read_text(encoding="utf-8"))
        sources.append({
            "priority": priority,
            "run_dir": str(directory.resolve()),
            "trace_count": len(rows),
            "traces_sha256": sha256(trace_path),
        })
        for row in rows:
            if scenario_allowlist is not None and row["scenario_id"] not in scenario_allowlist:
                continue
            key = trace_key(row)
            if key in selected:
                ignored_duplicates.append({
                    "key": list(key),
                    "ignored_source": str(directory.resolve()),
                    "rule": "first_source_priority",
                })
                continue
            selected[key] = row

    rows = sorted(selected.values(), key=trace_key)
    scenario_ids = {row["scenario_id"] for row in rows}
    if len(rows) != args.expected_traces or len(scenario_ids) != args.expected_scenarios:
        raise SystemExit(
            f"merged coverage mismatch: traces={len(rows)}/{args.expected_traces}, "
            f"scenarios={len(scenario_ids)}/{args.expected_scenarios}"
        )
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    trace_path = output / "traces.json"
    trace_path.write_text(
        json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    manifest = {
        "schema_version": "cityintent_trace_archive_merge_v1",
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "status": "complete",
        "trace_count": len(rows),
        "scenario_count": len(scenario_ids),
        "sources": sources,
        "ignored_duplicates": ignored_duplicates,
        "scenario_allowlist": sorted(scenario_allowlist) if scenario_allowlist is not None else None,
        "traces_sha256": sha256(trace_path),
    }
    (output / "merge_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "traces": len(rows),
        "scenarios": len(scenario_ids),
        "ignored_duplicates": len(ignored_duplicates),
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
