#!/usr/bin/env bash

set -e

BASE="99\_SMEsPlus\_Enterprise\_Suite"

mkdir -p "$BASE/07\_Output\_From\_AI"

mkdir -p "$BASE/12\_Traceability/Requirement\_Matrix"

mkdir -p "$BASE/14\_Claude\_Execution/Task\_Prompts"

cat > "$BASE/07\_Output\_From\_AI/ACC-001\_UPLOAD\_VERIFICATION\_STATUS.md" <<'EOF'

# ACC-001 Upload Verification Status

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: L99

## Verification Result

| Item | Path | GitHub Status | Action |

|---|---|---|---|

| ACC-001 FDS Package | 02\_Functional\_Design | Found | Do not recreate |

| ACC-001 Gap Analysis | 07\_Output\_From\_AI | Not Found | Create |

| ACC-001 Evidence Register | 07\_Output\_From\_AI | Not Found | Create |

| ACC-001 Checklist Status | 07\_Output\_From\_AI | Not Found | Create |

| ACC-001 Traceability Matrix | 12\_Traceability/Requirement\_Matrix | Not Found | Create |

| ACC-001 Claude Review Prompt | 14\_Claude\_Execution/Task\_Prompts | Not Found | Create |

## Conclusion

ACC-001 FDS exists. Supporting review and governance files are missing and should be created.

EOF

cat > "$BASE/07\_Output\_From\_AI/ACC-001\_GAP\_ANALYSIS.md" <<'EOF'

# ACC-001 Gap Analysis

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: L99

| Gap ID | Area | Gap | Impact | Recommendation | Status |

|---|---|---|---|---|---|

| GAP-ACC-001 | Thai Tax | VAT/WHT legal detail ยังต้อง review | Compliance risk | ส่ง Accounting/Legal review | Open |

| GAP-ACC-002 | e-Tax | ยังไม่กำหนด Phase | Scope unclear | Boss decision | Open |

| GAP-ACC-003 | Bank | ยังไม่กำหนด integration type | API scope unclear | เริ่มจาก bank statement import | Open |

| GAP-ACC-004 | Currency | THB หรือ Multi-currency ยังไม่ชัด | DB design impact | Confirm phase scope | Open |

| GAP-ACC-005 | Cost Center | ยังไม่กำหนด Phase | GL/report impact | Finance Owner decision | Open |

| GAP-ACC-006 | Report Export | ยังไม่ระบุ format ภาษี | UAT unclear | ระบุ export format | Open |

| GAP-ACC-007 | Claude Review | ยังไม่มีผล review | Evidence partial | ส่ง Claude review | Pending |

EOF

cat > "$BASE/07\_Output\_From\_AI/ACC-001\_EVIDENCE\_REGISTER.md" <<'EOF'

# ACC-001 Evidence Register

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: L99

| FR ID | Evidence Type | Evidence Status | Source / Note |

|---|---|---|---|

| FR-ACC-001 | Repository / Business | Partial | Requires Accounting Owner confirmation |

| FR-ACC-002 | Business | Partial | Standard accounting requirement |

| FR-ACC-003 | Business | Partial | Double-entry accounting principle |

| FR-ACC-004 | Repository | Verified | Reuse Approval Foundation |

| FR-ACC-005 | Business | Partial | Needs Accounting review |

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

cat > "$BASE/07\_Output\_From\_AI/ACC-001\_CHECKLIST\_STATUS.md" <<'EOF'

# ACC-001 Checklist Status

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: L99

| Checklist Item | Status |

|---|---|

| ตรวจ Repository ก่อนสร้างไฟล์ | Done |

| ไม่สร้าง FDS ซ้ำ | Done |

| ใช้ path เดิมของโครงการ | Done |

| Gap Analysis | Draft Completed |

| Evidence Register | Draft Completed |

| Traceability Matrix | Draft Completed |

| Claude Review Prompt | Draft Completed |

| Accounting / Legal Review | Pending |

| PMO Review | Pending |

| Boss Approval | Pending |

## Current Gate

Review Required

## Next Step

Submit ACC-001 package to Claude Review and Accounting/Legal Review.

EOF

cat > "$BASE/12\_Traceability/Requirement\_Matrix/ACC-001\_TRACEABILITY\_MATRIX.md" <<'EOF'

# ACC-001 Traceability Matrix

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: L99

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

cat > "$BASE/14\_Claude\_Execution/Task\_Prompts/ACC-001\_CLAUDE\_REVIEW\_PROMPT.md" <<'EOF'

# ACC-001 Claude Review Prompt

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Target Reviewer: Claude AI

## Review Target

Please review:

- 02\_Functional\_Design/ACC-001 Accounting Thailand Functional Design Specification Package.md

- 07\_Output\_From\_AI/ACC-001\_GAP\_ANALYSIS.md

- 07\_Output\_From\_AI/ACC-001\_EVIDENCE\_REGISTER.md

- 12\_Traceability/Requirement\_Matrix/ACC-001\_TRACEABILITY\_MATRIX.md

## Review Objectives

1. ตรวจ missing requirement ของ Accounting Thailand

2. ตรวจ VAT / WHT / Tax Invoice / Receipt / Credit Note / Debit Note completeness

3. ตรวจว่า requirement รองรับ SaaS Foundation หรือไม่

4. ตรวจ Clean Room compliance

5. ตรวจ evidence status

6. ตรวจ traceability completeness

7. ตรวจ API / DB / UI mapping gap

8. แนะนำ Reuse / Adapt / New classification

## Required Output

Please return review in this format:

| Finding ID | Area | Finding | Severity | Recommendation | Evidence Status |

|---|---|---|---|---|---|

## Decision

Please classify result as:

- Approved for PMO Review

- Approved with Minor Changes

- Hold for Major Revision

- Reject due to Missing Evidence

EOF

echo "Iteration-003 ACC-001 review package created successfully."