# TOGA × WikiChurches：与当前 proposal 的首轮对照

日期：2026-07-27

## 先说结论

TOGA 可以作为“训练期图教师 + 轻量 Adapter”的母体，但它没有处理
WikiChurches 的构件框，也没有把框外区域建模为未标注集合。我们真正可能
新增的接口，只能位于 TOGA 的 **Patch 选择/聚合及其教师监督信号**，不能把
多尺度 Patch、异构图、MGT、Top-N 筛选或训练期蒸馏写成自己的创新。

WikiChurches 原论文明确说明：构件框由艺术史领域专家制作，专家被要求优先
选择“风格纯正、具有时代原型性”的教堂图像，并为框内结构写描述；论文没有
说明专家必须穷尽一张图中的每个同类构件。因此，“原框可能是代表性而非穷尽
式”是合理假设，但**尚不是已证事实**，仍需审计或作者确认。

当前无裁决实验已经排除了两条直接路线：nnPU/IPW 风险估计和保守正例扩展
都没有超过 Ignore。现阶段不能把 PU 模块接入 TOGA 并宣称有效；最有信息量
的下一项证据仍是盲审补全/Oracle，之后才决定是否进入端到端实验。

## 1. TOGA 实际做了什么

### 1.1 推理路径

TOGA 的学生是 Tip-Adapter-F 的可学习缓存。测试时只保留：

\[
L_{\mathrm{test}}(x)=L_{\mathrm{ZS}}(x)+\alpha L_{\mathrm{Cache}}(x)
\]

图教师在测试时完全移除。

### 1.2 训练期教师

教师使用 18 个多尺度视觉视图：

- 整图 1 个；
- 3×3 网格 9 个；
- 2×2 网格 4 个；
- 垂直两半 2 个；
- 水平两半 2 个。

这些视觉节点与类别文本节点先分别经过模态内 Transformer，再进入
Modality-aware Graph Transformer。图关系包括 patch↔patch 以及
patch/image↔text。

### 1.3 节点筛选

MGT 输出的视觉节点用一个可学习投影打分，然后保留 Top-N 节点再聚合。
论文消融中，保留 50% 节点通常优于全部聚合、25% 和 75%。这个筛选器只从
最终分类损失学习“判别性”，没有使用构件框、构件名称或区域真值。

### 1.4 训练目标

训练期三路 logits 为：

\[
L_{\mathrm{train}}
=L_{\mathrm{ZS}}+\alpha L_{\mathrm{Cache}}+\delta L_{\mathrm{Graph}}
\]

总损失为联合分类交叉熵加教师单独的 Focal Loss：

\[
\mathcal L_{\mathrm{Total}}
=\mathcal L_{\mathrm{CE}}(L_{\mathrm{train}},y)
+\lambda\mathcal L_{\mathrm{Focal}}(L_{\mathrm{Graph}},y)
\]

这不是一个显式的 feature-level KD loss；教师通过联合 logits 和共同反向传播
在线影响缓存学生。Proposal 中“将局部知识蒸馏到 Adapter”的表述需要按此
实现细化，不能笼统假定存在额外的 teacher-student feature matching。

### 1.5 原论文实验边界

- 11 个标准分类数据集；
- 1/2/4/8/16-shot；
- 主干为 frozen CLIP ViT-B/16；
- 每种 shot 独立运行 3 次并报告平均准确率；
- 主文使用 RTX PRO 6000 98 GB；
- 没有 WikiChurches；
- 没有区域标注不完整性实验；
- 没有人工构件框或构件名称监督；
- 没有 PN / Ignore / PU / Oracle 对照。

## 2. WikiChurches 原论文给出的关键事实

- 共 9,485 张教堂图像；
- 4 个主要风格上提供 631 个构件框，覆盖 139 张图像；
- 风格为 Romanesque、Gothic、Renaissance、Baroque；
- 平均每张已标图约 4.5 个框；
- 构件标签共 92 个左右并具有层级关系；
- 高频标签包括 Tracery、Round Arch Window、Pointed Arch Window、
  Buttress、Pinnacle、Lombard Band 和 Pilaster；
- 原论文的框是艺术史专家标注，风格标签则来自 Wikipedia 社区，二者可靠性
  来源不同；
- 原论文另做过 200 张图像级风格标签审计：86.1% 完全正确、4.0% 错误、
  2.5% 信息不足，其余为部分正确。

原文对构件标注的描述支持“选择性采样”的判断：专家先浏览同一风格的图像，
选择风格纯正且具有原型性的教堂，再在选中图像中画框并写结构描述。它并未
规定每个同类构件都必须画出。因此：

- 可以把框外区域视为“未知”，不应直接视为已确认负例；
- 不能仅凭论文文字给出 Missing Positive Rate；
- 盲审的目标不是复刻原始数据生产，而是估计原始框的召回率以及框外真阳性。

## 3. 对当前 proposal 的影响

| Proposal 组件 | 与论文关系 | 当前判断 |
|---|---|---|
| TOGA 图教师、MGT、多尺度 Patch | 母体已有 | 可复用，不是创新 |
| Top-N 判别节点筛选 | 母体已有 | 可作为干预接口 |
| 构件框内 Patch 为可靠正例 | WikiChurches 支持 | 需处理框与规则 Patch 的空间匹配 |
| 框外 Patch 为 P/U 混合集合 | 论文未直接证明 | 合理假设，需盲审/Oracle |
| nnPU / IPW | Proposal 候选 | 当前真实数据诊断为 No-Go |
| 高可信正例扩展 | Proposal 候选 | 当前多种子诊断为 No-Go |
| 区域监督校准 TOGA Patch 筛选 | 母体未做 | 只有 Oracle 显示端到端空间后才值得实现 |

## 4. 当前最重要的纠偏

1. TOGA 原始 Patch 是规则多尺度裁块，不是 ViT token，也不是专家构件框。
   构件框监督要先定义与 18 个裁块的 IoU/覆盖率映射；很多小构件可能无法被
   18 个粗粒度块准确表达。
2. WikiChurches 论文特别指出 pinnacle、quatrefoil 等关键结构很小，需要
   高分辨率处理。TOGA 把所有裁块缩放到 224×224，可能丢失小构件证据。
3. 因此即使 Oracle 明显优于 Ignore，也不能默认只改 Top-N 打分就够；可能
   还需引入 region proposal 或更细的 patch 粒度。那会改变方法边界与算力。
4. 当前实验评估的是冻结 CLIP 区域特征上的局部识别，不是完整 TOGA 分类。
   它能筛掉无效 PU 路线，但还不能证明 TOGA 端到端会提升或下降。

## 5. 推荐的决策顺序

1. 用当前 HTML 完成 50 张盲审，先获得新增框和不确定标记；
2. 计算 Original Annotation Recall、Missing Positive Rate、标注一致性；
3. 用新增框构造 Oracle，先在局部任务比较 PN / Ignore / Oracle；
4. 只有 Oracle 相对 Ignore 有稳定正增益，才实现 TOGA 中的区域校准接口；
5. 端到端最小矩阵先做 WikiChurches-4 的 1/4/16-shot × 3 seeds：
   Tip-Adapter-F、原 TOGA、TOGA+Ignore、TOGA+Oracle；
6. 若 TOGA+Oracle 仍无分类增益，就停止该方法方向，不再搜索 PU loss。

## 6. 下载文件

- `papers/TOGA_arXiv_2603.18101.pdf`
- `papers/WikiChurches_arXiv_2108.06959.pdf`

