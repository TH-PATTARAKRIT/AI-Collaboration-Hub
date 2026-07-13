# SMEsPlus Enterprise Suite

**Project ID:** SMEPLUS-ENTERPRISE-001  
**Branch:** `SMEsPlus`  
**Primary Path:** `99_SMEsPlus_Enterprise_Suite/`  
**Project Target Milestone:** **31 October 2026**  
**State 01:** **CLOSED — PASS WITH CONTROL**  
**Final Approval Authority:** Boss  
**AI PMO:** Support Only; not an Accountable Owner

## Product Direction

SMEsPlus Enterprise Suite is an Odoo-first, enterprise-controlled SaaS ERP platform for Thai SMEs and enterprise-lite organizations.

Core principles:

- UI/UX = Simple + Odoo-first
- Control = SMEsPlus / Enterprise-first
- Approval Engine approves only
- Source Module executes
- Posting Engine posts
- Events are immutable facts
- Clean Room 100%
- No Evidence = No Progress
- No Gate skipping
- AI cannot self-approve

## Source of Truth

- **GitHub:** controlled published baseline, version control, approvals, and gate evidence
- **Google Drive:** collaboration and working-document area
- A working document does not replace the GitHub-controlled baseline until reviewed and published.

## Current Top-Level Structure

```text
99_SMEsPlus_Enterprise_Suite/
├── 00_Architecture_Office/
├── 00_Master_Templates/
├── 00_Project_Governance/
├── 01_AI_Handoff/
├── 01_SaaS_Foundation/
├── 02_Functional_Design/
├── 03_Architecture/
├── 03_Architecture_Decisions/
├── 04_Review_Gates/
├── 05_Prompts/
├── 06_Templates/
├── 07_Output_From_AI/
├── 08_Testing_Evidence/
├── 09_Security_Clean_Room/
├── 11_Diagrams/
├── 12_State_AI_Execution_Control/
├── 12_Traceability/
├── 13_Jira_Control/
├── 14_Claude_Execution/
├── 15_ChatGPT_Review/
├── 16_Learning_Analysis/
├── 17_Functional_Specification_Factory/
└── V2.0/
```

This list is the controlled high-level map. Subfolders remain governed by their local README and registry records.

## State 01 Controlled Baseline

Path: `00_Project_Governance/State_01_Project_Identity/`

1. `STATE01_PROJECT_CHARTER_v1.0.md`
2. `STATE01_SCOPE_PRINCIPLES_RACI_v1.0.md`
3. `STATE01_SOURCE_OF_TRUTH_POLICY_v1.0.md`
4. `STATE01_EVIDENCE_REGISTER.md`
5. `STATE01_GATE_REVIEW_AND_BOSS_APPROVAL_RECORD.md`
6. `STATE01_CLOSURE_CONFIRMATION.md`

## Authority and Workflow

1. Specialist or assigned AI creates a deliverable with evidence.
2. Executive Secretary coordinates execution and verifies completeness.
3. Assigned reviewer checks quality and traceability.
4. Boss makes the final non-delegable approval decision.
5. AI PMO may support drafting, checklists, evidence preparation, and reporting only.

Every controlled deliverable requires:

- Task or document ID
- Accountable Owner
- Evidence location
- Timestamp
- Reviewer
- Verification status
- Gate impact

## Current Gate Position

- State 01 Project Identity: **CLOSED — PASS WITH CONTROL**
- State 02 Governance: **IN PROGRESS / HOLD until canonical baseline approval**
- State 03 Architecture: **IN PROGRESS / Gate A HOLD**
- State 04 Functional Design: **CONTINUE IN PARALLEL**
- Feature Build, Merge, Release, Deployment, and Production: **HOLD until respective gates pass**

## Repository Status

| Component | Status |
|---|---|
| Project identity baseline | Approved and closed |
| Governance documents | Available; consolidation in progress |
| Registry files | Available; reconciled for State 01 |
| Templates | Available |
| Functional deliverables | In progress |
| Learning and database evidence | Available as working evidence baseline |
| Build readiness | HOLD |
| Production readiness | HOLD |

**Last Updated:** 2026-07-13  
**Updated By:** Executive Secretary under Boss authorization
