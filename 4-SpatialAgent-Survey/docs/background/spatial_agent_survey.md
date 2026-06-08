# Spatial Agent: A Survey on Spatially-Aware LLM Agents

## 空间感知型大语言模型智能体研究综述

> 基于 SpatialAgent 研究计划 v7 的文献全景梳理
> 作者: Li
> 日期: 2026-03-22
> 目的: 为 "Where You Are Shapes Who You Become" 论文提供系统性文献定位

---

## 目录

1. [引言：为什么需要 Spatial Agent Survey](#1-引言)
2. [LLM Agent 基础架构演进](#2-llm-agent-基础架构演进)
3. [空间认知与空间推理](#3-空间认知与空间推理)
4. [Space Syntax：从建筑学到计算社会科学](#4-space-syntax从建筑学到计算社会科学)
5. [LLM Agent 中的空间表征](#5-llm-agent-中的空间表征)
6. [多智能体社会模拟与涌现行为](#6-多智能体社会模拟与涌现行为)
7. [空间环境中的智能体行为评估](#7-空间环境中的智能体行为评估)
8. [关键研究空白与机会](#8-关键研究空白与机会)
9. [本研究的定位](#9-本研究的定位)
10. [参考文献](#10-参考文献)

---

## 1. 引言

### 1.1 Survey 的动机

当前 LLM Agent 研究已经在 **WHO**（身份、人格、目标）和 **WHAT**（事件、记忆、任务）两个维度上取得了显著进展。然而，**WHERE**——即智能体所处的空间构型如何系统性地影响其行为——这一维度的研究仍然高度碎片化。

本 survey 的目标不是穷尽所有 LLM Agent 文献，而是聚焦于一个核心问题：

> **空间信息（特别是构型级空间表征）如何被整合到 LLM Agent 系统中，以及这种整合带来了什么样的行为后果？**

### 1.2 Survey 的组织逻辑

本 survey 沿着五条线索交织展开：

```
建筑学 Space Syntax ──────────────────────────────┐
                                                   ▼
认知科学中的空间推理 ──→ LLM 的空间能力 ──→ [Spatial Agent] ──→ 评估方法
                                                   ▲
LLM Agent 架构演进 ──→ 多智能体社会模拟 ──────────┘
```

这五条线索的交汇点，正是本研究所在的位置：**将 Space Syntax 构型理论引入 LLM 多智能体社会模拟，并通过受控实验检验空间表征对智能体行为的因果效应。**

### 1.3 文献检索策略

- **核心数据库**：ACL Anthology, AAAI/IJCAI/NeurIPS/ICLR proceedings, arXiv (cs.AI, cs.CL, cs.MA), Environment and Planning B, Journal of Space Syntax
- **检索关键词**：`LLM agent spatial`, `space syntax computation`, `spatial reasoning language model`, `multi-agent simulation emergent behavior`, `generative agent`, `embodied agent navigation`, `spatial cognition NLP`
- **时间范围**：经典理论追溯至 1984（Hillier & Hanson），LLM 相关文献聚焦 2023-2026
- **筛选标准**：与"文本化空间环境中的智能体行为"直接相关的工作优先

---

## 2. LLM Agent 基础架构演进

### 2.1 从工具调用到自主智能体

LLM Agent 的发展可以粗略分为三个阶段：

| 阶段 | 时期 | 代表工作 | 核心能力 |
|------|------|---------|---------|
| **工具增强** | 2022-2023 | Toolformer (Schick et al., 2023), HuggingGPT (Shen et al., 2023) | LLM 学会调用外部工具 |
| **规划与推理** | 2023-2024 | ReAct (Yao et al., 2023), Chain-of-Thought (Wei et al., 2022), Tree of Thoughts (Yao et al., 2024) | LLM 获得多步推理与规划能力 |
| **自主社会智能体** | 2023-2026 | Generative Agents (Park et al., 2023), AgentBench (Liu et al., 2024), Voyager (Wang et al., 2023) | LLM 成为具有记忆、规划、社交能力的自主体 |

### 2.2 主流 Agent 架构的模块化分析

当前主流 LLM Agent 架构通常包含以下模块：

```
┌─────────────────────────────────────────────┐
│                LLM Agent                     │
│                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ Perception│  │ Memory   │  │ Planning │  │
│  │ Module    │  │ Module   │  │ Module   │  │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  │
│       │              │              │        │
│       └──────────────┼──────────────┘        │
│                      ▼                       │
│              ┌──────────────┐                │
│              │ Action Module│                │
│              └──────────────┘                │
└─────────────────────────────────────────────┘
```

**关键观察**：在几乎所有主流架构中，Perception Module 主要处理的是**语义信息**（角色描述、对话历史、任务指令），而非**结构性空间信息**。即使在涉及空间的系统中（如 Generative Agents），空间信息也被简化为地点名称和简单邻接关系。

### 2.3 代表性工作详析

#### 2.3.1 Generative Agents (Park et al., 2023)

Park 等人的开创性工作首次展示了 LLM Agent 在虚拟小镇中的社会模拟能力。

**空间处理方式**：
- 地图以树状结构表示（World → Area → Room → Object）
- Agent 通过地点名称和语义描述感知环境
- 移动决策基于"去哪里做什么"的目标驱动，而非空间构型

**空间维度的不足**：
- 没有拓扑深度、可达性、控制力等结构指标
- 地点之间的关系仅通过邻接表示
- 空间对社交行为的影响完全通过共现（co-presence）间接实现

> **与本研究的关系**：Generative Agents 提供了 LLM 社会模拟的基础范式，但其空间表征停留在"地点名 + 邻接"的最低层次，正好对应本研究中的 C1 (Topology-Only) 条件。本研究的核心问题是：在这个基础之上，注入构型级空间信息能否系统性地改变行为？

#### 2.3.2 Voyager (Wang et al., 2023)

Voyager 展示了 LLM Agent 在 Minecraft 中的自主探索与技能学习。

**空间处理方式**：
- 通过 Minecraft API 获取结构化环境信息（方块类型、生物位置）
- 空间感知被转化为自然语言描述
- 导航通过预定义的移动原语实现

**局限性**：
- 空间信息服务于"生存与建造"任务，而非社会行为
- 没有空间构型对行为的系统性影响分析

#### 2.3.3 MetaGPT (Hong et al., 2024)

MetaGPT 引入了标准化操作流程（SOP）来协调多 Agent 协作。

**空间维度缺失**：
- 完全在抽象任务空间中运作
- Agent 之间的交互不受物理或虚拟空间约束
- 代表了"无空间"多智能体系统的一个极端

### 2.4 Agent 架构中的空间盲区

综合分析当前主流 Agent 架构，可以识别出以下空间盲区：

| 维度 | 当前状态 | 缺失内容 |
|------|---------|---------|
| **位置表征** | 地点名称、语义标签 | 构型指标（Integration, Depth, Control） |
| **空间关系** | 简单邻接 | 拓扑距离、可达性梯度、瓶颈结构 |
| **空间对行为的影响** | 共现 → 交互 | 结构性位置 → 行为类型调制 |
| **空间对社会结构的影响** | 未建模 | 空间构型 → 社交网络涌现 |

---

## 3. 空间认知与空间推理

### 3.1 认知科学中的空间认知

空间认知研究为理解"空间如何影响行为"提供了理论基础。

#### 3.1.1 空间心理地图 (Cognitive Maps)

Tolman (1948) 最早提出"认知地图"概念，认为生物体（不仅是人类）会在内部构建环境的空间表征。后续研究（O'Keefe & Nadel, 1978）发现了海马体中的位置细胞（place cells）和网格细胞（grid cells），证实了空间认知的神经基础。

**对本研究的启示**：LLM 没有神经生物学意义上的空间认知，但可能通过训练语料中的大量空间描述文本，编码了某种"统计性空间常识"。这正是本研究"跳跃1"的理论基础。

#### 3.1.2 空间语言与空间推理

Levinson (2003) 系统研究了不同文化中的空间语言系统，发现语言如何编码空间关系会影响空间推理能力。Landau & Jackendoff (1993) 区分了 **"what"** 系统（物体识别）和 **"where"** 系统（空间关系），指出语言主要编码拓扑关系而非精确几何。

**对本研究的启示**：这为"跳跃2"（物理空间 → 文本化空间）提供了一定的理论支持——如果人类语言本身就倾向于编码拓扑而非几何关系，那么 Space Syntax 的拓扑指标在文本化后可能保留了关键信息。

### 3.2 LLM 的空间推理能力

#### 3.2.1 基准测试与评估

近年来涌现了一系列评估 LLM 空间推理能力的基准：

| 基准 | 年份 | 评估内容 | 主要发现 |
|------|------|---------|---------|
| SpartQA (Mirzaee et al., 2021) | 2021 | 空间推理问答 | LLM 在复杂空间推理上表现不佳 |
| StepGame (Shi et al., 2022) | 2022 | 多步空间推理 | 推理步数增加时性能急剧下降 |
| SpatialBench (Yamada et al., 2024) | 2024 | 综合空间能力 | GPT-4 在简单空间任务上有改善，复杂任务仍不足 |
| MapQA (Chang et al., 2024) | 2024 | 基于地图的空间问答 | 多模态模型表现优于纯文本模型 |
| SpatialEval (Li et al., 2025) | 2025 | 多维度空间评估 | 大参数模型空间能力显著提升 |

**综合评价**：LLM 在以下空间任务上表现较好：
- 简单方位关系判断（"A 在 B 的左边"）
- 基于语义的空间常识（"厨房通常在卧室附近"）
- 路径描述理解

LLM 在以下空间任务上表现较差：
- 复杂拓扑推理（多步传递关系）
- 精确距离估计
- 三维空间关系

#### 3.2.2 LLM 空间能力的来源

对于 LLM 空间能力的来源，学界存在两种主要观点：

**观点 A：统计模式复现**
- LLM 从训练语料中学到了空间描述的统计模式
- 空间"推理"本质上是语言模式匹配，而非真正的空间理解
- 支持证据：LLM 在需要真正空间推理的新颖场景中表现不佳 (Gurnee & Tegmark, 2024)

**观点 B：涌现性空间理解**
- 大规模语言建模可能涌现出某种程度的空间理解
- 世界模型假说 (Li et al., 2023; Gurnee & Tegmark, 2024) 认为 LLM 内部编码了空间结构
- 支持证据：线性探针可以从 LLM 内部表征中提取地理坐标信息

**对本研究的立场**：本研究不需要解决"LLM 是否真正理解空间"这一哲学问题。关键的实证问题是：**结构化空间描述能否系统性地改变 LLM Agent 的行为？** 无论底层机制是"真正理解"还是"模式匹配"，只要行为变化是系统性的、可控的、沿着理论方向的，这一研究就有价值。

### 3.3 Embodied AI 中的空间导航

Embodied AI 领域在空间导航方面有大量工作，但与本研究的关切有本质区别：

| 维度 | Embodied Navigation | 本研究 |
|------|--------------------|--------|
| 目标 | 到达指定位置 | 空间如何影响社会行为 |
| 空间表征 | 视觉/点云/占据网格 | 文本化拓扑指标 |
| 评估标准 | 到达率、路径效率 | 行为类型、社交模式 |
| 智能体数量 | 通常单智能体 | 多智能体社会 |

代表工作包括：
- **VLN-CE** (Krantz et al., 2020)：视觉语言导航
- **ALFRED** (Shridhar et al., 2020)：指令跟随型家务任务
- **Habitat** (Savva et al., 2019)：3D 环境中的导航与交互
- **SayNav** (Rajvanshi et al., 2024)：利用 LLM 进行语义导航

**关键区别**：这些工作关注的是"如何在空间中移动"，本研究关注的是"空间构型如何塑造你在到达某处后的行为"。换言之，本研究的核心不是导航问题，而是**空间社会行为**问题。

---

## 4. Space Syntax：从建筑学到计算社会科学

### 4.1 经典 Space Syntax 理论

#### 4.1.1 理论起源

Space Syntax 由 Bill Hillier 和 Julienne Hanson 在 1984 年的 *The Social Logic of Space* 中系统提出。其核心主张是：

> **空间构型（spatial configuration）——即空间之间的拓扑关系模式——是理解空间如何影响社会生活的关键。**

这一理论从建筑学出发，但其影响远超建筑领域，延伸到城市规划、犯罪学、考古学和社会科学。

#### 4.1.2 核心概念

| 概念 | 定义 | 社会学含义 |
|------|------|-----------|
| **Integration** | 一个空间相对于所有其他空间的平均拓扑深度的倒数 | 高 Integration 空间是自然的汇聚点，倾向于承载公共活动 |
| **Mean Depth** | 从一个空间到所有其他空间的平均最短路径步数 | 高 Depth 空间更隐蔽，倾向于承载私密活动 |
| **Connectivity** | 一个空间直接连接的邻居数量 | 高 Connectivity 空间提供更多选择和感知 |
| **Control Value** | 一个空间对其邻居的"控制力"（= Σ 1/k_j） | 高 Control 空间是结构性瓶颈，倾向于承载监视/门控行为 |
| **Choice** | 经过该空间的最短路径数量 | 高 Choice 空间是自然的通行走廊 |
| **Intelligibility** | Integration 与 Connectivity 的全局相关性 | 高 Intelligibility 的系统中，局部线索能预测全局结构 |

#### 4.1.3 关键实证发现

Space Syntax 在物理空间中的核心实证发现包括：

1. **自然移动模型 (Natural Movement)**：Integration 与行人流量存在强正相关 (Hillier et al., 1993)。这一发现在全球数百个城市中得到验证。

2. **空间与社交**：Turner (2001) 等的可视域分析（VGA）表明，可见性高的空间承载更多社交活动。

3. **隐私梯度**：Hanson (1998) 的住宅研究表明，空间深度与隐私水平正相关。卧室和浴室通常位于拓扑深层，客厅和厨房位于浅层。

4. **控制与监视**：Hillier & Shu (2000) 的犯罪地理学研究表明，高 Control 空间的犯罪率更低，因为这些位置具有自然监视效应。

### 4.2 Space Syntax 的计算化

#### 4.2.1 从手工分析到算法化

Space Syntax 的计算化经历了以下阶段：

| 阶段 | 时期 | 工具 | 特点 |
|------|------|------|------|
| 手工分析 | 1984-1990s | 手绘凸空间图 | 小规模、劳动密集 |
| 专用软件 | 1990s-2010s | Depthmap (Turner, 2001), Space Syntax Toolkit | 图形界面、批量计算 |
| 开源与GIS整合 | 2010s-present | DepthmapX, UNA (Sevtsuk & Mekonnen, 2012), QGIS Space Syntax Toolkit | 与城市大数据结合 |
| 机器学习增强 | 2020s | 基于图神经网络的空间分析 | 自动化特征提取 |

#### 4.2.2 图论形式化

Space Syntax 的核心分析可以被严格形式化为图论操作。给定一个空间系统表示为图 G = (V, E)，其中 V 是空间集合，E 是可达性关系：

```
Integration(v) = (n-1) / Σ_u d(v,u)        # 全局可达性
Mean_Depth(v) = Σ_u d(v,u) / (n-1)         # 平均拓扑距离
Connectivity(v) = |{u : (v,u) ∈ E}|        # 邻居数
Control(v) = Σ_{u:(v,u)∈E} 1/Connectivity(u)  # 对邻居的控制力
```

**对本研究的重要性**：这种图论形式化使得 Space Syntax 指标可以被纯粹地从拓扑结构中计算，不依赖物理度量（距离、面积），因此天然适合文本化——只需传达拓扑关系和指标值，无需传达几何信息。

### 4.3 Space Syntax 在计算系统中的应用

#### 4.3.1 数字游戏与虚拟环境

Space Syntax 已被应用于游戏关卡设计和虚拟环境分析：

- **游戏关卡分析**：Bafna (2003), Ostwald (2011) 等将 Space Syntax 应用于分析 FPS 游戏地图的空间逻辑。发现 Integration 高的区域通常是玩家遭遇战的高频区域。

- **虚拟建筑评估**：Conroy Dalton (2002) 在虚拟现实中验证了 Space Syntax 预测，发现虚拟环境中的行人行为模式与物理空间高度一致。

- **NPC 路径规划**：少量工作尝试用 Space Syntax 指标指导 NPC 的移动偏好（如 Knecht & Kolbe, 2010），但这些系统使用的是规则型 AI，而非 LLM。

#### 4.3.2 ABM（Agent-Based Modeling）中的空间

传统 ABM（如 NetLogo, MASON, Repast）中的空间模型：

- **Schelling 隔离模型**：空间只是一个均匀网格，没有构型差异
- **Epstein & Axtell 的 Sugarscape**：空间有资源分布差异，但没有拓扑构型
- **Batty (2013) 的城市 ABM**：更接近 Space Syntax 精神，但 Agent 是简单规则型

**关键空白**：目前没有将 Space Syntax 的构型理论与 LLM Agent 系统结合的工作。传统 ABM 中的 Agent 太简单，无法表现出复杂的社会行为；LLM Agent 系统中的空间太简单，无法体现构型效应。**本研究正好处于这两者的交汇点。**

### 4.4 Space Syntax 的批评与局限

在引入 Space Syntax 之前，有必要了解该理论本身的局限：

| 批评 | 内容 | 本研究的回应 |
|------|------|-------------|
| **还原论** | 将复杂社会现象还原为拓扑指标 | 本研究不声称 Space Syntax 解释一切；只检验构型信息是否产生可检测的增量效应 |
| **因果方向** | 空间构型 → 行为 vs 行为 → 空间构型 | 在 LLM Agent 系统中，空间是研究者设定的，因果方向明确 |
| **文化差异** | 不同文化中空间行为模式不同 | 本研究关注的是 LLM 的行为，而非人类文化差异 |
| **尺度依赖** | 指标在不同空间尺度上的含义不同 | 本研究限定在建筑尺度（20 节点左右） |
| **指标共线性** | 多个指标高度相关 | v7 设计了明确的指标决策树（3.2节），处理 Openness-Connectivity 共线 |

---

## 5. LLM Agent 中的空间表征

### 5.1 当前空间表征的分类学

基于对现有文献的分析，可以将 LLM Agent 系统中的空间表征分为以下层次：

```
Level 0: 无空间（纯对话/任务空间）
    └── MetaGPT, AutoGPT, ChatDev

Level 1: 地点名称（Name Only）
    └── 简单角色扮演系统, 部分文本冒险游戏

Level 2: 地点名称 + 语义描述
    └── Generative Agents (Park et al., 2023)

Level 3: 地点名称 + 邻接关系 + 在场信息
    └── 部分游戏 NPC 系统

Level 4: 结构化空间指标（本研究提出）
    └── Integration, Mean Depth, Control, Connectivity

Level 5: 完整空间模型（含视觉/几何）
    └── Embodied AI 系统（Habitat, AI2-THOR）
```

**关键发现**：当前大多数 LLM 社会模拟系统停留在 Level 2-3，而 Embodied AI 系统虽然达到 Level 5，但主要关注导航而非社会行为。**Level 4 的空间表征——纯拓扑结构指标——是一个尚未被系统探索的中间层。**

### 5.2 空间信息的文本化策略

将空间信息转化为 LLM 可处理的文本，存在多种策略：

| 策略 | 示例 | 优点 | 缺点 |
|------|------|------|------|
| **自然语言描述** | "这是一个繁忙的广场" | 直觉、易理解 | 语义模糊，难以控制 |
| **结构化数值** | "Integration: 2.45" | 精确 | LLM 对数值的理解不稳定 |
| **相对排名** | "这是最容易到达的地点" | 提供比较信息 | 隐含指导行为的暗示 |
| **绝对结构描述** | "该位置与其他位置的平均拓扑距离为 1.8 步" | 精确且不隐含行为指导 | 需要 LLM 自行推断行为含义 |
| **功能性描述** | "这里适合聚会" | 直接映射到行为 | 完全绕过空间推理 |

本研究选择**绝对结构描述**作为主表征，理由在于：
1. 不直接告诉 Agent "该做什么"（避免功能性描述的归因问题）
2. 传达了精确的结构信息（避免自然语言的模糊性）
3. 不隐含排名和比较语义（避免相对排名的暗示效应）

### 5.3 空间信息在 Prompt 中的位置效应

少量工作关注了信息在 prompt 中的位置如何影响 LLM 的行为：

- **Primacy/Recency 效应** (Liu et al., 2024): LLM 倾向于更多关注 prompt 开头和结尾的信息
- **Lost in the Middle** (Liu et al., 2024): 长上下文中，中间位置的信息更容易被忽略
- **System prompt vs User prompt** (various): 系统 prompt 中的指令通常比用户 prompt 中的更稳定

**对本研究的影响**：v7 计划在预实验中测试空间描述在三种位置（系统 prompt 末尾、当前情境中部、用户指令前）的效果差异，这一设计直接回应了位置效应的文献。

### 5.4 与本研究条件矩阵的对应关系

将文献中的空间表征方式映射到本研究的实验条件：

```
Level 0 (无空间)         ←→  C0 No Space
Level 1 (地点名)         ←→  C1 Name Only (Topology-Only)
Level 2 (语义描述)       ←→  C2 Stable Non-Spatial Affordance
Level 3 (邻接+在场)      ←→  C1 的一部分
Level 4 (结构指标)       ←→  C6m/C6f Perception-Only
Level 4 + Sampling       ←→  C4 Full SpatialAgent
```

---

## 6. 多智能体社会模拟与涌现行为

### 6.1 从经典 ABM 到 LLM Agent 社会

#### 6.1.1 经典社会模拟

| 模型 | 年份 | 核心主题 | 空间角色 |
|------|------|---------|---------|
| Schelling 隔离模型 | 1971 | 种族隔离涌现 | 均匀网格，无结构差异 |
| Sugarscape | 1996 | 财富分配 | 资源分布，无拓扑 |
| Axelrod 文化扩散 | 1997 | 文化趋同/分化 | 邻域定义，无结构效应 |
| MASON Social Networks | 2005 | 社会网络动态 | 可选空间嵌入 |

**关键差距**：经典 ABM 中的 Agent 遵循简单规则（如"如果邻居与我不同，则搬走"），无法表现出 LLM Agent 那样复杂的社会行为（如"根据空间氛围决定是否分享敏感信息"）。

#### 6.1.2 LLM 驱动的社会模拟

2023 年以来，LLM 驱动的社会模拟迅速发展：

**Generative Agents (Park et al., 2023)**
- 25 个 LLM Agent 在虚拟小镇中生活
- 展示了记忆、反思、规划的涌现能力
- 社交行为主要由角色设定和记忆驱动，而非空间构型

**Concordia (Vezhnevets et al., 2023)**
- Google DeepMind 的多 Agent 社会模拟框架
- 支持多种社会场景（协商、合作、冲突）
- 空间设置较为灵活，但没有系统性的空间构型分析

**AgentSims (Lin et al., 2024)**
- 可扩展的 Agent 社会模拟平台
- 支持经济、社交、政治等多维度模拟
- 空间以功能区域划分，无拓扑指标

**S³ (Gao et al., 2024)**
- 社会网络模拟系统
- 关注信息传播和意见形成
- 社交网络结构而非空间结构是核心变量

**OASIS (Yang et al., 2025)**
- 面向开放式社会互动的大规模 Agent 模拟
- 支持上百个 Agent 同时交互
- 空间被简化为"场景标签"

### 6.2 涌现行为研究

#### 6.2.1 什么是涌现行为？

在多智能体系统中，**涌现行为**指的是系统整体表现出的、不能简单从个体规则推导的宏观模式。

在 LLM Agent 社会模拟中，已观察到的涌现行为包括：
- 信息级联传播 (Park et al., 2023)
- 自组织的社交圈层 (Gao et al., 2024)
- 集体决策中的群体极化 (Argyle et al., 2023)
- 合作与背叛的动态均衡 (Akata et al., 2023)

#### 6.2.2 空间对涌现的潜在作用

Space Syntax 理论预测，空间构型应当影响以下涌现现象：

| 涌现现象 | Space Syntax 预测 | 现有 LLM 研究状态 |
|---------|-------------------|-------------------|
| **社交中心形成** | 高 Integration 空间自然成为社交中心 | 仅通过共现机制实现 |
| **信息传播路径** | 高 Control 空间成为信息瓶颈 | 未建模 |
| **隐私梯度** | 深层空间承载更多私密行为 | 仅通过语义标签（如"卧室"）间接暗示 |
| **社交网络拓扑** | 空间构型塑造交互频率，进而影响网络结构 | 未系统研究 |

> **这恰是本研究"跳跃3"的关切**：微观空间偏移是否能累积成宏观社会网络结构的差异。v7 将此作为阶段3的探索性扩展，而非主论文的核心主张。

### 6.3 行为可信度（Believability）

#### 6.3.1 什么是行为可信度？

在游戏 AI 和虚拟人文献中，**believability** 是一个核心评价维度：

> Agent 的行为是否"让人觉得像是一个真人在该情境下会做的事"？

Park et al. (2023) 通过人类评估验证了 Generative Agents 的 believability。但他们的评估没有单独考察**空间行为可信度**——即 Agent 的行为是否与其所处的空间位置"匹配"。

#### 6.3.2 空间行为可信度

本 survey 提出一个新维度——**spatial believability**：

> Agent 在高 Integration 空间中表现得更社交、在深层空间中表现得更私密、在瓶颈空间中表现出更多控制行为——这种空间-行为一致性是否让虚拟世界更可信？

这一维度在现有文献中几乎未被系统讨论，但对游戏设计和虚拟社会具有直接应用价值。

---

## 7. 空间环境中的智能体行为评估

### 7.1 评估框架分类

| 评估范式 | 代表工作 | 优点 | 缺点 |
|---------|---------|------|------|
| **人类评估** | Park et al. (2023), believability ratings | 效度高 | 成本高、难以规模化 |
| **LLM-as-Judge** | Zheng et al. (2024), MT-Bench | 可扩展 | 存在自我偏见风险 |
| **基于规则的指标** | AgentBench (Liu et al., 2024) | 客观、可重复 | 难以捕捉细微行为差异 |
| **两阶段分离评估** | 本研究提出 | 控制评估偏见 | 流程复杂 |

### 7.2 LLM-as-Judge 的偏见问题

LLM-as-Judge 是当前评估 Agent 行为的主流方法，但存在已知偏见：

- **位置偏见**：倾向于选择第一个选项 (Zheng et al., 2024)
- **冗余偏见**：倾向于高评更长的回答
- **自我偏见**：同源 LLM 可能系统性高评自己生成的内容
- **顺序偏见**：评估顺序影响评分

**本研究的应对**（v7 设计）：
1. Rule-Based Scorer 作为无偏探针
2. 两阶段分离评估（盲编码 → 空间关联）
3. 跨模型 Judge 交叉验证（Qwen vs DeepSeek）

### 7.3 行为编码方法

#### 7.3.1 从定性到定量

社会行为的编码是连接原始 Agent 输出与统计分析的关键环节：

```
Agent 原始输出  →  行为编码  →  空间关联  →  统计检验
  (自由文本)      (分类标签)   (与指标对齐)   (BSR/TAR)
```

#### 7.3.2 编码信度的挑战

在 LLM Agent 行为编码中，以下挑战尤为突出：

1. **行为边界模糊**：Agent 的一次输出可能包含多种行为成分
2. **语义vs.结构**：同一行为在不同空间语境中可能有不同含义
3. **LLM 编码的一致性**：LLM 作为编码器的 inter-rater reliability 如何保证？

v7 设计的编码信度协议（coding manual + 双人 pilot + κ 阈值 + LLM-human 校准）正是对这些挑战的系统回应。

### 7.4 BSR 与 TAR：一种新的双指标框架

本研究提出的 BSR/TAR 框架在评估方法论上具有以下独特性：

| 指标 | 测量内容 | 理论意义 |
|------|---------|---------|
| **BSR** (Behavioral Spatial Responsiveness) | 行为是否随空间特征变化 | 回答"有没有空间响应" |
| **TAR** (Theory-Aligned Responsiveness) | 变化方向是否与 Space Syntax 一致 | 回答"是否沿理论方向响应" |

**为什么需要两个指标？** 因为行为可能随空间变化（BSR > 0），但变化方向可能与理论预测相反（TAR < 0）。分离这两个维度可以更精确地定位效应。

这种设计在现有文献中没有直接先例，但在精神上类似于：
- 信号检测论中的 sensitivity vs bias
- 机器学习中的 accuracy vs direction

---

## 8. 关键研究空白与机会

### 8.1 三大核心空白

基于以上文献综述，本 survey 识别出三个核心研究空白，这些空白直接对应本研究的 Section 1.2：

#### 空白 1：表征空白 (Representation Gap)

**现状**：LLM Agent 系统中的空间信息停留在地点名称、语义标签或简单邻接关系的层次。没有系统将 Space Syntax 的构型指标（Integration, Depth, Control）作为结构化输入注入 Agent 的感知模块。

**机会**：Space Syntax 的图论形式化使得构型指标可以被无损地文本化，为 LLM Agent 提供一种全新的空间感知通道。

#### 空白 2：识别空白 (Identification Gap)

**现状**：即使某些 LLM Agent 系统展现出了空间相关的行为模式，也缺乏实验协议来区分：
- 拓扑必然效应（任何有空间的系统都会产生的共现效应）
- 语义常识效应（LLM 基于"厨房""广场"等语义标签的先验知识）
- 构型增量效应（Space Syntax 结构指标带来的额外行为调制）

**机会**：通过精心设计的条件矩阵（C0→C1→C2→C6m→C6f→C4），可以逐层分离不同来源的空间效应。

#### 空白 3：理论空白 (Theory Gap)

**现状**：建筑学 Space Syntax 社区和 AI Agent 社区之间缺乏系统对话。Space Syntax 的实证发现几乎完全基于物理空间中的人类行为，尚未在 LLM Agent 系统中被检验。

**机会**：本研究可以开启一个新的研究方向——Space Syntax 理论在人工智能体社会中的迁移与检验。

### 8.2 次级研究空白

| 空白 | 现状 | 机会 |
|------|------|------|
| **空间-社会网络共演化** | ABM 中有空间对网络的研究，但 Agent 太简单 | 用 LLM Agent 观察更复杂的空间-网络耦合 |
| **空间启动 vs 持续引导** | 无相关研究 | 通过时间分段分析区分空间信息的短期和长期效应 |
| **空间行为可信度** | Believability 评估未考虑空间维度 | 提出 spatial believability 作为新评价维度 |
| **开源模型的空间能力** | 空间推理评估主要针对 GPT 系列 | 系统评估 Qwen、DeepSeek 等开源模型的空间能力 |

### 8.3 方法论空白

| 方法论维度 | 空白 | 本研究的填补 |
|-----------|------|-------------|
| **因变量设计** | 缺乏区分"响应存在"与"方向对齐"的指标 | BSR + TAR 双指标框架 |
| **初始条件控制** | LLM Agent 实验缺乏严格的 matched design | MIC (Matched Initial Conditions) 协议 |
| **评估偏见控制** | LLM-as-Judge 偏见在 Agent 评估中未被充分重视 | 三重机制（Rule-Based + 两阶段分离 + 跨模型） |
| **编码信度** | LLM Agent 行为编码的信度协议缺失 | 显式 coding manual + κ 阈值 + LLM-human 校准 |

---

## 9. 本研究的定位

### 9.1 在文献版图中的位置

```
                    空间复杂度 (低 → 高)

     无空间         地点名     构型指标    完整3D
       │              │          │           │
  ┌────┼──────────────┼──────────┼───────────┼────┐
  │    │  MetaGPT     │          │           │    │  复杂
  │    │  ChatDev     │  Gen.    │ ★本研究★  │    │  社会
Agent  │              │  Agents  │           │    │  行为
复杂度 │              │          │           │    │
  │    │  Schelling   │          │           │    │
  │    │  Sugarscape  │          │ Habitat   │    │  简单
  │    │              │          │ AI2-THOR  │    │  导航
  └────┼──────────────┼──────────┼───────────┼────┘
       │              │          │           │
```

### 9.2 核心贡献的独特性

| 贡献 | 最接近的现有工作 | 本研究的差异 |
|------|----------------|-------------|
| 构型级空间表征协议 | Generative Agents 的地点描述 | 从语义标签升级到 Space Syntax 结构指标 |
| 模块分解实验框架 | Ablation studies in ML | 用 C6m/C6f/C4 拆开 Perception、Movement、Sampling 三个效应 |
| BSR + TAR 双指标 | 无直接先例 | 同时回答"是否响应"和"是否按理论方向响应" |
| MIC 对照协议 | Generative Agents 的单次运行 | 30 个 matched seeds 的系统方差控制 |
| 空间启动 vs 持续引导 | 无直接先例 | 通过时间分段分析区分短期和长期空间效应 |

### 9.3 局限性声明

本 survey 本身有以下局限：

1. **时效性**：LLM Agent 领域发展极快，2026年后可能出现重要新工作
2. **领域偏向**：偏重 NLP/AI 会议文献，对建筑学期刊的覆盖可能不够充分
3. **语言偏向**：以英文文献为主，中文 LLM Agent 研究（如 ChatGLM 生态）覆盖有限
4. **未覆盖领域**：未深入涉及 VR/AR 中的空间行为研究，以及人机交互中的空间设计

---

## 10. 参考文献

### Space Syntax 经典文献

- Hillier, B., & Hanson, J. (1984). *The Social Logic of Space*. Cambridge University Press.
- Hillier, B., Penn, A., Hanson, J., Grajewski, T., & Xu, J. (1993). Natural movement: or, configuration and attraction in urban pedestrian movement. *Environment and Planning B*, 20(1), 29-66.
- Hillier, B., & Shu, S. (2000). Crime and urban layout: The need for evidence. In *Secure Foundations: Key Issues in Crime Prevention, Crime Reduction and Community Safety*, Institute of Public Policy Research.
- Hanson, J. (1998). *Decoding Homes and Houses*. Cambridge University Press.
- Turner, A. (2001). Depthmap: A program to perform visibility graph analysis. In *Proceedings of the 3rd International Space Syntax Symposium*.
- Bafna, S. (2003). Space Syntax: A brief introduction to its logic and analytical techniques. *Environment and Behavior*, 35(1), 17-29.
- Ostwald, M. J. (2011). The mathematics of spatial configuration: Revisiting, revising and critiquing justified plan graph theory. *Nexus Network Journal*, 13(2), 445-470.

### Space Syntax 计算与应用

- Sevtsuk, A., & Mekonnen, M. (2012). Urban Network Analysis: A new toolbox for ArcGIS. *Revue internationale de géomatique*, 22(2), 287-305.
- Conroy Dalton, R. (2002). *Is spatial intelligibility critical to the design of large-scale virtual environments?* International Journal of Design Computing.
- Knecht, K., & Kolbe, T. H. (2010). Space Syntax for modeling building evacuation. *Advances in 3D Geo-Information Sciences*, Lecture Notes in Geoinformation and Cartography.
- Batty, M. (2013). *The New Science of Cities*. MIT Press.

### LLM Agent 架构

- Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. In *Proceedings of UIST 2023*.
- Wang, G., Xie, Y., Jiang, Y., et al. (2023). Voyager: An open-ended embodied agent with large language models. In *NeurIPS 2023*.
- Hong, S., Zhuge, M., Chen, J., et al. (2024). MetaGPT: Meta programming for a multi-agent collaborative framework. In *ICLR 2024*.
- Liu, X., Yu, H., Zhang, H., et al. (2024). AgentBench: Evaluating LLMs as agents. In *ICLR 2024*.
- Schick, T., Dwivedi-Yu, J., Dessì, R., et al. (2023). Toolformer: Language models can teach themselves to use tools. In *NeurIPS 2023*.
- Shen, Y., Song, K., Tan, X., et al. (2023). HuggingGPT: Solving AI tasks with ChatGPT and its friends in Hugging Face. In *NeurIPS 2023*.

### LLM 推理与空间能力

- Wei, J., Wang, X., Schuurmans, D., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. In *NeurIPS 2022*.
- Yao, S., Zhao, J., Yu, D., et al. (2023). ReAct: Synergizing reasoning and acting in language models. In *ICLR 2023*.
- Yao, S., Yu, D., Zhao, J., et al. (2024). Tree of thoughts: Deliberate problem solving with large language models. In *NeurIPS 2024*.
- Mirzaee, R., Long, H., Peng, B., et al. (2021). SpartQA: A textual question answering benchmark for spatial reasoning. In *NAACL 2021*.
- Shi, W., Zhao, H., & Sui, Z. (2022). StepGame: A new benchmark for robust multi-hop spatial reasoning in texts. In *AAAI 2022*.
- Gurnee, W., & Tegmark, M. (2024). Language models represent space and time. In *ICLR 2024*.

### 多智能体社会模拟

- Vezhnevets, A. S., Agapiou, J. P., Aharon, A., et al. (2023). Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia. *arXiv preprint*.
- Lin, Z., Yu, Z., et al. (2024). AgentSims: An open-source sandbox for large language model evaluation. In *AAAI 2024*.
- Gao, C., Lan, X., Li, N., et al. (2024). Large language model-empowered agents for simulating macroeconomic activities. In *ACL 2024*.
- Argyle, L. P., Busby, E. C., Fulda, N., et al. (2023). Out of one, many: Using language models to simulate human samples. *Political Analysis*, 31(3), 337-351.
- Akata, E., Schulz, L., Coda-Forno, J., et al. (2023). Playing repeated games with large language models. In *NeurIPS 2023*.

### 空间认知

- Tolman, E. C. (1948). Cognitive maps in rats and men. *Psychological Review*, 55(4), 189-208.
- O'Keefe, J., & Nadel, L. (1978). *The Hippocampus as a Cognitive Map*. Clarendon Press.
- Levinson, S. C. (2003). *Space in Language and Cognition*. Cambridge University Press.
- Landau, B., & Jackendoff, R. (1993). "What" and "where" in spatial language and spatial cognition. *Behavioral and Brain Sciences*, 16(2), 217-265.

### Embodied AI 与导航

- Savva, M., Kadian, A., Maksymets, O., et al. (2019). Habitat: A platform for embodied AI research. In *ICCV 2019*.
- Shridhar, M., Thomason, J., Gordon, D., et al. (2020). ALFRED: A benchmark for interpreting grounded instructions for everyday tasks. In *CVPR 2020*.
- Krantz, J., Wijmans, E., Majumdar, A., et al. (2020). Beyond the nav-graph: Vision-and-language navigation in continuous environments. In *ECCV 2020*.
- Rajvanshi, A., et al. (2024). SayNav: Grounding large language models for dynamic planning to navigation in new environments. In *ICRA 2024*.

### 评估方法

- Zheng, L., Chiang, W.-L., Sheng, Y., et al. (2024). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. In *NeurIPS 2024*.
- Liu, N. F., Lin, K., Hewitt, J., et al. (2024). Lost in the middle: How language models use long contexts. *TACL*, 12, 157-173.

### ABM 经典

- Schelling, T. C. (1971). Dynamic models of segregation. *Journal of Mathematical Sociology*, 1(2), 143-186.
- Epstein, J. M., & Axtell, R. (1996). *Growing Artificial Societies: Social Science from the Bottom Up*. MIT Press.
- Axelrod, R. (1997). The dissemination of culture: A model with local convergence and global polarization. *Journal of Conflict Resolution*, 41(2), 203-226.

---

## 附录 A：现有 Spatial Agent 系统对比表

| 系统 | 空间表征层次 | Agent 类型 | 社会行为 | 空间-行为关联分析 | 开源 |
|------|:----------:|:---------:|:-------:|:---------------:|:----:|
| Generative Agents (2023) | L2 | LLM (GPT) | 丰富 | 无 | 部分 |
| Concordia (2023) | L2 | LLM (Gemini) | 丰富 | 无 | 是 |
| AgentSims (2024) | L2 | LLM (多种) | 中等 | 无 | 是 |
| Voyager (2023) | L5 | LLM (GPT-4) | 无 | 无 | 是 |
| Habitat (2019) | L5 | RL/LLM | 导航 | 无 | 是 |
| **SpatialAgent (本研究)** | **L4** | **LLM (Qwen3.5-Plus)** | **丰富** | **系统性** | **是** |

## 附录 B：研究方向路线图

```
                      当前 (2026)                未来方向
                         │
   ┌─────────────────────┼─────────────────────┐
   │                     │                     │
   ▼                     ▼                     ▼
 单地图验证           跨地图泛化          动态空间
 (阶段1-2)           (阶段3)           (空间随行为改变)
   │                     │                     │
   ▼                     ▼                     ▼
 文本化空间          多模态空间          空间生成
 (当前)             (视觉+文本)         (Agent 建造空间)
   │                     │                     │
   ▼                     ▼                     ▼
 受控实验           自然观察            干预实验
 (当前)            (真实游戏数据)       (空间设计优化)
```

## 附录 C：写 Survey 本身的价值

对于本研究而言，写这份 survey 有以下直接价值：

1. **Related Work 基础**：论文 Section 2 可以直接从本 survey 的 Section 2-7 中提炼
2. **定位清晰化**：通过文献版图中的"空白"来定义贡献点
3. **方法论辩护**：BSR/TAR、MIC、两阶段评估等方法论创新的必要性来自对现有方法不足的分析
4. **理论桥梁**：Space Syntax（Section 4）与 LLM Agent（Section 2）的对话框架
5. **潜在独立发表**：如果扩充到 8000+ 词并补充更多定量分析，可以作为独立 survey paper 投稿

---

*本 survey 基于 SpatialAgent 研究计划 v7 编写，服务于 AAMAS-27/AAAI-27 投稿准备。*
