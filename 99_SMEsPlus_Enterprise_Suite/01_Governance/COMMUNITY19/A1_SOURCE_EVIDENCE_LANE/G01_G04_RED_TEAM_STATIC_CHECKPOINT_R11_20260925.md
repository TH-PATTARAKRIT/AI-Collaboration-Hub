# SMEsPlus Community19 G01-G04 RED TEAM Checkpoint R11

Date: 2026-09-25
Mode: A1 Source Evidence + Question Gate + Roster Reconciliation
Formal Coverage: NOT AUTHORIZED / NOT CALCULATED

## Control boundary
- Pipeline remains A1 Source Evidence -> QUESTION GATE -> A2 Blind Runtime -> Reconciliation -> A3 Independent Adversarial Verification -> MASTER.
- A2/A3/MASTER are prohibited for any module/batch without a governed question document/question bank that is present, verified and frozen/eligible.
- No Evidence = No Progress.
- Source Presence != Runtime Reachability.
- Authorized Community19 desktop `THPATTARAKRIT-SOLUTION-SERVICE-2.local` is OFFLINE; last seen 2026-09-24T12:53:18.011+00:00.

## Roster reconciliation control
- Current A1 control index remains G01=23, G02=11, G03=11, G04=9.
- Historical Group Structure V2 evidence identifies `GROUP_STRUCTURE_V2_CORE.tsv` as the full 299-row mapping artifact with SHA-256 `203ff43e7844a734de5e9aaebb91529e46dd7998423d4d5772999ed0db9ff5bf`.
- Current accessible Library/GitHub surfaces confirm the mapping artifact pointer and group counts but still do not expose the row-level TSV bytes. Therefore no exact G02-G04 full technical roster is promoted from category, prefix, dependency or count-matching inference.
- Historical evidence explicitly anchors `product`, `uom`, `analytic` to MASTER_DATA and splits `account` into ACCOUNT_BASE + ACCOUNT_PROCESS; this does not reveal the remaining row membership.

## G01 PLATFORM_BASE — new A1 source slices
Upstream static anchor: `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`.

Verified source blobs:
- `odoo/addons/base/models/__init__.py` = `d748881f7eea3eae1e8b8b89d2bc90d4f9e9c379`
- `ir_demo_failure.py` = `3d06979845f0fc0cbb2f7a12b4aabc5dfa9ce45f`
- `image_mixin.py` = `614a70f497fe7746a66d7a07620193e2fff9eb24`
- `decimal_precision.py` = `3a5b116cff0692042e03b83b3f71d1934823290a`
- `properties_base_definition_mixin.py` = `1a124a33772a9bb2b8da83dacf4470f0440eacab`
- `report_paperformat.py` = `fc7dc8edd3c0fe144cc9c765f9d25caff437addd`

Static findings:
1. The base model initializer provides a reproducible inventory of the active base model source surface at this upstream anchor.
2. Demo-install failures are retained in transient records tied to the failing module and error, then return to the module lifecycle via `ir.module.module.next()`; runtime demo failure behavior is not claimed.
3. `image.mixin` stores derivative image sizes as related attachment-backed fields, making image persistence/resizing a shared base behavior rather than a feature-local assumption.
4. Decimal precision is unique by usage, cached at registry level, invalidated on create/write/unlink, and explicitly warns that reducing precision does not rewrite existing data and can disturb financial balance.
5. Properties base-definition resolution uses privileged definition lookup paths and injects the definition identifier during create; this is a static configuration/data-shaping surface only.
6. Report paper format rejects simultaneous use of a predefined non-custom format and explicit page dimensions; orientation changes computed print width/height.

Disposition: A1 ACTIVE / VERIFIED STATIC DELTA / BASE NOT COMPLETE.

## G01 QUESTION GATE
- `W1-STD` remains FROZEN / VERIFIED.
- `W1-B01` remains FROZEN / ELIGIBLE.
- `W1-B02` remains FROZEN / ELIGIBLE.
- `W1-B03` (`digest`, `portal`, `utm`) remains FROZEN / independently integrity-verified / ELIGIBLE from the prior replay. Current repository search again locates `FREEZE_W1-B03.json` and the rolling-freeze status; no gate regression was found.
- Runtime A2 was NOT EXECUTED because the authorized Community19 runtime device is offline.
- Reconciliation, A3 and MASTER do not advance.

## G02 IDENTITY_ACCESS — roster recovery + candidate-source evidence
Controlled count: 11. Exact governed row-level roster remains unrecovered.

The previously recorded 11-name auth-family reconstruction remains CANDIDATE ONLY / NO CANONICAL MEMBERSHIP CREDIT. This run did not invent or add any new candidate module name.

New upstream static evidence was taken only from names already present in that controlled candidate record:
- `auth_totp/models/res_users.py` = `3887b4e59304f0eda7d2ce172e2fc714148cfc07`
- `auth_totp/models/auth_totp_rate_limit_log.py` = `3dec867b36f37708a2d1dfdc4853c4829d345359`
- `auth_passkey/models/res_users_identitycheck.py` = `60d071a2db9fdee17c02bf9c6bb3c4b3c68b5506`
- `auth_ldap/models/res_company_ldap.py` = `c5ec49981985eab031ff6f8a9fa585f21327cfc1`

Static findings:
1. TOTP-enabled users are forced to API-key-only RPC for password-based RPC paths, and the TOTP secret participates in session-token inputs.
2. TOTP validation rejects token reuse through a stored last-counter check and rate-limits code checks and authentication-mail actions to 5 events per one-hour window per user/type.
3. TOTP enable/disable and device revocation paths are identity-checked; runtime enforcement is not claimed.
4. Passkey extends the recent identity-check surface with a WebAuthn credential path and falls back to password when selected by the user.
5. LDAP authentication explicitly rejects blank passwords, requires the LDAP search to resolve exactly one DN, supports optional STARTTLS, and can create a local user from a configured template or new record.

Question Gate: no governed/frozen G02 question-bank package was found in the current Community19 GMVQ search.
Disposition: A1 ACTIVE / ROSTER RECONCILIATION / CANDIDATE SOURCE EVIDENCE DEEPENED / WAIT QUESTION.

## G03 MASTER_DATA — exact anchors deepened
Controlled count: 11. Exact full roster remains unrecovered. Exact historical anchors remain `product`, `uom`, `analytic` only.

New verified upstream source blobs:
- `product/models/product_category.py` = `12f3f260001b8e580f36f7c35ffabf8d8e5d203a`
- `analytic/models/analytic_plan.py` = `849677f0a6d2d24a030a87b2e2ecd165cd1a9101`
- `analytic/models/analytic_distribution_model.py` = `a9083cf1a447f69552caf03d98b190d6647dc8ea`

Static findings:
1. Product categories are hierarchical, parent-stored, recursion-protected and carry a product properties definition surface.
2. Analytic plans support company-dependent applicability, hierarchy/root semantics and dynamic plan-column synchronization through `ir.model.fields`.
3. Analytic distribution models enable automatic company checks and constrain company compatibility when distributions are applied.

Question Gate: no governed/frozen G03 question-bank package was found.
Disposition: A1 ACTIVE / VERIFIED ANCHOR DELTA / EXACT ROSTER OPEN / WAIT QUESTION.

## G04 ACCOUNT_BASE — accounting boundary deepened
Controlled count: 9. Exact nine-row roster remains unrecovered. Historical evidence only establishes that the `account` family is split between ACCOUNT_BASE and ACCOUNT_PROCESS; source prefix alone is not used to assign rows.

New verified upstream source blobs from the `account` module boundary:
- `account/models/account_lock_exception.py` = `11f8afc6112e467370d293018ec8cf9193ecc1f9`
- `account/models/account_code_mapping.py` = `6fdb13ce3caf234a5411771a7c3c7eef99a589a2`
- `account/models/account_root.py` = `5e58980e31c3a8b30480ad19fb8fe1dbe9141bb0`

Static findings:
1. Lock-date exceptions have active/revoked/expired states, are company-scoped, can be user-scoped or global, and require exactly one soft-lock date field per exception.
2. Revocation is restricted to accounting-manager/adviser authority or superuser and exception creation posts tracking evidence to company chatter; the model also constructs an audit-trail domain for changes during the exception window.
3. Account code mapping is a non-persistent UI model constrained to Chart-of-Accounts access paths and writes account codes in company context.
4. Account root is a non-persistent hierarchy derived from the first two account-code characters and restricts its supported search forms.

Question Gate: no governed/frozen G04 question-bank package was found.
Disposition: A1 ACTIVE / VERIFIED ACCOUNT BOUNDARY DELTA / EXACT ROSTER OPEN / WAIT QUESTION.

## Final gate state
- G01: A1 ACTIVE; eligible G01 frozen batches preserved; A2 NOT EXECUTED due offline runtime.
- G02: A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION.
- G03: A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION.
- G04: A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION.
- Formal Coverage remains prohibited until the Canonical Function-ID denominator is Boss-frozen.
