# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G6 — Specialist Review: Metering / Wallet

Status: SPECIALIST REVIEW COMPLETE — MATERIAL FINDINGS OPEN FOR CORRECTION
Artifacts reviewed:
- `34_G6_USAGE_LEDGER_METERING_MODEL_DRAFT.md`
- `35_G6_PREPAID_WALLET_CAPACITY_AUTHORIZATION_AND_CUSTOMER_TRANSPARENCY_DRAFT.md`

Review units:
1. Platform / Infrastructure Architecture
2. Database Engineering & Performance
3. SRE / Performance & Load Testing
4. Security / Tenant Isolation
5. FinOps / SaaS Cost Economics
6. Billing / Wallet / Metering Architecture
7. Product Package / Commercial Governance
8. Independent Architecture Audit liaison

Final Approver: Boss only

## 1. Cross-specialist assessment

The draft direction is materially stronger than direct telemetry billing or a mutable wallet balance model. The recommended architecture is compatible with G1–G5, but the following controls must be explicit before G6 may become a freeze candidate.

## 2. Specialist Findings

| ID | Severity | Finding | Required correction |
|---|---|---|---|
| SR-01 | CRITICAL | Canonical financial ownership could be confused by the new Organization Root / Company / Branch hierarchy. | Freeze Tenant as wallet/entitlement/metering financial owner; lower levels are allocation dimensions unless separately designed. |
| SR-02 | CRITICAL | `usage_event_id` alone may not prevent duplicate billing after retries, fan-out or Cell movement. | Require a canonical `economic_event_id`/idempotency identity plus source lineage; Placement Epoch cannot create a second charge. |
| SR-03 | HIGH | Event-time vs ingestion-time ambiguity can misapply entitlement/rate at period boundaries. | Require trusted occurrence time + observed time + rule/entitlement version reconstruction and append-only late correction. |
| SR-04 | CRITICAL | Metering outage could either stop critical ERP or create unmetered unsecured optional consumption. | Define degraded mode: durable evidence capture/replay; optional new chargeable work defers without authorization; integrity work proceeds only within prior entitlement/safety. |
| SR-05 | HIGH | Raw telemetry quality/confidence is not yet a formal promotion veto. | Add evidence-quality states and fail charge eligibility when attribution/quantity/unit/source confidence is insufficient. |
| SR-06 | HIGH | Derived aggregates can drift from event ledger. | Require reconciliation totals/checks and charge HOLD on unresolved discrepancy. |
| SR-07 | CRITICAL | Wallet reservation races can double-spend Available Balance. | Freeze atomic/fencing-equivalent authorization invariant independent of implementation mechanism. |
| SR-08 | CRITICAL | Actual consumption can exceed reserved amount and create negative balance after work already completes. | Require bounded maximum reservation for non-interruptible work and checkpoint/re-authorization for interruptible heavy work. |
| SR-09 | HIGH | Pending bank/payment state might be credited too early. | Distinguish pending vs confirmed funding; only policy-confirmed funds are spendable. |
| SR-10 | CRITICAL | Operational wallet entries could be mistaken for statutory accounting truth. | Freeze wallet as operational service-credit ledger; Accounting posting/reconciliation remains separate controlled contract. |
| SR-11 | HIGH | Multi-currency arithmetic can corrupt balance/forecast. | Freeze currency-scoped wallet balances; explicit FX conversion event required before cross-currency use. |
| SR-12 | HIGH | Metering evidence may capture excessive business/customer payload. | Apply data minimization; ledger stores metering facts and references, not full business payload unless justified. |
| SR-13 | MEDIUM | Dashboard might present provisional estimates as settled/final charges. | Add explicit data state/freshness labels: measured, reserved, provisional/projected, settled, final/closed. |
| SR-14 | HIGH | 30-day forecast could create false precision or stale warnings. | Require confidence/data-quality status and continuous recalculation from actual usage/reservations; no exact-date claim when confidence is inadequate. |
| SR-15 | CRITICAL | Wallet exhaustion service behavior remains dangerous if interpreted as immediate whole-ERP shutdown. | Freeze action-level staged restriction; protect committed business truth and critical integrity completion subject to safety. Whole-service policy remains later commercial/legal decision. |
| SR-16 | HIGH | Manual adjustment/rate/rule changes can bypass evidence if admin-controlled without SoD. | Require immutable versioned commercial rules, reason-coded adjustments, approval/SoD appropriate to risk, and no silent ledger edit. |
| SR-17 | HIGH | Third-party service retries/vendor costs can be passed through as duplicate customer charges. | Require separately disclosed commercial unit, trusted vendor evidence, duplicate exclusion and prepaid authorization. |
| SR-18 | HIGH | Closed-period dispute correction can rewrite history if not constrained. | Require compensating correction/adjustment lineage; no destructive reopen of closed usage/wallet evidence. |
| SR-19 | HIGH | Base subscription coverage and variable wallet authorization are conflated. | Separate fixed scheduled obligation from variable usage reservation; both may draw from wallet but have distinct evidence and service-term rules. |
| SR-20 | HIGH | Rule change during an active reservation can change price after authorization. | Reservation must bind commercial rule/version and maximum authorized exposure for its lease; later rule change does not silently reprice the held workload. |
| SR-21 | HIGH | A single business action may consume several commercial-candidate units, creating accidental multi-charge. | Preserve G2 Commercial Unit Mapping and require charge grouping/reconciliation to the underlying economic event. |
| SR-22 | MEDIUM | Customer export/exit after wallet depletion could be treated as unlimited free heavy processing or completely blocked. | Separate basic data rights from expensive export/processing capacity; contract and capacity policy must define allowed bounded exit behavior. |

## 3. Specialist Architecture Recommendation

Recommend retaining:
- event-level immutable Normalized Usage Evidence Ledger as canonical operational usage evidence;
- derived aggregates for dashboard/billing performance;
- immutable operational Wallet Ledger with derived balances;
- pre-authorization/reservation + actual reconciliation for material additional usage;
- Tenant-level financial ownership with lower-level allocation dimensions;
- external billing/payment systems as integrated sinks/sources of confirmation, not sole Core evidence authority.

Reject:
- raw telemetry direct billing;
- mutable balance-only wallet truth;
- unsecured postpaid variable consumption;
- customer-controlled metering identity/quantity;
- immediate full-ERP shutdown as the default wallet exhaustion response.

## 4. External Evidence Assessment

AWS SaaS Lens supports tenant-level consumption visibility and use of metering data as a billing input. AWS Marketplace metering demonstrates practical importance of explicit dimensions, entitlement separation, retry/deduplication and audit records. These sources validate the need for deterministic metering controls but do not define SMEsPlus units, event cadence or billing provider.

## 5. Review Disposition

`READY FOR INDEPENDENT CHALLENGE — SR-01 THROUGH SR-22 MUST BE COVERED BEFORE G6 PASS CANDIDATE`.

No numerical prices, wallet thresholds, notification cadence, meter units, database mechanism or billing provider is frozen.
Build / Merge / Production remain HOLD.
