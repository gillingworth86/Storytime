# F005 Email Templates - Setup Guide

This directory contains email templates for the Storytime welcome sequence.

**PRD Reference:** `docs/prds/F005-email-welcome-sequence.md`
**GitHub Issue:** #18 (with sub-issues #29, #30)
**Email Platform:** Kit (formerly ConvertKit)

---

## Directory Structure

```
email-templates/
├── README.md                    # This file
├── 01-confirmation-welcome.md   # Markdown content - confirmation email
├── 02-vision.md                 # Markdown content - Day 2
├── 03-sneak-peek.md             # Markdown content - Day 5
├── 04-engagement.md             # Markdown content - Day 10
└── html/
    ├── README.md                # Kit setup instructions
    ├── _base-template.html      # Base HTML template
    ├── 01-confirmation-welcome.html
    ├── 02-vision.html
    ├── 03-sneak-peek.html
    └── 04-engagement.html
```

## Quick Start

### For Kit Setup (HTML Templates)

See `html/README.md` for detailed Kit configuration instructions.

**Quick steps:**
1. Go to Kit Dashboard → Settings → Email → Confirmation email
2. Paste `html/01-confirmation-welcome.html` (ensure `{{ confirmation_url }}` is present)
3. Create a new Sequence with emails #2, #3, #4
4. Connect sequence to your signup form

### Template Overview

| Email | File | Timing | Subject Line |
|-------|------|--------|--------------|
| Confirmation/Welcome | `01-*` | Immediate | Confirm your spot in the Storytime universe |
| Vision | `02-*` | Day 2 | Why I'm building Storytime |
| Sneak Peek | `03-*` | Day 5 | How Storytime remembers (sneak peek inside) |
| Engagement | `04-*` | Day 10 | Quick question (I'd love your input) |

---

## File Types

### Markdown Files (*.md)
- **Purpose:** Human-readable content for review and editing
- **Use:** Edit these to update email copy
- **Format:** Plain text with formatting hints

### HTML Files (html/*.html)
- **Purpose:** Production-ready templates for Kit
- **Use:** Copy/paste directly into Kit's HTML editor
- **Features:**
  - Matches Storytime landing page design
  - Mobile responsive
  - Email client compatible (Outlook, Gmail, Apple Mail)
  - Kit template variables included

---

## Key Metrics to Track

| Metric | Target | Where to Find |
|--------|--------|---------------|
| Confirmation email open rate | >60% | Kit analytics |
| Confirmation rate (clicks) | >50% | Kit analytics |
| Follow-up avg open rate | >40% | Kit analytics |
| Unsubscribe rate | <2% | Kit analytics |
| Reply rate | >5% | Count manually |

---

## Kit Configuration Checklist

- [ ] Custom confirmation email configured with HTML template
- [ ] `{{ confirmation_url }}` verified in confirmation button
- [ ] Reply-to set to monitored inbox
- [ ] Welcome sequence created with 3 emails (Day 2, 5, 10)
- [ ] Sequence connected to signup form
- [ ] Test emails sent and verified in multiple clients
- [ ] Mobile rendering tested

---

## Updating Email Content

### Workflow

1. **Edit Markdown** - Update content in `*.md` files
2. **Update HTML** - Apply changes to `html/*.html` files
3. **Test locally** - Open HTML in browser to preview
4. **Update Kit** - Paste new HTML into Kit dashboard
5. **Send test** - Verify rendering in email clients

### Design Elements

The HTML templates include these branded elements:
- **Gradient background:** Midnight → Twilight → Deep Purple
- **Card layout:** Subtle glass-morphism effect
- **Gold accents:** Buttons, highlights, borders
- **Story excerpts:** Styled quote blocks
- **Feature lists:** Emoji + text formatting

---

## Troubleshooting

**Confirmation email not being received:**
- Check spam folder
- Verify subscriber email is correct
- Check Kit logs for bounces

**Links not working in emails:**
- Ensure `{{ confirmation_url }}` is correctly formatted
- Test send to personal email first

**Low open rates:**
- Check subject lines are compelling
- Verify emails aren't landing in spam
- Test different send times

**Broken layout:**
- Use the HTML templates (not Markdown)
- Test in multiple email clients
- Check Kit's preview feature

---

## Phase B: Automation

Currently using Kit's built-in automation:
- Confirmation email: Automatic on signup
- Follow-up sequence: Automatic delays (Day 2, 5, 10)

All automation is handled by Kit - no manual intervention required once configured.

---

**Last Updated:** 2026-01-28
