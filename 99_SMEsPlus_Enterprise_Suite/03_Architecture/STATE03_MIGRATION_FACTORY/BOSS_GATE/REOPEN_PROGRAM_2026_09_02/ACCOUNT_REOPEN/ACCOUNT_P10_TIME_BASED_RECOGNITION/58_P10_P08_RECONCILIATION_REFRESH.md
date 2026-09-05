# P10 ↔ P08 — RECONCILIATION REFRESH

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D19` (part 1).

---

## 1. Delta Check

| Peer | Last consumed | Current head | Delta |
|------|---------------|--------------|-------|
| `P08` Record-to-Report | `4bdf8a2` | `4bdf8a2` | **NONE** |

**The ledger process has not moved. Per the idempotent-resume rule, it is not reprocessed.** Its positions as consumed in the prior round stand unchanged.

## 2. Positions Carried Forward, With Their Classes Restated

| Position | P10's class for it | Why |
|----------|-------------------|-----|
| No accounting-event object exists in any of 22 roots | **class `C`** at the peer's own scope | The peer's root-set defect was closed for only 3 of ~23 class-`A` claims. P10's own root-scoped search is `FACT VERIFIED` for **one** root |
| Closing a period is moving a date; the ledger has no period object | class `B` — peer-supplied, not re-derived | Load-bearing for `PD-04`; P10 should re-derive it |
| The irrevocable lock relocates rather than refuses | **`FACT VERIFIED`** | P10 re-derived it from source and from an executed test |
| A posted journal item is editable in place | class `B` | Context, not load-bearing |
| The balance invariant has no database-level enforcement | class `B` | Context |
| The peer's gate: 0 of 8, eight tolerance-zero boundaries open | **`FACT VERIFIED`** — its own register | Determines `TZ-7` |

## 3. What P10 Reconciles Here

**Recognition period · posting date · lock date · re-date behaviour · journal mutation · period close.**

| Concept | Owner | P10's position | Status |
|---------|-------|----------------|--------|
| Recognition period | **P10** | Determined by base, window, grid and rule | Held |
| Posting date | **P08** | P10 does not define it | Held |
| Lock date | **P08** | P10 consumes it | Held. **P10 now has the deployed census: 1 of 90 companies has one** |
| Re-date behaviour | **P08** | P10 requires that it not silently alter a recognition period | `BOSS DECISION` — `PD-05`, coupled |
| Journal mutation | **P08** | P10 must assume a posted recognition entry can change | Held |
| **Period close** | **P08** | **P10 must not define core ledger close semantics** | **Held, and explicitly disclaimed** |

## 4. Explicit Disclaimer

> **P10 does not define core ledger close semantics.** Every statement P10 makes about locks, close and re-dating is either an observation of the ledger's behaviour or a **requirement addressed to the ledger owner**. Where P10 has stated a preference — that a recognition period should survive a posting constraint — it is a **recommendation carried to the Boss**, not a rule P10 may impose.

This disclaimer is added because the prior round came close to the opposite: it eliminated an option on a ledger-scoped boundary that no one had adopted.

## 5. Obligations Restated

`OB-01` author the accounting-event object · `OB-02` provide somewhere to record the period an amount belongs to · `OB-03` on a constraint-driven date change, refuse **or record a trace — and where there is no violation to detect, the trace is mandatory** · `OB-04` the untracked post-lock editability of allocations · `OB-05` the currency model for an entry carrying no currency.

`OB-03` is **restated** this round to carry the peer's refinement. The prior wording offered two alternatives; on the lock-free path only one of them exists.
