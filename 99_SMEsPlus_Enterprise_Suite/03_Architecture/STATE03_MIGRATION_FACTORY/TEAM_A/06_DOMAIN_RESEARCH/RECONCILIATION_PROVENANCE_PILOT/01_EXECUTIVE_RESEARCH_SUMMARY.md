> Domain: RECONCILIATION_PROVENANCE_PILOT (Gx10) | Documentation-Tier

# 01 — EXECUTIVE RESEARCH SUMMARY (Gx10)

## Scope

Four functions: Stock Moves History (physical provenance), backdating audit trail (direct stock↔financial cross-linking), cost/valuation origin tracking (per-lot identity), and Bank Reconciliation (explicitly distinguished as a different concept, not this scenario's subject).

## Headline finding — a real, documented Stock-Fact-to-Financial-Fact link exists

When an inventory transfer is backdated, Odoo posts a **chatter message on both the picking (stock side) and the journal entry (financial side)**, recording who backdated it, when, and why. This is the clearest direct evidence this Deep Study has found of the two "truths" (Stock Truth, Financial Truth) being cross-referenced with a shared audit trail at the level of an individual transaction — not just conceptually adjacent, but literally linked by a synchronized chatter record on both sides.

## Second finding — valuation carries its own origin-tracking mechanism

Clicking a product's Total Value in the valuation report shows "all incoming quantities with their remaining quantity and valuation" — i.e., the system already tracks, per lot/incoming-move, how much of that specific valued quantity remains, which is itself a reconciliation identity mechanism (this specific receipt's value is traceable independently of other receipts of the same product).

## Third finding — "reconciliation" is an overloaded term in the documentation

Bank Reconciliation (matching bank transactions to invoices/bills/payments) is Odoo's dominant use of the word "reconciliation," and is a **different** concept from Stock-Fact-to-Financial-Fact provenance. Recorded explicitly to prevent this Deep Study (or a future reader) from conflating the two.

## Not established

Whether the backdating chatter trail is the *only* stock↔financial cross-link mechanism, or whether ordinary (non-backdated) transactions have an equivalent, less-visible link (e.g., a stored reference field connecting a stock move to its journal entry) — not evidenced this round; the chatter trail is the clearest evidence found, not necessarily the only mechanism. Full runtime confirmation, as always.
