# WikiChurches Box-vs-Random regional-information probe

Predeclared decision: **GO**.

Only canonical train+val annotated images were encoded. Test images were used only as a filename exclusion set; encoded test images: 0.

## Data

- Images/churches: 97/97
- Official boxes: 433
- Matched random controls: 3464
- Controls above target official-overlap threshold: 16

## Primary paired result

- Mean image-level margin delta: +0.00649
- Paired bootstrap 95% CI: [+0.00511, +0.00803]
- Positive style directions: 3/4

| Style | Images | Mean paired margin Δ |
|---|---:|---:|
| Romanesque | 39 | +0.00797 |
| Gothic | 35 | +0.00740 |
| Renaissance | 8 | -0.00026 |
| Baroque | 15 | +0.00413 |

## Church-disjoint prototype CV

- Official-box balanced accuracy: 73.43%
- Random-region balanced accuracy: 49.22%
- Paired delta: +24.21 percentage points

## Decision checks

- mean_margin_delta: PASS
- bootstrap_ci_lower: PASS
- positive_style_directions: PASS
- prototype_balanced_accuracy_delta: PASS

This probe tests whether selected official regions carry more style information than area/aspect-matched same-image controls. It is not an end-to-end few-shot result and does not establish that unannotated regions are negatives.
