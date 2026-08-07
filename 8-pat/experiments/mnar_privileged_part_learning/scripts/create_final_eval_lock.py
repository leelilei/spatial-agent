#!/usr/bin/env python3
"""Create FINAL_EVAL_LOCK.json only after all dual-data gates pass."""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from final_eval_control import FINAL_SPLITS, sha256_file


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cub-screen-summary", type=Path, required=True)
    parser.add_argument("--cub-confirmation-summary", type=Path, required=True)
    parser.add_argument("--cct-oracle-summary", type=Path, required=True)
    parser.add_argument("--cct-selector-summary", type=Path, required=True)
    parser.add_argument("--final-protocol", type=Path, required=True)
    parser.add_argument(
        "--artifact", type=Path, action="append", required=True
    )
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def require_zero(summary, keys):
    for key in keys:
        if int(summary.get(key, -1)) != 0:
            raise RuntimeError(f"Required zero counter failed: {key}")


def main():
    args = parse_args()
    if args.output.exists():
        raise RuntimeError("FINAL_EVAL_LOCK.json already exists")
    cub_screen = json.loads(args.cub_screen_summary.read_text())
    cub_confirmation = json.loads(args.cub_confirmation_summary.read_text())
    cct_oracle = json.loads(args.cct_oracle_summary.read_text())
    cct_selector = json.loads(args.cct_selector_summary.read_text())
    protocol = json.loads(args.final_protocol.read_text())
    if not cub_screen.get("overall_gate_pass"):
        raise RuntimeError("CUB selector screen gate did not pass")
    if not cub_confirmation.get("overall_gate_pass"):
        raise RuntimeError("CUB multi-seed confirmation gate did not pass")
    if not cct_oracle.get("oracle_gate_pass"):
        raise RuntimeError("CCT Full Oracle gate did not pass")
    if not cct_selector.get("selector_gate_pass"):
        raise RuntimeError("CCT selector gate did not pass")
    require_zero(
        cub_screen,
        ["official_test_images_decoded_or_encoded"],
    )
    require_zero(
        cub_confirmation,
        ["official_test_images_decoded_or_encoded"],
    )
    require_zero(
        cct_oracle,
        [
            "cis_test_images_decoded_or_encoded",
            "trans_test_images_decoded_or_encoded",
        ],
    )
    require_zero(
        cct_selector,
        [
            "cis_test_images_decoded_or_encoded",
            "trans_test_images_decoded_or_encoded",
        ],
    )
    artifacts = []
    unique_paths = {
        path.resolve()
        for path in (
            [
                args.cub_screen_summary,
                args.cub_confirmation_summary,
                args.cct_oracle_summary,
                args.cct_selector_summary,
                args.final_protocol,
            ]
            + args.artifact
        )
    }
    for path in sorted(unique_paths):
        if not path.is_file():
            raise RuntimeError(f"Required lock artifact is missing: {path}")
        artifacts.append(
            {"path": str(path), "sha256": sha256_file(path)}
        )
    lock = {
        "experiment_id": protocol["experiment_id"],
        "created_at": datetime.now(timezone.utc).isoformat(),
        "winner": cub_screen["winner"],
        "winner_branch": cub_screen["winner_branch"],
        "arms": protocol["arms"],
        "model_seeds": protocol["final_model_seeds"],
        "final_splits": protocol["final_splits"],
        "post_test_policy": protocol["post_test_policy"],
        "test_decode_counters": {
            split: 0 for split in FINAL_SPLITS
        },
        "artifacts": artifacts,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(lock, indent=2, sort_keys=True) + "\n"
    )
    os.chmod(args.output, 0o444)
    print(
        json.dumps(
            {
                "lock": str(args.output.resolve()),
                "lock_sha256": sha256_file(args.output),
                "winner": lock["winner"],
                "artifacts": len(artifacts),
                "status": "LOCKED_READY_FOR_ONE_TIME_FINAL_EVALUATION",
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
