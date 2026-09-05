# AAS-03 EXPERT C — Lead Integration & Localization
## Adversarial challenge of the frozen S18 findings brief
Read-only forensic. No database written, no source modified, no server run.
Date 2026-09-05. Finding prefix `C-`.

---

## 0. EVIDENCE BASE AND DECLARED BOUNDS

**Archive (runtime evidence).** `~/OCC_BACKUP/idemo18_uat_pre_scgl_occ_website_20260830_085432.dump`
Tool: `/opt/homebrew/opt/postgresql@18/bin/pg_restore` (18.6). Extraction form used throughout:
`pg_restore -t <table> --data-only -f <out> <dump>`.

**Table-existence discriminator (used, and it fired).** For every extraction I counted the
`COPY public.<t> (` header separately from the row count. A 0-byte-meaningful file is
ambiguous; a header count is not:

```
account_accrued_orders_wizard : COPY_header=1 rows=0     <- table EXISTS, empty
account_automatic_entry_wizard: COPY_header=1 rows=0     <- table EXISTS, empty
account_transfer_model        : COPY_header=1 rows=0     <- table EXISTS, empty
stock_landed_cost             : COPY_header=0 rows=0     <- table ABSENT
account_transfer_model_account_account_rel : COPY_header=0 rows=0  <- name I guessed; ABSENT
```
This is the control the memory note "control that cannot detect its failure" demands.
Byte size alone would have reported all five identically.

**Source PATH SETs.**
- **PATH SET A1** `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons` — 797 module dirs (`ls -1 | wc -l`).
- **PATH SET A2** `.../odoo/addons_archive` — **961 module dirs**. *This root is not named in the frozen brief.* Union A1+A2 = 1,758.
- **PATH SET B** every directory on `/Volumes/iMacSys` named `scgl_*` or `purchase_request` — 169 dirs, 2,179 `.py`/`.xml`/`.csv` files.
- **PATH SET C** version-matched OCA WHT source at
  `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/smeplus-custom/addons/`.

**A tooling false negative I caught in myself.** My first PATH SET B sweep was
`timeout 600 find ...`. `timeout` is not installed on this host (`which timeout` → not found);
the command exited 1 and printed nothing. Taken at face value that is
"no custom module source exists on the volume". Re-run without `timeout`: **169 directories**.
Recorded because the frozen brief's S18-11 rests on exactly this class of sweep.

---

## 1. PRIMARY ASSIGNMENT — "materially configured"

### C-01 — CHALLENGED. The "15 of 126" figure is a jsonb row count, not the effective configuration. In company 1 the effective count is 126 of 126.

The brief resolves the field **per category**. The field is company-dependent, so the unit of
the claim is the **(category, company) pair**. I resolved all 504.

**Resolution rule, from v18 source, not assumed.**
`odoo/models.py:2995-3025` `_field_to_sql`, which `_fetch_query` (`models.py`, `sql = self._field_to_sql(...)`) uses to build every read:

```python
if field.company_dependent:
    sql_field = SQL("%(column)s->%(company_id)s", column=sql_field,
                    company_id=str(self.env.company.id))
    fallback = field.get_company_dependent_fallback(self)
    fallback = field.convert_to_column(field.convert_to_write(fallback, self), self)
    if fallback not in (None, 0):   # 0, 0.0, False, None
        sql_field = SQL('COALESCE(%(field)s, to_jsonb(%(fallback)s::%(column_type)s))', ...)
```
and `odoo/addons/base/models/ir_default.py:154-182`, `ORDER BY d.user_id, d.company_id, d.id`,
first row per field wins (Postgres sorts NULL last in ASC, so a company row outranks a global one).

**Raw jsonb (T_product_category.sql, 126 rows):**
```
property_stock_account_input_categ_id
  None                                        111
  '{"1": 176, "2": 62, "3": 100, "4": 138}'    15
```

**ir_default rows for this field** (A_ir_default.sql joined to A_ir_model_fields.sql):
id 49 co=1 → `176`; id 54 co=2 → `false`; id 63 co=3 → `false`; **company 4 — no row**; no global row.

**Effective value, all 504 pairs:**

| company | from jsonb | from ir_default | effective |
|---|---|---|---|
| 1 | 15 → 176 | 111 → **176** (row 49) | **176 on 126 of 126** |
| 2 | 15 → 62 | 111 → False (row 54) | 62 on 15, none on 111 |
| 3 | 15 → 100 | 111 → False (row 63) | 100 on 15, none on 111 |
| 4 | 15 → 138 | 111 → None (**no row**) | 138 on 15, none on 111 |

**Configured pairs = 171 of 504, not 60.** Company 1 — the company holding 9,733 of the
15,522 moves and 25,978 of the 47,801 valuation layers — has **no unconfigured category at all**.
The brief's sentence "*the 111 non-configured categories resolve to no account in companies 2, 3, 4*"
is correct as far as it goes and enumerates exactly the three companies for which the answer is
"none". Company 1 is absent from that sentence, and the "15 of 126" headline then travels
unqualified. This understates the configuration in the only company where it could matter.

### C-02 — MISSING from the brief. Companies 2/3 `false` and company 4 "no row" are behaviourally identical; the distinction the brief draws carries no consequence.

`false` → `convert_to_cache(False)` → empty recordset → `convert_to_column` → `None` → the
`if fallback not in (None, 0)` guard fails → no COALESCE → SQL NULL.
A missing `ir_default` row → `_get_model_defaults(...).get(name)` → `None` → identical path.
Same resolved value, same reads, same writes. Presenting them as two different states implies a
difference that does not exist.

### C-03 — CHALLENGED (extension of C-01). Same defect, same field family, wider. The sibling accounts are also effectively configured in company 1.

Same 504-pair resolution over every company-dependent `product.category` field:

```
property_stock_account_output_categ_id  co1 -> 701 on 126/126   (co2/3/4: 15 configured, 111 none)
property_stock_valuation_account_id     co1 -> 169 on 119 + {216,217,218,219,220,221,222} on 7  = 126/126
property_stock_journal                  co1 -> 40 on 126/126 (all from ir_default; jsonb NULL 126/126)
property_valuation                      all four companies -> 'manual_periodic' 126/126 (one global row, id 10)
property_cost_method                    co1 -> 'average' 18 / 'standard' 108 ; co2/3/4 -> 'standard' 126
property_stock_account_production_cost_id  co1/2/3 -> False 126 ; co4 -> None 126
property_account_creditor_price_difference_categ  -> no ir_default row anywhere, None 126/126 x4
```
S18-02's conclusion (126/126 × 4/4 = `manual_periodic`) is **SUPPORTED** and reproduced independently.
Its neighbours are not.

### C-04 — RISKY, and it inverts the brief's risk direction. Company 1 is the only company where the valuation policy can be switched without hitting the guard, and switching it posts to 210300.

`stock_account/models/product.py:963-971`:
```python
@api.constrains(... + ['property_valuation'])
def _check_valuation_accounts(self):
    for category in self:
        if category.property_valuation == 'real_time':
            if any(not category[account] for account in fnames):
                raise ValidationError(_('The stock accounts should be set in order to use the automatic valuation.'))
```
with `fnames = [input, output, valuation]`. Against C-01/C-03:

- **company 1** — all three resolve non-false on **126 of 126** categories → the guard **cannot refuse**.
- **companies 2, 3, 4** — all three are false/None on 111 of 126 → the guard **refuses** 111, permits 15.

And `ProductCategory.write()` (`product.py:1032-1090`) reads `property_valuation` **after**
`super().write()` for the replenish half:
```python
in_svl_vals_list = products._svl_replenish_stock(description, products_orig_quantity_svl)
in_stock_valuation_layers = SVL.sudo().create(in_svl_vals_list)
if product_category.property_valuation == 'real_time':
    move_vals_list += Product._svl_replenish_stock_am(in_stock_valuation_layers)
```
and `_svl_replenish_stock_am` (`product.py:809-830`), for positive quantity:
`debit = stock_valuation`, **`credit = stock_input`**, in `product_accounts['stock_journal']`.

So a single company-dependent write of `property_valuation` on a company-1 category credits
account **176** in journal **40** — the two objects the brief reports as carrying zero items —
for the on-hand value of that category's products. Magnitude available in the same archive:

```
SVL SUM(remaining_value)   company 1  29,835,023.51 THB   (25,978 layers)
                           company 2  60,059,575.87 THB   (21,823 layers)
```
(awk over `A_stock_valuation_layer.sql`, NF uniform at 20 on all 47,801 rows.)

This is not the same statement as "the account is configured but unused". It is
"the account is fully configured in the live company, has no guard against activation, and one
company-dependent field write routes tens of millions of baht through it".

**I have not measured** whether any user currently holds write access to `product.category`
`property_valuation` in company 1. That is the missing clause — see §6.

---

## 2. PRIMARY ASSIGNMENT — "reachable"

I enumerated **writers**, not observed rows, as instructed.

### C-05 — CHALLENGED. `purchase.action_accrued_expense_entry` is a deployed, bound, permissioned writer whose account domain contains 210300.

`account/wizard/accrued_orders.py:44-52`:
```python
account_id = fields.Many2one('account.account', required=True, string='Accrual Account',
    check_company=True,
    domain="[('account_type', '=', 'liability_current')] if context.get('active_model') == 'purchase.order' else [('account_type', '=', 'asset_current')]")
```
`purchase/views/purchase_views.xml:864-871` binds it to `purchase.order` for `account.group_account_user`.

Deployed, from the archive, not from source:
```
ir_model_data ('purchase','action_accrued_expense_entry') -> ir.actions.act_window res_id 433
ir_act_window id=433: binding_model_id=588, binding_type=action, binding_view_types=list,form,
                      target=new, res_model=account.accrued.orders.wizard,
                      name={"en_US":"Accrued Expense Entry","th_TH":"รายการค่าใช้จ่ายคงค้าง"}
ir_model_data ('purchase','model_purchase_order') -> res_id 588        [binding resolves]
res_groups_users_rel: gid 28 (account.group_account_user) -> 22 users
                      gid 29 (account.group_account_manager) -> 9 users
res_users: 47 rows, 43 active
```
Account 176 is `liability_current` (`A_account_account.sql`: id 176, `{"en_US":"Uninvoiced Receipts"}`,
`code_store {"1":"210300"}`, `reconcile=t`, `deprecated=f`) → **inside the domain**.
The wizard's input population is non-empty: the brief's own S18-07 counts 1,580 received-not-invoiced
lines, ฿30,080,689.78 pre-tax. The wizard has **no default** for `account_id`; company 1 offers
22 `liability_current` candidates, of which at least three are plausible (175 `210200 Accrued Expenses`,
244 `212001 ค่าใช้จ่ายค้างจ่าย`, 176 `210300 Uninvoiced Receipts`).

The account is not unreachable. It is unused, on a live path, with a non-empty input set.

### C-06 — SUPPORTED, with a stronger control than the brief used. No accrual entry exists.

The brief's control ("15,434 of 15,522 have a non-empty ref") proves the field is populated,
not that an English phrase can match it. The wizard writes
`ref = _('Accrued %(entry_type)s entry as of %(date)s', ...)` — capital A. A case-sensitive
grep for `accru` would miss every one. Re-run case-insensitively over `A_account_move.sql`,
field 29 (`ref`):

```
moves: 15522     ref empty/NULL: 88     ref non-empty: 15434
ci match "accru"      : 0        <- claim under test
ci match "uninvoiced" : 0
ci match "grni"       : 0
ci match "reversal"   : 119      <- POSITIVE CONTROL: an English ref phrase does fire in this field
ci match "withhold|wht|ภาษีหัก" : 1
```
S18-07's negative **stands**, now with a discriminating positive control rather than a
populated-field control.

### C-07 — MISSING. `mrp_account`'s WIP wizard defaults its overhead credit to account 176 and does not consult the valuation policy at all.

`mrp_account/wizard/mrp_wip_accounting.py:70-78`:
```python
def _get_overhead_account(self):
    overhead_account = self.env.company.account_production_wip_overhead_account_id
    if overhead_account: return overhead_account.id
    cop_acc = ProductCategory._fields['property_stock_account_production_cost_id'].get_company_dependent_fallback(ProductCategory)
    if cop_acc: return cop_acc.id
    return ProductCategory._fields['property_stock_account_input_categ_id'].get_company_dependent_fallback(ProductCategory).id
```
and `default_get` sets `journal_id` from `property_stock_journal.get_company_dependent_fallback` → **journal 40** for company 1.

Deployed state, from `A_res_company.sql` (204 columns):
```
co1  account_production_wip_overhead_account_id = NULL   account_production_wip_account_id = NULL
co2  NULL / NULL      co3  NULL / NULL      co4  NULL / NULL
```
`property_stock_account_production_cost_id` ir_default: co1 `false` (row 51), co2 `false`, co3 `false`, co4 no row.
Both earlier branches are falsy → **the third branch is taken → account 176 for company 1**.

Deployment facts:
```
ir_module_module: mrp 18.0.2.0 installed, mrp_account 18.0.1.0 installed
ir_model_data ('mrp_account','action_wip_accounting') -> ir.actions.act_window res_id 954
mrp_wip_accounting.xml:37-44  binding_model_id = mrp.model_mrp_production, group_account_user, target=new
mrp_production: 5,549 rows
```
This route is **independent of `property_valuation`** — no `real_time` gate anywhere in the file.
Caveat, stated rather than glossed: the debit line uses
`self.env.company.account_production_wip_account_id.id`, which is NULL here, so an untouched
wizard would not post. The line list is `<field name="line_ids"><list editable="bottom">` with
`account_id` editable, so a user completes the debit and the 176 credit stands. Reachability:
**yes, with one manual field**. Not "unreachable".

### C-08 — MISSING. A scheduled writer is armed but unconfigured.

```
ir_cron: 66 rows, 58 active
  id=18 active=t "Account: Post draft entries with auto_post enabled and accounting date up to today"
  id=24 active=t "Account automatic transfers: Perform transfers"
        ir_model_data ('account_auto_transfer','ir_cron_auto_transfer') -> ir.cron res_id 24
ir_module_module: account_auto_transfer 18.0.1.0 installed
account_transfer_model      : COPY_header=1 rows=0
account_transfer_model_line : COPY_header=1 rows=0
```
`account_auto_transfer` moves balances between arbitrary origin and destination accounts on a
schedule. The module is installed, the cron is **active**, and **zero** transfer models are
configured. One row in `account_transfer_model` makes an unattended writer live against any
account, 176 included. Present state: cannot fire. Distance to firing: one configuration record.

### C-09 — Enumerated and dismissed, with the reason.

- `account_automatic_entry_wizard` — table present, 0 rows (TransientModel, so 0 rows is
  uninformative about history). `ir_model_data ('account','action_automatic_entry_change_account')
  -> ir.actions.server res_id 251` exists; "Change Account" retargets selected journal items to
  any account. **Reachable writer, no type restriction.**
- `account_reconcile_model` 16 rows / `account_reconcile_model_line` 8 rows — the four Odoo
  defaults per company. The only accounts named are 200 / 86 / 124 / 162 ("Internal Transfers").
  `rule_type=writeoff_button` lets the user override the account at reconciliation time.
  Weak route; recorded, not relied on.
- **Landed costs** — `stock_landed_costs` `state=uninstalled` in `ir_module_module`, and
  `stock_landed_cost` has **COPY_header=0** (no table). Two independent confirmations.
  The brief's bounded absence is **SUPPORTED**.
- **Import** — `base_import` 18.0.2.0 and `account_base_import` 18.0.1.0 both installed, and the
  channel has already been used at scale: `ir_model_data` module `occ_mig` holds **181,540**
  external IDs, including **10,190 for `account.move`**. `occ_mig` is **not** a row in
  `ir_module_module` — it is an xmlid namespace belonging to a data migration, not a module.
  An xmlid-keyed import can create or update moves and lines on any account.

### C-10 — CHALLENGED, and this one is a wrong-cause finding, not a wrong-conclusion one. S18-06's "the bill-line override is v19-only" is false. It exists in v18.

The brief's evidence was a **file-name** search: "*v18 `stock_account/models/` contains no
`account_move_line.py` at all (directory listed: 15 files, none named that)*". The file name is
absent. The behaviour is not — the class lives in `account_move.py`:

`stock_account/models/account_move.py:255-274` (PATH SET A1, v18.0+e.20250608):
```python
class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    ...
    def _compute_account_id(self):
        super()._compute_account_id()
        input_lines = self.filtered(lambda line: (
            line._eligible_for_cogs()
            and line.move_id.company_id.anglo_saxon_accounting
            and line.move_id.is_purchase_document()))
        for line in input_lines:
            accounts = line.with_company(line.company_id).product_id.product_tmpl_id.get_product_accounts(fiscal_pos=...)
            if accounts['stock_input']:
                line.account_id = accounts['stock_input']

    def _eligible_for_cogs(self):
        return self.product_id.is_storable and self.product_id.valuation == 'real_time'
```
The brief's **conclusion** (no bill line posts to a clearing account here) is correct. Its
**cause** is wrong. The mechanism is present in the deployed generation and is inert because of
two configuration values, not because the code does not exist:

```
res_company.anglo_saxon_accounting:  co1 = t   co2 = f   co3 = f   co4 = f
product.valuation = 'real_time':      nowhere (126/126 x 4/4 manual_periodic, C-03)
```
In company 1 the first gate is already open. The second is one `ir_default` row (id 10) or one
jsonb key away — and per C-01, company 1's `accounts['stock_input']` is already 176 on 126 of 126
categories, so `if accounts['stock_input']:` would pass on every line. The brief's framing
("v19-only") suggests the deployment is structurally immune. It is not.

Method note for the record: the search unit (a file name) did not match the claim unit (a
behaviour). This is the same shape as the memory note "check unit must match the defect".

### C-11 — SUPPORTED, bounded. Bounded negative on custom source, with controls, and with its boundary stated.

POPULATION: PATH SET B — 169 dirs, 2,179 `.py`/`.xml`/`.csv` files.
UNIT: file containing the pattern.

```
pattern property_stock_account_input_categ_id ->   0 files
pattern stock_input                           ->   0 files
pattern 210300                                ->   0 files
pattern Uninvoiced                            ->   0 files
pattern property_valuation                    ->   0 files
POSITIVE CONTROLS, same file list, same tool:
pattern account.move                          ->  98 files
pattern account_id                            ->  75 files
pattern product.category                      ->  16 files
```
No `scgl_*` or `purchase_request` source writes the GRNI account or touches the valuation
policy. This **corroborates** S18-12's explicit check on `scgl_product_category_company`.

**Boundary, stated because it is load-bearing:** PATH SET B is *name-scoped*. It cannot speak
for any installed module named otherwise — see C-13, which shows that set is 55 modules, not 16.

---

## 3. PRIMARY ASSIGNMENT — the inverse claim (0 journal items), by a second method

### C-12a — SUPPORTED. Three methods, uniform-shape control, injection control, draft rows included.

**Method 2 — awk state machine over the frozen extraction, field 7 (`account_id`), independent of `pgc.py`:**
```
ROWS: 40353          NF distribution: NF=64 -> 40353   (no column shift anywhere)
account_id=176 -> 0    62 -> 0    100 -> 0    138 -> 0
account_id=701 -> 0   702 -> 0    703 -> 0    704 -> 0
POSITIVE CONTROL  account_id=169 -> 2940     distinct account_id present: 144
journal_id 16 -> 0    24 -> 0    32 -> 0    40 -> 0     distinct journals present: 22
parent_state: posted 36805, draft 3540, cancel 8   <- draft lines ARE in the population
company: 1 -> 25166, 2 -> 15187
```

**Synthetic injection control** (memory: "prove the filter can fire"). One real row copied with
field 7 forced to `176`:
```
injected file: rows 40354   account_id=176 -> 2   account_id=169 -> 2940
```
0 → 2. The predicate can fire; the zero is a property of the data.

**Method 3 — a fresh, independent extraction from the dump:**
```
pg_restore -t account_move_line --data-only -f X_aml.sql <dump>   rc=0  18,155,413 bytes
diff against the frozen T_account_move_line.sql: 4 lines, all of them the
  \restrict / \unrestrict random session tokens pg_dump emits per run.
X_aml.sql, NF==64 numeric-id rows: 40,353   account_id==176: 0
```

**A trap worth publishing.** A naive `grep -c $'\t176\t'` over the same file returns **4**.
Field-anchored, those hits are in column 1 (`id`), column 2 (`move_id`) and column 11
(`payment_id`) — zero in column 7. A pattern-width error here manufactures a finding.

**S18-03 reproduced by the same awk method** over `A_stock_valuation_layer.sql`:
```
SVL rows 47,801, NF uniform at 20
company 1: 25,978 layers  account_move_id != NULL = 0   account_move_line_id != NULL = 0   stock_move_id != NULL = 23,943
company 2: 21,823 layers  account_move_id != NULL = 0   account_move_line_id != NULL = 0   stock_move_id != NULL = 20,992
                                                                              (23,943 + 20,992 = 44,935, matches the brief)
```

### C-12b — SUPPORTED, and the brief understated its own population count.
55 installed modules, not 16, have no source in either declared root — see C-13. The zero-item
result is unaffected (it is a data fact), but any *explanation* of the zero that rests on
"we have read the code" inherits that gap.

---

## 4. SECONDARY — Thailand localization

### C-13 — CHALLENGED, and this is a denominator defect that reaches the whole package. The deployed non-core module set is 55, not 16, and the WHT stack is entirely inside the 39 the brief never enumerated.

```
ir_module_module: 361 installed
not present in PATH SET A1 (797 dirs)                       -> 66 modules
not present in A1 ∪ A2 (addons + addons_archive, 1,758)     -> 55 modules
custom_installed.txt (the frozen brief's population)        -> 16 modules
```
The brief's 16 is the result of a `scgl_*` + `purchase_request` name pattern. The 39 it omits
include, among others:

- the entire Thai WHT stack (C-14),
- `om_data_remove` 18.0.1.0.0 (Odoo Mates, Sunpop.cn) — **installed**; a prior process recorded this
  module as deleting the ledger without authorisation. It is live in this deployment too.
- `account_payment_multi_deduction` 18.0.1.0.2 (Ecosoft/OCA), `hr_expense_petty_cash` 18.0.1.2 (Ecosoft/OCA),
  `bi_print_journal_entries`, `journal_entries_report`, `full_summarize_bills`, `print_voucher_request`,
  `account_invoice_fixed_discount`, `sale_fixed_discount`, `date_range`, `report_xlsx`, `stock_card_report`,
  `construction`, `fleet` and its six satellites, `inherit_inventory`, `inherit_sales`, `accessories`,
  `delivery_cement_truck`, `equipment_sequence`, `product_stock_equipment`, `hr_payroll_other_input`.

Two consequences. First, **PATH SET A1 is not the deployed core**: `fleet`, `snailmail`,
`construction`, `account_fleet`, `hr_fleet`, `documents_fleet`, `journal_entries_report` are all
installed and all absent from `.../odoo/addons`; they live in the undeclared
`.../odoo/addons_archive` (961 dirs). Second, an undeclared customization surface exists that
`custom_installed.txt` cannot show at all — `res_company` carries Studio fields
`x_scgl_wip_control_enabled` (t on companies 3 and 4) and `x_scgl_project_wip_account_id`
(705 / 706), with `web_studio` 18.0.1.0 installed and 341 `web_studio` xmlids.

### C-14 — CHALLENGED. `l10n_th 18.0.2.0` does not supply the WHT mechanism. Four OCA/Ecosoft modules do.

The task framing, and any inference from "l10n_th is installed", conflate two different things.

```
PATH SET A1 /l10n_th : 17 files. models/{template_th, account_move, ir_actions_report, res_bank, res_partner}.py
                       __manifest__.py 'version': '2.0'   (-> latest_version 18.0.2.0)
grep "withholding.tax.cert" over all 797 A1 modules, *.py  -> 0 hits
grep "account.withholding.tax" over all 797 A1 modules      -> 0 hits
ir_module_module: l10n_th 18.0.2.0, author "Almacom (http://almacom.co.th/)"
```
`l10n_th` is a chart-of-accounts + EMV QR + report-layout module. It contains no WHT code.

Ownership resolved from `ir_model_data`, `model='ir.model'`:
```
l10n_th_withholding_tax           -> model_account_withholding_tax        (ir.model 908)
l10n_th_withholding_tax_cert      -> model_withholding_tax_cert           (909)
                                     model_withholding_tax_cert_line      (910)
                                     model_create_withholding_tax_cert    (911)
l10n_th_withholding_tax_cert_form -> model_report_withholding_tax_pdf     (912)
l10n_th_withholding_tax_report    -> model_withholding_tax_report         (920)
                                     model_withholding_tax_report_wizard  (921)
```
```
ir_module_module, name matching withholding|wht  (9 rows, the full set):
  l10n_th_withholding_tax             installed  18.0.1.4      Ecosoft, OCA
  l10n_th_withholding_tax_cert        installed  18.0.1.3      Ecosoft, OCA, SCG
  l10n_th_withholding_tax_cert_form   installed  18.0.1.0.2    Ecosoft, OCA, SCG
  l10n_th_withholding_tax_report      installed  18.0.1.0.1    Ecosoft, OCA
  l10n_th_withholding_tax_multi       UNINSTALLED              Ecosoft, OCA
  l10n_ar_withholding / l10n_in_withholding / l10n_in_withholding_payment / l10n_it_edi_withholding  uninstalled
```
Version-matching source exists for all four, inside the declared R4 path set
`/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/smeplus-custom/addons/`
(manifest sweep over 127 candidate dirs on `/Volumes/iMacSys` and `$HOME` excluding `~/Library`).

### C-15 — MECHANISM EXISTENCE, kept separate from reachability.

**Deployed mechanism** (read from PATH SET C, version-matched):
1. `account.withholding.tax` — rate record. `account_id` domain `[('wt_account','=',True)]`
   (`account_account.wt_account` is a real column in this archive), `type` sale/purchase/none,
   `amount` %, `tax_tag_ids`, `company_id`.
2. `account.move.line.wt_tax_id` — WHT rate carried on the **bill line**.
3. `account.payment.register` (`wizard/account_payment_register.py`) — on registering from
   `account.move.line`, computes `amount_wt = Σ(wt_tax_id.amount / 100 * price_subtotal)`,
   reduces `amount`, forces `payment_difference_handling='reconcile'`, sets
   `writeoff_account_id = wt_tax_id.account_id` and stamps the WHT tax tags on the write-off line.
4. `account.payment.wt_tax_id` — "*Optional hidden field to keep wt_tax. Useful for case 1 tax only*".
5. `withholding.tax.cert` + `.line`, produced by the `create.withholding.tax.cert` wizard.
6. `l10n_th_withholding_tax_multi` **uninstalled** → **one WHT rate per payment only**.

**A second, separate implementation exists on this host and is NOT deployed here.**
`scgl_wht_control` ("SCGL WHT Control") has source at two locations, one of them a whole project
tree `/Volumes/iMacSys/97_OCC_PROJECT_WHT_CONTROL/`. It does **not appear in
`ir_module_module` at all** in this database — not installed, not uninstalled, never on the
addons path. EXISTS, NOT DEPLOYED.

Whether the deployed OCA stack is the same mechanism a prior process analysed as a "series-16
custom wizard" I **cannot decide from this evidence base**. What I can state: series-16 copies of
these same OCA modules exist on this host (`ODOO/ODOO-COMMUNITY/Odoo16/addons/l10n_th_withholding_tax`
16.0.1.0.1, `.../l10n_th_withholding_tax_cert` 14.0.1.0.0), so a series-16 finding may well concern
an *earlier version of this same OCA family* rather than a bespoke wizard. Settling it requires
reading that process's register and status field, not its summary. **EVIDENCE REQUIRED NEXT.**

### C-16 — MECHANISM REACHABILITY. The certificate layer is populated; the tax-application layer has never run on a payment.

`account_payment`, 3,508 rows, NF uniform at 35:
```
partner_type   supplier 1,183   customer 2,325
state          paid 3,504   in_process 4
company        co1 1,899   co2 1,609        (co3, co4: zero)

wt_tax_id (f33) NOT NULL          0 of 3,508      and 0 of 1,183 supplier payments
is_multi_deduction (f35) = t      0 of 3,508      (consistent with the multi module uninstalled)
wt_cert_cancel (f34) = t      3,181 of 3,508  ->  327 payments hold a live cert
```
`account_move_line.wt_tax_id` (f61) NOT NULL = **4 of 40,353**, with positive controls in the
same pass: `purchase_line_id` 2,606, `product_id` 7,963, `payment_id` 7,430
(and `expense_id` 0, `vehicle_id` 0 — two further real zeros in adjacent columns).
The four:
```
aml 83601 move 28220 journal 34 (AP co1) account 288 wt_tax_id=3 debit 7,090.00  2026-08-29
aml 83214 move 28111 journal 34 (AP co1) account 186 wt_tax_id=7 debit 8,000.00  2026-08-30
aml 83345 move 28136 journal 10 (AP co2) account  75 wt_tax_id=3 debit 7,000.00  2026-08-27
aml 53623 move 18655 journal 10 (AP co2) account 420 wt_tax_id=3 debit 7,321.25  2026-08-25
```
All four are vendor-bill expense lines from the last week of the dataset. **None reached a payment.**

`account.withholding.tax`, 40 rows — all `type='purchase'`; rates 1/2/3/5 %; 16 active, 24 inactive;
by company co1 8, co2 16, co3 8, co4 8; accounts 65 / 103 / 179 (and co4's), all `232000 Withholding Tax`.

`withholding.tax.cert`, 332 rows:
```
state            done 327, cancel 3, draft 2
income_tax_form  pnd53 205, pnd3 125, NULL 2
tax_payer        withholding 332 (all)
company          co1 193, co2 139
payment_id       327 non-null, 327 distinct  (= 3,508 - 3,181 exactly)
date range          2026-01-03 .. 2026-08-29
create_date range   2026-08-25 20:42:19 .. 2026-08-29 07:48:11
create_uid       uid 1 -> 328,  uid 127 -> 3,  uid 117 -> 1
ir_model_data module occ_mig, model withholding.tax.cert -> 328 external IDs
```
Every certificate carries a business date spread over eight months and a creation timestamp
inside a five-day window, 328 of them under uid 1 with a migration external ID. The register was
**bulk-loaded**, not produced by day-to-day operation. Four certs were created by real users.

`withholding.tax.cert.line`, 348 rows:
```
wt_cert_income_type   '5' 332,  '6' 16
wt_percent            3% 217,  1% 97,  5% 32,  0% 2
SUM(base)    10,755,666.83      SUM(amount)   160,338.51
             by cert state: done 158,483.71 (co1 94,020.37 + co2 64,463.34); cancel 1,383.80; draft 21.00
ref_move_line_id NOT NULL    1 of 348
one line has a cert_id absent from withholding_tax_cert (450.00)
|base * pct/100 - amount| > 0.01 on 1 of 348
```

### C-17 — RISKY. WHT reaches the ledger, but by a route that leaves the module's own audit trail empty, and it does not reach the PND-specific accounts.

Journal items on WHT-related accounts (awk, field 7; debit f34, credit f35):
```
account 179  232000 Withholding Tax  co1   206 items  debit 85,988.54  credit 94,704.16   192 carry a payment_id
account  65  232000 Withholding Tax  co2   152 items  debit 56,582.89  credit 64,715.51   138 carry a payment_id
account 103 (co3), 141 (co4)                 0 items
Thai-COA WHT payable accounts:
  co1 250 214001 PND1 -> 0    251 214002 PND3 -> 0    252 214003 PND53 -> 0
  co2 382 / 383 / 384          -> 0 / 0 / 0
  co3 507 / 508 / 509          -> 0 / 0 / 0
  co4 624 / 625 / 626          -> 0 / 0 / 0
journal split, accounts 179 + 65: 59 KAS2 bank co1 (191), 69 KAS1 bank co2 (132),
  34 AP co1 (14), 10 AP co2 (14), 70 SIC1 bank co2 (5), 54 SCB1 bank co1 (1), 68 BKK3 bank co2 (1)
all 358 items parent_state = posted
```
Three observations, each separable:

1. **The applied-WHT route is not the module's route.** 358 items sit on the generic
   `232000 Withholding Tax` accounts, 330 of them raised in **bank** journals at payment time.
   If the `account.payment.register` mechanism had produced them, the payments would carry
   `wt_tax_id`. Zero of 3,508 do. So the amounts were entered by some other path — bank-side
   write-off, manual entry, or migration — and the module's own payment→tax linkage is empty.
2. **The PND-specific liability accounts carry nothing.** `214001 / 214002 / 214003`
   (ภาษีหัก ณ ที่จ่ายค้างจ่าย ภ.ง.ด.1 / ภ.ง.ด.3 / ภ.ง.ด.53) exist in all four charts and hold
   zero items, while the certificate register classifies 330 of 332 certs as pnd3 or pnd53.
   The form classification lives only in the certificate register, not in the ledger.
3. **Register and ledger do not tie.**
   ```
   cert lines, state=done, WHT amount        158,483.71   (co1 94,020.37 + co2 64,463.34)
   GL gross credits, accounts 179 + 65       159,419.67   (co1 94,704.16 + co2 64,715.51)
   difference                                     935.96   (co1 683.79 + co2 252.17)  = 0.59%
   ```
   Both figures are enumerated from rows, not re-derived from a total.

Whether any of the three is a compliance defect requires statutory authority I do not hold.
**HOLD — STATUTORY EVIDENCE REQUIRED. Routed to P07.** Specifically: (a) whether a WHT credit
posted to a generic `232000` account rather than the PND-keyed liability accounts satisfies Thai
filing requirements; (b) whether a certificate register that cannot be traced to its journal
items (`ref_move_line_id` populated on 1 of 348) meets the record-keeping standard; (c) whether
the ฿935.96 register-to-ledger difference is material.

### C-18 — SUPPORTED for what is measured, NOT DECIDABLE for one ratio. Observable WHT on supplier payments, with denominators, no conclusion attached.
```
supplier payments                                        1,183  of 3,508 (33.7%)
  with account.payment.wt_tax_id set                         0  of 1,183   (0.00%)
  with a live (non-cancelled) WHT certificate         <=    327 of 3,508 payments overall;
     certs are not split by partner_type in the cert table, so the supplier-only
     subset is NOT DECIDABLE from the tables extracted. See §6.
vendor-bill lines carrying account.move.line.wt_tax_id       4  of 40,353 lines (0.0099%)
payments in companies 3 and 4                                0  (both companies hold zero moves)
WHT rate records applicable to purchases                    40  (16 active), all type='purchase'
```

---

## 5. STATUS OF EACH FROZEN FINDING I TESTED

| Frozen | Verdict | Basis |
|---|---|---|
| S18-02 valuation 126/126 × 4/4 `manual_periodic` | **SUPPORTED** | C-03, reproduced independently across all 504 pairs |
| S18-03 zero SVL→GL link | **SUPPORTED** | C-12a, awk + NF control, both companies |
| S18-05 "configured on 15 of 126" | **CHALLENGED** | C-01: 126/126 in company 1; 171 of 504 pairs |
| S18-05 "co2/co3 false, co4 no row" as a distinction | **CHALLENGED** | C-02: behaviourally identical |
| S18-05 accounts 176/62/100/138 → 0 items | **SUPPORTED** | C-12a, three methods + injection control |
| S18-05 journals 16/24/32/40 → 0 items | **SUPPORTED** | C-12a |
| S18-06 "bill-line override is v19-only" | **CHALLENGED** | C-10: present in v18 `account_move.py:255-274` |
| S18-06 no bill line posts to a clearing account | **SUPPORTED**, wrong cause | C-10 |
| S18-07 no accrual entries exist | **SUPPORTED**, stronger control | C-06 |
| S18-07 exposure framed as unreachable | **CHALLENGED** | C-05, C-07, C-08, C-09 |
| S18-11 "16 installed custom modules" | **CHALLENGED** | C-13: 55 non-core; A2 root undeclared |
| S18-12 the guard is vacuous for 110/126 | not re-tested; its explicit property-field check **corroborated** | C-11 |
| Bounded absence: landed costs | **SUPPORTED** | C-09, two independent confirmations |
| Bounded absence: `ir_property` | not tested | — |

---

## 6. EVIDENCE REQUIRED NEXT

1. **C-04's unmeasured clause.** Who can write `product.category.property_valuation` in company 1?
   Needs `ir_model_access`, `ir_rule`, `res_groups_users_rel` resolved against
   `stock.group_stock_manager` / `account.group_account_manager`. Until measured, C-04 is a
   capability, not a live exposure. I am flagging this explicitly because the well-evidenced half
   of C-04 makes the unmeasured half feel safe.
2. **C-18's undecidable line.** Split the 327 certificate-bearing payments by `partner_type`
   via `withholding_tax_cert.payment_id` → `account_payment.partner_type`. Both tables are
   extracted; the join was not run. Do not report a supplier-only WHT coverage ratio until it is.
3. **C-15's open comparison.** Read the prior P01 register and its status field — not its
   summary — to determine whether its "series-16 custom wizard" is this OCA family at 16.0.1.0.1
   or a distinct implementation. Do not adopt either reading before that.
4. **C-13's consequence.** 55 installed modules have no source in either declared root. Every
   negative source claim in the frozen package is bounded by that gap. The next step is a
   version-matched source census over all 55, not over the 16.
5. **The 39 unenumerated modules as writers.** `om_data_remove`, `account_payment_multi_deduction`,
   `hr_expense_petty_cash`, `full_summarize_bills`, `bi_print_journal_entries`,
   `journal_entries_report`, `print_voucher_request` all touch accounting objects and none was
   swept by C-11's name-scoped PATH SET B.
6. **Studio surface.** `res_company.x_scgl_wip_control_enabled` / `x_scgl_project_wip_account_id`
   (accounts 705 / 706) are Studio fields on companies 3 and 4. Inert today because those
   companies hold zero moves. Enumerate the full Studio field set on accounting models.
7. **P07 routing.** C-17 (a), (b), (c) as stated.

---

## 7. PRE-COMMIT SWEEP

Four checks with disjoint units, run over this document before submission.

1. **Identifier check (unit: identifier).** Defined `C-01 … C-18`, plus `C-12a` and `C-12b`.
   Cited: the same set, no others. No orphan `C-` reference. Peer families cited by name only
   (S18-xx belong to the frozen brief; P01 and P07 are peer processes).
2. **Negative-claim check (unit: negative statement).** Every zero in this report carries a
   named positive control from the *same pass*: C-06 (`reversal` 119), C-11 (`account.move` 98 /
   `account_id` 75 / `product.category` 16), C-12a (account 169 = 2,940; 144 distinct accounts;
   injection 0→2), C-16 (`purchase_line_id` 2,606 / `product_id` 7,963 / `payment_id` 7,430),
   §0 (COPY-header discriminator, absent vs empty).
3. **Arithmetic check (unit: figure).** Every total is enumerated from rows, none re-derived.
   Independently re-added here: 94,020.37 + 64,463.34 = 158,483.71. 94,704.16 + 64,715.51 =
   159,419.67. 159,419.67 − 158,483.71 = 935.96. 683.79 + 252.17 = 935.96. 3,508 − 3,181 = 327,
   and `distinct payment_id` on live certs = 327. 23,943 + 20,992 = 44,935. 15 × 4 + 111 = 171.
   25,166 + 15,187 = 40,353. 36,805 + 3,540 + 8 = 40,353.
4. **Unit check (unit: claim-unit vs measurement-unit).** C-01 measures (category, company) pairs
   because the field is company-dependent. C-12a measures journal items. C-16 measures payments
   and lines separately, never conflated. C-18 states its denominator on every line, and marks
   the one ratio whose denominator is not yet established as NOT DECIDABLE rather than estimating it.

No binary verdict word is used anywhere in this report. Disagreement with the frozen package is preserved as stated,
not reconciled.
