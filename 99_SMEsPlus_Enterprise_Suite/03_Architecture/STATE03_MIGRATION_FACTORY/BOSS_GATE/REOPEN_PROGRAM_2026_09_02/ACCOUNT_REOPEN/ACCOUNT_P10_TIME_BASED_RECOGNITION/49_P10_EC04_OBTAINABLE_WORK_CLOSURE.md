# P10 — EC-04 OBTAINABLE WORK CLOSURE

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D11`.

---

## 1. The Criterion, Retrieved

> **`EC-04` — Tolerance-Zero Closed.** *"All applicable tolerance-zero boundaries must be evidence-closed before advancement… `CONDITIONAL PASS` may not bypass a tolerance-zero risk."* Applicable examples include company isolation, financial integrity, unauthorized or duplicate posting, and immutable posted facts.

The prior round wrote that P10 **"cannot"** close it. That was withdrawn as unsupported. This document does the work instead of characterising it.

## 2. Component Register

| # | Tolerance-zero component | Obtainable work this round | Status after this round |
|---|--------------------------|----------------------------|-------------------------|
| `TZ-1` | **Has a recognition entry actually been re-dated in the deployed estate?** | Read the lock columns of all four archives; probe **all four** for entries whose date diverges from their schedule | **PARTIAL — corrected from CLOSED, see `52` `P10-R-13`.** A, B, D: no recognition entries at all, nothing could have been re-dated (`FACT VERIFIED`). C: 30,032 asset-linked entries, **3 candidate signatures**, no lock present, cause undetermined (`UNRESOLVED — EVIDENCE REQUIRED`) |
| `TZ-2` | Is the lock-triggered re-date **reachable** in the deployed estate? | Lock-date census across the full population | **CLOSED — EVIDENCE VERIFIED.** Reachable in 1 of 90 companies; **dormant** there, because that database holds ten journal entries, no recognition entries and no assets |
| `TZ-3` | Is the **lock-free** mutation path reachable and exposed? | — | **HOLD — EXTERNAL EVIDENCE.** Reachable by construction in all four; exposure not enumerated. Owned jointly with the ledger process |
| `TZ-4` | Company-boundary defect 1 — allocation policy resolved from the executing company | Deployed configuration census | **PARTIAL.** All 88 companies in the two multi-company databases hold **one identical configuration**, so the divergence cannot currently arise. The defect is intact; the mitigation is a data state, not a control. **An executing reproduction remains outstanding** |
| `TZ-5` | Company-boundary defect 2 — a company-less report object posting a company-owned entry | Chart-sharing census | **PARTIAL.** 1 of 544 accounts in one database and 0 of 544 in the other are shared, so the loud branch is the likely one today. Conditional, not controlled. **Executing reproduction outstanding** |
| `TZ-6` | Duplicate recognition | — | **HOLD — RUNTIME.** Constructed on paper in round 1; never reproduced |
| `TZ-7` | Immutable posted facts | — | **HOLD — PEER.** The ledger process reports a posted journal item is editable in place, and holds its own gate at 0 of 8 |
| `TZ-8` | Is an executing reproduction actually unavailable? | Checked the host: restore tooling **and initialised database data directories** are present | **RE-CLASSED.** The premise was never tested. `C — NOT ATTEMPTED`, not an environmental fact. **No server was started: that is a state change outside a read-only research session's remit** |

## 3. What Closed, and What It Cost

**One component closed with verified evidence and one moved from unobtained to partial**, from work the prior round called obtainable and did not do. Cost: four archive probes and one column read.

`TZ-1` was first recorded here as closed; that was corrected within the same round when the probe was finally run against the fourth database (`52` `P10-R-13`). The correction is recorded rather than the document being quietly amended.

## 4. What Did Not Close, and Why

| Component | Reason | Whose |
|-----------|--------|-------|
| `TZ-3` | The path is the peer's; its population in P10's mechanisms is unenumerated | Joint — P10 and the ledger owner |
| `TZ-4`, `TZ-5` | Require executing the code, not reading data | P10, blocked on `TZ-8` |
| `TZ-6` | Requires execution | P10 |
| `TZ-7` | The ledger owner holds it at 0 of 8 boundaries closed | Ledger owner |
| `TZ-8` | Attempting it means starting a database service on the user's host — a state change | Boss / operator |

**Correction to the prior round's reasoning, restated:** the earlier wording implied nobody was obliged to do the outstanding work. Three components are P10's, one is blocked only on permission to start a local service, and two are genuinely the ledger owner's. That is an accountability map, not an exemption.

## 5. Status

> **`EC-04`: NOT SATISFIED. Eight components — 1 closed, 3 partial, 3 on hold for external evidence or runtime, 1 re-classed as not attempted.**

The criterion forbids a conditional recommendation from bypassing a tolerance-zero risk, and none is offered.

## 6. The Cheapest Remaining Action

`TZ-8`. Both database data directories on this host are already initialised. Starting one is a state change P10 will not make in a read-only research session, but it is **minutes of operator time**, and it is the only route to closing `TZ-4`, `TZ-5` and `TZ-6` either way. Recorded for the Boss as an operational request, not a research blocker.
