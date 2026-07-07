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
  `results/cityintent_v1_rc1/paper_backed_baselines_2x2_smoke_v3_gpt54mini_2026-07-07/`

Two earlier prompt-discipline smoke archives are kept as debugging evidence:

- `results/cityintent_v1_rc1/paper_backed_baselines_2x2_smoke_gpt54mini_2026-07-07/`
- `results/cityintent_v1_rc1/paper_backed_baselines_2x2_smoke_v2_gpt54mini_2026-07-07/`
- `results/cityintent_v1_rc1/paper_backed_baselines_open_meet_v3_gpt54mini_2026-07-07/`

The v3 prompt adds explicit action-protocol reminders that social outcomes
usually require `move -> enter -> dwell/wait if early -> interact`, and that
`co_presence.time_window` must be respected.

## Final V3 Results

| Agent | Scenario | Task | Feasibility | Social appropriateness | Accepted interactions | Violations | Main failure |
|---|---|---:|---:|---:|---:|---:|---|
| `api_llm_plan_and_execute` | `social_copresence_open_meet` | 1.000 | 1.000 | 1.000 | 1 | 0 | Success |
| `api_llm_plan_and_execute` | `social_copresence_message_gated` | 0.308 | 0.600 | 0.500 | 0 | 2 | Waited/dwelled at paid cafe without service and still missed accepted interaction |
| `api_llm_react_tool_policy` | `social_copresence_open_meet` | 0.000 | 0.000 | 0.000 | 0 | 8 | Repeated interaction attempts without accepted entry state |
| `api_llm_react_tool_policy` | `social_copresence_message_gated` | 0.308 | 0.900 | 0.500 | 0 | 1 | Repeated messages and never converted coordination into accepted interaction |

Aggregate metrics:

| Agent | Task mean | Feasibility mean | Impossible trace rate | Social mean | City false continue |
|---|---:|---:|---:|---:|---:|
| `api_llm_plan_and_execute` | 0.654 | 0.800 | 0.200 | 0.750 | 0.500 |
| `api_llm_react_tool_policy` | 0.154 | 0.450 | 0.550 | 0.250 | 0.500 |

## Main Takeaway

The new baselines are technically connected: they call the real provider,
produce typed actions, record model telemetry, and can be scored by the existing
CityIntent executor. But the smoke does **not** justify immediately launching a
full 6-scenario repeated matrix.

Plan-and-Execute can complete the simplest open meeting once the protocol
explicitly states the entry/wait/interact chain. ReAct-style tool use still
fails the same simple social evidence task by repeating invalid or non-evidential
actions. This is useful: paper-backed execution-agent lineage is not enough by
itself to solve urban co-presence evidence.

## Next Decision

Before the full paper-backed baseline matrix, fix and re-smoke ReAct-style action
discipline on `social_copresence_open_meet`:

- expose the last action result as a compact `last_observation`;
- make previous violations more salient;
- add a hard instruction that an invalid interaction without entry must be
  repaired by `enter`, not another `interact`;
- consider a lightweight action-validator hint before calling the model, without
  auto-correcting the action.

Then run:

```text
api_llm_react_tool_policy
api_llm_plan_and_execute
x 6 social_outcome scenarios
x 3 repeats
```

only if both baselines can pass or meaningfully fail the open-meet sanity cell.
