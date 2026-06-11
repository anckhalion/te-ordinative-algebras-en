# Chapter 4 — The Proportional Space 𝒫: Formal Definition

---

## 4.1 What a Proportional Space Must Be

Chapter 3 listed the requirements. This chapter delivers the first: a space in which all the objects of the Proportional Algebra can coexist, be compared, and be transformed.

The space must be:
1. **Multi-dimensional** — content, identity, and expression have multiple independent components
2. **Ordered** — some configurations are more coherent than others
3. **Metrised** — compatibility is a measure, not a binary
4. **Dynamic** — the space evolves as collapses occur
5. **Recursively scaled** — what emerges at one level becomes an element at the next (§3.8)

No single existing mathematical structure satisfies all five. The Proportional Space 𝒫 combines elements from several, in a specific way dictated by the ontology of the Technology of Expressions.

---

## 4.2 The Three Regions of 𝒫

The Proportional Space is not homogeneous. It contains three structurally distinct regions:

### Region 1: The Coherent Field (ℭ_h)

The coherent field is the space of *un-collapsed structured potential*. It contains everything that *could* be expressed but has not yet been — every possible molecular configuration, every possible sentence, every possible emotional trajectory.

The coherent field is:
- **Non-enumerable** — its elements cannot be listed (they are a continuum of possibilities)
- **Simultaneously present** — unlike the decoherent region, where elements are sequential, the coherent field is a simultaneous superposition
- **Not directly observable** — by definition, what is coherent has not been collapsed into expression; it can only be accessed through collapse

In the notation of the TE, ℭ_h is the domain of the Collapse Function's first argument: the C in E = Φ(C, I, K).

In the notation of the OST, ℭ_h corresponds to the space of *all possible proportional configurations* that the relational field R could organise.

### Region 2: The Identity Space (𝕀)

The identity space is the space of *Remirs* — the internal structures of identities. Each identity I is characterised by its Remir ℛ(I) = (V_I, B_I), where V_I is the set of semantic vectors that constitute the identity's active structure, and B_I is the resonance matrix between those vectors.

The identity space is:
- **Finite-dimensional for any given identity** — each identity has a finite number of active semantic vectors (though the number can change as the identity evolves)
- **Vectorial** — each Remir is a structured set of oriented vectors, not a point
- **Evolutionary** — identities change over time as they traverse their trajectories; the identity space is therefore parametrised by the trajectory T(I)

In the notation of the OST, 𝕀 corresponds to the space of *singularities* Σ — each identity is an irreducible, non-interchangeable unit with a unique function.

### Region 3: The Decoherent Space (𝒟)

The decoherent space is the space of *expressed realities* — everything that has been collapsed into a visible, audible, measurable form. A molecule, a sentence, a painting, a medical symptom, a temperature reading — all are elements of 𝒟.

The decoherent space is:
- **Observable** — its elements are the data of the sciences
- **Domain-specific** — each element carries a domain vocabulary (chemical, linguistic, emotional)
- **Partially ordered** — some expressions are more coherent than others (the order ≤_𝓚)

In the notation of the OST, 𝒟 corresponds to the space of *emergent functions* Φ — each expression is the result of the ordered interaction of singularities within a relational field.

### The Architecture

The three regions are connected by the operations defined in Chapter 3:

$$\mathfrak{C}_h \xrightarrow{\Phi} \mathcal{D} \xrightarrow{S} \text{Invariants}$$

$$\mathbb{I} \times \mathbb{I} \xrightarrow{\otimes} \mathfrak{C}_{shared}$$

The Collapse Φ maps from the coherent field to the decoherent space. The Strip S maps from the decoherent space back toward the structural core. The Resonance ⊗ generates shared coherent fields from pairs of identities.

---

## 4.3 Formal Definition

We now state the definition precisely.

> **Definition 4.1 (Proportional Space).** The Proportional Space is the ordered quintuple:
>
> $$\mathcal{P} = (\mathfrak{C}_h, \mathbb{I}, \mathcal{D}, \rho, \leq_{\mathcal{K}})$$
>
> where:
> - ℭ_h is the **coherent field** — a topological space of structured potential
> - 𝕀 is the **identity space** — a space of Remirs, each a finite-dimensional vector structure
> - 𝒟 is the **decoherent space** — a partially ordered set of expressed realities
> - ρ: ℭ_h × 𝕀 → [0, 1] is the **resonance metric** — measuring compatibility between content and identity
> - ≤_𝓚 is the **coherence order** — a partial order on 𝒟

The three regions are connected by three operations:

> - **Collapse**: Φ: ℭ_h × 𝕀 × K → 𝒟
> - **Strip**: S: 𝒟 → ℐ × [0, 1] (where ℐ is the space of invariants)
> - **Resonance**: ⊗: 𝕀 × 𝕀 → ℭ_shared ⊆ ℭ_h

And three relations:

> - **Coherence order**: E₁ ≤_𝓚 E₂ ⟺ ⟨𝓚⁵⟩(E₁) ≤ ⟨𝓚⁵⟩(E₂) (partial order on 𝒟)
> - **Structural equivalence**: E₁ ≡_S E₂ ⟺ S(E₁) = S(E₂) (equivalence on 𝒟)
> - **Compatibility**: C ∼_ρ I ⟺ ρ(C, I) ≥ θ (tolerance relation on ℭ_h × 𝕀)

This quintuple, with its operations and relations, is the Proportional Algebra.

---

## 4.4 Properties of 𝒫

### 4.4.1 𝒫 Is Not a Vector Space

A vector space requires closure under addition and scalar multiplication. 𝒫 does not have these: you cannot "add" two expressions and get another expression. The collapse of a Rilke poem and the collapse of a water molecule do not produce a third object under addition. Composition in 𝒫 is governed by Φ and ⊗, not by linear operations.

### 4.4.2 𝒫 Is Not a Metric Space (Globally)

A metric space requires a distance function d(x, y) defined for all pairs. The resonance function ρ(C, I) is defined only between the coherent field and the identity space — not between two expressions, or between two identities in general. ρ is a *local* metric, not a global one. Within the decoherent space, the ordering is given by ≤_𝓚, which is a partial order, not a distance.

### 4.4.3 𝒫 Is a Fibred Space

The closest mathematical analogy is a **fibre bundle** — a space in which the total space is partitioned into fibres, each fibre being a local space with its own structure.

In 𝒫:
- The **base space** is the coherent field ℭ_h
- The **fibres** are the identity-indexed collapses: for each identity I and context K, the fibre is the set of all expressions E that I can collapse from ℭ_h in context K
- The **projection** is the Strip operator S, which maps from the total space (expressions) back to the base (invariants)

This is not merely an analogy. The fibre bundle structure captures precisely what the PA requires: that the same coherent content can be "seen" differently by different identities (different fibres), and that the Strip operator collapses the fibre structure back to the base (the invariant).

### 4.4.4 𝒫 Is Dynamic

The space is parametrised by the trajectories of its identities. As an identity I traverses its trajectory T(I) = {E₁, E₂, ..., Eₙ}, the identity-update operator 𝒰 (TE equation 16.5) transforms I into I':

$$I_{n+1} = \mathcal{U}(I_n, E_n)$$

This changes the Remir ℛ(I), which changes the resonance ρ(C, I), which changes the set of collapsible contents, which changes the fibre. The space evolves as its inhabitants evolve.

### 4.4.5 𝒫 Is Recursively Scaled

Per §3.8, the space is self-similar across scales. An emergent function Φ at level N becomes a singularity σ* at level N+1. In PA terms: an expression E ∈ 𝒟_N can be "promoted" to an element of ℭ_h_{N+1} — it becomes a structured potential at a higher level of organisation.

The promotion must satisfy the vertical coherence constraint:

$$\rho_{N+1}(E_{promoted}, I_{N+1}) \leq_{\mathcal{K}} \rho_N(C_N, I_N)$$

The proportional relations at the lower level are *inherited*, not replaced.

---

## 4.5 The Context Operator K

Context has appeared repeatedly in the Collapse Function but has not been formally treated. In the Proportional Space, context is an operator on the fibre structure:

> **Definition 4.2 (Context).** A context K is a constraint on the coherent field that restricts the set of collapsible contents for a given identity:
>
> $$K: \mathfrak{C}_h \to \mathfrak{C}_K \subseteq \mathfrak{C}_h$$
>
> The Collapse Function then operates on the restricted field:
>
> $$E = \Phi(C_K, I, K) \quad \text{where } C_K = K(\mathfrak{C}_h)$$

Context is not a passive container. It is an **active filter** that determines which proportional relations are available for collapse. The same identity, resonating with the same coherent content, in a different context, collapses a different expression.

Examples:
- In chemistry, K is the set of physical conditions (temperature, pressure, solvent) — they determine which molecular configurations are accessible
- In language, K is the communicative situation (audience, medium, genre) — it determines which meanings can be expressed
- In music, K is the instrument, the room, the audience — it determines which tonal relations can be realised

Context is why the Proportional Space is not a single fixed landscape. It is a **family of landscapes**, indexed by context. Each context K defines a different slice through ℭ_h, and therefore a different set of possible expressions.

---

## 4.6 Summary

| Component | Symbol | Role in 𝒫 | OST Correspondent |
|---|---|---|---|
| Coherent field | ℭ_h | Space of structured potential | All possible configurations of R |
| Identity space | 𝕀 | Space of Remirs | Singularities Σ |
| Decoherent space | 𝒟 | Space of expressed realities | Emergent functions Φ |
| Resonance metric | ρ | Measures compatibility C ↔ I | Intensity of R |
| Coherence order | ≤_𝓚 | Ranks expressions by coherence | Quality of Φ |
| Context | K | Constrains the accessible field | Boundary conditions of ⟨Σ, R, Φ⟩ |

The Proportional Space is defined. It has three regions, a local metric, a partial order, a context operator, dynamic evolution, and recursive scaling. It is the ground on which the operations and relations of Chapters 5 through 7 will be built.

---

*The space exists. Now we measure it.*

---
