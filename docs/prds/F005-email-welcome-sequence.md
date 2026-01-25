# PRD F005: Email Welcome Sequence

**Feature:** Email Welcome Sequence for New Subscribers
**Status:** Draft
**Priority:** P1 (High Value)
**Effort:** Small (<1 week)
**Owner:** [To be assigned]
**Created:** 2026-01-25
**Last Updated:** 2026-01-25

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Implementation Strategy](#2-implementation-strategy)
3. [User Stories](#3-user-stories)
4. [Functional Requirements](#4-functional-requirements)
5. [Email Content Specifications](#5-email-content-specifications)
6. [User Experience & Design](#6-user-experience--design)
7. [Edge Cases & Error Handling](#7-edge-cases--error-handling)
8. [Testing Requirements](#8-testing-requirements)
9. [Success Metrics & Validation](#9-success-metrics--validation)
10. [Implementation Plan](#10-implementation-plan)
11. [Automation Upgrade Path](#11-automation-upgrade-path)
12. [Open Questions & Decisions](#12-open-questions--decisions)

---

## 1. Executive Summary

### 1.1 Problem Statement

**Current State:**
After a visitor signs up on the Storytime landing page (F002), they receive only a double opt-in confirmation email from Kit. There is no:
- Welcome message explaining what to expect
- Value delivery to build excitement
- Engagement nurturing to maintain interest
- Relationship building before product launch

**Impact:**
- Subscribers may forget they signed up
- No ongoing engagement during waitlist period
- Missed opportunity to build brand affinity
- Higher unsubscribe risk when launch email arrives
- No feedback loop with early audience

### 1.2 Proposed Solution

Create a **4-email welcome sequence** that engages new subscribers from signup through launch readiness:

| Email | Timing | Purpose |
|-------|--------|---------|
| Confirmation/Welcome | Immediate (on signup) | Confirm subscription + welcome + story preview |
| #2 Vision | Day 2 (after confirm) | Share product story, build emotional connection |
| #3 Sneak Peek | Day 5 | Preview features, generate excitement |
| #4 Engagement | Day 10 | Request feedback, deepen relationship |

**Key Decision: Combined Confirmation + Welcome**
- The double opt-in confirmation email does double duty: confirms AND welcomes
- Delivers immediate value (story excerpt) before they even confirm
- Reduces total emails from 5 to 4 (less inbox clutter)
- Higher confirmation rates (more compelling than bland "please confirm")

**Implementation Approach: Manual-First**
- **Phase A (Now):** Confirmation email via Kit settings; follow-ups sent manually
- **Phase B (After validation):** Automate once 100 signups achieved

### 1.3 Success Criteria

| Metric | Target | Measurement |
|--------|--------|-------------|
| Confirmation email open rate | >60% | Kit analytics |
| Confirmation rate (click to confirm) | >50% | Kit analytics |
| Sequence open rate (avg) | >40% | Kit analytics |
| Click-through rate | >10% | Kit analytics |
| Unsubscribe rate | <2% | Kit analytics |
| Reply rate | >5% | Manual count |
| Sequence completion | >70% | Confirmed subscribers receiving all 3 follow-ups |

### 1.4 Scope

**In Scope (F005):**
- ✅ 4-email sequence content and copy
- ✅ Email timing strategy
- ✅ Subject line optimization
- ✅ Manual sending process documentation
- ✅ Email templates in Kit
- ✅ Tracking and metrics setup
- ✅ Automation requirements (for future Phase B)

**Out of Scope:**
- ❌ Automated sending (deferred to Phase B - see SD-001)
- ❌ Personalization beyond first name
- ❌ Segmentation based on behavior
- ❌ A/B testing of email variants
- ❌ Advanced analytics (heatmaps, etc.)

### 1.5 Dependencies

**Depends on:**
- F002 Email Collection Integration (must be complete)
- Kit account configured with double opt-in

**Blocks:**
- None directly (F008 Referral could integrate with sequence)

### 1.6 Cost Considerations

**Phase A (Manual):** $0 additional cost
- Uses existing Kit free/basic tier
- Manual sending via dashboard

**Phase B (Automated):** Decision deferred (see SD-001 in backlog)
- Kit Creator: ~$29/mo (automations + sequences)
- Kit Free: $0 (limited automations)

**Decision trigger:** 100 signups achieved OR manual sending unsustainable

---

## 2. Implementation Strategy

### 2.1 Two-Phase Approach

```
┌─────────────────────────────────────────────────────────────┐
│                    F005 IMPLEMENTATION                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  PHASE A: Manual (Now)              PHASE B: Automated       │
│  ─────────────────────              ─────────────────────    │
│                                                              │
│  ┌─────────────────┐                ┌─────────────────┐     │
│  │ Email templates │                │ Platform choice │     │
│  │ created in      │    ──────►    │ (Kit Free or   │     │
│  │ Kit             │   100 signups  │  Kit Creator)  │     │
│  └────────┬────────┘    achieved    └────────┬────────┘     │
│           │                                   │              │
│           ▼                                   ▼              │
│  ┌─────────────────┐                ┌─────────────────┐     │
│  │ Manual trigger: │                │ Auto trigger:   │     │
│  │ Check dashboard │                │ On subscription │     │
│  │ daily, send to  │                │ confirmation    │     │
│  │ new confirms    │                │                 │     │
│  └────────┬────────┘                └────────┬────────┘     │
│           │                                   │              │
│           ▼                                   ▼              │
│  ┌─────────────────┐                ┌─────────────────┐     │
│  │ Track in        │                │ Full analytics  │     │
│  │ spreadsheet     │                │ in platform     │     │
│  └─────────────────┘                └─────────────────┘     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Phase A: Manual Process

**Daily workflow (5-10 minutes):**

1. **Check Kit dashboard** for newly confirmed subscribers
2. **Note confirmation date** for each new subscriber
3. **Send appropriate email** based on days since confirmation:
   - Day 0: Send Email #1 (Welcome)
   - Day 2: Send Email #2 (Vision)
   - Day 5: Send Email #3 (Sneak Peek)
   - Day 10: Send Email #4 (Engagement)
4. **Log in tracking spreadsheet:**
   - Subscriber email (or ID)
   - Email sent
   - Date sent
   - Opens/clicks (check next day)

**Tracking spreadsheet columns:**
| Subscriber | Confirmed | Email 1 | Email 2 | Email 3 | Email 4 | Notes |
|------------|-----------|---------|---------|---------|---------|-------|
| user@... | 2026-01-25 | ✅ 01-25 | ⏳ 01-27 | ⏳ 01-30 | ⏳ 02-04 | |

### 2.3 Phase A Sustainability Limits

Manual sending becomes unsustainable when:
- >10 new subscribers/day (50+ minutes daily)
- >50 active subscribers in sequence (complex tracking)
- Missed sends due to human error

**Trigger for Phase B:** Any of the above OR 100 total signups

---

## 3. User Stories

### 3.1 Primary: New Subscriber Welcome

**As a** new Storytime subscriber
**I want** to receive a welcoming email after I confirm my subscription
**So that** I feel valued and know what to expect

**Acceptance Criteria:**
1. Email arrives within 24 hours of confirmation (Phase A) / immediately (Phase B)
2. Email addresses me by first name (if available) or friendly generic
3. Email sets clear expectations for communication frequency
4. Email provides immediate value (story sample or insight)
5. Email has clear, recognizable Storytime branding
6. Email works correctly on mobile devices
7. Unsubscribe link is present and functional

### 3.2 Secondary: Ongoing Engagement

**As a** waitlist subscriber
**I want** to receive periodic updates about Storytime
**So that** I stay excited and don't forget about the product

**Acceptance Criteria:**
1. I receive 3-4 emails over 10 days (not overwhelming)
2. Each email provides new, interesting content
3. Emails build on each other (narrative arc)
4. I can reply to emails and expect a response
5. I can unsubscribe at any time
6. Emails don't feel spammy or overly promotional

### 3.3 Tertiary: Feedback Collection

**As a** product owner
**I want** subscribers to share feedback during the welcome sequence
**So that** I can validate assumptions and improve the product

**Acceptance Criteria:**
1. At least one email explicitly asks for feedback
2. Reply mechanism is clear and easy
3. Feedback is tracked and reviewed
4. Engaged subscribers can be identified for follow-up
5. Response rate of >5% achieved

---

## 4. Functional Requirements

### 4.1 Email Content Requirements

**REQ-001: Four-Email Sequence**
- **Description:** Create exactly 4 emails with distinct purposes
- **Priority:** Must-have
- **Acceptance:** All 4 emails written, reviewed, and loaded in Kit

**REQ-002: Consistent Branding**
- **Description:** All emails match Storytime visual identity
- **Priority:** Must-have
- **Acceptance:**
  - Color scheme: midnight (#0f1419), gold (#fbbf24), cream (#fef3c7)
  - Font: Clean, readable (system fonts for email compatibility)
  - Tone: Warm, magical, parent-friendly

**REQ-003: Mobile Optimization**
- **Description:** Emails render correctly on mobile devices
- **Priority:** Must-have
- **Acceptance:**
  - Single-column layout
  - Minimum 16px font size
  - Touch-friendly buttons (min 44px)
  - Images scale appropriately

**REQ-004: Personalization**
- **Description:** Use subscriber's first name when available
- **Priority:** Should-have
- **Acceptance:**
  - Kit merge tag: `{{ subscriber.first_name }}`
  - Fallback: "there" or "friend" if no name

### 4.2 Timing Requirements

**REQ-005: Email Timing Schedule**
- **Description:** Emails sent at optimal intervals
- **Priority:** Must-have
- **Schedule:**
  | Email | Day | Time (subscriber local) |
  |-------|-----|------------------------|
  | #1 Welcome | 0 (same day as confirm) | Within 24h |
  | #2 Vision | 2 | Morning (9-10am) |
  | #3 Sneak Peek | 5 | Morning (9-10am) |
  | #4 Engagement | 10 | Morning (9-10am) |

**REQ-006: Timezone Handling (Phase A)**
- **Description:** Send during reasonable hours
- **Priority:** Should-have
- **Acceptance:**
  - Phase A: Send all emails ~9am AEST (target market)
  - Phase B: Use Kit's send-time optimization if available

### 4.3 Tracking Requirements

**REQ-007: Open Tracking**
- **Description:** Track email open rates
- **Priority:** Must-have
- **Acceptance:** Kit's built-in open tracking enabled

**REQ-008: Click Tracking**
- **Description:** Track link clicks within emails
- **Priority:** Must-have
- **Acceptance:** All links use Kit's click tracking

**REQ-009: Manual Tracking Spreadsheet (Phase A)**
- **Description:** Maintain spreadsheet of sequence progress
- **Priority:** Must-have (Phase A only)
- **Acceptance:**
  - Google Sheet or similar
  - Updated daily
  - Tracks: subscriber, confirm date, emails sent, opens, clicks

### 4.4 Compliance Requirements

**REQ-010: Unsubscribe Link**
- **Description:** Every email includes one-click unsubscribe
- **Priority:** Must-have (legal requirement)
- **Acceptance:** Kit auto-includes unsubscribe link

**REQ-011: Physical Address**
- **Description:** Include physical mailing address (CAN-SPAM)
- **Priority:** Must-have (legal requirement)
- **Acceptance:** Footer includes address or Kit default

**REQ-012: Reply-To Address**
- **Description:** Replies go to monitored inbox
- **Priority:** Must-have
- **Acceptance:** Reply-to set to active email address

---

## 5. Email Content Specifications

### 5.1 Confirmation/Welcome Email (Combined)

**Purpose:** Confirm subscription + welcome + deliver immediate value

**Timing:** Immediate (sent automatically by Kit on signup)

**Type:** Double opt-in confirmation email (requires click to confirm)

**Subject Line:**
- Primary: "Confirm your spot in the Storytime universe ✨"
- Alt: "One click to start your story adventure"

**Preview Text:** "Click to confirm + get a sneak peek of the magic inside..."

**Content Structure:**

```
HEADER
[Storytime text header - simple, not image-heavy for deliverability]

GREETING
Hi there,

WELCOME + CONFIRMATION
Welcome to the Storytime universe!

You're one click away from joining a community of parents who believe
bedtime stories should be more than random tales—they should be adventures
that remember, characters that return, and worlds that grow with your child.

[CONFIRM SUBSCRIPTION BUTTON]
         👆 Click to confirm your spot

IMMEDIATE VALUE (delivered before they even confirm!)
While you're here, here's a tiny taste of what Storytime creates:

───────────────────────────────────
"Maya pushed open the garden gate and gasped. The flowers glowed
softly in the twilight, and a gentle 'whoo' came from the old oak tree.
A beautiful silver owl swooped down, landing on a low branch.

'Hello Maya,' said the owl in a voice like wind chimes. 'I'm Whisper,
guardian of the Whispering Garden. We've been waiting for someone
brave enough to hear the flowers' secrets.'"
───────────────────────────────────

That's Maya meeting Whisper the Owl for the first time. In Storytime,
Whisper will remember Maya—and your child—night after night.

WHAT'S NEXT
Once you confirm, you'll hear from me a few times over the next couple
weeks with:
• The story behind why I'm building this
• A deeper look at how the "story memory" works
• A chance to shape what we build

No spam. Just genuine updates from a parent building something for parents.

CLOSING
Click the button above to confirm, and let the adventure begin.

Warmly,
[Founder name]
Storytime

FOOTER
[Unsubscribe link] | [Physical address if required]

(If you didn't sign up for Storytime, you can safely ignore this email.)
```

**Key Metrics:**
- Target open rate: >60% (confirmation emails typically high)
- Target confirmation rate: >50%
- Target click rate: >50% (the confirm button)

**Kit Setup:**
- Configure in Settings → Emails → Confirmation email
- Enable "Custom confirmation email"
- Paste content above (adjust for Kit's template format)
- Ensure `{{ subscriber.confirmation_url }}` merge tag is in the button

---

### 5.2 Email #2: Vision

**Purpose:** Share the product story, build emotional connection

**Timing:** Day 2 (48 hours after confirmation)

**Subject Line Options:**
- Primary: "Why I'm building Storytime"
- Alt A: "The bedtime problem every parent knows"
- Alt B: "My daughter asked for 'the same story, but different'"

**Preview Text:** "It started with a simple request at bedtime..."

**Content Structure:**

```
HEADER
[Storytime text header]

GREETING
Hi {{first_name | default: "there"}},

THE STORY
Last year, my daughter asked me something that stopped me in my tracks.

"Dad, can we have the same story, but different?"

She wanted to see her favorite character again—but in a NEW adventure.
She wanted continuity. She wanted a universe that remembered.

I looked for an app that could do this. Generate personalized stories?
Sure, plenty of those. But stories that REMEMBER? Characters that RETURN?
A universe that GROWS?

Nothing.

THE PROBLEM
Every AI story app I found had the same issue: amnesia. Each story started
fresh. No memory. No callbacks. No "remember when we saved the forest
sprites?" No inside jokes. No beloved companions returning.

It felt... hollow.

THE VISION
Storytime is different. We're building:

✨ Persistent characters who remember your child
🌙 Story arcs that span weeks and months
🦉 House characters (like Whisper the Owl) who become true companions
📚 A universe that grows richer with every bedtime

Your child won't just hear stories. They'll LIVE in a story universe
that's uniquely theirs.

CLOSING
That's what I'm building. And I'd love for your family to be part of it.

Next time, I'll show you exactly how the "story memory" works. It's
pretty magical.

Talk soon,
[Founder name]

P.S. - Still curious about your child's current favorite story! Hit reply
if you have a moment.

FOOTER
[Unsubscribe link]
```

**Key Metrics:**
- Target open rate: >40%
- Target reply rate: >3%

---

### 5.3 Email #3: Sneak Peek

**Purpose:** Preview features, generate excitement

**Timing:** Day 5

**Subject Line Options:**
- Primary: "How Storytime remembers (sneak peek inside)"
- Alt A: "See how Maya's universe grew over 7 nights"
- Alt B: "The magic behind the memory ✨"

**Preview Text:** "Here's how story continuity actually works..."

**Content Structure:**

```
HEADER
[Storytime text header]

GREETING
Hi {{first_name | default: "there"}},

THE HOOK
Remember Maya and Whisper the Owl from my first email? Let me show you
how their story EVOLVED over a week of bedtimes.

THE DEMONSTRATION
[BOX: Story 1]
Night 1: Maya meets Whisper in the Whispering Garden. Whisper teaches
her to understand the language of flowers.

[BOX: Story 3]
Night 3: The garden sprites need help! Maya uses her new flower-language
skills (callback!) to solve the mystery. Whisper is proud.

[BOX: Story 7]
Night 7: A new child, Luna, discovers the garden. Maya—now confident—
becomes the teacher, showing Luna what Whisper taught her.

See what happened? Maya GREW. She went from student to teacher. The
story remembered her journey.

THE FEATURES
Here's what powers this:

🧠 **Story Memory** - Each story builds on the last
👤 **Character Persistence** - Whisper remembers everything
🎭 **Character Growth** - Your child's character evolves
🌍 **Universe Building** - New locations unlock over time

And yes, it all happens automatically. You just say "another adventure"
and the magic continues.

EXCITEMENT BUILDER
We're putting the finishing touches on the first version now. Early
waitlist members (that's you!) will be first to try it.

CLOSING
One more email coming in a few days. I have a question for you that
will actually shape what we build.

Until then,
[Founder name]

FOOTER
[Unsubscribe link]
```

**Key Metrics:**
- Target open rate: >40%
- Target click rate: >10% (if any links included)

---

### 5.4 Email #4: Engagement

**Purpose:** Request feedback, deepen relationship, identify engaged subscribers

**Timing:** Day 10

**Subject Line Options:**
- Primary: "Quick question (I'd love your input)"
- Alt A: "Help me build the right thing"
- Alt B: "What would make Storytime perfect for YOUR family?"

**Preview Text:** "Your answer will directly shape what we build..."

**Content Structure:**

```
HEADER
[Storytime text header]

GREETING
Hi {{first_name | default: "there"}},

THE ASK
I have a question for you—and your answer will directly influence what
we build first.

THE QUESTION
**What's the #1 thing that would make bedtime stories better for your family?**

Just hit reply and tell me. Could be:
- "My kid gets bored of the same themes"
- "I want stories that teach kindness without being preachy"
- "We need shorter stories for busy nights"
- "I wish we could save favorite stories"
- Something completely different!

No wrong answers. I read every reply personally.

WHY THIS MATTERS
We're a small team building something new. Unlike big companies that
build what they THINK parents want, we can actually build what you
TELL US you want.

Your reply = real influence.

STATUS UPDATE
Quick update on where we are:
✅ Story generation engine working
✅ Character persistence working
🔄 Building the parent dashboard
⏳ Launch target: [timeframe]

You'll be among the first to know when it's ready.

CLOSING
Thanks for being on this journey with us. Seriously—it means a lot.

Now, hit reply and tell me: what would make bedtime stories better?

[Founder name]

P.S. - Everyone who replies gets added to our "VIP early access" list.
You'll get to try Storytime before the general waitlist.

FOOTER
[Unsubscribe link]
```

**Key Metrics:**
- Target open rate: >35%
- Target reply rate: >5%
- Target VIP conversion: Track who replies for priority access

---

## 6. User Experience & Design

### 6.1 Email Design Principles

**Visual Style:**
- Clean, minimal design (not cluttered)
- Primarily text-based (better deliverability)
- Accent colors sparingly: gold (#fbbf24) for highlights
- White/light background for readability
- Dark text (#1a1a1a) for body copy

**Typography:**
- System font stack for maximum compatibility
- Body: 16px minimum
- Headers: 20-24px
- Line height: 1.6 for readability

**Mobile First:**
- Single column layout
- Full-width on mobile
- Max-width 600px on desktop
- Touch targets minimum 44px

### 6.2 Emotional Journey

```
Confirmation/Welcome (automatic)
├── Emotion: Curious, intrigued by story excerpt
├── Trust level: Low → Medium
└── Action: Click to confirm subscription

Email #2: Vision (Day 2)
├── Emotion: Connected, understanding, aligned
├── Trust level: Medium
└── Action: Feel invested in the mission

Email #3: Sneak Peek (Day 5)
├── Emotion: Excited, impressed, wanting more
├── Trust level: Medium → High
└── Action: Anticipate launch

Email #4: Engagement (Day 10)
├── Emotion: Valued, heard, influential
├── Trust level: High
└── Action: Reply with feedback
```

### 6.3 Reply Experience

When subscribers reply:
- Replies go to monitored inbox
- Response within 24-48 hours (manual)
- Personalized reply (not template)
- Thank them, acknowledge their input
- Note engaged subscribers for VIP treatment

---

## 7. Edge Cases & Error Handling

### 7.1 Edge Cases

**EDGE-001: Subscriber Never Confirms**
- **Scenario:** User signs up but doesn't click confirmation
- **Handling:** No welcome sequence sent (correct behavior)
- **Mitigation:** Kit can send confirmation reminder

**EDGE-002: Subscriber Unsubscribes Mid-Sequence**
- **Scenario:** User unsubscribes after Email #2
- **Handling:** Stop all further emails immediately
- **Phase A:** Remove from tracking spreadsheet
- **Phase B:** Automation handles automatically

**EDGE-003: Subscriber Re-subscribes**
- **Scenario:** User unsubscribes then re-subscribes later
- **Handling Phase A:** Start fresh sequence (treat as new)
- **Handling Phase B:** Configure automation to check history

**EDGE-004: Email Bounces**
- **Scenario:** Email address becomes invalid
- **Handling:** Kit auto-handles, removes from list
- **Action:** No manual intervention needed

**EDGE-005: Missed Manual Send (Phase A)**
- **Scenario:** Forgot to send email on scheduled day
- **Handling:** Send as soon as noticed
- **Impact:** Sequence timing off, but acceptable
- **Prevention:** Daily reminder/checklist

**EDGE-006: High Volume Day (Phase A)**
- **Scenario:** 15+ confirmations in one day
- **Handling:** Batch process, may take longer
- **Trigger for Phase B:** If this happens consistently

### 7.2 Error Messages

Not applicable—emails are outbound only. No user-facing error states.

---

## 8. Testing Requirements

### 8.1 Pre-Launch Testing

**TEST-001: Email Rendering**
- [ ] Test all 4 emails in Kit preview
- [ ] Send test emails to personal accounts
- [ ] Check rendering in:
  - Gmail (web)
  - Gmail (mobile app)
  - Apple Mail (iOS)
  - Outlook (web)
- [ ] Verify links work correctly
- [ ] Verify unsubscribe works

**TEST-002: Merge Tags**
- [ ] Test with subscriber who has first_name set
- [ ] Test with subscriber who has no first_name (fallback)
- [ ] Verify personalization displays correctly

**TEST-003: Deliverability**
- [ ] Check spam score (Kit or external tool)
- [ ] Verify emails don't land in spam folder
- [ ] Test from different email providers

**TEST-004: Mobile Experience**
- [ ] Read each email on mobile device
- [ ] Tap all links/buttons
- [ ] Verify text is readable without zooming

### 8.2 Ongoing Monitoring (Phase A)

**Weekly checks:**
- [ ] Open rates for each email
- [ ] Click rates for each email
- [ ] Unsubscribe rate
- [ ] Bounce rate
- [ ] Reply count
- [ ] Sequence completion rate

---

## 9. Success Metrics & Validation

### 9.1 Key Performance Indicators

| Metric | Target | Good | Needs Work | Measurement |
|--------|--------|------|------------|-------------|
| Confirmation Email Open Rate | >60% | 50-60% | <50% | Kit |
| Confirmation Rate (clicks) | >50% | 40-50% | <40% | Kit |
| Follow-up Avg Open Rate | >40% | 30-40% | <30% | Calculated |
| Click-Through Rate | >10% | 5-10% | <5% | Kit |
| Unsubscribe Rate | <2% | 2-5% | >5% | Kit |
| Reply Rate | >5% | 2-5% | <2% | Manual count |
| Sequence Completion | >70% | 50-70% | <50% | Tracking sheet |

### 9.2 Qualitative Metrics

- **Reply sentiment:** Are replies positive/engaged?
- **Feedback quality:** Do replies contain actionable insights?
- **VIP interest:** How many request early access?

### 9.3 Success Threshold for Phase B

Trigger automation implementation when:
1. ✅ 100 total signups achieved, AND
2. ✅ Sequence metrics meet "Good" thresholds, AND
3. ✅ Manual process taking >30 min/day

---

## 10. Implementation Plan

### 10.1 Phase A Tasks

**Confirmation Email Setup (1 hour)**
- [ ] Configure custom confirmation email in Kit settings
- [ ] Add branded content with story excerpt
- [ ] Test confirmation flow end-to-end
- [ ] Verify confirmation link works

**Follow-up Emails Preparation (2 hours)**
- [ ] Create Email #2 (Vision) template in Kit
- [ ] Create Email #3 (Sneak Peek) template in Kit
- [ ] Create Email #4 (Engagement) template in Kit
- [ ] Internal review of all copy

**Testing (1-2 hours)**
- [ ] Test confirmation email from fresh signup
- [ ] Send test follow-ups to personal accounts
- [ ] Test on multiple email clients (Gmail, Apple Mail, Outlook)
- [ ] Verify all links work
- [ ] Check spam score

**Launch (30 minutes)**
- [ ] Confirmation email goes live automatically
- [ ] Set up tracking spreadsheet for manual follow-ups
- [ ] Set daily reminder to check for new confirmed subscribers
- [ ] Set daily reminder to check dashboard

**Ongoing (5-10 minutes/day)**
- [ ] Check for new confirmations
- [ ] Send appropriate emails
- [ ] Update tracking spreadsheet
- [ ] Monitor metrics weekly

### 10.2 Deliverables

1. **Email templates:** 4 emails created in Kit
2. **Tracking spreadsheet:** Template with columns defined
3. **Process documentation:** Step-by-step manual process
4. **Weekly report template:** Metrics tracking format

---

## 11. Automation Upgrade Path

### 11.1 Trigger for Automation

Implement Phase B when ANY of these occur:
- 100 signups achieved (demand validated)
- Manual process taking >30 min/day
- Missing sends due to human error
- Request from team to automate

### 11.2 Platform Decision (SD-001)

When ready for automation, evaluate:

**Option A: Kit Creator ($29/mo)**
- Pros: No code changes, same platform as F002
- Cons: $29/mo ongoing cost
- Implementation: ~1 hour (configure automations in dashboard)

**Option B: Kit Free ($0/mo)**
- Pros: Free, includes 1 automation
- Cons: Requires serverless proxy (code changes), Kit branding
- Implementation: ~4-6 hours (code + setup)

**Option C: Kit Creator ($39/mo)**
- Pros: Unlimited automations, no branding
- Cons: Higher cost than Kit, requires code changes
- Implementation: ~4-6 hours (code + setup)

**Recommendation:** Re-evaluate when threshold reached. If validation successful and expecting growth, Kit Creator is simplest. If budget-constrained, Kit Free is viable.

### 11.3 Automation Configuration

**Kit automation setup:**
1. Confirmation/Welcome email: Already automatic (via Settings → Emails)
2. Create automation: "Follow-up Sequence"
3. Trigger: "Subscriber confirms subscription"
4. Actions:
   - Delay 2 days: Send Email #2 (Vision)
   - Delay 5 days: Send Email #3 (Sneak Peek)
   - Delay 10 days: Send Email #4 (Engagement)

**Kit automation setup:**
1. Confirmation email: Configure in Kit settings
2. Create sequence: "Follow-up Sequence"
3. Add 3 emails with delays (2, 5, 10 days)
4. Trigger: Form submission (after confirmation)
5. Update F002 code to use Kit API

---

## 12. Open Questions & Decisions

### 12.1 Decisions Made

| Question | Decision | Rationale |
|----------|----------|-----------|
| How many emails? | 4 total | Enough to build relationship, not overwhelming |
| Combine confirmation + welcome? | Yes | Reduces emails, delivers value immediately, higher confirm rate |
| Manual or automated? | Manual first (follow-ups only) | Validate demand before $29/mo cost |
| Personalization? | None (no first name on signup) | Keep signup form simple, one field only |
| Include images? | Minimal | Better deliverability, faster loading |
| Ask for feedback? | Yes, Email #4 | Valuable insights, identifies engaged users |

### 12.2 Open Questions

**Q-001: Exact subject lines?**
- **Status:** Options provided, test in Phase B
- **Decision:** Use "Primary" options for Phase A

**Q-002: Physical address requirement?**
- **Status:** Check Kit default
- **Action:** Verify CAN-SPAM compliance

---

## Appendix: Email Checklist

Before sending each email, verify:

- [ ] Subject line is compelling
- [ ] Preview text is set
- [ ] Personalization tags work
- [ ] All links are correct and tracked
- [ ] Unsubscribe link present
- [ ] Mobile rendering tested
- [ ] Spam score acceptable
- [ ] Sent from correct sender name/email

---

**PRD Status:** ✅ Ready for Implementation (Phase A)

**Next Steps:**
1. Review and approve email copy
2. Create templates in Kit
3. Set up tracking spreadsheet
4. Begin sending to new subscribers

---

**Document Metadata:**
- Word Count: ~3,500
- Sections: 12
- Email templates: 4 (fully specified)
- Implementation time: 3-5 hours (Phase A)
