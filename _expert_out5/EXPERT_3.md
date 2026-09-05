# AAS-03 EXPERT 3 — LEAD INTEGRATION & LOCALIZATION
## Adversarial challenge of the frozen P01 series-16 package (`s16/brief/FINDINGS.md`)
Scope: Thai withholding-tax (WHT) mechanism on deployment `iSMEs_2026-07-11_05-03-27.dump`
(`database.uuid 45a8e08e-5dcd-11ee-90f5-5242ea102159`, `web.base.url https://swr.smeplus.asia`).
READ-ONLY. No database written, no source modified, no server run, no external network used.

---

## 0. DECLARED BOUNDARIES

**POPULATION (runtime).** The single archive named in the brief,
`~/Downloads/iSMEs_2026-07-11_05-03-27.dump`. Every count below is over a whole table extracted
from that archive, never a sample. Table row counts are stated with the archive's own totals.

**PATH SET (source).** Two sets, declared separately and both executed:
- **PS-1 (whole host):** `../src_paths.json` / `../src_versions.json` — 3,174 module names,
  58,263 manifests. Used to enumerate *every* candidate copy of the four deployed WHT modules.
- **PS-2 (deployment-adjacent tree):** `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/{addons,swr}`
  — 61 module directories. Selected **after** PS-1 discriminated it, not by convenience.

**PATTERN.** Declared and executed at each step; commands and outputs are quoted inline.
Grep patterns carry a positive control (a token that must hit) and a negative control (a token
that must not).

**UNIT.** Stated per claim. Units used: *module directory*, *distinct `.py` content variant*,
*`account_payment` row*, *`account_move` row*, *`account_move_line` row*, *`withholding_tax_cert`
row*, *`withholding_tax_cert_line` row*, *product template*. These are **not** interchangeable
and each claim below names its own.

**COVERAGE ASSERTION for the derived projections** (`E3_am.tsv`, `E3_aml.tsv`):
```
E3_am.tsv rows=183590   (archive account_move rows=183590)
E3_aml.tsv rows=447384  (archive account_move_line rows=447384)
aml rows whose move_id is NOT in am = 0
NF integrity: account_move_line NF=67 rows=447384 (single value)
              account_move      NF=85 rows=183590 (single value)
              account_payment   NF=36 rows=22468  (single value)
              withholding_tax_cert NF=19 rows=5201 (single value)
```
**POSITIVE CONTROL on column mapping** — cert line 3 records `ref_move_line_id=2774`,
`base 2500, wt_percent 3, amount 75`. Independently projected row 2774:
```
['2774','1299','1137','75',...,'posted','product','2023-10-12','0.00','75.00','-75.00','0.00','2',...]
      id  move  acct 1137   state   dtype      date        Dr      Cr      balance  subtot wt_tax_id
```
account 1137, credit 75.00 — mapping confirmed.
**POSITIVE CONTROL 2** — sum of product-line `price_subtotal` == `account_move.amount_untaxed`
for **36,867 of 36,867** posted `in_invoice` moves, 0 differ.
**NEGATIVE CONTROL** — lookup of a non-existent id returns `None`.
**SYNTHETIC INJECTION CONTROL** — injecting one row with `wt_tax_id='3'` moves the predicate
count 17,878 → 17,879. The filter can fire.

**STATUTORY BOUNDARY.** Everything below headed *Source Behaviour* or measured from the archive is
observed system behaviour. **Nothing below states what Thai law requires.** Items whose resolution
needs statutory authority are marked `UNRESOLVED — STATUTORY EVIDENCE REQUIRED` and routed to P07.

---

## 1. ASSIGNMENT 1 — DISPROVE THAT THE DEPLOYED WHT MECHANISM IS THE ONE P01 PREVIOUSLY ANALYSED

### 1.1 The four deployed modules and their candidate populations

Deployed versions, read from the archive (`s16/installed.txt`, 189 rows + 1 NULL):
```
l10n_th_withholding_tax            16.0.1.0.1
l10n_th_withholding_tax_cert       16.0.14.0.1.0.0
l10n_th_withholding_tax_cert_form  16.0.1.0.1
l10n_th_withholding_tax_report     16.0.1.0.0
```
`adapt_version` (`odoo/modules/module.py`) is an unconditional series prefix, so I enumerated
**every** path in PS-1 for each module name, read each `__manifest__.py`, applied `adapt_version`
with serie `16.0`, and kept only exact matches. Command output:
```
l10n_th_withholding_tax            deployed=16.0.1.0.1        candidates=6  / population=61 paths
l10n_th_withholding_tax_cert       deployed=16.0.14.0.1.0.0   candidates=15 / population=49 paths
l10n_th_withholding_tax_cert_form  deployed=16.0.1.0.1        candidates=9  / population=43 paths
l10n_th_withholding_tax_report     deployed=16.0.1.0.0        candidates=8  / population=35 paths
TOTAL CANDIDATES 38
```

### E3-F-01 — **CHALLENGED.** A version match does not identify the code for two of the four modules.
**UNIT: distinct `.py` content variant** (hash over all `.py` under the module, excluding
`.git/`, `__pycache__/`, `tests/`, `static/`, `i18n/`, `readme/`).
```
l10n_th_withholding_tax           version-matching copies=6   DISTINCT .py VARIANTS=1
l10n_th_withholding_tax_cert      version-matching copies=15  DISTINCT .py VARIANTS=4
l10n_th_withholding_tax_cert_form version-matching copies=9   DISTINCT .py VARIANTS=1
l10n_th_withholding_tax_report    version-matching copies=8   DISTINCT .py VARIANTS=6
```
The brief's identification method ("165 of 190 deployed modules have a version-matching copy on
this host") is sound for `l10n_th_withholding_tax` and `..._cert_form` — one content variant each,
so the version *does* pin the code. It is **not** sound for `..._cert` (4 variants share the one
version string) or `..._report` (**6 variants share the one version string**, and two of the eight
matching copies sit in an **Odoo 14** tree and an **ODOO 12** tree). For `..._report` the manifest
version is literally `'version': '1.0.0'` with a stale comment `# version 14.0.1.0.0`, so
`adapt_version` manufactures `16.0.1.0.0` out of a string that carries no series at all.

This is not a defect in the brief's arithmetic; it is a limit on what that arithmetic can conclude,
and the brief does not state the limit. **I do not accept "version-matching copy exists" as
"the deployed code is identified" for these two modules, and I did not rely on it.**

### E3-F-02 — **SUPPORTED.** The deployed cert module is identified by the deployed *registry*, not by its version.
The four `..._cert` variants differ. I discriminated them against the archive's own
`ir_model_fields`, i.e. the model as the deployment actually built it:
```
sig=1  pdate=1 movetype=1  /Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/swr/l10n_th_withholding_tax_cert
sig=0  pdate=1 movetype=0  .../ODOO 14/.../WITHHOLDING TAX/l10n_th_withholding_tax_cert
sig=0  pdate=1 movetype=1  .../ODOO 14/.../landed-cost-migration-14.0 2/...-14.0.1.0.0/l10n_th_withholding_tax_cert
sig=0  pdate=1 movetype=1  .../ODOO 14/.../landed-cost-migration-14.0/..._cert_form-13.0.1.0.2/l10n_th_withholding_tax_cert
```
Archive registry, model `withholding.tax.cert`:
```
    signature | binary | store= t | req= f
```
Only one of the four variants declares `signature`. The deployment has it. **The deployed cert
module is the `Odoo16/swr` variant (md5 `a2e964f437ff`, 5 copies on this host).**
This is a discriminating identification, not a convenience choice.

### E3-F-03 — **SUPPORTED.** The deployed cert module is the 2021 Odoo-14.0 source, plus one field.
Per-file `diff` between the deployed variant and the pure Odoo-14 copy
(`.../landed-cost-migration-14.0 2/l10n_th_withholding_tax_cert-14.0.1.0.0/`, file mtime
2021-05-12):
```
--- .../Odoo16/swr/.../models/withholding_tax_cert.py            2026-07-06
+++ .../ODOO 14/.../l10n_th_withholding_tax_cert/models/withholding_tax_cert.py  2021-05-12
@@ -187,7 +187,6 @@
-    signature = fields.Binary()
models/account_payment.py            (no differences)
models/account_move.py               (no differences)
wizard/create_withholding_tax_cert.py(no differences)
__init__.py, models/__init__.py, wizard/__init__.py (no differences)
```
Apart from one added `Binary` field, **the certificate engine running this deployment is byte-for-byte
the 2021 series-14 source.** The `16.0.` in `16.0.14.0.1.0.0` is a loader prefix, nothing more.

### E3-F-04 — **RISKY (latent, measured as never fired).** A series-14 API call survives in the deployed cert code.
`models/withholding_tax_cert.py:212`:
```python
if record.move_id and record.move_id.type == "entry":
```
`type` was renamed `move_type` on `account.move` in series 14→16. Checked against the deployment's
own registry, **not** against source:
```
account.move field rows: 183
account.move has a field literally named type? -> []
  move_type | selection | store=t | state=base
```
There is no `type` field on `account.move` in this deployment. The expression is guarded by
`record.move_id and ...`, so it is only reached when a certificate is created from a journal entry.
Measured (UNIT = `withholding_tax_cert` row, POPULATION = all 5,201):
```
anchor: payment_id set=3794  move_id set=0  both=0  neither=1407
```
**`move_id` is NULL on all 5,201 rows.** Per the latent-vs-live rule: the defect is real in the
deployed source and has **never fired**, because the journal-entry certificate route has never been
used. It is a live hazard the first time an operator uses that route, not a historical error.

### E3-F-05 — **CHALLENGED / EVIDENCE REQUIRED.** The report module's deployed code is not identified by any SHA or version.
`l10n_th_withholding_tax_report` in the deployment-adjacent tree is a **dirty git working tree**:
```
--- dirty? ---
 M models/ir_actions_report.py
 M models/report_withholding_tax.py
 M report/report_withholding_tax_xlsx.py
?? models/report_withholding_tax.py_bkp
git diff --stat:  3 files changed, 246 insertions(+), 134 deletions(-)
HEAD: dca2be519a7005d2c8f6170d23a25fb4949d7fe7  Wed Apr 26 13:36:01 2023 +0700  "migration"
manifest 'version' at HEAD:          '1.0.0'   # version 14.0.1.0.0
manifest 'version' in working tree:  '1.0.0'   # version 14.0.1.0.0
working-tree mtimes: 2026-07-06 15:04 (all three modified files + the .py_bkp)
```
246 inserted lines, **version string unchanged**, **nothing committed**. The archive was created
**2026-07-11 05:03:27**; the working-tree files are dated **2026-07-06**. So the tree is
*plausibly* contemporaneous but I cannot prove it is what was loaded: the deployment records only
`16.0.1.0.0`, which both the 2023 commit and the 2026 working tree satisfy. **The deployed
`l10n_th_withholding_tax_report` code is NOT identified by any evidence available to me.** Findings
E3-F-16..E3-F-19 below are therefore stated as *properties of the on-disk 2026-07-06 working tree*,
explicitly not as properties of the deployment. Routed to EVIDENCE REQUIRED NEXT.

### E3-F-06 — **SUPPORTED.** The deployment-adjacent tree is a *later* working copy, not a deployment snapshot.
I intersected PS-2 with the archive's installed-module list rather than trusting directory names
(memory rule: declared set vs deployed set).
```
installed=190  tree_dirs=61   installed AND in tree = 45
in tree but NOT installed = 16 (amount_in_words_thai, cheque_control, footer_layout,
  gsk_automatic_mail_server, hr_expense_petty_cash(+_sequence), hr_expense_sequence,
  import_bridge_axis, pos_multi_uom_price, print_payment_remittance_adviec,
  scgl_import_product_images(+.zip), scgl_invoice_translated,
  scgl_swr_payment_term(+.zip), stock_lot_active.zip)
version-match=43  mismatch=2  no-manifest=0  of 45
  MISMATCH po_request_py3o        tree=16.0.1.6    db=16.0.1.5
  MISMATCH scgl_swr_custom_module tree=16.0.1.0.1  db=16.0.1.0.0
```
The tree is **ahead** of the deployment on two modules, one of which (`scgl_swr_custom_module`) is
an SWR-specific customisation. It is the best available source, and it is not a snapshot.

### 1.2 The withholding arithmetic — full base, not prorated

**Source Behaviour.** `l10n_th_withholding_tax/wizard/account_payment_register.py:42-54`
(single content variant across all 6 version-matching copies — E3-F-01):
```python
@api.depends("source_amount","source_amount_currency","source_currency_id",
             "company_id","currency_id","payment_date")
def _compute_amount(self):
    res = super()._compute_amount()
    if self._context.get("active_model") == "account.move":
        active_ids = self._context.get("active_ids", [])
        invoices = self.env["account.move"].browse(active_ids)
        inv_lines = invoices.mapped("invoice_line_ids").filtered("wt_tax_id")
        amount_wt = sum(
            inv_lines.mapped(lambda l: l.wt_tax_id.amount / 100 * l.price_subtotal)
        )
        if amount_wt:
            self._update_payment_register(amount_wt, inv_lines)
    return res

def _update_payment_register(self, amount_wt, inv_lines):
    self.amount -= amount_wt
    self.payment_difference_handling = "reconcile"
    ...
```

### E3-F-07 — **SUPPORTED (source).** Withholding is computed on the **full invoice-line base**, never prorated to the payment.
`l.price_subtotal` is the whole invoice line. `super()._compute_amount()` has just set `self.amount`
to the **residual** to settle. The subtraction therefore deducts 100% of the invoice's withholding
from whatever fraction of the invoice is being paid. There is no residual ratio, no
`amount_residual` term, no proration anywhere in the expression. The identical expression is
repeated in `models/account_move.py:41-43` for the stored `wht_amount` field.

### E3-F-08 — **SUPPORTED.** The deployed data **does** contain partial payments, including on WHT-bearing bills.
UNIT = vendor bill (`in_invoice` move), POPULATION = `account_partial_reconcile` (63,773 rows).
```
vendor bills (in_invoice) touched by >=1 partial reconcile = 36429
distinct settling counterparties per bill: {1: 36149, 2: 277, 3: 2, 4: 1}
bills settled by MORE THAN ONE counterparty = 280 (0.77%)
vendor bills carrying >=1 wt line = 1929 ; of those, multi-settled = 3
```
So the answer to "does the deployed data show partial payments at all" is **yes, 280 bills**, and
**3 of them carry withholding**. The exposure surface is live but small.

### E3-F-09 — **CHALLENGED. The full-base defect did NOT fire on the observed partial payments — because the amount did not come from the module's arithmetic at all.**
The two clean cases (the third, move 110411, I discard: its partial amounts exceed the bill total,
so my pairing for that bill is unreliable and I will not build a claim on it):
```
=== bill move_id=9450  untaxed=465600.00 total=498192.00 stored_wht=13968 date=2023-12-08
    wt line 26981: subtotal=465600.00 wt_tax_id=2 (WHT3%, master rate now 0.0)
    settled by payment_id=2416 (2023-12-25) and payment_id=4972 (2024-03-27)

=== payment 2416  move=10708 amount=242112.00 wt_tax_id=NULL
     acct 1137  2260000 Withholding Tax             Dr=0.00       Cr=6984.00
     acct 33    111003 Outstanding Payments         Dr=0.00       Cr=242112.00
     acct 1282  2217000 Accounting Payable-Domestic Dr=249096.00  Cr=0.00
=== payment 4972  move=68908 amount=242112.00 wt_tax_id=2
     acct 1282  2217000 Accounting Payable-Domestic Dr=249096.00  Cr=0.00
     acct 1137  2260000 Withholding Tax             Dr=0.00       Cr=6984.00
     acct 33    111003 Outstanding Payments         Dr=0.00       Cr=242112.00
```
Each payment settled exactly half the bill (249,096.00 × 2 = 498,192.00 = the total) and withheld
exactly half the withholding (6,984.00 × 2 = 13,968.00 = 3% of 465,600.00). **That is prorated,
which the code cannot produce.** Worse, payment 4972 posted a 3% withholding on **2024-03-27**,
three months *after* the master rate for `wt_tax_id=2` was written down to 0 (below). The module's
expression `wt_tax_id.amount/100 * price_subtotal` evaluates to **0.00** for that payment.

**I therefore do not publish "withholding is computed on the full base per partial payment" as an
observed behaviour of this deployment.** The source computes that way; the ledger does not reflect
it; and the reason is E3-F-10, which is a larger finding than the one I was sent to test.

### E3-F-10 — **SUPPORTED. The withholding amount posted to the ledger is operator-determined, not rate-derived. Measured on 1,854 payments.**
`account_withholding_tax` — the entire master table, 7 rows:
```
id  acct  name      amount  create_date          write_date
5   1137  WHT15%    15      2023-10-04 02:12:18  2023-10-04 02:12:27
1   1137  WHT1%     1       2023-09-15 04:20:54  2023-10-04 02:12:36
3   1137  WHT5%     5       2023-09-15 04:21:41  2023-10-04 02:12:47
6   1137  WHT10%    10      2023-10-04 02:13:03  2023-10-04 02:13:03
4   1137  WHT0.5%   0.5     2023-09-21 01:54:27  2023-10-20 06:40:14
7   1137  WHT2%     2       2023-11-08 08:25:09  2023-11-08 08:25:33
2   1137  WHT3%     0       2023-09-15 04:21:10  2023-12-29 02:59:30   <-- rate 0, named "3%"
```
**`WHT3%` carries `amount = 0`, last written 2023-12-29 02:59:30 by uid 26.**

DISCRIMINATING TEST. UNIT = `account_payment` row. POPULATION = all 4,945 payments with
`wt_tax_id` non-NULL. PREDICTION if the posted WHT comes from `account_withholding_tax.amount`:
a `wt_tax_id=2` payment posts **zero** WHT to account 1137.
```
  wt_id  name      payments     WHT!=0     WHT==0     sum posted WHT   master rate
  2      WHT3%         2038       2022         16      1621903.01      0
  4      WHT0.5%       1501       1483         18     18360296.76      0.5
  1      WHT1%         1333       1331          2      2307564.10      1
  3      WHT5%           57         48          9        63295.65      5
  7      WHT2%           10         10          0         2203.20      2
  5      WHT15%           3          3          0         9564.37      15
  6      WHT10%           3          2          1        17482.33      10

  wt_tax_id=2 payments CREATED ON/AFTER the 2023-12-29 rate write: 1867
  of those posting NON-ZERO WHT: 1854 (99.30%)   total = 1,440,563.92
```
**1,854 payments created after the rate went to zero posted ฿1,440,563.92 of withholding that the
master rate cannot produce.** The mechanism is visible in the source: the wizard sets
`payment_difference_handling = "reconcile"` and the operator types the net cash `amount`; the
difference is written off to `wt_tax_id.account_id`. The rate is a *suggested default*, and the
suggestion here is zero. The `wt_tax_id` field is fully editable on the wizard —
`wizard/account_payment_register_views.xml` places it with only
`attrs="{'invisible': [('payment_difference_handling','!=','reconcile')]}"`.

**NEGATIVE CONTROL** — payments with `wt_tax_id` NULL that nevertheless credit account 1137:
**294**. The withholding account is reachable entirely outside the WHT module's own field.

**This challenges the framing of the assignment.** The question "is withholding computed on the
full base or prorated" presupposes that the module computes it. On the measured evidence it
largely does not. I preserve the disagreement rather than resolve it: E3-F-07 (source computes
full-base) and E3-F-09/E3-F-10 (the ledger amounts are not the source's output) are both true and
they do not reconcile into a single statement about "the deployed WHT mechanism".

### E3-F-11 — **SUPPORTED (source), small measured footprint.** `_compute_wht_amount` assigns to the recordset, not the record.
`l10n_th_withholding_tax/models/account_move.py:36-44`:
```python
@api.depends("invoice_line_ids")
def _compute_wht_amount(self):
    self.wht_amount = 0
    for rec in self:
        inv_lines = rec.invoice_line_ids.filtered("wt_tax_id")
        amount_wt = sum(inv_lines.mapped(lambda l: l.wt_tax_id.amount/100 * l.price_subtotal))
        self.wht_amount = amount_wt        # <-- `self`, not `rec`
```
In a multi-record recompute every record in the batch receives the **last** record's value.
`wht_amount` is `store=True` (confirmed in the archive registry) and `invisible="1"` in the form
view, so no operator ever sees it. Measured, UNIT = invoice-type `account_move` row:
```
POPULATION: invoice-type account_move rows = 39779
stored wht_amount == recomputed at current rates: match=39572  mismatch=207 (0.52%)
  of the mismatches: stored=0 but calc!=0 -> 1 ; stored!=0 but calc==0 -> 158 ; both nonzero&differ -> 48
SMOKING-GUN TEST: invoice moves with ZERO wt-bearing lines = 37840
  of those, stored wht_amount != 0 = 7 (0.02%)   sum = 3,259.87
POSITIVE CONTROL: invoice moves WITH >=1 wt line = 1939 ; stored wht_amount != 0 = 1179
```
**The source defect is certain. Its measured footprint is 7 moves / ฿3,259.87, and I cannot
separate "cross-record leak" from "line deleted after the compute" without runtime.** I record it
at that size and do not inflate it. The 158 "stored≠0 but recompute=0" cases are the E3-F-10
rate-change footprint, not this bug: any future retrigger of `_compute_wht_amount` on those moves
will silently rewrite ฿-values to 0.

---

## 2. ASSIGNMENT 2 — DISPROVE THAT WHT IS CORRECTLY SCOPED TO APPLICABLE PURCHASES

I did **not** assume withholding excludes goods. I measured what it is applied to.

### E3-F-12 — **SUPPORTED.** Withholding is applied to goods and stock purchases in this deployment.
UNIT = `account_move_line` row. POPULATION = all 447,384.
```
account_move_line rows with wt_tax_id NOT NULL = 17878 of 447384 (3.996%)
by parent move_type: {'entry': 15219, 'in_invoice': 2605, 'in_refund': 54}
by parent_state:     {'posted': 17402, 'cancel': 475, 'draft': 1}
by display_type:     {'product': 17878}
payment_id set on the line: 15213
```
Restricting to vendor-bill lines (the scoping decision point):
```
wt-bearing lines on in_invoice/in_refund = 2659
  display_type='product' = 2659 ; with product_id = 2516 ; WITHOUT product_id = 143

by (detailed_type, type):
    ('service','service')   2178
    ('consu','consu')        282     <-- goods
    <no product>             143
    ('product','product')     56     <-- storable stock

by product category (top):
    All / Expenses / Service                          2018
    All / Expenses / Material / Rice                   195     <-- raw material for the mill
    <no product>                                       143
    All / Expenses / Supplies                           72
    All / Expenses / Transport&Loading                  62
    All / Expenses / Spare Part&Maintenance&Project     48
    All / Expenses / IT                                  7
    All / Expenses / Stationery                          4
    All / Expenses / Material / กระดาษการ์ด TAG           3
    All / Expenses / Material / สติ๊กเกอร์+Other PKG       3
    All / Expenses / Manufacturing Cost                  1
    All / Saleable / Finished goods / Sales Revenue - Overseas  1

by account (top):
    6120002 Cost of issuing BL documents  [expense_direct_cost]  1284
    2900000 Goods Receipt Note(GRN)       [liability_current]     151   <-- the GRNI clearing account
    7260003 Maintenance & Repair          [expense]               144
    6120008 Shipping Cost - Oversea       [expense_direct_cost]   103
    ...
    7180001 Major Expense Job:MEJ         [asset_fixed]            64   <-- capitalised
    4010010 Discount on Receipt Rice Product [expense_direct_cost] 48
```
**338 goods lines (282 `consu` + 56 storable), 195 raw-rice material lines, 151 lines posting to the
GRNI clearing account 2900000, and 64 lines posting to a fixed-asset account** carry withholding
tax. The brief's S16-05 establishes that account 39 / 2900000 is the *goods receipt* bridge — so
withholding is attached to lines whose accounting treatment is a goods receipt.

**Whether withholding is properly applicable to any of these expense types is
`UNRESOLVED — STATUTORY EVIDENCE REQUIRED`. Routed to P07.** I state only that the deployment
applies it there.

### E3-F-13 — **SUPPORTED.** Scoping is not systematic: 54% of withholding lines cannot have come from configuration.
The only configured source of a withholding default is `product.template.supplier_wt_tax_id`
(`models/account_move.py:17-28`, `models/product.py`). UNIT = product template,
POPULATION = all 3,949:
```
templates with supplier_wt_tax_id set = 91 (2.30%) ; with customer wt_tax_id set = 3
  by detailed_type: {'service': 88, 'consu': 3}
  value counts:     {'2': 89, '4': 1, '1': 1}       <-- 89 of 91 point at WHT3%, master rate 0.0
ALL templates by detailed_type: {'consu':2307, 'product':1485, 'service':157}
```
UNIT = wt-bearing vendor-bill line, POPULATION = the 2,659 from E3-F-12:
```
line == product default                              1223  45.99%
line != product default (override)                    844  31.74%
product has NO supplier_wt_tax_id -> default False    449  16.89%
line has no product     -> default False              143   5.38%
=> lines whose WHT could NOT have come from the product default: 1436 (54.01%)
```
**Only 2.30% of the product catalogue is configured for withholding at all, 89 of those 91 point at
a zero rate, and 54.01% of the withholding actually applied was keyed or overridden by hand.**
The `wt_tax_id` column is `optional="show"` and editable in the invoice-line tree
(`views/account_move_view.xml`), so this is the designed behaviour, not a workaround.

### E3-F-14 — **RISKY.** The withholding path is unreachable for payments not registered from an invoice.
`_compute_amount` is gated on `self._context.get("active_model") == "account.move"`, and
`default_get` likewise. Payments created by any other route — directly on `account.payment`, from
the reconciliation widget (`active_model == 'account.move.line'`), or by import — never enter the
computation. The 294 payments in the E3-F-10 negative control that credit account 1137 with no
`wt_tax_id` are consistent with such routes, though I have not proved which route produced them.
**EVIDENCE REQUIRED NEXT.**

---

## 3. ASSIGNMENT 3 — WHAT `income_tax_form` ACTUALLY CONTAINS, AND WHETHER ANY CODE PATH DETERMINES IT

### E3-F-15 — **SUPPORTED. No code path determines `income_tax_form`. It is operator input, end to end.**
**Source Behaviour.** The only writer, `models/withholding_tax_cert.py:196-224`:
```python
@api.depends("payment_id", "move_id")
def _compute_wt_cert_data(self):
    income_tax_form = self._context.get("income_tax_form", False)
    ...
    record.update({... "income_tax_form": income_tax_form})
```
and the only source of that context key, `wizard/create_withholding_tax_cert.py:96-101`:
```python
income_tax_form = fields.Selection(selection=INCOME_TAX_FORM, string="Income Tax Form")
                                   # no default, not required
...
ctx.update({"income_tax_form": self.income_tax_form,
            "wt_cert_income_type": self.wt_cert_income_type})
```
The field is `required=True` on `withholding.tax.cert` but **optional on the wizard that fills it**.
Nothing derives it from the partner, the account, the product, the income type, or the tax record.

**Registry-wide search for any field that could hold the mapping.**
PATTERN `/wt|wht|pnd|income_tax|withhold/i` over field **name**; POPULATION = all 11,992
`ir_model_fields` rows; UNIT = field. POSITIVE CONTROL `/vat/` → 67 hits. NEGATIVE CONTROL
`/zzqqxx/` → 0 hits. Result: **32 matches**, of which the only `res.partner` hit is
`x_studio_many2one_field_wwtrJ` — a Studio-generated field matching only on the letters "wt" inside
a random suffix, i.e. a **false positive of my own pattern, not a hit**.
**There is no field anywhere in this deployment that carries a PND form or a withholding rate per
partner.**

### Contents, measured. UNIT = `withholding_tax_cert` row, POPULATION = all 5,201.
```
income_tax_form:  pnd53 4437 (85.31%)   pnd3 751 (14.44%)   pnd1 13 (0.25%)   NULL 0
state:            done 5191, cancel 5, draft 5
tax_payer:        withholding 5201 (single value)
company_id:       {'1': 5201}
create_uid:       {'27': 4870, '24': 218, '28': 107, '25': 5, '2': 1}
```
The `INCOME_TAX_FORM` selection defines four values; **`pnd3a` is never used**. The
`WHT_CERT_INCOME_TYPE` selection defines 15 values; **3 are used** (5: 4,381 lines; 6: 1,766; 2: 12).

### E3-F-16 — **SUPPORTED, and it cuts both ways.** The form is perfectly consistent per supplier and completely undefended by the system.
```
distinct suppliers appearing on certs = 506
suppliers whose certs use MORE THAN ONE income_tax_form = 0 (0.00%)
```
**Zero of 506 suppliers ever received two different PND forms across 5,201 certificates over
~3 years.** The mapping is a stable 1:1 function of the supplier — and it exists only in operator
habit. It is not derivable from the one partner attribute that might carry it:
```
income_tax_form x supplier is_company (UNIT = cert; unresolved partners = 0):
     pnd1   is_company=f     5      pnd1   is_company=t     8
     pnd3   is_company=f     2      pnd3   is_company=t   749
     pnd53  is_company=t  4437
vat present on cert suppliers: pnd1 13/13, pnd3 751/751, pnd53 4437/4437 (all set)
```
749 of 751 `pnd3` certificates and all 4,437 `pnd53` certificates are for `is_company=TRUE`
partners. **`is_company` does not separate PND3 from PND53.** The classification is reproduced from
memory 5,201 times with no stored rule, no validation, and no detection if it is ever wrong.
The correctness of any individual classification is
`UNRESOLVED — STATUTORY EVIDENCE REQUIRED`. **Routed to P07.**

### E3-F-17 — **SUPPORTED.** The same income type is filed under three different PND forms.
UNIT = cert line joined to its cert:
```
     pnd1   type=2      7        pnd1   type=5      6
     pnd3   type=5    680        pnd3   type=6     71
     pnd53  type=2      4        pnd53  type=5   3445      pnd53  type=6   1584
```
Income type 5 appears under all three forms; type 2 under pnd1 and pnd53; type 6 under pnd3 and
pnd53. No constraint relates them. Whether any of these combinations is admissible is
`UNRESOLVED — STATUTORY EVIDENCE REQUIRED`. **Routed to P07.**

---

## 4. FINDINGS OUTSIDE THE THREE ASSIGNMENTS THAT THE PACKAGE DOES NOT CARRY

### E3-F-18 — **SUPPORTED. 1,407 certificates (27.05%) are anchored to nothing in the ledger.**
UNIT = `withholding_tax_cert` row. Measured twice, by two independent tools.
Python parser:
```
anchor: payment_id set=3794  move_id set=0  both=0  neither=1407
```
Independent `awk` positive control over the raw COPY block:
```
rows=5201 payment_id NULL=1407 move_id NULL=5201 both NULL=1407
NF=19 rows=5201  (single field-count, no mis-splits)
```
Their profile:
```
by create_uid: {'27': 1378, '24': 20, '28': 9}
by year:       {'2024': 728, '2025': 334, '2026': 180, '2023': 165}
by state:      {'done': 1405, 'draft': 1, 'cancel': 1}
by form:       {'pnd53': 986, 'pnd3': 420, 'pnd1': 1}
their cert lines = 1499 ; sum(amount) = 9,537,106.08 ;
   of those lines carrying ANY journal-item reference = 29
```
**฿9,537,106.08 of certified withholding sits on 1,405 `done` certificates that reference no
payment, no journal entry, and — in 1,470 of 1,499 lines — no journal item.** They are spread
evenly across all four years, so this is standing practice, not a migration artefact.

**Mechanism, from the deployed source.** `security/ir.model.access.csv` grants
`account.group_account_invoice` **read/write/create/unlink = 1,1,1,1** on `withholding.tax.cert`
and its lines; `views/withholding_tax_cert.xml` publishes a menu
(`WT Certificates`, parent `account.menu_finance_payables`) on a form declared
`create="1" edit="1" delete="1"`, with `<tree editable="bottom">` on `wt_line` exposing `amount`,
`wt_percent` and `base` as free input, a `clickable="True"` statusbar and an
`action_draft` button with `states="done,cancel"`. **An invoicing user can create, re-open, edit
and delete a withholding certificate by hand, with no ledger anchor.**

**Note on the asymmetry:** `pnd3` is **420 unanchored vs 331 anchored (55.9% unanchored)**, against
`pnd53` at 986/3,451 (22.2%). The two forms are not produced the same way.

### E3-F-19 — **SUPPORTED. Certificate identity is broken in both directions.**
```
cert.name: population=5201  NULL=1417  distinct=3658
duplicated values=75 covering 202 rows
   JRCAUOB2026040047 x9   JRCAUOB2026050006 x9   JRCAUOB2026050128 x9
   JRCAUOB2026060066 x8   JRCSH12026060165  x8   JRCAUOB2026050053 x6 ...
of the 1,407 unanchored certs: name NULL = 1407
of the 3,794 payment-anchored certs: name NULL = 10
name shape: {'JR...serial': 3784, '<null>': 1417}
```
**1,417 certificates carry no number at all; 202 certificates share 75 numbers, up to 9 to a
number.** `name` is a stored compute copying `payment_id.name`, is `invisible="1"` in the form, has
no default, no sequence, no `required`, and no unique constraint. A certificate number is not an
identifier in this deployment.

### E3-F-20 — **SUPPORTED. The only arithmetic control on certificate lines cannot fail, and is switched off entirely at rate 0.**
`models/withholding_tax_cert.py:229-245` back-derives the base from the tax:
```python
"wt_percent": wt_percent,
"base": (abs(move_line.balance) / wt_percent * 100) if wt_percent else False,
"amount": abs(move_line.balance),
```
and `:329-338` then checks the identity it just constructed:
```python
@api.constrains("base","wt_percent","amount")
def _check_wt_line(self):
    if rec.wt_percent and float_compare(rec.amount, rec.base*rec.wt_percent/100, prec) != 0:
        raise ValidationError(_("WT Base/Percent/Tax mismatch!"))
```
Measured, UNIT = `withholding_tax_cert_line` row, POPULATION = all 6,159:
```
amount == base*pct/100 (tol 0.005): consistent=6048  inconsistent=0  pct-zero=111  null=0
wt_percent distribution: {'3':2642, '0.5':1688, '1':1623, '0':111, '5':80, '2':10, '10':5}
```
**6,048 of 6,048 consistent is not evidence of correctness — the base was computed from the amount,
so the constraint validates a tautology.** It says nothing about whether the base matches any
invoice. And the `if rec.wt_percent` guard means the check is **skipped whenever the rate is 0**:
```
111 lines with wt_percent=0 : 2023-11-08 .. 2026-07-06
  base nonzero: 101 ; amount nonzero: 12
  sum base = 5,698,486.81 ; sum amount = 37,064.11
  e.g. line 405: base=5,500,123.20  wt_percent=0  amount=27,500.62   (27,500.62/5,500,123.20 = 0.5%)
  e.g. line 6780: base=-1.39  wt_percent=0  amount=0  cert_id=NULL   (negative base)
```
**฿5,698,486.81 of declared base and ฿37,064.11 of tax on 111 lines have never been checked by
anything**, including one line whose base and amount imply 0.5% while the line records 0%, and one
line with a negative base.

### E3-F-21 — **SUPPORTED. 362 certificate lines belong to no certificate; 44 reference journal items outside the withholding account.**
```
cert_id NULL lines = 362  (sum amount 1,725,132.64) ; cert_id pointing to a missing cert = 0
certs with >=1 line = 5199 of 5201 ; certs with ZERO lines = 2
ref_move_line_id NULL on lines = 2384 / 6159 (38.71%)
distinct ref_move_line_id = 3628 ; on acct 1137 = 3584 ; NOT on 1137 = 44 (all resolvable)
   their account_id: {'33': 34, '1306': 10}
      33   = 111003 Outstanding Payments            [asset_current]
      1306 = 2250013 Accrued Tax P.N.D.1 employees  [liability_current]
```
The wizard filters candidate lines to accounts flagged `wt_account=True`, of which there is exactly
one:
```
account_account = 339 ; accounts flagged wt_account=TRUE = 1
   id=1137 code=2260000 name=Withholding Tax type=liability_current
```
**44 certificate lines therefore cite journal items the wizard could not have offered** — including
10 citing the *employee* P.N.D.1 accrual account from supplier certificates.

### E3-F-22 — **SUPPORTED. Withholding posted to the ledger and withholding certified do not reconcile, in both directions.**
UNIT = posted journal item on account 1137:
```
journal items on acct 1137 = 5863 ; posted = 5675 (draft 3, cancel 185)
  posted credit-side = 5528 (26,139,905.55)   debit-side = 108 (26,007,030.14)   zero = 39
```
UNIT = posted **credit-side** item on 1137 (the withholding events), POPULATION = 5,528:
```
referenced by >=1 cert line = 3499 ; NOT referenced = 2029 (36.70%)
uncertified credit amount = 12,065,773.78  of  26,139,905.55
```
Second, independent route — UNIT = `account_payment` whose move carries a 1137 item:
```
population = 5232 ; with >=1 cert = 3689 ; with NO cert = 1543 (29.49%)
certs with payment_id = 3794 ; payment's move has >=1 WHT item = 3773 ; has NONE = 21
```
Two different units, two different routes, the same shape: **roughly 30–37% of posted withholding
carries no certificate link, and 21 certificates point at payments that withheld nothing.**
Meanwhile cert lines total ฿26,219,137.38 against ฿26,139,905.55 of posted credits.
I state the traceability gap, not "no certificate exists": 38.71% of cert lines carry no
`ref_move_line_id`, so an untraced certificate may exist for some of the 2,029.

### E3-F-23..26 — Properties of the **on-disk 2026-07-06 report working tree** (see E3-F-05: NOT proven to be the deployed code)

`models/report_withholding_tax.py`, uncommitted, header
`# Developed by Marcos Ferreira @ SCG Legacy Thailand / Jira: ACC-6 / TXT Exportation for Revenue`:

**E3-F-23 — The submission TXT hardcodes the income code.**
```python
# 15- Income code
"2",
```
No reference to `line.wt_cert_income_type`. Measured against the certificates the report would
select (UNIT = cert line on a `done` cert, POPULATION = 5,784):
```
income type 2   lines=   11  MATCHES the hardcoded 2
income type 5   lines= 4120  DIFFERS
income type 6   lines= 1653  DIFFERS
=> 5773 of 5784 lines (99.81%) exported with an income code that differs from their certificate.
```
Whether field 15 must equal the certificate's income type is
`UNRESOLVED — STATUTORY EVIDENCE REQUIRED`. **Routed to P07.** What I state without statutory
authority: **the system's own two artefacts disagree on 99.81% of lines.**

**E3-F-24 — The same record exports its year in two different eras.**
```python
# 13- Tax month  str(line.cert_id.date.strftime('%m')).zfill(2)
# 14- Tax year   int(line.cert_id.date.strftime('%Y'))                 <-- Gregorian
# 16- Payment date str(self.format_date_dmy(line.cert_id.date)).replace("/","")
...
def format_date_dmy(self, date=None):
    year_thai = int(date.strftime(DEFAULT_YEAR_FORMAT_WHT)) + 543      <-- Buddhist era
```
Field 14 is Gregorian; field 16 is BE. This is the same era ambiguity the brief records at S16-07
(30 `account_move` rows dated `2567`), reappearing inside the filing export. Certificate dates
themselves are clean — `cert.date` years are 2023/2024/2025/2026 only, and `payment_date` likewise
— so nothing double-converts today.

**E3-F-25 — PND1 certificates are unreportable.**
```python
INCOME_TAX_FORM = {"pnd3": "P03", "pnd53": "P53"}
income_tax_form = fields.Selection(selection=[("pnd3","PND3"),("pnd53","PND53")], required=True)
def format_pnd(self, pnd):  return INCOME_TAX_FORM[pnd]     # KeyError on pnd1 / pnd3a
```
```
cert lines the report could emit, by form:
  pnd53  lines=5020  tax=24,102,624.65   REPORTABLE
  pnd3   lines= 751  tax=   235,338.49   REPORTABLE
  pnd1   lines=  13  tax=    83,862.42   NOT OFFERED BY THE REPORT WIZARD
```
**13 certificates / ฿83,862.42 recorded under `pnd1` cannot be selected by the reporting module at
all.** `pnd3a` is offered by the certificate and by neither the report nor the data.

**E3-F-26 — The filing period is driven by the certificate's own editable date.**
```python
domain = [("cert_id.income_tax_form","=",self.income_tax_form),
          ("cert_id.date",">=",self.date_from), ("cert_id.date","<=",self.date_to),
          ("cert_id.company_partner_id","=",self.company_id.partner_id.id),
          ("cert_id.state","not in",["cancel","draft"])]
```
UNIT = `done` cert, POPULATION = 5,191:
```
cert.date vs cert.payment_date (all 5,201): date<payment 283 ; equal 1120 ; date>payment 3798
   delta days min=-365  max=+22
done certs whose `date` is in a DIFFERENT calendar month from `payment_date` = 437 (8.42%)
   their line tax = 2,725,891.46
   month offset: {-12:3, -4:1, -3:1, -2:2, -1:178, +1:252}
of the 5191 'done' certs the report will include, 1405 (27.07%) have no payment and no journal
   entry; their line tax = 9,535,929.93
```
**437 certificates carrying ฿2,725,891.46 fall in a different filing month from their payment**,
three of them a full year apart, and the report has no anchoring filter, so the 1,405 hand-made
certificates (E3-F-18) are included in whatever period their editable date lands in.

**Note on a zero I refuse to call a negative result.** `withholding_tax_report` extracts to
**0 rows**, and `create_withholding_tax_cert` to **10 rows, all dated 2026-07-09..11** (the two days
before the archive). Both models are `models.TransientModel`; Odoo vacuums them.
**0 rows is not evidence that the report was never run.** It is an unfinished measurement, and I
publish it as such.

---

## 5. STATUS

### SUPPORTED
- E3-F-02, E3-F-03: the deployed certificate engine is the 2021 series-14 source plus one field,
  identified against the deployment's own registry (`signature`), not against a version string.
- E3-F-06: the deployment-adjacent tree is a later working copy (2 of 45 modules ahead).
- E3-F-07: source computes withholding on the full invoice base, never prorated (single content
  variant across all 6 version-matching copies).
- E3-F-08: partial payments exist — 280 bills, 3 of them WHT-bearing.
- E3-F-10: **1,854 payments (99.30% of the post-2023-12-29 `WHT3%` cohort) posted ฿1,440,563.92 of
  withholding that the master rate 0.0 cannot produce.** The posted amount is operator-determined.
  Negative control: 294 payments credit the WHT account with no `wt_tax_id` at all.
- E3-F-12: withholding is applied to 338 goods lines, 195 raw-rice material lines, 151 GRNI-account
  lines and 64 fixed-asset lines. (Admissibility → P07.)
- E3-F-13: 2.30% of the catalogue is configured, 89 of those 91 at a zero rate, and 54.01% of
  applied withholding is hand-keyed or overridden.
- E3-F-15, E3-F-16, E3-F-17: `income_tax_form` has no determining code path anywhere and no
  supporting field on `res.partner` (32-hit registry sweep, the one partner hit a false positive of
  my own pattern); it is nonetheless perfectly consistent across all 506 suppliers, and is not
  explained by `is_company`.
- E3-F-18: 1,407 certificates (27.05%), ฿9,537,106.08, anchored to nothing; measured twice by
  independent tools; mechanism located in access rights and view definitions.
- E3-F-19: 1,417 certificates with no number; 202 sharing 75 numbers.
- E3-F-20: the only arithmetic control is a tautology, and is skipped entirely at rate 0 —
  111 lines, ฿5,698,486.81 of base, never checked.
- E3-F-21: 362 orphan lines; 44 lines citing journal items outside the single WHT account.
- E3-F-22: 2,029 posted withholding items (36.70%, ฿12,065,773.78) with no certificate link, and
  1,543 of 5,232 WHT-bearing payments (29.49%) with no certificate — two units, two routes.

### CHALLENGED (I dispute the package or the assignment framing)
- **E3-F-01 challenges the brief's identification method.** "165 of 190 deployed modules have a
  version-matching copy" is true and, for two of the four WHT modules, insufficient: 4 and **6**
  distinct content variants share a single version string, and the report module's version string
  (`'1.0.0'`) carries no series at all. The brief does not state this limit. My reads therefore
  used registry discrimination (E3-F-02), not version matching.
- **E3-F-09/E3-F-10 challenge the assignment's own framing.** I was asked whether withholding is
  computed on the full base per partial payment or prorated. On the two clean partial-payment cases
  the ledger shows **prorated halves that the code cannot produce**, and one of them posts 3% three
  months after the master rate became 0. The premise that the module computes the posted amount is
  not supported by the deployment. **I decline to publish "full-base withholding on partial
  payments" as an observed behaviour.** Both statements stand unreconciled and I preserve the
  disagreement rather than pick one.
- **E3-F-11 partially challenges its own severity.** The `self.wht_amount` recordset assignment is a
  certain source defect; its measured footprint is 7 moves / ฿3,259.87, and leak cannot be separated
  from stale-recompute without runtime. I publish the small number.

### MISSING (evidence that should exist in the package and does not)
- No account anywhere in the frozen brief of *which* source tree the WHT modules were read from, or
  of the fact that the cert module is series-14 code.
- No measurement of the certificate population against the ledger. The brief reports
  `withholding_tax_cert: 5,201 (done 5,191 / cancel 5 / draft 5)` and stops. The 27.05% unanchored
  cohort, the 1,417 missing numbers and the 36.70% uncertified posted withholding are all one join
  away and are absent.
- No statement of `account_withholding_tax` contents. Seven rows, one of which is a 0% rate named
  "3%" driving 2,038 payments, would have been cheap to publish.

### RISKY
- E3-F-04: the series-14 `move_id.type` call is latent only because the journal-entry certificate
  route has never been used (0 of 5,201). First use raises AttributeError.
- E3-F-14: withholding is unreachable for payments not registered from an invoice; 294 payments
  credit the WHT account outside the module's field and I have not identified their route.
- E3-F-05 + E3-F-23..26: four material findings rest on an **uncommitted working tree dated 5 days
  before the archive**, whose module version string is identical to a 2023 commit 246 lines behind
  it. They are stated as properties of that file, not of the deployment.
- The 111 zero-rate certificate lines and the 89-of-91 zero-rate product defaults mean any future
  recompute silently rewrites historical withholding to zero (158 invoice moves already show
  stored≠0 against a current-rate recompute of 0).

### UNRESOLVED — STATUTORY EVIDENCE REQUIRED → routed to peer process P07
1. Whether withholding is applicable to the goods, raw-material, GRNI-account and fixed-asset lines
   measured in E3-F-12.
2. Whether the per-supplier PND3/PND53/PND1 classification in E3-F-16 is correct for any supplier.
3. Whether the income-type ↔ PND-form combinations in E3-F-17 are admissible.
4. Whether field 15 of the RD submission layout must equal the certificate's `wt_cert_income_type`
   (E3-F-23), and whether fields 14 and 16 may carry different eras (E3-F-24).
5. Whether a certificate with no payment, no journal entry, no journal-item reference and no number
   (E3-F-18, E3-F-19) is a valid instrument.
6. Whether a certificate line stating 0% against a non-zero base and a non-zero tax (E3-F-20) is
   admissible.
I have not searched for, inferred, or imported any statutory source, and I state no requirement of
Thai law anywhere above.

### EVIDENCE REQUIRED NEXT
1. **Identify the deployed `l10n_th_withholding_tax_report` code.** Nothing in the archive or the
   host pins it. Needed: the deployment host's addons path and file mtimes/hashes at 2026-07-11, or
   a filestore/ir_attachment artefact carrying a rendered report. Until then E3-F-23..26 cannot be
   attributed to the deployment.
2. **`mail_message` / `mail_tracking_value` on `withholding.tax.cert`.** The model inherits
   `mail.thread` with `tracking=True` on `name`, `date`, `state`, `payment_id`, `move_id`. That
   tracking history would settle how the 1,407 unanchored certificates were created and whether any
   `payment_id` was ever cleared — the one question E3-F-18 leaves open.
3. **`ir_logging` / `base_automation` / `om_data_remove` usage.** `om_data_remove 16.0.1.0.1` is
   INSTALLED here (memory: P06 found it deletes ledger rows unauthorised). It must be excluded, by
   evidence, as a cause of the missing anchors — I have not done so.
4. **`res_users` 27, 24, 28, 26.** One user (27) created 4,870 of 5,201 certificates and 1,378 of
   1,407 unanchored ones; user 26 wrote the `WHT3%` rate to 0 on 2023-12-29. Identify the roles.
5. **The 294 payments that credit account 1137 with no `wt_tax_id`** — determine the creating route
   (E3-F-14).
6. **A second deployment with WHT activity**, if one exists in the programme, as a discriminating
   population: every finding above rests on a single company (`company_id = 1` on all 5,201 certs),
   so I cannot separate "this module behaves this way" from "this operator works this way".

---

## 6. COMMAND INDEX (every claim above is reproducible from these)

```
# extraction (18.6 pg_restore; piping yields 0 bytes)
/opt/homebrew/opt/postgresql@18/bin/pg_restore -t <table> --data-only -f s16/E3_<table>.sql \
    ~/Downloads/iSMEs_2026-07-11_05-03-27.dump
#   tables added by this expert: account_withholding_tax, withholding_tax_cert_line,
#   create_withholding_tax_cert, account_account_create_withholding_tax_cert_rel,
#   withholding_tax_report, res_partner

# projections (field-count asserted single-valued before use)
awk 'BEGIN{FS="\t";OFS="\t"} /^COPY public.account_move_line /{f=1;next} f&&/^\\.$/{f=0} \
  f{print $1,$2,$7,$11,$20,$25,$30,$31,$35,$36,$37,$44,$61,$62}' \
  s16/T_account_move_line.sql > s16/E3_aml.tsv
awk 'BEGIN{FS="\t";OFS="\t"} /^COPY public.account_move /{f=1;next} f&&/^\\.$/{f=0} \
  f{print $1,$29,$30,$13,$6,$44,$46,$75,$39,$41}' s16/T_account_move.sql > s16/E3_am.tsv

# source candidate enumeration (PS-1, adapt_version applied with serie 16.0)
python3 - <<'PY'   # over ../src_paths.json, 3,174 module names
  read every __manifest__.py; keep adapt_version(raw)==deployed; hash all .py per module
PY

# writer enumeration (PS-2), with controls
grep -rn --include='*.py' --include='*.xml' --include='*.csv' -l "wt_tax_id" \
  /Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/{addons,swr} | grep -v '\.git/'
grep -rl --include='*.py' "account.move"          .../{addons,swr} | wc -l   # POSITIVE CONTROL = 54
grep -rl --include='*.py' "zzz_nonexistent_token_xyz" .../{addons,swr} | wc -l # NEGATIVE CONTROL = 0

# deployed-vs-declared module set
comm -12 <(cut -f1 s16/installed.txt|sort) <(ls .../Odoo16/addons .../Odoo16/swr|sort -u)

# variant discrimination against the deployment's own registry
python3 -c "... load('s16/T_ir_model_fields.sql','ir_model_fields') ..."
```

**Nothing in this report was written to the database, to any source tree, or to any host outside
the scratchpad. No external network was used.**
