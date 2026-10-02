# U154 Neutral Knowledge — Stock Scrapping Flow and Valuation

**Unit:** U154 | **Classification:** Neutral Knowledge (Non-Technical)
**Date:** 2026-10-02

---

## What Scrapping Does in Practice

When a business decides that a product is damaged, expired, or otherwise unfit for sale or use,
it creates a scrap order. The scrap order records which product is being written off, how much,
from which physical location, and optionally which lot or serial number. A single button press
finalises the scrap and simultaneously removes the stock from the warehouse and records the
financial loss.

---

## How the System Records the Loss

Scrapping moves goods from a normal warehouse shelf to a special holding area called an inventory
loss location. This location acts as a virtual bin that absorbs the removed stock. If the company
uses automated accounting, the system immediately creates a journal entry that reduces the value
of the stock asset on the balance sheet and charges the equivalent amount to a scrap or inventory
loss expense account. The two accounting lines balance to zero, satisfying double-entry
bookkeeping.

---

## Cost Method Differences

The amount charged to the expense account depends on how the business values its inventory.

For businesses using the standard cost or average cost method, the loss is calculated simply by
multiplying the current unit cost of the product by the quantity being scrapped. The unit cost at
the moment of scrapping is applied uniformly.

For businesses using the first-in first-out method, the system traces which purchase receipts
still have unsold quantity and takes the cost from the oldest receipts first. The scrapped units
consume the oldest cost layers before moving to newer ones, so the financial loss reflects the
actual purchase price of the specific units being written off.

---

## What Happens to Available Stock

The scrapping process immediately reduces the quantity shown in the warehouse. The system checks
whether enough stock is available before proceeding. If there is insufficient stock, it warns
the user and gives them the option to continue or cancel. Scrapping a product with lot or serial
tracking removes those specific units from circulation.

---

## Irreversibility

Once a scrap order is marked as done, it cannot be deleted through the normal interface. There is
no cancel or undo button on a completed scrap order. Reversing a scrap requires creating a separate
corrective stock move manually, which is an intentional design choice to maintain an unbroken audit
trail.

---

## Replenishment Option

The scrap order includes an optional flag that, when checked, triggers an automatic replenishment
request for the scrapped quantity. This helps ensure that the warehouse restores its stock levels
without requiring a separate manual step.

---

## Multiple Companies

When an organisation operates multiple companies, each company's scrap orders are strictly isolated.
The source location and the scrap destination are automatically filtered to show only locations
belonging to the same company as the scrap order. This prevents one company's stock adjustments
from accidentally affecting another company's inventory or accounts.

---

## Accounting Requirement

The journal entry is only created when specific conditions are met. The product must be a storable
item, the company must use real-time automated inventory valuation, and the scrap location must
have an expense account assigned to it. If any of those conditions is absent, the stock quantity
is reduced but no accounting entry is generated. This is relevant for businesses that perform
periodic rather than perpetual inventory valuation.

---

## Architecture Change in Version 19

Earlier versions of the platform maintained a separate audit table called a valuation layer to
record each movement of inventory value. In version nineteen this separate table was removed. The
monetary value of each stock movement is now recorded directly on the movement record itself,
simplifying the data model while preserving the same accounting outcomes. A separate history table
records manual adjustments to product costs for audit purposes.

---

## Claim Count Verification

This neutral file covers twenty-two distinct technical claims from the restricted evidence file.
Each claim maps to one row in the VDR claims table in the restricted evidence file and all
descriptions above are written without technical code identifiers.
