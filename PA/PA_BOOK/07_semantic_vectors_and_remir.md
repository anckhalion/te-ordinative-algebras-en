# Chapter 7 — Semantic Vectors and the Remir as Algebraic Structure

---

## 7.1 The Identity Problem

The Proportional Space 𝒫 has been defined (Chapter 4), metrised (Chapter 5), and ordered (Chapter 6). One question remains open at the heart of the construction: **what is an identity, algebraically?**

In the Technology of Expressions, identity (I) is defined functionally: it is the active vector that performs the collapse. It is not a psychological self, not a social role, not a biological body — it is the *operator* that selects from the coherent field and collapses it into an expression. 

In the Semantic Algebra, identity appears implicitly: the Strip operator S extracts structural content that was "filtered through" an identity, but S does not describe the identity itself.

The Proportional Algebra must go further. If identity is the operator at the centre of the collapse, and if ρ measures the compatibility between content and identity, then the algebra needs a formal description of what an identity *is* — what it is made of, how it changes, and how two identities relate.

This chapter provides that description. The answer is: **an identity is a Remir, and a Remir is an algebraic structure.**

---

## 7.2 The Remir: Formal Definition

The Remir was introduced in the TE (equation 1.9) as the internal structure of an identity:

$$\mathcal{R}(I) = (V_I, B_I)$$

where V_I is the set of semantic vectors that constitute the identity, and B_I is the resonance matrix between them.

In the Proportional Algebra, we formalise this precisely.

> **Definition 7.1 (Remir).** The Remir of an identity I is the ordered pair:
>
> $$\mathcal{R}(I) = (V_I, B_I)$$
>
> where:
> - $V_I = \{\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n\}$ is a finite set of **semantic vectors** — the irreducible oriented components of the identity
> - $B_I: V_I \times V_I \to [-1, 1]$ is the **internal resonance matrix** — for each pair of vectors, the degree to which they are mutually aligned (+1), orthogonal (0), or opposed (-1)

### Semantic Vectors

A semantic vector $\vec{v}_i$ is not a mathematical vector in ℝⁿ. It is a **directed intensity** — it has:

- A **direction** (what domain of coherent content it is oriented toward)
- An **intensity** (how strongly it is active in the identity)
- An **orientation** (whether it is generative or absorptive with respect to the coherent field)

Examples:
- A physicist's identity might contain a strong vector oriented toward mathematical structure, a moderate vector oriented toward empirical verification, and a weak vector oriented toward aesthetic form
- A poet's identity might contain a strong vector oriented toward sonic pattern, a strong vector toward emotional resonance, and a moderate vector toward linguistic precision
- A molecule's "identity" (the set of conditions that determine its collapse) contains vectors oriented toward energy minimisation, spatial symmetry, and electron distribution

The OST correspondent is immediate: semantic vectors are the **singularities** within the identity's internal system. The identity is itself an ordinative set ⟨Σ_I, R_I, Φ_I⟩, where the singularities are the semantic vectors, the relational field is the resonance matrix, and the emergent function is the identity's capacity to collapse.

### The Resonance Matrix

The matrix B_I describes the *internal proportional structure* of the identity — how the identity's vectors relate to each other. This is the key: the identity is not a list of capacities. It is a *proportional structure* of capacities.

$$B_I = \begin{pmatrix} 1 & b_{12} & \cdots & b_{1n} \\ b_{21} & 1 & \cdots & b_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ b_{n1} & b_{n2} & \cdots & 1 \end{pmatrix}$$

where $b_{ij} = B_I(\vec{v}_i, \vec{v}_j)$ and the diagonal is always 1 (each vector is perfectly aligned with itself).

The matrix captures internal coherence:
- If all off-diagonal entries are positive → the identity's vectors are **mutually reinforcing** (high internal coherence)
- If some entries are negative → some vectors are **in tension** (internal conflict)
- If most entries are near zero → the vectors are **unrelated** (fragmented identity)

The trace of B_I divided by n gives the **average internal coherence** of the identity:

$$\bar{b}(I) = \frac{1}{n(n-1)} \sum_{i \neq j} b_{ij}$$

An identity with $\bar{b}(I)$ close to 1 is highly integrated. An identity with $\bar{b}(I)$ close to 0 is fragmented. An identity with $\bar{b}(I)$ negative is in internal conflict.

---

## 7.3 The Dominant Vector

The TE defines the dominant vector (equation 1.10) as the vector with the highest resonance with the identity's trajectory:

$$\lambda(I) = \arg\max_{\vec{v} \in V_I} \beta(\vec{v}, I)$$

where β is a function measuring the "weight" of each vector in the identity's active configuration.

In the PA, we refine this: the dominant vector is the **eigenvector of B_I with the largest eigenvalue.**

$$B_I \vec{v}_\lambda = \lambda_{max} \vec{v}_\lambda$$

This is not a metaphor. It is the precise algebraic statement that the dominant vector is the one that is *most reinforced by all other vectors* in the identity — the direction that the identity's internal proportional structure most strongly supports.

The dominant vector determines:
- **What the identity is most likely to collapse** — it collapses content aligned with $\vec{v}_\lambda$
- **How the identity appears to others** — the dominant vector is the identity's "signature," its most visible orientation
- **Where the trajectory tends** — the identity's path through 𝒫 is biased toward regions of ℭ_h aligned with $\vec{v}_\lambda$

---

## 7.4 Identity Evolution: The Remir Under Transformation

The Remir is not static. As the identity traverses its trajectory, collapsing expressions and integrating them (the identity-update operator 𝒰 from TE equation 16.5), the Remir changes:

$$\mathcal{R}(I_{n+1}) = \mathcal{U}_R(\mathcal{R}(I_n), E_n)$$

where 𝒰_R is the **Remir-update operator** — it takes the current Remir and the latest expression, and produces a new Remir.

The update can take three forms:

### 7.4.1 Vector Addition

A new experience introduces a new semantic vector not previously present in the identity. The dimension of V_I increases by one:

$$V_{I_{n+1}} = V_{I_n} \cup \{\vec{v}_{new}\}$$

The resonance matrix expands correspondingly, with new entries measuring the resonance between the new vector and all existing ones.

This corresponds to the OST's *evolution*: a new singularity joins the system, and the relational field restructures to incorporate it.

### 7.4.2 Vector Strengthening or Weakening

An existing vector increases or decreases in intensity as a result of the collapse. The vector set does not change, but the weights do:

$$|\vec{v}_i|_{n+1} = |\vec{v}_i|_n + \Delta_i(E_n)$$

where Δ_i is the impact of expression E_n on vector i. If the collapse reinforced the direction of $\vec{v}_i$, Δ_i > 0. If it contradicted it, Δ_i < 0.

### 7.4.3 Matrix Restructuring

The resonance matrix itself changes: vectors that were independent become correlated, or vectors that were aligned become opposed. This is the deepest form of identity transformation:

$$B_{I_{n+1}} = B_{I_n} + \Delta B(E_n)$$

This corresponds to the OST's *restructuring*: the relational field R changes, which changes the emergent function Φ, which changes the identity.

---

## 7.5 Inter-Identity Relations

Two identities relate through their Remirs. The PA defines three fundamental inter-identity relations:

### 7.5.1 Compatibility (⟨𝓚⁵⟩_inter)

Two identities are compatible if their Remirs can generate a shared coherent field (the ⊗ operation):

$$\langle\mathcal{K}^5\rangle_{inter}(I_1, I_2) = \frac{|V_{I_1} \cdot V_{I_2}|}{\max(|V_{I_1}|, |V_{I_2}|)}$$

where $V_{I_1} \cdot V_{I_2}$ denotes the set of vectors in I₁ that have positive resonance with at least one vector in I₂. High ⟨𝓚⁵⟩_inter means the identities share structural orientations. Low ⟨𝓚⁵⟩_inter means they are oriented in different directions.

### 7.5.2 Complementarity

Two identities are complementary if their Remirs cover different regions of ℭ_h with minimal overlap:

$$\text{Complementarity}(I_1, I_2) = 1 - \langle\mathcal{K}^5\rangle_{inter}(I_1, I_2)$$

Complementary identities do not share vectors but do not conflict. They can collaborate because their coverages are additive.

### 7.5.3 Antagonism

Two identities are antagonistic if their dominant vectors are opposed:

$$\text{Antagonism}(I_1, I_2) = -B_{cross}(\vec{v}_{\lambda_1}, \vec{v}_{\lambda_2})$$

where B_cross measures the cross-resonance between the dominant vectors of the two identities. High antagonism (strongly negative cross-resonance) means the identities' primary orientations actively conflict.

This connects to the OST's pathology of *Antagonist Order* (§6): a singularity or subgroup generates a function perpendicular to the global Φ.

---

## 7.6 The Identity as an Algebra

We can now state what an identity is, algebraically:

> **Theorem 7.1 (The Remir Algebra).** The set of all Remirs 𝕀, equipped with:
>
> - the internal product B_I (resonance matrix)
> - the update operator 𝒰_R (evolution under collapse)
> - the cross-product ⊗ (resonance between identities)
>
> forms a **non-commutative, non-associative algebra** with:
>
> - no global identity element (there is no "null identity" that leaves all contents unchanged)
> - no global inverse (identity transformation is irreversible — you cannot "un-learn" in the algebraic sense)
> - a partial order induced by the coherence of the internal matrix ($\bar{b}(I_1) \leq \bar{b}(I_2)$)

The Remir Algebra is a richer structure than a group (which requires associativity and inverses) and a weaker structure than a ring (which requires two commutative operations). It is, in fact, a structure that has no standard name in classical algebra — because classical algebra does not deal with objects that are simultaneously operators, evolving systems, and proportional structures.

This is the algebraic signature of identity in the Proportional Algebra: **an irreversible, non-commutative, self-modifying proportional structure with no neutral element.**

---

## 7.7 Summary: Part II Complete

Part II has built the Proportional Space:

| Chapter | Built | Symbol | Status |
|---|---|---|---|
| 4 | The space itself | 𝒫 = (ℭ_h, 𝕀, 𝒟, ρ, ≤_𝓚) | ✅ Defined |
| 5 | The resonance metric | ρ: ℭ_h × 𝕀 → [0,1] | ✅ 5 components, composite formula |
| 6 | The coherence order | ≤_𝓚 on 𝒟 | ✅ Partial order, lattice structure |
| 7 | The identity structure | ℛ(I) = (V_I, B_I) | ✅ Non-commutative algebra |

The space is defined, metrised, ordered, and its central objects — identities — are characterised as algebraic structures.

Part III will define the three operations that act on this space: Collapse (Φ), Strip (S), and Resonance (⊗).

---

*The anatomy is mapped. Now we describe what the anatomy does.*

---
