from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from final_eval_control import (  # noqa: E402
    FINAL_SPLITS,
    FinalEvaluationLedger,
    sha256_file,
    verify_lock,
)


class FinalEvaluationControlTests(unittest.TestCase):
    def make_lock(self, root: Path):
        artifact = root / "artifact.json"
        artifact.write_text('{"frozen": true}\n')
        lock = root / "FINAL_EVAL_LOCK.json"
        lock.write_text(
            json.dumps(
                {
                    "experiment_id": "PAT-F-260728-001",
                    "artifacts": [
                        {
                            "path": str(artifact),
                            "sha256": sha256_file(artifact),
                        }
                    ],
                    "test_decode_counters": {
                        split: 0 for split in FINAL_SPLITS
                    },
                }
            )
        )
        return artifact, lock

    def test_hash_change_invalidates_lock(self):
        with tempfile.TemporaryDirectory() as temporary:
            artifact, lock = self.make_lock(Path(temporary))
            verify_lock(lock)
            artifact.write_text('{"frozen": false}\n')
            with self.assertRaises(RuntimeError):
                verify_lock(lock)

    def test_ledger_allows_exactly_one_start(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            _, lock = self.make_lock(root)
            state = root / "FINAL_EVAL_STATE.json"
            ledger = FinalEvaluationLedger(lock, state)
            ledger.initialize()
            ledger.begin_once()
            ledger.record_decode("CUB_OFFICIAL_TEST", 2)
            with self.assertRaises(RuntimeError):
                ledger.begin_once()
            result = root / "results.json"
            result.write_text('{"reported": true}\n')
            ledger.complete(result)
            final_state = json.loads(state.read_text())
            self.assertEqual(
                final_state["status"], "COMPLETED_NO_FURTHER_TUNING"
            )
            self.assertEqual(
                final_state["decode_counts"]["CUB_OFFICIAL_TEST"], 2
            )
            with self.assertRaises(RuntimeError):
                ledger.record_decode("CUB_OFFICIAL_TEST")


if __name__ == "__main__":
    unittest.main()
