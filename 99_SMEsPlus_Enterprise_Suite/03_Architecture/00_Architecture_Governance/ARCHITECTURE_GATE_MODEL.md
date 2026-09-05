# State 03 Architecture Gate Model

Session: [SMEPLUS-26-07-10-001]
Control Level: /L99.99
Status: CONTROLLED DRAFT
Final Approval Authority: Boss
Independent Reviewer: ChatGPT L99

## Prompt Governance Constitution Adoption

Effective immediately for all new STATE03 prompts: apply **SMEsPlus Prompt Governance Constitution v1.0**, Base Prompt Standard and **Profile A — Logic Analysis & Architecture**.

- Every prompt must declare a valid Session ID, Step ID, Prompt ID (`STEPxxyyzz`), execution mode, included/excluded scope, evidence baseline, acceptance criteria, and Required Final Report.
- Architecture analysis may derive only abstract business rules, workflows, data models, indexes, and API boundaries from verified requirements and permitted evidence.
- No final execution code is authorized by Profile A.
- Clean Room 100%, No Evidence = No Progress, role separation, and Boss-as-Sole-Final-Approver apply.
- This adoption does not pass any Architecture Gate, authorize build, merge, release, deployment, or production change.

Reference: `00_Project_Governance/SMEPLUS_PROMPT_GOVERNANCE_CONSTITUTION_v1.0.md`; Jira ERPPLUS-96; Draft PR #36.

**Profile E applies:** STATE03 Architecture prompts require `HIGH_REASONING`. Record the exact Model when known; otherwise record `MODEL_NOT_DISCLOSED`, Platform, Agent Type, Tooling Context, execution date, and evidence. A model/capability downgrade must be reported before work continues.

**Prompt Lineage applies:** Any STATE03 prompt that uses prior architecture work must declare Parent Prompt ID, Reference Prompt IDs, Reference Type, exact evidence baseline, and Previous State Snapshot. A closed prompt is Historical Evidence, not automatically-current status.

## Gate A — Scope Baseline

Required:

- product boundary
- business capability map
- architecture domain list
- AI Owner and reviewer for every domain
- architecture deliverable list
- initial risk and dependency register
- architecture principles

Allowed result: PASS / HOLD / FAIL

Gate A does not authorize feature build.

## Gate B — Architecture Baseline

Required:

- system context and solution boundary
- application and module boundary
- tenant model and isolation strategy
- identity and access model
- data ownership and database strategy
- API, integration and event strategy
- security and privacy baseline
- measurable non-functional requirements
- infrastructure target architecture
- critical ADR records

Automatic HOLD conditions:

- tenant isolation is unclear
- identity and access scope is unclear
- data ownership is unclear
- critical risks have no owner
- evidence links are missing

## Gate C — Build Ready

Required:

- reviewed module architecture
- API and event contracts
- database and ORM mapping
- permission and data-scope matrix
- threat model for critical flows
- deployment pipeline design
- observability requirements
- measurable acceptance criteria
- test and evidence plan
- unresolved decisions classified and controlled

Gate C must not pass from document presence alone. Review evidence and traceability are mandatory.

## Gate D — Release Ready

Required evidence:

- security test result
- performance and capacity test result
- tenant isolation test result
- backup restore test result
- disaster recovery exercise result at the required level
- monitoring and alert test result
- rollback test result
- release approval record
- known-risk acceptance record
- deployment and artifact record

## Common Evidence Fields

Every gate item must record:

- item name
- AI Owner
- GitHub evidence location
- commit SHA or artifact hash
- timestamp
- reviewer
- verification result
- gate impact

## Gate Authority

AI Owners and Claude AI may prepare evidence but may not approve a gate.

ChatGPT L99 performs independent review and issues a recommendation.

Boss makes the final gate decision.

No Evidence = No Progress.
