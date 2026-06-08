# SpatialAgent 研究计划 v6

## Where You Are Shapes Who You Become: Space Syntax-Informed LLM Agents for Spatially Believable Game Worlds

> 版本: 6.0  
> 日期: 2026-03-16  
> 作者: Li  
> 目标会议: AAMAS-27 (首选) / AAAI-27 (备选)  
> 本版本目标: 基于 `v5 review` 做最后一轮方法学收口，修正阶段2主比较、run-level统计模型与 matched-seed 设计

---

## 修订说明：v5 → v6 核心变化

| 维度 | v5 | v6 | 修改理由 |
|------|----|----|---------|
| 阶段2主比较链 | `C4-C2` 被写作“空间结构信息 vs 一般上下文增强” | **`C6-C2` 升格为主比较**；`C4-C2` 降为系统总增益比较 | `C4` 含 `Action Sampling`，`C2` 不含，原比较不干净 |
| run-level 模型 | 每个 run 一个数据点，但仍写 `(1|run_id)` | **主分析改为 matched-seed run-level 模型：`DV ~ condition + (1|seed)`** | 修复样本层级与随机效应不自洽问题 |
| 角色协变量 | 试图在 run-level 中纳入 `social_tendency` | **角色异质性改到 agent×seed 聚合模型中处理** | 避免协变量层级与 DV 层级冲突 |
| 随机重复设计 | 多 runs 重复，但未说明跨条件是否配对 | **阶段2显式采用 matched-seed / blocked design** | 在相同资源下显著降低条件间方差 |
| TAR 实现 | 主要依赖高/低节点分组差值 | **双轨实现**：连续型主实现 + 高/低分组可视化 | 降低 20 节点小图上阈值分组带来的脆弱性 |
| C2 定义 | “稳定非空间上下文基线” | **更精确改写为 stable non-spatial affordance baseline** | 反映其本质是稳定的非空间地点 affordance，而非纯信息量控制 |
| 阶段2结论语气 | 架构增量 + 一般上下文比较 | **分层主张**：表征效应、采样效应、总系统效应分别报告 | 保证结论不强于设计可支撑范围 |

---

## 第一部分：研究背景

### 1.1 问题的起源

现有 LLM Agent 系统通常较好建模了两类变量：

- **WHO**：身份、人格、目标、背景
- **WHAT**：事件、记忆、任务、互动历史

但对第三类变量的建模仍然薄弱：

- **WHERE**：空间构型、深度、可达性、瓶颈性、可视性

这里的问题并不是“完全没有空间信息”，而是**缺乏构型级空间表征**。多数现有系统使用地点名称、功能标签或简单邻接关系，却没有系统引入 Space Syntax 这类成熟的空间结构分析框架。

### 1.2 研究空白

本研究聚焦三个明确空白：

1. **表征空白**：LLM Agent 缺乏 Space Syntax 风格的结构化空间表征。
2. **识别空白**：缺乏把“拓扑必然效应”与“空间化架构增量效应”分离的实验协议。
3. **理论空白**：缺乏建筑学 Space Syntax 与 LLM 多 Agent 社会模拟之间的系统对话。

### 1.3 三个理论跳跃

| 跳跃 | 从 → 到 | 合理性论证 | 风险 |
|------|---------|-----------|------|
| 跳跃1 | 真实人类 → LLM Agent | LLM 训练语料可能编码了人类空间-社会常识 | 模型可能只是语言模式复现，而非真正空间推理 |
| 跳跃2 | 物理空间 → 文本化空间 | 拓扑指标可抽象为结构性文本描述 | 物理 affordance 可能在文本中被削弱 |
| 跳跃3 | 个体空间行为 → 群体社会涌现 | 微观空间偏移可能累积成宏观网络结构 | 个体效应可能被时间动态与交互历史稀释 |

> `v6` 的策略仍然是：先把跳跃1和跳跃2验证清楚，再把跳跃3作为可选扩展。

---

## 第二部分：研究目标、问题与主张边界

### 2.1 总体目标

本研究不试图“证明 Space Syntax 在文本 Agent 世界被完整验证”，而是尝试回答三个更可 defend 的问题：

1. 结构化空间表征能否稳定改变 LLM Agent 行为？
2. 这种改变能否超出一般上下文增强？
3. 其中有多少变化沿着 Space Syntax 的理论方向发生？

### 2.2 研究问题

**RQ1（验证性）**：结构化空间表征是否比无空间、地点名、原始数值和稳定非空间 affordance 基线更能诱发 Agent 的空间响应？

**RQ2（验证性）**：在控制拓扑必然效应的前提下，完整空间化架构相对 `Topology-Only` 是否带来显著增量？

**RQ3（验证性）**：在空间化架构中，`Perception` 与 `Action Sampling` 的独立贡献分别是多少？

**RQ4（探索性）**：空间行为响应更接近结构性 Space Syntax 效应，还是更接近 LLM 已有语义常识的激活？

### 2.3 验证性 / 探索性分层

| 内容 | 性质 | 是否主论文核心 |
|------|------|:--------------:|
| 阶段1：表征有效性（Exp1A） | 验证性 | 是 |
| 阶段2：核心 4 条件架构比较 | 验证性 | 是 |
| 阶段2：模块分解（`C4/C6/C1`） | 验证性 | 是 |
| 阶段1：反直觉 2×2 设计（Exp1C） | 探索性高价值 | 是 |
| 阶段2：`Shuffled/Judge-Only/Fixed-Path/Rule-Based` | 机制探测 | 否，附录主报 |
| 阶段3：多地图涌现 | 探索性扩展 | 否 |
| 人类评估 | 外部有效性增强 | 否，时间允许时做 |

### 2.4 主张边界

`v6` 只尝试支撑以下级别的结论：

- 结构化空间表征可以系统性影响 LLM Agent 行为
- 这种影响在若干关键比较中超出稳定的非空间 affordance 基线
- 这些影响中有一部分沿着 Space Syntax 理论方向发生

`v6` 不预先声称：

- 完整验证 Space Syntax
- 证明所有社会涌现现象都由空间构型因果决定
- 证明任何单一指标具有跨环境普适性

---

## 第三部分：理论框架与主因变量

### 3.1 H1-H3 的推导链

#### H1：Integration 与社交频率

| 层级 | 内容 |
|------|------|
| Hillier 原始理论 | 高 Integration 空间汇聚自然流动，形成公共活动中心 |
| 物理空间实证 | 高 Integration 节点通常承载更高人流与更多面对面互动 |
| 文本 Agent 推导 | 若 Agent 知道某位置全局可达性更高、像结构枢纽，则更可能主动接触、停留或公开互动 |
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

核心指标仍为：

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

> `v6` 默认主文使用 `Mean Depth` 作为 H2 的稳健候选；`Openness` 若保留，仅作为附加分析。

### 3.3 双主因变量：BSR 与 TAR

#### 3.3.1 Unsigned BSR

`BSR`（Behavioral Spatial Responsiveness）回答：

> 行为是否随着空间特征发生系统性变化？

它衡量的是**响应存在性**，不区分方向。

常见实现：

- 行为分布差异的 `chi-square`
- `Cramer's V`
- 强度、敏感度等分布差异

#### 3.3.2 Signed TAR

`TAR`（Theory-Aligned Responsiveness）回答：

> 这种响应是否沿着理论预测方向发生？

它衡量的是**方向对齐性**。

### 3.4 TAR 的双轨实现（v6新增强化）

`v5` 的 TAR 主要依赖高 / 低节点分组，容易受 20 节点小图上的阈值选择影响。`v6` 改为双轨实现：

#### 主实现：连续型 TAR

对于每个假设，主验证性分析以连续空间特征为基础：

```text
H1: sociality ~ standardized Integration
H2: privacy_behavior ~ standardized MeanDepth
H3: gatekeeping ~ standardized Control
```

连续型回归系数的符号与大小即为主 TAR 指标：

- 正系数且方向符合假设：理论方向支持
- 近零：无明显方向性支持
- 反向系数：方向与理论相反

#### 辅助实现：高 / 低分组 TAR

仅用于：

- 可视化
- 直观解释
- 读者易于理解的图表展示

例如：

```text
TAR_H1_group = sociality(top 25% Integration) - sociality(bottom 25% Integration)
```

> 这样 `v6` 避免把主验证性分析建立在脆弱的二分阈值上，同时保留可解释的图示。

### 3.5 辅助因变量

- `Behavioral Entropy`
- 平均交互强度
- 信息敏感度比例
- 守门行为比例

行为熵仍为辅助指标，不承担主理论验证功能。

---

## 第四部分：环境、NPC 与控制变量

### 4.1 环境设置

验证性阶段只使用一张主地图：

- `Plaza`

探索性扩展使用：

- `Labyrinth`
- `Bridge`

三图的区分依据是指标分布，而不是叙事名称：

- `Plaza`：Integration 高峰集中
- `Labyrinth`：Depth 高、Connectivity 低
- `Bridge`：瓶颈和多中心更明显

### 4.2 NPC 角色设计标准化

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

### 4.3 初始位置随机化

- 每个 seed 下，NPC 初始位置随机分配
- 该分配在不同条件之间保持一致（见 matched-seed 设计）
- 主分析默认排除前 `5` 轮 warm-up
- 附录报告包含 / 排除前 `5` 轮的敏感性分析

### 4.4 Prompt 位置控制

预实验比较三种插入位置：

- 系统 prompt 末尾
- 当前情境中部
- 用户指令前

选取最稳定的位置，并在所有实验中固定。

---

## 第五部分：SpatialAgent-Lite 架构与条件矩阵

### 5.1 核心架构

主架构只保留两个模块：

1. `Spatial Perception`
2. `Spatial Action Sampling`

不把 `Memory` 和 `Planning` 作为主贡献，以避免归因污染。

### 5.2 Spatial Perception

主表征为 `Absolute Structural`：

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
- `Rule-Based Scorer` 只作为鲁棒性对照

### 5.4 条件矩阵

#### 5.4.1 验证性核心条件

| 条件 | Movement | 对话空间描述 | Sampling | 用途 |
|------|----------|--------------|----------|------|
| `C1 Topology-Only` | 邻接 + 地名 + 在场数 | 无 | 无 | 主基线 |
| `C2 Stable Non-Spatial Affordance` | 同 `C1` | 稳定的非空间地点 affordance 描述 | 无 | **主非空间对照** |
| `C4 Full SpatialAgent` | 空间指标 + 邻接 + 地名 + 在场数 | Absolute Structural | 有 | 完整系统 |
| `C6 Perception-Only` | 空间指标 + 邻接 + 地名 + 在场数 | Absolute Structural | 无 | **空间表征本身** |

#### 5.4.2 探索性机制条件

| 条件 | 作用 |
|------|------|
| `C3 Shuffled Signal` | 检验正确空间信息是否必要 |
| `C5 Judge-Only` | 检验 Judge 先验知识是否足以制造大部分效应 |
| `C7 Fixed-Path` | 分离 Movement 效应与到位后认知效应 |
| `Full-RuleScorer` | 检查 LLM Judge 是否放大效应 |

### 5.5 `C2` 的精确定义（v6改写）

`C2` 在 `v6` 中不再被宽泛称为 “rich non-spatial context”，而更精确地定义为：

> **stable non-spatial affordance baseline**

实现方式：

- 每个 seed 开始时，为每个位置从非空间描述池中抽取一条描述
- 该映射在整个 run 内保持固定
- 不同 seed 之间重新随机
- 描述与空间结构特征无系统关联

这意味着 `C2` 不是简单的“多给一点文字”，而是：

- 为每个位置提供稳定但非空间的地点语义 / 氛围 affordance

> 这样定义更准确，也更利于在论文中诚实说明：`C2` 是一个强基线，而不是纯 token 长度控制。

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

- 若某指标 `CV < 0.2`，则在该图中标记为低区分力
- 若高 `Control` 节点少于 3 个，则 `H3` 降级为描述性观察

### 6.0.2 LLM 空间理解门控

两层：

1. `Comprehension`
2. `Behavioral Inference`

通过标准：

- `Comprehension >= 85%`
- `Behavioral Inference >= 70%`

### 6.0.3 Prompt 位置测试

在微任务上测试三种插入位置，固定最稳定方案。

### 6.0.4 Lexical Norming（Exp1C 必做）

对候选语义标签收集五维评分：

- `publicness`
- `privacy`
- `danger`
- `valence`
- `brightness`

保留那些：

- 在 “public / private” 维度上差异大
- 在其他维度上差异尽量小

### 6.0.5 收敛性 pilot

在 `Plaza` 上先跑小规模模拟，观察：

- 网络密度
- 聚类系数
- degree Gini
- 平均交互强度

稳态判据：

> 连续 3 个窗口（每窗口 20 轮）内，关键指标变化幅度均 < `5%`

若 `200` 轮不足，阶段2 / 3 提升到 `300` 轮。

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

- `BSR`
- 连续型 `TAR_H1`
- 连续型 `TAR_H2`

### Exp1C：理论归因 2×2 因子设计

因子：

- `Topology`: 高 / 低
- `Semantic Label`: 公共 / 私密

形成四个 cell：

| | 公共标签 | 私密标签 |
|---|:---:|:---:|
| 高拓扑中心性 | 一致 | 冲突 |
| 低拓扑中心性 / 高深度 | 冲突 | 一致 |

每个 cell：

- 5 个独立场景
- 每场景 20 个微任务

模型：

```text
DV ~ topology_level * semantic_label + (1|scenario)
```

解释：

- `topology` 主效应：结构信号
- `semantic_label` 主效应：语义常识
- 交互项：冲突条件下的主导关系

> `Exp1C` 仍为探索性高价值证据，不承担确认性主结论。

---

## 6.2 阶段2：架构增量效应与模块分解

### 6.2.1 范围收缩

阶段2只在 `Plaza` 上做验证性主分析，目的是：

- 不把跨地图泛化问题混入确认性阶段
- 把资源集中到最重要的架构比较

### 6.2.2 Matched-Seed 设计（v6关键新增）

阶段2所有验证性核心条件采用 **matched-seed / blocked design**：

```text
for seed in 1..30:
  固定 NPC 初始位置分配
  固定环境随机事件序列
  固定 C2 描述池映射
  固定所有外部随机参数

  在 C1 / C2 / C4 / C6 下分别运行
```

这意味着：

- 同一个 `seed` 代表同一个初始世界实例
- 条件差异尽量只来自架构本身

好处：

1. 降低 run-level 方差
2. 提升条件比较精度
3. 允许在主分析中把 `seed` 作为随机截距

### 6.2.3 核心验证性条件与样本量

核心条件：

- `C1 Topology-Only`
- `C2 Stable Non-Spatial Affordance`
- `C4 Full SpatialAgent`
- `C6 Perception-Only`

运行参数：

- `30 matched seeds`
- 每个 seed 在 4 个条件下各运行一次
- 每 run `200-300` 轮（由收敛 pilot 决定）
- 10 个 NPC

### 6.2.4 阶段2主比较链（v6修正）

`v5` 的一个核心问题是让 `C4-C2` 承担了“空间结构信息 vs 一般上下文增强”的解释，但该对比混入了 `Action Sampling`。`v6` 改为：

```text
主比较 A: C4 - C1
  = 完整空间化架构相对 topology-only 的总增益

主比较 B: C6 - C1
  = 空间表征本身的增量效应

主比较 C: C4 - C6
  = Action Sampling 的独立增量

主比较 D: C6 - C2
  = 空间结构信息 vs 稳定非空间 affordance 基线
```

其中：

- **主比较 D** 是 `v6` 新升格的关键比较
- `C4 - C2` 仍可报告，但只解释为：

```text
完整空间化系统相对稳定非空间 affordance 条件的总系统增益
```

而不再被解释成“空间结构信息本身更优”

### 6.2.5 阶段2主分析模型（v6修正）

#### 一级：matched-seed run-level 主验证模型

每个 `seed × condition` 汇总成一个数据点。

主模型：

```text
DV_run ~ condition + (1|seed)
```

适用于：

- `BSR_run`
- `TAR_H1_run`
- `TAR_H2_run`
- `entropy_run`

这是 `v6` 的**主验证性模型**。

> 关键修正：如果每个 run 只有一个聚合数据点，就不再写 `(1|run_id)`，而是利用 matched-seed 结构写 `(1|seed)`。

#### 二级：agent×seed 聚合异质性模型

为了分析角色异质性，每个 `agent × seed × condition` 聚合成一个数据点：

```text
DV_agent_seed ~ condition + social_tendency + condition:social_tendency
                + (1|seed) + (1|agent_id)
```

这个模型用于：

- 检查空间效应是否被社交倾向调节
- 回答“外向 vs 内向 NPC 是否对空间结构有不同响应”

> 关键修正：角色相关协变量不再被错误地塞进 run-level 模型，而是在更合适的 `agent × seed` 聚合层级分析。

### 6.2.6 探索性机制条件

以下条件只做机制探测：

- `C3 Shuffled Signal`
- `C5 Judge-Only`
- `C7 Fixed-Path`
- `Full-RuleScorer`

运行规模：

- `10-12 matched seeds`

用途：

- 检测错误空间信号是否仍可造假效应
- 检测 Judge 先验知识的贡献
- 分离 Movement vs 到位后认知效应
- 检查 LLM Judge 是否系统性放大效应

### 6.2.7 控制位置后的条件效应

为分离“去哪里”和“到了后怎么做”，增加探索性模型：

```text
DV_event ~ condition + spatial_features + (1|seed) + (1|agent_id) + (1|location)
```

这里 `location` 随机效应的含义是：

> 在相同位置上比较不同条件的行为差异。

### 6.2.8 时间动态分析

阶段2必须报告：

1. 收敛曲线
2. 前半程 vs 后半程比较

模型：

```text
DV_event ~ condition * time_half + (1|seed) + (1|agent_id)
```

若交互显著，说明空间效应具有时间依赖性。

---

## 6.3 阶段3：探索性扩展

### 6.3.1 启动条件

只有在阶段2至少满足以下之一时，才进入阶段3：

1. `C4 > C1` 在至少一个主 `TAR` 指标上达到显著或稳定中等效应
2. `C6 > C1` 与 `C4 > C6` 方向稳定，模块分解有解释价值

### 6.3.2 多地图分析

使用：

- `Plaza`
- `Labyrinth`
- `Bridge`

目的仅为：

- 观察方向是否稳定
- 观察架构增量是否受构型调节

规模：

- `15 matched seeds / cell`

### 6.3.3 Exp3-Minimal

仅在可生成性 pilot 成功时执行。

若失败：

- 降级为描述性案例
- 不进入统计推断

---

## 第七部分：评估与统计分析

### 7.1 两阶段分离评估

#### 阶段A：盲行为编码

标注者只看行为文本，不看空间信息。

标注维度：

- 行为类型
- 交互强度
- 信息敏感度
- 守门 / 监视 / 拦截行为

#### 阶段B：空间关联分析

研究者将盲编码结果与空间特征进行事后关联。

这样可以避免把理论假设直接写回评分标准。

### 7.2 主验证分析

主结论仅基于：

- matched-seed run-level 分析

可报告的主结果包括：

- `BSR_run`
- 连续型 `TAR_H1_run`
- 连续型 `TAR_H2_run`
- `entropy_run`

### 7.3 异质性与事件级分析

下列分析不进入摘要主 claim：

- `agent × seed` 聚合模型
- event-level 模型
- `Fixed-Path`
- `Judge-Only`
- `Rule-Based`

它们只用于：

- 模式解释
- 效应量估计
- 机制探测

### 7.4 功效分析

#### 主验证分析

在 `30 matched seeds / cell` 下，两组 run-level 比较的可检测效应约为：

- `d >= 0.74`

这仍偏向中到大效应，但已经优于 `v5`。

#### 事件级补充

在考虑依赖结构后，事件级分析可帮助估计：

- `d ≈ 0.5` 的中等效应

### 7.5 统计规则

- `Benjamini-Hochberg FDR`
- 报告 `p 值 + 效应量 + 95% CI`
- 若 run-level 不显著而 event-level 显著：
  - 只能报告为“存在中小效应迹象”
  - 不得上升为主结论

### 7.6 LLM Judge 偏见检测

通过三种方式：

1. `Shuffled` 条件作为偏见探针
2. 人类-LLM 标注一致性分析
3. `Rule-Based` 与 `LLM Judge` 结果对照

---

## 第八部分：预算、时间线与保底论文

### 8.1 预算策略

资源继续集中在阶段2核心 4 条件：

| 实验 | 规模 | 备注 |
|------|------|------|
| 预实验 | 中等 | 含 lexical norming、prompt位置、收敛 pilot |
| 阶段1 | 中等 | Exp1A + Exp1C |
| 阶段2核心条件 | **最大头** | `30 matched seeds × 4 条件` |
| 阶段2机制条件 | 中等偏小 | `10-12 matched seeds` |
| 阶段3 | 可选 | 仅在前两阶段支持时启动 |

### 8.2 时间线

```text
W1-W2:
  指标实现、地图预检、NPC设计、lexical norming

W3:
  预实验：理解门控、prompt位置、收敛 pilot、C2 映射稳定性测试

W4-W5:
  阶段1：Exp1A + Exp1C

W6-W8:
  阶段2：4 个核心条件的 matched-seed 验证性实验

W9:
  阶段2：机制条件补充

W10-W12:
  仅在阶段2支持时进入阶段3；否则直接整理主论文结果

W13-W15:
  人类评估（若做）+ 论文写作

W16-W18:
  修改、内部 review、投稿
```

### 8.3 Minimum Viable Paper

保底论文只依赖：

1. 阶段1：表征有效性
2. 阶段2：核心 4 条件比较
3. `Exp1C`：探索性理论归因证据

保底题目可为：

**Does Space Syntax Help LLM Agents Behave Spatially? A Controlled Study of Structured Spatial Representations**

保底贡献：

1. 一套结构化空间表征协议
2. 一套区分空间表征效应、采样效应与总系统效应的实验框架
3. 一套区分“响应存在”和“方向对齐”的双主因变量设计
4. 一套 matched-seed 的 LLM Agent 对照实验协议

---

## 第九部分：风险与应对

| 风险 | 可能性 | 应对 |
|------|--------|------|
| `Openness` 共线，H2 不可分离 | 高 | 改用 `Mean Depth` |
| run-level 主效应不显著 | 中-高 | 作为 pilot 报告，并用 event-level 给出效应量估计 |
| `C2` 仍形成过强替代地点语义 | 中 | 在 Discussion 中明确其是 stable non-spatial affordance baseline，而非纯 token 基线 |
| `Exp1C` 语义标签混入额外维度 | 中-高 | lexical norming 严格筛选 |
| `Judge-Only` 接近 `Full` | 中 | 将主要解释转向 Judge 先验与空间常识效应 |
| `H3` 节点太少 | 高 | 降级为描述性观察 |
| 阶段3无稳定结果 | 中 | 不影响主论文成立 |

---

## 第十部分：投稿前自检清单

### 理论

- [ ] H1-H3 推导链完整
- [ ] `TAR` 的连续型定义清晰
- [ ] 主张没有强于设计能支撑的内容

### 预实验

- [ ] `Openness vs Mean Depth` 决策完成
- [ ] lexical norming 完成
- [ ] prompt 位置固定
- [ ] 收敛性 pilot 完成

### 阶段1

- [ ] `C4 > C0/C1/C2/C3/C5` 报告完整
- [ ] 同时报告 `BSR` 和连续型 `TAR`
- [ ] `Exp1C` 报告主效应与交互项

### 阶段2

- [ ] `30 matched seeds × 4 核心条件` 完成
- [ ] `C4-C1`、`C6-C1`、`C4-C6`、`C6-C2` 全部报告
- [ ] `C4-C2` 若报告，仅解释为总系统增益
- [ ] run-level 主模型写为 `DV ~ condition + (1|seed)`
- [ ] 角色异质性模型单独在 `agent × seed` 层级分析
- [ ] 收敛曲线与时间分段分析完成

### 评估

- [ ] 两阶段分离评估未泄露空间信息
- [ ] LLM Judge 偏见检测完成
- [ ] 人类评估若实施，则与主结论关系说明清楚

### 写作

- [ ] 摘要主结论只依赖 matched-seed run-level 验证性分析
- [ ] `RQ4` 明确写为探索性
- [ ] 阶段3明确写为可选扩展

---

## 一句话版 v6 核心策略

**用最少但最硬的 matched-seed 核心比较，区分空间表征效应、采样效应与总系统效应，并用 `BSR + TAR` 同时回答“有没有响应”与“是否按理论方向响应”。**
