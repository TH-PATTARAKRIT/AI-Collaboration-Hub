#!/bin/bash
# GB-08 re-runnable evidence script.
#
# Declared population : every directory under $VOL containing addons/base/models/res_currency.py
# Declared pattern    : the literal path suffix "addons/base/models/res_currency.py"
# Declared unit       : one directory = one "reference core root"
# Declared path set   : whatever that pattern returns under $VOL, unfiltered, unranked
#
# It prints, and nothing here is author-chosen:
#   1. the discovered root set and its cardinality
#   2. which roots are nested inside other roots (the unit is NOT disjoint)
#   3. the SHA-256 of each root's res_currency.py  -> the number of DISTINCT variants
#   4. the D1 branch-preference test, twice: by comment string and structurally by root_id
#   5. the D3 sum_currency test
#   6. manifested-module counts per root
#
# Usage:  VOL=/Volumes/iMacSys bash gb08_evidence.sh
set -u
VOL="${VOL:-/Volumes/iMacSys}"
cd "$VOL" || exit 1

ROOTS=$(find . -type f -path "*/addons/base/models/res_currency.py" 2>/dev/null \
        | sed 's|/addons/base/models/res_currency.py$||' | sort)
N=$(printf '%s\n' "$ROOTS" | grep -c .)

echo "== 1. POPULATION =="
echo "volume        : $VOL"
echo "pattern       : */addons/base/models/res_currency.py"
echo "roots found   : $N"
printf '%s\n' "$ROOTS" | cat -n
echo

echo "== 2. NESTING (roots are not disjoint) =="
printf '%s\n' "$ROOTS" | while IFS= read -r a; do
  printf '%s\n' "$ROOTS" | while IFS= read -r b; do
    [ "$a" = "$b" ] && continue
    case "$b" in "$a"/*) echo "CONTAINS: $a  ->  $b";; esac
  done
done
echo

echo "== 3/4/5. PER-ROOT TESTS =="
printf '%-3s %-14s %-12s %-13s %-9s %-7s %s\n' "#" "SHA256(12)" "D1-string" "D1-structural" "D3-files" "modules" "root"
i=0
printf '%s\n' "$ROOTS" | while IFS= read -r r; do
  i=$((i+1))
  f="$r/addons/base/models/res_currency.py"
  sha=$(shasum -a 256 "$f" 2>/dev/null | cut -c1-12)
  if grep -q 'Get rates through branch if selected company' "$f" 2>/dev/null; then s1=PRESENT; else s1=ABSENT; fi
  body=$(awk '/def _get_conversion_rate/{flag=1} flag{print} flag&&/return/{c++; if(c>=2) exit}' "$f" 2>/dev/null)
  if printf '%s' "$body" | grep -q 'root_id'; then s2=ROOT_ID_PREF; else s2=plain; fi
  d3=$(grep -rl "sum_currency" "$r" 2>/dev/null | grep -c .)
  mods=$(find "$r" -name "__manifest__.py" -type f 2>/dev/null | grep -c .)
  printf '%-3s %-14s %-12s %-13s %-9s %-7s %s\n' "$i" "$sha" "$s1" "$s2" "$d3" "$mods" "$r"
done
echo

echo "== 6. RESOLVER UNIQUENESS (res.currency._get_rates / _get_conversion_rate) =="
printf '%s\n' "$ROOTS" | while IFS= read -r r; do
  grep -rn "def _get_rates(self, company, date)\|def _get_conversion_rate(self, from_currency" "$r" --include="*.py" 2>/dev/null
done | sed "s|$VOL||" | sort -u
