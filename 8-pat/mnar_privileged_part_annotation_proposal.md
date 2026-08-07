# Proposal：预算约束下的细粒度关键点主动标注

> **暂定英文题目**  
> **Which Images Should We Annotate? Benefit- and Safety-Aware Keypoint
> Acquisition for Fine-Grained Recognition**
>
> **文档状态：Draft v1.1；2026-07-28 已触发最终 No-Go，本 proposal 不再是 active 研究方向**  
> **研究定位：Fine-grained Recognition / Few-shot Learning / Learning with
> Privileged Information / Active Annotation**

---

## 1. 当前核心问题

> **最终裁决（PAT-D-260728-010）：停止 CUB 稀疏关键点主动标注路线。**
>
> 三个新 10-shot episode 上，Random-K1 相对 Global 的平均优势为
> +8.67pp，但同架构 PrPool-K0 已达到 69.33% BA。K1 相对 K0 的真实平均
> 增量只有 +0.40pp（类别 bootstrap 95% 区间 −0.28 至 +1.10pp），Full
> Oracle 相对 K0 也只有 +1.10pp。两个冻结的关键点价值门均失败。此前
> “K1 保留 71.8% Oracle 增益”的解释混入了 Global 与 PrPool 的架构差异，
> 不再作为关键点因果价值结论。CCT 与所有 final splits 保持锁定。

以下问题是本轮实验所检验、现已停止的历史问题：

在固定的极低关键点标注预算下，完整类别标签和普通图像都已知，但只有少量图像
能够获得训练期关键点。当前研究回答：

> **应该选择哪些图像进行关键点标注，才能最大化细粒度识别收益，同时控制类别
> 级负迁移？**

CUB `PAT-D-260728-004` 曾给出一个表面正向前提：每个外层 fold 中每类只随机标注一张
图像（训练候选的 12.5%），三次独立选择得到 69.00%–69.65% OOF balanced
accuracy，平均保留 Full-Keypoint Oracle 增益的 71.8%。但 K1 的平均类别负
迁移率仍为 24.2%，最差类别 recall delta 达到 −50pp。`PAT-D-260728-010`
证明该“保留率”使用了架构不匹配的 Global 基线，不能解释为关键点贡献。

因此论文贡献不能是“稀疏关键点监督有效”或单独的一条预算曲线；这些内容与
Privileged Pooling 的 sample-efficiency 论述重叠。候选贡献必须同时包含：

1. 不读取关键点的图像级主动选择策略；
2. 平均收益与类别安全双门；
3. CUB 与 CCT20+ 的跨数据确认；
4. 双数据开发门全部通过后才进行一次性 final test。

历史冻结路线为：

- `PAT-D-260728-005`：CUB K1 策略筛查；
- `PAT-D-260728-006`：获胜策略与 Random 的三组配对 seed 确认；
- `PAT-E-260728-001`：CCT20+ Oracle 与策略迁移；
- `PAT-F-260728-001`：一次性 CUB official test 与 CCT Cis/Trans。

截至 `PAT-D-260728-007`，上述主动选择路线已触发停止条件：
`PAT-D-260728-005` 的四个 K1 单点策略均未通过双门；随后最后一次 K2
集合级验证中，Feature-Facility 为 69.60% BA / 23.5% 负迁移率，
Gradient-Facility 为 69.80% / 23.0%，仍未超过 70.18% 收益门或 17.5%
安全门。因此当前 proposal 不再把“普通图像侧主动选择关键点标注样本”写成已
支持的方法贡献；CCT20+ 与 final test 保持锁定，等待新的研究问题而不是继续
增加启发式。

随后 `PAT-D-260728-008` 固定三套 Random-K1 mask，测试分类保护型辅助梯度
投影。训练中平均 76.9% 的 batch 检测到梯度冲突，但相对 Naive 的平均 BA
变化为 −0.07pp，类别负迁移率只降低 0.17pp，均未通过双门。这说明 batch
全局负点积不是类别级负迁移的充分代理；当前也不能把简单 PCGrad 式安全训练
写成方法贡献。所有 final splits 继续锁定。

策略只能读取图像路径、类别、fold 和冻结普通图像特征，禁止接收关键点坐标。
事后审计确认，关键点价值和类别负迁移必须相对同架构 PrPool-K0 计算；相对
Global 的差值只能评价完整系统，不能作为关键点因果效应。

---

## 2. 历史动机与已停止的 MNAR 路线

以下内容保留为问题形成过程和停止性证据，不再定义当前方法目标。

### 2.1 原核心矛盾

部件标注常被用于帮助细粒度模型关注局部判别证据。现有研究已经证明，训练期
关键点或部件监督可以改善数据效率和跨场景泛化。但是，这类方法通常将拥有部件
标注的训练样本视为可直接信任的监督来源，很少区分这些样本是否代表最终目标
分布。

WikiChurches 实验呈现出一个更具体的矛盾：

- 官方构件框相较匹配随机区域包含明显更强的风格信息；
- 带框训练子集内部的局部分类高度可分；
- 但三代局部融合器均在独立 validation 上发生类别级负迁移；
- 偏移集中于被选择提供构件框的 90 个训练 church，而不是完整 canonical
  train。

对应证据为 `PAT-B-260727-002`、`PAT-B-260727-003/004/005` 与
[`PAT-B-260728-001`](./wiki/实验日志/PAT/诊断实验/PAT-B-260728-001.md)。

因此：

> **局部标注有信息，不等于局部标注具有代表性；局部标注有代表性，也不等于
> 其知识能够安全传递到最终分类。**

本研究不再把主要问题定义为框外漏标正例，而是研究局部特权标注的选择性覆盖。

---

## 3. 原 MNAR 科学问题（已停止）

设训练集为：

\[
\mathcal D=\{(x_i,y_i,s_i,s_i z_i)\}_{i=1}^{N},
\]

其中：

- \(x_i\)：图像；
- \(y_i\)：最终细粒度类别，对所有训练样本可用；
- \(z_i\)：部件点、框或 mask 等训练期特权标注；
- \(s_i\in\{0,1\}\)：该样本是否获得部件标注。

本研究关注的不是普通半监督学习。类别标签 \(y_i\) 从未缺失；选择性缺失的是
辅助的部件特权信息 \(z_i\)。

核心问题为：

> 当 \(s_i\) 依赖图像、类别、姿态、部件可见性或部件典型性时，能否识别局部
> 监督的有效支持范围，并只在其预期收益可靠时迁移局部知识，从而避免少样本
> 细粒度分类中的负迁移？

---

## 4. 与现有工作的边界

### 4.1 非随机缺失标签学习

ICLR 2022 的
[CADR](https://iclr.cc/virtual/2022/poster/6177) 与 ICCV 2023 的
[PRG](https://openaccess.thecvf.com/content/ICCV2023/html/Duan_Towards_Semi-supervised_Learning_with_Non-random_Missing_Labels_ICCV_2023_paper.html)
已研究类别标签非随机缺失。因此，
MNAR、propensity、imputation 或 doubly robust 不能单独作为本研究创新。

本研究的区别是：

- 最终类别标签完整；
- 缺失的是部件特权标注；
- 主要终点是部件知识是否损害最终分类。

### 4.2 支持域隔离

AAAI 2023 的
[Small-Paced Self-Training](https://xie-zheng.cn/assets/pdf/aaai23-xiez.pdf)
已研究过滤机制引起的 labeled /
unlabeled support isolation。因此，渐进式伪标注或 Wasserstein 邻域扩展也
不能单独构成创新。

本研究需要回答的是：部件教师在什么支持范围内值得被最终分类器采用。

### 4.3 Privileged Pooling

TPAMI 2023 的
[Privileged Pooling](https://arxiv.org/abs/2003.09168) 是最接近工作。
它已经覆盖：

- 训练期关键点监督；
- 细粒度物种识别；
- 少样本；
- 偏置相机陷阱数据；
- 只有部分训练图像具有关键点的设置。

因此，“稀疏部件监督改善少样本分类”不能作为新贡献。

当前可保留的差异是：

- 把部件标注可用性 \(s\) 作为显式随机变量；
- 系统区分 MCAR、MAR、MNAR 与 support violation；
- 评价平均收益之外的类别级和机制级负迁移；
- 要求安全机制不能退化为永远关闭局部知识。

### 4.4 部分特权信息与选择性蒸馏

[`LUPAPI`](https://pmc.ncbi.nlm.nih.gov/articles/PMC7872470/) 已研究只在
部分训练样本中存在的特权信息；
[selective privileged distillation](https://openaccess.thecvf.com/content/CVPR2023W/FGAHI/papers/Aslam_Privileged_Knowledge_Distillation_for_Dimensional_Emotion_Recognition_in_the_Wild_CVPRW_2023_paper.pdf)
也已研究错误教师导致的负迁移。本研究必须比较这些直接适配，
不能只把两者组合后称为创新。

---

## 5. 原 MNAR 研究假设

### H1：选择性部件标注会造成可重复的下游负迁移

在部件标注比例相同的条件下，MAR/MNAR 选择机制应比 MCAR 更容易导致局部
教师或蒸馏学生损害 global-only。

`PAT-D-260728-002` 在 CUB 25% 关键点标注预算下未支持该假设：MCAR 为
69.85% BA，而 MAR-X、MNAR-Z、SI-HARD 分别为 70.15%、70.60%、70.00%。
该反证限于偏向典型/关键点完整样本的当前机制和强度，但在出现新的相对 MCAR
伤害证据前，H1 不得写成已验证事实。

随后 `PAT-D-260728-003` 将预算降至每类 1 张，并选择最低典型性、最低关键点
完整度和单侧姿态支持。MCAR-1 为 69.65%，三个偏置臂分别为 69.55%、
69.85% 和 69.10%；最大下降仅 0.55pp。第二个预注册门仍未通过，因此当前
CUB/PrPool 上的 H1 方法路线停止。

### H2：信息性、代表性和可迁移性可以实验分离

部件教师可在带标注子集和完整 mask Oracle 上表现良好，但其无条件迁移仍可能
在未覆盖样本或特定类别上失败。

### H3：支持感知的条件收益控制可以减少负迁移

若模型同时估计：

- annotation support；
- 局部教师相对全局模型的条件收益；
- 该收益的不确定性；

则可以在不完全关闭局部知识的情况下，优于无条件部件蒸馏。

以上均为待验证假设，不是既定结论。

---

## 6. 原候选方法框架

候选框架暂不命名，由四部分组成。

### 6.1 Global reference

使用全部 \((x_i,y_i)\) 训练全局分类器：

\[
g(x_i)=\operatorname{logits}_{global}(x_i).
\]

它既是主模型，也是安全参照。

### 6.2 Privileged part teacher

只在 \(s_i=1\) 的样本上利用部件标注 \(z_i\)，构建部件池化表示和局部教师：

\[
t(x_i,z_i)=\operatorname{logits}_{part}(x_i,z_i).
\]

教师训练必须使用 image/class-disjoint 或 OOF 预测，避免把拟合训练样本误判为
知识收益。

### 6.3 Annotation support and conditional benefit

估计：

\[
\hat e(x,y)=P(s=1\mid x,y)
\]

以及局部教师相对 global reference 的条件收益：

\[
\Delta(x,y)=R_g(x,y)-R_t(x,z,y).
\]

当选择概率接近 0 时，模型必须报告 support violation，而不是通过极端 IPW
外推。

### 6.4 Risk-controlled transfer

学生模型只接收能够由普通图像特征预测的局部 residual：

\[
f(x)=g(x)+a(x)\,r(x),
\]

其中 \(a(x)\) 由支持程度和收益置信下界共同决定。若证据不足，
\(a(x)\rightarrow0\)，模型退回 global reference。

为了避免“安全”退化为永远关闭局部知识，必须同时报告：

- 局部分支激活率；
- 激活样本覆盖类别数；
- 激活区域的真实收益；
- 与 global-only 的平均和最差类别差异。

---

## 7. 原 MNAR 实验路线

### 当前实证状态

PartImageNet 三次 Oracle 门未建立正上界，因此该路线已经停止。CUB
`PAT-D-260728-001` 建立了 Full-Keypoint Oracle 相对 Global 的 +5.50pp
上界；随后 `PAT-D-260728-002` 在相同 25% 预算下比较 MCAR、MAR-X、
MNAR-Z 和 SI-HARD。四个部分标注臂均比 Global 高 4.40–5.15pp，三个偏置
臂也均未比 MCAR 差，预注册选择偏差门因此未通过。

这一结果将当前研究边界改为：不能直接开发纠偏方法。下一步必须先在独立冻结的
更强支持隔离设置中复现“偏置缺失相对 MCAR 造成伤害”；若仍失败，应收缩或
放弃 H1，而不是继续增强方法复杂度。

### 阶段 A：受控问题验证

使用
[PartImageNet Seg split](https://github.com/TACJu/PartImageNet)：

- train/validation 共享类别；
- test 全程冻结；
- 完整 part mask 作为隐藏 Oracle；
- 人为产生固定标注率的 MCAR、MAR、MNAR 和 support-isolation。

首先回答：

1. 相同标注预算下，MNAR 是否比 MCAR 更容易导致负迁移？
2. 完整 part Oracle 是否仍有足够下游增益？
3. global-only 是否掩盖类别级伤害？

### 阶段 B：最小安全机制

比较：

- Global-only；
- Naive privileged distillation；
- class-balanced / clipped IPW；
- PRG/CADR 思路的直接适配；
- Small-Paced Self-Training 思路的直接适配；
- Privileged Pooling；
- 候选 support-aware risk control；
- Full-part Oracle。

### 阶段 C：Few-shot 与 OOD

只有阶段 A/B 通过后，才进入 PartImageNet OOD split：

- base / validation / novel 类别互斥；
- 1/2/5/10-shot；
- 多随机种子；
- 验证部件知识能否迁移到 novel classes。

### 阶段 D：真实选择偏差压力测试

WikiChurches 只作为真实选择偏差场景：

- 不再用 validation 调整融合规则；
- canonical test 继续冻结；
- 报告 support violation 与类别级失败；
- 不把其未知选择机制当作合成 MNAR 的因果验证。

CUB 可作为点监督泛化实验，但不作为完整区域 mask Oracle。

---

## 8. 首个历史实验：PAT-C-260728-001

首个实验只做小规模可行性判断：

- PartImageNet Seg split；
- train-only 确定 Quadruped 中训练样本最多的 20 类；
- 冻结统一视觉 backbone；
- 每类最多 80 张 train 图用于模型开发；
- part annotation rate 为 20%；
- 三个固定随机种子；
- test 图像读取数必须为 0。

缺失机制：

1. MCAR：类别内随机抽取；
2. MAR-X：选择概率依赖全局视觉典型性；
3. MNAR-Z：选择概率依赖隐藏 mask 的可见部件面积与完整性；
4. SI-Hard：按典型性与部件可见性选取 top 20%，制造支持域缺口。

首轮只比较 Global、Naive、Clipped-IPW、Support-aware 与 Full-part Oracle。

### Go 条件

同时满足：

1. Oracle 相对 Global 的 validation balanced accuracy 至少提高 2pp；
2. Naive 在至少两个偏置机制中相对 MCAR 多产生至少 2pp 负迁移，或最差类别
   下降至少 5pp；
3. Support-aware 在偏置机制平均相对 Global 至少提高 1pp；
4. 所有偏置机制中最差类别下降不超过 2pp；
5. 相对 Naive 在最困难机制至少提高 2pp；
6. 非零局部激活率位于 10%–90%，且覆盖不少于 80% 的类别；
7. 三个种子方向一致。

若 Oracle 不超过 Global，说明当前 backbone/数据设置中部件信息没有可转移
上界，停止该原型。若 Support-aware 只通过完全关闭局部分支达到安全线，同样
判定 No-Go。

### 8.1 已完成结果

train-only 五折中，选中 Full-Part Oracle 相对 Global 提高 2.00pp，且最差
类别下降 1.25pp，刚好允许进入一次性 validation。validation 的三个 seed
均为正增益，但平均只提高 0.74pp，且每个 seed 的最差类别均下降 11.11pp。

因此，`PAT-C-260728-001` 对“冻结 CLIP 线性部件注意力 + additive local-logit
residual”判定 **No-Go**，并按协议停止 NAIVE/IPW/support-aware。该结果不否定
非随机缺失部件特权标注问题；它否定的是用一个缺少足够 Oracle 上界的局部头
继续研究缺失纠偏。

### 8.2 参考机制复核：PAT-C-260728-002

下载并核对 Privileged Pooling 原文与官方代码后，第二个机制门改用 3×3 卷积
sigmoid 注意力、四个受监督部件图与一个互补图、逐图加权平均池化、L2 归一化
后拼接，以及单一分类头。它不再使用 additive local logits。

全程只使用 train 五折。最佳 PrPool-inspired Oracle OOF 为 93.4375%，相对
CLIP CLS Global 的 91.8125% 提高 1.625pp，但最差类别下降 6.25pp；6 个候选
均不满足安全线。由此停止所有“冻结 CLIP patch + 新局部头”变体，且没有再次
读取 validation。

### 8.3 有限骨干适配：PAT-C-260728-003

最后一次预注册机制升级解冻 CLIP 视觉编码器最后一个 residual block 与
`ln_post`，并在同一 train-only 五折下公平比较 Adapted Global 和
Adapted PrPool Full-Part Oracle。Adapted Global 达到 94.5625% OOF balanced
accuracy，而完整部件 Oracle 为 94.0625%，下降 0.5000pp；最差类别下降
2.5000pp。

该结果同时未满足 +2.5pp 收益门和 −2pp 类别安全门。因此依照停止规则：

- 停止 PartImageNet 上该机制族的方法开发；
- 不运行 MCAR/MAR/MNAR/support-isolation correction arms；
- validation/test 均保持未读取、未编码；
- 研究题目只在新的正向 Oracle 基准上继续，或转为诊断/基准贡献。

---

## 9. 评价指标

主要指标：

- Balanced Accuracy；
- Macro-F1；
- Top-1 Accuracy；
- worst-class recall delta；
- negative-transfer class rate；
- negative-transfer mechanism rate；
- local activation rate；
- support-violation rate。

统计单位为图像；类别汇总使用等权 macro。最终完整实验至少使用五个种子，并
报告 bootstrap 置信区间。首轮 pilot 使用三个固定种子，只用于 Go/No-Go。

---

## 10. 候选贡献

只有实验通过后，才允许形成以下贡献：

1. 定义类别标签完整、部件特权标注非随机缺失的学习问题；
2. 建立完整 mask Oracle 下的 MCAR/MAR/MNAR/support-isolation 协议；
3. 量化部件监督的信息性、代表性和可迁移性分离；
4. 提出在非平凡使用局部知识约束下控制负迁移的方法；
5. 在合成机制与 WikiChurches 真实选择偏差之间建立压力测试。

当前不能使用“首次提出”或“SOTA”等表述。

---

## 11. 风险与停止规则

1. **近邻工作风险**：若 Privileged Pooling 或 MNAR-SSL 的直接适配已达到候选
   方法结果，则方法贡献不成立。
2. **Oracle 风险**：若完整部件监督不能改善最终分类，停止部件迁移方法。
3. **全关闭风险**：若安全机制主要依赖关闭局部分支，判定为无方法贡献。
4. **不可识别性**：真实 MNAR 无额外假设时不可完全恢复；必须报告假设与
   support violation。
5. **预训练重叠**：PartImageNet 来源于 ImageNet；foundation backbone 可能存在
   预训练重叠。首轮只做同 backbone 相对比较，完整论文需补充无重叠或从头训练
   控制。
6. **开发污染**：同一 validation 只能用于冻结协议后的单次确认；失败后不能
   继续针对该 validation 调 gate。

---

## 12. 历史下一步（已由当前四阶段路线取代）

`PAT-C-260728-001/002/003` 已依次检验 additive residual、论文式冻结
patch-head 和有限 backbone adaptation；三者均未建立稳定的完整部件 Oracle
上界。PartImageNet 方法开发现已停止。

继续该题目有两条合规路线：

1. **方法路线**：在 CUB 等已有部件/关键点监督正向先例的数据上，先原样复现
   Privileged Pooling 的正 Oracle，再冻结数据和缺失机制，研究 MCAR/MAR/MNAR
   与安全迁移；
2. **诊断路线**：将 WikiChurches 与 PartImageNet 的结果组织为“部件监督何时
   伤害”的选择偏差、支持缺口与负迁移基准，不再声称已有有效纠偏方法。

在新数据集通过 Oracle 门之前，不继续设计 support-aware correction，以避免
在没有可转移信号的设置中优化缺失机制。

方法路线的首个协议已冻结为
[`PAT-D-260728-001`](./experiments/mnar_privileged_part_learning/configs/PAT-D-260728-001_protocol.json)：
只使用 CUB 官方 train、每类 10-shot、五折 OOF，比较同一 ResNet-50
`layer4` 适配预算下的 Global 与 15 关键点 Full Oracle；官方 test 在该门控中
禁止读取。

该门控现已完成：Global OOF balanced accuracy 为 65.45%，Full-Keypoint
Oracle 为 70.95%，五折全部为正，总增益 +5.50pp，超过 +2pp 门槛。因此研究
题目可在 CUB 上继续。

但 46/200（23%）类别下降，最差观测类别差为 −40pp。每类仅有 10 个 OOF
预测，该差值较离散，但已足以说明“平均有效”不等于“类别安全”。下一步先冻结
机制并验证等预算 MCAR/MAR/MNAR/support-isolation 是否产生系统性差异，再决定
是否开发 support-aware correction；官方 test 继续冻结。

对应筛查协议冻结为
[`PAT-D-260728-002`](./experiments/mnar_privileged_part_learning/configs/PAT-D-260728-002_protocol.json)：
每个 fold 的 8 张/类训练图中只给 2 张关键点标注，等预算比较 MCAR、MAR-X、
MNAR-Z 与 SI-Hard；所有 Naive arms 固定训练 9 轮，不做超参搜索。只有当至少
一个偏置机制比 MCAR 低 2pp，或负迁移类别率高 0.10，才扩展到另外两个种子和
纠偏基线。

该筛查现已完成，且门控未通过：MCAR 为 69.85%，MAR-X 为 70.15%，MNAR-Z
为 70.60%，SI-HARD 为 70.00%。三个偏置臂相对 MCAR 均未下降，类别负迁移率
也未增加 0.10。操纵检查显示选择机制确实改变了典型性或关键点完整度，因此不能
把结果解释为选择掩码无差异。

据此，没有扩展 seed 7602/7603，也没有开始纠偏方法。随后冻结并完成
`PAT-D-260728-003`：预算降为每类 1 张，并按最低典型性、最低关键点完整度和
单侧姿态制造更强压力。MCAR-1 为 69.65%，三个偏置臂为 69.55%、69.85%、
69.10%，最大下降仍只有 0.55pp，第二次门控失败。

因此不再继续增强合成伤害，也不开发 correction。当前可辩护的新方向是：
“少量关键点标注的价值与样本选择稳健性”——每类仅 1 张关键点标注仍相对
Global 提高 4.20pp，并保留 Full Oracle 5.50pp 增益中的大部分。若坚持 MNAR
纠偏题目，则必须转到一个事先已有真实选择伤害、而非继续人为构造伤害的基准。

该新方向已由 `PAT-D-260728-004` 独立复核：每类随机标注 1/2/4 张，各做三个
嵌套选择 seed，K1/K2/K4 平均 BA 分别为 69.40%、69.68%、70.00%，Global
为 65.45%，Full Oracle 为 70.95%。K1 平均保留 71.8% Oracle 增益，三个
选择的范围只有 0.65pp，预注册稀疏价值门与选择稳健性门均通过。

随后 `PAT-D-260728-005/007/008` 分别否定了图像级主动选择、集合级
coverage 选择与简单梯度安全投影。最终可靠性审计 `PAT-D-260728-009` 在三个
新 10-shot episode 上复现了 K1/Full PrPool 相对 Global 的高分，但也暴露出
池化架构混杂。

`PAT-D-260728-010` 补上同架构零关键点对照：三个 episode 的
K1−K0 为 +0.75、+0.45、+0.00pp，平均 +0.40pp；Full−K0 平均 +1.10pp。
稀疏与完整关键点价值门均失败。因此不再推进 CUB 关键点预算、主动选择、
类别安全或 CCT20+ 迁移，下一项目必须更换核心问题或数据设定。

---

## 13. 参考文献与内部证据

1. Hu X, Niu Y, Miao C, Hua XS, Zhang H. *On Non-Random Missing Labels in
   Semi-Supervised Learning*. ICLR, 2022.
   https://iclr.cc/virtual/2022/poster/6177
2. Duan Y, Zhao Z, Qi L, et al. *Towards Semi-supervised Learning with
   Non-random Missing Labels*. ICCV, 2023.
   https://doi.org/10.1109/ICCV51070.2023.01477
3. Xie Z, Sun H, Li M. *Semi-supervised Learning with Support Isolation by
   Small-Paced Self-Training*. AAAI, 2023.
   https://xie-zheng.cn/assets/pdf/aaai23-xiez.pdf
4. Rodríguez AC, D'Aronco S, Schindler K, Wegner JD. *Fine-Grained Species
   Recognition with Privileged Pooling: Better Sample Efficiency Through
   Supervised Attention*. TPAMI, 2023.
   https://doi.org/10.1109/TPAMI.2023.3316718
5. Sabeti E, Drews J, Reamaroon N, et al. *Learning Using Partially Available
   Privileged Information and Label Uncertainty*. IEEE JBHI, 2021.
   https://doi.org/10.1109/JBHI.2020.3008601
6. Aslam MH, Pedersoli M, Koerich AL, Granger E. *Privileged Knowledge
   Distillation for Dimensional Emotion Recognition in the Wild*. CVPRW, 2023.
   https://openaccess.thecvf.com/content/CVPR2023W/FGAHI/html/Aslam_Privileged_Knowledge_Distillation_for_Dimensional_Emotion_Recognition_in_the_Wild_CVPRW_2023_paper.html
7. He J, Yang S, Yang S, et al. *PartImageNet: A Large, High-Quality Dataset of
   Parts*. ECCV, 2022. https://arxiv.org/abs/2112.00933
8. 项目内部选择偏差诊断：
   [`PAT-B-260728-001`](./wiki/实验日志/PAT/诊断实验/PAT-B-260728-001.md)。
9. 新方向机器可读预注册协议：
   [`PAT-C-260728-001`](./experiments/mnar_privileged_part_learning/configs/PAT-C-260728-001_protocol.json)。
