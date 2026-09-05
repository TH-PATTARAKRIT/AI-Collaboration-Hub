# P01 — SERIES-16 RECEIPT → VENDOR BILL → AP TRACE

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S16-04` · Deployment `45a8e08e` (`iSMEs`, SWR), 1 company

> ### CORRECTED — the GRNI totals below are ALL-STATES figures
>
> Verified after publication: the GRN net of **฿72,097,814.25** includes **70 cancelled and draft items**.
> **Posted-only the account nets to −฿7,048,692.08 — the opposite sign.** The 6,653-line bill relief
> likewise includes **฿175,017,092.70** on cancelled or draft bills. See
> `P01_S16_RECEIPT_VALUATION_CLEARING_DIRECT_PROOF.md §6`.

---

## 1. POPULATION

| Object | Rows |
|---|---|
| `purchase_order` | **5,881** — purchase 5,756 / draft 53 / cancel 71 / to approve 1 |
| — `invoice_status` | invoiced 5,573 / to invoice 97 / no 211 |
| `purchase_order_line` | **10,490** |
| `stock_picking` | **20,098** — done 18,218 / cancel 1,475 / assigned 230 / waiting 131 / draft 41 / confirmed 3 |
| `account_move` `in_invoice` | **37,055** (36,867 posted) |
| `in_refund` | 116 |
| Vendor-bill journal items | **111,912** |
| `account_payment` | **22,468** — supplier 19,575 / customer 2,893 |
| `account_move_line` total | **447,384** across 262 accounts |

**Vendor bills outnumber purchase orders 6:1** (37,055 against 5,881). Most vendor bills in this deployment do
not originate in a purchase order. That is a business-shape fact with direct consequences for three-way match,
and it is the opposite of the series-18 OCC deployment's shape.

---

## 2. WHERE A VENDOR BILL POSTS

| Account type | Journal items on vendor bills |
|---|---|
| `liability_payable` | **37,054** |
| `expense_direct_cost` | 36,640 |
| `asset_current` | 25,063 |
| `liability_current` | 7,844 |
| `expense` | 4,036 |
| `asset_fixed` | 925 |
| `income` | 281 |
| **`None` (no resolvable account type)** | **67** |
| `expense_depreciation` | 2 |

`liability_payable` = 37,054 against 37,055 bills: **one bill carries no payable line.** Recorded as an
observation with its denominator, not as a finding — a single-row anomaly needs its own probe before it is
characterised.

**67 journal items on vendor bills resolve to no account type.** Same treatment: bounded, recorded,
not yet explained.

---

## 3. THE CLEARING BRIDGE CLOSES — THE FIRST TIME P01 HAS OBSERVED IT

| Leg | Evidence |
|---|---|
| Receipt credits the GRN liability | account 39 `2900000 Goods Receipt Note(GRN)`, `liability_current`, **13,736 items**, Cr ฿6,486,344,109.63 |
| **Vendor bill debits it** | **6,653 bill lines**, Dr **฿4,516,394,611.47**, Cr ฿0.00 |
| Residual | ~~net ฿72,097,814.25~~ **all-states figure — posted-only net is −฿7,048,692.08** |

Receipt and bill are joined **by value in the ledger**, not merely by quantity on the order. This is the
mechanism P01 traced in source across four rounds and had never once observed operating.

### 3.1 Three-way match, and why the numbers are small here

**POPULATION:** `purchase_order_line`, 10,490 rows, excluding lines on `cancel`/`draft` orders.
**MEASURE:** `(qty_received − qty_invoiced) × price_unit`, gross, pre-tax, THB.

| Position | Lines | Value |
|---|---|---|
| Received not invoiced | **79** | **฿12,678,776.50** |
| Invoiced not received | **49** | **฿11,512,304.52** |

Compare series-18 OCC: 1,580 lines / ฿30,080,689.78 received-not-invoiced, **with no ledger recognition at all**.

Two differences, and only one of them is favourable:
- **Here the exposure is carried in the ledger** by the GRN account. There it was carried only by the order document.
- **Here most bills are not PO-linked** (37,055 bills against 5,881 orders), so the PO-line quantity comparison
  measures a much smaller slice of purchasing. **The small number is partly a smaller denominator, not only a
  better-controlled process**, and it must not be read as evidence of superior matching.

---

## 4. AP RESOLUTION

| Measure | Value |
|---|---|
| Payable items on vendor bills | 37,054 |
| Supplier payments | 19,575 of 22,468 |
| `account_partial_reconcile` | file extracted, 8.49 MB |
| `account_full_reconcile` | file extracted, 3.00 MB |

Reconciliation machinery is in heavy use. Detailed AP ageing was **not** computed this round and is recorded as
a bounded gap rather than estimated.

---

## 5. WHAT SEMANTIC INFORMATION SURVIVES INTO ACCOUNTING

| Element | Survives? | Evidence |
|---|---|---|
| Vendor identity | yes | partner on bill and payable line |
| Purchase order identity | **only for the PO-linked minority** | 5,881 orders against 37,055 bills |
| Receipt identity | **partially** | valuation-layer `description` carries `WH/IN/…`, `AP…`, `UB/…` document references as **free text**, not as a foreign key |
| Quantity/price basis | on the order line only | `qty_received` / `qty_invoiced` |
| Valuation event | yes, for `real_time` categories | 56,654 layers carry `account_move_id` |
| **Cost-explosion provenance** | **no** | see `P01_S16_RECEIPT_VALUATION_CLEARING_DIRECT_PROOF.md §7` |

**The receipt→bill link is carried by document text and by order-line quantities, not by a referential
accounting identity.** That is the same event-identity weakness P01 recorded from source in earlier rounds,
now observed in a deployment with 183,590 journal entries.

---

## 6. CLASSIFICATION

| Item | Classification |
|---|---|
| GRNI bridge closes: receipt credits, bill debits | **FACT VERIFIED** |
| Net ฿72,097,814.25 GRN residual | **FACT VERIFIED**; its correctness is **P08/P11's**, not P01's |
| Vendor bills outnumber POs 6:1 | **FACT VERIFIED** |
| Small received-not-invoiced figure reflects a smaller PO-linked denominator | **SUPPORTED INTERPRETATION** |
| One bill without a payable line; 67 items with no account type | **FACT VERIFIED** as counts; causes **UNRESOLVED** |
| Receipt→bill identity is textual, not referential | **SUPPORTED INTERPRETATION** |
| AP ageing | **NOT MEASURED** this round |
