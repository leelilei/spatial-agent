# 研究项目结构规范（Research Project Standard）

- 版本：v1（草案）
- 日期：2026-06-14
- 适用对象：`/Users/mac/Documents/6-Research` 下**以发表论文为目标**的研究项目
  （实证项目，综述项目同样适用）。
- **不适用**：学习/练习类项目（如 `0-LLM-learning`），它们不要求遵循本规范。

---

## 0. 为什么要这份规范

每个论文项目都应该能在 3 秒内回答：**「我在哪、做过什么、下一步做什么、论文能不能开写」。**
要稳定回答这四个问题，项目就得维护一组**固定的、有契约的文件**。

本规范做三件事：
1. 定义一套**标准目录骨架**和**每个文件的契约**（用途、必需性、最小格式）。
2. 用 `scaffold.py` 一键生成符合规范的新项目骨架。
3. 用 `check_compliance.py` 检查任意项目「该有的文件齐不齐」，并供 research-dashboard
   读取，显示「规范健康度」。

`research-dashboard` 读取的 `todolist.md` / `roadmap.yaml` / `project_map.yaml`
是本规范的一个子集——**规范是源，仪表盘是视图。**

---

## 1. 标准目录骨架

```text
<N-项目名>/
├── README.md                      # [L0] 项目是什么 + 当前状态入口
├── docs/
│   ├── guides/
│   │   ├── todolist.md            # [L0] 任务清单（仪表盘契约，唯一硬要求）
│   │   ├── roadmap.yaml           # [L1] 结构化阶段（仪表盘契约）
│   │   └── project_map.yaml       # [L2] 全功能研究地图（仪表盘契约）
│   ├── plans/
│   │   ├── proposal.md            # [L1] 当前研究方案（唯一 current 版本）
│   │   └── archive/               # [—] proposal 历史版本，命名 proposal_vN.md
│   ├── project/
│   │   ├── reference_sources.md   # [L2] 文献索引
│   │   ├── decisions.md           # [L3] 关键决策日志（带日期）
│   │   └── *_schema_v*.md         # [—] 数据 / 接口 schema（按需）
│   ├── background/                # [—] related work、理论背景
│   ├── experiments/               # [—] 实验设计与报告
│   └── reviews/                   # [—] 自我批判 / challenge
├── <项目名>-core/                  # [L3] 代码包（实证项目）
│   ├── src/                       #      研究代码
│   ├── scripts/                   #      可运行脚本
│   ├── configs/                   #      实验配置
│   ├── data/                      #      输入数据（大文件走 .gitignore）
│   ├── results/                   #      产出结果
│   └── tests/                     #      测试
├── benchmarks/  |  annotation/     # [—] 实验数据集（按项目需要）
├── paper/                          # [L3] 论文手稿
└── assets/papers/                  # [—] reference PDFs and literature metadata
    ├── metadata/                   # generated reports, manifests, citation tables, scripts
    ├── pdf/                        # local PDFs; optional one-level topic categories
    ├── fulltext/                   # extracted Markdown full text; mirrors pdf/ categories when useful
    └── notes/                      # reading notes for papers we expect to cite
```

方括号标注的是该文件/目录所属的**合规层级**（见第 3 节）。`[—]` 表示完全可选、不计入分级。

> 综述项目差异：用 `survey_plan.md` 代替 `proposal.md`，代码包可缺省，
> `benchmarks/` 通常换成 `assets/survey_paper/` 下的证据表。其余一致。

---

## 2. 文件契约

每个受规范约束的文件，定义「用途 / 必需性 / 最小格式」。

### 2.1 `README.md` — 项目门面 〔L0 必需〕

- **用途**：任何人（包括三个月后的你）打开就知道这是什么、现在到哪了。
- **最小格式**：
  ```markdown
  # <项目名>
  一句话研究问题。
  ## 当前状态
  当前阶段：Phase N — 名称 ｜ 完成度：X% ｜ 更新：YYYY-MM-DD
  详见 docs/guides/todolist.md
  ```

### 2.2 `docs/guides/todolist.md` — 任务清单 〔L0 必需〕

- **用途**：唯一的「真相源」任务清单；仪表盘进度与下一步都来自它。
- **必需头部**：
  ```markdown
  > 更新日期：YYYY-MM-DD
  > 当前主线：一句话描述当前在推什么
  ```
- **任务**：用 `- [ ]` / `- [x]`。
- **可选结构**：`## Phase N — 标题` 分阶段；`## 执行优先级` 下用 `### Priority N`
  标优先级；`## 暂不做` 段落内的任务不计入进度。
- **契约要点**：`更新日期` 必须随每次实质推进更新——它驱动仪表盘的「停滞提醒」。

### 2.3 `docs/plans/proposal.md` — 当前研究方案 〔L1 推荐〕

- **用途**：当前 live 的研究设计（动机、研究问题、方法、实验设计）。
- **版本治理（关键）**：
  - `proposal.md` **永远是当前版**，文件名不带版本号。
  - 产生新版本时：把旧的 `proposal.md` 复制到 `docs/plans/archive/proposal_vN.md`，
    再在 `proposal.md` 顶部更新版本与日期。
  - **任何时刻 `docs/plans/` 根目录下只有一个 `proposal.md`。** 杜绝 v1..v14 泛滥。
- **最小头部**：
  ```markdown
  # <项目名> Proposal
  > 版本：v4.6 ｜ 更新：YYYY-MM-DD ｜ 状态：active
  ```

### 2.4 `docs/guides/roadmap.yaml` — 结构化阶段 〔L1 推荐〕

- **用途**：定义阶段流图的轨道（tracks）与阶段（phases）。仪表盘契约，schema 见
  `research-dashboard/docs/PRD.md` §4.2。
- 无此文件时阶段从 todolist 的 Phase 标题派生。

#### 标准 Track 骨架（实证项目统一使用）

实证论文项目的 track **统一采用下面四个**，对应研究的生命周期弧线
`设计 → 构建 → 实验 → 写作`。每个 track 有一句"什么该进来"的判定，避免把实验
和工程混在一起：

| id | 名称 | order | accent | 判定：什么该进来 |
|---|---|---|---|---|
| `design` | 设计 | 1 | `#0071e3` | 还在决定"测什么、怎么测"：研究问题、proposal、schema、场景/benchmark 设计、项目搭建 |
| `build` | 构建 | 2 | `#ff9500` | 在造"用来跑实验的机器"：评测 harness、scorer、方法与对照的实现 |
| `experiment` | 实验 | 3 | `#34c759` | 在产出证据：baseline、treatment、ablation、pilot → 主实验 → 控制实验 |
| `write` | 写作 | 4 | `#af52de` | 在把证据讲成论文：统计分析、失败分析、draft、可复现 release |

约定：

- 所有"跑实验产出结果"的 phase（无论 baseline 还是 ablation）都归 `experiment`，
  不要拆进 `build`——这是把流图理清楚的关键。
- `build` 只放"造工具/实现方法"本身；方法实现完成后的运行归 `experiment`。
- `design` 包含项目卫生与版本治理这类 setup 工作。
- benchmark 若是项目核心贡献，可在 `design` 与 `build` 之间细分，但默认不拆。

### 2.5 `docs/guides/project_map.yaml` — 全功能研究地图 〔L2 推荐〕

- **用途**：驱动「阶段流图 / 历史 / 下一步 / 论文准备度」四个富面板。
  schema 见 PRD §4.3。
- 无此文件时四面板从 roadmap + todolist 派生（功能较弱）。

> **V2 统一文件（推荐）**：`docs/guides/project.yaml` 可一文件替代 `roadmap.yaml` +
> `project_map.yaml`（消除 phases 与 mapNodes 的重复），schema 见 `0-Tools/docs/PRD-v2.0.md` §5.2。
> 仪表盘与合规检查都优先读 `project.yaml`，并接受它满足 L1/L2 的 roadmap/map 要求。
> 用 `python3 0-Tools/research-standard/migrate.py <项目目录>` 从 V1 双文件迁移。

### 2.6 `docs/project/reference_sources.md` — 文献索引 〔L2 推荐〕

- **用途**：项目引用的核心文献清单 + 一句话定位，避免重复找。

### 2.7 `docs/project/decisions.md` — 决策日志 〔L3 推荐〕

- **用途**：记录「为什么这么做」的关键决策（取代散落的 kickoff / git_progress_log）。
- **最小格式**：每条 `## YYYY-MM-DD 决策标题` + 背景 / 决定 / 理由。

### 2.8 `<项目名>-core/` — 代码包 〔L3，实证项目必需〕

- **用途**：所有研究代码。固定子目录 `src/ scripts/ configs/ data/ results/ tests/`。
- 大数据 / 模型权重走 `.gitignore`，不进 git。

### 2.9 `paper/` — 论文手稿 〔L3 推荐〕

- **用途**：手稿正文与图表。论文准备度（project_map 的 `paper.sections`）应与此对应。

### 2.10 `assets/papers/` — 本地文献资产

- **用途**：集中保存论文 PDF、文献检索报告、引用源校准表、下载清单与阅读笔记。
- **标准布局**：
  ```text
  assets/papers/
  ├── metadata/   # generated reports, manifests, citation tables, helper scripts
  ├── pdf/        # local PDFs
  ├── fulltext/   # Markdown full text extracted from PDFs
  └── notes/      # reading notes for papers we expect to cite
  ```
- **PDF 分类规则**：`pdf/` 下最多增加一层主题分类，例如
  `pdf/01_agent_societies/<paper>.pdf`。不要使用
  `pdfs/report_downloads/` 这类“下载批次目录”；下载来源、失败原因、引用源校准应放在
  `metadata/`。
- **全文转换规则**：若需要让 Codex / LLM 辅助精读、检索和主题归纳，优先把 PDF 转成
  `fulltext/` 下的 Markdown。`fulltext/` 可镜像 `pdf/` 的一层主题分类，例如
  `fulltext/01_agent_societies/<paper>.fulltext.md`；转换清单、质量标记和失败原因放在
  `metadata/`，不要混入正文目录。
- **引用源规则**：PDF 的下载来源不等于论文引用来源。需要严肃写作时，应在
  `metadata/citation_sources.*` 中记录优先引用的期刊 / 会议 / DOI 版本。

---

## 3. 合规层级（Compliance Levels）

逐层递进，`check_compliance.py` 据此给项目打级。**只有低层全满足才认定达到高层。**

| 层级 | 名称 | 满足条件（在低层基础上新增） |
|---|---|---|
| **L0** | Minimal（可上架仪表盘） | `README.md` + `docs/guides/todolist.md` |
| **L1** | Tracked（有计划与阶段） | `docs/guides/roadmap.yaml` + `docs/plans/proposal.md` |
| **L2** | Mapped（全功能可视化） | `docs/guides/project_map.yaml` + `docs/project/reference_sources.md` |
| **L3** | Paper-ready（可写论文） | `paper/` + `docs/project/decisions.md`（实证项目另需 `<name>-core/`） |

设计意图：**L0 门槛极低**（建一个 todolist 就能被仪表盘点亮），愿意投入的项目逐层升级，
SMGA 目前在 L2→L3 之间。

---

## 4. 现有项目对照（2026-06-14）

| 项目 | 估计层级 | 主要缺口 |
|---|---|---|
| 1-SpatialAgent | L0→L1 | proposal 版本泛滥需收敛；todolist 缺 Phase 结构 |
| 2-GAME-AGENT | 未达 L0 | 缺 `docs/guides/todolist.md` |
| 3-SMGA | L2（接近 L3） | 补 `decisions.md`、`paper/` 落地 |
| 4-SpatialAgent-Survey | L0→L1 | 缺 todolist；plan 多版本需收敛 |
| 5-Chinese-ASR-Compression | 未达 L0 | 几乎空壳，缺 README/todolist |

> 0-LLM-learning 为学习项目，不在规范范围内。

---

## 5. 配套工具

- `scaffold.py <项目名> [--type empirical|survey]`：在 research 根下生成符合规范的骨架。
- `check_compliance.py [项目路径...]`：检查合规层级，输出 JSON；被 research-dashboard
  调用以显示「规范健康度」。

---

## 6. 开放问题

- L3 是否强制 `paper/`？早期项目可能想先 L2 稳定再说。
- 综述项目是否单独出一份 profile，还是继续用「inline 差异说明」？（当前选择：inline）
