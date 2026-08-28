> DOMAIN_01 — Accounting Core | Team A PART 2 (Sonnet) | Input: committed Part 1 evidence | No SMEsPlus design

# 03 — ACCOUNTING PRINCIPLE REGISTER

Every entry separates: ACCOUNTING PRINCIPLE / BUSINESS REQUIREMENT / ERP COMMON PATTERN /
REFERENCE-SYSTEM BEHAVIOUR / VENDOR-SPECIFIC IMPLEMENTATION / AI INFERENCE / UNKNOWN.
Never conflated, per directive §9.

| ID | Statement | Category | Evidence | Confidence |
|---|---|---|---|---|
| AP-01 | Every transaction is recorded as equal, offsetting debits and credits (Σdebit=Σcredit) | **ACCOUNTING PRINCIPLE** | [Wikipedia — Double-entry bookkeeping](https://en.wikipedia.org/wiki/Double-entry_bookkeeping) | HIGH |
| AP-02 | Assets = Liabilities + Equity | **ACCOUNTING PRINCIPLE** | [Wikipedia — Accounting equation](https://en.wikipedia.org/wiki/Accounting_equation) | HIGH |
| AP-03 | Journals are the book of original entry; the ledger is the authoritative source for financial reports | **ACCOUNTING PRINCIPLE** | [AccountingTools — Books of original entry](https://www.accountingtools.com/articles/what-are-books-of-original-entry.html) | HIGH |
| AP-04 | Posting is the act of transferring/finalizing journal entries into ledger accounts | **ACCOUNTING PRINCIPLE** | [Lumen Learning — Post to the Ledger](https://courses.lumenlearning.com/suny-finaccounting/chapter/journalizing-and-posting-to-the-general-ledger/) | HIGH |
| AP-05 | A correction to a posted fact should be additive (a new linked entry), not destructive (edit/delete) | **ERP COMMON PATTERN** (validated cross-vendor, not yet elevated to a cited accounting standard) | SAP B1 documentation ([sap-business-one-tips.com](https://www.sap-business-one-tips.com/en/reverse-journal-entry/)) | MEDIUM-HIGH |
| AP-06 | Transactions must not post into an already-reported/closed period without an authorized override | **ACCOUNTING PRINCIPLE / internal control** (period cutoff) | Cross-ERP: NetSuite ([Oracle NetSuite](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1451780.html)) | HIGH (principle) |
| AP-07 | Foreign-currency transactions are initially recognised at spot rate; monetary items are remeasured at each reporting date using the functional currency | **REGULATORY REQUIREMENT (IFRS)** | [IFRS — IAS 21](https://www.ifrs.org/issued-standards/list-of-standards/ias-21-the-effects-of-changes-in-foreign-exchange-rates/) | HIGH |
| AP-08 | Financial statements must be prepared, retained, and independently audited by a licensed accountant | **REGULATORY REQUIREMENT (Thailand)** | Accounting Act B.E. 2543 ([Emerhub](https://emerhub.com/thailand/financial-audits-in-thailand/)) | HIGH |
| AP-09 | Accounting records must be retained 5–7 years | **REGULATORY REQUIREMENT (Thailand)** | Revenue Code §87 / CCC ([Emerhub](https://emerhub.com/thailand/financial-audits-in-thailand/)) | HIGH |
| AP-10 | e-Tax invoices/receipts must maintain provable message integrity via a licensed digital signature | **REGULATORY REQUIREMENT (Thailand)**, scoped to e-Tax documents | Electronic Transactions Act ([esignglobal.com](https://www.esignglobal.com/blog/use-digital-signature-e-tax-invoices-thailand-rd)) | HIGH (for e-Tax scope) |
| AP-11 | Tax invoices require genuinely sequential numbering; gaps are an audit concern | **REGULATORY REQUIREMENT (Thailand)**, P4 secondary-source confidence | Revenue Code §86 (secondary source) ([invoicedataextraction.com](https://invoicedataextraction.com/blog/thailand-tax-invoice-requirements)) | MEDIUM (primary text not read) |
| AP-12 | Money must be stored as exact decimal, not binary floating point | **ERP/COMPUTING COMMON PATTERN** — reclassified down from "universal accounting principle" (Part 1 overstated this) | No IFRS clause found mandating storage representation; this is software-correctness norm | MEDIUM (norm, not standard) |
| AP-13 | An audit trail should allow tracing every ledger entry back to its originating transaction | **ACCOUNTING PRINCIPLE** | [Lumen Learning — posting creates traceable audit trail](https://courses.lumenlearning.com/suny-finaccounting/chapter/journalizing-and-posting-to-the-general-ledger/) | HIGH |
| AP-14 | Balance-sheet accounts carry their balance forward at year-end; income-statement accounts reset to zero | **ACCOUNTING PRINCIPLE** | General accounting practice; reference system implements via `include_initial_balance` (P1 SE-18) | HIGH (principle) / not independently triangulated externally this round |

## WHAT IS **NOT** IN THIS REGISTER
Thai statutory tamper-evidence for the *general ledger* (only e-Tax invoices confirmed);
Thai statutory gapless-numbering for *all* journal entries (only tax invoices, and only at P4
confidence); any IFRS/TFRS clause not directly retrieved this session. These remain **G —
Unknown** in `11_RESIDUAL_UNKNOWN_REGISTER.md`, not silently promoted here.
