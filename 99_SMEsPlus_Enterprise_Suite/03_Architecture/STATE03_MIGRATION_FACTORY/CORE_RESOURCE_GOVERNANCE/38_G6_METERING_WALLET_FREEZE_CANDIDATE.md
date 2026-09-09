# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G6 — Metering / Wallet Corrected Freeze Candidate

Status: CORRECTED FREEZE CANDIDATE — SUBJECT TO INDEPENDENT RE-CHALLENGE
Corrections incorporated: SR-01..SR-22 and CH-01..CH-36
Supersedes for G6 decision use:
- `34_G6_USAGE_LEDGER_METERING_MODEL_DRAFT.md`
- `35_G6_PREPAID_WALLET_CAPACITY_AUTHORIZATION_AND_CUSTOMER_TRANSPARENCY_DRAFT.md`

Owner: SaaS Team under SMEs Core
Final Approver: Boss only
Build / Merge / Production: HOLD

## 1. G6 Freeze Boundary

G6 freezes conceptual evidence, authorization, wallet, correction and customer-transparency contracts only.

G6 DOES NOT freeze:
- commercial unit names/weights;
- numerical included allowance or prices/rates;
- minimum wallet balance/reserve percentage;
- exact auto-top-up policy;
- exact reminder cadence beyond the inherited primary 30-day forecast requirement;
- grace/read-only/suspension duration;
- billing-cycle timezone/rounding scale;
- currencies/FX source;
- event store/message broker/database locking technology;
- billing/payment provider;
- evidence retention duration;
- statutory accounting/tax treatment.

## 2. Recommended Reference Architecture

```text
Trusted Source Activity / Platform Telemetry
        |
        v
Tenant Context + Producer/Source Proof
        |
        v
Economic Event Identity / Idempotency
        |
        v
Normalization + Quality + Defect/Retry Exclusion
        |
        v
Immutable Usage Evidence Ledger
        |
        +--> Derived Tenant Usage Aggregates / Capacity Signals
        |
        v
Event-Time Effective Entitlement + Commercial Rule Version
        |
        v
Commercial Unit Mapping / Included-Allowance Evaluation
        |
        +--> INCLUDED / NON-CHARGEABLE VISIBILITY
        |
        +--> ADDITIONAL CHARGEABLE CANDIDATE
                  |
                  v
        Prepaid/Secured Authorization + Reservation
                  |
                  v
        Execute / Checkpoint / Measure Actual
                  |
                  v
        Settle / Release / Adjustment
                  |
                  v
        Immutable Wallet Ledger
                  |
                  +--> Customer Statement / Dashboard
                  +--> Accounting Handoff/Reconciliation
```

An external billing/payment service may integrate with this chain but is not the sole canonical evidence authority for Tenant usage, entitlement or wallet authorization.

## 3. Canonical Ownership and Organizational Scope

Canonical hierarchy:
`PLATFORM -> TENANT -> ORGANIZATION ROOT / GROUP -> COMPANY -> BRANCH`.

Frozen G6 rule:
- Usage Evidence, Effective Entitlement, Wallet and financial authorization are owned at Tenant boundary.
- Organization Root/Company/Branch may be validated allocation/reporting dimensions.
- They cannot pool unrelated Tenants, transfer wallet credit, weaken isolation or independently change charge authorization.
- Future sub-wallet/budget design requires a separate governed model.

## 4. Usage Evidence Promotion Contract

A charge-relevant event must pass:

1. Authorized producer/source identity.
2. Trusted canonical Tenant context.
3. Source-domain evidence sufficient to prove the activity; producer authentication alone does not prove quantity/charge validity.
4. Canonical `economic_event_id` / idempotency identity where replay/fan-out is possible.
5. Platform-controlled or independently verified quantity/unit.
6. Trusted `occurred_at` plus `observed_at`.
7. Normalization to canonical resource/commercial-candidate unit and precision.
8. Retry/platform-defect amplification exclusion.
9. Evidence-quality state sufficient for the intended action.
10. Append immutable Normalized Usage Event with correction lineage.

Transport exactly-once semantics are NOT an architecture dependency. Correctness relies on idempotent economic identity, deduplication and reconciliation.

## 5. Minimum Normalized Usage Event Fields

At minimum:
- immutable `usage_event_id`;
- canonical `economic_event_id`/dedupe identity where applicable;
- `tenant_id`;
- optional validated organization/company/branch allocation IDs;
- source component/producer + source reference;
- workload/request/job/correlation identity;
- resource dimension and normalized quantity/precision;
- trusted `occurred_at`, `observed_at`;
- source placement/cell lineage and Placement Epoch where applicable;
- evidence-quality status;
- original/correction/reversal linkage;
- audit provenance.

When promoted to commercial evaluation, attach/resolve:
- Effective Entitlement version;
- Commercial Rule version;
- Commercial Unit Mapping;
- included/additional disposition;
- authorization/reservation reference where chargeable.

## 6. Cell Movement / Replay Control

Tenant/economic usage identity is independent of Cell identity.

Rules:
- old/new Cell replay cannot produce a second charge identity;
- Placement Epoch is lineage/fencing evidence, not a customer charge dimension;
- stale-authority source events are quarantined/reconciled where placement authority cannot be proven;
- Standard->Enterprise movement preserves Tenant, wallet, usage period and economic-event identities;
- no usage period reset or double settlement at cutover.

## 7. Commercial Unit and Outcome Rule

For each customer-facing commercial unit, the rule must explicitly state what constitutes billable completion, e.g.:
- retained quantity/time;
- successfully committed output;
- attempt-based service only when explicitly disclosed/contracted;
- third-party committed consumption where independently evidenced.

Default rule: failed internal processing is not silently chargeable merely because compute occurred.

One business/economic event cannot be multiplied into customer charges just because CPU, DB, queue, API and storage metrics all observed it. G2 Commercial Unit Mapping remains mandatory.

## 8. Event Time / Period / Rate Version

- Trusted occurrence time determines canonical usage period under the period policy.
- Observation/ingestion time is retained separately.
- Entitlement and commercial rule are resolved from the version effective at trusted event/authorization time.
- Active reservations bind their authorized commercial rule/version and maximum exposure for the lease; a later price/rule change cannot silently reprice that held workload.
- Commercial rules are immutable/time-effective. Never edit historical rate truth in place.
- Late events have one canonical period and follow explicit late/correction policy.
- Closed periods are not destructively rewritten.

## 9. Precision / Rounding

- Preserve normalized quantity at canonical measurement precision.
- Define deterministic unit conversion version.
- Avoid repeated per-event monetary rounding where it creates systematic bias; aggregate at appropriate precision before monetary rounding according to the commercial unit rule.
- Statement and wallet arithmetic must reproduce from the same rule/precision lineage.

Exact scales remain Accounting/Commercial evidence work.

## 10. Evidence Quality States

Candidate conceptual states:
`OBSERVED -> VERIFIED/ATTRIBUTED -> NORMALIZED -> ELIGIBLE -> AUTHORIZED -> SETTLED`
with exceptions:
`DUPLICATE / DEFECT-EXCLUDED / HELD-FOR-EVIDENCE / CORRECTED / REVERSED`.

If Tenant, quantity, source, unit, rule or dedupe evidence is materially insufficient: charge eligibility fails closed (`NO CHARGE / HOLD FOR EVIDENCE`).

## 11. Metering Degraded Mode

Metering-system outage must not corrupt ERP or create unsecured optional consumption.

Frozen rules:
- trusted source activity must retain durable replay/reconstruction evidence;
- already-entitled/authorized integrity-critical work may complete where technically safe and evidence can be reconstructed;
- NEW optional/additional chargeable work requiring authorization defers/denies when authorization cannot be proven;
- heavy/material work cannot start without required reservation;
- recovery replay must preserve original occurrence identity and dedupe;
- dashboard may show stale/degraded data explicitly, but execution never authorizes from stale dashboard cache.

No broker/outbox implementation is frozen.

## 12. Wallet Ledger Contract

Wallet is an append-only operational service-credit authorization ledger, not one mutable balance field and not statutory GL/subledger.

Entry classes include, as applicable:
- confirmed funding;
- reserve;
- release;
- usage settlement;
- base subscription/add-on settlement;
- refund/credit/debit adjustment;
- chargeback/funding reversal;
- dispute/hold markers;
- explicit instrument expiry only when contractually valid.

Every entry has Tenant, currency, immutable identity, source reference, timestamp, rule/authorization reference and audit provenance.

History is corrected by compensating entries, never silent deletion/edit.

## 13. Currency-Scoped Balance Model

Balances are derived by Tenant + currency/funding instrument scope.

Conceptually:
`Confirmed Spendable Funding - Settled Deductions - Active Reservations +/- Approved Adjustments = Available Balance`.

Rules:
- Pending Funding is not spendable by default.
- Reserved Balance != final usage.
- No cross-currency arithmetic without explicit evidenced FX conversion event/rule.
- No implicit wallet transfer/pooling between unrelated Tenants.

## 14. Atomic Financial Authorization

Concurrent requests must not double-spend Available Balance.

Frozen invariant:
> New reservation/authorization must use an atomic or fencing-equivalent Tenant+currency decision against authoritative current spendable balance and active reservations.

Implementation may use transactions, locking, compare-and-swap, ledger serialization or another proven mechanism; G6 freezes the invariant, not technology.

Duplicate funding/payment callbacks similarly require idempotent external settlement identity before creating spendable credit.

## 15. Reservation Contract

Reservation fields/semantics include:
- reservation identity/idempotency identity;
- Tenant + currency;
- parent workload/economic-event identity;
- entitlement/commercial rule version;
- authorized maximum quantity/value exposure;
- state and lease/expiry;
- created/authorized/execution timestamps;
- source order/job/action;
- settlement/release/correction lineage.

State model:
`REQUESTED -> AUTHORIZED/HELD -> EXECUTING -> SETTLED`
with `RELEASED / CANCELLED / EXPIRED / HELD-FOR-REVIEW / FAILED-RECONCILIATION` as controlled alternatives.

Expiry/recovery must inspect workload outcome; it cannot blindly release a reservation if consumption may have occurred.

## 16. Anti-Gaming / Aggregate Exposure

Reservation/admission cannot rely only on individual request size.

The platform must detect/consider:
- child-job fragmentation;
- many concurrent micro-requests;
- Tenant-window aggregate exposure;
- canonical parent workload/job grouping;
- active reservations and pending obligations.

Customer-controlled fragmentation cannot bypass heavy-work or prepaid controls.

## 17. Preventing Unsecured Negative Balance

- Non-interruptible chargeable work requires a bounded maximum exposure reserved before start.
- Unbounded work cannot begin as one non-interruptible prepaid operation.
- Interruptible/heavy work checkpoints and re-authorizes before exceeding held exposure.
- Accelerated consumption pauses/defers optional work before unsecured balance is created.
- If a platform-required integrity completion must finish an already accepted business transaction and new customer authorization cannot safely be obtained, SMEsPlus preserves business truth and absorbs unavoidable platform cost rather than fabricating unsecured customer debt.

## 18. Funding / Chargeback / Refund

Funding becomes spendable only after policy-confirmed settlement.

Duplicate confirmation is idempotently reconciled to the external payment reference.

Chargeback/refund does not delete historical usage or funding entries. Use compensating entries and adjust future authorization/risk state. Exact contractual recovery policy remains Commercial/Accounting work.

## 19. Fixed Base Obligation vs Variable Usage

Base subscription/rental and variable chargeable usage are distinct obligations even if both use the same wallet.

- Base rental is scheduled/known by service term and may reserve/settle according to contract.
- Variable usage uses included allowance + pre-authorization/reservation rules.
- Dashboard separately shows scheduled fixed obligation reservations and variable usage reservations.
- Reservation/deduction priority is an explicit commercial policy; no hidden ordering.

## 20. Wallet Exhaustion / Service Continuity

Insufficient Available Balance does NOT imply arbitrary destructive whole-ERP shutdown.

Frozen action order principle:
1. deny/defer new optional/additional chargeable workload lacking authorization;
2. deny activation of new paid capacity/Add-ons lacking confirmed funding;
3. preserve settled customer data/audit history;
4. preserve committed integrity-critical completion where technically necessary/safe;
5. use deterministic Protected Mode/action-level controls;
6. whole-service read-only/suspension/grace remains separate future commercial/legal/service policy.

Customer exit/data rights remain separate from heavy processing entitlement. Basic rights cannot imply unlimited free bulk processing/export.

## 21. 30-Day Forecast & Notification Contract

Inherited primary control: notify when projected insufficiency/depletion falls within 30 days.

Forecast input must include where relevant:
- authoritative Available Balance after active reservations;
- known scheduled base obligations;
- settled/current measured usage;
- current active reservations/pending authorized work;
- recent burn/growth evidence;
- known scheduled material workloads.

Customer display must expose:
- as-of/data freshness;
- measured/settled vs reserved vs projected amounts;
- confidence/quality;
- assumptions/range when exact-date confidence is inadequate.

Forecast is continuously recalculated from evidence and is never financial authorization.

Additional alert cadence needs dedupe/cooldown/escalation semantics but exact thresholds/timing remain open.

## 22. Customer Transparency / Statement Contract

Customer dashboard/statement must support:
- Tier/Package and active Add-ons;
- included entitlement;
- current attributable usage;
- remaining allowance;
- wallet currency;
- confirmed spendable/Available Balance;
- active reservations and their reason;
- scheduled fixed obligations;
- settled deductions/cost to date;
- projected month-end usage/cost;
- projected insufficiency/depletion;
- required action/top-up/package/add-on guidance;
- blocked/deferred action reason code;
- evidence drill-down from charge/deduction to customer-safe Usage Evidence;
- data state: measured/reserved/provisional/projected/settled/final;
- data freshness/as-of timestamp.

Customer drill-down cannot expose another Tenant's data or unnecessary raw infrastructure/security telemetry.

## 23. Third-Party / Pass-Through Usage

Separately chargeable third-party service requires:
- disclosed/contracted unit;
- trusted vendor/service identity and quantity evidence;
- idempotency/duplicate exclusion;
- clear success/failed/committed-cost rule;
- prepaid/secured authorization;
- explicit late-arrival/closed-period adjustment policy.

Vendor invoice cost or retries are not automatically the customer commercial unit.

## 24. Manual Adjustment / SoD / Security

No actor may silently edit usage/wallet history.

High-risk actions require controls proportionate to risk, including:
- immutable reason/evidence;
- actor identity;
- approval/SoD where applicable;
- old/new rule version lineage;
- customer-visible adjustment where it affects their balance/statement.

A super-admin path cannot bypass Tenant isolation, evidence integrity or financial authorization silently.

Usage evidence stores minimum necessary metering facts + references; full business payload/PII is excluded by default.

## 25. Accounting Handoff

Usage Evidence Ledger and Wallet Ledger are operational evidence.

They MUST reconcile to Accounting/Finance outputs but do not define statutory posting themselves.

Required future handoff proof:
- funding/payment confirmation -> wallet funding entry -> accounting cash/receivable/deferred/revenue treatment as approved;
- wallet settlement/statement -> accounting recognition contract;
- refund/chargeback/adjustment -> accounting correction contract;
- period totals reconcile by Tenant/currency/rule.

Tax/VAT/revenue recognition policy is outside G6 freeze and requires Accounting/Commercial validation.

## 26. End-to-End Reconciliation Identity

One traceable identity chain must link:
`Source Activity`
-> `Normalized Usage Event`
-> `Period Aggregate`
-> `Entitlement Decision`
-> `Commercial Unit/Rule`
-> `Reservation/Authorization`
-> `Wallet Settlement`
-> `Customer Statement Line`
-> `Accounting Handoff Reference`.

Partial publication or discrepancy enters recoverable `HELD / RECONCILIATION REQUIRED`; affected customer charge is not silently finalized.

## 27. Enterprise Compatibility

ENTERPRISE may use fixed/reserved capacity economics rather than per-unit wallet deductions for every event. Nevertheless Tenant-level Usage Evidence remains mandatory for:
- reserved-envelope proof;
- capacity governance;
- Cost-to-Serve;
- SLA/isolation analysis;
- package/capacity recommendation;
- audit/dispute where variable/additional services exist.

Same Core evidence semantics remain across tiers.

## 28. G6 Freeze Candidate Invariants

G6-01 Raw telemetry != Chargeable Usage.
G6-02 Canonical economic-event identity prevents duplicate charge across retry/fan-out/Cell movement.
G6-03 Tenant is canonical financial/metering/wallet owner.
G6-04 Lower organizational levels are allocation dimensions unless separately governed.
G6-05 Usage Evidence Ledger is immutable operational evidence, not GL/subledger.
G6-06 Wallet Ledger is immutable operational authorization evidence, not GL/subledger.
G6-07 Charge eligibility requires trusted attribution, normalized quantity/unit, event-time entitlement/rule, anti-double-charge mapping and financial authorization.
G6-08 No Evidence = No Chargeable Usage.
G6-09 Platform defects/retry amplification are excluded from customer charge.
G6-10 Event/rule/entitlement/correction history is time-versioned and reconstructable.
G6-11 Transport exactly-once is not required; idempotency/dedupe/reconciliation are mandatory.
G6-12 Pending Funding is not spendable by default.
G6-13 Wallet authorization is atomic/fencing-equivalent against Tenant+currency Available Balance.
G6-14 Reservation != usage; actual settlement/release is evidence-based.
G6-15 New additional chargeable usage cannot knowingly create unsecured negative balance.
G6-16 Wallet and funding corrections are compensating entries, not destructive edits.
G6-17 Wallet arithmetic is currency-scoped; FX is explicit.
G6-18 No implicit cross-Tenant wallet pooling/transfer.
G6-19 30-Day forecast is preparation, not credit, and must disclose quality/freshness.
G6-20 Dashboard distinguishes measured/reserved/projected/settled/final states.
G6-21 Meter outage fails closed for new optional chargeable authorization while preserving already-authorized integrity work where safe.
G6-22 Whole-service suspension is not implied by wallet depletion; Protected Mode is action-level/staged.
G6-23 Closed usage/wallet periods use compensating adjustments, not rewrite.
G6-24 External billing/payment vendors are integrations, not sole canonical Tenant usage authority.
G6-25 Accounting handoff/reconciliation is mandatory, but statutory posting/tax is not frozen at G6.
G6-26 No numerical price/meter/threshold/technology is frozen by G6.

## 29. Finding Coverage

The corrected candidate materially covers:
- SR-01..SR-22;
- CH-01..CH-36.

Independent re-challenge must verify each finding against the relevant controls above before Gate disposition.

## 30. Candidate Disposition

`READY FOR INDEPENDENT RE-CHALLENGE`.

Boss Final Approval is NOT implied.
Build / Merge / Production remain HOLD.
