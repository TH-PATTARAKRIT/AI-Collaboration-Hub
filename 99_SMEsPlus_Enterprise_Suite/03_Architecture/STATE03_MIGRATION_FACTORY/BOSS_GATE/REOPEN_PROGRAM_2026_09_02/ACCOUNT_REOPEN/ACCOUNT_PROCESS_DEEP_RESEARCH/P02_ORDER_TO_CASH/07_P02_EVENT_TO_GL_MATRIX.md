# 07 — P02 EVENT → GENERAL LEDGER MATRIX

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`

Account names below are **role names**, not vendor account names. The mapping from role to a real
account is given in §5 for the Thai chart, whose 27 accounts are a complete enumeration (`EV-P02-044`).

## 1. The Matrix

| AE | Accounting event | Debit | Credit | Amount basis | Tag |
|---|---|---|---|---|---|
| AE-01 | Inventory relief on outflow | *Outbound Stock (Goods Delivered)* | *Inventory Valuation* | quantity × costing-method cost at outflow | `FACT VERIFIED` |
| AE-03b | **Cost of sales debited to Revenue** | *Revenue* | *Outbound Stock (Goods Delivered)* | the AE-03 amount, when the product's accounts yield no expense account — **netting revenue against itself on the same document, with no error** | `FACT VERIFIED` `EV-P02-090` |
| AE-02a | Revenue | *Accounts Receivable* | *Revenue* | invoice line net of discount | `FACT VERIFIED` |
| AE-02b | Output tax | *Accounts Receivable* | *Output VAT* | tax on the post-discount base | `FACT VERIFIED` |
| AE-03 | Cost of sales | *Cost of Sales* — **or, where the product yields no expense account, the sale journal's default account, which the chart sets to *Revenue*** (`EV-P02-090`, `EV-P02-091`) | *Outbound Stock (Goods Delivered)* | **invoice line quantity** × re-derived average cost, with a **standard-price top-up** | `FACT VERIFIED` |
| AE-04 | Interim matching | — | — | matches AE-01 against AE-03 in the outbound stock account; **best-effort, conditional, silent when skipped** | `FACT VERIFIED` |
| AE-05 | Inventory restoration on return | *Inventory Valuation* | *Outbound Stock (Goods Delivered)* | **original layer cost** under FIFO/average; **current standard price** under standard costing | `FACT VERIFIED` |
| AE-06a | Revenue reversal | *Revenue* | *Accounts Receivable* | credit-note line | `FACT VERIFIED` |
| AE-06b | Output tax reversal | *Output VAT* | *Accounts Receivable* | — | `FACT VERIFIED` |
| AE-07 | Cost-of-sales reversal | *Outbound Stock (Goods Delivered)* | *Cost of Sales* | **original cost** if a cancelling reversal or if no order line is linked; **re-derived, and at today's standard price when no physical return exists**, otherwise | `FACT VERIFIED` |
| AE-08 | Receipt | *Outstanding Receipts* | *Accounts Receivable* | payment amount — **or no entry at all** where the payment method line has no outstanding account | `FACT VERIFIED` |
| AE-09 | Realised exchange difference | *FX Loss* **or** *FX Gain* (sign-driven) | the receivable/payable line | the difference between the rate implicit in the invoice and the rate implicit in the payment | `FACT VERIFIED` |
| AE-10 | Cash-basis tax | *Deferred Output VAT (transition)* | *Output VAT* | the proportion settled | `FACT VERIFIED` — **not enabled by the Thai data** |
| AE-11 | Write-off | **a user-chosen account, unconstrained** | *Accounts Receivable* | the payment difference | `FACT VERIFIED` |
| AE-12 | Down payment | *Accounts Receivable* | ***Customer Advances* if configured, otherwise *Revenue*** | down-payment amount | `FACT VERIFIED` |
| AE-13 | Bank reconciliation | *Bank* | *Outstanding Receipts* | statement amount | `SUPPORTED INTERPRETATION` |

## 2. The Complete Life Of One Unit — All Three Configurations

One unit, cost 60, sold for 100, VAT 7%, delivered then invoiced then paid.

### 2.1 Split recognition ON, outbound account = interim asset (generic-chart shape)

```
  Delivery      Dr Outbound Stock            60
                    Cr Inventory Valuation        60
  Invoice post  Dr Accounts Receivable      107
                    Cr Revenue                   100
                    Cr Output VAT                  7
                Dr Cost of Sales             60
                    Cr Outbound Stock             60      <- matched against the delivery leg
  Receipt       Dr Outstanding Receipts     107
                    Cr Accounts Receivable       107
  Bank recon    Dr Bank                     107
                    Cr Outstanding Receipts      107
```
Outbound stock account nets to zero. **This is the intended shape.**

### 2.2 Split recognition OFF, outbound account = expense account

```
  Delivery      Dr Cost of Sales             60
                    Cr Inventory Valuation        60      <- cost recognised HERE
  Invoice post  Dr Accounts Receivable      107
                    Cr Revenue                   100
                    Cr Output VAT                  7      <- NO cost line is added
```
Cost and revenue land in **different periods** whenever delivery and invoice straddle a period end.
`FACT VERIFIED`.

### 2.3 Split recognition OFF, outbound account = interim asset — **the Thai-chart default shape**

```
  Delivery      Dr Outbound Stock            60
                    Cr Inventory Valuation        60
  Invoice post  Dr Accounts Receivable      107
                    Cr Revenue                   100
                    Cr Output VAT                  7      <- NO cost line, ever
```
**Cost of sales is never recognised. The 60 sits in an asset account indefinitely.** Gross profit reads
100 instead of 40. `FACT VERIFIED` — mechanism at `01_P02_PROCESS_MAP.md` S5.

**And under the Thai chart as shipped there is no outbound stock account at all**, so real-time valuation
cannot be enabled without the implementer creating one per company; with valuation left at its
manual default, **the delivery entry does not exist either** and the whole cost side of the diagram is
empty. `FACT VERIFIED` `EV-P02-044`, `EV-P02-045`.

## 3. Where The Ledger Can Be Left Wrong Without Anyone Being Told

| # | Situation | Ledger state | Detection |
|---|---|---|---|
| 1 | Delivered, never invoiced | Outbound stock account carries a **debit** forever | none — no ageing, no exception report |
| 2 | Billed on order, never delivered | Outbound stock account carries a **credit** forever, valued at standard price | none |
| 3 | Outflow completed with no picked line | **Nothing at all** — goods gone, ledger silent | none — there is nothing to query |
| 4 | Interim matching skipped | Both legs sit unmatched | none |
| 5 | Split recognition off with an interim outbound account | Cost of sales **never** recognised | none |
| 6 | Credit note with no physical return | Outbound stock account **debited at today's standard price**, unmatched forever | none |
| 7 | Return with no credit note | Inventory restored, **revenue never reversed** | none |
| 8 | Invoice reset to draft and re-posted after inventory moved | Cost of sales silently **changes value** for the same shipment | none |
| 9 | Valuation entry re-dated by a lock while the layer keeps its creation timestamp | **Inventory valuation report and general ledger disagree** for the period | none — T4 §8 |
| 10 | Down payment with no advances account configured | **Revenue recognised on a deposit** | none |

**`FACT VERIFIED` — P02-F-37 (HEADLINE FOR THIS FILE).** All ten conditions leave the general ledger in a
state that is arithmetically balanced and semantically wrong, and **none of the ten produces an error, a
warning, a queue entry, or an exception report.** The outbound stock account — the single account through
which the entire cost side of P02 flows — has **no owner, no ageing, and no reconciliation control**.

**`DESIGN CANDIDATE` DC-07-01 (highest priority in this package).** In SMEsPlus the
*goods-delivered-not-invoiced* position must be a **controlled subledger**, not a general-ledger account:
per-obligation rows, mandatory ageing, an exception report, and a **period-close gate that requires its
residual to be explained before the period can close.** Nine of the ten rows above become visible the
moment that exists.

## 4. Subledger Ownership

| Subledger | Owner | Controls present in the reference | Tag |
|---|---|---|---|
| Accounts receivable | the customer invoice and its payments | dual residual, matching rows, settlement state | `FACT VERIFIED` |
| Inventory valuation | the valuation layer | ordered and reported by **creation timestamp only** — no accounting date of its own | `FACT VERIFIED` T4 §8 |
| **Goods delivered not invoiced** | **nobody** | **none** | `FACT VERIFIED` |
| Output tax | the tax lines | tax lock date, exigibility filter, tax report | `FACT VERIFIED` |
| Customer advances | the down-payment invoice | **none — the position may not even exist as a liability** | `FACT VERIFIED` T2 §4 |

**Two of the five subledgers this process depends on have no owner and no controls.**

## 5. Role → Thai Chart Account

The Thai chart is a **complete enumeration of 27 accounts** (`EV-P02-044`).

| Role in this matrix | Thai chart account | Present? |
|---|---|---|
| Accounts Receivable | Account Receivable, 1200 | yes |
| Accounts Receivable (point of sale) | Account Receivable (PoS), 1210 | yes |
| Inventory Valuation | Inventory, 1300 | yes |
| Revenue | Income, 4100 | yes |
| Cost of Sales | Cost of Revenue, 5100 | yes |
| Output VAT | Output VAT, 2310 | yes |
| FX Gain / FX Loss | Gain Account 4200 / Loss Account 5500 | yes |
| Withholding suffered (asset) | Withholding Income Tax, 1520 | yes |
| Withholding collected (liability) | Withholding Tax, 2320 | yes |
| Outstanding Receipts | Outstanding Cheques, 1201 — **classified as a current LIABILITY** | **absent in substance.** A receipt not yet cleared at the bank is an **asset** (undeposited funds). A current-liability account named for outstanding cheques is the **payment**-side position, not the receipt-side one. The Thai chart supplies the outbound-cash clearing role and **not** the inbound-cash clearing role. |
| Year-end earnings | Income Summary, 3400 | yes — but **no closing entry posts to it** (T4 §7) |
| **Outbound Stock (Goods Delivered)** | — | **ABSENT** |
| **Inbound Stock (Goods Received)** | Uninvoiced Receipts, 2103 — **defined but wired to nothing** | **absent in substance.** The account exists as a row and occurs nowhere else in the localisation; it is not assigned to the inbound stock property or to any property (`EV-P02-081`). Original claim of a purchase-side advantage **withdrawn** after independent challenge. |
| **Deferred Output VAT (cash-basis transition)** | — | **ABSENT** |
| **Customer Advances / Contract Liability** | — | **ABSENT** |
| **Bad-debt / impairment allowance** | — | **ABSENT** |

**`FACT VERIFIED` — P02-F-38 (THAI CHART GAP, HEADLINE).** Of the 16 account roles this process needs,
**four are absent from the Thai chart and one is only partially present.** The four absent roles are
exactly the four positions where P02 leaves value in limbo: goods delivered not invoiced, deferred output
tax, customer advances, and bad debt. `VERIFIED ABSENCE` within the declared 27-account population.

**`CONTRADICTED` — P02-F-38b, WITHDRAWN AND REPLACED.** This originally claimed that the chart is
structurally asymmetric — purchase side supported, sales side not. **The independent challenge refuted it
and the primary session verified the refutation.** The inbound interim account is defined as a row and is
**wired to nothing** (`EV-P02-081`); the Thai template assigns four property accounts and it is none of
them (`EV-P02-043`).

**Replacement finding — `FACT VERIFIED` — P02-F-38c (UNIFORM ABSENCE).**

| Direction | Interim goods position | Cash clearing position |
|---|---|---|
| **Purchase (P01)** | a defined account, **wired to nothing** | Outstanding Cheques, 1201 — an **outbound-cash** position |
| **Sale (P02)** | **absent** | **absent** |

The chart does not model value in transit **in either direction**. It offers an account name that looks
like the purchase-side interim role and connects it to nothing, and it offers no sales-side equivalent at
all. **Every position P02 needs in order to be auditable between its own events is a position this chart
does not have** — and so is the purchase-side equivalent, which is P01's problem, not a P02 advantage.

The replacement is **simpler and stronger** than the claim it replaces: there is no asymmetry to explain,
only a uniform absence to fill.

**Incidental observation, routed out of P02 scope.** The two accumulated-depreciation accounts in the same
chart are typed as **depreciation expense** rather than as contra-assets. That is an Asset-module concern,
not an O2C one; it is recorded here only because it was observed while enumerating the complete 27-account
population, and is routed to the Asset track without adjudication.

**`HOLD — CROSS-PROCESS RECONCILIATION REQUIRED` — P02-X-02.** The SMEsPlus chart of accounts is a Core
Accounting deliverable, not a P02 deliverable. P02 supplies the requirement: **these five roles must
exist as first-class positions**, and the *goods delivered not invoiced* role must be a controlled
subledger rather than an account. Routed to Core Accounting Reconciliation.
