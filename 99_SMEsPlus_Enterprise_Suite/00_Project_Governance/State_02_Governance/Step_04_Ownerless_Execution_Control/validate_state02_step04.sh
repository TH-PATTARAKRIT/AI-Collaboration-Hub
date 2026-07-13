#!/usr/bin/env bash
# validate_state02_step04.sh
# Preparer self-check only. NOT independent verification.
# Verifies that every SHA-256 entry in the manifest matches the bytes of the
# corresponding staged file, and that no staged file is missing from the manifest.
#
# Usage: validate_state02_step04.sh <staging_dir> <manifest_file>
# Exit:  0 = all checks passed (preparer self-check); non-zero = at least one failure.

set -u

STAGE="${1:?staging directory required}"
MANIFEST="${2:?manifest file required}"

if [ ! -d "$STAGE" ]; then
  echo "FAIL: staging directory not found: $STAGE"
  exit 1
fi
if [ ! -f "$MANIFEST" ]; then
  echo "FAIL: manifest file not found: $MANIFEST"
  exit 1
fi

fail=0

echo "== Checking manifest hash entries against staged files =="
while IFS= read -r line; do
  case "$line" in
    \#*|"") continue ;;
    "SELF - HASH EXCLUDED"*) continue ;;
  esac
  hash=$(printf '%s\n' "$line" | awk '{print $1}')
  file=$(printf '%s\n' "$line" | cut -d' ' -f2- | sed 's/^ *//')
  [ -z "$hash" ] && continue
  [ -z "$file" ] && continue
  path="$STAGE/$file"
  if [ ! -f "$path" ]; then
    echo "FAIL: listed in manifest but missing from staging: $file"
    fail=1
    continue
  fi
  actual=$(sha256sum "$path" | awk '{print $1}')
  if [ "$actual" != "$hash" ]; then
    echo "FAIL: hash mismatch for $file"
    echo "      manifest: $hash"
    echo "      actual:   $actual"
    fail=1
  else
    echo "OK: $file"
  fi
done < "$MANIFEST"

echo "== Checking for staged files not listed in manifest =="
for f in "$STAGE"/*; do
  name=$(basename "$f")
  [ "$name" = "$(basename "$MANIFEST")" ] && continue
  if ! grep -q "  $name\$" "$MANIFEST"; then
    echo "FAIL: staged file not present in manifest: $name"
    fail=1
  fi
done

if [ "$fail" -eq 0 ]; then
  echo "RESULT: PREPARER CHECK PASSED — 0 mismatches"
  exit 0
else
  echo "RESULT: PREPARER CHECK FAILED — see FAIL lines above"
  exit 1
fi
