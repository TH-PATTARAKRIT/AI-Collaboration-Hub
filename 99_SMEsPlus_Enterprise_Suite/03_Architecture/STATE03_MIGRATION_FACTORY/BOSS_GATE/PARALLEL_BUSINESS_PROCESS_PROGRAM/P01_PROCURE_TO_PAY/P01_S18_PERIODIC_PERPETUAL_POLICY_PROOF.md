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

### 7.1 IT IS NOT THE ONLY WRITER — CORRECTED BY CHALLENGE

**The first published version of this section named one mechanism. There are six, and one of
them is not valuation-gated.** Found by AAS-03 Expert A under the disproof assignment, verified
here before adoption (`ERR-P01-26`).

`R1:purchase_stock/models/account_move_line.py:298-313` — `_prepare_pdiff_svl_vals` writes
**both** link columns:

```
common_svl_vals = {
    'account_move_id': self.move_id.id,
    'account_move_line_id': self.id,
```

Its gate chain is **`cost_method`, not `valuation`**:
`R1:purchase_stock/models/account_invoice.py:126` filters
`l.product_id.cost_method != 'standard'`; `_apply_price_difference`
(`…/account_move_line.py:32-52`) gates on quantity and the existence of incoming layers;
`_prepare_pdiff_vals` (`:246-267`) gates **the journal-item half** on
`valuation == 'real_time'` (`:248`) but leaves **the valuation-layer half** gated only by
`float_is_zero(unit_valuation_difference * qty_to_correct)`.

**Under `manual_periodic`, this path can still create a valuation layer carrying both links.**

**And its precondition is satisfied in this deployment.** `property_cost_method` sets `average`
on **18 of 126** categories for company 1, so `cost_method != 'standard'` holds there.

**The path was reached and was exercised.** 354 posted vendor-bill journal items in company 1 fall
in those 18 categories; **18** carry a `purchase_line_id`; **16 of the 18 show a real price
difference** (e.g. bill unit 21,400.00 against a layer unit cost of 20,000.00). It produced no
valuation layer — because every one of those 16 layers has `remaining_qty = 0.00`, which drives
`qty_to_correct` to zero. **`remaining_qty` is a condition periodic policy does not control.**

**Consequence, stated plainly:**

- **The zero on `account_move_line_id` is not explained by periodic policy at all.** The first
  version of this document folded it in with the words *"Same for `account_move_line_id`"*. That
  was wrong.
- For the price-difference sub-population, **periodic policy is a sufficient explanation but not
  an identified one.**

*Residual, unresolved:* `remaining_qty` is mutated by later consumption, and the dump shows only
its value at 2026-08-30. Whether those 16 layers had `remaining_qty = 0` **at the moment their
bills were posted** cannot be settled from one snapshot.

### 7.2 Three valuation-independent skip conditions

`_account_entry_move` returns `[]` when `not product_id.is_storable`
(`R1:stock_account/models/stock_move.py:706-708`); `_validate_accounting_entries` skips on
`svl.currency_id.is_zero(svl.value)` (`:80`); and a layer with no stock move yields an empty
`linked_move` (`:82-92`).

Counterfactual, over all 47,801 layers — **rows that would be unlinked even under `real_time`**:

| Cause | Rows |
|---|---|
| no stock move | 2,319 |
| zero value | 1,096 |
| not storable | 574 |
| no stock move + not storable | 476 |
| zero value + no stock move | 70 |
| zero value + not storable | 38 |
| all three | 1 |
| **Total over-determined** | **4,574 of 47,801 (9.57%)** |

**The verdict "EXPECTED UNDER PERIODIC POLICY — VERIFIED" is scoped to the remaining 43,227 rows**,
where periodic is the only silent explanation available.

### 7.3 The counterfactual is not silent — and this strengthens the identification

Under `real_time`, `_get_accounting_data_for_valuation`
(`R1:stock_account/models/stock_move.py:477-500`) **raises `UserError`** when the journal or any
of the three accounts is missing. The location-level escape hatch
(`_get_src_account` / `_get_dest_account`, `:531-538`, falling back to
`location.valuation_in_account_id` / `valuation_out_account_id`) supplies nothing here:
**0 of 86 stock locations carry either account** (positive controls in the same read: `company_id`
non-null on 80 of 86; usages internal 60, inventory 8, view 7, transit 5, production 4,
supplier 1, customer 1).

**46,458 of 47,801 layers sit in categories that carry all three accounts.** For those, a
`real_time` counterfactual would have **produced entries**; for the other 1,343 it would have
**raised an error**. Either way the observed silent NULL is what periodic — and only periodic —
predicts.

**This is the argument that rules out "it would have been zero anyway" on the main path**, and it
is stronger than anything in the first version of this document.

---

## 8. THE DISCRIMINATING TEST — CORRECTED, AND STILL DECISIVE

The 47,801 layers are dominated by migrated predecessor history, so attributing the zero to policy
without separating migrated rows would be self-confirming.

### 8.1 The first version's classifier was unsound — `ERR-P01-27`

The first version separated a "native" set of **1,812** layers by `create_date` after
`database.create_date`. **`create_date` on this table is loader-supplied, not insertion time:**

| Measure | Value |
|---|---|
| `create_date` **earlier than the database itself** | **44,947 of 47,801** |
| `write_date` earlier than the database | **0** |
| `write_date` range | **2026-08-25 12:19:13 → 2026-08-29 10:23:34** |
| `write_date` by day | 2026-08-25: **47,218** · 08-29: 324 · 08-27: 153 · 08-28: 55 · 08-26: 51 |

**The entire table was physically written in a five-day window, seven days after the database was
created, and 98.8% of it on a single day.** There is no sub-population separable by insertion time,
and any classifier reading `create_date` as provenance is unsound on this table.

Worse, the 1,812 set was not what it was called: **1,254 of them are `Product Quantity Updated`
inventory adjustments written by `__system__`** inside that same load window. The denominator was
overstated by a factor of ~3.2.

### 8.2 The corrected set — two independent classifiers converging

| Classifier | Unit | Result |
|---|---|---|
| 1 — `create_uid` is a human user (114, 102, 117) | one layer | **559** |
| 2 — the underlying move is not an inventory adjustment | one layer | **558** |
| **Overlap** | | **558** — they differ by one human-entered inventory adjustment |

| Measure on the corrected 558 | Value |
|---|---|
| `create_date` range | 2026-08-26 06:58 → 2026-08-29 10:23 |
| non-zero value | 543 |
| in a category carrying all three accounts | 541 |
| purchase-linked | **61** |
| **carrying an `account_move_id`** | **0** |

**Over-determination-free core: 541 layers** — each with a stock move, a non-zero value, a storable
product, and a category carrying all three accounts, so none of the §7.2 causes can apply.

> **0 of 541. That, not 1,812, is the honest discriminating denominator — and it is still decisive.**

### 8.3 The purchase-linked sub-population is 61 rows, not 1,403

**The receipt-to-GRNI claim rests on far less than the first version implied.**

| Measure | Value |
|---|---|
| Valuation layers on purchase-linked moves | **2,146** |
| — of which migrated (`v14 2026` family) | **2,085** |
| — of which business-document layers in the corrected set | **61** |
| carrying an `account_move_id` | **0** |

The `1,403 done purchase-linked moves / ฿22,953,527.29` figure reproduces exactly, and **2,085 of
its 2,146 layers are migration rows.** It is a statement about the migrated ledger, not about
what the series-18 runtime does. **The runtime statement rests on 61 layers.**

### 8.4 The valuation layers are not internally consistent with the product master

| Measure | Value |
|---|---|
| Done purchase-linked moves | 3,124 |
| — carrying at least one valuation layer | 1,403 |
| — **storable, quantity > 0, and carrying NO layer** | **1,480** |
| Purchase receipts on **non-storable** products that **do** carry a layer | **220** |
| Layers on non-storable products across the whole table | **1,089** |

**Both directions are wrong under normal series-18 behaviour.** The loader that wrote this table on
2026-08-25 did not build layers move-by-move on valuation semantics.

**This weakens every behavioural inference drawn across the full 47,801 — the periodic one
included** — and it is a finding in its own right. It is the reason §8.2's corrected set is
restricted to layers with a human author and a real business document.

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
| The 0-of-47,801 zero-link result on `account_move_id` | **EXPECTED UNDER PERIODIC POLICY — VERIFIED, scoped to 43,227 rows.** For 4,574 rows (9.57%) it is **over-determined** by three valuation-independent causes |
| The 0-of-47,801 on `account_move_line_id` | **NOT EXPLAINED BY PERIODIC POLICY.** A non-valuation-gated writer exists (§7.1). **CORRECTED** |
| The same zero on the corrected 558-row business-document set | **EXPECTED UNDER PERIODIC POLICY — VERIFIED** |
| The same zero on the 541-row over-determination-free core | **EXPECTED UNDER PERIODIC POLICY — VERIFIED** — the strongest form available |
| The former "1,812 native layers" set | **WITHDRAWN** — `create_date` is loader-supplied; 1,254 of the 1,812 were `__system__` inventory adjustments (`ERR-P01-27`) |
| The 1,403 purchase-receipt / ฿22,953,527.29 figure | **arithmetically exact, but 2,085 of its 2,146 layers are migrated.** The runtime claim rests on **61** layers |
| `_validate_accounting_entries` is the only writer | **FALSE — CORRECTED.** Six writers; five are periodic-gated, one is gated on `cost_method` (`ERR-P01-26`) |
| A `real_time` counterfactual would have been silently zero anyway | **RULED OUT** — 0 of 86 locations carry a valuation account, and 46,458 of 47,801 layers sit in fully-configured categories |
| Stock journal configuration | **CONFIGURED, NOT EXECUTED — POLICY-DEPENDENT** |
| Whether periodic was *intended* here, given the predecessor posted to `STJ` | **UNRESOLVED — EVIDENCE REQUIRED.** Boss/owner decision, not a P01 decision |
| Whether periodic valuation is *appropriate* for this business | **NOT A P01 DECISION.** Routed to the Boss package |

---

## 12. WHAT WOULD FALSIFY THIS

Stated so a challenger has a target rather than a summary:

1. A product, category or company resolving to `real_time` — would require a jsonb value or an
   `ir_default` row that §3 and §4 say does not exist.
2. ~~A **second writer**~~ — **found, and this document is corrected.** See §7.1 and `ERR-P01-26`.
3. ~~Evidence that the 1,812-row native classifier is wrong~~ — **found, and the set is
   withdrawn and replaced.** See §8.1 and `ERR-P01-27`.
4. **A Python method override in a custom module.** This is the residual gap and it is **open**.
   `ir_model_data` bounds field-, model-, view- and data-level extension only — a pure method
   override leaves **no database trace**. **10 of 16 installed custom modules have no
   version-matching source on this host**, so for those ten an override of
   `_validate_accounting_entries`, `_account_entry_move` or `AccountMove._post` is
   **unverifiable by any means available in this session.**
   `scgl_account_coa_control 18.0.1.0.1` is the sharpest instance: it owns four view xmlids and
   zero fields, its name asserts chart-of-accounts control, and its only copy on this volume sits
   in a root P01 declared CLASS C — while this deployment **is** that project's deployment.

   **Every negative in §6 and §7 is therefore scoped as: *no field-level or data-level override;
   method-level override unverified for 10 of 16 custom modules.***

   What *can* be said, measured on the deployment: across **225,529** `ir_model_data` rows,
   **no custom module owns a single xmlid on `stock.valuation.layer`** (positive control: the 16
   custom modules own **1,160** xmlids in total, of which 718 are field definitions). The nine
   `product.category` fields owned by `scgl_product_category_company` are all
   `company_dependent = f` and none is a valuation or property field.

Disproof assignments 1–3 were issued to AAS-03 Expert A. **Two of the three landed**, and this
document has been corrected rather than defended. The outcome is recorded in
`P01_S18_AAS03_FRESH_CHALLENGE.md`; the corrections are logged as `ERR-P01-26` and `ERR-P01-27`
in `P01_RESEARCH_ERROR_AND_REVISION_LOG.md`. **The superseded text is preserved there, not
silently replaced.**
