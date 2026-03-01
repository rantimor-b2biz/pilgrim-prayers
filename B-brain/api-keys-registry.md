# API Keys Registry

Track all external services connected to your AI team.

> **IMPORTANT:** Never store actual API keys in this file. Keep your keys secure in Claude Code settings or environment variables only. This file is for documentation and tracking purposes.

---

## Connected Services

| Service | Purpose | Connected | Status |
|---------|---------|-----------|--------|
| Google Gemini (Imagen 3) | Image generation for weekly posts | 2026-02-10 | Active |
| Replicate | Image + video generation for weekly posts | 2026-02-10 | Active |

---

## Service Details

## Google Gemini / Imagen 3

**Connected:** 2026-02-10
**Purpose:** Generate images from AI prompts in visual-brief.md for weekly blog posts and newsletters
**Used by:** Visual Agent (via generate-images.py script)

### Capabilities
- Text-to-image generation using Imagen 3 model
- Multiple aspect ratios: 1:1, 4:3, 3:4, 16:9, 9:16
- Hero images, inline images, newsletter headers for Pilgrim Prayers posts
- SynthID watermark automatically embedded (identifies AI-generated content)

### Models Available

| Model | Price | Best For |
|-------|-------|----------|
| Imagen 3 (`imagen-3.0-generate-002`) | $0.03/image | Standard weekly post images |
| Imagen 4 (`imagen-4.0-generate-001`) | Similar | Higher quality, one at a time |
| Gemini 2.5 Flash | Free tier | Testing and experiments |
| Gemini 3 Pro Image | $0.134/image | Professional 4K, text rendering |

### Current Usage
- ~4 images per weekly post (hero, 2 inline, newsletter header)
- Estimated cost: ~$0.12/week with Imagen 3
- Estimated annual cost: ~$6.25/year

### Limitations
- Imagen 3: Paid tier required (no free tier for image generation)
- Content safety filters may block some prompts
- AI-generated images have SynthID watermark (invisible to humans)
- Video thumbnails should use real frames, not AI-generated

### Setup Notes
- API key stored as environment variable: `GEMINI_API_KEY`
- Or in `.env` file at workspace root
- Python SDK: `pip install google-genai`
- Image generation script: `T-tools/scripts/generate-images.py`

### How to Use

```bash
# Set API key (one time)
set GEMINI_API_KEY=AIzaSyCpSiZgWZoHWfdg1rU2TCHosTYkr0pirX0

# Install SDK (one time)
pip install google-genai

# Generate images for a specific project (any of these work)
python T-tools/scripts/generate-images.py 02-weekly-post-galilee-living-land
python T-tools/scripts/generate-images.py O-output/02-weekly-post-galilee-living-land
python T-tools/scripts/generate-images.py O-output/02-weekly-post-galilee-living-land/visual-brief.md

# Generate images for ALL projects at once
python T-tools/scripts/generate-images.py --all

# List all projects and their image status
python T-tools/scripts/generate-images.py --list

# Regenerate images (even if they already exist)
python T-tools/scripts/generate-images.py 02-weekly-post-galilee-living-land --force
```

Images are saved to: `O-output/[project-folder]/images/`

---

## Replicate

**Connected:** 2026-02-10
**Purpose:** Generate images and videos from AI prompts in visual-brief.md for weekly blog posts and newsletters
**Used by:** Visual Agent (via generate-replicate.py script)

### Capabilities
- Text-to-image generation (Flux, Recraft V3, Stable Diffusion)
- Text-to-video generation (Veo 3, Hailuo 02, Kling 2.5)
- Image-to-video generation (Wan 2.1, Hailuo 02)
- Multiple aspect ratios and resolutions
- Pay-per-use pricing, no minimum commitment

### Recommended Models

**Images:**

| Model | Price | Best For |
|-------|-------|----------|
| `black-forest-labs/flux-1.1-pro` | ~$0.04/image | High quality, fast, great for landscapes |
| `black-forest-labs/flux-schnell` | ~$0.003/image | Quick drafts, testing prompts |
| `recraft-ai/recraft-v3` | ~$0.04/image | SOTA quality, good text rendering |

**Videos:**

| Model | Price | Best For |
|-------|-------|----------|
| `google/veo-3-fast` | ~$0.10/sec | Text-to-video, high quality |
| `minimax/hailuo-02` | ~$0.08/sec | Realistic motion, 6-10 sec clips |
| `kling-ai/kling-2.5-turbo-pro` | ~$0.06/sec | Cinematic depth, smooth motion |

### Smart Model Selection

The script automatically picks the best model per image type:

| Image Type | Model | Cost | Why |
|------------|-------|------|-----|
| Hero image | `flux-pro` | $0.04 | First impression, needs max quality |
| Inline images | `flux-schnell` | $0.003 | Supporting, good enough at 10x less cost |
| Newsletter header | `flux-schnell` | $0.003 | Small size, mobile-viewed |
| Social sharing (OG) | `recraft` | $0.04 | Best at text overlays and branding |
| Video (default) | `hailuo` | ~$0.28 | Realistic nature scenes and pans |

Override with `--model flux-schnell` (all images) or add `**Model:** recraft` in the visual brief per section.

### Current Usage Estimate
- Smart mode (default): ~$0.06/post (1x Pro + 3x Schnell + 1x Recraft)
- With video: ~$0.34/post
- All Schnell (testing): ~$0.015/post
- Estimated annual cost (smart, no video): ~$3.12/year
- Estimated annual cost (smart + video): ~$17.68/year

### Limitations
- Video generation takes 30-120 seconds per clip
- Content safety filters may block some prompts
- Video max length varies by model (6-10 seconds typical)
- Higher resolution = higher cost

### Setup Notes
- API token stored as environment variable: `REPLICATE_API_TOKEN`
- Or in `.env` file at workspace root
- Tokens always start with `r8_`
- Python SDK: `pip install replicate`
- Generation script: `T-tools/scripts/generate-replicate.py`

### How to Get Your API Token
1. Go to [replicate.com](https://replicate.com) and create an account
2. Go to [replicate.com/account/api-tokens](https://replicate.com/account/api-tokens)
3. Click "Create" to generate a new token
4. Copy the token (starts with `r8_`)
5. Set it as environment variable:

```bash
# Windows
set REPLICATE_API_TOKEN=r8_OKf7wf3oylpagjZqQBx8Vsvk6SezQgh2wc7VA

# Mac/Linux
export REPLICATE_API_TOKEN=r8_your_token_here
```

### How to Use

```bash
# Set API token (one time)
set REPLICATE_API_TOKEN=r8_OKf7wf3oylpagjZqQBx8Vsvk6SezQgh2wc7VA

# Install SDK (one time)
pip install replicate

# Generate images (smart model selection: best model per image type)
python T-tools/scripts/generate-replicate.py 12.2-weekly-post-galilee-living-land

# Generate images + video
python T-tools/scripts/generate-replicate.py 12.2-weekly-post-galilee-living-land --video

# Generate for ALL projects at once
python T-tools/scripts/generate-replicate.py --all
python T-tools/scripts/generate-replicate.py --all --video

# See all available models with pricing
python T-tools/scripts/generate-replicate.py --models

# List all projects and their media status
python T-tools/scripts/generate-replicate.py --list

# Override model for all images
python T-tools/scripts/generate-replicate.py 12.2-weekly-post-galilee-living-land --model flux-schnell

# Choose a specific video model
python T-tools/scripts/generate-replicate.py 12.2-weekly-post-galilee-living-land --video --video-model kling

# Regenerate everything (even if files already exist)
python T-tools/scripts/generate-replicate.py --all --video --force
```

Images saved to: `O-output/[project-folder]/images/`
Videos saved to: `O-output/[project-folder]/videos/`

---

## How to Add a New Service

1. Use the prompt in `T-tools/prompts/BONUS/08-connect-api-keys.md`
2. Follow the setup process
3. Add documentation here (but NOT your actual API key)
4. Update the table above

---

> **© Tom Even**
> Workshops & future dates: [www.getagents.today](https://www.getagents.today)
> Newsletter: [www.agentsandme.com](https://www.agentsandme.com)
