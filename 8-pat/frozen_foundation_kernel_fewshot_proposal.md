# 冻结视觉基础模型的双容量核选择

## 论文定位

目标改为一篇可投 EI 会议的实证方法论文：不再依赖关键点或小样本神经适配，
而是研究冻结视觉基础模型的容量、分类器几何和类别风险。方法部分采用简单的
Dual-Capacity Kernel Selection（DCKS），实验部分复用已有完整负结果作为
“复杂适配未必优于强冻结表征”的边界证据。

## 方法

对同一图像提取 L2-normalized DINOv2-B/14 与 L/14 CLS 特征，分别构造
`gamma=scale` 的 RBF kernel。DCKS 的候选库包括：

- B-only；
- L-only；
- B/L additive kernel，L 权重 0.25、0.50、0.75；
- B/L geometric-product kernel，L 权重 0.25、0.50、0.75。

每个外折只在其 fold-training 数据上进行四折 inner OOF，按 Balanced Accuracy
选择 kernel mode；外折标签不参与选择。最终分类器统一为 `SVC(C=3,
kernel=precomputed)`。

该方法不声称发明 multiple-kernel learning。方法价值在于：不使用 query 标签、
不训练神经网络，并把容量选择纳入每个 few-shot task 内部的无泄漏估计。

## Episode 1 筛查门

论文路线 Go 需要同时满足：

1. DCKS 相对固定 DINOv2-B RBF 至少 `+1.0pp`；
2. 五个外折至少四折不低于 B；
3. 相对 B 的受损类别数不超过改善类别数；
4. 最差类别 recall delta 不低于 `-30pp`；
5. 完整报告 DCKS 相对 L-only 的结果与选择模式，不把 L endpoint 冒充融合。

通过后，完全冻结 kernel bank、inner selection 和 classifier，在 train-only
episodes 2/3 确认。两者都为正且三 episode 平均增益至少 `+0.75pp`，才判
论文路线正式 Go，并进入第二数据集。

## 预计论文贡献

1. 200-way few-shot fine-grained 条件下的严格 frozen-foundation protocol；
2. 一个 task-local、nested-OOF 的双容量核选择方法；
3. 容量、kernel geometry、类别风险、局部监督与 PEFT 负结果的统一分析；
4. 至少一个独立细粒度数据集上的冻结确认。

## 停止与诚实边界

- 若 L 与 DCKS 都不能相对 B 提升 1pp，不再扩大 backbone grid；
- 若 DCKS 只选择 L-only，论文改为 empirical benchmark，不能宣传 kernel fusion；
- CUB official test、CCT Cis/Trans 在第二数据开发门前保持锁定。
