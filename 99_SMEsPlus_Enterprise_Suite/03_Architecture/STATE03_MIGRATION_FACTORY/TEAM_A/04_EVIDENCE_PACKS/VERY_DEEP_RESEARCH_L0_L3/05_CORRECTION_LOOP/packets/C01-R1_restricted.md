# Correction packet C01-R1 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched.

| Field | Value |
|---|---|
| Correction packet | `C01-R1` |
| Correction request | CR-007/CR-010 |
| Classification | NEEDS_MORE_EVIDENCE · priority C1 |
| Boundary | C01 |
| Subject | Chain-level statements missing from O2C: reservation timing at confirmation, and the transfer-date lock-period constraint |
| Original evidence | C01 content c9083627 / packet HP_C01 (originals unchanged; lineage preserved) |
| Supersession | Supplements C01 CAP-C01-01/C01-05/C01-08 (no claim superseded; adds chain statements flagged F06 and F14 by the consistency audit) |

Claims table (new Claim-IDs; superseded originals remain in their files):

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-C01R1-C001 | SDV-F02 | stock/models/stock_picking.py:68 | reservation_method = fields.Selection | FACT | always | — | Each operation type has a reservation method: at confirmation (default), manually, or before the scheduled date. | N-C01R1-001 |
| VDR-C01R1-C002 | SDV-F02 | stock/models/stock_move.py:1734 | reservation_method == 'at_confirm' | FACT | operation type reserves at confirmation | — | On confirming a move, moves of operation types reserving at confirmation are assigned immediately in the same step. | N-C01R1-001 |
| VDR-C01R1-C003 | SDV-F02 | stock/models/stock_move.py:1973 | _should_assign_at_confirm | FACT | always | — | A move is assigned at confirmation when it bypasses reservation, its operation type reserves at confirmation, or its reservation date is not later than today. | N-C01R1-001 |
| VDR-C01R1-C004 | SDV-F02 | stock/models/stock_picking.py:70 | default='at_confirm' | OBSERVATION | restored dump | — | OBSERVATION: the source default is reservation at confirmation and all 16 operation types in the restored dump reserve at confirmation (dump query on operation-type configuration; pointer is the source default), so confirming a sales order's delivery would reserve available stock at once in this configuration. | N-C01R1-002 |
| VDR-C01R1-C005 | PCO-F04 | stock_account/models/stock_picking.py:31 | hard=True | FACT | always | — | The date-done lock-period check on transfers (U10 C186) compares the completion date with the fiscal-year lock and the hard lock only; sales, purchase and tax locks are not applied to transfers. This belongs in the order-to-cash and procure-to-pay cut-off narrative. | N-C01R1-003 |
