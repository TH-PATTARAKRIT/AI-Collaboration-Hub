# P01 — PERIOD LOCK / CUT-OFF FORENSIC

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.** Produced by the Code & UI Architect expert; the headline mechanism was
independently re-derived by this session.

---

## 1. CLASSIFICATION

> ### `MIXED — PATH-DEPENDENT`, with a version-dependent overlay
>
> **Nothing that *creates* an accounting fact is ever refused.** Goods receipt, vendor bill,
> journal entry, tax event, payment, and both entries that reconciliation spawns — **all
> re-date**. Only *edits to already-posted* facts are refused. **Reconciliation itself has no
> lock check at all.**

---

## 2. PER-ACTION BEHAVIOUR

| Action | Behaviour when the period is locked |
|---|---|
| Goods receipt | **RE-DATE** |
| Vendor bill posting | **RE-DATE** |
| Journal entry posting | **RE-DATE** |
| Tax event | **RE-DATE** |
| Vendor payment | **RE-DATE** |
| Entries spawned by reconciliation | **RE-DATE** |
| **Reconciliation itself** | **no lock check at all** |
| Editing an already-posted fact | **REFUSE** |

Classification: **FACT VERIFIED** (expert), with the posting re-date path re-derived by this
session.

---

## 3. THE SELF-CONFIRMING CUT-OFF, AND ITS THREE LAYERS

1. Posting **re-dates** the entry to a permitted date.
2. The state write then triggers a guard that reads **the value just rewritten**.
3. The re-date set is a **superset** of the guard set, so **the guard cannot fire on that path**.

Deeper, and more consequential: a date-compute rewrites purchase-document dates **while still in
draft, with no lock involved at all**. In the v16 deployment that accounts for **19.6% of 39,758
dated documents — every one of them with all locks unset.**

> **So date rewriting is not primarily a lock behaviour.** It happens in the ordinary course,
> on a fifth of documents, in a database with no locks configured. Cut-off testing that inspects
> a document's own date is inspecting a value the system routinely chooses.

**The expert first attributed those rewrites to lock enforcement and corrected itself before
publishing.** That correction is preserved here rather than smoothed away.

---

## 4. THE GOODS-RECEIPT LEG

The earlier finding — that the purchase-specific lock never protects goods receipt, because the
lock is selected by journal type while the valuation journal is a general journal — is
**VERIFIED** in both generations and in 8 of 8 deployed journals.

The expert then **understated it twice**, and corrects both:

1. The fiscal-year lock does not refuse the receipt either — **it relocates it**.
2. **The receipt's accounting date was never the receipt date to begin with** — it is the
   posting user's local "today". So there is no original date for a lock to protect.

---

## 5. TWO NEW LOCK FINDINGS IN v19

| # | Finding |
|---|---|
| `X4-PL-02` | v19 **group-gates the re-date warning**, so the users most likely to trigger it cannot see it |
| `X4-PL-04` | v19 catches a lock violation on statement-line un-reconciliation in a `try/except` and **discards it**, producing a silent inconsistent state. **Zero occurrences of this pattern in v18** |

Both are **expert-reported and not re-derived by this session.**

---

## 6. THE DEPLOYED REALITY — WHY MOST OF THIS IS CURRENTLY UNREACHABLE

> Across **90 company rows**, exactly **one** company has any lock date set, and the hard lock
> is unset in **90 of 90**.

**The gaps above are largely unreachable today because there are almost no locks to gap.**

That is the honest framing, and it cuts both ways: the exposure is real in the software and
almost entirely unexercised in these deployments. The one database that *does* have a lock set
is the fourth one — the database this package wrongly recorded as unreadable (`ERR-P01-15`), and
whose transaction data has **not** been analysed.

---

## 7. A CORRECTION TO THIS SESSION'S OWN BRIEF

`period_lock_date` **does exist** — in the v16 deployment, which has **no** sale, purchase or
hard lock columns at all. The earlier statement that the field does not exist is correct **only
for the v18 and v19 source**, and was published without that bound. The lock *vocabulary* itself
is version-dependent, which is a trap for any cross-version lock claim.

---

## 8. DISPOSITION

| Item | Status |
|---|---|
| Period lock classification | **`MIXED — PATH-DEPENDENT`** |
| Cut-off self-confirmation | **FACT VERIFIED**, and broader than a lock issue |
| Receipt leg unprotected | **FACT VERIFIED** |
| v19 warning gating and discarded violation | **expert-reported, not re-derived** |
| Whether any of it is exercised | **almost entirely not, in the three analysed databases** |
| `D4`'s lock data | **NOT YET SEARCHED — class C, known-reachable** |
| Routing | **P08** owns period-close architecture. P01 supplies evidence and decides nothing |
