> Domain: MANUFACTURING_VALUATION_PILOT (Gx7) | AWT Backlog | Not executable in this container

# AWT BACKLOG — Gx7

### MFG-F01 / MFG-F02 — join the shared cross-Gx capstone session

- **Criticality**: C1
- **Hypothesis to verify**: Consumption and completion post automatically under Automated valuation, unconditionally (no invoice dependency, unlike receipts/deliveries).
- **Required environment**: Same as the Gx1/2/4/5/6 combined session, plus Manufacturing app, a simple one-level BOM, Production location with WIP account configured.
- **Runtime action**: Confirm an MO, consume components, mark Done; check Journal Entries at each step.
- **Expected observable result**: Entry at consumption (component valuation → WIP), entry at completion (WIP + labor → finished good) — both immediate, no invoice needed.
- **Cross-module observation**: Compare directly against the receipt/delivery/adjustment results in the same session — this is the fourth and clearest confirmation of the unifying rule.
- **Accounting/stock effect**: Primary target.
- **Reversal scenario**: Scrap or cancel the MO; observe reversal behavior.
- **Evidence required**: Journal entries at consumption and completion.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: Runtime confirmation.

### MFG-F05 — Negative-inventory revaluation (documentation pass needed first)

- Not ready for an AWT hypothesis — `GAP-MFG-01` must close first.

## Backlog status

```
FUNCTIONS WITH AWT PLAN PREPARED : 4 (MFG-F01, F02, F03, F04)
FUNCTIONS AWAITING DOCUMENTATION FIRST : 1 (MFG-F05)
CAPSTONE SESSION NOW SPANS : Gx1, Gx2, Gx4, Gx5, Gx6, Gx7
```
