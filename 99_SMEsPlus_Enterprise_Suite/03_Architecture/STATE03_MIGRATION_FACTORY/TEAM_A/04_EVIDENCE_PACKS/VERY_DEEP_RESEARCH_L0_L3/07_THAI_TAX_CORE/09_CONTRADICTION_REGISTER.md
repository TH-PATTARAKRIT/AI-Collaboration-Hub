# Contradiction Register (tax-relevant)

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Source/dump evidence only — not runtime proof, not statutory proof. No V-level, no Complete, no coverage percentage. Assembled mechanically from the unit files named in each row; Restricted Technical Evidence (this file) is separate from the Neutral Clean-Room Knowledge Pack.


| Boundary | Claim-ID | Function-ID | Class | Condition | Flags | Statement | Pointer |
|---|---|---|---|---|---|---|---|
| TXA2 | VDR-TXA2-C061 | PCO-F04 | FACT | sale_stock installed | CONTRA | sale_stock computes delivery_date on draft invoices as the maximum effective_date of the linked sale orders; supersedes the statement that delivery_date has no Community source (VDR-U11-C191/N-U11-095, already flagged by C01 finding F03). | sale_stock/models/account_move.py:117 |
| U13 | VDR-U13-C217 | FUNCTION MAPPING REQUIRED | OBSERVATION | DB company chart th loaded | CONTRA | DB holds 179 company-prefixed template identifiers under module account (147 accounts, 18 taxes, 7 journals, 5 tax groups, 2 reconcile models); CONTRA B01 section 2.1 which cites 181 for this class (difference of 2 not explained here). | account/models/chart_template.py:1230 |
| U13 | VDR-U13-C368 | FUNCTION MAPPING REQUIRED | FACT | template th | CONTRA | Sales-side withholding tax (taxes withheld by customers) is a negative-percent tax forced tax_excluded posting to account 114300; DB shows 114300 is of type asset_current (not receivable), CONTRA the prior candidate map MODULE_l10n_th section 6 which calls it receivable-type. | l10n_th/data/template/account.tax-th.csv:62 |
| U25 | VDR-U25-C286 | FUNCTION MAPPING REQUIRED | FACT | accounting installed | CONTRA | Accounting managers also have full CRUD on res.currency and res.currency.rate (lines 6-7); U01 CAP-U01-06 dimension 7 states 'Everyone reads; system writes', which is correct for base alone but incomplete once accounting is installed (refinement of U01 C279, consistent with U13 C464). | account/security/ir.model.access.csv:6 |
| U11 | VDR-U11-C082 | FN-14 | FACT | always | CONTRA | Constraint requires invoice_date only when auto_post != 'no' AND is_purchase_document() (in_invoice, in_refund; receipts excluded because include_receipts defaults False). The prior FN-14 states a generic date requirement for auto-post; narrowed here. | account/models/account_move.py:2842 |

**Rows:** 5 (tax-relevant claims by keyword filter over units TXA1, TXA2, TXC, U13, U23, U24, U25, U11, U12 and correction packets) · generated 2026-10-02
