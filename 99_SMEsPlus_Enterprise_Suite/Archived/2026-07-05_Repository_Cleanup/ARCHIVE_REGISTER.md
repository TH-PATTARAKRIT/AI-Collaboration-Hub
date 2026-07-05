# ARCHIVE_REGISTER.md

Version: v1.0
Status: Approved for Execution / Pending Verification
Owner: SMEsPlus PMO / Executive Secretary AI
Scope: `99_SMEsPlus_Enterprise_Suite/Archived/2026-07-05_Repository_Cleanup/`
Created Date: 2026-07-05
Approved By: Boss

## Purpose

This register controls the repository cleanup work package approved by Boss. The approved approach is to move duplicate or non-authoritative artifacts into `Archived/` instead of deleting them.

## Archive Target Structure

```text
Archived/
└── 2026-07-05_Repository_Cleanup/
    ├── Duplicate_Folders/
    ├── Duplicate_Files/
    ├── Deprecated/
    └── Audit_Reference/
```

## Approved Archive Items

| ID | Source Path | Target Archive Path | Reason | Status |
|---|---|---|---|---|
| ARC-001 | `01_AI_Handoff/01_AI_Handoff/` | `Archived/2026-07-05_Repository_Cleanup/Duplicate_Folders/01_AI_Handoff/` | Self-nested duplicate folder | Approved / Pending move verification |
| ARC-002 | `03_Architecture_Decisions/03_Architecture_Decisions/` | `Archived/2026-07-05_Repository_Cleanup/Duplicate_Folders/03_Architecture_Decisions/` | Self-nested duplicate folder | Approved / Pending move verification |
| ARC-003 | `04_Review_Gates/04_Review_Gates/` | `Archived/2026-07-05_Repository_Cleanup/Duplicate_Folders/04_Review_Gates/` | Self-nested duplicate folder | Approved / Pending move verification |
| ARC-004 | `05_Prompts/05_Prompts/` | `Archived/2026-07-05_Repository_Cleanup/Duplicate_Folders/05_Prompts/` | Self-nested duplicate folder | Approved / Pending move verification |
| ARC-005 | `06_Templates/06_Templates/` | `Archived/2026-07-05_Repository_Cleanup/Duplicate_Folders/06_Templates/` | Self-nested duplicate folder | Approved / Pending move verification |
| ARC-006 | `08_Testing_Evidence/08_Testing_Evidence/` | `Archived/2026-07-05_Repository_Cleanup/Duplicate_Folders/08_Testing_Evidence/` | Self-nested duplicate folder | Approved / Pending move verification |
| ARC-007 | `09_Security_Clean_Room/09_Security_Clean_Room/` | `Archived/2026-07-05_Repository_Cleanup/Duplicate_Folders/09_Security_Clean_Room/` | Self-nested duplicate folder | Approved / Pending move verification |
| ARC-008 | `11_Diagrams/11_Diagrams/` | `Archived/2026-07-05_Repository_Cleanup/Duplicate_Folders/11_Diagrams/` | Self-nested duplicate folder | Approved / Pending move verification |
| ARC-009 | `12_Traceability/Requirement_Matrix/12_Traceability/Requirement_Matrix/` | `Archived/2026-07-05_Repository_Cleanup/Duplicate_Folders/12_Traceability_Requirement_Matrix/` | Self-nested duplicate folder | Approved / Pending move verification |
| ARC-010 | `02_Functional_Design/02_Functional_Design_v2/` | `Archived/2026-07-05_Repository_Cleanup/Duplicate_Folders/02_Functional_Design_v2/` | Exact duplicate tree | Approved / Pending move verification |
| ARC-011 | `00_Architecture_Office/SMEPLUS Architecture Office Workplan v0.1.pdf` | `Archived/2026-07-05_Repository_Cleanup/Duplicate_Files/SMEPLUS Architecture Office Workplan v0.1.root-copy.pdf` | Duplicate PDF | Approved / Pending move verification |

## Completion Criteria

1. Archive register lists every moved item.
2. Git commit evidence confirms each item was moved to `Archived/`.
3. Active repository scan confirms no duplicate or self-nested folders remain.
4. Decision log records the cleanup decision.
5. Root README and registry reflect active folders only.

## Current Work Package Status

```text
Repository Cleanup: APPROVED / IN PROGRESS
Archive Register: CREATED
Actual File Movement: PENDING VERIFICATION
Repository Structure Gate: AMBER
Build Gate: HOLD
Production Gate: HOLD
```
