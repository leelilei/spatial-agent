---
document_type: agent-handoff
project: few-shot-fine-grained-recognition
date: 2026-07-29
status: paper-route-go-no-confirmed-accuracy-sota
official_test_decode_count: 5600_unique_images_in_locked_audit
last_completed_experiment: PAT-K-260729-008
supplementary_locked_audit: PAT-K-260805-009
supplementary_official_test_access: 2026-08-05
---

# Few-shot 细粒度识别项目 Agent 交接文档

## 1. 用户目标

用户希望完成一篇可投 EI 检索会议的论文，不追求顶级期刊。优先级如下：

1. 任务与已有论文不能高度重复；
2. 至少有一个能够说清楚的创新点；
3. 实验链条完整，整体故事逻辑自洽；
4. 不为了“看起来成功”篡改门槛或隐藏负结果；
5. 在双数据开发门通过前，不访问正式 test。

最初研究方向是：

> 在极低关键点标注预算下，主动选择最值得标注的图像，以提高少样本
> 细粒度识别并控制类别级负迁移。

经过 CUB 系列实验，稀疏关键点机制未能超过强基础模型，研究重心已逐步
转向冻结视觉基础模型的少样本分类几何。是否继续转向，应由后续 agent
和用户共同决定，不要默认原 proposal 已经成立。

## 2. 必读文件

- 原始 proposal：
  `/Users/mac/Documents/6-Research/8-pat/few_shot_fine_grained_proposal_and_experiment_design.md`
- PAT-H-001～009 系列总结：
  `/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_DINOv2Geometry_PAT-H-260729-Series/PAT-H-260729_series_result_report.md`
- 最新 LoRA PEFT 结果：
  `/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_LastBlockLoRA_PAT-H-260729-010/PAT-H-260729-010_result_report.md`
- 最新标准实验日志：
  `/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_LastBlockLoRA_PAT-H-260729-010/standard_experiment_log.md`
- 最新异常记录：
  `/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_LastBlockLoRA_PAT-H-260729-010/异常记录.md`
- 当前实验代码：
  `/Users/mac/Documents/6-Research/8-pat/experiments/dinov2_sparse_anchor/`
- 最新类别安全纠错结果：
  `/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_ClassSafeCorrection_PAT-H-260729-011/PAT-H-260729-011_result_report.md`
- 最新文献与创新边界审计：
  `/Users/mac/Documents/6-Research/8-pat/PAT-LIT-260729-011_literature_audit.md`
- 当前重构 proposal：
  `/Users/mac/Documents/6-Research/8-pat/dino_semantic_part_query_proposal.md`
- 最新 Full-Keypoint 语义查询结果：
  `/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_DINOSemanticPartQuery_PAT-I-260729-001/PAT-I-260729-001_result_report.md`
- 当前 1-shot DCTPR proposal：
  `/Users/mac/Documents/6-Research/8-pat/dual_capacity_transductive_oneshot_proposal.md`
- 最新冻结确认结果：
  `/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_DCTPRConfirmation_PAT-K-260729-003/PAT-K-260729-003_result_report.md`
- 最新公开强基线结果：
  `/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_PublishedBaselines_PAT-K-260729-004/PAT-K-260729-004_result_report.md`
- 最新跨数据结果：
  `/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_StanfordDogs_DCTPR_PAT-K-260729-006/PAT-K-260729-006_result_report.md`
- 中文论文初稿：
  `/Users/mac/Documents/6-Research/8-pat/outputs/researchwrite/dual_capacity_transductive_oneshot/drafts/dctpr_chinese_manuscript_v0.md`
- 已编译英文 LaTeX 论文：
  `/Users/mac/Documents/6-Research/8-pat/outputs/researchwrite/dual_capacity_transductive_oneshot/latex/main.tex`
- 八页 PDF 与构建 QA：
  `/Users/mac/Documents/6-Research/8-pat/outputs/researchwrite/dual_capacity_transductive_oneshot/latex/main.pdf`
  `/Users/mac/Documents/6-Research/8-pat/outputs/researchwrite/dual_capacity_transductive_oneshot/latex/BUILD_QA.md`
- DCTPR reference 检索与逐条核验报告：
  `/Users/mac/Documents/6-Research/8-pat/outputs/researchwrite/dual_capacity_transductive_oneshot/sources/reference_audit_20260729.md`
- SAGE 冻结确认结果：
  `/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_StanfordDogs_SAGE_PAT-K-260729-007/PAT-K-260729-007_result_report.md`
- DCPR 未知 prior 筛查结果：
  `/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_DCPR_PAT-K-260729-008/PAT-K-260729-008_result_report.md`
- SOTA 路线决策：
  `/Users/mac/Documents/6-Research/8-pat/SOTA_ROUTE_DECISION_2026-07-29.md`
- 不均衡转导公开协议审计：
  `/Users/mac/Documents/6-Research/8-pat/PAT-LIT-260729-012_imbalanced_tfsl_audit.md`

## 3. 当前最重要结论

### 3.0.1 PAT-K-260805-009 补充结果（2026-08-05）

在不可变 `FINAL_EVAL_LOCK.json` 后完成了 official-test 审计。CUB 使用一个
200-way 1-shot episode（每类测试图最少 11 张），DCTPR 为 74.64%，BL-NCC 为
67.95%，TIM-ADM 为 76.18%；Stanford Dogs 使用三个互不重叠的 official-test
episodes，DCTPR 均值 70.49%，BL-NCC 为 63.56%，MAP-RAW 为 71.48%。DCTPR
相对 BL-NCC 分别提升 +6.69pp/+6.92pp，距最强 matched solver 1.53pp/0.99pp。
官方测试未用于调参，不能由此声称 accuracy SOTA。

同一锁定包还完成了 official-train 的单变量敏感性：CUB/Dogs 上 `T=1,2,3,5`
均保持正向，递归替换 `lambda=1` 在 CUB 退化，temperature 对两数据集更敏感。
B/L 特征提取与峰值显存已独立记录，task-head 与 end-to-end 成本不再混报。
完整 JSON、CSV、锁和结果说明位于：
`outputs/researchwrite/dual_capacity_transductive_oneshot/supplementary_results/PAT-K-260805-009/`。

### 3.0.0 SOTA 探索结论：当前没有确认的 accuracy SOTA

PAT-K-007 的 SAGE 在三个 untouched Dogs episodes 上只比最强 signed PT-MAP
高 `+0.0617pp`，低于预注册 `+0.10pp`，最终 No-Go。PAT-K-008 的 DCPR 在
CUB unknown-prior 开发上比 TIM-ADM 高 `+0.9644pp`，关闭 46.6% oracle gap，
且内部迁移为 `+0.9657pp`、30/40 轮换非劣；但仍低于预注册 `+1.0pp` 开发门，
因此同样 No-Go，未生成 Dogs 确认 episode。

当前不能声称 global SOTA、matched-protocol new best 或确认性精度最优。不得
使用 Dogs Episodes 4--6 继续挑 SAGE 规则，也不得扩大 PAT-K-008 的候选 prior
公式。DCTPR 准确率--效率论文仍为 paper-level GO，不受两条 SOTA 探索失败影响。

公开标准不均衡 TFSL 是 5-way、75 queries、Dirichlet 类比例协议；已有 alpha-TIM、
PUTM、alpha-AM 和 UNEM 等强方法。PAT-K-005/008 的 200-way deterministic stress
与之不可直接比数。若另开 SOTA 项目，必须先复现公开标准协议和 matched backbone，
不能把当前自建压力集结果包装成全球 SOTA。

### 3.0 最新路线：DCTPR paper-level empirical route GO

用户要求停止在 86% 强基线上反复搜索微小增益，改为选择一个合理的低准确率
任务。项目已转向 CUB 200-way 1-shot transductive recognition：每类一张有标签
support，九张无标签 query；仍统一使用冻结 DINOv2-B/L，不通过弱化 backbone
人为降低基线。

Dual-Capacity Transductive Prototype Refinement（DCTPR）使用归一化 B/L 拼接
特征、temperature 0.05 的类别均衡 Sinkhorn、三步软原型更新和固定 0.5
支持/查询中心权重。最初 CUB 结果如下：

| Episode | BL nearest support | strongest implemented comparator | DCTPR |
|---|---:|---:|---:|
| 1（开发） | 68.42% | 73.84% | 75.14% |
| 2（确认） | 68.12% | 73.44% | 74.71% |
| 3（确认） | 67.96% | 73.26% | 74.69% |

Episode 2/3 冻结门全部通过：DCTPR 相对最强比较项 +1.27pp/+1.43pp，相对
归纳 BL 基线 +6.59pp/+6.73pp。三 episode 相对归纳基线平均约 +6.68pp。

PAT-K-004 已补齐 TIM-ADM、MAP/PT-MAP 和 LaplacianShot。在 CUB 上 DCTPR
74.85%，最强 TIM-ADM 76.19%；DCTPR 低 1.35pp，但推理快约 3.8 倍。
PAT-K-006 使用 Stanford Dogs 官方 train list 的三个互不重叠 episodes，DCTPR
均值 70.36%，相对 BL nearest support +6.27pp，30/30 轮换正向；最强
MAP-RAW 70.97%，DCTPR 低 0.61pp但快约 49 倍。Dogs 三项冻结门全部通过。

因此当前是 **paper-level empirical route GO**，论文主张必须是准确率--效率
折中，不能声称精度 SOTA。PAT-K-005 同时确认：不均衡 query 下 uniform-prior
DCTPR 会退回约 68--69%，均衡 query prior 是明确限制。标准 Sinkhorn、原型
更新和拼接均不是独立创新；DCCR 仍为 No-Go。此处“official test 访问为 0”是
2026-07-29 的历史状态；2026-08-05 已按 PAT-K-260805-009 不可变锁完成审计。

### 3.1 已稳定确认的强基线

当前最稳定方案是：

> 官方冻结 DINOv2 ViT-B/14 CLS 特征 + RBF SVC（C=3）。

使用标准 `SVC.predict` 口径：

| CUB train-only episode | Balanced Accuracy |
|---|---:|
| Episode 1 | 86.20% |
| Episode 2 | 86.85% |
| Episode 3 | 85.90% |
| 三 episode 均值 | 约 86.32% |

此前 PASAC 为 70.75%，因此强基线绝对提高约 15.57pp。

注意：

- 这是性能提升，不是充分的方法创新；
- “DINOv2 + RBF”本身不能直接包装成论文核心贡献；
- 后续任何候选方法必须与 86.2%/86.32% 强基线比较，不能再与弱
  LogReg 或旧 PASAC 单独比较。

### 3.2 正式 test 状态

- CUB official test 解码/编码次数：2026-07-29 时为 `0`；2026-08-05 锁定审计
  使用 2,000 个 unique test images（B/L 各编码一次）
- CCT Cis/Trans 解码次数：`0`
- 当前没有 `FINAL_EVAL_LOCK.json`
- 不允许因为开发实验不理想而提前查看 test。

## 4. 已完成实验及结论

| 实验 | 目的 | 关键结果 | 判定 |
|---|---|---:|---|
| PAT-H-001 | DINOv2 基础表征与稀疏锚点 | CLS-Ridge 84.60%；CA-SAP 最佳 78.30% | 稀疏锚点失败 |
| PAT-H-002 | 强 Ridge 上的局部残差 | 84.70%，仅 +0.10pp | 失败 |
| PAT-H-003 | 冻结分类器筛查 | RBF 分数口径 86.10%；标准 predict 为 86.20% | 强基线建立 |
| PAT-H-004 | 自适应双几何融合 | 自适应臂无提升；秩融合开发集 86.60% | 主机制失败 |
| PAT-H-005 | 秩融合跨 episode 确认 | Episode 2 +0.15pp；Episode 3 −0.25pp | 确认失败 |
| PAT-H-006 | 查询多视图平均 | 最佳 86.10%，单视图 86.20% | 失败 |
| PAT-H-007 | 静态特征残差适配器 | 85.25%，参考 86.20% | 失败 |
| PAT-H-008 | 支持集多视图扩展 | 86.10%，参考 86.20% | 失败 |
| PAT-H-009 | 局部尺度核 | 86.30%，仅 +0.10pp | 失败 |
| PAT-H-010 | 图像增强 + 最后一层 LoRA | PEFT-RBF 86.05%，参考 86.20% | 失败 |
| PAT-H-011 | 嵌套 OOF 类别安全选择性纠错 | 86.20%，0 次改判，参考 86.20% | 失败 |
| PAT-I-001 | Full-Keypoint DINO 语义部件查询 | Full 85.50%；K0 80.90%；CLS 86.20%；hit 82.86% | 失败 |

## 5. 最近两项实验

### 5.1 PAT-H-260729-010：最后层 LoRA

### 方法

- 冻结 DINOv2 ViT-B/14；
- 仅在最后一个 transformer block 的以下线性层注入 LoRA：
  - `attn.qkv`
  - `attn.proj`
  - `mlp.fc1`
  - `mlp.fc2`
- LoRA rank 8、alpha 16、dropout 0.05；
- trainable backbone 参数：98,304；
- cosine head 由 fold-training 冻结特征类中心初始化；
- 图像增强：RandomResizedCrop、水平翻转、ColorJitter；
- 12 epochs，batch size 8，五折 seed 9601–9605。

### 正式结果

| Fold | Frozen RBF | PEFT head | PEFT RBF |
|---|---:|---:|---:|
| 0 | 85.50% | 86.25% | 85.25% |
| 1 | 87.50% | 87.25% | 88.00% |
| 2 | 86.50% | 85.50% | 85.25% |
| 3 | 85.75% | 86.50% | 86.00% |
| 4 | 85.75% | 84.50% | 85.75% |
| 总体 | 86.20% | 86.00% | 86.05% |

主臂 `PEFT_RBF` 相对参考为 `−0.15pp`，未达到预注册的 `+1.0pp`。
训练准确率在第 5～6 epoch 达到 100%，主要问题是少样本过拟合。

### 门控

- 不生成 episode 4/5；
- 不访问官方 test；
- 不继续调 LoRA rank、epoch、loss 或融合权重；
- `screen_success = false`。

### 5.2 PAT-H-260729-011：类别安全选择性纠错

- 五折嵌套 OOF，所有策略参数只用每个外折的训练部分学习；
- RBF reference：86.20%；
- selective correction：86.20%；
- actions / wins / harms：0 / 0 / 0；
- 只有 outer fold 3 的 inner OOF 接受 `94 -> 97`，外层未触发；
- `screen_success = false`；
- 不生成 episode 4/5，不进入 CCT20+，不访问 official test。

## 6. 已排除或不建议重复的路线

除非有全新的理论或证据，不要重复消耗 GPU 运行：

1. DINO patch token 的稀疏关键点传播；
2. confusion-aware part weighting；
3. Ridge/RBF 后的简单局部分数重排；
4. RBF 与 prototype/ridge 的静态或置信度融合；
5. 查询图翻转/中心裁剪特征平均；
6. 将多视图只扩展到 support set；
7. 缓存 CLS 上的残差 MLP/对比适配器；
8. 局部尺度自适应 RBF；
9. ViT-B 最后一层 LoRA 的直接超参数微调。

这些方向均已出现“不增益、跨 episode 反向或明显过拟合”。

## 7. 下一步建议

### 当前唯一主线：写作与图表

PAT-K-004/005/006 已补齐公开强基线、query-prior stress 和第二数据集，不能
继续搜索新的 DCCR、路由、融合权重、温度或 prior estimator。下一步只允许：

1. 将中文 v0 按 EI 会议格式改写为英文；
2. 生成主结果、效率和 query-prior stress 图表；
3. 核对参考文献元数据和 matched-reimplementation 表述；
4. official test 可保持锁定；若确需一次最终评估，必须先建立不可变 lock。

英文全文已经扩充为可编译的通用双栏 LaTeX 初稿，共 8 页、PDF 提取约 5,262
词，包含方法公式、TikZ 流程图、accuracy--runtime Pareto 图、逐 rotation
稳定性图、query-prior 边界图、组件分解、强基线效率比较、讨论和复现声明。
图形由归档 JSON 经 Python 脚本重建，附 source-data CSV、PDF/SVG/TIFF/PNG。
最终日志无 undefined citation/reference、无 overfull box；八页均已渲染检查。
作者信息仍为 `Anonymous Authors`，当前不是
特定会议官方模板。下一步应先确定 EI 会议，再迁移 document class、页数限制、
作者单位、参考文献样式和会议要求的声明，不再补方法搜索。

SAGE 与 DCPR 均已关闭。不要继续搜索 solver pair、fallback、prior estimator、
收缩系数或放宽门槛。若用户坚持 accuracy SOTA，必须另立项目，先复现公开 5-way
Dirichlet imbalance protocol 的 alpha-TIM、PUTM、alpha-AM/UNEM-family 强基线；
未完成 matched reproduction 前，不允许把任何自建 train-only protocol 结果称 SOTA。

以下 PAT-H/PAT-I 内容是历史停止记录，不再覆盖当前 PAT-K 主线。

### 历史：PAT-H-260729-011 后的状态更新

首选的类别安全选择性纠错已按冻结协议完成，结果为 No-Go：RBF 与纠错臂
均为 86.20%，最终没有外层样本被改判。只有 outer fold 3 在 inner OOF 中
找到 `94 -> 97` 的零伤害可靠 pair，但该 pair 未在对应外层评价触发。

因此：

1. 不生成 episode 4/5；
2. 不进入 CCT20+；
3. 不放宽 pair 支持数、允许历史伤害或事后降低 +0.50pp 门槛；
4. 当前冻结 DINOv2-B 上的启发式方法搜索停止；
5. official test 继续保持 0 次使用。

若继续项目，下一步必须由用户明确选择研究重构方向，而不是自动追加实验：

- 回到稀疏关键点主动选择，设计真正由关键点监督驱动的训练目标；或
- 将项目改写为冻结基础模型下的系统性负结果/几何评估，并重新判断目标
  EI 会议是否接受该类贡献；或
- 先做 DINOv2-L 冻结基线，仅测性能上限，但不把它当成方法创新。

### 历史：PAT-I-260729-001 重构结果

用户选择继续修改后，项目按新 proposal 测试了“训练期关键点监督直接构造
DINO 语义部件表征”。Full detector 在 held-out 关键点上达到 82.86% 的
3x3-token hit rate，并相对同管线 K0 提高 +4.60pp；但 Full 分类为 85.50%，
低于 CLS RBF 86.20%，且最差类别相对 K0 为 -30pp。

该结果说明关键点可以定位 DINO patch 中的语义部件，但当前聚合未给 CLS
增加判别信息。按冻结协议：

1. 不运行 K1；
2. 不恢复主动选择；
3. 不调整 detector、attention temperature、融合权重或分类器；
4. 当前关键点方法重构路线停止；
5. official test 与 CCT 继续锁定。

### 历史方案：类别安全选择性纠错

> 历史建议，已由 PAT-H-260729-011 的 No-Go 结果关闭。以下内容仅保留为
> 冻结实验的设计依据，不再作为自动执行路线。

下一步不应继续调 LoRA，也不应立即把更大 backbone 当成方法。当前缺少的
不是更高的基础精度，而是一个能够稳定超过强 RBF、同时控制类别伤害的
核心机制。

当时首选方向为：

> 基于强 RBF 的类别安全选择性纠错：只对低置信、且有可靠纠错证据的
> 样本修改预测，其余样本保持 RBF 原预测。

推荐按以下顺序推进：

1. 先做针对性文献查重，重点检查与 transductive refinement、
   LaplacianShot、TIM、置信度路由、选择性分类和 confusion-pair
   calibration 的差异；
2. 在 episode 1 上开发嵌套 OOF 纠错器；
3. 纠错器只能读取普通图像特征与 fold-training 统计，不能读取外层
   evaluation 标签、关键点或 test；
4. 候选输入限制为：
   - RBF top-1/top-2 margin；
   - 近邻标签一致性与局部纯度；
   - RBF 与 cosine prototype 的预测分歧；
   - fold-training 内混淆类别对的历史纠错可靠性；
5. 只有在内层 OOF 显示某类纠错动作具有正期望收益时才允许修改预测；
   其他样本必须保留 RBF 结果；
6. episode 1 开发门固定为：
   - 相对标准 RBF 86.20% 至少 `+0.50pp`；
   - 类别负迁移率不高于 RBF；
   - 最差类别伤害必须单独报告；
7. 通过开发门后才生成全新 train-only episode 4/5；
8. episode 4/5 使用完全冻结的特征、阈值和纠错逻辑，不允许继续调参；
9. episode 4/5 均通过后，再进入 CCT20+ 第二数据集；
10. 第二数据集也通过后，才讨论正式 test 锁文件。

建议实验编号：

- 文献与协议阶段：`PAT-LIT-260729-011`
- episode 1 选择性纠错开发：`PAT-H-260729-011`
- 新 episode 4/5 冻结确认：`PAT-H-260729-012`

这一方向优于继续做全局 PEFT 的原因：

- 强 RBF 已经能够正确处理大多数样本；
- LoRA 与残差适配器均显示少样本过拟合；
- 当前误差更适合“少改且安全地改”，而不是重新学习全部表征；
- 类别安全门与原 proposal 的“控制类别级负迁移”目标仍然一致。

### DINOv2-L 的定位

DINOv2-L/14 冻结 CLS + RBF 可以在核心机制确定后作为 backbone ablation，
用于测量性能上限，但不能作为下一篇论文的创新点。若执行，要求：

- 输入、episode、图像尺寸和 RBF 参数与 ViT-B 完全一致；
- 相对 ViT-B `SVC.predict = 86.20%` 至少提高 1.0pp 才值得扩展；
- 结果只能报告为更强 backbone 基线；
- 不得用它替代选择性纠错机制的跨 episode、跨数据集验证。

### 论文层面的选择

PAT-H-260729-011 已在 episode 1 开发门失败，因此当前方法搜索已经停止，
不再堆叠融合、LoRA 或更大模型。后续应在以下两条路线中明确选择：

1. 回到“稀疏关键点主动选择”，重新设计真正能利用关键点的训练目标；
2. 改成“冻结基础模型下的少样本细粒度分类几何与类别安全”论文，并补充
   一个独立、可复现且跨数据集有效的机制。

目前证据不足以声称完整方法已经成功，也不足以解锁双数据最终 test。

## 8. 服务器交接

### 连接信息

```bash
ssh -p 23 root@117.50.226.147
```

- 密码未写入本文件，请向用户重新索取；
- GPU：NVIDIA GeForce RTX 3080 Ti 12GB；
- 上次检查：GPU 空闲，显存 1 MiB；
- Python 环境：

```bash
source /usr/local/miniconda3/bin/activate py312
```

### 服务器路径

```text
/root/workspace/8-pat
/root/workspace/datasets/cub_200_2011
/root/workspace/8-pat/experiments/dinov2_sparse_anchor
/root/workspace/8-pat/runs/PAT-H-260729-001/features
/root/workspace/8-pat/runs/PAT-H-260729-005/features
/root/workspace/8-pat/runs/PAT-H-260729-010
/root/workspace/8-pat/experiments/dinov2_capacity_kernel
/root/workspace/8-pat/runs/PAT-K-260729-002/formal
/root/workspace/8-pat/runs/PAT-K-260729-003/features
/root/workspace/8-pat/runs/PAT-K-260729-003/formal
/root/workspace/8-pat/runs/PAT-K-260729-004/formal
/root/workspace/8-pat/runs/PAT-K-260729-005/formal
/root/workspace/8-pat/runs/PAT-K-260729-006
/root/workspace/datasets/stanford_dogs
```

重要缓存：

- PAT-H-001 episode 1 DINOv2-B CLS/mean-patch/dense patch；
- PAT-H-005 episode 2/3 DINOv2-B CLS；
- PAT-H-006 episode 1 四视图 CLS；
- PAT-H-010 五折 LoRA/head 状态、完整预测和日志。

不要删除服务器缓存，除非用户明确要求。

## 9. 本地归档

### PAT-H-001～009

```text
/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_DINOv2Geometry_PAT-H-260729-Series/
```

便携归档：

```text
PAT-H-260729-series-artifacts.tar.gz
SHA256:
e4193206ca4a3034318ef42546d69235db642508c6ff9e68c057d00f9e65dbde
```

### PAT-H-010

```text
/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_LastBlockLoRA_PAT-H-260729-010/
```

便携归档：

```text
PAT-H-260729-010-artifacts.tar.gz
SHA256:
8344c08d6e0f4fca5d0c200286a7122830ef1fbe8476bd37410a91042ccd26e0
```

### PAT-H-011

```text
/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_ClassSafeCorrection_PAT-H-260729-011/
```

便携归档：

```text
PAT-H-260729-011-artifacts.tar.gz
SHA256:
f761119bf7674f4ed689c952c0d8d68acdad0b1ca10b45ccb32bc967d6049796
```

### PAT-I-001

```text
/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_DINOSemanticPartQuery_PAT-I-260729-001/
```

便携归档：

```text
PAT-I-260729-001-artifacts.tar.gz
SHA256:
f6833df4370ee605c1e7d41c0010d5190d1810928d633978f08341fdf8f95ce5
```

归档已在本地执行 `sha256sum -c`，代码、协议、预测、日志和模型状态均通过。

### PAT-K-001～003

```text
/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_OneShotRegime_PAT-K-260729-001/
/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_DCCR_PAT-K-260729-002/
/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_DCTPRConfirmation_PAT-K-260729-003/
```

各目录包含本地 `SHA256SUMS`。DINOv2-L Episode 2/3 的完整 CLS 数组保留在
服务器，结果报告记录其哈希；本地保存 metadata 和 extraction log。

### PAT-K-004～006

```text
/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_PublishedBaselines_PAT-K-260729-004/
/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_CUB_QueryPriorStress_PAT-K-260729-005/
/Users/mac/Documents/6-Research/8-pat/raw/experiments/2026.07.29_StanfordDogs_DCTPR_PAT-K-260729-006/
```

截至 PAT-K-006，本地包含三集完整 B/L CLS 特征、清单、预测和日志。独立审计从
NPZ 重算 1,219,200 个预测值并验证 3,600 张 Dogs train 图像互不重叠、B/L
元数据对齐和 official-test 访问为 0。

完整论文证据包：

```text
packages/PAT-K-260729-complete-paper-evidence.tar.gz
SHA256: see companion `PAT-K-260729-complete-paper-evidence.tar.gz.sha256`
```

## 10. 实验纪律

后续 agent 必须遵守：

1. 新方法运行前先写冻结 protocol；
2. smoke 后再跑 formal；
3. 所有比较使用标准 `SVC.predict`，不要混用
   `decision_function.argmax`；
4. 任何开发集 winner 都必须在未用于调参的新 episode 上确认；
5. 不因结果接近门槛而事后放宽门槛；
6. 不把失败臂改名后重新包装；
7. 官方 test 只允许使用已封存的 PAT-K-260805-009 锁定结果；禁止继续访问、
   反向调参或另选测试清单；
8. 每阶段保存完整预测、模型配置、运行日志、环境和 SHA256；
9. 报告类别级正/负迁移和最差类别，而不只报告总体 BA；
10. EI 会议目标允许方法简单，但不允许创新性与实验结论表述失真。

## 11. 给新 Agent 的一句话摘要

> DCTPR 已完成 CUB-200 与 Stanford Dogs 共六个 train-only episodes、公开强
> 基线和 query-prior stress。DCTPR 相对 BL nearest support 提高 +6.68pp/
> +6.27pp；相对各数据集最强 TIM/MAP 低 1.35pp/0.61pp，但快约 3.8x/49x。
> Dogs 30/30 轮换正向并通过 paper-level empirical route gate。不均衡 query
> 会使 uniform-prior DCTPR 退回约 68--69%，必须作为 limitation。方法搜索已
> 停止方法搜索。2026-08-05 锁定 official-test 审计保持同一结论：CUB/Dogs
> DCTPR 为 74.64%/70.49%，相对 BL-NCC 提升 +6.69pp/+6.92pp，距最强
> matched solver 1.53pp/0.99pp。下一步只做投稿信息、引用与版式收尾，禁止
> 从测试结果反向修改方法。
