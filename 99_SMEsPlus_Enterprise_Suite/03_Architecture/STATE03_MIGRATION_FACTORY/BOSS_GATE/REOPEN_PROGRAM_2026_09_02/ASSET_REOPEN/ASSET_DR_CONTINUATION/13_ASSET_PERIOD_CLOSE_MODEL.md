# 13 — ASSET PERIOD CLOSE MODEL (LEVEL 15)

**LAYER 2 — AUDIT QUARANTINE.** Design content is **DESIGN CANDIDATE**.

---

## 1. What the reference product provides

| Control | Present | Notes |
|---|---|---|
| Fiscal-year lock date | Yes | Per company, with a per-user variant |
| Tax lock date | Yes | |
| Sale lock date | Yes | |
| Purchase lock date | Yes | |
| **Hard lock date** | Yes | The one that cannot be overridden by any user |
| Asset disposal guarded by the lock | **Yes** | Explicit refusal |
| Asset modify guarded by the lock | **Yes** | |
| Rewriting entry accounts guarded | **Partially** | Only entries dated after the lock are rewritten |
| **Asset confirm guarded** | **No explicit guard in the asset module** | `05` §5 — the exposure that matters |
| Asset pause guarded | **No explicit guard** | |
| **A costing close, distinct from the accounting close** | **No** | Does not exist |
| **A production/operational close** | **No** | Does not exist |
| Re-opening a closed period | By moving the lock date back — unless the hard lock blocks it | Blunt |

## 2. Three closes, not one — the design proposal

The reference product has one close. The design needs three, because three different
kinds of fact stop changing at three different times.

| Close | What it freezes | Typical timing | Dependency |
|---|---|---|---|
| **Operational close** | Time logs, machine identity, quantities, downtime causes | Day 1–2 after month end | None — must be first |
| **Costing close** | Depreciation for the period; normal capacity in force; the derived rate; the productive/non-productive split; the reconciliation of `09` §8 | Day 2–5 | **Requires the operational close.** The rate cannot be struck while hours can still change |
| **Accounting close** | Posted journal entries; the statutory ledger | Day 5–10, and legally binding | **Requires the costing close** |

**The dependency is one-directional and must be enforced.** A costing close that can be
struck before the operational close will compute a rate from incomplete hours; an
accounting close that can precede the costing close will post an amount the costing
model has not yet agreed.

**The management ledger (`10`) closes after the costing close and is independent of the
accounting close** — it has no statutory deadline because it has no statutory
presentation (`03` `BLK-04`).

## 3. The three timing problems, and the rules that resolve them

### `T-01` — Machine cost is recognised at order completion, not when the machine ran

Verified: the finished-goods valuation and the labour ledger entry are both produced
when the manufacturing order is marked done.

**Consequence.** An order that runs in January and completes in February puts January's
machine hours into February's inventory value and February's ledger. Under a
monthly-derived rate this is not a small displacement — the January hours are costed at
February's rate.

**Rule — DESIGN CANDIDATE:** cost is attributed to the period **in which the hours were
logged**, not the period in which the order completed. Work in progress at a period end
carries its own period's rate. This requires WIP to be valued at period end, which the
reference product does not do, and is the single largest structural addition the period
model needs.

**Rejected alternative:** costing everything at completion and accepting the
displacement. Rejected because it makes the `09` §8 reconciliation impossible — a
period's depreciation cannot reconcile to allocations that belong to other periods.

### `T-02` — The labour ledger entry is dated *today*, not the production date

Verified from source: the entry that posts work-centre cost to the ledger takes the
**current date**, not the manufacturing order's date and not the period being closed.

**Consequence.** Completing a December order on 3 January posts a **January** entry for
December's production. If December is then locked, the amount is permanently in the
wrong period, and nothing flags it.

**Rule — DESIGN CANDIDATE:** the costing entry carries the **costing period's** date,
not the posting date, and is refused if that period is locked. This inverts the
reference behaviour deliberately.

### `T-03` — The rate moves monthly by construction

A rate derived from monthly depreciation changes every month. Orders spanning a month
end therefore have two candidate rates.

**Rule — DESIGN CANDIDATE:** hours are rated at the rate **in force when the hours were
logged**. An order spanning a month end carries a blended cost made of two exactly
attributable parts. This follows automatically from `T-01` and needs no separate
mechanism.

**And the trap to avoid:** the reference product has a rate field on the work order that
*looks* like a snapshot and is **not read** by the valuation or ledger paths (`08` §5).
SMEsPlus must not repeat the pattern of storing a value that nothing consumes. Either
the snapshot is authoritative or it does not exist.

## 4. Late evidence — the rules

| Event | Before operational close | After operational close, before costing close | After costing close | After accounting close |
|---|---|---|---|---|
| Late time log | Accepted | **Rejected** — reopen the operational close explicitly | Rejected | Rejected |
| Corrected machine identity | Accepted | Accepted, with a correction record | **Correction entry only** | Correction entry in the next open period |
| Late maintenance record | Accepted | Accepted | Correction entry | Next open period |
| Late depreciation posting | n/a | Accepted | **Forces the costing close to be recomputed** | Blocked — see §5 |
| Change to normal capacity | Accepted, prospective | **Rejected for a closed period** | Rejected | Rejected |

**Normal capacity is never changed retrospectively.** It is the denominator that decides
how much cost is capitalised; permitting retrospective change would make inventory
value editable after the fact. This is a firm rule, not a candidate.

## 5. Incomplete manufacturing orders and WIP

| Question | Rule |
|---|---|
| An order open at period end | Its logged hours **are** costed, into WIP, at that period's rate |
| WIP valuation | Required at each period end. **The reference product does not do this** and it must be built |
| An order completed in a later period | Its earlier-period WIP transfers at the value already struck; only later hours take later rates |
| An order cancelled after cost allocation | The allocation is **reversed by a dated correction**, never deleted. `15` `EC-19` |
| A backorder | Inherits its parent's extra-cost basis; hours are its own |

## 6. Can an allocation change after the accounting period closes? — the challenge

The prompt requires this to be challenged rather than assumed.

**The case for allowing it:** costing is management information; refusing to correct a
known error preserves a number everyone knows is wrong.

**The case against, which prevails:** the productive allocation is not management
information alone — it is **inside inventory value**, which is inside the statutory
balance sheet. Changing it after the accounting close changes a statutory figure that
has been reported. That is a prior-period adjustment under TAS 8, not a costing tweak.

**Ruling:**

| Ledger | After the accounting close |
|---|---|
| Productive allocation (statutory inventory) | **Frozen.** Corrections go to the next open period as a dated correction, with the original preserved |
| Non-productive allocation (statutory expense) | **Frozen**, same rule |
| **Management ledger** (`10`) | **May be corrected retrospectively** — it has no statutory presentation. But only by a **dated correction entry**, never by silent restatement |

This asymmetry is deliberate and is the practical benefit of keeping the two ledgers
genuinely separate rather than notionally separate.

## 7. Reopening

| Lock | Reopenable | By whom |
|---|---|---|
| Operational close | Yes, explicitly and with a reason recorded | Production management |
| Costing close | Yes, and **it forces recomputation of the whole period's allocation** — never a partial patch | Costing/finance |
| Accounting close (soft locks) | Yes, by moving the lock | Finance |
| **Accounting close (hard lock)** | **No** | Nobody — this is its purpose |

**A reopened costing close must recompute, not patch.** Because the rate has a
period-wide denominator, changing one machine's hours changes that machine's whole
period. A partial correction would leave the `09` §8 reconciliation failing to close,
which is precisely the condition the reconciliation exists to detect.

## 8. The asset-side close checklist

| # | Step | Control |
|---|---|---|
| 1 | All depreciation entries for the period posted | Sub-ledger to ledger agreement — **a report the reference product does not have and SMEsPlus must** |
| 2 | Asset acquisitions in the period confirmed | Confirm posts the whole life at once — guard against a locked period (`05` §5) |
| 3 | Disposals in the period processed | Already lock-guarded |
| 4 | Production/non-production classification current | `12` §4 |
| 5 | Normal capacity in force recorded and dated | `11` §6 |
| 6 | Operational close complete | Precondition |
| 7 | Rate derived, allocation computed | `09` §3 |
| 8 | **Reconciliation closes to exactly zero, per machine** | `09` §8 — **the gate.** A machine that does not reconcile does not publish a cost |
| 9 | WIP valued | §5 |
| 10 | Costing entries posted with the **period** date | `T-02` |
| 11 | Management ledger period closed | `10` §9 |
| 12 | Accounting close | Last |
