# Phase 1 检索日志

日期：2026-04-13  
阶段：`Phase 1` 初始检索批次（v0）  
对应主计划：`docs/plans/survey_plan_v4.md §2.3`

## 0. 当前状态快照

截至 2026-04-13，本轮 `Phase 1` 宽搜已经形成：

- OpenAlex 宽搜原始返回：`400` 条
- OpenAlex family 内去重后：`397` 条
- 加上人工 seed batch 后，raw ingestion 总量：`449` 条
- 跨 family + seed 全局去重后：`417` 条

已生成的核心快照：

- `assets/survey_paper/phase1/phase1_candidate_pool_2026-04-13.csv`
- `assets/survey_paper/phase1/phase1_screening_backlog_2026-04-13.csv`
- `spatial-agent-survey/data/processed/papers_master_phase1_2026-04-13.csv`
- `spatial-agent-survey/data/processed/screening_sheet_phase1_2026-04-13.csv`
- `spatial-agent-survey/results/logs/phase1_openalex_pool_summary.json`

## 1. 本轮目标

本轮不是做最终纳入判定，而是先完成三件事：

1. 依据 `survey_plan_v4.md` 的 5 族 query 建出第一批可操作 paper list。
2. 优先把开放获取全文落到 `assets/survey_paper/pdfs/phase1_*`。
3. 把同一批条目同步为 `spatial-agent-survey/data/raw/phase1_search_seed_2026-04-13.jsonl`，为后续 ingest / dedupe / screening 做准备。

## 2. 本轮使用的数据源

- Semantic Scholar：用于宽搜标题与相近条目
- Google Scholar：用于补漏和定位 publisher page
- ACL Anthology：用于 ACL / Findings / NAACL 论文
- arXiv：用于 LLM agent、spatial reasoning、simulation 预印本
- IJCAI Proceedings：用于空间推理 benchmark / evaluation
- UCL Discovery：用于 Space Syntax / ABM foundational 文献
- 官方 DOI / 出版页：用于补足无 arXiv 的元数据

## 3. 直接沿用的 Query Families

| Family | Query | 目标 corpus |
|---|---|---|
| A | `"space syntax" AND ("agent" OR "LLM" OR "language model" OR "simulation")` | Core / Foundational |
| B | `"spatial representation" AND "multi-agent" AND ("social" OR "behavior")` | Core |
| C | `"spatial reasoning" AND ("large language model" OR "LLM" OR "GPT")` | Adjacent |
| D | `("generative agents" OR "LLM agent" OR "language agent") AND ("social simulation" OR "emergent behavior" OR "multi-agent" OR "sandbox" OR "virtual world" OR "NPC" OR "interactive simulacra" OR "social agent")` | Core |
| E | `"spatial configuration" AND ("social behavior" OR "movement" OR "interaction")` | Foundational |

## 4. 本轮筛入规则

- 优先开放获取全文；没有 open PDF 的条目先保留元数据，不阻塞整体推进。
- 优先能帮助判定以下问题的论文：
  - Agent 实际可访问的空间表征层级是什么
  - 空间环境是否与社会行为生成发生耦合
  - Space Syntax / configurational claims 能否为 research agenda 提供桥接
- 同一家族系统先保留代表版本，后续在 `systems_master` 阶段再做 `merge / split`。
- 这批 list 的 `tier guess` 只是工作假设，不是最终纳入结果。

## 5. Family -> 当前命中条目

### A. Space Syntax + AI

- `Space Syntax Based Agent Simulation`
- `Assisted Agent-Based Simulations`
- `Integrating Space Syntax with Spatial Interaction: The Spatial Metrics Problem`

### B. Spatial Representation + Agent + Social / Behavior

- `Generative Agents`
- `Affordable Generative Agents`
- `Concordia`
- `Project Sid`

### C. LLM Spatial Reasoning

- `SARAH`
- `Advancing Spatial Reasoning in Large Language Models`
- `SpatialVLM`
- `Reframing Spatial Reasoning Evaluation in Language Models`
- `Language Models Represent Space and Time`
- `When LLMs Recognize Your Space`

### D. LLM Social Simulation

- `Generative Agents`
- `Project Sid`
- `Artificial Leviathan`
- `OASIS`
- `AgentSociety`
- `Unveiling the Truth and Facilitating Change: Towards Agent-based Large-scale Social Movement Simulation`
- `AgentSims`

### E. Spatial Configuration + Social Behavior / Movement / Interaction

- `The Social Logic of Space`
- `From Isovists to Visibility Graphs`
- `Space is the Machine`
- `Integrating Space Syntax with Spatial Interaction: The Spatial Metrics Problem`

## 6. 当前批次产物

### 已写入的工作文件

- `assets/survey_paper/phase1/phase1_paper_list.md`
- `assets/survey_paper/phase1/phase1_candidate_pool_2026-04-13.csv`
- `assets/survey_paper/phase1/phase1_screening_backlog_2026-04-13.csv`
- `spatial-agent-survey/data/raw/phase1_search_seed_2026-04-13.jsonl`
- `spatial-agent-survey/data/raw/phase1_a_openalex_2026-04-13.jsonl`
- `spatial-agent-survey/data/raw/phase1_b_openalex_2026-04-13.jsonl`
- `spatial-agent-survey/data/raw/phase1_c_openalex_2026-04-13.jsonl`
- `spatial-agent-survey/data/raw/phase1_d_openalex_2026-04-13.jsonl`
- `spatial-agent-survey/data/raw/phase1_e_openalex_2026-04-13.jsonl`

### 已落库的全文 PDF

- `Core`: 8 篇
- `Adjacent`: 6 篇
- `Foundational`: 5 篇

### 宽搜 candidate pool 计数

- `A / Space Syntax + AI`: 82
- `B / Spatial Representation + Agent`: 72
- `C / LLM Spatial Reasoning`: 88
- `D / LLM Social Simulation`: 89
- `E / Spatial Cognition + Computation`: 97
- `seed batch`: 21
- 全局去重后 candidate pool: 417

### 当前只保留元数据的条目

- `When LLMs Recognize Your Space`
- `The Social Logic of Space`

原因：

- 前者当前优先使用 DOI / 发表页做记录，待确认是否存在可公开预印本。
- 后者是核心书籍来源，当前以 DOI 和既有阅读笔记支撑，不强制复制整本书 PDF。

## 7. 本轮注意事项

- `Concordia` 的 arXiv API 元数据写明为 32 页，但本地文件类型工具没有给出稳定页数；当前已确认其为有效 PDF，可先进入筛选批次，后续如有需要再做全文页数复核。
- `SoMoSiMu`、`OASIS`、`AgentSociety` 这类数字社会 / 平台社会模拟条目是否归入 `Core`，后续仍要按“是否存在可识别空间环境、是否与社会行为耦合”做严格判定。
- 本批次故意同时保留 `Core / Adjacent / Foundational`，是为了让 `Phase 1` 的 screening sheet 从一开始就有分层结构，而不是先搜一坨再临时分类。

## 8. 下一步

1. 用 `phase1_search_seed_2026-04-13.jsonl` 跑 `ingest_search_results.py`。
2. 跑去重和 screening 输入生成。
3. 在 `screening_sheet.csv` 中完成 `core / adjacent / foundational / excluded` 的正式筛选。
4. 对 `Generative Agents / Project Sid / Concordia / OASIS` 优先做 system-level 预判，准备后续 coding。
