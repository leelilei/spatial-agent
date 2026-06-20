# Telephone Notes Index

> Updated: 2026-06-20
> Status: all local PDF notes drafted; all 54 canonical notes deep-read;
> 4 duplicate / alias notes retained for source cleanup.

## Current State

- Local PDFs parsed: 58.
- Fulltext Markdown files: 58.
- Extraction failures: 0.
- Per-paper notes written: 58.
- Canonical notes deep-read: 54.
- Duplicate / alias notes retained: 4.
- Papers needing source/abstract caution: 9.
- Known duplicate: index 1 and index 11 are the same UIST 2023 Generative Agents paper.

## Priority Batches

| Batch | Goal | First output |
|---|---|---|
| A. Must-cite spine | Establish setting, closest neighbors, mechanism, and framing | 10-12 high-confidence notes |
| B. Agent society and memory levers | Support why natural levers are plausible and why our nulls matter | 8-10 support notes |
| C. Metrics and factuality | Support judge validation and fidelity measurement | 6-8 metric notes |
| D. Optional cleanup | Fill draft gaps and resolve flagged sources | As needed |

## Batch A Reading Queue

| Priority | Index | Paper | Role | Expected Telephone Use | Source status | Note |
|---:|---:|---|---|---|---|---|
| 1 | 11 | Generative Agents: Interactive Simulacra of Human Behavior | setting / must-cite neighbor | Agent societies show believable social diffusion; we measure fidelity of what spreads | abstract layout caution | `01_agent_societies/11_generative-agents-interactive-simulacra-of-human-behavior.md` |
| 2 | 50 | Simulating Misinformation Propagation in Social Networks using Large Language Models | close neighbor | LLM agents can simulate misinformation spread; we shift from propagation to held-belief fidelity | ok | `05_misinformation_correction/50_simulating-misinformation-propagation-in-social-networks-using-large-language-models.md` |
| 3 | 20 | Improving Factuality and Reasoning in Language Models through Multiagent Debate | debate / failed lever context | Debate can improve answers, but our society-level source condition shows speech can shift without belief repair | ok | `02_debate_consensus/20_improving-factuality-and-reasoning-in-language-models-through-multiagent-debate.md` |
| 4 | 39 | Large Language Models Cannot Self-Correct Reasoning Yet | correction limit | Supports why explicit correction may fail without reliable external grounding | ok | `03_hallucination_factuality/39_large-language-models-cannot-self-correct-reasoning-yet.md` |
| 5 | 61 | Belief Echoes: The Persistent Effects of Corrected Misinformation | mechanism | Continued influence after correction; human-side analog of persistent stale belief | abstract layout caution | `05_misinformation_correction/61_belief-echoes-the-persistent-effects-of-corrected-misinformation.md` |
| 6 | 54 | Rumor Cascades | mechanism / rumor dynamics | Cascade structure and diffusion dynamics; background for reach vs belief | abstract layout caution | `05_misinformation_correction/54_rumor-cascades.md` |
| 7 | 53 | The science of fake news | framing / misinformation | Canonical misinformation framing; use to separate reach, correction, and belief | abstract layout caution | `05_misinformation_correction/53_the-science-of-fake-news.md` |
| 8 | 68 | The Curse of Recursion | model-collapse analogy | Training-time recursive degradation; our contribution is communication-time analog | ok | `07_model_collapse_homogeneity/68_the-curse-of-recursion.md` |
| 9 | 69 | Self-Consuming Generative Models Go MAD | model-collapse analogy | Self-consumption and diversity/quality degradation; supports collapse framing | ok | `07_model_collapse_homogeneity/69_self-consuming-generative-models-go-mad.md` |
| 10 | 29 | TruthfulQA: Measuring How Models Mimic Human Falsehoods | factuality metric | Factuality can be measured as truthfulness, not just fluency; supports metric framing | ok | `03_hallucination_factuality/29_truthfulqa-measuring-how-models-mimic-human-falsehoods.md` |
| 11 | 12 | CAMEL: Communicative Agents for Mind Exploration of LLM Society | setting | Communication-centric LLM societies as a legitimate experimental setting | ok | `01_agent_societies/12_camel-communicative-agents-for-mind-exploration-of-llm-society.md` |
| 12 | 13 | AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation | setting / framework | Multi-agent conversation is a standard systems pattern; we study its fidelity risk | ok | `01_agent_societies/13_autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation.md` |

## Source Cautions

| Index | Paper | Issue | Action |
|---:|---|---|---|
| 1 | Generative Agents | Duplicate of index 11 | Do not write separate note unless needed for alias cleanup |
| 2 | Simulating Rumor Spreading in Social Networks using LLM Agents | Extracted abstract may include layout noise | Use full text/PDF, not abstract alone |
| 11 | Generative Agents: Interactive Simulacra of Human Behavior | Extracted abstract may include layout noise | Use full text/PDF, not abstract alone |
| 49 | Agent Hospital | Extracted abstract may include layout noise | Verify before citing |
| 53 | The science of fake news | Extracted abstract may include layout noise | Verify before citing |
| 54 | Rumor Cascades | Extracted abstract may include layout noise | Verify before citing |
| 55 | Emotions explain differences in the diffusion of true vs. false social media rumors | Local PDF appears to be a review, not the Scientific Reports article | Replace or verify before note |
| 61 | Belief Echoes | Extracted abstract may include layout noise | Use full text/PDF, not abstract alone |
| 66 | How Stereotypes Are Shared Through Language | Extracted abstract may include layout noise | Verify before citing |

## Claim-Evidence Matrix

| Telephone claim | Primary notes to write | Secondary notes |
|---|---|---|
| Agent societies are a real and important setting | 11, 12, 13 | 14, 15, 16, 17, 18 |
| Spread is not the same as fidelity | 11, 50, 53, 54 | 2, 51 |
| Speech can dissociate from held belief | 20, 39, 42, 43, 44 | 30, 37, 38 |
| Correction can fail because stale belief persists | 39, 61 | 53, 54 |
| Entrenchment/path dependence has precedent | 61, 66, 67 | 53, 54 |
| Model collapse is the analogy, not the same mechanism | 68, 69, 70 | 9, 10 |
| Factuality and judge validation need careful metrics | 29, 30, 32, 36 | 31, 33, 35, 40 |

## Completion Rules

Batch A is complete when:

- At least 10 notes are written.
- Each has a `must-cite` or `cite` decision, or a clear reason for downgrade.
- `paper/references.md` is updated with verified use sentences.
- The related-work draft has one paragraph outline for setting, mechanism, and framing.

## All Local PDF Notes Coverage

| Index | Decision | Role | Note |
|---:|---|---|---|
| 1 | replace | alias / duplicate record | `01_agent_societies/01_generative-agents.md` |
| 2 | cite | LLM-agent rumor simulation / reach baseline | `05_misinformation_correction/02_simulating-rumor-spreading-in-social-networks-using-llm-agents.md` |
| 3 | replace | alias / duplicate record | `02_debate_consensus/03_improving-factuality-and-reasoning-through-multiagent-debate.md` |
| 4 | cite | debate supervision / unreliable expert aggregation | `02_debate_consensus/04_debate-helps-supervise-unreliable-experts.md` |
| 5 | replace | alias / duplicate record | `03_hallucination_factuality/05_truthfulqa.md` |
| 9 | replace | alias / duplicate record | `07_model_collapse_homogeneity/09_ai-models-collapse-when-trained-on-recursively-generated-data.md` |
| 10 | maybe | collective synthetic cognition / model-homogeneity framing | `07_model_collapse_homogeneity/10_artificial-hivemind.md` |
| 11 | must-cite | setting / must-cite neighbor | `01_agent_societies/11_generative-agents-interactive-simulacra-of-human-behavior.md` |
| 12 | cite | communicative-agent society / setting | `01_agent_societies/12_camel-communicative-agents-for-mind-exploration-of-llm-society.md` |
| 13 | cite | multi-agent conversation framework / setting | `01_agent_societies/13_autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation.md` |
| 14 | background | multi-agent collaboration framework / emergent behavior | `01_agent_societies/14_agentverse-facilitating-multi-agent-collaboration-and-exploring-emergent-behaviors-in-ag.md` |
| 15 | background | role-structured multi-agent collaboration | `01_agent_societies/15_metagpt-meta-programming-for-a-multi-agent-collaborative-framework.md` |
| 16 | background | communicative software-development agents | `01_agent_societies/16_chatdev-communicative-agents-for-software-development.md` |
| 17 | background | multi-agent platform infrastructure | `01_agent_societies/17_agentscope-a-flexible-yet-robust-multi-agent-platform.md` |
| 18 | cite | social intelligence evaluation for agents | `01_agent_societies/18_sotopia-interactive-evaluation-for-social-intelligence-in-language-agents.md` |
| 19 | cite | theory of mind and multi-agent collaboration | `01_agent_societies/19_theory-of-mind-for-multi-agent-collaboration-via-large-language-models.md` |
| 20 | cite | debate / positive social-reasoning baseline | `02_debate_consensus/20_improving-factuality-and-reasoning-in-language-models-through-multiagent-debate.md` |
| 21 | cite | debate diversity / divergent thinking | `02_debate_consensus/21_encouraging-divergent-thinking-in-large-language-models-through-multi-agent-debate.md` |
| 22 | cite | persuasive debate / truthful answers | `02_debate_consensus/22_debating-with-more-persuasive-llms-leads-to-more-truthful-answers.md` |
| 23 | maybe | peer discussion for LLM evaluation | `02_debate_consensus/23_prd-peer-rank-and-discussion-improve-llm-based-evaluations.md` |
| 24 | cite | multi-agent debate for summary faithfulness | `02_debate_consensus/24_faithful-unfaithful-or-ambiguous-multi-agent-debate-with-initial-stance-for-summary-eval.md` |
| 25 | maybe | debate reveals hidden premises | `02_debate_consensus/25_multi-agent-llm-debate-unveils-the-premise-left-unsaid.md` |
| 26 | maybe | consensus agent / deliberative agreement | `02_debate_consensus/26_consensagent.md` |
| 27 | maybe | debate architecture / reasoning framework | `02_debate_consensus/27_cortexdebate.md` |
| 28 | maybe | multi-agent evaluation / selective evidence | `02_debate_consensus/28_selene.md` |
| 29 | must-cite | truthfulness benchmark / metric anchor | `03_hallucination_factuality/29_truthfulqa-measuring-how-models-mimic-human-falsehoods.md` |
| 30 | cite | self-consistency hallucination detection | `03_hallucination_factuality/30_selfcheckgpt.md` |
| 31 | cite | model knowledge and calibration | `03_hallucination_factuality/31_language-models-mostly-know-what-they-know.md` |
| 32 | cite | semantic entropy hallucination detection | `03_hallucination_factuality/32_detecting-hallucinations-in-large-language-models-using-semantic-entropy.md` |
| 33 | cite | hallucination evaluation benchmark | `03_hallucination_factuality/33_halueval.md` |
| 34 | background | Chinese hallucination evaluation | `03_hallucination_factuality/34_evaluating-hallucinations-in-chinese-large-language-models.md` |
| 35 | background | universal hallucination generation/evaluation | `03_hallucination_factuality/35_uhgeval.md` |
| 36 | cite | RAG hallucination benchmark | `03_hallucination_factuality/36_ragtruth.md` |
| 37 | cite | internal-state lie/factuality signal | `03_hallucination_factuality/37_the-internal-state-of-an-llm-knows-when-its-lying.md` |
| 38 | cite | calibration prompting / uncertainty | `03_hallucination_factuality/38_just-ask-for-calibration.md` |
| 39 | cite | correction limit / failed natural lever | `03_hallucination_factuality/39_large-language-models-cannot-self-correct-reasoning-yet.md` |
| 40 | background | hallucination benchmark extension | `03_hallucination_factuality/40_anah-v2.md` |
| 41 | maybe | LLM delusions / persistent false beliefs | `03_hallucination_factuality/41_delusions-of-large-language-models.md` |
| 42 | cite | long-term memory for LLM companions | `04_memory_state_agents/42_memorybank.md` |
| 43 | cite | virtual-context memory management | `04_memory_state_agents/43_memgpt.md` |
| 44 | cite | reflection as verbal reinforcement / memory | `04_memory_state_agents/44_reflexion.md` |
| 45 | background | reasoning-action interleaving | `04_memory_state_agents/45_react.md` |
| 46 | cite | lifelong embodied agent with skill memory | `04_memory_state_agents/46_voyager.md` |
| 47 | cite | agentic evolving memory | `04_memory_state_agents/47_a-mem.md` |
| 48 | background | LLM agent operating system | `04_memory_state_agents/48_aios-llm-agent-operating-system.md` |
| 49 | background | medical multi-agent simulation / applied agent society | `04_memory_state_agents/49_agent-hospital.md` |
| 50 | must-cite | close neighbor / fidelity metric | `05_misinformation_correction/50_simulating-misinformation-propagation-in-social-networks-using-large-language-models.md` |
| 51 | cite | agent personas and misinformation vulnerability | `05_misinformation_correction/51_simulating-misinformation-vulnerabilities-with-agent-personas.md` |
| 53 | must-cite | misinformation framing / reach vs impact | `05_misinformation_correction/53_the-science-of-fake-news.md` |
| 54 | cite | rumor dynamics / correction in cascades | `05_misinformation_correction/54_rumor-cascades.md` |
| 55 | replace | source problem / wrong local PDF | `05_misinformation_correction/55_emotions-explain-differences-in-the-diffusion-of-true-vs-false-social-media-rumors.md` |
| 61 | must-cite | mechanism / correction persistence | `05_misinformation_correction/61_belief-echoes-the-persistent-effects-of-corrected-misinformation.md` |
| 66 | cite | language transmission of stereotypes / cultural persistence | `06_transmission_culture/66_how-stereotypes-are-shared-through-language.md` |
| 67 | cite | audience tuning / stereotype transmission | `06_transmission_culture/67_the-audience-tuning-effect-of-negative-stereotypes-in-communication.md` |
| 68 | must-cite | model-collapse analogy | `07_model_collapse_homogeneity/68_the-curse-of-recursion.md` |
| 69 | cite | model-collapse analogy / diversity-quality tradeoff | `07_model_collapse_homogeneity/69_self-consuming-generative-models-go-mad.md` |
| 70 | cite | synthetic data collapse analysis | `07_model_collapse_homogeneity/70_how-bad-is-training-on-synthetic-data.md` |
| 71 | cite | trustworthy LLM-mediated communication / alignment intervention | `07_model_collapse_homogeneity/71_trustworthy-llm-mediated-communication-laac.md` |
