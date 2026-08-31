# 02 — RV-009 Corrected Package Integrity and SHA Reproduction

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009-D02`
Project: SMEsPlus ENTERPRISE SUITE · STATE03 — Architecture · GROUP A — Sales + Inventory + Purchase
Execution Function: EXPERT IBPV · Session: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009`

## 1. Reproduction Method

TEAM B's own manifest (`CORRECTIVE_CORR_008/28_TEAM_B_CORR008_FINAL_SHA256_MANIFEST.txt`) states its exact reproduction command. This session re-ran that identical command independently, from a clean working tree checked out at the frozen commit `359f96c0cfee2f74955fe7e8f1d0110ec21a0a45` on the dedicated branch, without modification:

```
cd 99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_B_DESIGN/GROUP_A_SALES_INVENTORY_PURCHASE
shasum -a 256 01_*.md 02_*.md 03_*.md 04_*.md 05_*.md 06_*.md 07_*.md 08_*.md 09_*.md 10_*.md 11_*.md 12_*.md \
  13_*.md 14_*.md 15_*.md 16_*.md 17_*.md 18_*.md 19_*.md 20_*.md 21_*.txt \
  CORRECTIVE_CORR_008/22_*.md CORRECTIVE_CORR_008/23_*.md CORRECTIVE_CORR_008/24_*.md \
  CORRECTIVE_CORR_008/25_*.md CORRECTIVE_CORR_008/26_*.md CORRECTIVE_CORR_008/27_*.md
```

## 2. Result

**PASS — 27/27 files present, 27/27 hashes match exactly**, byte-for-byte, between this session's independent recomputation and TEAM B's claimed manifest (file 28). All 27 hashes are standard 64-hex-character SHA-256 digests (independently length-checked, not merely visually compared). Diff of the two hash lists, sorted, produced zero differences.

File 28's own stated limitation was independently confirmed correct: it hashes files 01–27 and explicitly does not (cannot) hash itself; its own integrity is verifiable only via git blob/commit SHA, not a self-referential manifest entry. This session accepts that limitation as structurally sound, not a gap.

## 3. File 21 (Pre-Correction Manifest) Unchanged Verification

`CORRECTIVE_CORR_008/28` claims file `21_TEAM_B_FINAL_SHA256_MANIFEST.txt` (the historical pre-correction manifest) was intentionally not overwritten. Independently confirmed by diffing the current working-tree copy of file 21 against `git show b98a3b9fb435845dbd15fae79db63b0b73a82420:.../21_TEAM_B_FINAL_SHA256_MANIFEST.txt` (the original pre-correction commit): **zero differences — file 21 is byte-identical to its original, pre-correction form.**

## 4. Ancestry / Delta Verification — Exact Changed-File Set

`git diff --stat b98a3b9fb435845dbd15fae79db63b0b73a82420 359f96c0cfee2f74955fe7e8f1d0110ec21a0a45` independently reproduces the following exact change set (1,443 insertions, 66 deletions across 20 files):

**13 corrected baseline files** (matches the governing prompt's §7 claim of "13 TEAM B baseline files changed by CORR-008" exactly):
`03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md`, `04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md`, `05_INVENTORY_CORE_CANONICAL_DESIGN.md`, `07_PURCHASE_CANONICAL_DESIGN.md`, `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md`, `09_CANONICAL_BUSINESS_EVENT_CATALOG.md`, `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md`, `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md`, `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md`, `14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md`, `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md`, `19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md`, `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md`.

**7 new corrective deliverables** (files 22–28, `CORRECTIVE_CORR_008/`), matching the governing prompt's §3.4 mandatory list exactly, plus the manifest.

**Files independently confirmed unchanged**: `01`, `02`, `06`, `11`, `15`, `16`, `17`, `21`. This matters directly to Deliverable 09 (TBRAC/Accounting boundary) — files `15` (Accounting interface) and `16` (Thailand reality register) being untouched is a load-bearing fact for that deliverable's conclusions, independently confirmed here.

## 5. Cross-Team Artifact Isolation

`git diff --name-only b98a3b9fb435845dbd15fae79db63b0b73a82420 359f96c0cfee2f74955fe7e8f1d0110ec21a0a45` filtered for any path outside `GROUP_A_SALES_INVENTORY_PURCHASE/` (including `CORRECTIVE_CORR_007/`, which was superseded, not reused) returned **zero results**. No TEAM A evidence file, no prior Formal IBPV (FV-006) file, and no other domain-group or domain artifact was modified by CORR-008.

## 6. Overall Integrity Verdict

**VERIFIED.** The corrected package's manifest is honest and reproducible; its ancestry is a clean, isolated, linear correction of the frozen TEAM B baseline with no scope leakage. This verdict is strictly about integrity/reproducibility — it says nothing about whether the corrected *design content* actually closes the nine claimed findings. That question is answered independently in Deliverables 03–12.
