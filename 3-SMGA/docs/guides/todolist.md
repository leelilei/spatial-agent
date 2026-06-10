# SMGA Todo List

> 更新日期：2026-06-10
> 当前主线：Phase 2 — Experiment 0 infrastructure

---

## 0. 当前位置

SMGA 现在的位置：

```text
Proposal / schema 已定稿到 v4.6
Experiment 0 的 benchmark seed 已经可以被验证和评分
当前正在补齐可运行工程骨架
下一步：实现 diagnostic_v0/benchmark_loader.py
```

已经完成：

- [x] 整理并保存 `SMGA Proposal v4.6`
- [x] 写出 `SMGA Memory Schema v0.1`
- [x] 写出 `SMGA Scenario Package Schema v0.1`
- [x] 建立 `diagnostic_v0`
- [x] 手写 `seed_0001`
- [x] 实现 `validate_seed.py`
- [x] 实现 `probe_success_scorer.py`
- [x] 用 oracle-style example responses 跑通 5/5 probe success
- [x] 建立 SMGA 全局 todo / progress map

当前未完成但最近要补：

- [ ] `benchmark_loader.py`
- [ ] normalized probe response schema
- [ ] baseline harness
- [ ] model-calling runner
- [ ] memory artifact format for M0/M3 outputs
- [ ] claim extraction scorer
- [ ] planning-grounding scorer
- [ ] Stage 1 pilot runs

---

## 1. 全局路线图：从 proposal 到 submission

```text
Phase 0  Project / Git / Todo hygiene
Phase 1  Research plan and schemas
Phase 2  Experiment 0 infrastructure          <-- current phase
Phase 3  First baseline runs
Phase 4  SMGA treatment and ablations
Phase 5  Stage 1 pilot
Phase 6  Stage 2 main experiment
Phase 7  Stage 2b secondary controls
Phase 8  Analysis, writing, and release
```

这篇论文的主线不是“先写代码”，而是：

```text
研究问题锁定
→ benchmark 可验证
→ baseline 可运行
→ SMGA treatment 可运行
→ pilot 判断是否值得扩展
→ main experiment
→ secondary controls
→ analysis + paper
```

---

## 2. Phase 0 — Project Hygiene

目标：让项目状态清楚、可追踪、可恢复。

- [x] SMGA 从 SpatialAgent 中独立成项目目录
- [x] `3-SMGA/README.md` 指向当前 proposal 和 schema
- [x] 建立 active todo list
- [ ] 将当前 SMGA docs / benchmark / scorer 改动提交到 git
- [ ] 之后每完成一个 phase 或关键 milestone 都提交一次

完成标准：

```text
git status 清楚
README 能指向当前研究计划
todo 能说明当前 phase 和下一步动作
```

---

## 3. Phase 1 — Research Plan and Schemas

目标：把论文 claim、实验逻辑、memory structure、scenario package 都冻结到足够工程化的程度。

- [x] `SMGA Proposal v4.6`
- [x] `SMGA Memory Schema v0.1`
- [x] `SMGA Scenario Package Schema v0.1`
- [ ] 后续如 schema 改动，记录为 v0.2，不直接覆盖历史语义

完成标准：

```text
知道论文要测什么
知道 memory object 长什么样
知道 scenario package 长什么样
知道 success/failure condition 如何进入 scorer
```

---

## 4. Phase 2 — Experiment 0 Infrastructure

目标：用一个 hand-authored seed 跑通 benchmark 数据、校验器、scorer、loader 的基础链路。

已完成：

- [x] 建立 `benchmarks/diagnostic_v0/`
- [x] 手写 `seed_0001`
- [x] `seed_0001` 包含 entities / events / gold facts / contradictions / probes
- [x] 实现 `validate_seed.py`
- [x] 实现 `probe_success_scorer.py`
- [x] 示例 oracle responses 得到 5/5 probe success

正在做：

- [ ] 实现 `benchmark_loader.py`
- [ ] 给 loader 增加 CLI summary
- [ ] 定义 normalized probe response schema
- [ ] 用 loader + scorer 跑通完整读取与评分链路

完成标准：

```text
python3 validate_seed.py
python3 benchmark_loader.py seeds/seed_0001
python3 probe_success_scorer.py seeds/seed_0001 examples/seed_0001_probe_responses.json
```

三条命令都稳定通过。

---

## 5. Phase 3 — First Baseline Runs

目标：先让非 SMGA baseline 跑起来，得到第一批真实模型输出。

- [ ] 实现 `M0_GA` prompt harness
- [ ] 实现 `M0_prompted` prompt harness
- [ ] 固定 model config：provider / model version / temperature / decoding settings
- [ ] 为 `seed_0001` 生成 baseline probe responses
- [ ] 将 baseline responses 输出为 scorer 可读 JSON
- [ ] 用 `probe_success_scorer.py` 评分 `M0_GA`
- [ ] 用 `probe_success_scorer.py` 评分 `M0_prompted`
- [ ] 记录 baseline failure cases，检查 probe 是否过窄或过宽

完成标准：

```text
M0_GA 和 M0_prompted 都能在 seed_0001 上完整输出 responses
responses 能被 scorer 机械评分
失败案例能回溯到 required evidence / gold fact / success condition
```

---

## 6. Phase 4 — SMGA Treatment and Ablations

目标：把 SMGA treatment 和必要 ablations 接到同一个 benchmark/scorer 管线里。

- [ ] 定义 memory artifact output format
- [ ] 实现最小 `M3_actionable` memory formation
- [ ] 实现 planning affordance serialization
- [ ] 生成 `M3_actionable` probe responses
- [ ] 实现 `M3_placebo` stale memory construction
- [ ] 实现 `M2_memory_only` matched-candidate serialization
- [ ] 比较 `M0_prompted` vs `M3_actionable` 的 probe success
- [ ] 检查 `M3` 是否出现 socially unnatural / evidence-ID leakage 风险

完成标准：

```text
M2_memory_only
M3_placebo
M3_actionable
```

都能在 `seed_0001` 上跑完，并输出 scorer 可读 JSON。

---

## 7. Phase 5 — Stage 1 Pilot

目标：小规模验证是否值得扩展到主实验。

计划条件：

```text
M0_GA
M0_prompted
M3_placebo
M3_actionable
```

计划规模：

```text
4 conditions × 5 seeds
```

要完成：

- [ ] 扩展到 5 个 hand-authored 或 generated seeds
- [ ] 验证 placebo 不泄露 current content
- [ ] 验证 claim extractor pilot
- [ ] 验证 judge / annotation pilot
- [ ] 测 seed-level variance
- [ ] Gate 1：判断是否进入 Stage 2

完成标准：

```text
pipeline 稳定
M3 至少在 memory / planning / behavior 中一个方向有正向信号
Stage 2 seed budget 能决定 40 或 50
```

---

## 8. Phase 6 — Stage 2 Main Experiment

目标：跑主论文的核心结果表。

主实验条件：

```text
M0_GA
M0_prompted
M2_memory_only
M3_placebo
M3_actionable
```

计划规模：

```text
5 conditions × 40 seeds
或 Gate 1 后改为 50 seeds
```

核心对比：

```text
C1: M3_actionable > M0_prompted on grounded memory F1
C2: M3_actionable > M2_memory_only on history-grounded planning
C3: M3_actionable > M3_placebo on probe behavior success
C4: M3_actionable > M0_prompted on probe behavior success
```

完成标准：

```text
C1-C4 都有 paired seed-level results
Holm correction 和 SESOI 判断可复现
主结果表可以进入论文 Results section
```

---

## 9. Phase 7 — Stage 2b Secondary Controls

目标：补 reviewer 最可能攻击的两个控制条件。

条件：

```text
M0_plus
GraphMemory_social_schema
```

计划规模：

```text
15 seeds each
```

要回答：

- [ ] `M0_plus` 是否追平 `M3_actionable`
- [ ] `GraphMemory_social_schema` 是否追平 `M3_actionable`
- [ ] 如果 graph baseline 不跑，论文是否主动收窄 architecture claim

完成标准：

```text
S1: M3_actionable vs M0_plus
S2: M3_actionable vs GraphMemory_social_schema
```

能报告 CI，并决定最终 claim 边界。

---

## 10. Phase 8 — Analysis, Writing, and Release

目标：从实验结果变成可投稿论文。

### 可以早写

- [ ] Introduction
- [ ] Related Work
- [ ] Method overview
- [ ] SMGA memory schema
- [ ] Diagnostic benchmark construction
- [ ] Experimental conditions

### 实验后补

- [ ] Results
- [ ] Ablation analysis
- [ ] Failure cases
- [ ] Downgrade-rule interpretation
- [ ] Discussion
- [ ] Limitations

### Release assets

- [ ] scenario templates
- [ ] gold structures
- [ ] scorer scripts
- [ ] prompts
- [ ] validation set
- [ ] analysis scripts
- [ ] per-condition traces

完成标准：

```text
paper draft contains method, experiment, results, discussion, limitations
release package can reproduce tables
claim 不超过 v4.6 success/downgrade rules
```

---

## 执行优先级

### Priority 0：立即做，推进当前 Phase 2

- [ ] 将当前 SMGA docs / benchmark / scorer 改动提交到 git
- [ ] 实现 `benchmark_loader.py`
- [ ] 为 `benchmark_loader.py` 加 CLI summary
- [ ] 定义 normalized probe response schema
- [ ] 用 loader + scorer 跑通 `seed_0001` 的完整读取与评分链路

### Priority 1：跑第一个真实 baseline

- [ ] 实现 `M0_GA` prompt harness
- [ ] 实现 `M0_prompted` prompt harness
- [ ] 为 `seed_0001` 生成 baseline probe responses
- [ ] 将 baseline responses 输出为 scorer 可读 JSON
- [ ] 用 `probe_success_scorer.py` 评分 `M0_GA` 和 `M0_prompted`
- [ ] 记录 baseline failure cases

### Priority 2：接入 SMGA treatment

- [ ] 定义 memory artifact output format
- [ ] 实现最小 `M3_actionable` memory formation
- [ ] 实现 planning affordance serialization
- [ ] 生成 `M3_actionable` probe responses
- [ ] 对比 `M0_prompted` vs `M3_actionable`

### Priority 3：准备 pilot 和论文骨架

- [ ] 扩展到 5 个 seeds
- [ ] 写 claim extractor 输入/输出 schema
- [ ] 写 grounded memory F1 scorer
- [ ] 写 history-grounded planning scorer
- [ ] 建立 paper outline
- [ ] 先写 Introduction / Method skeleton

---

## 暂不做

- [ ] 自动生成 40-50 个 seeds
- [ ] GraphMemory baseline
- [ ] `M0_plus` compute-matched baseline
- [ ] second-model replication
- [ ] external benchmark adapter
- [ ] live multi-agent simulation

---

## 下一步具体动作

下一步只做一件事：

```text
实现 diagnostic_v0/benchmark_loader.py
```

目标输出：

```text
python3 benchmark_loader.py seeds/seed_0001

scenario_0001 / seed_0001
entities: 17
events: 12
gold facts: 9
contradictions: 3
probes: 5
validation: OK
```

