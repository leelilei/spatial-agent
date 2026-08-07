import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const inputPath = "/Users/mac/Documents/6-Research/outputs/ccf_conferences_2026/rechecked_2026-07-20/CCF会议投稿时间表_2026年8-11月_复核完整版.xlsx";
const outputDir = "/Users/mac/Documents/6-Research/outputs/ccf_conferences_2026/rechecked_ai_cv_2026-07-20";
const outputPath = `${outputDir}/CCF会议投稿时间表_2026年8-11月_AI-CV控制补充复核版.xlsx`;

await fs.mkdir(`${outputDir}/previews`, { recursive: true });
const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(inputPath));
const sheet = workbook.worksheets.getItem("会议清单");

// Required pre-edit visual baseline.
const before = await workbook.render({ sheetName: "会议清单", autoCrop: "all", scale: 1.2, format: "png" });
await fs.writeFile(`${outputDir}/previews/00_before_会议清单.png`, new Uint8Array(await before.arrayBuffer()));

console.log(`STRUCTURED_TABLES ${sheet.tables.items.length}`);
const structuredTable = sheet.tables.items[0];
console.log(`STRUCTURED_TABLE_NAME ${structuredTable.name}`);
console.log(`STRUCTURED_DATA_RANGE ${structuredTable.getDataRows().address}`);
console.log((await workbook.inspect({
  kind: "computedStyle",
  sheetId: "会议清单",
  range: "A36:I38",
  maxChars: 7000,
})).ndjson);

const newRows = [
  [
    "ICRA 2027", "B", "人工智能/机器人/控制", null,
    new Date("2026-09-15T00:00:00Z"), new Date("2027-01-31T00:00:00Z"),
    "Technical papers", "https://2027.ieee-icra.org/contribute/call-for-icra-2027-papers-now-accepting-submissions/",
    "本轮补漏；CCF B；官网已确认投稿与录用通知日期",
  ],
  [
    "DCC 2027", "B", "图像/视频压缩/视觉编码", null,
    new Date("2026-10-02T00:00:00Z"), new Date("2026-11-22T00:00:00Z"),
    "Full paper", "https://datacompressionconference.org/important-dates/",
    "本轮补漏；CCF B；范围含图像/视频、视觉搜索及深度学习压缩",
  ],
  [
    "FG 2027", "C", "计算机视觉/模式识别/生物特征", new Date("2026-10-09T00:00:00Z"),
    new Date("2026-10-16T00:00:00Z"), new Date("2026-12-20T00:00:00Z"),
    "Main conference：摘要 / 全文", "https://fg2027.ieee-biometrics.org/dates/",
    "本轮补漏；CCF C；官网日期均为 AoE",
  ],
];

const startRow = 39;
const endRow = startRow + newRows.length - 1;
structuredTable.rows.add(null, newRows);
console.log(`STRUCTURED_DATA_RANGE_AFTER ${structuredTable.getDataRows().address}`);
sheet.getRange(`D${startRow}:F${endRow}`).format.numberFormat = "yyyy-mm-dd";

// Match the existing CCF-rank color convention while preserving row banding elsewhere.
sheet.getRange("B39:B40").format.fill = "#D9EAF7";
sheet.getRange("B39:B40").format.font = { color: "#1F4E78" };
sheet.getRange("B41").format.fill = "#E2F0D9";
sheet.getRange("B41").format.font = { color: "#548235" };

// The source row had a yellow unresolved-note style; confirmed new rows use the normal body style.
sheet.getRange("I39:I41").format.fill = "#FFFFFF";
sheet.getRange("I39:I41").format.font = { color: "#000000" };
sheet.getRange("A39:I41").format.wrapText = true;

const check = await workbook.inspect({
  kind: "table",
  range: "会议清单!A35:I41",
  include: "values,formulas",
  tableMaxRows: 20,
  tableMaxCols: 12,
  tableMaxCellChars: 220,
  maxChars: 16000,
});
console.log("CHECK\n" + check.ndjson);

const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 300 },
  summary: "final formula error scan",
});
console.log("ERRORS\n" + errors.ndjson);

for (let i = 0; i < workbook.worksheets.items.length; i++) {
  const ws = workbook.worksheets.getItemAt(i);
  const preview = await workbook.render({ sheetName: ws.name, autoCrop: "all", scale: 1.4, format: "png" });
  await fs.writeFile(`${outputDir}/previews/${String(i + 1).padStart(2, "0")}_${ws.name}.png`, new Uint8Array(await preview.arrayBuffer()));
}

const exported = await SpreadsheetFile.exportXlsx(workbook);
await exported.save(outputPath);
console.log(`OUTPUT ${outputPath}`);
