# Ordinative Sciences Ecosystem Map

This file explains how the four public repositories of the Ordinative Sciences programme connect.

## Four Repositories, Four Roles

| Repository | Role | Function |
| --- | --- | --- |
| `ordinative_sciences_framework` | **Theory** | Defines the TE foundations, ontology, and full module architecture (Bootloader, Core, SVP, SCIMS, VERT, LENS, PPRO, OBSERVER). |
| `te-ordinative-lora` | **Practice** | Implements TE principles in model fine-tuning workflows; LoRA dataset and training pipeline. |
| `te-oct-framework-en` | **Validation** | Publishes the English mirror of the core framework, plus the OCT (Ordinative Category Theory) corpus with reproducibility assets and validation cycles. |
| `te-ordinative-algebras-en` | **Algebras** | Publishes the SA (Semantic Algebra) and PA (Proportional Algebra) frameworks — the analytical operators and the proportional space they live in. |

## Conceptual Flow

1. **Theory** (`ordinative_sciences_framework`) defines the principles.
2. **Practice** (`te-ordinative-lora`) applies the principles in training pipelines.
3. **Validation** (`te-oct-framework-en`) documents and tests formal/empirical consistency through OCT.
4. **Algebras** (`te-ordinative-algebras-en`, this repo) provides the formal operator-level grammar — the analytical tools that connect theory, practice, and validation.

The four repositories are not redundant. Each addresses a distinct layer of the same underlying programme.

## ASCII Map

```text
                    ORDINATIVE SCIENCES ECOSYSTEM
                              |
      ----------------------------------------------------------
      |                |                  |                    |
      v                v                  v                    v
   THEORY           PRACTICE          VALIDATION             ALGEBRAS
   ordinative_      te-ordinative-    te-oct-                te-ordinative-
   sciences_        lora              framework-en           algebras-en
   framework
      |                |                  |                    |
      |                | <---- trains --- |                    |
      | <--- defines - |                  |                    |
      |                |                  | <--- formalises -- |
      | ----- provides invariants ------> |                    |
      |                                                        |
      | ---------------- analytical grammar --------------- >  |
```

## How the Algebras Repository Relates

- **To Theory**: SA and PA operate on the structures defined by the TE framework. The Collapse Function `E = Φ(C, I, K)` (TE equation 1.1) is upgraded in PA to a formal algebraic operator with falsifiable properties.
- **To Practice**: The SA invariant library and the operators (S, π) are the structural primitives that the LoRA training pipeline aims to teach a model to recognise and apply.
- **To Validation**: PA's Extended Round-Trip and falsification criteria provide the structural-test layer that complements OCT's category-theoretic validation cycles.

## Suggested Reading Order

For a complete tour of the ecosystem:

1. `ordinative_sciences_framework` — read the Bootloader and Core to understand the foundations.
2. `te-ordinative-algebras-en` (this repo) — read SA first (operational entry), then PA (formal grounding).
3. `te-oct-framework-en` — read OCT for the category-theoretic and validation-cycle layer.
4. `te-ordinative-lora` — read the dataset and training pipeline to see the practical implementation.

For first-time readers of this repository specifically, start with `START_HERE_FIRST_TIME.md`.
