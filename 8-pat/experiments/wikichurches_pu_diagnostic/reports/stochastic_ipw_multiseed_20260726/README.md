# 多抽样种子 stochastic-IPW 复现实验

日期：2026-07-26

## 结论

- **候选抽样校正机制：AUC 层面可复现。** 在 8 个预先固定的 Bernoulli
  抽样种子上，IPW-nnPU 相对未加权 nnPU 的 ROC-AUC 平均提高
  `+0.018`，分层 bootstrap 95% CI 为 `+0.005–+0.034`；AP 提高
  `+0.007`，但 CI `−0.018–+0.031` 跨 0。
- **IPW 与 FullPool 的总体结果相容。** 两者差值为 AUC `+0.002`
  （`−0.010–+0.018`）、AP `−0.003`（`−0.023–+0.017`）。
- **“更接近 FullPool”仍只是趋势。** IPW 相对未加权方法的绝对 gap
  改变量为 AUC `−0.008`（`−0.018–+0.001`）、AP `−0.010`
  （`−0.026–+0.003`）；负数有利于 IPW，但两个区间仍跨 0。
- **当前 PU 方法整体仍为 No-Go。** IPW-nnPU 相对 Ignore 的差值为
  AUC `−0.082`（`−0.125–−0.043`）、AP `−0.101`
  （`−0.149–−0.051`）。因此不接入 few-shot 分类链路，也不据此宣称
  恢复了真实遗漏正例。

## 预声明设计

- 固定抽样种子：`20260726`–`20260733`，共 8 个；
- 固定 23,371 条候选母集和每条 Bernoulli 纳入概率 `q`；
- 每个种子重新独立抽样，不改变 `q`；
- 9 个满足正框和抽样数门槛的标签；
- 每个种子、标签使用相同的 30 个图像隔离 split；
- 5 个方法：PN-sampled、Ignore、nnPU-sampled、IPW-nnPU、
  FullPool-nnPU；
- 总结果数：`8 × 9 × 30 × 5 = 10,800` 行；
- 区间：同时重采样 sampler seed 与 label 的 10,000 次分层
  bootstrap。

抽样母集每个种子的总抽中数为 662–741（期望约 708）。正式评估的 9 个
标签中，每个种子抽中 217–276 条。seed `20260728` 的 Triangular
Pediment 只有 10 条被抽中候选；原脚本的任意训练门槛 6 会漏掉两个
split，因此正式配置把最小训练 U 设为 1，并完整重跑该种子。原阈值结果
保留在 `runs/seed20260728_threshold6/` 供审计。

## 汇总结果

| 方法 | ROC-AUC | 分层 95% CI | AP | 分层 95% CI |
|---|---:|---:|---:|---:|
| PN-sampled | 0.871 | 0.804–0.928 | 0.566 | 0.453–0.667 |
| Ignore | 0.874 | 0.816–0.922 | 0.551 | 0.448–0.651 |
| nnPU-sampled | 0.774 | 0.684–0.858 | 0.443 | 0.327–0.555 |
| IPW-nnPU | 0.792 | 0.707–0.866 | 0.450 | 0.340–0.555 |
| FullPool-nnPU | 0.790 | 0.699–0.868 | 0.453 | 0.336–0.560 |

| 对比 | ΔROC-AUC | 分层 95% CI | ΔAP | 分层 95% CI |
|---|---:|---:|---:|---:|
| IPW − unweighted nnPU | +0.018 | +0.005–+0.034 | +0.007 | −0.018–+0.031 |
| IPW − FullPool | +0.002 | −0.010–+0.018 | −0.003 | −0.023–+0.017 |
| IPW − Ignore | −0.082 | −0.125–−0.043 | −0.101 | −0.149–−0.051 |

8 个抽样种子中，IPW 相对未加权 nnPU 的 AUC 差值全部为正，范围
`+0.007–+0.027`；相对 Ignore 的 AUC 差值全部为负，范围
`−0.098–−0.072`。这将“抽样校正确实有作用”和“当前 PU 风险仍不适用”
明确分开。

## 机器利用与耗时

- GPU：NVIDIA GeForce RTX 2080 8 GB；
- 共享特征缓存：5,599 × 512，首次编码 41 秒，缓存命中检查 8 秒；
- 正式 8 种子采用 4 路并发，两批总耗时约 662 秒；
- 主并发区间 GPU 活跃样本平均利用率 97.8%，中位数 99%；
- 主并发监控样本中 97.0% 的 GPU 利用率不低于 95%；
- 最高温度 67°C，最高功耗 101 W，最高显存 692 MiB；
- seed `20260728` 完整性补跑 287 秒；
- 纯计算阶段合计约 17 分钟；含完整性检查、调度和汇总的端到端窗口约
  20 分钟；
- 所有正式作业退出码均为 0。

该工作负载成功跑满 GPU 计算单元，但模型和缓存很小，所以不会填满 8 GB
显存；4 个 worker 各占约一个 CPU 核。继续增加 worker 只会增加 GPU
上下文竞争，不会提供更多有效吞吐。

## 证据与复现

- `aggregate/multiseed_report.md`：自动生成的完整统计报告；
- `aggregate/all_results.csv`：10,800 行合并结果；
- `pools/resampling_audit.txt`：8 个固定种子的抽样审计；
- `logs/gpu.csv`：两批正式运行的 5 秒 GPU 监控；
- `logs/orchestrator.log`：8 个作业耗时和退出码；
- `runs/seed*/`：每个种子的原始结果、自动报告、日志和状态；
- `smoke/cache_build.log`、`smoke/cache_hit.log`：缓存编码与命中验证；
- `evidence_bundle.tar.gz`：从服务器回收的完整证据包。

实现脚本：

- `scripts/resample_candidate_pool.py`；
- `scripts/stochastic_ipw_pu_probe.py`；
- `scripts/aggregate_stochastic_ipw_multiseed.py`；
- `scripts/real_pu_no_adjudication_probe.py`。

`aggregate/all_results.csv` 的 SHA-256 为
`d20481ef6f27a68fa53a14fe23335156598db200adc0c1ee359bf6b96b0b3151`。

## 解释边界

FullPool 只是候选 sampling-risk 参照，不是标签 Oracle。框外 U 仍没有
人工真值，official P 的标注倾向和真实类先验仍未识别。本实验只能验证
已知 `q` 下的候选抽样校正是否可复现，不能估计真实 Missing Positive
Rate，也不能证明区域级提升会传递到 few-shot 分类。
