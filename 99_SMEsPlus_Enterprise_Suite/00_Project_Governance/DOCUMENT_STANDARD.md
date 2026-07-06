# DOCUMENT_STANDARD.md

Version: v1.0
Status: Approved
Owner: SMEsPlus PMO / Repository Owner
Approved By: Boss
Effective Date: 2026-07-05
Scope: `99_SMEsPlus_Enterprise_Suite/`

## Purpose

Define document naming, ownership, status and evidence standards for SMEsPlus Enterprise Suite.

## Required Metadata

Every controlled document must include:

- Version
- Status
- Owner
- Scope
- Reviewer / Approver when applicable
- Related documents
- Change history when applicable

## Naming Standard

Use clear names, preferably `UPPER_SNAKE_CASE` for governance and controlled artifacts.

Examples:

```text
FUNCTIONAL_SPECIFICATION_STANDARD.md
TRACEABILITY_STANDARD.md
QUALITY_GATE_STANDARD.md
```

## Status Values

```text
Draft
In Review
Approved
Accepted with Control
HOLD
Archived
Retired
```

## Source of Truth Rule

If a working artifact conflicts with a controlled standard, the controlled standard wins.

## Archive Rule

Deprecated or duplicate items must be moved to `Archived/` when evidence preservation is required.
