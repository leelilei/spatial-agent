# PAT-B-260728-001 protocol amendment

The feature encoder revealed, before any shift statistic was inspected, that
the canonical train file contains 5,838 views rather than one image per
church.

Two corrections were therefore made before the official analysis:

1. all train and validation features are aggregated to the church level;
2. the primary global comparison uses the same 90 box-bearing train churches
   as the local representation, while all canonical-train churches are
   retained as a negative reference control.

The first analysis process, which used all canonical-train churches as the
primary global comparison, is excluded from the formal decision. Its global
null result is reproduced in the corrected analysis as the declared
all-train control.

No test image, test feature, or test label was loaded in either analysis.
