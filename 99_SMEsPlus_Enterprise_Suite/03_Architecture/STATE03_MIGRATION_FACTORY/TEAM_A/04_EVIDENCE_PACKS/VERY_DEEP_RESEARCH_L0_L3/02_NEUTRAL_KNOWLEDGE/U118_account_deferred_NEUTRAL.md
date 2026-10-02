# U118 — Deferred Revenue and Expense: Neutral Knowledge
## Date: 2026-10-02
## Finding: ABSENT from Odoo 19 Community

---

## Presence or Absence Finding

Odoo 19 Community does not include a deferred revenue or deferred expense management module.
There is no standalone module called account deferred, and no deferred schedule model exists
anywhere in the Community accounting source. The Community account module provides standard
account types and journal entry capabilities, but all automated amortisation schedule features
belong to the Enterprise edition only.

The only mention of deferred accounts in Community is in test configuration helpers, where
standard balance sheet account categories are used as placeholders for payment method setup
tests. This is an accounting infrastructure detail, not a functional deferred revenue or expense
management feature.

---

## What Deferred Revenue and Deferred Expense Mean

In accounting, deferred revenue is money received from a customer before the related goods or
services have been delivered. Until delivery occurs, the amount is a liability because the
business owes the customer either the service or a refund. Common examples include annual
software subscription payments, prepaid maintenance contracts, and advance ticket sales.

Deferred expense (also called prepaid expense) is the opposite: money paid by the business
before the related benefit is received. Until the benefit is consumed, the amount is an asset.
Common examples include insurance premiums paid for future months and rent paid in advance.

Both situations require the initial receipt or payment to be recorded on the balance sheet rather
than immediately in income or expense, and then gradually recognised in profit and loss over time
as the obligation is fulfilled or the benefit is consumed.

---

## How Amortisation Schedules Work

An amortisation schedule for deferred revenue or expense defines how much of the deferred amount
is recognised in each accounting period. The most common method is straight-line: the total amount
is divided evenly across the number of periods. For example, a twelve-month service contract worth
twelve thousand units of currency would recognise one thousand per month.

The schedule requires:
- A start date (when deferral begins)
- An end date (when full recognition completes)
- The total amount to be deferred
- The account to hold the deferred balance during the deferral period
- The account to receive the recognised portion each period

---

## How Periodic Journal Entries Are Generated

In a system with automated deferred management, a scheduled background process runs at the end
of each accounting period. For each active deferral record, it calculates the amount to recognise
in that period and creates a journal entry that moves the appropriate portion from the balance
sheet account to the income or expense account. The entry is dated within the period being closed.

After the final period, the balance sheet account returns to zero and the full amount has been
recognised. The system marks the deferral record as complete and stops generating entries.

In Enterprise Odoo, this generation is triggered automatically by a scheduled action. In Community,
no such automation exists, and accountants must create the periodic recognition entries manually.

---

## Account Configuration Needed

For deferred revenue, a liability account is required to hold amounts not yet earned. This is
typically categorised as a current liability because most deferred revenues are expected to be
recognised within twelve months.

For deferred expense, an asset account is required to hold amounts not yet consumed. This is
typically categorised as a current asset or a prepayment account.

The recognised portion each period flows to the normal revenue or expense account associated with
the original transaction.

In Community, accountants can configure these account types using the standard account type
selection. The available types include current assets, prepayments, and current liabilities,
which can serve as deferred holding accounts in a manual workflow. However, no system logic
enforces or automates the movement between these accounts.

---

## Migration Implication

Organisations migrating from a system that has automated deferred revenue or expense management
to Odoo 19 Community will need to evaluate whether manual processes can replace the automation,
or whether the Enterprise edition is required. The account structure for holding deferred balances
can be set up in Community, but the scheduling and automatic journal entry creation will not be
available without Enterprise.
