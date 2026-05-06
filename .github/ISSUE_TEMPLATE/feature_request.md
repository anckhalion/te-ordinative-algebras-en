---
name: Feature / framework proposal
about: Suggest a new invariant, operator extension, cross-domain test, or engine feature
title: '[proposal] '
labels: enhancement
---

## Scope

What kind of contribution is this?

- [ ] New invariant submission (SA library extension)
- [ ] Operator extension (SA or PA)
- [ ] New cross-domain demonstration
- [ ] Engine feature (`PA/pa_engine/`)
- [ ] Documentation / pedagogy improvement
- [ ] Other

## Motivation

Why is this useful? What gap does it close? What does it make possible that is currently impossible or awkward?

## Proposal

Describe the proposed change, with formal definitions where applicable.

## Validation plan

How will the proposal be tested?

- For new invariants: 3+ maximally distant domains, etymological strip applied, round-trip integrity verified.
- For operator extensions: falsifiability conditions, compatibility with existing operators.
- For engine features: unit-level test cases.

## Cross-references

Related issues, PRs, chapters, or external work.

## Compatibility

Will the proposal break existing canonical objects? If so, what is the migration path?
