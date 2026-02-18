# Storytime Current State (Phase 1)

_Last updated: 2026-02-18_

This document defines the active project boundary to reduce onboarding and execution drift.

## Active Assets (Use These)

### Product + deployment
- Landing page implementation: `experimental/landing-pages/index.html`
- Legal pages: `experimental/landing-pages/privacy.html`, `experimental/landing-pages/terms.html`
- Deployment config: `vercel.json`
- Production deployment: Vercel Git integration

### Quality checks
- HTML validation + formatting checks via `package.json` scripts
- GitHub Actions quality workflow (`quality-checks.yml`)

### Planning + tracking
- **Canonical status source:** GitHub Issues
- Planning mirrors/snapshots: `docs/backlog.md`, `docs/prds/*`
- Evaluation + execution docs:
  - `docs/project-state-evaluation-2026-02-18.md`
  - `docs/implementation-plan-2026-02-18.md`

## Deprecated / Historical Assets (Reference Only)

- `netlify.toml`
- `netlify.toml.backup`
- `landing-page-ci-cd.yml` (deprecated/disabled workflow retained for rollback context)
- `IMPLEMENTATION-CHECKLIST.md` (historical implementation checklist)

## Source-of-Truth Policy

1. GitHub Issues own live status.
2. Markdown backlog/PRDs are planning snapshots and may lag.
3. Perform a lightweight weekly sync to keep snapshots aligned with Issues.
