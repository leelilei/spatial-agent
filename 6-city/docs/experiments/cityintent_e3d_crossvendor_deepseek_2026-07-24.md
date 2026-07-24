# E3d — Cross-vendor hard-tier replication with DeepSeek

Date: 2026-07-24

## Question

E3 and E3b varied model capability inside one provider/model family. E3d tests
whether the central CityIntent findings survive a vendor change: do the
plausible-to-verified gap and scaffold effects observed with GPT backbones also
appear with `deepseek-v4-flash`?

## Setup

Two paper-backed policies × six oracle-winnable `social_outcome_hard`
scenarios × three repeats:

- ReAct-style tool policy
- Plan-and-Execute

Agent calls use `deepseek-v4-flash` through the same typed CityIntent executor
and action-evidence contract. The second-pass plausibility judge remains fixed
at `gpt-5.4-mini`, matching E3, so the comparison changes the acting backbone
without changing the judge.

Archived:
`results/cityintent_v1_rc1/e3d_crossvendor_deepseek_2x6hardx3_2026-07-10/`.

Archive integrity:

- 3/3 repeats complete
- 12 traces and 12 judged traces per repeat
- 36/36 total judged rows
- full 6 scenario × 2 policy matrix in every repeat
- all actor traces identify `deepseek-v4-flash`
- zero archived failed calls and complete provider usage
- all three judge manifests identify `gpt-5.4-mini`

## Main result

| Backbone | Policy | Task | Feasibility | Face plaus. | Trace believ. | Face-believ. gap |
|---|---|---:|---:|---:|---:|---:|
| gpt-5.4-mini | ReAct | 0.726 | 0.908 | 0.819 | 0.487 | 0.332 |
| gpt-5.4-mini | Plan-and-Execute | 0.534 | 0.909 | 0.889 | 0.544 | 0.345 |
| gpt-5.6-luna | ReAct | 0.797 | 0.994 | 0.892 | 0.655 | 0.237 |
| gpt-5.6-luna | Plan-and-Execute | 0.905 | 0.976 | 0.907 | 0.681 | 0.227 |
| deepseek-v4-flash | ReAct | **0.856** | **0.986** | 0.861 | 0.564 | **0.297** |
| deepseek-v4-flash | Plan-and-Execute | 0.626 | 0.922 | 0.843 | 0.493 | **0.349** |

DeepSeek ReAct is almost fully legal (feasibility 0.986) but still misses about
14% of verified task outcomes and retains a 0.297 face-to-trace believability
gap. DeepSeek Plan-and-Execute is substantially weaker on outcomes (0.626) even
though its plans remain face-plausible (0.843). The central distinction between
reasonable-looking behavior and verified execution therefore survives a vendor
change.

## Significance analysis

The archived `crossvendor_comparison.md` uses the same two-sided 20,000-sample
permutation test and nonparametric bootstrap convention as the earlier
hard-tier backbone analysis (n=18 per model-policy cell).

| Comparison | Policy | Δ task | 95% CI | p | Reading |
|---|---|---:|---|---:|---|
| DeepSeek − mini | ReAct | +0.130 | [−0.010, +0.268] | 0.0867 | not significant |
| DeepSeek − Luna | ReAct | +0.059 | [−0.080, +0.200] | 0.4255 | not significant |
| DeepSeek − mini | Plan-and-Execute | +0.092 | [−0.106, +0.285] | 0.3868 | not significant |
| DeepSeek − Luna | Plan-and-Execute | **−0.278** | [−0.454, −0.099] | **0.0051** | significant |

Within-backbone scaffold comparisons:

- Mini: ReAct − Plan-and-Execute = +0.192, p=0.0264.
- Luna: ReAct − Plan-and-Execute = −0.107, p=0.1402; the apparent inversion is
  not significant.
- DeepSeek: ReAct − Plan-and-Execute = +0.230, p=0.0205.

## Findings

1. **The evidence gap crosses vendors.** A non-GPT actor still produces
   highly feasible and plausible traces that fail verified outcomes or receive
   much lower full-trace believability scores.
2. **ReAct is comparatively backbone-robust.** DeepSeek, mini, and Luna ReAct
   task scores are not significantly different in the pairwise comparisons.
3. **Plan-and-Execute is backbone-sensitive.** Luna significantly outperforms
   DeepSeek under the same fixed executor and judge, while DeepSeek and mini
   are statistically indistinguishable.
4. **Scaffold ranking is model-specific.** The earlier descriptive Luna
   inversion should not be generalized into a capability law: it is not
   significant, and ReAct is significantly ahead on both mini and DeepSeek.
   The defensible claim is that upfront planning quality interacts strongly
   with the particular backbone.
5. **Legality remains easier than effectiveness.** DeepSeek ReAct reaches
   feasibility 0.986 but task completion 0.856; its residual failures are not
   primarily illegal movement.

## Tooling and execution note

The run exposed two transport defects rather than scientific failures:

- Chat Completions initially ignored the configured curl transport and remained
  hard-coded to urllib, causing TLS EOF failures.
- The initial curl path exposed the Authorization header in local process
  arguments.

Both were fixed before the final repeat completed. The hardened transport uses
a mode-0600 temporary curl config that is deleted after each request, and the
resilient wrapper resumes completed scenario-policy cells. These changes affect
transport reliability and credential handling, not prompts, models, actions,
scoring, or the experimental matrix.

## Reproduction

Generate the comparison artifacts:

```bash
python 6-city/benchmarks/cityintent_v0/tools/analyze_crossvendor_backbones.py
```

The raw and derived outputs are documented in `ARCHIVE.md`,
`repeated_summary.md`, `crossvendor_summary.csv`, and
`crossvendor_significance.csv`.
