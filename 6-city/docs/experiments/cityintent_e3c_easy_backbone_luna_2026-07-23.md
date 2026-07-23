# E3c — Six-policy stronger-backbone sweep on the easy social tier

Date: 2026-07-23

## Question

E3 and E3b measured the backbone effect on the hard social tier. E3c closes the
corresponding easy-tier cell: when all six policies use `gpt-5.6-luna`, do the
weak decision scaffolds still fail the original six `social_outcome` scenarios?

## Setup

Six policies × six oracle-winnable `social_outcome` scenarios × three repeats:

- ReAct-style tool policy
- Plan-and-Execute
- GATSim adapted official planner
- SOTOPIA-style adapted `LLMAgent`
- Generative Agents adapted planner
- AgentSociety adapted plan blocks

The executor and evidence contract are unchanged. Agent calls use
`gpt-5.6-luna`; the second-pass judge remains on `gpt-5.4-mini` for comparability
with the earlier easy-tier table.

Archived:
`results/cityintent_v1_rc1/e3c_easy_luna_6x6easyx3_2026-07-10/`.

Archive integrity:

- 3/3 repeats complete
- 36 traces and 36 judged traces per repeat
- 108/108 total judged rows
- full 6 scenario × 6 policy matrix in every repeat

## Result

| Policy | mini task | luna task | Δ | luna feasibility | face↔believability gap |
|---|---:|---:|---:|---:|---:|
| ReAct | 1.000 | 1.000 | +0.000 | 0.976 | 0.158 |
| Plan-and-Execute | 0.917 | 1.000 | +0.083 | 0.979 | 0.197 |
| GATSim | 0.667 | 0.634 | −0.033 | 0.796 | 0.388 |
| AgentSociety | 0.325 | 0.857 | +0.532 | 0.946 | 0.214 |
| Generative Agents | 0.220 | 0.712 | +0.492 | 0.961 | 0.339 |
| SOTOPIA-style | 0.103 | 0.579 | +0.476 | 0.822 | 0.287 |

The mini comparison uses the earlier unified six-policy easy-tier archive.
These are descriptive differences; E3c does not add a new significance claim.

## Reading

1. **The hard-tier capability pattern replicates on the easy tier.** The three
   weakest mini policies gain by roughly 0.48–0.53 task completion, while ReAct
   is already at ceiling and GATSim is descriptively unchanged.
2. **Weak scaffolds are capability-sensitive, not intrinsically incapable.**
   AgentSociety reaches 0.857 and Generative Agents 0.712 on the same evidence
   contract where their mini scores were 0.325 and 0.220.
3. **A stronger backbone does not erase trace-quality gaps.** All six policies
   retain a positive face-plausibility versus trace-believability gap. GATSim's
   gap is the largest (0.388), alongside feasibility of 0.796.
4. **The easy tier is now mainly a ceiling/calibration tier.** ReAct and
   Plan-and-Execute both reach task 1.0. The hard tier remains the primary
   discriminative result for strong policies.

## Caveats

- GATSim's message-gated result remains confounded by its adapter action surface:
  the E4 oracle-through-adapters experiment showed that it cannot synthesize a
  `message` action.
- The judge backbone is intentionally held fixed, so E3c isolates the agent
  backbone rather than testing judge sensitivity.
