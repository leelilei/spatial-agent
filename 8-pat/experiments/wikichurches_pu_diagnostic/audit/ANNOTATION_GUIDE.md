# WikiChurches 局部构件盲审指南

## 任务

在不查看官方原始框的前提下，尽可能完整地标出图中清晰可见、可命名的建筑构件。目标是测量官方“characteristic visual features”框的覆盖程度，不是判断官方标注对错。

## 两阶段

1. 先独立完成 `WC-AUD-001` 至 `WC-AUD-008`；
2. 讨论标签粒度、边界和不确定项，冻结规则；
3. 两位标注者重新独立完成全部 50 图；
4. 完成后才解封官方框并做匹配。

## HTML 标注器

打开 `audit/blinded/index.html` 即可直接画框：

- 第一个 `WC-DEMO-001` 是正式样本之外的练习图，预置了窗、窗饰、小构件
  和扶壁示例；它不进入进度、CSV 或评分；
- 在图片空白处拖拽新建框；
- 拖动现有框可移动，拖动右下角圆点可缩放；
- 在右侧搜索并选择标准构件英文名；词表没有合适名称时可直接填写新名称；
- 每张图检查完成后点击“标记本图完成”；
- 页面按 `annotator_id` 在当前浏览器本地自动保存；
- 全部完成后点击“导出 CSV”，结果字段与评分脚本兼容。

两位标注者应使用不同浏览器配置文件或不同电脑，并分别使用
`annotator_a`、`annotator_b`，避免看到对方的记录。浏览器数据不是正式
备份；每天结束时都应导出一次 CSV。

练习图来自 WikiChurches 样本外图像
`Q2559480_wd0.jpg`（Chester Cathedral, Cloisters Garth），作者 Yahra，
许可为 CC BY-SA 3.0。练习框仅用于说明工具操作、框边界与嵌套构件记录，
不作为穷尽式建筑标注答案。

## 一框一构件

- 对重复出现的同类构件分别画框；
- 如果多个元素组成一个整体，可同时标“元素框”和“组框”，并在 `parent_label` 中写组名；
- 框应尽量贴合可见结构，不包含大面积无关墙面；
- 只标图中可见证据，不依据建筑风格臆测不可见结构。

## 字段

- `feature_label`：最具体且有把握的英文构件名；
- `parent_label`：更上位的类型，可空；
- `left, top, width, height`：相对于图像宽高的 0–1 坐标；
- `certainty`：`certain` / `uncertain` / `reject`；
- `visibility`：`clear` / `partial` / `tiny`；
- `occlusion`：`none` / `partial` / `heavy`；
- `notes`：边界、层级或遮挡说明。

## 禁止

- 不查看 `audit/sealed/`；
- 不自行查看 `building_parts.json`；只使用 HTML 中已冻结的标准名称词表；
- 不用已有框作为搜索提示；
- 不把纯纹理、阴影、树木或透视线误标为建筑构件。
