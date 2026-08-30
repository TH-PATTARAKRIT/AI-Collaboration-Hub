# DOMAIN_01 Thailand COA Closure — Evidence Index

Date: 2026-08-30
Jira: ERPPLUS-132
Boss Authorization Commit: `e8cc4d942d7f5c611ca3add0266c39196515b636`
Boss SaaS Architecture Amendment Commit: `c084a741b22e3352992fbeb0c212cbd1463efb92`

## Current Gate

`COA CLOSURE WORKSTREAM = OPEN / AUTHORIZED BY BOSS`

Current execution Gate remains:

`COA-G01 — Source Baseline Reconciliation`

Execution has not yet been credited for later Gates merely because the workstream and COA-G04S amendment have been approved.

## Revised Gate Register

| Gate | Owner Role | Evidence | Reviewer | Status | Gate Impact |
|---|---|---|---|---|---|
| COA-G01 Source Baseline Reconciliation | Team A Evidence | TBD | ChatGPT | OPEN / NO EXECUTION CREDIT YET | Blocks G02 |
| COA-G02 Base COA Kernel Discovery | Team B Design after G01 evidence | TBD | ChatGPT | NOT STARTED | Blocks G03/G04 |
| COA-G03 AI Semantic Consolidation | Team B Design | TBD | ChatGPT | NOT STARTED | Blocks canonical freeze |
| COA-G04 Account Type & Account Group Architecture | Team B Design | Existing 19-type Boss ruling + new artifact TBD | ChatGPT | PARTIAL BASELINE / OPEN | Blocks G04S |
| **COA-G04S SaaS COA Tenancy, Provisioning, Versioning & Upgrade Architecture** | Team B SaaS/Accounting Architecture | Boss amendment `c084a741...` + execution artifact TBD | ChatGPT | **BOSS AUTHORIZED / NOT EXECUTED** | **Blocks G05 and later freeze** |
| COA-G05 Financial Statement Taxonomy | Team B Design | External statement example + mapping TBD | ChatGPT | OPEN | Blocks COA freeze |
| COA-G06 Thailand Tax Accounting Controls | Team A evidence + Team B design | TBD | ChatGPT | OPEN | Blocks COA freeze |
| COA-G07 Multi-company & Dimension Proof | Team B Design / Verification | TBD | ChatGPT | NOT STARTED | Blocks PMO |
| COA-G08 Independent Audit + PMO + Boss Freeze | ChatGPT -> PMO -> Boss | TBD | Boss final | NOT OPEN | Final handoff gate |

## COA-G04S Mandatory Evidence Scope

Before G05 can be opened for closure credit, G04S must evidence:

- Tenant isolation
- Company isolation
- Standard Thai COA Template vs Company COA Instance separation
- Tenant/Company provisioning
- Template versioning
- Tenant customization boundary
- Controlled upgrade / delta handling
- Backward compatibility
- Canonical identity independent from Account Code
- Company-maintainable Account Group behaviour
- Multi-company sharing/separation rules
- Role/permission boundary
- Audit/change history
- Migration mapping compatibility
- Canonical reporting continuity after customization/upgrade

## Governance Red Flags

- Jira Assignee = UNASSIGNED.
- Due Date = TBD.
- Exact Base Kernel count = TBD / EVIDENCE REQUIRED.
- Exact final canonical COA count = TBD / EVIDENCE REQUIRED.
- COA-G04S execution evidence = NOT YET AVAILABLE.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
