> Domain: SALES_DELIVERY_VALIDATION_PILOT (Gx2) | Carry-forward / Re-audit Matrix | READ ONLY

# BASELINE CARRY-FORWARD / RE-AUDIT MATRIX (Gx2)

| Existing Asset | Path | Status | Reasoning |
|---|---|---|---|
| Gx1 (Goods Receipt Validation) findings | `../GOODS_RECEIPT_VALIDATION_PILOT/` | **Reusable, with one flagged contradiction** | Same methodology and evidence tier; GRV-F04 (valuation timing) is now cross-referenced against this Gx's GAP-SDV-01 rather than assumed consistent. |
| Accounting↔Inventory Backbone Roadmap | `00_Architecture_Governance/STATE03_ACCOUNTING_INVENTORY_BACKBONE_EXECUTION_ROADMAP.md` | **Reusable** | Lane C scenario 2 is this Gx's exact scope; scenario 3 (Return/Reversal) is partially covered here too (SDV-F06/F07) since delivery-side returns are documentation-adjacent. |
| GROUP_01_SALES_INVENTORY_PURCHASE Team A research | `TEAM_A/06_DOMAIN_RESEARCH/GROUP_01_SALES_INVENTORY_PURCHASE/` | **Needs Reconciliation — same condition as Gx1's BASELINE_CARRY_FORWARD.md** | Only session-prompt files present at this working-tree path; per Gx1's finding, a parallel unmerged branch (`claude/group-a-sales-inventory-purchase-dr002` @ `8b0993d8...`) exists but was not opened this round either. Not reused as content here; flagged once, not re-investigated per-Gx to avoid duplicate PMO asks (Boss order §9). |
| Inventory Core Backbone lineage reconciliation | `../INVENTORY_CORE_BACKBONE/03_LINEAGE_RECONCILIATION_DR002_TO_PRESENT.md` | **Reusable (by reference)** | Same disposition as recorded for Gx1: full lineage traced, canonical candidate recommended, not used as content input to this Gx's own documentation-tier findings. |
