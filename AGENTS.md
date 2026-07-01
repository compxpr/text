# Agent Instructions

## Mission

Text preserves reusable text assets, notes, snippets, templates, content metadata, validation records, artifacts, and handoff notes.

## Default behavior

- Keep the repo local-first.
- Do not introduce cloud calls.
- Do not store secrets, credentials, customer inventory, or support bundles.
- Do not add customer-identifying examples.
- Do not silently change content meaning while changing shared-service metadata.
- Preserve content ID, path, purpose, audience, source notes, review status, validation checks, artifacts, limitations, and fallback status.

## Required validation

Run this before handoff:

```powershell
pwsh -NoProfile -File .\contracts\tools\Validate-Contracts.ps1
```

Direct checker:

```powershell
python contracts\tools\check.py
```

## SPEC100 rule

For any SPEC100 task, produce a requirements traceability matrix and close every explicit and implied requirement individually.

Final handoff must include:

```text
SPEC100 unresolved_gaps=0
```

## Do not do

- Do not move this repo into another repo.
- Do not delete contract files without replacement validation.
- Do not add customer-identifying examples.
- Do not make AI or shared services the source of truth for content meaning.
