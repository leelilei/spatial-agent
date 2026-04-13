# From Individual to Society: A Survey on Social Simulation Driven by Large Language Model-based Agents

## 基本信息
- **作者**: Xinyi Mou, Xuanwen Ding, Qi He, Liang Wang, Jingcong Liang, Xinnong Zhang, Libo Sun, Jiayu Lin, Jie Zhou, Xuanjing Huang, Zhongyu Wei
- **发表**: arXiv preprint（2024年12月）
- **链接**: https://arxiv.org/abs/2412.03563
- **本地 PDF**: `assets/survey_paper/pdfs/05_Mou2024_Social_Simulation_LLM_Agents_Survey.pdf`
- **阅读日期**: 2026-04-13

## 一句话总结

这篇综述是你“社会行为”这一半最重要的对照文献，它把 LLM-driven social simulation 按 `individual / scenario / society` 三层展开，和你计划里的 `behavioral scale` 非常容易形成对照关系。

## 核心贡献（3点以内）
1. **三层分类法**：提出 `Individual Simulation / Scenario Simulation / Society Simulation` 的渐进式框架。
2. **模块化比较**：分别总结每一层常见的 architecture、scenario / objective 和 evaluation 方法。
3. **趋势梳理**：总结 social simulation 从早期原型到多阶段、多主体、规模化和多模态的发展趋势。

## 方法 / 结构

- 文章把 social simulation 分成三类：
  - **Individual Simulation**: 模拟特定个体或某类人群
  - **Scenario Simulation**: 在具体场景里组织多 Agent 协作或完成任务
  - **Society Simulation**: 在更复杂的 agent society 中研究宏观动态
- 对应结构分别讨论：
  - architecture / key components
  - scenario / objectives
  - evaluation
- 还专门整理了 **datasets and benchmarks**，并在最后讨论整个领域的时间演化趋势。

## 关键发现 / 结论

- 这篇文章最有价值的地方，是它把社会模拟看成一个从 **细粒度个体建模** 到 **大规模社会动态** 的连续谱。
- 它明确指出三类 simulation 之间不是并列关系，而是带有递进关系：
  - individual 是基础
  - scenario 引入组织化协作
  - society 指向复杂互动和涌现结构
- 在趋势部分，它认为：
  - individual simulation 正从粗粒度人格模拟走向情境化模拟
  - scenario simulation 正从简单任务走向 multi-stage 和协作型场景
  - society simulation 正从 preliminary environments 走向规模化与多模态
- 这对你很有帮助，因为它说明“社会行为”本身已经有层级结构，但空间变量仍未被系统嵌入这套框架。

## 与我们工作的关系
- **可借鉴**:
  - 它的三层分类很适合与你的 `behavioral scale` 对照：
    - `local action` 约对应 individual / 微观决策
    - `interaction` 约对应 scenario 中的小规模协作与对话
    - `emergent social structure` 约对应 society simulation
  - 它对 evaluation 和 dataset 的整理，可作为你后续 evidence table 的补充参考。
  - 它提供了一条更稳妥的论证路径：你不是在发明 social simulation，而是在已有 social simulation 文献上补入空间表征维度。
- **我们的差异化**:
  - 它的中心问题是 social simulation 的总体分类，不是空间如何调制社会行为。
  - 它虽然覆盖 society simulation，但没有把 spatial representation 当作 organizing principle。
  - 它的 progression 轴是 `individual -> scenario -> society`，而你的轴是 `representation -> behavior coupling`。
- **可引用的具体论点**:
  - social simulation 可被组织为 individual、scenario、society 三层。
  - 这三层之间具有从细粒度个体到宏观社会现象的递进关系。
  - 当前领域趋势正在走向更复杂环境、更高规模和多模态集成。

## 对 `survey_plan_v4` 最直接的用途

- **用于 `§1.5`**:
  - 可作为“社会模拟侧最接近但仍不重合”的综述来对照。
- **用于 `§3` / `§5`**:
  - 能帮助你定义并解释 `behavioral scale`，避免它看起来像完全主观设定。
- **用于 `§7 Research Agenda`**:
  - 它的趋势分析很适合支撑“未来研究正在变复杂，但空间维度仍未被系统化”的判断。

## 值得记住的图 / 表

- **Figure 1**: 三层 simulation 关系图，是全文最重要的结构图。
- **Individual / Scenario / Society** 三节的分层结构：很适合转译到你自己的 evidence map。
- **Trend of Social Simulations**: 可为你的 research agenda 提供时间演化线索。

## 疑问 / 待确认

- 它的 society simulation 文献中，有多少真正包含“空间环境”，需要你后续精读后再筛。
- 它的 individual / scenario / society 三层与您当前 `local action / interaction / emergent social structure` 的映射关系还需要在正文中谨慎措辞，最好写成“approximately aligns with”而不是完全等同。
