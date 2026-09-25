# 06 — Clean-Room Control

Purpose: enforce legal, governance, architectural, and evidentiary separation between reference learning and independent SMEsPlus design.

## Five-Class Finding Boundary

| Class | Meaning | Transfer Rule |
|---|---|---|
| OBSERVED_FACT | Directly inspectable evidence | May be cited with evidence |
| INFERRED_BUSINESS_SEMANTIC | Interpretation derived from one or more facts | Requires rationale, confidence, and review |
| UNVERIFIED_ASSUMPTION | Plausible but unproven | Cannot become progress or design baseline |
| PROPRIETARY_IMPLEMENTATION | Framework/source-specific implementation detail | Quarantine; do not transfer |
| TARGET_DESIGN | Independently designed SMEsPlus specification | Requires semantic traceability and independent rationale |

## Clean-Room Decision Test

A finding may enter independent specification only when all answers are YES:

1. Is the underlying business fact evidenced?
2. Can the rule be expressed without source code, ORM, class, method, table, or workflow-engine dependence?
3. Is the rule a general business/accounting/inventory/manufacturing principle or an independently justified requirement?
4. Is any proprietary implementation detail excluded?
5. Is the target design independently named and structured?
6. Is source classification/license treatment recorded?
7. Has an independent reviewer verified the boundary?

Any NO result means `HOLD`, `QUARANTINED`, or `NEEDS_REVIEW`.

## Core Independence Rule

The Odoo adapter may understand Odoo. SMEsPlus Core must not depend on Odoo architecture.

All classifications must be recorded in `99_EVIDENCE_REGISTER/CLEAN_ROOM_CLASSIFICATION_REGISTER.csv`.
