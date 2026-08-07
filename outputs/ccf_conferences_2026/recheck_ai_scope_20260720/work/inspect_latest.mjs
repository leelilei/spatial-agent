import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const p = "/Users/mac/Documents/6-Research/outputs/ccf_conferences_2026/rechecked_ai_cv_2026-07-20/CCF会议投稿时间表_2026年8-11月_AI-CV控制补充复核版.xlsx";
const wb = await SpreadsheetFile.importXlsx(await FileBlob.load(p));
console.log((await wb.inspect({
  kind: "table",
  range: "会议清单!A1:I41",
  include: "values,formulas",
  tableMaxRows: 50,
  tableMaxCols: 12,
  tableMaxCellChars: 240,
  maxChars: 30000,
})).ndjson);
