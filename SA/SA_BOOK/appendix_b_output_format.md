# Appendix B — S Output Format

---

This appendix provides the standard template for recording a Strip analysis. Every application of S to an expression should produce a document in this format, ensuring consistency across analysts and enabling verification.

---

## Standard Output Template

```
═══════════════════════════════════════════════════════
STRIP ANALYSIS — S OUTPUT
═══════════════════════════════════════════════════════

EXPRESSION:
  Source text:       [Original expression in original language]
  Translation:       [If applicable]
  Author/Source:     [Who produced this expression]
  Domain:            [Physics / Poetry / Scripture / etc.]
  Date:              [When produced, if known]

───────────────────────────────────────────────────────
PROCEDURE LOG
───────────────────────────────────────────────────────

Step 1 — Decomposition:
  Functional tokens:  [List decomposed tokens]
  Subject:            [Who/what acts]
  Operation:          [What action/relation]
  Object/Scope:       [What is acted upon]

Step 2a — Algebraic Mapping:
  [Token 1] → [Variable] — [reasoning]
  [Token 2] → [Variable] — [reasoning]
  [Token 3] → [Variable] — [reasoning]
  ...

Step 2b — Etymological Strip:
  [Token 1]:
    Root:             [Latin/Greek/Sanskrit/PIE root]
    Structural meaning: [What the root means across traditions]
    Cultural divergence: [If cultural meaning ≠ root meaning, note here]
    Mapping confirmed / CORRECTED: [Did 2a survive 2b?]
  [Token 2]:
    ...

Step 3 — Domain Strip:
  Residual domain terms removed: [List]
  Remaining algebraic expression: [Formula after full strip]

Step 4 — Formulation:
  Algebraic formula:  [The stripped structural content]

Step 5 — Structural Completion:
  Implied consequences:
    - [Consequence 1]
    - [Consequence 2]
    - ...

Step 6 — Universality Test:
  Domain 1: [Name] — [Does formula hold? Y/N] — [Brief justification]
  Domain 2: [Name] — [Does formula hold? Y/N] — [Brief justification]
  Domain 3: [Name] — [Does formula hold? Y/N] — [Brief justification]
  Result: PASSES / FAILS

Step 7 — Classification:
  Invariant match:    [ι₁ / ι₂ / ... / ι₁₀ / candidate / ∅]

───────────────────────────────────────────────────────
7-LAYER OUTPUT
───────────────────────────────────────────────────────

Layer 1 — Invariant (I):
  I = [Iₙ or ∅]
  If Iₙ:             [Which invariant, with formula]

Layer 2 — Emergent Function (𝔉):
  𝔉_d  =             [Declared function]
  𝔉_eff =            [Effective function]
  Δ     =            [Gap: 0 / non-zero / critical]

Layer 3 — Vector (v):
  v_d   =            [Declared direction]
  v_eff =            [Effective direction]
  λ_L     =            [< 0 / ≈ 0 / > 0]

Layer 4 — Source Signature (Σ_src):
  Position:           [Direct / Intermediary / Derivative]
  Coherence:          [High / Medium / Low]
  Authority:          [Structural / Role-based]
  Consciousness:      [High (1.0) / Medium (0.7) / Low (0.3) / Zero (0.0)]

Layer 5 — Relational Field (R):
  R =                 [Mutual (1.0) / Unilateral (0.7) / Projected (0.4) /
                       Instrumental (0.2) / Performative (0.1) / Absent (0.0)]
  Apparent receiver:  [Who the expression is addressed to]
  Structural receiver: [Who the expression actually operates on]

Layer 6 — Temporal Phase (τ_ph):
  τ_ph =                 [Ascending / Descending / Bifurcation / Cyclic / Indeterminate]
  Note:               τ_ph refers to the phase of the CONTENT, not the source.
  Derivation markers:
    Δ≈0 + λ_L<0 + R_mutual          → ascending
    Δ growing + λ_L>0 + R degrading → descending
    λ_L≈0 + Δ unstable               → bifurcation
    Recurrence without evolution  → cyclic
    Markers ambiguous             → indeterminate (note ambiguity)

Layer 7 — Diagnostic Synthesis (Δ_𝔉):
  Classification:     [Type 1-9b — see Chapter 6, §6.4]
  κ (coherence):      [Computed via:
                       κ = (w₁·δ_I + w₂·(1-|Δ_𝔉|) + w₃·align(v) + w₄·r + w₅·c_src) / Σwᵢ
                       Default weights: w₁=3, w₂=2, w₃=2, w₄=1.5, w₅=1.5
                       Components:
                         δ_I    = 1 if ι≠∅, 0 otherwise
                         |Δ_𝔉|    = normalised gap [𝔉_d vs 𝔉_eff]
                         align  = directional alignment [v_d vs v_eff]
                         r      = R numerical value (see Layer 5)
                         c_src  = consciousness numerical value (see Layer 4)]
  Indication:         [Brief structural recommendation]

───────────────────────────────────────────────────────
NOTES
───────────────────────────────────────────────────────

  [Any additional observations, mimicry detection,
   relationship to other invariants, open questions]

═══════════════════════════════════════════════════════
Analyst:             [Name / ID]
Date of analysis:    [Date]
Method version:      [SA v1.0]
═══════════════════════════════════════════════════════
```

---

## Usage Notes

1. **Step 2b is mandatory**. Every analysis must include the etymological strip. If the analyst skips Step 2b, the analysis is incomplete and unreliable.

2. **The Procedure Log must be preserved**. The 7-layer output alone is not sufficient — the procedure log shows *how* the analyst arrived at the output, enabling verification and error detection.

3. **Multiple analysts**: For high-stakes analyses, two or more analysts should independently apply S to the same expression and compare outputs. Divergences should be traced to specific steps and resolved.

4. **Superposition**: If the expression contains multiple invariants, list all of them in Layer 1 and note:
   - **9a (cooperative)**: invariants are compatible — note which receivers are likely to activate which invariant
   - **9b (antagonistic)**: invariants are in tension — apply diagnostic protocol: (1) contradiction test, (2) paradox test, (3) controphase test

5. **Type 3 subtypes**: For manipulation classifications, always distinguish:
   - **3a (conscious)**: source is aware of the inversion
   - **3b (unconscious)**: source genuinely believes their declared function. Note the gap between subjective and structural coherence.

6. **"Mimics" field**: If the expression is classified as semantic illusion or manipulation, always identify which invariant it mimics (Section 9.3).

7. **Version control**: As the method evolves, analyses should record the method version used. Future versions may add steps, refine classifications, or modify the invariant library.
