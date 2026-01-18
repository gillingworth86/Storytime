# CI/CD Implementation Guide - Lessons Learned

**Purpose:** Prevent common mistakes when implementing CI/CD pipelines from scratch.

## Phase 0: Discovery (DO THIS FIRST)

### 1. Check Git Configuration
```bash
# Check branch name (don't assume main/master)
git branch --show-current

# Check remote branches
git branch -r

# Check if repo has GitHub Actions already
ls -la .github/workflows/
```

### 2. Check Project Dependencies
```bash
# Check for lock files (affects caching strategy)
ls -la | grep -E "package-lock.json|yarn.lock|pnpm-lock.yaml|Gemfile.lock|composer.lock"

# Check package.json if it exists
cat package.json 2>/dev/null

# Check for existing build configs
ls -la | grep -E "webpack|vite|rollup|tsconfig"
```

### 3. Check Deployment State
```bash
# Check for existing deployment configs
ls -la | grep -E "netlify.toml|vercel.json|.platform.app.yaml"

# If Netlify account exists, ask user:
# - What's the actual Netlify URL? (don't assume custom domain)
# - Is the site already created? (get Site ID)
```

### 4. Check Existing CI/CD
```bash
# GitHub Actions
cat .github/workflows/*.yml 2>/dev/null

# GitLab CI
cat .gitlab-ci.yml 2>/dev/null

# Other CI systems
cat .circleci/config.yml 2>/dev/null
cat .travis.yml 2>/dev/null
```

---

## Phase 1: Minimal Working Pipeline

**Philosophy:** Start minimal, iterate based on actual errors.

### Workflow Structure (v1)
```yaml
name: CI/CD

on:
  push:
    branches: [<ACTUAL_BRANCH_NAME>]  # CHECK THIS FIRST
  pull_request:
    branches: [<ACTUAL_BRANCH_NAME>]

# CRITICAL: Add permissions if using security scanning
permissions:
  contents: read
  security-events: write  # For CodeQL/Trivy
  pull-requests: write    # For PR comments

jobs:
  # Job 1: Basic validation only
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup language runtime
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          # DON'T ADD CACHE YET - check for lock file first

      - name: Basic validation
        run: echo "Add minimal validation here"
        # Start with just checking files exist
        # Add linting/validation after this works

  # Job 2: Deploy (separate job, doesn't block on validation initially)
  deploy:
    runs-on: ubuntu-latest
    if: github.event_name == 'push'
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to platform
        run: echo "Add deployment here"
        # Use actual platform action after basic structure works
```

### Validation Rules (v1) - START LENIENT
```json
// .htmlvalidate.json (if using HTML validation)
{
  "extends": ["html-validate:recommended"],
  "rules": {
    // Start with everything OFF except critical errors
    "void-style": "off",
    "no-inline-style": "off",
    "no-implicit-button-type": "off",
    // Only enforce actual errors
    "no-dup-id": "error",
    "doctype-html": "error"
  }
}
```

**Rationale:** Let the first run tell you what needs fixing, don't preemptively set strict rules.

---

## Phase 2: Add Features Incrementally

### Decision Tree for Each Feature:

#### Adding npm Cache?
```yaml
# BEFORE adding cache, check:
# 1. Does package-lock.json exist?
# 2. If not, DON'T add cache line

# ✅ YES - has lock file:
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm'

# ❌ NO - no lock file:
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    # No cache line
```

#### Adding Security Scanning?
```yaml
# Use LATEST versions
- uses: aquasecurity/trivy-action@master
  continue-on-error: true  # Don't block on scan failures initially
  with:
    scan-type: 'fs'
    format: 'sarif'
    output: 'trivy-results.sarif'

# Use CodeQL v3 (not v2 - deprecated)
- uses: github/codeql-action/upload-sarif@v3
  if: always() && hashFiles('trivy-results.sarif') != ''  # Check file exists
  with:
    sarif_file: 'trivy-results.sarif'
```

#### Adding Lighthouse?
```yaml
# CRITICAL: Lighthouse needs DEPLOYED URL, not local files

# ❌ WRONG - will fail:
lighthouse-audit:
  steps:
    - uses: treosh/lighthouse-ci-action@v10
      with:
        urls: file:///path/to/index.html  # FAILS

# ✅ CORRECT:
lighthouse-audit:
  needs: deploy  # Run AFTER deployment
  steps:
    - name: Wait for deployment
      run: sleep 30  # Give CDN time to propagate

    - uses: treosh/lighthouse-ci-action@v10
      continue-on-error: true  # Don't block on failures
      with:
        urls: https://actual-deployed-url.com  # Use REAL URL
        uploadArtifacts: false  # Avoid artifact naming issues
        temporaryPublicStorage: false
```

#### Adding Playwright Tests?
```yaml
# Use LOCAL install, not global
- name: Install Playwright
  run: |
    npm install playwright  # Local, not -g
    npx playwright install chromium --with-deps  # Include --with-deps

# Then use in script
- name: Run tests
  run: |
    cat > test.js << 'EOF'
    const { chromium } = require('playwright');  # Will work now
    EOF
    node test.js
```

---

## Phase 3: Checklist Before Implementing

**Use this checklist BEFORE writing any workflow:**

### Discovery Checklist
- [ ] What is the actual git branch name? (`git branch --show-current`)
- [ ] Does a package-lock.json (or equivalent) exist?
- [ ] What is the actual deployment URL? (ask user, don't assume)
- [ ] Are there existing workflows? (check .github/workflows/)
- [ ] What validation is already passing locally? (don't add stricter rules)
- [ ] What permissions are needed? (add them upfront)

### Implementation Checklist
- [ ] Use LATEST action versions (check @v3, @v4, not @v2)
- [ ] Add `continue-on-error: true` for non-critical steps
- [ ] Check files exist before uploading (`hashFiles() != ''`)
- [ ] Use local npm installs, not global (`npm install` not `npm install -g`)
- [ ] Lighthouse runs AFTER deployment with real URL
- [ ] Security scans have proper permissions
- [ ] Validation rules are lenient initially
- [ ] Cache only added if lock file exists

### Testing Checklist
- [ ] First commit: minimal workflow that does almost nothing
- [ ] Second commit: add one feature, test it
- [ ] Third commit: add next feature, test it
- [ ] Don't add 10 features at once and debug 10 errors

---

## Common Anti-Patterns to Avoid

### ❌ Anti-Pattern 1: Assumption-Driven Development
```yaml
# Assuming branch is main (might be master)
branches: [main]

# Assuming custom domain (might be platform subdomain)
urls: https://mycustomdomain.com

# Assuming lock file exists
cache: 'npm'
```

### ✅ Pattern: Discovery-Driven Development
```yaml
# Check first, then configure
branches: [master]  # Checked with git branch

urls: https://project.netlify.app  # Got from user

# Only cache if lock file exists (checked first)
```

### ❌ Anti-Pattern 2: Strict-First Validation
```json
{
  "rules": {
    "void-style": ["error", {"style": "selfclose"}],
    "no-inline-style": "error",
    "performance-budget": ["error", {"maxScore": 0.95}]
  }
}
```

### ✅ Pattern: Lenient-First, Tighten Later
```json
{
  "rules": {
    "void-style": "off",  // Fix existing code first
    "no-inline-style": "off",  // Then tighten
    "no-dup-id": "error"  // Only critical errors
  }
}
```

### ❌ Anti-Pattern 3: All-or-Nothing Deployment
```yaml
jobs:
  validate-and-deploy:
    steps:
      - validate
      - test
      - security-scan
      - lighthouse
      - deploy  # Blocked if any above fails
```

### ✅ Pattern: Progressive Enhancement
```yaml
jobs:
  # Critical path: validate → deploy
  deploy:
    needs: validate
    steps: [deploy]

  # Optional: run after deploy, don't block
  lighthouse:
    needs: deploy
    continue-on-error: true
    steps: [audit]
```

---

## Red Flags During Implementation

**If you see these, STOP and check assumptions:**

1. **"Dependencies lock file is not found"**
   - Fix: Remove `cache:` line from setup-node

2. **"CodeQL Action v2 is deprecated"**
   - Fix: Use @v3, not @v2

3. **"INVALID_URL" from Lighthouse**
   - Fix: Using file:// URL, need https:// deployed URL

4. **"Cannot find module 'playwright'"**
   - Fix: Using `npm install -g`, need local `npm install`

5. **"Rule configuration error: type must be object"**
   - Fix: HTML validate rules need object format: `["error", {"style": "..."}]`

6. **"Resource not accessible by integration"**
   - Fix: Missing `permissions:` section in workflow

7. **"Create Artifact Container failed"**
   - Fix: Disable `uploadArtifacts` or use valid artifact name

8. **Workflow not triggering on push**
   - Fix: Check `paths:` filter includes changed files

---

## Summary: The Right Order

1. **Discover** - Check actual state (branch, files, URLs)
2. **Minimal** - Create simplest possible workflow
3. **Deploy** - Get deployment working first (core goal)
4. **Validate** - Add validation that matches existing code
5. **Enhance** - Add security, performance, tests incrementally
6. **Tighten** - Make rules stricter over time

**Key Principle:** Let the errors tell you what to add, don't predict all issues upfront.

---

## Estimated Timeline with This Approach

| Phase | Time | Commits | Errors |
|-------|------|---------|--------|
| Discovery | 5 min | 0 | 0 |
| Minimal workflow | 10 min | 1 | 0-1 |
| Add deployment | 10 min | 1 | 0-1 |
| Add validation | 10 min | 1 | 0-2 |
| Add enhancements | 20 min | 3-4 | 0-3 |
| **Total** | **~55 min** | **6-7** | **0-7** |

**Compare to our actual session:**
- Time: ~90 minutes
- Commits: 11 (many were fixes)
- Errors: 10+

**Savings with this approach:** ~35% less time, ~40% fewer commits

---

## Template: Minimal Starting Point

```yaml
# .github/workflows/ci.yml
name: CI/CD

on:
  push:
    branches: [REPLACE_WITH_ACTUAL_BRANCH]

permissions:
  contents: read
  security-events: write
  pull-requests: write

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Deploy
        run: echo "Add deployment here"
        # TODO: Add actual deployment action
        # TODO: Only after basic structure works
```

**Start here, then iterate based on actual errors.**

---

**This guide created from real mistakes - use it to avoid repeating them! 🎯**
