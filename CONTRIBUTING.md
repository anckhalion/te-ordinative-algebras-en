# Contributing

Thanks for your interest in contributing to this project.

## Scope

This repository contains two distinct formal frameworks (SA and PA) and a small reference engine for PA. Contributions are welcome for:

- clarity and consistency improvements
- formal proofs, counterexamples, and invariant validation
- cross-domain test cases
- engine code review and reproducibility runs
- translation and editorial quality
- issue reproduction and version diffs

## Two Distinct Frameworks

SA and PA are independent projects bundled in the same repository for convenient cross-reference. When opening an issue or PR, indicate which framework you are addressing:

- `[SA]` Semantic Algebra
- `[PA]` Proportional Algebra
- `[engine]` PA reference engine
- `[meta]` repository governance / cross-framework

## Before You Open a PR

1. Read `README.md` and `INDEX.md`
2. For SA: read `SA/README.md` and the relevant `SA/SA_BOOK/` chapters
3. For PA: read `PA/README.md` and the relevant `PA/PA_BOOK/` chapters
4. Confirm whether the target file is canonical or legacy
5. Open an issue for significant structural or ontological changes

## Contribution Rules

- Keep released versioned files stable where possible
- Prefer additive updates over destructive rewrites
- Add clear rationale for any change in formal definitions
- Avoid ambiguous claims that imply proven physical truth without verification
- Use reproducible examples when proposing behavior claims

## Commit and PR Guidance

- One topic per PR
- Clear title format: `[SA|PA|engine|meta]: short summary`
- Include:
  - what changed
  - why
  - compatibility impact
  - validation method (round-trip, falsification test, cross-domain instance)

## Documentation Style

- Keep section numbering consistent with existing files
- Preserve the formal notation conventions defined in `SA/SA_BOOK/appendix_a_vocabulary.md` and `PA/PA_BOOK/appendix_a_symbol_register.md`
- Prefer explicit definitions over metaphor when possible
- For new invariants, follow the validation thresholds in `SA/SA_BOOK/05_the_library_of_invariants.md`
