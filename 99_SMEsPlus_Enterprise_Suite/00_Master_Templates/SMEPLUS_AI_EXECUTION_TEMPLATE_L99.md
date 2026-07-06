# (split from combined source — see SOURCE_COMBINED_FILE_NOTE.md)

# SMEsPlus AI Execution Template L99

| Field | Value |
| --- | --- |
| Document ID | SMEPLUS-AI-L99-002 |
| Version | v2.0 |
| Status | READY FOR REVIEW |
| Gate Status | HOLD UNTIL FINAL REVIEW |
| Control Level | /L99 |
| Owner | PMO Evidence Controller |
| Reviewer | Enterprise Architect / Technical PMO Director |
| Approver | Boss / Final Gate Owner |
| Evidence Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Traceability | AI Prompt -> Input -> Output -> Review -> Evidence -> Gate Result |

## AI Execution Boundary

AI is allowed to assist with analysis, drafting, mapping, evidence register preparation, prompt preparation, and review support. AI must not approve its own output or convert a claim into progress without evidence.

## AI Work Package Header

| Field | Value |
| --- | --- |
| AI Execution ID | AI-XX-XXX-001 |
| AI Tool / Agent | ChatGPT / Claude / Copilot / Make / OpenAI API / Other |
| Workstream | TBD |
| State | STATE-XX |
| Module | TBD |
| Input Source | TBD |
| Prompt File | TBD |
| Expected Output | TBD |
| Acceptance Criteria | TBD |
| Owner | TBD |
| Reviewer | TBD |
| Approver | TBD |
| Evidence Path | TBD |
| Gate Status | HOLD |

## AI Allowed / Not Allowed Matrix

| Activity | Allowed Status | Gate Rule |
| --- | --- | --- |
| Summarize supplied notes | Allowed | Review required |
| Create Markdown template | Allowed | Review required |
| Create evidence register | Allowed | Verification required |
| Map requirement to process | Allowed | BA/SA review required |
| Analyze source/dump for learning | Allowed with Clean Room | No code, no direct reuse |
| Generate production code | HOLD | Requires Build Ready + AI Coding Ready |
| Generate migration script | HOLD | Requires Data/Migration Gate PASS |
| Merge PR | Not allowed | Human/Gate owner only |
| Release to production | Not allowed | Production Gate only |
| Approve own output | Not allowed | Independent review required |

## Prompt Control Template

Project: SMEsPlus Enterprise Suite
Control Level: /L99
Rule: No Evidence = No Progress
Task ID: AI-XX-XXX-001
State: STATE-XX
Module: TBD
Input Evidence: TBD
Allowed Output: TBD
Not Allowed: Do not invent requirements, endpoints, database schema, permissions, business rules, approval logic, posting logic, or production actions.
Review Required: Yes
Gate Status After Output: HOLD UNTIL REVIEW
