# Appendix A — Symbol Register

---

## Spaces

| Symbol | Name | Definition | Chapter |
|---|---|---|---|
| 𝒫 | Proportional Space | (ℭ_h, 𝕀, 𝒟, ρ, ≤_𝓚) | 4 |
| ℭ_h | Coherent Field | Space of un-collapsed structured potential | 4.2 |
| 𝕀 | Identity Space | Space of Remirs | 4.2 |
| 𝒟 | Decoherent Space | Space of expressed realities | 4.2 |
| ℐ | Invariant Space | Space of structural invariants (base of the fibre bundle) | 9.2 |
| ℭ_shared | Shared Coherent Field | Region of ℭ_h accessible to two identities via ⊗ | 10.2 |
| N(I) | Accessible Field | {C ∈ ℭ_h : ρ(C, I) ≥ θ} — neighbourhood of I in ℭ_h | 5.5.4 |

## Objects

| Symbol | Name | Definition | Chapter |
|---|---|---|---|
| C | Coherent Content | Element of ℭ_h — un-collapsed structured potential | 2.2 |
| I | Identity | Active functional vector that performs the collapse | 2.2 |
| K | Context | Constraint on ℭ_h that restricts accessible content: K(ℭ_h) → ℭ_K | 4.5 |
| E | Expression | Element of 𝒟 — collapsed, observable output | 2.2 |
| ℛ(I) | Remir | (V_I, B_I) — semantic vectors + resonance matrix | 7.2 |
| V_I | Semantic Vectors | {v₁, v₂, ..., vₙ} — directed intensities of the identity | 7.2 |
| B_I | Resonance Matrix | V_I × V_I → [-1, 1] — internal proportional structure | 7.2 |
| λ(I) | Dominant Vector | Eigenvector of B_I with largest eigenvalue | 7.3 |
| T(I) | Trajectory | Ordered sequence of an identity's collapses | 3.2 |
| ι_k | Invariant k | Structural law extracted by S — base point of fibre bundle | 9.5 |

## Operations

| Symbol | Name | Type Signature | Chapter |
|---|---|---|---|
| Φ | Collapse | ℭ_h × 𝕀 × K → 𝒟 | 8.2 |
| S | Strip | 𝒟 → ℐ × [0, 1] | 9.2 |
| π | Re-contextualisation | ℐ × 𝔻_target → 𝒟 | 9.3 |
| ⊗ | Resonance | 𝕀 × 𝕀 → ℭ_shared | 10.2 |
| 𝒰 | Identity Update | 𝕀 × 𝒟 → 𝕀 | 8.6 |
| τ | Pulsation | ℭ_h × 𝒟 × 𝕀 → ℝ⁺ | 12.2 |
| μ | Isomorphism Map | 𝔻₁ → 𝔻₂ (structure-preserving) | 2.3 |

## Metrics and Measures

| Symbol | Name | Range | Chapter |
|---|---|---|---|
| ρ | Resonance Metric | [0, 1] | 5.1 |
| ρ_v | Vectorial Alignment | [0, 1] | 5.2 |
| ρ_d | Proportional Depth | [0, 1] | 5.2 |
| ρ_K | Contextual Compatibility | [0, 1] | 5.2 |
| ρ_τ | Temporal Phase | [0, 1] | 5.2 |
| ρ_R | Relational Readiness | {1.0, 0.8, 0.5, 0.3, 0.1, 0.0} | 5.2 |
| 𝓚⁵ | Coherence Vector | (𝓚_1, 𝓚_2, 𝓚_3, 𝓚_4, 𝓚_5) — 5-dimensional extension of OST's intra-set coherence vector 𝓚 | 6.2 |
| ⟨𝓚⁵⟩ | Coherence Aggregate | [0, 1] — weighted mean of the 𝓚⁵ components (weights per §6.2) | 6.2 |
| 𝓚_1 | Internal Consistency | [0, 1] | 6.2 |
| 𝓚_2 | Source Alignment | [0, 1] | 6.2 |
| 𝓚_3 | Depth Preserved | [0, 1] | 6.2 |
| 𝓚_4 | Stability | [0, 1] | 6.2 |
| 𝓚_5 | Generative Capacity | [0, 1] | 6.2 |
| θ | Collapse Threshold | [0, 1] | 5.4 |
| δ | Fidelity | [0, 1] | 11.2 |
| b̄(I) | Average Internal Coherence | [-1, 1] | 7.2 |
| Ξ | Terminal Compatibility | [0, 1] | 16.5 |

## Relations

| Symbol | Name | Type | Chapter |
|---|---|---|---|
| ≤_𝓚 | Coherence Order | Partial order on 𝒟 | 6.3 |
| ≡_S | Structural Equivalence | Equivalence relation on 𝒟 | 3.4 |
| ∼_ρ | Compatibility | Tolerance relation on ℭ_h × 𝕀 | 3.4 |

## Collapse Types

| Type | Condition | Description | Chapter |
|---|---|---|---|
| A | ⟨𝓚⁵⟩ ≥ 0.7, ρ ≥ θ | Coherent — faithful carrier | 8.5 |
| B | 0.3 ≤ ⟨𝓚⁵⟩ < 0.7 | Partial — shallow but accurate | 8.5 |
| C | ⟨𝓚⁵⟩ < 0.3, S(E) ≠ ∅ | Distorted — content altered | 8.5 |
| D | S(E) = ∅ or ρ < θ | Failed — no structural content | 8.5 |

## Falsification Criteria

| Code | Would Falsify | Chapter |
|---|---|---|
| F1 | Φ as well-defined operation | 3.6 |
| F2 | The isomorphism map μ | 3.6 |
| F3 | The resonance metric ρ | 3.6 |
| F4 | S as extraction (not projection) | 3.6 |
| F5 | The coherence order ≤_𝓚 | 3.6 |
| F6 | The symmetry of ⊗ | 3.6 |

---

## Canon Alignment Note (Symbol Canon v1.0 — ratified 2026-06-11)

This register follows the **Symbol Canon for the Ordinative Sciences Programme**. Renames applied in v2.0 relative to v1.0.1 (notation only — no semantic changes):

| v1.0.1 | v2.0 | Object |
|---|---|---|
| 𝒞, 𝒞_shared, 𝒞_K | ℭ_h, ℭ_shared, ℭ_K | Coherent Field and derived regions (frees 𝒞 = TE Collective Field) |
| ℛ (space) | 𝕀 | Identity Space — the Remir ℛ(I) is unchanged |
| κ, κ_1…κ_5, ≤_κ | ⟨𝓚⁵⟩, 𝓚_1…𝓚_5, ≤_𝓚 | Coherence vector 𝓚⁵ and aggregate — extends OST's intra-set 𝓚 (3-vector); TE's pairwise κ(I_a, I_b) is a distinct object coexisting by operand distinction |
| I_k | ι_k | Invariants (ι-family programme-wide) |
| Α / Β / Γ / Δ | A / B / C / D | Collapse types — state taxonomy shared with OCT admissibility states (A admissible · B sterile/partial · C degenerative/distorted · D invalid/failed); PA instantiates it over collapse quality, OCT over morphism admissibility |
| D₁, D₂, D_target | 𝔻₁, 𝔻₂, 𝔻_target | Domains (𝔻 namespace; 𝒟 remains the Decoherent Space, declared equivalent to TE's plain D) |

Unchanged by design: Φ (Collapse, TE-aligned), S (Strip), π (Re-contextualisation), ⊗ (Resonance), τ (Pulsation), ρ and its five components (Resonance family), θ, 𝒰, μ, Ξ, ℐ (Invariant Space), V_I, B_I, λ(I).
