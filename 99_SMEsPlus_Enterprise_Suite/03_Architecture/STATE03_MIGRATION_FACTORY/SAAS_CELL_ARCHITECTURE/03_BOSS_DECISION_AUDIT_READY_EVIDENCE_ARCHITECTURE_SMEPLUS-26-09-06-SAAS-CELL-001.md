# [SMEPLUS-26-09-06-SAAS-CELL-001]
# BOSS DECISION — Audit-Ready & Evidence-Ready Architecture / L9999.9999

Project: SMEsPlus ENTERPRISE SUITE  
Date: 2026-09-06  
Boss: Sole Final Approver  
Jira: ERPPLUS-151  
Decision Status: APPROVED  
Mode: CONTINUATION / DELTA-FIRST / EVIDENCE-FIRST / CLEAN-ROOM / NO RESET

## 1. Decision

Boss APPROVES adding **Audit-Ready & Evidence-Ready Architecture** to the active `SAAS-CELL-001` architecture package.

The intent is to ensure SMEsPlus is designed so that customers can use normal system operations as reliable sources of audit evidence and internal-control evidence without needing to reconstruct history retrospectively.

Core principle:

> AUDITABILITY MUST BE DESIGNED, NOT RETROFITTED.

A transaction, approval, master-data change, access event, control execution, or historical fact that did not generate reliable evidence/provenance when it occurred cannot later be recreated with the same evidentiary reliability.

## 2. Positioning

Approved product positioning:

**SMEsPlus Audit-Ready / Evidence-Ready Platform**

SMEsPlus may support customer certification, audit, assurance, regulatory review, or internal-control assessment by generating and preserving reliable system evidence.

SMEsPlus MUST NOT self-declare that a customer is ISO/SOC/PDPA/GDPR compliant or certified solely because the software contains supporting functions.

## 3. Architecture Layers

1. Business Transaction Layer
2. Internal Control Layer
3. Evidence Generation Layer
4. Tamper-Evident Evidence Store
5. Control / Standard Mapping Layer
6. Audit / Assurance Workspace

Evidence generation is part of normal operations, not a later reporting add-on.

## 4. First-Class Internal Control Model

Material controls should be representable with at least:

- Control ID
- Business objective
- Risk
- Preventive / Detective / Corrective classification
- Owner
- Performer
- Approver
- Frequency / trigger
- Required evidence
- Exception handling
- Framework / standard mapping

A control is not complete merely because a log exists. The system must preserve the relationship between control design, control execution, business transaction, and resulting evidence.

## 5. Evidence Model

SMEsPlus must distinguish, where applicable:

### Business Event
Examples: InvoicePosted, GoodsReceived, PaymentApproved.

### Control Event
Examples: ApprovalPassed, SoDViolationBlocked, PeriodLockOverrideApproved.

### Audit Event
At minimum, where material:
- who
- did what
- when
- tenant
- company
- source/context
- previous value
- new value
- reason
- correlation/reference ID

Evidence must be traceable back to its originating transaction and control execution.

## 6. Evidence Provenance

Constitutional rule:

> NO PROVENANCE = NOT RELIABLE AUDIT EVIDENCE.

Critical evidence should preserve, where applicable:

- generator / actor
- tenant
- company
- source system/module
- transaction/object
- control
- timestamp
- version
- change history
- approval
- retention metadata
- export metadata

High-assurance evidence may additionally use cryptographic hash, signed manifests, append-only storage, immutable/object-lock mechanisms, legal hold, or equivalent controls. Exact technologies remain implementation candidates and are NOT frozen by this decision.

## 7. Authorization and Segregation of Duties

RBAC alone is insufficient for material ERP controls.

Approved direction:

`RBAC + Context/Attribute Control + Segregation of Duties + Approval Authority + Transaction Limit + Tenant/Company Context`

Examples include:

- creator cannot approve own transaction where SoD requires separation
- amount/authority thresholds
- independent verification of high-risk master-data changes
- explicit break-glass access
- full evidence of override/exception use

## 8. Financial Control Baseline

The following are treated as material audit-supporting Core capabilities where applicable:

- double-entry invariant
- period lock
- controlled reopen
- posting authorization
- sequential/controlled document numbering
- reversal/correction instead of destructive rewrite
- high-risk master-data change control
- reconciliation
- approval evidence
- immutable historical facts after finalization

## 9. Master Data Control

Master data should support risk classification, such as:

- Normal Master
- Controlled Master
- High-Risk Master

High-risk examples may include:

- vendor bank account
- customer credit limit
- chart of accounts
- tax configuration
- payment method
- approval matrix
- user privilege

High-risk changes may require:

- reason
- before/after values
- approval
- effective date
- maker/checker separation
- notification
- audit evidence

## 10. Quality / Traceability Capabilities

SMEsPlus should support reusable quality and traceability capabilities where relevant to the customer/industry, including:

- document control and revision
- approval / obsolete control
- non-conformance
- root cause analysis
- corrective action / improvement action
- inspection
- deviation / disposition
- lot / batch / serial traceability
- recall / genealogy

These capabilities are not mandatory in identical form for every industry or customer.

## 11. Information Security Evidence

SMEsPlus should be able to produce evidence for applicable controls such as:

- access review
- privilege changes
- authentication events
- failed access
- break-glass access
- security configuration
- backup execution
- restore tests
- incident history
- administrator activity
- export activity
- retention controls
- encryption configuration

## 12. Privacy / Data Governance

Where personal information is processed, architecture should support configurable governance for:

- data/PII classification
- purpose / legal-basis metadata where applicable
- consent metadata where applicable
- retention
- masking
- access
- disclosure/export
- deletion/anonymization workflow
- data-subject request evidence
- audit trail

Legal/regulatory mappings must remain versioned and separately governed because regulations may change.

## 13. Standard Mapping Architecture

A Control is NOT the same as a Standard clause.

Approved model:

`SMEsPlus Control -> Versioned Mapping Registry -> Standards / Frameworks / Regulations`

A single internal control may map to multiple external frameworks.

Framework mappings must be versioned and must not be permanently hard-coded into Core business logic.

## 14. Assurance & Evidence Center

Future product architecture should support an **Assurance & Evidence Center** or equivalent capability containing, as appropriate:

- Control Register
- Risk Register
- Evidence Register
- Control Test
- Exception Register
- CAPA / corrective action
- Access Review
- SoD Review
- Change History
- Financial / Period Controls
- Traceability Evidence
- Standard Mapping
- Audit Package Export

Audit-package export should be capable of preserving scope, control definition, population/evidence references, exceptions, approvals, configuration snapshot, generation timestamp, and manifest/integrity metadata where applicable.

## 15. Auditor Access

Auditor / assessor access must be controlled by:

- read-only by default
- time-bound where appropriate
- explicit scope
- tenant bound
- company bound
- evidence-only view where appropriate
- no transaction modification
- logged export/download
- fully audited access

## 16. Control Ownership

Every material SaaS control should classify ownership as:

1. **SMEsPlus Platform Control** — SMEsPlus operates the control.
2. **Customer Control** — customer defines/operates the control.
3. **Shared Control** — SMEsPlus provides/enforces the mechanism while the customer configures or operates part of the control.

Control ownership must be explicit to avoid false assurance and responsibility ambiguity.

## 17. Audit-Ready Constitution

AUD-01 — AUDITABILITY MUST BE DESIGNED, NOT RETROFITTED.  
AUD-02 — NO EVIDENCE WITHOUT PROVENANCE.  
AUD-03 — CRITICAL CONTROL EXECUTION MUST PRODUCE TRACEABLE EVIDENCE.  
AUD-04 — FINALIZED EVIDENCE MUST BE TAMPER-EVIDENT.  
AUD-05 — CONTROL != STANDARD; A CONTROL MAY MAP TO MANY STANDARDS.  
AUD-06 — STANDARD / FRAMEWORK MAPPINGS MUST BE VERSIONED.  
AUD-07 — AUDITOR ACCESS MUST BE READ-ONLY, SCOPED AND AUDITED.  
AUD-08 — CONTROL OWNERSHIP MUST BE EXPLICIT: PLATFORM / CUSTOMER / SHARED.  
AUD-09 — EVIDENCE MUST PRESERVE TENANT + COMPANY BOUNDARIES.  
AUD-10 — SMEPLUS SUPPORTS CERTIFICATION / ASSURANCE; SMEPLUS DOES NOT SELF-DECLARE CUSTOMER CERTIFICATION.

## 18. Integration with Existing Architecture Decisions

This approval is integrated with existing approved `SAAS-CELL-001` principles including:

- One Product / One Core Codebase
- Two deployment tiers
- Tenant isolation
- Company boundary
- Core–Extension Boundary
- Immutable historical facts
- transaction integrity
- financial integrity
- reconciliation
- no customer-specific Core fork
- evidence-first governance

Auditability and evidence generation must apply consistently across Standard and Enterprise tiers, while deployment/SLA/resource differences may vary.

## 19. Technology Freeze Status

This decision DOES NOT freeze specific technologies for:

- WORM storage
- object lock
- cryptographic signing
- hash algorithm
- audit database topology
- log platform
- SIEM platform
- e-signature provider
- standard-mapping engine
- evidence-export format

These remain evidence-driven implementation decisions.

## 20. Governance Effect

This Boss approval is now a controlled Architecture Baseline of `SMEPLUS-26-09-06-SAAS-CELL-001`.

Do not reopen this approved direction without a documented Material Delta or contradiction.

No Team C / production authorization is created by this approval.  
No database topology is frozen by this approval.  
Boss remains sole Final Approver.
