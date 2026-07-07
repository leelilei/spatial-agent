# CityIntent Paper-Backed Baselines 2x2 Smoke

Date: 2026-07-07

## Question

Can the first two paper-backed execution baselines run as real provider-backed
CityIntent agents, and do they immediately solve simple social-outcome evidence
tasks?

## Setup

- New policies:
  - `api_llm_react_tool_policy`: ReAct-style thought-action-observation policy.
  - `api_llm_plan_and_execute`: Plan-and-Execute policy alias for the existing
    initial-plan execution surface.
- Model: provider-backed `gpt-5.4-mini`.
- Scenarios:
  - `social_copresence_open_meet`
  - `social_copresence_message_gated`
- Final smoke archive:
  `results/cityintent_v1_rc1/paper_backed_baselines_2x2_smoke_v6_gpt54mini_2026-07-07/`

Earlier prompt-discipline smoke archives are kept as debugging evidence:

- `results/cityintent_v1_rc1/paper_backed_baselines_2x2_smoke_gpt54mini_2026-07-07/`
- `results/cityintent_v1_rc1/paper_backed_baselines_2x2_smoke_v2_gpt54mini_2026-07-07/`
- `results/cityintent_v1_rc1/paper_backed_baselines_open_meet_v3_gpt54mini_2026-07-07/`
- `results/cityintent_v1_rc1/paper_backed_baselines_2x2_smoke_v3_gpt54mini_2026-07-07/`
- `results/cityintent_v1_rc1/paper_backed_react_open_meet_v4_gpt54mini_2026-07-07/`
- `results/cityintent_v1_rc1/paper_backed_baselines_2x2_smoke_v4_gpt54mini_2026-07-07/`
- `results/cityintent_v1_rc1/paper_backed_baselines_2x2_smoke_v5_gpt54mini_2026-07-07/`

The final v6 prompt adds explicit action-protocol reminders that social outcomes
usually require `move -> enter -> paid-service if needed -> dwell/wait if early
-> interact`, and that `co_presence.time_window` must be respected. ReAct also
receives a compact `last_observation` and a `required_next_action` repair hint.

## Final V6 Results

| Agent | Scenario | Task | Feasibility | Social appropriateness | Accepted interactions | Violations | Main failure |
|---|---|---:|---:|---:|---:|---:|---|
| `api_llm_plan_and_execute` | `social_copresence_open_meet` | 1.000 | 1.000 | 1.000 | 1 | 0 | Success |
| `api_llm_plan_and_execute` | `social_copresence_message_gated` | 1.000 | 1.000 | 1.000 | 1 | 0 | Success |
| `api_llm_react_tool_policy` | `social_copresence_open_meet` | 1.000 | 1.000 | 1.000 | 1 | 0 | Success |
| `api_llm_react_tool_policy` | `social_copresence_message_gated` | 1.000 | 1.000 | 1.000 | 1 | 0 | Success |

Aggregate metrics:

| Agent | Task mean | Feasibility mean | Impossible trace rate | Social mean | City false continue |
|---|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 1.000 | 1.000 | 0.000 | 1.000 | 0.000 |
| `api_llm_react_tool_policy` | 1.000 | 1.000 | 0.000 | 1.000 | 0.000 |

## Main Takeaway

The new baselines are technically connected: they call the real provider,
produce typed actions, record model telemetry, and can be scored by the existing
CityIntent executor. After the v6 action-discipline update, both baselines pass
the two sanity cells with full task completion, full feasibility, and accepted
co-presence evidence.

The debugging path is itself informative. Earlier versions showed the exact
failure modes CityAgency is designed to expose: ReAct repeated interaction
without entry, and Plan-and-Execute waited in a paid cafe without service
evidence. The final adapter does not hide those failures; it makes the expected
environment protocol explicit enough that the baseline can be fairly evaluated
on harder cells.

## Next Decision

The sanity gate is now passed. The next run can be:

```text
api_llm_react_tool_policy
api_llm_plan_and_execute
x 6 social_outcome scenarios
x 3 repeats
```

This should be reported as a paper-backed execution-baseline expansion, not as a
replacement for the adapted official-framework comparison.
