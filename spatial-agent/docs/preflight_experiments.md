# v7 预实验双模式闭环

对应 `../../docs/plans/spatial_agent_research_plan_v7.md` 的 6.0 与 8.3.1，当前预实验支持：

- **离线模式**：生成任务、导入外部/人工响应、自动评分、输出 decision report
- **在线模式**：按统一 task schema 直接调用主模型或鲁棒性模型，并写入标准原始响应目录
- **本地 pilot**：指标质量预检、MIC 有效窗口 pilot、收敛性 pilot

## 已覆盖

- **指标质量预检**：输出相关矩阵、CV、高 `control` 节点计数与 H2 指标选择依据
- **LLM 理解门控**：`comprehension` 与 `behavioral_inference` 任务 + 自动阈值判定
- **Prompt 位置测试**：同一题目在三个 prompt 位置下的表现比较与推荐位置
- **C2 reverse-inference audit**：逐地点、逐维度的 leak 检查与待改写地点列表
- **Lexical Norming**：统一 JSONL task + 手工 CSV 表 + 标签排序结果
- **Coding Manual pilot 的 LLM 子集**：标准化任务包与响应 schema
- **MIC 有效窗口 pilot**：输出 run-level / window-level 指标、matched vs unmatched 方差比较、`ICC(seed)`
- **收敛性 pilot**：输出 delta 序列、稳态判断与建议总轮数

## 运行

在 `spatial-agent` 目录下：

```bash
python experiments/run_preflight.py --stage all
```

`all` 默认是 **offline-safe**，执行：

```bash
metrics -> tasks -> mic -> convergence -> analyze
```

### 分阶段运行

```bash
python experiments/run_preflight.py --stage metrics
python experiments/run_preflight.py --stage tasks
python experiments/run_preflight.py --stage mic
python experiments/run_preflight.py --stage convergence
python experiments/run_preflight.py --stage analyze
```

### 在线执行 LLM 任务

```bash
python experiments/run_preflight.py --stage run_online --model primary --mode online
python experiments/run_preflight.py --stage run_online --model robustness --mode online
```

### 导入离线响应

支持两种输入：

- 扁平 JSONL：`<responses-dir>/<task_family>.jsonl`
- 规范目录：`<responses-dir>/<task_family>/<model>/responses.jsonl`

```bash
python experiments/run_preflight.py --stage run_offline --responses-dir /path/to/responses
python experiments/run_preflight.py --stage analyze
```

如果是人工 lexical norming，也可直接放：

```text
<responses-dir>/lexical_norming_sheet.csv
```

## 任务与响应 schema

### Task JSONL

每条任务至少包含：

- `task_id`
- `task_family`
- `prompt_payload`
- `expected_answer`（若适用）
- `metadata`

### Response JSONL

每条响应至少包含：

- `task_id`
- `task_family`
- `model`
- `raw_text`
- `parsed_answer`（可空）
- `success`
- `latency_ms`
- `cache_hit`
- `error`

## 输出目录

- `results/preflight/metrics`
- `results/preflight/tasks`
- `results/preflight/raw`
- `results/preflight/scored`
- `results/preflight/mic`
- `results/preflight/convergence`
- `results/preflight/reports`

## 关键报告

- `results/preflight/reports/preflight_summary.md`
- `results/preflight/reports/preflight_decisions.json`
- `docs/preflight_gpt54_core20_report.md`
- `results/preflight/gpt54_core20/aggregate_summary.json`

其中会显式回答：

- H2 用 `openness` 还是 `mean_depth`
- 主模型是否通过理解门控
- prompt 位置固定哪个
- 哪些 `C2` 描述需要重写
- 哪些 lexical labels 保留
- 阶段 2 建议用 `200` 还是 `300` 轮

## 当前边界

- `MIC` 与 `convergence` 仍使用 **本地轻量 heuristic simulator**，目标是固定 protocol 与分析口径
- 在线 runner 依赖 `config.models` 中的 API 配置；默认 `all` 不会隐式触发网络调用
- `TAR_run` 继续按 `location-level Spearman + Fisher z` 的 v7 协议计算
