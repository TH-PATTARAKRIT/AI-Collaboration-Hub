> Domain: PERIOD_CUTOFF_VALIDATION_PILOT (Gx6) | Documentation-Tier

# 01 — EXECUTIVE RESEARCH SUMMARY (Gx6)

## Scope

Four functions: Lock Dates, Fiscal Year/Period configuration, the month-end Stock Closing + accrual process, and physical-date-vs-recorded-date cut-off consistency itself.

## The headline finding — resolves the 4-pilot valuation-timing question

Odoo 19's documented architecture is explicit and internally consistent once all the pieces are assembled:

1. A stock movement (receipt, delivery) does **not** post a journal entry on its own (contradicts the generic claim Gx1's `GRV-F04` recorded from a less specific documentation page).
2. Journal entries post when the **financial transaction** happens — a vendor bill or customer invoice (confirms Gx2's `SDV-F05` finding).
3. For anything physically moved but **not yet invoiced by period end**, a month-end **Stock Closing entry**, informed by accrual entries (Bill To Receive / Invoices To Be Issued / Billed Not Received / Invoiced Not Delivered / WIP), sweeps the outstanding value into the Balance Sheet so it is never missing — this is the mechanism that makes the architecture GAAP-complete despite deferring most entries to invoice time.
4. Gx4's `IAV-F03` finding (inventory *adjustments* post "immediately, no additional steps") is **not a contradiction of the above** — an adjustment has no future vendor bill/customer invoice to defer to; the adjustment application *is itself* the financial transaction in that case. Re-read this way, all four pilots' findings are mutually consistent, not contradictory.

## Remaining open question

The one piece not yet resolved: `GAP-PDT-01`/`CQS-GRV-04` (whether "received quantities" Bill Control Policy is a hard or soft gate) is **independent** of this valuation-timing resolution — it's a control-authority question, not a posting-timing question — and remains open, still requiring AWT.

## Not established

Full runtime confirmation of the resolved architecture (documentation-tier convergent evidence is now strong, but no source/runtime access exists in this container — same constraint as every prior Gx). Lock Date specifics (who can override a Hard Lock, exact interaction with inventory dates) also remain undocumented at the depth needed for a control design.
