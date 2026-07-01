# ADR-002: Domain-Based ERD and Migration Slicing

**Status:** ACCEPTED  
**Date:** 2026-07-02  
**Context:** iTEST02 PostgreSQL dump analysis  
**Owner:** TBD  
**Related folder:** `03_Architecture_Decisions`

## Context

The full database contains 1,395 tables and 5,141 foreign keys. A single ERD is not useful for review and would obscure module accountability.

## Decision

Functional and migration design must be split by business domains such as Accounting, Inventory, Sales, HR, Manufacturing, Website, Projects, Documents, and AI Knowledge.

## Consequences

### Positive

Improves readability, ownership, prioritization, and test planning.

### Negative / Risk

Cross-module dependencies may be missed unless supported by a traceability matrix.

## Evidence Required

- Module inventory CSV
- Foreign key inventory CSV
- Domain ERD markdown files
- Cross-module dependency matrix

## Gate Mapping

| Gate | Result | Reason |
|---|---|---|
| Functional design evidence | PASS | Based on extracted schema metadata |
| Technical validation | PASS | Requires restore or owner review |
| Security / privacy | CONDITIONAL | Sensitive columns are present |
| Production readiness | CONDITIONAL | Not approved until validation completes |

## Next Action

Continue expanding ERD views by owner priority, beginning with Accounting, HR, Stock, and Sales.
