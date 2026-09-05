# 05 — Exceptions and Gaps

Purpose: record every unresolved, contradictory, inaccessible, ambiguous, ownerless, or governance-sensitive research item.

## Exception Classes

- EVIDENCE_MISSING
- EVIDENCE_INACCESSIBLE
- LINEAGE_UNPROVEN
- VERSION_CONFLICT
- COUNT_RECONCILIATION_GAP
- SOURCE_DB_AMBIGUITY
- BUSINESS_MEANING_AMBIGUITY
- LICENSE_REVIEW_REQUIRED
- CLASS_D_QUARANTINE
- LEGAL_TAX_REVIEW_REQUIRED
- SECURITY_REVIEW_REQUIRED
- TARGET_DESIGN_DECISION_REQUIRED
- OUT_OF_SCOPE_CHANGE_CONTROL_REQUIRED

## Mandatory Fields

Every exception must include owner, evidence reference, timestamp, severity, verification status, gate impact, required resolution, and due date or TBD.

No unresolved exception may be silently converted into a verified fact or target-design decision.

All exceptions must be registered in `99_EVIDENCE_REGISTER/RESEARCH_EXCEPTION_REGISTER.csv`.
