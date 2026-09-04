#!/bin/sh
# P11 CP-01 — PEER EVIDENCE INTAKE ENUMERATION
# Declares POPULATION, PATTERN, PATH SET and UNIT before counting.
#
# POPULATION : every ref reachable from origin in TH-PATTARAKRIT/AI-Collaboration-Hub
# PATTERN    : (a) branch name matching the P01..P10 process slugs
#              (b) any tracked path segment matching ^P(0[1-9]|10)_
# PATH SET   : refs/remotes/origin/*  (ALL of them, not a chosen subset)
# UNIT       : one git ref; one tracked file path
set -e
cd "$(git rev-parse --show-toplevel)"
git fetch -q origin 'refs/heads/*:refs/remotes/origin/*'

echo "== A. total remote branches (denominator) =="
git branch -r | grep -v HEAD | wc -l

echo "== B. branches whose name matches a P01..P10 process slug =="
git branch -r | grep -v HEAD | grep -Ei \
 'p2p|procure-to-pay|o2c|order-to-cash|m2c|manufacture-to-cost|a2r|acquire-to-retire|e2p|expense-to-pay|b2r|bank-to-reconcile|tax-to-compliance|th-tax-compliance|r2r|record-to-report|plan-to-analyze|time-based-recognition|core-reconciliation' \
 || echo "(none)"

echo "== C. any tracked path segment matching ^P(0[1-9]|10)_ on ANY ref =="
for b in $(git branch -r | grep -v HEAD | sed 's| *origin/||'); do
  git ls-tree -r --name-only "origin/$b" 2>/dev/null | grep -E '(^|/)P(0[1-9]|10)_'
done | sort -u | sed -n '1,50p'
echo "(end C)"

echo "== D. local peer clone commit counts ahead of origin/SMEsPlus =="
for d in ../ACCOUNT_P0*_2026_09_04_EXECUTION ../ACCOUNT_P1*_2026_09_04_EXECUTION; do
  [ -d "$d/.git" ] || continue
  n=$(git -C "$d" rev-list --count origin/SMEsPlus..HEAD 2>/dev/null || echo NA)
  w=$(git -C "$d" status --porcelain 2>/dev/null | wc -l)
  printf '%s  commits_ahead=%s  worktree_changes=%s  branch=%s\n' \
    "$(basename "$d")" "$n" "$w" "$(git -C "$d" branch --show-current 2>/dev/null)"
done
