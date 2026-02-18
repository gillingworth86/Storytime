# Storytime (Phase 1 Validation)

Storytime is currently a **landing-page-first validation project**.

- **Goal:** Validate demand before full product build.
- **Success target:** 100 email signups in 3 weeks.
- **Deployment:** Vercel (automatic Git-based deploys).
- **Current product surface:** `experimental/landing-pages/index.html`.

## Current State

For the canonical snapshot of what is active vs deprecated, read:

- [`docs/current-state.md`](docs/current-state.md)

## Quick Start

1. Install dependencies:
   ```bash
   npm install
   ```
2. Validate HTML:
   ```bash
   npm run validate:html
   ```
3. Check active docs for drift:
   ```bash
   npm run lint:docs-active
   ```
4. Serve the landing page locally:
   ```bash
   npm run serve:landing
   ```
5. Open `http://localhost:8000`.

## Development Workflow

1. Create a branch from `master`.
2. Make changes.
3. Run local quality checks:
   ```bash
   npm run validate:html
   npm run format:check
   npm run lint:docs-active
   ```
4. Open a PR.
5. Merge to `master` to trigger Vercel deployment.

## Active Documentation

- [`QUICKSTART.md`](QUICKSTART.md): Vercel-first setup and day-to-day workflow
- [`docs/project-state-evaluation-2026-02-18.md`](docs/project-state-evaluation-2026-02-18.md): latest evaluation
- [`docs/implementation-plan-2026-02-18.md`](docs/implementation-plan-2026-02-18.md): implementation plan derived from evaluation
- [`docs/backlog.md`](docs/backlog.md): mirrored planning backlog (GitHub Issues are canonical)
- [`docs/strategy/`](docs/strategy): strategy and GTM planning artifacts

## Commands

```bash
npm run validate:html      # Validate landing page HTML
npm run format:check       # Check HTML formatting
npm run format:fix         # Auto-fix HTML formatting
npm run serve:landing      # Serve landing page locally
npm run lighthouse         # Run Lighthouse against production
npm run lighthouse:local   # Run Lighthouse against local server
npm run lint:docs-active   # Fail on outdated platform references in active docs
```
