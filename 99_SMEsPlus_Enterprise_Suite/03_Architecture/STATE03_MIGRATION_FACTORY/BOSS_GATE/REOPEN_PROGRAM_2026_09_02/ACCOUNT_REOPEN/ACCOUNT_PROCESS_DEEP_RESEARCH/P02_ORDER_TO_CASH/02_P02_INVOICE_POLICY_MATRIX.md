# 02 — P02 INVOICE POLICY MATRIX

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`

## 0. Mandated Separation

> **INVOICE POLICY ≠ COGS RECOGNITION POLICY.**

This file proves the separation from evidence and then shows exactly where the reference process
fails to keep the two apart.

## 1. The Two Policies Are Held On Different Objects

| Policy | Question it answers | Where it is configured | Scope of the setting |
|---|---|---|---|
| **Invoice policy** | *When may I bill?* | A two-value selection on the **product** | Per product |
| **Cost-recognition policy** | *When does cost of sales arise?* | A boolean on the **company**, plus which account the **product category** points at | Per company × per product category |

`FACT VERIFIED` — `EV-P02-008` (product-level invoice policy), `EV-P02-040` (company-level
recognition boolean), `EV-P02-024` (category-level account choice).

**`FACT VERIFIED` — P02-F-12.** The two policies are configured at **different granularities** and
are **never validated against one another**. A single product can be billed on ordered quantity
while its cost is recognised on invoice, on delivery, or never — and nothing in the configuration
surface shows the combination to the person choosing it.

## 2. Invoice Policy — Complete Enumeration

**DENOMINATOR.** POPULATION: the invoice-policy selection values. PATTERN: the selection literal on
the product template. PATH SET: sales module product template. UNIT: selection value.
**The population is 2 and is complete.** `EV-P02-008`

| Value | Billable quantity formula | Evidence |
|---|---|---|
| `order` (Ordered quantities) | `ordered qty − invoiced qty` | `EV-P02-004` |
| `delivery` (Delivered quantities) | `delivered qty − invoiced qty` | `EV-P02-004` |

**Default assignment** — `FACT VERIFIED` `EV-P02-048`: goods (storable/consumable type) are forced
to `order` whenever the field is empty. Services keep whatever is set. Therefore **the platform
default for physical goods is invoice-on-order, i.e. bill before you ship.**

## 3. Invoice Policy Matrix — All Reachable Combinations

Columns: what actually happened operationally. Rows: the policy. Cells: what the system will let
you bill, and what the accounting consequence is.

| Policy | Nothing delivered | Partially delivered | Fully delivered | Over-delivered |
|---|---|---|---|---|
| **`order`** | **Billable in full.** Revenue and AR recognised for goods that have not left. If cost recognition is on invoice, a cost line is created for inventory that is still on hand. | Billable in full. | Billable in full. | Billable **only up to ordered qty**; the line is flagged as an upselling opportunity and the excess is never billed. `EV-P02-007` |
| **`delivery`** | Not billable (billable qty = 0). | Billable up to delivered qty. | Billable in full. | Billable up to **delivered** qty — i.e. the over-delivery **is** billable, silently, above the ordered quantity. |

**`FACT VERIFIED` — P02-F-13 (ASYMMETRY).** Over-delivery is treated in two opposite ways by the two
policies. Under `order` it is capped and surfaced as a status (`upselling`). Under `delivery` it is
billed without comment. The same physical event — shipping more than was ordered — is a controlled
exception in one configuration and an invisible revenue increase in the other. `EV-P02-004`,
`EV-P02-007`

## 4. The Four Timing Cases The Directive Requires

### 4.1 Order-Based Invoice
Revenue recognised at invoice post, independent of any physical event. `FACT VERIFIED`.
**Accounting consequence:** if cost recognition is on invoice, the cost line is generated from a
cost re-derivation that has **no delivered quantity to consume** — see `03_P02_DELIVERY_COGS_TRACE.md`
§4. The cost falls back to the product's current standard price. Revenue is real; cost is an estimate.

### 4.2 Fulfilment-Based Invoice
Revenue recognised at invoice post, but the *billable quantity* is gated on delivered quantity.
`FACT VERIFIED`. This is the only combination in which billed quantity and relieved inventory are
structurally forced to agree — and even here they agree only if the delivered-quantity field has not
been overwritten by hand (`EV-P02-002`).

### 4.3 Invoice Before Delivery
Reachable in two ways: (a) `order` policy, and (b) a manually created customer invoice with no order
behind it at all. `FACT VERIFIED`.
**Accounting consequence, case (b):** the cost re-derivation has no order line to attach to, so it
does not enter the delivery-aware path at all and returns the product's **standard price** directly.
`EV-P02-019`, `EV-P02-021`. Cost of sales is then a number with no relationship to any inventory
layer, and the offsetting credit lands in the interim account with no delivery entry to match it.
The residual is permanent and silent.

### 4.4 Delivery Before Invoice
The intended shape. Delivery parks the cost in the interim account; the invoice moves it to expense
and the two are matched. `FACT VERIFIED` `EV-P02-041`. Matching is best-effort — see
`01_P02_PROCESS_MAP.md` S8.

## 5. Partial Delivery / Partial Invoice / Backorder

| Case | Billable-quantity behaviour | Tag |
|---|---|---|
| Partial delivery, `delivery` policy | Billable rises with each completed outflow. | `FACT VERIFIED` `EV-P02-004` |
| Partial delivery, `order` policy | Billable is unaffected by delivery entirely. | `FACT VERIFIED` `EV-P02-004` |
| Partial invoice | Each posted or **draft** invoice reduces the remaining billable quantity. | `FACT VERIFIED` `EV-P02-005` |
| Backorder | The undelivered remainder is split to a new movement with its picked marker cleared. Delivered quantity therefore reflects only what was actually picked, not what was planned. | `FACT VERIFIED` `EV-P02-049` |

## 6. Where The Separation Breaks

The directive demands that invoice policy and cost-recognition policy stay separate. In the
reference process they are separate **as configuration** but **coupled at runtime**, in one place:

**`FACT VERIFIED` — P02-F-14 (THE COUPLING).** When cost recognition is on the invoice, the
**quantity** used for the cost line is the **invoice line quantity**, not the delivered quantity.
`EV-P02-016`.

That single decision imports the invoice policy into the cost-recognition policy:

```
   invoice policy  ->  invoice line quantity  ->  cost-of-sales quantity
```

Consequences:

| Scenario | Inventory actually relieved | Cost of sales recognised | Interim account residual |
|---|---|---|---|
| `order` policy, 100 billed, 0 delivered | 0 | 100 × standard price | 100 × standard price, credit, permanent |
| `order` policy, 100 billed, 60 delivered | 60 × layer cost | 60 × layer cost + 40 × standard price | 40 × standard price, credit |
| `delivery` policy, 60 billed, 60 delivered | 60 × layer cost | 60 × layer cost | 0 |
| any policy, 60 delivered, never billed | 60 × layer cost | 0 | 60 × layer cost, debit, permanent |

Rows 1, 2 and 4 all leave a permanent residual in an account that has no owner, no ageing, and no
exception report. `SUPPORTED INTERPRETATION` for the arithmetic; `FACT VERIFIED` for each
underlying mechanism (`EV-P02-016`, `EV-P02-020`, `EV-P02-041`).

## 7. SMEsPlus Design Positions (all `DESIGN CANDIDATE`, none approved)

| # | Position | Rationale |
|---|---|---|
| DC-02-01 | Invoice policy and cost-recognition policy must be **declared together** as one named, versioned, effective-dated *Revenue & Cost Recognition Profile* held at tenant × company level, with the product only selecting a profile. | Removes the unvalidated cross-object combination that produces P02-F-12 and the third row of P02-F-05. |
| DC-02-02 | The cost-of-sales quantity must be sourced from the **outflow ledger**, never from the invoice line. | Breaks the coupling in P02-F-14 at its root. |
| DC-02-03 | Billing a quantity that has not been delivered must produce an explicit **unearned/unshipped** position, not a cost line valued at a fallback price. | Makes row 1 of §6 an accounting fact instead of an estimate. |
| DC-02-04 | Over-delivery must be a single controlled exception with one behaviour, independent of invoice policy. | Removes P02-F-13. |
| DC-02-05 | The "goods delivered not invoiced" position must be a **subledger with mandatory ageing**, and closing a period must require its residual to be explained. | Makes rows 1, 2 and 4 of §6 visible. |

## 8. Negative Claims

| Claim | Classification | Search boundary |
|---|---|---|
| There are exactly two invoice-policy values | `VERIFIED ABSENCE` (of a third) | The selection is a literal on the product template in the sales module and is the complete denominator. Extension modules that could add a value were **not** searched. |
| No validation exists between invoice policy and cost-recognition configuration | `NOT FOUND IN SEARCHED SCOPE` | Searched: product template, product category, company accounting settings, and the invoice-posting cost generator. Not searched: configuration-wizard layers and localisation modules other than the Thai one. |
