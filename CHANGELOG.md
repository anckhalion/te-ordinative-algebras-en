# Changelog

All notable changes to this repository should be documented in this file.

The format is inspired by Keep a Changelog and semantic versioning principles for documentation releases.

## [Unreleased — v2.0.0-dev] - 2026-06-11

### Changed — Canonical notation consolidation (Symbol Canon v1.0)

Programme-wide symbol renames per the **Symbol Canon for the Ordinative Sciences Programme** (ratified by the author 2026-06-11). Notation only — no semantic changes.

- **PA**: 𝒞 → ℭ_h (with ℭ_shared, ℭ_K); Identity Space ℛ → 𝕀 (the Remir ℛ(I) unchanged); coherence family κ/κ_1…κ_5/≤_κ → 𝓚⁵/⟨𝓚⁵⟩/𝓚_1…𝓚_5/≤_𝓚 (extends OST's 𝓚); invariants I_k → ι_k; collapse types Α/Β/Γ/Δ → A/B/C/D (state taxonomy shared with OCT); domains D₁/D₂/D_target → 𝔻₁/𝔻₂/𝔻_target. LaTeX macro layer updated (\mathfrak{C}_h, \mathbb{I}, \mathcal{K}).
- **SA**: Φ/Φ_d/Φ_eff → 𝔉/𝔉_d/𝔉_eff; gap Δ/Δ_S → Δ_𝔉; K → 𝒦_p; K_real → 𝒦_r; invariants I/I₁–I₁₀ → ι/ι₁–ι₁₀; Controphase C → C_φ; Domain D → 𝔻; τ → τ_ph; λ → λ_L; ω → ω_att. Unchanged: S, π, σ, R, ρ, θ, Σ_src, U, κ (SA scope, canon-declared). The TE collapse equation E = Φ(C, I, K) is quoted in TE notation by design.
- Canon Alignment Notes added to both symbol registers (PA Appendix A, SA Appendix A); SA↔PA equivalences appendix updated on both sides; engine notation note added (`PA/pa_engine/CANON_NOTATION_NOTE.md`).

### Added — Two-channel extension and the Atlas

- **SA §6.8 The Two-Channel Extension** — S(E) = ⟨ι, P⟩: the connotation co-operator κ_c (systematization, not a new primitive), payload typology, three+one detectors (etymological divergence, Δ_𝔉 sign, PPRO markers, ι-scatter), formal properties (idempotence on clean text; π transports ι, never P).
- **SA §9.8 The Fourth Quadrant** — the ⟨ι, P⟩ matrix; the **Device** class with dual calibrated band (extractive 0.12–0.45 / pedagogical 0.5–0.85); the truth-shield phenomenon (measured: one blind analysis in three read the borrowed-carrier case clean); three operational rules (spread, scatter, annotation).
- **SA Appendix E — The Atlas**: 47 famous texts from ten categories stripped with the calibrated two-channel method; full library coverage (ι₁–ι₁₀), all four quadrants; five full-depth exemplars; declared edges with both readings; double index. Validation: 3-run blind calibration with pre-registered falsifiers (0 false positives on sealed clean controls).
- **`SYMBOL_CANON.md`** at repository root — condensed programme canon documenting the v2.0 notation.
- Two-channel sections propagated to the SA_FULL manuscripts (Complete 5/5, Unified 5/5, Foundations: compact extension + Device rows).

## [1.0.1] - 2026-05-06

### Notes
- Release tag created to activate the Zenodo deposit pipeline for this repository. Future releases will be automatically deposited on Zenodo with assigned DOI.
- No content changes from `v1.0.0`; this is a tag-only release for archival purposes.

## [1.0.0] - 2026-05-06

Initial public release.

### Added

#### Semantic Algebra (SA) corpus

- `SA/README.md` and `SA/START_HERE_SA.md`
- `SA/SA_BOOK/` chapter-level Markdown (21 files):
  - `00_editorial_proposal.md`, `00_prologue.md`, `00b_before_you_object.md`
  - Chapters 1–13: lossy channel, domain binding, projection problem, axiom and invariant, library of invariants, strip operator, re-contextualization operator, seven-text experiment, discrimination test, self-correction (Ungaretti), `10b` ghost observer, connections, implications, epilogue
  - `appendix_a_vocabulary.md`, `appendix_b_output_format.md`, `appendix_c_invariant_library.md`, `appendix_d_natural_sciences.md`
- `SA/SA_FULL/` single-file manuscripts:
  - `Semantic_Algebra_Foundations_EN.md` — concise foundations
  - `Semantic_Algebra_Complete_Manuscript.md` — extended manuscript
  - `Semantic_Algebra_What_Language_Hides_UNIFIED.md` — unified compilation

#### Proportional Algebra (PA) corpus

- `PA/README.md` and `PA/START_HERE_PA.md`
- `PA/PA_BOOK/` chapter-level Markdown (24 files):
  - Part I — The Problem of the Absent Grammar (chapters 1–3)
  - Part II — The Proportional Space (chapters 4–7)
  - Part III — The Operators (chapters 8–12)
  - Part IV — Cross-Domain Applications (chapters 13–17)
  - Part V — Completion (chapters 18–20)
  - `appendix_a_symbol_register.md`, `appendix_b_te_equations_in_pa.md`, `appendix_c_sa_pa_equivalences.md`, `appendix_d_bibliography.md`
- `PA/PA_FULL/Proportional_Algebra_Foundations_UNIFIED.md` — single-file manuscript
- `PA/pa_engine/` Python reference engine (~700 lines, 7 files):
  - `dynamics.py`, `ert_diagnostic.py`, `metric.py`, `operators.py`, `remir.py`, `simulation_orchestrator.py`, `test_cases.py`

#### Front-door

- `README.md`
- `INDEX.md`
- `START_HERE_FIRST_TIME.md`
- `SIMPLE_GLOSSARY.md`
- `SUPER_SIMPLE_FAQ.md`

#### Governance

- `LICENSE` (CC BY-NC-SA 4.0)
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `.github/ISSUE_TEMPLATE/bug_report.md`
- `.github/ISSUE_TEMPLATE/feature_request.md`
- `.github/pull_request_template.md`

#### Operational

- `CHANGELOG.md` (this file)
- `RELEASE_CHECKLIST.md`

#### Discovery

- `ECOSYSTEM.md` — cross-repository map (4 repositories: Theory / Practice / Validation / Algebras)
- `OBJECT_REGISTRY.md` and `object_registry.json` — registry of canonical objects
- `LOAD_PROFILES.md` — reading profiles A through G
- `PUBLICATION_SCOPE.md` — included/excluded scope statement

#### Repository configuration

- `.gitignore` (private notes, LaTeX artifacts, Python build artifacts)
- `.gitattributes` (LF line endings)

### Notes

- This is the **initial release** of both SA and PA in public form. SA had circulated privately as working drafts; PA was announced in the foundational TE text and is here published for the first time.
- SA and PA are presented as **distinct frameworks** (per editorial decision), bundled in the same repository for cross-reference convenience. PA Theorem 9.1 establishes the formal restriction relationship between them without collapsing them into a single project.
- All author attributions in front-matter are unified to `Fabio Ghioni` (citations and bibliography excepted).
- The public mirror is **Markdown-only** by design. LaTeX projects exist privately and may be deposited separately on Zenodo for archival purposes.
