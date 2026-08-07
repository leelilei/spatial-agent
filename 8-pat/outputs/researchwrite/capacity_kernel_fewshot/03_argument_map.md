# Argument map

## Scientific tension

- Known: a frozen DINOv2-B embedding plus RBF already beats multiple bespoke local and adaptation mechanisms.
- Unknown: whether the bottleneck is model capacity and whether capacities contain complementary task geometry.
- Why it matters: few-shot papers often compare methods while silently changing pretraining, backbone capacity, or classifier; a controlled capacity/kernel study can reveal where gains actually come from.

## Central research question

Can task-local nested selection over DINOv2-B/L kernels provide a stable, leakage-controlled improvement for 200-way few-shot fine-grained recognition?

## Central thesis

If L scaling produces a repeatable gain and DCKS selects or fuses capacities without outer-label tuning, a simple frozen-feature pipeline is a more reliable practical solution than small-data neural adaptation.

## Supporting arguments

1. Three episodes establish B+RBF as a stable reference rather than a lucky split.
2. B and L encode the same images at different capacities, enabling controlled capacity attribution.
3. Inner OOF kernel selection separates method development from outer evaluation.
4. Class-level deltas and mode frequencies reveal whether gains come from robust scaling, genuine fusion, or endpoint selection.

## Counterarguments

1. DCKS may simply choose L-only, leaving an empirical benchmark rather than a method advance.
2. Larger capacity raises inference cost and may not transfer to other datasets.
3. CUB episodes share the same source pool; a second dataset remains necessary.

## Final move

Run episode 1 with a frozen kernel bank. A route Go unlocks untouched episodes 2/3. Only confirmed results justify a second-dataset protocol and paper draft.
