# SA15 — END-TO-END SCENARIO REGISTER — CORR5 CONTROLLED VERSION

> **CONTROLLED VERSION NOTICE.** This is the CORR5-corrected controlled version of
> `PHASE_SA_CROSS_MODULE_ASSURANCE_2026_09_08/SA15_END_TO_END_SCENARIO_REGISTER.md`. **The historical
> file is not overwritten**; it remains readable as published so that `C4-07-F-03` stays auditable.
> Supersession rule: **this version governs** where the two differ. Corrections are marked `[CORR5]`
> with their basis. Authority: `SA_CORR5_06`, master prompt §9.

Status: **HOLD** — 15 mandated scenarios plus 3 added; **3** traversable end-to-end with no named break
(E2E-02, E2E-11, E2E-12), **13** with a named break, **2** not traversable (E2E-04, E2E-07).
`[CORR5]` *E2E-15 regraded from `TRAVERSABLE` to `TRAVERSABLE WITH NAMED BREAK` — basis `SA_CORR5_06`
§2: its cited ground (`SA09` "idempotency established") was superseded by `SA_CORR2_09` §3, which grades
idempotency `NOT ESTABLISHED`; element 15 is `specified, not built, not verified` (`SA_CORR5_01`).*
Governing law: master prompt §12.

---

## 1. Traversability classification

| Class | Meaning |
|---|---|
| `TRAVERSABLE` | Every hop has an evidenced producer, consumer and compatible interface |
| `TRAVERSABLE WITH NAMED BREAK` | The spine is evidenced; one or more named hops carry an open item |
| `NOT TRAVERSABLE` | At least one hop cannot be routed at all on current evidence |

**`[CORR5]` Mandatory reading rule (master prompt §9):** `TRAVERSABLE` and `SA CONTRACT COMPLETE` mean
*a test case can be written*. **Neither means built, proven, verified or compliant.** No scenario in
this register is verified; `0 of 22` joint cross-proof scenarios are `VERIFIED`.

---

## 2. Mandated scenarios

| ID | Scenario | Class | Breaks / blockers |
|---|---|---|---|
| E2E-01 | Customer → Sales → Stock → Delivery → AR → Payment → Bank → Accounting | `TRAVERSABLE WITH NAMED BREAK` | commercial entry (SA-D21) — `[CORR5]` price and credit determination executed at `SA_CORR3_13`, residual Boss elections `TV6-BOSS-01`/`-02`; cancellation gate `XD-01` — `[CORR5]` design resolved at `SA_CORR3_01`, residual Boss election `XD1-P1` |
| E2E-02 | Purchase demand → Purchase → Receipt → AP → Payment → Bank → Accounting | `TRAVERSABLE` | approval internal logic open (A2) but the flow routes |
| E2E-03 | Sales → Manufacture → RM → Production → FG → Delivery → AR → Accounting | `TRAVERSABLE WITH NAMED BREAK` | BOM/routing semantics thin; fixed-overhead injection path (R-22) — `[CORR5]` chain studied at `SA_CORR3_03`, residual Boss restatement `B-6` (`BLK-07`) |
| E2E-04 | Sales → Manufacture → RM shortage → Purchase → Receipt → Production → Delivery → Accounting | **`NOT TRAVERSABLE`** | shortage→purchase trigger undetermined (BN-04, TVDR-01); `C2-D-01` |
| E2E-05 | Sales → Dropship → Purchase → Vendor-to-customer → AR/AP → Accounting | `TRAVERSABLE WITH NAMED BREAK` `[CORR5]` | *was `NOT TRAVERSABLE`* — `SA_CORR2_01` §4.3: the inventory-event question is answered; the named breaks are `H-02` (movement→valuation hop `SEMANTICALLY INCOMPATIBLE — MEASURED`) and `H-03` (cost→revenue link `NO IDENTITY`); residual Boss election `XMC-D-01`; control bypass `SA03-F-02` |
| E2E-06 | Sales → MTO/Buy → Purchase → Receipt → Delivery → Accounting | `TRAVERSABLE WITH NAMED BREAK` | order→purchase linkage and its reservation semantics unevidenced (BN-06) |
| E2E-07 | Sales → Kit → Component inventory → Delivery → Accounting | **`NOT TRAVERSABLE`** | component resolution point and costing level — `[CORR5]` costing level **resolved at `SA_CORR3_02`** (`C2-D-03`: 0 Boss decisions); the **resolution point** (BN-07, IR-12) remains the unrouted hop |
| E2E-08 | Service → Delivery/completion evidence → AR → Payment → Accounting | `TRAVERSABLE WITH NAMED BREAK` `[CORR5]` | *was `NOT TRAVERSABLE`* — `SA_CORR2_03` §3.1: the trigger is an assertion with no independent event record; `XMC-C-C1`…`C6` specify the assertion event; the break is the absence of an independent operational event |
| E2E-09 | Purchase → Asset capitalization → Depreciation → Accounting | `TRAVERSABLE WITH NAMED BREAK` | derecognition defect (AR-17); Equipment side thin |
| E2E-10 | Expense → Approval → Payable/Payment → Accounting | `TRAVERSABLE WITH NAMED BREAK` | P05 terminal HOLD (AR-18) |
| E2E-11 | Sales return → Inventory return → Credit/reversal → Accounting | `TRAVERSABLE` | return is the most fully evidenced area in the corpus; `[CORR5]` cost basis of the reversal is Boss election `JT-05` — a break on the **accounting value**, not on the route |
| E2E-12 | Purchase return → Inventory return → Debit/reversal → Accounting | `TRAVERSABLE` | structurally identical; `[CORR5]` return basis conflict `PENDING — INVENTORY INTERNAL RESOLUTION FIRST` |
| E2E-13 | Manufacturing scrap / by-product / variance → Inventory → Accounting | `TRAVERSABLE WITH NAMED BREAK` | by-product valuation open (IR-08, AR-12); `[CORR5]` normal/abnormal scrap classes specified at `SA_CORR5_07` §3.3 |
| E2E-14 | Month close → Inventory valuation → AR/AP → Bank → Tax → GL → Financial reporting | `TRAVERSABLE WITH NAMED BREAK` | AR-20 close, AR-21 analytic, AR-22 tax all `PARTIAL` against recorded Phase S terminal states |
| **E2E-15** | **Correction / reversal / retry / duplicate event** | **`TRAVERSABLE WITH NAMED BREAK`** `[CORR5]` | *was `TRAVERSABLE` — "strongest area: idempotency and ordering-independence established (`SA09`)"*. **Corrected:** `SA09` was superseded by `SA_CORR2_09` §3 (idempotency `NOT ESTABLISHED`, *"recorded absent in four Accounting packages"*); the joint cross-proof grades scenario 22 `HOLD`; the estate's only carrier is table-global and populated on 0 of 13,814 rows. **The named break is element 15 — `specified` (`SA_CORR5_01`), `not built, not verified`.** Reversal semantics are established (`XMC-C-A8`/`A9`); **retry and duplicate detection are specified only** |

## 3. Scenarios added by this register

| ID | Scenario | Why added | Class |
|---|---|---|---|
| **E2E-16** | Quality inspection → hold/release/reject → Inventory availability → cost recognition timing | Boss ruled the Quality boundary (`4c469f8e`) | `TRAVERSABLE WITH NAMED BREAK` `[CORR5]` — *was `NOT TRAVERSABLE`*; `SA_CORR2_03` §3.3: quality holds are a location state; the object is absent, the route is evidenced |
| **E2E-17** | Manufacturing work order → equipment breakdown → maintenance order → completion → work order resumes | Route stated verbatim in Boss decision `a11c9e7b` §3 | `TRAVERSABLE WITH NAMED BREAK` `[CORR5]` — *was `NOT TRAVERSABLE`*; `SA_CORR3_04`: 9 of 12 maintenance routes close at SMEs Core; residual `BLK-08` (Boss `B-6`) |
| **E2E-18** | Project → operational progress → source facts → analytic dimension → derived project financial view | Boss ruled the Project ↔ Analytic boundary (`fa57d10f`) | `TRAVERSABLE WITH NAMED BREAK` `[CORR5]` — *was `NOT TRAVERSABLE`*; `SA_CORR2_03` §3.2: **traversed and found to duplicate financial truth three ways** — a named, measured break |

## 4. Traversability summary — counted by enumerating identifiers

| Class | Scenarios (enumerated) | Count |
|---|---|---|
| `TRAVERSABLE` | E2E-02, E2E-11, E2E-12 | **3** |
| `TRAVERSABLE WITH NAMED BREAK` | E2E-01, E2E-03, E2E-05, E2E-06, E2E-08, E2E-09, E2E-10, E2E-13, E2E-14, E2E-15, E2E-16, E2E-17, E2E-18 | **13** |
| `NOT TRAVERSABLE` | E2E-04, E2E-07 | **2** |
| **Total** | 15 mandated + 3 added | **18** |

Check: **3 + 13 + 2 = 18**, and every identifier E2E-01…E2E-18 appears exactly once above.
`[CORR5]` *The historical file's check line read "4 + 7 + 7 = 18" over a table enumerating 13
identifiers with printed counts 4 / 7 / 2 (`JCP3-F-11`). This table enumerates all 18.*

## 5. SA15-F-01 — corrected

`[CORR5]` **The three fully traversable scenarios are all receipts or returns.** E2E-02 purchase-to-pay,
E2E-11 sales return and E2E-12 purchase return are the only end-to-end flows that traverse without a
named break. Not one is a *forward sale to a customer*; E2E-01 still carries named breaks, now reduced
to Boss elections. **The historical sentence counted E2E-15 among them; it no longer does, and the
finding is stronger for it: SMEsPlus can currently prove end-to-end that it can receive and return
goods. It cannot yet prove that it can sell something, and it cannot yet prove that it can safely retry.**

## 6. SA15-F-02 — unchanged, with CORR2's qualifications carried

All five governing decisions carry `APPROVED DIRECTION / DETAIL DESIGN PENDING`; the three added routes
are evidenced (`SA_CORR2_03` §3) and E2E-18 has been traversed and found defective — a better Pre-Test
input than an untraversed route.

## 7. Handoff to Pre-Test Matrix

This register does **not** execute the Pre-Test Matrix (master prompt §21). Scenario priority is carried
to `SA17` (CORR5 controlled version), with `[CORR5]` **E2E-15 raised from priority 18 to a dependency
gate**: nothing may be read as testing retry, duplicate detection or any cross-module join until
element 15 is built (`SA_CORR4_07` §5.1 prohibitions 2 and 3).

---

`SA15 — HOLD`. Three of eighteen end-to-end scenarios traverse without a named break; two cannot be
traversed. **Zero are verified.**

Boss remains the sole Final Approver.
