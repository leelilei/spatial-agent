# CityIntent v0 Plausibility Judge Experiment

Date: 2026-06-23

Purpose:

> Test the CityAgency paper story with a second-pass LLM judge: agents may
> produce actions that look reasonable at face value, while the complete city
> trace becomes unbelievable or impossible.

This experiment follows the first API architecture run:

- traces: `6-city/results/cityintent_v0/api_architecture_gap_gpt54mini/traces.json`
- judged output: `6-city/results/cityintent_v0/api_architecture_gap_gpt54mini_judged_v2/`

## Run

Command:

```bash
python 6-city/benchmarks/cityintent_v0/tools/judge_trace_plausibility.py ^
  --llm-config 6-city/benchmarks/cityintent_v0/configs/fhl_gpt54mini.json ^
  --input 6-city/results/cityintent_v0/api_architecture_gap_gpt54mini/traces.json ^
  --output-dir 6-city/results/cityintent_v0/api_architecture_gap_gpt54mini_judged_v2
```

The judge asks for two separate plausibility judgments:

- `judge_face_plausibility`: whether the actions and reasons sound like a
  reasonable city plan at face-validity/demo level.
- `judge_trace_believability`: whether the complete action sequence still looks
  like believable urban behavior after loops, omissions, odd timing, or drift.

The deterministic runner still supplies:

- `trace_feasibility`: whether the trace remains executable under world rules.
- `goal_completion`: how much of the scenario objective was satisfied.

## Aggregate Result

| Agent | Face plausibility | Trace feasibility | Face-feasibility gap | Trace believability | Face-believability gap | Goal completion | Reading |
|---|---:|---:|---:|---:|---:|---:|---|
| `utility_planner` | 0.772 | 0.875 | 0.083 | 0.530 | 0.244 | 0.906 | Deterministic actions can be valid but behavior may end too early or ignore social texture. |
| `api_llm_direct_actor` | 0.859 | 0.920 | 0.000 | 0.547 | 0.311 | 0.912 | Strong face validity, weakest full-trace believability among API agents. |
| `api_llm_plan_then_act` | 0.926 | 1.000 | 0.000 | 0.815 | 0.111 | 0.944 | Best balance in this judge run; planning reduces local drift. |
| `api_llm_reactive_replanner` | 0.923 | 1.000 | 0.000 | 0.789 | 0.134 | 1.000 | Best deterministic success, but still loses believability in waiting/unfinished-task cases. |

## Largest Face-Believability Gaps

| Scenario | Agent | Face | Believability | Deterministic feasibility | Gap | Main issue |
|---|---:|---:|---:|---:|---:|---|
| `lunch_meeting_time_pressure` | `utility_planner` | 0.72 | 0.00 | 1.00 | 0.72 | premature finish |
| `unexpected_friend_encounter` | `api_llm_direct_actor` | 0.74 | 0.18 | 0.75 | 0.56 | repetitive social looping |
| `budget_errand_chain` | `api_llm_direct_actor` | 0.82 | 0.33 | 0.857 | 0.49 | goal repetition and idle drift |
| `lunch_meeting_time_pressure` | `api_llm_plan_then_act` | 0.84 | 0.46 | 1.00 | 0.38 | idle waiting / missed meeting action |
| `avoid_crowd_event` | `api_llm_reactive_replanner` | 0.78 | 0.42 | 1.00 | 0.36 | missed grocery task |

Only one row shows a large face-feasibility gap:

| Scenario | Agent | Face | Feasibility | Gap | Main issue |
|---|---:|---:|---:|---:|---|
| `commute_disruption` | `utility_planner` | 0.66 | 0.00 | 0.66 | ignores disruption context |

## Interpretation

The strongest signal is not simply "plausible plan versus hard infeasible
trace." In this v0 run, most full traces are deterministically feasible. The
more important failure is:

> locally reasonable actions accumulate into globally unbelievable city
> behavior.

This supports the CityAgency framing, but sharpens it. The benchmark should
measure at least three layers:

1. face validity of the local plan/action rationale;
2. deterministic feasibility under the city world model;
3. full-trace believability as human-like urban agency.

This is especially useful because high goal completion can hide bad agency. For
example, `api_llm_direct_actor` reaches 0.912 goal completion and 0.920 trace
feasibility, but only 0.547 trace believability. That is exactly the kind of
gap a city-agency benchmark should expose.

## Method Update

`judge_trace_plausibility.py` now writes checkpointed outputs after every judged
trace and resumes from `judged_traces.json` by default. This matters because
full judge runs require many API calls.

## Caveats

1. The actor model and judge model currently use the same configured provider,
   so judge independence is incomplete.
2. This is still one run per scenario/agent. The next version should add
   repeated API samples and confidence intervals.
3. The judge prompt is useful for diagnostics, but paper-grade claims need a
   small human-coded audit set or at least cross-model judge agreement.
4. The v0 scenarios are small. More pressure cases are needed for robust
   impossible-trace evaluation.

## Next Step

The next experiment should add repeated runs for the three API architectures on
the same eight scenarios, then report variance for:

- goal completion;
- trace feasibility;
- face plausibility;
- trace believability;
- face-believability gap;
- failure taxonomy.
