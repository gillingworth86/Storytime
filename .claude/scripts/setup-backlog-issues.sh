#!/bin/bash
# Setup GitHub Issues for Storytime Backlog
# Run this script once to create all labels and issues
# Requires: gh CLI authenticated (run `gh auth login` first)

set -e

echo "=== Setting up Storytime Backlog in GitHub Issues ==="

# Check gh is available
if ! command -v gh &> /dev/null; then
    echo "Error: gh CLI not found. Install from https://cli.github.com/"
    exit 1
fi

# Check authentication
if ! gh auth status &> /dev/null; then
    echo "Error: Not authenticated. Run 'gh auth login' first."
    exit 1
fi

echo ""
echo "Creating labels..."

# Priority labels
gh label create "backlog" --description "Backlog item" --color "0E8A16" --force
gh label create "priority:p0" --description "Critical/blocking" --color "B60205" --force
gh label create "priority:p1" --description "High value" --color "D93F0B" --force
gh label create "priority:p2" --description "Medium value" --color "FBCA04" --force
gh label create "priority:p3" --description "Nice to have" --color "C5DEF5" --force

# Status labels
gh label create "status:available" --description "Ready to be picked up" --color "0E8A16" --force
gh label create "status:in-progress" --description "Currently being worked on" --color "1D76DB" --force
gh label create "status:blocked" --description "Waiting on dependency" --color "E4E669" --force

# Type labels
gh label create "type:prd" --description "Requires PRD creation" --color "D4C5F9" --force
gh label create "type:implementation" --description "Ready for coding" --color "BFD4F2" --force
gh label create "type:bug" --description "Bug fix" --color "D73A4A" --force
gh label create "type:docs" --description "Documentation" --color "0075CA" --force

# Phase labels
gh label create "phase:1-landing" --description "Phase 1: Landing page" --color "EDEDED" --force
gh label create "phase:2-app" --description "Phase 2: Full application" --color "BFDADC" --force

echo "Labels created!"
echo ""
echo "Creating issues..."

# F002: Email Collection (P0) - PRD Done, Ready for Implementation
gh issue create \
    --title "[F002] Email Collection Integration (Buttondown)" \
    --label "backlog,priority:p0,status:available,type:implementation,phase:1-landing" \
    --body "## Feature: F002 - Email Collection Integration

**Priority:** P0 (Critical Path)
**Type:** Implementation (PRD Complete)
**Phase:** 1-landing
**Effort:** Small (1-2 days)

### Description
Integrate Buttondown email service to collect and manage email signups. Replace placeholder forms with functional email capture. PRD is complete and ready for implementation.

### PRD Location
\`docs/prds/F002-email-collection.md\`

### Success Criteria
- [ ] Email submissions successfully captured in Buttondown
- [ ] Confirmation emails sent automatically (within 2 min)
- [ ] Double opt-in flow working
- [ ] Success/error UI states implemented
- [ ] All 3 forms functional (hero, mid-page, footer)
- [ ] Export capability for email list
- [ ] Analytics tracking working

### Dependencies

**Depends on:**
- F001 Analytics Integration ✅ (Completed)

**Blocks:**
- F003 A/B Testing Framework
- F004 Social Proof Section
- F005 Email Welcome Sequence

### Implementation Tasks
See PRD Section 12 for detailed task breakdown.

---
*Created from backlog migration on $(date +%Y-%m-%d)*"

echo "Created F002"

# F003: A/B Testing (P1)
gh issue create \
    --title "[F003] Landing Page A/B Testing Framework" \
    --label "backlog,priority:p1,status:blocked,type:prd,phase:1-landing" \
    --body "## Feature: F003 - Landing Page A/B Testing Framework

**Priority:** P1 (High Value)
**Type:** PRD Required
**Phase:** 1-landing
**Effort:** Medium (1-2 weeks)

### Description
Implement lightweight A/B testing to optimize messaging, CTAs, and page layout for maximum conversions. Test variations of hero copy, button text, and value propositions.

### Success Criteria
- [ ] Test at least 2 variations of hero section
- [ ] Statistical significance (95% confidence)
- [ ] Identify winning variant
- [ ] Improve conversion rate by 20%+

### Dependencies

**Depends on:**
- #[F002 issue number] - Email Collection must be working to measure conversions

**Blocks:**
- None directly

### Notes
- Consider tools: Google Optimize, Optimizely, or custom implementation
- Plausible Analytics already integrated for tracking

---
*Created from backlog migration on $(date +%Y-%m-%d)*"

echo "Created F003"

# F004: Social Proof (P1)
gh issue create \
    --title "[F004] Social Proof Section" \
    --label "backlog,priority:p1,status:blocked,type:prd,phase:1-landing" \
    --body "## Feature: F004 - Social Proof Section

**Priority:** P1 (High Value)
**Type:** PRD Required
**Phase:** 1-landing
**Effort:** Small (<1 week)

### Description
Add testimonials, user quotes, or early tester feedback to build trust and credibility. Reduces skepticism and increases signup likelihood.

### Success Criteria
- [ ] Display 3-5 authentic testimonials
- [ ] Include photos/names (with permission)
- [ ] Position strategically on landing page
- [ ] A/B test impact on conversion rate

### Dependencies

**Depends on:**
- #[F002 issue number] - Need email collection working to measure impact

**Blocks:**
- None directly

### Notes
- Need to collect testimonials from early testers
- Consider fake/placeholder testimonials for testing only (not production)

---
*Created from backlog migration on $(date +%Y-%m-%d)*"

echo "Created F004"

# F005: Email Welcome Sequence (P1) - PRD can start now
gh issue create \
    --title "[F005] Email Welcome Sequence" \
    --label "backlog,priority:p1,status:available,type:prd,phase:1-landing" \
    --body "## Feature: F005 - Email Welcome Sequence

**Priority:** P1 (High Value)
**Type:** PRD Required (can start now, implementation needs F002)
**Phase:** 1-landing
**Effort:** Small (<1 week)

### Description
Create automated email sequence for new signups: confirmation, welcome message, value delivery, and engagement nurturing.

### Success Criteria
- [ ] 3-5 email sequence created
- [ ] 40%+ open rate on welcome email
- [ ] 10%+ click-through rate
- [ ] Reduce unsubscribe rate below 2%

### Dependencies

**Depends on:**
- F002 Email Collection - for implementation (but PRD can start now)

**Blocks:**
- None

### PRD Notes
PRD can be created independently of F002 implementation. The email content, timing, and strategy can be defined now. Implementation will happen in Buttondown after F002 is complete.

### Suggested Email Sequence
1. **Email 1 (Immediate):** Confirmation + welcome
2. **Email 2 (Day 1):** Product vision + what to expect
3. **Email 3 (Day 3):** Sneak peek at features
4. **Email 4 (Day 7):** Engagement check + feedback request

---
*Created from backlog migration on $(date +%Y-%m-%d)*"

echo "Created F005"

# F006: SEO Optimization (P2)
gh issue create \
    --title "[F006] Landing Page SEO Optimization" \
    --label "backlog,priority:p2,status:available,type:prd,phase:1-landing" \
    --body "## Feature: F006 - Landing Page SEO Optimization

**Priority:** P2 (Medium Value)
**Type:** PRD Required
**Phase:** 1-landing
**Effort:** Small (<1 week)

### Description
Optimize meta tags, Open Graph tags, schema markup, and semantic HTML for search engine visibility and social sharing.

### Success Criteria
- [ ] Google PageSpeed score 90+
- [ ] All meta tags properly configured
- [ ] Twitter/Facebook cards working
- [ ] Lighthouse SEO score 95+

### Dependencies

**Depends on:**
- None (can work on existing landing page)

**Blocks:**
- None directly

---
*Created from backlog migration on $(date +%Y-%m-%d)*"

echo "Created F006"

# F007: FAQ Section (P2)
gh issue create \
    --title "[F007] FAQ Section" \
    --label "backlog,priority:p2,status:available,type:prd,phase:1-landing" \
    --body "## Feature: F007 - FAQ Section

**Priority:** P2 (Medium Value)
**Type:** PRD Required
**Phase:** 1-landing
**Effort:** Small (<1 week)

### Description
Add Frequently Asked Questions section to address common concerns about privacy, story content, pricing expectations, and launch timeline.

### Success Criteria
- [ ] 8-10 common questions answered
- [ ] Reduces support email volume
- [ ] Improves time-on-page
- [ ] Schema markup for FAQ rich results

### Dependencies

**Depends on:**
- None

**Blocks:**
- None

### Notes
Landing page already has a FAQ accordion component that can be expanded.

---
*Created from backlog migration on $(date +%Y-%m-%d)*"

echo "Created F007"

# F008: Referral Program (P2)
gh issue create \
    --title "[F008] Referral Program" \
    --label "backlog,priority:p2,status:blocked,type:prd,phase:1-landing" \
    --body "## Feature: F008 - Referral Program

**Priority:** P2 (Medium Value)
**Type:** PRD Required
**Phase:** 1-landing
**Effort:** Medium (1-2 weeks)

### Description
Enable early signups to refer friends in exchange for early access, bonus features, or discounts. Viral growth mechanism.

### Success Criteria
- [ ] Unique referral links per signup
- [ ] Track referral conversions
- [ ] 15%+ of signups come from referrals
- [ ] Incentive structure defined

### Dependencies

**Depends on:**
- F002 Email Collection - need subscriber system first

**Blocks:**
- None

---
*Created from backlog migration on $(date +%Y-%m-%d)*"

echo "Created F008"

# F009: Exit Intent Popup (P2)
gh issue create \
    --title "[F009] Exit Intent Popup" \
    --label "backlog,priority:p2,status:blocked,type:prd,phase:1-landing" \
    --body "## Feature: F009 - Exit Intent Popup

**Priority:** P2 (Medium Value)
**Type:** PRD Required
**Phase:** 1-landing
**Effort:** Small (<1 week)

### Description
Capture abandoning visitors with last-chance offer or alternative CTA (e.g., \"Get notified when we launch\" vs immediate signup).

### Success Criteria
- [ ] Trigger on exit intent behavior
- [ ] Convert 5-10% of abandoners
- [ ] A/B test messaging
- [ ] Don't annoy returning users

### Dependencies

**Depends on:**
- F002 Email Collection - popup needs working email capture

**Blocks:**
- None

---
*Created from backlog migration on $(date +%Y-%m-%d)*"

echo "Created F009"

# F010: User Authentication (P3)
gh issue create \
    --title "[F010] User Authentication System" \
    --label "backlog,priority:p3,status:blocked,type:prd,phase:2-app" \
    --body "## Feature: F010 - User Authentication System

**Priority:** P3 (Planning Stage)
**Type:** PRD Required
**Phase:** 2-app
**Effort:** Large (2+ weeks)

### Description
Build secure authentication for parent accounts: email/password, OAuth (Google, Apple), session management, and password reset flows.

### Success Criteria
- [ ] Email/password registration working
- [ ] OAuth integration (Google minimum)
- [ ] Password reset via email
- [ ] Session persistence and security

### Dependencies

**Depends on:**
- Phase 1 validation success (100 email signups)
- Decision to proceed with Phase 2

**Blocks:**
- F011 Story Generation Engine
- F012 Story Universe Persistence
- F013 Parent Dashboard

---
*Created from backlog migration on $(date +%Y-%m-%d)*"

echo "Created F010"

# F011: Story Generation (P3)
gh issue create \
    --title "[F011] Story Generation Engine (MVP)" \
    --label "backlog,priority:p3,status:blocked,type:prd,phase:2-app" \
    --body "## Feature: F011 - Story Generation Engine (MVP)

**Priority:** P3 (Planning Stage)
**Type:** PRD Required
**Phase:** 2-app
**Effort:** Large (2+ weeks)

### Description
Core feature: Generate personalized bedtime stories using AI (Claude API). Include character customization, story themes, and reading level adaptation.

### Success Criteria
- [ ] Generate story in <30 seconds
- [ ] Story quality rated 4+ stars by parents
- [ ] Personalization elements working
- [ ] Cost per story <\$0.10

### Dependencies

**Depends on:**
- F010 User Authentication
- Phase 1 validation success

**Blocks:**
- F012 Story Universe Persistence

---
*Created from backlog migration on $(date +%Y-%m-%d)*"

echo "Created F011"

# F012: Story Universe Persistence (P3)
gh issue create \
    --title "[F012] Story Universe Persistence" \
    --label "backlog,priority:p3,status:blocked,type:prd,phase:2-app" \
    --body "## Feature: F012 - Story Universe Persistence

**Priority:** P3 (Planning Stage)
**Type:** PRD Required
**Phase:** 2-app
**Effort:** Large (2+ weeks)

### Description
Maintain consistent characters, settings, and plot threads across multiple stories. Create sense of ongoing narrative.

### Success Criteria
- [ ] Character details persist across stories
- [ ] Story callback references work
- [ ] Parent and child satisfaction high
- [ ] Technical architecture scalable

### Dependencies

**Depends on:**
- F010 User Authentication
- F011 Story Generation Engine

**Blocks:**
- None

---
*Created from backlog migration on $(date +%Y-%m-%d)*"

echo "Created F012"

# F013: Parent Dashboard (P3)
gh issue create \
    --title "[F013] Parent Dashboard" \
    --label "backlog,priority:p3,status:blocked,type:prd,phase:2-app" \
    --body "## Feature: F013 - Parent Dashboard

**Priority:** P3 (Planning Stage)
**Type:** PRD Required
**Phase:** 2-app
**Effort:** Medium (1-2 weeks)

### Description
Allow parents to view story history, manage child profiles, customize preferences, and track reading activity.

### Success Criteria
- [ ] View all generated stories
- [ ] Edit child preferences
- [ ] Download/print stories
- [ ] Activity tracking dashboard

### Dependencies

**Depends on:**
- F010 User Authentication
- F011 Story Generation Engine

**Blocks:**
- None

---
*Created from backlog migration on $(date +%Y-%m-%d)*"

echo "Created F013"

echo ""
echo "=== Setup Complete ==="
echo ""
echo "Next steps:"
echo "1. Update dependency references in issues (replace [F002 issue number] with actual numbers)"
echo "2. View issues: gh issue list --label backlog"
echo "3. Start working: Follow .claude/skills/backlog-management.md"
