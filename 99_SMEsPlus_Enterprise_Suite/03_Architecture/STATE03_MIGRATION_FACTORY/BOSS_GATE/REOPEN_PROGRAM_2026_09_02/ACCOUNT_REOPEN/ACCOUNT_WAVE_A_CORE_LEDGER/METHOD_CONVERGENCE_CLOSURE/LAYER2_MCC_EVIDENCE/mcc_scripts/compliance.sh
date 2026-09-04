#!/bin/bash
D="/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT_WAVE_A_MCC_2026_09_04_EXECUTION/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/ACCOUNT_WAVE_A_CORE_LEDGER/METHOD_CONVERGENCE_CLOSURE"
cd "$D" || exit 1
echo "### 1. Uppercase PASS token (case-sensitive), excluding the 4 legitimate forms"
grep -rn "PASS" --include='*.md' . | grep -vE "RECOMMEND PASS|CONDITIONAL PASS|exclude .*PASS|excludes \`PASS\`|the word \`PASS\`|forbidden|No \`PASS\` is declared|not \`PASS\`|Why not \`PASS\`|allowed" 
echo "  ^ (blank = clean)"
echo
echo "### 2. Approval / gate-movement wording"
grep -rniE "final approv|is approved|we approve|sign-?off|gate (is )?(open|cleared|moved|passed)|authoris(ed|ation) to (implement|develop|deploy)|ready for (development|team b|team c|implementation)|wave a (is )?(closed|complete|final)" --include='*.md' . | grep -viE "no ai may|sole final approver|not declared|forbidden|may not|cannot|Boss will|Boss decides|Boss ratifies|Boss is the"
echo "  ^ (blank = clean)"
echo
echo "### 3. Self-declared convergence"
grep -rn "CONVERGED" --include='*.md' . | grep -vE "NOT CONVERGED|\`CONVERGED\`|reverts? from|status|reaching|to \`?CONVERGED|convicted"
echo "  ^ (blank = clean)"
echo
echo "### 4. Required terminal-state and disclaimer presence"
for f in MCC_A_CANONICAL_BASELINE_RECONCILIATION.md MCC_B_GB03_ROOT_CLOSURE.md MCC_C_FX08_MCU13_FORENSIC_REVERIFICATION.md MCC_D_GATING_UNKNOWN_EXHAUSTION_REGISTER.md MCC_E_DENOMINATOR_RECONCILIATION.md MCC_F_NEGATIVE_CLAIM_EXHAUSTION.md MCC_G_BALANCED_BUT_WRONG_FIXED_POINT_PROOF.md MCC_H_FIXED_POINT_CONVERGENCE_PROOF.md MCC_I_MC01_MC10_TARGETED_RERUN.md MCC_K_REUSABLE_METHOD_DELTA.md; do
  d=$(grep -c "Boss is the sole Final Approver\|Boss ratifies\|Boss will decide" "$f")
  printf "%-58s disclaimer=%s\n" "$f" "$d"
done
