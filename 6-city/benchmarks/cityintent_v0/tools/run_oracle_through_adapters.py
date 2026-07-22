"""E4 — drive an oracle decision end-to-end through each REAL framework adapter.

The compliance probe (2026-07-06) showed the evidence contract is satisfiable and
that each adapter's *translation surface* can express the winning move, but it
stopped short of running a full episode through the real adapters: the pinned
framework checkouts were not on that machine.

They are now, so this closes the gap. Each adapter is instantiated for real
(including `verify_official_checkout` against the pinned commit + file hashes),
and only its LLM call is replaced by a deterministic replay that emits the oracle
plan **in that framework's own native output format**. Everything downstream —
the framework's own parsing, queueing, replanning triggers, evidence synthesis,
the typed executor and the evidence-contract verifier — runs for real.

If every adapter then earns environment-accepted evidence, the "the adapter
pipeline cannot produce accepted evidence" reading of the rc1 / social-family
results is refuted end-to-end, not just at the function level.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
for extra in (ROOT, ROOT / "tools"):
    if str(extra) not in sys.path:
        sys.path.insert(0, str(extra))

import run_baseline_traces as rbt  # noqa: E402
from run_compliance_probe import ORACLE_PLANS, SCENARIO_DIR, WORLD_PATH, load_json  # noqa: E402

REPO_ROOT = ROOT.parents[2]
DEFAULT_OUTPUT_DIR = (
    REPO_ROOT / "6-city" / "results" / "cityintent_v1_rc1" / "oracle_through_adapters_2026-07-10"
)
LLM_CONFIG = ROOT / "configs" / "fhl_gpt54mini.json"

ADAPTERS = {
    "gatsim": ("gatsim_official", "GATSimOfficialPlannerAdapter"),
    "sotopia": ("sotopia_official", "SOTOPIAOfficialLLMAgentAdapter"),
    "generative_agents": ("generative_agents_official", "GenerativeAgentsOfficialPlannerAdapter"),
    "agentsociety": ("agentsociety_official", "AgentSocietyOfficialPlanBlocksAdapter"),
}


def build_adapter(name: str, world, scenario, primary, plan: dict[str, Any]):
    """Patch the LLM call on the CLASS before constructing.

    Generative Agents and AgentSociety generate their initial plan inside
    `__init__`, so an instance-level patch would arrive too late and the real
    provider would be hit.
    """
    module_name, class_name = ADAPTERS[name]
    module = __import__(f"external_adapters.{module_name}", fromlist=[class_name])
    cls = getattr(module, class_name)
    attr, responder = oracle_responder(name, plan)
    sentinel = object()
    original = cls.__dict__.get(attr, sentinel)
    setattr(cls, attr, lambda self, system, prompt: responder(system, prompt))
    try:
        adapter = cls(world, scenario, primary, llm_config=LLM_CONFIG)
    finally:
        if original is sentinel:
            delattr(cls, attr)
        else:
            setattr(cls, attr, original)
    # keep the SAME closure (and its call counter) alive for the episode
    setattr(adapter, attr, responder)
    return adapter


def oracle_responder(name: str, plan: dict[str, Any]):
    """Return (method_name, responder) emitting the oracle in native format."""
    actions = [a for a in plan["actions"] if a["kind"] != "finish"]
    state = {"calls": 0}

    if name == "sotopia":
        # per-turn: one native AgentAction per call
        cmds = list(plan["sotopia_commands"])

        def complete_json(system, prompt):
            i = state["calls"]
            state["calls"] += 1
            if i >= len(cmds):
                return {"action_type": "none", "argument": "finish", "to": []}
            action_type, argument, to = cmds[i]
            return {"action_type": action_type, "argument": argument, "to": to}

        return "complete_json", complete_json

    elif name == "generative_agents":
        # native: {"plan": [action dicts]}; later calls must not reset the queue
        def complete_json(system, prompt):
            state["calls"] += 1
            if state["calls"] == 1:
                return {"plan": actions, "reflection": "oracle replay"}
            return {"plan": [], "insights": []}

        return "complete_json", complete_json

    elif name == "agentsociety":
        # native: guidance call, then {"plan": {"steps": [{"action": {...}}]}}
        def complete_json(system, prompt):
            state["calls"] += 1
            if "guidance" in system:
                return {"intention": "oracle replay"}
            if state["calls"] <= 2:
                return {"plan": {"steps": [
                    {"type": "action", "intention": "oracle replay", "action": a}
                    for a in actions
                ]}}
            return {"plan": {"steps": []}}

        return "complete_json", complete_json

    elif name == "gatsim":
        # native: {"plan": [[target, act, start, dur, path, note] ...]}
        targets: list[str] = []
        for a in actions:
            t = a.get("target")
            if a["kind"] == "move" and t and (not targets or targets[-1] != t):
                targets.append(t)
        activities = [[t, "oracle", "00:00", "0", "shortest", "oracle replay"] for t in targets]

        def _complete_json(system, prompt):
            state["calls"] += 1
            if state["calls"] == 1:
                return {"plan": activities}
            return {"plan": []}

        return "_complete_json", _complete_json

    else:
        raise ValueError(name)


def run_one(name: str, scenario_id: str, plan: dict[str, Any]) -> dict[str, Any]:
    world = rbt.CityWorld(load_json(WORLD_PATH))
    scenario = load_json(SCENARIO_DIR / f"{scenario_id}.json")
    primary = next(a for a in scenario["agents"] if a["agent_id"] == scenario["primary_agent"])

    adapter = build_adapter(name, world, scenario, primary, plan)
    provenance = dict(adapter.model_info)

    state = rbt.TraceState(
        scenario_id=scenario_id, agent_id=primary["agent_id"], agent_type=f"oracle_{name}",
        time=rbt.parse_time(scenario["episode"]["start_time"]),
        end_time=rbt.parse_time(scenario["episode"]["end_time"]),
        location=primary["start_location"], budget=float(primary["budget"]),
    )
    state.inside_location = state.location
    rbt.record_visit(state, state.location, state.time, kind="start")
    rbt.record_entry(state, state.location, state.time, kind="start")

    for _ in range(int(scenario["episode"]["max_steps"]) * 3):
        value = adapter.next_action(state)
        action = rbt.Action(**{k: v for k, v in value.items() if k != "raw_response"})
        rbt.execute_action(world, scenario, state, action)
        if action.kind in {"finish", "abandon"} or state.time >= state.end_time:
            break

    scored = rbt.score_trace(world, scenario, state)
    outcomes = [c for c in scored["conditions"] if c["role"] == "outcome"]
    evidenced = [c for c in outcomes if c["score"] >= 1.0 and c["evidence"]]
    return {
        "adapter": name,
        "scenario": scenario_id,
        "source_commit": provenance.get("source_commit", "")[:10],
        "integration_level": provenance.get("integration_level", ""),
        "task_completion": scored["metrics"].get("task_completion"),
        "trace_feasibility": scored["metrics"].get("trace_feasibility"),
        "outcomes_evidenced": f"{len(evidenced)}/{len(outcomes)}",
        "any_accepted_evidence": bool(state.entries[1:] or state.services or state.purchases or state.interactions),
        "accepted": {
            "entries": [e["location"] for e in state.entries if e.get("kind") != "start"],
            "services": [f"{s['location']}:{s['service']}" for s in state.services],
            "purchases": [f"{p['location']}:{p['item']}" for p in state.purchases],
            "interactions": [f"{i['with']}@{i['location']}" for i in state.interactions],
        },
        "violations": len(state.violations),
        "passed": len(evidenced) == len(outcomes) and len(outcomes) > 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()
    os.environ.setdefault("FHL_API_KEY", "offline-oracle-replay")

    rows: list[dict[str, Any]] = []
    for scenario_id, plan in ORACLE_PLANS.items():
        for name in ADAPTERS:
            try:
                rows.append(run_one(name, scenario_id, plan))
            except Exception as exc:  # keep going; a failure is itself a result
                rows.append({"adapter": name, "scenario": scenario_id,
                             "passed": False, "error": f"{type(exc).__name__}: {exc}"})

    all_passed = all(r.get("passed") for r in rows)
    report = {
        "probe": "oracle_through_real_adapters",
        "generated": datetime.now(timezone.utc).isoformat(),
        "all_passed": all_passed,
        "rows": rows,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "oracle_through_adapters.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print("=== Oracle through REAL adapters (E4) ===")
    hdr = f"{'adapter':20} {'scenario':28} {'task':>5} {'feas':>5} {'outcomes':>9} {'viol':>4}  accepted"
    print(hdr); print("-" * len(hdr))
    for r in rows:
        if "error" in r:
            print(f"{r['adapter']:20} {r['scenario']:28} ERROR: {r['error'][:60]}")
            continue
        acc = ",".join(filter(None, [
            "entry:" + "/".join(r["accepted"]["entries"]) if r["accepted"]["entries"] else "",
            "svc:" + "/".join(r["accepted"]["services"]) if r["accepted"]["services"] else "",
            "buy:" + "/".join(r["accepted"]["purchases"]) if r["accepted"]["purchases"] else "",
            "meet:" + "/".join(r["accepted"]["interactions"]) if r["accepted"]["interactions"] else "",
        ]))
        print(f"{r['adapter']:20} {r['scenario']:28} {r['task_completion']!s:>5} "
              f"{r['trace_feasibility']!s:>5} {r['outcomes_evidenced']:>9} {r['violations']:>4}  {acc[:60]}")
    print(f"\nALL PASSED: {all_passed}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
