"""LLM API 调用封装模块。"""

from __future__ import annotations

import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import httpx
from llm.cache import ResponseCache


@dataclass
class LLMResponse:
    text: str
    model: str
    cache_hit: bool = False
    latency_ms: int | None = None
    raw: dict[str, Any] | None = None


class OpenAICompatibleClient:
    """OpenAI-compatible chat client with cache and retry."""

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str | None,
        wire_api: str = "chat_completions",
        cache: ResponseCache | None = None,
        max_retries: int = 2,
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url
        self.wire_api = wire_api
        self.cache = cache
        self.max_retries = max_retries

    def complete(
        self,
        *,
        model: str,
        messages: list[dict[str, str]],
        temperature: float,
        max_tokens: int,
    ) -> LLMResponse:
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "base_url": self.base_url,
        }
        cache_key = self.cache.make_key(payload) if self.cache is not None else None
        if cache_key is not None:
            cached = self.cache.get(cache_key)
            if cached is not None:
                return LLMResponse(
                    text=str(cached["text"]),
                    model=model,
                    cache_hit=True,
                    latency_ms=cached.get("latency_ms"),
                    raw=cached,
                )

        last_error: Exception | None = None
        for _ in range(self.max_retries + 1):
            try:
                start = time.perf_counter()
                text, raw = self._request(model=model, messages=messages, temperature=temperature, max_tokens=max_tokens)
                latency_ms = int((time.perf_counter() - start) * 1000)
                if cache_key is not None and self.cache is not None:
                    self.cache.set(cache_key, {"text": text, "latency_ms": latency_ms, "raw": raw})
                return LLMResponse(text=text, model=model, cache_hit=False, latency_ms=latency_ms, raw=raw)
            except Exception as exc:  # pragma: no cover - exercised via mocks in tests
                last_error = exc
        raise RuntimeError(f"LLM request failed after retries: {last_error}") from last_error

    def _request(
        self,
        *,
        model: str,
        messages: list[dict[str, str]],
        temperature: float,
        max_tokens: int,
    ) -> tuple[str, dict[str, Any]]:
        if not self.base_url:
            raise ValueError("base_url is required for OpenAI-compatible requests.")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        if self.wire_api == "responses":
            payload = {
                "model": model,
                "input": _messages_to_input(messages),
                "temperature": temperature,
                "max_output_tokens": max_tokens,
            }
            endpoint = urljoin(self.base_url.rstrip("/") + "/", "responses")
        else:
            payload = {
                "model": model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
            }
            endpoint = urljoin(self.base_url.rstrip("/") + "/", "chat/completions")

        with httpx.Client(timeout=60.0) as client:
            response = client.post(endpoint, headers=headers, json=payload)
            response.raise_for_status()
            raw = response.json()
        text = _extract_text(raw)
        return text, raw


def build_llm_client(
    model_cfg: dict[str, Any],
    *,
    cache_dir: str | Path | None = None,
) -> OpenAICompatibleClient:
    api_key = os.getenv(model_cfg["api_key_env"])
    if not api_key:
        raise ValueError(f"Missing API key env: {model_cfg['api_key_env']}")
    base_url = os.getenv(model_cfg.get("base_url_env", ""), model_cfg.get("base_url"))
    cache = ResponseCache(cache_dir or ".cache/preflight_llm")
    return OpenAICompatibleClient(
        api_key=api_key,
        base_url=base_url,
        wire_api=model_cfg.get("wire_api", "chat_completions"),
        cache=cache,
    )


def _messages_to_input(messages: list[dict[str, str]]) -> str:
    return "\n\n".join(f"{message['role'].upper()}: {message['content']}" for message in messages)


def _extract_text(raw: dict[str, Any]) -> str:
    if "choices" in raw:
        choices = raw.get("choices") or []
        if choices:
            return str(((choices[0] or {}).get("message") or {}).get("content") or "")

    output = raw.get("output") or []
    collected: list[str] = []
    for item in output:
        for content in item.get("content", []):
            if content.get("type") in {"output_text", "text"} and content.get("text"):
                collected.append(str(content["text"]))
    if collected:
        return "\n".join(collected)

    if isinstance(raw.get("output_text"), str):
        return str(raw["output_text"])
    return ""
