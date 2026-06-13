# Survey 研究计划 v4

> 规范说明：本文件为当前 live 综述计划（survey_plan.md，综述项目以此代替 proposal.md）。历史版本见 docs/plans/archive/。

## Where Agents Dwell: A Scoping Review of Spatial Representation and Its Social Effects in LLM Multi-Agent Systems

> 日期: 2026-04-11  
> 作者: Li  
> 时间线: 12-14 周  
> 定位: Scoping review + research agenda  
> 变更记录: v4 回应 v3_r1 review — 补 corpus 分层、分析单位、双层空间编码、编码质控、§2 限重

---

## 一、核心定位

### 1.1 研究问题

> **What is known, what is missing, and what is needed to study how spatial configuration may shape social behavior in LLM multi-agent systems?**

本文不回答"空间构型是否/如何塑造 Agent 社会行为"这一因果命题——因为系统性实证证据尚不存在。本文回答的是一个 scoping 问题：在现有文献中，空间表征被如何使用、社会行为被如何生成、两者的交叉地带有多大的研究空白、以及未来实证研究需要什么样的概念工具和评估维度。

### 1.2 论文类型

**Scoping review + structured research agenda**，遵循 PRISMA-ScR 框架。

不是：
- 系统综述（corpus 不够大、不够同质）
- 立场文章（有系统检索和证据编码，不仅仅是 opinion）
- 方法论文（不提出完整的新方法体系）

### 1.3 核心论点

Space Syntax 在物理空间中积累了 40 年实证证据证明空间构型塑造人类社会行为。LLM 多智能体社会模拟已发展 3 年，但现有系统的空间表征几乎全部停留在地点名称或语义描述层面，尚未系统性地引入构型级空间信息。本文映射这一空白，提出空间表征分类学，建立跨领域证据地图，并规划"空间构型化智能体社会"的研究议程。

### 1.4 三个贡献（严格分层）

| 层级 | 贡献 | 性质 |
|------|------|------|
| **Primary** | 一张覆盖现有 LLM Agent 系统的空间表征 evidence map，识别构型层（L4）的系统性空白 | 描述性 — 来自文献编码 |
| **Secondary** | 一套连接 Space Syntax 理论与 LLM multi-agent 文献的桥接叙事，明确哪些命题可迁移、哪些缺乏实证桥接 | 分析性 — 来自跨领域对照 |
| **Tertiary** | 一个面向后续实证研究的 research agenda，包含可操作的研究问题、候选评估维度和实验设计方向 | 前瞻性 — 来自 gap 分析 |

**不再作为 headline contribution**:
- BSR/TAR → 降级为 §7 研究议程中"候选评估维度"的一个例子
- "Space Syntax 教程" → 降级为 §2 的功能性角色（服务于读者理解，不单独作为贡献）

### 1.5 与已有 Survey 的关系

| 对比对象 | 核心关切 | 本文的差异 |
|---------|---------|-----------|
| Feng et al. (2025) *Spatial Intelligence Across Scales* | LLM 的空间理解能力（按 micro/meso/macro 尺度） | 聚焦社会行为效应，而非空间能力本身 |
| Guo et al. (2024) *LLM-based Multi-Agents: A Survey* | 多智能体架构、通信机制、任务与挑战 | 聚焦空间表征及其社会后果，而非通用 multi-agent 架构 |
| Hu et al. (2024) *LLM-Based Game Agents* | 游戏 Agent 架构、能力与 genre taxonomy | 聚焦空间维度与社会行为耦合，而非游戏能力全景 |
| Gao et al. (2024) *LLM-Empowered ABM and Simulation* | LLM 驱动仿真在 cyber / physical / social / hybrid 场景中的总体版图 | 聚焦 agent-accessible spatial representation，而非仿真应用全景 |
| Mou et al. (2024) *Social Simulation Driven by LLM-based Agents* | 从 individual / scenario / society 的社会模拟分层 | 聚焦空间如何调制社会模拟，而非社会模拟的一般分类 |
| Feng et al. (2024) *Social Agents in Game-Theoretic Scenarios* | 社会智能体在博弈场景中的 agent design 与 evaluation protocol | 聚焦开放空间环境中的社会行为，而非博弈框架下的社会推理 |
| Embodied AI / VLN / VLA surveys (Gu 2022; Zhang 2024; Ma 2024) | 导航、具身规划与 action interface | 聚焦社会行为，而非导航与任务完成 |
| Spatial reasoning benchmarks (Li 2024, Yamada 2024) | LLM 空间推理测试 | 聚焦长时程社会模拟，而非单次推理 |

互补关系声明（写入 §1）：本文与 Feng et al. (2025) 互补——Feng 回答"LLM 能否理解空间"（能力），本文问"如果能，这对社会行为意味着什么"（效应与议程）。与 Guo / Hu / Gao / Mou 等综述相比，本文也不试图覆盖 LLM agent 或 social simulation 的整体技术版图，而是将问题收缩到 **agent 可访问的空间表征如何连接到社会行为生成** 这一交叉空白。

---

## 二、Review Protocol

### 2.1 方法论框架

采用 PRISMA-ScR (Preferred Reporting Items for Systematic Reviews and Meta-Analyses, extension for Scoping Reviews) 框架，适用于跨学科、新兴领域的文献映射。

### 2.2 Corpus 分层

三类文献在本文中承担不同的证据角色，必须在方法层面显式区分：

| 层级 | 名称 | 定义 | 证据角色 | 编码方式 |
|------|------|------|---------|---------|
| **Core** | LLM multi-agent systems | 包含可识别空间环境且涉及社会行为的 LLM 多智能体系统 | Evidence map 的主编码对象 | 结构化 evidence table（全字段） |
| **Adjacent** | Spatial reasoning & spatially-aware agents | LLM 空间推理 benchmark、单 Agent 空间导航系统 | 提供 LLM 空间能力的可行性边界 | Supplementary table（能力维度编码） |
| **Foundational** | Space Syntax theory & empirical findings | Space Syntax 理论、物理空间实证研究、经典 ABM | 提供理论框架和可迁移命题 | Narrative synthesis（不做 evidence table 主编码） |

**关键规则**：正文中引用 Foundational corpus 的结论时，必须标注"来自物理空间实证"，不可让读者误解为对 LLM multi-agent 社会行为的直接证据。

### 2.3 检索策略

**数据库**:
- Semantic Scholar API（主检索）
- Google Scholar（补充）
- ACL Anthology（NLP 专项）
- arXiv cs.AI / cs.CL / cs.MA（预印本）
- Environment and Planning B / Journal of Space Syntax（Space Syntax 专项）

**检索字符串族**:

| 族 | 检索字符串 | 目标 corpus |
|----|----------|------------|
| A: Space Syntax + AI | `"space syntax" AND ("agent" OR "LLM" OR "language model" OR "simulation")` | Core / Foundational |
| B: Spatial repr + Agent | `"spatial representation" AND "multi-agent" AND ("social" OR "behavior")` | Core |
| C: LLM spatial reasoning | `"spatial reasoning" AND ("large language model" OR "LLM" OR "GPT")` | Adjacent |
| D: LLM social simulation | `("generative agents" OR "LLM agent" OR "language agent") AND ("social simulation" OR "emergent behavior" OR "multi-agent" OR "sandbox" OR "virtual world" OR "NPC" OR "interactive simulacra" OR "social agent")` | Core |
| E: Spatial cognition + computation | `"spatial configuration" AND ("social behavior" OR "movement" OR "interaction")` | Foundational |

**时间范围**:
- Space Syntax 理论：1984-2026（经典理论无时间限制）
- LLM Agent 文献：2022-2026（GPT-3.5 后时代）
- 空间推理 benchmarks：2020-2026

### 2.4 纳入与排除标准

| 维度 | 纳入 | 排除 |
|------|------|------|
| **Agent 类型** | 文本驱动 LLM agent（含 VLM）；经典 ABM（仅作 Foundational 对照） | 纯机器人控制；纯强化学习 agent（无语言交互） |
| **空间维度** | 系统中存在可识别的空间环境（虚拟/文本/3D） | 纯任务空间（如代码协作、辩论场景） |
| **行为维度** | 涉及社会行为（对话、合作、冲突、移动选择） | 仅涉及导航到达率或路径效率（除非作为 Adjacent corpus） |
| **文献类型** | 期刊论文、会议论文、arXiv 预印本 | 博客、新闻报道、课程作业 |
| **语言** | 英文、中文 | 其他语言 |

**典型排除原因类别**（用于 PRISMA-ScR 流程图）：
- E1: 无空间环境（纯任务/对话场景）
- E2: 无社会行为（纯导航/路径规划）
- E3: 非 LLM agent（传统 ABM 超出 Foundational 范围）
- E4: 重复报告（同一系统的次要论文，已被主论文覆盖）
- E5: 不可获取全文

### 2.5 筛选流程

```
检索结果（预计 300-500 篇）
    ↓ 标题+摘要筛选（纳入/排除标准 + corpus 分层标签）
预筛选集（预计 80-120 篇）
    ↓ 全文快速扫描（10 min/篇）
    ↓ 标注排除原因类别（E1-E5）
编码集
  ├── Core corpus（预计 25-40 个系统）→ 结构化主编码
  ├── Adjacent corpus（预计 10-15 篇）→ 补充编码
  └── Foundational corpus（预计 10-15 篇）→ 叙事综合
正文引用集（预计 30-50 篇核心 + 20-30 补充）
```

### 2.6 分析单位

**Bibliographic screening** 以 **paper** 为单位。

**Evidence map** 以 **system / environment configuration** 为单位：

- 一个系统 = 一种独特的 Agent 架构 + 环境设计组合
- 一篇论文可报告多个系统或多种环境配置 → 分别编码
- 同一系统家族的多篇论文（如 Generative Agents → AGA → 后续扩展） → 合并为一个 system family，按最新版编码，注明版本演变

Evidence table 中设置 `system_family` 字段，防止同家族系统被误计为独立证据点。

### 2.7 编码方案

每个纳入系统（Core corpus）按以下维度编码：

**基本信息**

| 编码维度 | 取值 |
|---------|------|
| **系统名称** | 自由文本 |
| **System family** | 自由文本（用于标记同家族系统） |
| **对应论文** | 引用列表 |
| **年份** | 2020-2026 |
| **Agent 数量** | 1 / 2-10 / 10-100 / 100+ |

**空间表征（双层编码）**

| 编码维度 | 取值 | 说明 |
|---------|------|------|
| **Environment-side representation** | text-only / 2D grid / 2.5D isometric / 3D engine / graph-based | 系统内部的环境数据结构 |
| **Agent-accessible representation** | L0-L5（见 §2.9） | Agent 实际接收到的空间输入 |
| **Representation gap note** | 自由文本 | 记录环境与 Agent 输入之间的差异 |

**关键区分**：L0-L5 仅编码 Agent 实际可访问的空间信息，不编码环境后端。一个 3D engine 环境如果只向 Agent 发送房间名称，则 environment-side = 3D engine，agent-accessible = L1。

**社会行为（分层编码）**

| 编码维度 | 取值 |
|---------|------|
| **Behavioral scale** | local action / interaction / emergent social structure |
| **Behavior type** | dialogue / cooperation / conflict / mobility / role differentiation / norm formation / other |
| **Evidence status** | observed effect / designed affordance only / hypothesized but not tested |

Scale 说明：
- `local action`: 个体决策（如移动选择、地点偏好）
- `interaction`: 双人或小组社会互动（对话、合作、冲突）
- `emergent social structure`: 宏观涌现（角色分化、社会网络、规范形成）

**空间-行为耦合 & 评估**

| 编码维度 | 取值 |
|---------|------|
| **空间-行为耦合** | none / implicit / explicit |
| **评估方法** | 人类评估 / 自动指标 / LLM-as-Judge / 混合 / 无 |
| **Space Syntax 相关构念** | 是否涉及 integration/depth/control/choice 或等价概念 |

### 2.8 编码质量控制

单人研究者的最小化质控方案：

| 步骤 | 时机 | 方法 |
|------|------|------|
| **二次复核** | 标题摘要筛选完成后 | 随机抽取 15% 的排除论文，重新判断纳入/排除；若翻转率 > 10%，全量复核 |
| **Adjudication memo** | L0-L5 编码完成后 | 挑出最模糊的 8-10 个系统，撰写每个系统的分类理由和备选分类 |
| **External audit** | Phase 1 末 | 邀请导师或合作者对 5-8 个系统的 L0-L5 编码做独立判断，记录一致率 |
| **Taxonomy 版本化** | 贯穿整个编码过程 | 每次调整 L0-L5 边界定义时，记录变更日志（原定义 → 新定义 → 触发案例） |

Adjudication memo 和 taxonomy 变更日志放入 Appendix A，供 reviewer 审查。

### 2.9 L0-L5 分类学定义（精炼版）

**分类维度**：Agent 可访问空间信息的结构显式程度（structural explicitness of agent-accessible spatial information），专指与社会行为相关的空间结构信息被编码到 Agent 实际输入中的程度。

**不是**：环境渲染保真度、Agent 是否 embodied、或技术复杂度的排序。

| 层次 | 定义 | 判定条件（针对 Agent 实际输入） | 代表系统 |
|------|------|-------------------------------|---------|
| **L0** | 无空间信息 | Agent 输入中不包含任何位置或环境描述 | MetaGPT, ChatDev |
| **L1** | 地点标签 | Agent 知道自己"在哪"（地名），但不知道空间关系 | 简单 RPG, ChatArena |
| **L2** | 语义描述 | Agent 获得位置的自然语言描述（氛围、功能），但无拓扑结构 | Generative Agents (Park 2023) |
| **L3** | 邻接 + 在场 | Agent 知道哪些位置相邻、谁在哪里，支持基于共现的交互 | LIGS, AGA |
| **L4** | 构型指标 | Agent 获得基于全局拓扑分析的结构特征（如 Integration, Depth） | **尚无系统实现 — underexplored design space** |
| **L5** | 完整几何 | Agent 实际接收 3D 坐标、视域、物理约束等完整几何信息 | 需逐系统验证（见下方说明） |

**判定规则**：
- L0-L5 不是质量排序；L5 不天然"优于" L4
- L4 被标记为 **underexplored design space**，而非已有实现的描述性分类
- **L5 防误判**：仅当 Agent 的 prompt / API 输入中实际包含几何数据时才编码为 L5。若 3D 引擎仅渲染画面供人类观看，Agent 只收文本，则按 Agent 实际接收的信息编码
- 混合型系统按其最高结构显式层级编码，但在 `representation gap note` 中注明混合情况
- 边界模糊案例进入 adjudication memo

---

## 三、论文结构

### 3.1 组织逻辑

```
问题定义 → 理论基础 → 证据映射 → 能力评估 → 社会模拟现状 → 研究议程
   §1          §2          §3          §4           §5            §6-7
```

### 3.2 目录

```
1. Introduction
   1.1 The WHERE gap in LLM agent research
   1.2 Scope and research questions
   1.3 Relation to existing surveys (multi-survey positioning table)
   1.4 Review methodology overview (corpus tiers, unit of analysis)

2. Space Syntax: A Primer for AI Researchers [硬上限 1500-2000 词]
   2.1 Core claim: configuration shapes encounter (Hillier & Hanson, 1984)
   2.2 Four key measures (Integration, Depth, Control, Choice) — definitions + one worked example
   2.3 Strongest empirical findings and their boundary conditions
   2.4 What this means for the rest of the paper (bridge paragraph)

3. How Do LLM Agent Systems Represent Space? — An Evidence Map
   3.1 Review protocol summary (corpus tiers, screening, coding; full protocol in Appendix)
   3.2 Spatial representation taxonomy: L0-L5 (agent-accessible, not environment-side)
   3.3 Evidence map: systems × agent-accessible representation × behavioral scale × evidence status
   3.4 The L4 gap: configurational representation as underexplored design space
   3.5 Environment-side vs. agent-accessible: what gets lost in translation?

4. Can LLMs Process Configurational Information?
   4.1 Spatial reasoning benchmarks (SpartQA → SpatialEval)
   4.2 Topological vs. geometric reasoning
   4.3 Statistical pattern vs. emergent understanding (world model debate)
   4.4 Existing spatially-aware LLM agents (Oh et al., 2025)
   4.5 Feasibility assessment for configurational input

5. Space in Multi-Agent Social Simulation: Current State
   5.1 From classical ABM to LLM agent societies
   5.2 Emergent social behavior in current systems
   5.3 How space currently mediates (or fails to mediate) social behavior
   5.4 Space Syntax propositions as transferable hypotheses (clearly labeled "untested")

6. Toward Evaluation of Spatially Mediated Social Behavior
   6.1 What would "spatial behavioral validity" mean?
   6.2 Candidate evaluation dimensions
   6.3 Challenges: confound separation, matched controls, effect size thresholds

7. Research Agenda
   7.1 Representation: how to textualize configuration?
   7.2 Mechanism: structural reasoning vs. linguistic association?
   7.3 Emergence: micro-level spatial bias → macro-level social structure?
   7.4 Generalization: across models, languages, and environment types
   7.5 Applications: game NPCs, urban simulation, environmental psychology

8. Conclusion

Appendix A: Full Review Protocol + Adjudication Memo + Taxonomy Change Log
Appendix B: Complete Evidence Table (Core + Adjacent)
```

### 3.3 版本演变追踪

| v2 → v3 | v3 → v4 | 驱动来源 |
|----------|---------|---------|
| 研究问题从因果命题收缩为 scoping | — (保持) | v2_r1 #1 |
| §3 L0-L5 改为 evidence map 的分析工具 | L0-L5 限定为 agent-accessible 编码 | v3_r1 #3 |
| — | 新增 corpus 三层分级 (Core/Adjacent/Foundational) | v3_r1 #1 |
| — | 分析单位从 paper 改为 system | v3_r1 #2 |
| — | 空间编码拆为 environment-side + agent-accessible | v3_r1 #3 |
| — | 社会行为编码拆为 behavioral scale + behavior type + evidence status | v3_r1 #4 |
| — | 新增编码质控方案 (二次复核 + adjudication memo + external audit) | v3_r1 #5 |
| §2 Space Syntax Primer 2500-3500 词 | 硬上限 1500-2000 词，删 Appendix C | v3_r1 #6 |
| — | D 族检索词补充 sandbox/virtual world/NPC/social agent 等 | v3_r1 #8 |
| — | 新增排除原因类别 E1-E5 | v3_r1 #9 |

---

## 四、执行计划

### Phase 0: Review Protocol 与 Evidence Matrix（Week 1-2）

在任何正文写作之前，先完成检索和编码基础设施。

#### Week 1: 精读 Anchor Papers + 建立编码框架

| # | 任务 | 产出 |
|---|------|------|
| 1.1 | 精读 Hillier & Hanson (1984)，优先 Ch.1-3, Ch.6；若难获取，用 *Space is the Machine* (1996, 免费在线) 替代 | `hillier1984_social_logic_of_space.md` (60-80 行) |
| 1.2 | 精读 Turner et al. (2001) *From Isovists to Visibility Graphs*（18 页） | `turner2001_visibility_graph.md` (60-80 行) |
| 1.3 | 精读 Oh et al. (2025) *Spatially Aware LLM Agents* | `oh2025_spatially_aware_llm.md` (60-80 行) |
| 1.4 | 设计 evidence table 模板（按 §2.7 编码方案）+ 撰写 coding manual + claim matrix | `evidence_table_template.md` + `coding_manual.md` + `claim_matrix.md` |

**Coding manual 必须包含**：
- Unit of analysis 定义（system vs paper 的判定规则）
- Corpus tiering 判定规则（Core / Adjacent / Foundational）
- L0-L5 decision tree（含边界案例处理流程）
- Behavioral scale 定义 + 示例
- Evidence status 定义 + 示例
- Ambiguous-case handling：遇到无法判定的系统时，标记进入 adjudication memo

**Claim matrix 必须包含**：
- 不同 `evidence status` 可支撑的 claim 类型
- `Core / Adjacent / Foundational` 三类 corpus 的 claim 上限
- 允许/不允许的论断措辞示例

**Week 1 自检**:
- [ ] 能用自己的话解释 Integration/Depth/Control 的图论定义
- [ ] 能解释 VGA 与 axial map 分析的关系
- [ ] 能说明 Oh et al. 的空间感知水平定义与 L0-L5 的异同
- [ ] Evidence table 模板已确定，包含全部双层空间编码 + 分层行为编码
- [ ] Coding manual 初稿已完成
- [ ] Claim matrix 初稿已完成

#### Week 2: 检索执行 + 初步编码

| # | 任务 | 产出 |
|---|------|------|
| 2.1 | 执行 5 族检索字符串，收集候选论文 | 检索结果汇总（预计 300-500 篇） |
| 2.2 | 标题+摘要筛选 | 预筛选集（预计 80-120 篇） |
| 2.3 | 精读 Hillier (1996) *Space is the Machine* Ch.1, Ch.4 + Penn & Turner (2001) | 补充 reading notes |
| 2.4 | 扩展 `spatial_theory.md` 至完整教程（含公式、直觉解释） | 扩展后的 `spatial_theory.md`（3-5 页） |

**Week 2 自检**:
- [ ] 预筛选集论文清单已确定
- [ ] `spatial_theory.md` 包含 Integration/Depth/Control/Choice/Intelligibility 的完整定义和公式
- [ ] 能手算一个简单图的 justified graph 和 Integration

---

### ★ Readiness Gate（Week 2 末）

**以下条件全部满足后，方可进入 Phase 1**：

- [ ] 3 篇 anchor paper reading notes 已完成（Hillier, Turner, Oh）
- [ ] `spatial_theory.md` 已扩展至 3+ 页
- [ ] 预筛选论文集已确定（80+ 篇），并标注 corpus 层级
- [ ] Evidence table 模板已确定（含双层空间编码 + 分层行为编码 + system family 字段）
- [ ] `coding_manual.md` 已完成（含 L0-L5 decision tree + 分析单位 + corpus 分层规则）
- [ ] `claim_matrix.md` 已完成（含 evidence status -> allowable claims 映射）
- [ ] L0-L5 分类学的判定条件已明确，并对至少 3 个已知系统做 pilot coding 验证

**若未满足**：延长 Phase 0 一周，不跳过。

---

### Phase 1: 编码与分析（Week 3-5）

#### Week 3: 全文扫描 + 编码

| # | 任务 | 产出 |
|---|------|------|
| 3.1 | 对预筛选集进行全文快速扫描（10 min/篇），按 corpus 层级分流，标注排除原因（E1-E5） | Core corpus（预计 25-40 个系统）+ Adjacent（10-15）+ Foundational（10-15） |
| 3.2 | 对 Core corpus 进行结构化编码（按 §2.7 全字段），对 Adjacent corpus 做补充编码 | 填充后的 evidence table |
| 3.3 | 精读 Feng et al. (2025) 全文 | 多 survey 定位对比表 |
| 3.4 | 对排除论文随机抽取 15% 做二次复核 | 复核记录（翻转率统计） |

#### Week 4: 分析与 Taxonomy 验证 + 质控

| # | 任务 | 产出 |
|---|------|------|
| 4.1 | 基于 evidence table 验证 L0-L5 分类学：每层是否有足够系统支撑？是否需要调整边界？ | Taxonomy coding memo + taxonomy change log |
| 4.2 | 生成 evidence map：按"agent-accessible repr × behavioral scale × evidence status"交叉制表 | Evidence map 可视化草稿 |
| 4.3 | 识别 L4 gap 的具体证据：有多少系统在 L3 以下？有多少涉及构型？ | L4 gap analysis 文档 |
| 4.4 | 整理 Space Syntax 命题的可迁移性评估 | 命题迁移表（标注 evidence status） |
| 4.5 | 撰写 adjudication memo（最模糊的 8-10 个系统） | `adjudication_memo.md` |
| 4.6 | 邀请导师/合作者对 5-8 个系统做 independent L0-L5 判断 | External audit 记录 |

#### Week 5: 竞争排查 + 补充检索

| # | 任务 | 产出 |
|---|------|------|
| 5.1 | 排查 2025-2026 是否出现竞争性 survey | 竞争分析结论 |
| 5.2 | 根据编码中发现的引用链，补充遗漏论文 | 更新后的 evidence table |
| 5.3 | 更新 `reference_index.md` | 更新后的参考文献库 |

**Phase 1 完成标准**:
- [ ] Core corpus evidence table 覆盖 25+ 个系统
- [ ] L0-L5 taxonomy 经过 evidence table 验证，adjudication memo 已完成
- [ ] External audit 完成（5+ 系统，记录一致率）
- [ ] Evidence map 草稿完成（agent-accessible repr × behavioral scale × evidence status）
- [ ] 确认无竞争性 survey 占据本文定位

---

### Phase 2: 论文写作（Week 6-9）

#### 写作依赖关系

```
§2 Space Syntax Primer ──→ §3 Evidence Map (含 L0-L5)
                                     ↓
§4 LLM Spatial Reasoning ←── 独立，可并行
                                     ↓
§5 Space in Social Sim ────→ §6 Evaluation Dimensions
                                     ↓
                              §7 Research Agenda
                                     ↓
                    §1 Introduction + §8 Conclusion（最后写）
```

#### 逐周计划

**Week 6: §2 + §5**

| Section | 字数 | 素材 | 要点 |
|---------|------|------|------|
| §2 Space Syntax Primer | **1500-2000（硬上限）** | `spatial_theory.md` + Hillier/Turner notes | 只保留后文必需的最小理论底座：核心主张 + 4 个指标定义 + 一个 worked example + 最强实证发现 + boundary conditions。持续提醒：Space Syntax 在本文中是解释变量来源，不是独立综述 |
| §5 Space in Social Sim | 2000-2500 | 5 篇完整 reading notes + evidence table | §5.4 关键：将 Space Syntax 命题翻译为可检验假设，明确标注"尚未检验"；引用 Foundational corpus 时标注"物理空间实证" |

**Week 7: §3 + §4**

| Section | 字数 | 素材 | 要点 |
|---------|------|------|------|
| §3 Evidence Map | 3000-3500 | Evidence table + L0-L5 taxonomy + coding memo + adjudication memo | **本文核心章节**。以 evidence map 大表为中心；§3.2 强调 L0-L5 是 agent-accessible 编码；§3.5 新增 environment-side vs agent-accessible 差异讨论；仅编码 Core corpus |
| §4 LLM Spatial Reasoning | 1500-2000 | `spatial_agent_survey.md` §3 + `reference_index.md` Cat.3 | 聚焦可行性评估：现有证据是否支持 LLM 处理构型输入？结论应谨慎 |

**Week 8: §6 + §7**

| Section | 字数 | 素材 | 要点 |
|---------|------|------|------|
| §6 Evaluation Dimensions | 1500-2000 | evidence table 中的评估方法编码 + `plan_v9.md` 中的评估设计（去除内部命名） | BSR/TAR 仅作为候选 operationalization 之一，不是章节中心；重点是"评估空间-行为耦合需要什么维度" |
| §7 Research Agenda | 1500-2000 | §2-§6 的 gaps 综合 | 5 个开放问题，每个给出具体可操作的研究方向 |

**Week 9: §1 + §8 + 图表 + Appendix**

| 任务 | 内容 |
|------|------|
| §1 Introduction | WHERE gap + multi-survey 定位表 + review methodology 概述 + 组织逻辑 |
| §8 Conclusion | 三个主要发现 + 局限 + 展望 |
| 图表 | 见下方清单 |
| Appendix A | 完整 review protocol + adjudication memo + taxonomy change log |
| Appendix B | 完整 evidence table (Core + Adjacent) |

#### 关键图表

| # | 图表 | 类型 | 章节 | 必要性 |
|---|------|------|------|--------|
| 1 | **Evidence map 大表** | 系统×agent-accessible repr×behavioral scale×evidence status | §3 | 必须 |
| 2 | **Corpus 分层示意图** | 三层嵌套：Core → Adjacent → Foundational | §1 | 必须 |
| 3 | **L0-L5 空间表征分类学** | 带判定条件的层次图，标注 agent-accessible 视角 | §3 | 必须 |
| 4 | **Multi-survey 定位矩阵** | 对比表 | §1 | 必须 |
| 5 | **PRISMA-ScR 筛选流程图** | 含排除原因类别 E1-E5 | §1/Appendix | 必须 |
| 6 | **Environment-side vs Agent-accessible 对照** | 示例对比（2-3 个系统） | §3 | 必须 |
| 7 | **Space Syntax 核心指标 worked example** | 一个 5 节点图的 Integration 计算 | §2 | 推荐 |
| 8 | **Space Syntax 命题迁移表** | 映射表，标注 evidence status | §5 | 推荐 |

---

### Phase 3: 修订与投稿（Week 10-14）

| 周次 | 任务 |
|------|------|
| Week 10 | 全文通读，检查论证一致性；确认所有 claim 有 evidence table 与 claim matrix 支撑 |
| Week 11 | 内部审阅（导师/合作者反馈） |
| Week 12-13 | 修订 |
| Week 14 | 格式化 + 投稿 |

---

## 五、投稿策略（分化版）

短版和长版是**两个不同的产品**，不是同一篇文章的长度伸缩。

### 5.1 产品 A: Short Scoping Paper

| 维度 | 设计 |
|------|------|
| **首选 venue** | **AAMAS-27 Blue Sky**（最匹配：multi-agent + vision paper 气质） |
| **备选 venue** | IJCAI-27 Workshop（若 AAMAS 截止日期已过） |
| **长度** | 4-6 页 |
| **核心内容** | WHERE gap + L0-L5 taxonomy（agent-accessible 视角）+ L4 gap 的证据 + 精炼版 agenda |
| **不包含** | 完整 Space Syntax 教程、完整 evidence table、评估方法论讨论、coding manual |
| **语气** | Sharp vision + provocative agenda |
| **完成时间** | Phase 2 结束后即可提取 |

**注**：开始写短版前必须选定一个主 venue 并锁定文风，不在多个 venue 之间摇摆。

### 5.2 产品 B: Full Scoping Review

| 维度 | 设计 |
|------|------|
| **目标 venue** | AI Magazine (AAAI) / Environment and Planning B / Frontiers in AI |
| **长度** | 20-30 页 |
| **核心内容** | 完整 PRISMA-ScR protocol + Space Syntax primer + evidence map + taxonomy + agenda |
| **语气** | Systematic, evidence-backed, cross-disciplinary bridge |
| **完成时间** | Phase 3 结束后 |

**不建议直接瞄准 ACM Computing Surveys**：当前 corpus 规模和领域成熟度不足以支撑其系统性要求。

### 5.3 截止日期待查

| Venue | Track | 预计截止日期 |
|-------|-------|-------------|
| AAMAS-27 | Blue Sky | 2026 秋? |
| IJCAI-27 | Workshop | 2027 年初? |
| AI Magazine | Rolling | 随时 |
| Environment and Planning B | Rolling | 随时 |

---

## 六、风险与应对

| 风险 | 应对 |
|------|------|
| Hillier 1984 原著太长/难获取 | 用 *Space is the Machine* (1996, spaceisthemachine.com) + *Space Syntax Methodology* (2014) 教材替代 |
| 检索结果过少（交叉领域文献稀疏） | 扩大 D 族检索范围；接受 corpus 小的事实，在论文中诚实报告，这本身就是 gap 的证据 |
| L0-L5 分类学经 evidence table 验证后不成立 | 调整层级定义或改为二维框架；taxonomy 应从数据中生长，不预设 |
| §2 Space Syntax Primer 写不好 | 找建筑学背景的人审阅；参考其他跨学科 survey 的理论引入写法 |
| 时间拖延 | Phase 0 的 readiness gate 是硬门槛，不跳过；§5 素材最充足，若卡壳可先写 §5 建立信心 |

---

## 七、项目备忘（不进入论文正文）

Survey 完成后，所建立的领域知识将用于重新评估实证计划 v9，预期方向：

- 根据 evidence map 判断哪些实验条件必要
- 根据 Space Syntax 命题迁移表调整假设优先级
- 根据 LLM 空间推理可行性评估调整效应量预期
- 将 v9 简化为更聚焦的 v10

此部分仅作项目管理备忘，不出现在论文任何位置。

---

## 八、立即开始

**本周任务**：Phase 0, Week 1

1. 确认 Hillier 1984 获取方式：检查 `assets/papers/pdfs/02_Space_Syntax/`；若无 PDF，下载 *Space is the Machine* (spaceisthemachine.com)
2. 精读 Hillier Ch.1-3 + Ch.6，填写 `hillier1984_social_logic_of_space.md`
3. 精读 Turner et al. (2001)，填写 `turner2001_visibility_graph.md`
4. 精读 Oh et al. (2025)，填写 `oh2025_spatially_aware_llm.md`
5. 设计 evidence table 模板（含双层空间编码 + 分层行为编码 + system family）
6. 撰写 `coding_manual.md` 初稿
7. 撰写 `claim_matrix.md` 初稿

**本周结束时的自检**：
- [ ] 能用自己的话解释"构型"与"组合"的区别
- [ ] 能手算一个 5 节点图的 Integration
- [ ] 能解释 VGA 与 axial map 的关系
- [ ] 能说明 Oh et al. 的空间感知定义与 L0-L5 的异同
- [ ] Evidence table 模板已确定（含全部新增字段）
- [ ] Coding manual 包含 L0-L5 decision tree
- [ ] Claim matrix 明确区分 observed effect / designed affordance only / hypothesized but not tested 的 claim 上限
- [ ] 用 coding manual 对 3 个已知系统（Generative Agents, Project Sid, SARAH）做 pilot coding，验证可操作性
