# Correction packet U11-R2 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched.

| Field | Value |
|---|---|
| Correction packet | `U11-R2` |
| Correction request | CR-019 |
| Classification | CORRECTION_REQUIRED · priority Material |
| Boundary | U11 |
| Subject | Invoice delivery date is filled when the sales-delivery module is installed; abnormal-document warning is active from the posting buttons |
| Original evidence | U11 4202eba8 / HP_U11; found by TXA2 (content in HP_TXA2) and C01 audit F03 (originals unchanged; lineage preserved) |
| Supersession | VDR-U11-C191 / N-U11-095 (SUPERSEDED-IN-PART: the base stub statement is right but the claim that no Community source fills the delivery date is wrong when the sales-delivery module is installed); U11 dimension-5 / VDR-U11-C018 context statement (SUPERSEDED-IN-PART: the warning default is off only for programmatic callers) |

Claims table (new Claim-IDs; superseded originals remain in their files):

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U11R2-C001 | PCO-F04 | account/models/account_move.py:1100 | def _compute_delivery_date | FACT | always | — | In the base accounting module the invoice delivery date is computed by an empty stub (pass); it is informational (shown only when set on a sale document). | N-U11R2-001 |
| VDR-U11R2-C002 | PCO-F04 | sale_stock/models/account_move.py:117 | def _compute_delivery_date | FACT | sales-delivery module installed (it is in the dump) | — | The sales-delivery module extends the stub: for invoices still in draft it sets the delivery date to the latest effective date among the linked sales orders (when any order has one). | N-U11R2-001 |
| VDR-U11R2-C003 | PCO-F04 | sale_stock/models/account_move.py:127 | move.delivery_date = fields.Datetime.context_timestamp | FACT | sales-delivery module installed | — | The value is stored as a timestamp converted to the user's time zone. | N-U11R2-001 |
| VDR-U11R2-C004 | PCO-F04 | account/models/account_move.py:1108 | def _compute_taxable_supply_date | FACT | always | — | The taxable-supply date is also an empty stub in the base module (U11-C191 correct for this field); foreign country packs implement it, no Thai pack does (TXA1 F65). | N-U11R2-002 |
| VDR-U11R2-C005 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6183 | disable_abnormal_invoice_detection', True | FACT | programmatic callers | — | Posting skips the abnormal-document confirmation wizard by default (context key defaults to true). | N-U11R2-003 |
| VDR-U11R2-C006 | FUNCTION MAPPING REQUIRED | account/views/account_move_views.xml:706 | 'disable_abnormal_invoice_detection': False | FACT | posting from the document form buttons | — | The Post and Confirm buttons on the document form pass the key as false, so the wizard opens when a document has an abnormal amount or date warning. | N-U11R2-003 |
| VDR-U11R2-C007 | PCO-F04 | n/a | n/a | UNKNOWN | always | RT | UNKNOWN — whether the informational delivery date is ever used for tax point, lock or accounting-date decisions beyond display (none found in the source read); runtime/printing behaviour needs execution. | N-U11R2-004 |
