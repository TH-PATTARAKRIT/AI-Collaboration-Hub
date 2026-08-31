> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B Corrective Rework (CORR-008)

# 26 — TEAM B CORR-008 DELTA AND TRACEABILITY REGISTER

Session: `SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-008`

Each entry follows the governance-required chain format established in
[19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md](../19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md) §02:
`Formal IBPV Finding / Boss Clarification → pre-correction statement → governing evidence → correction decision
→ corrected artifact/section → re-verification question`.

---

### CORR8-01 — Denied-Approval Wind-Down Path
```
Finding: FV006-STE-004 (D04, Critical) / FV006-EVT-003 (D05, Critical)
→ Pre-correction statement: "07" §01 stated Pending Approval with no exit on denial; "08" §01 and "09" §02
  conflicted on when the Inventory fulfillment request was created
→ Governing evidence: none evidencing the internal legacy logic (Boss Gate §4.1 Controlled Carry-Forward
  Unknown, unaffected); the state/event completeness question is independently resolvable without it
→ Correction decision: add `Rejected` state, `Supply Commitment Rejected` event; resolve the create-timing
  conflict by adopting "created synchronously at Confirm, Blocked during Pending Approval"; reuse the existing
  Cancellation not-yet-executed cascade for stand-down rather than inventing a new one
→ Corrected artifact/section: 07 §01/§03; 08 §01; 09 §02; 12 §14
→ Re-verification question: does the closure eliminate the orphaned-fulfillment-request risk without inventing
  legacy internal logic?
```

### CORR8-02 — Retry / Idempotency Contract
```
Finding: FV006-INT-001 (D10, Critical)
→ Pre-correction statement: idempotency stated only for the Stock Position bin case (12 §11)
→ Governing evidence: TEAM A 13 §02 item 3 (the one evidenced concurrency case)
→ Correction decision: state one general business-identity idempotency invariant for every Confirm/Movement-
  Execution action, without prescribing implementation mechanism
→ Corrected artifact/section: 12 §11 (new paragraph); 08 new §11; 09 §00A (cross-reference)
→ Re-verification question: does the invariant cover every action category FV006-INT-001 named?
```

### CORR8-03 — Downstream-Failure Compensation
```
Finding: FV006-INT-002 (D10, Major)
→ Pre-correction statement: both Hard handoffs (10 §02) documented success path only
→ Governing evidence: none directly (12 §13's UNKNOWN is adjacent, not identical scope)
→ Correction decision: add Handoff Unresolved/Resolved observable status pair, owned by the initiating
  Commitment, detected via the transport window, retryable under CORR8-02's contract, no invented compensation
→ Corrected artifact/section: 10 §02 (new column); 12 new §13A; 09 new §03A; 08 new §12
→ Re-verification question: does the owner/status/retry/convergence/audit statement satisfy all seven CORR-008
  §4 elements for both named Hard handoffs?
```

### CORR8-04 — Sequential-Approval Wording Inconsistency
```
Finding: FV006-SOD-004 (D07, Major)
→ Pre-correction statement: 13 §03/§06 and 07 §03 used "Sequential"/"ordered" without distinguishing
  numbering/labeling from enforced gating order
→ Governing evidence: Boss Evidence Gate carry-forward control item 1
→ Correction decision: wording clarification only, at every point of use — no redesign, no renaming of the
  control's own label
→ Corrected artifact/section: 13 §03 (reading-note blockquote + row edit); 13 §06; 07 §03
→ Re-verification question: does every instance of "sequential"/"ordered" now carry the numbering-only
  qualifier?
```

### CORR8-05 — Self-Approval Mechanism Gap
```
Finding: FV006-SOD-001 (D07, Major)
→ Pre-correction statement: 13 §02's Business Problem/Need said "prevent self-approval"; mechanism was
  role-based only
→ Governing evidence: TEAM A 13 §01 item 10 (role-based gate, test-confirmed); identity-based half not
  evidenced, added as a new TEAM B target requirement
→ Correction decision: add an explicit identity-based self-approval exclusion requirement, independent of role
  membership, composing with the existing §05 SoD data-shape requirement
→ Corrected artifact/section: 13 §02 (rows rewritten/added); 13 §05 (cross-reference); 13 §06
→ Re-verification question: does the addition fully satisfy APR-001's own stated purpose, and is it correctly
  labeled as a target requirement rather than a legacy-behavior claim?
```

### CORR8-06 — Event Transport / Interaction Semantics
```
Finding: FV006-EVT-002 (D05, Critical, systemic)
→ Pre-correction statement: no event stated sync/async, ordering, or consumer-failure behavior
→ Governing evidence: 08 §10's one-pair-only transport characterization (Purchase direct/synchronous vs. Sales
  indirect/event-driven)
→ Correction decision: one catalog-wide transport-semantics section — classification rule, default, ordering
  guarantee, consumer-failure rule — closed once rather than per-row
→ Corrected artifact/section: 09 new §00A
→ Re-verification question: does the rule give sufficient precision for a future pass/fail test, without
  resolving the separate FV006-EVT-004/005 race findings (explicitly out of CORR-008 scope)?
```

### CORR8-07 — Traceability Unit / Handling Unit Ownership & Lifecycle
```
Finding: FV006-DFO-001 (D06, Major)
→ Pre-correction statement: both facts catalogued in 03 §03 but absent from the Master Ownership Table (10 §01)
→ Governing evidence: none for an ownership-matrix equivalent (design-completeness question, not an
  evidence-traceability one)
→ Correction decision: add three rows to 10 §01 (owner = Inventory, exclusively); define lifecycle-end for
  each; explicitly avoid deepening the separate, open FV006-EVT-001 dead-event question by not adding new
  catalogued events
→ Corrected artifact/section: 10 §01; 03 §03 (cross-ref); 05 §06 (cross-ref); 12 §05 (Reversal-linkage note)
→ Re-verification question: does the ownership/lifecycle statement meet the same completeness bar as every
  other Master Ownership Table row?
```

### CORR8-08 — Shared-Master Archival / Hard-Delete Protection Rule
```
Finding: FV006-DFO-005 (D06, Major)
→ Pre-correction statement: no general archival rule; protection stated only for UOM's conversion ratio and
  Warehouse's owning-company assignment
→ Governing evidence: TEAM A UOM-06, PAY-07, CUR-08
→ Correction decision: generalize the three evidenced individual protections into one rule spanning every
  Shared Master concept, with a stated zero-historical-reference exception boundary
→ Corrected artifact/section: 04 new §08; 03 §01 (cross-ref)
→ Re-verification question: does the generalization avoid overstating evidence for concepts with no
  individually-evidenced protection?
```

### CORR8-09 — SaaS / Tenant Baseline Traceability Reconciliation
```
Finding: FV006-SAAS-001 (D11, Major) / FV006-SAAS-003 (D11, Moderate) / FV006-XDF-006 (D03, Critical) /
  FV006-GAP-007 (D13, Major, consolidated) + Boss CORR-008 clarification (multi-tenancy not re-decided)
→ Pre-correction statement: 14 presented the Tenant mandate and its own structural elaboration without
  distinguishing their evidentiary weight
→ Governing evidence: STATE01_PROJECT_CHARTER_v1.0.md §5; STATE01_SCOPE_PRINCIPLES_RACI_v1.0.md; 
  ARCHITECTURE_GOVERNANCE_STANDARD.md (mandate only); AQ Boss SaaS Context Clarification §3 items 2-3 and
  COA-G01 SI-01/SI-02 (the same cross-module Tenant/Company-context invariant, already established for
  Domain 01)
→ Correction decision: five-category statement-by-statement classification (14 §08); per-row Tenant-scoping
  restatement (14 §05); full cross-file sweep confirming no contradiction elsewhere
→ Corrected artifact/section: 14 §00, §02, §03, §05, new §08; 18 §04 (reclassification, retained not deleted)
→ Re-verification question: is the mandate correctly traced to its approved sources, is the structural
  elaboration honestly labeled as TEAM B's own choice, and does no statement permit cross-tenant leakage?
```

---

## Coverage Statement

All nine CORR-008 findings have a complete chain entry above. No entry omits a link in the required chain. This
register is additive to, and does not replace,
[19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md](../19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md), which remains
the traceability record for the pre-correction package's original decisions.
