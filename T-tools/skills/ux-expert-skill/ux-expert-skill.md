---
name: ux-expert-skill
description: Output templates for the UX Expert Agent. Includes landing page audits, friction reports, mobile assessments, A/B test documentation, and monthly performance summaries.
---

# UX Expert Skill

Standard output templates for every deliverable from the UX Expert Agent.

## When to Use

- Conducting weekly landing page audits
- Documenting friction points and user behavior insights
- Recording A/B test results and rollout decisions
- Assessing mobile experience and performance
- Delivering monthly performance summaries and strategic recommendations

---

## Template 1: Weekly Friction Analysis Report

**Save to:** `O-output/ux-expert/[YYYY-MM-DD]-friction-analysis.md`
**Created:** Weekly (Mondays)
**Shared with:** Paid Search Agent in Monday briefing

```markdown
# Friction Analysis Report

**Week of:** [YYYY-MM-DD]
**Data Source:** Microsoft Clarity + Google Analytics 4
**Next Sync:** [Friday date and time]

---

## Executive Summary

This week's biggest friction point: [1-sentence summary]

**Impact on conversion:** [Estimated % impact]
**Priority:** [High / Medium / Low]
**Recommendation:** [What to fix]

---

## Top 3 Friction Points

### 1. [Friction Point Title]

**Where:** [Page name / URL]
**What users do:** [Behavior from Clarity heatmap/recordings]
**Why it matters:** [Drop-off rate or abandonment metric]
**Hypothesis:** [Why users get stuck]
**Evidence:** [Screenshot or Clarity snippet]
**Fix:** [What we're doing about it]
**Timeline:** [In progress / Testing next week / Rolled out]

---

### 2. [Friction Point Title]

**Where:** [Page name / URL]
**What users do:** [Behavior from Clarity]
**Why it matters:** [Drop-off rate]
**Hypothesis:** [Why]
**Evidence:** [Data]
**Fix:** [Solution]
**Timeline:** [Timeline]

---

### 3. [Friction Point Title]

**Where:** [Page]
**What users do:** [Behavior]
**Why it matters:** [Impact]
**Hypothesis:** [Why]
**Evidence:** [Data]
**Fix:** [Solution]
**Timeline:** [Timeline]

---

## Funnel Health Check

### Conversion Funnel Summary

```
Step 1 (Landing): 100%
  ↓
Step 2 (Scroll hero): XX%
  ↓
Step 3 (Click CTA): XX%
  ↓
Step 4 (Fill form - name/email): XX%
  ↓
Step 5 (Fill form - prayer text): XX%
  ↓
Step 6 (Select location): XX%
  ↓
Step 7 (Payment): XX%
  ↓
Step 8 (Thank you): XX% (SUCCESS)
```

**Biggest drop-off:** Step [X] ([X]% drop)
**Most concerning:** [Which step / why]
**Session recording insight:** [What users say/do when they leave]

---

## Device Performance

| Metric | Mobile | Desktop | Difference |
|--------|--------|---------|-----------|
| **Bounce Rate** | XX% | XX% | [+/- X%] |
| **Conversion Rate** | XX% | XX% | [+/- X%] |
| **Avg Session Duration** | XXs | XXs | [+/- Xs] |
| **Form Completion Rate** | XX% | XX% | [+/- X%] |

**Insight:** [If mobile converts significantly different, note it]
**Action:** [If mobile needs dedicated strategy, flag here]

---

## Message Alignment Check (Collaboration with Paid Search)

| Landing Page | Ad Message Check | Status | Notes |
|--------------|------------------|--------|-------|
| [Page name] | Does page headline match ad? | ✓ / ✗ / Needs update | [Details] |
| [Page name] | Does emotional tone match ad? | ✓ / ✗ / Needs update | [Details] |
| [Page name] | Does CTA match ad promise? | ✓ / ✗ / Needs update | [Details] |

**Alert to Paid Search:** [If misalignment detected]

---

## Performance Metrics

| Metric | This Week | Last Week | Change |
|--------|-----------|-----------|--------|
| **Conversion Rate** | XX% | XX% | [+/- X%] |
| **Page Load Time** | X.Xs | X.Xs | [+/- Xs] |
| **Scroll Depth (avg)** | XX% | XX% | [+/- X%] |
| **Form Abandonment** | XX% | XX% | [+/- X%] |
| **Mobile Conversion** | XX% | XX% | [+/- X%] |

**Trend:** [Up / Down / Flat]
**Analysis:** [What changed; what stayed same]

---

## A/B Test Status

### In Progress

| Test | Variable | Variant A | Variant B | Started | Expected Winner |
|------|----------|-----------|-----------|---------|-----------------|
| [Test name] | [Element tested] | [A variant] | [B variant] | [Date] | [Prediction] |

---

### Completed This Week

| Test | Variable | Winner | Confidence | Impact | Decision |
|------|----------|--------|------------|--------|----------|
| [Test name] | [Element] | [Winning variant] | [Confidence %] | [+X% conversion] | [Roll out / Keep control] |

---

## Speed & Performance

**PageSpeed Insights Score:**
- Mobile: [XX/100]
- Desktop: [XX/100]

**Core Web Vitals:**
| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| **First Contentful Paint** | <1.5s | XXs | ✓ / ✗ |
| **Largest Contentful Paint** | <2.5s | XXs | ✓ / ✗ |
| **Cumulative Layout Shift** | <0.1 | X.XX | ✓ / ✗ |

**Action items:** [If any metrics are failing]

---

## Next Week's Focus

1. [Highest priority fix]
2. [Second priority]
3. [Third priority]

---

## Alert to Paid Search Agent

[If conversion dropped, traffic quality issue suspected, mobile strategy needed, or page-to-ad misalignment detected, note here]

---
```

---

## Template 2: A/B Test Results Document

**Save to:** `O-output/ux-expert/[YYYY-MM-DD]-ab-test-[test-name].md`
**Created:** When test reaches statistical significance
**Shared with:** Paid Search Agent in Monday briefing

```markdown
# A/B Test Results: [Test Name]

**Test Duration:** [Start date] → [End date]
**Duration:** [X days / X weeks]
**Test Element:** [What changed]
**Statistical Significance:** [X% confidence level]

---

## Test Setup

**Hypothesis:**
[What we thought would happen and why]

**Variant A (Control):**
[Description of original version]
[Screenshot or visual reference if applicable]

**Variant B (Test):**
[Description of new version]
[Screenshot or visual reference if applicable]

**Sample Size:**
- Variant A: [X visitors]
- Variant B: [X visitors]

---

## Results

| Metric | Variant A (Control) | Variant B (Test) | Difference |
|--------|-------------------|-----------------|-----------|
| **Clicks** | X | X | X |
| **Conversions** | X | X | X |
| **Conversion Rate** | XX% | XX% | [+/- X%] ⭐ |
| **Mobile Conversion** | XX% | XX% | [+/- X%] |
| **Desktop Conversion** | XX% | XX% | [+/- X%] |

---

## Analysis

**Winner:** [Variant A / Variant B / No significant difference]

**Confidence Level:** [Statistical significance %]

**Key Finding:** [What the data tells us about user behavior]

**Why this matters:** [How it impacts conversion funnel]

---

## Decision & Rollout

- [ ] **Roll out to 100%:** [Winning variant]
- [ ] **Continue testing:** [Need more data]
- [ ] **Archive both variants:** [Neither variant won; move on]

**Timeline:** [By what date this rolls out]

**Monitoring Plan:** [How we'll verify the win persists over time]

---

## Insights for Paid Search Agent

**Message Implication:** [If test winner changes messaging expectation]
- Example: "Users respond better to 'Place My Prayer' than 'Submit Prayer'" → Update ad copy language

**Audience Implication:** [If test reveals audience preference]
- Example: "Mobile users strongly prefer 3-field form; desktop users tolerate 6-field" → Mobile-specific landing page needed

**Next Test to Run:** [What hypothesis this validates for next test]

---

## Notes

[Any qualitative observations from session recordings or user feedback]

---
```

---

## Template 3: Mobile Audit Report

**Save to:** `O-output/ux-expert/[YYYY-MM-DD]-mobile-audit.md`
**Created:** Bi-weekly (Thursdays)
**Shared with:** Paid Search Agent in sync meetings if mobile strategy needs update

```markdown
# Mobile Audit Report

**Audit Date:** [YYYY-MM-DD]
**Pages Audited:** [List of pages]
**Testing Device(s):** [iPhone model, Android model]

---

## Mobile Performance Score

| Page | Mobile Score | Desktop Score | Gap | Priority |
|------|-------------|---------------|----|----------|
| [Page name] | XX/100 | XX/100 | [X points] | [High / Medium] |
| [Page name] | XX/100 | XX/100 | [X points] | [High / Medium] |

---

## Usability Checklist

### Critical (Mobile Breaks)

- [ ] **Touch targets** are at least 44x44px
  - [ ] All buttons are tappable
  - [ ] Form fields have adequate padding
  - **Status:** [✓ Pass / ✗ Fail]
  - **Fix:** [If failing]

- [ ] **Text is readable** (minimum 16px body text)
  - [ ] No horizontal scrolling
  - [ ] Headings are large enough
  - **Status:** [✓ Pass / ✗ Fail]
  - **Fix:** [If failing]

- [ ] **Forms work on mobile**
  - [ ] One input per line (no side-by-side on small screens)
  - [ ] Input fields expand to fill width
  - [ ] Mobile keyboard is visible
  - **Status:** [✓ Pass / ✗ Fail]
  - **Fix:** [If failing]

- [ ] **Images load properly**
  - [ ] Images are scaled to viewport
  - [ ] Images load within 2 seconds
  - [ ] No broken images
  - **Status:** [✓ Pass / ✗ Fail]
  - **Fix:** [If failing]

### High (Mobile Struggles)

- [ ] **Navigation is mobile-friendly**
  - [ ] Hamburger menu or clear nav structure
  - [ ] Menu items are tappable
  - **Status:** [✓ Pass / ✗ Fail]
  - **Fix:** [If failing]

- [ ] **Load time is acceptable** (<3s)
  - [ ] First Contentful Paint: < 1.5s
  - [ ] Largest Contentful Paint: < 2.5s
  - **Status:** [✓ Pass / ✗ Fail]
  - **Fix:** [If failing]

- [ ] **CTA is visible & clickable**
  - [ ] Button is above the fold (or clearly visible)
  - [ ] Button is at least 44x44px
  - **Status:** [✓ Pass / ✗ Fail]
  - **Fix:** [If failing]

---

## Conversion Metrics

| Page | Mobile CR | Desktop CR | Difference | Status |
|------|-----------|------------|-----------|--------|
| [Page] | XX% | XX% | [+/- X%] | [Monitor / Optimize / Critical] |

**Analysis:**
[If mobile converts significantly worse, note why]

---

## Speed Analysis

| Page | Mobile Load | Desktop Load | Target | Status |
|------|-------------|--------------|--------|--------|
| [Page] | X.Xs | X.Xs | <3s | [✓ / ✗] |

**Slowest Assets:**
1. [Asset name] — [Size] — [Load time]
2. [Asset name]
3. [Asset name]

**Optimization Opportunities:**
- [ ] Compress images (target: [X]KB)
- [ ] Minify CSS/JS
- [ ] Defer off-screen images
- [ ] Enable caching

---

## Session Insights

**Mobile User Behavior:** [From Clarity recordings]
- [Behavior observation]
- [Common path to conversion]
- [Common exit point]

**Pain Points:** [What users struggle with on mobile]
1. [Issue]
2. [Issue]
3. [Issue]

---

## Recommendations

### Immediate (This Week)
1. [Fix description]
2. [Fix description]

### High Priority (Next Week)
1. [Fix description]
2. [Fix description]

### Medium Priority (Within 2 Weeks)
1. [Fix description]

---

## Test Plan

**Next mobile test:** [What we'll A/B test]
**Timeline:** [When we'll run it]

---
```

---

## Template 4: Monthly UX Performance Summary

**Save to:** `O-output/ux-expert/[YYYY-MM]-ux-summary.md`
**Created:** Last business day of each month
**Shared with:** Paid Search Agent in monthly review

```markdown
# UX Performance Summary — [Month]

**Report Period:** [Month, Year]
**Prepared:** [Date]
**Key Data Source(s):** Microsoft Clarity, Google Analytics 4

---

## Month at a Glance

| Metric | This Month | Last Month | Change | Trend |
|--------|-----------|-----------|--------|-------|
| **Conversion Rate** | XX% | XX% | [+/- X%] | [↑ / ↓ / →] |
| **Mobile Conversion** | XX% | XX% | [+/- X%] | [↑ / ↓ / →] |
| **Page Load Time** | X.Xs | X.Xs | [+/- Xs] | [↑ / ↓ / →] |
| **Form Abandonment** | XX% | XX% | [+/- X%] | [↑ / ↓ / →] |
| **Scroll Depth** | XX% | XX% | [+/- X%] | [↑ / ↓ / →] |
| **Return Visitors** | XX% | XX% | [+/- X%] | [↑ / ↓ / →] |

**Overall Assessment:** [Green / Yellow / Red]
**Headline:** [1-sentence summary of month]

---

## Top Wins This Month

1. **[Test Winner or Friction Fix]**
   - Impact: [+X% conversion]
   - What changed: [Brief description]
   - Why it worked: [Insight]

2. **[Test Winner or Friction Fix]**
   - Impact: [+X% conversion]
   - What changed: [Brief description]
   - Why it worked: [Insight]

3. **[Test Winner or Friction Fix]**
   - Impact: [+X% conversion]
   - What changed: [Brief description]
   - Why it worked: [Insight]

---

## Friction Points Addressed

| Friction | Status | Impact | Next Step |
|----------|--------|--------|-----------|
| [Friction point] | Fixed / In Progress / Identified | [+/- X%] | [Next action] |
| [Friction point] | Fixed / In Progress / Identified | [+/- X%] | [Next action] |

---

## A/B Tests Completed

| Test | Winner | Confidence | Impact | Rollout |
|------|--------|------------|--------|---------|
| [Test name] | [Variant] | XX% | [+X%] | [Rolled out / In progress] |
| [Test name] | [Variant] | XX% | [+X%] | [Rolled out / In progress] |

---

## Mobile Strategy Update

**Mobile Traffic:** XX% of total
**Mobile Conversion:** XX% (vs XX% desktop)
**Status:** [On track / Needs attention / Critical]

**This Month:**
- [Mobile action completed]
- [Mobile action in progress]

**Next Month:**
- [Mobile priority #1]
- [Mobile priority #2]

---

## Performance by Landing Page

| Page | Sessions | Bounce % | Conv. Rate | Trend | Priority |
|------|----------|----------|-----------|-------|----------|
| [Page] | XXX | XX% | XX% | [↑ / ↓] | [High / Medium / Low] |
| [Page] | XXX | XX% | XX% | [↑ / ↓] | [High / Medium / Low] |

**Biggest opportunity:** [Page with most growth potential]
**Immediate attention needed:** [Page with biggest decline]

---

## Collaboration with Paid Search

**Insights shared with Paid Search Agent:**
1. [Insight from this month]
2. [Insight from this month]
3. [Insight from this month]

**Feedback received from Paid Search Agent:**
1. [Feedback / learning]
2. [Feedback / learning]

**Joint wins this month:**
- [Collaboration outcome]

---

## Biggest Learning This Month

**Insight:** [What we learned about users, behavior, or conversion]

**Why it matters:** [Impact on strategy]

**Implication:** [What changes as a result]

*[This goes into M-memory/learning-log.md]*

---

## Next Month's Focus (Top 3)

1. **[Priority #1]**
   - Current state: [Metric]
   - Target: [Goal]
   - Approach: [How we'll improve]

2. **[Priority #2]**
   - Current state: [Metric]
   - Target: [Goal]
   - Approach: [How we'll improve]

3. **[Priority #3]**
   - Current state: [Metric]
   - Target: [Goal]
   - Approach: [How we'll improve]

---

## Strategic Recommendations

**For UX Team:**
[Recommendations for next month's design/UX work]

**For Paid Search Team:**
[Recommendations for targeting, landing page selection, or message alignment]

**For Product:**
[Any structural/feature recommendations if applicable]

---

## Metrics Dashboard

**Conversion Funnel:**
```
Landing Page Visit: 100%
Scroll Hero: XX%
Click CTA: XX%
Enter Name/Email: XX%
Write Prayer: XX%
Select Location: XX%
Complete Payment: XX%
Thank You Page: XX% ✓
```

**Device Breakdown:**
- Mobile: XX% (conversion XX%)
- Desktop: XX% (conversion XX%)
- Tablet: XX% (conversion XX%)

**Traffic Source Conversion:**
- Paid Search: XX% conversion
- Organic: XX% conversion
- Direct: XX% conversion

---

## Notes & Context

[Any other relevant updates, blockers, or context]

---
```

---

## Template 5: Landing Page Audit Checklist

**Save to:** `O-output/ux-expert/[YYYY-MM-DD]-lp-audit-[page-name].md`
**Created:** Weekly (Mondays) for each active landing page
**Shared with:** Paid Search Agent if issues are found

```markdown
# Landing Page Audit: [Page Name]

**URL:** [Full URL]
**Audit Date:** [YYYY-MM-DD]
**Auditor:** UX Expert Agent
**Status:** ✓ Healthy / ⚠️ Needs Review / ✗ Critical Issues

---

## Quick Health Check

### Above the Fold (First 3 Seconds)

- [ ] **Headline is clear**
  - Does visitor understand what we do? YES / NO
  - Matches ad headline? YES / NO / PARTIAL

- [ ] **Hero image is compelling**
  - Loads in <1s? YES / NO
  - Is it relevant to the page? YES / NO
  - Does it evoke trust? YES / NO

- [ ] **CTA is visible**
  - Button is visible without scrolling? YES / NO
  - Is it clear what clicking does? YES / NO

- [ ] **Trust signal visible**
  - Testimonial, number, badge, or proof? YES / NO

---

### Form Fields

- [ ] **Required fields only**
  - Count: [Number of fields]
  - Are all necessary? YES / NO / Some optional

- [ ] **Mobile-friendly inputs**
  - Proper input types (email, tel, etc.)? YES / NO
  - Touch targets 44px+? YES / NO
  - One per line on mobile? YES / NO

- [ ] **Microcopy is warm**
  - Placeholder text? [Yes / No]
  - Helper text? [Yes / No]
  - Tone: [Warm / Neutral / Cold]

---

### Trust Elements

| Element | Present | Quality | Notes |
|---------|---------|---------|-------|
| Testimonials | ✓ / ✗ | Good / Fair / Poor | [If issue] |
| Numbers/Stats | ✓ / ✗ | Good / Fair / Poor | [If issue] |
| Team photos | ✓ / ✗ | Good / Fair / Poor | [If issue] |
| Security badges | ✓ / ✗ | Good / Fair / Poor | [If issue] |
| Privacy statement | ✓ / ✗ | Good / Fair / Poor | [If issue] |

---

### Performance

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Page Load | <3s | XXs | ✓ / ✗ |
| FCP | <1.5s | XXs | ✓ / ✗ |
| LCP | <2.5s | XXs | ✓ / ✗ |
| CLS | <0.1 | X.XX | ✓ / ✗ |

---

## Issues Found

### Critical (Fix This Week)

- [ ] [Issue]: [Description and impact]
  - Fix: [Solution]
  - Timeline: [ASAP]

### High Priority (Fix This Week)

- [ ] [Issue]: [Description]
  - Fix: [Solution]
  - Timeline: [By end of week]

### Medium Priority (Plan for Next Week)

- [ ] [Issue]: [Description]
  - Fix: [Solution]
  - Timeline: [Next week]

### Low Priority (Consider)

- [ ] [Issue]: [Description]
  - Fix: [Solution]
  - Timeline: [When we get to it]

---

## Page-to-Ad Message Alignment

**Ad Message:** [What the ad says]
**Page Headline:** [What the page says]
**Match Level:** ✓ Perfect / ⚠️ Close / ✗ Misaligned

**If misaligned:**
[Recommendation: Update page headline OR update ad copy]

---

## Conversion Data

| Metric | Value | Status |
|--------|-------|--------|
| Sessions | XXX | — |
| Bounce Rate | XX% | [High / Normal / Low] |
| Conversion Rate | XX% | [High / Normal / Low] |
| Form Completion | XX% | [High / Normal / Low] |

---

## Next Steps

1. [Action]
2. [Action]
3. [Action]

---
```

---

## When & How to Use These Templates

| Deliverable | Frequency | When | Shared With |
|-------------|-----------|------|------------|
| Friction Analysis | Weekly | Mondays | Paid Search Agent |
| A/B Test Results | Per test | When complete | Paid Search Agent |
| Mobile Audit | Bi-weekly | Thursdays | Paid Search Agent (if action needed) |
| Monthly Summary | Monthly | Month-end | Paid Search Agent + Project Lead |
| Landing Page Audit | Weekly | Mondays | Paid Search Agent (if issues) |

---

## Output Directory Structure

All UX deliverables go to:
```
O-output/ux-expert/
├── [YYYY-MM-DD]-friction-analysis.md
├── [YYYY-MM-DD]-ab-test-[test-name].md
├── [YYYY-MM-DD]-mobile-audit.md
├── [YYYY-MM-DD]-lp-audit-[page-name].md
├── [YYYY-MM]-ux-summary.md
└── README.md (index of all reports)
```

---

## Quality Checklist

Before publishing any UX report:

- [ ] Report is based on actual data (Clarity, GA4, PageSpeed Insights)
- [ ] Friction points have evidence (heatmaps, session recordings, metrics)
- [ ] Recommendations are specific and actionable
- [ ] Mobile data is separate from desktop (they tell different stories)
- [ ] Paid Search Agent can understand insights in 5 minutes
- [ ] Next steps are clear and have timelines
- [ ] Document is well-formatted and easy to scan

---

Last updated: 2026-02-24

> © Tom Even | UX Expert Skill
> For workshops and resources: [www.getagents.today](https://www.getagents.today)
