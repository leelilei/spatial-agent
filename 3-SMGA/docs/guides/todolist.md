# SMGA Todo List

> 更新日期：2026-06-14
> 当前主线：Phase 3 — First baseline runs

---

## 0. 当前位置

SMGA 现在的位置：

```text
Proposal / schema 已定稿到 v4.6
Experiment 0 的 benchmark seed 已经可以被验证和评分
`fhl` Responses API provider 已接入并用 `gpt-5.4` 跑通 `M0_GA` 与 `M0_prompted`
两个 baseline 已完成评分（seed_0001，单 seed 管线诊断）：`M0_GA` = 4/5，`M0_prompted` = 1/5
意外信号：`M0_prompted` 远低于 `M0_GA`（probe_0003 还触发 forbidden marker），疑似 probe/marker 口径过窄
下一步：先做 probe/marker 口径复盘（marker v0.2），再进入 Phase 4（SMGA treatment）
```

当前工程骨架：

- [x] `O-01` `benchmark_loader.py`
- [x] `O-02` normalized probe response schema
- [x] `O-03` baseline harness
- [x] `O-04` model-calling runner
- [x] `O-05` condition-blind response normalizer
- [ ] `O-06` memory artifact format for M0/M3 outputs
- [ ] `O-07` claim extraction scorer
- [ ] `O-08` planning-grounding scorer
- [ ] `O-09` Stage 1 pilot runs

---

## 1. 全局路线图：从 proposal 到 submission

```text
Phase 0  Project / Git / Todo hygiene
Phase 1  Research plan and schemas
Phase 2  Experiment 0 infrastructure
Phase 3  First baseline runs                  <-- current phase
Phase 4  SMGA treatment and ablations
Phase 5  Stage 1 pilot
Phase 6  Stage 2 main experiment
Phase 7  Stage 2b secondary controls
Phase 8  Analysis, writing, and release
```

这篇论文的主线：

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

- [x] `P0-01` SMGA 从 SpatialAgent 中独立成项目目录
- [x] `P0-02` `3-SMGA/README.md` 指向当前 proposal 和 schema
- [x] `P0-03` 建立 active todo list
- [x] `P0-04` 将当前 SMGA docs / benchmark / scorer 改动提交到 git
- [ ] `P0-05` 之后每完成一个 phase 或关键 milestone 都提交一次

完成标准：

```text
git status 清楚
README 能指向当前研究计划
todo 能说明当前 phase 和下一步动作
```

---

## 3. Phase 1 — Research Plan and Schemas

目标：把论文 claim、实验逻辑、memory structure、scenario package 都冻结到足够工程化的程度。

- [x] `P1-01` `SMGA Proposal v4.6`
- [x] `P1-02` `SMGA Memory Schema v0.1`
- [x] `P1-03` `SMGA Scenario Package Schema v0.1`
- [x] `P1-04` `SMGA Normalized Probe Response Schema v0.1`
- [ ] `P1-05` 后续如 schema 改动，记录为 v0.2，不直接覆盖历史语义

完成标准：

```text
知道论文要测什么
知道 memory object 长什么样
知道 scenario package 长什么样
知道 success/failure condition 如何进入 scorer
知道 baseline response 如何进入 scorer
```

---

## 4. Phase 2 — Experiment 0 Infrastructure

目标：用一个 hand-authored seed 跑通 benchmark 数据、校验器、scorer、loader 的基础链路。

- [x] `P2-01` 建立 `benchmarks/diagnostic_v0/`
- [x] `P2-02` 手写 `seed_0001`
- [x] `P2-03` `seed_0001` 包含 entities / events / gold facts / contradictions / probes
- [x] `P2-04` 实现 `validate_seed.py`
- [x] `P2-05` 实现 `probe_success_scorer.py`
- [x] `P2-06` 示例 oracle responses 得到 5/5 probe success
- [x] `P2-07` 实现 `benchmark_loader.py`
- [x] `P2-08` 给 loader 增加 CLI summary
- [x] `P2-09` 定义 normalized probe response schema
- [x] `P2-10` 用 loader + scorer 跑通完整读取与评分链路
- [x] `P2-11` 移除 `seed_0001` 中会泄漏 benchmark/scoring 语气的文本

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

- [x] `P3-01` 实现 `M0_GA` prompt harness
- [x] `P3-02` 实现 `M0_prompted` prompt harness
- [x] `P3-03` 实现 `model_calling_runner.py`
- [x] `P3-04` 实现 `response_normalizer.py`
- [x] `P3-05` 建立 baseline model config 模板
- [x] `P3-06` 固定 model config：provider / model version / temperature / decoding settings
- [x] `P3-07` 为 `seed_0001` 生成 `M0_GA` raw model outputs
- [x] `P3-08` 为 `seed_0001` 生成 `M0_prompted` raw model outputs
- [x] `P3-09` 将 `M0_GA` responses 输出为 scorer 可读 JSON
- [x] `P3-10` 将 `M0_prompted` responses 输出为 scorer 可读 JSON
- [x] `P3-11` 用 `probe_success_scorer.py` 评分 `M0_GA`
- [x] `P3-12` 用 `probe_success_scorer.py` 评分 `M0_prompted`
- [x] `P3-13` 记录 baseline failure cases，检查 probe 是否过窄或过宽

当前已固定 baseline 调用配置：

```text
provider: fhl
wire_api: responses
model: gpt-5.4
transport: curl
responses_input_mode: string
omit_temperature: true
json_mode: false
disable_response_storage: true
sleep: 3
retries: 3
retry_sleep: 5
```

当前 `M0_GA` 真实结果：

```text
seed_0001 / M0_GA / fhl gpt-5.4
score: 4/5 headline probes passed (80.0%)
failed: probe_0004
failure reason: not enough required response markers
interpretation: 模型方向基本正确，但没有显式包含 verify / less rely 等 planning-grounding marker
```

下一步具体动作：

```text
1. 用同一 `fhl_responses_gpt54_config.example.json` 跑 `M0_prompted`
2. normalize `M0_prompted` responses
3. score `M0_prompted`
4. 对比 `M0_GA` vs `M0_prompted` 的 failure cases
5. 判断 probe_0004 是合理 baseline failure，还是 normalizer / marker 需要 v0.2 调整
```

完成标准：

```text
M0_GA 和 M0_prompted 都能在 seed_0001 上完整输出 responses
responses 能被 scorer 机械评分
失败案例能回溯到 required evidence / gold fact / success condition
```

---

## 6. Phase 4 — SMGA Treatment and Ablations

目标：把 SMGA treatment 和必要 ablations 接到同一个 benchmark/scorer 管线里。

- [ ] `P4-01` 定义 memory artifact output format
- [ ] `P4-02` 实现最小 `M3_actionable` memory formation
- [ ] `P4-03` 实现 planning affordance serialization
- [ ] `P4-04` 生成 `M3_actionable` probe responses
- [ ] `P4-05` 实现 `M3_placebo` stale memory construction
- [ ] `P4-06` 实现 `M2_memory_only` matched-candidate serialization
- [ ] `P4-07` 比较 `M0_prompted` vs `M3_actionable` 的 probe success
- [ ] `P4-08` 检查 `M3` 是否出现 socially unnatural / evidence-ID leakage 风险

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

- [ ] `P5-01` 扩展到 5 个 hand-authored 或 generated seeds
- [ ] `P5-02` 验证 placebo 不泄露 current content
- [ ] `P5-03` 验证 claim extractor pilot
- [ ] `P5-04` 验证 judge / annotation pilot
- [ ] `P5-05` 测 seed-level variance
- [ ] `P5-06` Gate 1：判断是否进入 Stage 2

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

要完成：

- [ ] `P6-01` 运行 5 conditions × 40 seeds
- [ ] `P6-02` 如 Gate 1 variance 过高，扩展到 50 seeds
- [ ] `P6-03` 生成 C1-C4 paired seed-level results
- [ ] `P6-04` 实现 Holm correction
- [ ] `P6-05` 实现 SESOI 判断
- [ ] `P6-06` 生成可进入论文 Results section 的主结果表

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

要完成：

- [ ] `P7-01` 跑 `M0_plus` control
- [ ] `P7-02` 跑 `GraphMemory_social_schema` control
- [ ] `P7-03` 报告 `M3_actionable` vs `M0_plus` 的 CI
- [ ] `P7-04` 报告 `M3_actionable` vs `GraphMemory_social_schema` 的 CI
- [ ] `P7-05` 判断 `M0_plus` 是否追平 `M3_actionable`
- [ ] `P7-06` 判断 `GraphMemory_social_schema` 是否追平 `M3_actionable`
- [ ] `P7-07` 如 graph baseline 不跑，论文主动收窄 architecture claim

完成标准：

```text
S1: M3_actionable vs M0_plus
S2: M3_actionable vs GraphMemory_social_schema
```

能报告 CI，并决定最终 claim 边界。

---

## 10. Phase 8 — Analysis, Writing, and Release

目标：从实验结果变成可投稿论文。

可以早写：

- [ ] `P8A-01` Introduction
- [ ] `P8A-02` Related Work
- [ ] `P8A-03` Method overview
- [ ] `P8A-04` SMGA memory schema
- [ ] `P8A-05` Diagnostic benchmark construction
- [ ] `P8A-06` Experimental conditions

实验后补：

- [ ] `P8B-01` Results
- [ ] `P8B-02` Ablation analysis
- [ ] `P8B-03` Failure cases
- [ ] `P8B-04` Downgrade-rule interpretation
- [ ] `P8B-05` Discussion
- [ ] `P8B-06` Limitations

Release assets：

- [ ] `P8C-01` scenario templates
- [ ] `P8C-02` gold structures
- [ ] `P8C-03` scorer scripts
- [ ] `P8C-04` prompts
- [ ] `P8C-05` validation set
- [ ] `P8C-06` analysis scripts
- [ ] `P8C-07` per-condition traces

完成标准：

```text
paper draft contains method, experiment, results, discussion, limitations
release package can reproduce tables
claim 不超过 v4.6 success/downgrade rules
```

---

## 执行优先级

### Priority 0：完成当前工程闭环

- [x] `R0-01` 将当前 SMGA docs / benchmark / scorer 改动提交到 git
- [x] `R0-02` 实现 `benchmark_loader.py`
- [x] `R0-03` 为 `benchmark_loader.py` 加 CLI summary
- [x] `R0-04` 定义 normalized probe response schema
- [x] `R0-05` 用 loader + scorer 跑通 `seed_0001` 的完整读取与评分链路

### Priority 1：跑第一个真实 baseline

- [x] `R1-01` 实现 `M0_GA` prompt harness
- [x] `R1-02` 实现 `M0_prompted` prompt harness
- [x] `R1-03` 实现 model-calling runner
- [x] `R1-04` 实现 condition-blind response normalizer
- [x] `R1-05` 建立 baseline model config 模板
- [x] `R1-06` 固定 model config
- [x] `R1-07` 为 `seed_0001` 生成 baseline probe responses
- [x] `R1-08` 将 baseline responses 输出为 scorer 可读 JSON
- [x] `R1-09` 用 `probe_success_scorer.py` 评分 `M0_GA` 和 `M0_prompted`
- [x] `R1-10` 记录 baseline failure cases

R1 当前细分状态：

```text
M0_GA raw outputs: done
M0_GA normalized scorer JSON: done
M0_GA score: 4/5
M0_prompted raw outputs: next
M0_prompted normalized scorer JSON: pending
M0_prompted score: pending
```

### Priority 2：接入 SMGA treatment

- [ ] `R2-01` 定义 memory artifact output format
- [ ] `R2-02` 实现最小 `M3_actionable` memory formation
- [ ] `R2-03` 实现 planning affordance serialization
- [ ] `R2-04` 生成 `M3_actionable` probe responses
- [ ] `R2-05` 对比 `M0_prompted` vs `M3_actionable`

### Priority 3：准备 pilot 和论文骨架

- [ ] `R3-01` 扩展到 5 个 seeds
- [ ] `R3-02` 写 claim extractor 输入/输出 schema
- [ ] `R3-03` 写 grounded memory F1 scorer
- [ ] `R3-04` 写 history-grounded planning scorer
- [ ] `R3-05` 建立 paper outline
- [ ] `R3-06` 先写 Introduction / Method skeleton

---

## 暂不做

- [ ] `H-01` 自动生成 40-50 个 seeds
- [ ] `H-02` GraphMemory baseline
- [ ] `H-03` `M0_plus` compute-matched baseline
- [ ] `H-04` second-model replication
- [ ] `H-05` external benchmark adapter
- [ ] `H-06` live multi-agent simulation

---

## 下一步具体动作

下一步只做一件事：

```text
复盘 probe / marker 口径（marker v0.2）
```

为什么：`M0_prompted` 在 `seed_0001` 上仅 1/5，远低于 `M0_GA` 的 4/5，违反直觉。
疑似 probe 的 required/forbidden marker 过窄、或 affordance 判定过严。
先判断是"口径问题"还是"真实差异"，再决定扩 seeds / 进 Phase 4。

目标输出：

```text
probe_0001 / 0003 / 0004 / 0005 失败归因（口径问题 vs 真实差异）
marker v0.2 调整建议（required / forbidden / affordance）
Phase 4 启动判断
```

已完成（Phase 3 收尾）：

```text
provider / model / decoding: fhl / gpt-5.4 / responses / curl transport
M0_GA：raw + normalized + score = 4/5
M0_prompted：raw + normalized + score = 1/5
两个 baseline 的 failure cases 已记录
```
