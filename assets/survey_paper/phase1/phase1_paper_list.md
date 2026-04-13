# Phase 1 Paper List

日期：2026-04-13  
状态：`v0` 首批工作清单  
说明：以下是依据 `survey_plan_v4.md` 的 5 族 query 整理出的首批高优先级工作清单。它是从更大的 `417` 篇 candidate pool 中抽出的 `priority seed list`，方便优先下载 PDF、先行阅读和先做 system-level 预判。`Tier guess` 仅代表当前工作判断，后续以 `screening_sheet.csv` 的正式筛选为准。

## Core Candidates

| ID | Query | Tier guess | Year | Paper | Why it is in the batch | Source | Local PDF |
|---|---|---|---|---|---|---|---|
| C01 | D | core | 2023 | Generative Agents: Interactive Simulacra of Human Behavior | 当前最关键的基线系统；直接关系到 L2/L3 边界和社会行为生成。 | [arXiv](https://arxiv.org/abs/2304.03442) | [PDF](../pdfs/phase1_core/01_Generative_Agents_Park2023.pdf) |
| C02 | B, D | core | 2024 | Affordable Generative Agents | 是 `Generative Agents` 路线的重要扩展，适合比较环境交互与社会行为是否被压缩。 | [arXiv](https://arxiv.org/abs/2402.02053) | [PDF](../pdfs/phase1_core/02_Affordable_Generative_Agents_Yu2024.pdf) |
| C03 | D | core | 2024 | Project Sid: Many-agent simulations toward AI civilization | 大规模 Minecraft 社会模拟，适合编码 `agent_count`、role differentiation 和 environment-side / agent-side gap。 | [arXiv](https://arxiv.org/abs/2411.00114) | [PDF](../pdfs/phase1_core/03_Project_Sid_Altera2024.pdf) |
| C04 | D | core | 2024 | Artificial Leviathan: Exploring Social Evolution of LLM Agents Through the Lens of Hobbesian Social Contract Theory | 典型 sandbox society 条目，适合观察空间环境与冲突/合作/秩序形成是否耦合。 | [arXiv](https://arxiv.org/abs/2406.14373) | [PDF](../pdfs/phase1_core/04_Artificial_Leviathan_Dai2024.pdf) |
| C05 | B, D | core | 2023 | Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia | 是“空间环境 + 社会模拟 + GABM”桥梁文献，值得优先进入方法链。 | [arXiv](https://arxiv.org/abs/2312.03664) | [PDF](../pdfs/phase1_core/05_Concordia_Vezhnevets2023.pdf) |
| C06 | D | core | 2024 | OASIS: Open Agent Social Interaction Simulations with One Million Agents | 代表大规模数字社会平台环境，可测试“数字空间是否可视为可识别环境配置”。 | [arXiv](https://arxiv.org/abs/2411.11581) | [PDF](../pdfs/phase1_core/06_OASIS_Yang2024.pdf) |
| C07 | D | core | 2025 | AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society | 代表更大规模社会模拟平台，适合编码宏观 emergent social structure。 | [arXiv](https://arxiv.org/abs/2502.08691) | [PDF](../pdfs/phase1_core/07_AgentSociety_Piao2025.pdf) |
| C08 | D | core-candidate | 2024 | Unveiling the Truth and Facilitating Change: Towards Agent-based Large-scale Social Movement Simulation | 社会运动与平台互动方向的重要候选，需要在 screening 中确认其“空间环境”是否足够明确。 | [ACL Anthology](https://aclanthology.org/2024.findings-acl.285/) | [PDF](../pdfs/phase1_core/08_SoMoSiMu_Mou2024.pdf) |

## Adjacent Candidates

| ID | Query | Tier guess | Year | Paper | Why it is in the batch | Source | Local PDF |
|---|---|---|---|---|---|---|---|
| A01 | D | adjacent | 2023 | AgentSims: An Open-Source Sandbox for Large Language Model Evaluation | 虽以 evaluation sandbox 为主，但提供“环境化评测”的方法边界。 | [arXiv](https://arxiv.org/abs/2308.04026) | [PDF](../pdfs/phase1_adjacent/01_AgentSims_Lin2023.pdf) |
| A02 | C | adjacent | 2026 | SARAH: Spatially Aware Real-time Agentic Humans | 更接近 embodied / conversational motion，但能帮助定义高保真空间感知与本综述边界。 | [arXiv](https://arxiv.org/abs/2602.18432) | [PDF](../pdfs/phase1_adjacent/02_SARAH_Ng2026.pdf) |
| A03 | C | adjacent | 2024 | Advancing Spatial Reasoning in Large Language Models: An In-Depth Evaluation and Enhancement Using the StepGame Benchmark | 代表纯空间推理 benchmark 路线，用于限定 “capability != social effect”。 | [arXiv](https://arxiv.org/abs/2401.03991) | [PDF](../pdfs/phase1_adjacent/03_StepGame_Spatial_Reasoning_Li2024.pdf) |
| A04 | C | adjacent | 2024 | SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities | 代表 VLM / embodied spatial reasoning 能力边界。 | [arXiv](https://arxiv.org/abs/2401.12168) | [PDF](../pdfs/phase1_adjacent/04_SpatialVLM_Chen2024.pdf) |
| A05 | C | adjacent | 2024 | Reframing Spatial Reasoning Evaluation in Language Models: A Real-World Simulation Benchmark for Qualitative Reasoning | 帮助讨论“simulation benchmark 与真实环境抽象”的关系。 | [IJCAI](https://www.ijcai.org/proceedings/2024/701) | [PDF](../pdfs/phase1_adjacent/05_Reframing_Spatial_Reasoning_Evaluation_Li2024.pdf) |
| A06 | C, E | adjacent | 2023 | Language Models Represent Space and Time | 代表 LLM 内部世界模型/表示层证据，适合放在 Adjacent 作为能力边界。 | [arXiv](https://arxiv.org/abs/2310.02207) | [PDF](../pdfs/phase1_adjacent/06_Language_Models_Represent_Space_Time_Gurnee2023.pdf) |
| A07 | C | adjacent-candidate | 2025 | When LLMs Recognize Your Space: Research on Experiences with Spatially Aware LLM Agents | 与空间感知体验直接相关，但当前先保留元数据，等待公开预印本或全文渠道确认。 | [DOI](https://doi.org/10.1109/TVCG.2025.3616809) | Metadata only |

## Foundational Candidates

| ID | Query | Tier guess | Year | Paper | Why it is in the batch | Source | Local PDF |
|---|---|---|---|---|---|---|---|
| F01 | E | foundational | 1984 | The Social Logic of Space | 这是整篇 survey 的经典理论锚点；当前以书籍来源和阅读笔记引用，不强制复制全书 PDF。 | [DOI](https://doi.org/10.1017/CBO9780511597237) | Metadata only |
| F02 | E | foundational | 2001 | From Isovists to Visibility Graphs: A Methodology for the Analysis of Architectural Space | Visibility graph 是后续 configurational discussion 的关键桥梁。 | [DOI](https://doi.org/10.1068/b2684) | [PDF](../pdfs/phase1_foundational/01_From_Isovists_to_Visibility_Graphs_Turner2001.pdf) |
| F03 | A | foundational | 2001 | Space Syntax Based Agent Simulation | 是 space syntax 与 agent simulation 直接接轨的早期关键条目。 | [UCL Discovery](https://discovery.ucl.ac.uk/2027/) | [PDF](../pdfs/phase1_foundational/02_Space_Syntax_Based_Agent_Simulation_Penn2001.pdf) |
| F04 | A | foundational | 2017 | Assisted Agent-Based Simulations | 可帮助连接 configurational analysis 与模拟辅助设计。 | [UCL Discovery](https://discovery.ucl.ac.uk/id/eprint/1571698/) | [PDF](../pdfs/phase1_foundational/03_Assisted_Agent_Based_Simulations_Koutsolampros2017.pdf) |
| F05 | A, E | foundational | 2022 | Integrating Space Syntax with Spatial Interaction: The Spatial Metrics Problem | 适合做“空间指标如何迁移到模拟与交互分析”的方法论桥梁。 | [UCL Discovery](https://discovery.ucl.ac.uk/id/eprint/10155554/) | [PDF](../pdfs/phase1_foundational/04_Integrating_Space_Syntax_with_Spatial_Interaction_Batty2022.pdf) |
| F06 | E | foundational | 1996 | Space is the Machine: A Configurational Theory of Architecture | 作为 `The Social Logic of Space` 之后的扩展理论书，可支持 §2 primer 的结构化写法。 | [Official site](https://spaceisthemachine.com/) | [PDF](../pdfs/phase1_foundational/05_Space_is_the_Machine_Hillier1996.pdf) |

## 备注

- `core-candidate` / `adjacent-candidate` 表示当前保留进入工作集，但是否最终纳入仍需过正式 screening。
- 同一家族系统后续会在 `systems_master` 阶段做 `merge / split`，本表先按 paper 维度保留。
- 完整 candidate pool 见 `phase1_candidate_pool_2026-04-13.csv` 与 `phase1_screening_backlog_2026-04-13.csv`。
