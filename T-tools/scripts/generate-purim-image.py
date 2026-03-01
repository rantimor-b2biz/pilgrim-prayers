#!/usr/bin/env python3
"""
Generate Purim blog post image via Replicate
Western Wall - golden hour - prayer note placement
Output: 1200x675 (16:9), suitable for blog hero image
"""

import replicate
import os
import sys
from pathlib import Path

def generate_image():
    # The prompt
    prompt = """A documentary photograph of the Western Wall in Jerusalem, golden hour lighting.
Warm, soft evening light illuminates ancient pale limestone with deep vertical weathering
patterns and crevices. Close-up angle shows tactile texture of the stone. A single right hand,
gentle and respectful, places a white prayer note into a stone crevice. Only the hand is visible—no face.
Soft shadows between stones create depth and dimension. The sky shows warm blues transitioning
to gold. Photography style: authentic, reverent, intimate, documentary real.
Color palette: warm golds, pale cream stone, deep shadow blacks in crevices, soft blue sky.
Mood: sacred, peaceful, hopeful. No crowds, no people visible except the hand.
Technical: photographic, high detail, 16:9 aspect ratio, professional quality,
cinematic lighting, shallow depth of field, sharp focus on hand and stone texture."""

    print("=" * 60)
    print("Generating Purim Blog Image")
    print("=" * 60)
    print("Model: Stability AI SDXL")
    print("Output: Western Wall - Golden Hour")
    print("Size: 1200x675 (16:9)")
    print("Status: Creating...")
    print()

    try:
        # Check if API token is set
        api_token = os.environ.get('REPLICATE_API_TOKEN')
        if not api_token:
            print("ERROR: REPLICATE_API_TOKEN not set")
            print()
            print("Please set your token first:")
            print('  export REPLICATE_API_TOKEN="your-token-here"')
            print()
            print("Then run this script again:")
            print('  python3 T-tools/scripts/generate-purim-image.py')
            sys.exit(1)

        # Run the model
        output = replicate.run(
            "stability-ai/sdxl:39ed52f2a60837716dead404dda9f29d873e91e559a440d65e91cb2265fba2dea",
            input={
                "prompt": prompt,
                "aspect_ratio": "16:9",
                "num_inference_steps": 50,
                "guidance_scale": 7.5
            }
        )

        print("SUCCESS! Image created.")
        print()
        print("Image URL:")
        print("-" * 60)

        if isinstance(output, list):
            for i, url in enumerate(output, 1):
                print(f"{i}. {url}")
        else:
            print(output)

        print("-" * 60)
        print()
        print("Next steps:")
        print("1. Download the image from the URL above")
        print("2. Optimize for web (< 500KB)")
        print("3. Save to: O-output/02-deliverables/week-10-deliverables/assets/purim-western-wall.jpg")
        print("4. Update: O-output/02-deliverables/week-10-deliverables/visual/2026-03-03-purim-visual-direction.md")
        print()

    except Exception as e:
        print(f"ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    generate_image()
