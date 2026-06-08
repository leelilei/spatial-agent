from __future__ import annotations

import argparse
from pathlib import Path

from agent import create_agent
from main import run_episode


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate Building Room Finder Agent")
    parser.add_argument("--episodes", type=int, default=10)
    parser.add_argument("--agent", choices=["auto", "openai", "rule"], default="auto")
    parser.add_argument("--log-dir", default="logs")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    log_dir = Path(args.log_dir)
    results = []

    for episode_id in range(1, args.episodes + 1):
        agent = create_agent(args.agent)
        metrics = run_episode(
            agent=agent,
            episode_id=episode_id,
            interactive=False,
            log_dir=log_dir,
            echo=False,
        )
        results.append(metrics)

    successes = sum(1 for result in results if result["success"])
    total_steps = sum(result["step_count"] for result in results)
    total_invalid = sum(result["invalid_action_count"] for result in results)
    total_repeated = sum(result["repeated_action_count"] for result in results)
    total_tokens = sum(result["total_tokens"] for result in results)
    total_cost = sum(result["total_cost"] for result in results)

    print(f"Episodes: {args.episodes}")
    print(f"Agent: {args.agent}")
    print(f"Success rate: {successes / args.episodes:.2%}")
    print(f"Average steps: {total_steps / args.episodes:.2f}")
    print(f"Invalid action count: {total_invalid}")
    print(f"Invalid action rate: {total_invalid / max(total_steps, 1):.2%}")
    print(f"Repeated action count: {total_repeated}")
    print(f"Total tokens: {total_tokens}")
    print(f"Total cost: {total_cost:.6f}")
    print(f"Logs saved to: {log_dir}")


if __name__ == "__main__":
    main()
