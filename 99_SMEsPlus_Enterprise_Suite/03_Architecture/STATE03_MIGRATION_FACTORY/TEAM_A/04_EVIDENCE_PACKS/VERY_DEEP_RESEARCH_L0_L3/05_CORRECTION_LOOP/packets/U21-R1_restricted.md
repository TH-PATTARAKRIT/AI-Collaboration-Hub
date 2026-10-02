# Correction packet U21-R1 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched.

| Field | Value |
|---|---|
| Correction packet | `U21-R1` |
| Correction request | CR-024 |
| Classification | CORRECTION_REQUIRED · priority Material |
| Boundary | U21 |
| Subject | Certificate adapter loads stored private-key PEM with password=None; stored PEM is encrypted when the key record has a password |
| Original evidence | U21 content (HP_U21); found by U37 (CONTRA on VDR-U37-C412) (originals unchanged; lineage preserved) |
| Supersession | VDR-U21-C281 context statement 'consistent with the stored unencrypted PEM' (SUPERSEDED-IN-PART: true only for key records with no password field; when a password is set the stored pem_key is encrypted and the adapter call fails) |

Claims table (new Claim-IDs; superseded originals remain in their files):

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U21R1-C001 | FUNCTION MAPPING REQUIRED | certificate/tools/certificate_adapter.py:41 | private_key_id.pem_key | FACT | always | — | The certificate adapter reads the stored pem_key from the key record linked to the certificate. | N-U21R1-001 |
| VDR-U21R1-C002 | FUNCTION MAPPING REQUIRED | certificate/tools/certificate_adapter.py:43 | load_pem_private_key(key, password=None) | FACT | always | — | The adapter loads the key PEM with password=None regardless of whether the key record has a password. | N-U21R1-001 |
| VDR-U21R1-C003 | FUNCTION MAPPING REQUIRED | certificate/models/key.py:88 | pwd = key.password.encode | FACT | always | — | When computing pem_key, the password is read from the key record's password field. | N-U21R1-002 |
| VDR-U21R1-C004 | FUNCTION MAPPING REQUIRED | certificate/models/key.py:113 | BestAvailableEncryption(pwd) if pwd else serialization.NoEncryption() | FACT | key record has a password | — | The stored pem_key is serialised with BestAvailableEncryption when pwd is non-empty, and NoEncryption otherwise. | N-U21R1-002 |
| VDR-U21R1-C005 | FUNCTION MAPPING REQUIRED | certificate/tools/certificate_adapter.py:43 | load_pem_private_key(key, password=None) | INFERENCE | key record has a password | RT | INFERENCE: when a certificate's linked key has a password the stored pem_key is password-encrypted; the adapter always passes password=None, so loading an encrypted key would raise a ValueError. U21-C281's statement 'consistent with the stored unencrypted PEM' is accurate only for key records with no password. Runtime confirmation of the error path is needed (AWT). | N-U21R1-002 |
