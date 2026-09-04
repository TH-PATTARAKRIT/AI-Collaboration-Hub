#!/bin/bash
cd "/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT_WAVE_A_MC_2026_09_04_EXECUTION"
P=$(cat /tmp/wavea_path.txt)
SCANNED=$(ls "$P"/[0-2][0-9]_*.md "$P"/CORR1/C[01][0-9]_*.md "$P"/GAPCLOSE/G0[2-5]_*.md 2>/dev/null)
UN=""
for f in $(find "$P" -name "*.md" | sort); do echo "$SCANNED" | grep -qxF "$f" || UN="$UN $f"; done
echo "### Token counts over the 19 UNSCANNED files"
T=0
for tok in "never" "always" "cannot" "does not exist" "there is no" "no such" "impossible" "no support" "no control" "no validation" "anywhere"; do
  n=$(grep -ohi "$tok" $UN 2>/dev/null | wc -l | tr -d ' ')
  T=$((T+n)); printf "%-18s %5s\n" "$tok" "$n"
done
echo "TOTAL RAW HITS: $T"
echo
echo "### Per-file raw hit density"
for f in $UN; do
  n=$(grep -ohiE "never|always|cannot|does not exist|there is no|no such|impossible|no support|no control|no validation|anywhere" "$f" 2>/dev/null | wc -l | tr -d ' ')
  printf "%5s  %s\n" "$n" "$(echo "$f" | sed "s|$P/||")"
done | sort -rn
