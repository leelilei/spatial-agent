import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const inputPath = "/Users/mac/Documents/6-Research/outputs/ccf_conferences_2026/CCF会议投稿时间表_2026年8-11月.xlsx";
const outputDir = "/Users/mac/Documents/6-Research/outputs/ccf_conferences_2026/recheck_work/previews";
await fs.mkdir(outputDir, { recursive: true });

const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(inputPath));
const overview = await workbook.inspect({
  kind: "workbook,sheet,table",
  maxChars: 16000,
  tableMaxRows: 100,
  tableMaxCols: 30,
  tableMaxCellChars: 240,
});
console.log(overview.ndjson);

const sheetInfo = await workbook.inspect({ kind: "sheet", include: "id,name", maxChars: 8000 });
console.log("SHEETS\n" + sheetInfo.ndjson);

for (let i = 0; i < workbook.worksheets.items.length; i++) {
  const sheet = workbook.worksheets.getItemAt(i);
  const used = sheet.getUsedRange();
  const inspection = await workbook.inspect({
    kind: "region",
    sheetId: sheet.name,
    range: used?.address ?? "A1:Z100",
    maxChars: 30000,
    tableMaxRows: 200,
    tableMaxCols: 30,
    tableMaxCellChars: 300,
  });
  console.log(`SHEET ${sheet.name}\n${inspection.ndjson}`);
  const preview = await workbook.render({ sheetName: sheet.name, autoCrop: "all", scale: 1.4, format: "png" });
  await fs.writeFile(`${outputDir}/${String(i + 1).padStart(2, "0")}_${sheet.name.replaceAll("/", "_")}.png`, new Uint8Array(await preview.arrayBuffer()));
}
