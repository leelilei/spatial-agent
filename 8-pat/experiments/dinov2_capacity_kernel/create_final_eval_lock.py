#!/usr/bin/env python3
"""Seal the official-test protocol, manifests, and evaluation code hashes."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--protocol", type=Path, required=True)
    parser.add_argument("--selection-summary", type=Path, required=True)
    parser.add_argument("--code", type=Path, nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    selection = json.loads(args.selection_summary.read_text())
    lock = {
        "status": "LOCKED_BEFORE_OFFICIAL_TEST_IMAGE_DECODING",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "experiment_id": selection["experiment_id"],
        "protocol_path": str(args.protocol),
        "protocol_sha256": sha256(args.protocol),
        "selection_summary_sha256": sha256(args.selection_summary),
        "manifest_sha256": {
            "cub": selection["cub"]["manifest_sha256"],
            "stanford_dogs": selection["stanford_dogs"]["manifest_sha256"],
        },
        "code_sha256": {str(path): sha256(path) for path in args.code},
        "official_test_images_decoded_or_encoded_at_lock": 0,
        "retuning_after_lock": "forbidden",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n")
    print(json.dumps(lock, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
