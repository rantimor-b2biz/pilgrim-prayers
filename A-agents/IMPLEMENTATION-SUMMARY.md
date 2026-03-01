---
title: UX Expert & Paid Search Agent — Implementation Summary
description: What was created and how to use the new collaboration framework
---

# Implementation Summary

## What Was Created

### 1. **Collaboration Framework** (`collaboration-ux-paidearch.md`)

A comprehensive 1,500+ line document defining:

✅ **Clear Division of Responsibilities**
- UX Expert owns: Landing pages, forms, mobile UX, speed, trust signals, friction analysis, A/B testing
- Paid Search owns: Keywords, ad targeting, ad copy, campaign structure, performance analysis, budget

✅ **Weekly Sync Protocol**
- **Monday:** UX Brief (UX → PS) — What happened, friction points, test results
- **Wednesday:** PS Brief (PS → UX) — Traffic quality, conversion rates, emerging keywords
- **Friday:** Joint Review (Both) — 30-min alignment on priorities and decisions

✅ **Data Exchange Framework**
- What UX shares: Clarity data, funnel metrics, A/B results, mobile analysis
- What PS shares: Search terms, traffic quality, Quality Scores, geo performance

✅ **When to Escalate**
- Conversion drops >10% → immediate alert
- Page breaks → immediate pause
- Mobile converts 2x+ desktop → strategy shift
- Quality Score tanks → investigate page experience

✅ **Example Scenarios**
- Scenario 1: Conversion drops 15% — diagnose immediately
- Scenario 2: New keyword emerges — create dedicated landing page
- Scenario 3: Mobile converts better — mobile-first strategy
- Scenario 4: Low-converting page → intent mismatch → new LP needed

✅ **Success Metrics** (Both track)
- Conversion rate
- Cost per prayer (CPA)
- Page load time
- Mobile conversion rate
- Form abandonment
- Traffic quality
- Return visitors

---

### 2. **UX Expert Skill** (`T-tools/skills/ux-expert-skill/ux-expert-skill.md`)

Templates and output formats for UX Expert deliverables:

✅ **5 Output Templates:**

1. **Friction Analysis Report** (Weekly)
   - Top 3 friction points with hypotheses
   - Funnel health check
   - Device performance breakdown
   - Message alignment check with ads
   - Performance metrics trending

2. **A/B Test Results** (Per test)
   - Test setup and sample size
   - Results table with statistical significance
   - Winner and confidence level
   - Insights for Paid Search (message/audience implications)

3. **Mobile Audit Report** (Bi-weekly)
   - Mobile score vs desktop
   - Critical/high/medium priority issues
   - Touch target, text readability, form, navigation checks
   - Conversion metrics by device
   - Speed analysis and optimization opportunities

4. **Monthly UX Performance Summary**
   - Month-at-a-glance metrics
   - Top wins and friction points addressed
   - Performance by landing page
   - Collaboration insights with Paid Search
   - Next month's top 3 priorities

5. **Landing Page Audit Checklist** (Weekly per page)
   - Quick health check (above fold, form, trust)
   - Issues categorized by severity
   - Page-to-ad message alignment
   - Conversion data and status

**All templates include:**
- Data sources and metrics
- Clear formatting for quick scanning
- Recommended actions
- Output directory: `O-output/ux-expert/[YYYY-MM-DD]-[report-type].md`

---

### 3. **Sync Protocol Quick Reference** (`SYNC-PROTOCOL.md`)

A 400-line quick reference guide with:

✅ **The Three Weekly Syncs**
- Monday UX Brief (5 min read)
- Wednesday PS Brief (5 min read)
- Friday Joint Review (30 min call/async)

✅ **What Each Agent Shares**
- Templates to copy/paste for consistency
- Data each agent should have ready
- How other agent responds

✅ **Escalation Alerts**
- UX alerts (conversion drops, page breaks, mobile insights)
- PS alerts (traffic spikes, quality score issues)
- When to trigger immediate action

✅ **Common Scenarios**
- Low conversion on high-traffic page → diagnose mismatch
- A/B test winner → rollout across channels
- Mobile converts better → mobile-first strategy

✅ **One-Pager Reference**
- Color-coded weekly timeline
- What happens each day
- What triggers urgent escalation

---

### 4. **Updated Agent Definitions**

**UX Expert Agent** (`ux-expert-agent.md`) — Already existed, now enhanced with:
- Clear collaboration boundaries with Paid Search
- Explicit "when to loop each other in"
- Links to collaboration framework
- References to output templates

**Paid Search Agent** (`paid-search-agent.md`) — Already existed, now enhanced with:
- Clear collaboration boundaries with UX
- Data sources from UX (Clarity, funnel data)
- Quality Score troubleshooting with UX
- References to collaboration framework

---

### 5. **Updated Agent Directory** (`README.md`)

New comprehensive overview showing:
- All 8 agents and their roles
- Collaboration networks and pipelines
- Key collaboration points (UX ↔ PS is the main one)
- When to use each agent
- Where skills live
- How to add new agents
- When agents disagree (reference brand foundation)

---

## How to Use These Materials

### Getting Started

**If you're new to the system:**
1. Read `A-agents/README.md` (5 min) — Understand all agents
2. Read `A-agents/ux-expert-agent.md` (15 min) — UX Expert's job
3. Read `A-agents/paid-search-agent.md` (15 min) — Paid Search job
4. Read `A-agents/collaboration-ux-paidearch.md` (30 min) — How they work together

**If you're running the weekly syncs:**
1. Print `A-agents/SYNC-PROTOCOL.md` (quick reference)
2. Copy the templates each agent uses
3. Follow the 3-sync rhythm (Monday → Wednesday → Friday)

**If you're creating UX deliverables:**
1. Use templates from `T-tools/skills/ux-expert-skill/ux-expert-skill.md`
2. Save to `O-output/ux-expert/[date]-[report-type].md`
3. Share with Paid Search Agent in Monday brief

**If you're analyzing Paid Search performance:**
1. Use templates from `T-tools/skills/paid-search-skill/paid-search-skill.md`
2. Save to `B-brain/ads-performance/[date]-weekly-report.md`
3. Share with UX Expert Agent in Wednesday brief

---

## Key Responsibility Split

### UX Expert Owns:

| Responsibility | Frequency | Output |
|---|---|---|
| Landing page audits | Weekly | `[date]-friction-analysis.md` |
| Form optimization | Bi-weekly | `[date]-mobile-audit.md` |
| A/B testing | Ongoing | `[date]-ab-test-[name].md` |
| Mobile audits | Bi-weekly | `[date]-mobile-audit.md` |
| Monthly summary | Monthly | `[YYYY-MM]-ux-summary.md` |

### Paid Search Owns:

| Responsibility | Frequency | Output |
|---|---|---|
| Keyword strategy | Weekly | Search terms report |
| Ad copy creation | Weekly | `[date]-ad-copy.md` |
| Campaign performance | Weekly | `[date]-weekly-report.md` |
| Budget allocation | Monthly | Campaign structure review |
| Quality Score optimization | Weekly | `[date]-weekly-report.md` |

### Both Track:

| Metric | Owner | Cadence |
|---|---|---|
| **Conversion Rate** | Both | Weekly |
| **Cost Per Prayer (CPA)** | Paid Search | Weekly |
| **Page Load Time** | UX | Monthly |
| **Mobile Conversion** | Both | Weekly |
| **Return Visitors** | Both | Monthly |

---

## The Weekly Rhythm

```
MONDAY 9 AM
├─ UX Brief sent: friction points, A/B results, funnel alerts
└─ PS reads: notices form abandonment up → planning test

TUESDAY-WEDNESDAY
├─ UX works on: top friction point fixes, new A/B test
└─ PS works on: keyword expansion, ad copy optimization

WEDNESDAY 2 PM
├─ PS Brief sent: traffic quality, emerging keywords, conversion trends
└─ UX reads: new keyword identified → sketches dedicated landing page

THURSDAY-FRIDAY
├─ UX prepares: new landing page variant ready, A/B test ready
└─ PS prepares: new campaign structure, keyword allocation

FRIDAY 10 AM (30-min sync)
├─ Review: What worked, what didn't, priorities for next week
├─ Decide: Top 3 actions, who owns what, by when
└─ Commit: Handshake on next week's focus
```

---

## Integration Checklist

- [x] **Collaboration Framework Created** — `collaboration-ux-paidearch.md` (1,500+ lines, fully detailed)
- [x] **UX Skill Templates Created** — `ux-expert-skill.md` (5 templates, ready to use)
- [x] **Sync Protocol Documented** — `SYNC-PROTOCOL.md` (quick reference, copy/paste ready)
- [x] **Agent Definitions Updated** — Both agents reference collaboration framework
- [x] **Directory Updated** — `A-agents/README.md` shows all agents and collaboration networks
- [x] **Example Scenarios** — In collaboration framework (4 detailed scenarios)
- [x] **Success Metrics** — Defined for both agents

**Next Steps (Optional - not included here):**
- [ ] Implement Clarity integration (if not already done)
- [ ] Set up Google Sheets for sync notes
- [ ] Create Slack channel for agent-to-agent communication
- [ ] Schedule first Friday sync to review framework
- [ ] Train both agents on new templates

---

## File Locations

```
Pilgrim Prayers/
├── A-agents/
│   ├── ux-expert-agent.md ← UX Expert definition
│   ├── paid-search-agent.md ← Paid Search definition
│   ├── collaboration-ux-paidearch.md ← MAIN COLLABORATION FRAMEWORK ⭐
│   ├── SYNC-PROTOCOL.md ← Quick reference for weekly syncs ⭐
│   ├── IMPLEMENTATION-SUMMARY.md ← You are here
│   └── README.md ← Directory overview
│
└── T-tools/
    └── skills/
        ├── ux-expert-skill/ ← NEW
        │   └── ux-expert-skill.md ← UX output templates
        └── paid-search-skill/
            └── paid-search-skill.md ← PS output templates
```

---

## Quick Links for Daily Use

**For UX Expert Agent:**
- Definition: `A-agents/ux-expert-agent.md`
- Skill/Templates: `T-tools/skills/ux-expert-skill/ux-expert-skill.md`
- Collaboration: `A-agents/collaboration-ux-paidearch.md` (sections: "UX Expert Owns", "When to Loop Each Other In")

**For Paid Search Agent:**
- Definition: `A-agents/paid-search-agent.md`
- Skill/Templates: `T-tools/skills/paid-search-skill/paid-search-skill.md`
- Collaboration: `A-agents/collaboration-ux-paidearch.md` (sections: "Paid Search Owns", "When to Loop Each Other In")

**For Weekly Syncs:**
- Quick Ref: `A-agents/SYNC-PROTOCOL.md`
- Full Framework: `A-agents/collaboration-ux-paidearch.md` (sections: "Weekly Sync Protocol", "When to Loop Each Other In")

**For Understanding the Team:**
- Overview: `A-agents/README.md`

---

## How This Differs from Before

### Before
- Both agents existed independently
- General collaboration points mentioned in each agent definition
- No structured sync protocol
- No shared templates for handoff
- No escalation protocol for urgent issues

### After
- **Tight collaboration framework** with 3 structured syncs per week
- **Clear data exchange** — UX shares Clarity/funnel data; PS shares traffic/keyword data
- **Unified templates** — Both use standard formats for consistency
- **Escalation protocol** — Know when to alert immediately (>10% conversion drop, page breaks, etc.)
- **Scenario planning** — 4 detailed examples of how collaboration actually works
- **Success metrics** — Both track the same KPIs

---

## Questions?

**"What if UX finishes a landing page variant before Friday?"**
- Don't wait. UX can alert PS immediately: "New healing prayer landing page ready. Can you test it with new campaign?"

**"What if PS finds a brilliant new keyword mid-week?"**
- Don't wait. PS can ask UX immediately: "Emerging keyword 'prayer for grief' — 40+ searches/month. Do we have a landing page for this intent?"

**"What if something breaks?"**
- Escalate immediately. Conversion drops >10%? Conversion >20%? Page breaks? Alert each other on Slack/call right away.

**"What if we disagree on strategy?"**
- Refer to brand foundation (`C-core/voice-dna.md`, `C-core/project-brief.md`) and learning log (`M-memory/learning-log.md`). If still unclear, escalate to project lead.

---

## Success Looks Like

✅ Weekly syncs happen consistently (Monday, Wednesday, Friday)
✅ UX builds landing pages → PS drives traffic to them → conversion improves
✅ Friction insights from UX inform PS keyword/audience targeting
✅ Traffic quality insights from PS inform UX design priorities
✅ Both agents use standard templates → consistency, speed, clarity
✅ When conversion changes, both agents know why (data-driven decisions)
✅ New keywords → new landing pages ready within 48 hours
✅ Conversion rate trends up month-over-month
✅ Return visitor rate increases (sign of user satisfaction)

---

## Implementation Timeline

**Immediate (This Week):**
- [ ] Both agents read full collaboration framework
- [ ] Both agents review their new skill templates
- [ ] Schedule first Friday sync (30 minutes)

**Week 2:**
- [ ] Start Monday UX Brief rhythm
- [ ] Start Wednesday PS Brief rhythm
- [ ] Run first Friday joint review

**Week 3+:**
- [ ] Refine templates based on what works
- [ ] Feed learnings to `M-memory/learning-log.md`
- [ ] Quarterly deep dive to assess strategy

---

## Document Versions & Updates

**Created:** 2026-02-24
**Framework Version:** 1.0 (Initial Release)
**Review Schedule:** Monthly (adjust templates as needed)
**Update Owner:** Project Lead + Both Agents

---

> **© Tom Even**
> Pilgrim Prayers AI Team Implementation
> For workshops & resources: [www.getagents.today](https://www.getagents.today)
