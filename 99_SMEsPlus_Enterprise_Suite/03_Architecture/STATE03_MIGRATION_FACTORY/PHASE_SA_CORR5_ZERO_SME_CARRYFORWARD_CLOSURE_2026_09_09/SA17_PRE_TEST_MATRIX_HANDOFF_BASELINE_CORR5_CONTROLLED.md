# SA17 — PRE-TEST MATRIX HANDOFF BASELINE — CORR5 CONTROLLED VERSION

> **CONTROLLED VERSION NOTICE.** CORR5-corrected controlled version of
> `PHASE_SA_CROSS_MODULE_ASSURANCE_2026_09_08/SA17_PRE_TEST_MATRIX_HANDOFF_BASELINE.md`. **The historical
> file is not overwritten.** This version governs where the two differ; corrections are marked `[CORR5]`
> with their basis. Authority: `SA_CORR5_06`, master prompt §9.

Status: **PREPARED — NOT EXECUTED**
Governing law: master prompt §21 — Phase SA must **not** execute the Pre-Test Matrix.

---

## 1. What this baseline hands over, and what it does not

**Hands over:** business scenarios, their required inputs, expected outputs, routing, inventory and
accounting impacts, controls, exceptions, expected evidence, unresolved bounded risks, a recommended
scenario priority — **and `[CORR5]` the dependency order of §2a, the three prohibitions of §2b, and the
runtime-only obligation registers of §2c, which travel verbatim.**

**Does not hand over:** executable test cases, test data, expected values, environment definitions, or
any statement that a scenario would succeed.

**`[CORR5]` Readiness vocabulary (master prompt §9):**
- `TRAVERSABLE` / `SA CONTRACT COMPLETE` = *a test case can be written*. **Not** built, proven, verified
  or compliant.
- **Idempotency may not be graded low-risk because a uniqueness carrier exists.** The only carrier in
  the evidenced estate admits unlimited empty values; a uniqueness check over it passes on every row.
- **Tenant isolation, idempotency and cross-module joins are not testable until an implementation and
  an executed test exist**: `0 of 8` isolation proofs · `0 of 60` negative cases · `0 of 13`
  enforcement surfaces · element 15 `specified, not built, not verified`.

---

## 2. Scenario handoff table

Priority rule applied: **a scenario the business performs daily and cannot traverse outranks a scenario
it performs rarely and can.** `[CORR5]` Traversability column reconciled to the CORR5 controlled `SA15`.

| Pri | Scenario | Traversability | Required inputs not yet established | Expected evidence | Bounded risk carried |
|---|---|---|---|---|---|
| 1 | **E2E-01** Customer → Sales → Stock → Delivery → AR → Payment → Bank → Accounting | `WITH NAMED BREAK` | `[CORR5]` Boss elections `TV6-BOSS-01`/`-02` (price/credit defaults), `XD1-P1` (cancellation-gate severity) | movement record; recognition event under `BD-ACC-01`; settlement; reconciliation | The most common SME transaction is not fully traversable |
| 2 | **E2E-05** Dropship | `WITH NAMED BREAK` `[CORR5]` | Boss election `XMC-D-01` (two valuation facts or none); where dropship cost lands (`C2-D-02`) | AR + AP against one commercial act; **a cost recognition bound to the same identity or a recorded determination that none arises (`XMC-C-C6`)** | Control-floor bypass (`SA03-F-02`); `H-03` cost→revenue `NO IDENTITY` |
| 3 | **E2E-04** Sales → Manufacture → RM shortage → Purchase → Production → Delivery | `NOT TRAVERSABLE` | shortage → purchase trigger, ownership, reservation interaction (`C2-D-01`) | linked demand chain; cost accumulation | Two modules must agree on who raises supply |
| 4 | **E2E-07** Kit / bundle | `NOT TRAVERSABLE` | component resolution point (`BN-07`, `IR-12`); `[CORR5]` costing level **resolved** (`SA_CORR3_02`) | component movements; one commercial line | `BD-ACC-03A/03B` set policy at Product Category |
| 5 | **E2E-08** Service → completion evidence → AR | `WITH NAMED BREAK` `[CORR5]` | who asserts completion, when, on what basis (`XMC-C-C2`) — **specified**; no independent event exists | recognition event with no stock movement, carrying asserter, time, basis, obligation | Service recognition rests on a human assertion |
| 6 | **E2E-16** Quality hold → availability → cost timing | `WITH NAMED BREAK` `[CORR5]` | the Quality **object** (absent); the route is evidenced (location-state) | inspection outcome; availability change; cost timing | Sits on the accounting path |
| 7 | **E2E-03** Sales → Manufacture → FG → Delivery → AR | `WITH NAMED BREAK` | BOM/routing operating semantics; `[CORR5]` normal-capacity denominator — Boss restatement `B-6` | consumption, production, variance | Fixed-overhead pool/receiver studied (`SA_CORR3_03`); denominator Boss-owned |
| 8 | **E2E-14** Month close → valuation → AR/AP → Bank → Tax → GL → reporting | `WITH NAMED BREAK` | period object; analytic data; statutory register content | closing position; statements | Three constituent items `PARTIAL` |
| 9 | **E2E-17** Work order → equipment breakdown → maintenance → resume | `WITH NAMED BREAK` `[CORR5]` | production/non-production classification of maintenance cost — 9 of 12 routes close at SMEs Core; `BLK-08` Boss | downtime; cost destination | Route written in a Boss decision |
| 10 | **E2E-18** Project → source facts → analytic dimension → derived view | `WITH NAMED BREAK` `[CORR5]` | derivation mechanism; behaviour when a source fact reverses | derived view with no duplicate truth | **Traversed and found to duplicate financial truth three ways** |
| 11 | **E2E-06** MTO / buy-to-order | `WITH NAMED BREAK` | order→purchase linkage and reservation semantics | linked documents | — |
| 12 | **E2E-09** Purchase → capitalization → depreciation | `WITH NAMED BREAK` | Equipment-side semantics | asset register; schedule; disposal entry | Derecognition entry recorded as draft and deletable |
| 13 | **E2E-10** Expense → approval → payable → payment | `WITH NAMED BREAK` | — | approval record **including that approval occurred** | `XD-03` |
| 14 | **E2E-13** Scrap / by-product / variance | `WITH NAMED BREAK` | `[CORR5]` normal vs abnormal scrap **classes specified** (`SA_CORR5_07` §3.3); cost causality = COGS residual; Thai labels unvalidated | inventory adjustment with reason class; cost effect | Salvage undefined |
| 15 | **E2E-02** Purchase demand → Purchase → Receipt → AP → Payment | `TRAVERSABLE` | — | full chain | Approval internal logic open (A2) |
| 16 | **E2E-11** Sales return | `TRAVERSABLE` | `[CORR5]` reversal cost basis — Boss election `JT-05` | return movement; reversal event referencing the original (`XMC-C-A8`) | Value of the reversal is undecided |
| 17 | **E2E-12** Purchase return | `TRAVERSABLE` | `[CORR5]` return basis conflict `PENDING — INVENTORY INTERNAL RESOLUTION FIRST` | as above | — |
| **18 → gate** | **E2E-15** Correction / reversal / retry / duplicate | **`WITH NAMED BREAK`** `[CORR5]` | **element 15** — identity basis specified (`SA_CORR5_01` `E15-A1`, `XMC-C-A14`), **not built, not verified**; `MTI-50` → `CF-I-03` order | reversal event referencing the original (**specified, established**); **idempotent retry and duplicate detection — MAY NOT be expected as evidence until built**; ordering-independent reconciliation (`XMC-C-A12`) | `[CORR5]` *was "Strongest established area".* **Corrected: weakest proven area — the one dimension that cannot be tested today, and whose test returns clean when it means nothing.** Raised from lowest priority to a **dependency gate on every other scenario's retry/duplicate/join dimension** |

### 2a. `[CORR5]` Dependency order — what must be tested first (from `SA_CORR4_07` §5.2, carried verbatim)

1. **`MTI-50` retention** — `CF-I-03` is unbuildable without a historised grant store; **not partially: at all.**
2. **`CF3-C-01`…`C-04` instrument controls** — synthetic injection, discriminating population, coverage assertion, negative control — **before any positive test.**
3. **`CF3-B-02`** — a grant issued *after* the act must deny.
4. **`CF3-B-07`** — an actor holding grants in two tenants.
5. **The five formerly-unscoped path classes** (`G1`, now specified at `SA_CORR5_02`) — a suite that omits them tests only the paths that were specified.
6. `[CORR5]` **`RT-E15-08` synthetic injection for element 15, and `RT-E15-06` for the attempt identity** — before any scenario's retry dimension is scheduled.

**This order is by dependency; §2's order is by business criticality. Both are held.**

### 2b. `[CORR5]` The three prohibitions — verbatim, from `SA_CORR4_07` §5.1

1. **Nothing may be read as testing tenant isolation until an implementation exists.** `0 of 8` isolation proofs, `0 of 13` enforcement surfaces, `0 of 60` negative cases (52 rejection cells + 8 substitution tests `S-01`…`S-08`).
2. **Nothing may be read as testing idempotency.** The carrier is table-global; `0 of 13,814` rows carry a deduplication key; a test over that population returns clean and means nothing.
3. **Nothing may be read as testing a cross-module join.** Element 15 is the join key; it is specified and not built.

### 2c. `[CORR5]` Runtime-only obligation registers that travel with this baseline

`RT-E15-01`…`-09` (`SA_CORR5_01` §9) · `RT-AUD-01`…`-09` (`SA_CORR5_03`) · `RT-G5-01`…`-07`
(`SA_CORR5_04`) · `RFC-P/N/B/C-*` (`SA_CORR5_05` §8) · `RT-M05-01`, `RT-M33-01`…`-03` (`SA_CORR5_07`)
· `CF3-*` (`SA_CORR4_03` §3.13) · the rejection matrix and `S-01`…`S-08`.

---

## 3. Controls the Pre-Test Matrix must exercise

| Control | Why it must be tested early |
|---|---|
| Approval **occurrence** is recorded, not only assigned | `XD-03`: the occurrence half was populated on 0 of 27,874 rows in the evidenced estate; `[CORR5]` class 14 execution context at `SA_CORR5_02` |
| A cross-module auto-created document meets the target module's own control floor | `SA03-F-02`; `XMC-C-D3` |
| Every accounting-determining constraint holds on non-interface write paths | `SA11-F-02` / ND-06 |
| A period lock binds the entry, not the path | `SA10-F-05` / ND-07 |
| A reservation survives an adjustment | `SA06-F-04` / ND-05 |
| Context-internal transfer neutrality is asserted, not configured | `SA06-F-05`; `[CORR5]` `TRANSFER_INTERNAL` reason class |
| Same-event retry is idempotent; a reversal creates a new event referencing the original | `BD-ACC-01`; `[CORR5]` **testable only after element 15 is built — `RT-E15-01`, `-03`; until then this row is a specification, not a control** |
| No cross-company statutory posting, offsetting or filing | `BD-ACC-02` |
| `[CORR5]` A non-sale stock reduction with no reason class is refused | `MTI-33`; `RT-M33-01` |
| `[CORR5]` An act under a grant later revoked for cause becomes `SUSPECT` without any edit to its record | `CF-I-03R`; `RFC-C-01` |
| `[CORR5]` A background financial process runs one tenant at a time and platform totals equal the sum of per-tenant results | `MTI-29`; `TRG-02`; `RT-G5-05` |

## 4. Nature DNA determinations — carried unchanged (`ND-01`…`ND-08`), plus `[CORR5]`

| # | Determination | Source |
|---|---|---|
| ND-01…ND-08 | as the historical file | as the historical file |
| ND-09 | A cross-module fulfilment that produces revenue must produce a cost recognition bound to the same identity, or an explicit, recorded determination that it does not | `SA_CORR2_01` §4.5 |
| ND-11 | A service recognition event carries its asserter, the time of assertion and the basis asserted, and is itself an Accounting Event | `SA_CORR2_03` §3.1 |
| `[CORR5]` ND-12 | A platform principal is not a tenant user; multi-tenant membership is never a multi-tenant execution context; a platform act names its target tenant as object | `SA_CORR5_02` class 1 |
| `[CORR5]` ND-13 | A reason classification on non-sale reductions binds to a platform-owned class, never to a tenant label | `SA_CORR5_07` §3.3 |

## 5. Mandatory Functional Design record element — unchanged (`SA12-F-01`)

## 6. Bounded risks handed to the next phase

| Risk | Bound |
|---|---|
| Business natures that cannot be routed | `E2E-04`, `E2E-07` — Boss elections `C2-D-01`, `BN-07` resolution point |
| The isolation specification is unproven | 58 invariants specified, **0 proven**; design intent only; `[CORR5]` 25 of 58 re-run at `SA_CORR4_06`, further movements at `SA_CORR5_10` §4 |
| `[CORR5]` **Element 15 is specified and unproven** | `E15-A1`, `XMC-C-A14`; `RT-E15-*`; prohibition 2 |
| Fixed production overhead | narrowed to the normal-capacity denominator, Boss `B-6` |
| `[CORR5]` The COGS residual | `JT-05` (Boss), `GAP-FS-07` (Inventory tracing), TAS 2 confirmations (`HOLD`) — `SA_CORR5_10` §3 |
| The evidence base is thin on the demand-and-supply front end | bounded and measured, `SA00` §7 |
| This session's challenge is not independent | declared, `SA_CORR5_12` |

## 7. What the next phase must not assume

- That `TRAVERSABLE` means a scenario would succeed.
- That the Account interfaces are blocked. Nine are `READY-WITH-DELTA` (`SA13` §4) — **`[CORR5]` on the
  same reading rule: the deltas are named, not closed.**
- That a specification is a control.
- `[CORR5]` **That E2E-15 is low-risk.** It is the one scenario whose expected evidence cannot be produced
  today.
- `[CORR5]` **That any Phase S terminal state or any invariant has been proven by Phase SA.** None has.

---

`SA17 — PREPARED`. The Pre-Test Matrix is **not executed** in this phase.

Boss remains the sole Final Approver.
