# A2 — SYSTEM KNOWLEDGE MAP

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-29-MIG-A-D01-ACCOUNTING-CONT-001 |
| Continues | SMEPLUS-26-08-28-MIG-A-EXPERT-DR-001 (evidence b2e5a2a / closure c441443) |
| Phase | A2 — System Knowledge Map |
| Baseline | 1,504 modules (research inventory only, NOT approved product scope) |
| STEP linkage | **TBD / BASELINE LINKAGE REQUIRED** — STEP0303R5 is PRIOR GOVERNANCE/PLANNING EVIDENCE ONLY and does not bind this workstream |

## 1. Accounting-related module map
Derived from `MODULE_MASTER_REGISTER_FULL.csv` (1,504 rows, A1).

| Selector | Modules |
|---|---:|
| Name matches `^account(_|$)` / `^accountant(_|$)` **or** category starts `Accounting` | **511** |
| — in `01_ACCOUNT` partition | 62 |
| — in `02_OTHER` partition | 442 |
| — in `addons_extra` (customer layer) | 7 |
| License split | LGPL-3 256 · OEEL-1 248 · OPL-1 5 · AGPL-3 1 · UNDECLARED 1 |

**Accounting Core nucleus (this domain):**
| Module | Area | License | Read status |
|---|---|---|---|
| `account` | 01_ACCOUNT | LGPL-3 | SOURCE READ |
| `analytic` | 02_OTHER | LGPL-3 | SOURCE READ (only where directly coupled) |
| `account_debit_note`, `account_edi`, `account_payment`, `account_tax_python` | 01_ACCOUNT | LGPL-3 | dependency context |
| `account_accountant`, `accountant`, `account_reports`, `account_asset`, `account_budget` | 01_ACCOUNT | **OEEL-1** | **BLACK-BOX — metadata only** |

`account_lock_date` and `account_fiscal_year` do **not exist** as modules — lock behaviour is
carried on `res.company` fields inside `account` (see 06_BUSINESS_RULE_REGISTER).

## 2. Source partitions involved
S-01 `01 ACCOUNT` (62 modules) · S-02 `02 OTHER` (1,371) · S-03 `addons_extra` (69) ·
S-04 `ks_*` (2, separately classified) · S-05 dump `iTEST02_2026-06-14` (Research Reference
Snapshot only). Source path is READ ONLY; nothing was written, moved or modified.

## 3. Dependency map (Accounting Core)
```
account  ──> base, analytic, portal, digest, mail, product, uom, web, base_setup, html_editor
   │
   ├─ extended by (readable):  account_debit_note, account_edi, account_payment,
   │                           account_tax_python, account_qr_code_emv
   ├─ extended by (BLACK-BOX): account_accountant, account_reports, account_asset,
   │                           account_budget, accountant
   └─ extended by (customer):  Thai WHT stack, smesplus_account_reports, cr_effective_date_entries,
                               full_summarize_bills, bi_print_journal_entries (CLASS-D)
```
Downstream consumers deferred to other domains: AR/AP, Payments, Tax/VAT/WHT, Assets,
Inventory Valuation, Reporting.

## 4. Dump object anchors (Accounting Core)
| Table | Cols | Constraints | Indexes |
|---|---:|---:|---:|
| `account_move` | 96 | 37 | 37 |
| `account_move_line` | 76 | 31 | 27 |
| `account_journal` | 35 | 16 | 3 |
| `account_account` | 20 | 7 | 4 |
| `account_analytic_line` | 36 | 24 | 14 |
| `account_partial_reconcile` | 17 | 10 | 4 |
| `account_full_reconcile` | 5 | 3 | 0 |
| `account_lock_exception` | 13 | 5 | 1 |
| `account_analytic_account` | 12 | 7 | 4 |
| `res_company` | 259 | 89 | 5 |

## 5. Custom / accounting-related customer modules
`smesplus_account_reports`, `smesplus_tax_period_date`, `cr_effective_date_entries`,
`full_summarize_bills` (CLASS-D), `bi_print_journal_entries` (CLASS-D),
`dev_print_cheque` (CLASS-D), Thai WHT stack (deferred to Tax domain).

## 6. Known gaps
- G-1 No PostgreSQL toolchain available this session → `pg_restore -l` not executed (see
  `DATABASE_EXCEPTION_REGISTER.md`). Dump structure taken from approved prior evidence.
- G-2 Enterprise accounting behaviour (`account_accountant`, `account_reports`) is black-box;
  reconciliation UI and report engine behaviour cannot be sourced.
- G-3 Row-level data profile unavailable — no restore; the snapshot is known from prior
  evidence to be a configuration/UAT database (6 journal entries, 23 journal lines).
- G-4 `analytic` inspected only where directly coupled, per domain scope.

## 7. Clean-room risks
| ID | Risk | Control applied |
|---|---|---|
| CR-1 | Reading LGPL-3 source could leak implementation into target design | A7 neutralization applied to every critical finding; no target design produced |
| CR-2 | Proprietary OEEL-1 accounting modules in the dependency path | Metadata only; **no OEEL-1/OPL-1 source body read at any point** |
| CR-3 | Vendor-specific field/table names becoming target schema | Recorded as vendor fact, neutralized to generic concept; no schema designed |
| CR-4 | CLASS-D undeclared-license customer modules | Remain HOLD/QUARANTINE; not read for design content |
