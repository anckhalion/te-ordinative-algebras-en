# Start Here (First Time)

This guide is written for people with zero background.
No technical knowledge is required.

## In One Sentence

This repository contains two distinct formal frameworks — Semantic Algebra (SA) and Proportional Algebra (PA) — that come from the Technology of Expressions research programme. They give you tools to extract, classify, and re-express structural patterns across any field.

## If You Have 5 Minutes

1. Read `README.md` (what is in the repository).
2. Read `SIMPLE_GLOSSARY.md` (plain words for the key terms).
3. Read `SUPER_SIMPLE_FAQ.md` (short answers to common confusion).

## If You Have 20 Minutes

1. Read `README.md`.
2. Open `SA/README.md` and `SA/START_HERE_SA.md`.
3. Read `SA/SA_BOOK/00_prologue.md` and `SA/SA_BOOK/01_the_lossy_channel.md`.
4. Then look at the operators: `SA/SA_BOOK/06_the_strip_operator.md`.

## If You Want the Formal Theory

1. Read `PA/README.md` and `PA/START_HERE_PA.md`.
2. Read `PA/PA_BOOK/01_why_the_sciences_cannot_speak.md` through `PA/PA_BOOK/03_what_is_needed.md` for motivation.
3. Read `PA/PA_BOOK/04_the_proportional_space.md` for the formal space definition.
4. Read `PA/PA_BOOK/08_collapse_operator.md`, `09_strip_and_recontextualisation.md`, and `10_resonance_operator.md` for the three operators.
5. Read `PA/PA_BOOK/11_extended_round_trip.md` for the integrity test.

## If You Want Validation Evidence

- SA positive validation (7-text experiment): `SA/SA_BOOK/08_the_seven_text_experiment.md`
- SA negative validation (discrimination): `SA/SA_BOOK/09_the_discrimination_test.md`
- SA self-correction case study (Ungaretti): `SA/SA_BOOK/10_the_self_correction.md`
- PA cross-domain demonstrations: `PA/PA_BOOK/13_chemistry.md` to `PA/PA_BOOK/17_artificial_intelligence.md`
- PA falsification criteria: `PA/PA_BOOK/18_limits_and_open_questions.md`

## If You Want to Run Code

The PA reference engine is in `PA/pa_engine/`. It is a small Python package (~700 lines) implementing the resonance metric, the Remir structure, the collapse and strip operators, and a simulation orchestrator.

Entry script: `PA/pa_engine/simulation_orchestrator.py`.

The engine is for experimentation — not production software.

## Do Not Confuse This Project With

1. A "theory of everything" that claims cross-domain unity without falsification — both frameworks include explicit falsification criteria.
2. A finished AI product — this is research material, including reference code, not a deployed system.
3. A purely philosophical text — both frameworks contain operational procedures and replicable tests.
4. A medical or biological project — `PA/PA_BOOK/16_medicine.md` discusses medicine as a domain of application, not as a clinical recommendation.

## If You Feel Lost

Use this recovery path:
1. Return to `README.md`.
2. Read `SIMPLE_GLOSSARY.md`.
3. Read `INDEX.md` and follow only one section at a time.

## Two Frameworks, One Repository

This repository deliberately bundles SA and PA in the same place because the cross-references between them are tight. They remain **distinct projects** — not two halves of one — and each can be read on its own. See `ECOSYSTEM.md` for how they relate to the other repositories in the Ordinative Sciences programme.
