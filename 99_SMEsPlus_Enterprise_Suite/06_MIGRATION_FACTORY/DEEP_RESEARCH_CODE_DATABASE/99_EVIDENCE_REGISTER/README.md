# 99 — Evidence Register

This folder is the controlled evidence index for `[SMEPLUS-26-08-28-DEEP-CD-001]`.

## Mandatory Registers

1. `CODE_DEEP_RESEARCH_REGISTER.csv`
2. `DATABASE_DEEP_RESEARCH_REGISTER.csv`
3. `CODE_DB_MAPPING_REGISTER.csv`
4. `BUSINESS_SEMANTIC_REGISTER.csv`
5. `RESEARCH_EXCEPTION_REGISTER.csv`
6. `CLEAN_ROOM_CLASSIFICATION_REGISTER.csv`
7. `DEEP_RESEARCH_EVIDENCE_REGISTER.csv`
8. `SHA256_MANIFEST.csv`

## Verification Rule

A work item is not progress unless these fields are present and inspectable:

- Item / Research ID
- Owner
- Source artifact and source path
- Version or timestamp
- Evidence location
- Observation
- Reviewer / verifier
- Verification status
- Gate impact

Blank, inaccessible, ownerless, contradictory, or unlinked evidence is `HOLD` or `FAIL / FROZEN` according to criticality.

CSV registers are append-controlled. Raw evidence must never be overwritten.
