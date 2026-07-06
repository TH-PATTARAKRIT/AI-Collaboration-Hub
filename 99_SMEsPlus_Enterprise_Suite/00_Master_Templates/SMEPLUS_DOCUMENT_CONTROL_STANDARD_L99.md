# (split from combined source — see SOURCE_COMBINED_FILE_NOTE.md)

# SMEsPlus Document Control Standard L99

| Field | Value |
| --- | --- |
| Document ID | SMEPLUS-DOCCTRL-L99-002 |
| Version | v2.0 |
| Status | READY FOR REVIEW |
| Gate Status | HOLD UNTIL FINAL REVIEW |
| Control Level | /L99 |
| Owner | PMO Evidence Controller |
| Reviewer | Enterprise Architect / Technical PMO Director |
| Approver | Boss / Final Gate Owner |
| Evidence Path | 99\_SMEsPlus\_Enterprise\_Suite/00\_Master\_Templates/ |
| Traceability | Document -> Version -> Review -> Approval -> Evidence -> Gate Result |

## Document Control Principle

A SMEsPlus document is not a controlled artifact unless it has document ID, version, status, owner, reviewer, approver, evidence path, change log, and gate status.

## Document Status Values

| Status | Meaning | Gate Rule |
| --- | --- | --- |
| DRAFT | Working draft | Not usable for approval |
| READY FOR REVIEW | Prepared and awaiting reviewer | HOLD |
| IN REVIEW | Reviewer is checking | HOLD |
| APPROVED | Approved by authorized approver | PASS for approved scope only |
| SUPERSEDED | Replaced by newer version | Do not use for new work |
| ARCHIVED | Retained for history | Read-only |

## Versioning Rule

| Version | Use Case |
| --- | --- |
| v0.1 | Initial draft |
| v0.2 | Draft correction |
| v1.0 | First approved baseline |
| v1.1 | Minor clarification |
| v2.0 | Major structural upgrade |

## File Naming Rule

SMEPLUS-{STATE}-{DOMAIN}-{DOCUMENT\_TYPE}-{SEQUENCE}\_L99\_v{VERSION}.md

For master templates:

SMEPLUS\_{DOCUMENT\_NAME}\_L99\_v{VERSION}.md

## Change Log Template

| Version | Date | Change Summary | Owner | Reviewer | Approver | Gate Impact |
| --- | --- | --- | --- | --- | --- | --- |
| vX.Y | YYYY-MM-DD | TBD | TBD | TBD | TBD | HOLD |

## Control Breach Result

| Control Breach | Gate Result |
| --- | --- |
| Missing owner | FROZEN |
| Missing reviewer | HOLD / FROZEN |
| Missing approver for approval claim | FAIL |
| Missing evidence path | HOLD / FAIL |
| Approved document overwritten without version | FAIL |
| AI-generated document with no review | HOLD |
| Production use without approved status | FROZEN |
