> GROUP A — Sales + Inventory + Purchase Integrated Backbone | EXPERT IBPV — Formal Re-Verification RV-011

# 02 — CORR-010 PACKAGE INTEGRITY AND SHA-256 REPRODUCTION

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-011-D02`

## 00 — Method

`shasum -a 256` was independently run against the working tree at
`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_B_DESIGN/GROUP_A_SALES_INVENTORY_PURCHASE/`
checked out at CORR-010's frozen executor commit `e44186448eaae38926a78447639d6fa693cc1a6f`, for every file
CORR-010's own manifest (`CORRECTIVE_CORR_010/38_CORR010_FINAL_SHA256_MANIFEST.txt`) lists — files 01–21,
`CORRECTIVE_CORR_008/22–28`, `CORRECTIVE_CORR_010/29–37`. This reproduction was **not** taken from file 38's own
text; it was independently computed against the live files and only then diffed against file 38's claimed values.

## 01 — Result: 37/37 Exact Match

| Check | Result |
|---|---|
| Files listed in CORR-010 manifest (file 38) | 37 |
| Files independently hashed by this session | 37 |
| Hash mismatches | **0** |
| Missing paths (listed in manifest, absent on disk) | **0** |
| Extra paths (present on disk, not in manifest, within the CORR-010 scope) | **0** |
| Duplicate path entries | **0** |

Full independent SHA-256 output is reproduced verbatim in this deliverable's own working notes and matches file
38 byte-for-byte across all 37 entries; a machine diff (`diff` between the sorted computed list and the sorted
claimed list) returned **zero lines** — the strongest form of independent confirmation available short of a
third-party witness.

**PASS — 37/37.**

## 02 — File 38's Self-Reference Limitation — Independently Confirmed Correct

File 38 states it cannot hash itself, and instead states its own integrity is verifiable only via its git blob/
commit SHA. This is the same limitation file 21 and file 28 (the two prior-package manifests) each state for
themselves. Independently confirmed accurate: a manifest that hashed itself would be self-referentially
inconsistent the instant its own hash entry were written. No defect found in this framing.

## 03 — Files 21 and 28 — Historical Manifests, Not Overwritten

CORR-010 claims files 21 (`21_TEAM_B_FINAL_SHA256_MANIFEST.txt`, the pre-CORR-008 manifest) and 28
(`CORRECTIVE_CORR_008/28_TEAM_B_CORR008_FINAL_SHA256_MANIFEST.txt`, the pre-CORR-010 manifest) were intentionally
left unmodified as historical evidence.

Independently checked with `git diff <original-commit> <CORR-010-final> -- <file>`:

- `git diff b98a3b9f... e441864... -- .../21_TEAM_B_FINAL_SHA256_MANIFEST.txt` → **empty**. File 21 is
  byte-identical to its state at the original TEAM B design commit.
- `git diff 359f96c0... e441864... -- .../CORRECTIVE_CORR_008/28_TEAM_B_CORR008_FINAL_SHA256_MANIFEST.txt` →
  **empty**. File 28 is byte-identical to its state at the CORR-008 frozen-input commit.

**Confirmed: neither historical manifest was overwritten. VERIFIED.**

## 04 — Scope Boundary — No Unrelated File in the Corrective Delta

`git diff --stat b2f7cbd3131963fca176a0ac0939c4bdf8af3e25 e44186448eaae38926a78447639d6fa693cc1a6f` (RV-009 final
→ CORR-010 final) was independently run against the whole repository, not filtered to the GROUP A folder. Result:
**21 files changed, 982 insertions(+), 41 deletions(-)**, every single path under
`TEAM_B_DESIGN/GROUP_A_SALES_INVENTORY_PURCHASE/` — 11 base design files (`04`, `05`, `06`, `07`, `08`, `09`,
`10`, `12`, `13`, `18`, `19`) plus 10 new files (`CORRECTIVE_CORR_010/29`–`38`). Zero paths touch TEAM A
evidence, prior Formal IBPV (RV-009) deliverables, Domain-01 (Accounting Core) evidence, or any file outside
GROUP A. **Matches CORR-010's own claimed scope exactly, independently confirmed — VERIFIED.**

## 05 — No TEAM B/TEAM A/Prior-IBPV Artifact Edited by This Session

`git status` at the time of writing this deliverable shows only new, untracked files under
`EXPERT_IBPV/GROUP_A_SALES_INVENTORY_PURCHASE/FORMAL_REVERIFICATION_RV_011/`. No existing file in the repository
was modified by this session.

## 06 — Overall Integrity Verdict

**VERIFIED.** CORR-010's package integrity claim is independently reproduced in full: hash-for-hash manifest
match, correct historical-manifest preservation, and a scope-clean corrective delta. This deliverable establishes
that CORR-010's *evidence package* is what it claims to be; it does not by itself establish that CORR-010's
*design closures* are substantively correct — that is independently re-performed in Deliverables 04–08.
