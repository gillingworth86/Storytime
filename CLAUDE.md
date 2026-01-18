# CLAUDE.md - Storytime Project Guide

This file provides guidance to Claude Code when working with this repository.

## Project Overview

**Storytime** is a landing page validation project for personalized bedtime stories with a persistent story universe.

**Current Phase:** Phase 1 - Landing page validation
**Goal:** Collect 100 email signups in 3 weeks
**Tech Stack:** Static HTML landing page, deployed to Netlify

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
- **Platform:** Netlify
- **Production URL:** https://getstorytime.netlify.app
- **Netlify secrets configured:** Yes (NETLIFY_AUTH_TOKEN, NETLIFY_SITE_ID)

### CI/CD Pipeline
- **Workflow:** `.github/workflows/landing-page-ci-cd.yml`
- **Triggers:** Changes to `experimental/landing-pages/**`, `.htmlvalidate.json`, or workflow file
- **Jobs:** quality-check → deploy-netlify → lighthouse-audit → post-deployment-tests

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
- URL is `https://getstorytime.netlify.app` (not custom domain)
- HTML validation rules are intentionally lenient
- Lighthouse runs after deployment, not before

## Development Commands

```bash
# Validate HTML locally
npx html-validate experimental/landing-pages/*.html

# Start local server
cd experimental/landing-pages && python -m http.server 8000

# Trigger CI/CD
git commit --allow-empty -m "trigger: test pipeline"
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

### Netlify
- Account: gillingworth86 GitHub account
- Site ID: Stored in GitHub secrets
- Auth token: Stored in GitHub secrets

### Analytics (Future)
- Plausible: Not yet configured
- Instructions in `netlify.toml` comments

### Email (Future)
- Buttondown: Not yet configured
- Instructions in `netlify.toml` comments

## Troubleshooting

### Workflow fails on push
- Check `.github/workflows/landing-page-ci-cd.yml` paths filter
- Verify secrets are configured in GitHub

### HTML validation errors
- Rules are in `.htmlvalidate.json`
- Rules are intentionally lenient for existing HTML
- Don't make stricter without fixing HTML first

### Deployment fails
- Check Netlify secrets: NETLIFY_AUTH_TOKEN, NETLIFY_SITE_ID
- Verify publish directory: `experimental/landing-pages`

## Resources

- **Detailed setup:** `.github/SETUP.md`
- **Quick start:** `QUICKSTART.md`
- **Implementation checklist:** `IMPLEMENTATION-CHECKLIST.md`
- **CI/CD guide:** `.claude/cicd-implementation-guide.md`
- **GitHub Actions:** https://github.com/gillingworth86/Storytime/actions
- **Netlify Dashboard:** https://app.netlify.com/

---

**Last Updated:** 2026-01-18
**Maintained by:** gillingworth86
