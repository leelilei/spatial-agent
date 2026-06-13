# 1-SpatialAgent Todo List

> 更新日期：2026-06-14
> 当前主线：Phase 1 — 把预实验与模型门控对齐到 v14-A 重构后的 framing，再进入受控环境构建

> 说明：本清单基于实证 SpatialAgent 的真实进度整理。
> 已完成项有 preflight 报告 / 代码 / 计划文档佐证；未完成项取自当前计划
> docs/plans/proposal.md（= 原 plan v14-A），请据实核对优先级。
> survey 工作已迁至 4-SpatialAgent-Survey，不在本项目范围。

---

## 0. 当前位置

研究 framing 已在 v14-A 完成重构：核心主张从「LLM agent 是否使用 space syntax」改为
「LLM 多智能体能否把**受控环境结构**转化为可测的涌现对话网络」，space syntax/图指标
仅作研究者侧的设计与测量工具，不作为 agent 的认知表征。目标会议 AAAI / AAMAS 主会。

工程侧已具备在线 preflight 编排（`run_preflight.py` + `configs/experiments/preflight_v7.yaml`），
并完成 gpt-5.4 的 20 轮核心门控测试。下一步真正的主线是：把预实验任务从重构前的 v7
对齐到 v14-A 的环境-结构 framing，再开始构建受控环境与对照条件。

---

## 1. Phase 0 — 研究框架与版本治理

- [x] 完成 v14-A 概念重构（环境结构 vs space syntax 认知）
- [x] 确定目标会议方向（AAAI / AAMAS 主会）
- [x] 按规范收敛计划版本：当前版 = proposal.md，历史版进 docs/plans/archive/

## 2. Phase 1 — 预实验与模型门控

- [x] 模型选型（见 docs/project/001_model_selection.md，gpt-5.4 可用）
- [x] 搭建在线 preflight 编排脚本与配置
- [x] 完成 gpt-5.4 的 20 轮核心门控（comprehension / behavioral_inference / prompt_position）
- [x] 确定默认 prompt 位置为 system_prefix（14/20）
- [ ] 把 preflight 任务从 v7 对齐到 v14-A 的环境-结构 framing
- [ ] 补齐扩展项的 20 轮重复（reverse_inference_audit / lexical_norming / coding_pilot_llm）

## 3. Phase 2 — 受控环境与对照条件构建

- [ ] 构建 matched graph-based 环境，计算研究者侧空间指标（integration / depth / betweenness 等）
- [ ] 实现信息量对照（information-volume control）
- [ ] 实现 shuffled mapping 对照
- [ ] 实现共现暴露对照（co-occurrence exposure control）

## 4. Phase 3 — 对话网络与机制识别

- [ ] 规则化事件抽取与对话网络构建
- [ ] QAP / run-level dyadic 分析
- [ ] 引入 null models 与 downgrade rules

## 5. Phase 4 — Stage 1 pilot 与主实验

- [ ] 小规模 pilot 判定主实验是否值得扩展
- [ ] 跑出主实验对话网络结果与对照对比

## 6. Phase 5 — 分析与论文写作

- [ ] 主结果与机制识别分析
- [ ] 撰写面向 AAAI / AAMAS 的论文 draft

---

## 执行优先级

### Priority 0：对齐 v14-A 的预实验

- [ ] 把 preflight 任务从 v7 对齐到 v14-A 的环境-结构 framing
- [ ] 补齐扩展项的 20 轮重复

### Priority 1：构建受控环境与对照

- [ ] matched graph 环境 + 研究者侧空间指标
- [ ] 三类对照（信息量 / shuffled mapping / 共现暴露）

### Priority 2：对话网络分析管线

- [ ] 事件抽取 + 对话网络构建 + QAP/null models

---

## 暂不做

> 本段落下的任务不计入进度。

- [ ] 在主 treatment 中直接给 agent 喂 integration/depth/control 等指标描述（v14-A 仅作诊断用途）
- [ ] 把本项目重新框成通用社会模拟或新 generative-agent 架构论文
