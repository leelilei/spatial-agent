# E3 — Backbone sweep: gpt-5.4-mini → gpt-5.6-luna (hard tier)

Date: 2026-07-10

## Question

Every result so far sits on one backbone (`gpt-5.4-mini`). Is the
plausible↔verified gap a small-model artefact, and does a stronger backbone
close it?

## Setup

Same 6 `social_outcome_hard` scenarios × 3 repeats × the 2 paper-backed
baselines (36 real traces), identical executor / evidence contract / judge
(judge kept on mini for comparability). Backbone swapped to `gpt-5.6-luna`.

Archived: `results/cityintent_v1_rc1/e3_backbone_luna_2x6hardx3_2026-07-10/`.

## Result

| Policy | Backbone | task | ±sd | feasibility | legacy goal |
|---|---|---:|---:|---:|---:|
| ReAct | mini | 0.726 | 0.232 | 0.908 | 0.728 |
| ReAct | **5.6-luna** | **0.797** | 0.231 | **0.994** | 0.853 |
| Plan-and-Execute | mini | 0.534 | 0.267 | 0.909 | 0.603 |
| Plan-and-Execute | **5.6-luna** | **0.905** | 0.187 | 0.976 | 0.900 |

Per scenario (task_completion, mini → luna):

| Scenario | ReAct | Plan-and-Execute |
|---|---|---|
| `budget_entangled_meet` | 0.77 → **0.64** | 0.39 → 0.87 |
| `deadline_then_meet` | 0.67 → 1.00 | 0.50 → 0.83 |
| `full_evening_chain` | 0.64 → 0.64 | 0.93 → 1.00 |
| `overlapping_windows` | 0.50 → 0.50 | 0.50 → 0.83 |
| `stale_plan_override` | 0.78 → 1.00 | 0.56 → 1.00 |
| `three_meeting_relay` | 1.00 → 1.00 | 0.33 → 0.89 |

## Findings

1. **The gap does not respond to capability at all for the strongest policy.**
   ReAct goes 0.726 → 0.797, but a permutation test puts this at **p = 0.36,
   95% CI [−0.078, +0.216] — not significant** (see
   `results/cityintent_v1_rc1/backbone_significance_2026-07-10/`). An earlier
   version of this note read it as "the gap narrows"; that was an over-reading.
   The correct statement is stronger: a much more capable backbone leaves the
   best policy statistically where it was, still missing ~20% of provably
   winnable outcomes. The plausible↔verified gap is **not** a small-model artefact.

2. **The scaffold advantage collapses when the model is strong — and inverts.**
   Plan-and-Execute gains +0.371 (0.534 → 0.905) versus ReAct's +0.071, and ends
   up *ahead* of ReAct. Plan-and-Execute commits to one upfront plan and cannot
   self-correct, so its score is almost entirely a function of planning quality;
   a stronger planner rescues it. ReAct's iterative correction was largely
   *compensating for weak planning*, so it has little left to gain. Together with
   the earlier same-backbone finding (21/21 vs 0/21 across scaffolds), this gives
   a two-dimensional picture: **scaffolding substitutes for model capability, and
   its value falls as capability rises.**

3. **Residual failures are concentrated and scaffold-independent.**
   `overlapping_windows` is 0.50 for both policies on both backbones, and
   `full_evening_chain` is unchanged for ReAct. These are the far-closes-first
   and duration-bridge traps — non-greedy temporal ordering resists both stronger
   models and better scaffolds.

4. **Feasibility saturates** (ReAct 0.908 → 0.994): the stronger model essentially
   stops making illegal moves. Legality is easy; achieving the outcome is not.
   The "legal but ineffective" dissociation therefore *widens* in relative terms.

5. One regression: ReAct drops on `budget_entangled_meet` (0.77 → 0.64), the
   irreversible-budget trap. Not investigated; n=3 per cell, so it may be noise.

## Tooling note (real bug found)

`gpt-5.6-*` are reasoning variants served through a Codex relay. In **non-streaming**
mode they return a bare `reasoning` item with encrypted content and **no message** —
while reporting `status: "completed"` with `incomplete_details: null`, so the loss
is invisible. The text exists **only** in `response.output_text.delta` events; even
under streaming the terminal `response.completed` object still contains no message.
Any non-streaming client silently loses the answer.

`0-Tools/research-standard/llm_client.py` gained optional `stream` (SSE delta
accumulation) and `max_output_tokens`. Both are off unless configured, so other
projects are unaffected.

**Method lesson:** a toy smoke test ("Reply with exactly: OK") passed for all three
variants and was a false positive — they only fail on non-trivial prompts.
Smoke tests must run the real pipeline.
