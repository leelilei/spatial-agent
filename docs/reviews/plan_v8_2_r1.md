# Review of `plan_v8_2.md`

**Venue Context**: AAMAS / AAAI  
**Reviewer Role**: Independent Expert Reviewer  
**Review Type**: Research Plan Review  
**Recommendation**: Major Revision

---

## Summary

This is a strong and substantially more focused research plan than many agent-systems proposals. The plan asks a clear central question: whether structured spatial descriptions can systematically shape LLM-agent behavior, and whether part of that response aligns with Space Syntax-inspired theoretical expectations. The document shows good discipline in defining contribution boundaries, elevating human evaluation, and separating confirmatory from exploratory components.

The plan is also unusually honest about what it does not claim. It does not present itself as a full validation of Space Syntax, nor as a claim that text-based agents are equivalent to embodied human spatial behavior. That restraint is appropriate and improves the plan's credibility.

My overall view is positive, but I do not think the plan is yet fully submission-ready. The main remaining issues concern internal validity, interpretation of controls, under-specification of the primary statistical pathway, and the gap between the elegance of the conceptual decomposition and the difficulty of executing it cleanly. The study is promising, but it still needs tightening before it can support a strong AAMAS or AAAI paper.

---

## Strengths

### 1. Clear central contribution

The plan has one recognizably central claim rather than a diffuse set of loosely related contributions. That is a major advantage for both execution and later paper writing.

### 2. Good boundary-setting

The document is explicit about what the study can and cannot show. This is especially important for a topic that risks overclaiming from text-only agents to physical-space theory.

### 3. Sensible decomposition of mechanism

The `C1 / C6m / C6f / C4` logic is one of the strongest parts of the proposal. It provides a plausible way to distinguish post-arrival interpretation, movement policy, and sampling effects without collapsing everything into a single monolithic intervention.

### 4. Stronger emphasis on external relevance

Making human evaluation a primary result is the right move. For this topic, statistical significance alone would be insufficient; practical perceptibility matters.

### 5. Better manuscript discipline

The plan's distinction between main-paper evidence and appendix material is thoughtful. This increases the chance that the final paper will be readable rather than technically overloaded.

---

## Major Concerns

### 1. The core causal question is still not fully isolated

The plan frames the central effect as the impact of structured spatial representation. However, the full system difference is still composed of multiple bundled changes:

- richer structured descriptions
- altered movement information
- sampling support
- potentially different decision burdens placed on the agent

The decomposition addresses this in principle, but the main claim will still depend heavily on whether the intermediate comparisons are clean and interpretable. If any link in the `C6m -> C6f -> C4` chain is noisy or unstable, the paper may end up with a convincing total effect but an ambiguous mechanism story.

This matters because the paper's novelty is not only that “something changed,” but that the change can be meaningfully attributed to structured spatial information rather than a general prompt-engineering upgrade.

**Recommendation**:

- Pre-register one primary causal claim and treat the mechanism decomposition as secondary unless the component comparisons are robust.
- Make explicit which result is sufficient for paper acceptance in the absence of a clean mechanism story.
- Define what counts as a failed decomposition versus a failed main hypothesis.

### 2. `C2` and `C2b` improve the control story, but they may still not be enough

The plan correctly repositions `C2` as a behavioral affordance baseline rather than a pure non-spatial control. That is an improvement. However, the control family still mixes different kinds of information:

- `C2` gives direct behavioral cues
- `C2b` gives non-spatial structural detail
- `C6m` gives spatially meaningful structure

These are conceptually useful baselines, but they are not tightly matched in cognitive burden or inferential distance. If `C6m` underperforms relative to `C2`, the interpretation may remain unclear: perhaps structure is weaker than direct behavioral prompting, or perhaps the representation requires more inference than the task permits. Similarly, if `C2b` is strong, the result may reflect general descriptive richness rather than space-specific structure.

**Recommendation**:

- Be explicit that the controls are interpretive baselines, not purity baselines.
- Add a plan for prompt-length and information-density matching across `C2`, `C2b`, and `C6m`.
- In the final paper, avoid overinterpreting any single contrast in this control family.

### 3. The statistical plan is directionally good but still not decision-complete

The plan provides the core `TAR_run` protocol and several mixed-model sketches, but the primary inferential path is still underspecified for a submission of this ambition.

Important questions remain:

- What is the single primary endpoint for the paper?
- Are the confirmatory tests run per map first and then meta-analyzed, or pooled with `map` as a factor?
- How exactly is multiplicity handled across hypotheses, contrasts, and time windows?
- What is the priority order between run-level, agent-level, and event-level analyses if they disagree?

At the moment, the reader can see pieces of the analysis strategy, but not yet one fully locked primary statistical narrative.

**Recommendation**:

- Define one primary endpoint and one primary contrast for the headline claim.
- Specify one official confirmatory analysis table listing each confirmatory comparison, its unit of analysis, correction method, and success criterion.
- State clearly that all other analyses are supportive or diagnostic.

### 4. The power logic is still somewhat optimistic relative to the design complexity

The plan is commendably conservative in saying it targets medium-to-large effects. Even so, the design remains ambitious:

- 3 maps
- 5 key conditions
- multiple hypothesis-aligned behaviors
- primary and robustness models
- time-window interpretation
- human evaluation

That is a lot of inferential surface area for 20 seeds per map. The main risk is not necessarily that no effect can be found, but that results become uneven across maps and contrasts, producing a paper with suggestive but fragmented evidence.

**Recommendation**:

- Explicitly rank all comparisons by importance before execution.
- Be prepared to treat some analyses as confirmatory and others as supporting, rather than trying to make the entire matrix carry equal evidential weight.
- Consider whether one map-aggregated primary result should dominate the submission narrative.

### 5. The human evaluation section is important but still underspecified

Elevating human evaluation is a good decision, but the protocol remains too high-level for a top-tier submission.

Key missing details include:

- how clips or behavior traces will be sampled
- whether raters are blind to condition and study purpose
- whether examples are balanced by map and scenario type
- whether raters compare paired outputs or independent outputs
- how inter-rater reliability will be handled

Because human evaluation now carries real interpretive weight, this section needs the same level of precision as the model-side analysis.

**Recommendation**:

- Predefine the sampling and balancing strategy for human-rating materials.
- Specify rater instructions, blindness, exclusion rules, and aggregation method.
- Report human-rating reliability as a first-class validity statistic, not just raw preference proportions.

### 6. Same-model Actor/Judge risk is still a real vulnerability

Using `Qwen3.5-Plus` for both Actor and Judge is operationally efficient, but it creates a credible concern that the scoring system may be partially aligned with the generation style of the same model family.

The robustness plan helps, but the same-model dependency still sits close to the core pipeline. If the main result depends strongly on the primary Judge, reviewers may question whether the effect is behavioral or merely legibility to the evaluator.

**Recommendation**:

- Make it explicit that rule-based and alternative-judge checks are not optional niceties but required credibility checks.
- Report the degree of convergence between human, rule-based, and alternative-LLM scoring.
- If those scorers disagree materially, downgrade the strength of the main claim.

---

## Minor Concerns

### 7. The plan still carries some terminology overhead

Even in its cleaned form, the plan includes many labels: `BSR`, `TAR`, `MIC`, `C1`, `C2`, `C2b`, `C4`, `C6m`, `C6f`, multiple stages, multiple appendices. This is manageable, but the final paper will still need a very strong design figure and a compact conditions table.

### 8. `H3` may remain weaker than `H1` and `H2`

The `Control Value` hypothesis is interesting, but it is also the most fragile because bottleneck-like nodes may be rare and because “gatekeeping behavior” is likely harder to annotate reliably. The paper should be prepared for `H3` to play a more limited role.

### 9. The cross-lingual extension is potentially distracting

The optional Chinese/English comparison is interesting, but it could also dilute the paper if introduced without strong motivation. Unless it is needed to explain a model effect, it should remain clearly secondary.

---

## Overall Assessment

This is a serious and thoughtfully designed plan with a realistic path to a publishable paper. Its best features are its focus, its conceptual honesty, and its attempt to connect agent behavior with structured spatial representations in a way that is methodologically inspectable. The main work remaining is not inventing more experiments, but locking the current design into a sharper inferential hierarchy.

If executed well, this could become a solid AAMAS paper and a plausible AAAI submission. But in its current form, I would still want revisions before I was confident that the eventual paper would be both convincing and easy to evaluate.

---

## Final Recommendation

**Major Revision**

The idea is strong, the plan is credible, and the contribution is potentially meaningful. The remaining challenge is to reduce interpretive ambiguity in the controls, make the statistical pathway fully explicit, and give the human-evaluation component the same rigor as the rest of the design.
