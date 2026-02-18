# Implementation Plan: Project State Recommendations (2026-02-18)

This plan operationalizes the recommendations from `docs/project-state-evaluation-2026-02-18.md`.

## Scope
- Align active onboarding docs with the current Vercel-first deployment model.
- Reduce status drift by clarifying GitHub Issues as the canonical source.
- Close validation gaps by adding legal pages referenced in config and UI.
- Add a lightweight docs drift check for outdated platform references.

## Workstreams

### 1) Documentation consolidation (P0)
1. Update `README.md` with:
   - Vercel-first setup and workflow.
   - Links to active strategy docs under `docs/strategy/*`.
   - A pointer to a new current-state reference doc.
2. Rewrite `QUICKSTART.md` as Vercel-first quick onboarding.
3. Add `docs/current-state.md` to explicitly list:
   - Active assets/workflows.
   - Deprecated/historical assets.
4. Mark `IMPLEMENTATION-CHECKLIST.md` as historical and point contributors to active docs.

### 2) Single source of truth for status (P0)
1. Update `docs/backlog.md` to explicitly state:
   - GitHub Issues are canonical status.
   - Backlog/PRDs are mirrored planning snapshots.
2. Add a lightweight weekly sync cadence note to keep docs aligned with Issues.

### 3) Validation hardening (P1)
1. Add `experimental/landing-pages/privacy.html`.
2. Add `experimental/landing-pages/terms.html`.
3. Update landing page footer links to route to `/privacy` and `/terms`.
4. Update `vercel.json` redirects to map `/privacy` and `/terms` to the new files.

### 4) Drift prevention guardrail (P1)
1. Add npm script `lint:docs-active` in `package.json`.
2. Check active onboarding docs (`README.md`, `QUICKSTART.md`) for outdated `Netlify` references.
3. Integrate command in local validation guidance.

## Validation Plan
- `npm run validate:html`
- `npm run lint:docs-active`
- `npm run format:check`

## Definition of Done
- Active docs are Vercel-first and internally consistent.
- Current-state/deprecated boundaries are documented.
- Privacy and terms pages exist and are reachable from footer + redirects.
- Drift check fails if Netlify references return to active onboarding docs.
