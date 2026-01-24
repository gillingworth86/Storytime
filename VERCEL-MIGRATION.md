# Vercel Migration Guide

**Migration Date:** 2026-01-24
**Reason:** Netlify build minute limits exhausted (300/month)
**Solution:** Migrate to Vercel (6,000 build minutes/month free tier)

---

## What Changed

### 1. Deployment Platform
- **Before:** Netlify (via GitHub Actions)
- **After:** Vercel (native Git integration)
- **Impact:** Automatic deployments on push, 20x more build minutes

### 2. CI/CD Workflow
- **Before:** `.github/workflows/landing-page-ci-cd.yml` (quality checks + deployment)
- **After:** `.github/workflows/quality-checks.yml` (quality checks only)
- **Impact:** GitHub Actions only runs tests, not deployment (~50 min/month vs ~300 min/month)

### 3. Configuration Files
- **Added:** `vercel.json` (headers, redirects, security settings)
- **Preserved:** `netlify.toml.backup`, `landing-page-ci-cd.yml.backup`
- **Removed:** `netlify.toml` (active), `landing-page-ci-cd.yml` (active)

---

## Setup Instructions (Manual Steps Required)

### Step 1: Connect Vercel to GitHub

1. Go to https://vercel.com
2. Sign up or log in using your GitHub account (gillingworth86)
3. Click **"Add New..."** → **"Project"**
4. Import `gillingworth86/Storytime`

### Step 2: Configure Vercel Project

**Build & Development Settings:**
```
Framework Preset: Other
Root Directory: ./
Build Command: (leave empty - static site)
Output Directory: experimental/landing-pages
Install Command: (leave empty)
```

**Git Settings:**
```
Production Branch: master
```

### Step 3: Deploy

1. Click **"Deploy"**
2. Wait for first deployment to complete
3. Copy the production URL (e.g., `https://storytime-abc123.vercel.app`)

### Step 4: Update Configuration

After first deployment, update these files:

**1. `.github/workflows/quality-checks.yml` (Line 72)**
```yaml
urls: |
  https://your-actual-vercel-url.vercel.app
```

**2. `CLAUDE.md` (Line 35)**
```markdown
- **Production URL:** https://your-actual-vercel-url.vercel.app
```

**3. (Optional) Add custom domain in Vercel dashboard**

---

## What's Preserved

All Netlify configuration is safely backed up:

### Backup Files
- `netlify.toml.backup` - Original Netlify configuration
- `.github/workflows/landing-page-ci-cd.yml.backup` - Original CI/CD workflow

### Git Tag
```bash
git tag -l netlify-backup
# Shows: netlify-backup (Backup of Netlify configuration before Vercel migration)
```

### Restore Point
```bash
git show netlify-backup:netlify.toml  # View original config
git show netlify-backup:.github/workflows/landing-page-ci-cd.yml  # View original workflow
```

---

## Rollback Instructions

If you need to revert to Netlify:

### Quick Rollback (Reset to Netlify)
```bash
# Checkout the backup tag
git checkout netlify-backup

# Or restore specific files
git checkout netlify-backup -- netlify.toml
git checkout netlify-backup -- .github/workflows/landing-page-ci-cd.yml

# Remove Vercel config
rm vercel.json
rm .github/workflows/quality-checks.yml

# Commit and push
git add .
git commit -m "rollback: Restore Netlify deployment"
git push origin master
```

### Manual Rollback (Copy from Backups)
```bash
# Restore from backup files
cp netlify.toml.backup netlify.toml
cp .github/workflows/landing-page-ci-cd.yml.backup .github/workflows/landing-page-ci-cd.yml

# Remove Vercel files
rm vercel.json
rm .github/workflows/quality-checks.yml

# Commit and push
git add .
git commit -m "rollback: Restore Netlify deployment from backups"
git push origin master
```

### Cleanup After Rollback
```bash
# Remove backup files (optional)
rm netlify.toml.backup
rm .github/workflows/landing-page-ci-cd.yml.backup

# Keep git tag for history
git tag -l  # netlify-backup will remain
```

---

## Vercel vs Netlify Comparison

| Feature | Netlify (Free) | Vercel (Free) |
|---------|----------------|---------------|
| Build minutes | 300/month | 6,000/month |
| Bandwidth | 100 GB/month | 100 GB/month |
| Deployments | Unlimited | Unlimited |
| Preview deploys | Yes (free) | Yes (free) |
| Custom domains | 1 | Unlimited |
| Edge functions | 125k/month | 100k/month |

**Winner for our use case:** Vercel (20x more build minutes)

---

## Quality Checks Retained

The new workflow (`.github/workflows/quality-checks.yml`) still runs:

✅ **HTML Validation** (html-validate)
✅ **Security Scanning** (Trivy)
✅ **Lighthouse Performance Audit** (on production only)

**What's removed:**
- ❌ Deployment job (Vercel handles this)
- ❌ Post-deployment smoke tests (can be added back if needed)

**Estimated build minutes:** ~50 minutes/month (vs Netlify's ~300 min/month)

---

## Troubleshooting

### Vercel deployment fails
**Check:**
1. Vercel dashboard for error logs
2. `vercel.json` syntax (JSON must be valid)
3. Output directory: `experimental/landing-pages` exists
4. Branch name: `master` (not `main`)

### Lighthouse audit fails
**Fix:**
1. Update production URL in `.github/workflows/quality-checks.yml`
2. Increase wait time (currently 60 seconds)
3. Verify Vercel deployment completed successfully

### Need help
- **Vercel docs:** https://vercel.com/docs
- **Vercel support:** https://vercel.com/support
- **GitHub Actions logs:** https://github.com/gillingworth86/Storytime/actions

---

## Next Steps After Migration

1. ✅ Connect Vercel to GitHub (manual)
2. ✅ Deploy first version
3. ✅ Update Lighthouse URL in workflow
4. ✅ Update CLAUDE.md with production URL
5. ⏳ Test a few commits to verify automatic deployment
6. ⏳ Monitor Vercel build minutes usage
7. ⏳ (Optional) Add custom domain in Vercel
8. ⏳ (Optional) Re-enable Plausible analytics
9. ⏳ (Optional) Add post-deployment smoke tests

---

**Migration completed by:** Claude Code
**Git tag for restore:** `netlify-backup`
**Questions?** Check Vercel dashboard or GitHub Actions logs first.
