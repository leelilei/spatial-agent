# Research Cockpit — 产品 PRD v2.0

- 状态：草案，待评审（重构愿景）
- 日期：2026-06-14
- 范围：整个 `/Users/mac/Documents/6-Research/0-Tools` 套件（dashboard + standard + 工具链）
- 关系：取代并合并 V1 的两份分散文档——
  `research-dashboard/docs/PRD.md`（v1.1）与 `research-standard/RESEARCH-PROJECT-STANDARD.md`。
  V1 文档保留为组件级历史，本文件是产品级单一真相。

---

## 1. 一句话愿景

**Research Cockpit 是一个本地、只读、纯文本驱动的"研究指挥舱"，让单个研究者对手上
所有论文项目随时"心里有底"——一眼知道每个项目在哪、下一步做什么、卡在哪、离投稿多远。**

---

## 2. 从 V1 学到了什么（重构动机）

V1 把"点亮所有项目 / 统一配置 / 心里有底 / 合规"都做出来了，但暴露了三个结构性问题：

1. **数据模型有冗余、心智负担高。** 一个项目要维护 `todolist.md` + `roadmap.yaml` +
   `project_map.yaml` 三个结构文件，其中 roadmap 的 phases 和 project_map 的 mapNodes
   **本质是同一批东西**（都按 phase 编号）。后端因此长出一堆 manifest/derived 的分支逻辑，
   作者也不知道该写哪个。
2. **详情页按"数据类型"切 tab，不是按"问题"。** 地图/历史/下一步/论文四个 tab，但用户
   打开项目时问的是"我现在怎么样"，结果一个完整现状被拆到三处、还要来回切。落地页是
   结构图而不是状态。
3. **"标准"和"仪表盘"像两个工具。** 其实它们是一件事的两面：标准 = 数据怎么长，
   仪表盘 = 数据怎么看。V1 把它们当两个产品，接缝处一直在打补丁。

V2 的目标就是把这三件事捋直。

---

## 3. 设计原则

1. **纯文本是唯一真相。** 所有状态都活在项目目录里的 Markdown/YAML，git 友好、手改或
   Claude 改都行。工具只读，绝不回写项目文件（仪表盘只写自己的历史快照）。
2. **问题驱动，不是数据驱动。** 每个视图回答研究者脑子里的一个问题，而不是罗列一类数据。
3. **门槛递进。** 一个 `todolist.md` 就能用；愿意多写一个 `project.yaml` 就解锁全部富视图。
   永远不强制。
4. **少而准。** 宁可少几个面板，也不堆 tab。每加一处信息都要过"它回答哪个问题"。
5. **本地零依赖。** Python 标准库 + 可选 PyYAML，纯静态前端，无框架、无构建、无云、无鉴权。
6. **标准是产品的一部分，不是附属文档。** 合规等级要能在仪表盘里指导你"下一步补什么"。

---

## 4. 架构：三支柱

```text
┌─────────────────────────────────────────────────────────┐
│  ① 标准 Standard  —— 数据怎么长                            │
│     每个项目的文件契约 + 4-track 模型 + L0–L3 成熟度        │
├─────────────────────────────────────────────────────────┤
│  ② 仪表盘 Dashboard —— 数据怎么看（只读派生）              │
│     工作区总览 + 项目指挥舱（Overview 优先 + 下钻）         │
├─────────────────────────────────────────────────────────┤
│  ③ 工具链 Tooling —— 维护数据                              │
│     scaffold（建合规项目）+ check（审计/升级建议）         │
└─────────────────────────────────────────────────────────┘
            ↑ 三者共享同一套数据模型与 4-track / L0–L3 定义
```

---

## 5. 数据模型 V2（核心重构）

### 5.1 把三个结构文件收敛为两个

| V1 | V2 | 说明 |
|---|---|---|
| `docs/guides/todolist.md` | `docs/guides/todolist.md` | 保留：**日常任务清单**（checkbox / Phase / 优先级）。 |
| `docs/guides/roadmap.yaml` + `docs/guides/project_map.yaml` | **`docs/guides/project.yaml`** | 合并：项目的**结构化骨架**。消除 phases 与 mapNodes 的重复。 |

一个项目的"真相"= **`todolist.md`（动态任务） + `project.yaml`（静态骨架）**。其余标准文件
（README、proposal/survey_plan、reference_sources、decisions、paper/）不变。

### 5.2 `project.yaml` schema（统一骨架）

```yaml
version: 2
project: 3-SMGA
type: empirical                 # empirical | survey（survey 无 build track）
title: Social Memory Graph Architecture
researchQuestion: How can socially actionable memory improve grounded planning…

phases:
  - n: 0
    title: 项目卫生与版本管理
    track: design               # design | build | experiment | write（标准 4-track）
    status: done                # done | current | next | planned | blocked
    date: 2026-06-11            # 完成日期 → 用于历史里程碑时间线
    summary: 让工作区清楚、可恢复。
    outputs:                    # 产物文件；仪表盘自动校验是否存在
      - README.md
      - docs/guides/todolist.md
  - n: 3
    title: 第一轮 baseline 运行
    track: experiment
    status: current
    summary: 先在 seed_0001 上跑非 SMGA baseline。
    next:                       # 该阶段下一步动作（缺省则从 todolist 派生）
      - Freeze provider/model/temp/decoding
      - Generate M0_GA outputs for seed_0001
    outputs:
      - scripts/benchmark_loader.py

paper:                          # 驱动"论文准备度"；缺省则不显示该面板
  sections:
    - id: results
      title: Results
      status: missing           # ready | done | draft | planned | blocked | missing
      blockers: [Baseline scores missing]
      next: [Populate after scorer runs]
```

### 5.3 仪表盘从这两个文件派生一切（不再有 manifest/derived 两套逻辑）

- **两层 track 流图** ← `phases`（按 track 分组，phase 为可点子节点）。
- **历史里程碑** ← `status: done` 且有 `date` 的 phases。
- **论文准备度** ← `paper.sections`。
- **概览/下一步** ← `current` phase + 其 `next`（缺省回退到 todolist 未完成任务）。
- **产出/资产** ← 所有 `outputs` + 文件存在性校验。
- **进度%** ← todolist 的 checkbox（有 Phase 用 Phase，无则全量）。
- **新鲜度** ← todolist 的 `更新日期`。
- **合规等级** ← 文件存在性（check_compliance）。

### 5.4 兼容与迁移

- 仪表盘**同时读 V1 与 V2**：有 `project.yaml` 用之；否则回退读 `roadmap.yaml` +
  `project_map.yaml`（V1 行为）。零中断。
- 提供 `migrate.py`：把 `roadmap.yaml` + `project_map.yaml` 合并为 `project.yaml`，原文件
  移入 `archive/`。逐项目自愿迁移。

---

## 6. 信息架构 V2（视图）

### 6.1 工作区总览（Home）

保留 V1 的项目卡（当前阶段 / 进度环 / 新鲜度 / 下一步 / 合规徽标）+ 顶部汇总
（活跃·停滞 / 本周净完成 / 总进度）+ 进度趋势图。**这一层 V1 已经不错，基本沿用。**

### 6.2 项目指挥舱（Project Cockpit）—— 重构重点

落地即"概览"，回答"我现在怎么样"；其余作下钻。

```text
┌────────────────────────────────────────────────────────┐
│ 3-SMGA                          [L3]  🟢 3天前更新        │
│ Research Q: How can socially actionable memory…          │
├──────────────────┬─────────────────────────────────────┤
│ 当前阶段          │ 此刻该做（Do Next，最多 3 条）         │
│ Phase 3 · 实验    │  1. Freeze provider/model/temp…       │
│ ●●●○○○○○○ 29%     │  2. Generate M0_GA outputs…           │
│ 23/80 任务        │  3. Score baselines…                  │
├──────────────────┼─────────────────────────────────────┤
│ 论文准备度 2/6    │ 卡住 / 风险：4 个 blocker             │
│ 最近：+19 本周    │ 上次里程碑：Exp0 infra (6-11)         │
└──────────────────┴─────────────────────────────────────┘
  [路线图 →]  [进展 →]  [论文 →]  [决策 →]  [产出 →]
```

下钻页（按"少而准"裁剪）：

| 页 | 回答的问题 | 来源 | 去留 |
|---|---|---|---|
| **概览** | 我现在怎么样？ | 派生 | **V2 新增，默认落地** |
| **路线图** | 整个计划长什么样、我在哪段？ | phases | 保留（两层 track 流图） |
| **进展** | 我做成了哪些里程碑？ | done phases + 热力图 | 保留，里程碑为主、热力图为辅 |
| **论文** | 论文还差什么？ | paper.sections | 保留 |
| **决策** | 当初为什么这么设计？ | decisions.md | **可选新增（按需）** |
| **产出** | 关键文件/数据/草稿在哪、在不在？ | outputs + 存在性 | **可选新增（按需）** |

- V1 的 **"Next Work"独立 tab 取消**，精华（Do Next）并入概览。
- 决策 / 产出默认折叠或仅在有内容时出现，避免 tab 膨胀。

---

## 7. 4-track 与 L0–L3（沿用 V1，明确化）

- **标准 4-track**：设计 design → 构建 build → 实验 experiment → 写作 write。
  综述项目省略 build。判定见 standard。所有"跑实验出结果"归 experiment。
- **成熟度 L0–L3**：L0 可上架 → L1 有计划与阶段 → L2 全功能可视化 → L3 可写论文。
- **V2 强化**：合规不只是徽标，概览页给"**升级提示**"——例如"补 `docs/project/decisions.md`
  即达 L3"。让工具主动牵引项目走向成熟。

---

## 8. 功能需求（V2）

P0 必须 / P1 重要 / P2 增强。

### 数据模型
- R1 (P0)：仪表盘读 `project.yaml`，派生全部结构视图；无则回退 V1 双文件。
- R2 (P0)：`project.yaml` 单文件即可替代 roadmap + project_map，无重复字段。
- R3 (P1)：`migrate.py` 合并 V1 双文件 → `project.yaml`。

### 指挥舱
- R4 (P0)：项目详情默认落地"概览"，一屏含当前阶段/进度/新鲜度/下一步1-3/阻塞/论文%/最近动态。
- R5 (P0)：取消独立 Next Work tab，并入概览。
- R6 (P1)：下钻页路线图/进展/论文沿用并精简（进展以里程碑为主）。
- R7 (P2)：可选"决策""产出"下钻页（有内容才出现）。

### 标准牵引
- R8 (P1)：概览/卡片显示"距下一合规等级还差哪个文件"的升级提示。
- R9 (P2)：`check --doctor` 给每个项目一句话"下一步该补什么"。

### 沿用 V1（不回退）
- 自动发现 + 仓库内覆盖配置；checkbox 进度回退；新鲜度；合规徽标；趋势图；
  两层 track 流图；学习类项目排除。

---

## 9. 里程碑（V2 分期）

- **V2.0-M1 指挥舱**：概览落地页 + 取消 Next Work tab（R4, R5）。**纯前端，先做，见效最快。**
- **V2.0-M2 数据模型**：`project.yaml` 支持 + 回退兼容 + `migrate.py`（R1, R2, R3）。
- **V2.0-M3 牵引与收尾**：升级提示、决策/产出下钻、`check --doctor`（R7, R8, R9）。

> 注：M1 不依赖 M2，可先单独交付，立刻解决"不直观"。

---

## 10. 非目标

- 不做 UI 内编辑/回写项目文件（保持只读）。
- 不做云同步 / 多用户 / 鉴权 / 账号。
- 不引入前端框架或构建步骤。
- 不强制任何项目写 `project.yaml`（L0 永远够用）。
- 不纳入学习类项目（0-LLM-learning、2-GAME-AGENT）。

---

## 11. 开放问题

- `project.yaml` 是否彻底取代双文件，还是长期双轨？（建议：双读兼容、自愿迁移，不强制弃用 V1。）
- 概览的"最近动态"用 sparkline 还是"最近完成的 N 件"列表？
- 综述项目的"实验"track 用什么名更贴（如"证据"）？
- 决策/产出是做成 tab 还是概览里的可展开区块？
