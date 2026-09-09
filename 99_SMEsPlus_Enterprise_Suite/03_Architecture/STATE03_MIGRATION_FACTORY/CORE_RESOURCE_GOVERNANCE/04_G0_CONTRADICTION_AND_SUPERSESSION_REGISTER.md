# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G0 — Contradiction & Supersession Register

Status: ACTIVE / NORMALIZATION REQUIRED
Owner: SaaS Team under SMEs Core

## Material Contradiction Review

| ID | Topic | Evidence Tension | Disposition |
|---|---|---|---|
| CR-01 | Monthly charge / projected bill vs prepaid-before-usage | Records 22–23 use projected monthly bill / overage language; record 26 prohibits unsecured postpaid overage | NORMALIZE: interpret as projected accrued chargeable usage / wallet deduction / secured charge estimate. No unsecured debt permission. |
| CR-02 | Wallet protection vs service interruption | Record 24 aims to prevent unexpected interruption; record 26 permits deny when paid capacity is insufficient | NORMALIZE: design deterministic Protected Mode; restrict optional/high-growth chargeable workloads first while preserving critical ERP integrity subject to safety. |
| CR-03 | Low base price 1,500–3,500 THB/month | Record 27 gives commercial direction; record 29 requires pre-pricing evidence before freeze | NO CONTRADICTION: price remains hypothesis/direction only. Freeze prohibited until evidence gate + Boss approval. |
| CR-04 | Package/organization size vs physical capacity | Record 28 uses room-size analogy; parent architecture says Tenant != Cell != Server != DB Host and Tenant Count != Capacity | NO CONTRADICTION: organization size is sales/sizing signal only, not physical placement identity. |
| CR-05 | STANDARD shared vs dedicated workload isolation | Parent baseline keeps STANDARD shared; workload controls may require isolated workers/resources for specific heavy jobs | NO CONTRADICTION: scoped workload isolation may be used without redefining Tenant as dedicated deployment or creating a third tier. |
| CR-06 | Enterprise migration vs identity continuity | Moving to dedicated resources could be misread as a new tenant | NORMALIZE: movement changes capacity/isolation placement only; Tenant identity and business semantics remain invariant. |

## Supersession Rules

1. Later Boss decisions refine earlier wording only where explicitly stated; they do not silently erase approved principles.
2. Record 26 constrains interpretation of records 22–25 on credit/charge timing.
3. Record 29 operationalizes records 22–28 into architecture work packages and explicitly blocks pricing/mechanism freeze.
4. Record 30 adds mandatory mobility evidence and becomes part of the pre-pricing evidence sequence.

## Gate Disposition

`NO FATAL PARENT CONTRADICTION FOUND`

However, CR-01, CR-02 and CR-06 require canonical interpretation to be carried into G1 invariants and later workstreams. Any design that reopens unsecured postpaid billing, all-or-nothing wallet shutdown, or tenant identity replacement is a gate blocker.
