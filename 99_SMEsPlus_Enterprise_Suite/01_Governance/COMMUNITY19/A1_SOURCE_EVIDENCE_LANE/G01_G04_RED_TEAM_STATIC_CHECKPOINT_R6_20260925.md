# SMEsPlus Community19 - RED TEAM G01-G04 Static Checkpoint R6

Date: 2026-09-25
Mode: A1 SOURCE/STATIC + QUESTION-GATE RECONCILIATION
Formal Coverage: NOT CALCULATED

## Environment
- Authorized Community19 desktop source/runtime device is OFFLINE.
- Upstream Odoo 19.0 static anchor remains `8d05257d83f9128953f580a066db67c48fcdb96f`.
- Upstream source is not asserted byte-identical to the governed local Community19 package.

## G01 PLATFORM_BASE - verified A1 delta
New `base` source slices:
- `ir_default.py` `20394caef7442c101e805e87718ac13fbba9ae09`
- `ir_exports.py` `ca5e8c4ff2e7a745a1fbc910be8ba96e1c4ac96e`
- `res_bank.py` `136d6a64338be3d5e3c40d5e7df8d600e0ad1ea2`
- `res_users_settings.py` `3aeed6ec46bc0b0be871973923e6f5114b1ed788`
- `res_country.py` `f24c2711071654b6e75e6743c122d1de527c924a`
- `res_lang.py` `563b4eff214fbd9940661b9f76ee3a3aa571c76c`
- `ir_mail_server.py` `6658a04471bb61a65276793f65050252dde6db17`

Verified findings:
1. `ir.default` scopes defaults by field, optional user, optional company and optional condition. Stored JSON values are validated against the target ORM field type.
2. Default changes invalidate relevant caches; default resolution is explicitly user/company-sensitive and includes company-dependent fallback handling.
3. `ir.exports` persists named export presets and ordered export-field selections.
4. `res.partner.bank` sanitizes account numbers, enforces uniqueness per partner, derives company from the account-holder partner, and uses company-aware domain checks.
5. `res.partner.bank` has an explicit outgoing-payment permission flag. Static presence is not runtime enforcement proof.
6. `res.users.settings` enforces one settings row per user and lazily creates it when absent.
7. `res.country` enforces unique name/code, validates address formats, supports country-specific address input views, and enforces state-code uniqueness within country.
8. `res.lang` enforces unique language identifiers, requires at least one active language after registry readiness, validates date/time formats, and uses `ir.default` when installing a default partner language.
9. `ir.mail_server` exposes multiple outgoing-mail transport/authentication modes, restricts sensitive configuration fields to system administrators, validates certificate-based transport configuration, and blocks archival while reported in active use.
10. Outgoing-mail debug mode explicitly warns that verbose logs may contain confidential information; this is an operational risk surface, not runtime proof.

Disposition: G01 A1 ACTIVE / VERIFIED STATIC DELTA / BASE NOT COMPLETE.

## QUESTION GATE
- W1-STD remains FROZEN / VERIFIED for the 23-module G01 roster.
- W1-B01 and W1-B02 remain FROZEN / independently verified.
- W1-B03 remains HOLD pending independent eligibility reconciliation.
- Runtime A2 was NOT executed because the authorized runtime/source device is unavailable.
- Reconciliation, A3 and MASTER do not advance.

## G02 IDENTITY_ACCESS
Exact controlled 11-row roster remains unrecovered. Re-search found no new controlled membership evidence. No governed/frozen eligible G02 question package was found.
Status: A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION.

## G03 MASTER_DATA
Exact controlled 11-row roster remains unrecovered. Existing `product`, `uom`, `analytic` evidence remains anchor-only. No governed/frozen eligible G03 question package was found.
Status: A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION.

## G04 ACCOUNT_BASE
Exact controlled nine-row roster remains unrecovered. ACCOUNT_BASE remains separated from ACCOUNT_PROCESS; broad accounting inventory is not membership proof. No governed/frozen eligible G04 question package was found.
Status: A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION.

## Integrity controls
- Source Presence != Runtime Reachability.
- Company-scoped source controls are not tenant-isolation proof.
- `GROUP_STRUCTURE_V2_CORE.tsv` row-level bytes remain unavailable while the authorized desktop is offline.
- No Evidence = No Progress.
- No A2/A3/MASTER transition without exact governed, verified, frozen/eligible questions.
- Formal Coverage remains prohibited until the Canonical Function-ID denominator is Boss-frozen.
