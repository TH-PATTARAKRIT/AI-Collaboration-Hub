# Atomic Handoff Packet — U49

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U49` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `7a603cb799d59d2c22e1c68dcd0a2b01bf7d7db7` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=100 supported_pointer_and_anchor=100 unknown_class=0 neutral_ids=19` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U49_auth_remaining.md` | `bb8fbb005613172cae48910f2517786344125b6dd3a16b9fadccc0e888ea981b` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U49_auth_remaining_NEUTRAL.md` | `21ca92cf179708d423a4409135b131e7d844ed4048bb5c8450c5a81859b512d8` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 100 (FACT 100 · OBSERVATION 0 · INFERENCE 0 · UNKNOWN 0) |
| Neutral statements | 19 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 0 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 100; `FUNCTION MAPPING REQUIRED`: 0 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U49-01 auth_passkey — Module Identity and Dependencies
- CAP-U49-02 auth_passkey — Data Model: auth.passkey.key
- CAP-U49-03 auth_passkey — Public Key Storage via Raw SQL
- CAP-U49-04 auth_passkey — Authentication Flow: _start_auth
- CAP-U49-05 auth_passkey — Authentication Verification: _verify_auth
- CAP-U49-06 auth_passkey — Registration Flow: _start_registration
- CAP-U49-07 auth_passkey — Registration Verification: _verify_registration_options
- CAP-U49-08 auth_passkey — Passkey Deletion: action_delete_passkey
- CAP-U49-09 auth_passkey — Passkey Creation Wizard: AuthPasskeyKeyCreate
- CAP-U49-10 auth_passkey — res.users Integration: auth_passkey_key_ids
- CAP-U49-11 auth_passkey — Login Hook: _login Override
- CAP-U49-12 auth_passkey — Credential Check: MFA Skip for Passkey
- CAP-U49-13 auth_passkey — Controller: start-auth Route
- CAP-U49-14 auth_passkey — Controller: Android Asset Links
- CAP-U49-15 auth_passkey — CREDENTIAL_PARAMS Extension
- CAP-U49-16 auth_passkey — Android Mobile Utils
- CAP-U49-17 auth_passkey — Deletion Logging
- CAP-U49-18 auth_passkey — Identity Check Integration
- CAP-U49-19 auth_passkey — action_use_password Fallback
- CAP-U49-20 auth_passkey — Security Rules
- CAP-U49-21 auth_passkey — Access Control Rules
- CAP-U49-22 auth_passkey — User Verification Enforcement
- CAP-U49-23 auth_passkey — Replay Attack Prevention
- CAP-U49-24 auth_passkey — action_rename_passkey
- CAP-U49-25 auth_passkey — action_create_passkey on res.users
- CAP-U49-26 auth_passkey_portal — Module Identity
- CAP-U49-27 auth_passkey_portal — Portal Tests: Create, Rename, Delete
- CAP-U49-28 auth_passkey_portal — Portal Permission Test
- CAP-U49-29 auth_password_policy_portal — Module Identity
- CAP-U49-30 auth_password_policy_portal — Controller: Portal Layout Values
- CAP-U49-31 auth_password_policy_portal — Frontend Translation Module
- CAP-U49-32 auth_password_policy_signup — Module Identity
- CAP-U49-33 auth_password_policy_signup — Controller: Signup Config
- CAP-U49-34 auth_totp (residual) — TOTP Algorithm Constants
- CAP-U49-35 auth_totp (residual) — TOTP.match Window
- CAP-U49-36 auth_totp (residual) — HOTP Implementation
- CAP-U49-37 auth_totp (residual) — auth_totp.device Model
- CAP-U49-38 auth_totp (residual) — Trusted Device Age Config
- CAP-U49-39 auth_totp (residual) — Rate Limiting: TOTP_RATE_LIMITS
- CAP-U49-40 auth_totp (residual) — _totp_rate_limit Implementation
- CAP-U49-41 auth_totp (residual) — Rate Limit Purge on Success
- CAP-U49-42 auth_totp (residual) — auth.totp.rate.limit.log Model
- CAP-U49-43 auth_totp (residual) — _check_credentials for TOTP
- CAP-U49-44 auth_totp (residual) — TOTP Enable: _totp_try_setting
- CAP-U49-45 auth_totp (residual) — TOTP Disable: action_totp_disable
- CAP-U49-46 auth_totp (residual) — Password Change Revokes Devices
- CAP-U49-47 auth_totp (residual) — RPC API Keys Only When TOTP Enabled
- CAP-U49-48 auth_totp (residual) — TOTP Enable Wizard: auth_totp.wizard
- CAP-U49-49 auth_totp (residual) — Wizard enable Method
- CAP-U49-50 auth_totp (residual) — Trusted Device Cookie
- CAP-U49-51 auth_totp (residual) — /web/login/totp Route
- CAP-U49-52 auth_totp (residual) — Session Token Includes totp_secret
- CAP-U49-53 auth_totp (residual) — TOTP Enable Wizard Launch: action_totp_enable_wizard
- CAP-U49-54 auth_totp (residual) — _mfa_type and _mfa_url
- CAP-U49-55 auth_totp_portal — Module Identity
- CAP-U49-56 auth_totp_portal — get_totp_invite_url Override
- CAP-U49-57 auth_totp_portal — Test: Portal TOTP Tours

## Contradiction claim ids
none

## Runtime-required claim ids
none

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
