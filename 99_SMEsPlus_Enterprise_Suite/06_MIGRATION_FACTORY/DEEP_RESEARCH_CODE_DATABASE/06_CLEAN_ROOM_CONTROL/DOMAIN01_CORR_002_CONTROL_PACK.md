# DOMAIN_01 Accounting Core — CORR-002 Control Pack

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`  
Issued: 2026-08-29 Asia/Bangkok  
Issuer: ChatGPT L99 — Independent Evidence Gate Review  
Status: **AUTHORIZED CORRECTION WORK / NOT A PASS**

## Objective

Correct the six evidence-control defects identified by the independent DOMAIN_01 re-audit without overwriting prior research history and without activating Team B.

## Required Outputs

| ID | Required Output | Acceptance Test | Gate Result if Missing |
|---|---|---|---|
| CORR2-01 | `PROVENANCE_TAXONOMY_CANONICAL.md` | One canonical P-code taxonomy plus explicit crosswalk from all prior Part1/Part2 usages | HOLD |
| CORR2-02 | `TEAM_B_CANDIDATE_INPUT_v2_SANITIZED.md` | Every statement tagged ACCOUNTING_PRINCIPLE / REGULATORY_REQUIREMENT / ERP_COMMON_PATTERN / OBSERVED_REFERENCE_BEHAVIOR / INFERENCE / UNKNOWN; no vendor structure or implementation transfer | HOLD |
| CORR2-03 | `THAI_REGULATORY_EVIDENCE_MATRIX.md` | Each Thai claim has authority/source/date/scope/claim limit; unsupported broad claims remain HOLD | HOLD |
| CORR2-04 | `DB_OBJECT_COUNT_RECONCILIATION.csv` + `.md` | Reconcile direct vs historical TABLE/TABLE DATA/INDEX/CONSTRAINT/FK count definitions and explain +94 index difference | HOLD |
| CORR2-05 | `COMMIT_CHAIN_DISPOSITION.md` | Resolve `b2e5a2a...` as valid/stale/rewritten/erroneous with evidence; no silent substitution | HOLD |
| CORR2-06 | `EVIDENCE_COMPLETENESS_v2.md` + `TEAM_A_DOMAIN_STATUS_v2.md` | Separate mechanism/structural/data-level/behavioral/statutory coverage; status must reflect unresolved controls | HOLD |

## Candidate-Input Classification Rule

No statement may enter sanitized candidate input without one of these labels:

1. `ACCOUNTING_PRINCIPLE` — independently established general accounting rule;
2. `REGULATORY_REQUIREMENT` — exact authority and scope cited;
3. `ERP_COMMON_PATTERN` — common implementation/control pattern, not a mandatory accounting fact;
4. `OBSERVED_REFERENCE_BEHAVIOR` — neutral behavioral observation with proprietary details removed;
5. `INFERENCE` — reasoned but not directly proven;
6. `UNKNOWN` — unresolved / not eligible for downstream baseline.

Examples of controls:

- exact-decimal storage is `ERP_COMMON_PATTERN` unless independently mandated;
- additive correction/reversal is not automatically a universal accounting-law requirement;
- period lock immutability must distinguish accounting control from source-specific mechanism;
- Thai tax-invoice sequence requirements must retain their exact statutory scope;
- no narrow e-Tax requirement may be generalized into all GL records.

## DB Census Reconciliation Schema

Required columns:

```text
object_class,
historical_artifact,
historical_extraction_rule,
historical_count,
direct_pg_restore_class,
direct_count,
inclusion_exclusion_rule,
duplicate_filter_policy,
version_timestamp,
reconciliation_status,
evidence_location,
reviewer,
notes
```

Allowed `reconciliation_status`:

- `SAME_SCOPE`
- `DIFFERENT_SCOPE`
- `VERSION_DELTA`
- `EXTRACTION_ERROR`
- `UNRESOLVED`

No numerical difference is interpreted as database change without evidence.

## Thai Regulatory Evidence Minimum

Use official authority where available. Current independent corroboration already anchors:

- Revenue Department Section 86/4 — tax-invoice sequence-number field requirement;
- Revenue Department VAT Announcement No. 46 — numerical progression for the approved cash-register abbreviated-tax-invoice regime;
- ETDA e-Tax materials — digital signature / XML electronic submission requirements.

Broad retention, audit, general-ledger numbering, or universal gapless requirements remain separate controls unless supported by authoritative evidence.

## Completion Rule

CORR-002 may be presented for re-audit only when all six outputs exist with:

- owner;
- evidence location;
- timestamp;
- reviewer/verifier;
- verification status;
- gate impact.

Team A may state `CORR-002 PACK PREPARED FOR INDEPENDENT RE-AUDIT` only after those fields are inspectable.

It may not state `PASS`, `CLEAN-ROOM APPROVED`, `TEAM B AUTHORIZED`, or `PRODUCTION READY`.

`No Evidence = No Progress.`  
`Never Skip Gate.`
