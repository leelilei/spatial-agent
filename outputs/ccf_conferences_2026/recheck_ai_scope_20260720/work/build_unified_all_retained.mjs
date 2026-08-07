import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const sourcePath = "/Users/mac/Documents/6-Research/outputs/ccf_conferences_2026/rechecked_agents_ei_2026-07-20/CCF与EI会议投稿时间表_2026年8-11月_智能体-AI-CV补充版.xlsx";
const currentPath = "/Users/mac/Documents/6-Research/outputs/ccf_conferences_2026/rechecked_expanded_multimedia_hci_2026-07-20/AI-CV-多媒体-HCI-智能体及其他会议完整汇总_2026年8-11月.xlsx";
const outputDir = "/Users/mac/Documents/6-Research/outputs/ccf_conferences_2026/rechecked_with_cities_2026-07-21";
const outputPath = `${outputDir}/AI-CV-多媒体-HCI-智能体及其他会议完整汇总_含举办城市.xlsx`;
const d = (iso) => iso ? new Date(`${iso}T00:00:00Z`) : null;
const fromExcelDate = (v) => {
  if (v instanceof Date) return v;
  if (typeof v === "number" && v > 30000) return new Date(Date.UTC(1899, 11, 30) + v * 86400000);
  return v ?? null;
};

await fs.mkdir(`${outputDir}/previews`, { recursive: true });
const current = await SpreadsheetFile.importXlsx(await FileBlob.load(currentPath));
const currentPreview = await current.render({ sheetName: "全部会议汇总", autoCrop: "all", scale: 0.9, format: "png" });
await fs.writeFile(`${outputDir}/previews/00_before_全部会议汇总.png`, new Uint8Array(await currentPreview.arrayBuffer()));
const source = await SpreadsheetFile.importXlsx(await FileBlob.load(sourcePath));

// Preserve a baseline of the supplied source as well.
for (let i = 0; i < source.worksheets.items.length; i++) {
  const ws = source.worksheets.getItemAt(i);
  const png = await source.render({ sheetName: ws.name, autoCrop: "all", scale: 0.9, format: "png" });
  await fs.writeFile(`${outputDir}/previews/00_before_${String(i + 1).padStart(2, "0")}_${ws.name}.png`, new Uint8Array(await png.arrayBuffer()));
}

const original = source.worksheets.getItem("会议清单").getRange("A7:I41").values;
if (original.length !== 35) throw new Error(`Expected 35 original CCF rows, found ${original.length}`);

const categoryFor = (name) => {
  if (["ICRA 2027"].includes(name)) return "人工智能大类";
  if (["3DV 2027", "DCC 2027", "FG 2027"].includes(name)) return "计算机视觉 / 模式识别";
  if (["ICASSP 2027", "MMAsia 2026", "MMM 2027"].includes(name)) return "多媒体 / 多媒体系统";
  if (["IUI 2027"].includes(name)) return "人机交互 / 智能交互";
  if (["AAMAS 2027", "DAI 2026"].includes(name)) return "智能体 / 多智能体";
  return "其他 CCF B/C";
};

const originalRows = original.map((r) => {
  const [name, rank, direction, abstract, full, result, round, url, note] = r;
  const category = categoryFor(name);
  return [
    category,
    name,
    `CCF ${rank}`,
    direction,
    fromExcelDate(abstract),
    fromExcelDate(full),
    null,
    fromExcelDate(result),
    name === "IUI 2027" ? "2027-02-08—02-11" : "见会议官网",
    name === "DAI 2026" ? "窗口内，近期截止" : (category === "其他 CCF B/C" ? "原清单完整保留" : "窗口内，可投"),
    "CCF会议；不以 EI 为本表判断依据",
    url,
    [round, note].filter(Boolean).join("；"),
  ];
});

const extras = [
  ["人工智能大类", "ICARA 2027", "EI候选·较高", "自动化、机器人、智能系统", null, d("2026-10-01"), null, d("2026-11-01"), "2027-02-25—02-27", "窗口内，可投", "官网列示 2021–2026 往届 EI / IEEE Xplore 记录", "https://www.icara.us/", "当届仍以最终数据库检索为准"],
  ["人工智能大类", "ICCAI 2027", "EI候选·中", "计算与人工智能", null, d("2026-11-10"), null, d("2026-11-30"), "2027-04-23—04-26", "窗口内，可投", "官网声明 EI Compendex / Scopus", "https://www.iccai.net/", "投稿前复核当届出版社与 proceedings 信息"],
  ["人工智能大类", "ISoIRS 2027", "EI候选·中", "智能机器人、具身智能", d("2026-11-04"), d("2026-11-19"), null, d("2027-01-14"), "2027（日期待官网更新）", "窗口内，可投", "当届提交 EI 评估；官网称 2025–2026 已 EI", "https://www.isoirs.org/", "提交评估不等于保证收录"],

  ["计算机视觉 / 模式识别", "VISAPP 2027", "EI候选·中", "计算机视觉、表征、3D、机器人", null, d("2026-09-15"), d("2026-10-22"), d("2026-11-13"), "2027-02-26—02-28", "窗口内，可投", "官网称论文集提交 EI 评估", "https://visapp.scitevents.org/CallForPapers.aspx", "第二轮通知 12-04；EI 非保证"],
  ["计算机视觉 / 模式识别", "ICPRAM 2027", "EI候选·中", "模式识别、机器学习、图像视频", null, d("2026-09-15"), d("2026-10-22"), d("2026-11-13"), "2027-02-20—02-22", "窗口内，可投", "官网称论文集提交 EI 评估", "https://icpram.scitevents.org/CallForPapers.aspx?y=2027", "第二轮通知 12-04；EI 非保证"],
  ["计算机视觉 / 模式识别", "ROBOVIS 2027", "EI候选·较高", "机器人视觉、智能系统", null, d("2026-09-15"), d("2026-10-22"), d("2026-11-13"), "2027-02-27—02-28", "窗口内，可投", "Springer CCIS；官网称论文集由 EI-Compendex 收录", "https://robovis.scitevents.org/CallforPapers.aspx", "第二轮通知 12-04；以最终卷检索为准"],
  ["计算机视觉 / 模式识别", "ICDIP 2027", "EI候选·较高", "数字图像处理、计算机视觉", null, d("2026-11-10"), null, d("2026-12-10"), "2027-04-16—04-18", "窗口内，可投", "SPIE Proceedings；官网声明 EI Compendex 等检索", "https://www.icdip.org/", "本表保留官网首轮 11-10"],

  ["多媒体 / 多媒体系统", "MMSys 2027", "非CCF专业", "多媒体系统、流媒体、QoE、视觉系统", d("2026-09-10"), d("2026-09-17"), d("2026-11-19"), d("2026-10-24"), "2027-03-30—04-02", "窗口内，两轮可投", "ACM Multimedia Systems Proceedings；不另作 EI 结论", "https://2027.acmmmsys.org/deadlines.html", "第一轮通知 10-24；第二轮注册 11-12、全文 11-19、通知 12-22"],
  ["多媒体 / 多媒体系统", "ICMR 2027", "CCF B·待公布", "多媒体检索、跨模态检索", null, null, null, null, "2027-06-07—06-10", "投稿日期待官网公布", "ACM ICMR Proceedings；不另作 EI 结论", "https://icmr2027.foodai.org/cfc", "官网已发布征稿范围，但截至 2026-07-20 尚未给出投稿日期"],
  ["多媒体 / 多媒体系统", "IVSP 2027", "EI候选·较高", "图像、视频、信号处理、多媒体技术", null, d("2026-09-20"), null, d("2026-10-25"), "2027-03-03—03-05", "窗口内，可投", "SPIE Proceedings；官网声明 EI Compendex / Scopus", "https://www.ivsp.net/", "官网列示 2019–2025 往届 EI 记录；当届仍以最终检索为准"],

  ["人机交互 / 智能交互", "HRI 2027", "非CCF专业", "人机交互、人机协作、社会机器人", d("2026-09-11"), d("2026-09-18"), null, null, "2027-03-08—03-12", "窗口内，可投", "ACM/IEEE HRI Proceedings；不另作 EI 结论", "https://humanrobotinteraction.org/2027/", "官网尚未公布 review / decision notification"],
  ["人机交互 / 智能交互", "CHIIR 2027", "非CCF专业", "人本信息检索、交互式检索、用户研究", d("2026-10-08"), d("2026-10-15"), d("2026-10-29"), d("2026-12-15"), "2027-03-07—03-11", "窗口内，多轨可投", "ACM SIGIR Proceedings；不另作 EI 结论", "https://chiir2027.github.io/", "短文、Demo、Design、Industry 等轨道截止 10-29"],
  ["人机交互 / 智能交互", "EHRI 2026", "EI候选·中", "具身智能、人机协作、人机交互", d("2026-07-16"), d("2026-08-01"), null, d("2026-09-13"), "2026-12-25—12-27", "窗口内，近期截止", "当届数字论文集提交 EI / Scopus 评估", "https://www.icehri.org/", "Final paper 11-15；提交评估不等于保证收录"],

  ["智能体 / 多智能体", "PRIMA 2026", "非CCF专业", "MAS 基础、协作协调、Agentic AI", d("2026-08-03"), d("2026-08-03"), null, d("2026-09-25"), "2026-12-14—12-17", "窗口内，延期截止", "多智能体专业会议；非 CCF", "https://www.prima2026.org/", "延期摘要/全文截止均为 8-03 AoE"],
  ["智能体 / 多智能体", "ICAART 2027", "EI候选·中", "Agents、MAS、LLM Agent、认知机器人", null, d("2026-09-15"), d("2026-10-22"), d("2026-11-13"), "2027-02-23—02-25", "窗口内，可投", "SCITEPRESS；官网称论文集提交 EI 评估", "https://icaart.scitevents.org/CallforPapers.aspx?y=2027", "第二轮通知 12-04；EI 非保证"],
  ["智能体 / 多智能体", "EUMAS 2026", "非CCF专业", "欧洲多智能体系统", null, d("2026-05-18"), null, d("2026-06-30"), "2026-09-21—09-25", "已关闭，仅关注下一届", "Springer LNCS", "https://euramas.github.io/eumas2026/", "专业度高，但不符合本轮投稿窗口"],
  ["智能体 / 多智能体", "IEEE/WIC WI-IAT 2026", "CCF C", "Web Intelligence、智能体技术", null, d("2026-07-15"), null, d("2026-08-31"), "2026-12-03—12-06", "已关闭，仅关注下一届", "录用论文提交 IEEE Xplore，须满足其要求", "https://www.wi-iat.org/wi-iat2026/index.html", "主会全文截止早于本轮窗口"],
];

const pickOriginal = (category) => originalRows.filter((r) => r[0] === category);
const pickExtras = (category) => extras.filter((r) => r[0] === category);
const rows = [
  ...pickOriginal("人工智能大类"), ...pickExtras("人工智能大类"),
  ...pickOriginal("计算机视觉 / 模式识别"), ...pickExtras("计算机视觉 / 模式识别"),
  ...pickOriginal("多媒体 / 多媒体系统"), ...pickExtras("多媒体 / 多媒体系统"),
  ...pickOriginal("人机交互 / 智能交互"), ...pickExtras("人机交互 / 智能交互"),
  ...pickOriginal("智能体 / 多智能体"), ...pickExtras("智能体 / 多智能体"),
  ...pickOriginal("其他 CCF B/C"),
];
if (rows.length !== 52) throw new Error(`Expected 52 retained+new rows, found ${rows.length}`);

const cityByConference = {
  "ICRA 2027": "首尔（韩国）",
  "ICARA 2027": "巴黎（法国）",
  "ICCAI 2027": "首尔（韩国）",
  "ISoIRS 2027": "待官网公布",
  "3DV 2027": "塞萨洛尼基（希腊）",
  "DCC 2027": "斯诺伯德（美国犹他州）",
  "FG 2027": "待官网公布",
  "VISAPP 2027": "待官网公布",
  "ICPRAM 2027": "待官网公布",
  "ROBOVIS 2027": "待官网公布",
  "ICDIP 2027": "北京（中国）",
  "ICASSP 2027": "多伦多（加拿大）",
  "MMAsia 2026": "待官网公布",
  "MMM 2027": "暹粒（柬埔寨）",
  "MMSys 2027": "根特（比利时）",
  "ICMR 2027": "新加坡",
  "IVSP 2027": "札幌（日本）",
  "IUI 2027": "赫尔辛基（芬兰）",
  "HRI 2027": "圣何塞（美国加州）",
  "CHIIR 2027": "柏林（德国）",
  "EHRI 2026": "成都（中国）",
  "AAMAS 2027": "河内（越南）",
  "DAI 2026": "香港（中国）",
  "PRIMA 2026": "熊本（日本）",
  "ICAART 2027": "待官网公布",
  "EUMAS 2026": "马尔默（瑞典）",
  "IEEE/WIC WI-IAT 2026": "布里斯班（澳大利亚）",
  "CIDR 2027": "阿姆斯特丹（荷兰）",
  "CSFW 2027": "东京（日本，暂定）",
  "CSFW 2027 Summer": "东京（日本，暂定）",
  "CSFW 2027 Fall": "东京（日本，暂定）",
  "WSDM 2027": "香港（中国）",
  "ICDT 2027": "里尔（法国）",
  "EDBT 2027": "里尔（法国）",
  "CGO 2027": "待官网公布",
  "DATE 2027": "待官网公布",
  "ISCAS 2027": "波尔多（法国）",
  "SIGMETRICS 2027": "亚特兰大（美国佐治亚州）",
  "CHES 2027": "待官网公布",
  "SANER 2027": "里士满（美国弗吉尼亚州）",
  "ADMA 2026": "香港（中国）",
  "ADMA 2026 Short": "香港（中国）",
  "ADMA 2026 Poster/Encore": "香港（中国）",
  "ECIR 2027": "南安普敦（英国）",
  "BigData 2026": "菲尼克斯（美国亚利桑那州）",
  "ICC 2027": "华盛顿哥伦比亚特区（美国）",
  "MSN 2026": "宁波（中国）",
  "WCNC 2027": "巴拿马城（巴拿马）",
  "AsiaCCS 2027": "澳门（中国）",
  "FC 2027": "Rockley（巴巴多斯，暂定）",
  "PETS 2027": "代尔夫特（荷兰）",
  "PETS 2027 Issue2": "代尔夫特（荷兰）",
  "PETS 2027 Issue3": "代尔夫特（荷兰）",
  "REFSQ 2027": "巴塞尔（瑞士）",
  "DSN 2027": "柏林（德国）",
};
rows.forEach((r) => r.splice(9, 0, cityByConference[r[1]] ?? "待官网公布"));

const workbook = Workbook.create();
const sheet = workbook.worksheets.add("全部会议汇总");
sheet.showGridLines = false;
sheet.mergeCells("A1:N1");
sheet.getRange("A1:N1").values = [["2026年8–11月会议完整汇总：AI · CV · 多媒体 · HCI · 智能体 · 其他"]];
sheet.mergeCells("A2:N2");
sheet.getRange("A2:N2").values = [["共 52 条：原清单 35 条 CCF B/C 全部保留，并加入 17 条 EI / 专业会议补充；举办城市已逐项核验，未公布者明确标注。"]];
sheet.mergeCells("A3:N3");
sheet.getRange("A3:N3").values = [["分组顺序：人工智能 → 计算机视觉 → 多媒体 → 人机交互 → 智能体 → 其他 CCF B/C；EI“提交评估”不代表最终收录。"]];
sheet.getRange("A5:N5").values = [["大类", "会议", "级别 / 类型", "细分方向", "摘要截止", "全文截止", "后续截止", "通知日期", "会议日期", "举办城市", "当前状态", "EI / 出版状态", "官网", "投稿轮次 / 核验备注"]];
sheet.getRange(`A6:N${5 + rows.length}`).values = rows;

const navy = "#1F4E78";
sheet.getRange("A1:N1").format = { fill: navy, font: { color: "#FFFFFF", bold: true, size: 16 }, horizontalAlignment: "center", verticalAlignment: "center", rowHeight: 32 };
sheet.getRange("A2:N2").format = { fill: "#EAF2F8", font: { color: navy, italic: true, size: 10 }, wrapText: true, verticalAlignment: "center", rowHeight: 28 };
sheet.getRange("A3:N3").format = { fill: "#F7F9FB", font: { color: "#44546A", size: 10 }, wrapText: true, verticalAlignment: "center", rowHeight: 26 };
sheet.getRange("A5:N5").format = { fill: navy, font: { color: "#FFFFFF", bold: true }, horizontalAlignment: "center", verticalAlignment: "center", wrapText: true, rowHeight: 34, borders: { preset: "all", style: "thin", color: "#B4C6E7" } };
sheet.getRange(`A6:N${5 + rows.length}`).format = { verticalAlignment: "center", wrapText: true, rowHeight: 44, borders: { preset: "all", style: "thin", color: "#D9E2F3" } };
sheet.getRange(`E6:H${5 + rows.length}`).format.numberFormat = "yyyy-mm-dd";
sheet.tables.add(`A5:N${5 + rows.length}`, true, "CompleteConferenceList2026").style = "TableStyleMedium2";

// Apply semantic styling dynamically from the actual rows.
const catFill = {
  "人工智能大类": "#DDEBF7",
  "计算机视觉 / 模式识别": "#E2F0D9",
  "多媒体 / 多媒体系统": "#FCE4D6",
  "人机交互 / 智能交互": "#D9E1F2",
  "智能体 / 多智能体": "#E4DFEC",
  "其他 CCF B/C": "#E7E6E6",
};
let previousCategory = null;
rows.forEach((r, idx) => {
  const excelRow = idx + 6;
  sheet.getRange(`A${excelRow}`).format.fill = catFill[r[0]];
  sheet.getRange(`A${excelRow}`).format.font = { bold: true, color: "#203864" };
  if (r[0] !== previousCategory) sheet.getRange(`A${excelRow}:N${excelRow}`).format.borders = { top: { style: "medium", color: navy } };
  previousCategory = r[0];

  const level = String(r[2]);
  if (level.startsWith("CCF B")) sheet.getRange(`C${excelRow}`).format.fill = "#D9EAF7";
  else if (level.startsWith("CCF C")) sheet.getRange(`C${excelRow}`).format.fill = "#E2F0D9";
  else if (level.includes("较高")) sheet.getRange(`C${excelRow}`).format.fill = "#C6E0B4";
  else if (level.includes("EI候选")) sheet.getRange(`C${excelRow}`).format.fill = "#FFF2CC";
  else sheet.getRange(`C${excelRow}`).format.fill = "#E7E6E6";

  const status = String(r[10]);
  sheet.getRange(`K${excelRow}`).format.fill = status.includes("已关闭") ? "#E7E6E6" : (status.includes("待官网") ? "#FFF2CC" : (status.includes("原清单") ? "#EAF2F8" : "#E2F0D9"));
  if (String(r[11]).includes("提交 EI 评估")) sheet.getRange(`L${excelRow}`).format.fill = "#FFF2CC";
  if (String(r[11]).includes("往届 EI") || String(r[11]).includes("EI-Compendex 收录") || String(r[11]).includes("SPIE Proceedings")) sheet.getRange(`L${excelRow}`).format.fill = "#E2F0D9";
});

const widths = { A: 175, B: 155, C: 110, D: 220, E: 98, F: 98, G: 98, H: 98, I: 145, J: 160, K: 150, L: 270, M: 295, N: 310 };
for (const [col, px] of Object.entries(widths)) sheet.getRange(`${col}:${col}`).format.columnWidthPx = px;
sheet.freezePanes.freezeRows(5);
sheet.freezePanes.freezeColumns(2);

const check = await workbook.inspect({ kind: "table", range: "全部会议汇总!A1:N57", include: "values,formulas", tableMaxRows: 60, tableMaxCols: 16, tableMaxCellChars: 180, maxChars: 46000 });
console.log("CHECK\n" + check.ndjson);
const errors = await workbook.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 300 }, summary: "final formula error scan" });
console.log("ERRORS\n" + errors.ndjson);

const preview = await workbook.render({ sheetName: "全部会议汇总", autoCrop: "all", scale: 1.05, format: "png" });
await fs.writeFile(`${outputDir}/previews/01_全部会议汇总.png`, new Uint8Array(await preview.arrayBuffer()));
const exported = await SpreadsheetFile.exportXlsx(workbook);
await exported.save(outputPath);
console.log(`OUTPUT ${outputPath}`);
