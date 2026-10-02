> Domain: SALES_DELIVERY_VALIDATION_PILOT (Gx2) | AWT Backlog | Not executable in this container

# AWT BACKLOG — Gx2 (Sales Delivery Validation)

### SDV-F05 — COGS / valuation timing at delivery (TOP PRIORITY — shared with Gx1 GRV-F04)

- **Criticality**: C1
- **Hypothesis to verify**: Resolve `GAP-SDV-01` / `GAP-GRV-01`(pilot cross-ref): does perpetual valuation post at physical movement time, or only at invoice/bill time via a Stock Variation buffer, in Odoo 19?
- **Required environment**: Odoo 19 Community, Inventory + Accounting + Sales apps, one Product Category set to Automatic/Perpetual + FIFO.
- **Configuration prerequisite**: A Sales Order for that product, confirmed but not yet invoiced.
- **Runtime action**: Validate the delivery; immediately check Accounting → Journal Entries (expect: none, if the invoice-timing claim is correct) and the Inventory Valuation report's Stock Variation line (expect: populated); then create and post the customer invoice; check Journal Entries again (expect: COGS entry now appears, if the invoice-timing claim is correct).
- **Expected observable result**: A clean before/after showing whether the COGS entry appears at delivery-validate or at invoice-post — this single test resolves the shared contradiction.
- **Cross-module observation**: Compare against the same test performed on the purchase-receipt side (Gx1 `GRV-F04`'s AWT entry) — run both in the same session for direct comparability.
- **Accounting/stock effect**: Primary target of this test.
- **Reversal scenario**: Reverse the invoice (credit note) after the COGS entry appears; confirm the Stock Variation/valuation accounts net back to zero.
- **Evidence required**: Journal entry timestamps/lists at each checkpoint; Inventory Valuation report snapshots.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: The core contradiction itself.

### SDV-F04 — Invoicing policy (ordered vs. delivered quantities)

- **Hypothesis to verify**: Under "delivered quantities" policy, invoice creation is structurally blocked (not just discouraged) before delivery.
- **Required environment**: Same as SDV-F05.
- **Configuration prerequisite**: A product set to "Invoice what is delivered."
- **Runtime action**: Confirm a Sales Order for that product; attempt to create an invoice before validating any delivery.
- **Expected observable result**: Invoice creation is blocked or produces a zero-quantity invoice, not a full one.
- **Cross-module observation**: Compare against GRV-F06's softer, informational-only purchase-side control.
- **Accounting/stock effect**: N/A directly (control-verification only).
- **Reversal scenario**: N/A.
- **Evidence required**: UI/error behavior on the blocked attempt.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: Confirmation that the gate is structural, not merely a UI nudge.

### SDV-F06 / SDV-F07 — Return mechanics (pre- and post-invoice)

- **Hypothesis to verify**: Pre-invoice returns use Reverse Transfer alone; post-invoice returns require Reverse Transfer + Credit Note, and the credit note's stock-valuation interaction needs observation.
- **Required environment**: Same as above, one delivered-and-invoiced Sales Order, one delivered-but-not-invoiced Sales Order.
- **Configuration prerequisite**: None beyond having both order states available to test.
- **Runtime action**: Attempt Reverse-Transfer-only return on each; observe where it succeeds (pre-invoice case) and where documentation predicts extra steps are needed (post-invoice case).
- **Expected observable result**: Pre-invoice case fully resolves via Reverse Transfer; post-invoice case requires the Credit Note step to reconcile.
- **Cross-module observation**: Whether the Credit Note amount auto-populates from original invoice/valuation (`GAP-SDV-05`).
- **Accounting/stock effect**: Both a stock reversal and (post-invoice case) a financial reversal.
- **Reversal scenario**: This function *is* the reversal scenario for SDV-F02.
- **Evidence required**: Step-by-step record of both paths.
- **Target V**: V4/V5 per function | **Current V**: V2 | **Missing proof**: Full runtime walkthrough of both paths.

### SDV-F01 / SDV-F02 / SDV-F03

Lower priority — same AWT shape as Gx1's GRV-F01/F02/F03 (routing configuration, physical execution, backorder mechanics), to be executed in the same environment session as the above once available, not separately prioritized.

## Backlog status

```
FUNCTIONS WITH AWT PLAN PREPARED : 7 (all Gx2 functions)
TOP PRIORITY (shared across Gx1+Gx2) : SDV-F05 / GRV-F04 valuation-timing contradiction
```

No item may be executed without the environment queued at `BGQ-04` in `00_Architecture_Governance/STATE03_BOSS_GATE_QUEUE.md`.
