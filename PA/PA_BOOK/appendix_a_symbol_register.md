# Appendix A — Symbol Register

---

## Spaces

| Symbol | Name | Definition | Chapter |
|---|---|---|---|
| 𝒫 | Proportional Space | (𝒞, ℛ, 𝒟, ρ, ≤_κ) | 4 |
| 𝒞 | Coherent Field | Space of un-collapsed structured potential | 4.2 |
| ℛ | Identity Space | Space of Remirs | 4.2 |
| 𝒟 | Decoherent Space | Space of expressed realities | 4.2 |
| ℐ | Invariant Space | Space of structural invariants (base of the fibre bundle) | 9.2 |
| 𝒞_shared | Shared Coherent Field | Region of 𝒞 accessible to two identities via ⊗ | 10.2 |
| N(I) | Accessible Field | {C ∈ 𝒞 : ρ(C, I) ≥ θ} — neighbourhood of I in 𝒞 | 5.5.4 |

## Objects

| Symbol | Name | Definition | Chapter |
|---|---|---|---|
| C | Coherent Content | Element of 𝒞 — un-collapsed structured potential | 2.2 |
| I | Identity | Active functional vector that performs the collapse | 2.2 |
| K | Context | Constraint on 𝒞 that restricts accessible content: K(𝒞) → 𝒞_K | 4.5 |
| E | Expression | Element of 𝒟 — collapsed, observable output | 2.2 |
| ℛ(I) | Remir | (V_I, B_I) — semantic vectors + resonance matrix | 7.2 |
| V_I | Semantic Vectors | {v₁, v₂, ..., vₙ} — directed intensities of the identity | 7.2 |
| B_I | Resonance Matrix | V_I × V_I → [-1, 1] — internal proportional structure | 7.2 |
| λ(I) | Dominant Vector | Eigenvector of B_I with largest eigenvalue | 7.3 |
| T(I) | Trajectory | Ordered sequence of an identity's collapses | 3.2 |
| I_k | Invariant k | Structural law extracted by S — base point of fibre bundle | 9.5 |

## Operations

| Symbol | Name | Type Signature | Chapter |
|---|---|---|---|
| Φ | Collapse | 𝒞 × ℛ × K → 𝒟 | 8.2 |
| S | Strip | 𝒟 → ℐ × [0, 1] | 9.2 |
| π | Re-contextualisation | ℐ × D_target → 𝒟 | 9.3 |
| ⊗ | Resonance | ℛ × ℛ → 𝒞_shared | 10.2 |
| 𝒰 | Identity Update | ℛ × 𝒟 → ℛ | 8.6 |
| τ | Pulsation | 𝒞 × 𝒟 × ℛ → ℝ⁺ | 12.2 |
| μ | Isomorphism Map | D₁ → D₂ (structure-preserving) | 2.3 |

## Metrics and Measures

| Symbol | Name | Range | Chapter |
|---|---|---|---|
| ρ | Resonance Metric | [0, 1] | 5.1 |
| ρ_v | Vectorial Alignment | [0, 1] | 5.2 |
| ρ_d | Proportional Depth | [0, 1] | 5.2 |
| ρ_K | Contextual Compatibility | [0, 1] | 5.2 |
| ρ_τ | Temporal Phase | [0, 1] | 5.2 |
| ρ_R | Relational Readiness | {1.0, 0.8, 0.5, 0.3, 0.1, 0.0} | 5.2 |
| κ | Coherence Function | [0, 1] | 6.2 |
| κ_1 | Internal Consistency | [0, 1] | 6.2 |
| κ_2 | Source Alignment | [0, 1] | 6.2 |
| κ_3 | Depth Preserved | [0, 1] | 6.2 |
| κ_4 | Stability | [0, 1] | 6.2 |
| κ_5 | Generative Capacity | [0, 1] | 6.2 |
| θ | Collapse Threshold | [0, 1] | 5.4 |
| δ | Fidelity | [0, 1] | 11.2 |
| b̄(I) | Average Internal Coherence | [-1, 1] | 7.2 |
| Ξ | Terminal Compatibility | [0, 1] | 16.5 |

## Relations

| Symbol | Name | Type | Chapter |
|---|---|---|---|
| ≤_κ | Coherence Order | Partial order on 𝒟 | 6.3 |
| ≡_S | Structural Equivalence | Equivalence relation on 𝒟 | 3.4 |
| ∼_ρ | Compatibility | Tolerance relation on 𝒞 × ℛ | 3.4 |

## Collapse Types

| Type | Condition | Description | Chapter |
|---|---|---|---|
| Α | κ ≥ 0.7, ρ ≥ θ | Coherent — faithful carrier | 8.5 |
| Β | 0.3 ≤ κ < 0.7 | Partial — shallow but accurate | 8.5 |
| Γ | κ < 0.3, S(E) ≠ ∅ | Distorted — content altered | 8.5 |
| Δ | S(E) = ∅ or ρ < θ | Failed — no structural content | 8.5 |

## Falsification Criteria

| Code | Would Falsify | Chapter |
|---|---|---|
| F1 | Φ as well-defined operation | 3.6 |
| F2 | The isomorphism map μ | 3.6 |
| F3 | The resonance metric ρ | 3.6 |
| F4 | S as extraction (not projection) | 3.6 |
| F5 | The coherence order ≤_κ | 3.6 |
| F6 | The symmetry of ⊗ | 3.6 |

---
