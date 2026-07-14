# STATE02_STEP03_HASH_EXCEPTION_REGISTER_v1.1.md

Session: SMEPLUS-26-07-14-STEP03-CORR
State: 02 — Governance
Step: 03 — Canonical RACI
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Target Branch: SMEsPlus
Execution Branch: claude/canonical-raci-evidence-xgk851
Prepared By: Claude Code (Responsible role only)
Execution Timestamp: 2026-07-14 (UTC)
Document Status: OPEN — INDEPENDENT VERIFICATION PENDING
Gate Status: HOLD
Supersedes: STATE02_STEP03_HASH_EXCEPTION_REGISTER_v1.0.md (retained unmodified as
historical evidence — HEX-001, HEX-002, HEX-003, all from the prior R1 cycle)

## 1. Purpose

Records every SHA256 discrepancy or scope change found during the Task 3 recalculation
following RC-001..RC-010 application, as an inspectable evidence finding. No discrepancy
is closed by editing a file to force a hash match.

## 2. Exception Register (this cycle)

| Exception ID | File | Type | Prior Hash | Actual Hash | Root Cause | Corrective Action | Boss Approval Req. | Status |
|---|---|---|---|---|---|---|---|---|
| HEX-004 | `APPROVAL_AUTHORITY_MATRIX.md`, `AI_ROLE_AND_RESPONSIBILITY.md`, `ARCHITECTURE_GOVERNANCE_STANDARD.md`, `FOLDER_REGISTRY.yaml` | EXPECTED CHANGE (4 files) | Pre-correction blob SHAs (see `STATE02_SOURCE_CORRECTION_BEFORE_AFTER_REGISTER_v1.0.md`) | Post-correction sha256 values recorded in `STATE02_STEP03_SHA256_MANIFEST_v1.1.txt` §B | RC-001 through RC-007 and RC-009 applied per Boss Decision 2, commit `ff6cb12` | None required — change is Boss-authorized and traceable via before/after register | No (already authorized) | REMEDIATED BY BEFORE/AFTER REGISTER, PENDING INDEPENDENT VERIFICATION |
| HEX-005 | `CANONICAL_ROLE_GLOSSARY.md` | NOT LISTED (new controlled file) | (absent — file did not previously exist) | `da774d889b1a276e1321c5952aab9b2ebe5f6a844d4d2993d33613741d863551` | RC-010 additive glossary created, commit `ff6cb12` | Added to manifest `STATE02_STEP03_SHA256_MANIFEST_v1.1.txt` §B | No (additive, Boss-authorized) | REMEDIATED BY MANIFEST UPDATE, PENDING INDEPENDENT VERIFICATION |
| HEX-006 | `STATE02_CANONICAL_RACI_CORRECTION_RECORD_v1.0.md`, `STATE02_SOURCE_CORRECTION_BEFORE_AFTER_REGISTER_v1.0.md`, `STATE02_SOURCE_CORRECTION_EXECUTION_RECORD_v1.0.md`, `STATE02_SOURCE_CORRECTION_ROLLBACK_PLAN_v1.0.md` | NOT LISTED (new controlled files, 4) | (absent) | See `STATE02_STEP03_SHA256_MANIFEST_v1.1.txt` §A | New evidence records created this session (Tasks 1, 2b) | Added to manifest §A | No | REMEDIATED BY MANIFEST UPDATE, PENDING INDEPENDENT VERIFICATION |
| HEX-007 | `DOCUMENT_REGISTRY.yaml` | INFORMATIONAL — scope addition, no content change | Not previously included in a Step 03 hash manifest | `49adead252d3576286a1bbfaca15fa27dc9f7b8ee787dc3b053051fed7fccbdb` | RC-008 required re-inspection of this file; it was not previously in the Step 03 manifest scope even though it was inspected in `STATE02_SOURCE_GOVERNANCE_CONFLICT_REGISTER_v1.0.md` §3 | Added to manifest §B for completeness; file content NOT modified | No | INFORMATIONAL — NO ACTION BEYOND RECORD |

## 3. Carried Forward From v1.0

```text
HEX-001 (STATE02_RACI_REVIEW_RECORD_v1.0.md, MISMATCH) — REMEDIATED BY R1 MANIFEST,
  PENDING INDEPENDENT VERIFICATION (unchanged this cycle; hash still MATCH against
  current manifest — see reverification record).
HEX-002 (STATE02_RACI_SECRETARY_REVIEW_AND_CORRECTION_RECORD_v1.0.md, NOT LISTED) —
  REMEDIATED BY R1 MANIFEST, PENDING INDEPENDENT VERIFICATION (unchanged this cycle).
HEX-003 (PACKAGE_MANIFEST_SHA256_STATE02_STEP03_RACI.txt, INFORMATIONAL) — NO ACTION
  BEYOND RECORD (unchanged this cycle).
```

## 4. Disposition Rules Applied

```text
Prior manifests (v1.0, v1.1 pre-this-cycle) = retained UNMODIFIED as historical evidence.
Current manifest (v1.1, this cycle)          = authoritative recalculated baseline.
No source or package file was edited to force a hash match.
HASH RESULT remains HOLD until an Independent Evidence Verifier confirms the manifest.
```

## 5. Control Statement

These exceptions are documentation/process-control findings arising from Boss-authorized,
traceable changes. They are not unexplained defects and do not lift or lower any
authority. The package is NOT marked Fully Verified — only the Independent Evidence
Verifier may record that result. Gate remains HOLD. Boss remains Sole Final Approver.
