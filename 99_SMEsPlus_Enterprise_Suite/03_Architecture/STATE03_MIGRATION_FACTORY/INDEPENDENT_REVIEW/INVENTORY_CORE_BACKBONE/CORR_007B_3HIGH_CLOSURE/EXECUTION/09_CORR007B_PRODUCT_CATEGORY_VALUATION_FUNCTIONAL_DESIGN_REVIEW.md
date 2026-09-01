# CORR-007B — Boss Addendum: Product Category Valuation Policy Review

Session: `SMEPLUS-26-09-02-CORR007B-3HIGH-CLOSURE-001` (Boss Addendum 3, `N-A12-01`)
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `audit/inventory-core-corr007b-3high-closure-010`
Base commit: `deceb7339b39eba309236782f159f8393224f5fd`
Timestamp: 2026-09-02
Mode: Evidence-first / clean-room / no development authorization / read-only

## 0. Relationship to file 08

Boss's third addendum states the prior proof is still insufficient and asks specifically whether
Product Category — not company, not product — is the true owner of costing/valuation policy, using
screenshot terminology ("Standard Price", "Automated"/"Manual", "Stock Journal"/"Stock Input"/"Stock
Output"/"Stock Valuation Accounts"). Most of the underlying mechanism was already proven in
`08_..._FUNCTIONAL_DESIGN_PROOF.md` §15–§20 (the `periodic`/`real_time` selection, its class location was
not yet nailed down explicitly, and category-vs-company precedence was shown via one compute method but
not fully walked through). This file closes that specific gap and independently checks Boss's screenshot
terminology against source rather than assuming a 1:1 label match.

## 1. Proof point 1 — Product Category is the owner of costing method and valuation policy

`stock_account/models/product.py:660` — `class ProductCategory(models.Model):` (full class boundary
confirmed: next class starts elsewhere in the file; `property_valuation` at `:666-675` and
`property_cost_method` at `:676-689` are both declared inside this class, not on `ProductTemplate`
(`:12`) or `ProductProduct` (`:163`), which are separate classes earlier in the same file).

Both fields are `company_dependent=True` — meaning the same `product.category` record can hold a
different value per company, but for a given company, **the category is the object that carries the
setting**, matching Boss's clarification exactly. Confirmed.

## 2. Proof point 2 — how products inherit valuation behavior from Product Category

`stock_account/models/product.py:73-77` (already cited in file 08 §16, re-verified in full context this
session):

```
@api.depends('categ_id.property_valuation')
def _compute_valuation(self):
    for product_template in self:
        product_template.valuation = (
            product_template.categ_id.with_company(product_template.company_id).property_valuation
            or self.env.company.inventory_valuation
        )
```

Precedence, proven directly from this compute method: **category value, if set, wins; if the category
has no value set for the current company, fall back to `res.company.inventory_valuation`.** The same
pattern applies to `cost_method` at `:62-68` against `categ_id.property_cost_method`. There is no
product-template-level or product-variant-level override field — confirmed by the same full-tree search
already reported in file 08 §16 ("no field found at that granularity").

## 3. Proof point 3 — Manual vs. Automated valuation, reconciled against source terminology

Boss's screenshot uses "Automated" / "Manual". The actual field (`stock_account/models/product.py:666-675`,
full declaration read) is:

```
property_valuation = fields.Selection(
    string="Inventory Valuation",
    selection=[
        ('periodic', 'Periodic (at closing)'),
        ('real_time', 'Perpetual (at invoicing)'),
    ],
    ...
    help="""Periodic: The accounting entries are suggested manually in the inventory valuation report.
    Perpetual: An accounting entry is automatically created to value the inventory when a product is
    billed or invoiced.
    """)
```

**This is the same field already proven in file 08, not a different one.** The selection *values*
(`periodic`/`real_time`) and this source snapshot's UI *labels* ("Periodic (at closing)"/"Perpetual (at
invoicing)") do not literally say "Manual"/"Automated" — but the field's own help text uses exactly that
language ("suggested **manually**" vs. "**automatically** created"), so Boss's screenshot vocabulary is
evidence-consistent with this field, most likely reflecting a different Odoo release's shorter button
labels for the identical two options. This is reported precisely rather than silently assumed identical,
because getting the field right matters more than getting the label right.

## 4. Proof points 4–5 — mapping Manual/Periodic and Automated/Perpetual to posting behavior

Unchanged from file 08 §17 (`_should_create_account_move()`, `stock_move.py:630-635`, re-cited, not
re-derived): `product_id.valuation == 'real_time'` is the sole method-dependent condition in the
per-move posting gate. Periodic ⇔ deferred-to-closing behavior; Perpetual ⇔ per-move immediate posting.
No new evidence needed here beyond file 08; the mapping Boss asks for is exactly the one already proven.

## 5. Proof point 6 — Standard Price / FIFO / AVCO effect on valuation and close

`stock_account/models/product.py:676-689` (`property_cost_method`, full declaration read) — three
values: `standard` (fixed cost per product, set manually, variance absorbed via
`property_price_difference_account_id` under Perpetual — file 08 §20), `fifo` and `average` (both
recomputed from actual move history via `_run_fifo_batch`/`_run_average_batch`, `product.py:256-263`,
already cited file 08 §18). Cost method and valuation timing (Periodic/Perpetual) are **independent
axes** — any of the three cost methods can be paired with either valuation timing; source does not couple
them. Confirmed by the field declarations being entirely separate selections with no mutual constraint
found in either field's definition or compute logic.

## 6. Proof point 7 — does `stock.move` create or skip accounting entries by category setting?

Identical to §4 — the gate reads `self.product_id.valuation`, a related/compute field ultimately sourced
from the product's category (via §2's precedence chain). No separate category-level gate exists;
category flows through the product to the move via this single computed field. Confirmed, not
re-derived.

## 7. Proof point 8 — how Product Category accounts drive GL posting

| Boss's screenshot term | Field found in source | Class / model | Citation | Status |
|---|---|---|---|---|
| Stock Journal | `property_stock_journal` (category) / `account_stock_journal_id` (company) | `product.category` / `res.company` | `stock_account/models/product.py:691-692`; `res_company.py:12` | **Found**, both levels. |
| Stock Valuation Account | `property_stock_valuation_account_id` | `product.category` | `stock_account/models/product.py:694-698` | **Found.** |
| Stock Variation Account | `account_stock_variation_id` (related to the above) | `product.category` | `stock_account/models/product.py:702-704` | **Found** — this is the P&L-side true-up/expense-equivalent account (file 08 §20). |
| Price Difference Account | `property_price_difference_account_id` | `product.category` | `stock_account/models/product.py:699-701` | **Found**, Perpetual/standard-cost only (field help text says so explicitly). |
| **Stock Input Account** | `property_stock_account_input_categ_id` | — | Referenced only in `point_of_sale/tests/test_pos_stock_account.py:41` and `addons_extra/om_data_remove/models/model.py:265` | **NOT declared as a field anywhere in the available core module source** (`stock`, `stock_account`, `account`, `product`, `point_of_sale/models/product_category.py` all checked directly). |
| **Stock Output Account** | `property_stock_account_output_categ_id` | — | Same two reference-only locations | **Same — not declared.** |
| Expense Account | `property_account_expense_categ_id` | `product.category` | `account/models/product.py:23-24` (`class ProductCategory`, `account` module) | **Found** — owned by `account`, not `stock_account`. |
| Income Account | `property_account_income_categ_id` | `product.category` | `account/models/product.py:16-17` | **Found** — owned by `account`, not `stock_account`. |
| (Not in Boss's list, but the modern equivalent of Input/Output) | `stock.location.valuation_account_id` | `stock.location`, not `product.category` | `stock_account/models/stock_location.py:11-14` (full 41-line file read) | **Found** — this is the actual interim/contra account used by `_get_account_move_line_vals` (`stock_move.py:215-224`, file 08 §7) for Perpetual per-move postings. It lives on the **location** (e.g. the Supplier or Customer virtual location), not on the category. |

**Named finding, reported precisely rather than smoothed into a match**: Boss's screenshot most likely
reflects a materially older Odoo release where "Stock Input Account"/"Stock Output Account" were
`product.category` fields (this was true in Odoo ≤ 16). In this source baseline, that classic two-account
category-level design has been replaced by a **location-level** `valuation_account_id` for the
Perpetual/real-time contra-posting, plus the category-level Stock Valuation / Stock Variation / Price
Difference accounts already proven above. This is a genuine architecture difference between what Boss's
screenshot shows and what this source snapshot implements, not a proof failure — SMEsPlus functional
design must use the location-based model actually present in source, not the category-based
Input/Output model from the screenshot.

## 8. Proof points 9–11 — month-end close (Manual/Periodic), reconciliation (Automated/Perpetual), year-end

Unchanged from file 08 §7, §18–§19, §22 — no new mechanism was found beyond what those sections already
prove. Re-stated briefly for completeness, not re-derived: Periodic month-end = `action_close_stock_
valuation` computing and posting the value gap (file 08 §7); Perpetual "reconciliation" = the same
`stock_value()`/`stock_accounting_value()` pair run as a check rather than as the primary posting
mechanism, surfaced via `stock_account.stock.valuation.report` (file 08 §7); year-end = no
month-12-specific code path and no source-evidenced P&L-to-Retained-Earnings closing entry (file 08
§22, G-6) — this conclusion is unchanged by the category-level investigation in this file.

## 9. Proof point 12 — Account × Inventory Functional Design Matrix by Product Category

| Category setting | GL impact of a `stock.move` | When value is known | Accounts touched | Governing citation |
|---|---|---|---|---|
| `property_valuation = 'real_time'` (Automated/Perpetual), any cost method | Immediate, per move, at validation | Continuously | Stock Valuation (asset) ↔ `stock.location.valuation_account_id`; Price Difference (standard cost variance only) | `stock_move.py:168-224`, `product.py:694-701` |
| `property_valuation = 'periodic'` (Manual/Periodic), any cost method | None at move time; deferred | Only after `action_close_stock_valuation` runs | Stock Valuation (asset) ↔ Stock Variation (P&L true-up) | `stock_move.py:630-635`; `res_company.py:49-263` |
| `property_cost_method = 'standard'` | Move valued at `product.standard_price` | Known instantly (fixed cost) | Price Difference absorbs bill-vs-standard gap (Perpetual only) | `product.py:679-681`, `:699-701` |
| `property_cost_method = 'fifo'`/`'average'` | Move valued by consuming/averaging actual cost layers | Recomputed as of any `at_date` via `_run_fifo_batch`/`_run_average_batch` | Same Stock Valuation/Variation accounts as above | `product.py:256-263` (cited file 08 §18) |
| No category override set | Falls back to `res.company.inventory_valuation`/`cost_method` | Same as whichever method the company default resolves to | Falls back to `res.company.account_stock_journal_id`/`account_stock_valuation_id` when category-level accounts are unset | `product.py:73-84`; `res_company.py:12-38` |

## 10. Evidence integrity

All newly-cited files this session (`stock_account/models/stock_location.py`,
`account/models/product.py`, `product/models/product_category.py`,
`point_of_sale/tests/test_pos_stock_account.py`, `addons_extra/om_data_remove/models/model.py`,
`point_of_sale/models/product_category.py`) are hashed in `06_CORR007B_SHA256_MANIFEST.txt` §E4.

## 11. Disposition

This file adds one confirmed structural fact (Product Category is the proven owner, class-verified) and
one genuine negative finding (Stock Input/Output accounts are not declared fields in this source
baseline; the modern equivalent is location-level) to the six gaps already named in file 08. It does not
introduce a seventh gap on its own — the Input/Output finding is folded into file 08's G-6 territory as a
terminology/architecture-version reconciliation note for Team B, not a new open risk, because the
underlying GL mechanics (which accounts move value where) were already fully proven in file 08 §7 and
§20 using the accounts that do exist in source.

**`N-A12-01` disposition is unchanged by this file: HIGH REMAINS.** This file strengthens the evidence
base; it does not close the item. See `04_CORR007B_FINAL_HIGH_DISPOSITION_REGISTER.md` and
`05_CORR007B_BOSS_DECISION_RECOMMENDATION.md` (both updated) and the four-lens challenge in
`14_CORR007B_AI_EXPERT_PANEL_CHALLENGE_REPORT.md` (originally numbered `10`; see
`16_CORR007B_CLEANUP_SUPERSESSION_INDEX.md` for why).
