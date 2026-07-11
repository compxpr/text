# Contracts scaffold

This `contracts/` validation scaffold is generated from
[`codex/templates/contract-catalog-scaffold`](https://github.com/compxpr/codex/tree/main/templates/contract-catalog-scaffold),
a shared template extracted from this repo and `powershell-stuffing` (Wave 2
#11) after both had copy-pasted and independently drifted their own copies.

**Pinned template version:** `v1.0.0` (codex commit `7514cf4`, 2026-07-10)

## Generated -- do not hand-edit
These files are rendered from the shared template with this repo's own
placeholder values (`REPO_ID=text`, `OWNS_KIND=content`,
`MANIFEST_ID_PREFIX=text-repo`, etc. -- full table in the template's
`USAGE.md`). To change them, edit `codex/templates/contract-catalog-scaffold/`,
bump its version, then re-render here and update the pinned version above.
- `schemas/artifact.schema.json`
- `schemas/check.schema.json`
- `schemas/manifest.schema.json`
- `schemas/repo.schema.json`
- `schemas/service.schema.json`
- `tools/check.py`
- `tools/Validate-Contracts.ps1`

Each generated file also carries its own "GENERATED from ..." marker
(`$comment` in the JSON schemas, a header comment in the Python/PowerShell
files) as a second line of defense against accidental hand-editing.

## Repo-owned -- edit freely, never templated
- `decisions/0001-0004-*.md` -- this repo's own design-decision prose.
- `docs/service-integration.md`, `docs/content-contract.md`,
  `integrations/*.md` -- share a loose skeleton with `powershell-stuffing`'s
  copies but the content is genuinely repo-specific.
- `examples/*.yaml` -- real example data for this repo.
- `schemas/content_record.schema.json` -- this repo's own per-item schema
  (`powershell-stuffing`'s analog is `script.schema.json`; neither is part of
  the shared template).

## Validating
```
python contracts/tools/check.py
pwsh -NoProfile -File contracts/tools/Validate-Contracts.ps1
```
Both run in CI via `.github/workflows/contracts.yml`.
