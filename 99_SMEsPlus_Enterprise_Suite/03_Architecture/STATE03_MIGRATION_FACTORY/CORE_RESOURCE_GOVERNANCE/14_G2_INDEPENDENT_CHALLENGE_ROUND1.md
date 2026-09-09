# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G2 — Independent Architecture Challenge / Round 1

Status: CHALLENGE COMPLETE — CORRECTION REQUIRED
Input Draft: `12_G2_PACKAGE_TO_CAPACITY_ENTITLEMENT_DRAFT.md`
Specialist Review: `13_G2_SPECIALIST_REVIEW.md`

## CH-01 — Double-Charge Risk Across Entitlement Dimensions
Severity: MATERIAL COMMERCIAL RISK.

A single business activity can create transaction count, API calls, generated output, DB growth and worker consumption simultaneously. If every dimension can become independently chargeable without a mapping contract, customer may be charged multiple times for the same economic event.

Required correction: add a `Commercial Unit Mapping Rule` that separates primary customer charge units from internal diagnostic/cost metrics and prohibits duplicate charging unless separately contracted value/resource consumption is explicit.

## CH-02 — STANDARD Add-on Escape Hatch
Severity: MATERIAL ARCHITECTURE/ECONOMIC RISK.

Unlimited add-ons could allow a sustained heavy Tenant to remain indefinitely in STANDARD even when it degrades shared economics or safety.

Required correction: add-on entitlement is valid only within the approved STANDARD maximum shared envelope. Sustained usage beyond that envelope triggers Package/Cell/Enterprise review.

## CH-03 — Downgrade / Entitlement Shrink Safety
Severity: MATERIAL CUSTOMER/INTEGRITY RISK.

A Tenant may request downgrade or an add-on may expire while current data/workload already exceeds the new entitlement.

Required correction: entitlement reduction requires preflight and deterministic disposition: allow with grandfathered read/use boundary, require cleanup/archive, delay effective date, purchase add-on, upgrade, or HOLD. Never delete/corrupt business data to force compliance.

## CH-04 — Add-on Expiry During Active Reservation
Severity: MATERIAL OPERATIONAL RISK.

An entitlement could expire while a pre-authorized heavy job or long-running process is active.

Required correction: effective entitlement evaluation must include active reservations and execution leases; expiry cannot silently revoke a reservation mid-transaction without a safe policy.

## CH-05 — Unrelated-Customer Pooling
Severity: MATERIAL SECURITY/COMMERCIAL RISK.

Shared service providers or accounting firms could attempt to pool package entitlements across unrelated customers.

Required correction: entitlements belong to canonical Tenant identity only. Business relationship/common service provider does not create shared entitlement/security boundary.

## CH-06 — Included Allowance vs Guaranteed Physical Capacity
Severity: MATERIAL EXPECTATION RISK.

Included allowance could be interpreted as a hard infrastructure reservation even in STANDARD.

Required correction: STANDARD included entitlement grants controlled logical access to shared capacity under SLA/fair-scheduling/protection policy; it does not imply dedicated physical reservation unless contractually stated.

## CH-07 — Critical Operating Reserve Abuse
Severity: MATERIAL COST/FAIRNESS RISK.

A Tenant could classify high-cost work as critical ERP activity to bypass charge/capacity controls.

Required correction: criticality is a platform-governed workload classification, not customer self-declaration. Operating reserve protects correctness/critical integrity, not unlimited free processing.

## CH-08 — Package Recommendation Explainability
Severity: MATERIAL PRODUCT-GOVERNANCE RISK.

Using many signals without a decision contract can create arbitrary package recommendations.

Required correction: recommendation must produce evidence-backed reason codes (e.g., storage, sustained processing, API intensity, isolation/SLA, economic crossover) and distinguish recommendation from forced enforcement.

## CH-09 — Entitlement Version/Time Semantics
Severity: MATERIAL AUDIT RISK.

The draft requires effective time but does not fully define historical reconstruction.

Required correction: effective entitlement must be versioned with valid-from/valid-to, source decision, supersession lineage and immutable historical reconstruction for billing/dispute/migration evidence.

## Round-1 Verdict

`REWORK REQUIRED — 9 MATERIAL PACKAGE/ENTITLEMENT CORRECTIONS`

G2 cannot pass until CH-01 through CH-09 are corrected and re-challenged.
