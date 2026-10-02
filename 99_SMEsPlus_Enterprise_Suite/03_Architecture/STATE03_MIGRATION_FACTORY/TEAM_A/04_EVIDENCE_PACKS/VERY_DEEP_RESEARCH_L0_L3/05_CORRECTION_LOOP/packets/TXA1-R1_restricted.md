# Correction packet TXA1-R1 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched.

| Field | Value |
|---|---|
| Correction packet | `TXA1-R1` |
| Correction request | CR-023 |
| Classification | CORRECTION_REQUIRED · priority Normal |
| Boundary | TXA1 |
| Subject | Which document-level changes trigger a tax-line resynchronisation (narrowing of TXA1-C114) |
| Original evidence | TXA1 content 760d9d0f / packet HP_TXA1; found by U30 (CONTRA on VDR-U30-C094) (originals unchanged; lineage preserved) |
| Supersession | VDR-TXA1-C114 / N-TXA1-032 (SUPERSEDED-IN-PART: partner and invoice date are snapshotted but not compared by later branches; only item-level changes plus document currency, type and rate trigger recomputation) |

Claims table (new Claim-IDs; superseded originals remain in their files):

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-TXA1R1-C001 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3334 | 'invoice_currency_rate', 'invoice_date' | FACT | draft documents | — | Before a change, a snapshot of the document's currency, partner, type, currency rate and invoice date is taken for documents. | N-TXA1R1-001 |
| VDR-TXA1R1-C002 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3337 | if move.state == 'draft' | FACT | always | — | The document-level snapshots are taken only for documents in draft state. | N-TXA1R1-001 |
| VDR-TXA1R1-C003 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:3337 | if move.state == 'draft' | INFERENCE | draft documents | — | INFERENCE relying on VDR-U30-C094 (controller re-read the snapshot construction, not every later branch): the partner and invoice-date snapshots are not used by a later comparison; only currency, type and rate (with item-level changes) decide whether tax items are recomputed. TXA1-C114's inclusion of partner among the triggers is therefore not supported. | N-TXA1R1-002 |
| VDR-TXA1R1-C004 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | draft documents | RT | UNKNOWN — numeric and display effect of changing the partner or invoice date on an existing draft (whether taxes or rate follow through other mechanisms such as fiscal-position or rate recomputation); needs execution. | N-TXA1R1-003 |
