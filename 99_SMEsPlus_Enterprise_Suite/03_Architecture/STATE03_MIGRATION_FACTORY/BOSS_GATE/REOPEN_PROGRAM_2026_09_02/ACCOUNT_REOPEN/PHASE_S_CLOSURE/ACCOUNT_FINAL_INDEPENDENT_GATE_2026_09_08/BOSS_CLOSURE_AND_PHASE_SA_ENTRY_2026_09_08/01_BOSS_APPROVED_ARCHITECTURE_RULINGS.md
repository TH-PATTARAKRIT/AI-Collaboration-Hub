# BOSS-APPROVED ARCHITECTURE RULINGS

Authority: Boss — Sole Final Approver  
Status: APPROVED  
Applies to: Account Phase S closure and Phase SA entry

## BD-ACC-01 — Canonical Accounting Event Identity

**CLOSED / BOSS APPROVED**

- Source Module owns the Business Fact.
- Accounting Core owns the canonical Accounting Event Identity.
- Posting Engine owns Ledger Posting.
- Accounting Event Identity is distinct from Source Document Number, Journal Entry Number, and Reconciliation Matching Number.
- The canonical Accounting Event is immutable in identity and provenance.
- Same-event retry must not create duplicate accounting events.
- Reversal is a new accounting event referencing the original accounting event.
- Every accounting event is bounded by Tenant + Company context.

Phase SA may design the technical representation independently; this ruling does not prescribe UUID/ULID/sequence/schema implementation.

## BD-ACC-02 — Company-scoped Tax / No Consolidated Tax Filing

**CLOSED / BOSS APPROVED**

- SMEsPlus does not perform Consolidation Accounting in the approved scope.
- VAT, WHT, tax registers, statutory tax reporting, tax ownership and filing are Company-scoped.
- Multi-company management/informational views may be provided.
- Such views must not create cross-company tax posting, offsetting, settlement, statutory aggregation, or filing authority.
- Multi-company support does not weaken Company accounting/tax boundaries.

## BD-ACC-03A — Inventory Valuation Recognition Policy

**CLOSED / BOSS APPROVED**

- Allowed policy values: `Periodic | Perpetual`.
- Policy authority: Product Category.
- Product must not override this policy.

## BD-ACC-03B — Inventory Costing Method Policy

**CLOSED / BOSS APPROVED**

- Allowed policy values: `Standard | Average | FIFO`.
- Policy authority: Product Category.
- Product must not override this policy.

## Product > Accounting boundary

At Product level, the approved Account override surface is limited to:

- Income Account
- Expense Account
- Price Difference Account

If a Product-level account is not set, it inherits from Product Category according to the Phase SA design. Periodic/Perpetual and Standard/Average/FIFO are not Product-level override controls.

## Source-learning generation and test-reset utilities

- v18/v19/source-generation identity is Evidence Provenance, not a SMEsPlus target-platform decision.
- Source-specific findings must remain generation-qualified where required.
- `om_data_remove` is classified as a source-learning/test-data reset utility, not a SMEsPlus accounting architecture requirement.
- Production SMEsPlus must not depend on a general-purpose transaction-deletion business module.
- Production corrections must preserve auditability through controlled correction/reversal/adjustment mechanisms rather than silent deletion.

These rulings supersede any unresolved Phase S question that asks the same decision without a material delta.