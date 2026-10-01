# Correction packet U07-R1 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched.

| Field | Value |
|---|---|
| Correction packet | `U07-R1` |
| Correction request | CR-009 |
| Classification | CORRECTION_REQUIRED · priority Material |
| Boundary | U07 |
| Subject | Inert extension methods (return wizard, extra move values, return classification) and bill-reset valuation |
| Original evidence | U07 content 03a764e2 / packet HP_U07; U10 content 4a4f39cf; verifier-side findings C02 F02, F19, F20, F21 (originals unchanged; lineage preserved) |
| Supersession | VDR-U07-C145 (SUPERSEDED: the override that sets order-line and partner on vendor-return moves is never invoked); VDR-U07-C097 (SUPERSEDED-IN-PART: orphan override); VDR-U07-C158, VDR-U10-C144, VDR-U10-C145 (SUPERSEDED-IN-PART: the return-classification helper has no caller); U07 CAP-U07-05 state-list statement that a bill reset re-values receipts (SUPERSEDED); neutral N-U07-065, N-U07-039, N-U07-076, N-U10-064, N-U10-065 (SUPERSEDED-IN-PART) |

Claims table (new Claim-IDs; superseded originals remain in their files):

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U07R1-C001 | GRV-F07 | purchase_stock/models/stock.py:128 | def _prepare_move_default_values(self, return_line, new_picking) | FACT | purchase-receiving module installed | — | The purchase-receiving module defines a two-argument override of _prepare_move_default_values on the return wizard model and calls the parent with the same two arguments. | N-U07R1-001 |
| VDR-U07R1-C002 | GRV-F07 | stock/wizard/stock_picking_return.py:25 | def _prepare_move_default_values(self, new_picking) | FACT | always | — | The base method of that name is defined on the return-line model (class defined at line 7) with a single argument; the wizard model (class at line 86) has no such method. | N-U07R1-001 |
| VDR-U07R1-C003 | GRV-F07 | stock/wizard/stock_picking_return.py:50 | self._prepare_move_default_values(new_picking) | FACT | always | — | The base flow calls the method with one argument on each return line record. | N-U07R1-001 |
| VDR-U07R1-C004 | GRV-F07 | sale_stock/wizard/stock_picking_return.py:9 | def _prepare_move_default_values(self, new_picking) | FACT | sales-delivery module installed | — | For contrast, the sales-delivery module extends the line-model method with the correct one-argument signature. | N-U07R1-001 |
| VDR-U07R1-C005 | GRV-F07 | purchase_stock/models/stock.py:128 | def _prepare_move_default_values(self, return_line, new_picking) | INFERENCE | purchase-receiving module installed | RT | INFERENCE: the purchase-receiving override targets a wizard method that does not exist in the base and is never called with two arguments, so it does not run; vendor-return moves therefore do not receive the order line and partner from this override (the link, if present, comes from copying the original receipt move). Confirm by execution (AWT). | N-U07R1-002 |
| VDR-U07R1-C006 | PDT-F04 | purchase_stock/models/stock_move.py:100 | super()._prepare_extra_move_vals(qty) | FACT | purchase-receiving module installed | — | The purchase-receiving module overrides _prepare_extra_move_vals (line 99) and calls the parent. | N-U07R1-003 |
| VDR-U07R1-C007 | PDT-F04 | purchase_stock/models/stock_move.py:99 | def _prepare_extra_move_vals | INFERENCE | always | — | INFERENCE from a search of the addons tree: no other definition and no caller of _prepare_extra_move_vals exists, so this override is inert and extra moves do not receive the order-line link through it. | N-U07R1-003 |
| VDR-U07R1-C008 | GRV-F07 | stock_account/models/stock_move.py:683 | def _is_returned | FACT | always | — | The helper _is_returned classifies a move as returned-in (source customer) or returned-out (destination supplier). | N-U07R1-004 |
| VDR-U07R1-C009 | GRV-F07 | stock_account/models/stock_move.py:683 | def _is_returned | INFERENCE | always | — | INFERENCE from a search of the addons tree: the helper has no caller; valuation statements that rely on it as the return classification describe a method not used by any flow in this revision. | N-U07R1-004 |
| VDR-U07R1-C010 | GRV-F04 | stock_account/models/account_move.py:42 | _set_value() | FACT | automated or periodic valuation | — | Bill-side revaluation of incoming and dropship moves runs at posting. | N-U07R1-005 |
| VDR-U07R1-C011 | GRV-F04 | stock_account/models/account_move.py:46 | def button_draft | FACT | always | — | Resetting a bill to draft unlinks the cost-of-sales lines generated at posting and does not re-value the receipts. | N-U07R1-005 |
