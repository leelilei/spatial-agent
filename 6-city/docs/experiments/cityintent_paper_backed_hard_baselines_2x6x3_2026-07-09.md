# CityIntent Paper-Backed Baselines on the HARD Social Family (E2 baseline side)

Date: 2026-07-09

## Question

The easy `social_outcome` family had a ceiling: ReAct-style tool-use scored
21/21 accepted co-presence (task_completion 1.0), leaving no headroom to
discriminate strong policies or to justify a backbone sweep. Does the new
`social_outcome_hard` family (E1, two-sided verified) restore dynamic range for
the two strongest policies, and do failures land on the designed mechanisms?

## Setup

- Agents: `api_llm_react_tool_policy`, `api_llm_plan_and_execute` (the two
  paper-backed execution baselines).
- Scenarios: the 6 `social_outcome_hard` scenarios.
- Repeats: 3 (36 real provider-backed traces, gpt-5.4-mini via FHL).
- Same typed executor + environment-owned evidence contract + judge as prior runs.
- Archive: `results/cityintent_v1_rc1/paper_backed_baselines_2x6hardx3_gpt54mini_2026-07-09/`.

## Headline result — the ceiling is broken

| Policy | Easy tier task | **Hard tier task** | Hard feasibility |
|---|---:|---:|---:|
| ReAct-style tool-use | 1.000 (21/21) | **0.726 ± 0.232** | 0.908 |
| Plan-and-Execute | 0.857 (18/21) | **0.534 ± 0.267** | 0.909 |

The hard family drops the strongest policy from a perfect score to 0.73, and the
planner to 0.53 — restoring the headroom a backbone sweep (E3) needs.

## The "legal but ineffective" dissociation now appears in the STRONGEST baselines

Feasibility stays ~0.91 while task_completion falls to 0.53–0.73: the plans are
legal, the outcomes are not achieved. This is no longer a property of the weak
SOTOPIA-style adapter (0/21) — it holds for frontier-style scaffolds on
well-posed, provably-winnable tasks. The clearest single cells:

- `hard_overlapping_windows` / ReAct: **feasibility 1.000, task 0.500** — every
  move legal; took the near already-reachable option and missed the
  far-closes-first window.
- `hard_three_meeting_relay` / Plan-and-Execute: **feasibility 1.000, task 0.333**
  — a fully legal trace that commits nearest-first and forfeits the strict-order
  windows.

The judge sees it too: face-plausibility 0.82–0.89 vs trace-believability
0.49–0.54 (face–believability gap ≈ 0.33–0.35).

## Failures land on the designed mechanisms (per-scenario task_completion)

| Scenario (mechanism) | ReAct | Plan-Exec |
|---|---:|---:|
| `three_meeting_relay` (strict-order sequencing) | 1.000 | **0.333** |
| `budget_entangled_meet` (irreversible budget) | 0.769 | **0.385** |
| `deadline_then_meet` (non-greedy ordering under deadline) | 0.667 | 0.500 |
| `stale_plan_override` (fresh update beats memory) | 0.778 | 0.555 |
| `full_evening_chain` (meal-duration bridge) | **0.643** | 0.929 |
| `overlapping_windows` (far-closes-first) | 0.500 | 0.500 |

Every drop is mechanism-legible, not noise:

- **Plan-and-Execute dies where commitment is punished**: relay (0.333) and
  budget-entanglement (0.385) — it locks in an upfront plan and cannot adapt when
  a window ordering or an irreversible purchase invalidates it.
- **ReAct dies where a greedy salience-first step exits early**: full_evening_chain
  (0.643, must dwell through a meal to bridge into the social window) and
  overlapping_windows (0.500, must skip the near trap for the far-closing option).
- **Neither policy dominates** — `full_evening_chain` inverts the ranking
  (Plan-Exec 0.929 > ReAct 0.643): the one scenario where planning the
  meal-duration bridge ahead beats reactive salience. The family separates the
  two policies *by mechanism*, which is what a discriminating benchmark should do.

## Secondary diagnostics

- ReAct budget_consistency 0.944 (< 1.0): it occasionally goes budget-negative on
  the entanglement trap; Plan-Exec stays budget-legal but simply fails the outcome.
- ReAct done_state_loop_rate 0.333: some repeated-completion looping under pressure.
- Cost asymmetry: ReAct ≈ 10 calls / 87k tokens per trace vs Plan-Exec 1 call /
  7.6k — the adaptivity that wins costs ~11× the tokens.

## Takeaways

1. **Ceiling broken → E3 (backbone sweep) is now justified**: with strong policies
   at 0.53–0.73 there is room to rank models.
2. **The gap generalizes upward**: plausible↔verified dissociation is not an
   artifact of weak scaffolds; it holds for ReAct/Plan-and-Execute on winnable
   tasks, strengthening Claim A.
3. **Mechanism validity**: failures map onto the intended traps (sequencing,
   budget entanglement, non-greedy ordering), confirming the hard tier measures
   spatio-temporal commitment, not noise.

## Next

- E2 adapter side: run the 4 official adapters over `social_outcome_hard` × 3 on
  the checkout machine, then extend the unified table to 6 policies × 12 scenarios.
- E3: backbone sweep over the combined family (needs provider routing decision).
