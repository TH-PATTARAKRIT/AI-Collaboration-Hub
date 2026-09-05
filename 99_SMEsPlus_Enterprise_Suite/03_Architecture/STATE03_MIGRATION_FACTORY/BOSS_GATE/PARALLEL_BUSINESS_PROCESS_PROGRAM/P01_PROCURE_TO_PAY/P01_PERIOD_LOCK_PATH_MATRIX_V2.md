# P01 — PERIOD LOCK PATH MATRIX v2

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.** Produced under an explicit **disproof** assignment; the decisive mechanism was
re-derived by this session.


> ### ⚠ SUPERSEDED — `ERR-P01-41`
>
> Statements below that the **series-16 core source does not exist** are **FALSE**. The enumeration
> covered `/Volumes/iMacSys` and the claim attached to it said *"anywhere"*. Estate-wide there are
> **31 core trees across five series**: 14.0 ×1, **16.0 ×3**, 17.0 ×2, 18.0 ×15, 19.0 ×10 — and
> **every series-14, -16 and -17 tree is under `/Users/admin`**, none on the volume. Verified by
> reading, not listing: `odoo-16.0+e.20230401` carries `version_info = (16, 0, 0, FINAL, 0, '')`,
> **955 addons**, `account/models/account_move.py` 4,200 lines,
> `stock_account/models/product.py` 873 lines, `purchase/models/purchase.py` 1,447 lines, with
> `purchase_stock` and `l10n_th` present. **A search gap, not a source gap.**

---

## 1. CLASSIFICATION

> ### `MIXED — PATH-DEPENDENT` **and** `VERSION-DEPENDENT`
>
> **Operative behaviour on every procure-to-pay path: `SOFT RE-DATE`.**
>
> **Reliance: HOLD** — no lock has ever been exercised in any deployment in this estate.

---

## 2. THE MECHANISM, RE-DERIVED

Two facts, both verified directly by this session:

1. **The posting routine re-dates before it refuses.** It collects the violated lock dates, then
   **assigns a new accounting date** to the move. The refusal check exists, and it runs on
   `write` and `unlink` paths — **edits to already-posted facts** — not on the creation path.
2. **The hard lock is inside the re-dating set.** The violation lookup passes `hard=True`
   alongside the fiscal-year, sale, purchase and tax locks.

> **Therefore even the hard lock does not refuse a posting. It moves it.**

That is the single most counter-intuitive result in the P01 programme: the control named "hard"
is not a stop.

The vendor's own field help says the date *"will be postponed to a later time"* — the behaviour
is documented, not accidental.

## 2.1 The asymmetry an expert derived, and P01 records

The violation set is built with `sale=(journal.type == 'sale')` and
`purchase=(journal.type == 'purchase')`. Because of how the permitted date is then chosen,
**sale documents can be refused under some lock configurations and purchase documents cannot**.

> **A purchase document can never be refused by any lock configuration.**

Classification: **FACT VERIFIED** for the mechanism (re-derived here);
**SUPPORTED INTERPRETATION** for the sale/purchase asymmetry — expert-derived, not independently
re-derived by this session.

---

## 3. THE ELEVEN PATHS — FIVE BEHAVIOURS, NOT TWO

| Path | Behaviour when the period is locked |
|---|---|
| Purchase order | **NOT APPLICABLE** — no accounting fact |
| Goods receipt | **RE-DATE** |
| Valuation | **RE-DATE** |
| Vendor bill | **RE-DATE** |
| Tax event | **RE-DATE** |
| Payment | **RE-DATE** |
| Reconciliation | **RE-DATE**, and see §4 |
| **Return** | **ALLOW** — collapses to the goods-receipt path |
| **Refund / credit note** | **RE-DATE** |
| **Landed cost** | **RELOCATE — and it splits the document from its entry.** See §4.1 |
| **Subcontract receipt** | same as goods receipt |
| *(edits to an already-posted fact)* | **REFUSE** |

**The four paths the prior round never covered — return, refund, landed cost, subcontract —
are where the prior conclusion was weakest, and one of them breaks the pattern.**

---

## 4. THE THREE FINDINGS THE PATH SWEEP PRODUCED

### 4.1 Landed cost splits document from ledger — permanently
The landed-cost **document stays inside the locked period** while its **journal entry is pushed
out**. The two no longer agree, and nothing reconciles them afterwards.
**Expert-reported; not re-derived by this session.**

### 4.2 Cash-basis reconciliation introduces a *third* dating rule
It relocates to **today** — neither the original date nor the lock boundary — and does so using
a lock set that **excludes the tax lock it may be violating**.
**Expert-reported; not re-derived.**

### 4.3 A refusal converted into silent partial execution
One reconciliation path **catches the lock refusal and continues**. The exception is raised and
discarded, leaving the operation partly done.
**Expert-reported; not re-derived.**

---

## 5. THE RELIANCE PROBLEM — WHY ALL OF THIS IS SOURCE-GRADE

> **No lock has ever been exercised anywhere in this estate.**

The one deployment carrying a lock date had it written **one day before the dump was taken, and
after every one of that database's ten journal entries already existed.** The lock has never
been in force while anything was posted.

So the entire matrix above is **source capability**, observed nowhere. `HOLD`.

---

## 6. TWO OVERRIDE CHANNELS — EXPERT-REPORTED

| Channel | Description |
|---|---|
| Self-granted exception | A billing administrator can grant themselves a soft-lock exception **with no reason, no expiry and no second approver**. Zero such rows exist in any deployment |
| **Partner merge** | The contacts merge wizard **defeats both the lock check and the audit-trail guard in one operation** |

The second is the **third independent appearance** in this programme of partner-merge as a
control-bypass primitive — previously found on the company-resolution path and on a hard lock.
**That makes it a systemic property of the reference model, not a local defect.**

---

## 7. A THAI-SPECIFIC FINDING IN THE OPERATING DEPLOYMENT

A custom module adds a **tax-period date outside the lock's control**: **62,351 moves carry it,
and 5,320 diverge from the accounting date — in both directions.**

Separately, the bill date is **unbounded**: two posted vendor bills carry dates of **1967** and
**2568** — the latter a Buddhist-era year entered without conversion.

**Expert-reported; not re-derived.** Routed to **P07** (tax period) and **P08** (period close).
P01 asserts nothing statutory.

---

## 8. CORRECTION TO THIS SESSION'S OWN BRIEF

The brief named a series-16 **source root**. That root holds **58 custom modules and zero core
source**. The distinction is now made throughout: the series-16 **custom** layer is available and
matches the deployment; the series-16 **core** does not exist **on this volume — and that phrasing
is the only part that survived.** It **does** exist under `/Users/admin` (`ERR-P01-41`): three
trees, verified by reading. Series-16 core behaviour is **no longer UNRESOLVED for want of source**
— it is **UNREAD**, and reading it is a concrete action rather than an external dependency.

---

## 9. DISPOSITION

| Item | Status |
|---|---|
| Classification | **`MIXED — PATH-DEPENDENT` and `VERSION-DEPENDENT`** |
| Operative behaviour on P01 paths | **`SOFT RE-DATE`** |
| Hard lock | **also re-dates — FACT VERIFIED** |
| Purchase documents refusable | **No** — SUPPORTED INTERPRETATION |
| Ever exercised | **No, anywhere** |
| Owner | **P08** owns period-close architecture. P01 supplies evidence and decides nothing |
