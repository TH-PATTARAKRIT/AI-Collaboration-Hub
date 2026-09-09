# BOSS DECISION — PREPAID BEFORE USAGE; 30-DAY NOTICE IS NOT CREDIT

Session: SMEPLUS-26-09-06-SAAS-CELL-001
Jira: ERPPLUS-151
Status: BOSS APPROVED DIRECTION
Date: 2026-09-09

## Decision

SMEsPlus shall require sufficient prepaid service credit, secured credit, or already-paid reserved capacity before allowing chargeable usage or activating additional capacity.

The 30-day advance notice is a forecast and customer-preparation control only. It is not a 30-day unsecured credit facility and does not authorize continued consumption after available paid capacity is exhausted.

## Core Rules

1. 30-Day Notice != 30-Day Credit.
2. No Unsecured Postpaid Overage.
3. Chargeable capacity/workload must be financially covered before execution/activation.
4. If actual consumption accelerates and prepaid balance becomes insufficient before the previously forecast 30-day depletion date, SMEsPlus must require top-up/secured authorization immediately before allowing further chargeable consumption.
5. Payment/top-up must be confirmed before new chargeable capacity becomes available.
6. Forecasts must be continuously recalculated from actual usage; earlier estimates do not guarantee service until the forecasted date.
7. Non-chargeable/customer-owned data access and exit rights remain governed separately by contract and data-retention/exit policy; they must not create unlimited free processing capacity.
8. No Evidence = No Chargeable Overage.
9. No Surprise Billing.

## Control Flow

Paid/secured capacity -> usage request -> pre-execution entitlement/capacity check -> allow/reserve/deny.

If projected depletion <= 30 days -> notify.
If available paid capacity becomes insufficient earlier -> top-up required before further chargeable usage.

## Open Design Items

- Exact reserve algorithm and pre-authorization method
- Which workloads are hard-gated versus safely degraded
- Grace/read-only policy for base service expiration
- Recalculation cadence for projected depletion
- Notification/escalation channels
- Standard vs Enterprise application of reserved capacity and variable charges

Boss remains sole Final Approver.