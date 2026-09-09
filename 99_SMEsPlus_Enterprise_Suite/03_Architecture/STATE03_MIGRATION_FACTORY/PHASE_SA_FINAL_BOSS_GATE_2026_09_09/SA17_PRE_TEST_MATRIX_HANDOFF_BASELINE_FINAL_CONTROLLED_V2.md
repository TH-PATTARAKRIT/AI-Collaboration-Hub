# SA17 — PRE-TEST MATRIX HANDOFF BASELINE — FINAL CONTROLLED VERSION (v2)

> **CONTROLLED VERSION NOTICE.** Supersedes `SA17_PRE_TEST_MATRIX_HANDOFF_BASELINE_CORR5_CONTROLLED.md`
> (CORR5, `379fd073`), which superseded the historical `SA17`. **Neither earlier file is overwritten.**
> This version governs. New corrections `[FG]`; inherited ones keep `[CORR5]`. Authority: `SA_FINAL_01`
> §5, master prompt §6.

Status: **PREPARED — NOT EXECUTED**
Governing law: master prompt §21 of the Phase SA kickoff — Phase SA must **not** execute the Pre-Test
Matrix.

---

## 1. What this baseline hands over

**Hands over:** business scenarios, required inputs, expected outputs, routing, inventory and accounting
impacts, controls, exceptions, expected evidence, unresolved bounded risks, a recommended scenario
priority, `[CORR5]` the dependency order of §2a, the three prohibitions of §2b, the runtime-obligation
registers of §2c, and `[FG]` **the Boss-decision dependency map of §2d**.

**Does not hand over:** executable test cases, test data, expected values, environment definitions, or
any statement that a scenario would succeed.

**Readiness vocabulary** (carried unchanged): `TRAVERSABLE` / `SA CONTRACT COMPLETE` = *a test case can
be written*; **not** built, proven, verified or compliant. **Idempotency may not be graded low-risk
because a uniqueness carrier exists.** **Tenant isolation, idempotency and cross-module joins are not
testable until an implementation and an executed test exist**: `0 of 8` isolation proofs · `0 of 60`
negative cases · `0 of 13` enforcement surfaces · element 15 `specified, not built, not verified`.

---

## 2. Scenario handoff table

Priority rule: **a scenario the business performs daily and cannot traverse outranks one it performs
rarely and can.** `[FG]` Traversability reconciled to `SA15` final controlled v2; the two re-graded
scenarios move down the priority order accordingly, because priority is driven by traversability.

| Pri | Scenario | Traversability | Required inputs not yet established | Expected evidence | Bounded risk carried |
|---|---|---|---|---|---|
| 1 | **E2E-01** Customer → Sales → … → Accounting | `WITH NAMED BREAK` | Boss `F2` (`TV6-BOSS-01`, `XD1-P1`), `TV6-BOSS-02` | movement record; recognition event under `BD-ACC-01`; settlement; reconciliation | The most common SME transaction is not fully traversable |
| 2 | **E2E-05** Dropship | `WITH NAMED BREAK` | Boss `F3` (`XMC-D-01`, `C2-D-02`) | AR + AP against one commercial act; **a cost recognition bound to the same identity or a recorded determination that none arises** (`XMC-C-C6`) | Control-floor bypass (`SA03-F-02`); `H-03` `NO IDENTITY` |
| 3 | **E2E-08** Service → completion evidence → AR | `WITH NAMED BREAK` | none — `XMC-C-C2` specifies asserter, time, basis, obligation | recognition event with no stock movement | Service recognition rests on a human assertion |
| 4 | **E2E-16** Quality hold → availability → cost timing | `WITH NAMED BREAK` | the Quality **object** (absent); route evidenced | inspection outcome; availability change; cost timing | Sits on the accounting path |
| 5 | **E2E-03** Sales → Manufacture → FG → Delivery → AR | `WITH NAMED BREAK` | Boss `F5` (`B-6`, `POH-D-02`) | consumption, production, variance, absorbed overhead | Overhead pool, denominator, receiver and variance now **specified** (`SA_CORR5_10A`); the elections are Boss's |
| 6 | **E2E-14** Month close → … → reporting | `WITH NAMED BREAK` | period object **specified** (`XMC-C-A15`); analytic data; statutory register content | closing position; statements | Three constituent items `PARTIAL` |
| 7 | **E2E-17** Work order → breakdown → maintenance → resume | `WITH NAMED BREAK` | Boss `F5` (`BLK-08`) | downtime; cost destination | 9 of 12 routes close at SMEs Core |
| 8 | **E2E-18** Project → source facts → analytic → derived view | `WITH NAMED BREAK` | derivation mechanism; reversal behaviour | derived view with no duplicate truth | **Traversed and found to duplicate financial truth three ways** |
| 9 | **E2E-04** Sales → Manufacture → RM shortage → Purchase → Production | **`NOT TRAVERSABLE`** | **Boss `F4` (`C2-D-01`)** — the routing *template* exists (`XMC-F-03`) and `BN-04` is `PARTIAL`, **but the target manufacturing state machine has no exit from the shortage state on procurement being raised**, so the shortage→supply hop is unrouted | linked demand chain; cost accumulation | *A first draft of this baseline re-graded this row to `WITH NAMED BREAK` and moved it to priority 9; the re-grade was withdrawn by this session's own challenge (`CHF-03`). The priority position is left here rather than restored to 3, because the break is a Boss election and the rows above it are not — but Boss should know it is the one untraversable flow* |
| 10 | **E2E-06** MTO / buy-to-order | `WITH NAMED BREAK` | order→purchase linkage and reservation semantics | linked documents | — |
| 11 | **E2E-09** Purchase → capitalization → depreciation | `WITH NAMED BREAK` | Equipment-side semantics | asset register; schedule; disposal entry | Derecognition entry recorded as draft and deletable |
| 12 | **E2E-10** Expense → approval → payable → payment | `WITH NAMED BREAK` | — | approval record **including that approval occurred** | `XD-03` |
| 13 | **E2E-13** Scrap / by-product / variance | `WITH NAMED BREAK` | by-product valuation; **Boss `F1` for the cost side** (`F1`'s own card omitted this scenario — `CHF-18`) | inventory adjustment with reason class; cost effect; **salvage as an inbound fact of a distinct product** (`XMC-C-D7`) | Reason classes specified; Thai labels unvalidated |
| 14 | **E2E-11** Sales return | `WITH NAMED BREAK` | Boss `F1` (`JT-05`) | return movement; reversal event referencing the original | Value of the reversal undecided |
| 15 | **E2E-12** Purchase return | `WITH NAMED BREAK` | Boss `F1` (`JT-05`) | as above | return basis `PENDING` |
| 16 | **E2E-02** Purchase demand → … → Payment | **`TRAVERSABLE`** | — | full chain | Approval internal logic open (A2) |
| 17 | **`[FG]` E2E-07** Kit / bundle | **`TRAVERSABLE`** | **none** | component movements; one commercial line; **components carry the cost, the parent is not a valued object** | *was priority 4 and `NOT TRAVERSABLE`.* **No Boss decision required** (`SA_CORR3_02` §11–§12) |
| **18 → gate** | **E2E-15** Correction / reversal / retry / duplicate | `WITH NAMED BREAK` | **element 15** — specified (`E15-A1`, `XMC-C-A14`), **not built**; `MTI-50` → `CF-I-03` order; Boss `F8` for severity | reversal event referencing the original (**established**); **idempotent retry and duplicate detection MAY NOT be expected as evidence until built** | **A dependency gate on every other scenario's retry/duplicate/join dimension** |

### 2a. Dependency order — what must be tested first (carried verbatim)

1. **`MTI-50` retention** — `CF-I-03` is unbuildable without a historised grant store; not partially: at all.
2. **`CF3-C-01`…`C-04` instrument controls** — synthetic injection, discriminating population, coverage assertion, negative control — **before any positive test**.
3. **`CF3-B-02`** — a grant issued *after* the act must deny.
4. **`CF3-B-07`** — an actor holding grants in two tenants.
5. **The five formerly-unscoped path classes** (`G1`, specified at `SA_CORR5_02`).
6. **`RT-E15-08` and `RT-E15-06`** — element-15 and attempt-identity synthetic injection — before any scenario's retry dimension is scheduled.

### 2b. The three prohibitions — verbatim

1. **Nothing may be read as testing tenant isolation until an implementation exists.** `0 of 8` isolation proofs, `0 of 13` enforcement surfaces, `0 of 60` negative cases (52 rejection cells + 8 substitution tests `S-01`…`S-08`).
2. **Nothing may be read as testing idempotency.** The carrier is table-global; `0 of 13,814` rows carry a deduplication key; a test over that population returns clean and means nothing.
3. **Nothing may be read as testing a cross-module join.** Element 15 is the join key; it is specified and not built.

### 2c. Runtime-only obligation registers — eight families

`RT-E15-01`…`-09` · `RT-AUD-01`…`-09` · `RT-G5-01`…`-07` · `RFC-P-01`…`-03`, `RFC-N-01`…`-03`,
`RFC-B-01`…`-02`, `RFC-C-01`…`-02` · `RT-M05-01`, `RT-M33-01`…`-03` · `RT-POH-01`…`-05` ·
`CF3-P/N/B/C-*` · the 52-cell rejection matrix and `S-01`…`S-08`.

**Reading of the historical *"element 15 must not be written"* prohibition** (carried): the case **may
be written**, and **may not be executed or read as passing** until built.

### 2d. `[FG]` Boss-decision dependency map — which family unblocks which scenario

| Boss family | Unblocks | Blocks Pre-Test **entry**? |
|---|---|---|
| `F1` `JT-04` / `JT-05` | expected accounting values on `E2E-01`, `-03`, `-11`, `-12`, **`-13`**; 22-scenario rows 1–6, 8, 9, 16, 17 | No |
| `F2` control defaults | `E2E-01`; rows 5, 10 | No |
| `F3` dropship | `E2E-05`; row 18 | No |
| `F4` `XMC-D-02` / `C2-D-01` | **`E2E-04` — the one untraversable flow** ; `E2E-06`; row 18 | **`XMC-D-02` YES** — it sets how many boundaries the matrix must cover |
| `F5` overhead | `E2E-03`, `-13`, `-17`; rows 16, 17 | No |
| `F6` `MTI-D-04` … | row 15; `CF3-P-04` test data | **`MTI-D-04` YES** — the isolation suite's exception set |
| `F7` `RC-D-01` … | every row's authorization dimension; `AUD-C-A5` | **`RC-D-01` YES** — the negative-access suite's axis denominator |
| `F8` `C-02` | `E2E-15` severity | No — but it sets **exit** criteria |

---

## 3. Controls the Pre-Test Matrix must exercise

Approval **occurrence** recorded, not only assigned (`XD-03`: 0 of 27,874 rows) · a cross-module
auto-created document meets the target module's control floor (`SA03-F-02`, `XMC-C-D3`) · every
accounting-determining constraint holds on non-interface write paths (`SA11-F-02`) · a period lock binds
the entry, not the path (`ND-07`, `XMC-C-A15`) · a reservation survives an adjustment (`ND-05`) ·
transfer neutrality asserted, not configured (`SA06-F-05`) · same-event retry idempotent **— testable
only after element 15 is built** · no cross-company statutory posting (`BD-ACC-02`) · a non-sale
reduction with no reason class is refused (`MTI-33`) · an act under a grant later revoked for cause
becomes `SUSPECT` without any edit (`CF-I-03R`) · a background financial process runs one tenant at a
time and platform totals equal the sum of per-tenant results (`MTI-29`, `TRG-02`).

## 4. Nature DNA determinations carried into Functional Design

`ND-01`…`ND-08` as the historical file · `ND-09` cross-module fulfilment produces a bound cost
recognition or a recorded determination · `ND-10` *Perpetual* at the physical movement, *Periodic* at
period close — **a SMEs Core position carried as the recommendation on Boss `F1`, not Boss-approved** ·
`ND-11` a service recognition event carries asserter, time and basis · `ND-12` an assurance activity
declares its population and its complement · `ND-13` a platform principal's acts name the target tenant
as object and never read tenant business data · `ND-14` a reason classification binds to a
platform-owned class, never a tenant label.

## 5. Mandatory Functional Design record element — unchanged (`SA12-F-01`)

## 6. Bounded risks handed to the next phase

Business natures that cannot be routed — **one: `E2E-04`**, on a Boss-gated structural ground (`CHF-03`); `E2E-07` is re-graded and closed · the isolation specification is unproven (58 invariants, **0 proven**) · **element 15 is
specified and unproven** · fixed production overhead narrowed to Boss `F5` · the COGS residual is Boss
`F1` plus statutory `HOLD`s · the evidence base is thin on the demand-and-supply front end · **this
session's challenge is not independent** (`SA_FINAL_06`).

## 7. What the next phase must not assume

That `TRAVERSABLE` means a scenario would succeed · that the Account interfaces are blocked (nine are
`READY-WITH-DELTA`; the deltas are named, not closed) · that a specification is a control · that
`E2E-15` is low-risk · **`[FG]` that `E2E-07`'s new `TRAVERSABLE` grade means the kit flow is proven —
it means both stated blockers are closed and a test can be written** · that any Phase S terminal state
or any invariant has been proven by Phase SA. **None has.**

---

`SA17 — PREPARED`. The Pre-Test Matrix is **not executed** in this phase.

Boss remains the sole Final Approver.
