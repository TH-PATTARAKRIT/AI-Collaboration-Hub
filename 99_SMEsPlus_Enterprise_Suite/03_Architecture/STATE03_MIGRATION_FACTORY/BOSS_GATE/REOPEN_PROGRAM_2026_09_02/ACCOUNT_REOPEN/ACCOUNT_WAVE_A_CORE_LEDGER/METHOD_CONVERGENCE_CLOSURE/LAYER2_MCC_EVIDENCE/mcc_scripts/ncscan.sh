#!/bin/bash
P="$1"
echo "=== MANIFEST: files in scope ==="
MCFILES=$(find "$P/METHOD_CONVERGENCE" -name '*.md' | sort)
MCCFILES=$(find "$P/METHOD_CONVERGENCE_CLOSURE" -name '*.md' 2>/dev/null | sort)
echo "MC package files:  $(echo "$MCFILES" | grep -c .)"
echo "MCC package files: $(echo "$MCCFILES" | grep -c .)"
echo "MC lines:  $(cat $MCFILES 2>/dev/null | wc -l)"
echo "MCC lines: $(cat $MCCFILES 2>/dev/null | wc -l)"
echo
echo "=== TOKEN LOAD (literal English) ==="
for t in "does not exist" "there is no" "never" "always" "cannot" "impossible" "no validation" "no control" "no rule" "no constraint" "unsupported" "unreachable" "anywhere" "none of" "no such"; do
  a=$(cat $MCFILES 2>/dev/null | grep -oic "$t" | paste -sd+ - | bc 2>/dev/null)
  b=$(cat $MCCFILES 2>/dev/null | grep -oic "$t" | paste -sd+ - | bc 2>/dev/null)
  printf "%-18s MC=%-5s MCC=%-5s\n" "$t" "${a:-0}" "${b:-0}"
done
echo
echo "=== SEMANTIC-EQUIVALENT LOAD (completeness assertions) ==="
for t in "complete" "exhaustive" "the only" "in every case" "bounded" "closed" "all of" "every " "fully" "entire"; do
  a=$(cat $MCFILES 2>/dev/null | grep -oic "$t" | paste -sd+ - | bc 2>/dev/null)
  b=$(cat $MCCFILES 2>/dev/null | grep -oic "$t" | paste -sd+ - | bc 2>/dev/null)
  printf "%-18s MC=%-5s MCC=%-5s\n" "$t" "${a:-0}" "${b:-0}"
done
