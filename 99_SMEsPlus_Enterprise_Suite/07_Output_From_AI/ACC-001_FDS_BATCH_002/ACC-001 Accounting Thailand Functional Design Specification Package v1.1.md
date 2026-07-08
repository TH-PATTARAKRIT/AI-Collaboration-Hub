# ACC-001 Accounting Thailand Functional Design Specification Package

Version: v1.1
Previous Version: v1.0
Batch: FDS-ACC-BATCH-002
Status: DRAFTED — REVISION REQUIRED BEFORE GATE
Gate Status: HOLD / REVIEW REQUIRED
Owner: Functional Specification AI
Revised By: Claude AI (SMEsPlus Expert FDS Designer, /L99.99)
Revision Authorization: Boss — /L99.99 AUTHORIZE FDS-ACC-BATCH-002 (2026-07-07)
Working Rule: L99
Project: SMEsPlus Enterprise Suite
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Branch: SMEsPlus
Path: 99_SMEsPlus_Enterprise_Suite/02_Functional_Design/ACC-001 Accounting Thailand Functional Design Specification Package v1.1.md
Source v1.0 SHA256: 4c38d189a0a4358c (prefix, commit 6a947c90d616)
Revision Sources: ACC-001_CLAUDE_STATE3_REVIEW_COMMENTS.md (SMEPLUS-STATE03-ACC-CLREV-001); ACC-001_REMAINING_GAPS_CONFIRMATION.md; ACC-001_REVISION_SCOPE_PROPOSAL.md
Generated: 2026-07-08 (Asia/Bangkok)

---

## Revision History

| Version | Date | Changed By | Change Summary |
|---|---|---|---|
| v1.0 | 2026-07-01 | Functional Specification AI | Initial draft — State 2 complete |
| v1.1 | 2026-07-08 | Claude AI (FDS-ACC-BATCH-002) | REV-01 Posting Rules; REV-02 Traceability fix; REV-03 Thai Tax Annex; REV-04 Data model extension; REV-05 API extension; REV-06 UI mapping fix; REV-07 AC expansion; REV-09 Governance wording; REV-10 artifact sync |

---

## 1. Executive Summary

ACC-001 Accounting Thailand เป็นโมดูลบัญชีสำหรับธุรกิจไทยบน SaaS Platform ของ SMEsPlus Enterprise Suite

โมดูลนี้รองรับ: General Ledger, Chart of Accounts, Journal Entry, Accounts Receivable, Accounts Payable, VAT ซื้อ/VAT ขาย, Withholding Tax, ใบกำกับภาษี, ใบเสร็จรับเงิน, ใบลดหนี้/ใบเพิ่มหนี้, Bank/Cash, Period Closing, Financial Reports, Evidence & Audit Trail

โมดูลนี้ต้อง reuse SaaS Foundation เดิม ได้แก่ Tenant, IAM, Role Permission, Approval, Notification, Audit, Evidence, Integration, Configuration และ Security

**v1.1 Revision Note:** Added Posting Rules (§6-A), Thai Tax Detail Annex (§6-B), extended data model (§8), extended API (§9), fixed UI mapping (§10), expanded acceptance criteria (§11), completed traceability (§12). All tax/legal content tagged LEGAL_TAX_REVIEW_REQUIRED. REV-08 items (opening balances, year-end close, multi-currency, cost center, payment allocation, petty cash, PDC) marked BOSS_DECISION_REQUIRED and excluded from implemented scope.

---

## 2. Source of Truth

| Source | Usage |
|---|---|
| 99_SMEsPlus_Enterprise_Suite/README.md | Repository structure, workflow, evidence rule |
| 01_SaaS_Foundation/ | Shared SaaS capability |
| 17_Functional_Specification_Factory/ | FDS package structure |
| AI_WORKING_INDEX.md | AI working control |
| MODULE_EXPANSION_PLAN.md | Module expansion reference |
| State 1 Repository Inventory | Reuse / Gap baseline |
| ACC-001_CLAUDE_STATE3_REVIEW_COMMENTS.md | State 3 review findings (SMEPLUS-STATE03-ACC-CLREV-001) |
| ACC-001_REMAINING_GAPS_CONFIRMATION.md | Gap confirmation GAP-ACC-001 to GAP-ACC-015 |

---

## 3. Scope

### In Scope

- Accounting setup (company, tax ID, branch, fiscal year, document sequences, tax codes, WHT types)
- Chart of accounts
- Journal entry, approval, posting, reversal
- AR / AP accounting (invoice, bill, receipt, payment voucher)
- VAT management (input / output VAT, ภ.พ.30)
- WHT management (certificate issuance, ภ.ง.ด.3 / ภ.ง.ด.53)
- Tax invoice (full form) / Receipt / Credit note / Debit note
- Bank and cash transaction
- Bank statement import and reconciliation
- Period closing
- Financial reports (trial balance, GL, P&L, balance sheet)
- Audit and evidence control
- API / DB / UI / AC mapping

### Out of Scope (Phase 1)

- Full payroll calculation
- Full inventory costing engine
- Full manufacturing cost accounting
- Bank direct payment execution
- Direct e-Filing submission — pending OQ-ACC-001 Boss decision (BOSS_DECISION_REQUIRED)
- Certified e-Tax Invoice / e-Receipt — pending OQ-ACC-001 Boss decision (BOSS_DECISION_REQUIRED)
- Abbreviated tax invoice (อย่างย่อ) — pending Boss decision (BOSS_DECISION_REQUIRED)
- Multi-currency — pending OQ-ACC-002 Boss decision (BOSS_DECISION_REQUIRED)
- Cost center / project accounting — pending OQ-ACC-003 Boss decision (BOSS_DECISION_REQUIRED)
- Opening balances / data migration — pending Boss decision (BOSS_DECISION_REQUIRED / REV-08)
- Fiscal year-end close to retained earnings — pending Boss decision (BOSS_DECISION_REQUIRED / REV-08)
- Payment allocation across multiple invoices — pending Boss decision (BOSS_DECISION_REQUIRED / REV-08)
- AR / AP aging report — pending Boss decision (BOSS_DECISION_REQUIRED / REV-08)
- Advance payment / deposit with VAT — pending Boss decision (BOSS_DECISION_REQUIRED / REV-08)
- Petty cash / post-dated cheques — pending Boss decision (BOSS_DECISION_REQUIRED / REV-08)
- Recurring / template journals — Phase 2 candidate

---

## 4. User Roles

| Role | Responsibility |
|---|---|
| Accounting Admin | Configure accounting master data, tax codes, WHT types, sequences |
| Accountant | Create journal, invoice, bill, tax records, credit/debit notes |
| Finance Officer | Handle payment, receipt, bank, cash, bank reconciliation |
| Approver | Approve accounting documents |
| Auditor | Review evidence, audit trail, financial records |
| Tenant Admin | Manage user access and company scope |
| Boss / Owner | Final approval for sensitive accounting actions |

### Role × Screen Access Matrix

| Screen | Accounting Admin | Accountant | Finance Officer | Approver | Auditor | Tenant Admin |
|---|---|---|---|---|---|---|
| SCR-ACC-002 Setup | Edit | View | — | — | View | Edit |
| SCR-ACC-003 Chart of Accounts | Edit | View | — | — | View | — |
| SCR-ACC-004/005 Journal | — | Create/Edit | — | Approve | View | — |
| SCR-ACC-006 AR Invoice | — | Create | — | Approve | View | — |
| SCR-ACC-007 AP Bill | — | Create | — | Approve | View | — |
| SCR-ACC-008 VAT Report | View | View | View | — | View | — |
| SCR-ACC-009 WHT Certificate | — | Create | — | — | View | — |
| SCR-ACC-010a Tax Invoice | — | Issue | — | — | View | — |
| SCR-ACC-010b Receipt | — | — | Issue | — | View | — |
| SCR-ACC-011 Bank & Cash | — | — | All | — | View | — |
| SCR-ACC-011b Bank Reconciliation | — | — | All | — | View | — |
| SCR-ACC-012 Period Closing | Admin | — | — | — | View | — |
| SCR-ACC-013 Financial Reports | View | View | View | — | View | — |
| SCR-ACC-016 Credit Note | — | Create | — | Approve | View | — |
| SCR-ACC-017 Debit Note | — | Create | — | Approve | View | — |
| SCR-ACC-018 WHT Filing Reports | — | View | — | — | View | — |
| SCR-ACC-014 Evidence Panel | All roles — view and attach per document ownership |
| SCR-ACC-015 Audit Log | — | — | — | — | View | — |

---

## 5. Functional Requirements

| FR ID | Function | Description | Priority | Reuse Type |
|---|---|---|---|---|
| FR-ACC-001 | Accounting Setup | ตั้งค่าบริษัท เลขผู้เสียภาษี สาขา รอบบัญชี เลขที่เอกสาร รหัสภาษี ประเภท WHT | Must | Adapt |
| FR-ACC-002 | Chart of Accounts | สร้างและจัดการผังบัญชี | Must | New |
| FR-ACC-003 | Journal Entry | บันทึกรายการบัญชี เดบิต เครดิต พร้อม source document linkage | Must | New |
| FR-ACC-004 | Journal Approval | ส่งอนุมัติรายการบัญชี | Must | Reuse Approval |
| FR-ACC-005 | Journal Posting | Post รายการบัญชีหลังอนุมัติ ตาม posting rules | Must | New |
| FR-ACC-006 | Reverse Journal | กลับรายการบัญชีที่ post แล้วใน period ที่เปิดอยู่ | Must | New |
| FR-ACC-007 | Accounts Receivable | จัดการลูกหนี้ ใบแจ้งหนี้ ใบเสร็จ | Must | New |
| FR-ACC-008 | Accounts Payable | จัดการเจ้าหนี้ บิลซื้อ ใบสำคัญจ่าย | Must | New |
| FR-ACC-009 | VAT Management | จัดการภาษีซื้อ ภาษีขาย รายงาน ภ.พ.30 ตาม tax point | Must | New |
| FR-ACC-010 | WHT Management | คำนวณและออกหนังสือรับรองหัก ณ ที่จ่าย ภ.ง.ด.3/53 | Must | New |
| FR-ACC-011 | Tax Invoice | ออกใบกำกับภาษีเต็มรูป ครบ mandatory fields | Must | New |
| FR-ACC-012 | Credit / Debit Note | ออกใบลดหนี้/ใบเพิ่มหนี้ พร้อม original tax invoice reference และ reason | Must | New |
| FR-ACC-013 | Bank & Cash | รับเงิน จ่ายเงิน โอนเงิน import bank statement กระทบยอด | Must | New |
| FR-ACC-014 | Period Closing | ปิดงวดบัญชี ล็อกการแก้ไขย้อนหลัง | Must | New |
| FR-ACC-015 | Financial Reports | งบทดลอง GL งบกำไรขาดทุน งบฐานะการเงิน | Must | New |
| FR-ACC-016 | Evidence Attachment | แนบเอกสารหลักฐานทุก transaction สำคัญ | Must | Reuse Evidence |
| FR-ACC-017 | Audit Trail | บันทึก audit log ทุก action สำคัญ | Must | Reuse Audit |
| FR-ACC-018 | Export Reports | Export รายงานเป็น PDF / Excel / CSV | Should | Adapt |
| FR-ACC-019 | API Integration | เปิด API สำหรับ Sales, Purchase, Inventory, Bank | Should | Reuse Integration |
| FR-ACC-020 | Multi-Company / Branch Accounting | แยกรายการตามบริษัท สาขา แผนก — tenant scoped | Must | Reuse Tenant Scope |

**FR-ACC-021 through FR-ACC-025: BOSS_DECISION_REQUIRED — deferred pending REV-08 decisions**

---

## 6. Business Rules

| BR ID | Rule |
|---|---|
| BR-ACC-001 | Journal Entry ต้องมี Debit = Credit ก่อนบันทึกหรือ post |
| BR-ACC-002 | รายการที่ post แล้วห้ามแก้ไขโดยตรง ต้อง reverse หรือ adjustment entry |
| BR-ACC-003 | เอกสารภาษีต้องมีเลขผู้เสียภาษีและข้อมูลสาขาที่เกี่ยวข้อง (5-digit branch code; 00000 = head office) |
| BR-ACC-004 | งวดบัญชีที่ปิดแล้วห้ามเพิ่ม แก้ไข หรือลบ transaction — ระบบต้องปฏิเสธทุก channel รวม API |
| BR-ACC-005 | Transaction สำคัญต้องมี evidence ก่อนส่งอนุมัติ |
| BR-ACC-006 | การอนุมัติทุกครั้งต้องบันทึก approver, timestamp, decision |
| BR-ACC-007 | WHT ต้องคำนวณจากประเภทค่าใช้จ่ายและอัตราที่ตั้งค่าไว้ใน WHTType และต้องคำนวณ ณ วันที่จ่ายเงิน ไม่ใช่วันที่บันทึกบิล |
| BR-ACC-008 | VAT ซื้อและ VAT ขายต้องแยกตามเดือนภาษี ตาม tax point ที่กำหนด (ดู §6-B) |
| BR-ACC-009 | เลขที่เอกสารต้อง unique ภายใต้ tenant/company/branch/document type/sequence; sequence reset policy per DocumentSequence config |
| BR-ACC-010 | ผู้ใช้ต้องมี permission ตาม role และ scope ก่อนเข้าถึงรายการบัญชี |
| BR-ACC-011 | Tax invoice ต้องมี mandatory fields ครบก่อน issue (ดู §6-B TH-02) |
| BR-ACC-012 | Credit/debit note ต้องระบุ original tax invoice number และ reason code |
| BR-ACC-013 | VAT rounding ต้องใช้กฎ satang rounding ที่ configured ใน tenant (ดู §6-B TH-06) |
| BR-ACC-014 | Reverse journal ต้องอยู่ใน period ที่เปิดอยู่เท่านั้น — ห้าม reverse เข้า closed period |
| BR-ACC-015 | Journal และ document ทุกรายการต้องมี source document reference (ref_type / ref_id) เพื่อ subledger drill-down |

---

## 6-A. Posting Rules

**Governance note:** Posting rules define the automatic Dr/Cr journal lines generated when each accounting document is posted. These rules are authored as functional design only. They must be reviewed by an Accounting Owner before implementation and do not override Thai accounting law or Thai Revenue Code requirements.

### PR-ACC-001 — AR Invoice Posting

| Line | Account Type | Dr / Cr | Amount | Condition |
|---|---|---|---|---|
| 1 | Accounts Receivable (AR) | Dr | Invoice amount incl. VAT | Always |
| 2 | Revenue / Sales | Cr | Net amount excl. VAT | Always |
| 3 | Output VAT (VAT Payable) | Cr | VAT amount | If VAT registered and tax point = invoice date |

Source document link: ref_type = 'invoice', ref_id = invoice_id

### PR-ACC-002 — Customer Receipt Posting

| Line | Account Type | Dr / Cr | Amount | Condition |
|---|---|---|---|---|
| 1 | Bank / Cash | Dr | Amount received | Always |
| 2 | Accounts Receivable (AR) | Cr | Amount received | Always |
| 3 | Output VAT (VAT Payable) | Cr | VAT amount | If tax point = payment receipt (service) |

Source document link: ref_type = 'receipt', ref_id = receipt_id

### PR-ACC-003 — Vendor Bill Posting

| Line | Account Type | Dr / Cr | Amount | Condition |
|---|---|---|---|---|
| 1 | Expense / Asset | Dr | Net amount excl. VAT | Always |
| 2 | Input VAT (VAT Receivable) | Dr | VAT amount | If VAT claimable |
| 3 | Accounts Payable (AP) | Cr | Bill total incl. VAT | Always |

Source document link: ref_type = 'bill', ref_id = bill_id

### PR-ACC-004 — Vendor Payment with WHT

| Line | Account Type | Dr / Cr | Amount | Condition |
|---|---|---|---|---|
| 1 | Accounts Payable (AP) | Dr | Bill total | Always |
| 2 | Bank / Cash | Cr | Amount paid (net of WHT) | Always |
| 3 | WHT Payable | Cr | WHT amount | If WHT applicable |

Source document link: ref_type = 'payment_voucher', ref_id = voucher_id
WHT timing: WHT obligation arises at payment date, not bill date (BR-ACC-007)

### PR-ACC-005 — Credit Note Posting

| Line | Account Type | Dr / Cr | Amount | Condition |
|---|---|---|---|---|
| 1 | Revenue / Sales | Dr | Net amount of credit | Always |
| 2 | Output VAT (VAT Payable) | Dr | VAT adjustment amount | If original had VAT |
| 3 | Accounts Receivable (AR) | Cr | Total credit amount | Always |

Source document link: ref_type = 'credit_note', ref_id = credit_note_id; original_tax_invoice_id must be set

### PR-ACC-006 — Debit Note Posting

| Line | Account Type | Dr / Cr | Amount | Condition |
|---|---|---|---|---|
| 1 | Accounts Receivable (AR) | Dr | Total debit amount | Always |
| 2 | Revenue / Sales | Cr | Net debit amount | Always |
| 3 | Output VAT (VAT Payable) | Cr | VAT adjustment amount | If additional VAT applies |

Source document link: ref_type = 'debit_note', ref_id = debit_note_id; original_tax_invoice_id must be set

### PR-ACC-007 — Reversal Posting

| Line | Account Type | Dr / Cr | Amount | Condition |
|---|---|---|---|---|
| All original lines | Opposite of original | Opposite | Same amounts | Always |

Rules:
- Reversal must be posted to an open period (BR-ACC-014)
- Reversal journal carries ref_type = 'reversal', ref_id = original journal_id
- Reversal creates a new journal_id; original journal is marked status = 'reversed'
- System blocks reversal if target period is closed

### PR-ACC-008 — Closed Period Rejection

No posting occurs. System returns error code `ERR-ACC-PERIOD-CLOSED` with:
- period_id of the blocked period
- Suggested alternative: open a correction period (Accounting Admin action) or post to next open period

---

## 6-B. Thai Tax Detail Annex

**LEGAL_TAX_REVIEW_REQUIRED — All items in this annex are functional design drafts. They must be reviewed and confirmed by a qualified Thai accounting professional or legal advisor before any development or compliance claim is made. None of these items constitute tax advice.**

### TH-01 — VAT Tax Point (จุดความรับผิดในภาษีมูลค่าเพิ่ม)

| Transaction Type | Tax Point Rule | Notes |
|---|---|---|
| Sale of goods | Date of delivery or transfer of ownership | Earlier of delivery or payment |
| Sale of services | Date of payment receipt | Each payment installment triggers VAT |
| Continuous services | Date of invoice issuance (per period) | Per Revenue Department guidance |
| Import | Date of customs clearance | — |

System must capture tax_point_date separately from document_date.
ภ.พ.30 report month is determined by tax_point_date, not invoice_date.

**LEGAL_TAX_REVIEW_REQUIRED**

### TH-02 — Tax Invoice Mandatory Fields (ใบกำกับภาษีเต็มรูป)

All of the following must be present before a tax invoice can be issued (FR-ACC-011, BR-ACC-011):

| Field | Requirement |
|---|---|
| Document title | The words "ใบกำกับภาษี" must appear prominently |
| Seller legal name | Full legal name as registered with Revenue Department |
| Seller address | Full Thai address |
| Seller tax ID | 13-digit tax identification number |
| Seller branch code | 5-digit branch code; 00000 = สำนักงานใหญ่ |
| Buyer name | Full name (individual or juristic) |
| Buyer address | Full Thai address |
| Buyer tax ID | Required if buyer is VAT-registered juristic entity |
| Buyer branch code | Required if buyer provided one |
| Serial number | Unique document number per DocumentSequence |
| Issue date | Date of issue (must not be backdated into closed period) |
| Description of goods/services | Clear description per line item |
| Quantity and unit | Per line item |
| Unit price | Per line item, excl. VAT |
| Total amount excl. VAT | Sum of line items |
| VAT rate | Displayed as percentage (e.g., 7%) |
| VAT amount | Shown as separate line item |
| Total amount incl. VAT | Grand total |

**LEGAL_TAX_REVIEW_REQUIRED**

### TH-03 — Credit Note and Debit Note Tax Treatment

| Requirement | Rule |
|---|---|
| Original tax invoice reference | credit_note / debit_note must carry original_tax_invoice_no and original_tax_invoice_date |
| Reason code | Must specify reason (e.g., price reduction, return, incorrect amount) |
| VAT adjustment | VAT report (ภ.พ.30) must be adjusted in the month the credit/debit note is issued, not the original month |
| Document title | "ใบลดหนี้" or "ใบเพิ่มหนี้" must appear prominently |
| Seller / Buyer fields | Same mandatory fields as tax invoice |

**LEGAL_TAX_REVIEW_REQUIRED**

### TH-04 — WHT Certificate Content (หนังสือรับรองการหักภาษี ณ ที่จ่าย / 50 ทวิ)

| Field | Requirement |
|---|---|
| Payer name, address, tax ID | Full details |
| Payee name, address, tax ID | Full details |
| Type of income (ประเภทเงินได้) | Classified per Revenue Code sections |
| Payment date | Date payment was made (WHT obligation date) |
| Gross payment amount | Before WHT deduction |
| WHT rate | Per WHTType configuration |
| WHT amount withheld | Computed amount |
| Certificate serial number | Per DocumentSequence |

WHT timing rule: WHT obligation arises at date of payment, not date of bill recording (BR-ACC-007).

**LEGAL_TAX_REVIEW_REQUIRED**

### TH-05 — ภ.ง.ด.3 and ภ.ง.ด.53 Report Requirements

| Report | Applicable To | Frequency | Key Data |
|---|---|---|---|
| ภ.ง.ด.3 | WHT on payments to individuals | Monthly | Payee name, tax ID, income type, amount, WHT amount |
| ภ.ง.ด.53 | WHT on payments to juristic entities | Monthly | Same as ภ.ง.ด.3 |

System must support:
- Monthly aggregation of WHT records per report type
- Export in format required by Revenue Department (format TBD — pending OQ-ACC-004 Boss decision)
- Drill-down from report line to source certificate

Cross-border WHT (ภ.ง.ด.54 / ภ.พ.36): **BOSS_DECISION_REQUIRED — out of Phase 1 scope unless explicitly authorized**

**LEGAL_TAX_REVIEW_REQUIRED**

### TH-06 — Satang Rounding Rule

| Scenario | Rule |
|---|---|
| VAT rounding per line | Round half-up (0.5 satang → 1 satang) per line item |
| VAT rounding per document | Sum of rounded line VATs vs. document-level rounding — system must use one consistent method configured per tenant |
| Rounding difference | If rounding difference exists between tax invoice and receipt, post to Rounding Difference account |

The rounding method (per-line vs per-document) must be configured in TaxCode and applied consistently across tax invoice, VAT report, and GL.

**LEGAL_TAX_REVIEW_REQUIRED**

### TH-07 — Document Numbering and Cancellation Policy

| Rule | Detail |
|---|---|
| Sequence reset | Per DocumentSequence config: yearly reset (e.g., YYYY-NNNNNN), monthly reset, or no reset — per tenant / branch |
| Uniqueness | BR-ACC-009: unique per tenant / company / branch / document_type |
| Cancelled document | Cancelled tax invoice must retain its number; number cannot be reused; document must be marked cancelled with audit log |
| Gap in sequence | Gaps caused by cancellation are allowed; system must not auto-fill gaps |
| Retention | Cancelled documents must be retained for Revenue Department inspection (retention period: LEGAL_TAX_REVIEW_REQUIRED) |

**LEGAL_TAX_REVIEW_REQUIRED**

### TH-08 — Branch Code Convention

| Value | Meaning |
|---|---|
| 00000 | สำนักงานใหญ่ (Head Office) |
| 00001–99999 | Branch number as registered |

Seller branch code must be captured from company setup (FR-ACC-001).
Buyer branch code must be captured from Customer master (if VAT-registered) and displayed on tax invoice.

**LEGAL_TAX_REVIEW_REQUIRED**

### TH-09 — TaxCode and WHT Rate Configuration

**TaxCode entity fields:**

| Field | Type | Description |
|---|---|---|
| tax_code_id | UUID | PK |
| tenant_id | UUID | Tenant scope |
| code | VARCHAR(20) | e.g., VAT7, VAT0, EXEMPT |
| rate | DECIMAL(5,2) | e.g., 7.00, 0.00 |
| tax_type | ENUM | OUTPUT, INPUT, EXEMPT, NON_CLAIMABLE |
| description_th | TEXT | Thai description |
| description_en | TEXT | English description |
| is_active | BOOLEAN | — |

**WHTType entity fields:**

| Field | Type | Description |
|---|---|---|
| wht_type_id | UUID | PK |
| tenant_id | UUID | Tenant scope |
| income_type_code | VARCHAR(10) | Revenue Code section |
| description_th | TEXT | Thai description |
| rate | DECIMAL(5,2) | WHT rate percentage |
| report_type | ENUM | PND3, PND53 |
| is_active | BOOLEAN | — |

**LEGAL_TAX_REVIEW_REQUIRED**

---

## 7. Workflow

### WF-ACC-001 Journal Entry Workflow

1. Accountant สร้าง Journal Entry (status = Draft)
2. ระบบตรวจ Debit = Credit (BR-ACC-001)
3. แนบ evidence (BR-ACC-005)
4. ส่งอนุมัติ (status = Submitted)
5. Approver อนุมัติ → status = Approved / Reject → status = Rejected / Request Revision → status = Revision_Requested
6. ระบบ post journal เมื่ออนุมัติ (status = Posted) ตาม Posting Rules §6-A
7. ระบบบันทึก audit trail (BR-ACC-006)
8. รายการแสดงใน GL และรายงานการเงิน

**Document Status Enumeration:** Draft → Submitted → Approved → Posted → Reversed | Rejected | Revision_Requested

### WF-ACC-002 Expense / AP Workflow

1. Accountant บันทึกบิลซื้อ (status = Draft)
2. ระบุ vendor, tax invoice no., tax_point_date, VAT (TaxCode), WHT (WHTType)
3. แนบหลักฐาน
4. ส่งอนุมัติ
5. Finance จ่ายเงิน — WHT คำนวณ ณ วันที่จ่าย (BR-ACC-007)
6. ระบบออก payment voucher + WHT certificate
7. ระบบ post ตาม PR-ACC-003 (bill) และ PR-ACC-004 (payment)
8. รายการเข้า VAT input report และ WHT report

### WF-ACC-003 AR / Receipt Workflow

1. สร้าง invoice (status = Draft)
2. ออก tax invoice (FR-ACC-011) — ตรวจ mandatory fields (BR-ACC-011)
3. รับชำระเงิน → ออก receipt
4. ระบบ post ตาม PR-ACC-001 (invoice) และ PR-ACC-002 (receipt)
5. ระบบบันทึก VAT ขาย ตาม tax_point_date (TH-01)
6. รายการเข้า AR และรายงานภาษี (ภ.พ.30)

### WF-ACC-004 Period Closing Workflow

1. Accountant Admin เรียก pre-close checklist
2. ระบบตรวจ unposted transactions
3. ระบบตรวจ missing evidence
4. ระบบตรวจ pending approvals
5. Accounting Admin ปิดงวด (status = Closed)
6. ระบบ lock period — ปฏิเสธ transaction ทุกประเภทรวม API (BR-ACC-004)
7. ระบบบันทึก audit trail

### WF-ACC-005 Bank Reconciliation Workflow (new)

1. Finance Officer import bank statement (FR-ACC-013)
2. ระบบ auto-match ยอดใน BankStatement กับ JournalLine
3. Finance Officer review matched / unmatched items
4. Finance Officer confirm match หรือ manual adjust
5. ระบบบันทึก ReconciliationMatch
6. ระบบ report unreconciled items

---

## 8. Data Entities

### Core Accounting Entities

| Entity | Key Fields |
|---|---|
| Account | account_id, tenant_id, company_id, account_code, account_name_th, account_name_en, account_type, parent_account_id, is_active |
| FiscalYear | fiscal_year_id, tenant_id, company_id, year_label, start_date, end_date, status (Open/Closed) |
| AccountingPeriod | period_id, fiscal_year_id, tenant_id, company_id, period_month, status (Open/Closed) |
| DocumentSequence | sequence_id, tenant_id, company_id, branch_id, document_type, prefix, current_number, reset_policy (Yearly/Monthly/None), last_reset_date |
| JournalEntry | journal_id, tenant_id, company_id, branch_id, journal_no, journal_date, status, total_debit, total_credit, ref_type, ref_id, description, created_by, approved_by, posted_at |
| JournalLine | line_id, journal_id, account_id, debit, credit, description, tax_code_id, cost_center_id (BOSS_DECISION_REQUIRED) |

### AR / AP Entities

| Entity | Key Fields |
|---|---|
| Customer | customer_id, tenant_id, name_th, name_en, tax_id, branch_code, address, is_vat_registered |
| Vendor | vendor_id, tenant_id, name_th, name_en, tax_id, branch_code, address, is_vat_registered |
| Invoice | invoice_id, tenant_id, company_id, branch_id, invoice_no, customer_id, invoice_date, tax_point_date, amount_excl_vat, vat_amount, total_amount, tax_code_id, status |
| Bill | bill_id, tenant_id, company_id, branch_id, bill_no, vendor_id, bill_date, tax_point_date, amount_excl_vat, vat_amount, wht_amount, wht_type_id, total_amount, status |
| Receipt | receipt_id, tenant_id, company_id, branch_id, receipt_no, invoice_id, receipt_date, payment_method, amount, tax_point_date |
| PaymentVoucher | voucher_id, tenant_id, company_id, branch_id, voucher_no, bill_id, payment_date, vendor_id, gross_amount, wht_amount, net_amount, bank_account_id |

### Tax Document Entities

| Entity | Key Fields |
|---|---|
| TaxInvoice | tax_invoice_id, tenant_id, company_id, branch_id, tax_invoice_no, invoice_id, tax_date, tax_point_date, seller_tax_id, seller_branch_code, buyer_name, buyer_tax_id, buyer_branch_code, amount_excl_vat, vat_amount, total_amount, tax_code_id, status |
| CreditNote | credit_note_id, tenant_id, company_id, branch_id, credit_note_no, original_tax_invoice_id, original_tax_invoice_no, original_tax_invoice_date, issue_date, reason_code, reason_text, amount_excl_vat, vat_adjustment, total_amount, status |
| DebitNote | debit_note_id, tenant_id, company_id, branch_id, debit_note_no, original_tax_invoice_id, original_tax_invoice_no, original_tax_invoice_date, issue_date, reason_code, reason_text, amount_excl_vat, vat_adjustment, total_amount, status |
| WHTCertificate | wht_id, tenant_id, company_id, branch_id, certificate_no, voucher_id, vendor_id, payment_date, income_type_code, wht_type_id, gross_amount, wht_rate, wht_amount, status |

### Tax Configuration Entities

| Entity | Key Fields |
|---|---|
| TaxCode | tax_code_id, tenant_id, code, rate, tax_type (OUTPUT/INPUT/EXEMPT/NON_CLAIMABLE), rounding_method (PerLine/PerDocument), description_th, description_en, is_active |
| WHTType | wht_type_id, tenant_id, income_type_code, description_th, rate, report_type (PND3/PND53), is_active |

### Bank / Reconciliation Entities

| Entity | Key Fields |
|---|---|
| BankAccount | bank_account_id, tenant_id, company_id, bank_name, account_no, currency (THB default), is_active |
| BankStatement | statement_id, bank_account_id, tenant_id, statement_date, imported_at, total_debit, total_credit, status (Imported/Reconciled) |
| StatementLine | stmt_line_id, statement_id, transaction_date, description, debit_amount, credit_amount, balance, is_matched |
| ReconciliationMatch | match_id, stmt_line_id, journal_line_id, matched_by, matched_at, match_type (Auto/Manual), notes |

### Shared / SaaS Foundation Entities (Reuse)

| Entity | Key Fields |
|---|---|
| Evidence | evidence_id, ref_type, ref_id, file_url, file_name, uploaded_by, uploaded_at |
| AuditLog | audit_id, tenant_id, ref_type, ref_id, action, actor_id, timestamp, before_value, after_value |

---

## 9. API Mapping

### Accounting Setup APIs

| API ID | Method | Endpoint | Purpose | Auth |
|---|---|---|---|---|
| API-ACC-001 | GET | /api/v1/accounting/accounts | Get chart of accounts | Role: Accountant+ |
| API-ACC-002 | POST | /api/v1/accounting/accounts | Create account | Role: Accounting Admin |
| API-ACC-S01 | GET | /api/v1/accounting/setup | Get accounting setup (company, tax ID, branch, fiscal config) | Role: Accounting Admin |
| API-ACC-S02 | PUT | /api/v1/accounting/setup | Update accounting setup | Role: Accounting Admin |
| API-ACC-S03 | GET | /api/v1/accounting/tax-codes | List tax codes | Role: Accountant+ |
| API-ACC-S04 | POST | /api/v1/accounting/tax-codes | Create tax code | Role: Accounting Admin |
| API-ACC-S05 | GET | /api/v1/accounting/wht-types | List WHT types | Role: Accountant+ |
| API-ACC-S06 | POST | /api/v1/accounting/wht-types | Create WHT type | Role: Accounting Admin |
| API-ACC-S07 | GET | /api/v1/accounting/document-sequences | List sequences | Role: Accounting Admin |
| API-ACC-S08 | PUT | /api/v1/accounting/document-sequences/{id} | Update sequence config | Role: Accounting Admin |

### Journal APIs

| API ID | Method | Endpoint | Purpose |
|---|---|---|---|
| API-ACC-003 | POST | /api/v1/accounting/journals | Create journal (status = Draft) |
| API-ACC-004 | POST | /api/v1/accounting/journals/{id}/submit | Submit for approval |
| API-ACC-004b | POST | /api/v1/accounting/journals/{id}/reject | Reject with reason |
| API-ACC-004c | POST | /api/v1/accounting/journals/{id}/request-revision | Request revision |
| API-ACC-005 | POST | /api/v1/accounting/journals/{id}/post | Post journal — validates period open (returns ERR-ACC-PERIOD-CLOSED if not) |
| API-ACC-006 | POST | /api/v1/accounting/journals/{id}/reverse | Reverse posted journal — validates target period open |

### AR / AP / Tax Document APIs

| API ID | Method | Endpoint | Purpose |
|---|---|---|---|
| API-ACC-007 | POST | /api/v1/accounting/invoices | Create AR invoice |
| API-ACC-008 | POST | /api/v1/accounting/bills | Create vendor bill |
| API-ACC-009 | GET | /api/v1/accounting/reports/vat | Get VAT report (ภ.พ.30) — filter by tax_month |
| API-ACC-010 | GET | /api/v1/accounting/reports/wht | Get WHT report — filter by report_type (PND3/PND53), month |
| API-ACC-011 | POST | /api/v1/accounting/tax-invoices | Issue tax invoice — validates mandatory fields (returns ERR-ACC-TI-INCOMPLETE if missing) |
| API-ACC-011b | POST | /api/v1/accounting/tax-invoices/{id}/cancel | Cancel tax invoice (number retained, status = Cancelled) |
| API-ACC-012 | POST | /api/v1/accounting/receipts | Create receipt |
| API-ACC-CN01 | POST | /api/v1/accounting/credit-notes | Create credit note (requires original_tax_invoice_id + reason_code) |
| API-ACC-CN02 | GET | /api/v1/accounting/credit-notes/{id} | Get credit note |
| API-ACC-DN01 | POST | /api/v1/accounting/debit-notes | Create debit note (requires original_tax_invoice_id + reason_code) |
| API-ACC-DN02 | GET | /api/v1/accounting/debit-notes/{id} | Get debit note |
| API-ACC-011c | POST | /api/v1/accounting/payments | Create payment (with WHT calculation) |

### Bank & Reconciliation APIs

| API ID | Method | Endpoint | Purpose |
|---|---|---|---|
| API-ACC-BS01 | POST | /api/v1/accounting/bank-statements/import | Import bank statement file |
| API-ACC-BS02 | GET | /api/v1/accounting/bank-statements/{id}/lines | Get statement lines |
| API-ACC-BS03 | POST | /api/v1/accounting/bank-statements/{id}/auto-match | Run auto-match |
| API-ACC-BS04 | POST | /api/v1/accounting/reconciliation/match | Manual match: stmt_line_id + journal_line_id |
| API-ACC-BS05 | DELETE | /api/v1/accounting/reconciliation/match/{id} | Unmatch |
| API-ACC-BS06 | GET | /api/v1/accounting/reconciliation/unreconciled | Get unreconciled items |

### Period and Report APIs

| API ID | Method | Endpoint | Purpose |
|---|---|---|---|
| API-ACC-013 | POST | /api/v1/accounting/periods/{id}/close | Close accounting period |
| API-ACC-014 | GET | /api/v1/accounting/reports/trial-balance | Trial balance |
| API-ACC-015 | GET | /api/v1/accounting/reports/general-ledger | General ledger |
| API-ACC-R01 | GET | /api/v1/accounting/reports/profit-loss | P&L report — filter by period / fiscal year |
| API-ACC-R02 | GET | /api/v1/accounting/reports/balance-sheet | Balance sheet — as of date |
| API-ACC-R03 | GET | /api/v1/accounting/reports/wht-filing/{type} | WHT filing export (PND3/PND53) — format per OQ-ACC-004 decision |
| API-ACC-018 | GET | /api/v1/accounting/reports/{report}/export | Export report as PDF / Excel / CSV |

**API Cross-Cutting Behavior:**
- All endpoints require `tenant_id` in JWT claims (not in URL)
- All list endpoints support pagination: `?page=1&page_size=50`
- POST endpoints are idempotent when `idempotency_key` header is supplied
- Closed-period violation returns `HTTP 422` with `ERR-ACC-PERIOD-CLOSED`
- Missing mandatory tax fields return `HTTP 422` with `ERR-ACC-TI-INCOMPLETE`
- Cross-tenant access returns `HTTP 403`
- API version prefix `/api/v1/` — Enterprise Architect review required for final API contract

---

## 10. UI / Screen Mapping

| Screen ID | Screen Name | Related FR | Notes |
|---|---|---|---|
| SCR-ACC-001 | Accounting Dashboard | FR-ACC-015 | — |
| SCR-ACC-002a | Accounting Setup — Company | FR-ACC-001 | Company, tax ID, branch, fiscal year |
| SCR-ACC-002b | Accounting Setup — Tax Codes | FR-ACC-001 | TaxCode config |
| SCR-ACC-002c | Accounting Setup — WHT Types | FR-ACC-001 | WHTType config |
| SCR-ACC-002d | Accounting Setup — Document Sequences | FR-ACC-001 | Sequence reset policy |
| SCR-ACC-003 | Chart of Accounts | FR-ACC-002 | — |
| SCR-ACC-004 | Journal Entry List | FR-ACC-003 | Status filter |
| SCR-ACC-005 | Journal Entry Form | FR-ACC-003/004/005 | Inline balance check; status state machine |
| SCR-ACC-006 | AR Invoice | FR-ACC-007 | — |
| SCR-ACC-007 | AP Bill | FR-ACC-008 | — |
| SCR-ACC-008 | VAT Report (ภ.พ.30) | FR-ACC-009 | Filter by tax_month |
| SCR-ACC-009 | WHT Certificate | FR-ACC-010 | — |
| SCR-ACC-010a | Tax Invoice Form | FR-ACC-011 | Mandatory field validation; separate from receipt |
| SCR-ACC-010b | Receipt Form | FR-ACC-007 | Separate from tax invoice |
| SCR-ACC-011a | Bank & Cash | FR-ACC-013 | — |
| SCR-ACC-011b | Bank Statement Import | FR-ACC-013 | File upload + auto-match trigger |
| SCR-ACC-011c | Bank Reconciliation | FR-ACC-013 | Match/unmatch UI; unreconciled list |
| SCR-ACC-012 | Period Closing | FR-ACC-014 | Pre-close checklist display |
| SCR-ACC-013a | Trial Balance | FR-ACC-015 | — |
| SCR-ACC-013b | General Ledger | FR-ACC-015 | — |
| SCR-ACC-013c | Profit & Loss Report | FR-ACC-015 | — |
| SCR-ACC-013d | Balance Sheet | FR-ACC-015 | — |
| SCR-ACC-014 | Evidence Panel | FR-ACC-016 | Reuse SaaS Foundation component |
| SCR-ACC-015 | Audit Log Viewer | FR-ACC-017 | Reuse SaaS Foundation component |
| SCR-ACC-016 | Credit Note Form | FR-ACC-012 | Requires original TI selection + reason |
| SCR-ACC-017 | Debit Note Form | FR-ACC-012 | Requires original TI selection + reason |
| SCR-ACC-018 | WHT Filing Reports (ภ.ง.ด.3/53) | FR-ACC-010 | Separate from certificate screen |
| SCR-ACC-019 | Export Panel | FR-ACC-018 | PDF/Excel/CSV per report |

**UI Cross-Cutting Requirements:**
- All posted/cancelled/closed-period documents must display as read-only with visible status badge
- Thai/English bilingual display: per-tenant configuration (BOSS_DECISION_REQUIRED for print output language)
- Print/PDF layouts for tax invoice, receipt, credit/debit note, WHT certificate, payment voucher: **layout design pending REV-03 legal review — do not send to Figma until tax content is legally reviewed**
- Buddhist Era / CE date display on tax documents: **BOSS_DECISION_REQUIRED (UIQ-ACC-003)**

**UI Handoff Status: NOT READY FOR HANDOFF — pending REV-03 legal review, entity finalization, and Boss decisions on bilingual/calendar/print scope**

---

## 11. Acceptance Criteria

### Journal / Posting

| AC ID | Given | When | Then |
|---|---|---|---|
| AC-ACC-001 | Accountant creates journal | Debit ≠ Credit | System blocks submit; displays balance error |
| AC-ACC-002 | Journal has evidence attached | Accountant submits for approval | System creates approval task |
| AC-ACC-003 | Approver approves journal | System posts | Entry appears in GL with correct Dr/Cr per §6-A |
| AC-ACC-004 | Journal is posted | User tries to edit directly | System rejects; offers Reverse action only |
| AC-ACC-005a | Accountant posts to closed period (UI) | — | System blocks; displays ERR-ACC-PERIOD-CLOSED |
| AC-ACC-005b | External caller posts to closed period via API | — | API returns HTTP 422 + ERR-ACC-PERIOD-CLOSED |
| AC-ACC-006 | Approver rejects journal | — | Status = Rejected; Accountant can revise and resubmit |
| AC-ACC-007 | Accountant requests reversal | Target period is closed | System blocks reversal; displays period status |
| AC-ACC-008 | Accountant requests reversal | Target period is open | System creates opposite-sign journal in same period |

### Period Closing

| AC ID | Given | When | Then |
|---|---|---|---|
| AC-ACC-009 | Period has unposted transactions | Accounting Admin tries to close | System shows pre-close warning list; blocks close |
| AC-ACC-010 | Period has missing evidence | Accounting Admin tries to close | System shows evidence gap list; blocks close |
| AC-ACC-011 | Period is closed | Any user adds transaction | System blocks; all channels including API |

### VAT / Tax

| AC ID | Given | When | Then |
|---|---|---|---|
| AC-ACC-012 | VAT transactions exist | User opens VAT report | System shows amounts split by tax_point_date month |
| AC-ACC-013 | AR invoice for goods | Invoice date = delivery date | tax_point_date = invoice_date; VAT posted to that month |
| AC-ACC-014 | AR invoice for services | Receipt of payment | tax_point_date = receipt_date; VAT posted to receipt month |
| AC-ACC-015 | Tax invoice form submitted | Mandatory field missing (e.g., buyer tax ID) | System returns ERR-ACC-TI-INCOMPLETE; does not issue |
| AC-ACC-016 | VAT rounding config = PerLine | Multi-line invoice | Each line VAT rounded independently; sum = document VAT |
| AC-ACC-017 | Credit note issued | Original TI field empty | System blocks; requires original_tax_invoice_id |
| AC-ACC-018 | Credit note issued | VAT adjustment | ภ.พ.30 adjusted in month of credit note, not original month |

### WHT

| AC ID | Given | When | Then |
|---|---|---|---|
| AC-ACC-019 | Vendor bill exists | Finance makes payment | WHT calculated at payment date using WHTType rate |
| AC-ACC-020 | WHT payment made | User generates certificate | System creates certificate with all mandatory fields per §6-B TH-04 |
| AC-ACC-021 | Invalid WHT rate entered | Save attempt | System validates rate against WHTType; blocks if not configured |

### Security / Access

| AC ID | Given | When | Then |
|---|---|---|---|
| AC-ACC-022 | User without permission | Accesses accounting report screen | System rejects; HTTP 403 via API |
| AC-ACC-023 | Cross-tenant API call | Any request with mismatched tenant_id | System returns HTTP 403; no data returned |

### Document Numbering

| AC ID | Given | When | Then |
|---|---|---|---|
| AC-ACC-024 | Tax invoice cancelled | Cancellation confirmed | Number retained; status = Cancelled; number not reused |
| AC-ACC-025 | Duplicate document number | Post attempt with existing number | System blocks; returns ERR-ACC-DUPLICATE-DOC-NO |

### Evidence

| AC ID | Given | When | Then |
|---|---|---|---|
| AC-ACC-026 | User attaches evidence | Any key document | System records file_url, uploaded_by, uploaded_at with audit log |
| AC-ACC-027 | User submits document without evidence | BR-ACC-005 triggered | System blocks submit; prompts evidence attachment |

---

## 12. Traceability Matrix (v1.1 — Complete)

All 20 FRs mapped. FR-ACC-001 mis-mapping corrected (GAP-ACC-009). 7 previously unmapped FRs now mapped.

| FR ID | Business Rule | Business Process | Data Entity | API | UI Screen | Acceptance Criteria | Evidence Status | Gap Status | Gate |
|---|---|---|---|---|---|---|---|---|---|
| FR-ACC-001 Accounting Setup | BR-ACC-009, BR-ACC-010 | Not in named WF (config) | DocumentSequence, TaxCode, WHTType | API-ACC-S01 to S08 | SCR-ACC-002a-d | AC-ACC-022 | EVD-v1.1-001 | ADDRESSED (was mis-mapped) | HOLD |
| FR-ACC-002 Chart of Accounts | BR-ACC-010 | Not in named WF | Account | API-ACC-001, 002 | SCR-ACC-003 | AC-ACC-022 | EVD-v1.1-001 | MATCHED | HOLD |
| FR-ACC-003 Journal Entry | BR-ACC-001, BR-ACC-015 | WF-ACC-001 | JournalEntry, JournalLine | API-ACC-003 | SCR-ACC-004, 005 | AC-ACC-001, 002 | EVD-v1.1-001 | MATCHED | HOLD |
| FR-ACC-004 Journal Approval | BR-ACC-006 | WF-ACC-001 steps 4-5 | JournalEntry, AuditLog | API-ACC-004, 004b, 004c | SCR-ACC-005 | AC-ACC-002, 006 | EVD-v1.1-001 | MATCHED | HOLD |
| FR-ACC-005 Journal Posting | BR-ACC-002 | WF-ACC-001 steps 6-8 | JournalEntry, JournalLine | API-ACC-005 | SCR-ACC-005 | AC-ACC-003 | EVD-v1.1-001 | MATCHED | HOLD |
| FR-ACC-006 Reverse Journal | BR-ACC-002, BR-ACC-014 | WF-ACC-001 (reversal branch) | JournalEntry | API-ACC-006 | SCR-ACC-005 | AC-ACC-007, 008 | EVD-v1.1-001 | MATCHED | HOLD |
| FR-ACC-007 Accounts Receivable | BR-ACC-008, BR-ACC-015 | WF-ACC-003 | Invoice, Receipt, TaxInvoice | API-ACC-007, 012 | SCR-ACC-006, 010a, 010b | AC-ACC-012, 013, 014 | EVD-v1.1-001 | MATCHED | HOLD |
| FR-ACC-008 Accounts Payable | BR-ACC-007, BR-ACC-015 | WF-ACC-002 | Bill, PaymentVoucher, WHTCertificate | API-ACC-008, 011c | SCR-ACC-007 | AC-ACC-019, 020 | EVD-v1.1-001 | MATCHED | HOLD |
| FR-ACC-009 VAT Management | BR-ACC-008, BR-ACC-013 | WF-ACC-002/003 VAT touchpoints | TaxInvoice, TaxCode | API-ACC-009 | SCR-ACC-008 | AC-ACC-012, 016, 018 | EVD-v1.1-002 (LEGAL_TAX_REVIEW_REQUIRED) | PARTIAL — legal review pending | HOLD |
| FR-ACC-010 WHT Management | BR-ACC-007 | WF-ACC-002 WHT touchpoint | WHTCertificate, WHTType | API-ACC-010, R03 | SCR-ACC-009, 018 | AC-ACC-019, 020, 021 | EVD-v1.1-002 (LEGAL_TAX_REVIEW_REQUIRED) | PARTIAL — legal review pending | HOLD |
| FR-ACC-011 Tax Invoice | BR-ACC-011, BR-ACC-009 | WF-ACC-003 | TaxInvoice, TaxCode | API-ACC-011, 011b | SCR-ACC-010a | AC-ACC-015, 024, 025 | EVD-v1.1-002 (LEGAL_TAX_REVIEW_REQUIRED) | ADDRESSED (was GAP) | HOLD |
| FR-ACC-012 Credit / Debit Note | BR-ACC-012, BR-ACC-009 | New WF (credit/debit note) | CreditNote, DebitNote | API-ACC-CN01, CN02, DN01, DN02 | SCR-ACC-016, 017 | AC-ACC-017, 018 | EVD-v1.1-002 (LEGAL_TAX_REVIEW_REQUIRED) | ADDRESSED (was GAP) | HOLD |
| FR-ACC-013 Bank & Cash | BR-ACC-015 | WF-ACC-005 | BankAccount, BankStatement, StatementLine, ReconciliationMatch | API-ACC-BS01 to BS06, 011c | SCR-ACC-011a, 011b, 011c | AC-ACC-026 | EVD-v1.1-001 | ADDRESSED (was GAP) | HOLD |
| FR-ACC-014 Period Closing | BR-ACC-004 | WF-ACC-004 | AccountingPeriod, FiscalYear | API-ACC-013 | SCR-ACC-012 | AC-ACC-009, 010, 011 | EVD-v1.1-001 | MATCHED | HOLD |
| FR-ACC-015 Financial Reports | BR-ACC-010 | Not in named WF | JournalEntry, JournalLine, Account | API-ACC-014, 015, R01, R02 | SCR-ACC-013a-d | AC-ACC-022 | EVD-v1.1-001 | ADDRESSED (was GAP) | HOLD |
| FR-ACC-016 Evidence Attachment | BR-ACC-005 | All document WFs | Evidence | (SaaS Foundation API) | SCR-ACC-014 | AC-ACC-026, 027 | EVD-v1.1-001 | MATCHED | HOLD |
| FR-ACC-017 Audit Trail | BR-ACC-006 | All document WFs | AuditLog | (SaaS Foundation API) | SCR-ACC-015 | AC-ACC-023 | EVD-v1.1-001 | MATCHED | HOLD |
| FR-ACC-018 Export Reports | BR-ACC-010 | Not in named WF | (report output) | API-ACC-018 | SCR-ACC-019 | AC-ACC-022 | EVD-v1.1-001 | ADDRESSED (was GAP) | HOLD |
| FR-ACC-019 API Integration | BR-ACC-010 | Not in named WF (API contract) | All entities | All API-ACC-* | — | AC-ACC-023 | EVD-v1.1-001 | ADDRESSED (was GAP) | HOLD |
| FR-ACC-020 Multi-Company/Branch | BR-ACC-009, BR-ACC-010 | All WFs (tenant scope) | All entities (company_id, branch_id, tenant_id) | All API-ACC-* (JWT claims) | All screens | AC-ACC-023 | EVD-v1.1-001 | ADDRESSED (was GAP) | HOLD |

**UAT Cases: Not yet defined — QA/UAT package required (gate action 7)**

---

## 13. Evidence Matching (updated v1.1)

| Requirement | Evidence Status | Evidence Type |
|---|---|---|
| SaaS reuse | EVIDENCED | Repository README / SaaS Foundation |
| No Evidence = No Progress | EVIDENCED | Repository README |
| Functional AI folder ownership | EVIDENCED | Repository README |
| ACC module need | PARTIAL | Module expansion / Business domain |
| Thai VAT / WHT details | LEGAL_TAX_REVIEW_REQUIRED | Thailand compliance — legal reviewer not yet assigned |
| Posting Rules (v1.1 new) | PARTIAL — authored, legal/accounting review pending | §6-A Posting Rules (this document) |
| API details | PARTIAL — extended in v1.1, Enterprise Architect review pending | §9 API Mapping (this document) |
| DB details | PARTIAL — extended in v1.1, DB Design AI review pending | §8 Data Entities (this document) |
| UI details | PARTIAL — extended in v1.1, UX review pending | §10 UI Mapping (this document) |
| Credit/Debit Note | PARTIAL — authored, legal review pending | §6-B TH-03; §8 CreditNote/DebitNote |
| Bank Reconciliation | PARTIAL — authored, architecture review pending | §7 WF-ACC-005; §8 Bank entities |

---

## 14. SaaS Alignment Check

| Checkpoint | Status |
|---|---|
| Multi-Tenant | Required — tenant_id on all entities |
| Tenant Data Isolation | Required — enforced via JWT + DB row filtering |
| IAM | Reuse |
| RBAC | Reuse — Role × Screen matrix added §4 |
| Approval Workflow | Reuse |
| Notification | Reuse |
| Audit Trail | Reuse |
| Evidence Management | Reuse |
| Subscription / Module Activation | Reuse |
| API-First | Required — all functions exposed via API |
| Configuration Driven | Required — TaxCode, WHTType, DocumentSequence configurable |
| Security Review | Required — pending Security Compliance AI |
| QA / UAT Mapping | Required — UAT cases not yet created |

---

## 15. Claude AI Handoff (v1.1)

Review completed at State 3 (SMEPLUS-STATE03-ACC-CLREV-001). Revision FDS-ACC-BATCH-002 addresses all REV-01 to REV-09 items except REV-08 (BOSS_DECISION_REQUIRED).

Expected next review: ChatGPT L99 → Functional Specification AI / BA / SA → Legal/Accounting Owner (§6-B) → PMO → Boss gate decision.

---

## 16. Open Questions

| ID | Question | Owner | Status |
|---|---|---|---|
| OQ-ACC-001 | e-Tax Invoice / e-Receipt phase | Boss | OPEN |
| OQ-ACC-002 | Multi-currency Phase 1 yes/no | Boss | OPEN — data model prepared for extension |
| OQ-ACC-003 | Cost center / project accounting Phase 1 | Boss | OPEN — entity field placeholder added |
| OQ-ACC-004 | ภ.พ.30 / ภ.ง.ด.3 / ภ.ง.ด.53 export format | Accounting Owner / Boss | OPEN |
| OQ-ACC-005 | Bank integration: direct or import-only | Boss / Finance Owner | OPEN |
| OQ-ACC-006 | Abbreviated tax invoice (อย่างย่อ) scope | Boss | OPEN |
| OQ-ACC-007 | Opening balances / data migration | Boss | OPEN (REV-08) |
| OQ-ACC-008 | Fiscal year-end close to retained earnings | Boss | OPEN (REV-08) |
| OQ-ACC-009 | Payment allocation across invoices | Boss | OPEN (REV-08) |
| OQ-ACC-010 | Advance payment / deposit VAT treatment | Boss | OPEN (REV-08) |
| OQ-ACC-011 | Petty cash / PDC handling | Boss | OPEN (REV-08) |
| OQ-ACC-012 | Tax document print language: Thai / bilingual / config | Boss / UX | OPEN (UIQ-ACC-003) |
| OQ-ACC-013 | Buddhist Era vs CE on tax documents | Accounting Owner / UX | OPEN (UIQ-ACC-003) |
| OQ-ACC-014 | Cross-border WHT (ภ.ง.ด.54 / ภ.พ.36) Phase 1 scope | Boss / Legal | OPEN |

---

## 17. Assumptions

| ID | Assumption |
|---|---|
| AS-ACC-001 | โมดูลนี้จะใช้ SaaS Foundation ที่มีอยู่แล้ว |
| AS-ACC-002 | Phase แรกเน้น functional completeness ก่อน direct government filing |
| AS-ACC-003 | เอกสารภาษีต้องผ่าน legal/accounting review ก่อน development |
| AS-ACC-004 | API/DB/UI mapping เป็น draft เพื่อให้ Architecture และ Legal review ต่อ |
| AS-ACC-005 | ระบบต้องรองรับ tenant/company/branch scope ทุก transaction — เพิ่ม company_id/branch_id ใน v1.1 |
| AS-ACC-006 | Currency = THB only ใน Phase 1 จนกว่า OQ-ACC-002 จะมีคำตอบ |
| AS-ACC-007 | Posting rules ใน §6-A เป็น draft functional design — ต้องผ่าน Accounting Owner review |
| AS-ACC-008 | Tax invoice print layout จะออกแบบโดย Figma UX UI AI หลัง §6-B ผ่าน legal review |

---

## 18. Clean Room Compliance

| Check | Status |
|---|---|
| ไม่อ้างอิงหน้าจอหรือ workflow เฉพาะของคู่แข่ง | Self-assessed — pending independent review |
| ออกแบบจาก business need และ accounting principle | Self-assessed — pending independent review |
| แยก assumption และ open question | Self-assessed — pending independent review |
| รองรับ SaaS และ multi-tenant | Self-assessed — pending independent review |
| มี traceability เบื้องต้น | Self-assessed — pending independent review |
| ต้องรอ ChatGPT L99 / PMO review ก่อน approved | HOLD |

*(REV-09: Self-approval wording "Pass" replaced with "Self-assessed — pending independent review" per GV-01)*

---

## 19. State Record

| State | Status | Date | Notes |
|---|---|---|---|
| State 1 | Repository Inventory | Prior session | Complete |
| State 2 | Draft Completed | 2026-07-01 | v1.0 |
| State 3 | Claude AI Review | 2026-07-07 | SMEPLUS-STATE03-ACC-CLREV-001 — REVISION REQUIRED |
| State 4 (current) | Revision Drafted | 2026-07-08 | v1.1 FDS-ACC-BATCH-002 — DRAFTED / NOT APPROVED |
| State 5 | ChatGPT L99 Re-Review | Pending | — |
| State 6 | Legal / Accounting Owner Review | Pending | §6-B annex |
| State 7 | PMO Evidence Verification | Pending | — |
| State 8 | Boss Gate Decision | Pending | — |

---

PREPARED ONLY / NOT APPROVED / REQUIRES CHATGPT L99 REVIEW
