# Product Requirements Document (PRD) Guide

**Last Updated:** 2026-01-24

---

## What is a PRD?

A **Product Requirements Document (PRD)** is a comprehensive specification that describes exactly what needs to be built, why it matters, and how success will be measured. Think of it as a blueprint for feature development.

**In this project, PRDs serve a specific purpose:** Enable Claude Code to build features in a single iteration with excellent quality, without requiring clarifications or back-and-forth.

---

## Why We Use PRDs

### The Problem
Building features often fails because:
- Requirements are vague or incomplete
- Edge cases aren't considered upfront
- Technical decisions are made during coding (leading to rework)
- Success criteria are unclear
- Features are too large to complete in one go

### The Solution
A well-crafted PRD:
- ✅ **Removes ambiguity** - Every detail is specified
- ✅ **Catches edge cases early** - Before any code is written
- ✅ **Validates technical approach** - Ensures feasibility
- ✅ **Defines success clearly** - Measurable outcomes
- ✅ **Right-sizes features** - Breaks large work into buildable chunks
- ✅ **Enables one-shot delivery** - Build it right the first time

---

## How PRDs Work in This Project

### 1. The Backlog
All feature ideas live in `docs/backlog.md`:
- Each feature has a unique ID (F001, F002, etc.)
- Brief description and success metrics
- Priority level (P0-P3) and effort estimate

### 2. PRD Generation
When ready to build a feature:
1. **Request:** "Create PRD for F001"
2. **Claude analyzes:**
   - Reads backlog item
   - Researches codebase and external dependencies
   - Assesses feature scope and complexity
   - Identifies risks and trade-offs
3. **Claude generates:**
   - Complete PRD in `docs/prds/F001-feature-name.md`
   - Market research and tool comparisons (if applicable)
   - Technical architecture and implementation plan
   - All edge cases and error scenarios

### 3. Review & Approval
You review the PRD and:
- Verify requirements match your vision
- Validate technical approach
- Resolve any open questions
- Approve for implementation

### 4. Implementation
With an approved PRD:
- **Request:** "Build F001"
- Claude has everything needed for one-shot delivery
- No clarifying questions needed
- High-quality implementation on first attempt

### 5. Validation
After deployment:
- Measure against success metrics in PRD
- Validate all acceptance criteria met
- Move feature to "Completed" in backlog

### Claude's PRD Creation Process

When you request a PRD, Claude follows this process:

**1. Setup & Planning:**
- Creates todo list for all 13 sections
- Asks about section order preference (if strategic choice exists)
- Explains sequencing rationale

**2. Sequential Section Delivery:**
- Completes one section at a time
- Shows section for review before proceeding
- Gets explicit approval at each gate
- Updates todos in real-time

**3. Strategic Sequencing:**
- Typically: Sections 3-6 first (define WHAT)
- Then: Sections 7-13 (define HOW)
- Then: Section 2 (platform choice with data)
- Finally: Section 1 (executive summary)

**4. Quality Verification:**
- Each section checked against quality standards
- Specific, testable criteria
- Concrete specifications (not vague)
- Code examples where helpful

**5. User Involvement:**
- Strategic decisions presented for your input
- Progress visibility through todos
- Course correction opportunities at each section

---

## Best Practices for PRD Creation Process

### Incremental Section Delivery

**DON'T:** Create entire PRD before showing user (risks misalignment and wasted effort)

**DO:** Complete and review section-by-section
- Complete one section at a time
- Show section to user for review
- Get explicit approval before proceeding
- Allows course corrections early

**Benefits:**
- User sees progress in real-time
- Early feedback prevents rework
- Builds trust through transparency
- Reduces "why is this taking so long?" perception

---

### Process Transparency with TodoWrite

**Always:**
- Create todos for EACH PRD section at the start (not just "write PRD")
- Update status in real-time (pending → in_progress → completed)
- Show parallel vs sequential work clearly
- Mark todos completed immediately after finishing (don't batch)

**Example todo structure:**
```
- Section 3: User Stories (in_progress)
- Section 4: Functional Requirements (pending)
- Section 5: Technical Specifications (pending)
- Sections 1-2: Executive Summary & Analysis (pending - strategic, do last)
- Sections 7-13: Remaining sections (pending)
```

**Why this matters:**
- Users want to see "threads you're pulling"
- Breakdown of work reduces perceived wait time
- Visibility into process builds trust
- Helps resume work if interrupted

---

### Involve User in Strategic Decisions

**Don't assume - always ask:**
- Section order preference (which first?)
- Platform decision timing (now or after requirements?)
- Level of detail needed (comprehensive vs minimal?)
- Implementation approach (client-side vs server-side?)

**Template:**
"I have two approaches: [Option A with rationale] vs [Option B with rationale]. Which would be most efficient for your needs?"

**Why:**
- Users have context we don't (their priorities, timeline)
- Participation in efficiency decisions builds ownership
- Different projects may need different approaches

---

### Strategic Section Sequencing

**Optimal PRD creation order:**

1. **Sections 3-6 first** (User Stories, Requirements, Technical Specs, UX)
   - These define WHAT we need
   - Platform-agnostic at this stage

2. **Sections 7-13 next** (Edge Cases, Security, Testing, Deployment, Metrics, Implementation)
   - These define HOW and operational details
   - Security/testing needs may reveal platform constraints

3. **Section 2 then** (Platform Analysis)
   - Informed by all requirements
   - Data-driven choice based on documented needs

4. **Section 1 last** (Executive Summary)
   - Summarizes completed analysis
   - Can't write good summary without the details

**Rationale:**
- Requirements inform platform choice (not vice versa)
- Doing analysis AFTER requirements = data-driven decision
- Doing analysis BEFORE requirements = premature optimization

---

## PRD Structure

Every PRD follows a 13-section template:

### Core Sections
1. **Executive Summary** - Problem, solution, success criteria
2. **User Stories** - Who needs this and why
3. **Functional Requirements** - What the feature must do
4. **Technical Specifications** - How it will be built

### Detail Sections
5. **User Experience & Design** - UI flows, components, responsiveness
6. **Edge Cases & Error Handling** - What can go wrong and how to handle it
7. **Security & Privacy** - Auth, data protection, compliance
8. **Testing Requirements** - Unit, integration, manual test scenarios

### Deployment Sections
9. **Deployment & Configuration** - Environment variables, migrations, setup
10. **Success Metrics & Validation** - KPIs, analytics events, success checklist
11. **Implementation Plan** - Task breakdown, dependencies, risks

### Supporting Sections
12. **Open Questions & Decisions** - Items to resolve before building
13. **References & Resources** - Documentation, examples, related work

---

## PRD Content Quality Standards

These standards ensure PRDs have sufficient detail for one-shot implementation.

### Platform-Agnostic Requirements Documentation

**Best practice:**
- Write functional requirements platform-agnostically
- Use [TOOL] placeholder when decision isn't finalized
- Document what needs to happen, not how with specific tool
- In technical specs, document BOTH/ALL platform options
- Make platform decision AFTER documenting all requirements

**Example:**
```markdown
**REQ-002: Email Submission**
- User can submit email via [TOOL] integration
- Submission triggers double opt-in flow
- Success confirmation appears within 2 seconds

(NOT: "User submits email via Kit API" - that's premature)
```

**Benefits:**
- Requirements remain pure (not biased by tool limitations)
- Platform analysis is data-driven
- Easy to swap platforms later if needed
- Forces clarity about actual needs vs tool features

---

### User Stories Need Comprehensive Acceptance Criteria

**Standard:**
- Each user story needs 5-7 specific, testable acceptance criteria
- Cover happy path AND edge cases
- Include performance expectations
- Include error handling
- Include data persistence

**Template:**
```markdown
**As a** [role]
**I want** [capability]
**So that** [benefit]

**Acceptance Criteria:**
1. [Specific, testable criterion - happy path]
2. [Edge case handling]
3. [Performance expectation with numbers]
4. [Error handling scenario]
5. [Success state verification]
6. [Data persistence verification]
7. [Accessibility requirement]
```

**Quality test:**
- Can a developer implement from acceptance criteria alone?
- Can a tester write test cases from acceptance criteria?
- Are criteria specific enough to be binary pass/fail?

---

### Functional Requirements Need Priority and Dependencies

**Standard format:**
```markdown
**REQ-XXX: [Requirement Name]**
- Description: [What it does]
- Priority: Must-have (P0) | Should-have | Nice-to-have
- Acceptance: [How we know it's done]
- Dependencies: [What this requires]
```

**Priority definitions:**
- **Must-have (P0)**: Core functionality, launch blocker
- **Should-have**: Important but not launch-critical
- **Nice-to-have**: Enhances experience but optional

---

### Technical Specs Need Multiple Implementation Options

**Best practice:**
- Document architecture pattern (client-side vs server-side)
- Show request/response formats for each platform option
- Include CORS, rate limiting, authentication details
- Provide code examples for key implementations (~50-200 lines)
- Document security implications of each approach
- Compare approaches with pros/cons

**Example structure:**
```markdown
### 5.3 Platform-Specific API Integration

#### 5.3.1 Platform A API
- Endpoint, auth, request format, response format
- CORS support, rate limits
- Pros: [list], Cons: [list]
- Code example: [~50 lines]

#### 5.3.2 Platform B API
- Endpoint, auth, request format, response format
- CORS support, rate limits
- Pros: [list], Cons: [list]
- Code example: [~50 lines]
```

---

### UX Specifications Need Emotional Journey Mapping

**Section 6 must include:**

1. **Complete user journey with emotional states at each step**
   ```markdown
   STAGE: EMAIL SUBMISSION
   User Action: Clicks submit button
   Emotional State: 😬 Anticipation, slight anxiety
   Duration: <1 second (critical moment)
   Design Goal: Immediate acknowledgment
   Critical UX:
   - Button responds within 100ms
   - Loading indicator appears immediately
   - Clear visual feedback (button state change)
   - No uncertainty about whether click registered
   ```

2. **Precise timing specifications** (not vague like "fast"):
   - Button press feedback: 100ms
   - Loading state appearance: <100ms after click
   - API response target: <1s (timeout at 5s)
   - Success message fade-in: 300ms
   - Success message auto-hide: 5s
   - Animation easing: ease-out for entrances, ease-in for exits

3. **All UI states specified:**
   - Default, hover, active, loading, success, error, disabled
   - For EACH interactive element

4. **Animation timing table:**
   | Element | Duration | Easing | Purpose |
   |---------|----------|--------|---------|
   | Button press | 100ms | ease-out | Immediate tactile feedback |
   | Success fade-in | 300ms | ease-out | Celebratory appearance |

---

### Copy and Messaging Deserve Dedicated Specification

**Section 6 must include:**
- Tone definition (friendly, warm, professional, casual)
- Exact copy for: buttons, placeholders, success messages, error messages
- Show alternatives with different tones
- Include rationale for tone choices

**Example:**
```markdown
#### Success Messages
✅ "Thanks! Check your email..." (Warm, exclamation shows enthusiasm)
❌ "Thank you. Please check your email." (Too formal, period = stern)
❌ "Success! Email sent." (Technical, not human)
```

---

### Error States Are Equal Citizens to Success States

**Best practice:**
- Document ALL error scenarios in Section 7 (Edge Cases)
- Specify exact error messages (copy matters!)
- Include error recovery paths (how user fixes it)
- Test error messaging tone (blame-free, helpful)
- Map error types to user messages

**Error message guidelines:**
- Blame the system, not the user
- Provide clear next step
- Be specific but not technical
- Maintain warm, friendly tone even in errors

**Example:**
```markdown
❌ "Invalid email address" (blames user, unhelpful)
✅ "Hmm, that email doesn't look quite right. Can you double-check it?" (warm, helpful)
```

---

### Accessibility Needs Concrete Implementation Specs

**Section 6 must include:**
- Exact ARIA attributes needed (not just "make it accessible")
- Keyboard navigation (tab order, enter/space behavior)
- Screen reader announcements for each state
- Focus indicator specifications (color, size, offset)
- Color contrast ratios with numbers (not just "high contrast")
- WCAG level target (AA vs AAA)

**Example:**
```markdown
**Email Input Field:**
- aria-label="Email address"
- aria-required="true"
- aria-invalid="false" (changes to "true" on validation error)
- aria-describedby="emailError" (when error present)

**Screen reader announces:**
- On focus: "Email address, required, edit text"
- On error: "Invalid email. Please enter a valid email address"
- On success: "Success! Check your email to confirm your subscription"
```

---

### Mobile-Specific Considerations Need Separate Section

**Section 6 must include:**
- Minimum touch target sizes (44px iOS HIG minimum)
- Input types for mobile keyboards (`type="email"`)
- Viewport zoom behavior (16px font minimum to prevent zoom)
- Mobile vs desktop layouts separately
- iOS vs Android differences where applicable

---

### Security Section Needs Risk Assessment

**Section 8 must include:**
- Risk level for each approach (LOW/MED/HIGH)
- Mitigation strategies for each risk
- CSP headers needed (exact directives)
- Rate limiting (client-side and server-side)
- PII handling (where email goes, what's logged)
- GDPR compliance approach

---

## Scope Management: Breaking Down Large Features

Claude automatically assesses if a feature is too large for one iteration:

### Small Feature (≤1 day)
**Example:** F002 - Email Collection Integration
- Single integration point (Kit API)
- Clear scope and requirements
- **Action:** Create single PRD, build in one shot

### Medium Feature (1-3 days)
**Example:** F001 - Analytics Integration
- Moderate complexity (Plausible setup + event tracking)
- A few integration points
- **Action:** Create single comprehensive PRD

### Large Feature (>3 days)
**Example:** F011 - Story Generation Engine
- High complexity (AI, customization, persistence)
- Multiple components and integrations
- **Action:** Break into sub-features:
  - F011a: Basic story generation (MVP)
  - F011b: Character customization
  - F011c: Story quality improvements
  - F011d: Multi-turn story conversations

**Principle:** Each sub-feature must be independently valuable and deployable.

---

## Example Workflow

### Step 1: Pick from Backlog
You identify F001 (Analytics Integration) as the next priority.

### Step 2: Request PRD
```
You: "Create PRD for F001"
```

### Step 3: Claude's Process
```
Claude:
1. ✓ Read F001 from backlog.md
2. ✓ Research Plausible Analytics documentation
3. ✓ Compare alternatives (Google Analytics, Fathom, Plausible)
4. ✓ Explore codebase for integration points
5. ✓ Assess CSP headers, HTML changes needed
6. ✓ Define success metrics and test scenarios
7. ✓ Generate complete PRD
```

### Step 4: Review PRD
You read `docs/prds/F001-analytics-integration.md` and check:
- ✓ Plausible is the right choice (privacy-focused, lightweight)
- ✓ Technical approach is sound
- ✓ Success metrics align with goals (track to 100 signups)
- ✓ No open questions remaining

### Step 5: Approve & Build
```
You: "Approved. Build F001"

Claude:
1. ✓ Adds Plausible script to index.html
2. ✓ Updates CSP headers in netlify.toml
3. ✓ Configures event tracking for email signups
4. ✓ Tests locally
5. ✓ Commits and pushes
6. ✓ Creates PR
```

### Step 6: Deploy & Validate
```
You: Merge PR → Tag release (v1.1.0)
Result: Production deploy with analytics working
Validation: Check Plausible dashboard shows events
```

---

## Quality Standards

### Pre-Implementation Quality Checklist

Before marking a section as "complete", verify:

**User Stories (Section 3):**
- [ ] 5-7 specific acceptance criteria per story
- [ ] Acceptance criteria are testable (binary pass/fail)
- [ ] Edge cases covered in acceptance criteria
- [ ] Performance expectations specified

**Functional Requirements (Section 4):**
- [ ] Each requirement has priority (P0/Should/Nice-to-have)
- [ ] Dependencies documented
- [ ] Acceptance criteria specific and measurable
- [ ] Platform-agnostic (uses [TOOL] if decision pending)

**Technical Specifications (Section 5):**
- [ ] Code examples provided (~50-200 lines total)
- [ ] Multiple implementation options compared
- [ ] CORS, rate limiting, auth details specified
- [ ] Security implications documented

**UX & Design (Section 6):**
- [ ] Complete user journey with emotional states mapped
- [ ] Timing specified in milliseconds (not "fast")
- [ ] All UI states documented (default, hover, active, loading, success, error, disabled)
- [ ] Exact copy provided (not placeholders)
- [ ] Error states given equal detail to success states
- [ ] Animation durations and easing functions specified
- [ ] Accessibility specs concrete (ARIA attributes, keyboard nav, screen reader announcements)
- [ ] Mobile considerations included (touch targets, input types, viewport)

**Edge Cases & Errors (Section 7):**
- [ ] Every error scenario has exact message copy
- [ ] Error messages are blame-free and helpful
- [ ] Recovery paths documented

**Security (Section 8):**
- [ ] Risk assessment for each approach (LOW/MED/HIGH)
- [ ] Mitigation strategies specified
- [ ] CSP headers documented

### Excellent PRD (Ready to Build) ✅
- All requirements are crystal clear
- Every edge case has a defined solution
- Technical approach is validated with code examples
- Complete test scenarios provided
- Success criteria are measurable
- Timing specifications in milliseconds
- Error messages have exact copy
- Accessibility implementation is concrete
- Claude can build without any questions

### Poor PRD (Not Ready) ❌
- Vague requirements ("make it good", "improve UX")
- Missing edge cases or error handling
- Unvalidated technical assumptions
- No code examples
- No test scenarios
- Vague timing ("fast", "responsive")
- Generic error handling ("show error message")
- Vague accessibility ("make it accessible")
- Would require clarifications during build

**Goal:** Every PRD must be "Excellent" before development starts.

---

## Tips for Working with PRDs

### DO:
- ✅ Review PRDs thoroughly before approving
- ✅ Ask questions if anything is unclear
- ✅ Validate that success metrics align with goals
- ✅ Ensure technical approach fits the architecture
- ✅ Resolve all open questions before building

---

### Template Phrases for PRD Review & Feedback

**Starting a section:**
"Now working on Section X: [Name]. I'll document [what this section covers] and show you for review when complete."

**Completing a section:**
"**Section X complete!** I've documented: [bullet list of what's included]. Ready for your review!"

**Requesting feedback:**
"Does this Section X capture all the [user stories/requirements/etc.] you need? Should I add or modify anything before moving to Section Y?"

**Strategic decisions:**
"I have two approaches: [Option A with rationale] vs [Option B with rationale]. Which would be most efficient for your needs?"

**Showing progress:**
"I've completed sections 3-6. Remaining: sections 7-13 (technical details), then section 2 (platform choice), then section 1 (summary). This sequencing allows data-driven platform decision."

---

### DON'T:
- ❌ Skip the PRD for "quick" features (they're rarely quick)
- ❌ Rush approval without reading
- ❌ Start building before PRD is complete
- ❌ Ignore raised risks or concerns
- ❌ Skip validation after deployment

---

## PRD Storage & Organization

```
docs/
├── backlog.md              # All feature ideas and priorities
├── PRD-GUIDE.md           # This file
└── prds/                   # Generated PRDs (one per feature)
    ├── F001-analytics-integration.md
    ├── F002-email-collection.md
    ├── F003-ab-testing.md
    └── ...
```

**Naming Convention:** `FXXX-feature-name.md`
- Use feature ID from backlog
- Use kebab-case for feature name
- Keep filenames concise but descriptive

---

## When to Update a PRD

PRDs can be updated in these situations:

### During Review (Before Building)
- Clarify ambiguous requirements
- Add missing edge cases
- Refine technical approach
- Update based on feedback

### During Implementation (Rare)
- Document unexpected discoveries
- Record decisions made during build
- Update with actual vs. planned implementation

### After Deployment
- Add lessons learned
- Update with actual metrics achieved
- Mark as "Completed" with deployment date

**Important:** Major changes during implementation suggest the PRD wasn't thorough enough. Learn from this for future PRDs.

---

## Frequently Asked Questions

### Q: Do I need a PRD for every feature?
**A:** Yes, for anything non-trivial. Even "small" features benefit from thinking through requirements, edge cases, and success metrics upfront.

### Q: How long does it take to create a PRD?
**A:** Claude generates PRDs in minutes. Your review typically takes 10-30 minutes depending on complexity.

### Q: What if I disagree with the technical approach?
**A:** That's what the review phase is for! Discuss alternatives before approving. The PRD can be revised.

### Q: Can I build without a PRD?
**A:** You can, but you shouldn't. PRDs save far more time than they take by preventing rework, missed edge cases, and scope creep.

### Q: What if requirements change after the PRD is approved?
**A:** Small changes: Update the PRD and note the change. Large changes: Consider if this should be a new feature instead.

### Q: How do I know if a feature should be broken down?
**A:** Claude assesses this automatically. Rule of thumb: If it takes >3 days to build or has >5 major components, consider breaking it down.

---

## Success Stories

### Before PRDs
- Feature request → Start coding → Realize edge cases → Rewrite code
- Vague requirements → Multiple iterations → Frustration
- Large features → Get stuck midway → Never finish

### After PRDs
- Feature request → Create PRD → Review → Build once → Deploy → Done
- Clear requirements → One iteration → High quality
- Right-sized features → Predictable delivery → Steady progress

---

## Related Documentation

- **Backlog:** `docs/backlog.md` - All feature ideas and priorities
- **PRD Framework:** `.claude/prd-framework.md` - Detailed framework for Claude
- **Project Guide:** `CLAUDE.md` - Overall project context for Claude
- **CI/CD Guide:** `.claude/cicd-implementation-guide.md` - Deployment process

---

## Summary

**PRDs are your blueprint for successful feature development.**

1. **Start with backlog** - Identify feature to build
2. **Generate PRD** - Claude creates comprehensive spec
3. **Review thoroughly** - Ensure it's build-ready
4. **Build once** - High quality, no rework
5. **Validate** - Measure against success criteria

**Time invested in PRDs pays off 10x during implementation.**

Questions? Check the PRD Framework (`.claude/prd-framework.md`) or ask Claude!
