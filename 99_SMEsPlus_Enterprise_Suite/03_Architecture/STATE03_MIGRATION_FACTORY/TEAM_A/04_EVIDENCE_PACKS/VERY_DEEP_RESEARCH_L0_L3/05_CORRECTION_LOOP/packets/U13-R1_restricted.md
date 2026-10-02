# Correction packet U13-R1 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched.

| Field | Value |
|---|---|
| Correction packet | `U13-R1` |
| Correction request | CR-022 |
| Classification | CORRECTION_REQUIRED · priority Normal |
| Boundary | U13 |
| Subject | E-document import tax-total correction tolerance (0.03 staged path; no threshold on the legacy path; 0.05 only in a comment) and export-method shadowing caveat |
| Original evidence | U13 content c348a8c8 / packet HP_U13; found by U34 (CONTRA on VDR-U34-C085/C086 and C273/C274) (originals unchanged; lineage preserved) |
| Supersession | VDR-U13-C441 (SUPERSEDED-IN-PART: 'within 0.05' reflects a code comment, not the implemented tolerance); VDR-U13-C430 (QUALIFIED: the cited export method may be shadowed in the installed inheritance order — RT) |

Claims table (new Claim-IDs; superseded originals remain in their files):

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U13R1-C001 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:1725 | tolerance = 0.03 | FACT | staged import path | — | In the staged (newer) import path the tax-total correction uses a tolerance of 0.03. | N-U13R1-001 |
| VDR-U13R1-C002 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_common.py:599 | less than 0.05 different | FACT | always | — | The figure 0.05 appears only in a code comment describing the correction; it is not the implemented tolerance of the staged path. | N-U13R1-001 |
| VDR-U13R1-C003 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:1269 | def _correct_invoice_tax_amount | FACT | legacy import path | — | A separate legacy method corrects invoice tax amounts for rounding on the older import path. | N-U13R1-002 |
| VDR-U13R1-C004 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:1269 | def _correct_invoice_tax_amount | INFERENCE | legacy import path | — | INFERENCE relying on the reading recorded in VDR-U34-C273 (controller re-read only the method head): the legacy method applies a rounding-level difference to taxes matched by exact rate without a numeric threshold. | N-U13R1-002 |
| VDR-U13R1-C005 | FUNCTION MAPPING REQUIRED | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:39 | def _export_invoice(self, invoice) | FACT | always | — | The older UBL 2.0 builder defines its own export method; U13-C430 cites a same-named method in the newer builder file. | N-U13R1-003 |
| VDR-U13R1-C006 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | installed formats | RT | UNKNOWN — which of the two export methods runs for each format in the installed inheritance order (U34 simulated the order and found the older skeleton wins for several formats); needs execution to confirm. | N-U13R1-004 |
