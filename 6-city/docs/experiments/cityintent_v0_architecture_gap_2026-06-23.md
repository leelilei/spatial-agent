# CityIntent v0 Architecture Gap Experiment

Date: 2026-06-23

Purpose:

> Step 4 for the CityAgency push: run the first 8-scenario architecture table
> after adding plausibility-feasibility gap metrics and two API-backed agent
> architectures.

## Run

Command:

```bash
python 6-city/benchmarks/cityintent_v0/tools/run_baseline_traces.py ^
  --agents utility_planner,api_llm_direct_actor,api_llm_plan_then_act,api_llm_reactive_replanner ^
  --llm-config 6-city/benchmarks/cityintent_v0/configs/fhl_gpt54mini.json ^
  --results-dir 6-city/results/cityintent_v0/api_architecture_gap_gpt54mini
```

Output directory:

- `6-city/results/cityintent_v0/api_architecture_gap_gpt54mini/`

Artifacts:

- `summary.md`
- `summary.csv`
- `aggregate.json`
- `traces.json`
- `traces.jsonl`

## Agents

| Agent | Type | Description |
|---|---|---|
| `utility_planner` | deterministic | Rule-based baseline using known success conditions and shortest feasible paths. |
| `api_llm_direct_actor` | real API | SOTOPIA-like next-action policy. |
| `api_llm_plan_then_act` | real API | Generates an initial full-episode plan, then executes it without replanning. |
| `api_llm_reactive_replanner` | real API | Reassesses unfinished goals, visible events, violations, and constraints every step. |

## Aggregate Result

| Agent | Plan plausibility | Trace feasibility | Gap | Impossible trace | False continue | Goal completion | Main reading |
|---|---:|---:|---:|---:|---:|---:|---|
| `utility_planner` | 1.000 | 0.875 | 0.125 | 0.125 | 0.000 | 0.906 | Feasible on most tasks, but brittle under commute disruption. |
| `api_llm_direct_actor` | 1.000 | 0.920 | 0.080 | 0.080 | 0.125 | 0.912 | Plausible local actions, but shows loops, budget failure, social derailment, and goal drift. |
| `api_llm_plan_then_act` | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.944 | Initial planning improves trace feasibility in this run, but misses part of lunch-meeting goal. |
| `api_llm_reactive_replanner` | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | Best current architecture in this single run; validates the value of explicit replanning state. |

## Failure Taxonomy Rows

| Scenario | Agent | Failure taxonomy | Interpretation |
|---|---|---|---|
| `avoid_crowd_event` | `api_llm_direct_actor` | `done_state_loop`, `money_budget_failure` | Direct actor over-executes plausible errands and exhausts budget. |
| `budget_errand_chain` | `api_llm_direct_actor` | `done_state_loop` | Direct actor completes the chain but repeats a destination/action pattern. |
| `commute_disruption` | `utility_planner` | `impossible_route` | Rule baseline follows a brittle shortest path through a disruption. |
| `unexpected_friend_encounter` | `api_llm_direct_actor` | `goal_drift`, `social_derailment` | Direct actor handles the salient social interaction but fails to recover the private task. |

## Preliminary Claim

This run supports the CityAgency story:

> Direct LLM action can look locally plausible, but architecture matters for
> converting plausible plans into executable city traces.

The direct actor is not simply weaker across all metrics; it often completes
goals. The diagnostic value is in the failure type: its failures are exactly the
urban-agency failures CityAgency wants to measure, including done-state loops,
budget overrun, social derailment, and goal drift.

The current `api_llm_reactive_replanner` result is strong. That is useful, not a
problem: it suggests the benchmark can distinguish architectures and that
explicit unfinished-condition state may reduce impossible traces.

## Caveats

1. `plan_plausibility` is still a deterministic proxy based on action validity
   and stated reasons. It is not yet an independent LLM/human plausibility judge.
2. This is one run per scenario. The next robust version should add repeated
   seeds or repeated API calls and report reliability.
3. The v0 scenario set is small. The next scenario expansion should add harder
   infeasible-city cases where all architectures face stronger pressure.
4. `api_llm_reactive_replanner` receives explicit unfinished-condition state,
   so its advantage should be described as an architectural affordance, not as a
   pure model capability.

## Next Step

The next most important implementation step is a lightweight plausibility judge:

```text
trace/rationale -> plausible urban plan score
```

Then the core paper table can separate:

- plan plausibility
- executable trace feasibility
- gap rate
- impossible trace taxonomy
- architecture-level mitigation

