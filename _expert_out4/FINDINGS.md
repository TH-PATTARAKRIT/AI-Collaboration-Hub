# P01 SERIES-18 DIRECT VERIFICATION — FROZEN FINDINGS BRIEF (for adversarial challenge)

## Evidence base
- Archive: `~/OCC_BACKUP/idemo18_uat_pre_scgl_occ_website_20260830_085432.dump`
  (custom format 1.16, created 2026-08-30 08:52:24 +07, dbname `idemo18_uat`,
   dumped from PostgreSQL 17.9, dumped by pg_dump 17.9)
- Restore tool: `/opt/homebrew/opt/postgresql@18/bin/pg_restore` 18.6 (16.15 also present)
- Method: `pg_restore -t <table> --data-only -f <file>` then parse the `COPY public.<t> (cols) FROM stdin;` block.
- TOC enumerated: 23,232 entries; 1,122 TABLE definitions; 1,122 TABLE DATA entries.

## S18-01 Deployment identity
- `database.uuid = 551ab874-9acb-11f1-b150-6ec7a480be3d`  (NOT among the five uuids in the P04 census)
- `database.create_date = 2026-08-18 06:09:12`; `web.base.url = https://occ.smeplus.cloud`
- ir_module_module: 1,369 rows; 361 installed, 1,005 uninstalled, 3 uninstallable.
- All 361 installed carry `latest_version` beginning `18.0`. base 18.0.1.3, account 18.0.1.3,
  stock 18.0.1.1, purchase 18.0.1.2, stock_account 18.0.1.1, purchase_stock 18.0.1.2,
  purchase_request 18.0.1.10.0, l10n_th 18.0.2.0.
- res_company: 4 rows (ids 1,2,3,4), all THB (currency 133), no parent.
- account_move: 15,522 (posted 13,773 / draft 1,746 / cancel 3). By company: 1 -> 9,733; 2 -> 5,789; **companies 3 and 4 have ZERO**.
- move_type: entry 10,028; out_invoice 3,559; in_invoice 1,904; out_refund 30; in_refund 1.
- stock_valuation_layer: 47,801. By company: 1 -> 25,978; 2 -> 21,823; 3 and 4 zero.

## S18-02 Valuation policy — PROVED, both storage locations read
- v18 stores company-dependent values in TWO places: the per-record jsonb column and `ir_default`.
  ORM resolution: `fields.py:785 get_company_dependent_fallback` -> `ir.default._get_model_defaults`
  (`base/models/ir_default.py:154-182`, `ORDER BY d.user_id, d.company_id, d.id`, first row wins;
  NULLs sort last in Postgres ASC so a company-specific row outranks a global one).
- `product_category.property_valuation` jsonb: **NULL on 126 of 126 categories** (no override anywhere).
- `ir_default` for `product.category.property_valuation`: **one row, company_id = NULL, value `"manual_periodic"`**.
- `product.template.valuation` / `product.product.valuation` are `related="categ_id.property_valuation", readonly=True`
  (`R1:stock_account/models/product.py:17` and `:147`) — no product-level override exists in v18.
- => **Every product in all four companies resolves to `manual_periodic` (Manual/periodic). 126/126, 4/4.**
- v18 selection labels (`R1:stock_account/models/product.py:915-917`): `('manual_periodic','Manual'), ('real_time','Automated')`.
  v19 relabels `real_time` to `Perpetual (at invoicing)` — different generation, different semantics.
- `property_cost_method`: global ir_default `"standard"`; jsonb sets `average` on 18 categories for company 1 only.

## S18-03 Zero-link classification
- `stock_valuation_layer.account_move_id` non-null: **0 of 47,801**. Same for `account_move_line_id`.
- Positive controls in the same parse: `stock_move_id` non-null 44,935; `company_id` 47,801; `product_id` 47,801.
- Synthetic injection control: setting one row's `account_move_id` moved the count 0 -> 1. The parser can register a non-null.
- Source mechanism, same generation: `R1:stock_account/models/stock_valuation_layer.py:74-95` `_validate_accounting_entries`
  `if not svl.with_company(svl.company_id).product_id.valuation == 'real_time': continue`.
  Under periodic no SVL enters `svl_move_list`, `_account_entry_move` is never called, no account.move is created.
- **CLASSIFICATION: EXPECTED UNDER PERIODIC POLICY — VERIFIED.**

## S18-04 Sub-population decomposition (the "47,801" is not one population)
- 45,978 layers (96.2%) carry v14-migration descriptions (`v14 2026: ...`, `Opening rebalance 2026-01-01`).
- 11 layers are `Migration correction: align layers to on-hand x cost (2026-08-26)` and have NO stock move.
- **1,812 layers are native v18 runtime output** (created 2026-08-25..2026-08-29, all with a stock move, 946 non-zero value).
- **DISCRIMINATING SET: of those 1,812 native layers, 0 carry an account_move_id.**
  So the zero is not an artefact of migration: it holds in the natively-created sub-population too.
- 2,866 layers have no stock move at all; 1,205 have value exactly 0.00 (skipped even under real_time by
  `if svl.currency_id.is_zero(svl.value): continue`).

## S18-05 GRNI clearing account — CONFIGURED, NOT EXECUTED
- `property_stock_account_input_categ_id` set in the jsonb on **15 of 126 categories, for all four companies**
  (values 1->176, 2->62, 3->100, 4->138).
- Those accounts are `210300 "Uninvoiced Receipts"`, `liability_current`, `reconcile = true`, one per company.
- `ir_default` at company level: company 1 -> 176; companies 2 and 3 -> **explicitly `false`**; company 4 -> **no row**.
  So the 111 non-configured categories resolve to no account in companies 2, 3, 4.
- Stock journals: `ir_default product.category.property_stock_journal` = 16 (co2), 24 (co3), 32 (co4), 40 (co1),
  all `STJ / "Inventory Valuation" / type general`. jsonb NULL on 126/126 — the journal comes only from the company default.
- **EXECUTION TEST on account_move_line (40,353 rows):**
  accounts 176 / 62 / 100 / 138 -> **0 journal items each**. Journals 16 / 24 / 32 / 40 -> **0 journal items each**.
  Positive control: 144 distinct accounts do appear; top accounts 186 (4,049), 211 (3,522), 169 (2,940);
  top journals 45 (8,226), 33 (7,707), 9 (4,504).
- Account 169 = `130000 Inventory` carries 2,940 items — **all in journal 45 `MIG26 "COA Migration 2026"`**,
  all `entry`, all posted, dates 2026-01-03..2026-08-25. Inventory reaches the GL only through migrated entries.

## S18-06 Bill-line account override is v19-only
- v19 `R3:stock_account/models/account_move_line.py:13-24` `_compute_account_id` sets the bill line to
  `accounts['stock_valuation']` when `product_id.valuation == 'real_time'`.
- **v18 `stock_account/models/` contains no `account_move_line.py` at all** (directory listed: 15 files, none named that).
- Deployed reality: 3,375 vendor-bill product lines; top accounts 186 (`510000 Cost of Revenue`, co1) 1,062 and
  72 (`510000`, co2) 966. No line posts to a valuation or clearing account.
- `anglo_saxon_accounting`: company 1 = TRUE, companies 2, 3, 4 = FALSE. v18's anglo-saxon eligibility
  (`R1:stock_account/models/account_move.py:278`) is `is_storable and valuation == 'real_time'` — inert under periodic.

## S18-07 Three-way match / received-not-invoiced exposure
- purchase_order 13,887 (purchase 13,735 / done 142 / draft 10); companies 1 and 2 only.
  invoice_status: no 12,307; to invoice 1,548; invoiced 32.
- purchase_order_line 21,102; qty_received > 0 on 3,335; qty_invoiced > 0 on 2,575.
- Excluding cancelled/draft orders: **1,580 lines received-not-invoiced, gross pre-tax ฿30,080,689.78**
  (co1 ฿15,258,362.01 / co2 ฿14,822,327.77); 183 lines invoiced-not-received, ฿1,734,752.87.
- stock_move: 51,081 rows; 3,158 linked to a purchase line, 3,124 done.
  **1,403 done purchase-linked moves carry valuation layers totalling ฿22,953,527.29 — 0 of them post a journal entry.**
- No accrual entries exist: 0 of 15,522 moves carry 'accru' in `ref`
  (positive control: 15,434 of 15,522 have a non-empty ref).

## S18-08 A candidate cutoff finding that the discriminating test REFUTED
- 1,667 of 1,879 posted vendor bills have `date` != `invoice_date`; median +13 days, max +30, **never negative**.
- Discriminating test: **all 1,879 are in the same month**, and 1,747 of 1,879 carry an accounting date equal to
  the LAST DAY of the month (124 more on day 25).
- => month-end posting convention, NOT a period-cutoff violation. **Candidate finding withdrawn before publication.**

## S18-09 Period locks
- All four companies: `fiscalyear_lock_date`, `tax_lock_date`, `sale_lock_date`, `purchase_lock_date`,
  `hard_lock_date` all NULL. `po_lock = 'edit'` on all four.
- P01's lock-date findings are therefore NOT REACHABLE in this deployment: no lock is configured.

## S18-10 purchase_request — INSTALLED, CONFIGURED, REACHABLE, EXERCISED
- 1,043 requests (approved 866, to_approve 96, draft 74, rejected 7); 3,398 lines;
  1,504 lines linked to a purchase order (`purchase_state` purchase 1,462 / done 42).
- `stock_move.created_purchase_request_line_id` exists. `scgl_multi_approve_purchase_request_event` table present.

## S18-11 Second population-selection defect (source side)
- 16 installed custom modules. Full-volume, pattern-scoped `find -type d -name <module>` + manifest version compare:
  **6 of 16 have a version-matching source copy; 10 do not** (7 have zero copies by name anywhere; 3 exist only at other versions).
- `purchase_request` deployed at 18.0.1.10.0: 16 copies on the volume, versions 19.0.2.4 x4, 19.0.1.1, 19.0.1.0 x3,
  19.0.1.0.0, **18.0.1.8 x4**, 14.0.1.3.8 x2, 1.0. **No copy at 18.0.1.10.0.**
- **None of the 6 version-matching copies is inside the declared path set R4 (`.../smeplus-custom/addons`).**
  5 are at `ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/` (the parent directory, not the `addons` subdirectory);
  1 is under `CLAUDE AI/SMEsPlus/SMEsPlus18/02_base_Extramodule/`.
- `scgl_account_coa_control` exists only under `97_OCC_PROJECT`, a root P01 declared CLASS C — and this
  deployment IS the OCC deployment (`web.base.url = https://occ.smeplus.cloud`).

## S18-12 A deployed company-scope guard that executes but cannot refuse
- `scgl_product_category_company` 18.0.1.5.0 is installed AND has a version-matching source copy.
- It adds `PurchaseOrder.button_confirm` -> `_scgl_validate_product_company_scope` and an `@api.constrains`
  on purchase order lines: the product's category must be allowed for the order's company.
- Deployed configuration: `scgl_allow_purchase = True` on **126 of 126** categories;
  `scgl_product_category_company_rel` holds 32 rows covering only **16 of 126** categories
  (3 of the 15 GRNI-configured ones). The module documents "Empty Companies means All Companies".
- => the guard executes on every PO confirmation and **permits everything for 110 of 126 categories**.
  Same shape as P01's v19 "guard executes but is vacuous" finding; here the cause is configuration, not code.
- This module does NOT touch `property_valuation` or any `property_stock_*` field — checked explicitly,
  because a category customisation is the one thing that could have falsified S18-02.

## S18-13 A false zero caught inside this run
- Reading `scgl_product_category_company_rel` with assumed column names `product_category_id` / `res_company_id`
  produced a clean `Counter()` — zero. The real columns are `category_id` / `company_id`; there are 32 rows.
  Caught only because the row count (32) was printed beside the aggregate. A well-formed zero is not self-authenticating.

## Bounded absences in this deployment (population = the 1,122 TABLE definitions in the archive TOC)
- `ir_property`: **no table definition at all** (series 17+ removed it).
- `stock_landed_cost*`: **no table definitions** — landed costs not installed. P01's landed-cost work is
  NOT REACHABLE in this deployment.
