# CityIntent v1 Release Gate

Status: `pending_human_audit`

Benchmark: `1.0-rc1` / `release_candidate_pending_human_audit`

## Blockers

- two-person human audit incomplete: {'annotator_a': 0, 'annotator_b': 16}

## Human Audit

Pending rows: `{"annotator_a": 0, "annotator_b": 16}`

Material findings: 0

## Runtime Checks

- `0`: `/opt/anaconda3/bin/python -m unittest discover -s /Users/mac/Documents/6-Research/6-city/benchmarks/cityintent_v0/tests -p test_*.py`
- `0`: `/opt/anaconda3/bin/python /Users/mac/Documents/6-Research/6-city/benchmarks/cityintent_v0/tools/validate_cityintent_v0.py`
- `0`: `/opt/anaconda3/bin/python /Users/mac/Documents/6-Research/6-city/benchmarks/cityintent_v0/tools/validate_external_adapters.py --framework all`
