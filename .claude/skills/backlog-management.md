# Backlog Management Skill

**Purpose:** Guide Claude through selecting, tracking, and completing backlog items using GitHub Issues as the source of truth.

**Last Updated:** 2026-01-25

---

## Overview

This skill enables Claude to:
1. Find available work from the backlog
2. Pick up items with proper session tracking
3. Track progress during work
4. Handle session failures/restarts gracefully
5. Complete items with proper documentation
6. Hand off incomplete work to future sessions

**Source of Truth:** GitHub Issues with label `backlog`

---

## Quick Reference Commands

```bash
# View available work (prioritized)
gh issue list --label "backlog" --label "status:available" --state open --json number,title,labels --jq '.[] | "\(.number): \(.title) [\(.labels | map(.name) | join(", "))]"'

# View in-progress work (check for abandoned sessions)
gh issue list --label "backlog" --label "status:in-progress" --state open

# Pick up an item
gh issue edit <NUMBER> --add-label "status:in-progress" --remove-label "status:available"
gh issue comment <NUMBER> --body "Session <SESSION_ID> picked up this item on $(date +%Y-%m-%d)"

# Complete an item
gh issue close <NUMBER> --comment "Completed by session <SESSION_ID>. PR: #<PR_NUMBER>"
```

---

## Label System

### Priority Labels (mutually exclusive)
| Label | Meaning | Selection Order |
|-------|---------|-----------------|
| `priority:p0` | Critical/blocking | First |
| `priority:p1` | High value | Second |
| `priority:p2` | Medium value | Third |
| `priority:p3` | Nice to have | Fourth |

### Status Labels (mutually exclusive)
| Label | Meaning | Who Sets |
|-------|---------|----------|
| `status:available` | Ready to be picked up | Default / on creation |
| `status:in-progress` | Currently being worked on | Session that picks it up |
| `status:blocked` | Waiting on dependency/decision | Session that identifies blocker |

### Type Labels (can have multiple)
| Label | Meaning |
|-------|---------|
| `type:prd` | Requires PRD creation |
| `type:implementation` | Ready for coding |
| `type:bug` | Bug fix |
| `type:docs` | Documentation only |

### Phase Labels
| Label | Meaning |
|-------|---------|
| `phase:1-landing` | Phase 1: Landing page validation |
| `phase:2-app` | Phase 2: Full application |

---

## Workflow: Selecting Next Item

### Step 1: Check for In-Progress Items First

**CRITICAL:** Before selecting new work, check if there's abandoned in-progress work.

```bash
gh issue list --label "backlog" --label "status:in-progress" --state open --json number,title,body,comments
```

**If in-progress items exist:**
1. Read the issue comments to understand session history
2. Check the last comment date - if >24 hours old, likely abandoned
3. **Resume that work** (see "Restarting Failed Sessions" section)
4. Do NOT pick up new work until in-progress items are completed or explicitly re-queued

### Step 2: Check Dependencies

Before picking up any item, verify its dependencies are satisfied:

```bash
# Read the issue body for "Depends on:" section
gh issue view <NUMBER> --json body
```

**Dependency rules:**
- If issue says "Depends on: #X", check if #X is closed
- If dependency is open, the item is NOT available (even if labeled `status:available`)
- Comment on blocked items: "Blocked by #X - cannot start until dependency resolved"

### Step 3: Select by Priority

```bash
# Get highest priority available item
gh issue list --label "backlog" --label "status:available" --label "priority:p0" --state open --limit 1

# If no P0, try P1
gh issue list --label "backlog" --label "status:available" --label "priority:p1" --state open --limit 1

# Continue down priority levels...
```

### Step 4: Pick Up the Item

```bash
# Update labels
gh issue edit <NUMBER> --add-label "status:in-progress" --remove-label "status:available"

# Add session tracking comment
gh issue comment <NUMBER> --body "## Session Started

**Session ID:** <YOUR_SESSION_ID>
**Date:** $(date +%Y-%m-%d)
**Branch:** claude/<branch-name>

### Plan
- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

### Notes
Starting work on this item..."
```

---

## Workflow: Tracking Progress

### During Work

Add progress comments as you complete significant milestones:

```bash
gh issue comment <NUMBER> --body "### Progress Update

**Session:** <SESSION_ID>
**Status:** In progress

**Completed:**
- [x] Task 1
- [x] Task 2

**Remaining:**
- [ ] Task 3

**Notes:** <Any context for future sessions>"
```

### If Blocked

```bash
# Mark as blocked
gh issue edit <NUMBER> --add-label "status:blocked" --remove-label "status:in-progress"

# Explain the blocker
gh issue comment <NUMBER> --body "### Blocked

**Session:** <SESSION_ID>
**Blocker:** <Description of what's blocking>
**Needs:** <What's needed to unblock>

This item cannot proceed until the blocker is resolved."
```

### Before Session Ends (IMPORTANT)

**Always leave a handoff comment before your session ends:**

```bash
gh issue comment <NUMBER> --body "### Session Handoff

**Session:** <SESSION_ID>
**Date:** $(date +%Y-%m-%d)
**Status:** <Completed | Partially complete | Blocked>

**What was done:**
- Item 1
- Item 2

**What remains:**
- Item 3
- Item 4

**Current state:**
- Branch: <branch-name>
- Last commit: <commit-sha>
- PR: <PR number if created>

**Context for next session:**
<Any important context, decisions made, gotchas discovered>

**Files modified:**
- path/to/file1.md
- path/to/file2.html"
```

---

## Workflow: Restarting Failed/Interrupted Sessions

### Step 1: Find Abandoned Work

```bash
gh issue list --label "backlog" --label "status:in-progress" --state open
```

### Step 2: Read Session History

```bash
gh issue view <NUMBER> --comments
```

Look for:
- Last session ID that worked on it
- What was completed
- What remains
- Branch name and last commit
- Any blockers or context

### Step 3: Check Branch State

```bash
# Fetch and check the branch
git fetch origin
git log origin/<branch-name> --oneline -5

# Check for uncommitted work (if same machine)
git status
```

### Step 4: Resume Work

```bash
# Add resumption comment
gh issue comment <NUMBER> --body "### Session Resumed

**Previous Session:** <PREVIOUS_SESSION_ID>
**New Session:** <YOUR_SESSION_ID>
**Date:** $(date +%Y-%m-%d)

**Picking up from:**
<Summary of where previous session left off>

**Plan:**
- [ ] Remaining task 1
- [ ] Remaining task 2"
```

### Step 5: Continue from Last Known State

1. Check out the branch: `git checkout <branch-name>`
2. Pull latest: `git pull origin <branch-name>`
3. Review the last commit to understand state
4. Continue where previous session left off

---

## Workflow: Completing Items

### Step 1: Verify Completion Criteria

Check the issue's acceptance criteria are met:
- All tasks in the issue description completed
- Tests passing (if applicable)
- PR created and merged (if code change)
- Documentation updated (if required)

### Step 2: Close with Summary

```bash
gh issue close <NUMBER> --comment "### Completed

**Session:** <SESSION_ID>
**Date:** $(date +%Y-%m-%d)

**Deliverables:**
- PR #<NUMBER> merged
- Files: list key files changed

**Summary:**
<Brief description of what was delivered>

**Validation:**
- [ ] Acceptance criteria met
- [ ] Tests passing
- [ ] Deployed to production (if applicable)

**Follow-up items:** (if any)
- Create issue for X
- Note about Y"
```

### Step 3: Unblock Dependents

Check if any other issues were blocked on this one:

```bash
# Search for issues that depend on this one
gh issue list --label "backlog" --state open --search "depends on #<COMPLETED_NUMBER>"
```

For each blocked issue:
```bash
gh issue comment <BLOCKED_NUMBER> --body "Dependency #<COMPLETED_NUMBER> is now resolved. This item can proceed."
gh issue edit <BLOCKED_NUMBER> --add-label "status:available" --remove-label "status:blocked"
```

---

## Dependencies Framework

### Defining Dependencies

When creating issues, specify dependencies in the issue body:

```markdown
## Dependencies

**Depends on:**
- #12 - Email collection must be implemented first
- #15 - Analytics required for tracking

**Blocks:**
- #18 - Welcome sequence needs this
- #20 - A/B testing needs signup flow
```

### Dependency Rules

1. **Hard dependencies:** Cannot start until dependency is CLOSED
   - Example: "Implementation depends on PRD being approved"

2. **Soft dependencies:** Can start but cannot complete
   - Example: "Can develop locally but needs API key to deploy"

3. **Circular dependencies:** NEVER allowed
   - If detected, break the cycle by splitting items

### Checking Dependencies Programmatically

```bash
# Get issue body and parse dependencies
gh issue view <NUMBER> --json body --jq '.body' | grep -A5 "Depends on:"
```

### Dependency Diagram (Current Backlog)

```
Phase 1: Landing Page Validation
├── F001: Analytics ✅ DONE
├── F002: Email Collection (depends on: F001 ✅)
│   └── Ready for implementation
├── F003: A/B Testing (depends on: F002)
│   └── Blocked until F002 complete
├── F004: Social Proof (depends on: F002)
│   └── Blocked until F002 complete
└── F005: Email Welcome Sequence (depends on: F002)
    └── Blocked until F002 complete - BUT PRD can start now

Phase 2: Application (depends on: Phase 1 validation success)
├── F010: Story Generation
├── F011: User Authentication
├── F012: Story Dashboard
└── F013: Family Sharing
```

---

## Issue Templates

### New Feature (PRD Required)

```markdown
## Feature: [FXXX] - [Name]

**Priority:** P0 | P1 | P2 | P3
**Type:** PRD → Implementation
**Phase:** 1-landing | 2-app

### Description
[2-3 sentence description of the feature]

### Success Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

### Dependencies

**Depends on:**
- None | #XX - [reason]

**Blocks:**
- #XX - [reason]

### Effort Estimate
- PRD: X hours
- Implementation: X days

### Notes
[Any additional context]
```

### Implementation Task (PRD Exists)

```markdown
## Implementation: [FXXX] - [Name]

**Priority:** P0 | P1 | P2 | P3
**Type:** Implementation
**PRD:** docs/prds/FXXX-name.md

### Tasks
- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

### Dependencies

**Depends on:**
- PRD approved ✅
- #XX - [reason]

### Acceptance Criteria
[Copy from PRD or link to PRD section]

### Files to Modify
- path/to/file1
- path/to/file2
```

---

## Error Recovery

### Scenario: Session crashed mid-work

1. Check issue comments for last known state
2. Check git log for any commits made
3. Resume from last checkpoint (see "Restarting Failed Sessions")

### Scenario: Branch has conflicts

```bash
# Fetch latest
git fetch origin master

# Rebase (preferred) or merge
git rebase origin/master

# If conflicts, resolve and continue
git add .
git rebase --continue

# Update issue with conflict resolution notes
gh issue comment <NUMBER> --body "Resolved merge conflicts with master"
```

### Scenario: API/Service unavailable

1. Mark issue as blocked with reason
2. Create separate issue for the outage if systemic
3. Document workaround if possible
4. Resume when service restored

### Scenario: Picked up wrong item (dependency not met)

```bash
# Return item to available
gh issue edit <NUMBER> --add-label "status:available" --remove-label "status:in-progress"

# Comment explaining
gh issue comment <NUMBER> --body "Returning to available - dependency #XX not yet complete"

# Pick up the dependency instead (or find different work)
```

---

## Best Practices

### DO:
- ✅ Always check for in-progress items before picking new work
- ✅ Leave detailed handoff comments before session ends
- ✅ Update issue with progress at each milestone
- ✅ Check dependencies before starting
- ✅ Link commits and PRs to issues (`fixes #XX`)
- ✅ Close issues promptly when complete
- ✅ Unblock dependent issues after completion

### DON'T:
- ❌ Pick up new work when in-progress items exist
- ❌ Leave items in-progress without handoff notes
- ❌ Start work on items with unmet dependencies
- ❌ Forget to update status labels
- ❌ Create circular dependencies
- ❌ Work on multiple backlog items simultaneously (focus!)

---

## Integration with Other Skills

### PRD Framework (`.claude/prd-framework.md`)
- When issue has `type:prd` label, use PRD framework to create PRD
- PRD location: `docs/prds/FXXX-feature-name.md`
- After PRD complete, update issue to `type:implementation`

### CI/CD Guide (`.claude/cicd-implementation-guide.md`)
- Reference for deployment workflows
- Use when implementing features that affect CI/CD

---

## Metrics & Reporting

### Weekly Status Check

```bash
# Summary of backlog status
echo "=== Backlog Status ==="
echo "Available:"
gh issue list --label "backlog" --label "status:available" --state open --json number,title --jq '.[] | "  #\(.number): \(.title)"'

echo "In Progress:"
gh issue list --label "backlog" --label "status:in-progress" --state open --json number,title --jq '.[] | "  #\(.number): \(.title)"'

echo "Blocked:"
gh issue list --label "backlog" --label "status:blocked" --state open --json number,title --jq '.[] | "  #\(.number): \(.title)"'

echo "Completed (last 7 days):"
gh issue list --label "backlog" --state closed --json number,title,closedAt --jq '.[] | select(.closedAt > (now - 604800 | todate)) | "  #\(.number): \(.title)"'
```

---

**End of Backlog Management Skill**
