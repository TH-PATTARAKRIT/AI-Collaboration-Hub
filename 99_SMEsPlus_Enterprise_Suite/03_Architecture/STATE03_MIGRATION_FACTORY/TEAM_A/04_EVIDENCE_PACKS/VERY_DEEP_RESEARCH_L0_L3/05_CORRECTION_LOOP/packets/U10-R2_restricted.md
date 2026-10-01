# Correction packet U10-R2 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched.

| Field | Value |
|---|---|
| Correction packet | `U10-R2` |
| Correction request | CR-008 |
| Classification | CORRECTION_REQUIRED · priority C1 |
| Boundary | U10 |
| Subject | Posting inside a locked period: the entry date is moved, not refused (fiscal/hard/tax/sale/purchase locks) |
| Original evidence | U10 content 4a4f39cf / packet HP_U10; U11 CAP-U11-04 (consistent with this packet); verifier-side finding C02 F01 (originals unchanged; lineage preserved) |
| Supersession | VDR-U10-C150, VDR-U10-C194, VDR-U10-C164 (SUPERSEDED-IN-PART: the statements that a lock-date refusal happens when valuation/closing entries are posted omit the date shift performed in posting); neutral N-U10-074, N-U10-093, N-U10-096 (SUPERSEDED-IN-PART) |

Claims table (new Claim-IDs; superseded originals remain in their files):

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U10R2-C001 | PCO-F01 | account/models/account_move.py:5704 | _get_violated_lock_dates(move.date | FACT | always | — | While posting, each entry's date is tested against the company lock dates (the check takes the tax-report effect and the journal into account). | N-U10R2-001 |
| VDR-U10R2-C002 | PCO-F01 | account/models/account_move.py:5706 | move.date = move._get_accounting_date( | FACT | always | — | If any lock is violated, the entry's date is replaced by the accounting date computed for it (the first date not blocked by the violated locks) and posting continues. | N-U10R2-001 |
| VDR-U10R2-C003 | PCO-F01 | account/models/account_move.py:4001 | posted_move._check_fiscal_lock_dates() | FACT | always | — | When the date or state of already-posted entries is written, the fiscal lock check is run and tax lines are checked against the tax lock; this is where refusals occur (edits of posted entries, resets, deletions). | N-U10R2-002 |
| VDR-U10R2-C004 | PCO-F01 | stock_account/models/res_company.py:78 | account_move._post() | FACT | automated valuation closing | — | The stock closing entry is posted through the same posting method, so the date shift applies to it. | N-U10R2-003 |
| VDR-U10R2-C005 | PCO-F01 | account/models/account_move.py:5704 | _get_violated_lock_dates(move.date | INFERENCE | always | RT | INFERENCE: posting of valuation, cost-of-sales, landed-cost and closing entries inside a locked period is not refused by the lock; the entry takes the shifted accounting date. The exact date chosen per lock type and its effect on numbering and period reports need execution (AWT). | N-U10R2-003 |
