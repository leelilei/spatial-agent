# Notes For `survey_plan_v4`

基于 2026-04-12 的一次快速排查整理。  
本笔记主要依据题名、摘要、目录信息和来源页元数据，不等于全文精读笔记。

## 1. 最值得直接写进 `§1.3 Relation to existing surveys` 的论文

| 论文 | 建议定位 | 可安全写入的核心点 | 不建议过度声称 |
|---|---|---|---|
| Feng et al. (2025) *Spatial Intelligence Across Scales* | 最直接的空间侧对照 | 它关心 LLM 的 spatial intelligence，覆盖 embodied、urban、earth scales。 | 不要把它写成 social simulation survey。 |
| Guo et al. (2024) *LLM-based Multi-Agents* | 多智能体总综述 | 它提供 MAS 架构、通信、任务与挑战全景。 | 不要说它专门讨论空间表征。 |
| Hu et al. (2024) *LLM-Based Game Agents* | 游戏/虚拟世界侧对照 | 它对 sandbox、NPC、multi-agent game environment 很接近你的 core corpus。 | 不要说它回答了空间对社会行为的效应问题。 |
| Gao et al. (2024) *LLM-Empowered ABM and Simulation* | 仿真总版图对照 | 它把 LLM+simulation 分为 cyber / physical / social / hybrid，是你和 ABM 社区对话的桥。 | 不要把它写成专门研究 spatial configuration。 |
| Mou et al. (2024) *Social Simulation Driven by LLM-based Agents* | 社会模拟侧最强对照 | 它从 individual / scenario / society 三层整理 LLM social simulation。 | 不要说它系统编码了空间维度。 |
| Feng et al. (2024) *Social Agents in Game-Theoretic Scenarios* | 社会推理/评估对照 | 它适合支撑 social agent、evaluation protocol、game framework。 | 不要把博弈场景等同于开放空间环境。 |
| Gu (2022), Zhang (2024), Ma (2024) | Adjacent corpus 的导航/具身背景 | 它们说明 foundation model 时代的 embodied planning、VLN、VLA 文献已经成熟。 | 不要把导航成功率直接转译为社会行为效应。 |

## 2. 一句总定位

这一组现有综述基本已经覆盖了：

- LLM agent 的总体架构
- LLM multi-agent 的协作机制
- game / sandbox 环境中的 agent 能力
- social simulation 的一般分层
- embodied / navigation / VLA 的空间能力背景

但仍没有一篇把问题收缩到：

**agent 实际可访问的空间表征是什么，以及这种空间表征如何与社会行为生成、互动结构和涌现社会效应发生关系。**

这句话很适合放进 `§1` 的 novelty statement。

## 3. 建议直接写进 `§1` 的 4 个判断

1. 现有综述要么讨论空间能力，要么讨论 multi-agent/social simulation，要么讨论导航/具身任务，但很少把“空间表征”本身作为社会行为研究的分析单位。
2. 现有综述通常按任务、架构、benchmark 或应用域组织文献，而不是按 `agent-accessible spatial representation` 组织。
3. 因此，你的切入点不是再做一篇更大的 LLM agent survey，而是把“空间输入的结构显式程度”引入为一个新的 cross-cutting review axis。
4. 截至 2026-04-12 的这轮初步排查，没有看到与 “spatial representation + social effects in LLM multi-agent systems” 完全同位的 scoping review。

## 4. 对 `§3 Evidence Map` 最有帮助的论文

| 论文 | 对应你文中的用途 |
|---|---|
| Hu et al. (2024) | 帮你补 `Core corpus` 的游戏 / sandbox / NPC 系统索引。 |
| Guo et al. (2024) | 帮你界定 multi-agent 系统家族、通信与任务组织维度。 |
| Gao et al. (2024) | 帮你把 ABM/simulation 社区的分类法接进来，尤其适合支撑“为什么要看 environment 与 representation”。 |
| Mou et al. (2024) | 很适合对照你的 `behavioral scale` 三层：个体行动、互动、社会结构。 |
| Feng et al. (2024) | 可补 social agent evaluation protocol。 |

## 5. 对 `§4 Can LLMs Process Configurational Information?` 最有帮助的论文

| 论文 | 对应你文中的用途 |
|---|---|
| Feng et al. (2025) | 最适合作为 “空间能力存在，但跨尺度且未必进入社会模拟” 的总背景。 |
| Gu et al. (2022) | 提供 VLN 的经典任务、方法和评价对象。 |
| Zhang et al. (2024) | 提供 foundation model 时代 VLN 进展。 |
| Ma et al. (2024) | 提供 VLA / embodied AI 的 action interface 背景。 |

这几篇共同支持一个谨慎表述：

LLM 或 foundation-model-based agents 已显示出一定的空间理解、导航和 action-planning 潜力，但这些证据大多来自任务完成或导航 benchmark，尚不能直接证明其能处理用于社会行为建模的 configurational input。

## 6. 对 `§2 Review Protocol` 和 Appendix 最有帮助的 scoping review 范文

| 论文 | 可借鉴点 | 为什么和你契合 |
|---|---|---|
| Silacci et al. (2026) | 明确“系统映射而非效应证明”；把 prompt、模型透明度、标准化 outcome 缺失写成方法学发现。 | 你也面临“证据仍探索性、不能做强因果结论”的问题。 |
| Leiser et al. (2025) | 在异质 LLM 文献中做 research perspective grouping；强调双人编码、附录表格和 PRISMA-ScR checklist。 | 你也需要处理异质 corpus，并把 coding manual / evidence table 外显化。 |
| Tudor Car et al. (2020) | 由于报告不充分而发展 exploratory framework；把概念分析与 scoping review 结合。 | 这和你的 L0-L5 taxonomy 很像，能为“taxonomy 从文献中长出来”提供写法参照。 |

## 7. 我建议你现在就吸收到 `survey_plan_v4` 里的改动

1. `§1.5` 不要只保留 Feng / Hu / Gao 三类；至少把 Guo (2024) 与 Mou (2024) 补进去。
2. 原表里的 “Multi-agent simulation surveys (Gao 2023)” 建议改成 `Gao et al. (2024)`，否则年份和对象都不够准。
3. 你的 novelty 句子最好从“空间能力 vs 社会效应”扩展成“三重错位”：
   - 现有 survey 多按任务/架构组织
   - 现有空间工作多看导航/能力
   - 现有社会模拟工作少把空间表征当作核心变量
4. `Phase 5` 的竞争性排查可以优先盯住 2024-2026 的 4 篇：
   - Feng et al. (2025)
   - Gao et al. (2024)
   - Mou et al. (2024)
   - Luo et al. (2025)

## 8. 一个可直接改写进正文的短段落

Recent surveys have mapped adjacent parts of the landscape, including spatial intelligence across scales, LLM-based multi-agent architectures, game agents, social simulation, and embodied navigation. Yet these reviews typically organize the literature by task, architecture, benchmark, or application domain. What remains under-specified is a cross-cutting question central to the present review: what kinds of spatial representation are actually made accessible to agents, and how those representations may shape interaction patterns and emergent social behavior in multi-agent settings.

## 9. 下一步最值得做的事

1. 精读 Feng et al. (2025)，把它和本文的差异写成一张 2 列对照表。
2. 精读 Gao et al. (2024) 与 Mou et al. (2024)，把它们的分类维度抽出来，对照你自己的 `behavioral scale` 和 corpus tiers。
3. 从 Silacci / Leiser / Tudor Car 三篇里各抄一个结构模板：
   - introduction 中如何证明 scoping review 合理
   - methods 中如何交代筛选与编码
   - discussion 中如何把“报告不充分”写成发现而不是缺点
