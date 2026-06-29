# CityAgency Four Official Framework Adapters

Date: 2026-06-30

## Purpose

Replace locally invented architecture labels with auditable integrations of
real external agent systems. The tested unit is each framework's official
decision layer under one shared CityIntent world and executor.

## Integration Surfaces

| Framework | Pinned commit | Official surface used | Integration label |
|---|---|---|---|
| GATSim | `3dc40248086cdfb1eca38d22b76b0edb5fe53ea6` | `generate_prompt`, daily/update plan templates, six-field activity plan | `adapted_official_planner` |
| SOTOPIA | `a0aaafb440e570e5e61b7c44a44e5e417c545383` | `LLMAgent.aact`, `agenerate_action` prompt, `AgentAction` schema | `adapted_official_llm_agent` |
| Generative Agents | `fe05a71d3e4ed7d10bf68aa4eda6dd995ec070f4` | Smallville daily plan, reflection, and revised schedule prompts | `adapted_official_memory_planner` |
| AgentSociety | `c8001a42409eb37be7cf745395bbe2269e7d83e0` | TPB guidance, detailed-plan, and mobility place-analysis blocks | `adapted_official_plan_blocks` |

For every framework, the trace stores the repository, commit, verified files,
actual model, integration level, and `native_backend=false`. CityIntent owns
the graph, time, budget, events, action execution, and deterministic scoring.
This is a real official decision-layer integration, not a claim that the full
GATSim, SOTOPIA, Smallville, or AgentSociety backend is running.

CitySim is not included as an official adapter because no official public code
implementation was found to pin and execute. A CitySim implementation would
currently be a paper reconstruction and must be labelled separately.

## Experiment

- model: `gpt-5.4-mini`
- provider: `fhl` via the shared research-standard client
- scenarios: `budget_errand_chain`, `closed_poi_replacement`
- traces: 8 (4 frameworks x 2 scenarios)
- total observed wall time: 474.8 seconds
- repetitions: 1

## Aggregate Results

| Framework adapter | Goal completion | Trace feasibility | Plausibility-feasibility gap | Feasibility violation | Budget consistency | Intention consistency |
|---|---:|---:|---:|---:|---:|---:|
| GATSim | 1.000 | 1.000 | 0.000 | 0.000 | 1.000 | 1.000 |
| Generative Agents | 1.000 | 0.875 | 0.125 | 0.125 | 0.500 | 0.875 |
| SOTOPIA | 0.875 | 0.812 | 0.188 | 0.125 | 0.500 | 0.781 |
| AgentSociety | 0.775 | 0.834 | 0.167 | 0.111 | 0.500 | 0.714 |

These are smoke results, not leaderboard estimates. With only two scenarios
and one stochastic run, rank ordering is not stable enough for a paper claim.

## Diagnostic Findings

1. The four official integrations execute end to end.

   Every trace contains verified official provenance and real provider output,
   then passes through the same typed CityIntent executor and scorer.

2. Framework structure produces visibly different failure modes.

   SOTOPIA's per-turn policy continued taking locally plausible moves after its
   budget became negative. Generative Agents could reflect and revise after a
   violation, but one run confused route waypoints with paid destinations.
   AgentSociety produced a coherent chain in an initial smoke, but the formal
   stochastic run drifted and failed to return home. GATSim completed both
   sampled scenarios without a deterministic violation.

3. Fluent planning is not sufficient evidence of executable city behavior.

   All four adapters received aggregate plan plausibility of 1.0, while three
   still produced nonzero impossible-trace gaps. This is exactly the diagnostic
   separation proposed by CityAgency.

4. Runtime cost differs materially by control loop.

   SOTOPIA calls the model every turn. Generative Agents may add reflection and
   schedule-revision calls after each new violation. Plan-oriented adapters can
   need fewer calls. The next runner revision should persist per-trace API call,
   latency, and token counts before a full comparison.

## Artifacts

- `benchmarks/cityintent_v0/external_adapters/`
- `benchmarks/cityintent_v0/tools/setup_external_framework.py`
- `benchmarks/cityintent_v0/tools/validate_external_adapters.py`
- `results/cityintent_v0/external_frameworks_4way_gpt54mini_2026-06-30/`

## Next Experiment

Run all four adapters over the complete 12-scenario suite with at least three
repetitions, persist cost/latency metadata, and report paired scenario-level
differences rather than relying on this two-scenario aggregate.
