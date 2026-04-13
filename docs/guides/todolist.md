# SpatialAgent Survey Todo List

> 更新日期：2026-04-13  
> 依据文档：`survey_research_guide.md`、`survey_plan_v4.md`、`coding_manual.md`、`claim_matrix.md`  
> 用途：查看当前 survey 执行进度，明确下一步要做什么

---

## 当前进度总览

### 已完成

- [x] `Phase 0` 基础设施已搭好
- [x] `Phase 0` gate 已正式确认关闭
- [x] `survey_plan_v4.md` 已定稿进入执行状态
- [x] `spatial-agent-survey/` 子项目骨架已建立
- [x] `guide`、`survey_paper` 工作区与 Phase 1 工作流边界已写清
- [x] `Phase 1` 原始检索池已扩展到 `417` 篇候选
- [x] 第一轮 assistant 预筛已完成，已收敛到 `117` 篇保留池
- [x] `Phase 1` abstract rereview round 1 已人工接受
- [x] 首批高优先级全文 PDF 已落库到 `assets/survey_paper/pdfs/phase1_*`

### 进行中

- [ ] `Phase 1` unresolved 条目复核与 targeted expansion search
- [ ] `Core` 系统的 `system / configuration` 级编码准备

### 未开始

- [ ] `Phase 1` 正式 coding
- [ ] `Phase 2` evidence map / appendix 导出
- [ ] `Phase 3` 正文写作与 claim check

---

## 执行优先级

> 原则：所有任务按“是否解除关键路径阻塞”排序，而不是按“看起来重要”排序。  
> 当前关键路径是：`round 1 接受 -> unresolved resolve / targeted expansion -> Core corpus 稳定 -> system-level coding -> analysis/export -> manuscript`

### Priority 0：当前唯一主线

- [ ] 处理 `3` 个 `hold_ambiguous_space` 的全文复核
- [ ] 处理 `8` 个 `hold_missing_abstract` 的补全文/补元数据
- [ ] 决定 round 1 结果是否直接转成正式 `screening_sheet`
- [ ] 发起一轮 targeted expansion search，补强 `Core`

说明：
当前最大的风险不是“没做第一轮筛选”，而是 `Core` 可能收得过窄。要先判断这是字段真实稀缺，还是检索覆盖还不够。

### Priority 1：紧跟在 P0 后面

- [ ] 根据 accepted round 1，把 `36 adjacent` 再压缩到真正服务“空间能力边界”的集合
- [ ] 根据 accepted round 1，把 `45 foundational` 再压缩到最小桥接理论集
- [ ] 生成 `exclusion_recheck_sample` 并进入二次复核
- [ ] 确认高优先级 `Core` 论文 PDF 已齐全

说明：
这一层的目标不是扩库，而是把 `Phase 1` 从“assistant prescreen”变成“人工确认后的正式语料表”。

### Priority 2：Phase 1.5 编码准备

- [ ] 从已确认的 `Core` 论文中提取 `system family`
- [ ] 按 `system / environment configuration` 拆分编码单位
- [ ] 建立第一版 `systems_master`
- [ ] 建立第一版 `core_evidence`
- [ ] 为 `merge / split` 决策建立真实日志

说明：
只有在 `Core` 语料稳定之后，这一层的表才值得建立，否则会反复返工。

### Priority 3：延后启动

- [ ] `Phase 2` evidence map / appendix 导出
- [ ] `Phase 3` 正文写作与 claim check

说明：
这两层必须建立在已验证的 `Core` 和 `Adjacent` 编码结果之上，当前不属于主攻方向。

---

## Phase 0：基础设施与协议

### 状态

- [x] 完成

### 已完成项

- [x] `survey_research_guide.md`
- [x] `survey_plan_v4.md`
- [x] `coding_manual.md`
- [x] `claim_matrix.md`
- [x] `spatial-agent-survey/` 目录与基础脚本
- [x] Phase 0 seed corpus 脚本和模板产物
- [x] `Phase 0 readiness checklist`
- [x] pilot taxonomy validation 相关 appendix 草案

### 仍需确认

- [x] 3 个 pilot 系统的最终人工编码结果已形成最小落表
- [x] `Adjudication memo` 已进入正式持续维护状态
- [x] `taxonomy_change_log` 已开始按真实案例记录

说明：
上面三项原本是 `Phase 0` gate 中最后还停留在“待确认”的部分；截至 2026-04-13，现已补齐并确认 `Phase 0` 完成。当前真正的大规模执行瓶颈已经转移到 `Phase 1` 的人工预筛。

---

## Phase 1：检索、预筛、分层

### 状态

- [ ] 进行中

### 已完成项

- [x] `assets/survey_paper/phase1/phase1_search_log.md`
- [x] `assets/survey_paper/phase1/phase1_paper_list.md`
- [x] `assets/survey_paper/phase1/phase1_candidate_pool_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_screening_backlog_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_assistant_prescreen_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_prescreen_keep_pool_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_manual_tier_review_sheet_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_manual_tier_review_sheet_summary.md`
- [x] `assets/survey_paper/phase1/phase1_abstract_rereview_round1_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_abstract_rereview_round1_summary.md`
- [x] `assets/survey_paper/phase1/phase1_candidate_pool_summary.md`
- [x] `assets/survey_paper/phase1/phase1_assistant_prescreen_summary.md`
- [x] `spatial-agent-survey/data/raw/phase1_a_openalex_2026-04-13.jsonl`
- [x] `spatial-agent-survey/data/raw/phase1_b_openalex_2026-04-13.jsonl`
- [x] `spatial-agent-survey/data/raw/phase1_c_openalex_2026-04-13.jsonl`
- [x] `spatial-agent-survey/data/raw/phase1_d_openalex_2026-04-13.jsonl`
- [x] `spatial-agent-survey/data/raw/phase1_e_openalex_2026-04-13.jsonl`
- [x] `spatial-agent-survey/data/raw/phase1_search_seed_2026-04-13.jsonl`
- [x] `spatial-agent-survey/data/processed/papers_master_phase1_2026-04-13.csv`
- [x] `spatial-agent-survey/data/processed/screening_sheet_phase1_2026-04-13.csv`
- [x] `spatial-agent-survey/results/logs/phase1_openalex_pool_summary.json`

### 当前数字

- [x] OpenAlex family 内去重后：`397`
- [x] 加入 seed batch 后 raw ingestion：`449`
- [x] 全局去重后 candidate pool：`417`
- [x] assistant first-pass 保留池：`117`
- [x] 保留池分布：`21 core / 43 adjacent / 53 foundational`
- [x] accepted `abstract rereview round 1` 推荐分布：`11 core / 36 adjacent / 45 foundational / 25 excluded`
- [x] unresolved：`3 hold_ambiguous_space + 8 hold_missing_abstract`

### 下一步必须做的事

- [ ] 先处理 `3` 个 `hold_ambiguous_space`：`OASIS / SoMoSiMu / Multimodal Safety Evaluation`
- [ ] 再处理 `8` 个 `hold_missing_abstract`
- [ ] 决定 `11 core` 是否直接作为首版 confirmed core 集
- [ ] 发起 targeted expansion search，目标是补出更多“明确有空间环境 + 社会行为”的 `Core`
- [ ] 对 accepted 排除项补正式 `E1-E5`
- [ ] 产出 accepted round 1 对应的 `screening_sheet` 正式版
- [ ] 生成 `exclusion_recheck_sample`，进入二次复核流程

### 这一阶段的完成标准

- [ ] `papers_master` 正式稳定
- [ ] `screening_sheet` 有完整排除原因
- [ ] `Core / Adjacent / Foundational / Excluded` 全量定稿
- [ ] 可以从正式筛选结果进入 `system-level coding`

---

## Phase 1.5：系统级编码准备

### 状态

- [ ] 尚未正式开始

### 已有基础

- [x] `systems_master_template.csv`
- [x] `core_evidence_template.csv`
- [x] `adjacent_evidence_template.csv`
- [x] `pilot_systems.csv`

### 下一步

- [ ] 从已确认的 `Core` 论文中提取 system family
- [ ] 按 `system / environment configuration` 拆分编码单位
- [ ] 建立第一版 `systems_master`
- [ ] 建立第一版 `core_evidence`
- [ ] 为 `merge / split` 决策建立真实日志
- [ ] 启动 `Generative Agents / Project Sid / Concordia / OASIS` 的优先编码

---

## Phase 2：分析与导出

### 状态

- [ ] 未开始

### 计划中的关键产物

- [ ] evidence map 大表
- [ ] `agent-accessible repr × behavioral scale × evidence status` 交叉表
- [ ] `environment-side vs agent-accessible` 对照示例表
- [ ] `L4 gap` 统计摘要
- [ ] appendix 完整 evidence table
- [ ] PRISMA-ScR 统计结果正式版

### 进入条件

- [ ] `Core` 正式编码完成
- [ ] `Adjacent` 补充编码完成
- [ ] QC 开始产生真实检查结果

---

## Phase 3：正文写作与论断检查

### 状态

- [ ] 未开始

### 写作前条件

- [ ] `claim_matrix` 逐条可对照执行
- [ ] evidence map 可稳定导出
- [ ] appendix 表可稳定导出
- [ ] `L4 gap` 与 representation gap 统计已经稳定

### 写作顺序提醒

- [ ] 先写 `§3 Evidence Map`
- [ ] 再写 `§5 Space in Social Simulation`
- [ ] 再写 `§4 Feasibility`
- [ ] 最后补 `§1 Introduction` 和 `§8 Conclusion`

---

## 本周优先级

### 1. 先做

- [ ] 全文解决 `3 hold_ambiguous_space`
- [ ] 补齐 `8 hold_missing_abstract`
- [ ] 给 accepted 排除项补 `E1-E5`

### 2. 接着做

- [ ] 产出 accepted round 1 的 `screening_sheet` 正式版
- [ ] 压缩 `36 adjacent`
- [ ] 压缩 `45 foundational`

### 3. 然后再做

- [ ] 发起一轮 targeted expansion search 补强 `Core`
- [ ] 生成 `exclusion_recheck_sample`
- [ ] 确认高优先级 `Core` 论文 PDF 是否齐全
- [ ] 为首批 `Core` 系统建立 `system family` 列表

### 4. 暂不提前启动

- [ ] 大规模 `systems_master / core_evidence` 编码
- [ ] `Phase 2` 图表和 appendix 导出
- [ ] `Phase 3` 正文写作

---

## 风险与提醒

- [ ] 不要把 assistant first-pass 当成最终筛选结果
- [ ] 不要让 `Foundational` 文献无限膨胀
- [ ] 不要把 spatial reasoning benchmark 直接当作 social effect evidence
- [ ] 不要在 `Core` 论文未定稿前开始写 narrative 主文
- [ ] 不要跳过 `E1-E5` 排除原因记录

---

## 如果今天只做一件事

- [ ] 打开 `assets/survey_paper/phase1/phase1_abstract_rereview_round1_2026-04-13.csv`，先解决 `3 hold_ambiguous_space`
