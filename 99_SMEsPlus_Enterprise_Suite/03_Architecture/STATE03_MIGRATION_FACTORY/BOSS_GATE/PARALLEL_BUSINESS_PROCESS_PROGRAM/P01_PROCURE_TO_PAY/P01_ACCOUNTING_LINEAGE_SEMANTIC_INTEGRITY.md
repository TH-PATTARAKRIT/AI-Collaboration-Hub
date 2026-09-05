# P01 — ACCOUNTING LINEAGE: SEMANTIC INTEGRITY

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.**

The directive singles this out as material: *account survives, amount survives, but what the
line represented may not.* This document establishes the three lineage kinds separately.

---

## 1. THE THREE KINDS, DEFINED

| Kind | Question it answers | Survives correction? |
|---|---|---|
| **NUMERICAL** | *How much was it?* | usually |
| **ACCOUNTING** | *Which account, which side, which reconciliation?* | partly |
| **BUSINESS SEMANTIC** | *What business event was this? Which receipt, which purchase line, which tax, which advance — and why was it corrected?* | **no** |

---

## 2. WHAT IS DESTROYED

On a delete-based correction the surviving record preserves the account, the label, the balance
and the tax tags. It does **not** preserve:

- the item's **kind** — that it was a valuation line rather than an ordinary expense line;
- its **link to the originating purchase line**;
- product, quantity, partner, analytic distribution, currency;
- **any reason for the correction.**

> **The ledger can be re-added. The story cannot be re-read.**

---

## 3. THE STRUCTURAL POINT — THIS IS NOT ONLY ABOUT DELETION

Business-semantic lineage in procure-to-pay is weak **before** any correction happens:

| Link | State |
|---|---|
| Bill line → order line | explicit — **but `ON DELETE SET NULL` in both deployed series** |
| Receipt movement → order line | explicit — **`ON DELETE SET NULL`** |
| Bill line → the receipt it settles | **derived, not stored**, in the earlier series |
| Order → its accrual entry | **no link at all** |
| Asset → the purchase that created it | **no link** — confirmed with P04 |
| Cross-company generated document → its origin | a chatter message only |

> **Deleting one order line severs the bill's origin and the receipt's purpose in a single
> operation, leaving both documents present and internally valid.**

Correction-by-deletion does not create the semantic gap. **It widens a gap the model already
has.**

---

## 4. WHY THE AUDIT RECORD DOES NOT CLOSE IT

Even where a deletion is logged, the record is **field-level**: it says *this field changed from
A to B*. It cannot express *this line was the valuation half of receipt #N against purchase line
#M*, because that meaning was never in a tracked field.

And empirically, the record cannot distinguish a **destroy-and-recreate of the same line** from a
genuine deletion — the two present identically.

---

## 5. WHAT THIS MEANS FOR THE TARGET DESIGN

Stated as learning; **P01 makes no target-architecture decision.**

1. **Business-semantic lineage must be a stored relationship, not an inference** — a first-class
   link from every derived journal item to the business event that caused it.
2. **A correction must record its reason**, and a field-level diff is not a reason.
3. **Referential severance must not be silent** — a link that nulls itself on delete destroys
   provenance without any record that provenance existed.
4. **An audit trail that cannot distinguish deletion from re-issue is not an audit trail.**

---

## 6. CLASSIFICATION

| Claim | Class |
|---|---|
| Numerical lineage usually survives | **SUPPORTED INTERPRETATION** |
| Accounting lineage partly survives | **SUPPORTED INTERPRETATION** |
| **Business-semantic lineage does not survive a delete-based correction** | **FACT VERIFIED** — the destroyed fields are enumerable and none carries the business meaning |
| The links are `ON DELETE SET NULL` in both deployed series | **FACT VERIFIED** — deployed schemas, cross-series |
| Unlogged destruction occurs and outnumbers logged | **expert-reported, not re-derived** |

---

## 7. ROUTING

**P08** owns audit and correction architecture. **P11** reconciles the event-identity question
across processes. P01 supplies the evidence and asserts no design.
