# Correction packet U05-R1 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched.

| Field | Value |
|---|---|
| Correction packet | `U05-R1` |
| Correction request | CR-025 |
| Classification | CORRECTION_REQUIRED · priority Normal |
| Boundary | U05 |
| Subject | Seeded gift-card reward product carries a tax; the tax-strip override applies only to discount products created after the loyalty-order bridge is installed |
| Original evidence | U05 content (HP_U05); found by U32 (CONTRA on VDR-U32-C146) (originals unchanged; lineage preserved) |
| Supersession | VDR-U05-C019 (SUPERSEDED-IN-PART: true for discount reward products created after the loyalty-order bridge is installed; not true for the seeded gift-card product which carries a 7% tax in the dump) |

Claims table (new Claim-IDs; superseded originals remain in their files):

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U05R1-C001 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/loyalty_reward.py:9 | _get_discount_product_values | FACT | loyalty-order bridge installed | — | The loyalty-order bridge overrides _get_discount_product_values to set taxes_id to False on every discount-product values dict. | N-U05R1-001 |
| VDR-U05R1-C002 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/loyalty_reward.py:13 | taxes_id | FACT | loyalty-order bridge installed | — | The override sets 'taxes_id': False for discount products; it runs only at product creation and only for discount reward types. | N-U05R1-001 |
| VDR-U05R1-C003 | FUNCTION MAPPING REQUIRED | loyalty/data/loyalty_data.xml:5 | gift_card_product_50 | OBSERVATION | restored dump | — | OBSERVATION (pointer = data record; U32 DB reconciliation): the seeded gift-card product was declared without a taxes_id override in the data file and carries the 7% sale tax in the dump; the tax-strip override covers discount products, not the gift-card program product. | N-U05R1-002 |
| VDR-U05R1-C004 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | seeded configuration | RT | UNKNOWN — the accounting and tax-reporting effect of the tax asymmetry (untaxed sale line, taxed redemption line) on the gift-card balance and on VAT returns needs runtime confirmation (AWT). | N-U05R1-003 |
