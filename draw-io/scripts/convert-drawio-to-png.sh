#!/bin/bash
set -e

# Convert .drawio files to .drawio.png
# Usage: bash convert-drawio-to-png.sh <file1.drawio> [file2.drawio] ...

# Pre-flight: check drawio CLI
if ! command -v drawio &> /dev/null; then
  echo "✗ drawio CLI not found." >&2
  echo "  Install from: https://github.com/jgraph/drawio-desktop/releases" >&2
  exit 1
fi

# Check arguments
if [ $# -eq 0 ]; then
  echo "Usage: $0 <file1.drawio> [file2.drawio] ..."
  echo "Example: $0 assets/architecture.drawio"
  exit 1
fi

generated_files=()

for drawio in "$@"; do
  png="${drawio%.drawio}.drawio.png"
  echo "Converting $drawio to $png..."

  # drawio CLI export to PNG with 2x scale for high quality
  if ! drawio -x -f png -s 2 -t -o "$png" "$drawio" 2>/dev/null; then
    echo "✗ drawio PNG export failed for $drawio" >&2
    continue
  fi

  generated_files+=("$png")
  echo "✓ Generated $png"
done

# Stage all generated files at once to avoid index.lock conflicts
# Note: This git add is intended for pre-commit hook workflows
if [ ${#generated_files[@]} -gt 0 ]; then
  git add "${generated_files[@]}"
  echo "Staged ${#generated_files[@]} file(s)"
fi
