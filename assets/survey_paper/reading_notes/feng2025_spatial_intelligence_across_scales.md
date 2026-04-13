# A Survey of Large Language Model-Powered Spatial Intelligence Across Scales

## 基本信息
- **作者**: Jie Feng, Jinwei Zeng, Qingyue Long, Hongyi Chen, Jie Zhao, Yanxin Xi, Zhilun Zhou, Yuan Yuan, Shengyuan Wang, Qingbin Zeng, Songwei Li, Yunke Zhang, Yuming Lin, Tong Li, Jingtao Ding, Chen Gao, Fengli Xu, Yong Li
- **发表**: arXiv preprint（2025年4月）
- **链接**: https://arxiv.org/abs/2504.09848
- **本地 PDF**: `assets/survey_paper/pdfs/01_Feng2025_Spatial_Intelligence_Across_Scales.pdf`
- **阅读日期**: 2026-04-13

## 一句话总结

这篇综述试图把 LLM spatial intelligence 放到跨尺度框架里统一理解，从基础能力一直连到 embodied、urban、earth 三个应用层级，是你写 `§1` 和 `§4` 时最需要正面对话的一篇相邻综述。

## 核心贡献（3点以内）
1. **跨尺度框架**：把 spatial intelligence 组织为从基础能力到真实世界应用的连续谱，而不是只盯 embodied navigation。
2. **能力分解**：把基础能力拆成 `spatial memory / knowledge` 与 `abstract spatial reasoning` 两块。
3. **应用版图扩展**：将真实世界应用划分为 `embodied spatial intelligence`、`urban spatial intelligence` 和 `earth spatial intelligence`。

## 方法 / 结构

- 从 **human spatial cognition** 切入，讨论 cognitive map、schema 等认知基础。
- 提出一个总 taxonomy：
  - **Foundational capabilities**:
    - spatial memory and knowledge
    - abstract spatial reasoning
  - **Real-world applications**:
    - embodied
    - urban
    - earth
- 最后单列 **Challenges and Discussions**，并讨论它与 **world model** 的关系。

## 关键发现 / 结论

- 这篇文章的核心问题是：空间智能并不只属于 embodied AI，而是跨越从室内导航到城市再到地球尺度的多层级研究对象。
- 它认为当前评估存在明显碎片化问题：很多工作只在特定任务、单一尺度或单一领域评估 spatial intelligence，缺少统一评价框架。
- 在基础能力层面，它特别强调：
  - LLM 已经显示出一定的 spatial memory / knowledge 能力
  - LLM 在 qualitative、geometric、graph-based spatial reasoning 上已有系统评测
  - 但多跳推理、复杂规划和统一评测仍然是瓶颈
- 在挑战部分，它明确提出一个很适合你借用的判断：
  - 目前最关键的问题之一，是空间推理到底应主要由语言形式承载，还是需要 graph-based / multimodal representations

## 与我们工作的关系
- **可借鉴**:
  - 可作为 `§1.5` 中最直接的对照对象，帮助你说明“它看空间能力，我们看空间表征对社会行为的效应”。
  - 可作为 `§4 Can LLMs Process Configurational Information?` 的背景支撑，用来证明 LLM 空间能力研究已经形成相对独立的文献簇。
  - 它把 urban intelligence 单独拉出来，这一点对你很重要，因为你的题目正好站在 urban/spatial/social 的交叉带。
- **我们的差异化**:
  - 它的组织轴是 `能力 -> 多尺度应用`，不是 `agent-accessible representation -> social effects`。
  - 它关心 spatial intelligence 的总体图景，不把社会行为生成、互动结构、涌现秩序作为中心问题。
  - 它没有把“Agent 实际接收到何种空间表征”做成主分析单位，更没有像你这样提出 L0-L5 分类学。
- **可引用的具体论点**:
  - 现有 spatial intelligence 研究跨越 embodied、urban、earth 多尺度，但缺少统一框架。
  - 当前通行工作常围绕任务或尺度组织，而非围绕 representation 组织。
  - 统一评估 general spatial intelligence 仍然是开放问题。

## 对 `survey_plan_v4` 最直接的用途

- **用于 `§1 Introduction`**:
  - 写成“最邻近但不重合”的 survey。
  - 用来强调你的问题不是 “LLM 能不能理解空间”，而是 “空间表征进入 agent 后会如何影响社会行为”。
- **用于 `§4`**:
  - 为 “LLM 处理构型输入的可行性” 提供外围证据。
  - 但要谨慎写，不能把它对 spatial intelligence 的讨论直接当成 configurational social simulation 的证据。

## 值得记住的图 / 表

- **Figure 1**: 多尺度 spatial intelligence 总图，从 embodied 到 urban 再到 earth。
- **Figure 2**: taxonomy 图，最适合拿来对比你自己的 L0-L5 分类学。
- **Section 5 Challenges and Discussions**: 很适合引用其中关于统一评估与 representation form 的讨论。

## 疑问 / 待确认

- 它提到 urban intelligence，但需要后续精读确认：其中“urban”究竟更多是 GIS / mobility / geospatial LLM，还是已经触及社会互动层面。
- 它谈到 schema learning 与 spatial syntax integration 的挑战，这一点值得二次确认，可能会对你的 `§2` 和 `§4` 都有帮助。
