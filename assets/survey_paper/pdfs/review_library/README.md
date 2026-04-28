# Review Library

这 13 篇不是 Phase 1 的原始筛选语料，而是背景综述库与 scoping review 写法参考。

详细写作使用方式见：

- [Survey Exemplar Usage Guide](../../../../docs/guides/survey_exemplar_usage_guide.md)
- [Survey Reference Gap Memo](../../../../docs/guides/survey_reference_gap_memo_2026-04-28.md)

当前结论：

- 这 13 篇已经足够支撑 topic/background survey positioning 与 scoping review 写法参考。
- 暂不继续找更多 generic LLM-agent / embodied-agent / social-simulation survey。
- 需要补充的是 scoping review 方法/报告规范，以及 1-2 篇计算/AI/HCI 风格成文模板，而不是再扩充背景综述库。

## Survey / Review Background

| Priority | File | Paper | Type | Why it matters | Source |
|---|---|---|---|---|---|
| P0 | [01_Feng2025_Spatial_Intelligence_Across_Scales.pdf](./01_Feng2025_Spatial_Intelligence_Across_Scales.pdf) | Feng et al. (2025), *A Survey of Large Language Model-Powered Spatial Intelligence Across Scales: Advances in Embodied Agents, Smart Cities, and Earth Science* | Survey | 最贴近当前题目，直接覆盖 spatial intelligence、embodied agents、urban/smart-city 尺度。 | [arXiv](https://arxiv.org/abs/2504.09848) |
| P0 | [02_Guo2024_LLM_Multi_Agents_Survey.pdf](./02_Guo2024_LLM_Multi_Agents_Survey.pdf) | Guo et al. (2024), *Large Language Model based Multi-Agents: A Survey of Progress and Challenges* | Survey | 可作为 LLM multi-agent systems 总体图景和 taxonomy 参考。 | [arXiv](https://arxiv.org/abs/2402.01680) |
| P0 | [03_Hu2024_LLM_Game_Agents_Survey.pdf](./03_Hu2024_LLM_Game_Agents_Survey.pdf) | Hu et al. (2024), *A Survey on Large Language Model-Based Game Agents* | Survey | 对 sandbox、NPC、虚拟世界、多 agent 行为很有帮助，和当前 core corpus 很接近。 | [arXiv](https://arxiv.org/abs/2404.02039) |
| P0 | [04_Gao2024_LLM_ABM_Simulation_Survey.pdf](./04_Gao2024_LLM_ABM_Simulation_Survey.pdf) | Gao et al. (2024), *Large language models empowered agent-based modeling and simulation: a survey and perspectives* | Survey | 直接连接 LLM 与 ABM/simulation，是社会模拟这条线的重要桥梁。 | [Nature HSS Communications](https://www.nature.com/articles/s41599-024-03611-3) |
| P0 | [05_Mou2024_Social_Simulation_LLM_Agents_Survey.pdf](./05_Mou2024_Social_Simulation_LLM_Agents_Survey.pdf) | Mou et al. (2024), *From Individual to Society: A Survey on Social Simulation Driven by Large Language Model-based Agents* | Survey | 直接覆盖 social simulation，从个体到社会的层次划分很适合对照当前 behavioral scale。 | [arXiv](https://arxiv.org/abs/2412.03563) |
| P1 | [06_Feng2024_Social_Agents_Game_Theory_Survey.pdf](./06_Feng2024_Social_Agents_Game_Theory_Survey.pdf) | Feng et al. (2024), *A Survey on Large Language Model-Based Social Agents in Game-Theoretic Scenarios* | Survey | 虽偏 game-theoretic scenario，但对 social agent、interaction、evaluation protocol 很有参考价值。 | [arXiv](https://arxiv.org/abs/2412.03920) |
| P1 | [07_Luo2025_LLM_Agent_Methodology_Survey.pdf](./07_Luo2025_LLM_Agent_Methodology_Survey.pdf) | Luo et al. (2025), *Large Language Model Agent: A Survey on Methodology, Applications and Challenges* | Survey | 适合把 spatial representation 放进更大的 agent methodology 讨论中。 | [arXiv](https://arxiv.org/abs/2503.21460) |
| P1 | [08_Gu2022_VLN_Survey.pdf](./08_Gu2022_VLN_Survey.pdf) | Gu et al. (2022), *Vision-and-Language Navigation: A Survey of Tasks, Methods, and Future Directions* | Survey | 可作为 embodied / spatial environment 文献传统的背景参考。 | [ACL Anthology](https://aclanthology.org/2022.acl-long.524/) |
| P1 | [09_Zhang2024_VLN_Foundation_Models_Survey.pdf](./09_Zhang2024_VLN_Foundation_Models_Survey.pdf) | Zhang et al. (2024), *Vision-and-Language Navigation Today and Tomorrow: A Survey in the Era of Foundation Models* | Survey | 可补 foundation models 时代的 spatial navigation / embodied planning 文献脉络。 | [arXiv](https://arxiv.org/abs/2407.07035) |
| P1 | [10_Ma2024_VLA_Embodied_AI_Survey.pdf](./10_Ma2024_VLA_Embodied_AI_Survey.pdf) | Ma et al. (2024), *A Survey on Vision-Language-Action Models for Embodied AI* | Survey | 可作为 embodied AI 与 action interface 的补充背景，帮助界定 Adjacent corpus 边界。 | [arXiv](https://arxiv.org/abs/2405.14093) |

## Scoping Review Writing References

| Use | File | Paper | Why it matters | Source |
|---|---|---|---|---|
| Writing reference | [11_Silacci2026_LLM_Agents_Scoping_Review.pdf](./11_Silacci2026_LLM_Agents_Scoping_Review.pdf) | Silacci et al. (2026), *Large Language Model-Based Agents for Physical Activity and Cognitive Training: Scoping Review* | 主题是 LLM agents，且明确使用 scoping review 体裁，适合参考问题设定、纳入排除与结果分组写法。 | [JMIR AI](https://ai.jmir.org/2026/1/e80123) |
| Writing reference | [12_Leiser2025_LLM_Architectures_Scoping_Review.pdf](./12_Leiser2025_LLM_Architectures_Scoping_Review.pdf) | Leiser et al. (2025), *Large Language Model Architectures in Health Care: Scoping Review of Research Perspectives* | 适合参考如何在新兴、异质性很强的 LLM 领域做 corpus 分层和 research perspective synthesis。 | [JMIR](https://www.jmir.org/2025/1/e70315) |
| Writing reference | [13_TudorCar2020_Conversational_Agents_Scoping_Review.pdf](./13_TudorCar2020_Conversational_Agents_Scoping_Review.pdf) | Tudor Car et al. (2020), *Conversational Agents in Health Care: Scoping Review and Conceptual Analysis* | 是比较成熟的 scoping review 例子，适合参考 PRISMA-ScR 呈现、概念分析和结果组织。 | [JMIR](https://www.jmir.org/2020/8/e17158) |

## Method / Reporting Standards and Computing Exemplars To Add

这些文献是方法、报告规范与写作模板参考，不进入 Phase 1 article screening；当前已按 `14-19` 归档，后续写方法章节和 bibliography 时补齐引用。

| Priority | Reference | Use | Status |
|---|---|---|---|
| P0 | [14_Tricco2018_PRISMA_ScR.pdf](./14_Tricco2018_PRISMA_ScR.pdf) | PRISMA-ScR 报告规范、flowchart 和 checklist 对齐 | local PDF |
| P0 | [15_Peters2024_JBI_Scoping_Reviews.pdf](./15_Peters2024_JBI_Scoping_Reviews.pdf) | PCC framing、charting、evidence mapping 方法依据 | local PDF |
| P0 | [16_Arksey2005_Scoping_Studies_Framework.pdf](./16_Arksey2005_Scoping_Studies_Framework.pdf) | 新兴领域 mapping 型综述的方法基础 | local PDF |
| P0 | [17_Levac2010_Scoping_Studies_Advancing_Methodology.pdf](./17_Levac2010_Scoping_Studies_Advancing_Methodology.pdf) | 迭代式 scoping review、numerical summary 与 thematic synthesis | local PDF |
| P1 | [18_Bevilacqua2025_Human_Centered_AI_Scoping_Review.html](./18_Bevilacqua2025_Human_Centered_AI_Scoping_Review.html) | AI/HCI 风格 scoping review；参考 PRISMA-ScR、OSF protocol、IEEE Xplore search 和 design-method charting | local PMC HTML; JMIR PDF direct link returned 403 |
| P1 | [19_Feliciani2019_Simulation_Models_Peer_Review_Scoping_Review.pdf](./19_Feliciani2019_Simulation_Models_Peer_Review_Scoping_Review.pdf) | 计算社会科学/仿真模型 scoping review；参考异质 simulation / ABM 文献如何转 taxonomy | local PDF |

Reserve only:

- Peters et al. (2015), *Guidance for conducting systematic scoping reviews*, DOI `10.1097/XEB.0000000000000050`
- Wohlgemut et al. (2024), *A scoping review, novel taxonomy and catalogue of implementation frameworks for clinical decision support systems*, DOI `10.1186/s12911-024-02739-1`
- Sousa et al. (2026), *The landscape of artificial intelligence tools and platforms for evidence synthesis: a scoping review*, DOI `10.1186/s13643-025-02842-y`

## How To Use These Exemplars

最低限度图表集：

- `Table 1`: multi-survey positioning matrix，参考 `01-10` 的 survey scope 与本 README 的定位表。
- `Figure 1`: corpus/evidence-role diagram，区分 `anchor_core`、`bridge_core`、`Adjacent`、`Foundational`。
- `Figure 2`: PRISMA-ScR flowchart，参考 `11`、`12` 与 PRISMA-ScR。
- `Figure 3`: `L0-L5` taxonomy diagram，参考 `01` 的跨尺度图式和 `07` 的 taxonomy overview。
- `Table 3`: core evidence map，参考 `11`、`12` 的结果表组织方式。
- `Table 4`: environment-side vs agent-accessible examples，用于解释为什么 3D backend 不自动等于 `L5`。
- `Table 6`: Space Syntax proposition transfer table，明确 physical-space 命题只是可迁移假设。
- `Table 7`: evaluation dimension table，定义行为、表示层级、baseline 和证据强度。

章节参考口径：

- `§1 Introduction`: 用 `01-05` 证明邻近 survey 已经很多，缺口是 agent-accessible spatial representation 与 social behavior 的连接。
- `§2 Space Syntax Primer`: 以 Space Syntax foundational sources 为主，`01` 只作 AI bridge。
- `§3 Evidence Map`: 参考 `11-13` 的 scoping review reporting，展示 corpus、PRISMA、L0-L5、evidence map 和 counts。
- `§4 Feasibility`: 用 `01`、`08`、`09`、`10` 支撑“模型可消费更丰富空间输入”的可行性，不支撑 social-effect 强 claim。
- `§5 Space in LLM Social Simulation`: 用 `03-06` 总结当前 social simulation 中的空间使用方式。
- `§6 Evaluation`: 用 `06`、`07`、`11`、`12` 组织 evaluation dimensions 和 evidence-strength 约束。
- `§7 Research Agenda`: 只把前文缺口转成议程，不引入新的 unsupported literature thread。

## Suggested Reading Order

1. `01` Feng 2025 spatial intelligence across scales
2. `04` Gao 2024 LLM + ABM / simulation survey
3. `05` Mou 2024 social simulation survey
4. `02` Guo 2024 LLM multi-agents survey
5. `11` Silacci 2026 scoping review writing reference
