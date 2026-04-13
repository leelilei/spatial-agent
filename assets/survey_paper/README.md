# Survey Paper Collection

为 [docs/plans/survey_plan_v4.md](../../docs/plans/survey_plan_v4.md) 准备的相近综述论文集合。

收集日期：2026-04-12

## 说明

- 我将“类似的 scope review 文章”解释为两类：
  - 与当前选题高度相关的 survey/review 论文
  - 可直接参考写法与结构的 scoping review 论文
- 所有 PDF 均存放在 `pdfs/` 下，并已做基础文件类型校验。
- 配套笔记见 [survey_plan_v4_notes.md](./survey_plan_v4_notes.md)。
- 四篇精读卡见 `reading_notes/`。
- `phase1/` 目录用于维护当前综述的检索日志、paper list 和阶段性工作批次。

## Phase 1 工作约定

- `phase1/phase1_search_log.md`: 记录本轮数据库、query family、筛选备注与补搜说明。
- `phase1/phase1_paper_list.md`: 记录进入当前工作集的论文、tier 判断、相关性说明与本地 PDF 状态。
- `pdfs/phase1_core/`: Core corpus 的首批全文。
- `pdfs/phase1_adjacent/`: Adjacent corpus 的首批全文。
- `pdfs/phase1_foundational/`: Foundational corpus 的首批全文。

当前已生成：

- [phase1_search_log.md](./phase1/phase1_search_log.md)
- [phase1_paper_list.md](./phase1/phase1_paper_list.md)
- [phase1_candidate_pool_summary.md](./phase1/phase1_candidate_pool_summary.md)
- [phase1_assistant_prescreen_summary.md](./phase1/phase1_assistant_prescreen_summary.md)
- [phase1_manual_tier_review_sheet_2026-04-13.csv](./phase1/phase1_manual_tier_review_sheet_2026-04-13.csv)
- [phase1_manual_tier_review_sheet_summary.md](./phase1/phase1_manual_tier_review_sheet_summary.md)
- [phase1_abstract_rereview_round1_2026-04-13.csv](./phase1/phase1_abstract_rereview_round1_2026-04-13.csv)
- [phase1_abstract_rereview_round1_summary.md](./phase1/phase1_abstract_rereview_round1_summary.md)

这部分资产是“当前 survey 写作与筛选工作集”，并不替代 `assets/papers/` 的长期论文库。

## 1. 主题相近的 survey/review

| 优先级 | 本地文件 | 论文 | 类型 | 为什么相关 | 来源 |
|---|---|---|---|---|---|
| P0 | [01_Feng2025_Spatial_Intelligence_Across_Scales.pdf](./pdfs/01_Feng2025_Spatial_Intelligence_Across_Scales.pdf) | Feng et al. (2025), *A Survey of Large Language Model-Powered Spatial Intelligence Across Scales: Advances in Embodied Agents, Smart Cities, and Earth Science* | Survey | 和你的题目最贴近，直接覆盖 spatial intelligence、embodied agents、urban/smart-city 尺度。 | [arXiv](https://arxiv.org/abs/2504.09848) |
| P0 | [02_Guo2024_LLM_Multi_Agents_Survey.pdf](./pdfs/02_Guo2024_LLM_Multi_Agents_Survey.pdf) | Guo et al. (2024), *Large Language Model based Multi-Agents: A Survey of Progress and Challenges* | Survey | 可作为 LLM multi-agent systems 总体图景和 taxonomy 参考。 | [arXiv](https://arxiv.org/abs/2402.01680) |
| P0 | [03_Hu2024_LLM_Game_Agents_Survey.pdf](./pdfs/03_Hu2024_LLM_Game_Agents_Survey.pdf) | Hu et al. (2024), *A Survey on Large Language Model-Based Game Agents* | Survey | 对 sandbox、NPC、虚拟世界、多 Agent 行为很有帮助，和你的 core corpus 很接近。 | [arXiv](https://arxiv.org/abs/2404.02039) |
| P0 | [04_Gao2024_LLM_ABM_Simulation_Survey.pdf](./pdfs/04_Gao2024_LLM_ABM_Simulation_Survey.pdf) | Gao et al. (2024), *Large language models empowered agent-based modeling and simulation: a survey and perspectives* | Survey | 直接连接 LLM 与 agent-based modeling/simulation，是“社会模拟”那条线的重要桥梁文献。 | [Nature Humanities and Social Sciences Communications](https://www.nature.com/articles/s41599-024-03611-3) |
| P0 | [05_Mou2024_Social_Simulation_LLM_Agents_Survey.pdf](./pdfs/05_Mou2024_Social_Simulation_LLM_Agents_Survey.pdf) | Mou et al. (2024), *From Individual to Society: A Survey on Social Simulation Driven by Large Language Model-based Agents* | Survey | 直接覆盖 social simulation，从个体到社会的层次划分很适合对照你的 behavior scale。 | [arXiv](https://arxiv.org/abs/2412.03563) |
| P1 | [06_Feng2024_Social_Agents_Game_Theory_Survey.pdf](./pdfs/06_Feng2024_Social_Agents_Game_Theory_Survey.pdf) | Feng et al. (2024), *A Survey on Large Language Model-Based Social Agents in Game-Theoretic Scenarios* | Survey | 虽然偏 game-theoretic scenario，但对 social agent、interaction、evaluation protocol 很有参考价值。 | [arXiv](https://arxiv.org/abs/2412.03920) |
| P1 | [07_Luo2025_LLM_Agent_Methodology_Survey.pdf](./pdfs/07_Luo2025_LLM_Agent_Methodology_Survey.pdf) | Luo et al. (2025), *Large Language Model Agent: A Survey on Methodology, Applications and Challenges* | Survey | 如果你想把 spatial representation 嵌进更大的 agent methodology 讨论，这篇很适合做背景综述支撑。 | [arXiv](https://arxiv.org/abs/2503.21460) |
| P1 | [08_Gu2022_VLN_Survey.pdf](./pdfs/08_Gu2022_VLN_Survey.pdf) | Gu et al. (2022), *Vision-and-Language Navigation: A Survey of Tasks, Methods, and Future Directions* | Survey | 虽然核心是导航，但可作为 embodied / spatial environment 文献传统的背景参考。 | [ACL Anthology](https://aclanthology.org/2022.acl-long.524/) |
| P1 | [09_Zhang2024_VLN_Foundation_Models_Survey.pdf](./pdfs/09_Zhang2024_VLN_Foundation_Models_Survey.pdf) | Zhang et al. (2024), *Vision-and-Language Navigation Today and Tomorrow: A Survey in the Era of Foundation Models* | Survey | 可补 foundation models 时代的 spatial navigation / embodied planning 文献脉络。 | [arXiv](https://arxiv.org/abs/2407.07035) |
| P1 | [10_Ma2024_VLA_Embodied_AI_Survey.pdf](./pdfs/10_Ma2024_VLA_Embodied_AI_Survey.pdf) | Ma et al. (2024), *A Survey on Vision-Language-Action Models for Embodied AI* | Survey | 可作为 embodied AI 与 action interface 的补充背景，帮助界定你的 Adjacent corpus 边界。 | [arXiv](https://arxiv.org/abs/2405.14093) |

## 2. Scoping Review 写法参考

| 用途 | 本地文件 | 论文 | 为什么值得参考 | 来源 |
|---|---|---|---|---|
| 写法参考 | [11_Silacci2026_LLM_Agents_Scoping_Review.pdf](./pdfs/11_Silacci2026_LLM_Agents_Scoping_Review.pdf) | Silacci et al. (2026), *Large Language Model-Based Agents for Physical Activity and Cognitive Training: Scoping Review* | 主题是 LLM agents，且明确使用 scoping review 体裁，适合参考问题设定、纳入排除与结果分组写法。 | [JMIR AI](https://ai.jmir.org/2026/1/e80123) |
| 写法参考 | [12_Leiser2025_LLM_Architectures_Scoping_Review.pdf](./pdfs/12_Leiser2025_LLM_Architectures_Scoping_Review.pdf) | Leiser et al. (2025), *Large Language Model Architectures in Health Care: Scoping Review of Research Perspectives* | 适合参考如何在新兴、异质性很强的 LLM 领域做 corpus 分层和 research perspective synthesis。 | [JMIR](https://www.jmir.org/2025/1/e70315) |
| 写法参考 | [13_TudorCar2020_Conversational_Agents_Scoping_Review.pdf](./pdfs/13_TudorCar2020_Conversational_Agents_Scoping_Review.pdf) | Tudor Car et al. (2020), *Conversational Agents in Health Care: Scoping Review and Conceptual Analysis* | 这是比较成熟的 scoping review 例子，适合参考 PRISMA-ScR 呈现、概念分析和结果组织。 | [JMIR](https://www.jmir.org/2020/8/e17158) |

## 我建议你优先读的 5 篇

1. Feng et al. (2025) spatial intelligence across scales
2. Gao et al. (2024) LLM + ABM/simulation survey
3. Mou et al. (2024) social simulation survey
4. Guo et al. (2024) LLM multi-agents survey
5. Silacci et al. (2026) scoping review 写法参考

## Reading Notes

- [feng2025_spatial_intelligence_across_scales.md](./reading_notes/feng2025_spatial_intelligence_across_scales.md)
- [gao2024_llm_abm_simulation_survey.md](./reading_notes/gao2024_llm_abm_simulation_survey.md)
- [mou2024_social_simulation_llm_agents_survey.md](./reading_notes/mou2024_social_simulation_llm_agents_survey.md)
- [hu2024_llm_game_agents_survey.md](./reading_notes/hu2024_llm_game_agents_survey.md)
