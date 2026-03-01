# AI Agent Team Template (ABC-TOM)

Welcome! This template helps you build your own team of AI agents for content creation.

**Organized using the ABC-TOM Framework:**
> "Feed the ABC. Let TOM execute."

---

## The Structure

```
ABC — The Foundation (What You Feed The System)
├── A-agents/     → Your AI team definitions
├── B-brain/      → Knowledge, research, references
└── C-core/       → Brand DNA, identity, who you are

TOM — The Execution (What The System Does)
├── T-tools/      → Skills, workflows, reusable capabilities
├── O-output/     → Everything your agents create
└── M-memory/     → What the system learns over time
```

---

## What's Inside

### A-agents/ (Your Team)

```
A-agents/
├── copywriter-agent.md  → Writes all your content
├── gatekeeper-agent.md  → Reviews quality before publishing
└── README.md            → How agents work together
```

**The hierarchy:**
```
YOU (direction + final approval)
    ↓
Copywriter Agent (creates content)
    ↓
Gatekeeper Agent (quality check)
    ↓
YOU (publish)
```

### B-brain/ (Knowledge)

```
B-brain/
├── research/              → Industry data, competitor info
├── writing-samples/       → Your past content (for voice learning)
├── brand-discovery-worksheet.md → Quick onboarding (Hebrew)
└── data/                  → Analytics, metrics
```

Feed your agents the knowledge they need.

### C-core/ (Your Brand)

```
C-core/
├── project-brief.md  → What you do, who you serve
├── voice-dna.md      → How your brand speaks
└── icp-profile.md    → Your target audience
```

**Fill these in first!** Your agents need to know your brand to write for it.

### T-tools/ (Skills, Prompts & Workflows)

```
T-tools/
├── skills/                → Specialized knowledge (linkedin, twitter)
├── prompts/               → Saved prompts (numbered for workshop)
└── workflows/             → Step-by-step processes
```

Three types of tools:
- **Skills** — Expert playbooks for specific content types
- **Prompts** — Copy-paste instructions for common actions
- **Workflows** — Multi-step processes that coordinate agents

### O-output/ (Created Work)

```
O-output/
└── [your-projects-go-here]/
```

Each project gets its own folder. Numbered for order.

### M-memory/ (System Learning)

```
M-memory/
├── learning-log.md   → How we work (execution patterns)
├── feedback.md       → What they say (audience signals)
└── decisions.md      → Why we do things (strategic rationale)
```

**This is what makes your system get smarter over time.**

---

## How to Use

### Step 0: Quick Start (Brand Discovery)

**Fastest way to get started:**

1. Open `B-brain/brand-discovery-worksheet.md`
2. Fill in the 10 questions (~10 minutes)
3. Ask Claude: "קרא את התשובות והמר אותן לקבצי C-core"
4. Claude populates your C-core files automatically

This is the workshop onboarding flow.

### Step 1: Fill Your Core (C-core/)

If you prefer to fill manually:

1. **`C-core/project-brief.md`** — What you do
2. **`C-core/voice-dna.md`** — How you sound
3. **`C-core/icp-profile.md`** — Who you serve

### Step 2: Feed the Brain (B-brain/)

Add knowledge your agents need:

1. **Writing samples** — Put your past content in `B-brain/writing-samples/`
2. **Research** — Any industry data or competitor info
3. **References** — Examples of content you admire

### Step 3: Create Content

When you want to create content:

1. Give the Copywriter a topic and direction
2. Agent reads from A, B, C folders to understand context
3. Agent uses T-tools for specialized knowledge
4. Copywriter creates the content → saves to O-output
5. Gatekeeper reviews quality
6. Iterate until approved
7. You publish!

### Step 4: Update Memory (M-memory/)

After each project:
- Log what worked in `M-memory/learning-log.md`
- Agents read this before starting new work
- Your team gets better over time

---

## Example Workflow

**You say:** "I need a LinkedIn post about productivity"

**Copywriter Agent:**
1. Reads `C-core/voice-dna.md` and `C-core/icp-profile.md`
2. Checks `M-memory/learning-log.md` for past patterns
3. Uses `T-tools/skills/linkedin-post-skill/` for LinkedIn best practices
4. Writes the post
5. Saves to `O-output/`

**Gatekeeper Agent:**
1. Reviews against quality standards
2. Scores the work
3. Approves or sends back with feedback

**You:**
1. Review and publish
2. Log learnings to `M-memory/`

---

## Folder Quick Reference

| Folder | What Goes Here | Agents Read/Write |
|--------|----------------|-------------------|
| **A-agents/** | Team definitions | Reference only |
| **B-brain/** | Knowledge, research | Read |
| **C-core/** | Brand DNA | Read |
| **T-tools/** | Skills, prompts, workflows | Read |
| **O-output/** | Created content | Write |
| **M-memory/** | Learning patterns | Read + Write |

---

## Getting Started Checklist

- [ ] Fill `B-brain/brand-discovery-worksheet.md` (or fill C-core manually)
- [ ] Ask Claude to convert worksheet → C-core files
- [ ] Add 3-5 writing samples to `B-brain/writing-samples/`
- [ ] Read through each agent file in `A-agents/`
- [ ] Read the LinkedIn skill in `T-tools/skills/linkedin-post-skill/`
- [ ] Try creating one simple LinkedIn post
- [ ] Log what you learned in `M-memory/learning-log.md`

---

## Tips for Success

1. **Be specific in C-core files** — Vague brand info = vague content
2. **Feed the brain** — More knowledge in B-brain = smarter agents
3. **Update memory** — Your team improves by remembering
4. **One project per output folder** — Keep things organized
5. **Start simple** — Try one LinkedIn post before complex workflows

---

## The ABC-TOM Mantras

**The core concept:**
> "Feed the ABC. Let TOM execute."

**The distinction:**
> "ABC is who you are. TOM is what you do."

**The insight:**
> "Brain is what you feed the system. Memory is what the system learns."

---

## Need Help?

- Read the agent files — they explain their own roles
- Check the skills folder for platform-specific guidance
- Review the framework documentation for deeper understanding

---

*Keep yourself in the loop.*

---

> **© Tom Even**
> Workshops & future dates: [www.getagents.today](https://www.getagents.today)
> Newsletter: [www.agentsandme.com](https://www.agentsandme.com)
