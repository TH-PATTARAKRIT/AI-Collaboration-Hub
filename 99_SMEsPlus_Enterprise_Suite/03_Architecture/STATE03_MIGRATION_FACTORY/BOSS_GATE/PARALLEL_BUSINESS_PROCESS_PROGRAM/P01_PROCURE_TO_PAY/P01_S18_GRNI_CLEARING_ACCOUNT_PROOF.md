# P01 — SERIES-18 GOODS-RECEIVED CLEARING ACCOUNT PROOF

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S18-05`
Governing separation: **CONFIGURED is not EXECUTED.** The two are reported separately throughout.


> ### PEER DELTA APPLIED — BOUND TO ONE IDENTITY
>
> Peer **P04** (`9e377e30`, `P04-F-101`) records **three** series-18 database identities on this
> host, not one: `551ab874` (361 modules — the one analysed here), `4b766580` (478 modules), and
> `96548e18` (`T805efaplus`, 123 modules, never transacted). **Everything in this document is
> bounded to `551ab874` @ 2026-08-30** and is not a claim about the series-18 generation as
> deployed elsewhere. See `P01_S18_PEER_DELTA_HANDOFF.md §2.2`.

---

## 1. WHAT THE ACCOUNT IS

`property_stock_account_input_categ_id` is the **goods-received / interim input account** — the
receipt-side half of the clearing bridge that P01 has traced across four rounds. Its role is to
carry the obligation between the moment goods are received and the moment the vendor bill is
posted, so that the two events reconcile against each other rather than against the ledger.

**Deployment evidence — identifiers only, not canonical identity:**

| Company | Account id | `code` | Type | `reconcile` | Name |
|---|---|---|---|---|---|
| 1 | 176 | `210300` | `liability_current` | **true** | Uninvoiced Receipts |
| 2 | 62 | `210300` | `liability_current` | **true** | Uninvoiced Receipts |
| 3 | 100 | `210300` | `liability_current` | **true** | Uninvoiced Receipts |
| 4 | 138 | `210300` | `liability_current` | **true** | Uninvoiced Receipts |

The account is correctly typed for the role: a current liability, marked reconcilable so receipt
and bill can be matched off against each other. **Whoever configured this understood the mechanism.**

---

## 2. CONFIGURATION — READ FROM BOTH STORAGE LOCATIONS

### 2.1 Per-record jsonb, `product_category` (126 rows)

`property_stock_account_input_categ_id` is set on **15 of 126 categories**, and each of those 15
carries a value for **all four companies**: `{'1': 176, '2': 62, '3': 100, '4': 138}`.

That is **60 configured (category, company) pairs**, not 15. The denominator of configured pairs
is 15 × 4; the denominator of possible pairs is 126 × 4 = **504**.

The 15 categories are the operating material categories of a concrete business — aggregates
(sand, stone, fly ash, admixture), construction materials, electrical and plumbing supplies, road
materials, fuel and lubricants, tools and equipment, and precast pipe/concrete.

### 2.2 Company-level `ir_default`

| Field | co 1 | co 2 | co 3 | co 4 |
|---|---|---|---|---|
| `property_stock_account_input_categ_id` | **176** | **`false`** | **`false`** | **no row** |
| `property_stock_account_output_categ_id` | 701 | `false` | `false` | no row |
| `property_stock_valuation_account_id` | 169 | `false` | `false` | no row |
| `property_stock_journal` | **40** | **16** | **24** | **32** |

### 2.3 Effective value per (category, company) pair — the number that actually matters

Applying the resolution order proved in `P01_S18_PERIODIC_PERPETUAL_POLICY_PROOF.md §2.1`
(jsonb\[company] → company `ir_default` → global `ir_default`):

| Company | Categories resolving to a clearing account | Categories resolving to none |
|---|---|---|
| 1 | **126** (15 by jsonb + 111 by company default 176) | 0 |
| 2 | **15** (jsonb only; company default is explicit `false`) | 111 |
| 3 | **15** | 111 |
| 4 | **15** (jsonb only; no default row and no global row) | 111 |

**Effective total: 171 of 504 (category, company) pairs resolve to a clearing account.**

The headline "configured on 15 categories" is true of the jsonb layer and **understates company 1**,
where every category resolves. Reporting only the jsonb layer would have repeated `ERR-P01-19` in
mirror image — that error under-reported configuration by reading one location; this one would have
under-reported it by reading the other.

### 2.4 An explicit `false` is not a missing row

Companies 2 and 3 carry `ir_default` rows whose value is `false`; company 4 has **no row at all**.

**Behaviourally these are identical, and the first version of this section implied otherwise.**
Traced through the ORM: `false` → `convert_to_cache(False)` → empty recordset →
`convert_to_column` → `None` → the `if fallback not in (None, 0)` guard in
`R1:odoo/models.py:2995-3025` fails → no `COALESCE` → SQL NULL. A missing row →
`_get_model_defaults(...).get(name)` → `None` → **the identical path**. Same resolved value, same
reads, same writes. (Corrected on Expert C's challenge, `C-02`.)

The distinction is retained here for exactly one reason, and it is not a behavioural one: an
explicit `false` is a **record that someone acted**, and a missing row is not. That is evidence
about *intent*, which §9 needs and which nothing else in this database supplies. It carries **no
consequence for how any value resolves.**

---

## 3. VALUATION POLICY PER CATEGORY

All 126 categories, in all four companies, resolve to `manual_periodic` — proved completely in
`P01_S18_PERIODIC_PERPETUAL_POLICY_PROOF.md §6`. **No configured category is under a policy that
would consult the clearing account at receipt.**

---

## 4. THE EVENT PATH THAT WOULD REFERENCE THE ACCOUNT

Same generation, from source:

`R1:stock_account/models/stock_valuation_layer.py:74-95` `_validate_accounting_entries`
→ gated on `product_id.valuation == 'real_time'`
→ `R1:stock_account/models/stock_move.py:703` `_account_entry_move`
→ `:725` `journal_id, acc_src, acc_dest, acc_valuation = self._get_accounting_data_for_valuation()`
(`:477`)
→ for an incoming move, `acc_src` is the **input (clearing) account** and `acc_valuation` the
valuation account.
`R1:purchase_stock/models/stock_move.py:189` overrides `_account_entry_move` for purchase-linked
moves.

**The path exists and is complete in this generation.** Its entry gate is the valuation policy,
and that gate is closed for every product in this deployment.

---

## 5. EXECUTION TEST

**POPULATION:** `account_move_line`, **40,353 rows**, the complete journal-item population of the
deployment. **UNIT:** one journal item. **PATTERN:** exact match on `account_id` / `journal_id`.

| Account | Role | Journal items |
|---|---|---|
| 176 (co 1) | Uninvoiced Receipts | **0** |
| 62 (co 2) | Uninvoiced Receipts | **0** |
| 100 (co 3) | Uninvoiced Receipts | **0** |
| 138 (co 4) | Uninvoiced Receipts | **0** |
| 701 (co 1) | Stock Interim Delivered | **0** |
| 169 (co 1) | Inventory `130000` | 2,940 |

| Journal | Items |
|---|---|
| 40 / 16 / 24 / 32 (`STJ` Inventory Valuation, all four companies) | **0** |

**POSITIVE CONTROLS.** The same counter, over the same parse, returns non-zero freely: the largest
accounts are 186 (4,049 items), 211 (3,522), 169 (2,940), 343 (2,408); the largest journals are
45 (8,226), 33 (7,707), 9 (4,504), 34 (4,202). A zero from this counter is a measurement, not a
silence.

*One count corrected on Expert B's challenge:* the first version said **144 distinct accounts**.
It is **143 accounts plus a NULL bucket** — **71 journal items carry no `account_id` at all**. The
distinct-account figure is **143**, and the 71 account-less rows are named rather than absorbed
into it.

### 5.1 THE TEST WAS THREE TIMES NARROWER THAN THE CONFIGURATION — WIDENED

The first version tested only the **input** account. The same 15 categories also configure the
**output** and **valuation** accounts for all four companies, and those had not been tested.

| Account role | Accounts | Journal items |
|---|---|---|
| Input / clearing | 176, 62, 100, 138 | **0 each** |
| Output | 701, 702, 703, 704 | **0 each** |
| Valuation | 169 (co 1) and the company-2/3/4 equivalents | **0 — except account 169, which carries 2,940** |

**And all 2,940 items on account 169 sit in journal 45 `MIG26 "COA Migration 2026"`** — migrated
entries, never the runtime valuation path.

So across the **whole three-account stock-valuation configuration, in four companies, the series-18
runtime has posted nothing at all.** This does not change the conclusion; it changes what the
conclusion is about — not one unused account, but an entire unused stock-accounting configuration.

**The 2,940 items on account 169 do not come from the valuation path.** Every one of them is in
journal **45 `MIG26 "COA Migration 2026"`**, `move_type = entry`, all posted, dated 2026-01-03 to
2026-08-25, with names of the form `WH/OUT/16353 - …`. Inventory reaches this ledger **only**
through migrated predecessor entries. Debits ฿215,249.69 against credits ฿11,822,573.16.

**CLASSIFICATION: CONFIGURED — VERIFIED. EXECUTED — NO. Cause: POLICY-DEPENDENT.**

---

## 6. WHAT THE UNEXERCISED BRIDGE LEAVES UNRECORDED

Because the bridge never posts, the period between receipt and bill carries **no ledger
recognition of the obligation**.

### 6.1 THE EXPOSURE, RESTATED ON A DECLARED TAX BASIS — `ERR-P01-28`

**The first published version of this section summed two different tax bases into one number.**
Found by AAS-03 Expert A, verified here before adoption.

**POPULATION:** `purchase_order_line`, 21,102 rows, excluding lines on orders in state `cancel` or
`draft`. **UNIT:** one purchase order line. **CURRENCY:** THB throughout — `currency_id` is 133 on
all 13,887 orders and `currency_rate` is 1.0 on all of them, so currency risk is nil by
enumeration. **DISCOUNT:** zero on every line, likewise by enumeration.

**The defect.** 312 of the 1,580 received-not-invoiced lines carry a purchase tax with
`price_include_override = 'tax_included'` (`PV7% รวม VAT`). On those lines `price_unit` is
**VAT-inclusive**. The ratio `(product_qty × price_unit) / price_subtotal` is **exactly 1.0700 on
all 312** and **exactly 1.0000 on the other 1,267** — the diagnosis is identified, not inferred.
Summing `price_unit` across both groups mixes tax bases.

| Basis | Company 1 | Company 2 | Total |
|---|---|---|---|
| **Tax-exclusive** — the correct basis for a GRNI accrual | ฿14,692,566.42 | ฿14,336,901.24 | **฿29,029,467.66** |
| ~~As first published~~ (mixed basis) | ฿15,258,362.01 | ฿14,822,327.77 | ~~฿30,080,689.78~~ |
| Overstatement | | | **฿1,051,222.12 — 3.49%** |

**VAT on a purchase is recoverable input tax and is not accrued to inventory**, so the
tax-exclusive figure is the one a GRNI accrual would use. If instead the question were cash
exposure to vendors, the tax-**inclusive** basis would be right — but then **all 1,580** lines
must be grossed up, giving ฿30,962,543.77. **The first published number was neither**: 1,267 lines
on one basis plus 312 on the other.

The same defect applied to the counter-figure: invoiced-not-received **฿1,734,752.87 →
฿1,663,518.07** tax-exclusive.

### 6.2 AND THE AGGREGATE HID THREE DISTINCT POPULATIONS — `ERR-P01-29`

| Sub-population | Lines | Tax-exclusive | (as first published, mixed basis) |
|---|---|---|---|
| **Received against a goods receipt** (`qty_received_method = stock_moves`) | **1,411** | **฿27,490,865.80** | ฿28,540,809.47 |
| **Typed by an operator** (`qty_received_method = manual`) — **all 169 are service products** | **169** | **฿1,538,601.86** | ฿1,539,880.31 |
| **Total** | **1,580** | **฿29,029,467.66** | ฿30,080,689.78 |

By product type (mixed basis, as measured): storable 1,403 lines ฿28,455,002.22 · service 169
lines ฿1,539,880.31 · non-storable consumable 8 lines ฿85,807.25.

**The 169 manual lines have no receipt document at all.** No picking, no stock move, no valuation
layer, and no possible GRNI entry: `qty_received` there is a number an operator typed. **A
three-way match has only two legs on those lines**, and they are **5.30%** of the tax-exclusive
figure. They do not belong in a *received*-not-invoiced aggregate and are broken out here rather
than summed. The 8 non-storable consumable lines can likewise never produce a valuation layer.

**Separately: 18 lines are over-received** — `qty_received > product_qty` — carrying
**฿1,669,526.29** tax-exclusive (฿1,707,560.30 on the published basis), **5.75%** of the
exposure. Not an arithmetic error, but a distinct control condition that a single aggregate
conceals.

> **A note on how this table was produced.** The split was first written by *subtracting* a
> mixed-basis sub-total from the tax-exclusive total — which is the very error §6.1 corrects,
> committed inside the correction. Recomputing each sub-population on its own basis gives
> ฿27,490,865.80 and ฿1,538,601.86, not the ฿27,489,587.35 that subtraction produced. **Derive
> each figure; never subtract across bases.** Logged as part of `ERR-P01-28`.

### 6.3 THE CORRECTED HEADLINE

> **฿29,029,467.66 tax-exclusive across 1,580 purchase order lines is received-and-not-invoiced
> and recognised nowhere in the ledger.** Of that, **฿27,490,865.80 across 1,411 lines is backed
> by an actual goods receipt**; the remaining **฿1,538,601.86 across 169 service lines** is an
> operator-entered quantity with no receipt document.

**No accrual is booked against any of it.** Case-insensitive over `ref` on all 15,522 journal
entries: `accru` **0**, `uninvoiced` **0**, `grni` **0**.

*Control, strengthened on Expert C's challenge (`C-06`).* The first version's control — "15,434 of
15,522 have a non-empty `ref`" — proves the field is **populated**, not that an English phrase can
**match** in it. The accrual wizard writes `ref = _('Accrued %(entry_type)s entry as of %(date)s')`
with a capital A, so a case-sensitive search would have missed every one. The discriminating
control is a different English phrase in the same field: `reversal` matches **119**. The negative
now rests on a control that fires.

### 6.4 A SEPARATE MEASURE THAT MUST NOT BE ADDED TO IT

`P01_S18_PERIODIC_PERPETUAL_POLICY_PROOF.md §8.3` reports ฿22,953,527.29 of valuation-layer value
on 1,403 purchase-linked receipt moves. **That is a different measure**: layer value at receipt
cost, against purchase-order price on the un-invoiced quantity. They are **not two views of one
number and are not reconcilable**. Further, only 1,403 of 3,124 done purchase-linked moves carry
any layer, so ฿22.95M is a **floor** on receipt value, not a measure of it — and 2,085 of its
2,146 layers are migrated rows.

### 6.5 How to read this, and how not to


This is **not a defect of the software** and it is **not a posting error**. Under periodic
valuation, no receipt-time entry is expected, and the ฿30.08 million is a **timing position, not a
missing transaction**. It is disclosed here because:

- it is the exact exposure the configured-but-dormant clearing account exists to carry;
- at a reporting date it is a **completeness question for liabilities and inventory**, answerable
  only by a periodic count and a manual accrual, and no accrual entry exists in this database;
- P01's terms of reference are the accounting *events* of the P2P chain, and "the obligation is
  unrecognised between receipt and bill" is an event-level fact about this deployment.

Whether that treatment is acceptable is a reporting-policy question. It is **not decided here**,
and it is not P01's to decide. It is routed to the Boss decision package and flagged to P08
(record-to-report) and P11 (core reconciliation).

---

## 7. DOES THE VENDOR BILL RESOLVE OR BYPASS THE BRIDGE? — BYPASS

Detail in `P01_S18_VENDOR_BILL_AP_CLEARING_RECONCILIATION.md`. In summary: vendor bill product
lines post to **expense**, not to the clearing account. Of 3,375 product lines on 1,904 vendor
bills, the two largest accounts are 186 (`510000 Cost of Revenue`, company 1) with 1,062 lines and
72 (`510000`, company 2) with 966. **No bill line posts to 210300.** There is nothing in the
clearing account to resolve, and the bill does not attempt to.

---

## 8. CLASSIFICATION SUMMARY

| Item | Classification |
|---|---|
| Clearing account exists, correctly typed and reconcilable, in all four companies | **FACT VERIFIED** |
| Configured on 15 of 126 categories in the jsonb, for all four companies | **FACT VERIFIED** |
| Effective configuration is **171 of 504** (category, company) pairs | **FACT VERIFIED** |
| Company 1 resolves for **all** categories via its company default | **FACT VERIFIED** |
| Companies 2 and 3 carry an explicit `false`; company 4 carries no row | **FACT VERIFIED** |
| Source event path referencing the account exists in this generation | **FACT VERIFIED** |
| The account carries zero journal items | **FACT VERIFIED**, with positive controls |
| The stock journals carry zero journal items | **FACT VERIFIED**, with positive controls |
| Cause of non-execution | **POLICY-DEPENDENT — VERIFIED** |
| Reachability of the account under current configuration | **NOT LATENT — REACHABLE BY FOUR SEPARATE ROUTES, none of which requires a code change.** ~~*"no other trigger was found"*~~ **CORRECTED — `ERR-P01-31`**, §10 |
| **฿29,029,467.66** tax-exclusive received-not-invoiced, unrecognised and unaccrued | **FACT VERIFIED**, denominator, unit and tax basis declared in §6.1 |
| — of which receipt-backed | **฿27,490,865.80** on 1,411 lines — **FACT VERIFIED** |
| — of which operator-typed service quantities with no receipt document | **฿1,538,601.86** on 169 lines — **FACT VERIFIED**; **excluded** from any *received*-not-invoiced reading |
| ~~฿30,080,689.78 as first published~~ | **CORRECTED — `ERR-P01-28`**: mixed two tax bases (312 of 1,580 lines carry VAT-inclusive unit prices). Overstated by ฿1,051,222.12 (3.49%) |
| Whether that treatment is acceptable | **NOT A P01 DECISION** — Boss package; notified to P08 and P11 |

---

## 9. THE CONFIGURATION TELLS A STORY WORTH RECORDING

The clearing account is present, correctly typed, reconcilable, named for its purpose, and mapped
across four companies and the fifteen categories that actually carry this business's material
flows. The valuation journals exist in every company. **Everything needed for a perpetual bridge
is in place, and the single switch that would turn it on is set to periodic.**

Combined with §9.1 of the policy proof — the series-14 predecessor **did** post to an `STJ` stock
journal — the most economical reading is that this configuration was built for perpetual valuation
and the policy switch was either not carried across the migration or was deliberately turned off.

**That reading is `SUPPORTED INTERPRETATION`, not fact.** Distinguishing "deliberate policy change"
from "setting lost in migration" needs evidence this package does not hold — a migration
specification, a configuration decision record, or the predecessor's own settings. It is recorded
as `UNRESOLVED — EVIDENCE REQUIRED` and is the highest-value single question this run raises.

---

## 10. THE ACCOUNT IS NOT UNREACHABLE — `ERR-P01-31`

The first published version of §8 classified the clearing account as **LATENT**, adding *"no other
trigger was found"*. **That was a search that stopped too early, stated as a finding.** AAS-03
Expert C was assigned to disprove "configured and reachable" and instead enumerated **writers**
rather than observed rows. Four routes, all verified here before adoption. **None requires a code
change.**

### 10.1 Route 1 — switching the valuation policy has no guard in company 1

`R1:stock_account/models/product.py:963-971`:

```
@api.constrains(… + ['property_valuation'])
def _check_valuation_accounts(self):
    for category in self:
        if category.property_valuation == 'real_time':
            if any(not category[account] for account in fnames):
                raise ValidationError(_('The stock accounts should be set in order to use the automatic valuation.'))
```

with `fnames` = input, output, valuation. Against the effective resolution in §2.3:

| Company | Categories where all three accounts resolve | The guard |
|---|---|---|
| **1** | **126 of 126** | **cannot refuse** |
| 2, 3, 4 | 15 of 126 | refuses 111, permits 15 |

And `ProductCategory.write()` (`R1:…/product.py:1032-1090`) calls `_svl_replenish_stock_am`
(`:809-830`), which for positive quantity posts **debit valuation / credit `stock_input`** in
`product_accounts['stock_journal']`.

> **A single write of `property_valuation` on one company-1 category credits account 176 in
> journal 40** — the two objects §5 reports as carrying zero items — for the on-hand value of that
> category's products. Scale available in the same archive:
> `SUM(remaining_value)` = **฿29,835,023.51** in company 1 (25,978 layers) and ฿60,059,575.87 in
> company 2 (21,823 layers).

**The unmeasured clause, stated rather than glossed.** Whether any user currently holds write
access to `product.category.property_valuation` in company 1 has **not been measured** — it needs
`ir_model_access`, `ir_rule` and `res_groups_users_rel` resolved against the stock and account
manager groups. **Until it is, this is a capability, not a live exposure**, and it is recorded that
way because the well-evidenced half of a finding is what makes the unmeasured half feel safe.

### 10.2 Route 2 — the accrual wizard is deployed, bound and permissioned

`R1:account/wizard/accrued_orders.py:44-52` — `account_id` carries the domain
`[('account_type','=','liability_current')]` when the active model is `purchase.order`.
Account 176 **is** `liability_current`. Deployed, read from the archive:

| Evidence | Value |
|---|---|
| `ir_model_data ('purchase','action_accrued_expense_entry')` | → `ir.actions.act_window` **433** |
| `ir_act_window` 433 | `binding_model_id` 588, `res_model = account.accrued.orders.wizard`, name *"Accrued Expense Entry / รายการค่าใช้จ่ายคงค้าง"* |
| `ir_model_data ('purchase','model_purchase_order')` | → 588 — **the binding resolves** |
| `account.group_account_user` | **22 users**; `account.group_account_manager` 9 |
| Wizard default for `account_id` | **none** — the user picks |
| Input population | non-empty: the 1,580 received-not-invoiced lines of §6 |

**A live, permissioned, unattended-by-default path whose account picker includes 176, with a
non-empty input set and no default.** The account is unused; it is not unreachable.

### 10.3 Route 3 — the manufacturing WIP wizard *defaults* its credit to account 176

`R1:mrp_account/wizard/mrp_wip_accounting.py:70-78` resolves the overhead account in three steps:
company `account_production_wip_overhead_account_id`, then
`property_stock_account_production_cost_id`, then **`property_stock_account_input_categ_id`**.

Deployed: `account_production_wip_overhead_account_id` is **NULL on all four companies**;
`property_stock_account_production_cost_id` is `false` for companies 1–3 and absent for company 4.
**Both earlier branches are falsy, so the third is taken — account 176 for company 1**, with
`journal_id` defaulted from `property_stock_journal` → **journal 40**.

`mrp` 18.0.2.0 and `mrp_account` 18.0.1.0 are **installed**; the action is bound to
`mrp.production` for `account.group_account_user`; **`mrp_production` holds 5,549 rows**.

**This route does not consult `property_valuation` at all.** Caveat stated rather than glossed: the
debit line takes `company.account_production_wip_account_id`, which is NULL here, so an untouched
wizard would not post — but `account_id` is editable in the line list, so a user completes the
debit and the 176 credit stands. **Reachable with one manual field.**

### 10.4 Route 4 — an armed scheduled writer, one configuration record from firing

`account_auto_transfer` 18.0.1.0 is **installed**; `ir_cron` id 24
(*"Account automatic transfers: Perform transfers"*) is **active** — 58 of the 66 crons are.
`account_transfer_model` and `account_transfer_model_line` **exist and hold zero rows**.

The module moves balances between arbitrary origin and destination accounts on a schedule. Today it
cannot fire. **Distance to firing: one configuration record.**

### 10.5 And two further writers with no account-type restriction at all

- `account.automatic.entry.wizard` — `ir_model_data ('account','action_automatic_entry_change_account')`
  → `ir.actions.server` 251. "Change Account" retargets selected journal items to **any** account.
- **Import.** `base_import` 18.0.2.0 and `account_base_import` 18.0.1.0 are installed, and the
  channel has already been used at scale: `ir_model_data` holds **181,540** external IDs under the
  `occ_mig` namespace, of which **10,190 are `account.move`**. `occ_mig` is not a module — it is a
  migration's xmlid namespace. An xmlid-keyed import can create or update moves on any account.

### 10.6 Corrected classification

| Item | Classification |
|---|---|
| The clearing account is **configured** | **FACT VERIFIED** (§2) |
| The clearing account is **not exercised** | **FACT VERIFIED**, three methods and an injection control (§5) |
| The clearing account is **unreachable** | **FALSE — CORRECTED.** Four routes, none requiring a code change |
| Route 1 (policy switch, unguarded in company 1) | **REACHABLE — capability proven; user write access NOT MEASURED** |
| Route 2 (accrual wizard) | **REACHABLE — deployed, bound, 22 permissioned users, non-empty input** |
| Route 3 (MRP WIP wizard) | **REACHABLE — defaults to 176; needs one manual field; 5,549 production orders** |
| Route 4 (scheduled transfers) | **ARMED, NOT CONFIGURED** — one record from firing |
| Routes 5–6 (change-account wizard, xmlid import) | **REACHABLE, no account-type restriction** |

**Why this correction matters more than its subject.** *"No other trigger was found"* is a claim
about the world made from a search of observed rows. **Reachability is a property of writers, not
of rows** — and the difference between them is the difference between "this account is dormant" and
"this account is one field-write away from carrying ฿29.8 million". Registered against the standing
rule that a **negative about the evidence base needs the same authority as a negative about the
subject**.
