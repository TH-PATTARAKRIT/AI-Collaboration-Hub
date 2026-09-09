# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G0 — Parent Evidence Register

Status: G0 EVIDENCE REGISTER — ACTIVE
Owner: SaaS Team under SMEs Core
Final Approver: Boss only
Build / Merge / Production: HOLD

## Purpose
This register establishes the authoritative parent evidence baseline for Core Resource Governance. It is a continuation of `[SMEPLUS-26-09-06-SAAS-CELL-001]` and must not redesign from memory.

## Parent Evidence Population

| Ref | Evidence | SHA | Carry-Forward Relevance |
|---|---|---|---|
| P-01 | `01_NEW_SESSION_PROMPT_SMEPLUS-26-09-06-SAAS-CELL-001.md` | `3878572ca45fc8f82626cbc7da3fdfa5d262ec8d` | Two-tier SaaS baseline, Tenant/Company semantics, one Core/many Cells, Cell capacity envelope, Standard→Enterprise mobility |
| P-22 | `22_BOSS_DECISION_USAGE_BASED_CAPACITY_AND_TRANSPARENT_BILLING_SMEPLUS-26-09-06-SAAS-CELL-001.md` | `8ce2e1958df2157ce4e9f2a89763541b268ff87d` | Included capacity, measurable usage, no surprise billing, no evidence = no chargeable overage |
| P-23 | `23_BOSS_DECISION_CUSTOMER_USAGE_VISIBILITY_AND_PROJECTED_MONTHLY_COST_SMEPLUS-26-09-06-SAAS-CELL-001.md` | `7b41f9defdccb2aa3b808863db32b634d1184d3f` | Customer usage visibility, projected cost, two-dashboard model |
| P-24 | `24_BOSS_DECISION_WALLET_PROTECTION_AND_ADVANCE_NOTIFICATION_SMEPLUS-26-09-06-SAAS-CELL-001.md` | `c8ded81dd37cc5c146a7e1c04edb0f54615722fe` | Prepaid wallet, runway forecast, notification states |
| P-25 | `25_BOSS_DECISION_30_DAY_ADVANCE_WALLET_DEPLETION_NOTICE_SMEPLUS-26-09-06-SAAS-CELL-001.md` | `08f5df935ca696d91388b6706f871c69d5783a64` | 30-day forecast-based depletion notice |
| P-26 | `26_BOSS_DECISION_PREPAID_BEFORE_USAGE_30_DAY_NOTICE_IS_NOT_CREDIT_SMEPLUS-26-09-06-SAAS-CELL-001.md` | `4b3fd233cd09bb80edaa1b5a8428b7c8ea61e07d` | Prepaid before usage, no unsecured postpaid, pre-execution entitlement/capacity check |
| P-27 | `27_BOSS_DIRECTION_LOW_BASE_SUBSCRIPTION_WITH_PREPAID_USAGE_SERVICES_SMEPLUS-26-09-06-SAAS-CELL-001.md` | `1dd07d4a8753c07cdd52f45b0daa2057631fe517` | Low-base-subscription commercial direction; price remains non-frozen |
| P-28 | `28_BOSS_DECISION_PACKAGE_AND_ORGANIZATION_SIZE_AS_ROOM_SIZE_MODEL_SMEPLUS-26-09-06-SAAS-CELL-001.md` | `0d3468f5e524dfccf311f9f89533afab2c4ac70c` | Package sizing signal, package != tier, package != physical host |
| P-29 | `29_BOSS_AUTHORIZED_TENANT_RESOURCE_GOVERNANCE_AND_CAPACITY_WORK_PACKAGE_SMEPLUS-26-09-06-SAAS-CELL-001.md` | `168d14d7ba9120b51d81c2898eacf791fa223db9` | Resource envelope work package, logical vs physical quota, heavy-job preauthorization, protected mode, cell headroom, pre-pricing evidence gate |
| P-30 | `30_BOSS_DIRECTION_STANDARD_TO_ENTERPRISE_MOBILITY_MUST_BE_DESIGNED_SMEPLUS-26-09-06-SAAS-CELL-001.md` | `0395a3a6b6b77383233f49fe4f6e7c2c401044ed` | Standard→Enterprise as first-class mobility with identity, billing, audit and semantic continuity |

## Reconciled Parent Baseline

1. Two deployment tiers only: STANDARD and ENTERPRISE.
2. STANDARD remains pool-based multi-tenant SaaS unless evidence requires scoped isolation.
3. ENTERPRISE remains dedicated resource / dedicated tenant environment.
4. Tenant identity is independent of Cell / Server / Database Host identity.
5. One product / one Core codebase / many Cells.
6. Tenant Count is not a valid capacity model by itself.
7. Organization size may help package selection but actual workload is authoritative for capacity suitability.
8. Commercial package / logical entitlement must remain separate from physical infrastructure implementation.
9. Additional chargeable usage requires prepaid or otherwise secured authorization before execution/activation.
10. 30-day notice is forecast/preparation control and is not unsecured credit.
11. Customer-facing usage must be understandable, visible, traceable and auditable.
12. SMEsPlus software inefficiency must not be charged to the customer.
13. Customer logical quota must remain below technical safety/failure boundaries.
14. Heavy workloads may require preflight, reservation and isolated execution path.
15. Standard→Enterprise mobility must preserve Tenant identity, business semantics, accounting/tax meaning, usage evidence, wallet/billing history and audit lineage.
16. No final package price/capacity/topology is frozen before Cost-to-Serve, load testing, telemetry, margin simulation and Boss Final Freeze.

## G0 Evidence Disposition

`PARENT BASELINE IDENTIFIED / TRACEABLE / MATERIAL DECISIONS PRESERVED`

This register does not by itself close G0. It must be read together with the Carry-Forward Register, Contradiction/Supersession Register, Open Assumption Register, and Independent Challenge Report.
