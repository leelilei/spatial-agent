# E3d Cross-Vendor Backbone Comparison

Two-sided permutation test (20,000 samples) and nonparametric bootstrap 95% CI, n=18 per model-policy cell. Random seed: 20260724.

## Main Metrics

| Model | Policy | Task | Feasibility | Face plaus. | Trace believ. | Face-believ. gap |
|---|---|---:|---:|---:|---:|---:|
| gpt-5.4-mini | ReAct | 0.726 | 0.908 | 0.819 | 0.487 | 0.332 |
| gpt-5.4-mini | Plan-and-Execute | 0.534 | 0.909 | 0.889 | 0.544 | 0.345 |
| gpt-5.6-luna | ReAct | 0.797 | 0.994 | 0.892 | 0.655 | 0.237 |
| gpt-5.6-luna | Plan-and-Execute | 0.905 | 0.976 | 0.907 | 0.681 | 0.227 |
| deepseek-v4-flash | ReAct | 0.856 | 0.986 | 0.861 | 0.564 | 0.297 |
| deepseek-v4-flash | Plan-and-Execute | 0.626 | 0.922 | 0.843 | 0.493 | 0.349 |

## Task-Completion Significance

| Comparison | Policy | Δ | 95% CI | p | Verdict |
|---|---|---:|---|---:|---|
| deepseek-v4-flash − gpt-5.4-mini | ReAct | +0.130 | [-0.010, +0.268] | 0.0867 | not significant |
| deepseek-v4-flash − gpt-5.6-luna | ReAct | +0.059 | [-0.080, +0.200] | 0.4255 | not significant |
| deepseek-v4-flash − gpt-5.4-mini | Plan-and-Execute | +0.092 | [-0.106, +0.285] | 0.3868 | not significant |
| deepseek-v4-flash − gpt-5.6-luna | Plan-and-Execute | -0.278 | [-0.454, -0.099] | 0.0051 | **significant** |
| gpt-5.4-mini/ReAct − gpt-5.4-mini/Plan-and-Execute | ReAct − Plan-and-Execute | +0.192 | [+0.029, +0.349] | 0.0264 | **significant** |
| gpt-5.6-luna/ReAct − gpt-5.6-luna/Plan-and-Execute | ReAct − Plan-and-Execute | -0.107 | [-0.238, +0.027] | 0.1402 | not significant |
| deepseek-v4-flash/ReAct − deepseek-v4-flash/Plan-and-Execute | ReAct − Plan-and-Execute | +0.230 | [+0.049, +0.410] | 0.0205 | **significant** |

## Reading

- ReAct is comparatively backbone-robust: DeepSeek is descriptively above mini and Luna, but neither difference is significant.
- Plan-and-Execute is backbone-sensitive: Luna significantly outperforms DeepSeek, while DeepSeek and mini are statistically indistinguishable.
- The Luna scaffold inversion is not significant. On DeepSeek, ReAct significantly outperforms Plan-and-Execute, so scaffold ranking depends on the specific backbone rather than a single generic capability ordering.
- DeepSeek ReAct remains nearly fully feasible while missing verified outcomes and retaining a substantial face-to-trace believability gap; the core evidence-gap finding crosses vendors.
