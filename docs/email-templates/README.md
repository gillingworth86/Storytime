# F005 Email Templates - Setup Guide

This directory contains email templates for the Storytime welcome sequence.

**PRD Reference:** `docs/prds/F005-email-welcome-sequence.md`
**GitHub Issue:** #29

---

## Quick Start

### Step 1: Configure Confirmation/Welcome Email (Automatic)

This email is sent automatically by Buttondown when someone signs up.

1. Log into [Buttondown](https://buttondown.email/)
2. Go to **Settings** → **Emails** → **Confirmation email**
3. Enable **"Custom confirmation email"**
4. Copy content from `01-confirmation-welcome.md`
5. **CRITICAL:** Ensure `{{ confirmation_url }}` is in the confirm button
6. Save and send a test email

### Step 2: Create Follow-up Email Templates (Manual Sending)

These emails are sent manually based on days since confirmation.

| Email | File | When to Send |
|-------|------|--------------|
| Vision | `02-vision.md` | Day 2 after confirmation |
| Sneak Peek | `03-sneak-peek.md` | Day 5 after confirmation |
| Engagement | `04-engagement.md` | Day 10 after confirmation |

To save as drafts in Buttondown:
1. Go to **Emails** → **New email**
2. Copy subject and content from template file
3. Save as draft (don't send yet)
4. Repeat for all 3 templates

---

## Daily Manual Process (Phase A)

**Time required:** 5-10 minutes/day

1. **Check Buttondown dashboard** for newly confirmed subscribers
2. **Identify which email to send** based on confirmation date:
   - Day 0-1: They just got the confirmation email
   - Day 2: Send Vision email
   - Day 5: Send Sneak Peek email
   - Day 10: Send Engagement email
3. **Send the appropriate email** via Buttondown
4. **Log in tracking spreadsheet** (see template below)

---

## Tracking Spreadsheet Template

Create a Google Sheet with these columns:

| Subscriber Email | Confirmed Date | Email 1 (Welcome) | Email 2 (Vision) | Email 3 (Sneak Peek) | Email 4 (Engagement) | Notes |
|------------------|----------------|-------------------|------------------|----------------------|----------------------|-------|
| user@example.com | 2026-01-25 | ✅ Auto | ⏳ 01-27 | ⏳ 01-30 | ⏳ 02-04 | |

**Legend:**
- ✅ = Sent (with date)
- ⏳ = Scheduled (with target date)
- ❌ = Unsubscribed
- 📩 = Replied (add to VIP list)

---

## Template Files

| File | Purpose |
|------|---------|
| `01-confirmation-welcome.md` | Automatic confirmation + welcome + story excerpt |
| `02-vision.md` | Day 2 - Founder story, build emotional connection |
| `03-sneak-peek.md` | Day 5 - Feature preview, generate excitement |
| `04-engagement.md` | Day 10 - Request feedback, identify engaged users |

---

## Key Metrics to Track

| Metric | Target | Where to Find |
|--------|--------|---------------|
| Confirmation email open rate | >60% | Buttondown analytics |
| Confirmation rate (clicks) | >50% | Buttondown analytics |
| Follow-up avg open rate | >40% | Buttondown analytics |
| Unsubscribe rate | <2% | Buttondown analytics |
| Reply rate | >5% | Count manually |

---

## Buttondown Configuration Checklist

- [ ] Custom confirmation email enabled
- [ ] Confirmation email content added with `{{ confirmation_url }}`
- [ ] Reply-to set to monitored inbox
- [ ] Test confirmation flow works end-to-end
- [ ] Email #2, #3, #4 saved as drafts
- [ ] Tracking spreadsheet created

---

## Phase B: Automation (Future)

When any of these trigger points are reached:
- 100 signups achieved
- Manual process taking >30 min/day
- Missing sends due to human error

**Then:** Upgrade to Buttondown Standard ($29/mo) for automations.

See PRD Section 11 for automation setup instructions.

---

## Troubleshooting

**Confirmation email not being received:**
- Check spam folder
- Verify subscriber email is correct
- Check Buttondown logs for bounces

**Links not working in emails:**
- Ensure `{{ confirmation_url }}` is correctly formatted
- Test send to personal email first

**Low open rates:**
- Check subject lines are compelling
- Verify emails aren't landing in spam
- Test different send times

---

**Last Updated:** 2026-01-25
