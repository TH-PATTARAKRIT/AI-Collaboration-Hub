# Correction packet U11-R1 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched.

| Field | Value |
|---|---|
| Correction packet | `U11-R1` |
| Correction request | CR-002/CR-005 |
| Classification | CORRECTION_REQUIRED · priority Material |
| Boundary | U11 |
| Subject | Payment state 'in payment' is not reachable in Community; invoice cancel does not cancel its settling payments |
| Original evidence | U11 content 4202eba8 / packet HP_U11; verifier-side findings C01 F02 and F12; U12 claim C187 (in-payment hook) (originals unchanged; lineage preserved) |
| Supersession | VDR-U11-C003, C039, C040, C042 (SUPERSEDED-IN-PART: in-payment is conditional on an extension that is not in Community); VDR-U11-C031, C058 (SUPERSEDED-IN-PART: payment-cancel effect applies only to payments whose own entry is the cancelled entry); neutral N-U11-002, N-U11-013, N-U11-016, N-U11-024 (SUPERSEDED-IN-PART) |

Claims table (new Claim-IDs; superseded originals remain in their files):

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U11R1-C001 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:7371 | return 'paid' | FACT | always | — | The in-payment hook returns paid. | N-U11R1-001 |
| VDR-U11R1-C002 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:7369 | accountant module | FACT | always | — | The hook's docstring says the in-payment state is enabled by overriding it in the accountant module, which is not part of Community. | N-U11R1-001 |
| VDR-U11R1-C003 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1302 | _get_invoice_in_payment_state() | FACT | always | — | When a posted invoice has settling payments that are not all matched, the payment state takes the hook value. | N-U11R1-002 |
| VDR-U11R1-C004 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:1321 | _get_invoice_in_payment_state() | FACT | always | — | A posted invoice with a matched in-process payment that has no entry takes the hook value as well. | N-U11R1-002 |
| VDR-U11R1-C005 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:7367 | def _get_invoice_in_payment_state | INFERENCE | no extension overrides the hook | — | INFERENCE: a search of the addons tree finds a single definition of the hook, so in Community the value in-payment is never assigned; the selection value (account_move.py:57) exists but is only reachable through an external override. | N-U11R1-003 |
| VDR-U11R1-C006 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6395 | self.payment_ids.state = "canceled" | FACT | always | — | button_cancel removes the reconciliations of the entry's lines and then sets the state of the entry's payment_ids to canceled. | N-U11R1-004 |
| VDR-U11R1-C007 | FUNCTION MAPPING REQUIRED | account/models/account_payment.py:1250 | payment_ids = fields.One2many | FACT | always | — | payment_ids on a journal entry is the one-to-many link to payments whose own entry (move_id) is this entry; it is not the list of payments settling an invoice. | N-U11R1-004 |
| VDR-U11R1-C008 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:214 | matched_payment_ids | FACT | always | — | Payments linked to an invoice are held in matched_payment_ids, a separate field. | N-U11R1-004 |
| VDR-U11R1-C009 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:6394 | self.line_ids.remove_move_reconcile() | INFERENCE | invoice or bill being cancelled | RT | INFERENCE from the three claims above: cancelling an invoice removes the reconciliations of its lines but does not set its settling payments to canceled; they stay posted and become unreconciled. The resulting payment state and any follow-up behaviour need execution (AWT). | N-U11R1-005 |
