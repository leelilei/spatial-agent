# Spatial Agent Survey 研究计划

## 写还是不写？—— 差异化分析与行动方案

> 日期: 2026-03-22
> 背景: 发现 Feng et al. (2025) 已发表 "A Survey of Large Language Model-Powered Spatial Intelligence Across Scales"
> 目的: 评估是否仍值得写一份独立 survey，以及如何切入

---

## 一、已有 Survey 全景

### 1.1 主要竞争者：Feng et al. (2025)

- **标题**: A Survey of Large Language Model-Powered Spatial Intelligence Across Scales: Advances in Embodied Agents, Smart Cities, and Earth Science
- **发表**: arXiv:2504.09848, 2025年4月
- **作者**: Jie Feng 等 18 人
- **组织方式**: 按**尺度**划分
  - Micro: Embodied Agent（导航、感知）
  - Meso: Smart City（城市规划、交通）
  - Macro: Earth Science（遥感、气候）
- **核心问题**: "LLM 如何理解和推理空间？"
- **理论锚点**: 无——工程驱动分类
- **社会行为**: 未涉及
- **Space Syntax**: 未涉及

### 1.2 其他相关 Survey

| Survey | 年份/会议 | 关注点 | 与你的重叠 |
|--------|----------|--------|-----------|
| Zha et al. "How to Enable LLM with 3D Capacity?" | IJCAI 2025 | 3D 空间理解（点云、视觉） | 低 |
| Plaat et al. "Agentic Large Language Models" | JAIR 2025 | 通用 Agent 能力（推理、行动、交互） | 低 |
| "LLM-based Multi-agents: Progress and Challenges" | IJCAI 2024 | 多 Agent 协作机制 | 中（多 Agent），但无空间维度 |
| "LLM-based Autonomous Agents" | Frontiers of CS | 自主 Agent 系统 | 低 |

### 1.3 关键发现：没有人占据你的位置

**所有已有 survey 都不覆盖以下交叉地带：**

- Space Syntax 构型理论 × LLM Agent
- 空间对社会行为的调制效应
- 多 Agent 社会模拟中的空间维度
- 空间行为可信度（Spatial Believability）

---

## 二、结论：值得写

### 2.1 Feng et al. vs 你的定位对比

| 维度 | Feng et al. (2025) | 你的独特领地 |
|------|-------------------|-------------|
| **组织原则** | 按尺度（micro/meso/macro） | 按因果链（构型 → 行为） |
| **核心问题** | "LLM 如何理解空间？" | "空间构型是否塑造 Agent 社会行为？" |
| **理论锚点** | 无 | **Space Syntax**（Hillier 1984） |
| **Agent 模式** | 单 Agent 导航/感知 | **多 Agent 社会模拟** |
| **空间表征** | 视觉/几何/坐标 | **拓扑-构型**（Integration, Depth, Control） |
| **社会行为** | 未涉及 | 核心——社交性、私密性、守门行为 |
| **评估方法** | 任务性能（导航成功率） | **BSR/TAR 双指标 + 行为可信度** |
| **学科桥梁** | CS/AI 内部 | **建筑理论 × AI Agent** |

### 2.2 互补关系（论文中需显式声明）

```
Feng et al. 回答：LLM 如何感知和推理空间？（能力问题）
本 survey 回答：空间构型如何塑造 Agent 的社会行为？（效应问题）

互补，不竞争。
```

---

## 三、最锐利的切入角度

### 3.1 不要叫 "Spatial Agent Survey"

太宽泛，与 Feng et al. 正面碰撞。

### 3.2 推荐定位

**核心转换**：从 "空间智能" 转向 "空间构型对社会行为的塑造"

### 3.3 候选标题

**首选：**
> **From Navigation to Habitation: A Survey on How Spatial Configuration Shapes LLM Agent Social Behavior**

**备选：**
> **Space Shapes Society: Bridging Space Syntax Theory and LLM Multi-Agent Social Simulation**

> **Where You Are Shapes Who You Become: A Survey on Spatially-Configured Agent Societies**

### 3.4 一句话论点

> 尽管 Space Syntax 在物理空间中积累了 40 年实证证据证明空间构型塑造人类社会行为，尽管 LLM 多智能体社会模拟已发展 3 年，**这两个知识体系从未被系统连接**。本 survey 映射这一空白，识别所需的理论与方法论桥梁，并规划"空间构型化智能体社会"的研究议程。

---

## 四、推荐结构

### 4.1 组织逻辑：因果链（而非尺度）

```
Theory → Representation → Capability → Application → Evaluation → Future
```

### 4.2 目录

```
1. Introduction
   1.1 The WHERE Gap: WHO 和 WHAT 已建模，WHERE 仍缺失
   1.2 为什么是"构型"而非"位置"
   1.3 与已有 Survey 的关系（显式对比表 vs Feng et al.）
   1.4 本文范围与组织

2. Space Syntax: 空间与社会的构型理论
   2.1 起源与核心概念（Integration, Depth, Control, Choice）
   2.2 物理空间中的关键实证发现
       - 自然移动模型 (Hillier et al., 1993)
       - 隐私梯度 (Hanson, 1998)
       - 控制与监视 (Hillier & Shu, 2000)
   2.3 图论形式化
   2.4 计算工具生态（depthmapX, momepy, QGIS SST）
   2.5 批评与局限
   → 目的：让 AI 读者理解 Space Syntax

3. LLM Agent 系统中的空间表征
   3.1 空间表征层次分类学（L0-L5）★ 原创贡献
       L0: 无空间（MetaGPT, ChatDev）
       L1: 地点名（简单 RPG）
       L2: 语义描述（Generative Agents）
       L3: 邻接+在场
       L4: 构型指标 ← 本研究关注的空白层
       L5: 完整 3D（Habitat, AI2-THOR）
   3.2 现有系统空间处理方式（系统化对比表）
   3.3 构型空白：缺失了什么
   3.4 空间构型的文本化策略与挑战
   → 目的：映射表征版图，定位 L4 空白

4. LLM 能处理构型信息吗？
   4.1 空间推理基准（SpartQA, StepGame, SpatialBench...）
   4.2 拓扑推理 vs 几何推理
   4.3 统计模式 vs 涌现理解（世界模型辩论）
   4.4 对构型空间输入的可行性含义
   → 目的：建立可行性基础

5. 多智能体社会模拟：空间作为社会基础设施
   5.1 从经典 ABM 到 LLM Agent 社会
       Schelling → Sugarscape → Generative Agents → Project Sid
   5.2 LLM 系统中的涌现社会行为
   5.3 空间在现有模拟中的角色（系统化对比）
   5.4 Space Syntax 预测了什么、但尚未被检验
       - H1: Integration → 社交频率
       - H2: Depth → 私密行为
       - H3: Control → 守门行为
   → 目的：展示应用领域与未验证预测

6. 评估空间驱动的社会行为
   6.1 行为可信度 vs 空间行为可信度（新维度）
   6.2 BSR/TAR 双指标框架 ★ 方法论贡献
   6.3 实验设计挑战（匹配条件、混淆分离）
   6.4 LLM-as-Judge 的应用与偏见
   6.5 编码信度问题
   → 目的：提供方法论工具包

7. 研究议程：开放问题与机会
   7.1 表征问题（如何最佳地文本化构型？）
   7.2 机制问题（空间启动 vs 持续引导？）
   7.3 涌现问题（微观空间偏移 → 宏观社会结构？）
   7.4 跨模型泛化性
   7.5 应用方向（游戏设计、城市模拟、环境心理学）
   → 目的：为 SpatialAgent 实证论文铺路

8. Conclusion
```

---

## 五、Survey 的 5 个独特价值

| # | 独特价值 | Feng et al. 是否覆盖 |
|---|---------|:-------------------:|
| 1 | **形式化空间理论**（Space Syntax）作为组织框架 | 否 |
| 2 | **社会行为维度**（社交/私密/守门），而非导航/感知 | 否 |
| 3 | **L0-L5 空间表征分类学**，显式识别 L4 构型空白 | 否 |
| 4 | **BSR/TAR + MIC 方法论贡献** | 否 |
| 5 | **跨学科桥梁**：首次连接建筑理论与 LLM Agent | 否 |

---

## 六、投稿策略

### 6.1 推荐：双版本策略

| 版本 | 目标 | 长度 | 优先级 |
|------|------|------|:------:|
| **短版** | AAMAS-27 Blue Sky / IJCAI-27 Survey Track | 6-8 页 | 先投 |
| **长版** | ACM Computing Surveys (CSUR) | 30-40 页 | 后投 |

### 6.2 其他可选目标

- **AI Magazine** (AAAI) — 可达性强，适合 position piece
- **Environment and Planning B** — Space Syntax 传统阵地，跨学科影响
- **CHI 2027 alt.chi** — 强调游戏设计/空间可信度角度

### 6.3 战略价值

Survey 为你的 SpatialAgent 实证论文（v7）铺路：
- 让审稿人认为你的工作属于一个被识别的研究方向
- 而非一个孤立的、缺乏上下文的实验

---

## 七、现有素材盘点

| 素材 | 文件 | 完成度 | 利用方式 |
|------|------|:------:|---------|
| Survey 初稿 | `../surveys/survey_spatial_agent.md` | ~60% | 核心骨架，需重组结构 |
| 参考文献库 | `../references/paperrefence.md` | 60+ 篇 | 参考文献骨架 |
| Reading notes | `assets/papers/reading_notes/` (12篇) | 完整 | Section 2,3,5 素材 |
| Space Syntax 理论 | `../background/spatial_theory.md` | 完整 | Section 2 素材 |
| v7 研究计划 | `plan_v7.md` | 完整 | Section 5,6 素材（H1-H3, BSR/TAR, 条件矩阵） |

---

## 八、工作量与时间线

| 阶段 | 工作内容 | 时间 |
|------|---------|:----:|
| **1. 结构重组** | 按新目录重组 `../surveys/survey_spatial_agent.md`，补 Space Syntax 深度 | 1 周 |
| **2. 文献补缺** | 检查 2025-2026 新论文，补 Feng et al. 对比分析 | 1 周 |
| **3. 写作+图表** | 对比表、L0-L5 分类图、因果链图 | 1 周 |
| **4. 审阅修订** | 导师/合作者反馈 | 1 周 |
| **总计** | | **4 周** |

> 短版（AAMAS/IJCAI）可在前 2 周内完成。

---

## 九、风险与应对

| 风险 | 可能性 | 应对 |
|------|:------:|------|
| 领域快速发展，出现竞争 survey | 中 | 先投短版抢占 niche |
| AI 审稿人不认 Space Syntax 的相关性 | 中 | 论文中显式论证"为什么 AI 研究者应关心构型理论" |
| Space Syntax 审稿人不认 LLM 的有效性 | 中 | 引用"三跳跃"框架，诚实承认局限 |
| 与主论文时间冲突 | 低 | Survey 作为 Related Work 的扩展版，写一份用两次 |

---

## 十、最终建议

### 写。理由：

1. **空白真实存在** — 没有任何已有 survey 覆盖"空间构型 → Agent 社会行为"
2. **素材已有 60%** — 不需从零开始
3. **战略价值** — 为 SpatialAgent 实证论文铺路
4. **成本低** — 4 周工作量，无 API 费用
5. **切入角度锐利** — "Space Syntax × LLM Agent Society" 无人占据

### 但要注意：

- **不要与 Feng et al. 竞争** — 在 Introduction 中显式致敬，说明互补关系
- **不要贪大** — 明确排除导航/遥感/城市计算（那是 Feng et al. 的领地）
- **先出短版** — 快速获得可见度，锁定研究方向的优先权

---

## 十一、下一步行动清单

- [ ] 确定投稿目标（短版 + 长版 or 只做一版？）
- [ ] 基于 Section 4.2 目录重组 `../surveys/survey_spatial_agent.md`
- [ ] 精读 Feng et al. 全文，撰写详细对比分析
- [ ] 完成 L0-L5 分类学的系统化对比表（覆盖所有已知 LLM Agent 系统）
- [ ] 绘制关键图表（因果链图、表征分类图、文献版图定位图）
- [ ] 撰写 Section 2 (Space Syntax for AI readers) 的深度内容
- [ ] 内部审阅，收集反馈
