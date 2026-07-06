#!/usr/bin/env bash

set -e

BASE="99\_SMEsPlus\_Enterprise\_Suite"

mkdir -p "$BASE/02\_Functional\_Design"

mkdir -p "$BASE/07\_Output\_From\_AI"

mkdir -p "$BASE/12\_Traceability/ Requirement\_Matrix"

cat > "$BASE/02\_Functional\_Design/ACC-001\_ACCOUNTING\_THAILAND\_FDS\_PACKAGE.md" <<'EOF'

# ACC-001 Accounting Thailand FDS Package

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: L99

## Executive Summary

Accounting Thailand รองรับ General Ledger, Chart of Accounts, Journal Entry, AR, AP, VAT, WHT, Tax Invoice, Receipt, Credit Note, Debit Note, Bank/Cash, Period Closing, Reports, Evidence และ Audit Trail

โมดูลนี้ต้อง reuse SaaS Foundation: Tenant, IAM, RBAC, Approval, Notification, Audit, Evidence, Integration, Configuration และ Security

## Functional Requirements

| FR ID | Function | Priority | Reuse |

|---|---|---|---|

| FR-ACC-001 | Accounting Setup | Must | Adapt |

| FR-ACC-002 | Chart of Accounts | Must | New |

| FR-ACC-003 | Journal Entry | Must | New |

| FR-ACC-004 | Journal Approval | Must | Reuse Approval |

| FR-ACC-005 | Journal Posting | Must | New |

| FR-ACC-006 | Reverse Journal | Must | New |

| FR-ACC-007 | Accounts Receivable | Must | New |

| FR-ACC-008 | Accounts Payable | Must | New |

| FR-ACC-009 | VAT Management | Must | New |

| FR-ACC-010 | WHT Management | Must | New |

| FR-ACC-011 | Tax Invoice / Receipt | Must | New |

| FR-ACC-012 | Credit Note / Debit Note | Must | New |

| FR-ACC-013 | Bank & Cash | Must | New |

| FR-ACC-014 | Period Closing | Must | New |

| FR-ACC-015 | Financial Reports | Must | New |

| FR-ACC-016 | Evidence Attachment | Must | Reuse Evidence |

| FR-ACC-017 | Audit Trail | Must | Reuse Audit |

| FR-ACC-018 | API Integration | Should | Reuse Integration |

| FR-ACC-019 | Multi-Company / Branch Scope | Must | Reuse Tenant Scope |

## Business Rules

| BR ID | Rule |

|---|---|

| BR-ACC-001 | Debit ต้องเท่ากับ Credit |

| BR-ACC-002 | Posted transaction ห้ามแก้ไขโดยตรง ต้อง reverse หรือ adjustment |

| BR-ACC-003 | เอกสารภาษีต้องมี Tax ID และ Branch |

| BR-ACC-004 | Period ที่ปิดแล้วห้ามแก้ไขย้อนหลัง |

| BR-ACC-005 | Transaction สำคัญต้องมี Evidence ก่อนส่งอนุมัติ |

| BR-ACC-006 | Approval ต้องมี approver, decision, timestamp |

| BR-ACC-007 | WHT คำนวณตามประเภทค่าใช้จ่ายและอัตราที่ตั้งค่า |

| BR-ACC-008 | VAT ซื้อ/ขายต้องแยกตามเดือนภาษี |

| BR-ACC-009 | Document number ต้อง unique ตาม tenant/company/branch/type |

| BR-ACC-010 | ทุก access ต้องผ่าน RBAC และ tenant scope |

## Workflows

### WF-ACC-001 Journal Entry

Create Journal → Validate Debit/Credit → Attach Evidence → Submit Approval → Approve/Reject → Post → Audit Log

### WF-ACC-002 AP Expense

Create Bill → Input VAT/WHT → Attach Evidence → Approval → Payment → Voucher → Post Accounting

### WF-ACC-003 AR Receipt

Create Invoice → Tax Invoice → Receive Payment → Receipt → Post Accounting → VAT Output

### WF-ACC-004 Period Closing

Pre-close Check → Unposted Check → Evidence Check → Pending Approval Check → Close Period → Lock Period

## Data Entities

| Entity | Key Fields |

|---|---|

| Account | account\_id, code, name, type |

| JournalEntry | journal\_id, journal\_no, date, status |

| JournalLine | line\_id, account\_id, debit, credit |

| Invoice | invoice\_id, customer\_id, amount, vat |

| Bill | bill\_id, vendor\_id, amount, vat, wht |

| TaxInvoice | tax\_invoice\_id, number, tax\_date |

| Receipt | receipt\_id, amount, payment\_method |

| PaymentVoucher | voucher\_id, vendor\_id, amount |

| WHTCertificate | certificate\_id, rate, amount |

| BankAccount | bank\_account\_id, bank\_name, account\_no |

| AccountingPeriod | period\_id, year, month, status |

| Evidence | evidence\_id, ref\_type, ref\_id, file\_url |

| AuditLog | audit\_id, ref\_type, ref\_id, action, actor |

## API Mapping

| API ID | Method | Endpoint |

|---|---|---|

| API-ACC-001 | GET | /api/accounting/accounts |

| API-ACC-002 | POST | /api/accounting/accounts |

| API-ACC-003 | POST | /api/accounting/journals |

| API-ACC-004 | POST | /api/accounting/journals/{id}/submit |

| API-ACC-005 | POST | /api/accounting/journals/{id}/post |

| API-ACC-006 | POST | /api/accounting/journals/{id}/reverse |

| API-ACC-007 | POST | /api/accounting/invoices |

| API-ACC-008 | POST | /api/accounting/bills |

| API-ACC-009 | GET | /api/accounting/vat-report |

| API-ACC-010 | GET | /api/accounting/wht-report |

| API-ACC-011 | POST | /api/accounting/payments |

| API-ACC-012 | POST | /api/accounting/receipts |

| API-ACC-013 | POST | /api/accounting/periods/{id}/close |

| API-ACC-014 | GET | /api/accounting/reports/trial-balance |

| API-ACC-015 | GET | /api/accounting/reports/general-ledger |

## UI Mapping

| Screen ID | Screen |

|---|---|

| SCR-ACC-001 | Accounting Dashboard |

| SCR-ACC-002 | Accounting Setup |

| SCR-ACC-003 | Chart of Accounts |

| SCR-ACC-004 | Journal Entry List |

| SCR-ACC-005 | Journal Entry Form |

| SCR-ACC-006 | AR Invoice |

| SCR-ACC-007 | AP Bill |

| SCR-ACC-008 | VAT Report |

| SCR-ACC-009 | WHT Certificate |

| SCR-ACC-010 | Tax Invoice / Receipt |

| SCR-ACC-011 | Bank & Cash |

| SCR-ACC-012 | Period Closing |

| SCR-ACC-013 | Financial Reports |

| SCR-ACC-014 | Evidence Panel |

| SCR-ACC-015 | Audit Log Viewer |

## Acceptance Criteria

| AC ID | Given | When | Then |

|---|---|---|---|

| AC-ACC-001 | Journal debit/credit ไม่เท่ากัน | Submit | ระบบต้องปฏิเสธ |

| AC-ACC-002 | Journal มี evidence | Submit | ระบบสร้าง approval task |

| AC-ACC-003 | Approver อนุมัติ | Post | รายการเข้า GL |

| AC-ACC-004 | Journal post แล้ว | Edit | ระบบต้อง block |

| AC-ACC-005 | มี VAT transaction | Open VAT report | ระบบแสดง VAT ตามเดือน |

| AC-ACC-006 | มี WHT transaction | Generate certificate | ระบบคำนวณและออกเลขเอกสาร |

| AC-ACC-007 | Period ปิดแล้ว | Add backdated transaction | ระบบต้อง block |

| AC-ACC-008 | User ไม่มี permission | Access accounting | ระบบปฏิเสธ |

## Open Questions

| ID | Question |

|---|---|

| OQ-ACC-001 | e-Tax/e-Receipt อยู่ Phase แรกหรือ Phase ถัดไป |

| OQ-ACC-002 | Phase แรกรองรับ THB เท่านั้นหรือ multi-currency |

| OQ-ACC-003 | ต้องมี cost center/project accounting ตั้งแต่ Phase แรกหรือไม่ |

| OQ-ACC-004 | Export ภ.พ.30/ภ.ง.ด.3/ภ.ง.ด.53 ต้องใช้ format ใด |

| OQ-ACC-005 | Bank integration ใช้ import statement หรือ direct integration |

## Clean Room Compliance

- ไม่คัดลอก workflow เฉพาะของคู่แข่ง

- ออกแบบจาก business need และ accounting principle

- แยก assumption/open question

- รองรับ SaaS multi-tenant

- รอ Claude/PMO review ก่อน Approved

EOF

cat > "$BASE/07\_Output\_From\_AI/ACC-001\_GAP\_ANALYSIS.md" <<'EOF'

# ACC-001 Gap Analysis

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

| Gap ID | Area | Gap | Impact | Recommendation |

|---|---|---|---|---|

| GAP-ACC-001 | Thai Tax | VAT/WHT legal detail ยังต้อง review | เสี่ยง compliance | ส่ง Accounting/Legal review |

| GAP-ACC-002 | e-Tax | ยังไม่ตัดสินใจ phase | Scope ไม่ชัด | Boss กำหนด phase |

| GAP-ACC-003 | Bank | ยังไม่กำหนด integration type | API scope ไม่ชัด | เริ่มจาก import statement |

| GAP-ACC-004 | Currency | ยังไม่ชัดว่า multi-currency หรือ THB | DB design กระทบ | Confirm phase scope |

| GAP-ACC-005 | Cost Center | ยังไม่ตัดสินใจ | Report/GL mapping กระทบ | Confirm with Finance Owner |

| GAP-ACC-006 | Report Export | ยังไม่ระบุ format ภาษี | UAT ไม่ชัด | ระบุ export format |

| GAP-ACC-007 | Claude Review | ยังไม่มีผล review | Evidence partial | ส่ง Claude review |

EOF

cat > "$BASE/07\_Output\_From\_AI/ACC-001\_EVIDENCE\_REGISTER.md" <<'EOF'

# ACC-001 Evidence Register

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

| FR ID | Evidence Type | Evidence Status | Source / Note |

|---|---|---|---|

| FR-ACC-001 | Repository / Business | Partial | Requires accounting owner confirmation |

| FR-ACC-002 | Business | Partial | Standard accounting requirement |

| FR-ACC-003 | Business | Partial | Double-entry accounting principle |

| FR-ACC-004 | Repository | Verified | Reuse Approval Foundation |

| FR-ACC-005 | Business | Partial | Needs PMO/Accounting review |

| FR-ACC-006 | Business | Partial | Needed for posted correction control |

| FR-ACC-007 | Business | Partial | AR module requirement |

| FR-ACC-008 | Business | Partial | AP module requirement |

| FR-ACC-009 | Legal/Business | Pending | Thai VAT review required |

| FR-ACC-010 | Legal/Business | Pending | Thai WHT review required |

| FR-ACC-011 | Legal/Business | Pending | Tax invoice review required |

| FR-ACC-012 | Legal/Business | Pending | Credit/Debit note review required |

| FR-ACC-013 | Business | Partial | Finance process review required |

| FR-ACC-014 | Business | Partial | Accounting close control |

| FR-ACC-015 | Business | Partial | Report list needs owner approval |

| FR-ACC-016 | Repository | Verified | No Evidence = No Progress |

| FR-ACC-017 | Repository | Verified | Audit Foundation |

| FR-ACC-018 | Repository | Partial | Integration Foundation |

| FR-ACC-019 | Repository | Verified | Tenant / company / branch scope |

EOF

cat > "$BASE/12\_Traceability/ Requirement\_Matrix/ACC-001\_TRACEABILITY\_MATRIX.md" <<'EOF'

# ACC-001 Traceability Matrix

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

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

cat > "$BASE/07\_Output\_From\_AI/ITERATION\_001\_ACC001\_SUMMARY.md" <<'EOF'

# Iteration-001 ACC-001 Summary

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

## Files Created

| Path | File |

|---|---|

| 02\_Functional\_Design | ACC-001\_ACCOUNTING\_THAILAND\_FDS\_PACKAGE.md |

| 07\_Output\_From\_AI | ACC-001\_GAP\_ANALYSIS.md |

| 07\_Output\_From\_AI | ACC-001\_EVIDENCE\_REGISTER.md |

| 12\_Traceability/ Requirement\_Matrix | ACC-001\_TRACEABILITY\_MATRIX.md |

## Result

ACC-001 Accounting Thailand initial FDS package is ready for upload and commit.

## Next Step

State 3 / Iteration-002:

- Claude Review Handoff

- Evidence Matching Refinement

- Legal/Accounting Review Questions

- ACC-001 Enterprise FDS v1.0 Merge Preparation

EOF

echo "Iteration-001 ACC-001 package created successfully."