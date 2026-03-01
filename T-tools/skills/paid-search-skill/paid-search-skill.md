---
name: paid-search-skill
description: Output templates for the Paid Search Agent. Includes ad copy briefs, campaign structure documents, weekly performance reports, keyword maps, and monthly strategy reviews.
---

# Paid Search Skill

Standard output templates for every deliverable from the Paid Search Agent.

## When to Use

- Writing new search ad copy or updating existing variants
- Documenting campaign structure changes
- Delivering weekly performance analysis
- Maintaining the keyword map
- Creating monthly strategy reviews

---

## Template 1: Ad Copy Brief

**Save to:** `O-output/ads/search/[YYYY-MM-DD]-ad-copy.md`
**Created:** Weekly or as needed (after each approved blog post)

```markdown
# Ad Copy Brief: [Campaign / Theme]

**Date:** [YYYY-MM-DD]
**Inspired by:** [Blog post title or Research Agent insight]
**Campaign:** [Which campaign this feeds]
**Status:** Draft / Gatekeeper Approved / Live

---

## Headlines (30 characters max each)

| # | Headline | Chars | Pin Position | Notes |
|---|----------|-------|-------------|-------|
| 1 | | | H1 (optional) | |
| 2 | | | H2 (optional) | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |
| 11 | | | | |
| 12 | | | | |
| 13 | | | | |
| 14 | | | | |
| 15 | | | | |

**Headline categories covered:**
- [ ] Brand message (who we are)
- [ ] Benefit (what the user gets)
- [ ] Place (Jerusalem, specific site)
- [ ] Emotional (how it feels)
- [ ] CTA (gentle invitation)

---

## Descriptions (90 characters max each)

| # | Description | Chars | Pin Position | Notes |
|---|-------------|-------|-------------|-------|
| 1 | | | D1 (optional) | |
| 2 | | | D2 (optional) | |
| 3 | | | | |
| 4 | | | | |

---

## Ad Extensions

**Sitelinks:**
| Sitelink Text | Final URL | Description Line 1 | Description Line 2 |
|--------------|-----------|--------------------|--------------------|
| | | | |

**Callouts:**
| Callout Text (25 chars max) |
|-----------------------------|
| |

**Structured Snippets:**
| Header | Values |
|--------|--------|
| | |

---

## A/B Test Plan

| Test | Variant A | Variant B | Hypothesis |
|------|-----------|-----------|------------|
| | | | |

---

## Paid Search Agent Notes

- **Why this angle:** [Connection to blog post, trend, or audience insight]
- **Target ad group:** [Which ad group]
- **Expected performance:** [Any predictions based on past data]
- **Voice check:** [How this aligns with voice-dna.md]
```

---

## Template 2: Campaign Structure Document

**Save to:** `B-brain/ads-performance/campaign-structure.md`
**Updated:** Monthly or when restructuring

```markdown
# Campaign Structure: Pilgrim Prayers Google Ads

**Last updated:** [YYYY-MM-DD]
**Account ID:** [Google Ads account ID]

---

## Account Overview

| Campaign | Type | Budget/Day | Bid Strategy | Status |
|----------|------|-----------|-------------|--------|
| | | | | |

---

## Campaign: [Name]

**Objective:** [What this campaign aims to achieve]
**Geo-targeting:** [Countries / regions]
**Schedule:** [Days / hours]
**Bid strategy:** [Strategy + target]

### Ad Group: [Name]

**Keywords:**
| Keyword | Match Type | Status | Avg CPC | Quality Score |
|---------|-----------|--------|---------|---------------|
| | | | | |

**Negative Keywords:**
| Keyword | Level (Campaign / Ad Group) |
|---------|-----------------------------|
| | |

**Active Ads:**
| Ad ID | Type | Headlines | Descriptions | Status |
|-------|------|-----------|-------------|--------|
| | RSA | [H1, H2, ...] | [D1, D2, ...] | |

---

## Audience Lists

| Audience Name | Source | Window | Size (est.) | Used In |
|--------------|--------|--------|-------------|---------|
| | | | | |

---

## Notes

- [Strategic decisions and their rationale]
```

---

## Template 3: Weekly Performance Report

**Save to:** `B-brain/ads-performance/[YYYY-MM-DD]-weekly-report.md`
**Created:** Every Friday

```markdown
# Weekly Performance Report: [Date Range]

**Reporting period:** [Mon DD] - [Sun DD], [YYYY]
**Prepared by:** Paid Search Agent

---

## Summary

| Metric | This Week | Last Week | Change | Notes |
|--------|-----------|-----------|--------|-------|
| Spend | | | | |
| Clicks | | | | |
| Impressions | | | | |
| CTR | | | | |
| Avg CPC | | | | |
| Conversions | | | | |
| CPA | | | | |
| Conversion Rate | | | | |
| Impression Share | | | | |

---

## Campaign Breakdown

| Campaign | Spend | Clicks | Conv | CPA | CTR | QS Avg | Action |
|----------|-------|--------|------|-----|-----|--------|--------|
| | | | | | | | |

---

## Top Performing

**Best ad variant this week:**
| Headline combo | Description | CTR | Conv Rate | Why it works |
|---------------|-------------|-----|-----------|-------------|
| | | | | |

**Best keyword this week:**
| Keyword | Clicks | Conv | CPA | Campaign |
|---------|--------|------|-----|----------|
| | | | | |

---

## Needs Attention

**Underperforming campaigns:**
| Campaign | Issue | Recommended Action |
|----------|-------|--------------------|
| | | |

**Wasted spend (irrelevant search terms):**
| Search Term | Clicks | Spend | Action |
|------------|--------|-------|--------|
| | | | Add as negative |

---

## Search Terms Worth Adding

| Search Term | Current Impressions | Recommended Match Type | Target Campaign |
|------------|--------------------|-----------------------|----------------|
| | | | |

---

## Optimization Actions Taken

- [ ] [Action 1]
- [ ] [Action 2]

## Optimization Actions Recommended (For Ran)

- [ ] [Action 1 -- requires Google Ads UI]
- [ ] [Action 2 -- requires Google Ads UI]

---

## GA4 Insights

| Metric | Paid Traffic | Organic Traffic | Notes |
|--------|-------------|----------------|-------|
| Bounce Rate | | | |
| Avg Session Duration | | | |
| Pages/Session | | | |
| Conversion Rate | | | |

---

## GSC Insights

**Organic queries overlapping with paid:**
| Query | Organic Clicks | Organic CTR | Paid Active? | Recommendation |
|-------|---------------|-------------|-------------|----------------|
| | | | | |

---

## M-memory Updates

**What to log in feedback.md:**
- [Key learning from this week]

**What to log in learning-log.md:**
- [Pattern discovered]

---

## Next Week Focus

1. [Priority 1]
2. [Priority 2]
3. [Priority 3]
```

---

## Template 4: Keyword Map

**Save to:** `B-brain/ads-performance/keyword-map.md`
**Updated:** Weekly (after search terms review)

```markdown
# Keyword Map: Pilgrim Prayers

**Last updated:** [YYYY-MM-DD]

---

## Tier 1: Direct Intent

| Keyword | Match Type | Campaign | Ad Group | Status | Avg CPC | QS | Notes |
|---------|-----------|----------|----------|--------|---------|-----|-------|
| | | | | | | | |

---

## Tier 2: Faith-Seeking

| Keyword | Match Type | Campaign | Ad Group | Status | Avg CPC | QS | Notes |
|---------|-----------|----------|----------|--------|---------|-----|-------|
| | | | | | | | |

---

## Tier 3: Gift / Occasion

| Keyword | Match Type | Campaign | Ad Group | Status | Avg CPC | QS | Notes |
|---------|-----------|----------|----------|--------|---------|-----|-------|
| | | | | | | | |

---

## Tier 4: Site-Specific / Branded

| Keyword | Match Type | Campaign | Ad Group | Status | Avg CPC | QS | Notes |
|---------|-----------|----------|----------|--------|---------|-----|-------|
| | | | | | | | |

---

## Negative Keywords (Account Level)

| Keyword | Date Added | Reason |
|---------|-----------|--------|
| | | |

---

## Keyword Pipeline (To Test)

| Keyword Idea | Source | Tier | Priority | Notes |
|-------------|--------|------|----------|-------|
| | Blog post / Research / Search terms | | | |

---

## Notes

- [Strategic decisions about keyword selection]
```

---

## Template 5: Monthly Strategy Review

**Save to:** `B-brain/ads-performance/[YYYY-MM]-monthly-review.md`
**Created:** First week of each month

```markdown
# Monthly Strategy Review: [Month Year]

**Reporting period:** [Month YYYY]
**Prepared by:** Paid Search Agent

---

## Executive Summary

[2-3 sentences: What happened, what worked, what needs to change]

---

## Performance Overview

| Metric | This Month | Last Month | Change | Target | Status |
|--------|-----------|-----------|--------|--------|--------|
| Total Spend | | | | | |
| Prayer Submissions | | | | | |
| Cost per Submission | | | | | |
| Total Clicks | | | | | |
| Avg CTR | | | | | |
| Impression Share | | | | | |

---

## Budget Analysis

| Campaign | Spend | % of Budget | Conversions | CPA | ROI Assessment |
|----------|-------|-------------|-------------|-----|----------------|
| | | | | | |

**Budget reallocation recommendation:**
| From | To | Amount | Rationale |
|------|----|--------|-----------|
| | | | |

---

## What Worked

| Winning Element | Evidence | Action |
|----------------|----------|--------|
| | | Scale / Expand |

---

## What Didn't Work

| Underperformer | Evidence | Action |
|---------------|----------|--------|
| | | Fix / Pause / Test |

---

## Keyword Performance

**Top 10 keywords by conversions:**
| Keyword | Clicks | Conv | CPA | Trend |
|---------|--------|------|-----|-------|
| | | | | |

**New keywords added this month:** [count]
**Keywords paused this month:** [count]
**Negative keywords added:** [count]

---

## Seasonal Planning (Next Month)

| Upcoming Date/Season | Impact on Ads | Budget Action | Content Connection |
|---------------------|---------------|---------------|-------------------|
| | | | |

---

## Research Agent Cross-Reference

**Trending topics from Research Agent that created keyword opportunities:**
| Trend | Keywords Added | Performance So Far |
|-------|--------------|-------------------|
| | | |

---

## Recommendations

### Must Do (This Week)
1. [Action]

### Should Do (This Month)
1. [Action]

### Could Do (Next Month)
1. [Action]

---

## M-memory Updates

**Update feedback.md with:**
- [What converted best and why]

**Update learning-log.md with:**
- [Patterns and lessons]
```

---

## Integration with ABC-TOM

When using this skill:

1. **Read from C-core:** Voice DNA before writing any ad copy
2. **Read from B-brain:** Content calendar for seasonal alignment, keyword map for context
3. **Read from O-output:** Latest final-post.md for ad hooks, Research Agent's brief for trends
4. **Check M-memory:** Learning log for past patterns, feedback for audience signals
5. **Output to B-brain:** Performance reports, keyword maps, strategy reviews
6. **Output to O-output:** Ad copy briefs in `O-output/ads/search/`
7. **Update M-memory:** Winning messages and conversion patterns after each weekly report

---

*Every ad should feel like an invitation, not a billboard.*

---

> **Framework: ABC-TOM** by Tom Even
> Workshops & future dates: [www.getagents.today](https://www.getagents.today)
> Newsletter: [www.agentsandme.com](https://www.agentsandme.com)
