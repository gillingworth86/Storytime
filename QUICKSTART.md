# 🚀 Storytime Quick Start (Vercel)

This quick start covers the **current** Phase 1 flow: static landing page + Vercel deployment + quality checks.

## 1) Local setup

```bash
npm install
npm run validate:html
npm run format:check
npm run lint:docs-active
```

## 2) Run locally

```bash
npm run serve:landing
```

Open: `http://localhost:8000`

## 3) Make and validate changes

```bash
git checkout -b feature/your-change
# edit files
npm run validate:html
npm run format:check
npm run lint:docs-active
git add .
git commit -m "feat: describe change"
git push origin feature/your-change
```

## 4) Open and merge PR

- Open PR to `master`.
- Ensure quality checks pass.
- Merge PR.
- Vercel deploys automatically from GitHub integration.

## 5) Production checks

- Confirm deployment in Vercel dashboard.
- Run Lighthouse if needed:
  ```bash
  npm run lighthouse
  ```

---

## Important links

- Repository: https://github.com/gillingworth86/Storytime
- GitHub Actions: https://github.com/gillingworth86/Storytime/actions
- Vercel Dashboard: https://vercel.com/dashboard
- Current state doc: [`docs/current-state.md`](docs/current-state.md)

---

## Note on legacy docs

Some files are intentionally retained as historical references (for rollback/context). Use `docs/current-state.md` to distinguish active vs deprecated assets.
