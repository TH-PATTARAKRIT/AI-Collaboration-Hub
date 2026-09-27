# G01 QUESTION GATE — Independent Freeze Replay (Claude Code Handoff Cycle C1)

Date: 2026-09-27
Handoff: SMEPLUS-26-09-27-CLAUDE-CODE-CONTROLLED-HANDOFF-001
Mode: DELTA-FIRST replay of all G01 freeze manifests in the repository
Formal Coverage: NOT AUTHORIZED / NOT CALCULATED

## Method

For every `FREEZE_W1-*.json`:
1. SHA-256 of every declared bank file compared with the manifest.
2. Unique `QID:` count per module bank.
3. Freeze hash recomputed with the canonical `freeze_batch.py` formula
   (`batch \n sorted(modules) \n sorted(file:sha256) \n`).
4. Where the canonical formula did not match, the manifest's own declared basis
   (`batch \n module \n bank_sha \n std55_sha \n review_sha \n`) was replayed.

## Result

| Batch | Module(s) | Bank bytes | MVQ QIDs | Canonical replay | Declared-basis replay | Gate disposition |
|---|---|---|---|---|---|---|
| W1-STD | 23 G01 modules (Standard 55) | MATCH | STD-Q 55 | MATCH | — | ELIGIBLE (Standard 55) |
| W1-B01 | base, mail, web | MATCH | 50/50/50 | MATCH | — | ELIGIBLE |
| W1-B02 | auth_signup, base_automation, bus | MATCH | 40/40/41 | MATCH | — | ELIGIBLE (floor delta, see below) |
| W1-B03 | digest, portal, utm | MATCH | 40/40/40 | MATCH | — | ELIGIBLE (floor delta) |
| W1-B04 | base_setup, base_sparse_field, google_recaptcha | MATCH | 41/41/42 | MATCH | — | ELIGIBLE (floor delta) |
| W1-B05 | web_tour | MATCH | 40 | MATCH | — | ELIGIBLE (floor delta) |
| W1-B06 | html_builder | MATCH | 40 | MISMATCH | NOT REPRODUCIBLE | HOLD-LOCAL / FREEZE-INTEGRITY |
| W1-B07 | html_editor | MATCH | 40 | MISMATCH | MATCH (declared basis) | DELTA-RECHECK — non-canonical basis, reproducible |
| W1-B08 | http_routing | MATCH | 40 | MISMATCH | MATCH (declared basis) | DELTA-RECHECK — non-canonical basis, reproducible |
| W1-B09 | onboarding | MATCH | 40 | MISMATCH | NOT REPRODUCIBLE | HOLD-LOCAL / FREEZE-INTEGRITY |
| W1-B10 | phone_validation | MATCH | 40 | MATCH | — | ELIGIBLE (floor delta) |
| W1-B11 | privacy_lookup | MATCH | 40 | MISMATCH | MATCH (basis undeclared in manifest) | DELTA-RECHECK — basis not declared |

## Material deltas vs. prior RED TEAM R14

1. **W1-B07 upgraded** from R14 `HOLD / MISMATCH` to `DELTA-RECHECK`: the hash is
   reproducible from the basis the manifest itself declares. It is still not
   the canonical `freeze_batch.py` basis; a governed re-freeze with the
   canonical tool (or a governed ruling accepting the declared basis) closes it.
2. **W1-B06 remains HOLD**: no tested basis reproduces `58e86d15…`.
3. **W1-B09 NEW HOLD**: `f9f50636…` not reproducible under either basis.
4. **W1-B08 / W1-B11 NEW DELTA-RECHECK**: same condition as W1-B07; B11's manifest
   also omits `modules`, `bank_files`, `frozen_at`, `authorization`.
5. **Floor delta (governance)**: the handoff states the current governed floor is
   GVQ 55 + MVQ ≥ 48 (depth ≥ 103). Every repository freeze manifest still encodes
   `module_specific_floor: 40 / combined_floor: 95`. Under the 48 floor, only
   base/mail/web (50) meet the floor; 17 G01 banks (40–42) are BELOW FLOOR.
   No repository artifact records the 48/103 ruling. Owner: MASTER + GMVQ to
   register the governing artifact; GMVQ to top-up or record exceptions.
   Questions were not edited or invented by this replay.
6. **G01 bank gap**: `resource`, `resource_mail`, `web_hierarchy`, `web_unsplash`
   are governed G01 members with Standard 55 only — NO module bank yet.

## Remediation owner

- GMVQ/OVQDT: canonical re-freeze of B06, B07, B08, B09, B11 with `freeze_batch.py`; floor top-up to ≥ 48; author banks for the four missing modules.
- MASTER: register the 48/103 floor artifact so freeze manifests and lint encode it.

Lane A / A1 are NOT blocked by any of the above (A1 does not wait on question freeze; only A2+ transitions are gated).
