> Domain: SALES_DELIVERY_VALIDATION_PILOT (Gx2) | Documentation-Tier

# 01 — EXECUTIVE RESEARCH SUMMARY

## Why this Gx

`STATE03_ACCOUNTING_INVENTORY_BACKBONE_EXECUTION_ROADMAP.md` Lane C scenario 2: *"Stockable Sales Delivery -> Stock Truth -> Cost / Valuation Handoff -> Accounting effect."* The natural mirror of Gx1 (Purchase Receipt) on the outbound side, and the scenario most likely to expose the same valuation-timing question from the opposite direction.

## What was established (documentation-tier)

Seven candidate functions (`04_FUNCTION_REGISTER.md`): delivery routing configuration, physical delivery execution, partial delivery/backorder handling, invoicing policy (ordered vs. delivered quantities) as a financial-control gate, COGS/valuation timing at delivery, pre-invoice returns via Reverse Transfer, and post-invoice returns via Credit Note.

## Material finding — a genuine cross-Gx contradiction, not just a new fact

Documentation search surfaced a specific, repeated claim: **"Since Odoo 19, the Perpetual method impacts the stock valuation account at the invoice level"** and **"Odoo 19 no longer creates journal entries upon the physical receipt or delivery of goods... shifted to invoice posting."** This directly narrows or contradicts Gx1's `GRV-F04` finding, which (drawing on a more generic "Automatic inventory valuation" page) recorded perpetual valuation as posting "in real time whenever stock enters or leaves the warehouse" — i.e., at the *movement*, not the *invoice*. Both claims cite genuine Odoo 19 documentation pages; they were not cross-checked against each other in Gx1 because Gx1 did not yet have a delivery-side or COGS-specific search pass. This is recorded as `GAP-SDV-01` (Evidence Conflict) rather than silently resolved in either direction — per Master Prompt §2.7 and Boss's order §12 ("never infer away a contradiction").

## What was NOT established

No source/runtime access (same constraint as Gx1). No AWT performed — `AWT_BACKLOG.md` prepared instead. The valuation-timing contradiction above is specifically flagged as requiring runtime confirmation, not documentation-only resolution, since both claims are documentation-tier and mutually narrowing rather than one being obviously wrong.

## Recommendation

Fit for continued documentation-tier work. The valuation-timing contradiction (GAP-SDV-01) should be the **first** AWT unit executed once an environment is authorized (`BGQ-04`), since it affects both Gx1 and Gx2's C1 functions simultaneously.
