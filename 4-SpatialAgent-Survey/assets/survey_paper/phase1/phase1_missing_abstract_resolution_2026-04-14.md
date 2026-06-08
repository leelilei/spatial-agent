# Phase 1 Missing-Abstract Resolution

日期：2026-04-14  
对象：`phase1_abstract_rereview_round1_2026-04-13.csv` 中原 `hold_missing_abstract` 的 8 个条目  
目的：把“缺摘要但已可判定”的条目一次性收口，避免后续正式 `screening_sheet` 再被同一问题阻塞。

---

## 裁定结果总览

### 保留

- `Reasoning Paths with Reference Objects Elicit Quantitative Spatial Reasoning in Large Vision-Language Models`
  - `adjacent`
  - 理由：官方摘要明确它是 quantitative spatial reasoning benchmark，直接服务空间输入处理能力边界。

- `Space is the Machine: A Configurational Theory of Architecture`
  - `foundational`
  - 理由：虽缺标准摘要，但本地 PDF、survey plan 与 reference index 已一致把它作为 Space Syntax 扩展理论主锚点。

- `The Social Logic of Space`
  - `foundational`
  - 理由：虽缺标准摘要，但本地阅读笔记与计划文档已确认其为 Space Syntax 经典理论锚点。

- `Social networks and spatial configuration—How office layouts drive social interaction`
  - `foundational`
  - 理由：摘要直接讨论 office layout 的 configurational measures 如何影响社会互动，是本文需要的空间构型-社会互动桥接证据。

- `The Relationship between Spatial Configuration and Social Interaction in Tehran Residential Areas: Bridging the Space Syntax Theory and Behavior Settings Theory`
  - `foundational`
  - 理由：补到的摘要直接围绕 residential layout、Space Syntax 与 social interaction 的关系展开。

- `Using space syntax and agent-based approaches for modeling pedestrian volume at the urban scale`
  - `foundational`
  - 理由：摘要明确属于 space syntax 与经典 ABM / movement modeling 的方法桥梁。

### 排除

- `Agent-Based Modelling Meets Generative AI in Social Network Simulations`
  - `excluded`
  - `E1`
  - 理由：补到的摘要主要是社交网络用户仿真、内容转发与推荐机制，仍没有足够证据证明存在可识别空间环境或 agent-facing 空间结构。

- `Building Problem Spaces for Deaf and Hard of Hearing Students’ Spatial Cognition in a Programming Language`
  - `excluded`
  - `E2`
  - 理由：现有元数据只支持它是空间认知教育研究，不直接服务本文需要的社会行为或 Space Syntax 桥接。

---

## 使用的补充来源

对缺摘要但可在线确认的条目，优先参考官方或出版方页面：

- ACL Anthology / EMNLP proceedings
- Springer / DOI landing page
- ScienceDirect / journal abstract page
- DOAJ / publisher abstract page

对无法补到标准摘要、但在本仓库中已被反复作为主锚点使用的书籍条目，则依据以下本地材料保留：

- `assets/papers/reading_notes/hillier1984_social_logic_of_space.md`
- `docs/plans/survey_plan_v4.md`
- `docs/project/reference_index.md`
- `assets/survey_paper/phase1/phase1_paper_list.md`

---

## 对当前统计的影响

- `hold_missing_abstract` 已从 `8` 降为 `0`
- 当前 `R1` 统计变为：`87 keep / 1 downgrade / 29 exclude`
- 当前 `R1` 推荐层级变为：`8 core / 36 adjacent / 44 foundational / 29 excluded`

---

## 下一步

- 将 `R1` 结果同步进正式 `screening_sheet`
- 给所有 `excluded` 条目补齐最终 `E1-E5`
- 基于当前 `8 core` 启动首版 confirmed core 集检查与 targeted expansion search
