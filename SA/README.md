# SA — Semantic Algebra

A formal method for extracting universal structural invariants from natural language and re-projecting them into any target domain.

## Scope

This folder contains the Semantic Algebra corpus in English for:

- GitHub public repository content
- Zenodo / OSF deposits
- Hugging Face documentation/dataset cards
- AI training material (the SA invariant library and operators serve as structural primitives in the TE LoRA training pipeline — see `te-ordinative-lora` repository)

## What SA Is

Semantic Algebra operates on natural-language expressions through two operators:

- **S (Strip)**: extracts whatever structural content is present in an expression — or certifies its absence — by removing field-specific vocabulary.
- **π (Re-contextualization)**: takes a structural pattern and re-expresses it deliberately in a chosen target domain.

The objects produced by S are called **invariants** — structural patterns that do not change under change of domain. The current invariant library contains 10 validated invariants (`ι₁` through `ι₁₀`).

## What SA Is Not

- Not a numerical algebra in the high-school sense; "algebra" here means a structured grammar with formal operators and tests.
- Not a claim that all wisdom traditions or scientific disciplines say the same thing — most expressions, when stripped, contain no invariant at all. The invariants that survive are rare.
- Not deployed software — the formal method is procedural and human-replicable; AI implementations are downstream applications.

## Relationship to Proportional Algebra

PA Theorem 9.1 establishes that SA is mathematically a restriction of PA to the decoherent space `D`. This connects them formally without collapsing them into a single project. SA was developed first, has independent applications, and has its own validation track. See `../PA/PA_BOOK/appendix_c_sa_pa_equivalences.md` for the complete correspondence table.

## Start Here

1. `START_HERE_SA.md` — orientation and reading paths
2. `SA_BOOK/00_prologue.md` — the four-people-in-a-room framing
3. `SA_BOOK/00b_before_you_object.md` — anticipated critiques and structural responses
4. `SA_BOOK/01_the_lossy_channel.md` — the foundational claim about natural language
5. `SA_BOOK/06_the_strip_operator.md` — the S operator definition and procedure
6. `SA_BOOK/07_the_recontextualization_operator.md` — the π operator definition and procedure

## Validation

- **Positive validation** (`SA_BOOK/08_the_seven_text_experiment.md`): 7 texts from 7 maximally distant domains. Result: 5 distinct invariants, 1 unprogrammed convergence (Shakespeare's *King Lear* and Lao Tzu's *Tao Te Ching* both yielding ι₁).
- **Negative validation** (`SA_BOOK/09_the_discrimination_test.md`): 4 expressions that simulate depth. Result: 0 false positives, 3 different diagnostic types correctly identified.
- **Self-correction case study** (`SA_BOOK/10_the_self_correction.md`): documented procedural correction of an initial projection error in the analysis of Ungaretti's *M'illumino d'immenso*.

## Editorial Note

Two single-file manuscripts are provided in `SA_FULL/`:

- `Semantic_Algebra_Foundations_EN.md` — concise reference (~580 lines)
- `Semantic_Algebra_Complete_Manuscript.md` — extended manuscript (~4770 lines) with prologue, "Before You Object" critiques, and case-study chapters
- `Semantic_Algebra_What_Language_Hides_UNIFIED.md` — unified compilation

Use the concise version for orientation and the complete manuscript for full study. The chapter-level files in `SA_BOOK/` are the canonical source of truth.
