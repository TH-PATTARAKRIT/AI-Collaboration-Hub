# [SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-010-PRE]
# GROUP A — Non-Accounting Targeted Closure Pre-Prompt Five-Unit Challenge / L999.999

Project: SMEsPlus ENTERPRISE SUITE  
STATE: STATE03 — Architecture  
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone  
Boss: Sole Final Approver  
Risk Class: HIGH — Pre-Development blocker correction  
Current corrected TEAM B input: `359f96c0cfee2f74955fe7e8f1d0110ec21a0a45`  
Formal IBPV RV-009 final branch head reviewed: `b2f7cbd3131963fca176a0ac0939c4bdf8af3e25`  
Target TEAM B branch: `claude/team-b-group-a-sip-nonacct-corr-010`

## 1. Boss Directive

Boss approves the control rule:

> **Close all non-Accounting GROUP A work first. Do not declare Pre-Development Gate PASS until the required Accounting/AR-AP dependency is independently resolved.**

Purpose: remove every executable GROUP A blocker that does not depend on Accounting, while keeping the Accounting-dependent Sales cancellation-gate item explicitly on HOLD rather than allowing GROUP A to invent AR/AP lifecycle facts.

This authorization does not authorize Team C, Development, merge to `SMEsPlus`, Production, or a Pre-Development Gate PASS.

## 2. Five-Unit Challenge

### 2.1 Audit VETO

Status: **NO VETO — PROCEED WITH NARROW NON-ACCOUNTING CLOSURE**

Mandatory controls:

1. Freeze `359f96c...` as the TEAM B design input; treat RV-009 as independent finding evidence, not editable source design.
2. Close only non-Accounting items that TEAM B has authority to resolve.
3. Do not self-resolve Sales-side cancellation-gate symmetry / AR-AP lifecycle dependency.
4. Do not claim legacy approval internal workflow is known when source evidence remains missing.
5. Do not merge or modify TEAM A or prior IBPV evidence.
6. Preserve all historical evidence and supersession chains.
7. Rebuild hashes after TEAM B correction and stop for independent IBPV re-verification.

### 2.2 TBRAC

Status: **PROCEED — NO NEW THAILAND-WIDE CLAIMS**

The target findings are concurrency, event, state, evidence-labeling and documentation-control matters. No correction may generalize reference/customer behavior into Thailand-wide business reality. Existing real-user-validation classifications remain unchanged unless new authoritative evidence exists.

### 2.3 EXPERT IBPV

Status: **PROCEED — TARGETED CLOSURE REQUIRED**

Mandatory closure scope from RV-009:

- `FV006-EVT-004` — ordering race condition;
- `FV006-EVT-005` — reservation-claim atomicity race;
- `FV006-EVT-001` — dead-event-catalog question registration/disposition;
- RV-009 light TEAM B defects B1–B8;
- correction of false/stale tracking statements concerning `EVT-001/004/005`;
- explicit residual register showing Accounting-dependent A1 remains HOLD;
- explicit residual register showing legacy approval internal-logic evidence A2 remains Boss-decision/evidence-boundary controlled unless authoritative evidence exists.

The three deferred policy defaults remain safe to defer unless the correction uncovers a new dependency that changes that conclusion.

### 2.4 EXPERT IDTM — Advisory Only

Status: **PROCEED**

Corrections must be future-testable without dictating implementation technology. In particular:

- same-line event ordering must have one unambiguous truth;
- reservation ownership/claim atomicity must have an observable invariant preventing double allocation;
- duplicate/retry semantics must remain consistent with CORR-008 idempotency rules;
- race-condition resolution must identify exact precondition, event/state effect and invariant.

No Formal IDTM matrix is created here.

### 2.5 EXPERT IESA — Advisory Only

Status: **PROCEED**

Check that local race-condition fixes do not create system-level contradictions across Sales, Inventory, Purchase, Tenant/Company boundaries or Accounting interface boundaries. Do not redesign Accounting Core. Do not re-open Multi-Tenant SaaS mandate.

## 3. Scope Classification

### IN SCOPE — TEAM B may close now

1. `FV006-EVT-004` ordering-race design defect.
2. `FV006-EVT-005` reservation-claim atomicity defect.
3. `FV006-EVT-001` registration/disposition and any directly necessary event-catalog correction.
4. RV-009 B1–B8 documentation/precision/cross-reference/labeling defects.
5. File 18 zero-silent-drop registration for `EVT-001/004/005`.
6. Removal/correction of false claims that these findings were already tracked.
7. Cross-file consistency and regression sweep over corrected TEAM B artifacts.
8. Corrective evidence package and SHA-256 manifest.

### CONTROLLED CARRY-FORWARD — DO NOT SELF-CLOSE

A1. Sales-side cancellation-gate symmetry / Accounting-AR/AP dependency.  
Status: `HOLD — WAITING FOR ACCOUNTING/AR-AP AUTHORITY`.

A2. Legacy approval internal workflow / permission evidence for the three named modules.  
Status: preserve as `EVIDENCE MISSING / BOSS DECISION REQUIRED` unless authoritative evidence is independently obtained under separate authority.

A3. Three deferred policy defaults.  
Status: safe to defer unless new evidence changes the dependency timing.

C4. TEAM A evidence branch-lineage integration.  
Owner: PMO / repository governance. TEAM B may produce a precise handoff note but must not alter TEAM A evidence to manufacture lineage.

## 4. Multi-Approve Boundary

Approval-related correction may maintain a clean vendor-neutral interface boundary with a configurable approval capability, but this corrective session must **not** redesign or implement a Multi-Approve engine, infer legacy approval internals, or make company-specific approval policy decisions without an approved baseline.

Allowed: clarify what GROUP A must provide to / receive from an approval capability (request facts, result, actor/reason/audit requirements, state/event consequences).  
Not allowed: design engine internals, approval-rule DSL, database schema, workflow implementation, or copy legacy behavior.

## 5. Prompt Readiness

| Field | Result |
|---|---|
| Risk | HIGH |
| Audit VETO | NO VETO |
| TBRAC | PROCEED |
| IBPV | TARGETED CLOSURE REQUIRED |
| IDTM | ADVISORY ONLY |
| IESA | ADVISORY ONLY |
| Blocking unknown before TEAM B starts | NONE for authorized non-Accounting scope |
| Accounting-dependent blocker | EXPLICIT HOLD / OUT OF CORR-010 EXECUTION SCOPE |
| Readiness | **READY** |
| Team C | NOT AUTHORIZED |
| Pre-Development Gate | MUST NOT PASS in this session |

## 6. Required Terminal Meaning

A successful CORR-010 terminal state may state only that all authorized **non-Accounting** TEAM B corrective items are closed and ready for independent re-verification.

It must also state that GROUP A remains **Pre-Development Gate HOLD** pending at least the authoritative Accounting/AR-AP dependency and any separate Boss decision still required for legacy approval fidelity.

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
