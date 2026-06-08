# SMGA Selected Papers

This file records the first curated paper set for SMGA. The set is intentionally small: it includes only papers needed for the current SMGA v4.4 framing, baseline design, benchmark choice, and evaluation protocol.

## P0 Core Papers

| Priority | Paper | Local target | Source | SMGA use |
|---|---|---|---|---|
| P0 | Generative Agents: Interactive Simulacra of Human Behavior | `pdfs/01_foundations/01_Generative_Agents_Park2023.*` | `1-SpatialAgent/assets/survey_paper/pdfs/phase1_core/01_Generative_Agents_Park2023.*` | Direct GA baseline: memory stream, reflection, planning, believable behavior |
| P0 | Affordable Generative Agents | `pdfs/01_foundations/02_Affordable_Generative_Agents_Yu2024.*` | `1-SpatialAgent/assets/papers/pdfs/01_LLM_Game_Agents/03_Affordable_Generative_Agents_Yu2024.*` | Bottleneck framing and contrast with AGA Social Memory |
| P0 | SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents | `pdfs/03_social_benchmarks/07_SOTOPIA_Zhou2024_ICLR.*` | `1-SpatialAgent/assets/papers/pdfs/05_Multi_Agent_Social_Simulation/05_SOTOPIA_Zhou2024_ICLR.*` | External social-interaction evaluation foundation |
| P0 | A-MEM: Agentic Memory for LLM Agents | `pdfs/02_memory_architectures/03_AMEM_Xu2025.*` | `1-SpatialAgent/assets/papers/pdfs/06_Agent_Memory_Cognitive/04_AMEM_Xu2025.*` | Closest memory-architecture / graph-memory control |
| P0 | MemGPT: Towards LLMs as Operating Systems | `pdfs/02_memory_architectures/04_MemGPT_Packer2023.*` | `1-SpatialAgent/assets/papers/pdfs/06_Agent_Memory_Cognitive/02_MemGPT_Packer2023.*` | Long-term memory and storage-management baseline |
| P0 | Reflexion: Language Agents with Verbal Reinforcement Learning | `pdfs/02_memory_architectures/05_Reflexion_Shinn2023_NeurIPS.*` | `1-SpatialAgent/assets/papers/pdfs/06_Agent_Memory_Cognitive/03_Reflexion_Shinn2023_NeurIPS.*` | Prompted / verbal reflection baseline |
| P0 | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | `pdfs/04_evaluation/10_LLM_as_Judge_MT_Bench_Zheng2023_NeurIPS.*` | `1-SpatialAgent/assets/papers/pdfs/07_Evaluation_Methodology/02_LLM_as_Judge_MT_Bench_Zheng2023_NeurIPS.*` | Human-agreement and LLM-judge validation background |
| P0 | A Survey on LLM-as-a-Judge | `pdfs/04_evaluation/11_Survey_LLM_as_Judge_2024.*` | `1-SpatialAgent/assets/papers/pdfs/07_Evaluation_Methodology/03_Survey_LLM_as_Judge_2024.*` | Bias, reliability, and meta-evaluation background |

## P1 Supporting Papers

| Priority | Paper | Local target | Source | SMGA use |
|---|---|---|---|---|
| P1 | Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents | `pdfs/02_memory_architectures/06_AgeMem_Yu2026.*` | `1-SpatialAgent/assets/papers/pdfs/06_Agent_Memory_Cognitive/01_AgeMem_Yu2026.*` | Recent memory-management context |
| P1 | MultiAgentBench: Evaluating the Collaboration and Competition of LLM Agents | `pdfs/03_social_benchmarks/08_MultiAgentBench_Zhu2025.*` | `1-SpatialAgent/assets/papers/pdfs/01_LLM_Game_Agents/06_MultiAgentBench_Zhu2025.*` | Multi-agent evaluation context |
| P1 | Network Formation and Dynamics Among Multi-LLMs | `pdfs/03_social_benchmarks/09_Network_Formation_LLMs_Papachristou2025.*` | `1-SpatialAgent/assets/papers/pdfs/07_Evaluation_Methodology/07_Network_Formation_LLMs_Papachristou2025.*` | Social-network behavior and prompt-sensitivity context |
| P1 | Navigates Like Me: Understanding How People Evaluate Human-Like AI in Video Games | `pdfs/04_evaluation/12_Navigates_Like_Me_Milani2023.*` | `1-SpatialAgent/assets/papers/pdfs/2303.02160v1.*` | Human-likeness / believability evaluation context |

## Reading Notes Copied

- `reading_notes/park2023_generative_agents.md`
- `reading_notes/Generative_Agents_Interactive_Simulacra_of_Human_Behavior_notes_2026-04-06.md`
- `reading_notes/yu2024_affordable_generative_agents.md`
- `reading_notes/affordable_generative_agents_2024.md`
- `reading_notes/zhu2025_multiagentbench.md`

## Deferred Papers

These are relevant to SMGA but were not copied because no local curated file was selected in this pass:

- CoALA
- MemoryBank
- Voyager
- LIFELONG-SOTOPIA
- SOTOPIA-pi / SOTOPIA-π
- AriGraph
- G-Memory

## Exclusion Rule

Do not bulk-copy SpatialAgent assets. Space Syntax, spatial reasoning, NPC dialogue, and survey-wide evidence assets stay in `1-SpatialAgent` unless a specific SMGA paper section requires them.
