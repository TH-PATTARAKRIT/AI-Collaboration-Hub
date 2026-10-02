# U156 — Fleet Vehicle Management: Neutral Knowledge

**Unit:** U156 | **Scope:** Community fleet add-on | **Claims:** 20

---

## Neutral-Reference Table

| Claim-ID | Neutral Reference (plain prose) |
|---|---|
| U156-C01 | Fleet module dependency list in the manifest |
| U156-C02 | Fleet module declared as a top-level application |
| U156-C03 | Primary vehicle data model declaration |
| U156-C04 | Vehicle model reference and driver assignment fields |
| U156-C05 | Vehicle lifecycle state field using a configurable state model |
| U156-C06 | Odometer virtual field backed by a log table |
| U156-C07 | Odometer unit selection field on the vehicle record |
| U156-C08 | Dedicated odometer log model for individual readings |
| U156-C09 | Last odometer reading resolved by maximum recorded value |
| U156-C10 | Vehicle contract model for lease and insurance tracking |
| U156-C11 | Days-remaining computation for contract expiry alerts |
| U156-C12 | Recurring cost frequency and amount on vehicle contracts |
| U156-C13 | Daily cron job managing contract state transitions and renewal alerts |
| U156-C14 | Scheduler method that posts renewal activity reminders and auto-transitions contract states |
| U156-C15 | Service log model recording maintenance costs and odometer at time of service |
| U156-C16 | Service log creates an odometer entry on write to prevent zero-value readings |
| U156-C17 | SQL-backed cost analysis view combining service and contract costs by month |
| U156-C18 | Daily-cost proration formula in the contract cost analysis view |
| U156-C19 | Two-tier security groups for fleet with Officer and Administrator levels |
| U156-C20 | Fleet community module has no direct accounting journal entry creation |

---

## Functional Summary (Neutral)

The fleet management component provides a structured system for tracking a company's vehicle inventory across its full operational life — from initial request through active use to cancellation. Each vehicle record holds identifying information such as registration details, a link to a driver, and physical characteristics inherited from a reusable model definition. Vehicle status is tracked through a user-configurable set of stages.

Odometer readings are stored as individual log entries; the vehicle's displayed current reading is the highest recorded value across all entries, not necessarily the most recently dated one. Recording a service visit automatically creates an odometer snapshot linked to that service record.

Contracts covering leases, insurance policies, or omnium cover are tracked against each vehicle with defined start and expiry dates, responsible parties, and optional recurring cost amounts at daily, weekly, monthly, or yearly frequencies. A scheduled background process runs daily to advance each contract through its lifecycle stages and to post a reminder notification when a contract approaches its configured alert threshold.

Cost reporting is provided through a read-only database view that aggregates service and contract spending month by month per vehicle, including a proration formula for daily-frequency contract charges.

Two access tiers control who can manage fleet records: an Officer role that can view and edit all vehicles, and an Administrator role that inherits Officer access and is granted unrestricted visibility over contracts, services, odometer records, and vehicle records. Multi-company record rules restrict each user's visibility to records belonging to their company.

No direct connection to the accounting journal is present in the community module. An accounting bridge add-on would be required to generate journal entries or analytic cost lines from fleet costs.
