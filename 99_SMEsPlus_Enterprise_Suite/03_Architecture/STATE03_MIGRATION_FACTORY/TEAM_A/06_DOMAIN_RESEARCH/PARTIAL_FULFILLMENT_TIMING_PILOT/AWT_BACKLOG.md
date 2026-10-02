> Domain: PARTIAL_FULFILLMENT_TIMING_PILOT (Gx5) | AWT Backlog | Not executable in this container

# AWT BACKLOG — Gx5

### PDT-F03 — Bill-before-receipt anomaly (CHEAPEST HIGH-VALUE TEST IN THE BACKLOG)

- **Criticality**: C1
- **Hypothesis to verify**: A vendor bill can be created/validated before any receipt exists, even with Bill Control Policy = "received quantities."
- **Required environment**: Same as Gx1, Purchase app, Bill Control Policy = "received quantities."
- **Configuration prerequisite**: None beyond that policy setting.
- **Runtime action**: Confirm a PO with zero receipt; attempt to create a vendor bill directly.
- **Expected observable result**: Either blocked (documentation's naive reading) or permitted (forum report's claim) — a single quick test resolves this.
- **Cross-module observation**: If permitted, check whether the bill's `Should Be Paid`/three-way-match flag reflects the discrepancy.
- **Accounting/stock effect**: If permitted, whether any valuation/COGS entry is also created despite no stock movement.
- **Reversal scenario**: N/A.
- **Evidence required**: Simple pass/fail observation.
- **Target V**: V5 (floor V4) | **Current V**: V1 | **Missing proof**: Everything — but this is the single cheapest test to run once an environment exists.

### PDT-F01 / PDT-F02 (join the shared cross-Gx valuation-timing test)

- **Hypothesis to verify**: Per-partial-shipment invoicing/billing also determines per-partial COGS/valuation posting timing (testing `GAP-PDT-03`'s hypothesis directly).
- **Required environment**: Same as the combined Gx1/Gx2/Gx4 valuation-timing test session.
- **Runtime action**: In that same session, additionally split a delivery/receipt into two partials and check whether each partial's invoice/bill independently triggers its own COGS/valuation entry, or whether they're batched.
- **Evidence required**: Journal entries per partial event.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: Full runtime walkthrough, ideally combined with the Gx1/Gx2/Gx4 test session for efficiency.

### PDT-F04

Lower priority — bundle with PDT-F02's test session; check whether over-billing across partials is blocked.

## Backlog status

```
FUNCTIONS WITH AWT PLAN PREPARED : 4 (all)
CHEAPEST TEST IN ENTIRE DEEP STUDY SO FAR : PDT-F03 (single boolean observation)
```
