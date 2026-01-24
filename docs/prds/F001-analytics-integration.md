# PRD: F001 - Analytics Integration

**Status:** Draft - Ready for Review
**Priority:** P0 (Critical Path)
**Effort Estimate:** 1 day
**Owner:** TBD
**Created:** 2026-01-24
**Last Updated:** 2026-01-24

---

## 1. Executive Summary

Storytime needs analytics to track visitor behavior, measure conversion rates, and validate the landing page's effectiveness in achieving the 100 email signup goal within 3 weeks.

**Problem Statement:**
Currently, there is no visibility into landing page performance. We cannot answer critical questions:
- How many people are visiting the site?
- Where are they coming from?
- Are they engaging with the content?
- How many visitors convert to email signups?
- What's the drop-off rate in the conversion funnel?

Without this data, we're flying blind and cannot optimize for the signup goal.

**Proposed Solution:**
Integrate a privacy-focused, lightweight analytics solution that tracks visitor behavior and conversion events without compromising user privacy or page performance.

**Success Criteria:**
- Track unique visitors, page views, and bounce rate
- Monitor email form submission events with 100% accuracy
- Measure conversion rate (visitor → signup)
- Analytics dashboard accessible within 24 hours of deployment
- Zero impact on page load performance (<50ms script load time)
- GDPR/CCPA compliant (no cookie consent banner required)

---

## 2. Market Analysis: Analytics Tool Comparison

### 2.1 Evaluation Criteria

For this project, we evaluated analytics solutions based on:

| Criterion | Weight | Rationale |
|-----------|--------|-----------|
| **Privacy Compliance** | Critical | GDPR/CCPA compliance required; avoid cookie banners |
| **Cost** | High | Pre-revenue project, minimize recurring costs |
| **Integration Ease** | High | Need to deploy quickly (P0 priority) |
| **Performance Impact** | High | Landing page must load fast (Lighthouse 90+) |
| **Event Tracking** | Medium | Need custom events for email signups |
| **Data Retention** | Medium | Need historical data for trend analysis |
| **User Experience** | Low | Analytics are for us, not end users |

### 2.2 Options Evaluated

#### Option 1: Google Analytics 4 (GA4)
**Pros:**
- ✅ Industry standard, comprehensive features
- ✅ Free forever (for our scale)
- ✅ Powerful custom event tracking
- ✅ Integration with Google Ads (future)
- ✅ Extensive documentation and community

**Cons:**
- ❌ Requires cookie consent banner (GDPR)
- ❌ Heavy script (~45KB gzipped)
- ❌ Collects PII, raises privacy concerns
- ❌ Complex setup, steep learning curve
- ❌ Data owned by Google
- ❌ Blocked by 30%+ of users (ad blockers)

**Cost:** Free
**Privacy:** ⚠️ Problematic - Needs cookie banner
**Performance:** ⚠️ Heavy (45KB)
**Integration:** ⚠️ Complex setup

**Verdict:** ❌ **Not Recommended**
- Privacy concerns conflict with brand values
- Cookie banner hurts conversion rates
- Overkill for simple landing page validation

---

#### Option 2: Plausible Analytics
**Pros:**
- ✅ Privacy-first (GDPR/CCPA compliant by default)
- ✅ No cookie consent banner required
- ✅ Lightweight script (<1KB gzipped)
- ✅ Simple, intuitive dashboard
- ✅ Custom event tracking built-in
- ✅ Open source (can self-host later)
- ✅ EU-hosted data (GDPR compliant)
- ✅ Not blocked by most ad blockers
- ✅ Real-time analytics
- ✅ Easy integration (single script tag)

**Cons:**
- ❌ Paid service ($9/month for 10k pageviews)
- ⚠️ Fewer features than GA4 (not needed for our use case)
- ⚠️ No funnel visualization (can build manually)

**Cost:** $9/month (~$108/year)
**Privacy:** ✅ Excellent - No cookies, GDPR compliant
**Performance:** ✅ Excellent - <1KB script
**Integration:** ✅ Excellent - Single script tag

**Verdict:** ✅ **Recommended**
- Aligns with privacy-first brand values
- Simplicity enables fast implementation
- Cost justified by critical need for data
- Can self-host open source version later if needed

---

#### Option 3: Fathom Analytics
**Pros:**
- ✅ Privacy-focused (GDPR/CCPA compliant)
- ✅ No cookie consent required
- ✅ Lightweight script (~1.6KB gzipped)
- ✅ Simple dashboard
- ✅ Custom events supported
- ✅ EU data hosting available

**Cons:**
- ❌ More expensive ($14/month for 100k pageviews)
- ⚠️ Slightly larger script than Plausible
- ⚠️ Less active development than Plausible
- ⚠️ Closed source (no self-hosting option)

**Cost:** $14/month (~$168/year)
**Privacy:** ✅ Excellent
**Performance:** ✅ Good (1.6KB)
**Integration:** ✅ Excellent

**Verdict:** ⚠️ **Alternative Option**
- Similar to Plausible but more expensive
- No self-hosting option (vendor lock-in)
- Consider if Plausible unavailable

---

#### Option 4: Simple Analytics
**Pros:**
- ✅ Privacy-focused (GDPR/CCPA compliant)
- ✅ No cookies required
- ✅ Lightweight script (~3KB gzipped)
- ✅ Simple interface
- ✅ Events and goals supported

**Cons:**
- ❌ More expensive ($19/month for 100k hits)
- ⚠️ Larger script than Plausible/Fathom
- ⚠️ Fewer integrations

**Cost:** $19/month (~$228/year)
**Privacy:** ✅ Excellent
**Performance:** ✅ Good (3KB)
**Integration:** ✅ Good

**Verdict:** ⚠️ **Not Recommended**
- More expensive than Plausible
- Larger script size
- No compelling advantage

---

#### Option 5: Umami (Open Source)
**Pros:**
- ✅ Free (self-hosted)
- ✅ Privacy-focused, GDPR compliant
- ✅ No cookies required
- ✅ Lightweight script (~2KB)
- ✅ Full control over data
- ✅ Custom events supported

**Cons:**
- ❌ Requires hosting infrastructure
- ❌ Setup and maintenance overhead
- ❌ Database management needed
- ❌ Less polished UI than paid options
- ❌ No managed service/support

**Cost:** Free + hosting costs (~$5-10/month)
**Privacy:** ✅ Excellent
**Performance:** ✅ Good (2KB)
**Integration:** ⚠️ Complex (requires server setup)

**Verdict:** ⚠️ **Future Option**
- Great for long-term cost savings
- Too much overhead for Phase 1 (landing page validation)
- Consider for Phase 2 when building full app infrastructure

---

### 2.3 Recommendation: Plausible Analytics

**Selected:** Plausible Analytics

**Rationale:**
1. **Privacy-first approach** aligns with Storytime's brand values (children's content)
2. **No cookie banner** removes conversion funnel friction
3. **Minimal performance impact** (<1KB script) maintains Lighthouse scores
4. **Simple integration** enables same-day deployment (P0 priority)
5. **Cost-effective** for validation phase ($9/month vs. $14-19 for alternatives)
6. **Open source** provides exit strategy (self-host later if needed)
7. **Not blocked** by most ad blockers (unlike GA4)

**Cost Analysis:**
- $9/month × 3 weeks validation period = ~$7 spent
- If successful (100 signups), cost per signup = $0.07
- ROI: Invaluable data for optimization decisions

**Migration Path:**
- Phase 1: Use Plausible cloud (fast setup)
- Phase 2+: Evaluate self-hosting Plausible (save costs at scale)

---

## 3. User Stories

### Primary User Story
**As a** product owner
**I want** real-time visibility into landing page performance
**So that** I can measure progress toward the 100 signup goal and identify optimization opportunities

**Acceptance Criteria:**
1. Plausible dashboard shows live visitor count within 1 minute of site visit
2. All pageviews are tracked accurately (verified via multiple test visits)
3. Email signup events appear in dashboard within 30 seconds
4. Historical data is accessible for trend analysis
5. Dashboard accessible via shared link (no account required for stakeholders)

### Secondary User Story
**As a** marketer
**I want** to track conversion funnel drop-off points
**So that** I can optimize the user journey from visitor to signup

**Acceptance Criteria:**
1. Can see visitor → email form view → signup conversion rates
2. Bounce rate visible to identify engagement issues
3. Traffic sources tracked (direct, referral, social, etc.)

---

## 4. Functional Requirements

### 4.1 Core Functionality

**REQ-001: Pageview Tracking**
- **Description:** Track all pageviews on landing page (index.html)
- **Priority:** Must-have
- **Acceptance:** Every page load appears in Plausible dashboard within 60 seconds

**REQ-002: Visitor Tracking**
- **Description:** Track unique visitors (without cookies, using IP + User Agent hash)
- **Priority:** Must-have
- **Acceptance:** Unique visitor count accurate within ±5% margin

**REQ-003: Traffic Source Tracking**
- **Description:** Identify how visitors found the site (referrer, UTM parameters)
- **Priority:** Must-have
- **Acceptance:** Referrer data visible in dashboard for all external traffic

**REQ-004: Custom Event - Email Form Viewed**
- **Description:** Fire event when user scrolls to email signup form
- **Priority:** Should-have
- **Acceptance:** Event triggered when form enters viewport (Intersection Observer)

**REQ-005: Custom Event - Email Signup Submitted**
- **Description:** Fire event when user submits email form
- **Priority:** Must-have
- **Acceptance:** Event triggered on form submit, appears in dashboard within 30 seconds

**REQ-006: Custom Event - CTA Clicked**
- **Description:** Track clicks on primary CTA buttons
- **Priority:** Nice-to-have
- **Acceptance:** Event triggered on button click with button ID in metadata

**REQ-007: Page Engagement Metrics**
- **Description:** Track bounce rate and average time on page
- **Priority:** Should-have
- **Acceptance:** Metrics visible in Plausible dashboard

### 4.2 User Interface Requirements
*Not applicable - analytics are invisible to end users*

### 4.3 Data Requirements

**Input Data:**
- Pageview events (automatic)
- Custom events (JavaScript triggers)
- UTM parameters (from URLs)

**Output Data:**
- Dashboard metrics in Plausible web UI
- CSV exports (available via Plausible export feature)

**Data Validation:**
- No PII collected (no emails, names, etc. sent to analytics)
- Events fire only once per user action (no duplicates)

**Data Persistence:**
- Plausible stores data for 2 years (sufficient for this project)

---

## 5. Technical Specifications

### 5.1 Architecture Overview

```
User's Browser
    ↓
[Landing Page (index.html)]
    ↓
[Plausible Script (plausible.js)]
    ↓
[Plausible API (plausible.io)]
    ↓
[Plausible Dashboard]
```

**Components:**
- **Frontend:** Modified `index.html` with script tag and event tracking
- **External Service:** Plausible Analytics (cloud-hosted)
- **Configuration:** Updated CSP headers in `netlify.toml`

### 5.2 Integration Implementation

#### Step 1: Add Plausible Script to HTML

**Location:** `experimental/landing-pages/index.html`

**Add to `<head>` section (before closing `</head>`):**
```html
<!-- Plausible Analytics - Privacy-friendly analytics -->
<script defer data-domain="getstorytime.netlify.app" src="https://plausible.io/js/script.js"></script>
```

**Alternative (with custom events support):**
```html
<!-- Plausible Analytics with custom events -->
<script defer data-domain="getstorytime.netlify.app" src="https://plausible.io/js/script.tagged-events.js"></script>
```

**Notes:**
- `defer` attribute: Script loads asynchronously (no blocking)
- `data-domain`: Matches Netlify site URL
- `script.tagged-events.js`: Enables custom event tracking

#### Step 2: Update CSP Headers

**Location:** `netlify.toml`

**Modify Content-Security-Policy (line ~39):**
```toml
Content-Security-Policy = """
  default-src 'self';
  script-src 'self' 'unsafe-inline' https://plausible.io;
  style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
  font-src 'self' https://fonts.gstatic.com;
  img-src 'self' data: https:;
  connect-src 'self' https://plausible.io;
  frame-ancestors 'none';
  base-uri 'self';
  form-action 'self';
"""
```

**Changes:**
- `script-src`: Add `https://plausible.io`
- `connect-src`: Add `https://plausible.io`

#### Step 3: Add Custom Event Tracking

**For email signup form submission:**

**Location:** `experimental/landing-pages/index.html` (in existing `<script>` tag or new one)

```javascript
// Track email form submissions
document.addEventListener('DOMContentLoaded', function() {
  const emailForms = document.querySelectorAll('form');

  emailForms.forEach(form => {
    form.addEventListener('submit', function(e) {
      // Fire Plausible event
      if (window.plausible) {
        plausible('Email Signup', {
          props: {
            location: form.dataset.location || 'unknown'
          }
        });
      }
    });
  });
});
```

**For CTA button clicks (optional):**
```javascript
// Track CTA button clicks
document.addEventListener('DOMContentLoaded', function() {
  const ctaButtons = document.querySelectorAll('.cta-button');

  ctaButtons.forEach(button => {
    button.addEventListener('click', function() {
      if (window.plausible) {
        plausible('CTA Clicked', {
          props: {
            button_id: button.id || 'unknown',
            button_text: button.textContent.trim()
          }
        });
      }
    });
  });
});
```

**For email form visibility (scroll tracking):**
```javascript
// Track when email form becomes visible
document.addEventListener('DOMContentLoaded', function() {
  const emailForms = document.querySelectorAll('form');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        if (window.plausible) {
          plausible('Form Viewed', {
            props: {
              location: entry.target.dataset.location || 'unknown'
            }
          });
        }
        // Track only once per form
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 }); // Trigger when 50% visible

  emailForms.forEach(form => observer.observe(form));
});
```

### 5.3 Data Models

**Plausible Event Schema:**
```typescript
interface PlausibleEvent {
  // Automatic properties (sent by Plausible script)
  domain: string;              // "getstorytime.netlify.app"
  url: string;                 // Full page URL
  referrer: string | null;     // Referrer URL
  screen_width: number;        // Device screen width

  // Custom event properties
  name?: string;               // Event name (e.g., "Email Signup")
  props?: {                    // Custom properties (optional)
    [key: string]: string | number;
  };
}
```

**Example Custom Event:**
```json
{
  "name": "Email Signup",
  "url": "https://getstorytime.netlify.app/",
  "props": {
    "location": "hero"
  }
}
```

### 5.4 External Dependencies

**Service:** Plausible Analytics
- **Website:** https://plausible.io
- **Docs:** https://plausible.io/docs
- **Script CDN:** https://plausible.io/js/script.js
- **API Endpoint:** https://plausible.io/api/event
- **Dashboard:** https://plausible.io/getstorytime.netlify.app

**Authentication:**
- Sign up at https://plausible.io/register
- Add site domain: `getstorytime.netlify.app`
- No API key required for basic tracking (script embeds domain)

**Rate Limits:**
- No explicit rate limits for tracking
- 10k pageviews/month included in $9 plan

**Configuration:**
- **Environment Variables:** None required (domain configured in script tag)
- **Secrets:** Plausible account credentials (not stored in repo)

### 5.5 File Structure

```
experimental/landing-pages/
├── index.html                 # Modified with Plausible script + event tracking
└── (other existing files)

netlify.toml                   # Modified CSP headers

docs/
└── prds/
    └── F001-analytics-integration.md  # This document
```

**Changes Summary:**
- `index.html`: Add script tag, add event tracking JavaScript
- `netlify.toml`: Update CSP to allow Plausible domains

---

## 6. User Experience & Design

### 6.1 User Flows

**Flow 1: Visitor arrives and browses**
1. User lands on https://getstorytime.netlify.app
2. Plausible script loads asynchronously (deferred, no blocking)
3. Pageview event sent to Plausible API (< 100ms)
4. User scrolls through content
5. Email form enters viewport → "Form Viewed" event fired
6. User reads content, decides not to sign up, leaves
7. Plausible records bounce (no form submission)

**Flow 2: Visitor converts to signup**
1. User lands on site (pageview tracked)
2. User scrolls to email form ("Form Viewed" event)
3. User enters email and clicks submit button
4. Form submit triggers "Email Signup" event to Plausible
5. Plausible records conversion
6. Dashboard updates within 30 seconds

**Flow 3: Dashboard monitoring**
1. Product owner visits https://plausible.io/getstorytime.netlify.app
2. Sees real-time visitor count, pageviews, top pages
3. Clicks "Goals" tab to see email signup conversions
4. Analyzes conversion rate and traffic sources
5. Identifies optimization opportunities

### 6.2 UI Components & States

**Component: Plausible Script (Invisible to Users)**
- **Loading State:** Script loads asynchronously in background
- **Success State:** Events sent successfully (silent, no UI)
- **Error State:** Script blocked or failed (silent, no UI impact)
- **Fallback:** If Plausible unavailable, site functions normally (graceful degradation)

**No user-facing UI changes required.**

### 6.3 Responsive Design
*Not applicable - analytics script works across all devices*

### 6.4 Accessibility
*Not applicable - analytics script has no accessibility requirements (invisible to users)*

**Note:** Analytics do not impact accessibility scores or screen reader experience.

---

## 7. Edge Cases & Error Handling

### 7.1 Edge Cases

**EDGE-001: Ad Blocker Enabled**
- **Scenario:** User has ad blocker that blocks Plausible script
- **Expected Behavior:** Page loads normally, no analytics data collected
- **Implementation:** Use `defer` attribute and check for `window.plausible` before calling
- **Impact:** ~10-15% of visitors may not be tracked (acceptable for validation)

**EDGE-002: JavaScript Disabled**
- **Scenario:** User has JavaScript disabled in browser
- **Expected Behavior:** Page loads normally (HTML/CSS functional), no analytics
- **Implementation:** `defer` script tag fails gracefully
- **Impact:** <1% of visitors (negligible)

**EDGE-003: Slow Network Connection**
- **Scenario:** User on 3G or slower connection
- **Expected Behavior:** Plausible script loads last (deferred), doesn't block page render
- **Implementation:** `defer` attribute ensures non-blocking load
- **Impact:** No performance degradation

**EDGE-004: Multiple Form Submissions**
- **Scenario:** User submits email form multiple times (double-click, etc.)
- **Expected Behavior:** Each submission tracked separately
- **Implementation:** No deduplication at analytics level (handle in backend if needed)
- **Impact:** Slight inflation of conversion count (acceptable, rare)

**EDGE-005: Form Viewed Multiple Times**
- **Scenario:** User scrolls form in/out of viewport multiple times
- **Expected Behavior:** "Form Viewed" fires only once
- **Implementation:** `observer.unobserve(form)` after first trigger
- **Impact:** Accurate funnel metrics

**EDGE-006: Plausible Service Outage**
- **Scenario:** Plausible.io is down or unreachable
- **Expected Behavior:** Site functions normally, no analytics data collected
- **Implementation:** Script fails silently, no errors thrown
- **Impact:** Temporary data gap (acceptable for validation phase)

### 7.2 Error Scenarios

**ERROR-001: Script Load Failure**
- **Trigger:** Plausible CDN unreachable or blocked
- **User Message:** None (silent failure)
- **Logging:** Browser console may show 404 or CORS error (not visible to users)
- **Recovery:** Site functions normally without analytics

**ERROR-002: Event Send Failure**
- **Trigger:** Network error when sending event to Plausible API
- **User Message:** None (silent failure)
- **Logging:** Browser network tab shows failed request
- **Recovery:** Event lost, but doesn't impact user experience

**ERROR-003: CSP Violation**
- **Trigger:** CSP headers block Plausible script or API calls
- **User Message:** None (script doesn't load)
- **Logging:** Browser console shows CSP violation error
- **Recovery:** Fix CSP headers in netlify.toml, redeploy

### 7.3 Validation Rules

**Event Tracking:**
- Only fire events on actual user actions (not programmatic triggers)
- Check for `window.plausible` existence before calling
- Use `defer` attribute for script tag (non-blocking)

**CSP Headers:**
- Must include `https://plausible.io` in `script-src`
- Must include `https://plausible.io` in `connect-src`
- Test CSP compliance with browser dev tools

---

## 8. Security & Privacy

### 8.1 Authentication & Authorization
**Not applicable** - Analytics are client-side, no authentication required for tracking.

**Dashboard Access:**
- Plausible dashboard protected by email/password (set during signup)
- Optional: Share dashboard via public link (read-only)

### 8.2 Data Protection

**Sensitive Data:** None
- Plausible does **not** collect PII (Personally Identifiable Information)
- No emails, names, or personal data sent to analytics
- Visitor tracking uses hashed IP + User Agent (no cookies)

**Encryption:**
- In transit: HTTPS for all Plausible API calls
- At rest: Plausible encrypts data in EU data centers

**PII Handling:**
- Email signup events track **occurrence only**, not email addresses
- Event properties must **never** include PII
- GDPR/CCPA compliant by design

**Example - Correct:**
```javascript
plausible('Email Signup', { props: { location: 'hero' } });
```

**Example - WRONG (DO NOT DO):**
```javascript
// ❌ NEVER include email or PII in events
plausible('Email Signup', { props: { email: 'user@example.com' } });
```

### 8.3 API Security

**Rate Limiting:** Handled by Plausible (no explicit limits)

**Input Sanitization:**
- Event properties should be validated before sending
- Avoid sending user-generated content in event props

**CORS Policy:**
- Plausible API accepts requests from configured domain only (`getstorytime.netlify.app`)

### 8.4 Secret Management

**Plausible Account Credentials:**
- **Storage:** Not stored in repository
- **Access:** Product owner's password manager
- **Rotation:** Change password every 90 days (standard practice)

**No API Keys Required:**
- Domain-based authentication (script tag includes `data-domain`)
- No secrets needed in code or environment variables

---

## 9. Testing Requirements

### 9.1 Unit Tests

**Test Case 1: Plausible Script Loads**
- **Given:** Page loads with Plausible script tag
- **When:** DOM ready event fires
- **Then:** `window.plausible` function exists

**Test Case 2: Email Signup Event Fires**
- **Given:** Plausible script loaded, email form exists
- **When:** User submits email form
- **Then:** `plausible('Email Signup', {...})` called

**Test Case 3: Form Viewed Event Fires**
- **Given:** Plausible script loaded, email form exists
- **When:** Form scrolls into viewport (50%+ visible)
- **Then:** `plausible('Form Viewed', {...})` called once

**Test Case 4: Graceful Degradation**
- **Given:** Plausible script blocked by ad blocker
- **When:** User submits email form
- **Then:** Form submission succeeds, no JavaScript errors

### 9.2 Integration Tests

**Test Case 1: End-to-End Pageview Tracking**
- **Setup:** Deploy to preview environment, open Plausible dashboard
- **Steps:**
  1. Visit landing page from incognito browser
  2. Wait 60 seconds
  3. Check Plausible dashboard
- **Expected:** Pageview appears in dashboard with correct URL and timestamp

**Test Case 2: Custom Event Tracking**
- **Setup:** Deploy to preview, open Plausible dashboard on "Goals" tab
- **Steps:**
  1. Visit landing page
  2. Scroll to email form (trigger "Form Viewed")
  3. Submit email form (trigger "Email Signup")
  4. Wait 60 seconds
  5. Check dashboard
- **Expected:** Both events appear in Goals tab with accurate counts

**Test Case 3: CSP Compliance**
- **Setup:** Deploy to preview
- **Steps:**
  1. Open browser developer tools (Console tab)
  2. Load landing page
  3. Check for CSP violation errors
- **Expected:** No CSP errors, Plausible script loads successfully

### 9.3 Manual Test Scenarios

**Scenario 1: Happy Path - Visitor to Signup**
1. Open incognito browser window
2. Navigate to https://getstorytime.netlify.app
3. Scroll through page content
4. Scroll to email form (observe form in viewport)
5. Enter test email: test@example.com
6. Click "Get Early Access" button
7. **Expected:**
   - Form submits successfully
   - No JavaScript errors in console
   - Plausible dashboard shows pageview + "Form Viewed" + "Email Signup" events

**Scenario 2: Ad Blocker Enabled**
1. Enable uBlock Origin or similar ad blocker
2. Navigate to landing page
3. Scroll and interact with page
4. Submit email form
5. **Expected:**
   - Page loads and functions normally
   - Email form submission works
   - Plausible may not track (acceptable)
   - No errors or broken functionality

**Scenario 3: Multiple Visitors Simultaneously**
1. Open 3 incognito windows
2. Navigate all to landing page within 10 seconds
3. Wait 60 seconds
4. Check Plausible dashboard
5. **Expected:**
   - Real-time visitor count shows 3 (or drops as windows close)
   - Total pageviews = 3

**Scenario 4: Mobile Device Testing**
1. Open landing page on mobile device (or Chrome DevTools device emulation)
2. Scroll to email form
3. Submit form
4. **Expected:**
   - All events track correctly (same as desktop)
   - No performance issues

### 9.4 Performance Tests

**Test Case 1: Script Load Time**
- **Tool:** Chrome DevTools Network tab
- **Steps:**
  1. Load landing page
  2. Measure Plausible script download time
- **Expected:** <50ms load time (script is <1KB)

**Test Case 2: Lighthouse Score Impact**
- **Tool:** Chrome Lighthouse or GitHub Actions workflow
- **Steps:**
  1. Run Lighthouse before adding Plausible
  2. Run Lighthouse after adding Plausible
  3. Compare Performance scores
- **Expected:** No more than 1-2 point decrease (script is deferred, minimal impact)

**Test Case 3: Page Load Speed**
- **Tool:** Chrome DevTools Performance tab
- **Steps:**
  1. Record page load with Plausible script
  2. Check for render-blocking resources
- **Expected:** Plausible script doesn't block rendering (defer attribute works)

---

## 10. Deployment & Configuration

### 10.1 Environment Variables

**None required** - Plausible uses domain-based authentication.

**Optional (for future API access):**
```bash
# If using Plausible API for programmatic access
PLAUSIBLE_API_KEY=your_api_key_here  # Not needed for basic tracking
```

### 10.2 Feature Flags
**Not applicable** - Analytics should always be enabled in production.

**For testing:**
Could add feature flag to disable analytics in development:
```javascript
const ENABLE_ANALYTICS = window.location.hostname !== 'localhost';
if (ENABLE_ANALYTICS && window.plausible) {
  plausible('Event Name');
}
```

### 10.3 Third-Party Service Setup

**Service: Plausible Analytics**

**Step 1: Create Account**
1. Visit https://plausible.io/register
2. Sign up with email and password
3. Verify email address

**Step 2: Add Site**
1. Click "Add a website"
2. Enter domain: `getstorytime.netlify.app`
3. Select timezone: UTC or local timezone
4. Click "Add site"

**Step 3: Configure Site (Optional)**
1. Go to Site Settings
2. Enable "File Downloads" tracking (if needed)
3. Enable "Outbound Links" tracking (if needed)
4. Set up email reports (optional)

**Step 4: Get Tracking Code**
1. Plausible shows JavaScript snippet
2. Copy snippet (or use from this PRD)
3. Verify `data-domain` matches your domain

**Step 5: Verify Installation**
1. Deploy code with Plausible script
2. Visit your site
3. Go to Plausible dashboard
4. Check for real-time pageview (should appear within 60 seconds)

**Step 6: Set Up Goals (Custom Events)**
1. Go to Site Settings → Goals
2. Add custom event goal: "Email Signup"
3. Add custom event goal: "Form Viewed"
4. Add custom event goal: "CTA Clicked" (optional)

**Step 7: Share Dashboard (Optional)**
1. Go to Site Settings → Visibility
2. Toggle "Public" to enable shared link
3. Copy shared link for stakeholders
4. **Note:** Anyone with link can view data (read-only)

**Verification Steps:**
- Visit site and trigger events
- Check Plausible dashboard for pageviews
- Check Goals tab for custom events
- Verify no CSP errors in browser console

---

## 11. Success Metrics & Validation

### 11.1 KPIs (Key Performance Indicators)

**Metric 1: Unique Visitors**
- **Target:** Track 100% of non-ad-blocked visitors
- **Measurement:** Plausible dashboard → Unique Visitors count
- **Frequency:** Daily review

**Metric 2: Email Signup Conversion Rate**
- **Target:** Establish baseline (likely 2-5%)
- **Calculation:** (Email Signups / Unique Visitors) × 100
- **Measurement:** Plausible Goals → Email Signup count ÷ Unique Visitors
- **Frequency:** Daily review

**Metric 3: Form Visibility Rate**
- **Target:** >80% of visitors scroll to email form
- **Calculation:** (Form Viewed / Pageviews) × 100
- **Measurement:** Plausible Goals → Form Viewed count ÷ Pageviews
- **Frequency:** Weekly review

**Metric 4: Bounce Rate**
- **Target:** <70% (industry average for landing pages)
- **Measurement:** Plausible dashboard → Bounce Rate
- **Frequency:** Daily review

**Metric 5: Traffic Sources**
- **Target:** Identify top 3 sources (direct, social, referral)
- **Measurement:** Plausible dashboard → Top Sources
- **Frequency:** Weekly review

### 11.2 Analytics Events

**Event 1: Pageview (Automatic)**
```json
{
  "name": "pageview",
  "url": "https://getstorytime.netlify.app/"
}
```

**Event 2: Form Viewed**
```json
{
  "name": "Form Viewed",
  "props": {
    "location": "hero"  // or "footer", "mid-page"
  }
}
```

**Event 3: Email Signup**
```json
{
  "name": "Email Signup",
  "props": {
    "location": "hero"  // Identifies which form (if multiple)
  }
}
```

**Event 4: CTA Clicked (Optional)**
```json
{
  "name": "CTA Clicked",
  "props": {
    "button_id": "cta-hero",
    "button_text": "Get Early Access"
  }
}
```

### 11.3 Success Criteria Checklist

**Implementation:**
- [ ] Plausible script added to index.html
- [ ] CSP headers updated in netlify.toml
- [ ] Custom event tracking code added
- [ ] Code deployed to production
- [ ] No JavaScript errors in browser console
- [ ] No CSP violations in browser console

**Functionality:**
- [ ] Pageviews tracked accurately (test with multiple browsers)
- [ ] Email signup events appear in dashboard within 30 seconds
- [ ] Form viewed events fire only once per visitor
- [ ] CTA click events tracked (if implemented)
- [ ] Ad blocker scenario handled gracefully (no errors)

**Performance:**
- [ ] Plausible script loads in <50ms
- [ ] Lighthouse Performance score remains 90+
- [ ] No render-blocking issues
- [ ] Page load time unaffected (<100ms difference)

**Privacy & Security:**
- [ ] No PII sent to Plausible (verified in Network tab)
- [ ] CSP headers correctly configured
- [ ] HTTPS enforced for all Plausible API calls

**Dashboard:**
- [ ] Plausible account created and configured
- [ ] Site added with correct domain
- [ ] Goals configured for custom events
- [ ] Dashboard accessible and showing data
- [ ] (Optional) Shared dashboard link created for stakeholders

**Validation:**
- [ ] 24-hour test period shows consistent data
- [ ] Conversion rate calculation accurate
- [ ] No data gaps or anomalies
- [ ] Team trained on dashboard usage

---

## 12. Implementation Plan

### 12.1 Task Breakdown

**Phase 1: Setup (30 minutes)**
- [ ] Task 1: Create Plausible account at plausible.io
- [ ] Task 2: Add site domain (getstorytime.netlify.app)
- [ ] Task 3: Configure custom event goals in Plausible dashboard
- [ ] Task 4: (Optional) Enable shared dashboard link

**Phase 2: Code Integration (2 hours)**
- [ ] Task 5: Add Plausible script tag to index.html `<head>`
- [ ] Task 6: Update CSP headers in netlify.toml
- [ ] Task 7: Add email form submit event tracking
- [ ] Task 8: Add form visibility event tracking (IntersectionObserver)
- [ ] Task 9: (Optional) Add CTA click event tracking
- [ ] Task 10: Test locally (verify no console errors)

**Phase 3: Testing & Validation (1 hour)**
- [ ] Task 11: Deploy to preview environment (PR preview deploy)
- [ ] Task 12: Test pageview tracking (incognito browser)
- [ ] Task 13: Test custom events (form submit, form viewed)
- [ ] Task 14: Verify CSP compliance (no console errors)
- [ ] Task 15: Test with ad blocker enabled (graceful degradation)
- [ ] Task 16: Run Lighthouse audit (verify performance impact <2 points)

**Phase 4: Production Deployment (30 minutes)**
- [ ] Task 17: Merge PR to master
- [ ] Task 18: Tag release (v1.1.0 or similar)
- [ ] Task 19: Production deploy triggered automatically
- [ ] Task 20: Verify analytics working in production
- [ ] Task 21: Monitor Plausible dashboard for 24 hours

**Phase 5: Documentation & Training (30 minutes)**
- [ ] Task 22: Document dashboard access for team
- [ ] Task 23: Create guide for interpreting metrics
- [ ] Task 24: Share dashboard link with stakeholders
- [ ] Task 25: Update backlog (mark F001 as complete)

**Total Estimated Time:** 4.5 hours (within 1 day estimate)

### 12.2 Dependencies

**Depends on:**
- Netlify deployment working (already in place)
- CSP headers configurable (already in netlify.toml)
- Email form exists on landing page (already in place)

**Blocks:**
- F003: A/B Testing (needs analytics baseline first)
- F005: Email Welcome Sequence (needs conversion tracking)
- Any optimization work (needs data to optimize)

### 12.3 Risks & Mitigation

**Risk 1: Plausible script blocked by ad blockers**
- **Impact:** Medium - 10-15% of visitors not tracked
- **Probability:** High
- **Mitigation:** Acceptable for validation phase; can self-host later if needed
- **Contingency:** Consider proxy script through own domain (future)

**Risk 2: CSP misconfiguration breaks site**
- **Impact:** High - Site could be broken
- **Probability:** Low (with testing)
- **Mitigation:** Test in preview environment first, validate CSP headers
- **Contingency:** Revert CSP change if issues occur

**Risk 3: Performance regression**
- **Impact:** Medium - Lighthouse score drops, SEO affected
- **Probability:** Low (script is <1KB, deferred)
- **Mitigation:** Run Lighthouse before/after, measure impact
- **Contingency:** Remove Plausible if performance drops >5 points

**Risk 4: Plausible service outage**
- **Impact:** Low - Temporary data gap, site still functional
- **Probability:** Low (Plausible has 99.9% uptime SLA)
- **Mitigation:** Site functions normally without analytics
- **Contingency:** Wait for service restoration, no action needed

**Risk 5: Budget constraint**
- **Impact:** Low - $9/month is minimal cost
- **Probability:** Very Low
- **Mitigation:** Cost justified by critical data needs
- **Contingency:** Can cancel subscription after validation phase if needed

---

## 13. Open Questions & Decisions

### Questions (to be resolved before build)
- [x] **Q1:** Which analytics tool should we use?
  - **Answer:** Plausible Analytics (see Section 2.3)
  - **Decision Maker:** Product Owner

- [x] **Q2:** Should we track CTA button clicks?
  - **Answer:** Nice-to-have, implement if time allows
  - **Decision Maker:** Product Owner

- [ ] **Q3:** Should we enable shared public dashboard link?
  - **Answer:** TBD - Decide based on stakeholder needs
  - **Decision Maker:** Product Owner
  - **Options:** Public (anyone with link) vs. Private (login required)

- [ ] **Q4:** What timezone for Plausible dashboard?
  - **Answer:** TBD
  - **Decision Maker:** Product Owner
  - **Recommendation:** UTC (standard) or local timezone

### Decisions Made

**D1:** Use Plausible Analytics (not Google Analytics)
- **Rationale:** Privacy-first approach, no cookie banner, lightweight, aligns with brand values

**D2:** Track Email Signup as primary conversion event
- **Rationale:** Directly measures progress toward 100 signup goal (P0 priority)

**D3:** Use cloud-hosted Plausible (not self-hosted)
- **Rationale:** Faster setup, no infrastructure overhead for Phase 1; can migrate later

**D4:** Implement Form Viewed event (scroll tracking)
- **Rationale:** Enables funnel analysis (visitors → form viewers → signups)

**D5:** Use `defer` attribute for script loading
- **Rationale:** Non-blocking, maintains page performance

**D6:** Update CSP headers to allow Plausible
- **Rationale:** Required for analytics to function

---

## 14. References & Resources

### Documentation
- **Plausible Docs:** https://plausible.io/docs
- **Plausible Integration Guide:** https://plausible.io/docs/integration-guides
- **Plausible Custom Events:** https://plausible.io/docs/custom-event-goals
- **Plausible Script Extensions:** https://plausible.io/docs/script-extensions
- **CSP and Plausible:** https://plausible.io/docs/troubleshoot-integration#content-security-policy-csp

### Related Features
- **F002:** Email Collection Integration (Buttondown) - Will use analytics to measure
- **F003:** A/B Testing Framework - Depends on baseline analytics
- **F005:** Email Welcome Sequence - Conversion tracking required

### Code Examples
- **Plausible Script Tag:** https://plausible.io/docs/plausible-script
- **Event Tracking:** https://plausible.io/docs/custom-event-goals#trigger-custom-events-with-javascript
- **IntersectionObserver:** https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API

### Codebase References
- **index.html:** `/experimental/landing-pages/index.html`
- **netlify.toml:** `/netlify.toml` (CSP headers at line ~39)
- **Workflow:** `/.github/workflows/landing-page-ci-cd.yml`

---

## Appendix

### A. Glossary
- **Pageview:** Single page load event
- **Unique Visitor:** Individual person visiting site (tracked via hashed IP + User Agent)
- **Bounce Rate:** Percentage of visitors who leave after viewing only one page
- **Conversion Rate:** Percentage of visitors who complete desired action (email signup)
- **CSP:** Content Security Policy (HTTP security header)
- **PII:** Personally Identifiable Information (email, name, etc.)
- **GDPR:** General Data Protection Regulation (EU privacy law)
- **CCPA:** California Consumer Privacy Act (US privacy law)

### B. Alternative Event Tracking Approach (Data Attributes)

Instead of JavaScript event listeners, can use Plausible's data-attribute approach:

```html
<!-- Add data attribute to form -->
<form data-plausible-event="Email Signup" data-location="hero">
  <!-- form fields -->
</form>

<!-- Add data attribute to CTA button -->
<button class="cta-button" data-plausible-event="CTA Clicked" data-button-id="hero-cta">
  Get Early Access
</button>
```

**Pros:**
- Simpler implementation (no JavaScript required)
- Declarative (easier to see what's tracked)

**Cons:**
- Less control over event timing
- Harder to track visibility events (IntersectionObserver not possible)

**Recommendation:** Use JavaScript approach for full control and flexibility.

### C. Change Log
- **2026-01-24:** Initial PRD created with comprehensive market analysis
- **2026-01-24:** Added detailed implementation plan and test scenarios
- **2026-01-24:** Completed all sections except open questions (Q3, Q4)

---

## PRD Completeness Checklist (for Claude)

- [x] Executive summary clear and concise
- [x] User stories with acceptance criteria
- [x] All functional requirements specified
- [x] Technical architecture documented
- [x] API contracts defined (Plausible events)
- [x] Data models specified (PlausibleEvent schema)
- [x] UI/UX flows documented (visitor journeys)
- [x] Edge cases identified (6 edge cases, 3 error scenarios)
- [x] Error handling specified (graceful degradation)
- [x] Security considerations addressed (privacy-first, no PII)
- [x] Testing requirements comprehensive (unit, integration, manual, performance)
- [x] Deployment steps clear (5-phase implementation plan)
- [x] Success metrics defined (5 KPIs + events)
- [x] Implementation plan realistic (4.5 hours total)
- [x] Market analysis complete (5 options evaluated)
- [ ] Minor open questions remaining (Q3: public dashboard, Q4: timezone)

**Ready for Build:** ☑ Yes - Pending final decisions on Q3 & Q4 (non-blocking)

**Note:** Q3 and Q4 are configuration decisions that can be made during/after implementation. They do not block development work.
