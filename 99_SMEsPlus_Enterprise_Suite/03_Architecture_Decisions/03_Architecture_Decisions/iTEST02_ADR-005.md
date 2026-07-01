# ADR-005: Evidence-First Repository Promotion

**Status:** ACCEPTED  
**Date:** 2026-07-02  
**Context:** iTEST02 PostgreSQL dump analysis  
**Owner:** TBD  
**Related folder:** `03_Architecture_Decisions`

## Context

The project follows an evidence-based delivery model. Documentation can be committed as draft evidence, but implementation claims must be backed by logs, screenshots, scripts, or owner signoff.

## Decision

All generated analysis files must be committed with explicit status labels such as DRAFT, PASS, HOLD, FAIL, or FROZEN. No implementation progress should be claimed without evidence.

## Consequences

### Positive

Creates auditability and prevents false progress reporting.

### Negative / Risk

Requires discipline and may slow informal updates.

## Evidence Required

- Commit hash
- File manifest
- Evidence gate report
- Owner approvals where applicable

## Gate Mapping

| Gate | Result | Reason |
|---|---|---|
| Functional design evidence | PASS | Based on extracted schema metadata |
| Technical validation | PASS | Requires restore or owner review |
| Security / privacy | PASS | Sensitive columns are present |
| Production readiness | CONDITIONAL | Not approved until validation completes |

## Next Action

Commit the generated design and decision files with a clear draft status.
