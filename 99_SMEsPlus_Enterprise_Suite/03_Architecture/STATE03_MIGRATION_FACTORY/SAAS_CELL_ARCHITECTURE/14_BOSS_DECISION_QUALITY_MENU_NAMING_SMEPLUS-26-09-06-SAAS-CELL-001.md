# 14 — BOSS DECISION: QUALITY MENU NAMING

Session: `[SMEPLUS-26-09-06-SAAS-CELL-001]`
Jira: `ERPPLUS-151`
Status: BOSS APPROVED DIRECTION / DETAIL DESIGN PENDING

## Boss Decision

Boss approved the next First Image menu naming direction:

- Canonical English / Default UI: `Quality`
- Thai controlled localization: `คุณภาพ`

## Scope Intent

`Quality` is the top-level user-facing business capability label and is intentionally broader than `Quality Control`.

Candidate capability coverage includes:
- Inspections
- Quality Plans
- Nonconformance / NCR
- Corrective Actions / CAPA
- Quality Certificates
- Quality Reports

## Cross-Module Relationship

Quality must remain traceable to source business facts across Purchase, Inventory, Manufacturing and Sales/Delivery.

Examples:
- Purchase Receipt -> Incoming Inspection -> Accept / Hold / Reject -> Inventory
- Manufacturing -> In-Process / Final Inspection -> Pass / Hold / Rework / Scrap -> Inventory
- Finished Goods -> Final Quality Result -> Delivery -> Customer / Certificate

Reporting rule:

`Different Reports, Same Business Facts.`

Inspection results must be traceable to their originating receipt, lot/serial, manufacturing order, delivery, product and company/tenant context as applicable.

## Authorization

Menu grouping does not weaken role boundaries. Inspector, Quality Manager, Warehouse and Production permissions remain independently controllable.

## Governance

- English remains Canonical Product Language and Default UI.
- Thai remains controlled semantic localization.
- No Evidence = No Progress.
- Boss remains sole Final Approver.
- This decision does not authorize Team C implementation or production deployment.
