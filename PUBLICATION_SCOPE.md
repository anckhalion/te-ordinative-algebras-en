# Publication Scope (te-ordinative-algebras-en)

Date: 2026-05-06

## Included

- Front-door files: `README.md`, `INDEX.md`, `START_HERE_FIRST_TIME.md`, `SIMPLE_GLOSSARY.md`, `SUPER_SIMPLE_FAQ.md`
- Governance: `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`
- Operational: `CHANGELOG.md`, `RELEASE_CHECKLIST.md`
- Discovery: `ECOSYSTEM.md`, `OBJECT_REGISTRY.md`, `object_registry.json`, `LOAD_PROFILES.md`
- `.github/` issue and PR templates
- `SA/` — Semantic Algebra full corpus:
  - `SA/README.md`, `SA/START_HERE_SA.md`
  - `SA/SA_BOOK/` — chapter-level Markdown files (Foundations + Complete Manuscript chapters and appendices)
  - `SA/SA_FULL/` — single-file Markdown manuscripts (Foundations EN, Complete Manuscript, What Language Hides UNIFIED)
- `PA/` — Proportional Algebra full corpus:
  - `PA/README.md`, `PA/START_HERE_PA.md`
  - `PA/PA_BOOK/` — chapter-level Markdown files (20 chapters + 4 appendices)
  - `PA/PA_FULL/` — single-file Markdown manuscript
  - `PA/pa_engine/` — Python reference engine for PA operations

## Excluded

- LaTeX projects (Overleaf-ready) — those live in private working directories and are not part of this public mirror; the public mirror is Markdown-only by design
- Session memory dumps and brainstorming drafts (excluded by `.gitignore` patterns: `SESSION_MEMORY_DUMP*.md`, `*_DRAFT*.md`, `notes_private/`, `**/not-to-release/`)
- Italian source folders, work-in-progress framework v6.x development paths, and other internal research artifacts

## Editorial Note

SA and PA are presented as **distinct frameworks** sharing a common publication channel. The structural relationship between them (PA Theorem 9.1: SA is the restriction of PA to the decoherent space `D`) is documented inside the corpus itself and does not collapse the two into a single project.

## Source-of-Truth

The Markdown files in this repository are the canonical public version. Any LaTeX or print edition is a derivative of these Markdown sources.
