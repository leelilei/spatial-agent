# SMGA Todo List

> 更新日期：2026-06-15
> 当前主线：Phase 5 — Stage 1 pilot analysis and Gate 1 prep

---

## 0. 当前位置

SMGA 现在的位置：

```text
Proposal / schema 已定稿到 v4.6
Experiment 0 的 benchmark seed 已经可以被验证和评分
`fhl` Responses API provider 已接入并用 `gpt-5.4` 跑通 `M0_GA` 与 `M0_prompted`
scorer 已升级：affordance 候选集（v0.2）+ condition-blind LLM-judge（judge_scorer.py）
关键发现：关键词尺子 4/5 vs 1-2/5 的差距是测量假象；LLM-judge 下两个 baseline 均 4/5（旗鼓相当）
judge 仍能抓真实失败（M0_prompted probe_0003 转去问无关信息）并区分实质差异（probe_0004）
测量已修到可信，足以进入 treatment 比较
Stage 1 10-seed pilot 已完成（10 seeds x 5 probes x 5 conditions）：
  M0_GA=37/50, M0_prompted=35/50, M2_memory_only=33/50, M3_placebo=28/50, M3_actionable=38/50
关键信号：M3(结构化可执行记忆)仍是最强条件，但只比 M0_GA 高 1/50；更清楚的机制信号是高于 interface-matched stale placebo 10/50，尤其是 probe_0004 reduced-reliance planning（M3=7/10, placebo=0/10）。
主要风险：probe_0003 norm-response/social-repair 仍弱（M3=3/10），需要失败案例盲审；不能直接把 10-seed pilot 当论文结论。
probe_0002 归因更新：M3 的原始回答其实正确执行了“可向核心团队分享、不可外传”的修订规则；更大的问题是评估口径把 bounded sharing 误判成 maintain_privacy failure。详见 `docs/project/experiment0_probe_0002_diagnostic.md`。
评估卫生更新：`judge_scorer.py` 已支持落盘 verdict JSON，并已把 bounded sharing / global refusal / external privacy boundary 的 rubric 区分清楚。
10-seed pilot 结果见 `docs/project/stage1_pilot_10seed_2026-06-15.md`；Gate 1 failure audit 见 `docs/project/gate1_failure_audit_2026-06-15.md`；2-seed alpha 记录见 `docs/project/stage1_pilot_alpha_2026-06-15.md`。
Gate 1 结论：conditional go for Stage 2 prep，但不能直接开 40-50 seeds。先修 `probe_0003` 的 target/rubric mismatch、明确 `probe_0004` 的 checked-collaboration 边界、降低 M3 unrelated-memory intrusion，然后重跑 10-seed。
```

当前工程骨架：

- [x] `O-01` `benchmark_loader.py`
- [x] `O-02` normalized probe response schema
- [x] `O-03` baseline harness
- [x] `O-04` model-calling runner
- [x] `O-05` condition-blind response normalizer
- [x] `O-06` memory artifact format for M2/M3/placebo outputs
- [ ] `O-07` claim extraction scorer
- [ ] `O-08` planning-grounding scorer
- [x] `O-09a` Stage 1 alpha pilot run on existing 2 seeds
- [x] `O-09b` Stage 1 expanded pilot run on 5-10 seeds

---

## 1. 全局路线图：从 proposal 到 submission

```text
Phase 0  Project / Git / Todo hygiene
Phase 1  Research plan and schemas
Phase 2  Experiment 0 infrastructure
Phase 3  First baseline runs
Phase 4  SMGA treatment and ablations
Phase 5  Stage 1 pilot                        <-- current phase
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

- [x] `P4-01` 定义 memory artifact output format
- [x] `P4-02` 实现最小 `M3_actionable` memory formation
- [x] `P4-03` 实现 planning affordance serialization
- [x] `P4-04` 生成 `M3_actionable` probe responses
- [x] `P4-05` 实现 `M3_placebo` stale memory construction
- [x] `P4-06` 实现 `M2_memory_only` matched-candidate serialization
- [x] `P4-07` 比较 `M0_prompted` vs `M3_actionable` 的 probe success
- [x] `P4-08` 检查 `M3` 是否出现 socially unnatural / evidence-ID leakage 风险

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
M2_memory_only
M3_placebo
M3_actionable
```

实际 pilot 规模：

```text
5 conditions × 10 seeds
```

要完成：

- [x] `P5-01` 扩展到 10 个 hand-authored/generated diagnostic seeds
- [ ] `P5-02` 验证 placebo 不泄露 current content（construction 已实现，Gate 1 audit 未发现 current-content 胜出迹象；仍需 artifact spot-check）
- [ ] `P5-03` 验证 claim extractor pilot
- [x] `P5-04` 验证 judge / annotation pilot（LLM-judge 50 summaries present, 0 status errors）
- [x] `P5-05` 测 seed-level variance
- [x] `P5-06a` Gate 1 failure audit：probe_0003/probe_0004 + M3 naturalness/leakage
- [ ] `P5-06b` Gate 1 measurement hardening：修 probe/rubric/M3 retrieval 后重跑 10-seed
- [ ] `P5-06c` Gate 1 final decision：判断是否进入 Stage 2 main run

完成标准：

```text
pipeline 稳定
M3 至少在 memory / planning / behavior 中一个方向有正向信号
Stage 2 seed budget 能决定 30/40/50
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

- [x] `R2-01` 定义 memory artifact output format
- [x] `R2-02` 实现最小 `M3_actionable` memory formation
- [x] `R2-03` 实现 planning affordance serialization
- [x] `R2-04` 生成 `M3_actionable` probe responses
- [x] `R2-05` 对比 `M0_prompted` vs `M3_actionable`
- [x] `R2-06` 实现并运行 `M3_placebo`
- [x] `R2-07` 记录 Stage 1 alpha pilot 结果

### Priority 3：准备 pilot 和论文骨架

- [x] `R3-01` 扩展到 10 个 diagnostic seeds
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

### 现在在哪（上下文）

Experiment 0：用 seed_0001（易）+ seed_0002（难）两个手写诊断场景，比较 4 个条件——
- `M0_GA` / `M0_prompted`：读**原始事件日志**的 GA 式 baseline（一个普通反思、一个提示式反思）
- `M2_memory_only`：模型形成的结构化记忆，但以**纯文本**喂入
- `M3_actionable`：**同一批记忆**，额外给结构 + `currency_status` + planning affordance（SMGA 的核心治疗）

测量用 condition-blind 的 LLM-judge（`judge_scorer.py`，已验证不冤枉好回答、也能抓真实失败）。
完整跑法见 `benchmarks/diagnostic_v0/README.md` 的 “Full Pipeline” 一节。

### 发现了什么（n=10，诊断级，**非结论**）

合计 /10：`M0_GA=9`，`M0_prompted=7`，`M2=8`，`M3_placebo=7`，`M3=10`。
- **M3 在当前两种子诊断中最强（10/10）**，但样本太小，只能作为继续 pilot 的信号，不能作为论文结论。
- **M3 > M3_placebo（10/10 vs 7/10）**，提供了初步 memory-content signal。
- **M2 仍不稳健**：seed_0002 只有 3/5，尤其 `probe_0002` 把 Dan 转去问 Cara，而不是直接分享允许范围内的信息。
- **M0_GA 意外很强（9/10）**：这提醒我们后续 claim 不能只针对最简单 prompted baseline，还要保留 GA-style baseline 的强度判断。
- **probe_0002 结论修正**：M3 没有失败；失败的是早先的 bounded-sharing 评估口径。

### 下一步：先归因，**不要扩规模**

刚完成的归因：`probe_0002` 不是一个干净的 M3 行为失败。M3 回答已经说清 Dan 是 core team member，因此可以分享 budget-cut detail，同时不能外传。失败信号主要来自评估层：

1. mechanical normalizer 把 “do not share outside the team” 选成 dominant `maintain_privacy`，尽管同一回答也表达了 `share_information`。
2. mechanical scorer 把这个 dominant label 当作 forbidden action，无法区分“拒绝向 Dan 分享”和“向 Dan 分享但不外传”。
3. `current_status_used` 规则没有识别 “core team member / can share / within the core team” 这种修订后许可语义。

评估卫生已推进：

1. `judge_scorer.py` 现在保存 machine-readable verdict summary，结果不再只停留在终端输出。
2. judge rubric 已明确区分 bounded sharing、global refusal、external privacy boundary。

重跑/复核已经完成：M3 在 seed_0002 为 5/5，probe_0002 为 PASS。

下一步只做一件事：**Gate 1 measurement hardening**。根据 `docs/project/gate1_failure_audit_2026-06-15.md`，先修 `probe_0003` 的 containment/repair 混淆、明确 `probe_0004` 的 checked-collaboration 判定边界、降低 M3 unrelated-memory intrusion，然后重跑 10-seed。

### 为什么是这个顺序（原因）

扩到 proposal 计划的 40–50 seeds 很贵（钱 + 时间）。在“treatment 未显收益、且关键诊断 probe 反向”时就扩规模，
只会得到一堆**无法解释的噪声**、还烧掉预算。**必须先把单点机制弄清，再决定扩不扩、扩什么、claim 怎么收窄。**
这正是 Experiment 0（诊断、小规模、可解释）存在的意义。

### 已完成（Phase 3 测量修复 + Phase 4 两种子对比）

```text
scorer v0.2 + judge_scorer.py（condition-blind LLM-judge）
memory_module.py（Module A）+ treatment_harness.py（M2/M3）
seed_0002（更难、修订-追踪，validate 通过）
10 条 judge：M0_GA=9 M0_prompted=7 M2=8 M3_placebo=7 M3=10（/10，诊断，bounded-sharing rubric + placebo 后）
```
