#!/bin/bash
D="/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT_WAVE_A_MCC_2026_09_04_EXECUTION/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/ACCOUNT_WAVE_A_CORE_LEDGER/METHOD_CONVERGENCE_CLOSURE"
cd "$D" || exit 1
NOTE='
---

> ### FIGURE-GOVERNANCE NOTICE — appended mechanically, package-wide
>
> **`MCC_00_CANONICAL_FIGURES_REGISTER.md` governs every published figure and disposition in this
> package.** Where a figure in this file differs from a row in `MCC_00`, **`MCC_00` governs**; the text
> here stands unedited so the lineage is visible (`DR-NC-06`).
>
> This notice was appended to **every** Layer-1 file by one command, after the independent audit panel
> found that this round had failed to propagate its own last correction to three of its own files
> (`MCC_J` `J-16`). It is the mechanism, not the intention, that `ER-CORE-3` requires.'
for f in MCC_A_CANONICAL_BASELINE_RECONCILIATION.md MCC_B_GB03_ROOT_CLOSURE.md MCC_C_FX08_MCU13_FORENSIC_REVERIFICATION.md MCC_D_GATING_UNKNOWN_EXHAUSTION_REGISTER.md MCC_E_DENOMINATOR_RECONCILIATION.md MCC_F_NEGATIVE_CLAIM_EXHAUSTION.md MCC_G_BALANCED_BUT_WRONG_FIXED_POINT_PROOF.md MCC_H_FIXED_POINT_CONVERGENCE_PROOF.md MCC_I_MC01_MC10_TARGETED_RERUN.md MCC_J_FRESH_EXPERT_AND_AUDIT_CHALLENGE.md MCC_K_REUSABLE_METHOD_DELTA.md ACCOUNT_WAVE_A_MCC_MASTER_RECONCILIATION.md; do
  if [ -f "$f" ]; then printf '%s\n' "$NOTE" >> "$f"; echo "appended: $f"; fi
done
echo
echo "=== VERIFY: every Layer-1 file carries the notice ==="
for f in *.md; do
  [ "$f" = "MCC_00_CANONICAL_FIGURES_REGISTER.md" ] && continue
  [ "$f" = "ACCOUNT_WAVE_A_MCC_EVIDENCE_MANIFEST_SHA256.md" ] && continue
  printf "%-58s %s\n" "$f" "$(grep -c 'FIGURE-GOVERNANCE NOTICE' "$f")"
done
