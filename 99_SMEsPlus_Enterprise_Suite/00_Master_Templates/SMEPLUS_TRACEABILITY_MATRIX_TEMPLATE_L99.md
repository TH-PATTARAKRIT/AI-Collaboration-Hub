# (split from combined source — see SOURCE_COMBINED_FILE_NOTE.md)

# SMEsPlus Traceability Matrix Template L99

| Field | Value |
| --- | --- |
| Document ID | SMEPLUS-TRC-L99-002 |
| Version | v2.0 |
| Status | READY FOR REVIEW |
| Gate Status | HOLD UNTIL FINAL REVIEW |
| Control Level | /L99 |
| Owner | PMO Evidence Controller |
| Reviewer | Enterprise Architect / Technical PMO Director |
| Approver | Boss / Final Gate Owner |
| Evidence Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Traceability | Requirement -> Evidence -> Gate Result |

## Traceability Rule

No Traceability = No Gate Pass
No Gate Approval = No Next State

## Traceability Chain

Functional Requirement
-> Business Rule
-> Business Process
-> Module / Function
-> Source / Learning Observation, if any
-> Data Object / Table / DTO
-> Screen / API
-> Jira Issue
-> AI Execution Reference
-> GitHub / Figma / CI / Test Evidence
-> UAT Case
-> Gate Result

## Matrix Template

| Trace ID | FR ID | Function | Module | BP ID | BR ID | Data Object / Table | Screen ID | API ID | Jira Key | AI Ref | GitHub / Figma / CI / Test Evidence | UAT Case | Owner | Reviewer | Gate Result | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRC-XX-XXX-001 | FR-XXX-001 | TBD | TBD | BP-XXX-001 | BR-XXX-001 | TBD | SCR-XXX-001 | API-XXX-001 | ERPPLUS-XXX | AI-XX-XXX-001 | EVD-XX-XXX-001 | UAT-XXX-001 | TBD | TBD | HOLD | Complete evidence |

## Status Values

| Status | Meaning |
| --- | --- |
| MATCHED | Requirement has sufficient evidence across required fields |
| PARTIAL | Some evidence exists but mapping is incomplete |
| GAP | Evidence or mapping not found |
| NEW | New requirement requiring design approval |
| RETIRE | Requirement should not continue |
| HOLD | Cannot move forward until missing trace is fixed |
