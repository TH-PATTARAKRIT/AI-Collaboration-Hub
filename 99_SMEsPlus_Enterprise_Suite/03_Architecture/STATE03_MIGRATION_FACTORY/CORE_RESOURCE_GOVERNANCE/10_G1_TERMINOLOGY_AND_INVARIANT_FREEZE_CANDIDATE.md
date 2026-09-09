# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G1 — Terminology & Invariant Freeze Candidate

Status: CORRECTED FREEZE CANDIDATE — SUBJECT TO INDEPENDENT RE-CHALLENGE
Supersedes for G1 decision use: `07_G1_TERMINOLOGY_AND_INVARIANT_DRAFT.md`
Corrections incorporated: CH-01 through CH-08 from `09_G1_INDEPENDENT_CHALLENGE_ROUND1.md`
Owner: SaaS Team under SMEs Core
Final Approver: Boss only

## 1. G1 Freeze Boundary

G1 freezes vocabulary and invariant meaning only.

G1 DOES NOT freeze:
- Package names or THB prices
- Included DB/storage/API/transaction values
- CPU/RAM/worker quantities
- Warning percentages
- Cell headroom or stop-placement thresholds
- Physical server counts
- PostgreSQL tenancy topology
- Kubernetes/Docker/cgroup mechanism
- Per-tenant container/DB design
- Final Protected Mode action matrix
- Heavy-job reservation algorithm
- Standard-to-Enterprise crossover threshold

No later team may derive numerical capacity, price or topology from G1 terminology alone.

## 2. Canonical Terminology — Freeze Candidate

| Term | Frozen Meaning | Explicit Boundary |
|---|---|---|
| SMEsPlus Product | One clean-room SaaS ERP product using one Core codebase across deployment forms | No Standard/Enterprise Core fork |
| Deployment Tier | Resource-isolation, SLA and operational model | Not company size, package size, company count or user count |
| STANDARD | Shared-resource multi-tenant Cell model with Tenant-specific security, entitlement, metering and fair scheduling | Does not imply low quality or dedicated infra per Tenant |
| ENTERPRISE | Dedicated resource/security/operational boundary for one Tenant with stronger isolation/SLA/reserved capacity | Does not imply one physical server or one fixed DB mechanism; realization remains evidence-dependent |
| Commercial Package | Customer-facing offer defining entitlement/capacity class and commercial terms | Not Tenant, Cell, Server, DB Host or Deployment Tier |
| Capacity Class | Logical sizing/entitlement class used to group resource envelope expectations | Not a physical machine class by definition |
| Tenant | Customer and security boundary: one independent customer or one demonstrably controlled corporate/economic group | Not Company, Cell, Server or Database identity |
| Company | Legal/accounting/business entity inside one Tenant | Cannot weaken Tenant security boundary |
| Cell | Operational placement/capacity/failure boundary containing shared platform resources for eligible STANDARD tenants | Not Package or Tenant identity |
| Placement | Controlled mapping of Tenant workload to an eligible Cell/resource boundary | Does not change Tenant identity |
| Capacity Entitlement | Logical resource envelope available under Package/add-on/contract | Does not transfer ownership of physical infrastructure |
| Included Allowance | Included entitlement before additional approved capacity/action is required | Not permission to consume until physical failure |
| Customer Logical Usage | Tenant-attributable, customer-understandable consumption used for visibility/entitlement/approved charging | Excludes raw platform overhead unless explicit published mapping exists |
| Internal Physical Consumption | Actual CPU/RAM/DB/IO/storage/worker/network/protection consumption used for engineering/SRE/FinOps | Not automatically chargeable customer usage |
| Quota | Logical entitlement boundary for a measurable resource dimension | Not technical failure boundary |
| Rate Limit | Time-based flow limit for request/job/API execution | Not total entitlement |
| Protection Boundary | Technical control region where restriction/admission changes are required to preserve safety/headroom | Not a price point and not one universal scalar |
| Failure Boundary | Measured unsafe region beyond which correctness, availability, recoverability or required performance cannot be assured | Not a commercial package limit |
| Headroom | Intentionally unused physical capacity for variability, maintenance, recovery and safety | Not sellable logical quota by default |
| Operating Reserve | Capacity prioritized for critical ERP integrity operations during pressure/protection states | Cannot override physical safety/correctness limits and is not evidence of a specific reserve quantity |
| Burst | Short-lived workload excursion that does not by itself prove package/tier unsuitability | Not automatically Enterprise justification |
| Sustained Heavy Workload | Persistent legitimate Tenant workload causing material shared-capacity/economic pressure | Excludes SMEsPlus implementation defects/inefficiency |
| Heavy Job | Predictable workload class capable of material CPU/RAM/DB/IO/storage/queue/worker impact | Not every asynchronous/background action |
| Raw Telemetry | Low-level engineering observation/event | Not customer charge evidence by itself |
| Normalized Usage Event | Tenant-attributed, normalized, timestamped usage fact promoted from trusted telemetry with controlled lineage | Requires trusted Tenant context, unit/resource identity, time/period and deduplication/idempotency identity where applicable |
| Usage Evidence Ledger | Immutable/auditable operational record of Normalized Usage Events and evidence lineage | Not General Ledger, accounting subledger or statutory posting |
| Chargeable Usage | Usage eligible for wallet deduction/charge only after Tenant attribution, evidence normalization, published unit/rule, entitlement evaluation and financial authorization are satisfied | No retroactive hidden charging |
| Additional Chargeable Usage | Chargeable consumption beyond included allowance or separately purchased add-on/capacity | Primary canonical term; must comply with prepaid/secured rules |
| Overage | Optional commercial/customer-facing synonym for Additional Chargeable Usage where contractually defined | Must never imply unsecured postpaid authorization |
| Prepaid Service Credit | Customer-funded balance available for eligible future service deductions | 30-Day Notice is not credit |
| Reserved Balance | Eligible service credit committed to authorized pending usage/capacity reservation | Not final measured consumption |
| Available Balance | Eligible prepaid/secured balance remaining after reservations | Not historical wallet value |
| Capacity Reservation | Pre-execution reservation of entitlement/resource/credit for foreseeable material workload | Actual final consumption is reconciled separately |
| Protected Mode | Deterministic staged restriction policy that limits selected workload classes to preserve integrity/safety | Not automatically whole-ERP shutdown |
| Hard Cap | Resource/action-specific stop boundary when continuation would violate entitlement or safety | Tenant-wide restriction requires separate explicit policy/safety basis |
| Standard-to-Enterprise Mobility | Controlled move from shared STANDARD capacity to dedicated ENTERPRISE boundary while preserving Tenant identity/business semantics/audit lineage | Not product fork, data reset or semantic migration |
| Cost-to-Serve | Measured total cost of serving representative Tenant/workload profiles, including appropriate platform protection overhead | Does not define customer billing units automatically |
| Platform Inefficiency | Resource consumption caused by SMEsPlus defects or inefficient implementation | Must not be converted into customer Chargeable Usage |

## 3. Usage Evidence Promotion Contract

`Raw Telemetry`
→ prove Trusted Tenant Context
→ normalize resource/unit/time/identity
→ deduplicate/idempotency control where applicable
→ `Normalized Usage Event`
→ append immutable lineage to `Usage Evidence Ledger`
→ evaluate Package/Entitlement/Published Commercial Rule
→ verify prepaid/secured financial authorization
→ `Chargeable Usage / Capacity Action`

No stage may be skipped when the result is customer charge, wallet deduction, entitlement restriction or dispute evidence.

## 4. Canonical Architecture Invariants — Freeze Candidate

| ID | Disposition | Frozen Rule |
|---|---|---|
| CRG-01 | APPROVE | Tenant identity is independent of physical Server/Node/Cell identity. |
| CRG-02 | APPROVE | Package is a commercial entitlement, not physical host identity. |
| CRG-03 | APPROVE | Tenant quota does not imply dedicated infrastructure. |
| CRG-04 | APPROVE | STANDARD remains shared-resource multi-tenant unless evidence justifies stronger isolation for a defined workload/tier. |
| CRG-05 | MODIFY / APPROVE | For each material resource dimension, commercial entitlement must leave evidence-backed technical protection margin before the unsafe/failure region. |
| CRG-06 | APPROVE | Customer logical storage is distinct from indexes, WAL, replication, backup, PITR and other platform protection overhead. |
| CRG-07 | MODIFY / APPROVE | Attachment/file binaries shall not reside in the transactional DB by default; exceptions require explicit performance, backup/restore, replication/WAL, security and economic evidence. |
| CRG-08 | APPROVE | Resource enforcement must preserve Tenant isolation, accounting integrity, auditability and transaction correctness. |
| CRG-09 | MODIFY / APPROVE | Foreseeably material workloads must be preflighted; reservation is mandatory where estimated consumption could cross entitlement, financial-authorization or technical-safety boundaries. |
| CRG-10 | APPROVE | 30-Day forecast warning does not create unsecured service credit. |
| CRG-11 | APPROVE | Additional Chargeable Usage requires paid/secured entitlement before execution/activation where the prepaid model applies. |
| CRG-12 | APPROVE | Customers must not be charged for SMEsPlus implementation inefficiency. |
| CRG-13 | MODIFY / APPROVE | Usage evidence must reconcile Tenant attribution, customer statement/wallet action, entitlement decision and internal telemetry lineage. |
| CRG-14 | APPROVE | Package migration or Cell movement must not change business semantics. |
| CRG-15 | APPROVE | Standard-to-Enterprise mobility preserves canonical Tenant identity, data semantics and audit lineage. |
| CRG-16 | APPROVE | Cell admission is based on measurable multidimensional capacity, not fixed Tenant count alone. |
| CRG-17 | APPROVE | Noisy-neighbor controls must act before physical resource exhaustion. |
| CRG-18 | APPROVE | Backup/DR/protection overhead is platform Cost-to-Serve and must not be naively equated to customer logical quota. |
| CRG-19 | ADD / APPROVE | SMEsPlus operates as one Product, one Core codebase, many Cells/resource boundaries. |
| CRG-20 | ADD / APPROVE | Only two deployment tiers exist: STANDARD and ENTERPRISE. |
| CRG-21 | ADD / APPROVE | Lower-level Company/business relationships can never weaken the Tenant security boundary. |
| CRG-22 | ADD / APPROVE | Wallet balance does not reset by billing period; usage counters may reset while historical evidence remains auditable. |
| CRG-23 | ADD / APPROVE | No Unsecured Postpaid Overage. |
| CRG-24 | ADD / APPROVE | No Evidence = No Chargeable Usage/Overage. |
| CRG-25 | ADD / APPROVE | Customer commercial units and internal resource metrics may differ only when traceability and published conversion/control rules are preserved. |
| CRG-26 | ADD / APPROVE | Protection controls prioritize critical ERP integrity operations where technically safe, but never override physical safety/correctness limits. |
| CRG-27 | ADD / APPROVE | Numerical capacity, prices, thresholds and topology mechanisms remain HOLD until their evidence gates are satisfied. |
| CRG-28 | ADD / APPROVE | Chargeable usage must be Tenant-attributable, reproducible, timestamped, deduplicated where required and contractually/financially authorized. |
| CRG-29 | ADD / APPROVE | Usage Evidence Ledger is operational evidence and cannot silently become accounting General Ledger/subledger truth. |
| CRG-30 | ADD / APPROVE | ENTERPRISE dedicated boundary does not mandate one physical server/database; implementation mechanism remains evidence-dependent. |

## 5. Multidimensional Capacity Rule

The simplified phrase `Commercial Limit < Protection Boundary < Failure Boundary` is retained only as an intuition.

The frozen rule is:

> For every material resource dimension or coupled capacity policy, customer entitlement/admission must leave sufficient evidence-backed protection margin before the measured unsafe/failure region.

CPU, RAM, DB connections, DB size, IOPS, queue depth, worker time, object storage and other dimensions may have different metrics, thresholds and interaction models.

## 6. Billing / Cost Separation Rule

Internal Cost-to-Serve may include infrastructure amplification such as indexes, WAL, replicas, backups, restore workspace, spare headroom and observability.

Those costs may inform package economics but do not become customer usage automatically.

Any conversion from internal cost metrics to commercial Chargeable Usage requires an explicit customer-facing unit/rule and must exclude SMEsPlus implementation inefficiency.

## 7. Protection Rule

Protected Mode and Hard Cap are action/resource policies, not synonyms for full Tenant shutdown.

Critical ERP integrity operations receive operating-reserve priority where technically safe. Whole-service restriction, read-only mode or shutdown requires a separate explicit safety/commercial/contractual policy and is not authorized by terminology alone.

## 8. Open Evidence Preserved

G0 OA-01 through OA-14 remain open unless explicitly closed by later gates. G1 freezes definitions; it does not manufacture missing evidence.

## 9. Freeze Candidate Disposition

All CH-01 through CH-08 corrections are incorporated.

Status: `READY FOR INDEPENDENT RE-CHALLENGE`.
