# CityIntent v1-rc1 Unified Six-Policy Social Table

Date: 2026-07-08

## Question

What is the first paper-ready comparison when the four adapted official
decision layers and the two paper-backed execution baselines are placed on the
same six social-outcome scenarios?

## Source Archives

- `results/cityintent_v1_rc1/external_frameworks_4x6socialx1_gpt54mini_2026-07-06/`
- `results/cityintent_v1_rc1/paper_backed_baselines_2x6socialx3_gpt54mini_2026-07-07/`

The generated unified archive is:

`results/cityintent_v1_rc1/unified_six_policy_social_table_2026-07-08/`

The table is reproducible with:

```powershell
python 6-city/benchmarks/cityintent_v0/tools/build_unified_social_table.py
```

## Main Result

| Policy | Family | Accepted co-presence | Outcome rate | Full social | Social pass^3 | Full task | Fully feasible | Joint success | Legal but ineffective | Plausible but unverified |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ReAct-style tool-use policy | paper-backed execution baseline | 21/21 | 1.000 | 1.000 | 1.000 | 1.000 | 0.833 | 0.833 | 0.000 | 0.000 |
| Plan-and-Execute policy | paper-backed execution baseline | 18/21 | 0.857 | 0.833 | 0.833 | 0.833 | 0.722 | 0.667 | 0.056 | 0.167 |
| GATSim adapted planner | adapted official decision layer | 15/21 | 0.714 | 0.667 | 0.667 | 0.667 | 0.500 | 0.500 | 0.000 | 0.278 |
| AgentSociety plan-block adapter | adapted official decision layer | 4/21 | 0.190 | 0.222 | 0.167 | 0.222 | 0.278 | 0.167 | 0.111 | 0.778 |
| Generative Agents adapted planner | adapted official decision layer | 2/21 | 0.095 | 0.111 | 0.000 | 0.056 | 0.056 | 0.000 | 0.056 | 0.667 |
| SOTOPIA-style LLMAgent adapter | adapted official decision layer | 0/21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.611 | 0.000 | 0.611 | 0.889 |

`Social pass^3` is the fraction of scenario-policy cells where all three
repeats accept all required co-presence outcomes.

## Scenario Heatmap

| Scenario | ReAct | Plan-and-Execute | GATSim | AgentSociety | Generative Agents | SOTOPIA-style |
|---|---:|---:|---:|---:|---:|---:|
| `social_copresence_decoy_location` | 3/3 | 3/3 | 0/3 | 0/3 | 1/3 | 0/3 |
| `social_copresence_event_window` | 3/3 | 3/3 | 3/3 | 0/3 | 0/3 | 0/3 |
| `social_copresence_message_gated` | 3/3 | 3/3 | 0/3 | 0/3 | 0/3 | 0/3 |
| `social_copresence_open_meet` | 3/3 | 3/3 | 3/3 | 1/3 | 0/3 | 0/3 |
| `social_copresence_two_party` | 6/6 | 3/6 | 6/6 | 0/6 | 0/6 | 0/6 |
| `social_copresence_with_errand` | 3/3 | 3/3 | 3/3 | 3/3 | 1/3 | 0/3 |

## Reading

This is the cleanest current CityAgency result. The social-outcome family is
not unwinnable: ReAct, Plan-and-Execute, and GATSim all complete most or all of
the required environment-owned co-presence outcomes. At the same time, the
SOTOPIA-style `LLMAgent` adapter produces 0/21 accepted outcomes while retaining
0.611 fully feasible traces, 0.813 mean face plausibility, and 0.889
plausible-but-unverified traces.

That is exactly the paper story: plausible social behavior and legal movement
are not enough. A city agent must produce verifiable state transitions in the
world: entering the right place, at the right time, with the right counterpart,
and completing the required interaction.

The two paper-backed execution baselines add a useful ceiling. ReAct closes the
social-evidence gap, but at higher cost and with residual paid-state or terminal
state issues. Plan-and-Execute is cheaper and face-plausible, but is brittle on
the two-party simultaneous co-presence scenario. This lets the benchmark argue
about architecture mechanisms rather than only ranking model names.

## Next Step

The next paper-facing step is judge or human-audit sensitivity on this unified
table. The deterministic co-presence outcome should remain the primary metric;
LLM plausibility scores should be treated as explanatory diagnostics.
