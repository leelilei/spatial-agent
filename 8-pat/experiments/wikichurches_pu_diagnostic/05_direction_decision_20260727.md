# 2026-07-27 方法方向裁决

## 结论

下一步不再围绕 TOGA 调参，也不把 nnPU/IPW 或伪正例扩展换皮后接入 TOGA。
保留“选择性局部标注可能有用”这一研究问题，但将方法表述由
**missing-positive recovery** 改为：

> 从选择性、非穷尽的正例区域锚点学习局部判别证据，同时对未标区域保持
> abstention。

建议的工作名为 **Positive-only Box-Anchor Token Adapter**。名称只是内部
占位，专项查重后再确定。

## 为什么必须换核心机制

今天的证据共同排除了三条路径：

1. nnPU/IPW 风险估计显著弱于 Ignore；
2. 保守高置信正例扩展仍弱于 Ignore；
3. TOGA 在 WikiChurches 上经过 validation-only 调参后，冻结确认仍以
   1 胜 8 负结束。

TOGA 的 18 个规则裁块也与 WikiChurches 的小型建筑构件不匹配。即使继续
优化教师权重，也没有解决空间粒度和区域监督接口的问题。

## 新母体

- 主分类器：保留已验证更强的 Tip-Adapter-F；
- 局部表示：改用高分辨率 ViT dense patch tokens，而不是 TOGA 的 18 个
  粗裁块；
- 框特征：将官方框映射到 token 网格，用 masked pooling 或 RoIAlign 提取；
- 语义：第一版只使用图像的建筑风格标签，不依赖难以解释的英文构件名称。

## 新增机制

对已标框内 token 施加单边正锚约束：

- 要求对应风格的局部响应在框内达到最小置信度；
- 框外 token 不进入区域 BCE 的负项；
- 不生成完整伪框，不估计未知类先验；
- 图像级标签通过 MIL/log-sum-exp 聚合监督至少一个局部证据；
- 最终局部 logit 通过 validation 学到的标量门控与 Tip-F 融合；
- 推理时不需要构件框。

关键点是“框内需要高响应”，而不是“框外必须低响应”。因此它不会重复今天
已经失败的 PN、PU 或 pseudo-positive 路线。

## 先做的判别性实验

### Box-vs-Random 信息探针

1. 只使用 train split 中带官方框的图像，并按 church ID 隔离；
2. 提取 336/448 分辨率的 frozen dense tokens；
3. 对每个官方框生成同图、同面积和近似长宽比的随机对照区域；
4. 比较官方框与随机区域对建筑风格的 class margin、线性探针和 prototype
   分类准确率；
5. 使用图像内配对 bootstrap 或 permutation test。

预设 GO 条件建议为：

- 官方框的平均 class margin 高于匹配随机区域；
- 95% 配对区间下界大于 0；
- 至少 3/4 风格方向一致；
- church-disjoint 验证准确率至少提高 2 个百分点。

若不通过，停止整个局部框方向；若通过，再实现 token adapter。

## 与已有工作的边界

- RegionCLIP 已证明 global CLIP 与区域文本存在域差，并提供区域级预训练；
- CPEA 已使用 class-aware patch embeddings 和 dense patch matching 做
  few-shot 分类；
- CLIP-MHAdapter 已用 patch-token self-attention 做街景属性分类；
- PU purification 和 incomplete-label ranking 也已有先例。

因此不能把“patch token、区域 CLIP、MIL 或 PU”单独写成创新。待验证的差异
只能是：

> 面向选择性专家局部框的 positive-only box anchoring、未标 token
> abstention，以及它对 few-shot VLM 最终分类的作用。

## 参考入口

- RegionCLIP, CVPR 2022:
  https://openaccess.thecvf.com/content/CVPR2022/html/Zhong_RegionCLIP_Region-Based_Language-Image_Pretraining_CVPR_2022_paper
- CPEA, ICCV 2023:
  https://openaccess.thecvf.com/content/ICCV2023/html/Hao_Class-Aware_Patch_Embedding_Adaptation_for_Few-Shot_Image_Classification_ICCV_2023_paper.html
- CLIP-MHAdapter, arXiv 2026:
  https://arxiv.org/abs/2602.16590
- Positive-Unlabeled Data Purification, CVPR 2021:
  https://openaccess.thecvf.com/content/CVPR2021/html/Guo_Positive-Unlabeled_Data_Purification_in_the_Wild_for_Object_Detection_CVPR_2021_paper.html

## Box-vs-Random 正式结果

`PAT-B-260727-002` 已按上述预设条件完成：

- 官方 train+val：97 张图 / 97 个 church；
- 官方框：433；
- 同图面积和长宽比匹配随机对照：3,464；
- test 图像编码数：0；
- 图像级 style-margin 配对差：`+0.00649`；
- 配对 bootstrap 95% CI：`+0.00511–+0.00803`；
- Romanesque、Gothic、Baroque 为正，Renaissance 为 `−0.00026`；
- church-disjoint prototype balanced accuracy：
  官方框 `73.43%`，随机区域 `49.22%`，差 `+24.21pp`；
- 四项预设条件全部通过，区域信息探针判定为 **GO**。

3,464 个控制区域中只有 16 个（0.46%）超过 0.05 官方框重叠阈值，集中在
两个超大框。事后排除这两个框后，配对差仍为 `+0.00648`，95% CI 为
`+0.00509–+0.00803`，不改变结论。

该 GO 只允许进入 positive-only token adapter 原型，不允许直接声称最终
few-shot 分类有效，也不证明框外区域是真负例。

## Positive-only adapter 开发结果

`PAT-B-260727-003` 已完成最小原型的 validation-only 停止性实验：

- 448×448 CLIP dense tokens，28×28 patch grid；
- canonical train 中每个风格固定 16 个官方框锚点；
- 8 组同源随机框锚点作为负对照；
- Tip-Adapter-F 的 1/4/16-shot × seeds 1/2/3，共 9 个开发运行；
- 测试图编码数为 0。

1-shot 在 `top-1% patches, γ=20` 时平均提高 `+1.62pp`，但 4-shot 与
16-shot 按预设稳健规则都退回 `γ=0`。门槛只达到 1 个正稳健 shot、
1 个优于随机框的 shot 和 2/9 配对胜场，未达到 2、2、5 的要求，故判定
为 **NO-GO**，不运行测试确认。

事后诊断显示官方局部分支单独准确率仍有 `46.60%`，明显高于随机框均值
`25.49%`；失败不是“框无信息”，而是局部分数类别校准失衡：206 张验证图
中 91 张被局部分支预测为 Baroque，只有 19 张被预测为 Gothic。4-shot
融合对 Baroque 平均提高 `+12.18pp`，同时对 Gothic 降低 `−10.90pp`。

因此当前方向更新为：

> 停止原始 cosine 局部分数与全局 logits 的直接标量加和。若继续，只验证
> train-only、church-disjoint 的逐类 bias/scale 校准 residual evidence，
> 并以全局低置信门控限制局部分支的作用范围。

该方案仍需新的 validation-only 门槛，不能沿用本次开发集结果直接进入测试。

## Train-LOCO 类校准残差结果

`PAT-B-260727-004` 按上一节建议完成：

- 90 个带框 train church 逐一 leave-one-church-out；
- 每类 8 个官方锚点与 8 组随机锚点；
- 逐类负分布 z-score 校准；
- 基于 Tip-F 归一化 margin 的低置信 soft gate；
- 测试图编码数为 0。

总体表现明显比原始加和好：1-shot `+1.13pp`、3/3 seed 获胜；4-shot
`+0.97pp`、2/3 seed 获胜；正稳健 shot、官方优于随机框的 shot 和总胜场
三个门槛均通过。

但预设的类别安全门槛失败：

- Romanesque `+2.22pp`；
- Gothic `−10.26pp`；
- Renaissance `+2.78pp`；
- Baroque `+8.12pp`。

这说明低置信门控确实限制了局部分支的总体伤害，但逐类独立的 bias/scale
校准没有学习 Gothic–Baroque 的交叉混淆。最终仍为 **NO-GO**，不运行
测试确认。

若继续，本方向只剩一个有明确机制差异的最小实验：在 90 个 train-LOCO
church 上训练强收缩、class-balanced 的 4×4 multinomial residual head，
用 train 内 church-disjoint CV 选择正则强度，并把逐风格安全约束放进
validation 候选选择。Renaissance 只有 4 个 calibration church，因此该
版本必须强正则并报告不确定性；若仍失败，应停止 WikiChurches 局部框融合，
不再通过扩大网格或更换随机种子延长路线。

## Multinomial residual 最终结果

`PAT-B-260727-005` 已完成最后一次预先声明的局部融合实验。4×4
class-balanced ridge multinomial head 在 90 个 train-LOCO church 上选中
`λ=0.01`，稳健 CV balanced accuracy 为 `86.28%`，说明 train 带框子集内部
确实高度可分。

但迁移到独立 validation 后，1/4/16-shot 的全部非零候选都违反逐风格安全
线。最接近的候选分别为：

- 1-shot：总体 `+0.16pp`，稳健分数 `−0.34`，Gothic `−5.77pp`；
- 4-shot：总体 `+0.49pp`，稳健分数 `−0.39`，Gothic `−13.46pp`；
- 16-shot：总体 `−0.49pp`，稳健分数 `−0.73`，Gothic `−5.77pp`。

三个 shot 均按协议退回 `γ=0`，测试图编码数为 0。最终判定 **NO-GO**。

这一结果把问题从“融合公式不够好”进一步缩小为“带框 train 子集不代表
canonical validation 的局部证据分布”。查询时已 leave-one-church-out，
因此不能用同建筑泄漏解释 train CV 与 validation 的巨大落差。

### 最终方向

停止 WikiChurches 局部框到 Tip-F 的融合路线，不再调 λ、γ、gate 或 seed。
后续只有两条科学上可辩护的选择：

1. 将现有证据整理成选择性局部标注的诊断结果：官方框有信息，但这种信息
   在选择偏差下不能稳定传递到 few-shot 终点；
2. 获得覆盖更具代表性 church 的补全标注，或换用真正完整的区域监督数据，
   在新开发集上重新开始方法验证。

当前 canonical test 始终未用于三轮局部融合开发，继续保留为未来真正改变
数据条件后的冻结确认集。

## 2026-07-28 选择偏差诊断

`PAT-B-260728-001` 对上述解释进行了正式 church-level 检验。

- 同一 90 个带框 train church 的 Global CLIP prototype：
  train BA `84.46%`，validation BA `57.36%`，下降 `27.10pp`，
  风格分层置换 `p=0.00120`；
- Local residual：
  train OOF BA `86.22%`，validation BA `52.18%`，下降 `34.03pp`，
  分层置换 `p=0.00070`；
- Gothic local recall 从 `91.43%` 降到 `26.00%`，下降 `65.43pp`，
  局部偏移效应四风格第 1；
- 作为负对照，全部 5,750 个 canonical-train church 的 global CLIP
  与 validation 不显著偏移（`p=0.47965`），validation BA 反而高
  `3.90pp`。

因此得到比“一般 train–validation 域偏移”更精确的结论：

> 偏移集中于被选中提供构件框的 90 个 train church，而不属于完整
> canonical train。局部标注子集内部高度可分，但覆盖不足以代表验证分布。

这正式支持停止 adapter/fusion 调参。若不改变标注覆盖或数据集，继续开发
只会重复拟合带框子集与 canonical validation 之间的选择偏差。
