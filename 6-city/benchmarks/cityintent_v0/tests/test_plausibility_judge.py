from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

from judge_trace_plausibility import write_json  # noqa: E402


class PlausibilityJudgeArchiveTest(unittest.TestCase):
    def test_write_json_atomically_replaces_complete_archive(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "nested" / "judged_traces.json"

            write_json(output, [{"id": 1}])
            write_json(output, [{"id": 1}, {"id": 2}])

            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), [{"id": 1}, {"id": 2}])
            self.assertFalse(output.with_name(f"{output.name}.tmp").exists())


if __name__ == "__main__":
    unittest.main()
