# [SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-008]
# GROUP A — TEAM B Nine-Finding Formal-IBPV Corrective Rework Pre-Prompt Challenge & Readiness Record / L999.999

Project: SMEsPlus ENTERPRISE SUITE  
STATE: STATE03 — Architecture  
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone  
Execution Team: TEAM B — Independent Canonical Domain Design  
Lifecycle Stage: Targeted corrective rework after Formal IBPV FV-006  
Boss: Sole Final Approver  
Risk Class: HIGH  
Canonical Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Canonical Baseline at Challenge Start: `1bac1379cbd09e2deae458840a6c754105213357`  
Frozen TEAM B Design Input: `b98a3b9fb435845dbd15fae79db63b0b73a82420`  
Formal IBPV Finding Commit: `535724c0a2a5d0a972713f513dc567d8b27fc89b`  
Dedicated Corrective Branch: `claude/team-b-group-a-sip-corr-008`

## 1. Boss Directive

Boss directs the project to consolidate the previous eight TEAM-B-owned Formal IBPV corrective findings together with the SaaS/Tenant baseline-traceability finding into **one next End-to-End corrective prompt**, and to continue until the material doubt in the controlled corrective scope is exhausted.

Boss also clarified the governing SaaS principle:

- SMEsPlus is a SaaS platform and Tenant context is not an optional per-module feature.
- Tenant context applies cross-module.
- Company-scoped operations require Tenant + Company context.
- Do not ask Boss to re-approve whether SMEsPlus should be multi-tenant.

CORR-007 is superseded before execution by CORR-008. This is documented in `CORRECTIVE_CORR_007/02_SUPERSESSION_NOTICE_CORR007_TO_CORR008.md`.

This authorization is not a declaration that TEAM B is Final, that Formal IBPV passes after TEAM B edits, that the Pre-Development Gate passes, or that TEAM C may start.

## 2. Controlled Corrective Scope — Nine Findings

1. **Denied-approval wind-down path** — Formal IBPV D14 §3.4 / `FV006-STE-004` + `FV006-EVT-003`.
2. **Retry / idempotency contract for Confirm and Movement Execution** — D14 §3.5 / `FV006-INT-001`.
3. **Downstream-failure compensation for hard cross-domain handoffs** — D14 §3.5 / `FV006-INT-002`.
4. **Sequential-approval wording internal inconsistency** — D14 §3.1 / `FV006-SOD-004`.
5. **Self-approval mechanism gap** — D14 §3.1 / `FV006-SOD-001`.
6. **Event transport-semantics gap** — D14 §3.6 / `FV006-EVT-002`.
7. **Lot/serial and package fact ownership/lifecycle gap** — D14 §3.7 / `FV006-DFO-001`.
8. **Shared-master archival / hard-delete protection rule** — D14 §3.7 / `FV006-DFO-005`.
9. **SaaS / Tenant baseline traceability reconciliation** — Formal IBPV D14 §3.2 / `FV006-SAAS-001`, D13 `FV006-GAP-007`, D03 `FV006-XDF-006`; reconcile TEAM B's Tenant boundary model to the already-established SaaS context controls without re-deciding the Multi-Tenant principle.

The ninth item is a controlled reclassification of the IBPV concern. The project already has a controlled SaaS context ruling stating:

- Platform Template administration = Platform Context.
- Tenant-owned or tenant-access operation = Tenant Context mandatory.
- Company-scoped operation = Tenant Context + Company Context mandatory.
- Platform operations must not impersonate Tenant operations.
- Tenant/Company operations must not access or mutate Platform-owned Published Standard Template data.

Therefore the corrective question is not `Should SMEsPlus be multi-tenant?` The corrective question is `Does TEAM B's GROUP A Tenant/Company boundary design trace correctly to the approved SaaS context controls, and are any additional structural statements clearly identified as design elaboration, evidence-supported fact, controlled assumption, or unresolved decision rather than silently presented as pre-approved baseline?`

## 3. Five-Unit Pre-Prompt Challenge

### 3.1 Audit VETO — Evidence / Governance Challenge

Status: **NO VETO — PROCEED WITH NINE-FINDING TARGETED CORRECTION**

Mandatory controls:

- Correct only the nine findings and directly necessary cross-file consistency references.
- Do not re-open the question of whether SMEsPlus is SaaS or multi-tenant.
- For CORR8-09, distinguish `existing Boss-controlled SaaS invariant` from `TEAM B structural elaboration` and from `genuinely new unsupported structural assumption`.
- Do not convert an Accounting-domain COA-specific observation into a GROUP-A-wide factual rule unless the underlying ruling is explicitly cross-module or Boss has now reaffirmed it as such.
- Preserve the frozen TEAM B package as the pre-correction audit baseline.
- Every changed statement must trace to an IBPV finding, governing baseline, or explicit corrective rationale.
- If a genuinely new material tenancy structural decision cannot be derived from current controls, register it as `DESIGN DECISION BLOCKED AT THIS POINT`; do not invent it.
- No Team C, no code, no DDL/ORM/API implementation, no merge to `SMEsPlus`.
- Reconcile historical readiness/manifest artifacts after edits and create a new reproducible corrective manifest/readiness record.

### 3.2 TBRAC — Thailand Reality Challenge

Status: **PROCEED — NO THAILAND-SPECIFIC BLOCKER**

Challenge result:

- The nine corrections are generic design/control/integrity/traceability matters.
- SaaS Tenant/Company context is a platform-control issue, not a Thailand-business-reality claim.
- Do not turn Tax Branch or other Thai observations into universal Tenant structure unless separately evidenced/approved.
- Preserve existing TBRAC evidence classification; no real-user validation is required merely to close these internal design defects.

### 3.3 EXPERT IBPV — Pre-Prompt Advisory Challenge

Status: **PROCEED — TARGETED REWORK IS THE CORRECT OWNER/ACTION**

TEAM B must answer independently:

- Denied approval: What business state/event winds down the pending commitment and downstream demand, and what audit history remains?
- Retry/idempotency: What invariant makes repeated Confirm/Movement Execution safe from duplicate business effects?
- Cross-domain failure: What business truth, ownership, retry eligibility, and convergence state applies when receiver-side handoff fails?
- Sequential wording: Does the design avoid claiming enforcement sequencing that evidence has not verified?
- Self-approval: Is creator/requester identity distinguished from approver identity explicitly?
- Event semantics: Are sync/async class, ordering expectation, duplicate/replay behavior, and consumer-failure handling explicit enough for canonical flow integrity?
- Traceability/Handling Unit: Who owns each fact, which events create/change/retire it, and what history survives?
- Shared Master: Is destructive hard deletion prevented once history references the fact?
- SaaS/Tenant: Can every material Tenant/Company boundary statement be traced to existing platform governance, or clearly labeled as TEAM B elaboration/assumption/unknown; and does the corrected GROUP A model preserve Tenant isolation consistently across all relevant facts and handoffs?

IBPV findings define defects and verification questions; they are not an answer key. Formal IBPV re-verification remains mandatory after TEAM B correction.

### 3.4 EXPERT IDTM — Future Testability Challenge

Status: **PROCEED — ADVISORY ONLY**

Corrective design must become future-testable without writing Formal tests now:

- observable state/event outcomes;
- exact duplicate/retry invariants;
- explicit recovery/convergence truth;
- exact ownership/history invariants;
- explicit Tenant/Company isolation invariants that future Multi-Tenant/Security tests can assert.

IDTM must not dictate implementation technology or architecture.

### 3.5 EXPERT IESA — ERP & SaaS System-Level Challenge

Status: **PROCEED — SYSTEM-INTEGRITY LENS ONLY**

Corrective design must avoid local fixes that create systemic ambiguity:

- orphan demand after approval denial;
- duplicated commitments/movements/reservations;
- unauditable failure states;
- cross-domain inconsistency;
- tenant/company leakage;
- destructive loss of historical references;
- a Tenant structure that contradicts the project's platform-wide SaaS boundary.

IESA is advisory here; no Formal IESA assurance is active.

## 4. Consolidated Challenge Result

| Unit | Result |
|---|---|
| Audit VETO | NO VETO — nine-finding targeted correction required |
| TBRAC | PROCEED — no Thailand-specific blocker |
| IBPV advisory | PROCEED — nine corrective questions are valid TEAM B work |
| IDTM advisory | PROCEED — make corrected semantics future-testable |
| IESA advisory | PROCEED — preserve ERP/SaaS system integrity |

## 5. Prompt Readiness Decision

```text
Target: TEAM B targeted corrective rework of nine Formal IBPV findings
Risk: HIGH
Five-Unit Challenge: COMPLETE
Critical Blocking Unknown Before Start: NONE
Scope Owner: TEAM B
New Evidence Required Before Start: NO
Boss Policy Decision Required Before Start: NO for the nine corrective questions as framed
Tenant / Multi-Tenant Principle: ALREADY CONTROLLED — DO NOT RE-ASK
Genuinely New Tenant Structural Rule: MUST BE LABELED; may remain CONTROLLED UNKNOWN if not derivable
Team D: NOT ACTIVE
TEAM C / Development: NOT AUTHORIZED
Formal IBPV Re-Verification: REQUIRED AFTER CORRECTIVE COMPLETION
Readiness: READY
```

## 6. Hard Boundary — Items Not Closed by This Corrective Scope

This corrective session must not falsely report the entire Pre-Development Gate as PASS. Separate items remain governed by their own evidence/authority paths, including:

- cancellation-gate dependency on Accounting/AR-AP semantics;
- acquisition/reconstruction of missing legacy approval internal-workflow source;
- deferred business-policy defaults: canonical Invoiced Quantity, Over-Fulfillment/Over-Billing default, Sales Confirmation Gate default;
- unrelated Team A High/Medium/Low gaps;
- Figma/UX, Team C implementation, Team D, Formal IDTM, Formal IESA, Release or Production.

CORR-008 may close the **Tenant baseline-traceability defect**; it may not invent unresolved Tenant implementation architecture or claim runtime isolation proof.

## 7. Required Terminal State

The corrective session may terminate only as one of:

- `TEAM B CORRECTIVE REWORK COMPLETE — NINE FINDINGS CLOSED — READY FOR FORMAL IBPV RE-VERIFICATION`
- `TEAM B CORRECTIVE REWORK PARTIAL — MATERIAL GAP REMAINS / HOLD`
- `FAIL / FROZEN — TRUE STOP CONDITION`

It may not declare `BOSS APPROVED`, `FINAL APPROVED`, `PRE-DEVELOPMENT GATE PASS`, `TEAM C AUTHORIZED`, `DEVELOPMENT READY`, or `PRODUCTION READY`.

`Ask until materially clear — not until everyone agrees.`  
`Independent experts challenge the questions; the authorized Team discovers the answers.`
