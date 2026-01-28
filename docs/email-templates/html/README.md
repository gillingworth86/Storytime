# HTML Email Templates for Kit

These HTML email templates are designed to match the Storytime landing page styling and are ready to be loaded into Kit (formerly ConvertKit).

## Template Files

| File | Subject Line | Timing | Purpose |
|------|--------------|--------|---------|
| `01-confirmation-welcome.html` | Confirm your spot in the Storytime universe | Automatic on signup | Double opt-in + welcome + story preview |
| `02-vision.html` | Why I'm building Storytime | Day 2 | Founder story, emotional connection |
| `03-sneak-peek.html` | How Storytime remembers (sneak peek inside) | Day 5 | Feature preview, generate excitement |
| `04-engagement.html` | Quick question (I'd love your input) | Day 10 | Request feedback, identify engaged users |

## Design System

These templates use the Storytime brand design system:

### Colors
- **Midnight:** `#0f1419` - Background
- **Twilight:** `#1a1f3a` - Secondary background
- **Deep Purple:** `#2d1b4e` - Accent background
- **Purple:** `#6366f1` - Border accent
- **Amber:** `#f59e0b` - Primary CTA
- **Gold:** `#fbbf24` - Highlights, links
- **Cream:** `#fef3c7` - Headings
- **Text Primary:** `#f9fafb` - Emphasis text
- **Text Secondary:** `#d1d5db` - Body text

### Typography
- **Headings:** Georgia, serif (fallback for Fraunces)
- **Body:** System font stack (-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif)

### Layout
- Max width: 600px
- Mobile responsive with media queries
- Table-based layout for email client compatibility

## Kit Template Variables

These templates use Kit's Liquid templating syntax:

| Variable | Description |
|----------|-------------|
| `{{ confirmation_url }}` | Double opt-in confirmation link (Email #1 only) |
| `{{ unsubscribe_url }}` | Unsubscribe link |
| `{{ address }}` | Physical mailing address (CAN-SPAM compliance) |
| `{{ subscriber.first_name }}` | Subscriber's first name (if collected) |

## Loading Templates into Kit

### Step 1: Confirmation Email (Email #1)

1. Go to Kit Dashboard → **Settings** → **Email**
2. Find **Confirmation email** section
3. Click **Edit** or **Customize**
4. Switch to HTML mode
5. Copy the entire contents of `01-confirmation-welcome.html`
6. Paste into the HTML editor
7. **Verify** the `{{ confirmation_url }}` variable is in the button link
8. Save and send a test email

### Step 2: Create Email Sequence

1. Go to Kit Dashboard → **Sequences**
2. Click **+ New Sequence**
3. Name it "Storytime Welcome Sequence"

#### Add Email #2 (Vision)
1. Click **+ Add Email**
2. Set delay: **2 days** after subscription
3. Subject: `Why I'm building Storytime`
4. Switch to HTML mode
5. Paste contents of `02-vision.html`
6. Save

#### Add Email #3 (Sneak Peek)
1. Click **+ Add Email**
2. Set delay: **5 days** after subscription
3. Subject: `How Storytime remembers (sneak peek inside)`
4. Switch to HTML mode
5. Paste contents of `03-sneak-peek.html`
6. Save

#### Add Email #4 (Engagement)
1. Click **+ Add Email**
2. Set delay: **10 days** after subscription
3. Subject: `Quick question (I'd love your input)`
4. Switch to HTML mode
5. Paste contents of `04-engagement.html`
6. Save

### Step 3: Connect Sequence to Form

1. Go to Kit Dashboard → **Forms & Landing Pages**
2. Select your signup form
3. Under **Incentive** or **Settings**, find sequence settings
4. Connect the "Storytime Welcome Sequence"

## Testing

Before going live:

1. **Send test emails** to yourself from Kit
2. **Check rendering** in:
   - Gmail (web + mobile)
   - Apple Mail (iOS + Mac)
   - Outlook (web)
3. **Verify links** work correctly
4. **Test on mobile** devices
5. **Check spam score** using Kit's built-in tools

## Customization

### Updating Content
1. Edit the HTML files in this directory
2. Re-paste into Kit
3. Content is between the `<td class="content">` tags

### Using the Base Template
`_base-template.html` provides the foundational structure. To create new emails:
1. Copy the base template
2. Replace `{{EMAIL_TITLE}}` with your subject
3. Replace `{{PREVIEW_TEXT}}` with preview text
4. Replace `{{EMAIL_CONTENT}}` with your content

## Troubleshooting

**Emails landing in spam:**
- Ensure `{{ unsubscribe_url }}` is present
- Keep image-to-text ratio low
- Avoid spammy words in subject lines

**Broken layout in Outlook:**
- Use table-based layout (already implemented)
- Avoid CSS properties unsupported by Outlook
- Test with Litmus or Email on Acid

**Images not loading:**
- Host images on reliable CDN
- Always include alt text
- Use absolute URLs

---

**Last Updated:** 2026-01-28
