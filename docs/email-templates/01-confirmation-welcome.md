# Confirmation/Welcome Email Template

**Purpose:** Combined double opt-in confirmation + welcome + story preview
**Timing:** Automatic (sent by Buttondown on signup)
**Buttondown Setup:** Settings → Emails → Confirmation email

---

## Subject Line

```
Confirm your spot in the Storytime universe ✨
```

## Preview Text

```
Click to confirm + get a sneak peek of the magic inside...
```

---

## Email Content

Copy everything below the line into Buttondown's confirmation email editor:

---

**STORYTIME**

Hi there,

Welcome to the Storytime universe!

You're one click away from joining a community of parents who believe bedtime stories should be more than random tales—they should be adventures that remember, characters that return, and worlds that grow with your child.

<a href="{{ confirmation_url }}" style="display: inline-block; background-color: #fbbf24; color: #0f1419; padding: 14px 28px; text-decoration: none; border-radius: 6px; font-weight: bold;">Confirm Your Spot</a>

👆 Click to confirm your subscription

---

**While you're here, here's a tiny taste of what Storytime creates:**

> *"Maya pushed open the garden gate and gasped. The flowers glowed softly in the twilight, and a gentle 'whoo' came from the old oak tree. A beautiful silver owl swooped down, landing on a low branch.*
>
> *'Hello Maya,' said the owl in a voice like wind chimes. 'I'm Whisper, guardian of the Whispering Garden. We've been waiting for someone brave enough to hear the flowers' secrets.'"*

That's Maya meeting Whisper the Owl for the first time. In Storytime, Whisper will remember Maya—and your child—night after night.

---

**What's Next**

Once you confirm, you'll hear from me a few times over the next couple weeks with:

• The story behind why I'm building this
• A deeper look at how the "story memory" works
• A chance to shape what we build

No spam. Just genuine updates from a parent building something for parents.

---

Click the button above to confirm, and let the adventure begin.

Warmly,
The Storytime Team

---

*(If you didn't sign up for Storytime, you can safely ignore this email.)*

---

## Buttondown Configuration Notes

1. Navigate to **Settings → Emails → Confirmation email**
2. Enable **"Custom confirmation email"**
3. Paste the content above
4. **CRITICAL:** Ensure `{{ confirmation_url }}` is inside the confirm button/link
5. Send a test email to verify formatting
6. Test the confirmation link works

## Target Metrics

- Open rate: >60%
- Confirmation rate (clicks): >50%
