# Chapter 9 — S and π: The SA Operators as Special Case of the PA

---

## 9.1 Where We Meet Old Friends

The reader who has already encountered the Semantic Algebra will recognise two operators: **S** (Strip) and **π** (Re-contextualisation). They were introduced in *What Language Hides* as the foundational tools of semantic analysis — the bisturi and the re-projection lens.

This chapter shows that S and π are not independent inventions. They are **special cases** of the Proportional Algebra — the PA operators restricted to the decoherent space 𝒟. The SA, in its entirety, is the PA with the coherent field ℭ_h hidden from view.

This is not a demotion. It is a clarification. The SA remains the most effective operational tool for structural analysis of expressions. What the PA provides is the space in which S and π operate, the metric that explains *why* they work, and the extended round-trip that tests *how well* they work.

---

## 9.2 The Strip Operator S — PA Formalisation

### 9.2.1 SA Definition (Review)

In the Semantic Algebra, the Strip operator was defined procedurally:

> *Given an expression E, strip away the domain-specific vocabulary (Layer 1-4 of the 7-layer architecture), and extract the structural content — the invariant — that remains.*

The output is a classified invariant ι_k with a coherence measure ⟨𝓚⁵⟩ and a type classification (Types 1-11).

### 9.2.2 PA Definition

In the Proportional Algebra, S is formalised as a projection:

> **Definition 9.1 (Strip Operator).** The Strip is a mapping:
>
> $$S: \mathcal{D} \to \mathcal{I} \times [0, 1]$$
>
> where ℐ is the space of structural invariants and [0, 1] is the coherence measure ⟨𝓚⁵⟩.
>
> S takes an expression E ∈ 𝒟 and produces a pair (ι_k, ⟨𝓚⁵⟩) — the invariant and its coherence.

In fibre-bundle terms (§4.4.3): S is the **projection from the total space to the base space**. The total space is the decoherent space 𝒟 (all expressions, in all domains, carrying all invariants). The base space is the space of invariants ℐ. The fibre over each invariant ι_k is the set of all expressions that carry that invariant — the equivalence class [ι_k].

S projects "downward" from the fibre to the base: it discards the domain-specific encoding (the fibre) and preserves only the structural invariant (the base point).

### 9.2.3 What S Removes and What It Preserves

The seven layers of the SA architecture map onto the PA as follows:

| SA Layer | Content | PA Region | S Removes? |
|---|---|---|---|
| L1: Surface syntax | Grammar, word order | Domain encoding in 𝒟 | ✅ Removed |
| L2: Lexical domain | Technical vocabulary | Domain encoding in 𝒟 | ✅ Removed |
| L3: Rhetorical structure | Persuasion, framing | Identity filter (I) | ✅ Removed |
| L4: Cultural frame | Norms, assumptions | Context (K) | ✅ Removed |
| **L5: Structural dynamic** | **Proportional relations** | **ℐ** | **❌ Preserved** |
| **L6: Operational invariant** | **The structural law** | **ℐ** | **❌ Preserved** |
| **L7: Meta-systemic position** | **Position in 𝒫** | **ℐ** | **❌ Preserved** |

Layers 1-4 are the *fibre* — the domain-specific encoding. Layers 5-7 are the *base* — the invariant. S removes the fibre and preserves the base.

### 9.2.4 Algebraic Properties of S

**Idempotency**:

$$S(S(E)) = S(E)$$

Stripping a stripped expression produces the same result. Once the domain encoding is removed, further stripping has no effect. In fibre-bundle terms: projecting from the base to the base is the identity.

**Domain-independence**:

$$S(E_1) = S(E_2) \iff E_1 \equiv_S E_2$$

Two expressions yield the same invariant under S if and only if they are structurally equivalent. This is the formal definition of structural equivalence (§3.4).

**Non-injectivity**:

$$S(E_1) = S(E_2) \;\not\!\!\!\implies E_1 = E_2$$

Many different expressions can carry the same invariant. S maps many-to-one. This is structurally correct: the whole point of S is that the same structural law can appear in infinitely many domain-specific forms.

**Partial inversibility**:

S is the partial inverse of Φ, in the sense that:

$$S(\Phi(C, I, K)) = I_{structural} \quad \text{where } I_{structural} \subseteq C$$

The structural content extracted by S is a *subset* of the original coherent content C — the part that survived the three losses of collapse (selection, projection, instantiation). S cannot reconstruct C, but it can recover the invariant core.

---

## 9.3 The Re-contextualisation Operator π — PA Formalisation

### 9.3.1 SA Definition (Review)

In the Semantic Algebra, π was defined as:

> *Given an invariant ι_k, re-express it in a target domain 𝔻, producing a new expression that carries the same structural content in a different vocabulary.*

### 9.3.2 PA Definition

In the Proportional Algebra, π is formalised as a section of the fibre bundle:

> **Definition 9.2 (Re-contextualisation Operator).** The re-contextualisation is a mapping:
>
> $$\pi: \mathcal{I} \times \mathcal{D}_{target} \to \mathcal{D}$$
>
> that takes an invariant ι_k ∈ ℐ and a target domain specification 𝔻_target, and produces a new expression E' ∈ 𝒟 such that:
>
> $$S(E') = ι_k$$

In fibre-bundle terms: π is a **section** — it lifts from the base space (invariants) back up to a specific fibre (a domain-specific expression). Given the base point ι_k, π selects a specific point in the fibre over ι_k — the expression that carries ι_k in the target domain.

### 9.3.3 The SA Round-Trip as a Fibre-Bundle Property

The SA round-trip test:

$$S(\pi(ι_k, D)) = ι_k$$

is simply the statement that a section followed by a projection returns to the base point. This is a *defining property* of fibre bundles — it is not an empirical discovery but a structural necessity. The SA, without knowing it, had discovered a fibre-bundle property.

The PA now explains *why* the round-trip works: because the decoherent space 𝒟 has the structure of a fibre bundle over the space of invariants ℐ, and S and π are the projection and section of that bundle.

---

## 9.4 S and π as Restrictions of PA Operations

The relationship between SA and PA can now be stated precisely:

> **Theorem 9.1 (SA as Special Case of PA).** The Semantic Algebra is the Proportional Algebra restricted to the decoherent space 𝒟, with the coherent field ℭ_h treated as inaccessible.

Proof sketch:
1. S = Φ⁻¹_partial — S is the partial inverse of Collapse, restricted to extracting the invariant without accessing the original C
2. π = Φ restricted to invariants — π is a collapse operation where the "content" is a known invariant (not a raw coherent content) and the "identity" is the target domain specification
3. The SA round-trip S(π(ι, 𝔻)) = ι is a consequence of the fibre-bundle structure of 𝒟

The SA operates entirely within 𝒟. The PA operates across all three regions (ℭ_h, 𝕀, 𝒟). The SA's operators are PA operators with restricted domain.

### What the SA Cannot Do (and the PA Can)

| Capability | SA | PA |
|---|---|---|
| Extract invariants from expressions | ✅ S | ✅ S |
| Re-express invariants in new domains | ✅ π | ✅ π |
| Measure the resonance between content and identity | ❌ | ✅ ρ |
| Verify that the original collapse was coherent | ❌ | ✅ Extended round-trip |
| Describe the coherent field before collapse | ❌ | ✅ ℭ_h |
| Measure inter-identity compatibility | ❌ | ✅ ⊗ |
| Track identity evolution over the trajectory | ❌ | ✅ 𝒰 |

The SA is the PA's diagnostic arm. The PA is the SA's theoretical body.

---

## 9.5 The Invariant Library as a Catalogue of 𝒫

The Semantic Algebra developed a library of ten invariants (ι₁ through ι₁₀), each a structural law extracted from expressions across multiple domains. In the PA, this library receives a precise interpretation:

> Each invariant ι_k corresponds to an **equivalence class** in the decoherent space 𝒟 under the structural equivalence relation ≡_S.

The class [ι_k] = {E ∈ 𝒟 : S(E) = ι_k} is the set of all expressions — in all domains, across all contexts — that carry the same structural law.

Within each class, the coherence order ≤_𝓚 ranks the expressions. The most coherent expression of each invariant is the supremum of the class — the "purest" carrier of that structural law.

The library is therefore a **catalogue of the base points of the fibre bundle** — a list of the structural laws that the PA's space contains. The library is necessarily incomplete (the number of possible invariants may be infinite), but each entry is verified by the round-trip test.

---

*The diagnostic arm is formalised. Now we build the relational arm — the operation that two identities perform together.*

---
