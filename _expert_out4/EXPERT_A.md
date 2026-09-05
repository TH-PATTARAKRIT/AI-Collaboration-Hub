# EXPERT_A — AAS-03 Expert A (Leader Functional Design)
## Adversarial challenge of the P01 SERIES-18 frozen findings package
Date: 2026-09-05 · Mode: READ-ONLY forensic. No database written, no source modified,
no module installed, no Odoo server run. All work is `pg_restore --data-only` extraction
plus static reading of two reference source trees.

**Primary disproof assignment:** *Disprove that periodic valuation policy explains the
0-of-47,801 zero-link result.*

**Headline:** I could not overturn the periodic reading as a **sufficient** cause, and I
independently strengthened part of its source basis. I did break it as an **identified,
exclusive and complete** explanation, on three separate grounds, and I broke the
discriminating set that the package relies on to rule out migration artefact. On the
secondary assignment I reproduced every published P2P figure to the digit and found one
material measurement defect in the headline exposure.

---

## 0. Evidence base and independence

The working directory did **not** contain the three tables the package's central claims
rest on (`stock_valuation_layer`, `ir_default`, `account_move`). I therefore re-extracted
them myself rather than inheriting the author's parse.

```
$ ls /…/scratchpad/s18/T_*.sql | xargs -n1 basename
   T_account_full_reconcile.sql T_account_journal.sql T_account_move_line.sql
   T_account_partial_reconcile.sql T_account_payment.sql T_ir_config_parameter.sql
   T_pcrel.sql T_product_category.sql T_product_template.sql T_purchase_order.sql
   T_purchase_order_line.sql T_purchase_request.sql T_purchase_request_line.sql
   T_res_users.sql T_scglrel.sql T_stock_move.sql T_stock_picking.sql
   T_stock_picking_type.sql T_stock_quant.sql
   -> stock_valuation_layer, ir_default, account_move: ABSENT
```
Re-extracted (prefix `A_`) from the same archive with the same tool:
```
$ PG=/opt/homebrew/opt/postgresql@18/bin/pg_restore
$ D=~/OCC_BACKUP/idemo18_uat_pre_scgl_occ_website_20260830_085432.dump
$ for t in stock_valuation_layer ir_default account_move product_product \
           account_account res_company ir_module_module ir_model_fields \
           ir_model_data ir_model_fields_selection stock_location account_tax \
           account_tax_purchase_order_line_rel; do
      $PG -t $t --data-only -f A_$t.sql "$D" 2> A_$t.err; done
  stock_valuation_layer -> 10451068 bytes, err=0
  ir_default            ->     5197 bytes, err=0
  account_move          ->  8500935 bytes, err=0
  ir_model_data         -> 27914048 bytes, err=0
  …
$ for f in A_*.sql; do grep -c '^COPY public\.' $f; done   # all == 1
```
Each extract contains exactly one `COPY` block, so no sibling table contaminated the parse
(`pg_restore -t` accepts patterns; this was checked, not assumed).

**Declared enumeration frame used throughout.** Where I make a negative claim I state:
POPULATION (the set of things counted) · PATTERN (the text/predicate matched) ·
PATH SET (where I looked) · UNIT (what one count is).

---

## 1. Route 1 — Can valuation resolve to `real_time` anywhere in this deployment?

### A-01 · The `ir_default` claim reproduces, and the population is closed
POPULATION: every row of `ir_default` in the archive. PATTERN: none — I printed all 54
rows and resolved `field_id` through `ir_model_fields`. PATH SET: `A_ir_default.sql`,
`A_ir_model_fields.sql`. UNIT: one `ir_default` row.

```
$ python3 a1.py
ir_default rows: 54
…
10  product.category.property_valuation  user=None co=None cond=None val="manual_periodic"
…
```
Exactly **one** row for `product.category.property_valuation`: `user_id` NULL,
`company_id` NULL, `condition` NULL, value `"manual_periodic"`. There is no
company-scoped row, no user-scoped row and no conditional row that could outrank it.
Because I printed the entire table rather than filtering, this is a closed enumeration,
not a search that returned nothing.

Positive control in the same output: 53 other rows print with resolved model/field names,
including four `property_stock_journal` rows and four `property_account_*` rows, so the
join and the print path both fire.

### A-02 · The jsonb claim reproduces, with a stronger positive control than published
POPULATION: all 126 `product_category` rows. PATH SET: `T_product_category.sql`.
UNIT: one category.
```
$ python3 a2.py
product_category rows: 126
  property_valuation:                     non-null   0/126
  property_cost_method:                   non-null  18/126  [('{"1": "average"}', 18)]
  property_stock_account_input_categ_id:  non-null  15/126
  property_stock_valuation_account_id:    non-null  15/126
  property_stock_journal:                 non-null   0/126
```
The zero on `property_valuation` sits **between two non-zero columns of the same jsonb
type in the same parse of the same table**. A parser that could not register a jsonb value
would have returned zero for `property_cost_method` too. The negative is controlled.

### A-03 · I extended the check to a storage location the package did not name — no override
The package checked two storage locations (jsonb + `ir_default`). There is a third thing
that could defeat both: a module **redefining the field**. I tested that on the
**deployment**, not on source, so the test covers all 361 installed modules including the
ten with no version-matching source copy.

Mechanism (verified in source before relying on it):
`odoo/addons/base/models/ir_model.py:1233-1247` — an `ir.model.data` xmlid
`field_<model>__<name>` is created for **every** module satisfying
`module == model._original_module or module in field._modules or …`. A module that
contributes any definition of an existing field therefore gets its own xmlid row.

POPULATION: all 225,529 `ir_model_data` rows. PATTERN: `model = 'ir.model.fields'` and
`res_id` in the field-id set {7646, 7635, 7643, 7647, 7687, 7688}. PATH SET:
`A_ir_model_data.sql`. UNIT: one xmlid row.
```
$ python3 a4.py
ir_model_data rows: 225529
  product.category.property_valuation:  module=stock_account
  product.template.valuation:           module=stock_account
  product.product.valuation:            module=stock_account
  product.category.property_cost_method:module=stock_account
  svl.account_move_id:                  module=stock_account
  svl.account_move_line_id:             module=stock_account
```
Positive control — the same query over the 16 installed custom modules returns 718 field
xmlids across 13 of them (`scgl_multi_approve_core` 264, `purchase_request` 170,
`scgl_occ_transportation_costs` 95, `scgl_dashboard_core` 94, `scgl_signature` 28,
`scgl_product_category_company` 21, …). The query can find a custom module owning a field;
it finds none on any valuation field.

Deployed field metadata agrees with v18 core and shows no customisation:
```
product.category.property_valuation : ttype=selection store=t company_dependent=t state=base
product.template.valuation          : store=f related=categ_id.property_valuation readonly=t
product.product.valuation           : store=f related=categ_id.property_valuation readonly=t
```
`state = 'base'` on all three — none is a Studio/manual field.

Deployed selection values (`ir_model_fields_selection`, 3,503 rows) for field 7646 are
exactly `manual_periodic`/`real_time` — **no third value was added** by any module:
```
field 7646 value='manual_periodic' seq=0  {"en_US":"Manual","th_TH":"ด้วยตัวเอง"}
field 7646 value='real_time'       seq=1  {"en_US":"Automated","th_TH":"อัตโนมัติ"}
```

### A-04 · The ORM resolution the package cites is correct — I re-derived it
`odoo/models.py:2995-3013` builds `column -> '<env.company.id>'` and then
`COALESCE(field, to_jsonb(fallback))`, where `fallback =
field.get_company_dependent_fallback(records)` (`odoo/fields.py:785-791`) which calls
`ir.default._get_model_defaults` (`addons/base/models/ir_default.py:153-182`,
`ORDER BY d.user_id, d.company_id, d.id`, first row kept per field).

So: per-company jsonb key first; if that key is absent, the `ir_default` row wins. With
the jsonb NULL on 126/126 and a single global `ir_default` of `"manual_periodic"`, every
category in every one of the four companies resolves to `manual_periodic`. Field
definition confirms there is no Python-level `default=` to fall through to
(`stock_account/models/product.py:915-920` — `company_dependent=True, copy=True`, no
`default`).

**Verdict on Route 1: I could not break it.** The claim is correct and is now supported by
one more independent test than the package published.

---

## 2. Route 2 — Is `_validate_accounting_entries` the only writer? **No. The package is incomplete here.**

The package (S18-03) attributes the zero to a single mechanism. I enumerated the writers.

POPULATION: v18 core addons tree. PATTERN: `stock_valuation_layer_ids` (the o2m inverse of
both `account_move_id` and `account_move_line_id`), plus direct `account_move_id` /
`account_move_line_id` assignment, excluding `/tests/`. PATH SET:
`/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons`. UNIT: one source
line that places the key into an `account.move` / SVL vals dict.
```
$ grep -rn --include="*.py" "stock_valuation_layer_ids" "$V18" | grep -v "/tests/"
$ grep -rn --include="*.py" "account_move_line_id" "$V18" | grep -v "/tests/" | grep -iE "svl|valuation"
```

Six write sites, not one:

| # | Site | Gate | Gated on valuation? |
|---|---|---|---|
| W1 | `stock_account/models/stock_move.py:683` `_prepare_account_move_vals` | via `_validate_accounting_entries` `stock_valuation_layer.py:78` | yes — `real_time` |
| W2 | `stock_account/models/stock_valuation_layer.py:267` | `product.valuation != 'real_time': continue` (`:245`) | yes |
| W3 | `stock_account/models/product.py:790` `_svl_empty_stock_am` | callers `product.py:76, 87, 1068` | yes |
| W4 | `stock_account/models/product.py:837` `_svl_replenish_stock_am` | callers `product.py:97, 1079` | yes |
| W5 | `stock_account/wizard/stock_valuation_layer_revaluation.py:215` | `if self.property_valuation != 'real_time': return` (`:187`) | yes |
| W6 | `purchase_stock/models/account_move_line.py:298-313` `_prepare_pdiff_svl_vals` | see A-05 | **NO** |
| — | `stock_landed_costs/models/stock_landed_cost.py:197` | — | module not installed (no `stock_landed_cost*` table in the TOC) |

W1–W5 are all periodic-gated, so the package's conclusion for those five is right — but the
package published one of them and generalised. **W6 is not gated on valuation at all.**

### A-05 · CHALLENGED — a writer of BOTH link columns that periodic policy does not stop
`purchase_stock/models/account_move_line.py:298-313`:
```python
def _prepare_pdiff_svl_vals(self, corrected_layer, quantity, unit_cost, pdiff):
    common_svl_vals = {
        'account_move_id': self.move_id.id,
        'account_move_line_id': self.id,
        …
```
Gate chain, read end to end:
* `purchase_stock/models/account_invoice.py:118-130` — `AccountMove._post`:
  `valued_lines |= invoice.invoice_line_ids.filtered(lambda l: l.product_id and
  l.product_id.cost_method != 'standard')`. **The predicate is `cost_method`, not
  `valuation`.**
* `…/account_move_line.py:32-52` `_apply_price_difference` — gates on quantity and on the
  existence of incoming layers. **No valuation gate.**
* `…/account_move_line.py:246-267` `_prepare_pdiff_vals` — the **AML** half is gated
  (`and self.product_id.valuation == 'real_time'`, line 248), but the **SVL** half is
  gated only by `if not float_is_zero(unit_valuation_difference * qty_to_correct, …)`.
  **No valuation gate.**

So in v18, under `manual_periodic`, a stock valuation layer carrying a non-null
`account_move_id` **and** a non-null `account_move_line_id` can still be created.

**And the precondition is satisfied in this deployment.** `property_cost_method` jsonb sets
`{"1": "average"}` on 18 of 126 categories, i.e. `cost_method != 'standard'` for company 1.
```
$ python3 a7.py
categories with jsonb cost_method containing 'average': 18
  ['11','16','24','25','39','41','46','86','89','90','91','92','93','94','104','122','123','124']
```

### A-06 · The path was REACHABLE and was EXERCISED — measured, not assumed
POPULATION: all 40,353 `account_move_line` rows. PATTERN: `move_type` in
(`in_invoice`,`in_refund`,`in_receipt`) AND `state='posted'` AND `company_id='1'` AND
`product_id` resolves to a category in the 18-set. UNIT: one AML.
```
$ python3 a8.py
AML rows: 40353
AML with purchase_line_id non-null: 2606      <-- positive control for the column
posted vendor-bill AML with a product: 2922   (co1 1660 / co2 1262)
  company 1 AND category in the 18 'average' set: 354
     of those, purchase_line_id non-null: 18
     categories hit: 104(328) 93(14) 24(8) 123(4)
```
Tracing all 18 candidates (`a9.py`), 16 have a valued incoming layer and **every one shows
a real price difference** — e.g. `AML 48062 / AP2026/05/0065`, bill unit 21,400.00 against
`SVL 29206 unit_cost 20,000.00`; `AML 53525 / AP2026/07/0125`, 9,862.00 against 9,216.82;
`AML 49130`, 1,500.00 against 1,401.87.

**And yet 0 of 47,801 rows carry either link.** The reason visible in the dump is
*independent of valuation policy*: **every one of those 16 layers has
`remaining_qty = 0.00`**, which drives `out_layer_qty = total_qty`, hence
`out_qty_to_invoice = invoicing_layer_qty`, hence `qty_to_correct = 0`, hence
`float_is_zero(unit_valuation_difference * qty_to_correct)` — no SVL. The entire
difference is routed to the "already out" branch, whose only output (the pdiff AML) *is*
valuation-gated.

**Consequence for the package:** the 0 on `account_move_line_id` — which S18-03 folds into
the periodic explanation with the words *"Same for `account_move_line_id`"* — is **not
explained by periodic policy at all**. It is explained by a `remaining_qty = 0` condition
on a path periodic policy does not control. The 0 on `account_move_id` is likewise
over-determined for this sub-population. **The periodic explanation is sufficient but not
identified.**

### A-07 · Ruled out (with citation) — `_ignore_automatic_valuation` is not a cause
My brief listed it as a candidate. It is not one: `_ignore_automatic_valuation`
(`stock_account/models/stock_move.py:591`, overridden `mrp_account/models/stock_move.py:23`)
is referenced **only** at `stock_account/models/stock_move.py:573`, inside
`_prepare_analytic_lines`. It never reaches the `account_move_id` write. Reported as a
negative so it is not re-opened.

### A-08 · Ruled out with a positive control — `_should_exclude_for_valuation`
`stock_account/models/stock_move.py:695-699` returns
`self.restrict_partner_id and self.restrict_partner_id != self.company_id.partner_id`.
```
$ python3 b2.py
GUARD restrict_partner_id: {'restrict_null': 44935, 'no_move': 2866}
   POSITIVE CONTROL stock_move.restrict_partner_id non-null overall: 0 / 51081
```
The column exists and parses; it is uniformly NULL across all 51,081 stock moves. Not a
cause. The negative is controlled: I confirmed the column can be read, and that its
population-wide count is 0 rather than that my filter found nothing.

---

## 3. Route 3 — Is the zero over-determined? **Yes, for 4,574 of 47,801 layers.**

POPULATION: all 47,801 SVL rows. PATTERN: the four silent skip conditions that
`_validate_accounting_entries` / `_account_entry_move` apply *before* any valuation
consideration. PATH SET: `A_stock_valuation_layer.sql`, `T_stock_move.sql`,
`A_product_product.sql`, `T_product_template.sql`. UNIT: one SVL row.

### A-09 · CHALLENGED — 9.57% of the population would be unlinked even under `real_time`
```
$ python3 b2.py
GUARD is_storable over 47,801 SVLs: {'t': 46712, 'f': 1089}
GUARD currency_id.is_zero(value): value == 0 exactly: 1205 / 47801
GUARD no stock move at all: 2866 / 47801

COUNTERFACTUAL: SVLs that would be skipped/unlinked EVEN UNDER real_time: 4574 / 47801
   no_stock_move                                  2319
   zero_value                                     1096
   not_storable                                    574
   no_stock_move + not_storable                    476
   zero_value + no_stock_move                       70
   zero_value + not_storable                        38
   zero_value + no_stock_move + not_storable         1
```
Source basis for each: `_account_entry_move` returns `[]` silently when
`not self.product_id.is_storable` (`stock_move.py:706-708`);
`_validate_accounting_entries` does `continue` on
`svl.currency_id.is_zero(svl.value)` (`stock_valuation_layer.py:80`); and a layer with no
move yields an empty `linked_move`, so no `am_vals` are appended
(`stock_valuation_layer.py:82-92`).

For these 4,574 rows the data cannot distinguish "periodic" from three other sufficient
causes. The package's line **"CLASSIFICATION: EXPECTED UNDER PERIODIC POLICY — VERIFIED"**
should be scoped to the 43,227 rows where periodic is the only silent explanation.

### A-10 · The counterfactual is not even coherent for most categories — this *helps* the package
Under `real_time`, `_get_accounting_data_for_valuation`
(`stock_account/models/stock_move.py:477-500`) raises `UserError` when the journal or any of
the three accounts is missing. So for the unconfigured categories the counterfactual is not
"a null link" — it is **a blocked stock operation**. I checked the location escape hatch the
package did not check (`_get_src_account`/`_get_dest_account`,
`stock_move.py:531-538`, fall back to `location.valuation_out/in_account_id`):
```
$ python3 b1.py
stock_location rows: 86
  valuation_in_account_id:  non-null 0/86
  valuation_out_account_id: non-null 0/86
  POSITIVE CONTROL company_id non-null: 80/86
  POSITIVE CONTROL usage: internal 60, inventory 8, view 7, transit 5, production 4, supplier 1, customer 1
```
No location supplies a valuation account. Distribution of the layers:
```
$ python3 b3.py
categories with all 3 stock accounts in jsonb: 15
SVL by categ configured?: CONFIGURED 46458, NOT_CONFIGURED 1343
```
So 46,458 of 47,801 layers sit in categories that *do* carry the accounts. For those, a
`real_time` counterfactual would have produced entries; for the other 1,343 it would have
raised. Either way the observed silent NULL is what periodic predicts. This is a genuine
strengthening of the package's identification argument on the main path, and it should be
published because it is the only thing that rules out "it would have been zero anyway".

---

## 4. Route 4 — Break the "1,812 native layers" discriminating set. **It breaks.**

This is the single most consequential correction I have. The set exists to rule out
"the zero is a migration artefact". It does not do that.

### A-11 · CHALLENGED — `create_date` on this table is back-dated data, not an insertion time
```
$ python3 b5.py
database.uuid        = 551ab874-9acb-11f1-b150-6ec7a480be3d
database.create_date = 2026-08-18 06:09:12
web.base.url         = https://occ.smeplus.cloud

SVL create_date  min: 2026-01-01 00:00:00           max: 2026-08-29 10:23:34.494039
SVL write_date   min: 2026-08-25 12:19:13.83922     max: 2026-08-29 10:23:34.494039
SVLs with create_date BEFORE database.create_date: 44947
SVLs with write_date  BEFORE database.create_date: 0
write_date by day: 2026-08-25: 47218 | 2026-08-29: 324 | 2026-08-27: 153 | 2026-08-28: 55 | 2026-08-26: 51
```
44,947 rows claim a `create_date` **earlier than the database itself was created**. The
`write_date` minimum is 2026-08-25 12:19:13 — i.e. **the entire 47,801-row table was
physically written in a five-day window, seven days after the database was created, and
98.8% of it on a single day.** `create_date` was set explicitly by a loader; only
`write_date` carries real insertion time.

Therefore **there is no sub-population separable by insertion time.** Any classifier that
reads `create_date` as provenance — as the package's "created 2026-08-25..08-29" phrasing
does — is unsound on this table.

### A-12 · CHALLENGED — 69% of the "native runtime output" set is a machine stock-take
```
$ python3 b4.py
### 1,812 'native' layers -> description prefix families
   1254  Product Quantity Updated        <- inventory adjustment
    222  OCC/MO<ref>      155  WH/MO<ref>
     43  OCC/OUT<ref>      37  WH/OUT<ref>
     23  OCC/IN<ref>       18  WH/IN<ref>
     20  DS<ref>           17  UB<ref>     2  Revaluation of …
### create_uid of the 1,812: {'1': 1253, '114': 383, '102': 172, '117': 4}
### users: 1=__system__  114=ocean.trans.ac02@…  102=occgroup.st.sw@…  117=occgroup.ac.ap03@…
### of the 1,812: is_inventory 't' = 1254 | purchase-linked = 61 | picking_id non-null = 142
```
1,254 of the 1,812 are inventory adjustments written by `__system__` inside the same
five-day load window as the migration. Calling them "native v18 runtime output" overstates
the denominator by a factor of ~3.2.

### A-13 · SUPPORTED on a corrected set — two independent classifiers converge on 558/559
```
$ python3 b6.py
SVLs with a human create_uid: 559 | description family: all OTHER
  create_date range 2026-08-26 06:58 .. 2026-08-29 10:23
  is_inventory of their moves: None 375, 'f' 183, 't' 1
  account_move_id non-null: 0   value != 0: 544   purchase-linked: 61

Business-document (non-inventory-adjustment) layers in the OTHER family: 558
  account_move_id non-null: 0   value != 0: 543   purchase-linked: 61
  by create_uid: 114:382  102:172  117:4
  categ configured for real-time accounts (15-set): CONFIGURED 541, NOT 17
```
Classifier 1 (`create_uid` is a human) gives 559. Classifier 2 (the move is not an
inventory adjustment) gives 558. They overlap on 558 — one human-entered inventory
adjustment separates them. Two classifiers with different units agreeing to one row is a
sound set.

**The package's conclusion survives on this corrected set: 0 of 558.** The over-determination
-free core is tighter still — **541 layers** that simultaneously have a stock move, a
non-zero value, a storable product and a category carrying all three accounts. That number,
not 1,812, is the honest discriminating denominator, and it is still decisive.

### A-14 · MISSING — the P2P-relevant sub-population is not in the discriminating set at all
Only **61** of the 558 are purchase-linked. The receipt-to-GRNI claim that S18-05 and
S18-07 turn on is therefore tested on 61 rows, not 1,812:
```
$ python3 b4.py
### SVLs on purchase-linked moves: 2146   family: v14_2026 2085, OTHER 61
###   account_move_id non-null among them: 0
```
2,085 of the 2,146 purchase-linked layers are migration rows. The package should say so.

### A-15 · RISKY — the SVL population is not internally consistent with the product master
```
$ python3 c5.py
done purchase-linked moves: 3124
  WITHOUT any valuation layer: 1721
  their product type: type=consu,storable=t 1480 | type=consu,storable=f 241
  their quantity == 0?: qty>0 1721
  WITH a layer: type=consu,storable=t 1183 | type=consu,storable=f 220
```
**1,480 done purchase receipts on storable products with quantity > 0 carry no valuation
layer at all**, while **220 purchase receipts on non-storable products do** (and 1,089 SVLs
sit on non-storable products across the table, per A-09). Both directions are wrong under
normal v18 behaviour. The loader built layers on a basis other than move-by-move
valuation. This weakens *any* inference — the periodic one included — drawn from patterns
across the full 47,801, and it is a finding in its own right.

---

## 5. Custom-module reach — how far the negative extends, and where it stops

### A-16 · SUPPORTED — no custom module extends any valuation model, tested on the deployment
POPULATION: all 225,529 `ir_model_data` rows. PATTERN: `module` in the 16 installed custom
modules. UNIT: one xmlid.
```
$ python3 c6.py
  purchase_request:               170 fields / 12 models | KEY: stock.move(3) purchase.order.line(2) product.template(1) product.product(1)
  scgl_product_category_company:   21 fields /  3 models | KEY: product.category(9) product.template(6) product.product(6)
  scgl_signature:                  28 fields /  3 models | KEY: account.move(8)
  scgl_delivery_cost:              19 fields /  4 models | KEY: stock.picking(2)
  scgl_stock_fleet:                 2 fields /  1 model  | KEY: stock.picking(2)
  scgl_multi_approve_core:        264 fields / 12 models | KEY: none
  … (13 modules, 718 field xmlids total)
### Any custom module owning an xmlid on stock.valuation.layer: 0 rows
### total custom xmlids: 1160  (ir.model.fields 718, selections 94, views 77, models 75, access 63, rules 36…)
```
No custom module owns a single xmlid on `stock.valuation.layer`. The nine
`product.category` fields owned by `scgl_product_category_company` are
`company_ids, usage_type, active, show_on_product, scgl_company_scope_summary,
scgl_allow_sale, scgl_allow_purchase, scgl_allow_expense,
scgl_available_for_current_companies` — none is a valuation or property field, and all are
`company_dependent = f`. This corroborates S18-12's explicit check.

### A-17 · MISSING — the deployment-side test bounds fields, not methods
This is the residual doubt I could not close. An `ir_model_data` xmlid is created for
**field, model, view and data** extension. A pure Python method override —
`_validate_accounting_entries`, `_account_entry_move`, `ProductCategory.write`,
`AccountMove._post` — leaves **no database trace whatsoever**. Ten of the sixteen custom
modules have no version-matching source copy (S18-11), so for those ten a method override
is unverifiable by any means available in this session. `scgl_account_coa_control` is the
sharpest instance: it owns four `ir.ui.view` xmlids and zero fields, its name asserts
chart-of-accounts control, and its only source copy is under a root P01 declared CLASS C
while this deployment *is* the OCC deployment. The package's S18-02/S18-03 negatives should
be scoped as *"no field-level or data-level override; method-level override unverified for
10 of 16 custom modules."*

---

## 6. SECONDARY — P2P functional semantics

### A-18 · Every published figure reproduces to the digit
```
$ python3 c1.py / c4.py
PO currency_id distinct: {133: 13887}   PO currency_rate distinct: {1.0: 13887}
POL discount non-zero: 0                POL display_type: {None: 20296, line_note: 806}
RNI lines: 1580   sum((qty_received - qty_invoiced) * price_unit) = 30080689.7776
  by company: co1 15258362.0124 / co2 14822327.7652
invoiced-not-received: 183 lines, 1734752.87
done purchase-linked moves 3124 → 1403 carry ≥1 SVL (2146 layers), sum(value) = 22953527.29
  account_move_id non-null among them: 0
  POSITIVE CONTROL sum(value) over all 47,801 SVL = 89720002.01
```
Currency risk is nil (single currency, rate 1.0) and discount risk is nil (uniformly zero).
Both are ruled out by enumeration, not assumption.

### A-19 · CHALLENGED — the headline ฿30,080,689.78 is **not** "gross pre-tax"
```
$ python3 c2.py
lines where price_subtotal != product_qty * price_unit (tol 0.05): 312
  their total by price_unit:       16068680.39
  their total pro-rata subtotal:   15017458.279  (sum of 312 per-line pro-rata terms)
$ python3 c3.py
ratio (product_qty*price_unit)/price_subtotal: [('1.0000', 1267), ('1.0700', 312), ('st0', 1)]
Taxes on the 312 MISMATCHED lines:
   191 lines -> [('PV7% (รวม VAT / VAT included)', '7.0000', 'tax_included', 'purchase', co1)]
   121 lines -> [('PV7% (รวม VAT / VAT included)', '7.0000', 'tax_included', 'purchase', co2)]
Taxes on the MATCHING lines:
   558 co1 + 547 co2 -> [('7%', '7.0000', None, 'purchase')]   159 -> no tax
     4 -> [('Undue PV7% (ไม่รวม VAT / VAT excluded)', 'tax_excluded')]
```
312 of the 1,580 lines carry a tax with `price_include_override = 'tax_included'`. On those
lines `price_unit` is **VAT-inclusive**, and the ratio is exactly 1.0700 on all 312 and
exactly 1.0000 on the other 1,267 — the diagnosis is identified, not inferred.

Summing `price_unit` across both groups mixes tax bases. The consistent tax-exclusive
exposure is:
```
PUBLISHED basis   co1 15,258,362.01  co2 14,822,327.77  TOTAL ฿30,080,689.78
TAX-EXCLUSIVE     co1 14,692,566.42  co2 14,336,901.24  TOTAL ฿29,029,467.66
OVERSTATEMENT                                                  ฿ 1,051,222.12  (3.49% of the published figure)
```
The same defect applies to the counter-figure: invoiced-not-received ฿1,734,752.87 →
tax-exclusive **฿1,663,518.07**.

Note the *label* is wrong in both directions depending on intent. If the intended measure
is the GRNI accrual, tax-exclusive (฿29,029,467.66) is correct — VAT on a purchase is not
accrued to inventory. If the intended measure is cash exposure to vendors, tax-inclusive is
correct, but then all 1,580 lines must be grossed up, giving ฿30,962,543.77
(pro-rata of `price_total`), not ฿30,080,689.78. **The published number is neither**; it is
1,267 lines on one basis plus 312 on the other.

### A-20 · CHALLENGED — 169 lines of the "exposure" have no receipt document at all
```
$ python3 c2.py
RNI lines by qty_received_method: {'stock_moves': 1411, 'manual': 169}
  MANUAL exposure:      1,539,880.31  (169 lines)
  STOCK_MOVES exposure: 28,540,809.47 (1,411 lines)
RNI lines by product type: consu/storable 1403 | service 169 | consu/non-storable 8
  exposure by type: storable 28,455,002.22 | service 1,539,880.31 | non-storable consu 85,807.25
```
The 169 `manual` lines are exactly the 169 **service** lines. `qty_received` there is a
number an operator typed, not a goods receipt: no picking, no stock move, no valuation
layer, no GRNI. A three-way match (PO / receipt / invoice) has only **two** legs on those
lines. They are ฿1,539,880.31 (5.1%) of the published exposure and should be reported
separately, not summed into a received-not-invoiced figure. A further 8 non-storable
`consu` lines (฿85,807.25) can likewise never produce a valuation layer.

### A-21 · RISKY — 18 over-received lines carry ฿1,707,560.30
```
over-receipt lines (qty_received > product_qty): 18   exposure: 1,707,560.30
```
5.7% of the exposure sits on lines where more was received than ordered. Not an arithmetic
error, but it is a distinct control condition that the single aggregate hides.

### A-22 · The three-way-match reading is sound in direction, understated in one place
`0 of 1,403` purchase-linked SVL-bearing moves posting a journal entry reproduces exactly,
and I confirm ฿22,953,527.29. Two qualifications the package should carry:
1. That ฿22.95M and the ฿30.08M are **different measures** — the first is layer value at
   receipt cost, the second is PO price on the un-invoiced quantity. They are not two views
   of one number and should not be read as reconcilable.
2. Per A-15, only 1,403 of 3,124 done purchase-linked moves have a layer at all, so the
   ฿22.95M is a floor on receipt value, not a measure of it.

The **substantive** three-way-match conclusion — that goods receipts create no GRNI entry
and no accrual exists — I could not break. S18-05's execution test reproduces in spirit:
inventory reaches the GL only through migration journal 45.

---

## 7. Statement of position

### SUPPORTED
- **S18-02 in full.** Every product in all four companies resolves to `manual_periodic`.
  I reproduced both storage locations independently, re-derived the ORM resolution from
  `models.py:2995-3013` / `fields.py:785` / `ir_default.py:153-182`, and added a third test
  the package did not run (module attribution via `ir_model_data`, positive control 718
  custom field xmlids) which also comes back clean. The deployed selection values carry no
  third option.
- **W1–W5: five of the six core writers of `account_move_id` are periodic-gated.** The
  package named one; I verified five. Its conclusion for those is right and better
  supported than it published.
- **The zero-link count itself.** 0 of 47,801 on both columns, re-extracted and re-parsed
  from the archive. Strongest positive control available: `stock_valuation_layer_id` is
  non-null on **2** rows out of 47,801 in the same parse — an adjacent nullable many2one
  read at a density of 0.004%. A parser blind to sparse values could not have produced that.
- **Every P2P count and sum in S18-07**, to the digit, including ฿30,080,689.78,
  ฿1,734,752.87 and ฿22,953,527.29.
- **A-10, new:** no `stock_location` supplies a valuation account (0/86, controlled), so
  under a `real_time` counterfactual the unconfigured categories would have *raised*, not
  silently produced nulls. This is the argument that rules out "it would have been zero
  anyway" on the main path, and the package does not currently make it.

### MISSING
- The package's writer enumeration. It published one mechanism where six exist (A-05).
- Any scoping of the negative to **method-level** override. `ir_model_data` bounds field,
  model, view and data extension only; ten of sixteen custom modules have no
  version-matching source, so a Python override of `_validate_accounting_entries`,
  `_account_entry_move` or `AccountMove._post` is unverifiable here (A-17).
- The purchase-linked sub-population inside the discriminating set: 61 rows, not 1,812
  (A-14). The receipt-to-GRNI claim rests on those 61.
- Separation of the ฿30.08M into its receipt-backed and typed-quantity halves (A-20).

### RISKY
- **A-15.** The SVL table is not consistent with the product master in either direction:
  1,089 layers on non-storable products, and 1,480 done storable purchase receipts with no
  layer. Inferences drawn across the whole 47,801 inherit that inconsistency.
- **A-11.** `create_date` is back-dated on 44,947 rows. Any downstream work that treats it
  as provenance will be wrong.
- **A-21.** ฿1,707,560.30 of the exposure is on over-received lines.
- The `_post` filter `l.product_id.cost_method != 'standard'`
  (`purchase_stock/models/account_invoice.py:126`) reads a company-dependent field in
  `self.env`'s company, which at post time is the *user's* active company, not necessarily
  the invoice's. In a four-company database that is a latent correctness issue in its own
  right. I did not pursue it; it is out of my scope but should not be lost.

### CHALLENGED
1. **A-05 / A-06 — "periodic policy explains the 0-of-47,801" is sufficient but NOT
   identified.** `_prepare_pdiff_svl_vals` writes both link columns and is gated on
   `cost_method`, not `valuation`. The precondition holds here (18 categories at `average`
   for company 1), the path was reached by 18 posted vendor-bill lines, 16 of them with a
   real price difference, and it produced nothing — because every impacted layer had
   `remaining_qty = 0`, a condition periodic policy does not control. **The 0 on
   `account_move_line_id` is not explained by periodic policy at all.**
2. **A-09 — the zero is over-determined for 4,574 of 47,801 layers (9.57%)** by three
   valuation-independent silent skips: no stock move (2,866), zero value (1,205),
   non-storable product (1,089). The verdict should be scoped to the 43,227 remainder.
3. **A-11 / A-12 — the "1,812 native layers" discriminating set does not discriminate.**
   Every row in the table was written in one five-day window (98.8% on one day); 1,254 of
   the 1,812 are `__system__` inventory adjustments from that same window. The defensible
   set is **558** (two independent classifiers converge at 558/559), and the
   over-determination-free core is **541**. The conclusion survives; the denominator is
   overstated 3.2x.
4. **A-19 — ฿30,080,689.78 is not "gross pre-tax."** 312 of 1,580 lines carry
   `price_include_override = 'tax_included'` at exactly 1.0700. Tax-exclusive:
   **฿29,029,467.66** (co1 14,692,566.42 / co2 14,336,901.24). Overstatement
   **฿1,051,222.12 — 3.49% of the published figure**. Same defect on the ฿1,734,752.87 counter-figure
   (→ ฿1,663,518.07).
5. **A-20 — 169 lines (฿1,539,880.31) are service products with a typed `qty_received`.**
   No receipt document exists; a three-way match has two legs there. They do not belong in
   a received-not-invoiced aggregate.

### Where I could not break it, and the residual doubt
I attacked Route 1 four ways — jsonb, `ir_default` (full 54-row enumeration, not a
filtered search), deployed field metadata, and module attribution with a firing positive
control — and it held every time. I attacked the writer enumeration and found one
ungated writer, then measured its reachability rather than stopping at naming it. I tried
to make the zero over-determined and succeeded for 9.57% of the population but **not** for
the 43,227-row remainder, and A-10 shows the `real_time` counterfactual is incoherent for
the unconfigured categories rather than silently zero.

The residual doubt is concentrated in one place: **A-17**. Ten of sixteen custom modules
have no readable source at the deployed version, and no database artefact records a Python
method override. I cannot exclude that one of them overrides
`_validate_accounting_entries`, `_account_entry_move` or `AccountMove._post`. Everything I
can test says no; the thing I cannot test is exactly the thing that would falsify the
claim.

Second residual: A-06's `remaining_qty = 0` reading uses the **dump-time** value.
`remaining_qty` is mutated by consumption after a layer is created. If any of those 16
layers had `remaining_qty > 0` at the moment its bill was posted, `qty_to_correct` would
have been non-zero and a linked SVL **should** exist — and none does. I cannot resolve
which held from a single snapshot. Either way A-05 stands (the writer is not
valuation-gated); what is unresolved is whether the observed zero on those 16 is explained
by `remaining_qty = 0` or by the path not executing.

### EVIDENCE REQUIRED NEXT
1. **Source for the 10 custom modules at their deployed versions** — particularly
   `scgl_account_coa_control 18.0.1.0.1` — then grep for
   `_validate_accounting_entries|_account_entry_move|_prepare_account_move_vals|def _post|property_valuation|_apply_price_difference`.
   Until then S18-02/S18-03 carry an unbounded method-override gap.
2. **`mail_tracking_value` / `mail_message` on `product.category`** — did `property_valuation`
   or `property_cost_method` ever change? `property_cost_method` has `tracking=True`
   (`stock_account/models/product.py:929`), `property_valuation` does not. Tracking rows
   would settle whether the deployment was ever `real_time`, which no current-state read can.
3. **A time-series for `remaining_qty`** on the 16 layers in A-06 — or the account move of
   the corresponding bills — to decide the second residual doubt.
4. **The loader that wrote the SVL table on 2026-08-25.** A-15 says it did not follow v18
   valuation semantics. Its script or spec would explain 1,089 layers on non-storable
   products and 1,480 storable receipts with none, and would tell us how much of the
   47,801 can bear any behavioural inference at all.
5. **Restatement of S18-07** on a declared tax basis, with the service/manual lines and the
   over-received lines broken out rather than summed.
