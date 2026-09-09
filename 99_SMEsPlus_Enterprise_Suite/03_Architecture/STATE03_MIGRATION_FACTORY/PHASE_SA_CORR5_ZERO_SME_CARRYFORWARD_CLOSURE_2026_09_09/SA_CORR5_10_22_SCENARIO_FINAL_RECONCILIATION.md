# SA_CORR5_10 — 22-SCENARIO FINAL RECONCILIATION, BY DIMENSION

## CP-SA-C5-100 — 22-SCENARIO SA-SPEC CLOSURE VERIFIED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR5-ZERO-SME-CARRYFORWARD-001]`
Branch: `architecture/phase-sa-corr5-zero-sme-carryforward-closure-2026-09-09-001`
Boss: **SOLE FINAL APPROVER**

---

## 1. What this file answers, and what it must not be read as

Master prompt §13: classify every scenario **by dimension, not one overloaded status**, and aggregate
into exactly one of `SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED` · `SA-SPEC COMPLETE / PRE-TEST READY`
· `SA MATERIAL GAP — EXACT GAP`. Target: **0 material Phase SA gaps owned by SMEs Core / PMO /
document owner**, and *"do not require runtime proof to satisfy this target."*

**Constants that do not move and are restated so nothing below is read as moving them:** the joint
cross-proof result is **`0 of 22 VERIFIED`** (`JCP3-F-02`'s counterfactual holds — no specification act
verifies a scenario); **`0` invariants proven; `0 of 10` handoffs contract-compliant; `0 of 8 · 0 of 13 ·
0 of 41 · 0 of 60`; 6 vetoes in force, 0 discharged.**

Inputs consumed: `SA_CORR3_06` §3.1 (22 rows), §4.3 (gap classes); `SA_CORR4_07` §4 (22 rows, `PB`
column, `(c)` blockers), §5; `SA_CORR5_01`…`09`; Boss rulings `BD-ACC-01`, `-02`, `-03A`, `-03B`
(2026-09-08).

---

## 2. Dimension vocabulary

| Code | Dimension | `C` means | `B` means | `S` means | `G` means |
|---|---|---|---|---|---|
| **SEM** | Semantic completeness | the business fact and its accounting meaning are stated | a Boss election decides the meaning | — | SMEs Core/PMO/doc-owner gap |
| **IN** | Input completeness | every required input is named with an owner | | | |
| **OUT** | Output completeness | every emitted fact and its consumer are named | | | |
| **RT** | Routing completeness | the flow reaches Inventory / Manufacturing / Purchase as the law requires | | | |
| **IC** | Inventory convergence | Stock Truth reconciliation is stated (`SA_CORR2_05`, `SA_CORR3_08` §4.4) | | | |
| **AC** | Accounting convergence | Financial Truth reconciliation is stated (`SA_CORR2_06`, `SA_CORR3_08` §5; §3 below) | | `S` = a Thai statutory rule slot marked `HOLD / EVIDENCE REQUIRED` (evidence acquisition, Thai Accounting-Tax track) | |
| **TC** | Tenant/Company contract | `XMC-C-D1` + `HF-CTX-*` + `G1`/`G3`/`G5` | | | |
| **ID** | Idempotency contract | `E15-A1`, `XMC-C-A6`…`A9`, `A14` | | | |
| **AU** | Audit/control | `AUD-C`, `CF-I-03`, `CF-I-03R`, named controls | | | |
| **RP** | Runtime proof required | **always `Y`** — no implementation exists | | | |
| **PT** | Pre-Test readiness | `WRITABLE` — a case can be written now; `GATED` — writable only after a named Boss election | | | |

**A `G` in any dimension fails the target. A `B` is a genuine Boss election (category 6). An `S` is a
statutory evidence hold, not a Phase SA gap.** Every cell's basis is in §4's notes column.

---

## 3. The COGS residual, re-measured before the table (`C5-B-04`)

The *"COGS gap, elements 4 and 7"* carried on 12 scenarios named one joint decision: `JT-01`, *which
concept owns valuation policy* — whose *"ultimate design choice (adopt Category-as-owner…) → Boss /
Architecture owner"*. **Boss took it on 2026-09-08:** `BD-ACC-03A` (Periodic | Perpetual, authority =
Product Category) and `BD-ACC-03B` (Standard | Average | FIFO, authority = Product Category), plus the
Product-level override boundary. The closure act: *"must not be re-asked without material delta."*

| COGS decision | State before | **State now** | Basis |
|---|---|---|---|
| `JT-01` valuation policy owner | `NOT DECIDABLE` (2026-09-03) | **RULED — Product Category** | `BD-ACC-03A/03B` |
| `JT-04` recognition timing (*"final event selection → Boss"*) | `NOT DECIDABLE` | **`C10-A1` ANSWERED BY CONSTRUCTION of `BD-ACC-03A`**: *Perpetual* = the cost event is recognised on the **physical event date of the movement** (the movement occurrence is the basis, `XMC-C-A3`); *Periodic* = recognised at **period close over the period's movements**. The reference estate's invoice-vs-delivery instability is a property of the reference, not of SMEsPlus, and is expressly **not inherited** (`SA12-F-01` clause). **`BP-02` "not selectable" (scenario 3) is a reference limitation with no SMEsPlus counterpart** | adjudication; challenge target `SA_CORR5_11` |
| `JT-05` return cost basis (original vs current) | `NOT DECIDABLE` | **Boss policy election — carried, not new** (CORR3/CORR4 lists). SMEs Core recommendation: **original cost** — reverse the cost recognised on the original event (`XMC-C-A8` binds the reversal to the original identity, so the original amount is always recoverable); current-cost reversal manufactures a margin no sale earned. **Thai TAS 2 confirmation (`TH-NEW-02`) `HOLD / EVIDENCE REQUIRED`** | `09_JT05` §4–5 |
| `GAP-FS-07` inter-company path never traced | open | open — an **Inventory evidence act**, Pre-Test-entry obligation | `05_CROSS_CONTEXT_REGISTER_R2` `XCR-01` |
| `SME-Q-02`/`-03` business inputs; `TH-NEW-01` | missing | inputs Boss may take or waive; `TH-NEW-01` statutory `HOLD` | `08_JT04` §4 |

**Consequence for elements 4 and 7:** element 4 = **`N/A` by design with reason** (the producer never
decides recognition timing; the Accounting Core resolves it from the category policy — `SA_CORR3_08`
§2.3 already graded it compliant); element 7 = **carried** (basis, amount, and the method version per
`BD-ACC-03B`). **The "COGS gap" as a 12-scenario blocker dissolves into: `JT-05` on scenarios 8 and 9
(Boss), a statutory `HOLD` where a Thai rule attaches, and `GAP-FS-07` on the inter-company path
(scenario 15's door, Inventory).** `MTI-46`'s value half and `AAS-V-03` follow (`SA_CORR5_09`).

---

## 4. The register

| # | Scenario | SEM | IN | OUT | RT | IC | AC | TC | ID | AU | RP | PT | **Aggregate** | Exact gap / basis |
|---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|---|
| 1 | Stockable purchase receipt → handoff | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | AC: el.4 `N/A` by design, el.7 carried (§3). The reference's *swept suspense* goods-received bridge is **not inherited**: the receipt accrual event and the bill event are two events over one occurrence identity, item-matched by `XMC-C-A3` part 4 (`C10-A2`) |
| 2 | Vendor bill with receipt timing variation | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | *"no prior-period attribution mechanism exists"* was a reference observation. **`XMC-C-A15`/`A16` (§5) state the SMEsPlus obligation**: an event recognised after its physical period carries an explicit prior-period attribution to the original occurrence and is never re-dated (`A9`) |
| 3 | Stockable sales delivery → cost handoff | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | `JT-04` by construction; `BP-02` reference-only (§3) |
| 4 | Customer invoice, delivery timing variation | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | `JT-04` discharged (CORR2); lifecycle interface `XMC-C-B1`…`B7` |
| 5 | Partial receipt | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | *over-receipt tolerance undefined* → **`C10-A3`**: tolerance is a company-scoped configuration record (`CF-I-07`), **default `0` — an over-receipt is refused, never silently accepted** (`MTI-20` direction); a tolerated over-receipt is its own evented fact with a reason class |
| 6 | Partial delivery | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | `H-05` (draft invoice consumes quantity, deletable) is answered by `XMC-C-B2`/`B4`: *draft* is published as **not gate-grade**; no module may gate on it |
| 7 | Backorder | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | `R-17 NO CONSUMER` and *never-mode cancellation leaves no trail* → **`XMC-C-D5`** (§5): a remainder is a first-class demand fact with a named consumer; its cancellation is an evented act with a reason class. The Sales-side **producing design** is a Functional Design obligation (`C4-02-F-04`, `C4-D-01`), forbidden to this round and not a Phase SA gap |
| 8 | Purchase return | C | C | C | C | C | **B** | C | C | C | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss election `JT-05` (return cost basis)`** | route and reversal identity complete (`XMC-C-A8`); the **value** of the reversal is `JT-05`; *"return basis conflict PENDING — INVENTORY INTERNAL RESOLUTION FIRST"* is the same election seen from Inventory |
| 9 | Sales return | C | C | C | C | C | **B** | C | C | C | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss election `JT-05``** | as 8; `TH-NEW-02` TAS 2 confirmation `S` inside the same cell |
| 10 | Cancellation before physical execution | C | C | C | C | C | C | C | C | **B** | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss election `XD1-P1` (cancellation-gate severity default)`** | design resolved (`SA_CORR3_01`); the control's **default severity** is a Boss-reserved election (`B-1`); everything else `C` |
| 11 | Correction after physical execution | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | *corrected-entry link does not exist* (reference) → `XMC-C-A8`/`A9`: reversal + new event, each discoverable from the other; the only correction route after a completed movement is a reversing movement (`INV-F-40`) — **specified** |
| 12 | Inventory count / adjustment | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | *approval mechanism absent* → `FDS_APPROVAL` + class 14 context (`SA_CORR5_02`) + `ND-04` occurrence event + `L7-08` approver ≠ counter; *adjustment silently reduces a reservation* → `ND-05` + `SA06-F-04` control; reason class mandatory (`MTI-33`, `SA_CORR5_07` §3.3) |
| 13 | Scrap / damage / write-off | C | C | C | C | C | C·**S** | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | reason classes incl. `DESTRUCTION_FOR_TAX` specified; **salvage value** = a cost-consequence class with the amount under category policy (`BD-ACC-03B`) — **`S`: `TH-HOLD-02` destruction evidence rule `HOLD / EVIDENCE REQUIRED`** (statutory, not a spec gap); Thai labels unvalidated |
| 14 | Internal warehouse transfer — no financial effect | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | *no independent check* → `SA06-F-05` control (neutrality **asserted**, `SA17` §3) + `TRANSFER_INTERNAL` class + boundary rule `DETERMINED`; the check is a runtime control (`RT-M33-03`-class) |
| 15 | Multi-company / tenant boundary | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | **this scenario is element 10**: `XMC-C-D1` (13/9/10), `G1` 5/5, `G2` re-scoped, `G3` `AUD-C`, `G5` 10/10; `MTI-22` complete at register level. **The cross-company *door* (`XCR-02`) is Boss-gated (`MTI-D-04`) — the *wall* this scenario tests is fully specified.** `0 of 8` proofs, `0 of 60` negatives: runtime |
| 16 | Manufacturing RM → WIP → FG | C | C | C | C | C | **B** | C | C | C | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss restatement `B-6` (`BLK-07` normal-capacity denominator)`** | pool, receiver studied (`SA_CORR3_03`, three of six unblocked); the **denominator** is Boss-owned; fixed-overhead injection path exists as a design once the denominator is elected |
| 17 | Manufacturing reversal / scrap / variance | C | C | C | C | C | **B** | C | C | C | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss restatement `B-6` (`BLK-07`/`BLK-08`)`** | variance owner is one of the six chain elements gated on `B-6`; normal/abnormal scrap classes specified |
| 18 | Stockable vs consumable vs service routing | C | C | C | C | C | C | **B** | C | C | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss election `XMC-D-02` (does the 16-element contract extend beyond Inventory → Accounting?)`** | *two-axis tie-break undefined* → **`XMC-C-D6`** (§5): the physical axis governs Inventory routing and valuation carriage; the category valuation policy (`BD-ACC-03A`) governs whether a stock-affecting line is valued; a line with no physical movement is a Part C assertion event (`XMC-C-C1`). `BD-ACC-01`'s silence for services is drawn by `C1` at SMEs Core (CORR3 §18 *not requested*). **What remains Boss is the element-contract scope for the service leg** |
| 19 | Period-end / cut-off | C | C | C | C | C | C·**S** | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | *no accounting-period object exists* (reference, `G-11`) → **`XMC-C-A15`** (§5): the accounting period as a first-class object with open / closing / closed states; a lock binds the **entry** (`ND-07`); *reconciliation at the closing boundary only* → continuous reconciliation is a runtime control (`RC-09`); **`S`: statutory tax register content `HOLD / EVIDENCE REQUIRED`** |
| 20 | Historical migration across fiscal years | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | *element 14 provenance reference does not exist and must be originated* → **`XMC-C-A17`** (§5) originates its **semantics**: batch identity · source identity · source record reference · mapping rule identity + version · load-act attempt identity (`A14`) · evidence reference; travels **beside** the identity (`A7`); `MTI-42` explicit context assignment; `L10-01`…`-10` context halves. Representation = Functional Design |
| 21 | AI migration mapping + deterministic reconciliation | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | element 14 as 20; **deterministic reconciliation = per-company certification, group total as a sum of certified per-company results** (`L10-07`, quantity half); `MTI-42` prohibits inferring context and `A17`'s mapping-rule identity + version **evidences the compliant act** — closing the *"cannot evidence"* clause |
| 22 | Retry / idempotency / replay | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | **this scenario is element 15** — `SA_CORR5_01`: `E15-A1`, `A6`, `A7`, `A14`; `RISK-C02` specified; `UAE-29` ruled (`BD-ACC-01`); `C-02` dissolved; `RT-E15-01`…`-09` |

### 4.1 Tally, re-derived from the rows

| Aggregate | Scenarios (enumerated) | n |
|---|---|---:|
| **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | 1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 15, 19, 20, 21, 22 | **16** |
| **`SA-SPEC COMPLETE / PRE-TEST READY`** | — | **0** *(no implementation exists; nothing is executable)* |
| **`SA MATERIAL GAP — EXACT GAP`** — every one a **Boss election** | 8, 9 (`JT-05`) · 10 (`XD1-P1`) · 16, 17 (`B-6`) · 18 (`XMC-D-02`) | **6** |
| **Total** | | **22** ✓ |

| Dimension cells | `C` | `B` | `S` (inside a `C` cell) | **`G`** |
|---|---:|---:|---:|---:|
| 22 scenarios × 9 dimensions (SEM…AU) | **192** | **6** | 3 (13, 19, 9) | **0** |

> ### `C5-10-F-01` — the target is met on the dimension that was asked, and the reason must be stated exactly
> **Material Phase SA gaps owned by SMEs Core / PMO / document owner across the 22: `0`.** Six scenarios
> remain `SA MATERIAL GAP` and **every one names a Boss election that pre-dates this round** (`JT-05`,
> `XD1-P1`, `B-6`, `XMC-D-02`); three carry a statutory `HOLD` inside an otherwise complete cell. **This
> is not a claim that 16 scenarios are safe, verified or ready** — `0 of 22` are verified, and all 22
> require an implementation and an executed test. It is the claim that **no further Phase SA round can
> move a single dimension of any of the 22 by SMEs Core work**, which is what the zero-carry-forward gate
> asks.

---

## 5. Contract clauses originated in this file (Phase SA namespace, business-semantic only)

| ID | Clause | Rationale (independent, not inherited) | Challenge target |
|---|---|---|---|
| **`XMC-C-A15`** | **An accounting period is a first-class object** of the company: identity, calendar position, and state (`OPEN` → `CLOSING` → `CLOSED`); every accounting event carries the period it is recognised in; a period lock binds the **entry** (`ND-07`), never the path; closing and re-opening are evented, approved acts (`MTI-40` pattern) | `SA10-F-05` two lock-defeat paths (one leaving no record); `SA_CORR2_06` `AR-20` *"no accounting-period object (`G-11`); re-dating past a lock is the default behaviour"*; the Account programme's evidence that locked-period entries are silently re-dated | yes — is a period object *conceptual design* (authorised) or *data-model design* (authorised under the DNA constitution)? Either is inside the closure act's grant |
| **`XMC-C-A16`** | **Prior-period attribution**: an event whose physical date falls in a `CLOSED` period is recognised in the earliest `OPEN` period **with an explicit attribution reference to the original occurrence and to the closed period**; the original is never re-dated (`A9`); the attribution is itself part of the basis' recognition role, so a same-fact re-presentation stays one event | scenario 2; `A9`; P08 *"locked-period entries silently re-dated"* | yes |
| **`XMC-C-A17`** | **Provenance reference (element 14)** — semantics only: batch identity · source system identity · source record reference · mapping rule identity **and version** · load-act attempt identity (`A14`) · evidence reference; travels beside the event identity, never inside the basis (`A7`); mandatory on every migrated, replayed or recovered fact and `N/A + reason` on every other | `GAP-FS-08`; `MTI-42`; `L10-09`/`-10`; `A7`'s *"companion, not component"* | yes — the strongest objection is that `GAP-FS-08` is *"rank 3, Inventory-owned, not in this authorization"*; the answer is that Phase SA owns the **cross-module contract element** and states its semantics, while the Inventory-side representation remains Inventory's |
| **`XMC-C-D5`** | **A remainder of a partially fulfilled demand is a business fact** with an owner and a named consumer; cancelling a remainder is an evented act carrying a reason class; a remainder may not disappear without a fact recording why | scenario 7 `R-17`; `L6` *never-mode cancellation leaves no trail* | yes |
| **`XMC-C-D6`** | **Routing tie-break**: (1) does the line move stock the company owns? → Inventory routing and a movement fact; (2) if yes, is the product category **valued** under `BD-ACC-03A`? → valuation carriage or explicit `N/A` with reason; (3) if no movement → Part C assertion event. **Precedence is physical > policy > commercial**, and the resolution inputs are retained on the line (`ND-01`) | scenario 18; `XMC-C-C1`; the boundary rule of `03_INVENTORY_FUNCTIONAL_DESIGN_V1` (*where* vs *whether*) | yes |
| **`C10-A1`, `C10-A2`, `C10-A3`** | adjudications in §3 and rows 1, 5 | as stated | yes |

**Five clauses and three adjudications are originated here and reviewed by nobody outside this
session at the time of writing.** They are the first thing `SA_CORR5_11` attacks.

---

## 6. What changed against CORR4, exactly

| | CORR4 | **CORR5** |
|---|---|---|
| Aggregate | 22 `SA MATERIAL GAP` (one overloaded status) | 16 / 0 / 6, by dimension |
| Element 15 dimension | blocks all 22 | `C` on 22 of 22 (`RP` = Y) |
| Context/authorization dimension | `SA CONTRACT COMPLETE — RUNTIME TEST REQUIRED` on 22 | unchanged, now with `G1`/`G3`/`G5` closed |
| "COGS gap el.4/7" on 12 rows | carried | dissolved into `JT-05` (2 rows), statutory `S` (3 cells), `GAP-FS-07` (door) |
| "design mechanism does not exist" on 8 rows | carried as origination acts | 5 answered by existing specification, 3 by originated contract clauses (`A15`/`A16`, `D5`, `D6`) |
| Boss elections in the 22 | 5 (8, 9, 10, 18, 22) | **4 distinct, on 6 scenarios** (`JT-05`, `XD1-P1`, `B-6`, `XMC-D-02`); scenario 22's `C-02`/`UAE-29` dissolved |
| `0 of 22 VERIFIED` | unchanged | **unchanged** |

## 7. Residual

1. **The `C` cells are claims about sufficiency for writing a test, not correctness.** Eighteen of the
   `C` rows rest on CORR2/CORR3 reconciliations reviewed only by same-model challengers.
2. **`C10-A1` (`JT-04` by construction) is the single most consequential adjudication in this package**
   after element 15: it removes a "Joint decision" from twelve rows on the strength of a Boss ruling
   that names the policy values but not the word *timing*. If Boss holds that `BD-ACC-03A` did **not**
   settle timing, twelve rows return to `B` — and the package's recommendation changes. It is stated
   as an adjudication with its reasoning so that reading can be taken deliberately.
3. **Scenario 15's `C` on the routing dimension** depends on distinguishing the *wall* from the *door*;
   a reader who holds that an isolation scenario is incomplete while any cross-company relationship is
   unruled would grade it `B` (`MTI-D-04`). Either way the owner is Boss, not SMEs Core.

## 8. Checkpoint

> ## `CP-SA-C5-100 — 22-SCENARIO SA-SPEC CLOSURE VERIFIED`
> **22 × 9 dimensions: 192 `C` · 6 `B` · 0 `G` · aggregate 16 / 0 / 6 · every remaining gap a
> pre-existing Boss election · 5 contract clauses + 3 adjudications originated · `0 of 22 VERIFIED`
> unchanged · 1 finding (`C5-10-F-01`).**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
