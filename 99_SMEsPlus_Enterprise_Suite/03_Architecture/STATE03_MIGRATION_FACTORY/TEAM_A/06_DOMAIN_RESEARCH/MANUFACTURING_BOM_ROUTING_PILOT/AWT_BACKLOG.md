> Domain: MANUFACTURING_BOM_ROUTING_PILOT | AWT Backlog | Not executable in this container

# AWT BACKLOG

### BRP-F03 — Subcontracting valuation (highest priority in this pilot)

- **Criticality**: C1
- **Hypothesis to verify**: Sending components to a Subcontracting Location produces no valuation-account journal entry (only a location-to-location internal stock move); the subcontractor's returned finished good produces a valuation entry that includes some captured subcontractor fee/cost.
- **Required environment**: Same Odoo 19 environment as Gx7's capstone, plus Subcontracting feature enabled, one subcontractor partner, one Subcontracting-type BoM.
- **Runtime action**: Send components to the Subcontracting Location; check Journal Entries (expect none). Receive the subcontracted finished good; check Journal Entries for the fee-capture mechanism.
- **Expected observable result**: No entry at send; an entry at receipt that reconciles component cost + a distinguishable subcontractor-fee component.
- **Evidence required**: Journal Entries at both steps; the specific account(s) touched at receipt.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: `GAP-BRP-03` — the fee-capture mechanism specifically.

### BRP-F01 / F02 / F04 / F05

Lower priority — follow the same AWT shape as Gx7's routing/execution/config functions; fold into the same capstone session (already spans Gx1/2/4/5/6/7).

## Backlog status

```
FUNCTIONS WITH AWT PLAN PREPARED : 1 detailed (BRP-F03) + 4 lower-priority (F01/F02/F04/F05)
FUNCTIONS AWAITING DOCUMENTATION FIRST : 0
CAPSTONE SESSION NOW SPANS : Gx1, Gx2, Gx4, Gx5, Gx6, Gx7, MANUFACTURING_BOM_ROUTING_PILOT
```
