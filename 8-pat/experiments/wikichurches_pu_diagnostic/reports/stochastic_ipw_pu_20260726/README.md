# 已知随机纳入概率的 IPW-PU 诊断

日期：2026-07-26

## 决策

- **候选抽样校正：有限 Go。** IPW-nnPU 相对未加权 sampled-U nnPU
  的 ROC-AUC 提高 0.016，且聚合结果与 FullPool-nnPU 没有显著差异。
- **PU 方法整体：No-Go。** IPW 和 FullPool 都显著落后 Ignore；修复候选
  抽样偏差不能修复当前 P/U 风险本身，因此不进入下游 few-shot 分类。

## 随机候选设计

原 deterministic top-3 被替换为独立 Bernoulli 抽样。对每个
图像—标签组：

1. 为全部框外候选计算冻结 CLIP ViT-B/32 分数；
2. 通过温度 0.05 的指数权重构造纳入概率；
3. 校准使 `Σq_i = 3`；
4. 约束 `0.01 < q_i < 0.80`；
5. 使用固定 seed `20260726` 独立抽样；
6. 将每个 `q_i`、sampled 指示、完整 rank 和选择变量写入母集 CSV。

审计结果：

- 图像—标签组：236；
- 完整 label-region 母集：23,371 条；
- 去重视觉区域：5,599；
- 期望抽样数：708；
- 实际抽样数：690；
- 每组 `Σq_i` 最大绝对误差：`2.71e-08`；
- 全母集 q 范围：0.0109–0.1594；
- 母集生成耗时：56 秒。

## 方法

- `PN-sampled`：把随机抽中的 U 作为负例；
- `Ignore`：只使用官方 P 与可靠跨标签负框；
- `nnPU-sampled`：对随机 U 不加权；
- `IPW-nnPU`：在 U 负风险上使用自归一化 `1/q_i`；
- `FullPool-nnPU`：使用完整候选母集，作为 sampling-risk 参照。

FullPool 不是标签 Oracle；所有 U 仍无人工真值。

正式实验使用 9 个标签、30 个按图像隔离的 split、固定类先验 0.25，
共 1,350 行结果。

## 结果

| 方法 | ROC-AUC | 95% CI | AP | 95% CI |
|---|---:|---:|---:|---:|
| PN-sampled | 0.875 | 0.811–0.927 | 0.571 | 0.463–0.665 |
| Ignore | 0.874 | 0.816–0.921 | 0.551 | 0.449–0.649 |
| nnPU-sampled | 0.776 | 0.681–0.858 | 0.423 | 0.303–0.545 |
| IPW-nnPU | 0.792 | 0.703–0.868 | 0.438 | 0.308–0.571 |
| FullPool-nnPU | 0.790 | 0.697–0.867 | 0.453 | 0.338–0.560 |

## 配对差值

| 对比 | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| IPW − unweighted sampled | +0.016 | +0.001–+0.027 | +0.015 | -0.019–+0.045 |
| IPW − FullPool | +0.002 | -0.019–+0.022 | -0.015 | -0.075–+0.043 |
| unweighted sampled − FullPool | -0.014 | -0.035–+0.006 | -0.030 | -0.091–+0.033 |
| IPW − Ignore | -0.082 | -0.119–-0.043 | -0.113 | -0.180–-0.037 |

IPW 权重 ESS：

- 均值：16.90；
- 最小值：7.14；
- 最大值：28.87。

## FullPool 逼近检验

以每个 split 到 FullPool 的绝对指标差为目标：

| 对比 | Δ absolute AUC gap | 95% CI | Δ absolute AP gap | 95% CI |
|---|---:|---:|---:|---:|
| IPW gap − unweighted gap | +0.000 | -0.015–+0.017 | -0.008 | -0.032–+0.017 |

负数表示 IPW 更接近 FullPool。AUC gap 没有变化，AP gap 有轻微改善但区间
跨 0。逐标签上，IPW 在 AUC 上有 4/9 个标签更接近 FullPool，在 AP 上
有 5/9 个。因此不能声称 IPW 稳定恢复了逐标签母集结果。

聚合层面 IPW 与 FullPool 的差值接近 0，说明随机 q 和风险实现基本合理；
逐标签绝对 gap 未改善，说明当前 690 个样本和高方差权重不足以稳定复原
每个标签的 FullPool 模型。

## 解释

本轮隔离了两件事：

1. deterministic top-k 确实不是合适的 propensity 实验设计；
2. 即使候选抽样偏差被消除，FullPool-nnPU 仍低于 Ignore。

因此当前主要瓶颈不是 candidate sampling，而是：

- U 不是总体分布的无偏标签混合；
- 类先验没有真实标注支持；
- official P 的 annotation propensity 仍未知；
- 评估只有已知官方 P/reliable N，无法验证遗漏正例恢复。

## 下一步判断

不建议继续在同一无裁决数据上：

- 调温度、q 上下界或 IPW 截断；
- 搜类先验以追逐测试集；
- 把当前区域头接到分类链路宣称提升。

这些操作只能优化已知标签测试，不能解决遗漏正例真值问题。

如果仍坚持完全无人工裁决，可将该结果作为“采样校正方法学负结果”，转向
不依赖 U 真值的表示学习问题；若目标仍是验证漏标和 Oracle gap，则需要
最小规模人工确认。

## 运行信息

- GPU：RTX 2080；
- 正式运行耗时：326 秒；
- 峰值显存：1,590 MiB；
- 退出码：0。

## 证据文件

- `pool_gen/full_candidate_pool.csv`：23,371 条母集与 q；
- `pool_gen/sampling_audit.txt`：概率和抽样审计；
- `run30/stochastic_ipw_report.md`：自动聚合报告；
- `run30/per_split_results.csv`：1,350 行正式结果；
- `run30/environment_and_inputs.txt`：版本与哈希；
- `run30/status.txt`、`run30/gpu*.txt|csv`：运行状态；
- `smoke/`：1-repeat 预运行。

实现：

- `scripts/clip_outside_box_triage.py`；
- `scripts/stochastic_ipw_pu_probe.py`；
- `scripts/real_pu_no_adjudication_probe.py`。

