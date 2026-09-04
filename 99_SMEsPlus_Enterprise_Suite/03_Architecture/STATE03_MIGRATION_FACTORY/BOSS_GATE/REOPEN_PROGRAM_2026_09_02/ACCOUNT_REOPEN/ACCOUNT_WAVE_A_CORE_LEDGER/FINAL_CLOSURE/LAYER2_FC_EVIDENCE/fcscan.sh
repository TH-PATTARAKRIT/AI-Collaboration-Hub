#!/bin/bash
# FC negative-claim compliance scan. Run from ACCOUNT_WAVE_A_CORE_LEDGER.
scan() {
  local label="$1"; shift
  local dir="$1"; shift
  local n; n=$(find "$dir" -name '*.md' 2>/dev/null | wc -l | tr -d ' ')
  local l; l=$(find "$dir" -name '*.md' -print0 2>/dev/null | xargs -0 cat 2>/dev/null | wc -l | tr -d ' ')
  printf "%-18s files=%-4s lines=%s\n" "$label" "$n" "$l"
}
tok() {
  local dir="$1"; shift
  find "$dir" -name '*.md' -print0 2>/dev/null | xargs -0 cat 2>/dev/null | grep -oiF "$1" | wc -l | tr -d ' '
}
echo "=== MANIFEST ==="
scan "FINAL_CLOSURE" FINAL_CLOSURE
scan "MCC" METHOD_CONVERGENCE_CLOSURE
scan "MC" METHOD_CONVERGENCE
echo
echo "=== UNBOUNDED-NEGATIVE TOKENS (FC vs MCC) ==="
printf "%-22s %-8s %-8s\n" TOKEN FC MCC
for t in "does not exist" "there is no" "no rule" "no constraint" "no such" "nowhere" "impossible" "never occurs"; do
  printf "%-22s %-8s %-8s\n" "$t" "$(tok FINAL_CLOSURE "$t")" "$(tok METHOD_CONVERGENCE_CLOSURE "$t")"
done
echo
echo "=== BOUNDING TOKENS (evidence that negatives carry a declared bound) ==="
printf "%-26s %-8s %-8s\n" TOKEN FC MCC
for t in "declared pattern" "path set" "bounded" "NOT YET SEARCHED" "outside the bound" "NEGATIVE-CLAIM" "class \`A\`" "class \`C\`"; do
  printf "%-26s %-8s %-8s\n" "$t" "$(tok FINAL_CLOSURE "$t")" "$(tok METHOD_CONVERGENCE_CLOSURE "$t")"
done
echo
echo "=== PROHIBITED VERDICT WORDING SCAN (must be zero) ==="
for t in " PASS" "APPROVED" "FINAL APPROVAL" "CERTIFIED"; do
  printf "%-22s FC=%s\n" "$t" "$(tok FINAL_CLOSURE "$t")"
done
