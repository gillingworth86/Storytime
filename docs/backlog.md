# Storytime Product Backlog

**Last Updated:** 2026-01-25
**Current Phase:** Phase 1 - Landing Page Validation
**Goal:** 100 email signups in 3 weeks

---

## Priority Framework

- **P0:** Critical for current phase success
- **P1:** High value, near-term delivery
- **P2:** Medium value, future phases
- **P3:** Nice to have, low priority

---

## Phase 1: Landing Page Validation

### P0 - Critical Path

#### F002: Email Collection Integration (Buttondown)
**Status:** 🔄 In Progress (separate session)
**Priority:** P0
**Effort:** Small

Integrate Buttondown email service to collect and manage email signups. Replace placeholder forms with functional email capture.

**Success Metrics:**
- Email submissions successfully captured in Buttondown
- Confirmation emails sent automatically
- Double opt-in flow working
- Export capability for email list

---

### P1 - High Value

#### F003: Landing Page A/B Testing Framework
**Status:** Not Started
**Priority:** P1
**Effort:** Medium

Implement lightweight A/B testing to optimize messaging, CTAs, and page layout for maximum conversions. Test variations of hero copy, button text, and value propositions.

**Success Metrics:**
- Test at least 2 variations of hero section
- Statistical significance (95% confidence)
- Identify winning variant
- Improve conversion rate by 20%+

---

#### F004: Social Proof Section
**Status:** 🔄 In Progress (this session)
**Priority:** P1
**Effort:** Small
**PRD:** [F004-social-proof-section.md](prds/F004-social-proof-section.md)

Add testimonials, user quotes, or early tester feedback to build trust and credibility. Reduces skepticism and increases signup likelihood.

**Success Metrics:**
- Display 3-5 authentic testimonials
- Include photos/names (with permission)
- Position strategically on landing page
- A/B test impact on conversion rate

---

#### F005: Email Welcome Sequence
**Status:** Not Started
**Priority:** P1
**Effort:** Small

Create automated email sequence for new signups: confirmation, welcome message, value delivery, and engagement nurturing.

**Success Metrics:**
- 3-5 email sequence created
- 40%+ open rate on welcome email
- 10%+ click-through rate
- Reduce unsubscribe rate below 2%

---

### P2 - Future Phases

#### F006: Landing Page SEO Optimization
**Status:** Not Started
**Priority:** P2
**Effort:** Small

Optimize meta tags, Open Graph tags, schema markup, and semantic HTML for search engine visibility and social sharing.

**Success Metrics:**
- Google PageSpeed score 90+
- All meta tags properly configured
- Twitter/Facebook cards working
- Lighthouse SEO score 95+

---

#### F007: FAQ Section
**Status:** Not Started
**Priority:** P2
**Effort:** Small

Add Frequently Asked Questions section to address common concerns about privacy, story content, pricing expectations, and launch timeline.

**Success Metrics:**
- 8-10 common questions answered
- Reduces support email volume
- Improves time-on-page
- Schema markup for FAQ rich results

---

#### F008: Referral Program
**Status:** Not Started
**Priority:** P2
**Effort:** Medium

Enable early signups to refer friends in exchange for early access, bonus features, or discounts. Viral growth mechanism.

**Success Metrics:**
- Unique referral links per signup
- Track referral conversions
- 15%+ of signups come from referrals
- Incentive structure defined

---

#### F009: Exit Intent Popup
**Status:** Not Started
**Priority:** P2
**Effort:** Small

Capture abandoning visitors with last-chance offer or alternative CTA (e.g., "Get notified when we launch" vs immediate signup).

**Success Metrics:**
- Trigger on exit intent behavior
- Convert 5-10% of abandoners
- A/B test messaging
- Don't annoy returning users

---

## Phase 2: Full Application (Future)

### P3 - Planning Stage

#### F010: User Authentication System
**Status:** Not Started
**Priority:** P3
**Effort:** Large

Build secure authentication for parent accounts: email/password, OAuth (Google, Apple), session management, and password reset flows.

**Success Metrics:**
- Email/password registration working
- OAuth integration (Google minimum)
- Password reset via email
- Session persistence and security

---

#### F011: Story Generation Engine (MVP)
**Status:** Not Started
**Priority:** P3
**Effort:** Large

Core feature: Generate personalized bedtime stories using AI (Claude API). Include character customization, story themes, and reading level adaptation.

**Success Metrics:**
- Generate story in <30 seconds
- Story quality rated 4+ stars by parents
- Personalization elements working
- Cost per story <$0.10

---

#### F012: Story Universe Persistence
**Status:** Not Started
**Priority:** P3
**Effort:** Large

Maintain consistent characters, settings, and plot threads across multiple stories. Create sense of ongoing narrative.

**Success Metrics:**
- Character details persist across stories
- Story callback references work
- Parent and child satisfaction high
- Technical architecture scalable

---

#### F013: Parent Dashboard
**Status:** Not Started
**Priority:** P3
**Effort:** Medium

Allow parents to view story history, manage child profiles, customize preferences, and track reading activity.

**Success Metrics:**
- View all generated stories
- Edit child preferences
- Download/print stories
- Activity tracking dashboard

---

## Completed Features

### Phase 1 Completed

#### F001: Analytics Integration (Plausible)
**Status:** ✅ Completed
**Priority:** P0
**Effort:** Small
**Completed:** 2026-01-24
**Owner:** Claude

Integrated Plausible Analytics to track visitor behavior, conversion rates, and email signup funnel performance.

**Deliverables:**
- ✅ Plausible script integrated into index.html
- ✅ CSP headers configured in vercel.json
- ✅ Custom event tracking (Email Signup, Form Viewed)
- ✅ Test suite created (test-analytics.html)
- ✅ Test report documenting all validations
- ✅ PRD updated to reflect Vercel deployment

**Documentation:**
- [PRD: F001-analytics-integration.md](prds/F001-analytics-integration.md)
- [Test Report: F001-TEST-REPORT.md](F001-TEST-REPORT.md)

---

---

## Feature Request Template

When adding new features to backlog, use this format:

```markdown
#### FXXX: Feature Name
**Status:** Not Started | In Progress | Blocked | Completed
**Priority:** P0 | P1 | P2 | P3
**Effort:** Small (<1 week) | Medium (1-2 weeks) | Large (2+ weeks)

[2-3 sentence description of the feature and why it matters]

**Success Metrics:**
- Metric 1
- Metric 2
- Metric 3
```

---

## Notes

- Feature IDs are sequential (F001, F002, etc.)
- Priority may change based on validation learnings
- Effort estimates are for single developer
- All P0 features must complete before Phase 2
- Review backlog weekly during Phase 1

---

## Future Considerations (Not included in F002)

Not included in F002, consider for future:
Name field collection (Q-006 revisited)
Personalization opportunity
Higher friction (test impact)
Email preferences
Frequency selection
Topic interests
Child age/gender
Welcome email series
Email #1: Immediate confirmation
Email #2: Story about product vision
Email #3: Sneak peek at features
Email #4: Reminder to whitelist
Referral program
Share link with friends
Rewards for referrals
Move up waitlist
Waitlist position
"You're #47 in line!"
Gamification
Urgency/FOMO
A/B testing
Different CTAs
Different form copy
Different value props
Advanced analytics
Heatmaps
Session recordings
Funnel analysis
Email verification (beyond double opt-in)
Real-time email validation API
Catch typos (did you mean @gmail.com?)
Block disposable emails
Progressive profiling
Collect additional info over time
Not all at once (reduce friction)
These should have their own PRDs when prioritized
