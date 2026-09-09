# BOSS DECISION — PACKAGE AND ORGANIZATION SIZE AS ROOM-SIZE MODEL

Session: SMEPLUS-26-09-06-SAAS-CELL-001
Date: 2026-09-09
Status: BOSS APPROVED DIRECTION
Boss: Sole Final Approver

## Decision

SMEsPlus shall continue to divide the base rental / subscription into commercial packages. Organization size may be used as one practical package-sizing input, analogous to choosing a larger or smaller condominium room.

The condominium analogy is adopted as a customer-facing commercial explanation:

- Room rent = Base Subscription / Base Rental.
- Room size = Package / included capacity class.
- Electricity and water = measurable variable usage / overage.
- Additional internet or optional facilities = optional integration / connectivity / add-on services.
- Core common-area operations required for the SaaS platform should normally be included in the base rental rather than fragmented into hidden fees.
- Other optional or third-party services remain separate and transparent.

## Important Architecture Boundary

Package size and organization size must NOT be confused with deployment tier.

- STANDARD and ENTERPRISE remain the two deployment tiers.
- STANDARD may contain multiple package sizes / capacity classes.
- ENTERPRISE remains dedicated capacity / dedicated tenant environment.
- Organization size alone shall not force a deployment tier.
- Actual workload, transaction volume, storage, processing intensity, integration load, growth, isolation, SLA, and sustained resource demand remain material capacity inputs.

Therefore:

> Organization size is a package-sizing signal, not the sole definition of capacity or tier.

## Commercial Direction

A future Standard package model may resemble:

- Small room / Small package
- Medium room / Medium package
- Large room / Large package

Each package shall define a clear included capacity envelope and a transparent base rental. Additional measurable usage beyond included capacity shall require prepaid credit / secured authorization before chargeable consumption.

The customer must be able to understand:

1. Which package they rent.
2. What is included in the package.
3. What additional consumption is chargeable.
4. Current wallet balance.
5. Forecasted depletion / top-up need.
6. Whether another package or Enterprise would be economically more suitable.

## Constitutional Rules Retained

- No Surprise Billing.
- No Evidence = No Chargeable Overage.
- Prepaid Before Usage for additional chargeable consumption.
- 30-Day Notice is forecast/customer-preparation control, not unsecured credit.
- Tenant Count != Capacity.
- Tier != Company Size.
- Pricing must follow the business process, not distort the business process.

## Open Design Work

Not frozen yet:

- Final package names.
- Final monthly prices.
- Exact definition of organization-size bands.
- Included transaction / processing / API / storage capacity per package.
- Transaction taxonomy and weights.
- Cost-to-Serve and target margin.
- Package upgrade/downgrade rules.
- Standard-to-Enterprise recommendation thresholds.

These shall be validated through Cost-to-Serve analysis, telemetry, load testing, and commercial simulation before final pricing freeze.
