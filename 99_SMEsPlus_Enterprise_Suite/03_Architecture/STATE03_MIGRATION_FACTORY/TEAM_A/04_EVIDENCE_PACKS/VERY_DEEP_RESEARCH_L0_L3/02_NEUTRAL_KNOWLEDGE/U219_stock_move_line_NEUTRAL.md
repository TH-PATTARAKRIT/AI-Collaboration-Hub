# U219 — Stock Move Line: Neutral Knowledge Base

**Unit**: U219
**Module**: Stock Move Line
**Source SHA256**: `bdab636fdc5ef1377242ec66c25a3a48a1aafcbd2da3859f5a55ba838733cf88`
**Claims**: 20

---

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U219-C01 | MODEL-DECL | stock/models/stock_move_line.py:15-19 | class StockMoveLine | FIELD | Always | STABLE | The detailed product move line model is named "stock.move.line" and records are sorted by destination package descending then by identifier ascending | Inventory transfer detail line model |
| U219-C02 | FIELD-QUANTITY | stock/models/stock_move_line.py:37-39 | quantity field | FIELD | Always | MIGRATION-FLAG | The single quantity field on a move line holds both the done quantity and the reserved quantity; it replaces the separate done-quantity field and reserved-quantity field that existed before version 16 | Move line done or reserved amount field |
| U219-C03 | FIELD-QTY-BASE | stock/models/stock_move_line.py:40-42 | quantity_product_uom field | FIELD | Always | STABLE | A stored computed field converts the move line quantity to the product base unit of measure and is kept in sync whenever the quantity or unit of measure changes | Move line quantity in product base unit |
| U219-C04 | FIELD-LOT-ID | stock/models/stock_move_line.py:48-50 | lot_id field | FIELD | Always | STABLE | The lot or serial number field is a relational reference to an existing tracking record and is domain-filtered to the same product as the move line | Move line existing lot or serial reference |
| U219-C05 | FIELD-LOT-NAME | stock/models/stock_move_line.py:51 | lot_name field | FIELD | When picking type allows new lot creation | STABLE | The lot name text field is a staging area for auto-creating a new tracking record at transfer validation; it is replaced by the relational reference once the record is created | Move line new lot name staging field |
| U219-C06 | FIELD-PKG-SRC | stock/models/stock_move_line.py:44-47 | package_id field | FIELD | Always | STABLE | The source package field holds the package from which products are taken and is domain-restricted to packages located at the source location | Move line source package field |
| U219-C07 | FIELD-PKG-DEST | stock/models/stock_move_line.py:52-56 | result_package_id field | FIELD | Always | STABLE | The destination package field holds the package into which products are placed at the destination location and drives both putaway strategy selection and quant attribution | Move line destination package field |
| U219-C08 | FIELD-STATE | stock/models/stock_move_line.py:83 | state field | FIELD | Always | STABLE | The state field on a move line is a stored relation to the parent stock move state and carries no independent lifecycle of its own | Move line state derived from parent move |
| U219-C09 | FIELD-DATE | stock/models/stock_move_line.py:60-62 | date field | FIELD | Always | STABLE | The date field is initialised to the creation timestamp and is automatically updated to the current time when the quantity increases on a picked line or when the transfer is validated | Move line timestamp field |
| U219-C10 | FIELD-OWNER | stock/models/stock_move_line.py:64-67 | owner_id field | FIELD | When inventory owner differs from company | STABLE | The owner field identifies the partner whose inventory is being consumed and is passed through to all quant reservation and availability update operations | Move line inventory owner field |
| U219-C11 | ACTION-DONE-VALIDATION | stock/models/stock_move_line.py:615-647 | _action_done method | BEHAVIOR | During transfer validation | STABLE | Before moving any quants, the validation step checks rounding precision and collects tracked lines that lack a lot or serial reference for error reporting | Transfer validation pre-check step |
| U219-C12 | ACTION-DONE-LOT-CREATE | stock/models/stock_move_line.py:649-676 | _action_done method | BEHAVIOR | When lot name is set and picking type allows new lots | STABLE | During validation the system searches for an existing lot matching the staged name; if found it links the existing record; if not found it queues the line for batch lot creation | Lot auto-creation during transfer validation |
| U219-C13 | LOT-BATCH-CREATE | stock/models/stock_move_line.py:756-773 | _create_and_assign_production_lot | BEHAVIOR | When ml_ids_to_create_lot is non-empty | STABLE | New lot records are created in a single batch operation from the staged name values and are immediately written back to the relational lot field on the affected move lines | Batch lot creation and assignment method |
| U219-C14 | ACTION-DONE-QUANT-MOVE | stock/models/stock_move_line.py:696-706 | _action_done method | BEHAVIOR | For each move line during validation | STABLE | Quant moves proceed in three steps: unreserve the source, deduct from source available quantity capturing the inbound date, then credit the destination with the destination package reference | Quant transfer sequence in validation |
| U219-C15 | ACTION-DONE-DATE | stock/models/stock_move_line.py:712-714 | _action_done method | BEHAVIOR | After all quant moves complete | STABLE | The date field on all processed move lines is set to the current timestamp after the quant transfer loop completes, recording the actual completion time | Done timestamp assignment after quant move |
| U219-C16 | PUTAWAY-RESULT-PKG | stock/models/stock_move_line.py:262-293 | _apply_putaway_strategy | BEHAVIOR | When putaway rules are active | STABLE | Putaway strategy grouping uses the outermost destination package; if the package has a type then a single putaway covers the whole package, otherwise per-product putaway is applied while enforcing a single destination location per package | Putaway strategy applied by destination package |
| U219-C17 | AGG-QUANTITIES | stock/models/stock_move_line.py:885-977 | _get_aggregated_product_quantities | BEHAVIOR | During delivery report generation | STABLE | Aggregation groups lines by the combination of product, display name, description, unit of measure, and packaging unit; lot and serial information is intentionally excluded because it is already one line per tracking record; backorder quantities are accumulated to reconstruct the original ordered amount | Product quantity aggregation for reporting |
| U219-C18 | MIGRATION-QTY-DONE | stock/models/stock_move_line.py:37 | quantity field | MIGRATION | When migrating from version 15 or earlier | MIGRATION-FLAG | The done quantity formerly called qty done and the reserved quantity formerly called product unit quantity or reserved unit quantity on the move line were merged into a single quantity field in version 16 and this unified field name is unchanged in version 19 | Legacy done and reserved quantity field rename |
| U219-C19 | MIGRATION-REFERENCE | stock/models/stock_reference.py:4-15 | StockReference model | MIGRATION | When migrating procurement group references | MIGRATION-FLAG | The procurement group reference on moves was replaced by a many-to-many relation to a new reference model from version 16 onward; the move line itself only carries a derived text reference field, never a direct relational link to procurement or group records | Procurement group to stock reference migration |
| U219-C20 | PARTIAL-INDEX | stock/models/stock_move_line.py:97-98 | _free_reservation_index | FIELD | Database index | STABLE | A partial database index covers the combination of identifier, company, product, lot, source location, owner, and source package filtered to non-done non-cancelled lines with positive reserved quantity that are not yet picked, supporting efficient free-reservation queries | Free reservation partial index definition |

---

## Appendix: Field Name Cross-Reference (Migration)

| Odoo 15 name (move line) | Odoo 19 name | Note |
|---|---|---|
| qty_done | quantity | Done quantity |
| product_uom_qty (on move line) | quantity | Reserved quantity (now same field) |
| reserved_uom_qty (v16 intermediate) | quantity | Intermediate name, gone in v17+ |
| lot_id | lot_id | Unchanged |
| lot_name | lot_name | Unchanged |
| package_id | package_id | Unchanged |
| result_package_id | result_package_id | Unchanged |
| owner_id | owner_id | Unchanged |
| location_id | location_id | Unchanged |
| location_dest_id | location_dest_id | Unchanged |
| N/A | picked | New field in v16+ |
| N/A | quantity_product_uom | New stored computed in v16+ |
| N/A | package_history_id | New in v16+ |
