# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G2 — Package to Capacity Entitlement Freeze Candidate

Status: CORRECTED FREEZE CANDIDATE — SUBJECT TO INDEPENDENT RE-CHALLENGE
Supersedes for G2 decision use: `12_G2_PACKAGE_TO_CAPACITY_ENTITLEMENT_DRAFT.md`
Corrections incorporated: CH-01 through CH-09 from `14_G2_INDEPENDENT_CHALLENGE_ROUND1.md`
Owner: SaaS Team under SMEs Core
Final Approver: Boss only

## 1. G2 Freeze Boundary

G2 freezes the conceptual commercial-to-entitlement model only.

It does NOT freeze package names, prices, customer metering units, numerical allowances, rates, user/company limits, physical server/Cell class, CPU/RAM amounts, warning thresholds or Enterprise crossover values.

## 2. Canonical Commercial-to-Entitlement Chain

`Deployment Tier`
→ `Commercial Package`
→ `Versioned Capacity Entitlement Set`
→ `Included Allowances + Policy Rights`
→ optional `Add-on / Reserved / Temporary Authorized Capacity`
→ `Tenant Effective Entitlement`
→ `Usage / Admission / Financial Authorization Evaluation`

Rules:
- STANDARD may contain multiple Packages/Capacity Classes.
- ENTERPRISE remains one deployment tier and may contain reserved-capacity packages.
- Package/entitlement never identifies a physical Server/DB/Cell.
- Cell movement may occur without Package change.
- STANDARD package change does not change Tenant identity.
- STANDARD→ENTERPRISE is controlled mobility, not Package renaming.

## 3. Entitlement Dimensions — Conceptual

A Package may expose controlled entitlement across these categories; exact units/values remain HOLD:

1. Business Data Capacity — logical transactional/master/audit data attributable to Tenant.
2. File / Attachment Capacity — tenant-owned retained binary/document content.
3. Archive Capacity — long-term/inactive retained content under lifecycle policy.
4. Interactive Workload Capacity — normal synchronous ERP activity/concurrency envelope.
5. Background / Processing Capacity — scheduled/background work; heavy work may require preflight/reservation.
6. API / Integration Capacity — controlled integration activity envelope.
7. Generated Output / Export Capacity — material report/export packaging where separately justified.
8. Service / SLA Rights — support/availability/service commitments, separate from raw workload quota.

## 4. Commercial Unit Mapping Rule — Anti-Double-Charge

Internal resource metrics may observe one business action across multiple dimensions, but commercial charging must identify the customer-facing primary unit(s) and conversion logic explicitly.

Mandatory controls:
- one underlying event must not be charged repeatedly merely because it consumed CPU, DB, API and queue simultaneously;
- secondary engineering metrics may inform Cost-to-Serve, protection or recommendation without becoming separate charges;
- multiple commercial charges are permitted only when they represent separately disclosed/contracted value or capacity (for example, retained storage plus an explicitly priced optional third-party service);
- every Chargeable Usage line must identify its commercial unit/rule and Usage Evidence lineage.

Exact unit taxonomy remains OA-01 / later-gate evidence.

## 5. STANDARD Add-on Boundary

Add-ons augment entitlement but do not create an unlimited escape hatch from STANDARD shared-resource economics.

An Add-on is valid only while the resulting Tenant workload remains inside the evidence-backed STANDARD maximum shared envelope and applicable safety/fairness rules.

Sustained conditions beyond STANDARD suitability require disposition among:
- operational Cell move;
- STANDARD Package upgrade;
- redesigned/limited workload;
- ENTERPRISE candidate review;
- HOLD pending evidence.

Temporary legitimate burst alone does not force ENTERPRISE.

## 6. Versioned Effective Entitlement Contract

Every entitlement instance/change must carry at minimum:
- Tenant ID;
- entitlement/package/add-on identifier;
- version;
- valid-from timestamp;
- valid-to/expiry where applicable;
- source decision/order/contract reference;
- supersedes/superseded-by lineage;
- commercial/financial authorization reference where chargeable;
- state (scheduled/active/reserved/expired/superseded/held);
- audit actor/system provenance.

Historical entitlement at any material billing/usage/migration timestamp must be reconstructable without rewriting history.

## 7. Entitlement Reduction / Downgrade Safety

A downgrade, add-on expiry or entitlement shrink requires preflight against current logical usage, data footprint, active reservations and operational obligations.

Allowed dispositions include:
- schedule later effective date;
- retain existing data under controlled grandfather/read rules while blocking additional growth;
- archive/cleanup through explicit customer-controlled action;
- renew/buy Add-on;
- remain/upgrade Package;
- ENTERPRISE review;
- HOLD.

Forbidden:
- deleting/corrupting business facts to force quota compliance;
- silently making accounting/inventory history inaccessible;
- retroactively charging under a rule not active at the usage timestamp.

## 8. Active Reservation / Expiry Rule

A valid capacity/resource/credit reservation creates an execution lease for the authorized workload according to its reservation contract.

Entitlement expiry or Package change must evaluate active leases explicitly. It must not silently revoke a reservation mid-transaction/job in a way that breaks correctness.

Exact lease duration, cancellation and reconciliation mechanics remain later evidence.

## 9. Tenant Ownership Rule

Commercial Package, Add-on, wallet/credit authorization and Usage Evidence belong to the canonical Tenant boundary.

Unrelated customers cannot pool entitlements merely because they share:
- accounting firm;
- consultant;
- service provider;
- business partner;
- reseller;
- system integrator.

Common ownership/control must satisfy the canonical Tenant definition before shared Tenant entitlement is possible.

## 10. Included Allowance Meaning in STANDARD

Included Allowance grants logical entitlement to controlled shared-resource service under SLA, fair scheduling, protection and admission policy.

It does not imply:
- dedicated CPU/RAM;
- dedicated physical server;
- dedicated DB;
- unlimited concurrency;
- guaranteed execution of every heavy workload regardless of safety;
- physical reservation unless separately contracted.

## 11. Critical Workload / Operating Reserve Control

Critical ERP workload classification is governed by platform architecture and business-integrity semantics, not customer self-labeling.

Operating Reserve exists to protect correctness and continuity of explicitly classified integrity-critical operations where technically safe.

It is not:
- unlimited free processing;
- a bypass of entitlement;
- a bypass of prepaid financial authorization for optional/chargeable work;
- a guarantee beyond physical safety/correctness boundaries.

## 12. Package Recommendation Contract

Package recommendation must be explainable and evidence-backed.

Permitted reason-code classes include:
- logical data/storage footprint or growth;
- sustained transaction/interactive load;
- sustained processing/heavy-job load;
- API/integration intensity;
- concurrency pattern;
- SLA/isolation/compliance requirement;
- recurring Cell protection pressure attributable to legitimate Tenant workload;
- economic crossover from Cost-to-Serve;
- customer-requested dedicated environment.

Organization size, Company count and user count are input signals only.

A recommendation is not automatically an enforcement action. Enforcement requires the applicable entitlement/protection/safety policy.

## 13. Effective Entitlement Composition

`Base Package Entitlement`
+ `Active Add-ons`
+ `Valid Reserved / Temporary Authorized Capacity`
+ `Contractual Rights`
- `Expired / Superseded Entitlements`
= `Tenant Effective Entitlement at Time T`

Evaluation at Time T must use the version valid at the relevant usage/execution timestamp.

## 14. Customer Transparency Contract

Before additional consumption becomes chargeable or materially restricted, the customer-facing model must be able to disclose, where the metric is supported:
- Tier and Package;
- included entitlement;
- active Add-ons/reservations;
- current attributable usage;
- remaining allowance;
- projected capacity/cost impact;
- required top-up/add-on/upgrade/reservation action;
- evidence behind deduction/charge/restriction.

Forecast does not create financial authorization.

## 15. G2 Invariants

G2-01 Package != Deployment Tier != Tenant != Cell != Infrastructure.

G2-02 Tenant Effective Entitlement is time-versioned and historically reconstructable.

G2-03 No Add-on can legitimize unsafe or economically unsustainable unlimited STANDARD workload.

G2-04 Entitlement shrink must not destroy business truth or silently break integrity.

G2-05 Active authorized reservations require explicit lease-aware expiry handling.

G2-06 Unrelated Tenants cannot pool commercial entitlement.

G2-07 Included STANDARD allowance is logical shared-service entitlement, not dedicated physical reservation.

G2-08 Criticality classification is platform-governed; Operating Reserve is not unlimited free capacity.

G2-09 Commercial Unit Mapping must prevent accidental duplicate charging of one underlying economic/resource event.

G2-10 Package recommendation must be evidence-backed and explainable.

G2-11 Organization/user/Company size signals never override actual workload/isolation/economic evidence.

G2-12 No numerical package capacity or price is frozen at G2.

## 16. Package Mobility Outcomes

A controlled review may result in:
1. STAY CURRENT PACKAGE;
2. BUY/RENEW DIMENSION-SPECIFIC ADD-ON;
3. UPGRADE STANDARD PACKAGE;
4. DOWNGRADE / ENTITLEMENT REDUCTION WITH SAFE PRECHECK;
5. MOVE CELL / PLACEMENT WITHOUT COMMERCIAL CHANGE;
6. ENTERPRISE CANDIDATE REVIEW;
7. HOLD — EVIDENCE INSUFFICIENT.

## 17. Open Evidence Preserved

Customer-facing units, numerical envelope sizes, actual charging rates, Cost-to-Serve values, Cell limits and Enterprise crossover remain open and require later evidence.

## 18. Freeze Candidate Disposition

CH-01 through CH-09 are incorporated.

Status: `READY FOR INDEPENDENT RE-CHALLENGE`.
