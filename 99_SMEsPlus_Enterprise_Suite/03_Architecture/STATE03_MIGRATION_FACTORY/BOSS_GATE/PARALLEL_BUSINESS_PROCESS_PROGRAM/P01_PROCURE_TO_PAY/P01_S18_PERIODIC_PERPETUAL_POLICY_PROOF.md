# P01 — SERIES-18 PERIODIC vs PERPETUAL VALUATION POLICY PROOF

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S18-04`
Status: **MANDATORY CONTROL** — an identical zero was at risk of being misclassified as a defect.


> ### PEER DELTA APPLIED — BOUND TO ONE IDENTITY
>
> Peer **P04** (`9e377e30`, `P04-F-101`) records **three** series-18 database identities on this
> host, not one: `551ab874` (361 modules — the one analysed here), `4b766580` (478 modules), and
> `96548e18` (`T805efaplus`, 123 modules, never transacted). **Everything in this document is
> bounded to `551ab874` @ 2026-08-30** and is not a claim about the series-18 generation as
> deployed elsewhere. See `P01_S18_PEER_DELTA_HANDOFF.md §2.2`.

---

## 1. THE CONTROL THIS DOCUMENT ENFORCES

Two deployments in this estate report the same observation:

> `stock_valuation_layer.account_move_id` is set on **zero** rows.

The series-19 estate reports it. This series-18 deployment reports it.
**Same observed zero is not the same accounting semantic.** This document proves the semantic for
the series-18 deployment **on its own**, without reference to the series-19 estate. The comparison
is deferred to `P01_S18_S19_CONTROLLED_COMPARISON.md`, which may not be read before this one.

---

## 2. WHERE THE POLICY IS STORED IN THIS GENERATION

`property_valuation` is a **company-dependent** field on `product.category`. In this ORM generation
a company-dependent value can live in exactly **two** places:

1. the per-record **jsonb column** `product_category.property_valuation`, keyed by company id;
2. a row in **`ir_default`** for the field, scoped to a company or global.

`ir_property` — the storage used up to series 16 — **has no table definition in this archive at
all** (population: the 1,122 TABLE definitions in the TOC). There is no third location.

Reading only one of the two locations is exactly the defect recorded as `ERR-P01-19`, which
produced a false zero and the wrong remediation. **Both are read below.**

### 2.1 Resolution order, from source

`R1:odoo/fields.py:785-792`

```
def get_company_dependent_fallback(self, records):
    assert self.company_dependent
    fallback = records.env['ir.default'] \
        .with_user(SUPERUSER_ID) \
        .with_company(records.env.company) \
        ._get_model_defaults(records._name).get(self.name)
```

`R1:addons/base/models/ir_default.py:154-182` — the query is

```
SELECT f.name, d.json_value FROM ir_default d JOIN ir_model_fields f ON d.field_id=f.id
 WHERE f.model=%s AND (d.user_id IS NULL OR d.user_id=%s) AND (d.company_id IS NULL OR d.company_id=%s)
   AND d.condition IS NULL
 ORDER BY d.user_id, d.company_id, d.id
```

…and the loop keeps the **first** row per field. PostgreSQL sorts NULLs **last** under `ASC`, so a
company-specific row outranks a global one. Effective value =
**jsonb\[company] if present, else the company `ir_default` row, else the global `ir_default` row.**

---

## 3. LOCATION 1 — THE PER-RECORD JSONB COLUMN

`product_category`: **126 rows.**

| Field | Rows where the jsonb column is NULL | Companies with a value set |
|---|---|---|
| `property_valuation` | **126 of 126** | none |
| `property_cost_method` | 108 of 126 | company 1 on 18 categories, all `average` |
| `property_stock_journal` | **126 of 126** | none |
| `property_stock_account_input_categ_id` | 111 of 126 | **all four**, 15 categories each |
| `property_stock_account_output_categ_id` | 111 of 126 | all four, 15 categories each |
| `property_stock_valuation_account_id` | 111 of 126 | all four, 15 categories each |
| `property_account_creditor_price_difference_categ` | **126 of 126** | none |

**No category overrides the valuation policy for any company.**

## 4. LOCATION 2 — `ir_default`

`ir_default`: **54 rows**, joined to `ir_model_fields` to resolve `field_id` to `model.field`.

| Field | company_id | value |
|---|---|---|
| `product.category.property_valuation` | **NULL (global)** | **`"manual_periodic"`** |
| `product.category.property_cost_method` | NULL (global) | `"standard"` |

There is exactly **one** row for `property_valuation`, it is global, and it is `manual_periodic`.
No company-scoped row exists to override it for any of the four companies.

---

## 5. IS THERE A PRODUCT-LEVEL OVERRIDE? — NO

`R1:stock_account/models/product.py:17` (`product.template`) and `:147` (`product.product`):

```
valuation = fields.Selection(related="categ_id.property_valuation", readonly=True)
```

`valuation` is a **read-only related field**. In this generation there is no product-level or
template-level valuation setting; the category is the only determinant. A product's policy is its
category's policy.

---

## 6. EFFECTIVE POLICY — COMPLETE, NOT SAMPLED

| Scope | Categories | Companies | Effective `property_valuation` |
|---|---|---|---|
| Whole deployment | **126 of 126** | **4 of 4** | **`manual_periodic`** |

**No mixed population exists.** Every (category, company) pair — all 504 — resolves to periodic.
This is not a sample: the jsonb column was read on all 126 rows and `ir_default` holds a single
global row.

### 6.1 The label differs between generations, and so does the meaning

`R1:stock_account/models/product.py:915-917` (series 18):

```
property_valuation = fields.Selection([
    ('manual_periodic', 'Manual'),
    ('real_time', 'Automated')], string='Inventory Valuation',
```

The series-19 tree relabels `real_time` to **`Perpetual (at invoicing)`**. The stored value in this
deployment is `manual_periodic`, whose series-18 label is **Manual**. Any cross-generation reading
of this field must use the **stored value**, never the label.

---

## 7. IS RECEIPT ACCOUNTING EXPECTED UNDER THIS POLICY? — NO

`R1:stock_account/models/stock_valuation_layer.py:74-95`, `_validate_accounting_entries`:

```
for svl in self:
    if not svl.with_company(svl.company_id).product_id.valuation == 'real_time':
        continue
    if svl.currency_id.is_zero(svl.value):
        continue
    move = svl.stock_move_id
    ...
    svl_move_list[svl.id] = move.id

moves = self.env['stock.move'].browse(move_ids)
...
for svl in self:
    linked_move = moves.browse(svl_move_list[svl.id])
    if linked_move:
        am_vals += linked_move....._account_entry_move(svl.quantity, svl.description, svl.id, svl.value)
if am_vals:
    account_moves = self.env['account.move'].sudo().create(am_vals)
    account_moves._post()
```

Under `manual_periodic` the first `continue` fires for **every** layer. `svl_move_list` stays
empty; `moves` is an empty recordset; `am_vals` stays empty; **no `account.move` is created and
`account_move_id` is never written.**

**The absence of a journal entry at receipt is the specified behaviour of this configuration.**

### 7.1 Two further skip conditions, recorded so they are not conflated with the policy

- `if svl.currency_id.is_zero(svl.value): continue` — **1,205** of the 47,801 layers have
  `value = 0.00` and would be skipped even under `real_time`.
- A layer with no `stock_move_id` yields an empty `linked_move` and is skipped regardless —
  **2,866** layers have no stock move.

These are **independent sufficient causes** for individual rows. They do not explain the zero on
their own (§8 shows the zero holds on a sub-population free of both), but a claim that attributes
the *entire* zero to policy without excluding them would be over-stated.

---

## 8. THE DISCRIMINATING TEST

The 47,801 layers are 96.2% migrated predecessor history (see
`P01_S18_DEPLOYMENT_IDENTITY_PROOF.md §6.2`). Migrated rows were inserted by a migration process,
not created by the series-18 runtime, so **they would carry no journal link under any policy.**
Attributing the zero to policy without separating them would be a self-confirming test.

**Discriminating sub-population:** valuation layers created by the series-18 runtime —
description free of migration markers, `create_date` after `database.create_date`, and carrying a
stock move.

| Measure | Value |
|---|---|
| Native runtime layers | **1,812** |
| …carrying a `stock_move_id` | 1,812 (100%) |
| …with non-zero value | 946 |
| …created between | 2026-08-25 12:19:13 and 2026-08-29 10:23:34 |
| …by company | company 1: 1,132; company 2: 680 |
| **…carrying an `account_move_id`** | **0** |

**The zero holds in the sub-population where migration and zero-value cannot explain it.**

### 8.1 The narrowest and strongest form of the test

Restricting further to receipts against purchase orders — the exact P2P event P01 exists to
analyse:

| Measure | Value |
|---|---|
| `stock_move` rows | 51,081 |
| …linked to a purchase order line | 3,158 |
| …of those, in state `done` | 3,124 |
| …of those, carrying valuation layers | **1,403** |
| Total value of those layers | **฿22,953,527.29** |
| **…of those layers, carrying an `account_move_id`** | **0** |

**1,403 completed goods receipts against purchase orders, ฿22.95 million of movement value, and
not one journal entry — under a policy where that is correct.**

---

## 9. IS THE JOURNAL CONFIGURATION DORMANT, FUTURE-FACING OR ACTIVE?

`ir_default` sets `product.category.property_stock_journal` per company:
16 (co 2), 24 (co 3), 32 (co 4), **40 (co 1)** — all four are `STJ / "Inventory Valuation" /
type general`. The jsonb column is NULL on 126/126, so the company default is the only source.

**Execution test** on `account_move_line` (40,353 rows): journals 16, 24, 32, 40 carry
**0 journal items each**.
*Positive control:* the same counter returns 8,226 for journal 45, 7,707 for journal 33 and 4,504
for journal 9, so the query can register a non-zero.

**Classification: CONFIGURED, NOT EXECUTED, and consistent with the policy.** The configuration is
**dormant by design under `manual_periodic`** — it is what the system would use if the policy were
changed to `real_time`, and it is not evidence that anything is wrong.

### 9.1 The predecessor did post to a stock journal

15,434 of 15,522 journal entries carry a non-empty `ref`, and those refs carry strings of the form
`[v14 STJ/UB/00087 - …] STJ/2026/04/0505`. The **series-14 predecessor used an `STJ` stock
journal**. The series-18 system does not. Whether that is a deliberate policy change or an
unintended consequence of the migration is **UNRESOLVED — EVIDENCE REQUIRED**, and it is the single
most consequential open question this run produces. It is routed to the Boss decision package,
not decided here.

---

## 10. DOES SUBSEQUENT ACCOUNTING RESOLVE THE ECONOMIC EFFECT?

Partly, and later. Detail is in `P01_S18_VENDOR_BILL_AP_CLEARING_RECONCILIATION.md`. In summary:

- Vendor bill product lines post to an **expense** account (`510000 Cost of Revenue`), not to a
  valuation or clearing account — 1,062 lines to account 186 (co 1) and 966 to account 72 (co 2)
  out of 3,375 product lines.
- Inventory (`130000`, account 169) carries 2,940 journal items, **all** in journal 45
  `MIG26 "COA Migration 2026"` — migrated entries only, never the runtime valuation path.
- Between receipt and bill there is **no ledger recognition of the obligation at all**, and no
  accrual: 0 of 15,522 moves carry `accru` in `ref` (*positive control:* 15,434 have a non-empty ref).

So the economic effect is recognised **when the bill is posted**, as expense — which is what
periodic valuation means. The exposure this leaves open between receipt and bill is quantified in
`P01_S18_GRNI_CLEARING_ACCOUNT_PROOF.md §6`.

---

## 11. CLASSIFICATION

| Question | Classification |
|---|---|
| Valuation policy in this deployment | **`manual_periodic` — FACT VERIFIED**, 126/126 categories × 4/4 companies, both storage locations read |
| Mixed population | **None** — FACT VERIFIED |
| Receipt accounting expected under this policy | **No** — FACT VERIFIED from source, same generation |
| The 0-of-47,801 zero-link result | **EXPECTED UNDER PERIODIC POLICY — VERIFIED** |
| The same zero on the 1,812-row native sub-population | **EXPECTED UNDER PERIODIC POLICY — VERIFIED** |
| The same zero on the 1,403 purchase-receipt sub-population | **EXPECTED UNDER PERIODIC POLICY — VERIFIED** |
| Stock journal configuration | **CONFIGURED, NOT EXECUTED — POLICY-DEPENDENT** |
| Whether periodic was *intended* here, given the predecessor posted to `STJ` | **UNRESOLVED — EVIDENCE REQUIRED.** Boss/owner decision, not a P01 decision |
| Whether periodic valuation is *appropriate* for this business | **NOT A P01 DECISION.** Routed to the Boss package |

---

## 12. WHAT WOULD FALSIFY THIS

Stated so a challenger has a target rather than a summary:

1. A product, category or company resolving to `real_time` — would require a jsonb value or an
   `ir_default` row that §3 and §4 say does not exist.
2. A **second writer** of `stock_valuation_layer.account_move_id` in the series-18 tree or in any
   of the 16 installed custom modules. If one exists, §7's mechanism is necessary but not sufficient.
3. Evidence that the 1,812-row native classifier is wrong — e.g. migrated rows that carry no
   migration marker and a post-creation timestamp.

Disproof assignments 1 and 2 were issued to AAS-03 Expert A; the outcome is recorded in
`P01_S18_AAS03_FRESH_CHALLENGE.md` and any correction is carried into
`P01_RESEARCH_ERROR_AND_REVISION_LOG.md` rather than silently replacing this text.
