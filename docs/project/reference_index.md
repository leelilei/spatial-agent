# SpatialAgent: Comprehensive Academic Paper Collection

This compilation assembles **60+ papers, tools, and resources** across eight research categories for the SpatialAgent project—bridging architectural Space Syntax theory with LLM-based game agents. Each entry includes verified titles, authors, venues, years, and direct access URLs. The collection spans foundational works from the 1984 origins of Space Syntax to cutting-edge 2026 preprints on spatially-aware agents, providing a complete literature base for an AAAI-27 or CHI 2027 submission.

---

## Category 1: LLM-based game agents

These seven papers form the core baseline for understanding how large language models power autonomous game agents, from the seminal generative agents architecture to recent multi-agent benchmarks.

**1. Generative Agents: Interactive Simulacra of Human Behavior**
- **Authors:** Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein
- **Venue:** UIST 2023 (ACM Symposium on User Interface Software and Technology)
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2304.03442
- **Notes:** Seminal paper introducing the generative agent architecture with **memory stream, reflection, and planning** in a sandbox town of 25 agents. The foundational reference for SpatialAgent's agent architecture.

**2. A Survey on Large Language Model-Based Game Agents**
- **Authors:** Sihao Hu, Tiansheng Huang, Gaowen Liu, Ramana Rao Kompella, Fatih Ilhan, Selim Furkan Tekin, Yichang Xu, Zachary Yahn, Ling Liu
- **Venue:** arXiv preprint (submitted April 2024, revised November 2025)
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2404.02039
- **Notes:** Comprehensive survey with a unified reference architecture covering memory, reasoning, perception-action at single-agent level and communication/organizational models at multi-agent level across six game genres.

**3. Affordable Generative Agents**
- **Authors:** Yangbin Yu, Qin Zhang, Junyou Li, Qiang Fu, Deheng Ye
- **Venue:** Transactions on Machine Learning Research (TMLR), August 2024
- **Year:** 2024
- **URLs:** https://arxiv.org/abs/2402.02053 | https://openreview.net/forum?id=7tlYbcq5DY
- **Notes:** Proposes the AGA framework reducing LLM API costs to **~31% of baseline** via Lifestyle Policy and Social Relationship Memory. Tested on Stanford Town and VirtualHome.

**4. Project Sid: Many-Agent Simulations Toward AI Civilization**
- **Authors:** Altera.AL, Andrew Ahn, Nic Becker, Stephanie Carroll, Nico Christie, Manuel Cortes, Arda Demirci, Melissa Du, Frankie Li, Shuying Luo, Peter Y. Wang, Mathew Willows, Feitong Yang, Guangyu Robert Yang
- **Venue:** arXiv preprint, October 2024
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2411.00114
- **Notes:** Demonstrates **10–1,000+ LLM agents** in Minecraft developing emergent social behaviors: specialized roles, collective rules, cultural and religious transmission. Introduces the PIANO architecture for real-time multi-output coherence.

**5. LIGS: Developing an LLM-Infused Game System for Emergent Narrative**
- **Authors:** Jin Jeong, Tak Yeon Lee
- **Venue:** CHI EA 2025 (Extended Abstracts of the CHI Conference on Human Factors in Computing Systems)
- **Year:** 2025
- **URL:** https://dl.acm.org/doi/10.1145/3706599.3720212
- **DOI:** 10.1145/3706599.3720212
- **Notes:** LLM-driven emergent narratives where players freely input text while LLMs operate NPCs and update game objects. User study with 20 participants.

**6. MultiAgentBench: Evaluating the Collaboration and Competition of LLM Agents**
- **Authors:** Kunlun Zhu, Hongyi Du, Zhaochen Hong, Xiaocheng Yang, Shuyi Guo, Zhe Wang, Zhenhailong Wang, Cheng Qian, Xiangru Tang, Heng Ji, Jiaxuan You
- **Venue:** ACL 2025 (Main Conference)
- **Year:** 2025
- **URLs:** https://arxiv.org/abs/2503.01935 | GitHub: https://github.com/MultiagentBench/MARBLE
- **Notes:** Benchmark evaluating multi-agent LLM systems with milestone-based KPIs. Tests star, chain, tree, and graph coordination topologies. GPT-4o-mini achieves highest task scores; **graph topology performs best** in research scenarios.

**7. Artificial Leviathan: Exploring Social Evolution of LLM Agents Through the Lens of Hobbesian Social Contract Theory**
- **Authors:** Gordon Dai, Weijia Zhang, Jinhan Li, Siqi Yang, Chidera Onochie Ibe, Srihas Rao, Arthur Caetano, Misha Sra
- **Venue:** arXiv preprint, June 2024
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2406.14373
- **Notes:** Simulates agent society with psychological drives in a sandbox survival environment. Agents evolve from Hobbesian "state of nature" to peaceful commonwealth via emergent social contracts.

---

## Category 2: Space Syntax theory and agent simulation

The foundational architecture-domain literature, from the original 1984 theory to recent computational extensions combining Space Syntax with machine learning and deep learning.

### Foundational works

**1. The Social Logic of Space**
- **Authors:** Bill Hillier and Julienne Hanson
- **Venue:** Cambridge University Press, 1984 (paperback 1988)
- **Year:** 1984
- **ISBN:** 978-0-521-36784-4
- **URLs:** https://doi.org/10.1017/CBO9780511597237 | https://www.cambridge.org/core/books/social-logic-of-space/6B0A078C79A74F0CC615ACD8B250A985
- **Notes:** The foundational text introducing the Space Syntax framework and its theory of how spatial configuration shapes social encounter patterns.

**2. Space is the Machine: A Configurational Theory of Architecture**
- **Author:** Bill Hillier
- **Venue:** Cambridge University Press, 1996; Electronic edition by Space Syntax, 2007
- **Year:** 1996
- **URLs:** https://spaceisthemachine.com/ (free official download) | https://patterns.architexturez.net/system/files/SITM.pdf
- **Notes:** **Freely available online.** Extends *The Social Logic of Space* into a comprehensive configurational theory of architecture with extensive empirical research.

**3. From Isovists to Visibility Graphs: A Methodology for the Analysis of Architectural Space**
- **Authors:** Alasdair Turner, Maria Doxa, David O'Sullivan, Alan Penn
- **Venue:** Environment and Planning B: Planning and Design, Vol. 28(1), pp. 103–121, 2001
- **Year:** 2001
- **URLs:** https://doi.org/10.1068/b2684 | Free PDF: http://discovery.ucl.ac.uk/160/1/turner-doxa-osullivan-penn-2001.pdf
- **Notes:** Introduces **Visibility Graph Analysis (VGA)**, extending isovist analysis to graph-based methods. Critical for SpatialAgent's spatial representation layer.

**4. Space Syntax Based Agent Simulation**
- **Authors:** Alan Penn and Alasdair Turner
- **Venue:** 1st International Conference on Pedestrian and Evacuation Dynamics, 2001; published in Schreckenberg & Sharma (eds.) *Pedestrian and Evacuation Dynamics*, pp. 99–114, Springer, 2002
- **Year:** 2001/2002
- **URLs:** https://discovery.ucl.ac.uk/2027/1/penn.pdf | https://www.academia.edu/276347/Space_Syntax_Based_Agent_Simulation
- **Notes:** Describes the **exosomatic visual architecture (EVA)** based on visibility graphs for agent-based pedestrian simulation. Directly foundational for combining Space Syntax with agent simulation.

**5. Space Syntax Methodology (4th edition, draft)**
- **Authors:** Kinda Al-Sayed, Alasdair Turner, Bill Hillier, Shinichi Iida, Alan Penn (with contributions from Griffiths, Karimi, Vaughan, Psarra, Conroy Dalton, Varoudis, Sailer, Yang, Fatah gen. Schieck, Hanna)
- **Venue:** Bartlett School of Architecture, UCL, London, 2014
- **Year:** 2014
- **URL:** https://www.researchgate.net/publication/295855785_Space_Syntax_methodology
- **Notes:** Highly accessible teaching textbook covering Space Syntax theory, spatial analysis techniques, observation methods, data modelling, and agent-based modelling using depthmapX.

### Recent computational extensions (2020–2026)

**6. Agent-Based Analysis of Urban Spaces Using Space Syntax and Spatial Cognition Approaches: A Case Study in Bari, Italy**
- **Authors:** Dario Esposito, Stefania Santoro, Domenico Camarda
- **Venue:** Sustainability, Vol. 12(11), 4625, 2020
- **Year:** 2020
- **URL:** https://www.mdpi.com/2071-1050/12/11/4625

**7. Computational Analytical Methods for Buildings and Cities: Space Syntax and Shape Grammar**
- **Authors:** Michael J. Ostwald, Ju Hyun Lee
- **Venue:** Buildings, Vol. 13(7), 1613, 2023
- **Year:** 2023
- **URL:** https://www.mdpi.com/2075-5309/13/7/1613

**8. Comparative Analysis of Pedestrian Volume Models: Agent-Based Models, Machine Learning Methods and Multiple Regression Analysis**
- **Authors:** Lior Wolpert, Itzhak Omer
- **Venue:** Computers, Environment and Urban Systems, 2024
- **Year:** 2024
- **URL:** https://www.sciencedirect.com/science/article/abs/pii/S0198971524001674
- **Notes:** Directly compares Space Syntax-based regression, **gradient boosting ML**, and agent-based models for pedestrian volume prediction.

**9. Evaluation of Spatial Visual Perception of Streets Based on Deep Learning and Spatial Syntax**
- **Venue:** Scientific Reports (Nature), 2025
- **Year:** 2025
- **URL:** https://www.nature.com/articles/s41598-025-03189-z
- **Notes:** Applies deep learning to street view images combined with Space Syntax network accessibility analysis.

**10. Visibility Graph Analysis vs. Human Mobility Patterns: An Empirical Validation of Simulation-Based Analysis Using Space Syntax in Public Squares**
- **Authors:** Reza Askarizad, Chiara Garau
- **Venue:** Springer (INPUT 2023 proceedings, published 2026)
- **Year:** 2026
- **URL:** https://link.springer.com/chapter/10.1007/978-3-031-97654-4_4
- **Notes:** Validates VGA agent-based simulation against real-world pedestrian observation in Cagliari, Italy.

---

## Category 3: Spatially-aware LLM agents

The most directly relevant category for SpatialAgent—papers exploring how LLMs can perceive, reason about, and respond to spatial environments.

**1. When LLMs Recognize Your Space: Research on Experiences with Spatially Aware LLM Agents**
- **Authors:** Seungwoo Oh, Nakyoung An, Youngwug Cho, Myeongul Jung, Kwanguk Kenny Kim
- **Venue:** IEEE Transactions on Visualization and Computer Graphics (IEEE TVCG), Vol. 31, No. 11, pp. 10090–10098, November 2025 (IEEE VR 2025)
- **Year:** 2025
- **DOI:** 10.1109/TVCG.2025.3616809
- **URL:** https://pubmed.ncbi.nlm.nih.gov/41052126/
- **Notes:** Directly studies **spatial awareness levels in LLM agents** during counselling conversations. The closest prior work to SpatialAgent's core hypothesis that spatial awareness improves agent behavior.

**2. SARAH: Spatially Aware Real-time Agentic Humans**
- **Authors:** Evonne Ng, Siwei Zhang, Zhang Chen, Michael Zollhoefer, Alexander Richard
- **Venue:** arXiv preprint, February 2026
- **Year:** 2026
- **URLs:** https://arxiv.org/abs/2602.18432 | Project page: https://evonneng.github.io/sarah/
- **Notes:** First real-time, fully causal method for spatially-aware conversational motion in VR. Generates full-body 3D motion conditioned on user position and dyadic audio at **300+ FPS**.

**3. Advancing Spatial Reasoning in Large Language Models: An In-Depth Evaluation and Enhancement Using the StepGame Benchmark**
- **Authors:** Fangjun Li, David C. Hogg, Anthony G. Cohn
- **Venue:** AAAI 2024, Vol. 38, pp. 18500–18507
- **Year:** 2024
- **URLs:** https://arxiv.org/abs/2401.03991 | https://ojs.aaai.org/index.php/AAAI/article/view/29811
- **Notes:** Refines the StepGame benchmark; GPTs show proficiency in mapping text to spatial relations but **limitations in multi-hop spatial reasoning**. Tests Chain-of-Thought and Tree-of-Thoughts strategies.

**4. SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities**
- **Authors:** Boyuan Chen, Zhuo Xu, Sean Kirmani, Brain Ichter, Dorsa Sadigh, Leonidas Guibas, Fei Xia
- **Venue:** CVPR 2024, pp. 14455–14465
- **Year:** 2024
- **URL:** https://spatial-vlm.github.io/
- **Notes:** Framework endowing VLMs with direct spatial reasoning (distance estimation, spatial relationship understanding), enabling chain-of-thought spatial reasoning.

**5. Reframing Spatial Reasoning Evaluation in Language Models: A Real-World Simulation Benchmark for Qualitative Reasoning**
- **Authors:** Fangjun Li, David C. Hogg, Anthony G. Cohn
- **Venue:** IJCAI 2024
- **Year:** 2024
- **URL:** https://www.ijcai.org/proceedings/2024/0701.pdf
- **Notes:** Introduces a benchmark using 3D simulation data evaluating LMs' qualitative spatial reasoning with natural narratives and diverse room layouts.

---

## Category 4: NPC dialogue and behavior systems

Papers covering the practical engineering of LLM-powered non-player characters, from cross-platform architectures to security concerns and persona consistency.

**1. LLM-Driven NPCs: Cross-Platform Dialogue System for Games and Social Platforms**
- **Authors:** Li Song
- **Venue:** arXiv preprint, April 2025
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2504.13928
- **Notes:** Prototype enabling LLM-powered NPCs across Unity and Discord with cloud-based memory synchronization (LeanCloud) and favorability mechanisms.

**2. Deflanderization for Game Dialogue: Balancing Character Authenticity with Task Execution in LLM-based NPCs**
- **Authors:** Pasin Buakhaw, Kun Kerdthaisong, Phuree Phenhiran, Pitikorn Khlaisamniang, Supasate Vorathammathorn, Piyalitt Ittichaiwong, Nutchanon Yongsatianchot
- **Venue:** CPDC 2025 (Commonsense Persona-Grounded Dialogue Challenge Round 2); arXiv:2510.13586v3
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2510.13586
- **Notes:** Introduces the "Deflanderization" prompting technique to suppress excessive role-play in LLM NPCs while improving task fidelity. Ranked 2nd on Task 1 and Task 3 (API track).

**3. Tricking LLM-Based NPCs into Spilling Secrets**
- **Authors:** Kyohei Shiomi, Zhuotao Lian, Toru Nakanishi, Teruaki Kitasuka
- **Venue:** ProvSec 2025 (19th International Conference on Provable and Practical Security)
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2508.19288
- **Notes:** Examines adversarial **prompt injection attacks on LLM-based NPCs** using 30 handcrafted prompts across social engineering, instructional override, and meta-prompting categories.

**4. Ubisoft Project NEO NPC (Industry Prototype)**
- **Creators:** Ubisoft Paris Studio R&D (Xavier Manzanares, Virginie Mosser, Mélanie Lopez Malet, David Louapre, Guillemette Picard); Technology: Inworld AI + NVIDIA ACE
- **Venue:** GDC 2024, March 2024; "Teammates" demo late 2025
- **Year:** 2024
- **URLs:** https://news.ubisoft.com/en-us/article/5qXdxhshJBXoanFZApdG3L/how-ubisofts-new-generative-ai-prototype-changes-the-narrative-for-npcs | https://inworld.ai/blog/ubisoft-neo-npc-prototype
- **Notes:** Industry prototype (not a formal paper) featuring NPCs with writer-crafted personalities, unscripted dialogue, real-time emotion/animation, memory, and **contextual/environmental awareness**.

**5. Fixed-Persona SLMs with Modular Memory: Scalable NPC Dialogue on Consumer Hardware**
- **Authors:** Martin Braas et al.
- **Venue:** arXiv:2511.10277 (references AAAI 2026)
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2511.10277
- **Notes:** Modular NPC dialogue using Small Language Models fine-tuned with LoRA for fixed personas, with runtime-swappable memory modules. **Memory swap times <0.03s** on consumer hardware.

**6. Character-LLM: A Trainable Agent for Role-Playing**
- **Authors:** Yunfan Shao, Linyang Li, Junqi Dai, Xipeng Qiu
- **Venue:** EMNLP 2023, pp. 13153–13187
- **Year:** 2023
- **URLs:** https://arxiv.org/abs/2310.10158 | https://aclanthology.org/2023.emnlp-main.814/
- **Notes:** Trains LLMs to act as specific historical characters using experience reconstruction. Addresses **persona consistency** and character hallucination mitigation.

---

## Category 5: Multi-agent social simulation and emergent behavior

Papers on how populations of LLM agents develop social structures, strategic behavior, and emergent collective phenomena.

**1. Language Agents with Reinforcement Learning for Strategic Play in the Werewolf Game**
- **Authors:** Zelai Xu, Chao Yu, Fei Fang, Yu Wang, Yi Wu
- **Venue:** arXiv preprint (submitted October 2023, revised May 2025)
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2310.18940
- **Notes:** Combines LLM reasoning with RL for strategic Werewolf gameplay. LLM generates diverse action candidates; RL policy selects optimal action via population-based training.

**2. Learning Strategic Language Agents in the Werewolf Game with Iterative Latent Space Policy Optimization (LSPO)**
- **Authors:** Zelai Xu, Chao Yu, Fei Fang, Yu Wang, Yi Wu
- **Venue:** ICML 2025
- **Year:** 2025
- **URLs:** https://arxiv.org/abs/2502.04686 | https://icml.cc/virtual/2025/poster/45520
- **Notes:** Maps free-form utterances to a finite latent strategy space, applies **counterfactual regret minimization** for game-theoretic optimization, then fine-tunes LLM via DPO.

**3. ProAgent: Building Proactive Cooperative Agents with Large Language Models**
- **Authors:** Ceyao Zhang, Kaijie Yang, Siyi Hu, Zihao Wang, Guanghe Li, Yihang Sun, Cheng Zhang, Zhaowei Zhang, Anji Liu, Song-Chun Zhu, Xiaojun Chang, Junge Zhang, Feng Yin, Yitao Liang, Yaodong Yang
- **Venue:** AAAI 2024, Vol. 38, No. 16, pp. 17591–17599
- **Year:** 2024
- **URLs:** https://arxiv.org/abs/2308.11339 | https://ojs.aaai.org/index.php/AAAI/article/view/29710 | https://pku-proagent.github.io/
- **Notes:** LLM-based framework with Planner, Verificator, Controller, Memory modules and Belief Revision mechanism. Outperforms 5 baselines by **>10%** in Overcooked-AI.

**4. S³: Social-network Simulation System with Large Language Model-Empowered Agents**
- **Authors:** Chen Gao, Xiaochong Lan, Zhihong Lu, Jinzhu Mao, Jinghua Piao, Huandong Wang, Depeng Jin, Yong Li
- **Venue:** arXiv preprint, July 2023
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2307.14984
- **Notes:** Pioneering LLM social network simulation modeling emotion, attitude, and interaction. Demonstrates **information propagation, attitude polarization, and emotional contagion**.

**5. SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents**
- **Authors:** Xuhui Zhou, Hao Zhu, Leena Mathur, Ruohong Zhang, Haofei Yu, Zhengyang Qi, Louis-Philippe Morency, Yonatan Bisk, Daniel Fried, Graham Neubig, Maarten Sap
- **Venue:** ICLR 2024 (Spotlight)
- **Year:** 2024
- **URLs:** https://arxiv.org/abs/2310.11667 | https://sotopia.world/
- **Notes:** Open-ended environment for simulating complex social interactions. Includes the SOTOPIA-Eval multi-dimensional evaluation framework. Even GPT-4 scores significantly lower than humans on hard social scenarios.

**6. AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents**
- **Authors:** Jinghua Piao et al. (Tsinghua University)
- **Venue:** arXiv preprint, February 2025
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2502.08691
- **Notes:** Large-scale simulator with **10,000+ agents** and 5M+ interactions. Agents have emotions, needs, and cognition. Reproduces real-world social experiments including polarization and inflammatory message spread.

---

## Category 6: Agent memory and cognitive architecture

Papers addressing how agents store, organize, and retrieve memories—from LLM-specific architectures to neuroscience-inspired spatial cognition models.

**1. Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents (AgeMem)**
- **Authors:** Yi Yu, Liuyi Yao, Yuexiang Xie, Qingquan Tan, Jiaqi Feng, Yaliang Li, Libing Wu
- **Venue:** arXiv preprint, January 2026
- **Year:** 2026
- **URL:** https://arxiv.org/abs/2601.01885
- **Notes:** Unified framework integrating LTM and STM into agent policy via tool-based actions. Uses **3-stage progressive RL with step-wise GRPO**. Outperforms baselines on five long-horizon benchmarks.

**2. MemGPT: Towards LLMs as Operating Systems**
- **Authors:** Charles Packer, Vivian Fang, Shishir G. Patil, Kevin Lin, Sarah Wooders, Joseph E. Gonzalez
- **Venue:** arXiv preprint, October 2023
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2310.08560
- **Notes:** OS-inspired virtual context management system managing different memory tiers (main context ≈ RAM, external context ≈ disk) via self-managed paging.

**3. Reflexion: Language Agents with Verbal Reinforcement Learning**
- **Authors:** Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
- **Venue:** NeurIPS 2023 (Poster)
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2303.11366
- **Notes:** Agents verbally reflect on task feedback and store reflective text in **episodic memory buffer** for improved decision-making in subsequent trials. State-of-the-art on sequential decision-making.

**4. A-MEM: Agentic Memory for LLM Agents**
- **Authors:** Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Jun-tao Tan, Yongfeng Zhang
- **Venue:** arXiv preprint, February 2025
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2502.12110
- **Notes:** Zettelkasten-style structured memory with agent-driven organization. Creates interconnected memory networks through atomic notes. Achieves **85–93% token reduction** vs. baselines.

**5. Vector-Based Navigation Using Grid-Like Representations in Artificial Agents**
- **Authors:** Andrea Banino, Caswell Barry, Benigno Uria, Charles Blundell, Timothy Lillicrap, Piotr Mirowski et al. (DeepMind)
- **Venue:** Nature, Vol. 557(7705), pp. 429–433, May 2018
- **Year:** 2018
- **URL:** https://www.nature.com/articles/s41586-018-0102-6
- **Notes:** Landmark paper. Trained recurrent network developed **spontaneous grid-like representations** for path integration. Agent surpassed expert human navigation and exhibited shortcut behaviors.

**6. Place Cells, Grid Cells, and Memory**
- **Authors:** May-Britt Moser, David C. Rowland, Edvard I. Moser
- **Venue:** Cold Spring Harbor Perspectives in Biology, 2015
- **Year:** 2015
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC4315928/
- **Notes:** Comprehensive neuroscience review of hippocampal-entorhinal spatial mapping circuits. Place cells, grid cells, head direction cells, and border cells form cognitive maps. Foundational reference for biologically-inspired spatial memory.

**7. A Non-Spatial Account of Place and Grid Cells Based on Clustering Models of Concept Learning**
- **Authors:** Love lab (multiple authors)
- **Venue:** Nature Communications, 2019
- **Year:** 2019
- **URL:** https://www.nature.com/articles/s41467-019-13760-8
- **Notes:** Proposes domain-general learning algorithm explaining both spatial and conceptual representations. Suggests medial temporal lobe uses **general-purpose algorithms** rather than navigation-specific circuits.

---

## Category 7: Evaluation methodology

Papers providing the methodological toolkit for evaluating SpatialAgent's outputs—from LLM-as-judge protocols to agent believability testing and social network analysis.

**1. GVGAI-LLM: Evaluating Large Language Model Agents with Infinite Games**
- **Authors:** Yuchen Li, Cong Lin, Muhammad Umair Nasir, Philip Bontrager, Jialin Liu, Julian Togelius
- **Venue:** arXiv preprint, August 2025
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2508.08501
- **Notes:** Video game benchmark built on GVGAI framework testing LLM reasoning via ASCII-represented arcade games. Defines **meaningful step ratio, step efficiency, and overall score** metrics. Reveals persistent LLM limitations in spatial reasoning.

**2. Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena**
- **Authors:** Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, Ion Stoica
- **Venue:** NeurIPS 2023
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2306.05685
- **Notes:** The seminal paper formalizing LLM-as-a-Judge. GPT-4 judges achieve **>80% agreement** with human preferences—matching human inter-annotator agreement. Documents position bias, verbosity bias, and self-enhancement bias.

**3. A Survey on LLM-as-a-Judge**
- **Venue:** arXiv preprint, November 2024
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2411.15594
- **Notes:** Comprehensive survey covering functionality, methodology, application, meta-evaluation, and limitations of LLM judges across five perspectives.

**4. Navigates Like Me: Understanding How People Evaluate Human-Like AI in Video Games**
- **Authors:** Stephanie Milani, Julian Juliani, Ida Momennejad et al.
- **Venue:** CHI 2023
- **Year:** 2023
- **URL:** https://dl.acm.org/doi/fullHtml/10.1145/3544548.3581348
- **Notes:** AI navigation agent that **passes the Turing Test**—human judges cannot distinguish AI from human navigation. Analyzes justifications for human-likeness assessments.

**5. Turing's Test and Believable AI in Games**
- **Authors:** Daniel Livingstone
- **Venue:** ACM Computers in Entertainment, 2006
- **Year:** 2006
- **URL:** https://dl.acm.org/doi/10.1145/1111293.1111303
- **Notes:** Classic review of Turing test applicability to game AI with proposed methodology for believability testing.

**6. Assessing Believability**
- **Authors:** Julian Togelius, Georgios N. Yannakakis, Sergey Karakovskiy, Noor Shaker
- **Venue:** In Hingston (ed.) *Believable Bots*, Springer, 2013, pp. 215–230
- **Year:** 2013
- **URL:** https://link.springer.com/chapter/10.1007/978-3-642-32323-2_9
- **Notes:** Proposes external observer assessment over participatory observation for NPC believability, with results from Mario AI Championship Turing Test track.

**7. Network Formation and Dynamics Among Multi-LLMs**
- **Authors:** Marios Papachristou, Yuan Yuan
- **Venue:** PNAS Nexus, Vol. 4, Issue 12, December 2025
- **Year:** 2025
- **URLs:** https://arxiv.org/abs/2402.10659 | https://academic.oup.com/pnasnexus/article/4/12/pgaf317/8361967
- **Notes:** Studies network formation behaviors of LLM agents. Reproduces **preferential attachment, triadic closure, and homophily** at micro level; community structure and small-world effects at macro level.

**8. Unveiling the Collective Behaviors of Large Language Model-Based Autonomous Agents in an Online Community**
- **Venue:** ScienceDirect, 2025
- **Year:** 2025
- **URL:** https://www.sciencedirect.com/science/article/pii/S2543925125000154
- **Notes:** Studies LLM agents on Chirper (AI-only social platform). Finds structured interaction networks with **power-law degree distributions** and interaction homophily, but without typical small-world characteristics.

---

## Category 8: Space Syntax computational tools

Open-source software and libraries for implementing Space Syntax computations within SpatialAgent's pipeline.

**1. depthmapX — Open-Source Space Syntax Analysis Software**
- **Developers:** Tasos Varoudis, SpaceGroupUCL (originally Alasdair Turner)
- **License:** GPLv3
- **URLs:** https://github.com/SpaceGroupUCL/depthmapX | https://spacegroupucl.github.io/depthmapX/ | https://varoudis.github.io/depthmapX/
- **Key papers:**
  - Turner, A. (2001). "Depthmap: A Program to Perform Visibility Graph Analysis." 3rd International Space Syntax Symposium, Atlanta, pp. 12–31.
  - Turner, A. (2004). "Depthmap 4: A Researcher's Handbook." Free PDF: http://discovery.ucl.ac.uk/2651/1/2651.pdf
  - Koutsolampros, P., Sailer, K., Varoudis, T., & Haslem, R. (2019). "Dissecting Visibility Graph Analysis." 12th International Space Syntax Symposium.

**2. Space Syntax Toolkit for QGIS**
- **Developers:** SpaceGroupUCL
- **URLs:** https://github.com/SpaceGroupUCL/qgisSpaceSyntaxToolkit | https://plugins.qgis.org/plugins/esstoolkit/
- **Key paper:** Gil, J., Varoudis, T., Karimi, K., & Penn, A. (2015). "The Space Syntax Toolkit: Integrating depthmapX and Exploratory Spatial Analysis Workflows in QGIS." 10th International Space Syntax Symposium. https://discovery.ucl.ac.uk/1490063/

**3. momepy — Urban Morphology Measuring Toolkit (Python)**
- **Developer:** Martin Fleischmann
- **URLs:** https://github.com/martinfleis/momepy | https://docs.momepy.org/ | https://pypi.org/project/momepy/
- **Key paper:** Fleischmann, M. (2019). "momepy: Urban Morphology Measuring Toolkit." Journal of Open Source Software, 4(43), 1807. DOI: https://doi.org/10.21105/joss.01807
- **Notes:** Part of PySAL. Built on GeoPandas and NetworkX. Supports street network analysis as primal and dual graphs, enabling **Space Syntax-style connectivity analysis**.

**4. NetworkX — Graph Analysis for Spatial Networks**
- **URLs:** https://github.com/networkx/networkx | https://networkx.org/
- **Key paper:** Hagberg, A., Schult, D. & Swart, P. (2008). "Exploring Network Structure, Dynamics, and Function using NetworkX." SciPy Proceedings.
- **Notes:** Provides foundational graph algorithms (betweenness centrality, closeness centrality, shortest paths) underlying Space Syntax computations. The **nx_spatial** extension (https://github.com/bwreilly/nx_spatial) adds GIS-oriented functionality.

**5. OSMnx — OpenStreetMap Network Analysis**
- **Developer:** Geoff Boeing
- **URL:** https://github.com/gboeing/osmnx
- **Key paper:** Boeing, G. (2017). "OSMnx: New Methods for Acquiring, Constructing, Analyzing, and Visualizing Complex Street Networks." Computers, Environment and Urban Systems, 65, 126–139.
- **Notes:** Retrieves and models OpenStreetMap street networks as NetworkX graphs. Frequently used as a **data pipeline feeding into depthmapX or momepy** for Space Syntax analysis.

**6. PySAL — Python Spatial Analysis Library**
- **URL:** https://github.com/pysal/pysal
- **Notes:** Umbrella library including esda (spatial autocorrelation), momepy, libpysal, and other spatial analysis subpackages relevant to configurational analysis.

**7. sDNA — Spatial Design Network Analysis**
- **Developers:** Cardiff University (Chiaradia, Webster, Cooper)
- **Year:** 2012
- **Notes:** Alternative spatial network analysis tool developed at Cardiff University.

**8. topologicpy**
- **Developer:** Wassim Jabi
- **Notes:** Open-source Python library implementing visibility graphs as an alternative to depthmapX for VGA.

---

## Conclusion

This collection maps the complete intellectual territory for SpatialAgent. Three strategic observations emerge for positioning the paper. First, the **gap between Categories 2 and 1 is the core contribution space**: Space Syntax agent simulation (Penn & Turner 2001) used simple rule-based agents, while LLM game agents (Park et al. 2023) lack spatial-configurational awareness—SpatialAgent bridges this 20-year divide. Second, Category 3 reveals that spatially-aware LLM agents remain extremely rare; Oh et al. (2025) is the closest precedent, but it operates in counselling rather than game environments, leaving game-oriented spatial awareness essentially unexplored. Third, the evaluation methodology can draw on an unusually rich toolkit—combining Space Syntax metrics (integration, choice, visibility) with LLM-as-Judge protocols and social network analysis creates a novel multi-layered evaluation framework that reviewers at AAAI or CHI would find compelling. The computational tools in Category 8, particularly depthmapX and momepy with NetworkX, provide a ready-made pipeline for implementing Space Syntax computations within a Python-based agent framework.