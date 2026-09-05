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

Companies 2 and 3 carry `ir_default` rows whose value is `false`. That is a **deliberate
un-setting**, not an omission. Company 4 has **no row at all** — an omission. The two are
distinguished here because they are distinguishable in the data and because conflating them is the
`NULL vs empty vs false vs absent` failure mode. Their *effect* is the same; their *provenance* is not.

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

**POSITIVE CONTROLS.** The same counter, over the same parse, returns non-zero freely:
144 distinct accounts appear in the population; the largest are 186 (4,049 items), 211 (3,522),
169 (2,940), 343 (2,408). The largest journals are 45 (8,226), 33 (7,707), 9 (4,504), 34 (4,202).
A zero from this counter is a measurement, not a silence.

**The 2,940 items on account 169 do not come from the valuation path.** Every one of them is in
journal **45 `MIG26 "COA Migration 2026"`**, `move_type = entry`, all posted, dated 2026-01-03 to
2026-08-25, with names of the form `WH/OUT/16353 - …`. Inventory reaches this ledger **only**
through migrated predecessor entries. Debits ฿215,249.69 against credits ฿11,822,573.16.

**CLASSIFICATION: CONFIGURED — VERIFIED. EXECUTED — NO. Cause: POLICY-DEPENDENT.**

---

## 6. WHAT THE UNEXERCISED BRIDGE LEAVES UNRECORDED

Because the bridge never posts, the period between receipt and bill carries **no ledger
recognition of the obligation**.

**POPULATION:** `purchase_order_line`, 21,102 rows, excluding lines on orders in state `cancel`
or `draft`. **UNIT:** one purchase order line. **MEASURE:**
`(qty_received − qty_invoiced) × price_unit`, i.e. gross, pre-tax, in the order currency
(all orders are THB — every company's currency is 133).

| Position | Lines | Gross pre-tax value |
|---|---|---|
| **Received not invoiced** | **1,580** | **฿30,080,689.78** |
| — company 1 | 885 | ฿15,258,362.01 |
| — company 2 | 695 | ฿14,822,327.77 |
| **Invoiced not received** | 183 | ฿1,734,752.87 |

**No accrual is booked against any of it.** 0 of 15,522 journal entries carry `accru` in `ref`
(*positive control:* 15,434 of 15,522 have a non-empty `ref`, and their content is legible —
the migration markers in §9.1 of the policy proof were read from this same field).

### 6.1 How to read this, and how not to

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
| Reachability of the account under current configuration | **LATENT.** Would become live if valuation policy were changed to `real_time`; no other trigger was found |
| ฿30,080,689.78 received-not-invoiced, unrecognised and unaccrued | **FACT VERIFIED**, denominator and unit declared in §6 |
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
