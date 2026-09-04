# P10 — ACCRUAL TRACE (ACCRUED EXPENSE AND ACCRUED REVENUE)

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1

---

## 1. What the Accrual Mechanism Is

A **point-in-time estimate**, not a schedule. The operator selects a set of open orders, names a cut-off date and a reversal date, and the mechanism produces exactly two journal entries: the accrual at the cut-off and its reversal one day later by default (`E-P10-024`, `E-P10-025`).

It is a transient wizard. Nothing is stored. There is no accrual object, no schedule, no period set, and no state.

Direction is inferred from the kind of order selected: purchase orders produce accrued expense against a current-liability account; sales orders produce accrued revenue against a current-asset account (`E-P10-024`).

## 2. The Recognition Base — the one genuinely sophisticated part

The base is **not** taken from the order. It is re-derived, at the cut-off date, from delivery and invoicing progress: a shadow copy of the order is built in memory and its received/delivered and invoiced quantities are recomputed *as at the cut-off date*, then the not-yet-invoiced portion is valued (`E-P10-024` and the surrounding method).

This is the only mechanism in P10 that computes a **point-in-time economic position** rather than spreading a known amount. It is also the only one whose base cannot be reproduced from stored data after the fact — the shadow computation is discarded.

Consequence: the accrual amount is **not reproducible** after the source orders progress further. Re-running the wizard at the same cut-off date after a delivery has been recorded produces a different amount, with nothing recording that it did. Classification: `VERIFIED FACT` that the computation is in-memory and discarded; `INFERENCE` for the non-reproducibility, which follows arithmetically and is testable at runtime.

## 3. The Trace

```
Source Document   : one or more open orders (purchase or sale)
Recognition Base  : re-derived delivered-not-invoiced position at the cut-off date
Schedule          : NONE - a single point
Period Event      : NONE
Accounting Event  : the operator's decision to run the wizard
Journal           : two entries - accrual at cut-off, reversal at cut-off + 1 day
Modification      : NONE - the wizard is transient
Reversal          : pre-committed at creation; not conditional on anything
Reporting         : none specific to accruals
Close             : both entries are posted immediately, not softly
```

## 4. Findings

### `P10-F-09` — the audit link back to the source order is dead code

The mechanism builds a collection of "orders that received an entry", returns it, and iterates it to write a chatter note on each order recording the accrual entry and its reversal. **That collection is initialised empty and never appended to anywhere in the module** (`E-P10-027`).

Therefore: no order ever receives the note; no link from order to accrual entry is stored anywhere; the only trace from an accrual entry back to its origin is free text in the entry's reference and line labels.

Class: `VERIFIED FACT`, boundary = the accrual wizard module in reference root `RR-1`, established by enumerating all four occurrences of the identifier in the file. This is the same defect class as the `equipment_sequence` dead code found by the prior Asset round: a declared control whose executor does not exist.

### `P10-F-18` — the reversal is unconditional and pre-dated

The reversal is created and posted at the same instant as the accrual (`E-P10-028`), dated one day later by default. It is not conditional on the real invoice ever arriving, and it does not reference the invoice when it does.

Consequence: if the vendor bill arrives dated **before** the reversal date, the cost is in the books twice for that interval. If it arrives after the accrual period but the accrual was never run for the following period, the cost is missing for that interval. Both are ordinary consequences of the reversing-accrual convention and are accepted practice — but the mechanism provides **no control that detects either state**, because there is no link between the accrual and the invoice that eventually settles it.

### `P10-F-19` — hard posting, no soft posting

Unlike every other mechanism in P10, the accrual posts immediately rather than scheduling (`E-P10-028`). A future-dated accrual is therefore posted now with a future date, rather than being held. Combined with the shared posting layer's silent lock re-dating (`E-P10-036`), an accrual aimed at a locked period lands somewhere else with no warning.

### `P10-F-20` — currency and company handling is stricter here than anywhere else in P10

The wizard refuses mixed-company selections and mixed-currency selections outright, and it carries the foreign-currency amount **only** when exactly one order is selected (`E-P10-026`).

This is the strongest scope control found on any P10 mechanism, and it is worth recording as the positive comparator: it proves that the reference product *can* express "this operation is COMPANY-scoped and denies when the scope is ambiguous" — it simply does not do so on the deferral mechanisms. The multi-order case silently drops the foreign-currency dimension, which is the same defect as `P10-F-04` in a narrower form.

## 5. Accrued Revenue

Same mechanism, opposite direction. The one asymmetry worth noting: on the sales side the base is the *uninvoiced delivered value* including a timesheet-driven variant, and down-payment lines are excluded from the population. On the purchase side no such exclusion exists. Whether that asymmetry is correct is a business question for P01/P02 reconciliation, recorded as a peer dependency in `10_P10_CROSS_PROCESS_OWNERSHIP.md`.

## 6. Scope Determination (`REV2-CORR1`)

| Question | Answer | Basis |
|----------|--------|-------|
| Owning scope of the accrual | **COMPANY** | It is a journal entry with no other home |
| Owning scope of the underlying obligation | **TENANT** (the order is a customer/supplier relationship fact) | Business semantics |
| Executing scope | COMPANY, and **correctly denied when ambiguous** | `E-P10-026` |
| Mutation scope | None — the object is transient | `E-P10-024` |
| Financial effect owner | The company of the selected orders, proven before execution | `E-P10-026` |
| Executing scope == owning scope? | **Yes** — this mechanism gets it right | |

## 7. What SMEsPlus Must Decide Here

Accrual is the mechanism most exposed to Thai statutory treatment, because the accrual basis of taxable income and the accrual basis of accounting do not always coincide, and because a reversing accrual that crosses a tax period has a different consequence from one that does not. Every statutory statement on this point is marked `HOLD / EVIDENCE REQUIRED` and routed to the Accounting-Tax track — see `11_P10_CONTRADICTION_REGISTER.md` `P10-C-06`. No statutory claim is made in this document.
