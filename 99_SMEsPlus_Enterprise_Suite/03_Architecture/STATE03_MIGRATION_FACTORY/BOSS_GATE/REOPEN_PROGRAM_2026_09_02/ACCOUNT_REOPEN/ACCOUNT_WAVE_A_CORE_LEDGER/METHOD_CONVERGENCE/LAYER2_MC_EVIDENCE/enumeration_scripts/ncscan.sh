#!/bin/bash
cd "/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT_WAVE_A_MC_2026_09_04_EXECUTION"
P=$(cat /tmp/wavea_path.txt)
echo "### CANONICAL PACKAGE FILE COUNT (denominator for the scan)"
find "$P" -name "*.md" | wc -l
echo "-- G06 declared scope: 45 files (01-26, C01-C13, G02-G05) --"
echo
echo "### FILES NOT COVERED BY G06's declared scope"
ls "$P/GAPCLOSE/" "$P/GAPCLOSE/L12_FINAL_REVIEW/" 2>/dev/null | grep -E "^(G06|G07|G08|G09|G10|G11|GR1|GR2)"
ls "$P/CORR1/L12_FRESH_REVIEW/" "$P/CHALLENGE/" "$P/EXPERT_REVIEW/" "$P/LAYER2_EVIDENCE_QUARANTINE/" 2>/dev/null
echo
echo "### NEGATIVE-STRENGTH TOKEN SCAN over the UNSCANNED files"
UNSCANNED=""
for f in GAPCLOSE/G06_ACCOUNT_WAVE_A_NEGATIVE_CLAIM_FINAL_COMPLIANCE_SCAN.md GAPCLOSE/G07_ACCOUNT_WAVE_A_FINAL_L9_SAAS_BOUNDARY_REVIEW.md GAPCLOSE/G08_ACCOUNT_WAVE_A_FINAL_L11_RECONCILIATION_PROOF.md GAPCLOSE/G09_ACCOUNT_WAVE_A_FINAL_L12_INDEPENDENT_REVIEW.md GAPCLOSE/G10_ACCOUNT_WAVE_A_FINAL_GATE_REPORT.md GAPCLOSE/G11_ACCOUNT_WAVE_A_FINAL_EVIDENCE_MANIFEST_SHA256.md "GAPCLOSE/L12_FINAL_REVIEW/GR1_FINAL_GATE_REVIEW_CLOSURE_VALIDITY.md" "GAPCLOSE/L12_FINAL_REVIEW/GR2_FINAL_GATE_REVIEW_CROSS_BOUNDARY.md"; do
  [ -f "$P/$f" ] && UNSCANNED="$UNSCANNED $P/$f"
done
echo "files scanned: $(echo $UNSCANNED | wc -w | tr -d ' ')"
for tok in "never" "always" "cannot" "does not exist" "there is no" "no such" "impossible" "no support" "no control" "no validation"; do
  n=$(grep -ohi "$tok" $UNSCANNED 2>/dev/null | wc -l | tr -d ' ')
  printf "%-20s hits=%s\n" "$tok" "$n"
done
