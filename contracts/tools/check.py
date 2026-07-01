#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, RefResolver

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "contracts" / "schemas"
EXAMPLE_DIR = ROOT / "contracts" / "examples"

FILES = [
    "README.md",
    "AGENTS.md",
    ".github/workflows/contracts.yml",
    "PROJECT.md",
    "TEXT-CONTRACT.md",
    "CONTRACT-SPEC100.md",
    "CONTRACT-ROADMAP.md",
    "contract-requirements.txt",
    "content/sample.md",
    "contracts/schemas/manifest.schema.json",
    "contracts/schemas/repo.schema.json",
    "contracts/schemas/content_record.schema.json",
    "contracts/schemas/check.schema.json",
    "contracts/schemas/service.schema.json",
    "contracts/schemas/artifact.schema.json",
    "contracts/examples/manifest.yaml",
    "contracts/examples/artifact.yaml",
    "contracts/docs/service-integration.md",
    "contracts/docs/content-contract.md",
    "contracts/integrations/app-platform.md",
    "contracts/integrations/report-studio.md",
    "contracts/integrations/ai-policy.md",
    "contracts/integrations/fixture-lab.md",
    "contracts/decisions/0001-content-meaning-is-owned-here.md",
    "contracts/decisions/0002-review-status-remains-visible.md",
    "contracts/decisions/0003-audience-and-purpose-remain-explicit.md",
    "contracts/decisions/0004-service-packaging-does-not-change-content.md",
    "contracts/tools/check.py",
    "contracts/tools/Validate-Contracts.ps1",
]

EXAMPLES = {
    "contracts/examples/manifest.yaml": "contracts/schemas/manifest.schema.json",
    "contracts/examples/artifact.yaml": "contracts/schemas/artifact.schema.json",
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def stop(msg: str) -> None:
    print("ERROR: " + msg, file=sys.stderr)
    raise SystemExit(1)


def store() -> dict[str, Any]:
    result: dict[str, Any] = {}
    for path in sorted(SCHEMA_DIR.glob("*.schema.json")):
        schema = read_json(path)
        result[path.name] = schema
        result[str(path)] = schema
        if "$id" in schema:
            result[schema["$id"]] = schema
    return result


def validate_with_schema(example: str, schema: str) -> None:
    schema_obj = read_json(ROOT / schema)
    resolver = RefResolver.from_schema(schema_obj, store=store())
    validator = Draft202012Validator(schema_obj, resolver=resolver)
    data = read_yaml(ROOT / example)
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    if errors:
        stop(example + " -> " + errors[0].message)


def validate_manifest_contract() -> None:
    manifest = read_yaml(EXAMPLE_DIR / "manifest.yaml")
    repo = manifest.get("repo", {})
    if repo.get("local_first") is not True:
        stop("local_first must be true")
    if repo.get("owns_content") is not True:
        stop("owns_content must be true")

    records = manifest.get("records", [])
    if not records:
        stop("at least one content record is required")

    for record in records:
        content_id = record.get("content_id", "<missing content_id>")
        content_path = record.get("path")
        if not content_path:
            stop(f"{content_id}: content path required")
        if not (ROOT / content_path).exists():
            stop(f"{content_id}: content path does not exist: {content_path}")
        if not record.get("checks"):
            stop(f"{content_id}: content checks required")


def main() -> int:
    missing = [path for path in FILES if not (ROOT / path).exists()]
    if missing:
        stop("missing " + ", ".join(missing))

    for path in sorted(SCHEMA_DIR.glob("*.schema.json")):
        Draft202012Validator.check_schema(read_json(path))

    for example, schema in EXAMPLES.items():
        validate_with_schema(example, schema)

    validate_manifest_contract()

    print("Text repository contract validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
