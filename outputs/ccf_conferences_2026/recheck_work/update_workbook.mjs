import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const inputPath = "/Users/mac/Documents/6-Research/outputs/ccf_conferences_2026/CCF会议投稿时间表_2026年8-11月.xlsx";
const outputDir = "/Users/mac/Documents/6-Research/outputs/ccf_conferences_2026/rechecked_2026-07-20";
const outputPath = `${outputDir}/CCF会议投稿时间表_2026年8-11月_复核完整版.xlsx`;

const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(inputPath));
const sheet = workbook.worksheets.getItem("会议清单");

const beforeStyle = await workbook.inspect({
  kind: "computedStyle",
  sheetId: "会议清单",
  range: "D7:I38",
  maxChars: 5000,
});
console.log("BEFORE_STYLE\n" + beforeStyle.ndjson);

const dates = {
  F7: "2026-10-06",
  F10: "2026-11-23",
  F11: "2026-11-02",
  F12: "2026-12-01",
  F13: "2027-01-27",
  F14: "2026-11-09",
  F16: "2027-01-11",
  F18: "2026-12-15",
  F19: "2026-12-01",
  F21: "2027-01-13",
  F23: "2026-12-02",
  F24: "2026-10-02",
  F26: "2026-09-04",
  F27: "2026-09-18",
  D28: "2026-09-21",
  E28: "2026-10-05",
  F28: "2026-12-07",
  F29: "2026-10-24",
  F30: "2027-01-15",
  F37: "2027-01-14",
  E38: "2026-12-02",
  F38: "2027-03-18",
};

for (const [cell, iso] of Object.entries(dates)) {
  sheet.getRange(cell).values = [[new Date(`${iso}T00:00:00Z`)]];
  sheet.getRange(cell).format.numberFormat = "yyyy-mm-dd";
}

const links = {
  H7: "https://www.cidrdb.org/cidr2027/cfp.html",
  H10: "https://iui.acm.org/2027/call-for-papers/",
  H12: "https://edbticdt2027.github.io/?contents=important_dates.html",
  H13: "https://edbticdt2027.github.io/?contents=important_dates.html",
  H14: "https://conf.researchr.org/dates/cgo-2027",
  H16: "https://2027.ieee-iscas.org/call-for-papers",
  H18: "https://ches.iacr.org/2027/",
  H19: "https://conf.researchr.org/dates/saner-2027",
  H21: "https://2027.ieeeicassp.org/important-dates/",
  H24: "https://www.mmasia2026.org/important-dates",
  H26: "https://adma2026.github.io/important_date.html",
  H27: "https://adma2026.github.io/important_date.html",
  H28: "https://www.ecir2027.co.uk/",
  H29: "https://bigdataieee.org/BigData2026/important-dates/",
  H30: "https://icc2027.ieee-icc.org/authors/call-symposium-papers",
  H37: "https://2027.refsq.org/dates",
  H38: "https://dsn2027-berlin.github.io/call-for-contributions/",
};
for (const [cell, url] of Object.entries(links)) sheet.getRange(cell).values = [[url]];

const notes = {
  I7: "已确认：作者通知 2026-10-06",
  I10: "最终决定 2026-11-23；初步通知 2026-10-29",
  I11: "已确认：Notifications 2026-11-02",
  I12: "已确认：ICDT 第二轮通知 2026-12-01",
  I13: "最终通知 2027-01-27；初轮 Acc/Rej/Rev 2026-12-05",
  I14: "已确认：R2 作者通知 2026-11-09",
  I15: "截至 2026-07-20，官方 CFP 仍未公布作者通知时间",
  I16: "已确认：作者通知 2027-01-11",
  I18: "通知 2026-12-15；官网标注日程为 tentative",
  I19: "已确认：Research Track 通知 2026-12-01",
  I20: "截至 2026-07-20，官方 OpenReview 仅公布摘要/全文截止",
  I21: "已确认：Paper Acceptance Notification 2027-01-13",
  I23: "最终通知 2026-12-02；初步通知 2026-10-27",
  I24: "已确认：Acceptance Notification 2026-10-02",
  I26: "已确认：Short Paper 通知 2026-09-04",
  I27: "已确认：Poster/Encore 通知 2026-09-18",
  I28: "官网当前标注 proposed：摘要 9-21、全文 10-05、通知 12-07",
  I29: "已确认：Paper Acceptance 2026-10-24",
  I30: "已确认：Notification of Acceptance 2027-01-15",
  I37: "已确认：Research Authors notification 2027-01-14",
  I38: "全文 2026-12-02；最终通知 2027-03-18；早拒 2027-01-26",
};
for (const [cell, note] of Object.entries(notes)) sheet.getRange(cell).values = [[note]];

sheet.getRange("G38").values = [["Research track：摘要 / 全文"]];
sheet.getRange("B2").values = [[new Date("2026-07-20T00:00:00Z")]];
sheet.getRange("B2").format.numberFormat = "yyyy-mm-dd";

await fs.mkdir(outputDir, { recursive: true });
const exported = await SpreadsheetFile.exportXlsx(workbook);
await exported.save(outputPath);

const check = await workbook.inspect({
  kind: "table",
  range: "会议清单!A1:I38",
  include: "values,formulas",
  tableMaxRows: 50,
  tableMaxCols: 12,
  tableMaxCellChars: 180,
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

const previewDir = `${outputDir}/previews`;
await fs.mkdir(previewDir, { recursive: true });
for (let i = 0; i < workbook.worksheets.items.length; i++) {
  const ws = workbook.worksheets.getItemAt(i);
  const preview = await workbook.render({ sheetName: ws.name, autoCrop: "all", scale: 1.4, format: "png" });
  await fs.writeFile(`${previewDir}/${String(i + 1).padStart(2, "0")}_${ws.name}.png`, new Uint8Array(await preview.arrayBuffer()));
}

console.log(`OUTPUT ${outputPath}`);
