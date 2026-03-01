# O-output Folder Structure — Visual Guide

## 🎯 Overview

The **O-output** folder is organized into 6 main sections, each with a specific purpose in the content lifecycle.

```
O-output/
├─ 00-index/          Navigation & structure docs
├─ 01-briefs/         Content planning before production
├─ 02-deliverables/   Agent work-in-progress
├─ 03-published/      Final published content
├─ 04-campaigns/      Marketing campaigns (email, social, etc.)
├─ 05-archive/        Old work and legacy content
└─ 06-ads/            Paid search and advertising
```

---

## 📋 Detailed View

### 00-index (Navigation)
```
00-index/
└─ INDEX.md .................... Master navigation (this file)
└─ STRUCTURE.md ................ Visual structure guide (this file)
```
**Purpose:** Help you navigate the entire O-output folder

---

### 01-briefs (Planning)
```
01-briefs/
└─ week-8/
   ├─ 2026-02-24-week8-garden-tomb-brief.md ...... MAIN BRIEF ⭐
   ├─ 2026-02-24-research-agent-brief.md
   ├─ 2026-02-24-storyteller-agent-brief.md
   ├─ 2026-02-24-WEEK8-CONTENT-WORKFLOW.md
   ├─ WEEK8-QUICK-START.md
   └─ README-WEEK8.md
```
**Purpose:** Content planning documents before agents start work
**Lifecycle:** Created before production, stays as reference

---

### 02-deliverables (Work-in-Progress)
```
02-deliverables/
└─ week-8-deliverables/
   ├─ research/
   │  └─ 2026-02-24-garden-tomb-research.md (when ready)
   ├─ storyteller/
   │  └─ 2026-02-24-garden-tomb-story.md (when ready)
   ├─ copywriter/
   │  └─ 2026-02-24-garden-tomb-post.md (when ready)
   ├─ gatekeeper/
   │  └─ 2026-02-24-garden-tomb-review.md (when ready)
   ├─ visual/
   │  └─ 2026-02-24-garden-tomb-visual-direction.md (when ready)
   └─ newsletter/
      └─ 2026-02-24-garden-tomb-email.md (when ready)
```
**Purpose:** Agent deliverables as they're being created
**Lifecycle:** Created during production, moved to 03-published when final

---

### 03-published (Final Content)
```
03-published/
└─ blog-posts/
   └─ 2026-02/
      └─ week-8/
         └─ garden-tomb-quiet-morning.md (final published post)
```
**Purpose:** Final published blog posts
**Lifecycle:** Created after Gatekeeper approval, permanent archive

---

### 04-campaigns (Marketing)
```
04-campaigns/
└─ email/
   └─ 2026-02/
      └─ week-8-garden-tomb.md (final email version)
```
**Purpose:** Email campaigns, social content, promotional materials
**Lifecycle:** Created after blog publishing, permanent archive

---

### 05-archive (Old Work)
```
05-archive/
└─ old-posts/
   ├─ 08-weekly-post-garden-tomb-quiet-morning/
   ├─ 12.2-weekly-post-galilee-living-land/
   ├─ 13-weekly-post-mount-of-olives/
   └─ [other past work]
```
**Purpose:** Previous posts and archived projects
**Lifecycle:** Permanent reference, don't delete

---

### 06-ads (Advertising)
```
06-ads/
├─ search-campaigns/
│  └─ [campaign folders]
└─ ads/ (legacy)
```
**Purpose:** Paid search campaigns, ad copy, performance data
**Lifecycle:** Permanent archive

---

## 🔄 Content Flow Diagram

### From Brief to Published

```
1. PLANNING
   01-briefs/week-8/
   ├─ Main brief created
   ├─ Agent briefs created
   ├─ Workflow outlined
   └─ Timeline established
          ↓

2. PRODUCTION
   02-deliverables/week-8-deliverables/
   ├─ Research Agent delivers
   ├─ Storyteller Agent delivers
   ├─ Copywriter Agent delivers
   ├─ Visual Agent delivers
   ├─ Gatekeeper Agent reviews
   └─ Newsletter Agent delivers
          ↓

3. PUBLISHING
   03-published/blog-posts/2026-02/week-8/
   └─ Final post published
          ↓

4. CAMPAIGNS
   04-campaigns/email/2026-02/
   └─ Email campaign sent
          ↓

5. ARCHIVE
   Everything stays in 03-published/ and 04-campaigns/
   permanently for future reference
```

---

## 📍 Where Things Live

### **I'm working on Week 8 content**
- Read brief: `01-briefs/week-8/2026-02-24-week8-garden-tomb-brief.md`
- Save research: `02-deliverables/week-8-deliverables/research/`
- Save story: `02-deliverables/week-8-deliverables/storyteller/`
- Save post: `02-deliverables/week-8-deliverables/copywriter/`
- Gatekeeper review: `02-deliverables/week-8-deliverables/gatekeeper/`
- Final post: `03-published/blog-posts/2026-02/week-8/`
- Email: `04-campaigns/email/2026-02/`

### **I need to review past posts**
- Go to: `05-archive/old-posts/` or `03-published/blog-posts/`

### **I'm launching an ad campaign**
- Save to: `06-ads/search-campaigns/[campaign-name]/`

### **I'm creating a new week**
1. Create: `01-briefs/week-[X]/`
2. Create: `02-deliverables/week-[X]-deliverables/`
3. Work through the flow

---

## 📝 Naming Convention

All files use this format:

```
[DATE]-[type]-[subject].md

EXAMPLES:
2026-02-24-week8-garden-tomb-brief.md
2026-02-24-garden-tomb-research.md
2026-02-24-garden-tomb-post.md
2026-02-24-garden-tomb-email.md
```

**Pattern breakdown:**
- `[DATE]` — YYYY-MM-DD (file creation date)
- `[type]` — week8, garden-tomb, email, etc.
- `[subject]` — What it is (brief, research, post, email)

---

## 🎯 Quick Tips

**Tip 1:** Always start in `01-briefs/week-[X]/` for planning
```
→ Read the brief
→ Understand the workflow
→ Know the deliverable structure
```

**Tip 2:** Save agent work in `02-deliverables/week-[X]-deliverables/[agent]/`
```
→ Research saves here
→ Storyteller saves here
→ Copywriter saves here
→ Etc.
```

**Tip 3:** Move to `03-published/` only after Gatekeeper approval
```
→ Blog posts go to: 03-published/blog-posts/2026-02/week-8/
→ Keep the folder structure consistent
```

**Tip 4:** Email version goes to `04-campaigns/email/`
```
→ After blog is published
→ Create email campaign version
→ Save in dated folder
```

**Tip 5:** Everything in `03-published/` and `04-campaigns/` is permanent
```
→ Don't delete old posts
→ Keep campaigns for reference
→ This is your archive
```

---

## 🔍 Finding Things Quickly

### **Search pattern:**
- By week: `week-[number]`
- By date: `2026-02-24`
- By type: `-research`, `-post`, `-email`
- By site: `-garden-tomb`, `-mount-of-olives`

### **Examples:**
```
Find all Week 8 files:
  → Search: week-8

Find all garden tomb content:
  → Search: garden-tomb

Find all deliverables:
  → Look in: 02-deliverables/

Find old posts:
  → Look in: 05-archive/old-posts/
```

---

## 📊 File Statistics

**Current state (2026-02-24):**
- Briefs created: Week 8 ✅
- Deliverables awaiting: 6 agents
- Published posts: Multiple (in 03-published/)
- Email campaigns: Multiple (in 04-campaigns/)
- Ad campaigns: Multiple (in 06-ads/)

---

## ✅ Structure Checklist

When creating new content, ensure:

- [ ] Briefs go in `01-briefs/week-[X]/`
- [ ] Agent work goes in `02-deliverables/week-[X]-deliverables/[agent]/`
- [ ] Published posts go in `03-published/blog-posts/YYYY-MM/week-[X]/`
- [ ] Email campaigns go in `04-campaigns/email/YYYY-MM/`
- [ ] Ad campaigns go in `06-ads/search-campaigns/`
- [ ] Old work goes in `05-archive/`
- [ ] Files follow naming convention: `[DATE]-[type]-[subject].md`

---

**Visual Structure Guide — 2026-02-24**

> © Pilgrim Prayers Content Organization
