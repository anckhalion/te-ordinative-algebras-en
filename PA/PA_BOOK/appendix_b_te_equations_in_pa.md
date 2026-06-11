# Appendix B — The 12 TE Equations in PA Notation

---

This appendix lists the twelve foundational equations of the Technology of Expressions (TE) and their translation into the formal notation of the Proportional Algebra.

| # | TE Equation | TE Notation | PA Translation | PA Chapter |
|---|---|---|---|---|
| **1.1** | Collapse Function | E = Φ(C, I, K) | Φ: ℭ_h × 𝕀 × K → 𝒟. Collapse iff ρ(C, I, K) ≥ θ(C). | 8.2 |
| **1.2** | Decoherence Equation | D = Ψ(C, N, t) | D ∈ 𝒟. N = noise vector in fibre. t = τ (pulsation count). ⟨𝓚⁵⟩(D) < ⟨𝓚⁵⟩(E_original). | 6.2, 12.2 |
| **1.3** | Extended Semantic Derivative | dΦ/dt(I) | dΦ/dτ = lim_{n→∞} (Φ_{n+1} − Φ_n)/τ_n. Three regimes: >0 (evolution), =0 (inertia), <0 (degeneration). | 12.5 |
| **1.4** | Semantic Tension | T_sem = R − Φ(C, I, K) | T_sem = ρ(C, I) − ⟨𝓚⁵⟩(E). Tension = resonance minus achieved coherence. Residual = un-collapsed potential. | 5.1, 6.2 |
| **1.5** | Vertical Coherence | ⟨𝓚⁵⟩_v(I) > θ_v | The coherence of the identity's trajectory satisfies the vertical threshold: Σ_i ⟨𝓚⁵⟩(E_i) / n ≥ θ_v. Recursive: R_{n+1} ⊇ R_n. | 4.4.5, 3.8 |
| **1.6** | Semantic Inertia | dΦ/dt → 0 | dΦ/dτ = 0. Pulsation continues (τ > 0) but produces no change. The Remir repeats without restructuring. B_I is frozen. | 12.5 |
| **1.7** | Pulsation | T = τ(C ↔ E) | τ: ℭ_h × 𝒟 × 𝕀 → ℝ⁺. τ = d(C)/(ρ · plasticity) · τ₀. Time is generated, not parametric. | 12.2 |
| **1.8** | Expression–Content Asymmetry | E ≠ C; |E| < |C| | Φ is non-invertible. The three losses (selection, projection, instantiation) ensure |E| < |C_K| < |C|. S recovers I_{structural} ⊂ C, not C itself. | 8.3.4 |
| **1.9** | Remir | ℛ(I) = (V_I, B_I) | V_I = finite set of semantic vectors. B_I: V_I × V_I → [-1,1]. Dominant vector λ(I) = eigenvector of B_I with max eigenvalue. 𝕀 is a non-commutative, non-associative algebra. | 7.2, 7.6 |
| **1.10** | Dominant Vector | λ(I) = argmax β(v, I) | λ(I) = eigenvector of B_I with largest eigenvalue λ_max. Determines collapse direction and trajectory bias. | 7.3 |
| **1.13** | Terminal Compatibility | Ξ(I, 𝒯, t) → [0,1] | Ξ measures ρ_K at the body-identity interface. Declining Ξ = declining capacity to collapse through the physical channel. High ρ_v + low ρ_K = identity "knows more, can say less." | 16.5 |
| **1.14** | Collective Field | ℭ_h = f({I₁...Iₙ}) | ⊗ⁿ_{k=1} I_k = ∪_{all resonant pairs} ℭ_shared. n-fold resonance. Emergent directions, resonance cascades, critical mass. | 10.6 |

---

## Key Transformations

1. **Time (t) → Pulsation count (τ)**: All TE equations parametrised by t are re-parametrised by pulsation cycles. This eliminates the need for external time.

2. **Coherence (abstract) → ⟨𝓚⁵⟩ (5-component function)**: All TE references to "coherence" become the formal ⟨𝓚⁵⟩ function with its five components.

3. **Resonance (intuitive) → ρ (5-component metric)**: All TE references to "compatibility" or "resonance" become the formal ρ function with its five components and threshold θ.

4. **Identity (functional description) → Remir algebra**: All TE references to identity become the formal Remir ℛ(I) = (V_I, B_I) with its algebraic properties.

---
