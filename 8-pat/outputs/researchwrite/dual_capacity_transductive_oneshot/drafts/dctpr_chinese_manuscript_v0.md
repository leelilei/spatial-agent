# Fast Dual-Capacity Transductive Prototype Refinement for High-Way One-Shot Fine-Grained Recognition

## 摘要

视觉基础模型显著提高了少样本识别的表征质量，但在高类别数 one-shot 任务中，
每类唯一支持图仍会形成有偏原型。现有转导方法能够利用无标签查询集修正决策，
却常需较长的迭代优化。本文提出 Dual-Capacity Transductive Prototype
Refinement（DCTPR）：拼接冻结 DINOv2-B/14 与 L/14 的归一化 CLS 特征，以
类别均衡的软分配估计查询中心，并用三步固定原型更新完成任务级适配。DCTPR
不训练神经参数，也不读取查询标签。我们在 CUB-200 和 Stanford Dogs 上构造
六个仅使用官方训练划分的高类别数 1-shot episodes。DCTPR 相对双容量最近支持
基线分别提高 6.68 和 6.27 个百分点。在 CUB 上，DCTPR 达到 74.85%，比最强
TIM-ADM 低 1.35 个百分点但快约 3.8 倍；在 Stanford Dogs 上达到 70.36%，
比最强 MAP-RAW 低 0.61 个百分点但快约 49 倍。类别不均衡压力测试进一步表明，
均匀查询先验是当前方法的重要适用条件。结果支持将 DCTPR 定位为一种面向
均衡、高类别数 one-shot 细粒度任务的轻量准确率--效率折中方案。

## 1. 引言

少样本细粒度识别同时面临类间差异细微和类内变化显著的问题。冻结视觉基础
模型能够提供强表征，但 one-shot 条件下每类只有一个有标签样本，类别原型会
受到姿态、背景和拍摄条件的显著影响。转导式 few-shot learning 通过联合使用
无标签查询集缓解原型偏差，代表方法包括 LaplacianShot、TIM 和 PT-MAP。
然而，这些方法要么依赖图优化，要么执行较长的交替更新或最优传输迭代。

本文研究一个更窄而实用的问题：在冻结基础模型已经很强的情况下，能否用一个
无训练、短迭代的任务适配器取得接近强转导优化器的精度？为此，我们组合两个
容量不同的 DINOv2 表征，并执行固定三步的类别均衡原型细化。贡献如下：

1. 提出 DCTPR，一个用于高类别数 1-shot 细粒度识别的轻量双容量转导适配器；
2. 在 CUB-200 和 Stanford Dogs 的六个 train-only episodes 上进行完全冻结验证；
3. 与 TIM-ADM、MAP/PT-MAP 和 LaplacianShot 进行同特征、同任务的匹配比较，
   展示接近最强精度但显著更低的推理成本；
4. 通过两档类别不均衡实验量化均匀查询先验的失效边界。

## 2. 相关工作

简单分类器与强表征的研究表明，few-shot 性能在很大程度上取决于预训练特征。
DINOv2 提供了可直接迁移的通用视觉特征。转导推断方面，LaplacianShot 使用
查询图上的拉普拉斯正则，TIM 最大化查询预测与类别之间的互信息，PT-MAP
利用特征分布变换、最优传输和 MAP 原型更新。DCTPR 不声称重新发明这些组件，
而是研究双容量冻结表征和短程软原型细化在高-way 细粒度任务中的效率边界。

## 3. 方法

给定每类一个支持样本及无标签查询集，分别提取冻结 DINOv2-B/14 与 L/14
的 CLS 特征。两个特征先独立 L2 归一化，再拼接并再次归一化。每类支持特征
构成初始原型。查询与原型的余弦分数除以固定温度 0.05 后，通过 Sinkhorn
归一化得到行和为 1、列和等于已知每类查询数的软分配。

对类别 c，使用软分配加权得到查询中心。新原型为原支持特征与查询中心的等权
和，并再次归一化。该过程固定执行三次。所有参数在 CUB Episode 1 后冻结，
Stanford Dogs 不参与任何方法或基线参数选择。

## 4. 实验设计

CUB-200 使用 200-way 1-shot/9-query，Stanford Dogs 使用 120-way
1-shot/9-query。每个数据集构造三个 10-shot train-only episodes，每个 episode
进行十个支持位置轮换。Dogs 三集互不重叠，共使用 3,600 张官方训练图像。
所有 official test 图像均未解码或编码。

比较方法包括双容量 nearest support、无原型更新的 balanced Sinkhorn、
TIM-ADM、MAP-RAW、适配 signed DINO 特征的 PT-MAP，以及 LaplacianShot。
LaplacianShot 的 lambda 只在 CUB Episode 1 从作者公开网格选择，之后冻结。
主指标为跨轮换 balanced accuracy，并报告单轮推理时间。

## 5. 结果

在 CUB-200 上，nearest-support、DCTPR 和 TIM-ADM 分别为 68.17%、74.85%
和 76.19%。DCTPR 超过 MAP-RAW、signed PT-MAP 和两种 LaplacianShot，
比 TIM-ADM 低 1.35 个百分点，但推理时间为 0.033 秒，对比 TIM-ADM 的
0.126 秒。在 Stanford Dogs 上，DCTPR 从 64.09% 提高到 70.36%，三个
episode 的增益均超过 5.9 个百分点，30 个轮换全部正向。最强 MAP-RAW 为
70.97%，但单轮耗时 1.679 秒，约为 DCTPR 的 49 倍。

在 mild 3/9 与 severe 1--9 类别计数压力下，DCTPR 的均匀先验臂只有
68.34% 和 68.86%；使用真实类计数的 oracle 控制达到 73.35% 和 72.87%。
因此，大部分退化来自错误的类别边际，而不是特征几何完全失效。

## 6. 讨论

DCTPR 的优势不是最高绝对精度，而是在零神经训练和三步固定更新下取得稳定的
跨数据增益。其最重要限制是需要已知均衡查询先验。真实数据流通常不满足这一
条件，oracle-count 结果只能说明潜在上限，不能视为部署方案。另一个限制是
公开基线采用共同 DINO 特征上的匹配更新规则重实现，而非直接运行旧仓库中的
原始 backbone 管线。后续工作应研究不读取标签的类别先验估计，并在开放集和
流式查询条件下验证。

## 7. 结论

本文给出一个简单、快速且可复现的双容量转导原型细化方法。六个跨数据
train-only episodes 表明，DCTPR 能稳定回收 one-shot 原型偏差造成的大部分
损失，并以显著更低的计算成本接近更复杂的转导优化器。其结论严格限定于已知
均衡查询先验；类别不均衡结果同时给出了方法有效范围和下一步改进方向。

## 参考文献骨架

1. Oquab et al. DINOv2: Learning Robust Visual Features without Supervision. 2023.
2. Ziko et al. Laplacian Regularized Few-Shot Learning. ICML, 2020.
3. Boudiaf et al. Transductive Information Maximization for Few-Shot Learning. NeurIPS, 2020.
4. Hu et al. Leveraging the Feature Distribution in Transfer-based Few-Shot Learning. 2020.
5. Veilleux et al. Realistic Evaluation of Transductive Few-Shot Learning. 2022.
6. Khosla et al. Novel Dataset for Fine-Grained Image Categorization: Stanford Dogs. 2011.
