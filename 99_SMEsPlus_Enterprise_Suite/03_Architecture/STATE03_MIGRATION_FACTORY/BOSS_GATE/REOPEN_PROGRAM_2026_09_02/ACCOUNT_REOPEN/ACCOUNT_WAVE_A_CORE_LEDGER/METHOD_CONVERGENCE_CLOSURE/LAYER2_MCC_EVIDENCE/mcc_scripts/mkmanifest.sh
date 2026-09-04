#!/bin/bash
# Generates ACCOUNT_WAVE_A_MCC_EVIDENCE_MANIFEST_SHA256.md over the MCC package.
D="/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT_WAVE_A_MCC_2026_09_04_EXECUTION/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/ACCOUNT_WAVE_A_CORE_LEDGER/METHOD_CONVERGENCE_CLOSURE"
OUT="$D/ACCOUNT_WAVE_A_MCC_EVIDENCE_MANIFEST_SHA256.md"
cd "$D" || exit 1
{
echo "# ACCOUNT WAVE A — MCC EVIDENCE MANIFEST (SHA-256)"
echo
echo 'Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Branch `research/account-wave-a-mcc-2026-09-04-001`'
echo 'Parent commit `33cdc6fa009c4eafcca543c253ccad19e97fd0dc`'
echo "Generated $(date -u +%Y-%m-%dT%H:%M:%SZ) UTC"
echo
echo '> Reproduce with: `shasum -a 256 <file>` from the package directory.'
echo '> The manifest excludes itself.'
echo
echo "## Layer 1 — clean-room deliverables"
echo
echo "| SHA-256 | Lines | File |"
echo "|---|---|---|"
find . -maxdepth 1 -name '*.md' ! -name 'ACCOUNT_WAVE_A_MCC_EVIDENCE_MANIFEST_SHA256.md' | sort | while read -r f; do
  printf '| `%s` | %s | `%s` |\n' "$(shasum -a 256 "$f" | cut -d' ' -f1)" "$(wc -l < "$f" | tr -d ' ')" "${f#./}"
done
echo
echo "## Layer 2 — audit quarantine (vendor tokens; Boss / PMO / AI-Audit only)"
echo
echo "| SHA-256 | Lines | File |"
echo "|---|---|---|"
find ./LAYER2_MCC_EVIDENCE -type f | sort | while read -r f; do
  printf '| `%s` | %s | `%s` |\n' "$(shasum -a 256 "$f" | cut -d' ' -f1)" "$(wc -l < "$f" | tr -d ' ')" "${f#./}"
done
echo
echo "## Package roll-up"
echo
N=$(find . -type f ! -name 'ACCOUNT_WAVE_A_MCC_EVIDENCE_MANIFEST_SHA256.md' | wc -l | tr -d ' ')
L=$(find . -type f ! -name 'ACCOUNT_WAVE_A_MCC_EVIDENCE_MANIFEST_SHA256.md' | tr '\n' '\0' | xargs -0 cat | wc -l | tr -d ' ')
R=$(find . -type f ! -name 'ACCOUNT_WAVE_A_MCC_EVIDENCE_MANIFEST_SHA256.md' | sort | tr '\n' '\0' | xargs -0 shasum -a 256 | shasum -a 256 | cut -d' ' -f1)
echo "| Measure | Value |"
echo "|---|---|"
echo "| Files | **$N** |"
echo "| Lines | **$L** |"
echo "| **Roll-up digest** (SHA-256 of the sorted per-file digest list) | \`$R\` |"
echo
echo "## Parent-package integrity — verified unmodified by this session"
echo
echo "| Check | Result |"
echo "|---|---|"
cd "$D/../../../../../../../../.." 2>/dev/null || cd "/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT_WAVE_A_MCC_2026_09_04_EXECUTION"
DIRTY=$(git status --porcelain | grep -v 'METHOD_CONVERGENCE_CLOSURE' | wc -l | tr -d ' ')
echo "| Tracked files modified outside the MCC package | **$DIRTY** |"
echo "| Parent commit reachable from HEAD | **$(git merge-base --is-ancestor 33cdc6fa009c4eafcca543c253ccad19e97fd0dc HEAD && echo yes || echo no)** |"
} > "$OUT"
echo "written: $OUT"
