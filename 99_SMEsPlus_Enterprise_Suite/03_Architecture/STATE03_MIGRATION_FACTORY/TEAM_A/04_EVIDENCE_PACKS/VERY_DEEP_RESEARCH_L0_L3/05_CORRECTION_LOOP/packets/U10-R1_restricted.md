# Correction packet U10-R1 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched.

| Field | Value |
|---|---|
| Correction packet | `U10-R1` |
| Correction request | CR-004 |
| Classification | CORRECTION_REQUIRED · priority C1 |
| Boundary | U10 |
| Subject | Valuation hook map: hooks credited with invoice-side stock-move/COGS selection have no caller |
| Original evidence | U10 content 4a4f39cf / packet HP_U10; verifier-side finding C01 F04 (originals unchanged; lineage preserved) |
| Supersession | VDR-U10-C336, VDR-U10-C338, VDR-U10-C339 and hook-map rows for purchase receiving and sales delivery (SUPERSEDED-IN-PART: override facts remain; the implied effect 'COGS delta booking / refund' is not supported by any call site); neutral N-U10-171, N-U10-172 (SUPERSEDED-IN-PART) |

Claims table (new Claim-IDs; superseded originals remain in their files):

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U10R1-C001 | SDV-F05 | stock_account/models/account_move.py:169 | def _stock_account_get_last_step_stock_moves | FACT | always | — | Base definition of the hook that selects the last-step stock moves related to an invoice. | N-U10R1-001 |
| VDR-U10R1-C002 | SDV-F05 | sale_stock/models/account_move.py:17 | super()._stock_account_get_last_step_stock_moves() | FACT | sales-delivery module installed | — | The sales-delivery override extends the hook result and calls the parent (no other caller). | N-U10R1-001 |
| VDR-U10R1-C003 | GRV-F04 | purchase_stock/models/account_invoice.py:122 | super()._stock_account_get_last_step_stock_moves() | FACT | purchase-receiving module installed | — | The purchase-receiving override extends the hook result and calls the parent (no other caller). | N-U10R1-001 |
| VDR-U10R1-C004 | SDV-F05 | stock_account/models/account_move.py:169 | def _stock_account_get_last_step_stock_moves | INFERENCE | always | — | INFERENCE from a search of the whole addons tree for the hook name: every occurrence is the base definition (stock_account/models/account_move.py:169), an override definition (sale_stock/models/account_move.py:14, purchase_stock/models/account_invoice.py:119, point_of_sale/models/account_move.py:36) or a call to the parent inside such an override (sale_stock 17, purchase_stock 122, point_of_sale 37). No method outside the override chain invokes it, so the hook is inert in this revision. | N-U10R1-002 |
| VDR-U10R1-C005 | GRV-F04 | stock_account/models/stock_move.py:677 | def _get_related_invoices | FACT | always | — | Base definition of the hook returning the invoices related to a stock move; its comment says it is meant to be overridden in the purchase and sales-delivery modules. | N-U10R1-003 |
| VDR-U10R1-C006 | GRV-F04 | purchase_stock/models/stock_move.py:248 | super()._get_related_invoices() | FACT | purchase-receiving module installed | — | Purchase-receiving override extends the result and calls the parent. | N-U10R1-003 |
| VDR-U10R1-C007 | SDV-F05 | sale_stock/models/stock.py:99 | super(StockMove, self)._get_related_invoices() | FACT | sales-delivery module installed | — | Sales-delivery override extends the result and calls the parent. | N-U10R1-003 |
| VDR-U10R1-C008 | GRV-F04 | stock_account/models/stock_move.py:677 | def _get_related_invoices | INFERENCE | always | — | INFERENCE from a search of the addons tree for the hook name: only definitions and parent calls inside overrides exist (stock_account 677, purchase_stock 245/248, sale_stock 95/99); no invoker was found, so this hook is also inert in this revision. The only other match is a differently named localization method. | N-U10R1-004 |
