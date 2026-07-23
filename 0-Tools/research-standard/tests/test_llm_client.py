from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


STANDARD_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(STANDARD_DIR))

from llm_client import (  # noqa: E402
    LLMConfig,
    OpenAICompatibleChatClient,
    post_json_with_curl,
)


class CurlTransportSafetyTest(unittest.TestCase):
    def test_chat_completions_honors_curl_transport(self) -> None:
        config = LLMConfig(
            model="test-model",
            wire_api="chat_completions",
            base_url="https://example.invalid",
            transport="curl",
        )
        client = OpenAICompatibleChatClient(config=config, api_key="test-key")
        response = {
            "choices": [{"message": {"content": '{"action":"finish"}'}}],
            "usage": {"total_tokens": 7},
        }

        with (
            patch("llm_client.post_json_with_curl", return_value=response) as curl_post,
            patch("llm_client.post_json") as urllib_post,
        ):
            content = client.complete({"system_prompt": "s", "user_prompt": "u"})

        self.assertEqual(content, '{"action":"finish"}')
        curl_post.assert_called_once()
        urllib_post.assert_not_called()

    def test_timeout_error_does_not_expose_authorization_command(self) -> None:
        secret = "sk-test-secret-must-not-appear"
        expired = subprocess.TimeoutExpired(["curl"], timeout=1)
        with patch("llm_client.subprocess.run", side_effect=expired) as run:
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
        command = run.call_args.args[0]
        self.assertNotIn(secret, " ".join(command))


if __name__ == "__main__":
    unittest.main()
