# 06 — COGS Business Event Matrix (Consolidated from Verified DR Evidence)

This file consolidates the parent prompt's Sections 8 ("COGS Event Matrix"), 9 ("COGS Recognition Event"), and 10 ("Interim Account Forensics") into one file, because the underlying evidence for all three was already produced with genuine sourcing in the DR session (files `12`, `13`, `16`–`22`), and this session's job is fact-*verification*, not re-deriving the same reference-ERP research a second time. Every row below cites its DR source file; nothing here is new invention.

**Reminder of the evidence ceiling (file `05`):** every row describes the *reference ERP's documented behavior*, treated as a benchmark, not SMEsPlus's own future behavior. SMEsPlus's own event matrix does not exist yet because SMEsPlus has not been built or designed to this level.

## A. Purchase Flow (source: DR files `17`, `21`)

| Event | Quantity Impact | Inventory Value Impact | COGS Impact | Timing / Config Dependency | Fact Status |
|---|---|---|---|---|---|
| PO | None | None | None | — | VERIFIED (negative — PO itself has no accounting effect) |
| Receipt | Increases on-hand qty | Perpetual: increases Inventory Asset immediately. Periodic: qty only, value at close. | None directly | Depends on Periodic/Perpetual (`CGS-U01`) | VERIFIED for Perpetual pattern generally; `CGS-U30` (bill-before-receipt) weakly evidenced |
| Vendor Bill | None | Confirms/adjusts cost basis; may trigger Price Difference posting if bill price ≠ receipt valuation | None directly | Price Difference scope is `CGS-U03` CONFLICTING | PARTIALLY VERIFIED |
| Payment | None | None | None | — | VERIFIED (negative) |
| Purchase Return | Decreases qty | Reverses value at original or current basis (mechanism not uniformly confirmed) | None directly (reverses prior capitalization) | `CGS-U26` (Periodic-specific return handling) HOLD | HOLD |
| Vendor Credit Note | None (financial only) | May not equal the inventory-side reversal amount | None directly | Related to `CGS-U32` discrepancy pattern | HOLD |

## B. Sale Flow (source: DR file `18`)

| Event | Quantity Impact | Inventory Value Impact | COGS Impact | Timing / Config Dependency | Fact Status |
|---|---|---|---|---|---|
| SO | None | None | None | — | VERIFIED (negative) |
| Delivery | Decreases qty | Perpetual: releases Inventory Asset value | Perpetual (pre-19): recognizes COGS at delivery | Version-dependent (`CGS-U01`) | VERIFIED for pre-19 pattern; NOT the 19.0+ pattern |
| Customer Invoice | None | None (Perpetual) / drives value release (Periodic, at close) | Perpetual 19.0+: recognizes COGS at invoice, not delivery | Version-dependent — this is the crux of `JT-04`, see file `14` | CONFLICTING across versions — `CGS-U01` |
| Payment | None | None | None | — | VERIFIED (negative) |
| Customer Return | Increases qty | Reversal valued at *current* average (AVCO) not original — confirmed discrepancy vs. credit-note amount | Reverses prior COGS, imperfectly | This is `JT-05`, see file `15` | BLOCKING / HOLD — `CGS-U32` |
| Customer Credit Note | None (financial only) | May not equal inventory-side reversal | Financial-side reversal only | `CGS-U32` | HOLD |

## C. Inventory Flow (source: DR files `10`, `19`, `20`, `23`)

| Event | Quantity Impact | Value Impact | COGS Impact | Fact Status |
|---|---|---|---|---|
| Internal Transfer (same company) | Location change only | None (same valuation pool) | None | VERIFIED (negative) |
| Inventory Adjustment — Increase | Increases qty | Increases value at current cost | Not COGS | VERIFIED as a general principle; SMEsPlus-specific account TBD |
| Inventory Adjustment — Decrease | Decreases qty | Decreases value | **Configuration-dependent** whether this lands in COGS or a distinct Loss account — `CGS-U22` | BLOCKING — no safe default documented |
| Scrap | Decreases qty | Decreases value | Same as above — requires deliberate Loss location/account configuration | BLOCKING — `CGS-U22` |
| Backdate / Period Crossing | — | — | Interacts with Lock Date; `CGS-U17` HOLD | HOLD |

## D. Cost Flow (source: DR files `15`, `21`)

| Method | Receipt Cost Formation | Return Cost Basis | Landed Cost | Fact Status |
|---|---|---|---|---|
| Standard Cost | Fixed; variance to Price Difference Account (scope `CGS-U03` conflicting) | Not the primary open item | Eligibility unconfirmed — `CGS-U35` | PARTIAL |
| Average (AVCO) | Recalculated on each receipt | **Current average on return, not original — the core `CGS-U32`/`JT-05` fact** | Documented, eligible | VERIFIED for receipt; BLOCKING for return |
| FIFO | Layer-based | Layer-consumption on return only community-corroborated, not primary-documented | Documented, eligible | HOLD for return sub-case |
| Landed Cost (cross-cutting) | Allocated to eligible categories | — | Residual-after-full-sale posting is version-inconsistent, sometimes **no journal entry at all** — `CGS-U36` | BLOCKING |

## E. COGS Recognition Event — The Central Finding

The reference ERP does not have one COGS recognition event. Two independently-documented patterns exist across its own version history:

- **Pre-major-version-19:** COGS recognized **at delivery** (physical stock movement), with an interim account bridging until invoice.
- **19.0+:** COGS recognized **at invoice/bill posting**, with the delivery-time interim mechanism demoted to a closing gap-filler rather than the primary trigger.

This is not a SMEsPlus design choice being described — it is a documented fact about the benchmark system changing its own architecture. **SMEsPlus's own COGS recognition event is undecided and is exactly what `JT-04` must rule on** (file `14`). Selecting "whichever the reference does" is not available as an option, because the reference does not have a single answer.

## F. Interim Account Concepts Observed (source: DR files `06`, `08`, `21`)

| Concept | Business Purpose (as documented) | Creation Event | Clearing Event | Fact Status |
|---|---|---|---|---|
| Stock Input / Stock Output | Bridges physical movement and financial posting timing gap under interim-posting patterns | Physical movement | Bill/invoice posting | VERIFIED as a documented pattern in pre-19 versions |
| GRNI (Goods Received Not Invoiced) | Accrual for received-not-yet-billed goods | Receipt | Vendor bill | Whether Periodic has an equivalent visibility mechanism is `CGS-U25` BLOCKING |
| Goods Delivered Not Invoiced | Accrual for delivered-not-yet-invoiced goods | Delivery | Customer invoice | Same open question, sale side |
| Price Difference / Variation Account | Absorbs receipt-vs-bill cost variance | Bill posting when price ≠ valuation | Period close or immediate, scope conflicting | CONFLICTING — `CGS-U03` |
| Landed Cost Clearing | Holds allocated landed cost pending final destination posting | Landed cost bill | COGS or remains in expense account — version-inconsistent | CONFLICTING — `CGS-U34` |

No concept above is asserted as a required SMEsPlus account; each is reported strictly as an observed reference-system pattern, per the clean-room boundary in the DR session's own governing prompt.
