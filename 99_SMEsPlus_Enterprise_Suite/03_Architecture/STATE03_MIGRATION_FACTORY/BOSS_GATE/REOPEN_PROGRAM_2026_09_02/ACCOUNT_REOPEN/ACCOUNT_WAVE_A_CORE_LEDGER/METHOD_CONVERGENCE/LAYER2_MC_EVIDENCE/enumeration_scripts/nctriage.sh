#!/bin/bash
cd "/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT_WAVE_A_MC_2026_09_04_EXECUTION"
P=$(cat /tmp/wavea_path.txt)
SCANNED=$(ls "$P"/[0-2][0-9]_*.md "$P"/CORR1/C[01][0-9]_*.md "$P"/GAPCLOSE/G0[2-5]_*.md 2>/dev/null)
UN=""
for f in $(find "$P" -name "*.md" | sort); do echo "$SCANNED" | grep -qxF "$f" || UN="$UN $f"; done
echo "### HIGH-RISK ABSOLUTE-ABSENCE PHRASING in the 19 unscanned files"
echo "(pattern: absence assertion with a universal-scope qualifier)"
grep -ohiE ".{0,70}(does not exist anywhere|nowhere in|anywhere in the (tree|codebase|system|domain)|no such .{0,30} exists anywhere|in no (module|addon)|never .{0,25} anywhere).{0,50}" $UN 2>/dev/null | sed 's/^ *//' | sort -u | head -30
echo
echo "### COUNT of universal-scope absence phrases"
grep -ohiE "(does not exist anywhere|nowhere in|anywhere in the (tree|codebase|system|domain)|no such .{0,30} exists anywhere)" $UN 2>/dev/null | wc -l
echo
echo "### 'anywhere' hits with context, unscanned set (45 total)"
grep -ohiE ".{0,60}anywhere.{0,60}" $UN 2>/dev/null | sed 's/^ *//' | sort -u | head -25
