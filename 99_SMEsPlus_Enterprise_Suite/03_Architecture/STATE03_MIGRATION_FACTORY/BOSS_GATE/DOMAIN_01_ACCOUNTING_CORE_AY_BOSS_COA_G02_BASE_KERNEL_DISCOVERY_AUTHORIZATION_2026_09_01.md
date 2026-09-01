# DOMAIN_01 Accounting Core — Boss COA-G02 Base COA Kernel Discovery Authorization

Date: 2026-09-01
Project: SMEsPlus ENTERPRISE SUITE
Gate: `COA-G02 — Base COA Kernel Discovery`
Authority: Boss = Sole Final Approver

## Boss Directive

Following verified closure of `COA-G01 — Source Baseline Reconciliation`, Boss directed the project to **proceed with the next step**.

This directive is recorded as explicit authorization to open and execute:

`COA-G02 — Base COA Kernel Discovery`

## Authorized Objective

Identify the **smallest defensible Thailand Base COA Kernel** required by core accounting behaviour and Thailand-specific accounting/control semantics, using the evidence already reconciled and closed under COA-G01.

The working expectation of `~32` baseline accounts remains a **non-binding candidate range only**.

`Exact Base Kernel Count = TBD / EVIDENCE REQUIRED` until this Gate proves it.

## Mandatory Evidence Inputs

At minimum, COA-G02 shall use:

1. `COA_G01_BASE_KERNEL_CANDIDATE_INPUT.md`
2. `DOMAIN_01_COA_BASE_KERNEL_AND_AI_CONSOLIDATION_STANDARD.md`
3. `DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md`
4. `DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md`
5. Boss-approved Odoo18 workbook primary source
6. `l10n_th` source/template evidence already ported under COA-G01
7. Team A Accounting Core deep-research evidence
8. Boss Thai COA business rulings and SI-01..SI-10 controls

## Discovery Rule

Each proposed Base Kernel account must have:

- canonical business purpose;
- canonical Account Type;
- source evidence anchor;
- Thailand relevance;
- control/statutory reason for inclusion;
- explicit reason the business distinction cannot safely be represented only as a dimension, source attribute, or optional company extension.

## Prohibitions

COA-G02 must NOT:

- force exactly 32 accounts;
- copy 389 source rows as target accounts;
- freeze the final Standard Thai COA;
- perform COA-G03 row-by-row semantic consolidation beyond what is required to identify Kernel candidates;
- design or implement database schema/API/ORM;
- start Development or Production work;
- import vendor technical architecture.

## Gate Sequence

`COA-G01 = APPROVED / PASS / CLOSED`

`COA-G02 = OPEN / BOSS AUTHORIZED`

`COA-G03 and later = NOT AUTHORIZED by this ruling`

No Evidence = No Progress.
Never Skip Gate.
