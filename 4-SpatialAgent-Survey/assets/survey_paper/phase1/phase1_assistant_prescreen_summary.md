# Phase 1 Assistant Prescreen Summary

日期：2026-04-13  
阶段：`Phase 1` 标题摘要预筛第一轮（assistant first-pass）

## 1. 输入与输出

输入：

- `phase1_candidate_pool_2026-04-13.csv`：`417` 条候选

输出：

- `phase1_assistant_prescreen_2026-04-13.csv`：对全部 `417` 条给出 first-pass 推荐标签
- `phase1_prescreen_keep_pool_2026-04-13.csv`：按标题去重后的保留池

## 2. 第一轮预筛结果

### 全量 417 条的 assistant 推荐

- `core`: 25
- `adjacent`: 49
- `foundational`: 56
- `excluded`: 287

### 标题去重后的保留池

- 总量：`117`
- `core`: 21
- `adjacent`: 43
- `foundational`: 53

这意味着第一轮预筛已经把广搜池从 `417` 条收敛到 `117` 条，已经进入计划里“约 80-120 篇预筛集”的目标区间边缘。

## 3. 这轮预筛是怎么做的

这是一个可复跑的 assistant first-pass，不是最终人工裁决。它使用了几类规则：

- `seed_anchor`: 直接匹配你已经确认过的高优先级 seed 文献
- `known_core_title`: 匹配明确属于 generative-agent / social-simulation 路线的系统标题
- `llm_social_simulation`: 匹配 LLM / generative AI + social simulation / behavior simulation 系统
- `llm_spatial_reasoning`: 匹配 LLM spatial reasoning / spatially-aware / navigation / geospatial 能力论文
- `space_syntax_bridge`: 匹配 Space Syntax / visibility / spatial configuration 与 movement / social interaction / pedestrian 等桥接论文
- `spatial_cognition_anchor`: 匹配空间认知、空间语言、认知地图等 foundational 背景

## 4. 当前最稳的高优先级保留项

### Core 高优先级

- `Generative Agents`
- `Affordable Generative Agents`
- `Project Sid`
- `Concordia`
- `Artificial Leviathan`
- `OASIS`
- `AgentSociety`
- `TravelAgent`
- `Environment-Aware Spatial Interactions in VR Role-Play`

### Adjacent 高优先级

- `Advancing Spatial Reasoning in Large Language Models`
- `AgentSims`
- `Language Models Represent Space and Time`
- `Reframing Spatial Reasoning Evaluation in Language Models`
- `SARAH`
- `SpatialVLM`
- `When LLMs Recognize Your Space`

### Foundational 高优先级

- `The Social Logic of Space`
- `Space is the Machine`
- `From Isovists to Visibility Graphs`
- `Space Syntax Based Agent Simulation`
- `Integrating Space Syntax with Spatial Interaction`

## 5. 当前仍然需要人工重点复核的部分

### Core 边界

以下条目被 first-pass 保留为 `core`，但仍建议你优先复核是否真的满足“可识别空间环境 + 社会行为耦合”：

- `CharacterEval`
- `Public Health Policy / Vaccine Hesitancy` 一类 generative-agent case study
- `Social Engineering Attacks` 一类行为模拟条目

### Adjacent 边界

`adjacent` 里目前仍有一些“空间能力很强，但与本文主线距离较远”的条目，后续可能继续收缩：

- geospatial / GIS assistant
- drone / inspection / UAV
- object navigation / VLN

### Foundational 边界

`foundational` 里目前还保留了一些空间认知与空间语言背景文献；下一轮人工筛选时，可能继续把它们分成：

- 应保留的理论锚点
- 可删去的广义背景项

## 6. 推荐的下一步

1. 先从 `phase1_prescreen_keep_pool_2026-04-13.csv` 开始人工复核，而不是再从 417 条重头看。
2. 优先人工确认 `21 core` 是否应继续收缩到更稳的 `20-30` 个系统论文。
3. 再人工压缩 `43 adjacent`，把真正需要的空间能力边界论文收缩到约 `15-25`。
4. 最后从 `53 foundational` 中保留最能支撑 §2 和 bridging narrative 的 `10-20` 条。

## 7. 对应文件

- [phase1_assistant_prescreen_2026-04-13.csv](./phase1_assistant_prescreen_2026-04-13.csv)
- [phase1_prescreen_keep_pool_2026-04-13.csv](./phase1_prescreen_keep_pool_2026-04-13.csv)
- [phase1_assistant_prescreen_summary_2026-04-13.json](./phase1_assistant_prescreen_summary_2026-04-13.json)
