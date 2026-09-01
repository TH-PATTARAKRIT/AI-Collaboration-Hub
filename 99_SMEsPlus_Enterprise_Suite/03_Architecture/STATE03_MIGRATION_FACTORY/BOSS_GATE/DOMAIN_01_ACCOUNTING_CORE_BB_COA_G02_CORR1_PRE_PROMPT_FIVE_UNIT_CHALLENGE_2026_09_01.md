# [SMEPLUS-26-09-01-COA-G02-CORR1-PRE-001]
# COA-G02 CORR1 — Five-Unit Pre-Prompt Challenge for SI Evidence-Record Correction / L999.999

Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain: DOMAIN_01 Accounting Core / COA
Gate: COA-G02 — Base COA Kernel Discovery
Risk Class: HIGH — Gate-affecting Accounting Governance Correction
Boss: Sole Final Approver

## 1. Triggering Independent Audit

Independent Audit commit:

`d452ecc8fc826ed9d07b738ff5a5efc9028a633e`

Terminal disposition:

`COA-G02 = HOLD / CORRECTION REQUIRED`

Substantive audit result:

`36-CONCEPT BASE COA KERNEL CANDIDATE = INDEPENDENTLY SUPPORTED`

Open blocking findings:

- `G02-AUD-01` — mandatory SaaS Invariant evidence-record fields missing from `COA_G02_SAAS_INVARIANT_COMPLIANCE.md`.
- `G02-AUD-02` — `COA_G02_GATE_REPORT.md` does not contain the mandatory explicit SI-01..SI-10 Gate matrix.

The audit explicitly found no accounting-semantic defect requiring redesign of the 36-concept candidate.

## 2. Boss Cross-Gate SaaS Invariant Control

Controlling Boss ruling:

`DOMAIN_01_ACCOUNTING_CORE_AO_BOSS_CROSS_GATE_SAAS_INVARIANTS_RULING.md`

Every SI-01..SI-10 Gate record must include:

1. applicability to the Gate;
2. evidence location;
3. owner / owner role;
4. reviewer / verifier;
5. verification status;
6. conflict / exception if any;
7. Gate impact.

Allowed verification status vocabulary only:

- `PASS / VERIFIED`
- `HOLD / EVIDENCE REQUIRED`
- `FAIL / FROZEN`
- `N/A — JUSTIFICATION REQUIRED`

## 3. Five-Unit Challenge

### 3.1 Audit VETO

Status: `NO VETO — PROCEED WITH TARGETED CORRECTION ONLY`

Opinion:

- Correction scope is mechanically clear from G02-AUD-01 and G02-AUD-02.
- Do not reopen the 36-concept semantic result.
- Do not convert the correction into a new design round.
- Every SI row must use the exact Boss-required fields and allowed status vocabulary.
- Corrected Team B artifacts must stop for fresh targeted Independent Re-audit.
- Team B must not self-declare G02 PASS or READY FOR PMO.

Primary risk: correcting prose while leaving the Boss-required evidence structure incomplete.

### 3.2 TBRAC

Status: `PROCEED — NO NEW THAILAND ACCOUNTING CLAIMS`

Opinion:

- CORR1 is governance/evidence-record correction only.
- Do not add new statutory interpretations for VAT, WHT, CIT or Thai financial reporting.
- Existing G02 substantive Thai-accounting conclusions remain unchanged unless an actual contradiction is discovered during the correction.

Primary risk: accidentally expanding a structural correction into tax/accounting policy design.

### 3.3 EXPERT IBPV

Status: `PROCEED — PRESERVE BUSINESS SEMANTICS`

Opinion:

- Preserve K01..K36, nine reductions and six additions exactly as independently supported.
- The SI matrix must describe Gate relevance without changing business-process semantics.
- Later-Gate responsibilities for G04/G04S/G05/G06/G07 must remain explicit.

Primary risk: rewriting business semantics while attempting to improve evidence presentation.

### 3.4 EXPERT IDTM

Status: `PROCEED — ADVISORY TRACEABILITY / REPRODUCIBILITY ONLY`

Opinion:

- Each SI row should be independently re-checkable from the cited evidence location.
- Reviewer/verifier and Gate impact must be unambiguous.
- Do not claim runtime proof where only G02 classification/discovery evidence exists.

Primary risk: a matrix that looks complete but cannot be re-performed.

### 3.5 EXPERT IESA

Status: `PROCEED — SAAS CONTROL RECORD MUST BE COMPLETE`

Opinion:

- SI-01..SI-10 are guardrails at G02, not proof that G04S/G07 are complete.
- Tenant/company/template/version/upgrade/isolation references must preserve later-Gate ownership.
- `PASS / VERIFIED` at G02 may only mean the G02 candidate does not violate the invariant at the authorized classification/discovery scope; it must not imply runtime implementation evidence.

Primary risk: using a G02 compliance row to falsely claim SaaS runtime readiness.

## 4. Consolidated Correction Scope

Authorized correction only:

1. republish `COA_G02_SAAS_INVARIANT_COMPLIANCE.md` with the exact seven mandatory evidence-record fields for each SI-01..SI-10;
2. use only the Boss-approved verification status vocabulary;
3. preserve explicit later-Gate deferrals and avoid runtime-proof claims;
4. amend `COA_G02_GATE_REPORT.md` with an explicit SI-01..SI-10 matrix meeting the same structure;
5. preserve the 36-concept candidate and all independently supported semantic evidence unchanged;
6. publish correction evidence and stop for fresh targeted Independent Re-audit.

Not authorized:

- COA-G03;
- redesign of K01..K36;
- new account-count optimization;
- new tax/statutory design;
- final Standard Thai COA freeze;
- database/API/ORM design;
- Development, Release, Deployment or Production;
- PMO or Boss self-approval by Team B.

## 5. Prompt Readiness Record

| Field | Decision |
|---|---|
| Prompt / Session | `SMEPLUS-26-09-01-COA-G02-CORR1-001` |
| Risk Class | HIGH |
| Current execution role | Team B targeted correction |
| Audit VETO | NO VETO |
| TBRAC | PROCEED — NO NEW TH ACCOUNTING CLAIMS |
| IBPV | PROCEED — PRESERVE SEMANTICS |
| IDTM | PROCEED — TRACEABILITY ONLY |
| IESA | PROCEED — COMPLETE SI CONTROL RECORD |
| Blocking pre-execution unknown | NONE |
| Readiness | `READY — TARGETED G02-AUD-01/02 CORRECTION ONLY` |
| 36-concept redesign | PROHIBITED unless correction uncovers genuine contradictory evidence |
| G02 PASS self-declaration | PROHIBITED |
| PMO Verification | NOT YET AUTHORIZED |
| COA-G03 | NOT AUTHORIZED |
| Development / Production | NOT AUTHORIZED |

## 6. Required Lifecycle

`Team B CORR1 -> Fresh Targeted Independent Re-audit -> PMO Verification only if re-audit PASS -> Boss G02 Decision -> COA-G03 only if separately authorized`

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
