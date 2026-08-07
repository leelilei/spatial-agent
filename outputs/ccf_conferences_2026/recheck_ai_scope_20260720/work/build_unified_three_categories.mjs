import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const sourcePath = "/Users/mac/Documents/6-Research/outputs/ccf_conferences_2026/rechecked_agents_ei_2026-07-20/CCF与EI会议投稿时间表_2026年8-11月_智能体-AI-CV补充版.xlsx";
const outputDir = "/Users/mac/Documents/6-Research/outputs/ccf_conferences_2026/rechecked_unified_2026-07-20";
const outputPath = `${outputDir}/AI-CV-智能体会议汇总_2026年8-11月.xlsx`;
const d = (iso) => iso ? new Date(`${iso}T00:00:00Z`) : null;

await fs.mkdir(`${outputDir}/previews`, { recursive: true });

// Baseline render of the supplied/recent workbook before restructuring.
const source = await SpreadsheetFile.importXlsx(await FileBlob.load(sourcePath));
for (let i = 0; i < source.worksheets.items.length; i++) {
  const ws = source.worksheets.getItemAt(i);
  const png = await source.render({ sheetName: ws.name, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(`${outputDir}/previews/00_before_${String(i + 1).padStart(2, "0")}_${ws.name}.png`, new Uint8Array(await png.arrayBuffer()));
}

const workbook = Workbook.create();
const sheet = workbook.worksheets.add("三类会议汇总");
sheet.showGridLines = false;

const rows = [
  ["人工智能大类", "ICRA 2027", "CCF B", "人工智能、机器人、控制", null, d("2026-09-15"), null, d("2027-01-31"), "2027（会议日期待官网更新）", "窗口内，可投", "CCF会议；不以 EI 为本表判断依据", "https://2027.ieee-icra.org/contribute/call-for-icra-2027-papers-now-accepting-submissions/", "原主清单已收录；技术论文"],
  ["人工智能大类", "ICARA 2027", "EI候选·较高", "自动化、机器人、智能系统", null, d("2026-10-01"), null, d("2026-11-01"), "2027-02-25—02-27", "窗口内，可投", "官网列示 2021–2026 往届 EI / IEEE Xplore 记录", "https://www.icara.us/", "当届仍以最终数据库检索为准"],
  ["人工智能大类", "ICCAI 2027", "EI候选·中", "计算与人工智能", null, d("2026-11-10"), null, d("2026-11-30"), "2027-04-23—04-26", "窗口内，可投", "官网声明 EI Compendex / Scopus", "https://www.iccai.net/", "投稿前复核当届出版社与 proceedings 信息"],
  ["人工智能大类", "ISoIRS 2027", "EI候选·中", "智能机器人、具身智能", d("2026-11-04"), d("2026-11-19"), null, d("2027-01-14"), "2027（会议日期待官网更新）", "窗口内，可投", "当届提交 EI 评估；官网称 2025–2026 已 EI", "https://www.isoirs.org/", "提交评估不等于保证收录"],

  ["计算机视觉 / 模式识别", "3DV 2027", "CCF C", "三维视觉、重建、3D 学习", null, d("2026-08-28"), null, d("2026-12-02"), "2027（会议日期见官网）", "窗口内，可投", "CCF会议；不以 EI 为本表判断依据", "https://3dvconf.github.io/2027/", "补充材料 9-02；初步通知 10-27"],
  ["计算机视觉 / 模式识别", "DCC 2027", "CCF B", "图像/视频压缩、视觉编码", null, d("2026-10-02"), null, d("2026-11-22"), "2027（会议日期见官网）", "窗口内，可投", "CCF会议；不以 EI 为本表判断依据", "https://datacompressionconference.org/important-dates/", "范围含视觉搜索和深度学习压缩"],
  ["计算机视觉 / 模式识别", "FG 2027", "CCF C", "人脸与手势、模式识别、生物特征", d("2026-10-09"), d("2026-10-16"), null, d("2026-12-20"), "2027（会议日期见官网）", "窗口内，可投", "CCF会议；不以 EI 为本表判断依据", "https://fg2027.ieee-biometrics.org/dates/", "摘要和全文日期均为 AoE"],
  ["计算机视觉 / 模式识别", "VISAPP 2027", "EI候选·中", "计算机视觉、表征、3D、机器人", null, d("2026-09-15"), d("2026-10-22"), d("2026-11-13"), "2027-02-26—02-28", "窗口内，可投", "官网称论文集提交 EI 评估", "https://visapp.scitevents.org/CallForPapers.aspx", "第二轮通知 12-04；EI 非保证"],
  ["计算机视觉 / 模式识别", "ICPRAM 2027", "EI候选·中", "模式识别、机器学习、图像视频", null, d("2026-09-15"), d("2026-10-22"), d("2026-11-13"), "2027-02-20—02-22", "窗口内，可投", "官网称论文集提交 EI 评估", "https://icpram.scitevents.org/CallForPapers.aspx?y=2027", "第二轮通知 12-04；EI 非保证"],
  ["计算机视觉 / 模式识别", "ROBOVIS 2027", "EI候选·较高", "机器人视觉、智能系统", null, d("2026-09-15"), d("2026-10-22"), d("2026-11-13"), "2027-02-27—02-28", "窗口内，可投", "Springer CCIS；官网称论文集由 EI-Compendex 收录", "https://robovis.scitevents.org/CallforPapers.aspx", "第二轮通知 12-04；以最终卷检索为准"],
  ["计算机视觉 / 模式识别", "ICDIP 2027", "EI候选·较高", "数字图像处理、计算机视觉", null, d("2026-11-10"), null, d("2026-12-10"), "2027-04-16—04-18", "窗口内，可投", "SPIE Proceedings；官网声明 EI Compendex 等检索", "https://www.icdip.org/", "本表保留官网首轮 11-10"],

  ["智能体 / 多智能体", "AAMAS 2027", "CCF B", "自主智能体、多智能体系统", d("2026-10-02"), d("2026-10-09"), null, null, "2027（会议日期待官网更新）", "窗口内，可投", "多智能体旗舰会议；不另作 EI 结论", "https://openreview.net/group?id=ifaamas.org/AAMAS/2027/Conference", "截至 7-20，官方仅明确摘要/全文截止"],
  ["智能体 / 多智能体", "DAI 2026", "CCF C", "分布式 AI、多智能体、Agentic AI", d("2026-07-27"), d("2026-08-03"), d("2026-08-10"), d("2026-09-16"), "2026-11-29—12-02", "窗口内，近期截止", "正式论文集；不另作 EI 保证", "https://www.adai.ai/dai/2026/", "Research/Industry 8-03；AI Paper Track 8-10、通知 9-16"],
  ["智能体 / 多智能体", "PRIMA 2026", "非CCF专业", "MAS 基础、协作协调、Agentic AI", d("2026-08-03"), d("2026-08-03"), null, d("2026-09-25"), "2026-12-14—12-17", "窗口内，延期截止", "多智能体专业会议；非 CCF", "https://www.prima2026.org/", "延期摘要/全文截止均为 8-03 AoE"],
  ["智能体 / 多智能体", "ICAART 2027", "EI候选·中", "Agents、MAS、LLM Agent、认知机器人", null, d("2026-09-15"), d("2026-10-22"), d("2026-11-13"), "2027-02-23—02-25", "窗口内，可投", "SCITEPRESS；官网称论文集提交 EI 评估", "https://icaart.scitevents.org/CallforPapers.aspx?y=2027", "第二轮通知 12-04；EI 非保证"],
  ["智能体 / 多智能体", "EUMAS 2026", "非CCF专业", "欧洲多智能体系统", null, d("2026-05-18"), null, d("2026-06-30"), "2026-09-21—09-25", "已关闭，仅关注下一届", "Springer LNCS", "https://euramas.github.io/eumas2026/", "专业度高，但不符合本轮投稿窗口"],
  ["智能体 / 多智能体", "IEEE/WIC WI-IAT 2026", "CCF C", "Web Intelligence、智能体技术", null, d("2026-07-15"), null, d("2026-08-31"), "2026-12-03—12-06", "已关闭，仅关注下一届", "录用论文提交 IEEE Xplore，须满足其要求", "https://www.wi-iat.org/wi-iat2026/index.html", "主会全文截止早于本轮窗口"],
];

sheet.mergeCells("A1:M1");
sheet.getRange("A1:M1").values = [["人工智能 · 计算机视觉 · 智能体会议统一汇总"]];
sheet.mergeCells("A2:M2");
sheet.getRange("A2:M2").values = [["核验日期：2026-07-20｜全文截止主窗口：2026-08-01 至 2026-11-30｜CCF B/C 与 EI 候选统一列示；EI“提交评估”不代表最终收录。"]];
sheet.mergeCells("A3:M3");
sheet.getRange("A3:M3").values = [["排序规则：人工智能大类 → 计算机视觉/模式识别 → 智能体/多智能体；交叉会议按主方向归类，细节见“细分方向”。"]];
const headers = [["大类", "会议", "级别 / 类型", "细分方向", "摘要截止", "全文截止", "后续截止", "通知日期", "会议日期", "当前状态", "EI / 出版状态", "官网", "核验备注"]];
sheet.getRange("A5:M5").values = headers;
sheet.getRange(`A6:M${5 + rows.length}`).values = rows;

const navy = "#1F4E78";
const lightBlue = "#D9EAF7";
const border = "#B4C6E7";
sheet.getRange("A1:M1").format = { fill: navy, font: { color: "#FFFFFF", bold: true, size: 16 }, horizontalAlignment: "center", verticalAlignment: "center", rowHeight: 32 };
sheet.getRange("A2:M2").format = { fill: "#EAF2F8", font: { color: navy, italic: true, size: 10 }, wrapText: true, verticalAlignment: "center", rowHeight: 28 };
sheet.getRange("A3:M3").format = { fill: "#F7F9FB", font: { color: "#44546A", size: 10 }, wrapText: true, verticalAlignment: "center", rowHeight: 26 };
sheet.getRange("A5:M5").format = { fill: navy, font: { color: "#FFFFFF", bold: true }, horizontalAlignment: "center", verticalAlignment: "center", wrapText: true, rowHeight: 34, borders: { preset: "all", style: "thin", color: border } };
sheet.getRange(`A6:M${5 + rows.length}`).format = { verticalAlignment: "center", wrapText: true, rowHeight: 48, borders: { preset: "all", style: "thin", color: "#D9E2F3" } };
sheet.getRange(`E6:H${5 + rows.length}`).format.numberFormat = "yyyy-mm-dd";

const table = sheet.tables.add(`A5:M${5 + rows.length}`, true, "UnifiedConferenceList2026");
table.style = "TableStyleMedium2";

// Category blocks: contiguous and color-coded within one filterable table.
sheet.getRange("A6:A9").format.fill = "#DDEBF7";
sheet.getRange("A10:A16").format.fill = "#E2F0D9";
sheet.getRange("A17:A22").format.fill = "#E4DFEC";
sheet.getRange("A6:A22").format.font = { bold: true, color: "#203864" };
for (const r of [6, 10, 17]) sheet.getRange(`A${r}:M${r}`).format.borders = { top: { style: "medium", color: navy } };

// Semantic status colors.
for (const r of [6, 10, 11, 12, 17, 18, 22]) sheet.getRange(`C${r}`).format.fill = lightBlue;
for (const r of [7, 15, 16]) sheet.getRange(`C${r}`).format.fill = "#E2F0D9";
for (const r of [8, 9, 13, 14, 20]) sheet.getRange(`C${r}`).format.fill = "#FFF2CC";
for (const r of [19, 21]) sheet.getRange(`C${r}`).format.fill = "#E7E6E6";
sheet.getRange("J6:J20").format.fill = "#E2F0D9";
sheet.getRange("J21:J22").format.fill = "#E7E6E6";
for (const r of [8, 9, 13, 14, 20]) sheet.getRange(`K${r}`).format.fill = "#FFF2CC";
for (const r of [7, 15, 16]) sheet.getRange(`K${r}`).format.fill = "#E2F0D9";

const widths = { A: 170, B: 150, C: 110, D: 225, E: 98, F: 98, G: 98, H: 98, I: 160, J: 150, K: 285, L: 300, M: 300 };
for (const [col, px] of Object.entries(widths)) sheet.getRange(`${col}:${col}`).format.columnWidthPx = px;
sheet.freezePanes.freezeRows(5);
sheet.freezePanes.freezeColumns(2);

const check = await workbook.inspect({
  kind: "table",
  range: `三类会议汇总!A1:M${5 + rows.length}`,
  include: "values,formulas",
  tableMaxRows: 30,
  tableMaxCols: 15,
  tableMaxCellChars: 240,
  maxChars: 30000,
});
console.log("CHECK\n" + check.ndjson);

const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 300 },
  summary: "final formula error scan",
});
console.log("ERRORS\n" + errors.ndjson);

const preview = await workbook.render({ sheetName: "三类会议汇总", autoCrop: "all", scale: 1.25, format: "png" });
await fs.writeFile(`${outputDir}/previews/01_三类会议汇总.png`, new Uint8Array(await preview.arrayBuffer()));

const exported = await SpreadsheetFile.exportXlsx(workbook);
await exported.save(outputPath);
console.log(`OUTPUT ${outputPath}`);
