> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 14 — INTEGRATION REGISTER

Coupling points recorded as dependencies only. **No research performed on the deferred side.**

| ID | Deferred domain | Coupling observed | Deferred to |
|---|---|---|---|
| INT-01 | AR / AP | Customer invoices and vendor bills are the *same* `account_move` table, distinguished by `move_type`; `payment_state` tracks settlement | AR/AP domain |
| INT-02 | Payments | `account_payment` (LGPL-3) extends the core; reconciliation links payments to items | Payments domain |
| INT-03 | Tax / VAT / WHT | Tax lines are system-generated inside the entry; `account_tax` (28 cols); Thai WHT stack extends move/line | Tax domain |
| INT-04 | Assets | `account_asset` (**OEEL-1, black-box**) posts depreciation entries into the core | Assets domain |
| INT-05 | Inventory valuation | `stock_account` posts valuation entries into the core | Inventory Valuation domain |
| INT-06 | Reporting | `account_reports` (**OEEL-1, black-box**) reads the core; Thai statutory reports build on it | Reporting domain |
| INT-07 | Analytic accounting | `account_analytic_line` (36 cols) coupled to postings — in scope only where directly coupled | Partially in scope |
| INT-08 | Reconciliation UI | `account_accountant` (**OEEL-1, black-box**) provides the reconciliation workbench | Deferred |
| INT-09 | Budget | `account_budget` (**OEEL-1, black-box**) | Deferred |
| INT-10 | Customer layer | `smesplus_account_reports`, `smesplus_tax_period_date`, `cr_effective_date_entries`, `full_summarize_bills` (CLASS-D) | Customer-layer domain |

**Structural note.** Four of the ten couplings are to OEEL-1 black-box modules. The accounting
core is readable, but several things that *write into it* are not.
