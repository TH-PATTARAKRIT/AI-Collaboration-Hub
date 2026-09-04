#!/bin/bash
cd "/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT_WAVE_A_MC_2026_09_04_EXECUTION"
MC=$(cat /tmp/mc_path.txt)
OUT="$MC/12_ACCOUNT_WAVE_A_METHOD_CONVERGENCE_EVIDENCE_MANIFEST_SHA256.md"
{
echo "# 12 — ACCOUNT WAVE A — METHOD CONVERGENCE EVIDENCE MANIFEST (SHA-256)"
echo
echo "Session \`SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001\`"
echo "Branch \`research/account-wave-a-mc-2026-09-04-001\` · Parent baseline commit \`56288c4\`"
echo "Generated 2026-09-04"
echo
echo "## 1. Layer 1 — clean-room deliverables"
echo
echo "| File | Lines | SHA-256 |"
echo "|---|---|---|"
for f in "$MC"/*.md; do
  [ "$f" = "$OUT" ] && continue
  printf "| \`%s\` | %s | \`%s\` |\n" "$(basename "$f")" "$(wc -l < "$f" | tr -d ' ')" "$(shasum -a 256 "$f" | cut -d' ' -f1)"
done
echo
echo "## 2. Layer 2 — audit quarantine"
echo
echo "| File | Lines | SHA-256 |"
echo "|---|---|---|"
for f in "$MC"/LAYER2_MC_EVIDENCE/*.md; do
  printf "| \`LAYER2_MC_EVIDENCE/%s\` | %s | \`%s\` |\n" "$(basename "$f")" "$(wc -l < "$f" | tr -d ' ')" "$(shasum -a 256 "$f" | cut -d' ' -f1)"
done
echo
echo "## 3. Parent baseline under review — hashes as read this session"
echo
echo "| File | SHA-256 |"
echo "|---|---|"
P=$(cat /tmp/wavea_path.txt)
for f in "$P/02_ACCOUNT_WAVE_A_FUNCTION_COVERAGE_REGISTER.md" "$P/16_L9_ACCOUNT_WAVE_A_SAAS_BOUNDARY_REGISTER.md" "$P/20_ACCOUNT_WAVE_A_CONTRADICTION_REGISTER.md" "$P/21_ACCOUNT_WAVE_A_UNKNOWN_EVIDENCE_GAP_REGISTER.md" "$P/GAPCLOSE/G06_ACCOUNT_WAVE_A_NEGATIVE_CLAIM_FINAL_COMPLIANCE_SCAN.md" "$P/GAPCLOSE/G08_ACCOUNT_WAVE_A_FINAL_L11_RECONCILIATION_PROOF.md" "$P/GAPCLOSE/G09_ACCOUNT_WAVE_A_FINAL_L12_INDEPENDENT_REVIEW.md" "$P/GAPCLOSE/G10_ACCOUNT_WAVE_A_FINAL_GATE_REPORT.md" "$P/GAPCLOSE/L12_FINAL_REVIEW/GR1_FINAL_GATE_REVIEW_CLOSURE_VALIDITY.md" "$P/GAPCLOSE/L12_FINAL_REVIEW/GR2_FINAL_GATE_REVIEW_CROSS_BOUNDARY.md"; do
  [ -f "$f" ] && printf "| \`%s\` | \`%s\` |\n" "$(echo "$f" | sed "s|$P/||")" "$(shasum -a 256 "$f" | cut -d' ' -f1)"
done
echo
echo "## 4. Enumeration scripts — repeatability basis (\`MC-04\`)"
echo
echo "Retained at session scratchpad \`enum/\`. Each is a single-pass mechanical command set over a"
echo "declared path set; none depends on judgement. Command forms are reproduced in Layer 2"
echo "\`MCE01\` so that the method is reusable without access to this session."
echo
echo "| Script | Purpose | SHA-256 |"
echo "|---|---|---|"
S="$MC/LAYER2_MC_EVIDENCE/enumeration_scripts"
for f in "$S"/*.sh; do
  printf "| \`%s\` | enumeration | \`%s\` |\n" "$(basename "$f")" "$(shasum -a 256 "$f" | cut -d' ' -f1)"
done
echo
echo "## 5. Primary evidence sources"
echo
echo "| Ref | Location | Access |"
echo "|---|---|---|"
echo "| \`SRC-A\` | Reference ERP accounting addon, v18 line, build 20250608 | Read, verified this session |"
echo "| \`SRC-C\` | Framework base models and security | Read, verified this session |"
echo "| \`SRC-E\` | Framework ORM core | Read, verified this session |"
echo "| \`SRC-F\` | Whole addons tree — bounding scope for negative claims, **791 directories** | Read, verified this session |"
echo
echo "> \`SRC-F\` is recorded at **791**, correcting the figure of 797 stated in \`MCE00\`."
echo "> The searches ran over the real tree; only the stated denominator was wrong. See \`MCE02\` \`MCX-04\`."
echo
echo "## 6. Integrity statement"
echo
echo "No file of the parent baseline was modified by this session. \`MCE00\` is retained unedited;"
echo "\`MCE02\` records every contradiction to it and governs where they conflict, per \`DR-NC-06\`."
echo "No source code was modified. Nothing was merged or deployed."
} > "$OUT"
wc -l "$OUT"
