#!/bin/bash
cd "/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT_WAVE_A_MC_2026_09_04_EXECUTION"
P=$(cat /tmp/wavea_path.txt)
# G06 declared scope: parent 01-26, CORR1 C01-C13, GAPCLOSE G02-G05
SCANNED=$(ls "$P"/[0-2][0-9]_*.md "$P"/CORR1/C[01][0-9]_*.md "$P"/GAPCLOSE/G0[2-5]_*.md 2>/dev/null)
ALL=$(find "$P" -name "*.md" | sort)
echo "ALL files: $(echo "$ALL" | wc -l | tr -d ' ')  lines: $(cat $(echo "$ALL") 2>/dev/null | wc -l | tr -d ' ')"
echo "G06-SCANNED files: $(echo "$SCANNED" | wc -l | tr -d ' ')  lines: $(cat $SCANNED 2>/dev/null | wc -l | tr -d ' ')"
echo
echo "### UNSCANNED FILE LIST + LOC"
for f in $ALL; do
  if ! echo "$SCANNED" | grep -qxF "$f"; then
    printf "%6s  %s\n" "$(wc -l < "$f" | tr -d ' ')" "$(echo "$f" | sed "s|$P/||")"
  fi
done | sort -rn
