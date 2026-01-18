# 🤖 Storytime CI/CD Automation

**Complete automated deployment pipeline for your landing page and future application**

---

## 📖 What You Have Now

A **production-ready CI/CD pipeline** that automatically:

### ✅ On Every Code Change
- Validates HTML structure and quality
- Runs Lighthouse performance audits (requires 90+ scores)
- Scans for security vulnerabilities
- Creates preview deployments for pull requests
- Deploys to production when merged to master
- Runs post-deployment smoke tests
- Reports all results in GitHub

### 🚀 Deployment Flow

```
Your Change → GitHub Push → Automated Tests → Deploy → Verify → Done!
```

**Preview Deployments:** Every PR gets its own URL to review before merging
**Production Deployments:** Automatic on merge to master branch
**Zero Downtime:** Netlify handles traffic switching seamlessly

---

## 🗂 What Was Created

### Workflow Files
```
.github/
├── workflows/
│   ├── landing-page-ci-cd.yml    # Phase 1: Landing page automation (ACTIVE)
│   └── app-ci-cd.yml              # Phase 2: Full app automation (for future)
├── lighthouserc.json              # Performance budget configuration
└── SETUP.md                        # Detailed setup instructions
```

### Configuration Files
```
netlify.toml                        # Netlify deployment configuration
.htmlvalidate.json                  # HTML validation rules
QUICKSTART.md                       # 5-minute setup guide
IMPLEMENTATION-CHECKLIST.md         # Track your progress
CI-CD-README.md                     # This file
```

---

## ⚡ Quick Start

### Option 1: Follow the 5-Minute Setup
**Fastest way to get deployed:**
👉 See [QUICKSTART.md](QUICKSTART.md)

### Option 2: Detailed Setup
**For comprehensive understanding:**
👉 See [.github/SETUP.md](.github/SETUP.md)

### Option 3: Track Your Progress
**Use the checklist:**
👉 See [IMPLEMENTATION-CHECKLIST.md](IMPLEMENTATION-CHECKLIST.md)

---

## 🎯 Current Phase: Landing Page (Phase 1)

### What's Automated:
✅ HTML validation
✅ Performance monitoring (Lighthouse)
✅ Security scanning (Trivy)
✅ Automated deployment (Netlify)
✅ PR preview deployments
✅ Post-deployment testing

### What's Manual (for now):
⏳ Analytics setup (Plausible) - see docs/tool-stack-recommendations.md
⏳ Email integration (Buttondown) - see docs/email-sequence.md
⏳ A/B testing tracking - see docs/landing-page-copy.md

---

## 🔮 Future Phase: Full App (Phase 2)

### When You're Ready to Build the App:

1. **Create app structure** in the `app/` directory
2. **Activate workflow** by editing `.github/workflows/app-ci-cd.yml`
3. **Add tests** for your application code
4. **Configure environments:**
   - Staging: `staging.getstorytime.com`
   - Production: `app.getstorytime.com`

### What Will Be Automated:
🔄 Linting and type checking
🔄 Unit, integration, and E2E tests
🔄 Build process
🔄 Deploy to staging (on develop branch)
🔄 Deploy to production (on master branch)
🔄 Database migrations
🔄 Rollback on failure

---

## 📊 Monitoring & Observability

### GitHub Actions Dashboard
**URL:** https://github.com/gillingworth86/Storytime/actions

**What You'll See:**
- ✅ Green checkmarks when everything passes
- ❌ Red X when something fails
- 📊 Detailed logs for debugging
- ⏱️ Build times and performance metrics

### Netlify Dashboard
**URL:** https://app.netlify.com/

**What You'll See:**
- 🚀 Deploy history and status
- 📈 Bandwidth and visitor metrics
- 🔍 Deploy logs and debugging info
- ⚙️ Site configuration and settings

### Lighthouse Reports
**Location:** GitHub Actions → Workflow Run → Lighthouse Audit job

**What You'll See:**
- Performance score (target: 90+)
- Accessibility score (target: 95+)
- Best practices score (target: 90+)
- SEO score (target: 95+)
- Detailed recommendations for improvements

---

## 🛠 Development Workflow

### Making Changes to Landing Page

```bash
# 1. Create a feature branch
git checkout -b feature/update-headline

# 2. Make your changes
# Edit experimental/landing-pages/index.html

# 3. Commit and push
git add .
git commit -m "feat: update hero section headline"
git push origin feature/update-headline

# 4. Create PR on GitHub
# - CI/CD runs automatically
# - Preview deployment created
# - Review preview URL in PR comments

# 5. After approval, merge PR
# - Automatic production deployment
# - Changes live in ~2 minutes
```

### Testing Locally

```bash
# Start local server
cd experimental/landing-pages
python -m http.server 8000
# Visit: http://localhost:8000

# Validate HTML
npx html-validate *.html

# Check performance
npx lighthouse http://localhost:8000 --view
```

---

## 🔐 Security Features

### Automated Security Scanning
- **Trivy:** Scans for vulnerabilities in dependencies and config
- **GitHub CodeQL:** Static analysis for code security issues
- **Dependabot:** Automatic dependency updates

### Security Headers (via netlify.toml)
- X-Frame-Options: DENY
- X-Content-Type-Options: nosniff
- X-XSS-Protection: enabled
- Content Security Policy: configured
- HTTPS: enforced by default

### Secrets Management
All sensitive data stored as GitHub Secrets:
- `NETLIFY_AUTH_TOKEN` - Never exposed in logs
- `NETLIFY_SITE_ID` - Safely referenced in workflows

---

## 📈 Performance Budgets

Your site must meet these requirements to deploy:

| Metric | Budget | Current |
|--------|--------|---------|
| Performance | 90+ | Check Actions |
| Accessibility | 95+ | Check Actions |
| Best Practices | 90+ | Check Actions |
| SEO | 95+ | Check Actions |
| FCP (First Contentful Paint) | <2s | Check Actions |
| LCP (Largest Contentful Paint) | <2.5s | Check Actions |
| CLS (Cumulative Layout Shift) | <0.1 | Check Actions |
| TBT (Total Blocking Time) | <300ms | Check Actions |

If these aren't met, the build will fail and you'll get recommendations.

---

## 🐛 Troubleshooting

### Common Issues

**Problem:** "NETLIFY_AUTH_TOKEN not set"
```
✅ Solution: Check GitHub secrets are named exactly:
   - NETLIFY_AUTH_TOKEN (not netlify_token)
   - NETLIFY_SITE_ID (not site_id)
```

**Problem:** Workflow fails on HTML validation
```
✅ Solution: Run locally to see specific errors:
   npx html-validate experimental/landing-pages/*.html
```

**Problem:** Lighthouse score too low
```
✅ Solution: Check the Lighthouse job in Actions for specific issues
   Common fixes:
   - Optimize images (use WebP)
   - Minify CSS/JS
   - Remove unused code
   - Add alt text to images
```

**Problem:** Preview deployment not showing in PR
```
✅ Solution: Ensure:
   - PR is from a branch (not a fork)
   - Secrets are configured correctly
   - Check workflow logs for errors
```

### Getting Help

1. **Check workflow logs:** GitHub Actions → Failed workflow → View logs
2. **Check Netlify logs:** Netlify dashboard → Deploys → Failed deploy → Logs
3. **Review setup guide:** [.github/SETUP.md](.github/SETUP.md)
4. **Review checklist:** [IMPLEMENTATION-CHECKLIST.md](IMPLEMENTATION-CHECKLIST.md)

---

## 📦 What's Included vs What's Coming

### ✅ Included (Phase 1)
- [x] Landing page CI/CD
- [x] Automated quality checks
- [x] Performance monitoring
- [x] Security scanning
- [x] Preview deployments
- [x] Production deployment
- [x] Smoke tests

### ⏳ Coming Soon (Phase 1.5)
- [ ] Plausible analytics integration
- [ ] Buttondown email integration
- [ ] A/B test tracking
- [ ] Conversion tracking

### 🔮 Planned (Phase 2)
- [ ] Full app CI/CD
- [ ] Automated testing suite
- [ ] Staging environment
- [ ] Database migrations
- [ ] Backend deployment
- [ ] E2E testing

---

## 🎓 Learning Resources

### GitHub Actions
- **Docs:** https://docs.github.com/en/actions
- **Marketplace:** https://github.com/marketplace?type=actions
- **Your Workflows:** https://github.com/gillingworth86/Storytime/actions

### Netlify
- **Docs:** https://docs.netlify.com/
- **Community:** https://answers.netlify.com/
- **Your Sites:** https://app.netlify.com/

### Performance
- **Lighthouse:** https://developers.google.com/web/tools/lighthouse
- **Web.dev:** https://web.dev/
- **PageSpeed:** https://pagespeed.web.dev/

---

## 🏆 Success Metrics

Track these to know your CI/CD is working:

### Deployment Metrics
- ✅ Deployment success rate: Target 99%+
- ✅ Average deployment time: Target <3 minutes
- ✅ Failed deployments caught by CI: Target 100%
- ✅ Preview deployment availability: Target 100%

### Quality Metrics
- ✅ Lighthouse performance: Target 90+
- ✅ Zero security vulnerabilities: Target 100%
- ✅ HTML validation pass rate: Target 100%
- ✅ Automated test coverage: Target 80%+ (Phase 2)

### Developer Experience
- ✅ Time to deploy after merge: <3 minutes
- ✅ PR review efficiency: Preview URLs available
- ✅ Confidence in deployments: No manual steps
- ✅ Rollback capability: Instant via Netlify

---

## 🎉 You're All Set!

Your CI/CD automation is **production-ready** and will:

1. ✅ **Save you hours** of manual deployment work
2. ✅ **Catch bugs** before they reach production
3. ✅ **Ensure performance** stays high
4. ✅ **Enable collaboration** with safe preview environments
5. ✅ **Scale with you** as you build the full application

### Next Steps

1. **Complete setup:** Follow [QUICKSTART.md](QUICKSTART.md)
2. **Test it out:** Create a PR and watch the magic happen
3. **Launch your landing page:** Start collecting those 100 signups!
4. **Add analytics:** Set up Plausible when ready
5. **Collect feedback:** Use the validation data to decide on Phase 2

---

**Questions?** Check the [Implementation Checklist](IMPLEMENTATION-CHECKLIST.md) or [Detailed Setup Guide](.github/SETUP.md)

**Ready to deploy?** Follow the [Quick Start Guide](QUICKSTART.md)

🚀 **Happy deploying!**
