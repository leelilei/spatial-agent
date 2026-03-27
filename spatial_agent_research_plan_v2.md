# SpatialAgent 研究计划 v2

## Where You Are Shapes Who You Become: Space Syntax-Informed LLM Agents for Spatially Believable Game Worlds

> 版本: 2.0
> 日期: 2026-03-15
> 作者: Li
> 目标会议: AAMAS-27 (首选) / AAAI-27 (备选) / CHI 2027 (备选)
> 本版本基于 v1 及四份独立评审意见大幅修订

---

## 修订说明：v1 → v2 核心变化

| 维度 | v1 | v2 | 修改理由 |
|------|----|----|---------|
| 主张强度 | "首次证明空间构型因果塑造多Agent社会涌现" | "提供控制性证据表明空间结构化表征系统性地影响Agent交互模式" | 四份评审一致认为v1 claim过大 |
| 核心模块 | 4个（Perception + Memory + Planning + ActionSampling） | 2个（Perception + ActionSampling），其余移至附录 | 降低归因复杂度，让消融更干净 |
| Baseline 设计 | 1个（No Space） | 6个（梯度化对照） | 解决"只是更多上下文"和"只是prompt engineering"的质疑 |
| 实验结构 | 4个平行实验 | 3阶段递进（机制验证→行为效应→社会涌现） | 建立因果链，前一阶段不成立则不进入下一阶段 |
| 假设表述 | 强方向性单因子映射 | 保守双向机制假设 | 避免被简单反例击溃 |
| 空间描述风格 | 解释性/暗示性 | 客观结构性 + 表征消融对比 | 堵住"循环论证/prompt泄漏"漏洞 |
| 评估体系 | 以LLM-as-Judge为主 | 结构化行为标注 + 交叉模型验证 + 扩大人类评估 | 解决Judge与Actor同偏好问题 |
| 统计方法 | 简单t检验，n=5 runs | Mixed-Effects Model，n≥15 runs，预注册分析计划 | 提高统计功效，避免p-hacking质疑 |
| 理论定位 | "引入Space Syntax理论" | "与Hillier进行真正理论对话，探索空间-社会映射在虚拟Agent中的适用性" | 避免被建筑学审稿人认为只是"借了几个变量名" |
| 投稿策略 | AAAI首选 | AAMAS首选（审稿人更理解多Agent社会模拟） | 减少"这只是prompt engineering"的审稿偏见 |

---

## 第一部分：研究背景

### 1.1 问题的起源

LLM驱动的游戏Agent近年取得了显著进展。Generative Agents（Park et al., UIST 2023）证明25个LLM Agent可在虚拟小镇中自发组织社交活动；Project Sid（Altera, 2024）在Minecraft中实现了30个Agent的社会角色分化；Affordable Generative Agents（2024）探索了成本可控的多Agent模拟方案。

然而，现有LLM Agent架构普遍缺乏对**空间构型（spatial configuration）**的显式建模。当前Agent的行为决策主要依赖两个维度：

- **WHO（身份）**：人设、性格、背景故事、目标
- **WHAT（事件）**：对话历史、事件记忆、当前任务状态

第三个对人类行为至关重要的维度——**WHERE（空间）**——在决策中几乎缺席。需要说明的是，Generative Agents等工作并非完全"空间盲"：它们会根据地点名称和功能标签做出差异化行为（如去咖啡馆聊天、回家睡觉）。但这种空间意识停留在**语义标签层面**，缺乏对空间拓扑结构、可见性、可达性等**构型属性**的显式推理。

建筑学领域的Space Syntax理论（Hillier & Hanson, 1984）在过去40年积累了大量实证，系统性地证明了空间构型对人类社会行为的塑造力量。然而，这一成熟理论从未被系统性地引入LLM Agent研究。

### 1.2 研究空白的精确界定

**空白1**：现有LLM Agent缺乏**构型级**空间认知——不是没有空间信息，而是没有来自建筑学空间分析理论的、可操作的结构化空间表征。

**空白2**：没有研究将空间构型作为**控制变量**，在排除拓扑必然效应（topology-driven encounter probability）的前提下，考察空间认知对Agent行为的额外效应。

**空白3**：建筑学Space Syntax理论和LLM Agent研究之间不存在学术桥梁——两个领域都在研究"Agent在空间中的行为"，但使用的是完全不同的方法论和范式。

### 1.3 两个关键的理论跳跃

将Space Syntax从建筑学迁移到LLM Agent领域，需要论证两个跳跃的合理性：

| 跳跃 | 从 → 到 | 合理性论证 |
|------|---------|-----------|
| 跳跃1 | 真实人类 → LLM Agent | LLM的训练数据包含海量关于人类空间行为的描述（小说、新闻、社科文献），因此可能具有隐含的空间-社会常识。本研究的一个子目标正是测试这种隐含知识能否被显式空间特征激活。 |
| 跳跃2 | 物理空间 → 文字描述的空间 | 在文本世界中，Space Syntax指标不再代表物理视线或身体可达性，而代表**空间开放性、连通性、控制性的语义抽象**。这种抽象化是否保留了足够的行为引导力，正是实验要回答的问题之一。 |

本研究不预设这些跳跃必然成立，而是将其作为**实验性假设**进行系统验证。

---

## 第二部分：研究目标与问题

### 2.1 总体目标

据我们所知，这是最早将建筑学空间构型分析方法系统性地应用于LLM多Agent社会模拟的工作之一。我们的目标是：

1. 提出空间感知Agent架构（SpatialAgent-Lite），将Space Syntax空间特征注入Agent的感知和行为选择循环
2. 通过严格控制的对比实验，检验空间结构化表征对Agent行为的影响是否超出一般性上下文丰富化（context enrichment）的效果
3. 探索Space Syntax的空间-社会映射原理在LLM Agent社会中是否依然成立

### 2.2 研究问题（收缩版）

**RQ1（表征验证）**：Space Syntax衍生的空间结构化表征，是否能提升LLM Agent在不同场景中的行为环境一致性（Behavioral-Spatial Consistency, BSC）？

- 操作化：对比多种空间表征方式（无空间 / 地名标签 / 丰富非空间上下文 / 正确空间特征 / 错配空间特征），在相同场景中的BSC差异
- **关键识别**：效果是否超出"任何额外上下文都能提升"的基准线？

**RQ2（认知效应分离）**：在控制拓扑必然效应（topology-driven encounter opportunity）的前提下，空间化表征是否仍能显著改变Agent的行为策略与交互模式？

- 操作化：在同一张地图上，对比SpatialAgent与Topology-Only Agent（使用相同移动策略，但对话时不注入空间信息）的行为差异
- **关键识别**：排除"地图结构本身导致的相遇概率差异"

**RQ3（指标效应）**：Space Syntax的各空间指标（Integration, Connectivity, Visual Depth, Control Value）中，哪些对Agent行为的影响最稳定？

- 操作化：特征消融实验
- **注意**：不预设方向性结论，以探索性分析为主

### 2.3 空间-行为假设（修订版）

基于Space Syntax理论，我们提出以下**机制性假设**（注意：与v1相比，假设表述更保守、更双向、更机制化）：

| 编号 | 假设 | 理论依据 | 与v1的变化 |
|------|------|---------|-----------|
| H1 | Integration 水平会调节Agent社交互动频率的分布——在控制相遇机会后，高Integration区域的Agent仍表现出更高的社交主动性 | Hillier "natural movement"理论 | 增加了"控制相遇机会后"的限定 |
| H2 | 空间可见性（Visual Depth）和逃脱可供性（Connectivity）共同调节Agent的隐私敏感行为——低可见性+高连通性空间中Agent更倾向分享敏感信息，低可见性+低连通性空间中Agent可能更倾向防御行为 | 隐私不仅取决于不被观察，也取决于不被困住 | 从单因子单方向改为**双因子交互假设** |
| H3 | 高Control Value节点更容易涌现**信息中介/守门角色**（gatekeeper），而非一定是"领导者" | Control Value在建筑学中对应"必经之路"的控制者，不等同于社会领导力 | 从"领导者"修正为"守门人/中介者" |
| H4 | 空间Connectivity分布影响Agent间信息传播速度——但需区分这是图论必然结果还是Agent认知效应的放大 | 图论中高连通性天然加速扩散 | 增加了对混淆因素的显式声明 |

> **注意**：v1中的H5（"不同构型→不同涌现"）过于笼统且不可证伪，本版本将其降级为**探索性分析目标**，不作为主假设。

---

## 第三部分：理论框架

### 3.1 与Hillier的真正理论对话

本研究对Space Syntax理论的使用不仅停留在"借用指标"层面，而是在两个层次上与Hillier进行对话：

**指标层（已有）**：使用Integration、Connectivity、Visual Depth、Control Value作为空间特征输入Agent的认知循环。

**构型层（新增）**：讨论空间拓扑结构如何作为**社会关系的基础设施**——空间构型通过约束"谁能遇见谁"、"谁能看见谁"、"信息沿什么路径流通"，内在地塑造社交网络的形态。

Hillier在《The Social Logic of Space》中的核心论点是：

> 空间不仅是社会活动的容器，空间关系本身就是社会关系的编码。

本研究要探索的是：**这一原理在LLM Agent社会中是否依然成立？** 如果成立，它是因为LLM从训练数据中习得了人类的空间-社会常识，还是因为空间构型的社会效应具有某种超越物理实体的普遍性？这是一个我们在Discussion中需要正面讨论的深层问题。

### 3.2 Space Syntax核心指标定义

所有指标基于空间拓扑图 G = (V, E) 计算，其中V为空间节点集合，E为连接边集合。

**Integration（整合度）**

```
Integration(i) = (n - 1) / Σ_j d(i, j)
```

其中 n 为节点总数，d(i, j) 为节点 i 到节点 j 的最短拓扑距离。

- 本研究使用**全局Integration（Rn）**
- 在20节点图中，全局与局部Integration差异较小，但我们会在论文中明确说明使用的是哪种
- 建筑学含义：高Integration空间是天然的聚集点

**Connectivity（连通性）**

```
Connectivity(i) = degree(i)
```

建筑学含义：高Connectivity空间四通八达，局部交通枢纽。

**Visual Depth（视觉深度）——重新定义**

在物理空间中，Visual Depth基于isovist（视域）分析，度量从一个点能看到的面积。在本研究的**文本化离散图模型**中，我们将其重新定义为**空间开放性指标**：

```
Openness(i) = |{j : visible(i, j) = 1}| / (n - 1)
```

其中 visible(i, j) = 1 当从节点i可以直接观察到节点j（无中间遮挡）。

> **重要说明**：我们坦诚承认，这一简化丧失了物理视域分析的连续性和丰富性。在文本世界中，Openness不代表"能看到多远"，而代表"对空间开放程度的语义抽象"。我们将在论文中明确讨论这一简化的局限。

> **与Connectivity的区分**：Connectivity度量直接相连的邻居数（拓扑可达性），Openness度量可视节点数（视线通达性）。在含有视线遮挡的图中，两者可以显著不同（如通过弯曲走廊连接但互不可见的节点）。我们将报告两者的Pearson相关系数，如r > 0.8则在消融实验中合并讨论。

**Control Value（控制值）**

```
Control(i) = Σ_{j∈neighbors(i)} 1 / Connectivity(j)
```

建筑学含义：如果邻居节点的Connectivity都低，则你是它们的"必经之路"，控制力高。对应**守门人/瓶颈**角色，不等同于社会领导力。

### 3.3 指标相关性与多重共线性

我们将在正式实验前报告四个指标在三种构型中的**相关矩阵**。如果某对指标r > 0.8，将在消融实验中合并分析并在论文中讨论。

---

## 第四部分：技术架构——SpatialAgent-Lite

### 4.1 架构总览（精简版）

SpatialAgent-Lite在标准Generative Agents架构（Perceive-Plan-Retrieve-Reflect-Act）基础上，增加**2个核心模块**：

```
标准 Generative Agents：
  [Perceive] → [Plan] → [Retrieve] → [Reflect] → [Act]

SpatialAgent-Lite：
  [Perceive] → [Spatial Perception] → [Plan] → [Retrieve] → [Reflect] → [Spatial Action Sampling]
                      ↑                                                          ↑
                客观空间特征描述                                             空间适配性评分
```

> **为何精简到2个模块**：v1中的4模块（Perception + Memory + Planning + ActionSampling）导致效果归因不清——审稿人无法判断是哪个模块起作用。精简后，消融分析更干净。Spatial Memory Retrieval和Spatial Planning将在附录中描述并作为扩展实验。

### 4.2 模块一：Spatial Perception（空间感知）

**职责**：将Agent当前空间节点的数值属性转化为**客观结构性描述**，注入Agent的决策上下文。

**关键设计变更（vs v1）**：

v1中的转换器使用了解释性/暗示性语言（如"这是社交中心""隐私很好"），被评审一致认为是"循环论证/prompt泄漏"。v2将描述改为**严格客观的结构性陈述**，让LLM自行推理行为含义。

**三种表征方式（用于消融对比）**：

| 表征 | 示例 | 用途 |
|------|------|------|
| Raw Numeric | `integration=0.82, connectivity=4, openness=0.77, control=1.2` | 测试LLM能否直接处理数值 |
| Neutral Structural | "该位置与14个其他位置的平均拓扑距离为1.8步，直接连接4个相邻位置，可直接观察到12个位置，经过该位置可控制进出3个区域的通行" | **主方案**：客观事实，不含行为暗示 |
| Interpretive (v1风格) | "这是一个人流汇聚的核心区域，视野开阔，你的一举一动容易被注意到" | 对照：测试行为差异是否来自暗示性措辞 |

**主方案使用Neutral Structural**，Interpretive仅作为消融对比条件。

**输入数据结构**：

```json
{
  "location_id": "tavern_backroom",
  "location_name": "迷雾酒馆 - 密室",
  "spatial_metrics": {
    "integration": 0.32,
    "connectivity": 2,
    "openness": 0.15,
    "control_value": 0.85,
    "depth_from_entrance": 3
  },
  "dynamic_context": {
    "agents_present": ["Merchant_Elara", "Guard_Theron"],
    "time_of_day": "night"
  }
}
```

**转换逻辑（Neutral Structural模式）**：

```python
def spatial_to_language_neutral(node, all_nodes):
    """客观空间描述生成器 —— 不含任何行为暗示。"""
    desc = []

    # Integration → 位置可达性（纯事实）
    int_pct = percentile_rank(node.integration, [n.integration for n in all_nodes])
    avg_dist = round((len(all_nodes) - 1) / node.integration, 1) if node.integration > 0 else "∞"
    desc.append(f"该位置与其他所有位置的平均拓扑距离为{avg_dist}步（在所有位置中排第{int_pct}百分位）")

    # Connectivity → 连接数（纯事实）
    desc.append(f"该位置直接连接{node.connectivity}个相邻位置")

    # Openness → 可观察范围（纯事实）
    visible_count = sum(1 for n in all_nodes if is_visible(node, n))
    desc.append(f"从该位置可以直接观察到{visible_count}个其他位置")

    # Control Value → 通行控制（纯事实）
    if node.control_value > 1.0:
        controlled = len([n for n in neighbors(node) if connectivity(n) <= 2])
        desc.append(f"经过该位置可控制进出{controlled}个区域的通行")

    # 动态信息（纯事实）
    n_agents = len(node.agents_present)
    if n_agents == 0:
        desc.append("此刻该位置无人")
    else:
        desc.append(f"此刻该位置有{n_agents}人在场：{'、'.join(node.agents_present)}")

    return "。".join(desc) + "。"
```

**设计原则**：

1. **客观陈述，不暗示行为**——"平均距离1.8步"而非"核心区域"
2. **使用百分位排名**使描述跨构型可比
3. 融合静态指标与动态信息，但严格区分二者

### 4.3 模块二：Spatial Action Sampling（空间条件化行为采样）

**职责**：确保空间对Agent行为有可控的影响力度，不完全依赖LLM对空间描述的"自愿"遵循。

**算法流程**：

```
输入: 当前空间上下文S (Neutral Structural描述), Agent状态A, 对话上下文C
输出: 最终行为 action*

Step 1: 生成候选行为（不含空间信息的prompt）
  让LLM生成K=5个候选行为 {a_1, ..., a_5}

Step 2: 空间适配性评分
  对每个候选行为 a_k:
    使用独立的Judge模型评估 score_k = SpatialFitness(a_k, S)
    Judge prompt: "给定以下空间客观描述：{S}，
                   该Agent选择了以下行为：{a_k}，
                   请判断该行为在此空间条件下是否合理（0-1分）。
                   注意：只评估行为与空间条件的匹配度，
                   不评估文字质量、生动性或细节丰富程度。"

Step 3: 加权采样
  P(a_k) = softmax(score_k / temperature)
  action* = sample(P)
```

**关键改进（vs v1）**：

1. Judge模型与Actor模型**必须不同**（如Actor用Qwen-Max，Judge用GPT-4o或DeepSeek）
2. Judge rubric明确排除"文字质量"这一混淆维度
3. 保留替代方案：如Judge API成本过高，可训练轻量评分模型

### 4.4 移至附录的模块

以下模块在v2主论文中**不作为核心贡献**，但在附录中描述并作为扩展实验：

**Spatial Memory Retrieval（空间记忆检索）**：

- 原理保留（场景依赖记忆），但权重值不硬编码
- 改用embedding-based空间相似度（空间特征向量化 + 余弦相似度）
- 权重α/β/γ/δ通过超参数搜索确定，而非人工设定

**Spatial Planning（空间效用规划）**：

- 移除硬编码效用函数（被评审批评为"退化成经典Utility-based AI"）
- 改为让LLM通过Chain-of-Thought推理选择目的地：给出所有可达位置的客观空间特征，让LLM自行推理最优去处
- 这样体现的是LLM的空间推理能力，而非人工编写的算式

---

## 第五部分：实验设计

### 5.0 预实验：LLM空间推理能力测试

**目的**：在正式实验前，验证所选LLM能否理解我们的空间描述并做出合理推理。

**方法**：给单个Agent不同的空间描述，测试它能否正确回答关于空间属性的问题：

- "根据描述，这个地方适合私密对话吗？为什么？"
- "从你的位置能观察到几个方向的人？"
- "如果你需要快速离开，有几条路线可选？"

**决策规则**：如果LLM在Neutral Structural描述下的回答准确率 < 70%，则需简化描述粒度或更换模型。

### 5.1 三阶段递进实验设计

```
阶段1: 机制验证              阶段2: 行为效应              阶段3: 社会涌现
(LLM能理解空间吗?)     →    (空间信息改变行为吗?)    →   (空间构型塑造社会吗?)

微任务 / 单Agent              同地图多baseline对比         多地图长期模拟
                              多Agent短期模拟              网络分析 + 人类评估

前置条件：无                  前置：阶段1通过              前置：阶段2效应显著
```

**逻辑递进关系**：每个阶段是下一阶段的**前提条件**。如果阶段1表明LLM无法理解空间描述，则不进入阶段2；如果阶段2表明空间认知效应不显著，则阶段3的涌现分析将缺乏基础。

---

### 阶段1：机制验证（预计2周）

#### Exp1A: 表征方式对比

**目的**：验证真正有效的是"正确的空间结构化表征"，而非"多写两句描述"。

**实验条件**（6个）：

| 条件 | 空间信息 | 目的 |
|------|---------|------|
| C0: No Space | 无任何空间信息 | 最低基线 |
| C1: Name Only | 仅地点名（"酒馆密室"） | 排除语义标签已足够的可能 |
| C2: Rich Non-Spatial | 等长度非空间描述（天气、历史、NPC衣着） | 排除"更多上下文=更好"的效应 |
| C3: Raw Numeric | Space Syntax原始数值 | 测试LLM对数值的处理能力 |
| **C4: Neutral Structural** | **客观空间结构描述（主方案）** | **核心测试条件** |
| C5: Shuffled Signal | 空间指标错配到错误地点 | 验证正确信息的必要性 |

**任务设计**：不做完整社会模拟，而是设计一组**干净的单Agent微任务**：

1. **秘密透露决策**：Agent持有秘密，在不同空间条件下判断是否透露
2. **社交主动性**：Agent遇到另一NPC，决定是主动搭话、简短寒暄还是回避
3. **位置选择**：Agent有特定目标（如密谈），从3个候选位置中选择
4. **停留/离开**：Agent在某位置，判断是否继续停留

每个微任务 × 6个条件 × 20个不同空间场景 × 3次重复 = 1,440次LLM调用

**核心比较**：

- C4 vs C0: 空间信息是否有效
- C4 vs C1: 结构化特征是否优于简单标签
- C4 vs C2: 空间特征是否优于等量非空间上下文
- C4 vs C5: 正确空间信息是否必要
- C4 vs C3: 自然语言描述是否优于原始数值

#### Exp1B: 表征风格消融

**目的**：区分"空间结构理解"与"暗示性prompt措辞"的效果。

| 条件 | 描述风格 |
|------|---------|
| Neutral Structural（主方案） | "该位置与其他位置平均距离1.8步，直接连接4个位置" |
| Interpretive（v1风格） | "这是人流汇聚的核心区域，容易被注意到" |

如果Interpretive显著优于Neutral但Neutral不优于Name Only，说明效果来自暗示性措辞，而非空间结构理解——这将是一个重要的**负面发现**，需要在论文中诚实报告并调整架构。

---

### 阶段2：行为效应（预计4周）

**前提**：阶段1证明C4（Neutral Structural）显著优于C0/C1/C2/C5。

#### Exp2: 同地图多Agent行为效应

**在同一张地图（Plaza）上**对比以下Agent类型：

| Agent类型 | 移动策略 | 对话时的空间信息 | 目的 |
|-----------|---------|----------------|------|
| **Random Walk** | 随机选择相邻节点 | 无空间信息 | 度量拓扑必然效应的**下界** |
| **Topology-Only** | 与SpatialAgent相同的移动算法 | 无空间信息 | **分离拓扑效应 vs 认知效应**的关键对照 |
| **Rich-Context** | 与SpatialAgent相同 | 等长度非空间描述 | 排除"更多context"效应 |
| **Shuffled-Signal** | 与SpatialAgent相同 | 错配的空间信息 | 验证正确信息的必要性 |
| **SpatialAgent-Lite** | LLM CoT推理选目的地 | Neutral Structural描述 | **核心实验条件** |

**运行参数**：

- 10 Agent × 200轮 × 5条件 × **15次重复**（不同随机种子）
- 总调用量：约150,000次

**核心比较链**：

```
SpatialAgent > Topology-Only → 空间认知有额外贡献
SpatialAgent > Rich-Context  → 不只是"更多context"
SpatialAgent > Shuffled      → 正确空间信息是关键
Topology-Only > Random Walk  → 拓扑结构本身有效应（非Agent认知）
```

**评估指标**：

| 指标 | 定义 | 分析单元 |
|------|------|---------|
| BSC（行为空间一致性） | 不同类型空间中Agent行为的差异度 | 每个run的条件均值 |
| SDR（秘密透露合理性） | P(reveal \| private_space) - P(reveal \| public_space) | 每次秘密透露事件 |
| 社交主动性差异 | 高Integration区域 vs 低Integration区域的主动对话比例 | 每个run的区域均值 |
| 行为适配度（结构化标注） | Agent行为类型（公开讨论/低声/拒绝/转移）与空间条件的匹配度 | 每次交互事件 |

#### Exp2-Ablation: 架构消融

在SpatialAgent-Lite上做消融：

| 条件 | 保留模块 | 目的 |
|------|---------|------|
| Full | Perception + Action Sampling | 完整主方案 |
| -Perception | 仅Action Sampling（但用Name Only作为空间信息） | 评估Perception模块贡献 |
| -ActionSampling | 仅Perception（无候选评分，直接LLM输出） | 评估Action Sampling贡献 |

#### Exp2-Feature: 特征消融

在保持完整架构的情况下，逐一移除空间指标：

| 条件 | 移除的指标 |
|------|----------|
| Full | 全部4个指标 |
| -Integration | 移除Integration描述 |
| -Openness | 移除Openness描述 |
| -Control | 移除Control Value描述 |
| -Connectivity | 移除Connectivity描述 |

> 架构消融与特征消融**严格分开**，避免评审质疑混淆。

---

### 阶段3：社会涌现探索（预计4周）

**前提**：阶段2证明SpatialAgent > Topology-Only（空间认知效应显著）。

#### Exp3: 多地图涌现分析

使用三种空间构型，**每种构型同时运行SpatialAgent和Topology-Only Agent作为对照**：

| 条件 | Agent类型 | 空间构型 |
|------|----------|---------|
| Plaza-Spatial | SpatialAgent-Lite | 广场型 |
| Plaza-TopoOnly | Topology-Only | 广场型 |
| Labyrinth-Spatial | SpatialAgent-Lite | 迷宫型 |
| Labyrinth-TopoOnly | Topology-Only | 迷宫型 |
| Grid-Spatial | SpatialAgent-Lite | 网格型 |
| Grid-TopoOnly | Topology-Only | 网格型 |

每条件：200轮 × 15次重复

**核心分析**：

不再简单声称"三种构型涌现不同"（这是拓扑必然的），而是分析：

> **空间化Agent在不同构型下表现出的行为偏移，是否系统性地大于Topology-Only Agent？**

具体指标：

| 指标 | 定义 | 分析方法 |
|------|------|---------|
| 社交网络结构差异 | degree centrality, clustering coefficient, density | Mixed-Effects Model: layout × agent_type 交互项 |
| 信息传播速度 | 谣言从源头到50%/100% Agent的轮数 | 每个run一个数据点 |
| 信息中介涌现 | betweenness centrality最高的Agent是否位于高Control Value节点 | 位置-角色关联分析 |
| 空间-社交耦合度 | 空间距离矩阵与社交频率矩阵的相关性 | Mantel test |
| **认知增量** | Spatial条件各指标 - TopoOnly条件各指标 | **核心新增指标** |

#### Exp3-Minimal: 最小差异对实验

为更干净地回答"哪个空间属性起作用"，增加两组**只改变单一属性**的对比：

| 对比 | 操控 | 其他控制 |
|------|------|---------|
| 对A | 同一地图，将中心广场拆为两个小广场（改变Integration分布） | 拓扑、节点数、功能标签不变 |
| 对B | 同一地图，给某些通道加/减视线遮挡（改变Openness） | 拓扑连通性不变 |

#### Exp4: 人类评估（修订版）

**被试**：40-50人（扩大样本量），从游戏玩家社区和一般互联网用户各招一半（控制空间敏感度偏差）

**材料设计**（关键改进）：

- 给评估者看**简化地图位置示意图 + 对话内容**，而非v1中的空间语言描述
- 双盲设计：评估者不知道哪组是SpatialAgent
- A/B pairwise比较 + Likert量表

**评估问题**：

1. "这个NPC的行为是否符合其所处位置的特点？"（环境一致性，Likert 1-7）
2. "这个NPC的行为是否像一个真人？"（行为可信度，Likert 1-7）
3. A/B强制二选一："哪组NPC更像真人？"
4. **新增控制问题**："你是否觉得NPC的行为被人为操控/引导了？"（Likert 1-7）——如果此分数高，说明方法太"刻意"

**统计方法**：

- 配对t检验 + Cohen's d效应量
- 报告 inter-rater agreement（Krippendorff's α）
- Attention check题剔除不合格被试

---

## 第六部分：评估体系（重构版）

### 6.1 结构化行为标注替代开放评分

v1中的LLM-as-Judge使用开放式"评分1-5分"，被评审指出容易产生"更具体=更高分"的偏好偏差。v2改为**结构化行为标注**：

**步骤1**：对Agent的每次交互行为进行自动分类标注：

```
行为类型 = {公开讨论, 低声交谈, 拒绝交流, 转移话题, 主动搭讪,
            分享秘密, 回避某人, 提供帮助, 请求帮助, 交易, 巡逻, 等待}
```

**步骤2**：由研究者预先定义**空间-行为适配规则表**：

| 空间条件 | 适配行为 | 不适配行为 |
|---------|---------|-----------|
| 高Openness + 多人在场 | 公开讨论、主动搭讪 | 分享秘密 |
| 低Openness + 少人 | 低声交谈、分享秘密 | 大声公开讨论 |
| 高Control Value | 巡逻、等待、拦截 | — |

**步骤3**：计算**行为适配率**：适配行为次数 / 总行为次数

> 这样评估的是**行为决策本身**，而非文本的表面质量。

### 6.2 交叉模型验证

| 角色 | 模型 |
|------|------|
| Actor（Agent推理） | Qwen-Max |
| Judge（行为标注） | GPT-4o |
| Secondary Judge | DeepSeek-V3 |

报告两个Judge之间的一致性（Cohen's κ），关键case人工复核。

### 6.3 统计分析计划（预注册级别）

**独立样本单位**：模拟run（非单轮对话）

**统计方法**：

- 阶段1微任务：卡方检验（行为类型分布差异）
- 阶段2行为效应：Linear Mixed-Effects Model
  - 固定效应：agent_type（条件）
  - 随机效应：run, agent_pair
  - 嵌套效应：round within run
- 阶段3涌现分析：ANOVA + post-hoc Tukey HSD
  - 核心检验：layout × agent_type 交互项
- 多重比较校正：Benjamini-Hochberg FDR

**效应量报告**：所有显著结果报告Cohen's d或η²

---

## 第七部分：实验环境

### 7.1 The Misty Tavern（迷雾酒馆世界）

- Text-based RPG，中世纪奇幻主题
- 每张地图20个空间节点，10个NPC Agent
- 三种构型使用**相同功能节点**，仅改变拓扑关系

### 7.2 移动模型（新增明确定义）

| 参数 | 设定 | 理由 |
|------|------|------|
| 移动时间成本 | 每移动一步消耗1轮 | 简化模型，便于控制 |
| 节点容量 | 无上限 | 避免引入额外混淆变量 |
| 路径偶遇 | Agent移动经过中间节点时，有50%概率与在场Agent产生短暂交互 | 保留Labyrinth通道中的社交机会 |
| 停留时间 | 每次到达目的地后停留2-5轮（LLM自主决定） | 平衡移动与交互 |
| 模拟时间映射 | 1轮 = 游戏内30分钟，200轮 ≈ 游戏内约4天 | 明确时间尺度 |

### 7.3 NPC Agent配置

10个NPC，配置沿用v1设计。增加两类任务标注：

- **空间敏感任务**：密谈、交换情报、跟踪、踩点（预期受空间强烈影响）
- **空间不敏感任务**：日常寒暄、固定交易、例行巡逻（预期受空间影响较弱）

> 如果方法只在空间敏感任务上有效，这是好事——说明边界条件清楚。

### 7.4 三种空间构型的定量描述

每种构型在论文中将报告以下标准Space Syntax汇总指标：

| 指标 | Plaza | Labyrinth | Grid |
|------|-------|-----------|------|
| Mean Integration | — | — | — |
| Integration Variance | 高 | 低 | 中 |
| Mean Connectivity | — | — | — |
| Mean Depth | — | — | — |
| Intelligibility (r²) | 高 | 低 | 中 |
| Integration Core (top 20%) | 集中于广场 | 分散 | 多中心 |
| 死胡同数量 | 少 | 多 | 无 |

> 具体数值在构型实现后填入。

---

## 第八部分：预期贡献（收缩版）

### 8.1 跨学科桥梁贡献（主贡献）

首次探索建筑学Space Syntax理论在LLM Agent社会模拟中的应用，建立两个领域之间的学术桥梁。

### 8.2 架构贡献

提出SpatialAgent-Lite：通过Spatial Perception和Spatial Action Sampling两个模块，将客观空间结构化表征注入Agent的认知和行为选择循环。

### 8.3 实验方法论贡献

设计了一套**区分拓扑必然效应与空间认知效应**的实验协议，包括梯度化baseline对照和三阶段递进验证。

### 8.4 实证贡献

提供控制性实验证据，表明空间结构化表征与Agent交互模式之间存在系统性关联，并在若干设置下呈现可重复的行为偏移。

### 8.5 开源贡献

发布Space Syntax计算工具包、三种空间构型评测环境、SpatialAgent-Lite框架代码和评估脚本。

---

## 第九部分：资源需求与预算

### 9.1 API调用估算

| 实验 | 调用量估算 | 备注 |
|------|----------|------|
| 预实验（LLM空间理解测试） | ~500次 | |
| 阶段1 Exp1A+1B | ~5,000次 | 微任务，调用量小 |
| 阶段2 Exp2（5条件 × 15重复） | ~150,000次 | 主要成本来源 |
| 阶段2 消融 | ~90,000次 | 架构消融 + 特征消融 |
| 阶段3 Exp3（6条件 × 15重复） | ~180,000次 | |
| 阶段3 最小差异对 | ~60,000次 | |
| Judge评估 | ~50,000次 | 结构化标注 |
| 调试与迭代 | ~20,000次 | |
| **总计** | **~555,000次** | |

### 9.2 成本估算

| 方案 | 模型选择 | 总成本 |
|------|---------|--------|
| 经济方案 | Actor: DeepSeek-V3, Judge: GPT-4o-mini | ~¥1,500 |
| 推荐方案 | Actor: Qwen-Max, Judge: GPT-4o | ~¥12,000 |
| 混合方案 | 阶段1-2用DeepSeek，阶段3用Qwen-Max | ~¥5,000 |

> v2的实验量显著大于v1（v1约¥2,730），因为增加了大量baseline和重复次数。建议采用混合方案。

### 9.3 人类评估

- 40-50人 × ¥30/人 = ¥1,200-1,500

### 9.4 总预算

| 方案 | API成本 | 人类评估 | 合计 |
|------|--------|---------|------|
| 经济版 | ¥1,500 | ¥1,200 | **¥2,700** |
| 推荐版 | ¥5,000 | ¥1,500 | **¥6,500** |

---

## 第十部分：时间线（修订版）

```
2026年3月下旬 - 4月上旬（W1-3）
  ├── 精读P0论文（Generative Agents, Hillier Ch.3-5, Turner VGA）
  ├── 写阅读笔记
  ├── 实现Space Syntax核心指标计算（NetworkX）
  └── 设计三种空间构型 + 计算并验证指标

2026年4月中旬（W4-5）
  ├── 搭建Text-based RPG模拟引擎基础版
  ├── 实现Spatial Perception模块（三种表征方式）
  ├── 运行预实验：LLM空间推理能力测试
  └── 运行阶段1：Exp1A + Exp1B（微任务验证）
      → 决策点：如果阶段1失败，调整表征方案或更换模型

2026年4月下旬 - 5月上旬（W6-8）
  ├── 实现Spatial Action Sampling模块
  ├── 实现5种Agent类型（SpatialAgent + 4个baseline）
  ├── 搭建10NPC完整世界
  ├── 端到端联调
  └── 运行阶段2：Exp2 + 消融实验
      → 决策点：如果SpatialAgent未显著优于Topology-Only，调整方案

2026年5月中旬 - 6月上旬（W9-12）
  ├── 运行阶段3：Exp3多地图涌现分析
  ├── 运行最小差异对实验
  ├── 社交网络分析 + 信息传播分析
  └── 所有自动评估数据整理、初步画图表

2026年6月中旬 - 7月上旬（W13-16）
  ├── 准备人类评估材料 + 招募被试
  ├── 执行Exp4人类评估
  ├── 撰写论文Method + Experiments
  └── 撰写Results

2026年7月（W17-20）
  ├── 撰写Introduction + Related Work + Theory + Discussion
  ├── 论文内部review + 修改
  └── 投稿（首选AAMAS-27 / 备选AAAI-27摘要截止7月25日）
```

---

## 第十一部分：风险评估与应对

| 风险 | 可能性 | 影响 | 应对策略 |
|------|--------|------|---------|
| 阶段1失败：LLM无法区分不同空间表征 | 中 | 致命 | 1) 简化描述粒度 2) 增加few-shot示例 3) 更换模型 4) 若全部失败→这本身是重要负面发现，可写成"LLM空间推理局限性"论文 |
| 阶段2：SpatialAgent未优于Topology-Only | 中 | 高 | 1) 说明拓扑效应是主要驱动力→仍有理论价值 2) 改写论文定位为"空间构型对Agent社会的topology-driven效应" |
| Neutral描述不如Interpretive有效 | 高 | 中 | 诚实报告→说明"当前LLM需要暗示性空间描述才能产生行为偏移"→有方法论价值 |
| API成本超预算 | 中 | 中 | 混合方案：关键实验用Qwen-Max，其余用DeepSeek |
| 人类评估控制问题得分高（"感觉被操控"） | 中 | 高 | 进一步降低描述的引导性；这也是重要发现——说明方法需要更隐式的空间注入方式 |
| 审稿人仍质疑"只是prompt engineering" | 高 | 高 | 1) Shuffled条件是最强证据 2) 表征消融分梯度呈现 3) 收缩主张到可defend范围 |
| Space Syntax指标在小图上区分度不够 | 中 | 中 | 1) 报告指标分布+相关矩阵 2) 最小差异对实验补充因果识别 |

---

## 第十二部分：论文结构草案（修订版）

```
Title: Where You Are Shapes Who You Become:
       Space Syntax-Informed LLM Agents for Spatially Believable Game Worlds

Abstract (200 words)
  - 问题：现有LLM Agent架构缺乏对空间构型的显式建模
  - 方法：引入建筑学Space Syntax的结构化空间表征，提出SpatialAgent-Lite
  - 关键实验设计：梯度化baseline + 三阶段递进验证 + 拓扑-认知效应分离
  - 结果：具体数字

1. Introduction (1.5页)
   - LLM Agent的成功与空间认知的缺失（注意：不说"空间盲"，说"缺乏构型级空间建模"）
   - 建筑学Space Syntax的核心洞察
   - 两个理论跳跃的声明
   - 本文贡献（4条，措辞谨慎）

2. Related Work (1页)
   2.1 LLM-based Game Agents
   2.2 Space Syntax and Agent Simulation
   2.3 Context-Aware NPC Systems
   2.4 Embodied AI / Spatial Reasoning in LLMs（新增）
   → 指出三个领域的空白交叉点

3. Theoretical Framework (1页)
   3.1 Space Syntax指标定义（含Openness的重新定义）
   3.2 空间-行为机制假设 H1-H4
   3.3 与Hillier的理论对话：空间构型作为社会关系基础设施
   3.4 从物理空间到文本空间的迁移论证

4. SpatialAgent-Lite Architecture (1页)
   4.1 架构总览（2模块）
   4.2 Spatial Perception：客观结构化空间描述
   4.3 Spatial Action Sampling：空间条件化行为选择

5. Experimental Design (1.5页)
   5.1 三阶段递进设计总览
   5.2 阶段1：表征验证（Exp1A + 1B）
   5.3 阶段2：行为效应（Exp2 + 消融）
   5.4 阶段3：涌现分析（Exp3 + 最小差异对 + 人类评估）
   5.5 移动模型与环境参数

6. Results (1.5页)
   6.1 阶段1结果
   6.2 阶段2结果
   6.3 阶段3结果
   6.4 人类评估结果
   6.5 假设验证汇总

7. Discussion (1页)
   7.1 Space Syntax理论在虚拟Agent中的适用性——两种解释的讨论
   7.2 拓扑效应 vs 认知效应的相对贡献
   7.3 对游戏设计和PCG的实践启示
   7.4 局限性：
       - 文本环境的生态效度
       - 20节点图的规模限制
       - LLM空间推理能力的边界
       - 单一主题世界的外部效度
   7.5 面向建筑学社区的价值

8. Conclusion (0.25页)

References (~60篇，增加Embodied AI文献)

Appendix:
  A. Spatial Memory Retrieval扩展模块
  B. Spatial Planning扩展模块（LLM CoT版本）
  C. 三种构型完整指标表 + 指标相关矩阵
  D. 10个NPC人设详情
  E. Prompt模板（三种表征方式完整文本）
  F. 完整实验数据表
```

总页数：约8页正文 + 参考文献 + 附录

---

## 第十三部分：投稿策略

| 目标 | 截止日期 | 适配度 | 需要强化的点 |
|------|---------|:------:|------------|
| **AAMAS-27** | 2026年10月（预估） | ★★★★★ | 多Agent涌现、空间构型效应——审稿人最懂 |
| AAAI-27 | 2026年8月1日 | ★★★ | 方法严谨性、baseline公平性——时间紧 |
| CHI 2027 | 2026年9月（预估） | ★★★ | 需强化人类评估和设计启示 |
| IJCAI-27 | 2027年1月（预估） | ★★★ | 备用 |

**推荐路线**：7-8月完成实验和写作 → 首投AAMAS-27（最匹配）→ 若被拒，根据审稿意见修改后投AAAI-28或CHI 2028。

---

## 附录：给自己的Checklist

投稿前必须确认的事项：

- [ ] 阶段1通过：Neutral Structural显著优于No Space、Name Only、Rich Context、Shuffled
- [ ] 阶段2通过：SpatialAgent > Topology-Only（空间认知有额外贡献）
- [ ] 四个指标的相关矩阵已报告
- [ ] 每种构型的标准Space Syntax汇总指标已报告
- [ ] 所有统计分析使用Mixed-Effects Model或相应方法
- [ ] 多重比较已做FDR校正
- [ ] LLM-as-Judge使用结构化行为标注而非开放评分
- [ ] Judge模型与Actor模型不同
- [ ] 人类评估 ≥ 40人，含attention check和inter-rater agreement
- [ ] 人类评估控制问题（"感觉被操控"）得分在可接受范围
- [ ] Discussion中正面讨论了"LLM训练数据常识 vs Space Syntax理论普适性"
- [ ] Discussion中坦诚讨论了文本环境的生态效度局限
- [ ] 论文中未使用过度强硬的措辞（"prove" → "provide evidence"）
