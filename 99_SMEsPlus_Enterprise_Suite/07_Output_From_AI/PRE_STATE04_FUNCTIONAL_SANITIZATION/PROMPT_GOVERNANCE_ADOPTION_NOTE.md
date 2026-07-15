# PRE-STATE04 Prompt Governance Adoption Note

Status: CONTROLLED ADOPTION NOTE — does not formally start STEP0401  
Authority: Boss Directive — SMEsPlus Prompt Governance Constitution v1.0  
Reference: Jira ERPPLUS-96; Draft PR #36  
Scope: PRE-STATE04 Functional Sanitization and the future STATE04 Functional Design stream.

## Current Position

- STEP0401 is NOT formally started.
- Current activity is PRE-STATE04 Batch 0 Independent Review.
- This note does not close Batch 0, approve a gate, authorize Batch 1, merge PR #35, or authorize Build, Release, Deploy, or Production.

## Applicable Prompt Profile

### Current PRE-STATE04 Independent Review

Use the Base Prompt Standard with:

- Execution Mode: READ-ONLY REVIEW
- Role separation: reviewer is separate from the Batch 0 preparer
- Required Final Report and YAML Result Manifest
- Clean Room/IP Protection requirements

### When STEP0401 Formally Starts

Use **Profile B — Functional Design**:

- map verified requirements to functional components
- perform Fit-Gap analysis under Open ERP-first principles
- create BPMN, Functional Requirements, Acceptance Criteria, and traceability
- define tenant-isolation requirements where applicable

### Future UI Work

Use **Profile D — Frontend/UI** only in STATE05, after FDS and API Contract readiness. Figma Design Authority, approved Design Tokens, and approved Mock API/API Contracts are mandatory.

## AI Model & Capability Control

Profile E applies to the current PRE-STATE04 Independent Review and future STATE04 work. Independent Review requires `HIGH_REASONING`; record the Model when known, otherwise use `MODEL_NOT_DISCLOSED` with complete Platform, Agent Type, Capability Tier, Tooling Context, execution date, and evidence output. No silent downgrade is permitted.

## Mandatory Restrictions

- Learn only permitted abstract business behavior, business rules, data concepts, and process controls.
- Do not copy, port, translate, reproduce, or structurally imitate third-party implementation.
- Do not connect to Production APIs.
- Do not bypass Approval, Posting, or Audit controls.
- Boss is the Sole Final Approver.

No Evidence = No Progress. Clean Room 100%.
