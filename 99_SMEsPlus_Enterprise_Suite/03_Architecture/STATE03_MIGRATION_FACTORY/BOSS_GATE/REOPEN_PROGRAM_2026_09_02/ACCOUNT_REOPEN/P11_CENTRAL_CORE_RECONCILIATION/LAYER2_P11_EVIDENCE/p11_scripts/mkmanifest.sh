#!/bin/sh
# P11 evidence manifest — per-file SHA-256 plus roll-up.
# POPULATION: every file in the P11 package directory. PATTERN: find -type f. UNIT: one file.
cd "$(dirname "$0")/../.."
find . -type f ! -name 'P11_EVIDENCE_MANIFEST.md' | sort | while read f; do
  printf '%s  %s\n' "$(shasum -a 256 "$f" | cut -d' ' -f1)" "${f#./}"
done
