[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20059540.svg)](https://doi.org/10.5281/zenodo.20059540)

# Ordinative Algebras — Semantic Algebra (SA) and Proportional Algebra (PA)

English public mirror of two distinct formal frameworks developed within the Technology of Expressions / Ordinative Sciences research programme.

## Two Frameworks, One Repository

This repository bundles two **independent** formal systems that share a structural relationship:

| Framework | Folder | Focus |
| --- | --- | --- |
| **Semantic Algebra (SA)** | `SA/` | A formal method to extract universal structural invariants from natural language and re-project them into any target domain. |
| **Proportional Algebra (PA)** | `PA/` | The formal space, metric, and operators that govern collapse from coherent content to expressed form across all domains — language, chemistry, music, emotion, medicine, AI, and more. |

The relationship: **PA Theorem 9.1** establishes that SA is mathematically a restriction of PA to the decoherent space `D`. This connects them formally without collapsing them into a single project. SA was developed first as a tool for AI training and cross-domain translation; PA was announced in the foundational TE text and provides the deeper theoretical structure.

For convenience, both are versioned and released together. They can be read independently.

## Part of a Larger Ecosystem

This repository is one of four public repositories in the Ordinative Sciences programme:

| Repository | Purpose | What you'll find there |
| --- | --- | --- |
| **[ordinative_sciences_framework](https://github.com/anckhalion/ordinative_sciences_framework)** | **Theory** | The complete TE framework, core ontology, and operational modules. |
| **[te-ordinative-lora](https://github.com/anckhalion/te-ordinative-lora)** | **Practice** | Code, datasets, and scripts to fine-tune an LLM into a TE-compliant ordinative agent. |
| **[te-oct-framework-en](https://github.com/anckhalion/te-oct-framework-en)** | **Validation** | English mirror of the core framework, plus OCT (Ordinative Category Theory) datasets and benchmarks. |
| **te-ordinative-algebras-en** (this repo) | **Algebras** | The SA and PA formal frameworks — analytical operators and the proportional space they live in. |

These repositories are designed to work together. Reading one in isolation can lead to incomplete understanding.

For a full map, see `ECOSYSTEM.md`.

## First-Time Reader Shortcut

If this is your first visit, start here:

1. `START_HERE_FIRST_TIME.md`
2. `SIMPLE_GLOSSARY.md`
3. `SUPER_SIMPLE_FAQ.md`

## What Is in `SA/`

Semantic Algebra — an operator-based method that:

1. Takes any natural-language expression and applies the **Strip operator (S)** to extract its structural content (invariant), removing field-specific vocabulary.
2. Takes a known structural content and applies the **Re-contextualization operator (π)** to re-express it in any chosen target domain.
3. Verifies that the round-trip `S(π(I, D)) = I` holds — a formal integrity test on the extraction.

Validated through:
- A 7-text experiment across maximally distant domains (Lao Tzu, Shakespeare, Einstein, Rumi, Bhagavad Gita, Gödel, Ungaretti) producing an unprogrammed convergence.
- A discrimination test on 4 expressions that simulate depth — 0 false positives.
- A documented self-correction case (Ungaretti's *M'illumino d'immenso*), demonstrating the method's capacity to detect and correct projection errors.

Current invariant library: 10 validated invariants (ι₁ through ι₁₀).

## What Is in `PA/`

Proportional Algebra — a formal grammar that:

1. Defines the **Proportional Space `𝒫 = (ℭ_h, 𝕀, 𝒟, ρ, ≤_𝓚)`** — the ground in which coherent content, identities, expressions, and their relations live.
2. Defines three operators: **Collapse (Φ)**, **Strip (S)**, **Resonance (⊗)**, and the **Pulsation generator (τ)** that produces time as an emergent quantity.
3. Provides the **Extended Round-Trip (ERT)** — a four-step diagnostic that tests not only analytical fidelity (as SA does) but also genetic fidelity of the original collapse.
4. States six explicit falsification criteria (F1–F6).

Demonstrated across five domains: chemistry, language, emotion, medicine, artificial intelligence.

A small Python reference engine implementing the PA operators is in `PA/pa_engine/`.

## Important Disambiguation

- "PA" in this repository means **Proportional Algebra**, not anything else (e.g., Pennsylvania, public address, etc.).
- "Algebra" here refers to a structured grammar with operators and tests, not numerical algebra.
- This is **research material**, not deployed software or a proven physical theory. Both frameworks include explicit falsification criteria and operational tests.

## What You Will Find

- Front-door files: `START_HERE_FIRST_TIME.md`, `INDEX.md`, `SIMPLE_GLOSSARY.md`, `SUPER_SIMPLE_FAQ.md`
- Governance: `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`
- Operational: `CHANGELOG.md`, `RELEASE_CHECKLIST.md`
- Discovery: `ECOSYSTEM.md`, `OBJECT_REGISTRY.md`, `object_registry.json`, `LOAD_PROFILES.md`, `PUBLICATION_SCOPE.md`
- `SA/` — Semantic Algebra full corpus
- `PA/` — Proportional Algebra full corpus + reference engine
- `.github/` — issue and PR templates

## What This Repository Is Not

- Not a model-weight repository
- Not a turnkey productized AI system
- Not a claim of proven cross-domain unity without falsification evidence
- Not LaTeX or print-ready material — the public mirror is Markdown-only by design (LaTeX projects exist privately and may be deposited separately on Zenodo)

## Start Here (New Readers)

For SA-first reading:

1. `SA/README.md`
2. `SA/START_HERE_SA.md`
3. `SA/SA_BOOK/00_prologue.md`
4. `SA/SA_BOOK/01_the_lossy_channel.md`
5. `SA/SA_BOOK/06_the_strip_operator.md`

For PA-first reading:

1. `PA/README.md`
2. `PA/START_HERE_PA.md`
3. `PA/PA_BOOK/01_why_the_sciences_cannot_speak.md`
4. `PA/PA_BOOK/04_the_proportional_space.md`
5. `PA/PA_BOOK/08_collapse_operator.md`

## Citation

To cite SA: *Ghioni, F. Semantic Algebra: Foundations. Technology of Expressions — Ordinative Sciences. 2026.*

To cite PA: *Ghioni, F. Proportional Algebra: Foundations. Technology of Expressions — Ordinative Sciences. 2026.*

Include the version tag (e.g., `v1.0.0`) and this repository URL.
