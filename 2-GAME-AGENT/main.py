from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from agent import Agent, create_agent
from env import BuildingRoomEnv


def run_episode(
    agent: Agent | None = None,
    episode_id: int = 1,
    interactive: bool = False,
    log_dir: Path | None = None,
    echo: bool = True,
) -> dict[str, Any]:
    env = BuildingRoomEnv()
    observation = env.reset()
    logs: list[dict[str, Any]] = []
    recent_actions: list[str] = []

    if echo:
        print(observation)

    while not env.done:
        state = env.get_state()
        allowed_actions = env.allowed_actions()

        if interactive:
            print("\nAllowed actions:")
            for action in allowed_actions:
                print(f"- {action}")
            action = input("> ").strip()
        else:
            if agent is None:
                raise ValueError("Agent is required when interactive is False.")
            action = agent.choose_action(state, observation, allowed_actions, recent_actions)
            if echo:
                print(f"\nAction: {action}")

        result = env.step(action)
        recent_actions.append(action)
        observation = result.observation

        logs.append(
            {
                "episode_id": episode_id,
                "step": env.step_count,
                "current_room": state["current_room"],
                "observation": observation,
                "allowed_actions": allowed_actions,
                "agent_action": action,
                "is_valid_action": result.is_valid_action,
                "reward": result.reward,
                "done": result.done,
                "success": result.success,
                "inventory": list(env.inventory),
            }
        )

        if echo:
            print(observation)

    metrics = {
        "episode_id": episode_id,
        "success": env.success,
        "step_count": env.step_count,
        "invalid_action_count": env.invalid_action_count,
        "repeated_action_count": env.repeated_action_count,
        "total_tokens": getattr(agent, "total_tokens", 0) if agent is not None else 0,
        "total_cost": getattr(agent, "total_cost", 0.0) if agent is not None else 0.0,
        "trajectory": logs,
    }

    if log_dir is not None:
        log_dir.mkdir(parents=True, exist_ok=True)
        log_path = log_dir / f"episode_{episode_id:03d}.json"
        log_path.write_text(json.dumps(metrics, indent=2, ensure_ascii=False), encoding="utf-8")

    return metrics


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Building Room Finder Agent")
    parser.add_argument("--mode", choices=["manual", "agent"], default="manual")
    parser.add_argument("--agent", choices=["auto", "openai", "rule"], default="auto")
    parser.add_argument("--episode-id", type=int, default=1)
    parser.add_argument("--log-dir", default="logs")
    parser.add_argument("--quiet", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    agent = None if args.mode == "manual" else create_agent(args.agent)
    metrics = run_episode(
        agent=agent,
        episode_id=args.episode_id,
        interactive=args.mode == "manual",
        log_dir=Path(args.log_dir),
        echo=not args.quiet,
    )
    print(
        "\nResult: "
        f"success={metrics['success']}, "
        f"steps={metrics['step_count']}, "
        f"invalid_actions={metrics['invalid_action_count']}"
    )


if __name__ == "__main__":
    main()
