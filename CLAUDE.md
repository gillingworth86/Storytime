# CLAUDE.md - Storytime Project Guide

This file provides guidance to Claude Code when working with this repository.

## Project Overview

**Storytime** is a landing page validation project for personalized bedtime stories with a persistent story universe.

**Current Phase:** Phase 1 - Landing page validation
**Goal:** Collect 100 email signups in 3 weeks
**Tech Stack:** Static HTML landing page, deployed to Vercel (migrated from Netlify 2026-01-24)

## Repository Structure

```
Storytime/
├── experimental/landing-pages/  # Phase 1: Landing page HTML
│   └── index.html
├── app/                          # Phase 2: Full app (future)
├── docs/                         # Marketing and strategy docs
├── .github/workflows/            # CI/CD automation
└── .claude/                      # Claude-specific guides
```

## Important Conventions

### Git Configuration
- **Branch name:** `master` (not main)
- **Remote:** origin (GitHub: gillingworth86/Storytime)

### Deployment
- **Platform:** Vercel (native Git integration)
- **Production URL:** https://getstorytime.vercel.app
- **Deployment:** Automatic on push to `master` branch
- **Preview URLs:** Automatic for all PRs and branches
- **Configuration:** `vercel.json` (headers, redirects, security settings)

**Legacy Netlify Setup (Preserved):**
- Backup files: `netlify.toml.backup`, `.github/workflows/landing-page-ci-cd.yml.backup`
- Git tag: `netlify-backup` (restore point if needed)
- Old URL: https://getstorytime.netlify.app (will be deprecated)

### CI/CD Pipeline
- **Workflow:** `.github/workflows/quality-checks.yml`
- **Purpose:** Quality checks only (Vercel handles deployment automatically)
- **Triggers:** Push to `master` or PRs affecting `experimental/landing-pages/**`
- **Jobs:**
  - HTML validation (`html-validate`)
  - Security scanning (`trivy`)
  - Lighthouse performance audit (on master push only, after Vercel deploys)
- **Build minutes usage:** ~50 minutes/month (well under GitHub's free tier)

## CI/CD Implementation Guidelines

**⚠️ IMPORTANT:** When implementing or modifying CI/CD pipelines, always follow the guide at:
👉 `.claude/cicd-implementation-guide.md`

**Key principles:**
1. **Discovery first:** Check actual state before making assumptions
2. **Start minimal:** Get basic workflow running before adding features
3. **Iterate incrementally:** Add one feature at a time, test each
4. **Let errors guide:** Don't predict all issues upfront

**Common gotchas for this project:**
- Branch is `master`, not `main`
- No `package-lock.json` exists (don't add npm cache)
- Deployment is handled by Vercel (not GitHub Actions)
- HTML validation rules are intentionally lenient
- Lighthouse audit URL needs updating after first Vercel deployment

## Development Commands

```bash
# Validate HTML locally
npx html-validate experimental/landing-pages/*.html

# Start local server
cd experimental/landing-pages && python -m http.server 8000

# Deploy to Vercel
git push origin master
# Vercel automatically deploys on push (no manual trigger needed)

# Trigger quality checks workflow manually
git commit --allow-empty -m "trigger: test quality checks"
git push origin master
```

## Phase Transition Notes

### Phase 1 (Current): Landing Page
- Focus: Validation and signup collection
- No build process required (static HTML)
- CI/CD focuses on validation and deployment

### Phase 2 (Future): Full Application
- Will activate `.github/workflows/app-ci-cd.yml`
- Will add testing, building, staging environments
- Update this file when transitioning

## External Services

### Vercel (Current Deployment)
- Account: Connect via GitHub (gillingworth86)
- Configuration: `vercel.json`
- Deployment: Native Git integration (automatic)
- Build minutes: 6,000/month free tier
- Dashboard: https://vercel.com/dashboard

### Netlify (Deprecated - Legacy)
- Status: Migrated to Vercel 2026-01-24
- Reason: Build minute limits (300/month) exhausted
- Backup: Config preserved in `netlify.toml.backup`
- Restore: Use git tag `netlify-backup` if rollback needed

### Analytics (Future)
- Plausible: Not yet configured
- Instructions in `vercel.json` CSP headers

### Email (Future)
- Buttondown: Not yet configured
- Will need CSP updates in `vercel.json`

## Troubleshooting

### Quality checks workflow fails
- Check `.github/workflows/quality-checks.yml` paths filter
- Verify HTML validation rules in `.htmlvalidate.json`
- Security scan failures are set to `continue-on-error: true`

### HTML validation errors
- Rules are in `.htmlvalidate.json`
- Rules are intentionally lenient for existing HTML
- Don't make stricter without fixing HTML first

### Vercel deployment fails
- Check Vercel dashboard: https://vercel.com/dashboard
- Verify `vercel.json` configuration is valid
- Ensure output directory is `experimental/landing-pages`
- Check Vercel project settings for correct branch

### Lighthouse audit fails
- Update the production URL in `.github/workflows/quality-checks.yml`
- Ensure Vercel deployment completed before Lighthouse runs
- Wait time is set to 60 seconds (may need adjustment)

### Need to rollback to Netlify
```bash
git checkout netlify-backup
mv netlify.toml.backup netlify.toml
mv .github/workflows/landing-page-ci-cd.yml.backup .github/workflows/landing-page-ci-cd.yml
rm vercel.json
git add . && git commit -m "rollback: Restore Netlify deployment"
```

## Resources

- **Detailed setup:** `.github/SETUP.md`
- **Quick start:** `QUICKSTART.md`
- **Implementation checklist:** `IMPLEMENTATION-CHECKLIST.md`
- **CI/CD guide:** `.claude/cicd-implementation-guide.md`
- **GitHub Actions:** https://github.com/gillingworth86/Storytime/actions
- **Vercel Dashboard:** https://vercel.com/dashboard
- **Migration docs:** `VERCEL-MIGRATION.md` (rollback instructions)

---

**Last Updated:** 2026-01-24 (Vercel migration)
**Maintained by:** gillingworth86
