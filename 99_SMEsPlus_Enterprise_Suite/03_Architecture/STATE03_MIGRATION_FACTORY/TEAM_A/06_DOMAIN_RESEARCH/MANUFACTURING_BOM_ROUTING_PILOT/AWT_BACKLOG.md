> Domain: MANUFACTURING_BOM_ROUTING_PILOT | AWT Backlog | Not executable in this container

# AWT BACKLOG

### BRP-F03 — Subcontracting valuation (highest priority in this pilot; documentation pass complete 2026-09-29)

- **Criticality**: C1
- **Hypothesis to verify**: Sending components to a Subcontracting Location produces no valuation-account journal entry (only a location-to-location internal stock move); the subcontractor's returned finished good, once the vendor bill for the subcontracting fee is posted, produces an entry debiting the Finished Goods Valuation Account for component cost + fee.
- **Required environment**: Same Odoo 19 environment as Gx7's capstone, plus Subcontracting feature enabled, one subcontractor partner, one Subcontracting-type BoM.
- **Runtime action**: Send components to the Subcontracting Location; check Journal Entries (expect none). Receive the subcontracted finished good and post the subcontractor's vendor bill; check Journal Entries for the Finished Goods Valuation Account debit.
- **Expected observable result**: No entry at send; an entry at vendor-bill-posting time that reconciles component cost + the subcontractor fee from the vendor price field.
- **Evidence required**: Journal Entries at both steps; the specific account(s) touched.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: full runtime confirmation only — documentation-tier mechanism now identified.

### BRP-F08 — By-Products cost allocation (second priority)

- **Criticality**: C1
- **Hypothesis to verify**: total production cost is allocated between the primary finished good and its by-product(s) by some specific, discoverable method (proportional value share, a fixed by-product valuation with residual to the primary good, or another rule).
- **Required environment**: Same Odoo 19 environment, By-Products feature enabled, one BoM with a declared by-product.
- **Runtime action**: Complete an MO producing both primary good and by-product; inspect the valuation/cost breakdown for each.
- **Expected observable result**: A discoverable, consistent allocation rule between the two output products.
- **Evidence required**: Cost/valuation figures for both the primary good and the by-product from the same MO.
- **Target V**: V5 (floor V4) | **Current V**: **V1** (candidate default disclosed 2026-09-29 — `EV-BRP-13`/`EV-BRP-14`, third-party listing + pre-19 forum, not official-doc-confirmed for Odoo 19.0; not upgraded to V2) | **Missing proof**: `GAP-BRP-09` — Odoo-19-specific confirmation of the allocation method, and whether it matches the disclosed candidate default (zero-allocation-to-by-product).
- **Negative-case AWT scenario (documentation-tier design, added 2026-09-29)**: configure a BoM where the By-Product's own standalone market value exceeds the primary finished good's; complete an MO; inspect whether the by-product enters stock at zero/unset cost and whether the primary good absorbs 100% of production cost — this is the specific edge case the candidate default would predict, and the one most likely to surface a real financial-control problem if confirmed.

### BRP-F01 / F02 / F04 / F05 / F06 / F07 / F09

Lower priority — follow the same AWT shape as Gx7's routing/execution/config functions; fold into the same capstone session (already spans Gx1/2/4/5/6/7).

## Backlog status

```
FUNCTIONS WITH AWT PLAN PREPARED : 2 detailed (BRP-F03, BRP-F08) + 7 lower-priority (F01/F02/F04/F05/F06/F07/F09)
FUNCTIONS AWAITING DOCUMENTATION FIRST : 0
CAPSTONE SESSION NOW SPANS : Gx1, Gx2, Gx4, Gx5, Gx6, Gx7, MANUFACTURING_BOM_ROUTING_PILOT
```
