from pathlib import Path

from spatial_agent_survey.ingest import (
    dedupe_papers,
    ingest_search_results,
    openalex_result_to_raw_record,
    papers_to_rows,
    reconstruct_openalex_abstract,
    write_csv,
)


def test_ingest_search_results_normalizes_multiple_raw_shapes(tmp_path):
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    (raw_dir / "A.jsonl").write_text(
        '\n'.join(
            [
                '{"title":"Paper One","abstract":"A","year":2025,"url":"https://example.com/1","authors":["Ada","Bob"]}',
                '{"paperTitle":"Paper Two","summary":"B","publication_year":"2024","link":"https://example.com/2","author":"Carol; Dan"}',
            ]
        ),
        encoding="utf-8",
    )
    papers = ingest_search_results(raw_dir)
    assert len(papers) == 2
    assert papers[0].title == "Paper One"
    assert papers[1].title == "Paper Two"
    assert papers[1].source_families == ["A"]
    rows = papers_to_rows(papers)
    assert rows[1]["authors"] == "Carol; Dan"


def test_dedupe_papers_merges_source_families():
    papers = [
        ingest_search_results_from_payload("A", [{"title": "Same Paper", "year": 2025, "url": "https://example.com/x"}])[0],
        ingest_search_results_from_payload("B", [{"title": "Same Paper", "year": 2025, "url": "https://example.com/x"}])[0],
    ]
    deduped, duplicates = dedupe_papers(papers)
    assert len(deduped) == 1
    assert len(duplicates) == 1
    assert deduped[0].source_families == ["A", "B"]


def test_reconstruct_openalex_abstract_orders_tokens():
    inverted_index = {
        "world": [1],
        "hello": [0],
        "agents": [2],
    }
    assert reconstruct_openalex_abstract(inverted_index) == "hello world agents"


def test_openalex_result_to_raw_record_normalizes_core_fields():
    raw = {
        "id": "https://openalex.org/W123",
        "doi": "https://doi.org/10.1000/example",
        "title": "Sample OpenAlex Paper",
        "publication_year": 2025,
        "abstract_inverted_index": {"paper": [1], "sample": [0]},
        "primary_location": {
            "landing_page_url": "https://example.com/paper",
            "source": {"display_name": "ExampleConf"},
        },
        "authorships": [
            {"author": {"display_name": "Ada Lovelace"}},
            {"author": {"display_name": "Alan Turing"}},
        ],
        "type": "article",
        "cited_by_count": 42,
        "ids": {"openalex": "https://openalex.org/W123"},
    }
    record = openalex_result_to_raw_record(
        raw,
        query_family="D",
        search_variant="generative agents social simulation",
        search_batch="phase1_openalex_2026-04-13",
    )
    assert record["title"] == "Sample OpenAlex Paper"
    assert record["abstract"] == "sample paper"
    assert record["venue"] == "ExampleConf"
    assert record["doi"] == "10.1000/example"
    assert record["authors"] == ["Ada Lovelace", "Alan Turing"]
    assert record["query_family"] == "D"


def test_write_csv_can_emit_utf8_bom_for_spreadsheet_compatibility(tmp_path):
    path = tmp_path / "manual_review.csv"
    write_csv(
        path,
        [{"title": "测试", "note": "中文列"}],
        ["title", "note"],
        encoding="utf-8-sig",
    )
    raw = path.read_bytes()
    assert raw.startswith(b"\xef\xbb\xbf")


def ingest_search_results_from_payload(stem: str, payload: list[dict]):
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as temp_dir:
        raw_dir = Path(temp_dir)
        path = raw_dir / f"{stem}.jsonl"
        path.write_text("\n".join(__import__("json").dumps(row) for row in payload), encoding="utf-8")
        return ingest_search_results(raw_dir)
