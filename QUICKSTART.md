# 🚀 Storytime CI/CD Quick Start

Get your landing page deployed with automated CI/CD in under 15 minutes!

---

## ⚡ 5-Minute Setup

### 1. Create Netlify Site (3 minutes)

```
1. Go to: https://app.netlify.com/
2. Login with GitHub (gillingworth86 account)
3. Click "Add new site" → "Import an existing project"
4. Select "Storytime" repository
5. Configure:
   - Publish directory: experimental/landing-pages
   - Build command: echo 'Static site'
6. Click "Deploy site"
7. Copy your Site ID (in Site Settings)
```

### 2. Get Netlify Token (1 minute)

```
1. User Settings → Applications
2. New access token
3. Name: "Storytime CI/CD"
4. Generate → COPY TOKEN (save it!)
```

### 3. Add GitHub Secrets (2 minutes)

```
1. Go to: https://github.com/gillingworth86/Storytime/settings/secrets/actions
2. New repository secret:
   - Name: NETLIFY_AUTH_TOKEN
   - Value: [paste token]
3. New repository secret:
   - Name: NETLIFY_SITE_ID
   - Value: [paste site ID]
```

### 4. Commit & Push (1 minute)

```bash
cd c:\Dev\Storytime
git add .github/ netlify.toml
git commit -m "ci: add automated deployment pipeline"
git push origin master
```

### 5. Watch It Deploy! (2 minutes)

```
1. Go to: https://github.com/gillingworth86/Storytime/actions
2. Watch "Landing Page CI/CD" run
3. Visit your deployed site! 🎉
```

---

## 🔄 Daily Workflow

### Making Changes

```bash
# 1. Create feature branch
git checkout -b feature/update-headline

# 2. Edit landing page
# Edit experimental/landing-pages/index.html

# 3. Commit and push
git add .
git commit -m "feat: update hero headline"
git push origin feature/update-headline

# 4. Create PR on GitHub
# - Preview deployment will be created automatically
# - Review the preview URL posted in the PR comments

# 5. Merge PR
# - Production deployment happens automatically
```

---

## 📊 What Gets Automated

### On Every Push to Main:
✅ HTML validation
✅ Lighthouse performance audit (90+ score required)
✅ Security vulnerability scanning
✅ Deploy to production (getstorytime.com)
✅ Smoke tests to verify deployment

### On Every Pull Request:
✅ All quality checks
✅ Preview deployment with unique URL
✅ Comment on PR with preview link

---

## 🛠 Useful Commands

### Test HTML Locally
```bash
npx html-validate experimental/landing-pages/*.html
```

### Run Local Server
```bash
# Option 1: Python
cd experimental/landing-pages
python -m http.server 8000

# Option 2: Node.js
npx http-server experimental/landing-pages -p 8000

# Visit: http://localhost:8000
```

### Check Site Performance
```bash
npx lighthouse https://getstorytime.com --view
```

---

## 📍 Important URLs

| Purpose | URL |
|---------|-----|
| GitHub Repository | https://github.com/gillingworth86/Storytime |
| GitHub Actions | https://github.com/gillingworth86/Storytime/actions |
| Netlify Dashboard | https://app.netlify.com/ |
| Production Site | https://getstorytime.com (or your Netlify URL) |
| Detailed Setup Guide | [.github/SETUP.md](.github/SETUP.md) |

---

## 🔮 Next Steps After Landing Page Launch

### Phase 1: Validation (Current)
- [x] CI/CD automation set up
- [ ] Add Plausible analytics
- [ ] Add Buttondown email forms
- [ ] Launch to target communities
- [ ] Track signups

### Phase 2: Full App (Future)
- [ ] Set up separate `app/` CI/CD workflow
- [ ] Add automated testing
- [ ] Add staging environment
- [ ] Add database migrations
- [ ] Add backend deployment

---

## 🆘 Common Issues

**Problem:** Workflow fails with "NETLIFY_AUTH_TOKEN not set"
**Solution:** Check secret name is exactly `NETLIFY_AUTH_TOKEN` (case-sensitive)

**Problem:** "Publish directory not found"
**Solution:** Verify `netlify.toml` has `publish = "experimental/landing-pages"`

**Problem:** Lighthouse score too low
**Solution:** Review Lighthouse report in Actions tab for specific recommendations

**Problem:** Preview deployment not showing in PR
**Solution:** Check that PR is from a branch (not a fork) in the same repository

---

## ✅ Success Indicators

You'll know everything is working when:

1. ✅ GitHub Actions badge shows green
2. ✅ Netlify shows "Published" status
3. ✅ Your landing page loads at production URL
4. ✅ PR comments include preview deployment links
5. ✅ Lighthouse scores 90+ on all metrics

---

**Ready to deploy? Follow the 5-Minute Setup above!** 🚀

For detailed configuration and troubleshooting, see [.github/SETUP.md](.github/SETUP.md)
