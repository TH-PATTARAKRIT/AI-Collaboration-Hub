# AAS-03 EXPERT 4 — LEAD CODE & UI ARCHITECT
## Adversarial challenge of the frozen P01 series-16 brief
Read-only. No database written, no source modified, no server run, no external network used.

---

## 0. DECLARATIONS

**POPULATION A — deployed modules.** `s16/installed.txt`, 190 distinct module names (189 lines + a final
line without a trailing newline; `cut -f1 | sort -u` = 190). 144 of these exist in the E-ENT series-16 core;
46 do not (the brief says 45 — the difference is `studio_customization`, which the brief counts separately).

**POPULATION B — core code that can execute here.** The 144 installed core modules only, not the 955
directories in the tree. Uninstalled core code cannot write a row.

**POPULATION C — custom code that can execute here.** The 45 installed non-core modules, 359 `.py` files
excluding `__pycache__`.

**PATH SET.**
- Core: `…/16 ODOO 16 ENTERPRISE/odoo-16.0+e.20230401/odoo/addons` (955 dirs; the sibling `…/addons`
  named in the brief's method notes **does not exist in this tree** — `ugrep: …/addons: No such file or
  directory`. E-ENT is the merged-layout core; the split layout belongs to E-SOM/E-KIT).
- Custom: `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/addons` — see §1, newly identified.
- Runtime: `~/Downloads/iSMEs_2026-07-11_05-03-27.dump`, extracted per table with
  `/opt/homebrew/opt/postgresql@18/bin/pg_restore -t <t> --data-only -f T_<t>.sql <dump>`.
  Tables I extracted beyond the frozen set: `ir_act_server`, `base_automation`, `ir_cron`, `ir_sequence`,
  `res_lang`, `ir_logging`, `ir_model`, `account_withholding_tax`, `withholding_tax_cert_line`,
  plus `--schema-only`.

**UNIT.** Stated per claim. Where I count code I count *assignment sites*, not files and not modules.
Where I count data I count *cells* (table, column, row) or *rows*, never "records" unqualified.

**PARSER COVERAGE CONTROL.** `s16/pgc.py` silently pads or truncates a row whose field count differs from
the COPY header (`vals = (vals + [None]*len(cols))[:len(cols)]`) — the same class of defect that produced
the brief's own method defect #4. I re-implemented the scan with an explicit ragged-row counter
(`/tmp/e4/scan_be.py`). **Result: `ragged_rows = 0` on every table I scanned** (account_move 183,590;
account_move_line 447,384; account_analytic_line 339,382; stock_move 103,949; stock_picking 20,098;
stock_move_line 139,952; purchase_order 5,881; purchase_order_line 10,490; stock_quant 27,196;
account_payment 22,468; withholding_tax_cert 5,201; mrp_production 10,764; purchase_request 2,163;
stock_scrap 2,286; hr_expense 2; hr_expense_sheet 0; stock_landed_cost 0). The padding path never fired,
so the brief's counts are not exposed to it either.

---

## 1. NEW: THE DEPLOYMENT'S CUSTOM ADDONS DIRECTORY IS IDENTIFIABLE AS A SINGLE TREE

The brief locates custom modules only as "45 of the 190 deployed modules are not in any core tree".
Scattered copies across the host index make every reading provisional. They need not be.

```
$ ls /Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/            → addons  swr  swr.zip
$ ls /Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/addons | wc -l   → 59
$ comm -12 <deployed-non-core-46> <that dir listing> | wc -l      → 45
$ comm -23 <deployed-non-core-46> <that dir listing>              → studio_customization
```

**45 of the 46 deployed non-core modules are present in that one directory; the only absentee is
`studio_customization`, which is generated inside the database and exists nowhere on the host.**
Manifest-version check against the deployed versions (with Odoo's `adapt_version` prefix rule applied):

```
version-match: 43 / 45   mismatch: 2
MISMATCH po_request_py3o        deployed=16.0.1.5    manifest=1.6   adapted=16.0.1.6
MISMATCH scgl_swr_custom_module deployed=16.0.1.0.0  manifest=1.0.1 adapted=16.0.1.0.1
```

Both mismatches are the tree being **one patch ahead** of the deployment, not behind. The directory also
holds 14 modules that are present but **not installed** (`amount_in_words_thai`, `cheque_control`,
`footer_layout`, `gsk_automatic_mail_server`, `hr_expense_petty_cash`, `hr_expense_petty_cash_sequence`,
`hr_expense_sequence`, `import_bridge_axis`, `pos_multi_uom_price`, `print_payment_remittance_adviec`,
`scgl_import_product_images`, `scgl_invoice_translated`, `scgl_swr_payment_term`, and a `.zip`) —
each verified against `installed.txt` one by one.

**This is a declarable PATH SET for custom source, not an author-chosen convenience sample.** Every custom
finding below is read from it. The two ahead-of-deployment modules are flagged wherever cited.

Also worth recording, because it defeats version-based series inference: several deployed versions carry a
*foreign* series inside them — `full_summarize_bills 16.0.14.0.0.1` (manifest `14.0.0.1`),
`l10n_th_partner`/`l10n_th_amount_to_text`/`l10n_th_withholding_tax_cert`/`partner_firstname`/
`partner_company_type` all `16.0.14.0.1.0.0` (manifest `14.0.1.0.0`), `l10n_th_base_location 16.0.15.0.1.0.0`
(manifest `15.0.1.0.0`). Series-14 and series-15 code is running on a series-16 platform. The `16.0.` prefix
in `ir_module_module.latest_version` is applied by `adapt_version` and says nothing about the code's series.

---

## 2. ASSIGNMENT 1 — DISPROVING "THE VALUATION POLICY GATE IS THE ONLY THING THAT DETERMINES WHETHER A RECEIPT POSTS"

### 2.1 The complete writer set

**UNIT: assignment sites that set `stock_valuation_layer.account_move_id`**, whether directly or through the
`account.move.stock_valuation_layer_ids` one2many (`stock_account/models/account_move.py:12`).

Command (POPULATION B, all 144 installed core modules; coverage assertion: all 144 directories exist,
`missing=0 of 144`; xargs exit 1 = "some batch matched nothing", stderr empty):
```
awk -v c="$CORE" '{printf "%s/%s%c", c, $0, 0}' /tmp/e4/inst_core.txt > /tmp/e4/dirs.nul
xargs -0 -P 10 -n 4 grep -rn --include='*.py' \
  -E "stock\.valuation\.layer|stock_valuation_layer_ids|account_move_id" < /tmp/e4/dirs.nul
→ 530 lines
```
*(Method note against myself: I read this file at 102 lines while the parallel grep was still running and
began drawing conclusions from it. The completed file has 530. A partially-written output file is
indistinguishable from a finished small one. I re-ran every derived count on the complete file.)*

| # | Site | Method | Gate |
|---|---|---|---|
| W1 | `stock_account/models/stock_move.py:524` | `_prepare_account_move_vals` | reached only via `stock_valuation_layer._validate_accounting_entries`, which requires `product_id.valuation == 'real_time'` **and** `not currency_id.is_zero(value)` |
| W2 | `stock_account/models/product.py:289` | `_change_standard_price` | `product.type != 'product' or product.valuation != 'real_time'` → skip |
| W3 | `stock_account/models/product.py:612` | `_svl_empty_stock_am` | caller-gated: `product.category.write()` emits it only `if product_category.property_valuation == 'real_time'` **evaluated before `super().write()`** |
| W4 | `stock_account/models/product.py:648` | `_svl_replenish_stock_am` | same, but evaluated **after** `super().write()` |
| W5 | `stock_account/wizard/stock_valuation_layer_revaluation.py:130` | manual revaluation wizard | no policy gate at the assignment; the wizard is only offered for real_time products |
| W6 | `stock_landed_costs/models/stock_landed_cost.py:171` | `button_validate` | landed-cost validation |
| **W7** | **`stock_account/models/account_move.py:375`** | **`_prepare_in_invoice_svl_vals`** — `'account_move_id': self.move_id.id` | **no valuation gate whatsoever** |

**Cross-check against a wider, differently-run corpus.** A second grep over the *whole* core tree
(all 955 module directories, pattern additionally including `svl`, `_account_entry_move`,
`_get_accounting_data_for_valuation`, `_prepare_account_move_vals`) completed later and returned 935 lines
touching 11 modules — 7 installed (`stock_account`, `stock_account_enterprise`, `stock_landed_costs`,
`purchase_stock`, `purchase_mrp`, `mrp_account`, `mrp_account_enterprise`, plus `hr_expense`) and 4 not
(`account_fleet`, `l10n_mx_edi_landing`, `mrp_subcontracting_dropshipping`, `point_of_sale`).
**Pattern-width caveat, stated rather than assumed: that corpus is NOT a superset for my unit** — its
pattern misses `move_vals['stock_valuation_layer_ids'] = …` entirely (0 hits) and catches only 2 of the
`'stock_valuation_layer_ids': [(6` sites. It is a superset for *modules that mention the model*, which is
what I used it for. Three installed modules it surfaced were absent from my 144-module result:
`mrp_account_enterprise`, `purchase_mrp`, `stock_account_enterprise`. Re-probing each on **my** unit:
`mrp_account_enterprise` and `stock_account_enterprise` match only a read-only report SQL alias `svl`,
`purchase_mrp` only a lambda variable of that name; on my unit all three hit nothing outside `tests/`.
**W1-W7 survives the cross-check.**

**But `purchase_mrp 16.0.1.0` (INSTALLED) does change W7's input**, which my first pass missed:
```python
# purchase_mrp/models/account_move.py:10-14
def _get_stock_valuation_layers(self, move):
    """ Do not handle the invoice correction for kit. It has to be done manually """
    layers = super()._get_stock_valuation_layers(move)
    return layers.filtered(lambda svl: svl.product_id == self.product_id)
```
A kit (phantom BoM) receipt produces layers for the *components*, so this filter returns an empty
recordset and `_create_in_invoice_svl` hits `if not layers: continue` — the price-difference correction is
silently skipped for kits. **LATENT in this deployment, measured:** `mrp_bom` 983 rows, `type` distribution
`{'normal': 983}` — **zero phantom BoMs**, and 0 of 10,490 purchase order lines reference a kit product.

**In POPULATION C (45 installed custom modules, 359 `.py` files) there are ZERO writers.**
Positive control on the same corpus: `move_id` → 58 hits; `account_move_id` → **1** hit, and it is
`om_data_remove/models/model.py:157`, a string in a delete list, not an assignment. So the negative is a
measurement, not silence.

### 2.2 W7 is a second writer, it is not policy-gated, and it fired 1,175 times here

`stock_account/models/account_move.py`, `_post()` (lines 44-87), selects the lines:
```python
if invoice.move_type in ('in_invoice', 'in_refund', 'in_receipt'):
    valued_lines |= invoice.invoice_line_ids.filtered(
        lambda l: l.product_id and l.product_id.cost_method != 'standard')
```
`_create_in_invoice_svl` (line 277) then checks only quantity > 0 and "layers exist". **The predicate is
`cost_method != 'standard'`. It is not `valuation == 'real_time'`.** Four product categories carry no
`property_cost_method` row at all, so their `cost_method` is the global default `standard` — but 26 of 30
categories are `fifo`/`average` regardless of their valuation policy, and every one of those passes.

Measured, with a coverage control (`unresolved account_move_id: 0`; policy resolved product→template→category
exactly as the brief's corrected method):

```
SVL rows                                   74,982
with account_move_id                       57,863
  move_type of the linked entry:  entry 56,688 | in_invoice 1,175
  state of the linked entry:      posted 57,854 | cancel 9
SVL.account_move_line_id NOT NULL           1,267   ← W7's signature
SVL.price_diff_value NOT NULL               1,267
SVL.stock_landed_cost_id NOT NULL               0
```

**1,175 valuation layers are linked to a vendor bill, not to a stock journal entry.** Their journal entry
is created by `account.move._post()` on a bill, not by picking validation, and the valuation policy plays
no part in whether it exists.

### 2.3 This dissolves the brief's Residual B

I reproduce the brief's S16-03 table to the row:

```
('manual_periodic', unlinked) 16,075   ('manual_periodic', linked)  1,209
('real_time',       unlinked)  1,044   ('real_time',       linked) 56,654
coverage control: 0 of 74,982 unresolved
```

Now split Residual B (the 1,209 `manual_periodic` layers that carry a journal entry) by writer:

```
Residual B                                       1,209
  written by W7 (account_move_line_id set)       1,173   (97.0%)
  linked entry move_type: in_invoice 1,172 | entry 37
  stock_move_id NULL                             1,194
  stock_valuation_layer_id (parent layer) set    1,173
```

**97.0% of Residual B is W7 output.** It is not an anomaly, not a policy inconsistency and not evidence of
policy history: it is the documented behaviour of a second writer that the brief's causal model omits.
The brief's S16-03 claim that the policy gate explains the linked/unlinked split is **incomplete by
1,173 rows on one side and, as §2.4 shows, misdirected on the other.**

### 2.4 Residual A is 82.8% explained by product *type*, not by policy

Residual A = 296 `real_time` layers, value ≠ 0, no journal entry. `stock_move._account_entry_move`
(line 543) opens with:
```python
if self.product_id.type != 'product':
    return am_vals          # no stock valuation for consumable products
```
Measured over those 296, by current product-template type:
```
detailed_type 'consu'   245   (82.8%)
detailed_type 'product'  51
stock_move state: done 278 | no stock move 18
account_move_line_id set: 0    (so none of these is W7 output)
```
**245 of 296 belong to products that are consumables today.** Either the type was changed after the layers
were created, or a path created a layer for a non-storable product. Both are findings; neither is the
valuation policy. The brief left Residual A unexplained.

### 2.5 A policy change *is* directly recorded — the brief refuted it with the wrong instrument

The brief argues policy change is not the explanation because "`ir_property` records current state, not
history — so history cannot be excluded, but the even spread does not support it." The history is not
missing. `product.category.write()` writes it into the SVL `description`:

```
SVL description class                          n     linked   sum(value)
Costing method change …                       20         9        3,900.00
Valuation method change …                      2         1            0.00
Product value manually modified …            114       106   -5,765,792,311,288,002.00
Revaluation of …                           2,372     1,248     -697,163,055,955,841.12
```
The 22 category-change rows in full show two events:

- **2023-10-11** category *All / Expenses / Material*: `standard → fifo`, then
  `manual_periodic → real_time`. Empty-out layers unlinked (pre-write policy = periodic), replenish layer
  **linked to move 1346** (post-write policy = real_time). Textbook W3/W4 ordering.
- **2025-01-21** category *All / Expenses / Material / แม่พิมพ์*: `fifo → average`. **All 9 empty-out
  layers carry journal entries (moves 129035-129043); all 9 replenish layers carry none.** W3 is gated on
  the policy *before* `super().write()`, W4 on the policy *after* it. That asymmetry is only producible if
  `property_valuation` went `real_time → manual_periodic` in the same write. And `ir_property` today
  reports that category as `manual_periodic`.

**So at least one category's valuation policy changed after the `ir_property` write-date window the brief
used to exclude history, and the SVL table records it.** `ir_property` write dates were the wrong
instrument; the direct record was three columns away.

### 2.6 What actually decides whether a receipt posts — the corrected causal statement

Five independent conditions, only one of which is the policy:
1. `product_id.type == 'product'` (`_account_entry_move`) — kills 245 of Residual A.
2. `product_id.valuation == 'real_time'` (`_validate_accounting_entries`) — the brief's gate.
3. `not currency_id.is_zero(value)` — the brief's 748 zero-value skips.
4. `cost_method != 'standard'` on a *posted vendor bill* — W7, an entirely separate entry point that
   ignores 1 and 2 and produced 1,175 links.
5. `_get_accounting_data_for_valuation` must resolve a journal and the three accounts. Here it always can:
   `property_stock_journal` is a single global row `account.journal,8`, and **all 15 `real_time`
   categories carry a non-null valuation / input / output account triple** (full table derived and checked
   category by category). No missing-account blocker exists in this configuration.

### 2.7 CHALLENGE to S16-05 — account 1173 is unreachable, not "wired and never fired"

The brief states: "**`1173 4310005 Purchase price variance`: CONFIGURED, 0 items.** The price-difference
engine is wired and has never fired in 183,590 journal entries." That conflates two different engines.

`property_account_creditor_price_difference_categ` is read in exactly one place across the 144 installed
core modules (declared search; the only other hits are a 9.0 migration script and two test files):
`purchase_price_diff/models/account_move_line.py:11-12` — a module that **is** installed (16.0.1.1,
`auto_install: True`). Its override:
```python
def _get_price_diff_account(self):
    if self.product_id.cost_method == 'standard':
        debit_pdiff_account = self.product_id.property_account_creditor_price_difference \
                              or self.product_id.categ_id.property_account_creditor_price_difference_categ
        ...
        return debit_pdiff_account
    return super()._get_price_diff_account()      # → purchase_stock: accounts['expense']
```
Its only caller is `purchase_stock/models/account_invoice.py:45`, inside
`_stock_account_prepare_anglo_saxon_in_lines_vals`, which opens:
```python
if move.move_type not in ('in_invoice','in_refund','in_receipt') or not move.company_id.anglo_saxon_accounting:
    continue
```
Account 1173 therefore requires **three** conditions, and **two of them fail independently**:

| Condition | Here |
|---|---|
| `company.anglo_saxon_accounting` | **FALSE** (`res_company.anglo_saxon_accounting = f`) |
| `product.valuation == 'real_time'` | true for the configured category |
| `cost_method == 'standard'` (else `purchase_price_diff` falls through to `accounts['expense']`) | **fifo** |

The single configured row is `product.category,10` = *All / Expenses / Material / Rice*, whose
`property_cost_method` is **`fifo`**. Even with anglo-saxon accounting switched on, that category would
route to `accounts['expense']` and never to 1173. (The brief also reports one configured row; there are
**6 further `property_account_creditor_price_difference` rows at `product.template` level** that it does
not mention.)

**Corrected statement.** Price differences are not absent and the engine is not idle. The *valuation-layer*
engine (W7) fired **1,267 times**. What is switched off is the *journal-line* engine, at the company flag,
and account 1173 is additionally unreachable for the one category it is configured on. "0 items on 1173"
is the expected output of a disabled path and is **evidence of nothing** about price-difference activity —
which means the real exposure is the opposite of the brief's reading: inventory valuation is being
corrected for price differences 1,267 times while **no purchase-price-variance line ever reaches the P&L**.

---

## 3. ASSIGNMENT 2 — METHOD OVERRIDES THAT CHANGE P2P ACCOUNTING

Enumeration over POPULATION C (45 installed custom modules), pattern = `def <name>` for the assigned method
list plus every accounting-model `_inherit`, plus raw SQL, plus writes to `date`/`name`/`state`:

**Not present anywhere in the installed custom code:** `_post`, `action_post`, `_create_invoices`,
`_get_accounting_data_for_valuation`, `_prepare_account_move_vals`, `_stock_account_prepare_anglo_saxon_*`,
`_check_fiscalyear_lock_date`. Positive control: the same command returned 36 `def` hits for other names,
so the pattern fires.

### C-1 `scgl_account_sequence 16.0.1.0.0` — LIVE, and it is the reason the BE dates are visible in names
```python
# models/account_move.py — full replacement of sequence.mixin._get_starting_sequence
starting_sequence = "%s%d%02d0000" % (self.journal_id.code, self.date.year, self.date.month)
# models/sequence_mixin.py
_sequence_monthly_regex = r'^(?P<prefix1>[\D\d]+?)(?P<year>\d{4})(?P<month>(0[1-9]|1[0-2]))(?P<seq>\d*)(?P<suffix>\D*?)$'
```
The move name is built from `self.date.year`. Core's regex constrains a 4-digit year to `(19|20|21)\d{2}`;
this one accepts **any** four digits, so `2567` is accepted as a year by the monthly matcher and by
`sequence.mixin._constrains_date_sequence`. Journal 5 in the data: 7,768 moves, names
`CABA2023…` 1,791 / `CABA2024…` 2,731 / `CABA2025…` 2,210 / `CABA2026…` 1,001 / **`CABA2567…` 30**.
`models/__init__.py` imports `sequence_mixin` and `account_move` but **comments out `account_journal`**, so
that module's `CHECK (code ~* '^[^0-9]*$')` journal-code constraint is dead code and never loaded.

### C-2 `scgl_purchase_advance_payment 16.0.1.0.0` — LIVE, three defects
- Its `purchase.order.line._prepare_invoice_line` is **not an override**: core series-16
  `purchase.order.line` defines `_prepare_account_move_line` (`purchase/models/purchase.py:1350`) and has no
  `_prepare_invoice_line`. So the method is reachable **only** from this module's own wizard. Normal
  PO→bill creation is untouched. *(Latent for the ordinary path — a distinction that matters, and one an
  override-name grep alone would get wrong.)*
- `_create_bill` for the `delivered` branch has `# return purchase_order_ids._create_invoices(final=self.deduct_down_payments)`
  commented out and calls `action_create_invoice()`, which takes no `final` argument. **The
  `deduct_down_payments` field is therefore inert.** Measured:
  ```
  down-payment bill lines (account_move_line.is_downpayment = t)   60
    all in_invoice, all posted, debit ฿14,429,800.46, credit ฿0.00
    lines with negative quantity or price (a deduction)             0
  down-payment PO lines                                           137  (57 line_section + 80 value lines)
    product_qty on all 80 value lines                        0.000000
    price_subtotal on all 80 value lines                         0.00
    qty_invoiced = 1.0 while product_qty = 0.0                     18
  ```
  ฿14.4m of advances are debited (accounts 1152001 *Advance Payment*, 1152005 *Deposit*,
  1231011 *Work in process(Asset)*, and four expense accounts) and **nothing in this mechanism ever nets
  them off the final vendor bill**. 18 PO lines are over-invoiced by construction.
- `self.env['account.move'].sudo().create(...)` (wizard line 203) creates the bill as superuser.

### C-3 `l10n_th_withholding_tax 16.0.1.0.1` — LIVE
```python
def _compute_wht_amount(self):
    self.wht_amount = 0
    for rec in self:
        ...
        self.wht_amount = amount_wt      # writes the RECORDSET, not `rec`
```
A stored compute that assigns to `self` inside a `for rec in self` loop: on a multi-record recompute every
record takes the last record's value. Measured over 37,171 vendor bills, recomputing
`Σ rate/100 × price_subtotal`: **207 stored values disagree with the recomputation**, 7 of them non-zero on
moves with no WHT line at all. The dominant cause of the other 200 is C-4.

`_compute_amount` on `account.payment.register` mutates wizard state from inside a compute
(`self.amount -= amount_wt`, `payment_difference_handling`, `writeoff_account_id`, `writeoff_label`) —
fields outside its own `@api.depends` set. And the deduction is `Σ rate × full invoice price_subtotal` with
no proration, so a **partial** payment still deducts 100% of the invoice's withholding.

### C-4 `account.withholding.tax` id 2 is named "WHT3%" and its rate is 0 — LIVE, highest-volume category
```
wt id 2  "WHT3%"    rate = 0      7,834 journal-item lines, 2,038 payments, base ฿19,723,704.95 → computes ฿0.00
wt id 4  "WHT0.5%"  rate = 0.5    4,707 lines, base ฿145,549,541.58 → ฿727,747.71
wt id 1  "WHT1%"    rate = 1      5,051 lines, base ฿9,937,344.09  → ฿99,373.44
wt id 3/7/5/6 = 5 / 2 / 15 / 10 percent, 219 / 44 / 12 / 11 lines
```
The most-used withholding category computes zero. It is **not** a statutory-amount finding — the
certificates carry their own per-line rate and 2,642 `withholding_tax_cert_line` rows show
`wt_percent = 3` (cert lines total: 6,159 rows, base ฿4,552,157,594.03, amount ฿26,219,137.38; 111 lines at
`wt_percent = 0`; account 1137 shows 5,863 items, Dr ฿26,889,437.34 / Cr ฿27,367,226.89). So the exposure is
that the **automatic** deduction silently returns zero for that category and depends entirely on manual
write-off entry; the certificate and the ledger are populated by a different route.
*(I checked and discarded a candidate finding here: `account_payment.wt_cert_cancel = TRUE` on 18,762 of
22,468 payments looks alarming, but `_compute_wt_cert_cancel` sets it True when a payment has **no** cert
at all. It is not a cancellation count. Reading the compute before publishing was what stopped it.)*

### C-5 `scgl_budget_management 16.0.1.0.0` — LIVE, one latent crash
`_compute_po_amount` executes its SQL inside `if line.analytic_account_id.id:` but reads
`self.env.cr.fetchone()[0]` **outside** that guard, still inside the loop. A budget line with no analytic
account therefore consumes the *previous* line's result set, or raises on the first such line. Budget here
is advisory only — nothing in the module blocks a PO that exceeds a budget.

### C-6 Modules read and found to have no P2P accounting effect
`scgl_swr_custom_module` (fields only: `mill_id`, `brand_id`, `port`; `rice_mill.py` commented out of
`__init__` — **note: source is 1.0.1, deployment runs 1.0.0, so this reading is of a later revision**),
`purchase_request 16.0.1.0` (OCA; `button_confirm`/`unlink`/`_action_done` overrides post chatter messages
and maintain allocations only — no accounting), `full_summarize_bills` (report + Thai baht-text; manifest
version `14.0.0.1`), `scgl_tax_period_date` (§5), `scgl_account_reports` (raw-SQL tax report, read-only),
`dev_print_cheque`, `print_voucher_request`, `full_invoice_custom`, `bi_print_journal_entries` (report
layers). No custom module writes `account_move.date`, `name`, `state`, `move_type` or `journal_id` —
positive control: the same pattern returned 40+ hits on other models.

---

## 4. ASSIGNMENT 3 — `om_data_remove 16.0.1.0.1`

Source read: `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/addons/om_data_remove/models/model.py`,
374 lines, manifest version `16.0.1.0.1` = the deployed version exactly.

### 4.1 What it can delete
`res.config.settings.remove_data(o, s)` (lines 13-45) resolves each model name to its table and executes
```python
sql = "delete from %s" % t_name
self._cr.execute(sql)
self._cr.commit()
```
No ORM. Therefore: **no `unlink()` override runs, no `_check_fiscalyear_lock_date`, no posted-state check,
no record rule, no company filter, no chatter, no `ir_logging` entry, and `commit()` makes it
non-rollbackable.** If one table's delete raises, the ValidationError is raised *after* the earlier tables
have already been committed — partial deletion is a reachable state.

`remove_account()` deletes, in order: `payment.transaction`, `account.bank.statement.line`,
`account.payment`, `account.analytic.line`, `account.analytic.account`, `account.partial.reconcile`,
`account.move.line`, `hr.expense.sheet`, `account.move`.
`remove_inventory()` deletes 13 tables **including `stock.valuation.layer`** and `stock.move`, `stock.quant`,
`stock.picking`, `stock.production.lot`.
`remove_account_chart()` additionally NULLs `property_account_creditor_price_difference_categ`,
`property_stock_account_input_categ_id`, `property_stock_account_output_categ_id`,
`property_stock_valuation_account_id` on every product category and both valuation accounts on every
stock location, and sets `chart_template_id = False` on the company.
`remove_all()` chains fifteen of these.

### 4.2 Guards that exist
- Menu `menu_remove_data` and the settings-view block are `groups="base.group_system"`. That is the only
  access control; the module ships **no `security/` directory** (`ls …/om_data_remove/security` → no such
  file or directory), so it relies entirely on the core `res.config.settings` ACL.
- 10 of the 20 buttons carry an XML `confirm=` string. **10 do not** — including
  `remove_all` ("Delete All Transactions Except Master Data"), `remove_mrp_bom`, `remove_project`,
  `remove_quality`, `remove_quality_setting`, `remove_website`, `remove_product`,
  `remove_product_attribute`, `remove_message`, `reset_cat_loc_name`. A single click on
  "Delete All Transactions Except Master Data" begins an unconfirmed, committed, fifteen-table wipe.

### 4.3 The schema consequence for this brief's central metric
From `pg_restore --schema-only`:
```
ADD CONSTRAINT stock_valuation_layer_account_move_id_fkey
    FOREIGN KEY (account_move_id) REFERENCES public.account_move(id) ON DELETE SET NULL;
ADD CONSTRAINT stock_valuation_layer_account_move_line_id_fkey
    FOREIGN KEY (account_move_line_id) REFERENCES public.account_move_line(id) ON DELETE SET NULL;
ADD CONSTRAINT stock_valuation_layer_stock_move_id_fkey  … ON DELETE SET NULL;
```
**A raw `DELETE FROM account_move` leaves every `stock_valuation_layer` row in place with
`account_move_id` silently set to NULL.** That is exactly the shape the brief reports for the other
generations — series-18 OCC 0 of 47,801, series-19 0 of 14,441. I am **not** asserting that is what happened
there; those databases are outside my evidence base. I am asserting that a mechanism installed on this
estate produces that signature without leaving a trace in the SVL table, and that "0 of N linked" must
therefore be tested against it before being read as "the valuation→GL path never executed".

### 4.4 Did it run *here*? No positive evidence; and the negative has a stated limit
`delete from <table>` empties a table completely, so a run would show as a table that is empty, or whose
minimum id is far above 1 because everything before the wipe is gone. Measured:

```
table                        rows     min_id     max_id  density
account_move               183,590        619    205,369    89.7%
account_move_line          447,384      1,327    535,556    83.7%
stock_valuation_layer       74,982        114     76,238    98.5%
purchase_order               5,881         70      6,021    98.8%
stock_move                 103,949        193    122,788    84.8%
account_payment             22,468         36     23,156    97.2%
mrp_production              10,764         22     11,140    96.8%
stock_quant                 27,196        183     66,753    40.9%
account_analytic_line      339,382        116    482,874    70.3%
hr_expense                       2          6          8    66.7%
hr_expense_sheet                 0          -          -        -
stock_landed_cost                0          -          -        -
ir_logging                       0 rows
```
Every table `remove_account` / `remove_inventory` / `remove_purchase` / `remove_mrp` targets is populated
with a low minimum id. **No table shows a wipe signature.**

**Limits of that negative, stated rather than assumed:** (a) `hr_expense_sheet` and `stock_landed_cost` are
empty, and an empty table cannot be distinguished by this test from a wiped one — for those two,
`remove_expense` and the landed-cost path are *not excluded*; (b) the module writes no log, no chatter and
no tracking, and `ir_logging` is empty, so a run followed by a restore-from-backup would leave nothing here;
(c) the archive is a single point in time (2026-07-11), so this is a statement about the surviving state,
not about the deployment's history.

---

## 5. ASSIGNMENT 4 — THE BUDDHIST-ERA DATES

### 5.1 The leakage is materially wider than 30 rows

The brief reports "30 `account_move` rows dated year 2567". Cell-level scan, PATTERN `^2[5-9]\d\d-\d\d-\d\d`,
UNIT = (table, column, row), with a CE-year control on the same column and `ragged_rows = 0` everywhere:

| table | column | BE cells | CE control on same column |
|---|---|---|---|
| account_move | `date` | **30** | 183,560 |
| account_move | `tax_period` | **7** | 62,344 |
| account_move | `invoice_date` | **1** | 39,757 |
| account_move_line | `date` | **120** | 447,264 |
| account_analytic_line | `date` | **120** | 339,262 |
| stock_picking | `scheduled_date` | **178** | 19,920 |
| stock_picking | `date_deadline` | **2** | 18,668 |
| stock_move | `date` | **5** | 103,938 |
| stock_move | `date_deadline` | **6** | 75,072 |
| purchase_order | `date_planned` | **2** | 5,869 |
| purchase_order_line | `date_planned` | **6** | 10,426 |
| purchase_request_line | `date_required` | **7** | 5,168 |

Zero BE cells, with a working control, in: `stock_move_line`, `account_payment`, `withholding_tax_cert`,
`mrp_production`, `stock_quant`, `purchase_request`, `stock_scrap`, `hr_expense`.

The 120 `account_move_line` rows are exactly 4 lines × the same 30 moves, with no desync in either
direction (`aml on BE moves: 120, of which CE-dated: 0`). The 120 analytic lines follow them.
Buddhist years present: 2566, 2567, 2568.

### 5.2 It is typed, not converted — and `scgl_tax_period_date` is not implicated

`scgl_tax_period_date 16.0.0.0.1` is 45 lines. It adds `account.move.tax_period` and
`account.move.line.tax_period_date` and a `create()` that stamps the former onto tax lines. It performs **no
date arithmetic and never writes `date`**. Its own field carries 7 BE values — it stores what it is given.
(It does carry a smaller defect: `@api.model def create(self, vals_list)` overriding a `model_create_multi`
method, then reading `rec.tax_period` off a potentially multi-record result.)

Whole-custom-tree scan for BE conversion (`543|Buddhi|thai_year|be_year|2566|2567|2568`, `.py` + `.xml`):
every hit is in a **report/presentation** layer — `dev_print_cheque/report/thainlp.py` (not installed),
`l10n_th_withholding_tax_cert_form/reports/layout.xml:183,395` (`+543` at render time),
`l10n_th_withholding_tax_report/models/report_withholding_tax.py:49,121` and
`report/report_withholding_tax_xlsx.py:408`. **Nothing writes a converted value back.**

Non-module code paths checked: `base_automation` 1 row, `ir_act_server` 94 rows of which exactly one
mentions `unlink`/`date`/`account.move` and it is `records.action_unlink_all()` on model 374 =
`privacy.lookup.wizard.line` (a transient), `ir_cron` 33 rows, `ir_logging` 0 rows.

**The sufficient mechanism is data entry.** `res_lang`: `th_TH` is **active** with
`date_format = '%d/%m/%Y'`, and `en_US` has itself been changed to `%d/%m/%Y` (Odoo's shipped `en_US`
default is `%m/%d/%Y`). Odoo 16 has no Buddhist-era handling; a user typing `10/04/2567` yields the Python
date `2567-04-10`. Two independent corroborations:
- All 178 BE `stock_picking.scheduled_date` values end `17:00:00` — midnight Bangkok converted to UTC, the
  exact signature of a *date* typed into a datetime widget. Their `create_date` and `date_done` are correct
  CE (e.g. `WH/INT/00459` scheduled `2567-08-06 17:00:00`, done `2024-09-07 09:33:53`).
- All 5 BE `stock_move.date` rows are `state = 'cancel'` — nothing was valued from them.

### 5.3 What actually happened to the 30 CABA moves — a correction of emphasis

All 30 are cash-basis moves in journal 5, every one carrying `tax_cash_basis_origin_move_id`. Their **origin
bills are all correctly dated CE** (`AP2024040168`…`AP2024110538`, dates 2024-04-10 … 2024-11-18, all
`in_invoice`, journal 2). The names `CABA2567MMNNNN` are *derived from* the bad date by C-1's
`_get_starting_sequence`, they did not cause it. Several rows have `create_date == write_date`
(e.g. 74974, 75050, 75054, 75076, 119126, 119298), so the BE date was present when the record was created,
not applied by a later edit. 7 of the 30 additionally have a BE `tax_period`.

**Consequence, stated at the right size:** the exposure is not 30 rows in a header table. It is
**120 posted journal items and 120 analytic lines that no period report, ageing bucket or fiscal-year
close will ever see**, plus 178 warehouse documents (176 of them `done`) whose scheduled date is 543 years
out. With `period_lock_date`, `fiscalyear_lock_date` and `tax_lock_date` all NULL and `po_lock = 'edit'`,
nothing prevents more.

---

## 6. CHALLENGE TO S16-04 — THE GL *WAS* WRITTEN WITH ABSURD AMOUNTS

### 6.1 The brief's arithmetic reproduces exactly
```
SVL rows with |value| > 1e12                 30
  of which linked to a journal entry         25, all state = posted
  their journal entries: 25 moves, 50 items, debit = credit = ฿31,622,699.37
  largest single line in those 25 moves      ฿4,430,937.00
  dates 2024-08-17 … 2024-08-31
sum(value) over the whole table excluding the 30   ฿400,338,755.98
```
Every figure matches the brief. The disagreement is not arithmetic.

### 6.2 The conclusion does not follow, because the population was drawn on the wrong side

"The GL was NOT corrupted" was tested only on the 25 entries reachable *from the 30 SVL rows*. The
discriminating query is the one over the ledger itself. `account_move_line`, 447,384 rows, coverage control
`aml whose move_id is not in account_move: 0`:

```
|amount| > 1e12 :   0 lines
|amount| > 1e10 :   4 lines,   2 moves,  all posted
|amount| > 1e9  :  10 lines,   5 moves,  8 posted / 2 cancel
|amount| > 1e8  : 104 lines,  49 moves, 94 posted / 10 cancel
```
The top four:
```
aml 18720  move 6756  STJ2023110741  posted  2023-11-23  acct 1289  Cr ฿19,784,867,370.00  "UB/00001 - คัดแล้ว-ข้าวขาว5%"
aml 18721  move 6756  STJ2023110741  posted  2023-11-23  acct 1068  Dr ฿19,784,867,370.00  "UB/00001 - …"
aml 18738  move 6765  STJ2023110750  posted  2023-11-23  acct 1289  Dr ฿19,745,654,299.40  "Revaluation of UB/00001 (negative inventory)"
aml 18739  move 6765  STJ2023110750  posted  2023-11-23  acct 1068  Cr ฿19,745,654,299.40  "Revaluation of UB/00001 (negative inventory)"
```
**A posted journal entry of ฿19.78 billion, partially reversed by a posted ฿19.75 billion revaluation,
leaving ฿39,213,070.60 permanently misallocated between 1147001 *Work in progress* and 1148002
*Semi Product*.** Neither move appears among the 25 the brief examined, because their SVLs sit below the
1e12 threshold the brief chose.

**The claim "the GL was NOT corrupted" is CHALLENGED.** The correct statement is: *the 25 journal entries
linked to the 30 largest valuation layers are balanced and sane*; the ledger as a whole is not.

### 6.3 The brief's attribution of the 30 is also wrong

The brief says the 30 come "from `WH/MO/…` manufacturing and `UB/…` unbuild documents". By description
class:
```
UB/ 9 | WH/MO/ 6 | WH/IN/ 3 | WH/OUT/ 2 | AP… (vendor bill) 2
Revaluation of… 3 | Product value manually modified 2 | Product… 3
```
The two **largest** are a receipt and a delivery, not an MO or an unbuild:
```
svl 27394  WH/IN/03709   +฿1,533,508,025,629,365,764,096.00  unit ฿52,616,504,567,828,624.00  qty 29,145
svl 27943  WH/OUT/01128  -฿1,037,501,181,874,222,661,632.00  unit ฿35,720,474,500,747,900.00  qty -29,045
```
and two are **W7 vendor-bill price-difference layers** (`svl 27395`, `svl 27396`, ~-4.4e17 and -4.97e17,
qty 0) — i.e. the second writer from §2 carried the corrupt cost into the P2P stream.

### 6.4 A code-level candidate root cause the brief did not identify

All four of the giant WH/IN / WH/OUT layers point at **one purchase order line**:
```
purchase_order_line 3453, PO2024071276 (state purchase)
   product_qty 500.000000   price_unit ฿30,000.00
   qty_received 0.000000    qty_invoiced 0.000000     qty_received_method = 'stock_moves'
   stock moves in state 'done' referencing it: 716,822 units
   stock_move.price_unit on those moves: 30   (sane)
```
`purchase_stock/models/stock_move.py::_get_price_unit` (lines 29-73), which `stock_account`'s
`_get_in_svl_vals` uses as `unit_cost = abs(move._get_price_unit())` for any non-`standard` cost method:
```python
received_qty = line.qty_received                       # 0
if self.state == 'done':
    received_qty -= self.product_uom._compute_quantity(self.quantity_done, line.product_uom)   # → negative
if float_compare(line.qty_invoiced, received_qty, …) > 0:      # 0 > negative  → ALWAYS TRUE
    receipt_value = sum(move_layer.value) + sum(invoiced_layer.value)
    remaining_value = invoiced_value - receipt_value            # invoiced_value = 0
    remaining_qty   = invoiced_qty - received_qty
    price_unit = remaining_value / remaining_qty                # = -(cumulative layer value)/qty
```
With `qty_received` stuck at 0, the exceptional branch fires on **every** receipt for that line and prices
it from the running total of the layers it has already created — a positive feedback loop. The escalation is
visible in the layer series for the affected products, e.g. product 11633 goes unit ฿257 → ฿49,213 → ฿692,892,928,508.81
between 2024-01 and 2024-08-31, then a manual modification of −฿1,073,730,548,532,915.38 on 2024-09-03.

The precondition is measurable and is not unique to that line:
```
PO lines with qty_received_method='stock_moves', DONE stock moves, and qty_received = 0.000000 : 32
   total done quantity on them: 2,406,805 units
   all 32 in state 'purchase'; qty_received_manual is NULL or 0 on all 32
CONTROL: 9,328 PO lines have done stock moves; 9,296 of them have qty_received > 0
```
**32 of 9,328 (0.34%) purchase order lines are in a state where a stored compute over done stock moves
reports zero received.** I present this as the strongest available mechanism, not as proof: settling it
requires a controlled reproduction, which read-only access cannot provide (see §9).

### 6.5 Manual valuation intervention at scale — not in the brief at all
```
'Revaluation of …'                 2,372 layers, 1,248 with a journal entry, 2023-11-04 … 2026-07-09, 250 distinct days
'Product value manually modified'    114 layers,   106 with a journal entry, 18 distinct days
```
`stock.valuation.layer.revaluation` (W5) and `_change_standard_price` (W2) have been used 2,486 times, and
1,354 of those wrote to the ledger. With all three lock dates NULL, that is an unconstrained manual
adjustment channel into inventory valuation and the GL.

### 6.6 Two smaller ledger/subledger breaks
- **9 valuation layers are linked to CANCELLED journal entries** (moves 1346, 2056, 80037, 119400, 122935,
  127571, 127596, 132024, 166611), values from ฿0.00 to −฿7,136,031.75. The subledger says valued; the
  ledger says cancelled.
- **Journal-entry date vs stock-move date.** `_prepare_account_move_vals` (stock_move.py:505-527) dates the
  entry `context['force_period_date']` → `svl.account_move_line_id.date` → **`fields.Date.context_today`**.
  Measured over 56,444 SVL→`entry` pairs that have a stock move: **only 66.69% share the stock move's date;
  33.31% (18,801) do not**, spread from −2,256,472 days to +20,842 days, with 1,578 at +1 day and 1,228 at
  −8 days. The inventory subledger and the GL are not date-aligned for a third of the postings, and no lock
  date constrains it.

---

## 7. ASSIGNMENT 5 — LATENT vs LIVE IN *THIS* CONFIGURATION

| Item | Status | Basis |
|---|---|---|
| W1 `_prepare_account_move_vals` | **LIVE** | 56,688 SVL→`entry` links |
| W7 `_prepare_in_invoice_svl_vals` | **LIVE** | 1,267 SVLs with `account_move_line_id`; 1,175 linked to `in_invoice` |
| W2 `_change_standard_price` | **LIVE** | 114 layers, 106 linked |
| W5 revaluation wizard | **LIVE** | 2,372 layers, 1,248 linked |
| W3/W4 category policy change | **LIVE, twice** | 22 layers, 2023-10-11 and 2025-01-21 |
| `purchase_mrp._get_stock_valuation_layers` kit filter | **LATENT** | `mrp_bom` 983 rows, all `type='normal'`; 0 of 10,490 PO lines on a kit product |
| Price-difference **journal line** → account 1173 | **UNREACHABLE** | `anglo_saxon_accounting = f`; and the one configured category is `fifo`, not `standard` |
| W6 `stock_landed_costs` | **LATENT** | module installed, `stock_landed_cost` 0 rows, `stock_landed_cost_id` 0 of 74,982 |
| Anglo-Saxon COGS lines (`_stock_account_prepare_anglo_saxon_out_lines_vals`) | **LATENT** | `res_company.anglo_saxon_accounting = f` |
| Storno reversal (`is_storno`) | **LATENT** | `res_company.account_storno = f` |
| Price-difference account 1173 *Purchase price variance* | **CONFIGURED, NEVER FIRED** | 0 journal items — confirms the brief |
| `scgl_account_sequence` `_get_starting_sequence` | **LIVE** | 7,768 journal-5 names built from `date.year` |
| `scgl_account_sequence` `account_journal` code constraint | **DEAD** | commented out of `models/__init__.py` |
| `scgl_purchase_advance_payment._prepare_invoice_line` | **LATENT for normal PO→bill** | core defines `_prepare_account_move_line`, not this name |
| `scgl_purchase_advance_payment` wizard | **LIVE** | 137 PO lines / 60 bill lines / ฿14,429,800.46 |
| `deduct_down_payments` | **DEAD** | the `final=` call is commented out; 0 deduction lines exist |
| `l10n_th_withholding_tax._compute_wht_amount` recordset bug | **LIVE** | 207 of 37,171 bills disagree with recomputation |
| `WHT3%` at rate 0 | **LIVE** | 7,834 lines, 2,038 payments, ฿19.7m base → ฿0.00 computed |
| `scgl_tax_period_date` | **LIVE but date-neutral** | 62,351 moves carry `tax_period`; no date arithmetic in source |
| `scgl_budget_management._compute_po_amount` cursor bug | **LATENT** | fires only for a budget line with no analytic account |
| `om_data_remove` | **INSTALLED, ARMED, NO EVIDENCE OF EXECUTION HERE** | §4.4, with limits stated |
| `scgl_swr_custom_module` | **LIVE, accounting-neutral** | fields only; source is one patch ahead of deployment |
| `purchase_request` P2P overrides | **LIVE, accounting-neutral** | chatter + allocations only |

---

## 8. VERDICT BY CATEGORY

### SUPPORTED (independently reproduced from the archive)
- S16-01 lock vocabulary and state: `period_lock_date`, `fiscalyear_lock_date`, `tax_lock_date` all NULL;
  `po_lock = 'edit'`; `anglo_saxon_accounting = f`. Additionally `account_storno = f`.
- S16-02 in full, once keyed correctly: `property_valuation` 16 rows = 1 global `manual_periodic` + 15
  per-category `real_time`; `property_cost_method` 27 = 1 global `standard` + 18 fifo + 8 average;
  `property_stock_journal` 1 global `account.journal,8`; `property_account_creditor_price_difference_categ`
  1 row → `account.account,1173`; 30 product categories; `ir_property` 13,331 rows.
- S16-03 arithmetic: the 4-cell table, 0 unresolved, 296 + 748 = 1,044, 1,209.
- S16-04 arithmetic: 30 rows > 1e12, 25 linked and posted, 50 items, D = C = ฿31,622,699.37,
  ฿400,338,755.98 excluding the 30.
- S16-06: `stock_landed_cost` 0 rows with the module installed; `stock_landed_cost_id` 0 of 74,982;
  `withholding_tax_cert` 5,201 (done 5,191 / cancel 5 / draft 5). Account 1173 is configured and carries
  0 items — the *count* is confirmed; the brief's reading of it is challenged in §2.7.
- S16-07: exactly 30 `account_move.date` cells in Buddhist years.

### CHALLENGED

1. **"The valuation policy gate determines whether a valuation layer carries a journal entry."**
   A second writer exists (`_prepare_in_invoice_svl_vals`) with no policy predicate; it produced 1,175 of
   the 57,863 links and **1,173 of the 1,209 rows in the brief's own Residual B**.
2. **"Policy-change was tested as the explanation and REFUTED."** Refuted with `ir_property` write dates,
   which cannot see history. The SVL `description` column records two policy/cost-method change events
   directly, and the 2025-01-21 event's linked/unlinked asymmetry proves a `real_time → manual_periodic`
   flip **after** the ir_property window the brief relied on.
3. **"The GL was NOT corrupted."** True of the 25 entries examined; false of the ledger. Move 6756 posts
   ฿19,784,867,370.00 and move 6765 posts ฿19,745,654,299.40, both `posted`, net ฿39,213,070.60 misallocated.
4. **Attribution of the 30 giant layers to MO and unbuild.** The two largest are a receipt (`WH/IN/03709`)
   and a delivery (`WH/OUT/01128`); two more are vendor-bill price-difference layers.
5. **Residual A is not unexplained.** 245 of 296 (82.8%) are products whose template type is `consu`, which
   `_account_entry_move` skips before any policy test.
6. **"30 `account_move` rows dated 2567" understates the leak.** 12 (table, column) pairs across 7 tables
   carry Buddhist years: 30 move dates, 120 journal items, 120 analytic lines, 178 pickings, plus purchase
   and request dates.
7. **The E-ENT core's `<root>/addons` does not exist.** The brief's method note treats the split layout as
   general; for E-ENT the PATH SET is `odoo/addons` alone.
8. **"The price-difference engine is wired and has never fired."** The journal-line path is disabled at
   the company flag (`anglo_saxon_accounting = f`) and account 1173 is additionally unreachable for its
   own category (`fifo`, while `purchase_price_diff` routes only `standard`). Meanwhile the
   valuation-layer price-difference engine fired 1,267 times. §2.7.
9. **The configured price-difference surface is larger than one row** — 6 further
   `property_account_creditor_price_difference` rows exist at `product.template` level.

### MISSING FROM THE BRIEF (new, evidenced)
- The custom addons tree is identifiable as one directory, 45/46 present, 43/45 exact version match (§1).
- Series-14 and series-15 modules running on the series-16 platform (§1).
- The complete SVL→GL writer set: 7 sites, and zero in custom code (§2.1).
- ฿14,429,800.46 of vendor advances with a dead deduction mechanism and 18 over-invoiced PO lines (C-2).
- `WHT3%` configured at rate 0 across 7,834 lines and 2,038 payments (C-4).
- 2,372 manual revaluations and 114 manual price modifications, 1,354 of them posting to the GL (§6.5).
- 9 valuation layers pointing at cancelled journal entries (§6.6).
- 33.31% of inventory journal entries are not dated on their stock move's date (§6.6).
- 32 purchase order lines with done receipts and `qty_received = 0`, the precondition for the runaway
  unit-cost branch (§6.4).
- `stock_valuation_layer.account_move_id` is `ON DELETE SET NULL`, so a raw `DELETE FROM account_move`
  reproduces the "0 of N linked" signature invisibly (§4.3).
- 10 of `om_data_remove`'s 20 destructive buttons carry no confirmation (§4.2).
- `purchase_mrp` silently skips price-difference correction for kits (latent here: no phantom BoMs) (§2.1).

### RISKY (real, but I have not measured the consequence — do not publish as established)
- `l10n_th_withholding_tax._compute_amount` writing non-dependency fields from inside a compute.
- Partial payments deducting 100% of an invoice's withholding.
- `scgl_budget_management` cursor reuse (latent).
- `scgl_tax_period_date`'s `@api.model create` on a `model_create_multi` method.
- Whether the 51 non-`consu` rows in Residual A share a single cause.

### EVIDENCE REQUIRED NEXT
1. **`ir_property` history.** `mail_message` / `mail_tracking_value` for `product.category` writes on
   2023-10-11 and 2025-01-21 would date the policy flips precisely. Not extracted; both tables are in the
   TOC.
2. **`qty_received = 0` root cause.** Whether it is a stale stored compute or a deliberate manual reset
   needs `mail_tracking_value` on `purchase.order.line`, or a controlled recompute — the latter is a write
   and is outside my mandate.
3. **The runaway-unit-cost chain.** Only a controlled reproduction (a scratch database, PO line with
   `qty_received` forced to 0, repeated receipts) can convert §6.4 from mechanism to proof.
4. **Move 6756 / 6765 provenance.** Which SVL created STJ2023110741, and whether UB/00001's negative-stock
   revaluation was manual. Requires joining `stock_valuation_layer` to those two moves and reading
   `mail_message`.
5. **Cross-generation test of §4.3.** For the series-18 and series-19 archives: are there SVL rows whose
   `account_move_id` is NULL but whose `stock_move_id` also went NULL, and does `account_move.id` start far
   above 1? That distinguishes "never posted" from "posted then deleted". Those archives are outside my
   evidence base.
6. **`hr_expense_sheet` and `stock_landed_cost`.** Empty tables cannot be distinguished from wiped ones by
   the id-density test; a different instrument is needed before either is called "never used".

---

## 9. DEFECTS I COMMITTED AND CORRECTED BEFORE PUBLISHING
1. **I keyed `ir_property` on the `name` column** and concluded there was no global `property_valuation`
   default and that the brief's S16-02 was wrong. `ir_property.name` holds the field's *label* for global
   defaults (`'Valuation Property'`) and the technical name for per-record rows. Keyed on `fields_id`
   (14374) the global row is right there, `value_text = 'manual_periodic'`, `res_id` and `company_id` NULL.
   **The brief was correct and I was about to publish a false correction of it.** Every property figure in
   §8 is re-derived through `ir_model_fields`.
2. **I read a background grep's output file while it was still being written**, at 102 of an eventual 530
   lines, and started classifying writers from it. A partially-flushed file looks exactly like a complete
   small one. All writer counts were re-derived after the task reported completion, and the coverage
   assertion (`missing=0 of 144`, stderr empty) was added afterwards.
3. **I nearly published `wt_cert_cancel = TRUE on 18,762 of 22,468 payments` as a mass cert-cancellation.**
   Reading `_compute_wt_cert_cancel` first showed it is set True when a payment has *no* certificate.
4. **My first custom-tree grep used `--include=*.py` unquoted under zsh**, which failed with
   `no matches found` rather than returning zero results — a command that errors and a search that finds
   nothing are not the same outcome, and the shell made them look alike.
6. **My first writer enumeration was scoped to the 144 installed core modules and I treated it as
   complete.** A wider grep finishing later surfaced three installed modules my result had not listed.
   Re-probing each on my own unit showed none contains an assignment site — but it also surfaced
   `purchase_mrp`'s override of W7's *input*, which is a real behaviour change I had missed. Two
   corpora with different pattern widths caught what one did not, and neither was a superset of the
   other.
5. **I initially trusted `s16/pgc.py`'s row padding.** It silently reshapes any ragged row. I re-scanned
   with an explicit ragged-row counter before relying on any cell-level count.

---

## 10. ONE-LINE POSITION
The brief's measurements reproduce; its causal model does not. The valuation-policy gate is one of five
conditions and not the decisive one for 1,173 of the rows the brief could not explain; the policy *did*
change and the subledger says so in plain text; and the ledger did receive a posted ฿19.78 billion entry
that the brief's chosen population could not see. The one account the brief reads as "wired and never
fired" is unreachable by construction, while the engine it belongs to has fired 1,267 times somewhere
the brief did not look.
