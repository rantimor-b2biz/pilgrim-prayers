#!/bin/bash
set -euo pipefail

# Only run in Claude Code on the web (Replit / remote environment)
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

echo "Installing Python dependencies for Replicate image/video generation..."
pip install replicate --quiet

echo "Replicate ready."
