# Repository Index

Map of files in `te-ordinative-algebras-en`.

## Quick Orientation

If you are trying to understand the project quickly:

1. `START_HERE_FIRST_TIME.md`
2. `SIMPLE_GLOSSARY.md`
3. `SUPER_SIMPLE_FAQ.md`
4. `README.md` for scope and disambiguation
5. `ECOSYSTEM.md` for cross-repository context

For SA-specific entry: `SA/README.md` → `SA/START_HERE_SA.md`.
For PA-specific entry: `PA/README.md` → `PA/START_HERE_PA.md`.

## Front-Door

- `README.md`
- `INDEX.md` (this file)
- `START_HERE_FIRST_TIME.md`
- `SIMPLE_GLOSSARY.md`
- `SUPER_SIMPLE_FAQ.md`

## Governance

- `LICENSE` (CC BY-NC-SA 4.0)
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `.github/ISSUE_TEMPLATE/`
- `.github/pull_request_template.md`

## Operational

- `CHANGELOG.md`
- `RELEASE_CHECKLIST.md`

## Discovery

- `ECOSYSTEM.md`
- `OBJECT_REGISTRY.md`
- `object_registry.json`
- `LOAD_PROFILES.md`
- `PUBLICATION_SCOPE.md`

## SA — Semantic Algebra

- `SA/README.md`
- `SA/START_HERE_SA.md`
- `SA/SA_BOOK/` — chapter-level Markdown:
  - `00_editorial_proposal.md`
  - `00_prologue.md`
  - `00b_before_you_object.md`
  - `01_the_lossy_channel.md`
  - `02_domain_binding.md`
  - `03_the_projection_problem.md`
  - `04_the_axiom_and_the_invariant.md`
  - `05_the_library_of_invariants.md`
  - `06_the_strip_operator.md`
  - `07_the_recontextualization_operator.md`
  - `08_the_seven_text_experiment.md`
  - `09_the_discrimination_test.md`
  - `10_the_self_correction.md`
  - `10b_the_ghost_observer.md`
  - `11_connections.md`
  - `12_implications.md`
  - `13_epilogue.md`
  - `appendix_a_vocabulary.md`
  - `appendix_b_output_format.md`
  - `appendix_c_invariant_library.md`
  - `appendix_d_natural_sciences.md`
- `SA/SA_FULL/` — single-file Markdown manuscripts:
  - `Semantic_Algebra_Foundations_EN.md` — concise foundations
  - `Semantic_Algebra_Complete_Manuscript.md` — extended manuscript
  - `Semantic_Algebra_What_Language_Hides_UNIFIED.md` — unified compilation

## PA — Proportional Algebra

- `PA/README.md`
- `PA/START_HERE_PA.md`
- `PA/PA_BOOK/` — chapter-level Markdown (20 chapters + 4 appendices):
  - Part I — The Problem of the Absent Grammar:
    - `01_why_the_sciences_cannot_speak.md`
    - `02_the_principle_of_structural_isomorphism.md`
    - `03_what_is_needed.md`
  - Part II — The Proportional Space:
    - `04_the_proportional_space.md`
    - `05_the_resonance_metric.md`
    - `06_the_coherence_order.md`
    - `07_semantic_vectors_and_remir.md`
  - Part III — The Operators:
    - `08_collapse_operator.md`
    - `09_strip_and_recontextualisation.md`
    - `10_resonance_operator.md`
    - `11_extended_round_trip.md`
    - `12_pulsation_temporal_generator.md`
  - Part IV — Cross-Domain Applications:
    - `13_chemistry.md`
    - `14_language.md`
    - `15_emotion.md`
    - `16_medicine.md`
    - `17_artificial_intelligence.md`
  - Part V — Completion:
    - `18_limits_and_open_questions.md`
    - `19_relation_to_oct_ogt.md`
    - `20_epilogue.md`
  - Appendices:
    - `appendix_a_symbol_register.md`
    - `appendix_b_te_equations_in_pa.md`
    - `appendix_c_sa_pa_equivalences.md`
    - `appendix_d_bibliography.md`
- `PA/PA_FULL/` — single-file Markdown manuscript:
  - `Proportional_Algebra_Foundations_UNIFIED.md`
- `PA/pa_engine/` — Python reference engine:
  - `dynamics.py`
  - `ert_diagnostic.py`
  - `metric.py`
  - `operators.py`
  - `remir.py`
  - `simulation_orchestrator.py` (entry point)
  - `test_cases.py`

## Publication Notes

- The Markdown files in this repository are the **canonical public version**.
- LaTeX-ready projects (for Overleaf / KDP / Zenodo) exist privately and are not part of this public mirror.
- Italian source folders and internal research artifacts are excluded by `.gitignore` policy.
