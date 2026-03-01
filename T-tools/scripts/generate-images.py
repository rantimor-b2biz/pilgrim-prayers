"""
Pilgrim Prayers - Image Generator (Google Gemini / Imagen)
Reads AI prompts from a visual-brief.md file and generates images using Google Gemini API.

Works with any project folder in O-output/.

Usage:
    python generate-images.py <project-folder-or-visual-brief>
    python generate-images.py --all
    python generate-images.py --list

Examples:
    python generate-images.py O-output/02-weekly-post-galilee-living-land
    python generate-images.py 02-weekly-post-galilee-living-land
    python generate-images.py --all
    python generate-images.py --list

Setup:
    1. pip install google-genai
    2. Set your API key as environment variable: GEMINI_API_KEY
       - Windows: set GEMINI_API_KEY=your_key_here
       - Mac/Linux: export GEMINI_API_KEY=your_key_here
    3. Or create a .env file in the workspace root with: GEMINI_API_KEY=your_key_here
"""

import os
import re
import sys
from pathlib import Path

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("ERROR: google-genai package not installed.")
    print("Run: pip install google-genai")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Workspace root: two levels up from T-tools/scripts/
# ---------------------------------------------------------------------------
WORKSPACE_ROOT = Path(__file__).parent.parent.parent
OUTPUT_DIR = WORKSPACE_ROOT / "O-output"


def get_api_key():
    """Get API key from environment variable or .env file."""
    key = os.environ.get("GEMINI_API_KEY")
    if key:
        return key

    env_file = WORKSPACE_ROOT / ".env"
    if env_file.exists():
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("GEMINI_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")

    print("ERROR: GEMINI_API_KEY not found.")
    print("Set it as an environment variable or in a .env file in the workspace root.")
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

    # Direct path to the file
    if path.is_file() and path.name == "visual-brief.md":
        return path

    # It's a directory: look for visual-brief.md inside
    if path.is_dir():
        brief = path / "visual-brief.md"
        if brief.exists():
            return brief

    # Maybe they gave just the folder name (e.g. "02-weekly-post-galilee-living-land")
    brief = OUTPUT_DIR / path_arg / "visual-brief.md"
    if brief.exists():
        return brief

    # Maybe they gave a path relative to workspace root
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
            has_brief = brief.exists()
            image_count = len(list(images_dir.glob("*.png"))) if images_dir.exists() else 0

            if has_brief and image_count > 0:
                status = f"[DONE] {image_count} images generated"
            elif has_brief:
                status = "[READY] visual-brief.md found, no images yet"
            else:
                status = "[NO BRIEF] no visual-brief.md"

            print(f"  {project_dir.name}  {status}")


def parse_visual_brief(filepath):
    """
    Parse any visual-brief.md file and extract image sections with AI prompts.
    Flexible: matches any ## heading that contains an AI Prompt code block.
    Works with any post structure and any number of images.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    images = []

    # Split into sections by ## headings
    section_pattern = re.compile(r"^## (.+)$", re.MULTILINE)
    section_starts = [(m.start(), m.group(1)) for m in section_pattern.finditer(content)]

    for idx, (start, heading) in enumerate(section_starts):
        # Get section content (from this heading to the next, or end of file)
        end = section_starts[idx + 1][0] if idx + 1 < len(section_starts) else len(content)
        section = content[start:end]

        heading_lower = heading.lower().strip()

        # Skip non-image sections (notes, agent notes, etc.)
        skip_keywords = ["visual agent", "notes", "color", "alternative", "why this", "check"]
        if any(kw in heading_lower for kw in skip_keywords):
            continue

        # Determine image name from heading
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
            # Generic: slugify the heading
            name = re.sub(r"[^a-z0-9]+", "-", heading_lower).strip("-")
            if not name:
                continue

        # Extract AI prompt from code block
        prompt_match = re.search(r"\*\*AI Prompt:\*\*\s*```\s*\n(.*?)```", section, re.DOTALL)
        if not prompt_match:
            prompt_match = re.search(r"```\s*\n(.*?)```", section, re.DOTALL)

        if not prompt_match:
            continue

        prompt_text = prompt_match.group(1).strip()

        # Skip non-generatable prompts
        if prompt_text.upper().startswith("NOTE:"):
            print(f"  SKIP: {name} (marked as note, not AI-generated)")
            continue
        if prompt_text.lower().startswith("use the hero image"):
            print(f"  SKIP: {name} (derived from hero image, needs manual overlay)")
            continue

        # Determine aspect ratio from section content or defaults
        aspect = "16:9"  # default
        # Look for explicit aspect ratio before the AI Prompt section
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
        })

    return images


def generate_images(images, output_dir, model="imagen-3.0-generate-002", force=False):
    """Generate images using Gemini/Imagen API."""
    api_key = get_api_key()
    client = genai.Client(api_key=api_key)

    output_path = Path(output_dir) / "images"
    output_path.mkdir(parents=True, exist_ok=True)

    print(f"\nGenerating {len(images)} images...")
    print(f"Output directory: {output_path}")
    print(f"Model: {model}")
    print()

    results = []

    for i, img in enumerate(images):
        print(f"[{i+1}/{len(images)}] Generating: {img['name']} ({img['heading']})")
        print(f"  Aspect ratio: {img['aspect_ratio']}")
        print(f"  Prompt: {img['prompt'][:100]}...")

        # Skip if image already exists (unless --force)
        filepath = output_path / f"{img['name']}.png"
        if filepath.exists() and not force:
            print(f"  EXISTS: {filepath} (use --force to regenerate)")
            results.append({"name": img["name"], "path": str(filepath), "status": "exists"})
            continue

        try:
            response = client.models.generate_images(
                model=model,
                prompt=img["prompt"],
                config=types.GenerateImagesConfig(
                    number_of_images=1,
                    aspect_ratio=img["aspect_ratio"],
                ),
            )

            if response.generated_images:
                response.generated_images[0].image.save(str(filepath))
                print(f"  SAVED: {filepath}")
                results.append({"name": img["name"], "path": str(filepath), "status": "success"})
            else:
                print(f"  WARNING: No image returned for {img['name']}")
                results.append({"name": img["name"], "path": None, "status": "no image returned"})

        except Exception as e:
            print(f"  ERROR: {e}")
            results.append({"name": img["name"], "path": None, "status": f"error: {e}"})

    return results


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


def main():
    if len(sys.argv) < 2:
        print("Pilgrim Prayers - Image Generator (Gemini/Imagen)")
        print()
        print("Usage:")
        print("  python generate-images.py <project-folder>")
        print("  python generate-images.py <path-to-visual-brief.md>")
        print("  python generate-images.py --all")
        print("  python generate-images.py --list")
        print()
        print("Options:")
        print("  --all       Generate images for ALL projects with a visual-brief.md")
        print("  --list      List all projects and their image generation status")
        print("  --force     Regenerate images even if they already exist")
        print()
        print("Examples:")
        print("  python generate-images.py O-output/02-weekly-post-galilee-living-land")
        print("  python generate-images.py 02-weekly-post-galilee-living-land")
        print("  python generate-images.py --all")
        sys.exit(1)

    force = "--force" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]

    # --list: show project status
    if "--list" in sys.argv:
        list_projects()
        sys.exit(0)

    # --all: process all projects
    if "--all" in sys.argv:
        briefs = find_all_visual_briefs()
        if not briefs:
            print("No visual-brief.md files found in O-output/.")
            sys.exit(0)

        print(f"Pilgrim Prayers - Image Generator (Gemini/Imagen)")
        print(f"Found {len(briefs)} projects with visual briefs.\n")

        all_results = []
        for brief in briefs:
            project_name = brief.parent.name
            print(f"\n{'=' * 50}")
            print(f"PROJECT: {project_name}")
            print(f"{'=' * 50}")

            images = parse_visual_brief(str(brief))
            print(f"Found {len(images)} images to generate.")

            if images:
                results = generate_images(images, str(brief.parent), force=force)
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

    print(f"Pilgrim Prayers - Image Generator (Gemini/Imagen)")
    print(f"Reading: {brief_path}")

    images = parse_visual_brief(str(brief_path))
    print(f"Found {len(images)} images to generate.")

    if not images:
        print("No AI prompts found in the visual brief. Nothing to generate.")
        sys.exit(0)

    output_dir = str(brief_path.parent)
    results = generate_images(images, output_dir, force=force)
    print_summary(results)


if __name__ == "__main__":
    main()
