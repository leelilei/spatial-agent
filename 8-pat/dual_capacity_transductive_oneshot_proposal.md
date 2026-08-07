# 双容量转导原型细化：200-way 1-shot 细粒度识别

## 当前判定

项目从 200-way 10-shot 归纳分类转向 200-way 1-shot 转导分类。这个转向不是
换弱分类器，而是将每类可用标签从十张降为一张，并明确允许模型联合使用
九张无标签查询图像。冻结 DINOv2-B/L 仍是全部方法的共同特征基础。

`PAT-K-260729-003` 在两个未参与方法选择的 CUB train-only episodes 上通过
冻结确认门；`PAT-K-260729-004` 补齐公开转导基线，`PAT-K-260729-005` 完成
query-prior 压力测试，`PAT-K-260729-006` 又在三个互不重叠的 Stanford Dogs
train-only episodes 上通过跨数据冻结门。因此当前为 **paper-level empirical
route GO**。论文定位是准确率--效率折中，不宣称精度 SOTA。

## 研究问题

在 200 类细粒度 1-shot 任务中，单张支持图容易形成有偏原型。不同容量的
冻结视觉基础模型提供互补几何；无标签查询集合则可用于修正单样本原型。
本文研究：能否在不训练神经参数的条件下，将双容量表征和类别均衡的转导
原型细化结合，稳定改善高类别数 1-shot 识别？

## 方法：DCTPR

Dual-Capacity Transductive Prototype Refinement（DCTPR）包含四步：

1. 对每张图提取冻结 DINOv2-B/14 和 DINOv2-L/14 CLS，并分别 L2 归一化；
2. 拼接 B/L 特征后再次归一化，每类唯一支持图作为初始原型；
3. 以温度 0.05 的余弦分数执行类别均衡 Sinkhorn 软分配；
4. 用支持原型和该类软查询中心等权更新并归一化，固定重复三次。

模型不读取查询标签，不训练神经参数。查询集合在当前基准中已知每类恰有
九张图；该均衡先验必须在论文中显式说明，并通过不均衡实验补充边界。

## 冻结结果

| CUB train-only episode | BL nearest support | B refine | L refine | BL Sinkhorn | DCTPR |
|---|---:|---:|---:|---:|---:|
| Episode 1（开发） | 68.42% | 73.84% | 73.46% | 73.79% | **75.14%** |
| Episode 2（确认） | 68.12% | 73.22% | 73.22% | 73.44% | **74.71%** |
| Episode 3（确认） | 67.96% | 73.13% | 72.92% | 73.26% | **74.69%** |
| 三集均值 | 68.17% | 73.40% | 73.20% | 73.50% | **74.85%** |

DCTPR 相对 BL 归纳基线三集平均提高约 `+6.68pp`。相对每集最强的已实现
同预算比较项，三集分别提高约 `+1.30pp`、`+1.27pp` 和 `+1.43pp`。

## 公开强基线与跨数据结果

| Dataset | BL nearest support | DCTPR | TIM-ADM | MAP-RAW | signed PT-MAP | LaplacianShot |
|---|---:|---:|---:|---:|---:|---:|
| CUB-200（3 episodes） | 68.17% | **74.85%** | 76.19% | 74.30% | 74.37% | 68.30% |
| Stanford Dogs（3 episodes） | 64.09% | **70.36%** | 70.01% | 70.97% | 70.94% | 64.43% |

在 CUB 上，DCTPR 比最强 TIM-ADM 低 1.35pp，但单轮推理约 0.033 秒，
比 TIM-ADM 快约 3.8 倍。在 Stanford Dogs 上，DCTPR 比最强 MAP-RAW 低
0.61pp，但快约 49 倍，并略高于 TIM-ADM。Dogs 三个 episode 相对 BL
nearest support 分别提高 +5.94pp、+6.58pp 和 +6.29pp，30/30 个支持轮换
全部正向。

## Query-prior 压力边界

在 CUB mild 3--9 和 severe 1--9 类别计数不均衡时，仍强制均匀先验的 DCTPR
宏平均 BA 只有 68.34% 和 68.86%；使用真实类计数的 oracle 控制可恢复到
73.35% 和 72.87%。这说明当前方法的主要适用边界是已知均衡 query prior。
论文必须把这一点作为 limitation，而不是把 oracle 控制写成可部署方法。

## 已关闭分支

Dual-Capacity Consensus Refinement（DCCR）在 Episode 1 为 75.18%，仅比
BL refinement 高 0.04pp，且只有 6/10 个轮换不低于后者，未通过预注册门。
一致性加权不能作为论文贡献，也不再继续调参。

## 文献边界

以下机制均已有工作，必须作为相关工作或强基线而非创新点：

- LaplacianShot：Laplacian-regularized transductive inference
  (Ziko et al., 2020, doi:10.48550/arXiv.2006.15486)；
- TIM：transductive information maximization
  (Boudiaf et al., 2020, doi:10.48550/arXiv.2008.11297)；
- PT-MAP：特征分布变换与 MAP/optimal-transport refinement
  (Hu et al., 2020, doi:10.48550/arXiv.2006.03806)；
- balanced-query evaluation 的现实性风险
  (Veilleux et al., 2022, doi:10.48550/arXiv.2204.11181)；
- iterative graph/prototype refinement 与 conditional transport 等后续方法。

## 论文贡献边界

可主张的贡献是一个面向 200-way 细粒度 1-shot 的简单组合方法、严格的
多 episode 冻结验证，以及容量融合、转导分配和原型更新的分解实验。不能
主张首次使用 Sinkhorn、首次原型更新、首次特征拼接或当前 SOTA。

## 当前论文主张

1. DCTPR 是面向高类别数、均衡 1-shot transduction 的简单无训练适配器；
2. 六个跨数据 episode 中均稳定改善 frozen dual-capacity nearest support；
3. 相对每个数据集的最强公开基线只损失 0.61--1.35pp，但推理快 3.8--49 倍；
4. 类别不均衡实验明确量化均匀 query prior 的适用边界。

2026-08-05 已在不可变锁后完成一次 official-test 审计。CUB official test 上
DCTPR 为 74.64%，相对 BL-NCC 提升 6.69pp，距 TIM-ADM 1.53pp；Dogs 三个
互不重叠的 official-test episodes 上 DCTPR 为 70.49%，相对 BL-NCC 提升
6.92pp，距 MAP-RAW 0.99pp。测试标签未用于调参，后续禁止从 official-test
结果反向修改超参数。结果保持准确率--效率故事，但仍不能声称 accuracy SOTA。

## SAGE 准确率新最佳探索：冻结确认失败

在 Dogs Episodes 1--3 上，TIM-ADM 与 MAP-RAW 一致时取共同预测、否则取
signed PT-MAP 的 SAGE 规则比最强单 solver 高 +0.170pp。该规则在 Episodes
4--6 manifest 和特征创建前冻结，并设定三项联合门槛。确认集上 SAGE 为
69.633%，最强 signed PT-MAP 为 69.571%，只提高 `+0.0617pp`，未达到
`+0.10pp` 主门；另外两门为 2/3 episode 胜出和 23/30 rotation 非劣，均通过。

因此 SAGE 为 **No-Go**，不能称 matched-protocol new best，更不能称全局 SOTA。
Episodes 4--6 不得再用于选择另一套 ensemble 规则。此阴性结果不改变 DCTPR
准确率--效率论文的 paper-level GO，但关闭了在现有 Dogs 协议上继续搜索微小
融合增益的路线。
