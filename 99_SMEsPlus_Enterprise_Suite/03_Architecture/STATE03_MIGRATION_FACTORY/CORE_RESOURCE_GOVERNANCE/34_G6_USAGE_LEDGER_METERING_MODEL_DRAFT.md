# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G6 — Usage Ledger & Metering Model Draft

Status: DRAFT FOR SPECIALIST REVIEW AND INDEPENDENT CHALLENGE
Gate: G6 — Metering / Wallet
Owner: SaaS Team under SMEs Core
Final Approver: Boss only
Build / Merge / Production: HOLD

## 1. Purpose

Define one canonical, auditable usage-evidence architecture that supports customer transparency, entitlement evaluation, prepaid authorization, wallet deduction, dispute handling, package recommendation, Cell/Enterprise suitability and internal Cost-to-Serve without converting raw platform telemetry directly into customer charges.

This draft carries forward G1–G5 and the Boss-approved hierarchy:

`PLATFORM -> TENANT -> ORGANIZATION ROOT / GROUP -> COMPANY -> BRANCH`

Commercial ownership and financial authorization remain at the canonical Tenant boundary. Company/Branch may be allocation/reporting dimensions but cannot create cross-Tenant pooling or weaken Tenant isolation.

## 2. Evidence Anchors

Internal evidence:
- `10_G1_TERMINOLOGY_AND_INVARIANT_FREEZE_CANDIDATE.md`
- `15_G2_PACKAGE_TO_CAPACITY_ENTITLEMENT_FREEZE_CANDIDATE.md`
- `21_G3_STORAGE_DATABASE_FREEZE_CANDIDATE.md`
- `26_G4_COMPUTE_RUNTIME_FREEZE_CANDIDATE.md`
- `33_G5_INDEPENDENT_RECHALLENGE_AND_GATE_DISPOSITION.md`
- Parent SaaS Cell Architecture records 22–30

External pattern evidence reviewed 2026-09-10:
- AWS SaaS Lens — Tenant Activity and Consumption: tenant-level activity/consumption must be observable and can feed billing while remaining a tenant-aware operational signal.
  https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tenant-activity-and-consumption.html
- AWS Marketplace SaaS metering guidance: explicit pricing dimensions, entitlement-vs-consumption separation, deduplication/retry semantics and auditable metering records are material controls in usage-based billing.
  https://docs.aws.amazon.com/marketplace/latest/userguide/metering-for-usage.html

These references support design principles only. They do not freeze SMEsPlus vendor, billing provider, event frequency, dimensions, prices or numerical limits.

## 3. Architecture Alternatives

### Option A — Raw telemetry directly drives billing
Disposition: REJECT.
Reason: raw CPU/DB/queue/request telemetry is noisy, implementation-dependent, can include platform defects, can be duplicated/retried and is not necessarily customer-understandable.

### Option B — Periodic aggregate-only usage table
Disposition: REJECT as sole evidence authority.
Reason: cheap operationally but insufficient for dispute reconstruction, correction lineage, idempotency proof, migration/cell-move duplication control and rule-version reconstruction.

### Option C — Immutable normalized usage evidence ledger with derived aggregates
Disposition: RECOMMEND.
Reason: preserves event lineage while allowing operational/customer aggregates to be derived for performance. Aggregates are views/materializations, not the only source of truth.

### Option D — External billing provider is canonical usage truth
Disposition: REJECT as SMEsPlus Core authority.
Reason: an external provider may receive/export billing facts but must not become the only place where Tenant attribution, entitlement, reservation, correction and business evidence can be proven.

## 4. Canonical Evidence Promotion Chain

`Source Activity / Trusted Telemetry`
-> validate Trusted Tenant Context
-> identify canonical Economic / Usage Event
-> normalize Unit / Resource / Quantity / Time / Source
-> validate platform-defect exclusion where applicable
-> deduplicate / idempotency control
-> append `Normalized Usage Event`
-> append immutable lineage to `Usage Evidence Ledger`
-> derive period/resource aggregates
-> evaluate Effective Entitlement at Event Time
-> apply Commercial Unit Mapping / Included Allowance
-> determine Charge Eligibility
-> require financial authorization where chargeable
-> emit Wallet/Charge/Statement linkage

No stage may be skipped when the result affects money, entitlement restriction, package recommendation or customer dispute evidence.

## 5. Normalized Usage Event Contract

Every material normalized event shall carry or resolve at minimum:
- `usage_event_id` — platform-generated immutable identifier;
- `economic_event_id` or idempotency/deduplication identity where the same business/resource event can be retried/replayed;
- canonical `tenant_id`;
- optional `organization_root_id`, `company_id`, `branch_id` as subordinate allocation dimensions only;
- `resource_dimension` / `commercial_candidate_unit`;
- normalized quantity and precision;
- `occurred_at` and `observed_at` timestamps;
- source system/component and source event reference;
- source execution/correlation/job/request identifier where applicable;
- Placement/Cell lineage including placement epoch where movement can duplicate/replay activity;
- entitlement/rule evaluation version reference when promoted to charge eligibility;
- quality/confidence/evidence status;
- correction/reversal lineage if later corrected;
- producer/service identity and audit provenance.

Customer-supplied quantity, Tenant, unit, price, Cell, timestamp or classification is never trusted solely because it appears in a client payload.

## 6. Event Identity and Anti-Double-Charge Rule

One underlying economic/resource event must have one canonical metering identity even if it passes through App -> Queue -> Worker -> DB -> Storage or moves between Cells.

Rules:
1. Retries/replays must not create duplicate chargeable events.
2. Cell movement must not create a second billing identity for the same event; Placement Epoch is lineage, not a new charge key by itself.
3. Queue redelivery and API retry require idempotency/equivalent deduplication semantics.
4. Fragmenting one job into many child jobs cannot increase commercial charge unless the disclosed commercial unit itself is legitimately quantity-based.
5. Engineering metrics can multiply for Cost-to-Serve without multiplying customer charge lines.

## 7. Tenant / Organization Attribution

Canonical financial ownership = `Tenant`.

Company/Branch dimensions may support:
- internal customer allocation;
- statement drill-down;
- operational diagnostics;
- cost center reporting.

They must not:
- pool unrelated Tenant entitlement;
- permit cross-Tenant query/retrieval;
- move wallet ownership below Tenant without a future explicit commercial model;
- change Tenant security boundary.

## 8. Charge Eligibility Contract

A usage event is eligible to become Chargeable Usage only if all conditions hold:
1. Trusted Tenant attribution is proven.
2. Event/unit/quantity is normalized and reproducible.
3. Duplicate/replay control passes.
4. Effective Entitlement and included allowance at the relevant event time are reconstructed.
5. Published/contracted commercial unit and rule version is known.
6. Commercial Unit Mapping proves no accidental double-charge.
7. Platform inefficiency/defect exclusion has been applied where resource causation is material.
8. Required prepaid/secured authorization exists before execution/activation for chargeable usage.
9. Customer-visible evidence can explain the resulting deduction/charge.

If evidence is insufficient: `NO CHARGE / HOLD FOR EVIDENCE`; never invent usage.

## 9. Time, Period and Rule Versioning

Metering requires both occurrence and observation time.

Controls:
- server/platform-trusted occurrence time is preferred over client-declared time for financial evaluation;
- late events do not change the commercial rule retroactively; resolve the rule that was effective at the trusted occurrence time;
- closed-period statements/evidence are not destructively rewritten;
- corrections after closure use explicit adjustment/reversal/correction lineage;
- period aggregation uses a documented timezone/calendar contract;
- numerical rounding/precision policy must be deterministic and must avoid repeated per-event rounding bias where aggregation precision is required.

Exact billing-cycle timezone, grace window and rounding scales remain open for Accounting/Commercial validation.

## 10. Raw Telemetry vs Customer Meter

Raw telemetry can include:
- CPU time/pressure;
- RAM pressure;
- DB duration/connections/locks;
- I/O;
- queue/worker time;
- request counts;
- bytes transferred/stored;
- backup/replication overhead;
- retry amplification;
- platform/system work.

Customer commercial units may be simpler. A published mapping may use a subset or normalized derivative, but raw infrastructure metrics do not become chargeable automatically.

Platform-caused retries, bad SQL, missing index, memory leak, defective query plan or system amplification remain internal Cost-to-Serve unless a separate legitimate customer-facing unit is proven.

## 11. Metering Availability / Failure Semantics

Metering failure must not silently create either unlimited free chargeable consumption or corruption of mission-critical ERP processing.

Candidate control:
- trusted source activity is durably journaled/outboxed or otherwise retained for later promotion;
- included/authorized critical integrity operations may continue where safety permits and evidence can be reconstructed;
- new optional/additional chargeable work that cannot prove entitlement/financial authorization must defer/deny rather than create unsecured usage;
- heavy jobs requiring reservation must not start when authorization state is unavailable;
- replay after recovery must preserve dedupe and original occurrence lineage.

No specific message broker/outbox technology is frozen.

## 12. Aggregation and Reconciliation

Derived aggregates must reconcile back to ledger events.

Required chain:
`Source Evidence Count/Quantity`
= `Normalized Ledger Quantity +/- Explicit Corrections`
= `Period Aggregate`
-> `Included Allowance Consumption`
-> `Additional Chargeable Quantity`
-> `Wallet Reservation/Settlement`
-> `Customer Statement Line`

Discrepancy => HOLD the affected charge/statement item until resolved.

## 13. Security / Privacy / Retention

- Usage Evidence is Tenant-isolated and deny-by-default across Tenants.
- Metering records should store minimum necessary metering facts, not full business payloads by default.
- Admin/operator access is audited.
- Evidence correction is append-only/compensating, not silent mutation.
- Retention period must meet dispute/audit/accounting requirements; exact duration remains legal/accounting evidence work.

## 14. G6 Draft Invariants

G6-D01 Raw telemetry != Chargeable Usage.
G6-D02 One economic event cannot be double-charged through retries, fan-out or Cell movement.
G6-D03 Tenant is canonical financial/metering ownership boundary.
G6-D04 Usage Evidence Ledger is operational evidence, not statutory GL/subledger.
G6-D05 Charge eligibility requires event-time entitlement and rule reconstruction.
G6-D06 Late/corrected events use append-only correction lineage.
G6-D07 Meter outage cannot create unsecured optional usage.
G6-D08 Platform-defect/resource amplification is not customer chargeable usage.
G6-D09 Derived aggregates must reconcile to event evidence.
G6-D10 No numerical meter unit, price, frequency, retention duration or billing provider is frozen at G6 draft.

## 15. Open Items for Challenge

- exact customer-facing unit taxonomy;
- aggregation/rounding precision;
- late-event settlement policy;
- accounting/tax treatment of prepaid service credit;
- statement close/reopen policy;
- third-party pass-through service evidence;
- data-retention duration;
- final customer dashboard latency/SLA;
- exact dispute workflow.
