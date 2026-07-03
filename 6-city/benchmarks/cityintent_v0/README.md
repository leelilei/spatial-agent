# CityIntent v1.0 Release Candidate

Status: `1.0-rc1`, locally validated and awaiting two-person blinded human audit.

This package is the first runnable CityAgency track. It keeps the `CityIntent`
name because v0 focuses on intention persistence and constraint-sensitive
action. It is not yet a full experiment runner. Its job is to verify that our
proposed benchmark object is concrete enough to support agent comparisons.

## What This Tests

CityIntent includes four offline architecture probes, three generic
API-backed policies, and four verified external-framework adapters:

| Agent id | Architecture | Purpose |
|---|---|---|
| `utility_planner` | `UtilityPlannerAgent` | Deterministic non-LLM baseline using time, distance, cost, needs, and relationships |
| `llm_direct_actor` | `LLMDirectActor` | SOTOPIA-like direct next-action policy |
| `reactive_replanner` | `ReactiveReplannerAgent` | Observe each step and replan after disruption |
| `memory_reflection` | `MemoryReflectionAgent` | Generative-agent-style memory, reflection, and planning |
| `api_llm_direct_actor` | `APILLMDirectActor` | Real provider-backed direct next-action policy |
| `api_llm_plan_then_act` | `APILLMPlanThenAct` | Real provider-backed initial-plan-then-execute policy |
| `api_llm_reactive_replanner` | `APILLMReactiveReplanner` | Real provider-backed observe-update-act replanner |
| `gatsim_official_planner` | `GATSimOfficialPlannerAdapter` | Pinned official GATSim planning code/templates adapted to the CityIntent world |
| `sotopia_official_llm_agent` | `SOTOPIAOfficialLLMAgentAdapter` | Pinned official SOTOPIA per-turn private-goal action policy |
| `generative_agents_official_planner` | `GenerativeAgentsOfficialPlannerAdapter` | Pinned official Smallville daily planning, reflection, and revision prompts |
| `agentsociety_official_plan_blocks` | `AgentSocietyOfficialPlanBlocksAdapter` | Pinned official AgentSociety TPB guidance, detailed-plan, and place-analysis blocks |

The benchmark deliberately does **not** start by evaluating SimCity or CitySim
as full systems. CitySim-style agents can become a later adapter. The first
scientific question is whether different agent architectures behave differently
in the same verifiable city environment.

The four external adapters pin and verify official repositories, commits, and
key source-file hashes. They execute or extract the official decision prompts
and preserve each framework's characteristic control structure. CityIntent
still owns the micro-city world and typed action executor, so all four are
labelled `adapted_official_*`, not native full-backend results. CitySim is not
listed as an official adapter because its paper does not currently provide an
official public implementation that can be pinned and executed.

## Scenario Set

CityIntent currently has 12 scenarios:

- 8 original seed scenarios covering budget, disruption, memory, POI closure,
  preference, social-spatial tradeoff, opportunistic social interaction, and
  time pressure.
- 4 targeted pressure scenarios:
  - `detour_commute_midroute_block`
  - `closed_study_spot_replacement`
  - `school_pickup_social_detour`
  - `meeting_wait_trap`

The pressure scenarios are intentionally diagnostic. They stress cases where an
action can sound locally plausible while the full city trace becomes
unbelievable or deterministically invalid.

## Action-Evidence Protocol

Version 0.2 separates physical arrival from task completion:

- `move` changes the outdoor graph location only. Passing through or arriving
  creates no entry, purchase, service, or goal-completion evidence.
- `enter` checks opening constraints and creates explicit entry evidence.
- `buy` and `use_service` require entry, deduct the POI cost, and create typed
  completion evidence such as `groceries`, `medicine`, or `meal`.
- `dwell` requires entry and, at paid locations, prior purchase or service
  evidence.
- `finish` and `abandon` are distinct terminal actions.

Each success-condition row in `traces.json` includes the exact evidence used by
the deterministic verifier. This prevents a plausible plan or a route passing
through a POI from being scored as a completed urban activity.

Version 0.3 adds interruptible movement. If a road or transit block becomes
visible after a multi-edge move begins, execution stops at the last reachable
node and records `route_interruptions` without blaming the agent. A subsequent
move counts as a verified replan only when its chosen path avoids an active
blocked edge that the normal shortest path would have used. Re-attempting an
already visible blocked edge remains a feasibility violation.

Version 1.0-rc1 adds environment-owned social and activity evidence:

- `interact` is accepted only after entry and when the named counterpart is
  observable at that location and time.
- `co_presence` requires an accepted interaction record; presence at a venue is
  not enough.
- school pickup requires a completed `child_pickup` service before the deadline;
  arrival at school is not pickup.
- success conditions have `outcome`, `process`, or `constraint` roles.
  `task_completion` uses outcomes only, so budget or avoidance points cannot
  substitute for a missing intended result.

`goal_completion` remains as the legacy weighted aggregate for comparison.
The v1 primary completion metric is `task_completion`.

## Contents

```text
benchmark_config.json        # benchmark-level metrics and agent architecture list
schema/scenario.schema.json  # JSON schema for scenario packages
worlds/micro_city.json       # graph city with POIs, opening hours, prices, and edges
scenarios/*.json             # twelve seed and pressure scenarios
tools/validate_cityintent_v0.py
tools/run_baseline_traces.py
tests/test_action_protocol_v02.py
tools/judge_trace_plausibility.py
tools/run_repeated_experiment.py
tools/build_human_audit.py
tools/score_human_audit.py
tools/setup_external_framework.py
tools/validate_external_adapters.py
tests/test_human_audit_tools.py
configs/fhl_gpt54mini.json
external_adapters/*_manifest.json
external_adapters/*_official.py
```

## Verification

Run from the repository root:

```bash
python 6-city/benchmarks/cityintent_v0/tools/validate_cityintent_v0.py
```

The validator checks:

- world graph connectivity
- location and agent references
- episode time windows
- metric coverage
- scenario coverage
- architecture probes for the four first-test agents
- graph reachability from the primary agent to critical POIs

## Baseline Smoke Run

Run deterministic first-pass baselines from the repository root:

```bash
python 6-city/benchmarks/cityintent_v0/tools/run_baseline_traces.py
```

Default outputs are written to:

```text
6-city/results/cityintent_v1_rc1_offline_2026-07-02/
```

The current offline runner supports:

- `utility_planner`
- `llm_direct_actor`
- `reactive_replanner`
- `memory_reflection`
- `api_llm_direct_actor` for a real configured provider
- `api_llm_plan_then_act` for a real configured provider
- `api_llm_reactive_replanner` for a real configured provider
- the four verified external adapters after setting up their pinned checkouts

## External Framework Adapters

Create the four pinned sparse checkouts. These fetch only the official source
surfaces required by each adapter, not the complete frontends, datasets, map
tiles, Redis/Ray services, or archived simulations:

```bash
python 6-city/benchmarks/cityintent_v0/tools/setup_external_framework.py --framework gatsim
python 6-city/benchmarks/cityintent_v0/tools/setup_external_framework.py --framework sotopia
python 6-city/benchmarks/cityintent_v0/tools/setup_external_framework.py --framework generative-agents
python 6-city/benchmarks/cityintent_v0/tools/setup_external_framework.py --framework agentsociety
```

Verify all source remotes, commits, required-file hashes, benchmark-config
links, and official prompt surfaces:

```bash
python 6-city/benchmarks/cityintent_v0/tools/validate_external_adapters.py
```

Run the four real provider-backed adapters on the same scenarios:

```bash
python 6-city/benchmarks/cityintent_v0/tools/run_baseline_traces.py ^
  --agents gatsim_official_planner,sotopia_official_llm_agent,generative_agents_official_planner,agentsociety_official_plan_blocks ^
  --scenario-ids budget_errand_chain,closed_poi_replacement ^
  --llm-config 6-city/benchmarks/cityintent_v0/configs/fhl_gpt54mini.json ^
  --results-dir 6-city/results/cityintent_v0/external_frameworks_4way_gpt54mini
```

The trace `model_info` records `framework`, `source_repo`, `source_commit`,
`source_verified`, `integration_level`, `native_backend`, and the actual LLM.
GATSim's explicit activity-plan paths are preserved; SOTOPIA keeps its
per-turn `AgentAction`; Generative Agents keeps daily planning, reflection, and
schedule revision; AgentSociety keeps TPB guidance, typed plan steps, and place
analysis.

Provider-backed runs also archive per-call latency, retries, prompt hashes, and
provider token usage (or a labelled character estimate). Totals are written to
`telemetry_aggregate.json` and the telemetry columns in `summary.csv`.
Every run writes a sanitized `run_manifest.json`. Existing archives are not
overwritten unless `--overwrite` is passed explicitly.

Important: `llm_direct_actor`, `reactive_replanner`, and `memory_reflection`
remain offline architecture proxies and should not be reported as real LLM
results. The `api_llm_*` policies and all four `*_official_*` adapters call the
configured model provider; only the latter are verified external-framework
decision-layer integrations.

Small API smoke run:

```bash
python 6-city/benchmarks/cityintent_v0/tools/run_baseline_traces.py ^
  --agents utility_planner,api_llm_direct_actor ^
  --scenario-ids closed_poi_replacement,memory_dependent_place_choice ^
  --llm-config 6-city/benchmarks/cityintent_v0/configs/fhl_gpt54mini.json ^
  --results-dir 6-city/results/cityintent_v0/api_smoke_gpt54mini
```

Full API architecture run:

```bash
python 6-city/benchmarks/cityintent_v0/tools/run_baseline_traces.py ^
  --agents utility_planner,api_llm_direct_actor,api_llm_plan_then_act,api_llm_reactive_replanner ^
  --llm-config 6-city/benchmarks/cityintent_v0/configs/fhl_gpt54mini.json ^
  --results-dir 6-city/results/cityintent_v0/api_architecture_gap_gpt54mini
```

## Second-Pass Plausibility Judge

After generating traces, run the independent LLM judge to separate face-valid
urban plans from believable full trajectories:

```bash
python 6-city/benchmarks/cityintent_v0/tools/judge_trace_plausibility.py ^
  --llm-config 6-city/benchmarks/cityintent_v0/configs/fhl_gpt54mini.json ^
  --input 6-city/results/cityintent_v0/api_architecture_gap_gpt54mini/traces.json ^
  --output-dir 6-city/results/cityintent_v0/api_architecture_gap_gpt54mini_judged_v2
```

The judge reports:

- `judge_face_plausibility`: whether the actions and reasons sound like a
  reasonable city plan at demo/face-validity level
- `trace_feasibility`: deterministic environment feasibility from the runner
- `judge_trace_believability`: whether the complete sequence still looks like
  believable city behavior
- `face_feasibility_gap`: surface plausibility minus deterministic feasibility
- `face_believability_gap`: surface plausibility minus full-trace believability

The script writes checkpointed outputs after each judged trace and resumes from
`judged_traces.json` by default.

## Repeated Reliability Table

Run repeated API experiments and build an agent-level mean/std table:

```bash
python 6-city/benchmarks/cityintent_v0/tools/run_repeated_experiment.py ^
  --repeats 3 ^
  --agents utility_planner,api_llm_direct_actor,api_llm_plan_then_act,api_llm_reactive_replanner ^
  --llm-config 6-city/benchmarks/cityintent_v0/configs/fhl_gpt54mini.json ^
  --output-dir 6-city/results/cityintent_v0/api_repeated_reliability_gpt54mini ^
  --skip-existing
```

For deterministic protocol repeats without the second-pass LLM judge, add
`--skip-judge`. The repeated table still includes calls, token use, latency,
route interruptions, and verified replans.

The repeated runner creates:

- `repeated_summary.md`: paper-style main table
- `all_runs.csv`: repeat/scenario/agent rows
- `agent_repeated_summary.csv`: agent-level means and sample standard deviations
- `scenario_agent_repeated_summary.csv`: scenario-agent diagnostics
- `failure_taxonomy_summary.csv`: failure counts and events per trace

The first v0.3 real-model matrix is archived at
`6-city/results/cityintent_v03/external_frameworks_4x4x3_gpt54mini_2026-07-01/`.
It contains 48 traces: four diagnostic scenarios, four verified official
decision-layer adapters, and three repeats. The accompanying interpretation is
in `6-city/docs/experiments/cityintent_v03_interruptible_movement_4x4x3_2026-07-01.md`.

## Blinded Human Audit

The v0.3 balanced 16-trace rubric-debugging pilot is archived at
`6-city/annotation/cityintent_v03_blind_pilot_2026-07-01/`. One seeded repeat is
sampled from each scenario-adapter cell. Annotators receive only the rubric,
world reference, blinded packet, and their own blank CSV. Framework identity,
repeat id, metrics, violations, failure taxonomy, and verified replans remain in
the separate sealed key.

Model dry-runs under `dry_run/` are rubric debugging only and are not human
validation. After two independent human annotation files are locked, run
`tools/score_human_audit.py` to report exact agreement, Cohen's kappa, and
calibration against deterministic completion, feasibility, and replanning.

## Freeze Gate

CityIntent v1 is not frozen yet. Freeze requires:

- a v1 trace sample from the verified external-framework adapters;
- two independent human annotations completed without sealed-key access;
- pre-adjudication agreement and verifier-calibration reports;
- documented resolution of material disagreements, followed by a final
  regression run and immutable v1 manifest.

Prepare two handoff ZIPs without the sealed key or the other annotator's file:

```powershell
python tools/prepare_human_audit_handoff.py
```

After both independent CSVs are returned, score the audit and create the material
finding disposition template:

```powershell
python tools/score_human_audit.py `
  --annotations-a ../../annotation/cityintent_v1_rc1_blind_validation_2026-07-02/annotations/annotator_a.csv `
  --annotations-b ../../annotation/cityintent_v1_rc1_blind_validation_2026-07-02/annotations/annotator_b.csv `
  --key ../../annotation/cityintent_v1_rc1_blind_validation_2026-07-02/sealed/audit_key.csv `
  --output-dir ../../annotation/cityintent_v1_rc1_blind_validation_2026-07-02/agreement
```

Run the complete release gate from the repository root:

```powershell
python 6-city/benchmarks/cityintent_v0/tools/check_v1_release.py
```

Only after the report says `ready_to_freeze` may the same command be rerun with
`--freeze`. The command then changes the benchmark to `1.0`, sets status to
`frozen`, and writes an immutable artifact-hash manifest under
`6-city/releases/cityintent_v1/`.
