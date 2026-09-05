# EXPERT_1 — AAS-03 Leader Functional Design
## Adversarial challenge of the frozen P01 SERIES-16 findings brief
Read-only. No database written, no source modified, no Odoo server run, no external network.

---

## 0. DECLARED BOUNDS

**POPULATION.** The single deployment archive `~/Downloads/iSMEs_2026-07-11_05-03-27.dump`
(CUSTOM 1.14, dbname `iSMEs`, 651 `TABLE DATA` entries, one company
`บริษัท ข้าวสุวรรณภูมิ จำกัด`). Every count below is over the **whole** table named, never a
sample, unless a filter is stated in the line itself.

**PATTERN.** Extraction: `/opt/homebrew/opt/postgresql@18/bin/pg_restore -t <table> --data-only -f T_<table>.sql ~/Downloads/iSMEs_2026-07-11_05-03-27.dump`.
Parse: `s16/pgc.py::load` (whole-table into memory) or `s16/stream.py::stream` (row generator,
written this session for the 206 MB `account_move_line` and 92 MB `account_move`). Both parse the
`COPY public.<t> (...) FROM stdin;` block, split on TAB, map `\N`→None. Arithmetic in
`decimal.Decimal`, never float.

**PATH SET — evidence at rest.** 13 tables were already extracted in `s16/`. I extracted 16 more
from the same archive this session: `stock_location, stock_rule, stock_warehouse, stock_scrap,
mrp_bom, mrp_bom_line, product_supplierinfo, stock_return_picking, stock_return_picking_line,
account_tax, purchase_request_line, hr_expense, hr_expense_sheet, mrp_production,
account_analytic_line, stock_move_line`. **Bound I did not test:** I did not sweep `$HOME` or
`/Volumes` for other database artefacts. Every claim below is scoped to this one archive; none of
them is a claim about the SWR estate as a whole.

**PATH SET — source.** `/Users/admin/Library/CloudStorage/GoogleDrive-…/16 ODOO 16 ENTERPRISE/odoo-16.0+e.20230401/odoo/addons`
(the version-ranked winner, 144/144). Files read this session: `purchase/models/purchase.py`,
`purchase/models/account_invoice.py`, `purchase_stock/models/purchase.py`,
`purchase_stock/models/stock_move.py`, `purchase_stock/models/account_invoice.py`,
`purchase_price_diff/models/account_move_line.py`, `purchase_price_diff/__manifest__.py`,
`stock_account/models/account_move.py`, `stock_account/models/stock_move.py`,
`stock_account/models/product.py`, `account_reports/models/account_report.py`,
`account/models/account_move_line.py`.

**UNIT.** Declared per claim. The units used are: *journal item* (`account_move_line` row),
*journal entry* (`account_move` row), *PO line* (`purchase_order_line` row), *stock move*
(`stock_move` row), *valuation layer* (`stock_valuation_layer` row), *payment*
(`account_payment` row), *WHT certificate* (`withholding_tax_cert` row), *product category*
(`product_category` row). Where the brief and I differ on the unit, I say so.

**Verified method premise (shared with the brief).** `stock_account/models/product.py:15-16` and
`:106-107` define `valuation` and `cost_method` on **both** `product.template` and
`product.product` as `fields.Selection(related="categ_id.property_valuation", readonly=True)` /
`related="categ_id.property_cost_method"`. There is therefore **no** per-product override
population; the product→template→category join is the only correct route, and the brief's
correction #4 is right. I re-ran it with the same coverage control and got **0 of 74,982
unresolved**, and the identical 2×2 (`real_time` 56,654 / 1,044; `manual_periodic` 1,209 /
16,075). The brief's corrected method reproduces exactly.

---

## 1. WHAT REPRODUCES

Before challenging, I re-derived the brief's load-bearing numbers from the archive. These all
reproduce to the digit and I do not dispute them as arithmetic:

| brief claim | my recomputation | unit |
|---|---|---|
| `purchase_order_line` 10,490 | 10,490 | PO line |
| Received-not-invoiced 79 lines / ฿12,678,776.50 | 79 / `12678776.50200000` | PO line |
| Invoiced-not-received 49 lines | 49 | PO line |
| Account 39: 13,736 items, Dr 6,558,441,923.88 / Cr 6,486,344,109.63 / net 72,097,814.25 | identical | journal item |
| bill lines debiting 39: 6,653 / ฿4,516,394,611.47 Dr / ฿0.00 Cr | 6,653 (6,595 posted + 41 cancel + 17 draft) / identical | journal item |
| SVL 74,982 rows, 57,863 with `account_move_id` | identical | valuation layer |
| 30 layers with `|value| > 1e12`; rest sum ฿400,338,755.98 | 30; 74,952 rows sum `400338755.98` | valuation layer |
| Residual A 296, Residual B 1,209 | identical | valuation layer |
| 30 moves dated year 2567 | identical | journal entry |

The arithmetic is sound. **Every finding below is about the interpretation attached to these
numbers, or about a population the brief did not open.**

---

## 2. MANDATORY DISPROOF 1 — the 296 and the 1,209

**Task:** find a legitimate mechanism that produces either residual.
**Result: both residuals are largely disproved as anomalies. The brief's own refutation of the
policy-change explanation is also disproved.**

### 2.1 Residual B (1,209 `manual_periodic` layers that carry a journal entry) — 1,172 explained

The brief treats `account_move_id` on a periodic layer as evidence of a valuation posting. It is
not. `stock_account/models/account_move.py:371-390`, `_prepare_in_invoice_svl_vals`, writes:

```
'account_move_id': self.move_id.id,
'account_move_line_id': self.id,
```

i.e. the **vendor bill's own id**, as a back-reference on a price-difference correction layer.
Its caller, `AccountMove._post` at `:44-61`, is gated only on
`move_type in ('in_invoice','in_refund','in_receipt')` **and** `product_id.cost_method != 'standard'`.
It is **not** gated on `valuation == 'real_time'`, and it is **not** gated on
`anglo_saxon_accounting`.

Measurement (unit: valuation layer; population: all 1,209 Residual-B layers; the `account_move_id`
resolved against the whole `account_move` table):

```
Residual B: account_move move_type/journal:
  Counter({('in_invoice','2'): 1172, ('entry','8'): 37})
Residual B: of the 1194 without stock_move_id, move_type:
  Counter({'in_invoice': 1172, 'entry': 22})
```

**1,172 of 1,209 (96.9%) point at a vendor bill in the AP journal, not at a valuation entry.**
Categories 24, 25, 26, 27, 29, 30, 15, 33 are all `manual_periodic` with `cost_method` fifo or
average, so they qualify for that path by design. This is documented reference-ERP behaviour, not
an anomaly.

Positive control that the query could have returned valuation entries: the same join over the
`real_time`-linked layers returns `[(('entry','8'), 56651), (('in_invoice','2'), 3)]` — the
predicate distinguishes the two shapes.

Of the remaining 37: 22 carry no stock move and are the `Due to a change of product category`
(12) and `Costing method change for product category` (9) layers — created by a category write
while the product was still in a `real_time` category, then reclassified by the current-state
join. **15** are `WH/IN/…` receipts of แม่พิมพ์ (moulds), all in category 15.

### 2.2 The brief's refutation of the policy-change explanation does not hold

The brief writes: *"Policy-change was tested as the explanation and REFUTED … all 15 `real_time`
`ir_property` rows were written 2023-09-15..2023-12-08."*

That test reads only the `property_valuation` rows **that still exist**. An `ir_property` row is
deleted when a value is reset to the company default; the surviving rows cannot bound when policy
changed. The sibling field carries the trace the deleted row did not:

```
res    value            field                create_date            write_date
15     average          property_cost_method 2023-09-22 07:26:17   2025-01-21 06:52:06
```

Category 15's `property_cost_method` row was created **inside** the 2023-09-22 07:18–07:35
configuration session in which categories 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19 and 22 each
received **both** a `property_cost_method` row **and** a `property_valuation = real_time` row.
Category 15 has the cost-method row from that session and **no** `property_valuation` row at all —
and its cost-method row was **modified on 2025-01-21**, seventeen months outside the brief's stated
window.

Discriminating measurement (unit: valuation layer; population: all 191 SVL rows for category 15):

```
SVL rows for category 15: 191   with account_move_id: 22
  LINKED create_date range: 2024-01-27 .. 2025-01-21 06:52:06
  LINKED after 2025-01-21: 0
  2025-01  linked=10  unlinked=24
  2025-02 .. 2026-07: linked=0 across 18 months and 84 unlinked layers
```

The last linked layer is timestamped `2025-01-21 06:52:06` — **the same second as the
`property_cost_method` write**. Zero linked layers in the following eighteen months. The
never-transacted-after row is the informative one here: it is a clean structural break, not a
proportional spread. Positive control: the same query over all categories returns 56,654 linked
`real_time` layers spread across the whole period, so "0 linked after 2025-01-21" is not an
instrument failure.

**Conclusion on Residual B: at most 15 of 1,209 remain unexplained, and those 15 are the strongest
evidence *for* the policy-change hypothesis the brief declared refuted.**

### 2.3 Residual A (296 `real_time` layers, non-zero value, no journal entry) — 245 explained

`stock_account/models/stock_move.py:546-548`:

```
if self.product_id.type != 'product':
    # no stock valuation for consumable products
    return am_vals
```

Measurement (unit: valuation layer; population: all 296; product type read from
`product_template.type` via `product_product.product_tmpl_id`):

```
product.type distribution: Counter({'consu': 245, 'product': 51})
```

**245 of 296 (82.8%) are consumable products.** A consumable in a `real_time` category still gets
a valuation layer and can never get a journal entry. That is an explicit early return in the
reference ERP, and it is exactly what the data shows.

Of the 51 storable ones, the descriptions and move geometry decompose them further:
11 `Due to a change of product category`, 9 `Product value manually modified` (revaluation
wizard), 3 `Quantity Updated` inventory adjustments, the rest `UB/…` unbuild and `WH/MO/…`
manufacturing consumption. **A genuine residual of roughly 25–30 storable layers survives** and I
do not claim it is explained.

Two negatives with positive controls, on the same 296:
- `restrict_partner_id` (owner-restricted / consignment stock, the `_account_entry_move` early
  return at `:550-552`) is set on **0 of 296**. Positive control: `restrict_partner_id` is set on
  **1** stock move in the whole 103,949-row table, so the predicate can fire but the population is
  effectively empty. **Consignment does not explain Residual A, and consignment is not a live
  business state in this deployment.**
- `is_inventory='t'` on 6 of 296 and `scrapped='t'` on 9 of 296. Positive controls: 3,010 and
  2,295 respectively across the whole table.

### 2.4 Verdict on Disproof 1

**CHALLENGED — largely disproved.** The brief's headline "296 / 1,209 anomalies" is an artefact of
(a) reading a bill back-reference field as a valuation posting, and (b) joining historical layers
to current-state category configuration. A defensible restatement is **"≈15 + ≈25–30 layers
unexplained"**, roughly 2.7% of the 1,505 the brief reports, and the 15 point at a category-15
policy change on 2025-01-21 rather than at a posting defect.

---

## 3. MANDATORY DISPROOF 2 — `4310005 Purchase price variance` with 0 items

**Task:** disprove that 0 items means the price-difference engine never fired; find any other
account or path carrying purchase price differences.
**Result: fully disproved on both halves. The account-1173 engine is structurally unreachable in
this deployment, and a different price-difference engine fired 1,123 times.**

### 3.1 Why account 1173 could never receive an item

Two independent gates, both closed:

**Gate 1 — company setting.** `purchase_stock/models/account_invoice.py:35`:

```
if move.move_type not in ('in_invoice','in_refund','in_receipt') or not move.company_id.anglo_saxon_accounting:
    continue
```

`_stock_account_prepare_anglo_saxon_in_lines_vals` is the **only** caller of
`account.move.line._get_price_diff_account()`. The brief's own S16-01 records
`anglo_saxon_accounting = FALSE`. The method therefore returns `[]` for every one of the 37,055
vendor bills, unconditionally.

**Gate 2 — cost method.** Even with gate 1 open, `purchase_price_diff/models/account_move_line.py`
routes to `property_account_creditor_price_difference[_categ]` **only** when
`self.product_id.cost_method == 'standard'`:

```
def _get_price_diff_account(self):
    if self.product_id.cost_method == 'standard':
        ... return debit_pdiff_account
    return super()._get_price_diff_account()
```

The single configured `property_account_creditor_price_difference_categ` row is on **category 10**
(`All / Expenses / Material / Rice`), whose `property_cost_method` is **`fifo`**, not `standard`.
Even with anglo-saxon on, that configuration could not reach account 1173.

**So `1173 = 0 items` is the only possible outcome. It is a latent configuration, not a
non-firing engine, and it is not evidence of a control failure.** The brief's sentence *"The
price-difference engine is wired and has never fired in 183,590 journal entries"* is literally
true and materially misleading: it invites a reader to treat a correct zero as a defect.

### 3.2 The price-difference path that IS in use

`stock_account/models/account_move.py:44-69` runs a **second, different** price-difference engine
on every vendor bill post, and it is gated **only** on `cost_method != 'standard'`:

```
if invoice.move_type in ('in_invoice','in_refund','in_receipt'):
    valued_lines |= invoice.invoice_line_ids.filtered(lambda l: l.product_id and l.product_id.cost_method != 'standard')
if valued_lines:
    stock_valuation_layers |= valued_lines._create_in_invoice_svl()
...
if stock_valuation_layers:
    stock_valuation_layers._validate_accounting_entries()
```

It writes the difference to `stock_valuation_layer.price_diff_value` and posts through the stock
journal against the valuation and stock-input accounts. Measurement (unit: valuation layer;
population: all 74,982):

```
price_diff_value non-null:  1267
price_diff_value != 0    :  1123
sum price_diff_value     :  2246313274.64
abs sum price_diff_value :  2247191737.24
median |price_diff_value|:  28.79    max |price_diff_value|: 949239810
with account_move_id: 1123   with account_move_line_id: 1123   with parent layer: 1123   with stock_move_id: 0
```

**The price-difference engine fired 1,123 times for a gross ฿2,246,313,274.64.** It routed
nowhere near account 1173.

### 3.3 The third path: account 39 is itself the price-difference sink

`anglo_saxon_accounting = FALSE`, yet 6,595 **posted** vendor-bill items debit account 39
(`2900000 Goods Receipt Note(GRN)`, `liability_current`). No stock module put them there. The
configuration did:

```
product.category.property_account_expense_categ_id:
  GLOBAL -> 22 (411000 Cost of Revenue)
  cat 5,6,8,9,10,11,12,13,14,16,17,18,19,22,32,34  -> 39 (2900000 Goods Receipt Note(GRN))   [16 categories]
product.category.property_stock_account_input_categ_id:
  cat 8,9,10,12,13,14,16,17,18,19,32 -> 39                                                   [11 categories]
  cat 6 -> 1156, cat 11 -> 1160, cat 22 -> 1160, cat 34 -> 1161  [expense accounts as stock input]
```

**Sixteen product categories have their *Expense Account* pointed at the GRN liability account.**
The vendor bill therefore debits GRN because GRN is configured as the expense account, and the
real-time receipt credits GRN because GRN is configured as the stock-input account. This is a
hand-built imitation of anglo-saxon accounting assembled out of two unrelated configuration
fields. Its consequences:

- purchase cost for those sixteen categories **never enters the income statement from the bill**;
- there is no engine anywhere that computes the bill-vs-receipt difference for them, so the
  difference simply **remains in account 39** as an unlabelled residual;
- four categories (6, 11, 22, 34) credit a **consumption expense account** on goods receipt.

**The path carrying purchase price differences in this deployment is account 39 itself, cleared
manually — see §4.**

### 3.4 Verdict on Disproof 2

**CHALLENGED — disproved.** `1173 = 0` is correct-by-construction; the operative price-difference
mechanisms are `stock_valuation_layer.price_diff_value` (1,123 firings, ฿2.25bn gross) and the
unengineered residual in account 39.

---

## 4. THE ฿72,097,814.25 IS NOT AN UNCLEARED POSITION

The brief calls account 39's net *"฿72,097,814.25 outstanding"*. Four separate measurements say it
is not a position at all.

### 4.1 It is not a balance any Odoo report in this system can produce

Split by move state (unit: journal item; population: all 13,736 items on account 39):

```
posted   items=13666  Dr=6383424831.18  Cr=6390473523.26  NET=  -7048692.08
cancel   items=   53  Dr= 172292940.50  Cr=  95870586.37  NET=  76422354.13
draft    items=   17  Dr=   2724152.20  Cr=         0.00  NET=   2724152.20
                                                          sum =  72097814.25
```

`account_reports/models/account_report.py:710-714`:

```
def _get_options_all_entries_domain(self, options):
    if not options.get('all_entries'):
        return [('parent_state','=','posted')]
    else:
        return [('parent_state','!=','cancel')]
```

**No option in any Odoo financial report ever includes `parent_state='cancel'`.** The brief's
figure is dominated by 53 **cancelled** journal items worth ฿76,422,354.13 — 106% of the number it
reports. The posted balance is **−฿7,048,692.08**, a *debit* balance on a current-liability
account, i.e. the **opposite sign** from the reading the brief attaches to it.

### 4.2 The account is not reconcilable, so no item-level "uncleared" set exists

```
account 39: {'code':'2900000','name':'Goods Receipt Note(GRN)','account_type':'liability_current','reconcile':'f'}
```

Positive control: 29 of the 339 accounts carry `reconcile='t'` (ids 1, 2, 31, 32, 33, 1071, 1072,
1117, 1118, 1119, 1120 …). Account 39 is not among them. **There is no receipt-to-bill matching in
the ledger.** The ฿72m (or the −฿7m) is a bare arithmetic net of streams that were never matched
and cannot be matched. "Uncleared" is not measurable on this account as configured.

### 4.3 The balance is manually driven to zero, repeatedly

Posted running balance by period (unit: journal item; population: all posted items on account 39):

```
2023-09  ->        0.00      2024-09  ->        0.00      2025-09  ->        0.00
2025-05  ->        0.00      2025-12  ->        0.00
```

Five clean returns to exactly ฿0.00. The instrument: 39 journal items in **journal 3 (MISC)**,
Dr ฿17,431,612.34 / Cr ฿1,895,367,654.71, **net −฿1,877,936,042.37** — twenty-six times the
"outstanding" figure — with refs reading `ปรับปรุงบัญชี 2900000 Goods Re…` ("adjust account
2900000 Goods Receipt Note"), `ปรับปรุงบัญชี 4010008 Consumpt…`, `ปรับปรุงรายการ GRN` ("adjust GRN
entries") and `ปรับปรุงยอดยกมางบการเงิน ปี256…` ("adjust financial-statement opening balance year
256x", ฿274,297,054.03 on 2023-09-30). Monthly, 2023-09 through 2024-03, then intermittently.

**The GRNI account is a manually maintained suspense account, swept by month-end journal entries.**
Its net at any date is the residue after the last sweep, not an exposure.

### 4.4 The account is fed by four streams, three of which cannot clear

By move type and journal (unit: journal item; all states; population: all 13,736):

```
('entry','8')      Dr 2024615700.07  Cr 4574484541.58  net -2549868841.51   [stock journal]
('in_invoice','2') Dr 4516394611.47  Cr          0.00  net  4516394611.47   [vendor bills]
('entry','3')      Dr   17431612.34  Cr 1895367654.71  net -1877936042.37   [manual MISC]
('in_refund','2')  Dr          0.00  Cr   16491913.34  net   -16491913.34   [vendor refunds]
```

Two structurally unmatchable legs, each larger than the reported net:

**(a) Non-PO vendor bills debiting GRNI.** 298 posted items, **net ฿269,689,658.68**, on bills that
carry no `purchase_line_id` on any line — so no receipt exists to credit them, ever. That is 3.7×
the reported "outstanding".

**(b) Vendor returns debiting GRNI.** The 99 done vendor-return stock moves generate 83 journal
entries whose whole account footprint is:

```
acct 1062 Raw material               83 items  Dr          0.00  Cr 129185824.89
acct 39   Goods Receipt Note(GRN)    82 items  Dr 129086326.14  Cr         0.00
acct 1156 Consumption of raw mat.     1 item   Dr     99498.75  Cr         0.00
```

Vendor returns **debit** GRNI ฿129,086,326.14. Vendor refunds credit it only ฿16,491,913.34 (all
states) / ฿10,972,540.12 (posted, PO-linked). The return leg alone leaves ≈฿112.6m–118.1m of
unmatched **debit** — 1.6× the brief's entire reported net, and of the wrong sign for a GRNI
liability.

### 4.5 Verdict

**CHALLENGED.** ฿72,097,814.25 is (i) state-contaminated, (ii) computed on a non-reconcilable
account, (iii) the residue of a manual monthly sweep of ฿1.9bn, and (iv) smaller than at least two
individual unmatchable legs feeding it. It is neither "uncleared", nor "timing", nor "rounding" —
it is **the current reading of a manually maintained suspense account**. The number should be
withdrawn from the brief in the form it is stated, and replaced with the posted balance
(−฿7,048,692.08) plus the four-stream decomposition.

---

## 5. IS 79 RECEIVED-NOT-INVOICED CREDIBLE FOR A PADDY MILLER?

### 5.1 `qty_received` is faithfully maintained — the 79 is not a stale-field artefact

I re-derived `qty_received` from `stock_move` for every `state='purchase'`, `qty_received_method='stock_moves'`
PO line, implementing `purchase_stock/models/purchase.py:314-334` (done moves only; product must
match the line; `_is_purchase_return()` with `to_refund` subtracts):

```
stock_moves+purchase lines: 9522     lines with NO linked stock move at all: 6
DISAGREEMENTS stored vs recomputed: 27
  line 1083 stored 4704.000000 recomputed 196.000000   (factor 24)
  line 4778 stored 9408.000000 recomputed 392.000000   (factor 24)
  ...
```

All 27 disagreements are exactly factor 24 and coincide with the 52 moves whose `product_uom`
differs from the line's `product_uom` — a UoM conversion my re-derivation deliberately omitted.
**`qty_received` is not stale. The brief is right on this specific point and I could not break it.**

### 5.2 But the field is manual on 746 lines and the method is per-line

```
qty_received_method: Counter({'stock_moves': 9686, 'manual': 746, None: 58})
qty_received_manual NOT NULL: 5079   nonzero: 628
```

`purchase/models/purchase.py:1054-1060` sets `manual` for `consu`/`service` products;
`purchase_stock/models/purchase.py:300-304` overrides to `stock_moves` for `consu`/`product`.
**746 PO lines (7.1%) have a received quantity that is whatever a user typed, with no stock move
behind it**, and 628 of those carry a non-zero manual value. Five of the 79 received-not-invoiced
lines are of this kind. The brief reports the 79 without saying that a fourteenth of the
denominator is unverifiable by construction.

### 5.3 The 79 is a snapshot, and it is the wrong instrument for the question

The count is a point-in-time open exposure on 30 June/11 July 2026, not a measure of how well
receipts and bills match over three years. The three-year matching quality is what §4.4 measures,
and it is poor. A better companion statistic from the same population:

```
state=purchase lines: 10265
  qty_received == qty_invoiced : 10137   (of which 254 are both zero with product_qty > 0)
  qty_received  >  qty_invoiced:    79
  qty_invoiced  >  qty_received:    49
```

254 confirmed PO lines have ordered quantity and **zero** received and **zero** invoiced. That is a
larger open-commitment population than the 79 and the brief does not name it.

### 5.4 The 49 invoiced-not-received lines are not benign — they are the trigger for S16-04

See §7. The brief lists 79 and 49 side by side as symmetric timing statistics. They are not
symmetric: `qty_invoiced > qty_received` is the **entry condition to a division in the reference
ERP that has no zero-guard**, and it is the proximate cause of the 15-order-of-magnitude
divergence the brief reports separately in S16-04.

### 5.5 Verdict

**PARTLY SUPPORTED, MISLEADINGLY FRAMED.** The 79 is correctly computed and `qty_received` is
correctly maintained. It is not credible as a *characterisation of GRNI health* for a paddy miller,
because in this deployment the GRNI account is not driven by the PO line at all (§4.4): 73% of
vendor bills never touch a PO line, and the account is swept manually. The 79 measures the PO
module's own bookkeeping, not the business's received-not-invoiced position.

---

## 6. BUSINESS STATES THE BRIEF DOES NOT NAME

Unit: as stated per row. Population: the whole named table.

| state | measurement | in brief? |
|---|---|---|
| **Vendor bills with no purchase order** | **27,089 of 37,055 in_invoice moves (73.1%) carry no `purchase_line_id` on any line**; 26,989 of them posted, ฿472,011,748.05 of ฿4,609,967,957.41 posted bill value (10.24%) | **no** |
| **Export logistics as the dominant bill stream** | Non-PO posted bill items: 1117 `Accounting Payable-Import&Export` 21,732 items; 1278 `Shipping Cost - Oversea` 15,792; 1205 `Cost of issuing BL documents` 3,614; 1206 `marine insurance` 3,354; 1207 `certification service fee` 2,768; 1204 `Seafreight Charge` 451 items ฿225,537,516.55 | **no** |
| **Multiple AP control accounts** | vendor bills settle to at least 10, 1113 `Accounting Payable-Rice`, 1115 `-Packaging`, 1117 `-Import&Export`, 1118 `-Rent`, 1119 `-Under the contract`, 1120 `Outstanding Check`, 1282 `-Domestic`; driven by 1,715 `res.partner.property_account_payable_id` `ir_property` rows | **no** ("payable 37,054" by `account_type` conflates them) |
| **Purchase requisition stage** | `purchase_request` 2,163 (approved 2,147 / draft 7 / rejected 5 / to_approve 4); `purchase_request_line` 5,175; `stock_move.created_purchase_request_line_id` exists | named as a module only |
| **Vendor returns** | 123 purchase-linked stock moves internal→supplier (99 done, 19 cancel), 121 with `to_refund='t'`, over 86 distinct PO lines, 2023-10-06..2026-06-15; plus 5 out-to-supplier moves with **no** `purchase_line_id` | **no** |
| **A dedicated "Returns" operation type** | `stock_picking_type` id 6, `code=incoming`, name `Returns`, 94 pickings (75 done / 17 cancel / 2 waiting), origins `Return of WH/OUT/…` and one `Return of WH/RET/…` (a return of a return) | **no** |
| **Purchase down payments / vendor advances** | 137 PO lines `is_downpayment='t'`, all `state='purchase'`, **`price_subtotal` total ฿0.00**, `qty_received` total 0, `qty_invoiced` total 18; 60 journal items `is_downpayment='t'` on accounts 1102/1073/1077/1214/1240/1241/1207. Module `scgl_purchase_advance_payment 16.0.1.0.0` installed | **no** |
| **Scrap** | `stock_scrap` 2,286 (2,277 done); 2,295 stock moves `scrapped='t'` | **no** |
| **Inventory adjustments** | 3,010 stock moves `is_inventory='t'` | **no** |
| **Manufacturing consumption** | `mrp_production` 10,764 (9,807 done); picking types `Pick Components`, `Store Finished Product`, `PRODUCTION IN PROCESS`, `Manufacturing (MO)` | only as the *symptom* in S16-04 |
| **Unbuild** | `UB/…` moves appear in both residual sets and in the S16-04 corruption chain | named in passing |
| **Drop-ship** | `sale_order_id` and `sale_line_id` are NULL on **all 10,490** PO lines; `stock_dropshipping` is **not** in the 190 installed modules. Positive control: both columns exist in the extracted header. **Not a live state.** | correctly absent |
| **Subcontracting** | `mrp_subcontracting` is **not** in the 190 installed modules; `purchase_mrp` and `sale_mrp` are. **Not a live state.** | correctly absent |
| **Consignment / owner-restricted stock** | `restrict_partner_id` set on **1** of 103,949 stock moves; 2 `res.partner.property_stock_supplier` rows. Positive control: the predicate returns 1, so it can fire. **Effectively not a live state.** | correctly absent |
| **Intercompany** | 1 company in `res_company`. Not applicable. | correctly absent |
| **Landed costs** | `stock_landed_cost` 0 rows, `stock_valuation_layer.stock_landed_cost_id` set on **0** of 74,982. Confirms the brief. | yes |
| **Employee expense as a purchase channel** | `hr_expense` 2 rows, `hr_expense_sheet` 2. Effectively unused, but `account_move_line.expense_id` exists | no — and it does not matter |

**The single most consequential omission is the first row.** The brief's P2P reconstruction
describes the path taken by 26.9% of vendor bills by count. Stating it by value (89.8% PO-linked)
is equally true and gives the opposite impression — the brief states neither, so a reader cannot
tell which population any P2P conclusion applies to.

---

## 7. NEW FINDING — S16-04's 15-order-of-magnitude divergence originates in PROCURE-TO-PAY, not in manufacturing

The brief attributes the 30 extreme layers to *"`WH/MO/…` manufacturing and `UB/…` unbuild
documents"*. That is where the corruption **surfaces**. The chain begins at a goods receipt and is
driven by a vendor bill.

### 7.1 The chain, traced

All in product 11556 `วัตถุดิบ-ข้าวหอมมะลิอีสาน67` (raw paddy), category 10, `real_time` + `fifo`,
on **PO line 3453 of PO2024071276** (vendor 197, 500 t @ ฿30,000/t = ฿30/kg):

```
26816  2024-08-26  WH/IN/03638   unit_cost         30.67        <- last sane receipt
27102  2024-08-27  WH/IN/03634   unit_cost     712186.25        <- first anomaly (a receipt)
27193  2024-08-28  AP2024081214  qty 0  value -10954387437.50   <- bill price-diff layer, parent 27102
27199  2024-08-28  WH/IN/03689   unit_cost 4456673707.51
27283  2024-08-29  WH/IN/03707   unit_cost 15685015415021.04    value 736489898812313344.00
27395  2024-08-30  AP2024081365  price_diff_value 836312850     parent 27283
27396  2024-08-30  AP2024081372  price_diff_value 949239810     parent 27283
27394  2024-08-30  WH/IN/03709   unit_cost 52616504567828624.00 value 1.53e21
27942/3 2024-09-03 WH/OUT/01127/8 (returns to vendor, purchase_line_id 3453)
27485/7 2024-08-31 WH/MO/04039/SWR  <- manufacturing picks up the corrupt cost
UB/00443, UB/00444, 2024-09-03      <- unbuild propagates it
```

The stock moves themselves are clean: `SM 44320 (WH/IN/03707) price_unit=30`,
`SM 44418 (WH/IN/03709) price_unit=30`. The corruption is entirely in the valuation layer.

### 7.2 The mechanism, in the reference ERP source

`purchase_stock/models/stock_move.py:29-72`, `_get_price_unit`:

```
received_qty = line.qty_received
if self.state == 'done':
    received_qty -= self.product_uom._compute_quantity(self.quantity_done, line.product_uom)
if float_compare(line.qty_invoiced, received_qty, precision_rounding=line.product_uom.rounding) > 0:
    move_layer     = line.move_ids.stock_valuation_layer_ids
    invoiced_layer = line.invoice_lines.stock_valuation_layer_ids
    receipt_value  = sum(move_layer.mapped('value')) + sum(invoiced_layer.mapped('value'))
    invoiced_value = 0
    invoiced_qty   = 0
    for invoice_line in line.invoice_lines:
        ...
        invoiced_value += invoice_line.price_unit * invoice_line.quantity
        invoiced_qty   += invoice_line.product_uom_id._compute_quantity(invoice_line.quantity, line.product_id.uom_id)
    remaining_value = invoiced_value - receipt_value
    remaining_qty   = invoiced_qty   - line.product_uom._compute_quantity(received_qty, line.product_id.uom_id)
    price_unit = float_round(remaining_value / remaining_qty, precision_digits=price_unit_prec)
```

Three defects, all live on this line:

1. **`remaining_qty` has no zero-guard.** It is a difference of two quantities and the division is
   unconditional. As receipts catch up with bills it approaches zero.
2. **`invoiced_qty` and `invoiced_value` are unsigned.** They iterate `line.invoice_lines` and add
   `price_unit * quantity` for **every** linked line regardless of `move_type`. By contrast
   `purchase/models/purchase.py:1024-1033` `_compute_qty_invoiced` explicitly **subtracts**
   `in_refund` quantities. The two computations disagree on the same field.
3. **Cancelled bills are not filtered.** `_compute_qty_invoiced` excludes
   `move_id.state == 'cancel'`; `_get_price_unit` does not.

PO line 3453's `invoice_lines` (unit: journal item; population: every `account_move_line` with
`purchase_line_id = 3453`; positive control: 14,335 journal items in the table carry a
`purchase_line_id`, so the filter can fire):

```
AP2024080343  posted in_invoice  59588.000000 @ 30.84
AP2024081145  posted in_invoice  29055.000000 @ 30.00
AP2024081214  posted in_invoice  15382.000000 @ 30.00
AP2024081120  posted in_invoice  31633.000000 @ 30.00
AP2024081128  posted in_invoice  29015.000000 @ 30.00
AP2024081365  posted in_invoice  27905.000000 @ 30.00
AP2024081372  posted in_invoice  31673.000000 @ 30.00
AP2024081396  CANCEL in_invoice  46955.000000 @ 30.84    <- counted by _get_price_unit, excluded by _compute_qty_invoiced
RAP2024080001..7  posted in_refund, one mirroring each posted bill
```

Seven bills, seven matching refunds, one cancelled bill. `qty_invoiced` on the line is
**0.000000** (sign-aware). `_get_price_unit`'s unsigned sum is roughly **481,000 units**. And
`receipt_value` includes `invoiced_layer` — the price-difference layers themselves — so each
correction enlarges the next receipt's unit cost, which enlarges the next correction. A closed
positive-feedback loop, entered by a **vendor return / re-billing cycle**.

### 7.3 The brief's boundary understates the population

```
|value| > 1e12 : 30 layers      |value| > 1e9 : 37 layers
|unit_cost| > 1e5 : 66 layers across 22 distinct products
2 of the 30 are vendor-bill price-difference layers, not manufacturing layers
```

The "30" is an artefact of a `|value| > 1e12` threshold. Seven more layers exceed `|value| 1e9`,
and 66 carry a unit cost above ฿100,000 — for paddy whose true cost is ฿25–35/kg.

### 7.4 Verdict

**The S16-04 finding is real, correctly measured, and mis-attributed.** It is a Procure-to-Pay
defect with a named, source-level, reproducible mechanism, entered through the vendor
return/refund cycle on invoiced-before-received PO lines. It is not a manufacturing defect and it
is not an unexplained subledger break. It should be re-stated with §7.2 as its cause, and the
S16-05 "price-difference engine never fired" line should be withdrawn — the engine that fired is
the one that produced SVL 27395 and 27396.

---

## 8. PURCHASE-SIDE EVENTS THAT DO NOT REACH ACCOUNTING

Unit: as stated. Positive control given for each negative.

1. **Vendor returns that relieve inventory without a ledger entry.** 99 done vendor-return moves;
   **83 produce a journal entry, 16 do not.** Positive control: the other 83 do, so the join can
   find them.
2. **The commitment stage.** 2,163 purchase requests / 5,175 request lines and 5,881 purchase
   orders create **no** accounting entry of any kind. `account_budget` and
   `scgl_budget_management` are installed; whether budget commitment is recorded elsewhere is
   **EVIDENCE REQUIRED NEXT** (I did not extract `crossovered_budget*`).
3. **Vendor advances.** 137 down-payment PO lines carry ฿0.00 of `price_subtotal` and 0 received
   quantity, so PO totals do not include committed advance cash. Only 60 journal items carry
   `is_downpayment='t'`.
4. **1,475 cancelled pickings** and **97 cancelled PO lines** leave no trace in the ledger.
5. **12,581 draft journal entries** never reach the ledger, of which **11,767 are journal 11
   (DEPRE) dated 2026-07-31 .. 2038-08-31** (forward depreciation schedules) and **697 are journal
   3 (MISC) dated 2026-01-12 .. 2034-11-30**. 32 are draft vendor bills.
6. **Withholding tax certificates.** Unit: payment / certificate.
   ```
   account_payment 22,468 (supplier 19,575 / customer 2,893; outbound 17,107 / inbound 5,361)
   payments with wt_tax_id                       : 4,945   (4,941 of them supplier)
     of those, with NO withholding_tax_cert      : 1,488
   withholding_tax_cert                          : 5,201   (done 5,191)
     with no payment_id at all                   : 1,407   (1,405 of them 'done')
     pointing at a payment with no wt_tax_id     :   253
     cert payment_ids absent from account_payment:     0
   ```
   Positive controls: 3,786 done certificates **do** carry a payment, and 4,941 supplier payments
   **do** carry a `wt_tax_id`, so both halves of each negative could have returned zero and did
   not. **1,488 withheld payments have no certificate, and 1,405 issued certificates cannot be
   traced to the payment they certify.** This is a Thai statutory obligation and the brief reports
   only the 5,201 total.
7. **`wt_cert_cancel='t'` on 18,762 of 22,468 payments (83.5%).** The field name suggests a
   cancelled WHT certificate. I did not locate its writer in the custom modules and I do not
   assert what it means — **EVIDENCE REQUIRED NEXT**.

---

## 9. S16-07 REFINEMENT — the Buddhist-era dates are a P2P artefact

Unit: journal entry. Population: all 183,590 `account_move` rows, filtered on
`int(date[:4]) > 2100`.

```
moves dated year > 2100 : 30    year: all 2567    journal: all 5 (CABA Cash Basis Taxes)    state: all posted
tax_cash_basis_origin_move_id resolved: Counter({('in_invoice','posted'): 30})
  CABA2567040001..0020 -> AP2024040168..AP2024040174 (invoice_date 2024-04-10/11/12)
  CABA2567110001..0010 -> AP2024110525/528/530/538   (invoice_date 2024-11-13/14/15)
```

**All 30 are cash-basis VAT entries derived from posted vendor bills.** The bills themselves are
correctly dated 2024; only the derived entry carries 2567, and the day and month match the bill.
So the defect enters on the **payment/reconciliation leg of Procure-to-Pay**, not in general
ledger data entry. This narrows the brief's finding from "date leakage" to "the cash-basis tax
engine took a Buddhist-era date from a P2P event".

Negative with positive control: the custom `scgl_tax_period_date` fields are **not** the carrier —
`account_move_line.tax_period_date` has **0** rows with year > 2100 out of **18,197** non-null
values (`Counter({'2024':7469,'2025':6803,'2026':2592,'2023':1331,'1072':2})`), and
`account_move.tax_period` is set on 62,351 moves with no 2567 value. The predicate could fire and
did not. **Where the 2567 value entered is EVIDENCE REQUIRED NEXT.**

Incidental: **2 journal items carry `tax_period_date` in year 1072.** A second date-integrity
defect the brief does not report.

---

## 10. STATUS

### SUPPORTED
- Every headline arithmetic figure in the brief reproduces to the digit from the archive (§1).
- The brief's corrected classification method (product → template → `categ_id` → `ir_property`) is
  the only correct route; `valuation`/`cost_method` are read-only `related` fields with no
  per-product override (`stock_account/models/product.py:15-16,106-107`).
- `qty_received` is faithfully maintained against `stock_move`; only 27 of 9,522 lines disagree and
  all 27 are UoM-factor-24 artefacts of my re-derivation (§5.1).
- `stock_landed_cost` 0 rows and `stock_valuation_layer.stock_landed_cost_id` 0 of 74,982 —
  installed, never exercised.
- Drop-ship, subcontracting, consignment and intercompany are correctly absent as live states, each
  with a positive control (§6).
- S16-03's core point — that in this deployment, unlike series 18 and 19, the valuation→GL path
  executes — stands.

### CHALLENGED
- **S16-05 "net ฿72,097,814.25 outstanding".** State-contaminated (53 cancelled items =
  ฿76,422,354.13; posted balance is **−฿7,048,692.08**), computed on an account with
  `reconcile='f'`, swept manually by ฿1.9bn of MISC entries, and smaller than two individual
  unmatchable legs (non-PO bills ฿269.7m Dr; vendor returns ฿129.1m Dr). Should be withdrawn as
  stated. (§4)
- **S16-05 "the price-difference engine is wired and has never fired".** Structurally unreachable
  behind two independent gates; a different price-difference engine fired 1,123 times for
  ฿2,246,313,274.64 gross. (§3)
- **S16-03 "296 real_time-unlinked" as an anomaly.** 245 of 296 are consumable products, an
  explicit early return in `stock_account/models/stock_move.py:546-548`. (§2.3)
- **S16-03 "1,209 periodic-linked" as an anomaly.** 1,172 of 1,209 point at a vendor bill, a
  back-reference written by `_prepare_in_invoice_svl_vals`, not a valuation posting. (§2.1)
- **S16-03 "policy-change was tested and REFUTED".** The test read only surviving `ir_property`
  rows; category 15's sibling `property_cost_method` row carries `write_date 2025-01-21 06:52:06`
  and category 15's linked layers stop dead at that timestamp. (§2.2)
- **S16-04 attribution to manufacturing/unbuild.** Origin is a goods receipt + vendor bill
  price-difference chain on PO line 3453; manufacturing and unbuild are propagation. (§7)
- **S16-04 boundary "30 layers".** Threshold artefact: 37 exceed `|value| 1e9`, 66 carry
  `|unit_cost| > 1e5` across 22 products. (§7.3)
- **S16-06 P2P flow reconstruction.** 27,089 of 37,055 vendor bills (73.1% by count) carry no PO
  link; the dominant non-PO stream is export logistics. The described flow covers 26.9% of bills by
  count and 89.8% of bill value — the brief states neither unit. (§6)

### MISSING (present in the data, absent from the brief)
- Non-PO vendor bills as the majority document population, and the export-logistics cost stream
  behind them.
- Multiple AP control accounts driven by 1,715 partner-level `ir_property` rows.
- Purchase requisition stage (2,163 requests / 5,175 lines).
- Vendor returns (123 moves, 86 PO lines) and the dedicated `Returns` operation type (94 pickings).
- Purchase down payments (137 lines, `scgl_purchase_advance_payment`).
- Scrap (2,286) and inventory adjustments (3,010) as valuation-affecting purchase-adjacent events.
- The GRNI account being configured as the **expense account** on 16 product categories — the
  design fact that makes the whole GRNI bridge work and makes it unclearable.
- The WHT certificate coverage gaps (1,488 / 1,405 / 253).
- 2 journal items dated year 1072.

### RISKY
- The brief's practice of quoting all-state totals (account 39, bill lines) without a state split
  produces figures no Odoo report can reproduce. A reader reconciling to the running system cannot arrive at them.
- Reading `stock_valuation_layer.account_move_id` as "the valuation entry" is unsafe: the field
  holds a **vendor bill** id on 1,172+ rows. Any downstream metric built on it inherits the error.
- Using current-state `ir_property` to classify three years of history, without stating that a
  reverted property leaves no row, invites the same false refutation twice.
- The manual monthly GRNI sweep (39 MISC items, ฿1.9bn) means the GRNI account balance carries no
  independent information about receipt/bill matching at any date. Any control designed on that
  balance is inert.
- `_get_price_unit`'s unguarded `remaining_value / remaining_qty` is **still live**: 49 PO lines
  currently satisfy `qty_invoiced > qty_received`, and 123 vendor-return moves exist. The
  conditions that produced the August 2024 blow-up have not been removed.

### EVIDENCE REQUIRED NEXT
1. **Where the 2567 date enters.** All 30 CABA entries derive from posted vendor bills; neither
   `tax_period_date` (0 of 18,197) nor `tax_period` carries it. Extract `account_partial_reconcile`
   `max_date` for the reconciliations behind CABA2567* and read `scgl_tax_period_date` /
   `scgl_account_sequence` source.
2. **`wt_cert_cancel='t'` on 18,762 of 22,468 payments.** Locate the writer in
   `l10n_th_withholding_tax_cert*` or `scgl_*` before any conclusion is drawn.
3. **The 16 done vendor-return moves with no journal entry** — which categories, and is
   `_validate_accounting_entries`'s `currency_id.is_zero(value)` guard the explanation?
4. **The residual ~25–30 storable `real_time` unlinked layers** (§2.3) after removing consumables,
   category changes and revaluations.
5. **Budget commitment.** Extract `crossovered_budget`, `crossovered_budget_lines` and the
   `scgl_budget_management` tables to test whether the PO commitment stage reaches any ledger.
6. **The other 21 of the 30 extreme layers** — I traced product 11556 end to end; products 11630,
   11632 and 11633 (21 of the 30) were not individually traced and may have a second entry point.
7. **The 27,089 non-PO bills** — sample and confirm whether any are inventory purchases that
   *should* have had a PO, i.e. whether the 298 GRNI-debiting non-PO items are a control bypass
   rather than a design choice.
8. **PATH SET not tested:** whether other database artefacts for this SWR project exist elsewhere
   on the host. Every claim above is scoped to `iSMEs_2026-07-11_05-03-27.dump` alone.

### PRESERVED DISAGREEMENT
The brief's author and I agree on every number and disagree on what four of them mean. I did not
break §5.1 (`qty_received` maintenance) and I record that the brief is right there and I tried to
break it. On S16-03 the brief's *method correction* (#4 in its own defect list) is sound and I
adopted it unchanged; my disagreement is with the interpretation layered on top of it, not with the
join. On S16-04 the brief's decision not to publish "quadrillions posted to the GL" was correct and
its check was the right check; my objection is that having established the GL was clean, it stopped
before asking which document created the subledger value — the answer was two joins away and it
inverts the attribution.
