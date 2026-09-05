# 32 — P03 / P04-B-35 RECONCILIATION

**LAYER 2 — AUDIT QUARANTINE.**

---

## 1. Authoritative definitions, retrieved not assumed

| ID | Source | Statement |
|---|---|---|
| `DEP-13` | P03 `14`, added in `25` §6 | Count of work centres with no company. Closes `SCOPE-02`. Status was `HOLD — UAT REQUIRED`, one query |
| `P04-B-35` / `P04-PD-01` | P04 message; blocker register `10_P04_BLOCKER_REGISTER.md` on `research/account-p04-acquire-to-retire-2026-09-04-001` | The work centre creates a financial effect and cannot answer which company owns it. High. Closing evidence: one runtime count |

## 2. The reported relationship, tested

P04 reported that `P04-B-35` "may close on one runtime count identified as `DEP-13`". The
directive requires this not be assumed still accurate. **It is no longer accurate**, and
the reason is this round's evidence rather than any change in P04's position:

| Assumption in the reported relationship | Status after execution |
|---|---|
| The count is executable | **TRUE** — executed, `31` §3 |
| The count returns a meaningful population | **FALSE** — 0 rows in all three readable databases |
| A non-zero result would close the blocker | **TRUE in principle**, untestable in practice |
| Therefore the blocker closes on the count | **FALSE** — a vacuous count closes nothing |

## 3. Reconciled status

> **`P04-B-35` — NOT CLOSED. Closing evidence EXECUTED and VACUOUS.**
>
> The specified query is correct and was run read-only across every readable deployed
> database. It returns 0 of 0. The blocker's *mechanism* remains `FACT VERIFIED`; its
> *incidence* is unmeasurable in any deployment currently available.

**`DEP-13` moves from `HOLD — UAT REQUIRED` to `EXECUTED — VACUOUS; awaiting a deployment
with work centres`.** That is a real change of state and not a closure: what was unknown
(can it be run?) is now known, and what remains unknown (what does it show?) is now
precisely bounded.

## 4. P03's amendment to the closing criterion

P03 proposes — and does not impose, since the blocker is P04's — that the criterion be
restated:

> **Current:** one runtime count of work centres with no company.
> **Proposed:** one runtime count of work centres with no company, **in a deployment where
> `mrp_workcenter` is non-empty**; and, absent such a deployment, an explicit statement
> that the incidence is unmeasurable and the mechanism must be treated as present.

The amendment matters because the criterion as written is satisfiable by a zero that means
nothing, which would close a High blocker on no evidence. **This is `P11-D-2` in `37` §4**
— the general form of the problem, which recurs for every latent defect in the programme.

## 5. Notified to P04

P04 is informed of this reconciliation through this file on P03's published branch. Per
`smeplus-peer-intake-discipline`, **a peer's pushed branch is readable**; P04 does not need
a message to obtain it, and P03 makes no claim about whether P04 has read it.

P03 does **not** amend P04's register. That is P04's to do.

## 6. `DEP-04` — the other P04-shared dependency

`DEP-04` (installed-module list) is **PARTIALLY CLOSED** this round — `26` §6 — and is
reported to the Asset track as evidence toward its priority-1 query `Q-04`. P03 does not
close `Q-04`: it was framed against the *running* system, and a dump is not that object.
