# PASAC 定向文献查重记录

检索日期：2026-07-28  
目标：判断“稀疏语义关键点校准 K0 注意力通道置换，并以 K0 教师保持分类能力”是否存在直接同题工作。

## 最接近工作

| 工作 | 已覆盖内容 | 与 PASAC 的关键差异 |
|---|---|---|
| [Privileged Pooling（2020）](https://arxiv.org/abs/2003.09168) | 训练期关键点监督的注意力池化；包含完全相同结构的无注意力监督对照 | 使用完整 privileged annotations；未研究每类一张图、K0 通道置换校准或教师保持 |
| [Semi-supervised Keypoint Localization（2021）](https://arxiv.org/abs/2101.07988) | 少量关键点标签、未标注图像、语义一致性和增强一致性 | 目标是关键点定位，不是 few-shot 细粒度分类，也不从强 K0 分类注意力通道出发 |
| [Weakly Supervised Keypoint Discovery（2021）](https://arxiv.org/abs/2109.13423) | 图像级监督与 viewpoint equivariance 的关键点发现 | 不使用稀疏语义关键点去校准既有分类注意力通道 |
| [SEAM（CVPR 2020）](https://arxiv.org/abs/2004.04581) | 自监督 equivariant attention consistency | 面向弱监督语义分割；没有语义关键点和通道身份分配 |
| [PDiscoNet（ICCV 2023）](https://arxiv.org/abs/2309.03173) | 仅图像标签的细粒度部件发现；含 equivariance、集中度、正交性等约束 | 无稀疏语义关键点；不做 K0 通道到已命名部件的一对一校准 |
| [AttentionShift（CVPR 2023）](https://openaccess.thecvf.com/content/CVPR2023/html/Liao_AttentionShift_Iteratively_Estimated_Part-Based_Attention_Map_for_Pointly_Supervised_Instance_CVPR_2023_paper.html) | 点监督注意力与部件级迭代修正 | 面向实例分割；单点是实例监督，不是类别内稀疏关键点预算 |
| [Keypoint-Guided Optimal Transport（2023）](https://arxiv.org/abs/2303.13102) | 少量匹配关键点指导跨域最优传输 | 面向域适应和图像翻译；不是分类注意力通道的语义身份分配 |

## 查重判断

- **不能使用的宽泛创新表述**：“首次用稀疏关键点做一致性学习”“首次用关键点监督注意力”“首次做弱监督部件发现”。这些均有明显近邻。
- **当前可保留的窄创新表述**：“面向 few-shot 细粒度分类，以 fold-local 一对一分配解决 K0 注意力通道置换，再用 K0 教师保持抑制稀疏微调漂移。”
- 当前检索未找到四个条件同时出现的直接工作，但尚未完成所有引用链、中文数据库与付费数据库检索，因此只能写成“据我们的检索”，不能写“世界首次”。

## 对实验设计的直接影响

查重迫使方法必须包含两个可独立验证的机制，而非普通一致性损失：

1. `WARMSTART_IDENTITY → PERMUTATION_ONLY` 验证通道置换校准；
2. `PERMUTATION_ONLY → PASAC` 验证教师保持；
3. 分类指标之外必须报告语义 attention hit rate，证明改进确实来自通道语义化。

