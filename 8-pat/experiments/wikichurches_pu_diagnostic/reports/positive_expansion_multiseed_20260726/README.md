# 保守正例扩展多种子实验

日期：2026-07-26

## 决策

**PositiveExpansion：No-Go。**

在 8 个候选抽样种子、9 个标签、30 个 image-disjoint split 上，保守正例
扩展相对 Ignore：

- ROC-AUC：`−0.0022`，分层 95% CI `−0.0047–−0.0004`；
- AP：`−0.0067`，分层 95% CI `−0.0137–−0.0008`。

两个区间均在 0 以下。9/9 标签没有正 AUC 增益，8/8 sampler seed 的
AUC 差值均为负。因此不接入 few-shot Adapter，不放宽阈值重跑，也不再
在同一无裁决评估上搜索伪标签权重。

## 冻结方法

每个图像隔离 split 内：

1. 只用官方正框 P 和层级不兼容的可靠负框训练 5 个子模型；
2. 每个子模型保留 25% 可靠负框作训练内校准；
3. 阈值取校准负框最高分与训练正框 25% 分位数的较大值；
4. 候选必须在 5 个子模型中至少通过 4 个；
5. 接纳候选以固定权重 0.25 加为弱正例；
6. 未接纳 U 完全 abstain，既不作正例也不作负例；
7. 评估图像不参与候选选择、阈值设定或训练。

所有参数在正式聚合前冻结，未使用评估结果调参。

## 完整性

- sampler seed：8；
- 标签：9；
- split：30 / seed / label；
- 新实验结果：`8 × 9 × 30 × 2 = 4,320` 行
  （Ignore 复现与 PositiveExpansion）；
- 新增 PositiveExpansion 行：2,160；
- 与上一轮五方法基线合并：12,960 行；
- Ignore 与上一轮逐行复现的最大指标差：0；
- 10,000 次 sampler-seed × label 分层 bootstrap。

## 结果

| 方法 | ROC-AUC | 分层 95% CI | AP | 分层 95% CI |
|---|---:|---:|---:|---:|
| PN-sampled | 0.871 | 0.804–0.928 | 0.566 | 0.453–0.667 |
| Ignore | 0.874 | 0.816–0.922 | 0.551 | 0.448–0.651 |
| nnPU-sampled | 0.774 | 0.684–0.858 | 0.443 | 0.327–0.555 |
| IPW-nnPU | 0.792 | 0.707–0.866 | 0.450 | 0.340–0.555 |
| FullPool-nnPU | 0.790 | 0.699–0.868 | 0.453 | 0.336–0.560 |
| PositiveExpansion | 0.872 | 0.814–0.921 | 0.544 | 0.438–0.642 |

PositiveExpansion 明显优于 nnPU/IPW，但没有超过更简单的 Ignore。它与
PN-sampled 的 AUC 基本相同，AP 也没有显著优势。

## 选择诊断

- 平均每个 split 接纳 0.79 个伪正例；
- 平均选择率约 3.6%；
- 8/9 标签至少有少量扩展；
- Buttress 平均选择 2.04 个，AUC/AP 差值 `−0.004/−0.022`；
- Triangular Pediment 平均选择 2.60 个，差值
  `−0.011/−0.025`；
- 8 个种子的 AUC 差值范围为 `−0.003–−0.001`。

这说明失败不是由某一个随机候选样本导致，而是保守伪正例在当前已知标签
评估上没有增加可泛化信息。

## 冻结 Go 条件

预先要求同时满足：

- ΔAUC 和 ΔAP 均至少 `+0.01`；
- 两个分层 CI 下界均大于 0；
- 覆盖至少 4 个标签；
- 每个 sampler seed 的 AUC 方向均为正。

实际结果只满足覆盖条件，最终为 **No-Go**。

## 运行

- 共享缓存：5,599 × 512 个 frozen CLIP 特征；
- smoke：6 秒；
- 正式 8 种子使用 8 个 CPU worker 并发：16–18 秒；
- 正式计算期间 CPU 使用率约 99%，8 个 runnable worker；
- 本轮不需要重复调用 GPU 编码，因而没有为“跑满 GPU”进行无意义计算；
- 8 个正式作业退出码均为 0。

## 证据

- `aggregate/positive_expansion_report.md`：自动统计报告；
- `aggregate/combined_results.csv`：12,960 行合并结果；
- `runs/seed*/per_split_results.csv`：每种子的原始结果；
- `runs/seed*/summary.json`：选择率和冻结配置；
- `logs/orchestrator.log`、`logs/vmstat.txt`：运行与 CPU 审计；
- `smoke/`：1-repeat 预运行；
- `evidence_bundle.tar.gz`：服务器证据包。

`combined_results.csv` SHA-256：
`88a61a8de63830a20662435e7fb614ec7fe27386e90bc04b19d655c20b7eec80`。

实现：

- `scripts/conservative_positive_expansion_probe.py`；
- `scripts/aggregate_positive_expansion_multiseed.py`。

## 下一步边界

本轮与前序 IPW 实验共同排除了两条无裁决路线：

1. 把 U 作为带校正的风险样本；
2. 只把极高置信 U 作为弱正例。

继续调阈值、伪正例权重、类先验或换另一种 PU loss，都会在没有 U 真值的
同一评估上产生方法搜索偏差。若研究目标仍是验证真实遗漏正例，下一项有
辨识力的实验是完成最小人工盲审；若坚持零人工标注，则应将当前结果作为
方法学负结果，改写研究问题，而不是继续宣称 missing-positive recovery。
