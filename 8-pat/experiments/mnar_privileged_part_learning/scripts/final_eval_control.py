"""Immutable lock and one-time test-access controls for PAT-F-260728-001."""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path


FINAL_SPLITS = (
    "CUB_OFFICIAL_TEST",
    "CCT_CIS_TEST",
    "CCT_TRANS_TEST",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def atomic_json_write(path: Path, payload: dict) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    )
    os.replace(temporary, path)


def verify_lock(lock_path: Path) -> dict:
    lock = json.loads(lock_path.read_text())
    if lock.get("experiment_id") != "PAT-F-260728-001":
        raise RuntimeError("Unexpected final-evaluation lock experiment ID")
    for record in lock["artifacts"]:
        path = Path(record["path"])
        if not path.is_file():
            raise RuntimeError(f"Locked artifact is missing: {path}")
        observed = sha256_file(path)
        if observed != record["sha256"]:
            raise RuntimeError(f"Locked artifact hash changed: {path}")
    if set(lock["test_decode_counters"]) != set(FINAL_SPLITS):
        raise RuntimeError("Lock does not contain all final split counters")
    if any(lock["test_decode_counters"].values()):
        raise RuntimeError("Final split counter was nonzero at lock time")
    return lock


class FinalEvaluationLedger:
    """Atomic, one-shot state ledger used by the final dataset adapters."""

    def __init__(self, lock_path: Path, state_path: Path):
        self.lock_path = lock_path
        self.state_path = state_path
        self.lock = verify_lock(lock_path)

    def initialize(self) -> None:
        if self.state_path.exists():
            raise RuntimeError("Final evaluation state already exists")
        atomic_json_write(
            self.state_path,
            {
                "experiment_id": "PAT-F-260728-001",
                "lock_sha256": sha256_file(self.lock_path),
                "status": "LOCKED_READY",
                "decode_counts": {split: 0 for split in FINAL_SPLITS},
                "created_at": datetime.now(timezone.utc).isoformat(),
            },
        )

    def begin_once(self) -> None:
        state = json.loads(self.state_path.read_text())
        if state["lock_sha256"] != sha256_file(self.lock_path):
            raise RuntimeError("Final lock changed after ledger creation")
        if state["status"] != "LOCKED_READY":
            raise RuntimeError(
                f"Final evaluation cannot start from {state['status']}"
            )
        state["status"] = "RUNNING"
        state["started_at"] = datetime.now(timezone.utc).isoformat()
        atomic_json_write(self.state_path, state)

    def record_decode(self, split: str, count: int = 1) -> None:
        if split not in FINAL_SPLITS or count < 1:
            raise ValueError("Invalid final split decode event")
        state = json.loads(self.state_path.read_text())
        if state["status"] != "RUNNING":
            raise RuntimeError("Test image decode outside the one-time run")
        state["decode_counts"][split] += int(count)
        atomic_json_write(self.state_path, state)

    def complete(self, result_path: Path) -> None:
        state = json.loads(self.state_path.read_text())
        if state["status"] != "RUNNING":
            raise RuntimeError("Final evaluation is not running")
        if not result_path.is_file():
            raise RuntimeError("Final result file does not exist")
        state["status"] = "COMPLETED_NO_FURTHER_TUNING"
        state["completed_at"] = datetime.now(timezone.utc).isoformat()
        state["result_path"] = str(result_path.resolve())
        state["result_sha256"] = sha256_file(result_path)
        atomic_json_write(self.state_path, state)
