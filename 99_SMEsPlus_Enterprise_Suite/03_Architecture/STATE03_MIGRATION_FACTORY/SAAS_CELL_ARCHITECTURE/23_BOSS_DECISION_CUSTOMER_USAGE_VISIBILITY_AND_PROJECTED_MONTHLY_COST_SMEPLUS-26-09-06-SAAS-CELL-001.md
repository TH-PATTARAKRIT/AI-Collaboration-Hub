# BOSS DECISION — CUSTOMER USAGE VISIBILITY AND PROJECTED MONTHLY COST

Project: SMEsPlus ENTERPRISE SUITE
Session: [SMEPLUS-26-09-06-SAAS-CELL-001]
Jira: ERPPLUS-151
Date: 2026-09-09
Status: BOSS APPROVED DIRECTION

## Decision

Boss approved the customer-facing usage visibility principle for SMEsPlus Standard and Enterprise commercial governance.

### Core rule

Customers must be able to see during the current billing period whether they are likely to incur additional charges before those charges appear on the monthly invoice.

This extends the previously approved transparent usage-based capacity direction and the constitutional rule:

> No Evidence = No Chargeable Overage.

It also adopts:

> No Surprise Billing.

## Customer-facing dashboard

The customer dashboard shall provide at least:

- Current plan / tier
- Base monthly subscription or reserved-capacity fee
- Included capacity / allowance
- Current measured usage
- Remaining allowance
- Current estimated monthly bill
- Projected month-end bill
- Estimated overage, if any
- Warning thresholds before overage
- Customer spending cap / overage policy where applicable
- Evidence / drill-down for chargeable usage

The customer must be able to understand whether the current month is likely to remain at the base fee or incur additional charges.

## Commercial distinction

### Standard

Standard uses shared capacity with an included capacity envelope. Additional usage within the permitted Standard shared-cell envelope may generate transparent metered overage according to published rules.

### Enterprise

Enterprise primarily pays for reserved dedicated capacity at a predictable monthly price. Resource expansion is handled as a capacity review / package upgrade, rather than surprise per-transaction overage inside the reserved envelope.

## Governance requirements

1. No hidden metering.
2. No retroactive unpublished charging rule.
3. No chargeable overage without auditable usage evidence.
4. Customers must see current and projected cost before billing close.
5. Temporary legitimate bursts must not automatically be treated as sustained heavy usage.
6. SMEsPlus software inefficiency must not be converted into customer overage.
7. Critical ERP integrity transactions must not be interrupted unpredictably by commercial controls.
8. Customer-facing commercial units should be understandable; internal CPU/RAM/DB/I/O metrics may be used for engineering and Cost-to-Serve analysis but should not be exposed as raw billing complexity unless contractually appropriate.

## Two-dashboard model

### Customer Dashboard

Purpose: transparency and spend predictability.

Answers:
- How much have I used?
- How much is included?
- Will I pay extra this month?
- What is the projected month-end bill?
- Why is an overage being projected or charged?

### Boss / Platform Dashboard

Purpose: platform economics and capacity governance.

Answers:
- Revenue per tenant
- Resource usage per tenant
- Cost-to-Serve
- Gross SaaS margin
- Capacity pressure
- Standard vs Enterprise suitability
- Enterprise migration / capacity review candidates

## Architecture chain

Tenant Resource Governor
-> Tenant Capacity Meter
-> Commercial Entitlement Engine
-> Customer Usage Dashboard / Projected Bill
-> Auditable Monthly Billing

## Open items

The following remain subject to design, research, load testing, and Boss Final Freeze:

- exact billing units
- included quotas
- overage rates
- warning thresholds
- spend-cap behavior
- projected-bill algorithm
- Standard maximum shared-cell envelope
- Enterprise capacity package sizes
- migration / upgrade gates

Boss remains the sole Final Approver.
