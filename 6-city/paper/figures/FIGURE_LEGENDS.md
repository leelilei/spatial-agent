# Main figure legends

## Fig. 1 | Overview of the CityIntent evaluation framework

**a**, CityIntent evaluation loop connecting a private intention, blind agent
policy, executable action protocol, dynamic city simulator and evidence-based
scorer. Public events alter the world during execution. **b**, Scenario anatomy
separating intention, world state, events, constraints, oracle evidence and a
matched negative. **c**, Eight intention constructs used throughout the
benchmark. **d**, Mechanism-by-world construction plan. Filled cells denote
accepted public calibration sources; dashed cells denote the planned Wave-4
public instances. Private worlds remain pending. The framework evaluates
verified outcomes rather than plausible action narration.

## Fig. 2 | Comparison of model and agent-policy performance

**a**, Mean task completion and item-level bootstrap 95% confidence intervals
for six model-policy systems on 24 Wave-3 public items. Confidence intervals
were estimated with 5,000 deterministic bootstrap resamples over items.
**b**, Mean task completion for each system and intention construct.
**c**, Paired item-level difference between ReAct and Plan-and-Execute for each
model; diamonds show the mean difference and points denote individual items
(n = 24 items per model). **d**, Mean task completion, trace feasibility,
intention consistency and full-task rate. Source data are provided as a Source
Data file.

## Fig. 3 | Mechanism diversity and cross-world validity

**a**, Distribution of item difficulty for the three accepted mechanism
sources (n = 24 public instances per source). The Wave-4 position is retained
without quantitative marks pending data collection. **b**, Mean task
completion across three public city topologies and accepted mechanism sources.
**c**, Wave-3 item difficulty versus corrected item-total correlation; the
shaded region denotes the accepted difficulty interval and the dashed line the
minimum correlation threshold. Each point denotes one public item.
**d**, Wave-3 promotion funnel from generation to cross-world acceptance.
Source data are provided as a Source Data file.

## Fig. 4 | Dynamic public updates expose stale execution commitments

**a–c**, Same-model, same-item action timelines for route disruption,
event-revealed reservation and updated social co-presence. For each construct,
the displayed model was selected by the largest observed ReAct minus
Plan-and-Execute task-completion difference. Circles indicate ReAct actions,
squares indicate Plan-and-Execute actions and dashed vertical lines indicate
public events. Values at right report final task completion. These traces are
representative case studies linked to the complete aggregate analysis in
Fig. 2. Source data are provided as a Source Data file.

## Fig. 5 | Current validity evidence and preregistered release gates

**a**, Oracle and matched-negative task completion for 24 Wave-3 public items.
Lines connect controls belonging to the same item. **b**, Distributions of
empirical item difficulty, observed six-system range and corrected item-total
correlation across three public worlds (n = 24 items). The dashed line denotes
the minimum accepted correlation. **c**, Prespecified human-scoring agreement
panel, retained without quantitative marks until 72 stratified traces have been
independently annotated. **d**, Prespecified public-private generalization
panel, retained without quantitative marks until the 48-item private test has
been completed. Source data are provided as a Source Data file.
