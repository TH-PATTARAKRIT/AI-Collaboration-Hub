# AI10 — P09_PEER_HANDOFF_MATRIX

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Layer:** 1 — clean-room.

Explicit evidence handoffs. **P09 hands over findings; it does not adjudicate another process's determination, and it does not settle `HOLD-AS-01` or `DIS-09`.**

---

## 1. → P04 — ACQUIRE-TO-RETIRE (asset depreciation)

| # | Handed over | Class | What P04 needs to decide |
|---|---|---|---|
| H04-1 | the zeroing theorem and its unconditional corollary (`AI02` §3) | FACT VERIFIED | whether the asset module's both-legs assignment is the intended asset-side behaviour, and what the asset-side requirement should be |
| H04-2 | the two-row structure with one balance-sheet leg and one profit-and-loss leg, and that **both** receive the allocation under an explicit guard whose comment addresses only the conditionality, not the symmetry | FACT VERIFIED | — |
| H04-3 | the surfaces disagree: the analytic account shows a **zero** balance while budget consumption shows the **full** cost, because the budget query filters to income and expense general accounts | FACT VERIFIED | whether asset depreciation is expected to appear in cost-centre reporting at all |
| H04-4 | the deferred-expense and deferred-revenue variants share the shape | shape FACT VERIFIED | per-variant confirmation |
| H04-5 | **P09 confirms P04's original finding in full and adds the algebra, the unconditionality, and the surface divergence** | — | — |

**P09 does not hand P04 a verdict on the prior Asset package's costing-veto premise.** That is `HOLD-AS-01` / `DIS-09`, preserved for P11.

## 2. → P03 — MANUFACTURE-TO-COST (WIP, equipment, production cost)

| # | Handed over | Class | What P03 needs to decide |
|---|---|---|---|
| H03-1 | **the masking interaction** (`AI11` §3): where a work-centre hourly rate recovers machine ownership cost, the cost centre may show approximately the right total while the depreciation attribution contributes zero and the machine-hour attribution silently carries it | **SUPPORTED INTERPRETATION**; firing is a costing-policy fact, **UNRESOLVED — EVIDENCE REQUIRED** | whether SMEsPlus work-centre rates are intended to recover depreciation, and if so how double attribution is prevented |
| H03-2 | one work-order duration change produces two management records at two rates, aggregated by a profitability section that does not distinguish them | mechanism FACT VERIFIED, firing configuration-dependent | — |
| H03-3 | the work centre is itself an allocation carrier — master data holding a distribution — and its scope is **undetermined** (`HOLD-SC-01`, `PD-01`) | UNRESOLVED — SCOPE EVIDENCE REQUIRED | the work-centre scope determination P09 cannot make |
| H03-4 | work-in-progress has two unreconciled representations, one of which spawns no management record at all | FACT VERIFIED / class B for "not reconciled" | — |

## 3. → P08 — RECORD-TO-REPORT (journal entry and journal item semantics)

| # | Handed over | Class | What P08 needs to decide |
|---|---|---|---|
| H08-1 | the allocation carrier is at **row** granularity while the attribution's subject is the **event** — `AI-S-01`, the generalisation of `MA-11` | FACT VERIFIED as a structural statement | whether SMEsPlus's accounting event carries attribution at event level |
| H08-2 | there is **no account-type test and no row-type test** on the management-record creation path; eligibility is purely "was this row given an allocation" | FACT VERIFIED | the eligibility rule SMEsPlus adopts |
| H08-3 | the obligation check is gated twice (execution context, then row type) and gates only the complaint, never the creation | FACT VERIFIED (row-type gate); call-site enumeration class **B from P09's position** | — |
| H08-4 | the accounting-event identity that P09 needs and the reference pattern lacks — `DEP-P09-01`, P09's standing blocking dependency and the ground for `AAS+-VETO-01` | UNRESOLVED — blocking | **this is the dependency that most constrains P09** |

## 4. → P10 — TIME-BASED RECOGNITION

| # | Handed over | Class | What P10 needs to decide |
|---|---|---|---|
| H10-1 | deferred expense and deferred revenue are produced by the **same** two-row mechanism as depreciation, so the zeroing corollary applies to them by the same arithmetic | shape FACT VERIFIED; per-variant confirmation in `AI07` | whether recognition schedules are expected to attribute to cost centres |
| H10-2 | the cut-off and accrual wizard propagates an allocation to generated rows, in one branch through a recomputed proportional map | FACT VERIFIED (base package) | whether that propagation is symmetric — **P09 flags this as the highest-priority item P10 should re-test with the algebra in hand** |

## 5. → P11 — CORE ACCOUNTING RECONCILIATION

| # | Handed over | Class |
|---|---|---|
| H11-1 | the whole `AI` continuation: algebra, eligibility, trace, sweep, surfaces, scope, attack | as classified per document |
| H11-2 | **`HOLD-AS-01` and `DIS-09` — preserved, unsettled, and explicitly not adjudicated by P09.** P04's finding contradicts a premise underpinning a standing costing veto held by a prior Asset package. Two parallel evidence tracks disagree; that reconciliation is Boss-level | **HOLD — CROSS-PROCESS RECONCILIATION REQUIRED** |
| H11-3 | `AI-R-01`: the model must declare whether the analytic ledger is a cost-attribution ledger or a balanced analytic subledger. **The reference pattern is both and neither** | DESIGN DECISION REQUIRED AT FINAL GATE |
| H11-4 | `AI-S-01`: a control must match the fact it governs in scope **and granularity** | FACT VERIFIED as a structural statement |
| H11-5 | the masking interaction (`H03-1`) — because it means a plausible cost-centre total is **not** evidence of correct attribution | SUPPORTED INTERPRETATION |

## 6. WHAT P09 EXPLICITLY DOES NOT HAND OVER

- No verdict on another process's model.
- No settlement of `HOLD-AS-01` or `DIS-09`.
- No statutory claim.
- No upgrade of any class B, C or D item belonging to another process. P04's call-site enumeration and its project-to-asset counting finding remain **class B from P09's position** and are not restated as P09 class A.

## 7. CHECKPOINT

**CP-AI10 — CROSS-PROCESS HANDOFF COMPLETED.** Five processes, 20 handoff items. Auto-continue.
