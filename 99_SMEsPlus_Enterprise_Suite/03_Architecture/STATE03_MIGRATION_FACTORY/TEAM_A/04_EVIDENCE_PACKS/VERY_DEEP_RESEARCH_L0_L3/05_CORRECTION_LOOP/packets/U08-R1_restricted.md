# Correction packet U08-R1 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched.

| Field | Value |
|---|---|
| Correction packet | `U08-R1` |
| Correction request | CR-001 |
| Classification | CORRECTION_REQUIRED · priority Material |
| Boundary | U08 |
| Subject | Return eligibility of a transfer (done-only vs sale-linked) |
| Original evidence | U08 content c8173586 / packet HP_U08; verifier-side finding C01 F01 (C01 content c9083627) (originals unchanged; lineage preserved) |
| Supersession | VDR-U08-C235 (SUPERSEDED-IN-PART: base rule stays valid; effective rule when the sales-delivery module is installed differs); neutral N-U08-127 (SUPERSEDED-IN-PART) |

Claims table (new Claim-IDs; superseded originals remain in their files):

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U08R1-C001 | GRV-F07; SDV-F06 | stock/models/stock_picking.py:2136 | self.state == 'done' | FACT | always | — | Base rule: a transfer is returnable only when its state is done. | N-U08R1-001 |
| VDR-U08R1-C002 | SDV-F06 | sale_stock/models/stock.py:324 | self.sale_id | FACT | sales-delivery module installed (it is installed in the dump) | — | The sales-delivery module extends the rule: returnable when the base rule holds OR the transfer is linked to a sales order; no state test is applied to the second branch. | N-U08R1-001 |
| VDR-U08R1-C003 | SDV-F06 | stock/wizard/stock_picking_return.py:113 | _can_return | FACT | always | — | The return wizard refuses with the message 'You may only return Done pickings' only when the eligibility rule is false, so with the extension a sales-linked transfer in any state passes this check. | N-U08R1-002 |
| VDR-U08R1-C004 | SDV-F06 | stock/wizard/stock_picking_return.py:122 | location_dest_usage == 'inventory' | FACT | always | — | Return lines are built from the transfer's moves, skipping cancelled moves and moves whose destination location has inventory usage; no picking-state filter appears at this point. | N-U08R1-002 |
| VDR-U08R1-C005 | SDV-F06 | stock/wizard/stock_picking_return.py:128 | No products to return | FACT | always | — | The wizard raises 'No products to return (only lines in Done state and not fully returned yet can be returned)' when no lines remain, so the Done restriction in the message is applied through the line list, not through the eligibility check. | N-U08R1-003 |
| VDR-U08R1-C006 | SDV-F06 | n/a | n/a | UNKNOWN | sales-delivery module installed | RT | UNKNOWN — what quantity the wizard offers for a not-done sales-linked transfer and what document results; resolving needs execution (AWT). | N-U08R1-004 |
