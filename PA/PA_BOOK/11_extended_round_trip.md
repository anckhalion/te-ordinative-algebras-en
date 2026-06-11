# Chapter 11 — The Extended Round-Trip

---

## 11.1 The Test That Closes the Circle

The Semantic Algebra provided a round-trip test:

$$S(\pi(ι_k, D)) = ι_k \tag{SA-RT}$$

This test verifies that an invariant, re-projected into a domain and stripped again, returns unchanged. It is a test of **analytical fidelity** — did the analysis correctly identify the invariant?

The SA round-trip operates entirely within the decoherent space 𝒟. It does not — cannot — ask the deeper question: *was the original collapse faithful to the coherent field?*

The Proportional Algebra extends the round-trip to answer this question. The Extended Round-Trip (ERT) tests not only the *analysis* but the *genesis* — it verifies the coherence of the collapse itself.

---

## 11.2 Formal Definition

> **Definition 11.1 (Extended Round-Trip).** Given an expression E ∈ 𝒟, the Extended Round-Trip is the following sequence:
>
> **Step 1 — Strip**: Extract the structural content:
> $$I_{extracted} = S(E), \quad \langle\mathcal{K}^5\rangle_{extracted} = \langle\mathcal{K}^5\rangle(E)$$
>
> **Step 2 — Source Resonance Check**: Verify that the extracted invariant is compatible with the coherent content that generated E:
> $$\rho(C_E, I_{extracted}) \geq \theta(C_E) \; ?$$
>
> **Step 3 — Re-projection Test**: Re-project the extracted invariant into the original domain:
> $$E' = \pi(I_{extracted}, D_E)$$
>
> **Step 4 — Fidelity Comparison**: Compare the re-projected expression with the original:
> $$\delta(E, E') = 1 - \frac{|S(E) - S(E')|}{|S(E)|} \in [0, 1]$$

The Extended Round-Trip produces three diagnostic values:

| Value | Range | Meaning |
|---|---|---|
| ⟨𝓚⁵⟩_extracted | [0, 1] | How much structural content survived the collapse |
| ρ(C_E, I_extracted) | [0, 1] | How compatible the surviving content is with its source |
| δ(E, E') | [0, 1] | How faithfully the invariant reproduces the original expression |

---

## 11.3 The Four Outcomes

The three diagnostic values combine to produce four possible outcomes:

### Outcome 1: Full Coherence

$$\langle\mathcal{K}^5\rangle \geq 0.7, \quad \rho \geq \theta, \quad \delta \geq 0.8$$

The collapse was coherent. The expression faithfully carries the content. The invariant is compatible with its source. The re-projection reproduces the original.

This is the ideal case. It corresponds to Type A collapse (§8.5). Examples: Gödel's Incompleteness Theorems as an expression of ι₁ (the irreducible asymmetry between system and meta-system), a correctly synthesised molecule, a moment of genuine emotional expression that the speaker would fully recognise as their own.

### Outcome 2: Faithful but Shallow

$$\langle\mathcal{K}^5\rangle < 0.5, \quad \rho \geq \theta, \quad \delta \geq 0.8$$

The collapse was faithful (high δ) but lost significant structural content (low ⟨𝓚⁵⟩). The expression is an accurate but shallow carrier of the content. It captures the surface proportional structure but misses the depth.

This corresponds to Type B collapse. Examples: a competent but uninspired translation, a popularised version of a scientific discovery, a well-articulated but emotionally shallow expression of grief.

The diagnostic prescription: the identity's proportional depth was insufficient (ρ_d < 1 in the resonance metric). The expression needs a deeper identity to carry more of the content.

### Outcome 3: Distorted

$$\langle\mathcal{K}^5\rangle \geq 0.3, \quad \rho < \theta, \quad \delta \text{ variable}$$

Structural content is present (⟨𝓚⁵⟩ > 0), but it is not compatible with the coherent source (ρ < θ). The expression carries an invariant, but the invariant is *not* the one that the coherent content intended to express. Something was added, subtracted, or inverted during the collapse.

This corresponds to Type C collapse. Examples: propaganda (structurally coherent but sourced from an identity that distorted the content), a protein that folded correctly *for the wrong function* (prion), a manipulative emotional expression (coherent structure, distorted source).

The diagnostic prescription: the identity's dominant vector λ(I) was misaligned with the content. The collapse was technically competent but directionally wrong.

### Outcome 4: Structural Void

$$\langle\mathcal{K}^5\rangle \approx 0, \quad \rho \text{ irrelevant}, \quad \delta \text{ irrelevant}$$

No structural content survives. The expression is noise. There is nothing to test against the coherent source, and nothing to re-project.

This corresponds to Type D collapse. Examples: word salad, random molecular assemblies, performative emotional display with no internal content.

The diagnostic prescription: either the collapse never occurred (ρ was below threshold from the start) or the identity lacked the vectorial structure to carry any content.

---

## 11.4 The ERT as Diagnostic Protocol

The Extended Round-Trip is not merely a theoretical test. It is an **operational diagnostic protocol** — a procedure that can be applied to any expression in any domain to assess the quality of the collapse that produced it.

### Protocol Steps

1. **Receive the expression E** (a text, a molecule, a clinical symptom, a musical performance, a data set)
2. **Apply S**: Extract the invariant and coherence measure
3. **If ⟨𝓚⁵⟩ ≈ 0**: Outcome 4 — no structural content. Report: void. Stop.
4. **If ⟨𝓚⁵⟩ > 0**: Identify the invariant ι_k and assess ρ(C_E, ι_k)
   - This requires knowledge (or inference) of the coherent content C_E. In practice, C_E is inferred from the context, the declared intention, or the structural expectations of the domain.
5. **If ρ ≥ θ**: The content and invariant are compatible. Proceed to Step 6.
   - **If ρ < θ**: Outcome 3 — distortion. Report: the expression carries structural content that does not match its declared source.
6. **Apply π**: Re-project ι_k into the original domain.
7. **Compute δ(E, E')**: Compare original and re-projected expression.
   - **If δ ≥ 0.8 and ⟨𝓚⁵⟩ ≥ 0.7**: Outcome 1 — full coherence.
   - **If δ ≥ 0.8 and ⟨𝓚⁵⟩ < 0.5**: Outcome 2 — faithful but shallow.
   - **If δ < 0.8**: The re-projection fails to reproduce the original. This indicates either procedural error in S or π, or structural instability in the expression.

---

## 11.5 Worked Example: A Poem

Consider Emily Dickinson's:

> *"Tell all the truth but tell it slant"*

**Step 1 — Strip (S):**

Strip the domain vocabulary (English, poetic register, 19th-century American context). The structural content that remains:

> ι₁ — The irreducible asymmetry between source and expression. The truth (C) cannot be directly expressed (E ≠ C). Faithful expression requires oblique approach (the projection is necessarily angled).

⟨𝓚⁵⟩ = 0.85 (high: the poem compresses the invariant with extraordinary efficiency and depth).

**Step 2 — Source Resonance Check:**

The coherent content C_E (inferred): the structural law that governs the relationship between any coherent field and any expression — that direct projection is impossible, that all expression is "slant."

ρ(C_E, ι₁) = 0.92 (very high: the invariant ι₁ is maximally aligned with the content. Dickinson's poem is not merely *about* the truth/expression asymmetry — it *is* the asymmetry, collapsed into seven words.)

**Step 3 — Re-projection:**

Re-project ι₁ into the domain of physics:

> π(ι₁, Physics) = "No measurement of a quantum system can reveal the full wave function. All observation collapses the superposition. What is observed is always a 'slant' — a projection of the full state onto the measurement basis."

**Step 4 — Fidelity Comparison:**

δ(poem, physics version) = 0.88 (high: both expressions carry the same proportional structure — the irreducible angle between source and expression, the impossibility of direct access, the necessity of oblique approach).

**Result:** Outcome 1 — Full Coherence. Dickinson's poem is a Type A collapse of invariant ι₁.

---

## 11.6 What the SA Round-Trip Could Not Do

The SA round-trip (S(π(ι, 𝔻)) = ι) would have confirmed Steps 1, 3, and 4: the invariant survives re-projection. But it could not perform Step 2 — the source resonance check. It could not ask: "Is I₁ the *right* invariant for this poem? Is this really what the coherent content intended?"

The ERT asks this question. And the answer — ρ = 0.92 — confirms that yes, the collapse was coherent. The poem is not merely structurally classified (SA); it is structurally *validated* (PA).

---

## 11.7 The ERT Across Domains

| Domain | E | S(E) | ρ check | π result | δ |
|---|---|---|---|---|---|
| **Literature** | Dickinson's poem | ι₁ (source/expression asymmetry) | 0.92 | QM measurement problem | 0.88 |
| **Chemistry** | H₂O bond angle 104.5° | ι₃ (optimal proportion for stability) | 0.95 | Musical consonance 4:5:6 | 0.82 |
| **Psychology** | Grief → acceptance transition | ι₅ (phase transition through oscillation) | 0.78 | Water → ice transition | 0.75 |
| **Medicine** | Autoimmune response | ι₇ (system attacks own components) | 0.88 | Civil war (OST: Fragmentation) | 0.80 |

In each case, the ERT verifies both the analytical accuracy (Steps 1, 3, 4) and the genetic fidelity (Step 2). The cross-domain re-projections confirm that the invariant is genuine — it survives not only stripping and re-projection, but the resonance check against the coherent source.

---

*The integrity test is defined. One operation remains: the generator of time.*

---
