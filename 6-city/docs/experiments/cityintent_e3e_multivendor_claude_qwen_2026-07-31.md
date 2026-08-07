# E3e — Multi-vendor hard-tier extension with Claude and Qwen

Date: 2026-07-31

## Question

E3d established that the plausible-to-verified outcome gap crosses from GPT
backbones to DeepSeek. E3e expands the actor-model coverage again: does the
gap, and the interaction between actor backbone and execution scaffold, survive
on Claude and Qwen?

## Setup

Two paper-backed policies × six oracle-winnable `social_outcome_hard`
scenarios × three repeats:

- ReAct-style tool policy
- Plan-and-Execute

Actor calls use Yunwu's OpenAI-compatible Chat Completions endpoint:

- `claude-sonnet-4-5-20250929`
- `qwen3-235b-a22b-instruct-2507`

The second-pass soft plausibility judge remains fixed at FHL
`gpt-5.4-mini`, matching E3/E3d. Deterministic task completion and feasibility
do not depend on this judge.

Formal archives:

- `results/cityintent_v1_rc1/e3e_yunwu_claude_sonnet45_2x6hardx3_2026-07-31/`
- `results/cityintent_v1_rc1/e3e_yunwu_qwen3_235b_a22b_instruct_2x6hardx3_2026-07-31/`
- combined analysis:
  `results/cityintent_v1_rc1/e3e_multivendor_backbone_analysis_2026-07-31/`

## Archive integrity

- Claude: 3/3 repeats, 36/36 actor traces, 36/36 judged traces
- Qwen: 3/3 repeats, 36/36 actor traces, 36/36 judged traces
- 72/72 total new traces and judgments
- every repeat contains the same 6-scenario × 2-policy matrix
- all 386 actor calls succeeded; zero archived failed actor calls
- exact provider token usage is present for every actor call
- Claude actor total: 191 calls, 764,623 tokens
- Qwen actor total: 195 calls, 714,144 tokens
- every final judge manifest identifies FHL `gpt-5.4-mini`

## Main results

| Backbone | Policy | Task | Feasibility | Face plaus. | Trace believ. | Face-believ. gap |
|---|---|---:|---:|---:|---:|---:|
| `claude-sonnet-4-5-20250929` | ReAct | **0.932** | **1.000** | 0.928 | 0.722 | 0.207 |
| `claude-sonnet-4-5-20250929` | Plan-and-Execute | 0.556 | 0.960 | 0.854 | 0.478 | **0.377** |
| `qwen3-235b-a22b-instruct-2507` | ReAct | 0.787 | 0.945 | 0.898 | 0.618 | 0.280 |
| `qwen3-235b-a22b-instruct-2507` | Plan-and-Execute | **0.821** | 0.960 | 0.862 | 0.538 | 0.323 |

The evidence gap remains positive in all four new model-policy cells. In
particular, Claude Plan-and-Execute is highly feasible (0.960) and
face-plausible (0.854), but its verified task completion is only 0.556 and its
face-to-trace believability gap is 0.377.

## Focused significance tests

The combined analysis follows E3d's two-sided 20,000-sample permutation test
and nonparametric bootstrap convention, with `n=18` per model-policy cell. It
also applies Holm correction across eight focused E3e comparisons.

| Comparison | Delta task | 95% CI | raw p | Holm p | Reading |
|---|---:|---|---:|---:|---|
| Claude ReAct − Claude Plan-and-Execute | **+0.376** | [+0.246, +0.492] | 0.0001 | **0.0004** | significant |
| Qwen ReAct − Qwen Plan-and-Execute | −0.034 | [−0.201, +0.124] | 0.6894 | 1.0000 | not significant |
| Claude − Qwen, ReAct | +0.145 | [+0.007, +0.290] | 0.0704 | 0.3651 | not significant |
| Claude − Qwen, Plan-and-Execute | **−0.265** | [−0.405, −0.120] | 0.0022 | **0.0150** | significant |

The one-repeat Qwen smoke descriptively favored Plan-and-Execute, but the full
three-repeat result is a near tie and not significant. That correction is why
the smoke was not reported as a final finding.

## Findings

1. **The evidence gap now spans four model families.** GPT, DeepSeek, Claude,
   and Qwen all retain positive face-to-trace gaps under the same CityIntent
   evidence contract.
2. **ReAct is comparatively portable.** Claude and Qwen ReAct task completion
   is not significantly different after correction, and neither new ReAct
   result differs significantly from DeepSeek in the focused tests.
3. **Upfront planning is strongly backbone-sensitive.** Qwen
   Plan-and-Execute exceeds Claude by 0.265 after Holm correction, while Claude
   shows a large, significant ReAct advantage.
4. **Scaffold ranking is not a generic capability ordering.** The defensible
   claim is an interaction between the particular actor backbone and the
   execution scaffold, not that one scaffold universally dominates.
5. **Feasibility remains easier than effectiveness.** All four new cells have
   feasibility at or above 0.945, but verified task completion ranges from
   0.556 to 0.932.

## Limitations and next decision

E3e changes the actor backbone while holding the judge fixed, which is correct
for actor comparison but does not test evaluator sensitivity. The next
experiment should therefore be a stratified cross-judge and human-validation
audit, not another broad actor-model sweep. Llama or Kimi may be retained as a
future open-model robustness extension, but they are lower priority than
closing evaluator validity.

## Reproduction

```bash
python 6-city/benchmarks/cityintent_v0/tools/analyze_e3e_multivendor_backbones.py
```

