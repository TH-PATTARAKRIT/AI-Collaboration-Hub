# P01 — PROCURE-TO-PAY PROCESS MAP

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.** Contains no reference-system identifiers.
Evidence: cited by ID against `LAYER2_EVIDENCE_QUARANTINE/E00_P01_PRIMARY_EVIDENCE_BASE.md`.
Terminal state of this document: **input to Core Accounting Reconciliation.** Not approved,
not frozen, not implementation authority.

---

## 1. THE SPINE

```
Demand
  → Purchase Request            (optional; project-custom capability only)
  → Request for Quotation
  → Purchase Order              ← commitment, NOT a financial fact
  → Goods Receipt / Service Acceptance
        → Storable  → Inventory Valuation event
        → Consumable→ (no valuation event)
        → Service   → (no receipt-side event at all)
        → Asset     → decided later, at the bill
  → Vendor Bill                 ← the liability event
  → Accounts Payable
  → Withholding decision        (Thai purchases; ownership UNRESOLVED — see §7)
  → Payment
  → Settlement / Reconciliation
  → FX difference               ← arises at settlement, not at bill
  → Reporting
  → Period Close
```

The single most important structural statement this session can make about that spine:

> **It is not one chain. It is at least four chains that share a document set.**

The path a purchase takes is selected not by the buyer's intent but by two configuration
attributes of the item — whether it is *storable*, and whether its valuation mode is
*continuous* or *periodic* — plus one company-level attribute (whether the company runs the
clearing-account model). Those attributes decide which events exist at all, which accounts
are used, and whether the receipt has any accounting consequence. See `P01_RECEIPT_VALUATION_MATRIX.md`.

---

## 2. STAGE-BY-STAGE

### 2.1 Purchase Request

**Not part of the base capability.** A purchase-request capability exists only in the
project's own custom addon sets, in both the v18-line and v19-line copies. Its behaviour and
its accounting consequences (if any) were assigned to the Localization expert and are
reported in `P01_AAS03_EXPERT_CHALLENGE.md`.

Classification: **SUPPORTED INTERPRETATION** — the module exists in the custom sets and is
absent from the four base-generation roots searched. Negative claim class **A within the five
declared roots**; class **C** for every root not searched.

### 2.2 Request for Quotation → Purchase Order

One record carries both. The transition from quotation to order is a **status change plus an
approval timestamp**. `EV-P01-01`.

**No accounting document is created. No journal entry is created. No payable is created.**
Classification: **FACT VERIFIED**, scope `R1`. Class A within that scope.

This confirms the directive's instruction not to assume that an order creates a payable —
in the searched scope it does not.

Two order-stage controls were verified:

| Control | Behaviour | Evidence |
|---|---|---|
| Cancellation guard | An order cannot be cancelled while a related vendor bill exists in any state other than cancelled or draft | `EV-P01-02` |
| Company lock setting | A company-level setting drives an order straight to a terminal state on approval, removing the intermediate state entirely | `EV-P01-03` |

The second is a **semantic hazard**: the same business event (order approved) leaves the
document in two different terminal shapes depending on a company setting, so downstream logic
that tests the order's state is testing a configuration, not a business fact.

### 2.3 The order-stage accrual — a second path to the ledger

There is a **second, independent route from a purchase order to the general ledger** that does
not pass through goods receipt or vendor bill: an accrual routine that posts an expense and a
liability sized from received-but-not-billed quantity, with an automatic reversal at a later
date. `EV-P01-16`.

This matters for `§2.7 BUSINESS EVENT OWNERSHIP` because it means **the purchase order does,
after all, have a path to an accounting effect** — just not through the ordinary chain. The
statement "the order creates no accounting effect" is therefore true of order *confirmation*
and false of the order as a *source document*.

Its integrity rests entirely on the automatic reversal. Two findings weaken that:

1. The accumulator meant to record which orders were accrued is initialised empty and never
   written to, in **both** generations examined. Consequently **no note is posted to the order
   and the order carries no record that an accrual exists**. `EV-P01-17`.
2. No pre-existing-accrual check was found in the routine. Combined with (1), the same order
   set can be accrued repeatedly with no warning and no document-level evidence.

Classification of (1): **FACT VERIFIED** (identifier grep over the whole file, both
generations). Classification of (2): **NOT FOUND IN SEARCHED SCOPE — CLASS B**; the scope
searched was the routine's own file. A guard living elsewhere would not have been seen.

### 2.4 Goods Receipt

Receipt is the point at which operational truth is created. Whether it is also the point at
which *accounting* truth is created depends entirely on item configuration:

| Item shape | Valuation layer | Journal entry | Evidence |
|---|---|---|---|
| Storable, continuous valuation | yes | yes — inventory debited, goods-received clearing credited | `EV-P01-04`,`EV-P01-05` |
| Storable, periodic valuation | yes | **none** | `EV-P01-05` |
| Consumable | none | **none** | `EV-P01-04` |
| Service | no receipt document at all | none | derived from the above |

The consequence: **for three of the four shapes, the goods-receipt event has no accounting
consequence whatsoever, and the entire economic effect of the purchase first appears at the
bill.** Cut-off, accrual completeness and period-close correctness therefore rest on the bill
date for most of the population, and on the receipt date only for one shape.

Two further receipt-stage findings:

- **The accounting date of the receipt entry is not the goods-movement date.** It is a context
  override where one is supplied, otherwise the date of a linked bill line, otherwise **the
  system's current date in the acting user's timezone**. `EV-P01-06`. A receipt processed
  today for goods that moved last month can post into the current period. This directly
  echoes the Account Wave A finding on system-derived accounting dates; that it recurs in a
  second, independent process is evidence the pattern is systemic rather than local.
- **Account resolution fails at transaction time, not at configuration time.** A missing
  clearing account, valuation account or valuation journal raises a blocking error while the
  user is trying to receive goods. `EV-P01-08`. The account may also be overridden per
  storage location, giving a second, quieter configuration surface. `EV-P01-07`.

### 2.5 Classification: Inventory / Expense / Asset

The directive asks who decides. The answer found is uncomfortable:

- **Inventory vs Expense** is decided at the **receipt**, by item configuration.
- **Asset** is decided at the **bill**, by a flag on the **general-ledger account of the bill
  line**, applied automatically at posting and executed with elevated privilege. `EV-P01-18`.

These two mechanisms **compete for the same field**. On a vendor bill, the line's account is
silently replaced by the goods-received clearing account whenever the item is storable and
continuously valued and the company runs the clearing model. `EV-P01-09`. Asset creation then
inspects that replaced account. So for a storable, continuously-valued item, the account the
asset rule reads is the clearing account, not the account the user chose.

Classification: **SUPPORTED INTERPRETATION.** The two mechanisms are each FACT VERIFIED; that
they collide is a reading of their composition and has **not** been confirmed at runtime.
Recorded as `CONTRA-P01-04` and as required runtime evidence.

### 2.6 Vendor Bill — the liability event

The bill is the first point at which every purchase shape produces an accounting effect, and
is therefore the **canonical liability event owner** for P01.

The counter-account of the payable differs by item shape, not by business decision:

| Item shape | Debit side of the bill |
|---|---|
| Storable, continuous valuation, clearing model on | Goods-received clearing account (`EV-P01-09`) |
| Storable, periodic valuation | Item expense account |
| Consumable / service | Item expense account |
| Asset-flagged account | Asset account, then automatic asset creation (`EV-P01-18`) |

### 2.7 Three-way matching

**The three-way-match capability is not in the active base addons root of the generation prior
SMEsPlus rounds cited as the target.** It is present in the archive root of that same build,
in the later generation, and in the project's own custom v19 set. `EV-P01-23`.

Classification: **FACT VERIFIED, class A within the five declared roots.** It is *not* a claim
that the capability is unavailable — only that it is not in the active root of `R1`.

The consequence for design is that quantity-and-price matching between order, receipt and bill
is, in the base capability, **not a gate**. What exists in the base is a bill-to-order
*matching aid* and a set of derived quantities. The detailed lifecycle and matching semantics
were assigned to the Functional Design expert.

### 2.8 Price and quantity differences

Where a bill's price differs from the receipt's valuation, the correction is split:

- for quantity **still on hand**, the valuation layer is corrected;
- for quantity **already consumed**, a journal item is posted to the item's expense account
  against the clearing account. `EV-P01-14`.

Three findings on this mechanism:

1. **If the item has no expense account configured, the price difference for already-consumed
   quantity is silently not posted at all.** `EV-P01-14`. No error, no warning, no suspense
   account. The value simply does not appear.
2. It is generated **only under continuous valuation**. `EV-P01-15`. Under periodic valuation
   no price-difference posting was found — class **A within the price-difference routine**,
   which is gated on the valuation mode; class **C** for any other module that might post one.
3. **The engine decides which receipt a bill line settles by replaying history in the order
   recorded by the audit-log tracking records of the entry's status field**, falling back to
   the record's creation timestamp. `EV-P01-13`.

Finding (3) is the single most architecturally significant item in this package. The financial
outcome depends on a **mail/audit side-table that is not an accounting record**: it can be
purged, it is absent on migrated documents, and it is not part of any accounting control. A
migration that imports historical bills imports no tracking history, so every imported bill
falls to the creation-timestamp branch and the layer matching may differ from the source
system's own result.

### 2.9 Payment

A vendor payment **produces no journal entry at all unless an outstanding-payments account is
configured on it**. `EV-P01-20`. A payment record can therefore exist as an operational fact
with no accounting effect.

### 2.10 Settlement, reconciliation and FX

Foreign-exchange difference entries are created by the **reconciliation engine at settlement**,
not at bill and not at receipt. `EV-P01-21`. The bill therefore carries the rate of the bill
date and the difference emerges only when the payable is matched.

The rate-selection and missing-rate behaviour of each step was assigned to the Code & UI
Architect expert, and interacts with the standing Boss ruling on rate ownership and
missing-rate policy recorded on the Account Wave A track.

### 2.11 Reversal and correction

One finding here is severe enough to state in the process map:

> **Resetting a posted vendor bill to draft, or cancelling it, *deletes* the interim and
> price-difference journal items rather than reversing them.** `EV-P01-11`. Duplicating an
> entry strips them as well. `EV-P01-12`. Resetting a bill to draft also deletes any
> still-draft assets created from it. `EV-P01-19`.

This is a direct contradiction of `§2.13` — *never silently overwrite historical economic
truth*. It is a pattern SMEsPlus must **not** transfer. Recorded as `CONTRA-P01-01`.

### 2.12 Period close

Period-lock enforcement and its bypass surface were assigned to the Code & UI Architect
expert. Two P01-specific interactions are already visible from the evidence above and are
recorded as required cross-checks:

- the receipt entry's date can be forced through a context override (`EV-P01-06`), which is a
  candidate lock-bypass path and must be proven or disproven;
- a manual revaluation routine can change the value of previously-received goods after the
  fact (`EV-P01-22`), which is a candidate route into a closed period.

---

## 3. WHAT THIS MAP DELIBERATELY DOES NOT SAY

- It does not say which generation or copy is deployed. `DEP-P01-01`.
- It does not say what Thai law requires. No statutory source was consulted.
- It does not report runtime behaviour. Nothing here was executed or observed in a database.
- It does not treat the reference system's behaviour as a requirement. Reference source is
  evidence, not authority.
