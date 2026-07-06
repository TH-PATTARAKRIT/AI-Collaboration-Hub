# ACC-001 Accounting Thailand Functional Design Specification Package

Version: v1.0

Status: Draft Completed

Owner: Functional Specification AI

Working Rule: L99

Project: SMEsPlus Enterprise Suite

Path: 02\_Functional\_Design/ACC-001\_ACCOUNTING\_THAILAND\_FDS\_PACKAGE.md

---

## 1. Executive Summary

ACC-001 Accounting Thailand เป็นโมดูลบัญชีสำหรับธุรกิจไทยบน SaaS Platform ของ SMEsPlus Enterprise Suite

โมดูลนี้รองรับ:

- General Ledger

- Chart of Accounts

- Journal Entry

- Accounts Receivable

- Accounts Payable

- VAT ซื้อ / VAT ขาย

- Withholding Tax

- ใบกำกับภาษี

- ใบเสร็จรับเงิน

- ใบลดหนี้ / ใบเพิ่มหนี้

- Bank / Cash

- Period Closing

- Financial Reports

- Evidence & Audit Trail

โมดูลนี้ต้อง reuse SaaS Foundation เดิม ได้แก่ Tenant, IAM, Role Permission, Approval, Notification, Audit, Evidence, Integration, Configuration และ Security

---

## 2. Source of Truth

| Source | Usage |

|---|---|

| 99\_SMEsPlus\_Enterprise\_Suite/README.md | Repository structure, workflow, evidence rule |

| 01\_SaaS\_Foundation/ | Shared SaaS capability |

| 17\_Functional\_Specification\_Factory/ | FDS package structure |

| AI\_WORKING\_INDEX.md | AI working control |

| MODULE\_EXPANSION\_PLAN.md | Module expansion reference |

| State 1 Repository Inventory | Reuse / Gap baseline |

---

## 3. Scope

### In Scope

- Accounting setup

- Chart of accounts

- Journal posting

- AR / AP accounting

- VAT management

- WHT management

- Tax invoice / receipt / credit note / debit note

- Bank and cash transaction

- Period closing

- Accounting reports

- Audit and evidence control

- API / DB / UI / AC mapping

### Out of Scope

- Full payroll calculation

- Full inventory costing engine

- Full manufacturing cost accounting

- Bank direct payment execution

- Direct e-Filing submission unless integration is approved

- Certified e-Tax provider submission unless integration is approved

---

## 4. User Roles

| Role | Responsibility |

|---|---|

| Accounting Admin | Configure accounting master data |

| Accountant | Create journal, invoice, bill, tax records |

| Finance Officer | Handle payment, receipt, bank, cash |

| Approver | Approve accounting documents |

| Auditor | Review evidence, audit trail, financial records |

| Tenant Admin | Manage user access and company scope |

| Boss / Owner | Final approval for sensitive accounting actions |

---

## 5. Functional Requirements

| FR ID | Function | Description | Priority | Reuse Type |

|---|---|---|---|---|

| FR-ACC-001 | Accounting Setup | ตั้งค่าบริษัท เลขผู้เสียภาษี สาขา รอบบัญชี เลขที่เอกสาร | Must | Adapt |

| FR-ACC-002 | Chart of Accounts | สร้างและจัดการผังบัญชี | Must | New |

| FR-ACC-003 | Journal Entry | บันทึกรายการบัญชี เดบิต เครดิต | Must | New |

| FR-ACC-004 | Journal Approval | ส่งอนุมัติรายการบัญชี | Must | Reuse Approval |

| FR-ACC-005 | Journal Posting | Post รายการบัญชีหลังอนุมัติ | Must | New |

| FR-ACC-006 | Reverse Journal | กลับรายการบัญชีที่ post แล้ว | Must | New |

| FR-ACC-007 | Accounts Receivable | จัดการลูกหนี้ ใบแจ้งหนี้ ใบเสร็จ | Must | New |

| FR-ACC-008 | Accounts Payable | จัดการเจ้าหนี้ บิลซื้อ ใบสำคัญจ่าย | Must | New |

| FR-ACC-009 | VAT Management | จัดการภาษีซื้อ ภาษีขาย และรายงาน ภ.พ.30 | Must | New |

| FR-ACC-010 | WHT Management | คำนวณและออกหนังสือรับรองหัก ณ ที่จ่าย | Must | New |

| FR-ACC-011 | Tax Invoice | ออกใบกำกับภาษีเต็มรูป / อย่างย่อ ถ้ารองรับ | Must | New |

| FR-ACC-012 | Credit / Debit Note | ออกใบลดหนี้ / ใบเพิ่มหนี้ | Must | New |

| FR-ACC-013 | Bank & Cash | รับเงิน จ่ายเงิน โอนเงิน กระทบยอด | Must | New |

| FR-ACC-014 | Period Closing | ปิดงวดบัญชี ล็อกการแก้ไขย้อนหลัง | Must | New |

| FR-ACC-015 | Financial Reports | งบทดลอง GL งบกำไรขาดทุน งบฐานะการเงิน | Must | New |

| FR-ACC-016 | Evidence Attachment | แนบเอกสารหลักฐานทุก transaction สำคัญ | Must | Reuse Evidence |

| FR-ACC-017 | Audit Trail | บันทึก audit log ทุก action สำคัญ | Must | Reuse Audit |

| FR-ACC-018 | Export Reports | Export รายงานเป็น PDF / Excel / CSV | Should | Adapt |

| FR-ACC-019 | API Integration | เปิด API สำหรับ Sales, Purchase, Inventory, Bank | Should | Reuse Integration |

| FR-ACC-020 | Multi-Company / Branch Accounting | แยกรายการตามบริษัท สาขา แผนก โครงการ | Must | Reuse Tenant Scope |

---

## 6. Business Rules

| BR ID | Rule |

|---|---|

| BR-ACC-001 | Journal Entry ต้องมี Debit = Credit ก่อนบันทึกหรือ post |

| BR-ACC-002 | รายการที่ post แล้วห้ามแก้ไขโดยตรง ต้อง reverse หรือ adjustment |

| BR-ACC-003 | เอกสารภาษีต้องมีเลขผู้เสียภาษีและข้อมูลสาขาที่เกี่ยวข้อง |

| BR-ACC-004 | งวดบัญชีที่ปิดแล้วห้ามเพิ่ม แก้ไข หรือลบ transaction |

| BR-ACC-005 | Transaction สำคัญต้องมี evidence ก่อนส่งอนุมัติ |

| BR-ACC-006 | การอนุมัติทุกครั้งต้องบันทึก approver, timestamp, decision |

| BR-ACC-007 | WHT ต้องคำนวณจากประเภทค่าใช้จ่ายและอัตราที่ตั้งค่าไว้ |

| BR-ACC-008 | VAT ซื้อและ VAT ขายต้องแยกตามเดือนภาษี |

| BR-ACC-009 | เลขที่เอกสารต้อง unique ภายใต้ tenant/company/branch/document type |

| BR-ACC-010 | ผู้ใช้ต้องมี permission ตาม role และ scope ก่อนเข้าถึงรายการบัญชี |

---

## 7. Workflow

### WF-ACC-001 Journal Entry Workflow

1. Accountant สร้าง Journal Entry

2. ระบบตรวจ Debit = Credit

3. แนบ evidence

4. ส่งอนุมัติ

5. Approver อนุมัติ / Reject / Request Revision

6. ระบบ post journal เมื่ออนุมัติ

7. ระบบบันทึก audit trail

8. รายการแสดงใน GL และรายงานการเงิน

### WF-ACC-002 Expense / AP Workflow

1. Accountant บันทึกบิลซื้อ

2. ระบุ vendor, tax invoice, VAT, WHT

3. แนบหลักฐาน

4. ส่งอนุมัติ

5. Finance จ่ายเงิน

6. ระบบออก payment voucher

7. ระบบ post accounting

8. รายการเข้า VAT/WHT report

### WF-ACC-003 AR / Receipt Workflow

1. สร้าง invoice

2. ออก tax invoice

3. รับชำระเงิน

4. ออก receipt

5. ระบบ post accounting

6. ระบบบันทึก VAT ขาย

7. รายการเข้า AR aging และรายงานภาษี

### WF-ACC-004 Period Closing Workflow

1. Accountant เรียกตรวจ pre-close checklist

2. ระบบตรวจ unposted transaction

3. ระบบตรวจ missing evidence

4. ระบบตรวจ pending approval

5. Accounting Admin ปิดงวด

6. ระบบ lock period

7. ระบบบันทึก audit trail

---

## 8. Data Entities

| Entity | Key Fields |

|---|---|

| Account | account\_id, account\_code, account\_name, account\_type, parent\_account\_id |

| JournalEntry | journal\_id, journal\_no, journal\_date, status, total\_debit, total\_credit |

| JournalLine | line\_id, journal\_id, account\_id, debit, credit, description |

| Customer | customer\_id, tax\_id, branch\_code, name |

| Vendor | vendor\_id, tax\_id, branch\_code, name |

| Invoice | invoice\_id, invoice\_no, customer\_id, invoice\_date, amount, vat\_amount, status |

| Bill | bill\_id, bill\_no, vendor\_id, bill\_date, amount, vat\_amount, wht\_amount, status |

| TaxInvoice | tax\_invoice\_id, tax\_invoice\_no, tax\_date, tax\_type, vat\_amount |

| Receipt | receipt\_id, receipt\_no, receipt\_date, payment\_method, amount |

| PaymentVoucher | voucher\_id, voucher\_no, payment\_date, vendor\_id, amount |

| WHTCertificate | wht\_id, certificate\_no, vendor\_id, wht\_rate, wht\_amount |

| BankAccount | bank\_account\_id, bank\_name, account\_no, currency |

| AccountingPeriod | period\_id, fiscal\_year, period\_month, status |

| Evidence | evidence\_id, ref\_type, ref\_id, file\_url, uploaded\_by |

| AuditLog | audit\_id, ref\_type, ref\_id, action, actor\_id, timestamp |

---

## 9. API Mapping

| API ID | Method | Endpoint | Purpose |

|---|---|---|---|

| API-ACC-001 | GET | /api/accounting/accounts | Get chart of accounts |

| API-ACC-002 | POST | /api/accounting/accounts | Create account |

| API-ACC-003 | POST | /api/accounting/journals | Create journal |

| API-ACC-004 | POST | /api/accounting/journals/{id}/submit | Submit journal for approval |

| API-ACC-005 | POST | /api/accounting/journals/{id}/post | Post journal |

| API-ACC-006 | POST | /api/accounting/journals/{id}/reverse | Reverse posted journal |

| API-ACC-007 | POST | /api/accounting/invoices | Create invoice |

| API-ACC-008 | POST | /api/accounting/bills | Create vendor bill |

| API-ACC-009 | GET | /api/accounting/vat-report | Get VAT report |

| API-ACC-010 | GET | /api/accounting/wht-report | Get WHT report |

| API-ACC-011 | POST | /api/accounting/payments | Create payment |

| API-ACC-012 | POST | /api/accounting/receipts | Create receipt |

| API-ACC-013 | POST | /api/accounting/periods/{id}/close | Close accounting period |

| API-ACC-014 | GET | /api/accounting/reports/trial-balance | Trial balance |

| API-ACC-015 | GET | /api/accounting/reports/general-ledger | General ledger |

---

## 10. UI / Screen Mapping

| Screen ID | Screen Name | Related FR |

|---|---|---|

| SCR-ACC-001 | Accounting Dashboard | FR-ACC-015 |

| SCR-ACC-002 | Accounting Setup | FR-ACC-001 |

| SCR-ACC-003 | Chart of Accounts | FR-ACC-002 |

| SCR-ACC-004 | Journal Entry List | FR-ACC-003 |

| SCR-ACC-005 | Journal Entry Form | FR-ACC-003 |

| SCR-ACC-006 | AR Invoice | FR-ACC-007 |

| SCR-ACC-007 | AP Bill | FR-ACC-008 |

| SCR-ACC-008 | VAT Report | FR-ACC-009 |

| SCR-ACC-009 | WHT Certificate | FR-ACC-010 |

| SCR-ACC-010 | Tax Invoice / Receipt | FR-ACC-011 |

| SCR-ACC-011 | Bank & Cash | FR-ACC-013 |

| SCR-ACC-012 | Period Closing | FR-ACC-014 |

| SCR-ACC-013 | Financial Reports | FR-ACC-015 |

| SCR-ACC-014 | Evidence Panel | FR-ACC-016 |

| SCR-ACC-015 | Audit Log Viewer | FR-ACC-017 |

---

## 11. Acceptance Criteria

| AC ID | Given | When | Then |

|---|---|---|---|

| AC-ACC-001 | ผู้ใช้สร้าง journal | Debit และ Credit ไม่เท่ากัน | ระบบต้องไม่ให้ submit |

| AC-ACC-002 | Journal มี evidence ครบ | ผู้ใช้ submit approval | ระบบต้องสร้าง approval task |

| AC-ACC-003 | Approver อนุมัติ journal | ระบบ post รายการ | รายการต้องแสดงใน GL |

| AC-ACC-004 | Journal post แล้ว | ผู้ใช้พยายามแก้ไข | ระบบต้องปฏิเสธและให้ reverse เท่านั้น |

| AC-ACC-005 | มีรายการ VAT ซื้อ/ขาย | ผู้ใช้เปิด VAT report | ระบบต้องแสดงยอดแยกตามเดือนภาษี |

| AC-ACC-006 | มีรายการ WHT | ผู้ใช้สร้าง certificate | ระบบต้องคำนวณยอดและสร้างเลขเอกสาร |

| AC-ACC-007 | งวดปิดแล้ว | ผู้ใช้เพิ่ม transaction ย้อนหลัง | ระบบต้อง block |

| AC-ACC-008 | ผู้ใช้ไม่มี permission | เข้าหน้ารายงานบัญชี | ระบบต้องปฏิเสธการเข้าถึง |

| AC-ACC-009 | มีเอกสารบัญชี | ผู้ใช้แนบ evidence | ระบบต้องบันทึกไฟล์พร้อม audit |

| AC-ACC-010 | รายการอนุมัติถูก reject | ผู้ใช้เปิดเอกสาร | สถานะต้องเป็น Rejected และแก้ไขส่งใหม่ได้ |

---

## 12. Traceability Matrix

| FR | BR | DB | API | UI | AC |

|---|---|---|---|---|---|

| FR-ACC-001 | BR-ACC-009 | AccountingPeriod | API-ACC-013 | SCR-ACC-002 | AC-ACC-007 |

| FR-ACC-002 | BR-ACC-010 | Account | API-ACC-001, API-ACC-002 | SCR-ACC-003 | AC-ACC-008 |

| FR-ACC-003 | BR-ACC-001 | JournalEntry, JournalLine | API-ACC-003 | SCR-ACC-004, SCR-ACC-005 | AC-ACC-001 |

| FR-ACC-004 | BR-ACC-006 | JournalEntry, AuditLog | API-ACC-004 | SCR-ACC-005 | AC-ACC-002 |

| FR-ACC-005 | BR-ACC-002 | JournalEntry, JournalLine | API-ACC-005 | SCR-ACC-005 | AC-ACC-003 |

| FR-ACC-006 | BR-ACC-002 | JournalEntry | API-ACC-006 | SCR-ACC-005 | AC-ACC-004 |

| FR-ACC-007 | BR-ACC-008 | Invoice, Receipt | API-ACC-007, API-ACC-012 | SCR-ACC-006 | AC-ACC-005 |

| FR-ACC-008 | BR-ACC-007 | Bill, PaymentVoucher | API-ACC-008, API-ACC-011 | SCR-ACC-007 | AC-ACC-006 |

| FR-ACC-009 | BR-ACC-008 | TaxInvoice | API-ACC-009 | SCR-ACC-008 | AC-ACC-005 |

| FR-ACC-010 | BR-ACC-007 | WHTCertificate | API-ACC-010 | SCR-ACC-009 | AC-ACC-006 |

| FR-ACC-014 | BR-ACC-004 | AccountingPeriod | API-ACC-013 | SCR-ACC-012 | AC-ACC-007 |

| FR-ACC-016 | BR-ACC-005 | Evidence | - | SCR-ACC-014 | AC-ACC-009 |

| FR-ACC-017 | BR-ACC-006 | AuditLog | - | SCR-ACC-015 | AC-ACC-010 |

---

## 13. Evidence Matching

| Requirement | Evidence Status | Evidence Type |

|---|---|---|

| SaaS reuse | Verified | Repository README / SaaS Foundation |

| No Evidence = No Progress | Verified | Repository README |

| Functional AI folder ownership | Verified | Repository README |

| ACC module need | Partial | Module expansion / Business domain |

| Thai VAT / WHT details | Pending Legal Review | Thailand compliance source required |

| API details | Draft | Functional AI design |

| DB details | Draft | Functional AI design |

| UI details | Draft | Functional AI design |

---

## 14. SaaS Alignment Check

| Checkpoint | Status |

|---|---|

| Multi-Tenant | Required |

| Tenant Data Isolation | Required |

| IAM | Reuse |

| RBAC | Reuse |

| Approval Workflow | Reuse |

| Notification | Reuse |

| Audit Trail | Reuse |

| Evidence Management | Reuse |

| Subscription / Module Activation | Reuse |

| API-First | Required |

| Configuration Driven | Required |

| Security Review | Required |

| QA / UAT Mapping | Required |

---

## 15. Claude Handoff

Claude AI should review:

1. Missing accounting requirements

2. Ambiguous Thai compliance rules

3. VAT / WHT completeness

4. API coverage

5. DB entity completeness

6. SaaS alignment

7. Clean Room compliance

8. Duplicate with existing repository files

Expected Claude Output:

- Review Summary

- Gap List

- Risk List

- Recommended Adjustment

- Evidence Status

- Approval / Hold Decision

---

## 16. Open Questions

| ID | Question | Owner |

|---|---|---|

| OQ-ACC-001 | ต้องรองรับ e-Tax Invoice / e-Receipt ตั้งแต่ Phase แรกหรือ Phase ถัดไป | Boss |

| OQ-ACC-002 | ต้องรองรับหลาย currency หรือเฉพาะ THB ใน Phase แรก | Boss |

| OQ-ACC-003 | ต้องมี cost center / project accounting ตั้งแต่ Phase แรกหรือไม่ | Boss |

| OQ-ACC-004 | ต้อง export ภ.พ.30 / ภ.ง.ด.3 / ภ.ง.ด.53 เป็น format ใด | Accounting Owner |

| OQ-ACC-005 | ต้องเชื่อมธนาคารจริงหรือ import bank statement ก่อน | Boss / Finance Owner |

---

## 17. Assumptions

| ID | Assumption |

|---|---|

| AS-ACC-001 | โมดูลนี้จะใช้ SaaS Foundation ที่มีอยู่แล้ว |

| AS-ACC-002 | Phase แรกเน้น functional completeness ก่อน direct government filing |

| AS-ACC-003 | เอกสารภาษีต้องผ่าน legal/accounting review ก่อน development |

| AS-ACC-004 | API/DB/UI mapping เป็น draft เพื่อให้ Claude และ Architecture review ต่อ |

| AS-ACC-005 | ระบบต้องรองรับ tenant/company/branch scope ทุก transaction |

---

## 18. Clean Room Compliance

| Check | Status |

|---|---|

| ไม่อ้างอิงหน้าจอหรือ workflow เฉพาะของคู่แข่ง | Pass |

| ออกแบบจาก business need และ accounting principle | Pass |

| แยก assumption และ open question | Pass |

| รองรับ SaaS และ multi-tenant | Pass |

| มี traceability เบื้องต้น | Pass |

| ต้องรอ Claude / PMO review ก่อน approved | Pending |

---

## 19. State 2 Result

Status: Draft Completed

Next Gate: Claude Review / PMO Review

Next State: State 3 - ACC-001 Claude Review & Evidence Matching