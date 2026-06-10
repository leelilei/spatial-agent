#!/usr/bin/env python3
"""Run SMGA prompt bundles through a model provider.

The runner reads prompt JSONL files produced by `baseline_harness.py`, records
raw model outputs, and creates a response draft whose scorer-facing fields can
be filled by a later condition-blind normalizer.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Protocol


DEFAULT_TEMPERATURE = 0.0
DEFAULT_TIMEOUT_SECONDS = 120
DEFAULT_PROVIDER = "mock"
DEFAULT_MODEL = "mock-baseline"


class ModelClient(Protocol):
    def complete(self, prompt: dict[str, Any]) -> str:
        """Return the raw model text for one prompt record."""


@dataclass(frozen=True)
class RunConfig:
    provider: str
    model: str
    temperature: float
    timeout: int
    sleep: float
    json_mode: bool


@dataclass(frozen=True)
class MockClient:
    model: str

    def complete(self, prompt: dict[str, Any]) -> str:
        probe_id = str(prompt.get("probe_id", "unknown_probe"))
        return json.dumps(
            {
                "probe_id": probe_id,
                "response_text": (
                    f"Mock response for {probe_id}. Replace this with a real model "
                    "answer before scoring baseline performance."
                ),
            },
            ensure_ascii=False,
        )


@dataclass(frozen=True)
class OpenAIChatClient:
    model: str
    temperature: float
    timeout: int
    api_key: str
    json_mode: bool = True

    def complete(self, prompt: dict[str, Any]) -> str:
        payload: dict[str, Any] = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": str(prompt.get("system_prompt", ""))},
                {"role": "user", "content": str(prompt.get("user_prompt", ""))},
            ],
            "temperature": self.temperature,
        }
        if self.json_mode:
            payload["response_format"] = {"type": "json_object"}

        request = urllib.request.Request(
            "https://api.openai.com/v1/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                data = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"OpenAI API HTTP {exc.code}: {detail}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"OpenAI API request failed: {exc}") from exc

        choices = data.get("choices")
        if not choices:
            raise RuntimeError(f"OpenAI API response has no choices: {data}")
        content = choices[0].get("message", {}).get("content")
        if not isinstance(content, str):
            raise RuntimeError(f"OpenAI API response has no text content: {data}")
        return content


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as file:
        for line_no, line in enumerate(file, start=1):
            if not line.strip():
                continue
            record = json.loads(line)
            if not isinstance(record, dict):
                raise TypeError(f"{path}:{line_no} must contain a JSON object")
            records.append(record)
    return records


def load_json_object(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise TypeError(f"{path} must contain a JSON object")
    return data


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
            file.write("\n")


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as file:
        json.dump(data, file, indent=2, ensure_ascii=False, sort_keys=True)
        file.write("\n")


def parse_response_json(raw_text: str) -> dict[str, Any] | None:
    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError:
        data = parse_embedded_json_object(raw_text)
    if isinstance(data, dict):
        return data
    return None


def parse_embedded_json_object(raw_text: str) -> Any:
    start = raw_text.find("{")
    end = raw_text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return None
    try:
        return json.loads(raw_text[start : end + 1])
    except json.JSONDecodeError:
        return None


def build_client(config: RunConfig) -> ModelClient:
    if config.provider == "mock":
        return MockClient(model=config.model)
    if config.provider == "openai_chat":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is required for --provider openai_chat")
        return OpenAIChatClient(
            model=config.model,
            temperature=config.temperature,
            timeout=config.timeout,
            api_key=api_key,
            json_mode=config.json_mode,
        )
    raise ValueError(f"unsupported provider: {config.provider}")


def resolve_run_config(args: argparse.Namespace) -> RunConfig:
    config_doc: dict[str, Any] = {}
    if args.config:
        config_doc = load_json_object(args.config)

    provider = args.provider or str(config_doc.get("provider", DEFAULT_PROVIDER))
    model = args.model or str(config_doc.get("model", DEFAULT_MODEL))
    temperature = args.temperature
    if temperature is None:
        temperature = float(config_doc.get("temperature", DEFAULT_TEMPERATURE))
    timeout = args.timeout
    if timeout is None:
        timeout = int(config_doc.get("timeout", DEFAULT_TIMEOUT_SECONDS))
    sleep = args.sleep
    if sleep is None:
        sleep = float(config_doc.get("sleep", 0.0))
    json_mode = bool(config_doc.get("json_mode", True))
    if args.no_json_mode:
        json_mode = False

    return RunConfig(
        provider=provider,
        model=model,
        temperature=float(temperature),
        timeout=int(timeout),
        sleep=float(sleep),
        json_mode=json_mode,
    )


def default_raw_output_path(prompt_path: Path, output_dir: Path | None) -> Path:
    stem = prompt_path.stem
    if stem.endswith("_prompts"):
        stem = stem[: -len("_prompts")]
    filename = f"{stem}_raw_outputs.jsonl"
    return (output_dir or prompt_path.parent) / filename


def default_response_draft_path(prompt_path: Path, output_dir: Path | None) -> Path:
    stem = prompt_path.stem
    if stem.endswith("_prompts"):
        stem = stem[: -len("_prompts")]
    filename = f"{stem}_responses.raw_draft.json"
    return (output_dir or prompt_path.parent) / filename


def run_prompts(
    *,
    prompt_path: Path,
    client: ModelClient,
    provider: str,
    model: str,
    temperature: float,
    limit: int | None,
    sleep_seconds: float,
) -> list[dict[str, Any]]:
    prompts = load_jsonl(prompt_path)
    if limit is not None:
        prompts = prompts[:limit]

    records: list[dict[str, Any]] = []
    for index, prompt in enumerate(prompts, start=1):
        started_at = utc_now()
        start_time = time.monotonic()
        raw_text = ""
        parsed_json: dict[str, Any] | None = None
        error = None
        status = "ok"
        try:
            raw_text = client.complete(prompt)
            parsed_json = parse_response_json(raw_text)
            if parsed_json is None:
                status = "unparseable_json"
        except Exception as exc:  # Provider failures should be captured per probe.
            status = "error"
            error = str(exc)

        elapsed_ms = int((time.monotonic() - start_time) * 1000)
        records.append(
            {
                "scenario_id": prompt.get("scenario_id"),
                "seed_id": prompt.get("seed_id"),
                "condition_id": prompt.get("condition_id"),
                "probe_id": prompt.get("probe_id"),
                "provider": provider,
                "model": model,
                "temperature": temperature,
                "status": status,
                "started_at": started_at,
                "elapsed_ms": elapsed_ms,
                "raw_response_text": raw_text,
                "parsed_response_json": parsed_json,
                "error": error,
            }
        )
        print(f"{index}/{len(prompts)} {prompt.get('probe_id')}: {status}")
        if sleep_seconds and index < len(prompts):
            time.sleep(sleep_seconds)
    return records


def merge_response_draft(
    *,
    template_path: Path,
    raw_records: list[dict[str, Any]],
    provider: str,
    model: str,
    temperature: float,
) -> dict[str, Any]:
    draft = load_json_object(template_path)
    raw_by_probe = {record.get("probe_id"): record for record in raw_records}

    model_config = draft.setdefault("model_config", {})
    model_config.update(
        {
            "provider": provider,
            "model": model,
            "temperature": temperature,
        }
    )

    for response in draft.get("responses", []):
        if not isinstance(response, dict):
            continue
        probe_id = response.get("probe_id")
        raw_record = raw_by_probe.get(probe_id)
        if not raw_record:
            continue
        parsed = raw_record.get("parsed_response_json")
        response_text = ""
        if isinstance(parsed, dict):
            response_text = str(parsed.get("response_text", ""))
        response["response_text"] = response_text
        response["raw_model_output"] = raw_record
        response["normalization_notes"] = (
            "Raw model output captured; condition-blind normalization pending."
        )
    return draft


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run SMGA prompt bundles through a model provider.")
    parser.add_argument("prompts_jsonl", type=Path, help="Prompt JSONL produced by baseline_harness.py.")
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Optional model config JSON. CLI provider/model flags override matching config fields.",
    )
    parser.add_argument(
        "--provider",
        choices=("mock", "openai_chat"),
        default=None,
        help="Model provider. Defaults to config value or mock.",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Model name or mock model label.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=None,
        help="Sampling temperature passed to real providers.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=None,
        help="HTTP timeout in seconds for real providers.",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=None,
        help="Seconds to sleep between provider calls.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional maximum number of prompts to run.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Directory for raw outputs and response draft. Defaults to the prompt file directory.",
    )
    parser.add_argument(
        "--raw-output",
        type=Path,
        default=None,
        help="Explicit raw outputs JSONL path.",
    )
    parser.add_argument(
        "--response-template",
        type=Path,
        default=None,
        help="Optional response template JSON from baseline_harness.py.",
    )
    parser.add_argument(
        "--response-draft",
        type=Path,
        default=None,
        help="Output path for response draft JSON.",
    )
    parser.add_argument(
        "--no-json-mode",
        action="store_true",
        help="Disable JSON response_format for openai_chat.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    prompt_path = args.prompts_jsonl
    raw_output_path = args.raw_output or default_raw_output_path(prompt_path, args.output_dir)
    response_draft_path = args.response_draft or default_response_draft_path(prompt_path, args.output_dir)

    try:
        config = resolve_run_config(args)
        client = build_client(config)
        raw_records = run_prompts(
            prompt_path=prompt_path,
            client=client,
            provider=config.provider,
            model=config.model,
            temperature=config.temperature,
            limit=args.limit,
            sleep_seconds=config.sleep,
        )
        write_jsonl(raw_output_path, raw_records)
        print(f"raw outputs: {raw_output_path}")

        if args.response_template:
            draft = merge_response_draft(
                template_path=args.response_template,
                raw_records=raw_records,
                provider=config.provider,
                model=config.model,
                temperature=config.temperature,
            )
            write_json(response_draft_path, draft)
            print(f"response draft: {response_draft_path}")
    except (OSError, json.JSONDecodeError, TypeError, ValueError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
