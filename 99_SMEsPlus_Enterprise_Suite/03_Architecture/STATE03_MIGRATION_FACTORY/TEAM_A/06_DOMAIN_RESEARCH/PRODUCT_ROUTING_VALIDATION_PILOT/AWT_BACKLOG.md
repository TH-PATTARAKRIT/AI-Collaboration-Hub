> Domain: PRODUCT_ROUTING_VALIDATION_PILOT (Gx8) | AWT Backlog | Not executable in this container

# AWT BACKLOG — Gx8

### RTG-F02 / RTG-F03 — join the shared cross-Gx capstone session (add a Consumable case)

- **Criticality**: C1
- **Hypothesis to verify**: A Consumable-type purchase expenses at vendor-bill time with zero stock-valuation-account activity at any point; a Storable purchase/sale continues to follow the Gx6/Gx2 model.
- **Required environment**: Same as the existing capstone session, plus one product configured as Goods + Track Inventory OFF.
- **Runtime action**: Purchase and receive the Consumable product; confirm no stock valuation entry is ever created, only an expense entry at vendor-bill posting.
- **Expected observable result**: Clean, single expense entry, no interim stock account activity at all — the simplest case in the whole capstone test.
- **Cross-module observation**: Direct contrast against the Storable case in the same session.
- **Evidence required**: Journal entries (or explicit absence) for the Consumable case.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: Runtime confirmation, low-risk given how clean the documentation-tier evidence already is.

## Backlog status

```
FUNCTIONS WITH AWT PLAN PREPARED : 2 (RTG-F02, RTG-F03 — added to existing capstone session)
CAPSTONE SESSION NOW SPANS : Gx1, Gx2, Gx4, Gx5, Gx6, Gx7, Gx8
```
