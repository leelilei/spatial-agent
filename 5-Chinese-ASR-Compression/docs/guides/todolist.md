# Chinese ASR Compression Todo List

> 更新日期：2026-06-14
> 当前主线：Phase 1 — 选题已定（跨架构中文 ASR 压缩），进入 baseline 与评测基建搭建

> 说明：本清单为按规范补建的起步骨架，任务取自
> docs/plans/research_plan_v3_cross_architecture_chinese_asr_compression.md，
> 请据实核对并补充真实进度。

---

## 0. 当前位置

选题定位与 gap 分析已在 research_plan v3 完成：核心问题是「手机端离线中文 ASR 应压缩
哪种架构（AR / NAR / LLM-based）」。接下来要把对比对象固定下来，并搭起统一评测基建。

---

## 1. Phase 1 — 评测基建与未压缩 baseline

- [ ] 固定要对比的架构与具体模型清单（Whisper / Paraformer / SenseVoice / …）
- [ ] 搭建统一评测脚本：WER、延迟、内存、功耗四项指标
- [ ] 选定中文测试集并跑通未压缩 baseline，得到 Pareto 起点

## 2. Phase 2 — 压缩方法与跨架构对比

- [ ] 在各架构上施加量化 / 蒸馏，记录压缩后指标
- [ ] 产出跨架构「准确率-速度-内存」Pareto 对比

---

## 执行优先级

### Priority 0：先把评测闭环跑通

- [ ] 统一评测脚本 + 未压缩 baseline

### Priority 1：第一轮压缩对比

- [ ] 至少在 AR 与 NAR 各一个模型上完成一轮压缩对比

---

## 暂不做

> 本段落下的任务不计入进度。

- [ ] 端侧（录音笔/手机）实机部署（等压缩结论稳定后再做）
