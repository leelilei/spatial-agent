import re, os
from pathlib import Path

PDFS_DIR = Path("/Users/mac/Documents/6-Research/1-SpatialAgent/spatial-agent/references/pdfs")
MD_OUTPUT = Path("/Users/mac/Documents/6-Research/1-SpatialAgent/spatial-agent/references/paper_list.md")
BIB_OUTPUT = Path("/Users/mac/Documents/6-Research/1-SpatialAgent/spatial-agent/references/papers.bib")
REPORT_OUTPUT = Path("/Users/mac/Documents/6-Research/1-SpatialAgent/spatial-agent/references/download_status.md")

# Create dirs if not exist
PDFS_DIR.mkdir(parents=True, exist_ok=True)
MD_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with open("/Users/mac/Documents/6-Research/1-SpatialAgent/paperrefence.md", "r") as f:
    lines = f.readlines()

current_cat = "Unknown Category"
papers = []
current_paper = None

for line in lines:
    line = line.strip()
    if line.startswith("## Category"):
        current_cat = line.split(":", 1)[1].strip() if ":" in line else line.replace("## ", "")
    elif line.startswith("**") and re.match(r"^\*\*\d+\.", line):
        if current_paper: papers.append(current_paper)
        title = re.sub(r'^\*\*\d+\.\s*', '', line).strip('*').strip()
        current_paper = {"title": title, "category": current_cat, "authors": "", "year": "", "url": "", "venue": ""}
    elif line.startswith("- **Authors:**") or line.startswith("- **Author:**"):
        if current_paper: current_paper["authors"] = line.split("**", 2)[-1].strip()
    elif line.startswith("- **Venue:**"):
        if current_paper: current_paper["venue"] = line.split("**", 2)[-1].strip()
    elif line.startswith("- **Year:**"):
        if current_paper: current_paper["year"] = line.split("**", 2)[-1].strip()
    elif line.startswith("- **URL") or line.startswith("- **DOI"):
        if current_paper and not current_paper.get("url"):
            parts = line.split("**", 2)
            if len(parts) > 2:
                current_paper["url"] = parts[-1].strip().split('|')[0].strip()

if current_paper: papers.append(current_paper)

all_pdfs = [p.name for p in PDFS_DIR.rglob("*.pdf")]
missing = []

md_content = ["# 必读论文清单 (Auto-Generated)\n", "\n## 优先级说明\n- P0: 必须精读\n- P1: 需要精读\n- P2: 需要泛读\n\n## 论文列表\n"]
bib_content = []

current_cat_header = ""
for paper in papers:
    if paper["category"] != current_cat_header:
        current_cat_header = paper["category"]
        md_content.append(f"\n### {current_cat_header}\n")
        md_content.append("| 下载状态 | 论文 | 作者 | 年份 | 状态 | 笔记 |\n")
        md_content.append("|---|---|---|---|---|---|\n")

    found = False
    clean_title_words = ''.join(c for c in paper["title"] if c.isalnum() or c.isspace()).split()
    for pdf in all_pdfs:
        match_count = sum(1 for w in clean_title_words if len(w)>2 and w.lower() in pdf.lower())
        if match_count >= 2 or (len(clean_title_words) <= 2 and match_count == len(clean_title_words)):
            found = True
            break
            
    status = "✔ 已下载" if found else "✗ 缺失"
    if not found: missing.append(paper)
    
    title_link = f"[{paper['title']}]({paper['url']})" if paper.get('url') else paper["title"]
    md_content.append(f"| {status} | {title_link} | {paper.get('authors','')} | {paper.get('year','')} | ☐ 未读 | - |\n")
    
    bib_id = ""
    authors_field = paper.get("authors", "")
    if authors_field:
        first_author = authors_field.split(",")[0].split()[-1]
        bib_id = ''.join(c for c in first_author if c.isalnum()) + paper.get("year", "")
    else:
        bib_id = ''.join(c for c in clean_title_words[:1] if c.isalnum()) + paper.get("year", "")
        
    if bib_id:
        bib_content.append(f"@article{{{bib_id},\n  title={{{paper['title']}}},\n  author={{{paper.get('authors','')}}},\n  journal={{{paper.get('venue','')}}},\n  year={{{paper.get('year','')}}},\n  url={{{paper.get('url','')}}}\n}}\n\n")

with open(MD_OUTPUT, "w") as f:
    f.writelines(md_content)
with open(BIB_OUTPUT, "w") as f:
    f.writelines(bib_content)

with open(REPORT_OUTPUT, "w") as f:
    f.write("# 下载失败报告 (受限于反爬虫机制或需付费墙，请手动获取)\n\n")
    for m in missing:
        f.write(f"- **{m['title']}**\n  - URL: {m.get('url', 'N/A')}\n\n")

print(f"Generated {MD_OUTPUT.name}, {BIB_OUTPUT.name}, Missing: {len(missing)}")
