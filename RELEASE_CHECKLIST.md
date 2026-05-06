# Release Checklist (GitHub)

Use this before each public release.

## Content

- [ ] Canonical files are listed in `INDEX.md`
- [ ] Legacy files (if any) are marked as reference-only
- [ ] No private session dump or working-only draft is included
- [ ] Version/date fields are coherent across `CHANGELOG.md`, `OBJECT_REGISTRY.md`, and corpus front-matter

## Consistency

- [ ] SA and PA chapter ordering is preserved
- [ ] PA `pa_engine/` imports resolve and `simulation_orchestrator.py` runs in a clean environment
- [ ] Cross-references between SA and PA appendices remain valid
- [ ] `ECOSYSTEM.md` cross-links to other repositories resolve

## Publication

- [ ] `README.md` links resolve
- [ ] License choice is intentional (CC BY-NC-SA 4.0)
- [ ] `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md` are present
- [ ] `SECURITY.md` policy is present
- [ ] `.github/` templates render correctly on GitHub

## Final sanity check

- [ ] Claims are framed as research and falsifiable, not as physical fact
- [ ] No statement implies proven cross-domain identity without round-trip / falsification evidence
- [ ] No author attribution other than Fabio Ghioni in front-matter (citations and bibliography excepted)
