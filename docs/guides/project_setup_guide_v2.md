# SpatialAgent 项目启动指引 v2

> 适用对象：当前仓库的研究执行者  
> 文档目标：帮助你在现有仓库中快速进入研究、理解目录分工、找到代码入口、知道资料和结果应该放在哪里  
> 当前主计划：`../plans/plan_v7.md`  
> 方法执行手册：`./research_mentorship_guide_v2.md`  
> 说明：旧版 `project_setup_guide.md` 保留为历史脚手架文档；当前仓库请以本文件为准

---

## 1. 先理解这三份核心文档的分工

这三份文档不是一回事，阅读顺序也不一样。

### `docs/plans/plan_v7.md`

这是当前唯一有效的主研究计划。它负责回答：

- 这篇论文到底要证明什么
- `RQ1-RQ4`、`H1-H3` 是什么
- `MIC`、`TAR_run`、`C6m / C6f / C4` 分别承担什么方法角色
- 哪些实验是主验证，哪些只是扩展或机制分析

如果你对项目的研究方向、实验结构、主张边界有疑问，先回到 `plan_v7.md`，不要先看代码。

### `docs/guides/research_mentorship_guide_v2.md`

这是研究执行手册。它负责回答：

- 推进顺序应该是什么
- 每个阶段开始前要准备什么
- 哪些结果才算过关
- 哪些是高价值扩展，哪些不该抢主线

如果你已经知道研究要做什么，但不知道“先做哪一步、做到什么程度算合格”，看这份。

### `docs/guides/project_setup_guide_v2.md`

这份文档只做落地导引。它负责回答：

- 当前仓库的目录是怎么分工的
- 代码、配置、论文资产、notebook、结果分别在哪
- 新接手的人应该从哪里开始看
- 研究资料和运行产物分别应该归档到哪里

它不是新的研究计划，也不是从零搭项目骨架的说明书。

---

## 2. 当前仓库的整体结构

当前根目录只保留四个主区域：

```text
.
├── docs/
├── assets/
├── scripts/
└── spatial-agent-core/
```

### `docs/`

仓库级文档区。这里只放“说明性内容”，不放代码和运行产物。

当前重点子目录：

- `docs/plans/`: 主计划与历史版本；当前以 `plan_v7.md` 为准
- `docs/guides/`: 各类操作指引、执行手册、项目说明
- `docs/experiments/`: preflight 和实验设计文档
- `docs/reviews/`: 计划评审、challenge、版本 review
- `docs/background/`: Space Syntax 理论与 related work
- `docs/decisions/`: 关键设计决策
- `docs/meeting_notes/`: 会议纪要

一句话理解：`docs/` 回答“为什么这样做、应该怎么做、当前做到哪里”。

### `assets/`

长期保存的研究资产区。这里放静态资料，不放可执行工程。

当前重点路径：

- `assets/papers/pdfs/`: 论文 PDF
- `assets/papers/reading_notes/`: 阅读笔记
- `assets/papers/generated/`: 自动生成的论文清单、BibTeX、下载状态

一句话理解：`assets/` 回答“研究材料在哪里”。

### `scripts/`

仓库级辅助脚本。它们服务于整个仓库，不属于 `spatial-agent-core/` 的运行主线。

当前脚本主要用于：

- 下载论文
- 重试 arXiv 下载
- 生成参考文献相关索引

一句话理解：`scripts/` 是仓库层面的辅助工具箱。

### `spatial-agent-core/`

这是实际可运行的主工程。代码、配置、实验入口、notebook、结果、论文写作都在这里。

一句话理解：真正执行实验时，你大部分时间都在这个目录里工作。

---

## 3. `spatial-agent-core/` 里到底看什么

如果你已经进入执行阶段，优先理解这个子项目的分工：

```text
spatial-agent-core/
├── configs/
├── data/
├── experiments/
├── notebooks/
├── paper/
├── references/
├── results/
├── scripts/
├── src/
└── tests/
```

### `configs/`

实验配置入口。

- `configs/default.yaml`: 默认项目配置
- `configs/layouts/`: 地图布局配置
- `configs/agents/`: NPC 设定
- `configs/experiments/`: 实验条件配置；当前已有 `preflight_v7.yaml` 等

如果你要改实验条件、地图、角色或 preflight 参数，先看这里。

### `src/`

核心代码实现。

- `src/space/`: 空间图和指标计算
- `src/agent/`: agent、perception、memory、planning、action sampling
- `src/world/`: world state、event system、engine、renderer
- `src/llm/`: LLM client、judge、prompt、cache
- `src/analysis/`: preflight 和行为分析相关工具

如果你要实现方法、补逻辑、查核心流程，主要看这里。

### `experiments/`

实验运行入口。

- `run_preflight.py`: v7 preflight
- `run_exp1.py`, `run_exp2.py`, `run_exp3.py`, `run_exp4_prep.py`: 各实验入口

如果你已经完成环境准备并要真正跑实验，从这里开始。

### `tests/`

回归验证入口。改完空间指标、agent 行为、preflight 逻辑后，优先补看和运行这里的测试。

### `notebooks/`

探索性分析和结果整理入口。当前 notebook 已经集中到这里，不再放在顶层 `assets/`。

如果你要看指标分布、实验结果、社交网络分析、人评分析，优先看这里。

### `results/`

实验输出和中间汇总目录。当前重点是：

- `results/preflight/`: v7 preflight 任务、原始响应、评分结果、summary、quality report、MIC/convergence 指标

如果你想知道 preflight 是否已经跑过、结论是什么、当前数据产物在哪，先从这里看。

### `paper/`

论文写作目录。LaTeX 主文、章节、补充材料都在这里。

### `references/`

参考资料说明目录。它不是 PDF 仓库本体，PDF 和阅读笔记已经统一在顶层 `assets/papers/`。

### `data/`

工程运行数据目录，用于保存 raw、processed、human_eval、synthetic 等数据容器。

---

## 4. 按 v7 的推荐启动顺序进入项目

不要一上来就写代码。当前仓库最稳妥的进入顺序如下。

### 第一步：先锁定研究主线

按顺序阅读：

1. `docs/plans/README.md`
2. `docs/plans/plan_v7.md`
3. `docs/guides/research_mentorship_guide_v2.md`

读到这里，你至少要明确：

- 当前主计划是 `v7`
- 主验证链条不是“随便跑几个实验”，而是围绕 `MIC`、`TAR_run`、`C6m / C6f / C4`
- 阶段 1、阶段 2、阶段 3 的地位不一样

### 第二步：再定位仓库与目录

按顺序看：

1. `README.md`
2. `docs/README.md`
3. `assets/README.md`
4. `spatial-agent-core/README.md`
5. 本文件 `project_setup_guide_v2.md`

做到这一步时，你应当知道：

- 文档在 `docs/`
- 论文资产在 `assets/papers/`
- 代码主工程在 `spatial-agent-core/`
- notebook 在 `spatial-agent-core/notebooks/`
- 结果在 `spatial-agent-core/results/`

### 第三步：确认 preflight 现状

重点查看：

- `docs/experiments/preflight_experiments.md`
- `docs/experiments/preflight_gpt54_core20_report.md`
- `spatial-agent-core/configs/experiments/preflight_v7.yaml`
- `spatial-agent-core/results/preflight/reports/preflight_summary.md`
- `spatial-agent-core/results/preflight/reports/preflight_decisions.json`

做到这一步时，你应当知道：

- v7 preflight 做了哪些任务
- 当前有哪些结论已经形成
- 哪些指标、数据和任务文件已经落地

### 第四步：再进入代码和实验

推荐入口顺序：

1. `spatial-agent-core/src/space/`
2. `spatial-agent-core/src/agent/`
3. `spatial-agent-core/src/world/`
4. `spatial-agent-core/src/llm/`
5. `spatial-agent-core/src/analysis/`
6. `spatial-agent-core/experiments/`
7. `spatial-agent-core/tests/`

这样看代码，能先理解空间表示，再理解 agent，再理解 world 和实验执行。

---

## 5. 研究资料、实验结果和文档应该放在哪里

这是当前仓库最容易混乱的地方，必须先统一。

### 文档放 `docs/`

放这里的内容包括：

- 计划
- 评审
- 指南
- 背景理论
- 实验说明
- 会议纪要

不要把这类说明文档继续塞进 `spatial-agent-core/`。

### 静态研究资产放 `assets/`

放这里的内容包括：

- 论文 PDF
- 阅读笔记
- 生成的 BibTeX 和 paper list

不要把论文 PDF、阅读笔记、资料型 markdown 放回代码子项目。

### 可运行工程内容放 `spatial-agent-core/`

放这里的内容包括：

- 代码
- 配置
- 实验入口
- notebook
- 运行数据
- 结果产物
- 论文写作文件

### 运行结果放 `spatial-agent-core/results/`

包括：

- preflight 输出
- 实验日志
- figures、tables
- 各类 summary 和中间评分结果

不要把运行结果混放到 `docs/` 或 `assets/`。

### 分析 notebook 放 `spatial-agent-core/notebooks/`

当前 notebook 已经集中在这里。`assets/` 是静态资产区，不再承担 notebook 角色。

---

## 6. 一个新执行者第一次进项目时，最小闭环应该怎么走

下面这条链路是当前最推荐的“第一次上手流程”。

1. 读 `plan_v7.md`，确认研究问题、主张边界和实验主链。
2. 读 `research_mentorship_guide_v2.md`，确认阶段纪律和推进顺序。
3. 读本文件，确认目录分工和真实路径。
4. 看 `spatial-agent-core/results/preflight/`，确认已有 preflight 产物与当前状态。
5. 看 `spatial-agent-core/configs/experiments/` 与 `spatial-agent-core/experiments/`，确认实验入口。
6. 看 `spatial-agent-core/src/` 与 `tests/`，确认实现主线。
7. 需要写分析时进入 `spatial-agent-core/notebooks/`。
8. 需要整理资料时回到 `assets/papers/`。
9. 需要写说明或计划时回到 `docs/`。

如果你走完这条链路，基本已经具备开始执行 v7 的最小条件。

---

## 7. Setup 完成检查清单

- [ ] 我知道当前唯一主计划是 `docs/plans/plan_v7.md`
- [ ] 我知道 `docs/guides/research_mentorship_guide_v2.md` 负责执行方法，不是目录说明
- [ ] 我知道代码主工程在 `spatial-agent-core/`
- [ ] 我知道论文 PDF、阅读笔记、BibTeX 在 `assets/papers/`
- [ ] 我知道 notebook 在 `spatial-agent-core/notebooks/`
- [ ] 我知道实验结果和 preflight 输出在 `spatial-agent-core/results/`
- [ ] 我知道实验配置在 `spatial-agent-core/configs/`
- [ ] 我知道实验运行入口在 `spatial-agent-core/experiments/`
- [ ] 我知道仓库级说明文档应该写回 `docs/`
- [ ] 我知道运行产物不应该混放到 `docs/` 或 `assets/`

---

## 8. 当前版本最重要的判断

当前仓库不是“准备搭一个项目”，而是“已经有文档、资产、代码、preflight 结果的在研项目”。

所以你的启动心态应该是：

- 先对齐 `v7`
- 再理解当前目录和已有产物
- 再开始补实验、补代码、补分析

如果一上来把它当成空仓库来搭脚手架，很容易把旧路径、旧分工和旧假设重新带回来。
