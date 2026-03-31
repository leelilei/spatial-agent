# SpatialAgent 研究计划 v3

## Where You Are Shapes Who You Become: Space Syntax-Informed LLM Agents for Spatially Believable Game Worlds

> 版本: 3.0
> 日期: 2026-03-16
> 作者: Li
> 目标会议: AAMAS-27 (首选) / AAAI-27 (备选)
> 本版本基于 v2 及两份第二轮评审意见进行方法学收口

---

## 修订说明：v2 → v3 核心变化

| 维度 | v2 | v3 | 修改理由 |
|------|----|----|---------|
| 评估协议 | 结构化标注 + 预定义适配规则表 | **两阶段分离评估**：先盲标行为类型，再独立做空间关联分析 | Review1-§1: 规则表将假设写回评估，构成循环定义 |
| Agent条件定义 | 文字描述各条件差异 | **信息访问矩阵 + 决策模块矩阵**，一表穷尽 | Review1-§2: Topology-Only 定义模糊导致 RQ2 不干净 |
| 理论验证 vs 常识激活 | 仅在Discussion中讨论 | **新增反直觉空间条件**（拓扑结构与语义标签矛盾） | Review2-C5: 不区分这两种解释，理论贡献降级 |
| Openness指标 | 作为Visual Depth替代，承诺事后检查共线性 | **预实验先检查共线性**，备选用Mean Depth替代 | Review2-C1: Openness与Connectivity极可能r>0.8 |
| Action Sampling归因 | 未单独测试Judge效应 | **新增Judge-Only消融条件** | Review2-C2: Judge先验知识可能是主要驱动力 |
| 统计功效 | "n≥15 runs"无功效依据 | **正式功效分析 + 探索性研究声明** | Review2-C4: 缺乏样本量论证 |
| Exp3-Minimal | 两个思路，未明确实例数 | **每种操控≥5个程序化生成实例** | Review1-§4: 需做实不做点缀 |
| 阶段1门控 | 单一准确率>70% | **双层门控**：理解准确度 + 行为推理一致性 | Review1-§5: 单一指标不足 |
| Rich Non-Spatial (C2) | 天气/历史等无行为引导性描述 | **具有行为可供性的非空间描述** | Review2-C6: C2太弱会沦为稻草人 |
| 统计框架 | 阶段2用Mixed-Effects，阶段3用ANOVA | **全流程统一Mixed-Effects** | Review1-§6: 框架不一致 |
| 空间描述风格 | Neutral Structural含百分位排名 | 新增 **Absolute-Only条件**（仅绝对值，不含排名） | Review2-§4.2: 百分位隐含比较语义 |
| 模型一致性 | 混合方案（阶段1-2 DeepSeek，阶段3 Qwen-Max） | **全流程统一一个Actor模型** | Review2-§9: 跨阶段模型切换引入混淆 |
| 理论跳跃 | 声明2个跳跃 | 增加**第三跳跃**：个体空间行为→群体社会涌现 | Review2-§1.2: Space Syntax实证主要关于个体行人流 |
| 保底方案 | 未定义 | **明确Minimum Viable Paper**：阶段1+2即可成文 | Review2-C10: 时间线风险需要保底 |

---

## 第一部分：研究背景

### 1.1 问题的起源

（基本沿用v2，不再赘述。核心论点：现有LLM Agent缺乏构型级空间认知。）

### 1.2 研究空白（精确界定，沿用v2）

### 1.3 三个理论跳跃（v3新增第三跳跃）

| 跳跃 | 从 → 到 | 合理性论证 | 风险 |
|------|---------|-----------|------|
| 跳跃1 | 真实人类 → LLM Agent | LLM训练数据包含海量人类空间行为描述，可能具有隐含空间-社会常识 | LLM可能只是模仿表面模式，不具真正空间推理 |
| 跳跃2 | 物理空间 → 文字描述的空间 | 在文本世界中，Space Syntax指标代表空间特征的语义抽象 | 抽象化可能丧失物理空间的核心行为引导力 |
| **跳跃3（新增）** | **个体空间行为 → 群体社会涌现** | Space Syntax的经典实证主要关于个体行人流（natural movement）。将其推广到多Agent社会网络涌现，需要假设微观空间行为能通过交互累积产生宏观社会结构 | 个体效应可能在群体互动中被稀释或被其他因素覆盖 |

> 本研究不预设这三个跳跃必然成立，而是将其作为**待检验的实验性假设**。三阶段实验设计分别对应这三个跳跃的验证。

---

## 第二部分：研究目标与问题

### 2.1 总体目标

（沿用v2，措辞谨慎。）

### 2.2 研究问题

**RQ1（表征验证）**：Space Syntax衍生的空间结构化表征，能否提升LLM Agent的行为环境一致性（BSC），且效果超出一般性上下文丰富化？

**RQ2（认知效应分离）**：在控制拓扑必然效应的前提下，空间化表征能否显著改变Agent的行为策略与交互模式？

**RQ3（指标效应）**：各空间指标中，哪些对Agent行为影响最稳定？

**RQ4（新增 — 理论归因）**：观察到的空间-行为关联，是Space Syntax理论预测的结构性效应，还是LLM训练数据中空间常识被激活的结果？

> RQ4直接回应Review2-C5，通过反直觉空间条件进行区分。

### 2.3 空间-行为假设

（沿用v2的H1-H4修订版。H5仍为探索性目标。）

补充说明：

- **H3的可检验性前提**：需要在三种构型中确认存在足够数量（≥3个）的高Control Value节点。如果某构型中仅有1-2个高Control Value节点，H3在该构型中标注为"不适用"。
- **H2的备选方案**：如果预实验显示Openness与Connectivity高度共线（r > 0.8），H2将改为使用Mean Depth替代Openness。

---

## 第三部分：理论框架

### 3.1 与Hillier的理论对话（深化版）

在v2基础上增加两个讨论点：

**Hillier的空间句法二元性（inhabitants vs visitors）**

Hillier区分了"居民"（长期占据某空间的使用者）和"访客"（临时路过的人），两者对空间的使用模式和社会行为显著不同。在Agent模拟中：

- "常驻"在某区域的Agent（如酒馆老板Finn固定在酒馆）→ inhabitants
- "路过"的Agent（如巡逻的守卫Theron）→ visitors

**设计含义**：Spatial Perception模块应区分Agent在当前位置是"常驻"还是"访问"状态，空间描述中可标注"你已在此位置停留了X轮"。

**从个体行为到群体涌现的理论依据**

Space Syntax的natural movement理论主要解释个体行人流分布。从个体空间行为推导出群体社会涌现，依赖以下机制假设：

1. 空间构型约束Agent的相遇概率分布（拓扑效应）
2. 空间感知调节每次相遇中的交互方式和深度（认知效应）
3. 大量微观交互通过累积产生宏观社交网络结构

本研究的阶段2验证(1)+(2)，阶段3验证(3)。

### 3.2 Space Syntax核心指标（修订版）

**Integration, Connectivity, Control Value**：定义沿用v2。

**Openness vs Mean Depth — 预检验决策树**：

v2中将Visual Depth简化为Openness。但两份评审均指出Openness与Connectivity极可能高度共线。v3采用以下决策树：

```
预实验阶段：计算三种构型中 Openness 与 Connectivity 的 Pearson r

如果 r ≤ 0.8：
  → 保留 Openness 作为独立指标
  → H2 使用 Openness × Connectivity 交互假设

如果 r > 0.8：
  → 弃用 Openness
  → 改用 Mean Depth（节点到所有其他节点的平均拓扑距离）作为"隐蔽/深层程度"指标
  → H2 改为：Mean Depth 调节隐私敏感行为（高Depth=深层空间→更隐蔽）
  → 在论文中明确讨论此替代的理论代价
```

**Mean Depth的定义**：

```
Mean Depth(i) = Σ_j d(i, j) / (n - 1)
```

Mean Depth高的节点远离入口、深藏内部，与Connectivity无必然相关。这一指标在Space Syntax文献中是"空间隐蔽程度"的标准度量。

**visible(i, j)的精确定义**（如保留Openness）：

```
visible(i, j) = 1，当且仅当从 i 到 j 的最短路径上不存在
                任何标记为 "visual_blocker" 的中间节点。
```

- `visual_blocker`属性在地图设计时手工标注（如弯曲走廊的拐角节点、封闭建筑的墙壁节点）
- 标注规则在附录中完整给出，确保可复现
- 如果20节点图中visual_blocker过少导致Openness≈Connectivity，触发上述备选方案

### 3.3 指标质量预检（v3新增）

在正式实验前，对三种构型报告：

| 检查项 | 目的 |
|--------|------|
| 四个指标的Pearson相关矩阵 | 检测多重共线性 |
| 各指标的分布直方图 | 确认有足够的高/低极端值 |
| 各指标的变异系数（CV） | CV < 0.2的指标在该构型中视为"无区分力"，对应假设标注"不适用" |
| 高Control Value节点数量 | H3的可检验性前提 |
| Integration核心（top 20%）的空间分布 | 验证三种构型的设计意图 |

---

## 第四部分：技术架构——SpatialAgent-Lite

### 4.1 架构总览

（沿用v2的2模块设计：Spatial Perception + Spatial Action Sampling。）

### 4.2 模块一：Spatial Perception（修订版）

**四种表征方式（v3扩展，用于消融）**：

| 表征 | 示例 | 目的 |
|------|------|------|
| Raw Numeric | `integration=0.82, connectivity=4, depth=1.8, control=1.2` | 测试LLM对数值的理解 |
| **Absolute Structural（v3新增）** | "该位置与其他位置的平均拓扑距离为1.8步。直接连接4个相邻位置。从该位置经过可控制进出3个区域的通行。" | **不含任何排名/比较**，纯绝对事实 |
| Neutral Structural（v2主方案） | "该位置与其他位置的平均拓扑距离为1.8步（在所有位置中排第85百分位）…" | 含百分位排名，提供相对位置信息 |
| Interpretive（v1风格） | "这是人流汇聚的核心区域，容易被注意到" | 暗示性描述，测试prompt泄漏效应 |

> **v3主方案改为Absolute Structural**（而非v2的Neutral Structural），因为百分位排名隐含了比较语义。Neutral Structural降为消融对比条件，用于测试"排名信息本身的影响"。

**紧凑Schema表征（v3新增备选）**：

Review1建议测试更紧凑的格式以减少token冗余。新增以下备选：

```
[SPACE] 名称=迷雾酒馆-密室 | 距离=1.8步(深层) | 连接=2 | 控制=0.85(高) | 在场=2人(Elara,Theron) | 时段=夜晚
```

在预实验中对比Schema格式与自然语言格式的LLM理解准确度，选择更优方案。

**常驻/访问状态标注（v3新增）**：

```
你在该位置的状态：常驻（已停留12轮）
# 或
你在该位置的状态：途经（刚到达）
```

### 4.3 模块二：Spatial Action Sampling（修订版）

**关键改进：引入规则评分器替代方案**

v2中Judge使用第二个LLM，Review2-C2指出这引入了LLM先验知识的混淆。v3提供两种评分器并在消融中对比：

| 评分器 | 实现方式 | 优势 | 劣势 |
|--------|---------|------|------|
| **LLM Judge** | 独立LLM评估行为-空间匹配度 | 灵活、不需预定义规则 | 可能引入LLM先验偏见 |
| **Rule-Based Scorer** | 基于空间指标阈值的确定性评分 | 完全透明、无LLM偏见 | 泛化性弱、需手工设计规则 |

> 如果消融实验显示LLM Judge与Rule-Based Scorer效果接近，说明效果可归因于空间信息本身而非Judge的先验知识。

**Temperature参数**：

- 默认τ=0.5
- 预实验中测试τ∈{0.1, 0.3, 0.5, 0.7, 1.0}的敏感性
- τ过低（<0.2）退化为argmax（空间完全决定行为），τ过高（>0.8）接近均匀采样
- 在论文中报告τ的选择逻辑和敏感性分析

### 4.4 所有Agent条件的信息访问矩阵（v3关键新增）

| Agent条件 | Movement Policy | 空间指标 | 动态在场信息 | 拓扑邻接 | 对话空间描述 | Action Sampling |
|-----------|:-:|:-:|:-:|:-:|:-:|:-:|
| **C0: Random Walk** | 随机选相邻节点 | ✗ | ✗ | ✓(隐式) | ✗ | 标准LLM |
| **C1: Topology-Only** | LLM CoT（仅给拓扑邻接 + 地名） | ✗ | ✓ | ✓ | ✗ | 标准LLM |
| **C2: Rich Non-Spatial** | 同Topology-Only | ✗ | ✓ | ✓ | 等长度非空间描述 | 标准LLM |
| **C3: Shuffled Signal** | 同SpatialAgent | ✓(错配) | ✓ | ✓ | 错配空间描述 | Spatial Sampling |
| **C4: SpatialAgent-Lite** | LLM CoT（给空间指标+拓扑+地名） | ✓(正确) | ✓ | ✓ | Absolute Structural | Spatial Sampling |
| **C5: Judge-Only（v3新增）** | 同SpatialAgent | ✗ | ✓ | ✓ | ✗ | Spatial Sampling(Judge有空间信息) |

**C5 Judge-Only的关键作用**：

- Actor LLM不接收任何空间描述
- 但Spatial Action Sampling的Judge仍基于空间信息对候选行为评分
- 如果C5 ≈ C4，说明效果主要来自Judge的先验空间常识，Perception模块不必要
- 如果C4 > C5，说明Actor直接感知空间信息有额外价值

**Movement Policy明确分层**：

| Agent | 选择目的地时能看到什么 |
|-------|---------------------|
| Random Walk | 仅知道邻居节点列表 |
| Topology-Only | 邻居节点列表 + 地名 + 在场Agent数 |
| SpatialAgent-Lite | 邻居节点列表 + 地名 + 在场Agent数 + 各节点空间指标 |

> Topology-Only与SpatialAgent-Lite在Movement时的唯一差异是：是否看到空间指标。在Interaction时的唯一差异是：对话prompt中是否注入空间描述。这使得RQ2的分离更加干净。

---

## 第五部分：实验设计

### 5.0 预实验（v3扩展版）

#### 5.0.1 指标质量预检

计算三种构型中所有指标的分布、相关矩阵、CV值。触发Openness→Mean Depth的备选决策。

#### 5.0.2 LLM空间理解测试（双层门控）

| 层级 | 测试内容 | 通过标准 |
|------|---------|---------|
| **L1: 理解准确度** | LLM能否正确复述空间描述中的关键数值和事实？（"该位置连接几个相邻位置？""从该位置到最远位置需要几步？"） | ≥ 85% 准确率 |
| **L2: 行为推理一致性** | LLM能否基于空间描述做出方向一致的行为推断？（"在该位置适合进行私密对话吗？""如果需要快速离开，有几条路线？"） | ≥ 70% 一致性 + 推理链合理 |

如果L1通过但L2不通过：说明LLM能读懂但不能据此推理 → 需要更显式的行为可供性提示，或考虑Interpretive风格

如果L1也不通过：说明描述格式有问题 → 测试Schema格式 → 更换模型

#### 5.0.3 表征格式对比

在小规模任务上对比：

- 自然语言（Absolute Structural）
- Schema格式
- 混合格式（Schema + 关键信息的自然语言扩展）

选择LLM理解最准确且token最少的格式作为主方案。

#### 5.0.4 Temperature敏感性

测试Spatial Action Sampling中τ∈{0.1, 0.3, 0.5, 0.7, 1.0}对微任务结果的影响。

#### 5.0.5 路径偶遇概率敏感性

测试encounter_probability∈{0.2, 0.5, 0.8}对关键社交网络指标的影响，选择使Labyrinth社交密度不会被人为低估的参数。

---

### 阶段1：机制验证（预计2周）

#### Exp1A: 表征方式对比（扩展为7条件）

| 条件 | 描述 | 目的 |
|------|------|------|
| C0: No Space | 无空间信息 | 最低基线 |
| C1: Name Only | 仅地名 | 排除语义标签足够 |
| C2: Rich Non-Spatial（改进版） | 等长度**具有行为可供性**的非空间描述 | 公平排除"更多上下文=更好" |
| C3: Raw Numeric | Space Syntax数值 | 测试数值处理能力 |
| C4a: Absolute Structural（v3主方案） | 客观绝对值描述 | 核心测试 |
| C4b: Neutral Structural（含百分位） | 含排名的描述 | 测试排名信息的额外效应 |
| C5: Shuffled Signal | 错配空间信息 | 验证正确信息必要性 |

**Rich Non-Spatial (C2) 的改进设计**：

v2中C2使用无行为引导性的描述（天气、历史），被Review2指出太弱。v3改为**同样具有行为可供性的非空间描述**：

| 示例 | 行为引导方向 |
|------|------------|
| "周围传来嘈杂的争吵声和酒杯碰撞声，空气中弥漫着浓烈的酒气" | 可能引导社交/放松行为 |
| "此地弥漫着刺鼻的硫磺气味，墙壁上有暗红色的可疑痕迹" | 可能引导回避/警惕行为 |
| "你听到远处传来轻柔的竖琴声，身旁的壁炉散发着温暖的光" | 可能引导放松/开放行为 |

> C2提供**同等强度但不同维度**的行为引导——如果C4a仍优于C2，说明空间结构信息的行为引导力是独特的、不可被氛围描述替代的。

#### Exp1C: 反直觉空间条件（v3关键新增 — 回应RQ4）

**目的**：区分"Space Syntax理论预测"与"LLM空间常识"。

**设计**：构造拓扑结构与语义标签**矛盾**的空间场景：

| 场景 | 拓扑指标 | 语义标签 | Space Syntax预测 | 常识预测 |
|------|---------|---------|-----------------|---------|
| 场景X | Integration极高（全局枢纽） | "偏僻小巷" | 高社交（H1） | 低社交（小巷=冷清） |
| 场景Y | Mean Depth极高（深层内部） | "开放露台" | 低社交/高隐私 | 高社交（露台=开放） |
| 场景Z | Control Value极高（瓶颈） | "普通过道" | 守门人行为（H3） | 无特殊行为（普通过道） |

**分析逻辑**：

- 如果Agent行为遵循**拓扑指标**（场景X中增加社交）→ 支持解释A（Space Syntax理论效应）
- 如果Agent行为遵循**语义标签**（场景X中减少社交）→ 支持解释B（LLM常识激活）
- 如果两者都影响 → 混合效应，需在论文中量化各自贡献

> 这是全文**理论贡献**的关键分界线。如果解释A成立，论文标题可以保持"Space Syntax-Informed"；如果解释B主导，论文需重新定位为"空间上下文对LLM Agent行为的影响"——仍有价值，但理论深度不同。

---

### 阶段2：行为效应（预计4周）

#### Exp2: 同地图多Agent行为效应

在Plaza地图上运行6种Agent条件（C0, C1, C2, C4a, C5, **C5-JudgeOnly**），每条件200轮 × **20次重复**。

> 重复次数从v2的15次增至20次，依据功效分析（见第六部分）。

**核心比较链**（沿用v2 + 新增Judge-Only）：

```
C4a > C1 (Topology-Only)   → 空间认知有额外贡献
C4a > C2 (Rich Non-Spatial) → 不只是"更多context"
C4a > C5 (Shuffled)         → 正确空间信息是关键
C4a vs C5-JudgeOnly         → Perception vs Judge先验
C1 > C0 (Random Walk)       → 拓扑结构本身有效应
```

#### Exp2-Ablation: 架构消融（扩展版）

| 条件 | Perception模块 | Action Sampling | 评分器类型 | 目的 |
|------|:-:|:-:|:-:|------|
| Full-LLMJudge | ✓ Absolute Structural | ✓ | LLM Judge | 完整主方案 |
| Full-RuleScorer | ✓ Absolute Structural | ✓ | Rule-Based | 排除Judge LLM偏见 |
| Perception-Only | ✓ Absolute Structural | ✗ | — | 评估Perception单独贡献 |
| **JudgeOnly** | ✗ | ✓ | LLM Judge(有空间信息) | **评估Judge先验知识的贡献** |
| NoModule | ✗ | ✗ | — | =Topology-Only |

**关键对比**：

- Full-LLMJudge vs Full-RuleScorer → Judge的LLM偏见是否影响结果
- Full-LLMJudge vs JudgeOnly → Perception模块的独立价值
- Full-LLMJudge vs Perception-Only → Action Sampling的独立价值

#### Exp2-Feature: 特征消融

（沿用v2设计，逐一移除各指标。）

---

### 阶段3：社会涌现探索（预计4周）

#### Exp3: 多地图涌现分析

（沿用v2设计：3构型 × SpatialAgent + Topology-Only对照，每条件200轮 × 20次重复。）

核心分析改进：**认知增量**（SpatialAgent指标 - Topology-Only指标）跨构型是否呈现系统性模式。

#### Exp3-Minimal: 最小差异对实验（v3强化版）

**从点缀升级为主实验之一。**

| 操控类型 | 方法 | 实例数 | 控制 |
|---------|------|:------:|------|
| Integration操控 | 在基础地图上，程序化地添加/移除连接中心节点的边 | ≥5个变体 | Connectivity分布尽量不变 |
| Depth操控 | 在基础地图上，程序化地加/减深层死胡同 | ≥5个变体 | Integration分布尽量不变 |
| Control操控 | 在基础地图上，程序化地添加/移除瓶颈节点的旁路 | ≥5个变体 | 整体连通性不变 |

**程序化生成规则**：

1. 以Plaza为基础模板
2. 对目标属性做±1σ的操控（仅修改1-2条边）
3. 检查其他指标变化幅度 < 0.5σ
4. 如果无法满足约束，扩大操控幅度或丢弃该实例
5. 每种操控生成≥5个合格实例

> 这使得Exp3-Minimal不再是"作者挑选的两张地图"，而是"一族系统性操控的地图实例"，说服力显著增强。

#### Exp4: 人类评估

（沿用v2设计，40-50人，增加下述改进。）

**新增被试预测试**：

- 简短空间推理测试（Mental Rotation Test缩短版，5题）
- 按空间推理能力分组，分析评分是否存在交互效应

**评估材料**：给被试看简化ASCII地图 + Agent位置标记 + 对话内容，不展示任何空间语言描述。

---

## 第六部分：评估体系（v3重构版）

### 6.1 两阶段分离评估（核心改进）

**v2问题**：预定义的"空间-行为适配规则表"将理论假设直接编码进评估标准，构成循环定义。

**v3方案**：将评估严格拆为两个独立阶段：

**阶段A：盲行为编码（不涉及空间信息）**

标注者（LLM或人类）仅看到Agent的行为输出文本，**不看空间描述**，对行为进行分类标注：

```
行为类型 = {
  公开讨论, 低声交谈, 拒绝交流, 转移话题,
  主动搭讪, 分享敏感信息, 回避某人,
  提供帮助, 请求帮助, 交易, 巡逻, 等待, 观察
}

交互强度 = {无交互, 短暂寒暄, 深入对话, 合作行动, 冲突}

信息敏感度 = {无信息交换, 公开信息, 私人信息, 秘密信息}
```

> 标注时**完全不知道**Agent处于什么空间。这确保行为编码不受空间预期污染。

**阶段B：空间关联分析（研究者事后进行）**

将阶段A的盲编码结果与空间属性进行统计关联分析：

```python
# 不是预定义"哪个行为适合哪个空间"
# 而是统计观察"不同空间中的行为分布是否显著不同"

for each spatial_feature in [Integration, Connectivity, Depth, Control]:
    chi_square_test(
        behavior_distribution_at_high_feature_nodes,
        behavior_distribution_at_low_feature_nodes
    )
```

> **关键区别**：v2是先定义"高Openness应该→公开讨论"然后检查是否匹配；v3是先盲标行为，再统计观察行为分布是否随空间特征变化。如果变化模式恰好与Space Syntax理论一致，则为假设提供支持——但这是**观察到的关联**，不是**预编码的规则**。

### 6.2 LLM Judge设计（改进版）

**Judge Rubric严格排除表面特征**：

```
你将看到一个NPC的行为描述。请仅对行为决策本身进行分类标注，
不要评价文字质量、生动性或细节丰富程度。

请标注：
1. 行为类型（从以下选项中选择：...）
2. 交互强度（从以下选项中选择：...）
3. 信息敏感度（从以下选项中选择：...）

注意：不要推测该NPC所处的环境，仅基于行为本身标注。
```

**交叉模型验证**：

| 角色 | 模型 |
|------|------|
| Actor | 全流程统一（推荐Qwen-Max或DeepSeek-V3） |
| Judge A（行为标注） | GPT-4o |
| Judge B（复核） | DeepSeek-V3 |

报告两个Judge的Cohen's κ。如果κ < 0.6，引入人工标注子集作为金标准。

### 6.3 统计分析框架（统一版）

**全流程使用Linear Mixed-Effects Model（LMM）**：

```
阶段1：
  DV ~ condition + (1|scenario)

阶段2：
  DV ~ agent_type + (1|run) + (1|agent_pair)

阶段3：
  DV ~ agent_type * layout + (1|run) + (1|agent_pair)
  核心检验：agent_type × layout 交互项
```

**多重比较**：Benjamini-Hochberg FDR校正。

**效应量**：所有显著结果报告Cohen's d或η²。

**人类评估**：

- 主分析：LMM，DV = Likert评分, 固定效应 = condition, 随机效应 = subject
- 稳健性检验：Ordinal Logistic Regression（因Likert为序数数据）
- 报告 inter-rater agreement（Krippendorff's α），要求α ≥ 0.67

### 6.4 功效分析（v3新增）

**假设**：中等效应量 Cohen's d = 0.5, α = 0.05, power = 0.80, 双侧检验。

**简单两组比较**：所需每组n ≈ 64。

**Mixed-Effects Model下的调整**：

- 假设ICC（组内相关系数）= 0.3（同一run内轮次中等相关）
- 设计效应 DE = 1 + (m-1) × ICC，其中m=200轮
- 有效独立样本量 ≈ n_runs × (200 / DE)
- 以n_runs=20, DE≈60.7 → 每组有效样本≈66 → 刚好满足

> n=20 runs是基于功效分析的最低要求。如果预实验显示ICC更高，需增加runs数。

**对于阶段3的2×3交互效应**：

- 检测交互效应通常需要更大样本
- 在n=20 runs/cell下，只能可靠检测到 η² ≥ 0.06（中等效应）
- 如果交互效应偏小，在论文中声明为"探索性分析，报告效应量和置信区间，不仅依赖p值"

**H3的特殊考量**：

如果每种构型中高Control Value节点仅有1-2个，则H3的检验功效极低。处理方案：

- 将H3降级为"描述性观察"而非"假设检验"
- 或合并三种构型的高Control Value节点数据进行分析

---

## 第七部分：资源需求与预算

### 7.1 API调用估算（v3修订）

| 实验 | 调用量 | 备注 |
|------|--------|------|
| 预实验全套 | ~3,000 | 指标预检+LLM测试+格式对比+参数敏感性 |
| 阶段1 Exp1A(7条件)+1C(反直觉) | ~8,000 | 微任务 |
| 阶段2 Exp2(6条件×20重复) | ~240,000 | 主要成本 |
| 阶段2 消融(5条件×10重复) | ~100,000 | |
| 阶段3 Exp3(6条件×20重复) | ~240,000 | |
| 阶段3 Minimal(≥15地图变体×10重复) | ~150,000 | v3强化 |
| Judge标注 | ~80,000 | 两个Judge |
| 总计 | **~821,000** | |

### 7.2 成本估算

**推荐方案**：全流程统一使用DeepSeek-V3（Actor）+ GPT-4o-mini（Judge）

| 项目 | 成本 |
|------|------|
| API | ~¥3,000-5,000 |
| 人类评估（50人×¥30） | ¥1,500 |
| **总计** | **¥4,500-6,500** |

> 全流程统一Actor模型，避免跨阶段模型切换的混淆。

---

## 第八部分：时间线（v3修订）

```
W1-2（3月下旬-4月初）
  ├── 精读P0论文 + 写阅读笔记
  ├── 实现Space Syntax指标计算
  └── 设计三种构型 + 指标质量预检

W3（4月上旬）
  ├── 搭建模拟引擎基础版
  ├── 实现Spatial Perception（多种表征格式）
  ├── 预实验全套（LLM理解测试、格式对比、参数敏感性）
  └── → 决策点1：选定主表征格式 + 确认Openness vs Mean Depth

W4-5（4月中旬）
  ├── 运行阶段1：Exp1A + Exp1C（反直觉条件）
  └── → 决策点2：阶段1是否通过？RQ4初步倾向？

W6-8（4月下旬-5月上旬）
  ├── 实现所有6种Agent条件
  ├── 搭建完整10-NPC世界
  ├── 运行阶段2：Exp2 + 消融
  └── → 决策点3：空间认知效应是否显著？
      如果显著 → 继续阶段3
      如果不显著 → 执行Minimum Viable Paper方案

W9-12（5月中旬-6月上旬）
  ├── 运行阶段3：Exp3 + Exp3-Minimal
  ├── 网络分析 + 信息传播分析
  └── 整理所有数据 + 初步画图

W13-15（6月中旬-7月上旬）
  ├── 人类评估（设计+招募+执行）
  └── 撰写论文Method + Experiments + Results

W16-18（7月）
  ├── 撰写Introduction + Related Work + Theory + Discussion
  ├── 内部review + 修改
  └── 投稿AAMAS-27
```

### Minimum Viable Paper（保底方案）

如果阶段3因时间不足或效应不显著而无法完成，**阶段1 + 阶段2的结果足以支撑一篇有价值的论文**：

**保底论文标题**：*Does Space Syntax Help LLM Agents Behave Spatially? A Controlled Study of Spatial Representation Effects*

**保底论文贡献**：
1. 首次系统测试多种空间表征方式对LLM Agent行为的影响
2. 梯度化baseline + 反直觉条件的方法论设计
3. 区分空间认知效应与拓扑/上下文效应的实验协议

> 这篇论文不包含"社会涌现"的宏大叙事，但在方法论严谨性上可能更强。适合投AAMAS或AAAI的Agent track。

---

## 第九部分：风险评估

| 风险 | 可能性 | 应对 |
|------|--------|------|
| Openness与Connectivity共线 | 高 | 已有备选：Mean Depth |
| 反直觉条件显示LLM完全遵循语义标签 | 中 | 诚实报告→论文重新定位为"空间上下文效应"研究 |
| Judge-Only效果接近Full SpatialAgent | 中 | 说明效果来自LLM先验→改用Rule-Based Scorer作为主方案 |
| 阶段2效应不显著 | 中 | 执行MVP论文方案（阶段1+方法论贡献） |
| 功效不足（效应太小） | 中 | 报告效应量+置信区间，声明为探索性研究 |
| H3不可检验（高CV节点太少） | 高 | 降级为描述性观察 |

---

## 第十部分：论文结构草案

```
Title: Where You Are Shapes Who You Become:
       Space Syntax-Informed LLM Agents for Spatially Believable Game Worlds

1. Introduction (1.5页)
   - 问题：LLM Agent缺乏构型级空间认知
   - 三个理论跳跃的声明
   - 贡献（4-5条）

2. Related Work (1页)
   2.1 LLM-based Game Agents
   2.2 Space Syntax and Agent Simulation
   2.3 Context-Aware NPC Systems
   2.4 Embodied AI / Spatial Reasoning in LLMs

3. Theoretical Framework (1页)
   3.1 Space Syntax指标（含Openness/Depth决策、指标预检结果）
   3.2 假设H1-H4
   3.3 与Hillier的理论对话（含inhabitants/visitors）
   3.4 迁移论证（三个跳跃）

4. SpatialAgent-Lite (0.75页)
   4.1 架构（2模块）
   4.2 Spatial Perception（Absolute Structural）
   4.3 Spatial Action Sampling（LLM Judge + Rule-Based对比）
   4.4 信息访问矩阵（一表穷尽所有Agent条件）

5. Experimental Design (1.5页)
   5.1 三阶段总览 + 门控逻辑
   5.2 阶段1：表征验证 + 反直觉条件
   5.3 阶段2：行为效应 + 消融
   5.4 阶段3：涌现 + 最小差异对
   5.5 人类评估

6. Results (1.5页)
   6.1 预实验与指标预检
   6.2 阶段1: 哪种表征有效 + 理论vs常识归因
   6.3 阶段2: 认知效应分离 + Judge归因
   6.4 阶段3: 涌现分析（如完成）
   6.5 人类评估

7. Discussion (1页)
   7.1 理论验证 vs 常识激活：结合Exp1C结果正面讨论
   7.2 拓扑效应 vs 认知效应的相对贡献
   7.3 Hillier理论在虚拟Agent中的适用边界
   7.4 局限性：
       - 文本环境生态效度
       - 20节点图规模
       - LLM空间推理边界
       - 单一主题世界
       - 模型泛化性（特定LLM的结论不一定适用于其他LLM）
       - Agent密度效应（10 Agent/20节点 = 0.5 Agent/节点）
       - 200轮是否达到社交网络稳态
   7.5 对建筑学和游戏AI的启示

8. Conclusion (0.25页)

Appendix:
  A. Spatial Memory Retrieval + Spatial Planning扩展模块
  B. 完整指标预检结果（分布、相关矩阵、CV）
  C. visible(i,j)标注规则（如使用Openness）
  D. 10个NPC人设详情
  E. 所有表征格式完整文本
  F. Temperature + encounter probability敏感性分析
  G. 功效分析详情
  H. 社交网络指标随轮次的收敛曲线
```

---

## 附录：v3投稿前自检清单

### 预实验
- [ ] 指标相关矩阵已计算，Openness vs Mean Depth决策已完成
- [ ] 各指标CV已报告，标注了"不适用"的假设
- [ ] LLM空间理解双层门控已通过
- [ ] 表征格式已选定
- [ ] Temperature和encounter probability敏感性已测试

### 阶段1
- [ ] 7条件表征对比结果：C4a > C0, C1, C2, C5
- [ ] 反直觉空间条件结果：理论归因 vs 常识归因初步结论
- [ ] Exp1B排名效应（如执行）

### 阶段2
- [ ] 信息访问矩阵在论文中清晰呈现
- [ ] SpatialAgent > Topology-Only > Random Walk
- [ ] SpatialAgent > Rich Non-Spatial
- [ ] Judge-Only vs Full SpatialAgent归因分析
- [ ] LLM Judge vs Rule-Based Scorer对比
- [ ] 特征消融结果

### 阶段3（如完成）
- [ ] 认知增量跨构型分析
- [ ] Exp3-Minimal: ≥5个程序化实例/操控
- [ ] 社交网络收敛曲线已报告

### 评估
- [ ] 两阶段分离评估：盲编码→事后关联分析
- [ ] Judge标注中无空间信息泄露
- [ ] 两个Judge的Cohen's κ ≥ 0.6
- [ ] 人类评估 ≥ 40人，含空间推理预测试
- [ ] Inter-rater agreement α ≥ 0.67
- [ ] 控制问题（"感觉被操控"）得分在可接受范围

### 统计
- [ ] 全流程统一Mixed-Effects Model
- [ ] FDR校正
- [ ] 效应量报告
- [ ] 功效分析依据
- [ ] 人类评估稳健性：Ordinal Logistic Regression

### 论文措辞
- [ ] 无"prove"/"首次"等过度措辞
- [ ] Discussion中正面讨论两种解释（理论vs常识）
- [ ] Discussion中坦诚讨论所有局限性
- [ ] 全流程使用同一Actor模型
