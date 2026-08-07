#!/usr/bin/env python3
"""Thin LLM client for the society simulation, reusing the diagnostic_v0 runner."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path
from typing import Any

# Reuse the proven provider transport + configs from the parent project (3-SMGA).
_DIAG = Path(__file__).resolve().parents[2] / "3-SMGA" / "benchmarks" / "diagnostic_v0"
if str(_DIAG) not in sys.path:
    sys.path.insert(0, str(_DIAG))

import model_calling_runner as mcr  # noqa: E402

DEFAULT_CONFIG = _DIAG / "configs" / "fhl_responses_gpt54_config.example.json"


class _SecureCurlChatClient:
    """Chat Completions transport that keeps credentials out of process arguments."""

    def __init__(self, base_client: Any) -> None:
        self.model = base_client.model
        self.temperature = base_client.temperature
        self.timeout = base_client.timeout
        self.api_key = base_client.api_key
        self.json_mode = base_client.json_mode
        self.base_url = base_client.base_url
        self.omit_temperature = base_client.omit_temperature

    @staticmethod
    def _curl_quote(value: str) -> str:
        return value.replace("\\", "\\\\").replace('"', '\\"')

    def complete(self, prompt: dict[str, Any]) -> str:
        payload: dict[str, Any] = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": str(prompt.get("system_prompt", ""))},
                {"role": "user", "content": str(prompt.get("user_prompt", ""))},
            ],
        }
        if not self.omit_temperature:
            payload["temperature"] = self.temperature
        if self.json_mode:
            payload["response_format"] = {"type": "json_object"}

        fd, raw_path = tempfile.mkstemp(prefix="telephone-curl-", suffix=".conf")
        config_path = Path(raw_path)
        try:
            os.fchmod(fd, 0o600)
            config_text = "\n".join([
                f'url = "{self._curl_quote(self.base_url)}"',
                f'header = "Authorization: Bearer {self._curl_quote(self.api_key)}"',
                'header = "Content-Type: application/json"',
                'request = "POST"',
                'data-binary = "@-"',
                "http1.1",
                "silent",
                "show-error",
                f"max-time = {int(self.timeout)}",
                'write-out = "\\n%{http_code}"',
                "",
            ])
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                handle.write(config_text)
            fd = -1
            completed = subprocess.run(
                ["curl", "--config", str(config_path)],
                input=json.dumps(payload),
                text=True,
                encoding="utf-8",
                errors="replace",
                capture_output=True,
                timeout=self.timeout + 5,
                check=False,
            )
        finally:
            if fd >= 0:
                os.close(fd)
            config_path.unlink(missing_ok=True)

        if completed.returncode != 0:
            raise RuntimeError(f"curl request failed: {completed.stderr.strip()}")
        body, separator, status_text = (completed.stdout or "").rpartition("\n")
        if not separator or not status_text.isdigit():
            raise RuntimeError("curl response missing HTTP status")
        status_code = int(status_text)
        if status_code < 200 or status_code >= 300:
            raise RuntimeError(f"Chat Completions API HTTP {status_code}: {body}")
        data = json.loads(body)
        choices = data.get("choices")
        if not choices:
            raise RuntimeError(f"Chat Completions response has no choices: {data}")
        content = choices[0].get("message", {}).get("content")
        if not isinstance(content, str):
            raise RuntimeError(f"Chat Completions response has no text content: {data}")
        return content


class LLM:
    """Wraps the proven provider transport. `model` overrides the config model."""

    def __init__(self, config: Path | str = DEFAULT_CONFIG, model: str | None = None) -> None:
        args = argparse.Namespace(
            config=Path(config), provider=None, model=model, temperature=None,
            timeout=None, sleep=None, no_json_mode=False, workers=None,
        )
        self.config = mcr.resolve_run_config(args)
        base_client = mcr.build_client(self.config)
        self.client = (
            _SecureCurlChatClient(base_client)
            if self.config.wire_api == "chat_completions" and self.config.transport == "curl"
            else base_client
        )
        self._counter_lock = threading.Lock()
        self._logical_calls = 0
        self._transport_attempts = 0
        self._successful_calls = 0

    def complete(self, system: str, user: str) -> str:
        prompt = {"system_prompt": system, "user_prompt": user}
        with self._counter_lock:
            self._logical_calls += 1
        attempts = 0
        retries = int(getattr(self.config, "retries", 0))
        retry_sleep = float(getattr(self.config, "retry_sleep", 1.0))
        while True:
            attempts += 1
            with self._counter_lock:
                self._transport_attempts += 1
            try:
                result = self.client.complete(prompt)
                with self._counter_lock:
                    self._successful_calls += 1
                return result
            except Exception:
                if attempts > retries:
                    raise
                time.sleep(retry_sleep)

    def complete_json(self, system: str, user: str) -> dict[str, Any]:
        parsed = mcr.parse_response_json(self.complete(system, user))
        return parsed if isinstance(parsed, dict) else {}

    def usage_snapshot(self) -> dict[str, int]:
        """Thread-safe counts of logical model calls and transport attempts."""
        with self._counter_lock:
            return {
                "logical_calls": self._logical_calls,
                "transport_attempts": self._transport_attempts,
                "successful_calls": self._successful_calls,
            }
