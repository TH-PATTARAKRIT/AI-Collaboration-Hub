# DOMAIN_01 ACCOUNTING CORE — TEAM B TARGETED REVISION DIRECTIVE

## Control identity

| Field | Value |
|---|---|
| Project | SMEsPlus ENTERPRISE SUITE |
| STATE | STATE03 — Architecture |
| Board | Board06 — Data & Canonical Model |
| Workstream | SMEsPlus Migration Factory |
| Domain | DOMAIN_01 — Accounting Core |
| Directive | CORR-B01 → CORR-B07 Targeted Revision |
| Source audit | `DOMAIN_01_ACCOUNTING_CORE_I_TEAM_B_INDEPENDENT_DESIGN_AUDIT.md` |
| Audit commit | `aa60c2d0497cefe804d37953bbfaa597c3476d79` |
| Jira | `ERPPLUS-100` |
| Issuer role | ChatGPT — Independent Design Auditor / Gate Controller |
| Executor role | Team B — Independent Clean-Room Design Executor |
| Final authority | Boss — Sole Final Approver |
| Status | **AUTHORIZED TARGETED CORRECTION / PMO HOLD / NOT A PASS** |

## 1. Purpose

Execute one controlled corrective round against the existing Team B DOMAIN_01 independent design. Do **not** restart B0–B17. Do not expand product scope. Do not open implementation/development.

The correction must resolve exactly the three material findings from the independent audit and propagate the effects through the existing evidence chain.

## 2. Material findings to close

### D01-B-AUD-01 — Consumption permanence vs period reopen

Current design is internally contradictory because:

- period close is treated as a Consumption trigger;
- Consumption is permanent and cannot be retracted; yet
- period reopen is described as restoring correctability for entries consumed only by period close.

Team B must select one coherent business-semantic model and update every dependent invariant, lifecycle, mathematical rule and traceability statement.

Acceptance test:

```text
No state/lifecycle path may simultaneously require irreversible consumption
and later require that same consumption to disappear for correctability.
```

A candidate direction may distinguish `period lock` from independent permanent consumption, but Team B must independently justify the final model rather than copy this wording as a mandatory design.

### D01-B-AUD-02 — Accounting equation mathematics

Current MP-02 is incomplete for an open reporting period because Revenue and Expense accounts may remain open while the simplified equation is stated as:

```text
Assets = Liabilities + Equity
```

Team B must produce a mathematically valid conceptual formulation covering:

- open-period Revenue and Expense;
- Current Earnings / period result;
- its relationship to Equity;
- transition to period-end close/carry-forward;
- the simplified balance-sheet equation after the relevant closing treatment.

Acceptance test:

```text
A ledger may contain balanced entries and non-zero open-period Revenue/Expense
without making the stated accounting equation false or undefined.
```

No physical storage/schema choice is authorized by this correction.

### D01-B-AUD-03 — Historical as-of stability after VOID

Current MP-09 excludes Lines belonging to a currently VOIDED Entry. If an entry was valid at historical date D1 and was voided later at D2, a future recomputation of `as of D1` can lose the entry and rewrite historical truth.

Team B must define time-consistent historical reconstruction so that later events do not silently alter what was true at the requested historical point.

Acceptance test:

```text
Given Entry E effective at D1 and a later void/correction event at D2 > D1,
recomputing the ledger as-of D1 after D2 must reproduce the same historical fact set
that was effective at D1, subject only to explicitly modeled effective-time semantics.
```

The design may use additive correction/void facts, effective-time event semantics, or another independently reasoned conceptual model. It must not rely on current state alone for historical reconstruction.

## 3. Controlled execution sequence

### CORR-B01 — Lifecycle correction

Update the consumption / period-close / reopen semantics and all directly dependent controls.

Minimum affected evidence:

- `B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md`
- `B05_ACCOUNTING_INVARIANT_BASELINE.md` (`BINV-06`, `BINV-07`, related controls)
- `B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md` where lifecycle assumptions are used
- `B13_DESIGN_OPTION_TRADEOFF_REGISTER.md`

### CORR-B02 — Mathematical correction

Correct MP-02 and any related conceptual/account-category/current-earnings/carry-forward semantics.

Minimum affected evidence:

- `B07_CONCEPTUAL_INFORMATION_MODEL.md`
- `B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md`
- `B05_ACCOUNTING_INVARIANT_BASELINE.md` where carry-forward/equity semantics are affected

### CORR-B03 — Historical reconstruction correction

Correct VOID / correction / as-of semantics.

Minimum affected evidence:

- `B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md`
- `B07_CONCEPTUAL_INFORMATION_MODEL.md` if event/effective-time semantics change
- `B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md` (`MP-09`, `MP-10` as applicable)

### CORR-B04 — Propagation and traceability

Update every downstream artifact affected by CORR-B01..03, at minimum:

- `B15_DESIGN_TRACEABILITY_MATRIX.md`
- `DOMAIN_01_ACCOUNTING_CORE_F_TEAM_B_DESIGN_EVIDENCE_PACK.md`
- `DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md`
- `DOMAIN_01_ACCOUNTING_CORE_H_DESIGN_FINAL_GATE_CANDIDATE.md`

Do not erase prior audit findings. Record corrective history explicitly.

### CORR-B05 — Focused adversarial regression

Run a new focused red-team pass against the corrected interactions. It must test at least:

1. period close → reopen → correction with and without independent permanent consumption;
2. multiple close/reopen cycles;
3. balanced open-period ledger with Revenue/Expense/current earnings;
4. period-end close/carry-forward transition;
5. Entry valid at D1 then VOID/corrected at D2 and historical as-of D1/D2 reconstruction;
6. correction of a correction;
7. multi-company isolation under corrected lifecycle and aggregation semantics;
8. audit-event permanence and reconstructability.

Each test must record expected invariant, observed design result and disposition.

### CORR-B06 — Evidence integrity / remote proof

Publish:

- a correction summary;
- exact list of modified artifacts;
- exact commit SHA;
- remote-push verification;
- owner;
- timestamp;
- verifier/reviewer;
- verification status;
- gate impact.

### CORR-B07 — Mandatory stop

After CORR-B01..06, stop at:

```text
READY FOR CHATGPT INDEPENDENT RE-AUDIT
```

Team B must not self-declare:

- PMO PASS;
- Boss Final Pass;
- development ready;
- production ready;
- schema/API ready.

## 4. Carry-forward controls

The six existing Team B assumptions remain visible. Assumption #2 — period-close behavior — must be revised/reframed if CORR-B01 changes its semantics. No assumption may disappear merely because the correction touches it.

The twenty Team A residual unknowns remain zero-progress carry-forward items unless new inspectable evidence resolves a specific item.

## 5. Clean-room boundary

Allowed:

- independently reasoned business semantics;
- accounting mathematics;
- conceptual entities and relationships;
- state/event semantics;
- invariants and controls;
- clean-room traceability.

Not authorized:

- vendor source/model/table/field/method/class translation;
- physical target schema/SQL/ORM design;
- application code;
- migration engine implementation;
- source reuse;
- CLASS-D source-body inspection.

## 6. Gate state

```text
TEAM B DESIGN EVIDENCE     = VERIFIED REMOTE
CLEAN-ROOM REVIEW          = REVIEW PASS
INDEPENDENT DESIGN AUDIT   = HOLD / TARGETED REVISION
PMO VERIFICATION           = HOLD
BOSS FINAL GATE            = NOT OPEN
DEVELOPMENT                = NOT AUTHORIZED
PRODUCTION                 = NOT AUTHORIZED
```

The scoped DOMAIN_01 work does not close the global Deep Research EC-03 or EC-05 holds.

`No Evidence = No Progress.`  
`Never Skip Gate.`  
`Boss is the sole Final Approver.`