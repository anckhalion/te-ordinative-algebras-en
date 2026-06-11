# PA — Proportional Algebra

The formal space, metric, and operators that govern the collapse from coherent content to expressed form across all domains.

## Scope

This folder contains the Proportional Algebra corpus in English for:

- GitHub public repository content
- Zenodo / OSF deposits
- Hugging Face documentation/dataset cards
- Reference engine (`pa_engine/`) for experimental verification of PA operators

## What PA Is

Proportional Algebra is announced in the foundational TE text and is here published for the first time. It provides:

1. **The Proportional Space** `P = (C, R, D, ρ, ≤_𝓚)` — the formal ground in which coherent content (`C`), identities (`R`), expressions (`D`), and their relations live.
2. **Three operators**:
   - `Φ` (Collapse) — the central operation that generates expressions from coherent content via an identity in a context.
   - `S` (Strip) — the partial inverse of Φ; identical to the SA operator and identified in PA as the projection of a fibre bundle from `D` onto invariant space `I`.
   - `⊗` (Resonance) — generates shared coherent fields between two identities.
3. **The Pulsation generator** `τ` — produces time as an emergent quantity from the cycle of collapse and return, rather than treating time as an external parameter.
4. **The Extended Round-Trip (ERT)** — a four-step diagnostic that tests both analytical fidelity (as SA does) and genetic fidelity of the original collapse.
5. **Six explicit falsification criteria** (F1–F6).

## What PA Is Not

- Not a metaphysics — every operator has procedural definitions and falsifiable properties.
- Not a numerical algebra — "algebra" here means a structured grammar with operations and tests.
- Not a "theory of everything" — PA explicitly states its limits (Chapter 18) and identifies the questions that belong to OCT/OGT.

## Cross-Domain Demonstrations

PA is demonstrated across five domains in Part IV (chapters 13–17):

- **Chemistry** — bonds as proportional collapses; H₂O as worked example with full ERT.
- **Language** — syntax as geometry of proportional vectors; ambiguity as superposition.
- **Emotion** — emotional dynamics as phase transitions in `P`.
- **Medicine** — disease as `⟨𝓚⁵⟩` degradation; therapy as re-coherence.
- **Artificial Intelligence** — specification for a PA-aligned AI; alignment over scale.

Each demonstration applies the full operator set and reports concrete coherence/resonance values.

## Relationship to Semantic Algebra

PA Theorem 9.1 establishes that SA is mathematically a restriction of PA to the decoherent space `D`. The 10 SA invariants become base points of the fibre bundle in PA. The 7-layer SA architecture maps onto PA regions: layers 1–4 are the fibre (removed by S); layers 5–7 are the base (preserved by S).

This connects them formally without collapsing them into a single project. SA was developed first and has independent applications. See `PA_BOOK/appendix_c_sa_pa_equivalences.md` for the complete correspondence table.

## Reference Engine

`pa_engine/` is a small Python package (~700 lines, 7 files) implementing the PA operators and metric for experimentation:

- `remir.py` — the Remir structure (semantic vectors + resonance matrix)
- `metric.py` — the resonance metric ρ with its 5 components
- `operators.py` — the Collapse, Strip, and Resonance operators
- `dynamics.py` — temporal evolution and pulsation
- `ert_diagnostic.py` — the Extended Round-Trip test
- `test_cases.py` — worked examples
- `simulation_orchestrator.py` — entry point

The engine is for experimental verification of the framework. It is not production software.

## Start Here

1. `START_HERE_PA.md` — orientation and reading paths
2. `PA_BOOK/01_why_the_sciences_cannot_speak.md` — motivation
3. `PA_BOOK/04_the_proportional_space.md` — the formal space
4. `PA_BOOK/08_collapse_operator.md` — the central operation
5. `PA_BOOK/11_extended_round_trip.md` — the integrity test

## Falsification

Six explicit falsification criteria are listed in `PA_BOOK/03_what_is_needed.md` §3.6 and `PA_BOOK/18_limits_and_open_questions.md`:

- **F1** — Same `(C, I, K)` produces structurally different `E`
- **F2** — Two expressions classified as structurally isomorphic carry different content
- **F3** — `ρ` assigns wrong compatibility values
- **F4** — `S` yields the same invariant for all expressions
- **F5** — `≤_𝓚` reverses independent coherence judgements
- **F6** — `I₁ ⊗ I₂ ≠ I₂ ⊗ I₁` without contextual cause

None of these have been observed. All are testable.

## Editorial Note

The single-file manuscript `PA_FULL/Proportional_Algebra_Foundations_UNIFIED.md` is the unified compilation. The chapter-level files in `PA_BOOK/` are the canonical source of truth. The Python engine in `pa_engine/` is the runnable companion.
