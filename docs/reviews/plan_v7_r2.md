# Second Review of "Where You Are Shapes Who You Become: Space Syntax-Informed LLM Agents for Spatially Believable Game Worlds"

**Reviewer**: Expert Reviewer 2  
**Date**: 2026-04-01  
**Plan Version**: v7.0  
**Recommendation**: Major Revision

---

## Overall Assessment

This is a substantially improved plan. The v7 revision is more disciplined than earlier versions in how it defines the main estimands, separates exploratory from confirmatory components, and constrains theoretical overclaiming. In particular, the explicit `TAR_run` protocol, the `C6m/C6f/C4` decomposition, and the clearer statement of claim boundaries make the study more reviewable and more executable.

My remaining concern is less about whether the design is careful, and more about whether the paper is currently trying to be too many things at once. At present, the project reads as a bundle of contributions: a spatial representation protocol, a causal decomposition of perception/movement/sampling, a new metric pair (`BSR/TAR`), a matched-initial-conditions design, a coding protocol, a robustness program, and a possible multi-map extension. Each component is defensible on its own, but together they create a risk that the final paper will feel method-heavy and contribution-diffuse rather than centered around one sharp take-away.

For that reason, my recommendation remains **Major Revision**, but the path forward is clear: reduce narrative load, clarify the primary claim, and define what counts as success even under mixed empirical results.

---

## Strengths

### 1. The plan is now much more intellectually honest

The revised framing is appropriately careful about what the study does and does not claim. The distinction between validating a structured spatial representation effect and "validating Space Syntax" as a whole is important and well judged.

### 2. The confirmatory core is stronger than before

The central comparison logic is more coherent in v7. The split between `C6m`, `C6f`, and `C4` gives the paper a plausible causal narrative rather than a simple condition bake-off.

### 3. The metrics are operationalized rather than merely named

`TAR_run` is no longer a conceptual placeholder. The location-level aggregation and Fisher-z transformation make the analysis pipeline concrete enough to audit and reproduce.

### 4. The author shows good judgment about risk management

The plan anticipates several likely reviewer objections in advance, especially around coding reliability, C2 leakage, and the limited contribution of MIC. That is a real strength.

---

## Major Concerns

### 1. The paper's main contribution is still not singular enough

The current draft appears to make several contributions of similar rhetorical weight:

- a structured spatial representation framework
- a two-metric outcome design (`BSR` and `TAR`)
- a decomposition of perception, movement, and sampling
- a matched-initial-conditions experimental protocol
- a broader methodology for long-horizon LLM agent studies

This is too many "main" contributions for one paper unless they are strictly subordinated to a single thesis. Right now, a reader could come away unsure whether the paper is primarily about spatial representation, experimental design, metric design, or reproducibility protocol.

**Recommendation**:

- Define one primary contribution and treat the rest as supporting machinery.
- My recommended hierarchy is:
  - primary contribution: structured spatial representations can systematically alter LLM-agent behavior, with part of that effect aligning with space-syntax-style predictions
  - secondary contribution: `C6m/C6f/C4` disentangles where the effect enters the pipeline
  - tertiary contribution: `BSR/TAR` and MIC are implementation tools, not headline claims

If this hierarchy is not enforced, the final manuscript will likely feel overengineered.

### 2. The metric system risks becoming a communication burden

`BSR`, `TAR`, `TAR_run`, hypothesis-specific variants, overall aggregation, entropy, priming windows, and multiple robustness readouts may be analytically useful, but they impose a large explanatory tax on the reader. A good metric system should increase inferential clarity; here it may instead increase interpretive friction.

The key issue is not whether the metrics are wrong, but whether the paper can teach them quickly enough for reviewers to trust the results without losing the narrative thread.

**Recommendation**:

- Pre-commit to one primary response-existence metric and one primary theory-alignment metric in the main paper.
- Move most auxiliary metrics and robustness forms to appendix tables.
- Include an early "how to read the results" box or figure that explains in one page what positive, null, and dissociated `BSR/TAR` patterns mean.

Without this compression, the paper may be judged as complicated rather than rigorous.

### 3. The staged program is stronger as a research agenda than as a single paper

Stage 1, Stage 2, mechanism probes, robustness subsets, human evaluation, and Stage 3 together form a credible research program. But a conference paper is not a lab roadmap. The current plan still risks sounding like a grant proposal rather than a sharply bounded submission.

This matters because reviewers will often evaluate the manuscript they imagine you will write, not the internal design discipline behind it. If too many stages are treated as central, the main claim will seem underfocused.

**Recommendation**:

- Treat Stage 2 as the unquestioned center of the paper.
- Use Stage 1 only to motivate that the representation matters at all.
- Put Stage 3 firmly behind a gate and present it, if included, as a scope extension rather than part of the paper's core evidential burden.
- Keep human evaluation optional unless it becomes essential to the final paper claim.

The current plan already gestures in this direction, but the writing logic needs to be stricter than the research logic.

### 4. The plan does not yet specify a clean result-to-claim matrix

The design is detailed, but the publication logic is still underspecified. What exactly will the paper claim if the outcomes are mixed?

For example:

- What if `BSR` is positive but `TAR` is weak or unstable?
- What if `C4 > C1`, but `C6m` and `C6f` do not separate cleanly?
- What if effects appear in early windows only?
- What if Stage 1 is strong but Stage 2 is directionally messy?

Without a result-to-claim matrix, the eventual manuscript may drift into post hoc interpretation. Reviewers will notice this immediately.

**Recommendation**:

- Add an explicit decision table mapping major result patterns to allowable claims.
- Define in advance what constitutes:
  - representational success
  - theory-aligned success
  - mechanism ambiguity
  - null-but-informative outcome

This would materially strengthen the plan because it converts methodological detail into interpretive discipline.

### 5. Exp1C and the mechanism conditions still threaten to dominate reviewer attention

Even after the v7 revision, `Exp1C` remains conceptually interesting but rhetorically dangerous. It is the kind of design that attracts reviewer discussion because it is easy to debate and easy to misunderstand. The same is true of `Shuffled`, `Judge-Only`, `Fixed-Path`, and `Rule-Based` comparisons.

The problem is not that these components are bad. The problem is salience. If too much manuscript space is spent explaining them, reviewers may treat them as central tests and then judge the paper against standards they were never meant to satisfy.

**Recommendation**:

- Explicitly rank all experiments by evidential priority in the paper outline.
- Keep `Exp1C` framed as a supporting or interpretive experiment, not as a pillar of the confirmatory case.
- Present mechanism conditions as diagnostic probes, not co-equal tests of the main thesis.

The paper should make it impossible for a reader to confuse "interesting side evidence" with "main claim support."

### 6. Readability and submission strategy remain serious risks

The plan is very thorough, but it is also dense. The naming system (`BSR`, `TAR`, `MIC`, `C1-C7`, `Exp1A`, `Exp1C`, staged sections, multiple gates) creates a high onboarding cost. This may be acceptable for an internal plan, but not for a conference paper unless aggressively simplified.

**Recommendation**:

- Create a strict main-paper vs appendix split before running the full study.
- Keep the main paper centered on:
  - one motivating question
  - one core design figure
  - one primary table of conditions
  - one primary result figure for `BSR/TAR`
- Push operational detail, pilot logic, budget logic, and most decision thresholds out of the main narrative.

At present, the strongest risk is not bad science. It is that the paper's structure may hide the science it actually has.

---

## Minor Concerns

### 7. The target audience is still somewhat ambiguous

The plan seems to speak simultaneously to multi-agent simulation researchers, game-AI researchers, architectural theory readers, and LLM evaluation readers. A paper can reach multiple communities, but it must write to one primary audience. The current framing still needs a clearer home.

### 8. The role of human evaluation is strategically unclear

The plan labels human evaluation as optional, which is reasonable for execution. But from a paper-positioning perspective, it is unclear whether believability is merely a bonus external-validity signal or part of the reason this work matters. That should be decided earlier.

### 9. The title remains more expansive than the actual claims

The current title is memorable, but it suggests a broader developmental or identity-level claim than the study actually supports. A more precise title would better match the paper's empirical scope.

---

## Verdict

This is a strong and much improved research plan. The remaining revisions should focus less on adding more methodological safeguards and more on reducing conceptual and narrative overload. The study is close to being compelling, but it still needs a stricter contribution hierarchy and a clearer publication logic.

If those issues are addressed, the project has a realistic path to becoming a solid conference submission.

---

## Final Recommendation

**Major Revision**

The study design is now credible. The main remaining task is to turn a sophisticated research program into a paper with one unmistakable center of gravity.
