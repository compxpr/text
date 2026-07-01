# Text Repository Contract

## Purpose

This contract defines content metadata, audience, source, validation, artifact, and handoff boundaries for reusable text assets.

## Core rule

This repo owns text content, content purpose, audience, source notes, revision status, examples, validation checks, and handoff records. Shared services may add metadata, package records, and review outputs, but they must not change content meaning silently.

## Required boundaries

- Content purpose stays explicit.
- Audience and intended use stay visible.
- Source notes and revision status remain traceable.
- Validation commands or review checks remain recorded.
- Artifacts and handoffs stay identifiable.
- Shared-service gaps produce fallback metadata.

## Completion principle

A text integration is not complete unless it preserves content ID, path, audience, purpose, source notes, revision status, validation checks, artifact inventory, fallback status, and limitations.
