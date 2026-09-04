#!/bin/sh
# P11 CP-01 — PEER EVIDENCE INTAKE ENUMERATION  (v2, corrected per X4-F02)
#
# v1 DEFECT, found by independent review and reproduced here:
#   `set -e` around the section-C loop killed the subshell at the first ref with no
#   match (origin/SMEsPlus, enumerated first), so PATTERN (b) could NEVER return a hit.
#   v1's empty section C was an ARTEFACT, not a measurement. v2 removes `set -e` from C,
#   adds `|| true` per ref, and adds a POSITIVE CONTROL so an empty C is evidence.
#
# POPULATION : every ref reachable from origin in TH-PATTARAKRIT/AI-Collaboration-Hub,
#              and every sibling session clone matching ACCOUNT_P01..P10
# PATTERN    : (a) branch name matching a P01..P10 process slug
#              (b) any tracked path segment matching ^P(0[1-9]|10)_ on ANY ref
#              (c) local clone commits-ahead, pushed-branch state, untracked count
# PATH SET   : refs/remotes/origin/*  (ALL of them) ; the parent volume directory
# UNIT       : one git ref ; one tracked file path ; one clone
cd "$(git rev-parse --show-toplevel)"
git fetch -q origin 'refs/heads/*:refs/remotes/origin/*'
date '+SNAPSHOT_UTC=%Y-%m-%dT%H:%M:%S%z'

echo "== A. total remote branches (declared denominator) =="
git branch -r | grep -v HEAD | wc -l | tr -d ' '

echo "== B. branches whose name matches a P01..P10 process slug =="
git branch -r | grep -v HEAD | grep -Ei \
 'p2p|procure-to-pay|o2c|order-to-cash|m2c|manufacture-to-cost|a2r|acquire-to-retire|e2p|expense-to-pay|b2r|bank-to-reconcile|tax-to-compliance|th-tax-compliance|r2r|record-to-report|plan-to-analyze|time-based-recognition|core-reconciliation' \
 || echo "(none)"

echo "== C. tracked path segments matching ^P(0[1-9]|10)_ on ANY ref =="
echo "-- C0 POSITIVE CONTROL: the loop must be able to return a hit at all --"
ctl=0
for b in $(git branch -r | grep -v HEAD | sed 's| *origin/||'); do
  n=$(git ls-tree -r --name-only "origin/$b" 2>/dev/null | grep -cE '(^|/)P(0[1-9]|10)_' || true)
  ctl=$((ctl + n))
done
echo "C0 total matching paths across all refs = $ctl   (0 here means the pattern truly finds nothing;"
echo "    v1 could not distinguish this from a dead loop)"
echo "-- C1 distinct matching paths --"
for b in $(git branch -r | grep -v HEAD | sed 's| *origin/||'); do
  git ls-tree -r --name-only "origin/$b" 2>/dev/null | grep -E '(^|/)P(0[1-9]|10)_' || true
done | sort -u | sed -n '1,60p'
echo "(end C)"

echo "== D. peer clone state — commits ahead, pushed, untracked (WIP) =="
cd ..
for d in ACCOUNT_P0[1-9]_*_2026_09_04_EXECUTION ACCOUNT_P10_*_2026_09_04_EXECUTION; do
  [ -d "$d/.git" ] || continue
  br=$(git -C "$d" branch --show-current 2>/dev/null)
  ahead=$(git -C "$d" rev-list --count origin/SMEsPlus..HEAD 2>/dev/null || echo NA)
  pushed=$(git -C "$d" ls-remote --heads origin "$br" 2>/dev/null | wc -l | tr -d ' ')
  unt=$(git -C "$d" ls-files --others --exclude-standard 2>/dev/null | wc -l | tr -d ' ')
  printf '%-48s commits_ahead=%s pushed=%s untracked=%s\n' "$d" "$ahead" "$pushed" "$unt"
done
