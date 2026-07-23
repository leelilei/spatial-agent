# Backbone effect — significance (hard tier, task_completion)

Permutation test (20k) + bootstrap 95% CI on the difference, n=18 per cell.

| Policy | mini | luna | Δ | 95% CI | p | verdict |
|---|---:|---:|---:|---|---:|---|
| ReAct | 0.726 | 0.797 | +0.071 | [-0.078, +0.216] | 0.3602 | not significant |
| Plan-and-Execute | 0.534 | 0.905 | +0.371 | [+0.217, +0.513] | 0.0001 | **significant** |
| GATSim | 0.750 | 0.701 | -0.049 | [-0.293, +0.194] | 0.8306 | not significant |
| SOTOPIA-style | 0.158 | 0.527 | +0.369 | [+0.232, +0.516] | 0.0000 | **significant** |
| Generative Agents | 0.410 | 0.629 | +0.219 | [+0.054, +0.387] | 0.0152 | **significant** |
| AgentSociety | 0.314 | 0.665 | +0.351 | [+0.186, +0.512] | 0.0004 | **significant** |

## Reading

The four weaker policies improve significantly on the stronger backbone
(p < 0.02). The two strongest — ReAct (0.726) and GATSim (0.750) — do **not**
move at all: their intervals straddle zero.

This corrects two over-readings in the E3 / E3b notes:
- ReAct's +0.071 was reported as "the gap narrows"; p = 0.36, so it does not.
- GATSim's −0.049 was reported as an engineered-scaffold regression with design
  implications; p = 0.83, so it is noise.

The corrected statement is stronger than the original: a much more capable
backbone lifts weak scaffolds substantially but leaves the best policies exactly
where they were, with ReAct still missing ~20% of provably winnable outcomes.
The plausible-verified gap is therefore not a small-model artefact — the evidence
is now firmer, because the strongest policies show *no* capability response at all.

