# ACC-001 Traceability Matrix

Version: v1.0
Status: Partial / Review Required
Owner: Functional Specification AI
Reviewer: PMO AI / Claude AI
Project: SMEsPlus Enterprise Suite
Control Level: L99
Created: 2026-07-07T01:31:49+07:00
Gate Impact: Traceability Gate / FDS Gate / Build Gate

---

## Purpose

This file creates a real repository traceability artifact for ACC-001 Accounting Thailand Functional Design Specification.

This file does not approve build.

---

## Traceability Rule

No ACC-001 requirement is marked MATCHED in this version because reviewer approval is incomplete.

---

## Matrix

| FR ID | Function | Main Mapping Evidence | Evidence File | Reviewer | Gate Result | Status | Next Action |
|---|---|---|---|---|---|---|---|
| FR-ACC-001 | Accounting Setup | Setup / period / document numbering | ACC-001 FDS | PMO AI / Accounting Owner | REVIEW REQUIRED | PARTIAL | Confirm setup scope |
| FR-ACC-002 | Chart of Accounts | Account model / COA screen / account API | ACC-001 FDS | Accounting Owner / DB Owner | REVIEW REQUIRED | PARTIAL | Review COA design |
| FR-ACC-003 | Journal Entry | Journal entry rule and workflow | ACC-001 FDS | PMO AI / Accounting Owner | REVIEW REQUIRED | PARTIAL | Confirm journal validation |
| FR-ACC-004 | Journal Approval | Reuse Approval Foundation | ACC-001 FDS / SaaS Foundation | PMO AI / Enterprise Architect AI | REVIEW REQUIRED | PARTIAL | Confirm approval reuse |
| FR-ACC-005 | Journal Posting | Posting control | ACC-001 FDS | Accounting Owner / QA-UAT AI | REVIEW REQUIRED | PARTIAL | Review posting rule |
| FR-ACC-006 | Reverse Journal | Reverse / adjustment control | ACC-001 FDS | Accounting Owner / QA-UAT AI | REVIEW REQUIRED | PARTIAL | Define reversal constraints |
| FR-ACC-007 | Accounts Receivable | AR invoice and receipt flow | ACC-001 FDS | Accounting Owner / API Owner | REVIEW REQUIRED | PARTIAL | Review AR flow |
| FR-ACC-008 | Accounts Payable | AP bill and payment voucher flow | ACC-001 FDS | Accounting Owner / API Owner | REVIEW REQUIRED | PARTIAL | Review AP flow |
| FR-ACC-009 | VAT Management | VAT draft requirement | ACC-001 FDS / Gap Register | Accounting Compliance Reviewer | HOLD | HOLD | Compliance review required |
| FR-ACC-010 | WHT Management | WHT draft requirement | ACC-001 FDS / Gap Register | Accounting Compliance Reviewer | HOLD | HOLD | Compliance review required |
| FR-ACC-011 | Tax Invoice | Tax document draft requirement | ACC-001 FDS / Gap Register | Accounting Compliance Reviewer | HOLD | HOLD | Confirm document scope |
| FR-ACC-012 | Credit / Debit Note | Draft only | ACC-001 FDS / Gap Register | Accounting Compliance Reviewer / API Owner | HOLD | GAP | Define workflow, API and AC |
| FR-ACC-013 | Bank & Cash | Bank and cash draft flow | ACC-001 FDS / Gap Register | Boss / Finance Owner | REVIEW REQUIRED | PARTIAL | Confirm bank approach |
| FR-ACC-014 | Period Closing | Period closing workflow | ACC-001 FDS | Accounting Owner / QA-UAT AI | REVIEW REQUIRED | PARTIAL | Review pre-close checklist |
| FR-ACC-015 | Financial Reports | Report draft list | ACC-001 FDS / Gap Register | Accounting Owner / QA-UAT AI | REVIEW REQUIRED | PARTIAL | Define reports and AC |
| FR-ACC-016 | Evidence Attachment | Reuse Evidence Foundation | README / Bootstrap / ACC-001 FDS | PMO AI / Liza | REVIEW REQUIRED | PARTIAL | Confirm implementation mapping |
| FR-ACC-017 | Audit Trail | Reuse Audit Foundation | Bootstrap / ACC-001 FDS | PMO AI / Liza | REVIEW REQUIRED | PARTIAL | Confirm audit event model |
| FR-ACC-018 | Export Reports | Draft only | ACC-001 FDS / Gap Register | Accounting Owner / QA-UAT AI | HOLD | GAP | Define export format and tests |
| FR-ACC-019 | API Integration | Draft only | ACC-001 FDS / Evidence Register | Enterprise Architect AI / API Owner | HOLD | GAP | Produce reviewed API contract |
| FR-ACC-020 | Multi-Company / Branch Accounting | SaaS scope reuse | SaaS Foundation / ACC-001 FDS | Enterprise Architect AI / PMO AI | REVIEW REQUIRED | PARTIAL | Validate tenant scope |

---

## Gate Summary

| Gate | Status | Reason |
|---|---|---|
| FDS Gate | REVIEW REQUIRED | Draft exists but reviewer approvals are incomplete |
| Traceability Gate | HOLD | No item is fully MATCHED yet |
| API Gate | HOLD | API mapping is draft |
| DB Gate | HOLD | Data entities are draft |
| UX Gate | HOLD | No Figma evidence linked |
| QA / UAT Gate | HOLD | Formal test cases are not yet reviewed |
| Build Gate | HOLD | Upstream gates are not passed |

---

## End
