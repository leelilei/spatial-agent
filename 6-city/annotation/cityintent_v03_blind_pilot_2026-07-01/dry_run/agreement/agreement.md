# CityIntent Human Audit Agreement

Audit items: 16

Pending rows: `{"annotator_a": 0, "annotator_b": 0}`

## Inter-Annotator Agreement

| Field | n | Exact agreement | Cohen kappa |
|---|---:|---:|---:|
| `completion_label` | 16 | 0.75 | 0.522 |
| `feasibility_label` | 16 | 0.688 | 0.208 |
| `replan_label` | 16 | 0.875 | 0.652 |
| `evidence_sufficient` | 16 | 1.0 | 1.0 |
| `first_invalid_step` | 1 | 1.0 | 1.0 |

## Verifier Calibration

### annotator_a

| Field | n | Exact agreement |
|---|---:|---:|
| `completion_label` | 16 | 0.625 |
| `feasibility_label` | 16 | 0.688 |
| `replan_label` | 4 | 0.75 |

### annotator_b

| Field | n | Exact agreement |
|---|---:|---:|
| `completion_label` | 16 | 0.5 |
| `feasibility_label` | 15 | 0.733 |
| `replan_label` | 3 | 0.333 |

