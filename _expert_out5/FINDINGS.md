# P01 SERIES-16 SAME-GENERATION VERIFICATION — FROZEN FINDINGS BRIEF

## Evidence base
- Deployment: `~/Downloads/iSMEs_2026-07-11_05-03-27.dump` (CUSTOM 1.14, created 2026-07-11 05:03:27 +07,
  dbname `iSMEs`, from PostgreSQL 15.7). Extract: `pg_restore -t <t> --data-only -f <file>` (18.6 binary), parse COPY block.
- `database.uuid = 45a8e08e-5dcd-11ee-90f5-5242ea102159`; `database.create_date = 2023-09-28 07:04:31`;
  `web.base.url = https://swr.smeplus.asia`. **SWR project — a DIFFERENT project from the series-18 OCC estate.**
- 651 TABLE DATA entries in the archive TOC. 1 company: บริษัท ข้าวสุวรรณภูมิ จำกัด (a rice miller).
- Source: three complete series-16 cores exist. RANKED against the deployment by module version:
  **E-ENT `odoo-16.0+e.20230401`** 144/190 present, **144/144 version-match**;
  E-SOM `odoo-16.0` 91/91; E-KIT `odoov16` 92/92. **Zero version mismatches in any tree.** E-ENT chosen.
- Whole-host index (58,263 manifests, 3,174 module names): of the 190 deployed modules,
  **165 have a version-matching copy on this host, 24 exist at another version, 1 (`studio_customization`,
  Studio-generated) has none anywhere.**

## S16-01 Deployment identity and activation
- 1,009 module rows; **190 installed** (189 at `16.0.x`, 1 NULL = `studio_customization`), 815 uninstalled, 4 uninstallable.
- base 16.0.1.3, account 16.0.1.2, stock 16.0.1.1, stock_account 16.0.1.1, purchase 16.0.1.2,
  purchase_stock 16.0.1.2, l10n_th 16.0.2.0, purchase_request 16.0.1.0, **stock_landed_costs 16.0.1.1 INSTALLED**,
  account_accountant 16.0.1.1.
- `anglo_saxon_accounting = FALSE`. Lock fields in this generation are `period_lock_date`,
  `fiscalyear_lock_date`, `tax_lock_date` (+`po_lock`) — a DIFFERENT vocabulary from series 18's five fields.
  **All three lock dates are NULL.**

## S16-02 Valuation policy — A MIXED POPULATION, the first in this programme
- Series 16 stores company-dependent values in **`ir_property`** (13,331 rows), not jsonb. `ir_property` does
  not exist in series 18; the jsonb columns do not exist here. Storage location is generation-specific.
- `property_valuation`: **1 global row = `manual_periodic`**, plus **15 per-category rows = `real_time`**.
  30 product categories total, so **15 real_time / 15 inheriting periodic**.
- `property_cost_method`: global `standard`; 18 categories `fifo`, 8 `average`.
- `property_stock_journal`: **one GLOBAL row → `account.journal,8`**.
- GRNI input account: 11 categories → `account.account,39`; also 1156/1160/1161; 6 explicitly NULL.
- **`property_account_creditor_price_difference_categ` IS configured** (1 category → `account.account,1173`).

## S16-03 The zero that is NOT zero — the programme's first positive control
- `stock_valuation_layer`: **74,982 rows, 57,863 (77.2%) carry `account_move_id`.**
  Series-18 OCC: 0 of 47,801. Series-19 estate: 0 of 14,441. **Here the valuation→GL path executes.**
- **Discriminating test** (SVL → `product_product` → `product_template.categ_id` → policy;
  coverage control: **0 of 74,982 unresolved**):

  | policy | linked | unlinked |
  |---|---|---|
  | `real_time` | **56,654** | 1,044 |
  | `manual_periodic` | 1,209 | **16,075** |

- Residual A: **296** real_time layers, non-zero value, **no** journal entry (748 more are value = 0.00 and are
  correctly skipped by the `currency_id.is_zero(value)` guard).
- Residual B: **1,209** manual_periodic layers that **do** carry a journal entry, across **9 distinct categories**.
- **Policy-change was tested as the explanation and REFUTED**: both residuals spread across 2023/2024/2025/2026
  roughly in proportion to total volume, while all 15 `real_time` `ir_property` rows were written
  2023-09-15..2023-12-08. `ir_property` records current state, not history — so history cannot be excluded,
  but the even spread does not support it.

## S16-04 A 15-order-of-magnitude subledger/ledger divergence
- **30 valuation layers carry |value| > 1e12**, up to **±1.5e21 THB**, with `unit_cost` values such as
  **744,082,316,162.43** and **−352,468,555,154.38** per unit (milled rice), from `WH/MO/…` manufacturing and
  `UB/…` unbuild documents. Negative unit costs are themselves invalid.
- Excluding those 30 rows the whole-table value sums to a sane **฿400,338,755.98**.
- **25 of the 30 carry a journal entry, and all 25 are POSTED** (dates 2024-08-17..2024-08-31).
- **BUT their journal entries are balanced and sane**: 50 items, debits = credits = **฿31,622,699.37**,
  net by account in the millions (Raw material +6,607,206.36; WIP −3,828,200.44; Semi Product −3,517,056.32;
  ByProduct +482,308.21; GRN +255,742.20).
- **Therefore: the GL was NOT corrupted. The inventory SUBLEDGER and the GL disagree by ~15 orders of magnitude
  on these 30 rows.** This is a subledger-to-ledger reconciliation break, not a corrupt posting.

## S16-05 GRNI clearing bridge — CONFIGURED **AND** EXECUTED
- `account_move_line`: **447,384 rows, 262 distinct accounts.**
- **Account 39 = `2900000 Goods Receipt Note(GRN)`, `liability_current`: 13,736 items,
  Dr ฿6,558,441,923.88 / Cr ฿6,486,344,109.63, net ฿72,097,814.25 outstanding.**
- Vendor bills relieve it: **6,653 bill lines debit account 39, ฿4,516,394,611.47 Dr, ฿0.00 Cr.**
- Valuation accounts all active: 1062 Raw material 22,561 items; 1068 WIP 39,935; 1289 Semi Product 10,993;
  1286 ByProduct 4,695.
- **`1173 4310005 Purchase price variance`: CONFIGURED, 0 items.** The price-difference engine is wired and
  has never fired in 183,590 journal entries.
- Positive controls: top accounts 1068 (39,935), 1117 (29,042), 1083 (27,366), 33 (22,978).

## S16-06 P2P populations
- `account_move`: **183,590** — posted 169,143 / draft 12,581 / cancel 1,866.
  Types: entry 143,811; **in_invoice 37,055**; out_invoice 2,602; in_refund 116; out_refund 6.
- Vendor bill journal items: 111,912. By type: payable 37,054; expense_direct_cost 36,640;
  asset_current 25,063; liability_current 7,844; expense 4,036; asset_fixed 925; income 281; **None 67**.
- `purchase_order` 5,881 (purchase 5,756 / draft 53 / cancel 71 / to approve 1); invoice_status
  invoiced 5,573 / to invoice 97 / no 211. `purchase_order_line` 10,490.
- **Received-not-invoiced: 79 lines, ฿12,678,776.50. Invoiced-not-received: 49 lines, ฿11,512,304.52.**
  (Contrast series-18 OCC: 1,580 lines / ฿30,080,689.78 with NO ledger recognition. Here the GRNI account
  carries the position.)
- `stock_picking` 20,098 (done 18,218). `account_payment` **22,468** (supplier 19,575 / customer 2,893).
- **`stock_landed_cost`: 0 rows.** Module INSTALLED, NEVER EXERCISED. (`stock_valuation_layer` even carries a
  `stock_landed_cost_id` column here.)
- `withholding_tax_cert`: **5,201** (done 5,191 / cancel 5 / draft 5), 2023-10-01..2026-07-13.
  Cert carries `income_tax_form` (the PND mapping), `payment_id`, `supplier_partner_id`.
  `account_payment` carries `wt_tax_id` and `wt_cert_cancel`.
- Reversal: **5,115 `account_move` rows carry `reversed_entry_id`**; the reversal *wizard* table has 0 rows.

## S16-07 Buddhist-era date leakage
- **30 `account_move` rows are dated year `2567`** (BE 2567 = 2024 CE) in a Gregorian date column —
  all `move_type = entry`, **all POSTED**, named `CABA2567…`, dated `2567-04-10` etc.
- Separately 1,733 rows are dated before 2015 (2005–2012) — opening/migration data.
- Any period report, ageing bucket or fiscal-year close reads these 30 as year 2567.

## Method defects committed and corrected inside this run (all before publication)
1. **Ranked the three series-16 trees by `odoo/addons` count and nearly called two of them "partial"** —
   they use the split layout with 461 and 464 modules under `<root>/addons`. All three are complete cores.
   My `ERR-P01-41` count of 3 stands.
2. **Version comparison produced false mismatches** because Odoo core manifests omit `version`;
   `module.py:56` defaults it to `'1.0'` and `:393` applies `adapt_version`. Corrected → 144/144.
3. **My host-index version normaliser assumed `16.0.`**, so a v18 tree's `stock_landed_costs 1.1` false-matched
   as `16.0.1.1`. Exact-version matching across the host index is only valid where the containing tree's series
   is confirmed. Core reads therefore come from E-ENT only.
4. **The first discriminating test classified all 74,982 layers as one policy** because I joined on
   `stock_valuation_layer.categ_id` — **a column that does not exist in series 16**. My parser padded it with
   nulls and the result looked plausible against a 57,863-row "positive control". Corrected by joining
   product → template → category, with an explicit coverage control (0 unresolved).
5. **Nearly published "quadrillions posted to the GL"** — the linked journal entries are balanced and sane.
   Checked before publishing.
