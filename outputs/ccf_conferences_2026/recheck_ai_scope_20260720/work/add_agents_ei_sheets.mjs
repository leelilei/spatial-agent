import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const inputPath = "/Users/mac/Documents/6-Research/outputs/ccf_conferences_2026/rechecked_ai_cv_2026-07-20/CCF会议投稿时间表_2026年8-11月_AI-CV控制补充复核版.xlsx";
const outputDir = "/Users/mac/Documents/6-Research/outputs/ccf_conferences_2026/rechecked_agents_ei_2026-07-20";
const outputPath = `${outputDir}/CCF与EI会议投稿时间表_2026年8-11月_智能体-AI-CV补充版.xlsx`;
const d = (iso) => iso ? new Date(`${iso}T00:00:00Z`) : null;

await fs.mkdir(`${outputDir}/previews`, { recursive: true });
const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(inputPath));

// Required visual baseline before changing the workbook.
for (let i = 0; i < workbook.worksheets.items.length; i++) {
  const ws = workbook.worksheets.getItemAt(i);
  const before = await workbook.render({ sheetName: ws.name, autoCrop: "all", scale: 1.2, format: "png" });
  await fs.writeFile(`${outputDir}/previews/00_before_${ws.name}.png`, new Uint8Array(await before.arrayBuffer()));
}

const navy = "#1F4E78";
const blue = "#D9EAF7";
const pale = "#EAF2F8";
const green = "#E2F0D9";
const yellow = "#FFF2CC";
const red = "#FCE4D6";
const gray = "#E7E6E6";
const border = "#B4C6E7";

function styleSheet(sheet, titleRange, subtitleRange, headerRange, bodyRange, dateRange, widths) {
  sheet.showGridLines = false;
  sheet.mergeCells(titleRange);
  sheet.mergeCells(subtitleRange);
  sheet.getRange(titleRange).format = {
    fill: navy,
    font: { color: "#FFFFFF", bold: true, size: 16 },
    horizontalAlignment: "center",
    verticalAlignment: "center",
    rowHeight: 30,
  };
  sheet.getRange(subtitleRange).format = {
    fill: pale,
    font: { color: navy, italic: true, size: 10 },
    horizontalAlignment: "left",
    verticalAlignment: "center",
    wrapText: true,
    rowHeight: 32,
  };
  sheet.getRange(headerRange).format = {
    fill: navy,
    font: { color: "#FFFFFF", bold: true },
    horizontalAlignment: "center",
    verticalAlignment: "center",
    wrapText: true,
    borders: { preset: "all", style: "thin", color: border },
    rowHeight: 32,
  };
  sheet.getRange(bodyRange).format = {
    verticalAlignment: "center",
    wrapText: true,
    borders: { preset: "all", style: "thin", color: "#D9E2F3" },
    rowHeight: 46,
  };
  sheet.getRange(dateRange).format.numberFormat = "yyyy-mm-dd";
  for (const [col, px] of Object.entries(widths)) sheet.getRange(`${col}:${col}`).format.columnWidthPx = px;
  sheet.freezePanes.freezeRows(5);
}

// Sheet 1: venues close to AAMAS, including closed high-relevance venues as watchlist items.
const agents = workbook.worksheets.add("智能体会议");
agents.getRange("A1:K1").values = [["AAMAS 类多智能体 / Agentic AI 会议补充", null, null, null, null, null, null, null, null, null, null]];
agents.getRange("A2:K2").values = [["核验日期：2026-07-20｜主筛选窗口：全文截止 2026-08-01 至 2026-11-30；已关闭会议仅作为下一届关注名单。", null, null, null, null, null, null, null, null, null, null]];
agents.getRange("A5:K5").values = [["会议", "CCF", "相关方向", "摘要截止", "全文截止", "通知日期", "会议日期", "当前状态", "出版/EI 表述", "官网", "核验备注"]];
const agentRows = [
  ["AAMAS 2027", "B", "自主智能体、多智能体系统", d("2026-10-02"), d("2026-10-09"), null, "2027（日期待官网更新）", "窗口内，可准备", "顶级多智能体会议；本表不另作 EI 结论", "https://openreview.net/group?id=ifaamas.org/AAMAS/2027/Conference", "主清单已有；截至核验日官方仅明确摘要/全文截止"],
  ["DAI 2026", "C", "分布式 AI、多智能体、Agentic AI", d("2026-07-27"), d("2026-08-03"), null, "2026-11-29—12-02", "窗口内，近期截止", "正式论文集；不将其 EI 状态作额外保证", "https://www.adai.ai/dai/2026/", "Research/Industry 全文 8-03；AI Paper Track 全文 8-10、通知 9-16；各轨日期不同"],
  ["PRIMA 2026", "非CCF", "MAS 基础、协作协调、Agentic AI", d("2026-08-03"), d("2026-08-03"), d("2026-09-25"), "2026-12-14—12-17", "窗口内，延期截止", "多智能体专业会议；非 CCF", "https://www.prima2026.org/", "延期后的摘要和全文截止均为 8-03 AoE；与 AAMAS 主题最接近的补充之一"],
  ["ICAART 2027", "非CCF", "Agents、MAS、LLM Agent、认知机器人", null, d("2026-09-15"), d("2026-11-13"), "2027-02-23—02-25", "窗口内；另有 10-22 轮次", "官网称论文集提交 EI 等数据库评估", "https://icaart.scitevents.org/CallforPapers.aspx?y=2027", "Regular 9-15；Position/Regular 10-22；提交评估不等于保证收录"],
  ["EUMAS 2026", "非CCF", "欧洲多智能体系统", null, d("2026-05-18"), d("2026-06-30"), "2026-09-21—09-25", "已关闭，仅关注下一届", "Springer LNCS", "https://euramas.github.io/eumas2026/", "专业度高，但不符合本轮 8–11 月投稿窗口"],
  ["IEEE/WIC WI-IAT 2026", "C", "Web Intelligence、智能体技术", null, d("2026-07-15"), d("2026-08-31"), "2026-12-03—12-06", "已关闭，仅关注下一届", "录用论文提交 IEEE Xplore，须满足其范围与质量要求", "https://www.wi-iat.org/wi-iat2026/index.html", "与智能体相关且为 CCF C，但主会全文截止早于本轮窗口"],
];
agents.getRange(`A6:K${5 + agentRows.length}`).values = agentRows;
styleSheet(agents, "A1:K1", "A2:K2", "A5:K5", `A6:K${5 + agentRows.length}`, `D6:F${5 + agentRows.length}`, {
  A: 150, B: 70, C: 210, D: 100, E: 100, F: 100, G: 145, H: 150, I: 235, J: 285, K: 290,
});
agents.tables.add(`A5:K${5 + agentRows.length}`, true, "AgentVenues2026").style = "TableStyleMedium2";
agents.getRange("H6:H9").format.fill = green;
agents.getRange("H10:H11").format.fill = gray;
agents.getRange("I9:I9").format.fill = yellow;
agents.getRange("K9:K9").format.fill = yellow;

// Sheet 2: EI candidates. Wording is deliberately separated into confirmed-history vs submission-for-review.
const ei = workbook.worksheets.add("EI候选");
ei.getRange("A1:L1").values = [["AI / 计算机视觉 / 智能体方向 EI 候选", null, null, null, null, null, null, null, null, null, null, null]];
ei.getRange("A2:L2").values = [["核验日期：2026-07-20｜“提交 EI 评估”不代表最终收录；投稿前须再次核查当届出版社、会议记录和最终卷。", null, null, null, null, null, null, null, null, null, null, null]];
ei.getRange("A5:L5").values = [["会议", "方向", "CCF", "第一截止", "后续截止", "通知日期", "会议日期", "出版方/载体", "EI 状态", "核验强度", "官网", "备注"]];
const eiRows = [
  ["ICAART 2027", "智能体 / 多智能体 / AI", "非CCF", d("2026-09-15"), d("2026-10-22"), d("2026-11-13"), "2027-02-23—02-25", "SCITEPRESS Proceedings", "官网称提交 EI 评估", "中", "https://icaart.scitevents.org/CallforPapers.aspx?y=2027", "第二轮通知 12-04；EI 非保证"],
  ["VISAPP 2027", "计算机视觉 / 表征 / 3D / 机器人", "非CCF", d("2026-09-15"), d("2026-10-22"), d("2026-11-13"), "2027-02-26—02-28", "SCITEPRESS Proceedings", "官网称提交 EI 评估", "中", "https://visapp.scitevents.org/CallForPapers.aspx", "第二轮通知 12-04；EI 非保证"],
  ["ICPRAM 2027", "模式识别 / 机器学习 / 图像视频", "非CCF", d("2026-09-15"), d("2026-10-22"), d("2026-11-13"), "2027-02-20—02-22", "SCITEPRESS Proceedings", "官网称提交 EI 评估", "中", "https://icpram.scitevents.org/CallForPapers.aspx?y=2027", "第二轮通知 12-04；EI 非保证"],
  ["ROBOVIS 2027", "机器人 / 计算机视觉 / 智能系统", "非CCF", d("2026-09-15"), d("2026-10-22"), d("2026-11-13"), "2027-02-27—02-28", "Springer CCIS", "官网称论文集由 EI-Compendex 收录", "较高", "https://robovis.scitevents.org/CallforPapers.aspx", "第二轮通知 12-04；仍以最终卷检索为准"],
  ["ICARA 2027", "自动化 / 机器人 / 智能系统", "非CCF", d("2026-10-01"), null, d("2026-11-01"), "2027-02-25—02-27", "Conference Proceedings；往届入 IEEE Xplore", "官网列示 2021–2026 往届 EI 记录", "较高", "https://www.icara.us/", "当届最终 EI 状态仍需以数据库实际检索为准"],
  ["ICDIP 2027", "数字图像处理 / 计算机视觉", "非CCF", d("2026-11-10"), null, d("2026-12-10"), "2027-04-16—04-18", "SPIE Conference Proceedings", "官网声明论文集由 EI Compendex 等检索", "较高", "https://www.icdip.org/", "官网另出现后续延长期信息；本表保留首轮 11-10"],
  ["ICCAI 2027", "计算与人工智能", "非CCF", d("2026-11-10"), null, d("2026-11-30"), "2027-04-23—04-26", "International Conference Proceedings", "官网声明 EI Compendex / Scopus", "中", "https://www.iccai.net/", "投稿前复核当届出版社与最终 proceedings 信息"],
  ["ISoIRS 2027", "智能机器人系统 / 具身智能", "非CCF", d("2026-11-19"), null, d("2027-01-14"), "2027（日期待官网更新）", "Digital Conference Proceedings；往届 IEEE", "当届提交 EI 评估；2025–2026 官网称已 EI", "中", "https://www.isoirs.org/", "摘要 11-04；当届 EI 非保证"],
];
ei.getRange(`A6:L${5 + eiRows.length}`).values = eiRows;
styleSheet(ei, "A1:L1", "A2:L2", "A5:L5", `A6:L${5 + eiRows.length}`, `D6:F${5 + eiRows.length}`, {
  A: 145, B: 205, C: 72, D: 100, E: 100, F: 100, G: 145, H: 205, I: 240, J: 75, K: 285, L: 265,
});
ei.tables.add(`A5:L${5 + eiRows.length}`, true, "EICandidates2026").style = "TableStyleMedium2";
ei.getRange("I6:I8").format.fill = yellow;
ei.getRange("I9:I12").format.fill = green;
ei.getRange("I13:I13").format.fill = yellow;
ei.getRange("J6:J13").format.horizontalAlignment = "center";
ei.getRange("L6:L13").format.fill = "#FFFDF2";

for (const name of ["智能体会议", "EI候选"]) {
  console.log(`CHECK_${name}\n` + (await workbook.inspect({
    kind: "table",
    range: `${name}!A1:L20`,
    include: "values,formulas",
    tableMaxRows: 25,
    tableMaxCols: 14,
    tableMaxCellChars: 260,
    maxChars: 24000,
  })).ndjson);
}

const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 300 },
  summary: "final formula error scan",
});
console.log("ERRORS\n" + errors.ndjson);

for (let i = 0; i < workbook.worksheets.items.length; i++) {
  const ws = workbook.worksheets.getItemAt(i);
  const preview = await workbook.render({ sheetName: ws.name, autoCrop: "all", scale: 1.25, format: "png" });
  await fs.writeFile(`${outputDir}/previews/${String(i + 1).padStart(2, "0")}_${ws.name}.png`, new Uint8Array(await preview.arrayBuffer()));
}

const exported = await SpreadsheetFile.exportXlsx(workbook);
await exported.save(outputPath);
console.log(`OUTPUT ${outputPath}`);
