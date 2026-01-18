# Storytime CI/CD Setup Guide

This guide will walk you through setting up complete CI/CD automation for the Storytime landing page using your **gillingworth86** GitHub account and Netlify.

---

## 🎯 Overview

Your CI/CD pipeline will automatically:
- ✅ Validate HTML quality
- ✅ Run Lighthouse performance audits
- ✅ Scan for security vulnerabilities
- ✅ Deploy preview builds for pull requests
- ✅ Deploy to production on merge to main
- ✅ Run post-deployment smoke tests

---

## 📋 Prerequisites

- [x] GitHub account: **gillingworth86** (you have this)
- [x] Netlify account connected to GitHub (you have this)
- [x] Storytime repository on GitHub
- [ ] GitHub repository secrets configured (we'll do this below)

---

## Part 1: Create Netlify Site

### Step 1: Create a New Netlify Site

1. **Log in to Netlify** using your gillingworth86 GitHub account:
   - Go to: https://app.netlify.com/
   - Click "Log in with GitHub"

2. **Create a new site**:
   - Click "Add new site" → "Import an existing project"
   - Choose "Deploy with GitHub"
   - Select your **Storytime** repository
   - **Important:** Click "Show advanced" and configure:
     - **Base directory:** Leave empty
     - **Build command:** `echo 'Static site'`
     - **Publish directory:** `experimental/landing-pages`
   - Click "Deploy site"

3. **Get your site details**:
   - After deployment, you'll see your site URL (e.g., `random-name-123.netlify.app`)
   - Go to **Site settings**
   - Note your **Site ID** (looks like: `abc12345-67de-89fg-hijk-lmnop1234567`)

### Step 2: Get Netlify Authentication Token

1. Go to **User settings** (click your avatar → User settings)
2. Click **Applications** in the sidebar
3. Under "Personal access tokens", click **New access token**
4. Name it: `Storytime CI/CD`
5. Click **Generate token**
6. **COPY THE TOKEN IMMEDIATELY** - you won't see it again!
   - Format: `nfp_abc123def456ghi789jkl012mno345pqr678stu901vwx234yz`

### Step 3: Configure Custom Domain (Optional but Recommended)

1. In your Netlify site settings, go to **Domain management**
2. Click **Add custom domain**
3. Enter: `getstorytime.com` (or your chosen domain)
4. Follow the DNS configuration instructions
5. Enable **HTTPS** (Netlify will automatically provision SSL)

---

## Part 2: Configure GitHub Secrets

### Step 1: Add Secrets to GitHub Repository

1. Go to your **Storytime** repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret** and add:

#### Secret 1: NETLIFY_AUTH_TOKEN
- **Name:** `NETLIFY_AUTH_TOKEN`
- **Value:** Paste the token from Part 1, Step 2
- Click **Add secret**

#### Secret 2: NETLIFY_SITE_ID
- **Name:** `NETLIFY_SITE_ID`
- **Value:** Paste the Site ID from Part 1, Step 1
- Click **Add secret**

### Step 2: Verify Secrets

Your secrets should now look like this:
```
NETLIFY_AUTH_TOKEN = nfp_***************************
NETLIFY_SITE_ID = abc12345-67de-89fg-hijk-***********
```

---

## Part 3: Test the CI/CD Pipeline

### Step 1: Commit and Push Workflow Files

The workflow files are already in your repository at:
- `.github/workflows/landing-page-ci-cd.yml`
- `.github/lighthouserc.json`
- `netlify.toml`

If they're not committed yet:

```bash
cd c:\Dev\Storytime
git add .github/ netlify.toml
git commit -m "ci: add CI/CD automation for landing page"
git push origin main
```

### Step 2: Watch the Workflow Run

1. Go to your repository on GitHub
2. Click the **Actions** tab
3. You should see "Landing Page CI/CD" running
4. Click on it to watch the progress

### Step 3: Verify Deployment

After the workflow completes:
1. Check the workflow summary for the deployment URL
2. Visit your site (e.g., `getstorytime.com` or `your-site.netlify.app`)
3. Verify the landing page loads correctly

---

## Part 4: Test Pull Request Preview Deployments

### Step 1: Create a Test Branch

```bash
git checkout -b test-ci-cd
```

### Step 2: Make a Small Change

Edit `experimental/landing-pages/index.html`:
- Change a word in the hero heading
- Or update a color in the styles

### Step 3: Commit and Push

```bash
git add .
git commit -m "test: verify CI/CD preview deployment"
git push origin test-ci-cd
```

### Step 4: Create Pull Request

1. Go to GitHub and create a Pull Request from `test-ci-cd` to `main`
2. The CI/CD workflow will automatically:
   - Run quality checks
   - Deploy a preview version
   - Comment on the PR with the preview URL
3. Click the preview URL to see your changes

### Step 5: Merge and Deploy

1. After reviewing, merge the PR
2. The workflow will automatically deploy to production
3. Verify at your production URL

---

## Part 5: Monitoring and Maintenance

### View Deployment Logs

**Netlify Dashboard:**
- https://app.netlify.com/sites/YOUR-SITE/deploys

**GitHub Actions:**
- https://github.com/gillingworth86/Storytime/actions

### Lighthouse Performance Reports

After each deployment, Lighthouse generates a performance report:
1. Go to the Actions tab
2. Click on a completed workflow run
3. Find the "Lighthouse Performance Audit" job
4. Click to see the performance score and recommendations

### Common Issues and Fixes

#### Issue: "Error: Unable to get local issuer certificate"
**Fix:** Update Node.js or add `NODE_TLS_REJECT_UNAUTHORIZED=0` temporarily

#### Issue: "NETLIFY_AUTH_TOKEN not set"
**Fix:** Verify the secret name exactly matches `NETLIFY_AUTH_TOKEN` (case-sensitive)

#### Issue: "Publish directory not found"
**Fix:** Check that `netlify.toml` specifies `publish = "experimental/landing-pages"`

#### Issue: HTML validation fails
**Fix:** Run `npx html-validate experimental/landing-pages/*.html` locally to fix issues

---

## Part 6: Next Steps - Analytics & Email Integration

### Add Plausible Analytics (when ready)

1. Sign up at https://plausible.io/
2. Add your domain
3. Copy the tracking script
4. Add to `index.html` before `</head>`:
   ```html
   <script defer data-domain="getstorytime.com" src="https://plausible.io/js/script.js"></script>
   ```
5. Update `netlify.toml` CSP headers (follow the comments in the file)

### Add Buttondown Email (when ready)

1. Sign up at https://buttondown.email/
2. Create your newsletter
3. Get the email form embed code
4. Replace the placeholder forms in `index.html`
5. Update `netlify.toml` CSP headers (follow the comments in the file)

### Add A/B Testing for Headlines

The landing page has 4 headline variants rotating. To track which converts best:
1. Add conversion tracking in Plausible (custom events)
2. Or use Netlify's Split Testing feature
3. Or use a dedicated A/B testing tool like Google Optimize

---

## Part 7: Phase 2 - Full Application (Future)

When you're ready to build the full Storytime app:

1. Create `app/` directory structure
2. Add a new workflow: `.github/workflows/app-ci-cd.yml`
3. Update `netlify.toml` to add separate site config for the app
4. Consider splitting into:
   - Landing page: `getstorytime.com`
   - App: `app.getstorytime.com`

---

## 🎉 Success Checklist

After completing this setup, you should have:

- [x] Netlify site created and connected
- [x] GitHub secrets configured
- [x] CI/CD pipeline running successfully
- [x] Landing page deployed to production
- [x] Preview deployments working for PRs
- [x] Performance monitoring with Lighthouse
- [x] Security scanning with Trivy

---

## 📞 Support Resources

- **Netlify Docs:** https://docs.netlify.com/
- **GitHub Actions Docs:** https://docs.github.com/en/actions
- **Lighthouse CI:** https://github.com/GoogleChrome/lighthouse-ci

---

## 🔐 Security Best Practices

✅ Never commit secrets to the repository
✅ Keep GitHub secrets up to date
✅ Review Netlify access logs regularly
✅ Enable Netlify's DDoS protection
✅ Use HTTPS only (enforced by Netlify)
✅ Review security scan results in Actions

---

**Need help?** Check the GitHub Issues or review the workflow logs for detailed error messages.
