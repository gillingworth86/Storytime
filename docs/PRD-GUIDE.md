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

## Scope Management: Breaking Down Large Features

Claude automatically assesses if a feature is too large for one iteration:

### Small Feature (≤1 day)
**Example:** F002 - Email Collection Integration
- Single integration point (Buttondown API)
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

### Excellent PRD (Ready to Build) ✅
- All requirements are crystal clear
- Every edge case has a defined solution
- Technical approach is validated and documented
- Complete test scenarios provided
- Success criteria are measurable
- Claude can build without any questions

### Poor PRD (Not Ready) ❌
- Vague requirements ("make it good", "improve UX")
- Missing edge cases or error handling
- Unvalidated technical assumptions
- No test scenarios
- Unclear success criteria
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
