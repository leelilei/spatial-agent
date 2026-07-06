# CityIntent v1-rc1 Oracle Compliance Probe

Date: 2026-07-06

## Question

Is the rc1 finding (task_completion << legacy goal; SOTOPIA 0/4 accepted
meetings) an **adapter artifact** — i.e. does the evidence contract / executor
make accepted outcome evidence unreachable, or can an adapter's action surface
simply not express the winning move? This is the largest threat to Claim A, since
without ruling it out a reviewer reduces the gap to "your verifier is just too
strict / your pipeline is broken."

## Design

Two deterministic tiers, no live model call
(`benchmarks/cityintent_v0/tools/run_compliance_probe.py`):

- **Tier A — contract satisfiability.** For each evidence-critical scenario, run a
  hand-authored *oracle* trace (the smallest correct winning plan) straight
  through the real `execute_action` + `score_trace`. Pass iff
  `task_completion == 1.0`, `trace_feasibility == 1.0`, zero violations, and every
  outcome-role condition carries accepted evidence.
- **Tier B — adapter action-surface reachability.** Push each winning action
  through the *real* per-adapter translation surface: SOTOPIA's `_parse_command`
  (native `action_type/argument` → action dict) and the shared `validate_actions`
  that consumes the Generative-Agents / AgentSociety native plan format. Pass iff
  the produced action dict equals the oracle action.

Scenarios: `meeting_wait_trap` (accepted co-presence interaction),
`school_pickup_social_detour` (accepted `child_pickup` service before deadline),
`budget_errand_chain` (accepted purchase + service under budget).

## Result — ALL PASS

| Scenario | Tier A task_completion | Feasible | Accepted evidence | Tier B surfaces |
|---|---:|---:|---|---|
| `meeting_wait_trap` | 1.0 | 1.0 | interaction with ben @12:35, cafe_central | SOTOPIA / GA / AgentSociety all ok |
| `school_pickup_social_detour` | 1.0 | 1.0 | child_pickup service @17:32 (< 18:10) | all ok |
| `budget_errand_chain` | 1.0 | 1.0 | medicine purchase + meal service, budget 3 | all ok |

Archived: `results/cityintent_v1_rc1/compliance_probe_oracle/`
(`compliance_probe_report.json`, `compliance_probe_summary.md`).
Guarded by `tests/test_compliance_probe.py` (2 passing).

## Interpretation

- **The contract is satisfiable.** A correct trace earns full task_completion with
  accepted, environment-owned evidence for interaction, service, and purchase
  outcomes. The rc1 low scores are therefore **not** an impossible/over-strict
  verifier.
- **The adapter action surfaces can express the winning move.** SOTOPIA's own
  parser turns `interact ben 2` into an accepted interaction; GA/AgentSociety
  native plans survive validation. So SOTOPIA's 0/4 meetings are **not** a
  translation-surface limitation.
- Net: the plausible↔verified gap is a **decision-quality** signal, not a pipeline
  artifact — the strongest form of the "adapter artifact" confound is refuted.

## Incidental finding (contract self-consistency)

The first oracle for `budget_errand_chain` scored 0.733: `return_home`
(`visit_before`) is scored off **entry** records, so arriving at home without an
`enter` does not count. This is consistent with the contract's "arrival ≠ entry"
rule; adding the `enter home_aria` step fixed it to 1.0. A small confirmation that
the contract applies uniformly even to plain "visit/return" outcomes.

## Scope & limits (complement to run on the checkout machine)

Tier B exercises the translation *functions*, not a full live-model episode
through the checked-out framework backends (`tmp/external/` is absent in this
working copy). The complementary confirmation — the same oracle plans injected as
explicit instructions to each real adapter with a live provider, showing each
end-to-end pipeline yields accepted evidence — should run where the verified
checkouts exist. GATSim's evidence-action synthesizer (activity-list native
format) is not covered by Tier B here and belongs to that end-to-end pass. The
oracle command strings in `run_compliance_probe.py` make that run turnkey.
