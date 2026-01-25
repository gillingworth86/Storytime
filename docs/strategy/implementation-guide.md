# Storytime Implementation Guide

**Timeline:** 7 days from setup to launch
**Budget:** ~$40-43

---

## Day 1-2: Setup & Registration

### Step 1: Register Domain (30 minutes)

1. Go to **Namecheap.com** or **Porkbun.com**
2. Search for domain options:
   - First choice: `getstorytime.com`
   - Backup: `storytime.app`, `mystorytime.com`, `bedtimestorytime.com`
3. Purchase domain (~$12-15)
4. **Don't configure DNS yet**—we'll do this after Carrd setup

**⏸ Pause here if domain isn't available—pick alternative before proceeding**

---

### Step 2: Sign Up for Carrd (15 minutes)

1. Go to **carrd.co**
2. Click "Sign Up"
3. Choose **Pro Plus** plan ($19/year)
   - This includes A/B testing which is critical for your headline variants
4. Complete payment
5. Verify email

---

### Step 3: Sign Up for Kit (ConvertKit) (10 minutes)

1. Go to **kit.com**
2. Click "Start free"
3. Choose the **Free** plan (up to 10,000 subscribers)
4. Set up your creator profile
5. Verify email
6. **Create a form** for your waitlist (we'll embed it in Carrd)

**Where to find the form embed:**
- Forms → Select your form → Embed → Copy the HTML or use the form action URL

---

### Step 4: Sign Up for Plausible (15 minutes)

1. Go to **plausible.io**
2. Start free 30-day trial (no credit card needed)
3. Add your domain: `getstorytime.com` (or your chosen domain)
4. **Save your tracking script**—you'll add this to Carrd later

**Script will look like:**
```html
<script defer data-domain="getstorytime.com" src="https://plausible.io/js/script.js"></script>
```

---

## Day 3-4: Build Landing Page

### Step 5: Create Landing Page in Carrd (3-4 hours)

#### 5.1 Choose a Template

1. Log into Carrd
2. Click "New Site"
3. Choose template category: **Landing**
4. Recommended templates that work well for this:
   - "Aerial" (clean, conversion-focused)
   - "Frame" (modern, image-focused)
   - "Lens" (minimal, fast-loading)
5. Select template and click "Choose"

#### 5.2 Structure Your Page

Create these sections (in order):

1. **Hero Section**
   - Headline: [Use Variant B from landing-page-copy.md]
   - Subheadline
   - Email capture form
   - Hero image/illustration (stock photo of parent reading to child, or simple illustration)

2. **How It Works** (3-4 steps with icons)
   - Step 1: Tell us about your child
   - Step 2: Receive your first story in 30 seconds
   - Step 3: Watch their universe grow
   - Step 4: Bring the magic into the real world (coming soon)

3. **Sample Story Progression**
   - Title: "See how Maya's universe grows"
   - Show Story 1, Story 3, Story 7 from landing-page-copy.md
   - Use cards or expandable sections

4. **Pricing Section**
   - Free tier: First 10 stories
   - Paid tier: $9.99/month for unlimited
   - Money-back guarantee badge

5. **FAQ Section**
   - Use accordion/collapsible elements
   - Include 5-6 most important FAQs from landing-page-copy.md

6. **Footer CTA**
   - "Ready to start your child's story universe?"
   - Email capture form (same as hero)
   - Footer links

#### 5.3 Add Kit Email Form

1. In Carrd editor, add a "Form" element where you want email capture
2. Click "Form Settings"
3. Choose "Custom" action
4. Paste the Kit form action URL:
   ```
   https://app.kit.com/forms/YOUR_FORM_ID/subscriptions
   ```
5. Set method to "POST"
6. Add email field with placeholder "Your email address"
7. Add submit button text: "Join waitlist" or "Start your story universe"

**Test the form:**
- Click "Publish" → "Preview"
- Submit a test email
- Check Kit dashboard to confirm it arrived

#### 5.4 Design Tips

**Colors:**
- Use warm, calming colors (soft blues, purples, warm neutrals)
- Avoid harsh reds or aggressive CTAs
- Consider: #6B4FBB (purple), #F7B32B (warm yellow), #2D3142 (dark blue-gray)

**Fonts:**
- Headline: Something friendly but readable (Poppins, Quicksand, Nunito)
- Body: Highly readable (Inter, Open Sans, Source Sans Pro)

**Images:**
- Use Unsplash.com for free stock photos (search "parent child bedtime")
- Or use simple illustrations from unDraw.co (free, customizable)

**Mobile optimization:**
- Preview on mobile (Carrd has mobile preview)
- Ensure text is readable at small sizes
- Make CTA buttons thumb-friendly (minimum 44px height)

---

### Step 6: Set Up A/B Testing for Headlines (30 minutes)

Carrd Pro Plus includes built-in A/B testing:

1. In Carrd editor, click "Settings" → "A/B Testing"
2. Create 4 variants (one for each headline):
   - **Variant A:** "Build a story universe with your child"
   - **Variant B:** "Stories that remember. Adventures that continue."
   - **Variant C:** "Never run out of bedtime stories again"
   - **Variant D:** "Custom bedtime stories in 30 seconds"

3. Set traffic split to 25% each
4. Keep everything else identical across variants
5. Publish all variants

**Tracking:**
- Plausible will track which variant gets most traffic
- Kit signup numbers will show which converts best
- After 100 total visitors per variant, pick winner

---

### Step 7: Connect Custom Domain (30 minutes)

#### 7.1 In Carrd:
1. Go to site settings
2. Click "Domain"
3. Add your custom domain: `getstorytime.com`
4. Carrd will show you DNS records to add

#### 7.2 In Namecheap/Porkbun:
1. Log into domain registrar
2. Go to DNS management
3. Add records provided by Carrd:
   - Usually an A record pointing to Carrd's IP
   - And a CNAME for www subdomain

4. **Wait 1-24 hours for DNS propagation**

**Test:**
- Visit your domain in incognito mode
- Should show your Carrd page

---

## Day 5: Add Analytics & Testing

### Step 8: Add Plausible Tracking (15 minutes)

1. In Carrd editor, go to "Settings" → "Advanced"
2. Find "Head Code" section
3. Paste your Plausible tracking script:
```html
<script defer data-domain="getstorytime.com" src="https://plausible.io/js/script.js"></script>
```
4. Save and publish

**Set up conversion goals in Plausible:**
1. Go to Plausible dashboard
2. Click "Settings" → "Goals"
3. Add custom event goal: `Signup` or `Email_Submit`
4. In Carrd form, add this to the form action attributes:
```javascript
plausible('Signup');
```

---

### Step 9: Test Everything (1 hour)

Create a testing checklist:

- [ ] Hero section loads correctly
- [ ] All 4 headline variants are live and rotating
- [ ] Email form submits successfully
- [ ] Test email appears in Kit dashboard
- [ ] Sample stories are readable and formatted well
- [ ] Pricing section is clear
- [ ] FAQ accordions expand/collapse
- [ ] Footer CTA works
- [ ] Mobile view looks good (test on actual phone)
- [ ] Page loads fast (under 3 seconds)
- [ ] Plausible tracking is working (check dashboard)
- [ ] Domain is live and SSL certificate is active (https://)

**Test on these devices:**
- Desktop (Chrome, Firefox, Safari)
- Mobile (iPhone, Android)
- Tablet (iPad if available)

---

## Day 6: Email Sequence Setup

### Step 10: Set Up Email Automation in Kit (2 hours)

#### 10.1 Welcome Email (Day 0)

1. In Kit, go to **Sequences** → "New Sequence"
2. Create the welcome email using content from `email-sequence.md` (Email 1)
3. Set it to send **immediately upon signup**
4. Attach the sequence to your signup form in **Automations**

**Subject:** Welcome to Storytime! Quick question...

[Use content from email-sequence.md]

#### 10.2 Schedule Follow-up Emails

**Email 2 (Day 3):**
- Subject: "Here's what we're building ✨"
- Schedule to send 3 days after signup
- Include sample story

**Email 3 (Day 7):**
- Subject: "Quick favour? Help me prioritize"
- Schedule to send 7 days after signup
- Include link to survey (create in Google Forms or Typeform)

**Email 4 (Day 14):**
- Subject: "The awkward question: what would you actually pay?"
- Schedule to send 14 days after signup
- Pricing validation question

**Kit automation:**
- Use tags to segment subscribers
- Trigger the sequence when someone subscribes via your form
- Test by subscribing yourself with a test email

---

### Step 11: Create Feature Survey (30 minutes)

Use **Google Forms** (free) or **Typeform** (better UX, free tier available):

1. Create form with questions from email-sequence.md
2. Make it short (10 questions max, 2 minutes to complete)
3. Get shareable link
4. Add link to Email 3

**Survey URL should be:**
- Short: Use bit.ly or tinyurl to shorten
- Trackable: Add UTM parameters to track source

---

## Day 7: Final Pre-Launch

### Step 12: Soft Launch to Friends & Family (1 hour)

**Before going public, test with 5-10 trusted people:**

1. Send personalized messages to friends/family who are parents
2. Ask for brutal honesty:
   - Is the value prop clear?
   - Would you sign up?
   - What's confusing?
   - Any typos or broken links?

3. Make any necessary tweaks based on feedback

---

### Step 13: Create Social Media Assets (1 hour)

Prepare these for distribution:

**Twitter/X:**
- 3-4 tweet variations
- Hero image (1200x675px)

**Facebook:**
- Post copy variations
- Square image (1080x1080px)

**Reddit:**
- Post templates (already created in distribution-plan.md)
- Screenshot of landing page for proof

**Tools for images:**
- Canva.com (free tier)
- Use brand colors
- Include headline + CTA

---

### Step 14: Final Checklist Before Launch

- [ ] Landing page is live on custom domain
- [ ] SSL certificate is active (https)
- [ ] All 4 headline variants are rotating
- [ ] Email capture form works and submits to Kit
- [ ] Welcome email sends immediately
- [ ] Follow-up emails are scheduled
- [ ] Plausible tracking is working
- [ ] Conversion goals are set up in Plausible
- [ ] Page loads fast (<3 seconds)
- [ ] Mobile-responsive on all devices
- [ ] All links work (FAQ, footer links, etc.)
- [ ] Typos checked and fixed
- [ ] Privacy policy page created (required for email capture)
- [ ] Terms of service page created (optional but recommended)
- [ ] Distribution posts are drafted and ready
- [ ] Spreadsheet set up to track signups by channel

---

## Launch Day: Distribution Begins

### Step 15: Execute Week 1 Distribution Plan

**Monday morning (launch day):**

1. **Reddit posts:**
   - r/SideProject (feedback request)
   - r/roastmystartup (validation)

2. **Track immediately:**
   - Open Plausible dashboard
   - Monitor real-time traffic
   - Watch for signup notifications from Kit

3. **Engage:**
   - Respond to every comment within 2 hours
   - Answer questions authentically
   - Thank people for feedback

4. **Tuesday-Wednesday:**
   - Post to r/Parenting (story share)
   - Share in 2-3 Facebook groups

5. **Thursday-Friday:**
   - Post to r/daddit and r/Mommit
   - Tweet about it

6. **Weekend:**
   - Monitor analytics
   - Calculate conversion rates by channel
   - Identify what's working

---

## Ongoing: Weeks 2-3

### Week 2: Double Down on Winners

1. Check analytics from Week 1
2. Identify channel with highest conversion
3. Post to 5 more communities in that channel
4. A/B test results: Pick winning headline, update all variants to use it

### Week 3: Final Push

1. Cross-post to remaining communities
2. Reach out to micro-influencers
3. Ask early subscribers to share
4. Post "48 hours left" urgency message
5. Track toward 100 signup goal

---

## Tools Reference

### Access URLs:
- **Landing page:** https://getstorytime.com (your domain)
- **Carrd dashboard:** https://carrd.co/dashboard
- **Kit dashboard:** https://app.kit.com/
- **Plausible analytics:** https://plausible.io/getstorytime.com

### Logins:
Store these securely (use password manager):
- Domain registrar login
- Carrd login
- Kit login
- Plausible login

---

## Troubleshooting

### Email form not working:
- Check Kit form action URL is correct
- Verify POST method is set
- Test with different email providers (Gmail, Outlook, etc.)
- Check Kit dashboard for error logs

### Domain not connecting:
- DNS propagation can take up to 24 hours
- Use dnschecker.org to verify DNS records
- Double-check DNS records match Carrd's requirements
- Try clearing browser cache

### Plausible not tracking:
- Check script is in <head> section, not <body>
- Disable ad blockers when testing
- View page source to confirm script is present
- Check browser console for JavaScript errors

### Low conversion rates:
- Review headline clarity
- Check mobile experience
- Reduce friction (fewer form fields)
- Add more social proof or testimonials
- Test different CTA button copy

---

## Success Metrics Dashboard

Track these weekly:

| Metric | Week 1 | Week 2 | Week 3 | Goal |
|--------|--------|--------|--------|------|
| Total traffic | | | | 1000+ |
| Email signups | | | | 100 |
| Conversion rate | | | | 10%+ |
| Best channel | | | | Identified |
| Winning headline | | | | Identified |

---

## Post-Launch: If You Hit 100 Signups

1. **Send celebration email** to all subscribers
2. **Validate pricing** with Day 14 email responses
3. **Begin building MVP** of actual product
4. **Set up payment processing** (Stripe)
5. **Plan beta launch** for email subscribers

---

## Post-Launch: If You Don't Hit 100 Signups

1. **Analyze why:**
   - Low traffic? → Distribution problem
   - High traffic, low conversion? → Messaging problem
   - Lukewarm feedback? → Product-market fit problem

2. **Pivot or iterate:**
   - Test different value props
   - Target different audience
   - Adjust pricing
   - Or shelve idea and move on

3. **Celebrate learning:**
   - You validated (or invalidated) in <3 weeks
   - Cost: ~$40
   - That's a successful validation test

---

## Next Steps After This Guide

1. Register domain ✓
2. Sign up for Carrd Pro Plus ✓
3. Sign up for Kit ✓
4. Sign up for Plausible trial ✓
5. Build landing page ✓
6. Launch and distribute ✓

**Ready to start? Begin with Day 1-2 setup tasks.**

Questions or stuck? Document issues and iterate quickly. The goal is to launch within 7 days, not achieve perfection.

Good luck! 🚀
