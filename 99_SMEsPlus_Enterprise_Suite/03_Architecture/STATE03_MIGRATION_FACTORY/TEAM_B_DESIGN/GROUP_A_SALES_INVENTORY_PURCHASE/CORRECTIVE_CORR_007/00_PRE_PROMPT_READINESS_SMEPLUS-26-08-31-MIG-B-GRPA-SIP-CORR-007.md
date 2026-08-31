# [SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-007]
# GROUP A — TEAM B Targeted IBPV Corrective Rework Pre-Prompt Challenge & Readiness Record / L999.999

Project: SMEsPlus ENTERPRISE SUITE  
STATE: STATE03 — Architecture  
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone  
Execution Team: TEAM B — Independent Canonical Domain Design  
Lifecycle Stage: Targeted corrective rework after Formal IBPV FV-006  
Boss: Sole Final Approver  
Risk Class: HIGH  
Canonical Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Canonical Baseline at Challenge Start: `3dc8b1e3572041f7d98e0e5fb8207d7bfda63512`  
Frozen TEAM B Design Input: `b98a3b9fb435845dbd15fae79db63b0b73a82420`  
Formal IBPV Finding Commit: `535724c0a2a5d0a972713f513dc567d8b27fc89b`  
Dedicated Corrective Branch: `claude/team-b-group-a-sip-corr-007`

## 1. Boss Directive

Boss accepts the eight TEAM-B-owned rework items identified by Formal IBPV and directs the project to close them thoroughly until the material ambiguity in those eight items is exhausted.

This authorization is **not** a declaration that TEAM B is Final, that the Pre-Development Gate passes, or that TEAM C may start.

Current corrective scope is limited to the eight TEAM-B-owned design/documentation gaps below. It does not silently resolve separate Boss-policy, Accounting-domain, or evidence-acquisition items.

## 2. Controlled Corrective Scope — Eight Findings

1. **Denied-approval wind-down path** — Formal IBPV D14 §3.4 / `FV006-STE-004` + `FV006-EVT-003`.
2. **Retry / idempotency contract for Confirm and Movement Execution** — D14 §3.5 / `FV006-INT-001`.
3. **Downstream-failure compensation for hard cross-domain handoffs** — D14 §3.5 / `FV006-INT-002`.
4. **Sequential-approval wording internal inconsistency** — D14 §3.1 / `FV006-SOD-004`.
5. **Self-approval mechanism gap** — D14 §3.1 / `FV006-SOD-001`.
6. **Event transport-semantics gap** — D14 §3.6 / `FV006-EVT-002`.
7. **Lot/serial and package fact ownership/lifecycle gap** — D14 §3.7 / `FV006-DFO-001`.
8. **Shared-master archival / hard-delete protection rule** — D14 §3.7 / `FV006-DFO-005`.

Formal IBPV Deliverable 15 explicitly classifies these as TEAM B corrective work that does not require a new Boss business-policy decision or new source evidence in order to design/clarify them.

## 3. Five-Unit Pre-Prompt Challenge

### 3.1 Audit VETO — Evidence / Governance Challenge

Status: **NO VETO — PROCEED WITH TARGETED CORRECTION**

Mandatory controls:

- Correct only the eight listed findings and any directly necessary cross-file consistency references.
- Do not use this corrective session to resolve the separate cancellation-gate Accounting-domain decision, legacy approval-source acquisition, deferred policy defaults, or unrelated Group A gaps.
- Preserve the frozen TEAM B package as the pre-correction audit baseline. Every changed design statement must be traceable to an IBPV finding and a corrective rationale.
- No silent invention. If a correction exposes a material dependency that cannot be settled inside TEAM B authority, classify it `DESIGN DECISION BLOCKED AT THIS POINT` and stop only that decision point.
- No Team C, no code, no DDL/ORM/API implementation, no merge to `SMEsPlus`.
- The old TEAM B readiness/manifest artifacts must not remain misleading after design changes; explicitly supersede/reconcile them and create a new reproducible corrective manifest/readiness record.

### 3.2 TBRAC — Thailand Reality Challenge

Status: **PROCEED — NO THAILAND-SPECIFIC BLOCKER FOR THESE EIGHT ITEMS**

Challenge result:

- The eight corrections are generic control/integrity/design-clarity matters, not evidence that a particular behavior is Thailand-wide practice.
- Do not convert retry, approval, archival, event-delivery, lot/serial/package, or failure-compensation rules into Thailand claims unless a source explicitly supports that classification.
- Preserve all existing TBRAC classifications. No real-user validation is required merely to close these eight internal design defects.

### 3.3 EXPERT IBPV — Pre-Prompt Advisory Challenge

Status: **PROCEED — TARGETED REWORK IS THE CORRECT OWNER/ACTION**

Closure questions TEAM B must answer explicitly:

- Denied approval: What exact business state/event winds down the pending commitment, what downstream demand is withdrawn, and what audit history remains?
- Retry/idempotency: What makes Confirm and Movement Execution safely repeatable, and what observable result proves a duplicate request did not create duplicate business effects?
- Cross-domain failure: What is the business-level compensation/reconciliation contract when the initiator commits but the receiver fails?
- Sequential wording: Does the design distinguish level numbering/order metadata from unverified enforcement sequencing?
- Self-approval: Is identity-based self-approval prevention explicitly represented, rather than assumed from role membership?
- Event semantics: For every material event class, are sync/async semantics, ordering expectations, duplicate-delivery behavior, and consumer-failure handling explicit at the canonical contract level?
- Traceability Unit / Handling Unit: Who owns the fact, what events create/change/retire it, and what historical references survive?
- Shared Master: Is there a general archival/immutability rule preventing destructive hard deletion once historical transactions reference the fact?

IBPV does not supply the design answers; TEAM B must independently close the defects and later submit to independent re-verification.

### 3.4 EXPERT IDTM — Future Testability Challenge

Status: **PROCEED — ADVISORY ONLY**

Corrective design must become future-testable without writing tests now:

- state/event transitions must have observable preconditions and outcomes;
- retry/idempotency must expose a stable business identity/deduplication invariant at semantic level without prescribing implementation;
- failure compensation must define post-failure truth and reconciliation outcome;
- event contracts must define delivery/ordering assumptions sufficiently for later concurrency/fault-injection tests;
- ownership/archival rules must create exact invariants that later tests can assert.

IDTM must not dictate implementation architecture or become an answer key for TEAM B.

### 3.5 EXPERT IESA — ERP & SaaS System-Level Challenge

Status: **PROCEED — SYSTEM-INTEGRITY LENS ONLY**

Corrective design must avoid local fixes that create system-level ambiguity:

- denied approvals must not leave orphan demand or hidden financial/control exposure;
- retries must not duplicate commitments, movements, reservations, or downstream effects;
- failed cross-domain handoffs must converge to an auditable known state;
- approval and archival controls must remain compatible with multi-company/tenant isolation and immutable audit history;
- lot/serial/package ownership must remain coherent across cross-domain handoffs.

IESA is advisory here; no Formal IESA assurance is active.

## 4. Consolidated Challenge Result

| Unit | Result |
|---|---|
| Audit VETO | NO VETO — targeted correction required |
| TBRAC | PROCEED — no Thailand-specific blocker |
| IBPV advisory | PROCEED — eight defects are TEAM B-owned corrective scope |
| IDTM advisory | PROCEED — make corrected semantics future-testable |
| IESA advisory | PROCEED — preserve ERP/SaaS system integrity |

## 5. Prompt Readiness Decision

```text
Target: TEAM B targeted corrective rework of eight Formal IBPV findings
Risk: HIGH
Five-Unit Challenge: COMPLETE
Critical Blocking Unknown Before Start: NONE
Scope Owner: TEAM B
New Evidence Required Before Start: NO
Boss Policy Decision Required Before Start: NO for these eight items
Team D: NOT ACTIVE
TEAM C / Development: NOT AUTHORIZED
Formal IBPV Re-Verification: REQUIRED AFTER CORRECTIVE COMPLETION
Readiness: READY
```

## 6. Hard Boundary — Items Not Closed by This Corrective Scope

This session must not falsely report the entire Pre-Development Gate as PASS. Separate items remain governed by their own evidence/authority paths, including:

- the cancellation-gate dependency on Accounting/AR-AP semantics;
- legacy approval internal-workflow source/evidence acquisition;
- the deferred business-policy defaults already listed by TEAM B/IBPV;
- any other independent Formal IBPV finding not one of the eight controlled TEAM B rework items above.

SaaS/Tenant is a mandatory cross-module platform invariant already established elsewhere in project governance; this corrective session must not ask whether SMEsPlus should be multi-tenant. Any separate Tenant issue is a baseline-traceability/structural-detail review, not authority to remove or re-decide the mandatory Tenant principle.

## 7. Required Terminal State of the Corrective Session

The corrective session may terminate only as one of:

- `TEAM B CORRECTIVE REWORK COMPLETE — EIGHT FINDINGS CLOSED — READY FOR FORMAL IBPV RE-VERIFICATION`
- `TEAM B CORRECTIVE REWORK PARTIAL — MATERIAL GAP REMAINS / HOLD`
- `FAIL / FROZEN — TRUE STOP CONDITION`

It may not declare:

- `BOSS APPROVED`
- `FINAL APPROVED`
- `TEAM C AUTHORIZED`
- `DEVELOPMENT READY`
- `PRE-DEVELOPMENT GATE PASS`

`Ask until materially clear — not until everyone agrees.`  
`Independent experts challenge the questions; the authorized Team discovers the answers.`
