# Visual Generation Workflow
**Version:** 1.0
**Updated:** 2026-03-01

The complete loop from post approval to published images — Visual Agent, Replicate API, and Agency Manager review.

---

## Overview

```
Copywriter (approved post)
        ↓
Visual Agent — creates visual-brief.md
        ↓
Replicate API — generates images
        ↓
Images saved to /visual/images/
        ↓
Agency Manager — reviews images
        ↓
    APPROVED?
   ↙         ↘
  YES          NO
   ↓            ↓
 DONE    Visual Agent revises prompts
              ↓
         Replicate (--force)
              ↓
         New images → review again
```

---

## Folder Structure (Standard)

Every project must follow this structure:

```
O-output/02-deliverables/week-[N]-deliverables/
└── visual/
    ├── visual-brief.md          ← Visual Agent writes this
    └── images/                  ← Replicate saves here automatically
        ├── hero.png
        ├── inline-1.png
        ├── newsletter-header.png
        └── social-sharing.png
```

The file **must be named `visual-brief.md`** — the script depends on this exact name.

---

## Step 1: Visual Agent Creates Brief

Visual Agent reads the approved post and creates `visual-brief.md`.

**Required sections in the brief** (each section becomes one image):

```markdown
## Hero Image
**Aspect ratio:** 16:9
**Model:** flux-pro

[AI prompt here]

---

## Inline Image 1
**Aspect ratio:** 4:3
**Model:** flux-schnell

[AI prompt here]

---

## Newsletter Header
**Aspect ratio:** 600:250
**Model:** flux-schnell

[AI prompt here]

---

## Social Sharing
**Aspect ratio:** 1200:630
**Model:** recraft

[AI prompt here]
```

The script reads everything inside code blocks under each `## Heading` as the prompt.
The heading name becomes the filename (e.g., `## Hero Image` → `hero-image.png`).

---

## Step 2: Generate via Replicate

Visual Agent runs from the workspace root:

```bash
python T-tools/scripts/generate-replicate.py \
  O-output/02-deliverables/week-[N]-deliverables/visual/visual-brief.md
```

**What the script does:**
- Reads all prompts from `visual-brief.md`
- Selects the best model per image type (or uses `**Model:**` override)
- Calls Replicate API
- Downloads and saves all images to `.../visual/images/`
- Prints a cost summary when done

**With video:**
```bash
python T-tools/scripts/generate-replicate.py [path] --video
```

**Estimated costs per weekly post:**
| Mode | Cost |
|------|------|
| Default (smart model selection) | ~$0.06 |
| All Flux Pro | ~$0.20 |
| All Flux Schnell (draft/testing) | ~$0.015 |
| + Video | add ~$0.28 |

---

## Step 3: Visual Agent Reports to Agency Manager

After images are generated, Visual Agent sends this report:

```
VISUAL GENERATION COMPLETE — Week [N]: [Post Title]

Generated images:
  hero.png             → [path]/images/hero.png
  inline-1.png         → [path]/images/inline-1.png
  newsletter-header.png → [path]/images/newsletter-header.png
  social-sharing.png   → [path]/images/social-sharing.png

Estimated cost: $[X]
Models used: [list]

Ready for Agency Manager review.
```

---

## Step 4: Agency Manager Reviews

Agency Manager opens each image and checks against the **Visual Review Checklist:**

### Image Review Checklist

**Brand:**
- [ ] Warm tone — Jerusalem gold, ancient stone, parchment (not cold or dark)
- [ ] Feels like "a quiet photograph taken by someone who was truly there"
- [ ] No stock photography feel (no perfect models, no staged hands)

**Content:**
- [ ] No political imagery (no soldiers, flags, barriers, protests)
- [ ] No identifiable faces (privacy)
- [ ] No Catholic/Orthodox iconography (no crucifixes, icons, rosaries)
- [ ] No tourist crowds or souvenir-shop atmosphere
- [ ] No suffering or graphic violence

**Composition:**
- [ ] Hero image: room for text overlay on left or right third
- [ ] Newsletter header: readable at 600px wide and on mobile
- [ ] Social sharing image: one clear focal point, readable at thumbnail size

**Mood:**
- [ ] Matches the post's emotional tone (Lenten = weight + warmth, not darkness)
- [ ] The image could stand alone — someone who sees it without text should feel something

### Decision

| Outcome | Action |
|---------|--------|
| APPROVED | All images sign off → proceed to publish |
| PARTIAL — one image needs revision | Visual Agent revises that prompt + re-runs with `--force` |
| REJECTED — full revision | Visual Agent rewrites brief + re-runs all |

---

## Step 5: Revision (if needed)

Visual Agent:

1. Updates the specific section(s) in `visual-brief.md` with new/improved prompt
2. Re-runs the script with `--force` flag to overwrite existing images:

```bash
python T-tools/scripts/generate-replicate.py \
  O-output/02-deliverables/week-[N]-deliverables/visual/visual-brief.md \
  --force
```

3. Reports new images to Agency Manager
4. Repeat until APPROVED

**Common revision reasons and fixes:**

| Agency Manager Feedback | Visual Agent Fix |
|------------------------|-----------------|
| "Too dark / cold" | Add "warm golden light, morning sun" to prompt |
| "Too generic / stock photo" | Add specific Jerusalem detail: name the stone, the arch, the specific site |
| "Feels religious (Catholic)" | Remove any cross, church interior, or ornate altar reference from prompt |
| "Too many people" | Add "empty, or one distant figure, no tourist crowds" |
| "Text overlay area missing" | Add "negative space on [left/right] third for text overlay" |
| "Wrong aspect ratio" | Check `**Aspect ratio:**` line in the brief section |

---

## Quick Reference Commands

```bash
# List all projects and their visual brief status
python T-tools/scripts/generate-replicate.py --list

# Generate for a single project
python T-tools/scripts/generate-replicate.py O-output/02-deliverables/week-9-deliverables/visual/visual-brief.md

# Force regenerate (after prompt revision)
python T-tools/scripts/generate-replicate.py [path] --force

# Generate all projects at once
python T-tools/scripts/generate-replicate.py --all

# Use cheaper model for drafts
python T-tools/scripts/generate-replicate.py [path] --model flux-schnell

# See all available models and costs
python T-tools/scripts/generate-replicate.py --models
```

---

## API Token Setup

The script reads the token from:
1. Environment variable: `REPLICATE_API_TOKEN`
2. `.env` file at the workspace root: `REPLICATE_API_TOKEN=r8_your_token_here`

In Claude Code on the web (Replit), the session-start hook installs the `replicate` package automatically. You still need to set the API token in the `.env` file.
