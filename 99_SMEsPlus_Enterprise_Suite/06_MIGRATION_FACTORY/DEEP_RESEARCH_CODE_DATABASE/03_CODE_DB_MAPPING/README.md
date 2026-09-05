# 03 — Code ↔ Database Mapping

Purpose: reconcile source persistence expectations against actual database evidence without treating unmatched items as automatic defects.

## Required Mapping Chain

```text
Source Module
→ Source Model
→ Source Field
→ Persistence Expectation
→ Actual Table
→ Actual Column / Relation
→ Business Meaning
→ Mapping Status
→ Evidence
```

## Allowed Mapping Statuses

- VERIFIED_MATCH
- EXPECTED_NON_STORED
- RELATION_TABLE
- GENERATED_DERIVED
- SOURCE_ONLY
- DB_ONLY
- TABLE_NOT_FOUND
- COLUMN_NOT_FOUND
- AMBIGUOUS
- NEEDS_BUSINESS_REVIEW
- QUARANTINED

Every status must include evidence, confidence, reviewer, verification status, and gate impact.

All detailed mappings must be registered in `99_EVIDENCE_REGISTER/CODE_DB_MAPPING_REGISTER.csv`.
