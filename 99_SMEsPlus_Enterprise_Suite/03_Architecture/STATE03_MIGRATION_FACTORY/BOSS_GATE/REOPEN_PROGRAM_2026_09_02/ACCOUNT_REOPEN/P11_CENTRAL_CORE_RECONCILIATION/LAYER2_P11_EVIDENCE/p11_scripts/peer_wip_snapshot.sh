#!/bin/sh
# P11 CP-01 — PEER WORK-IN-PROGRESS SNAPSHOT (time-bounded)
# The peer sessions are LIVE. Any count here is a snapshot at the stated instant,
# not a stable population. Re-run to obtain a later snapshot.
# POPULATION : every sibling session clone matching ACCOUNT_P??_*_2026_09_04_EXECUTION
# PATTERN    : git ls-files --others --exclude-standard  (untracked, uncommitted)
# PATH SET   : the parent volume directory of this clone
# UNIT       : one untracked file
date '+SNAPSHOT_UTC=%Y-%m-%dT%H:%M:%S%z'
cd "$(git rev-parse --show-toplevel)/.."
for d in ACCOUNT_P0[1-9]_*_2026_09_04_EXECUTION ACCOUNT_P10_*_2026_09_04_EXECUTION; do
  [ -d "$d/.git" ] || continue
  ahead=$(git -C "$d" rev-list --count origin/SMEsPlus..HEAD 2>/dev/null || echo NA)
  pushed=$(git -C "$d" ls-remote --heads origin "$(git -C "$d" branch --show-current)" 2>/dev/null | wc -l | tr -d ' ')
  printf '%-48s commits=%s pushed_branch=%s untracked=%s\n' "$d" "$ahead" "$pushed" \
    "$(git -C "$d" ls-files --others --exclude-standard 2>/dev/null | wc -l | tr -d ' ')"
  git -C "$d" ls-files --others --exclude-standard 2>/dev/null \
    | sed 's|^99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/||' \
    | sed 's/^/    /'
done
