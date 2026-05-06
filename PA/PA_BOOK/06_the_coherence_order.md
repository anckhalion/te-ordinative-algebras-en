# Chapter 6 — The Coherence Order ≤_κ

---

## 6.1 Why Order Matters

The Proportional Space has been defined (Chapter 4) and metrised (Chapter 5). But a space with a metric and no ordering is a landscape with distances but no heights — you can tell how far apart two points are, but not which is above the other.

The coherence order ≤_κ provides the heights. It answers the question: **of two expressions, which is more coherent?** Not more complex, not more beautiful, not more useful — more *coherent*. Coherence, in the PA, has a precise meaning: the degree to which the proportional relations within an expression are internally consistent and aligned with the coherent content that generated them.

This is not a value judgement. It is a structural diagnosis. A crystal is more coherent than a pile of sand. A sonnet is more coherent than a randomly shuffled sequence of the same words. A successful chemical synthesis is more coherent than a failed one. In each case, the proportional relations between the components are either preserved (coherent) or disrupted (incoherent).

---

## 6.2 The κ Function

The coherence of an expression is measured by the function κ, already developed in the Semantic Algebra and now formalised within the Proportional Space.

> **Definition 6.1 (Coherence Function).** The coherence of an expression E ∈ 𝒟 is:
>
> $$\kappa(E) = \sum_{i=1}^{5} w_i \cdot \kappa_i(E), \quad \kappa(E) \in [0, 1]$$

The five components are:

### Component 1: Internal Proportional Consistency (κ_1)

Do the proportional relations within the expression contradict each other?

A water molecule has bond angles of 104.5° — the hydrogen-oxygen-hydrogen relations are internally consistent. A hypothetical molecule with the same atoms but bond angles of 180° would be internally inconsistent (and indeed does not exist stably). κ_1 measures this: the degree to which the proportional relations within E are mutually compatible.

$$\kappa_1(E) = 1 - \frac{\text{number of internal contradictions}}{\text{total number of internal relations}}$$

### Component 2: Alignment with the Coherent Source (κ_2)

How faithfully does the expression carry the content that generated it?

A faithful translation of a poem preserves the proportional relations of the original (the rhythmic structure, the imagery, the semantic direction). A poor translation destroys them. κ_2 measures the fidelity of the collapse — how much of C survived the transition to E.

$$\kappa_2(E) = \rho(C_E, I_E)$$

where C_E is the coherent content that generated E and I_E is the structural content extractable from E via the Strip operator S. This is the first half of the extended round-trip (§3.5).

### Component 3: Proportional Depth Preserved (κ_3)

How much of the content's proportional complexity survived the collapse?

A photograph captures the two-dimensional proportional relations of a scene but loses the three-dimensional depth. A hologram captures more. κ_3 measures how much of the content's structural depth — the number of proportional levels — is preserved in the expression.

$$\kappa_3(E) = \frac{d(S(E))}{d(C_E)}$$

If the Strip recovers all the structural depth of the original content, κ_3 = 1. If it recovers less, κ_3 < 1.

### Component 4: Stability Under Perturbation (κ_4)

Does the expression maintain its proportional structure when slightly perturbed?

A stable molecule remains a molecule when the temperature fluctuates slightly. An unstable compound decomposes. A coherent argument survives minor objections; an incoherent one collapses under the first challenge. κ_4 measures structural resilience — the expression's resistance to small perturbations.

$$\kappa_4(E) = 1 - \frac{\Delta\kappa}{\Delta\epsilon}\bigg|_{\epsilon \to 0}$$

where ε is a small perturbation and Δκ is the resulting change in coherence. If the coherence is insensitive to perturbation (Δκ/Δε ≈ 0), the expression is stable: κ_4 ≈ 1. If it is highly sensitive, κ_4 → 0.

This connects directly to the OST's classification of system responses to stress (§4.2): elastic, plastic, fracture.

### Component 5: Generative Capacity (κ_5)

Can the expression serve as a source for further collapses?

A fertile expression — a great theorem, a foundational experiment, a seminal artwork — generates further expressions. It becomes a singularity at the next level (§3.8). A sterile expression — a trivial tautology, a dead-end experiment — generates nothing. κ_5 measures the expression's capacity to function as C for future collapses.

$$\kappa_5(E) = |\{E' \in \mathcal{D} : E \in \mathcal{C}_{E'}\}| / N_{max}$$

where the numerator is the number of further expressions for which E serves as (part of) the coherent content, and N_max normalises.

---

## 6.3 The Coherence Order

Given the κ function, the coherence order is defined:

> **Definition 6.2 (Coherence Order).** For E₁, E₂ ∈ 𝒟:
>
> $$E_1 \leq_\kappa E_2 \iff \kappa(E_1) \leq \kappa(E_2)$$

### Properties

**Reflexive**: E ≤_κ E (every expression is as coherent as itself). ✅

**Antisymmetric**: if E₁ ≤_κ E₂ and E₂ ≤_κ E₁, then κ(E₁) = κ(E₂). ✅

**Transitive**: if E₁ ≤_κ E₂ and E₂ ≤_κ E₃, then E₁ ≤_κ E₃. ✅

Therefore ≤_κ is a **partial order** on 𝒟.

**Why partial, not total?** Because not all expressions are comparable. A symphony and a molecule both have coherence values, but comparing them directly is meaningless — they exist in different fibres of 𝒫 (different identity-context combinations). The order is well-defined *within* a fibre (within a domain, within a class of expressions sharing an invariant) and undefined *between* incomparable fibres.

This is the correct structure. A total order would imply that every expression can be ranked against every other — that Beethoven's Fifth is "more coherent" than penicillin. Such a claim is absurd. The partial order respects the structural boundaries between domains while providing diagnostic power within them.

---

## 6.4 The Lattice of Coherence Classes

The coherence order, combined with the structural equivalence ≡_S, produces a rich structure.

Within each equivalence class [I_k] — the class of all expressions that carry invariant k — the coherence order produces a **lattice**: a partially ordered set in which every pair of elements has a greatest lower bound (infimum) and a least upper bound (supremum).

- The **infimum** of the class is the least coherent expression carrying the invariant — the weakest, most distorted, most noise-laden version of the structural law.
- The **supremum** is the most coherent — the purest, most faithful, most generative expression of the invariant.

For example, in the class of expressions carrying invariant I₁ (the irreducible asymmetry between source and expression — "the map is not the territory"):

- A bumper sticker reading "Don't believe everything you read" carries I₁ but with low κ — shallow, no generative capacity, contextually limited.
- Korzybski's "The map is not the territory" carries I₁ with medium κ — memorable, clear, moderate depth.
- Gödel's Incompleteness Theorems carry I₁ with high κ — maximum depth, maximum generative capacity, maximum stability under perturbation.

These three expressions are structurally equivalent (≡_S) but ordered (≤_κ). They form a chain within the lattice of I₁.

---

## 6.5 κ as Diagnostic

The coherence function κ and the order ≤_κ serve three practical functions:

**1. Quality assessment.** Given two expressions that claim to express the same content, κ tells which one does it better. This is not aesthetic preference; it is structural diagnosis. The expression with higher κ preserves more of the proportional structure.

**2. Degeneration detection.** If a system's expressions show declining κ over time (κ(E_n) < κ(E_{n-1}) < ...), the system is degenerating — it is losing proportional coherence. In OST terms: dΦ/dt < 0.

**3. Evolution tracking.** If a system's expressions show increasing κ over time, the system is evolving — it is integrating more proportional structure. In OST terms: dΦ/dt > 0, with the trajectory approaching a higher coherence attractor.

---

*The space is ordered. Now we examine its internal structure — the identity as an algebraic object.*

---
