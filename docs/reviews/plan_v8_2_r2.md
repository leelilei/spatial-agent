# Review of "Do Spatial Descriptions Shape LLM Agent Behavior? A Space Syntax-Informed Investigation"

**Conference**: AAMAS-27  
**Reviewer**: Expert Reviewer (AAMAS PC Member)  
**Date**: 2026-04-01  
**Plan Version**: v8.2  

---

## Overall Assessment

This research plan represents a substantial improvement over earlier versions. The authors have clearly responded to prior feedback by focusing the contribution, strengthening theoretical justification, and establishing clear boundaries between confirmatory and exploratory components. The plan is now centered on a single, well-defined research question with appropriate methodological rigor.

However, while the plan is now more focused and executable, several concerns remain about the fundamental validity of the approach, the practical significance of the expected findings, and whether the study design can actually deliver on its stated goals.

**Recommendation**: Weak Accept (Borderline)

**Score**: 6/10

---

## Strengths

### 1. Clear Contribution Hierarchy

The plan now has a single, well-articulated primary contribution: demonstrating that structured spatial representations can systematically alter LLM agent behavior with partial Space Syntax alignment. The supporting mechanisms (C6m/C6f/C4 decomposition, BSR/TAR metrics, MIC design) are appropriately positioned as methodological tools rather than co-equal contributions.

This is a significant improvement over v7 and addresses the "too many contributions" problem effectively.

### 2. Honest Theoretical Positioning

Section 2.3 ("Why text-based spatial descriptions might preserve effective information") is a genuine attempt to address the fundamental validity question. The authors acknowledge that:
- Text cannot fully replicate embodied affordance
- The study tests "linguistic associations" rather than "true spatial reasoning"
- The work is positioned as "proof of concept" not "complete validation"

This intellectual honesty is commendable and appropriate for the scope of the work.

### 3. Pre-Registered Interpretation Logic

The result-to-claim decision matrix (Section 8) is excellent. It prevents post-hoc rationalization and demonstrates that the authors have thought through what different result patterns would mean. The seven patterns cover the major outcome scenarios, and the "disallowed interpretations" section shows methodological discipline.

### 4. Appropriate Simplification

The reduction from 30 seeds × 1 map to 20 seeds × 3 maps is a smart trade-off. Cross-map generalization is indeed more scientifically valuable than excessive within-map seed blocking, especially given the acknowledged limitations of MIC effectiveness beyond early rounds.

### 5. Human Evaluation as Primary Outcome

Upgrading human evaluation from "optional" to "primary outcome" is the right decision. The discrimination task (Task 2) is particularly valuable—if humans cannot distinguish C4 from C1 behaviors, the practical significance of any statistical effects becomes questionable.

---

## Major Concerns

### 1. The Theoretical Defense Remains Insufficient

While Section 2.3 is an improvement, it still doesn't adequately address the core validity problem.

**The Issue**: The authors argue that Space Syntax metrics are "abstract topological measures" that can be conveyed through language. But this misses the point. Space Syntax theory was developed to explain how *physical spatial configuration* shapes *embodied human movement and encounter patterns*. The causal mechanism involves:
- Visual fields and sightlines
- Physical effort of navigation
- Probabilistic encounter rates based on actual movement
- Accumulated spatial experience over time

When you tell an LLM "this location has mean depth 1.8," you're not activating these mechanisms—you're testing whether the model has learned linguistic associations between spatial descriptors and behavioral scripts.

**Why This Matters**: If the study finds positive results, the interpretation is ambiguous:
- Did the LLM engage in spatial reasoning?
- Or did it pattern-match "deep location" → "private behavior" from training data?

The current plan doesn't distinguish between these interpretations, yet they have very different implications for the contribution's significance.

**Recommendation**: 
- Add a "spatial reasoning" task that tests whether the model can make novel inferences from spatial descriptions (not just reproduce training data associations)
- Include a condition where spatial descriptions are *correct but counter-stereotypical* (e.g., a high-integration location described as suitable for private conversations) to test whether the model follows structure or stereotypes
- Discuss this limitation more prominently in the framing

### 2. C2 Is Still Problematic (Though Improved)

The authors now honestly acknowledge that C2 is a "behavioral affordance baseline" rather than a "non-spatial control," and they've added C2b. This is better, but the fundamental problem remains.

**The Issue**: The comparison C6m vs C2 is framed as "structural information vs direct behavioral cues," but this creates a false dichotomy. In real environments:
- Structural properties *generate* affordances
- Affordances *reflect* structural properties
- They're not independent dimensions

**Example**: "This space encourages quiet conversation" (C2) is not "non-structural"—it's a phenomenological description of what high-depth, low-integration spaces typically afford. You've just moved the spatial information from explicit to implicit.

**The Real Question**: Are you testing whether *explicit structural descriptions* work better than *implicit phenomenological descriptions*? If so, that's a valid (but different) research question about representation format, not about spatial vs non-spatial information.

**Recommendation**:
- Reframe the C2 comparison as testing "explicit structural format vs implicit phenomenological format"
- Acknowledge that both conditions contain spatial information, just encoded differently
- Consider adding a true non-spatial control: descriptions of temporal patterns ("this location is usually busy in the morning") or social norms ("people here tend to be formal")

### 3. The Expected Effect Sizes May Be Too Small to Matter

The plan targets d ≥ 0.5 effects, which is reasonable for statistical purposes. But is this practically meaningful?

**Context**: In real game design or social simulation:
- Developers already use semantic tags ("tavern," "throne room," "dungeon")
- These tags implicitly carry spatial-behavioral associations
- The question is whether *adding explicit Space Syntax metrics* provides meaningful value over existing practices

**The Issue**: If C4 outperforms C1 by d = 0.5, but humans can barely distinguish the behaviors (Task 2), and the effect is model-specific (Qwen vs Llama differ), then what's the practical takeaway?

**Recommendation**:
- Add a "practical significance threshold" beyond statistical significance
- Define what effect size would justify the added complexity of computing and representing Space Syntax metrics
- Consider a cost-benefit framing: does the improvement justify the implementation effort?

### 4. The Three-Map Design May Not Provide Sufficient Generalization Evidence

The plan uses Plaza, Labyrinth, and Bridge—three maps with different structural profiles. This is good, but:

**The Issue**: 
- All three maps are still *designed* environments with clear structural logic
- Real game worlds often have irregular, evolved, or procedurally generated layouts
- The maps are small (20 nodes implied)—real game worlds have hundreds of locations

**Risk**: The effects might only appear in small, well-structured graphs where spatial metrics are highly differentiated. In larger, messier environments, the signal might disappear.

**Recommendation**:
- Include at least one "irregular" or "procedurally generated" map in Stage 2
- Report the distribution of spatial metrics for each map (are they actually differentiated enough to test the hypotheses?)
- Discuss the generalization limits explicitly

### 5. The Model Selection Strategy Has Unresolved Issues

The plan uses Qwen3.5-Plus as the primary model with Llama 3.3 70B for robustness. But:

**Issue 1**: Qwen is trained primarily on Chinese text. Space Syntax research is predominantly English/Western. The cross-cultural validity of spatial-behavioral associations is unknown.

**Issue 2**: The robustness subset is small (10 seeds × 3 maps × 3 conditions = 90 runs). If Qwen and Llama show different patterns, you won't have enough power to characterize the difference.

**Issue 3**: Both models are open-source. While this aids reproducibility, it also means they may have similar training data sources and biases. A truly independent check would include a closed-source model (GPT, Claude, Gemini).

**Recommendation**:
- Expand the robustness subset to 15-20 seeds
- Add at least one closed-source model to the robustness check (even if only on a subset of conditions)
- Pre-register what you'll conclude if models disagree (currently unclear)

### 6. The Human Evaluation Design Needs More Detail

The plan says "50 participants" for human evaluation, but doesn't specify:
- Recruitment method (crowdsourcing? lab study?)
- Participant expertise (gamers? non-gamers? spatial cognition experts?)
- Evaluation materials (how many behavior samples per participant?)
- Statistical power for the discrimination task

**Issue**: If the discrimination task is underpowered, you might conclude "humans can't distinguish" when actually the task design was too noisy.

**Recommendation**:
- Specify recruitment method and participant criteria
- Run a power analysis for the discrimination task
- Consider a within-subjects design where each participant sees multiple C1/C4 pairs

---

## Minor Concerns

### 7. H3 (Control Value) Is Likely Unviable

The plan acknowledges that high-Control nodes may be rare, but doesn't provide a clear decision rule. If only 2-3 nodes have meaningful Control values, the location-level Spearman correlation will be unreliable.

**Recommendation**: 
- Pre-register a minimum threshold (e.g., "H3 only tested if ≥ 5 nodes with Control ≥ 1.5")
- If threshold not met, drop H3 entirely rather than reporting weak/noisy results

### 8. The Time Dynamics Analysis Is Underspecified

The plan mentions "0-50, 51-100, 101-200+" time windows but doesn't specify:
- What pattern would support "spatial priming"?
- What pattern would support "sustained guidance"?
- How to distinguish "effect decay" from "effect absorption into memory"?

**Recommendation**: Pre-register specific predictions for temporal patterns.

### 9. The MIC Validity Check May Be Circular

The plan proposes checking MIC effectiveness by comparing matched vs unmatched condition differences. But:
- If MIC is effective, matched conditions should have lower variance
- But you're using MIC in the main analysis
- So you're using the data to validate the method you're applying to that same data

**Recommendation**: Use a separate pilot dataset for the MIC validity check, or use a holdout subset.

### 10. The Budget Seems Optimistic

The plan estimates ¥5,000-6,000 total, with API costs around ¥1,200-1,500. But:
- 300 runs × 250 rounds × 10 agents = 750,000 agent turns
- Even at ¥0.001 per turn, that's ¥750
- Plus Judge calls, plus robustness subset, plus pilots
- Human evaluation (50 participants × ¥30) = ¥1,500 alone

The budget may be underestimated by 50-100%.

**Recommendation**: Rerun the budget calculation with conservative assumptions and add a larger buffer.

---

## Missing Elements

### 11. No Discussion of Failure Modes

The result-to-claim matrix covers different result patterns, but doesn't discuss:
- What if the effects are highly variable across seeds?
- What if the effects only appear for certain agent personality types?
- What if the effects are present but very small (d = 0.2-0.3)?

**Recommendation**: Add a "failure modes and contingencies" section.

### 12. No Comparison to Existing Spatial Agent Work

The plan doesn't position this work relative to:
- Embodied AI research on spatial navigation
- Game AI research on spatial reasoning
- Existing LLM spatial reasoning benchmarks

**Recommendation**: Add a "related work" section that clarifies how this differs from and builds on prior work.

### 13. No Data/Code Sharing Plan

The plan emphasizes reproducibility but doesn't specify:
- Will the code be released?
- Will the generated behavior data be released?
- Will the prompts be released?

**Recommendation**: Commit to open science practices explicitly.

---

## Verdict and Path Forward

This is a much-improved plan that addresses many prior concerns. The single focused contribution, honest theoretical positioning, pre-registered interpretation logic, and upgraded human evaluation are all strengths.

However, three fundamental issues remain:

1. **Theoretical Validity**: The text-based approach may test linguistic associations rather than spatial reasoning, and the plan doesn't adequately distinguish these interpretations.

2. **Practical Significance**: Even if statistically significant, the effects may be too small or model-specific to justify the added complexity in real applications.

3. **Generalization**: The three-map design is better than one map, but may not provide sufficient evidence for broader claims.

### Recommended Revisions for Strong Accept:

**Critical**:
1. Add a spatial reasoning task that tests novel inferences (not just training data reproduction)
2. Reframe C2 as "implicit vs explicit spatial encoding" rather than "spatial vs non-spatial"
3. Define practical significance thresholds beyond statistical significance
4. Expand robustness subset and add a closed-source model

**Important**:
5. Add an irregular/procedural map to test generalization
6. Specify human evaluation details (recruitment, power analysis)
7. Pre-register temporal dynamics predictions
8. Add related work positioning

If these revisions are made, this could be a solid AAMAS paper. Without them, it's a borderline accept—methodologically sound but with limited theoretical clarity and uncertain practical impact.

---

## Final Recommendation

**Weak Accept (6/10)**

The plan is executable and addresses prior feedback, but fundamental validity and significance questions remain. With revisions, this could become a strong contribution. As-is, it's acceptable but not compelling.

**Confidence**: High (I am confident in this assessment)

**Expertise**: High (I have published on LLM agents, spatial reasoning, and multi-agent simulation)
