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

### MFG-F05 — Negative-inventory revaluation (documentation pass partial, version tension open)

- **Hypothesis to verify — two competing versions, must be disambiguated, not assumed**: (a) pre-19: negative-inventory MO consumption later triggers a "Revaluation of WH/MO/XXX" journal entry once real cost is known; (b) Odoo 19: no such automatic entry — cost is booked only at vendor-bill posting.
- **Required environment**: Odoo 19 specifically (not 17/18) — a BOM whose component goes negative on-hand during an MO, then is later replenished.
- **Runtime action**: Confirm an MO consuming a negative-on-hand component; replenish the component via a vendor bill; check Journal Entries for any "Revaluation of WH/MO/XXX" entry.
- **Expected observable result**: If (b) is correct, no such entry appears — cost is fully captured at vendor-bill time instead. If (a) still holds in 19, the entry appears as described.
- **Evidence required**: Journal Entries across the full sequence (negative consumption → replenishment/bill).
- **Target V**: V5 (floor V4) | **Current V**: V1 | **Missing proof**: Full runtime confirmation — this is now the single highest-value AWT case in this pilot, since it directly bears on whether the cross-Gx valuation-timing Material Finding needs a negative-inventory exception.

## Backlog status

```
FUNCTIONS WITH AWT PLAN PREPARED : 5 (MFG-F01, F02, F03, F04, F05)
FUNCTIONS AWAITING DOCUMENTATION FIRST : 0
CAPSTONE SESSION NOW SPANS : Gx1, Gx2, Gx4, Gx5, Gx6, Gx7
```
