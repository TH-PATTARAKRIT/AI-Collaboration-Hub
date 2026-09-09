# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G1 — Terminology & Invariant Draft

Status: EXECUTION DRAFT — SUBJECT TO SPECIALIST REVIEW / INDEPENDENT CHALLENGE
Owner: SaaS Team under SMEs Core
Final Approver: Boss only
Gate: G1 — Terminology / Invariant Gate

## 1. Gate Purpose

Freeze shared vocabulary and architecture invariants before any numerical sizing, package quota, pricing, physical topology or enforcement threshold is frozen.

This document carries forward G0 evidence and does not resolve open numerical assumptions OA-01 through OA-14.

## 2. Canonical Terminology — Draft

| Term | Canonical Meaning | Explicit Non-Meaning |
|---|---|---|
| SMEsPlus Product | One clean-room SaaS ERP product with one Core codebase | Not a separate Standard product and Enterprise product |
| Deployment Tier | Resource-isolation / SLA operating model | Not company size, package size or user count |
| STANDARD | Shared-resource, multi-tenant Cell deployment with tenant-specific security, quota, metering and fair scheduling | Not low quality; not one tenant per server/DB/container by default |
| ENTERPRISE | Dedicated tenant resource/environment boundary with stronger isolation/SLA/reserved capacity | Not necessarily one physical server; exact mechanism is not frozen |
| Commercial Package | Customer-facing product/capacity offer | Not a server, Cell, DB host or deployment tier |
| Capacity Class | A logical entitlement/sizing class used to express included resource envelope | Not a fixed physical host identity |
| Tenant | Customer/security boundary: one independent customer or one demonstrably controlled corporate/economic group | Not a Server, Database, Cell or Company |
| Company | Legal/accounting/business entity inside one Tenant | Cannot weaken Tenant security boundary |
| Cell | Operational placement and failure/capacity boundary containing shared platform resources for a population of STANDARD tenants | Not equal to a Package or Tenant |
| Placement | The controlled mapping of a Tenant to an eligible Cell/resource boundary | Not customer identity |
| Capacity Entitlement | The logical resource envelope a Tenant is entitled to use under Package/add-on/contract | Not physical infrastructure ownership |
| Included Allowance | Capacity included before additional chargeable capacity/action is required | Not unlimited use until physical failure |
| Customer Logical Usage | Customer-understandable attributable consumption used for visibility, entitlement and permitted charging | Not raw total infrastructure overhead |
| Internal Physical Consumption | Actual CPU/RAM/DB/IO/storage/worker/network/protection consumption used for engineering and Cost-to-Serve | Not automatically billable customer usage |
| Quota | Logical entitlement boundary for a measurable resource dimension | Not the same as technical failure boundary |
| Rate Limit | Time-based control of request/job/API flow | Not total capacity entitlement |
| Protection Limit | Technical safety control that restricts load before platform failure risk | Not a commercial price point |
| Failure Boundary | Measured condition beyond which correctness, availability, recovery or performance can no longer be safely assured | Not a customer package limit |
| Headroom | Reserved unused physical capacity required for variability, recovery, maintenance and safety | Not sellable logical quota by default |
| Operating Reserve | Capacity intentionally preserved for critical ERP integrity operations during pressure/protection states | Not a promise to operate beyond technical safety |
| Burst | Short-lived workload excursion that does not by itself establish sustained package unsuitability | Not automatically Enterprise justification |
| Sustained Heavy Workload | Repeated/persistent legitimate workload that materially consumes shared capacity/economics over time | Not platform inefficiency or bad SQL caused by SMEsPlus |
| Heavy Job | Predictable job class capable of material CPU/RAM/DB/IO/worker/storage impact | Not every background job |
| Raw Telemetry | Low-level engineering observations/events | Not directly a customer charge record |
| Normalized Usage Event | Tenant-attributed, normalized, timestamped usage fact derived from controlled telemetry | Not yet a financial posting |
| Usage Ledger | Immutable/auditable record of normalized usage facts and their lineage | Not the statutory accounting ledger |
| Chargeable Usage | Usage that is contractually allowed to create a deduction/charge because unit, entitlement, evidence and financial authorization rules are satisfied | Not undocumented or retrospective usage |
| Additional Chargeable Usage | Chargeable consumption beyond included allowance or separately purchased add-on/capacity | Must not imply unsecured postpaid debt |
| Overage | Customer-facing commercial synonym for approved Additional Chargeable Usage where the published contract uses the term | Not permission for unsecured postpaid consumption |
| Prepaid Service Credit | Customer-funded balance available for eligible future service deductions | Not a 30-day credit facility |
| Reserved Balance | Portion of service credit committed to authorized pending usage/capacity | Not yet final measured consumption |
| Available Balance | Total eligible prepaid/secured balance less reserved commitments | Not the same as wallet total historical value |
| Capacity Reservation | Pre-execution reservation of entitlement/resource/credit for a workload likely to create material consumption | Not guaranteed actual charge amount |
| Protected Mode | Deterministic staged restriction state used to preserve integrity and safety by limiting selected workloads before broader failure | Not automatically whole-ERP shutdown |
| Hard Cap | A deterministic stop boundary for a specific resource/action class when continuation would violate entitlement or safety | Not necessarily tenant-wide lockout |
| Standard-to-Enterprise Mobility | Controlled move from shared STANDARD capacity to dedicated ENTERPRISE capacity while preserving Tenant identity and business semantics | Not a product fork or data reset |
| Cost-to-Serve | Measured total platform cost attributable to serving a representative tenant/workload profile, including protection overhead where appropriate | Not customer billing units by definition |
| Platform Inefficiency | Resource consumption caused by SMEsPlus defects/inefficient implementation such as bad SQL, N+1, memory leak, defective index or platform bug | Must not be converted to customer usage |

## 3. Candidate Invariant Disposition — Draft

| ID | Draft Disposition | Canonical Rule |
|---|---|---|
| CRG-01 | APPROVE | Tenant identity is independent of Server/Node/Cell identity. |
| CRG-02 | APPROVE | Package is a commercial entitlement, not physical host identity. |
| CRG-03 | APPROVE | Tenant quota does not imply dedicated infrastructure. |
| CRG-04 | APPROVE | STANDARD remains shared-resource multi-tenant unless evidence justifies stronger isolation. |
| CRG-05 | APPROVE | Commercial quota must remain below technical protection/failure boundaries for each material dimension. |
| CRG-06 | APPROVE | Customer logical storage is distinct from replication, backup, WAL, indexes and other platform protection overhead. |
| CRG-07 | MODIFY | Attachment/file binaries shall not be placed in the transactional DB by default; exceptions require explicit technical/economic evidence and protection analysis. |
| CRG-08 | APPROVE | Resource enforcement must preserve Tenant isolation, accounting integrity, auditability and transaction correctness. |
| CRG-09 | MODIFY | Workloads with foreseeable material capacity risk must be preflighted; reservation is required where estimated consumption could cross entitlement, credit or safety boundaries. |
| CRG-10 | APPROVE | 30-Day forecast warning does not create unsecured credit. |
| CRG-11 | APPROVE | Additional chargeable consumption requires paid/secured entitlement before execution/activation where the prepaid model applies. |
| CRG-12 | APPROVE | Customer must not be charged for SMEsPlus implementation inefficiency. |
| CRG-13 | APPROVE | Usage evidence must reconcile customer statement, entitlement action and internal telemetry lineage. |
| CRG-14 | APPROVE | Package migration or Cell movement must not change business semantics. |
| CRG-15 | APPROVE | Standard-to-Enterprise mobility preserves canonical Tenant identity, audit lineage and data semantics. |
| CRG-16 | APPROVE | Cell admission is based on measurable capacity, not fixed Tenant count alone. |
| CRG-17 | APPROVE | Noisy-neighbor controls must act before physical resource exhaustion. |
| CRG-18 | APPROVE | Backup/DR overhead is platform protection cost and must not be naively equated with customer logical quota. |
| CRG-19 | ADD / APPROVE | One SMEsPlus Product, one Core codebase, many deployment Cells/resources. |
| CRG-20 | ADD / APPROVE | Only two deployment tiers exist: STANDARD and ENTERPRISE. |
| CRG-21 | ADD / APPROVE | Lower-level Company/business relationships can never weaken the Tenant security boundary. |
| CRG-22 | ADD / APPROVE | Wallet balance does not reset by billing period; usage counters may reset while historical evidence remains auditable. |
| CRG-23 | ADD / APPROVE | No Unsecured Postpaid Overage. |
| CRG-24 | ADD / APPROVE | No Evidence = No Chargeable Usage/Overage. |
| CRG-25 | ADD / APPROVE | Customer-facing usage units may differ from internal metrics only when traceability is preserved. |
| CRG-26 | ADD / APPROVE | Protection controls prioritize critical ERP integrity operations where technically safe, but may never override hard technical safety boundaries. |
| CRG-27 | ADD / APPROVE | Numerical package limits, prices, thresholds and topology choices remain unfrozen until the required evidence gate is satisfied. |
| CRG-28 | ADD / APPROVE | Chargeable usage must be tenant-attributable, reproducible, timestamped and contractually authorized. |

## 4. Relationships to Freeze Conceptually

`Commercial Package -> Capacity Entitlement -> Tenant Usage -> Metering Evidence -> Capacity Control / Wallet / Customer Statement`

`Tenant Envelope -> Cell Envelope -> Platform Envelope`

`Commercial Limit < Protection Boundary < Failure Boundary`

The final relationship above is dimensional/policy-based, not a claim that all heterogeneous resources share one scalar threshold.

## 5. Explicitly Not Frozen at G1

- Package names or THB price points
- DB/storage GB values
- CPU/RAM amounts
- API rates
- Transaction weights
- Warning percentages
- Cell saturation thresholds
- PostgreSQL tenancy topology
- Kubernetes/Docker/cgroup mechanism
- DB-per-tenant/schema-per-tenant/shared-schema choice
- Final Protected Mode action matrix
- Final heavy-job reservation algorithm

## 6. Draft Gate Position

G1 cannot pass until Specialist Review and Independent Adversarial Challenge confirm that terminology is non-contradictory, mechanism-neutral where required, and sufficient to prevent later package/resource/billing semantic drift.
