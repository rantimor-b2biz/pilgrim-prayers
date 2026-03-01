"""
Pilgrim Prayers - Image & Video Generator (Replicate)
Reads AI prompts from a visual-brief.md file and generates images and videos using Replicate API.

Smart model selection: automatically picks the best model for each image type,
or you can override with --model.

Works with any project folder in O-output/.

Usage:
    python generate-replicate.py <project-folder-or-visual-brief>
    python generate-replicate.py <project-folder> --video
    python generate-replicate.py --all
    python generate-replicate.py --list

Examples:
    python generate-replicate.py 12.2-weekly-post-galilee-living-land
    python generate-replicate.py 12.2-weekly-post-galilee-living-land --video
    python generate-replicate.py --all --video
    python generate-replicate.py --list
    python generate-replicate.py 12.2-weekly-post-galilee-living-land --model schnell

Setup:
    1. pip install replicate
    2. Set your API token as environment variable: REPLICATE_API_TOKEN
       - Windows: set REPLICATE_API_TOKEN=r8_your_token_here
       - Mac/Linux: export REPLICATE_API_TOKEN=r8_your_token_here
    3. Or create a .env file in the workspace root with: REPLICATE_API_TOKEN=r8_your_token_here
"""

import os
import re
import sys
import urllib.request
from pathlib import Path

try:
    import replicate
except ImportError:
    print("ERROR: replicate package not installed.")
    print("Run: pip install replicate")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Workspace root: two levels up from T-tools/scripts/
# ---------------------------------------------------------------------------
WORKSPACE_ROOT = Path(__file__).parent.parent.parent
OUTPUT_DIR = WORKSPACE_ROOT / "O-output"


# ---------------------------------------------------------------------------
# MODEL REGISTRY
# Each model has: replicate ID, cost, best for, and quality tier
# ---------------------------------------------------------------------------
MODELS = {
    # --- IMAGE MODELS ---
    "flux-pro": {
        "id": "black-forest-labs/flux-1.1-pro",
        "type": "image",
        "cost": "$0.04/image",
        "quality": "high",
        "speed": "~4 sec",
        "best_for": "Hero images, landscapes, photorealism. Best overall quality.",
    },
    "flux-schnell": {
        "id": "black-forest-labs/flux-schnell",
        "type": "image",
        "cost": "$0.003/image",
        "quality": "good",
        "speed": "~1 sec",
        "best_for": "Quick drafts, testing prompts, inline images where speed matters.",
    },
    "recraft": {
        "id": "recraft-ai/recraft-v3",
        "type": "image",
        "cost": "$0.04/image",
        "quality": "high",
        "speed": "~5 sec",
        "best_for": "Social sharing images with text overlay, logos, branded graphics.",
    },
    # --- VIDEO MODELS ---
    "hailuo": {
        "id": "minimax/hailuo-02",
        "type": "video",
        "cost": "~$0.28/video",
        "quality": "high",
        "speed": "~60 sec",
        "best_for": "Realistic motion, nature scenes, cinematic landscape pans.",
    },
    "kling": {
        "id": "kling-ai/kling-2.5-turbo-pro",
        "type": "video",
        "cost": "~$0.25/video",
        "quality": "high",
        "speed": "~45 sec",
        "best_for": "Cinematic depth, smooth motion, facial expressions.",
    },
    "wan": {
        "id": "wan-video/wan-2.1-t2v-480p",
        "type": "video",
        "cost": "~$0.05/video",
        "quality": "good",
        "speed": "~30 sec",
        "best_for": "Quick video drafts, budget-friendly, lower resolution.",
    },
}

# ---------------------------------------------------------------------------
# SMART MODEL SELECTION
# Maps image type → recommended model based on what works best
# ---------------------------------------------------------------------------
MODEL_RECOMMENDATIONS = {
    # Hero image: highest quality, this is the first thing people see
    "hero": "flux-pro",
    # Inline images: good quality but can save cost with Schnell
    "inline-1": "flux-schnell",
    "inline-2": "flux-schnell",
    "inline-3": "flux-schnell",
    "inline-4": "flux-schnell",
    "inline-5": "flux-schnell",
    # Newsletter header: simple, small, Schnell is enough
    "newsletter-header": "flux-schnell",
    # Social sharing: needs text overlay capability, Recraft is best
    "social-sharing": "recraft",
    # Thumbnail: small, Schnell is fine
    "thumbnail": "flux-schnell",
    # Banner: wide format, Flux Pro for quality
    "banner": "flux-pro",
    # Background: atmospheric, Flux Pro
    "background": "flux-pro",
}

# Default for any image type not in the map
DEFAULT_IMAGE_MODEL = "flux-pro"

# Video model defaults
DEFAULT_VIDEO_MODEL = "hailuo"


def get_api_token():
    """Get API token from environment variable or .env file."""
    token = os.environ.get("REPLICATE_API_TOKEN")
    if token:
        return token

    env_file = WORKSPACE_ROOT / ".env"
    if env_file.exists():
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("REPLICATE_API_TOKEN="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")

    print("ERROR: REPLICATE_API_TOKEN not found.")
    print("Set it as an environment variable or in a .env file in the workspace root.")
    print()
    print("Get your token at: https://replicate.com/account/api-tokens")
    sys.exit(1)


def find_visual_brief(path_arg):
    """
    Resolve a user-provided path to a visual-brief.md file.
    Accepts:
      - Direct path to a visual-brief.md file
      - A project folder (will look for visual-brief.md inside)
      - A project folder name without O-output/ prefix
    """
    path = Path(path_arg)

    if path.is_file() and path.name == "visual-brief.md":
        return path

    if path.is_dir():
        brief = path / "visual-brief.md"
        if brief.exists():
            return brief

    brief = OUTPUT_DIR / path_arg / "visual-brief.md"
    if brief.exists():
        return brief

    brief = WORKSPACE_ROOT / path_arg
    if brief.is_file():
        return brief
    if brief.is_dir():
        brief_file = brief / "visual-brief.md"
        if brief_file.exists():
            return brief_file

    return None


def find_all_visual_briefs():
    """Find all visual-brief.md files in O-output/."""
    briefs = []
    if not OUTPUT_DIR.exists():
        return briefs
    for project_dir in sorted(OUTPUT_DIR.iterdir()):
        if project_dir.is_dir():
            brief = project_dir / "visual-brief.md"
            if brief.exists():
                briefs.append(brief)
    return briefs


def list_projects():
    """List all projects in O-output/ and their visual brief status."""
    if not OUTPUT_DIR.exists():
        print("No O-output/ directory found.")
        return

    print("Projects in O-output/:")
    print()
    for project_dir in sorted(OUTPUT_DIR.iterdir()):
        if project_dir.is_dir():
            brief = project_dir / "visual-brief.md"
            images_dir = project_dir / "images"
            videos_dir = project_dir / "videos"
            has_brief = brief.exists()
            image_count = len(list(images_dir.glob("*.png"))) if images_dir.exists() else 0
            video_count = len(list(videos_dir.glob("*.mp4"))) if videos_dir.exists() else 0

            if has_brief and (image_count > 0 or video_count > 0):
                parts = []
                if image_count > 0:
                    parts.append(f"{image_count} images")
                if video_count > 0:
                    parts.append(f"{video_count} videos")
                status = f"[DONE] {', '.join(parts)} generated"
            elif has_brief:
                status = "[READY] visual-brief.md found, no media yet"
            else:
                status = "[NO BRIEF] no visual-brief.md"

            print(f"  {project_dir.name}  {status}")


def list_models():
    """Print all available models with details."""
    print("Available Models:")
    print()
    print("  IMAGE MODELS")
    print("  " + "-" * 70)
    for name, info in MODELS.items():
        if info["type"] == "image":
            print(f"  {name:<16} {info['cost']:<16} {info['speed']:<12} {info['quality']}")
            print(f"  {'':16} {info['best_for']}")
            print()

    print("  VIDEO MODELS")
    print("  " + "-" * 70)
    for name, info in MODELS.items():
        if info["type"] == "video":
            print(f"  {name:<16} {info['cost']:<16} {info['speed']:<12} {info['quality']}")
            print(f"  {'':16} {info['best_for']}")
            print()

    print("  SMART DEFAULTS (per image type)")
    print("  " + "-" * 70)
    for img_type, model_name in MODEL_RECOMMENDATIONS.items():
        cost = MODELS[model_name]["cost"]
        print(f"  {img_type:<20} → {model_name:<16} ({cost})")
    print()
    print(f"  Estimated cost per post (smart): ~$0.06 (1x Pro hero + 3x Schnell + 1x Recraft)")
    print(f"  Estimated cost per post (all Pro): ~$0.20 (5x Flux Pro)")
    print(f"  Estimated cost per post (all Schnell): ~$0.015 (5x Flux Schnell)")


def get_model_for_image(image_name, override=None):
    """
    Get the best model for a given image type.
    Returns (model_short_name, replicate_model_id).
    """
    if override and override in MODELS:
        return override, MODELS[override]["id"]

    model_name = MODEL_RECOMMENDATIONS.get(image_name, DEFAULT_IMAGE_MODEL)
    return model_name, MODELS[model_name]["id"]


def parse_visual_brief(filepath):
    """
    Parse any visual-brief.md file and extract image sections with AI prompts.
    Flexible: matches any ## heading that contains an AI Prompt code block.
    Also checks for **Model:** override in the section.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    images = []

    section_pattern = re.compile(r"^## (.+)$", re.MULTILINE)
    section_starts = [(m.start(), m.group(1)) for m in section_pattern.finditer(content)]

    for idx, (start, heading) in enumerate(section_starts):
        end = section_starts[idx + 1][0] if idx + 1 < len(section_starts) else len(content)
        section = content[start:end]

        heading_lower = heading.lower().strip()

        skip_keywords = ["visual agent", "notes", "color", "alternative", "why this", "check"]
        if any(kw in heading_lower for kw in skip_keywords):
            continue

        if heading_lower.startswith("hero"):
            name = "hero"
        elif re.match(r"inline\s*(image\s*)?1", heading_lower):
            name = "inline-1"
        elif re.match(r"inline\s*(image\s*)?2", heading_lower):
            name = "inline-2"
        elif re.match(r"inline\s*(image\s*)?3", heading_lower):
            name = "inline-3"
        elif re.match(r"inline\s*(image\s*)?4", heading_lower):
            name = "inline-4"
        elif re.match(r"inline\s*(image\s*)?5", heading_lower):
            name = "inline-5"
        elif "newsletter" in heading_lower:
            name = "newsletter-header"
        elif "social" in heading_lower or "open graph" in heading_lower or "og image" in heading_lower:
            name = "social-sharing"
        elif "thumbnail" in heading_lower:
            name = "thumbnail"
        elif "banner" in heading_lower:
            name = "banner"
        elif "background" in heading_lower:
            name = "background"
        else:
            name = re.sub(r"[^a-z0-9]+", "-", heading_lower).strip("-")
            if not name:
                continue

        prompt_match = re.search(r"\*\*AI Prompt:\*\*\s*```\s*\n(.*?)```", section, re.DOTALL)
        if not prompt_match:
            prompt_match = re.search(r"```\s*\n(.*?)```", section, re.DOTALL)

        if not prompt_match:
            continue

        prompt_text = prompt_match.group(1).strip()

        if prompt_text.upper().startswith("NOTE:"):
            print(f"  SKIP: {name} (marked as note, not AI-generated)")
            continue
        if prompt_text.lower().startswith("use the hero image"):
            print(f"  SKIP: {name} (derived from hero image, needs manual overlay)")
            continue

        # Check for model override in the section: **Model:** flux-pro
        model_override = None
        model_match = re.search(r"\*\*Model:\*\*\s*(\S+)", section)
        if model_match:
            model_override = model_match.group(1).strip().lower()

        # Determine aspect ratio
        aspect = "16:9"
        before_prompt = section.split("AI Prompt")[0] if "AI Prompt" in section else section
        aspect_match = re.search(r"(\d+:\d+)", before_prompt)
        if aspect_match:
            aspect = aspect_match.group(1)
        elif "inline" in name:
            aspect = "4:3"

        images.append({
            "name": name,
            "prompt": prompt_text,
            "aspect_ratio": aspect,
            "heading": heading.strip(),
            "model_override": model_override,
        })

    return images


def generate_image(img, output_path, model_id, force=False):
    """Generate a single image using Replicate API."""
    filepath = output_path / f"{img['name']}.png"
    if filepath.exists() and not force:
        print(f"  EXISTS: {filepath} (use --force to regenerate)")
        return {"name": img["name"], "path": str(filepath), "status": "exists"}

    try:
        output = replicate.run(
            model_id,
            input={
                "prompt": img["prompt"],
                "aspect_ratio": img["aspect_ratio"],
                "output_format": "png",
                "output_quality": 90,
                "num_outputs": 1,
            },
        )

        image_url = None
        if isinstance(output, list) and len(output) > 0:
            image_url = str(output[0])
        elif isinstance(output, str):
            image_url = output
        elif hasattr(output, "url"):
            image_url = output.url

        if image_url:
            urllib.request.urlretrieve(image_url, str(filepath))
            print(f"  SAVED: {filepath}")
            return {"name": img["name"], "path": str(filepath), "status": "success"}
        else:
            print(f"  WARNING: No image returned for {img['name']}")
            return {"name": img["name"], "path": None, "status": "no image returned"}

    except Exception as e:
        print(f"  ERROR: {e}")
        return {"name": img["name"], "path": None, "status": f"error: {e}"}


def generate_images(images, output_dir, model_override=None, force=False):
    """Generate images using smart model selection per image type."""
    output_path = Path(output_dir) / "images"
    output_path.mkdir(parents=True, exist_ok=True)

    print(f"\nGenerating {len(images)} images...")
    print(f"Output directory: {output_path}")
    if model_override:
        print(f"Model override: {model_override} (all images)")
    else:
        print("Model selection: SMART (best model per image type)")
    print()

    results = []

    for i, img in enumerate(images):
        # Pick model: CLI override > brief override > smart default
        if model_override:
            model_name, model_id = model_override, MODELS[model_override]["id"]
        elif img.get("model_override") and img["model_override"] in MODELS:
            model_name, model_id = img["model_override"], MODELS[img["model_override"]]["id"]
        else:
            model_name, model_id = get_model_for_image(img["name"])

        cost = MODELS[model_name]["cost"]
        print(f"[{i+1}/{len(images)}] {img['name']} ({img['heading']})")
        print(f"  Model: {model_name} ({cost})")
        print(f"  Aspect ratio: {img['aspect_ratio']}")
        print(f"  Prompt: {img['prompt'][:80]}...")

        result = generate_image(img, output_path, model_id, force=force)
        results.append(result)

    return results


def generate_video(prompt, output_dir, model_name=None, force=False):
    """Generate a short video using Replicate API."""
    model_name = model_name or DEFAULT_VIDEO_MODEL
    model_id = MODELS[model_name]["id"]

    output_path = Path(output_dir) / "videos"
    output_path.mkdir(parents=True, exist_ok=True)

    filepath = output_path / "post-video.mp4"
    if filepath.exists() and not force:
        print(f"\n  EXISTS: {filepath} (use --force to regenerate)")
        return {"name": "post-video", "path": str(filepath), "status": "exists"}

    cost = MODELS[model_name]["cost"]
    print(f"\nGenerating video...")
    print(f"  Model: {model_name} ({cost})")
    print(f"  Output: {output_path}")
    print(f"  Prompt: {prompt[:80]}...")

    try:
        output = replicate.run(
            model_id,
            input={
                "prompt": prompt,
                "duration": "6",
            },
        )

        video_url = None
        if isinstance(output, str):
            video_url = output
        elif hasattr(output, "url"):
            video_url = output.url

        if video_url:
            urllib.request.urlretrieve(video_url, str(filepath))
            print(f"  SAVED: {filepath}")
            return {"name": "post-video", "path": str(filepath), "status": "success"}
        else:
            print("  WARNING: No video returned")
            return {"name": "post-video", "path": None, "status": "no video returned"}

    except Exception as e:
        print(f"  ERROR: {e}")
        return {"name": "post-video", "path": None, "status": f"error: {e}"}


def print_summary(results):
    """Print generation summary."""
    print("\n" + "=" * 50)
    print("GENERATION SUMMARY")
    print("=" * 50)

    success = sum(1 for r in results if r["status"] == "success")
    exists = sum(1 for r in results if r["status"] == "exists")
    failed = len(results) - success - exists

    for r in results:
        if r["status"] == "success":
            icon = "NEW"
        elif r["status"] == "exists":
            icon = "OLD"
        else:
            icon = "FAIL"
        print(f"  [{icon}] {r['name']}: {r['path'] or r['status']}")

    print(f"\nTotal: {len(results)} | New: {success} | Already existed: {exists} | Failed: {failed}")


def process_project(brief_path, model_override=None, video_flag=False, video_model=None, force=False):
    """Process a single project: generate images and optionally video."""
    print(f"Reading: {brief_path}")
    images = parse_visual_brief(str(brief_path))
    print(f"Found {len(images)} images to generate.")

    if not images:
        print("No AI prompts found in the visual brief. Nothing to generate.")
        return []

    output_dir = str(brief_path.parent)
    results = generate_images(images, output_dir, model_override=model_override, force=force)

    if video_flag:
        hero_images = [img for img in images if img["name"] == "hero"]
        if hero_images:
            video_prompt = (
                "Slow cinematic aerial pan over the scene. "
                "Gentle camera movement, golden hour light, peaceful atmosphere. "
                + hero_images[0]["prompt"]
            )
            video_result = generate_video(video_prompt, output_dir, model_name=video_model, force=force)
            results.append(video_result)
        else:
            print("\nNo hero image prompt found for video generation.")

    return results


def main():
    if len(sys.argv) < 2:
        print("Image & Video Generator (Replicate) - Smart Model Selection")
        print()
        print("Usage:")
        print("  python generate-replicate.py <project-folder>")
        print("  python generate-replicate.py <project-folder> --video")
        print("  python generate-replicate.py --all")
        print("  python generate-replicate.py --models")
        print("  python generate-replicate.py --list")
        print()
        print("Model options:")
        print("  --model <name>     Override image model for ALL images")
        print("  --video-model <n>  Choose video model (hailuo, kling, wan)")
        print("  (no flag)          Smart selection: best model per image type")
        print()
        print("Available image models: flux-pro, flux-schnell, recraft")
        print("Available video models: hailuo, kling, wan")
        print()
        print("Other options:")
        print("  --all       Generate for ALL projects")
        print("  --video     Also generate a short video from the hero prompt")
        print("  --force     Regenerate even if files already exist")
        print("  --list      List all projects and their status")
        print("  --models    Show all models with pricing and recommendations")
        print()
        print("Examples:")
        print("  python generate-replicate.py 12.2-weekly-post-galilee-living-land")
        print("  python generate-replicate.py 12.2-weekly-post-galilee-living-land --video")
        print("  python generate-replicate.py 12.2-weekly-post-galilee-living-land --model flux-schnell")
        print("  python generate-replicate.py --all --video --video-model kling")
        sys.exit(1)

    # Parse flags
    video_flag = "--video" in sys.argv
    force = "--force" in sys.argv

    # Parse --model override
    model_override = None
    if "--model" in sys.argv:
        idx = sys.argv.index("--model")
        if idx + 1 < len(sys.argv):
            model_override = sys.argv[idx + 1].lower()
            if model_override not in MODELS or MODELS[model_override]["type"] != "image":
                print(f"ERROR: Unknown image model '{model_override}'")
                print(f"Available: {', '.join(k for k, v in MODELS.items() if v['type'] == 'image')}")
                sys.exit(1)
    # Legacy --schnell flag
    if "--schnell" in sys.argv:
        model_override = "flux-schnell"

    # Parse --video-model
    video_model = None
    if "--video-model" in sys.argv:
        idx = sys.argv.index("--video-model")
        if idx + 1 < len(sys.argv):
            video_model = sys.argv[idx + 1].lower()
            if video_model not in MODELS or MODELS[video_model]["type"] != "video":
                print(f"ERROR: Unknown video model '{video_model}'")
                print(f"Available: {', '.join(k for k, v in MODELS.items() if v['type'] == 'video')}")
                sys.exit(1)

    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    # Remove model/video-model values from args
    if "--model" in sys.argv:
        idx = sys.argv.index("--model")
        if idx + 1 < len(sys.argv):
            val = sys.argv[idx + 1]
            if val in args:
                args.remove(val)
    if "--video-model" in sys.argv:
        idx = sys.argv.index("--video-model")
        if idx + 1 < len(sys.argv):
            val = sys.argv[idx + 1]
            if val in args:
                args.remove(val)

    # --models: show all models
    if "--models" in sys.argv:
        list_models()
        sys.exit(0)

    # --list: show project status
    if "--list" in sys.argv:
        list_projects()
        sys.exit(0)

    # Verify API token
    os.environ["REPLICATE_API_TOKEN"] = get_api_token()

    # --all: process all projects
    if "--all" in sys.argv:
        briefs = find_all_visual_briefs()
        if not briefs:
            print("No visual-brief.md files found in O-output/.")
            sys.exit(0)

        print(f"Image & Video Generator (Replicate) - Smart Model Selection")
        print(f"Found {len(briefs)} projects with visual briefs.\n")

        all_results = []
        for brief in briefs:
            project_name = brief.parent.name
            print(f"\n{'=' * 50}")
            print(f"PROJECT: {project_name}")
            print(f"{'=' * 50}")

            results = process_project(
                brief,
                model_override=model_override,
                video_flag=video_flag,
                video_model=video_model,
                force=force,
            )
            all_results.extend(results)

        if all_results:
            print_summary(all_results)
        sys.exit(0)

    # Single project
    if not args:
        print("ERROR: No project folder or visual-brief.md specified.")
        sys.exit(1)

    brief_path = find_visual_brief(args[0])
    if not brief_path:
        print(f"ERROR: Could not find visual-brief.md for: {args[0]}")
        print()
        list_projects()
        sys.exit(1)

    print(f"Image & Video Generator (Replicate) - Smart Model Selection")
    results = process_project(
        brief_path,
        model_override=model_override,
        video_flag=video_flag,
        video_model=video_model,
        force=force,
    )

    if results:
        print_summary(results)


if __name__ == "__main__":
    main()
