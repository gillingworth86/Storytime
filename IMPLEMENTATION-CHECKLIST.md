> [!WARNING]
> **Historical document (Netlify-era):** This checklist is retained for reference only and is not the active setup path.
>
> Use [`QUICKSTART.md`](QUICKSTART.md) and [`docs/current-state.md`](docs/current-state.md) for the current Vercel-first workflow.

# 📋 Storytime CI/CD Implementation Checklist

Use this checklist to track your progress through setting up complete CI/CD automation.

---

## Phase 1: Landing Page Automation (Current)

### 🔧 Infrastructure Setup

- [ ] **Netlify Account**
  - [ ] Logged in with gillingworth86 GitHub account
  - [ ] New site created and linked to Storytime repository
  - [ ] Site ID copied and saved
  - [ ] Personal access token generated and saved
  - [ ] Custom domaster configured (optional): `getstorytime.com`

- [ ] **GitHub Secrets**
  - [ ] `NETLIFY_AUTH_TOKEN` added to repository secrets
  - [ ] `NETLIFY_SITE_ID` added to repository secrets
  - [ ] Secrets verified in Settings → Secrets and variables → Actions

- [ ] **CI/CD Files Committed**
  - [ ] `.github/workflows/landing-page-ci-cd.yml` committed
  - [ ] `.github/lighthouserc.json` committed
  - [ ] `netlify.toml` committed
  - [ ] `.htmlvalidate.json` committed
  - [ ] Files pushed to `master` branch

### ✅ Verify Automation

- [ ] **GitHub Actions**
  - [ ] First workflow run completed successfully
  - [ ] All jobs passed (quality-check, lighthouse-audit, deploy-netlify)
  - [ ] Green checkmark appears in GitHub Actions tab
  - [ ] No error messages in workflow logs

- [ ] **Netlify Deployment**
  - [ ] Site shows "Published" status in Netlify dashboard
  - [ ] Production URL accessible and working
  - [ ] SSL/HTTPS enabled and working
  - [ ] All pages load without errors

- [ ] **Landing Page Functionality**
  - [ ] Hero section displays correctly
  - [ ] Rotating headlines working
  - [ ] Email forms present (even if not connected yet)
  - [ ] FAQ accordions expand/collapse
  - [ ] Pricing section displays
  - [ ] Mobile responsive (test on phone)
  - [ ] Stars animation working
  - [ ] All links functional

### 🧪 Test Pull Request Workflow

- [ ] **Create Test PR**
  - [ ] Created feature branch (`git checkout -b test/ci-cd`)
  - [ ] Made small change to landing page
  - [ ] Committed and pushed changes
  - [ ] Created pull request on GitHub

- [ ] **Verify PR Automation**
  - [ ] CI/CD workflow triggered automatically
  - [ ] Preview deployment created
  - [ ] Bot commented on PR with preview URL
  - [ ] Preview URL accessible and shows changes
  - [ ] All quality checks passed

- [ ] **Merge and Deploy**
  - [ ] PR merged to master
  - [ ] Production deployment triggered automatically
  - [ ] Changes visible on production site
  - [ ] No errors in deployment

### 📊 Performance & Security

- [ ] **Lighthouse Scores**
  - [ ] Performance: 90+ ✓
  - [ ] Accessibility: 95+ ✓
  - [ ] Best Practices: 90+ ✓
  - [ ] SEO: 95+ ✓
  - [ ] Review recommendations if scores are low

- [ ] **Security Scan**
  - [ ] Trivy scan completed
  - [ ] No critical vulnerabilities found
  - [ ] Review any warnings in scan results

- [ ] **HTML Validation**
  - [ ] HTML validation passed
  - [ ] No structural errors
  - [ ] Accessibility checks passed

---

## Phase 1.5: Analytics & Email Integration (Next)

### 📈 Plausible Analytics

- [ ] **Setup**
  - [ ] Signed up at https://plausible.io/
  - [ ] Added domaster: `getstorytime.com`
  - [ ] Copied tracking script

- [ ] **Integration**
  - [ ] Added script to `index.html` before `</head>`
  - [ ] Updated `netlify.toml` CSP headers for Plausible
  - [ ] Committed and deployed changes
  - [ ] Verified tracking in Plausible dashboard
  - [ ] Set up conversion goals for email signups

### 📧 Kit (ConvertKit) Email

- [ ] **Setup**
  - [ ] Signed up at https://kit.com/
  - [ ] Created form + sequence
  - [ ] Configured email sequence (4 emails)
  - [ ] Copied form embed code / action URL

- [ ] **Integration**
  - [ ] Replaced placeholder forms in `index.html`
  - [ ] Updated `netlify.toml` CSP headers for Kit (app.kit.com / api.kit.com)
  - [ ] Tested form submission
  - [ ] Verified welcome email sends
  - [ ] Verified follow-up emails scheduled

### 🧪 A/B Testing

- [ ] **Headline Variants**
  - [ ] All 4 headline variants rotating correctly
  - [ ] Tracking which variant each user sees
  - [ ] Tracking conversion by variant
  - [ ] Running test for at least 100 signups per variant

---

## Phase 2: Distribution & Validation (After Launch)

### 🚀 Launch Preparation

- [ ] **Final Pre-Launch Checks**
  - [ ] All links working
  - [ ] No typos in copy
  - [ ] Privacy policy page created
  - [ ] Terms page created
  - [ ] Contact information added
  - [ ] Social sharing images (og:image) added
  - [ ] Favicon added
  - [ ] Google Search Console verified

- [ ] **Soft Launch**
  - [ ] Shared with friends/family
  - [ ] Collected initial feedback
  - [ ] Fixed any reported issues
  - [ ] Confirmed email flow working

### 📣 Distribution

- [ ] **Week 1: Soft Launch** (Goal: 25 signups)
  - [ ] Posted to r/SideProject
  - [ ] Posted to r/roastmystartup
  - [ ] Posted to r/Parenting
  - [ ] Posted to 2-3 Facebook groups
  - [ ] Tracked conversions by channel

- [ ] **Week 2: Scale Up** (Goal: 50 more signups)
  - [ ] Identified best-performing channel
  - [ ] Doubled down on winning channel
  - [ ] Posted to Tier 2 communities
  - [ ] Adjusted messaging based on feedback

- [ ] **Week 3: Final Push** (Goal: 25 final signups)
  - [ ] Cross-posted to remastering communities
  - [ ] Asked subscribers to share
  - [ ] Reached 100 signup target 🎉

### 📊 Metrics & Analysis

- [ ] **Tracking Setup**
  - [ ] Tracking spreadsheet created
  - [ ] Daily signup tracking
  - [ ] Conversion rate by channel
  - [ ] Cost per signup calculated
  - [ ] Best-performing headline identified

- [ ] **Validation Analysis**
  - [ ] Survey responses analyzed
  - [ ] Price sensitivity validated
  - [ ] Feature priorities ranked
  - [ ] Key objections identified
  - [ ] Go/no-go decision made

---

## Phase 3: Full App Development (Future)

### 🏗 App Infrastructure

- [ ] **Technology Stack**
  - [ ] Frontend framework chosen
  - [ ] Backend framework chosen
  - [ ] Database selected
  - [ ] Hosting provider selected
  - [ ] Architecture documented

- [ ] **Development Environment**
  - [ ] Local development setup documented
  - [ ] Environment variables configured
  - [ ] Database migrations setup
  - [ ] Seed data created

### 🔄 App CI/CD Pipeline

- [ ] **Workflow Configuration**
  - [ ] Activated `.github/workflows/app-ci-cd.yml`
  - [ ] Added linting and type checking
  - [ ] Added unit tests
  - [ ] Added integration tests
  - [ ] Added E2E tests with Playwright

- [ ] **Environments**
  - [ ] Staging environment created
  - [ ] Production environment created
  - [ ] Environment variables configured
  - [ ] Database instances provisioned

- [ ] **Deployment Strategy**
  - [ ] Staging deploys on push to `develop`
  - [ ] Production deploys on push to `master`
  - [ ] Automated tests run before production
  - [ ] Rollback strategy documented

### 🧪 Testing Strategy

- [ ] **Test Coverage**
  - [ ] Unit test coverage >80%
  - [ ] Integration tests for API endpoints
  - [ ] E2E tests for critical user flows
  - [ ] Performance tests configured
  - [ ] Security tests automated

- [ ] **Quality Gates**
  - [ ] All tests must pass before merge
  - [ ] Code coverage threshold enforced
  - [ ] Lighthouse scores mastertained
  - [ ] No critical security vulnerabilities

### 📱 Beta Launch

- [ ] **Beta Program**
  - [ ] Beta invite email sent to first 100 signups
  - [ ] Onboarding flow tested
  - [ ] Payment integration tested
  - [ ] Story generation working
  - [ ] Feedback collection system setup

- [ ] **Monitoring**
  - [ ] Error tracking configured (Sentry)
  - [ ] Performance monitoring (Plausible + custom)
  - [ ] User analytics dashboard
  - [ ] Alerts configured for critical errors

---

## 🎯 Success Criteria

### Phase 1: Landing Page ✓
- [x] CI/CD fully automated
- [ ] 100 email signups achieved
- [ ] Conversion rate >10% on best channel
- [ ] Positive feedback from target audience

### Phase 2: Validation
- [ ] Validated willingness to pay $9.99/month
- [ ] Identified most-wanted features
- [ ] Confirmed distribution channels work
- [ ] Decision to build or pivot

### Phase 3: App Launch
- [ ] Beta launched to first 100 users
- [ ] Payment processing working
- [ ] Story generation working reliably
- [ ] Positive user reviews
- [ ] Path to profitability clear

---

## 📞 Need Help?

- **Setup Issues:** See [.github/SETUP.md](.github/SETUP.md)
- **Quick Start:** See [QUICKSTART.md](QUICKSTART.md)
- **GitHub Actions:** Check the Actions tab for detailed logs
- **Netlify Issues:** Check Netlify dashboard deploy logs

---

## 🎉 Milestones

Track your major achievements:

- [ ] 🚀 First successful CI/CD deployment
- [ ] 📈 First 10 email signups
- [ ] 💯 100 email signups (validation goal!)
- [ ] 🎨 Full app design complete
- [ ] 🏗 App CI/CD pipeline operational
- [ ] 🧪 Beta launch to first users
- [ ] 💰 First paying customer
- [ ] 🌟 Profitability achieved

---

**Current Phase:** Phase 1 - Landing Page Automation

**Next Step:** Complete Infrastructure Setup section above ☝️
