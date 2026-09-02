# Next Controlled Action and Owner Matrix

Ordered by dependency — items higher in the list unblock items below them.

| # | Action | Owner | Blocks |
|---|---|---|---|
| 1 | Reissue file access for `งบการเงิน 2567.pdf` (Thai financial-statement source) | Boss | COA-G01 blocker N-04 |
| 2 | Decide N-05 and C-03 (both flagged "ACCEPTED RESIDUAL UNKNOWN / BOSS DECISION REQUIRED") | Boss | COA-G01 closure |
| 3 | Commission ChatGPT independent re-audit of the submitted CORR5 package | Boss / ChatGPT Audit role | COA-G01 closure |
| 4 | Complete PMO Verification and Boss Gate Decision for COA-G01 | PMO / Boss | COA-G01 closure, COA-G02 start |
| 5 | Decide whether `l10n_th_withholding_tax_multi` is part of the intended module baseline (`ACC-WHT-06`) | Boss | WHT full closure |
| 6 | Complete the 10-item `LEGAL_TAX_REVIEW_REQUIRED` register (WHT) and the 5 flagged 50-TWI form fields | Legal/Tax reviewer | WHT and TWI closure, COA-G06 |
| 7 | Decide whether VAT and CIT are in-scope for Accounting Core or explicitly deferred elsewhere | Boss | COA-G06, statutory-completeness claims |
| 8 | Remediate the PND3/PND53 code-quality risks (duplicated `tax_report_pnd.py`, hardcoded WHT-condition column) before treating as SMEsPlus's own design | Team C (once authorized) | COA-G06 |
| 9 | Decide the standard-COA-template option (`B13` DT-03) | Boss | COA-G04S |
| 10 | Commission AR/AP aging and fixed-asset roll-forward research (currently zero research performed) | Team A (research pass) | P0-10, migration-reconciliation sign-off |
| 11 | Extend `B03`-style domain-boundary analysis to Sales, Purchase, Expense, Employee, Manufacturing (Inventory boundary already done) | Team B | Full Financial-Truth-Center integrity claim |
| 12 | Confirm whether Inventory-backbone content inside `ISOLATED_ACCOUNT_CORR5` is intentional joint-tracking or should be relocated | Boss | Account×Inventory interface closure |
| 13 | Schedule Joint Account×Inventory session for landed-cost / return / adjustment posting scenarios | Boss (convene) | Account×Inventory interface closure |
| 14 | Mark the stale root-level `03_Architecture/STATE03_MIGRATION_FACTORY/` copy as archived/superseded | Boss / repo owner | Prevents future stale-citation risk (VC-01) |
| 15 | Targeted content search of `COA_G01_EVIDENCE/` (99 files) and `COA_G01_SOURCE_PORT/` (63 files) for the "389/389" figure and "13 Do-NOT-Merge controls" cited in the governing prompt | Next investigating session | ST-02 closure |
| 16 | Content-read `COA_STANDARD/` (3 files) for the "36 Base Kernel" / "19 active types" claims | Next investigating session | ST-03, COA-G04 preparation |
| 17 | Read full `B09` CO-01–CO-16 against SoD, backup/recovery, and destructive-action controls specifically | Next investigating session | VC-07 closure |
| 18 | Decide whether to formally recreate the missing 18-deliverable Account Reopen package, or treat this package as its replacement | Boss | G-A3 |

**No item on this list authorizes Team C, development, or production.**
