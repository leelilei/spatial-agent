#!/usr/bin/env python3
"""Thin LLM client for the society simulation, reusing the diagnostic_v0 runner."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

_DIAG = Path(__file__).resolve().parents[1] / "benchmarks" / "diagnostic_v0"
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
        return self.client.complete({"system_prompt": system, "user_prompt": user})

    def complete_json(self, system: str, user: str) -> dict[str, Any]:
        parsed = mcr.parse_response_json(self.complete(system, user))
        return parsed if isinstance(parsed, dict) else {}
