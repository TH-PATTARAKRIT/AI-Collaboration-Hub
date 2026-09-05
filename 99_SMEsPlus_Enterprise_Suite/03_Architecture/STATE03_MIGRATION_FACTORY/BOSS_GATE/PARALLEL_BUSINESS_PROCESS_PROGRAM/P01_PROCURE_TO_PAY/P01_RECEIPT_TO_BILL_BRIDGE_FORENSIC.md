# P01 — RECEIPT → BILL BRIDGE FORENSIC

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-TARGETED-CROSS-PROCESS-CLOSURE-001`
Continuation of `…-REV2-001`. **No reset. No prior evidence discarded.**
Layer: **1.**

> **This file was rewritten twice within this round.** Two earlier readings — one in the
> previous round and one earlier today — were corrected by evidence, once by the author and
> once by an independent expert. Both originals are preserved in
> `P01_RESEARCH_ERROR_AND_REVISION_LOG.md` (`ERR-P01-07`, `-08`, `-09`, `-10`). What follows is
> the third and current reading.

---

## 1. THE EVIDENCE BASE, CORRECTLY LABELLED

An independent expert established, and this session then verified directly, that **the estate
contains no readable deployed v18 database at all**:

| Tag | Actual product version | Evidence | Character |
|---|---|---|---|
| `D1` | **19.0** | module registry: four core module versions all read `19.0.x` | 44 companies; 31 orders; 14,441 movements; **16 journal entries** |
| `D2` | **19.0** | same version family | near-empty |
| `D3` | **16.0** — *not* 18.0 | module registry: the same four core module versions all read `16.0.x` | 5,881 orders; 103,949 movements; 183,590 journal entries |
| `D4` | unknown | not readable by the available tooling | — |

**Every statement made earlier in this session about "the deployed v18 database" was about an
generation-16 database.** Corrected throughout. See `ERR-P01-09`.

Consequence for the programme: **the generation the source analysis targets (v18) has no
deployed representative in this estate.** Source-derived v18 findings cannot be checked against
any running system here.

---

## 2. FINAL CLASSIFICATION

> ### `VERSION-DEPENDENT` — with a deployment-scoped rider
>
> **The receipt-side bridge was removed by design between the generations, not left
> unconfigured.**
>
> - **v16 (`D3`)** — receipt-side valuation exists and operates.
> - **v19 source** — the receipt-side clearing bridge is **deleted**, and inventory is
>   recognised **at the vendor bill**. This is stated in the product's own configuration label:
>   the perpetual option reads **"Perpetual (at invoicing)"**.
> - **v19 deployments** — *neither* route reaches the ledger, because the valuation accounts and
>   the valuation journal are unset. **That is a separate, additional finding** from the design
>   change.

---

## 3. WHAT v19 ACTUALLY DOES — THE CORRECTION THAT MATTERS

Earlier readings in this session treated v19 as having a receipt-side mechanism that was merely
unconfigured. **That was wrong.**

| Fact | Evidence |
|---|---|
| The perpetual valuation option is labelled **"Perpetual (at invoicing)"** in three places in the v19 source | verified directly |
| On a **purchase document**, a storable product whose valuation is perpetual and whose category resolves a valuation account has its **bill line account set to the stock valuation account** | verified directly; path and line recorded in the Layer 2 evidence base |
| The goods-received clearing accounts have **no runtime use** in v19 | verified; the expert corrected the earlier "anywhere" phrasing — 15 hits exist in **test files** |
| The valuation-layer object does not exist in v19 | verified: it is neither a v19 model nor a table in either v19 database |

**So v19 replaced a receipt-time clearing model with an invoice-time recognition model.** The
inventory asset is recognised when the bill is posted, directly, with no intermediate account.
Nothing is "missing" — the business event that carries valuation **moved from the receipt to the
bill**.

This is a coherent design, and it is a **fundamentally different accounting model** from the one
the v18 source analysis describes.

---

## 4. THE SEPARATE DEPLOYMENT FINDING — AND ITS CORRECT CLASS

Independently of the design change, in **both** v19 deployments:

| Configuration | Value |
|---|---|
| Category **valuation account** | set on **0 of 37** |
| Category valuation **journal** | set on **0 of 37** |
| Company-level stock journal | set on **0 of 44** *(the column is **nullable**, correcting an expert's "NOT NULL" characterisation)* |
| Location valuation account | set on **0 of 525** |
| Account-level stock-variation account | set on **0 of 544** |
| Category valuation **policy** | perpetual on 27 of 37 (`D1`), 28 of 37 (`D2`) |
| Inventory closing period | `manual` on 87 of 88 company rows, disabling the periodic route |

Since the v19 bill-line rule requires a resolvable valuation account, and none exists,
**inventory value reaches the general ledger by no route at all** — not at receipt, because
that route was removed; not at invoicing, because the account is unset; and not periodically,
because the closing period is manual.

**That is a larger and better-evidenced finding than the one this session started with**, and
the credit for framing it belongs to the independent expert.

A module named `om_data_remove`, which nulls the category valuation account, is **installed in
all three databases**. It lives in a source root **outside P01's declared path set** — recorded
as a scope gap, not adopted as a cause.

### The class of the deployment claim

**Class `B` — not found in the searched scope — not class `A`.**

The expert's landed attack: `D1` has **zero** done movements from a supplier-usage location.
All 1,201 order-linked receipts arrive from an inter-company transit location, and the
third-party vendor-receipt population across both v19 databases is **2 movements**.

**A deployment-scoped claim about vendor receipts cannot be carried by a population of two.**
The configuration finding stands on its own terms; the behavioural inference from it does not.

---

## 5. CORRECTIONS TO THIS SESSION'S OWN FIGURES

| Earlier statement | Corrected |
|---|---|
| "3,680 movements carry a computed value" | 3,680 **non-null**, of which **2,431 non-zero** |
| "the v18 bridge demonstrably operates" | the **v16** bridge fires on **6,530 of 13,214** receipts — **49.4%**, not universally |
| "no runtime use anywhere in the v19 root" | no runtime use; **15 occurrences exist in test files** |
| "the deployed v18 database" | **the deployed v16 database** |

---

## 6. ANSWERING THE DIRECTIVE'S QUESTION

> *Does the deployed system have a receipt-to-liability accounting bridge?*

| | Answer |
|---|---|
| `D3` (v16) | **Yes**, and it operates on about half of receipts |
| v19 **source** | **No — by design.** Recognition moved to the bill |
| `D1`, `D2` (v19) | **No, and no invoice-time recognition either**, because no valuation account is configured anywhere |

> *If no: how is receive-before-bill represented?*

Operationally only. Quantity moves; a value is computed and stored on the movement; **nothing
reaches the ledger**. There is no accrual and no clearing balance. In v19 that is expected
between receipt and bill *by design*; what is **not** by design is that it never arrives at the
bill either.

---

## 7. THE THREE-DAY TEST

Receive day 5 · consume day 6 · bill day 7.

| | `D3` (v16) | v19 **as designed** | v19 **as deployed** |
|---|---|---|---|
| Day 5 | inventory ↑, clearing ↑ | — (by design) | — |
| Day 6 | inventory ↓, cost recognised | — | — |
| Day 7 | clearing discharged, payable ↑ | **inventory recognised**, payable ↑ | expense ↑, payable ↑ |
| If the period closes on day 6 | purchase is in the period | purchase is absent — **an accepted consequence of invoice-time recognition** | purchase absent, **and inventory never capitalised at all** |

Classification: **SUPPORTED INTERPRETATION**, not executed. Priority-one runtime test.

---

## 8. WHAT THIS FILE DOES NOT CLAIM

- It does not claim v19 is wrong to recognise at invoicing. That is a design choice, and P01
  makes no target-architecture decision.
- It does not claim the v19 deployments intend to leave the accounts unset — `U-02`,
  `HOLD — RUNTIME EVIDENCE REQUIRED`.
- It does not carry a behavioural claim about vendor receipts in the v19 deployments; the
  population is two movements — **class B**.
- It reports no executed behaviour anywhere.
