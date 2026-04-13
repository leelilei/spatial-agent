# Review of "From Navigation to Habitation: How Spatial Configuration Shapes LLM Agent Social Behavior"

**Reviewer**: Expert Reviewer (Survey / Spatial Computing / LLM Agents)  
**Date**: 2026-04-11  
**Plan Version**: `survey_plan_v2`  
**Recommendation**: Major Revision

---

## Overall Assessment

这是一份有明显潜力的 survey 计划。选题窗口是对的，问题意识也足够新：它试图把 Space Syntax 这套成熟的空间构型理论，与 LLM multi-agent social simulation 这一新兴方向连接起来。这种跨界连接如果做扎实，确实有机会形成一个有辨识度的综述。

但以“可投稿的 survey 计划”标准来看，当前版本仍有一个根本性问题：它还不像一篇 survey，更像是一个混合体，里面同时装入了 narrative review、conceptual framework、method paper，以及后续 empirical paper 的前导基础设施。这样做的风险不是“内容不够多”，而是“主线不够单一”。如果不收缩，最后论文很可能既不够像系统综述，也不够像立场文章，还会被 reviewer 追问证据边界和贡献边界。

我对这个计划的核心判断是：**题目值得做，材料也开始成形，但必须先把“论文要回答什么”与“论文最多能稳健回答什么”对齐。** 当前版本在这两点之间仍有明显张力。

---

## Strengths

### 1. 选题稀缺且有真实空白

第 1 节对 gap 的判断是有洞察力的。现有 spatial LLM 文献确实更多关注“模型能否理解空间”或“agent 如何导航”，而较少系统讨论“空间构型如何影响社会行为的生成与分布”。这个切口比单纯再做一版 spatial reasoning survey 更有辨识度。

### 2. 与 Feng et al. 的区分是有效的

第 1.3 节把“能力问题”和“效应问题”分开，这是当前计划里最清楚也最有说服力的定位动作之一。只要后续把这个差异落实到 corpus 组织方式和 claim 边界上，这会成为文章的重要入口。

### 3. 计划的素材盘点比较诚实

第 3 节没有假装“资料已齐备”，而是明确列出哪些 notes 已完整、哪些 anchor papers 还没补。这种透明度很好，也说明作者对真正的瓶颈在哪里有清醒认识。

### 4. 章节组织具备叙事潜力

`Theory -> Representation -> Capability -> Application -> Evaluation -> Agenda` 这个顺序是可写的，也有跨学科读者能跟上的潜力。它比纯按年份或纯按任务类型排列更有思想性。

---

## Major Concerns

### 1. 核心研究问题被表述成了“因果回答”，但现有文献基础更接近“证据盘点”

当前第 1.1-1.2 节将核心问题写成“空间构型如何塑造 LLM Agent 的社会行为”。这句话听起来像是 survey 可以给出实质性回答，但从第 3 节与第 5 节自己的设定看，现状恰恰是：

- `L4` 构型表征仍被定义为空白
- `H1-H3` 被描述为理论预测，尚未在 agent 中得到系统检验
- 第 4 节也主要是在论证“构型输入是否可行”，而不是总结已有因果证据

这意味着当前 corpus 最多只能稳健回答下面这类问题：

- 现有 LLM agent work 如何表征空间？
- 哪些社会行为已经被空间信息影响，哪些还没有？
- Space Syntax 哪些命题可以迁移成 AI 研究假设？
- 目前证据支持到哪一步，缺口在哪里？

换言之，**你真正能写稳的是“state of evidence + conceptual agenda”，而不是“causal answer paper”。**

**Recommendation**:

- 把主问题改写为可被 survey 回答的形式，例如：  
  `What is known, missing, and needed to study how spatial configuration may shape LLM-agent social behavior?`
- 将“空间构型塑造行为”改成更谨慎的 framing，例如“provides hypotheses, priors, and evaluation lenses”
- 在摘要与引言中提前声明：本文不是在证明该因果链已经成立，而是在建立其文献地图、表征框架与研究议程

### 2. 贡献层级过满，五个“独特贡献”目前不像一个 survey 的单一主轴

第 1.4 节同时提出：

1. `L0-L5` 分类学
2. Space Syntax 教程
3. 构型-行为因果链框架
4. `BSR/TAR` 方法论
5. 跨学科研究议程

这五项各自都能成立，但放在一篇 survey 中，它们的“主贡献地位”彼此竞争。尤其是第 4 项 `BSR/TAR`，它明显来自实证论文 `plan_v9` 的方法设计，而不是从现有 survey corpus 中自然长出来的综述性结论。结果是，这篇文章会给人一种感觉：**它在用 survey 的壳，承载一个未来研究 program 的全部部件。**

**Recommendation**:

- 强制设定主次层级
- 我建议的层级是：
  - Primary: 一个 evidence-backed 的空间表征与研究缺口框架
  - Secondary: 一个连接 Space Syntax 与 LLM multi-agent literature 的桥接叙事
  - Tertiary: 研究议程与可能的评估维度
- `BSR/TAR` 不宜作为 survey headline contribution，除非你能证明它是对现有评价文献的系统归纳与抽象；否则更适合作为 companion empirical paper 的方法资产

### 3. 计划缺少 survey methodology，本质上还没有“检索与筛选协议”

作为计划文本，当前版本已经写了主题、结构、素材来源和时间表，但还没有真正的 review protocol。尤其第 3 周的检索设计仍停留在“关键词 + 渠道”层面，没有以下关键信息：

- 时间范围
- 纳入标准与排除标准
- 如何定义“LLM agent”
- 如何区分单 agent、multi-agent、embodied agent、game NPC、social simulation
- 如何处理 position paper、benchmark paper、system paper、demo paper
- 如何进行编码与归类
- taxonomy 是从 literature inductively 归纳，还是 deductively 先验设定

没有这部分，你在引言里的强断言，比如“这两个知识体系从未被系统连接”，就会显得证据支撑不足。对于 journal 尤其如此。

**Recommendation**:

- 明确将本文定位为 `scoping review` 或 `structured narrative review`，而不是模糊的 “survey”
- 新增一节或一个附录，至少包含：
  - databases / venues / date range
  - search strings families
  - inclusion / exclusion criteria
  - screening flow
  - coding schema
  - evidence table template
- 第 4 周之前先产出一个 `evidence matrix`，再写正文，不要先写后补 protocol

### 4. `L0-L5` 分类学目前有启发性，但分类维度混杂，尚未证明它是稳健 taxonomy

第 3 节把空间表征分成 `L0-L5`，这个想法有潜力，但目前仍存在一个分类学常见问题：不同层级混入了不同维度。

当前层级里同时混合了：

- 空间信息的抽象程度
- 环境表示模态
- agent 是否 embodied
- 信息是否支持导航
- 信息是否可能影响社会行为

例如，`L5 完整 3D` 并不天然比 `L4 构型指标` “更高阶”；如果研究目标是社会行为，那么 `L4` 甚至可能比 `L5` 更贴近理论变量。换句话说，当前更像一条“表现形式梯度”，而不是真正严格的层级序列。

此外，`L4` 被定义为“空白层”，这在叙事上有效，但在 taxonomy 上会让人质疑：如果该层主要不是 literature 中已存在的大类，而是作者提出的目标设计空间，那么它究竟是“描述性分类”还是“规范性分类”？

**Recommendation**:

- 明确 taxonomy 的分类原则：到底是按 `representation format`、`structural faithfulness` 还是 `behavioral relevance`
- 考虑改成二维框架，例如：
  - x-axis: spatial representation explicitness / structure
  - y-axis: coupling to movement / social interaction
- 如果坚持 `L0-L5`，要给每层提供必要且充分的判定条件，并说明如何处理混合型系统
- 把 `L4` 明确标成 “underexplored design space” 可能比“既有层级”更稳

### 5. 第 6 节与 Phase 4 让这篇 survey 过度服务于一篇特定 empirical paper

第 6 节的 `BSR/TAR` 与第 6 部分“与实证论文的双向关系”，再加上 Phase 4 “通过 survey 回到 v9/v10”，共同构成了一个明显信号：这篇 survey 正在被设计成 `plan_v9` 的理论铺垫。

从项目管理上看，这完全合理；但从发表逻辑上看，这是危险的。一个好的 survey 应该首先服务于 field-level understanding，而不是先服务于某个具体实验设计。否则 reviewer 会自然质疑：

- 这篇 survey 是在总结领域，还是在为作者自己的实验做文献合法化？
- `BSR/TAR` 的出现，究竟是 literature-driven，还是 project-driven？

**Recommendation**:

- 在计划层面就把“field-facing contribution”和“project-facing utility”分开
- 正文里尽量少直接引用 `C1-C6m`、`v9` 这种项目内部命名
- 如果保留第 6 节，建议把它改写成 “evaluation dimensions in spatially mediated social simulation”，其中 `BSR/TAR` 只是作者提出的一种候选 operationalization，而不是整节的中心

### 6. 证据基础目前不平衡，写作顺序有“先搭楼再补地基”的风险

第 3 节素材盘点其实已经暴露出一个结构性问题：当前最扎实的是多 agent 文献，而最关键的桥梁部分，即 Space Syntax anchor texts 与 `Oh 2025`，都还处于空模板状态。换言之，最决定文章是否成立的部分，恰恰是最未完成的部分。

这会带来两个风险：

- 第 2 节可能写成“二手教程”，缺乏原始理论的精度
- 第 3 节和第 4 节可能为了支撑预设的 `L0-L5` 和“可行性”结论，而对 literature 做过度解释

**Recommendation**:

- 设立更硬的 readiness gate
- 在 `Hillier 1984 / Turner 2001 / Oh 2025` 三份 notes 完成之前，不建议进入第 5-8 周的正文写作
- 第 2 周末应先产出：
  - 一版 `Space Syntax` 概念表
  - 一版 agent systems evidence table
  - 一版 taxonomy coding memo
- 用这些中间产物驱动写作，而不是直接用章节标题驱动写作

### 7. 投稿策略没有分化，短版和长版目前不是同一篇文章的两个长度版本

第 1.5 节同时面向 `AAMAS Blue Sky / IJCAI Survey Track` 与 `ACM Computing Surveys / AI Magazine / Environment and Planning B`。但这几类 venue 的期望产物非常不同：

- `Blue Sky` 要的是 sharp vision 和 agenda
- `Survey Track` 要的是 coverage 与 synthesis
- `Computing Surveys` 要的是系统性、完整性和成熟领域整合
- `AI Magazine / EPB` 又更接受跨学科 narrative 与 perspective

当前计划试图用同一套结构去兼容所有 venue，这大概率会导致每种 venue 都“不够像它想要的那篇文章”。

**Recommendation**:

- 尽快拆成两个产品定义
- Short version:
  - 聚焦 `gap + taxonomy + agenda`
  - 砍掉大篇幅教程与方法论自创部分
- Long version:
  - 保留 `Space Syntax tutorial + evidence map + taxonomy + agenda`
  - 如果 corpus 不够成熟，不建议直接瞄准 `ACM Computing Surveys`
- 以当前选题成熟度看，我认为更现实的顺序是：
  - 先做一篇强 narrative / scoping review
  - 再视 corpus 完整度决定是否扩展成 journal version

---

## Minor Concerns

### 8. 竞争性对比对象仍然过少

当前只把 `Feng et al. (2025)` 作为主要对比对象，这在引言上可以，但在真正的 related work positioning 中不够。至少还应纳入：

- embodied AI / VLN / world-model survey
- game agent / NPC survey
- multi-agent social simulation survey
- spatial reasoning benchmark survey

否则“本 survey 的独特性”会建立在过窄的对照集上。

### 9. 还缺一张真正承载综述价值的主表

目前图表清单里有 taxonomy 图、流程图、定位矩阵，但最重要的其实应该是一张 evidence map 大表，至少覆盖：

- paper / system
- environment type
- spatial representation type
- number of agents
- social behavior type
- evaluation method
- evidence strength
- whether Space Syntax-like construct is explicit or implicit

这张表会比单纯的 `L0-L5` 阶梯图更能证明综述价值。

### 10. 时间线偏乐观

10-12 周对写出一篇可投的 narrative survey 也许够，但前提是 corpus 稳定、检索协议明确、taxonomy 已定。就当前状态看，真正需要额外预留的是“筛选与编码”时间，而不是只预留“写作周”。

---

## Verdict

**Major Revision**

这份计划最可贵的地方，是它已经找到了一个值得写的交叉口；最需要修正的地方，是它还没有决定自己到底是一篇 `survey`、一篇 `position paper`，还是一套为 empirical work 服务的文献基础设施。

如果作者愿意做以下四个关键收缩，我认为这会迅速从“有想法的计划”变成“可投稿的综述计划”：

1. 把核心问题改写为 survey 可回答的问题，而不是直接的因果命题。
2. 增补明确的 review protocol，把检索、筛选、编码方法写清楚。
3. 压缩贡献层级，把 `L0-L5 + evidence map + agenda` 作为主轴，弱化 `BSR/TAR` 的中心性。
4. 将短版与长版投稿目标拆成两套不同产品，而不是同一篇文章的长度伸缩。

---

## Suggested Path Forward

如果让我给出一个最稳妥的 v3 方向，我会建议把本文明确改造成：

**A scoping survey and research agenda on spatial representation and socially relevant spatial effects in LLM agent systems**

对应的正文主线可以收敛为：

1. 为什么“空间构型”值得进入 LLM multi-agent 讨论
2. 现有系统如何表征空间，证据覆盖到哪里
3. 哪些 Space Syntax 命题可迁移，哪些仍缺实证桥接
4. 一个谨慎的 taxonomy / evidence map
5. 一个面向后续 empirical work 的研究议程

如果按这个方向重写，这篇 survey 的成功概率会显著高于当前版本。
