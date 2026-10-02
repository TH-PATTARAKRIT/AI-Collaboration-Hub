# U169 — stock: Physical Inventory Count and Quant Adjustment — NEUTRAL KNOWLEDGE
**Unit**: U169 | **Group**: G06/G01 | **Priority**: P1 | **Module Status**: PRESENT
**Odoo Version**: 19.0 Community | **Date**: 2026-10-02

---

## PURPOSE SUMMARY

The physical inventory count mechanism allows warehouse staff to reconcile the quantities the system believes are on the shelves against what is physically present. When discrepancies are found, the system creates internal stock movements that silently correct the on-hand figures; for businesses using automated costing, those movements also produce accounting journal entries. The entire mechanism is built into the stock unit records themselves — there is no separate inventory order or session document.

---

## NEUTRAL CLAIMS (22)

| # | Claim ID | Boundary | Plain-Language Description |
|---|----------|----------|---------------------------|
| 1 | U169-N01 | Count initiation | A physical inventory count is started by opening the Physical Inventory screen. The system displays all on-hand stock records for internal and transit locations in an editable list. There is no separate inventory order to create or open; the count is performed inline on the stock records. |
| 2 | U169-N02 | Inventory mode | The editing rights for counted quantities are gated by a system flag called inventory mode. Only users who belong to the stock user group can set this flag, and only while in the Physical Inventory screen. |
| 3 | U169-N03 | Counted quantity | Each stock record carries a separate field for the quantity a user physically counted. This field is empty (zero) by default and is independent of the system-tracked on-hand quantity. |
| 4 | U169-N04 | Count flag | When a user enters a counted quantity, the record is automatically marked as participating in the current count. This flag is what the system uses to know which records to include when the count is applied. Records where no count has been entered are not touched. |
| 5 | U169-N05 | Difference field | The system automatically computes the gap between the counted quantity and the system on-hand quantity. A positive gap means the physical shelf has more than the system expects (surplus); a negative gap means the shelf has less (shrinkage). The gap is shown in the count screen and used to generate the correcting movements. |
| 6 | U169-N06 | Conflict detection | If a stock movement (a delivery, receipt, or internal transfer) is processed for a product while its count is in progress, the system marks that count record as outdated. When the user tries to apply an outdated count, a conflict resolution screen appears before any correction is made. |
| 7 | U169-N07 | Applying the count | When the user applies the count, the system creates one correcting stock movement per counted record. These movements are immediately validated; there is no separate confirmation step. The count flag is cleared once the movements are done. |
| 8 | U169-N08 | Correcting movement direction | For a surplus, the correcting movement runs from the virtual Inventory Loss location into the physical storage location, increasing on-hand stock. For shrinkage, the movement runs the other direction, reducing on-hand stock. |
| 9 | U169-N09 | Inventory Loss location | Every company has a dedicated virtual location called Inventory Loss (or Inventory Adjustment). It exists solely to serve as the counterpart for correcting movements. Stock sent to or received from this location does not represent real physical flow; it is an accounting device. |
| 10 | U169-N10 | Per-product loss location | Each product template can have its own designated Inventory Loss location, overriding the company default. This allows different product categories to post their adjustments to different virtual counterpart locations if the business requires it. |
| 11 | U169-N11 | Real-time valuation: journal entry | For products configured with automated costing (real-time valuation), applying a physical count creates a financial journal entry in addition to the stock movement. A surplus increases the stock asset balance and charges an inventory adjustment expense; a shrinkage does the reverse. |
| 12 | U169-N12 | Journal entry condition | A journal entry is only created if the inventory adjustment location has an expense account assigned to it. Without that account assignment, the stock quantities are corrected but no accounting entry is generated. |
| 13 | U169-N13 | Accounting date | Stock accountants can specify an accounting date on the count records before applying them. When set, the resulting journal entry is posted in the chosen accounting period rather than the current date. This supports period-end adjustments. |
| 14 | U169-N14 | Standard price account | For Standard Price products, the correcting journal entry uses the product category's stock valuation account as the asset side and the inventory adjustment location's expense account as the counterpart. FIFO and Average Cost products use the same pattern but the asset value is drawn from the current cost. |
| 15 | U169-N15 | Lot-level granularity | Stock records are individually tracked per lot or serial number. A physical count can therefore record a different quantity for each lot of the same product in the same location. The correcting movement carries the lot reference, so inventory history remains fully traceable by lot. |
| 16 | U169-N16 | Package support | When stock is stored in packages, the correcting movement preserves the package assignment, so the package quantity in the system matches what was counted inside the box. |
| 17 | U169-N17 | Location-level cycle count frequency | Each physical storage location can be assigned an inventory count frequency in days. When non-zero, the system calculates a next-count date for every stock record in that location after each count is applied. |
| 18 | U169-N18 | Annual inventory date | At the company level, an annual inventory month and day can be configured. For locations that have no cycle count frequency, the system uses this company date as the next-count reminder. |
| 19 | U169-N19 | No automatic trigger | The system never automatically starts or applies a count. The count frequency settings and annual date only update reminder dates visible in the inventory screen; warehouse staff must open the screen and apply the count manually. |
| 20 | U169-N20 | No lock during count | The system does not prevent other stock operations from processing during an active count. If a movement is processed against a product being counted, the conflict detection mechanism marks the count record as outdated rather than blocking the movement. |
| 21 | U169-N21 | Apply-all path | In addition to applying counts record by record, a user can apply all flagged records in the current screen at once using an Apply All action. This presents a wizard where a reference label can be entered for traceability. |
| 22 | U169-N22 | Auto-apply shortcut | For barcode-driven or bulk workflows, a fast-apply mode exists where entering a quantity immediately triggers the correction without a separate apply step. This path is intended for cycle count workflows where counts are applied as they are scanned, rather than staged and reviewed first. |

---

## MIGRATION IMPACT NOTES

1. **No stock.inventory model**: The `stock.inventory` model was abolished in Odoo 16. Any migration from Odoo 14 or earlier that references `stock.inventory`, `stock.inventory.line`, or the `_action_start_inventory()` / `action_done()` cycle must be redesigned. Counts are now direct operations on `stock.quant`.

2. **inventory_quantity_count field does not exist**: Some Odoo documentation from earlier versions references an `inventory_quantity_count` computed field on stock.quant. This field does not exist in Odoo 19 Community. Use a `search([('inventory_quantity_set', '=', True)])` count instead.

3. **accounting_date field is stock_account-only**: The `accounting_date` field on `stock.quant` (for period-specific JE posting) is added by the `stock_account` module. It does not exist in a pure-stock (no valuation) installation.

4. **Inventory Loss location per company**: When adding a new company, `create_missing_inventory_loss_location()` must be triggered. If not run, `_apply_inventory()` falls back to the company-level `ir.default` for `property_stock_inventory`. A missing default causes a validation error on apply.

5. **Real-time valuation JE gated by valuation_account_id**: For automated costing products, journal entries are only created if `stock.location.valuation_account_id` is set on the inventory loss location. A fresh installation without a configured chart of accounts will silently skip the JE even for real_time products. This is a common oversight in clean-room migrations.
