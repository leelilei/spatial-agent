# CityIntent v1-rc1 Social-Outcome Family Experiment

Date: 2026-07-06

## Research Question

Can official urban/social-agent decision architectures reliably turn plausible
coordination behavior into environment-accepted co-presence outcomes across a
family of city episodes?

## Setup

- Six oracle-winnable `social_outcome` scenarios: open meeting, message-gated
  meeting, event-window meeting, two-party sequential meetings, meeting plus
  errand, and a decoy-location test.
- Four pinned adapted official decision layers: GATSim, a SOTOPIA-style
  `LLMAgent` policy, Generative Agents, and AgentSociety.
- Agent model: provider-backed `gpt-5.4-mini`.
- Repeats: 3 per scenario-adapter cell.
- Coverage: 4 adapters x 6 scenarios x 3 repeats = 72 traces.
- Social proof obligations: 21 co-presence outcomes per adapter. Five scenarios
  require one meeting per repeat; the two-party scenario requires two.
- Execution telemetry: 364 successful agent calls, 2,572,773 provider-reported
  tokens, and 2,240.439 seconds aggregate request latency.
- Soft evaluators: `gpt-5.4-mini` and `gpt-5.4` on all 72 identical traces.
- Hard outcomes: environment-accepted `interaction` evidence, task completion,
  and deterministic trace feasibility.

## Main Family Result

| Adapter | Accepted co-presence | Outcome rate | Full social traces | Social `pass^3` | Full task | Fully feasible | Joint success | Legal but ineffective | Plausible but unverified |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| AgentSociety | 4/21 | 0.190 | 0.222 | 0.167 | 0.222 | 0.278 | 0.167 | 0.111 | 0.778 |
| GATSim | 15/21 | 0.714 | 0.667 | 0.667 | 0.667 | 0.500 | 0.500 | 0.000 | 0.278 |
| Generative Agents | 2/21 | 0.095 | 0.111 | 0.000 | 0.056 | 0.056 | 0.000 | 0.056 | 0.667 |
| SOTOPIA-style LLMAgent | 0/21 | 0.000 | 0.000 | 0.000 | 0.000 | 0.611 | 0.000 | 0.611 | 0.889 |

`Social pass^3` is the fraction of scenario-adapter cells where every repeat
accepts all required co-presence outcomes. Joint success requires full task
completion and full trace feasibility.

SOTOPIA is a benchmark, not an agent architecture. The row above names the
adapted `LLMAgent`-style decision policy used inside CityIntent.

## Core Finding: Legal But Ineffective Is A Family Effect

The SOTOPIA-style LLMAgent adapter produces no accepted co-presence outcome in
21 opportunities and no full task success, while 61.1% of its traces are fully
feasible. The mini judge marks 88.9% as face-plausible. This extends the earlier
meeting anecdote into a repeated six-scenario family effect: legal and plausible
coordination behavior is not evidence that a meeting occurred.

The result is not caused by an impossible family or an unreachable action type:

- every scenario has an oracle trace with task 1.0, feasibility 1.0, and accepted
  interaction evidence;
- the compliance probe shows the adapter translation surfaces can express the
  winning interaction action;
- GATSim obtains 15/21 accepted outcomes, proving the live shared pipeline can
  realize them under the same model and executor.

## Architecture Profiles

- **GATSim** achieves social `pass^3` on open meeting, event-window meeting,
  two-party meetings, and meeting plus errand. It fails all repeats of the
  message-gated and decoy-location scenarios.
- **AgentSociety** achieves `pass^3` only on meeting plus errand and succeeds in
  one open-meeting repeat. It enters a target venue without completing the social
  outcome in 61.1% of traces.
- **Generative Agents** accepts only 2/21 outcomes, one in the decoy scenario and
  one in meeting plus errand. No scenario reaches social `pass^3`, and no trace is
  a joint success.
- **SOTOPIA-style LLMAgent** sends counterpart-directed messages without a
  successful meeting in 61.1% of traces. It demonstrates coordination language
  without environment-accepted co-presence.

## Evidence-Gap Diagnostics

| Adapter | Message without meeting | Interact attempt without success | Target entry without meeting | Mean task | Mean feasibility | Mean face plausibility |
|---|---:|---:|---:|---:|---:|---:|
| AgentSociety | 0.333 | 0.333 | 0.611 | 0.325 | 0.615 | 0.903 |
| GATSim | 0.000 | 0.333 | 0.333 | 0.667 | 0.819 | 0.776 |
| Generative Agents | 0.333 | 0.056 | 0.722 | 0.220 | 0.666 | 0.772 |
| SOTOPIA-style LLMAgent | 0.611 | 0.056 | 0.111 | 0.103 | 0.913 | 0.813 |

The decision policies fail at different stages: the SOTOPIA-style LLMAgent often
communicates but does not establish joint state; Generative Agents and
AgentSociety often reach relevant places without producing accepted interaction
evidence; GATSim attempts some interactions that fail a location, timing, or
coordination gate.

## Plausibility-Judge Robustness

| Metric | n | Mini mean | Full mean | MAE | Pearson | Spearman | Threshold agreement | Kappa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Face plausibility | 72 | 0.816 | 0.727 | 0.136 | 0.566 | 0.516 | 0.681 | 0.098 |
| Trace believability | 72 | 0.413 | 0.472 | 0.207 | 0.433 | 0.441 | 0.778 | 0.253 |
| Rationale alignment | 72 | 0.706 | 0.484 | 0.291 | 0.443 | 0.483 | 0.569 | 0.271 |
| Urban common sense | 72 | 0.594 | 0.658 | 0.172 | 0.557 | 0.549 | 0.667 | 0.344 |

Soft evaluator agreement is weak to moderate. Plausibility scores explain how a
failed trace may look convincing, but only the environment decides whether the
social outcome occurred.

## Claim Supported

Across a repeated social-outcome family, architecture-specific planning and
coordination behavior often appears plausible, and may remain physically legal,
without producing the environment-owned state change required by the private
goal. This is a reproducible plausible-to-verified gap, not a single-scenario
anecdote.

## Limits

- These are adapted official decision layers under a shared CityIntent executor,
  not native end-to-end framework deployments.
- The agent backbone is fixed to `gpt-5.4-mini`; model-by-architecture sensitivity
  remains a separate experiment.
- Human construct validation is still required before v1 freeze.
- The six scenarios test controlled micro-city social mechanisms, not population-
  scale urban behavior or human realism.

## Archive

`6-city/results/cityintent_v1_rc1/external_frameworks_4x6socialx1_gpt54mini_2026-07-06/`
