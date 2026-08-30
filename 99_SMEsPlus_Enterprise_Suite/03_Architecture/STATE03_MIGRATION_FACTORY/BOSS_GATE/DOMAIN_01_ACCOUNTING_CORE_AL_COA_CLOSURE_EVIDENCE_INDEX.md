# DOMAIN_01 Thailand COA Closure — Evidence Index

Date: 2026-08-30
Jira: ERPPLUS-132
Boss Authorization Commit: `e8cc4d942d7f5c611ca3add0266c39196515b636`
Boss SaaS Architecture Amendment Commit: `c084a741b22e3352992fbeb0c212cbd1463efb92`
Boss Cross-Gate SaaS Invariants Ruling: `e16b29f35d8011723a6e2593994bc226870d9fd7`

## Current Gate

`COA CLOSURE WORKSTREAM = OPEN / AUTHORIZED BY BOSS`

Current execution Gate remains:

`COA-G01 — Source Baseline Reconciliation`

Execution has not yet been credited for later Gates merely because the workstream, COA-G04S amendment and Cross-Gate SaaS Invariants have been approved.

## Cross-Gate SaaS Invariant Control

**SI-01 through SI-10 apply to every COA Closure Gate: G01, G02, G03, G04, G04S, G05, G06, G07 and G08.**

1. `SI-01 Tenant context is mandatory.`
2. `SI-02 Company context is mandatory where company-scoped.`
3. `SI-03 Standard Template is not tenant-owned mutable data.`
4. `SI-04 Tenant customization cannot modify the published Standard Template.`
5. `SI-05 Account Code / Name is not canonical identity.`
6. `SI-06 Published Template Version is immutable.`
7. `SI-07 Upgrade is explicit, previewable and auditable.`
8. `SI-08 No cross-tenant COA access.`
9. `SI-09 Company customization must preserve canonical reporting semantics.`
10. `SI-10 SaaS Core must not hard-code Thailand-specific source architecture.`

Every Gate Report must include a `SAAS INVARIANT COMPLIANCE` matrix covering SI-01..SI-10 with evidence, owner, reviewer, status and Gate impact.

Enforcement:

- applicable SI violation -> `FAIL / FROZEN`;
- applicable SI evidence missing -> `HOLD`;
- `N/A` requires explicit justification;
- no Gate may be declared PASS/FROZEN/READY FOR HANDOFF/COMPLETE while an applicable SI is unresolved.

## Revised Gate Register

| Gate | Owner Role | Evidence | Reviewer | Status | Gate Impact |
|---|---|---|---|---|---|
| COA-G01 Source Baseline Reconciliation | Team A Evidence | TBD + SI-01..SI-10 compliance evidence required | ChatGPT | OPEN / NO EXECUTION CREDIT YET | Blocks G02 |
| COA-G02 Base COA Kernel Discovery | Team B Design after G01 evidence | TBD + SI-01..SI-10 compliance evidence required | ChatGPT | NOT STARTED | Blocks G03/G04 |
| COA-G03 AI Semantic Consolidation | Team B Design | TBD + SI-01..SI-10 compliance evidence required | ChatGPT | NOT STARTED | Blocks canonical freeze |
| COA-G04 Account Type & Account Group Architecture | Team B Design | Existing 19-type Boss ruling + new artifact TBD + SI compliance | ChatGPT | PARTIAL BASELINE / OPEN | Blocks G04S |
| **COA-G04S SaaS COA Tenancy, Provisioning, Versioning & Upgrade Architecture** | Team B SaaS/Accounting Architecture | Boss amendment `c084a741...` + execution artifact TBD + SI compliance | ChatGPT | **BOSS AUTHORIZED / NOT EXECUTED** | **Blocks G05 and later freeze** |
| COA-G05 Financial Statement Taxonomy | Team B Design | External statement example + mapping TBD + SI compliance | ChatGPT | OPEN | Blocks COA freeze |
| COA-G06 Thailand Tax Accounting Controls | Team A evidence + Team B design | TBD + SI compliance | ChatGPT | OPEN | Blocks COA freeze |
| COA-G07 Multi-company & Dimension Proof | Team B Design / Verification | TBD + SI compliance | ChatGPT | NOT STARTED | Blocks PMO |
| COA-G08 Independent Audit + PMO + Boss Freeze | ChatGPT -> PMO -> Boss | Full SI-01..SI-10 final compliance matrix required | Boss final | NOT OPEN | Final handoff gate |

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

## Audit Veto Control

The Cross-Gate ruling is a mandatory audit control, not a recommendation.

Any applicable SI violation or unresolved evidence gap prevents the affected Gate from receiving closure credit and prevents final COA handoff unless Boss separately issues a controlled exception ruling.

## Governance Red Flags

- Jira Assignee = UNASSIGNED.
- Due Date = TBD.
- Exact Base Kernel count = TBD / EVIDENCE REQUIRED.
- Exact final canonical COA count = TBD / EVIDENCE REQUIRED.
- COA-G01 SI-01..SI-10 compliance evidence = NOT YET VERIFIED.
- COA-G04S execution evidence = NOT YET AVAILABLE.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
