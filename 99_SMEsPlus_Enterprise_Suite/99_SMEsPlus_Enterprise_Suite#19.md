#!/usr/bin/env bash

set -e

BASE="99\_SMEsPlus\_Enterprise\_Suite"

mkdir -p "$BASE/07\_Output\_From\_AI"

mkdir -p "$BASE/12\_Traceability/Requirement\_Matrix"

cat > "$BASE/07\_Output\_From\_AI/ACC-001\_FUNCTIONAL\_SPEC\_STATUS\_REPORT.md" <<'EOF'

# ACC-001 Functional Specification Status Report

Version: v1.0

Status: State Recovery

Owner: Functional Specification AI

Working Rule: /L99

## Current State

ACC-001 Functional Specification Draft Package

## Repository Verification

| Item | Status |

|---|---|

| ACC-001 FDS Package | Found |

| STATE 1 Repository Inventory | Found |

| ACC-001 Gap Analysis | To Be Created |

| ACC-001 Evidence Register | To Be Created |

| ACC-001 Traceability Matrix | To Be Created |

| ACC-001 Checklist Status | To Be Created |

## State Completion Rule

State นี้จะถือว่า Draft Completed เมื่อมีไฟล์ครบ:

1. ACC-001 FDS Package

2. ACC-001 Gap Analysis

3. ACC-001 Evidence Register

4. ACC-001 Traceability Matrix

5. ACC-001 Checklist Status

## Current Decision

Proceed to create missing 4 files only.

## Next Gate

Claude Review / PMO Review

EOF

cat > "$BASE/07\_Output\_From\_AI/ACC-001\_GAP\_ANALYSIS.md" <<'EOF'

# ACC-001 Gap Analysis

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: /L99

| Gap ID | Area | Gap | Impact | Recommendation | Status |

|---|---|---|---|---|---|

| GAP-ACC-001 | Thai Tax | VAT/WHT legal detail ยังต้อง review | Compliance risk | Accounting/Legal review | Open |

| GAP-ACC-002 | e-Tax | ยังไม่กำหนด Phase | Scope unclear | Boss decision | Open |

| GAP-ACC-003 | Bank | ยังไม่กำหนด integration type | API scope unclear | Start with bank statement import | Open |

| GAP-ACC-004 | Currency | THB หรือ Multi-currency ยังไม่ชัด | DB design impact | Confirm phase scope | Open |

| GAP-ACC-005 | Cost Center | ยังไม่กำหนด Phase | GL/report impact | Finance Owner decision | Open |

| GAP-ACC-006 | Report Export | ยังไม่ระบุ format ภาษี | UAT unclear | Define export format | Open |

| GAP-ACC-007 | Claude Review | ยังไม่มีผล review | Evidence partial | Execute Claude review | Pending |

EOF

cat > "$BASE/07\_Output\_From\_AI/ACC-001\_EVIDENCE\_REGISTER.md" <<'EOF'

# ACC-001 Evidence Register

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: /L99

| FR ID | Evidence Type | Evidence Status | Source / Note |

|---|---|---|---|

| FR-ACC-001 | Repository / Business | Partial | Accounting Owner confirmation required |

| FR-ACC-002 | Business | Partial | Standard accounting requirement |

| FR-ACC-003 | Business | Partial | Double-entry accounting principle |

| FR-ACC-004 | Repository | Verified | Reuse Approval Foundation |

| FR-ACC-005 | Business | Partial | Accounting review required |

| FR-ACC-006 | Business | Partial | Posted correction control |

| FR-ACC-007 | Business | Partial | AR requirement |

| FR-ACC-008 | Business | Partial | AP requirement |

| FR-ACC-009 | Legal / Business | Pending | Thai VAT review required |

| FR-ACC-010 | Legal / Business | Pending | Thai WHT review required |

| FR-ACC-011 | Legal / Business | Pending | Tax invoice review required |

| FR-ACC-012 | Legal / Business | Pending | Credit/Debit note review required |

| FR-ACC-013 | Business | Partial | Finance process review required |

| FR-ACC-014 | Business | Partial | Period closing control |

| FR-ACC-015 | Business | Partial | Report list needs owner approval |

| FR-ACC-016 | Repository | Verified | No Evidence = No Progress |

| FR-ACC-017 | Repository | Verified | Audit Foundation |

| FR-ACC-018 | Repository | Partial | Integration Foundation |

| FR-ACC-019 | Repository | Verified | Tenant / company / branch scope |

EOF

cat > "$BASE/12\_Traceability/Requirement\_Matrix/ACC-001\_TRACEABILITY\_MATRIX.md" <<'EOF'

# ACC-001 Traceability Matrix

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: /L99

| FR | BR | DB | API | UI | AC | Evidence |

|---|---|---|---|---|---|---|

| FR-ACC-001 | BR-ACC-009 | AccountingPeriod | API-ACC-013 | SCR-ACC-002 | AC-ACC-007 | Partial |

| FR-ACC-002 | BR-ACC-010 | Account | API-ACC-001, API-ACC-002 | SCR-ACC-003 | AC-ACC-008 | Partial |

| FR-ACC-003 | BR-ACC-001 | JournalEntry, JournalLine | API-ACC-003 | SCR-ACC-004, SCR-ACC-005 | AC-ACC-001 | Partial |

| FR-ACC-004 | BR-ACC-006 | JournalEntry, AuditLog | API-ACC-004 | SCR-ACC-005 | AC-ACC-002 | Verified |

| FR-ACC-005 | BR-ACC-002 | JournalEntry, JournalLine | API-ACC-005 | SCR-ACC-005 | AC-ACC-003 | Partial |

| FR-ACC-006 | BR-ACC-002 | JournalEntry | API-ACC-006 | SCR-ACC-005 | AC-ACC-004 | Partial |

| FR-ACC-007 | BR-ACC-008 | Invoice, Receipt | API-ACC-007, API-ACC-012 | SCR-ACC-006 | AC-ACC-005 | Partial |

| FR-ACC-008 | BR-ACC-007 | Bill, PaymentVoucher | API-ACC-008, API-ACC-011 | SCR-ACC-007 | AC-ACC-006 | Partial |

| FR-ACC-009 | BR-ACC-008 | TaxInvoice | API-ACC-009 | SCR-ACC-008 | AC-ACC-005 | Pending |

| FR-ACC-010 | BR-ACC-007 | WHTCertificate | API-ACC-010 | SCR-ACC-009 | AC-ACC-006 | Pending |

| FR-ACC-011 | BR-ACC-003 | TaxInvoice, Receipt | API-ACC-007, API-ACC-012 | SCR-ACC-010 | AC-ACC-005 | Pending |

| FR-ACC-012 | BR-ACC-003 | TaxInvoice | TBD | SCR-ACC-010 | TBD | Pending |

| FR-ACC-013 | BR-ACC-010 | BankAccount | API-ACC-011, API-ACC-012 | SCR-ACC-011 | TBD | Partial |

| FR-ACC-014 | BR-ACC-004 | AccountingPeriod | API-ACC-013 | SCR-ACC-012 | AC-ACC-007 | Partial |

| FR-ACC-015 | BR-ACC-010 | JournalEntry, JournalLine | API-ACC-014, API-ACC-015 | SCR-ACC-013 | TBD | Partial |

| FR-ACC-016 | BR-ACC-005 | Evidence | Reuse Evidence API | SCR-ACC-014 | AC-ACC-002 | Verified |

| FR-ACC-017 | BR-ACC-006 | AuditLog | Reuse Audit API | SCR-ACC-015 | AC-ACC-003 | Verified |

| FR-ACC-018 | BR-ACC-010 | IntegrationLog | TBD | TBD | TBD | Partial |

| FR-ACC-019 | BR-ACC-010 | TenantScope Fields | All APIs | All Screens | AC-ACC-008 | Verified |

EOF

cat > "$BASE/07\_Output\_From\_AI/ACC-001\_CHECKLIST\_STATUS.md" <<'EOF'

# ACC-001 Checklist Status

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: /L99

## State Checklist

| Item | Status |

|---|---|

| Repository checked before action | Done |

| Existing FDS reused | Done |

| No duplicate FDS created | Done |

| Functional Specification | Done |

| Business Rules | Done |

| Workflow | Done |

| Data Entities | Done |

| API Mapping | Done |

| UI Mapping | Done |

| Acceptance Criteria | Done |

| Gap Analysis | Draft Completed |

| Evidence Register | Draft Completed |

| Traceability Matrix | Draft Completed |

| Checklist Status | Draft Completed |

## State Result

ACC-001 Functional Specification Draft Package = Completed

## Next Gate

Claude Review / PMO Review / Accounting-Legal Review

## Remaining Before Approval

| Item | Status |

|---|---|

| Claude Review | Pending |

| PMO Review | Pending |

| Accounting / Legal Review | Pending |

| Boss Approval | Pending |

EOF

echo "ACC-001 State Recovery and Close Package created successfully."