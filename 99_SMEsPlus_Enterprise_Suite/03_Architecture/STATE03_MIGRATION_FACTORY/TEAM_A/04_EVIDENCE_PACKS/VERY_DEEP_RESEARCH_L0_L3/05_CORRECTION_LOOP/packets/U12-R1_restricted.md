# Correction packet U12-R1 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched.

| Field | Value |
|---|---|
| Correction packet | `U12-R1` |
| Correction request | CR-003 |
| Classification | CORRECTION_REQUIRED · priority Normal |
| Boundary | U12 |
| Subject | Which payment provider is enabled in the dump (cash on delivery, not wire transfer) |
| Original evidence | U12 content 0b9dd753 / packet HP_U12; U20 report (content c89f4262) (originals unchanged; lineage preserved) |
| Supersession | U12 CAP-U12-08 DB-reconciliation prose ('custom (enabled)') (SUPERSEDED-IN-PART: the enabled provider is the cash-on-delivery row owned by the delivery module; the wire-transfer provider owned by the custom-payment module is disabled) |

Claims table (new Claim-IDs; superseded originals remain in their files):

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U12R1-C001 | FUNCTION MAPPING REQUIRED | payment_custom/data/payment_provider_data.xml:5 | custom | FACT | custom-payment module installed | — | The custom-payment module declares a provider of code custom with custom mode wire transfer. | N-U12R1-001 |
| VDR-U12R1-C002 | FUNCTION MAPPING REQUIRED | delivery/data/payment_provider_data.xml:4 | payment_provider_cod | FACT | delivery module installed | — | The delivery module declares the cash-on-delivery provider record, whose provider code is custom (line 8), alongside its payment-method record (payment_method_data.xml:4). | N-U12R1-001 |
| VDR-U12R1-C003 | FUNCTION MAPPING REQUIRED | delivery/data/payment_provider_data.xml:4 | payment_provider_cod | OBSERVATION | restored dump | — | OBSERVATION (pointer = the declaring record; dump query, configuration only): two provider rows are not disabled — one with code custom whose owner module is the delivery module (cash on delivery; enabled, published) and the demo provider (test mode, published); the wire-transfer provider row of the custom-payment module is disabled. | N-U12R1-002 |
