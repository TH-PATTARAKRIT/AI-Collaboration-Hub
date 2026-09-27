# G01 Recovery QID Trace Matrix C2

Date: 2026-09-27 (Asia/Bangkok)
Status: TRACE CONTROL ONLY / NOT PRIMARY EVIDENCE / NOT QID PASS
Branch: research/g01-evidence-first-recovery-20260926
Primary evidence dependency: G01_EVIDENCE_FIRST_RECOVERY_PILOT_R4_20260927.md
R4 blob: bc2fd867355bee3a50c9e9fce5ffdc54d18ba1d6
Runtime/A2: NOT EXECUTED
Formal Coverage: NOT AUTHORIZED

## privacy_lookup QID trace expansion

| QID | Source-backed hypothesis / R4 trace | Boundary |
|---|---|---|
| G01-PRIVACY-LOOKUP-Q001 | invalid email rejection; R4 PRIVACY-AKU-002 | static source support only; runtime required |
| G01-PRIVACY-LOOKUP-Q008 | transient-model exclusion; R4 PRIVACY-AKU-002 | static source support only; runtime required |
| G01-PRIVACY-LOOKUP-Q009 | non-auto model exclusion; R4 PRIVACY-AKU-002 | static source support only; runtime required |
| G01-PRIVACY-LOOKUP-Q013 | non-cascade partner-reference discovery; R4 PRIVACY-AKU-002/003 | static source support only; runtime required |
| G01-PRIVACY-LOOKUP-Q014 | cascade-child exclusion target; R4 PRIVACY-AKU-002/003 | static source support only; runtime required |
| G01-PRIVACY-LOOKUP-Q017 | company-restricted result-opening boundary; R4 PRIVACY-AKU-004/005 | runtime/config proof required |
| G01-PRIVACY-LOOKUP-Q018 | normal read-authority boundary; R4 PRIVACY-AKU-004 | runtime role proof required |
| G01-PRIVACY-LOOKUP-Q019 | result-label disclosure boundary; R4 PRIVACY-AKU-004 | negative-role runtime proof required |
| G01-PRIVACY-LOOKUP-Q020 | archive state/event behavior; R4 PRIVACY-AKU-005 | runtime transaction/audit proof required |
| G01-PRIVACY-LOOKUP-Q021 | delete/unlinked-line behavior; R4 PRIVACY-AKU-005 | runtime destructive-action proof required |
| G01-PRIVACY-LOOKUP-Q022 | system-administrator access boundary; R4 PRIVACY-AKU-001 | runtime/config proof required |
| G01-PRIVACY-LOOKUP-Q023 | bulk archive eligibility/idempotence; R4 PRIVACY-AKU-005 | runtime proof required |
| G01-PRIVACY-LOOKUP-Q024 | bulk delete skip/already-unlinked guard; R4 PRIVACY-AKU-005 | runtime proof required |
| G01-PRIVACY-LOOKUP-Q025 | repeated single-delete failure behavior; R4 PRIVACY-AKU-005 | runtime proof required |
| G01-PRIVACY-LOOKUP-Q026 | one-log-per-session/remediation behavior; R4 PRIVACY-AKU-006 | runtime proof required |
| G01-PRIVACY-LOOKUP-Q027 | persisted name masking; R4 PRIVACY-AKU-006 | runtime persisted-value proof required |
| G01-PRIVACY-LOOKUP-Q028 | persisted email local-part masking; R4 PRIVACY-AKU-006 | runtime persisted-value proof required |
| G01-PRIVACY-LOOKUP-Q029 | deterministic domain masking; R4 PRIVACY-AKU-006 | runtime persisted-value proof required |
| G01-PRIVACY-LOOKUP-Q030 | handler attribution in audit log; R4 PRIVACY-AKU-006 | runtime actor/audit proof required |
| G01-PRIVACY-LOOKUP-Q033 | transient expiry vs persistent-log lifecycle; R4 PRIVACY-AKU-006 | runtime scheduler/lifecycle proof required |
| G01-PRIVACY-LOOKUP-Q034 | lookup-only must not create remediation log; R4 PRIVACY-AKU-006 | runtime negative proof required |
| G01-PRIVACY-LOOKUP-Q036 | flush-before-discovery freshness boundary; R4 PRIVACY-AKU-003 | runtime transaction/freshness proof required |

All 22 candidates remain A1-PARTIAL / RUNTIME-REQUIRED.
This matrix provides traceability only. It does not provide Independent RED TEAM per-QID PASS, release credit, A2 authorization, or Formal Coverage.

## Independent gate status at checkpoint
PR #68 remains OPEN / DRAFT / NOT MERGED with zero review submissions and zero review threads.

## Disposition
QID TRACE EXPANSION C2 = PERSISTED TRACE CONTROL ONLY.
A1 Single Exit remains NOT READY.
A2 NOT AUTHORIZED.
Formal Coverage PROHIBITED before Boss-frozen Canonical Function-ID denominator.
