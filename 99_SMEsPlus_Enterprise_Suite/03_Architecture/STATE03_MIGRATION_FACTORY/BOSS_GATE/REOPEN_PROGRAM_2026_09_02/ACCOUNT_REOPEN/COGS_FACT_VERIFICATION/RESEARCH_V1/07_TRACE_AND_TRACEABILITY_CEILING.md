# 07 — Purchase/Sale/Return Fact Trace and Source↔DB↔Posting Traceability Ceiling

Consolidates the parent prompt's requested files 10, 11, 12, and 13.

## 1. Why This Is One File, Not Four

The parent prompt asks for, per flow: Transaction ID, Movement ID, Valuation ID, Journal Entry ID, Journal Line IDs, Account IDs, Debit, Credit, Quantity, Unit Cost, Total Value, Date/Timestamp, Company, Source reference — "for representative scenarios, capture deterministic linkage."

**This cannot be produced for SMEsPlus.** No SMEsPlus transaction has ever been created; there is no ID scheme, no database row, no posted journal line to cite. Any table populated with plausible-looking IDs and amounts here would be fabricated evidence presented as fact — exactly what the governing rules for this session (`No fabricated journal entry`, `No fabricated cost`, `Do not manufacture a clean conclusion`) forbid. So this file states the ceiling honestly instead of manufacturing one.

## 2. What Can Be Traced Instead — Conceptual Flow, Not IDs

Using the reference ERP's documented behavior (Evidence Level 6/7, per file `05`), the *conceptual* chain is traceable even though no concrete IDs exist:

**Purchase → COGS conceptual chain (source: DR files `17`, `21`):**
`Vendor Bill/Receipt → Inventory Asset (capitalized cost) → [held as asset until release event] → Delivery/Invoice (per JT-04 outcome) → COGS`

**Sale → COGS conceptual chain (source: DR file `18`):**
`Sales Order → Delivery or Invoice (version-dependent trigger, JT-04) → Inventory Asset reduced → COGS increased by the same amount, at the resolved account`

**Return → Reversal conceptual chain (source: DR file `19`):**
`Customer Return → Inventory Asset increased at current cost (not original, AVCO) → COGS decreased → Credit Note (financial) issued independently → the two reversal amounts are not proven equal (`CGS-U32`)`

Each arrow above is evidence-backed as a *pattern in the benchmark system*; none of it is a proof that SMEsPlus will implement the same pattern, and none of it substitutes for the Level 1–5 evidence the parent prompt actually asked for.

## 3. Representative Scenario Walk (Conceptual, Explicitly Labeled Hypothetical)

To satisfy the spirit of "representative scenario" without fabricating false-precision IDs, one scenario is walked in **labeled hypothetical form only** — every number is marked as illustrative, not observed:

> Illustrative only, not evidence: a AVCO-costed item is received at 100 units for value X, delivered in full, then 10 units are returned in a later period. Under the documented reference-ERP behavior, the return is valued at the average cost prevailing *at the time of the return* (which may differ from X/100 if intervening receipts occurred), while the customer credit note reverses the *original sale price*. The DR session's own evidence (`CGS-U32`) states these two reversal amounts are not proven to reconcile automatically, and "manual adjustment" is the reference system's own stated remedy. No specific unit counts, costs, or dates above are drawn from an actual transaction — they illustrate the *mechanism* the evidence describes, nothing more.

## 4. What Would Close This Gap

Per file `05` §"What This Means": a live reference-instance walkthrough (to observe real IDs and postings in the *benchmark* system, still not SMEsPlus) or, more usefully for SMEsPlus's own future, building SMEsPlus far enough to generate its own first real transactions once `JT-01`–`JT-12` are decided. Neither happened, or could reasonably happen, in a documentation-review session.
