from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Protocol

from prompts import SYSTEM_PROMPT, format_user_prompt


class Agent(Protocol):
    name: str
    total_tokens: int
    total_cost: float

    def choose_action(
        self, state: dict, observation: str, allowed_actions: list[str], recent_actions: list[str]
    ) -> str:
        ...


@dataclass
class RuleAgent:
    name: str = "rule"
    total_tokens: int = 0
    total_cost: float = 0.0

    def choose_action(
        self, state: dict, observation: str, allowed_actions: list[str], recent_actions: list[str]
    ) -> str:
        current_room = state["current_room"]
        inventory = state["inventory"]
        visible_items = state["visible_items"]
        locked_rooms = state["locked_rooms"]

        if (
            current_room == "entrance"
            and "sign" in visible_items
            and "read sign" in allowed_actions
            and "read sign" not in recent_actions
        ):
            return "read sign"
        if (
            current_room == "office"
            and "note" in visible_items
            and "read note" in allowed_actions
            and "read note" not in recent_actions
        ):
            return "read note"
        if "meeting_key" in visible_items and "meeting_key" not in inventory:
            return "take meeting_key"
        if current_room == "storage" and "meeting_key" in inventory and "meeting_room" in locked_rooms:
            return "open meeting_room"
        if "file" in visible_items:
            return "take file"
        if current_room == "entrance":
            return "go corridor"
        if current_room == "corridor":
            if "meeting_key" not in inventory:
                return "go storage"
            return "go storage"
        if current_room == "storage":
            if "meeting_room" not in locked_rooms:
                return "go meeting_room"
            return "go corridor"
        if current_room in {"office", "stairwell", "meeting_room"}:
            return "go corridor" if "go corridor" in allowed_actions else allowed_actions[0]
        return allowed_actions[0]


class LLMAgent:
    name = "openai"

    def __init__(self, model: str | None = None, timeout: float = 20.0) -> None:
        self.model = model or os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")
        self.timeout = timeout
        self.total_tokens = 0
        self.total_cost = 0.0
        self._client = None

    def choose_action(
        self, state: dict, observation: str, allowed_actions: list[str], recent_actions: list[str]
    ) -> str:
        if not os.environ.get("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY is not set.")

        if self._client is None:
            from openai import OpenAI

            self._client = OpenAI(timeout=self.timeout)

        prompt = format_user_prompt(state, allowed_actions, recent_actions)
        response = self._client.responses.create(
            model=self.model,
            instructions=SYSTEM_PROMPT,
            input=prompt,
            temperature=0,
        )

        usage = getattr(response, "usage", None)
        if usage is not None:
            total_tokens = getattr(usage, "total_tokens", None)
            if isinstance(total_tokens, int):
                self.total_tokens += total_tokens

        return normalize_action(response.output_text)


@dataclass
class AutoAgent:
    primary: LLMAgent
    fallback: RuleAgent
    name: str = "auto"

    @property
    def total_tokens(self) -> int:
        return self.primary.total_tokens + self.fallback.total_tokens

    @property
    def total_cost(self) -> float:
        return self.primary.total_cost + self.fallback.total_cost

    def choose_action(
        self, state: dict, observation: str, allowed_actions: list[str], recent_actions: list[str]
    ) -> str:
        try:
            return self.primary.choose_action(state, observation, allowed_actions, recent_actions)
        except Exception:
            return self.fallback.choose_action(state, observation, allowed_actions, recent_actions)


def normalize_action(text: str) -> str:
    for line in text.splitlines():
        action = line.strip().strip("`").strip()
        if action:
            return action
    return ""


def create_agent(agent_name: str) -> Agent:
    if agent_name == "rule":
        return RuleAgent()
    if agent_name == "openai":
        return LLMAgent()
    if agent_name == "auto":
        return AutoAgent(primary=LLMAgent(), fallback=RuleAgent())
    raise ValueError(f"Unknown agent: {agent_name}")
