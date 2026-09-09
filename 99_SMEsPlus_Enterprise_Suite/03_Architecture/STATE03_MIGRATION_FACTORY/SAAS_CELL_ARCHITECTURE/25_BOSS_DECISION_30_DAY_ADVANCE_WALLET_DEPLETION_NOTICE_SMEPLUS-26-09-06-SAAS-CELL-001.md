# BOSS DECISION — 30-DAY ADVANCE WALLET DEPLETION NOTICE

Session: SMEPLUS-26-09-06-SAAS-CELL-001
Jira: ERPPLUS-151
Date: 2026-09-09
Status: BOSS APPROVED DIRECTION

## Decision

SMEsPlus shall notify the customer in advance when the projected wallet balance is expected to become insufficient.

The primary advance-notice requirement is 30 days before the projected insufficiency / depletion date.

This requirement applies to the customer-facing wallet protection model and is intended to give the customer sufficient time to prepare budget, internal approval, PO/payment processing, or top-up.

## Core Rule

> Notify before depletion, not after depletion.

> The primary wallet depletion warning shall be triggered when the forecasted depletion / insufficient-balance date falls within 30 days.

## Forecast Basis

The 30-day warning is forecast-based, not dependent only on the calendar month-end.

Example:

- Current wallet balance: 6,000 THB
- Estimated burn rate: 200 THB/day
- Forecasted depletion date: 30 days from now
- Result: Trigger advance warning now

## Customer-Facing Information

The notice should show at minimum:

- Current wallet balance
- Current usage / burn rate
- Projected depletion or insufficiency date
- Estimated remaining service runway
- Estimated amount required to top up
- Relevant usage evidence / cost drivers

## Additional Reminder Stages

30 days is the mandatory primary notice. Additional reminders such as 14, 7, 3, or 1 day before projected insufficiency may be designed later, but are not frozen by this decision.

## Retained Constitutional Rules

- No Surprise Billing.
- No Evidence = No Chargeable Overage.
- Wallet balance does not reset at month-end.
- Usage counters may reset by billing period while historical evidence remains auditable.

## Open Items

The following remain open for design and validation:

- exact forecasting algorithm
- burn-rate smoothing / seasonality treatment
- additional reminder cadence
- channel policy (in-app/email/SMS/etc.)
- escalation rules
- grace / restriction behavior after depletion

Boss remains the sole Final Approver.
