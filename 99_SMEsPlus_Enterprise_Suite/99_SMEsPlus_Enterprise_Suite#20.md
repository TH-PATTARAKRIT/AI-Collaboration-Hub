#!/usr/bin/env bash

set -e

BASE="99\_SMEsPlus\_Enterprise\_Suite"

mkdir -p "$BASE/02\_Functional\_Design"

mkdir -p "$BASE/07\_Output\_From\_AI"

mkdir -p "$BASE/12\_Traceability/Requirement\_Matrix"

create\_module () {

ID="$1"

NAME="$2"

SCOPE="$3"

SAFE\_NAME=$(echo "$NAME" | tr ' ' '\_' | tr '/' '\_')

cat > "$BASE/02\_Functional\_Design/${ID}\_${SAFE\_NAME}\_FDS\_PACKAGE.md" <<EOF

# ${ID} ${NAME} Functional Specification Draft Package

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: /L99

## 1. Executive Summary

${ID} ${NAME} เป็นส่วนหนึ่งของ Accounting Thailand Domain สำหรับ SMEsPlus Enterprise Suite

Scope หลัก:

${SCOPE}

โมดูลนี้ต้อง reuse SaaS Foundation ได้แก่ Tenant, IAM, RBAC, Approval, Notification, Audit, Evidence, Integration, Configuration และ Security

## 2. Functional Requirements

| FR ID | Function | Priority | Reuse |

|---|---|---|---|

| FR-${ID}-001 | Setup / Configuration | Must | Adapt |

| FR-${ID}-002 | Create Transaction / Record | Must | New |

| FR-${ID}-003 | Edit Draft | Must | New |

| FR-${ID}-004 | Submit for Approval | Must | Reuse Approval |

| FR-${ID}-005 | Approve / Reject | Must | Reuse Approval |

| FR-${ID}-006 | Post / Confirm | Must | New |

| FR-${ID}-007 | Reverse / Cancel | Must | New |

| FR-${ID}-008 | Evidence Attachment | Must | Reuse Evidence |

| FR-${ID}-009 | Audit Trail | Must | Reuse Audit |

| FR-${ID}-010 | Report / Export | Should | Adapt |

## 3. Business Rules

| BR ID | Rule |

|---|---|

| BR-${ID}-001 | ทุก transaction ต้องอยู่ภายใต้ tenant/company/branch scope |

| BR-${ID}-002 | ผู้ใช้ต้องมี permission ก่อน view/create/edit/approve/export |

| BR-${ID}-003 | เอกสารที่ approved/posted แล้วห้ามแก้ไขโดยตรง |

| BR-${ID}-004 | การแก้ไขรายการที่ posted ต้องใช้ reverse หรือ adjustment |

| BR-${ID}-005 | รายการสำคัญต้องมี evidence ก่อนส่งอนุมัติ |

| BR-${ID}-006 | ทุก approval ต้องบันทึก approver, decision, timestamp |

| BR-${ID}-007 | ทุกการเปลี่ยนสถานะต้องบันทึก audit trail |

| BR-${ID}-008 | เลขที่เอกสารต้อง unique ตาม tenant/company/branch/document type |

## 4. Workflow

Draft → Attach Evidence → Submit Approval → Approve / Reject → Post / Confirm → Report / Audit

## 5. Data Entities

| Entity | Key Fields |

|---|---|

| ${SAFE\_NAME}Header | id, document\_no, document\_date, status, tenant\_id, company\_id, branch\_id |

| ${SAFE\_NAME}Line | id, header\_id, account\_id, amount, tax\_amount, description |

| Evidence | evidence\_id, ref\_type, ref\_id, file\_url |

| AuditLog | audit\_id, ref\_type, ref\_id, action, actor\_id, timestamp |

## 6. API Mapping

| API ID | Method | Endpoint |

|---|---|---|

| API-${ID}-001 | GET | /api/accounting/${SAFE\_NAME,,} |

| API-${ID}-002 | POST | /api/accounting/${SAFE\_NAME,,} |

| API-${ID}-003 | PUT | /api/accounting/${SAFE\_NAME,,}/{id} |

| API-${ID}-004 | POST | /api/accounting/${SAFE\_NAME,,}/{id}/submit |

| API-${ID}-005 | POST | /api/accounting/${SAFE\_NAME,,}/{id}/approve |

| API-${ID}-006 | POST | /api/accounting/${SAFE\_NAME,,}/{id}/post |

| API-${ID}-007 | POST | /api/accounting/${SAFE\_NAME,,}/{id}/reverse |

| API-${ID}-008 | GET | /api/accounting/${SAFE\_NAME,,}/report |

## 7. UI Mapping

| Screen ID | Screen |

|---|---|

| SCR-${ID}-001 | ${NAME} List |

| SCR-${ID}-002 | ${NAME} Form |

| SCR-${ID}-003 | ${NAME} Detail |

| SCR-${ID}-004 | Approval Panel |

| SCR-${ID}-005 | Evidence Panel |

| SCR-${ID}-006 | Audit Log Viewer |

| SCR-${ID}-007 | Report / Export |

## 8. Acceptance Criteria

| AC ID | Given | When | Then |

|---|---|---|---|

| AC-${ID}-001 | User ไม่มี permission | Access screen | ระบบต้องปฏิเสธ |

| AC-${ID}-002 | Draft ไม่มี evidence | Submit approval | ระบบต้อง block |

| AC-${ID}-003 | Approver approve | Post transaction | ระบบต้องเปลี่ยนสถานะเป็น posted |

| AC-${ID}-004 | Transaction posted แล้ว | User edit | ระบบต้อง block |

| AC-${ID}-005 | User reverse | Reverse valid posted item | ระบบต้องสร้าง reverse record |

| AC-${ID}-006 | User export report | Has permission | ระบบต้อง export ได้ |

## 9. Open Questions

| ID | Question |

|---|---|

| OQ-${ID}-001 | ต้องมี custom workflow เฉพาะโมดูลนี้หรือไม่ |

| OQ-${ID}-002 | ต้อง export report format ใด |

| OQ-${ID}-003 | ต้องเชื่อม module อื่นใดใน Phase แรก |

## 10. Clean Room Compliance

- Reuse Foundation เท่าที่มี

- ไม่สร้างซ้ำกับ ACC-001

- ไม่คัดลอกคู่แข่ง

- ต้องผ่าน Review ก่อน Approved

EOF

cat > "$BASE/07\_Output\_From\_AI/${ID}\_GAP\_ANALYSIS.md" <<EOF

# ${ID} Gap Analysis

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: /L99

| Gap ID | Gap | Impact | Recommendation | Status |

|---|---|---|---|---|

| GAP-${ID}-001 | Business owner ยังไม่ confirm scope รายละเอียด | Requirement อาจเปลี่ยน | Business review | Open |

| GAP-${ID}-002 | Report format ยังไม่ระบุ | UAT ไม่ชัด | Define report/export format | Open |

| GAP-${ID}-003 | Integration scope ยังไม่ชัด | API อาจขยาย | Confirm integration scope | Open |

| GAP-${ID}-004 | Claude Review ยังไม่ดำเนินการ | Evidence partial | Execute batch review | Pending |

EOF

cat > "$BASE/07\_Output\_From\_AI/${ID}\_EVIDENCE\_REGISTER.md" <<EOF

# ${ID} Evidence Register

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: /L99

| FR ID | Evidence Type | Evidence Status | Source / Note |

|---|---|---|---|

| FR-${ID}-001 | Repository / Business | Partial | Requires owner confirmation |

| FR-${ID}-002 | Business | Partial | Draft requirement |

| FR-${ID}-003 | Business | Partial | Draft requirement |

| FR-${ID}-004 | Repository | Verified | Reuse Approval Foundation |

| FR-${ID}-005 | Repository | Verified | Reuse Approval Foundation |

| FR-${ID}-006 | Business | Partial | Requires review |

| FR-${ID}-007 | Business | Partial | Requires review |

| FR-${ID}-008 | Repository | Verified | Reuse Evidence Foundation |

| FR-${ID}-009 | Repository | Verified | Reuse Audit Foundation |

| FR-${ID}-010 | Business | Partial | Report confirmation required |

EOF

cat > "$BASE/12\_Traceability/Requirement\_Matrix/${ID}\_TRACEABILITY\_MATRIX.md" <<EOF

# ${ID} Traceability Matrix

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: /L99

| FR | BR | DB | API | UI | AC | Evidence |

|---|---|---|---|---|---|---|

| FR-${ID}-001 | BR-${ID}-001 | ${SAFE\_NAME}Header | API-${ID}-001 | SCR-${ID}-001 | AC-${ID}-001 | Partial |

| FR-${ID}-002 | BR-${ID}-002 | ${SAFE\_NAME}Header, ${SAFE\_NAME}Line | API-${ID}-002 | SCR-${ID}-002 | AC-${ID}-002 | Partial |

| FR-${ID}-003 | BR-${ID}-003 | ${SAFE\_NAME}Header | API-${ID}-003 | SCR-${ID}-002 | AC-${ID}-004 | Partial |

| FR-${ID}-004 | BR-${ID}-005 | Evidence | API-${ID}-004 | SCR-${ID}-004 | AC-${ID}-002 | Verified |

| FR-${ID}-005 | BR-${ID}-006 | AuditLog | API-${ID}-005 | SCR-${ID}-004 | AC-${ID}-003 | Verified |

| FR-${ID}-006 | BR-${ID}-007 | ${SAFE\_NAME}Header | API-${ID}-006 | SCR-${ID}-003 | AC-${ID}-003 | Partial |

| FR-${ID}-007 | BR-${ID}-004 | ${SAFE\_NAME}Header | API-${ID}-007 | SCR-${ID}-003 | AC-${ID}-005 | Partial |

| FR-${ID}-008 | BR-${ID}-005 | Evidence | Reuse Evidence API | SCR-${ID}-005 | AC-${ID}-002 | Verified |

| FR-${ID}-009 | BR-${ID}-007 | AuditLog | Reuse Audit API | SCR-${ID}-006 | AC-${ID}-003 | Verified |

| FR-${ID}-010 | BR-${ID}-008 | ${SAFE\_NAME}Header | API-${ID}-008 | SCR-${ID}-007 | AC-${ID}-006 | Partial |

EOF

}

create\_module "ACC-002" "General Ledger" "- บันทึกและแสดงรายการบัญชีแยกประเภท

- แสดง transaction ตาม account, period, branch, department, project

- รองรับ posting จาก journal, AR, AP, VAT, WHT, bank และ adjustment"

create\_module "ACC-003" "Chart of Accounts" "- จัดการผังบัญชี

- รองรับ account code, account type, parent-child account

- รองรับ lock account เมื่อถูกใช้งานแล้ว"

create\_module "ACC-004" "Journal Entry" "- บันทึก journal entry

- ตรวจ debit = credit

- ส่งอนุมัติ, post, reverse และ audit trail"

create\_module "ACC-005" "Accounts Payable" "- บันทึก vendor bill

- รองรับ VAT ซื้อ, WHT, payment voucher

- เชื่อมกับ Purchase และ Cash/Bank"

create\_module "ACC-006" "Accounts Receivable" "- บันทึก customer invoice

- รองรับ tax invoice, receipt, credit note, debit note

- เชื่อมกับ Sales และ Cash/Bank"

create\_module "ACC-007" "VAT Management Thailand" "- จัดการ VAT ซื้อและ VAT ขาย

- จัดทำรายงานภาษีซื้อ/ขาย

- เตรียมข้อมูลสำหรับ ภ.พ.30"

create\_module "ACC-008" "WHT Management Thailand" "- จัดการภาษีหัก ณ ที่จ่าย

- รองรับ WHT certificate

- เตรียมข้อมูลสำหรับ ภ.ง.ด.3 และ ภ.ง.ด.53"

create\_module "ACC-009" "Cash and Bank" "- จัดการเงินสดและบัญชีธนาคาร

- รับเงิน จ่ายเงิน โอนเงิน

- รองรับ bank reconciliation และ statement import"

create\_module "ACC-010" "Period Closing" "- ตรวจรายการก่อนปิดงวด

- ตรวจ unposted transaction, missing evidence, pending approval

- ปิดงวดและ lock transaction ย้อนหลัง"

cat > "$BASE/07\_Output\_From\_AI/ACCOUNTING\_BATCH\_ACC002\_TO\_ACC010\_STATUS\_REPORT.md" <<'EOF'

# Accounting Batch ACC-002 to ACC-010 Status Report

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: /L99

## Batch Scope

| Module | Status |

|---|---|

| ACC-002 General Ledger | Draft Completed |

| ACC-003 Chart of Accounts | Draft Completed |

| ACC-004 Journal Entry | Draft Completed |

| ACC-005 Accounts Payable | Draft Completed |

| ACC-006 Accounts Receivable | Draft Completed |

| ACC-007 VAT Management Thailand | Draft Completed |

| ACC-008 WHT Management Thailand | Draft Completed |

| ACC-009 Cash and Bank | Draft Completed |

| ACC-010 Period Closing | Draft Completed |

## Files Created Per Module

| File Type | Count |

|---|---:|

| FDS Package | 9 |

| Gap Analysis | 9 |

| Evidence Register | 9 |

| Traceability Matrix | 9 |

| Batch Status Report | 1 |

## Total Files

37 files

## Current Gate

Draft Completed → Ready for Batch Review

## Next Step

Send ACC-002 to ACC-010 batch to Claude Review / PMO Review after upload.

EOF

echo "Accounting Batch ACC-002 to ACC-010 created successfully."