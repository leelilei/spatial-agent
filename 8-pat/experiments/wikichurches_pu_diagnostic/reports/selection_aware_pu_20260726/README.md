# Selection-aware PU propensity-proxy 诊断

日期：2026-07-26

## 决策

**No-Go，不接入下游 few-shot 分类。**

简单 propensity-proxy 加权相对标准 nnPU 只有极小且不稳定的改善，并且仍
显著差于 PN 和 Ignore。继续调权重或类先验容易变成同一测试协议上的
后验调参，不能形成可信方法证据。

## 为什么只能称为 propensity proxy

当前 U 是每个图像—标签组合按冻结 CLIP 分数确定性选择的 top-3。条件于
排序变量，候选纳入概率是 0 或 1，缺少 overlap，因此真实 candidate
selection propensity 不可识别。

本轮只构建探索性 proxy：

1. 用 CLIP ViT-B/16 编码区域；
2. 用目标文本相似度、log 面积、log 长宽比、中心 x/y 区分官方 P 与 U；
3. 以 class-balanced Logistic Regression 估计 proxy `e(x)`；
4. 对 P 使用归一化 `1/e(x)` 权重；
5. 在 nnPU 正风险和负风险修正项中使用相同权重。

它建模的是当前样本内的“官方框样式 versus top-3 U 样式”，不是已识别的
因果标注概率。

## 实验

- 图像：50；
- 官方框 P：237；
- 框外候选 U：708；
- 标签：9；
- 30 个按图像隔离的 split / 标签；
- 方法：PN、Ignore、三档 nnPU、两档 SA-nnPU；
- 类先验：标准 nnPU 0.10/0.25/0.50，SA-nnPU 固定 0.25；
- propensity floor：0.10/0.20；
- 结果：1,890 行；
- GPU：RTX 2080；
- 耗时：454 秒；
- 峰值显存：1,594 MiB；
- 退出码：0。

## 聚合结果

| 方法 | ROC-AUC | 95% CI | AP | 95% CI |
|---|---:|---:|---:|---:|
| PN | 0.862 | 0.784–0.926 | 0.557 | 0.428–0.662 |
| Ignore | 0.874 | 0.816–0.921 | 0.551 | 0.449–0.649 |
| nnPU(π=0.10) | 0.728 | 0.627–0.826 | 0.405 | 0.275–0.538 |
| nnPU(π=0.25) | 0.746 | 0.635–0.848 | 0.422 | 0.272–0.570 |
| nnPU(π=0.50) | 0.785 | 0.664–0.887 | 0.472 | 0.316–0.606 |
| SA-nnPU(π=0.25) | 0.749 | 0.635–0.851 | 0.427 | 0.278–0.573 |

两个 propensity floor 得到相同结果，因为 raw proxy propensity 的最小值
均值为 0.543，0.10/0.20 截断都没有激活。

## 关键配对差值

| 对比 | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| SA-nnPU − nnPU(π=0.25) | +0.002 | -0.003–+0.008 | +0.005 | -0.003–+0.014 |
| SA-nnPU − PN | -0.114 | -0.163–-0.064 | -0.130 | -0.191–-0.060 |
| SA-nnPU − Ignore | -0.126 | -0.193–-0.062 | -0.124 | -0.204–-0.026 |

相对标准 nnPU，SA-nnPU 的标签级 AUC 差值在 9 个标签中 6 个为正，
但幅度很小且总体区间跨 0。相对 PN，9/9 个标签均为负；相对 Ignore，
8/9 个标签为负。

## 权重诊断

- raw `e(x)` 最小值均值：0.543；
- raw `e(x)` 中位数均值：0.778；
- raw `e(x)` 最大值均值：0.889；
- P 权重有效样本量均值：7.16；
- ESS 范围：5.62–8.90。

ESS 没有塌缩，因此失败不能简单归因于极端大权重。主要问题是当前 proxy
只产生温和重加权，无法修复 top-k U 的结构性选择偏差。

## 结论边界

可以得出：

1. 简单逆 proxy-propensity 加权不足以修复标准 nnPU；
2. 当前 selection-aware 实现未通过接入下游分类的门槛；
3. deterministic top-k 设计缺少 propensity overlap；
4. 若继续无裁决路线，应先改变候选采样设计。

不能得出：

1. 所有 selection-aware PU 都无效；
2. U 中没有真实遗漏正例；
3. PN 或 Ignore 对真实遗漏构件最优；
4. 真实 Oracle gap 为零。

## 后续实验状态

以下重设计已经完成：

1. 导出完整框外候选母集；
2. 按预先固定的随机策略采样 U，并记录已知纳入概率；
3. 使用已知 inclusion probability 做 IPW，而不是从 deterministic
   top-k 结果反推 propensity；
4. 仍只评估已知标签稳定性，不声称遗漏正例恢复精度。

结果见 `reports/stochastic_ipw_pu_20260726/README.md`。IPW 在聚合层面
接近 FullPool，但 FullPool PU 仍低于 Ignore，因此采样偏差不是主要瓶颈。

如果目标是判断真实漏标、Oracle gap 或最终论文主张，则仍需要少量人工
裁决；当前无裁决路线已经达到可识别性上限。

## 证据文件

- `run30/real_pu_report.md`：自动聚合报告；
- `run30/per_split_results.csv`：1,890 行原始结果；
- `run30/environment_and_inputs.txt`：版本和输入哈希；
- `run30/status.txt`：退出码与耗时；
- `run30/gpu.csv`、`run30/gpu_summary.txt`：GPU 监控；
- `smoke/`：1-repeat 预运行。

实现位于 `scripts/real_pu_no_adjudication_probe.py`。
