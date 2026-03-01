# Agent Definitions & Responsibilities

This directory contains the core agent definitions for the Pilgrim Prayers AI Team.

---

## The 8 Agents

| Agent | Role | Owns | Key Output |
|-------|------|------|-----------|
| **Copywriter** | Content creator | Blog posts, email copy, web copy | Weekly posts, campaigns |
| **Gatekeeper** | Quality reviewer | Brand fit, voice, boundaries | Approval stamps, feedback |
| **Paid Search** | Search marketer | Google Ads, keywords, targeting | Ad campaigns, performance reports |
| **Research** | Insight finder | Trends, keywords, audience signals | Research briefs, trend reports |
| **Storyteller** | Narrative architect | Story discovery, emotional arc | Story briefs, narrative angles |
| **Newsletter** | Email strategist | Email campaigns, list segments | Email campaigns, audience insights |
| **Visual** | Creative director | Colors, fonts, imagery, design | Brand guidelines, graphics |
| **UX Expert** | Conversion specialist | Landing pages, forms, mobile UX | Page audits, friction reports, tests |

---

## Agent Files

### Core Definitions
- `copywriter-agent.md` — Writes blog posts, emails, website content
- `gatekeeper-agent.md` — Reviews all content for quality before publishing
- `paid-search-agent.md` — Manages Google Ads strategy and campaigns
- `research-agent.md` — Discovers trends, keywords, and audience insights
- `storyteller-agent.md` — Identifies and crafts powerful narratives
- `newsletter-agent.md` — Strategizes and executes email campaigns
- `visual-agent.md` — Provides visual direction and brand assets
- `ux-expert-agent.md` — Optimizes landing pages, forms, and conversions

### Collaboration
- **`collaboration-ux-paidearch.md`** ← **START HERE if working with both UX and Paid Search**
  - Clear responsibility division
  - Weekly sync protocols (Monday, Wednesday, Friday)
  - When to escalate
  - Data sharing framework
  - Example scenarios

---

## How Agents Work Together

### Main Content Pipeline

```
Research Agent (finds trends)
    ↓
Storyteller (identifies stories)
    ↓
Copywriter (writes content)
    ↓
Gatekeeper (reviews)
    ↓
Newsletter (repurposes for email)
```

### Paid Search & UX Pipeline

```
Paid Search (drives traffic via ads)
    ↓ (to)
UX Expert (optimizes landing pages)
    ↓ (feedback)
Paid Search (refines targeting based on data)
```

**Weekly syncs:** Monday (UX brief) + Wednesday (PS brief) + Friday (joint review)

### All Content Agents + Visual

Visual Agent provides direction for every piece:
- Photography style
- Color palette
- Font choices
- Design system

---

## Key Collaboration Points

### UX Expert ↔ Paid Search (Daily)
- UX builds landing pages; Paid Search drives traffic to them
- See: `collaboration-ux-paidearch.md` (entire framework)
- **Weekly syncs:** Monday + Wednesday + Friday

### Content Pipeline (Weekly)
- Research → Storyteller → Copywriter → Gatekeeper → Newsletter
- Each agent reads the previous agent's output

### Visual Direction (Always)
- Visual provides palette, fonts, photography style
- All content agents incorporate this direction

---

## When to Use Each Agent

**Need a blog post?** → Copywriter Agent
**Need it reviewed?** → Gatekeeper Agent
**Need Google Ads strategy?** → Paid Search Agent
**Need content ideas?** → Research Agent
**Need a powerful story?** → Storyteller Agent
**Need an email campaign?** → Newsletter Agent
**Need visual direction?** → Visual Agent
**Need a landing page optimized?** → UX Expert Agent

---

## Required Reading for All Agents

Before any agent works on anything, they read:

**From C-core:**
- `C-core/project-brief.md` — What Pilgrim Prayers does
- `C-core/voice-dna.md` — How we sound
- `C-core/icp-profile.md` — Who we're serving (Margaret, 62, Texas)

**From M-memory:**
- `M-memory/learning-log.md` — What we've learned so far
- `M-memory/feedback.md` — How the audience reacts
- `M-memory/decisions.md` — Strategic choices made

---

## Agent Output Templates

Each agent has a skill file with standard output templates:

- **Copywriter:** `T-tools/skills/weekly-post-skill/` (blog posts, email copy)
- **Newsletter:** `T-tools/skills/newsletter-skill/` (email campaigns)
- **Paid Search:** `T-tools/skills/paid-search-skill/` (ad copy, campaigns, reports)
- **Research:** `T-tools/skills/research-skill/` (research briefs, trend reports)
- **UX Expert:** `T-tools/skills/ux-expert-skill/` (landing page audits, friction reports, A/B tests)

---

## Adding a New Agent

To add a new agent:

1. Create `[role]-agent.md` in this directory
2. Include these sections:
   - **Core Identity** — Who they are and what they do
   - **Required Reading** — Which files they read first
   - **Seven Duties** — Main responsibilities (weekly, bi-weekly, monthly tasks)
   - **Collaboration** — Who they work with, how often
   - **Output Formats** — What they deliver
   - **Success Metrics** — How you measure if they're working
3. Create output templates in `T-tools/skills/[role]-skill/`
4. Update this README
5. Add collaboration notes if they work with existing agents

---

## When Agents Disagree

If two agents propose different directions:

1. **Check the brand foundation** — `C-core/voice-dna.md` and `C-core/project-brief.md`
2. **Check the learning log** — `M-memory/learning-log.md`
3. **Check the decisions log** — `M-memory/decisions.md`
4. **If still unclear** → Escalate to project lead

The brand foundation and memory files are the source of truth.

---

## Accessing Agent Definitions

**From within Claude Code**, you can reference agent definitions:

```
Read the UX Expert Agent definition at: A-agents/ux-expert-agent.md
Read the collaboration framework at: A-agents/collaboration-ux-paidearch.md
```

---

## Team Overview

```
┌─────────────────────────────────────────────────────┐
│  Pilgrim Prayers AI Team                            │
├─────────────────────────────────────────────────────┤
│                                                     │
│  CONTENT PIPELINE                                   │
│  Research → Storyteller → Copywriter → Gatekeeper   │
│                              ↓                      │
│                          Newsletter                 │
│                              ↑                      │
│                          Visual Agent               │
│                                                     │
│  CONVERSION PIPELINE                                │
│  Paid Search (ads) → UX Expert (landing pages)      │
│  ↑ (data) ← ↓ (friction insights)                   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

Last updated: 2026-02-24

> © Tom Even | Pilgrim Prayers AI Agent Team
> For workshops and resources: [www.getagents.today](https://www.getagents.today)
> Newsletter: [www.agentsandme.com](https://www.agentsandme.com)
