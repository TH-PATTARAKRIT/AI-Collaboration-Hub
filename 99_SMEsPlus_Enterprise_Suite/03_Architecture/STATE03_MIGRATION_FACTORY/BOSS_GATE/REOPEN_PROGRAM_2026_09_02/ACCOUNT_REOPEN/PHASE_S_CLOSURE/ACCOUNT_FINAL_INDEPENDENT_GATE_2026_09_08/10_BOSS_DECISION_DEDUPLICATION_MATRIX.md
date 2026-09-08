# 10 — BOSS DECISION DEDUPLICATION MATRIX

Timestamp: `2026-09-08T19:28+07:00`
Prepared by: SMT + Secretary / Independent Gate
Purpose: Boss sees only genuine architecture/business/legal decisions; no technical mechanics are pushed upward.

| Candidate | Classification | SMT / Secretary recommendation | Phase-S gate impact |
|---|---|---|---|
| `BD-ACC-01` accounting-event identity as a platform property | **GENUINE NEW BOSS ARCHITECTURE DECISION** | Carry to Boss Final Gate. If deferred, Phase SA may proceed by treating event identity / recognition trigger / period membership as required inputs rather than deriving them. | **Not the cause of current HOLD** |
| `BD-ACC-02` whether tax-reporting grouping may span companies and under what security boundary | **GENUINE BOSS STATUTORY / SECURITY DECISION** | Carry to Boss or qualified Thai tax/legal authority. All non-statutory interfaces may proceed around it. | **Only Tax interface attribute waits** |
| `BD-ACC-03` valuation-method policy | **ALREADY DECIDED — DO NOT ASK BOSS AGAIN AS A GLOBAL POLICY** | Carry forward the established SMEsPlus policy: supported costing methods include Standard / Average (AVCO) / FIFO, with valuation/costing policy owned at Product Category configuration boundary. A tenant/company choosing among supported methods is a Phase-SA/configuration decision, not a new global Boss question. | **No new Boss decision required** |
| `BD-ACC-04` bare `AAS+-VETO-01` collision | **NOT A PHASE-S BOSS BLOCKER — GOVERNANCE HOUSEKEEPING** | Use producer-qualified identifiers `P08/AAS+-VETO-01` and `P09/AAS+-VETO-01` now. Renumber only if PMO later wants canonical namespace cleanup, preserving lineage. | **Deferable non-blocker** |

## What Boss is NOT asked to decide

Boss is not asked to decide:
- B-35 instrument mechanics — independently certified by this gate;
- RC-04/RC-05/M-2 technical outcomes — SMT/verifier decides from evidence;
- whether Account should continue — current gate result determines that;
- how to correct the two bounded carrier defects — exact owner/action is already named.

## Final Boss-facing set

Only two genuine material decisions remain for a future Boss Final Gate:
1. `BD-ACC-01` — accounting-event identity ownership.
2. `BD-ACC-02` — cross-company tax-reporting grouping/security boundary.

Neither is the cause of the present Phase-S technical HOLD. The present HOLD is caused only by the bounded P09 and P08 carrier defects identified by GATE-02 and GATE-03.
