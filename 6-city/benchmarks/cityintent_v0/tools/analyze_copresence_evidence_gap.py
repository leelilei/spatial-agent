"""Evidence-gap anatomy for failed co-presence outcomes (local, zero-API analysis).

For every co_presence OUTCOME condition that a baseline failed to earn, attribute
*why* it failed by replaying the trace against the scenario's co_presence
requirements (venue set, time window, message gate). This turns the aggregate
"legal but ineffective" headline into a per-mechanism failure taxonomy and pulls
concrete exemplar traces for the paper.

Failure classes (mutually exclusive, checked in order):
  no_venue_entry     - never entered any location in the condition's venue set
  entered_no_interact- entered a correct venue but never issued an `interact`
  interact_rejected  - issued `interact` but the environment rejected it at attempt
                       time (outside window, missing entry, or missing message gate)
  window_overrun     - met the right counterpart at the right venue and started
                       inside the window, but the interaction ran PAST the window
                       close, so it does not count (a timing-precision miss)
  wrong_target       - interacted, accepted, but with the wrong counterpart
  other              - none of the above (diagnostic catch-all)

Scans the two paper-backed baseline runs (easy + hard tiers) already on disk.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[2]
RESULTS = REPO_ROOT / "6-city" / "results" / "cityintent_v1_rc1"
SCENARIO_DIR = ROOT / "scenarios"

# All six policies per tier: the two paper-backed baselines plus the four
# adapted official decision layers.
RUNS = {
    "easy": [
        RESULTS / "paper_backed_baselines_2x6socialx3_gpt54mini_2026-07-07",
        RESULTS / "external_frameworks_4x6socialx1_gpt54mini_2026-07-06",
    ],
    "hard": [
        RESULTS / "paper_backed_baselines_2x6hardx3_gpt54mini_2026-07-09",
        RESULTS / "external_frameworks_4x6hardx3_gpt54mini_2026-07-10",
    ],
}
OUTPUT_DIR = RESULTS / "copresence_evidence_gap_six_policy_2026-07-10"


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def parse_time(value: str) -> int:
    h, m = value.split(":")
    return int(h) * 60 + int(m)


def scenario_copresence_specs(scenario: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Map each co_presence outcome id -> its requirements."""
    specs: dict[str, dict[str, Any]] = {}
    message_targets = {
        c.get("to")
        for c in scenario["success_conditions"]
        if c.get("type") == "send_message"
    }
    for c in scenario["success_conditions"]:
        if c.get("type") != "co_presence" or c.get("role") != "outcome":
            continue
        counterpart = next(
            (a for a in c.get("agents", []) if a != scenario["primary_agent"]), None
        )
        venues = set(c.get("location_any_of") or ([c.get("location")] if c.get("location") else []))
        start, end = (parse_time(t) for t in c["time_window"])
        specs[c["id"]] = {
            "counterpart": counterpart,
            "venues": venues,
            "window": (start, end),
            "requires_message": counterpart in message_targets,
        }
    return specs


def classify_failure(trace: dict[str, Any], spec: dict[str, Any]) -> str:
    venues = spec["venues"]
    counterpart = spec["counterpart"]
    _, window_end = spec["window"]
    entered_venue = any(e["location"] in venues for e in trace.get("entries", []))
    interact_actions = [
        step for step in trace.get("trace", [])
        if step.get("action", {}).get("kind") == "interact"
    ]
    accepted_here = [
        it for it in trace.get("interactions", [])
        if it.get("location") in venues
    ]
    with_counterpart = [it for it in accepted_here if it.get("with") == counterpart]
    if with_counterpart:
        # accepted at the right venue+person but the condition still scored < 1.0:
        # the interaction ended after the window closed.
        if any(int(it.get("end_time", it.get("time", 0))) > window_end for it in with_counterpart):
            return "window_overrun"
        return "other"
    if accepted_here:  # accepted, but only with someone else
        return "wrong_target"
    if not entered_venue:
        return "no_venue_entry"
    if not interact_actions:
        return "entered_no_interact"
    return "interact_rejected"


def analyze() -> dict[str, Any]:
    report: dict[str, Any] = {"tiers": {}}
    exemplars: list[dict[str, Any]] = []
    for tier, run_dirs in RUNS.items():
        per_policy: dict[str, Counter] = defaultdict(Counter)
        totals: dict[str, dict[str, int]] = defaultdict(lambda: {"failed": 0, "total": 0})
        judged_paths = [
            p
            for run_dir in run_dirs
            if run_dir.exists()
            for p in sorted(run_dir.glob("repeat_*/judged/judged_traces.json"))
        ]
        for judged in judged_paths:
            for trace in load_json(judged):
                scenario = load_json(SCENARIO_DIR / f"{trace['scenario_id']}.json")
                specs = scenario_copresence_specs(scenario)
                policy = (trace["agent_type"].replace("api_llm_", "")
                           .replace("_official_planner", "").replace("_official_llm_agent", "")
                           .replace("_official_plan_blocks", ""))
                for cond in trace["conditions"]:
                    if cond["type"] != "co_presence" or cond.get("role") != "outcome":
                        continue
                    spec = specs.get(cond["id"])
                    if spec is None:
                        continue
                    totals[policy]["total"] += 1
                    if cond["score"] >= 1.0:
                        continue
                    totals[policy]["failed"] += 1
                    reason = classify_failure(trace, spec)
                    per_policy[policy][reason] += 1
                    if reason in {"entered_no_interact", "interact_rejected"} and len(exemplars) < 14:
                        exemplars.append({
                            "tier": tier,
                            "scenario": trace["scenario_id"],
                            "policy": policy,
                            "outcome": cond["id"],
                            "reason": reason,
                            "feasibility": trace["metrics"].get("trace_feasibility"),
                            "messages": len(trace["messages"]),
                            "entered_venues": [e["location"] for e in trace["entries"]
                                               if e["location"] in spec["venues"]],
                            "n_interact_actions": sum(
                                1 for s in trace["trace"]
                                if s.get("action", {}).get("kind") == "interact"),
                            "accepted_interactions": trace["interactions"],
                        })
        report["tiers"][tier] = {
            "per_policy": {p: dict(c) for p, c in per_policy.items()},
            "totals": {p: dict(v) for p, v in totals.items()},
        }
    report["exemplars"] = exemplars
    return report


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Co-Presence Evidence-Gap Anatomy",
        "",
        "Why baselines fail co-presence outcomes, by tier and policy. Each cell counts",
        "failed co_presence outcomes attributed to a mechanism. `entered_no_interact`",
        "and `interact_rejected` are the pure 'legal but ineffective' modes: the agent",
        "reached the venue but never converted it into environment-accepted co-presence.",
        "",
    ]
    classes = ["no_venue_entry", "entered_no_interact", "interact_rejected",
               "window_overrun", "wrong_target", "other"]
    for tier, block in report["tiers"].items():
        lines.append(f"## {tier.capitalize()} tier")
        lines.append("")
        lines.append("| Policy | Failed/Total | " + " | ".join(classes) + " |")
        lines.append("|---|---:|" + "|".join(["---:"] * len(classes)) + "|")
        for policy in sorted(block["totals"]):
            counts = block["per_policy"].get(policy, {})
            tot = block["totals"][policy]
            cells = " | ".join(str(counts.get(c, 0)) for c in classes)
            lines.append(f"| `{policy}` | {tot['failed']}/{tot['total']} | {cells} |")
        lines.append("")
    lines.append("## Exemplar 'legal but ineffective' traces")
    lines.append("")
    for ex in report["exemplars"]:
        lines.append(
            f"- **{ex['tier']}/{ex['scenario']}** ({ex['policy']}, {ex['reason']}): "
            f"feasibility={ex['feasibility']}, messages={ex['messages']}, "
            f"entered correct venue={ex['entered_venues']}, "
            f"interact actions issued={ex['n_interact_actions']}, "
            f"accepted interactions={ex['accepted_interactions']}"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    report = analyze()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "copresence_evidence_gap.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    md = render_markdown(report)
    (OUTPUT_DIR / "copresence_evidence_gap.md").write_text(md, encoding="utf-8")
    print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
