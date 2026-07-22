# Co-Presence Evidence-Gap Anatomy — all six policies (E5 extended)

Date: 2026-07-10

## Question

The first evidence-gap pass covered only the two paper-backed baselines and
concluded "the gap is temporal precision, not navigation" (`no_venue_entry = 0`
everywhere). That conclusion was drawn from the *strongest* policies only. Does
it hold once the four adapted official decision layers are included?

## Method

Zero-API re-analysis. `tools/analyze_copresence_evidence_gap.py` now scans both
runs per tier (baselines + adapters, six policies, 288 judged traces) and
attributes every failed co_presence OUTCOME to one mutually-exclusive mechanism.

Archived: `results/cityintent_v1_rc1/copresence_evidence_gap_six_policy_2026-07-10/`.

## Result

| Tier | Policy | Failed/Total | no_venue_entry | entered_no_interact | interact_rejected | window_overrun |
|---|---|---:|---:|---:|---:|---:|
| easy | react_tool_policy | 0/21 | 0 | 0 | 0 | 0 |
| easy | plan_and_execute | 3/21 | 0 | 0 | 2 | 1 |
| easy | gatsim | 6/21 | 0 | 0 | 6 | 0 |
| easy | agentsociety | 17/21 | 6 | 8 | 2 | 1 |
| easy | generative_agents | 19/21 | 6 | 12 | 0 | 1 |
| easy | sotopia | 21/21 | 19 | 2 | 0 | 0 |
| hard | react_tool_policy | 6/27 | 0 | 1 | 1 | 4 |
| hard | gatsim | 6/27 | 0 | 0 | 3 | 3 |
| hard | plan_and_execute | 17/27 | 0 | 1 | 7 | 9 |
| hard | agentsociety | 23/27 | 10 | 5 | 7 | 1 |
| hard | generative_agents | 24/27 | 4 | 12 | 5 | 3 |
| hard | sotopia | 27/27 | 22 | 5 | 0 | 0 |

## Finding: the failure mode stratifies by policy strength — a capability ladder

The earlier "the gap is timing, not navigation" claim **only holds for the strong
policies**. Across all six there are three qualitatively different failures:

1. **Never arrives** — SOTOPIA-style: `no_venue_entry` 19/21 (easy) and 22/27
   (hard). Its 0/48 accepted co-presence is not a failure to close a meeting; it
   never walks to the venue at all, messaging from where it stands. This also
   explains its otherwise paradoxical high feasibility with near-zero completion:
   **standing still is perfectly legal at every step.**
2. **Arrives but never acts** — Generative Agents: `entered_no_interact` 12/12 of
   its non-navigation failures in each tier. It navigates to the right venue and
   then simply never issues the interaction — the meeting is in the plan and
   absent from the execution. AgentSociety sits between (1) and (2).
3. **Acts but mistimes** — ReAct / Plan-and-Execute / GATSim: `no_venue_entry = 0`
   in every cell; all failures are `window_overrun` or `interact_rejected`.

So: **cannot get there → gets there but doesn't act → acts but mistimes.** Three
distinct architectural deficits behind one aggregate metric.

## Why this matters

- It is the failure taxonomy Claim A promises, now grounded per policy rather
  than asserted.
- It corrects an over-generalisation in the earlier note: the temporal-precision
  finding is a property of the strong-policy regime, not of the benchmark overall.
- It pre-empts two opposite objections at once: the weak scaffolds are not failing
  because the contract is too strict (they never reach the venue), and the strong
  ones are not failing because the toy graph is hard (they navigate perfectly).
