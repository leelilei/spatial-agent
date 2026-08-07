# 训练期关键点监督的 DINO 语义部件查询

## 当前定位

本方案是 PAT-H-260729-011 之后的研究重构，不延续 PASAC、类别特定稀疏
锚点重排或选择性纠错。首要任务不是直接提出 K1 主动标注算法，而是重新建立
一个严格的关键点价值上界：在同一冻结 DINOv2 表征和同一分类器下，完整
fold-training 关键点能否产生超过无关键点控制与 CLS 强基线的表示。

## 科学问题

冻结 DINOv2 的 CLS 已在三个 CUB train-only episode 上达到约 86.32% 平均
Balanced Accuracy。此前局部机制失败可能意味着 CLS 已包含大部分可用证据，
也可能意味着关键点只被用于类内锚点或注意力辅助损失，没有被用于学习跨类别
共享的语义部件定位器。

本方案检验：

> 仅用外折训练部分的语义关键点，能否在冻结 DINOv2 patch token 空间拟合
> 跨类别部件查询器，并把所有图像转换成无需推理期关键点的部件表征，从而
> 同时提高 held-out 部件定位与少样本分类？

## 方法：Semantic Part Query

### 1. 冻结输入

- DINOv2 ViT-B/14；
- deterministic 392x392 direct resize；
- 28x28 patch tokens 与 CLS token；
- backbone 完全冻结。

### 2. Full semantic detector

对每个外折，只从 fold-training 图像抽取可见关键点所在 patch token，标签为
15 个语义部件之一；同时从远离所有可见关键点的位置抽取背景 token。使用固定
`RidgeClassifier(alpha=1)` 拟合 16 类线性 token detector。

外折评价图像的关键点只用于 localization metric，不能进入 detector、阈值或
分类器拟合。

### 3. Architecture-matched K0 control

K0 使用相同的 15 路空间注意力和相同的输出维度，但 detector score 全为零，
因此每个部件都是对 784 个 patch 的均匀池化。Full 与 K0 的唯一区别是训练期
关键点监督拟合的 detector。

### 4. Keypoint-free representation

对每个语义部件，将 detector 在 784 个 patch 上的分数逐图 z-score 后做空间
softmax，并加权池化原始 DINO patch token。15 个部件向量等权平均得到
`semantic_part_mean`。最终表示为归一化 CLS 与归一化 part mean 的等权拼接，
分类器固定为 `RBF SVC(C=3, gamma=scale)`。

推理阶段不读取关键点。

## 第一机制门：PAT-I-260729-001

只使用 CUB official train episode 1 五折 OOF，比较：

1. `CLS_RBF`：当前 86.20% 强基线；
2. `K0_UNIFORM_PART_RBF`：CLS + uniform mean-patch；
3. `FULL_SEMANTIC_PART_RBF`：CLS + Full semantic part mean。

同时报告 held-out 关键点 3x3-token hit rate。该指标只验证 detector 是否定位
到目标邻域，不冒充标准 PCK。

全部条件同时满足才 Go：

- Full 相对 K0 至少 `+0.50pp`；
- Full 相对 CLS_RBF 至少 `+0.50pp`；
- Full hit rate 相对 K0 至少 `+10pp`；
- 相对 K0 的受损类别数不超过改善类别数；
- 最差类别 recall delta 不低于 `-20pp`。

失败则停止该语义查询路线，不调 Ridge alpha、背景数、attention temperature 或
融合权重。通过后才单独冻结 K1 协议，再研究随机 K1 与主动选择。

## 与既有工作的边界

训练期关键点监督注意力、pose-normalized few-shot、label-only part discovery、
transformer patch selection 和 DINO-assisted keypoint detection 均已有先例。本
方案不能把这些组件单独写成创新。潜在贡献只可能来自以下组合及其严格因果
对照：

> 在冻结 foundation-token 空间学习跨类别语义部件查询，用训练期关键点把所有
> 图像转换成 keypoint-free 表征，并相对 uniform pooling 与强 CLS 分类器同时
> 验证增量。

这只是待验证的创新边界，不是“首次”声明。

## 条件路线

1. Full oracle gate 通过：冻结机制，进入每类一张关键点的 K1 实验；
2. K1 在新 episode 通过：比较 Random 与预注册主动选择；
3. episode 4/5 冻结确认通过：进入 CCT20+ 开发验证；
4. 双数据开发门通过后：才允许创建 final-evaluation lock；
5. 任一前置门失败：停止，不读取 official test。

## 2026-07-29 机制门结果

PAT-I-260729-001 已完成并判定 No-Go。Full 语义查询器获得 82.86% 的
held-out 3x3-token hit rate，并将同管线 K0 从 80.90% 提高到 85.50%；但
CLS RBF 为 86.20%，Full 低 0.70pp，且最差类别相对 K0 下降 30pp。

因此当前证据支持“线性语义监督可以定位冻结 DINO patch 中的 CUB 部件”，
不支持“语义部件池化能给 CLS 增加分类信息”。按冻结协议停止，不进入 K1、
主动选择或后续数据集，也不调整 detector/pooling/fusion 超参数。
