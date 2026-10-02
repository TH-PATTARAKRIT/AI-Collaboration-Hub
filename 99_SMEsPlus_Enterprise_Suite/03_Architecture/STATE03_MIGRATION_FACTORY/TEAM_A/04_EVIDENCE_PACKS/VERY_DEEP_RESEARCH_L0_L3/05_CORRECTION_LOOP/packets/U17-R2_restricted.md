# Correction packet U17-R2 — RESTRICTED TECHNICAL EVIDENCE

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION** · RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION · source revision `19.0.post20260921` · DELTA-FIRST: only the affected scope was re-researched.

| Field | Value |
|---|---|
| Correction packet | `U17-R2` |
| Correction request | CR-026 |
| Classification | CORRECTION_REQUIRED · priority Material |
| Boundary | U17 |
| Subject | Gamification challenge end-of-period comparison is a format mismatch; end-of-period rewards never trigger for periodic challenges |
| Original evidence | U17 content (HP_U17); found by U38 (CONTRA on VDR-U38-C440) (originals unchanged; lineage preserved) |
| Supersession | VDR-U17-C466 (SUPERSEDED: the claim that periodic challenges trigger end-of-period rewards is not supported; the comparison always returns false because Datetime.to_string produces a datetime string while Date.to_string produces a date-only string) |

Claims table (new Claim-IDs; superseded originals remain in their files):

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U17R2-C001 | FUNCTION MAPPING REQUIRED | gamification/models/gamification_challenge.py:46 | fields.Datetime.to_string(end_date) | FACT | periodic challenge (daily/weekly/monthly/yearly) | — | For periodic challenges the helper returns end_date as a Datetime string, e.g. '2026-10-31 00:00:00'. | N-U17R2-001 |
| VDR-U17R2-C002 | FUNCTION MAPPING REQUIRED | gamification/models/gamification_challenge.py:668 | yesterday = date.today() - timedelta(days=1) | FACT | always | — | In the reward-dispatch method, yesterday is computed as a date object. | N-U17R2-001 |
| VDR-U17R2-C003 | FUNCTION MAPPING REQUIRED | gamification/models/gamification_challenge.py:671 | challenge_ended = force or end_date == fields.Date.to_string(yesterday) | FACT | always | — | challenge_ended is set by comparing end_date (a Datetime string for periodic challenges) with fields.Date.to_string(yesterday) (a date-only string like '2026-10-31'). | N-U17R2-001 |
| VDR-U17R2-C004 | FUNCTION MAPPING REQUIRED | gamification/models/gamification_challenge.py:671 | challenge_ended = force or end_date == fields.Date.to_string(yesterday) | INFERENCE | periodic challenge | RT | INFERENCE: Datetime.to_string produces 'YYYY-MM-DD HH:MM:SS' while Date.to_string produces 'YYYY-MM-DD'; the strings are never equal, so challenge_ended is always False for periodic challenges unless force=True. End-of-period rewards and top-three badges therefore only run on manual close. Runtime confirmation of the exact behaviour on a populated database with a closing call is needed (AWT). | N-U17R2-002 |
