# T-tools: Skills, Prompts & Workflows

This folder contains reusable tools that give your agents superpowers.

> "Tools are how things get done."

---

## What's Here

```
T-tools/
├── skills/                → Specialized knowledge for specific tasks
│   ├── linkedin-post-skill/
│   └── twitter-thread-skill/
├── prompts/               → Saved prompts for common actions
│   ├── 01-convert-brand-discovery.md
│   ├── 02-learn-my-writing-style.md
│   ├── 03-sync-agents-with-context.md
│   ├── 04-create-linkedin-post.md
│   └── BONUS/
│       ├── 05-create-new-agent.md
│       ├── 06-create-new-skill.md
│       ├── 07-enable-auto-revision-loop.md
│       ├── 08-connect-api-keys.md
│       ├── 09-content-calendar.md
│       ├── 10-repurpose-content.md
│       ├── 11-analyze-competitor.md
│       ├── 12-create-hook-bank.md
│       └── 13-weekly-review.md
├── workflows/             → Step-by-step processes
│   └── linkedin-post-workflow.md
└── README.md              → You are here
```

---

## The Three Types of Tools

### Skills
**What:** Specialized knowledge packages for specific content types.

**Think of them as:** Expert playbooks with best practices, templates, and quality checklists.

**Example:** `skills/linkedin-post-skill/` — Everything an agent needs to write great LinkedIn posts.

### Prompts
**What:** Saved prompts for common actions you'll repeat.

**Think of them as:** Copy-paste instructions you don't want to type every time.

**Example:** `prompts/04-create-linkedin-post.md` — The exact prompt to give Claude when you want a LinkedIn post.

**Workshop flow:** Prompts are numbered to guide you through the workshop exercises (01 → 07).

### Workflows
**What:** Step-by-step processes that coordinate multiple agents or actions.

**Think of them as:** Recipes that describe how different parts work together.

**Example:** `workflows/linkedin-post-workflow.md` — The full process from idea to published post.

---

## How to Use

### Using Skills
Agents automatically read skills when working on matching tasks:
1. Agent reads skill file for best practices
2. Applies frameworks and rules
3. Uses quality checklist before delivering

### Using Prompts
Copy the prompt and paste it to Claude:
1. Open the prompt file
2. Copy the prompt text
3. Paste to Claude
4. Get results

### Using Workflows
Follow the workflow for complex multi-step tasks:
1. Read the workflow file
2. Follow each step in order
3. Reference skills as needed

---

## Available Tools

### Skills

| Skill | Purpose | Use When |
|-------|---------|----------|
| linkedin-post-skill | LinkedIn content | Writing LinkedIn posts |
| twitter-thread-skill | Twitter/X threads | Creating Twitter threads |

### Prompts (Workshop Order)

| # | Prompt | What It Does |
|---|--------|--------------|
| 01 | convert-brand-discovery | Convert worksheet answers → C-core files |
| 02 | learn-my-writing-style | Analyze writing samples → update voice DNA |
| 03 | sync-agents-with-context | Update agents after changing C-core |
| 04 | create-linkedin-post | Create a LinkedIn post from a topic |

**BONUS prompts** (in `prompts/BONUS/`):

| # | Prompt | What It Does |
|---|--------|--------------|
| 05 | create-new-agent | Create a new agent definition |
| 06 | create-new-skill | Create a new skill file |
| 07 | enable-auto-revision-loop | Set up automatic revision workflow |
| 08 | connect-api-keys | Connect external APIs (image gen, TTS, etc.) |
| 09 | content-calendar | Plan content for weeks/months ahead |
| 10 | repurpose-content | Turn one piece into multiple formats |
| 11 | analyze-competitor | Study what works for others in your space |
| 12 | create-hook-bank | Build a collection of opening lines |
| 13 | weekly-review | Review performance and capture learnings |

### Workflows

| Workflow | Purpose |
|----------|---------|
| linkedin-post-workflow | Full process: idea → draft → review → publish |

---

## Creating New Tools

### New Skill
1. Create folder: `skills/[name]-skill/`
2. Create file: `[name]-skill.md`
3. Include: When to use, principles, templates, checklist

### New Prompt
1. Create file: `prompts/[##]-[name].md`
2. Number for order if part of a sequence
3. Include: The exact prompt text to copy

### New Workflow
1. Create file: `workflows/[name]-workflow.md`
2. Include: Steps, agents involved, expected outputs

---

> **© Tom Even**
> Workshops & future dates: [www.getagents.today](https://www.getagents.today)
> Newsletter: [www.agentsandme.com](https://www.agentsandme.com)
