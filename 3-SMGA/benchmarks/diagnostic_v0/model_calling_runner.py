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
import subprocess
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
DEFAULT_WIRE_API = "chat_completions"
DEFAULT_CHAT_COMPLETIONS_URL = "https://api.openai.com/v1/chat/completions"
DEFAULT_RESPONSES_URL = "https://api.openai.com/v1/responses"
DEFAULT_BASE_URL = DEFAULT_CHAT_COMPLETIONS_URL


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
    retries: int = 0
    retry_sleep: float = 1.0
    wire_api: str = DEFAULT_WIRE_API
    base_url: str = DEFAULT_BASE_URL
    reasoning_effort: str | None = None
    service_tier: str | None = None
    store: bool | None = None
    omit_temperature: bool = False
    responses_input_mode: str = "messages"
    input_char_limit: int | None = None
    transport: str = "urllib"


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
    base_url: str = DEFAULT_BASE_URL
    omit_temperature: bool = False

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

        request = urllib.request.Request(
            self.base_url,
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


@dataclass(frozen=True)
class OpenAIResponsesClient:
    model: str
    temperature: float
    timeout: int
    api_key: str
    json_mode: bool = True
    base_url: str = DEFAULT_RESPONSES_URL
    reasoning_effort: str | None = None
    service_tier: str | None = None
    store: bool | None = None
    omit_temperature: bool = False
    input_mode: str = "messages"
    input_char_limit: int | None = None
    transport: str = "urllib"

    def complete(self, prompt: dict[str, Any]) -> str:
        payload = self.build_payload(prompt)
        if self.transport == "curl":
            return self.complete_with_curl(payload)
        if self.transport != "urllib":
            raise ValueError(f"unsupported responses transport: {self.transport}")

        request = urllib.request.Request(
            normalize_endpoint(self.base_url, "responses"),
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
            raise RuntimeError(f"Responses API HTTP {exc.code}: {detail}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"Responses API request failed: {exc}") from exc

        content = extract_responses_text(data)
        if not isinstance(content, str):
            raise RuntimeError(f"Responses API response has no text content: {data}")
        return content

    def complete_with_curl(self, payload: dict[str, Any]) -> str:
        command = [
            "curl",
            "-sS",
            normalize_endpoint(self.base_url, "responses"),
            "-H",
            f"Authorization: Bearer {self.api_key}",
            "-H",
            "Content-Type: application/json",
            "--data-binary",
            "@-",
            "--write-out",
            "\n%{http_code}",
        ]
        completed = subprocess.run(
            command,
            input=json.dumps(payload),
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=self.timeout,
            check=False,
        )
        if completed.returncode != 0:
            raise RuntimeError(f"curl request failed: {completed.stderr.strip()}")
        output = completed.stdout or ""
        body, separator, status_text = output.rpartition("\n")
        if not separator or not status_text.isdigit():
            raise RuntimeError(f"curl response missing HTTP status: {output}")
        status_code = int(status_text)
        if status_code < 200 or status_code >= 300:
            raise RuntimeError(f"Responses API HTTP {status_code}: {body}")
        try:
            data = json.loads(body)
        except json.JSONDecodeError as exc:
            content = extract_responses_text_from_raw_body(body)
            if isinstance(content, str):
                return content
            raise RuntimeError(f"Responses API returned invalid JSON: {body}") from exc
        content = extract_responses_text(data)
        if not isinstance(content, str):
            raise RuntimeError(f"Responses API response has no text content: {data}")
        return content

    def build_payload(self, prompt: dict[str, Any]) -> dict[str, Any]:
        payload: dict[str, Any] = {"model": self.model}
        if self.input_mode == "string":
            input_text = format_responses_string_input(prompt)
            if self.input_char_limit is not None:
                input_text = input_text[: self.input_char_limit]
            payload["input"] = input_text
        elif self.input_mode == "user":
            input_text = str(prompt.get("user_prompt", "")).strip()
            if self.input_char_limit is not None:
                input_text = input_text[: self.input_char_limit]
            payload["input"] = input_text
        elif self.input_mode == "literal_ok":
            input_text = "Reply with exactly: ok"
            if self.input_char_limit is not None:
                input_text = input_text[: self.input_char_limit]
            payload["input"] = input_text
        elif self.input_mode == "messages":
            payload["input"] = [
                {"role": "system", "content": str(prompt.get("system_prompt", ""))},
                {"role": "user", "content": str(prompt.get("user_prompt", ""))},
            ]
        else:
            raise ValueError(f"unsupported responses_input_mode: {self.input_mode}")
        if not self.omit_temperature:
            payload["temperature"] = self.temperature
        if self.json_mode:
            payload["text"] = {"format": {"type": "json_object"}}
        if self.reasoning_effort:
            payload["reasoning"] = {"effort": self.reasoning_effort}
        if self.service_tier:
            payload["service_tier"] = self.service_tier
        if self.store is not None:
            payload["store"] = self.store
        return payload


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


def normalize_endpoint(base_url: str, wire_api: str) -> str:
    if base_url.endswith("/chat/completions") or base_url.endswith("/responses"):
        return base_url
    if wire_api == "responses":
        return f"{base_url.rstrip('/')}/v1/responses"
    return f"{base_url.rstrip('/')}/v1/chat/completions"


def extract_responses_text(data: dict[str, Any]) -> str | None:
    output_text = data.get("output_text")
    if isinstance(output_text, str):
        return output_text

    output = data.get("output")
    if not isinstance(output, list):
        return None

    chunks: list[str] = []
    for item in output:
        if not isinstance(item, dict):
            continue
        content = item.get("content")
        if not isinstance(content, list):
            continue
        for part in content:
            if not isinstance(part, dict):
                continue
            text = part.get("text")
            if isinstance(text, str):
                chunks.append(text)
    if chunks:
        return "".join(chunks)
    return None


def extract_responses_text_from_raw_body(body: str) -> str | None:
    """Best-effort recovery for proxy responses with malformed JSON escaping."""
    start_token = '"text":"'
    start = body.find(start_token)
    if start == -1:
        return None
    start += len(start_token)

    end_candidates = [
        body.find('"}],"status"', start),
        body.find('"}]},"usage"', start),
        body.find('"}]}', start),
    ]
    end_candidates = [index for index in end_candidates if index != -1]
    if not end_candidates:
        return None
    raw_text = body[start : min(end_candidates)]

    try:
        return json.loads(f'"{raw_text}"')
    except json.JSONDecodeError:
        return raw_text.replace(r"\"", '"').replace(r"\\", "\\")


def get_api_key(provider: str) -> str:
    provider_env_name = f"{provider.upper()}_API_KEY"
    api_key = os.environ.get(provider_env_name) or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            f"{provider_env_name} or OPENAI_API_KEY is required for --provider {provider}"
        )
    return api_key


def format_responses_string_input(prompt: dict[str, Any]) -> str:
    system_prompt = str(prompt.get("system_prompt", "")).strip()
    user_prompt = str(prompt.get("user_prompt", "")).strip()
    if system_prompt and user_prompt:
        return f"System instructions:\n{system_prompt}\n\nUser prompt:\n{user_prompt}"
    return system_prompt or user_prompt


def build_client(config: RunConfig) -> ModelClient:
    if config.provider == "mock":
        return MockClient(model=config.model)
    if config.wire_api == "chat_completions":
        api_key = get_api_key(config.provider)
        return OpenAIChatClient(
            model=config.model,
            temperature=config.temperature,
            timeout=config.timeout,
            api_key=api_key,
            json_mode=config.json_mode,
            base_url=normalize_endpoint(config.base_url, config.wire_api),
            omit_temperature=config.omit_temperature,
        )
    if config.wire_api == "responses":
        api_key = get_api_key(config.provider)
        return OpenAIResponsesClient(
            model=config.model,
            temperature=config.temperature,
            timeout=config.timeout,
            api_key=api_key,
            json_mode=config.json_mode,
            base_url=config.base_url,
            reasoning_effort=config.reasoning_effort,
            service_tier=config.service_tier,
            store=config.store,
            omit_temperature=config.omit_temperature,
            input_mode=config.responses_input_mode,
            input_char_limit=config.input_char_limit,
            transport=config.transport,
        )
    raise ValueError(f"unsupported wire_api for provider {config.provider}: {config.wire_api}")


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
    retries = int(config_doc.get("retries", 0))
    retry_sleep = float(config_doc.get("retry_sleep", 1.0))
    wire_api = str(config_doc.get("wire_api", DEFAULT_WIRE_API))
    base_url = str(config_doc.get("base_url", DEFAULT_BASE_URL))
    reasoning_effort = config_doc.get("reasoning_effort", config_doc.get("model_reasoning_effort"))
    if reasoning_effort is not None:
        reasoning_effort = str(reasoning_effort)
    service_tier = config_doc.get("service_tier")
    if service_tier is not None:
        service_tier = str(service_tier)
    store = config_doc.get("store")
    if "disable_response_storage" in config_doc:
        store = not bool(config_doc["disable_response_storage"])
    if store is not None:
        store = bool(store)
    omit_temperature = bool(config_doc.get("omit_temperature", False))
    responses_input_mode = str(config_doc.get("responses_input_mode", "messages"))
    input_char_limit = config_doc.get("input_char_limit")
    if input_char_limit is not None:
        input_char_limit = int(input_char_limit)
    transport = str(config_doc.get("transport", "urllib"))

    return RunConfig(
        provider=provider,
        model=model,
        temperature=float(temperature),
        timeout=int(timeout),
        sleep=float(sleep),
        json_mode=json_mode,
        retries=retries,
        retry_sleep=retry_sleep,
        wire_api=wire_api,
        base_url=base_url,
        reasoning_effort=reasoning_effort,
        service_tier=service_tier,
        store=store,
        omit_temperature=omit_temperature,
        responses_input_mode=responses_input_mode,
        input_char_limit=input_char_limit,
        transport=transport,
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
    probe_ids: set[str],
    sleep_seconds: float,
    retries: int,
    retry_sleep: float,
) -> list[dict[str, Any]]:
    prompts = load_jsonl(prompt_path)
    if probe_ids:
        prompts = [prompt for prompt in prompts if str(prompt.get("probe_id")) in probe_ids]
    if limit is not None:
        prompts = prompts[:limit]

    records: list[dict[str, Any]] = []
    for index, prompt in enumerate(prompts, start=1):
        print(f"{index}/{len(prompts)} {prompt.get('probe_id')}: calling", flush=True)
        started_at = utc_now()
        start_time = time.monotonic()
        raw_text = ""
        parsed_json: dict[str, Any] | None = None
        error = None
        status = "ok"
        attempts = 0
        while True:
            attempts += 1
            try:
                raw_text = client.complete(prompt)
                parsed_json = parse_response_json(raw_text)
                status = "unparseable_json" if parsed_json is None else "ok"
                error = None
                break
            except Exception as exc:  # Provider failures should be captured per probe.
                status = "error"
                error = str(exc)
                if attempts > retries:
                    break
                print(
                    f"{index}/{len(prompts)} {prompt.get('probe_id')}: retry {attempts}/{retries} after {error}",
                    flush=True,
                )
                time.sleep(retry_sleep)

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
                "attempts": attempts,
                "started_at": started_at,
                "elapsed_ms": elapsed_ms,
                "raw_response_text": raw_text,
                "parsed_response_json": parsed_json,
                "error": error,
            }
        )
        print(f"{index}/{len(prompts)} {prompt.get('probe_id')}: {status}", flush=True)
        if sleep_seconds and index < len(prompts):
            time.sleep(sleep_seconds)
    return records


def config_summary(config: RunConfig) -> dict[str, Any]:
    return {
        "provider": config.provider,
        "model": config.model,
        "wire_api": config.wire_api,
        "endpoint": normalize_endpoint(config.base_url, config.wire_api),
        "temperature": config.temperature,
        "timeout": config.timeout,
        "sleep": config.sleep,
        "retries": config.retries,
        "retry_sleep": config.retry_sleep,
        "json_mode": config.json_mode,
        "reasoning_effort": config.reasoning_effort,
        "service_tier": config.service_tier,
        "store": config.store,
        "omit_temperature": config.omit_temperature,
        "responses_input_mode": config.responses_input_mode,
        "input_char_limit": config.input_char_limit,
        "transport": config.transport,
    }


def auth_summary(provider: str) -> dict[str, bool]:
    provider_env_name = f"{provider.upper()}_API_KEY"
    return {
        provider_env_name: bool(os.environ.get(provider_env_name)),
        "OPENAI_API_KEY": bool(os.environ.get("OPENAI_API_KEY")),
    }


def first_payload_summary(
    config: RunConfig,
    prompt_path: Path,
    probe_ids: set[str],
) -> dict[str, Any]:
    prompts = load_jsonl(prompt_path)
    if probe_ids:
        prompts = [prompt for prompt in prompts if str(prompt.get("probe_id")) in probe_ids]
    if not prompts:
        raise ValueError(f"{prompt_path} contains no prompts")
    if config.wire_api != "responses":
        raise ValueError("--print-first-payload currently supports wire_api=responses only")
    client = OpenAIResponsesClient(
        model=config.model,
        temperature=config.temperature,
        timeout=config.timeout,
        api_key="redacted",
        json_mode=config.json_mode,
        base_url=config.base_url,
        reasoning_effort=config.reasoning_effort,
        service_tier=config.service_tier,
        store=config.store,
        omit_temperature=config.omit_temperature,
        input_mode=config.responses_input_mode,
        input_char_limit=config.input_char_limit,
        transport=config.transport,
    )
    return client.build_payload(prompts[0])


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
        default=None,
        help="Model provider label. Defaults to config value or mock.",
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
        "--probe-id",
        action="append",
        default=[],
        help="Run only a specific probe_id. May be passed multiple times.",
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
    parser.add_argument(
        "--print-config",
        action="store_true",
        help="Print resolved non-secret config and exit without calling a provider.",
    )
    parser.add_argument(
        "--print-first-payload",
        action="store_true",
        help="Print the first non-secret request payload and exit without calling a provider.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    prompt_path = args.prompts_jsonl
    raw_output_path = args.raw_output or default_raw_output_path(prompt_path, args.output_dir)
    response_draft_path = args.response_draft or default_response_draft_path(prompt_path, args.output_dir)

    try:
        config = resolve_run_config(args)
        if args.print_config:
            summary = config_summary(config)
            summary["auth_env_present"] = auth_summary(config.provider)
            print(json.dumps(summary, indent=2, ensure_ascii=False, sort_keys=True))
            return 0
        if args.print_first_payload:
            print(
                json.dumps(
                    first_payload_summary(config, prompt_path, set(args.probe_id)),
                    indent=2,
                    ensure_ascii=False,
                    sort_keys=True,
                )
            )
            return 0
        client = build_client(config)
        raw_records = run_prompts(
            prompt_path=prompt_path,
            client=client,
            provider=config.provider,
            model=config.model,
            temperature=config.temperature,
            limit=args.limit,
            probe_ids=set(args.probe_id),
            sleep_seconds=config.sleep,
            retries=config.retries,
            retry_sleep=config.retry_sleep,
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
