# SA15 — END-TO-END SCENARIO REGISTER — FINAL CONTROLLED VERSION (v2)

> **CONTROLLED VERSION NOTICE.** This supersedes `SA15_END_TO_END_SCENARIO_REGISTER_CORR5_CONTROLLED.md`
> (CORR5 package, commit `379fd073`), which superseded the historical
> `PHASE_SA_CROSS_MODULE_ASSURANCE_2026_09_08/SA15_END_TO_END_SCENARIO_REGISTER.md`. **Neither earlier
> file is overwritten**; both remain readable so the correction chain stays auditable. This version
> governs. New corrections are marked `[FG]`; corrections inherited from CORR5 keep their `[CORR5]`
> marks. Authority: `SA_FINAL_01` §5 (`FG-F-01`), master prompt §3 and §6.

Status: **HOLD** — 15 mandated scenarios plus 3 added; **2** traversable end-to-end with no named break
(E2E-02, E2E-07), **15** with a named break, **1** not traversable (E2E-04).
`[FG]` *One re-grade is applied and one attempted re-grade is **withdrawn by this session's own challenge**:
`E2E-07` → `TRAVERSABLE` (basis `SA_CORR3_02` §12, a consequences table stated "for their owners" and only
partly applied by CORR5); `E2E-04` **remains `NOT TRAVERSABLE`** — a first draft of this file re-graded it
and suppressed the second clause of its own source sentence (`CHF-03`). See §2.*

---

## 1. Traversability classification

| Class | Meaning |
|---|---|
| `TRAVERSABLE` | Every hop has an evidenced producer, consumer and compatible interface |
| `TRAVERSABLE WITH NAMED BREAK` | The spine is evidenced; one or more named hops carry an open item |
| `NOT TRAVERSABLE` | At least one hop cannot be routed at all on current evidence |

**Mandatory reading rule** (carried from CORR5, unchanged): `TRAVERSABLE` means *a test case can be
written*. **It does not mean built, proven, verified or compliant.** `0 of 22` joint cross-proof
scenarios are `VERIFIED`, and no scenario here is verified.

---

## 2. The two corrections this version applies

| Scenario | Was (CORR5 controlled) | **Now** | Basis, at primary text |
|---|---|---|---|
| **`E2E-07`** Kit / bundle | `NOT TRAVERSABLE` — CORR5's controlled row reads *"costing level **resolved at `SA_CORR3_02`** (`C2-D-03`: 0 Boss decisions); the **resolution point** (`BN-07`, `IR-12`) remains the unrouted hop"*. **CORR5 read `SA_CORR3_02` and applied half of it, retaining the resolution-point blocker with a stated reason** (`CHF-05`) | **`TRAVERSABLE`** | **This is a reversal of a reasoned prior position, not the application of an overlooked one.** `SA_CORR3_02` §12 proposes exactly this — **`SA15` `E2E-07`: `NOT TRAVERSABLE` → `TRAVERSABLE` — "both stated blockers now closed"**. Blocker 1, costing level: resolved by `SA_CORR3_02` (`C2-D-03` → **`A`, resolved, 0 Boss decisions**; *"the components carry the cost; the parent is not a valued object"*). Blocker 2, resolution point: `SA_CORR2_05` re-grades **`IR-12` → `RECONCILED — RESOLUTION POINT DETERMINED`**. `SA05` `BN-07` → **`DETERMINED`**; `SA_CORR2_02` §3.4 `BN-07` residual → **`RESOLVED — NO BOSS DECISION REQUIRED`** |
| **`E2E-04`** Sales → Manufacture → RM shortage → Purchase → Production → Delivery | `NOT TRAVERSABLE` — *"shortage→purchase trigger undetermined (`BN-04`, `TVDR-01`)"* | **`NOT TRAVERSABLE` — RETAINED, on a corrected ground** | **A first draft of this file re-graded this row and was falsified by its own source** (`CHF-03`). `SA_CORR2_02` §3.1 (**not** `SA_CORR2_03`, `CHF-04`) re-grades `BN-04` → **`PARTIAL`** and `XMC-F-03` shows the routing *template* exists (*"make-or-buy on demand"*) — **but the same source sentence continues:** *"the target manufacturing state machine's shortage state exits **only on reservation completing, never on procurement being raised.** **A shortage can therefore be entered and never left by supply.**"* §5 of that register restates it: *"soft fulfiller binding, **and a shortage state with no supply exit**"*. **On this register's own definition — *at least one hop cannot be routed at all on current evidence* — the shortage→supply hop is unrouted.** The break is `C2-D-01` **and** the missing supply exit, which CORR2 raised together in one cell as one decision. **`TVDR-01` is not a live blocker: CORR2 closed it** |

> **Why this was missed for three rounds.** `SA_CORR3_02` §12 is headed *"Consequences carried to other
> registers — **stated for their owners, not applied here**"*. CORR4 did not sweep it; CORR5 swept the
> **CORR2** consequences into `SA15`/`SA17` and not the **CORR3** ones. This is the programme's recorded
> *a revision log is not a correction* defect at its fourth occurrence, and its first occurrence inside
> the artefact that hands work to Pre-Test.

---

## 3. Mandated scenarios

| ID | Scenario | Class | Breaks / blockers |
|---|---|---|---|
| E2E-01 | Customer → Sales → Stock → Delivery → AR → Payment → Bank → Accounting | `WITH NAMED BREAK` | price/credit → Boss `F2` (`TV6-BOSS-01`) and `TV6-BOSS-02`; cancellation gate → Boss `F2` (`XD1-P1`) |
| E2E-02 | Purchase demand → Purchase → Receipt → AP → Payment → Bank → Accounting | **`TRAVERSABLE`** | approval internal logic open (A2); the flow routes |
| E2E-03 | Sales → Manufacture → RM → Production → FG → Delivery → AR → Accounting | `WITH NAMED BREAK` | BOM/routing semantics thin; overhead → Boss `F5` |
| **E2E-04** | Sales → Manufacture → RM shortage → Purchase → Receipt → Production → Delivery | **`NOT TRAVERSABLE`** | **Retained.** The routing *template* is determined (`XMC-F-03`, *make-or-buy on demand*) and `BN-04` is `PARTIAL` (`SA_CORR2_02` §3.1) — **but the same source sentence continues that the target manufacturing state machine's shortage state exits *"only on reservation completing, never on procurement being raised. A shortage can therefore be entered and never left by supply."*** The shortage→supply hop is unrouted. **Two-clause break: `C2-D-01` (soft-vs-hard binding) and the missing procurement exit — CORR2 raised both in one cell as one decision (`F4`).** `TVDR-01` is **not** a live blocker; CORR2 closed it. *A first draft of this file re-graded this row to `WITH NAMED BREAK` and suppressed the second clause; withdrawn by `CHF-03`* |
| E2E-05 | Sales → Dropship → Purchase → Vendor-to-customer → AR/AP → Accounting | `WITH NAMED BREAK` `[CORR5]` | `H-02` movement→valuation hop `SEMANTICALLY INCOMPATIBLE — MEASURED`; `H-03` cost→revenue `NO IDENTITY`; Boss `F3` |
| E2E-06 | Sales → MTO/Buy → Purchase → Receipt → Delivery → Accounting | `WITH NAMED BREAK` | order→purchase linkage and reservation semantics (`BN-06`) |
| **E2E-07** | Sales → Kit → Component inventory → Delivery → Accounting | **`TRAVERSABLE`** `[FG]` | *was `NOT TRAVERSABLE`.* **Both stated blockers closed** — components carry the cost, the parent is not a valued object; resolution point `RECONCILED`. **No Boss decision required** |
| E2E-08 | Service → Delivery/completion evidence → AR → Payment → Accounting | `WITH NAMED BREAK` `[CORR5]` | the trigger is a human assertion with no independent operational event; `XMC-C-C1`…`C6` specify the assertion event |
| E2E-09 | Purchase → Asset capitalization → Depreciation → Accounting | `WITH NAMED BREAK` | derecognition defect (`AR-17`); Equipment side thin |
| E2E-10 | Expense → Approval → Payable/Payment → Accounting | `WITH NAMED BREAK` | P05 terminal HOLD (`AR-18`) |
| E2E-11 | Sales return → Inventory return → Credit/reversal → Accounting | `WITH NAMED BREAK` `[CORR5]` | route most fully evidenced in the corpus; **break: reversal cost basis → Boss `F1` (`JT-05`)** |
| E2E-12 | Purchase return → Inventory return → Debit/reversal → Accounting | `WITH NAMED BREAK` `[CORR5]` | structurally identical; return basis `PENDING — INVENTORY INTERNAL RESOLUTION FIRST` |
| E2E-13 | Manufacturing scrap / by-product / variance → Inventory → Accounting | `WITH NAMED BREAK` | by-product valuation open (`IR-08`, `AR-12`); scrap reason classes specified (`SA_CORR5_07` §3.3); salvage object specified (`XMC-C-D7`) |
| E2E-14 | Month close → Inventory valuation → AR/AP → Bank → Tax → GL → reporting | `WITH NAMED BREAK` | `AR-20`, `AR-21`, `AR-22` `PARTIAL`; period object specified (`XMC-C-A15`) |
| E2E-15 | Correction / reversal / retry / duplicate event | `WITH NAMED BREAK` `[CORR5]` | **element 15 — `specified, not built, not verified`**; reversal semantics established (`XMC-C-A8`/`A9`); retry and duplicate detection specified only |
| E2E-16 | Quality inspection → hold/release/reject → availability → cost timing | `WITH NAMED BREAK` `[CORR5]` | quality holds are a location state; the first-class Quality **object** is absent, the route is evidenced |
| E2E-17 | Work order → equipment breakdown → maintenance → resume | `WITH NAMED BREAK` `[CORR5]` | 9 of 12 maintenance routes close at SMEs Core; residual `BLK-08` → Boss `F5` |
| E2E-18 | Project → source facts → analytic dimension → derived view | `WITH NAMED BREAK` `[CORR5]` | **traversed and found to duplicate financial truth three ways** |

## 4. Traversability summary — counted by enumerating identifiers

| Class | Scenarios (enumerated) | Count |
|---|---|---|
| `TRAVERSABLE` | E2E-02, E2E-07 | **2** |
| `TRAVERSABLE WITH NAMED BREAK` | E2E-01, E2E-03, E2E-05, E2E-06, E2E-08, E2E-09, E2E-10, E2E-11, E2E-12, E2E-13, E2E-14, E2E-15, E2E-16, E2E-17, E2E-18 | **15** |
| `NOT TRAVERSABLE` | E2E-04 | **1** |
| **Total** | 15 mandated + 3 added | **18** |

Check: **2 + 15 + 1 = 18**, and every identifier `E2E-01`…`E2E-18` appears exactly once above.

**Instrument note.** Counting `NOT TRAVERSABLE` by whole-file grep returns false positives from the
*"was `NOT TRAVERSABLE`"* annotations; the tally above is derived from the **class column only**, on a
second command shape. The counting-command-validation rule held again.

## 5. `SA15-F-01` — corrected again, and the finding is now sharper

`[FG]` **Two scenarios traverse without a named break: `E2E-02` (purchase-to-pay) and `E2E-07`
(kit/bundle). Neither is a forward sale.** Of the fifteen named breaks, **eight are a Boss election
rather than a specification gap** — `E2E-01`, `-03`, `-05`, `-11`, `-12`, `-13`, `-17`, and `-15` for its
severity — enumerated, not asserted (`CHF-12`). **`E2E-14`'s break is three `PARTIAL` items and statutory
register content, not a Boss election** (`CHF-10`). And `E2E-04` remains untraversable on a structural
ground its own source states.

> **The honest movement is smaller than a first draft of this file claimed and it is still real: the
> register goes from two untraversable scenarios to one, and the one that moved (`E2E-07`) moved all the
> way to `TRAVERSABLE` with no Boss decision attached.**

## 6. `SA15-F-02` — unchanged

All five governing decisions carry `APPROVED DIRECTION / DETAIL DESIGN PENDING`; the three added routes
are evidenced, and `E2E-18` has been traversed and found defective.

## 7. Handoff to Pre-Test Matrix

Priority is carried to `SA17` (final controlled v2). `[CORR5]` `E2E-15` remains a **dependency gate**:
nothing may be read as testing retry, duplicate detection or any cross-module join until element 15 is
built.

---

`SA15 — HOLD`. Two of eighteen end-to-end scenarios traverse without a named break; **one remains
untraversable** (`E2E-04`, Boss-gated on `C2-D-01`). **Zero are verified.**

Boss remains the sole Final Approver.
