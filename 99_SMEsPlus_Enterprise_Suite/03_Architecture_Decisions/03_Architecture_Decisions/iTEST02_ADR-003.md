# ADR-003: Mandatory Sensitive Data Masking Before Sharing

**Status:** PROPOSED  
**Date:** 2026-07-02  
**Context:** iTEST02 PostgreSQL dump analysis  
**Owner:** TBD  
**Related folder:** `03_Architecture_Decisions`

## Context

The schema includes many columns that indicate personal data, bank data, authentication data, tokens, employee data, and communication data. Sharing unmasked restored data would create privacy and security exposure.

## Decision

Any restored database, sample export, screenshot, or AI input must be masked or reduced to metadata unless explicit approval is recorded.

## Consequences

### Positive

Protects employees, customers, vendors, and company credentials while still allowing schema-level design work.

### Negative / Risk

May limit debugging of row-level data quality until a controlled masking process is ready.

## Evidence Required

- Sensitive column inventory
- Masking rule set
- Before and after masking evidence
- Approval record for any exception

## Gate Mapping

| Gate | Result | Reason |
|---|---|---|
| Functional design evidence | PASS | Based on extracted schema metadata |
| Technical validation | HOLD | Requires restore or owner review |
| Security / privacy | HOLD | Sensitive columns are present |
| Production readiness | HOLD | Not approved until validation completes |

## Next Action

Create masking rules per risk category and validate that no token or bank data is exposed.
