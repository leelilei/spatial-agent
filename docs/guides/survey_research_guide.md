# SpatialAgent Survey 研究执行指南

> 适用对象：当前仓库中负责推进 survey 论文的研究执行者  
> 当前主计划：`../plans/survey_plan_v4.md`  
> 编码执行手册：`../plans/coding_manual.md`  
> 论断约束矩阵：`../plans/claim_matrix.md`  
> 代码工作区：`../../spatial-agent-survey/`  
> 文档目标：把 survey 计划转成一套可日常执行、可检查、可交付的研究工作流

---

## 如何使用本手册

- 通读模式：先从第 1 节读到第 6 节，建立 survey 的完整推进框架。
- 执行模式：实际工作时，按“阶段目标 -> 当周任务 -> 输出物 -> 通过标准”逐段对照。
- 冲突处理：如果旧版想法、临时直觉和 `survey_plan_v4.md` 冲突，以 `v4`、`coding_manual.md`、`claim_matrix.md` 为准。
- 一句话版核心策略：先完成 `Phase 0` 的 protocol、coding manual、claim matrix 和 pilot coding，再进入大规模编码；全文写作始终由 evidence table 和 claim matrix 双重约束。

这篇 survey 不是一篇“先写 narrative、后补文献”的文章。它是一篇以 `evidence map` 为中心的 scoping review，研究工作流必须先有 `corpus`、`coding` 和 `claim discipline`，再有正文。

---

## 1. 先搞清楚这四份核心文件的分工

### `docs/plans/survey_plan_v4.md`

这是当前唯一有效的 survey 主计划。它回答：

- 这篇 survey 到底研究什么
- 为什么它是 `scoping review + structured research agenda`
- `Core / Adjacent / Foundational` 三类 corpus 各自承担什么角色
- `L0-L5` taxonomy 如何定义
- 每个阶段的交付、门槛和时间线是什么

如果你对“这篇文章想回答什么”有疑问，先回到这里，不要先改代码。

### `docs/plans/coding_manual.md`

这是 survey 的方法执行规则。它回答：

- `paper` 和 `system / environment configuration` 的分析单位怎么区分
- 什么时候 `merge`、什么时候 `split`
- `environment-side` 和 `agent-accessible` 怎么分别编码
- `L0-L5` 怎么判定
- 模糊案例怎么进入 `adjudication_memo`
- 二次复核、audit、taxonomy versioning 的阈值是什么

如果你已经知道要做 survey，但不知道“具体怎么编码”，看这份。

### `docs/plans/claim_matrix.md`

这是正文写作的“论断强度刹车系统”。它回答：

- 哪种证据允许支撑哪种 claim
- `observed_effect / designed_affordance_only / hypothesized_but_not_tested` 的论断上限分别是什么
- `Core / Adjacent / Foundational` 各能支持什么、不能支持什么
- 哪些句子属于可以写，哪些属于过度外推

如果你在写 evidence map、discussion 或 agenda 时不确定一句话会不会说过头，先查这份。

### `spatial-agent-survey/`

这是 survey 的可运行工作区。它负责：

- 检索结果导入
- 去重与 screening sheet 生成
- system-level coding 模板
- QC 和导出
- 长版综述正文与 appendix 组装

它不是仓库级文档目录，也不是实验论文代码目录。

---

## 2. 当前 survey 资产到底放在哪里

### `docs/plans/`

放计划、review、manual、claim matrix 这些规则性文件。

和 survey 直接相关的核心文件：

- `survey_plan_v4.md`
- `coding_manual.md`
- `claim_matrix.md`

### `docs/reviews/`

放版本 review。当前和 survey 直接相关的是：

- `survey_plan_v2_r1.md`
- `survey_plan_v3_r1.md`
- `survey_plan_v4_r1.md`

如果你需要知道“为什么现在的规则长这样”，回看这些 review。

### `assets/papers/`

放长期保存的论文资产：

- `pdfs/`: 论文 PDF
- `reading_notes/`: 阅读笔记
- `generated/`: 自动生成的 paper lists、BibTeX、状态文件

这部分是 survey 的资料源，但不是代码工作区。

### `assets/survey_paper/`

放 survey 论文自身的工作资产，尤其是：

- 相近 survey / scoping review 参考文献
- `Phase 1` 检索日志、paper list 和批次下载记录
- 为当前综述临时整理的 PDF 子集与筛选工作文件

建议把它理解成“论文写作侧的研究素材库”。它和 `assets/papers/` 的区别是：

- `assets/papers/` 偏长期、全局、可复用的论文资产
- `assets/survey_paper/` 偏当前这篇综述的专题工作集

### `spatial-agent-survey/`

这是 survey 的执行子项目。建议把它理解成：

- `data/raw/`: 原始检索结果、手工筛选输入、audit 原始记录
- `data/processed/`: `papers_master`、`systems_master`、`core_evidence`、`adjacent_evidence` 等规范化表
- `scripts/`: 半自动流水线入口
- `results/`: evidence map、PRISMA 统计、L4 gap summary、representation gap 例表
- `paper/`: 长版综述章节、appendix、图表和表格

一句话理解：`docs/` 回答“为什么与怎么做”，`assets/` 提供资料，`spatial-agent-survey/` 真正负责 survey 执行。

---

## 3. 按正确顺序推进，不要直接开始写正文

Survey 的推进顺序建议固定为：

1. 锁定方法规则
2. 跑通检索与 screening workflow
3. 完成 pilot coding
4. 才进入大规模编码
5. 先导 evidence map 和 appendix 表
6. 最后写正文

不要反过来。尤其不要：

- 先写一版 narrative 再找文献补
- 还没完成 `claim_matrix` 就开始写“空间如何影响社会行为”
- 还没稳定 `L0-L5` 的边界，就在正文中下 taxonomy 结论

---

## 4. 分阶段执行指南

### Phase 0：Protocol 与编码基础设施

目标：在任何大规模文献编码之前，先把规则写稳。

这阶段必须完成：

- `survey_plan_v4.md`
- `coding_manual.md`
- `claim_matrix.md`
- `spatial-agent-survey/` 的基本流水线
- 至少 3 个 pilot 系统的 coding

当前建议的 pilot 系统：

- `Generative Agents`
- `Project Sid`
- `SARAH`

这一步的关键不是“编码更多”，而是检查三个问题：

1. `L0-L5` 是否真的可判定
2. `environment-side` 和 `agent-accessible` 是否能被稳定区分
3. `observed_effect` 和 `designed_affordance_only` 是否会被混淆

通过标准：

- [ ] `coding_manual.md` 已完成
- [ ] `claim_matrix.md` 已完成
- [ ] 3 个 pilot 系统可完整编码
- [ ] 如果 pilot 中有 2 个及以上无法稳定归类，暂停进入 Phase 1，先修 manual

### Phase 1：检索、筛选、分层、编码

目标：得到可用于 evidence map 的主表，而不是“搜到一些论文”。

实际顺序：

0. 先在 `assets/survey_paper/phase1/` 建本轮检索日志和 `paper list`
1. 将检索结果放入 `spatial-agent-survey/data/raw/`
2. 运行导入脚本
3. 去重
4. 生成 screening sheet
5. 完成人工筛选
6. 标注 `Core / Adjacent / Foundational / Excluded`
7. 生成 system-level coding 模板
8. 对 `Core` 做主编码，对 `Adjacent` 做补充编码
9. 跑 QC

这阶段最重要的不是数量，而是分层与单位正确。

必须持续记住：

- `Core` 才是 evidence map 的主对象
- `Adjacent` 只服务“可行性边界”
- `Foundational` 只服务“理论背景与可迁移命题”
- `assets/survey_paper/phase1/phase1_search_log.md` 记录“怎么搜到这些论文”
- `assets/survey_paper/phase1/phase1_paper_list.md` 记录“为什么它们进入当前工作集”
- `assets/survey_paper/pdfs/phase1_core|adjacent|foundational/` 只放 Phase 1 直接需要的 PDF，不要求复制整个长期文献库

通过标准：

- [ ] `papers_master` 已稳定
- [ ] `screening_sheet` 有完整的排除原因
- [ ] `systems_master` 按 `system / configuration` 编码，而不是按整篇论文编码
- [ ] `core_evidence` 已形成
- [ ] 二次复核和 external audit 已记录

### Phase 2：分析、导出与 appendix

目标：先把论文真正依赖的图表和表格导出来。

这阶段优先产出：

- evidence map 大表
- `agent-accessible repr × behavioral scale × evidence status` 交叉表
- `environment-side vs agent-accessible` 对照示例
- `L4 gap` 统计摘要
- appendix evidence table
- PRISMA-ScR 统计摘要

写作顺序必须服从分析产物，而不是相反。

建议正文写作顺序：

1. `§3 Evidence Map`
2. `§5 Space in Social Simulation`
3. `§4 Feasibility`
4. `§2 Space Syntax Primer`
5. `§6 Evaluation`
6. `§7 Agenda`
7. `§1 Introduction`
8. `§8 Conclusion`

### Phase 3：正文与论断检查

目标：把长版综述写成一篇“每句话都能追溯到证据类型”的论文。

这一阶段最关键的动作不是润色，而是 claim check。

每写完一个 section，都要逐条检查：

1. 这句话是在描述文献分布，还是在声称空间 effect？
2. 如果是 effect claim，它是不是只建立在 `observed_effect` 条目上？
3. 这句话依赖的是 `Core`、`Adjacent` 还是 `Foundational`？
4. 我是否把物理空间实证误写成了对 LLM multi-agent 的直接证据？
5. 如果把句子里的 `suggests / may / appears` 换成 `shows / proves / demonstrates`，会不会过强？

只要答案是“会”，这句话就应该回改。

---

## 5. survey 子项目的日常操作顺序

在真正把文件送进 `spatial-agent-survey/` 之前，先在 `assets/survey_paper/` 维护一层研究工作台：

- `phase1/phase1_search_log.md`: 检索日期、数据库、query family、补搜说明
- `phase1/phase1_paper_list.md`: 当前批次候选论文、tier 判断、相关性备注、PDF 落库状态
- `pdfs/phase1_core/`
- `pdfs/phase1_adjacent/`
- `pdfs/phase1_foundational/`

推荐工作顺序是：先在 `survey_paper` 整理“当前批次要处理什么”，再把结构化输入同步到 `spatial-agent-survey/data/raw/`。

在 `spatial-agent-survey/` 下，默认工作顺序如下：

### 第一步：准备原始检索结果

将不同来源的检索结果整理成 `jsonl`，放入：

- `data/raw/`

每个文件建议对应一个 query family 或一个来源批次。

建议命名：

- `data/raw/phase1_search_seed_YYYY-MM-DD.jsonl`
- `data/raw/phase1_query_family_d_YYYY-MM-DD.jsonl`

`jsonl` 中至少保留这些字段：

- `title`
- `abstract`
- `year`
- `venue`
- `url`
- `authors`
- `query_family`
- `corpus_tier_guess`
- `search_batch`

### 第二步：导入与去重

运行：

- `scripts/ingest_search_results.py`
- `scripts/dedupe_papers.py`

产物：

- `data/processed/papers_master_raw.csv`
- `data/processed/papers_master.csv`
- `data/processed/paper_duplicates.csv`

### 第三步：生成 screening 输入

运行：

- `scripts/screen_prepare_inputs.py`

产物：

- `data/processed/screening_sheet.csv`
- `data/processed/exclusion_recheck_sample.csv`
- `results/logs/prisma_summary.json`

### 第四步：完成人工筛选与 corpus 分层

这是人工主导步骤。你要在 `screening_sheet.csv` 里完成：

- `final_status`
- `corpus_tier`
- `exclusion_reason`
- 必要的 `notes`

### 第五步：生成 coding 模板与 pilot

运行：

- `scripts/code_prepare_pilot.py`

产物：

- `systems_master_template.csv`
- `core_evidence_template.csv`
- `adjacent_evidence_template.csv`
- `pilot_systems.csv`
- appendix 模板文件

### 第六步：QC 与导出

运行：

- `scripts/qc_validate_evidence.py`
- `scripts/export_evidence_assets.py`

产物：

- `results/logs/qc_summary.json`
- `results/tables/evidence_map.csv`
- `results/tables/evidence_map.md`
- `results/tables/representation_gap_examples.csv`
- `results/logs/l4_gap_summary.json`

---

## 6. 每周应该交付什么

### Week 1

重点：

- 读 Anchor Papers
- 完成 `coding_manual` 和 `claim_matrix`
- 对 3 个 pilot 系统做 coding

必须有的输出：

- `coding_manual.md`
- `claim_matrix.md`
- 3 个 pilot system 编码结果

### Week 2

重点：

- 真正执行 5 族检索
- 建出 `papers_master`
- 完成 `screening_sheet`

必须有的输出：

- `assets/survey_paper/phase1/phase1_search_log.md`
- `assets/survey_paper/phase1/phase1_paper_list.md`
- `papers_master.csv`
- `screening_sheet.csv`
- 初版 `prisma_summary.json`

执行提醒：

- 5 族 query 直接沿用 `survey_plan_v4.md §2.3`
- 先把首批可获取全文的论文落到 `assets/survey_paper/pdfs/phase1_*`
- 再同步元数据到 `spatial-agent-survey/data/raw/`

### Week 3-4

重点：

- 完成 `Core / Adjacent / Foundational` 分层
- 形成 `systems_master` 与 `core_evidence`
- 完成 QC

必须有的输出：

- `core_evidence`
- `adjacent_evidence`
- `adjudication_memo`
- `taxonomy_change_log`
- `qc_summary.json`

### Week 5 之后

重点：

- evidence map 和 appendix 表先行
- 再开始长版综述正文写作

必须有的输出：

- evidence map 大表
- L4 gap 统计摘要
- appendix evidence table
- section drafts

---

## 7. 最容易犯的 10 个错误

1. 把 `Foundational` 文献写成对 LLM multi-agent 的直接证据。
2. 把 `Adjacent` benchmark 写成“已经证明空间会影响社会行为”。
3. 把 `L4 gap` 写成“L4 无效”，而不是“当前实现覆盖稀缺”。
4. 把 system family 直接按最新版折叠，抹掉关键表示差异。
5. 因为系统是 3D，就草率标记 `L5`。
6. 把 `designed_affordance_only` 当成 `observed_effect`。
7. 还没过 Phase 0 gate，就急着开始大规模编码。
8. 正文先写观点，再回头找证据补。
9. 把 short paper 当成独立产线重跑一套说法。
10. 让 taxonomy 的边界变化只留在脑子里，不进 `taxonomy_change_log`。

---

## 8. 完成标准：什么时候这篇 survey 才算“真的进入写作阶段”

只有当以下条件同时成立，才算真正进入写作阶段，而不是“边查边写”：

- [ ] `survey_plan_v4.md` 已稳定
- [ ] `coding_manual.md` 已稳定
- [ ] `claim_matrix.md` 已稳定
- [ ] pilot coding 已完成
- [ ] `papers_master` 已成型
- [ ] `Core / Adjacent / Foundational` 已完成分层
- [ ] `core_evidence` 已完成主编码
- [ ] `adjudication_memo` 和 `taxonomy_change_log` 已经开始记录
- [ ] QC 通过
- [ ] evidence map 与 appendix 主表已可导出

只要其中任何一项缺失，正文都应该被视为“草稿探索”，不能当成正式写作。

---

## 9. 推荐的实际阅读与执行顺序

如果今天是第一次正式进入这条 survey 线，按下面顺序即可：

1. `docs/plans/survey_plan_v4.md`
2. `docs/plans/coding_manual.md`
3. `docs/plans/claim_matrix.md`
4. 本文件 `survey_research_guide.md`
5. `spatial-agent-survey/README.md`
6. `spatial-agent-survey/scripts/`
7. `spatial-agent-survey/tests/`

如果今天已经在执行中，按下面顺序工作：

1. 看 `Week` 目标
2. 运行对应脚本
3. 更新 `screening_sheet / core_evidence / audit` 产物
4. 运行 QC
5. 导出结果
6. 再写对应 section

这篇 survey 的主线不是“写得快”，而是“证据结构足够稳，稳到后续 short paper 只需要提炼，不需要重做”。
