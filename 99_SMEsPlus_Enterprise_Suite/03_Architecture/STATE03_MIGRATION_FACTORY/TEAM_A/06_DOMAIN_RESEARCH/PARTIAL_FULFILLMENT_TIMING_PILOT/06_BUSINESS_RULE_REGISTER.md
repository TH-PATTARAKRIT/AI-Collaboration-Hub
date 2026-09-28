> Domain: PARTIAL_FULFILLMENT_TIMING_PILOT (Gx5) | Business Trace | Documentation-Tier (PDT-F03 partly forum-tier, flagged)

# 06 — BUSINESS RULE REGISTER (Gx5)

### PDT-F01 — Per-shipment invoicing alignment (sales)

- **WHAT**: Under "Invoice what is delivered," as soon as any partial delivery is confirmed, invoice creation becomes available for that delivered quantity — it does not wait for the full order to be fulfilled.
- **WHY**: Businesses need to bill for what was actually shipped as it ships, especially on long-running orders with staged fulfillment.
- **BUSINESS RULE**: A fully-backordered sales order produces multiple invoices — one per delivery — not one invoice deferred to final completion.
- **STATE**: Partial delivery validated → invoice creatable immediately (UI: Create Invoice button becomes active/"purple") → invoice created for that partial quantity only.
- **DATA CONCEPT**: Each invoice is scoped to a specific delivery's delivered quantity, not the order's total ordered quantity.
- **CONTROL**: This is a *per-event* alignment — financial recognition timing tracks physical timing at the shipment level, not the order level.
- **DEPENDENCY**: Builds on SDV-F03 (backorder creation) — each backorder, once itself delivered, triggers its own invoice cycle.
- **EVENT**: "Invoice created" (per delivery).
- **RISK**: A design assuming invoicing is batched to full-order completion would be wrong under this policy — each partial event is its own financial trigger.
- **UNKNOWN**: Whether this per-shipment alignment also determines COGS timing (i.e., does GAP-SDV-01's "posts at invoice time" apply per-partial-invoice too) — not confirmed, but consistent with that hypothesis if true.

### PDT-F02 — Per-receipt billing alignment (purchase)

- **WHAT**: Multiple bills may be issued against the same PO as partial receipts occur, linked by a shared **Bill Reference** field rather than a rigid one-bill-per-PO structure.
- **WHY**: Mirrors PDT-F01 — vendors may invoice as they ship, or per partial receipt.
- **BUSINESS RULE**: "Multiple bills for the same purchase order may be issued if the vendor is on back-order and sends invoices as products are shipped... multiple bills may have the same Bill Reference."
- **STATE**: Partial receipt validated → draft bill creatable for that portion (under "received quantities" policy) → multiple such bills accumulate against one PO.
- **DATA CONCEPT**: Bill Reference is the reconciliation key across multiple bills for one PO, not a strict database foreign key relationship implied by documentation alone.
- **CONTROL**: Draft bills can also be edited to change billed quantity/price/add products — same "Exception" flagging behavior as Gx1's `GRV-F06` applies here too.
- **DEPENDENCY**: Builds on GRV-F03 (backorder) and GRV-F06 (bill control policy).
- **EVENT**: "Bill created" (per partial receipt, potentially).
- **RISK**: If Bill Reference is only a label (not an enforced link), reconciliation across partial bills could rely on manual diligence rather than system enforcement — not evidenced either way.
- **UNKNOWN**: Whether the system itself sums/validates that total billed quantity across all bills sharing a reference does not exceed total received/ordered — `SOURCE/RUNTIME VERIFICATION REQUIRED`.

### PDT-F03 — Bill-before-receipt anomaly

- **WHAT**: A community-reported case describes Odoo 19 permitting vendor-bill creation for a PO **before** any product has been received, despite the Bill Control Policy being set to "received quantities" — which per Gx1's `GRV-F06` documentation should require at least partial receipt first.
- **WHY** (of the anomaly, not a business rule): Not explained in the source — this is a reported discrepancy, not a documented design.
- **BUSINESS RULE**: **Evidence-tier caveat**: this is a community forum question, not official documentation — lower confidence than every other finding in this Deep Study so far. It is recorded because it directly corroborates (rather than merely echoes) Gx1's independently-derived `CQS-GRV-04` finding that the "received quantities" control is not confirmed as a hard block.
- **STATE**: PO confirmed, zero receipt → bill creation apparently still possible (per the report).
- **DATA CONCEPT**: N/A — insufficient detail in the source.
- **CONTROL**: If confirmed by runtime testing, this would mean the Bill Control Policy is, in practice, advisory/soft even in its "received quantities" mode — a materially different conclusion than a naive reading of Gx1's own documentation evidence would suggest.
- **DEPENDENCY**: Directly tied to `GRV-F06`.
- **EVENT**: N/A.
- **RISK**: If a target design assumes "received quantities" policy is a hard, enforced gate based on documentation alone, this forum report (if runtime-confirmed) would falsify that assumption.
- **UNKNOWN**: Whether this is a genuine control gap, a role/permission override, a user configuration error on the reporter's part, or a version-specific behavior — entirely unconfirmed; must not be treated as established fact from a forum post alone.

### PDT-F04 — Cross-shipment quantity/bill reconciliation

- **WHAT**: The mechanism (Bill Reference) by which multiple partial bills against one PO are kept associated with each other and, implicitly, with the PO's total ordered/received quantity.
- **WHY**: Without this, partial billing would risk double-counting or losing track of what remains to be billed.
- **BUSINESS RULE**: Documented only as a shared reference field; no documented automatic total-reconciliation check was found.
- **STATE / DATA CONCEPT / CONTROL / DEPENDENCY / EVENT**: See PDT-F02 — this function is the reconciliation half of that same mechanism, not evidenced as a separate distinct feature.
- **RISK**: Same as PDT-F02's risk — absence of confirmed automatic reconciliation is itself the finding.
- **UNKNOWN**: Whether any system-level total check exists — `SOURCE/RUNTIME VERIFICATION REQUIRED`.
