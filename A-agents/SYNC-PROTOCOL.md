---
title: UX Expert & Paid Search Agent — Weekly Sync Protocol
description: Quick reference for the three weekly synchronization points between UX Expert and Paid Search agents
---

# Weekly Sync Protocol

**Quick reference for UX Expert ↔ Paid Search Agent weekly synchronization**

For full details, see: `collaboration-ux-paidearch.md`

---

## The Three Syncs

```
WEEK VIEW
├─ MONDAY: UX Brief (UX → PS)
├─ WEDNESDAY: PS Brief (PS → UX)
└─ FRIDAY: Joint Review (Both)
```

---

## MONDAY — UX Brief (9 AM)

**What:** UX Expert shares last week's friction & wins
**Format:** Email or Slack message + supporting docs
**Time to read:** 5 minutes

### UX Shares

```
MONDAY UX BRIEF — [Week of YYYY-MM-DD]

Top 3 Friction Points:
1. [Point] — Impact: [X% conversion drop]
   Hypothesis: [Why users get stuck]
   Fix: [In progress / tested / rolled out]

2. [Point] — Impact: [X%]
   Hypothesis: [Why]
   Fix: [What we're doing]

3. [Point] — Impact: [X%]
   Hypothesis: [Why]
   Fix: [What we're doing]

Last Week's A/B Test:
- Test: [Variable tested]
- Winner: [Winning variant]
- Confidence: [X%]
- Impact: [+X% conversion]
- Status: [Rolling out / archiving]

Funnel Health:
- Step 1→2: XX% (good)
- Step 3→4: XX% (dropping 10% from last week) ⚠️
- Biggest concern: [Step X] — hypothesis: [Why]

Alerts:
- Mobile conversion down 5% (investigating page speed)
- Form abandonment up 3% (testing reduced fields)
```

### Paid Search Responds

**If they see a problem:**
- "Form abandonment up 3% — this could be traffic quality. I'm checking which keywords drive forms."
- "Mobile conversion down 5% — our mobile traffic is 70%. Let's make mobile optimization #1 priority."

**By end of Monday:** Paid Search understands what's happening with the landing pages.

---

## WEDNESDAY — Paid Search Brief (2 PM)

**What:** Paid Search Agent shares traffic & performance data
**Format:** Email or Slack message + data exports
**Time to read:** 5 minutes

### Paid Search Shares

```
WEDNESDAY PAID SEARCH BRIEF — [Week of YYYY-MM-DD]

Traffic & Conversion by Landing Page:
- [Page Name]: 500 clicks → 25 conversions = 5% conversion ✓
- [Page Name]: 300 clicks → 9 conversions = 3% conversion ⚠️
- [Page Name]: 100 clicks → 4 conversions = 4% conversion

Quality Score Issues:
- [Campaign]: Avg QS 6 — Issue: landing page experience
  Action needed: Check page speed on [page name]

Emerging Keywords:
- "prayer for cancer healing" — [X searches/month] — high intent
  Recommendation: Create dedicated landing page variant?

Audience Insights:
- Mobile users searching for "prayer for healing" are converting better (6% vs 3% desktop)
- Implication: Mobile-first landing page for healing intent?

Traffic Quality:
- Overall CTR trending up 5% — good
- Conversion rate holding steady
- CPA down 3% — efficiency improving

Geo Performance:
- US: 5% conversion
- UK: 4% conversion
- Australia: 3% conversion
```

### UX Expert Responds

**If they see an opportunity:**
- "Emerging 'prayer for healing' keyword — I can create dedicated landing page variant by next Thursday if you want to test it."
- "Mobile converting 2x better — I'll make mobile-first design our priority next week."

**If they see a problem:**
- "Page getting 500 clicks but only 5% conversion — something's off. I'll review the page vs. your ad messaging."
- "Quality Score 6 on [page] — I'll check load time and mobile experience today."

**By end of Wednesday:** UX Expert understands traffic patterns and can prioritize fixes.

---

## FRIDAY — Joint Review (10 AM)

**What:** Both agents sync on performance, priorities, and next week
**Format:** 30-minute call or detailed async exchange
**Structure:** Follow the 4-step agenda below

### Step 1: Traffic & Conversion (10 min)

**PS shares:**
"This week we drove 2,000 clicks across all campaigns. Conversion rate held at 4.5%. Cost per prayer is $35. On track."

**UX responds:**
"Good week — no major changes from us. Page speed stayed solid. One A/B test hit significance (button text variant) — rolling out winner Monday."

**Or if there's a problem:**
"Conversion dropped to 3% this week. Two possibilities: (1) we changed hero image Tuesday, or (2) traffic quality shifted. I'm rolling back the image today. If it recovers, image was the issue. If not, traffic quality problem on your side?"

### Step 2: Friction Loop (10 min)

**UX brings data:** "Mobile form abandonment is high — users drop after second field"
**PS adds insight:** "Mobile is 70% of our traffic and converting 2x better than desktop. This matters."
**Decision:** "Let's create mobile-first 3-field form variant. Can you have it ready by Thursday?"

**Or:**

**PS brings data:** "Emerging keyword 'prayer for cancer healing' — 50+ searches/month, 15% conversion on generic page"
**UX responds:** "Generic page wasn't designed for healing intent. Let me create dedicated variant."
**Decision:** "Launch dedicated healing prayer landing page by Thursday; PS tests with new campaign"

### Step 3: Test Results & Rollout (5 min)

**UX shares:** "CTA button 'Place My Prayer' beat 'Submit Prayer' by 12%. Rolling out Monday."
**PS commits:** "I'll update all ad headlines to use 'Place' language to match. Setting expectations better = higher conversion."

### Step 4: Next Week's Priorities (5 min)

**Agree on top 3:**
1. "Reduce mobile form abandonment from 50% to <45%" — UX leads
2. "Create healing prayer landing page variant" — UX builds, PS tests
3. "Mobile-specific campaign structure" — PS leads with UX feedback

**Blockers?** "Do we have any blockers for next week?" No → ship it.

---

## Escalation Alerts (Ad-Hoc, Not Scheduled)

### UX Alert to Paid Search (Immediate)

**If conversion drops >10%:**
```
ALERT: Conversion dropped 15% on prayer submission page.
Cause: Rolled back new hero image (regression confirmed).
Action: I've reverted. Monitoring for recovery.
Watch for: If conversion doesn't recover, traffic quality issue on your side.
```

**If page breaks:**
```
ALERT: Prayer form page is throwing error on submit (SSL issue found).
Impact: 100% form failure since 2 PM.
Status: Fixing now, should be up in 30 minutes.
Consider: Pause keywords sending to this page until fixed.
```

**If mobile converts 2x+ desktop:**
```
ALERT: Mobile converting at 8%, desktop at 4%. Significant difference.
Insight: Mobile form is 3 fields; desktop version is 6.
Recommendation: Mobile-first landing page + mobile-only campaign?
Timeline: Can have mobile variant ready by Thursday if you want to test.
```

### Paid Search Alert to UX (Immediate)

**If traffic spikes but conversion flat:**
```
ALERT: Traffic up 40% this week, but conversion rate dropped from 5% to 3%.
Hypothesis: Driving wrong audience or page not scaling.
Question: Any issues on your side? Speed, design, messaging mismatch?
Data: All traffic is to [page name] — help me understand the drop.
```

**If Quality Score tanks:**
```
ALERT: Quality Score dropped from 7 to 5 on [page].
Diagnosis: "Landing page experience" is the issue.
Data: CTR is fine, ad relevance is fine.
Action needed: Page speed? Mobile UX? Content match with ad?
Can you review [page] against [these specific ad headlines]?
```

---

## Data You Should Have Before Each Sync

### UX Should Have (Before Monday)
- [ ] Microsoft Clarity heatmap data for past week
- [ ] GA4 funnel completion rates
- [ ] Mobile vs desktop breakdown
- [ ] Form field-by-field abandonment
- [ ] A/B test results (if any completed)
- [ ] Page load time (PageSpeed Insights)

### Paid Search Should Have (Before Wednesday)
- [ ] Google Ads campaign performance by page
- [ ] Conversion rate by landing page
- [ ] Quality Score breakdown
- [ ] Search terms report (new keywords)
- [ ] Cost per conversion (CPA) trending
- [ ] Geo and device performance

---

## Templates to Copy/Paste

### Monday UX Brief Template

```markdown
# UX Brief — Week of [DATE]

**Top 3 Friction Points:**
1. [Friction point] — Impact: [X%] — Fix: [In progress]
2. [Friction point] — Impact: [X%] — Fix: [In progress]
3. [Friction point] — Impact: [X%] — Fix: [In progress]

**A/B Test Results:**
- Test: [Variable]
- Winner: [Variant]
- Confidence: [X%]
- Status: [Rolling out]

**Funnel Alert:**
- Biggest drop: Step [X] → [X]% (was [X]% last week)
- Hypothesis: [Why users leaving]

**Alerts to PS:**
- [Alert if any]
- [Alert if any]
```

### Wednesday Paid Search Brief Template

```markdown
# Paid Search Brief — Week of [DATE]

**Traffic & Conversion by Page:**
| Page | Clicks | Conv. | Rate | Trend |
|------|--------|-------|------|-------|
| [Page] | XXX | XX | X% | ↑ / ↓ |

**Quality Score Issues:**
- [Campaign]: QS [X] — Issue: [landing page / CTR / ad relevance]

**Emerging Keywords:**
- "[Keyword]" — [X searches] — [intent tier] — Recommendation: [action]

**Audience Insight:**
- [Insight about user intent or geography]
```

### Friday Sync Checklist

```
FRIDAY SYNC CHECKLIST

☐ Traffic & conversion review (good/bad/why?)
☐ Friction review → performance analysis
☐ Test results & rollout decisions
☐ Top 3 priorities for next week
☐ Any blockers?

Decision: [Action item] — Owned by: [UX / PS] — Timeline: [By when]
Decision: [Action item] — Owned by: [UX / PS] — Timeline: [By when]
Decision: [Action item] — Owned by: [UX / PS] — Timeline: [By when]
```

---

## Common Scenarios

### "Landing page gets traffic but converts poorly"

**Monday:** UX notices low conversion on page
**Wednesday:** PS confirms: "Traffic going to [page] but converting at 2% (vs 5% average)"
**Friday:** Discussion:
- UX checks Clarity: "Hero image might not match what ad promises"
- PS checks ad copy: "Ad says 'prayer for healing' but page is generic prayer"
- Decision: Create dedicated healing prayer landing page; test it with new campaign

---

### "A/B test shows strong winner"

**Monday:** UX reports: "'Place My Prayer' button beats 'Submit Prayer' by 12%"
**Wednesday:** PS immediately updates ad headlines to use "Place" language
**Friday:** Review confirms: Consistency helps set expectations → conversion improves overall

---

### "Mobile converts 2x better than desktop"

**Monday:** UX alerts: "Mobile 8%, desktop 4% — mobile form is shorter and faster"
**Wednesday:** PS data confirms: "Mobile traffic is 70% of volume"
**Friday:** Decision: Create mobile-first landing page as default; desktop variant next
- UX: Build mobile variant by Thursday
- PS: Shift 60% budget to mobile campaigns starting next week

---

## One-Pager Reference

```
WEEKLY SYNC PROTOCOL

🔵 MONDAY (UX Brief)
   ├─ Share: Top 3 friction points + A/B results
   ├─ Alert: Any conversion issues
   └─ Ask: "Any traffic quality concerns?"

🟢 WEDNESDAY (PS Brief)
   ├─ Share: Traffic by page + performance trends
   ├─ Alert: Any quality score or traffic issues
   └─ Ask: "Should we create landing page for this keyword?"

🟡 FRIDAY (Joint Review)
   ├─ Review: Traffic, conversion, trends
   ├─ Decide: Top 3 priorities for next week
   ├─ Commit: Who owns what, by when
   └─ Check: Any blockers?

🔴 URGENT (Ad-hoc)
   ├─ >10% conversion drop → investigate immediately
   ├─ Page breaks → pause keywords to that page
   ├─ Traffic spikes but conversion flat → message/page mismatch?
   └─ Quality Score drops → page speed/content issue?
```

---

Last updated: 2026-02-24

For full collaboration framework: See `collaboration-ux-paidearch.md`

> © Tom Even | Weekly Sync Protocol for UX Expert & Paid Search
