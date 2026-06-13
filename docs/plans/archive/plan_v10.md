 # SpatialAgent 研究计划 v10

## Can Computable Spatial Configuration Shape LLM-Agent Social Behavior?

> 版本: 10.0  
> 日期: 2026-05-01  
> 作者: Li  
> 目标会议: AAMAS-27 首选 / AAAI-27 备选  
> 本版本目标: 基于当前 survey evidence map 与 research-gap 讨论，重写主 paper 的问题定位、理论边界和完整实验设计。`plan_v9.md` 保留为历史 protocol 参考，本文件作为当前主计划。

---

## 0. 一句话版本

这篇主 paper 不试图证明 Space Syntax 在 LLM-agent 世界中“成立”。

它要检验的是：

> 当 LLM agents 不只接收地点名、场景氛围或局部邻接，而是接收可计算的空间构型信息时，它们的社会行为是否会发生可测、可解释、具有实践意义的变化？

换句话说，本文关注的不是“有没有空间背景”，而是：

> 空间结构能否作为一种 agent-facing behavioral input，而不只是叙事背景或 prompt 装饰？

---

## 1. 从 Survey 到主 Paper 的逻辑

### 1.1 Survey 已经证明的问题

当前 survey 的 evidence map 显示，LLM-agent 系统并不缺“空间环境”。

现有系统中已经有：

- towns
- maps
- game worlds
- Minecraft-like worlds
- social VR environments
- 3D scenes
- graph-based social environments
- local movement and co-presence interfaces

但是，这些系统里 agent 真正接收到的空间信息通常停留在：

- 地点名或动作标签
- 语义场景描述
- 附近对象或附近人物
- 局部邻接关系
- 局部移动选项

survey 当前稳定 evidence map 的口径是：

- stable widened Core: `32` paper-level sources / `34` coded rows
- `anchor_core`: `17` sources / `19` rows
- `bridge_core`: `15` sources / `15` rows
- representation distribution: `L1 = 1 / L2 = 8 / L3 = 18 / L4 = 1 / L5 = 6`
- strict `anchor_core` 中 `L4 = 0`
- 唯一 `L4` 出现在 widened digital-network `bridge_core`，不构成严格物理空间 / Space Syntax 意义上的 anchor evidence

因此，survey 支撑的 gap 不是“LLM-agent 没有空间”，而是：

> 现有 LLM-agent 研究很少系统检验 agent-facing configurational information 是否能在语义场景描述之外影响社会行为。

### 1.2 主 Paper 要接住的问题

survey 证明了一个文献缺口：

> `L4` 构型级空间信息在现有 LLM-agent 社会模拟中几乎缺失。

主 paper 要做的是下一步实证测试：

> 如果我们真的把这类可计算的构型信息给 agent，它有没有行为价值？

两篇文章的关系：

| 论文 | 回答的问题 | 产物 |
|---|---|---|
| Survey | 现有文献有没有 agent-facing configurational spatial information？ | evidence map + taxonomy + research agenda |
| Main paper | 如果提供这种信息，LLM agent 行为是否改变？ | controlled experiment + system prototype + evaluation |

---

## 2. Research Gap 的最终表述

### 2.1 不建议使用的弱 gap

不要把 gap 写成：

> 现有 LLM-agent 系统没有使用 Space Syntax。

这个 gap 不够强，因为审稿人会问：

- 不用 Space Syntax 又怎样？
- 为什么一定要用这套理论？
- Space Syntax 本身是否足够可靠？

### 2.2 建议使用的强 gap

本文的 research gap 应写成：

> Although LLM-agent systems increasingly place agents in maps, towns, games, and simulated communities, the spatial layer is rarely treated as an explicit, computable, and experimentally controlled behavioral variable. Existing systems often expose place names, semantic scene descriptions, nearby entities, or local movement options, but seldom test whether agent-facing configurational structure, such as depth, integration, control, or global network position, changes social behavior beyond semantic prompting. As a result, we do not yet know whether spatial structure functions as a genuine behavioral signal in LLM-agent societies, or merely as narrative background.

中文解释：

> 虽然现有 LLM-agent 系统越来越常把 agent 放进地图、小镇、游戏和模拟社区里，但空间层很少被当作明确、可计算、可操控的行为变量。现有系统多给 agent 地点名、语义场景、附近对象或局部移动选项，却很少检验 agent 可见的构型信息，例如 depth、integration、control 或 global network position，是否能在语义 prompt 之外改变社会行为。因此我们还不知道，空间结构在 LLM-agent 社会中到底是一种真正的行为信号，还是只是叙事背景。

### 2.3 这不是“理论迁移 gap”，而是“实验变量缺失 gap”

本文不主张：

> Space Syntax 是正确理论，所以 LLM agents 应该使用它。

本文主张：

> Space Syntax-inspired topological descriptors provide a computable representation layer for testing whether LLM agents can respond to configurational information beyond semantic scene descriptions.

也就是说，我们把 Space Syntax 当作一组可计算的空间结构变量，而不是当作不可质疑的理论真理。

---

## 3. Space Syntax 的角色

### 3.1 Space Syntax 本质上提供什么

Space Syntax 的核心不是研究墙、门、房间本身，而是研究：

> 空间关系如何组织社会关系。

它把实体空间抽象为数理关系：

- 谁更中心
- 谁更深
- 谁更靠近入口
- 谁控制通道
- 谁更容易被经过
- 谁更容易被隔离
- 谁更可能成为 encounter / visibility / movement 的机会结构

例如四合院中，主人住在更深、更正中的位置，杂役住在靠近出入口的位置。这个现象不只是文化标签，也可以被理解为空间结构在分配：

- 访问门槛
- 可达性
- 权威
- 服务关系
- 公开性与私密性

因此，Space Syntax 给本文提供的是一套描述空间社会意义的结构语言。

### 3.2 迁移到 LLM Agent 的中间层

本文不直接迁移完整 Space Syntax 理论，而是迁移一个中间机制：

```text
configuration -> opportunity structure -> social behavior
```

在真实世界中：

```text
空间构型影响可见性、可达性、偶遇、隐私、控制，由此影响社会行为。
```

在 LLM-agent 世界中，本文测试：

```text
如果 agent 接收到构型信息，它是否会把这些信息转化为移动、对话、社交选择、信息传播或群体行为差异？
```

### 3.3 必须承认的理论风险

Space Syntax 不能被写成万能解释。

本文必须承认：

- Space Syntax 的一些解释具有黑盒性
- 指标之间可能共线
- 物理空间证据不能自动迁移到 LLM-agent 世界
- LLM 的响应可能来自语言关联，而不是结构推理
- 文本化空间不能复现 embodied affordance
- 负结果不等于 Space Syntax 被整体证伪

因此，本文的定位应是：

> Space Syntax-inspired proof of concept, not Space Syntax validation.

---

## 4. 主 Paper 的核心贡献

### 4.1 Primary Contribution

提出并实证检验一种 **computable configurational representation layer**，用于测试 LLM agents 是否会在语义场景描述之外，对空间构型信息产生系统性行为响应。

更短表达：

> We test whether computable spatial configuration can act as a behavioral input for LLM agents.

### 4.2 Secondary Contribution

建立一套控制条件，把以下因素拆开：

- 地点名
- 语义场景描述
- 隐式空间 affordance
- 非空间结构化描述
- 显式空间构型描述
- movement 信息
- action sampling

这样可以避免把所有效果都归因于“空间”。

### 4.3 Tertiary Contribution

提供一套评估框架，判断结构化空间表征是否具有：

- behavioral responsiveness
- theory-aligned direction
- model robustness
- human-perceived spatial appropriateness
- practical significance

---

## 5. 本文可以说什么 / 不可以说什么

### 5.1 可以说

如果结果支持，本文可以说：

- 结构化空间表征可以系统性影响 LLM Agent 行为
- 这种影响在关键比较中超出地点名或非空间基线
- 部分影响沿着 Space Syntax-inspired 理论方向发生
- 这种表征可能提升虚拟世界 / 游戏 NPC / 社会模拟中的行为可控性与空间一致性
- agent-facing configurational information 是值得进一步研究的环境输入层

### 5.2 不可以说

本文不应该说：

- 我们证明了 Space Syntax 在 LLM-agent 社会中成立
- LLM agents 等价于真实人类
- 空间结构因果决定所有社会涌现
- 拓扑描述一定优于自然语言描述
- 3D 环境天然就是高阶空间表征
- 所有正结果都是结构推理，而不是语言关联

### 5.3 最稳的贡献句

> We do not claim that Space Syntax is validated in LLM-agent societies. Instead, we use Space Syntax-inspired topological descriptors as a computable representation layer to test whether LLM agents can respond to configurational information beyond semantic scene labels, and whether such responses improve behavioral controllability, interpretability, and spatial appropriateness.

---

## 6. 核心研究问题

### RQ1: Behavioral Responsiveness

当 agent 接收结构化空间构型描述时，它们的行为是否相对于地点名、语义场景或非空间控制发生系统性变化？

### RQ2: Beyond Semantic Prompting

结构化空间描述的效果是否超出普通语义场景描述或隐式 affordance 描述？

### RQ3: Theory-Aligned Direction

行为变化是否部分沿着 Space Syntax-inspired 理论方向发生？

例如：

- 高 integration 位置是否更容易产生社交接触？
- 高 depth 位置是否更容易产生私密行为？
- 高 control 位置是否更容易产生守门、拦截或信息筛选行为？

### RQ4: Structure vs Language Association

agent 的响应更像是在利用抽象空间结构，还是主要在跟随语言刻板印象？

### RQ5: Practical Value

即便统计显著，这些行为差异是否足够大、足够可辨识，值得在真实 agent 系统中增加空间指标计算和描述生成成本？

---

## 7. 研究设计总览

### 7.1 总体设计

本文采用 **controlled simulation experiment**。

基本单位是一个 `run`：

```text
run = map × seed × condition
```

每个 run 中有一组 LLM agents 在同一张地图中进行多轮行动、移动、观察和互动。不同条件之间尽量共享初始状态，改变的核心变量是 agent 可以看到什么空间信息。

实验分为五个阶段：

| 阶段 | 目的 | 是否进入主结论 |
|---|---|---|
| Stage 0 Preflight | 验证地图、模型、prompt、指标和日志能否支撑实验 | 不进入主结论 |
| Stage 1 Micro-task | 先测试空间表征本身是否能改变单步行为判断 | 支撑主结论 |
| Stage 2 Long-run Simulation | 测试长程多 agent 社会行为是否受空间构型影响 | 主结论核心 |
| Stage 3 Mechanism and Robustness | 拆解机制、检查模型和地图鲁棒性 | 强化或限定结论 |
| Stage 4 Human Evaluation | 判断效果是否被人类感知为更空间适配 / 更可信 | 实践意义核心 |

### 7.2 最小可投稿版本

最低可投稿版本不追求所有扩展都完成，而是必须完成：

- `Stage 0` 全部 gate
- `Stage 1A` 表征微任务
- `Stage 2` 主长程模拟
- `Stage 3` 最小鲁棒性子集
- `Stage 4` 人类评估中的 pairwise preference

如果预算或时间不足，以下内容可降级为 appendix 或 future work：

- 完整多模型鲁棒性
- 全量 Irregular map 泛化
- H3 Control Value 的确认性检验
- 复杂社会网络涌现指标

---

## 8. 实验材料

### 8.1 地图

地图必须先作为 graph 结构定义，再从 graph 计算空间指标。

| 地图 | 节点数 | 结构特征 | 实验角色 |
|---|---:|---|---|
| `Plaza` | 约 20 | 中心性高峰明显，公共中心清楚 | 主验证地图 |
| `Labyrinth` | 约 20 | depth 高、路径绕、低 connectivity 区明显 | 隐私 / depth 检验 |
| `Bridge` | 约 20 | bottleneck 和 control 节点明显 | control / 守门检验 |
| `Irregular` | 25-30 | 程序生成或不规则布局，指标分布更混合 | 泛化测试 |

每张地图必须输出：

- graph adjacency
- node labels
- coordinates for visualization
- `Integration`
- `Mean Depth`
- `Control Value`
- `Connectivity`
- 可选 `Visibility / Openness`
- 指标分布图
- 指标相关矩阵

地图通过标准：

- 主指标不能全都共线
- `Integration` 至少有可区分的高低节点
- `Mean Depth` 或 `Openness` 至少一个能支持 H2
- `Control Value` 高节点若少于 `5` 个，则 H3 降级为描述性分析

### 8.2 Agents

主实验使用 `10` 个 NPC agents。

角色设计需要平衡：

| 维度 | 水平 | 目标分布 |
|---|---|---|
| 社交倾向 | 高 / 中 / 低 | 4 / 3 / 3 |
| 职业角色 | 公共型 / 中性型 / 隐蔽型 | 3-4 / 3 / 3-4 |
| 目标类型 | 社交型 / 信息型 / 独立型 | 3-4 / 3 / 3-4 |

硬约束：

- persona 中不得写入固定空间偏好
- 背景故事不得绑定特定地点
- 社交倾向、职业、目标不能完全重合
- 所有条件共享同一套 agent persona

### 8.3 模型

主模型优先使用一个成本可控、可批量运行的模型。

| 角色 | 默认模型 | 用途 |
|---|---|---|
| Primary Actor | `Qwen3.5-Plus` 或当前可用等价模型 | 生成 agent 行为 |
| Primary Judge | 与 Actor 分离或同源但需审计 | 行为评分 / sampling |
| Robustness Actor | `Llama 3.3 70B` 或等价开源模型 | 检查方向是否跨模型 |
| Robustness Closed Model | `Claude` / `GPT` 子集 | 检查是否只属于单一模型族 |
| Rule-based Scorer | 非 LLM | 检查 LLM judge 是否放大效应 |

若实际 API、预算或可用性发生变化，必须记录模型版本、日期、参数和 prompt 模板。

---

## 9. 空间表征与条件矩阵

### 9.1 变量原则

本文不比较“有空间 vs 无空间”这么粗的差异，而是比较不同类型的 agent-facing input：

- 地点名
- 局部拓扑
- 自然语言氛围
- 非空间结构化描述
- 显式空间构型描述
- movement 信息
- action sampling

### 9.2 主条件矩阵

| 条件 | Movement 输入 | 到位后描述 | Sampling | 作用 |
|---|---|---|---|---|
| `C1 Topology-Only` | 邻接 + 地名 + 在场人数 | 无 | 无 | 最小空间基线 |
| `C2 Implicit Spatial` | 同 `C1` | 隐式空间 affordance，例如安静、开放、适合交流 | 无 | 普通语义空间描述基线 |
| `C2b Non-Spatial Structural` | 同 `C1` | 非空间结构特征，例如材质、窗、光线数量 | 无 | 控制“结构化格式”本身 |
| `C2c Truly Non-Spatial` | 同 `C1` | 时间模式或社会规范，随机映射到地点 | 无 | 真正非空间控制 |
| `C6m Explicit Spatial Matched-Movement` | 同 `C1` | 显式构型描述 | 无 | 纯到位后 perception 效应 |
| `C6f Explicit Spatial Free-Movement` | 空间指标 + 邻接 + 地名 + 在场人数 | 显式构型描述 | 无 | movement 使用空间指标的贡献 |
| `C4 Full SpatialAgent` | 同 `C6f` | 显式构型描述 | 有 | 完整系统效果 |

### 9.3 显式构型描述模板

显式空间描述不能直接写“适合社交 / 适合私密”。

它应该描述结构：

```text
This location is highly integrated in the layout. It has short average topological distance to many other locations, high connectivity, and frequent path overlap. It is structurally exposed rather than secluded.
```

或：

```text
This location is relatively deep in the layout. It requires several topological steps from central areas, has low through-movement, and is structurally secluded.
```

禁止写法：

```text
This place is good for socializing.
This place is suitable for private conversation.
This place should make agents gather.
```

### 9.4 机制条件

| 条件 | 目的 | 地位 |
|---|---|---|
| `C_shuffle` | 打乱空间指标与地点映射，检查是否需要正确结构信号 | 机制检验 |
| `C_counter` | 结构与语义标签冲突，检查 agent 跟随结构还是语义 | 机制检验 |
| `C_fixed_path` | 固定 movement，只看到位后 perception | 机制检验 |
| `C_judge_only` | 只让 judge 看到空间信息，检查是否是 judge 制造效应 | 审计 |
| `C_rule_scorer` | 用非 LLM scorer 替代 judge | 审计 |

---

## 10. Stage 0: Preflight Gates

Stage 0 不进入主结论，但必须通过后才能开始正式实验。

| Gate | 目的 | 通过标准 |
|---|---|---|
| Map metric quality | 确认地图指标可区分 | 指标分布、相关矩阵、H2/H3 可检验性报告完成 |
| Spatial comprehension | 确认模型理解构型描述 | comprehension `>= 85%`，behavioral inference `>= 70%` |
| Novel inference test | 检查是否能从结构描述推断行为适配性 | accuracy `>= 75%` |
| Prompt placement test | 固定空间信息插入位置 | 至少比较 3 种位置，选择最稳定方案 |
| C2 reverse-inference audit | 确认隐式 / 非空间基线不泄露结构 | 人类或 LLM 不能稳定反推出 high/low integration/depth/control |
| MIC pilot | 检查 matched initial conditions 的有效窗口 | 报告 `0-50`、`51-100`、`101-200` seed ICC 或方差缩减 |
| Convergence pilot | 决定 `200` 轮还是 `300` 轮 | 主网络指标连续 3 个窗口 `delta_t < 0.2`，并通过 50 轮 holdout |
| Logging audit | 确保可复现 | prompt、response、parsed action、state、seed、condition 全部可追踪 |

若任一关键 gate 不通过，不能启动 Stage 2。

---

## 11. Stage 1: Micro-task 表征实验

### 11.1 目的

Stage 1 先避免长程模拟的复杂性，直接测试：

> 空间构型描述是否能改变 agent 对单步社会行为的判断？

### 11.2 任务类型

| 任务 | 对应假设 | 示例 |
|---|---|---|
| 主动搭话 | H1 Integration | 是否主动接近或发起对话 |
| 信息透露 | H2 Depth / Privacy | 是否透露敏感信息 |
| 位置选择 | H1/H2/H3 | 在多个地点中选择行动位置 |
| 停留 / 离开 | H1/H2 | 是否停留、回避或转移 |
| 守门 / 拦截 | H3 Control | 是否观察、阻拦、筛选信息 |

### 11.3 Stage 1A: 表征条件对比

条件：

- `C1`
- `C2`
- `C2b`
- `C2c`
- `C6m`
- `C_shuffle`

设计：

- 每张主地图选 `high / medium / low` 结构节点
- 每个任务类型至少 `30` 个 scenario
- 每个 scenario 在所有条件下运行
- 输出为二分类或 1-7 分评分

主比较：

```text
C6m > C1
C6m > C2
C6m > C2b
C6m > C2c
C6m > C_shuffle
```

Stage 1A 成功标准：

- 至少 H1 或 H2 相关任务中 `C6m` 相比 `C1/C2c` 达到中等效应
- `C6m` 相比 `C_shuffle` 方向正确
- 若 `C2` 大于或等于 `C6m`，记录为“语义 affordance 更强”，不强行解释为空间结构优势

### 11.4 Stage 1B: Counter-stereotypical test

设计一个 `2 × 2` 条件：

| | 公共语义标签 | 私密语义标签 |
|---|---|---|
| public-structural profile | 一致 | 冲突 |
| private-structural profile | 冲突 | 一致 |

目的：

> 区分 agent 是跟随结构，还是跟随语义标签。

模型：

```text
DV ~ structural_profile * semantic_label + (1|scenario)
```

解释：

- `structural_profile` 主效应强：支持结构响应
- `semantic_label` 主效应强：支持语言关联
- 交互项强：说明结构和语义冲突时存在竞争

---

## 12. Stage 2: 长程多 Agent 主实验

### 12.1 目的

Stage 2 是主 paper 的核心。

它测试：

> 在多 agent 长程社会模拟中，结构化空间表征是否会改变移动、互动、信息传播和社会网络模式？

### 12.2 设计

主设计：

```text
4 maps × 15 seeds × 7 main conditions = 420 runs
```

如果预算不足，最小版本：

```text
3 maps × 10 seeds × 5 core conditions = 150 runs
```

推荐正式版本：

- maps: `Plaza`, `Labyrinth`, `Bridge`, `Irregular`
- seeds: `15`
- agents: `10`
- rounds: `200` 或 `300`，由 convergence pilot 决定
- main conditions: `C1`, `C2`, `C2b`, `C2c`, `C6m`, `C6f`, `C4`

### 12.3 MIC 规则

`MIC = Matched Initial Conditions`，只匹配初始条件，不声称全程完全可比。

不同 condition 在同一 seed 下共享：

- 初始 agent 位置
- 初始目标 / persona
- 初始世界事件表
- 初始非空间描述映射
- 初始随机数种子

但 `50` 轮以后世界可以自然分化。报告时必须写清楚这一点。

### 12.4 主比较链

| 比较 | 解释 |
|---|---|
| `C4 - C1` | 完整 SpatialAgent 相对 topology-only 的总效应 |
| `C6m - C1` | 到位后 explicit spatial perception 的效应 |
| `C6m - C2c` | 显式空间结构 vs 真正非空间控制 |
| `C6m - C2` | 显式空间结构 vs 隐式空间 affordance |
| `C6m - C2b` | 空间内容 vs 非空间结构化描述 |
| `C6f - C6m` | movement 是否使用空间指标的增量 |
| `C4 - C6f` | action sampling 的增量 |

总系统效应可拆成：

```text
C4 - C1 = (C6m - C1) + (C6f - C6m) + (C4 - C6f)
```

### 12.5 主行为指标

| 行为层级 | 指标 |
|---|---|
| movement | 访问高 integration 节点比例、平均 depth、location entropy |
| encounter | co-presence rate、encounter diversity、repeat encounter |
| interaction | 主动对话率、对话对象多样性、敏感信息透露率 |
| information spread | 信息传播范围、传播速度、来源集中度 |
| social network | degree centralization、clustering、community formation、brokerage |
| role behavior | guarding、mediating、withholding、public/private action choice |

### 12.6 主理论指标

继续使用：

- `BSR`: Behavioral Spatial Responsiveness
- `TAR`: Theory-Aligned Responsiveness

定义原则：

```text
BSR = 行为是否随空间变量发生系统性差异
TAR = 行为变化是否沿着预注册理论方向发生
```

主端点：

```text
TAR_H1_run
```

主对比：

```text
C4 vs C1
```

主分析单元：

```text
run-level: map × seed × condition
```

---

## 13. Stage 3: 机制拆解与鲁棒性

### 13.1 机制条件

| 子实验 | 条件 | 最小规模 | 目的 |
|---|---|---:|---|
| Shuffled signal | `C_shuffle` vs `C6m` | 10 seeds × 3 maps | 检查正确空间指标是否必要 |
| Counter-stereotype | `C_counter` | micro-task + 5 seeds | 区分结构响应与语义联想 |
| Fixed path | `C_fixed_path` | 10 seeds × 3 maps | 固定移动后检查 perception 效应 |
| Judge-only audit | `C_judge_only` | 5 seeds × 2 maps | 检查 judge 是否制造效应 |
| Rule scorer audit | `C_rule_scorer` | 5 seeds × 2 maps | 检查非 LLM scorer 下方向是否保留 |

### 13.2 模型鲁棒性

最小鲁棒性子集：

```text
3 maps × 5 seeds × 3 conditions
conditions = C1, C6m, C4
```

推荐鲁棒性子集：

```text
4 maps × 10 seeds × 3 conditions
```

解释规则：

| 结果 | 解释 |
|---|---|
| 主模型与鲁棒性模型方向一致 | 支持跨模型外部效度 |
| 只有主模型显著 | 结论限定为 model-specific |
| 闭源模型与开源模型相反 | 讨论训练分布或 alignment 差异 |
| judge 更换后结果消失 | 说明评分机制可能驱动结果 |

---

## 14. Stage 4: 人类评估

### 14.1 目的

人类评估不用于证明 Space Syntax 正确。

它用于回答：

> 结构化空间表征带来的行为差异，人类读者是否能感知为更可信、更符合空间情境？

### 14.2 参与者

- 目标样本量: `60`
- 在线招募
- 通过注意力检查
- 盲法：参与者不知道条件标签

### 14.3 任务

| 任务 | 材料 | 输出 |
|---|---|---|
| Pairwise preference | 同一场景下 `C4` vs `C1` 或 `C6m` vs `C2c` 行为片段 | 哪个更符合空间情境 |
| Rating task | 单个行为片段 | believability、spatial appropriateness 1-7 |
| Judge calibration | 人类评分 vs LLM judge 评分 | agreement / kappa |

### 14.4 成功标准

- pairwise preference 显著偏离 `50%`
- spatial appropriateness 至少中等效应
- 人类评分与 LLM judge 至少中等一致
- 若统计显著但人类不可辨别，则降级为“技术上可测但实践意义弱”

---

## 15. 统计分析计划

### 15.1 确认性分析

| # | 对比 | 因变量 | 单位 | 模型 | 成功标准 |
|---|---|---|---|---|---|
| 1 | `C4 vs C1` | `TAR_H1_run` | run | mixed model | `p < .05`, `d >= 0.5` |
| 2 | `C4 vs C1` | `BSR_H1_run` | run | mixed model + FDR | `p < .05`, `d >= 0.5` |
| 3 | `C6m vs C1` | `TAR_H1_run` | run | mixed model + FDR | direction positive |
| 4 | `C6m vs C2c` | `TAR_H1_run` | run | mixed model + FDR | direction positive |
| 5 | `C6m vs C2` | `TAR_H1_run` | run | mixed model + FDR | tests explicit vs implicit |
| 6 | `C6m vs C2b` | `TAR_H1_run` | run | mixed model + FDR | tests spatial content vs format |
| 7 | `C4 vs C1` | human preference | participant | paired / mixed model | preference > 50% |

主模型：

```r
TAR_H1_run ~ condition + map + condition:map + (1|seed)
```

如果 map 数量不足或模型不稳定：

```r
TAR_H1_run ~ condition + (1|seed)
```

并将 map-specific 结果作为分层报告。

### 15.2 探索性分析

- H2 privacy / depth
- H3 control / guarding
- 时间动态：`0-50` vs full run
- agent trait moderation
- map-specific heterogeneity
- language-specific effects
- social network macro metrics

探索性分析不得替代主分析。

### 15.3 时间动态

预注册两种模式：

| 模式 | 现象 | 解释 |
|---|---|---|
| Spatial priming | 前 `50` 轮强，后期衰减 | 空间信息主要启动初始行为 |
| Sustained guidance | 前期和后期方向稳定 | 空间信息持续进入行为选择 |

---

## 16. 结果解释框架

| 层级 | 主实验 | counter test | 人类评估 | 可主张 |
|---|---|---|---|---|
| Tier 1 强结果 | TAR 显著且中等以上 | 结构胜过语义 | 可辨别 | configuration is a meaningful behavioral input |
| Tier 2 中等结果 | BSR/TAR 部分成立 | 结构与语义混合 | 可辨别或边界 | spatial descriptors help but are entangled with semantics |
| Tier 3 弱结果 | 只优于 minimal baseline | 语义强于结构 | 不稳定 | effect may be prompt-format or language-association driven |
| Tier 4 负结果 | 无稳定效应 | 跟随语义或随机 | 不可辨别 | current descriptors do not support robust configurational control |

负结果仍有价值，因为它说明：

> 有地图、有空间词、有 3D backend，并不自动意味着 LLM-agent 系统有空间机制。

---

## 17. 预算与规模控制

### 17.1 推荐正式规模

```text
Stage 2: 4 maps × 15 seeds × 7 conditions = 420 runs
rounds: 200-300
agents: 10
```

### 17.2 最小可投稿规模

```text
Stage 2: 3 maps × 10 seeds × 5 core conditions = 150 runs
core conditions = C1, C2c, C6m, C6f, C4
```

最小版本必须保留：

- `C1`: 最小空间基线
- `C2c`: 真正非空间控制
- `C6m`: explicit spatial perception
- `C6f`: movement contribution
- `C4`: full SpatialAgent

可以暂缓：

- `C2`
- `C2b`
- 完整 `Irregular`
- 大规模 closed-model robustness

---

## 18. 论文结构

建议主 paper 结构：

1. Introduction: 从 survey gap 引出问题
2. Related Work: LLM agents, spatial interfaces, Space Syntax as computable configuration
3. Method: maps, descriptors, conditions, agents, simulation engine
4. Preflight: model comprehension, map metric quality, baseline audit
5. Experiments: Stage 1 micro-task, Stage 2 long-run, Stage 3 robustness, Stage 4 human eval
6. Results: primary endpoint, secondary comparisons, human evaluation, robustness
7. Discussion: what works, what fails, relation to Space Syntax, limitations
8. Conclusion

---

## 19. 当前执行状态

### 已有基础

- `spatial-agent-core/` 已有工程骨架
- 已有 `configs/`, `experiments/`, `src/`, `tests/`, `paper/`
- 已有地图配置和实验配置雏形
- survey evidence map 已形成稳定基线
- survey 已证明 `L4` 缺口具有文献依据
- v10 已将 research gap 与实验设计合并为当前主计划

### 需要同步的文档问题

当前部分 guide 仍指向 v8.2 / v7，需要更新为：

- 当前主计划: `plan_v10.md`
- 历史 protocol 参考: `plan_v9.md`
- 执行 guide 待升级: `research_mentorship_guide_v3.md`

### 下一步任务

1. 对照 `spatial-agent-core` 当前代码，检查是否支持 `C1/C2c/C6m/C6f/C4` 最小条件矩阵。
2. 更新 configs，使 Stage 0 preflight 可直接运行。
3. 补齐地图 metric quality report。
4. 生成 `C2/C2b/C2c` 描述池和 audit 表。
5. 明确主模型、预算、正式 run 数。
6. 将本计划拆成 execution checklist。

---

## 20. 最终定位

本文不是在做：

> A proof that Space Syntax governs LLM-agent societies.

本文是在做：

> A controlled test of whether computable spatial configuration can function as a behavioral input layer for LLM agents beyond semantic scene prompting.

对应中文定位：

> 本文不是证明 Space Syntax 在 LLM-agent 社会中成立，而是检验可计算的空间构型信息能否在语义场景描述之外，成为 LLM Agent 行为生成中的有效输入层。
