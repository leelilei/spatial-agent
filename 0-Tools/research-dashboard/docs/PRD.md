# Research Dashboard PRD

- 版本：v1（完整规范）
- 状态：草案，待评审
- 日期：2026-06-14
- 适用范围：`/Users/mac/Documents/6-Research/0-Tools/research-dashboard`

---

## 1. 背景与问题

`research-dashboard` 是一个本地、只读的研究进度可视化工具。它用 Python 标准库起一个
HTTP 服务，前端是纯 HTML/CSS/JS，数据源是每个研究项目下的
`docs/guides/todolist.md`，外加可选的 `roadmap.yaml` 与 `project_map.yaml`。

它要回答的核心问题是一句话：

> **「我现在研究做到哪一步了？下一步该做什么？心里有没有底？」**

### 1.1 现状实测（2026-06-14）

`python3 server.py --check` 的真实结果：

| 项目 | 配置状态 | 解析结果 |
|---|---|---|
| 1-SpatialAgent | enabled | 可读，但进度显示 **0/0（0%）**，实际有 47 个 checkbox、30 个未完成 |
| 2-GAME-AGENT | enabled | ❌ 找不到 `todolist.md` |
| 3-SMGA | enabled | ✅ 完整：23/80（29%），有 roadmap + project_map |
| 4-SpatialAgent-Survey | enabled | ❌ 找不到 `todolist.md` |
| 5-Chinese-ASR-Compression | 未配置 | 未上架 |
| 0-LLM-learning | 未配置 | 未上架 |

结论：**除了 SMGA，仪表盘基本点不亮。** 它没有交付「心里有底」，反而因为大片空白
和报错，让人更没底。

### 1.2 根因（已定位）

1. **配置文件分裂，仓库内那份是死的。**
   仓库内 `research-dashboard/sources.json` 还是旧的 Windows 路径（`D:\...`），
   **根本没被加载**。真正生效的配置写死在 `server.py` 的常量里，指向仓库外的
   `/Users/mac/Documents/1-ProjectRes/Personal Todo/sources.json`。
   看仓库和实际运行是两套东西，极易误导。

2. **进度只认 `## Phase N` 标题。**
   `progress_summary()` 按 phase 汇总 checkbox。1-SpatialAgent 的 todolist 没有
   Phase 标题，于是 47 个任务全部不计入进度，显示 0%。即「有内容却一片空白」。

3. **完整体验门槛太高。**
   阶段流图、论文准备度等富面板依赖手写 `roadmap.yaml` + `project_map.yaml`。
   目前只有 SMGA 付了这个成本，其余项目跌回简陋的 derived 模式。

4. **上架一个项目要去仓库外手改 JSON**，无自动发现、UI 也加不了。

---

## 2. 目标与非目标

### 2.1 本期目标（已与用户确认）

- **G1 — 点亮所有项目。** 6 个研究项目，只要有 `todolist.md` 就能显示**真实进度
  百分比**，不再依赖 Phase 标题或 yaml。（对应原方向 A + B）
- **G2 — 强化「心里有底」体验。** 每个项目顶部给一个一眼看懂的答案：当前阶段、
  完成度%、距上次更新多久（过期标黄）、下一步 1–3 件事。（对应原方向 C）
- **G3 — 统一配置。** 单一可信配置来源，放进仓库；支持自动发现项目，新建
  `todolist.md` 即上架。

### 2.2 非目标（本期不做）

- 不做写入 / 编辑 todolist（保持只读，避免破坏来源文件）。
- 不做多用户、不做云同步、不做鉴权。
- 不强求每个项目都写 `roadmap.yaml` / `project_map.yaml`（它们仍是「锦上添花」层）。
- 不引入前端框架或构建步骤（保持零依赖、纯静态）。

---

## 3. 用户与使用场景

- **唯一用户**：项目所有者本人，CS 初学者，每周投入研究 ≤5 小时。
- **典型场景**：
  1. 一周开工前，打开仪表盘，3 秒内看清每个项目「在哪个阶段、完成多少、是否停滞」。
  2. 选定本周要推进的项目，点进去看「做过什么 / 下一步做什么」，直接照着干。
  3. 想确认论文能不能开写时，看「论文准备度」哪些 section 就绪、被什么卡住。
- **维护契约**：用户平时只维护 Markdown（`todolist.md`），yaml 只在愿意时补。

---

## 4. 数据契约（分层）

数据契约分三层，**层层可选、逐层增强**。这是本工具的核心设计原则：
**最低门槛能用，愿意投入就更好看。**

### 4.1 第 0 层 — `todolist.md`（必需，唯一硬要求）

只要项目下存在 `docs/guides/todolist.md` 且含 checkbox，就能上架并显示真实进度。

解析器识别：

| 语法 | 含义 |
|---|---|
| `> 更新日期：YYYY-MM-DD` | 新鲜度判断（G2 过期提醒） |
| `> 当前主线：...` | 顶部 Current Focus |
| `- [ ]` / `- [x]` | 任务，统计完成率 |
| `## ... Phase N ...` | 可选。有则按阶段汇总；**无则按全量 checkbox 汇总**（G1 关键变更） |
| `## 执行优先级` → `### Priority N` | 可选。给未完成任务排 P0–P4 优先级 |
| `## 暂不做` | 该段落下的任务不计入进度 |

**G1 核心规则变更**：当文档没有任何 Phase 标题时，进度 = 全文未被「暂不做」排除的
`[x]` 数 ÷ checkbox 总数。这样 1-SpatialAgent 这类项目立刻有真实百分比。

### 4.2 第 1 层 — `roadmap.yaml`（可选，结构化阶段）

控制阶段流图的轨道（tracks）与阶段（phases）结构。Schema（沿用现有实现）：

```yaml
version: 1
project: 3-SMGA
currentPhase: 3
tracks:
  - id: infrastructure
    name: 工程基础设施
    accent: "#ff9500"
    order: 2
phases:
  - number: 3
    title: 第一轮 baseline 运行
    track: infrastructure
    status: current        # done | in_progress | current | planned
    summary: 先在 seed_0001 上跑非 SMGA baseline。
    outputs:
      - benchmark_loader.py
```

无此文件时，阶段从 Markdown 的 Phase 标题派生（derived 模式）。

### 4.3 第 2 层 — `project_map.yaml`（可选，全功能）

驱动「研究阶段流图 / 历史 / 下一步 / 论文准备度」四个富面板。顶层键（沿用现有实现）：

```yaml
version: 1
project: 3-SMGA
title: Social Memory Graph Architecture
currentFocus: Phase 3 - First baseline runs
researchQuestion: How can socially actionable memory improve grounded planning ...

milestones:        # 「做过什么」：已完成里程碑，含产出文件路径（校验是否存在）
  - id: ...
    title: ...
    status: done
    phase: 2
    date: 2026-06-11
    outputs:
      - { path: scripts/benchmark_loader.py, label: Benchmark loader }
    taskRefs: [P2-01, P2-05]

mapNodes:          # 「阶段流图」节点，lane ∈ done|now|next|paper，可声明 dependsOn
  - id: baseline-runs
    title: First baseline runs
    lane: now
    status: current
    phase: 3
    dependsOn: [experiment-0-infra]
    outputs: [...]
    nextActions: [...]

paper:             # 「论文准备度」：各 section 的状态、依赖资产、blocker
  sections:
    - id: results
      title: Results
      status: missing     # ready|done|draft|planned|blocked|missing
      assets: [...]
      blockers: ["Baseline scores missing."]
      nextActions: [...]
```

无此文件时，四个面板从 roadmap + todolist 派生（功能较弱但可用）。

---

## 5. 功能需求

按三个目标分组，标注优先级（P0 必须 / P1 重要 / P2 增强）。

### G1 — 点亮所有项目

| ID | 优先级 | 需求 |
|---|---|---|
| F1.1 | P0 | 无 Phase 标题时，进度按全量 checkbox 完成率计算，不再为 0%。 |
| F1.2 | P0 | 自动发现：扫描 `<root>/*/docs/guides/todolist.md`，存在即上架。 |
| F1.3 | P1 | 自动发现的项目自动分配稳定 id（取目录名）与 accent（按顺序轮转调色板）。 |
| F1.4 | P1 | 已知项目缺 `todolist.md` 时，显示「未建任务清单」占位卡 + 一键复制模板提示，而非红色错误。 |

### G2 — 强化「心里有底」体验

| ID | 优先级 | 需求 |
|---|---|---|
| F2.1 | P0 | 每个项目卡顶部一行摘要：当前阶段名、完成度%进度条、未完成任务数。 |
| F2.2 | P0 | 新鲜度徽标：根据 `更新日期` 距今天数显示「N 天前更新」；超过阈值（默认 14 天）标黄、超过 30 天标红，提示「可能停滞」。 |
| F2.3 | P0 | 「下一步」前 1–3 件事：优先取当前阶段未完成任务，否则取最高优先级未完成任务。 |
| F2.4 | P1 | 工作区总览顶部：N 个项目活跃 / M 个停滞，本周（对比上一快照）净完成任务数。 |
| F2.5 | P2 | 进度趋势图已存在，确保每个点亮的项目都进入 `history.jsonl` 快照与图例。 |

### G3 — 统一配置

| ID | 优先级 | 需求 |
|---|---|---|
| F3.1 | P0 | 配置单一可信来源：仓库内 `research-dashboard/sources.json`。删除仓库外影子配置依赖。 |
| F3.2 | P0 | `sources.json` 改为「覆盖层」语义：自动发现为基础，配置文件只用于改名/改色/禁用/手动加非标准路径。空配置也能跑。 |
| F3.3 | P1 | research 根目录可由环境变量 `RESEARCH_DASHBOARD_ROOT` 覆盖；默认 `/Users/mac/Documents/6-Research`，缺失则回退到仓库上两级。 |
| F3.4 | P2 | `--check` 输出明确打印：配置来源路径、自动发现到的项目、每个项目的解析模式（layer 0/1/2）。 |

---

## 6. 模块设计

### 6.1 后端 `server.py`

- **配置加载（`load_source_configs`）重写为两步**：
  1. **发现**：glob `RESEARCH_ROOT/*/docs/guides/todolist.md`，生成基础 source 列表
     （id=目录名小写、name=目录名、accent=调色板轮转、enabled=true）。
  2. **合并覆盖**：若仓库内 `sources.json` 存在，按 id 合并，允许改 name/accent/path/
     enabled，以及追加非标准路径的项目。
  - 移除 `LEGACY_PERSONAL_TODO_DIR` 这条仓库外硬路径作为默认来源。
- **进度计算（新增 fallback）**：`parse_todo` 在 `phase_builders` 为空时，构造一个
  虚拟「全量」聚合，使 `progress_summary` 得到非零结果。保持现有 phase 模式不变。
- **新鲜度（新增）**：在 `parse_source` 输出里加 `staleness`: `{ days, level }`，
  `level ∈ fresh|warn|stale`，由 `updateDate` 与今天比较得出。阈值常量可配。
- **总览聚合（扩展 `dashboard_state().totals`）**：加 `activeCount` / `staleCount`，
  并基于 `history.jsonl` 上一条快照算 `weeklyCompletedDelta`。

### 6.2 前端 `static/`

- **项目卡（`source-grid`）**：补 F2.1/F2.2/F2.3 的顶部摘要行——阶段名 + 进度条 +
  新鲜度徽标 + 「下一步」最多 3 条。
- **总览（`summary`）**：补 F2.4 的活跃/停滞/本周净完成。
- **占位态**：缺 `todolist.md` 的已知项目渲染为温和的占位卡（F1.4），附模板片段。
- **趋势图**：确认所有点亮项目进图例（F2.5），无需重写。
- 不引入框架，沿用现有 `app.js` 的渲染函数风格。

### 6.3 文档与模板

- 新增 `docs/templates/todolist.template.md`：第 0 层最小可用模板（含
  `更新日期`、`当前主线`、一个 `## Phase 1`、几个 `- [ ]`、`## 执行优先级`）。
- 更新 `README.md`：说明新的「自动发现 + 覆盖层」配置语义，删掉对仓库外 sources.json
  的描述。

---

## 7. 分阶段里程碑

每个里程碑独立可验收、可单独提交，契合 ≤5h/周 的节奏。

### M1 — 点亮 + 统一配置（G1 + G3 的 P0）
- F3.1/F3.2 重写配置加载（发现 + 覆盖）。
- F1.1 无 Phase 时按全量 checkbox 算进度。
- F1.2 自动发现 6 个项目。
- **验收**：`--check` 显示 6 个项目，凡有 `todolist.md` 的进度均非零且数值正确；
  仓库内单一配置生效；删除仓库外配置后仍正常。

### M2 — 心里有底（G2 的 P0）
- F2.1 项目卡顶部摘要行。
- F2.2 新鲜度徽标 + 停滞提醒。
- F2.3 下一步 1–3 条。
- **验收**：打开首页，每个点亮项目 3 秒内能看清「阶段 / %/ 多久没更新 / 下一步」。

### M3 — 收尾增强（P1 + P2）
- F1.3/F1.4 占位卡与调色板。
- F2.4 总览活跃/停滞/本周净完成。
- F3.3/F3.4 环境变量与 `--check` 可观测性。
- 模板文件 + README 更新。
- 给缺失项目（2-GAME-AGENT、4-Survey、5-ASR、0-LLM-learning）各补一个最小
  `todolist.md`，使 6 个项目全部点亮。

---

## 8. 验收标准（总）

1. research 下每个含 `todolist.md` 的项目都显示**非零**真实进度。
2. 首页每个项目卡能一眼看到：当前阶段、完成度%、距上次更新天数（含停滞色）、下一步。
3. 配置只有仓库内一份；删除任何仓库外文件不影响运行；新建一个 `todolist.md` 后刷新
   即出现新项目，无需改代码。
4. 无 yaml 的项目不报错、不空白，至少有第 0 层的进度与下一步。
5. 不破坏 SMGA 现有的完整体验（roadmap + project_map 富面板照常）。

---

## 9. 风险与权衡

| 风险 | 应对 |
|---|---|
| 自动发现误抓非研究目录（如 `0-Tools` 自己） | 发现规则要求路径精确匹配 `*/docs/guides/todolist.md`；可在 `sources.json` 用 `enabled:false` 排除。 |
| 全量 checkbox 模式与 Phase 模式口径不一致 | 在卡片上标注进度来源（「按阶段」/「按任务」），避免误读。 |
| 仓库外旧配置仍被某些习惯依赖 | M1 保留一次性迁移说明；`--check` 打印实际配置来源，便于核对。 |
| 维护负担回潮（又得手写 yaml） | yaml 始终可选；第 0 层始终够用，富面板仅对愿意投入的项目（如 SMGA）开放。 |

---

## 10. 开放问题（待用户拍板）

- 停滞阈值用默认 14 天 / 30 天，还是按你的实际节奏调整？
- 是否要把 `0-LLM-learning`（偏学习、非论文项目）也纳入同一仪表盘，还是单独标记为
  「学习类」不参与论文准备度？
