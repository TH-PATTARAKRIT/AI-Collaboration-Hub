# ACC-001 Revision Scope Proposal

Document ID: SMEPLUS-STATE03-ACC-REVSCOPE-001
Version: v1.0
Status: DRAFTED (proposal only — execution requires Boss authorization)
Gate Status: HOLD / REVIEW REQUIRED
Owner: Claude AI (SMEsPlus Expert FDS Designer skill, /L99.99)
Approver: Boss (scope authorization) after ChatGPT L99 / PMO review
Source: `ACC-001_CLAUDE_STATE3_REVIEW_COMMENTS.md` (SMEPLUS-STATE03-ACC-CLREV-001)
Generated: 2026-07-07 (Asia/Bangkok)

---

## Proposed Revision Vehicle

- Revise `ACC-001 ... Package.md` from v1.0 to v1.1 as a single-document revision with IDs preserved.
- Batch ID: FDS-ACC-BATCH-002.
- Split-out drafts ACC-002 to ACC-005 v0.1 are not revised in this batch. They should inherit ACC-001 v1.1 in a subsequent sync step to avoid double-maintenance during review.

## Revision Work Items (priority order)

| Rev ID | Scope | Source Findings | Est. Effort | Blocking Dependency |
|---|---|---|---|---|
| REV-01 | Posting Rules section. Add journal templates for AR invoice, receipt, vendor bill, payment with WHT, credit/debit note, reversal; each with debit/credit lines, tax lines, and source-document linkage. | Posting rules absent | High | None |
| REV-02 | Complete section 12 traceability for 7 unmapped FRs and fix FR-ACC-001 mis-mapping. Author missing BRs for FR-ACC-011/012/013/015/018/019/020. | Traceability findings | High | None |
| REV-03 | Thai tax detail annex. Add tax point rules, full tax invoice mandatory fields, credit/debit note reference rules, WHT certificate rules, tax report definitions, satang rounding, numbering reset/cancellation policy, branch code convention, and TaxCode/WHT configuration FR. All rows must be tagged LEGAL_TAX_REVIEW_REQUIRED. | Thai tax findings | High | Legal reviewer must be nominated |
| REV-04 | Data model extension. Add CreditNote, DebitNote, BankStatement, StatementLine, ReconciliationMatch, TaxCode, WHTType, DocumentSequence, FiscalYear. Add source reference and company/branch scope columns to accounting entities. | API/DB findings | Medium | REV-01 informs entity fields |
| REV-05 | API extension. Add setup, tax-invoice issue, credit/debit note, statement import/reconcile, P&L, balance sheet, export, journal reject/revise endpoints. | API coverage findings | Medium | REV-04 |
| REV-06 | UI mapping fix. Split SCR-ACC-010; add credit/debit note, bank reconciliation, WHT filing report, and setup sub-screens. | UI findings | Low | REV-05 |
| REV-07 | Acceptance criteria expansion. Add at least one AC per FR plus tax-correctness ACs and negative-path ACs. | AC gap findings | Medium | REV-03 |
| REV-08 | New-FR decisions. Opening balances, fiscal year-end close, bank reconciliation as explicit FR detail, payment allocation and AR/AP aging, advance/deposit, petty cash, PDC, recurring journals. Add only per Boss decision. | RC-01 to RC-07 | Medium | Boss decision required first |
| REV-09 | Governance wording. Replace self-assessment approval language with pending independent review language. Remove approval decision wording from expected AI output. Fix header path metadata. | Governance findings | Low | None |
| REV-10 | Supporting artifact sync. Update Gap Analysis, Evidence Register, and Traceability Matrix after revision. | Register maintenance | Low | After REV-01 to REV-07 |

## Explicitly Out of Revision Scope

- Answering OQ-ACC-001 to OQ-ACC-005.
- Central matrix v0.2 reconciliation.
- Duplicate folder cleanup and nested matrix folder cleanup.
- ACC-002 to ACC-005 content revision.
- Any Build, Coding, Jira, UI execution, or downstream gate work.

## Proposed Sequence

1. Boss decides REV-08 scope items and OQ-ACC-001/002/003 at minimum.
2. Claude executes FDS-ACC-BATCH-002 for REV-01 to REV-07, REV-09, and REV-10.
3. ChatGPT L99 re-review, then Functional Specification AI / BA / SA review, legal/accounting review of REV-03 annex, PMO evidence verification, and Boss gate decision.

## Status

Proposal only. No revision has been executed. Batch FDS-ACC-BATCH-002 starts only on explicit Boss authorization.

PREPARED ONLY / NOT APPROVED / REQUIRES CHATGPT L99 REVIEW
