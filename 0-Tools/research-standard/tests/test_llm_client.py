from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


STANDARD_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(STANDARD_DIR))

from llm_client import post_json_with_curl  # noqa: E402


class CurlTransportSafetyTest(unittest.TestCase):
    def test_timeout_error_does_not_expose_authorization_command(self) -> None:
        secret = "sk-test-secret-must-not-appear"
        expired = subprocess.TimeoutExpired(
            ["curl", "-H", f"Authorization: Bearer {secret}"],
            timeout=1,
        )
        with patch("llm_client.subprocess.run", side_effect=expired):
            with self.assertRaisesRegex(
                RuntimeError, "provider curl request timed out after 1 seconds"
            ) as raised:
                post_json_with_curl(
                    "https://example.invalid/v1/responses",
                    {"input": "hello"},
                    secret,
                    1,
                )

        self.assertNotIn(secret, str(raised.exception))
        self.assertIsNone(raised.exception.__cause__)


if __name__ == "__main__":
    unittest.main()
