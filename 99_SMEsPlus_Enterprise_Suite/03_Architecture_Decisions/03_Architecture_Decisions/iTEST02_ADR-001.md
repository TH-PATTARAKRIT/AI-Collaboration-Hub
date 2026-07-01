# ADR-001: Isolated Restore Environment for iTEST02 Dump

**Status:** PROPOSED  
**Date:** 2026-07-02  
**Context:** iTEST02 PostgreSQL dump analysis  
**Owner:** TBD  
**Related folder:** `03_Architecture_Decisions`

## Context

The dump is a production-like ERP database export with broad module coverage and sensitive business data. Direct restore into shared or internet-connected environments would increase data leakage and operational risk.

## Decision

Restore must occur only in a segregated PostgreSQL environment with restricted access, no public endpoints, no uncontrolled extensions, and auditable restore logs.

## Consequences

### Positive

Enables safe validation, table counts, extension compatibility testing, and migration rehearsals.

### Negative / Risk

Adds setup effort and requires environment ownership before detailed row-level analysis.

## Evidence Required

- Restore command log
- PostgreSQL version and extension compatibility record
- Table count reconciliation
- Access control evidence
- Screenshot or terminal output of successful restore

## Gate Mapping

| Gate | Result | Reason |
|---|---|---|
| Functional design evidence | PASS | Based on extracted schema metadata |
| Technical validation | HOLD | Requires restore or owner review |
| Security / privacy | HOLD | Sensitive columns are present |
| Production readiness | HOLD | Not approved until validation completes |

## Next Action

Assign technical owner and perform first isolated restore rehearsal.
