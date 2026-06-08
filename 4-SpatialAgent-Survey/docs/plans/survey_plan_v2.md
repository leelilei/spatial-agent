# Survey 研究计划

## From Navigation to Habitation: How Spatial Configuration Shapes LLM Agent Social Behavior

> 日期: 2026-04-11  
> 作者: Li  
> 时间线: 10-12 周（Phase 1 知识构建 4 周 + Phase 2 写作 4 周 + Phase 3 修订投稿 2-4 周）

---

## 一、论文定位

### 1.1 核心论点

> Space Syntax 在物理空间中积累了 40 年实证证据证明空间构型塑造人类社会行为；LLM 多智能体社会模拟已发展 3 年——**这两个知识体系从未被系统连接**。本 survey 映射这一空白，建立"空间构型化智能体社会"的概念框架与研究议程。

### 1.2 核心问题

**空间构型如何塑造 LLM Agent 的社会行为？**

不是：LLM 如何理解空间（那是 Feng et al. 2025 的问题）。

### 1.3 与最接近的已有 Survey 的互补

| 维度 | Feng et al. (2025) | 本 Survey |
|------|-------------------|-----------|
| 核心问题 | LLM 如何理解空间？（能力） | 空间构型如何塑造 Agent 社会行为？（效应） |
| 组织原则 | 按尺度（micro/meso/macro） | 按因果链（构型 → 表征 → 行为） |
| 理论锚点 | 无 | Space Syntax (Hillier 1984) |
| Agent 模式 | 单 Agent 导航/感知 | 多 Agent 社会模拟 |
| 社会行为 | 未涉及 | 核心 |

### 1.4 五个独特贡献

1. **L0-L5 空间表征分类学** — 首次系统化 LLM Agent 系统的空间表征层次
2. **Space Syntax 的 AI 化教程** — 让 AI 研究者理解构型理论的核心洞见
3. **构型-行为因果链框架** — 从理论到表征到能力到应用到评估的完整映射
4. **BSR/TAR 评估方法论** — 区分"行为是否响应空间"与"响应是否沿理论方向"
5. **跨学科研究议程** — 建筑理论 × AI Agent 的首个系统性路线图

### 1.5 投稿目标

| 版本 | 目标 | 长度 | 优先级 |
|------|------|------|:------:|
| **短版** | AAMAS-27 Blue Sky / IJCAI-27 Survey Track | 6-8 页 | 先投 |
| **长版** | ACM Computing Surveys / AI Magazine / Environment and Planning B | 25-35 页 | 后投 |

截止日期待确认。若短版会议不合适，直接写长版投 journal。

---

## 二、论文结构

### 2.1 组织逻辑

```
Theory → Representation → Capability → Application → Evaluation → Agenda
  §2         §3              §4            §5            §6          §7
```

### 2.2 完整目录

```
1. Introduction
   1.1 The WHERE Gap: WHO 和 WHAT 已建模，WHERE 仍缺失
   1.2 为什么是"构型"而非"位置"
   1.3 与已有 Survey 的定位（vs Feng et al. 对比表）
   1.4 本文范围与组织

2. Space Syntax: 空间构型的社会理论
   2.1 起源与核心主张 (Hillier & Hanson, 1984)
   2.2 核心构型指标 (Integration, Depth, Control, Choice, Intelligibility)
   2.3 关键实证发现
       - 自然移动模型 (Hillier et al., 1993)
       - 隐私梯度 (Hanson, 1998)
       - 控制与监视 (Hillier & Shu, 2000)
   2.4 可见性图分析 (Turner et al., 2001)
   2.5 图论形式化与计算工具
   2.6 批评与局限
   → 目标：让 AI 读者理解 Space Syntax 的核心洞见

3. LLM Agent 系统中的空间表征
   3.1 空间表征层次分类学 (L0-L5) ★ 原创
       L0: 无空间 (MetaGPT, ChatDev)
       L1: 地点名 (简单 RPG)
       L2: 语义描述 (Generative Agents)
       L3: 邻接 + 在场
       L4: 构型指标 ← 本 survey 识别的空白层
       L5: 完整 3D (Habitat, AI2-THOR)
   3.2 现有系统空间处理方式（系统化对比表）
   3.3 从 L2 到 L4 的构型空白
   3.4 文本化策略与挑战
   → 目标：定位 L4 空白，说明为什么需要构型表征

4. LLM 能处理构型信息吗？
   4.1 空间推理基准 (SpartQA, StepGame, SpatialBench, SpatialEval)
   4.2 拓扑推理 vs 几何推理：LLM 的优劣势
   4.3 统计模式复现 vs 涌现理解（世界模型辩论）
   4.4 Spatially-Aware LLM Agent 的已有探索 (Oh et al., 2025; SARAH)
   4.5 对构型输入可行性的评估
   → 目标：回答"LLM 能否处理 Space Syntax 指标"

5. 多智能体社会模拟中的空间维度
   5.1 从经典 ABM 到 LLM Agent 社会
       Schelling → Sugarscape → Generative Agents → Project Sid
   5.2 LLM 多 Agent 系统中的涌现社会行为
       - 社会契约涌现 (Dai et al., 2024)
       - 角色分化与文化传播 (Altera, 2024)
       - 叙事涌现 (Jeong et al., 2025)
   5.3 空间在现有系统中的角色（系统化对比）
   5.4 Space Syntax 预测了什么、尚未在 Agent 中检验
       - H1: Integration → 社交频率
       - H2: Depth → 私密行为
       - H3: Control → 守门行为
   → 目标：展示应用场景与未验证的理论预测

6. 评估空间驱动的社会行为
   6.1 行为可信度 vs 空间行为可信度（新维度）
   6.2 BSR/TAR 双指标框架 ★ 方法论贡献
   6.3 实验设计挑战（匹配条件、混淆分离）
   6.4 LLM-as-Judge 的空间行为评估
   6.5 人类评估 Protocol
   → 目标：提供方法论工具包

7. 研究议程：开放问题与机会
   7.1 表征问题（如何最佳地文本化构型？）
   7.2 机制问题（结构推理 vs 语言关联？）
   7.3 涌现问题（微观空间偏移 → 宏观社会结构？）
   7.4 跨模型与跨语言泛化性
   7.5 应用方向（游戏 NPC、城市模拟、环境心理学）

8. Conclusion
```

---

## 三、素材清单与缺口

### 3.1 各 Section 的素材来源与缺口

| Section | 现有素材 | 缺口 | 对应行动 |
|---------|---------|------|---------|
| §1 Introduction | `spatial_agent_survey.md` §1（WHERE gap 论证完整） | Feng et al. 对比表 | Week 3: 精读 Feng et al. |
| §2 Space Syntax | `spatial_theory.md`（1.5KB 骨架）; `spatial_agent_survey.md` §4; `reference_index.md` Cat.2（10篇） | **Hillier 1984 未精读**; **Turner 2001 未精读**; VGA 详述缺失 | Week 1: 精读 Hillier + Turner |
| §3 空间表征 | `spatial_agent_survey.md` §2, §5; park2023/hu2024/yu2024 reading notes | L0-L5 分类学未系统化; **Oh 2025 未精读** | Week 1: 精读 Oh; Week 4: 系统化 L0-L5 |
| §4 LLM 空间推理 | `spatial_agent_survey.md` §3（基准+两种观点）; `reference_index.md` Cat.3（5篇） | 需更新 2025-2026 新基准 | Week 3: 文献补缺 |
| §5 多 Agent 模拟 | park2023/sid/dai/jeong/zhu reading notes（均完整）; `spatial_agent_survey.md` §6 | H1-H3 映射到文献需整理 | Week 5: 直接写作 |
| §6 评估方法 | `plan_v9.md` §7 (BSR/TAR 详细设计); zhu2025 reading note | 需形式化为独立方法论 | Week 7: 写作 |
| §7 研究议程 | `plan_v9.md` 各章节可提炼; 各 reading notes 中的 future work | 需综合整理 | Week 7: 写作 |

### 3.2 Reading Notes 状态

**完整（7 篇，可直接使用）**:
- `park2023_generative_agents.md` → §3, §5
- `assets/survey_paper/reading_notes/hu2024_llm_game_agents_survey.md` → §3, §4
- `yu2024_affordable_generative_agents.md` → §5, §6
- `altera2024_project_sid.md` → §5
- `dai2024_artificial_leviathan.md` → §5
- `jeong2025_ligs_emergent_narrative.md` → §5
- `zhu2025_multiagentbench.md` → §5, §6

**空模板（3 篇，必须在 Week 1-2 完成）**:
- `hillier1984_social_logic_of_space.md` → §2 ← **最高优先**
- `turner2001_visibility_graph.md` → §2 ← **最高优先**
- `oh2025_spatially_aware_llm.md` → §3, §4 ← **最高优先**

### 3.3 关键参考文件路径

| 文件 | 路径 | 用途 |
|------|------|------|
| Survey 初稿 | `docs/background/spatial_agent_survey.md` | §1-§5 的骨架，需按新目录重组 |
| Space Syntax 理论 | `docs/background/spatial_theory.md` | §2 的起点，需大幅扩展 |
| 参考文献库 | `docs/project/reference_index.md` | 全部 60+ 篇论文索引 |
| 实验计划 v9 | `docs/plans/plan_v9.md` | §6 BSR/TAR 方法论、§5 H1-H3 假设来源 |
| Reading notes | `assets/papers/reading_notes/*.md` | 各 section 素材 |
| PDFs | `assets/papers/pdfs/01-07_*/` | 精读原文（36 篇） |

---

## 四、执行计划

### Phase 1: 知识构建（Week 1-4）

Phase 1 的目标不是写论文，而是**补齐对核心领域的理解**。每周产出具体的 reading note 或文档，作为后续写作的素材。

#### Week 1: 精读三篇核心论文

| # | 论文 | 目标 | 产出 |
|---|------|------|------|
| 1.1 | Hillier & Hanson (1984) *The Social Logic of Space* | 理解构型理论的哲学基础、核心概念原始定义、社会学论证 | `hillier1984_social_logic_of_space.md`（60-80 行） |
| 1.2 | Turner et al. (2001) *From Isovists to Visibility Graphs* | 理解 VGA 数学基础、与 Space Syntax 指标关系、计算方法 | `turner2001_visibility_graph.md`（60-80 行） |
| 1.3 | Oh et al. (2025) *Spatially Aware LLM Agents* | 理解最接近的前置工作、空间感知水平操作化、实验设计 | `oh2025_spatially_aware_llm.md`（60-80 行） |

**精读策略**:
- Hillier 1984: 优先 Ch.1-3 (理论基础) + Ch.6 (社会逻辑)。若原著难获取，用免费在线的 *Space is the Machine* (1996) 替代
- Turner 2001: 全文精读（仅 18 页）
- Oh 2025: 全文精读，重点关注实验设计和空间感知水平定义

**Week 1 检验标准** — 完成后应能回答：
- [ ] "构型"与"组合"的区别是什么？
- [ ] Integration/Depth/Control 的图论定义是什么？
- [ ] VGA 与 axial map 分析的关系是什么？
- [ ] Oh et al. 如何操作化"空间感知水平"？与本 survey 的 L0-L5 有何异同？

#### Week 2: 扩展理论基础

| # | 任务 | 产出 |
|---|------|------|
| 2.1 | 精读 Hillier (1996) *Space is the Machine* 关键章节（Ch.1, Ch.4, Ch.8） | 补充到 hillier1984 reading note 或新建笔记 |
| 2.2 | 精读 Penn & Turner (2001) *Space Syntax Based Agent Simulation* | 理解 Space Syntax + Agent 模拟的唯一先例 |
| 2.3 | 将 `spatial_theory.md` 从 1.5KB 骨架扩展到完整教程（3-5 页） | 扩展后的 `spatial_theory.md` |

**Week 2 检验标准**:
- [ ] `spatial_theory.md` 包含 Integration/Depth/Control/Choice/Intelligibility 的完整定义、公式、直觉解释
- [ ] 能画出一个简单图的 justified graph 并手算 Integration
- [ ] 理解 Penn & Turner 2001 的 EVA (exosomatic visual architecture) 模型

#### Week 3: 文献补缺与竞争排查

| # | 任务 | 产出 |
|---|------|------|
| 3.1 | 精读 Feng et al. (2025) 全文，撰写对比分析 | Feng et al. 对比表（用于 §1.3） |
| 3.2 | 检索 2025-2026 新论文，补充到 `reference_index.md` | 更新后的参考文献库 |
| 3.3 | 排查是否有竞争性 survey 出现 | 竞争分析结论 |

**检索关键词**:
- `"space syntax" AND ("LLM" OR "language model" OR "agent")`
- `"spatial configuration" AND "multi-agent"`
- `"spatial reasoning" AND "social behavior" AND "LLM"`
- `"generative agents" AND "spatial"`

**检索渠道**: arXiv, Semantic Scholar, Google Scholar, ACL Anthology

**Week 3 检验标准**:
- [ ] 确认无竞争性 survey 占据本文定位
- [ ] `reference_index.md` 更新至 2026 年 4 月
- [ ] Feng et al. 对比分析完成

#### Week 4: L0-L5 分类学系统化

| # | 任务 | 产出 |
|---|------|------|
| 4.1 | 系统整理所有已知 LLM Agent 系统的空间处理方式 | L0-L5 分类表（完整版） |
| 4.2 | 为每个层次确认代表系统、空间信息类型、社会行为影响 | 系统化对比表（用于 §3.2） |
| 4.3 | 撰写 L4 构型空白的论证 | L4 gap analysis 文档 |

**L0-L5 分类学框架**:

| 层次 | 空间信息 | 代表系统 | 社会行为影响 |
|------|---------|---------|-------------|
| L0 | 无空间 | MetaGPT, ChatDev | 无 |
| L1 | 地点名称 | 简单 RPG, ChatArena | 仅通过名称语义 |
| L2 | 语义描述 | Generative Agents (Park 2023) | 通过 affordance 隐含 |
| L3 | 邻接 + 在场 | LIGS (Jeong 2025), AGA (Yu 2024) | 通过共现 |
| L4 | 构型指标 | **空白** ← survey 核心发现 | 理论预测存在但未验证 |
| L5 | 完整 3D | Habitat, AI2-THOR, SARAH | 主要服务导航而非社会行为 |

**Week 4 检验标准**:
- [ ] L0-L5 表格每层至少有 2 个代表系统，附引用
- [ ] L4 空白的论证逻辑清晰：为什么需要、为什么没人做、做了会怎样
- [ ] 对比表覆盖 ≥15 个系统

---

### Phase 2: 论文写作（Week 5-8）

#### 写作依赖关系

```
§2 Space Syntax Theory ─────→ §3 Spatial Representation (L0-L5)
                                        ↓
§4 LLM Spatial Reasoning ←── 独立，可与 §2/§3 并行
                                        ↓
§5 Multi-Agent Social Sim ──→ §6 Evaluation Methods
                                        ↓
                               §7 Research Agenda
                                        ↓
                      §1 Introduction + §8 Conclusion（最后写）
```

#### 逐周写作计划

**Week 5: §2 + §5（理论锚 + 最充足章节）**

| Section | 字数 | 素材来源 | 写作要点 |
|---------|------|---------|---------|
| §2 Space Syntax | 3000-4000 | `spatial_theory.md`(扩展版) + Hillier/Turner reading notes + `reference_index.md` Cat.2 | 为 AI 读者写的教程：概念→公式→实证→局限。避免建筑学术语堆砌 |
| §5 多 Agent 模拟 | 2500-3000 | 5 篇完整 reading notes + `spatial_agent_survey.md` §6 | 整合已有笔记；关键新增：§5.4 将 H1-H3 显式映射到文献中的证据 |

**Week 6: §3 + §4（表征 + 能力）**

| Section | 字数 | 素材来源 | 写作要点 |
|---------|------|---------|---------|
| §3 空间表征 L0-L5 | 2500-3000 | L0-L5 分类表 + Park/Hu/Oh reading notes | 核心产出：系统化对比表 + 构型空白论证。L0-L5 是 survey 的标志性贡献 |
| §4 LLM 空间推理 | 2000-2500 | `spatial_agent_survey.md` §3 + `reference_index.md` Cat.3 | 更新基准数据；明确立场：不需要解决"LLM 是否真正理解空间"，只需论证构型输入的可行性 |

**Week 7: §6 + §7（方法论 + 议程）**

| Section | 字数 | 素材来源 | 写作要点 |
|---------|------|---------|---------|
| §6 评估方法 | 2000-2500 | `plan_v9.md` §7 (BSR/TAR) + zhu2025 reading note | 将 BSR/TAR 从实验计划中的工具升级为独立方法论贡献 |
| §7 研究议程 | 1500-2000 | 综合 §2-§6 的 gaps + `plan_v9.md` 各章节 | 5 个开放问题的系统论述，每个问题给出可操作的研究方向 |

**Week 8: §1 + §8 + 图表**

| 任务 | 内容 |
|------|------|
| §1 Introduction | WHERE gap 论证 + Feng et al. 对比表 + 组织逻辑 |
| §8 Conclusion | 核心发现总结 + 局限 + 展望 |
| 图表制作 | 见下方图表清单 |

#### 关键图表清单

| # | 图表 | 类型 | 章节 | 优先级 |
|---|------|------|------|--------|
| 1 | L0-L5 空间表征分类学 | 阶梯图/金字塔 | §3 | 必须 |
| 2 | 因果链框架图 (Theory→Repr→Cap→App→Eval) | 流程图 | §1 | 必须 |
| 3 | 现有系统空间处理方式对比表 | 大表格 | §3 | 必须 |
| 4 | 与 Feng et al. 定位对比图 | 矩阵 | §1 | 推荐 |
| 5 | Space Syntax 核心指标示意图 | 概念图 | §2 | 推荐 |
| 6 | H1-H3 假设可视化 | 因果箭头图 | §5 | 推荐 |
| 7 | BSR/TAR 评估框架图 | 二维矩阵 | §6 | 可选 |

---

### Phase 3: 修订与投稿（Week 9-12）

| 周次 | 任务 |
|------|------|
| Week 9 | 全文通读，检查逻辑连贯性和论证完整性 |
| Week 10 | 内部审阅（导师/合作者反馈） |
| Week 11 | 根据反馈修订 |
| Week 12 | 格式化 + 投稿 |

---

### Phase 4: 回到实证论文（Phase 3 之后）

Survey 写作过程中建立的领域知识，用于重新评估实验计划 v9：

| 通过 survey 回答的问题 | 对实证论文的影响 |
|----------------------|----------------|
| 哪些 Space Syntax 指标在物理空间中证据最强？ | 决定优先检验 H1/H2/H3 中的哪个 |
| L4 构型表征的文本化有哪些已知挑战？ | 优化实验中的空间描述设计 |
| 现有 LLM 空间推理能力的实证边界在哪？ | 调整效应量预期和样本量 |
| 已有系统中空间对行为的影响有多大？ | 判断 v9 的 7 个条件是否必要 |

目标：将 v9 简化为更聚焦的 v10。

---

## 五、风险与应对

| 风险 | 应对 |
|------|------|
| Hillier 1984 原著太长/难获取 | 优先读 *Space is the Machine* (1996)，免费在线：spaceisthemachine.com |
| §2 (Space Syntax 给 AI 读者) 写不好 | 参考跨学科 survey 的理论引入写法；找建筑学背景的人审阅 |
| 发现竞争性 survey | Week 3 排查；若出现，调整切入角度而非放弃 |
| 时间拖延 | Phase 1 严格按周交付 reading note，不完美也推进；§5 素材最充足，可先写来建立信心 |

---

## 六、与实证论文的双向关系

Survey 不仅是独立产出，也是实证论文的基础设施：

| Survey 章节 | 为实证论文提供 |
|-------------|--------------|
| §2 Space Syntax | 理论基础的完整论证 |
| §3 L0-L5 | 实验条件（C1-C6m）的理论依据 |
| §4 LLM 空间推理 | 可行性论证 + 预实验设计依据 |
| §5 H1-H3 | 假设的文献支撑与先验预测 |
| §6 BSR/TAR | 评估方法论的完整说明 |
| §7 研究议程 | 实证论文在 research agenda 中的定位 |

---

## 七、立即开始

### 本周任务：精读 Hillier 1984

1. 确认获取方式：检查 `assets/papers/pdfs/02_Space_Syntax/` 是否有 PDF；若无，从 spaceisthemachine.com 下载 *Space is the Machine*
2. 精读 Ch.1-3 (理论基础) + Ch.6 (社会逻辑)
3. 填写 `assets/papers/reading_notes/hillier1984_social_logic_of_space.md`
4. 完成后的自检：能否用自己的话解释"构型"与"组合"的区别？能否手算一个 5 节点图的 Integration？
