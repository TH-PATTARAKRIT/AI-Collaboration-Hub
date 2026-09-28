> Domain: PARTIAL_FULFILLMENT_TIMING_PILOT (Gx5) | Documentation-Tier

# 01 — EXECUTIVE RESEARCH SUMMARY (Gx5)

## Scope

Four functions (`04_FUNCTION_REGISTER.md`), narrowly focused on timing consistency between a partial physical event and its financial recognition — not backorder mechanics (already covered).

## Material finding 1 — sales side: per-shipment invoicing is documented as immediate, not deferred

Documentation states that once at least a partial delivery is confirmed, invoice creation becomes available immediately ("Create Invoice button is now purple"), and that a fully-backordered order produces **two separate invoices, one per delivery** — not one invoice held until full completion. This is a genuine timing-consistency data point: quantity and financial timing are aligned *per partial event*, not batched to completion, on the sales side under "Invoice what is delivered."

## Material finding 2 — purchase side: a documented real-world anomaly directly corroborates Gx1's open question

A community-reported issue asks why Odoo 19 allows creating a bill for a PO **before** the product is received, despite the Bill Control Policy being set to "received quantities." This is not official documentation (it is a forum question, evidence-tier accordingly lower), but it **directly corroborates** Gx1's `CQS-GRV-04` finding that three-way matching/bill-control is a softer control than a hard block. Recorded as reinforcing evidence, not proof — the underlying mechanism is still not runtime-confirmed.

## Material finding 3 — multiple bills per PO tracked by a shared reference, not a hard 1:1 link

"Multiple bills for the same purchase order may be issued if the vendor is on back-order... multiple bills may have the same Bill Reference" — quantity reconciliation across partial receipts/bills relies on this shared reference field, a cross-shipment reconciliation mechanism worth flagging for `PDT-F04`.

## Not established

Full runtime confirmation of any of the above, and specifically whether the purchase-side bill-before-receipt behavior is a genuine control gap, a role-based override, or a documentation/version discrepancy.
