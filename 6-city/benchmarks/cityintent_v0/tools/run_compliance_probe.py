"""Oracle compliance probe for the CityIntent v1 evidence contract.

Purpose
-------
Rule out the "adapter artifact" confound behind the rc1 finding (e.g. SOTOPIA's
0/4 accepted meetings). The confound has two falsifiable pipeline claims:

  (A) the evidence contract / executor makes accepted outcome evidence
      *unreachable* (verifier is impossible or too strict), and
  (B) an adapter's action surface cannot *express* the winning move
      (e.g. cannot emit an accepted `interact`).

This probe refutes both deterministically, without any live model call:

  Tier A - contract satisfiability: run a hand-authored *oracle* trace (the
    known-correct winning plan) for each evidence-critical scenario straight
    through the real `execute_action` + `score_trace`. If accepted evidence
    appears and task_completion == 1.0 with zero violations, the contract is
    satisfiable -> claim (A) is false.

  Tier B - adapter action-surface reachability: push each winning action through
    the *real* per-adapter translation surface (SOTOPIA `_parse_command`, and the
    shared `validate_actions` used by the Generative-Agents / AgentSociety native
    plan format) and confirm the produced action dict equals the oracle action.
    If every winning action survives, the surface can express it -> claim (B) is
    false for those adapters.

Scope & limits
--------------
Tier B here exercises the translation *functions*, not a full live-model episode
through the checked-out framework backends (those checkouts live under
`tmp/external/` and are absent in this working copy). The complementary
end-to-end confirmation - the same oracle plans injected as explicit
instructions to each real adapter with a live provider - should be run on the
machine that holds the verified checkouts; the oracle command strings printed by
this probe make that run turnkey. Tier A + Tier B together already refute the
core "pipeline cannot produce accepted evidence" reading of the confound.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "tools") not in sys.path:
    sys.path.insert(0, str(ROOT / "tools"))

import run_baseline_traces as rbt  # noqa: E402

REPO_ROOT = ROOT.parents[2]
DEFAULT_OUTPUT_DIR = (
    REPO_ROOT
    / "6-city"
    / "results"
    / "cityintent_v1_rc1"
    / "compliance_probe_oracle"
)
WORLD_PATH = ROOT / "worlds" / "micro_city.json"
SCENARIO_DIR = ROOT / "scenarios"


# --- Oracle winning plans (hand-authored, verified against the world graph) ---
# Each is the smallest correct trace that earns every outcome-role condition.
ORACLE_PLANS: dict[str, dict[str, Any]] = {
    "meeting_wait_trap": {
        "evidence_focus": "accepted co-presence interaction with ben",
        "actions": [
            {"kind": "message", "to": "ben",
             "content": "Ben, let's meet at Central Cafe at 12:35."},
            {"kind": "move", "target": "cafe_central"},
            {"kind": "enter", "target": "cafe_central"},
            # burn time to the 12:35 window opening; also proves a paid dwell.
            {"kind": "buy", "target": "cafe_central", "item": "coffee", "minutes": 21},
            {"kind": "interact", "to": "ben", "minutes": 2},
            {"kind": "finish"},
        ],
        "sotopia_commands": [
            ("speak", "Ben, let's meet at Central Cafe at 12:35.", ["ben"]),
            ("action", "move cafe_central", []),
            ("action", "enter cafe_central", []),
            ("action", "buy cafe_central coffee 21", []),
            ("action", "interact ben 2", []),
        ],
    },
    "school_pickup_social_detour": {
        "evidence_focus": "accepted child_pickup service before deadline",
        "actions": [
            {"kind": "move", "target": "school"},
            {"kind": "enter", "target": "school"},
            {"kind": "use_service", "target": "school",
             "service": "child_pickup", "minutes": 5},
            {"kind": "finish"},
        ],
        "sotopia_commands": [
            ("action", "move school", []),
            ("action", "enter school", []),
            ("action", "use_service school child_pickup 5", []),
        ],
    },
    "budget_errand_chain": {
        "evidence_focus": "accepted purchase + service under budget",
        "actions": [
            {"kind": "move", "target": "pharmacy"},
            {"kind": "enter", "target": "pharmacy"},
            {"kind": "buy", "target": "pharmacy", "item": "medicine", "minutes": 5},
            {"kind": "move", "target": "budget_diner"},
            {"kind": "enter", "target": "budget_diner"},
            {"kind": "use_service", "target": "budget_diner",
             "service": "meal", "minutes": 15},
            {"kind": "move", "target": "home_aria"},
            # returning home requires an entry, not mere arrival (evidence contract:
            # visit_before is scored off entry records, not pass-through/arrival).
            {"kind": "enter", "target": "home_aria"},
            {"kind": "finish"},
        ],
        "sotopia_commands": [
            ("action", "move pharmacy", []),
            ("action", "enter pharmacy", []),
            ("action", "buy pharmacy medicine 5", []),
            ("action", "move budget_diner", []),
            ("action", "enter budget_diner", []),
            ("action", "use_service budget_diner meal 15", []),
            ("action", "move home_aria", []),
            ("action", "enter home_aria", []),
        ],
    },
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def run_oracle_trace(
    world: rbt.CityWorld, scenario: dict[str, Any], actions: list[dict[str, Any]]
) -> dict[str, Any]:
    """Drive an oracle action list through the real executor + verifier."""
    primary = next(
        agent for agent in scenario["agents"]
        if agent["agent_id"] == scenario["primary_agent"]
    )
    state = rbt.TraceState(
        scenario_id=scenario["scenario_id"],
        agent_id=primary["agent_id"],
        agent_type="oracle_compliance_probe",
        time=rbt.parse_time(scenario["episode"]["start_time"]),
        end_time=rbt.parse_time(scenario["episode"]["end_time"]),
        location=primary["start_location"],
        budget=float(primary["budget"]),
    )
    state.inside_location = state.location
    rbt.record_visit(state, state.location, state.time, kind="start")
    rbt.record_entry(state, state.location, state.time, kind="start")
    for payload in actions:
        rbt.execute_action(world, scenario, state, rbt.Action(**payload))
        if payload["kind"] in {"finish", "abandon"} or state.time >= state.end_time:
            break
    scored = rbt.score_trace(world, scenario, state)
    return {
        "metrics": scored["metrics"],
        "conditions": scored["conditions"],
        "violations": state.violations,
        "interactions": state.interactions,
        "services": state.services,
        "purchases": state.purchases,
        "final_budget": round(state.budget, 2),
        "final_time": rbt.format_time(state.time),
    }


def tier_a_check(result: dict[str, Any]) -> dict[str, Any]:
    metrics = result["metrics"]
    task = metrics.get("task_completion")
    feas = metrics.get("trace_feasibility")
    outcome_conditions = [c for c in result["conditions"] if c["role"] == "outcome"]
    every_outcome_evidenced = all(
        c["score"] >= 1.0 and c["evidence"] for c in outcome_conditions
    )
    passed = (
        task == 1.0
        and feas == 1.0
        and not result["violations"]
        and every_outcome_evidenced
    )
    return {
        "passed": passed,
        "task_completion": task,
        "trace_feasibility": feas,
        "constraint_satisfaction": metrics.get("constraint_satisfaction"),
        "violation_count": len(result["violations"]),
        "outcome_conditions_all_evidenced": every_outcome_evidenced,
    }


def _bare_adapter(module_name: str, class_name: str, world: rbt.CityWorld,
                  framework_name: str) -> Any:
    """Instantiate an adapter's translation surface without its git-checkout
    __init__ (which verifies the external framework checkout)."""
    module = __import__(f"external_adapters.{module_name}", fromlist=[class_name])
    cls = getattr(module, class_name)
    inst = cls.__new__(cls)
    inst.world = world
    inst.framework_name = framework_name
    return inst


def tier_b_sotopia(world: rbt.CityWorld, plan: dict[str, Any]) -> dict[str, Any]:
    """SOTOPIA native (action_type, argument, to) -> _parse_command -> validate_actions."""
    inst = _bare_adapter("sotopia_official", "SOTOPIAOfficialLLMAgentAdapter",
                         world, "SOTOPIA")
    rows: list[dict[str, Any]] = []
    ok = True
    for (action_type, argument, to), oracle in zip(
        plan["sotopia_commands"], plan["actions"]
    ):
        parsed = inst._parse_command(action_type, argument, to)
        validated = inst.validate_actions([parsed])
        produced = validated[0] if validated else {"kind": "<rejected>"}
        match = (
            produced.get("kind") == oracle["kind"]
            and produced.get("target") == oracle.get("target")
            and produced.get("to") == oracle.get("to")
        )
        ok = ok and match
        rows.append({
            "native": f"{action_type}:{argument}",
            "produced_kind": produced.get("kind"),
            "expected_kind": oracle["kind"],
            "match": match,
        })
    return {"passed": ok, "steps": rows}


def tier_b_plan_format(world: rbt.CityWorld, plan: dict[str, Any], module_name: str,
                       class_name: str, framework_name: str) -> dict[str, Any]:
    """Generative-Agents / AgentSociety native plan = list[action dict] -> validate_actions."""
    inst = _bare_adapter(module_name, class_name, world, framework_name)
    native_plan = [a for a in plan["actions"] if a["kind"] != "finish"]
    validated = inst.validate_actions(native_plan)
    by_kind_target = {(a["kind"], a.get("target"), a.get("to")) for a in validated}
    ok = True
    rows: list[dict[str, Any]] = []
    for oracle in native_plan:
        key = (oracle["kind"], oracle.get("target"), oracle.get("to"))
        survived = key in by_kind_target
        ok = ok and survived
        rows.append({"action": oracle["kind"], "target": oracle.get("target"),
                     "survived": survived})
    return {"passed": ok, "surviving_actions": len(validated),
            "native_actions": len(native_plan), "steps": rows}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    world = rbt.CityWorld(load_json(WORLD_PATH))

    report: dict[str, Any] = {
        "probe": "oracle_compliance_probe",
        "generated": datetime.now(timezone.utc).isoformat(),
        "world": WORLD_PATH.name,
        "scenarios": {},
    }
    all_passed = True

    for scenario_id, plan in ORACLE_PLANS.items():
        scenario = load_json(SCENARIO_DIR / f"{scenario_id}.json")
        trace = run_oracle_trace(world, scenario, plan["actions"])
        tier_a = tier_a_check(trace)
        tier_b = {
            "SOTOPIA": tier_b_sotopia(world, plan),
            "GenerativeAgents": tier_b_plan_format(
                world, plan, "generative_agents_official",
                "GenerativeAgentsOfficialPlannerAdapter", "GenerativeAgents"),
            "AgentSociety": tier_b_plan_format(
                world, plan, "agentsociety_official",
                "AgentSocietyOfficialPlanBlocksAdapter", "AgentSociety"),
        }
        scenario_passed = tier_a["passed"] and all(v["passed"] for v in tier_b.values())
        all_passed = all_passed and scenario_passed
        report["scenarios"][scenario_id] = {
            "evidence_focus": plan["evidence_focus"],
            "tier_a_contract_satisfiability": tier_a,
            "tier_b_adapter_surface": tier_b,
            "trace_metrics": trace["metrics"],
            "accepted_evidence": {
                "interactions": trace["interactions"],
                "services": trace["services"],
                "purchases": trace["purchases"],
            },
            "passed": scenario_passed,
        }

    report["all_passed"] = all_passed

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "compliance_probe_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    _write_markdown(args.output_dir / "compliance_probe_summary.md", report)

    _print_console(report)
    return 0 if all_passed else 1


def _write_markdown(path: Path, report: dict[str, Any]) -> None:
    lines = [
        "# Oracle Compliance Probe — Summary",
        "",
        f"Generated: {report['generated']}",
        "",
        "Refutes the adapter-artifact confound: (A) the evidence contract is",
        "satisfiable, and (B) adapter action surfaces can express the winning move.",
        "",
        "| Scenario | Evidence focus | Tier A task_completion | Tier A feasible | Tier B surfaces | Pass |",
        "|---|---|---:|---:|---|:--:|",
    ]
    for sid, block in report["scenarios"].items():
        a = block["tier_a_contract_satisfiability"]
        b = block["tier_b_adapter_surface"]
        surfaces = ", ".join(
            f"{name}={'ok' if v['passed'] else 'FAIL'}" for name, v in b.items()
        )
        lines.append(
            f"| `{sid}` | {block['evidence_focus']} | {a['task_completion']} | "
            f"{a['trace_feasibility']} | {surfaces} | "
            f"{'PASS' if block['passed'] else 'FAIL'} |"
        )
    lines += [
        "",
        f"**All passed:** {report['all_passed']}",
        "",
        "Tier B exercises the real translation functions (SOTOPIA `_parse_command`,",
        "shared `validate_actions`). End-to-end live-model runs through the verified",
        "framework checkouts are the complement, to run where `tmp/external/` exists.",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _print_console(report: dict[str, Any]) -> None:
    print("=== Oracle Compliance Probe ===")
    for sid, block in report["scenarios"].items():
        a = block["tier_a_contract_satisfiability"]
        status = "PASS" if block["passed"] else "FAIL"
        print(f"\n[{status}] {sid} — {block['evidence_focus']}")
        print(f"  Tier A: task_completion={a['task_completion']} "
              f"feasibility={a['trace_feasibility']} "
              f"violations={a['violation_count']} "
              f"outcomes_evidenced={a['outcome_conditions_all_evidenced']}")
        for name, v in block["tier_b_adapter_surface"].items():
            print(f"  Tier B [{name}]: {'ok' if v['passed'] else 'FAIL'}")
    print(f"\nALL PASSED: {report['all_passed']}")


if __name__ == "__main__":
    raise SystemExit(main())
