# P10 — CROSS-PROCESS OWNERSHIP

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1

Which process owns which part of time-based recognition, and what P10 needs from each peer. Peers `P01`–`P09` and `P11` are executing in parallel; where a peer's determination is not yet available the item is recorded as `PEER DEPENDENCY OPEN` and this session continues, per `SMEPLUS-26-09-04-ACC-REV2-CORR1` §7.

---

## 1. Ownership Boundary

| Element | Owner | P10's interest |
|---------|-------|----------------|
| The service or benefit window as a contract fact | `P02` O2C for revenue, `P01` P2P for expense | P10 **consumes** it and must not invent it |
| The measured amount to be recognised | `P01` / `P02` | P10 consumes it and must record the measurement date and rate |
| The recognition schedule derived from those two | **P10** | Owned outright |
| The recognition event and its identity | **P10** | Owned outright — this is P10's core asset |
| The journal entry realising a recognition event | `P04` A2R (the ledger) | P10 supplies the event; A2R owns posting, numbering, hashing and the audit trail |
| Period close, lock dates, reopening | `P04` A2R | P10 must declare what happens to a recognition event whose posting is blocked |
| Fiscal calendar / period grid definition | `P04` A2R | P10 consumes it; it must not be the civil calendar by default |
| Currency and rate policy | `P04` A2R (and the Wave A FX findings) | P10 must state which rate applies to each recognition event |
| Asset depreciation as a domain | Asset module (separate programme) | P10 owns the shared kernel question, not the asset object |
| Statutory presentation and tax treatment | `P07` Tax TH | P10 makes **no** statutory claim |
| Scope semantics reconciliation across processes | `P11` | P10 supplies its scope matrix; P11 reconciles |

## 2. What P10 Consumes From Peers

| # | From | What P10 needs | Status |
|---|------|----------------|--------|
| `X-01` | `P01` P2P | The canonical definition of "the period a purchased service covers", and whether it is a required field on a vendor bill line | `PEER DEPENDENCY OPEN` |
| `X-02` | `P02` O2C | The same for sold services, plus the subscription billing period and whether it may differ from the recognition window | `PEER DEPENDENCY OPEN` |
| `X-03` | `P02` O2C | Whether the delivered-not-invoiced position used by accrual is the same measurement O2C uses for revenue cut-off | `PEER DEPENDENCY OPEN` |
| `X-04` | `P04` A2R | The fiscal calendar object, and confirmation that the recognition grid is fiscal rather than civil | `PEER DEPENDENCY OPEN` — P10 records that the reference behaviour is civil, unconditionally |
| `X-05` | `P04` A2R | Lock-date model and the ruling on whether a posting constraint may alter a recognition period. P10's position: **it may not** | `PEER DEPENDENCY OPEN`; P10 finding `P10-F-05` is the input |
| `X-06` | `P04` A2R | The FX policy for a recognition event: frozen at measurement, or retranslated per period | `PEER DEPENDENCY OPEN`; interacts with the Wave A FX findings, which found a silent one-to-one fallback |
| `X-07` | `P05` E2P | Whether employee-expense prepayments enter the same mechanism | `PEER DEPENDENCY OPEN` |
| `X-08` | `P06` B2R | Whether bank-side prepayments and interest accruals are P10 events or P06 events | `PEER DEPENDENCY OPEN` |
| `X-09` | `P07` Tax TH | Presentation split between prepaid expense and deferred charge; treatment of a reversing accrual crossing a tax period; whether the recognition window has any tax-point significance | `HOLD / EVIDENCE REQUIRED` — routed, no claim made |
| `X-10` | `P11` | Ratification of P10's scope determinations | `PEER DEPENDENCY OPEN` |

## 3. What P10 Supplies to Peers

| # | To | What P10 supplies |
|---|-----|-------------------|
| `Y-01` | `P04` A2R | The recognition event as a ledger input carrying its own period, so that A2R can post it without redefining it |
| `Y-02` | `P04` A2R | The requirement that a re-dated posting must not silently alter a recognition period, and must produce a reportable divergence |
| `Y-03` | `P01` / `P02` | The requirement that a document line carrying a recognition window must record the measurement rate and date with it |
| `Y-04` | `P02` O2C | Notice that in the reference product one field pair simultaneously means recognition schedule, subscription billing period, and statutory electronic-invoice period. **These must be separated in SMEsPlus** |
| `Y-05` | `P07` Tax TH | The full list of statutory questions P10 has deliberately not answered |
| `Y-06` | `P11` | The scope ownership matrix and the two scope defects found |
| `Y-07` | Asset programme | The thirteen-axis comparison and the finding that the reference product's asset object is named for both domains |

## 4. The Overlap That Must Be Resolved by Ruling, Not by Research

**Accrual sits on the boundary between P10 and P01/P02 and cannot be assigned by evidence.**

Its base is a delivered-not-invoiced position — an operational fact owned by the order processes. Its effect is a reversing recognition — a P10 act. In the reference product the mechanism lives in the accounting layer but is driven from the order screens, which is exactly the ambiguity.

Two coherent assignments exist:
- **P10 owns the accrual event; P01/P02 own the measurement.** P10 then requires a stable, reproducible measurement service from the order processes — which the reference product does not have, because its measurement is computed in memory and discarded.
- **P01/P02 own the accrual entirely; P10 owns only schedule-driven recognition.** P10 then loses the ability to enforce one identity and one duplicate control across all time-based effects, which is the main benefit of a kernel.

This is a Boss decision under Stage J of the canonical acquisition flow. It is presented in `16_P10_AAS_PLUS.md` §5 as decision `P10-D-03`.

## 5. Sequencing Constraint

P10's kernel decision (`P10-D-01`) can be taken **before** `X-01`..`X-08` are answered, because the kernel's shape does not depend on which document supplies the window. It **cannot** be taken before `X-05` is ruled, because the separation of recognition period from posting date is the kernel's load-bearing element and belongs jointly to P10 and A2R.

Recorded as: `P10 blocked on X-05 for the kernel decision; unblocked for everything else.`
