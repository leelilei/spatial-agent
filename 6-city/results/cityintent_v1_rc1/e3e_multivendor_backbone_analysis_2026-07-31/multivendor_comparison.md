# E3e Multi-Vendor Backbone Analysis

Two-sided permutation tests (20,000 samples), nonparametric bootstrap 95% confidence intervals, and Holm adjustment across the eight focused E3e comparisons. Each model-policy cell has n=18. Random seed: 20260731.

## Main Metrics

| Model | Policy | Task | Feasibility | Face plaus. | Trace believ. | Face-believ. gap |
|---|---|---:|---:|---:|---:|---:|
| gpt-5.4-mini | ReAct | 0.726 | 0.908 | 0.819 | 0.487 | 0.332 |
| gpt-5.4-mini | Plan-and-Execute | 0.534 | 0.909 | 0.889 | 0.544 | 0.345 |
| gpt-5.6-luna | ReAct | 0.797 | 0.994 | 0.892 | 0.655 | 0.237 |
| gpt-5.6-luna | Plan-and-Execute | 0.905 | 0.976 | 0.907 | 0.681 | 0.227 |
| deepseek-v4-flash | ReAct | 0.856 | 0.986 | 0.861 | 0.564 | 0.297 |
| deepseek-v4-flash | Plan-and-Execute | 0.626 | 0.922 | 0.843 | 0.493 | 0.349 |
| claude-sonnet-4-5-20250929 | ReAct | 0.932 | 1.000 | 0.928 | 0.722 | 0.207 |
| claude-sonnet-4-5-20250929 | Plan-and-Execute | 0.556 | 0.960 | 0.854 | 0.478 | 0.377 |
| qwen3-235b-a22b-instruct-2507 | ReAct | 0.787 | 0.945 | 0.898 | 0.618 | 0.280 |
| qwen3-235b-a22b-instruct-2507 | Plan-and-Execute | 0.821 | 0.960 | 0.862 | 0.538 | 0.323 |

## Focused Task-Completion Tests

| Type | Comparison | Policy | Delta | 95% CI | raw p | Holm p | Holm verdict |
|---|---|---|---:|---|---:|---:|---|
| scaffold | claude-sonnet-4-5-20250929/ReAct - claude-sonnet-4-5-20250929/Plan-and-Execute | ReAct - Plan-and-Execute | +0.376 | [+0.246, +0.492] | 0.0001 | 0.0004 | **significant** |
| scaffold | qwen3-235b-a22b-instruct-2507/ReAct - qwen3-235b-a22b-instruct-2507/Plan-and-Execute | ReAct - Plan-and-Execute | -0.034 | [-0.201, +0.124] | 0.6894 | 1.0000 | not significant |
| new_model_pair | claude-sonnet-4-5-20250929 - qwen3-235b-a22b-instruct-2507 | ReAct | +0.145 | [+0.007, +0.290] | 0.0704 | 0.3651 | not significant |
| new_vs_deepseek | claude-sonnet-4-5-20250929 - deepseek-v4-flash | ReAct | +0.075 | [-0.044, +0.191] | 0.2846 | 1.0000 | not significant |
| new_vs_deepseek | qwen3-235b-a22b-instruct-2507 - deepseek-v4-flash | ReAct | -0.069 | [-0.223, +0.080] | 0.3987 | 1.0000 | not significant |
| new_model_pair | claude-sonnet-4-5-20250929 - qwen3-235b-a22b-instruct-2507 | Plan-and-Execute | -0.265 | [-0.405, -0.120] | 0.0022 | 0.0150 | **significant** |
| new_vs_deepseek | claude-sonnet-4-5-20250929 - deepseek-v4-flash | Plan-and-Execute | -0.070 | [-0.247, +0.118] | 0.4819 | 1.0000 | not significant |
| new_vs_deepseek | qwen3-235b-a22b-instruct-2507 - deepseek-v4-flash | Plan-and-Execute | +0.195 | [+0.007, +0.385] | 0.0608 | 0.3651 | not significant |
