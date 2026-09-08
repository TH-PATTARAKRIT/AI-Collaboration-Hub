# BOSS DECISION — Usage-Based Capacity and Transparent Billing

Session: SMEPLUS-26-09-06-SAAS-CELL-001
Jira: ERPPLUS-151
Status: BOSS APPROVED DIRECTION
Date: 2026-09-09

## Decision

SMEsPlus shall communicate from the beginning of the customer relationship that subscription pricing is not based only on company size or user count. Standard subscription includes an explicit capacity envelope, while measurable usage beyond the included envelope may create additional monthly charges or trigger a capacity/tier review.

The customer-facing principle is:

> Pay for the product entitlement plus the capacity actually consumed beyond the included allowance, under a transparent and pre-disclosed policy.

This is not permission for unpredictable billing. SMEsPlus must provide measurable usage, published units/rates, included allowance, thresholds, warnings, forecast, and auditability before overage is charged.

## Required commercial structure

STANDARD
- Base subscription / product entitlement
- Included capacity envelope
- Measured usage
- Optional capacity add-on / controlled overage within Standard maximum shared-cell envelope
- Capacity review when sustained usage approaches/exceeds Standard maximum
- Enterprise migration when workload or isolation requirements exceed Standard shared envelope

ENTERPRISE
- Dedicated resource/capacity envelope
- Commercial terms aligned with reserved/dedicated capacity and service commitments

No third commercial tier is created.

## Customer-facing billing guardrails

1. No retroactive hidden metering rules.
2. No surprise overage without prior disclosure of unit, rate, included allowance, and threshold policy.
3. Customer portal/dashboard shall show current usage and projected monthly usage.
4. Warning thresholds shall be configurable/published before chargeable overage.
5. Temporary legitimate bursts shall be distinguished from sustained heavy usage.
6. SMEsPlus software inefficiency is SMEsPlus responsibility and shall not be converted into customer overage.
7. Usage evidence must be reproducible and auditable per Tenant.
8. Customer disputes must be resolvable from immutable/metered evidence.

## Internal vs customer-facing measurement

Internal Cost-to-Serve may measure CPU pressure, RAM pressure, DB load, I/O, queue, storage, API volume, job consumption, and growth rate.

Customer billing should use simpler, understandable, measurable commercial units rather than exposing raw infrastructure complexity directly. Final billing units remain open for design and validation.

## Core architecture chain

Tenant Resource Governor
-> Tenant Capacity Meter
-> Commercial Entitlement Engine
-> Customer Usage Statement / Billing

## Invariants

UCE-01 Tier and pricing shall not be determined by company size alone.
UCE-02 Every Standard plan shall define an included capacity envelope.
UCE-03 Overage, add-on, or migration decisions shall be supported by measured Tenant usage evidence.
UCE-04 Customer-facing usage rules shall be disclosed from the start of service.
UCE-05 Billing shall remain predictable through allowance, thresholds, warnings, and usage visibility.
UCE-06 Sustained workload beyond the Standard maximum shared envelope may require Enterprise migration.
UCE-07 Temporary business bursts shall not automatically force Enterprise migration.
UCE-08 SMEsPlus performance defects shall not be charged to customers as usage.
UCE-09 Customer billing units and internal resource metrics may differ, but must remain traceably related.
UCE-10 No Evidence = No Chargeable Overage.

## Open items

- Define customer-facing metering units.
- Define included capacity envelopes by plan.
- Define threshold/warning policy.
- Define overage/add-on rules.
- Define Enterprise migration gate.
- Define Customer Usage Dashboard and Boss Cost-to-Serve Dashboard.
- Validate unit economics through load testing and production telemetry before final commercial freeze.
