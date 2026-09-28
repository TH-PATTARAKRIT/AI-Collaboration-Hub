> Domain: INVENTORY_ADJUSTMENT_VALIDATION_PILOT (Gx4) | AWT Backlog | Not executable in this container

# AWT BACKLOG — Gx4

### IAV-F03 — Financial posting timing (joins the shared cross-Gx priority test)

- **Criticality**: C1
- **Hypothesis to verify**: An applied inventory adjustment posts a GL entry immediately and unconditionally, regardless of the product category's valuation mode — unlike (per current documentation-tier understanding) a receipt or delivery.
- **Required environment**: Same as Gx1/Gx2, plus a product with a known counted-quantity discrepancy.
- **Configuration prerequisite**: One product category each in Manual and Automatic valuation mode, to test whether IAV-F03 behaves the same in both (unlike GRV-F04, which is documented as mode-dependent).
- **Runtime action**: Apply a count adjustment under each valuation mode; check Journal Entries immediately after.
- **Expected observable result**: If the "immediate, no additional steps" claim is unconditional, a journal entry appears in BOTH modes immediately — a genuine structural difference from GRV-F04/SDV-F05's deferral pattern.
- **Cross-module observation**: Run in the same session as the GRV-F04/SDV-F05 AWT tests for direct three-way comparison.
- **Accounting/stock effect**: Primary target.
- **Reversal scenario**: See IAV-F06 (undocumented — test whatever mechanism, if any, is discovered).
- **Evidence required**: Journal entries under both valuation modes.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: The mode-dependency question itself.

### IAV-F04 — Scrap / Loss Account

- **Hypothesis to verify**: Scrap posting requires and uses a dedicated Loss Account when configured, and falls back to the general valuation account when not.
- **Required environment**: Same, plus a location typed Inventory Loss, tested with and without a Loss Account set.
- **Runtime action**: Scrap the same product/quantity under each location configuration; check Journal Entries / P&L report placement.
- **Expected observable result**: Distinct P&L line when Loss Account is set; blended into general valuation otherwise.
- **Evidence required**: Journal entries and P&L report snapshots under both configurations.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: Full runtime confirmation.

### IAV-F01 / F02 / F05 / F06

Lower priority — F01/F02/F05 follow the same AWT shape as other Gx's routing/execution/config functions; F06 has no documentation-tier hypothesis yet (`GAP-IAV-02`) and needs a documentation pass before an AWT plan can be written.

## Backlog status

```
FUNCTIONS WITH AWT PLAN PREPARED : 2 detailed (IAV-F03, IAV-F04) + 3 lower-priority (F01/F02/F05)
FUNCTIONS AWAITING DOCUMENTATION FIRST : 1 (IAV-F06)
```
