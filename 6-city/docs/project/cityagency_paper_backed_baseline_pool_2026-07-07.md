# CityAgency Paper-Backed Baseline Pool

Date: 2026-07-07

## Purpose

This note turns the baseline discussion into a citable implementation plan. The
principle is simple: CityAgency should compare decision policies that have a
clear paper or benchmark lineage. Custom local agents can still be useful as
controls or ablations, but the main baseline table should not look like a set of
unnamed prompts invented only for this project.

The current experiments already use paper-backed adapted decision layers. The
next expansion should add a small number of paper-backed execution and mobility
architectures, not many loosely defined agent styles.

## Naming Rule

Use the source work to identify lineage, but name the executable object as an
adapter or policy. For example, SOTOPIA is a benchmark; the CityAgency baseline
is a `SOTOPIA-style LLMAgent decision adapter`, not "SOTOPIA" as a whole
benchmark.

Recommended wording:

> We evaluate adapted decision layers derived from representative agent systems
> and benchmarks, not the complete native systems unless explicitly stated.

## Already Connected

| CityAgency agent id | Paper/source lineage | What is actually evaluated | Integration status | Main reason to keep |
|---|---|---|---|---|
| `gatsim_official_planner` | GATSim | Mobility planning and schedule-update prompt surfaces mapped into CityIntent actions | Pinned adapted official decision layer | Strongest current urban-mobility planning baseline |
| `sotopia_official_llm_agent` | SOTOPIA | `LLMAgent`-style per-turn private-goal social action policy | Pinned adapted official decision layer | Tests whether social role-play agency becomes executable city agency |
| `generative_agents_official_planner` | Generative Agents / Smallville | Daily planning, reflection, and schedule revision prompt surfaces | Pinned adapted official decision layer | Canonical memory/reflection/planning lineage |
| `agentsociety_official_plan_blocks` | AgentSociety | TPB guidance, detailed-plan, and place-analysis prompt blocks | Pinned adapted official decision layer | Large-scale society simulation planning lineage |

These four should be described as `adapted official decision layers`. They are
not native end-to-end executions of the original systems.

## Candidate Expansion Pool

| Priority | Candidate adapter | Paper/source lineage | What CityAgency would test | Why it matters | Implementation stance |
|---|---|---|---|---|---|
| P0 | ReAct-style tool-use policy | ReAct; tau-bench; ChinaTravel; AppWorld | Interleaved reasoning, observation, and typed city action | Reviewer-standard execution baseline; checks whether failures are specific to city/social simulators | Implement as a paper-backed policy adapter and cite the benchmark implementations that use it |
| P0 | Plan-and-Execute policy | AppWorld | Initial plan followed by stepwise execution and repair | Separates "good plan" from "good execution" in the CityAgency thesis | We already have `api_llm_plan_then_act`; promote it only after aligning naming, prompts, and reporting with the cited lineage |
| P1 | Feasibility-aware planner-executor | FeasiGen; ChinaTravel neuro-symbolic planning | Detect infeasible city obligations and stop, substitute, or reroute rather than false-continue | Directly targets our false-continue and impossible-trace metrics | Implement after oracle-through-adapter checks so we know the environment can express the right repair |
| P1 | MobilityBench-style route-tool agent | MobilityBench | Route request decomposition, API/tool selection, and preference-constrained movement | Adds an explicitly mobility-benchmark-backed baseline beyond GATSim | Best added when CityIntent exposes route alternatives as tools rather than only typed moves |
| P1 | TrajGenAgent-style hierarchical grounding | TrajGenAgent | Activity-chain proposal followed by deterministic location, travel-time, and duration grounding | Bridges open-loop mobility trajectory generation with closed-loop city execution | Implement as a planner-grounder adapter, then test under disruptions |
| P2 | AgentMob-style evidence-grounded mobility policy | AgentMob | Tool-grounded next-location choice from history and urban context | Gives the urban-research side a mobility-prediction lineage | Needs careful framing because prediction evidence is not completion evidence |
| P2 | CodeAct / programmatic policy | AppWorld; TheAgentCompany | Generate explicit code or structured procedures to operate the city API | Strong execution baseline for deterministic action/state tasks | Useful later, but may overfit the benchmark API rather than model resident-like agency |

## Recommended Next Matrix

Do not expand to every candidate at once. The first runnable expansion adds two
paper-backed execution baselines to the current four adapted decision layers:

```text
4 current adapted decision layers
+ ReAct-style tool-use policy
+ Plan-and-Execute policy
x 6 social-outcome scenarios
x 3 repeats
x 1 fixed model
```

This directly tests whether the current social-outcome result is a limitation of
city/social simulation decision layers, or whether generic execution-agent
architectures also struggle to turn plausible plans into verified co-presence.

## Reporting Standard

Each baseline row should report:

- source paper or benchmark;
- exact executable policy name;
- whether the source code is pinned official code, reimplemented from paper, or
  only a lineage-inspired local control;
- prompt/action surfaces used;
- whether the adapter calls the original framework backend or only maps its
  decision layer into CityIntent;
- model provider and model id;
- deterministic outcome metrics and soft judge metrics.

## Claim Boundary

Paper-backed baselines strengthen the benchmark, but they do not by themselves
prove human-like urban behavior. CityAgency's current claim should remain:

> Different paper-backed agent decision policies that look plausible in language
> can diverge sharply when asked to produce verifiable continuous city traces.

## 2026-07-07 Implementation Status

Two runnable provider-backed policy adapters have been added:

- `api_llm_react_tool_policy`
- `api_llm_plan_and_execute`

The first smoke test is archived in
`docs/experiments/cityintent_paper_backed_baselines_2x2_smoke_2026-07-07.md`.
After the v6 action-discipline update, both baselines pass the open-meeting and
message-gated sanity cells with task, feasibility, and social scores all equal
to 1.0.

The full 2-agent x 6-social-scenario x 3-repeat matrix is archived in
`docs/experiments/cityintent_paper_backed_baselines_2x6x3_2026-07-07.md` and
`results/cityintent_v1_rc1/paper_backed_baselines_2x6socialx3_gpt54mini_2026-07-07/`.
It contains 36 provider-backed traces. ReAct accepts 21/21 required co-presence
outcomes, while Plan-and-Execute accepts 18/21 and mainly fails on two-party
simultaneous co-presence. This gives the benchmark a stronger baseline story:
generic execution-agent architectures can solve much of the social-outcome
family, so the lower adapted-framework scores are not an artifact of impossible
tasks or an over-strict verifier.
