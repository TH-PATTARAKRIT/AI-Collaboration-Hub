# Architecture Gate Crosswalk and Supersession

Session: [SMEPLUS-26-07-10-001]
Version: 2.0-draft
Status: CONTROLLED DRAFT
Gate Status: HOLD

## Canonical Model

The canonical State 03 control model is Gate A-D as defined in `ARCHITECTURE_GATE_MODEL_V2.md` after approved merge.

## Crosswalk

| Previous Control | Canonical Mapping | Status |
|---|---|---|
| Architecture Scope / Design preparation | Gate A preparation | HISTORICAL INPUT |
| Architecture Review Gate / baseline review | Gate B | SUPERSEDED AFTER APPROVED MERGE |
| Build or Design Ready review | Gate C | SUPERSEDED AFTER APPROVED MERGE |
| Release / Deployment readiness review | Gate D | SUPERSEDED AFTER APPROVED MERGE |
| State 03 Acceleration 14 Work Packages | WBS V2 mapping | HISTORICAL / TO BE MAPPED |
| Architecture Domain Owner Matrix | Canonical RACI + Named Owner Register | SUPERSEDED AFTER APPROVED MERGE |
| Architecture Gate Model v1 | Architecture Gate Model V2 | SUPERSEDED AFTER APPROVED MERGE |

## System of Record

- Governance authority: `00_STATE03_CANONICAL_GOVERNANCE_INDEX.md`
- Roles and accountability: `CANONICAL_ARCHITECTURE_RACI.md`
- Gate mechanics: `ARCHITECTURE_GATE_MODEL_V2.md`
- Work control: `ARCHITECTURE_WBS_V2.md`
- Deliverable control: `ARCHITECTURE_DELIVERABLE_REGISTER.md`
- Evidence control: `ARCHITECTURE_EVIDENCE_REGISTER_V2.md`
- Trust controls: `TRUST_CONTROL_MATRIX.md`

## Conflict Rule

Where an older State 03 document conflicts with the canonical model, the canonical document controls only after:

1. controlled Pull Request review,
2. Boss approval record,
3. merge to `SMEsPlus`, and
4. canonical index update.

Before merge, all new documents remain controlled drafts and Gate A remains HOLD.

## Historical Preservation

Superseded documents must not be deleted. They must remain available with status `SUPERSEDED` or `HISTORICAL` for traceability.
