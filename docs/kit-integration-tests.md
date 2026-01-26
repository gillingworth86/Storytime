# Kit Email Integration - Test Checklist

## Overview
This document covers all test scenarios for the Kit (ConvertKit) email signup integration on the Storytime landing page.

**Form locations:**
- Hero section (top of page)
- CTA section (mid-page)
- Footer section

---

## 1. Basic Functionality Tests

### 1.1 Form Submission
| Test | Steps | Expected Result | Status |
|------|-------|-----------------|--------|
| Valid email submits | Enter valid email, click submit | Success message appears, subscriber created in Kit | |
| Invalid email rejected | Enter "notanemail", click submit | Browser validation prevents submission | |
| Empty email rejected | Leave empty, click submit | Browser validation prevents submission | |
| Email with spaces | Enter " test@example.com " | Should trim and submit successfully | |

### 1.2 Kit Dashboard Verification
| Test | Steps | Expected Result | Status |
|------|-------|-----------------|--------|
| Subscriber created | Submit form, check Kit dashboard | New subscriber appears in list | |
| Subscriber state | Check subscriber details | State should be "unconfirmed" until email verified | |
| Confirmation email sent | Check inbox | Confirmation email received from Kit | |

---

## 2. UI/UX Tests

### 2.1 Success State
| Test | Steps | Expected Result | Status |
|------|-------|-----------------|--------|
| Success message displays | Submit valid email | Green success message: "Success! Now check your email..." | |
| Form input clears | After success | Email input is cleared | |
| Other forms disabled | Submit on hero form | CTA and footer forms become grayed out, disabled | |
| Disabled form appearance | Check disabled forms | Opacity reduced, inputs show "Already subscribed" | |

### 2.2 Error State
| Test | Steps | Expected Result | Status |
|------|-------|-----------------|--------|
| Network error | Disconnect internet, submit | Error message displays (may vary) | |
| Rate limit | Submit many times quickly | Kit handles rate limiting | |

### 2.3 Persistence
| Test | Steps | Expected Result | Status |
|------|-------|-----------------|--------|
| Page reload after subscribe | Subscribe, reload page | All forms disabled, "Already on list" message | |
| New browser/incognito | Open in incognito | Forms work (localStorage cleared) | |
| Clear localStorage | Clear storage, reload | Forms work again | |

---

## 3. Analytics/Tracking Tests

### 3.1 Plausible Events
| Test | Steps | Expected Result | Status |
|------|-------|-----------------|--------|
| Form Viewed - Hero | Scroll to hero form | Plausible: "Form Viewed" with location: "hero" | |
| Form Viewed - CTA | Scroll to CTA section | Plausible: "Form Viewed" with location: "mid-page" | |
| Form Viewed - Footer | Scroll to footer | Plausible: "Form Viewed" with location: "footer" | |
| Email Signup - Hero | Submit on hero form | Plausible: "Email Signup" with location: "hero" | |
| Email Signup - CTA | Submit on CTA form | Plausible: "Email Signup" with location: "mid-page" | |
| Email Signup - Footer | Submit on footer form | Plausible: "Email Signup" with location: "footer" | |
| Social Proof Viewed | Scroll to testimonials | Plausible: "Social Proof Viewed" | |

### 3.2 Verifying Plausible
1. Open browser DevTools → Network tab
2. Filter by "plausible"
3. Submit form
4. Look for POST request to plausible.io with event data

---

## 4. Cross-Browser Tests

| Browser | Form Submit | Success Message | Form Disable | Analytics |
|---------|-------------|-----------------|--------------|-----------|
| Chrome (desktop) | | | | |
| Safari (desktop) | | | | |
| Firefox (desktop) | | | | |
| Chrome (mobile) | | | | |
| Safari (iOS) | | | | |
| Samsung Internet | | | | |

---

## 5. Responsive Design Tests

| Viewport | Form Layout | Input Usable | Button Clickable |
|----------|-------------|--------------|------------------|
| Desktop (1920px) | | | |
| Laptop (1366px) | | | |
| Tablet (768px) | | | |
| Mobile (375px) | | | |
| Mobile (320px) | | | |

---

## 6. Edge Cases

| Test | Steps | Expected Result | Status |
|------|-------|-----------------|--------|
| Already subscribed email | Submit same email twice | Kit handles gracefully (may show success or "already subscribed") | |
| Very long email | Enter 254-char email | Should submit if valid | |
| Unicode in email | Enter test@例え.jp | Should handle international domains | |
| Rapid double-click | Double-click submit fast | Only one submission processed | |
| Form submit while offline | Go offline, submit | Graceful error handling | |

---

## 7. Security Tests

| Test | Steps | Expected Result | Status |
|------|-------|-----------------|--------|
| CSP headers present | Check response headers | Content-Security-Policy header present | |
| Kit domains allowed | Check CSP | *.kit.com and *.convertkit.com in connect-src | |
| No console errors | Open console, use site | No CSP violation errors | |
| HTTPS only | Try HTTP | Redirects to HTTPS | |

---

## 8. Performance Tests

| Test | Method | Target | Actual |
|------|--------|--------|--------|
| Kit script load | DevTools Network | < 100ms | |
| Form submit response | DevTools Network | < 2s | |
| Time to interactive | Lighthouse | < 3s | |

---

## Quick Smoke Test (5 minutes)

Run this before any deployment:

1. [ ] Load production URL
2. [ ] Enter test email in hero form
3. [ ] Click submit
4. [ ] Verify success message appears
5. [ ] Verify other forms are disabled
6. [ ] Check Kit dashboard for new subscriber
7. [ ] Check Plausible for "Email Signup" event
8. [ ] Reload page - verify "Already on list" state

---

## Test Data

**Test emails:**
- Use `+` addressing: `youremail+test1@gmail.com`
- Or Kit's test mode if available

**Clearing test state:**
```javascript
// Run in browser console to reset local state
localStorage.removeItem('storytime_subscribed');
localStorage.removeItem('storytime_sub_location');
location.reload();
```

---

## Known Limitations

1. **Preview URLs**: Kit may not accept submissions from Vercel preview URLs - test on production
2. **Confirmation required**: Subscribers won't appear as "active" until they confirm email
3. **localStorage**: Subscription state won't persist in private/incognito mode

---

## Troubleshooting

### Form submits but no subscriber in Kit
1. Check browser console for errors
2. Check Network tab for failed requests to kit.com
3. Verify CSP allows Kit domains
4. Try on production domain (not preview)

### Success message doesn't appear
1. Check that Kit's ck.5.js loaded (Network tab)
2. Verify form has `data-sv-form` attribute
3. Check for JavaScript errors in console

### Forms don't disable after success
1. Check console for JavaScript errors
2. Verify MutationObserver is running
3. Check that success message contains "success" text

---

*Last updated: 2026-01-26*
