# Launcher shell adoption

text is currently headless (no browser UI), so the WWT launcher shell does
not apply yet. This file records how to adopt it if text ever gains a UI.

Template location: `codex/templates/launcher-shell/`
- `tokens.css` — dark-default design tokens (brand #0086ea; green=ok, red=problem only)
- `shell-spec.md` — framework-agnostic layout spec (sidebar, header, hero, app grid, right rail, footer, background)
- `USAGE.md` — adoption steps (React drop-in via @wwt-launcher/design-system, or non-React via the spec)

Status: spec-only (no shell code applied — this app has no shell to reskin).
Chrome only — adopting the shell must never change functionality, routes, or data.
