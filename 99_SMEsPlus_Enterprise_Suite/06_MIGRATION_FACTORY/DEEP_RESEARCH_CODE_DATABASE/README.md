# SMEsPlus Deep Research — Code + Database

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`

Status: `AUTHORIZED / IN EXECUTION / FINAL GATE NOT REACHED`

Branch: `feature/SMEPLUS-DEEP-CD-001-cleanroom-research`

Final Approver: Boss only

## Purpose

This workspace contains controlled forensic learning, business-semantic extraction, source-to-database reconciliation, clean-room controls, vendor-neutral functional specifications, and the final evidence gate pack for SMEsPlus Enterprise Suite.

SMEsPlus is a new 100% clean-room Node.js SaaS ERP. Odoo, Salesforce, SAP Business One, legacy applications, source archives, and database dumps are reference and learning materials only.

The governing transformation is:

```text
Observed Source Fact
→ Business Semantic
→ Domain Invariant / Mathematical Rule
→ Vendor-Neutral Functional Specification
→ Independent SMEsPlus Target Design
```

The following transformation is prohibited:

```text
Odoo ORM / class / method / schema
→ direct SMEsPlus class / method / schema / workflow clone
```

## Authorized Inputs

1. `01_ACCOUNT(1).zip`
2. `02_OTHER(1).zip`
3. `addons_extra(1).zip`
4. Existing historical source, dump, mapping, governance, and evidence packs that can be revalidated

Historical PASS or closure is not inherited automatically. Every reused evidence item must be revalidated for accessibility, lineage, timestamp, scope, version, and consistency with the current source baseline.

## Execution Phases

| Phase | Name | Gate Rule |
|---|---|---|
| DR0 | Governance & Evidence Baseline | Must pass before DR1 |
| DR1 | Current Source Inventory Reconciliation | Must establish current denominator and lineage |
| DR2 | Source Code Deep Research | CLASS-D remains quarantined |
| DR3 | Database Deep Research | Independent from source-code assumptions |
| DR4 | Code ↔ DB Mapping Reconciliation | Unmatched does not automatically mean defect |
| DR5 | Business Semantic Extraction | Separate observed fact from inference |
| DR6 | Gap & Exception Classification | Every exception has owner and gate impact |
| DR7 | Clean-Room Independent Review | No proprietary implementation transfer |
| DR8 | Evidence Gate | Inspectable evidence required |
| DR9 | Boss Final Gate | Boss is sole final approver |

## Folder Structure

```text
DEEP_RESEARCH_CODE_DATABASE/
├── 00_GOVERNANCE/
├── 01_SOURCE_CODE_RESEARCH/
├── 02_DATABASE_RESEARCH/
├── 03_CODE_DB_MAPPING/
├── 04_BUSINESS_SEMANTICS/
├── 05_EXCEPTION_GAPS/
├── 06_CLEAN_ROOM_CONTROL/
├── 07_RESEARCH_SUMMARY/
├── 08_FINAL_GATE_PACK/
└── 99_EVIDENCE_REGISTER/
```

## Mandatory Controls

- No Evidence = No Progress
- Never Skip Gate
- Boss = Sole Final Approver
- No source-code copy, clone, conversion, or implementation reuse
- No Odoo ORM, schema, workflow-engine, or proprietary algorithm dependency in SMEsPlus Core
- CLASS-C: behavioral / semantic learning only
- CLASS-D: quarantined until explicit Boss authorization
- No implementation, merge, release, deployment, or production migration in this session
- No BOARD / STATE / STEP percentage without an approved denominator and weighting baseline

## Final Deliverable

`08_FINAL_GATE_PACK/DEEP_RESEARCH_CODE_DATABASE_FINAL_REPORT.md`

Allowed recommendations:

- PASS
- PASS WITH CONTROL
- HOLD
- FAIL / RETURN

Only Boss may issue the final decision.
