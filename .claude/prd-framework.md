# PRD Framework - Product Requirements Document Generator

**Purpose:** Convert backlog feature descriptions into fully-specified Product Requirements Documents (PRDs) that enable Claude Code to build features in a single, high-quality implementation cycle.

**Last Updated:** 2026-01-24

---

## Overview

This framework guides Claude through creating comprehensive PRDs from backlog items. A well-crafted PRD ensures:

1. **Clarity:** No ambiguity about what to build
2. **Completeness:** All edge cases and requirements covered
3. **Buildability:** Claude Code can implement without clarifications
4. **Testability:** Clear success criteria and test scenarios
5. **Scope Management:** Features sized appropriately for one-shot delivery

---

## When to Use This Framework

**Trigger:** User requests a PRD for a feature from `docs/backlog.md`

**Example:**
> "Create a PRD for F001: Analytics Integration"

**Your Response:**
1. Read the backlog item from `docs/backlog.md`
2. Follow the assessment process below
3. Generate a complete PRD in `docs/prds/FXXX-feature-name.md`

---

## PRD Assessment Process

### Phase 1: Discovery (ALWAYS DO THIS FIRST)

Before writing the PRD, gather context:

#### 1.1 Codebase Analysis
- **Read:** Current architecture, tech stack, existing patterns
- **Search:** Similar implementations already in codebase
- **Identify:** Dependencies, integration points, shared utilities
- **Check:** External service docs (APIs, SDKs, libraries)

#### 1.2 Feature Scoping
- **Estimate:** Implementation complexity (hours/days)
- **Assess:** Can this be built in ONE iteration without clarifications?
- **Decision:**
  - ✅ **Small/Medium (≤3 days):** Proceed with single PRD
  - ❌ **Large (>3 days):** Break into multiple sub-features

#### 1.3 Decomposition Strategy (if needed)
If feature is too large, break it down:

**Example:** F011: Story Generation Engine
- **Too large:** Full AI story generation with all features
- **Break into:**
  - F011a: Basic story generation (MVP - one API call)
  - F011b: Character customization layer
  - F011c: Story quality improvement (prompt engineering)
  - F011d: Multi-turn story conversations

**Rule:** Each sub-feature must be independently valuable and deployable.

---

### Phase 2: Requirements Gathering

#### 2.1 User Context
- Who will use this feature?
- What problem does it solve?
- What's the user's workflow?
- What are their pain points?

#### 2.2 Technical Context
- What systems does this integrate with?
- What data needs to persist?
- What APIs or SDKs are required?
- What are the performance requirements?

#### 2.3 Constraints & Non-Functional Requirements
- Security considerations (auth, data privacy, API keys)
- Performance targets (response time, throughput)
- Browser compatibility (if frontend)
- Mobile responsiveness (if applicable)
- Accessibility standards (WCAG 2.1 AA minimum)

---

## PRD Document Structure

Use this exact template for all PRDs:

```markdown
# PRD: [Feature ID] - [Feature Name]

**Status:** Draft | Ready for Build | In Progress | Completed
**Priority:** P0 | P1 | P2 | P3
**Effort Estimate:** X days
**Owner:** [If assigned]
**Created:** YYYY-MM-DD
**Last Updated:** YYYY-MM-DD

---

## 1. Executive Summary

[2-3 sentence overview of the feature and its value]

**Problem Statement:**
[What user problem does this solve?]

**Proposed Solution:**
[High-level approach to solving the problem]

**Success Criteria:**
- [Measurable outcome 1]
- [Measurable outcome 2]
- [Measurable outcome 3]

---

## 2. User Stories

### Primary User Story
**As a** [user type]
**I want** [action/feature]
**So that** [benefit/value]

**Acceptance Criteria:**
1. [Specific, testable criterion]
2. [Specific, testable criterion]
3. [Specific, testable criterion]

### Additional User Stories (if applicable)
[Repeat format above for secondary flows]

---

## 3. Functional Requirements

### 3.1 Core Functionality
**REQ-001:** [Specific requirement]
- **Description:** [Detailed explanation]
- **Priority:** Must-have | Should-have | Nice-to-have
- **Acceptance:** [How to verify this works]

**REQ-002:** [Next requirement]
[Continue for all functional requirements]

### 3.2 User Interface Requirements (if applicable)
- **Layout:** [Describe UI structure]
- **Components:** [List UI components needed]
- **Interactions:** [User interactions and feedback]
- **Responsive Behavior:** [Mobile, tablet, desktop considerations]
- **Accessibility:** [ARIA labels, keyboard navigation, screen reader support]

### 3.3 Data Requirements
- **Input Data:** [What data comes in?]
- **Output Data:** [What data goes out?]
- **Data Validation:** [Validation rules]
- **Data Persistence:** [What needs to be stored? Where?]

---

## 4. Technical Specifications

### 4.1 Architecture Overview
[Diagram or description of how this feature fits into existing architecture]

**Components:**
- **Frontend:** [Technologies, frameworks, libraries]
- **Backend:** [APIs, services, databases]
- **External Services:** [Third-party integrations]

### 4.2 API Contracts (if applicable)

#### Endpoint: [HTTP Method] /api/path
**Purpose:** [What this endpoint does]

**Request:**
```json
{
  "field1": "string",
  "field2": 123
}
```

**Response (Success - 200):**
```json
{
  "success": true,
  "data": {
    "result": "value"
  }
}
```

**Response (Error - 4xx/5xx):**
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error"
  }
}
```

**Validation Rules:**
- field1: Required, 1-100 characters
- field2: Optional, positive integer

[Repeat for all endpoints]

### 4.3 Data Models

#### Model: FeatureName
```typescript
interface FeatureName {
  id: string;              // UUID, primary key
  field1: string;          // Description
  field2: number;          // Description
  createdAt: Date;         // Timestamp
  updatedAt: Date;         // Timestamp
}
```

[Repeat for all data models]

### 4.4 External Dependencies
- **Service:** [e.g., Plausible Analytics]
  - **SDK/API:** [Link to documentation]
  - **Authentication:** [API key, OAuth, etc.]
  - **Configuration:** [Environment variables needed]
  - **Rate Limits:** [API limits to be aware of]

### 4.5 File Structure
```
/path/to/feature
├── components/
│   ├── FeatureComponent.tsx
│   └── FeatureSubComponent.tsx
├── hooks/
│   └── useFeature.ts
├── services/
│   └── featureService.ts
├── types/
│   └── feature.types.ts
└── tests/
    └── feature.test.ts
```

---

## 5. User Experience & Design

### 5.1 User Flows
**Flow 1: [Primary user action]**
1. User lands on [page/screen]
2. User clicks [button/link]
3. System [performs action]
4. User sees [result/feedback]

[Diagram if complex]

### 5.2 UI Components & States
**Component: FeatureButton**
- **Default State:** [Appearance and behavior]
- **Hover State:** [Visual feedback]
- **Loading State:** [Loading indicator]
- **Success State:** [Success feedback]
- **Error State:** [Error message display]
- **Disabled State:** [When disabled, appearance]

### 5.3 Responsive Design
- **Desktop (>1024px):** [Layout description]
- **Tablet (768-1024px):** [Layout adaptations]
- **Mobile (<768px):** [Mobile-specific changes]

### 5.4 Accessibility
- **Keyboard Navigation:** [Tab order, shortcuts]
- **Screen Readers:** [ARIA labels, live regions]
- **Color Contrast:** [WCAG 2.1 AA compliance]
- **Focus Indicators:** [Visible focus states]

---

## 6. Edge Cases & Error Handling

### 6.1 Edge Cases
**EDGE-001:** [Scenario]
- **Example:** User submits form while offline
- **Expected Behavior:** Show retry message, queue for later
- **Implementation:** Use service worker or show error

**EDGE-002:** [Next edge case]
[Continue for all edge cases]

### 6.2 Error Scenarios
**ERROR-001:** [Error type]
- **Trigger:** [What causes this error]
- **User Message:** [User-friendly error message]
- **Logging:** [What to log for debugging]
- **Recovery:** [How user can recover]

[Continue for all error scenarios]

### 6.3 Validation Rules
- **Field 1:** [Validation rules and error messages]
- **Field 2:** [Validation rules and error messages]

---

## 7. Security & Privacy

### 7.1 Authentication & Authorization
- **Who can access:** [User roles/permissions]
- **Auth method:** [Session, JWT, OAuth, etc.]
- **Token handling:** [Storage, expiration, refresh]

### 7.2 Data Protection
- **Sensitive data:** [What data is sensitive]
- **Encryption:** [At rest, in transit]
- **PII handling:** [GDPR/CCPA compliance]

### 7.3 API Security
- **Rate limiting:** [Requests per minute/hour]
- **Input sanitization:** [XSS, SQL injection prevention]
- **CORS policy:** [Allowed origins]

### 7.4 Secret Management
- **API Keys:** [How stored, rotated]
- **Environment Variables:** [Required vars]
- **Example .env:**
```
FEATURE_API_KEY=your_key_here
FEATURE_API_URL=https://api.example.com
```

---

## 8. Testing Requirements

### 8.1 Unit Tests
**Test Case 1:** [Function/component name]
- **Given:** [Initial state/input]
- **When:** [Action performed]
- **Then:** [Expected outcome]

[Continue for all unit test scenarios]

### 8.2 Integration Tests
**Test Case 1:** [Integration scenario]
- **Setup:** [Test environment, mocks, data]
- **Steps:** [Test procedure]
- **Expected:** [Result and side effects]

### 8.3 Manual Test Scenarios
**Scenario 1:** [Happy path]
1. [Step 1]
2. [Step 2]
3. [Expected result]

**Scenario 2:** [Error path]
[Continue for all manual test scenarios]

### 8.4 Performance Tests
- **Load Test:** [X concurrent users, Y requests/sec]
- **Response Time:** [<Xms for API, <Ys for page load]
- **Resource Usage:** [Memory, CPU limits]

---

## 9. Deployment & Configuration

### 9.1 Environment Variables
```bash
# Required
FEATURE_API_KEY=xxx
FEATURE_ENABLED=true

# Optional
FEATURE_DEBUG=false
FEATURE_TIMEOUT=5000
```

### 9.2 Feature Flags (if applicable)
- **Flag Name:** `feature_name_enabled`
- **Default:** `false`
- **Rollout Plan:** [Staged rollout strategy]

### 9.3 Database Migrations (if applicable)
```sql
-- Migration: add_feature_table
CREATE TABLE feature_name (
  id UUID PRIMARY KEY,
  field1 VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);
```

### 9.4 Third-Party Service Setup
**Service: [e.g., Plausible]**
1. [Setup step 1]
2. [Setup step 2]
3. [Verification step]

---

## 10. Success Metrics & Validation

### 10.1 KPIs (Key Performance Indicators)
- **Metric 1:** [Name] - Target: [X], Current: [Y]
- **Metric 2:** [Name] - Target: [X], Current: [Y]
- **Metric 3:** [Name] - Target: [X], Current: [Y]

### 10.2 Analytics Events
**Event:** `feature_action_completed`
```json
{
  "event": "feature_action_completed",
  "properties": {
    "user_id": "uuid",
    "feature_variant": "A",
    "duration_ms": 1234
  }
}
```

### 10.3 Success Criteria Checklist
- [ ] All functional requirements implemented
- [ ] All tests passing (unit, integration, e2e)
- [ ] Performance targets met
- [ ] Accessibility audit passed
- [ ] Security review completed
- [ ] Documentation updated
- [ ] Deployed to production
- [ ] Metrics tracking enabled

---

## 11. Implementation Plan

### 11.1 Task Breakdown
**Phase 1: Foundation (Day 1)**
- [ ] Task 1: [Specific, actionable task]
- [ ] Task 2: [Specific, actionable task]

**Phase 2: Core Features (Day 2)**
- [ ] Task 3: [Specific, actionable task]
- [ ] Task 4: [Specific, actionable task]

**Phase 3: Integration & Testing (Day 3)**
- [ ] Task 5: [Specific, actionable task]
- [ ] Task 6: [Specific, actionable task]

### 11.2 Dependencies
- **Depends on:** [Other features, services, or tasks]
- **Blocks:** [What can't start until this is done]

### 11.3 Risks & Mitigation
**Risk 1:** [Description]
- **Impact:** High | Medium | Low
- **Probability:** High | Medium | Low
- **Mitigation:** [How to reduce or handle]

---

## 12. Open Questions & Decisions

### Questions (to be resolved before build)
- [ ] **Q1:** [Question that needs answering]
  - **Answer:** [To be filled in]
  - **Decision Maker:** [Who decides]

### Decisions Made
- **D1:** [Decision description] - **Rationale:** [Why this choice]
- **D2:** [Next decision] - **Rationale:** [Why this choice]

---

## 13. References & Resources

### Documentation
- [External API Docs](https://link)
- [Internal Architecture Docs](path/to/docs)
- [Design Mockups](link/to/figma)

### Related Features
- F001: [Related feature]
- F002: [Another related feature]

### Code Examples
- [Similar implementation in codebase](path/to/file.ts:123)
- [External example](https://github.com/example)

---

## Appendix

### A. Glossary
- **Term 1:** Definition
- **Term 2:** Definition

### B. Change Log
- **2026-01-24:** Initial PRD created
- **YYYY-MM-DD:** [Change description]

---

**PRD Completeness Checklist (for Claude):**
- [ ] Executive summary clear and concise
- [ ] User stories with acceptance criteria
- [ ] All functional requirements specified
- [ ] Technical architecture documented
- [ ] API contracts defined (if applicable)
- [ ] Data models specified
- [ ] UI/UX flows documented
- [ ] Edge cases identified
- [ ] Error handling specified
- [ ] Security considerations addressed
- [ ] Testing requirements comprehensive
- [ ] Deployment steps clear
- [ ] Success metrics defined
- [ ] Implementation plan realistic
- [ ] No open questions remaining

**Ready for Build:** ☐ Yes ☐ No (resolve open items first)
```

---

## Claude's PRD Generation Process

When user requests a PRD (e.g., "Create PRD for F001"), follow this process:

### Step 1: Acknowledge & Confirm
```
I'll create a comprehensive PRD for [Feature ID: Name] from the backlog.
Let me first analyze the codebase and feature requirements.
```

### Step 2: Discovery (Use Tools)
- **Read:** `docs/backlog.md` to get feature details
- **Explore:** Codebase for similar patterns
- **Search:** External docs for APIs/services
- **Assess:** Feature complexity and scope

### Step 3: Scope Decision
**If feature is small/medium (≤3 days):**
```
This feature is appropriately scoped for a single implementation cycle.
I'll create a complete PRD now.
```

**If feature is large (>3 days):**
```
This feature is too large for a single implementation cycle.
I'm breaking it into [X] sub-features:
- F###a: [Sub-feature 1 - MVP]
- F###b: [Sub-feature 2]
- F###c: [Sub-feature 3]

Should I create PRDs for all sub-features, or start with the MVP?
```

### Step 4: Generate PRD
- Create file: `docs/prds/FXXX-feature-name.md`
- Fill in ALL sections (no TBDs or placeholders)
- Be specific and actionable
- Include code examples where helpful

### Step 5: Review & Validate
Before presenting PRD to user:
- [ ] All sections completed
- [ ] No ambiguous requirements
- [ ] Technical approach is sound
- [ ] Edge cases covered
- [ ] Testable acceptance criteria
- [ ] Realistic implementation plan

### Step 6: Present to User
```
✅ PRD created: docs/prds/FXXX-feature-name.md

**Summary:**
- Effort: X days
- Key Dependencies: [List]
- Ready for build: Yes/No

**Next Steps:**
1. Review PRD for accuracy
2. Resolve any open questions
3. Approve for implementation

Would you like me to proceed with building this feature?
```

---

## PRD Quality Standards

### Excellent PRD (Ready for Build)
- ✅ No ambiguity in requirements
- ✅ All edge cases identified
- ✅ Technical approach validated
- ✅ Complete test scenarios
- ✅ Clear success criteria
- ✅ Claude Code can build without clarifications

### Poor PRD (Not Ready)
- ❌ Vague requirements ("make it better")
- ❌ Missing edge cases
- ❌ Unvalidated technical approach
- ❌ No test scenarios
- ❌ Unclear success criteria
- ❌ Requires clarifications during build

**Goal:** Every PRD should be "Excellent" before building begins.

---

## Examples of Scope Decomposition

### Example 1: Large Feature → Sub-Features

**Original:** F011: Story Generation Engine (Too Large - 2 weeks)

**Decomposed:**
- **F011a:** Basic Story Generation API (3 days) - MVP
  - Single API call to Claude
  - Hard-coded prompt template
  - Return plain text story
  - No customization
- **F011b:** Character Customization (2 days)
  - User inputs: child name, age, interests
  - Dynamic prompt injection
  - Character consistency
- **F011c:** Story Quality Improvements (2 days)
  - Prompt engineering for better stories
  - Reading level adaptation
  - Theme selection
- **F011d:** Multi-Turn Stories (3 days)
  - Conversation history
  - Story continuation
  - Plot thread tracking

**Benefit:** Each sub-feature is independently valuable and testable.

### Example 2: Already Appropriately Scoped

**Original:** F001: Analytics Integration (1-2 days)

**Decision:** No decomposition needed
- Feature is small and focused
- Single integration point
- Clear success criteria
- Can be built in one iteration

**Action:** Create single comprehensive PRD

---

## Tips for Claude

### DO:
- ✅ Ask clarifying questions if backlog item is vague
- ✅ Research external APIs/services thoroughly
- ✅ Include realistic code examples
- ✅ Consider mobile and accessibility
- ✅ Think through edge cases deeply
- ✅ Specify exact error messages
- ✅ Define all data structures
- ✅ Include environment setup steps

### DON'T:
- ❌ Leave sections with "TBD" or "TODO"
- ❌ Use vague language ("should probably", "might need")
- ❌ Skip error handling or edge cases
- ❌ Assume user knows technical details
- ❌ Create PRDs that require clarification during build
- ❌ Over-engineer simple features
- ❌ Under-specify complex features

---

## Success Measurement

**PRD Quality Check:**
- Can Claude Code build this feature without asking ANY questions? → **Yes = Good PRD**
- Are all edge cases and errors handled? → **Yes = Good PRD**
- Could a different developer understand and build this? → **Yes = Good PRD**

If any answer is "No", the PRD needs more detail.

---

## Pull Request Best Practices

When creating a PR after implementation:

### Before Creating PR
1. **Review all commits** in the branch since diverging from base
2. **Summarize the actual changes** made (not just the PRD intent)
3. **Update PR title** to reflect what was built (not just the feature ID)

### PR Title Format
```
feat: [Concise description of what was built] (FXXX)
```

**Good examples:**
- `feat: Add social proof testimonials section (F004)`
- `feat: Integrate Buttondown email collection (F002)`

**Bad examples:**
- `F004 implementation` (too vague)
- `Create PRD for F004` (describes process, not outcome)

### PR Description Must Include
1. **Summary** - 2-3 bullet points of what changed
2. **Test plan** - How to verify the changes work
3. **Screenshots** - For UI changes (desktop + mobile)

### Template
```markdown
## Summary
- Added "Loved by Families" testimonials section after "How It Works"
- Implemented 4 testimonials with styled initials avatars
- Added Plausible "Social Proof Viewed" analytics event

## Test plan
- [ ] View testimonials section on desktop (2x2 grid)
- [ ] View on mobile (<768px) - should stack vertically
- [ ] Verify hover animation on cards
- [ ] Check Plausible event fires when scrolling to section

## Screenshots
[Desktop screenshot]
[Mobile screenshot]
```

**Key principle:** PR description should reflect the ACTUAL implementation, not just copy the PRD summary. Review commits before creating PR.

---

**Remember:** The goal is to enable ONE-SHOT feature delivery with excellent quality. Time spent on a thorough PRD pays off 10x during implementation.
