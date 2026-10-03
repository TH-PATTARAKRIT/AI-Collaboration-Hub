#!/usr/bin/env bash
set -euo pipefail

skill_dir="$(cd "$(dirname "$0")/.." && pwd)"
skill_name="$(basename "$skill_dir")"
output_dir="${1:-$(pwd)/dist}"

required_files=(
  "$skill_dir/SKILL.md"
  "$skill_dir/agents/openai.yaml"
  "$skill_dir/references/master-control.md"
  "$skill_dir/references/state-workflows.md"
  "$skill_dir/references/governance-controls.md"
  "$skill_dir/references/decision-and-handoff.md"
  "$skill_dir/templates/execution-order.md"
  "$skill_dir/templates/final-report.md"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "ERROR: missing required file: $file" >&2
    exit 1
  fi
done

grep -q '^name: smesplus-execution-controller$' "$skill_dir/SKILL.md" || {
  echo "ERROR: invalid skill name in SKILL.md" >&2
  exit 1
}

grep -q '^description:' "$skill_dir/SKILL.md" || {
  echo "ERROR: missing skill description" >&2
  exit 1
}

mkdir -p "$output_dir"
rm -f "$output_dir/skill.zip" "$output_dir/skill.zip.sha256"

parent_dir="$(dirname "$skill_dir")"
(
  cd "$parent_dir"
  zip -r "$output_dir/skill.zip" "$skill_name"
)

unzip -t "$output_dir/skill.zip"
sha256sum "$output_dir/skill.zip" > "$output_dir/skill.zip.sha256"

echo "PACKAGE COMPLETED"
echo "File: $output_dir/skill.zip"
echo "SHA256: $(cat "$output_dir/skill.zip.sha256")"
