# Text

Text is a local-first content utility repository for reusable text assets, notes, snippets, templates, and handoff records.

The repo's job is to preserve content purpose, audience, source notes, revision status, validation checks, artifact records, and handoff notes so reusable text can be managed safely across personal, engineering, and documentation workflows.

## Status

Current status: contract foundation present; initial reusable content catalog record populated.

This repo is active. It defines the contract model and validation surface for future text/content records.

## Core rule

This repository owns text records, content metadata, validation records, examples, and handoff notes.

Shared WWT suite services may add metadata, packaging, reporting, and fixture coverage, but they must not silently change content meaning.

## What belongs here

- Reusable text assets
- Notes, snippets, and templates
- Content metadata and manifests
- Audience and intended-use records
- Source notes and revision status
- Review or validation checks
- Artifact and handoff records
- Known limitations and fallback status

## What does not belong here

- Customer secrets
- Raw customer support bundles
- Unredacted credential files
- Customer-identifying examples
- Product-specific analysis engines
- Shared suite platform contracts that belong in other WWT repos

## Repository layout

```text
.
├── AGENTS.md
├── CONTRACT-ROADMAP.md
├── CONTRACT-SPEC100.md
├── PROJECT.md
├── TEXT-CONTRACT.md
├── contract-requirements.txt
├── content/
│   └── sample.md
├── contracts/
│   ├── decisions/
│   ├── docs/
│   ├── examples/
│   ├── integrations/
│   ├── schemas/
│   └── tools/
└── .github/
    └── workflows/
```

## Validate

### PowerShell wrapper

```powershell
pwsh -NoProfile -File .\contracts\tools\Validate-Contracts.ps1
```

To rebuild the local validation virtual environment:

```powershell
pwsh -NoProfile -File .\contracts\tools\Validate-Contracts.ps1 -RecreateVenv
```

### Direct Python command

```powershell
python -m venv .venv-contracts
.\.venv-contracts\Scripts\python.exe -m pip install -r contract-requirements.txt
.\.venv-contracts\Scripts\python.exe contracts\tools\check.py
```

On non-Windows shells, use `.venv-contracts/bin/python`.

## Validation scope

The contract checker verifies:

- required operating files exist
- JSON schemas are valid
- example manifests validate against schemas
- content records include paths and checks
- referenced content paths exist
- repo contract flags remain explicit

## SPEC100 closure

For substantial changes, include proof for:

- content metadata impact
- audience impact
- review impact
- artifact impact
- fixture impact
- validation commands run
- final line: `SPEC100 unresolved_gaps=0`

## Related shared-suite repos

- `wwt-app-platform`
- `wwt-report-studio`
- `wwt-source-registry`
- `wwt-ai-policy`
- `wwt-fixture-lab`

## Current next work

1. Add additional real reusable content records.
2. Expand validation evidence beyond the initial handoff template record.
3. Add report package export.
4. Add content fixture coverage.
5. Track validation evidence for every content record added.
