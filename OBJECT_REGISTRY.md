# Object Registry

Canonical registry of project objects for publication, maintenance, and automated tooling.

## Lifecycle Legend

- `canonical`: active and recommended
- `legacy`: historical/reference only
- `private`: not for default public publication

## Objects

| Object ID | Type | Version | Lifecycle | File | Depends On |
|---|---|---|---|---|---|
| `SA-FOUNDATIONS-1.0` | manuscript | 1.0 | canonical | `SA/SA_FULL/Semantic_Algebra_Foundations_EN.md` | none |
| `SA-COMPLETE-1.0` | manuscript | 1.0 | canonical | `SA/SA_FULL/Semantic_Algebra_Complete_Manuscript.md` | `SA-FOUNDATIONS-1.0` |
| `SA-WHATLANGHIDES-1.1` | manuscript | 1.1 | canonical | `SA/SA_FULL/Semantic_Algebra_What_Language_Hides_UNIFIED.md` | `SA-FOUNDATIONS-1.0` |
| `SA-BOOK-CHAPTERS-1.0` | corpus | 1.0 | canonical | `SA/SA_BOOK/` | none |
| `PA-FOUNDATIONS-1.0` | manuscript | 1.0 | canonical | `PA/PA_FULL/Proportional_Algebra_Foundations_UNIFIED.md` | `SA-FOUNDATIONS-1.0` |
| `PA-BOOK-CHAPTERS-1.0` | corpus | 1.0 | canonical | `PA/PA_BOOK/` | none |
| `PA-ENGINE-1.0` | reference-engine | 1.0 | canonical | `PA/pa_engine/` | `PA-FOUNDATIONS-1.0` |

## Execution / Reading Graph

For a reader entering the project:

1. `SA-FOUNDATIONS-1.0` — operational entry point (concise foundations)
2. `SA-COMPLETE-1.0` or `SA-WHATLANGHIDES-1.1` — extended manuscript versions
3. `SA-BOOK-CHAPTERS-1.0` — chapter-level reading
4. `PA-FOUNDATIONS-1.0` — formal grounding
5. `PA-BOOK-CHAPTERS-1.0` — chapter-level reading
6. `PA-ENGINE-1.0` — runnable reference for PA operators

## Optimization Rules

- Keep one canonical object per type/version.
- Preserve legacy objects without editing unless critical fixes are needed.
- Never promote a private object to canonical without explicit maintainer decision.
- The chapter-level corpus (`SA-BOOK-CHAPTERS-1.0`, `PA-BOOK-CHAPTERS-1.0`) and the single-file manuscripts are kept in sync at each release; if they diverge, the chapter-level version is the source of truth.
