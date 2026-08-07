# 8 图快速视觉复核

## 结论

快速配对复核已经观察到多处“官方框标出一个构件、同图中近似对称或重复的同类构件未标”的直接候选。研究前提不再只是由标注规模推测，值得继续双人盲审。

原始 JSON 还呈现出一个非常集中的选择模式：

- 139 张图中只有 6 张出现“同图同 leaf label”重复框；
- 631 个元素框中只有 6 个是同图同 leaf label 的第二个或后续实例；
- Pointed Arch Window、Buttress、Pilaster 等高频标签几乎都是每图最多一个。

这与建筑立面常见的重复窗、重复扶壁和成对壁柱形成明显张力，强烈提示标注者可能在选择代表性实例。由于标签粒度很细，这一统计仍需结合层级兼容匹配与人工复核解释。

该复核由非建筑专家在看到官方覆盖图后完成，因此：

- 只用于确认是否存在明显候选；
- 不进入 Missing Positive Rate；
- 不替代两名建筑背景标注者；
- 标签层级和边界仍须独立裁决。

## 明显候选

| 图像 | 官方已框 | 明显未框候选 | 当前判断 |
|---|---|---|---|
| WC-AUD-002 | 中央立面的 Gothic 窗、tracery、portal 等 | 两侧塔楼与中央立面存在多组重复尖拱窗/窗饰 | 高优先复核 |
| WC-AUD-004 | 右侧 Pilaster | 左侧镜像 Pilaster | 高置信候选 |
| WC-AUD-006 | 右侧 Round Arch Niche | 左侧镜像 Round Arch Niche | 高置信候选 |
| WC-AUD-007 | 右侧 Volute、局部 Balustrade | 立面另一侧的对称卷涡与栏杆结构 | 中高置信候选 |
| WC-AUD-008 | 单个 Pilaster | 正立面与侧立面的多处重复 Pilaster | 高优先复核 |

## 暂无明显重复候选

- WC-AUD-001：三个主要开口均已框，仍需高分辨率检查钟楼小开口；
- WC-AUD-003：当前只清楚看到一个 Coupled Twin Window；
- WC-AUD-005：当前框集中在中央 balustrade/volute，是否存在层级等价重复项需建筑专家判断。

## 当前证据强度

这 8 图支持的是：

> WikiChurches 框至少在部分图像上表现为代表性选择，而非对所有重复构件的显式穷尽。

它尚不支持：

> 全数据集漏标率是多少，或这些漏标一定会损害 few-shot 分类。

## Frozen-CLIP 候选排序

使用 OpenAI CLIP ViT-B/32 对 50 张图的框外滑窗进行同图同标签检索：

- 共输出 708 个 top-3 候选；
- 535/708 的分数不低于同图同标签官方框中位数；
- 加入 69 个审计标签的全局特异性约束后，185/708 同时满足正框阈值且标签 rank ≤ 5；
- 这些较强候选分布于 43/50 张图。

对最高特异性候选的快速查看能看到多处合理的重复 Onion Dome、Pinnacle、Buttress、Pilaster 和 Pointed Arch Window，但窗口较粗，也存在语义错配。因此该模型输出只作为盲审排序，不进入漏标率。

模型结果见 `model_assisted_triage/triage_report.md`。

对应图像：

- `pilot_contact_sheet_1.jpg`
- `pilot_contact_sheet_2.jpg`
