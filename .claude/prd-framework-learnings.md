# PRD Framework Learnings - Session 2026-01-25

## Context
This document captures learnings from creating the F002 PRD (Email Collection Integration). These insights should be integrated into the main PRD-GUIDE.md framework.

---

## Key Learnings

### 1. Incremental Section Delivery Over Monolithic Creation

**What we learned:**
- Users want to see progress and provide feedback section-by-section
- Creating entire PRD before showing user is inefficient (potential rework)
- Sequential delivery with review gates prevents wasted effort

**Best practice:**
- Complete one section at a time
- Show section to user for review
- Get explicit approval before proceeding
- Allows course corrections early

**Implementation:**
- Use TodoWrite to track section-by-section progress
- Mark sections as in_progress → completed
- Request review after each major section
- Don't proceed without user confirmation

---

### 2. Granular Task Tracking with TodoWrite

**What we learned:**
- Breaking PRD creation into 13+ discrete tasks makes progress visible
- Users can see exactly what's being worked on and what's remaining
- Task breakdown reduces perception of "why is this taking so long"

**Best practice:**
- Create todos for EACH PRD section (not just "write PRD")
- Update status in real-time (in_progress, completed)
- Show parallel vs sequential work clearly
- Give user visibility into the process

**Example todo structure:**
```
- Section 3: User Stories (in_progress)
- Section 4: Functional Requirements (pending)
- Section 5: Technical Specifications (pending)
- Sections 1-2: Executive Summary & Analysis (pending - strategic, do last)
- Sections 7-13: Remaining sections (pending)
```

---

### 3. Platform-Agnostic Requirements Documentation

**What we learned:**
- Don't commit to specific tools/platforms prematurely
- Use [TOOL] placeholder when decision isn't finalized
- Document requirements for ANY solution first
- Let requirements drive platform choice (not vice versa)

**Best practice:**
- Write functional requirements platform-agnostically
- Document what needs to happen, not how with specific tool
- In technical specs, document BOTH/ALL platform options
- Make platform decision AFTER documenting all requirements

**Benefits:**
- Requirements remain pure (not biased by tool limitations)
- Platform analysis is data-driven (what meets our needs?)
- Easy to swap platforms later if needed
- Forces clarity about actual needs vs tool features

---

### 4. Emotional Journey Mapping in UX Sections

**What we learned:**
- UX section needs more than functional flows
- Users experience emotional states at each interaction point
- Timing and responsiveness directly impact emotional experience
- Small delays (>100ms) create anxiety

**Best practice for Section 6 (UX & Design):**
- Map complete user journey with emotional states at each step
- Document timing expectations (button feedback <100ms, API <2s, etc.)
- Address anxiety-inducing moments (waiting, errors, uncertainty)
- Include microinteractions that provide delight
- Specify copy/messaging tone (warm vs formal, blame-free errors)
- Detail all UI states (default, hover, active, loading, success, error, disabled)

**Example emotional journey format:**
```
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

---

### 5. Precise Interaction Timing Specifications

**What we learned:**
- Vague timing ("fast", "quick") isn't implementable
- Specific millisecond targets guide implementation
- Different interactions have different timing expectations
- Timing impacts perceived quality

**Best practice:**
- Specify exact timing for all interactions
- Use industry standards (100ms tactile feedback, <3s load time)
- Document animation durations and easing functions
- Include timeout values (5s for API calls, etc.)

**Timing examples:**
- Button press feedback: 100ms
- Loading state appearance: <100ms after click
- API response target: <1s (timeout at 5s)
- Success message fade-in: 300ms
- Success message auto-hide: 5s
- Animation easing: ease-out for entrances, ease-in for exits

---

### 6. Strategic Section Sequencing

**What we learned:**
- Not all sections have equal dependencies
- Strategic sections (Executive Summary, Platform Choice) benefit from completing technical sections first
- Doing analysis AFTER requirements = data-driven decision
- Doing analysis BEFORE requirements = premature optimization

**Optimal PRD creation sequence:**
1. **Sections 3-6 first** (User Stories, Requirements, Technical Specs, UX) - These define WHAT we need
2. **Sections 7-13 next** (Edge Cases, Security, Testing, Deployment, Metrics, Implementation) - These define HOW and operational details
3. **Section 2 then** (Platform Analysis) - Informed by all requirements, make data-driven choice
4. **Section 1 last** (Executive Summary) - Summarizes completed analysis

**Rationale:**
- Requirements inform platform choice (not vice versa)
- Security/testing needs may reveal platform constraints
- Implementation plan needs platform decision
- Executive summary synthesizes everything

---

### 7. User Stories Need Comprehensive Acceptance Criteria

**What we learned:**
- User stories without acceptance criteria are too vague
- Each user story needs 5-7 specific, testable acceptance criteria
- Acceptance criteria should cover happy path AND edge cases
- Good acceptance criteria = clear definition of done

**Best practice:**
```
**As a** [role]
**I want** [capability]
**So that** [benefit]

**Acceptance Criteria:**
1. [Specific, testable criterion]
2. [Specific, testable criterion]
3. [Edge case handling]
4. [Performance expectation]
5. [Error handling]
6. [Success state]
7. [Data persistence]
```

**Quality test:**
- Can a developer implement from acceptance criteria alone?
- Can a tester write test cases from acceptance criteria?
- Are criteria specific enough to be binary pass/fail?

---

### 8. Functional Requirements Need Priority and Dependencies

**What we learned:**
- Not all requirements are equal priority
- Requirements have dependencies on each other
- Each requirement needs priority (P0/Must-have, Should-have, Nice-to-have)
- Dependencies help with implementation sequencing

**Best practice format:**
```
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

### 9. Technical Specs Need Multiple Implementation Options

**What we learned:**
- Section 5 should document multiple technical approaches
- Compare approaches with pros/cons
- Document platform-specific API details for each option
- Include configuration management strategies

**Best practice:**
- Document architecture pattern (client-side vs server-side)
- Show request/response formats for each platform option
- Include CORS, rate limiting, authentication details
- Provide code examples for key implementations
- Document security implications of each approach

**Example structure:**
```
### 5.3 Platform-Specific API Integration

#### 5.3.1 Platform A API
- Endpoint, auth, request format, response format
- CORS support, rate limits
- Pros/cons

#### 5.3.2 Platform B API
- Endpoint, auth, request format, response format
- CORS support, rate limits
- Pros/cons
```

---

### 10. Error States Are Equal Citizens to Success States

**What we learned:**
- PRDs often under-specify error handling
- Error states need same detail as success states
- Error messaging impacts user perception significantly
- Errors are opportunities to build trust (helpful vs blaming)

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

---

### 11. Copy and Messaging Deserve Dedicated Specification

**What we learned:**
- Copy isn't just "nice to have" - it's part of UX spec
- Tone consistency matters (formal vs casual)
- Small word choices impact perception ("Thanks!" vs "Thank you")
- Error messages need empathetic framing

**Best practice:**
- Include copy specifications in Section 6 (UX)
- Define tone (friendly, warm, professional, casual)
- Write exact copy for: buttons, placeholders, success messages, error messages
- Show alternatives with different tones
- Include rationale for tone choices

**Example:**
```
#### Success Messages
- "Thanks! Check your email..." (Warm, exclamation shows enthusiasm)
NOT: "Thank you. Please check your email." (Too formal, period = stern)
NOT: "Success! Email sent." (Technical, not human)
```

---

### 12. Accessibility Needs Concrete Implementation Specs

**What we learned:**
- "Make it accessible" is too vague
- Need specific ARIA attributes, keyboard navigation, screen reader announcements
- Include actual code examples for accessibility
- Accessibility intersects with UX (focus indicators, error announcements)

**Best practice:**
- Specify exact ARIA attributes needed
- Document keyboard navigation (tab order, enter/space behavior)
- Specify screen reader announcements for each state
- Include focus indicator specifications (color, size, offset)
- Document color contrast ratios (not just "high contrast")
- Reference WCAG level (AA vs AAA)

---

### 13. Animations Need Easing and Duration Specs

**What we learned:**
- "Smooth animation" isn't implementable
- Need exact durations (ms) and easing functions
- Different interaction types need different timings
- Easing affects perceived quality (linear vs ease-out)

**Best practice:**
- Create animation timing table
- Specify duration, easing function, and purpose for each animation
- Use standard easing functions (ease-in, ease-out, ease-in-out, linear)
- Document rationale (why this duration/easing?)

**Example table:**
| Element | Duration | Easing | Purpose |
|---------|----------|--------|---------|
| Button press | 100ms | ease-out | Immediate tactile feedback |
| Success fade-in | 300ms | ease-out | Celebratory appearance |

---

### 14. Mobile-Specific Considerations Need Separate Section

**What we learned:**
- Mobile isn't just "responsive CSS"
- Touch targets, keyboards, viewport behavior all differ
- Need specific mobile UX considerations
- iOS vs Android differences matter

**Best practice (in Section 6):**
- Document minimum touch target sizes (44px iOS HIG)
- Specify input types for mobile keyboards (type="email")
- Address viewport zoom behavior (16px font minimum)
- Show mobile vs desktop layouts separately
- Test on actual devices, not just browser resize

---

### 15. Security Section Needs Risk Assessment

**What we learned:**
- Different implementation approaches have different security risks
- Client-side API keys are risky (need mitigation)
- CORS, CSP, rate limiting all intersect
- Security isn't just "use HTTPS"

**Best practice (Section 8):**
- Assess risk level for each approach (LOW/MED/HIGH)
- Document mitigation strategies
- Specify CSP headers needed
- Include rate limiting (client-side and server-side)
- Address PII handling (where email goes, what's logged)
- Document GDPR compliance approach

---

### 16. User Wants Process Transparency

**What we learned:**
- User asked "why is this taking so long?"
- Wanted to see "threads you're pulling"
- Breakdown of work reduces perceived wait time
- Visibility into process builds trust

**Best practice:**
- Show todo list early (what will be done)
- Update todos in real-time (what's being done now)
- Break large tasks into visible subtasks
- Explain approach before executing (sequencing rationale)
- Ask for confirmation at decision points (which order to do sections?)

---

### 17. Involve User in Strategic Decisions

**What we learned:**
- User asked whether to do platform analysis now or later
- Wanted to participate in efficiency decision
- Users have context we don't (their priorities, timeline)

**Best practice:**
- Present options when strategic choice needed
- Explain rationale for each option
- Let user decide (they know their constraints)
- Document chosen approach in learnings

**Examples of strategic choices:**
- Section order (which first?)
- Platform decision timing (now or after requirements?)
- Level of detail (comprehensive vs minimal?)
- Implementation approach (client-side vs server-side?)

---

### 18. Context Switching Needs Explicit Todos

**What we learned:**
- Jumping between sections can lose track
- Todos mark clear checkpoints
- User can see what's complete vs pending
- Helps resume work if interrupted

**Best practice:**
- Update todos BEFORE starting new section
- Mark previous section completed
- Mark new section in_progress
- Keep pending sections visible (roadmap)

---

## Process Improvements for Future PRDs

### Before Starting PRD Creation:
1. Read existing PRDs in repo (understand format)
2. Read PRD-GUIDE.md (understand 13-section structure)
3. Check backlog for feature context
4. Create todo list for all 13 sections
5. Ask user: sequential delivery or monolithic?
6. Ask user: which sections are highest priority?

### During PRD Creation:
1. Complete sections sequentially (unless user requests otherwise)
2. Show section to user after completion
3. Get explicit approval before proceeding
4. Update todos in real-time
5. Use [TOOL] placeholder for undecided platforms
6. Document ALL options in technical specs
7. Ask user for strategic decisions (don't assume)

### Strategic Section Ordering:
- User Stories → Requirements → Tech Specs → UX (define WHAT)
- Edge Cases → Security → Testing → Deployment → Metrics (define HOW)
- Platform Analysis (make data-driven choice)
- Executive Summary (synthesize everything)

### Quality Checklist Before Showing Section:
- [ ] Acceptance criteria specific and testable
- [ ] Copy examples provided (exact wording)
- [ ] Timing specified (ms, not "fast")
- [ ] Error states equal detail to success states
- [ ] Mobile considerations included
- [ ] Accessibility specs concrete (ARIA, keyboard)
- [ ] Code examples where helpful
- [ ] Platform-agnostic where appropriate
- [ ] Dependencies documented
- [ ] Priorities assigned (P0, should-have, nice-to-have)

---

## Session-Specific Insights

### What worked well:
- Sequential section delivery with review gates
- Platform-agnostic [TOOL] placeholder
- Emotional journey mapping in UX section
- Precise timing specifications
- Strategic decision to do platform analysis AFTER requirements
- Breaking down 13 sections into trackable todos

### What to improve:
- Initial delay before showing progress (user wondered why taking long)
  → Solution: Show todos immediately, explain approach first
- Could have asked about section order sooner
  → Solution: Always ask user preferences for strategic decisions early

### User preferences observed:
- Wants visibility into process (todos, progress)
- Prefers efficiency (strategic approach)
- Values data-driven decisions (platform analysis after requirements)
- Appreciates comprehensive detail (emotional journey, timing specs)
- Wants control over strategic choices (asked which order is most efficient)

---

## Template Phrases for Future PRD Work

### Starting a section:
"Now working on Section X: [Name]. I'll document [what this section covers] and show you for review when complete."

### Completing a section:
"**Section X complete!** I've documented: [bullet list of what's included]. Ready for your review!"

### Requesting feedback:
"Does this Section X capture all the [user stories/requirements/etc.] you need? Should I add or modify anything before moving to Section Y?"

### Strategic decisions:
"I have two approaches: [Option A with rationale] vs [Option B with rationale]. Which would be most efficient for your needs?"

### Showing progress:
"I've completed sections 3-6. Remaining: sections 7-13 (technical details), then section 2 (platform choice), then section 1 (summary). This sequencing allows data-driven platform decision."

---

## Integration Notes

This file should be merged into PRD-GUIDE.md under new sections:
- "Best Practices for PRD Creation Process"
- "Sequential Section Delivery Approach"
- "Emotional Journey Mapping in UX"
- "Platform-Agnostic Requirements"
- "Strategic Section Sequencing"

Key additions to PRD-GUIDE.md:
1. Add process guidance (not just structure)
2. Add timing specifications to UX section template
3. Add emotional journey map template
4. Add quality checklist for each section
5. Add strategic sequencing guidance
