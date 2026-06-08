# Review of "Where Agents Dwell: A Scoping Review of Spatial Representation and Its Social Effects in LLM Multi-Agent Systems"

**Reviewer**: Expert Reviewer (Survey / Spatial Computing / LLM Agents)  
**Date**: 2026-04-11  
**Plan Version**: `survey_plan_v3`  
**Recommendation**: Minor Revision

---

## Overall Assessment

这一版是一次实质性的改进。相较于 `survey_plan_v2`，作者已经回应了上一轮评审中的大多数关键问题：研究问题从因果命题收缩为 scoping question，文章类型从模糊的 survey 收敛为 `scoping review + structured research agenda`，review protocol 被显式加入，贡献层级被压缩，`BSR/TAR` 也被降级为候选评估维度而不再占据 headline 位置。

更重要的是，`v3` 已经不再像一个“用综述包装未来实验计划”的混合体，而开始像一篇真正可以执行的综述计划。`evidence map` 现在是中心，`L0-L5` 被定位为分析工具，`L4` 被谨慎地标为 `underexplored design space`，这些都是正确的方向。

我的总体判断是：**这份计划现在已经可信，且具备开工条件；剩下的问题不再是“要不要重写定位”，而是“如何让 corpus、编码单位和证据强度设计足够严谨，以支撑最后的 claim”。**

---

## Major Improvements Over v2

### 1. 研究问题与证据边界已经对齐

第 1.1 节现在明确声明本文不回答“空间构型是否塑造 Agent 社会行为”这一因果命题，而是回答 `what is known / missing / needed` 的 scoping 问题。这是最关键也最正确的修正。

### 2. 文章类型终于稳定下来

第 1.2 节把本文界定为 `Scoping review + structured research agenda`，并明确它不是什么。这一点大幅降低了 reviewer 对 contribution 边界的困惑。

### 3. 贡献层级明显更健康

第 1.4 节把文章收敛到三层贡献，并明确降级 `BSR/TAR` 与 “Space Syntax 教程”。这使文章更像综述，而不是 research program 的部件集合。

### 4. Review protocol 的加入非常关键

第 2 节现在已经有数据库、检索字符串、时间范围、纳排标准、筛选流程、编码方案。这让“evidence map”不再只是一个叙事承诺，而是有了方法基础。

### 5. `L0-L5` 的表述比上一版稳健得多

第 2.6 节已经明确：该分类基于 `structural explicitness`，不是技术复杂度，也不是质量排序；`L4` 是 `underexplored design space` 而非虚构的已存在类别。这一修正很重要。

### 6. 短版与长版投稿策略终于区分开了

第 5 节不再把不同 venue 当作同一篇文章的长度伸缩，而是当作两个不同产品。这是成熟很多的写法。

---

## Remaining Major Concerns

### 1. 三类文献的“证据角色”仍然没有完全分开

当前计划将以下三类材料同时纳入整体叙事：

- Space Syntax 经典理论与实证文献
- LLM spatial reasoning / benchmark 文献
- LLM multi-agent social simulation systems

这三类材料都必要，但它们在文章中的证据角色并不相同：

- Space Syntax 文献提供理论与可迁移命题
- spatial reasoning 文献提供可行性边界
- multi-agent systems 文献才是 `evidence map` 的核心对象

如果不把这三类 corpus 在方法和结果层明确分层，最后很容易出现一种叙事滑移：读者会把来自 Space Syntax 或 benchmark 的证据，误读成对 LLM multi-agent 社会行为的直接证据。

**Recommendation**:

- 在 protocol 中显式区分 `core corpus` 与 `contextual corpus`
- 建议至少分成三层：
  - Core corpus: LLM multi-agent systems with identifiable spatial environments and social behavior
  - Adjacent corpus: spatial reasoning / spatially-aware agent papers
  - Foundational corpus: Space Syntax theory and empirical findings
- `evidence map` 只对 core corpus 做结构化主编码
- 其余两类文献可做 narrative synthesis 或 supplementary tables

### 2. 证据表的分析单位仍不够清楚：是“论文”、还是“系统”？

第 2.5 节目前把编码对象写成“每篇纳入论文”。但本文真正想比较的，很大程度上是**系统如何表示空间**，而不是论文如何写作。现实中常会出现：

- 一个系统对应多篇论文
- 一篇论文报告多个设置或多个环境
- 同一系统在不同版本中空间表示不同

如果编码单位停留在 paper-level，`evidence map` 容易混淆“系统数量”和“论文数量”，也容易重复计算同一家族系统。

**Recommendation**:

- 在 protocol 中增加一个字段，明确 `unit of analysis`
- 我建议：
  - bibliographic screening 以 paper 为单位
  - evidence map 以 system / environment configuration 为单位
  - 每个系统条目再挂接对应论文引用
- 对于多版本系统，增加 `system family` 字段，避免一类系统在大表里被误当成多个独立证据点

### 3. “空间表征”还需要区分 environment state 与 agent-facing input

`v3` 比 `v2` 前进了一大步，但第 2.6 节的 `L0-L5` 在执行时仍会遇到一个硬问题：**系统里存在什么空间信息**，和 **Agent 实际被提供什么空间信息**，并不是一回事。

例如：

- 某个 3D simulator 内部当然有完整几何
- 但 LLM agent 可能只收到房间名称、对象列表或局部文本描述
- 某些系统有拓扑图，但 agent 并不直接访问，只是通过工具接口间接行动

如果不区分这两层，`L5` 很可能被高估，`L3/L4` 也可能被误判。

**Recommendation**:

- 将空间编码拆成两个字段：
  - `environment-side representation`
  - `agent-accessible representation`
- `L0-L5` 只用于后者，也就是 Agent 实际可用的输入结构
- 在表里另外增加一列记录 environment backend 是否更丰富，以解释“环境有几何，不代表 agent 有几何输入”

### 4. “社会行为”与“空间-行为耦合”两个编码维度目前仍偏粗

第 2.5 节把 `对话 / 合作 / 冲突 / 移动选择 / 角色分化 / 无` 放在同一列，把 `none / implicit / explicit` 放在另一列。这是一个可行起点，但还不够支撑后续强结论。

原因在于，这里面混在一起的是不同层次的现象：

- `移动选择` 更接近局部决策行为
- `对话/合作/冲突` 更接近社会互动形式
- `角色分化` 更接近宏观涌现结果

如果这些都在一个平面上编码，文章很容易把“空间影响了移动机会”与“空间影响了社会结构”混写成同一种 evidence。

**Recommendation**:

- 将行为相关编码至少拆成两列：
  - `behavioral scale`: local action / interaction / emergent social structure
  - `behavior type`: dialogue / cooperation / conflict / mobility / role differentiation / etc.
- 再增加一列 `evidence status`：
  - observed effect
  - designed affordance only
  - hypothesized but not tested
- 这样第 5 节在讨论“空间如何中介社会行为”时，才不会把不同证据强度混成一类

### 5. 单人编码下，taxonomy 的可靠性仍需一个最小化质量控制方案

scoping review 不必像医学系统综述那样要求严格双人筛选，但当前计划把 `L0-L5` taxonomy 放在比较核心的位置，因此分类一致性本身会成为 reviewer 追问点。

当前版本有 protocol，但还没有写出任何质量控制步骤，例如：

- 重复筛选或回看
- 难判样本的裁决规则
- 外部审阅者抽查
- 版本化记录 taxonomy 边界调整

**Recommendation**:

- 增加一个轻量但明确的 quality-control 方案
- 例如：
  - 标题摘要筛选完成后，随机抽取 10-15% 做二次复核
  - `L0-L5` 分类中最模糊的 10 篇，形成 adjudication memo
  - 邀请一位合作者或导师对一小部分编码样本进行 independent audit
- 不必把它写成正式 inter-rater study，但要让读者知道 taxonomy 不是一次性拍脑袋完成的

### 6. 第 2 章的 Space Syntax primer 仍有“过重”风险

虽然 `v3` 已明确它不是 headline contribution，但当前第 2 章仍计划写 `2500-3500` 字，并附 `Appendix C: Space Syntax Computation Reference`。对于一篇以 evidence map 为中心的 scoping review，这仍然可能偏重。

风险不是“这章不该有”，而是它可能重新占据文章重心，让论文从“map the AI literature”滑回“teach Space Syntax to AI readers”。

**Recommendation**:

- 将第 2 章严格限制为服务后文所必需的最小理论底座
- 只保留：
  - 核心概念
  - 最相关的 2-4 个指标
  - 最直接可迁移的命题
  - 明确的 boundary conditions
- `Appendix C` 若篇幅吃紧，可以删掉或压缩成简表
- 主文中要持续提醒：Space Syntax 在本文中的作用是解释变量来源，而不是另一篇独立综述

---

## Minor Concerns

### 7. 短版产品的 venue 组合仍略显异质

`AAMAS Blue Sky / IJCAI Workshop / CHI alt.chi` 对文章气质的要求并不相同。内部计划里列多个备选没有问题，但真正开始写 short version 时，仍建议尽早选定一个主场景，否则文风会再次分裂。

### 8. 检索字符串还可以再补一些常见变体

尤其 LLM agent 这部分，可考虑补充：

- `virtual world`
- `sandbox`
- `NPC`
- `social agent`
- `interactive simulacra`

否则可能漏掉一部分并不自称 `multi-agent social simulation` 的相关系统论文。

### 9. “预计 300-500 篇 → 40-60 篇编码集”的压缩比例需要留痕

这个数量级大体合理，但最好在 protocol 中预先说明典型排除原因类别，方便后续 PRISMA-ScR 图真正落地，而不是只给一个数字区间。

---

## Verdict

**Minor Revision**

`survey_plan_v3` 已经明显跨过了上一版最危险的阶段。它现在具备了清晰的问题边界、合理的综述类型、较好的贡献层级，以及一个可以执行的 protocol。换句话说，这已经不是“先别写”的状态，而是“可以开始做，但要在编码设计上再补几块承重墙”的状态。

如果作者在进入大规模编码之前完成以下四项修正，我认为这份计划就已经足够稳：

1. 明确区分 `core corpus`、`adjacent corpus` 与 `foundational corpus`
2. 明确 evidence map 的分析单位是 `system` 还是 `paper`
3. 将空间编码拆分为 `environment-side` 与 `agent-accessible` 两层
4. 给 taxonomy 编码加入最小化质量控制步骤

---

## Suggested Next Step

如果只做一个最有价值的补强动作，我建议优先新增一页 `coding manual`，内容包括：

- unit of analysis
- corpus tiering
- L0-L5 决策规则
- ambiguous-case handling
- behavioral scale / evidence status definitions

这页文档一旦补上，后续的 evidence table、taxonomy 验证和正文写作都会稳很多。
