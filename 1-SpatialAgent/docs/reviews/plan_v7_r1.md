# Review of "Where You Are Shapes Who You Become: Space Syntax-Informed LLM Agents for Spatially Believable Game Worlds"

**Reviewer**: Expert Reviewer  
**Date**: 2026-04-01  
**Plan Version**: v7.0  
**Recommendation**: Major Revision

---

## Overall Assessment

This is an ambitious and well-structured research plan that attempts to bridge Space Syntax theory with LLM agent behavior. The v7 revision shows substantial improvement in addressing prior concerns about experimental design, particularly the separation of movement and perception effects. However, several fundamental issues remain that could limit the contribution's impact.

---

## Strengths

### 1. Excellent Methodological Transparency
The explicit `TAR_run` protocol (Section 3.4) using Spearman correlation + Fisher z-transformation is a significant improvement. This operationalization is clear and reproducible.

### 2. Smart Experimental Decomposition
The separation of C6m (matched movement) vs C6f (free movement) vs C4 (full system) elegantly isolates perception, movement, and sampling contributions. This addresses a critical confound in v6.

### 3. Honest About Limitations
The plan appropriately frames RQ4 as exploratory, acknowledges the "three theoretical leaps," and doesn't overclaim. The matched initial conditions (MIC) framing is more honest than "matched seeds."

### 4. Cost-Effective Design
The open-source model strategy (Qwen3.5-Plus) with third-party API pricing makes this financially feasible while maintaining reproducibility.

### 5. Comprehensive Risk Mitigation
The reverse-inference audit for C2, coding reliability protocol, and multiple robustness checks show careful planning.

---

## Major Concerns

### 1. Fundamental Validity: Can Text Truly Capture Spatial Structure?

The plan acknowledges "Leap 2" (physical space → textualized space) but doesn't adequately address whether linguistic descriptions can preserve the structural properties that Space Syntax measures in physical environments.

**Issue**: Space Syntax metrics like Integration and Control Value emerge from *embodied navigation* and *visual fields*. When you tell an LLM "this location has mean depth 1.8 steps," you're providing a symbolic abstraction, not the phenomenological experience that drives human spatial behavior.

**Question**: Are you testing Space Syntax theory, or are you testing whether LLMs have learned linguistic associations between spatial descriptors and social behaviors from their training data?

**Recommendation**: 
- Add a theoretical section explicitly defending why textual spatial descriptions should preserve the causal mechanisms Space Syntax proposes
- Consider adding a "spatial reasoning" pre-test where you verify the LLM can make valid inferences from spatial descriptions (beyond the comprehension gate)
- Discuss this limitation more prominently in the paper framing

---

### 2. The C2 Baseline May Be Fundamentally Flawed

The "stable non-spatial affordance" baseline is conceptually problematic.

**Issue**: You're trying to create descriptions that are "actionable" and "stable" but "decoupled from spatial structure." But in real environments, affordances and spatial structure are *intrinsically coupled*. A "relaxing" space is often structurally deep/private; a "bustling" space is often high-integration. The reverse-inference audit may filter out obvious leaks, but subtle correlations will remain.

**More fundamental problem**: Even if C2 descriptions pass the audit, you're comparing:
- C6m: "This location has mean depth 1.8 and connects to 4 neighbors" (structural)
- C2: "This location feels relaxing and encourages quiet conversation" (phenomenological)

These aren't equivalent controls—C2 provides *behavioral priming* while C6m provides *structural information*. A stronger C2 > C1 effect doesn't invalidate C6m; it just means behavioral priming is more direct than structural inference.

**Recommendation**:
- Reframe C2 as "behavioral affordance baseline" rather than "non-spatial control"
- Add a C2b condition: structural descriptions of *non-spatial* features (e.g., "This room has 3 windows, 2 doors, wooden floors") to test whether structural description format itself matters
- Acknowledge that C6m > C2 may reflect "indirect vs direct behavioral cueing" rather than "spatial vs non-spatial"

---

### 3. Exp1C Doesn't Test What You Think It Tests

The 2×2 design (structural profile × semantic label) is interesting but the interpretation is overclaimed.

**Issue**: You've renamed the factor to "composite structural profile" (public-structural vs private-structural), which is honest, but this means:
- You're not testing H1 or H2 independently
- You're testing whether a *bundle* of correlated features (high Integration + shallow depth + public semantics) produces different behavior than the opposite bundle
- The interaction term tells you about conflict resolution, but not about the independent causal role of Integration or Depth

**This is a manipulation check, not a hypothesis test.**

**Recommendation**:
- Move Exp1C to supplementary materials or frame it explicitly as "proof of concept that agents respond to spatial descriptions"
- Don't use Exp1C results to support H1 or H2 claims
- If you want to test H1/H2 independently, you need orthogonal manipulations (high Integration + high Depth vs high Integration + low Depth, etc.), which requires more complex scenarios

---

### 4. Statistical Power Is Overstated

You claim minimum detectable effect size d ≥ 0.74 with 30 MIC seeds, but this assumes:
- True independence between seeds (questionable given only 10 NPCs and 20 locations)
- No multiple comparisons penalty beyond FDR (but you have 5 conditions, 3 hypotheses, multiple time windows)
- Stable variance across conditions (but C4 with sampling may have higher variance than C1)

**Issue**: With only 30 seeds and 5-way comparisons, your actual power for detecting d = 0.5 effects is likely much lower than implied. The "we only claim to detect medium-to-large effects" framing is reasonable, but then why run 30 seeds if you're not trying to detect smaller effects?

**Recommendation**:
- Run a proper power simulation using pilot data variance estimates
- Report sensitivity analyses: what's the minimum effect size detectable at 80% power given your actual design?
- Consider whether 30 seeds is overkill for d ≥ 0.7 or underpowered for d ≈ 0.5

---

### 5. Model Selection Justification Is Weak

You've chosen Qwen3.5-Plus primarily for cost and reproducibility, which is pragmatic, but:

**Issue**: 
- Qwen models are trained primarily on Chinese text with English as secondary. Space Syntax theory and research are predominantly English/Western. This could affect how well the model has internalized spatial-social associations.
- The "comprehension ≥85%" gate tests explicit understanding, not implicit spatial reasoning
- Using the same model for Actor and Judge creates systematic bias that Rule-Based Scorer and DeepSeek robustness checks may not fully address

**Recommendation**:
- Add a cross-lingual analysis: does the effect size differ between English and Chinese scenario descriptions?
- Expand robustness subset to include at least one Western-trained model (e.g., Llama 3.3 70B, which is also open-source and cheap)
- Report model-specific effects prominently, not just as robustness checks

---

### 6. The "Matched Initial Conditions" Design Has Limited Value

You've correctly downgraded the claim from "matched seeds" to "MIC," but I'm still skeptical of the value.

**Issue**: 
- You acknowledge MIC effectiveness likely decays after ~50 rounds
- Your main analysis uses 200-300 rounds
- The ICC(seed) analysis will likely show minimal blocking effect after early windows
- You're spending significant complexity (30 seeds × 5 conditions = 150 runs) for a design feature that may only matter in the first 25% of data

**Alternative**: Run fewer seeds (15-20) but add more scenarios/maps. Between-scenario variance is scientifically more interesting than between-seed variance.

**Recommendation**:
- Reduce to 20 MIC seeds and add 2 more maps to Stage 2 (not just Stage 3)
- Focus power on cross-map generalization rather than within-map seed blocking
- Report MIC as a "variance reduction technique" but don't make it a methodological contribution

---

## Minor Concerns

### 7. H3 (Control Value) Is Likely Underpowered

You acknowledge high-Control nodes may be rare, but then don't adjust the design. If only 3-5 nodes have meaningful Control values, your location-level Spearman correlation will be dominated by noise.

**Recommendation**: 
- Pre-register a minimum threshold (e.g., "H3 only tested if ≥5 nodes with Control ≥ 1.5")
- Consider a binary high/low Control comparison instead of continuous correlation
- Or drop H3 from confirmatory analysis entirely

---

### 8. Time Dynamics Are Undertheorized

The "spatial priming vs sustained guidance" distinction is interesting but underdeveloped.

**Issue**: You'll likely find effects decay over time as memory accumulates, but you don't have a theoretical framework for *why* or *when* this should happen. Is it:
- Agents learning the space and no longer needing descriptions?
- Memory overwriting spatial cues?
- Social network structure becoming self-reinforcing?

**Recommendation**:
- Add a theoretical section on temporal dynamics
- Pre-register specific predictions (e.g., "H1 effect should be strongest in rounds 1-50, then stabilize at 50% of initial magnitude")

---

### 9. Human Evaluation Is Too Weak

50 participants rating believability is a nice addition, but it's not integrated into the main claims.

**Issue**: If human raters can't distinguish C4 from C1 behaviors, does it matter that TAR is significant? Conversely, if humans prefer C4, that's a stronger validity check than any statistical test.

**Recommendation**:
- Make human evaluation a primary outcome, not an optional add-on
- Use a discrimination task: can humans identify which behaviors came from C4 vs C1?
- Report human-LLM agreement as a validity check for the Judge

---

## Presentation Issues

### 10. The Plan Is Too Long
At 1520 lines, this is more detailed than most papers. Reviewers will struggle to extract the core contribution. The budget section (8.1-8.6) is excessive detail for a research plan.

### 11. Terminology Overload
BSR, TAR, MIC, C1-C7, H1-H3, Exp1A/1C/3-Minimal... The alphabet soup makes it hard to follow. Simplify.

### 12. The Title Oversells
"Where You Are Shapes Who You Become" implies causal developmental effects, but you're testing immediate behavioral responses in 200-round simulations. Consider: "Do Spatial Descriptions Shape LLM Agent Behavior? A Space Syntax-Informed Investigation"

---

## Missing Elements

### 13. No Discussion of Generative Validity
If this works, what does it mean for game design? For social simulation? For LLM architecture? The plan is methodologically rigorous but lacks vision for impact.

### 14. No Comparison to Existing Spatial Agent Work
How does this relate to embodied AI, spatial reasoning benchmarks, or existing game AI? You're treating this as pure Space Syntax validation, but it's also an LLM capabilities study.

### 15. No Code/Data Sharing Plan
You mention reproducibility but don't specify whether you'll release code, prompts, or generated data.

---

## Verdict

This is a well-designed study with clear improvements over v6, but it suffers from:

1. **Theoretical ambiguity** about what's actually being tested (Space Syntax in LLMs vs linguistic associations)
2. **Baseline validity concerns** (C2 may not be a true non-spatial control)
3. **Overcomplicated design** (30 seeds × 5 conditions may be overkill)
4. **Model selection risks** (Qwen may not be ideal for Western spatial theory)

### Path Forward

- Simplify to 20 seeds, 3 core conditions (C1, C2-revised, C4), 3 maps
- Strengthen theoretical justification for text-based Space Syntax
- Make human evaluation primary, not optional
- Reframe as "proof of concept" rather than "validation of Space Syntax"

If executed well, this could be a strong AAMAS paper, but it needs tighter focus and more honest framing of what can actually be concluded from LLM behavior in text-based environments.

---

## Final Recommendation

**Major Revision Required**

The core idea is sound, but the execution needs refinement to match the ambitious theoretical claims.
