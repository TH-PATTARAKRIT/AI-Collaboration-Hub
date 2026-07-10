# State 03 Canonical Governance Index

Session: [SMEPLUS-26-07-10-001]
Version: 2.0-draft
Status: APPROVED FOR CONTROLLED PREPARATION
Gate Status: HOLD
Approver: Boss
Independent Reviewer: ChatGPT L99
System of Record: GitHub branch `SMEsPlus` after approved merge

## 1. Source-of-Truth Hierarchy

1. Boss Approval Record
2. State 03 Canonical Governance Index
3. Architecture Scope and Gate Model
4. Canonical RACI and Named Owner Register
5. Architecture WBS and Deliverable Register
6. Domain Charters and Domain Architecture Documents
7. ADR, Evidence, Risk, Finding and Review Records
8. Historical and Superseded Documents

When two documents conflict, the higher active document in this hierarchy controls.

## 2. Canonical Governance Documents

| Document | Status | Purpose |
|---|---|---|
| STATE03_ARCHITECTURE_SCOPE_V2_APPROVAL_RECORD.md | APPROVED WITH CONDITIONS | Records Boss decision and limits |
| 00_STATE03_CANONICAL_GOVERNANCE_INDEX.md | CONTROLLED DRAFT | Defines source-of-truth hierarchy |
| STATE03_ARCHITECTURE_SCOPE_V2.md | APPROVED FOR CONTROLLED PREPARATION | Defines 24 domains and execution boundary |
| CANONICAL_ARCHITECTURE_RACI.md | CONTROLLED DRAFT | Defines role separation and decision authority |
| NAMED_OWNER_AND_REVIEWER_REGISTER.md | ACTIVE REGISTER | Records accountable assignments |
| ARCHITECTURE_GATE_MODEL_V2.md | CONTROLLED DRAFT | Defines Gate A-D mechanics |
| ARCHITECTURE_GATE_CROSSWALK_AND_SUPERSESSION.md | CONTROLLED DRAFT | Resolves old and new governance overlap |
| ARCHITECTURE_WBS_V2.md | ACTIVE REGISTER | Defines work packages for 24 domains |
| ARCHITECTURE_DELIVERABLE_REGISTER.md | ACTIVE REGISTER | Controls required deliverables |
| ARCHITECTURE_EVIDENCE_REGISTER_V2.md | ACTIVE REGISTER | Controls evidence and verification |
| TRUST_CONTROL_MATRIX.md | CONTROLLED DRAFT | Defines mandatory non-waivable controls |

## 3. Document Status Values

- ACTIVE
- APPROVED FOR CONTROLLED PREPARATION
- CONTROLLED DRAFT
- UNDER REVIEW
- HOLD
- SUPERSEDED
- HISTORICAL
- RETIRED

`APPROVED FOR CONTROLLED PREPARATION` does not mean Architecture Baseline approval.

## 4. Operating Boundary

Authorized:

- discovery
- current-state analysis
- target-state drafting
- option comparison
- domain charter and architecture document preparation
- ADR, risk, finding and evidence registration
- specialist and independent review

Not authorized:

- State 03 PASS
- Architecture Baseline declaration
- final technology lock
- feature build authorization
- merge approval for product implementation
- release, deployment or production use

## 5. Mandatory Control Rule

No GitHub path = No evidence.
No named owner = No accountability.
No reviewer = Not reviewed.
No acceptance criteria = Not verifiable.
No evidence = No progress.

## 6. Change Control

Changes to this index require:

1. corrective or change proposal
2. GitHub commit or Pull Request
3. independent review
4. Boss approval for authority, gate or supersession changes
5. change history update
