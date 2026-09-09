# SA_CORR5_10 — 22-SCENARIO FINAL RECONCILIATION, BY DIMENSION

## CP-SA-C5-100 — 22-SCENARIO SA-SPEC CLOSURE BY DIMENSION (0 OF 22 VERIFIED)

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

## 3. The COGS residual, re-measured before the table (`C5-B-04`) — corrected after self-challenge `CHC-01`

The *"COGS gap, elements 4 and 7"* carried on the COGS rows named one joint decision as its ground:
`JT-01`, *which concept owns valuation policy* — whose *"ultimate design choice (adopt
Category-as-owner…) → Boss / Architecture owner"*. **Boss took it on 2026-09-08:** `BD-ACC-03A`
(`Periodic | Perpetual`, authority = Product Category) and `BD-ACC-03B` (`Standard | Average | FIFO`,
authority = Product Category), plus the Product-level override boundary; the closure act: *"must not be
re-asked without material delta."*

> **What `BD-ACC-03A` settles, exactly: the policy *values* and their *owner*. Its three bullets contain
> no word about timing, date, event or movement.** The first freeze of this file (`C10-A1`) read the
> value *Perpetual* as *"recognition on the physical event date of the movement"* by construction.
> Internal self-challenge `CHC-01` falsified that reading at primary text: the definition comes from
> **`ND-10`** (`SA_CORR2_01` §5.1), a **SMEs Core** Nature-DNA determination that `SA_CORR2_12` records
> as *"none is Boss-approved"*; the current reference generation's own label reads **"Perpetual (at
> invoicing)"** (`C2-F-03`, `FACT VERIFIED`); and the COGS package assigns *"final event selection →
> Boss"* (`08_JT04` §5) with *"selecting among A/B/C/D/E is a Boss/Business decision in every case"*
> (`11_COGS_RECOGNITION_OPTIONS_ANALYSIS`). **`C10-A1` is withdrawn.** It was SMEs Core deciding an item
> the owning package reserved to Boss — the exact inversion the master prompt's challenge list names.

| COGS decision | State before | **State now** | Basis |
|---|---|---|---|
| `JT-01` valuation policy owner | `NOT DECIDABLE` (2026-09-03) | **RULED — Product Category** (owner and values). **Of the eight sub-facts `JT-01` gated (`CGS-U06/07/08/09/11/12/13/42`), the ruling answers the ownership fact; `CGS-U07`/`U08` (behaviour on a policy or category change mid-period) and the re-fetch items remain open COGS research items** — carried in the COGS unknown population, §3.1 | `BD-ACC-03A/03B`; `10_JT01` §4 |
| **`JT-04` recognition timing** | `NOT DECIDABLE` | **Boss election — carried, not new.** SMEs Core recommendation, attributed and not adopted: **`ND-10`** — *Perpetual* = recognition at the physical movement, *Periodic* = at period close, stated wherever the terms appear — because the reference's own meaning of the word moved between generations. Inputs Boss may take or waive: `SME-Q-03` (Business SME), `TH-NEW-01` (statutory `HOLD`), `CGS-U20`/`U31` re-fetch | `08_JT04` §4–5; `ND-10` |
| `JT-05` return cost basis (original vs current) | `NOT DECIDABLE` | **Boss policy election — carried.** SMEs Core recommendation: **original cost** (`XMC-C-A8` binds the reversal to the original identity, so the original amount is always recoverable; a current-cost reversal manufactures a margin no sale earned). `TH-NEW-02` `HOLD / EVIDENCE REQUIRED` | `09_JT05` §4–5 |
| `GAP-FS-07` inter-company path never traced | open | **traced at data level** (`SA_CORR5_07` §2.3): in the 44-company reference database the path is two single-company movements through one company-less transit location, 1,201 completed out-legs from one company paired with 1,201 completed in-legs across seven companies — the `XCR-01` shape. **The value leg (what each side records as cost) is untraced and is `JT-10`**, a COGS/joint decision | `SA_CORR5_07` §2.3 |
| `JT-10` inter-company transfer treatment | open | **joint Accounting × Inventory decision inside the COGS population — Boss/Business per that package's own routing**; carried | `05_CROSS_CONTEXT_REGISTER_R2` `XCR-01` |

### 3.1 The COGS unknown population is carried, not consumed

`18_UNKNOWN_BURNDOWN_REPORT` (COGS Targeted Resolution): **59 unknowns, 57 open, 0 closed in three
sessions.** This file re-measures the **three joint decisions** (`JT-01`, `-04`, `-05`) that sit *above* that
population against a Boss ruling that post-dates the report. It does **not** consume the **57 open
`CGS-U*` unknowns** themselves (`CHD-11`: the JTs are decisions the unknowns block, not members of the
59), which remain the **Account COGS track's** research population — a mix of documentation re-fetch (category 4),
Business-SME input, statutory `HOLD` and Boss election. **They are carried at `SA_CORR5_14` as a named
open population with its owner, not dissolved.** (`CHC-15`)

**Consequence for elements 4 and 7:** element 4 = **`N/A` by design with reason** (the producer never
decides recognition timing; `SA_CORR3_08` §2.3 graded it compliant) — **and the Accounting Core's own
recognition timing is the Boss election `JT-04`**; element 7 = **carried** (basis, amount, method
version per `BD-ACC-03B`). **The COGS rows therefore carry `B` (Boss election `JT-04`) on the accounting
convergence dimension, and rows 8/9 additionally `JT-05`.** `MTI-46`'s value half and `AAS-V-03` follow
(`SA_CORR5_09`).

---

## 4. The register — corrected after `CHC-01`…`-17`

| # | Scenario | SEM | IN | OUT | RT | IC | AC | TC | ID | AU | RP | PT | **Aggregate** | Exact gap / basis |
|---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|---|
| 1 | Stockable purchase receipt → handoff | C | C | C | C | C | **B**·S | C | C | C | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss election `JT-04` (recognition timing)`** | el.4 `N/A` by design, el.7 carried (§3). `C10-A2`: the reference's *swept suspense* goods-received bridge is **not inherited** — receipt accrual event and bill event are two events over one occurrence identity, item-matched by `XMC-C-A3` part 4. `S`: `TH-NEW-01` (does TAS 2 mandate a trigger event) `HOLD` |
| 2 | Vendor bill with receipt timing variation | C | C | C | C | C | **B**·S | C | C | C | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss election `JT-04``** | `XMC-C-A15`/`A16` (§5) state the SMEsPlus obligation for an event recognised after its physical period; **`A16` is a candidate rule whose interaction with Thai statutory period rules (VAT/WHT return periods, prior-period error vs current-period adjustment) is `S` — `HOLD / EVIDENCE REQUIRED`** (`CHC-05`) |
| 3 | Stockable sales delivery → cost handoff | C | C | C | C | C | **B**·S | C | C | C | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss election `JT-04``** | `BP-02` *not selectable* is a reference limitation; SMEsPlus's own timing is `JT-04` |
| 4 | Customer invoice, delivery timing variation | C | C | C | C | C | **B**·S | C | C | C | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss election `JT-04``** | `JT-04`'s **`CONFLICTING` flag** discharged (CORR2 `C2-F-03`); `JT-04` itself per §3 (`CHC-08`). Lifecycle interface `XMC-C-B1`…`B7` — note `B2` publishes cost-of-sales recognition at *posted*, which is one of the `JT-04` options, not its answer |
| 5 | Partial receipt | C | C | C | C | C | **B**·S | C | C | **B** | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss elections `JT-04`; over-receipt tolerance default (bundle with `B-1`/`B-2`)`** | `C10-A3` restated (`CHC-13`): the tolerance is a company-scoped configuration; **its default (refuse vs accept-and-event) is a control-default election of the same class as `XD1-P1`/`TV6-BOSS-01`** — SMEs Core recommends **refuse (`0`)**; a tolerated over-receipt is its own evented fact with a reason class |
| 6 | Partial delivery | C | C | C | C | C | **B**·S | C | C | C | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss election `JT-04``** | `H-05` answered by `XMC-C-B2`/`B4`: *draft* is published **not gate-grade** |
| 7 | Backorder | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | `R-17 NO CONSUMER`, *never-mode cancellation leaves no trail* → **`XMC-C-D5`** (§5). The Sales-side **producing design** is a Functional Design obligation (`C4-02-F-04`, `C4-D-01`), forbidden to this round |
| 8 | Purchase return | C | C | C | C | C | **B** | C | C | C | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss election `JT-05``** | reversal identity complete (`XMC-C-A8`); *return basis conflict PENDING — INVENTORY INTERNAL RESOLUTION FIRST* is `JT-05` seen from Inventory |
| 9 | Sales return | C | C | C | C | C | **B**·S | C | C | C | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss election `JT-05``** | `S` (`TH-NEW-02`) sits inside the `B` cell; reason class `RETURN_FROM_CUSTOMER` (`SA_CORR5_07` §3.3, `CHC-10`) |
| 10 | Cancellation before physical execution | C | C | C | C | C | C | C | C | **B** | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss election `XD1-P1``** | design resolved (`SA_CORR3_01`); the control's default severity is Boss-reserved (`B-1`) |
| 11 | Correction after physical execution | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | `XMC-C-A8`/`A9`; reversing movement (`INV-F-40`) |
| 12 | Inventory count / adjustment | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | `FDS_APPROVAL` + class 14 + `ND-04` + `L7-08`; `ND-05` + `SA06-F-04`; reason class mandatory |
| 13 | Scrap / damage / write-off | C | C | C | C | C | C·S | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | reason classes incl. `DESTRUCTION_FOR_TAX`; **salvage: `XMC-C-D7` (§5) originates the object's semantics** (`CHC-14`) — the *value* of recovered material is category policy (`BD-ACC-03B`) with the COGS residual; `S`: `TH-HOLD-02` |
| 14 | Internal warehouse transfer — no financial effect | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | `SA06-F-05` (neutrality **asserted**) + `TRANSFER_INTERNAL` class + boundary rule `DETERMINED` |
| 15 | Multi-company / tenant boundary | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | element 10: `XMC-C-D1`, `G1` 5/5, `G2` re-scoped, `G3` `AUD-C`, `G5` 10/10; `MTI-22` complete at register level. The cross-company *door* (`XCR-02`) is Boss-gated (`MTI-D-04`); `XCR-01` traced at data level, value = `JT-10`. `0 of 8` proofs, `0 of 60` negatives: runtime |
| 16 | Manufacturing RM → WIP → FG | C | C | C | C | C | **B** | C | C | C | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss residue `POH-D-01`, `-02`, `-06` (`B-6`)`** | **corrected (`CHC-07`)**: the SMEs Core design gaps `POH-G-01` (pool, denominator, capture), `POH-G-02` (receiver) and `POH-G-04` (variance) are **closed at specification level in `SA_CORR5_10A`**; the remaining `B` is the six-item Boss residue of `SA_CORR3_03` §9 — *none of which is "normal capacity or actual hours"*; `JT-04` also attaches |
| 17 | Manufacturing reversal / scrap / variance | C | C | C | C | C | **B** | C | C | C | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss residue `POH-D-01`, `-02`, `-06` (`B-6`)`** | variance owner, mechanism and destination specified (`SA_CORR5_10A` §5); normal/abnormal scrap classes; `POH-G-03` exclusion specified, build runtime |
| 18 | Stockable vs consumable vs service routing | C | C | **B** | C | C | C | C | C | C | Y | GATED | **`SA MATERIAL GAP — EXACT GAP: Boss elections `XMC-D-02` (contract scope) and `XMC-D-01`/`C2-D-02` (dropship valuation facts)`** | **`XMC-C-D6`** (§5) states the tie-break **with the supplier→customer case carved out** to `XMC-D-01`/`C2-D-02` (`CHC-02`); the service leg's element-contract scope is `XMC-D-02`; the election moved to `OUT` (`CHC-17`) |
| 19 | Period-end / cut-off | C | C | C | C | C | C·S | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | **`XMC-C-A15`** (§5) period object; lock binds the entry (`ND-07`); **`RC-03` of the Inventory V1 / R4 `RC-*` reconciliation family** (`07_INVENTORY_ACCOUNTING_CONTROL_IMPACT_V1` line 97; R4 `05_L4` line 122 — *not* the R1 `10` register's `RC-03`, a colliding identifier, `CHD-04`; `CHC-09`): reconciliation posture is *at the closing boundary* under `Periodic` and *continuous* under `Perpetual` by definition — each run states its posture; `S`: statutory register content, and `A16`'s statutory interaction, `HOLD` |
| 20 | Historical migration across fiscal years | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | **`XMC-C-A17`** (§5) provenance-reference semantics; `MTI-42`; `L10-01`…`-10` |
| 21 | AI migration mapping + deterministic reconciliation | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | element 14 as 20; per-company certification (`L10-07`); `A17`'s mapping-rule identity + version evidences the compliant act |
| 22 | Retry / idempotency / replay | C | C | C | C | C | C | C | C | C | Y | WRITABLE | **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | element 15 — `SA_CORR5_01`; `RT-E15-01`…`-09`. **`C-02` (is idempotency gate-blocking) is a Boss severity election that stays open** (`CHA-01`/`CHB-06`); it does not change any dimension cell — the specification is complete whichever way Boss rules the severity, which is why the row is not `B` |

### 4.1 Tally, re-derived from the rows

| Aggregate | Scenarios (enumerated) | n |
|---|---|---:|
| **`SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED`** | 7, 11, 12, 13, 14, 15, 19, 20, 21, 22 | **10** |
| **`SA-SPEC COMPLETE / PRE-TEST READY`** | — | **0** *(no implementation exists)* |
| **`SA MATERIAL GAP — EXACT GAP`** — every one a **Boss election**: six pre-date this round, one (the tolerance default) was originated by this round's own challenge and routed to Boss (`CHD-09`) | 1, 2, 3, 4, 5, 6 (`JT-04`) · 8, 9 (`JT-05`) · 10 (`XD1-P1`) · 5 also (tolerance default) · 16, 17 (`B-6`) · 18 (`XMC-D-02`, `XMC-D-01`) | **12** |
| **Total** | | **22** ✓ |

| Dimension cells (22 × 9 = 198) | `C` | `B` | `S` (inside a cell) | **`G`** |
|---|---:|---:|---:|---:|
| | **185** | **13** — AC on rows 1, 2, 3, 4, 5, 6, 8, 9, 16, 17 (10) · AU on rows 5, 10 (2) · OUT on row 18 (1) | **9** markers — rows 1, 2, 3, 4, 5, 6, 9 (inside `B`), 13, 19 (inside `C`) | **0** |

*(Re-derived cell by cell; `C` = 198 − 13 = 185. A first version of this row printed 184 / 14 / 8 beside
the correct derivation — `CHD-02`; the row now carries only the derived figures.)*

> ### `C5-10-F-01` — corrected
> **Material Phase SA gaps owned by SMEs Core / PMO / document owner across the 22: `0` — after
> `SA_CORR5_10A` closed the three overhead design gaps and `XMC-C-D7` the salvage object.** Twelve
> scenarios remain `SA MATERIAL GAP`, and **every one names a Boss election** — six that pre-date this
> round (`JT-04`, `JT-05`, `XD1-P1`, `B-6`, `XMC-D-02`/`XMC-D-01`) and one this round's challenge originated
> and routed to Boss (the over-receipt tolerance default, bundled with `B-1`/`B-2`).
> **The first freeze of this file reported 16 / 0 / 6; the honest figure after self-challenge is 10 / 0 /
> 12, and the difference is one item — `JT-04` — that SMEs Core had decided in Boss's place.** `0 of 22`
> are verified; all 22 require an implementation and an executed test. **What this file claims is that
> no further Phase SA round can move a dimension of any of the 22 by SMEs Core work — the remaining
> movement is Boss's, the COGS track's research population (§3.1), the Thai statutory track's evidence,
> and the build.**

---

## 5. Contract clauses originated in this file (Phase SA namespace, business-semantic only)

| ID | Clause | Rationale (independent, not inherited) | Challenge target |
|---|---|---|---|
| **`XMC-C-A15`** | **An accounting period is a first-class object** of the company: identity, calendar position, state (`OPEN` → `CLOSING` → `CLOSED`); every accounting event carries the period it is recognised in; a period lock binds the **entry** (`ND-07`), never the path; closing and re-opening are evented, approved acts | `SA10-F-05`; `AR-20` *"no accounting-period object (`G-11`)"*; locked-period entries silently re-dated in the evidenced estate | conceptual vs data-model design — both inside the closure act's grant |
| **`XMC-C-A16`** | **Prior-period attribution — candidate rule, statutory interaction `HOLD`**: an event whose physical date falls in a `CLOSED` period is recognised in the earliest `OPEN` period with an explicit attribution reference to the original occurrence and the closed period; the original is never re-dated (`A9`). **Whether Thai statutory period rules (VAT/WHT return periods; prior-period error vs current-period adjustment) permit this for a given fact class is `HOLD / EVIDENCE REQUIRED`** (`CHC-05`) | scenario 2; `A9` | statutory |
| **`XMC-C-A17`** | **Provenance reference (element 14)** — semantics only: batch identity · source system identity · source record reference · mapping rule identity **and version** · load-act attempt identity (`A14`) · evidence reference; beside the identity, never inside the basis (`A7`); mandatory on migrated/replayed/recovered facts, `N/A + reason` otherwise | `GAP-FS-08`; `MTI-42`; `L10-09`/`-10`; `A7` | Inventory-owned rank-3 artefact; Phase SA states the cross-module element's semantics only |
| **`XMC-C-D5`** | **A remainder of a partially fulfilled demand is a business fact** with an owner and a named consumer; cancelling it is an evented act carrying a reason class | scenario 7; `R-17` | — |
| **`XMC-C-D6`** | **Routing tie-break**: (1) does the line move stock the company owns? → Inventory routing and a movement fact; (2) if yes, is the category **valued** under `BD-ACC-03A`? → valuation carriage or explicit `N/A` with reason; (3) if no movement → Part C assertion event. Precedence physical > policy > commercial; resolution inputs retained (`ND-01`). **Carve-out (`CHC-02`): a supplier→customer movement with no internal end is *not* resolved by this clause; it is `XMC-D-01`/`C2-D-02`, Boss-reserved** | scenario 18; `XMC-C-C1`; the *where* vs *whether* boundary rule | — |
| **`XMC-C-D7`** | **Salvage** (`CHC-14`): recovered material from a scrap or write-down is an **inbound movement fact of a distinct product** (the recovered material) with recognition role *salvage recovery*, **linked to the scrap event identity** (`A8`-style discoverability), carrying its reason class; its value is category policy (`BD-ACC-03B`) or explicit `N/A + reason` while the COGS residual stands; owner Inventory (stock truth) with Accounting recognising the event | R1 row 23 *"salvage has no object and must be originated"*; `R4-F-03` | — |
| **`C10-A2`** | receipt accrual and bill are two events over one occurrence identity (row 1) | `XMC-C-A3`/`A4` | — |
| **`C10-A3` (restated)** | over-receipt tolerance is company-scoped configuration; **its default is a Boss control-default election**, SMEs Core recommends refuse | `CHC-13` | — |
| **`C10-A1`** | **WITHDRAWN** (`CHC-01`) | — | — |

**Six clauses originated here and reviewed by nobody outside this session** at the time of writing;
attacked at `SA_CORR5_11`.

---

## 6. What changed against CORR4, exactly — corrected

| | CORR4 | **CORR5 (first freeze)** | **CORR5 (after self-challenge)** |
|---|---|---|---|
| Aggregate | 22 `SA MATERIAL GAP` (one overloaded status) | 16 / 0 / 6 | **10 / 0 / 12**, by dimension |
| Element 15 dimension | blocks all 22 | `C` on 22 | `C` on 22 (`RP` = Y) |
| Context/authorization dimension | `SA CONTRACT COMPLETE — RUNTIME TEST REQUIRED` on 22 | unchanged, `G1`/`G3`/`G5` closed | unchanged |
| "COGS gap el.4/7" | carried on 12 rows | dissolved | **`JT-04` Boss election on 8 rows (1–6, 16, 17); `JT-05` on 2; statutory `S` on 9 cells; `GAP-FS-07` traced at data level; 54 COGS unknowns carried** |
| "design mechanism does not exist" on 8 rows (2, 7, 12, 13, 14, 16, 17, 19) | carried | — | **2 → `A15`/`A16`; 7 → `D5`; 19 → `A15`; 12, 13, 14 → existing specification + `D7`; 16, 17 → `SA_CORR5_10A` (design) + `B-6` (Boss)** (`CHC-16`) |
| Boss elections in the 22 | 5 (8, 9, 10, 18, 22) | 4 | **8 distinct**: `JT-04`, `JT-05`, `XD1-P1`, `B-6`, `XMC-D-02`/`XMC-D-01` (pre-existing), the **tolerance default (originated by this round's challenge, routed to Boss)**, on 12 scenarios, plus **`C-02`** (severity, scenario 22, open but cell-neutral) — `UAE-29` ruled by `BD-ACC-01` (`CHD-09`) |
| `0 of 22 VERIFIED` | unchanged | unchanged | **unchanged** |

## 7. Residual

1. **The `C` cells are claims about sufficiency for writing a test, not correctness.** Eighteen of the
   `C` rows rest on CORR2/CORR3 reconciliations reviewed only by same-model challengers.
2. **`JT-04` is the pivot of this file and it is Boss's.** The first freeze decided it at SMEs Core
   (`C10-A1`) and self-challenge `CHC-01` reversed that within the same round; the residual record of
   that reversal is kept in §3 so that a reader can see how close the package came to deciding a
   Boss item and reporting a zero on the strength of it.
3. **Scenario 15's `C` on the routing dimension** depends on distinguishing the *wall* from the *door*;
   a reader who holds that an isolation scenario is incomplete while any cross-company relationship is
   unruled would grade it `B` (`MTI-D-04`). Either way the owner is Boss, not SMEs Core.

## 8. Checkpoint

> ## `CP-SA-C5-100 — 22-SCENARIO SA-SPEC CLOSURE BY DIMENSION (0 OF 22 VERIFIED)`
> **22 × 9 dimensions: 185 `C` · 13 `B` · 9 `S` markers · 0 `G` · aggregate 10 / 0 / 12 · every
> remaining gap a pre-existing Boss election · 6 contract clauses + 2 adjudications originated, 1
> withdrawn · `0 of 22 VERIFIED` unchanged · 1 finding (`C5-10-F-01`) · corrected by `CHC-01`…`-17`.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
