# Research Tools

This directory contains shared helper tools for projects under
`/Users/mac/Documents/6-Research`.

## Tools

- `research-dashboard/`: recommended local HTML dashboard for research project
  progress and markdown todo files
- `research-todo/`: deprecated native macOS menu bar app kept for reference
- `research-standard/`: scaffold, compliance checks, migration helpers, and
  standard literature-asset tooling

## Standard Literature Workflow

After archiving PDFs under a project such as `6-city/assets/papers/pdf/`, convert
them to Markdown fulltext with:

```bash
python D:/0-Research/0-Tools/research-standard/convert_pdfs_to_fulltext.py D:/0-Research/6-city
```

The converter writes:

- `assets/papers/fulltext/**/*.fulltext.md`
- `assets/papers/fulltext/**/*.meta.json`
- `assets/papers/metadata/fulltext_manifest.json`
- `assets/papers/metadata/fulltext_summary.md`
