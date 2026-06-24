# CityIntent v0 Benchmark Smoke Test

Status: draft, locally validated.

This package is the first runnable CityAgency track. It keeps the `CityIntent`
name because v0 focuses on intention persistence and constraint-sensitive
action. It is not yet a full experiment runner. Its job is to verify that our
proposed benchmark object is concrete enough to support agent comparisons.

## What This Tests

CityIntent v0 starts with four offline architecture probes and three API-backed
LLM policies:

| Agent id | Architecture | Purpose |
|---|---|---|
| `utility_planner` | `UtilityPlannerAgent` | Deterministic non-LLM baseline using time, distance, cost, needs, and relationships |
| `llm_direct_actor` | `LLMDirectActor` | SOTOPIA-like direct next-action policy |
| `reactive_replanner` | `ReactiveReplannerAgent` | Observe each step and replan after disruption |
| `memory_reflection` | `MemoryReflectionAgent` | Generative-agent-style memory, reflection, and planning |
| `api_llm_direct_actor` | `APILLMDirectActor` | Real provider-backed direct next-action policy |
| `api_llm_plan_then_act` | `APILLMPlanThenAct` | Real provider-backed initial-plan-then-execute policy |
| `api_llm_reactive_replanner` | `APILLMReactiveReplanner` | Real provider-backed observe-update-act replanner |

The benchmark deliberately does **not** start by evaluating SimCity or CitySim
as full systems. CitySim-style agents can become a later adapter. The first
scientific question is whether different agent architectures behave differently
in the same verifiable city environment.

## Scenario Set

CityIntent v0 currently has 12 scenarios:

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

## Contents

```text
benchmark_config.json        # benchmark-level metrics and agent architecture list
schema/scenario.schema.json  # JSON schema for scenario packages
worlds/micro_city.json       # graph city with POIs, opening hours, prices, and edges
scenarios/*.json             # twelve seed and pressure scenarios
tools/validate_cityintent_v0.py
tools/run_baseline_traces.py
tools/judge_trace_plausibility.py
tools/run_repeated_experiment.py
configs/fhl_gpt54mini.json
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
6-city/results/cityintent_v0/baseline_smoke/
```

The current offline runner supports:

- `utility_planner`
- `llm_direct_actor`
- `reactive_replanner`
- `memory_reflection`
- `api_llm_direct_actor` for a real configured provider
- `api_llm_plan_then_act` for a real configured provider
- `api_llm_reactive_replanner` for a real configured provider

Important: the current LLM-named agents are offline architecture proxies. They
do not call external models and should not be reported as real LLM results.
Only `api_llm_*` agents call a model provider.

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

The repeated runner creates:

- `repeated_summary.md`: paper-style main table
- `all_runs.csv`: repeat/scenario/agent rows
- `agent_repeated_summary.csv`: agent-level means and sample standard deviations
- `scenario_agent_repeated_summary.csv`: scenario-agent diagnostics
- `failure_taxonomy_summary.csv`: failure counts and rates

## Next Implementation Step

The next code step is to make the experiment less anecdotal:

- expand the scenario suite with harder impossible-trace traps;
- calibrate the LLM judge against a small human-coded audit set;
- keep all agents behind the same typed action and scoring contract.
