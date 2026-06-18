#!/usr/bin/env python3
"""Thin LLM client for the society simulation, reusing the diagnostic_v0 runner."""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path
from typing import Any

# Reuse the proven provider transport + configs from the parent project (3-SMGA).
_DIAG = Path(__file__).resolve().parents[2] / "3-SMGA" / "benchmarks" / "diagnostic_v0"
if str(_DIAG) not in sys.path:
    sys.path.insert(0, str(_DIAG))

import model_calling_runner as mcr  # noqa: E402

DEFAULT_CONFIG = _DIAG / "configs" / "fhl_responses_gpt54_config.example.json"


class LLM:
    """Wraps the proven provider transport. `model` overrides the config model."""

    def __init__(self, config: Path | str = DEFAULT_CONFIG, model: str | None = None) -> None:
        args = argparse.Namespace(
            config=Path(config), provider=None, model=model, temperature=None,
            timeout=None, sleep=None, no_json_mode=False, workers=None,
        )
        self.config = mcr.resolve_run_config(args)
        self.client = mcr.build_client(self.config)

    def complete(self, system: str, user: str) -> str:
        prompt = {"system_prompt": system, "user_prompt": user}
        attempts = 0
        retries = int(getattr(self.config, "retries", 0))
        retry_sleep = float(getattr(self.config, "retry_sleep", 1.0))
        while True:
            attempts += 1
            try:
                return self.client.complete(prompt)
            except Exception:
                if attempts > retries:
                    raise
                time.sleep(retry_sleep)

    def complete_json(self, system: str, user: str) -> dict[str, Any]:
        parsed = mcr.parse_response_json(self.complete(system, user))
        return parsed if isinstance(parsed, dict) else {}
