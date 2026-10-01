# Correction packet U04-R1 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched.

| Field | Value |
|---|---|
| Correction packet | `U04-R1` |
| Correction request | CR-006 |
| Classification | CORRECTION_REQUIRED · priority Normal |
| Boundary | U04 |
| Subject | Cost source of order lines when the stock-margin bridge is installed |
| Original evidence | U04 content 2d9932ef / packet HP_U04; U22 content 37e4d26f (originals unchanged; lineage preserved) |
| Supersession | VDR-U04-C354 (SUPERSEDED: statement that all other lines go to the base computation is incorrect); neutral N-U04-199 (SUPERSEDED); consistent with VDR-U22 claims for the same bridge |

Claims table (new Claim-IDs; superseded originals remain in their files):

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U04R1-C001 | FUNCTION MAPPING REQUIRED | sale_stock_margin/models/sale_order_line.py:16 | if not line.has_valued_move_ids() | FACT | stock-margin bridge installed | — | Lines without valued stock moves are passed to the base cost computation. | N-U04R1-001 |
| VDR-U04R1-C002 | FUNCTION MAPPING REQUIRED | sale_stock_margin/models/sale_order_line.py:18 | property_cost_method != 'standard' | FACT | stock-margin bridge installed | — | Lines with valued moves whose category cost method is not standard get a blended cost: delivered quantity at the delivered unit price plus the remaining ordered quantity at the product standard price. | N-U04R1-002 |
| VDR-U04R1-C003 | FUNCTION MAPPING REQUIRED | sale_stock_margin/models/sale_order_line.py:32 | elif not line.product_uom_qty and line.qty_delivered | FACT | stock-margin bridge installed | — | Lines with zero ordered quantity and a delivered quantity (added from the delivery) are passed to the base computation. | N-U04R1-001 |
| VDR-U04R1-C004 | FUNCTION MAPPING REQUIRED | sale_stock_margin/models/sale_order_line.py:35 | line_ids_to_pass | INFERENCE | stock-margin bridge installed | — | INFERENCE: only the two branches above add lines to the pass-through set that the base computation receives (line 35); a line with valued moves, an ordered quantity and a standard-cost category matches no branch, is not passed to the base computation and keeps its stored cost. | N-U04R1-003 |
