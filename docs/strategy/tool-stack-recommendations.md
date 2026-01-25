# Tool Stack Recommendations for Storytime Landing Page

## Budget: $21-50 total | Timeline: <1 week | Solo builder

---

## 1. Landing Page Builder

### Option A: Carrd (RECOMMENDED)
**Price:** $19/year (Pro Plus plan)

**Pros:**
- Incredibly simple, perfect for solo builder
- Beautiful templates optimized for conversions
- Built-in A/B testing on Pro Plus plan (critical for your headline variants)
- Mobile-responsive by default
- Fast setup (2-3 hours for complete page)
- Can embed email forms easily
- Custom domain included
- Forms can integrate with webhooks

**Cons:**
- Limited to 3 sites on Pro Plus (fine for your needs)
- Less design flexibility than Framer
- Not ideal if you want to scale to full website later

**Best for:** Quick validation, A/B testing, simple email capture

---

### Option B: Framer
**Price:** $5/month (Mini plan) = $60/year or $15 first 3 months

**Pros:**
- More design flexibility and animations
- Better for brand building if you want polished aesthetics
- Scales better if you want to add pages later
- CMS features for blog/updates
- More "professional" looking out of the box

**Cons:**
- Steeper learning curve (2x the setup time)
- A/B testing requires external tools or manual variant pages
- Overkill for pure validation
- Monthly commitment vs annual

**Best for:** If you care about brand perception and plan to expand site

---

### **RECOMMENDATION: Carrd Pro Plus ($19/year)**

**Why:** Built-in A/B testing is critical for testing your 4 headline variants. At your budget and timeline, Carrd gets you launched fastest with the features you actually need. You can always migrate to Framer after validation if you want more design flexibility.

**Alternative:** If you're comfortable with HTML/CSS and want to save $19, you could use a free static site on GitHub Pages or Netlify, but you'd lose built-in A/B testing and need to manually code everything.

---

## 2. Email Capture & Marketing

### Option A: Kit (ConvertKit) (RECOMMENDED)
**Price:** FREE for up to 10,000 subscribers

**Pros:**
- Strong automation features (sequences, tagging, branching)
- Visual email builder + plain-text support
- Built-in subscriber management and tagging
- Easy embed forms and landing pages
- Scales well if you grow past validation
- Solid deliverability and creator-focused tooling

**Cons:**
- Free tier branding on forms/emails
- API access requires a server-side proxy (no client-side CORS)
- Slightly more setup than a purely client-side embed

**Best for:** Solo builders who want growth-ready automation and a mainstream ESP

---

### Option B: MailerLite (Free Tier)
**Price:** FREE for up to 1,000 subscribers

**Pros:**
- Easy drag-and-drop editor
- Solid automations for basic sequences
- Simple landing pages and forms
- Competitive pricing as you grow

**Cons:**
- Smaller ecosystem than Kit
- Fewer creator-specific integrations
- UI can feel busy for a quick validation sprint

**Best for:** If you want a simple editor and basic automations at low cost

---

### **RECOMMENDATION: Kit (ConvertKit) Free tier**

**Why:** Free tier easily covers your 100-signup goal, automations are built in, and Kit is the best long-term fit if you validate and scale. It supports forms, tags, and sequences without needing a tool change later.

---

## 3. Analytics

### Option A: Plausible (RECOMMENDED)
**Price:** $9/month (~$27 for 3-week test)

**Pros:**
- Privacy-friendly, GDPR compliant (no cookie banner needed!)
- Simple, beautiful dashboard
- Tracks page views, referrers, conversion goals
- Can set up custom events (email signups, button clicks)
- Fast, lightweight script
- Australian company (bonus for your market)

**Cons:**
- Not free
- Less detailed than Google Analytics
- No session recordings

**Best for:** Privacy-conscious brands wanting clean, ethical analytics

---

### Option B: Simple Analytics
**Price:** $19/month (~$57 for 3-week test)

**Pros:**
- Similar privacy benefits to Plausible
- Slightly more features
- Beautiful UI

**Cons:**
- More expensive than Plausible
- Very similar feature set, hard to justify extra cost

---

### Option C: Google Analytics (Free)
**Price:** FREE

**Pros:**
- Free
- Incredibly detailed data
- Industry standard

**Cons:**
- Privacy nightmare (requires cookie banners)
- Overkill for validation
- Complex setup
- Conflicts with your "privacy-friendly" positioning

---

### **RECOMMENDATION: Plausible ($9/month)**

**Why:** Privacy-friendly analytics aligns with your brand promise ("no invasive tracking"). Parents care about privacy. $9/month is within budget, and you can cancel after the 3-week test. The clean dashboard makes it easy to track your key metric (signups per channel).

**Alternative:** If you want to save $27, use Carrd's built-in analytics for basic traffic stats and just track email signups manually. Not ideal, but workable for a scrappy validation test.

---

## 4. Domain

### Recommendation: Namecheap or Porkbun
**Price:** ~$10-15/year for .com

**Suggestions:**
- storytime.com (likely taken/expensive)
- getstorytime.com
- storytime.app
- mystorytime.com
- storytime.io
- bedtimestorytime.com

**RECOMMENDATION:** Register `getstorytime.com` or `storytime.app` (~$12-15)

---

## Total Cost Breakdown

### Recommended Stack:
- **Carrd Pro Plus:** $19/year
- **Kit (ConvertKit):** FREE (up to 10,000 subscribers)
- **Plausible:** $9/month × 1 month = $9 (cancel after test)
- **Domain:** $12-15/year
- **Total:** ~$40-43 (within $21-50 budget)

### Budget-Conscious Alternative:
- **Carrd Pro Plus:** $19/year
- **Kit (ConvertKit):** FREE
- **No paid analytics:** Use Carrd's basic stats + manual tracking
- **Domain:** $12-15
- **Total:** ~$31-34

---

## 5. Setup Priority Order

### Day 1-2:
1. Register domain
2. Sign up for Carrd Pro Plus
3. Sign up for Kit (ConvertKit) (free)
4. Sign up for Plausible (start 30-day trial)

### Day 3-4:
1. Build landing page in Carrd using provided copy
2. Set up 4 headline variants for A/B testing
3. Embed Kit signup form
4. Connect custom domain

### Day 5:
1. Add Plausible tracking code
2. Set up conversion goals (email signup)
3. Test on mobile devices
4. Test email delivery from Kit

### Day 6:
1. Set up email welcome sequence in Kit
2. Schedule follow-up emails

### Day 7:
1. Final testing
2. Soft launch to friends/family
3. Begin distribution campaign

---

## Tool Integration Setup

### Carrd + Kit Integration:
```html
<!-- Embed Kit form in Carrd -->
<form
  action="https://app.kit.com/forms/YOUR_FORM_ID/subscriptions"
  method="post"
>
  <input type="email" name="email" placeholder="Your email address" required />
  <input type="submit" value="Join waitlist" />
</form>
```

### Plausible + Carrd Integration:
Add this to Carrd's custom code section:
```html
<script defer data-domain="getstorytime.com" src="https://plausible.io/js/script.js"></script>
```

Set up custom goal for email signups in Plausible dashboard.

---

## Next Steps

1. **Decide on domain name** (check availability at namecheap.com)
2. **Register domain**
3. **Sign up for Carrd Pro Plus**
4. **Create Kit account**
5. **Start building the landing page using the copy provided**

Want me to create a detailed implementation guide with screenshots and step-by-step instructions for each tool?
