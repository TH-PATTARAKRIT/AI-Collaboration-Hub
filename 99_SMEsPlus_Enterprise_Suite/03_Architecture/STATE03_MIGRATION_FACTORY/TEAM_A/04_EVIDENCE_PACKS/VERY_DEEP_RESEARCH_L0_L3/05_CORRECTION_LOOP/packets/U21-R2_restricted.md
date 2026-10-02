# Correction packet U21-R2 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched.

| Field | Value |
|---|---|
| Correction packet | `U21-R2` |
| Correction request | CR-028 |
| Classification | CORRECTION_REQUIRED · priority Normal |
| Boundary | U21 |
| Subject | E-mailed second factor (auth_totp_mail) code window is 1 to 2 hours from issue, not 1 to 3 hours |
| Original evidence | U21 content (HP_U21); found by U35 (CONTRA tag m_window) (originals unchanged; lineage preserved) |
| Supersession | N-U21-015 prose 'roughly one to three hours' (SUPERSEDED-IN-PART: with window=3600 and timestep=3600 the code is valid from 1 to 2 hours, not up to 3; the mail text says 1 hour) |

Claims table (new Claim-IDs; superseded originals remain in their files):

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U21R2-C001 | FUNCTION MAPPING REQUIRED | auth_totp_mail/models/res_users.py:143 | TOTP(key).match(credentials['token'], window=3600, timestep=3600) | FACT | always | — | The e-mailed code is verified by TOTP with window=3600 and timestep=3600. | N-U21R2-001 |
| VDR-U21R2-C002 | FUNCTION MAPPING REQUIRED | auth_totp_mail/models/res_users.py:165 | expiration = timedelta(seconds=3600) | FACT | always | — | The mail text describes the code as valid for one hour. | N-U21R2-001 |
| VDR-U21R2-C003 | FUNCTION MAPPING REQUIRED | auth_totp_mail/models/res_users.py:175 | counter = int(datetime.timestamp(now) / 3600) | FACT | always | — | The counter used to generate the code is the floor of the current Unix timestamp divided by 3600. | N-U21R2-001 |
| VDR-U21R2-C004 | FUNCTION MAPPING REQUIRED | auth_totp_mail/models/res_users.py:143 | TOTP(key).match(credentials['token'], window=3600, timestep=3600) | INFERENCE | always | — | INFERENCE: with timestep=3600 each counter value spans one hour; with window=3600 the matcher accepts the counter within ±1 step of the current one. A code generated at the start of a counter period is valid until the end of the next period (up to 2 hours); generated near the end, it is valid for just over 1 hour. The maximum window is 2 hours; N-U21-015's 'one to three hours' overstates it. The code is not single-use. | N-U21R2-002 |
