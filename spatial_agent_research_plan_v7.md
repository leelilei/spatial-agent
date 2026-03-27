# SpatialAgent 研究计划 v7

## Where You Are Shapes Who You Become: Space Syntax-Informed LLM Agents for Spatially Believable Game Worlds

> 版本: 7.0  
> 日期: 2026-03-16  
> 作者: Li  
> 目标会议: AAMAS-27 (首选) / AAAI-27 (备选)  
> 本版本目标: 基于 `v6 review1` 与 `v6 review2` 做最后一轮投稿前收口，补齐 `TAR_run` 的统计 protocol、修正 `Exp1C` 因子解释、重构 matched initial conditions 的表述，并解决 `C6 vs C1` 的 Movement 不对等问题

---

## 修订说明：v6 → v7 核心变化

| 维度 | v6 | v7 | 修改理由 |
|------|----|----|---------|
| `TAR_run` 定义 | 连续型主实现，但未写清单个 run 如何生成标量 | **显式 protocol**：location-level summary monotonic slope（Spearman rho + Fisher z） | Review1-P0: 理论上正确，但实现上模糊 |
| TAR 线性假设 | 默认连续型回归 | **主实现改为单调相关；线性 / log-linear 仅作鲁棒性检查** | Review2-P1: 20节点图上关系可能非线性 |
| `Exp1C` 因子命名 | `topology` 高/低，实际混合了高Integration与高Depth | **改写为 composite structural profile 因子** | Review1-P0: 不能把 `H1` 和 `H2` 混成单一轴 |
| 阶段2 Perception 条件 | `C6` 同时改变到位后行为与 Movement 信息 | **拆为 `C6m` 与 `C6f`**：Matched-Movement vs Free-Movement | Review2-P0: `C6-C1` 不纯，混入 Movement 效应 |
| matched-seed 表述 | 默认视为全程方差缩减 | **改为 matched initial conditions (MIC)** + 预实验量化实际方差缩减窗口 | Review2-P0: 世界状态会快速分叉，seed matching 有效窗口可能有限 |
| 功效解释 | 默认按 `30 matched seeds` 主分析 | **功效估计按保守独立组计算；MIC 视作额外增益，不写进最低功效承诺** | 避免高估 seed blocking 的价值 |
| `C2` 非空间性 | 仅通过随机映射保证与位置解耦 | **新增 reverse-inference audit**，验证描述不泄露结构位置类型 | Review2-P1: C2 可能隐含空间语义 |
| 编码信度 | 两阶段分离评估，但信度标准未定 | **新增 coding manual + 双人 pilot + κ 阈值 + LLM-human 校准协议** | Review2-P1: 编码不可靠会污染全部主结果 |
| 时间动态解释 | 收敛与分段分析 | **新增 spatial priming vs sustained guidance 框架** | Review2-P1: 记忆累积可能吸收空间效应 |
| 模型选择 | 未明确主 Actor | **指定主模型 + robustness subset** | Review2-P2: 模型选择影响结论外部效度 |
| Exp1C 场景数 | 5 scenes / cell | **提升为 10 scenes / cell** | Review2-P2: 随机场景效应组数过少 |
| 收敛判据 | “3窗口<5%”但未操作化 | **明确定义 delta 指标 + holdout 复检** | Review2-P2: 防止假稳态 |
| 阶段3启动条件 | “显著或稳定中等效应” | **量化为 p / d / 方向一致性三重门槛** | Review2-P2: 启动条件过松 |

---

## 第一部分：研究背景

### 1.1 问题的起源

现有 LLM Agent 研究通常较好建模了两类信息：

- **WHO**：身份、人格、目标、背景
- **WHAT**：事件、记忆、任务与互动历史

但对第三类信息的系统建模仍然不足：

- **WHERE**：空间构型、深度、可达性、瓶颈性、可视性

本研究关注的不是“有没有地点信息”，而是是否存在**构型级空间表征**。现有系统大多只利用地点名称、语义标签或简单邻接关系，而没有将 Space Syntax 作为一套结构理论引入 Agent 决策。

### 1.2 研究空白

本研究面向三个明确空白：

1. **表征空白**：缺乏 Space Syntax 风格的结构化空间输入。
2. **识别空白**：缺乏将拓扑必然效应与空间化架构增量效应分离的实验协议。
3. **理论空白**：缺乏建筑学 Space Syntax 与 LLM 多 Agent 社会模拟之间的系统对话。

### 1.3 三个理论跳跃

| 跳跃 | 从 → 到 | 合理性论证 | 风险 |
|------|---------|-----------|------|
| 跳跃1 | 真实人类 → LLM Agent | LLM 训练语料可能编码了人类空间-社会常识 | 模型可能只是语言模式复现，而非真正空间推理 |
| 跳跃2 | 物理空间 → 文本化空间 | 拓扑指标可抽象为结构性文本描述 | 物理 affordance 可能在文本中被削弱 |
| 跳跃3 | 个体空间行为 → 群体社会涌现 | 微观空间偏移可能累积成宏观网络结构 | 个体效应可能被时间动态、记忆与历史分叉稀释 |

> `v7` 的核心策略不变：先扎实验证跳跃1和跳跃2，再将跳跃3作为可选扩展，而非主论文必要条件。

---

## 第二部分：研究目标、问题与主张边界

### 2.1 总体目标

本研究不试图“完整验证 Space Syntax 在文本 Agent 世界中成立”，而是回答三个更可 defend 的问题：

1. 结构化空间表征能否稳定改变 LLM Agent 行为？
2. 这种改变能否超出稳定的非空间 affordance 基线？
3. 这种改变中有多少沿着 Space Syntax 理论方向发生？

### 2.2 研究问题

**RQ1（验证性）**：结构化空间表征是否比无空间、地点名、原始数值和稳定非空间 affordance 基线更能诱发空间响应？

**RQ2（验证性）**：在控制拓扑必然效应的前提下，完整空间化架构相对 `Topology-Only` 是否带来可检测的、具有实践意义的增量？

**RQ3（验证性）**：`Perception` 对到位后行为的影响、`Perception` 对 Movement 的影响、以及 `Action Sampling` 的影响，三者分别是多少？

**RQ4（探索性）**：观测到的空间行为响应更接近结构性 Space Syntax 效应，还是更接近 LLM 已有语义常识的激活？

### 2.3 验证性 / 探索性分层

| 内容 | 性质 | 是否主论文核心 |
|------|------|:--------------:|
| 阶段1：表征有效性（Exp1A） | 验证性 | 是 |
| 阶段2：核心 5 条件架构比较 | 验证性 | 是 |
| 阶段2：模块分解（`C6m/C6f/C4/C1`） | 验证性 | 是 |
| 阶段1：反直觉 2×2 设计（Exp1C） | 探索性高价值 | 是 |
| 阶段2：`Shuffled/Judge-Only/Fixed-Path/Rule-Based` | 机制探测 | 否，附录主报 |
| 阶段3：多地图涌现 | 探索性扩展 | 否 |
| 人类评估 | 外部有效性增强 | 否，时间允许时做 |

### 2.4 主张边界

`v7` 只尝试支撑以下级别的结论：

- 结构化空间表征可以系统性影响 LLM Agent 行为
- 这种影响在若干关键比较中超出稳定的非空间 affordance 基线
- 其中有一部分影响沿着 Space Syntax 理论方向发生

`v7` 不预先声称：

- 完整验证 Space Syntax
- 证明所有社会涌现都由空间构型因果决定
- 证明单一空间指标具有跨环境普适性
- 排除所有中小效应的不存在

> `v7` 在验证性层面的目标是检测**稳健且具有实践意义的中到大效应**，而非穷尽性排除所有中小效应。

---

## 第三部分：理论框架与主因变量

### 3.1 H1-H3 的推导链

#### H1：Integration 与社交频率

| 层级 | 内容 |
|------|------|
| Hillier 原始理论 | 高 Integration 空间汇聚自然流动，形成公共活动中心 |
| 物理空间实证 | 高 Integration 节点通常承载更高人流与更多面对面互动 |
| 文本 Agent 推导 | 若 Agent 得知某位置全局可达性高、像结构枢纽，则更可能主动接触、停留或公开互动 |
| 失效条件 | 地图过小、角色内向性覆盖空间效应、Movement 不受结构偏好影响 |

#### H2：Mean Depth / Openness 与私密行为

| 层级 | 内容 |
|------|------|
| Hillier 原始理论 | 深层空间对应更强的隐私梯度 |
| 物理空间实证 | 深层或低可见空间更容易承载私密、敏感话题 |
| 文本 Agent 推导 | 当描述传达“远离主通路 / 深藏内部 / 不易被打断”时，Agent 更可能低声交流或分享敏感信息 |
| 失效条件 | 指标共线、角色无隐私需求、语义标签压过结构信号 |

#### H3：Control Value 与守门行为

| 层级 | 内容 |
|------|------|
| Hillier 原始理论 | 高 Control 节点对邻近流动具有结构性控制力 |
| 物理空间实证 | 结构瓶颈更易承载监视、拦截、信息中介等行为 |
| 文本 Agent 推导 | 当描述传达“此处控制多条通路进出”时，Agent 更可能表现出巡视、阻拦、观察和筛选信息的行为 |
| 失效条件 | 高 Control 节点过少、角色设定不允许守门行为出现 |

### 3.2 指标决策树

核心指标：

- `Integration`
- `Connectivity`
- `Control Value`
- `Openness` 或 `Mean Depth`

决策规则：

```text
如果 Openness 与 Connectivity 的 r <= 0.8：
  保留 Openness

如果 r > 0.8：
  改用 Mean Depth 作为 H2 主指标
```

> `v7` 默认主文使用 `Mean Depth` 作为 H2 的稳健候选；`Openness` 若保留，仅作为附加分析。

### 3.3 双主因变量：BSR 与 TAR

#### 3.3.1 Unsigned BSR

`BSR`（Behavioral Spatial Responsiveness）回答：

> 行为是否随着空间特征发生系统性变化？

它衡量的是**响应存在性**，不区分方向。

#### 3.3.2 Signed TAR

`TAR`（Theory-Aligned Responsiveness）回答：

> 这种响应是否沿着理论预测方向发生？

它衡量的是**方向对齐性**。

### 3.4 `TAR_run` 的显式计算 protocol（v7关键新增）

`v6` 的问题在于：虽然提出了连续型 TAR，但没有写清楚**单个 run 如何生成一个稳定的 TAR 标量**。`v7` 采用如下 protocol。

#### Step 1：事件级到 location-level 的汇总

对每个 `run`、每个假设 `Hk`：

1. 收集该 run 中所有行为事件
2. 按 location 聚合
3. 只保留在该 run 中被访问次数 `>= 5` 的 location
4. 对每个 location 计算对应行为率：

```text
H1: sociality_rate(location)
H2: privacy_behavior_rate(location)
H3: gatekeeping_rate(location)
```

#### Step 2：计算 location-level 的单调关联

对每个 run，计算：

```text
rho_H1_run = Spearman( sociality_rate(location), standardized_Integration(location) )
rho_H2_run = Spearman( privacy_behavior_rate(location), standardized_MeanDepth(location) )
rho_H3_run = Spearman( gatekeeping_rate(location), standardized_Control(location) )
```

#### Step 3：Fisher z 变换

将单个 run 内的秩相关转换成更适合后续建模的标量：

```text
TAR_Hk_run = atanh(rho_Hk_run)
```

解释：

- `TAR > 0`：与理论方向一致
- `TAR = 0`：无明显方向性支持
- `TAR < 0`：与理论方向相反

#### Step 4：构造 hypothesis-specific BSR

对于每个 run 和每个假设：

```text
BSR_Hk_run = abs(TAR_Hk_run)
```

也就是说：

- `BSR` 衡量关联强度
- `TAR` 衡量方向

#### Step 5：overall BSR 的聚合

若需要一个总体指标，则定义为：

```text
Overall_BSR_run = mean( BSR_H1_run, BSR_H2_run, BSR_H3_run* )
```

其中：

- 若 `H3` 在该图中不可检验（高 Control 节点不足），则 `H3` 从 overall BSR 中剔除

### 3.5 TAR 的鲁棒性分析

为回应“线性假设可能不成立”的问题，`v7` 明确将线性与阈值关系分析降为**鲁棒性检查**，而不作为主实现。

对每个假设，补充报告：

1. **线性 slope**：location-level OLS 斜率
2. **log-linear**：如适用，对特征做 log 变换后的 slope
3. **分位差值图示**：top 25% vs bottom 25% location difference

若三者方向一致，则增强结论可信度；若方向冲突，则主结论保持以 Spearman/Fisher-z 实现为准，并在 Discussion 中承认关系形态不确定。

### 3.6 辅助因变量

- `Behavioral Entropy`
- 平均交互强度
- 信息敏感度比例
- 守门行为比例

这些指标用于描述模式，不承担主理论验证职责。

### 3.7 空间启动 vs 持续引导（v7新增理论区分）

在长时程模拟中，空间信息可能只在前期直接影响行为，后期则被记忆吸收并维持。

因此 `v7` 显式区分：

- **Spatial Priming**：空间描述对早期行为的直接启动作用
- **Sustained Spatial Guidance**：空间效应在中后期是否仍持续独立存在

这一区分将在阶段2的时间分段分析中正面检验。

---

## 第四部分：环境、模型、NPC 与控制变量

### 4.1 环境设置

验证性阶段只使用一张主地图：

- `Plaza`

探索性扩展：

- `Labyrinth`
- `Bridge`

三图的区分依据是指标分布，而不是名称：

- `Plaza`：Integration 高峰集中
- `Labyrinth`：Depth 高、Connectivity 低
- `Bridge`：瓶颈和多中心更明显

### 4.2 Actor / Judge 模型选择（v7修订：开源优先策略）

#### 设计原则

`v7` 采用**开源模型优先**策略，核心理由：

1. **可复现性**：开源模型权重公开，审稿人与后续研究者可精确复现实验。闭源模型（如 GPT 系列）随时可能更新或下架，无法保证长期可复现性
2. **成本效率**：通过第三方 API 平台（国产特价渠道），开源模型成本极低，允许在不压缩实验规模的情况下完成全部实验
3. **透明性**：Actor 和 Judge 的行为模式均可追溯到公开权重，增强结论可审查性

#### 主 Actor

- **Primary Actor = Qwen3.5-Plus（版本 2026-02-15）**

| 属性 | 详情 |
|------|------|
| 参数量 | 397B MoE，170B 激活 |
| 开源状态 | ✅ 权重公开（HuggingFace / ModelScope） |
| 能力定位 | 对标 Gemini-3-Pro / GPT-5.2 |
| API 成本 | 输入 ¥0.56/M tokens，输出 ¥3.36/M tokens |

选择理由：

1. 开源可复现：论文可写明 "Qwen3.5-Plus (2026-02-15), weights available at [link]"
2. 能力足够：397B MoE 模型在角色扮演、指令遵循、长上下文理解上均达到主流水平
3. 成本极低：全流程 Actor 成本可控在千元以内

#### 主 Judge

- **Primary Judge = Qwen3.5-Plus（同 Actor）**

| 属性 | 详情 |
|------|------|
| API 成本 | 同 Actor：输入 ¥0.56/M，输出 ¥3.36/M |

> **Actor-Judge 同源风险与对策**：Actor 和 Judge 使用同一模型，可能存在"自己生成、自己高评"的偏见。`v7` 通过三重机制控制此风险：
>
> 1. **Rule-Based Scorer 对照**：手工规则评分器不依赖任何 LLM，作为 Judge 偏见的无偏探针
> 2. **两阶段分离评估**：盲行为编码阶段完全不使用 LLM Judge，由人类 / 独立编码方案完成
> 3. **鲁棒性 Judge 交叉验证**：使用 DeepSeek-V3.2（不同架构、不同训练数据）作为第二 Judge

#### 鲁棒性模型子集

在阶段1与阶段2的关键比较子集上，额外使用不同厂商模型进行交叉验证：

| 角色 | 鲁棒性模型 | 成本 | 理由 |
|------|-----------|------|------|
| 鲁棒性 Actor | **DeepSeek-V3.2-exp** | 输入+输出 ¥1.4/M tokens | 不同架构（MoE vs Dense），不同训练数据 |
| 鲁棒性 Judge | **DeepSeek-V3.2-exp** | 同上 | 检测 Qwen Judge 的模型特异性偏见 |

规模：

- `10` 个 MIC seeds
- `3` 个关键条件（`C1 / C6m / C4`）
- `250` 轮

若主效应方向在两个模型间一致：增强结论的外部效度。
若方向不一致：在 Discussion 中明确报告模型依赖性，并讨论哪些结论是模型鲁棒的。

### 4.3 NPC 角色设计标准化

10 个 NPC 沿三个维度平衡设计：

| 维度 | 水平 | 分布 |
|------|------|------|
| 社交倾向 | 高 / 中 / 低 | 4 / 3 / 3 |
| 职业角色 | 公共型 / 中性型 / 隐蔽型 | 3-4 / 3 / 3-4 |
| 目标类型 | 社交型 / 信息型 / 独立型 | 3-4 / 3 / 3-4 |

约束：

1. 社交倾向与职业正交
2. 角色描述不写入空间偏好
3. 背景故事不绑定固定地点

### 4.4 Matched Initial Conditions（MIC）设计

为回应 review 中“matched-seed 的有效窗口可能被高估”的问题，`v7` 明确改用更诚实的术语：

> **Matched Initial Conditions (MIC)**  
> 而不是隐含全程可比性的 “matched-seed”

MIC 的含义是：

- 初始 NPC 位置相同
- 初始环境随机事件表相同
- 初始 `C2` 描述映射相同
- 但不声称从第 50 轮开始世界状态仍保持可比

### 4.5 MIC 有效窗口预检（v7新增）

在预实验中，量化 MIC 的实际方差缩减作用：

1. 计算 `0-50`、`51-100`、`101-200` 三个时间窗口内的条件差值方差
2. 比较：

```text
Var_matched(condition_diff) vs Var_unmatched(condition_diff)
```

3. 报告 `ICC(seed)` 或等价的方差缩减比例

解释规则：

- 若 `ICC(seed) >= 0.1`：说明 MIC 在该窗口仍有实质控制力
- 若 `ICC(seed) < 0.1`：说明 MIC 的价值主要限于早期窗口

> 重要：`v7` 的主功效估计**不依赖** MIC 带来的额外方差缩减。  
> MIC 被视为增益，而不是最低功效承诺的前提。

### 4.6 Prompt 位置控制

预实验比较三种插入位置：

- 系统 prompt 末尾
- 当前情境中部
- 用户指令前

选取最稳定的位置并固定。

---

## 第五部分：SpatialAgent-Lite 架构与条件矩阵

### 5.1 核心架构

只保留两个主模块：

1. `Spatial Perception`
2. `Spatial Action Sampling`

不把 `Memory` 和 `Planning` 作为主贡献，以避免归因污染。

### 5.2 Spatial Perception

主表征使用 `Absolute Structural`：

```text
该位置与其他位置的平均拓扑距离为 1.8 步。
该位置直接连接 4 个相邻位置。
经过该位置可控制进出 3 个区域的通行。
此刻在场 2 人：Elara、Theron。
```

优点：

- 不含排名与隐含比较语义
- 不直接告诉 Agent “该做什么”
- 易于与 `Name Only`、`Raw Numeric`、`C2` 对照

### 5.3 Spatial Action Sampling

流程：

1. Actor 生成 `K=5` 个候选行为
2. Judge 根据空间上下文评分
3. `softmax(score / tau)` 采样

设置：

- 默认 `tau = 0.5`
- `Rule-Based Scorer` 仅作为鲁棒性对照

### 5.4 条件矩阵（v7修订）

#### 5.4.1 验证性核心条件

| 条件 | Movement 信息 | 对话空间描述 | Sampling | 用途 |
|------|---------------|--------------|----------|------|
| `C1 Topology-Only` | 邻接 + 地名 + 在场数 | 无 | 无 | 主基线 |
| `C2 Stable Non-Spatial Affordance` | 同 `C1` | 稳定非空间 affordance 描述 | 无 | 主非空间对照 |
| `C6m Perception-Only (Matched Movement)` | **同 `C1`** | Absolute Structural | 无 | **纯到位后 Perception 效应** |
| `C6f Perception-Only (Free Movement)` | 空间指标 + 邻接 + 地名 + 在场数 | Absolute Structural | 无 | **Perception 对 Movement 的额外效应** |
| `C4 Full SpatialAgent` | 同 `C6f` | Absolute Structural | 有 | 完整系统 |

#### 5.4.2 探索性机制条件

| 条件 | 作用 |
|------|------|
| `C3 Shuffled Signal` | 检验正确空间信息是否必要 |
| `C5 Judge-Only` | 检验 Judge 先验知识是否足以制造大部分效应 |
| `C7 Fixed-Path` | 在固定路径下检验到位后认知效应 |
| `Full-RuleScorer` | 检查 LLM Judge 是否系统性放大效应 |

### 5.5 `C2` 的精确定义与非空间性验证（v7新增）

`C2` 被精确定义为：

> **stable non-spatial affordance baseline**

其本质不是纯 token-length control，而是：

- 稳定
- 可行动
- 与空间结构解耦

#### 描述池生成规则

1. 描述可以引导放松、警惕、好奇、社交等行为
2. 不允许出现明确地点名、方位词、出入口、深层/中心等结构暗示
3. run 内固定，runs 间随机重新映射

#### reverse-inference audit（v7新增）

为防止 `C2` 描述泄露空间结构信息，在正式实验前执行：

1. 让独立 LLM 与人类评估者看到单条 `C2` 描述
2. 询问其推断该地点是否可能：
   - 高 / 低 Integration
   - 高 / 低 Mean Depth
   - 高 / 低 Control
3. 若某条描述在任一维度上的推断准确率明显高于随机水平（例如 `> 65%`），则该描述被删除或改写

> 只有通过 reverse-inference audit 的 `C2` 描述，才能进入正式描述池。

---

## 第六部分：实验设计

## 6.0 预实验

### 6.0.1 指标质量预检

报告：

- 指标相关矩阵
- 分布直方图
- `CV`
- 高 `Control` 节点数量

规则：

- `CV < 0.2` 的指标视为低区分力
- 若高 `Control` 节点少于 `3` 个，则 `H3` 降级为描述性观察

### 6.0.2 LLM 空间理解门控

两层：

1. `Comprehension`
2. `Behavioral Inference`

通过标准：

- `Comprehension >= 85%`
- `Behavioral Inference >= 70%`

### 6.0.3 Prompt 位置测试

在微任务上测试三种插入位置并固定最稳定方案。

### 6.0.4 Lexical Norming（Exp1C 必做）

对候选语义标签收集五维评分：

- `publicness`
- `privacy`
- `danger`
- `valence`
- `brightness`

仅保留：

- 在“公共 / 私密”维度上差异大
- 在其他维度上差异尽量小的标签

### 6.0.5 MIC 有效窗口 pilot

比较 matched 与 unmatched 条件差异方差在三个时间窗口中的变化，量化 `ICC(seed)`。

### 6.0.6 收敛性 pilot（v7操作化）

在 `Plaza` 上先跑小规模模拟，观察：

- 网络密度
- 聚类系数
- degree Gini
- 平均交互强度

定义：

```text
delta_t(metric) = | mean_t - mean_{t-1} | / max(sd_all_windows, epsilon)
```

稳态判据：

1. 对所有主网络指标，连续 `3` 个窗口（每窗口 `20` 轮）满足 `delta_t < 0.2`
2. 在达到该判据后，继续运行 `50` 轮 holdout
3. 若 holdout 期间所有指标仍在同一稳定带内，则视为达到稳态

若 `200` 轮不足，则阶段2 / 3 提升到 `300` 轮。

---

## 6.1 阶段1：表征有效性

### Exp1A：6 条件微任务对比

| 条件 | 描述 |
|------|------|
| `C0` | No Space |
| `C1` | Name Only |
| `C2` | Stable Non-Spatial Affordance |
| `C3` | Raw Numeric |
| `C4` | Absolute Structural |
| `C5` | Shuffled Signal |

微任务：

1. 是否透露敏感信息
2. 是否主动搭话
3. 多位置选择
4. 是否停留 / 离开

主比较：

- `C4 > C0`
- `C4 > C1`
- `C4 > C2`
- `C4 > C3`
- `C4 > C5`

主报告：

- hypothesis-specific `BSR`
- `TAR_H1`
- `TAR_H2`

### Exp1C：反直觉 2×2 设计（v7重命名）

#### 核心修正

`v6` 的问题是把“高 Integration”与“高 Depth”混成了一个看似单一的 `topology` 因子。`v7` 明确承认这里操控的是：

> **composite structural profile**

即：

- **public-structural profile**：高 Integration、浅层、接近公共核心
- **private-structural profile**：低 Integration、深层、接近内部区域

因此 `Exp1C` 的两个因子变为：

- `Structural Profile`: public-structural / private-structural
- `Semantic Label`: public / private

形成四个 cell：

| | 语义=公共 | 语义=私密 |
|---|:---:|:---:|
| public-structural profile | 一致 | 冲突 |
| private-structural profile | 冲突 | 一致 |

每个 cell：

- `10` 个独立场景
- 每场景 `20` 个微任务

模型：

```text
DV ~ structural_profile * semantic_label + (1|scenario)
```

解释：

- `structural_profile` 主效应：复合结构信号
- `semantic_label` 主效应：语义常识
- 交互项：结构信号与语义标签冲突时的主导关系

> `Exp1C` 的结论必须被解释为：  
> “复合结构 profile 与语义标签之间的竞争关系”，  
> 而不是单独的 `Integration` 或 `Depth` 因子因果检验。

> `Exp1C` 仍是探索性高价值证据，不承担确认性主结论。

---

## 6.2 阶段2：架构增量效应与模块分解

### 6.2.1 范围收缩

阶段2只在 `Plaza` 上做验证性主分析。

目的：

- 不把跨地图泛化问题混入确认性阶段
- 把资源集中到最关键的架构比较

### 6.2.2 Matched Initial Conditions (MIC) 设计

阶段2所有验证性核心条件采用 **MIC / blocked design**：

```text
for seed in 1..30:
  固定 NPC 初始位置分配
  固定外部随机事件序列
  固定 C2 描述池映射
  固定 warm-up 前 5 轮的环境初始状态

  在 C1 / C2 / C6m / C6f / C4 下分别运行
```

这意味着：

- 同一个 `seed` 代表同一个初始世界实例
- 条件差异尽量只来自架构本身
- 但不声称第 100 轮后世界状态仍“严格匹配”

### 6.2.3 核心验证性条件与样本量

核心条件：

- `C1 Topology-Only`
- `C2 Stable Non-Spatial Affordance`
- `C6m Perception-Only (Matched Movement)`
- `C6f Perception-Only (Free Movement)`
- `C4 Full SpatialAgent`

运行参数：

- `30` 个 MIC seeds
- 每个 seed 在 5 个条件下各运行一次
- 每 run `200-300` 轮（由收敛 pilot 决定）
- `10` 个 NPC

### 6.2.4 阶段2主比较链（v7修正）

`v7` 的模块分解如下：

```text
主比较 A: C4 - C1
  = 完整空间化架构相对 topology-only 的总系统增益

主比较 B: C6m - C1
  = 纯到位后 Perception 效应

主比较 C: C6m - C2
  = 空间结构信息 vs 稳定非空间 affordance 基线（控制 Movement，控制无 Sampling）

主比较 D: C6f - C6m
  = Perception 对 Movement 决策的额外贡献

主比较 E: C4 - C6f
  = Action Sampling 的增量贡献
```

这意味着：

```text
Total architecture effect
  = (C6m - C1)            # 到位后 Perception
  + (C6f - C6m)           # Movement 受空间信息影响
  + (C4 - C6f)            # Sampling 贡献
```

> 这是 `v7` 最关键的结构性修复：  
> 彻底解决了 `v6` 中 `C6-C1` 混入 Movement 效应的问题。

### 6.2.5 阶段2主分析模型

#### 一级：MIC run-level 主验证模型

每个 `seed × condition` 汇总成一个数据点。

主模型：

```text
DV_run ~ condition + (1|seed)
```

适用于：

- `BSR_H1_run`
- `BSR_H2_run`
- `TAR_H1_run`
- `TAR_H2_run`
- `entropy_run`

#### 二级：agent × seed 聚合异质性模型

每个 `agent × seed × condition` 聚合成一个数据点：

```text
DV_agent_seed ~ condition + social_tendency + condition:social_tendency
                + (1|seed) + (1|agent_id)
```

用于：

- 检查空间效应是否受社交倾向调节
- 检查哪些角色类型更依赖空间化架构

### 6.2.6 早期窗口分析：Spatial Priming

为区分“空间直接影响”与“记忆维持后的惯性模式”，`v7` 预注册一个早期窗口分析：

- **Primary early window = 前 50 轮**

报告：

1. `0-50` 轮的 run-level `BSR/TAR`
2. 全程 `0-200` 或 `0-300` 轮的 run-level `BSR/TAR`

解释：

- 若早期效应强、后期减弱：空间信息更像 priming
- 若早期与后期都稳定：空间信息更像 sustained guidance
- 若后期更强：可能说明空间信息通过记忆与历史路径被放大

### 6.2.7 探索性机制条件

以下条件只做机制探测：

- `C3 Shuffled Signal`
- `C5 Judge-Only`
- `C7 Fixed-Path`
- `Full-RuleScorer`

运行规模：

- `12-20` 个 MIC seeds

其中：

- `C7 Fixed-Path` 提升到至少 `20` 个 seeds  
  因为它对验证“Movement vs 到位后行为”的分离具有较高解释价值

### 6.2.8 控制位置后的条件效应

探索性模型：

```text
DV_event ~ condition + spatial_features + (1|seed) + (1|agent_id) + (1|location)
```

解释：

> 在同一 location 上比较不同条件 Agent 的行为差异。

### 6.2.9 时间动态分析

阶段2必须报告：

1. 收敛曲线
2. 前半程 vs 后半程比较
3. 前 50 轮 priming 分析

模型：

```text
DV_event ~ condition * time_block + (1|seed) + (1|agent_id)
```

其中：

- `time_block` 至少包括 `0-50`, `51-100`, `101-200`

---

## 6.3 阶段3：探索性扩展

### 6.3.1 启动条件（v7量化）

仅当满足以下任一条件时才进入阶段3：

1. 在至少一个主验证性对比上，run-level 主分析达到：
   - `FDR-corrected p < 0.05`
   - 且 `d >= 0.5`
2. 或虽未显著，但同时满足：
   - run-level `d >= 0.5`
   - 前 50 轮与全程方向一致
   - event-level 95% CI 不跨 0

### 6.3.2 多地图分析

使用：

- `Plaza`
- `Labyrinth`
- `Bridge`

目的：

- 观察方向是否跨构型稳定
- 观察架构增量是否受构型调节

规模：

- `15` 个 MIC seeds / cell

### 6.3.3 Exp3-Minimal

仅在可生成性 pilot 成功时执行；否则降级为描述性案例，不做统计推断。

---

## 第七部分：评估、编码与统计分析

### 7.1 两阶段分离评估

#### 阶段A：盲行为编码

编码者只看行为文本，不看空间信息。

编码维度：

- 行为类型
- 交互强度
- 信息敏感度
- 守门 / 监视 / 拦截行为

#### 阶段B：空间关联分析

研究者将盲编码结果与空间特征做事后关联。

### 7.2 编码信度协议（v7新增）

#### 7.2.1 Coding Manual

在正式编码前先制定 coding manual，包含：

- 每类行为的定义
- 边界案例
- 正例 / 反例
- 多标签冲突处理原则

#### 7.2.2 Human pilot coding

随机抽取 `200-300` 条行为样本，由两名人类编码者独立编码。

信度阈值：

- 行为类型：`Cohen's kappa >= 0.70`
- 交互强度：`kappa >= 0.67`
- 信息敏感度：`kappa >= 0.67`
- 守门行为：`kappa >= 0.60`

若不达标：

1. 收缩编码类别
2. 修订 coding manual
3. 重新进行 pilot

#### 7.2.3 LLM-human calibration

在 human gold subset 上评估 LLM Judge：

- 若某维度上 `LLM-human kappa < 0.60`
- 该维度不能直接进入主结果

处理方案：

1. 改进 prompt
2. 降低标签粒度
3. 或在该维度上改用人类编码子集报告

### 7.3 主验证分析

主结论只基于：

- MIC run-level 分析

主结果包括：

- `BSR_H1_run`
- `BSR_H2_run`
- `TAR_H1_run`
- `TAR_H2_run`
- `entropy_run`

### 7.4 异质性与事件级分析

以下分析不进入摘要主 claim：

- `agent × seed` 聚合模型
- event-level 模型
- `Fixed-Path`
- `Judge-Only`
- `Rule-Based`

这些分析只用于：

- 模式解释
- 效应量估计
- 机制探测

### 7.5 功效分析

#### 主验证分析

在 `30` 个 MIC seeds 下，按保守独立组估计，两组 run-level 比较的最小可检测效应约为：

- `d >= 0.74`

> 重要：这个门槛**不假定** MIC 带来的额外方差缩减。  
> 若 MIC 在早期窗口中确实降低方差，则实际功效可能更高；若其效力很弱，当前估计仍然成立。

#### 事件级补充

考虑依赖结构后，事件级分析可帮助估计：

- `d ≈ 0.5` 量级的中等效应

### 7.6 统计规则

- `Benjamini-Hochberg FDR`
- 报告 `p 值 + 效应量 + 95% CI`
- 若 run-level 不显著但 event-level 显著：
  - 只能报告为“存在中小效应迹象”
  - 不能上升为主结论

### 7.7 LLM Judge 偏见检测

通过三种方式：

1. `Shuffled` 条件作为偏见探针
2. 人类-LLM 标注一致性分析
3. `Rule-Based` 与 `LLM Judge` 结果对照

---

## 第八部分：预算、时间线与保底论文

### 8.1 成本估算的价格假设（2026-03 实际平台价格）

以下成本基于第三方 API 平台的**国产特价渠道**实际价格。该渠道比模型官方价格低约 30%，是目前国内研究者常用的 API 接入方式。

| 模型 | 用途 | 输入价格 (¥/M tokens) | 输出价格 (¥/M tokens) | 渠道 |
|------|------|---------------------:|---------------------:|------|
| `Qwen3.5-Plus` | 主 Actor + 主 Judge | `¥0.56` | `¥3.36` | 国产特价 |
| `DeepSeek-V3.2-exp` | 鲁棒性 Actor + Judge | `¥1.40` | `¥1.40` | 国产特价 |

> **成本优势来源**：
> 1. 开源模型优先策略：Qwen3.5-Plus 和 DeepSeek-V3.2 均为开源模型，API 价格远低于 GPT 系列
> 2. 第三方平台聚合：国产特价渠道比官方价格再低约 30%
> 3. Actor 和 Judge 使用同一模型：无需为 Judge 单独支付高价闭源模型费用

### 8.2 Token 与调用量假设

为了让预算可追踪，`v7` 统一采用如下估算假设。

#### 8.2.1 单次调用的 token 与成本假设

| 调用类型 | 输入 tokens | 输出 tokens | 单次成本 (Qwen3.5-Plus) | 说明 |
|----------|------------:|------------:|------------------------:|------|
| 微任务 Actor 调用 | `1,000` | `120` | `¥0.00096` | 用于 Exp1A、Exp1C、理解测试、prompt 位置测试 |
| 非 Sampling 模拟 Actor 回合 | `1,500` | `180` | `¥0.00145` | `C1/C2/C6m/C6f` 等 |
| Sampling 模拟 Actor 回合 | `1,800` | `250` | `¥0.00185` | `C4/C3/C5/C7` 等，需生成候选行为 |
| Judge 评分调用 | `1,400` | `120` | `¥0.00119` | 对候选行为进行空间适配评分 |

> 单次成本计算公式：输入 tokens × ¥0.56/M + 输出 tokens × ¥3.36/M
>
> 这些数字是偏保守的中位估计。真实值会随 prompt 长度、记忆拼接策略和输出约束而变化。

#### 8.2.2 长时程模拟的轮次假设

预算采用：

- **基线估算轮次 = 250 轮 / run**

理由：

- `v7` 计划中正式轮次是 `200-300`，由收敛 pilot 决定
- 预算用 `250` 作为中间值，便于做中位数估算

如果最后收敛 pilot 表明需要 `300` 轮，则长时程实验的 API 成本大约在当前基础上**上浮 20%**。

### 8.3 分实验成本估算

> 以下所有估算基于 Qwen3.5-Plus 国产特价渠道价格（输入 ¥0.56/M，输出 ¥3.36/M）。
> 鲁棒性子集使用 DeepSeek-V3.2-exp（输入+输出 ¥1.4/M）。

#### 8.3.1 预实验

预实验包含：

- lexical norming
- `C2` reverse-inference audit
- LLM 理解门控
- prompt 位置测试
- MIC 有效窗口 pilot
- 收敛性 pilot
- coding manual pilot 的 LLM 子集

按中位估算，可近似为：

- `~100,000` 次 Actor turns 的等价量
- `~20,000` 次 Judge 调用的等价量

估算成本：

| 组成 | 估算成本 |
|------|---------:|
| Actor（Qwen3.5-Plus） | `~¥145` |
| Judge（Qwen3.5-Plus） | `~¥24` |
| 小计 | **`~¥170`** |

#### 8.3.2 阶段1：Exp1A + Exp1C

按当前设计：

- Exp1A 约 `1,440` 个微任务调用量级
- Exp1C 约 `10 scenes × 4 cells × 20 tasks = 800` 个微任务
- 加上少量重复与调试，保守按 `3,000` 个微任务调用估算

估算成本：

| 组成 | 估算成本 |
|------|---------:|
| Actor（Qwen3.5-Plus） | `~¥3` |
| 小计 | **`~¥3`** |

> 阶段1的 API 成本几乎可以忽略。

#### 8.3.3 阶段2核心 5 条件

核心条件：

- `C1`
- `C2`
- `C6m`
- `C6f`
- `C4`

规模：

- `30 MIC seeds`
- `5 conditions`
- `10 agents`
- `250 rounds`

等价回合数：

- 非 Sampling 条件：`4 × 30 × 10 × 250 = 300,000` Actor turns
- Sampling 条件：`1 × 30 × 10 × 250 = 75,000` Actor turns
- Judge 调用：`75,000`

估算成本：

| 组成 | 调用量 | 估算成本 |
|------|-------:|---------:|
| 非 Sampling Actor（Qwen3.5-Plus） | 300,000 turns | `~¥435` |
| Sampling Actor（Qwen3.5-Plus） | 75,000 turns | `~¥139` |
| Judge（Qwen3.5-Plus） | 75,000 calls | `~¥89` |
| 小计 | | **`~¥663`** |

#### 8.3.4 阶段2机制条件

机制条件：

- `C3 Shuffled`
- `C5 Judge-Only`
- `C7 Fixed-Path`
- `Full-RuleScorer`

按中位规模估算：

- `16 MIC seeds` 平均
- `250 rounds`

等价回合数：

- Actor turns：约 `160,000`（多为 Sampling 类型）
- Judge 调用：约 `120,000`
- Rule-Based 条件不消耗 Judge API

估算成本：

| 组成 | 估算成本 |
|------|---------:|
| Actor（Qwen3.5-Plus） | `~¥296` |
| Judge（Qwen3.5-Plus） | `~¥143` |
| 小计 | **`~¥439`** |

#### 8.3.5 模型鲁棒性子集

使用 DeepSeek-V3.2-exp 作为鲁棒性 Actor + Judge：

- `10 seeds`
- `3` 个关键条件（`C1/C6m/C4`）
- `250 rounds`

等价回合数：

- Actor turns：约 `75,000`
- Judge 调用：约 `25,000`

估算成本：

| 组成 | 估算成本 |
|------|---------:|
| Actor + Judge（DeepSeek-V3.2-exp） | `~¥250` |
| 小计 | **`~¥250`** |

#### 8.3.6 阶段3：多地图探索

若只做基础版阶段3（不含 Exp3-Minimal）：

- `3 maps`
- `2 conditions`（`C1` 与 `C4`）
- `15 MIC seeds`
- `250 rounds`

估算成本：

| 组成 | 估算成本 |
|------|---------:|
| Actor（Qwen3.5-Plus） | `~¥300` |
| Judge（Qwen3.5-Plus） | `~¥170` |
| 小计 | **`~¥470`** |

#### 8.3.7 阶段3：Exp3-Minimal

按一个”真的把它做完”的估算：

- `15` 个地图变体
- `2` 个条件（`C1` vs `C4`）
- `10 MIC seeds`
- `200 rounds`

等价规模大约为：

- `600,000` Actor turns
- `300,000` Judge 调用

估算成本：

| 组成 | 估算成本 |
|------|---------:|
| Actor（Qwen3.5-Plus） | `~¥870` |
| Judge（Qwen3.5-Plus） | `~¥357` |
| 小计 | **`~¥1,227`** |

> 由于采用开源模型，Exp3-Minimal 的成本从 v7 原估算的 ¥12,500 降至 ~¥1,200，不再是预算瓶颈。

### 8.4 人工成本估算

#### 8.4.1 编码 pilot

按：

- `200-300` 条样本
- `2` 名编码者
- 每名编码者 `3-4` 小时
- `¥80-100 / 小时`

估算：

| 项目 | 估算成本 |
|------|---------:|
| Human pilot coding | `~¥480-800` |

#### 8.4.2 人类评估

按：

- `50` 名参与者
- `¥30 / 人`

估算：

| 项目 | 估算成本 |
|------|---------:|
| Human evaluation | `~¥1,500` |

### 8.5 成本汇总一览

| 模块 | API 成本 | 人工成本 | 合计 |
|------|--------:|--------:|-----:|
| 预实验 | `~¥170` | — | `~¥170` |
| 阶段1 | `~¥3` | — | `~¥3` |
| 阶段2核心 (30 seeds × 5 条件) | `~¥663` | — | `~¥663` |
| 阶段2机制 (16 seeds × 4 条件) | `~¥439` | — | `~¥439` |
| 鲁棒性子集 (DeepSeek, 10 seeds × 3 条件) | `~¥250` | — | `~¥250` |
| 阶段3多地图 (15 seeds × 2 条件 × 3 图) | `~¥470` | — | `~¥470` |
| Exp3-Minimal (15 变体 × 2 条件 × 10 seeds) | `~¥1,227` | — | `~¥1,227` |
| 编码 pilot | — | `~¥480-800` | `~¥480-800` |
| 人类评估 | — | `~¥1,500` | `~¥1,500` |

### 8.6 三档总预算

#### 方案 A：MVP / 最小可投稿版

包含：

- 预实验全套
- 阶段1
- 阶段2核心 5 条件
- human coding pilot

不包含：

- 阶段2机制条件
- 鲁棒性子集
- 阶段3
- 人类评估

估算总成本：

| 类目 | 费用 |
|------|----:|
| 预实验 | `~¥170` |
| 阶段1 | `~¥3` |
| 阶段2核心 | `~¥663` |
| coding pilot | `~¥480-800` |
| 小计 | `~¥1,316-1,636` |
| 15% 机动缓冲 | `~¥200-250` |
| **合计** | **~¥1,500-1,900** |

#### 方案 B：推荐版 / 适合真正投稿

包含：

- 方案 A 全部
- 阶段2机制条件
- DeepSeek 鲁棒性子集
- 人类评估

不包含：

- 阶段3多地图
- Exp3-Minimal

估算总成本：

| 类目 | 费用 |
|------|----:|
| MVP 基础 | `~¥1,500-1,900` |
| 阶段2机制条件 | `~¥439` |
| DeepSeek 鲁棒性子集 | `~¥250` |
| 人类评估 | `~¥1,500` |
| 小计 | `~¥3,689-4,089` |
| 15% 机动缓冲 | `~¥550-610` |
| **合计** | **~¥4,200-4,700** |

#### 方案 C：全量版 / 含阶段3探索

包含：

- 推荐版全部
- 阶段3多地图
- Exp3-Minimal

估算总成本：

| 类目 | 费用 |
|------|----:|
| 推荐版基础 | `~¥4,200-4,700` |
| 阶段3多地图 | `~¥470` |
| Exp3-Minimal | `~¥1,227` |
| 小计 | `~¥5,897-6,397` |
| 15% 机动缓冲 | `~¥885-960` |
| **合计** | **~¥6,800-7,400** |

> **与此前版本的预算对比**：
>
> | 方案 | v7 原估算（闭源 Judge） | **v7 修订（开源优先）** | 降幅 |
> |------|------------------------:|-----------------------:|:----:|
> | MVP | ¥6,300-6,800 | **¥1,500-1,900** | **72-76%↓** |
> | 推荐版 | ¥16,300-17,000 | **¥4,200-4,700** | **72-74%↓** |
> | 全量版 | ¥38,000-39,500 | **¥6,800-7,400** | **81-82%↓** |
>
> 开源优先策略使全量版预算低于原 MVP 预算。**API 成本不再是实验规模的制约因素，人工标注费成为最大单项开支。**

### 8.7 预算策略建议

由于 API 成本已极低，`v7` 的预算策略从”削减实验规模控制成本”转变为：

#### 策略 1：直接按方案 B 执行，不压缩任何实验规模

推荐版全部费用 ~¥4,200-4,700，其中 API 成本仅 ~¥1,500，人工费 ~¥2,000。
30 个 MIC seeds 完整保留，不需要为省钱而降低统计功效。

#### 策略 2：根据阶段2结果决定是否补上方案 C

阶段3的 API 成本仅 ~¥1,700（多地图 + Exp3-Minimal），在方案 B 完成后随时可追加。

#### 策略 3：如需进一步降本，压缩人工费而非 API 费

- 编码 pilot 可先从 200 条样本开始（而非 300 条）
- 人类评估可从 30 人开始（而非 50 人），视需要追加

> **结论**：按方案 B 执行。全部 30 个 MIC seeds、5 个核心条件、4 个机制条件、鲁棒性子集和人类评估，总预算 ~¥4,500。

### 8.7 时间线

```text
W1-W2:
  指标实现、地图预检、NPC设计、lexical norming、C2 reverse-inference audit

W3:
  预实验：理解门控、prompt位置、MIC有效窗口、收敛 pilot、coding manual pilot

W4-W5:
  阶段1：Exp1A + Exp1C

W6-W8:
  阶段2：5 个核心条件的 MIC 验证性实验

W9:
  阶段2：机制条件补充 + human coding subset

W10-W12:
  仅在阶段2支持时进入阶段3；否则直接整理论文主结果

W13-W15:
  人类评估（若做）+ 论文写作

W16-W18:
  修改、内部 review、投稿
```

### 8.8 Minimum Viable Paper

保底论文只依赖：

1. 阶段1：表征有效性
2. 阶段2：核心 5 条件比较
3. `Exp1C`：探索性结构 profile vs 语义标签证据

保底题目可为：

**Does Space Syntax Help LLM Agents Behave Spatially? A Controlled Study of Structured Spatial Representations**

保底贡献：

1. 一套结构化空间表征协议
2. 一套区分到位后 Perception、Movement 贡献与 Sampling 贡献的实验框架
3. 一套区分“响应存在”和“方向对齐”的双主因变量设计
4. 一套用于长时程 LLM Agent 实验的 matched initial conditions 对照协议

> 不再将 matched design 单独包装成主要创新，而是作为实验框架的一部分。

---

## 第九部分：风险与应对

| 风险 | 可能性 | 应对 |
|------|--------|------|
| `Openness` 共线，H2 不可分离 | 高 | 改用 `Mean Depth` |
| `TAR_run` 在小图上过噪 | 中 | location-level Spearman + Fisher z；图示分位差值只作辅助 |
| MIC 方差缩减窗口很短 | 中-高 | 报告 `ICC(seed)`；不依赖 MIC 作为最低功效前提 |
| `C2` 描述泄露空间语义 | 中 | reverse-inference audit 过滤描述 |
| `Judge-Only` 接近 `Full` | 中 | 将主要解释转向 Judge 先验与空间常识效应 |
| `H3` 节点太少 | 高 | 降级为描述性观察 |
| 记忆吸收空间效应 | 中 | 通过前 50 轮 priming 分析与全程分析区分 |
| 编码信度不足 | 中 | 缩减标签粒度、修 coding manual、扩大 human subset |
| Actor-Judge 同源偏见 | 中 | Rule-Based Scorer 对照 + DeepSeek 鲁棒性 Judge 交叉验证 |
| Qwen3.5-Plus 空间理解不足 | 低-中 | 预实验门控（理解 ≥85%）；DeepSeek 鲁棒性子集交叉检验 |
| 阶段3无稳定结果 | 中 | 不影响主论文成立 |

---

## 第十部分：投稿前自检清单

### 理论

- [ ] H1-H3 推导链完整
- [ ] `TAR_run` 的 protocol 已明确写成步骤
- [ ] 主张没有强于设计能支撑的内容

### 预实验

- [ ] `Openness vs Mean Depth` 决策完成
- [ ] lexical norming 完成
- [ ] `C2` reverse-inference audit 完成
- [ ] MIC 有效窗口分析完成
- [ ] prompt 位置固定
- [ ] 收敛性 pilot 完成

### 阶段1

- [ ] `C4 > C0/C1/C2/C3/C5` 报告完整
- [ ] 同时报告 `BSR` 与 `TAR`
- [ ] `Exp1C` 使用 composite structural profile 解释，不误称为单一 topology 因子
- [ ] 每 cell 至少 10 个场景

### 阶段2

- [ ] `30 MIC seeds × 5 核心条件` 完成
- [ ] `C6m-C1`、`C6m-C2`、`C6f-C6m`、`C4-C6f`、`C4-C1` 全部报告
- [ ] `TAR_run` 按 location-level Spearman + Fisher z 生成
- [ ] 早期 50 轮 priming 分析完成
- [ ] `C7` 至少 20 seeds（若用于认知 vs movement 解释）

### 模型与评估

- [ ] Qwen3.5-Plus 空间理解门控通过（Comprehension ≥85%, Behavioral Inference ≥70%）
- [ ] DeepSeek-V3.2 鲁棒性子集方向一致性检查完成
- [ ] Actor-Judge 同源偏见检测完成（Rule-Based Scorer 对照 + DeepSeek Judge 交叉验证）
- [ ] coding manual 完成
- [ ] human pilot coding 达到预设 κ 阈值
- [ ] LLM-human calibration 完成
- [ ] 两阶段分离评估未泄露空间信息
- [ ] LLM Judge 偏见检测完成

### 写作

- [ ] 摘要主结论只依赖 MIC run-level 验证性分析
- [ ] 明确写出“主验证分析主要检测中到大效应”
- [ ] `RQ4` 明确写为探索性
- [ ] 阶段3明确写为可选扩展

---

## 一句话版 v7 核心策略

**用开源模型（Qwen3.5-Plus）保证可复现性，用 matched initial conditions 控制初始世界差异，用 `C6m / C6f / C4` 拆开到位后 Perception、Movement 与 Sampling 的贡献，并用显式 `TAR_run` protocol 同时回答”有没有响应”与”是否按理论方向响应”。**
