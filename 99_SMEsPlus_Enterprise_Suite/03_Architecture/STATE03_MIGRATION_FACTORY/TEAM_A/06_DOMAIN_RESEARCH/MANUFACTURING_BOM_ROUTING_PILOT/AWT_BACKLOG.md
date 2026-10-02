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
- **Hypothesis to verify, refined 2026-09-30 (source-code tier, Handoff `D-01`)**: total production cost is allocated between the primary finished good and its by-product(s) via a user-set, per-line Cost Share (%) — not an automatic computation from market value/quantity/weight. By-Product = total cost × %÷100 ÷ qty; primary good absorbs the remainder. Leaving Cost Share at 0% (no forced-100% rule, no warning) reproduces the originally-hypothesized "zero-allocation" risk as a configuration outcome, not a hard default.
- **Required environment**: Same Odoo 19 environment, By-Products feature enabled, one BoM with a declared by-product.
- **Runtime action**: Complete an MO producing both primary good and by-product with Cost Share explicitly set; repeat with Cost Share left at 0%; repeat again mixing a Standard-costed By-Product with a FIFO-costed primary good; inspect the valuation/cost breakdown for each run.
- **Expected observable result**: A discoverable, consistent allocation rule between the two output products, matching the source-level formula above; a value/cost inconsistency specifically in the mixed-costing-method run.
- **Evidence required**: Cost/valuation figures for both the primary good and the by-product from each MO run.
- **Target V**: V5 (floor V4) | **Current V**: **V1 documentation-tier** (source/dump finding received 2026-09-30, `SOURCE/DUMP FINDING — CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION`, `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET` — not a V-level upgrade) | **Missing proof**: `GAP-BRP-09` — runtime confirmation of the Cost Share mechanism, the Standard/FIFO-mixed edge case, Unbuild reversal behavior, and Subcontracting interaction (none runtime-confirmed).
- **Negative-case AWT scenario (refined 2026-09-30)**: (a) a BoM where the By-Product's own standalone market value exceeds the primary finished good's, Cost Share left at 0% — inspect whether the by-product enters stock at zero/unset cost and the primary good absorbs 100% of production cost; (b) a By-Product costed Standard alongside a FIFO-costed primary good — inspect whether the posted total reconciles to actual production cost or leaves a residual on the Production location's account; (c) Unbuild an MO with a By-Product and inspect the reversed values (Odoo's own relevant test is commented out in source — no design-level evidence either way).

### BRP-F01 / F02 / F04 / F05 / F06 / F07 / F09

Lower priority — follow the same AWT shape as Gx7's routing/execution/config functions; fold into the same capstone session (already spans Gx1/2/4/5/6/7).

## Backlog status

```
FUNCTIONS WITH AWT PLAN PREPARED : 2 detailed (BRP-F03, BRP-F08) + 7 lower-priority (F01/F02/F04/F05/F06/F07/F09)
FUNCTIONS AWAITING DOCUMENTATION FIRST : 0
CAPSTONE SESSION NOW SPANS : Gx1, Gx2, Gx4, Gx5, Gx6, Gx7, MANUFACTURING_BOM_ROUTING_PILOT
```
