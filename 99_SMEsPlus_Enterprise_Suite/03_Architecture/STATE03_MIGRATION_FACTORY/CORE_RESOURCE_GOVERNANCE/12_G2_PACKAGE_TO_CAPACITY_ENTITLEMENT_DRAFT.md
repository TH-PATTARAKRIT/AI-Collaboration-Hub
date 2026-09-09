# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G2 — Package to Capacity Entitlement Model / Draft

Status: EXECUTION DRAFT — SUBJECT TO SPECIALIST REVIEW / CHALLENGE
Gate: G2 — Package / Entitlement Gate
Owner: SaaS Team under SMEs Core

## 1. Gate Purpose

Define conceptually what a customer buys and what capacity entitlement is included, without freezing numerical quota, price, physical topology or billing rate.

## 2. Commercial Object Model

`Deployment Tier`
-> `Commercial Package`
-> `Capacity Entitlement Set`
-> `Included Allowances + Policy Rights`
-> optional `Add-on / Reserved Capacity`
-> `Tenant Effective Entitlement`

Rules:
- STANDARD may have multiple Commercial Packages / Capacity Classes.
- ENTERPRISE may have one or more reserved-capacity packages but remains one deployment tier.
- Package selection does not assign a physical server/Cell/DB.
- Tenant may move between eligible STANDARD packages without changing Tenant identity.
- STANDARD -> ENTERPRISE is a separate mobility decision, not merely a package rename.

## 3. Package Dimensions — Conceptual Only

A Package may express included entitlement across multiple dimensions. Exact values remain HOLD.

### A. Business Data Capacity
- logical business database usage;
- canonical transaction/master/audit metadata attributable to Tenant;
- excludes raw platform replication/backup overhead from customer logical usage.

### B. File / Attachment Capacity
- tenant-owned documents/images/PDFs/drawings/generated retained files;
- separate logical pool from Business Data by default.

### C. Archive Capacity
- long-term/inactive retained content under defined lifecycle/retention policy;
- distinct service behavior may apply later.

### D. Interactive Workload Capacity
- normal synchronous ERP request/concurrency envelope;
- customer-facing unit remains open.

### E. Background / Processing Capacity
- scheduled/background workload envelope;
- heavy jobs may require preflight/reservation.

### F. API / Integration Capacity
- controlled API/integration activity envelope;
- unit/rate remains open.

### G. Generated Output / Export Capacity
- large report/export/package generation where material resource consumption exists;
- must avoid charging twice for the same underlying event unless separate value/resource units are contractually justified.

### H. Service / SLA Rights
- support/service commitments and deployment-tier-specific rights;
- SLA rights must not be confused with workload quota.

## 4. Inputs for Package Recommendation

Package recommendation may consider:
- organization profile/size;
- user population;
- Company/branch count as complexity signals;
- transaction volume;
- data/storage footprint;
- file/attachment growth;
- API/integration intensity;
- report/batch/manufacturing workload;
- concurrency pattern;
- growth forecast;
- support/SLA requirement.

No single input is authoritative by itself.

`Organization Size helps select an initial room; Actual Workload validates whether the room is sufficient.`

## 5. Entitlement Types

| Type | Meaning |
|---|---|
| Included Entitlement | Capacity/right included in base Package |
| Add-on Entitlement | Separately purchased capacity that augments one or more dimensions |
| Reserved Entitlement | Capacity/credit/resource reserved before execution/activation |
| Temporary Authorized Capacity | Time-bound or workload-bound approved entitlement; must be prepaid/secured where chargeable |
| Enterprise Reserved Capacity | Dedicated resource envelope under ENTERPRISE commercial terms |

## 6. Effective Entitlement

Tenant Effective Entitlement is the controlled composition of:

`Base Package Entitlement`
+ `Active Add-ons`
+ `Valid Reserved/Temporary Capacity`
+ `Contractual Rights`
- `Expired/Revoked Entitlements`

Every entitlement change requires:
- Tenant identity;
- entitlement identifier/version;
- effective time;
- reason/source;
- commercial authorization where applicable;
- auditable history.

## 7. Customer-Facing Rule

Before additional usage becomes chargeable, customer must be able to know:
- current Package/Tier;
- what is included;
- current attributable usage;
- remaining allowance where measurable;
- whether proposed action needs add-on/top-up/upgrade/reservation;
- projected impact where calculable;
- evidence behind any deduction/charge.

## 8. Package Mobility Outcomes

Capacity review may yield:
1. STAY CURRENT PACKAGE;
2. BUY DIMENSION-SPECIFIC ADD-ON;
3. UPGRADE STANDARD PACKAGE;
4. MOVE TO ANOTHER STANDARD CELL/PLACEMENT for operational reasons without changing Package;
5. ENTERPRISE CANDIDATE REVIEW;
6. HOLD — EVIDENCE INSUFFICIENT.

Temporary burst alone does not automatically cause Enterprise movement.

## 9. Commercial Safety Rules

- No Unsecured Postpaid Overage.
- Additional Chargeable Usage requires prepaid/secured authorization where applicable.
- No Surprise Billing.
- No Evidence = No Chargeable Usage.
- Platform inefficiency is not customer usage.
- Package entitlement must not equal technical failure boundary.
- Customer-facing unit may differ from internal cost metric only with traceability.

## 10. Explicit Non-Decisions

G2 does not freeze:
- Small/Medium/Large names;
- 1,500–3,500 THB price direction;
- DB/storage GB quotas;
- transaction/API units;
- transaction weights;
- per-unit rates;
- Company/user limits;
- CPU/RAM guarantees;
- physical server/Cell class;
- package upgrade/downgrade thresholds;
- Enterprise crossover values.

## 11. Draft Gate Question

Can SMEsPlus describe what a customer buys as a coherent entitlement set without equating Package with physical infrastructure, double charging the same consumption, or hiding unsecured usage behind billing terminology?

Status: READY FOR SPECIALIST REVIEW.
