# ACC-001 UI Handoff Notes Draft v1.1

Document ID: SMEPLUS-ACC001-UIHANDOFF-v1.1
Version: v1.1
Batch: FDS-ACC-BATCH-002
Status: DRAFTED — NOT READY FOR FIGMA HANDOFF
Gate Status: HOLD / REVIEW REQUIRED (UX Gate: HOLD)
Owner: Functional Specification AI
Revised By: Claude AI (/L99.99, FDS-ACC-BATCH-002)
Generated: 2026-07-08 (Asia/Bangkok)

**IMPORTANT: This document is a UI handoff preparation draft only. Do NOT send to Figma UX UI AI until all preconditions in §Handoff Preconditions are met.**

---

## Overall Handoff Readiness

| Item | Status |
|---|---|
| Screen inventory | COMPLETE — 19 screens mapped in v1.1 §10 |
| Field-level definitions | NOT YET COMPLETE — blocked on REV-03 legal review and REV-04 entity finalization |
| Status state machine | DRAFTED — see §Document Status Enumeration below |
| Role × screen access matrix | DRAFTED — see ACC-001 v1.1 §4 |
| Print/PDF layout requirements | NOT YET — blocked on §6-B legal review |
| Bilingual / calendar decisions | BOSS_DECISION_REQUIRED (OQ-ACC-012, OQ-ACC-013) |
| Figma handoff status | BLOCKED — do not proceed |

---

## Document Status Enumeration (all document types)

This enumeration must be implemented consistently across all screens.

| Status | Visible Label | Edit? | Submit? | Approve? | Cancel? | Notes |
|---|---|---|---|---|---|---|
| Draft | ฉบับร่าง | Yes | Yes | No | Yes | Default on create |
| Submitted | รออนุมัติ | No | No | Yes (Approver) | No | Locked pending decision |
| Revision_Requested | ขอแก้ไข | Yes | Yes | No | No | Returned to creator |
| Approved | อนุมัติแล้ว | No | No | No | No | Ready to post |
| Posted | บันทึกแล้ว | No | No | No | No (Reverse only) | GL entry exists |
| Reversed | กลับรายการ | No | No | No | No | Linked to reversal journal |
| Rejected | ปฏิเสธ | Yes | Yes | No | Yes | Can be revised |
| Cancelled | ยกเลิก | No | No | No | No | Number retained; cannot repost |

---

## Screen Notes by Priority

### High Priority — Critical for Tax Compliance

**SCR-ACC-010a — Tax Invoice Form**
- Business objective: Issue full-form tax invoice compliant with Thai Revenue Code
- User roles: Accountant (create/issue), Auditor (view)
- Primary actions: Issue, Cancel, Print/Export
- Mandatory fields: All fields in §6-B TH-02 — must validate before issue button is active
- Validation: `ERR-ACC-TI-INCOMPLETE` blocks issue if any mandatory field is empty
- Status behavior: Draft → Issued → Cancelled (number retained after cancellation)
- Print/PDF: LEGAL_TAX_REVIEW_REQUIRED before layout can be designed
- Open questions: Buddhist Era date display (OQ-ACC-013); bilingual label (OQ-ACC-012)

**SCR-ACC-016 — Credit Note Form**
- Business objective: Issue credit note with VAT adjustment and original TI linkage
- Primary actions: Select original TI, enter reason, issue, print
- Mandatory fields: original_tax_invoice_id (lookup), original_tax_invoice_no (auto-filled), reason_code (dropdown), reason_text (free text), amount, VAT adjustment
- Validation: Cannot issue without original TI selection; reason_code required
- Status behavior: Draft → Issued → Cancelled
- VAT impact: Must show VAT adjustment amount preview before issue
- Print/PDF: LEGAL_TAX_REVIEW_REQUIRED

**SCR-ACC-017 — Debit Note Form**
- Same structure as SCR-ACC-016 with debit-side amounts
- Print/PDF: LEGAL_TAX_REVIEW_REQUIRED

**SCR-ACC-009 — WHT Certificate**
- Business objective: Issue WHT certificate (50 ทวิ) upon vendor payment
- Fields per §6-B TH-04: payer/payee details, income type, payment date, gross amount, WHT rate (from WHTType), WHT amount, certificate number (from DocumentSequence)
- Validation: WHTType must be selected; certificate blocked until payment voucher is posted
- Print/PDF: LEGAL_TAX_REVIEW_REQUIRED

**SCR-ACC-018 — WHT Filing Reports (ภ.ง.ด.3 / ภ.ง.ด.53)**
- Business objective: Monthly WHT report for Revenue Department filing
- Filters: report_type (PND3 / PND53), month, year
- Display: Payee list with income type, gross amount, WHT amount
- Export: Format pending OQ-ACC-004 Boss decision
- Separate screen from SCR-ACC-009 (certificate view)

---

### Medium Priority — Core Workflow Screens

**SCR-ACC-005 — Journal Entry Form**
- Status state machine: Draft → Submitted → Approved/Rejected/Revision_Requested → Posted → Reversed
- Balance indicator: Real-time Debit / Credit / Difference display; Submit button disabled when Difference ≠ 0
- Source document panel: ref_type / ref_id lookup (Invoice, Bill, Receipt, Voucher)
- Posted state: All fields read-only; only "Reverse" action available
- Reversal: Validates target period is open before creating reversal

**SCR-ACC-002a-d — Accounting Setup Sub-screens**
- 002a: Company info, tax ID, branch code
- 002b: TaxCode list + add (code, rate, type, rounding method)
- 002c: WHTType list + add (income type, rate, report type)
- 002d: DocumentSequence list + edit (prefix, reset policy)
- Access: Accounting Admin only

**SCR-ACC-011b — Bank Statement Import**
- File upload (CSV / bank-specific format — format TBD per OQ-ACC-005)
- Preview table before confirm import
- Auto-match trigger button
- Unmatched items count badge

**SCR-ACC-011c — Bank Reconciliation**
- Split pane: Statement lines (left) vs. Journal lines (right)
- Color coding: Matched (green), Unmatched (yellow/red)
- Actions: Auto-match, Manual match (drag or select-select), Unmatch
- Unreconciled summary at bottom

---

### Lower Priority — Report / Shared Screens

**SCR-ACC-013a-d — Financial Reports**
- Trial Balance, GL: Filter by period / date range; drill-down to journal
- P&L: Filter by fiscal year / period range; compare periods (pending Boss decision on comparative)
- Balance Sheet: As-of-date; account group hierarchy

**SCR-ACC-014 — Evidence Panel**
- Reuse SaaS Foundation component — do not redesign
- Display: File list, uploaded_by, uploaded_at, download link

**SCR-ACC-015 — Audit Log Viewer**
- Reuse SaaS Foundation component
- Display: action, actor, timestamp, before/after values

---

## Print / PDF Layout Requirements (BLOCKED)

All print layouts for the following documents require §6-B Thai Tax Annex legal review before Figma layout design:
- Tax invoice (เต็มรูป)
- Receipt (ใบเสร็จรับเงิน)
- Credit note (ใบลดหนี้)
- Debit note (ใบเพิ่มหนี้)
- WHT certificate (50 ทวิ)
- Payment voucher (ใบสำคัญจ่าย)

Layout decisions pending Boss decisions: bilingual (Thai/English), Buddhist Era display, print-from-browser vs PDF download (UIQ-ACC-002).

---

## Open UI Questions

| ID | Question | Owner | Blocking |
|---|---|---|---|
| UIQ-ACC-001 | Journal entry grid: line-entry style and Thai account name lookup? | Figma UX UI AI (after handoff) | SCR-ACC-005 detail |
| UIQ-ACC-002 | Document print: preview in-app vs direct PDF download? | Boss / UX | Print layout design |
| UIQ-ACC-003 | Thai Buddhist calendar year on tax documents? | Accounting Owner / UX | Tax invoice, WHT cert |
| UIQ-ACC-004 | Mobile scope for Approver role in Phase 1? | Boss | Approval screens |
| UIQ-ACC-005 | Bank statement import file format (CSV / BAY / KBank / SCB)? | Finance Owner | SCR-ACC-011b |
| UIQ-ACC-006 | Abbreviation tax invoice (อย่างย่อ) — if Boss approves, separate screen or mode? | Boss / UX | OQ-ACC-006 |

---

## Handoff Preconditions (NOT YET MET)

- [ ] REV-03 Thai Tax Annex §6-B reviewed and confirmed by legal/accounting reviewer
- [ ] REV-01 Posting Rules §6-A confirmed by Accounting Owner
- [ ] REV-04 Entities finalized and confirmed by DB Design AI
- [ ] Document status enumeration confirmed by ChatGPT L99 / PMO
- [ ] Role × screen matrix confirmed
- [ ] Boss decisions on: OQ-ACC-012 (bilingual), OQ-ACC-013 (calendar), OQ-ACC-002 (UIQ-002 print)
- [ ] ChatGPT L99 + PMO review of ACC-001 v1.1 completed
- [ ] Boss gate decision received

**None of the above preconditions are met. UI/Figma handoff must not proceed until all are confirmed.**

PREPARED ONLY / NOT APPROVED / DO NOT SEND TO FIGMA
