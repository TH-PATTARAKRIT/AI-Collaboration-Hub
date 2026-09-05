# 58 — P05 TOLERANCE-ZERO REGISTER V2

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E19`
Supersedes `26`. Population **re-derived, not assumed at 13**.

## 1. Population

The authoritative population is **13** (`TZ-01`..`TZ-13`), re-counted from `26 §3`. No item was added
or dropped by this round; **one is closed and several are re-classed.**

## 2. Register

| ID | Boundary | Live/Latent (v18 target) | Module installed | DB evidence | Runtime | Peer owner | **Status** |
|---|---|---|---|---|---|---|---|
| **`TZ-01`** | Petty-cash spending never credits the float account | **`C` — NOT DECIDABLE** | **yes** | 386/387 land on the float account, **but 100% of linked entries are migration output** | **none exists** | P08 | **HOLD — RUNTIME** (a live posting must be observed) |
| `TZ-02` | `petty.cash` has no company scoping | latent-consequence | yes | 4 companies; **no cross-company posting observed** | — | P08 | **HOLD — DATABASE** (source defect stands; effect not observed) |
| `TZ-03` | Expense fields writable after posting | **LIVE — reachable** | yes | 993 expenses | not tested | P08 | **HOLD — RUNTIME** |
| `TZ-04` | Payment guard omits `journal_id`/`ref` | **LIVE — reachable** | yes | — | not tested | P06/P08 | **HOLD — RUNTIME** |
| `TZ-05` | Raw `state='cancel'` from a non-accounting doc | **LATENT** | **no** (advance module) | table absent | — | P08 | **HOLD — DEPLOYMENT** |
| `TZ-06` | Cross-document duplicates undetected | mixed | partly | `DUP-04` reachable; advance legs vacuous | — | P01/P11 | **HOLD — PEER** |
| `TZ-07` | Advance clearing collapse | **LATENT** | **no** | — | — | P06 | **HOLD — DEPLOYMENT** |
| `TZ-08` | Hashed entry force-cancellable | **LIVE** (core gap) | core | not tested | — | **P08** | **HOLD — PEER** |
| `TZ-09` | Approval enforced in action, not on field | **LIVE — reachable** | yes | 979 sheets | not tested | P08 | **HOLD — RUNTIME** |
| `TZ-10` | Sheet `done`/"Paid" with no entry (`sample`) | **LIVE — reachable** | **`hr_expense_extract` INSTALLED on v18** | not isolated | — | P08 | **HOLD — DATABASE** |
| `TZ-11a` | Vendor down payment never deducted | **LIVE — reachable** in 4 registries, **not** on target | 4 of 6 | 21 wizard rows; **effect NOT observed** | — | **P01** | **HOLD — PEER** |
| `TZ-11b` | Payroll double payment | **LATENT** | uninstalled on v18 | — | — | P08 | **HOLD — DEPLOYMENT** |
| `TZ-12` | `sudo()` vendor-bill creation | **LIVE — reachable**, `PARTIAL AUTHORIZATION` | 4 of 6 | — | reach class C | **P01** | **HOLD — PEER** |
| `TZ-13` | Clearing books a bank receipt that never happened | **LATENT** | **no** | — | — | P06 | **HOLD — DEPLOYMENT** |

## 3. New Candidate — not admitted without adjudication

`PC-01` — **238 of 625 petty-cash sheets have no linked journal entry; 206 are `done`** — is a
financial-integrity/audit-trail exposure at production scale on the target platform. It is **not**
added to the tolerance-zero population by this session: admitting a boundary is a governance act, and
its cause is class **C** (`U-17`). **Recorded as `TZ-CANDIDATE-01`, routed to P08 and PMO.**

## 4. Tally

| Status | Count |
|---|---|
| **CLOSED** | **0** |
| HOLD — RUNTIME | **4** (incl. `TZ-01`) |
| HOLD — DEPLOYMENT | 4 |
| HOLD — DATABASE | 2 |
| HOLD — PEER | 3 |
| **Open** | **13 of 13** |

> **An interim draft of this file closed `TZ-01` as `CLOSED — INVALID ASSUMPTION` and called it the
> programme's first tolerance-zero closure. That was withdrawn within the same round**, after
> AAS-03 Challenge C showed the contradicting evidence was entirely migration output. **No
> tolerance-zero boundary is closed. The count remains 13 of 13 open**, and `no CONDITIONAL PASS may
> bypass any of them`.
>
> The episode is itself the lesson: a boundary closed on a population that never exercised the
> behaviour is not closed.
