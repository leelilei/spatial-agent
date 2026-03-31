# SpatialAgent 研究计划 Challenge 文档

> 目的：不是润色原计划，而是从反方评审、方法论质疑和投稿可行性的角度，系统性挑战这个 idea 与当前研究计划。
> 立场：我默认自己是一个挑剔但希望你赢的审稿人。

---

## 一句话判断

这是一个**很有辨识度、很有跨学科魅力**的 idea，但你当前版本最大的问题不是“想法不够新”，而是**claim 过大、因果识别不够干净、baseline 不够公平、评估设计容易被说成 prompt engineering 自嗨**。

如果现在就按这个版本直接往 AAAI/CHI 写，最危险的结果不是“被说没意思”，而是：

- 审稿人觉得你有趣，但证据链不闭合
- 审稿人觉得你测到的是“prompt 差异”，不是“空间理论”
- 审稿人觉得空间构型效应是环境 mechanics 导致的，不是 Agent cognition 导致的

我的总评是：

- **idea 值得做**
- **当前计划不该原样执行**
- **必须先收缩问题、重做对照、重写 claim**

---

## 核心结论

你现在其实同时想证明 4 件事：

1. LLM Agent 存在“空间失明”
2. Space Syntax 可以作为理论框架解释这种缺失
3. SpatialAgent 架构能提升单体行为可信度
4. 空间构型会因果性地塑造多 Agent 社会涌现

问题在于，这四件事不是一个难度等级。

- 第 1、2 点相对容易成立
- 第 3 点可以通过更严谨实验做出来
- 第 4 点是最危险的，它会把整篇论文的识别难度抬高一个量级

如果你不收缩，论文会变成“每一点都沾一点，但每一点都不够硬”。

---

## P0 级问题：最可能把论文直接打掉的点

### P0-1：你的“因果”主张现在并不干净

你在 `Exp2` 里想证明：**相同 Agent 配置下，不同空间构型导致不同社会涌现模式**。

但审稿人会马上问：

> 这些差异到底是因为 Agent 理解了空间，还是因为地图本身改变了 encounter 机会、路径长度、共处频率和信息传播通道？

也就是说，你现在把两个效应混在了一起：

- **环境 mechanics effect**：拓扑变了，所以谁更容易遇见谁自然变了
- **agent cognition effect**：Agent 真的因为理解空间特征而改变行为

如果不拆开，你的结论会被改写成：

> “不同地图会产生不同社会结构”

这句话虽然没错，但它远弱于你想要的：

> “Space Syntax-informed cognition causally changes multi-agent emergence.”

### 为什么危险

- 这会直接动摇 `RQ2` 和 `H1-H5` 的解释力
- 你可能最后只能证明“地图结构很重要”，而不是“SpatialAgent 很重要”
- 审稿人会说这更像社会网络/地图生成研究，而不是 Agent cognition 研究

### 你需要补什么

- 加入**非空间认知 Agent**但运行在同样地图上的对照
- 加入**简单规则/随机/脚本 Agent**作为 mechanics-only 下界
- 加入**shuffled spatial signal** 条件：给 Agent 错配或随机化的空间指标
- 明确区分：
  - 地图改变带来的 encounter baseline
  - 空间理解带来的额外行为偏移

### 更强的实验问法

不要直接问：

> 不同构型是否导致不同涌现？

而要问：

> 在控制 encounter opportunity 的前提下，空间语义/拓扑表征是否仍然能显著改变行为策略与网络结构？

---

### P0-2：baseline 不公平，容易被说成“你只是给了更多上下文”

你现在的 baseline 是“无空间感知”，而 SpatialAgent 会得到：

- 位置指标
- 动态环境
- 在场人数
- 噪音、光照、时间
- 空间语言化描述

这不是一个公平 baseline。审稿人会说：

> 你提升的原因，可能只是因为你给了模型更多 situational context，而不是因为 Space Syntax 理论本身有用。

### 为什么危险

如果 baseline 太弱，你整篇论文最重要的结论都会被打折：

- 不是 Space Syntax 赢了
- 是 “more context” 赢了

### 你至少需要 4 个 baseline

#### Baseline A：No Space

完全没有空间信息。这个你已经有了，但它只能算最低基线。

#### Baseline B：Location Name Only

只给地点名，例如“酒馆密室”“市场广场”。

目的：排除“语义标签本身就足够”的可能性。

#### Baseline C：Rich Scene Description without Syntax Metrics

给自然语言场景描述，但不包含 `integration / connectivity / control / visual depth` 这些结构化来源。

例如：

> 这里灯光昏暗、很安静、只有两个人在场。

目的：排除“任何场景描述都会提升表现”的可能性。

#### Baseline D：Shuffled / Wrong Spatial Signals

给真实地图，但把空间指标错配到别的地点。

目的：验证模型是否真的在利用正确的空间结构，而不是只对“听起来像环境描述”的文字起反应。

如果 D 也能提升很多，你的理论解释就危险了。

---

### P0-3：你现在测到的很可能是“prompt wording effect”，不是“theory effect”

你的核心入口是 `Spatial-to-Language Converter`。这一步其实非常强，也非常危险。

因为一旦你把数值转成这种语言：

- “这里是人流汇聚的核心区域”
- “这里是偏僻角落”
- “这里具有战略价值”
- “这里对话不易被偷听”

你其实已经在把行为倾向**直接写进 prompt** 了。

审稿人完全可以说：

> 你的方法不是让模型理解空间，而是在用自然语言暗示它应该怎么演。

### 这不是小问题

因为这会把你的贡献从：

- “引入空间理论”

降格成：

- “设计了一个更强的场景提示词”

### 你需要补的关键实验

#### 表征消融

比较至少三种输入方式：

1. `Raw numeric features`
2. `Neutral textual description`
3. `Interpretive textual description`

示例：

- Raw：`integration=0.82, connectivity=4, visual_depth=0.77`
- Neutral：`该节点可见范围较高，连接 4 个相邻节点`
- Interpretive：`这里是社交核心区域，容易被注意`

如果只有第 3 种有效，那你测到的是“解释性提示词”。
如果第 1、2 种也有效，你才能更有底气说是“空间表征”而不是“说教式 prompt”。

---

### P0-4：你把理论假设写得太直了，容易被反例秒杀

比如：

- `H2`：低 Visual Depth 区域更容易透露秘密
- `H3`：高 Control Value 节点更容易涌现领导者

这些说法都很漂亮，但太像“听起来合理”的一阶映射，而不是稳健假设。

### 反例很容易构造

#### 对 H2 的反例

低 visual depth 也可能意味着：

- 视野差，不安全
- 逃跑路线少
- 一旦被堵住风险更高

所以秘密透露未必增加，甚至可能下降。

#### 对 H3 的反例

高 control value 节点可能产生的不是“领导者”，而是：

- 守门人
- 哨兵
- 中介者
- 瓶颈拦截者

它未必对应社会意义上的 leadership。

### 建议改法

把强方向性假设改成更保守、可解释的机制假设：

- 不说“低 visual depth 必然提高秘密透露”
- 改成“privacy-related disclosure will be modulated by spatial visibility and escape affordance”

也就是说，把：

- 单一指标 -> 单一行为

改成：

- 一组空间约束 -> 某类行为倾向变化

---

### P0-5：`Exp2` 的地图设计同时改变了太多东西

你现在三张地图不是只改变一个变量，而是同时改变：

- Integration 分布
- Connectivity 分布
- Intelligibility
- 中心数量
- 死胡同数量
- 平均路径长度
- 层级结构

这很适合做“世界观展示”，不适合做严谨识别。

### 审稿人会怎么说

> 你当然能测出差异，因为你换了几乎整个世界。

### 更严谨的做法

至少加入两类设计：

#### 设计 1：整体构型对比

保留你现在的三地图，用来展示 effect existence。

#### 设计 2：单因子或近单因子操控

例如只改变：

- 某几个关键节点的 visibility
- 中心节点数量
- 单个瓶颈节点的 control value

其余尽量保持不变。

这样你才能更像在回答：

> 到底是哪种空间属性在起作用？

---

## P1 级问题：不会立刻致命，但会持续拖低说服力

### P1-1：四模块架构太“满”，容易削弱主线

你现在同时有：

- Spatial Perception
- Spatial Memory Retrieval
- Spatial Planning
- Spatial Action Sampling

问题是，当效果出来后，审稿人会问：

> 到底是谁起作用？

如果效果不出来，审稿人也会问：

> 是不是模块太多，互相抵消了？

### 建议

把论文主贡献缩成“两层”：

#### 主论文只保留最必要的 1-2 个模块

我的建议是优先保留：

1. `Spatial Perception`
2. `Spatial Action Sampling`

原因：

- 它们最直接对应“空间影响行为”
- 最容易做 clean ablation
- 最容易向审稿人解释

`Memory Retrieval` 和 `Planning` 可以：

- 放附录
- 放后续工作
- 或作为扩展实验，而不是主线

---

### P1-2：你把“理论贡献”和“工程贡献”写得都很大，容易互相打架

你想同时说自己是：

- 建筑学理论引入者
- Agent 架构设计者
- 算法设计者
- 社会涌现实证研究者

这在 proposal 阶段很鼓舞人，但在投稿时会变成问题：

> 你到底想让审稿人记住什么？

### 我的建议

在投稿版本里只保留一个主句：

> We operationalize space-syntax-derived spatial signals for LLM agents and show that these signals systematically alter behavior plausibility and interaction patterns.

这个句子比“首次证明空间构型因果塑造多 Agent 社会”更稳，也更容易 defend。

---

### P1-3：人类评估设计存在提示性偏差

你现在让被试看：

- 对话
- 空间描述
- 然后判断行为是否符合环境

问题是，如果空间描述本身已经写得很导向，例如：

> 这是一个隐私很高、不易被窃听的地方

那被试当然会更倾向认为“说秘密更合理”。

这会让人类评估变成：

- 评估 prompt 是否自洽

而不是：

- 评估 agent 是否自然

### 建议

- 人类评估材料尽量展示**地图/位置关系/场景事实**，少展示解释性语言
- 增加双盲 pairwise setup
- 增加一个问题：
  - “你是否感觉系统在刻意提示 NPC 应该怎么做？”

如果这个分数高，你的方法会很危险。

---

### P1-4：LLM-as-Judge 很可能和生成模型共享偏见

如果生成和评估都依赖同类模型，审稿人会质疑：

> 这是不是同一种模型偏好同一种写法？

### 建议

- judge 模型和 actor 模型分离
- 至少报告 judge 重复采样一致性
- 对关键 case 加人工复核
- 明确 judge rubric 中不要直接奖励“提到了空间”这种浅层特征

否则模型可能只是在奖励：

- 更具体
- 更解释性
- 更会说“我在这里所以我应该……”

而不是更 believable。

---

### P1-5：统计设计还不够像一篇严谨实验论文

你现在写了很多 `p < 0.05`，但还没有真正说明：

- 独立样本单位是什么
- 重复运行之间如何采样 seed
- 序列相关性怎么处理
- 多重比较怎么处理

### 这里是隐患

200 轮对话不是 200 个独立样本。

真正的独立单位更可能是：

- 模拟 run
- 地图实例
- agent pair
- rumor episode

### 建议

- 把 `run` 作为主要统计单位
- 对轮次级数据用 mixed-effects model
- 对多个假设做 FDR 或 Bonferroni 校正
- 预先写出 analysis plan，避免“挑显著结果”

---

### P1-6：外部效度很弱，必须主动承认

`Misty Tavern` 是一个很好的 prototype 世界，但它也是一个：

- 小规模
- 手工设计
- 文本化
- 单主题
- 高可控

的研究环境。

所以你不能把结论写太大。

### 安全写法

不要写：

> We show spatial configuration shapes believable game worlds in general.

更安全的是：

> We provide a controlled proof-of-concept that space-structured contextual signals can modulate LLM-agent behavior in a text-based social world.

这是“站得住”的说法。

---

## P2 级问题：不是主伤，但会影响完成度

### P2-1：Space Syntax 指标在 20 节点小图上的稳定性值得怀疑

尤其是：

- `visual depth` 被高度简化
- `control value` 在小图中可能很敏感
- 手工画图很容易让指标分布带有作者偏见

### 建议

- 报告每张地图完整指标分布
- 做程序化生成多个同类图，而不是只用 3 张“作者画的图”
- 检查结果是否依赖单个地图实例

---

### P2-2：你的任务脚本本身可能已经把答案写进去了

你的人设和秘密非常适合“私密空间中说秘密”这种预期结果，但这也可能让实验太顺：

- 商人走私
- 酒馆地下组织
- 间谍
- 黑魔法
- 盗贼踩点

审稿人会说：

> 你是不是挑了最容易被空间影响的剧情？

### 建议

加入两类任务：

- **空间敏感任务**：密谈、交换情报、跟踪、巡逻
- **空间不敏感任务**：寒暄、日常交易、固定 routine

如果你的方法只在前者有效，反而是好事，因为这说明边界条件清楚。

---

### P2-3：成本和时间线偏乐观

最危险的不是 API 钱，而是：

- 环境搭建
- 稳定重跑
- 数据清洗
- 评估协议打磨
- 人类实验招募
- 论文图表与叙事

如果你真的同时做 4 个模块 + 4 组实验 + 人类评估，四个月非常紧。

---

## 我会如何重写你的研究问题

### 当前版本的问题

你现在的研究问题从一开始就把自己推到了“因果证明 + 理论桥接 + 架构验证 + 社会涌现”四重高难度上。

### 更稳的版本

#### RQ1

空间结构化表征是否能提升 LLM Agent 在不同场景中的行为环境一致性？

#### RQ2

这种提升是否来自 `space syntax-derived signals`，而不是任意额外场景描述？

#### RQ3

在控制地图 mechanics 的前提下，空间化 Agent 与非空间化 Agent 是否表现出不同的互动分布与信息传播模式？

注意这里的关键变化：

- 从“证明空间构型塑造社会”改成“区分空间表征效应与 mechanics 效应”
- 从“大理论”改成“可 defend 的方法论问题”

---

## 我会如何重构实验

## 实验阶段 A：先证明你不是在做 prompt 花活

### A1. 表征方式对比

- `No Space`
- `Location Name Only`
- `Raw Metrics`
- `Neutral Spatial Description`
- `Interpretive Spatial Description`
- `Shuffled Spatial Description`

目标：

- 证明真正有效的是“正确空间表征”
- 而不是“多写两句环境描述”

### A2. 单行为任务

不要一开始就上 10 Agent 社会模拟。

先做一组更干净的微任务：

- 是否在何处透露秘密
- 是否主动开启对话
- 是否选择迁移到更合适的地点
- 是否在拥挤处停留/离开

这组实验更像机制验证。

---

## 实验阶段 B：再证明对 social simulation 有影响

### B1. 同图条件下对比 Agent 类型

在同一张图上比较：

- `Base Agent`
- `SpatialAgent`
- `SpatialAgent + shuffled signal`
- `Rule-based mobility baseline`

目标：

- 将认知效应和地图效应拆开

### B2. 多图条件下对比

保留你现在的三张地图，但只把它作为 second-stage evidence。

此时你不是在说：

> 三张地图不同，所以世界不同

而是在说：

> 空间化 Agent 在不同构型下表现出系统性的、可预测的偏移，并且这个偏移大于 baseline。

---

## 实验阶段 C：做最小但干净的机制验证

只操控一个关键空间因素，例如：

- 同一地点，开放可见 vs 遮挡私密
- 同一路径，有无 bottleneck
- 单中心 vs 双中心

目标：

- 给论文一个最容易讲清楚的“因果小实验”

这个实验往往比大而全的多图世界更有说服力。

---

## 我建议你砍掉什么

如果目标是提高论文成稿概率，我会建议你先砍掉以下内容中的一部分：

### 砍 1：先不要把四模块都放进主论文

优先保留：

- `Spatial Perception`
- `Spatial Action Sampling`

暂缓：

- `Spatial Memory Retrieval`
- `Spatial Planning`

### 砍 2：先不要把 H1-H5 都当作主假设

先保留最稳的两类：

- 可见性/隐私相关行为
- 中心性/社交接触相关行为

把 leadership、权力结构、宏观文化这种更大的说法放后面。

### 砍 3：先不要把论文定位成“首次证明空间构型因果塑造社会涌现”

改成：

- 一个空间结构化 Agent 框架
- 一个干净的实验协议
- 若干可复现的初步发现

这更容易中。

---

## 投稿视角：AAAI 和 CHI 分别会怎么打你

### AAAI 视角下的问题

AAAI 更关心：

- 方法是否明确
- 对照是否公平
- 评估是否严谨
- 贡献是否不是纯 prompt engineering

所以 AAAI 最敏感的是：

- baseline 太弱
- 因果不干净
- 模块太多讲不清
- 评估过于依赖 LLM judge

### CHI 视角下的问题

CHI 会更关心：

- 为什么这件事对人有意义
- 用户体验或设计启示是否扎实
- 人类研究是否严谨

所以如果走 CHI，你需要更强调：

- 玩家是否真的感知到空间可信度提升
- 这种提升如何影响 immersion、believability、narrative engagement
- 用户 study 不只是做 preference rating

### 我的判断

当前版本更像 **AAAI/AAMAS 风格的方法论文**，但前提是你必须先把实验做干净。

如果你保留现在这个宏大叙事、又没有强用户研究，投 CHI 反而不一定占优。

---

## 你最该重写的 5 句话

### 1. “当前所有 LLM 游戏 Agent 研究都存在根本性盲区：空间失明”

问题：

- 绝对化太强
- 很容易被 environment-aware、embodied、NPC context papers 反驳

更稳的写法：

> 现有工作通常缺乏对空间构型的显式建模，尤其缺少来自建筑学空间理论的可操作表示。

### 2. “首次将 Space Syntax 引入 LLM Agent 领域”

问题：

- “首次”太脆弱

更稳的写法：

> 据我们所知，这是最早系统性地将 space-syntax-derived metrics operationalize 到 LLM multi-agent behavior 中的工作之一。

### 3. “证明空间构型对多 Agent 社会行为具有显著塑造效应”

问题：

- “证明”太重

更稳的写法：

> 我们提供控制性证据，表明空间化表征与社会互动模式之间存在系统关联，并在若干设置下呈现可重复的行为偏移。

### 4. “Visual Depth 和 Integration 是影响最大的两个指标”

问题：

- 现在只是预期，不要提前写成半定论

更稳的写法：

> 我们将通过消融测试探索哪些空间指标最稳定地影响行为。

### 5. “这不是 prompt engineering”

问题：

- 你现在的设计还无法强有力地说这句话

更稳的写法：

> 我们通过多种 representation baselines 和 shuffled controls，检验观察到的效果是否超出一般性 prompt enrichment。

---

## 一个更可发表的“收缩版方案”

如果我是你，我会把第一版论文收缩成下面这样：

### 论文主张

提出一个 `SpatialAgent-lite`：

- 输入显式空间特征
- 通过最少模块影响行为选择
- 在控制实验中优于非空间基线和弱空间基线

### 只回答两个问题

1. 空间结构化表征能否提升行为环境一致性？
2. 这种提升是否超出普通环境描述带来的收益？

### 只做三组核心实验

1. `Representation Baseline` 对比
2. `Single-mechanism behavioral tasks`
3. `Same-map social simulation`

### 把多地图涌现放成附加证据

这样整篇论文会更像：

- 有一个干净方法点
- 有一个清楚识别问题
- 有一组可信实验

而不是：

- 一个很大很酷但容易被打散的 ambitious project

---

## 最后给你的直话

你的 idea 最大的优点是：

- 有强叙事张力
- 跨学科桥接非常漂亮
- 一眼能让人记住

你的计划最大的问题是：

- 太想一次性赢太多层
- 把最难证明的东西放成主结论
- 目前还没有把“空间理论效应”和“更多上下文/地图 mechanics 效应”分开

所以我对这个项目最真诚的建议不是“继续往下实现”，而是：

**先把论文从“大而全”改成“窄而硬”。**

如果你愿意，我下一步可以继续帮你做两件事中的任意一个：

1. 把这份 `challenge` 进一步改成“可执行修订版研究计划”
2. 直接帮你重写 `spatial_agent_research_plan_v1.md` 的核心几节，让它更像能投稿的版本
