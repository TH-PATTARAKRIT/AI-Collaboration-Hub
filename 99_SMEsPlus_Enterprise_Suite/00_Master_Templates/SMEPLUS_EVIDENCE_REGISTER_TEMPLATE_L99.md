# (split from combined source — see SOURCE_COMBINED_FILE_NOTE.md)

# SMEsPlus Evidence Register Template L99

| Field | Value |
| --- | --- |
| Document ID | SMEPLUS-EVD-L99-002 |
| Version | v2.0 |
| Status | READY FOR REVIEW |
| Gate Status | HOLD UNTIL FINAL REVIEW |
| Control Level | /L99 |
| Owner | PMO Evidence Controller |
| Reviewer | Enterprise Architect / Technical PMO Director |
| Approver | Boss / Final Gate Owner |
| Evidence Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Traceability | Work Item -> Evidence -> Verification -> Gate Impact |

## Evidence Rule

A task, document, module, gate, or AI output cannot be counted as progress unless evidence is inspectable and tied to the work item.

## Evidence Register Template

| Evidence ID | State | Workstream | Module | Work Item | Claim | Evidence Type | Evidence Path / Link | Owner | Reviewer | Verifier | Timestamp | Verification Status | Gate Impact | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EVD-XX-XXX-DOC-YYYYMMDD-001 | STATE-XX | TBD | TBD | TBD | TBD | DOC | TBD | TBD | TBD | TBD | TBD | Pending | HOLD | Attach evidence |

## Evidence Decision Rules

| Condition | Decision |
| --- | --- |
| Evidence exists, accessible, timestamped, tied to item, reviewed | PASS candidate |
| Evidence exists but reviewer/traceability incomplete | HOLD |
| Evidence path blank or inaccessible | FAIL or FROZEN |
| Owner missing | FROZEN |
| Evidence contradicts claim | FAIL |
| Percentage claimed without evidence | HOLD / FAIL depending criticality |
| AI output without input and criteria | HOLD |
| Clean Room learning without adaptation evidence | FAIL / FROZEN |

## Evidence Type Standards

| Type | Acceptable Evidence |
| --- | --- |
| Document | Markdown, DOCX, PDF, approved record, meeting decision |
| Jira | Issue key, status, worklog, acceptance criteria, comments |
| GitHub | Branch, commit SHA, PR, review, Actions/Checks |
| Figma | File URL, page, frame, version, reviewer note |
| CI/Test | Run ID, result log, screenshot, test report |
| Infrastructure | VM spec, config export, monitoring, backup, restore test |
| AI | Prompt, input files, output, reviewer decision, guardrail checklist |
| Clean Room | Observation, generic concept, adaptation decision, reuse risk review |
